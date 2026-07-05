"""Smoke tests for ADSentinel Flask application."""

import sys
import os
import json

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure mock data exists
mock_data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mock_dc_status.json")
if not os.path.exists(mock_data_path):
    with open(mock_data_path, "w") as f:
        json.dump([], f)


def test_dashboard_route():
    """Test that the dashboard route returns 200 and contains expected content."""
    from app import app
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"DC Status" in response.data or b"Dashboard" in response.data


def test_public_route():
    """Test that the public status page returns 200."""
    from app import app
    with app.test_client() as client:
        response = client.get("/public")
        assert response.status_code == 200


def test_app_config():
    """Test that the Flask app is configured correctly."""
    from app import app
    assert app is not None
    assert app.testing is False
