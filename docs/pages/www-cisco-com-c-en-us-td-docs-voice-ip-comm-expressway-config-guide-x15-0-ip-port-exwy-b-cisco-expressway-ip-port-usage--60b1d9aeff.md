---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--60b1d9aeff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_cisco-meeting-server.html
retrieved_at: 2026-08-16T15:15:32.563322+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: Cisco Meeting Server

## Chapter: Cisco Meeting Server

# Cisco Meeting Server

## Web Proxy for Cisco Meeting Server Connections

## Web Proxy for Cisco Meeting Server Port Reference

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

CMA Web client signaling

Guest PCs

1024-65535

TLS

Expressway-E public IP

443 1 1

Tunneled media

CMA Cisco Meeting WebRTC App

1024-65535

UDP

Expressway-E public IP

3478 (and TCP override port if configured)

Web interface access

Administrator PCs

1024-65535

TLS

Expressway-E IP

NOT 443 2 2

SSH tunnels for firewall traversal

Expressway-C

30000-35999

TCP

Expressway-E private IP

2222

SIP signaling

Expressway-C

25000-29999

TCP or TLS

Expressway-E

7001 (for first traversal zone; 7002 for second etc.)

CMA Cisco Meeting WebRTC App TURN requests

Any IP

1024-65535

UDP

Expressway-E TURN server public IP

3478

CMA Cisco Meeting WebRTC App TURN requests (TCP fallback)

Any IP

1024-65535

TCP

Expressway-E TURN server public IP

3478 4 4

Webbridge signaling (HTTPS)

Expressway-C

30000-35999

HTTPS

Meeting Server

443

Webbridge signaling (HTTPS)

Meeting Server

>=1024

HTTPS

Expressway-C

30000-35999

TURN client requests

Meeting Server

1024-65535

UDP

Expressway-E TURN server private IP

3478

Original Source: Expressway-E Private IP Translated Source: Expressway-E Public IP

24000- 29999

UDP and TCP

Original Destination: Expressway-E Public IP Translated Destination: Expressway-E Private IP

24000-29999

TURN relay (On premises)

Expressway-E Private IP

24000- 29999

UDP and TCP

Expressway-E Private IP

24000-29999

TURN relays 6 6

Meeting Server

Ephemeral

UDP

Expressway-E public IP

24000-29999

Important

From X12.5.5, support for static NAT functionality on TURN is extended to clustered systems. However, peers which are configured
                                             as TURN servers must be reachable using the private addresses for their corresponding public interfaces.

## SIP Edge for Meeting Server Connections (Standards-based Endpoints)

## SIP Edge for Cisco Meeting Server Port Reference (Standards-based Endpoints)

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

SIP signaling

Expressway-C

25000-29999

TCP or TLS

Expressway-E

7001 (for first traversal zone; 7002 for second etc.)

SIP signaling

Expressway-C

5060

UDP

Meeting Server

5060

SIP signaling

Expressway-C

25000-29999

TLS

Meeting Server

5061

SIP signaling

SIP endpoint (or its firewall)

>=1024

TCP

Expressway-E

5060

SIP signaling

SIP endpoint (or its firewall)

>=1024

TLS

Expressway-E

5061

Assent RTP

(traversed media)

Expressway-C

36000-59999

UDP

Expressway-E

2776 or 36000 (Small/Medium)

36000 - 36010 (even ports) (Large)

Assent RTCP

