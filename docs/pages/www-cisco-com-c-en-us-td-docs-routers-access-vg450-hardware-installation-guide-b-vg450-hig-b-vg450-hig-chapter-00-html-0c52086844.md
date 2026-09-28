---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg450-hardware-installation-guide-b-vg450-hig-b-vg450-hig-chapter-00-html-0c52086844
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg450/hardware/installation/guide/b_Vg450_hig/b_Vg450_hig_chapter_00.html
retrieved_at: 2026-08-22T01:15:26.496365+00:00
---

Cisco VG450 Voice Gateway Hardware Installation Guide

# Cisco VG450 Voice Gateway Hardware Installation Guide

Updated: October 15, 2018

Chapter: Overview of Cisco VG450 Voice Gateway

## Chapter: Overview of Cisco VG450 Voice Gateway

# Overview of Cisco VG450 Voice Gateway

Cisco High-Density Analog Voice Gateway provide enterprises, managed services providers, and service providers the ability
                        to directly connect public-switched telephone networks (PSTNs) and existing telephony equipment to Cisco 4000 Series Integrated
                        Services Routers. These fixed-port (FXS and FXO) modules provide Dual-Tone Multifrequency (DTMF) detection, voice compression
                        and decompression, call progress tone generation, Voice Activity Detection (VAD), echo cancellation, and adaptive jitter buffering.
                        Cisco VG450 Voice Gateway is a high-density analog voice gateway. It is an intermediate path that enables TDM to IP transition.

The Cisco VG450 Voice Gateway supports the following interfaces:

- Gigabit Ethernet (GE)

- USB

- Network Interface Module (NIM)

- Single-Wide Service Module (SWSM) interface

- Double-Wide Service Module (DWSM) interface

This chapter contains the following sections:

## Features and Benefits of Cisco VG450 Voice Gateway

Cisco VG450 Voice Gateway provides VoIP connectivity to analog devices, such as analog desk phones, analog conference room
                           phones, fax machines and modems. Cisco 450 Voice Gateway provides several improvements from the previous high-density analog
                           and digital extension modules (EVMs), in the following ways:

- On-board Digital Signal Processor (DSP)— The FXO and FXS service modules contain an onboard DSP and don’t require the router to have a dedicated packet voice DSP module
                              (PVDM) on the motherboard. The DSP on the voice module is necessary for the voice features. It also provides for echo cancellation
                              of up to 128-ms echo-tail length for demanding network conditions.

- Support for Online Insertion and Removal (OIR)— The FXS and FXO service modules support Online Insertion and Removal (OIR), reducing the downtime required for new or replacement
                              modules. The service modules can be inserted into the SM-X slot on the supported Cisco 4000 Series ISRs without powering off
                              the router.

- Higher loop current (35 mA) to accommodate specialty phones

- Longer loop length for loops with 26 AWG wire, up to 11,000 feet (3400 meters)

- Higher ringing voltage (65 Vrms, no load)

- FXO failover bypass ports— A failover bypass port, also called a failover trunk bypass, provides a way to use designated analog phone ports to make phone
                              calls through the PSTN during a power outage.

In addition to these features, Cisco 450 Voice Gateway supports the following features:

- Caller line ID

- G.711, G.729a, and G.726

- G722, iLBC, GSMAMR-NB, and Internet Speech Audio Codec (iSAC)

- Fax detection, pass-through, and relay (T.38)

- Modem pass-through

- DTMF detection

- Echo cancellation

- Voice activity detection

- Comfort noise generation

- Real-Time Control Protocol (RTCP)

- Acoustic shock protection

- Real-Time Transport Protocol (RTP)

- RFC 4733 Digit Relay

- Noise reduction is on the roadmap

- The FXS features include:

- Support for either FXS or DID functionality

- Message-Waiting Indicator (MWI)

- Cable detection: GR909 line test

- The FXO features include:

- Support for both ground-start and loop-start modes

- Support for FXO CAMA signaling type

- Call Detail Record (CDR) information

- Support for interworking with Cisco Unified Communications Manager (Skinny Client Control Protocol [SCCP]), H.323, Session
                              Initiation Protocol (SIP), and Media Gateway Control Protocol (MGCP) 0.1

