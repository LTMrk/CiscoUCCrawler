---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-feature-phone-feature-phone-feature-support-guide-html-4eec10032b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/feature/phone_feature/phone_feature_support_guide.html
retrieved_at: 2026-08-21T09:47:35.077410+00:00
---

Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST

# Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST

### Download Options

Updated: April 14, 2019

# Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, Unified Secure SRST

First Published : September 1, 2014

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

Last Updated: April 15, 2019

Overview

Conventions

Phone Feature Support for Unified CME, Release 12.6

Phone Feature Support for Unified CME, Release 12.5

Phone Feature Support for Cisco ATA 191 with Unified CME

Phone Feature Support for Cisco Jabber with Unified CME

Phone Feature Support for Analog Voice Gateways with Virtual CME

Phone Feature Support for Unified CME, Release 12.3

Phone Feature Support for Unified Secure SRST, Release 12.3

Phone Feature Support for Analog Voice Gateway with Secure SCCP SRST

Phone Feature Support for Unified CME, Release 12.2

Phone Feature Support for Unified E-SRST, Release 12.2

Phone Feature Support for Unified SRST, Release 12.1

Phone Feature Support for Unified CME, Unified SRST Release 12.0

Phone Feature Support for Unified CME, Release 11.7

Phone Feature Support for Unified CME, Release 11.6

Phone Feature Support for Unified CME, Release 11.5

Phone Feature Support for Release 11.0

Cisco Unified Communications Manager Express Phone Feature Support

Cisco Unified Survivable Remote Site Telephony Phone Feature Support

Cisco Unified Enhanced Survivable Remote Site Telephony Phone Feature Support

Cisco Unified Secure Survivable Remote Site Telephony Phone Feature Support

Phone Feature Support (Prior to Release 11.0)

Unified CME Support (Prior to Release 11.0)

Cisco Unified SRST Support (Prior to Release 11.0)

Cisco Unified E-SRST Support (Prior to Release 11.0)

KEM Support for Cisco Unified SIP IP Phones

Fast Track Phone Feature Support

## Overview

This document describes phone feature support information for Cisco Unified Communications Manager Express (Unified CME), Cisco Unified Survivable Remote Site Telephony (Unified SRST), Cisco Unified Enhanced Survivable Remote Site Telephony (Unified E-SRST), and Cisco Secure Survivable Remote Site Telephony (Secure SRST). Information on fast track phone configuration and feature support is included.

## Conventions

The following conventions are applicable to the information provided in the Feature Support sections.

Table 1 : Conventions

Convention

Description

Yes

The feature is supported.

Yes*

The feature is supported by Unified E-SRST (but not by Unified SRST Manager).

No

The feature is not supported.

No*

It is a known phone limitation.

Note: - If Yes* is applicable, the user is required to manually configure the feature in E-SRST mode.

## Phone Feature Support for Unified CME, Release 12.6

This section provides feature support information specific to Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a) for Cisco Unified Communications Manager Express.

Table 2: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8821

7832

8831

7841

8832

7861

8841

8845

8851/51NR

8861

8865

Toll Fraud Prevention for Unified CME Line Side SIP

Yes

Yes

Unified CME Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a Release) introduces support for SNMP Version 3 (SNMPv3) and Unified CME Password Policy. Unified CME GUI and CTI CSTA features are deprecated, and not available on Unified CME 12.6 and later releases.

## Phone Feature Support for Unified CME, Release 12.5

This section provides feature support information specific to Release 12.5 (Cisco IOS XE Gibraltar 16.10.1) for Cisco Unified Communications Manager Express.

Table 2: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8821

7832

8831

7841

8832

7861

8841

8845

8851/51NR

8861

8865

Virtual CME (vCME) on Cisco CSR1000V Cloud Services Router

Yes

Yes

As part of Unified CME Release 12.5 (Cisco IOS XE Gibraltar 16.10.1 Release), support was introduced for Cisco ATA 191, Cisco Jabber, and KEM Modules (CP-8800-Audio, CP-8800-Video).

### Phone Feature Support for Cisco ATA 191 with Unified CME

This section provides feature support information specific to Cisco ATA 191 with Cisco Unified Communications Manager Express.

Table 3: Phone Feature Support for Cisco ATA 191 with Unified CME

Features

Phone Model (Cisco ATA 191)

Anonymous Call Block

No

Auto-Answer

No

Auto Register

Yes

Auto Assign

No

Authenticate Register

No

Barge

No

cBarge/Merge

Yes

Call Park

Yes

Call Park Resume

No

Pickup

Pickup

Yes

Group Pickup

Yes

Distinctive Ring for Parked Call Recall

No

Park Monitor

No

Directed Call Park

No

Extension Mobility

No

Extension Assigner

Yes

Transfer

Alert Transfer

Yes

Attended/Consult Transfer

Yes

Blind Transfer

No

Conference

Meet-Me Conference

Yes

Ad-hoc Hardware Conference

No

Ad-hoc Software Conference

No*

Video Conference

No

Hold/Resume

Yes

Intercom

No

Fast Track

No

Headset Answer

No

Line Label

No

My Phone Apps - View On Phone

Speed Dial

No

Personal Speed Dial/Fast Dial

No

BLF Speed Dial

No

Voice Hunt Groups

No

After Hours

No

Single Number Reach (SNR)

No

Active Call Park List

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

Fast Dial

No

BLF Speed Dial

No

Single Number Reach (SNR)

No

Park Retrieval

No

Paging

Multicast (Only with G711ulaw codec)

No

Unicast (Only with G711ulaw codec)

No

Shared Line

Yes

Mixed Shared Line

Yes

Voice Hunt Group with Shared Line

No

Caller ID Display

No

Caller ID Blocking

Yes

Feature Access Code (FAC) 1

No

Call Transfer Recall

No

Voicemail

Yes

Message Waiting Indicator (MWI)

Yess

Video 2

No

Locale Support

No

Reset/Restart Phones via Reset/Restart Command

No

Button Layout/Softkey Template

No

Directory Services

Local Directory

No

Local Speed Dial

No

Personal Speed Dial

No

Privacy

No

iDivert* (Transfer to other mailboxes is not supported)

No

Enhanced iDivert

No

Do Not Disturb (DND)

No

DTMF

Yes

Feature Button/Programmable Line Key (PLK)

No

Key Expansion Module (KEM)

C-KEM

No

BE-KEM

No

A-KEM (CP-8800-Audio)

No

V-KEM (CP-8800-Video)

No

Bulk Registration Support

No

Upgrading/Downgrading Phone Firmware Versions

Yes

Live Record

No

Enabling/Disabling KPML

Yes

Alias Feature

No

Call Forward

All

Yes

Busy

Yes

No Answer

Yes

Mailbox

No

Unregistered

Yes

Night-Service

No

Max-Length

No

Call Forward All Softkey on Phone

No

Music on Hold (MOH)

Yes

Basic Automatic Call Distribution (B-ACD)

No

Night Service

No

Voice Hunt Group

No

Channel Hunt Stop

No

Voice Hunt Group/Ephone Hunt Group Statistics

No

Translation Profile

No

Busy Trigger Per Button

No

Conference Blocking

No

Transfer Blocking

No

COR

No

Voice Class Codec

No

Audio Codecs

G.722

No

G.711

No

G.729

No

iLBC

No

Transcoding

No

Multi-VRF (Only supported on ISR G2)

No

SNMP/MIB

No

Web GUI

No

Speed Dial

No

Busy Lamp Field (BLF)

No

Call Waiting

Yes

Forced Authorization Code

No

HTTP File Server (HFS)

No

Redial

Yes

Speakerphone

Dialing

No

Answering

No

System Message

No

Whisper Intercom

No

Abbreviated Dialing

No

After Hours

No

SSH to Phone

Yes

Span to PC

No

Web Access to Phone

Yes

Callback

No

Call Waiting Ring/Tone

No

Fax Transmission

T.38

Yes

Codec Passthrough

Yes

### Phone Feature Support for Cisco Jabber with Unified CME

This section provides feature support information specific to Cisco Jabber 12.1.0 with Unified CME 12.5 Release.

Table 4: Phone Feature Support for Cisco Jabber with Unified CME

Features

Phone Model (Cisco Jabber)

Auto Register

No

Auto Assign

No

Authenticate Register

No

Barge

No

cBarge/Merge

No

Call Park

Yes

Call Park Resume

Yes

Pickup

Pickup

Yes

Group Pickup

No

Distinctive Ring for Parked Call Recall

No

Park Monitor

No

Directed Call Park

Yes

Extension Mobility

No

Transfer

Alert Transfer

Yes

Attended/Consult Transfer

Yes

Blind Transfer

No

Conference

Meet-Me Conference

No

Ad-hoc Hardware Conference

Yes

Ad-hoc Software Conference

No

Video Conference

No

Hold/Resume

Yes

Intercom

No

Fast Track

No

Headset Answer

No

Line Label

No

My Phone Apps - View On Phone

Speed Dial

No

Personal Speed Dial/Fast Dial

No

BLF Speed Dial

No

Voice Hunt Groups

No

After Hours

No

Single Number Reach (SNR)

No

Active Call Park List

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

Fast Dial

No

BLF Speed Dial

No

Single Number Reach (SNR)

Yes

Paging

Multicast (Only with G711ulaw codec)

No

Unicast (Only with G711ulaw codec)

No

Shared Line

Yes

Mixed Shared Line

Yes

Voice Hunt Group with Shared Line

Yes

Caller ID Display

No

Caller ID Blocking

No

Feature Access Code (FAC) 1

No

Call Transfer Recall

No

Voicemail

No

Message Waiting Indicator (MWI)

No

Video

Yes

Locale Support

No

Reset/Restart Phones via Reset/Restart Command

Yes

Button Layout/Softkey Template

No

Directory Services

Local Directory

No

Local Speed Dial

No

Personal Speed Dial

No

Privacy

Yes

iDivert

No

Enhanced iDivert

No

Do Not Disturb (DND)

No

DTMF

Yes

Feature Button/Programmable Line Key (PLK)

No

Upgrading/Downgrading Phone Firmware Versions

No

Live Record

No

Enabling/Disabling KPML

No

Alias Feature

No

Call Forward

All

Yes

Busy

Yes

No Answer

Yes

Mailbox

No

Unregistered

Yes

Night-Service

No

Max-Length

No

Call Forward All Softkey on Phone

No

Music on Hold (MOH)

Yes

Basic Automatic Call Distribution (B-ACD)

No

Night Service

No

Voice Hunt Group

Yes

Channel Hunt Stop

No

Audio Codecs

G.722

No

G.711

No

G.729

No

iLBC

No

Video Codec (H.264)

Yes

Speed Dial

No

Busy Lamp Field (BLF)

No

Redial

Yes

### Phone Feature Support for Analog Voice Gateways with Virtual CME

The Support for SCCP endpoints on Virtual CME is restricted to Analog Voice Gateways. This section provides feature support information specific to Virtual CME for Analog Voice Gateway platforms. The support is introduced for Unified CME 12.5 (Cisco IOS XE Gibraltar 16.10.1) and later releases.

· For information on feature specific support for Unified CME across Analog VG Platforms, see Table 5.

Table 5: Phone Feature Support for Analog Voice Gateways with vCME

Features

VG310

VG320

VG350

Anonymous Call Block

No

No

No

Auto-Answer

No

No

No

Auto Register

Yes

Yes

Yes

Auto Assign

Yes

Yes

Yes

Authenticate Register

No

No

No

Barge

No

No

No

cBarge

No

No

No

Call Park

Yes

Yes

Yes

Pickup

Group Pickup

Yes

Yes

Yes

Call Pickup

Yes

Yes

Yes

Distinctive Ring for Parked Call Recall

No

No

No

Directed Call Park

Yes

Yes

Yes

Extension Mobility

No

No

No

Extension Assigner

Yes

Yes

Yes

Transfer

Alert Transfer

Yes

Yes

Yes

Attended/Consult Transfer

Yes

Yes

Yes

Blind Transfer

Yes

Yes

Yes

Conference

Meet-Me Conference

No

No

No

Ad-hoc Hardware Conference

No

No

No

Video Conference

No

No

No

Hold/Resume

Yes

Yes

Yes

Intercom

No

No

No

Fast Track

No

No

No

Headset Answer

No

No

No

Line Label

No

No

No

Single Number Reach (SNR) (except Mobility)

Yes

Yes

Yes

Park Retrieval

Yes

Yes

Yes

Paging

Multicast (Only with G711ulaw codec)

No

No

No

Unicast (Only with G711ulaw codec)

No

No

No

Shared Line (No Hold/ Remote Resume Support)

Yes

Yes

Yes

Mixed Shared Line (No Hold/ Remote Resume Support)

Yes

Yes

Yes

Voice Hunt Group with Shared Line

Yes

Yes

Yes

Caller ID Display

Yes

Yes

Yes

Caller ID Blocking

Yes

Yes

Yes

Feature Access Code ( VG Specific FAC )

Yes

Yes

Yes

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Call Transfer Recall

Yes

Yes

Yes

Voicemail

Yes

Yes

Yes

Message Waiting Indicator (MWI). See Configuring AMWI and VMWI .

Yes

Yes

Yes

Video

No

No

No

Locale Support

No

No

No

Button Layout/Softkey Template

No

No

No

Directory Services

Local Directory

No

No

No

Local Speed Dial

No

No

No

Personal Speed Dial

No

No

No

iDivert

No

No

No

Enhanced iDivert

No

No

No

Do Not Disturb (DND) (Supported with FAC)

Yes

Yes

Yes

DTMF

Yes

Yes

Yes

Feature Button/Programmable Line Key (PLK)

No

No

No

Live Record

No

No

No

Call Forward

All

Yes

Yes

Yes

Busy

Yes

Yes

Yes

No Answer

Yes

Yes

Yes

Mailbox

No

No

No

Unregistered

No

No

No

Night-Service

Yes

Yes

Yes

Max-Length

Yes

Yes

Yes

Multicast MOH

No

No

No

Unicast MOH

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

Yes

Yes

Yes

Night Service

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Channel Hunt Stop

Yes

Yes

Yes

Voice Hunt Group or Ephone Hunt Group Statistics

Yes

Yes

Yes

Audio Codecs

G.722

Yes

Yes

Yes

G.711

Yes

Yes

Yes

G.729

Yes

Yes

Yes

iLBC

Yes

Yes

Yes

Translation Profile

Yes

Yes

Yes

Busy Trigger Per Button (Maximum Value: 2)

Yes

Yes

Yes

Conference Blocking

Yes

Yes

Yes

Transfer Blocking

Yes

Yes

Yes

COR

Yes

Yes

Yes

Voice Class Codec

No

No

No

Transcoding

No

No

No

Multi-VRF

No

No

No

SNMP/MIB

Yes

Yes

Yes

Speed Dial

Yes

Yes

Yes

Busy Lamp Field (BLF)

No

No

No

Call Waiting

Yes

Yes

Yes

Forced Authorization Code

Yes

Yes

Yes

Redial

Yes

Yes

Yes

Speakerphone (Endpoint Supports)

Dialing

Yes

Yes

Yes

Answering

Yes

Yes

Yes

System Message

No

No

No

Whisper Intercom

No

No

No

Abbreviated Dialing

No

No

No

After Hours

Yes

Yes

Yes

Callback

No

No

No

Secondary CME

Yes

Yes

Yes

## Phone Feature Support for Unified CME, Release 12.3

This section provides feature support information specific to Release 12.3 (Cisco IOS XE Fuji 16.9.1) for Cisco Unified Communications Manager Express.

Table 6: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8821

7832

8831

7841

8832

7861

8841

8845

8851/51NR

8861

8865

Enhanced Line Mode on Cisco 4000 Series Integrated Services Routers

No

Yes (except 8821,8831, 8832)

Softkeys (Recents, Contacts, Apps, Favorites, Messages, Settings)

Yes (only for 7832)

Yes (only for 8832)

As part of Unified CME Release 12.3 (Cisco IOS XE Fuji 16.9.1 Release), support was introduced for Cisco IP Conference Phone 7832 and Cisco IP Conference Phone 8832.

## Phone Feature Support for Unified Secure SRST, Release 12.3

This section provides feature support information specific to Release 12.3 (Cisco IOS XE Fuji 16.9.1) for Cisco Unified Secure Survivable Remote Site Telephony.

Table 7: Unified E-SRST Phone Feature Support

Features

Phone Models

Cisco Unified IP Phone 6900 Series

Cisco Unified IP Phone 7900 Series

6961

7962

7945

7965

7975

Support for Secure SCCP Endpoints and Analog Voice Gateways on Secure SRST.

Note: For information on VG feature support, see Table 8: Phone Feature Support for Analog Voice Gateways with Secure SRST .

Yes

Yes

### Phone Feature Support for Analog Voice Gateway with Secure SCCP SRST

This section provides feature support information specific to Cisco Unified Secure Survivable Remote Site Telephony (Unified Secure SRST) across Voice Gateway platforms. The support is introduced for Unified Secure SRST 12.3 and later releases.

· For information on feature specific support for Unified SRST across platforms and protocols, see Table 8: Phone Feature Support for Analog Voice Gateways with Secure SRST.

Table 8: Phone Feature Support for Analog Voice Gateways with Secure SRST

Features

VG202

VG202XM

VG204

VG204XM

VG224

VG310

VG320

Anonymous Call Block

No

No

No

No

No

No

No

Auto-Answer

No

No

No

No

No

No

No

Auto Register

No

No

No

No

No

No

No

Auto Assign

No

No

No

No

No

No

No

Authenticate Register

No

No

No

No

No

No

No

Barge

No

No

No

No

No

No

No

cBarge

No

No

No

No

No

No

No

Call Park

No

No

No

No

No

No

No

Call Park Resume

No

No

No

No

No

No

No

Pickup

Group Pickup

No

No

No

No

No

No

No

Call Pickup

No

No

No

No

No

No

No

Distinctive Ring for Parked Call Recall

No

No

No

No

No

No

No

Park Monitor

No

No

No

No

No

No

No

Directed Call Park

No

No

No

No

No

No

No

Extension Mobility

No

No

No

No

No

No

No

Transfer

Alert/Semi-Consult Transfer

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

Blind Transfer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Conference

Meet-Me Conference

No

No

No

No

No

No

No

Ad-hoc Hardware Conference

No

No

No

No

No

No

No

Ad-hoc Software Conference (only with G.711 codec)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Video Conference

No

No

No

No

No

No

No

Hold/Resume

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Intercom

No

No

No

No

No

No

No

Fast Track

No

No

No

No

No

No

No

Headset Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Line Label

No

No

No

No

No

No

No

Mobility

No

No

No

No

No

No

No

My Phone Apps - View On Phone

Speed Dial

No

No

No

No

No

No

No

Personal Speed Dial/Fast Dial

No

No

No

No

No

No

No

BLF Speed Dial

No

No

No

No

No

No

No

Voice Hunt Groups

No

No

No

No

No

No

No

After Hours

No

No

No

No

No

No

No

Single Number Reach (SNR)

No

No

No

No

No

No

No

Active Call Park List

No

No

No

No

No

No

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

No

No

No

No

No

No

Fast Dial

No

No

No

No

No

No

No

BLF Speed Dial

No

No

No

No

No

No

No

Single Number Reach (SNR)

No

No

No

No

No

No

No

Park Retrieval

No

No

No

No

No

No

No

Paging

Multicast (Only with G711ulaw codec)

No

No

No

No

No

No

No

Unicast (Only with G711ulaw codec)

No

No

No

No

No

No

No

Shared Line (No Hold/ Remote Resume Support)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Mixed Shared Line

No

No

No

No

No

No

No

Voice Hunt Group with Shared Line

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Caller ID Display

No

No

No

No

No

No

No

Caller ID Blocking

No

No

No

No

No

No

No

Feature Access Code ( VG Specific FAC )

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer Recall

No

No

No

No

No

No

No

Voicemail

No

No

No

No

No

No

No

Message Waiting Indicator (MWI)

No

No

No

No

No

No

No

Video

No

No

No

No

No

No

No

Locale Support

No

No

No

No

No

No

No

Reset/Restart Phones via Reset/Restart Command

No

No

No

No

No

No

No

Button Layout/Softkey Template

No

No

No

No

No

No

No

Directory Services

Local Directory

No

No

No

No

No

No

No

Local Speed Dial

No

No

No

No

No

No

No

Personal Speed Dial

No

No

No

No

No

No

No

Privacy

No

No

No

No

No

No

No

iDivert

No

No

No

No

No

No

No

Enhanced iDivert

No

No

No

No

No

No

No

Do Not Disturb (DND)

No

No

No

No

No

No

No

DTMF

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Feature Button/Programmable Line Key (PLK)

No

No

No

No

No

No

No

Key Expansion Module (KEM)

No

No

No

No

No

No

No

Bulk Registration Support

No

No

No

No

No

No

No

Upgrading/Downgrading Phone Firmware Versions

No

No

No

No

No

No

No

Live Record

No

No

No

No

No

No

No

Enabling/Disabling KPML

No

No

No

No

No

No

No

Alias Feature

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Forward

All

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

No Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Mailbox

No

No

No

No

No

No

No

Unregistered

No

No

No

No

No

No

No

Night-Service

No

No

No

No

No

No

No

Max-Length

No

No

No

No

No

No

No

Call Forward All Softkey on Phone

No

No

No

No

No

No

No

Multicast MOH

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Unicast MOH (Supported Only on SIP phones)

No

No

No

No

No

No

No

Basic Automatic Call Distribution (B-ACD)

No

No

No

No

No

No

No

Night Service

No

No

No

No

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

No

No

No

No

No

No

No

Multiple Voice Hunt Group Join/Unjoin

No

No

No

No

No

No

No

Temporary Logout/Login From/To Voice Hunt Group Using FAC

No

No

No

No

No

No

No

Voice Hunt Group Status Message Display On Phone for Join/Unjoin

No

No

No

No

No

No

No

Channel Hunt Stop

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Hunt Group Statistics (Only for static members)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Audio Codecs

G.722

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

G.729

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

Translation Profile

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Busy Trigger Per Button

No

No

No

No

No

No

No

Conference Blocking

No

No

No

No

No

No

No

Transfer Blocking

No

No

No

No

No

No

No

COR

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Class Codec

No

No

No

No

No

No

No

Transcoding (Only supported on ISR G2)

No

No

No

No

No

No

No

Multi-VRF (Only supported on ISR G2)

No

No

No

No

No

No

No

SNMP/MIB (Supported only to get mode and number of registered phones)

No

No

No

No

No

No

No

Web GUI

No

No

No

No

No

No

No

Speed Dial

No

No

No

No

No

No

No

Busy Lamp Field (BLF)

No

No

No

No

No

No

No

Call Waiting

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Forced Authorization Code

No

No

No

No

No

No

No

HFS (HTTP Firmware Download)

No

No

No

No

No

No

No

Redial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Speakerphone (Endpoint Supports)

Dialing

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

System Message

No

No

No

No

No

No

No

Whisper Intercom

No

No

No

No

No

No

No

Abbreviated Dialing

No

No

No

No

No

No

No

After Hours

Yes

Yes

Yes

Yes

Yes

Yes

Yes

SSH to Phone

No

No

No

No

No

No

No

Span to PC

No

No

No

No

No

No

No

Web Access to Phone

No

No

No

No

No

No

No

Callback

No

No

No

No

No

No

No

## Phone Feature Support for Unified CME, Release 12.2

This section provides feature support information specific to Release 12.2 (Cisco IOS XE Fuji 16.8.1) for Cisco Unified Communications Manager Express.

Table 9: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8821

7841

8831

7861

8841

8845

8851/51NR

8861

8865

Voice Hunt Group with Shared Lines for  Unified CME on Cisco 4000 Series Integrated Services Router

Yes

Yes

All Agents Logged Out Messaged Display on SIP Phones in a Voice Hunt Group

