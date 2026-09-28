---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--40d49802d4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_acme-certificate-management.html
retrieved_at: 2026-08-16T15:15:44.416004+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: ACME Certificate Management

## Chapter: ACME Certificate Management

- ACME Certificate Management

- ACME Certificate Management Connections

- Expressway-E ACME Port Reference

# ACME Certificate Management

## ACME Certificate Management Connections

## Expressway-E ACME Port Reference

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

Write challenge files

Any (ACME provider IP addresses not predictable)

1024-65535

TCP

Expressway-E public NIC

80

Request certificate signing

Expressway-E public NIC

Ephemeral

TLS

Any (ACME provider domain)

443

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| Write challenge files | Any (ACME provider IP addresses not predictable) | 1024-65535 | TCP | Expressway-E public NIC | 80 |
| Request certificate signing | Expressway-E public NIC | Ephemeral | TLS | Any (ACME provider domain) | 443 |