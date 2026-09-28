---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-requirements-guide-unified-srst-platform-protocol-compatibility-matri-a849a79624
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/requirements/guide/Unified_SRST_Platform_Protocol_Compatibility_Matrix.html
retrieved_at: 2026-08-21T12:39:00.476293+00:00
---

Unified SRST Platform Protocol Compatibility Matrix

# Unified SRST Platform Protocol Compatibility Matrix

### Download Options

Platform and Protocol Compatibility for Unified SRST, Unified E-SRST, and Unified Secure SRST

First Published : July 30, 2018

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

Last Updated: March 30, 2024

Overview

Conventions

Platform and Protocol Support for Unified SRST and Unified Secure SRST Features

Platform and Protocol Support for Unified E-SRST Features

## Overview

This document provides information on the compatibility of Unified Survivable Remote Site Telephony features (for Unified SRST, Unified E-SRST, and Unified Secure SRST) across the Cisco Routers. Feature support is detailed by protocol and platform and was last updated for Cisco IOS XE 17.14.1a Release (Unified SRST Release 14.4).

For information on the Cisco IOS XE and Cisco IOS Release mapping with Unified SRST, see Unified CME, Unified SRST, and Cisco IOS Software Version Compatibility Matrix .

For information on feature description for Unified SRST, Unified E-SRST, and Unified Secure SRST, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

The protocols discussed in this document are:

· Session Initiation Protocol (SIP)

· Skinny Client Control Protocol (SCCP)

· Mixed Deployment (Supports both SIP and SCCP)

The platforms discussed in this document are:

· Cisco IOS XE Autonomous mode for Cisco 4000 Series Integrated Services Routers, Cisco 1000 (ISR1100 running IOS XE), Cisco 8300 Catalyst Edge Series Platforms, and Cisco 8200 Catalyst Edge Series Platforms

· Cisco IOS XE SD-WAN for Cisco 4000 Series Integrated Services Routers, Cisco 8300 Catalyst Edge Series, and Cisco 8200 Catalyst Edge Series Platforms

## Conventions

The following conventions are applicable to the information provided in the Feature Support sections.

Table 1 : Conventions

Convention

Description

Yes

The feature is supported.

–

The feature is not supported.

SIP

Session Initiation Protocol

SCCP

Skinny Client Control Protocol

Unified SRST

Unified Survivable Remote Site Telephony

Unified E-SRST

Unified Enhanced Survivable Remote Site Telephony

Unified Secure SRST

Unified Secure Survivable Remote Site Telephony

SD-WAN

Software Defined WAN Mode on Unified SRST

## P latform and Protocol Support for Unified SRST and Unified Secure SRST Features

As the feature support is consistent across Unified SRST and Unified Secure SRST, this section provides feature support information for both these products in Table 2: Unified SRST and Unified Secure SRST Feature Support .

· From Unified SRST Release 12.8 (Cisco IOS XE Amsterdam 17.2.1r), configuration and monitoring of Unified SRST using NetConf and RESTConf Yang models is supported in both Controller (SD-WAN) and Autonomous modes.

· From Unified SRST Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a), support is introduced for SNMP version 3 (SNMPv3) and toll fraud prevention for line-side SIP.  Unified SRST 12.6 and later releases do not support certain CLI commands configured under call-manager-fallback configuration mode to enhance security. For more information, see Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) .

· All features listed as supported for Unified SRST are also supported for Unified Secure SRST.

· If a feature is supported for both SIP and SCCP phones, then mixed deployment is supported on that platform.

For information on feature specific support for Unified SRST and Unified Secure SRST across platforms and protocols, see Table 2.

Table 2: Unified SRST and Unified Secure SRST Feature Support

Features

Classic IOS

Cisco IOS XE Autonomous Mode

Cisco IOS XE Controller Mode (SD-WAN)

SIP

SCCP

SIP

SCCP

SIP

Auto-Answer

Yes

Yes

Yes

Yes

—

Phone Registration to SRST (fallback)

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

Attended/Consult Transfer

Yes

Yes

Yes

Yes

Yes

Blind Transfer

—

Yes

—

—

Yes

Conference

Meet-Me Conference

—

—

—

—

—

Ad-hoc Hardware Conference

—

—

—

—

—

Ad-hoc Software Conference

Yes

Yes

Yes

Yes

Yes

Video Conference

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

Headset Answer

Yes

Yes

Yes

