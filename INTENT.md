# INTENT.md — J1-PIPELINE Phase -1 (ORACLE)

**Repository:** `OneByJorah/ADSentinel`
**Analysis Date:** 2026-07-05
**Analyst:** J1-PIPELINE ORACLE (read-only)
**Status:** Intent Reconstructed

---

## What This System Does

ADSentinel is a **lightweight, self-hosted Active Directory Domain Controller monitoring dashboard** — a single Flask process serving two interfaces:

| Interface | Route | Purpose |
|-----------|-------|---------|
| Admin Dashboard | `/` | Dark-themed single-page app with stat cards (CPU, memory, disk, temperature, network, active DCs), a DC list with online/inactive badges, and an alert log. Designed for IT ops teams to monitor their DC fleet at a glance. |
| Public Status Page | `/public` | Minimal "🟢 All Systems Operational" page for external stakeholders — shows overall uptime without exposing internal metrics. |
| Health Check | `/health` | JSON endpoint returning `{"status": "ok", "mock_dc_count": N}` for deployment monitoring hooks. |

Data collection is handled by **PowerShell scripts** intended to run on Windows Domain Controllers:

- `mock_dc_collector.ps1` — Functional mock collector that generates sample DC status (replication health, SYSVOL, LDAP bind, DHCP scope, service health) and writes to `mock_dc_status.json`
- `ldap_service.ps1` — Placeholder (single comment line)
- `notifications.ps1` — Placeholder (single comment line)

A **mock mode** (via `mock_dc_status.json`) allows the dashboard to run fully offline without live AD connectivity, enabling development, testing, and demonstration in isolated environments.

### Operational Role

ADSentinel is consumed by **IT operations teams and system administrators** who need a single-pane-of-glass view of their Active Directory health. It solves the runtime problem of "is my AD infrastructure healthy right now?" without requiring SSH/RDP access to individual domain controllers or a full enterprise monitoring stack.

---

## Why This Was Built

### Real Problem

Active Directory is the backbone of identity and access management in virtually every Windows-centric organization. When a Domain Controller goes down, replication breaks, or a critical service (DNS, DHCP, LDAP) stops responding, the impact is immediate and organization-wide: authentication failures, resource inaccessibility, and cascading outages. Ops teams need **instant visibility** into DC health, but the available tools force a tradeoff.

### Why Existing Tools Were Insufficient

Existing monitoring solutions for AD fall into two categories, both problematic:

1. **Enterprise monitoring suites** (Microsoft SCOM, SolarWinds, PRTG, Nagios, Zabbix) — Powerful but heavy. They require dedicated infrastructure, trained administrators, expensive licensing, and significant ongoing maintenance. Overkill for small-to-mid-size deployments or single-forest environments.

2. **Built-in Windows tools** (`repadmin`, `dcdiag`, AD Administrative Center, PowerShell cmdlets) — Powerful but CLI-only, no centralized dashboard, no historical view, no alerting. They require per-machine RDP/SSH access and manual invocation. No way to get a "green/red" at-a-glance view.

3. **Cloud-hosted status pages** (Statuspage.io, Instatus) — Good for external status but don't integrate with on-prem AD infrastructure. No AD-specific health metrics.

**The gap:** No lightweight, open-source, self-hosted dashboard existed that could be deployed in minutes (pip install flask, python3 app.py), run on a Raspberry Pi or cheap VPS, and give ops teams a single-pane-of-glass view of their AD health without enterprise overhead.

### What Triggered Development

The initial commit (03e86ad, Feb 4 2026) was titled "Add files via upload" and described the repo as a **"starter version"** of a DC monitoring dashboard — explicitly "SAFE to upload publicly to GitHub" with no credentials, no domain names, no secrets. The original README listed next phases: add PowerShell collector, add authentication, add database, add alerts.

The repo was **renamed** from its original name to `ADSentinel` (commit `d951861`, June 17 2026), indicating a branding and scoping decision to make it a standalone, publishable tool rather than an internal prototype. The rename aligned it with the JorahOne portfolio naming convention.

