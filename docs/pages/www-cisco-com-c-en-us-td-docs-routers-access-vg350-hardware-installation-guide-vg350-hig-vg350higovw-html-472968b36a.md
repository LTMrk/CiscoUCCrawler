---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg350-hardware-installation-guide-vg350-hig-vg350higovw-html-472968b36a
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg350/hardware/installation/guide/vg350_hig/vg350higovw.html
retrieved_at: 2026-08-21T12:51:20.647686+00:00
---

Cisco VG350 Voice Gateway Hardware Installation Guide

# Cisco VG350 Voice Gateway Hardware Installation Guide

Updated: March 27, 2014

Chapter: Overview of the Cisco VG350 Voice Gateway

## Chapter: Overview of the Cisco VG350 Voice Gateway

This chapter provides a brief description of the Cisco VG350 Voice Gateway (VG) and contains the following sections:

## Overview

The Cisco VG350 service module is a high-density analog voice gateway. It is an intermediate path that enables TDM to IP transition.

The Cisco VG350 Voice Gateway supports the following interfaces:

- Gigabit Ethernet (GE)

- USB

- High-Speed WAN Interface Card (HWIC) and Voice/WAN Interface Card (VWIC)

- Double-Wide Service Module (DWSM) interface

Warning	This unit is intended for installation in restricted access areas. A restricted access area can be accessed only through the use of a special tool, lock and key, or other means by security. Statement 1017

## VG350 Voice Gateway Chassis

The following figures show the front and back panels of the VG350 Voice Gateway Chassis:

- Figure 1-1 shows the Front Panel.

- Figure 1-2 shows the Back Panel.

Figure 1-1 Front Panel of the VG350 Voice Gateway

1

AC OK 1

3

ACT status LED

2

SYS status LED

4

PS1 (Right), PS2 (Left)

1. LED goes off if the AC power fails or is disconnected.  It does not go on and off with the power switch.

Figure 1-2 Back Panel of the VG350 Voice Gateway

1

USB serial console port

6

USB0 and USB1 (1, Top)

2

RJ-45 serial console port

7

Ground

3

SFP1 and SFP2 (2, Top)

8

CompactFlash 0 and 1 (0, Far right)

4

10/100/1000 Ethernet ports GE 0/1 and GE 0/2 (GE 0/2,Top)

9

SM-D-72FXS Service Module

5

10/100/1000 Ethernet port GE 0/0

10

SM-D-48FXS-E Service Module

### Configuration Options

The following configuration options are available for Cisco VG350 Voice Gateway:

Table 1-1	Configuration Options Possible with Cisco VG350 Voice Gateway with the Double-Wide High Density Analog Service Module (DWSM)

Configuration

VG350

SM 1

SM 2

Total number of ports

1

SM-D-72FXS

SM-D-72FXS

144

2

SM-D-72FXS

SM-D-48FXS-E

120

4

SM-D-48FXS-E

SM-D-48FXS-E

96

## Interfaces and Service Capabilities

Table 1-2 lists the built-in interface ports for the Cisco VG350.

Table 1-2 Built-in Interfaces for the Cisco VG350

Data Ports

Management Ports

10/100/1000 GE RJ-45

10/100/1000 SFP

USB Type A

Console Serial, RJ-45

Console Serial, Mini-USB (Type B)

Auxiliary,

RJ-45

Cisco VG350 Voice Gateway

3 2

2

2

1

1

1

2. One RJ-45 with two GE SFPs or three RJ-45 GEs.

## Physical Description and LEDs

### LED Indicators

Table 1-3 describes the LED indicators for the Cisco VG350.

Table 1-3 LED Indicators for Cisco VG350

LED

Color

Description

Location on the VG350

PS/PS1

Green

System is running.

Front bezel

Amber

System is not running.

PS2

Green

System is running.

Front bezel

Amber

System is not running.

AC OK

Green

AC power connected.

Front bezel

Off

No AC power connected

RPS

Green

System is running on external RPS power supply.

—

SYS

Solid green

Solid green indicates normal operation.

Front bezel

Blinking green

System is booting or is in ROM monitor mode.

Amber

System error.

Off

Power is off or system board is faulty.

ACT

Solid or blinking green

Solid or blinking indicates packet activity between the forwarding and routing engine and any I/O port.

Front bezel

Off

No packet transfers are occurring.

RJ-45 CON

Green

Serial console is active.

Back panel

USB CON

Green

USB console is active.

Back panel

GE: Link

Green

Solid green indicates the Ethernet port has a link partner.

Back panel

SFP S

Blinking green

Blinking frequency indicates port speed. See the definition for the S LED.

Back panel

SFP EN

Off

Not present.

Back panel

Green

Present and enabled.

Amber

