"""
ingest.py — Ingest and process markdown content for every URL in links/links.csv
            and write each page to raw/<slug>.md.

Collection merge
----------------
Before ingesting, any new CSV files dropped in links/collections/ are
automatically merged into links/links.csv.  Raindrop.io export format is
supported natively (id, title, note, excerpt, url, folder, tags, created, ...).
Rows are deduplicated by URL so merging the same export twice is safe.

Usage:
    python3 ingest.py              # one-shot: merge collections then fetch
    python3 ingest.py --watch      # daemon: auto-merge on CSV add/modify
    uv run python ingest.py --watch
"""

import argparse
import csv
import os
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

from utils import safe_output_path, slugify, validate_url

LINKS_DIR       = Path("links")
LINKS_FILE      = LINKS_DIR / "links.csv"
COLLECTIONS_DIR = LINKS_DIR / "collections"
RAW_DIR         = Path("raw")
JINA_BASE       = "https://r.jina.ai"
DELAY_SEC       = 2

# Configurable minimum content character threshold
MIN_CONTENT_CHARS = int(os.getenv("MIN_CONTENT_CHARS", "400"))

# Validate threshold
MIN_CONTENT_CHARS = max(200, min(5000, MIN_CONTENT_CHARS))

FIELDNAMES = ["id", "title", "url", "tags", "description"]

_RAW_DIR_RESOLVED = RAW_DIR.resolve()


# Maps source column names (Raindrop or our own) to our FIELDNAMES
RAINDROP_MAP = {
    "id":      "id",
    "title":   "title",
    "url":     "url",
    "tags":    "tags",
    "note":    "description",   # prefer note; fall back to excerpt
    "excerpt": "description",
}


def _read_links_csv() -> tuple[list[dict], set[str]]:
    """Return (rows, seen_urls) from the master links.csv."""
    if not LINKS_FILE.exists():
        return [], set()
    with LINKS_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    seen = {(r.get("url") or "").strip() for r in rows if r.get("url")}
    return rows, seen


def _write_links_csv(rows: list[dict]) -> None:
    LINKS_DIR.mkdir(parents=True, exist_ok=True)
    with LINKS_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _normalise_row(raw: dict) -> dict:
    """Map any supported CSV schema to our internal FIELDNAMES schema."""
    fields = {k.lower().strip(): v for k, v in raw.items()}

    # Already in our format?
    if "url" in fields and set(fields.keys()).issubset(set(FIELDNAMES)):
        return {k: fields.get(k, "") for k in FIELDNAMES}

    # Raindrop.io or unknown format — map what we can
    row: dict = {k: "" for k in FIELDNAMES}
    for src, dst in RAINDROP_MAP.items():
        val = (fields.get(src) or "").strip()
        if val and not row[dst]:   # don't overwrite a value already set
            row[dst] = val
    return row


def merge_collections() -> int:
    """
    Scan links/collections/*.csv, extract all URLs not already in
    links/links.csv, and append them.  Returns the count of new rows added.
    """
    if not COLLECTIONS_DIR.exists():
        return 0

    collection_files = sorted(COLLECTIONS_DIR.glob("*.csv"))
    if not collection_files:
        return 0

    existing_rows, seen_urls = _read_links_csv()
    new_rows: list[dict] = []

    for csv_path in collection_files:
        print(f"[merge] Reading collection: {csv_path.name}", flush=True)
        added_from_file = 0
        try:
            # utf-8-sig handles the BOM that Excel/Raindrop sometimes adds
            with csv_path.open(newline="", encoding="utf-8-sig") as f:
                for raw in csv.DictReader(f):
                    row = _normalise_row(raw)
                    url = (row.get("url") or "").strip()
                    if not url or url in seen_urls:
                        continue
                    seen_urls.add(url)
                    new_rows.append(row)
                    added_from_file += 1
        except Exception as exc:
            print(f"  WARN: could not read {csv_path.name}: {exc}", file=sys.stderr, flush=True)
            continue
        print(f"  + {added_from_file} new link(s) from {csv_path.name}", flush=True)

    if new_rows:
        _write_links_csv(existing_rows + new_rows)
        print(f"[merge] {len(new_rows)} total new link(s) written to {LINKS_FILE}", flush=True)
    else:
        print("[merge] No new links found in collections.", flush=True)

    return len(new_rows)