- Cable detection

- Overload protection

### Analog Phone Connectivity

Cisco 450 Voice Gateway are ideal for analog phone deployments ranging from centralized to sparsely concentrated or distributed
                              topologies. Cisco 4000 Series Integrated Services Routers offer many supplementary analog calling features, depending on the
                              call control and signaling type used. All supplementary analog features are supported through the FXS and FXO service modules.
                              The analog interface on Cisco 4000 Series also supports Feature Access Codes (FACs) for invoking supplementary services.

### Fax and Modem Connectivity

FXS ports on Cisco 450 Voice Gateway support fax machines and modems. When using fax machines, the gateways support T.38 fax
                              relay and fax pass-through. T.38 fax relay technologies allow transfer of faxes across the network with high reliability using
                              less bandwidth than a voice call. All modems can be connected to the Cisco VG Series Gateways and are transferred over the
                              network using modem pass-through.

### Protocols Supported

The voice gateways support the following protocols:

- SCCP

- H.323v4

- MGCP

- SIP

- Real-Time Transport Protocol (RTP)

- Secure Real-Time Transport Protocol (SRTP)

- Trivial File Transfer Protocol (TFTP)

- HTTP server

- Simple Network Management Protocol (SNMP)

- Telnet

- Dynamic Host Configuration Protocol (DHCP)

- DNS

- Cisco Unified Communications Manager or Cisco Unified Communications Manager Express redundancy support using Hot Standby
                                 Router Protocol (HSRP)

- Call survivability: MGCP failover to an H.323 connection to the Survivable Remote Site Telephony (SRST) router

- T.38 fax relay and modem pass-through

- Codec support: G.711, G.729. G.729a will be used if the gateway does not support G729 annex b

- RADIUS and TACACS+ for Telnet and authorization

The following table lists the feature specifications for Cisco 450 Voice Gateway.

Feature

SM-X-8FXS/12FXO

SM-X-16FXS/2FXO

SM-X-24FXS/4FXO

SM-X-72FXS

Tip and Ring Interface for each FXS port

Interface

FXS/FXO (RJ-21)RJ-21 ports 0 to 7: FXSRJ-21 ports 8 to 19: FXO

FXS/FXO (RJ-21)RJ-21 ports 0 to 15: FXSRJ-21 ports 16 and 17: FXO

FXS (RJ-21), FXO (RJ-11)RJ-21 ports 0 to 23: FXSRJ-11 ports 24 to 27: FXO

FXS (RJ-21)

Address signaling format

In-band DTMF Out-of-band pulse (8 to 12 pps)

In-band DTMF Out-of-band pulse (8 to 12 pps)

In-band DTMF Out-of-band pulse (8 to 12 pps)

In-band DTMF Out-of-band pulse (8 to 12 pps)

FXS signaling formats

FXS loop-start, ground-start, and DID signaling

FXS loop-start, ground-start, and DID signaling

FXS loop-start, ground-start, and DID signaling

FXS loop-start, ground-start, and DID signaling

## Cisco VG450 Voice Gateway Chassis

The following figures show the front and back panels of the Cisco VG450 Voice Gateway Chassis:

## Slot, Bay, and Ports

The FXO port is used to connect to PBX or key systems, or to provide off-premises connections to the PSTN. It supports battery
                           reversal detection and caller ID. The FXO port is also used to connect to analog Centralized Automatic Message Accounting
                           (CAMA) trunks to provide dedicated E-911 service (only in North America).

The FXS port is used to connect analog phones, modems, fax machines, and speaker phones to an enterprise IP voice system,
                           and to use them as extensions to your Cisco or third-party IP call-control system. Having these devices tightly integrated
                           with the IP-based phone system is advantageous for increased manageability, scalability, and cost-effectiveness. The Direct
                           Inward Dialing (DID) port is used to provide off-premises DID connection from the central office. It serves only incoming
                           calls from the PSTN. The Caller ID feature is not supported in DID mode.

Cisco 450 Voice Gateway supports the following:

- NIM-1MFT-T1/E1

- NIM-2MFT-T1/E1

- NIM-4MFT-T1/E1

- NIM-8MFT-T1/E1

