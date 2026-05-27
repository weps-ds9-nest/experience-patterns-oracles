"""
ingest.py — Pull clean markdown from r.jina.ai for every URL in links/links.csv
            and write each page to raw/<slug>.md.

Collection merge
----------------
Before ingesting, any new CSV files dropped in links/collections/ are
automatically merged into links/links.csv.  Raindrop.io export format is
supported natively (id, title, note, excerpt, url, folder, tags, created, ...).
Rows are deduplicated by URL so merging the same export twice is safe.

Usage:
    python3 ingest.py
    uv run --no-project python ingest.py
"""

import csv
import re
import sys
import time
from pathlib import Path

import requests

LINKS_DIR       = Path("links")
LINKS_FILE      = LINKS_DIR / "links.csv"
COLLECTIONS_DIR = LINKS_DIR / "collections"
RAW_DIR         = Path("raw")
JINA_BASE       = "https://r.jina.ai"
DELAY_SEC       = 2

FIELDNAMES = ["id", "title", "url", "tags", "description"]

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


def fetch_markdown(url: str, session: requests.Session) -> str:
    jina_url = f"{JINA_BASE}/{url}"
    print(f"  GET {jina_url}", flush=True)
    resp = session.get(jina_url, timeout=30, headers={"Accept": "text/markdown"})
    resp.raise_for_status()
    return resp.text


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
    session.headers.update({"User-Agent": "experience-patterns-oracle/0.1"})

    for i, row in enumerate(rows):
        url   = (row.get("url") or "").strip()
        title = (row.get("title") or "").strip()

        if not url:
            print(f"  SKIP row {i + 1}: no URL", flush=True)
            continue

        slug     = slugify(title) if title else slugify(url)
        out_path = RAW_DIR / f"{slug}.md"

        if out_path.exists():
            print(f"  SKIP {slug}.md (already exists)", flush=True)
            continue

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


if __name__ == "__main__":
    main()
