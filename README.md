# 🖥️ DC Status Dashboard

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Latest-000000?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintained by OneByJorah](https://img.shields.io/badge/Maintained%20by-OneByJorah-1E90FF?logo=github)](https://github.com/OneByJorah)

---

## 📋 Overview

**DC Status Dashboard** is an open-source Active Directory monitoring dashboard built for full operational visibility without vendor limitations. Monitor domain controller health, service status, and uptime from a clean web interface.

> **Maintained by [OneByJorah](https://github.com/OneByJorah)**

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Dashboard View** | Real-time overview of all domain controllers |
| 🌐 **Public Status Page** | Read-only public-facing status page |
| 🔧 **Modular Collectors** | PowerShell-based data collectors for AD metrics |
| 📱 **Responsive UI** | Works on desktop, tablet, and mobile |
| 🔔 **Notifications** | Email, Teams, and Telegram alert support (planned) |

---

## 📁 Project Structure

```
DC_Status_Dashboard/
├── app.py                    # Flask application entry point
├── requirements.txt          # Python dependencies
├── mock_dc_status.json       # Sample data for development
├── collectors/               # PowerShell data collectors
│   ├── ldap_service.ps1      # LDAP service monitoring
│   ├── mock_dc_collector.ps1 # Mock data collector
│   └── notifications.ps1     # Alert notification scripts
├── templates/                # HTML templates
│   ├── dashboard.html        # Admin dashboard
│   └── public.html           # Public status page
└── docs/                     # Documentation
```

---

## 📋 Prerequisites

| Requirement | Details |
|-------------|---------|
| **OS** | Windows Server 2016+ (collectors), Any OS (dashboard) |
| **Python** | 3.9 or higher |
| **PowerShell** | 5.1+ (for collectors) |
| **Network** | Access to domain controllers |

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/OneByJorah/DC_Status_Dashboard.git
cd DC_Status_Dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run with Mock Data

```bash
python app.py
```

Access the dashboard at `http://localhost:5000`

### 4. Deploy Collectors

On a Windows Server with AD access:

```powershell
# Run as Administrator
cd collectors
.\mock_dc_collector.ps1
```

---

## 🔧 Configuration

### Mock Data

Edit `mock_dc_status.json` to customize the displayed domain controllers:

```json
[
  {
    "name": "DC01",
    "status": "online",
    "ip": "192.168.1.10",
    "services": ["LDAP", "DNS", "Kerberos"]
  }
]
```

### Production Deployment

For production use with real data collectors:

1. Deploy PowerShell collectors on domain controllers
2. Configure secure API ingestion
3. Set up RBAC authentication
4. Configure alerting (Email/Teams/Telegram)

---

## 🗺️ Roadmap

| Phase | Feature | Status |
|-------|---------|--------|
| 1 | PowerShell collectors on DCs | 🚧 In Progress |
| 2 | Secure API ingestion | 📋 Planned |
| 3 | RBAC authentication | 📋 Planned |
| 4 | Email / Teams / Telegram alerts | 📋 Planned |
| 5 | Historical uptime visualization | 📋 Planned |

---

## 🔒 Security

- No credentials, domain names, or secrets stored in the repository
- Public page is read-only with no sensitive data exposure
- Production deployment should use RBAC and encrypted communication

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Dashboard won't start | Check Python version: `python --version` |
| No data displayed | Verify `mock_dc_status.json` exists and is valid JSON |
| Collector errors | Run PowerShell as Administrator |

---

## 🔄 Updates

```bash
cd /path/to/DC_Status_Dashboard
git pull origin main
pip install -r requirements.txt --upgrade
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

**Made with ❤️ by [OneByJorah](https://github.com/OneByJorah)**