No

Yes

Music On Hold from a Live Feed for Unified CME on Cisco 4000 Series Integrated Services Router

Yes

Yes

## Phone Feature Support for Unified E-SRST, Release 12.2

This section provides feature support information specific to Release 12.2 (Cisco IOS XE Fuji 16.8.1) for Cisco Unified Enhanced Survivable Remote Site Telephony.

Table 10: Unified E-SRST Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

Cisco Unified IP Phone 7900 Series

7811

8811

7975G

7821

8821

7965G

7841

8831

7945G

7861

8841

8845

8851/51NR

8861

8865

Voice Hunt Group Enhancements for Unified E-SRST on Cisco 4000 Series Integrated Services Router (Supported on SIP and SCCP Phones)

Yes

Yes

Yes

## Phone Feature Support for Unified SRST, Release 12.1

This section provides feature support information specific to Release 12.1 (Cisco IOS XE Fuji 16.7.1) for Cisco Unified Survivable Remote Site Telephony.

Table 11: Unified SRST Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8821

7841

8831

7861

8841

8845

8851/51NR

8861

8865

Secure SRST Support for SIP Phones on Cisco 4000 Series Integrated Services Router

Yes

Yes

Smart Licensing Support for Unified SRST

Yes

Yes

Unified SRST and Unified Border Element Colocation on Cisco 4000 Series Integrated Services Router

Yes

Yes

## Phone Feature Support for Unified CME, Unified SRST Release 12.0

This section provides feature support information specific to Release 12.0 for Cisco Unified Communications Manager Express and Cisco Unified Survivable Remote Site Telephony.

Table 12: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8821

7841

8831

7861

8841

8845

8851/51NR

8861

8865

IPv6 Support for SIP Phones on Unified SRST

Yes

Yes

Idle URL Support on SIP Phones

Yes

Yes

Called-Name Display (Dialed Number Identification Service)

Yes

Yes

Calling Number Local

Yes

Yes

cBarge for Mixed Shared Line

Yes

Yes

As part of Unified CME Release 12.0, support for Cisco Wireless IP Phone 8821, Cisco IP Phones 8845, 8865 was introduced on the 15.7(3)M Release of T-Train for the Cisco Integrated Services Routers Generation 2 (ISR G2).

## Phone Feature Support for Unified CME, Release 11.7

This section provides feature support information specific to Release 11.7 for Cisco Unified Communications Manager Express. All Unified CME Release 11.7 features are supported only on Cisco 4000 Series Integrated Services Routers.

Table 13: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8821

7841

8831

7861

8841

8845

8851/51NR

8861

8865

Transcoding support for Music on Hold (Cisco ISR 4000 Series)

Yes

Yes

Conferencing support on Unified CME (Cisco ISR 4000 Series)

Yes

Yes

Smart Licensing

NA

NA

As part of Unified CME Release 11.7, new phone support for Cisco Wireless IP Phones 8821, Cisco IP Phones 8845, 8865 was introduced for Cisco 4000 Series Integrated Services Router (On Cisco IOS XE Everest 16.5.1).

## Phone Feature Support for Unified CME, Release 11.6

This section provides feature support information specific to Release 11.6 for Cisco Unified Communications Manager Express.

Table 14: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8831

7841

8841

7861

8851/51NR

8861

B-ACD Loopback Calls

Yes

Yes

VHG Enhancements (HLog, PLK or Agent Status Control)

Yes

Yes

Secondary Dial Tone

Yes

Yes

Extension Assigner

Yes

Yes

Call Transfer Recall

Yes

Yes

Secondary CME

Yes

Yes

LTI-based Transcoding (Cisco 4000 Series ISR)

Yes

Yes

## Phone Feature Support for Unified CME, Release 11.5

This section provides feature support information specific to Release 11.5 for Cisco Unified Communications Manager Express.

Table 15: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

7811

8811

7821

8831

7841

8841

7861

8851/51NR

8861

B-ACD (SIP Phones)

Yes

Yes

Auto Registration (SIP Phones)

Yes

Yes

Night Service (SIP Phones)

Yes

Yes

## Phone Feature Support for Release 11.0

This section provides phone feature support information specific to Release 11.0 for the following products:

· Cisco Unified Communications Manager Express

· Cisco Unified Survivable Remote Site Telephony

· Cisco Unified Enhanced Survivable Remote Site Telephony

· Cisco Unified Secure Survivable Remote Site Telephony

Note: This section was last updated for Unified CME/SRST Release 11.0.

### Cisco Unified Communications Manager Express Phone Feature Support

This section provides information on phone feature support for Unified CME.

· For information on phone feature support for Unified CME Release 11.0, see Table 16.

Table 16: Unified CME Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

ATA

7811

8811

ATA-190

7821

8831

7841

8841

7861

8851/51NR

8861

Anonymous Call Block

Yes

Yes

No*

Auto-Answer

Yes

Yes

No*

Auto Register

No

No

No

Auto Assign

No

No

No

Authenticate Register

Yes

Yes

Yes

Barge

No

No

No

cBarge/Merge

Yes

Yes

No*

Call Park

Yes

Yes

No*

Call Park Resume

No

No

No

Pickup

Group Pickup

Yes

Yes

Yes

Call Pickup

Yes

Yes

Yes

Distinctive Ring for Parked Call Recall

No

No

No

Park Monitor

Yes

Yes

No*

Directed Call Park

Yes

Yes

No*

Extension Mobility

Yes

Yes

No*

Transfer

Alert/Semi-consult Transfer

Yes

Yes

Yes

Attended/Consult Transfer

Yes

Yes

Yes

Conference

Meet-Me Conference

Yes

Yes

Yes

Ad-hoc Hardware Conference                   (Only on ISR G2)

Yes

Yes

Yes

Ad-hoc Software Conference

Yes

Yes

Yes

Video Conference

No

No

No

Hold/Resume

Yes

Yes

Yes

Intercom

Yes

Yes

No*

Fast Track

Yes

Yes

Yes

Headset Answer

Yes

Yes

No*

Line Label

Yes

Yes

No*

Mobility

Yes

Yes

No*

My Phone Apps - View on Phone

Speed Dial

Yes

Yes

No*

Personal Speed Dial/Fast Dial

Yes

Yes

No*

Busy Lamp Field (BLF) Speed Dial

Yes

Yes

No*

Voice Hunt Groups

Yes

Yes

No*

After Hours

Yes

Yes

No*

Single Number Reach (SNR)

Yes

Yes

No*

Active Call Park List

Yes

Yes

No*

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

Yes

Yes

No*

Fast Dial

Yes

Yes

No*

BLF Speed Dial

Yes

Yes

No*

Single Number Reach (SNR)

Yes

Yes

No*

Park Retrieval

Yes

Yes

Yes

Paging

Multicast (Only with G711ulaw codec)

Yes

Yes

No*

Unicast (Only with G711ulaw codec)

Yes

Yes

No*

Shared Line

Yes

Yes

Yes

Mixed Shared Line

Yes

Yes

Yes

Voice Hunt Group with Shared Line

No

No

No

Caller ID Display

Yes

Yes

No*

Caller ID Blocking

No

No

No

Feature Access Code (FAC) ( Call Park, Pickup, Directed Pickup , Voice Hunt Group Join/Unjoin, and Temporary Logout/Login only)

Yes

Yes

No*

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Call forward to a Voice Hunt Group

Yes

Yes

Yes

Call Transfer Recall

No

No

No

Voicemail

Yes

Yes

Yes

Message Waiting Indicator (MWI)

Yes

Yes

No*

Video (Only SIP-SIP/SIP-SCCP Basic Call and SIP-SIP Supplementary Services)

No*

No*

No*

Locale Support

Yes

Yes

No*

Reset/Restart Phones via Reset/Restart Command

Yes

Yes

Yes

Button Layout/Softkey Template

Yes

Yes

No*

Directory Services

Local Directory

Yes

Yes

No*

Local Speed Dial

Yes

Yes

No*

Personal Speed Dial

Yes

Yes

No*

Privacy

Yes

Yes

No*

iDivert

Yes

Yes

No*

Enhanced iDivert

Yes

Yes

No*

Do Not Disturb (DND)

Yes

Yes

No*

DTMF

Yes

Yes

Yes

Feature Button/Programmable Line Key (PLK)

Yes

Yes (except 8831)

No*

Key Expansion Module (KEM)

No

Yes (only 8851/8861)

No*

Bulk Registration Support

Yes

Yes

No*

Upgrade/Downgrade Phone Firmware Versions

Yes

Yes

Yes

Secure CME

TLS

No

No

No

SRTP

No

No

No

CA

No

No

No

CAPF

No

No

No

Live Record

No

No

No

Enabling/Disabling KPML

Yes

Yes

No*

Alias Feature

No

No

No

Call-Forward

All

Yes

Yes

Yes

Busy

Yes

Yes

Yes

No Answer

Yes

Yes

Yes

Mailbox

Yes

Yes

Yes

Unregistered

Yes

Yes

Yes

Night-Service

No

No

No

Max-Length

No

No

No

Call Forward All Softkey on Phone

Yes

Yes

No*

Multicast MoH (Supported only on ISR G2)

No

No

No

Unicast MoH

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

No

No

No

Night Service

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

Yes

Yes

No*

Multiple Voice Hunt Group Join/Unjoin

Yes

Yes

No*

Temporary Logout/Login From/To Voice Hunt Group Using FAC

Yes

Yes

No*

Voice Hunt Group Status Message Display On Phone for Join/Unjoin

No

No

No

Channel Hunt Stop

Yes

Yes

No*

Voice Hunt Group Statistics (Only for static members)

Yes

Yes

Yes

Audio Codecs

G.722

Yes

Yes

No*

G.711

Yes

Yes

Yes

G.729

Yes

Yes

Yes

iLBC

Yes

Yes

No*

Translation Profile

Yes

Yes

Yes

Busy Trigger Per Button

Yes

Yes

Yes

Conference Blocking

Yes

Yes

Yes

Transfer Blocking

Yes

Yes

Yes

COR

Yes

Yes

Yes

Voice Class Codec

Yes

Yes

Yes

Transcoding (Only supported on ISR G2)

Yes

Yes

Yes

Multi-VRF (Only supported on ISR G2)

Yes

Yes

Yes

SNMP/MIB (Supported only to get mode and number of registered phones)

Yes

Yes

Yes

Web GUI

No

No

No

Speed Dial

Yes

Yes

No*

Busy Lamp Field (BLF)

Yes

Yes

No*

Call Waiting

Yes

Yes

Yes

Forced Authorization Code

Yes

Yes

Yes

HFS (HTTP Firmware Download)

Yes

Yes

No*

Redial

Yes

Yes

Yes

Speakerphone

Dialing

Yes

Yes

No*

Answering

Yes

Yes

No*

System Message

No

No

No

Whisper Intercom

No

No

No

Abbreviated Dialing

No

No

No

After Hours

Yes

Yes

Yes

SSH to Phone

Yes

Yes

No*

Span to PC

Yes

Yes (except 8831)

No*

Web Access to Phone

Yes

Yes

No*

Callback

No

No

No

### Cisco Unified Survivable Remote Site Telephony Phone Feature Support

This section provides information on phone feature support for Unified SRST.

· For information on phone specific feature support for Unified SRST Release 11.0, see Table 17.

Table 17: Unified SRST Phone Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

ATA

7811

8811

ATA-190

7821

8831

7841

8841

7861

8851/51NR

8861

8845/8865

Anonymous Call Block

No

No

No

Auto-Answer

Yes

Yes

No*

Auto Register

No

No

No

Auto Assign

No

No

No

Authenticate Register

No

No

No

Barge

No

No

No

cBarge

No

No

No

Call Park

No

No

No

Call Park Resume

No

No

No

Pickup

Group Pickup

No

No

No

Call Pickup

No

No

No

Distinctive Ring for Parked Call Recall

No

No

No

Park Monitor

No

No

No

Directed Call Park

No

No

No

Extension Mobility

No

No

No

Transfer

Alert/Semi-Consult Transfer

Yes

Yes

Yes

Attended/Consult Transfer

Yes

Yes

Yes

Conference

Meet-Me Conference

No

No

No

Ad-hoc Hardware Conference

No

No

No

Ad-hoc Software Conference

Yes

Yes

Yes

Video Conference

No

No

No

Hold/Resume

Yes

Yes

Yes

Intercom

No

No

No

Fast Track

No

No

No

Headset Answer

Yes

Yes

No*

Line Label

Yes

Yes

No*

Mobility

No

No

No

My Phone Apps - View On Phone

Speed Dial

No

No

No

Personal Speed Dial/Fast Dial

No

No

No

BLF Speed Dial

No

No

No

Voice Hunt Groups

No

No

No

After Hours

No

No

No

Single Number Reach (SNR)

No

No

No

Active Call Park List

No

No

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

No

No

Fast Dial

No

No

No

BLF Speed Dial

No

No

No

Single Number Reach (SNR)

No

No

No

Park Retrieval

No

No

No

Paging

Multicast (Only with G711ulaw codec)

No

No

No

Unicast (Only with G711ulaw codec)

No

No

No

Shared Line

No

No

No

Mixed Shared Line

No

No

No

Voice Hunt Group with Shared Line

No

No

No

Caller ID Display

Yes

Yes

No*

Caller ID Blocking

No

No

No

Feature Access Code (FAC)

No

No

No*

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Call Transfer Recall

No

No

No

Voicemail

Yes

Yes

Yes

Message Waiting Indicator (MWI)

Yes

Yes

No*

Video

No

No

No

Locale Support

No

No

No

Reset/Restart Phones via Reset/Restart Command

No

No

No

Button Layout/Softkey Template

No

No

No

Directory Services

Local Directory

No

No

No

Local Speed Dial

No

No

No

Personal Speed Dial

No

No

No

Privacy

No

No

No

iDivert

No

No

No

Enhanced iDivert

No

No

No

Do Not Disturb (DND)

Yes

Yes

No*

DTMF

Yes

Yes

Yes

Feature Button/Programmable Line Key (PLK)

Yes

Yes

No*

Key Expansion Module (KEM)

No*

Yes (only 8851/8851NR/8861)

No*

Bulk Registration Support

Yes

Yes

No*

Upgrading/Downgrading Phone Firmware Versions

No

No

No

Live Record

No

No

No

Enabling/Disabling KPML

Yes

Yes

No*

Alias Feature

Yes

Yes

Yes

Call Forward

All

Yes

Yes

Yes

Busy

Yes

Yes

Yes

No Answer

Yes

Yes

Yes

Mailbox

Yes

Yes

Yes

Unregistered

No

No

No

Night-Service

No

No

No

Max-Length

No

No

No

Call Forward All Softkey on Phone

Yes

Yes

No*

Multicast MOH (Supported only on ISR G2)

No

No

No

Unicast MOH

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

No

No

No

Night Service

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

No

No

No*

Multiple Voice Hunt Group Join/Unjoin

No

No

No*

Temporary Logout/Login From/To Voice Hunt Group Using FAC

No

No

No*

Voice Hunt Group Status Message Display On Phone for Join/Unjoin

No

No

No

Channel Hunt Stop

No

No

No

Voice Hunt Group Statistics (Only for static members)

No

No

No

Audio Codecs

G.722

Yes

Yes

No*

G.711

Yes

Yes

Yes

G.729

Yes

Yes

Yes

iLBC

Yes

Yes

No*

Translation Profile

Yes

Yes

Yes

Busy Trigger Per Button

Yes

Yes

Yes

Conference Blocking

Yes

Yes

Yes

Transfer Blocking

Yes

Yes

Yes

COR

Yes

Yes

Yes

Voice Class Codec

Yes

Yes

Yes

Transcoding (Only supported on ISR G2)

No

No

No

Multi-VRF (Only supported on ISR G2)

No

No

No

SNMP/MIB (Supported only to get mode and number of registered phones)

Yes

Yes

Yes

Web GUI

No

No

No

Speed Dial

Yes

Yes

No

Busy Lamp Field (BLF)

No

No

No

Call Waiting

Yes

Yes

Yes

Forced Authorization Code

Yes

Yes

Yes

HFS (HTTP Firmware Download)

No

No

No

Redial

Yes

Yes

Yes

Speakerphone

Dialing

Yes

Yes

No*

Answering

Yes

Yes

No*

System Message

Yes

Yes

No*

Whisper Intercom

No

No

No

Abbreviated Dialing

No

No

No

After Hours

Yes

Yes

Yes

SSH to Phone

Yes

Yes

No*

Span to PC

Yes

