# UX Pattern Oracle — Claude Instructions

**IMPORTANT: This is a NON RAG-FIRST MCP.**

Default behavior must work without LLM/API keys. LLM usage is opt-in only and must be explicitly triggered via environment variables or command flags. Any future implementation must respect this principle before suggesting RAG-based solutions.

This project uses the same instructions as GitHub Copilot. See `.github/copilot-instructions.md` for full project context.

Claude-specific notes:
- **Working Directory:** All commands assume you are in the `experience-patterns-oracles/` directory. If you're in the parent directory, first run `cd experience-patterns-oracles`
- Use the project's uv dependency management: `uv sync`
- When running Python scripts, use: `uv run python <script>.py`
- The knowledge graph compiles on startup via graphify (native extraction by default, LLM opt-in)
