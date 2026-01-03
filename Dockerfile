FROM python:3.14-slim

WORKDIR /app

# Instalar uv
RUN pip install --no-cache-dir uv

# Copiar metadata primero (mejor cache)
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

# Copiar código
COPY app ./app

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
