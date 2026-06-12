"""
update_wikilinks.py — Update wikilinks in wiki/ files using graph-based linking (LLM-free by default)

This script updates the ## Related section in wiki files by:
1. Using graphify-out/graph.json to find structurally connected nodes (default, no LLM)
2. Leveraging graph topology, neighbors, and paths for suggestions
3. Optionally using semantic similarity via Ollama when explicitly requested

Usage:
    uv run python update_wikilinks.py              # Update all wikilinks (graph-based, no LLM)
    uv run python update_wikilinks.py --use-semantic  # Opt-in: Add semantic similarity via Ollama
    uv run python update_wikilinks.py --dry-run    # Preview changes
    uv run python update_wikilinks.py --file specific-file.md  # Update single file
    uv run python update_wikilinks.py --verbose    # Verbose logging
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from utils import slugify

WIKI_DIR = Path("wiki")
GRAPH_FILE = Path("graphify-out") / "graph.json"

_WIKI_DIR_RESOLVED = WIKI_DIR.resolve()


def _ollama_available() -> bool:
    """Check if Ollama is available locally."""
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            timeout=2,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def _get_wiki_slugs() -> set[str]:
    """Get all slugs (filenames without .md) from wiki/."""
    if not WIKI_DIR.exists():
        return set()
    return {f.stem for f in WIKI_DIR.glob("*.md") if f.name != ".gitkeep"}


def _load_graph() -> dict[str, Any]:
    """Load the knowledge graph from graphify-out/graph.json."""
    if not GRAPH_FILE.exists():
        print("[update] WARN: graph.json not found. Graph-based linking disabled.", flush=True)
        return {}
    try:
        with GRAPH_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[update] WARN: Could not load graph.json: {e}", flush=True)
        return {}


def _get_graph_neighbors(graph: dict, node_id: str) -> list[str]:
    """Get neighbor node IDs for a given node in the graph."""
    if not graph:
        return []
    
    nodes = graph.get("nodes", [])
    links = graph.get("links", graph.get("edges", []))
    
    neighbor_ids: set[str] = set()
    for link in links:
        if link.get("source") == node_id:
            neighbor_ids.add(str(link["target"]))
        elif link.get("target") == node_id:
            neighbor_ids.add(str(link["source"]))
    
    # Map IDs to norm_labels (slugs)
    id_to_slug = {str(n["id"]): n.get("norm_label", "") for n in nodes}
    return [id_to_slug[i] for i in neighbor_ids if i in id_to_slug and id_to_slug[i]]


def _extract_wiki_content(wiki_path: Path) -> tuple[str, str]:
    """Extract title and content from a wiki file."""
    content = wiki_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    # Extract title (first heading)
    title = ""
    for line in lines:
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            break
    
    # Extract content (everything after ## Content or ## Full Article)
    content_start = None
    for i, line in enumerate(lines):
        if line.startswith("## Content") or line.startswith("## Full Article"):
            content_start = i + 1
            break
    
    if content_start:
        body = "\n".join(lines[content_start:])
    else:
        body = content
    
    return title, body


def _call_ollama_for_related(content: str, existing_slugs: set[str], top_k: int = 5) -> list[str]:
    """Use Ollama to find semantically related wiki entries."""
    slug_list = sorted(existing_slugs)
    
    prompt = f"""You are helping to find related UX patterns for a wiki entry.

Below is the content of a wiki entry. Identify which of these existing wiki slugs are most semantically related to this content.

Existing wiki slugs:
{', '.join(slug_list[:50])}

Wiki content:
{content[:2000]}

Return ONLY a comma-separated list of the top {top_k} most related slugs. Do not include any other text.
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            # Parse comma-separated list
            suggested = [s.strip() for s in output.split(",") if s.strip()]
            # Filter to only existing slugs
            valid = [s for s in suggested if s in existing_slugs]
            return valid[:top_k]
    except Exception as e:
        print(f"[ollama] Error: {e}", file=sys.stderr, flush=True)
    
    return []


def _extract_existing_links(content: str) -> set[str]:
    """Extract existing wikilinks from the ## Related section."""
    lines = content.split("\n")
    in_related = False
    links: set[str] = set()
    
    for line in lines:
        if line.startswith("## Related"):
            in_related = True
            continue
        if in_related and line.startswith("##"):
            break
        if in_related:
            # Extract [[wiki-link]] patterns
            matches = re.findall(r'\[\[([^\]]+)\]\]', line)
            links.update(matches)
    
    return links


