# SecureScan
Developed an automated tool to scan, detect, and report vulnerabilities in web applications using both static and dynamic analysis techniques. Designed for ease of use by developers and security engineers to integrate into CI/CD pipelines.

# Tech Stack
Python, Flask, Nmap, OWASP ZAP API, GitHub Actions, MongoDB, Docker

# key Highlights
Built a Python-based engine that integrates with OWASP ZAP API and Nmap to perform both DAST and basic network scans.

Implemented custom vulnerability scoring based on CVSS to prioritize findings.

Developed a Flask web dashboard to visualize scan reports, filtered by severity, CVE ID, and endpoint.

Added GitHub Actions integration to run automated scans on every pull request or push to the main branch.

Dockerized the entire application for portability and easy deployment in cloud or on-prem environments.

Designed role-based access controls for secure multi-user access to scan reports and settings.

# Folder Structure 
SecureScan/
├── backend/
│   ├── app.py                     # Flask app entry point
│   ├── config.py                  # Environment config (Mongo URI, secrets, etc.)
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── auth/                      # Authentication & user management
│   │   ├── routes.py
│   │   └── utils.py
│   ├── scanners/                  # ZAP & Nmap integration
│   │   ├── zap_scan.py
│   │   ├── nmap_scan.py
│   │   └── cve_lookup.py          # (Optional) Auto fetch CVE info via NVD API
│   ├── database/
│   │   ├── db.py
│   │   └── models.py              # Mongo models, e.g., Scan, User
│   ├── routes/
│   │   ├── scan_routes.py         # Endpoints for running scans
│   │   ├── report_routes.py       # Download/export routes
│   │   └── dashboard_routes.py    # Scan summary, chart APIs
│   └── templates/
│       ├── index.html
│       ├── report_template.html   # For PDF exports
│       └── login.html
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── charts.js          # Chart.js visualizations
│   └── README.md
│
├── scripts/
│   ├── zap_headless.sh           # Script to run ZAP in headless
│   └── ci_scan.py                # Used in GitHub Actions
│
├── .github/
│   └── workflows/
│       └── scan.yml              # GitHub Actions CI workflow
│
├── docker-compose.yml
├── README.md
└── LICENSE
# SecureScan 🔐

SecureScan is an automated vulnerability and port scanner for modern DevSecOps workflows. Built with Flask, OWASP ZAP, Nmap, MongoDB, and GitHub Actions.

## Features

- 🌐 Web UI to trigger scans
- 🛡️ OWASP ZAP for web vulnerability scanning
- ⚡ Nmap for network scanning
- 🧠 MongoDB to store and query scan history
- 🚀 GitHub Actions CI/CD support
- 🐳 Dockerized

## Quick Start

```bash
docker-compose up





