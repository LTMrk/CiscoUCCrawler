---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-ip-port-usage-exwy-b-ip-port-usage-configurati-5e4b27e2c8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/ip_port_usage/exwy_b_ip-port-usage-configuration-guide-14/exwy_b_ip-port-usage-configuration-guide_chapter_0110.html
retrieved_at: 2026-08-16T15:30:44.079373+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (X14.0)

# Cisco Expressway IP Port Usage Configuration Guide (X14.0)

Updated: April 14, 2021

Chapter: Provisioning Registrations Authentication and Calls

## Chapter: Provisioning Registrations Authentication and Calls

# Provisioning Registrations Authentication and Calls

## SIP Calls

## SIP Calls Port Reference

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

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

SIP endpoint

5060 (often, but could be different, >=1024)

Port number defined by registration (if registered) or by DNS lookup

SIP signaling

Expressway-C

25000-29999

TCP or TLS

SIP endpoint

>=1024

Port number defined by registration (if registered) or by DNS lookup

SIP signaling

Expressway-E

25000-29999

TCP or TLS

SIP endpoint (or its firewall)

>=1024

Port number defined by registration (if registered) or by DNS lookup

SIP signaling

SIP endpoint (or its firewall)

>=1024

UDP

Expressway-E

5060

SIP UDP disabled by default. Not recommended for internet facing connections.

SIP signaling

SIP endpoint (or its firewall)

>=1024

TCP

Expressway-E

5060

SIP TCP disabled by default (X8.9.2 and later).

SIP signaling

SIP endpoint (or its firewall)

>=1024

TLS

Expressway-E

5061

SIP signaling

SIP endpoint (or its firewall)

>=1024

MTLS

Expressway-E

5062

Assent RTP (traversed media)

Expressway-C

36000-59999

UDP

Expressway-E

2776 or 36000 (Small/Medium)

36000 - 36010 (even ports) (Large)

Assent RTCP (traversed media)

Expressway-C

36000-59999

UDP

Expressway-E

2777 or 36001 (Small/Medium)

36001 - 36011 (odd ports) (Large)

Assent RTP (traversed media)

SIP endpoint (or its firewall)

>=1024

Could be the firewall port where the media egressed, rather than an endpoint port

UDP

Expressway-E

36000-59999

Assent RTCP (traversed media)

SIP endpoint (or its firewall)

>=1024

Could be translated by the firewall to port where the media egressed, rather than an endpoint port

UDP

Expressway-E

36000-59999

Assent RTP (traversed media)

Expressway-E

36000-59999

UDP

SIP endpoint (or its firewall)

>=1024

Expressway waits until it receives media, then sends media to that source port (which could be the port where the media egressed
                                       the firewall, not an endpoint port)

TURN control

Any IP address†

>=1024 (signaling port from endpoint or the firewall)

UDP & TCP

Expressway-E

3478 (Small/Medium)

3478-3483 (Large)

TURN control

Expressway-C

>=1024

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

Any IP address‡

>=1024

Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port

UDP & TCP

Expressway-E

24000-29999

† The request could be from any IP address, unknown to the TURN server. Assume for example, that endpoint A and endpoint C
                           (TURN clients) can use the Expressway-E TURN server. The actual IP address from which the TURN server receives the request
                           could be the endpoint's firewall egress address (NATed).

‡ The media could go to any of the candidate addresses. For example, before ICE negotiation the TURN server does not know
                           which of endpoint B's candidate addresses will be the highest priority.

## H.323 Calls

## H.323 Calls Port Reference

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

Initial RAS connection

Registered endpoint in the Internet

1719

UDP

Expressway-E (public)

1719

Initial RAS connection

Expressway-E (public)

1719

UDP

Registered endpoint in the Internet

1719

Initial RAS connection

External address of firewall protecting off-premises endpoint

>=1024

UDP

Expressway-E (public)

1719

Initial RAS connection