def _update_related_section(content: str, new_links: list[str]) -> str:
    """Update the ## Related section with new wikilinks."""
    lines = content.split("\n")
    output = []
    in_related = False
    related_start = -1
    related_end = -1
    
    for i, line in enumerate(lines):
        if line.startswith("## Related"):
            in_related = True
            related_start = i
            output.append(line)
            continue
        if in_related and line.startswith("##"):
            in_related = False
            related_end = i
            break
        if in_related:
            continue  # Skip old related section
        output.append(line)
    
    # Insert new related section
    if related_start >= 0:
        # Insert after the ## Related line
        insert_pos = related_start + 1
        new_section = "\n".join(f"[[{link}]]" for link in new_links)
        output.insert(insert_pos, new_section)
    else:
        # Add new ## Related section at the end
        output.append("\n## Related")
        new_section = "\n".join(f"[[{link}]]" for link in new_links)
        output.append(new_section)
    
    return "\n".join(output)


def _process_file(wiki_path: Path, graph: dict, wiki_slugs: set[str], dry_run: bool, verbose: bool, use_semantic: bool = False) -> None:
    """Process a single wiki file to update its wikilinks."""
    title, content = _extract_wiki_content(wiki_path)
    existing_links = _extract_existing_links(content)
    
    if verbose:
        print(f"  [file] {wiki_path.name}", flush=True)
        print(f"  [title] {title}", flush=True)
        print(f"  [existing] {len(existing_links)} links: {', '.join(sorted(existing_links))}", flush=True)
    
    # Get graph-based neighbors (primary method)
    node_slug = wiki_path.stem
    graph_neighbors = _get_graph_neighbors(graph, node_slug)
    
    if verbose and graph_neighbors:
        print(f"  [graph] {len(graph_neighbors)} neighbors from graphify", flush=True)
    
    # Get semantic matches from Ollama (opt-in only)
    semantic_matches = []
    if use_semantic and _ollama_available():
        _, body = _extract_wiki_content(wiki_path)
        semantic_matches = _call_ollama_for_related(body, wiki_slugs, top_k=5)
        if verbose:
            print(f"  [semantic] {len(semantic_matches)} matches from Ollama", flush=True)
    
    # Combine and deduplicate, prioritizing graph neighbors
    combined = set(graph_neighbors)
    combined.update(semantic_matches)
    
    # Remove self-reference and existing links
    combined.discard(node_slug)
    combined -= existing_links
    
    # Filter to only existing wiki files
    valid_links = [link for link in combined if link in wiki_slugs]
    
    # Limit to top 7
    valid_links = sorted(valid_links)[:7]
    
    if verbose:
        print(f"  [suggested] {len(valid_links)} new links: {', '.join(valid_links)}", flush=True)
    
    if not valid_links:
        print(f"  ✓ No new links to add", flush=True)
        return
    
    # Update content
    new_content = _update_related_section(content, valid_links)
    
    if dry_run:
        print(f"  [dry-run] Would add: {', '.join(valid_links)}", flush=True)
    else:
        wiki_path.write_text(new_content, encoding="utf-8")
        print(f"  ✓ Updated {wiki_path.name} with {len(valid_links)} new links", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Update wikilinks in wiki files (graph-based by default)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--file", type=str, help="Update only this specific file")
    parser.add_argument("--use-semantic", action="store_true", help="Opt-in: Add semantic similarity via Ollama")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
    args = parser.parse_args()
    
    if args.verbose:
        print("[update] Verbose mode enabled", flush=True)
    
    if args.use_semantic:
        print("[update] Enhanced mode: using semantic similarity via Ollama (opt-in)", flush=True)
        if not _ollama_available():
            print("[update] ERROR: Ollama is not available. Install and start Ollama first, or run without --use-semantic for graph-only mode.", file=sys.stderr, flush=True)
            sys.exit(1)
    else:
        print("[update] Graph-based mode: using graph topology only (no LLM required)", flush=True)
    
    # Check prerequisites
    wiki_slugs = _get_wiki_slugs()
    if not wiki_slugs:
        print("[update] ERROR: No wiki files found.", file=sys.stderr, flush=True)
        sys.exit(1)
    
    graph = _load_graph()
    
    if args.verbose:
        print(f"[update] Wiki files: {len(wiki_slugs)}", flush=True)
        print(f"[update] Graph loaded: {bool(graph)}", flush=True)
        if args.use_semantic:
            print(f"[update] Ollama available: {_ollama_available()}", flush=True)
    
    # Determine files to process
    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"[update] ERROR: File not found: {args.file}", file=sys.stderr, flush=True)
            sys.exit(1)
        files_to_process = [file_path]
    else:
        files_to_process = sorted(WIKI_DIR.glob("*.md"))
        files_to_process = [f for f in files_to_process if f.name != ".gitkeep"]
    
    print(f"[update] Processing {len(files_to_process)} file(s)...", flush=True)
    if args.dry_run:
        print("[update] DRY RUN MODE - no changes will be written", flush=True)
    
    for wiki_path in files_to_process:
        try:
            _process_file(wiki_path, graph, wiki_slugs, args.dry_run, args.verbose, args.use_semantic)
        except Exception as e:
            print(f"  ✗ Error processing {wiki_path.name}: {e}", file=sys.stderr, flush=True)
    
    print(f"\n[update] Done.", flush=True)


if __name__ == "__main__":
    main()