Yes

—

Line Label

Yes (except 3905, 6901,  6921)

Yes (except 69xx series)

Yes

Yes (except 69xx series)

—

Shared Line

—

Yes

—

Yes

—

Caller ID Display

Yes

Yes

Yes

Yes

Yes

Feature Access Code (FAC)

Yes

Yes

Yes

Yes

—

Voicemail

Yes

Yes

Yes

Yes

—

Message Waiting Indicator (MWI)

Yes

Yes

Yes

Yes

—

Reset/Restart Phones via Reset/Restart Command

—

Yes

—

Yes

—

Do Not Disturb (DND)

Yes (except 3905, 6901)

Yes

Yes

Yes

—

DTMF

Yes

—

Yes

—

Yes

Key Expansion Module (KEM)

Yes (only 8961)

Yes (only on 7962/7965/7975, 8941, 8945)

Yes (Only 88xx Series)

Yes (only on 7962/7965/7975, 8941, 8945)

Yes (Only 88xx Series)

Bulk Registration Support

Yes (except 6921)

—

Yes

—

—

Enabling/Disabling KPML

Yes

—

Yes

—

—

Alias Feature

Yes

Yes

Yes

Yes

—

Call Forward

All

Yes

—

Yes

Yes

Yes

Busy

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

Mailbox

Yes

—

Yes

Yes

Yes

Unregistered

—

—

—

—

—

Night-Service

—

—

—

—

—

Max-Length

—

—

—

—

—

Call Forward All Softkey on Phone

Yes

—

Yes

—

—

Multicast MOH

—

Yes

—

Yes

—

Unicast MOH

Yes

Yes

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

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

—

Ephone Hunt Group

—

Yes

—

Yes

—

Voice Hunt Group/Ephone Hunt Group Statistics (Only for static members)

Yes

Yes

Yes

Yes

—

Voice Class Codec

Yes

—

Yes

—

Yes

Audio Codecs

G.722

—

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

G.729

Yes

Yes

Yes

Yes

Yes

iLBC

—

Yes

Yes

Yes

Yes

Translation Profile

Yes

Yes

Yes

Yes

—

Busy Trigger Per Button

Yes

—

Yes

—

—

Conference Blocking

Yes

Yes

Yes

Yes

—

Transfer Blocking

Yes

Yes

Yes

Yes

—

COR

Yes

Yes

Yes

Yes

Yes

VRF for Unified SRST

Yes

Yes

Yes

—

—

SNMP/MIB

—

Yes

—

Yes

—

Speed Dial

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

—

Forced Authorization Code

—

Yes

—

Yes

—

Redial

Yes

Yes

Yes

Yes

—

Speakerphone

Dialing

Yes

Yes

Yes

Yes

—

Answering

Yes

Yes

Yes

Yes

—

System Message

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

—

Call Waiting Ring

—

Yes

—

Yes

—

Configurable TLS Cipher Policy

—

—

Yes

Yes

—

SIP OAuth Authentication

—

—

Yes

—

—

## Platform and Protocol Support for Unified E-SRST Features

This section provides feature support information specific to Cisco Unified Enhanced Survivable Remote Site Telephony (Unified E-SRST). In comparison to Unified SRST and Unified Secure SRST, Unified E-SRST provides support for features such as Shared Line, BLF, Video, and Voice Hunt Group feature support.

Note:

· If a feature is supported for both SIP and SCCP phones, then mixed deployment is supported on that platform.

· Unified E-SRST is not supported for IOS XE Controller (SD-WAN) mode.

· From Unified E-SRST Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a), support is introduced for toll fraud prevention on Line Side SIP of Unified E-SRST.

For information on feature specific support for Unified E-SRST across platforms and protocols, see Table 3: Unified E-SRST Feature Support.

Table 3: Unified E-SRST Feature Support

Features

Classic IOS

Cisco IOS XE Autonomous Mode

SIP

SCCP

SIP

SCCP

Anonymous Call Block

—

—

—

—

Auto-Answer

Yes

Yes

Yes

Yes

Auto Register

—

—

—

—

Auto Assign

—

—

—

—

Authenticate Register

—

—

—

—

Barge

—

—

—

—

cBarge/Merge

—

—

—

—

Call Park

—

—

—

—

Call Park Resume

—

—

—

—

Pickup

Group Pickup

—

—

—

—

Directed Call Pickup

—

—

—

—

