# Phase 2 — ARCHITECTURE Report

**Repository:** `OneByJorah/DirWatch`
**Date:** 2026-07-05
**Analyst:** J1-PIPELINE ARCHITECT

---

## Architecture Overview

DirWatch uses a **single-process Flask architecture** with two Jinja2 HTML templates and file-based mock data. There is no database, no message queue, no container orchestration, and no API layer beyond the Flask routes.

```
┌─────────────────────────────────────────────────────┐
│                   Flask Process                       │
│                                                       │
│  ┌──────────────┐    ┌──────────────────────────┐    │
│  │  app.py       │    │  templates/               │    │
│  │  (20 LOC)     │───▶│  ├── dashboard.html      │    │
│  │               │    │  └── public.html         │    │
│  │  Routes:      │    └──────────────────────────┘    │
│  │  GET /        │                                     │
│  │  GET /public  │    ┌──────────────────────────┐    │
│  │  GET /health  │    │  mock_dc_status.json      │    │
│  └──────┬────────┘    │  (empty array [])         │    │
│         │             └──────────────────────────┘    │
│         │ reads                                        │
│         └─────────────────────────────────────────────┘
│                                                       │
│  ┌──────────────────────────────────────────────┐    │
│  │  collectors/ (PowerShell, run on Windows DCs) │    │
│  │  ├── mock_dc_collector.ps1  (functional)      │    │
│  │  ├── ldap_service.ps1       (placeholder)     │    │
│  │  └── notifications.ps1      (placeholder)     │    │
│  └──────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

---

## Architecture Score: 45/100 — DEGRADED

| Criterion | Score | Notes |
|-----------|-------|-------|
| Separation of Concerns | 50 | Single file for all routes; no models/views separation |
| Data Pipeline | 20 | Mock data loaded but not consumed by UI |
| Extensibility | 40 | Hardcoded template data makes adding real DCs difficult |
| Testability | 30 | No dependency injection, no test fixtures |
| Security Architecture | 30 | No auth, no HTTPS, no CSP, no input validation |
| Deployment Architecture | 20 | No Dockerfile, no containerization, no orchestration |
| Documentation Accuracy | 30 | README claims Docker support that doesn't exist |

---

## Key Architectural Observations

### 1. Single-File Flask App (app.py)

The entire application is 20 lines in one file. This is appropriate for a prototype but not for a production system. As features are added (auth, database, real-time updates, alerting), the single file will become unwieldy.

**Concern:** No modular structure for growth. No `models/`, `routes/`, `services/`, or `utils/` separation.

### 2. Data Pipeline Gap

The architecture has a **data pipeline that exists in code but is disconnected from the UI**:

- `app.py` loads `mock_dc_status.json` and passes it as `dc_data` to the template
- `dashboard.html` ignores `dc_data` and renders hardcoded DC entries
- The mock collector (`mock_dc_collector.ps1`) generates realistic JSON, but the dashboard never displays it

**Concern:** This is the single biggest architectural issue. The data contract (JSON schema) between collector and dashboard is defined but not implemented on the dashboard side. Adding real AD data will require rewriting the template to iterate over `dc_data`.

### 3. No Database or Persistence

The system has no database, no caching layer, and no persistent storage. All state is in-memory (loaded from JSON on startup). This means:
- Dashboard shows stale data until the Flask process is restarted
- No historical data or trend analysis
- No multi-user state
- No audit logging

**Concern:** Acceptable for a prototype, but a database (SQLite for simplicity) should be added before production use.

### 4. No Authentication or Authorization

The admin dashboard (`/`) is completely unprotected. Anyone who can reach the Flask port can see all DC metrics. The public status page (`/public`) is intentionally public, but the admin dashboard should be gated.

**Concern:** This is a security architecture gap that must be addressed before any production deployment.

### 5. PowerShell Collector Architecture

The collector design is sound: PowerShell scripts run on Windows Domain Controllers and write JSON to a shared file. The Flask app reads the file. This is a **poll-based, file-transfer architecture** — simple but with limitations:
- No real-time updates (polling interval dependent on collector schedule)
- No transport security (file share must be secured)
- No error handling if collector fails to write

**Concern:** The architecture should document the expected data flow (how does JSON get from Windows DC to the Flask server? SMB share? SCP? HTTP POST?).

### 6. No Health Endpoint Documentation

The `/health` endpoint exists (added in commit `74ab813`) but is not documented in the README API table. This is a documentation gap, not an architecture issue, but it means consumers of the system don't know about the health check.

### 7. Template Architecture

The dashboard template (`dashboard.html`) is a single 247-line file with inline CSS and JavaScript. This is acceptable for a single-page app of this size, but:
- No CSS framework (Bootstrap, Tailwind) — custom CSS is hand-written
- No JavaScript framework (React, Vue, Alpine) — vanilla JS for page switching
- No asset pipeline — CSS/JS is served inline, not as separate files

**Concern:** The inline approach works for now but will become a maintenance burden as the UI grows.

---

## Architecture Recommendations (Not to be implemented by FIXER)

These are architectural concerns for explicit decision, not items for Phase 4 FIXER to resolve:

1. **Add database layer** — SQLite for simplicity, PostgreSQL for production
2. **Wire template to data** — Replace hardcoded DC entries with Jinja2 iteration over `dc_data`
3. **Add authentication** — Flask-Login or similar for admin dashboard
4. **Modularize app** — Split into `routes/`, `models/`, `services/` as features grow
5. **Document data pipeline** — How does JSON get from Windows DC to Flask server?
6. **Add real-time updates** — WebSocket or polling for live DC status
7. **Add asset pipeline** — Serve CSS/JS as separate files, add cache headers
