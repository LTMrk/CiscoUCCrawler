---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-requirements-guide-unified-cme-platform-protocol-compatibility-matrix--ed25333db4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/requirements/guide/Unified_CME_Platform_Protocol_Compatibility_Matrix.html
retrieved_at: 2026-08-21T09:46:14.852159+00:00
---

Unified CME Platform Protocol Compatibility Matrix

# Unified CME Platform Protocol Compatibility Matrix

### Download Options

# Platform and Protocol Compatibility for Unified CME

First Published : July 30, 2018

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

Last Updated: August 16, 2021

Overview

Conventions

Platform and Protocol Support for Unified CME Features

## Overview

This document provides information on the compatibility of Unified Communications Manager Express (Unified CME) across Cisco router platforms. The feature support information for each platform is based on protocol support (SIP and SCCP). The document is last updated for Unified CME 14.1 (Cisco IOS XE Bengaluru 17.6.1a) Release.

For information on the Cisco IOS XE and Cisco IOS Release mapping with Unified CME and Virtual CME, see Unified CME, Unified SRST, and Cisco IOS Software Version Compatibility Matrix .

For information on feature description for Unified CME and Virtual CME, see Cisco Unified Communications Manager Express System Administrator Guide .

The protocols discussed in this document are:

· Session Initiation Protocol (SIP)

· Skinny Client Control Protocol (SCCP)

· Mixed Deployment (Supports both SIP and SCCP) – If both SIP and SCCP are supported on a platform, the mixed deployment is supported by default.

The platforms discussed in this document are:

· Cisco Integrated Services Router Generation 2 (ISR G2)

· Cisco 4000 Series Integrated Services Routers (ISR G3)

· Cisco Cloud Services Router 1000V Series (CSR 1000V)

· Cisco Catalyst 8000V Edge Software (Catalyst 8000V)

· Cisco 8200 Catalyst Edge Series

· Cisco 8300 Catalyst Edge Series

· Cisco ESR 6300 Embedded Series Router

· Cisco 1100 Integrated Services Router

## Conventions

The following conventions are applicable to the information provided in the Feature Support sections.

Table 1 : Conventions

Convention

Description

Yes

The feature is supported.

—

The feature is not supported.

ISR G2

Cisco Integrated Services Router Generation 2

ISR G3

Cisco 4000 Series Integrated Services Routers

CSR 1000V

Cisco Cloud Services Router 1000V Series

Catalyst 8000V

Cisco Catalyst 8000V Edge Software (Catalyst 8000V)

Catalyst 8200

Cisco 8200 Catalyst Edge Series Platforms

Catalyst 8300

Cisco 8300 Catalyst Edge Series Platforms

Cisco ESR 6300

Cisco ESR 6300 Embedded Series Router

Cisco ISR 1100

Cisco 1100 Integrated Services Router

SIP

Session Initiation Protocol

SCCP

Skinny Client Control Protocol

Unified CME

Cisco Unified Communications Manager Express

Virtual CME (vCME)

Unified CME on Cisco Cloud Services Router 1000V Series and Catalyst 8000V

## Platform and Protocol Support for Unified CME Features

This section provides feature support information specific to Cisco Unified Communications Manager Express (Unified CME). For information on feature specific support for Unified CME across platforms and protocols, see Table 2: Unified CME Feature Support .

Note:

· Unified CME Release 14.1 is available for Cisco 8200 and C8300 Catalyst Edge Series Platforms from Cisco IOS XE Bengaluru 17.6.1a onwards. For more information, see Unified CME Features Roadmap in Cisco Unified Communications Manager Express System Administrator Guide.

· Unified CME Release 14.1 is available for Cisco 1100 Integrated Services Routers from Cisco IOS XE Bengaluru 17.5.1a onwards. For more information, see Unified CME Features Roadmap in Cisco Unified Communications Manager Express System Administrator Guide.

