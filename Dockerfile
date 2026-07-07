# =============================================================================
# ADSentinel — Production Dockerfile
# python:3.11-slim base
# Tag: jorahone/adsentinel:latest
# =============================================================================

FROM python:3.11-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user --upgrade pip && \
    pip install --no-cache-dir --user gunicorn && \
    pip install --no-cache-dir --user -r requirements.txt

# ---- Runtime Stage ----
FROM python:3.11-slim

# Create non-root user
RUN groupadd -r adsentinel && useradd -r -g adsentinel -d /app -s /sbin/nologin adsentinel

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /root/.local /usr/local
COPY --from=builder /root/.local/bin /usr/local/bin

# Create application directory
RUN mkdir -p /app

# Copy application code
COPY . /app
WORKDIR /app

# Set ownership
RUN chown -R adsentinel:adsentinel /app

# Switch to non-root user
USER adsentinel

# Expose application port
EXPOSE 5000

# Healthcheck — verify the app responds
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/')" || exit 1

# Run with gunicorn (production WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "2", "--timeout", "60", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
