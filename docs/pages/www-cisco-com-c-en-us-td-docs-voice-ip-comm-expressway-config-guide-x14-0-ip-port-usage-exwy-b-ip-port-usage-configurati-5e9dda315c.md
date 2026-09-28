---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-ip-port-usage-exwy-b-ip-port-usage-configurati-5e9dda315c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/ip_port_usage/exwy_b_ip-port-usage-configuration-guide-14/exwy_b_ip-port-usage-configuration-guide_chapter_01100.html
retrieved_at: 2026-08-16T15:31:09.045339+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (X14.0)

# Cisco Expressway IP Port Usage Configuration Guide (X14.0)

Updated: April 14, 2021

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