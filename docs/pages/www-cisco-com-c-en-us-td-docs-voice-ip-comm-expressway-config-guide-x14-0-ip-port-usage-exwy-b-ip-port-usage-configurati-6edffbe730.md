---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-ip-port-usage-exwy-b-ip-port-usage-configurati-6edffbe730
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/ip_port_usage/exwy_b_ip-port-usage-configuration-guide-14/exwy_b_ip-port-usage-configuration-guide_chapter_0100.html
retrieved_at: 2026-08-16T15:30:35.384718+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (X14.0)

# Cisco Expressway IP Port Usage Configuration Guide (X14.0)

Updated: April 14, 2021

Chapter: Basic Networking Connections

## Chapter: Basic Networking Connections

# Basic Networking Connections

## Basic Networking - Expressway

## Networking Port Reference - Expressway

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

Administrator SSH

Admin PCs

1024-65535

TCP

Expressway-C

22

Administrator HTTP*

Admin PCs

1024-65535

TCP

Expressway-C

80

Administrator HTTPS

Admin PCs

1024-65535

TCP

Expressway-C

443

Name resolution (DNS)

Expressway-C

30000-35999

UDP & TCP†

Internal name server

53

Time synchronization (NTP)

Expressway-C

123

UDP

Internal time server

123

* Expressway redirects HTTP to HTTPS by default. You don't need to open the HTTP port, but you can allow HTTP for convenience
                           and redirect to HTTPS.

† Expressway will attempt DNS resolution over TCP if the response is too large.

## Basic Networking - Traversal Pair

## Networking Port Reference - Expressway Traversal Pair

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

Administrator SSH

Admin PCs

1024-65535

TCP

Expressway-C

22

Administrator HTTP*

Admin PCs

1024-65535

TCP

Expressway-C

80

Administrator HTTPS

Admin PCs

1024-65535

TCP

Expressway-C

443

Name resolution (DNS)

Expressway-C

30000-35999

UDP & TCP †

Internal name server

53

Time synchronization (NTP)

Expressway-C

123

UDP

Internal time server

123

* Expressway redirects HTTP to HTTPS by default. You don't need to open the HTTP port, but you can allow HTTP for convenience
                           and redirect to HTTPS.

† Expressway will attempt DNS resolution over TCP if the response is too large.

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

Administrator SSH

Admin PCs

1024-65535

TCP

Expressway-E private IP

22

Administrator HTTP

Admin PCs

1024-65535

TCP

Expressway-E private IP

80

Administrator HTTPS

Admin PCs

1024-65535

TLS

Expressway-E private IP

443

Internal name resolution (DNS)*

Expressway-E private IP

30000-35999

UDP & TCP

Internal name server

53

External name resolution (DNS)

Expressway-E public IP

30000-35999

UDP & TCP

External name server

53

Internal time synchronization (NTP)*

Expressway-E private IP

123

UDP

Internal time server

123

External time synchronization (NTP)

Expressway-E public IP

123

UDP

External time server

123

* You may prefer to connect Expressway-E to external DNS and NTP. You do not need both.

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Administrator SSH | Admin PCs | 1024-65535 | TCP | Expressway-C | 22 |
| Administrator HTTP* | Admin PCs | 1024-65535 | TCP | Expressway-C | 80 |
| Administrator HTTPS | Admin PCs | 1024-65535 | TCP | Expressway-C | 443 |
| Name resolution (DNS) | Expressway-C | 30000-35999 | UDP & TCP† | Internal name server | 53 |
| Time synchronization (NTP) | Expressway-C | 123 | UDP | Internal time server | 123 |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Administrator SSH | Admin PCs | 1024-65535 | TCP | Expressway-C | 22 |
| Administrator HTTP* | Admin PCs | 1024-65535 | TCP | Expressway-C | 80 |
| Administrator HTTPS | Admin PCs | 1024-65535 | TCP | Expressway-C | 443 |
| Name resolution (DNS) | Expressway-C | 30000-35999 | UDP & TCP † | Internal name server | 53 |
| Time synchronization (NTP) | Expressway-C | 123 | UDP | Internal time server | 123 |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Administrator SSH | Admin PCs | 1024-65535 | TCP | Expressway-E private IP | 22 |
| Administrator HTTP | Admin PCs | 1024-65535 | TCP | Expressway-E private IP | 80 |
| Administrator HTTPS | Admin PCs | 1024-65535 | TLS | Expressway-E private IP | 443 |
| Internal name resolution (DNS)* | Expressway-E private IP | 30000-35999 | UDP & TCP | Internal name server | 53 |
| External name resolution (DNS) | Expressway-E public IP | 30000-35999 | UDP & TCP | External name server | 53 |
| Internal time synchronization (NTP)* | Expressway-E private IP | 123 | UDP | Internal time server | 123 |
| External time synchronization (NTP) | Expressway-E public IP | 123 | UDP | External time server | 123 |