(traversed media

Expressway-C

36000-59999

UDP

Expressway-E

2777 or 36001 (Small/Medium)

36001 - 36011 (odd ports) (Large)

Assent RTP

(traversed media)

SIP endpoint (or its firewall)

>=1024

Could be the firewall port where the media egressed, rather than an endpoint port

UDP

Expressway-E

36000-59999

Assent RTCP

(traversed media)

SIP endpoint (or its firewall)

>=1024

Could be the firewall port where the media egressed, rather than an endpoint port

UDP

Expressway-E

36000-59999

Assent RTP

(traversed media)

Expressway-E

36000-59999

UDP

SIP endpoint (or its firewall)

>=1024

Expressway waits until it receives media, then sends media to that source port (which could be the port where the media egressed
                                       the firewall, not an endpoint port)

TURN request

Any IP address

>=1024 (signaling port from endpoint or the firewall)

UDP & TCP

Expressway-E public IP

3478 (Small/Medium)

3478-3483 (Large)

TURN request

Meeting Server

>=1024

UDP

Expressway-E private IP

3478 (Small/Medium)

3478-3483 (Large)

TURN media

Expressway-E

24000-29999

UDP & TCP

Any IP address

>=1024

TURN media

Any

>=1024

Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port

UDP & TCP

Expressway-E

24000-29999

TURN media

Meeting Server

50000-51000

UDP

Expressway-E private IP

24000-29999

## SIP Edge for Meeting Server Connections (Microsoft Clients)

## SIP Edge for Cisco Meeting Server Port Reference (Microsoft Clients)

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

SIP signaling

Expressway-C

25000-29999

TCP or TLS

Expressway-E

7001 (for first traversal zone; 7002 for second etc.)

SIP signaling

Expressway-C

25000-29999

TLS

Meeting Server

5061

SIP signaling

SIP endpoint (or its firewall)

>=1024

TCP

Expressway-E

5060

SIP signaling

SIP endpoint (or its firewall)

>=1024

TLS

Expressway-E

5061

Assent RTP

(traversed media)

Expressway-C

36000-59999

UDP

Expressway-E

2776 or 36000 (Small/Medium)

36000 - 36010 (even ports) (Large)

Assent RTCP

(traversed media)

Expressway-C

36000-59999

UDP

Expressway-E

2777 or 36001 (Small/Medium)

36001 - 36011 (odd ports) (Large)

Assent RTP

(traversed media)

SIP endpoint (or its firewall)

>=1024

Could be the firewall port where the media egressed, rather than an endpoint port

UDP

Expressway-E

36000-59999

Assent RTCP

(traversed media)

SIP endpoint (or its firewall)

>=1024

Could be the firewall port where the media egressed, rather than an endpoint port

UDP

Expressway-E

36000-59999

Assent RTP

(traversed media)

Expressway-E

36000-59999

UDP

SIP endpoint (or its firewall)

>=1024

Expressway waits until it receives media, then sends media to that source port (which could be the port where the media egressed
                                       the firewall, not an endpoint port)

TURN control

Any IP address

>=1024 (signaling port from endpoint or the firewall)

UDP & TCP

Expressway-E

3478 (Small/Medium)

3478-3483 (Large)

TURN media

Expressway-E

24000-29999

UDP & TCP

Any IP address

>=1024

TURN media

Any

>=1024

Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port

UDP & TCP

Expressway-E

24000-29999

## Connection Map-Point to Point Microsoft Interoperability Using Meeting Server

## Port Reference-Point to Point Microsoft Interoperability Using Meeting Server

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

SIP Signaling

Expressway-C

25000-29999

TCP or TLS

Expressway-E

7001 (for first traversal zone; 7002 for second etc.)

SIP Signaling

Expressway-C

25000-29999

TLS

Meeting Server

5061

SIP Signaling

Expressway-C

25000-29999

TCP

Meeting Server

5060

SIP Signaling

Microsoft client or its firewall

>=1024

TLS

Expressway-E

5061

SIP Signaling

Expressway-C

25000-29999

TLS

Unified CM

5061

SIP Signaling

Expressway-C

25000-29999

TCP

Unified CM

5060

SIP Signaling

Unified CM

Ephemeral

TLS

Expressway-C

5061

SIP Signaling

Unified CM

Ephemeral

TCP

Expressway-C

5060

TURN control

Any IP address

>=1024 (signaling port from endpoint or the firewall)

UDP & TCP

Expressway- E

3478 (Small/Medium)

TURN request

Meeting Server

>=1024

UDP/TCP

Expressway-E private IP

3478 (Small/Medium) 3478-3483 (Large)

TURN media

Expressway- E

24000-29999

UDP & TCP

Any IP address

>=1024

TURN media

Any

>=1024 Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port

UDP & TCP

Expressway- E

24000-29999

TURN media

Meeting Server

50000-51000

UDP

Expressway-E private IP

24000-29999

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| CMA Web client signaling | Guest PCs | 1024-65535 | TLS | Expressway-E public IP | 443 1 1 |
| Tunneled media | CMA Cisco Meeting WebRTC App | 1024-65535 | UDP | Expressway-E public IP | 3478 (and TCP override port if configured) |
| Web interface access | Administrator PCs | 1024-65535 | TLS | Expressway-E IP | NOT 443 2 2 8443 3 3 |
| SSH tunnels for firewall traversal | Expressway-C | 30000-35999 | TCP | Expressway-E private IP | 2222 |
| SIP signaling | Expressway-C | 25000-29999 | TCP or TLS | Expressway-E | 7001 (for first traversal zone; 7002 for second etc.) |
| CMA Cisco Meeting WebRTC App TURN requests | Any IP | 1024-65535 | UDP | Expressway-E TURN server public IP | 3478 |
| CMA Cisco Meeting WebRTC App TURN requests (TCP fallback) | Any IP | 1024-65535 | TCP | Expressway-E TURN server public IP | 3478 4 4 |
| Webbridge signaling (HTTPS) | Expressway-C | 30000-35999 | HTTPS | Meeting Server | 443 |
| Webbridge signaling (HTTPS) | Meeting Server | >=1024 | HTTPS | Expressway-C | 30000-35999 |
| TURN client requests | Meeting Server | 1024-65535 | UDP | Expressway-E TURN server private IP | 3478 |
| TURN relays 5 5 | Original Source: Expressway-E Private IP Translated Source: Expressway-E Public IP | 24000- 29999 | UDP and TCP | Original Destination: Expressway-E Public IP Translated Destination: Expressway-E Private IP | 24000-29999 |
| TURN relay (On premises) | Expressway-E Private IP | 24000- 29999 | UDP and TCP | Expressway-E Private IP | 24000-29999 |
| TURN relays 6 6 | Meeting Server | Ephemeral | UDP | Expressway-E public IP | 24000-29999 |

| Important | From X12.5.5, support for static NAT functionality on TURN is extended to clustered systems. However, peers which are configured
                                             as TURN servers must be reachable using the private addresses for their corresponding public interfaces. |
|---|---|

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| SIP signaling | Expressway-C | 25000-29999 | TCP or TLS | Expressway-E | 7001 (for first traversal zone; 7002 for second etc.) |
| SIP signaling | Expressway-C | 5060 | UDP | Meeting Server | 5060 |
| SIP signaling | Expressway-C | 25000-29999 | TLS | Meeting Server | 5061 |
| SIP signaling | SIP endpoint (or its firewall) | >=1024 | TCP | Expressway-E | 5060 |
| SIP signaling | SIP endpoint (or its firewall) | >=1024 | TLS | Expressway-E | 5061 |
| Assent RTP (traversed media) | Expressway-C | 36000-59999 | UDP | Expressway-E | 2776 or 36000 (Small/Medium) 36000 - 36010 (even ports) (Large) |
| Assent RTCP (traversed media | Expressway-C | 36000-59999 | UDP | Expressway-E | 2777 or 36001 (Small/Medium) 36001 - 36011 (odd ports) (Large) |
| Assent RTP (traversed media) | SIP endpoint (or its firewall) | >=1024 Could be the firewall port where the media egressed, rather than an endpoint port | UDP | Expressway-E | 36000-59999 |
| Assent RTCP (traversed media) | SIP endpoint (or its firewall) | >=1024 Could be the firewall port where the media egressed, rather than an endpoint port | UDP | Expressway-E | 36000-59999 |
| Assent RTP (traversed media) | Expressway-E | 36000-59999 | UDP | SIP endpoint (or its firewall) | >=1024 Expressway waits until it receives media, then sends media to that source port (which could be the port where the media egressed
                                       the firewall, not an endpoint port) |
| TURN request | Any IP address | >=1024 (signaling port from endpoint or the firewall) | UDP & TCP | Expressway-E public IP | 3478 (Small/Medium) 3478-3483 (Large) |
| TURN request | Meeting Server | >=1024 | UDP | Expressway-E private IP | 3478 (Small/Medium) 3478-3483 (Large) |
| TURN media | Expressway-E | 24000-29999 | UDP & TCP | Any IP address | >=1024 |
| TURN media | Any | >=1024 Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port | UDP & TCP | Expressway-E | 24000-29999 |
| TURN media | Meeting Server | 50000-51000 | UDP | Expressway-E private IP | 24000-29999 |

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| SIP signaling | Expressway-C | 25000-29999 | TCP or TLS | Expressway-E | 7001 (for first traversal zone; 7002 for second etc.) |
| SIP signaling | Expressway-C | 25000-29999 | TLS | Meeting Server | 5061 |
| SIP signaling | SIP endpoint (or its firewall) | >=1024 | TCP | Expressway-E | 5060 |
| SIP signaling | SIP endpoint (or its firewall) | >=1024 | TLS | Expressway-E | 5061 |
| Assent RTP (traversed media) | Expressway-C | 36000-59999 | UDP | Expressway-E | 2776 or 36000 (Small/Medium) 36000 - 36010 (even ports) (Large) |
| Assent RTCP (traversed media) | Expressway-C | 36000-59999 | UDP | Expressway-E | 2777 or 36001 (Small/Medium) 36001 - 36011 (odd ports) (Large) |
| Assent RTP (traversed media) | SIP endpoint (or its firewall) | >=1024 Could be the firewall port where the media egressed, rather than an endpoint port | UDP | Expressway-E | 36000-59999 |
| Assent RTCP (traversed media) | SIP endpoint (or its firewall) | >=1024 Could be the firewall port where the media egressed, rather than an endpoint port | UDP | Expressway-E | 36000-59999 |
| Assent RTP (traversed media) | Expressway-E | 36000-59999 | UDP | SIP endpoint (or its firewall) | >=1024 Expressway waits until it receives media, then sends media to that source port (which could be the port where the media egressed
                                       the firewall, not an endpoint port) |
| TURN control | Any IP address | >=1024 (signaling port from endpoint or the firewall) | UDP & TCP | Expressway-E | 3478 (Small/Medium) 3478-3483 (Large) |
| TURN media | Expressway-E | 24000-29999 | UDP & TCP | Any IP address | >=1024 |
| TURN media | Any | >=1024 Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port | UDP & TCP | Expressway-E | 24000-29999 |

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| SIP Signaling | Expressway-C | 25000-29999 | TCP or TLS | Expressway-E | 7001 (for first traversal zone; 7002 for second etc.) |
| SIP Signaling | Expressway-C | 25000-29999 | TLS | Meeting Server | 5061 |
| SIP Signaling | Expressway-C | 25000-29999 | TCP | Meeting Server | 5060 |
| SIP Signaling | Microsoft client or its firewall | >=1024 | TLS | Expressway-E | 5061 |
| SIP Signaling | Expressway-C | 25000-29999 | TLS | Unified CM | 5061 |
| SIP Signaling | Expressway-C | 25000-29999 | TCP | Unified CM | 5060 |
| SIP Signaling | Unified CM | Ephemeral | TLS | Expressway-C | 5061 |
| SIP Signaling | Unified CM | Ephemeral | TCP | Expressway-C | 5060 |
| TURN control | Any IP address | >=1024 (signaling port from endpoint or the firewall) | UDP & TCP | Expressway- E | 3478 (Small/Medium) |
| TURN request | Meeting Server | >=1024 | UDP/TCP | Expressway-E private IP | 3478 (Small/Medium) 3478-3483 (Large) |
| TURN media | Expressway- E | 24000-29999 | UDP & TCP | Any IP address | >=1024 |
| TURN media | Any | >=1024 Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port | UDP & TCP | Expressway- E | 24000-29999 |
| TURN media | Meeting Server | 50000-51000 | UDP | Expressway-E private IP | 24000-29999 |