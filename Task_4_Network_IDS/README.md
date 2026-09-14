# Task 4: Network Intrusion Detection System (Snort NIDS)

## Technical Overview
This module demonstrates the deployment and operational configuration of Snort, an open-source Network Intrusion Detection System (NIDS). The system is configured with custom signature rules to monitor, detect, and log suspicious network traffic patterns in real time.

## Snort Configuration & Rule Syntax

Custom detection logic is added to `/etc/snort/rules/local.rules`:

    alert icmp any any -> any any (msg:"[SECURITY ALERT] ICMP Echo Ping Scan Detected"; sid:1000001; rev:1;)

### Rule Syntax Decomposition
* **Action (`alert`):** Generates a real-time security log entry when criteria are met.
* **Protocol (`icmp`):** Specifies the network protocol to monitor.
* **Source/Destination (`any any -> any any`):** Matches traffic originating from any IP/Port directed to any IP/Port.
* **Rule Options:**
  * `msg`: Human-readable string logged upon rule trigger.
  * `sid`: Snort ID (Custom rules use values >= 1000001).
  * `rev`: Rule revision version tracking.

## Deployment Instructions

1. Install Snort (Linux / WSL):

    sudo apt update && sudo apt install snort -y

2. Append Custom Rules:

    sudo cat local.rules >> /etc/snort/rules/local.rules

3. Determine Active Network Interface:

    ip addr

4. Launch Snort in NIDS Console Mode:

    sudo snort -A console -q -c /etc/snort/snort.conf -i eth0

    (Note: Replace eth0 with your active interface name).

## Triggering & Verifying Security Alerts

In a secondary terminal window, generate test ICMP traffic:

    ping -c 3 8.8.8.8

### Expected NIDS Console Log Output

    09/14-20:10:01.402118 [**] [1:1000001:1] [SECURITY ALERT] ICMP Echo Ping Scan Detected [**] [Priority: 0] {ICMP} 192.168.1.50 -> 8.8.8.8
    09/14-20:10:02.403251 [**] [1:1000001:1] [SECURITY ALERT] ICMP Echo Ping Scan Detected [**] [Priority: 0] {ICMP} 192.168.1.50 -> 8.8.8.8
