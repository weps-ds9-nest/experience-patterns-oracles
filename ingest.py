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
    uv run --no-project python ingest.py --watch
"""

import csv
import ipaddress
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

LINKS_DIR       = Path("links")
LINKS_FILE      = LINKS_DIR / "links.csv"
COLLECTIONS_DIR = LINKS_DIR / "collections"
RAW_DIR         = Path("raw")
JINA_BASE       = "https://r.jina.ai"
DELAY_SEC       = 2

FIELDNAMES = ["id", "title", "url", "tags", "description"]

_RAW_DIR_RESOLVED = RAW_DIR.resolve()

_BLOCKED_NETWORKS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),   # link-local / cloud metadata
    ipaddress.ip_network("127.0.0.0/8"),       # loopback
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
]


def _validate_url(url: str) -> None:
    """Raise ValueError if the URL is not a safe external HTTPS URL."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Blocked non-HTTP scheme: {parsed.scheme!r}")
    hostname = parsed.hostname or ""
    try:
        addr = ipaddress.ip_address(hostname)
        for net in _BLOCKED_NETWORKS:
            if addr in net:
                raise ValueError(f"Blocked private/link-local IP: {addr}")
    except ValueError as e:
        if "Blocked" in str(e):
            raise
        # Hostname is a domain name, proceed


def _safe_output_path(directory: Path, slug: str, resolved_base: Path) -> Path:
    candidate = (directory / f"{slug}.md").resolve()
    if not candidate.is_relative_to(resolved_base):
        raise ValueError(f"Slug '{slug}' escapes output directory")
    return candidate


# Maps source column names (Raindrop or our own) to our FIELDNAMES
RAINDROP_MAP = {
    "id":      "id",
    "title":   "title",
    "url":     "url",
    "tags":    "tags",
    "note":    "description",   # prefer note; fall back to excerpt
    "excerpt": "description",
}


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "-", text).strip("-")


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


def _is_bad_content(path: Path) -> bool:
    """Return True if the file is too small or contains login-wall markers."""
    if path.stat().st_size < 800:
        return True
    content = path.read_text(encoding="utf-8", errors="ignore")
    return any(marker in content for marker in BAD_CONTENT_MARKERS)


def _build_fetch_urls(url: str) -> list[tuple[str, str]]:
    """
    Return an ordered list of (fetch_url, provider) to try for this URL.
    Medium domains get specialized content ingestion services first, then fallback providers.
    All other URLs go to the default content ingestion service.
    """
    _validate_url(url)
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
    if len(text) < 800:
        return False
    return not any(marker in text for marker in BAD_CONTENT_MARKERS)


def fetch_markdown(url: str, session: requests.Session) -> str:
    """
    Try each provider in order until one returns clean content.
    Raises the last exception if all providers fail.
    """
    last_exc: Exception = RuntimeError("No providers configured")
    for fetch_url, provider in _build_fetch_urls(url):
        print(f"  GET [{provider}] {fetch_url}", flush=True)
        try:
            _validate_url(fetch_url)
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


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    LINKS_DIR.mkdir(parents=True, exist_ok=True)

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

    # Step 3 — fetch markdown for each URL not yet scraped
    print(f"[ingest] Processing {len(rows)} link(s) ...", flush=True)
    session = requests.Session()
    session.verify = True
    session.headers.update({"User-Agent": "experience-patterns-oracle/0.1"})

    for i, row in enumerate(rows):
        url   = (row.get("url") or "").strip()
        title = (row.get("title") or "").strip()

        if not url:
            print(f"  SKIP row {i + 1}: no URL", flush=True)
            continue

        try:
            _validate_url(url)
        except Exception as exc:
            print(f"  SKIP row {i + 1}: unsafe/blocked URL '{url}': {exc}", file=sys.stderr, flush=True)
            continue

        slug = slugify(title) if title else slugify(url)
        try:
            out_path = _safe_output_path(RAW_DIR, slug, _RAW_DIR_RESOLVED)
        except ValueError as exc:
            print(f"  SKIP row {i + 1}: unsafe output slug generated: {exc}", file=sys.stderr, flush=True)
            continue

        if out_path.exists():
            if not _is_bad_content(out_path):
                print(f"  SKIP {slug}.md ({out_path.stat().st_size} bytes)", flush=True)
                continue
            print(f"  RE-FETCH {slug}.md (login wall or bad content detected)", flush=True)

        try:
            content = fetch_markdown(url, session)
        except Exception as exc:
            print(f"  WARN: could not fetch '{url}': {exc}", file=sys.stderr, flush=True)
            continue

        out_path.write_text(content, encoding="utf-8")
        print(f"  +  {out_path}  ({len(content)} chars)", flush=True)

        if i < len(rows) - 1:
            time.sleep(DELAY_SEC)

    print("[ingest] Done.", flush=True)


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
            "[watch] 'watchfiles' not installed — run: uv sync --no-install-project",
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
