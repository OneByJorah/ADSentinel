# Phase 0 — CLASSIFIER Report

**Repository:** `OneByJorah/ADSentinel`
**Date:** 2026-07-05
**Analyst:** J1-PIPELINE CLASSIFIER

---

## Classification

**PROJECT_CLASS: `Dashboard`**

### Secondary Classes
- `Web` — Flask-based web application serving HTML templates
- `Monitoring` — Active Directory Domain Controller health monitoring
- `Python` — Core application written in Python (Flask)
- `Shell` — PowerShell collectors for AD data gathering

### Classification Rationale

ADSentinel is primarily a **monitoring dashboard** — a single-page web application that provides IT operations teams with at-a-glance visibility into Active Directory Domain Controller health. The core deliverable is the dashboard UI (`/` route) and public status page (`/public` route), making `Dashboard` the most specific and accurate classification.

| Aspect | Evidence |
|--------|----------|
| Primary function | Web-based dashboard for DC health monitoring |
| Tech stack | Flask (Python), Jinja2 templates, HTML/CSS/JS |
| Data collection | PowerShell scripts (Windows AD) |
| Deployment | Single Flask process, no database, no container orchestration |
| Interfaces | Admin dashboard (`/`), Public status page (`/public`), Health check (`/health`) |

### Gating for Later Phases

- **Docker hardening (Phase 3):** No Dockerfile exists — Docker hardening checks are N/A until one is created
- **AI/LLM checks (Phase 11):** N/A — not an AI/Agent/LLM project
- **Kubernetes checks:** N/A — no K8s manifests
