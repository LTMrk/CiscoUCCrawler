---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--efcf8a7a43
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_basic-networking-connections.html
retrieved_at: 2026-08-16T15:15:02.953739+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

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

22 or 5022 1

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

UDP & TCP

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

Expressway will attempt DNS resolution over TCP if the response is too large.

1 Port 22 is configured as the Administrator SSH port on Expressway Appliances. The Expressway Virtual Machine can be deployed
                                       on port 22 or 5022 when the VM is deployed.

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

22 or 5022 1

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

UDP & TCP

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

Expressway will attempt DNS resolution over TCP if the response is too large.

1 Port 22 is configured as the Administrator SSH port on Expressway Appliances. The Expressway Virtual Machine can be deployed
                                       on port 22 or 5022 when the VM is deployed.

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

22 or 5022 1

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

1 Port 22 is configured as the Administrator SSH port on Expressway Appliances. The Expressway Virtual Machine can be deployed
                                       on port 22 or 5022 when the VM is deployed.

## Networking Port Reference - Smart Licensing

Expressway requires a connection to the Smart License server, and the port requirements vary based on the smart license transport
                                          setting. The details are listed in the table.

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

Smart Licensing requests originating from Expressway-E

Expressway-E

Ephemeral (30000- 35999)

TLS

https://smartreceiver.

cisco.com/

licservice/license

443

Smart License Direct

Expressway

1024-65535

TLS

smartreceiver.

cisco.com

443

Smart License on-prem CSSM

Expressway

1024-65535

TLS

User configured On-prem CSSM IP/FQDN

443

Smart License Proxy

Expressway

1024-65535

TLS

User configured proxy server IP/FQDN

user configured proxy server port

## Networking Port Reference - Email Notification Service

You can configure Simple Mail Transfer Protocol (SMTP) server for implicit or explicit connections. This is the difference
                              between the two connection types:

Explicit mode — The client connects to the SMTP server first. Later the server explicitly requests switching on TLS/SSL encryption . The default ports are 25 and 587.

Implicit mode — The client connects to the SMTP server. Soon after establishing the channel, the server switches on TLS/SSL encryption implicitly . The default TCP port is 465.

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Administrator SSH | Admin PCs | 1024-65535 | TCP | Expressway-C | 22 or 5022 1 |
| Administrator HTTP* | Admin PCs | 1024-65535 | TCP | Expressway-C | 80 |
| Administrator HTTPS | Admin PCs | 1024-65535 | TCP | Expressway-C | 443 |
| Name resolution (DNS) | Expressway-C | 30000-35999 | UDP & TCP | Internal name server | 53 |
| Time synchronization (NTP) | Expressway-C | 123 | UDP | Internal time server | 123 |

| Note | 1 Port 22 is configured as the Administrator SSH port on Expressway Appliances. The Expressway Virtual Machine can be deployed
                                       on port 22 or 5022 when the VM is deployed. |
|---|---|

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Administrator SSH | Admin PCs | 1024-65535 | TCP |  | 22 or 5022 1 |
| Administrator HTTP* | Admin PCs | 1024-65535 | TCP | Expressway-C | 80 |
| Administrator HTTPS | Admin PCs | 1024-65535 | TCP | Expressway-C | 443 |
| Name resolution (DNS) | Expressway-C | 30000-35999 | UDP & TCP | Internal name server | 53 |
| Time synchronization (NTP) | Expressway-C | 123 | UDP | Internal time server | 123 |

| Note | 1 Port 22 is configured as the Administrator SSH port on Expressway Appliances. The Expressway Virtual Machine can be deployed
                                       on port 22 or 5022 when the VM is deployed. |
|---|---|

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Administrator SSH | Admin PCs | 1024-65535 | TCP | Expressway-E private IP | 22 or 5022 1 |
| Administrator HTTP | Admin PCs | 1024-65535 | TCP | Expressway-E private IP | 80 |
| Administrator HTTPS | Admin PCs | 1024-65535 | TLS | Expressway-E private IP | 443 |
| Internal name resolution (DNS)* | Expressway-E private IP | 30000-35999 | UDP & TCP | Internal name server | 53 |
| External name resolution (DNS) | Expressway-E public IP | 30000-35999 | UDP & TCP | External name server | 53 |
| Internal time synchronization (NTP)* | Expressway-E private IP | 123 | UDP | Internal time server | 123 |
| External time synchronization (NTP) | Expressway-E public IP | 123 | UDP | External time server | 123 |

| Note | 1 Port 22 is configured as the Administrator SSH port on Expressway Appliances. The Expressway Virtual Machine can be deployed
                                       on port 22 or 5022 when the VM is deployed. |
|---|---|

| Note | Expressway requires a connection to the Smart License server, and the port requirements vary based on the smart license transport
                                          setting. The details are listed in the table. |
|---|---|

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Smart Licensing requests originating from Expressway-E | Expressway-E | Ephemeral (30000- 35999) | TLS | https://smartreceiver. cisco.com/ licservice/license | 443 |
| Smart License Direct | Expressway | 1024-65535 | TLS | smartreceiver. cisco.com | 443 |
| Smart License on-prem CSSM | Expressway | 1024-65535 | TLS | User configured On-prem CSSM IP/FQDN | 443 |
| Smart License Proxy | Expressway | 1024-65535 | TLS | User configured proxy server IP/FQDN | user configured proxy server port |