#!/usr/bin/env python3
"""
Task 3: Insecure Application Target
Author: CodeAlpha Intern
Description: Demonstrates severe security flaws for SAST analysis (CWE-798 & CWE-78).
"""

import os

# VULNERABILITY 1: CWE-798 (Use of Hard-coded Credentials)
API_SECRET_KEY = "SUPER_SECRET_PRODUCTION_KEY_998811"

def execute_diagnostics():
    print("--- Network Diagnostic Tool ---")
    
    # VULNERABILITY 2: CWE-78 (Improper Neutralization of Special Elements used in an OS Command)
    target_host = input("Enter target host/IP to audit: ")
    
    print(f"[*] Ping status for target: {target_host}")
    # Insecure: Unsanitized user input passed directly to system shell
    os.system("ping -c 1 " + target_host)

if __name__ == "__main__":
    execute_diagnostics()
