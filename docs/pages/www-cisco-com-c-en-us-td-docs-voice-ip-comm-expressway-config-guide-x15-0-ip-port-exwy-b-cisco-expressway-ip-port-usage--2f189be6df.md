---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--2f189be6df
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_microsoft-interoperability-using-gateway-expressway.html
retrieved_at: 2026-08-16T15:15:23.736372+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: Microsoft Interoperability Using Gateway Expressway

## Chapter: Microsoft Interoperability Using Gateway Expressway

# Microsoft Interoperability Using Gateway Expressway

## On-Premises Microsoft Clients

## Off-Premises Microsoft Clients

## Expressway with Microsoft Infrastructure Port Reference

### About the deployment connections and ports

Trunk connections between Microsoft infrastructure elements not shown.

Media/signaling connections required for Microsoft client to client calls not shown.

Microsoft port ranges may vary from those shown here; check the Microsoft documentation to determine the port ranges defined
                                    for your infrastructure.

Cisco Unified Communications Manager and collaboration endpoint connections not shown (for clarity). You can see an example
                                    of those on MRA Connections .

Multiple media paths are possible because there are two TURN servers in the DMZ. "Any" source IP address is listed because
                                    ICE negotiation could mean the media path uses a relay address provided by one of the TURN servers, or a reflexive address
                                    from the egress side of a firewall/NAT.

The Microsoft Interoperability service on the gateway Expressway has a shared pool of media ports (default 56000-57000). The
                                    service can use any port in the range for media connection on either TCP or UDP transport.

The drawing shows two IP addresses on the Expressway-E because you may have one or two NICs enabled on the Expressway-E. The
                                    address you enter for the TURN server (on the Microsoft interoperability configuration of the gateway Expressway) is the one
                                    that should listen on 3478 (TCP and UDP).

Purpose

Src. IP

Src. ports

Protocol

Dest. IP

Dst. Ports

SIP signaling to Lync environment

Gateway Expressway

25000-29999

TLS

Lync FE Server

5061

SIP signaling from Lync environment

Lync FE Server

Ephemeral ports (1024-65535)

TLS

Gateway Expressway: MS interop B2BUA

65072

SIP signaling

Microsoft client

5061

MTLS

Microsoft Edge

5061

SIP signaling

Microsoft Edge

5061

MTLS

Microsoft client

5061

SIP/TLS & TCP TURN

Microsoft client

443

TLS

Microsoft Edge

443

SIP/TLS & TCP TURN

Microsoft Edge

443

TLS

Microsoft client

443

STUN

Microsoft client

3478

UDP

Microsoft Edge

3478

STUN

Microsoft Edge

3478

UDP

Microsoft client

3478

AV media to on-prem Lync clients

Gateway Expressway

56000-57000

UDP

Lync clients

Lync client media ports

Screen sharing from on-prem Lync clients

Lync client

443

TCP

Gateway Expressway

56000-57000

Media from Microsoft interoperability B2BUA towards on-premises Cisco collaboration recipients

Gateway Expressway

56000-57000

UDP

Deployment dependent; bridge, endpoint, or a SIP proxy

Endpoint media ports

ICE negotiation and TURN requests from Gateway Expressway to Expressway-E TURN server

Gateway Expressway

56000-57000

UDP or TCP

Expressway-E TURN server

UDP 3478

TCP 3478

(3478-3483 on large systems)

UDP TURN media relays

Expressway-E TURN server

24000-29999

UDP

Any (reflexive or relay) from MS client or Edge

50000-59999 (Edge range) or client media ports

TCP TURN media relays

Expressway-E TURN server

24000-29999

TCP

Any (reflexive or relay) from MS client or Edge

50000-59999 (Edge range) or client media ports

| Purpose | Src. IP | Src. ports | Protocol | Dest. IP | Dst. Ports |
|---|---|---|---|---|---|
| SIP signaling to Lync environment | Gateway Expressway | 25000-29999 | TLS | Lync FE Server | 5061 |
| SIP signaling from Lync environment | Lync FE Server | Ephemeral ports (1024-65535) | TLS | Gateway Expressway: MS interop B2BUA | 65072 |
| SIP signaling | Microsoft client | 5061 | MTLS | Microsoft Edge | 5061 |
| SIP signaling | Microsoft Edge | 5061 | MTLS | Microsoft client | 5061 |
| SIP/TLS & TCP TURN | Microsoft client | 443 | TLS | Microsoft Edge | 443 |
| SIP/TLS & TCP TURN | Microsoft Edge | 443 | TLS | Microsoft client | 443 |
| STUN | Microsoft client | 3478 | UDP | Microsoft Edge | 3478 |
| STUN | Microsoft Edge | 3478 | UDP | Microsoft client | 3478 |
| AV media to on-prem Lync clients | Gateway Expressway | 56000-57000 | UDP | Lync clients | Lync client media ports |
| Screen sharing from on-prem Lync clients | Lync client | 443 | TCP | Gateway Expressway | 56000-57000 |
| Media from Microsoft interoperability B2BUA towards on-premises Cisco collaboration recipients | Gateway Expressway | 56000-57000 | UDP | Deployment dependent; bridge, endpoint, or a SIP proxy | Endpoint media ports |
| ICE negotiation and TURN requests from Gateway Expressway to Expressway-E TURN server | Gateway Expressway | 56000-57000 | UDP or TCP | Expressway-E TURN server | UDP 3478 TCP 3478 (3478-3483 on large systems) |
| UDP TURN media relays | Expressway-E TURN server | 24000-29999 | UDP | Any (reflexive or relay) from MS client or Edge | 50000-59999 (Edge range) or client media ports |
| TCP TURN media relays | Expressway-E TURN server | 24000-29999 | TCP | Any (reflexive or relay) from MS client or Edge | 50000-59999 (Edge range) or client media ports |