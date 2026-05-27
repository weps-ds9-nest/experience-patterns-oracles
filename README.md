# UX Pattern Oracle

A self-contained remote MCP server for consulting a curated knowledge graph of Experience and Behavioural Design Patterns. Built with **FastMCP** and **Graphifyy** — no CI/CD pipeline required.

## How it works

```
links/collections/*.csv  →  ingest.py  →  links/links.csv  (merged, deduped)
                                      →  raw/             (Jina Reader markdown)
                                      →  wiki/            (curated entries)
                                      →  graphify         (auto-runs on startup)
                                      →  graphify-out/graph.json
                                      →  server.py        (MCP over HTTP)
```

On startup, `server.py` checks whether `graphify-out/graph.json` exists. If it doesn't, it runs `graphify ./wiki --no-viz` automatically — the server compiles its own brain before accepting any request.

## Project structure

```
experience-patterns-oracles/
├── .github/
│   ├── copilot-instructions.md   # Copilot agent instructions for this repo
│   └── workflows/auto-wiki-build.yml
├── links/
│   ├── links.csv                 # Master URL list (id, title, url, tags, description)
│   └── collections/              # Drop Raindrop CSV exports here
├── raw/                          # Auto-generated markdown from r.jina.ai (do not edit)
├── wiki/                         # Curated wiki entries — edit and add [[wiki-links]] here
├── graphify-out/                 # Auto-generated knowledge graph (do not edit)
│   └── graph.json
├── ingest.py                     # Merges collections + fetches markdown
├── server.py                     # FastMCP server — 4 consultation tools
└── pyproject.toml                # Dependencies and project config (uv)
```

## Setup

Requires Python ≥ 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
# Install dependencies (no package build step needed)
uv sync --no-install-project
```

## Usage

### 1. Add links — Raindrop.io collections workflow

Export any Raindrop collection as CSV and drop it in `links/collections/`:

```bash
links/collections/ux-patterns.csv
links/collections/cognitive-biases.csv
# ... add as many exports as you like
```

Raindrop's export format (`id, title, note, excerpt, url, folder, tags, created, …`) is supported natively. When you run `ingest.py`, it automatically merges all collection CSVs into `links/links.csv`, deduplicating by URL — so dropping the same export twice is safe.

You can also add links manually to `links/links.csv` using the columns:
```
id,title,url,tags,description
```

### 2. Ingest — merge collections and fetch markdown

```bash
uv run --no-project python ingest.py
```

This runs in two steps:
1. **Merge** — all CSVs in `links/collections/` are merged into `links/links.csv`
2. **Fetch** — each URL not yet in `raw/` is fetched via `https://r.jina.ai/{url}` with a 2-second polite delay and written to `raw/<slug>.md`

### 3. Curate — promote entries to wiki

Copy and edit files from `raw/` into `wiki/`. Add `[[wiki-links]]` to connect related patterns.

### 4. Serve

```bash
uv run --no-project python server.py
# or with a custom port:
PORT=9000 uv run --no-project python server.py
```

On first run with a populated `wiki/`, Graphifyy compiles `graphify-out/graph.json` automatically. Subsequent starts skip compilation.

The MCP server listens on `http://0.0.0.0:8000` (default).

## MCP tools

| Tool | Description |
|---|---|
| `ask_ux_oracle(query)` | Full-text + semantic search across the pattern graph |
| `get_pattern_psychology(pattern_name)` | Cognitive/psychological links for a pattern |
| `generate_design_spec(pattern_name, target_platform)` | Platform-specific design spec scaffold |
| `predict_component_states(component_name)` | Predict UI states from graph neighbours |

## Dependencies

| Package | Role |
|---|---|
| `fastmcp` | MCP server framework |
| `graphifyy` | Knowledge graph compiler (runs on startup) |
| `requests` | HTTP client for `ingest.py` |
| `uvicorn` | ASGI server for HTTP transport |
| `httpx` | HTTP engine for FastMCP transport layer |
| `anyio` | Async I/O compatibility |
