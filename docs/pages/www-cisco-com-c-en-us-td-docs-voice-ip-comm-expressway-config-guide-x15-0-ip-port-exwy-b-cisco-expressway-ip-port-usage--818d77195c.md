---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--818d77195c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_mobile-and-remote-access.html
retrieved_at: 2026-08-16T15:15:15.504498+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: Mobile and Remote Access

## Chapter: Mobile and Remote Access

- Mobile and Remote Access

- MRA Connections

- MRA Port Reference

# Mobile and Remote Access

## MRA Connections

## MRA Port Reference

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

RTP/RTCP (ICE passthrough media)†

Off-premises endpoint

Eph

UDP

Off-premises endpoint

Eph

† ICE passthrough calls are supported only between off-premises endpoints. Not supported between off-premises and on-premises
                           endpoints.

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

UDS (phonebook and provisioning)

Off-premises endpoint

1024-65535

TLS

Expressway-E Public IP

8443

SIP signaling

Off-premises endpoint

1024-65535

TLS

Expressway-E Public IP

5061

RTP/RTCP media

Off-premises endpoint

1024-65535

UDP

Expressway-E Public IP

36000-59999

RTP/RTCP media

Expressway-E Public IP

36000-59999

UDP

Off-premises endpoint

1024-65535

XMPP (IM and Presence)

Off-premises endpoint

1024-65535

TCP

Expressway-E Public IP

5222

TURN control (ICE passthrough)

Any IP address†

>=1024 (signaling port from endpoint or the firewall)

UDP

Expressway-E

3478 (Small/Medium)

3478-3483 (Large)

TURN media (ICE passthrough)

Any IP address‡

>=1024

Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port

UDP

Expressway-E

24000-29999

† The request could be from any IP address, unknown to the TURN server. For example, assume that endpoint A and endpoint B
                           (TURN clients) can use the Expressway-E TURN server. The actual IP address from which the TURN server receives the request
                           could be the endpoint's firewall egress address (NATed).

‡ The media could go to any of the candidate addresses. For example, before ICE passthrough negotiation the TURN server does
                           not know which of endpoint B's candidate addresses will be the highest priority.

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

SSH tunnels

Expressway-C

30000-35999

TLS

Expressway-E Private IP

2222

SIP signaling

Expressway-C

25000-29999

TLS

Expressway-E Private IP

7001

SIP media

Expressway-C

36000-59999

UDP

Expressway-E Private IP

2776/7 or 36000-11

XMPP (IM and Presence)

Expressway-C

30000-35999

TCP

Expressway-E Private IP

7400

TURN control

Expressway-C

>=1024

UDP & TCP

Expressway-E

3478 (Small/Medium)

3478-3483 (Large)

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

SIP signaling (TCP)

Expressway-C

25000-29999

TCP

Unified CM

5060†

SIP signaling (TCP)

Unified CM

Ephemeral

TCP

Expressway-C

5060

SIP signaling (TLS)

Expressway-C

25000-29999

TLS

Unified CM

5061*

SIP signaling (TLS)

Unified CM

Ephemeral

TLS

Expressway-C

5061

SIP signaling (OAuth)

Expressway-C

25000-29999

TLS

Unified CM

5091

SIP signaling (OAuth)

Unified CM

5091

TLS

Expressway-C

5061

HTTP Configuration file download (TFTP)

(Pre 11.x Jabber and pre 11.x Unified CM)

Expressway-C

30000-35999

TCP

Unified CM Node

6970

HTTPS Headset Configuration file download (TFTP)

Expressway-C

30000-35999

TLS

Unified CM

6971

HTTPS Configuration file download (TFTP)

(11.x or later Jabber and 11.x or later Unified CM)

Expressway-C

30000-35999

TLS

Unified CM Node

6972

HTTP for UDS (User Data Services) and AXL (Administrative XML Layer)

Expressway-C

30000-35999

TLS

Unified CM Node

443 or 8443

XMPP (IM and Presence)

Expressway-C

30000-35999

TLS

IM and Presence Service Node

7400

HTTPS SOAP (IM and Presence)

Expressway-C

30000-35999

TLS

IM and Presence Service Node

8443

File transfer (IM and Presence)

Expressway-C

30000-35999

TLS

IM and Presence Service Node

7336

HTTPS to visual voicemail

Expressway-C

30000-35999

TLS

Cisco Unity Connection

443 or 8443

MWI (Message Waiting Indicator)

Expressway-C

30000-35999

TCP

Cisco Unity Connection

7080

MWI (Message Waiting Indicator)

Expressway-C

30000-35999

TLS

Cisco Unity Connection

7443

HTTP for metrics POST (Headset Management)

Expressway-C

30000-35999

TCP

Unified CM

9444

Audio Video Media (RTP/RTCP)

Expressway-C

36000-59999

UDP

On-prem media destination

Destination media's range eg, 16384-32767 (DX Series)

† Unified CM can listen on 5061 for TCP SIP but we discourage it.

* If you have MRA connections to the Unified CM which are line-side connections to 5060/5061, avoid using 5060/5061 as the
                           listening port for any SIP trunks you create on that Unified CM.

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