· Unified CME Release 14.1 (Cisco IOS XE Bengaluru 17.4.1a) enhances the existing Smart License feature and supports Cisco Catalyst 8000V Edge Software (Catalyst 8000V) platforms. For more information, see Unified CME Features Roadmap in Cisco Unified Communications Manager Express System Administrator Guide.

· Unified CME Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a) introduces a new password policy and supports SNMP version 3 (SNMPv3) and toll fraud prevention for line side SIP. For more information, see Unified CME Features Roadmap in Cisco Unified Communications Manager Express System Administrator Guide.

· Unified CME 12.6 and later releases do not support the features Web GUI and Computer Telephony Integration (CTI) Computer Supported Telecommunications Applications (CSTA) protocol suite.

Table 2: Unified CME Feature Support

Features

Routers with DSPs

Routers without DSPs

ISR G2

ISR G3

C8200 and C8300

CSR 1000V, Catalyst 8000V, ISR 1100, ESR 6300

SIP

SCCP

SIP

SCCP

SIP

SCCP

SIP

SCCP (VG310, VG320, VG350)

Anonymous Call Block

Yes

—

Yes

—

Yes

—

Yes

—

Auto-Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Auto Register

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Auto Assign

—

Yes

—

Yes

—

Yes

—

Yes

Authenticate Register

Yes

—

Yes

—

Yes

—

Yes

—

Barge

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

cBarge/Merge

Yes

Yes

Yes

Yes

Yes

Yes

—

—

Call Park

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Park Resume

—

—

—

—

—

—

—

—

Pickup

Group Pickup

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Directed Call Pickup

—

Yes

—

Yes

—

Yes

—

Yes

Distinctive Ring for Parked Call Recall

Yes (except 8800 Series IP Phones)

Yes

Yes (except 88XX Series IP Phones)

Yes

Yes (except 8800 Series IP Phones)

Yes

Yes (except 88XX Series IP Phones)

—

Park Monitor

Yes (except 7800 Series IP Phones)

Yes

Yes (except 7800 Series IP Phones)

Yes

Yes (except 7800 Series IP Phones)

Yes

Yes (except 7800 Series IP Phones)

—

Directed Call Park

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Extension Mobility

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Extension Assigner

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Transfer

Alert Transfer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Attended/Consult Transfer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Blind Transfer

—

Yes

—

Yes

—

Yes

—

Yes

Conference

Meet-Me Conference

Yes

Yes

Yes

Yes

Yes

Yes

—

—

Ad-hoc Hardware Conference

Yes

Yes

Yes

Yes

Yes

Yes

—

—

Ad-hoc Software Conference

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Video Conference

—

—

—

—

—

—

—

—

Hold/Resume

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Intercom

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Fast Track

Yes

—

Yes

—

Yes

—

Yes

—

Headset Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Line Label

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

My Phone Apps - View On Phone

Speed Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Personal Speed Dial/Fast Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

BLF Speed Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Voice Hunt Groups

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

After Hours

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Single Number Reach (SNR)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Active Call Park List

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Fast Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

BLF Speed Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Single Number Reach (SNR)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Park Retrieval

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Paging

Multicast (Only with G711ulaw codec)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Unicast (Only with G711ulaw codec)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Shared Line

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes 3

Mixed Shared Line

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes 3

Voice Hunt Group with Shared Line

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Caller ID Display

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Caller ID Blocking

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Feature Access Code (FAC) 1

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer Recall

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voicemail

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Message Waiting Indicator (MWI)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes 4

Video 2

Yes (except 8961)

Yes

Yes

Yes

Yes

Yes

Yes

—

Locale Support

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Reset/Restart Phones via Reset/Restart Command

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Button Layout/Softkey Template

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Directory Services

Local Directory

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Local Speed Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Personal Speed Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Privacy

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

iDivert* (Transfer to other mailboxes is not supported)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Enhanced iDivert

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Do Not Disturb (DND)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