- NIM-2FXO

- NIM-4FXO

- NIM-4EM

- NIM-2BRI-NT/TE

- NIM-4BRI-NT/TE

- NIM-2FXSP

- NIM-4FXSP

- NIM-2FXS/4FXOP

- SM-X-8FXS/12FXO

- SM-X-16FXS/2FXO

- SM-X-24FXS/4FXO

- SM-X-72FXS

- SM-X-72FXS

- No Skye SM is supported.

- No DSP Farm is supported

- No CUBE and CME are supported

- Old D3 analog FXS and combo FXS/FXO NIMs are not supported.

- T1/E1: channel-group CLI is not supported

- CME: telephone service CLI is not supported.

The following table provides information about Cisco 450 Voice Gateway SKU:

Interface

Maximum Number of FXS-E Ports

Maximum Number or RENs

LED

Number of Failed-over Ports

SM-X-8-FXS/12FXO

8

16

EN LED (Amber/Green)

ACT LED (Green)

8 ports on RJ-21

SM-X-16-FXS/2FXO

16

16

EN LED (Amber/Green)

ACT LED (Green)

2 ports on RJ-21

SM-X-24-FXS/4FXO

16

16

EN LED (Amber/Green)

ACT LED (Green)

4 ports on RJ-11

SM-X-72FXS

- 16 for 72FXS mode

- 56 for 56FXS-E mode

- 40

- 30

EN LED (Amber/Green)

ACT LED (Green)

—

The slot, bay, and port information for Cisco 450 Voice Gateway FXS module is as follows:

Interface

Slot

Bay

Port

SM-X-8-FXS/12FXO

1-2

0

0-7

SM-X-16-FXS/2FXO

1-2

0

0-15

SM-X-24-FXS/4FXO

1-2

0

0-23

SM-X-72FXS

1 and 3

0

- 0-71

- 0-55

The slot, bay, and port information for Cisco 450 Voice Gateway FXO module is as follows:

Interface

Slot

Bay

Port

SM-X-8-FXS/12FXO

1-2

0

8-19

SM-X-16-FXS/2FXO

1-2

0

16-17

SM-X-24-FXS/4FXO

1-2

0

24-27

## Technical Specifications

Description

SM-X-8FXS/12FXO

SM-X-16FXS/2FXO

SM-X-24FXS/4FXO

SM-X-72FXS

Physical

Dimensions (H x W x D)

1.58 x 7.44 x 7.6 inches

1.58 x 7.44 x 7.6 inches

1.58 x 7.44 x 7.6 inches

1.58 x 15.57 x 7.57 inches

Weight

1.90 lb (0.86 kg)

1.98 lb (0.90 kg)

2.12 lb (0.96 kg)

4.94 lb (2.24 kg)

Power

AC power

53.55W

70.32W

79.37W

128.16W

Current

4.46A on 12V

5.86A on 12V

6.61A on 12V

10.68A on 12V

Voltage

12V from backplane

12V from backplane

12V from backplane

12V from backplane

On-hook voltage

-44V

-44V

-44V

-44V

Off-hook loop current

25 mA (maximum) for short loop-length-port35 mA for long loop-length-port

25 mA (maximum) for short loop-length-port35 mA for long loop-length-port

25 mA (maximum) for short loop-length-port35 mA for long loop-length-port

25 mA (maximum) for short loop-length-port35 mA for long loop-length-port

Operating temperature

32
                                       o
                                       to 104
                                       o
                                       F (0
                                       o
                                       to 40
                                       o
                                       C)

32
                                       o
                                       to 104
                                       o
                                       F (0
                                       o
                                       to 40
                                       o
                                       C)

32
                                       o
                                       to 104
                                       o
                                       F (0
                                       o
                                       to 40
                                       o
                                       C)

32
                                       o
                                       to 104
                                       o
                                       F (0
                                       o
                                       to 40
                                       o
                                       C)

Nonoperating temperature

-40
                                       o
                                       to 158
                                       o
                                       F (-40
                                       o
                                       to 70
                                       o
                                       C)

-40
                                       o
                                       to 158
                                       o
                                       F (-40
                                       o
                                       to 70
                                       o
                                       C)

