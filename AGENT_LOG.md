# DirWatch — Repo Polish Log

**Repo:** OneByJorah/DirWatch
**Branch:** agent/polish-pass
**Author:** Jhonattan L. Jimenez (JorahOne) — https://github.com/OneByJorah
**Date:** 2026-07-20

## Stack (detected)
- Flask (Python 3.x) backend serving Jinja2 templates (`app.py`, `templates/`).
- Static dashboard (HTML/CSS/vanilla JS) + PowerShell collectors (scaffold/placeholders).
- Docker: `python:3.11-slim` + gunicorn, non-root, HEALTHCHECK.

## Identity problem found
Repo is named **DirWatch** but content/branding referenced **ADSentinel** (Active
Directory Domain Controller monitoring). Unify to **DirWatch** as a datacenter/DC
status dashboard.

## BROKEN (intake)
1. `mock_dc_status.json` = `[]` — app loaded empty array.
2. `templates/dashboard.html` ignored `dc_data` (hardcoded mock UI).
3. `/public` returned a plaintext string, not `public.html`.
4. Branding blue/green — not JorahOne design system (`#0d0d0c`, `#FFB300`, JetBrains Mono, ops status).
5. Name mismatch ADSentinel vs DirWatch across README/Dockerfile/compose/entrypoint/j1.yaml.
6. `.gitignore` minimal; `requirements.txt` empty; `.env.example` AD-specific.
7. `docs/screenshot.png` (ADSentinel-era) missing from README ref.

## FIXED
- Rebranded DirWatch across app/Docker/compose/entrypoint/j1.yaml/README.
- `app.py` loads `mock_dc_status.json`, renders real DC data via Jinja2; `/public` serves template; added `/api/status`.
- `dashboard.html` + `public.html` reworked to JorahOne design system, render live data + auto alerts.
- Populated `mock_dc_status.json` with 4 DCs (2 online / 2 offline).
- Dockerfile `chown -r` -> `-R` bug fixed; non-root + HEALTHCHECK retained.
- LICENSE credited Jhonattan L. Jimenez / JorahOne LLC, 2026.
- Completed `.gitignore`, `requirements.txt` (flask+gunicorn), `.env.example` (STATUS_FILE).
- Removed stale ADSentinel-era docs (AUDIT_REPORT/FIXES/CHANGELOG/ROADMAP/screenshot.png).
- 3 real Playwright screenshots added to `docs/screenshots/`.

## Verified
- Local: `python3 app.py` -> 200 on `/`, `/public`; `/api/status` returns JSON.
- Docker: `docker build` + `docker run` -> `/` 200, healthcheck `healthy`.
- gh repo metadata: description + topics (flask, docker, dashboard, monitoring, status-page) set.
- Pushed agent/polish-pass: 18c300a..c4f1012 (fast-forward).
