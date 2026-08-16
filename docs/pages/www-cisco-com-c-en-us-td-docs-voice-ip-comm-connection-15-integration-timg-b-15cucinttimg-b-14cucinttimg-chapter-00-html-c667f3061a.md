---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-integration-timg-b-15cucinttimg-b-14cucinttimg-chapter-00-html-c667f3061a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/timg/b_15cucinttimg/b_14cucinttimg_chapter_00.html
retrieved_at: 2026-08-16T18:47:21.626399+00:00
---

TIMG Integration Guide for Cisco Unity Connection Release 15

# TIMG Integration Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Integration Description

## Chapter: Integration Description

# Integration Description

## Integration Description

### Introduction

Cisco Unity Connection supports integrations through TIMG units
                              		(media gateways) with supported phone systems that provide in-band call
                              		information and MWI requests through the T1 digital lines.

Unity Connection supports integrations through TIMG units (media
                              		gateways) with the following phone systems:

Any phone system that provides call information and MWI requests
                                    			 through a serial data link (SMDI, MCI, or MD-110 protocol) to the master TIMG
                                    			 unit. For details, see the " Serial Integration with TIMG Units " section.

A supported phone system that provides in-band call information
                                    			 and MWI requests—through the T1 digital lines. For details, see the " In-Band Integration with TIMG Units "
                                    			 section.

#### Serial Integration
                              	 with TIMG Units

The phone system sends call information and MWI requests through
                                 		the data link, which is an RS-232 serial cable that connects the phone system
                                 		and the master TIMG unit. Voice connections are sent through the T1 digital
                                 		lines between the phone system and the TIMG units. The TIMG units communicate
                                 		with the Unity\\ Connection server through the LAN or WAN using Session
                                 		Initialization Protocol (SIP). Figure 1-1 shows the required connections
                                 		for a serial integration using TIMG units.

#### In-Band
                              	 Integration with TIMG Units

The phone system sends call information, MWI requests, and voice
                                 		connections through the T1 digital lines, which connect the phone system and
                                 		the TIMG units. The TIMG units communicate with the Unity Connection server
                                 		through the LAN or WAN using Session Initialization Protocol (SIP). Figure
                                    		  1-2 shows the required connections for an in-band integration using TIMG
                                 		units.

Call Information

The phone system sends the following information with forwarded
                                 		calls:

The extension of the called party

The extension of the calling party (for internal calls) or the
                                       			 phone number of the calling party (if it is an external call and the system
                                       			 uses caller ID)

The reason for the forward (the extension is busy, does not
                                       			 answer, or is set to forward all calls)

Unity\\ Connection uses this information to answer the call
                                 		appropriately. For example, a call forwarded to Unity\\ Connection is answered
                                 		with the personal greeting of the user. If the phone system routes the call
                                 		without this information, Unity\\ Connection answers with the opening greeting.

Serial integrations send requests to turn on and turn off MWIs
                                             		  through the data link.

Integration Functionality

The TIMG integration provides the following integration
                                 		features:

Call forward to personal greeting

Call forward to busy greeting

Caller ID

Easy message access (a user can retrieve messages without
                                       			 entering an ID because Unity\\ Connection identifies the user based on the
                                       			 extension from which the call originated; a password may be required)

Identified user messaging (Unity\\ Connection identifies the
                                       			 user who leaves a message during a forwarded internal call, based on the
                                       			 extension from which the call originated)

Message waiting indication (MWI)

Integrations with Multiple Phone Systems

Unity\\ Connection can be integrated with two or more phone systems at one time. For information on the maximum supported
                                 combinations and instructions for integrating Unity\\ Connection with multiple phone systems, see the Multiple Phone System Integration Guide for Cisco Unity Connection Release 15, available at

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/multiple/b_cuc15intmultiple.html .

### Call Information

The phone system sends the following information
                              		with forwarded calls:

- The extension of the called
                                 		  party

- The extension of the calling
                                 		  party (for internal calls) or the phone number of the calling party (if it is
                                 		  an external call and the system uses caller ID)

- The reason for the forward
                                 		  (the extension is busy, does not answer, or is set to forward all calls)

Unity Connection uses this information to answer
                              		the call appropriately. For example, a call forwarded to Unity Connection is
                              		answered with the personal greeting of the user. If the phone system routes the
                              		call without this information, Unity Connection answers with the opening
                              		greeting.

### Integration Functionality

The TIMG integration provides the following
                              		integration features:

- Call forward to personal
                                 		  greeting

- Call forward to busy
                                 		  greeting

- Caller ID

- Easy message access (a user
                                 		  can retrieve messages without entering an ID because Unity Connection
                                 		  identifies the user based on the extension from which the call originated; a
                                 		  password may be required)

- Identified user messaging
                                 		  (Unity Connection identifies the user who leaves a message during a forwarded
                                 		  internal call, based on the extension from which the call originated)

- Message waiting indication
                                 		  (MWI)

### Integrations with
                           	 Multiple Phone Systems

Unity Connection can be integrated with two or more phone systems at one time. For information on the maximum supported combinations
                              and instructions for integrating Unity Connection with multiple phone systems, see the Multiple Phone System Integration Guide for Cisco Unity Connection Release 15 , available at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html .

| Note | Serial integrations send requests to turn on and turn off MWIs
                                             		  through the data link. |
|---|---|

| Note | Serial integrations send requests to turn on and turn off MWIs
                                       		through the data link. |
|---|---|