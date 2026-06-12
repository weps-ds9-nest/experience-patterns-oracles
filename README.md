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

On startup, `server.py` checks whether `graphify-out/graph.json` exists. If it doesn't, it runs `graphify ./wiki --no-viz` automatically using Graphify's native Tree-sitter extraction and Leiden clustering — the server compiles its own brain before accepting any request. No LLM or API keys required.

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

**IMPORTANT:** This is a NON RAG-FIRST MCP. The default graph compilation works without any LLM or API keys. LLM usage is opt-in only.

## Usage

**Working Directory:** All commands below assume you are in the `experience-patterns-oracles/` directory. If you're in the parent directory, first run:
```bash
cd experience-patterns-oracles
```

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

**Lightweight promotion (default, no LLM required):**
```bash
# Basic promotion - direct copy with basic structure
uv run python promote_raw_to_wiki.py

# Verbose mode (shows file sizes, processing time)
uv run python promote_raw_to_wiki.py --verbose
```

**Manual curation:**
Copy and edit files from `raw/` into `wiki/`. Add `[[wiki-links]]` to connect related patterns.

**Update wikilinks (graph-based, no LLM):**
```bash
# Update all wikilinks using graph topology
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

On first run with a populated `wiki/`, the server compiles `graphify-out/graph.json` automatically. If no LLM API key is configured, it falls back to basic graph generation (no LLM required). Subsequent starts skip compilation.

The MCP server listens on `http://0.0.0.0:8000` (default).

## Complete Ingest & Curation Workflow

This section explains the end-to-end process from adding new URLs to having a fully functional knowledge graph.

### Overview

```
URLs → Ingest → Curate → Graph Compilation → Serve
```

### Step 1: Add URLs (Optional)

**Option A - Bookmark Collections:**
Export bookmarks as CSV and drop in `links/collections/`:
```bash
links/collections/ux-patterns.csv
links/collections/cognitive-biases.csv
```

**Option B - Manual Addition:**
Add rows directly to `links/links.csv` with columns: `id, title, url, tags, description`

### Step 2: Ingest Content

**One-shot mode** (merge collections then fetch):
```bash
uv run python ingest.py
```

**Watch mode** (recommended for development):
```bash
uv run python ingest.py --watch
```

This step:
- Merges all CSVs from `links/collections/` into `links/links.csv` (deduplicated by URL)
- Fetches markdown content for new URLs via content ingestion services
- Writes content to `raw/<slug>.md` with 2-second polite delay between requests

### Step 3: Curate Content

**Manual Curation:**
1. Review files in `raw/`
2. Edit and improve content
3. Copy curated files to `wiki/`
4. Add `[[wiki-links]]` to connect related patterns

**Lightweight Promotion** (default, no LLM):
```bash
uv run python promote_raw_to_wiki.py --verbose
```

**Update Wikilinks** (recommended, graph-based):
```bash
uv run python update_wikilinks.py
```

### Step 4: Compile Knowledge Graph

**Automatic compilation:**
The server automatically compiles `graphify-out/graph.json` on startup using Graphify's native Tree-sitter extraction and Leiden clustering. No LLM required.

**Manual compilation** (optional):
```bash
# Native extraction (no LLM required)
uv run graphify update wiki
```

### Step 5: Serve

```bash
uv run python server.py
# or with custom port:
PORT=9000 uv run python server.py
```

The MCP server will be available at `http://0.0.0.0:8000` (default).

### What Gets Committed to Git

- ✅ `wiki/` - Curated markdown entries
- ✅ `graphify-out/graph.json` - Compiled knowledge graph (recommended for faster deployment)
- ❌ `raw/` - Ingested content (local only)
- ❌ `links/` - URL collections (local only)

### Troubleshooting

**Ingest fails for specific URLs:**
- Some domains block content ingestion services
- The system uses fallback services for Medium domains
- Check terminal output for `[provider] failed` messages

**Graph compilation is slow:**
- Commit `graphify-out/graph.json` after local compilation
- This avoids recompilation on deployment

**Wiki links not working:**
- Run `uv run python update_wikilinks.py` to refresh connections
- Ensure wikilinks use format: `[[pattern-name]]`

## Optional: LLM Backend for Enhanced Processing

For enhanced semantic relationships and summarization, you can opt-in to LLM-based features:

### Enhanced Graph Compilation
```bash
# Set in .env:
GRAPHIFY_USE_LLM=true
GRAPHIFY_BACKEND=ollama
GRAPHIFY_MODEL=llama3:latest

# Then start the server
uv run python server.py
```

### Enhanced Content Promotion
```bash
# Opt-in to Ollama summarization during promotion
uv run python promote_raw_to_wiki.py --use-llm --verbose

# Custom timeout (default 240s)
OLLAMA_TIMEOUT=300 uv run python promote_raw_to_wiki.py --use-llm
```

### Enhanced Wikilink Updates
```bash
# Add semantic similarity to graph-based linking
uv run python update_wikilinks.py --use-semantic --verbose
```

**Note:** All LLM features are optional. The default workflow uses Graphify's native Tree-sitter extraction and Leiden clustering without any LLM or API keys.

## Deployment to Render

### Local development (no LLM required)

```bash
# Compile knowledge graph using native extraction
uv run graphify update wiki

# Promote raw files to wiki (lightweight mode)
uv run python promote_raw_to_wiki.py --verbose

# Update wikilinks using graph topology
uv run python update_wikilinks.py
```

### Optional: Enhanced Local Development with LLM

For enhanced semantic graphs and summarization, you can opt-in to Ollama:

```bash
# Install optional LLM dependencies
uv sync --group dev

# Set in .env:
GRAPHIFY_USE_LLM=true
GRAPHIFY_BACKEND=ollama
GRAPHIFY_MODEL=llama3:latest

# Compile knowledge graph with Ollama
uv run graphify update wiki --backend ollama --model llama3:latest

# Auto-promote raw files to wiki with Ollama
uv run python promote_raw_to_wiki.py --use-llm --verbose

# Update wikilinks with semantic similarity
uv run python update_wikilinks.py --use-semantic
```

**Note:** LLM backend is optional. The default workflow uses Graphify's native extraction without any LLM or API keys.

### Deploying

Render automatically detects `render.yaml` in your repository. Connect your repo to Render and it will deploy using the Dockerfile.

### Graph compilation on Render

The server compiles the graph on startup using Graphify's native Tree-sitter extraction and Leiden clustering (no LLM required). For fastest cold starts, commit `graphify-out/graph.json` after local compilation.

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
| `graphifyy` | Knowledge graph compiler (Tree-sitter + Leiden clustering, no LLM required) |
| `requests` | HTTP client for `ingest.py` |
| `uvicorn` | ASGI server for HTTP transport |
| `httpx` | HTTP engine for FastMCP transport layer |
| `anyio` | Async I/O compatibility |

### Optional Dependencies

| Package | Role |
|---|---|
| `openai` | Optional LLM backend for enhanced semantic features (opt-in only) |

## Data Management

The `raw/` and `links/` directories are excluded from git. See `DATA_MANAGEMENT.md` for:
- Why these are excluded (copyright, bloat, freshness)
- Local workflow for content ingestion
- How to contribute curated content to `wiki/`
