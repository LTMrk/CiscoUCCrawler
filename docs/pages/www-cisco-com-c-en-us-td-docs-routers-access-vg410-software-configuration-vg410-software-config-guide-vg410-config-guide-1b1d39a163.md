---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-software-configuration-vg410-software-config-guide-vg410-config-guide-1b1d39a163
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/software-configuration/vg410-software-config-guide/vg410-config-guide-overview.html
retrieved_at: 2026-08-22T01:18:05.396175+00:00
---

Cisco VG410 Voice Gateway Software Configuration Guide

# Cisco VG410 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Overview

## Chapter: Overview

# Overview

The Cisco VG410 Analog Voice Gateway or Cisco VG410 Voice Gateway is a Cisco IOS-XE software-based medium-density analog phone gateway that connects public-switched telephone networks (PSTNs)
                        and existing telephony equipment to Cisco Enterprise Routers.

This voice gateway offers Cisco IOS-XE software manageability on analog phone lines and supports business needs for analog
                        voice ports for modem calls, fax calls, and analog supplementary services.

This device also connects analog phones, fax machines, modems, and speakerphones to the enterprise voice systems and is an
                        intermediate path that enables TDM to IP transition. Further, the fixed-port (FXS and FXO) modules in this voice gateway provide
                        Dual-Tone Multifrequency (DTMF) detection, voice compression and decompression, call progress tone generation, Voice Activity
                        Detection (VAD), echo cancellation, and adaptive jitter buffering.

To know how to install this voice gateway, see the Cisco VG410 Voice Gateway Installation Guide . After installing the voice gateway, use this guide to complete basic router configuration using the setup command facility.

By default, the Cisco VG410 Voice Gateway boots up in the supported Cisco IOS XE platform versions only. To boot the device in a private image release, contact Cisco
                                    Technical Assistance Center (TAC).

This document is a summary of the software functionalities that are specific to Cisco VG410 Voice Gateway . This guide also contains information on using the Cisco IOS software to perform other configuration tasks, such as configuring
                        voice ports and other features.

## Features and Benefits

Cisco VG410 Voice Gateway provides VoIP connectivity to analog devices such as analog desk phones, analog conference room phones, fax machines, and
                           modems. This voice gateway provides several improvements from the previous high-density analog and digital extension modules
                           (EVMs) in the following ways:

Software Digital Signal Processor (DSP): The Cisco VG410 Voice Gateway chassis utilizes its built-in CPU cores to handle the digital signal processing (DSP) tasks required for software implementation.
                                 This means that the functionality typically provided by a separate DSP component is now distributed among the CPU cores within
                                 the device. Further, the CPU cores effectively handle the necessary DSP operations. The software DSP comes pre-installed as
                                 part of the manufacturing process.

FXS-E (extended loops or long loops) support: The first 24 ports of all the SKUs on the new modules support FXS-E with:

Higher loop current (35 mA) to accommodate specialty phones

Longer loop length for loops with 26 AWG wire, up to 11,000 feet (3400 meters)

Higher ringing voltage (65 Vrms, no load)

In addition to these features, Cisco VG410 Voice Gateway supports the following features:

Webex calling

Caller line ID

G.711, G.729a, G.729ab, and G.726

G722, iLBC

Fax pass-through and relay (T.38)

Modem pass-through, Modem relay, and V.150.1 MER modem relay support

DTMF detection

Echo cancellation

Voice activity detection

Comfort noise generation

Real-Time Control Protocol (RTCP)

Acoustic shock protection

Real-Time Transport Protocol (RTP)

RFC 4733 Digit Relay

Noise reduction

Call Details Records (CDR)

Support for Loop-start and Ground start signaling

Support for interworking with Cisco Unified Communications Manager (CUCM): Skinny Client Control Protocol (SCCP), Session
                                 Initiation Protocol (SIP), and Media Gateway Control Protocol (MGCP) 0.1

Cable detection: GR909 line test

### FXS Features

The FXS features include:

Support for either FXS or DID functionality

Message-Waiting Indicator (MWI)

### FXO Features

The FXO features include:

Overload protection

For more information on features, benefits, and other specifications, refer to the Cisco VG410 Voice Gateway Data Sheet .

## Supported Interfaces

Cisco VG410 Voice Gateway supports the following interfaces:

Gigabit Ethernet (GE)

Micro USB console port

RJ45 console port

FXS ports

FXO ports

USB Type A interface

## Cisco VG410 Voice Gateway Chassis

The following images show the I/O panel views of the Cisco VG410 Voice Gateway chassis that help you identify this device:

1

RJ 21 for FXS port

2

FXS LED

3

2X1 GE port

4

RJ45 console

5

Micro USB console

6

USB 3.0 type A port

7

Reset

8

System status indicator

9

Power supply status indicator

10

Temperature indicator

11

Environmental status indicator

1

RJ 21 for FXS port

2

FXS/FXO LED

3

RJ 11 for FXO port

4

2X1 GE port

5

RJ 45 console

6

Micro USB console

7

USB 3.0 Type A port

8

Reset

9

System status indicator

10

Power Supply status indicator

11

Temperature indicator

12

Environmental status indicator

1

RJ 21 for FXS port

2

FXS LED

3

RJ 21 for FXS port

4

2X1 GE port

5

RJ45 console

6

Micro USB console

7

USB 3.0 Type A port

8

Reset

9

System status indicator

10

Power status indicator

11

Temperature indicator

12

Environmental status indicator

| Note | By default, the Cisco VG410 Voice Gateway boots up in the supported Cisco IOS XE platform versions only. To boot the device in a private image release, contact Cisco
                                    Technical Assistance Center (TAC). |
|---|---|

| 1 | RJ 21 for FXS port |
|---|---|
| 2 | FXS LED |
| 3 | 2X1 GE port |
| 4 | RJ45 console |
| 5 | Micro USB console |
| 6 | USB 3.0 type A port |
| 7 | Reset |
| 8 | System status indicator |
| 9 | Power supply status indicator |
| 10 | Temperature indicator |
| 11 | Environmental status indicator |

| 1 | RJ 21 for FXS port |
|---|---|
| 2 | FXS/FXO LED |
| 3 | RJ 11 for FXO port |
| 4 | 2X1 GE port |
| 5 | RJ 45 console |
| 6 | Micro USB console |
| 7 | USB 3.0 Type A port |
| 8 | Reset |
| 9 | System status indicator |
| 10 | Power Supply status indicator |
| 11 | Temperature indicator |
| 12 | Environmental status indicator |

| 1 | RJ 21 for FXS port |
|---|---|
| 2 | FXS LED |
| 3 | RJ 21 for FXS port |
| 4 | 2X1 GE port |
| 5 | RJ45 console |
| 6 | Micro USB console |
| 7 | USB 3.0 Type A port |
| 8 | Reset |
| 9 | System status indicator |
| 10 | Power status indicator |
| 11 | Temperature indicator |
| 12 | Environmental status indicator |