<!-- j1-brand:v2 -->
<div align="center">

# ADSentinel

A lightweight, self-hosted Active Directory Domain Controller monitoring dashboard — real-time DC health, replication status, and service outage alerts.

[![GitHub](https://img.shields.io/badge/github-OneByJorah%2FADSentinel-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://github.com/OneByJorah/ADSentinel)
[![License](https://img.shields.io/badge/license-MIT-FFB300?style=for-the-badge&labelColor=0d0d0c)](LICENSE)
[![Language](https://img.shields.io/badge/HTML-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Built by](https://img.shields.io/badge/built%20by-JorahOne%20LLC-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://github.com/OneByJorah)

</div>

---

## Why This Exists

Domain Controllers are the backbone of any Windows network — when a DC goes down, everything stops. ADSentinel gives you a lightweight dashboard for monitoring DC health and replication status, with separate Admin and public-facing status views. PowerShell collectors pull data from Windows DCs, and a mock mode lets you develop without live servers.

## Key Features

| Feature | Why It Matters |
|---|---|
| Real-time DC health monitoring | See the status of all Domain Controllers at a glance |
| Replication status tracking | Detect replication failures before they cause outages |
| Public status page | Share a read-only view with stakeholders |
| PowerShell collectors | Lightweight agentless data collection from Windows DCs |
| Mock mode | Develop and test without connecting to live infrastructure |

## Quick Start

```bash
git clone https://github.com/OneByJorah/ADSentinel.git
cd ADSentinel
pip install -r requirements.txt
python3 app.py
```

- Admin dashboard: `http://localhost:5000`
- Public status page: `http://localhost:5000/public`

## Architecture

```
┌──────────────┐     ┌──────────────┐
│  Windows DCs  │────▶│  ADSentinel   │
│  (PowerShell) │     │  Flask App    │
└──────────────┘     └──────┬───────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
       ┌──────────┐  ┌──────────┐  ┌──────────┐
       │  Admin    │  │  Public   │  │  Mock    │
       │Dashboard  │  │Status Page│  │  Mode    │
       └──────────┘  └──────────┘  └──────────┘
```

## Documentation

| Doc | Description |
|---|---|
| [Setup Guide](docs/setup.md) | Installation and configuration |
| [DC Configuration](docs/dcs.md) | Connecting to your Domain Controllers |

---

## License

MIT © JorahOne, LLC — see [LICENSE](LICENSE)

<sub>Part of the JorahOne infrastructure ecosystem.</sub>