# Domains that block Jina Reader — routed through Freedium/12ft instead.
# Includes Medium's own domain, all known Medium publications, and custom
# domains that host Medium content (identified by their article hash URL suffix).
MEDIUM_DOMAINS = {
    "medium.com",
    "uxdesign.cc",
    "uxplanet.org",
    "bootcamp.uxdesign.cc",
    "towardsdatascience.com",
    "betterprogramming.pub",
    "levelup.gitconnected.com",
    "medium.muz.li",
    "blog.appliedinnovationexchange.com",
    "uxknowledgebase.com",
    "designsystemscollective.com",
}

# Blocked domains to prevent SSRF attacks
# Internal/private domains that should never be fetched
BLOCKED_DOMAINS = {
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    # Cloud metadata endpoints
    "169.254.169.254",
    "metadata.google.internal",
    # Internal network ranges (common patterns)
    "10.0.0.0",
    "172.16.0.0",
    "192.168.0.0",
}

# Content markers that indicate a login wall or anti-bot intercept page.
# Size alone is not reliable — some paywall pages are thousands of bytes.
BAD_CONTENT_MARKERS = (
    # Medium login walls
    "Member-only story",
    "medium.com/m/signin",
    "Open in app",
    "Get unlimited access",
    "to continue reading",
    "Sign up to read",
    # Cloudflare CAPTCHA / challenge pages
    "Just a moment",
    # Generic HTTP error pages
    "Page Not Found",
)


def _is_blocked_domain(url: str) -> bool:
    """Check if URL contains a blocked domain to prevent SSRF attacks."""
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    if not hostname:
        return True  # Block URLs without hostname

    # Check exact matches
    if hostname in BLOCKED_DOMAINS:
        return True

    # Check if hostname starts with any blocked network prefix
    for blocked in BLOCKED_DOMAINS:
        if hostname.startswith(blocked):
            return True

    return False


def _is_bad_content(path: Path) -> bool:
    """Return True if the file is too small or contains login-wall markers."""
    if path.stat().st_size < MIN_CONTENT_CHARS:
        return True
    content = path.read_text(encoding="utf-8", errors="ignore")
    return any(marker in content for marker in BAD_CONTENT_MARKERS)


def _build_fetch_urls(url: str) -> list[tuple[str, str]]:
    """
    Return an ordered list of (fetch_url, provider) to try for this URL.
    Medium domains get specialized content ingestion services first, then fallback providers.
    All other URLs go to the default content ingestion service.
    """
    domain = urlparse(url).netloc.lstrip("www.")
    if any(domain == d or domain.endswith("." + d) for d in MEDIUM_DOMAINS):
        return [
            (f"https://freedium.cfd/{url}",          "fallback-1"),
            (f"{JINA_BASE}/https://smry.ai/{url}",   "fallback-2"),
            (f"{JINA_BASE}/{url}",                   "default"),
        ]
    return [(f"{JINA_BASE}/{url}", "default")]


def _content_is_clean(text: str) -> bool:
    """
    Return True if the fetched text looks like real article content.
    Checks both minimum length (short = error/login page) and known bad markers.
    """
    if len(text) < MIN_CONTENT_CHARS:
        return False
    return not any(marker in text for marker in BAD_CONTENT_MARKERS)


def fetch_markdown(url: str, session: requests.Session) -> str:
    """
    Try each provider in order until one returns clean content.
    Raises the last exception if all providers fail.
    """
    # SSRF protection: check original URL and all fetch URLs
    if _is_blocked_domain(url):
        raise ValueError(f"Blocked domain in original URL: {url}")

    last_exc: Exception = RuntimeError("No providers configured")
    for fetch_url, provider in _build_fetch_urls(url):
        # SSRF protection: check each fetch URL
        if _is_blocked_domain(fetch_url):
            print(f"  [{provider}] blocked by SSRF protection — skipping", flush=True)
            last_exc = ValueError(f"{provider} blocked by SSRF protection")
            continue

        print(f"  GET [{provider}] {fetch_url}", flush=True)
        try:
            validate_url(fetch_url)
            resp = session.get(fetch_url, timeout=30, headers={"Accept": "text/markdown"})
            resp.raise_for_status()
            text = resp.text
            if _content_is_clean(text):
                return text
            print(f"  [{provider}] returned login wall — trying next provider", flush=True)
            last_exc = ValueError(f"{provider} returned login-wall content")
        except Exception as exc:
            print(f"  [{provider}] failed: {exc}", flush=True)
            last_exc = exc
    raise last_exc


