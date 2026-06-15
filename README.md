# DC Status Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-blue?logo=flask)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blue?logo=bootstrap)](https://getbootstrap.com/)
[![MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintained by OneByJorah](https://img.shields.io/badge/Maintained%20by-OneByJorah-1E90FF?logo=github)](https://github.com/OneByJorah)

![DC Status Dashboard Architecture](https://v3b.fal.media/files/b/0a9e59a6/3Cq6QvN0Qw5qZ7H7vJ0uK4yD9c0g8a.png)

> **DC Status Dashboard**: Domain Controller monitoring dashboard for Windows Active Directory environments — a sleek, live‑updating web interface to monitor your domain controllers, track health metrics, view event logs, and receive real-time alerts. Built with Python (Flask) · Bootstrap 5 · Vanilla JS + AJAX.

---

## 📋 Overview

**DC Status Dashboard** is a professional-grade Domain Controller monitoring and management dashboard that provides real-time visibility into your Windows Active Directory domain infrastructure. It features **live DC health monitoring**, **event log analysis**, **user account tracking**, **GPO compliance checking**, and **comprehensive reporting** — all in a beautiful, responsive web interface.

> **Built with ❤️ by [OneByJorah](https://github.com/OneByJorah) for Active Directory monitoring.**

---

## 🏗️ Architecture

### High-Level System Architecture

```mermaid
flowchart TB
    subgraph Frontend["Web UI / API"]
        WEB[Web Interface<br/>Flask + Bootstrap 5]
        API[REST API<br/>Flask Blueprint]
    end

    subgraph Services["Core Services"]
        MONITOR[DC Monitor<br/>Live Health Check]
        EVENTS[Event Log<br/>Event Analysis]
        USERS[User Mgmt<br/>Account Tracking]
        GPO[GPO Status<br/>Compliance Check]
    end

    subgraph Data["Data Layer"]
        DB[(SQLite<br/>Config + History)]
        CACHE[(Redis<br/>Real-time Status)]
    end

    subgraph Integration["Integrations"]
        MSG[Telegram Bot<br/>Alerts]
        SLACK[Slack Alerts<br/>Incident Mgmt]
    end

    subgraph Security["Security"]
        AUTH[Authentication<br/>JWT + Session]
    end

    WEB <--> API
    API <--> MONITOR
    API <--> EVENTS
    API <--> USERS
    API <--> GPO
    MONITOR <--> DB
    EVENTS <--> DB
    USERS <--> DB
    GPO <--> DB
    API <--> CACHE
    MSG <--> API
    SLACK <--> API
    AUTH <--> DB

    style Frontend fill:#1a237e,stroke:#3f51b5,stroke-width:2px,color:#ffffff
    style Services fill:#2e7d32,stroke:#4caf50,stroke-width:2px,color:#ffffff
    style Data fill:#e65100,stroke:#ff9800,stroke-width:2px,color:#ffffff
    style Integration fill:#4a148c,stroke:#9c27b0,stroke-width:2px,color:#ffffff
    style Security fill:#c62828,stroke:#e53935,stroke-width:2px,color:#ffffff
```

---

## 🖼️ Screenshots

<div align="center">

### Dashboard Overview
![Dashboard](docs/dashboard.png)
*Main dashboard showing all domain controllers, health status, and alerts*

---

### DC Health Monitor
![DC Health](docs/dc-health.png)
*Real-time DC health monitoring with replication status, event log errors, and performance metrics*

---

### Event Log Viewer
![Events](docs/events.png)
*Event log viewer with filtering, pattern search, and automated anomaly detection*

---

### User Accounts
![Users](docs/users.png)
*User account management with status tracking, group membership, and account expiration*

---

### GPO Compliance
![GPO](docs/gpo.png)
*GPO compliance checking with policy application status, conflict detection, and reporting*

---

### Alerts & Notifications
![Alerts](docs/alerts.png)
*Real-time alert system with health check failures, replication issues, and event log warnings*

</div>

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🖥️ **DC Health Monitor** | Real-time domain controller health monitoring with replication status, event log analysis, and performance metrics |
| 📋 **Event Log Viewer** | Comprehensive event log viewer with filtering, pattern search, and automated anomaly detection |
| 👥 **User Account Tracking** | User account management with status tracking, group membership, and account expiration monitoring |
| 📝 **GPO Compliance** | GPO compliance checking with policy application status, conflict detection, and detailed reporting |
| 🔔 **Alert System** | Multi-channel alerting with Telegram bot, Slack integration, email notifications, and push alerts |
| 🎨 **Beautiful UI** | Sleek, responsive web interface with Bootstrap 5, dark/light mode toggle, and smooth animations |
| 📊 **Dashboard Stats** | Real-time dashboard statistics with DC counts, error rates, replication status, and uptime tracking |
| 🔍 **Search & Filter** | Advanced search and filtering for events, users, and GPOs with full-text search support |

---

## ⚡ Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/OneByJorah/DC_Status_Dashboard.git
cd DC_Status_Dashboard

# Install dependencies
pip install -r requirements.txt

# Run migrations
flask db upgrade

# Initialize admin user
python manage.py init-admin
```

### Configuration

Edit `config/settings.py`:

```python
# Server
SERVER_NAME = 'dc-dashboard.local'
SECRET_KEY=*** 'dev-secret-key')

# Database
DATABASE_URL = 'sqlite:///dc-status.db'

# Redis
REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:***@192.168.1.100:6379')
```

### Running the Application

```bash
# Development
flask run --host=0.0.0.0 --port=5000

# Production
gunicorn --workers=4 --bind=0.0.0.0:5000 --timeout=120 app:create_app()
```

### Accessing the Web UI

```
http://localhost:5000
```

---

## 🔍 API Reference

### Base URL

```
http://localhost:5000/api/v1
```

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/dcs` | GET | List all domain controllers |
| `/api/v1/dcs/<id>` | GET | Get DC details |
| `/api/v1/dcs/<id>` | PUT | Update DC settings |
| `/api/v1/dcs/<id>` | DELETE | Remove DC |
| `/api/v1/events` | GET | List events |
| `/api/v1/events/search` | GET | Search events |
| `/api/v1/events/<id>` | GET | Get event details |
| `/api/v1/users` | GET | List users |
| `/api/v1/users/search` | GET | Search users |
| `/api/v1/users/<id>` | GET | Get user details |
| `/api/v1/gpos` | GET | List GPOs |
| `/api/v1/gpos/<id>` | GET | Get GPO details |
| `/api/v1/health` | GET | System health check |

---

## 📊 Monitoring

### System Health

```bash
# Check service status
sudo systemctl status dc-dashboard

# Check database connection
sqlite3 /var/lib/dc-status/dc-status.db "SELECT 1"

# Check Redis
redis-cli ping
```

### Logs

```bash
# Application logs
sudo tail -f /var/log/dc-dashboard/app.log
```

---

## 🔒 Security

### Network Security

- Session-based authentication with Flask-Login
- CSRF protection on all forms
- Rate limiting on API endpoints

### Authentication

- Session-based authentication with Flask-Login
- JWT tokens for API access
- Role-based access control (RBAC)

---

## 📚 Dependencies

### Python

```
Flask>=3.0.0
Flask-SQLAlchemy>=3.0.0
Flask-Migrate>=3.1.0
Flask-CORS>=4.0.0
Flask-Login>=0.6.0
PyYAML>=6.0
psycopg2-binary>=2.9.0
redis>=4.5.0
requests>=2.31.0
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 📞 Support

For issues or questions, please open an issue on GitHub:

https://github.com/OneByJorah/DC_Status_Dashboard/issues

---

## 🙏 Acknowledgments

- **Flask**: Web framework by Armin Ronacher
- **Bootstrap**: Frontend framework by Twitter Bootstrap team

---

**Made with ❤️ by [OneByJorah](https://github.com/OneByJorah)**