Present with failure.

CF0/CF1

Green

Flash memory is being accessed; do not eject the CompactFlash memory card.

Back panel

Amber

CompactFlash error.

Off

Flash memory is not being accessed; okay to eject the CompactFlash memory card.

Off

No FE or GE link is established.

PVDM 0,1,2, and 3

Green

PVDM is initialized.

Back panel

Amber

PVDM is detected but not initialized.

Off

No PVDM installed.

### Specifications

Table 1-4 details the technical specifications of the Cisco VG350 Voice Gateway.

Table 1-4 Cisco VG350 Voice Gateway Technical Specifications

Description

Specification

Physical

Dimensions (H x W x D)

5.22 x 17.25 x 18.75 in. (88.9 x 438.2 x 476.2 mm), 3 RU height

Weight with AC PS

(without modules)

39 lbs (17.69 kg)

Weight with AC PS

(without modules)

40 lbs (18.14 kg)

Weight (fully configured)

60 lbs (27.21 kg)

Power

AC input power

•	Input voltage

•	Frequency

•	Input current

•	Input current with AC

•	Surge current

100 to 240 VAC, autoranging

47 to 63 Hz

0.4 to 3.5 A (configuration dependent)

0.4 to 7.0 A (configuration dependent)

30 A maximum at 115 VAC 60 Hz

60 A maximum at 230 VAC 50 Hz

Power consumption

85 to 400 W, 600 to 1370 BTU/hr (configuration dependent)

With AC

85 to 800 W, 600 to 2740 BTU/hr (configuration dependent)

Ports

Console port

One RJ-45 connector and one mini USB Type B, USB 2.0 compliant

Auxiliary port

RJ-45 connector

USB ports

Two USB Type A, USB 2.0 compliant, 2.5 W (500 mA) maximum 3

10/100/1000 Gigabit Ethernet

Three RJ-45 connectors (GE 0/0, GE 0/1, GE 0/2) auto-MDIX2

SFP

Two RJ-45 connectors support SFP modules. When an SFP module is installed, the adjacent RJ-45 GE connector is disabled.

Environmental

Operating humidity

5 to 85%, noncondensing

Operating humidity

(short-term per NEBS)

5% to 90%, but not to exceed 0.024 kg water/kg of dry air

Operating temperature up to 5906 ft (1800 m) elevation

32 to 104°F (0 to 40°C)

Operating temperature up to 9843 ft (3000 m) elevation

32 to 104°F (0 to 40°C)

Operating temperature up to

13,123 ft (4000 m) elevation

32 to 86°F (0 to 30°C)

Temperature

(short-term per NEBS/1800m max altitude)

23 to 122°F (–5°C to 50°C)

Operating altitude maximum

13,123 ft (4000 m)

Note For China, the unit cannot operate above 2000 m.  The internal AC power supplies do not meet the new Chinese Safety requirements for products that operate in the 2001-5000 m range.

Transportation and Storage

Non-operating temperature

–40 to 158°F (–40 to 70°C)

Non-operating humidity

5 to 95% RH

Non-operating altitude

15,000 ft (4570 m)

Acoustic

Acoustic: Sound Pressure

(Typical/Maximum)

57.6 to 77.6 dBA

Acoustic: Sound Power

(Typical/Maximum)

67.8 to 84.7 dBA

Compliance

Safety compliance

•	IEC 60950-1, Safety of information technology equipment

•	EN 60950-1, Safety of information technology equipment

•	UL 60950-1, Standard for safety for information technology

equipment [US]

•	CAN/CSA C22.2 No. 60950-1, Safety of information technology

equipment including electrical business equipment [Canada]

•	AS/NZS 60950.1 2003

•	IEC60950, 3rd edition [PRC]

•	IEC60950, 2nd Edition [Mexico]

Immunity compliance

•	CISPR24 ITE-Immunity characteristics, Limits and methods of measurement

•	EN 55024 ITE-Immunity characteristics, Limits and methods ofmeasurement

•	EN 50082-1 Electromagnetic compatibility - Generic immunity standard - Part 1

•	EN 300-386 Electromagnetic compatibility for TNESD/EMI

•	EN 61000-6-1

•	SD/EMI

EMC compliance

•	EN 55022, Class A

•	CISPR22, Class A

•	CFR47, Part 15, Subpart B, Class A

•	EN300386, Class A

•	AS/NZS CISPR22, Class A

•	VCCI, Class A

•	SD/EMI, Class A

•	Harmonic Current Emission

– EN 61000-3-2 for EUT Power requirements <16A

– EN 61000-3-12 for EUT Power requirements >16A

- Voltage Fluctuation and Flicker

– EN 61000-3-3 for EUT Power requirements <16

