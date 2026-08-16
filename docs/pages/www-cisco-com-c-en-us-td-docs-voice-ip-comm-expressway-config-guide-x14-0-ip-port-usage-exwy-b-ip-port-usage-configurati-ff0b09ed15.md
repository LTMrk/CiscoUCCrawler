---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-ip-port-usage-exwy-b-ip-port-usage-configurati-ff0b09ed15
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/ip_port_usage/exwy_b_ip-port-usage-configuration-guide-14/exwy_b_ip-port-usage-configuration-guide_chapter_01101.html
retrieved_at: 2026-08-16T15:31:13.176097+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (X14.0)

# Cisco Expressway IP Port Usage Configuration Guide (X14.0)

Updated: April 14, 2021

Chapter: Serviceability

## Chapter: Serviceability

# Serviceability

## Serviceability - Expressway-C

## Serviceability - Traversal Pair

## Serviceability Ports - Traversal Pair

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

Network management (SNMP)

SNMP Manager

1024-65535

UDP

Expressway-C

161

System metrics

Expressway

25826

UDP

Analytics server(s)

25826

Remote logging (syslog)

Expressway

30000-35999

UDP

Syslog server(s)

514

Remote logging (syslog)

Expressway

30000-35999

TCP

Syslog server(s)

514

Remote logging (syslog)

Expressway

30000-35999

TLS

Syslog server(s)

6514

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| Network management (SNMP) | SNMP Manager | 1024-65535 | UDP | Expressway-C | 161 |
| System metrics | Expressway | 25826 | UDP | Analytics server(s) | 25826 |
| Remote logging (syslog) | Expressway | 30000-35999 | UDP | Syslog server(s) | 514 |
| Remote logging (syslog) | Expressway | 30000-35999 | TCP | Syslog server(s) | 514 |
| Remote logging (syslog) | Expressway | 30000-35999 | TLS | Syslog server(s) | 6514 |