Subsequent development followed a J1 Pipeline pattern:
- **June 30, 2026** — CI/health endpoint added (ADS-001, ADS-002, ADS-003 tickets), review findings captured, screenshot updated
- **July 4, 2026** — Portfolio standardization: community files (SECURITY.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md), CI/CD (CodeQL, Dependabot), CHANGELOG, issue/PR templates
- **July 5, 2026** — Security audit: secret scan, smoke tests (3/3 passing), `.env.example`, config standardization

The rapid standardization suggests ADSentinel was being prepared for **public open-source release** as a first-class JorahOne project.

### Ecosystem Fit

ADSentinel is part of JorahOne's **infrastructure observability and automation** portfolio:

```
JorahOne Ecosystem
├── ADSentinel              ← AD-specific monitoring dashboard
├── [other infra tools]     ← Broader infrastructure monitoring/automation
└── J1 Pipeline             ← Lifecycle management for all J1 repos
```

The tool serves both **internal JorahOne operations** (monitoring their own AD infrastructure) and **external users** (open-source community, IT ops teams at small-to-mid-size organizations). It follows J1 standards (SECURITY.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CodeQL, Dependabot, CHANGELOG, issue/PR templates), making it a first-class J1 project eligible for the full pipeline lifecycle.

---

## Operational Classification

**Classification: EXPERIMENTAL / EARLY PRODUCTION**

Evidence for **Production**:
- v1.0.0 released (2026-07-04) with CHANGELOG
- Health endpoint (`/health`) for deployment monitoring hooks
- CodeQL security analysis CI (Python + JavaScript/TypeScript)
- Dependabot configured for automated dependency updates
- Issue templates (bug report, feature request) and PR template
- SECURITY.md with vulnerability reporting policy and 90-day disclosure timeline
- CONTRIBUTING.md with contribution guidelines
- CODE_OF_CONDUCT.md (Contributor Covenant v2.1)
- MIT License
- Security audit performed (commit 07815b7 — secret scan, config standardization)
- Smoke tests exist (3/3 passing)

Evidence for **Experimental** (countervailing):
- `mock_dc_status.json` is an empty array `[]` — the dashboard renders hardcoded HTML data, not dynamic template data
- `ldap_service.ps1` and `notifications.ps1` are single-line placeholders
- **No Dockerfile exists** despite README claiming `docker build -t adsentinel .`
- No test suite in current HEAD (tests exist on `audit/ADSentinel` branch but not merged to main)
- No real AD data pipeline — the Flask app loads mock data but the template doesn't consume it dynamically
- The dashboard HTML contains hardcoded example data (DC-East, DC-West, DC-Central, DC-Factory) rather than rendering from the JSON payload
- `docs/` files are placeholders ("Roadmap placeholder", "GitHub steps placeholder")
- No git tags
- No database, no authentication, no persistent storage

**Verdict:** The scaffolding for a production tool is in place (CI/CD, community files, security policy, health checks), but the core data pipeline is incomplete. The dashboard is a static mockup, not a live monitoring tool. Classification: **Experimental** — the intent is production, but the implementation is not yet there.

---

## Key Architectural Decisions

1. **Single Flask process, no database** — The system is intentionally minimal: one Python file, two Jinja2 templates, no database, no message queue, no container orchestration. This makes it trivially deployable (`pip install flask && python3 app.py`) but limits it to mock/static data until a real data pipeline is built.

2. **PowerShell collectors for AD data** — PowerShell is the native scripting language for Windows Server/AD administration. Using PowerShell scripts (rather than Python LDAP libraries) means collectors can leverage existing AD PowerShell modules (`Get-ADDomainController`, `repadmin`, `dcdiag`) without additional dependencies. The tradeoff: collectors must run on Windows, while the dashboard runs on any platform with Python.

3. **File-based mock data** — `mock_dc_status.json` serves as the data contract between collectors and the dashboard. The collector writes JSON to disk; the Flask app reads it on startup. This is simple but means the dashboard shows stale data until the collector runs again. No real-time push mechanism.

4. **Hardcoded template data as fallback** — The dashboard HTML embeds example DC data (DC-East, DC-West, etc.) directly in the template rather than rendering from the JSON payload. This was likely a prototyping shortcut that was never refactored. The template receives `dc_data` from Flask but doesn't use it dynamically.