Distinctive Ring for Parked Call Recall

—

—

—

—

Park Monitor

—

—

—

—

Directed Call Park

—

—

—

—

Extension Mobility

—

—

—

—

Transfer

Alert Transfer

Yes

Yes

Yes

Yes

Attended Consult Transfer

Yes

Yes

Yes

Yes

Blind Transfer

—

Yes

—

Yes

Conference

Meet-Me Conference

—

—

—

—

Ad-hoc Hardware Conference

—

—

—

—

Ad-hoc Software Conference

Yes

Yes

Yes

Yes

Video Conference

—

—

—

—

Hold/Resume

Yes

Yes

Yes

Yes

Intercom

—

—

—

—

Fast Track

—

—

—

—

Headset Answer

Yes

Yes

Yes

Yes

Line Label

Yes (except 3905, 6901,  6921)

Yes (except 69xx series)

Yes

Yes (except 69xx series)

My Phone Apps - View On Phone

Speed Dial

—

—

—

—

Personal Speed Dial/Fast Dial

—

—

—

—

BLF Speed Dial

—

—

—

—

Voice Hunt Groups

—

—

—

—

After Hours

—

—

—

—

Single Number Reach (SNR)

—

—

—

—

Active Call Park List

—

—

—

—

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

—

—

—

—

Fast Dial

—

—

—

—

BLF Speed Dial

—

—

—

—

Single Number Reach (SNR)

—

—

—

—

Park Retrieval

—

—

—

—

Paging

Multicast (Only with G711ulaw codec)

—

—

—

—

Unicast (Only with G711ulaw codec)

—

—

—

—

Shared Line

Yes

Yes

Yes

Yes

Mixed Shared Line

Yes

Yes

Yes

Yes

Voice Hunt Group with Shared Line

Yes

Yes

Yes

Yes

Caller ID Display

Yes

Yes

Yes

Yes

Caller ID Blocking

—

—

—

—

Feature Access Code (FAC)

Yes

Yes

Yes

Yes

Call Transfer Recall

—

—

—

—

Voicemail

Yes

Yes

Yes

Yes

Message Waiting Indicator (MWI)

Yes

Yes

Yes

Yes

Video

Yes

Yes

Yes

Yes

Locale Support

—

—

—

—

Reset/Restart Phones via Reset/Restart Command

—

Yes

—

Yes

Button Layout/Softkey Template

—

—

—

—

Directory Services

Local Directory

—

—

—

—

Local Speed Dial

—

—

—

—

Personal Speed Dial

—

—

—

—

Privacy

—

—

—

—

iDivert

—

—

—

—

Enhanced iDivert

—

—

—

—

Do Not Disturb (DND)

Yes (except 3905, 6901)

Yes

Yes

Yes

DTMF

Yes

—

Yes

—

Feature Button/Programmable Line Key (PLK)

—

—

—

—

Key Expansion Module (KEM)

Yes (only 8961)

Yes (only on 7962/7965/7975, 8941, 8945)

Yes (Only 88xx Series)

Yes (only on 7962/7965/7975, 8941, 8945)

Bulk Registration Support

Yes (except 6921)

—

Yes

—

Upgrading/Downgrading Phone Firmware Versions

—

—

—

—

Live Record

—

—

—

—

Enabling/Disabling KPML

Yes

—

Yes

—

Alias Feature

Yes

Yes

Yes

Yes

Call Forward

All

Yes

—

Yes

—

Busy

Yes

Yes

Yes

Yes

No Answer

Yes

Yes

Yes

Yes

Mailbox

Yes

—

Yes

—

Unregistered

—

—

—

—

Night-Service

—

—

—

—

Max-Length

—

—

—

—

Call Forward All Softkey on Phone

Yes

—

Yes

—

Multicast MOH

—

Yes

—

Yes

Unicast MOH

Yes

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

Yes

Yes

Yes

Yes

Night Service

—

—

—

—

Voice Hunt Group

Yes

Yes

Yes

Yes

Ephone Hunt Group

—

Yes

—

Yes

Channel Hunt Stop

—

—

—

—

Voice Hunt Group/Ephone Hunt Group Statistics (Only for static members)

Yes

Yes

Yes

Yes

Voice Class Codec

Yes

—

Yes

—

Audio Codecs

G.722

—

Yes

Yes

Yes

G.711

Yes

Yes

Yes

Yes

G.729