DTMF

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Feature Button/Programmable Line Key (PLK)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Key Expansion Module (KEM)

C-KEM

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

BE-KEM

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

A-KEM (CP-8800-Audio)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

V-KEM (CP-8800-Video)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Bulk Registration Support

Yes

—

Yes

—

Yes

Yes

Yes

—

Upgrading/Downgrading Phone Firmware Versions

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Live Record

—

Yes

—

Yes

Yes

Yes

—

—

Enabling/Disabling KPML

Yes

—

Yes

—

Yes

Yes

Yes

—

Alias Feature

—

—

—

—

—

—

—

—

Call Forward

All

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Busy

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Mailbox

Yes

—

Yes

—

Yes

—

Yes

—

Unregistered

Yes

—

Yes

—

Yes

—

Yes

—

Night-Service

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Max-Length

—

Yes

—

Yes

—

Yes

—

Yes

Call Forward All Softkey on Phone

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Multicast MOH

—

Yes

—

Yes

—

Yes

—

—

Unicast MOH

Yes

Yes

Yes

Yes

Yes

Yes

Yes 5

Yes

Basic Automatic Call Distribution (B-ACD)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Night Service

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Channel Hunt Stop

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Hunt Group/Ephone Hunt Group Statistics

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Translation Profile

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Busy Trigger Per Button

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Conference Blocking

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Transfer Blocking

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

COR

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Class Codec

Yes

—

Yes

—

Yes

—

Yes

—

Audio Codecs

G.722

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

G.711

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

G.729

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

iLBC

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Transcoding

Yes

Yes

Yes

Yes

Yes

Yes

—

—

Multi-VRF (Only supported on ISR G2)

Yes

Yes

—

—

—

—

—

—

SNMP/MIB

—

Yes

—

Yes

—

Yes

—

Yes

Web GUI

Yes

Yes

—

—

—

—

—

—

IOS XE Web GUI

—

—

Yes

—

Yes

—

Yes

—

CTI CSTA

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Speed Dial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Busy Lamp Field (BLF)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Call Waiting

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Forced Authorization Code

—

Yes

—

Yes

—

Yes

—

Yes

HTTP File Server (HFS)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Redial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Speakerphone

Dialing

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Answering

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

System Message

—

Yes

—

Yes

—

Yes

—

—

Whisper Intercom

—

Yes

—

Yes

—

Yes

—

—

Abbreviated Dialing

—

Yes

—

Yes

—

Yes

—

—

After Hours

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

SSH to Phone

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Span to PC

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Web Access to Phone

Yes

Yes

Yes

Yes

Yes

Yes

Yes

—

Callback

—

Yes

—

Yes

—

Yes

—

—

Call Waiting Ring/Tone

—

Yes

—

Yes

—

Yes

—

—

Secondary CME

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Cisco Jabber for MAC (Supported from Cisco IOS XE Gibraltar 16.10.1 Release)

—

—

Yes

—

Yes

—

Yes

—

Cisco Jabber for Windows (Supported from Cisco IOS XE Gibraltar 16.10.1 Release)

—

—

Yes

—

Yes

—

Yes

—

SSL VPN Client

—

Yes

—

—

—

—

—

—

Virtual CME (Only on Cisco CSR1000V Cloud Services Router)

—

—

—

—

—

—

Yes

Yes

Secure CME

— 6

Yes

—

—

—

—

—

—

Secure Lineside

—

Yes

—

—

—

—

—

—

SIP Trunk

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Secure SIP Trunk

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

1 – Limited feature support for FAC in Unified CME

2 – Video is supported only on specific endpoints

3 - No Hold/ Remote Resume Support on Shared Line, Mixed Shared Line

4 – For MWI, see Configuring AMWI and VMWI

5 – MOH Groups is not supported on Virtual CME

6 – Not validated and not supported by Cisco TAC

Obtain Documentation and Submit a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What’s New in Cisco Product Documentation RSS feed. The RSS feeds are a free service.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R)

