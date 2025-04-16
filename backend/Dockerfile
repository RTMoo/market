FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /backend

ENV UV_COMPILE_BYTECODE=1

RUN uv venv /opt/venv

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ../pyproject.toml ../uv.lock /backend/

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=../pyproject.toml,target=/backend/pyproject.toml \
    uv sync --frozen --no-dev

COPY backend /backend
