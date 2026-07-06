# Phase 1 — AUDITOR Report

**Repository:** `OneByJorah/ADSentinel`
**Date:** 2026-07-05
**Analyst:** J1-PIPELINE AUDITOR

---

## Summary

| Category | Status | Score |
|----------|--------|-------|
| Lint / Formatting | ⚠️ DEGRADED | 60/100 |
| Dead Code | ⚠️ DEGRADED | 50/100 |
| Dependency Review | ✅ PASS | 90/100 |
| CVEs | ✅ PASS | 100/100 |
| SBOM | ❌ MISSING | 0/100 |
| Secrets (gitleaks) | ✅ PASS | 100/100 |
| License Compliance | ✅ PASS | 100/100 |
| GitHub Actions | ✅ PASS | 90/100 |
| README Compliance | ⚠️ DEGRADED | 65/100 |
| Tests | ❌ MISSING | 0/100 |
| Docker | ❌ MISSING | 0/100 |
| Folder Structure | ✅ PASS | 90/100 |

**Overall Audit Score: 54/100 — CRITICAL**

---

## 1. Lint & Formatting

### Findings

- **No linter configuration** — No `.flake8`, `.pylintrc`, `pyproject.toml` with linting rules, or `ruff.toml` exists
- **No formatter config** — No `.editorconfig`, no `black`/`ruff` formatter config
- **Code quality:** `app.py` is 20 lines — minimal surface area, but no linting pipeline
- **HTML templates:** No HTML linter configured; inline CSS/JS in templates is not validated
- **PowerShell scripts:** No PSScriptAnalyzer or linting for `.ps1` files

### Recommendation
Add `ruff` or `flake8` configuration and a lint step to CI. Add `.editorconfig`.

---

## 2. Dead Code

### Findings

- **`mock_dc_status.json` is an empty array `[]`** — The Flask app loads it on startup but the data is never consumed by the template. The file exists as a data contract placeholder but serves no runtime purpose.
- **`dc_data` passed to template but unused** — `render_template("dashboard.html", dc_data=data)` passes the mock data, but `dashboard.html` renders hardcoded DC entries (DC-East, DC-West, DC-Central, DC-Factory) instead of iterating over `dc_data`.
- **`ldap_service.ps1`** — Single comment line placeholder, no functional code
- **`notifications.ps1`** — Single comment line placeholder, no functional code
- **`docs/ROADMAP.md`** — Contains only "Roadmap placeholder" (19 bytes)
- **`docs/GITHUB_STEPS.txt`** — Contains only "GitHub steps placeholder" (24 bytes)
- **`ROADMAP.md` (root)** — Generic 11-line placeholder with no actionable roadmap items

### Recommendation
Remove or implement placeholder files. Wire `dc_data` to the template for dynamic rendering.

---

## 3. Dependency Review

### Findings

- **`requirements.txt`** contains a single dependency: `flask` (no version pin)
- **No `pip freeze` or lock file** — No `requirements-lock.txt`, no `Pipfile.lock`, no `poetry.lock`
- **No version pinning** — `flask` without a version means builds are non-reproducible

### Recommendation
Pin Flask version in `requirements.txt` and generate a lock file.

---

## 4. CVEs

### Findings

- **No known CVEs in the codebase itself** — The application is 20 lines of Flask with no external API calls, no database, no file uploads, no user input processing
- **Dependency CVEs cannot be assessed** without a lock file or pinned versions
- **Dependabot is configured** for `pip` ecosystem, which will flag CVEs once versions are pinned

### Recommendation
Pin Flask version and let Dependabot flag any CVEs.

---

## 5. SBOM

### Findings

- **No SBOM (Software Bill of Materials) generated**
- No `cyclonedx` or `spdx` manifest
- No `pip-audit` or `safety` scan configured

### Recommendation
Generate an SBOM using `pip-audit` or `cyclonedx-bom` and include in CI.

---

## 6. Secrets (gitleaks)

### Findings

- **No secrets detected in current codebase** — The repo was explicitly designed as "SAFE to upload publicly to GitHub" (per initial commit message)
- **Security audit performed** (commit `07815b7`) included secret scan — placeholder IPs/emails were sanitized
- **Hardcoded IP addresses in template** — `dashboard.html` contains `67.211.240.4` as a hardcoded external IP in the topbar pill. This is a placeholder IP but should be reviewed.
- **Hardcoded subnet references** — `192.168.1.0/24`, `192.168.2.0/24`, etc. in the template are example data, not real infrastructure

