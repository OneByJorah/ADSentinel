# Phase 3 — GUARDIAN (Security) Report

**Repository:** `OneByJorah/DirWatch`
**Date:** 2026-07-05
**Analyst:** J1-PIPELINE GUARDIAN

---

## Security Score: 25/100 — CRITICAL

| Category | Status | Score | Notes |
|----------|--------|-------|-------|
| Authentication / Authorization | ❌ MISSING | 0/100 | No auth on admin dashboard |
| HTTPS / TLS | ❌ MISSING | 0/100 | No TLS configured |
| CSP / Security Headers | ❌ MISSING | 0/100 | No security headers |
| Docker Hardening | N/A | N/A | No Dockerfile exists |
| Rootless Containers | N/A | N/A | No Dockerfile exists |
| Supply Chain | ⚠️ DEGRADED | 40/100 | Dependabot configured but no lock file |
| Secrets Management | ⚠️ DEGRADED | 60/100 | No `.env.example`, hardcoded IP in template |
| SBOM | ❌ MISSING | 0/100 | No SBOM generated |
| AppArmor / SELinux | N/A | N/A | No container deployment |
| Rate Limiting | ❌ MISSING | 0/100 | No rate limiting on any endpoint |

---

## Detailed Findings

### 1. Authentication / Authorization — CRITICAL

**Finding:** The admin dashboard (`/` route) has **no authentication whatsoever**. Anyone who can reach the Flask server on port 5000 can view all DC metrics, including potentially sensitive infrastructure information (IP addresses, DC names, service status).

**Risk:** Unauthenticated access to infrastructure monitoring data. An attacker who gains network access to the Flask port can enumerate domain controllers, their IPs, and their health status — valuable reconnaissance data.

**Recommendation:** Add Flask-Login or HTTP Basic Auth for the `/` route. The `/public` route can remain unauthenticated.

### 2. HTTPS / TLS — CRITICAL

**Finding:** The Flask app runs on HTTP with no TLS. The `app.run()` call has no SSL context configured.

**Risk:** All traffic between the dashboard and users is in plaintext. Session data, DC status, and any future credentials would be exposed to network sniffing.

**Recommendation:** Configure Flask with TLS (certificate + key) or deploy behind a reverse proxy (nginx/Caddy) that terminates TLS.

### 3. CSP / Security Headers — CRITICAL

**Finding:** No Content Security Policy (CSP) headers, no X-Content-Type-Options, no X-Frame-Options, no HSTS headers are set. The Flask app does not configure any security response headers.

**Risk:** Vulnerable to XSS, clickjacking, MIME-type sniffing attacks. The dashboard template includes inline `<style>` and `<script>` blocks with no CSP to restrict what can execute.

**Recommendation:** Add Flask-Talisman or middleware to set security headers:
- `Content-Security-Policy`
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Strict-Transport-Security` (if HTTPS is configured)

### 4. Docker Hardening — N/A

**Finding:** No Dockerfile exists. Docker hardening checks are not applicable until a container image is created.

**Note:** When a Dockerfile is created, it should follow Docker hardening best practices:
- Use a non-root user
- Use a minimal base image (python:3.10-slim or alpine)
- Set `USER` directive
- Add `HEALTHCHECK` instruction
- Don't run as root

### 5. Rootless Containers — N/A

**Finding:** No Dockerfile exists. Rootless container checks are not applicable.

### 6. Supply Chain Security — DEGRADED

**Findings:**
- **Dependabot configured** for `pip` ecosystem — ✅ Good
- **No lock file** — ❌ `requirements.txt` has no version pin, making Dependabot less effective
- **Dependabot ecosystem mismatch** — `npm` and `docker` configured but no corresponding artifacts (template vestiges)
- **No `pip-audit` or `safety` scan** — No automated CVE scanning for Python dependencies
- **CodeQL configured** — ✅ Good, covers Python and JavaScript/TypeScript

**Recommendation:** Pin Flask version, generate lock file, add `pip-audit` to CI, remove mismatched Dependabot ecosystems.

### 7. Secrets Management — DEGRADED

**Findings:**
- **No `.env.example`** — Referenced in INTENT.md but file does not exist on disk
- **Hardcoded IP in template** — `dashboard.html` contains `67.211.240.4` as a hardcoded external IP
- **Hardcoded example subnets** — `192.168.x.0/24` ranges in template (acceptable for demo data)
- **Security audit performed** (commit `07815b7`) — ✅ Good, placeholder IPs/emails were sanitized
- **`.gitignore` includes `.env`** — ✅ Good, prevents accidental secret commits

**Recommendation:** Create `.env.example` with documented variables. Replace hardcoded IP with a configurable variable or remove it.

### 8. SBOM — CRITICAL

**Finding:** No Software Bill of Materials (SBOM) has been generated for this project. Without an SBOM, there is no machine-readable inventory of dependencies for vulnerability tracking.

**Recommendation:** Generate an SBOM using `cyclonedx-bom` or `pip-audit` and include in CI pipeline.

### 9. AppArmor / SELinux — N/A

**Finding:** No container deployment exists. AppArmor/SELinux profiles are not applicable.

### 10. Rate Limiting — CRITICAL

**Finding:** No rate limiting is configured on any endpoint. The Flask app has no protection against brute-force attacks, DoS, or abuse.

**Risk:** An attacker could flood the `/` or `/public` endpoints with requests, consuming server resources. If authentication is added later, the login endpoint would be vulnerable to brute-force attacks without rate limiting.

**Recommendation:** Add Flask-Limiter or similar rate limiting middleware.

---

## Security Items Requiring Fixer Attention

### CRITICAL
1. **No authentication on admin dashboard** — `/` route is completely unprotected
2. **No HTTPS/TLS** — All traffic in plaintext
3. **No security headers (CSP, HSTS, XFO, XCTO)** — Vulnerable to XSS/clickjacking
4. **No rate limiting** — No DoS protection
5. **No SBOM** — No dependency inventory for vulnerability tracking

### DEGRADED
6. **No `.env.example`** — Missing config template
7. **Hardcoded IP in template** — `67.211.240.4` in `dashboard.html`
8. **Dependabot ecosystem mismatch** — `npm` and `docker` configured without artifacts
9. **No lock file** — Unpinned dependencies