– EN 61000-3-11 for EUT Power requirements >16A

3. 480 Mb/s individually, bandwidth is shared when both are used.

Warning	Ultimate disposal of this product should be handled according to all national laws and regulations. Statement 1040

## Software Elements

The operating system for the Cisco VG350 Voice Gateway is the Cisco IOS software that resides in flash memory.

### Configuration Connections

You can use an ASCII terminal or a PC to configure a Cisco VG350 Voice Gateway. The configuration can be performed in several ways:

- Locally, with a direct connection through the console port

- Remotely, with a connection through the auxiliary port and a modem

- Through Telnet and TFTP

Configuration Methods

### Configuration Methods

### Automated Configuration

If your Cisco VG350 Voice Gateway was ordered with the Simple Network-Enabled Auto-Provision ( SNAP) option, no onsite configuration is required. When the Cisco VG350 Voice Gateway is powered on and connected, the SNAP application downloads the applicable configuration files automatically.

### Manual Configuration

When a Cisco VG350 Voice Gateway is first installed, use the procedure in the “Power-On Procedure” section for the initial configuration. This sets the basic communication parameters.

After the Cisco VG350 Voice Gateway is operating and able to communicate, use the procedures in Cisco VG350 Voice Gateway Software Configuration Guide to configure the specific services and functions or to make changes to the existing configuration.

There are multiple methods for configuring a Cisco VG350 Voice Gateway:

- System configuration dialog

- Configuration mode—Cisco IOS software CLI

- setup command facility—Remote configuration through a LAN

- SNMP-based application—CiscoView or HP OpenView

- HTTP-based configuration server—Provides access to the CLI from a web browser

| 1 | AC OK 1 | 3 | ACT status LED |
|---|---|---|---|
| 2 | SYS status LED | 4 | PS1 (Right), PS2 (Left) |

| 1. LED goes off if the AC power fails or is disconnected.  It does not go on and off with the power switch. |
|---|

| 1 | USB serial console port | 6 | USB0 and USB1 (1, Top) |
|---|---|---|---|
| 2 | RJ-45 serial console port | 7 | Ground |
| 3 | SFP1 and SFP2 (2, Top) | 8 | CompactFlash 0 and 1 (0, Far right) |
| 4 | 10/100/1000 Ethernet ports GE 0/1 and GE 0/2 (GE 0/2,Top) | 9 | SM-D-72FXS Service Module |
| 5 | 10/100/1000 Ethernet port GE 0/0 | 10 | SM-D-48FXS-E Service Module |

| Configuration | VG350 |
|---|---|
| SM 1 | SM 2 | Total number of ports |
| 1 | SM-D-72FXS | SM-D-72FXS | 144 |
| 2 | SM-D-72FXS | SM-D-48FXS-E | 120 |
| 4 | SM-D-48FXS-E | SM-D-48FXS-E | 96 |

|  | Data Ports | Management Ports |
|---|---|---|
|  | 10/100/1000 GE RJ-45 | 10/100/1000 SFP | USB Type A | Console Serial, RJ-45 | Console Serial, Mini-USB (Type B) | Auxiliary, RJ-45 |
| Cisco VG350 Voice Gateway | 3 2 | 2 | 2 | 1 | 1 | 1 |

| 2. One RJ-45 with two GE SFPs or three RJ-45 GEs. |
|---|

| LED | Color | Description | Location on the VG350 |
|---|---|---|---|
| PS/PS1 | Green | System is running. | Front bezel |
| Amber | System is not running. |
| PS2 | Green | System is running. | Front bezel |
| Amber | System is not running. |
| AC OK | Green | AC power connected. | Front bezel |
| Off | No AC power connected |
| RPS | Green | System is running on external RPS power supply. | — |
| SYS | Solid green | Solid green indicates normal operation. | Front bezel |
| Blinking green | System is booting or is in ROM monitor mode. |
| Amber | System error. |
| Off | Power is off or system board is faulty. |
| ACT | Solid or blinking green | Solid or blinking indicates packet activity between the forwarding and routing engine and any I/O port. | Front bezel |
| Off | No packet transfers are occurring. |
| RJ-45 CON | Green | Serial console is active. | Back panel |
| USB CON | Green | USB console is active. | Back panel |
| GE: Link | Green | Solid green indicates the Ethernet port has a link partner. | Back panel |
| SFP S | Blinking green | Blinking frequency indicates port speed. See the definition for the S LED. | Back panel |
| SFP EN | Off | Not present. | Back panel |
| Green | Present and enabled. |
| Amber | Present with failure. |
| CF0/CF1 | Green | Flash memory is being accessed; do not eject the CompactFlash memory card. | Back panel |
| Amber | CompactFlash error. |
| Off | Flash memory is not being accessed; okay to eject the CompactFlash memory card. |
|  | Off | No FE or GE link is established. |  |
| PVDM 0,1,2, and 3 | Green | PVDM is initialized. | Back panel |
| Amber | PVDM is detected but not initialized. |
| Off | No PVDM installed. |

