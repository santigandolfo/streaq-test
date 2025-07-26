FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
COPY .python-version .python-version
RUN uv sync --frozen --no-cache --compile-bytecode
COPY . .

ENV PATH="/app/.venv/bin:$PATH"
