---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-software-configuration-vg410-software-config-guide-configuring-vg410--f26af5cb1a
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/software-configuration/vg410-software-config-guide/configuring-vg410-voice-ports.html
retrieved_at: 2026-08-22T01:18:13.730658+00:00
---

Cisco VG410 Voice Gateway Software Configuration Guide

# Cisco VG410 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Configuring the Voice Ports

## Chapter: Configuring the Voice Ports

- Configuring the Voice Ports

# Configuring the Voice Ports

## Voice Ports in Cisco VG410 Voice Gateway

The Cisco VG410 Voice Gateway supports the following SKUs:

VG410-24FXS: This has 24 analog FXS ports and no FXO port

VG410-24FXS/4FXO: This has 24 analog FXS ports and 4 FXO ports

VG410-48FXS: This has 48 analog FXS ports and no FXO port

## Signaling Types for the Analog Ports

FXS Ports: This voice port supports loop start, ground start, and DID signaling types.

FXO Ports: This voice port supports loop start and ground start signaling types.

## SKU Information

See the following table for information on the voice ports that are supported on these SKUs

SKUs

VG410-24FXS

VG410-24FXS/4FXO

VG410-48FXS

FXS Ports

24

24

48

FXO Ports

0

4

0

Number of Failed Over Ports

N/A

4

N/A

DID and long loop ports

24, 0/1/0 to 0/1/23

24, 0/1/0 to 0/1/23

24, 0/1/0 to 1/1/23

Maximum REN

16

16

24

RJ21 Connectors

1

1

2

## Fail Over Port Mapping

To view the fail over port mapping for Cisco VG410 Voice Gateway , see the following sample output of the show voice port summary:

```
VG410-24FXS/4FXO: provide 4 power fail-over ports:
PWR FAILOVER PORT        PSTN FAILOVER PORT
==================        ==================
0/1/0                    FXO BYPASS 0/1/24
0/1/1                    FXO BYPASS 0/1/25
0/1/2                    FXO BYPASS 0/1/26
0/1/3                    FXO BYPASS 0/1/27
```

## Configuring the Voice Ports

Cisco VG410 Voice Gateway supports FXS and FXO voice ports. To know how to configure these voice ports, see the Voice Port Configuration Guide .

To view detailed information about voice port configuration, see the Cisco IOS Voice Configuration Library .

It is recommended that you configure the interdigit timeout value for the voice ports. To configure this value for a specified
                                       voice port, use the timeouts interdigit <seconds> command in the voice-port configuration mode. If you do not configure this value, by default, the value is 10 seconds.

| SKUs | VG410-24FXS | VG410-24FXS/4FXO | VG410-48FXS |
|---|---|---|---|
| FXS Ports | 24 | 24 | 48 |
| FXO Ports | 0 | 4 | 0 |
| Number of Failed Over Ports | N/A | 4 | N/A |
| DID and long loop ports | 24, 0/1/0 to 0/1/23 | 24, 0/1/0 to 0/1/23 | 24, 0/1/0 to 1/1/23 |
| Maximum REN | 16 | 16 | 24 |
| RJ21 Connectors | 1 | 1 | 2 |

| Note | It is recommended that you configure the interdigit timeout value for the voice ports. To configure this value for a specified
                                       voice port, use the timeouts interdigit <seconds> command in the voice-port configuration mode. If you do not configure this value, by default, the value is 10 seconds. |
|---|---|