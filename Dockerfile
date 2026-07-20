# =============================================================================
# DirWatch — Production Dockerfile
# python:3.11-slim base, gunicorn WSGI server, non-root user
# Tag: jorahone/dirwatch:latest
# =============================================================================

FROM python:3.11-slim

# Create non-root user
RUN groupadd -r dirwatch && useradd -r -g dirwatch -d /app -s /sbin/nologin dirwatch

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

# Copy application code
COPY . /app

# Set ownership to non-root user
RUN chown -R dirwatch:dirwatch /app

# Switch to non-root user
USER dirwatch

# Expose application port
EXPOSE 5000

# Healthcheck — verify the app responds
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/')" || exit 1

# Run with gunicorn (production WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "2", "--timeout", "60", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