| Description | Specification |
|---|---|
| Physical |
| Dimensions (H x W x D) | 5.22 x 17.25 x 18.75 in. (88.9 x 438.2 x 476.2 mm), 3 RU height |
| Weight with AC PS (without modules) | 39 lbs (17.69 kg) |
| Weight with AC PS (without modules) | 40 lbs (18.14 kg) |
| Weight (fully configured) | 60 lbs (27.21 kg) |
| Power |
| AC input power |
| •	Input voltage •	Frequency •	Input current •	Input current with AC •	Surge current | 100 to 240 VAC, autoranging |
| 47 to 63 Hz |
| 0.4 to 3.5 A (configuration dependent) |
| 0.4 to 7.0 A (configuration dependent) |
| 30 A maximum at 115 VAC 60 Hz 60 A maximum at 230 VAC 50 Hz |
| Power consumption | 85 to 400 W, 600 to 1370 BTU/hr (configuration dependent) |
| With AC | 85 to 800 W, 600 to 2740 BTU/hr (configuration dependent) |
| Ports |
| Console port | One RJ-45 connector and one mini USB Type B, USB 2.0 compliant |
| Auxiliary port | RJ-45 connector |
| USB ports | Two USB Type A, USB 2.0 compliant, 2.5 W (500 mA) maximum 3 |
| 10/100/1000 Gigabit Ethernet | Three RJ-45 connectors (GE 0/0, GE 0/1, GE 0/2) auto-MDIX2 |
| SFP | Two RJ-45 connectors support SFP modules. When an SFP module is installed, the adjacent RJ-45 GE connector is disabled. |
| Environmental |
| Operating humidity | 5 to 85%, noncondensing |
| Operating humidity (short-term per NEBS) | 5% to 90%, but not to exceed 0.024 kg water/kg of dry air |
| Operating temperature up to 5906 ft (1800 m) elevation | 32 to 104°F (0 to 40°C) |
| Operating temperature up to 9843 ft (3000 m) elevation | 32 to 104°F (0 to 40°C) |
| Operating temperature up to 13,123 ft (4000 m) elevation | 32 to 86°F (0 to 30°C) |
| Temperature (short-term per NEBS/1800m max altitude) | 23 to 122°F (–5°C to 50°C) |
| Operating altitude maximum | 13,123 ft (4000 m) Note For China, the unit cannot operate above 2000 m.  The internal AC power supplies do not meet the new Chinese Safety requirements for products that operate in the 2001-5000 m range. |
| Transportation and Storage |
| Non-operating temperature | –40 to 158°F (–40 to 70°C) |
| Non-operating humidity | 5 to 95% RH |
| Non-operating altitude | 15,000 ft (4570 m) |
| Acoustic |
| Acoustic: Sound Pressure (Typical/Maximum) | 57.6 to 77.6 dBA |
| Acoustic: Sound Power (Typical/Maximum) | 67.8 to 84.7 dBA |
| Compliance |
| Safety compliance | •	IEC 60950-1, Safety of information technology equipment •	EN 60950-1, Safety of information technology equipment •	UL 60950-1, Standard for safety for information technology equipment [US] •	CAN/CSA C22.2 No. 60950-1, Safety of information technology equipment including electrical business equipment [Canada] •	AS/NZS 60950.1 2003 •	IEC60950, 3rd edition [PRC] •	IEC60950, 2nd Edition [Mexico] |
| Immunity compliance | •	CISPR24 ITE-Immunity characteristics, Limits and methods of measurement •	EN 55024 ITE-Immunity characteristics, Limits and methods ofmeasurement •	EN 50082-1 Electromagnetic compatibility - Generic immunity standard - Part 1 •	EN 300-386 Electromagnetic compatibility for TNESD/EMI •	EN 61000-6-1 •	SD/EMI |
| EMC compliance | •	EN 55022, Class A •	CISPR22, Class A •	CFR47, Part 15, Subpart B, Class A •	EN300386, Class A •	AS/NZS CISPR22, Class A •	VCCI, Class A •	SD/EMI, Class A •	Harmonic Current Emission – EN 61000-3-2 for EUT Power requirements <16A – EN 61000-3-12 for EUT Power requirements >16A Voltage Fluctuation and Flicker – EN 61000-3-3 for EUT Power requirements <16 – EN 61000-3-11 for EUT Power requirements >16A |

| 3. 480 Mb/s individually, bandwidth is shared when both are used. |
|---|