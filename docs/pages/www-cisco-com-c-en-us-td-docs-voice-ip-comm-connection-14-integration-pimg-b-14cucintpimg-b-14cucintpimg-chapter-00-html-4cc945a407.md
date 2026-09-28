---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-integration-pimg-b-14cucintpimg-b-14cucintpimg-chapter-00-html-4cc945a407
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/pimg/b_14cucintpimg/b_14cucintpimg_chapter_00.html
retrieved_at: 2026-08-16T18:36:34.718767+00:00
---

PIMG Integration Guide for Cisco Unity Connection Release 14

# PIMG Integration Guide for Cisco Unity Connection Release 14

Updated: March 25, 2021

Chapter: Introduction

## Chapter: Introduction

# Introduction

### Introduction

## Integration Description

Cisco\\ Unity Connection supports PIMG integrations with the following phone systems.

Phone System

Integration Type

Supported PIMG Units

Alcatel 4400

DTMF (analog)

Analog PIMG units (PIMG80LS or DMG1008LS)

Any phone system that provides a serial data link (SMDI, MCI, or MD-110 protocol) to the master PIMG unit

Serial (SMDI, MCI, or MD-110)

Analog PIMG units (PIMG80LS or DMG1008LS)

Avaya Definity G3

Digital

Digital PIMG units (PIMG80PBXDNI or DMG1008DNI)

Avaya Definity ProLogix

Digital

Digital PIMG units (PIMG80PBXDNI or DMG1008DNI)

Avaya S8300, Avaya S8500, and Avaya S8700

Digital

Digital PIMG units (PIMG80PBXDNI or DMG1008DNI)

Mitel SX-200

Digital

Digital Mitel PIMG units (PIMG80MTLPBXDNI or DMG1008MTLDNI)

Mitel SX-2000

Digital

Digital Mitel PIMG units (PIMG80MTLPBXDNI or DMG1008MTLDNI)

NEC NEAX 2400

Digital

Digital PIMG units (PIMG80PBXDNI or DMG1008DNI)

Nortel Meridian 1 (includes Succession and SL 1)

Digital

Digital PIMG units (PIMG80PBXDNI or DMG1008DNI)

Rolm 9751 9005

Digital

Digital Rolm PIMG units (PIMB80RLMPBXDNI or DMG1008RLMDNI)

Rolm 9751 9006

Digital

Digital Rolm PIMG units (PIMB80RLMPBXDNI or DMG1008RLMDNI)

Siemens Hicom 150

DTMF (analog)

Analog PIMG units (PIMG80LS or DMG1008LS)

Siemens Hicom 300 E (European)

DTMF (analog)

Analog PIMG unit (PIMG80LS or DMG1008LS)

Siemens Hicom 300-series E (North American)

Digital

Digital PIMG units (PIMG80PBXDNI or DMG1008DNI)

Siemens Hipath 3550

DTMF (analog)

Analog PIMG units (PIMG80LS or DMG1008LS)

Siemens Hipath 4000

DTMF (analog)

Analog PIMG units (PIMG80LS or DMG1008LS)

### Digital
                           	 Integration with Digital PIMG Units

The phone system sends call information, MWI requests, and voice
                              		connections through the digital lines, which connect the phone system to the
                              		PIMG units (media gateways). The PIMG units communicate with the Unity
                              		Connection server through the LAN or WAN using Session Initiation Protocol
                              		(SIP). Figure 1-1 shows the required connections for a digital integration
                              		using digital PIMG units.

### DTMF Integration
                           	 with Analog PIMG Units

The phone system sends call information, MWI requests, and voice
                              		connections through the analog lines, which connect the phone system to the
                              		PIMG units (media gateways). The PIMG units communicate with the Unity
                              		Connection server through the LAN or WAN using Session Initiation Protocol
                              		(SIP). Figure 1-2 shows the required connections for a DTMF integration using
                              		analog PIMG units.

### Serial (SMDI, MCI,
                           	 or MD-110) Integration with Analog PIMG Units

The phone system sends call information and MWI requests through
                              		the data link, which is an RS-232 serial cable that connects the phone system
                              		and the master PIMG unit (media gateway). Voice connections are sent through
                              		the analog lines between the phone system and the PIMG units. The PIMG units
                              		communicate with the Unity Connection server through the LAN or WAN using
                              		Session Initialization Protocol (SIP). Figure 1-3 shows the required
                              		connections for a serial integration using analog PIMG units.

