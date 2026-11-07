#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala as dependências usando uv a partir do uv.lock
uv sync --locked

# Converte os arquivos estáticos
uv run python manage.py collectstatic --no-input

# Aplica as migrações no banco de dados
uv run python manage.py migrate