FROM python:3.12-slim

# Install uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Install dependencies first (layer-cached unless lockfile changes)
COPY pyproject.toml uv.lock ./
RUN uv sync --no-install-project

# Copy the rest of the project
COPY . .

# Put the venv on PATH so `graphify` CLI is resolvable by server.py's subprocess call
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["python", "server.py"]
