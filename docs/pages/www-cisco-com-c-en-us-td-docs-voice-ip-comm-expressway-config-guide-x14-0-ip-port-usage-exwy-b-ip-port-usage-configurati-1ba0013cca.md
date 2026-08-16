---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-ip-port-usage-exwy-b-ip-port-usage-configurati-1ba0013cca
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/ip_port_usage/exwy_b_ip-port-usage-configuration-guide-14/exwy_b_ip-port-usage-configuration-guide_chapter_01110.html
retrieved_at: 2026-08-16T15:31:17.258199+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (X14.0)

# Cisco Expressway IP Port Usage Configuration Guide (X14.0)

Updated: April 14, 2021

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