---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-0-english-install-guide-hard-ins-vg248hwo-html-55df0c9c82
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_0/english/install/guide/hard_ins/vg248hwo.html
retrieved_at: 2026-08-22T01:16:33.567340+00:00
---

Hardware Installation Guide (Version 1.0)

# Hardware Installation Guide (Version 1.0)

Updated: March 17, 2015

Chapter: Overview

## Chapter: Overview

## Overview

The Cisco VG248 Analog Phone Gateway (VG248) enables you to connect analog telephones, modems, and fax machines to the Cisco CallManager IP telephony system.

These sections provide an overview of the VG248:

• Introduction

• Front Panel

• Rear Panel

## Introduction

The VG248 is a 19-inch rack-mountable hardware device. It includes 48 FXS port interfaces to connect directly to standard analog telephones, modems, or fax machines. The analog devices connected through the FXS port behave as if they are connected to a normal central office (CO) or PBX line, supporting features such as call waiting, caller ID, call transfer, and call transfer.

The VG248 also includes a 10/100 Mbps Ethernet port interface to connect to the Ethernet network for connectivity to Cisco CallManager and the IP telephony network.

Figure 1-1 provides an overview of the entire device.

Figure 1-1 VG248 Overview

These sections provide additional detail about the VG248 and its interfaces:

• Front Panel

• Rear Panel

## Front Panel

Figure 1-2 provides an overview of the interfaces and LED displays on the front panel of the VG248.

Figure 1-2 VG248 Front Panel

FXS telco connectors, ports 1-24 and 25-48

System status indicators

Port status indicators, ports 1-24 and 25-48

Ethernet port

Async 1 and 2 ports, unused

Ethernet status indicators

Console port

### FXS Telco Connectors

The FXS interface consists of two telco (RJ-21) connectors featuring these characteristics:

• On-premise connections only—analog phones must be physically located in the same building as the VG248.

• Maximum supported line length—5000 feet or 415 Ohms .

• Loop start support

• Support for disconnect supervision

• DTMF dialing

• Maximum ringer equivalency number (REN) load—3 per line, and only two phones per line can be off-hook at any one time

• Voice activity detection

• Supported codecs—G.711 and G.729a codecs; the same codec must be used for both directions.

Table 1-1 describes the FXS connector pinouts for ports 1-24.

Table 1-1 FXS Ports 1-24 Connector Pinouts

1, 26

Port 1 transmit/receive

2, 27

Port 2 transmit/receive

3, 28

Port 3 transmit/receive

4,29

Port 4 transmit/receive

5, 30

Port 5 transmit/receive

6,31

Port 6 transmit/receive

7, 32

Port 7 transmit/receive

8, 33

Port 8 transmit/receive

9, 34

Port 9 transmit/receive

10, 35

Port 10 transmit/receive

11, 36

Port 11 transmit/receive

12, 37

Port 12 transmit/receive

13, 38

Port 13 transmit/receive

14, 39

Port 14 transmit/receive

15, 40

Port 15 transmit/receive

16, 41

Port 16 transmit/receive

17, 42

Port 17 transmit/receive

18, 43

Port 18 transmit/receive

19, 44

Port 19 transmit/receive

20, 45

Port 20 transmit/receive

21, 46

Port 21 transmit/receive

22, 47

Port 22 transmit/receive

23, 48

Port 23 transmit/receive

24, 49

Port 24 transmit/receive

25, 50

Unused

Table 1-2 describes the FXS connector pinouts for ports 25-48.

Table 1-2 FXS Ports 25-48 Connector Pinouts

1, 26

Port 25 transmit/receive

2, 27

Port 26 transmit/receive

3, 28

Port 27 transmit/receive

4,29

Port 28 transmit/receive

5, 30

Port 29 transmit/receive

6,31

Port 30 transmit/receive

7, 32

Port 31 transmit/receive

8, 33

Port 32 transmit/receive

9, 34

Port 33 transmit/receive

10, 35

Port 34 transmit/receive

11, 36

Port 35 transmit/receive

12, 37

Port 36 transmit/receive

13, 38

Port 37 transmit/receive

14, 39

Port 38 transmit/receive

15, 40

Port 39 transmit/receive

16, 41

Port 40 transmit/receive

17, 42

Port 41 transmit/receive

18, 43

Port 42 transmit/receive

19, 44

Port 43 transmit/receive

20, 45

Port 44 transmit/receive

21, 46

Port 45 transmit/receive

22, 47

Port 46 transmit/receive

23, 48

Port 47 transmit/receive

24, 49

Port 48 transmit/receive

25, 50

Unused

### Status Indicators

Three sets of status indicator LEDs on the front panel display the VG248 status:

• Port Status Indicators

• System Status Indicators

• Ethernet Status Indicators

Table 1-3 includes descriptions of the LED states of these status indicators.

Table 1-3 LED Status Explanation

Ports 1-24

Off hook

Ringing

Not connected or on hook

Ports 25-48

Off hook

Ringing

Not connected or on hook

Power

Power connected and operating normally

N/A

Power not connected

Console

Console link connected

N/A

Console link not connected

Status

Operating normally

Potential hardware error detected.

Check the event log for details.

Not operating normally

TX

N/A

Packet transmitted.

Nothing transmitted

RX

N/A

Packet received.

Nothing received

100

Connected at 100 Mbps

