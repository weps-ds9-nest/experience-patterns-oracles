# UX Pattern Oracle

A self-contained remote MCP server for consulting a curated knowledge graph of Experience and Behavioural Design Patterns. Built with **FastMCP** and **Graphifyy** — no CI/CD pipeline required.

## How it works

```
links/collections/*.csv  →  ingest.py  →  links/links.csv  (merged, deduped)
                                      →  raw/             (ingested markdown)
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
├── wiki/                         # Curated wiki entries — edit and add [[wiki-links]] here
├── graphify-out/                 # Auto-generated knowledge graph (do not edit)
│   └── graph.json
├── ingest.py                     # Merges collections + ingests markdown
├── promote_raw_to_wiki.py        # Promotes raw content to wiki using Ollama
├── update_wikilinks.py           # Updates wikilinks using semantic similarity + graphify
├── server.py                     # FastMCP server — 4 consultation tools
├── utils.py                      # Shared helper functions (validate_url, slugify, etc.)
├── DATA_MANAGEMENT.md            # Guide for local data management
└── pyproject.toml                # Dependencies and project config (uv)
```

**Note:** The `raw/` and `links/` directories have their folders tracked in git but their contents are ignored to keep the repository lightweight. See `DATA_MANAGEMENT.md` for local workflow instructions.

## Setup

Requires Python ≥ 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
# Install dependencies
uv sync
```

## Usage

### 1. Add links — Bookmark collections workflow

Export bookmarks as CSV and drop them in `links/collections/`:

```bash
links/collections/ux-patterns.csv
links/collections/cognitive-biases.csv
# ... add as many exports as you like
```

Standard bookmark export formats (with columns like `id, title, note, excerpt, url, folder, tags, created, …`) are supported natively. When you run `ingest.py`, it automatically merges all collection CSVs into `links/links.csv`, deduplicating by URL — so dropping the same export twice is safe.

You can also add links manually to `links/links.csv` using the columns:
```
id,title,url,tags,description
```

### 2. Ingest — merge collections and fetch markdown

**One-shot** (merge then fetch in a single run):
```bash
uv run python ingest.py
```

**Watch mode** (recommended — leave running in the background):
```bash
uv run python ingest.py --watch
```

In watch mode, the script:
1. Runs an **immediate startup pass** — any CSVs already in `collections/` that contain new URLs are merged into `links/links.csv` right away
2. **Watches for changes** — the moment you drop or modify a CSV in `links/collections/`, it detects the change and merges new links automatically
3. Prints how many new links were added and reminds you to run `ingest.py` (without `--watch`) to fetch the markdown

Each URL is fetched via content ingestion services with a 2-second polite delay and written to `raw/<slug>.md`.

**Content ingestion fallback services:**
For Medium domains (medium.com, uxplanet.org, etc.), the system uses a fallback chain of content ingestion services to ensure reliable retrieval even if one service is blocked or fails.

See `DATA_MANAGEMENT.md` for detailed data management instructions.

### 3. Curate — promote entries to wiki

**Auto-promote with Ollama:**
```bash
# Basic promotion
uv run python promote_raw_to_wiki.py

# Verbose mode (shows file sizes, processing time, Ollama output)
uv run python promote_raw_to_wiki.py --verbose

# Custom timeout (default 240s)
OLLAMA_TIMEOUT=300 uv run python promote_raw_to_wiki.py
```

The script now:\- Cleans ANSI escape sequences from both input and output
- Provides detailed validation error messages
- Supports configurable timeout via `OLLAMA_TIMEOUT` env var
- Logs processing metrics in verbose mode

**Manual curation:**
Copy and edit files from `raw/` into `wiki/`. Add `[[wiki-links]]` to connect related patterns.

**Update wikilinks:**
```bash
# Update all wikilinks using semantic similarity + graph relationships
uv run python update_wikilinks.py

# Preview changes without writing
uv run python update_wikilinks.py --dry-run

# Update a specific file
uv run python update_wikilinks.py --file specific-file.md

# Verbose logging
uv run python update_wikilinks.py --verbose
```

### 4. Serve

```bash
uv run python server.py
# or with a custom port:
PORT=9000 uv run python server.py
```

On first run with a populated `wiki/`, Graphifyy compiles `graphify-out/graph.json` automatically. Subsequent starts skip compilation.

The MCP server listens on `http://0.0.0.0:8000` (default).

## Deployment to Render

### Local setup with Ollama

If you have Ollama installed locally, use it for graph compilation and content promotion without API keys:

```bash
# Compile knowledge graph with Ollama
uv run graphify wiki --no-viz --backend ollama

# Auto-promote raw files to wiki (with verbose logging)
uv run python promote_raw_to_wiki.py --verbose

# Update wikilinks using semantic similarity + graph relationships
uv run python update_wikilinks.py
```

### Deploying

Render automatically detects `render.yaml` in your repository. Connect your repo to Render and it will deploy using the Dockerfile.

### Graph compilation on Render

The server attempts to compile the graph on startup:
- Tries Ollama backend first (if available in environment)
- Falls back to other LLM backends if configured
- For fastest cold starts, commit `graphify-out/graph.json` after local compilation

## Access & Usage

The UX Pattern Oracle is a **publicly accessible MCP server** designed as a free consultation service for UX and Behavioural Design Patterns.

### Public Access
- No authentication required
- Anyone with the server URL can query the knowledge graph
- Rate-limited to 60 requests per minute per IP to prevent abuse
- Intended for educational and design consultation purposes

### How to Connect
Add this MCP server to your Claude Desktop or compatible MCP client:
```
Server URL: https://your-render-app-url.onrender.com/sse
Transport: SSE (Server-Sent Events)
```

### Cost
- Free to use (no API keys required for end users)
- Hosted on Render free tier
- Knowledge graph compiled from publicly available UX design resources

## MCP Tools

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

## Data Management

The `raw/` and `links/` directories are excluded from git. See `DATA_MANAGEMENT.md` for:
- Why these are excluded (copyright, bloat, freshness)
- Local workflow for content ingestion
- How to contribute curated content to `wiki/`
