---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg420-hardware-installation-vg420-hardware-installation-guide-overview-cisc-732ba8bbe8
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg420/hardware-installation/vg420-hardware-installation-guide/overview-cisco-vg420.html
retrieved_at: 2026-08-22T01:15:56.063761+00:00
---

Cisco VG420 Voice Gateway Hardware Installation Guide

# Cisco VG420 Voice Gateway Hardware Installation Guide

Updated: December 6, 2021

Chapter: Overview of Cisco VG420 Voice Gateway

## Chapter: Overview of Cisco VG420 Voice Gateway

# Overview of Cisco VG420 Voice Gateway

Cisco High-Density Analog Voice Gateways provide enterprises, managed services providers, and service providers the ability
                        to directly connect public-switched telephone networks (PSTNs) and existing telephony equipment to Cisco Enterprise Routers.

The fixed-port (FXS and FXO) modules in the voice gateway provide Dual-Tone Multifrequency (DTMF) detection, voice compression
                        and decompression, call progress tone generation, Voice Activity Detection (VAD), echo cancellation, and adaptive jitter buffering.

This guide specifies the installation of Cisco VG420 Voice Gateway , a high-density analog voice gateway. This voice gateway is an intermediate path that enables TDM to IP transition.

The Cisco VG420 Voice Gateway supports the following interfaces:

Gigabit Ethernet (GE)

Micro USB Console Port

RJ45 Console Port

FXS Ports

FXO Ports

Network Interface Module (NIM)

## Features and Benefits

The Cisco Voice Gateway provides VoIP connectivity to analog devices such as analog desk phones, analog conference room phones,
                           fax machines, and modems. This voice gateway provides several improvements from the previous high-density analog and digital
                           extension modules (EVMs) in the following ways:

On-board Digital Signal Processor (DSP) : The FXO and FXS service modules contain an onboard DSP and don’t require the router to have a dedicated packet voice DSP
                                 module (PVDM) on the motherboard. The DSP on the voice module is necessary for the voice features. It also provides for echo
                                 cancellation of up to 128-ms echo-tail length for demanding network conditions.

Support for Online Insertion and Removal (OIR) : The FXS and FXO service modules support Online Insertion and Removal (OIR), reducing the downtime required for new or replacement
                                 modules. The service modules can be inserted into the NIM slot on the device without powering off the voice gateway.

FXS-E (extended loops) support : FXS ports on the new modules support FXS-E with the following details:

Higher loop current (35 mA) to accommodate specialty phones

Longer loop length for loops with 26 AWG wire, up to 11,000 feet (3400 meters)

Higher ringing voltage (65 Vrms, no load)

In addition to these features, the following are also supported:

Caller line ID

G.711, G.729a, and G.726

G722, iLBC

Fax detection, pass-through, and relay (T.38)

Modem pass-through

DTMF detection

Echo cancellation

Voice activity detection

Comfort noise generation

Real-Time Control Protocol (RTCP)

Acoustic shock protection

Real-Time Transport Protocol (RTP)

RFC 4733 Digit Relay

Noise reduction

Features supported in Cisco VG410 Voice Gateway:

Webex calling

Call Details Records (CDR)

Support for Loop-start and Ground start signaling

Support for interworking with Cisco Unified Communications Manager (CUCM): Skinny Client Control Protocol (SCCP), Session
                                 Initiation Protocol (SIP), and Media Gateway Control Protocol (MGCP) 0.1

Cable detection: GR909 line test

The FXS features include:

Support for either FXS or DID functionality

Message-Waiting Indicator (MWI)

Cable detection: GR909 line test

The FXO features include:

Support for both ground-start and loop-start modes

Call Detail Record (CDR) information

Support for interworking with Cisco Unified Communications Manager (Skinny Client Control Protocol [SCCP]), Session Initiation
                                 Protocol (SIP), and Media Gateway Control Protocol (MGCP) 0.1

Cable detection

Overload protection

Analog phone connectivity

Fax and modem connectivity

## Protocols Supported

The Cisco VG420 Voice Gateway supports the following protocols:

SCCP

MGCP

SIP

