---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-d78f983b07
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_0111.html
retrieved_at: 2026-08-22T01:12:08.377952+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: ATA 191 Specifications

## Chapter: ATA 191 Specifications

# ATA 191 Specifications

## Physical Specifications

Description

Specification

Regulatory compliance

FCC (Part 15 Class B), CE, ICES-003, A-Tick certification, Restriction of Hazardous Substances (RoHS), and UL

Power supply

DC input voltage: 5V DC at 2.0A maximum power consumption: 5W

Switching type (100-240V): Automatic

Power adapter: 100-240V and 50-60 Hz (26-34 VA) input with 1.8m cord

Indicator lights and LEDs

Phone 1, phone 2, network, Problem Report Tool (PRT), and power

Documentation

User Guide (online)

Administration Guide (online)

Regulatory Compliance and Safety Information guide (online)

Dimensions

(W x H x D)

3.98 x 3.98 x 1.10 in. (101 x 101 x 28mm)

Unit weight

5.40 oz (153 g)

## Electrical Specifications

Description

Specification

Power

0.25 to 12W (idle to peak)

DC input voltage

5.0 VDC at 2.0A maximum

Power adapter

Universal AC/DC

~4.05 x 1.93 x 1.31 in. (~10.3 x 4.9 x 3.35 cm)

~4.23 oz (120 g) for the AC-input external power adapter

~4.9 ft (1.5 m) DC cord

6 ft (1.8 m) cord

UL/cUL, CE approved

Class I adapter

## Environmental Specifications

Description

Specification

Operating temperature

32 to 113°F (0 to 45°C)

Nonoperating temperature

–13 to 158°F (–25 to 70°C)

Operating humidity

10% to 90% noncondensing

Storage humidity

10% to 90% noncondensing

## Physical Interfaces

Description

Specification

Ethernet

One RJ-45 connector, IEEE 802.3 100BaseT standard

Analog phone

Two RJ-11 FXS voice ports

Power

5 VDC power connector

## Ringing Characteristics

Description

Specification

Tip/ring interfaces for each RJ-11 FXS port (SLIC)

Ring voltage

70VRMS (typical, balanced ringing only)

Ring frequency

20 Hz

Ring waveform

Trapezoidal with 1.2 to 1.6 crest factor

Ring load

1400 ohm + 40μF

Ringer equivalence number (REN)

Up to 3 REN per RJ-11 FXS port

Loop impedance

Up to 200 ohms (plus 430-ohm maximum phone DC resistance)

On-hook/off-hook characteristics

On-hook voltage (tip/ring)

–47V

Off-hook current

24 mA (nominal)

RJ-11 FXS port terminating impedance option

The ATA 191 provides multiple impedance, such as 600 ohm for American SKU, 900 ohm for European SKU, 220 ohm (820 ohm || 120nF)
                                       for Australian SKU, and so on.

## Software Specifications

Description

Specification

Call progress tones

Configurable for two sets of frequencies and single set of on/off cadence

Dual-tone multifrequency (DTMF)

DTMF tone detection and generation

Fax

Fax pass-through and T.38 fax relay mode.

V34 fax is supported for pass-through mode. Success of fax transmissions up to 33.6 kb/s depends on network conditions, and
                                       fax modem/fax machine tolerance to those conditions. The network must have reasonably low network jitter, network delay, and
                                       packet-loss rate.

The ATA 191 only supports T38 Fax Relay Version 0 (G3).

Line-echo cancellation

Echo canceler for each port

8 ms echo length

Nonlinear echo suppression (ERL > 28 dB for frequency = 300 to 2400 Hz)

Convergence time = 250 ms

ERLE = 10 to 20 dB

Double-talk detection

Out-of-band DTMF

RFC 2833 AVT tones for SIP

Cannot transmit RFC 2833 and in-band signaling, simultaneously.

Configuration

DHCP (RFC 2131)

Web configuration via built-in web server

Basic boot configuration (RFC 1350 TFTP Profiling)

Dial plan configuration

Cisco Discovery Protocol

Quality of Service

Class-of-service (CoS) bit-tagging (802.1P)

Type-of-service (ToS) bit-tagging

Security

Encryption for TFTP configuration files

Voice coder-decoders (codecs)

G.729A, G.729AB

G.711A-law

G.711µ-law

Voice features

Voice activity detection (VAD)

Comfort noise generation (CNG)

Dynamic jitter buffer (adaptive)

Voice-over-IP (VoIP) protocols

SIP (RFC 3261)

## SIP Compliance Reference Information

Information on how the ATA 191 complies with the IETF definition of SIP as described in RFC 2543 is found at the following
                              URL:

http://www.ietf.org/rfc/rfc2543.txt

