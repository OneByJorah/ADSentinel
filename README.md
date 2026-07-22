<div align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Active%20Directory-0078D4?style=for-the-badge&logo=microsoft&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</div>

<br>

<div align="center">
  <h1>DirWatch (ADSentinel)</h1>
  <p><strong>Active Directory DC Monitoring Dashboard</strong></p>
  <p>Real-time health, replication status, and alerting for domain controllers.</p>
  <p>
    <a href="#features">Features</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#contributing">Contributing</a>
  </p>
</div>

---

## Screenshot

![DirWatch Dashboard](docs/screenshot.png)
*Active Directory domain controller monitoring dashboard with real-time health metrics.*

## Features

- **Real-Time Monitoring** — Live health metrics for all domain controllers.
- **Replication Status** — Track AD replication between DCs.
- **Alert System** — Configurable alerts for DC health issues.
- **LDAP Integration** — Direct LDAP queries to Active Directory.
- **Historical Data** — Track health trends over time.
- **Flask Dashboard** — Lightweight Python web interface.
- **Docker Support** — Easy deployment with Docker.

## Quick Start

```bash
git clone https://github.com/OneByJorah/DirWatch.git
cd DirWatch

pip install -r requirements.txt
python3 app.py
```

Open **http://localhost:5000** in your browser.

### Docker

```bash
docker compose up -d
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `LDAP_SERVER` | — | Domain controller hostname |
| `LDAP_BASE_DN` | — | Base DN for queries |
| `LDAP_BIND_DN` | — | Bind DN for authentication |
| `LDAP_PASSWORD` | — | LDAP password |
| `ALERT_EMAIL` | — | Email for alerts |
| `REFRESH_INTERVAL` | `60` | Monitoring refresh interval (seconds) |

## Architecture

```
Browser ──HTTP──▶ Flask App ──LDAP──▶ Active Directory
                    │
                    ├──▶ Health Monitor
                    ├──▶ Replication Checker
                    ├──▶ Alert Engine
                    └──▶ SQLite (Historical Data)
```

## Project Structure

```
DirWatch/
├── app.py                 # Flask application
├── monitor/
│   ├── __init__.py
│   ├── health.py          # DC health monitoring
│   ├── replication.py     # Replication status
│   └── alerts.py          # Alert management
├── templates/             # HTML templates
├── static/                # CSS, JS
├── requirements.txt       # Python dependencies
├── docker-compose.yml     # Docker deployment
└── README.md
```

## Dashboard Panels

| Panel | Description |
|-------|-------------|
| **DC Overview** | Status of all domain controllers |
| **Replication** | Inter-DC replication health |
| **FSMO Roles** | FSMO role holder status |
| **Events** | Recent AD events and errors |
| **Trends** | Historical health metrics |

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards.

## Security

For security concerns, see [SECURITY.md](SECURITY.md). Please report vulnerabilities to **info@jorahone.com** — do not use public issues.

## License

MIT © Jhonattan L. Jimenez

---

<div align="center">
  <p>Active Directory domain controller monitoring.</p>
  <p><a href="https://github.com/OneByJorah">@OneByJorah</a></p>
</div>