Yes

Yes

Yes

Yes

iLBC

—

Yes

Yes

Yes

Translation Profile

Yes

Yes

Yes

Yes

Busy Trigger Per Button

Yes

—9

Yes

—

Conference Blocking

Yes

Yes

Yes

Yes

Transfer Blocking

Yes

Yes

Yes

Yes

COR

Yes

Yes

Yes

Yes

Transcoding

—

—

—

—

SNMP/MIB

—

Yes

—

Yes

Web GUI

—

—

—

—

IOS XE Web GUI

—

—

—

—

Speed Dial

Yes

Yes

Yes

Yes

Busy Lamp Field (BLF)

Yes

Yes

Yes

Yes

Call Waiting

Yes

Yes

Yes

Yes

Forced Authorization Code

—

Yes

—

Yes

HTTP File Server (HFS)

—

—

—

—

Redial

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

Answering

Yes

Yes

Yes

Yes

System Message

Yes

Yes

Yes

Yes

Whisper Intercom

—

—

—

—

Abbreviated Dialing

—

—

—

—

After Hours

Yes

Yes

Yes

Yes

Callback

—

—

—

—

Call Waiting Ring

—

Yes

—

Yes

Configurable TLS Cipher Policy

—

—

Yes

Yes

SIP OAuth Authentication

—

—

Yes

—

Obtain Documentation and Submit a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What’s New in Cisco Product Documentation RSS feed. The RSS feeds are a free service.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R)

Cisco Unified Communications Manager Express Phone Feature Support

© 2024 Cisco Systems, Inc. All Rights reserved.

| Convention | Description |
|---|---|
| Yes | The feature is supported. |
| – | The feature is not supported. |
| SIP | Session Initiation Protocol |
| SCCP | Skinny Client Control Protocol |
| Unified SRST | Unified Survivable Remote Site Telephony |
| Unified E-SRST | Unified Enhanced Survivable Remote Site Telephony |
| Unified Secure SRST | Unified Secure Survivable Remote Site Telephony |
| SD-WAN | Software Defined WAN Mode on Unified SRST |

| Features | Classic IOS | Cisco IOS XE Autonomous Mode | Cisco IOS XE Controller Mode (SD-WAN) |
|---|---|---|---|
| SIP | SCCP | SIP | SCCP | SIP |
| Auto-Answer | Yes | Yes | Yes | Yes | — |
| Phone Registration to SRST (fallback) | Yes | Yes | Yes | Yes | Yes |
| Transfer | Alert Transfer | Yes | Yes | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes | Yes | Yes |
| Blind Transfer | — | Yes | — | — | Yes |
| Conference | Meet-Me Conference | — | — | — | — | — |
| Ad-hoc Hardware Conference | — | — | — | — | — |
| Ad-hoc Software Conference | Yes | Yes | Yes | Yes | Yes |
| Video Conference | — | — | — | — | — |
| Hold/Resume | Yes | Yes | Yes | Yes | Yes |
| Headset Answer | Yes | Yes | Yes | Yes | — |
| Line Label | Yes (except 3905, 6901,  6921) | Yes (except 69xx series) | Yes | Yes (except 69xx series) | — |
| Shared Line | — | Yes | — | Yes | — |
| Caller ID Display | Yes | Yes | Yes | Yes | Yes |
| Feature Access Code (FAC) | Yes | Yes | Yes | Yes | — |
| Voicemail | Yes | Yes | Yes | Yes | — |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes | Yes | — |
| Reset/Restart Phones via Reset/Restart Command | — | Yes | — | Yes | — |
| Do Not Disturb (DND) | Yes (except 3905, 6901) | Yes | Yes | Yes | — |
| DTMF | Yes | — | Yes | — | Yes |
| Key Expansion Module (KEM) | Yes (only 8961) | Yes (only on 7962/7965/7975, 8941, 8945) | Yes (Only 88xx Series) | Yes (only on 7962/7965/7975, 8941, 8945) | Yes (Only 88xx Series) |
| Bulk Registration Support | Yes (except 6921) | — | Yes | — | — |
| Enabling/Disabling KPML | Yes | — | Yes | — | — |
| Alias Feature | Yes | Yes | Yes | Yes | — |
| Call Forward | All | Yes | — | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes | Yes | Yes |
| Mailbox | Yes | — | Yes | Yes | Yes |
| Unregistered | — | — | — | — | — |
| Night-Service | — | — | — | — | — |
| Max-Length | — | — | — | — | — |
| Call Forward All Softkey on Phone | Yes | — | Yes | — | — |
| Multicast MOH | — | Yes | — | Yes | — |
| Unicast MOH | Yes | Yes | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | Yes | Yes | Yes | Yes | — |
| Voice Hunt Group | Yes | Yes | Yes | Yes | — |
| Ephone Hunt Group | — | Yes | — | Yes | — |
| Voice Hunt Group/Ephone Hunt Group Statistics (Only for static members) | Yes | Yes | Yes | Yes | — |
| Voice Class Codec | Yes | — | Yes | — | Yes |
| Audio Codecs | G.722 | — | Yes | Yes | Yes | Yes |
| G.711 | Yes | Yes | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes | Yes | Yes |
| iLBC | — | Yes | Yes | Yes | Yes |
| Translation Profile | Yes | Yes | Yes | Yes | — |
| Busy Trigger Per Button | Yes | — | Yes | — | — |
| Conference Blocking | Yes | Yes | Yes | Yes | — |
| Transfer Blocking | Yes | Yes | Yes | Yes | — |
| COR | Yes | Yes | Yes | Yes | Yes |
| VRF for Unified SRST | Yes | Yes | Yes | — | — |
| SNMP/MIB | — | Yes | — | Yes | — |
| Speed Dial | Yes | Yes | Yes | Yes | — |
| Call Waiting | Yes | Yes | Yes | Yes | — |
| Forced Authorization Code | — | Yes | — | Yes | — |
| Redial | Yes | Yes | Yes | Yes | — |
| Speakerphone | Dialing | Yes | Yes | Yes | Yes | — |
| Answering | Yes | Yes | Yes | Yes | — |
| System Message | Yes | Yes | Yes | Yes | — |
| After Hours | Yes | Yes | Yes | Yes | — |
| Call Waiting Ring | — | Yes | — | Yes | — |
| Configurable TLS Cipher Policy | — | — | Yes | Yes | — |
| SIP OAuth Authentication | — | — | Yes | — | — |

