# Use uma imagem Python oficial como base
FROM python:3.11-slim

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV POETRY_NO_INTERACTION=1
ENV POETRY_CACHE_DIR=/tmp/poetry_cache

# Define o diretório de trabalho no container
WORKDIR /app

# Instala dependências do sistema necessárias e Poetry
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        curl \
        libpq-dev \
    && pip install poetry \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivos do Poetry
COPY pyproject.toml poetry.lock ./

# Instala as dependências usando Poetry (sem criar venv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root \
    && rm -rf $POETRY_CACHE_DIR

# Copia todo o código da aplicação
COPY . .

# Cria um usuário não-root para segurança
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expõe a porta que o Django irá usar
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]