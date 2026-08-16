---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--8a9fa8bc77
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_default-port-ranges.html
retrieved_at: 2026-08-16T15:14:58.246804+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: Default Port Ranges

## Chapter: Default Port Ranges

- Default Port Ranges

# Default Port Ranges

The following defaults are used throughout this document. Default port ranges may occasionally change (if unavoidable) as
                        new features are developed. Our documents list the current default ports for the given version number.

In some cases throughout this document we list port ranges used by third party infrastructure. These are default values and
                                    we cannot guarantee that these are correct for your environment. We recommend you follow the supplier's documentation to configure
                                    those connections.

Protocol

Purpose

Current Range

Details

TCP

Ephemeral ports

1024-65535

Outbound HTTP/S, LDAP

UDP

Ephemeral ports

1024-65535

DNS, outbound TURN requests

TCP

Ephemeral ports

30000-35999

UDP

Ephemeral ports

30000-35999

TCP

Outbound SIP

25000-29999

UDP&TCP

Inbound TURN requests on Small/Medium Expressway-E

3478

On Expressway-E only. Configurable to 443 or any port >= 1024

UDP&TCP

Inbound TURN requests on Large Expressway-E

3478-3483

On Large Expressway-E only. Configurable to a six port range with first port >=1024.

Configurable to a single port, if port multiplexing is enabled. For more information on TURN port multiplexing, see the Expressway Administrator Guide

TCP

Inbound TCP TURN request on Cisco Expressway-E

443

On Expressway-E only if TCP 443 TURN service is enabled.

UDP

TURN relays

24000-29999

On Expressway-E only.

UDP

RTP/RTCP media

36000-59999

The range is configurable within the default bounds. E.g., 37000-38200, but not 35000-36200.

On S/M Expressway, the first two ports can be used for multiplexed media if you do not use default/custom ports.

On L Expressway, the first twelve ports of the range are used for multiplexed media. You cannot customize that subrange.

UDP

Multiplexed media on Small/Medium Expressway-E systems

2776/2777 OR 36000/36001

2776/2777 is older pair but kept as default by the ability to customize when the new default range was introduced with S/M
                                    system options. Custom pair is defined on Configuration > Traversal > Ports .

On Expressway-E only.

In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have chosen to use 36000/36001 instead, then you don't need to also open 2776/2777.

UDP

Multiplexed media on Large Expressway-E systems

36000-36011

New range introduced with Large system option. This range is always the first twelve ports of the RTP/RTCP media range, so
                                    it will be different if you configure a different media range.

On Expressway-E Large OVAs or large scale appliances only.

In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have a large Expressway, then you should open the first twelve ports of the media range instead
                                                of 2776/2777.

TCP

SIP traversal

7001

Configurable. SIP listening port on the first Expressway-E traversal server zone. Subsequent traversal server zones will use
                                    incremental port numbers, eg. 7002, by default.

UDP

H.323 traversal

6001

Configurable. H.323 listening port on the first Expressway-E traversal server zone. Subsequent traversal server zones will
                                    use incremental port numbers, eg. 6002, by default.

| Note | In some cases throughout this document we list port ranges used by third party infrastructure. These are default values and
                                    we cannot guarantee that these are correct for your environment. We recommend you follow the supplier's documentation to configure
                                    those connections. |
|---|---|

| Protocol | Purpose | Current Range | Details |
|---|---|---|---|
| TCP | Ephemeral ports | 1024-65535 | Outbound HTTP/S, LDAP |
| UDP | Ephemeral ports | 1024-65535 | DNS, outbound TURN requests |
| TCP | Ephemeral ports | 30000-35999 |  |
| UDP | Ephemeral ports | 30000-35999 |  |
| TCP | Outbound SIP | 25000-29999 |  |
| UDP&TCP | Inbound TURN requests on Small/Medium Expressway-E | 3478 | On Expressway-E only. Configurable to 443 or any port >= 1024 |
| UDP&TCP | Inbound TURN requests on Large Expressway-E | 3478-3483 | On Large Expressway-E only. Configurable to a six port range with first port >=1024. Configurable to a single port, if port multiplexing is enabled. For more information on TURN port multiplexing, see the Expressway Administrator Guide |
| TCP | Inbound TCP TURN request on Cisco Expressway-E | 443 | On Expressway-E only if TCP 443 TURN service is enabled. |
| UDP | TURN relays | 24000-29999 | On Expressway-E only. |
| UDP | RTP/RTCP media | 36000-59999 | The range is configurable within the default bounds. E.g., 37000-38200, but not 35000-36200. On S/M Expressway, the first two ports can be used for multiplexed media if you do not use default/custom ports. On L Expressway, the first twelve ports of the range are used for multiplexed media. You cannot customize that subrange. |
| UDP | Multiplexed media on Small/Medium Expressway-E systems | 2776/2777 OR 36000/36001 | 2776/2777 is older pair but kept as default by the ability to customize when the new default range was introduced with S/M
                                    system options. Custom pair is defined on Configuration > Traversal > Ports . On Expressway-E only. Note In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have chosen to use 36000/36001 instead, then you don't need to also open 2776/2777. | Note | In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have chosen to use 36000/36001 instead, then you don't need to also open 2776/2777. |
| Note | In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have chosen to use 36000/36001 instead, then you don't need to also open 2776/2777. |
| UDP | Multiplexed media on Large Expressway-E systems | 36000-36011 | New range introduced with Large system option. This range is always the first twelve ports of the RTP/RTCP media range, so
                                    it will be different if you configure a different media range. On Expressway-E Large OVAs or large scale appliances only. Note In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have a large Expressway, then you should open the first twelve ports of the media range instead
                                                of 2776/2777. | Note | In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have a large Expressway, then you should open the first twelve ports of the media range instead
                                                of 2776/2777. |
| Note | In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have a large Expressway, then you should open the first twelve ports of the media range instead
                                                of 2776/2777. |
| TCP | SIP traversal | 7001 | Configurable. SIP listening port on the first Expressway-E traversal server zone. Subsequent traversal server zones will use
                                    incremental port numbers, eg. 7002, by default. |
| UDP | H.323 traversal | 6001 | Configurable. H.323 listening port on the first Expressway-E traversal server zone. Subsequent traversal server zones will
                                    use incremental port numbers, eg. 6002, by default. |

| Note | In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have chosen to use 36000/36001 instead, then you don't need to also open 2776/2777. |
|---|---|

| Note | In the connection maps and port references we do not show all the port options for the sake of clarity. For example, if the
                                                diagram shows 2776/2777, but you have a large Expressway, then you should open the first twelve ports of the media range instead
                                                of 2776/2777. |
|---|---|