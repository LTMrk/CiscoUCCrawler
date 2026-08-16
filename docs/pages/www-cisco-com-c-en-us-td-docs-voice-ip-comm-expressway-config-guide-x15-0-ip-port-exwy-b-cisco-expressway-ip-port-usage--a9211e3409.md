---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--a9211e3409
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_clustering-connections.html
retrieved_at: 2026-08-16T15:15:06.682341+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: Clustering Connections

## Chapter: Clustering Connections

# Clustering Connections

## Cluster Connections Before X8.8

## Cluster Port Reference Before X8.8

Purpose

Src. Ports

Protocol

Dest. IP

Dest. Ports

Cluster database synchronization (IPSec AH)

This peer

N/A

51

Other peers

N/A

Key exchange between peers (ISAKMP)

This peer

500

UDP

Other peers

500

Cluster recovery

This peer

30000-35999

UDP

Other peers

4371

Cluster communication

This peer

30000-35999

TCP

Other peers

4369-4380

Bandwidth management (Expressway-C cluster only)

This peer

1719

UDP

Other peers

1719

## Cluster Connections X8.8 Onwards

## Cluster Port Reference X8.8 Onwards

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

Cluster recovery

This peer

30000-35999

TCP

Other peers

4371

Cluster communication

This peer

30000-35999

TLS

Other peers

4372

Bandwidth management

This peer

1719

UDP

Other peers

1719

Purpose

Src. IP

Src. Ports

Protocol

Dest. IP

Dest. Ports

SIP TCP Signaling

This peer

25000-29999

TCP

Other peers

5061

SIP TLS Signaling

This peer

25000-29999

TLS

Other peers

5061

RTP/RTCP

This peer

36000-59999

UDP

Other peers

36000-59999

Bandwidth management

This peer

1719

UDP

Other peers

1719

Dbxsh is a python script that connects to a cluster database on the local loopback address over port 4370. The Dbxsh does
                                       not need to authenticate the database before executing the commands. The port is open for connection and is strictly for internal
                                       use only. This is accessible from root only.

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Cluster database synchronization (IPSec AH) | This peer | N/A | 51 | Other peers | N/A |
| Key exchange between peers (ISAKMP) | This peer | 500 | UDP | Other peers | 500 |
| Cluster recovery | This peer | 30000-35999 | UDP | Other peers | 4371 |
| Cluster communication | This peer | 30000-35999 | TCP | Other peers | 4369-4380 |
| Bandwidth management (Expressway-C cluster only) | This peer | 1719 | UDP | Other peers | 1719 |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| Cluster recovery | This peer | 30000-35999 | TCP | Other peers | 4371 |
| Cluster communication | This peer | 30000-35999 | TLS | Other peers | 4372 |
| Bandwidth management | This peer | 1719 | UDP | Other peers | 1719 |

| Purpose | Src. IP | Src. Ports | Protocol | Dest. IP | Dest. Ports |
|---|---|---|---|---|---|
| SIP TCP Signaling | This peer | 25000-29999 | TCP | Other peers | 5061 |
| SIP TLS Signaling | This peer | 25000-29999 | TLS | Other peers | 5061 |
| RTP/RTCP | This peer | 36000-59999 | UDP | Other peers | 36000-59999 |
| Bandwidth management | This peer | 1719 | UDP | Other peers | 1719 |

| Note | Dbxsh is a python script that connects to a cluster database on the local loopback address over port 4370. The Dbxsh does
                                       not need to authenticate the database before executing the commands. The port is open for connection and is strictly for internal
                                       use only. This is accessible from root only. |
|---|---|