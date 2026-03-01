# PyShark DNS Extractor 🔍🐍

A Python script to extract **DNS queries** from `.pcap` or `.pcapng` files using **PyShark**.  
It captures unique DNS queries, shows the source IP, queried domain, and detects the DNS server IP.  

---

## Features

- Reads `.pcap` / `.pcapng` capture files.
- Filters **DNS queries only**.
- Handles **IPv4 and IPv6**.
- Removes duplicate queries for cleaner output.
- Detects **DNS server IP**.

---

## Requirements

- Python 3
- [PyShark](https://github.com/KimiNewt/pyshark)
- Wireshark / TShark installed on your system.

> **Tip:** Use a virtual environment to install PyShark:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pyshark
```
---

## Usage 

```
python3 dnsExtract.py <file.pcap or file.pcapng>
```
---

## Sample Output

```
PyShark DNS Query Extractor
========================================
DNS IP Address: 192.168.50.2

Source IP            Domain Name
--------------------------------------------------
192.168.50.128       google.com
192.168.50.128       ads.mozilla.org
192.168.50.128       forums.kali.org
192.168.50.128       example.org
```
---

## How It Works
- The script opens a capture file using PyShark.
- It applies a filter to capture only DNS query packets (`dns.flags.response == 0`).
- For each packet, it extracts:
  - Source IP (your computer)
  - Queried domain name
- It removes duplicate queries to avoid repeated entries.
- It detects the DNS server IP and prints it above the table.
---

## DNS Concepts
- DNS Query: Request from a client asking “what is the IP of this domain?”
- DNS Response: Reply from DNS server containing the IP address.