5. **No authentication layer** — The admin dashboard (`/`) is unprotected. The original README listed authentication as a "next phase" item. This is acceptable for an experimental/internal tool but would need addressing before public production deployment.

6. **J1 portfolio standardization applied retroactively** — Community files, CI/CD, and issue templates were added in bulk (commit 27d1749) after the core app was built. This is a deliberate J1 pipeline pattern: build the prototype first, then standardize for open-source release.

---

## Repository Structure

```
ADSentinel/
├── app.py                       # Flask web server (20 LOC, single file)
├── requirements.txt             # Dependency: flask
├── mock_dc_status.json          # Mock data file (currently empty array [])
├── .env.example                 # Config template (SECRET_KEY, HOST, PORT, MOCK_DATA_PATH)
├── .gitignore                   # Python/IDE/OS/build ignores
├── CHANGELOG.md                 # v1.0.0 — 2026-07-04
├── LICENSE                      # MIT © OneByJorah
├── README.md                    # Full README with badges, features, architecture, API, deployment
├── ROADMAP.md                   # Placeholder (11 lines, generic items)
├── SECURITY.md                  # Vulnerability reporting policy
├── CONTRIBUTING.md              # Contribution guidelines
├── CODE_OF_CONDUCT.md           # Contributor Covenant v2.1
├── templates/
│   ├── dashboard.html           # Admin dashboard (247 LOC, dark theme, hardcoded data)
│   └── public.html              # Public status page (32 LOC, static)
├── collectors/
│   ├── mock_dc_collector.ps1    # PowerShell mock collector (functional, 28 LOC)
│   ├── ldap_service.ps1         # Placeholder (1 line)
│   └── notifications.ps1        # Placeholder (1 line)
├── docs/
│   ├── ROADMAP.md               # Placeholder ("Roadmap placeholder")
│   └── GITHUB_STEPS.txt         # Placeholder ("GitHub steps placeholder")
├── assets/
│   └── screenshot.png           # Dashboard screenshot
└── .github/
    ├── workflows/codeql.yml     # CodeQL analysis (Python + JS/TS)
    ├── dependabot.yml           # Dependabot (pip, npm, docker, github-actions)
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## Notes

- **Naming history:** The repo was originally named something other than ADSentinel (likely "DC Status Dashboard" or similar). It was renamed to ADSentinel in commit `d951861` (June 17, 2026). The initial README explicitly called it a "starter version" safe for public upload.

- **Dependabot ecosystem mismatch:** Dependabot is configured for `npm` and `docker` ecosystems, but no `package.json` or `Dockerfile` exists in the repo. This is a template vestige from the J1 portfolio standardization — the npm and docker entries should be removed until those artifacts exist.

- **No Dockerfile despite README claim:** The README includes `docker build -t adsentinel .` instructions, but no `Dockerfile` exists. This is a documentation gap.

- **Dashboard data is hardcoded, not dynamic:** The Flask app loads `mock_dc_status.json` and passes it as `dc_data` to the template, but `dashboard.html` renders hardcoded example DCs (DC-East, DC-West, DC-Central, DC-Factory) rather than iterating over `dc_data`. The mock data pipeline exists in code but is not wired to the UI.

- **Empty directories:** None. All directories contain at least one file.

- **Security audit in history:** Commit `07815b7` (July 5, 2026) performed a security audit including secret scan, placeholder IP/email replacement, and config standardization. This is a positive maturity signal.

- **Pipeline branches exist:** `audit/ADSentinel`, `brand-align/ADSentinel`, `pipeline/auto-review-ADSentinel-2026-06-30` — indicating J1 Pipeline phases have been run on this repo.

- **No git tags:** Despite a v1.0.0 CHANGELOG entry, no corresponding git tag exists.

- **Smoke tests exist on audit branch:** 3 tests (dashboard route, public route, app config) pass on the `audit/ADSentinel` branch but are not merged to `main`.

---

*This document was produced by J1-PIPELINE Phase -1 (ORACLE). It represents a read-only analysis of the repository's structure, history, and engineering intent. No code was modified.*
