---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--66b9cc87af
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_jabber-guest-services.html
retrieved_at: 2026-08-16T15:15:19.882838+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: Jabber Guest Services

## Chapter: Jabber Guest Services

# Jabber Guest Services

## Jabber Guest - Dual NIC Deployment

## Jabber Guest - Dual NIC Deployment Ports

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

Jabber Guest Client Signaling (HTTP always redirected to HTTPS)

Any (web browser)

1024-65535

TCP

Expressway-E Public IP

80

Jabber Guest Client Secure Signaling (HTTPS)

Any (web browser)

1024-65535

TLS

Expressway-E Public IP

443

To avoid port conflicts, traffic to Expressway-E public:80 must NAT&PAT to private:9980. HTTP is always redirected to HTTPS.

TLS

Expressway-EPrivate IP

(Outward NIC)

9980 # 1

To avoid port conflicts, traffic to Expressway-E public:443 must NAT&PAT to private:9443

TLS

Expressway-EPrivate IP

(Outward NIC)

9443 # 2

Jabber Guest Client Media (TURN)

Any (web browser

1024-65535

UDP

Expressway-E Public IP

3478 (S/M systems)

3478-3483 (L systems) * 3

SIP TCP signaling

Expressway-E private IP

30000-35999

TCP

Jabber Guest Server

5060

SIP TLS signaling

Expressway-E private IP

30000-35999

TLS

Jabber Guest Server

5061

SIP TCP signaling

Jabber Guest Server

Eph

TCP

Expressway-E private IP

5060

SIP TLS signaling

Jabber Guest Server

Eph

TLS

Expressway-E private IP

5061

Multiplexed media traversal

Expressway-C

36000-59999

UDP

Expressway-E Inward NIC

2776-2777 or

36000-36001

## Jabber Guest - Single NIC Deployment

## Jabber Guest - Single NIC Deployment Ports

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

Jabber Guest Client Media (TURN)

Any

1024-65535

UDP

Expressway-E Public IP

3478 (S/M systems)

3478-3483 (L systems) * 4

Jabber Guest Client Signaling (HTTP always redirected to HTTPS)

Any

1024-65535

TCP

Expressway-E Public IP

80

Jabber Guest Client Secure Signaling (HTTPS)

Any

1024-65535

TLS

Expressway-E Public IP

443

To avoid port conflicts, traffic to Expressway-E public:80 must NAT&PAT to private:9980. HTTP is always redirected to HTTPS.

TLS

Expressway-E Private IP

9980 # 5

To avoid port conflicts, traffic to Expressway-Epublic:443 must NAT&PAT to private:9443

TLS

Expressway-E Private IP

9443 # 6

SIP TCP signaling

Jabber Guest Server

Eph

TCP

Expressway-C

5060

SIP TLS signaling

Jabber Guest Server

Eph

TLS

Expressway-C

5061

If you are using single NIC deployments, the communication between core and edge must use NAT reflection, while the destination
                                       IP from core to edge would be the Public.

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| Jabber Guest Client Signaling (HTTP always redirected to HTTPS) | Any (web browser) | 1024-65535 | TCP | Expressway-E Public IP | 80 |
| Jabber Guest Client Secure Signaling (HTTPS) | Any (web browser) | 1024-65535 | TLS | Expressway-E Public IP | 443 |
| To avoid port conflicts, traffic to Expressway-E public:80 must NAT&PAT to private:9980. HTTP is always redirected to HTTPS. | TLS | Expressway-EPrivate IP (Outward NIC) | 9980 # 1 |
| To avoid port conflicts, traffic to Expressway-E public:443 must NAT&PAT to private:9443 | TLS | Expressway-EPrivate IP (Outward NIC) | 9443 # 2 |
| Jabber Guest Client Media (TURN) | Any (web browser | 1024-65535 | UDP | Expressway-E Public IP | 3478 (S/M systems) 3478-3483 (L systems) * 3 |
| SIP TCP signaling | Expressway-E private IP | 30000-35999 | TCP | Jabber Guest Server | 5060 |
| SIP TLS signaling | Expressway-E private IP | 30000-35999 | TLS | Jabber Guest Server | 5061 |
| SIP TCP signaling | Jabber Guest Server | Eph | TCP | Expressway-E private IP | 5060 |
| SIP TLS signaling | Jabber Guest Server | Eph | TLS | Expressway-E private IP | 5061 |
| Multiplexed media traversal | Expressway-C | 36000-59999 | UDP | Expressway-E Inward NIC | 2776-2777 or 36000-36001 |

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| Jabber Guest Client Media (TURN) | Any | 1024-65535 | UDP | Expressway-E Public IP | 3478 (S/M systems) 3478-3483 (L systems) * 4 |
| Jabber Guest Client Signaling (HTTP always redirected to HTTPS) | Any | 1024-65535 | TCP | Expressway-E Public IP | 80 |
| Jabber Guest Client Secure Signaling (HTTPS) | Any | 1024-65535 | TLS | Expressway-E Public IP | 443 |
| To avoid port conflicts, traffic to Expressway-E public:80 must NAT&PAT to private:9980. HTTP is always redirected to HTTPS. | TLS | Expressway-E Private IP | 9980 # 5 |
| To avoid port conflicts, traffic to Expressway-Epublic:443 must NAT&PAT to private:9443 | TLS | Expressway-E Private IP | 9443 # 6 |
| SSH Tunnels from Expressway-C to Expressway-E | Expressway-C | 35000-35999 | TCP | Expressway-E Public IP | 2222 |
| SIP Signaling | Expressway-C | 25000-25999 | TLS | Expressway-E Public IP | 7001 |
| TURN media relays | Expressway-C | 36000-59999 | UDP | Expressway-E Public IP | 24000-29999 |
| TURN media relays ** 7 | Expressway-E Public IP | 24000-29999 | UDP | Expressway-C | 36000-59999 |
| SIP TCP signaling | Expressway-C | 30000-35999 | TCP | Jabber Guest Server | 5060 |
| SIP TLS signaling | Expressway-C | 30000-35999 | TLS | Jabber Guest Server | 5061 |
| SIP TCP signaling | Jabber Guest Server | Eph | TCP | Expressway-C | 5060 |
| SIP TLS signaling | Jabber Guest Server | Eph | TLS | Expressway-C | 5061 |

| Note | If you are using single NIC deployments, the communication between core and edge must use NAT reflection, while the destination
                                       IP from core to edge would be the Public. |
|---|---|