Expressway-C

1719

UDP

Expressway-E (private)

6001 (for first traversal zone, 6002 for second etc.)

Q.931 / H.225 signaling

Any (endpoint in the Internet)

1720

TCP

Expressway-E (public)

1720

Q.931 / H.225 signaling

External address of firewall protecting off-premises Assent endpoint

>=1024

TCP

Expressway-E (public)

2776

Q.931 / H.225 signaling

External address of firewall protecting off-premises H.460.18/19 endpoint

>=1024

TCP

Expressway-E (public)

1720

Q.931 / H.225 signaling

Expressway-E (public)

15000-19999

TCP

Any (endpoint in the Internet)

1720 (endpoint signaling port, specified during registration. Could be another port >=1024)

Q.931 / H.225 signaling

Expressway-C

15000-19999

TCP

Expressway-E (private)

2776 (Assent calls)

Q.931 / H.225 signaling

Expressway-C

15000-19999

TCP

Expressway-E (private)

1720 (H.460.18 calls)

H.245

Expressway-C

15000-19999

TCP

Expressway-E (private)

2776 (Assent calls)

H.245

Expressway-C

15000-19999

TCP

Expressway-E (private)

2777 (H.460.18 calls)

H.245

Any (endpoint in the Internet)

>=1024

TCP

Expressway-E (public)

15000-19999

H.245

Expressway-E (public)

15000-19999

TCP

Any (endpoint in the Internet)

>=1024 (endpoint H.245 signaling port)

H.245

External address of firewall protecting off-premises Assent endpoint

>=1024

TCP

Expressway-E (public)

2776

H.245

External address of firewall protecting off-premises H.460.18/19 endpoint

>=1024

TCP

Expressway-E (public)

2777

RTP (multiplexed traversal media)

Expressway-C

36000-59998 (even ports)

UDP

Expressway-E (private)

2776 (Small/Medium)

or 36000-36010 (even ports) (Large)

RTCP (multiplexed traversal media)

Expressway-C

36001-59999 (odd ports)

UDP

Expressway-E (private)

2777 (Small/Medium)

or 36001-36011 (odd ports) (Large)

RTP (non-multiplexed traversal media)

Expressway-C

36000-59998 (even ports)

UDP

Expressway-E (private)

36000-59998 (even ports)

RTCP (non-multiplexed traversal media)

Expressway-C

36001-59999 (odd ports)

UDP

Expressway-E (private)

36001-59999 (odd ports)

RTP (non-multiplexed)

Expressway-E (public)

36000-59998 (even ports)

UDP

Any (endpoint in the Internet)

>=1024 (endpoint media range)

RTCP (non-multiplexed)

Expressway-E (public)

36001-59999 (odd ports)

UDP

Any (endpoint in the Internet)

>=1024 (endpoint media range)

RTP (non-multiplexed)

Any (endpoint in the Internet)

>=1024 (endpoint media range)

UDP

Expressway-E (public)

36000-59998 (even ports)

RTCP (non-multiplexed)

Any (endpoint in the Internet)

>=1024 (endpoint media range)

UDP

Expressway-E (public)

36001-59999 (odd ports)

RTP (multiplexed traversal media)

External address of firewall protecting off-premises H.460 endpoint (multiplexed media)

>=1024

UDP

Expressway-E (public)

2776 (Small/Medium)

or 36000-36010 (even ports) (Large)

RTCP (multiplexed traversal media)

External address of firewall protecting off-premises H.460 endpoint (multiplexed media)

>=1024

UDP

Expressway-E (public)

2777 (Small/Medium)

or 36001-36011 (odd ports) (Large)

RTP (multiplexed traversal media)

External address of firewall protecting off-premises H.460 endpoint (non-multiplexed media)

>=1024

UDP

Expressway-E (public)

36000-59998 (even ports)

RTCP (multiplexed traversal media)