| Description | Specification |
|---|---|
| Regulatory compliance | FCC (Part 15 Class B), CE, ICES-003, A-Tick certification, Restriction of Hazardous Substances (RoHS), and UL |
| Power supply | DC input voltage: 5V DC at 2.0A maximum power consumption: 5W Switching type (100-240V): Automatic Power adapter: 100-240V and 50-60 Hz (26-34 VA) input with 1.8m cord |
| Indicator lights and LEDs | Phone 1, phone 2, network, Problem Report Tool (PRT), and power |
| Documentation | User Guide (online) Administration Guide (online) Regulatory Compliance and Safety Information guide (online) |
| Dimensions (W x H x D) | 3.98 x 3.98 x 1.10 in. (101 x 101 x 28mm) |
| Unit weight | 5.40 oz (153 g) |

| Description | Specification |
|---|---|
| Power | 0.25 to 12W (idle to peak) |
| DC input voltage | 5.0 VDC at 2.0A maximum |
| Power adapter | Universal AC/DC ~4.05 x 1.93 x 1.31 in. (~10.3 x 4.9 x 3.35 cm) ~4.23 oz (120 g) for the AC-input external power adapter ~4.9 ft (1.5 m) DC cord 6 ft (1.8 m) cord UL/cUL, CE approved Class I adapter |

| Description | Specification |
|---|---|
| Operating temperature | 32 to 113°F (0 to 45°C) |
| Nonoperating temperature | –13 to 158°F (–25 to 70°C) |
| Operating humidity | 10% to 90% noncondensing |
| Storage humidity | 10% to 90% noncondensing |

| Description | Specification |
|---|---|
| Ethernet | One RJ-45 connector, IEEE 802.3 100BaseT standard |
| Analog phone | Two RJ-11 FXS voice ports |
| Power | 5 VDC power connector |

| Description | Specification |
|---|---|
| Tip/ring interfaces for each RJ-11 FXS port (SLIC) |
| Ring voltage | 70VRMS (typical, balanced ringing only) |
| Ring frequency | 20 Hz |
| Ring waveform | Trapezoidal with 1.2 to 1.6 crest factor |
| Ring load | 1400 ohm + 40μF |
| Ringer equivalence number (REN) | Up to 3 REN per RJ-11 FXS port |
| Loop impedance | Up to 200 ohms (plus 430-ohm maximum phone DC resistance) |
| On-hook/off-hook characteristics |
| On-hook voltage (tip/ring) | –47V |
| Off-hook current | 24 mA (nominal) |
| RJ-11 FXS port terminating impedance option | The ATA 191 provides multiple impedance, such as 600 ohm for American SKU, 900 ohm for European SKU, 220 ohm (820 ohm \|\| 120nF)
                                       for Australian SKU, and so on. |

| Description | Specification |
|---|---|
| Call progress tones | Configurable for two sets of frequencies and single set of on/off cadence |
| Dual-tone multifrequency (DTMF) | DTMF tone detection and generation |
| Fax | Fax pass-through and T.38 fax relay mode. V34 fax is supported for pass-through mode. Success of fax transmissions up to 33.6 kb/s depends on network conditions, and
                                       fax modem/fax machine tolerance to those conditions. The network must have reasonably low network jitter, network delay, and
                                       packet-loss rate. The ATA 191 only supports T38 Fax Relay Version 0 (G3). |
| Line-echo cancellation | Echo canceler for each port 8 ms echo length Nonlinear echo suppression (ERL > 28 dB for frequency = 300 to 2400 Hz) Convergence time = 250 ms ERLE = 10 to 20 dB Double-talk detection |
| Out-of-band DTMF | RFC 2833 AVT tones for SIP Note Cannot transmit RFC 2833 and in-band signaling, simultaneously. | Note | Cannot transmit RFC 2833 and in-band signaling, simultaneously. |
| Note | Cannot transmit RFC 2833 and in-band signaling, simultaneously. |
| Configuration | DHCP (RFC 2131) Web configuration via built-in web server Basic boot configuration (RFC 1350 TFTP Profiling) Dial plan configuration Cisco Discovery Protocol |
| Quality of Service | Class-of-service (CoS) bit-tagging (802.1P) Type-of-service (ToS) bit-tagging |
| Security | Encryption for TFTP configuration files |
| Voice coder-decoders (codecs) | G.729A, G.729AB G.711A-law G.711µ-law |
| Voice features | Voice activity detection (VAD) Comfort noise generation (CNG) Dynamic jitter buffer (adaptive) |
| Voice-over-IP (VoIP) protocols | SIP (RFC 3261) |

| Note | Cannot transmit RFC 2833 and in-band signaling, simultaneously. |
|---|---|