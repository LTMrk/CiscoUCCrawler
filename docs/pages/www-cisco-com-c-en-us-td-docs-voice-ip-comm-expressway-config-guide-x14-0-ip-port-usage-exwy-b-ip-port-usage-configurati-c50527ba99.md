---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-ip-port-usage-exwy-b-ip-port-usage-configurati-c50527ba99
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/ip_port_usage/exwy_b_ip-port-usage-configuration-guide-14/exwy_b_ip-port-usage-configuration-guide_chapter_01010.html
retrieved_at: 2026-08-16T15:31:00.697504+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (X14.0)

# Cisco Expressway IP Port Usage Configuration Guide (X14.0)

Updated: April 14, 2021

Chapter: IMP Federation with Microsoft Clients

## Chapter: IMP Federation with Microsoft Clients

- IMP Federation with Microsoft Clients

- IM and Presence Service Federation with Microsoft Connections

- IM and Presence Federation with Microsoft Clients Port Reference

# IMP Federation with Microsoft Clients

## IM and Presence Service Federation with Microsoft Connections

## IM and Presence Federation with Microsoft Clients Port Reference

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

Expressway-E listens for inbound Microsoft SIP IM&P

Any (Microsoft infrastructure for federated domain)

1024-65535

TLS

Expressway-E public

5061

Expressway-C listens for inbound Microsoft SIP IM&P

Expressway-E private

25000-29999

TLS

Expressway-C

5061

IM and Presence Service listens for inbound Microsoft SIP IM&P

Expressway-C

25000-29999

TLS

IM and Presence Service publisher

5061

Expressway-C listens for outbound Microsoft SIP IM&P

IM and Presence Service publisher

1024-65535

TLS

Expressway-C

5061

Expressway-E listens for outbound Microsoft SIP IM&P

Expressway-C

25000-29999

TLS

Expressway-E private

7001 (for first traversal zone; 7002 for second etc.)

Microsoft infrastructure listens for inbound Microsoft SIP IM&P

Expressway-E

25000-29999

TLS

Any (Microsoft infrastructure for federated domain)

5061

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| Expressway-E listens for inbound Microsoft SIP IM&P | Any (Microsoft infrastructure for federated domain) | 1024-65535 | TLS | Expressway-E public | 5061 |
| Expressway-C listens for inbound Microsoft SIP IM&P | Expressway-E private | 25000-29999 | TLS | Expressway-C | 5061 |
| IM and Presence Service listens for inbound Microsoft SIP IM&P | Expressway-C | 25000-29999 | TLS | IM and Presence Service publisher | 5061 |
| Expressway-C listens for outbound Microsoft SIP IM&P | IM and Presence Service publisher | 1024-65535 | TLS | Expressway-C | 5061 |
| Expressway-E listens for outbound Microsoft SIP IM&P | Expressway-C | 25000-29999 | TLS | Expressway-E private | 7001 (for first traversal zone; 7002 for second etc.) |
| Microsoft infrastructure listens for inbound Microsoft SIP IM&P | Expressway-E | 25000-29999 | TLS | Any (Microsoft infrastructure for federated domain) | 5061 |