### Recommendation
Replace hardcoded IP `67.211.240.4` with a dynamic placeholder or remove it.

---

## 7. License Compliance

### Findings

- **MIT License** — Present and correct at `LICENSE`
- **Copyright holder:** OneByJorah (2026)
- **License referenced in README** — Yes
- **No license header in source files** — `app.py` and `.ps1` files lack SPDX license identifiers

### Recommendation
Add SPDX license headers to source files.

---

## 8. GitHub Actions

### Findings

- **CodeQL workflow** — Present and correctly configured for Python + JavaScript/TypeScript
- **Dependabot** — Configured for `pip`, `npm`, `docker`, and `github-actions` ecosystems
- **Dependabot ecosystem mismatch:** `npm` and `docker` ecosystems are configured but no `package.json` or `Dockerfile` exists — these are template vestiges
- **No lint/test CI workflow** — Only CodeQL runs; no unit tests, no linting, no build verification

### Recommendation
Remove `npm` and `docker` from Dependabot config until those artifacts exist. Add a lint/test CI workflow.

---

## 9. README Compliance

### Findings

- **README exists** — Yes, comprehensive with badges, features, quick start, architecture, API, deployment
- **Missing `.env.example`** — Referenced in INTENT.md but file does not exist on disk
- **Docker instructions without Dockerfile** — README shows `docker build -t adsentinel .` but no `Dockerfile` exists
- **No health endpoint documented** — The `/health` endpoint exists in code but is not documented in the API table
- **No testing section** — No instructions for running tests
- **No contributing section** — README doesn't link to CONTRIBUTING.md
- **No security section** — README doesn't link to SECURITY.md
- **No screenshot shown** — `assets/screenshot.png` exists but is not embedded in README

### Recommendation
Create `.env.example`, add `/health` to API table, add testing/contributing/security sections, embed screenshot.

---

## 10. Tests

### Findings

- **No test files on `main` branch** — Zero test files in the repository
- **Smoke tests exist on `audit/ADSentinel` branch** — 3 tests (dashboard route, public route, app config) pass but are not merged to `main`
- **No test framework configured** — No `pytest`, `unittest`, or test runner config

### Recommendation
Merge smoke tests from audit branch to main. Add `pytest` configuration.

---

## 11. Docker

### Findings

- **No Dockerfile exists** — Despite README claiming `docker build -t adsentinel .`
- **No `.dockerignore`** — Would be needed if Dockerfile existed
- **Dependabot configured for `docker`** — Template vestige, no Docker artifacts to update

### Recommendation
Create a `Dockerfile` or remove Docker references from README and Dependabot.

---

## 12. Folder Structure

### Findings

- **Clean, well-organized structure** — Logical separation of templates, collectors, docs, assets, and GitHub config
- **No empty directories** — All directories contain at least one file
- **No nested submodules** — Clean single-level structure
- **Minor issue:** `docs/` contains only placeholder files — should be substantive or removed

### Recommendation
Populate `docs/` with real documentation or remove the directory.

---

## Items Requiring Fixer Attention

### CRITICAL
1. **No Dockerfile despite README claim** — Documentation is misleading; either create Dockerfile or fix README
2. **No `.env.example`** — Referenced in INTENT.md but missing from disk
3. **No test files on `main`** — Zero test coverage
4. **Dashboard data is hardcoded, not dynamic** — `dc_data` passed to template but ignored

### DEGRADED
5. **Placeholder files** — `ldap_service.ps1`, `notifications.ps1`, `docs/ROADMAP.md`, `docs/GITHUB_STEPS.txt`, `ROADMAP.md` are stubs
6. **Dependabot ecosystem mismatch** — `npm` and `docker` configured but no corresponding artifacts
7. **No version pinning** — `flask` without version in `requirements.txt`
8. **No linting/formatting config** — No `.editorconfig`, no linter config
9. **No SBOM** — No software bill of materials
10. **Hardcoded IP in template** — `67.211.240.4` in `dashboard.html`
