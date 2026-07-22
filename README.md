# ADSentinel (DirWatch)

Active Directory Domain Controller monitoring dashboard — real-time DC health, replication status, and alerting.

![status](https://img.shields.io/badge/status-active-FFB300?style=flat-square)
![language](https://img.shields.io/badge/python-3.10+-0d0d0c?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-FFB300?style=flat-square)

## Overview

ADSentinel is a self-hosted Active Directory Domain Controller monitoring dashboard that provides real-time visibility into DC health, replication status, and alerting. Built with Flask and Jinja2 templates, it includes PowerShell collectors for live AD data, a public status page, and mock mode for development without a live AD environment.

## Features

- Domain Controller health monitoring with real-time metrics
- Replication status tracking across all DCs
- Built-in alerting for failures and outages
- Public status page for stakeholder visibility
- Mock mode for development without live AD
- Admin dashboard with full metrics and historical data
- PowerShell collectors for live AD data ingestion
- Docker Compose deployment

## Architecture / Tech Stack

- **Backend**: Flask (Python 3.10+)
- **Templates**: Jinja2
- **Collectors**: PowerShell (AD data)
- **Deployment**: Docker Compose, local install

## Installation

```bash
git clone https://github.com/OneByJorah/DirWatch.git
cd DirWatch

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
python3 app.py
```

Or with Docker:
```bash
docker compose up -d
```

- Admin dashboard: `http://localhost:5000`
- Public status page: `http://localhost:5000/public`

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `production` | Flask environment mode |
| `PORT` | `5000` | Dashboard port |
| `HOST` | `0.0.0.0` | Bind address |

## License

MIT — see [LICENSE](LICENSE).

---
Part of the JorahOne / J1 ecosystem — AD monitoring for enterprise Windows environments.
