# DC Status Dashboard

An open-source Active Directory monitoring dashboard created to provide full operational visibility without the limitations of vendor licensing models.

This repository represents the **initial public foundation** of the project and is intentionally safe for public distribution.

---

## What This Repository Contains

- Flask-based dashboard with mock data
- Clean, responsive UI designed for operational readability
- Admin dashboard and public read-only status page
- Modular structure prepared for future expansion

---

## What This Repository Does NOT Contain

- No credentials
- No domain names
- No secrets
- No production monitoring logic (yet)

This ensures the project is safe to clone, review, and contribute to publicly.

---

## Project Background & Motivation

This project was started in response to real-world operational challenges encountered in a K-12 IT environment.

Many enterprise monitoring solutions impose strict limitations on their free or entry-level tiers, including:
- Device or node count caps
- Feature restrictions
- Limited data retention
- Rapidly escalating licensing costs as environments grow

In environments with constrained budgets and a large number of mission-critical systems—such as Domain Controllers, DNS, DHCP, and authentication services—these limitations can significantly reduce visibility and operational awareness.

This dashboard was created to:

- Provide **unrestricted visibility** into critical Active Directory services
- Eliminate artificial limitations imposed by vendor licensing models
- Enable full customization based on real operational requirements
- Support transparency through a public, read-only service status page
- Serve as a practical monitoring solution built by an administrator actively responsible for these systems

Beyond addressing an immediate operational need, this project also represents:
- A hands-on learning initiative driven by real infrastructure challenges
- A continuously evolving professional toolset
- A demonstration of proactive problem-solving in constrained environments

The project is intentionally open, modular, and extensible, allowing for future expansion, customization, and community contribution.

---

## Roadmap (Planned Phases)

1. PowerShell-based collector agents running on Domain Controllers  
2. Secure API ingestion and data persistence  
3. Authentication and role-based access control  
4. Alerting integrations (Email, Microsoft Teams)  
5. Historical uptime tracking and visualization  

---

## Project Status

This repository currently contains **mock data only** and serves as the public foundation of the project.  
Production data collection, authentication, and alerting will be introduced in future phases.