External address of firewall protecting off-premises H.460 endpoint (non-multiplexed media)

>=1024

UDP

Expressway-E (public)

36001-59999 (odd ports)

## TMS Connections

## TMS Port Reference

Cisco TMS can have two IP addresses; for managing public systems, or managing systems on the LAN. On Cisco TMS, go to Administrative Tools > Configuration > Network Settings > Advanced Network Settings . You should use the TMS public address with the Expressway-E, and the default LAN address with the Expressway-C.

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

SNMP for discovery of Expressway-E

Cisco TMS External IP

1024-65535

UDP

Expressway-E private

161

SNMP for discovery of Expressway-C

Cisco TMS

1024-65535

UDP

Expressway-C

161

HTTP Management of Expressway-E

Cisco TMS External IP

1024-65535

TCP

Expressway-E private IP

80

HTTP Management of Expressway-C

Cisco TMS

1024-65535

TCP

Expressway-E private IP

80

HTTPS Management of Expressway-E

Cisco TMS External IP

1024-65535

TCP

Expressway-E private

443

HTTPS Management of Expressway-C

Cisco TMS

1024-65535

TCP

Expressway-C

443

Feedback events (HTTP)

Expressway-E private

1024-65535

TCP

Cisco TMS External IP

80

Feedback events (HTTP)

Expressway-C

1024-65535

TCP

Cisco TMS

80

Feedback events (HTTPS)

Expressway-E private

1024-65535

TCP

Cisco TMS External IP

443

Feedback events (HTTPS)

Expressway-C

1024-65535

TCP

Cisco TMS

443

## LDAP Connections

## LDAP Port Reference

You can choose to use an LDAP server to authenticate and authorize administrator or user logins. You would only need to allow
                           the LDAP ports inbound from the Expressway-E in the rare case where you want a user to log in from outside the network and
                           you also do not allow credentials to be stored on the Expressway.

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

Authentication requests from the Expressway-C

Expressway-C

1024-65535

TCP

Directory Server

389

Authentication requests from the Expressway-E

Expressway-E private

1024-65535

TCP

Directory Server

389

Encrypted authentication requests from the Expressway-C

Expressway-C

1024-65535

TLS

Directory Server

636

Encrypted authentication requests from the Expressway-E

Expressway-E private

1024-65535

TLS

Directory Server

636

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| SIP signaling | Expressway-C | 25000-29999 | TCP or TLS | Expressway-E | 7001 (for first traversal zone; 7002 for second etc.) |
| SIP signaling | Expressway-C | 5060 | UDP | SIP endpoint | 5060 (often, but could be different, >=1024) Port number defined by registration (if registered) or by DNS lookup |
| SIP signaling | Expressway-C | 25000-29999 | TCP or TLS | SIP endpoint | >=1024 Port number defined by registration (if registered) or by DNS lookup |
| SIP signaling | Expressway-E | 25000-29999 | TCP or TLS | SIP endpoint (or its firewall) | >=1024 Port number defined by registration (if registered) or by DNS lookup |
| SIP signaling | SIP endpoint (or its firewall) | >=1024 | UDP | Expressway-E | 5060 SIP UDP disabled by default. Not recommended for internet facing connections. |
| SIP signaling | SIP endpoint (or its firewall) | >=1024 | TCP | Expressway-E | 5060 SIP TCP disabled by default (X8.9.2 and later). |
| SIP signaling | SIP endpoint (or its firewall) | >=1024 | TLS | Expressway-E | 5061 |
| SIP signaling | SIP endpoint (or its firewall) | >=1024 | MTLS | Expressway-E | 5062 |
| Assent RTP (traversed media) | Expressway-C | 36000-59999 | UDP | Expressway-E | 2776 or 36000 (Small/Medium) 36000 - 36010 (even ports) (Large) |
| Assent RTCP (traversed media) | Expressway-C | 36000-59999 | UDP | Expressway-E | 2777 or 36001 (Small/Medium) 36001 - 36011 (odd ports) (Large) |
| Assent RTP (traversed media) | SIP endpoint (or its firewall) | >=1024 Could be the firewall port where the media egressed, rather than an endpoint port | UDP | Expressway-E | 36000-59999 |
| Assent RTCP (traversed media) | SIP endpoint (or its firewall) | >=1024 Could be translated by the firewall to port where the media egressed, rather than an endpoint port | UDP | Expressway-E | 36000-59999 |
| Assent RTP (traversed media) | Expressway-E | 36000-59999 | UDP | SIP endpoint (or its firewall) | >=1024 Expressway waits until it receives media, then sends media to that source port (which could be the port where the media egressed
                                       the firewall, not an endpoint port) |
