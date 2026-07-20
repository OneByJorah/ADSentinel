#!/bin/bash
# DirWatch Docker Entrypoint
# Ensures a status data file exists; defaults to mock data when none provided.

set -e

# Default status file path
export STATUS_FILE="${STATUS_FILE:-/app/mock_dc_status.json}"

# If no status file is mounted/present, fall back to the bundled mock data
if [ ! -f "$STATUS_FILE" ]; then
    echo "No STATUS_FILE found at $STATUS_FILE — using bundled mock_dc_status.json"
    export STATUS_FILE=/app/mock_dc_status.json
fi

echo "Starting DirWatch with STATUS_FILE=$STATUS_FILE"
exec "$@"
