---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-sip-update-html-1ed41c5ab7
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi_cube_sip_update.html
retrieved_at: 2026-08-16T15:48:25.686819+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Early Dialog UPDATE Block

## Chapter: Early Dialog UPDATE Block

# Early Dialog UPDATE Block

## Overview

This feature enables Cisco Unified Border Element (CUBE) to consume UPDATE requests with SDP, received during an early dialog. UPDATE requests are blocked at CUBE and are not passed through from one leg to the other leg.

If the UPDATE request contains changes in caller-ID, transcoder insertion or deletion, or video escalation or de-escalation,
                           then, CUBE can renegotiate the capabilities by sending a DO re-invite after the call is established.

UPDATE request with SDP received during an early dialog is consumed by CUBE and hence is not passed from one leg to the other leg. This feature can be configured only for the UPDATE requests with SDP.

To pass through the information in UPDATE requests containing changes in caller-ID, transcoder insertion or deletion, or
                           video escalation or de-escalation, CUBE can renegotiate the capabilities by sending a DO re-invite after the call is established. Thus both the user agents are synchronized
                           and this helps in effective utilization of resources.

Renegotiation can be configured only for the UPDATE requests containing the following changes:

Caller ID

Transcoder insertion or deletion

Video escalation or de-escalation

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

Early
                                             					 Dialog UPDATE Block

Cisco IOS
                                             					 XE 3.16S

This feature allows CUBE to consume the UPDATE requests with SDP received during an early dialog.

The
                                             					 following command is introduced: early-media update
                                                   						  block .

## Important
                        	 Characteristics of Early Dialog UPDATE Block

The following are a
                           		few important characteristics of Early Dialog UPDATE block:

If multiple codec's is offered by the user agent through an UPDATE, first codec common between received and configured in
                                 in-leg at dial-peer is sent in 200OK.

UPDATE request is consumed, if an UPDATE request with SDP is
                                 			 received after CUBE sends out 200 OK for an INVITE and before ACK is received.

A 200 Ok is sent for an UPDATE even if there is no transcoder available ONLY for DTMF (rtp-nte to inband). CUBE falls back to inband.

If Transcoder is
                                 			 unavailable, only the first codec received in the UPDATE request is sent in
                                 			 200OK.

CUBE sends 488 message if transcoder is required but unavailable for codec changes.

When a video escalation is received via UPDATE, CUBE sends 200 OK with video port as ZERO. No Video data plane sessions are created.

When a video de-escalation is received via UPDATE, CUBE sends 200 ok with video port as ZERO. Data plane sessions for video are made as INACTIVE instead of deleting. So, effectively
                                 there will be four 2 DP connections present with remote video port as ZERO.

Early-media
                                 			 UPDATE renegotiation takes precedence over DO-EO renegotiation.

If an early dialog UPDATE is received from one leg to change the caller-ID and the other leg supports UPDATE method, CUBE sends across the caller-id UPDATE to other side and there wont be any renegotiation.

If Re-Invite is received before triggering DO invite, then DO is not
                                 			 triggered.

If no update-callerid command is enabled and
                                 			 UPDATE request contains only caller-ID changes, then re-negotiation does not
                                 			 happen for any early dialog caller-ID changes. If UPDATE request contains
                                 			 transcoder changes or video escalation or de-escalation, re-negotiation happens
                                 			 even if no update-callerid command is enabled.

If mid-call signaling block is configured, DO invite is not
                                 			 triggered.

If 18x block is enabled, CUBE fails to add rel1xx related fields in the header. 100rel is dependent on 181 sdp block.

## Prerequisites

rel1xx require "100rel" command needs to be configured in global voice service voip sip configuration mode.

## Restrictions

Switch over to fax calls are not supported.

Session Description Protocol (SDP) passthrough is not supported.

Alternative Network Address Types (ANAT) is not supported.

## Configure Early Dialog UPDATE Block

Configuring early dialog UPDATE Block enables CUBE to block all early dialog UPDATE requests from passing through to the user agents.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of
                              			 the following commands to block early dialog UPDATE requests:

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
                                       			 the following commands to block early dialog UPDATE requests:

In the
                                             				  dial-peer configuration mode

In the
                                             				  global VoIP SIP configuration mode

### Example:

```
!Applying Early Dialog UPDATE block to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# Voice-class sip early-media update block Device (config-dial-peer)# end
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

## Configure Early Dialog UPDATE Block Renegotiate

Configuring Early Dialog UPDATE Block Renegotiate enables CUBE to renegotiate the call if UPDATE request with SDP contains changes caller-ID, transcoder insertion or deletion, or video
                              escalation or deletion. CUBE renegotiates by sending a DO re-invite after the call is established.

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

debug ccsip all

debug voip ccapi inout

show voip rtp connections

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| Early
                                             					 Dialog UPDATE Block | Cisco IOS
                                             					 XE 3.16S | This feature allows CUBE to consume the UPDATE requests with SDP received during an early dialog. The
                                             					 following command is introduced: early-media update
                                                   						  block . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                          				privileged EXEC mode. Enter
                                                					 your password if prompted. |
| Step 2 | configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Enter one of
                                       			 the following commands to block early dialog UPDATE requests: In the
                                             				  dial-peer configuration mode voice-class sip early-media
                                                					 update block In the
                                             				  global VoIP SIP configuration mode early media update block Example: In
                                       			 dial-peer configuration mode !Applying Early Dialog UPDATE block to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# Voice-class sip early-media update block Device (config-dial-peer)# end Example: In global
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
                                       			 the call if the UPDATE request contains changes in caller ID, transcoder
                                       			 addition or deletion, or video escalation or de-escalation. |
| Step 4 | end | Exits VoIP
                                          				SIP configuration mode and enters privileged EXEC mode. |