| TURN control | Any IP address† | >=1024 (signaling port from endpoint or the firewall) | UDP & TCP | Expressway-E | 3478 (Small/Medium) 3478-3483 (Large) |
| TURN control | Expressway-C | >=1024 | UDP & TCP | Expressway-E | 3478 (Small/Medium) 3478-3483 (Large) |
| TURN media | Expressway-E | 24000-29999 | UDP & TCP | Any IP address | >=1024 |
| TURN media | Any IP address‡ | >=1024 Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port | UDP & TCP | Expressway-E | 24000-29999 |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Initial RAS connection | Registered endpoint in the Internet | 1719 | UDP | Expressway-E (public) | 1719 |
| Initial RAS connection | Expressway-E (public) | 1719 | UDP | Registered endpoint in the Internet | 1719 |
| Initial RAS connection | External address of firewall protecting off-premises endpoint | >=1024 | UDP | Expressway-E (public) | 1719 |
| Initial RAS connection | Expressway-C | 1719 | UDP | Expressway-E (private) | 6001 (for first traversal zone, 6002 for second etc.) |
| Q.931 / H.225 signaling | Any (endpoint in the Internet) | 1720 | TCP | Expressway-E (public) | 1720 |
| Q.931 / H.225 signaling | External address of firewall protecting off-premises Assent endpoint | >=1024 | TCP | Expressway-E (public) | 2776 |
| Q.931 / H.225 signaling | External address of firewall protecting off-premises H.460.18/19 endpoint | >=1024 | TCP | Expressway-E (public) | 1720 |
| Q.931 / H.225 signaling | Expressway-E (public) | 15000-19999 | TCP | Any (endpoint in the Internet) | 1720 (endpoint signaling port, specified during registration. Could be another port >=1024) |
| Q.931 / H.225 signaling | Expressway-C | 15000-19999 | TCP | Expressway-E (private) | 2776 (Assent calls) |
| Q.931 / H.225 signaling | Expressway-C | 15000-19999 | TCP | Expressway-E (private) | 1720 (H.460.18 calls) |
| H.245 | Expressway-C | 15000-19999 | TCP | Expressway-E (private) | 2776 (Assent calls) |
| H.245 | Expressway-C | 15000-19999 | TCP | Expressway-E (private) | 2777 (H.460.18 calls) |
| H.245 | Any (endpoint in the Internet) | >=1024 | TCP | Expressway-E (public) | 15000-19999 |
| H.245 | Expressway-E (public) | 15000-19999 | TCP | Any (endpoint in the Internet) | >=1024 (endpoint H.245 signaling port) |
| H.245 | External address of firewall protecting off-premises Assent endpoint | >=1024 | TCP | Expressway-E (public) | 2776 |
| H.245 | External address of firewall protecting off-premises H.460.18/19 endpoint | >=1024 | TCP | Expressway-E (public) | 2777 |
| RTP (multiplexed traversal media) | Expressway-C | 36000-59998 (even ports) | UDP | Expressway-E (private) | 2776 (Small/Medium) or 36000-36010 (even ports) (Large) |
| RTCP (multiplexed traversal media) | Expressway-C | 36001-59999 (odd ports) | UDP | Expressway-E (private) | 2777 (Small/Medium) or 36001-36011 (odd ports) (Large) |
| RTP (non-multiplexed traversal media) | Expressway-C | 36000-59998 (even ports) | UDP | Expressway-E (private) | 36000-59998 (even ports) |
| RTCP (non-multiplexed traversal media) | Expressway-C | 36001-59999 (odd ports) | UDP | Expressway-E (private) | 36001-59999 (odd ports) |
| RTP (non-multiplexed) | Expressway-E (public) | 36000-59998 (even ports) | UDP | Any (endpoint in the Internet) | >=1024 (endpoint media range) |
| RTCP (non-multiplexed) | Expressway-E (public) | 36001-59999 (odd ports) | UDP | Any (endpoint in the Internet) | >=1024 (endpoint media range) |
| RTP (non-multiplexed) | Any (endpoint in the Internet) | >=1024 (endpoint media range) | UDP | Expressway-E (public) | 36000-59998 (even ports) |
| RTCP (non-multiplexed) | Any (endpoint in the Internet) | >=1024 (endpoint media range) | UDP | Expressway-E (public) | 36001-59999 (odd ports) |
| RTP (multiplexed traversal media) | External address of firewall protecting off-premises H.460 endpoint (multiplexed media) | >=1024 | UDP | Expressway-E (public) | 2776 (Small/Medium) or 36000-36010 (even ports) (Large) |
| RTCP (multiplexed traversal media) | External address of firewall protecting off-premises H.460 endpoint (multiplexed media) | >=1024 | UDP | Expressway-E (public) | 2777 (Small/Medium) or 36001-36011 (odd ports) (Large) |
| RTP (multiplexed traversal media) | External address of firewall protecting off-premises H.460 endpoint (non-multiplexed media) | >=1024 | UDP | Expressway-E (public) | 36000-59998 (even ports) |
| RTCP (multiplexed traversal media) | External address of firewall protecting off-premises H.460 endpoint (non-multiplexed media) | >=1024 | UDP | Expressway-E (public) | 36001-59999 (odd ports) |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| SNMP for discovery of Expressway-E | Cisco TMS External IP | 1024-65535 | UDP | Expressway-E private | 161 |
| SNMP for discovery of Expressway-C | Cisco TMS | 1024-65535 | UDP | Expressway-C | 161 |
| HTTP Management of Expressway-E | Cisco TMS External IP | 1024-65535 | TCP | Expressway-E private IP | 80 |
| HTTP Management of Expressway-C | Cisco TMS | 1024-65535 | TCP | Expressway-E private IP | 80 |
| HTTPS Management of Expressway-E | Cisco TMS External IP | 1024-65535 | TCP | Expressway-E private | 443 |
| HTTPS Management of Expressway-C | Cisco TMS | 1024-65535 | TCP | Expressway-C | 443 |
| Feedback events (HTTP) | Expressway-E private | 1024-65535 | TCP | Cisco TMS External IP | 80 |
| Feedback events (HTTP) | Expressway-C | 1024-65535 | TCP | Cisco TMS | 80 |
| Feedback events (HTTPS) | Expressway-E private | 1024-65535 | TCP | Cisco TMS External IP | 443 |
| Feedback events (HTTPS) | Expressway-C | 1024-65535 | TCP | Cisco TMS | 443 |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Authentication requests from the Expressway-C | Expressway-C | 1024-65535 | TCP | Directory Server | 389 |
| Authentication requests from the Expressway-E | Expressway-E private | 1024-65535 | TCP | Directory Server | 389 |
| Encrypted authentication requests from the Expressway-C | Expressway-C | 1024-65535 | TLS | Directory Server | 636 |
| Encrypted authentication requests from the Expressway-E | Expressway-E private | 1024-65535 | TLS | Directory Server | 636 |