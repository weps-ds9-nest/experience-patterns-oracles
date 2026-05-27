# UX Pattern Oracle

A self-contained remote MCP server for consulting a curated knowledge graph of Experience and Behavioural Design Patterns. Built with **FastMCP** and **Graphifyy** — no CI/CD pipeline required.

## How it works

```
links.csv  →  ingest.py  →  raw/       (Jina Reader markdown)
                         →  wiki/      (curated entries)
                         →  graphify   (auto-runs on server startup)
                         →  graphify-out/graph.json
                         →  server.py  (MCP over HTTP)
```

On startup, `server.py` checks whether `graphify-out/graph.json` exists. If it doesn't, it runs `graphify ./wiki --no-viz` automatically — the server compiles its own brain before accepting any request.

## Project structure

```
experience-patterns-oracles/
├── .github/workflows/
│   └── auto-wiki-build.yml   # Optional CI fallback
├── raw/                       # Markdown fetched from r.jina.ai
├── wiki/                      # Curated wiki entries (source for the graph)
├── graphify-out/              # graph.json compiled by Graphifyy on startup
├── links.csv                  # Raindrop.io export (id, title, url, tags, description)
├── ingest.py                  # Fetch raw markdown from links.csv via r.jina.ai
├── server.py                  # FastMCP server — 4 consultation tools
└── pyproject.toml             # Dependencies and project config (uv)
```

## Setup

Requires Python ≥ 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
# Install dependencies (no package build step needed)
uv sync --no-install-project
```

## Usage

### 1. Populate links.csv

Export your Raindrop.io collection as CSV. The file expects these columns:

```
id,title,url,tags,description
```

### 2. Ingest — fetch raw markdown

```bash
uv run --no-project python ingest.py
```

Each URL is fetched via `https://r.jina.ai/{url}` with a 2-second polite delay and written to `raw/<slug>.md`.

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
