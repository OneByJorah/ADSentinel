# Roadmap

## Current
- Production stability improvements
- Documentation enhancements
- Test coverage expansion

## Next
- Feature enhancements
- Performance optimization
- Community contributions

## Planned

### Phase 1 — Real Data Pipeline
- Wire `mock_dc_status.json` data to dashboard template (replace hardcoded DC entries)
- Implement live PowerShell collector integration
- Add data refresh mechanism (polling or file watcher)

### Phase 2 — Authentication & Security
- Add Flask-Login or HTTP Basic Auth for admin dashboard
- Configure HTTPS (TLS certificate)
- Add security headers (CSP, HSTS, X-Frame-Options)
- Add rate limiting

### Phase 3 — Persistence & History
- Add SQLite database for historical DC status data
- Implement trend analysis and historical charts
- Add audit logging

### Phase 4 — Docker & Deployment
- Create Dockerfile for containerized deployment
- Add docker-compose.yml with health checks
- Add .dockerignore

### Phase 5 — Alerting
- Implement Teams/Telegram notifications (see collectors/)
- Add configurable alert thresholds
- Add escalation policies

### Phase 6 — Advanced Monitoring
- Real-time WebSocket updates
- Multi-forest support
- LDAP service management
- Performance counter dashboards
