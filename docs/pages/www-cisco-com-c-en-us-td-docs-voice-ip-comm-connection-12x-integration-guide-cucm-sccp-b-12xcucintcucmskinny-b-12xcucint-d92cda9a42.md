---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-integration-guide-cucm-sccp-b-12xcucintcucmskinny-b-12xcucint-d92cda9a42
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/cucm_sccp/b_12xcucintcucmskinny/b_12xcucintcucmskinny_chapter_00.html
retrieved_at: 2026-08-16T18:40:20.174916+00:00
---

Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 12.x

# Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 12.x

Updated: August 2, 2017

Chapter: Integration Overview

## Chapter: Integration Overview

# Integration Overview

## Integration Overview

## Introduction

The SCCP trunk integration is a method to establish
                           		communication between Unity Connection and Cisco Unified Communications Manager
                           		Express using SIP protocol. The Cisco Unified CM SCCP integration makes
                           		connections through a LAN or WAN. A gateway provides connections to the PSTN.

For a list of supported versions of Cisco Unified CM that are
                           		qualified to integrate with Cisco Unity Connection by SCCP, see the
                           		Compatibility Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

This document applies only when Unity Connection is installed on
                           		a separate server from Cisco Unified CM. This document does not apply to the
                           		configuration in which Unity Connection is installed as CiscoBusiness
                           		Edition—on the same server with Cisco Unified CM.

## Call Information

The phone system sends the following information with forwarded calls:

The extension of the called party

The extension of the calling party (for internal calls) or the phone number of the calling party (if it is an external call
                                 and the system uses caller ID)

The reason for the forward (the extension is busy, does not answer, or is set to forward all calls)

Unity Connection uses this information to answer the call appropriately. For example, a call forwarded to Unity Connection
                           is answered with the personal greeting of the user. If the phone system routes the call without this information, Unity Connection
                           answers with the opening greeting.

## Integration Functionality

The Cisco Unified CM SCCP integration with Unity Connection provides the following features:

Call forward to personal greeting

Call forward to busy greeting

Caller ID

Easy message access (a user can retrieve messages without entering an ID; Unity Connection identifies a user based on the
                                 extension from which the call originated; a password may be required)

Identified user messaging (Unity Connection automatically identifies a user who leaves a message during a forwarded internal
                                 call, based on the extension from which the call originated)

Message waiting indication (MWI)

## Integrations with
                        	 Multiple Phone Systems

Unity Connection can be integrated with two or more phone
                           		systems at one time. For information on the maximum supported combinations and
                           		instructions for integrating Unity Connection with multiple phone systems, see
                           		the Multiple Phone System Integration Guide for Cisco Unity
                              		  Connection, Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/multiple_integration/b_cuc12xintmultiple.html .

## Centralized Voice
                        	 Messaging

Cisco Unity Connection supports centralized voice messaging
                           		through the phone system, which supports various inter-phone system networking
                           		protocols including proprietary protocols, such as Avaya DCS, Nortel MCDN, or
                           		Siemens CorNet, and standards-based protocols, such as QSIG or DPNSS. Note that
                           		centralized voice messaging is a function of the phone system and its
                           		inter-phone system networking, not voicemail. Unity Connection supports
                           		centralized voice messaging as long as the phone system and its inter-phone
                           		system networking are properly configured. For details, see the “ Centralized Voice
                              		  Messaging ” section in the “Integrating Cisco Unity Connection with the
                           		Phone System” chapter of the Design Guide for Cisco Unity Connection, Release
                           		12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg.html .