| Features | Classic IOS | Cisco IOS XE Autonomous Mode |
|---|---|---|
| SIP | SCCP | SIP | SCCP |
| Anonymous Call Block | — | — | — | — |
| Auto-Answer | Yes | Yes | Yes | Yes |
| Auto Register | — | — | — | — |
| Auto Assign | — | — | — | — |
| Authenticate Register | — | — | — | — |
| Barge | — | — | — | — |
| cBarge/Merge | — | — | — | — |
| Call Park | — | — | — | — |
| Call Park Resume | — | — | — | — |
| Pickup | Group Pickup | — | — | — | — |
| Directed Call Pickup | — | — | — | — |
| Distinctive Ring for Parked Call Recall | — | — | — | — |
| Park Monitor | — | — | — | — |
| Directed Call Park | — | — | — | — |
| Extension Mobility | — | — | — | — |
| Transfer | Alert Transfer | Yes | Yes | Yes | Yes |
| Attended Consult Transfer | Yes | Yes | Yes | Yes |
| Blind Transfer | — | Yes | — | Yes |
| Conference | Meet-Me Conference | — | — | — | — |
| Ad-hoc Hardware Conference | — | — | — | — |
| Ad-hoc Software Conference | Yes | Yes | Yes | Yes |
| Video Conference | — | — | — | — |
| Hold/Resume | Yes | Yes | Yes | Yes |
| Intercom | — | — | — | — |
| Fast Track | — | — | — | — |
| Headset Answer | Yes | Yes | Yes | Yes |
| Line Label | Yes (except 3905, 6901,  6921) | Yes (except 69xx series) | Yes | Yes (except 69xx series) |
| My Phone Apps - View On Phone | Speed Dial | — | — | — | — |
| Personal Speed Dial/Fast Dial | — | — | — | — |
| BLF Speed Dial | — | — | — | — |
| Voice Hunt Groups | — | — | — | — |
| After Hours | — | — | — | — |
| Single Number Reach (SNR) | — | — | — | — |
| Active Call Park List | — | — | — | — |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | — | — | — | — |
| Fast Dial | — | — | — | — |
| BLF Speed Dial | — | — | — | — |
| Single Number Reach (SNR) | — | — | — | — |
| Park Retrieval | — | — | — | — |
| Paging | Multicast (Only with G711ulaw codec) | — | — | — | — |
| Unicast (Only with G711ulaw codec) | — | — | — | — |
| Shared Line | Yes | Yes | Yes | Yes |
| Mixed Shared Line | Yes | Yes | Yes | Yes |
| Voice Hunt Group with Shared Line | Yes | Yes | Yes | Yes |
| Caller ID Display | Yes | Yes | Yes | Yes |
| Caller ID Blocking | — | — | — | — |
| Feature Access Code (FAC) | Yes | Yes | Yes | Yes |
| Call Transfer Recall | — | — | — | — |
| Voicemail | Yes | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes | Yes |
| Video | Yes | Yes | Yes | Yes |
| Locale Support | — | — | — | — |
| Reset/Restart Phones via Reset/Restart Command | — | Yes | — | Yes |
| Button Layout/Softkey Template | — | — | — | — |
| Directory Services | Local Directory | — | — | — | — |
| Local Speed Dial | — | — | — | — |
| Personal Speed Dial | — | — | — | — |
| Privacy | — | — | — | — |
| iDivert | — | — | — | — |
| Enhanced iDivert | — | — | — | — |
| Do Not Disturb (DND) | Yes (except 3905, 6901) | Yes | Yes | Yes |
| DTMF | Yes | — | Yes | — |
| Feature Button/Programmable Line Key (PLK) | — | — | — | — |
| Key Expansion Module (KEM) | Yes (only 8961) | Yes (only on 7962/7965/7975, 8941, 8945) | Yes (Only 88xx Series) | Yes (only on 7962/7965/7975, 8941, 8945) |
| Bulk Registration Support | Yes (except 6921) | — | Yes | — |
| Upgrading/Downgrading Phone Firmware Versions | — | — | — | — |
| Live Record | — | — | — | — |
| Enabling/Disabling KPML | Yes | — | Yes | — |
| Alias Feature | Yes | Yes | Yes | Yes |
| Call Forward | All | Yes | — | Yes | — |
| Busy | Yes | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes | Yes |
| Mailbox | Yes | — | Yes | — |
| Unregistered | — | — | — | — |
| Night-Service | — | — | — | — |
| Max-Length | — | — | — | — |
| Call Forward All Softkey on Phone | Yes | — | Yes | — |
| Multicast MOH | — | Yes | — | Yes |
| Unicast MOH | Yes | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | Yes | Yes | Yes | Yes |
| Night Service | — | — | — | — |
| Voice Hunt Group | Yes | Yes | Yes | Yes |
| Ephone Hunt Group | — | Yes | — | Yes |
| Channel Hunt Stop | — | — | — | — |
| Voice Hunt Group/Ephone Hunt Group Statistics (Only for static members) | Yes | Yes | Yes | Yes |
| Voice Class Codec | Yes | — | Yes | — |
| Audio Codecs | G.722 | — | Yes | Yes | Yes |
| G.711 | Yes | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes | Yes |
| iLBC | — | Yes | Yes | Yes |
| Translation Profile | Yes | Yes | Yes | Yes |
| Busy Trigger Per Button | Yes | —9 | Yes | — |
| Conference Blocking | Yes | Yes | Yes | Yes |
| Transfer Blocking | Yes | Yes | Yes | Yes |
| COR | Yes | Yes | Yes | Yes |
| Transcoding | — | — | — | — |
| SNMP/MIB | — | Yes | — | Yes |
| Web GUI | — | — | — | — |
| IOS XE Web GUI | — | — | — | — |
| Speed Dial | Yes | Yes | Yes | Yes |
| Busy Lamp Field (BLF) | Yes | Yes | Yes | Yes |
| Call Waiting | Yes | Yes | Yes | Yes |
| Forced Authorization Code | — | Yes | — | Yes |
| HTTP File Server (HFS) | — | — | — | — |
| Redial | Yes | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes | Yes | Yes |
| Answering | Yes | Yes | Yes | Yes |
| System Message | Yes | Yes | Yes | Yes |
| Whisper Intercom | — | — | — | — |
| Abbreviated Dialing | — | — | — | — |
| After Hours | Yes | Yes | Yes | Yes |
| Callback | — | — | — | — |
| Call Waiting Ring | — | Yes | — | Yes |
| Configurable TLS Cipher Policy | — | — | Yes | Yes |
| SIP OAuth Authentication | — | — | Yes | — |