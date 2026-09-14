#!/usr/bin/env python3
"""
Task 1: Basic Network Sniffer
Author: CodeAlpha Intern
Description: Captures live IPv4 packets and displays key header fields and payloads.
"""

import sys
import logging
try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
except ImportError:
    print("[!] Scapy is not installed. Run: pip install scapy")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def process_packet(packet):
    if not packet.haslayer(IP):
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    proto_num = packet[IP].proto
    ttl = packet[IP].ttl

    protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
    proto_name = protocol_map.get(proto_num, f"Other({proto_num})")

    log_msg = f"[IP] {src_ip} -> {dst_ip} | Proto: {proto_name} | TTL: {ttl}"

    if packet.haslayer(TCP):
        log_msg += f" | Ports: {packet[TCP].sport} -> {packet[TCP].dport}"
    elif packet.haslayer(UDP):
        log_msg += f" | Ports: {packet[UDP].sport} -> {packet[UDP].dport}"

    print(log_msg)

    if packet.haslayer(Raw):
        payload = bytes(packet[Raw].load)
        snippet = payload[:32].decode("utf-8", errors="replace").replace("\n", " ")
        print(f"    └── Payload Snippet: {snippet}...")

def main():
    print("==================================================")
    print("      CodeAlpha - Network Packet Sniffer         ")
    print("==================================================")
    print("[*] Listening on active default interface...")
    print("[*] Press Ctrl+C to stop packet capture.\n")

    try:
        sniff(prn=process_packet, store=False, count=20)
        print("\n[*] Capture completed successfully.")
    except PermissionError:
        print("[!] Error: Root/Administrator privileges are required to capture raw network packets.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[*] Capture interrupted by user. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
