#!/usr/bin/env python3
"""
Task 3: Remediated Secure Application
Author: CodeAlpha Intern
Description: Secure implementation addressing CWE-798 and CWE-78 vulnerabilities.
"""

import os
import sys
import subprocess
import ipaddress

def get_api_key():
    # REMEDIATION CWE-798: Retrieve credential from system environment variables
    api_key = os.getenv("APP_API_KEY")
    if not api_key:
        print("[!] Security Error: APP_API_KEY environment variable is not configured.")
        sys.exit(1)
    return api_key

def validate_host(host_input):
    # REMEDIATION CWE-78: Strict input validation ensuring host is a valid IPv4/IPv6 address
    try:
        ip = ipaddress.ip_address(host_input)
        return str(ip)
    except ValueError:
        raise ValueError("Invalid target host. Input must be a valid IP address.")

def execute_diagnostics():
    print("--- Secure Network Diagnostic Tool ---")
    _ = get_api_key()

    user_input = input("Enter target IP to audit: ").strip()

    try:
        sanitized_ip = validate_host(user_input)
    except ValueError as err:
        print(f"[!] Input Error: {err}")
        return

    print(f"[*] Executing safe diagnostic ping against: {sanitized_ip}")

    # REMEDIATION CWE-78: Avoid shell invocation; pass arguments as an explicit array
    try:
        result = subprocess.run(
            ["ping", "-c", "1", sanitized_ip],
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )
        print(result.stdout)
    except subprocess.CalledProcessError:
        print("[!] Diagnostic check failed: Target unreachable.")
    except subprocess.TimeoutExpired:
        print("[!] Diagnostic check timed out.")

if __name__ == "__main__":
    execute_diagnostics()