def _get_wiki_slugs() -> set[str]:
    """Get all slugs (filenames without .md) from wiki/ for resume functionality."""
    wiki_dir = Path("wiki")
    if not wiki_dir.exists():
        return set()
    return {f.stem for f in wiki_dir.glob("*.md") if f.name != ".gitkeep"}


def _analyze_raw_directory() -> None:
    """Analyze the raw/ directory and show file size distribution."""
    if not RAW_DIR.exists():
        print("[analyze] raw/ directory does not exist.", flush=True)
        return

    files = list(RAW_DIR.glob("*.md"))
    files = [f for f in files if f.name != ".gitkeep"]
    
    if not files:
        print("[analyze] No markdown files found in raw/.", flush=True)
        return

    sizes = [f.stat().st_size for f in files]
    total_size = sum(sizes)
    avg_size = total_size / len(files) if files else 0

    # Count files at different thresholds
    thresholds = [200, 400, 600, 800, 1000, 2000, 5000]
    distribution = {}
    for threshold in thresholds:
        count = sum(1 for s in sizes if s < threshold)
        distribution[threshold] = count

    print(f"[analyze] Total files: {len(files)}", flush=True)
    print(f"[analyze] Total size: {total_size:,} bytes ({total_size / 1024 / 1024:.2f} MB)", flush=True)
    print(f"[analyze] Average size: {avg_size:.0f} bytes", flush=True)
    print(f"[analyze] Size distribution (files under threshold):", flush=True)
    for threshold in thresholds:
        print(f"  < {threshold:4d} chars: {distribution[threshold]:3d} files", flush=True)
    print(f"[analyze] Files >= {thresholds[-1]} chars: {len(files) - distribution[thresholds[-1]]} files", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest markdown content from URLs")
    parser.add_argument("--batch-size", type=int, default=10, help="Number of files to process per batch")
    parser.add_argument("--batch-delay", type=int, default=0, help="Delay in seconds between batches")
    parser.add_argument("--resume", action="store_true", help="Skip files already in wiki/")
    parser.add_argument("--dry-run", action="store_true", help="Preview what would be fetched without actually fetching")
    parser.add_argument("--analyze", action="store_true", help="Analyze raw/ directory file size distribution")
    args = parser.parse_args()

    # Handle analyze mode (standalone)
    if args.analyze:
        _analyze_raw_directory()
        return

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    LINKS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[ingest] Using MIN_CONTENT_CHARS={MIN_CONTENT_CHARS}", flush=True)
    if args.dry_run:
        print(f"[ingest] DRY RUN MODE - no files will be fetched or written", flush=True)
    if args.resume:
        print(f"[ingest] Resume mode: will skip files already in wiki/", flush=True)
    if args.batch_size > 0:
        print(f"[ingest] Batch mode: {args.batch_size} files per batch", flush=True)
    if args.batch_delay > 0:
        print(f"[ingest] Batch delay: {args.batch_delay}s between batches", flush=True)

    # Step 1 — merge any new Raindrop collection exports into links/links.csv
    merge_collections()

    # Step 2 — read master links.csv
    if not LINKS_FILE.exists():
        print(f"[ingest] {LINKS_FILE} not found — nothing to do.", flush=True)
        return

    with LINKS_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("[ingest] links.csv is empty — nothing to ingest.", flush=True)
        return

    # Get wiki slugs for resume mode
    wiki_slugs = _get_wiki_slugs() if args.resume else set()

    # Step 3 — fetch markdown for each URL not yet scraped
    print(f"[ingest] Processing {len(rows)} link(s) ...", flush=True)
    session = requests.Session()
    session.verify = True
    session.headers.update({"User-Agent": "experience-patterns-oracle/0.1"})

    processed_count = 0
    skipped_count = 0

    for i, row in enumerate(rows):
        url   = (row.get("url") or "").strip()
        title = (row.get("title") or "").strip()

        if not url:
            print(f"  SKIP row {i + 1}: no URL", flush=True)
            skipped_count += 1
            continue

        try:
            validate_url(url)
        except Exception as exc:
            print(f"  SKIP row {i + 1}: unsafe/blocked URL '{url}': {exc}", file=sys.stderr, flush=True)
            skipped_count += 1
            continue

        slug = slugify(title) if title else slugify(url)
        
        # Skip if already in wiki (resume mode)
        if args.resume and slug in wiki_slugs:
            print(f"  SKIP {slug}.md (already in wiki/)", flush=True)
            skipped_count += 1
            continue

        try:
            out_path = safe_output_path(RAW_DIR, slug, _RAW_DIR_RESOLVED)
        except ValueError as exc:
            print(f"  SKIP row {i + 1}: unsafe output slug generated: {exc}", file=sys.stderr, flush=True)
            skipped_count += 1
            continue

        if out_path.exists():
            if not _is_bad_content(out_path):
                print(f"  SKIP {slug}.md ({out_path.stat().st_size} bytes)", flush=True)
                skipped_count += 1
                continue
            print(f"  RE-FETCH {slug}.md (login wall or bad content detected)", flush=True)

        try:
            content = fetch_markdown(url, session)
        except Exception as exc:
            print(f"  WARN: could not fetch '{url}': {exc}", file=sys.stderr, flush=True)
            skipped_count += 1
            continue

        if args.dry_run:
            print(f"  [dry-run] Would write {out_path} ({len(content)} chars)", flush=True)
            processed_count += 1
        else:
            out_path.write_text(content, encoding="utf-8")
            print(f"  +  {out_path}  ({len(content)} chars)", flush=True)
            processed_count += 1

        # Batch delay
        if args.batch_size > 0 and processed_count % args.batch_size == 0 and i < len(rows) - 1:
            print(f"[ingest] Batch complete ({processed_count} processed). Pausing for {args.batch_delay}s...", flush=True)
            time.sleep(args.batch_delay)
        elif i < len(rows) - 1:
            time.sleep(DELAY_SEC)

    print(f"[ingest] Done. Processed: {processed_count}, Skipped: {skipped_count}", flush=True)


def watch_mode() -> None:
    """
    Watch links/collections/ for added or modified CSV files and immediately
    merge any new links into links/links.csv.

    On startup, runs an initial merge pass so any files already in collections/
    that haven't been processed yet are caught before the watch loop begins.
    """
    try:
        from watchfiles import Change, watch
    except ImportError:
        print(
            "[watch] 'watchfiles' not installed — run: uv sync",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(1)

    COLLECTIONS_DIR.mkdir(parents=True, exist_ok=True)

    # --- startup pass: catch anything already sitting in collections/ ---
    print("[watch] Startup: checking collections for unprocessed links …", flush=True)
    initial = merge_collections()
    if initial:
        print(f"[watch] Startup: added {initial} link(s) from existing files.", flush=True)
    else:
        print("[watch] Startup: nothing new found.", flush=True)

    print(f"[watch] Watching {COLLECTIONS_DIR} — drop a CSV any time (Ctrl+C to stop)", flush=True)

    for changes in watch(str(COLLECTIONS_DIR)):
        # Only react to added or modified CSVs, ignore deletes and non-CSV files
        relevant = {
            Path(path)
            for change_type, path in changes
            if path.endswith(".csv") and change_type in (Change.added, Change.modified)
        }
        if not relevant:
            continue

        for p in sorted(relevant):
            print(f"[watch] Detected {p.name} ({p.stat().st_size} bytes)", flush=True)

        added = merge_collections()
        if added:
            print(f"[watch] + {added} new link(s) written to {LINKS_FILE}", flush=True)
            print("[watch] Run 'python ingest.py' to fetch markdown for the new links.", flush=True)
        else:
            print("[watch] No new links found (all URLs already in links.csv).", flush=True)

        print(f"[watch] Watching {COLLECTIONS_DIR} …", flush=True)


if __name__ == "__main__":
    if "--watch" in sys.argv:
        watch_mode()
    else:
        main()