Real-Time Transport Protocol (RTP)

Secure Real-Time Transport Protocol (SRTP)

Trivial File Transfer Protocol (TFTP)

HTTP Server

Simple Network Management Protocol (SNMP)

Telnet

Dynamic Host Configuration Protocol (DHCP)

DNS

T.38 fax relay and modem pass-through

RADIUS and TACACS+ for Telnet and authorization

## Cisco VG420 Voice Gateway Chassis

The following images show the I/O and side panel views of the Cisco VG420 Voice Gateway chassis:

1

Status LEDs

2

FXS LED

3

Serial Console

4

Mini USB Console

5

Ethernet Ports

6

NIM Modules

1

Status LEDs

2

FXS LED

3

Serial Console

4

Mini USB Console

5

Ethernet Ports

6

NIM Modules

1

Status LEDs

2

FXS/FXO LED

3

Serial Console

4

Mini USB Console

5

Ethernet Ports

6

NIM Modules

1

Ground Lug

2

Removable Fan Tray

3

Power Switch

4

PSU1

5

PSU1 (Power LED)

6

PSU0 (Power LED)

7

PSU0

## SKU Information

The following table specifies the Cisco VG420 Voice Gateway SKU information. All the SKUs support the following external interfaces:

Front

Details

WAN Port

Two GE RJ-45 copper interface ports support 10BASE-T, 100BASE-TX, and 1000Base-T

Console port

One RJ45 serial console port and one USB console port

NIM slot

Two NIM slots to host supported NIM voice modules

Back

PSU

Support one or two, hot swappable, redundant PSUs

Fans

Removable fan tray

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

Number of Failed Over Ports

108 (0-107)

108 (0-107)

84 (0-83)

Maximum REN

80

80

80

RJ21 Connectors

6

6

4

## Removable or Interchangeable Modules and Cards

The following are the NIM models that are supported by Cisco VG420 Voice Gateway :

NIM-1MFT-T1/E1

NIM-2MFT-T1/E1

NIM-4MFT-T1/E1

NIM-8MFT-T1/E1

NIM-4E/M

NIM-2FXO

NIM-4FXO

NIM-2FXSP

NIM-4FXSP

NIM-2FXS/4FXOP

NIM-2BRI-NT/TE

NIM-4BRI-NT/TE

The following image represents the NIM slots:

## Locate the Labels

Use the Cisco Product Identification (CPI) tool to find labels on the platform. The tool provides detailed illustrations and
                           descriptions of where labels are located on Cisco products. It includes the following features:

A search option that allows browsing for models by using a tree-structured product hierarchy.

A search field on the final results page that makes it easier to look up multiple products.

End-of-sale products clearly identified in results lists.

The tool streamlines the process of locating the serial number labels and identifying products. Serial number information
                           expedites the entitlement process and is required to access support services.

The following image shows the location of the labels on the voice gateway.

The Serial number (SN), Common language equipment identifier (CLEI), Top Assembly Number (TAN), Product ID (PID), PID version
                           ID (VID), and Quick response (QR) code are printed on a label at the bottom of the hardware or on a label tray located on
                           the chassis.

1

Top Cover

2

PID

3

Label Tray

4

SN

5

CLEI

6

TAN

7

MAC

8

PIDVID

9

QR Code

## LED Information

LED

Colour

Description

PSU

Green/Off

Power Supply Unit

Off: The system is powered off.

PWR

Green/Amber

Power Supply Status

Off: The system is powered off.

Yellow: A Power Supply in the system is not functioning correctly.

Green: All installed PSUs are operating correctly.

STAT (Status)

Green/Amber/Red

System Status

Red: The system is booting

Red Blinking Red: The system has failed a hardware integrity error.

Yellow: Rommon has completed booting and system is at Rommon prompt or booting platform software.

USB CON/SERIAL CON

Green/Yellow

Console Active

RJ-45 CON

Green/Yellow

Serial Console Active

Green indicates that the RJ-45 is the active console port.

TEMP

Green/Yellow/Red

Off: Monitor is not active.

Red: The system has detected a critical overcurrent event and may shut down.

