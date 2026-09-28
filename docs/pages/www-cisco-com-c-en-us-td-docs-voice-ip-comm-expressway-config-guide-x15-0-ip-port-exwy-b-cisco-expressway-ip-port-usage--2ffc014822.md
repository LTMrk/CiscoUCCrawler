---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--2ffc014822
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_serviceability.html
retrieved_at: 2026-08-16T15:15:40.312805+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

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