-40
                                       o
                                       to 158
                                       o
                                       F (-40
                                       o
                                       to 70
                                       o
                                       C)

-40
                                       o
                                       to 158
                                       o
                                       F (-40
                                       o
                                       to 70
                                       o
                                       C)

FXS loop resistance

Up to 600 ohms for short loop-length-portUp to 1400 ohms for long loop-length-port

Up to 600 ohms for short loop-length-portUp to 1400 ohms for long loop-length-port

Up to 600 ohms for short loop-length-portUp to 1400 ohms for long loop-length-port

Up to 600 ohms for short loop-length-portUp to 1400 ohms for long loop-length-port

DID loop resistance

Up to 1400 ohms

Up to 1400 ohms

Up to 1400 ohms

Up to 1400 ohms

Ring frequency

20, 25, 30, and 50 Hz

20, 25, 30, and 50 Hz

20, 25, 30, and 50 Hz

20, 25, 30, and 50 Hz

REN loading

5 RENs per port (short-loop-length port)2 RENs per port (long-loop-length port)

5 RENs per port (short-loop-length port)2 RENs per port (long-loop-length port)

5 RENs per port (short-loop-length port)2 RENs per port (long-loop-length port)

5 RENs per port (short-loop-length port)2 RENs per port (long-loop-length port)

Impedance

600c, 600r, 900c, 900r, complex1, complex2, complex3, complex4, complex5, and complex6

600c, 600r, 900c, 900r, complex1, complex2, complex3, complex4, complex5, and complex6

600c, 600r, 900c, 900r, complex1, complex2, complex3, complex4, complex5, and complex6

600c, 600r, 900c, 900r, complex1, complex2, complex3, complex4, complex5, and complex6

FXS loop length

Short-loop-length port: 3000 ft (900 m) with 26 AWG, 5500 ft (1700 m) with 24 AWGLong-loop-length port: 11,000 ft (3400 m)
                                       with 26 AWG, 18,000 ft (5500 m) with 24 AWG

Short-loop-length port: 3000 ft (900 m) with 26 AWG, 5500 ft (1700 m) with 24 AWGLong-loop-length port: 11,000 ft (3400 m)
                                       with 26 AWG, 18,000 ft (5500 m) with 24 AWG

Short-loop-length port: 3000 ft (900 m) with 26 AWG, 5500 ft (1700 m) with 24 AWGLong-loop-length port: 11,000 ft (3400 m)
                                       with 26 AWG, 18,000 ft (5500 m) with 24 AWG

Short-loop-length port: 3000 ft (900 m) with 26 AWG, 5500 ft (1700 m) with 24 AWGLong-loop-length port: 11,000 ft (3400 m)
                                       with 26 AWG, 18,000 ft (5500 m) with 24 AWG

Cables

Category 3 and Category 5

Category 3 and Category 5

Category 3 and Category 5

Category 3 and Category 5

## Platform and Software Requirements

Cisco 450 Voice Gateway is supported on Cisco 4461 Integrated Services Router effective with Cisco IOS XE Fuji 16.9.1 or later.
                           The service modules provide gateway services for Cisco Unified Communications using Cisco Unified Communications Manager with
                           SRST or Cisco Unified Communications Manager Express. The following table provides information about the software version
                           that is compatible with FXO and FXS service modules.

Product Category

Software Version

Cisco IOS XE Software

Cisco IOS XE Fuji 16.9.1

Cisco Unified Communications Manager

10.5.2(SU8), 11.5.1(SU6) and 12.5

Cisco Unified Communications Manager Express

Any version that is compatible with Cisco IOS XE Fuji 16.7.1

Third-party Call Control

IP-based trunk; SIP and H.323

### Configuration Methods

After the Cisco VG450 Voice Gateway is operational, use the procedures described in the Cisco Voice 450 Gateway Software Configuration Guide to configure specific services and functions, or to make changes to an existing configuration.

You can configure the Cisco VG450 Voice Gateway by one of the following methods:

System configuration dialog

Configuration mode: Cisco IOS software CLI

Setup command facility: Remote configuration through a LAN

SNMP-based application: CiscoView or HP OpenView

HTTP-based configuration server: Provides access to the CLI from a web browser

