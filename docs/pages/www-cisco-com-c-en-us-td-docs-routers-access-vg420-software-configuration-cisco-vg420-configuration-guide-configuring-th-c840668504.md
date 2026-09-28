---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg420-software-configuration-cisco-vg420-configuration-guide-configuring-th-c840668504
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg420/software-configuration/cisco-vg420-configuration-guide/configuring-the-voice-ports.html
retrieved_at: 2026-08-22T01:17:31.688749+00:00
---

Cisco VG420 Voice Gateway Software Configuration Guide

# Cisco VG420 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Configuring the Voice Ports

## Chapter: Configuring the Voice Ports

- Configuring the Voice Ports

# Configuring the Voice Ports

## Voice Ports in Cisco VG420 Voice Gateway

The Cisco VG420 Voice Gateway supports the following SKUs:

VG420-144FXS: This has144 analog FXS ports and no FXO port

VG420-132FXS/6FXO: This has 132 analog FXS ports and 6 FXO ports

VG420-84FXS/6FXO: This has 84 analog FXS ports and 6 FXO ports

## Signaling Types for the Analog Ports

FXS Ports: This voice port supports loop start, ground start, and DID signaling types.

FXO Ports: This voice port supports loop start and ground start signaling types.

## SKU Information

See the following table for information on the voice ports that are supported on these SKUs

SKUs

VG420-144FXS

VG420-132FXS/6FXO

VG420-84FXS/6FXO

FXS Ports

144

132

84

FXO Ports

0

6

6

Number of Failed Over Ports

N/A

6

6

DID and long loop ports

108, 1/0/0 to 1/0/107

108, 1/0/0/ to 1/0/107

84, 1/0/0 to 1/0/83

Maximum REN

80

80

80

RJ21 Connectors

6

6

4

## Fail Over Port Mapping

To view the fail over port mapping for Cisco VG420 Voice Gateway , see the following sample output of the show voice port summary:

```
VG420-132FXS/6FXO: provide 6 power fail-over ports:
PWR FAILOVER PORT        PSTN FAILOVER PORT
==================        ==================
1/0/126                                        FXO BYPASS 1/0/132
1/0/127                                        FXO BYPASS 1/0/133
1/0/128                                        FXO BYPASS 1/0/134
1/0/129                                        FXO BYPASS 1/0/135
1/0/130                                        FXO BYPASS 1/0/136
1/0/131                                        FXO BYPASS 1/0/137

VG420-84FXS/6FXO: provide 6 power fail-over ports:
PWR FAILOVER PORT        PSTN FAILOVER PORT
==================        ==================
1/0/78                                        FXO BYPASS 1/0/84
1/0/79                                        FXO BYPASS 1/0/85
1/0/80                                        FXO BYPASS 0/1/86
1/0/81                                        FXO BYPASS 1/0/87
1/0/82                                        FXO BYPASS 0/1/88
1/0/83                                        FXO BYPASS 1/0/89
```

## Configuring the Voice Ports

Cisco VG420 Voice Gateway supports ds0-group and E&M voice ports on existing voice NIMs (NIM slot 0). To know how to configure these digital ds0-group
                           port, E&M, FXS and FXO voice ports, see the Voice Port Configuration Guide .

To view detailed information about voice port configuration, see the Cisco IOS Voice Configuration Library .

It is recommended that you configure the interdigit timeout value for the voice ports. To configure this value for a specified
                                       voice port, use the timeouts interdigit <seconds> command in the voice-port configuration mode. If you do not configure this value, by default, the value is 10 seconds.

To learn more about this command, see the Cisco IOS Voice Command Reference Guide .

| SKUs | VG420-144FXS | VG420-132FXS/6FXO | VG420-84FXS/6FXO |
|---|---|---|---|
| FXS Ports | 144 | 132 | 84 |
| FXO Ports | 0 | 6 | 6 |
| Number of Failed Over Ports | N/A | 6 | 6 |
| DID and long loop ports | 108, 1/0/0 to 1/0/107 | 108, 1/0/0/ to 1/0/107 | 84, 1/0/0 to 1/0/83 |
| Maximum REN | 80 | 80 | 80 |
| RJ21 Connectors | 6 | 6 | 4 |

| Note | It is recommended that you configure the interdigit timeout value for the voice ports. To configure this value for a specified
                                       voice port, use the timeouts interdigit <seconds> command in the voice-port configuration mode. If you do not configure this value, by default, the value is 10 seconds. To learn more about this command, see the Cisco IOS Voice Command Reference Guide . |
|---|---|