# Task 1: Basic Network Sniffer

## Technical Overview
This module provides a real-time network packet sniffer implemented in Python using `Scapy`. It hooks into the network interface to intercept IPv4 datagrams, parse transport layer headers (TCP, UDP, ICMP), and print formatted summaries alongside raw packet payload snippets.

## Features
* **IPv4 Header Decoding:** Extracts Source/Destination IP addresses, Time-To-Live (TTL), and Protocol identification.
* **Transport Layer Analysis:** Decodes TCP/UDP source and destination ports.
* **Payload Inspection:** Safely sanitizes and previews raw application-layer payload data.
* **Graceful Exception Handling:** Safeguards against missing dependencies and privilege errors.

## Installation & Execution

1. Install required dependencies:

    pip install -r requirements.txt

2. Execute with root privileges (required for raw socket capture):

    sudo python3 sniffer.py

## Example Console Output

    ==================================================
          CodeAlpha - Network Packet Sniffer         
    ==================================================
    [*] Listening on active default interface...
    [*] Press Ctrl+C to stop packet capture.

    [IP] 192.168.1.50 -> 142.250.190.46 | Proto: TCP | TTL: 64 | Ports: 52140 -> 443
        └── Payload Snippet: \x16\x03\x01\x02\x00\x01\x00\x01...
    [IP] 192.168.1.1 -> 192.168.1.50 | Proto: UDP | TTL: 255 | Ports: 53 -> 52140
