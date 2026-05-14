# Multi-stage Dockerfile: build wheel in builder, install in minimal runtime image

FROM python:3.11-slim AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    TZ=America/Sao_Paulo

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project metadata and source
COPY pyproject.toml README.md ./
COPY src ./src

# Install packaging tools and build wheel
RUN python -m pip install --upgrade pip setuptools wheel hatchling \
    && python -m pip wheel . -w /wheels

# Final slim image
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    TZ=America/Sao_Paulo

# Runtime deps (minimal) - keep libpq runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy built wheel(s) and install
COPY --from=builder /wheels /wheels
RUN python -m pip install --no-cache-dir /wheels/*.whl

# Copy remaining files
COPY . .

# Ensure entrypoint exists and is executable
COPY scripts/docker-entrypoint.sh /scripts/docker-entrypoint.sh
RUN chmod +x /scripts/docker-entrypoint.sh \
    && mkdir -p /app/logs /app/static /app/migrations

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/docs || exit 1

CMD ["/scripts/docker-entrypoint.sh"]