| Note | Switching between the modes requires reload of the ISR chassis. |
|---|---|

| Feature | SM-X-8FXS/12FXO | SM-X-16FXS/2FXO | SM-X-24FXS/4FXO | SM-X-72FXS |
|---|---|---|---|---|
| Tip and Ring Interface for each FXS port |
| Interface | FXS/FXO (RJ-21)RJ-21 ports 0 to 7: FXSRJ-21 ports 8 to 19: FXO | FXS/FXO (RJ-21)RJ-21 ports 0 to 15: FXSRJ-21 ports 16 and 17: FXO | FXS (RJ-21), FXO (RJ-11)RJ-21 ports 0 to 23: FXSRJ-11 ports 24 to 27: FXO | FXS (RJ-21) |
| Address signaling format | In-band DTMF Out-of-band pulse (8 to 12 pps) | In-band DTMF Out-of-band pulse (8 to 12 pps) | In-band DTMF Out-of-band pulse (8 to 12 pps) | In-band DTMF Out-of-band pulse (8 to 12 pps) |
| FXS signaling formats | FXS loop-start, ground-start, and DID signaling | FXS loop-start, ground-start, and DID signaling | FXS loop-start, ground-start, and DID signaling | FXS loop-start, ground-start, and DID signaling |

| Interface | Maximum Number of FXS-E Ports | Maximum Number or RENs | LED | Number of Failed-over Ports |
|---|---|---|---|---|
| SM-X-8-FXS/12FXO | 8 | 16 | EN LED (Amber/Green) ACT LED (Green) | 8 ports on RJ-21 |
| SM-X-16-FXS/2FXO | 16 | 16 | EN LED (Amber/Green) ACT LED (Green) | 2 ports on RJ-21 |
| SM-X-24-FXS/4FXO | 16 | 16 | EN LED (Amber/Green) ACT LED (Green) | 4 ports on RJ-11 |
| SM-X-72FXS | 16 for 72FXS mode 56 for 56FXS-E mode | 40 30 | EN LED (Amber/Green) ACT LED (Green) | — |

| Interface | Slot | Bay | Port |
|---|---|---|---|
| SM-X-8-FXS/12FXO | 1-2 | 0 | 0-7 |
| SM-X-16-FXS/2FXO | 1-2 | 0 | 0-15 |
| SM-X-24-FXS/4FXO | 1-2 | 0 | 0-23 |
| SM-X-72FXS | 1 and 3 | 0 | 0-71 0-55 |

| Interface | Slot | Bay | Port |
|---|---|---|---|
| SM-X-8-FXS/12FXO | 1-2 | 0 | 8-19 |
| SM-X-16-FXS/2FXO | 1-2 | 0 | 16-17 |
| SM-X-24-FXS/4FXO | 1-2 | 0 | 24-27 |

| Description | SM-X-8FXS/12FXO | SM-X-16FXS/2FXO | SM-X-24FXS/4FXO | SM-X-72FXS |
|---|---|---|---|---|
| Physical |
| Dimensions (H x W x D) | 1.58 x 7.44 x 7.6 inches | 1.58 x 7.44 x 7.6 inches | 1.58 x 7.44 x 7.6 inches | 1.58 x 15.57 x 7.57 inches |
| Weight | 1.90 lb (0.86 kg) | 1.98 lb (0.90 kg) | 2.12 lb (0.96 kg) | 4.94 lb (2.24 kg) |
| Power |
| AC power | 53.55W | 70.32W | 79.37W | 128.16W |
| Current | 4.46A on 12V | 5.86A on 12V | 6.61A on 12V | 10.68A on 12V |
| Voltage | 12V from backplane | 12V from backplane | 12V from backplane | 12V from backplane |
| On-hook voltage | -44V | -44V | -44V | -44V |
| Off-hook loop current | 25 mA (maximum) for short loop-length-port35 mA for long loop-length-port | 25 mA (maximum) for short loop-length-port35 mA for long loop-length-port | 25 mA (maximum) for short loop-length-port35 mA for long loop-length-port | 25 mA (maximum) for short loop-length-port35 mA for long loop-length-port |
| Operating temperature | 32
                                       o
                                       to 104
                                       o
                                       F (0
                                       o
                                       to 40
                                       o
                                       C) | 32
                                       o
                                       to 104
                                       o
                                       F (0
                                       o
                                       to 40
                                       o
                                       C) | 32
                                       o
                                       to 104
                                       o
                                       F (0
                                       o
                                       to 40
                                       o
                                       C) | 32
                                       o
                                       to 104
                                       o
                                       F (0
                                       o
                                       to 40
                                       o
                                       C) |
