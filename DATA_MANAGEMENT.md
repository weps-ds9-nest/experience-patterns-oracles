# Data Management

This document explains how data is managed locally.

## Directory Structure

- **`raw/`** - Contains ingested markdown content from external sources (folder tracked, contents ignored)
- **`links/`** - Contains URL lists and collection exports (folder tracked, contents ignored)

## Why Contents Are Ignored

- `raw/` contains hundreds of markdown files that grow over time
- `links/` contains CSV files that accumulate URLs
- Keeping these out of git keeps the repository lightweight and fast to clone
- Ingested content becomes stale over time; the workflow is designed to be run locally to ensure freshness

## Local Workflow

**Working Directory:** All commands below assume you are in the `experience-patterns-oracles/` directory. If you're in the parent directory, first run:
```bash
cd experience-patterns-oracles
```

### For Content Contributors

1. **Add new URLs** to `links/collections/` (e.g., export bookmarks as CSV)
2. **Run the ingest script** to fetch content:
   ```bash
   uv run python ingest.py
   ```
   Or use watch mode for automatic merging:
   ```bash
   uv run python ingest.py --watch
   ```
3. **Curate content** by promoting files from `raw/` to `wiki/`
4. **Commit only `wiki/` changes** to git

### For MCP Server Operators

1. **Ensure `wiki/` has content** - this is the source for the knowledge graph
2. **Run the server**:
   ```bash
   uv run python server.py
   ```
3. The server will automatically compile `graphify-out/graph.json` on first run
4. **Commit `graphify-out/graph.json`** for faster cold starts on deployment

## What to Commit

Only commit these to the public repository:
- **`wiki/`** - Curated, edited markdown entries with wiki-links
- **`graphify-out/graph.json`** - Compiled knowledge graph (optional, for faster deployment)
- Code files and configuration

Do NOT commit:
- `raw/` - Ingested content (manage locally)
- `links/` - URL lists (manage locally)

## Rebuilding from Scratch

If you need to rebuild the data from scratch:

1. Clone the repository
2. Navigate to the project directory:
   ```bash
   cd experience-patterns-oracles
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```
4. Add your URL collections to `links/collections/`
5. Run `uv run python ingest.py`
6. Curate content from `raw/` to `wiki/`
7. Run `uv run python server.py` to compile the graph

## Knowledge Graph Compilation

When the server runs, it requires a compiled knowledge graph at `graphify-out/graph.json` to power the pattern relationship matching.

### Enhanced Graph Compilation (Optional LLM)
To build a semantic knowledge graph with enhanced relationships, you can opt-in to LLM backend:
- **Ollama**: Set `GRAPHIFY_USE_LLM=true` and `GRAPHIFY_BACKEND=ollama`, then run `uv run python server.py` or `uv run graphify update wiki --backend ollama`.
- **Note**: The default workflow uses Graphify's native Tree-sitter extraction and Leiden clustering without any LLM or API keys.

## Backup Strategy

Since `raw/` and `links/` are not in git, consider:
- Backing up these directories separately
- Using version control locally if needed
- Exporting `links/links.csv` periodically for safekeeping
