# 📡 VY-NetworkRadar

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg) ![Security](https://img.shields.io/badge/Security-Strict-darkgreen.svg) ![Zero Leak](https://img.shields.io/badge/Zero_Leak-Verified-success.svg) ![Telemetry](https://img.shields.io/badge/Telemetry-None-red.svg) ![License](https://img.shields.io/badge/License-MIT-blue.svg)

 A modern, privacy-first Local Network Discovery (LAN) tool designed for DevSecOps engineers and system administrators. Built entirely in Python, this tool maps connected devices, resolves MAC addresses, and identifies hostnames without relying on external APIs or telemetry servers.


## ⚙️ Security & Privacy Philosophy (Secure by Design)

As a core engineering standard, this project is strictly built on **Privacy-First** principles:

* **Zero Telemetry:** The application does not collect, log, or transmit any user hardware data, IP addresses, network configurations, or scan results to third parties.
* **Offline Operation (No External API Calls):** Unlike standard network scanners, MAC Address to Vendor resolution (OUI lookup) is performed using an embedded offline database. It strictly prohibits sending MAC addresses to third-party lookup APIs.
* **Zero Routing Leak:** Network discovery initializes via local socket simulations rather than DNS querying external servers (e.g., 8.8.8.8), ensuring routing tables do not leak intent to ISPs.

## 🚀 Core Modules (In Development)

* **[1] Intelligent Subnet Detection:** Telemetry-free identification of local IP address and exact CIDR boundaries using kernel-level interface querying. *(Completed)*
* **[2] Asynchronous ARP Reconnaissance:** High-speed, targeted Layer-2 discovery to bypass standard ICMP blocks without creating broadcast storms. *(Coming Soon)*
* **[3] Offline Hostname & Vendor Resolution:** Resolving NetBIOS/Hostnames and matching MAC hardware vendors completely offline. *(Coming Soon)*
