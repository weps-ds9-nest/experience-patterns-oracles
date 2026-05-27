"""
ingest.py — Pull clean markdown from r.jina.ai for every URL in links.csv
            and write each page to raw/<slug>.md.

Usage:
    python3 ingest.py
    uv run ingest.py
"""

import csv
import re
import sys
import time
from pathlib import Path

import requests

LINKS_FILE = Path("links.csv")
RAW_DIR    = Path("raw")
JINA_BASE  = "https://r.jina.ai"
DELAY_SEC  = 2


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "-", text).strip("-")


def fetch_markdown(url: str, session: requests.Session) -> str:
    jina_url = f"{JINA_BASE}/{url}"
    print(f"  GET {jina_url}", flush=True)
    resp = session.get(jina_url, timeout=30, headers={"Accept": "text/markdown"})
    resp.raise_for_status()
    return resp.text


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if not LINKS_FILE.exists():
        print(f"[ingest] {LINKS_FILE} not found — nothing to do.", flush=True)
        return

    with LINKS_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("[ingest] links.csv is empty — nothing to ingest.", flush=True)
        return

    print(f"[ingest] Processing {len(rows)} link(s) …", flush=True)
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
        print(f"  ✓  {out_path}  ({len(content)} chars)", flush=True)

        if i < len(rows) - 1:
            time.sleep(DELAY_SEC)

    print("[ingest] Done.", flush=True)


if __name__ == "__main__":
    main()
