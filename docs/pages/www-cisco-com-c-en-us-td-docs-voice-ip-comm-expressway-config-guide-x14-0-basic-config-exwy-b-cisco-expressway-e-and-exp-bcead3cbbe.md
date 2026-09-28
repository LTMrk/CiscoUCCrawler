---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-bcead3cbbe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_dns-records.html
retrieved_at: 2026-08-16T15:28:05.719599+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: DNS Records

## Chapter: DNS Records

# DNS Records

## DNS Configuration on Host Server

The following records are required in the external DNS which hosts the externally routable domain ( example.com ). This allows:

External endpoints registration messages to be routed to the Expressway-E.

Calls from non-registered endpoints (or other infrastructure devices) to be routed to the Expressway-E.

### Host DNS A Record

Host

Host IP address

expe.example.com

192.0.2.2

### DNS SRV Records

Name

Service

Protocol

Priority

Weight

Port

Target host

example.com.

h323cs

tcp

10

10

1720

expe.example.com.

example.com.

h323ls

udp

10

10

1719

expe.example.com.

example.com.

h323rs

udp

10

10

1719

expe.example.com.

example.com.

sip

tcp

10

10

5060

expe.example.com.

example.com.

sip

udp

10

10

5060

expe.example.com.

example.com.

sips

tcp

10

10

5061

expe.example.com.

example.com.

turn

udp

10

10

3478

expe.example.com.

For example, the DNS records would be:

```
_h323cs._tcp.example.com. 86400 IN SRV 10 10 1720 expe.example.com.
_h323ls._udp.example.com. 86400 IN SRV 10 10 1719 expe.example.com.
_h323rs._udp.example.com. 86400 IN SRV 10 10 1719 expe.example.com.
_sip._tcp.example.com. 86400 IN SRV 10 10 5060 expe.example.com.
_sip._udp.example.com. 86400 IN SRV 10 10 5060 expe.example.com.
_sips._tcp.example.com. 86400 IN SRV 10 10 5061 expe.example.com.
_turn._udp.example.com. 86400 IN SRV 10 10 3478 expe.example.com.
expe.example.com. 86400 IN A 192.0.2.2
```

If you have a cluster of Expressway-Es, you must set up DNS A and SRV records for each peer/host in the cluster. See the Expressway Cluster Creation and Maintenance Deployment Guide for more information.

## DNS Configuration (Internal DNS Server)

The following records are required in the local DNS which hosts the internally routable domain: internal domain.net to allow
                           internal messages to be routed to the Expressway-C.

## Local DNS A Record

Host

Host IP address

expc.internal-domain.net

10.0.0.2

## Local DNS SRV Records

Name

Service

Protocol

Priority

Weight

Port

Target host

internal-

domain.net.

h323cs

tcp

10

10

1720

expc.internal-

domain.net.

internal-

domain.net.

h323ls

udp

10

10

1719

expc.internal-

domain.net.

internal-

domain.net.

h323rs

udp

10

10

1719

expc.internal-

domain.net.

internal-

domain.net.

sip

tcp

10

10

5060

expc.internal-

domain.net.

internal-

domain.net.

sip

udp

10

10

5060

expc.internal-

domain.net.

internal-

domain.net.

sips

tcp

10

10

5061

expc.internal-

domain.net.

For example, the DNS records would be:

```
_h323cs._tcp.internal-domain.net. 86400 IN SRV 10 10 1720 expc.internal-domain.net.
_h323ls._udp.internal-domain.net. 86400 IN SRV 10 10 1719 expc.internal-domain.net.
_h323rs._udp.internal-domain.net. 86400 IN SRV 10 10 1719 expc.internal-domain.net.
_sip._tcp.internal-domain.net. 86400 IN SRV 10 10 5060 expc.internal-domain.net.
_sip._udp.internal-domain.net. 86400 IN SRV 10 10 5060 expc.internal-domain.net.
_sips._tcp.internal-domain.net. 86400 IN SRV 10 10 5061 expc.internal-domain.net.
expc.internal-domain.net. 86400 IN A 10.0.0.2
```

If you have a cluster of Expressway-Cs, you must set up DNS A and SRV records for each peer/host in the cluster. See Expressway Cluster Creation and Maintenance Deployment Guide for more information.

| Host | Host IP address |
|---|---|
| expe.example.com | 192.0.2.2 |

| Name | Service | Protocol | Priority | Weight | Port | Target host |
|---|---|---|---|---|---|---|
| example.com. | h323cs | tcp | 10 | 10 | 1720 | expe.example.com. |
| example.com. | h323ls | udp | 10 | 10 | 1719 | expe.example.com. |
| example.com. | h323rs | udp | 10 | 10 | 1719 | expe.example.com. |
| example.com. | sip | tcp | 10 | 10 | 5060 | expe.example.com. |
| example.com. | sip | udp 1 | 10 | 10 | 5060 | expe.example.com. |
| example.com. | sips | tcp | 10 | 10 | 5061 | expe.example.com. |
| example.com. | turn | udp | 10 | 10 | 3478 2 | expe.example.com. |

| Host | Host IP address |
|---|---|
| expc.internal-domain.net | 10.0.0.2 |

| Name | Service | Protocol | Priority | Weight | Port | Target host |
|---|---|---|---|---|---|---|
| internal- domain.net. | h323cs | tcp | 10 | 10 | 1720 | expc.internal- domain.net. |
| internal- domain.net. | h323ls | udp | 10 | 10 | 1719 | expc.internal- domain.net. |
| internal- domain.net. | h323rs | udp | 10 | 10 | 1719 | expc.internal- domain.net. |
| internal- domain.net. | sip | tcp | 10 | 10 | 5060 | expc.internal- domain.net. |
| internal- domain.net. | sip | udp 3 | 10 | 10 | 5060 | expc.internal- domain.net. |
| internal- domain.net. | sips | tcp | 10 | 10 | 5061 | expc.internal- domain.net. |