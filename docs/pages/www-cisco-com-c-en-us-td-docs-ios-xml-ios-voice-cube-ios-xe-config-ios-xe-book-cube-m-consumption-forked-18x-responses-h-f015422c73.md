---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-cube-m-consumption-forked-18x-responses-h-f015422c73
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/cube_m_consumption-forked-18x-responses.html
retrieved_at: 2026-08-16T15:48:29.845637+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Forked 18x Responses

## Chapter: Forked 18x Responses

# Forked 18x Responses

## Overview

The Cisco Unified Border Element (CUBE) supports consumption of forked 18x responses with SDP, under certain conditions during an early dialog, to reduce the interoperability
                           issues that arise due to signaling forking.

When CUBE receives forked 18x responses with SDP, the media negotiation by default is end-to-end. This means that CUBE has to send an UPDATE with SDP on the inbound leg to renegotiate the new media offer. Under certain conditions, the inbound
                           leg may not be able to support sending UPDATE messages with SDP for media renegotiation. This results in CUBE consuming the forked 18x responses with SDP and may result in DSP resources being used for media interworking. Media parameters
                           such as direction change, and call escalation or de-escalation is not propagated end-to-end. If required, these media changes
                           can be renegotiated end-to-end, after the calls are connected, using a DO re-INVITE.

Forked 18x responses for INVITE requests with SDP during early dialog will be consumed by CUBE to reduce interoperability issues between user agents.

### Feature
                           	 Information for Consumption of Multiple Forked 18x Responses with SDP During
                           	 Early Dialog

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

Support
                                             					 for Forked 18x Responses with SDP during Early Dialog

Cisco IOS
                                             					 XE Denali 16.3.1

This feature allows CUBE to consume multiple forked 18x responses with SDP received during an early dialog.

### Characteristics of
                           	 Forked 18x Responses with SDP during Early Dialog

If PRACK or UPDATE is not supported on the inbound leg, by default, CUBE consumes the forked 18x responses

If PRACK or UPDATE is not supported and CUBE has to initiate renegotiation after call connect, then the early media update block re-negotiate CLI must be enabled

When PRACK and UPDATE are supported on the inbound leg and CUBE has to consume the forked 18x responses, the early media update block CLI must be enabled

If PRACK and UPDATE are supported and CUBE has to consume the forked 18x responses and initiate renegotiation after call connect, then the early media update block renegotiate CLI must be enabled

If mid-call
                                    			 signaling block or mid-call signaling passthrough media changes are configured,
                                    			 DO invite is not triggered

CUBE utilizes the EARLY UPDATE BLOCK functionality to configure the forked 18x responses with SDP during early dialog. The early media update block command is used to consume the forked 18x responses and the early media update block renegotiate command is used to renegotiate the forked 18x responses after the call connect.

Renegotiation (when
                              		enabled via configuration) is triggered for the forked 18x responses containing
                              		the following changes:

DSP Transcoder
                                    			 insertion

Video escalation
                                    			 or de-escalation

Media
                                    			 directional changes

It is recommended
                                          		  to configure the early media update block
                                                				re-negotiate command whenever there are transcoding, DTMF
                                          		  interworking, or video changes.

## Prerequisites

Re-negotiation
                                 			 is triggered only if the renegotiate early media update block
                                       				  re-negotiate CLI is enabled

## Restrictions

The following
                           		features or call-flows are not supported:

SIP
                                 			 Delayed-Offer to Delayed-Offer call flows

Session
                                 			 Description Protocol (SDP) passthrough mode

Secure Real-Time
                                 			 Transport Protocol (SRTP) passthrough calls

Alternative
                                 			 Network Address Types (ANAT)

Media
                                 			 flow-around

Media
                                 			 anti-trombone

Early-dialog
                                 			 UPDATE block

## Configure Consumption of Forked 18x Responses with SDP During Early Dialog

Perform the following procedure to enable CUBE to block all early dialog forked 18x requests from passing through to the user agents.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of
                              			 the following commands to block the forked 18x responses with SDP during early
                              			 dialog:

In the
                                    				  dial-peer configuration mode

In the
                                    				  global VoIP SIP configuration mode

- end

### DETAILED STEPS

Step 1

enable

Enables
                                          				privileged EXEC mode.

Enter
                                                					 your password if prompted.

Step 2

configure terminal

Enters global
                                          				configuration mode.

Step 3

Enter one of
                                       			 the following commands to block the forked 18x responses with SDP during early
                                       			 dialog:

In the
                                             				  dial-peer configuration mode

In the
                                             				  global VoIP SIP configuration mode

### Example:

```
!Applying Early Dialog UPDATE block to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip early-media update block Device (config-dial-peer)# end
```

### Example:

```
! Applying Early Dialog UPDATE block globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# early media update block Device (config-voi-sip)# end
```

Step 4

end

Exits VoIP
                                          				SIP configuration mode and enters privileged EXEC mode.

## Configure Consumption of Forked 18x Responses with SDP During Early Dialog Renegotiate

Perform the
                              		  following procedure to enable CUBE to renegotiate forked 18x calls with SDP
                              		  during early dialog after consumption of these forked 18x responses. CUBE
                              		  renegotiates by sending a DO invite after the call is established.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of
                              			 the following commands:

In the
                                    				  dial-peer configuration mode

In the
                                    				  global VoIP configuration mode

- end

### DETAILED STEPS

Step 1

enable

Enables
                                          				privileged EXEC mode.

Enter
                                                					 your password if prompted.

Step 2

configure terminal

Enters global
                                          				configuration mode.

Step 3

Enter one of
                                       			 the following commands:

In the
                                             				  dial-peer configuration mode

In the
                                             				  global VoIP configuration mode

### Example:

```
!Applying Early Dialog UPDATE block re-negotiate to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip early-media update block re-negotiate Device (config-dial-peer)# end
```

### Example:

```
! Applying Early Dialog UPDATE block re-negotiate globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# early media update block re-negotiate Device (config-voi-sip)# end
```

Step 4

end

Exits VoIP
                                          				SIP configuration mode and enters privileged EXEC mode.

## Tips to Troubleshoot

Use the following
                           		command for debugging information:

debug ccsip
                                 			 verbose

show voip rtp
                                 			 connections detail

show call
                                 			 active voice brief

show dspfarm
                                 			 dsp active

show voice dsmp
                                 			 stream brief

show platform
                                 			 hardware qfp active feature sbc global

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| Support
                                             					 for Forked 18x Responses with SDP during Early Dialog | Cisco IOS
                                             					 XE Denali 16.3.1 | This feature allows CUBE to consume multiple forked 18x responses with SDP received during an early dialog. |

| Note | CUBE utilizes the EARLY UPDATE BLOCK functionality to configure the forked 18x responses with SDP during early dialog. The early media update block command is used to consume the forked 18x responses and the early media update block renegotiate command is used to renegotiate the forked 18x responses after the call connect. |
|---|---|

| Note | It is recommended
                                          		  to configure the early media update block
                                                				re-negotiate command whenever there are transcoding, DTMF
                                          		  interworking, or video changes. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                          				privileged EXEC mode. Enter
                                                					 your password if prompted. |
| Step 2 | configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Enter one of
                                       			 the following commands to block the forked 18x responses with SDP during early
                                       			 dialog: In the
                                             				  dial-peer configuration mode voice-class sip early-media
                                                					 update block In the
                                             				  global VoIP SIP configuration mode early media update block Example: In
                                       			 dial-peer configuration mode !Applying Early Dialog UPDATE block to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip early-media update block Device (config-dial-peer)# end Example: In global
                                       			 VoIP SIP configuration mode ! Applying Early Dialog UPDATE block globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# early media update block Device (config-voi-sip)# end |  |
| Step 4 | end | Exits VoIP
                                          				SIP configuration mode and enters privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                          				privileged EXEC mode. Enter
                                                					 your password if prompted. |
| Step 2 | configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Enter one of
                                       			 the following commands: In the
                                             				  dial-peer configuration mode voice-class sip early-media
                                                					 update block re-negotiate In the
                                             				  global VoIP configuration mode early media update block
                                                					 re-negotiate Example: In
                                       			 dial-peer configuration mode !Applying Early Dialog UPDATE block re-negotiate to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip early-media update block re-negotiate Device (config-dial-peer)# end Example: In global
                                       			 VoIP SIP configuration mode ! Applying Early Dialog UPDATE block re-negotiate globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# early media update block re-negotiate Device (config-voi-sip)# end | Renegotiates
                                       			 the call if the forked 18x responses with SDP during early dialog contains
                                       			 changes in transcoder addition, or video escalation or de-escalation. |
| Step 4 | end | Exits VoIP
                                          				SIP configuration mode and enters privileged EXEC mode. |