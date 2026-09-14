# CodeAlpha Cybersecurity Engineering Portfolio

This repository contains the production-grade implementation of the required engineering tasks for the CodeAlpha Cybersecurity Internship. The projects encompass packet analysis, application security (AppSec) auditing, and network threat detection.

## Engineering Overview

| Task ID | Domain | Solution | Tech Stack | Security Value |
| :--- | :--- | :--- | :--- | :--- |
| **Task 1** | Network Security | Custom Packet Sniffer | Python 3, Scapy | Low-level packet inspection & protocol analysis |
| **Task 3** | Application Security | SAST Audit & Remediation | Python, Bandit, Subprocess | Vulnerability mitigation (CWE-78, CWE-798) |
| **Task 4** | Threat Detection | Snort NIDS Deployment | Snort 2.9+, Linux/WSL | Signature-based intrusion detection & alert logging |

---

## Directory Navigation

* [`Task_1_Network_Sniffer/`](./Task_1_Network_Sniffer/): Real-time packet capture engine capable of decoding IPv4, TCP, UDP, and ICMP frame headers and raw payload slices.
* [`Task_3_Secure_Code_Review/`](./Task_3_Secure_Code_Review/): Source code security review utilizing Static Application Security Testing (SAST) tools to remediate Command Injection and Credential Exposure risks.
* [`Task_4_Network_IDS/`](./Task_4_Network_IDS/): Deployment configuration for Snort NIDS, including custom detection rule definitions (`local.rules`) for live network threat monitoring.

---

## System Requirements & Prerequisites

* **Operating System:** Linux (Ubuntu 22.04 LTS recommended) or Windows Subsystem for Linux (WSL2).
* **Language Runtime:** Python 3.8+
* **Permissions:** Root / Superuser (`sudo`) access required for binding raw sockets and promiscuous mode monitoring.

---