Cisco Unified Communications Manager Express Phone Feature Support

© 2021 Cisco Systems, Inc. All Rights reserved.

| Convention | Description |
|---|---|
| Yes | The feature is supported. |
| — | The feature is not supported. |
| ISR G2 | Cisco Integrated Services Router Generation 2 |
| ISR G3 | Cisco 4000 Series Integrated Services Routers |
| CSR 1000V | Cisco Cloud Services Router 1000V Series |
| Catalyst 8000V | Cisco Catalyst 8000V Edge Software (Catalyst 8000V) |
| Catalyst 8200 | Cisco 8200 Catalyst Edge Series Platforms |
| Catalyst 8300 | Cisco 8300 Catalyst Edge Series Platforms |
| Cisco ESR 6300 | Cisco ESR 6300 Embedded Series Router |
| Cisco ISR 1100 | Cisco 1100 Integrated Services Router |
| SIP | Session Initiation Protocol |
| SCCP | Skinny Client Control Protocol |
| Unified CME | Cisco Unified Communications Manager Express |
| Virtual CME (vCME) | Unified CME on Cisco Cloud Services Router 1000V Series and Catalyst 8000V |

| Features | Routers with DSPs | Routers without DSPs |
|---|---|---|
| ISR G2 | ISR G3 | C8200 and C8300 | CSR 1000V, Catalyst 8000V, ISR 1100, ESR 6300 |
| SIP | SCCP | SIP | SCCP | SIP | SCCP | SIP | SCCP (VG310, VG320, VG350) |
| Anonymous Call Block | Yes | — | Yes | — | Yes | — | Yes | — |
| Auto-Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Auto Register | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Auto Assign | — | Yes | — | Yes | — | Yes | — | Yes |
| Authenticate Register | Yes | — | Yes | — | Yes | — | Yes | — |
| Barge | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| cBarge/Merge | Yes | Yes | Yes | Yes | Yes | Yes | — | — |
| Call Park | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Park Resume | — | — | — | — | — | — | — | — |
| Pickup | Group Pickup | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Directed Call Pickup | — | Yes | — | Yes | — | Yes | — | Yes |
| Distinctive Ring for Parked Call Recall | Yes (except 8800 Series IP Phones) | Yes | Yes (except 88XX Series IP Phones) | Yes | Yes (except 8800 Series IP Phones) | Yes | Yes (except 88XX Series IP Phones) | — |
| Park Monitor | Yes (except 7800 Series IP Phones) | Yes | Yes (except 7800 Series IP Phones) | Yes | Yes (except 7800 Series IP Phones) | Yes | Yes (except 7800 Series IP Phones) | — |
| Directed Call Park | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Extension Mobility | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Extension Assigner | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transfer | Alert Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Blind Transfer | — | Yes | — | Yes | — | Yes | — | Yes |
| Conference | Meet-Me Conference | Yes | Yes | Yes | Yes | Yes | Yes | — | — |
| Ad-hoc Hardware Conference | Yes | Yes | Yes | Yes | Yes | Yes | — | — |
| Ad-hoc Software Conference | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Video Conference | — | — | — | — | — | — | — | — |
| Hold/Resume | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Intercom | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Fast Track | Yes | — | Yes | — | Yes | — | Yes | — |
| Headset Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Line Label | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| My Phone Apps - View On Phone | Speed Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Personal Speed Dial/Fast Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| BLF Speed Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Voice Hunt Groups | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| After Hours | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Single Number Reach (SNR) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Active Call Park List | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Fast Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| BLF Speed Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Single Number Reach (SNR) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Park Retrieval | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Paging | Multicast (Only with G711ulaw codec) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Unicast (Only with G711ulaw codec) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Shared Line | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes 3 |
| Mixed Shared Line | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes 3 |
| Voice Hunt Group with Shared Line | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Caller ID Display | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Caller ID Blocking | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Feature Access Code (FAC) 1 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer Recall | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voicemail | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes 4 |
| Video 2 | Yes (except 8961) | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Locale Support | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Reset/Restart Phones via Reset/Restart Command | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Button Layout/Softkey Template | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Directory Services | Local Directory | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Local Speed Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Personal Speed Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Privacy | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| iDivert* (Transfer to other mailboxes is not supported) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Enhanced iDivert | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Do Not Disturb (DND) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| DTMF | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Feature Button/Programmable Line Key (PLK) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Key Expansion Module (KEM) | C-KEM | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| BE-KEM | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| A-KEM (CP-8800-Audio) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| V-KEM (CP-8800-Video) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Bulk Registration Support | Yes | — | Yes | — | Yes | Yes | Yes | — |
| Upgrading/Downgrading Phone Firmware Versions | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Live Record | — | Yes | — | Yes | Yes | Yes | — | — |
| Enabling/Disabling KPML | Yes | — | Yes | — | Yes | Yes | Yes | — |
| Alias Feature | — | — | — | — | — | — | — | — |
| Call Forward | All | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Mailbox | Yes | — | Yes | — | Yes | — | Yes | — |
| Unregistered | Yes | — | Yes | — | Yes | — | Yes | — |
| Night-Service | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Max-Length | — | Yes | — | Yes | — | Yes | — | Yes |
| Call Forward All Softkey on Phone | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Multicast MOH | — | Yes | — | Yes | — | Yes | — | — |
| Unicast MOH | Yes | Yes | Yes | Yes | Yes | Yes | Yes 5 | Yes |
| Basic Automatic Call Distribution (B-ACD) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Night Service | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Channel Hunt Stop | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Group/Ephone Hunt Group Statistics | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Translation Profile | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy Trigger Per Button | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Conference Blocking | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transfer Blocking | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| COR | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Class Codec | Yes | — | Yes | — | Yes | — | Yes | — |
| Audio Codecs | G.722 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| G.711 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| iLBC | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transcoding | Yes | Yes | Yes | Yes | Yes | Yes | — | — |
| Multi-VRF (Only supported on ISR G2) | Yes | Yes | — | — | — | — | — | — |
| SNMP/MIB | — | Yes | — | Yes | — | Yes | — | Yes |
| Web GUI | Yes | Yes | — | — | — | — | — | — |
| IOS XE Web GUI | — | — | Yes | — | Yes | — | Yes | — |
| CTI CSTA | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Speed Dial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy Lamp Field (BLF) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Call Waiting | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Forced Authorization Code | — | Yes | — | Yes | — | Yes | — | Yes |
| HTTP File Server (HFS) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Redial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Answering | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| System Message | — | Yes | — | Yes | — | Yes | — | — |
| Whisper Intercom | — | Yes | — | Yes | — | Yes | — | — |
| Abbreviated Dialing | — | Yes | — | Yes | — | Yes | — | — |
| After Hours | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| SSH to Phone | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Span to PC | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Web Access to Phone | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Callback | — | Yes | — | Yes | — | Yes | — | — |
| Call Waiting Ring/Tone | — | Yes | — | Yes | — | Yes | — | — |
| Secondary CME | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Cisco Jabber for MAC (Supported from Cisco IOS XE Gibraltar 16.10.1 Release) | — | — | Yes | — | Yes | — | Yes | — |
| Cisco Jabber for Windows (Supported from Cisco IOS XE Gibraltar 16.10.1 Release) | — | — | Yes | — | Yes | — | Yes | — |
| SSL VPN Client | — | Yes | — | — | — | — | — | — |
| Virtual CME (Only on Cisco CSR1000V Cloud Services Router) | — | — | — | — | — | — | Yes | Yes |
| Secure CME | — 6 | Yes | — | — | — | — | — | — |
| Secure Lineside | — | Yes | — | — | — | — | — | — |
| SIP Trunk | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Secure SIP Trunk | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |