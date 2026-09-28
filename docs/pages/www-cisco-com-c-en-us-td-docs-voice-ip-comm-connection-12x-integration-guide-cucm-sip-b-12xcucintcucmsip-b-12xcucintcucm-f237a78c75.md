---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-integration-guide-cucm-sip-b-12xcucintcucmsip-b-12xcucintcucm-f237a78c75
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/cucm_sip/b_12xcucintcucmsip/b_12xcucintcucmsip_chapter_00.html
retrieved_at: 2026-08-16T18:40:57.530535+00:00
---

Cisco Unified Communications Manager SIP Integration Guide for Cisco Unity Connection Release 12.x

# Cisco Unified Communications Manager SIP Integration Guide for Cisco Unity Connection Release 12.x

Updated: April 4, 2024

Chapter: Integration
	 Description

## Chapter: Integration
	 Description

# Integration
                     	 Description

Integration Description

## Introduction

The SIP trunk
                           		integration is a method to establish communication between Unity Connection and
                           		Cisco Unified CM using SIP protocol.

For a list of
                           		supported versions of Cisco Unified CM that are qualified to integrate with
                           		Cisco Unity Connection through a SIP trunk, see the Compatibility
                              		  Matrix for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html .

## Integration Functionality

The Cisco Unified CM SIP trunk integration with Cisco Unity Connection provides the following features:

Call forward to personal greeting

Call forward to busy greeting

Caller ID

Easy message access (a user can retrieve messages without entering an ID; Cisco Unity Connection identifies a user based on
                                 the extension from which the call originated; a password may be required)

Identified user messaging (Cisco Unity Connection automatically identifies a user who leaves a message during a forwarded
                                 internal call, based on the extension from which the call originated)

Message waiting indication (MWI)

## Integrations with
                        	 Multiple Phone Systems

Unity Connection can be integrated with two or more phone
                           		systems at one time. For information on the maximum supported combinations and
                           		instructions for integrating Unity Connection with multiple phone systems, see
                           		the Multiple Phone System Integration Guide for Cisco Unity
                              		  Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/multiple_integration/b_cuc12xintmultiple.html .

## Centralized Voice
                        	 Messaging

Unity Connection supports centralized voice messaging through
                           		the phone system, which supports various inter-phone system networking
                           		protocols including proprietary protocols, such as Avaya DCS, Nortel MCDN, or
                           		Siemens CorNet, and standards-based protocols, such as QSIG or DPNSS. Note that
                           		centralized voice messaging is a function of the phone system and its
                           		inter-phone system networking, not voicemail. Unity Connection supports
                           		centralized voice messaging as long as the phone system and its inter-phone
                           		system networking are properly configured. For details, see the “ Centralized Voice
                              		  Messaging ” section in the “Integrating Cisco Unity Connection with the
                           		Phone System” chapter of the Design Guide for Cisco Unity Connection, Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg.html .