#!/bin/bash
# ADSentinel Docker Entrypoint
# Handles first-run setup and credential onboarding

set -e

# If .env doesn't exist, run setup wizard
if [ ! -f /app/.env ]; then
    echo "============================================"
    echo "  ADSentinel — First Run Setup"
    echo "============================================"
    echo ""
    echo "No configuration found. Let's set up ADSentinel."
    echo ""
    
    # Generate random secret
    SECRET=$(python3 -c "import secrets; print(secrets.token_hex(32))")
    
    read -p "Use mock mode (no live AD required)? [Y/n]: " MOCK
    MOCK=${MOCK:-Y}
    
    if [[ "$MOCK" =~ ^[Yy] ]]; then
        MOCK_MODE=true
        echo "✅ Mock mode enabled — no AD credentials needed."
    else
        MOCK_MODE=false
        read -p "AD Domain (e.g., corp.local): " AD_DOMAIN
        read -p "AD Server hostname: " AD_SERVER
        read -p "AD Username: " AD_USERNAME
        read -s -p "AD Password: " AD_PASSWORD
        echo ""
    fi
    
    read -p "Port [5000]: " PORT
    PORT=${PORT:-5000}
    
    # Write .env
    cat > /app/.env <<EOF
SECRET_KEY=${SECRET}
MOCK_MODE=${MOCK_MODE}
PORT=${PORT}
AD_DOMAIN=${AD_DOMAIN:-}
AD_SERVER=${AD_SERVER:-}
AD_USERNAME=${AD_USERNAME:-}
AD_PASSWORD=${AD_PASSWORD:-}
LOG_LEVEL=INFO
EOF
    
    echo ""
    echo "✅ Configuration saved to /app/.env"
    echo "============================================"
fi

# Source .env
export $(grep -v '^#' /app/.env | xargs)

echo "Starting ADSentinel..."
exec "$@"