Blinking Yellow: One or more temperature sensors in the system are outside the acceptable range.

Green: All the temperature sensors in the system are within acceptable range.

FAN

Yellow/Green

Yellow: One or more fans in the system are outside the acceptable range.

Green: All temperature sensors and fans in the system are within acceptable range.

FXS/FXO

Green/Off

Green: There is at least one active call on the onboard analog FXS/FXO module.

## Technical Specifications

To access the Cisco VG420 Voice Gateway technical specifications, see the Cisco VG420 Voice Gateway Datasheet .

| 1 | Status LEDs |
|---|---|
| 2 | FXS LED |
| 3 | Serial Console |
| 4 | Mini USB Console |
| 5 | Ethernet Ports |
| 6 | NIM Modules |

| 1 | Status LEDs |
|---|---|
| 2 | FXS LED |
| 3 | Serial Console |
| 4 | Mini USB Console |
| 5 | Ethernet Ports |
| 6 | NIM Modules |

| 1 | Status LEDs |
|---|---|
| 2 | FXS/FXO LED |
| 3 | Serial Console |
| 4 | Mini USB Console |
| 5 | Ethernet Ports |
| 6 | NIM Modules |

| 1 | Ground Lug |
|---|---|
| 2 | Removable Fan Tray |
| 3 | Power Switch |
| 4 | PSU1 |
| 5 | PSU1 (Power LED) |
| 6 | PSU0 (Power LED) |
| 7 | PSU0 |

| Front | Details |
|---|---|
| WAN Port | Two GE RJ-45 copper interface ports support 10BASE-T, 100BASE-TX, and 1000Base-T |
| Console port | One RJ45 serial console port and one USB console port |
| NIM slot | Two NIM slots to host supported NIM voice modules |
| Back |  |
| PSU | Support one or two, hot swappable, redundant PSUs |
| Fans | Removable fan tray |

| SKUs | VG420-144FXS | VG420-132FXS/6FXO | VG420-84FXS/6FXO |
|---|---|---|---|
| FXS Ports | 144 | 132 | 84 |
| FXO Ports | 0 | 6 | 6 |
| Number of Failed Over Ports | N/A | 6 | 6 |
| Number of Failed Over Ports | 108 (0-107) | 108 (0-107) | 84 (0-83) |
| Maximum REN | 80 | 80 | 80 |
| RJ21 Connectors | 6 | 6 | 4 |

| 1 | Top Cover |
|---|---|
| 2 | PID |
| 3 | Label Tray |
| 4 | SN |
| 5 | CLEI |
| 6 | TAN |
| 7 | MAC |
| 8 | PIDVID |
| 9 | QR Code |

| LED | Colour | Description |
|---|---|---|
| PSU | Green/Off | Power Supply Unit Off: The system is powered off. Green: All installed PSUs are operating correctly. |
| PWR | Green/Amber | Power Supply Status Off: The system is powered off. Yellow: A Power Supply in the system is not functioning correctly. Green: All installed PSUs are operating correctly. |
| STAT (Status) | Green/Amber/Red | System Status Red: The system is booting Red Blinking Red: The system has failed a hardware integrity error. Yellow: Rommon has completed booting and system is at Rommon prompt or booting platform software. Green: Indicates normal System Operation. |
| USB CON/SERIAL CON | Green/Yellow | Console Active Green indicates that the console port is active. |
| RJ-45 CON | Green/Yellow | Serial Console Active Green indicates that the RJ-45 is the active console port. |
| TEMP | Green/Yellow/Red | Off: Monitor is not active. Red: The system has detected a critical overcurrent event and may shut down. Blinking Yellow: One or more temperature sensors in the system are outside the acceptable range. Green: All the temperature sensors in the system are within acceptable range. |
| FAN | Yellow/Green | Yellow: One or more fans in the system are outside the acceptable range. Green: All temperature sensors and fans in the system are within acceptable range. |
| FXS/FXO (Voice Port Status) | Green/Off | Green: There is at least one active call on the onboard analog FXS/FXO module. Off: There is no active call on the onboard analog FXS/FXO module. |