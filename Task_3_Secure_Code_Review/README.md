# Task 3: Secure Coding Review & Audit

## Technical Overview
This project demonstrates an end-to-end Application Security (AppSec) audit cycle. It includes identifying critical vulnerabilities within a target application using Static Application Security Testing (SAST), documenting root causes, and implementing remediation according to secure coding standards.

## Vulnerability Identification (SAST Audit)

Automated analysis performed using Bandit:

    pip install -r requirements.txt
    bandit -r vulnerable_app.py

### Findings Matrix

| CWE ID | Vulnerability Category | Severity | Description & Root Cause |
| :--- | :--- | :--- | :--- |
| **CWE-798** | Hard-coded Credentials | **HIGH** | Plaintext API secret key embedded directly in source code (`API_SECRET_KEY`). |
| **CWE-78** | OS Command Injection | **HIGH** | Unsanitized input concatenated directly into `os.system()`, enabling arbitrary command execution. |

## Remediation Details

1. **CWE-798 Mitigation:**
   * Removed inline secrets.
   * Leveraged standard `os.getenv("APP_API_KEY")` pattern to enforce dynamic environment variable injection.

2. **CWE-78 Mitigation:**
   * Replaced dangerous system shell invocation (`os.system`) with parameterized process creation via `subprocess.run()`.
   * Enforced strict input validation utilizing Python's native `ipaddress` validation module.

## Verification

Run Bandit against the remediated file to verify zero high-severity findings:

    bandit -r secure_app.py
