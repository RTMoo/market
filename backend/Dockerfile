# Используем готовый образ uv
FROM ghcr.io/astral-sh/uv:python3.12-alpine

# Устанавливаем рабочую директорию
WORKDIR /backend

# Устанавливаем переменные для виртуального окружения
ENV UV_COMPILE_BYTECODE=1

# Создаем виртуальное окружение с uv
RUN uv venv /opt/venv

# Устанавливаем переменные окружения для виртуального окружения
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Копируем pyproject.toml и uv.lock в контейнер
COPY ../pyproject.toml ../uv.lock /backend/

# Синхронизируем зависимости через uv
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=../pyproject.toml,target=/backend/pyproject.toml \
    uv sync --frozen --no-dev

# Копируем код проекта в рабочую директорию контейнера
COPY backend /backend

