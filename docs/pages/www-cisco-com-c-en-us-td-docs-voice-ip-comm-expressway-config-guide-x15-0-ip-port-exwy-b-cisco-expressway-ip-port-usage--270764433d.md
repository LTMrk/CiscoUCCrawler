---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--270764433d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_xmpp-federation.html
retrieved_at: 2026-08-16T15:15:36.012132+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: XMPP Federation

## Chapter: XMPP Federation

- XMPP Federation

- XMPP Federation Connections

- XMPP Port Reference

# XMPP Federation

## XMPP Federation Connections

## XMPP Port Reference

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

Internal XMPP connections

Expressway-C

Ephemeral

(30000-35999)

TCP

IM and Presence Service

7400

Outbound XMPP traversal

Expressway-C

Ephemeral

(30000-35999)

TCP

Expressway-E

7400

Inbound XMPP connections from federated domain

Any (An XMPP server)

Ephemeral

TCP or TLS

Expressway-E

5269

Outbound XMPP connections to federated domain

Expressway-E

Ephemeral

(30000-35999)

TCP or TLS

Any (An XMPP server)

5269

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| Internal XMPP connections | Expressway-C | Ephemeral (30000-35999) | TCP | IM and Presence Service | 7400 |
| Outbound XMPP traversal | Expressway-C | Ephemeral (30000-35999) | TCP | Expressway-E | 7400 |
| Inbound XMPP connections from federated domain | Any (An XMPP server) | Ephemeral | TCP or TLS | Expressway-E | 5269 |
| Outbound XMPP connections to federated domain | Expressway-E | Ephemeral (30000-35999) | TCP or TLS | Any (An XMPP server) | 5269 |