## Call Information

The phone system sends the following information with forwarded calls:

The extension of the called party

The extension of the calling party (for internal calls) or the phone number of the calling party (if it is an external call
                                 and the system uses caller ID)

The reason for the forward (the extension is busy, does not answer, or is set to forward all calls)

Unity Connection uses this information to answer the call appropriately. For example, a call forwarded to Unity Connection
                           is answered with the personal greeting of the user. If the phone system routes the call without this information, Unity Connection
                           answers with the opening greeting.

Serial integrations send requests to turn on and turn off MWIs through the data link.

## Integration Functionality

The PIMG integration provides the following integration features:

Call forward to personal greeting

Call forward to busy greeting

Caller ID

Easy message access (a user can retrieve messages without entering an ID because Unity Connection identifies the user based
                                 on the extension from which the call originated; a password may be required)

Identified user messaging (Unity Connection identifies the user who leaves a message during a forwarded internal call, based
                                 on the extension from which the call originated)

Message waiting indication (MWI)

## Integrations with
                        	 Multiple Phone Systems

Unity Connection can be integrated with two or more phone systems at one time. For information on the maximum supported combinations
                           and instructions for integrating Unity Connection with multiple phone systems, see the Multiple Phone System Integration Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/multiple/b_cuc15intmultiple.html .

## Centralized Voice
                        	 Messaging

Unity Connection supports centralized voice messaging through the phone system, which supports various inter-phone system
                           networking protocols including proprietary protocols such as Avaya DCS, Nortel MCDN, or Siemens CorNet, and standards-based
                           protocols such as QSIG or DPNSS. Note that centralized voice messaging is a function of the phone system and its inter-phone
                           system networking, not voicemail. Unity Connection supports centralized voice messaging as long as the phone system and its
                           inter-phone system networking are properly configured. For details, see the “ Centralized Voice Messaging ” section in the “Integrating Cisco Unity Connection with the Phone System” chapter of the Design Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html .

| Phone System | Integration Type | Supported PIMG Units |
|---|---|---|
| Alcatel 4400 | DTMF (analog) | Analog PIMG units (PIMG80LS or DMG1008LS) |
| Any phone system that provides a serial data link (SMDI, MCI, or MD-110 protocol) to the master PIMG unit | Serial (SMDI, MCI, or MD-110) | Analog PIMG units (PIMG80LS or DMG1008LS) |
| Avaya Definity G3 | Digital | Digital PIMG units (PIMG80PBXDNI or DMG1008DNI) |
| Avaya Definity ProLogix | Digital | Digital PIMG units (PIMG80PBXDNI or DMG1008DNI) |
| Avaya S8300, Avaya S8500, and Avaya S8700 | Digital | Digital PIMG units (PIMG80PBXDNI or DMG1008DNI) |
| Mitel SX-200 | Digital | Digital Mitel PIMG units (PIMG80MTLPBXDNI or DMG1008MTLDNI) |
| Mitel SX-2000 | Digital | Digital Mitel PIMG units (PIMG80MTLPBXDNI or DMG1008MTLDNI) |
| NEC NEAX 2400 | Digital | Digital PIMG units (PIMG80PBXDNI or DMG1008DNI) |
| Nortel Meridian 1 (includes Succession and SL 1) | Digital | Digital PIMG units (PIMG80PBXDNI or DMG1008DNI) |
| Rolm 9751 9005 | Digital | Digital Rolm PIMG units (PIMB80RLMPBXDNI or DMG1008RLMDNI) |
| Rolm 9751 9006 | Digital | Digital Rolm PIMG units (PIMB80RLMPBXDNI or DMG1008RLMDNI) |
| Siemens Hicom 150 | DTMF (analog) | Analog PIMG units (PIMG80LS or DMG1008LS) |
| Siemens Hicom 300 E (European) | DTMF (analog) | Analog PIMG unit (PIMG80LS or DMG1008LS) |
| Siemens Hicom 300-series E (North American) | Digital | Digital PIMG units (PIMG80PBXDNI or DMG1008DNI) |
| Siemens Hipath 3550 | DTMF (analog) | Analog PIMG units (PIMG80LS or DMG1008LS) |
| Siemens Hipath 4000 | DTMF (analog) | Analog PIMG units (PIMG80LS or DMG1008LS) |

| Note | Serial integrations send requests to turn on and turn off MWIs through the data link. |
|---|---|