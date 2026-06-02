# UX Pattern Oracle — Claude Instructions

This project uses the same instructions as GitHub Copilot. See `.github/copilot-instructions.md` for full project context.

Claude-specific notes:
- Use the project's uv dependency management: `uv sync`
- When running Python scripts, use: `uv run python <script>.py`
- The knowledge graph compiles on startup via graphify (uses Ollama if available)
- For deployment to Render, use Ollama backend: `graphify wiki --no-viz --backend ollama`
