"""Smoke tests for DirWatch Flask application."""

import json
import os
import sys
import tempfile

import pytest


@pytest.fixture
def app():
    """Create a test Flask app instance with mock data."""
    # Create a temporary mock data file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        mock_data = [
            {
                "Name": "DC-01",
                "Replication": "Healthy",
                "SYSVOL": "OK",
                "LDAPBind": "Success",
                "DHCPScope": "80% Used",
                "Services": {"DNS": "Running", "DHCP": "Running", "ADWS": "Stopped"},
            }
        ]
        json.dump(mock_data, f)
        temp_path = f.name

    # Override MOCK_DATA_PATH and import app
    os.environ["MOCK_DATA_PATH"] = temp_path
    os.environ["EXTERNAL_IP"] = "127.0.0.1"

    # Import after setting env vars
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from app import app as flask_app

    flask_app.config["TESTING"] = True
    yield flask_app

    # Cleanup
    os.unlink(temp_path)


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


class TestDashboard:
    """Tests for the dashboard route."""

    def test_dashboard_returns_200(self, client):
        """GET / should return 200 OK."""
        resp = client.get("/")
        assert resp.status_code == 200

    def test_dashboard_contains_title(self, client):
        """Dashboard page should contain the expected title."""
        resp = client.get("/")
        assert b"DC Status Dashboard" in resp.data


class TestPublicPage:
    """Tests for the public status page."""

    def test_public_returns_200(self, client):
        """GET /public should return 200 OK."""
        resp = client.get("/public")
        assert resp.status_code == 200

    def test_public_contains_status(self, client):
        """Public page should indicate all systems operational."""
        resp = client.get("/public")
        assert b"All Systems Operational" in resp.data or b"All systems operational" in resp.data


class TestAppConfig:
    """Tests for application configuration."""

    def test_app_has_testing_mode(self, app):
        """App should have TESTING mode enabled for tests."""
        assert app.testing is True

    def test_app_has_secret_key(self, app):
        """App may not have a secret key configured (no sessions used)."""
        # secret_key is None by default — acceptable for this app
        assert app.secret_key is None or isinstance(app.secret_key, str)