Subscription requests originating from Unified CM

Expressway-E

Ephemeral (30000- 35999)

TLS

fos-a.wbx2.com (onboarding service)

443

Authentication requests originating from Unified CM or IM and Presence Service

Expressway-E

Ephemeral (30000- 35999)

TLS

idbroker.

webex.com

(Common Identity Service)

443

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| RTP/RTCP (ICE passthrough media)† | Off-premises endpoint | Eph | UDP | Off-premises endpoint | Eph |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| UDS (phonebook and provisioning) | Off-premises endpoint | 1024-65535 | TLS | Expressway-E Public IP | 8443 |
| SIP signaling | Off-premises endpoint | 1024-65535 | TLS | Expressway-E Public IP | 5061 |
| RTP/RTCP media | Off-premises endpoint | 1024-65535 | UDP | Expressway-E Public IP | 36000-59999 |
| RTP/RTCP media | Expressway-E Public IP | 36000-59999 | UDP | Off-premises endpoint | 1024-65535 |
| XMPP (IM and Presence) | Off-premises endpoint | 1024-65535 | TCP | Expressway-E Public IP | 5222 |
| TURN control (ICE passthrough) | Any IP address† | >=1024 (signaling port from endpoint or the firewall) | UDP | Expressway-E | 3478 (Small/Medium) 3478-3483 (Large) |
| TURN media (ICE passthrough) | Any IP address‡ | >=1024 Port of relevant ICE candidate: host IP port, server reflexive port (outside firewall port), or TURN server port | UDP | Expressway-E | 24000-29999 |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| SSH tunnels | Expressway-C | 30000-35999 | TLS | Expressway-E Private IP | 2222 |
| SIP signaling | Expressway-C | 25000-29999 | TLS | Expressway-E Private IP | 7001 |
| SIP media | Expressway-C | 36000-59999 | UDP | Expressway-E Private IP | 2776/7 or 36000-11 |
| XMPP (IM and Presence) | Expressway-C | 30000-35999 | TCP | Expressway-E Private IP | 7400 |
| TURN control | Expressway-C | >=1024 | UDP & TCP | Expressway-E | 3478 (Small/Medium) 3478-3483 (Large) |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| SIP signaling (TCP) | Expressway-C | 25000-29999 | TCP | Unified CM | 5060† |
| SIP signaling (TCP) | Unified CM | Ephemeral | TCP | Expressway-C | 5060 |
| SIP signaling (TLS) | Expressway-C | 25000-29999 | TLS | Unified CM | 5061* |
| SIP signaling (TLS) | Unified CM | Ephemeral | TLS | Expressway-C | 5061 |
| SIP signaling (OAuth) | Expressway-C | 25000-29999 | TLS | Unified CM | 5091 |
| SIP signaling (OAuth) | Unified CM | 5091 | TLS | Expressway-C | 5061 |
| HTTP Configuration file download (TFTP) (Pre 11.x Jabber and pre 11.x Unified CM) | Expressway-C | 30000-35999 | TCP | Unified CM Node | 6970 |
| HTTPS Headset Configuration file download (TFTP) | Expressway-C | 30000-35999 | TLS | Unified CM | 6971 |
| HTTPS Configuration file download (TFTP) (11.x or later Jabber and 11.x or later Unified CM) | Expressway-C | 30000-35999 | TLS | Unified CM Node | 6972 |
| HTTP for UDS (User Data Services) and AXL (Administrative XML Layer) | Expressway-C | 30000-35999 | TLS | Unified CM Node | 443 or 8443 |
| XMPP (IM and Presence) | Expressway-C | 30000-35999 | TLS | IM and Presence Service Node | 7400 |
| HTTPS SOAP (IM and Presence) | Expressway-C | 30000-35999 | TLS | IM and Presence Service Node | 8443 |
| File transfer (IM and Presence) | Expressway-C | 30000-35999 | TLS | IM and Presence Service Node | 7336 |
| HTTPS to visual voicemail | Expressway-C | 30000-35999 | TLS | Cisco Unity Connection | 443 or 8443 |
| MWI (Message Waiting Indicator) | Expressway-C | 30000-35999 | TCP | Cisco Unity Connection | 7080 |
| MWI (Message Waiting Indicator) | Expressway-C | 30000-35999 | TLS | Cisco Unity Connection | 7443 |
| HTTP for metrics POST (Headset Management) | Expressway-C | 30000-35999 | TCP | Unified CM | 9444 |
| Audio Video Media (RTP/RTCP) | Expressway-C | 36000-59999 | UDP | On-prem media destination | Destination media's range eg, 16384-32767 (DX Series) |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Subscription requests originating from Unified CM | Expressway-E | Ephemeral (30000- 35999) | TLS | fos-a.wbx2.com (onboarding service) | 443 |
| Authentication requests originating from Unified CM or IM and Presence Service | Expressway-E | Ephemeral (30000- 35999) | TLS | idbroker. webex.com (Common Identity Service) | 443 |