# ADSentinel

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)

Active Directory Domain Controller monitoring dashboard. Real-time visibility into DC health, replication status, and alerting — self-hosted and lightweight.

## Features

- Domain Controller health monitoring
- Replication status tracking
- Built-in alerting for failures and outages
- Public status page
- Mock mode for development without live AD
- Admin dashboard with full metrics
- PowerShell collectors for live AD data

## Tech Stack

- Python 3.10+
- Flask
- Jinja2 templates
- Docker / Docker Compose

## Installation

```bash
git clone https://github.com/OneByJorah/ADSentinel.git
cd ADSentinel
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env as needed
```

## Usage

```bash
python3 app.py
```

Open **http://localhost:5000** for the admin dashboard or **http://localhost:5000/public** for the public status page.

### Docker

```bash
docker compose up -d
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `production` | Flask environment mode |
| `PORT` | `5000` | Dashboard port |
| `HOST` | `0.0.0.0` | Bind address |

## API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Admin dashboard |
| `/public` | GET | Public status page |

## Project Structure

```
ADSentinel/
├── app.py                 # Flask web server
├── requirements.txt       # Python dependencies
├── templates/             # Jinja2 templates
├── collectors/            # AD data collectors (PowerShell)
├── docs/                  # Documentation
├── assets/                # Static assets
└── mock_dc_status.json    # Mock data for development
```

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

Report vulnerabilities privately to **info@jorahone.com**. See [SECURITY.md](SECURITY.md).

## License

MIT © Jhonattan L. Jimenez