| Nonoperating temperature | -40
                                       o
                                       to 158
                                       o
                                       F (-40
                                       o
                                       to 70
                                       o
                                       C) | -40
                                       o
                                       to 158
                                       o
                                       F (-40
                                       o
                                       to 70
                                       o
                                       C) | -40
                                       o
                                       to 158
                                       o
                                       F (-40
                                       o
                                       to 70
                                       o
                                       C) | -40
                                       o
                                       to 158
                                       o
                                       F (-40
                                       o
                                       to 70
                                       o
                                       C) |
| FXS loop resistance | Up to 600 ohms for short loop-length-portUp to 1400 ohms for long loop-length-port | Up to 600 ohms for short loop-length-portUp to 1400 ohms for long loop-length-port | Up to 600 ohms for short loop-length-portUp to 1400 ohms for long loop-length-port | Up to 600 ohms for short loop-length-portUp to 1400 ohms for long loop-length-port |
| DID loop resistance | Up to 1400 ohms | Up to 1400 ohms | Up to 1400 ohms | Up to 1400 ohms |
| Ring frequency | 20, 25, 30, and 50 Hz | 20, 25, 30, and 50 Hz | 20, 25, 30, and 50 Hz | 20, 25, 30, and 50 Hz |
| REN loading | 5 RENs per port (short-loop-length port)2 RENs per port (long-loop-length port) | 5 RENs per port (short-loop-length port)2 RENs per port (long-loop-length port) | 5 RENs per port (short-loop-length port)2 RENs per port (long-loop-length port) | 5 RENs per port (short-loop-length port)2 RENs per port (long-loop-length port) |
| Impedance | 600c, 600r, 900c, 900r, complex1, complex2, complex3, complex4, complex5, and complex6 | 600c, 600r, 900c, 900r, complex1, complex2, complex3, complex4, complex5, and complex6 | 600c, 600r, 900c, 900r, complex1, complex2, complex3, complex4, complex5, and complex6 | 600c, 600r, 900c, 900r, complex1, complex2, complex3, complex4, complex5, and complex6 |
| FXS loop length | Short-loop-length port: 3000 ft (900 m) with 26 AWG, 5500 ft (1700 m) with 24 AWGLong-loop-length port: 11,000 ft (3400 m)
                                       with 26 AWG, 18,000 ft (5500 m) with 24 AWG | Short-loop-length port: 3000 ft (900 m) with 26 AWG, 5500 ft (1700 m) with 24 AWGLong-loop-length port: 11,000 ft (3400 m)
                                       with 26 AWG, 18,000 ft (5500 m) with 24 AWG | Short-loop-length port: 3000 ft (900 m) with 26 AWG, 5500 ft (1700 m) with 24 AWGLong-loop-length port: 11,000 ft (3400 m)
                                       with 26 AWG, 18,000 ft (5500 m) with 24 AWG | Short-loop-length port: 3000 ft (900 m) with 26 AWG, 5500 ft (1700 m) with 24 AWGLong-loop-length port: 11,000 ft (3400 m)
                                       with 26 AWG, 18,000 ft (5500 m) with 24 AWG |
| Cables | Category 3 and Category 5 | Category 3 and Category 5 | Category 3 and Category 5 | Category 3 and Category 5 |

| Product Category | Software Version |
|---|---|
| Cisco IOS XE Software | Cisco IOS XE Fuji 16.9.1 |
| Cisco Unified Communications Manager | 10.5.2(SU8), 11.5.1(SU6) and 12.5 |
| Cisco Unified Communications Manager Express | Any version that is compatible with Cisco IOS XE Fuji 16.7.1 |
| Third-party Call Control | IP-based trunk; SIP and H.323 |