N/A

Connected at 10 Mbps or not connected

Link

Ethernet link connected

N/A

Not connected

### Console Port

Use the console port to connect the VG248 to a console terminal for configuration and management tasks. Table 1-4 describes the console port connector pinouts.

Table 1-4 Console Port Connector Pinouts

1, 8

Connected to each other

2

DTR

3

TxD

4,5

Ground

6

RxD

7

DSR

### Ethernet Port

Use the Ethernet port to connect the VG 248 to the IP network to access Cisco CallManager. Table 1-5 describes the Ethernet port connector pinouts.

Table 1-5 Ethernet Port Connector Pinouts

1

TD+

2

TD-

3

RD+

4

—

5

—

6

RD-

7

—

8

—

## Rear Panel

The rear panel of the VG248 includes the power connector (see Figure 1-3 ). The VG248 has a single AC inlet requiring 100- 240 VAC, 50-60 Hz. The VG248 draws approximately 176W at 100v in its maximum load condition.

Figure 1-3 VG248 Rear Panel

Power connector

| 1 | FXS telco connectors, ports 1-24 and 25-48 | 5 | System status indicators |
|---|---|---|---|
| 2 | Port status indicators, ports 1-24 and 25-48 | 6 | Ethernet port |
| 3 | Async 1 and 2 ports, unused | 7 | Ethernet status indicators |
| 4 | Console port |  |  |

| Pin Number | Function |
|---|---|
| 1, 26 | Port 1 transmit/receive |
| 2, 27 | Port 2 transmit/receive |
| 3, 28 | Port 3 transmit/receive |
| 4,29 | Port 4 transmit/receive |
| 5, 30 | Port 5 transmit/receive |
| 6,31 | Port 6 transmit/receive |
| 7, 32 | Port 7 transmit/receive |
| 8, 33 | Port 8 transmit/receive |
| 9, 34 | Port 9 transmit/receive |
| 10, 35 | Port 10 transmit/receive |
| 11, 36 | Port 11 transmit/receive |
| 12, 37 | Port 12 transmit/receive |
| 13, 38 | Port 13 transmit/receive |
| 14, 39 | Port 14 transmit/receive |
| 15, 40 | Port 15 transmit/receive |
| 16, 41 | Port 16 transmit/receive |
| 17, 42 | Port 17 transmit/receive |
| 18, 43 | Port 18 transmit/receive |
| 19, 44 | Port 19 transmit/receive |
| 20, 45 | Port 20 transmit/receive |
| 21, 46 | Port 21 transmit/receive |
| 22, 47 | Port 22 transmit/receive |
| 23, 48 | Port 23 transmit/receive |
| 24, 49 | Port 24 transmit/receive |
| 25, 50 | Unused |

| Pin Number | Function |
|---|---|
| 1, 26 | Port 25 transmit/receive |
| 2, 27 | Port 26 transmit/receive |
| 3, 28 | Port 27 transmit/receive |
| 4,29 | Port 28 transmit/receive |
| 5, 30 | Port 29 transmit/receive |
| 6,31 | Port 30 transmit/receive |
| 7, 32 | Port 31 transmit/receive |
| 8, 33 | Port 32 transmit/receive |
| 9, 34 | Port 33 transmit/receive |
| 10, 35 | Port 34 transmit/receive |
| 11, 36 | Port 35 transmit/receive |
| 12, 37 | Port 36 transmit/receive |
| 13, 38 | Port 37 transmit/receive |
| 14, 39 | Port 38 transmit/receive |
| 15, 40 | Port 39 transmit/receive |
| 16, 41 | Port 40 transmit/receive |
| 17, 42 | Port 41 transmit/receive |
| 18, 43 | Port 42 transmit/receive |
| 19, 44 | Port 43 transmit/receive |
| 20, 45 | Port 44 transmit/receive |
| 21, 46 | Port 45 transmit/receive |
| 22, 47 | Port 46 transmit/receive |
| 23, 48 | Port 47 transmit/receive |
| 24, 49 | Port 48 transmit/receive |
| 25, 50 | Unused |

| LED | On | Flashing | Off |
|---|---|---|---|
| Port Status Indicators |
| Ports 1-24 | Off hook | Ringing | Not connected or on hook |
| Ports 25-48 | Off hook | Ringing | Not connected or on hook |
| System Status Indicators |
| Power | Power connected and operating normally | N/A | Power not connected |
| Console | Console link connected | N/A | Console link not connected |
| Status | Operating normally | Potential hardware error detected. Check the event log for details. | Not operating normally |
| Ethernet Status Indicators |
| TX | N/A | Packet transmitted. | Nothing transmitted |
| RX | N/A | Packet received. | Nothing received |
| 100 | Connected at 100 Mbps | N/A | Connected at 10 Mbps or not connected |
| Link | Ethernet link connected | N/A | Not connected |

| Pin Number | Function |
|---|---|
| 1, 8 | Connected to each other |
| 2 | DTR |
| 3 | TxD |
| 4,5 | Ground |
| 6 | RxD |
| 7 | DSR |

| Pin Number | Function |
|---|---|
| 1 | TD+ |
| 2 | TD- |
| 3 | RD+ |
| 4 | — |
| 5 | — |
| 6 | RD- |
| 7 | — |
| 8 | — |

| 1 | Power connector |
|---|---|