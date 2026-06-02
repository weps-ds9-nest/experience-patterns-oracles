# Data Management

This document explains how data is managed locally and why certain directories are excluded from the public repository.

## Excluded Directories

The following directories are **excluded from git** and managed locally:

- **`raw/`** - Contains ingested markdown content from external sources
- **`links/`** - Contains URL lists and collection exports
- **`wiki/graphify-out/`** - Cache directory (not used by the MCP server)

## Why These Are Excluded

### Copyright Concerns
The `raw/` directory contains content ingested from external websites. Redistributing this content in a public repository may violate copyright terms of the original sources.

### Repository Bloat
- `raw/` contains hundreds of markdown files that grow over time
- `links/` contains CSV files that accumulate URLs
- Including these would make the repository very large and slow to clone

### Data Freshness
Ingested content becomes stale over time. The ingestion workflow is designed to be run locally to ensure content is up-to-date.

## Local Workflow

### For Content Contributors

1. **Add new URLs** to `links/collections/` (e.g., export from Raindrop.io)
2. **Run the ingest script** to fetch content:
   ```bash
   uv run --no-project python ingest.py
   ```
   Or use watch mode for automatic merging:
   ```bash
   uv run --no-project python ingest.py --watch
   ```
3. **Curate content** by promoting files from `raw/` to `wiki/`
4. **Commit only `wiki/` changes** to git

### For MCP Server Operators

1. **Ensure `wiki/` has content** - this is the source for the knowledge graph
2. **Run the server**:
   ```bash
   uv run --no-project python server.py
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
- `wiki/graphify-out/` - Cache directory (not used by server)

## Rebuilding from Scratch

If you need to rebuild the data from scratch:

1. Clone the repository
2. Add your URL collections to `links/collections/`
3. Run `uv run --no-project python ingest.py`
4. Curate content from `raw/` to `wiki/`
5. Run `uv run --no-project python server.py` to compile the graph

## Backup Strategy

Since `raw/` and `links/` are not in git, consider:
- Backing up these directories separately
- Using version control locally if needed
- Exporting `links/links.csv` periodically for safekeeping
