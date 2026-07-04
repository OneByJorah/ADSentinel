# ADSentinel

> Domain Controller monitoring dashboard for Windows AD and DNS observability.

![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-%23FFB300?style=for-the-badge)
![Language](https://img.shields.io/badge/language-Python-informational?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-linux-informational?style=for-the-badge)

ADSentinel is an enterprise-grade, ops-precise platform built for VIDE and SMB operations. Run it solo. Deliver results.

- **DC health monitoring**: domain controller status and replication checks.
- **Alerting**: notifications via collector logic.
- **Mock/test mode**: uses `mock_dc_status.json` for offline development.
- **Responsive dashboard**: public and private (admin) views.
- **Lightweight**: Flask + SQLite-style JSON state, easy to self-host.

---

## Architecture

Client → Flask backend (`app.py`) → collectors (PowerShell/Mock JSON) → templates (`dashboard.html`, `public.html`) → browser UI.

Data paths:
- Mock collector: `mock_dc_status.json`
- Templates: `templates/dashboard.html`, `templates/public.html`
- Assets: `assets/screenshot.png`

---

| Layer | Stack |
|---|---|
| Runtime | Linux/Windows (PowerShell collectors) |
| Backend | Python / Flask |
| Collectors | PowerShell 5.1+ |
| Frontend | HTML5 (Jinja2 templates) |
| VCS | Git + GitHub (`github.com/OneByJorah/ADSentinel`) |

---

## Quickstart

```bash
git clone https://github.com/OneByJorah/ADSentinel.git
cd ADSentinel
# Follow in-repo setup instructions
```
Verify by checking service health or running the in-repo test command.

## Configuration

Environment variables are documented in-repo. See [Environment Variables](#environment-variables) for the full table.

## Roadmap

- Feature parity with production requirements
- Observability and alerting expansions
- Community feedback integration

## License

MIT — Copyright JorahOne, LLC. See [LICENSE](LICENSE) for details.

---

[OneByJorah](https://github.com/OneByJorah) · [JorahOne-Services](https://github.com/JorahOne-Services)
