---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-integration-cucm-sip-b-14cucintcucmsip-b-14cucintcucmsip-chapt-529d6968e4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/cucm_sip/b_14cucintcucmsip/b_14cucintcucmsip_chapter_00.html
retrieved_at: 2026-08-17T03:37:50.153808+00:00
---

Cisco Unified Communications Manager SIP Integration Guide for Cisco Unity Connection Release 14

# Cisco Unified Communications Manager SIP Integration Guide for Cisco Unity Connection Release 14

Updated: November 25, 2020

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

Unity Connection can be integrated with two or more phone systems at one time. For information on the maximum supported combinations
                           and instructions for integrating Unity Connection with multiple phone systems, see the Multiple Phone System Integration Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/multiple/b_cuc14intmultiple.html .

## Centralized Voice
                        	 Messaging

Unity Connection supports centralized voice messaging through the phone system, which supports various inter-phone system
                           networking protocols including proprietary protocols, such as Avaya DCS, Nortel MCDN, or Siemens CorNet, and standards-based
                           protocols, such as QSIG or DPNSS. Note that centralized voice messaging is a function of the phone system and its inter-phone
                           system networking, not voicemail. Unity Connection supports centralized voice messaging as long as the phone system and its
                           inter-phone system networking are properly configured. For details, see the “ Centralized Voice Messaging ” section in the “Integrating Cisco Unity Connection with the Phone System” chapter of the Design Guide for Cisco Unity Connection, Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/design/guide/b_14cucdg.html .