Yes ((except 8831)

No*

Web Access to Phone

Yes

Yes

No*

Callback

No

No

No

### Cisco Unified Enhanced Survivable Remote Site Telephony Phone Feature Support

This section provides information on phone feature support for Unified Enhanced SRST.

· For information on feature support for Unified E-SRST Release 11.0, see Table 18.

Table 18: Unified E-SRST Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

ATA

7811

8811

ATA-190

7821

8831

7841

8841

7861

8851/51NR

8861

Anonymous Call Block

No

No

No

Auto-Answer

Yes

Yes

No*

Auto Register

No

No

No

Auto Assign

No

No

No

Authenticate Register

Yes*

Yes*

Yes*

Barge

No

No

No

cBarge

No

No

No

Call Park

No

No

No

Call Park Resume

No

No

No

Pickup

Group Pickup

Yes* (using FAC)

Yes* (using FAC)

No*

Call Pickup

Yes* (using FAC)

Yes* (using FAC)

No*

Distinctive Ring for Parked Call Recall

No

No

No

Park Monitor

No

No

No

Directed Call Park

No

No

No

Extension Mobility

No

No

No

Transfer

Alert/Semi-Consult Transfer

Yes

Yes

Yes

Attended/Consult Transfer

Yes

Yes

Yes

Conference

Meet-Me Conference

No

No

No

Ad-hoc Hardware Conference

No

No

No

Ad-hoc Software Conference

Yes

Yes

Yes

Video Conference

No

No

No

Hold/Resume

Yes

Yes

Yes

Intercom

No

No

No

Fast Track

No

No

No

Headset Answer

Yes

Yes

No*

Line Label

Yes

Yes

No*

Mobility

No

No

No

My Phone Apps - View on Phone

Speed Dial

No

No

No

Personal Speed Dial/Fast Dial

No

No

No

BLF Speed Dial

No

No

No

Voice Hunt Groups

No

No

No

After Hours

No

No

No

Single Number Reach (SNR)

No

No

No

Active Call Park List

No

No

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

No

No

Fast Dial

No

No

No

BLF Speed Dial

No

No

No

Single Number Reach (SNR)

No

No

No

Park Retrieval

No

No

No

Paging

Multicast (Only with G711ulaw codec)

No

No

No

Unicast (Only with G711ulaw codec)

No

No

No

Shared Line

Yes

Yes (except 8831)

No*

Mixed Shared Line

Yes

Yes (except 8831)

No*

Voice Hunt Group with Shared Line

No

No

No

Caller ID Display

Yes

Yes

No*

Caller ID Blocking

No

No

No

Feature Access Code (FAC) ( Only for Voice Hunt Group Join/Unjoin, and Temporary Logout/Login Only)

Yes*

Yes*

No*

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Call Transfer Recall

No

No

No

Voicemail

Yes

Yes

Yes

Message Waiting Indicator (MWI)

Yes

Yes

No*

Video (Only SIP-SIP/SIP-SCCP Basic Call and SIP-SIP Supplementary Services)

No*

No*

No*

Locale Support

No

No

No

Reset/Restart Phones via Reset/Restart Command

No

No

No

Button Layout/Softkey Template

No

No

No

Directory Services

Local Directory

No

No

No

Local Speed Dial

No

No

No

Personal Speed Dial

No

No

No

Privacy (On Hold)

Yes*

Yes*

No*

iDivert

No

No

No

Enhanced iDivert

No

No

No

Do Not Disturb (DND)

Yes

Yes

No*

DTMF

Yes*

Yes*

Yes*

Feature Button/Programmable Line Key (PLK)

Yes

Yes

No*

Key Expansion Module (KEM)

No

Yes (only 8851/8851NR/8861)

No*

Bulk Registration Support

Yes

Yes

No*

Upgrading/Downgrading Phone Firmware Versions

No

No

No

Live Record

No

No

No

Enabling/Disabling KPML

Yes*

Yes*

No*

Alias Feature

No

No

No

Call Forward

All

Yes

Yes

Yes

Busy

Yes

Yes

Yes

No answer

Yes

Yes

Yes

Mailbox

Yes

Yes

Yes

Unregistered

No

No

No

Night-Service

No

No

No

Max-Length

No

No

No

Call Forward All Softkey on Phone

Yes

Yes

No*

Multicast MOH (Supported only on G2 routers)

No

No

No

Unicast MOH

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

No

No

No

Night Service

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

Yes*

Yes*

No*

Multiple Voice Hunt Group Join/Unjoin

Yes*

Yes*

No*

Temporary Logout/Login From/To Voice Hunt Group Using FAC

Yes*

Yes*

No*

Voice Hunt Group Status Message Display on Phone for Join/Unjoin

No

No

No

Channel Hunt Stop

No

No

No

Voice Hunt Group Statistics (Only for static members)

Yes

Yes

Yes

Audio Codecs

G.722

Yes

Yes

No*

G.711

Yes

Yes

Yes

G.729

Yes

Yes

Yes

iLBC

Yes

Yes

No*

Translation Profile

Yes*

Yes*

Yes*

Busy Trigger Per Button

Yes*

Yes*

Yes*

Conference Blocking

Yes*

Yes*

Yes*

Transfer Blocking

Yes*

Yes*

Yes*

COR

Yes

Yes

Yes

Voice Class Codec

Yes*

Yes*

Yes*

Transcoding (Only supported on ISR G2)

No

No

No

Multi-VRF (Only supported on ISR G2)

No

No

No

SNMP/MIB (Supported only to get mode and number of registered phones)

Yes

Yes

Yes

Web GUI

No

No

No

Speed Dial

Yes

Yes

No*

Busy Lamp Field (BLF)

Yes*

Yes*

No*

Call Waiting

Yes

Yes

Yes

Forced Authorization Code

Yes*

Yes*

Yes*

HFS (HTTP Firmware Download)

No

No

No

Redial

Yes

Yes

Yes

Speakerphone

Dialing

Yes

Yes

No*

Answering

Yes

Yes

No*

System Message

Yes*

Yes*

No*

Whisper Intercom

No

No

No

Abbreviated Dialing

No

No

No

After Hours

Yes

Yes

Yes

SSH to Phone

Yes

Yes

No*

Span to PC

Yes

Yes ((except 8831)

No*

Web Access to Phone

Yes

Yes

No*

Callback

No

No

No

### Cisco Unified Secure Survivable Remote Site Telephony Phone Feature Support

This section provides information on the phone feature support for Unified Secure SRST.

· For information on the phone feature support for Unified Secure SRST Release 11.0, see Table 19.

Table 19: Unified Secure SRST Feature Support

Features

Phone Models

Cisco IP Phone 7800 Series

Cisco IP Phone 8800 Series

ATA

7811

8811

ATA-190

7821

8831

7841

8841

7861

8851/51NR

8861

Basic Registration in Secure Mode

Yes

Yes

No*

Basic Registration in Non Secure Mode

Yes

Yes

No*

Hold/Resume

Yes

Yes

No*

Transfer

Alert/Semi-Consult Transfer

Local

Yes

Yes

No*

Over Trunk

Yes

Yes

No*

Between Secure and Non-Secure Phones

Yes

Yes

No*

Attended/ Consult Transfer

Local

Yes

Yes

No*

Over Trunk

Yes

Yes

No*

Between Secure and Non-Secure Phone

Yes

Yes

No*

Ad-hoc Software Conference

Local Endpoints

Yes

Yes

No*

Over Trunk

Yes

Yes

No*

Between Secure and Non-Secure Endpoints

Yes

Yes

No*

Video Conference

No

No

No

Call Forward

All

Yes

Yes

No*

Busy

Yes

Yes

No*

No Answer

Yes

Yes

No*

## Phone Feature Support (Prior to Release 11.0)

This section provides information on phone feature support for releases prior to Release 11.0.

### Unified CME Support (Prior to Release 11.0)

For information on phone feature support for Unified CME releases prior to Release 11.0, see Table 20 and Table 21.

Table 20: Unified CME SIP Phone Feature Support (for Unified CME releases 8.8 to 10.5)

Features

SIP Phone Models

3905

6901

6921

8941

DX650

7821

7962

9951

ATA-187

6911

6941

8945

7841

7965

9971

6945

8961

7861

7975

6961

Anonymous Call Block

No*

No*

No*

Yes

Yes

Yes

No*

Yes

No*

Auto-Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Auto Register

No

No

No

No

No

No

No

No

No

Auto Assign

No

No

No

No

No

No

No

No

No

Authenticate Register

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Barge

No

No

No

No

No

No

No

No

No

cBarge/Merge

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Call Park

No*

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Call Park Resume

No

No

No

No

No

No

No

No

No

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

Yes

Call Pickup

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Distinctive Ring for Parked Call Recall

No

No

No

No

No

No

No

No

No

Park Monitor

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Directed Call Park

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Extension Mobility

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Transfer

Alert/Semi-Consult Transfer

Yes

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

Yes

Conference

Meet-Me Conference

No*

Yes (only on 6911)

Yes

Yes

No*

Yes

Yes

Yes

Yes

Ad-hoc Hardware Conference (Only on ISR G2)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Ad-hoc Software Conference

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Video Conference

No

No

No

No

No

No

No

No

No

Hold/Resume

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Intercom

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Fast Track

No

No

No

No

No

No

No

No

No

Headset Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Line Label

No*

No*

No*

Yes

Yes

Yes

Yes

Yes

No*

Mobility

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

My Phone Apps - View on Phone

Speed Dial

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Personal Speed Dial/ Fast Dial

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

BLF Speed Dial

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Voice Hunt Groups

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

After Hours

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Single Number Reach (SNR)

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Active Call Park List

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Fast Dial

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

BLF Speed Dial

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Single Number Reach (SNR)

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Park Retrieval

Yes

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

No*

Yes (only on 6911)

Yes

Yes

No*

Yes

Yes

Yes

No*

Unicast (Only with G711ulaw codec)

No*

Yes (only on 6911)

Yes

Yes

No*

Yes

Yes

Yes

No*

Shared Line

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Mixed Shared Line

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Hunt Group with Shared Line

No

No

No

No

No

No

No

No

No

Caller ID Display

Yes

Yes (only on 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Caller ID Blocking

No

No

No

No

No

No

No

No

No

Feature Access Code (FAC) ( Call Park, Pickup, Directed Pickup , Voice Hunt Group Join/Unjoin, and Temporary Logout/Login Only)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer Recall

No

No

No

No

No

No

No

No

No

Voicemail

Yes

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

Yes

No*

Video (Only SIP-SIP/SIP-SCCP Basic Call and SIP-SIP Supplementary Services)

No*

No*

No*

Yes (except 8961)

Yes

No*

No*

Yes

No*

Locale Support

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Reset/Restart Phones via Reset/Restart Command

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Button Layout/Softkey Template

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Directory Services

Local Directory

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Local Speed Dial

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Personal Speed Dial

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

No*

Privacy

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Immediate Divert (iDivert)

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Enhanced iDivert

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Do Not Disturb (DND)

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

DTMF

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Feature Button / Programmable Line Keys (PLK)

No*

Yes (only on 6911)

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

No*

Key Expansion Module (KEM)

No*

No*

No*

Yes (only on 8961)

No*

No*

No*

Yes

No*

Bulk Registration Support

No*

No*

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

No*

Upgrading/Downgrading Phone Firmware Versions

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Secure CME

TLS

No

No

No

No

No

No

No

No

No

SRTP

No

No

No

No

No

No

No

No

No

CA

No

No

No

No

No

No

No

No

No

CAPF

No

No

No

No

No

No

No

No

No

Live Record

No

No

No

No

No

No

No

No

No

Enabling/Disabling KPML

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Alias Feature

No

No

No

No

No

No

No

No

No

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

Yes

Mailbox

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Unregistered

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Night Service

No

No

No

No

No

No

No

No

No

Max-Length

No

No

No

No

No

No

No

No

No

Call Forward All Softkey on Phone

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Multicast MOH (Supported only on ISR G2)

No

No

No

No

No

No

No

No

No

Unicast MOH

Yes

Yes

Yes

Yes

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

Yes

Yes

Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Multiple Voice Hunt Group Join/Unjoin

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Temporary Logout/Login From/To Voice Hunt Group Using FAC

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Voice Hunt Group Status Message Display On Phone for Join/Unjoin

No

No

No

No

No

No

No

No

No

Channel Hunt Stop

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Voice Hunt Group Statistics (Only for Static Members)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Audio Codecs

G.722

No*

No*

No*

Yes

Yes

Yes

Yes

Yes

No*

G.711

Yes

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

Yes

iLBC

No*

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Translation Profile

Yes

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

Yes

Voice Class Codec

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Transcoding (Only supported on ISR G2)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Multi-VRF (Only supported on ISR G2)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

SNMP/MIB (Supported only to get mode and number of registered phones)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Web GUI

No

No

No

No

No

No

No

No

No

Speed Dial

No*

Yes (only on 6911)

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

Yes

Busy Lamp Field (BLF)

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Call Waiting

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Forced Authorization Code

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

HFS (HTTP Firmware Download)

No

No

Yes

Yes

No*

Yes

Yes

Yes

No*

Redial

Yes

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

Yes (only on 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Answering

Yes

Yes (only on 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

System Message

No

No

No

No

No

No

No

No

No

Whisper Intercom

No

No

No

No

No

No

No

No

No

Abbreviated Dialing

No

No

No

No

No

No

No

No

No

After Hours

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

SSH to Phone

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Span to PC

Yes

Yes (only on 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Web Access to Phone

Yes

Yes (only on 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Callback

No

No

No

No

No

No

No

No

No

· For information on SCCP phone feature support for Unified CME releases prior to Release 11.0, see Table 21 .

Table 21: Unified CME SCCP Phone Feature Support (for Unified CME Releases 8.8 to 10.5)

Features

SCCP Phone Models

6941

7925

7926

8941

6945

7942

8945

6961

7931

7962

7965

7975

Anonymous Call Block

No

No

No

Auto-Answer

Yes

Yes

Yes

Auto Register

Yes

Yes

Yes

Auto Assign

Yes

Yes

Yes

Authenticate Register

No

No

No

Barge

Yes

Yes

Yes

cBarge/Merge

Yes

Yes

Yes

Call Park

Yes

Yes

Yes

Call Park Resume

No

No

No

Pickup

Group Pickup

Yes

Yes

Yes

Call Pickup

Yes

Yes

Yes

Distinctive Ring for Parked Call Recall

Yes

Yes

Yes

Park Monitor

Yes

Yes

Yes

Directed Call Park

Yes

Yes

Yes

Extension Mobility

Yes

Yes

Yes

Transfer

Alert/Semi-consult Transfer

Yes

Yes

Yes

Attended/Consult Transfer

Yes

Yes

Yes

Blind Transfer

Yes

Yes

Yes

Conference

Meet-Me Conference

Yes

Yes

Yes

Ad-hoc Hardware Conference (Only on ISR G2)

Yes

Yes

Yes

Ad-hoc Software Conference

Yes

Yes

Yes

Video Conference

No

No

No

Hold/Resume

Yes

Yes

Yes

Intercom

Yes

Yes

Yes

Fast Track

No

No

No

Headset Answer

Yes

Yes

Yes

Line Label

No*

Yes

Yes

Mobility

Yes

Yes

Yes

My Phone Apps - View on Phone

Speed Dial

Yes

Yes      (except 7931)

Yes

Personal Speed Dial/ Fast Dial

Yes

Yes  (except 7931)

Yes

BLF Speed Dial

Yes

Yes (except 7931)

Yes

Voice Hunt Groups

Yes

Yes (except 7931)

Yes

After Hours

Yes

Yes (except 7931)

Yes

Single Number Reach (SNR)

Yes

Yes (except 7931)

Yes

Active Call Park List

Yes

Yes (except 7931)

Yes

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

Yes

Yes (except 7931)

Yes

Fast Dial

Yes

Yes (except 7931)

Yes

BLF Speed Dial

Yes

Yes (except 7931)

Yes

Single Number Reach (SNR)

Yes

Yes

Yes

Park Retrieval

Yes

Yes

Yes

Paging

Multicast (Only with G711ulaw codec)

Yes

Yes

Yes

Unicast (Only with G711ulaw codec)

Yes

Yes

Yes

Shared Line

Yes

Yes

Yes

Mixed Shared Line

Yes

Yes

Yes

Voice Hunt Group with Shared Line

Yes

Yes

Yes

Caller ID Display

Yes

Yes

Yes

Caller ID Blocking

Yes

Yes

Yes

Feature Access Code (FAC)

Yes

Yes

Yes

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Call Transfer Recall

Yes

Yes

Yes

Voicemail

Yes

Yes

Yes

Message Waiting Indicator (MWI)

Yes

Yes

Yes

Video (Only SCCP-SCCP and SCCP-SIP Basic Call and SCCP-SCCP Supplementary Services)

No*

No*

Yes

Locale Support

Yes

Yes

Yes

Reset/Restart Phones via Reset/Restart Command

Yes

Yes

Yes

Button Layout/Softkey Template

Yes

Yes

Yes

Directory Services

Local Directory

Yes

Yes

Yes

Local Speed Dial

Yes

Yes

Yes

Personal Speed Dial

Yes

Yes

Yes

Privacy

Yes

Yes

Yes

Transfer to Voice Mail (TrnsfVM)

Yes

Yes

Yes

Do Not Disturb (DND)

Yes

Yes

Yes

DTMF

Yes

Yes

Yes

Feature Button/Programmable Line Keys (PLK)

Yes

Yes

Yes

Key Expansion Module (KEM)

No*

Yes (only on 7962/7965/7975)

Yes

Bulk Registration Support

No

No

No

Upgrading/Downgrading Phone Firmware Versions

Yes

Yes

Yes

Secure CME

TLS

Yes

Yes

Yes

SRTP

Yes

Yes

Yes

CA

Yes

Yes

Yes

CAPF

Yes

Yes

Yes

Live Record

Yes

Yes

Yes

Enabling/Disabling KPML

No

No

No

Alias Feature

No

No

No

Call Forward

All

Yes

Yes

Yes

Busy

Yes

Yes

Yes

No Answer

Yes

Yes

Yes

Mailbox

No

No

No

Unregistered

No

No

No

Night Service

Yes

Yes

Yes

Max-Length

Yes

Yes

Yes

Multicast MOH (Supported only on ISR G2)

Yes

Yes

Yes

Unicast MOH (except SCCP to SCCP)

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

Yes

Yes

Yes

Night Service

Yes

Yes

Yes

Voice Hunt Group

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

Yes

Yes

Yes

Voice Hunt Group Status Message Display on Phone for Join/Unjoin

Yes

Yes

Yes

Multiple Voice Hunt Group Join/Unjoin

Yes

Yes

Yes

Voice Hunt Group Temporary Logout/Login Using FAC

Yes

Yes

Yes

Channel Hunt Stop

Yes

Yes

Yes

Voice Hunt Group Statistics

Yes

Yes

Yes

Ephone Hunt Group

Yes

Yes

Yes

Ephone Hunt Group Dynamic Join/Unjoin

Yes

Yes

Yes

Ephone Hunt Group Status Message Display on Phone for Join/Unjoin

Yes

Yes

Yes

Ephone Hunt Group Temporary Logout/Login using HLog/FAC Softkey

Yes

Yes

Yes

Ephone Hunt Group Statistics

Yes

Yes

Yes

Audio Codecs

G.722

Yes

Yes

Yes

G.711

Yes

Yes

Yes

G.729

Yes

Yes

Yes

iLBC

Yes

Yes

Yes

Translation Profile

Yes

Yes

Yes

Busy Trigger Per Button

Yes

Yes

Yes

Conference Blocking

Yes

Yes

Yes

Transfer Blocking

Yes

Yes

Yes

COR

Yes

Yes

Yes

Voice Class Codec

No

No

No

Transcoding (Only supported on ISR G2)

Yes

Yes

Yes

Multi-VRF (Only supported on ISR G2)

Yes

Yes

Yes

SNMP/MIB

Yes

Yes

Yes

Web GUI

Yes

Yes

Yes

Speed Dial

Yes

Yes

Yes

Busy Lamp Field (BLF)

Yes

Yes

Yes

Call Waiting

Yes

Yes

Yes

Forced Authorization Code

Yes

Yes

Yes

HFS (HTTP Firmware Download)

No

No

No

Redial

Yes

Yes

Yes

Speakerphone

Dialing

Yes

Yes

Yes

Answering

Yes

Yes

Yes

System Message

No*

Yes

Yes

Whisper Intercom

Yes

Yes

Yes

Intercom

Yes

Yes

Yes

Abbreviated Dialing

Yes

Yes

Yes

After Hours

Yes

Yes

Yes

SSH to Phone

No

Yes

Yes

Span to PC

Yes

Yes

Yes

Web Access to Phone

Yes

Yes

Yes

Overlay DN

Yes

Yes

Yes

Callback

Yes

Yes

Yes

Feature Blocking (CFwdAll,  Confrn, GpickUp, Park, PickUp, Trnsfer)

Yes

Yes

Yes

### Cisco Unified SRST Support (Prior to Release 11.0)

For information on phone feature support for Unified SRST releases prior to Release 11.0, see Table 22 and Table 23 .

Table 22: Unified SRST Phone Feature Support (for Unified SRST Releases 10.5 and Prior)

Features

SIP Phone Models

3905

6901

6921

8941

DX650

7821

7962

Cisco IP Phone 8800 Series

9951

ATA-187

6911

6941

8945

7841

7965

9971

6945

8961

7861

7975

6961

Anonymous Call Block

No

No

No

No

No

No

No

No

No

No

Auto-Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Auto Register

No

No

No

No

No

No

No

No

No

No

Auto Assign

No

No

No

No

No

No

No

No

No

No

Authenticate Register

No

No

No

No

No

No

No

No

No

No

Barge

No

No

No

No

No

No

No

No

No

No

cBarge/Merge

No

No

No

No

No

No

No

No

No

No

Call Park

No

No

No

No

No

No

No

No

No

No

Call Park Resume

No

No

No

No

No

No

No

No

No

No

Pickup

Group Pickup

No

No

No

No

No

No

No

No

No

No

Call Pickup

No

No

No

No

No

No

No

No

No

No

Distinctive Ring for Parked Call Recall

No

No

No

No

No

No

No

No

No

No

Park Monitor

No

No

No

No

No

No

No

No

No

No

Directed Call Park

No

No

No

No

No

No

No

No

No

No

Extension Mobility

No

No

No

No

No

No

No

No

No

No

Transfer

Alert/Semi-Consult Transfer

Yes

Yes

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

Yes

Yes

Conference

Meet-Me Conference

No

No

No

No

No

No

No

No

No

No

Ad-hoc Hardware Conference

No

No

No

No

No

No

No

No

No

No

Ad-hoc Software Conference

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Video Conference

No

No

No

No

No

No

No

No

No

No

Hold/Resume

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Intercom

No

No

No

No

No

No

No

No

No

No

Fast Track

No

No

No

No

No

No

No

No

No

No

Headset Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Line Label

No*

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Mobility

No

No

No

No

No

No

No

No

No

No

My Phone Apps - View on Phone

Speed Dial

No

No

No

No

No

No

No

No

No

No

Personal Speed Dial/ Fast Dial

No

No

No

No

No

No

No

No

No

No

BLF Speed Dial

No

No

No

No

No

No

No

No

No

No

Voice Hunt Groups

No

No

No

No

No

No

No

No

No

No

After Hours

No

No

No

No

No

No

No

No

No

No

Single Number Reach (SNR)

No

No

No

No

No

No

No

No

No

No

Active Call Park List

No

No

No

No

No

No

No

No

No

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

No

No

No

No

No

No

No

No

No

Fast Dial

No

No

No

No

No

No

No

No

No

No

BLF Speed Dial

No

No

No

No

No

No

No

No

No

No

Single Number Reach (SNR)

No

No

No

No

No

No

No

No

No

No

Park Retrieval

No

No

No

No

No

No

No

No

No

No

Paging

Multicast (Only with G711ulaw codec)

No

No

No

No

No

No

No

No

No

No

Unicast (Only with G711ulaw codec)

No

No

No

No

No

No

No

No

No

No

Shared Line

No

No

No

No

No

No

No

No

No

No

Mixed Shared Line

No

No

No

No

No

No

No

No

No

No

Voice Hunt Group with Shared Line

No

No

No

No

No

No

No

No

No

No

Caller ID Display

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Caller ID Blocking

No

No

No

No

No

No

No

No

No

No

Feature Access Code (FAC) ( Only for Voice Hunt Group Join/Unjoin, and Temporary Logout/Login Only)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer Recall

No

No

No

No

No

No

No

No

No

No

Voicemail

Yes

Yes

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

Yes

Yes

No*

Video

No

No

No

No

No

No

No

No

No

No

Locale Support

No

No

No

No

No

No

No

No

No

No

Reset/Restart Phones via Reset/Restart Command

No

No

No

No

No

No

No

No

No

No

Button Layout/Softkey Template

No

No

No

No

No

No

No

No

No

No

Directory Services

Local Directory

No

No

No

No

No

No

No

No

No

No

Local Speed Dial

No

No

No

No

No

No

No

No

No

No

Personal Speed Dial

No

No

No

No

No

No

No

No

No

No

Privacy

No

No

No

No

No

No

No

No

No

No

Immediate Divert (iDivert)

No

No

No

No

No

No

No

No

No

No

Enhanced iDivert

No

No

No

No

No

No

No

No

No

No

Do Not Disturb (DND)

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

DTMF

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Feature Button / Programmable Line Keys (PLK)

No*

Yes (only on 6911)

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Key Expansion Module (KEM)

No*

No*

No*

Yes (only 8961)

No*

No*

No*

No*

Yes

No*

Bulk Registration Support

No*

No*

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Upgrading/Downgrading Phone Firmware Versions

No

No

No

No

No

No

No

No

No

No

Secure CME

TLS

No

No

No

No

No

No

No

No

No

No

SRTP

No

No

No

No

No

No

No

No

No

No

CA

No

No

No

No

No

No

No

No

No

No

CAPF

No

No

No

No

No

No

No

No

No

No

Live Record

No

No

No

No

No

No

No

No

No

No

Enabling/Disabling KPML

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Alias Feature

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

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

Yes

Yes

Mailbox

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Unregistered

No

No

No

No

No

No

No

No

No

No

Night Service

No

No

No

No

No

No

No

No

No

No

Max-Length

No

No

No

No

No

No

No

No

No

No

Call Forward All Softkey on Phone

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Multicast MOH (Supported only on ISR G2)

No

No

No

No

No

No

No

No

No

No

Unicast MOH

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

No

No

No

No

No

No

No

No

No

No

Night Service

No

No

No

No

No

No

No

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Multiple Voice Hunt Group Join/Unjoin

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Temporary Logout/Login From/To Voice Hunt Group Using FAC

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Voice Hunt Group Status Message Display on Phone for Join/Unjoin

No

No

No

No

No

No

No

No

No

No

Channel Hunt Stop

No

No

No

No

No

No

No

No

No

No

Voice Hunt Group Statistics (Only for Static Members)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Audio Codecs

G.722

No*

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

G.711

Yes

Yes

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

Yes

Yes

iLBC

No*

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Translation Profile

Yes

Yes

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

Yes

Yes

Voice Class Codec

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Transcoding (Only supported on ISR G2)

No

No

No

No

No

No

No

No

No

No

Multi-VRF (Only supported on ISR G2)

No

No

No

No

No

No

No

No

No

No

SNMP/MIB (Supported only to get mode and number of registered phones)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Web GUI

No

No

No

No

No

No

No

No

No

No

Speed Dial

No*

Yes (only on 6911)

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

Yes

No

Busy Lamp Field (BLF)

No

No

No

No

No

No

No

No

No

No

Call Waiting

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Forced Authorization Code

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

HFS (HTTP Firmware Download)

No

No

No

No

No

No

No

No

No

No

Redial

Yes

Yes

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

Yes (only 6911)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Answering

Yes

Yes (only 6911)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

System Message

No*

No*

Yes

Yes

No*

Yes

Yes

Yes

Yes

No*

Whisper Intercom

No

No

No

No

No

No

No

No

No

No

Abbreviated Dialing

No

No

No

No

No

No

No

No

No

No

After Hours

No

No

No

No

No

No

No

No

No

No

SSH to phone

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Span to PC

Yes

Yes (only 6911)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Web Access to Phone

Yes

Yes (only 6911)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Callback

No

No

No

No

No

No

No

No

No

No

For information on SCCP phone feature support for Unified SRST releases prior to Release 11.0, see Table 23 .

Table 23 : Unified SRST SCCP Phone Feature Support (for Unified SRST Releases 10.5 and Prior)

Features

SCCP Phone Models

6941

7925

7926

8941

6945

7942

8945

6961

7931

7962

7965

7975

Anonymous Call Block

No

No

No

Auto-Answer

Yes

Yes

Yes

Auto Register

No

No

No

Auto Assign

No

No

No

Authenticate Register

No

No

No

Barge

No

No

No

cBarge/Merge

No

No

No

Call Park

No

No

No

Call Park Resume

No

No

No

Pickup

Group Pickup

No

No

No

Call Pickup

No

No

No

Distinctive Ring for Parked Call Recall

No

No

No

Park Monitor

No

No

No

Directed Call Park

No

No

No

Extension Mobility

No

No

No

Transfer

Alert/Semi-consult Transfer

Yes

Yes

Yes

Attended/Consult Transfer

Yes

Yes

Yes

Blind Transfer

Yes

Yes

Yes

Conference

Meet-Me Conference

No

No

No

Ad-hoc Hardware Conference

No

No

No

Ad-hoc Software Conference

Yes

Yes

Yes

Video Conference

No

No

No

Hold/Resume

Yes

Yes

Yes

Intercom

No

No

No

Fast Track

No

No

No

Headset Answer

Yes

Yes

Yes

Line Label

No*

Yes

Yes

Mobility

No

No

No

My Phone Apps - View on Phone

Speed Dial

No

No

No

Personal Speed Dial/ Fast Dial

No

No

No

BLF Speed Dial

No

No

No

Voice Hunt Groups

No

No

No

After Hours

No

No

No

Single Number Reach (SNR)

No

No

No

Active Call Park List

No

No

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

No

No

Fast Dial

No

No

No

BLF Speed Dial

No

No

No

Single Number Reach (SNR)

No

No

No

Park Retrieval

No

No

No

Paging

Multicast (Only with G711ulaw codec)

No

No

No

Unicast (Only with G711ulaw codec)

No

No

No

Shared Line

Yes

Yes

Yes

Mixed Shared Line

No

No

No

Voice Hunt Group with Shared Line

Yes

Yes

Yes

Caller ID Display

Yes

Yes

Yes

Caller ID Blocking

No

No

No

Feature Access Code (FAC)

Yes

Yes

Yes

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Call Transfer Recall

No

No

No

Voicemail

Yes

Yes

Yes

Message Waiting Indicator (MWI)

Yes

Yes

Yes

Video

No

No

No

Locale Support

No

No

No

Reset/Restart Phones via Reset/Restart Command

Yes

Yes

Yes

Button Layout/Softkey Template

No

No

No

Directory Services

Local Directory

No

No

No

Local Speed Dial

No

No

No

Personal Speed Dial

No

No

No

Privacy

No

No

No

Transfer to Voice Mail (TrnsfVM)

No

No

No

Do Not Disturb (DND)

Yes

Yes

Yes

DTMF

No

No

No

Feature Button/Programmable Line Keys (PLK)

Yes

Yes

Yes

Key Expansion Module (KEM)

No*

Yes (only on 7962/7965/7975)

Yes

Bulk Registration Support

No

No

No

Upgrading/Downgrading Phone Firmware Versions

No

No

No

Secure CME

TLS

Yes

Yes

Yes

SRTP

Yes

Yes

Yes

CA

Yes

Yes

Yes

CAPF

Yes

Yes

Yes

Live Record

No

No

No

Enabling/Disabling KPML

No

No

No

Alias Feature

Yes

Yes

Yes

Call-Forward

All

Yes

Yes

Yes

Busy

Yes

Yes

Yes

No Answer

Yes

Yes

Yes

Mailbox

No

No

No

Unregistered

No

No

No

Night Service

No

No

No

Max-Length

No

No

No

Multicast MOH (Supported only on ISR G2)

Yes

Yes

Yes

Unicast MOH (except SCCP to SCCP)

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

Yes

Yes

Yes

Night Service

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

No

No

No

Voice Hunt Group Status Message Display on Phone for Join/Unjoin

No

No

No

Multiple Voice Hunt Group Join/Unjoin

No

No

No

Voice Hunt Group Temporary Logout/Login Using FAC

No

No

No

Channel Hunt Stop

No

No

No

Voice Hunt Group Statistics

Yes

Yes

Yes

Ephone Hunt Group

No

No

No

Ephone Hunt Group Dynamic Join/Unjoin

No

No

No

Ephone Hunt Group Status Message Display on Phone for Join/Unjoin

No

No

No

Ephone Hunt Group Temporary Logout/Login Using HLog/FAC Softkey

No

No

No

Ephone Hunt Group Statistics

No

No

No

Audio Codecs

G.722

Yes

Yes

Yes

G.711

Yes

Yes

Yes

G.729

Yes

Yes

Yes

iLBC

Yes

Yes

Yes

Translation Profile

Yes

Yes

Yes

Busy Trigger Per Button

No

No

No

Conference Blocking

No

No

No

Transfer Blocking

No

No

No

COR

Yes

Yes

Yes

Voice Class Codec

No

No

No

Transcoding (Only supported on ISR G2)

No

No

No

Multi-VRF (Only supported on ISR G2)

No

No

No

SNMP/MIB

Yes

Yes

Yes

Web GUI

Yes

Yes

Yes

Speed Dial

Yes

Yes

Yes

Busy Lamp Field (BLF)

No

No

No

Call Waiting

Yes

Yes

Yes

Forced Authorization Code

Yes

Yes

Yes

HFS (HTTP Firmware Download)

No

No

No

Redial

Yes

Yes

Yes

Speakerphone

Dialing

Yes

Yes

Yes

Answering

Yes

Yes

Yes

System Message

Yes

Yes

Yes

Whisper Intercom

No

No

No

Intercom

No

No

No

Abbreviated Dialing

No

No

No

After Hours

Yes

Yes

Yes

SSH to Phone

No

Yes

Yes

Span to PC

Yes

Yes

Yes

Web Access to Phone

Yes

Yes

Yes

Overlay DN

No

No

No

Callback

No

No

No

Feature Blocking (CFwdAll,  Confrn, GpickUp, Park, PickUp, Trnsfer)

No

No

No

### Cisco Unified E-SRST Support (Prior to Release 11.0)

For information on phone feature support for Unified E-SRST releases prior to Release 11.0, see Table 24 and Table 25 .

Table 24 : Unified E-SRST SIP Phone Feature Support (for Unified SRST Releases 10.5 and Prior)

Features

SIP Phone Models

3905

6901

6921

8941

DX650

7821

7962

9951

ATA-187

6911

6941

8945

7841

7965

9971

6945

8961

7861

7975

6961

Anonymous Call Block

No

No

No

No

No

No

No

No

No

Auto-Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Auto Register

No

No

No

No

No

No

No

No

No

Auto Assign

No

No

No

No

No

No

No

No

No

Authenticate Register

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Barge

No

No

No

No

No

No

No

No

No

cBarge/Merge

No

No

No

No

No

No

No

No

No

Call Park

No

No

No

No

No

No

No

No

No

Call Park Resume

No

No

No

No

No

No

No

No

No

Pickup (Only Using FAC)

Group Pickup

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

No*

Call Pickup

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

No*

Distinctive Ring for Parked Call Recall

No

No

No

No

No

No

No

No

No

Park Monitor

No

No

No

No

No

No

No

No

No

Directed Call Park

No

No

No

No

No

No

No

No

No

Extension Mobility

No

No

No

No

No

No

No

No

No

Transfer

Alert/Semi-Consult Transfer

Yes

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

Yes

Conference

Meet-Me Conference

No

No

No

No

No

No

No

No

No

Ad-hoc Hardware Conference

No

No

No

No

No

No

No

No

No

Ad-hoc Software Conference

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Video Conference

No

No

No

No

No

No

No

No

No

Hold/Resume

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Intercom

No

No

No

No

No

No

No

No

No

Fast Track

No

No

No

No

No

No

No

No

No

Headset Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Line Label

No*

No*

No*

Yes

Yes

Yes

Yes

Yes

No*

Mobility

No

No

No

No

No

No

No

No

No

My Phone Apps - View on Phone

Speed Dial

No

No

No

No

No

No

No

No

No

Personal Speed Dial/ Fast Dial

No

No

No

No

No

No

No

No

No

BLF Speed Dial

No

No

No

No

No

No

No

No

No

Voice Hunt Groups

No

No

No

No

No

No

No

No

No

After Hours

No

No

No

No

No

No

No

No

No

Single Number Reach (SNR)

No

No

No

No

No

No

No

No

No

Active Call Park List

No

No

No

No

No

No

No

No

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

No

No

No

No

No

No

No

No

Fast Dial

No

No

No

No

No

No

No

No

No

BLF Speed Dial

No

No

No

No

No

No

No

No

No

Single Number Reach (SNR)

No

No

No

No

No

No

No

No

No

Park Retrieval

No

No

No

No

No

No

No

No

No

Paging

Multicast (Only with G711ulaw codec)

No

No

No

No

No

No

No

No

No

Unicast (Only with G711ulaw codec)

No

No

No

No

No

No

No

No

No

Shared Line

No*

No*

No*

Yes

No*

Yes

No*

Yes

No

Mixed Shared Line

No*

No*

No*

Yes

No*

Yes

No*

Yes

No

Voice Hunt Group with Shared Line

No

No

No

No

No

No

No

No

No

Caller ID Display

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Caller ID Blocking

No

No

No

No

No

No

No

No

No

Feature Access Code (FAC) ( Only for Voice Hunt Group Join/Unjoin, and Temporary Logout/Login Only)

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

No*

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Transfer Recall

No

No

No

No

No

No

No

No

No

Voicemail

Yes

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

Yes

No*

Video (Only SIP-SIP/SIP-SCCP Basic Call and SIP-SIP Supplementary Services)

No*

No*

No*

Yes* (except 8861)

No

No*

No*

Yes*

No*

Locale Support

No

No

No

No

No

No

No

No

No

Reset/Restart Phones via Reset/Restart Command

No

No

No

No

No

No

No

No

No

Button Layout/Softkey Template

No

No

No

No

No

No

No

No

No

Directory Services

Local Directory

No

No

No

No

No

No

No

No

No

Local Speed Dial

No

No

No

No

No

No

No

No

No

Personal Speed Dial

No

No

No

No

No

No

No

No

No

Privacy(On Hold)

No*

No*

No*

Yes*

No*

Yes*

No*

Yes*

No*

Immediate Divert (iDivert)

No

No

No

No

No

No

No

No

No

Enhanced iDivert

No

No

No

No

No

No

No

No

No

Do Not Disturb (DND)

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

DTMF

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Feature Button / Programmable Line Keys (PLK)

No*

Yes (only on 6911)

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

No*

Key Expansion Module (KEM)

No*

No*

No*

Yes (only 8961)

No*

No*

No*

Yes

No*

Bulk Registration Support

No*

No*

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

No*

Upgrading/Downgrading Phone Firmware Versions

No

No

No

No

No

No

No

No

No

Secure CME

TLS

No

No

No

No

No

No

No

No

No

SRTP

No

No

No

No

No

No

No

No

No

CA

No

No

No

No

No

No

No

No

No

CAPF

No

No

No

No

No

No

No

No

No

Live Record

No

No

No

No

No

No

No

No

No

Enabling/Disabling KPML

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

No*

Alias Feature

No

No

No

No

No

No

No

No

No

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

Yes

Mailbox

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Unregistered

No

No

No

No

No

No

No

No

No

Night-Service

No

No

No

No

No

No

No

No

No

Max-Length

No

No

No

No

No

No

No

No

No

Call Forward All Softkey on Phone

No*

No*

Yes

Yes

Yes

Yes

Yes

Yes

No*

Multicast MOH (Supported only on ISR G2)

No

No

No

No

No

No

No

No

No

Unicast MOH

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

No

No

No

No

No

No

No

No

No

Night Service

No

No

No

No

No

No

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

No*

Multiple Voice Hunt Group Join/Unjoin

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

No*

Temporary Logout/Login From/To Voice Hunt Group Using FAC

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

No*

Voice Hunt Group Status Message Display On Phone for Join/Unjoin

No

No

No

No

No

No

No

No

No

Channel Hunt Stop

No

No

No

No

No

No

No

No

No

Voice Hunt Group Statistics (Only for Static Members)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Audio Codecs

G.722

No*

No*

No*

Yes

Yes

Yes

Yes

Yes

No*

G.711

Yes

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

Yes

iLBC

No*

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Translation Profile

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Busy Trigger Per Button

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Conference Blocking

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Transfer Blocking

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

COR

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Class Codec

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Transcoding (Only supported on ISR G2)

No

No

No

No

No

No

No

No

No

Multi-VRF (Only supported on ISR G2)

No

No

No

No

No

No

No

No

No

SNMP/MIB (Supported only to get mode and number of registered phones)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Web GUI

No

No

No

No

No

No

No

No

No

Speed Dial

No*

Yes (only on 6911)

Yes (except 6921)

Yes

Yes

Yes

Yes

Yes

No

Busy Lamp Field (BLF)

No*

No*

No*

Yes*

No*

Yes*

No*

Yes*

No*

Call Waiting

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Forced Authorization Code

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

Yes*

HFS (HTTP Firmware Download)

No

No

No

No

No

No

No

No

No

Redial

Yes

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

Yes (only 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Answering

Yes

Yes (only 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

System Message

No*

No*

Yes*

Yes*

No*

Yes*

Yes

Yes

No*

Whisper Intercom

No

No

No

No

No

No

No

No

No

Abbreviated Dialing

No

No

No

No

No

No

No

No

No

After Hours

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

SSH to phone

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No*

Span to PC

Yes

Yes (only 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Web Access to Phone

Yes

Yes (only 6911)

Yes

Yes

Yes

Yes

Yes

Yes

No*

Callback

No

No

No

No

No

No

No

No

No

· For information on SCCP phone feature support for Unified E-SRST releases prior to Release 11.0, see Table 25 .

Table 25 : Unified E-SRST SCCP Phone Feature Support (for Unified E-SRST Releases 10.5 and Prior)

Features

SCCP Phone Models

6941

7925

7926

8941

6945

7942

8945

6961

7931

7962

7965

7975

Anonymous Call Block

No

No

No

Auto-Answer

Yes

Yes

Yes

Auto Register

No

No

No

Auto Assign

No

No

No

Authenticate Register

No

No

No

Barge

No

No

No

cBarge/Merge

No

No

No

Call Park

Yes

Yes

Yes

Call Park Resume

No

No

No

Pickup

Group Pickup

Yes

Yes

Yes

Call Pickup

Yes

Yes

Yes

Distinctive Ring for Parked Call Recall

No

No

No

Park Monitor

Yes

Yes

Yes

Directed Call Park

Yes*

Yes*

Yes*

Extension Mobility

No

No

No

Transfer

Alert/Semi-consult Transfer

Yes

Yes

Yes

Attended/Consult Transfer

Yes

Yes

Yes

Blind Transfer

Yes

Yes

Yes

Conference

Meet-Me Conference

No

No

No

Ad-hoc Hardware Conference (Only on ISR G2)

No

No

No

Ad-hoc Software Conference

Yes

Yes

Yes

Video Conference

No

No

No

Hold/Resume

Yes

Yes

Yes

Intercom

No

No

No

Fast Track

No

No

No

Headset Answer

Yes

Yes

Yes

Line Label

No*

Yes

Yes

Mobility

No

No

No

My Phone Apps - View on Phone

Speed Dial

No

No

No

Personal Speed Dial/ Fast Dial

No

No

No

BLF Speed Dial

No

No

No

Voice Hunt Groups

No

No

No

After Hours

No

No

No

Single Number Reach (SNR)

No

No

No

Active Call Park List

No

No

No

My Phone Apps - Add/Delete/Modify from Phone

Speed Dial

No

No

No

Fast Dial

No

No

No

BLF Speed Dial

No

No

No

Single Number Reach (SNR)

No

No

No

Park Retrieval

Yes

Yes

Yes

Paging

Multicast (Only with G711ulaw codec)

No

No

No

Unicast (Only with G711ulaw codec)

No

No

No

Shared Line

Yes

Yes

Yes

Mixed Shared Line

Yes

Yes

Yes

Voice Hunt Group with Shared Line

Yes

Yes

Yes

Caller ID Display

Yes

Yes

Yes

Caller ID Blocking

No

No

No

Feature Access Code (FAC)

Yes*

Yes*

Yes*

Call Forward to Voice Hunt Group

Yes

Yes

Yes

Call Transfer to a Voice Hunt Group

Yes

Yes

Yes

Call Transfer Recall

No

No

No

Voicemail

Yes

Yes

Yes

Message Waiting Indicator (MWI)

Yes

Yes

Yes

Video

No

No

No

Locale Support

No

No

No

Reset/Restart Phones via Reset/Restart Command

Yes

Yes

Yes

Button Layout/Softkey Template

No

No

No

Directory Services

Local Directory

No

No

No

Local Speed Dial

No

No

No

Personal Speed Dial

No

No

No

Privacy

No

No

No

Transfer to Voice Mail (TrnsfVM)

No

No

No

Do Not Disturb (DND)

Yes

Yes

Yes

DTMF

No

No

No

Feature Button/Programmable Line Keys (PLK)

Yes

Yes

Yes

Key Expansion Module (KEM)

No*

Yes (only on 7962/7965/7975)

Yes

Bulk Registration Support

No

No

No

Upgrading/Downgrading Phone Firmware Versions

No

No

No

Secure CME

TLS

No

No

No

SRTP

No

No

No

CA

No

No

No

CAPF

No

No

No

Live Record

No

No

No

Enabling/Disabling KPML

No

No

No

Alias Feature

No

No

No

Call Forward

All

Yes

Yes

Yes

Busy

Yes

Yes

Yes

No Answer

Yes

Yes

Yes

Mailbox

No

No

No

Unregistered

No

No

No

Night Service

No

No

No

Max-Length

No

No

No

Multicast MOH (Supported only on ISR G2)

Yes

Yes

Yes

Unicast MOH (except SCCP to SCCP)

Yes

Yes

Yes

Basic Automatic Call Distribution (B-ACD)

Yes*

Yes*

Yes*

Night Service

No

No

No

Voice Hunt Group

Yes

Yes

Yes

Voice Hunt Group Dynamic Join/Unjoin

Yes*

Yes*

Yes*

Voice Hunt Group Status Message Display on Phone for Join/Unjoin

Yes*

Yes*

Yes*

Multiple Voice Hunt Group Join/Unjoin

Yes*

Yes*

Yes*

Voice Hunt Group Temporary Logout/Login Using FAC

Yes*

Yes*

Yes*

Channel Hunt Stop

No

No

No

Voice Hunt Group Statistics

Yes

Yes

Yes

Ephone Hunt Group

Yes

Yes

Yes

Ephone Hunt Group Dynamic Join/Unjoin

Yes*

Yes*

Yes*

Ephone Hunt Group Status Message Display on Phone for Join/Unjoin

Yes*

Yes*

Yes*

Ephone Hunt Group Temporary Logout/Login Using HLog/FAC Softkey

Yes*

Yes*

Yes*

Ephone Hunt Group Statistics

Yes

Yes

Yes

Audio Codecs

G.722

Yes

Yes

Yes

G.711

Yes

Yes

Yes

G.729

Yes

Yes

Yes

iLBC

Yes

Yes

Yes

Translation Profile

Yes*

Yes*

Yes*

Busy Trigger Per Button

No

No

No

Conference Blocking

Yes*

Yes*

Yes*

Transfer Blocking

No

No

No

COR

Yes

Yes

Yes

Voice Class Codec

No

No

No

Transcoding (Only supported on ISR G2)

No

No

No

Multi-VRF (Only supported on ISR G2)

No

No

No

SNMP/MIB

Yes

Yes

Yes

Web GUI

Yes

Yes

Yes

Speed Dial

Yes

Yes

Yes

Busy Lamp Field (BLF)

Yes*

Yes*

Yes*

Call Waiting

Yes

Yes

Yes

Forced Authorization Code

Yes

Yes

Yes

HFS (HTTP Firmware Download)

No

No

No

Redial

Yes

Yes

Yes

Speakerphone

Dialing

Yes

Yes

Yes

Answering

Yes

Yes

Yes

System Message

Yes*

Yes*

Yes*

Whisper Intercom

No

No

No

Intercom

No

No

No

Abbreviated Dialing

No

No

No

After Hours

Yes

Yes

Yes

SSH to Phone

No

Yes

Yes

Span to PC

Yes

Yes

Yes

Web Access to Phone

Yes

Yes

Yes

Overlay DN

No

No

No

Callback

No

No

No

Feature Blocking (CFwdAll,  Confrn, GpickUp, Park, PickUp, Trnsfer)

No

No

No

## KEM Support for Cisco Unified SIP IP Phones

Cisco Unified IP Key Expansion Modules (KEMs) are supported on:

· CP-8800-Audio (A-KEM) is supported with Cisco Unified IP Phones 8851/51NR, and 8861 from Unified CME 12.5 Release.

· CP-8800-Video (V-KEM) is supported with Cisco Unified IP Phone 8865 from Unified CME 12.5 Release.

· Cisco Unified 8961, 9951, and 9971 phones from Unified CME/SRST 9.1.

· Cisco Unified 8851/8851NR, and 8861 phones from Unified CME/SRST/E-SRST 10.0(fast-track mode) and Unified CME/SRST/E-SRST 11.0(built-in mode).

You attach KEMs to supported phones to increase line key and feature key appearances, speed dials, or programmable buttons on your phones.

Table 26 lists the number of keys supported on Cisco Unified 8851/51NR, 8861, 8961, 9951, and 9971 SIP IP phones without KEMs.

Table 26 : Number of Configurable Keys on Supported Cisco Unified SIP IP Phones without KEMs

Number of Keys

8961

9951

9971

8851/51NR

8861

8865

Fixed feature keys

5

5

6

5

5

5

Line keys

5

5

6

5

5

5

Programmable soft keys

5

5

6

5

5

5

With KEMs, the programmable buttons can be configured as phone line buttons, speed-dial buttons, or phone feature buttons.

Table 27 compares the number of feature keys that can be configured on supported Cisco Unified SIP IP 8861 phones with and without KEM .

Table 27 : Number of Configurable Feature Keys

Number of Keys

Without KEMs

With CP-BEKEM

With A-KEM and V-KEM

Busy-Lamp-Field speed dial

1 to 9

1 to 112

88

Directory number

1 to 10

1 to 113

89

Speed dial

1 to 9

1 to 112

88

Table 28 l ists the maximum number of KEMs supported on Cisco Unified 8851/51NR, 8861, 8865, 8961, 9951, and 9971 SIP IP phones .

Table 28 : Maximum Number of Supported KEMs and Additional Lines or Buttons

Cisco Unified SIP IP Phones

Maximum Number of Supported KEMs

Maximum Number of Additional

Lines or Buttons (BEKEM)

Maximum Number of Additional

Lines or Buttons (A-KEM, V-KEM)

8961

1

36

–

8851/51NR

2

72

56

9951

2

72

–

8861

3

108

84

8865

3

108

84

9971

3

108

-

## Fast Track Phone Feature Support

This section provides feature support and fast track configuration information for Cisco Unified SIP phone validated for Unified CME.

· For information on fast track configuration for Unified CME validated phones, see Table 29 .

· For information on fast track phone feature support for Unified CME releases, see Table 30 .

Table 29 : Supported Fast Track Phone Configurations

Cisco Unified SIP Phone Model

Recommended Fast Track Configuration

Unified CME

Versions Supported

Comments

Supported Locale Package Version

ATA 191

ATA 190

voice register pool-type ATA-190

description “Cisco Analog Phone Adapter ATA 190”

reference-pooltype ATA-187

Unified CME 10.5 onwards until native support is added

Cisco Analog Phone Adapter ATA 190

Not supported

7811

voice register pool-type  7811 xml-config maxNumCalls 4 xml-config busyTrigger 4

description Cisco IP Phone 7811

reference-pooltype 6921

Unified CME 10.5

10.5

7821

voice register pool-type 7821

description Cisco IP Phone 7821

reference-pooltype 6921

Unified CME 10.0 (15.3(3)M) to Unified CME 10.5 (15.4(3)M)

7821 phone is a hardware revision of the earlier 6921 phone.

10.5

7832

voice register pool-type  7832

description Cisco IP Phone 7832

reference-pooltype 7811

Unified CME 12.3

12.1

7841

voice register pool-type 7841

description Cisco IP Phone 7841

reference-pooltype 6941

Unified CME 10.0 (15.3(3)M) to Unified CME 10.5 (15.4(3)M)

7841 phone is a hardware revision of the earlier 6941 phone

10.5

7861

voice register pool-type 7861

description Cisco IP Phone 7861

reference-pooltype 6961 num-lines 16

Unified CME 10.0 (15.3(3)M) to Unified CME 10.5 (15.4(3)M)

7861 phone is a hardware revision of the earlier 6961 phone. This phone has 16 lines whereas 6961 has 12 lines.

10.5

8811

voice register pool-type  8811 xml-config maxNumCalls 200 xml-config busyTrigger 200 num-lines 24

description Cisco IP Phone 8811

reference-pooltype 9971

Unified CME 10.5

8811 is a conference station.

10.5

8821

voice register pool-type  8821 xml-config maxNumCalls 6 xml-config busyTrigger 6  num-lines 114

description Cisco IP Phone 8821

reference-pooltype 9971

Unified CME 10.5

10.5

8831

voice register pool-type  8831 xml-config maxNumCalls 4 xml-config busyTrigger 4

description Cisco IP Phone 8831

reference-pooltype 9971

Unified CME 10.0 (15.3(3)M) until built in phone support is added on Unified CME

8831 is an IP Conference Phone.

10.5

8832

voice register pool-type  8832

description Cisco IP Phone 8832

reference-pooltype 8811

Unified CME 12.3

12.1

8841

voice register pool-type 8841 xml-config maxNumCalls 200 xml-config busyTrigger 200 num-lines 24

description Cisco IP Phone 8841

reference-pooltype 8961

Unified CME 10.5

10.5

8851

voice register pool-type  8851 xml-config maxNumCalls 6 xml-config busyTrigger 6  num-lines 77

description Cisco IP Phone 8851

reference-pooltype 9951

Unified CME 10.5

10.5

8851NR

voice register pool-type  8851 xml-config maxNumCalls 6 xml-config busyTrigger 6  num-lines 77

description Cisco IP Phone 8851

reference-pooltype 9951

Unified CME 10.5

8851 has the same feature set as 8851NR, except support for Bluetooth.

10.5

8861

voice register pool-type  8861 xml-config maxNumCalls 6 xml-config busyTrigger 6  num-lines 114

description Cisco IP Phone 8861

reference-pooltype 9971

Unified CME 10.5

10.5

Note: Locale package versions mentioned in the above table are compatible with all the CME versions mentioned in the CME versions supported column.

Once the new SIP phone model is configured using the fast-track configuration approach, the new phone model can be provisioned using the existing voice register pool configuration option as shown below:

voice register pool 1

type 7821

id mac D824.BD27.9EAC

voice register global

mode cme

load 7821 sipCisco IP Phone 7800 Series.10-1-1SR1-4.loads

Note: Use the "show voice register pool-type <new-phone-model>" or "show voice register pool-type all" command to display the properties of a new phone model.

CME1# sh voice register pool type 7821

FastTrack Phone Model : 7821

Pooltype(index) representing the phone model : 48

Reference pooltype to inherit the properties from : 6921

Number of lines supported : 2 (inherited from 6921)

Number of addon modules supported : 0 (inherited from 6921)

Default session transport : UDP (inherited from 6921)

Description(helpstring) : Cisco IP Phone 7821

Phone supports GSM : NO (inherited from 6921)

Phone supports Telnet acess : NO (inherited from 6921)

Phone supports firmware download from CME : YES (inherited from 6921)

Phone specific XML tags :

maxNumCalls12/maxNumCalls (inherited from 6921)

busyTrigger12/busyTrigger (inherited from 6921)

Phone family : RTL_PHONES

Pool ID IP Address Ln DN Number State

=== === ======== == == ======= ====== ===

6 D824.BD27.9EAC 9.44.29.44 1 6 4080$ REGISTERED

CME1#

Table 30 : Unified CME Validated Fast Track Phone Feature Support

Features

Phone Models

ATA 190

7811

7821

7841

7861

8811

8831

8841

8845

8851

8851NR

8861

Ad-hoc Hardware Conference (Only on ISR G2)

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Ad-hoc Software Conference Call

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Forward All Softkey

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Forward All

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call forward Busy

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Forward No Answer

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Park

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Park Retrieval

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Call Pickup

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Directory Services

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Do Not Disturb

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

DTMF (RTP-NTE)

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Extension Mobility

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Group Pickup

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Headset Mode Answer

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Hold or Resume

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Line Label (name under pool)

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Message Waiting Indicator

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Music on Hold

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

My Phone Apps – View on Phone

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Redial

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Single Number Reach(SNR)

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Softkey Template

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Speakerphone Dialing/ Answering

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Shared Line

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Transcoding

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Transfer

Consult

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Alert

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voicemail

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Voice Hunt Groups

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Obtain Documentation and Submit a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What’s New in Cisco Product Documentation RSS feed. The RSS feeds are a free service.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R)

Cisco Unified Communications Manager Express Phone Feature Support

© 2019 Cisco Systems, Inc. All Rights reserved.

NOTE: Works with document’s Advanced Properties “Last Updated” property. Click File | Properties | Advanced Properties | Custom .

### This Document Applies to These Products

- Unified Communications Manager Express

| Convention | Description |
|---|---|
| Yes | The feature is supported. |
| Yes* | The feature is supported by Unified E-SRST (but not by Unified SRST Manager). |
| No | The feature is not supported. |
| No* | It is a known phone limitation. |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8821 |
| 7832 | 8831 |
| 7841 | 8832 |
| 7861 | 8841 |
|  | 8845 |
|  | 8851/51NR |
|  | 8861 |
|  | 8865 |
| Toll Fraud Prevention for Unified CME Line Side SIP | Yes | Yes |
| Unified CME Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a Release) introduces support for SNMP Version 3 (SNMPv3) and Unified CME Password Policy. Unified CME GUI and CTI CSTA features are deprecated, and not available on Unified CME 12.6 and later releases. |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8821 |
| 7832 | 8831 |
| 7841 | 8832 |
| 7861 | 8841 |
|  | 8845 |
|  | 8851/51NR |
|  | 8861 |
|  | 8865 |
| Virtual CME (vCME) on Cisco CSR1000V Cloud Services Router | Yes | Yes |
| As part of Unified CME Release 12.5 (Cisco IOS XE Gibraltar 16.10.1 Release), support was introduced for Cisco ATA 191, Cisco Jabber, and KEM Modules (CP-8800-Audio, CP-8800-Video). |

| Features | Phone Model (Cisco ATA 191) |
|---|---|
| Anonymous Call Block | No |
| Auto-Answer | No |
| Auto Register | Yes |
| Auto Assign | No |
| Authenticate Register | No |
| Barge | No |
| cBarge/Merge | Yes |
| Call Park | Yes |
| Call Park Resume | No |
| Pickup | Pickup | Yes |
| Group Pickup | Yes |
| Distinctive Ring for Parked Call Recall | No |
| Park Monitor | No |
| Directed Call Park | No |
| Extension Mobility | No |
| Extension Assigner | Yes |
| Transfer | Alert Transfer | Yes |
| Attended/Consult Transfer | Yes |
| Blind Transfer | No |
| Conference | Meet-Me Conference | Yes |
| Ad-hoc Hardware Conference | No |
| Ad-hoc Software Conference | No* |
| Video Conference | No |
| Hold/Resume | Yes |
| Intercom | No |
| Fast Track | No |
| Headset Answer | No |
| Line Label | No |
| My Phone Apps - View On Phone | Speed Dial | No |
| Personal Speed Dial/Fast Dial | No |
| BLF Speed Dial | No |
| Voice Hunt Groups | No |
| After Hours | No |
| Single Number Reach (SNR) | No |
| Active Call Park List | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No |
| Fast Dial | No |
| BLF Speed Dial | No |
| Single Number Reach (SNR) | No |
| Park Retrieval | No |
| Paging | Multicast (Only with G711ulaw codec) | No |
| Unicast (Only with G711ulaw codec) | No |
| Shared Line | Yes |
| Mixed Shared Line | Yes |
| Voice Hunt Group with Shared Line | No |
| Caller ID Display | No |
| Caller ID Blocking | Yes |
| Feature Access Code (FAC) 1 | No |
| Call Transfer Recall | No |
| Voicemail | Yes |
| Message Waiting Indicator (MWI) | Yess |
| Video 2 | No |
| Locale Support | No |
| Reset/Restart Phones via Reset/Restart Command | No |
| Button Layout/Softkey Template | No |
| Directory Services | Local Directory | No |
| Local Speed Dial | No |
| Personal Speed Dial | No |
| Privacy | No |
| iDivert* (Transfer to other mailboxes is not supported) | No |
| Enhanced iDivert | No |
| Do Not Disturb (DND) | No |
| DTMF | Yes |
| Feature Button/Programmable Line Key (PLK) | No |
| Key Expansion Module (KEM) | C-KEM | No |
| BE-KEM | No |
| A-KEM (CP-8800-Audio) | No |
| V-KEM (CP-8800-Video) | No |
| Bulk Registration Support | No |
| Upgrading/Downgrading Phone Firmware Versions | Yes |
| Live Record | No |
| Enabling/Disabling KPML | Yes |
| Alias Feature | No |
| Call Forward | All | Yes |
| Busy | Yes |
| No Answer | Yes |
| Mailbox | No |
| Unregistered | Yes |
| Night-Service | No |
| Max-Length | No |
| Call Forward All Softkey on Phone | No |
| Music on Hold (MOH) | Yes |
| Basic Automatic Call Distribution (B-ACD) | No |
| Night Service | No |
| Voice Hunt Group | No |
| Channel Hunt Stop | No |
| Voice Hunt Group/Ephone Hunt Group Statistics | No |
| Translation Profile | No |
| Busy Trigger Per Button | No |
| Conference Blocking | No |
| Transfer Blocking | No |
| COR | No |
| Voice Class Codec | No |
| Audio Codecs | G.722 | No |
| G.711 | No |
| G.729 | No |
| iLBC | No |
| Transcoding | No |
| Multi-VRF (Only supported on ISR G2) | No |
| SNMP/MIB | No |
| Web GUI | No |
| Speed Dial | No |
| Busy Lamp Field (BLF) | No |
| Call Waiting | Yes |
| Forced Authorization Code | No |
| HTTP File Server (HFS) | No |
| Redial | Yes |
| Speakerphone | Dialing | No |
| Answering | No |
| System Message | No |
| Whisper Intercom | No |
| Abbreviated Dialing | No |
| After Hours | No |
| SSH to Phone | Yes |
| Span to PC | No |
| Web Access to Phone | Yes |
| Callback | No |
| Call Waiting Ring/Tone | No |
| Fax Transmission | T.38 | Yes |
| Codec Passthrough | Yes |

| Features | Phone Model (Cisco Jabber) |
|---|---|
| Auto Register | No |
| Auto Assign | No |
| Authenticate Register | No |
| Barge | No |
| cBarge/Merge | No |
| Call Park | Yes |
| Call Park Resume | Yes |
| Pickup | Pickup | Yes |
| Group Pickup | No |
| Distinctive Ring for Parked Call Recall | No |
| Park Monitor | No |
| Directed Call Park | Yes |
| Extension Mobility | No |
| Transfer | Alert Transfer | Yes |
| Attended/Consult Transfer | Yes |
| Blind Transfer | No |
| Conference | Meet-Me Conference | No |
| Ad-hoc Hardware Conference | Yes |
| Ad-hoc Software Conference | No |
| Video Conference | No |
| Hold/Resume | Yes |
| Intercom | No |
| Fast Track | No |
| Headset Answer | No |
| Line Label | No |
| My Phone Apps - View On Phone | Speed Dial | No |
| Personal Speed Dial/Fast Dial | No |
| BLF Speed Dial | No |
| Voice Hunt Groups | No |
| After Hours | No |
| Single Number Reach (SNR) | No |
| Active Call Park List | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No |
| Fast Dial | No |
| BLF Speed Dial | No |
| Single Number Reach (SNR) | Yes |
| Paging | Multicast (Only with G711ulaw codec) | No |
| Unicast (Only with G711ulaw codec) | No |
| Shared Line | Yes |
| Mixed Shared Line | Yes |
| Voice Hunt Group with Shared Line | Yes |
| Caller ID Display | No |
| Caller ID Blocking | No |
| Feature Access Code (FAC) 1 | No |
| Call Transfer Recall | No |
| Voicemail | No |
| Message Waiting Indicator (MWI) | No |
| Video | Yes |
| Locale Support | No |
| Reset/Restart Phones via Reset/Restart Command | Yes |
| Button Layout/Softkey Template | No |
| Directory Services | Local Directory | No |
| Local Speed Dial | No |
| Personal Speed Dial | No |
| Privacy | Yes |
| iDivert | No |
| Enhanced iDivert | No |
| Do Not Disturb (DND) | No |
| DTMF | Yes |
| Feature Button/Programmable Line Key (PLK) | No |
| Upgrading/Downgrading Phone Firmware Versions | No |
| Live Record | No |
| Enabling/Disabling KPML | No |
| Alias Feature | No |
| Call Forward | All | Yes |
| Busy | Yes |
| No Answer | Yes |
| Mailbox | No |
| Unregistered | Yes |
| Night-Service | No |
| Max-Length | No |
| Call Forward All Softkey on Phone | No |
| Music on Hold (MOH) | Yes |
| Basic Automatic Call Distribution (B-ACD) | No |
| Night Service | No |
| Voice Hunt Group | Yes |
| Channel Hunt Stop | No |
| Audio Codecs | G.722 | No |
| G.711 | No |
| G.729 | No |
| iLBC | No |
| Video Codec (H.264) | Yes |
| Speed Dial | No |
| Busy Lamp Field (BLF) | No |
| Redial | Yes |

| Features | VG310 | VG320 | VG350 |
|---|---|---|---|
| Anonymous Call Block | No | No | No |
| Auto-Answer | No | No | No |
| Auto Register | Yes | Yes | Yes |
| Auto Assign | Yes | Yes | Yes |
| Authenticate Register | No | No | No |
| Barge | No | No | No |
| cBarge | No | No | No |
| Call Park | Yes | Yes | Yes |
| Pickup | Group Pickup | Yes | Yes | Yes |
| Call Pickup | Yes | Yes | Yes |
| Distinctive Ring for Parked Call Recall | No | No | No |
| Directed Call Park | Yes | Yes | Yes |
| Extension Mobility | No | No | No |
| Extension Assigner | Yes | Yes | Yes |
| Transfer | Alert Transfer | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes |
| Blind Transfer | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No | No | No |
| Ad-hoc Hardware Conference | No | No | No |
| Video Conference | No | No | No |
| Hold/Resume | Yes | Yes | Yes |
| Intercom | No | No | No |
| Fast Track | No | No | No |
| Headset Answer | No | No | No |
| Line Label | No | No | No |
| Single Number Reach (SNR) (except Mobility) | Yes | Yes | Yes |
| Park Retrieval | Yes | Yes | Yes |
| Paging | Multicast (Only with G711ulaw codec) | No | No | No |
| Unicast (Only with G711ulaw codec) | No | No | No |
| Shared Line (No Hold/ Remote Resume Support) | Yes | Yes | Yes |
| Mixed Shared Line (No Hold/ Remote Resume Support) | Yes | Yes | Yes |
| Voice Hunt Group with Shared Line | Yes | Yes | Yes |
| Caller ID Display | Yes | Yes | Yes |
| Caller ID Blocking | Yes | Yes | Yes |
| Feature Access Code ( VG Specific FAC ) | Yes | Yes | Yes |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer Recall | Yes | Yes | Yes |
| Voicemail | Yes | Yes | Yes |
| Message Waiting Indicator (MWI). See Configuring AMWI and VMWI . | Yes | Yes | Yes |
| Video | No | No | No |
| Locale Support | No | No | No |
| Button Layout/Softkey Template | No | No | No |
| Directory Services | Local Directory | No | No | No |
| Local Speed Dial | No | No | No |
| Personal Speed Dial | No | No | No |
| iDivert | No | No | No |
| Enhanced iDivert | No | No | No |
| Do Not Disturb (DND) (Supported with FAC) | Yes | Yes | Yes |
| DTMF | Yes | Yes | Yes |
| Feature Button/Programmable Line Key (PLK) | No | No | No |
| Live Record | No | No | No |
| Call Forward | All | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes |
| Mailbox | No | No | No |
| Unregistered | No | No | No |
| Night-Service | Yes | Yes | Yes |
| Max-Length | Yes | Yes | Yes |
| Multicast MOH | No | No | No |
| Unicast MOH | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | Yes | Yes | Yes |
| Night Service | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes |
| Channel Hunt Stop | Yes | Yes | Yes |
| Voice Hunt Group or Ephone Hunt Group Statistics | Yes | Yes | Yes |
| Audio Codecs | G.722 | Yes | Yes | Yes |
| G.711 | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes |
| iLBC | Yes | Yes | Yes |
| Translation Profile | Yes | Yes | Yes |
| Busy Trigger Per Button (Maximum Value: 2) | Yes | Yes | Yes |
| Conference Blocking | Yes | Yes | Yes |
| Transfer Blocking | Yes | Yes | Yes |
| COR | Yes | Yes | Yes |
| Voice Class Codec | No | No | No |
| Transcoding | No | No | No |
| Multi-VRF | No | No | No |
| SNMP/MIB | Yes | Yes | Yes |
| Speed Dial | Yes | Yes | Yes |
| Busy Lamp Field (BLF) | No | No | No |
| Call Waiting | Yes | Yes | Yes |
| Forced Authorization Code | Yes | Yes | Yes |
| Redial | Yes | Yes | Yes |
| Speakerphone (Endpoint Supports) | Dialing | Yes | Yes | Yes |
| Answering | Yes | Yes | Yes |
| System Message | No | No | No |
| Whisper Intercom | No | No | No |
| Abbreviated Dialing | No | No | No |
| After Hours | Yes | Yes | Yes |
| Callback | No | No | No |
| Secondary CME | Yes | Yes | Yes |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8821 |
| 7832 | 8831 |
| 7841 | 8832 |
| 7861 | 8841 |
|  | 8845 |
|  | 8851/51NR |
|  | 8861 |
|  | 8865 |
| Enhanced Line Mode on Cisco 4000 Series Integrated Services Routers | No | Yes (except 8821,8831, 8832) |
| Softkeys (Recents, Contacts, Apps, Favorites, Messages, Settings) | Yes (only for 7832) | Yes (only for 8832) |
| As part of Unified CME Release 12.3 (Cisco IOS XE Fuji 16.9.1 Release), support was introduced for Cisco IP Conference Phone 7832 and Cisco IP Conference Phone 8832. |

| Features | Phone Models |
|---|---|
| Cisco Unified IP Phone 6900 Series | Cisco Unified IP Phone 7900 Series |
| 6961 | 7962 |
|  | 7945 |
|  | 7965 |
|  | 7975 |
|  |  |
|  |  |
|  |  |
|  |  |
| Support for Secure SCCP Endpoints and Analog Voice Gateways on Secure SRST. Note: For information on VG feature support, see Table 8: Phone Feature Support for Analog Voice Gateways with Secure SRST . | Yes | Yes |

| Features | VG202 | VG202XM | VG204 | VG204XM | VG224 | VG310 | VG320 |
|---|---|---|---|---|---|---|---|
| Anonymous Call Block | No | No | No | No | No | No | No |
| Auto-Answer | No | No | No | No | No | No | No |
| Auto Register | No | No | No | No | No | No | No |
| Auto Assign | No | No | No | No | No | No | No |
| Authenticate Register | No | No | No | No | No | No | No |
| Barge | No | No | No | No | No | No | No |
| cBarge | No | No | No | No | No | No | No |
| Call Park | No | No | No | No | No | No | No |
| Call Park Resume | No | No | No | No | No | No | No |
| Pickup | Group Pickup | No | No | No | No | No | No | No |
| Call Pickup | No | No | No | No | No | No | No |
| Distinctive Ring for Parked Call Recall | No | No | No | No | No | No | No |
| Park Monitor | No | No | No | No | No | No | No |
| Directed Call Park | No | No | No | No | No | No | No |
| Extension Mobility | No | No | No | No | No | No | No |
| Transfer | Alert/Semi-Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Blind Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No | No | No | No | No | No | No |
| Ad-hoc Hardware Conference | No | No | No | No | No | No | No |
| Ad-hoc Software Conference (only with G.711 codec) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Video Conference | No | No | No | No | No | No | No |
| Hold/Resume | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Intercom | No | No | No | No | No | No | No |
| Fast Track | No | No | No | No | No | No | No |
| Headset Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Line Label | No | No | No | No | No | No | No |
| Mobility | No | No | No | No | No | No | No |
| My Phone Apps - View On Phone | Speed Dial | No | No | No | No | No | No | No |
| Personal Speed Dial/Fast Dial | No | No | No | No | No | No | No |
| BLF Speed Dial | No | No | No | No | No | No | No |
| Voice Hunt Groups | No | No | No | No | No | No | No |
| After Hours | No | No | No | No | No | No | No |
| Single Number Reach (SNR) | No | No | No | No | No | No | No |
| Active Call Park List | No | No | No | No | No | No | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No | No | No | No | No | No | No |
| Fast Dial | No | No | No | No | No | No | No |
| BLF Speed Dial | No | No | No | No | No | No | No |
| Single Number Reach (SNR) | No | No | No | No | No | No | No |
| Park Retrieval | No | No | No | No | No | No | No |
| Paging | Multicast (Only with G711ulaw codec) | No | No | No | No | No | No | No |
| Unicast (Only with G711ulaw codec) | No | No | No | No | No | No | No |
| Shared Line (No Hold/ Remote Resume Support) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Mixed Shared Line | No | No | No | No | No | No | No |
| Voice Hunt Group with Shared Line | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Caller ID Display | No | No | No | No | No | No | No |
| Caller ID Blocking | No | No | No | No | No | No | No |
| Feature Access Code ( VG Specific FAC ) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No | No | No | No | No |
| Voicemail | No | No | No | No | No | No | No |
| Message Waiting Indicator (MWI) | No | No | No | No | No | No | No |
| Video | No | No | No | No | No | No | No |
| Locale Support | No | No | No | No | No | No | No |
| Reset/Restart Phones via Reset/Restart Command | No | No | No | No | No | No | No |
| Button Layout/Softkey Template | No | No | No | No | No | No | No |
| Directory Services | Local Directory | No | No | No | No | No | No | No |
| Local Speed Dial | No | No | No | No | No | No | No |
| Personal Speed Dial | No | No | No | No | No | No | No |
| Privacy | No | No | No | No | No | No | No |
| iDivert | No | No | No | No | No | No | No |
| Enhanced iDivert | No | No | No | No | No | No | No |
| Do Not Disturb (DND) | No | No | No | No | No | No | No |
| DTMF | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Feature Button/Programmable Line Key (PLK) | No | No | No | No | No | No | No |
| Key Expansion Module (KEM) | No | No | No | No | No | No | No |
| Bulk Registration Support | No | No | No | No | No | No | No |
| Upgrading/Downgrading Phone Firmware Versions | No | No | No | No | No | No | No |
| Live Record | No | No | No | No | No | No | No |
| Enabling/Disabling KPML | No | No | No | No | No | No | No |
| Alias Feature | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Forward | All | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Mailbox | No | No | No | No | No | No | No |
| Unregistered | No | No | No | No | No | No | No |
| Night-Service | No | No | No | No | No | No | No |
| Max-Length | No | No | No | No | No | No | No |
| Call Forward All Softkey on Phone | No | No | No | No | No | No | No |
| Multicast MOH | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Unicast MOH (Supported Only on SIP phones) | No | No | No | No | No | No | No |
| Basic Automatic Call Distribution (B-ACD) | No | No | No | No | No | No | No |
| Night Service | No | No | No | No | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | No | No | No | No | No | No | No |
| Multiple Voice Hunt Group Join/Unjoin | No | No | No | No | No | No | No |
| Temporary Logout/Login From/To Voice Hunt Group Using FAC | No | No | No | No | No | No | No |
| Voice Hunt Group Status Message Display On Phone for Join/Unjoin | No | No | No | No | No | No | No |
| Channel Hunt Stop | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Group Statistics (Only for static members) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Audio Codecs | G.722 | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| G.711 | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| iLBC | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Translation Profile | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy Trigger Per Button | No | No | No | No | No | No | No |
| Conference Blocking | No | No | No | No | No | No | No |
| Transfer Blocking | No | No | No | No | No | No | No |
| COR | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Class Codec | No | No | No | No | No | No | No |
| Transcoding (Only supported on ISR G2) | No | No | No | No | No | No | No |
| Multi-VRF (Only supported on ISR G2) | No | No | No | No | No | No | No |
| SNMP/MIB (Supported only to get mode and number of registered phones) | No | No | No | No | No | No | No |
| Web GUI | No | No | No | No | No | No | No |
| Speed Dial | No | No | No | No | No | No | No |
| Busy Lamp Field (BLF) | No | No | No | No | No | No | No |
| Call Waiting | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Forced Authorization Code | No | No | No | No | No | No | No |
| HFS (HTTP Firmware Download) | No | No | No | No | No | No | No |
| Redial | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Speakerphone (Endpoint Supports) | Dialing | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Answering | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| System Message | No | No | No | No | No | No | No |
| Whisper Intercom | No | No | No | No | No | No | No |
| Abbreviated Dialing | No | No | No | No | No | No | No |
| After Hours | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| SSH to Phone | No | No | No | No | No | No | No |
| Span to PC | No | No | No | No | No | No | No |
| Web Access to Phone | No | No | No | No | No | No | No |
| Callback | No | No | No | No | No | No | No |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8821 |
| 7841 | 8831 |
| 7861 | 8841 |
|  | 8845 |
|  | 8851/51NR |
|  | 8861 |
|  | 8865 |
| Voice Hunt Group with Shared Lines for  Unified CME on Cisco 4000 Series Integrated Services Router | Yes | Yes |
| All Agents Logged Out Messaged Display on SIP Phones in a Voice Hunt Group | No | Yes |
| Music On Hold from a Live Feed for Unified CME on Cisco 4000 Series Integrated Services Router | Yes | Yes |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series | Cisco Unified IP Phone 7900 Series |
| 7811 | 8811 | 7975G |
| 7821 | 8821 | 7965G |
| 7841 | 8831 | 7945G |
| 7861 | 8841 |  |
|  | 8845 |  |
|  | 8851/51NR |  |
|  | 8861 |  |
|  | 8865 |  |
| Voice Hunt Group Enhancements for Unified E-SRST on Cisco 4000 Series Integrated Services Router (Supported on SIP and SCCP Phones) | Yes | Yes | Yes |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8821 |
| 7841 | 8831 |
| 7861 | 8841 |
|  | 8845 |
|  | 8851/51NR |
|  | 8861 |
|  | 8865 |
| Secure SRST Support for SIP Phones on Cisco 4000 Series Integrated Services Router | Yes | Yes |
| Smart Licensing Support for Unified SRST | Yes | Yes |
| Unified SRST and Unified Border Element Colocation on Cisco 4000 Series Integrated Services Router | Yes | Yes |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8821 |
| 7841 | 8831 |
| 7861 | 8841 |
|  | 8845 |
|  | 8851/51NR |
|  | 8861 |
|  | 8865 |
| IPv6 Support for SIP Phones on Unified SRST | Yes | Yes |
| Idle URL Support on SIP Phones | Yes | Yes |
| Called-Name Display (Dialed Number Identification Service) | Yes | Yes |
| Calling Number Local | Yes | Yes |
| cBarge for Mixed Shared Line | Yes | Yes |
| As part of Unified CME Release 12.0, support for Cisco Wireless IP Phone 8821, Cisco IP Phones 8845, 8865 was introduced on the 15.7(3)M Release of T-Train for the Cisco Integrated Services Routers Generation 2 (ISR G2). |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8821 |
| 7841 | 8831 |
| 7861 | 8841 |
|  | 8845 |
|  | 8851/51NR |
|  | 8861 |
|  | 8865 |
| Transcoding support for Music on Hold (Cisco ISR 4000 Series) | Yes | Yes |
| Conferencing support on Unified CME (Cisco ISR 4000 Series) | Yes | Yes |
| Smart Licensing | NA | NA |
| As part of Unified CME Release 11.7, new phone support for Cisco Wireless IP Phones 8821, Cisco IP Phones 8845, 8865 was introduced for Cisco 4000 Series Integrated Services Router (On Cisco IOS XE Everest 16.5.1). |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8831 |
| 7841 | 8841 |
| 7861 | 8851/51NR |
|  | 8861 |
| B-ACD Loopback Calls | Yes | Yes |
| VHG Enhancements (HLog, PLK or Agent Status Control) | Yes | Yes |
| Secondary Dial Tone | Yes | Yes |
| Extension Assigner | Yes | Yes |
| Call Transfer Recall | Yes | Yes |
| Secondary CME | Yes | Yes |
| LTI-based Transcoding (Cisco 4000 Series ISR) | Yes | Yes |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series |
| 7811 | 8811 |
| 7821 | 8831 |
| 7841 | 8841 |
| 7861 | 8851/51NR |
|  | 8861 |
| B-ACD (SIP Phones) | Yes | Yes |
| Auto Registration (SIP Phones) | Yes | Yes |
| Night Service (SIP Phones) | Yes | Yes |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series | ATA |
| 7811 | 8811 | ATA-190 |
| 7821 | 8831 |  |
| 7841 | 8841 |  |
| 7861 | 8851/51NR |  |
|  | 8861 |  |
| Anonymous Call Block | Yes | Yes | No* |
| Auto-Answer | Yes | Yes | No* |
| Auto Register | No | No | No |
| Auto Assign | No | No | No |
| Authenticate Register | Yes | Yes | Yes |
| Barge | No | No | No |
| cBarge/Merge | Yes | Yes | No* |
| Call Park | Yes | Yes | No* |
| Call Park Resume | No | No | No |
| Pickup | Group Pickup | Yes | Yes | Yes |
| Call Pickup | Yes | Yes | Yes |
| Distinctive Ring for Parked Call Recall | No | No | No |
| Park Monitor | Yes | Yes | No* |
| Directed Call Park | Yes | Yes | No* |
| Extension Mobility | Yes | Yes | No* |
| Transfer | Alert/Semi-consult Transfer | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes |
| Conference | Meet-Me Conference | Yes | Yes | Yes |
| Ad-hoc Hardware Conference                   (Only on ISR G2) | Yes | Yes | Yes |
| Ad-hoc Software Conference | Yes | Yes | Yes |
| Video Conference | No | No | No |
| Hold/Resume | Yes | Yes | Yes |
| Intercom | Yes | Yes | No* |
| Fast Track | Yes | Yes | Yes |
| Headset Answer | Yes | Yes | No* |
| Line Label | Yes | Yes | No* |
| Mobility | Yes | Yes | No* |
| My Phone Apps - View on Phone | Speed Dial | Yes | Yes | No* |
| Personal Speed Dial/Fast Dial | Yes | Yes | No* |
| Busy Lamp Field (BLF) Speed Dial | Yes | Yes | No* |
| Voice Hunt Groups | Yes | Yes | No* |
| After Hours | Yes | Yes | No* |
| Single Number Reach (SNR) | Yes | Yes | No* |
| Active Call Park List | Yes | Yes | No* |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | Yes | Yes | No* |
| Fast Dial | Yes | Yes | No* |
| BLF Speed Dial | Yes | Yes | No* |
| Single Number Reach (SNR) | Yes | Yes | No* |
| Park Retrieval | Yes | Yes | Yes |
| Paging | Multicast (Only with G711ulaw codec) | Yes | Yes | No* |
| Unicast (Only with G711ulaw codec) | Yes | Yes | No* |
| Shared Line | Yes | Yes | Yes |
| Mixed Shared Line | Yes | Yes | Yes |
| Voice Hunt Group with Shared Line | No | No | No |
| Caller ID Display | Yes | Yes | No* |
| Caller ID Blocking | No | No | No |
| Feature Access Code (FAC) ( Call Park, Pickup, Directed Pickup , Voice Hunt Group Join/Unjoin, and Temporary Logout/Login only) | Yes | Yes | No* |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes |
| Call forward to a Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No |
| Voicemail | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | No* |
| Video (Only SIP-SIP/SIP-SCCP Basic Call and SIP-SIP Supplementary Services) | No* | No* | No* |
| Locale Support | Yes | Yes | No* |
| Reset/Restart Phones via Reset/Restart Command | Yes | Yes | Yes |
| Button Layout/Softkey Template | Yes | Yes | No* |
| Directory Services | Local Directory | Yes | Yes | No* |
| Local Speed Dial | Yes | Yes | No* |
| Personal Speed Dial | Yes | Yes | No* |
| Privacy | Yes | Yes | No* |
| iDivert | Yes | Yes | No* |
| Enhanced iDivert | Yes | Yes | No* |
| Do Not Disturb (DND) | Yes | Yes | No* |
| DTMF | Yes | Yes | Yes |
| Feature Button/Programmable Line Key (PLK) | Yes | Yes (except 8831) | No* |
| Key Expansion Module (KEM) | No | Yes (only 8851/8861) | No* |
| Bulk Registration Support | Yes | Yes | No* |
| Upgrade/Downgrade Phone Firmware Versions | Yes | Yes | Yes |
| Secure CME | TLS | No | No | No |
| SRTP | No | No | No |
| CA | No | No | No |
| CAPF | No | No | No |
| Live Record | No | No | No |
| Enabling/Disabling KPML | Yes | Yes | No* |
| Alias Feature | No | No | No |
| Call-Forward | All | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes |
| Mailbox | Yes | Yes | Yes |
| Unregistered | Yes | Yes | Yes |
| Night-Service | No | No | No |
| Max-Length | No | No | No |
| Call Forward All Softkey on Phone | Yes | Yes | No* |
| Multicast MoH (Supported only on ISR G2) | No | No | No |
| Unicast MoH | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | No | No | No |
| Night Service | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | Yes | Yes | No* |
| Multiple Voice Hunt Group Join/Unjoin | Yes | Yes | No* |
| Temporary Logout/Login From/To Voice Hunt Group Using FAC | Yes | Yes | No* |
| Voice Hunt Group Status Message Display On Phone for Join/Unjoin | No | No | No |
| Channel Hunt Stop | Yes | Yes | No* |
| Voice Hunt Group Statistics (Only for static members) | Yes | Yes | Yes |
| Audio Codecs | G.722 | Yes | Yes | No* |
| G.711 | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes |
| iLBC | Yes | Yes | No* |
| Translation Profile | Yes | Yes | Yes |
| Busy Trigger Per Button | Yes | Yes | Yes |
| Conference Blocking | Yes | Yes | Yes |
| Transfer Blocking | Yes | Yes | Yes |
| COR | Yes | Yes | Yes |
| Voice Class Codec | Yes | Yes | Yes |
| Transcoding (Only supported on ISR G2) | Yes | Yes | Yes |
| Multi-VRF (Only supported on ISR G2) | Yes | Yes | Yes |
| SNMP/MIB (Supported only to get mode and number of registered phones) | Yes | Yes | Yes |
| Web GUI | No | No | No |
| Speed Dial | Yes | Yes | No* |
| Busy Lamp Field (BLF) | Yes | Yes | No* |
| Call Waiting | Yes | Yes | Yes |
| Forced Authorization Code | Yes | Yes | Yes |
| HFS (HTTP Firmware Download) | Yes | Yes | No* |
| Redial | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes | No* |
| Answering | Yes | Yes | No* |
| System Message | No | No | No |
| Whisper Intercom | No | No | No |
| Abbreviated Dialing | No | No | No |
| After Hours | Yes | Yes | Yes |
| SSH to Phone | Yes | Yes | No* |
| Span to PC | Yes | Yes (except 8831) | No* |
| Web Access to Phone | Yes | Yes | No* |
| Callback | No | No | No |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series | ATA |
| 7811 | 8811 | ATA-190 |
| 7821 | 8831 |  |
| 7841 | 8841 |  |
| 7861 | 8851/51NR |  |
|  | 8861 |  |
|  | 8845/8865 |  |
| Anonymous Call Block | No | No | No |
| Auto-Answer | Yes | Yes | No* |
| Auto Register | No | No | No |
| Auto Assign | No | No | No |
| Authenticate Register | No | No | No |
| Barge | No | No | No |
| cBarge | No | No | No |
| Call Park | No | No | No |
| Call Park Resume | No | No | No |
| Pickup | Group Pickup | No | No | No |
| Call Pickup | No | No | No |
| Distinctive Ring for Parked Call Recall | No | No | No |
| Park Monitor | No | No | No |
| Directed Call Park | No | No | No |
| Extension Mobility | No | No | No |
| Transfer | Alert/Semi-Consult Transfer | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No | No | No |
| Ad-hoc Hardware Conference | No | No | No |
| Ad-hoc Software Conference | Yes | Yes | Yes |
| Video Conference | No | No | No |
| Hold/Resume | Yes | Yes | Yes |
| Intercom | No | No | No |
| Fast Track | No | No | No |
| Headset Answer | Yes | Yes | No* |
| Line Label | Yes | Yes | No* |
| Mobility | No | No | No |
| My Phone Apps - View On Phone | Speed Dial | No | No | No |
| Personal Speed Dial/Fast Dial | No | No | No |
| BLF Speed Dial | No | No | No |
| Voice Hunt Groups | No | No | No |
| After Hours | No | No | No |
| Single Number Reach (SNR) | No | No | No |
| Active Call Park List | No | No | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No | No | No |
| Fast Dial | No | No | No |
| BLF Speed Dial | No | No | No |
| Single Number Reach (SNR) | No | No | No |
| Park Retrieval | No | No | No |
| Paging | Multicast (Only with G711ulaw codec) | No | No | No |
| Unicast (Only with G711ulaw codec) | No | No | No |
| Shared Line | No | No | No |
| Mixed Shared Line | No | No | No |
| Voice Hunt Group with Shared Line | No | No | No |
| Caller ID Display | Yes | Yes | No* |
| Caller ID Blocking | No | No | No |
| Feature Access Code (FAC) | No | No | No* |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No |
| Voicemail | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | No* |
| Video | No | No | No |
| Locale Support | No | No | No |
| Reset/Restart Phones via Reset/Restart Command | No | No | No |
| Button Layout/Softkey Template | No | No | No |
| Directory Services | Local Directory | No | No | No |
| Local Speed Dial | No | No | No |
| Personal Speed Dial | No | No | No |
| Privacy | No | No | No |
| iDivert | No | No | No |
| Enhanced iDivert | No | No | No |
| Do Not Disturb (DND) | Yes | Yes | No* |
| DTMF | Yes | Yes | Yes |
| Feature Button/Programmable Line Key (PLK) | Yes | Yes | No* |
| Key Expansion Module (KEM) | No* | Yes (only 8851/8851NR/8861) | No* |
| Bulk Registration Support | Yes | Yes | No* |
| Upgrading/Downgrading Phone Firmware Versions | No | No | No |
| Live Record | No | No | No |
| Enabling/Disabling KPML | Yes | Yes | No* |
| Alias Feature | Yes | Yes | Yes |
| Call Forward | All | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes |
| Mailbox | Yes | Yes | Yes |
| Unregistered | No | No | No |
| Night-Service | No | No | No |
| Max-Length | No | No | No |
| Call Forward All Softkey on Phone | Yes | Yes | No* |
| Multicast MOH (Supported only on ISR G2) | No | No | No |
| Unicast MOH | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | No | No | No |
| Night Service | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | No | No | No* |
| Multiple Voice Hunt Group Join/Unjoin | No | No | No* |
| Temporary Logout/Login From/To Voice Hunt Group Using FAC | No | No | No* |
| Voice Hunt Group Status Message Display On Phone for Join/Unjoin | No | No | No |
| Channel Hunt Stop | No | No | No |
| Voice Hunt Group Statistics (Only for static members) | No | No | No |
| Audio Codecs | G.722 | Yes | Yes | No* |
| G.711 | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes |
| iLBC | Yes | Yes | No* |
| Translation Profile | Yes | Yes | Yes |
| Busy Trigger Per Button | Yes | Yes | Yes |
| Conference Blocking | Yes | Yes | Yes |
| Transfer Blocking | Yes | Yes | Yes |
| COR | Yes | Yes | Yes |
| Voice Class Codec | Yes | Yes | Yes |
| Transcoding (Only supported on ISR G2) | No | No | No |
| Multi-VRF (Only supported on ISR G2) | No | No | No |
| SNMP/MIB (Supported only to get mode and number of registered phones) | Yes | Yes | Yes |
| Web GUI | No | No | No |
| Speed Dial | Yes | Yes | No |
| Busy Lamp Field (BLF) | No | No | No |
| Call Waiting | Yes | Yes | Yes |
| Forced Authorization Code | Yes | Yes | Yes |
| HFS (HTTP Firmware Download) | No | No | No |
| Redial | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes | No* |
| Answering | Yes | Yes | No* |
| System Message | Yes | Yes | No* |
| Whisper Intercom | No | No | No |
| Abbreviated Dialing | No | No | No |
| After Hours | Yes | Yes | Yes |
| SSH to Phone | Yes | Yes | No* |
| Span to PC | Yes | Yes ((except 8831) | No* |
| Web Access to Phone | Yes | Yes | No* |
| Callback | No | No | No |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series | ATA |
| 7811 | 8811 | ATA-190 |
| 7821 | 8831 |  |
| 7841 | 8841 |  |
| 7861 | 8851/51NR |  |
|  | 8861 |  |
| Anonymous Call Block | No | No | No |
| Auto-Answer | Yes | Yes | No* |
| Auto Register | No | No | No |
| Auto Assign | No | No | No |
| Authenticate Register | Yes* | Yes* | Yes* |
| Barge | No | No | No |
| cBarge | No | No | No |
| Call Park | No | No | No |
| Call Park Resume | No | No | No |
| Pickup | Group Pickup | Yes* (using FAC) | Yes* (using FAC) | No* |
| Call Pickup | Yes* (using FAC) | Yes* (using FAC) | No* |
| Distinctive Ring for Parked Call Recall | No | No | No |
| Park Monitor | No | No | No |
| Directed Call Park | No | No | No |
| Extension Mobility | No | No | No |
| Transfer | Alert/Semi-Consult Transfer | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No | No | No |
| Ad-hoc Hardware Conference | No | No | No |
| Ad-hoc Software Conference | Yes | Yes | Yes |
| Video Conference | No | No | No |
| Hold/Resume | Yes | Yes | Yes |
| Intercom | No | No | No |
| Fast Track | No | No | No |
| Headset Answer | Yes | Yes | No* |
| Line Label | Yes | Yes | No* |
| Mobility | No | No | No |
| My Phone Apps - View on Phone | Speed Dial | No | No | No |
| Personal Speed Dial/Fast Dial | No | No | No |
| BLF Speed Dial | No | No | No |
| Voice Hunt Groups | No | No | No |
| After Hours | No | No | No |
|  | Single Number Reach (SNR) | No | No | No |
| Active Call Park List | No | No | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No | No | No |
| Fast Dial | No | No | No |
| BLF Speed Dial | No | No | No |
| Single Number Reach (SNR) | No | No | No |
| Park Retrieval | No | No | No |
| Paging | Multicast (Only with G711ulaw codec) | No | No | No |
| Unicast (Only with G711ulaw codec) | No | No | No |
| Shared Line | Yes | Yes (except 8831) | No* |
| Mixed Shared Line | Yes | Yes (except 8831) | No* |
| Voice Hunt Group with Shared Line | No | No | No |
| Caller ID Display | Yes | Yes | No* |
| Caller ID Blocking | No | No | No |
| Feature Access Code (FAC) ( Only for Voice Hunt Group Join/Unjoin, and Temporary Logout/Login Only) | Yes* | Yes* | No* |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No |
| Voicemail | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | No* |
| Video (Only SIP-SIP/SIP-SCCP Basic Call and SIP-SIP Supplementary Services) | No* | No* | No* |
| Locale Support | No | No | No |
| Reset/Restart Phones via Reset/Restart Command | No | No | No |
| Button Layout/Softkey Template | No | No | No |
| Directory Services | Local Directory | No | No | No |
| Local Speed Dial | No | No | No |
| Personal Speed Dial | No | No | No |
| Privacy (On Hold) | Yes* | Yes* | No* |
| iDivert | No | No | No |
| Enhanced iDivert | No | No | No |
| Do Not Disturb (DND) | Yes | Yes | No* |
| DTMF | Yes* | Yes* | Yes* |
| Feature Button/Programmable Line Key (PLK) | Yes | Yes | No* |
| Key Expansion Module (KEM) | No | Yes (only 8851/8851NR/8861) | No* |
| Bulk Registration Support | Yes | Yes | No* |
| Upgrading/Downgrading Phone Firmware Versions | No | No | No |
| Live Record | No | No | No |
| Enabling/Disabling KPML | Yes* | Yes* | No* |
| Alias Feature | No | No | No |
| Call Forward | All | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes |
| No answer | Yes | Yes | Yes |
| Mailbox | Yes | Yes | Yes |
| Unregistered | No | No | No |
| Night-Service | No | No | No |
| Max-Length | No | No | No |
| Call Forward All Softkey on Phone | Yes | Yes | No* |
| Multicast MOH (Supported only on G2 routers) | No | No | No |
| Unicast MOH | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | No | No | No |
| Night Service | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | Yes* | Yes* | No* |
| Multiple Voice Hunt Group Join/Unjoin | Yes* | Yes* | No* |
| Temporary Logout/Login From/To Voice Hunt Group Using FAC | Yes* | Yes* | No* |
| Voice Hunt Group Status Message Display on Phone for Join/Unjoin | No | No | No |
| Channel Hunt Stop | No | No | No |
| Voice Hunt Group Statistics (Only for static members) | Yes | Yes | Yes |
| Audio Codecs | G.722 | Yes | Yes | No* |
| G.711 | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes |
| iLBC | Yes | Yes | No* |
| Translation Profile | Yes* | Yes* | Yes* |
| Busy Trigger Per Button | Yes* | Yes* | Yes* |
| Conference Blocking | Yes* | Yes* | Yes* |
| Transfer Blocking | Yes* | Yes* | Yes* |
| COR | Yes | Yes | Yes |
| Voice Class Codec | Yes* | Yes* | Yes* |
| Transcoding (Only supported on ISR G2) | No | No | No |
| Multi-VRF (Only supported on ISR G2) | No | No | No |
| SNMP/MIB (Supported only to get mode and number of registered phones) | Yes | Yes | Yes |
| Web GUI | No | No | No |
| Speed Dial | Yes | Yes | No* |
| Busy Lamp Field (BLF) | Yes* | Yes* | No* |
| Call Waiting | Yes | Yes | Yes |
| Forced Authorization Code | Yes* | Yes* | Yes* |
| HFS (HTTP Firmware Download) | No | No | No |
| Redial | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes | No* |
| Answering | Yes | Yes | No* |
| System Message | Yes* | Yes* | No* |
| Whisper Intercom | No | No | No |
| Abbreviated Dialing | No | No | No |
| After Hours | Yes | Yes | Yes |
| SSH to Phone | Yes | Yes | No* |
| Span to PC | Yes | Yes ((except 8831) | No* |
| Web Access to Phone | Yes | Yes | No* |
| Callback | No | No | No |

| Features | Phone Models |
|---|---|
| Cisco IP Phone 7800 Series | Cisco IP Phone 8800 Series | ATA |
| 7811 | 8811 | ATA-190 |
| 7821 | 8831 |  |
| 7841 | 8841 |  |
| 7861 | 8851/51NR |  |
|  | 8861 |  |
| Basic Registration in Secure Mode | Yes | Yes | No* |
| Basic Registration in Non Secure Mode | Yes | Yes | No* |
| Hold/Resume | Yes | Yes | No* |
| Transfer | Alert/Semi-Consult Transfer | Local | Yes | Yes | No* |
| Over Trunk | Yes | Yes | No* |
| Between Secure and Non-Secure Phones | Yes | Yes | No* |
|  | Attended/ Consult Transfer | Local | Yes | Yes | No* |
| Over Trunk | Yes | Yes | No* |
| Between Secure and Non-Secure Phone | Yes | Yes | No* |
| Ad-hoc Software Conference | Local Endpoints | Yes | Yes | No* |
| Over Trunk | Yes | Yes | No* |
| Between Secure and Non-Secure Endpoints | Yes | Yes | No* |
| Video Conference | No | No | No |
| Call Forward | All | Yes | Yes | No* |
| Busy | Yes | Yes | No* |
| No Answer | Yes | Yes | No* |

| Features | SIP Phone Models |
|---|---|
| 3905 | 6901 | 6921 | 8941 | DX650 | 7821 | 7962 | 9951 | ATA-187 |
|  | 6911 | 6941 | 8945 |  | 7841 | 7965 | 9971 |  |
|  |  | 6945 | 8961 |  | 7861 | 7975 |  |  |
|  |  | 6961 |  |  |  |  |  |  |
| Anonymous Call Block | No* | No* | No* | Yes | Yes | Yes | No* | Yes | No* |
| Auto-Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Auto Register | No | No | No | No | No | No | No | No | No |
| Auto Assign | No | No | No | No | No | No | No | No | No |
| Authenticate Register | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Barge | No | No | No | No | No | No | No | No | No |
| cBarge/Merge | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Call Park | No* | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Call Park Resume | No | No | No | No | No | No | No | No | No |
| Pickup | Group Pickup | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Pickup | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Distinctive Ring for Parked Call Recall | No | No | No | No | No | No | No | No | No |
| Park Monitor | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Directed Call Park | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Extension Mobility | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Transfer | Alert/Semi-Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No* | Yes (only on 6911) | Yes | Yes | No* | Yes | Yes | Yes | Yes |
| Ad-hoc Hardware Conference (Only on ISR G2) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Ad-hoc Software Conference | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Video Conference | No | No | No | No | No | No | No | No | No |
| Hold/Resume | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Intercom | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Fast Track | No | No | No | No | No | No | No | No | No |
| Headset Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Line Label | No* | No* | No* | Yes | Yes | Yes | Yes | Yes | No* |
| Mobility | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| My Phone Apps - View on Phone | Speed Dial | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Personal Speed Dial/ Fast Dial | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| BLF Speed Dial | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Voice Hunt Groups | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| After Hours | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Single Number Reach (SNR) | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Active Call Park List | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Fast Dial | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| BLF Speed Dial | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Single Number Reach (SNR) | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Park Retrieval | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Paging | Multicast (Only with G711ulaw codec) | No* | Yes (only on 6911) | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Unicast (Only with G711ulaw codec) | No* | Yes (only on 6911) | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Shared Line | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Mixed Shared Line | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Group with Shared Line | No | No | No | No | No | No | No | No | No |
| Caller ID Display | Yes | Yes (only on 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Caller ID Blocking | No | No | No | No | No | No | No | No | No |
| Feature Access Code (FAC) ( Call Park, Pickup, Directed Pickup , Voice Hunt Group Join/Unjoin, and Temporary Logout/Login Only) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No | No | No | No | No | No | No |
| Voicemail | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Video (Only SIP-SIP/SIP-SCCP Basic Call and SIP-SIP Supplementary Services) | No* | No* | No* | Yes (except 8961) | Yes | No* | No* | Yes | No* |
| Locale Support | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Reset/Restart Phones via Reset/Restart Command | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Button Layout/Softkey Template | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Directory Services | Local Directory | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Local Speed Dial | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Personal Speed Dial | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Privacy | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Immediate Divert (iDivert) | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Enhanced iDivert | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Do Not Disturb (DND) | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| DTMF | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Feature Button / Programmable Line Keys (PLK) | No* | Yes (only on 6911) | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | No* |
| Key Expansion Module (KEM) | No* | No* | No* | Yes (only on 8961) | No* | No* | No* | Yes | No* |
| Bulk Registration Support | No* | No* | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | No* |
| Upgrading/Downgrading Phone Firmware Versions | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Secure CME | TLS | No | No | No | No | No | No | No | No | No |
| SRTP | No | No | No | No | No | No | No | No | No |
| CA | No | No | No | No | No | No | No | No | No |
| CAPF | No | No | No | No | No | No | No | No | No |
| Live Record | No | No | No | No | No | No | No | No | No |
| Enabling/Disabling KPML | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Alias Feature | No | No | No | No | No | No | No | No | No |
| Call Forward | All | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Mailbox | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Unregistered | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Night Service | No | No | No | No | No | No | No | No | No |
| Max-Length | No | No | No | No | No | No | No | No | No |
| Call Forward All Softkey on Phone | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Multicast MOH (Supported only on ISR G2) | No | No | No | No | No | No | No | No | No |
| Unicast MOH | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Night Service | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Multiple Voice Hunt Group Join/Unjoin | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Temporary Logout/Login From/To Voice Hunt Group Using FAC | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Voice Hunt Group Status Message Display On Phone for Join/Unjoin | No | No | No | No | No | No | No | No | No |
| Channel Hunt Stop | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Voice Hunt Group Statistics (Only for Static Members) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Audio Codecs | G.722 | No* | No* | No* | Yes | Yes | Yes | Yes | Yes | No* |
| G.711 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| iLBC | No* | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Translation Profile | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy Trigger Per Button | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Conference Blocking | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transfer Blocking | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| COR | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Class Codec | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transcoding (Only supported on ISR G2) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Multi-VRF (Only supported on ISR G2) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| SNMP/MIB (Supported only to get mode and number of registered phones) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Web GUI | No | No | No | No | No | No | No | No | No |
| Speed Dial | No* | Yes (only on 6911) | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy Lamp Field (BLF) | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Call Waiting | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Forced Authorization Code | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| HFS (HTTP Firmware Download) | No | No | Yes | Yes | No* | Yes | Yes | Yes | No* |
| Redial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes (only on 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Answering | Yes | Yes (only on 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| System Message | No | No | No | No | No | No | No | No | No |
| Whisper Intercom | No | No | No | No | No | No | No | No | No |
| Abbreviated Dialing | No | No | No | No | No | No | No | No | No |
| After Hours | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| SSH to Phone | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Span to PC | Yes | Yes (only on 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Web Access to Phone | Yes | Yes (only on 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Callback | No | No | No | No | No | No | No | No | No |

| Features | SCCP Phone Models |
|---|---|
| 6941 | 7925 7926 | 8941 |
| 6945 | 7942 | 8945 |
| 6961 | 7931 |  |
|  | 7962 7965 |  |
|  | 7975 |  |
| Anonymous Call Block | No | No | No |
| Auto-Answer | Yes | Yes | Yes |
| Auto Register | Yes | Yes | Yes |
| Auto Assign | Yes | Yes | Yes |
| Authenticate Register | No | No | No |
| Barge | Yes | Yes | Yes |
| cBarge/Merge | Yes | Yes | Yes |
| Call Park | Yes | Yes | Yes |
| Call Park Resume | No | No | No |
| Pickup | Group Pickup | Yes | Yes | Yes |
| Call Pickup | Yes | Yes | Yes |
| Distinctive Ring for Parked Call Recall | Yes | Yes | Yes |
| Park Monitor | Yes | Yes | Yes |
| Directed Call Park | Yes | Yes | Yes |
| Extension Mobility | Yes | Yes | Yes |
| Transfer | Alert/Semi-consult Transfer | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes |
| Blind Transfer | Yes | Yes | Yes |
| Conference | Meet-Me Conference | Yes | Yes | Yes |
| Ad-hoc Hardware Conference (Only on ISR G2) | Yes | Yes | Yes |
| Ad-hoc Software Conference | Yes | Yes | Yes |
| Video Conference | No | No | No |
| Hold/Resume | Yes | Yes | Yes |
| Intercom | Yes | Yes | Yes |
| Fast Track | No | No | No |
| Headset Answer | Yes | Yes | Yes |
| Line Label | No* | Yes | Yes |
| Mobility | Yes | Yes | Yes |
| My Phone Apps - View on Phone | Speed Dial | Yes | Yes      (except 7931) | Yes |
| Personal Speed Dial/ Fast Dial | Yes | Yes  (except 7931) | Yes |
| BLF Speed Dial | Yes | Yes (except 7931) | Yes |
| Voice Hunt Groups | Yes | Yes (except 7931) | Yes |
| After Hours | Yes | Yes (except 7931) | Yes |
| Single Number Reach (SNR) | Yes | Yes (except 7931) | Yes |
| Active Call Park List | Yes | Yes (except 7931) | Yes |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | Yes | Yes (except 7931) | Yes |
| Fast Dial | Yes | Yes (except 7931) | Yes |
| BLF Speed Dial | Yes | Yes (except 7931) | Yes |
| Single Number Reach (SNR) | Yes | Yes | Yes |
| Park Retrieval | Yes | Yes | Yes |
| Paging | Multicast (Only with G711ulaw codec) | Yes | Yes | Yes |
| Unicast (Only with G711ulaw codec) | Yes | Yes | Yes |
| Shared Line | Yes | Yes | Yes |
| Mixed Shared Line | Yes | Yes | Yes |
| Voice Hunt Group with Shared Line | Yes | Yes | Yes |
| Caller ID Display | Yes | Yes | Yes |
| Caller ID Blocking | Yes | Yes | Yes |
| Feature Access Code (FAC) | Yes | Yes | Yes |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer Recall | Yes | Yes | Yes |
| Voicemail | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes |
| Video (Only SCCP-SCCP and SCCP-SIP Basic Call and SCCP-SCCP Supplementary Services) | No* | No* | Yes |
| Locale Support | Yes | Yes | Yes |
| Reset/Restart Phones via Reset/Restart Command | Yes | Yes | Yes |
| Button Layout/Softkey Template | Yes | Yes | Yes |
| Directory Services | Local Directory | Yes | Yes | Yes |
| Local Speed Dial | Yes | Yes | Yes |
| Personal Speed Dial | Yes | Yes | Yes |
| Privacy | Yes | Yes | Yes |
| Transfer to Voice Mail (TrnsfVM) | Yes | Yes | Yes |
| Do Not Disturb (DND) | Yes | Yes | Yes |
| DTMF | Yes | Yes | Yes |
| Feature Button/Programmable Line Keys (PLK) | Yes | Yes | Yes |
| Key Expansion Module (KEM) | No* | Yes (only on 7962/7965/7975) | Yes |
| Bulk Registration Support | No | No | No |
| Upgrading/Downgrading Phone Firmware Versions | Yes | Yes | Yes |
| Secure CME | TLS | Yes | Yes | Yes |
| SRTP | Yes | Yes | Yes |
| CA | Yes | Yes | Yes |
| CAPF | Yes | Yes | Yes |
| Live Record | Yes | Yes | Yes |
| Enabling/Disabling KPML | No | No | No |
| Alias Feature | No | No | No |
| Call Forward | All | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes |
| Mailbox | No | No | No |
| Unregistered | No | No | No |
| Night Service | Yes | Yes | Yes |
| Max-Length | Yes | Yes | Yes |
| Multicast MOH (Supported only on ISR G2) | Yes | Yes | Yes |
| Unicast MOH (except SCCP to SCCP) | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | Yes | Yes | Yes |
| Night Service | Yes | Yes | Yes |
| Voice Hunt Group | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | Yes | Yes | Yes |
| Voice Hunt Group Status Message Display on Phone for Join/Unjoin | Yes | Yes | Yes |
| Multiple Voice Hunt Group Join/Unjoin | Yes | Yes | Yes |
| Voice Hunt Group Temporary Logout/Login Using FAC | Yes | Yes | Yes |
| Channel Hunt Stop | Yes | Yes | Yes |
| Voice Hunt Group Statistics | Yes | Yes | Yes |
| Ephone Hunt Group | Yes | Yes | Yes |
| Ephone Hunt Group Dynamic Join/Unjoin | Yes | Yes | Yes |
| Ephone Hunt Group Status Message Display on Phone for Join/Unjoin | Yes | Yes | Yes |
| Ephone Hunt Group Temporary Logout/Login using HLog/FAC Softkey | Yes | Yes | Yes |
| Ephone Hunt Group Statistics | Yes | Yes | Yes |
| Audio Codecs | G.722 | Yes | Yes | Yes |
| G.711 | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes |
| iLBC | Yes | Yes | Yes |
| Translation Profile | Yes | Yes | Yes |
| Busy Trigger Per Button | Yes | Yes | Yes |
| Conference Blocking | Yes | Yes | Yes |
| Transfer Blocking | Yes | Yes | Yes |
| COR | Yes | Yes | Yes |
| Voice Class Codec | No | No | No |
| Transcoding (Only supported on ISR G2) | Yes | Yes | Yes |
| Multi-VRF (Only supported on ISR G2) | Yes | Yes | Yes |
| SNMP/MIB | Yes | Yes | Yes |
| Web GUI | Yes | Yes | Yes |
| Speed Dial | Yes | Yes | Yes |
| Busy Lamp Field (BLF) | Yes | Yes | Yes |
| Call Waiting | Yes | Yes | Yes |
| Forced Authorization Code | Yes | Yes | Yes |
| HFS (HTTP Firmware Download) | No | No | No |
| Redial | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes | Yes |
| Answering | Yes | Yes | Yes |
| System Message | No* | Yes | Yes |
| Whisper Intercom | Yes | Yes | Yes |
| Intercom | Yes | Yes | Yes |
| Abbreviated Dialing | Yes | Yes | Yes |
| After Hours | Yes | Yes | Yes |
| SSH to Phone | No | Yes | Yes |
| Span to PC | Yes | Yes | Yes |
| Web Access to Phone | Yes | Yes | Yes |
| Overlay DN | Yes | Yes | Yes |
| Callback | Yes | Yes | Yes |
| Feature Blocking (CFwdAll,  Confrn, GpickUp, Park, PickUp, Trnsfer) | Yes | Yes | Yes |

| Features | SIP Phone Models |
|---|---|
| 3905 | 6901 | 6921 | 8941 | DX650 | 7821 | 7962 | Cisco IP Phone 8800 Series | 9951 | ATA-187 |
|  | 6911 | 6941 | 8945 |  | 7841 | 7965 |  | 9971 |  |
|  |  | 6945 | 8961 |  | 7861 | 7975 |  |  |  |
|  |  | 6961 |  |  |  |  |  |  |  |
| Anonymous Call Block | No | No | No | No | No | No | No | No | No | No |
| Auto-Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Auto Register | No | No | No | No | No | No | No | No | No | No |
| Auto Assign | No | No | No | No | No | No | No | No | No | No |
| Authenticate Register | No | No | No | No | No | No | No | No | No | No |
| Barge | No | No | No | No | No | No | No | No | No | No |
| cBarge/Merge | No | No | No | No | No | No | No | No | No | No |
| Call Park | No | No | No | No | No | No | No | No | No | No |
| Call Park Resume | No | No | No | No | No | No | No | No | No | No |
| Pickup | Group Pickup | No | No | No | No | No | No | No | No | No | No |
| Call Pickup | No | No | No | No | No | No | No | No | No | No |
| Distinctive Ring for Parked Call Recall | No | No | No | No | No | No | No | No | No | No |
| Park Monitor | No | No | No | No | No | No | No | No | No | No |
| Directed Call Park | No | No | No | No | No | No | No | No | No | No |
| Extension Mobility | No | No | No | No | No | No | No | No | No | No |
| Transfer | Alert/Semi-Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No | No | No | No | No | No | No | No | No | No |
| Ad-hoc Hardware Conference | No | No | No | No | No | No | No | No | No | No |
| Ad-hoc Software Conference | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Video Conference | No | No | No | No | No | No | No | No | No | No |
| Hold/Resume | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Intercom | No | No | No | No | No | No | No | No | No | No |
| Fast Track | No | No | No | No | No | No | No | No | No | No |
| Headset Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Line Label | No* | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Mobility | No | No | No | No | No | No | No | No | No | No |
| My Phone Apps - View on Phone | Speed Dial | No | No | No | No | No | No | No | No | No | No |
| Personal Speed Dial/ Fast Dial | No | No | No | No | No | No | No | No | No | No |
| BLF Speed Dial | No | No | No | No | No | No | No | No | No | No |
| Voice Hunt Groups | No | No | No | No | No | No | No | No | No | No |
| After Hours | No | No | No | No | No | No | No | No | No | No |
| Single Number Reach (SNR) | No | No | No | No | No | No | No | No | No | No |
| Active Call Park List | No | No | No | No | No | No | No | No | No | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No | No | No | No | No | No | No | No | No | No |
| Fast Dial | No | No | No | No | No | No | No | No | No | No |
| BLF Speed Dial | No | No | No | No | No | No | No | No | No | No |
| Single Number Reach (SNR) | No | No | No | No | No | No | No | No | No | No |
| Park Retrieval | No | No | No | No | No | No | No | No | No | No |
| Paging | Multicast (Only with G711ulaw codec) | No | No | No | No | No | No | No | No | No | No |
| Unicast (Only with G711ulaw codec) | No | No | No | No | No | No | No | No | No | No |
| Shared Line | No | No | No | No | No | No | No | No | No | No |
| Mixed Shared Line | No | No | No | No | No | No | No | No | No | No |
| Voice Hunt Group with Shared Line | No | No | No | No | No | No | No | No | No | No |
| Caller ID Display | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Caller ID Blocking | No | No | No | No | No | No | No | No | No | No |
| Feature Access Code (FAC) ( Only for Voice Hunt Group Join/Unjoin, and Temporary Logout/Login Only) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No | No | No | No | No | No | No | No |
| Voicemail | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Video | No | No | No | No | No | No | No | No | No | No |
| Locale Support | No | No | No | No | No | No | No | No | No | No |
| Reset/Restart Phones via Reset/Restart Command | No | No | No | No | No | No | No | No | No | No |
| Button Layout/Softkey Template | No | No | No | No | No | No | No | No | No | No |
| Directory Services | Local Directory | No | No | No | No | No | No | No | No | No | No |
| Local Speed Dial | No | No | No | No | No | No | No | No | No | No |
| Personal Speed Dial | No | No | No | No | No | No | No | No | No | No |
| Privacy | No | No | No | No | No | No | No | No | No | No |
| Immediate Divert (iDivert) | No | No | No | No | No | No | No | No | No | No |
| Enhanced iDivert | No | No | No | No | No | No | No | No | No | No |
| Do Not Disturb (DND) | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| DTMF | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Feature Button / Programmable Line Keys (PLK) | No* | Yes (only on 6911) | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Key Expansion Module (KEM) | No* | No* | No* | Yes (only 8961) | No* | No* | No* | No* | Yes | No* |
| Bulk Registration Support | No* | No* | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Upgrading/Downgrading Phone Firmware Versions | No | No | No | No | No | No | No | No | No | No |
| Secure CME | TLS | No | No | No | No | No | No | No | No | No | No |
| SRTP | No | No | No | No | No | No | No | No | No | No |
| CA | No | No | No | No | No | No | No | No | No | No |
| CAPF | No | No | No | No | No | No | No | No | No | No |
| Live Record | No | No | No | No | No | No | No | No | No | No |
| Enabling/Disabling KPML | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Alias Feature | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Forward | All | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Mailbox | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Unregistered | No | No | No | No | No | No | No | No | No | No |
| Night Service | No | No | No | No | No | No | No | No | No | No |
| Max-Length | No | No | No | No | No | No | No | No | No | No |
| Call Forward All Softkey on Phone | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Multicast MOH (Supported only on ISR G2) | No | No | No | No | No | No | No | No | No | No |
| Unicast MOH | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | No | No | No | No | No | No | No | No | No | No |
| Night Service | No | No | No | No | No | No | No | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Multiple Voice Hunt Group Join/Unjoin | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Temporary Logout/Login From/To Voice Hunt Group Using FAC | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Voice Hunt Group Status Message Display on Phone for Join/Unjoin | No | No | No | No | No | No | No | No | No | No |
| Channel Hunt Stop | No | No | No | No | No | No | No | No | No | No |
| Voice Hunt Group Statistics (Only for Static Members) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Audio Codecs | G.722 | No* | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| G.711 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| iLBC | No* | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Translation Profile | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy Trigger Per Button | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Conference Blocking | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transfer Blocking | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| COR | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Class Codec | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transcoding (Only supported on ISR G2) | No | No | No | No | No | No | No | No | No | No |
| Multi-VRF (Only supported on ISR G2) | No | No | No | No | No | No | No | No | No | No |
| SNMP/MIB (Supported only to get mode and number of registered phones) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Web GUI | No | No | No | No | No | No | No | No | No | No |
| Speed Dial | No* | Yes (only on 6911) | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | Yes | No |
| Busy Lamp Field (BLF) | No | No | No | No | No | No | No | No | No | No |
| Call Waiting | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Forced Authorization Code | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| HFS (HTTP Firmware Download) | No | No | No | No | No | No | No | No | No | No |
| Redial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes (only 6911) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Answering | Yes | Yes (only 6911) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| System Message | No* | No* | Yes | Yes | No* | Yes | Yes | Yes | Yes | No* |
| Whisper Intercom | No | No | No | No | No | No | No | No | No | No |
| Abbreviated Dialing | No | No | No | No | No | No | No | No | No | No |
| After Hours | No | No | No | No | No | No | No | No | No | No |
| SSH to phone | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Span to PC | Yes | Yes (only 6911) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Web Access to Phone | Yes | Yes (only 6911) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Callback | No | No | No | No | No | No | No | No | No | No |

| Features | SCCP Phone Models |
|---|---|
| 6941 | 7925 7926 | 8941 |
| 6945 | 7942 | 8945 |
| 6961 | 7931 |  |
|  | 7962 7965 |  |
|  | 7975 |  |
| Anonymous Call Block | No | No | No |
| Auto-Answer | Yes | Yes | Yes |
| Auto Register | No | No | No |
| Auto Assign | No | No | No |
| Authenticate Register | No | No | No |
| Barge | No | No | No |
| cBarge/Merge | No | No | No |
| Call Park | No | No | No |
| Call Park Resume | No | No | No |
| Pickup | Group Pickup | No | No | No |
| Call Pickup | No | No | No |
| Distinctive Ring for Parked Call Recall | No | No | No |
| Park Monitor | No | No | No |
| Directed Call Park | No | No | No |
| Extension Mobility | No | No | No |
| Transfer | Alert/Semi-consult Transfer | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes |
| Blind Transfer | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No | No | No |
| Ad-hoc Hardware Conference | No | No | No |
| Ad-hoc Software Conference | Yes | Yes | Yes |
| Video Conference | No | No | No |
| Hold/Resume | Yes | Yes | Yes |
| Intercom | No | No | No |
| Fast Track | No | No | No |
| Headset Answer | Yes | Yes | Yes |
| Line Label | No* | Yes | Yes |
| Mobility | No | No | No |
| My Phone Apps - View on Phone | Speed Dial | No | No | No |
| Personal Speed Dial/ Fast Dial | No | No | No |
| BLF Speed Dial | No | No | No |
| Voice Hunt Groups | No | No | No |
| After Hours | No | No | No |
| Single Number Reach (SNR) | No | No | No |
| Active Call Park List | No | No | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No | No | No |
| Fast Dial | No | No | No |
| BLF Speed Dial | No | No | No |
| Single Number Reach (SNR) | No | No | No |
| Park Retrieval | No | No | No |
| Paging | Multicast (Only with G711ulaw codec) | No | No | No |
| Unicast (Only with G711ulaw codec) | No | No | No |
| Shared Line | Yes | Yes | Yes |
| Mixed Shared Line | No | No | No |
| Voice Hunt Group with Shared Line | Yes | Yes | Yes |
| Caller ID Display | Yes | Yes | Yes |
| Caller ID Blocking | No | No | No |
| Feature Access Code (FAC) | Yes | Yes | Yes |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No |
| Voicemail | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes |
| Video | No | No | No |
| Locale Support | No | No | No |
| Reset/Restart Phones via Reset/Restart Command | Yes | Yes | Yes |
| Button Layout/Softkey Template | No | No | No |
| Directory Services | Local Directory | No | No | No |
| Local Speed Dial | No | No | No |
| Personal Speed Dial | No | No | No |
| Privacy | No | No | No |
| Transfer to Voice Mail (TrnsfVM) | No | No | No |
| Do Not Disturb (DND) | Yes | Yes | Yes |
| DTMF | No | No | No |
| Feature Button/Programmable Line Keys (PLK) | Yes | Yes | Yes |
| Key Expansion Module (KEM) | No* | Yes (only on 7962/7965/7975) | Yes |
| Bulk Registration Support | No | No | No |
| Upgrading/Downgrading Phone Firmware Versions | No | No | No |
| Secure CME | TLS | Yes | Yes | Yes |
| SRTP | Yes | Yes | Yes |
| CA | Yes | Yes | Yes |
| CAPF | Yes | Yes | Yes |
| Live Record | No | No | No |
| Enabling/Disabling KPML | No | No | No |
| Alias Feature | Yes | Yes | Yes |
| Call-Forward | All | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes |
| Mailbox | No | No | No |
| Unregistered | No | No | No |
| Night Service | No | No | No |
| Max-Length | No | No | No |
| Multicast MOH (Supported only on ISR G2) | Yes | Yes | Yes |
| Unicast MOH (except SCCP to SCCP) | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | Yes | Yes | Yes |
| Night Service | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | No | No | No |
| Voice Hunt Group Status Message Display on Phone for Join/Unjoin | No | No | No |
| Multiple Voice Hunt Group Join/Unjoin | No | No | No |
| Voice Hunt Group Temporary Logout/Login Using FAC | No | No | No |
| Channel Hunt Stop | No | No | No |
| Voice Hunt Group Statistics | Yes | Yes | Yes |
| Ephone Hunt Group | No | No | No |
| Ephone Hunt Group Dynamic Join/Unjoin | No | No | No |
| Ephone Hunt Group Status Message Display on Phone for Join/Unjoin | No | No | No |
| Ephone Hunt Group Temporary Logout/Login Using HLog/FAC Softkey | No | No | No |
| Ephone Hunt Group Statistics | No | No | No |
| Audio Codecs | G.722 | Yes | Yes | Yes |
| G.711 | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes |
| iLBC | Yes | Yes | Yes |
| Translation Profile | Yes | Yes | Yes |
| Busy Trigger Per Button | No | No | No |
| Conference Blocking | No | No | No |
| Transfer Blocking | No | No | No |
| COR | Yes | Yes | Yes |
| Voice Class Codec | No | No | No |
| Transcoding (Only supported on ISR G2) | No | No | No |
| Multi-VRF (Only supported on ISR G2) | No | No | No |
| SNMP/MIB | Yes | Yes | Yes |
| Web GUI | Yes | Yes | Yes |
| Speed Dial | Yes | Yes | Yes |
| Busy Lamp Field (BLF) | No | No | No |
| Call Waiting | Yes | Yes | Yes |
| Forced Authorization Code | Yes | Yes | Yes |
| HFS (HTTP Firmware Download) | No | No | No |
| Redial | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes | Yes |
| Answering | Yes | Yes | Yes |
| System Message | Yes | Yes | Yes |
| Whisper Intercom | No | No | No |
| Intercom | No | No | No |
| Abbreviated Dialing | No | No | No |
| After Hours | Yes | Yes | Yes |
| SSH to Phone | No | Yes | Yes |
| Span to PC | Yes | Yes | Yes |
| Web Access to Phone | Yes | Yes | Yes |
| Overlay DN | No | No | No |
| Callback | No | No | No |
| Feature Blocking (CFwdAll,  Confrn, GpickUp, Park, PickUp, Trnsfer) | No | No | No |

| Features | SIP Phone Models |
|---|---|
| 3905 | 6901 | 6921 | 8941 | DX650 | 7821 | 7962 | 9951 | ATA-187 |
|  | 6911 | 6941 | 8945 |  | 7841 | 7965 | 9971 |  |
|  |  | 6945 | 8961 |  | 7861 | 7975 |  |  |
|  |  | 6961 |  |  |  |  |  |  |
| Anonymous Call Block | No | No | No | No | No | No | No | No | No |
| Auto-Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Auto Register | No | No | No | No | No | No | No | No | No |
| Auto Assign | No | No | No | No | No | No | No | No | No |
| Authenticate Register | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* |
| Barge | No | No | No | No | No | No | No | No | No |
| cBarge/Merge | No | No | No | No | No | No | No | No | No |
| Call Park | No | No | No | No | No | No | No | No | No |
| Call Park Resume | No | No | No | No | No | No | No | No | No |
| Pickup (Only Using FAC) | Group Pickup | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | No* |
| Call Pickup | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | No* |
| Distinctive Ring for Parked Call Recall | No | No | No | No | No | No | No | No | No |
| Park Monitor | No | No | No | No | No | No | No | No | No |
| Directed Call Park | No | No | No | No | No | No | No | No | No |
| Extension Mobility | No | No | No | No | No | No | No | No | No |
| Transfer | Alert/Semi-Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No | No | No | No | No | No | No | No | No |
| Ad-hoc Hardware Conference | No | No | No | No | No | No | No | No | No |
| Ad-hoc Software Conference | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Video Conference | No | No | No | No | No | No | No | No | No |
| Hold/Resume | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Intercom | No | No | No | No | No | No | No | No | No |
| Fast Track | No | No | No | No | No | No | No | No | No |
| Headset Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Line Label | No* | No* | No* | Yes | Yes | Yes | Yes | Yes | No* |
| Mobility | No | No | No | No | No | No | No | No | No |
| My Phone Apps - View on Phone | Speed Dial | No | No | No | No | No | No | No | No | No |
| Personal Speed Dial/ Fast Dial | No | No | No | No | No | No | No | No | No |
| BLF Speed Dial | No | No | No | No | No | No | No | No | No |
| Voice Hunt Groups | No | No | No | No | No | No | No | No | No |
| After Hours | No | No | No | No | No | No | No | No | No |
| Single Number Reach (SNR) | No | No | No | No | No | No | No | No | No |
| Active Call Park List | No | No | No | No | No | No | No | No | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No | No | No | No | No | No | No | No | No |
| Fast Dial | No | No | No | No | No | No | No | No | No |
| BLF Speed Dial | No | No | No | No | No | No | No | No | No |
| Single Number Reach (SNR) | No | No | No | No | No | No | No | No | No |
| Park Retrieval | No | No | No | No | No | No | No | No | No |
| Paging | Multicast (Only with G711ulaw codec) | No | No | No | No | No | No | No | No | No |
| Unicast (Only with G711ulaw codec) | No | No | No | No | No | No | No | No | No |
| Shared Line | No* | No* | No* | Yes | No* | Yes | No* | Yes | No |
| Mixed Shared Line | No* | No* | No* | Yes | No* | Yes | No* | Yes | No |
| Voice Hunt Group with Shared Line | No | No | No | No | No | No | No | No | No |
| Caller ID Display | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Caller ID Blocking | No | No | No | No | No | No | No | No | No |
| Feature Access Code (FAC) ( Only for Voice Hunt Group Join/Unjoin, and Temporary Logout/Login Only) | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | No* |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No | No | No | No | No | No | No |
| Voicemail | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Video (Only SIP-SIP/SIP-SCCP Basic Call and SIP-SIP Supplementary Services) | No* | No* | No* | Yes* (except 8861) | No | No* | No* | Yes* | No* |
| Locale Support | No | No | No | No | No | No | No | No | No |
| Reset/Restart Phones via Reset/Restart Command | No | No | No | No | No | No | No | No | No |
| Button Layout/Softkey Template | No | No | No | No | No | No | No | No | No |
| Directory Services | Local Directory | No | No | No | No | No | No | No | No | No |
| Local Speed Dial | No | No | No | No | No | No | No | No | No |
| Personal Speed Dial | No | No | No | No | No | No | No | No | No |
| Privacy(On Hold) | No* | No* | No* | Yes* | No* | Yes* | No* | Yes* | No* |
| Immediate Divert (iDivert) | No | No | No | No | No | No | No | No | No |
| Enhanced iDivert | No | No | No | No | No | No | No | No | No |
| Do Not Disturb (DND) | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| DTMF | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* |
| Feature Button / Programmable Line Keys (PLK) | No* | Yes (only on 6911) | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | No* |
| Key Expansion Module (KEM) | No* | No* | No* | Yes (only 8961) | No* | No* | No* | Yes | No* |
| Bulk Registration Support | No* | No* | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | No* |
| Upgrading/Downgrading Phone Firmware Versions | No | No | No | No | No | No | No | No | No |
| Secure CME | TLS | No | No | No | No | No | No | No | No | No |
| SRTP | No | No | No | No | No | No | No | No | No |
| CA | No | No | No | No | No | No | No | No | No |
| CAPF | No | No | No | No | No | No | No | No | No |
| Live Record | No | No | No | No | No | No | No | No | No |
| Enabling/Disabling KPML | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | No* |
| Alias Feature | No | No | No | No | No | No | No | No | No |
| Call Forward | All | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Mailbox | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Unregistered | No | No | No | No | No | No | No | No | No |
| Night-Service | No | No | No | No | No | No | No | No | No |
| Max-Length | No | No | No | No | No | No | No | No | No |
| Call Forward All Softkey on Phone | No* | No* | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Multicast MOH (Supported only on ISR G2) | No | No | No | No | No | No | No | No | No |
| Unicast MOH | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | No | No | No | No | No | No | No | No | No |
| Night Service | No | No | No | No | No | No | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | No* |
| Multiple Voice Hunt Group Join/Unjoin | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | No* |
| Temporary Logout/Login From/To Voice Hunt Group Using FAC | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | No* |
| Voice Hunt Group Status Message Display On Phone for Join/Unjoin | No | No | No | No | No | No | No | No | No |
| Channel Hunt Stop | No | No | No | No | No | No | No | No | No |
| Voice Hunt Group Statistics (Only for Static Members) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Audio Codecs | G.722 | No* | No* | No* | Yes | Yes | Yes | Yes | Yes | No* |
| G.711 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| iLBC | No* | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Translation Profile | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* |
| Busy Trigger Per Button | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* |
| Conference Blocking | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* |
| Transfer Blocking | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* |
| COR | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Class Codec | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* |
| Transcoding (Only supported on ISR G2) | No | No | No | No | No | No | No | No | No |
| Multi-VRF (Only supported on ISR G2) | No | No | No | No | No | No | No | No | No |
| SNMP/MIB (Supported only to get mode and number of registered phones) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Web GUI | No | No | No | No | No | No | No | No | No |
| Speed Dial | No* | Yes (only on 6911) | Yes (except 6921) | Yes | Yes | Yes | Yes | Yes | No |
| Busy Lamp Field (BLF) | No* | No* | No* | Yes* | No* | Yes* | No* | Yes* | No* |
| Call Waiting | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Forced Authorization Code | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* | Yes* |
| HFS (HTTP Firmware Download) | No | No | No | No | No | No | No | No | No |
| Redial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes (only 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Answering | Yes | Yes (only 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| System Message | No* | No* | Yes* | Yes* | No* | Yes* | Yes | Yes | No* |
| Whisper Intercom | No | No | No | No | No | No | No | No | No |
| Abbreviated Dialing | No | No | No | No | No | No | No | No | No |
| After Hours | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| SSH to phone | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Span to PC | Yes | Yes (only 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Web Access to Phone | Yes | Yes (only 6911) | Yes | Yes | Yes | Yes | Yes | Yes | No* |
| Callback | No | No | No | No | No | No | No | No | No |

| Features | SCCP Phone Models |
|---|---|
| 6941 | 7925 7926 | 8941 |
| 6945 | 7942 | 8945 |
| 6961 | 7931 |  |
|  | 7962 7965 |  |
|  | 7975 |  |
| Anonymous Call Block | No | No | No |
| Auto-Answer | Yes | Yes | Yes |
| Auto Register | No | No | No |
| Auto Assign | No | No | No |
| Authenticate Register | No | No | No |
| Barge | No | No | No |
| cBarge/Merge | No | No | No |
| Call Park | Yes | Yes | Yes |
| Call Park Resume | No | No | No |
| Pickup | Group Pickup | Yes | Yes | Yes |
| Call Pickup | Yes | Yes | Yes |
| Distinctive Ring for Parked Call Recall | No | No | No |
| Park Monitor | Yes | Yes | Yes |
| Directed Call Park | Yes* | Yes* | Yes* |
| Extension Mobility | No | No | No |
| Transfer | Alert/Semi-consult Transfer | Yes | Yes | Yes |
| Attended/Consult Transfer | Yes | Yes | Yes |
| Blind Transfer | Yes | Yes | Yes |
| Conference | Meet-Me Conference | No | No | No |
| Ad-hoc Hardware Conference (Only on ISR G2) | No | No | No |
| Ad-hoc Software Conference | Yes | Yes | Yes |
| Video Conference | No | No | No |
| Hold/Resume | Yes | Yes | Yes |
| Intercom | No | No | No |
| Fast Track | No | No | No |
| Headset Answer | Yes | Yes | Yes |
| Line Label | No* | Yes | Yes |
| Mobility | No | No | No |
| My Phone Apps - View on Phone | Speed Dial | No | No | No |
| Personal Speed Dial/ Fast Dial | No | No | No |
| BLF Speed Dial | No | No | No |
| Voice Hunt Groups | No | No | No |
| After Hours | No | No | No |
| Single Number Reach (SNR) | No | No | No |
| Active Call Park List | No | No | No |
| My Phone Apps - Add/Delete/Modify from Phone | Speed Dial | No | No | No |
| Fast Dial | No | No | No |
| BLF Speed Dial | No | No | No |
| Single Number Reach (SNR) | No | No | No |
| Park Retrieval | Yes | Yes | Yes |
| Paging | Multicast (Only with G711ulaw codec) | No | No | No |
| Unicast (Only with G711ulaw codec) | No | No | No |
| Shared Line | Yes | Yes | Yes |
| Mixed Shared Line | Yes | Yes | Yes |
| Voice Hunt Group with Shared Line | Yes | Yes | Yes |
| Caller ID Display | Yes | Yes | Yes |
| Caller ID Blocking | No | No | No |
| Feature Access Code (FAC) | Yes* | Yes* | Yes* |
| Call Forward to Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer to a Voice Hunt Group | Yes | Yes | Yes |
| Call Transfer Recall | No | No | No |
| Voicemail | Yes | Yes | Yes |
| Message Waiting Indicator (MWI) | Yes | Yes | Yes |
| Video | No | No | No |
| Locale Support | No | No | No |
| Reset/Restart Phones via Reset/Restart Command | Yes | Yes | Yes |
| Button Layout/Softkey Template | No | No | No |
| Directory Services | Local Directory | No | No | No |
| Local Speed Dial | No | No | No |
| Personal Speed Dial | No | No | No |
| Privacy | No | No | No |
| Transfer to Voice Mail (TrnsfVM) | No | No | No |
| Do Not Disturb (DND) | Yes | Yes | Yes |
| DTMF | No | No | No |
| Feature Button/Programmable Line Keys (PLK) | Yes | Yes | Yes |
| Key Expansion Module (KEM) | No* | Yes (only on 7962/7965/7975) | Yes |
| Bulk Registration Support | No | No | No |
| Upgrading/Downgrading Phone Firmware Versions | No | No | No |
| Secure CME | TLS | No | No | No |
| SRTP | No | No | No |
| CA | No | No | No |
| CAPF | No | No | No |
| Live Record | No | No | No |
| Enabling/Disabling KPML | No | No | No |
| Alias Feature | No | No | No |
| Call Forward | All | Yes | Yes | Yes |
| Busy | Yes | Yes | Yes |
| No Answer | Yes | Yes | Yes |
| Mailbox | No | No | No |
| Unregistered | No | No | No |
| Night Service | No | No | No |
| Max-Length | No | No | No |
| Multicast MOH (Supported only on ISR G2) | Yes | Yes | Yes |
| Unicast MOH (except SCCP to SCCP) | Yes | Yes | Yes |
| Basic Automatic Call Distribution (B-ACD) | Yes* | Yes* | Yes* |
| Night Service | No | No | No |
| Voice Hunt Group | Yes | Yes | Yes |
| Voice Hunt Group Dynamic Join/Unjoin | Yes* | Yes* | Yes* |
| Voice Hunt Group Status Message Display on Phone for Join/Unjoin | Yes* | Yes* | Yes* |
| Multiple Voice Hunt Group Join/Unjoin | Yes* | Yes* | Yes* |
| Voice Hunt Group Temporary Logout/Login Using FAC | Yes* | Yes* | Yes* |
| Channel Hunt Stop | No | No | No |
| Voice Hunt Group Statistics | Yes | Yes | Yes |
| Ephone Hunt Group | Yes | Yes | Yes |
| Ephone Hunt Group Dynamic Join/Unjoin | Yes* | Yes* | Yes* |
| Ephone Hunt Group Status Message Display on Phone for Join/Unjoin | Yes* | Yes* | Yes* |
| Ephone Hunt Group Temporary Logout/Login Using HLog/FAC Softkey | Yes* | Yes* | Yes* |
| Ephone Hunt Group Statistics | Yes | Yes | Yes |
| Audio Codecs | G.722 | Yes | Yes | Yes |
| G.711 | Yes | Yes | Yes |
| G.729 | Yes | Yes | Yes |
| iLBC | Yes | Yes | Yes |
| Translation Profile | Yes* | Yes* | Yes* |
| Busy Trigger Per Button | No | No | No |
| Conference Blocking | Yes* | Yes* | Yes* |
| Transfer Blocking | No | No | No |
| COR | Yes | Yes | Yes |
| Voice Class Codec | No | No | No |
| Transcoding (Only supported on ISR G2) | No | No | No |
| Multi-VRF (Only supported on ISR G2) | No | No | No |
| SNMP/MIB | Yes | Yes | Yes |
| Web GUI | Yes | Yes | Yes |
| Speed Dial | Yes | Yes | Yes |
| Busy Lamp Field (BLF) | Yes* | Yes* | Yes* |
| Call Waiting | Yes | Yes | Yes |
| Forced Authorization Code | Yes | Yes | Yes |
| HFS (HTTP Firmware Download) | No | No | No |
| Redial | Yes | Yes | Yes |
| Speakerphone | Dialing | Yes | Yes | Yes |
| Answering | Yes | Yes | Yes |
| System Message | Yes* | Yes* | Yes* |
| Whisper Intercom | No | No | No |
| Intercom | No | No | No |
| Abbreviated Dialing | No | No | No |
| After Hours | Yes | Yes | Yes |
| SSH to Phone | No | Yes | Yes |
| Span to PC | Yes | Yes | Yes |
| Web Access to Phone | Yes | Yes | Yes |
| Overlay DN | No | No | No |
| Callback | No | No | No |
| Feature Blocking (CFwdAll,  Confrn, GpickUp, Park, PickUp, Trnsfer) | No | No | No |

| Number of Keys | 8961 | 9951 | 9971 | 8851/51NR | 8861 | 8865 |
|---|---|---|---|---|---|---|
| Fixed feature keys | 5 | 5 | 6 | 5 | 5 | 5 |
| Line keys | 5 | 5 | 6 | 5 | 5 | 5 |
| Programmable soft keys | 5 | 5 | 6 | 5 | 5 | 5 |

| Number of Keys | Without KEMs | With CP-BEKEM | With A-KEM and V-KEM |
|---|---|---|---|
| Busy-Lamp-Field speed dial | 1 to 9 | 1 to 112 | 88 |
| Directory number | 1 to 10 | 1 to 113 | 89 |
| Speed dial | 1 to 9 | 1 to 112 | 88 |

| Cisco Unified SIP IP Phones | Maximum Number of Supported KEMs | Maximum Number of Additional Lines or Buttons (BEKEM) | Maximum Number of Additional Lines or Buttons (A-KEM, V-KEM) |
|---|---|---|---|
| 8961 | 1 | 36 | – |
| 8851/51NR | 2 | 72 | 56 |
| 9951 | 2 | 72 | – |
| 8861 | 3 | 108 | 84 |
| 8865 | 3 | 108 | 84 |
| 9971 | 3 | 108 | - |

| Cisco Unified SIP Phone Model | Recommended Fast Track Configuration | Unified CME Versions Supported | Comments | Supported Locale Package Version |
|---|---|---|---|---|
| ATA 191 |  |  |  |  |
| ATA 190 | voice register pool-type ATA-190 description “Cisco Analog Phone Adapter ATA 190” reference-pooltype ATA-187 | Unified CME 10.5 onwards until native support is added | Cisco Analog Phone Adapter ATA 190 | Not supported |
| 7811 | voice register pool-type  7811 xml-config maxNumCalls 4 xml-config busyTrigger 4 description Cisco IP Phone 7811 reference-pooltype 6921 | Unified CME 10.5 |  | 10.5 |
| 7821 | voice register pool-type 7821 description Cisco IP Phone 7821 reference-pooltype 6921 | Unified CME 10.0 (15.3(3)M) to Unified CME 10.5 (15.4(3)M) | 7821 phone is a hardware revision of the earlier 6921 phone. | 10.5 |
| 7832 | voice register pool-type  7832 description Cisco IP Phone 7832 reference-pooltype 7811 | Unified CME 12.3 |  | 12.1 |
| 7841 | voice register pool-type 7841 description Cisco IP Phone 7841 reference-pooltype 6941 | Unified CME 10.0 (15.3(3)M) to Unified CME 10.5 (15.4(3)M) | 7841 phone is a hardware revision of the earlier 6941 phone | 10.5 |
| 7861 | voice register pool-type 7861 description Cisco IP Phone 7861 reference-pooltype 6961 num-lines 16 | Unified CME 10.0 (15.3(3)M) to Unified CME 10.5 (15.4(3)M) | 7861 phone is a hardware revision of the earlier 6961 phone. This phone has 16 lines whereas 6961 has 12 lines. | 10.5 |
| 8811 | voice register pool-type  8811 xml-config maxNumCalls 200 xml-config busyTrigger 200 num-lines 24 description Cisco IP Phone 8811 reference-pooltype 9971 | Unified CME 10.5 | 8811 is a conference station. | 10.5 |
| 8821 | voice register pool-type  8821 xml-config maxNumCalls 6 xml-config busyTrigger 6  num-lines 114 description Cisco IP Phone 8821 reference-pooltype 9971 | Unified CME 10.5 |  | 10.5 |
| 8831 | voice register pool-type  8831 xml-config maxNumCalls 4 xml-config busyTrigger 4 description Cisco IP Phone 8831 reference-pooltype 9971 | Unified CME 10.0 (15.3(3)M) until built in phone support is added on Unified CME | 8831 is an IP Conference Phone. | 10.5 |
| 8832 | voice register pool-type  8832 description Cisco IP Phone 8832 reference-pooltype 8811 | Unified CME 12.3 |  | 12.1 |
| 8841 | voice register pool-type 8841 xml-config maxNumCalls 200 xml-config busyTrigger 200 num-lines 24 description Cisco IP Phone 8841 reference-pooltype 8961 | Unified CME 10.5 |  | 10.5 |
| 8851 | voice register pool-type  8851 xml-config maxNumCalls 6 xml-config busyTrigger 6  num-lines 77 description Cisco IP Phone 8851 reference-pooltype 9951 | Unified CME 10.5 |  | 10.5 |
| 8851NR | voice register pool-type  8851 xml-config maxNumCalls 6 xml-config busyTrigger 6  num-lines 77 description Cisco IP Phone 8851 reference-pooltype 9951 | Unified CME 10.5 | 8851 has the same feature set as 8851NR, except support for Bluetooth. | 10.5 |
| 8861 | voice register pool-type  8861 xml-config maxNumCalls 6 xml-config busyTrigger 6  num-lines 114 description Cisco IP Phone 8861 reference-pooltype 9971 | Unified CME 10.5 |  | 10.5 |

| Features | Phone Models |
|---|---|
| ATA 190 | 7811 | 7821 | 7841 | 7861 | 8811 | 8831 | 8841 | 8845 | 8851 | 8851NR | 8861 |
| Ad-hoc Hardware Conference (Only on ISR G2) | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Ad-hoc Software Conference Call | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Forward All Softkey | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Forward All | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call forward Busy | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Forward No Answer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Park | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Park Retrieval | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Call Pickup | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Directory Services | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Do Not Disturb | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| DTMF (RTP-NTE) | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Extension Mobility | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Group Pickup | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Headset Mode Answer | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Hold or Resume | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Line Label (name under pool) | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Message Waiting Indicator | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Music on Hold | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| My Phone Apps – View on Phone | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Redial | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Single Number Reach(SNR) | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Softkey Template | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Speakerphone Dialing/ Answering | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Shared Line | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transcoding | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Transfer | Consult | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Alert | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voicemail | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice Hunt Groups | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |