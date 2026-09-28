---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-midcall-reinvite-html-6fefa1a0b7
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-midcall-reinvite.html
retrieved_at: 2026-08-16T15:48:21.742844+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Mid-call Signaling

## Chapter: Mid-call Signaling

# Mid-call Signaling

## Overview

The Cisco Unified Border Element (CUBE) Mid-call Signaling support aims to reduce the interoperability issues that arise due to consuming mid-call RE-INVITES/UPDATES.

Mid-call
                           		Re-INVITEs/UPDATEs can be consumed in the following ways:

Mid-call
                                 			 Signaling Passthrough - Media Change

Mid-call
                                 			 Signaling Block

Mid-call
                                 			 Signaling Codec Preservation

H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

Mid-call
                                          				  Re-INVITE Consumption

Cisco IOS XE
                                          				  3.6S

The Mid-call
                                          				  Re-INVITE consumption feature consumes mid-call Re-INVITEs from CUBE and helps
                                          				  to avoid interoperability issues because of these re-invites

The following
                                          				  commands were introduced or modified: midcall-signaling .

Mid-call
                                          				  Codec Preservation

Cisco IOS XE
                                          				  3.9S

The Mid-call
                                          				  Codec Preservation feature helps to disables codec negotiation in the middle of
                                          				  a call and preserves the codec negotiated before the call.

The
                                          				  following commands were introduced or modified: midcall-signaling preserve-codec , voice-class sip midcall-signaling preserve-codec .

Mid-call
                                          				  Re-INVITE Consumption Enhancements

Cisco IOS XE
                                          				  3.16S

Mid-call signaling Re-INVITE consumption is enhanced to support:

Re-INVITE based call transfer

Call transfer with REFER Consume

Normalization of call hold in a call set-up

## Prerequisites

Enable CUBE application on a device

## Mid-call Signaling
                        	 Passthrough - Media Change

Passthrough media
                           		change method optimizes or consumes mid-call, media-related signaling within
                           		the call. Mid-call signaling changes will be passed through only when
                           		bidirectional media like T.38 or video is added. The command midcall-signaling passthru media-change needs to be configured to enable
                           		passthrough media change.

### Restrictions

Session Description Protocol (SDP) -passthrough is not supported.

When codec T is configured, the offer from CUBE has only
                                    			 audio codecs, and so the video codecs are not consumed.

Re-invites are not
                                    			 consumed if media flow-around is configured.

Re-invites are not
                                    			 consumed if media anti-tromboning is configured.

De-escalation
                                    			 re-invites are consumed. So, one call leg might be de-escalated to audio only
                                    			 while the other call leg continues to support audio and video.

Re-invites with
                                    			 media direction changes are consumed.

Video transcoding
                                    			 is not supported.

Multicast Music
                                    			 On Hold (MMOH) is not supported.

When the midcall-signaling passthru media-change command is configured transcoder is enabled, there might be some impact on Digital Signal Processing (DSP) resources as the
                                    transcoder might be used for all the calls.

Session timer is handled leg by leg whenever this feature is configured and it includes session timer negotiation for initial
                                    INVITE/200 OK transaction as well.

More than two
                                    			 m-lines in the SDP is not supported.

Alternative
                                    			 Network Address Types (ANAT) is not supported.

Video calls and
                                    			 Application streams are not supported when mid-call signaling block is
                                    			 configured.

In the SRTP-RTP scenario, re-invites are not consumed.

### Behavior of
                           	 Mid-call Re-INVITE Consumption

If mid-call signaling block is enabled on either of call-legs, video parameters and application streams are not negotiated,
                                    and are rejected in the answer.

When flow around and offer-all is configured, CUBE performs codec renegotiation even if mid-call signaling block is configured
                                    globally.

The following behavior is for refer consume scenario:

REFER consume is supported for blind, alert and consult call transfers.

Existing codecs or DTMF is used for local bridging of new call legs. No Re-INVITE or UPDATE is sent for media re-negotiation
                                          after REFER.

Call gets dropped when DSP is required but not available.

A call can be escalated to video only if transferee and transfer-to dial-peers do not have mid-call signaling block configured.

Video calls are de-escalated if mid-call signaling block configuration on transfer-to dial-peer.

For Re-INVITE based call-transfer involving Cisco Unified Communications Manager, all Re-INVITE are locally answered and transcoder
                                          is invoked if negotiated codecs are different than the codecs before call-transfer.

The following behavior is for INVITE with REPLACES Header consume scenario:

CUBE consumes INVITE with REPLACES Header only when the handle-replaces CLI is configured (under sip-ua or voice-class tenant ). In this case, CUBE consumes the INVITE and handles it locally. It triggers an outbound INVITE without replaces header and
                                          call gets connected with agent.

If the handle-replaces CLI is enabled, the 'transfer-to' party must have the same codec that is used for the original call setup. If there is a
                                          different codec offer, CUBE rejects the INVITE with 488 error.

If the handle-replaces CLI is not configured, CUBE does not consume the INVITE with REPLACES Header and the outgoing INVITE holds same replace header
                                          which CUBE is received.

INVITE with REPLACES Header consumption does not support the following configurations:

Delayed Offer INVITE

Codec, DTMF attribute changes, and RSVP

Mid-call Signaling block

IPv6

The following table provides the details of the behavior when the initial call is establish without 'sendrecv' parameter,
                                    that means, the initial call is established with 'sendonly', 'recvonly' or 'inactive'.

Scenario

Behavior

If an Offer is received with 'sendonly' and mid-call block is configured on any or both call legs

Offer is sent with 'sendrecv'.

If an Answer is received with 'sendonly' and the peer leg supports mid-call signaling

Answer is sent with 'sendonly'. Resume transaction is end-to-end.

If an Answer is received with 'sendonly' and the peer leg does not supports mid-call signaling

Answer is sent with 'sendrecv'. Resume transaction is consumed.

If Offer as well as Answer is received with 'sendonly' and Offering leg does not support mid-call signaling

Answer is sent with 'recvonly'. Resume from Offering leg is end-to-end. Resume from answering leg is consumed.

If Offer as well as Answer is received with 'sendonly' and Answering leg does not support mid-call signaling

Answer is sent with 'inactive'. Resume from Offering leg is consumed. Resume from answering leg is end-to-end.

If Offer as well as Answer is received with 'sendonly' and both legs do not support mid-call signaling

Answer is sent with ' recvonly'. Resume transaction is consumed.

### Configure Passthrough of Mid-call Signalling

Perform this task
                                 		  to configure passthrough of mid-call signaling (as Re-invites) only when
                                 		  bidirectional media is added.

### SUMMARY STEPS

- enable

- configure terminal

- Configure
                                 			 passthrough of mid-call signaling changes only when bidirectional media is
                                 			 added.

In Global VoIP SIP configuration mode

In dial-peer configuration mode

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

Configure
                                          			 passthrough of mid-call signaling changes only when bidirectional media is
                                          			 added.

In Global VoIP SIP configuration mode

In dial-peer configuration mode

#### Example:

```
Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# midcall-signaling passthru media-change
```

#### Example:

```
Device(config)# dial-peer voice 2 voip
Device(config-dial-peer)# voice-class sip midcall-signaling passthru media-change
```

Step 4

end

Exits to
                                             				privileged EXEC mode.

### Example Configuring Passthrough SIP Messages at Dial Peer Level

The following example shows how to passthrough SIP messages at the dial peer Level:

```
dial-peer voice 600 voip
 destination-pattern 2222222222
 session protocol sipv2
 session target ipv4:9.45.38.39:9001
voice-class sip midcall-signaling passthru media-change
 incoming called-number 1111111111
voice-class codec  2 offer-all
dial-peer voice 400 voip
 destination-pattern 1111111111
 session protocol sipv2
 session target ipv4:9.45.38.39:9000
 incoming called-number 2222222222
voice-class codec 1 offer-all
```

### Example Configuring Passthrough SIP Messages at the Global Level

The following example shows how to passthrough SIP messages at the global level:

```
Device(config)# voice service voip Device(conf-voi-serv)# no ip address trusted authenticate Device(conf-voi-serv)# allow-connections sip to sip Device(conf-voi-serv)# sip Device(conf-serv-sip)# midcall-signaling passthru media-change
```

## Mid-call Signaling
                        	 Block

The Block method
                           		blocks all mid-call media-related signaling to the specific SIP trunk. The
                           		command midcall-signaling block needs to be configured to enable this
                           		behavior. Video escalation and T.38 call flow are rejected when the midcall-signaling block command is configured. This command should
                           		be configured only when basic call is the focus and mid-call can be consumed.

### Restrictions

Session
                                    			 Description Protocol (SDP) -passthrough is not supported

Video calls and
                                    			 Application streams are not supported.

When media flow-around is configured, Mid-call INVITE is rejected with 488 error message.

Re-invites are
                                    			 not consumed if media anti-tromboning is configured.

Multicast Music On Hold (MMOH) is not supported.

When the midcall-signaling passthru media-change command is configured transcoder is enabled, there might be some impact on Digital Signal Processing (DSP) resources as the
                                    transcoder might be used for all the calls.

Session timer is handled leg by leg whenever this feature is configured.

More than two m-lines in the SDP is not supported.

Alternative
                                    			 Network Address Types (ANAT) is not supported.

When mid-call signaling block is configured, you can either configure REFER consume or enable TCL script. Mid-call signaling
                                    block is not supported if both REFER consume and TCL script are enabled. We also recommend not to configure supplementary-service media-renegotiate command.

In the SRTP-RTP scenario, re-invites are not consumed.

### Blocking Mid-Call
                           	 Signaling

Perform this task
                                 		  to block mid-call signaling:

### SUMMARY STEPS

- enable

- configure terminal

- Configure
                                 			 blocking of mid-call signaling changes:

In Global
                                       				  VoIP SIP configuration mode

In dial-peer configuration mode

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

Configure
                                          			 blocking of mid-call signaling changes:

In Global
                                                				  VoIP SIP configuration mode

In dial-peer configuration mode

#### Example:

```
Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# midcall-signaling block
```

#### Example:

```
Device(config)# dial-peer voice 2 voip
Device(config-dial-peer)# voice-class sip midcall-signaling block
```

Step 4

end

Exits to
                                             				privileged EXEC mode.

### Example Blocking SIP Messages at Dial Peer Level

```
dial-peer voice 107 voip
 destination-pattern 74000
 session protocol sipv2
 session target ipv4:9.45.36.9
 incoming called-number 84000
 voice-class codec 1 offer-all
!
dial-peer voice 110 voip
 destination-pattern 84000
 session protocol sipv2
 session target ipv4:9.45.35.2
 incoming called-number 74000
 voice-class codec 1 offer-all
 voice-class sip midcall-signaling block
!
```

### Example: Blocking SIP Messages at the Global Level

The following example shows how to block SIP messages at the global Level

```
Device(config)#voice service voip
Device(config-voi-serv)#no ip address trusted authenticate
Device(config-voi-serv)#allow-connections sip to sip
Device(config-voi-serv)#sip
Device(config-serv-sip)#midcall-signaling block
```

## Mid Call Codec
                        	 Preservation

Mid call codec
                           		preservation defines whether a codec can be negotiated after a call has been
                           		initiated. You can enable or disable codec negotiation in the middle of a call.

### Configure Mid Call Codec Preservation

This tasks
                                 		  disables codec negotiation in the middle of a call and preserves the codec
                                 		  negotiated before the call.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of
                                 			 the following to disable midcall codec renegotiation:

In Global VoIP SIP configuration mode

In dial-peer configuration mode

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode.

Enter
                                                   					 your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

Enter one of
                                          			 the following to disable midcall codec renegotiation:

In Global VoIP SIP configuration mode

In dial-peer configuration mode

#### Example:

```
Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# midcall-signaling preserve-codec
```

#### Example:

```
Device(config)# dial-peer voice 10 voip
Device(conf-dial-peer)# voice-class sip midcall-signaling preserve-codec
```

Step 4

end

#### Example:

```
Device(conf-serv-sip)# end
```

Exits to
                                             				privileged EXEC mode.

### Example: Configuring Mid Call Codec Preservation at the Dial Peer
                           	 Level

```
dial-peer voice 107 voip
 destination-pattern 74000
 session protocol sipv2
 session target ipv4:9.45.36.9
 incoming called-number 84000
 voice-class codec 1 offer-all
!
dial-peer voice 110 voip
 destination-pattern 84000
 session protocol sipv2
 session target ipv4:9.45.35.2
 incoming called-number 74000
 voice-class codec 1 offer-all
 voice-class sip midcall-signaling preserve-codec
!
```

### Example: Configuring Mid Call Codec Preservation at the Global
                           	 Level

```
Device(config)# voice service voip Device(conf-voi-serv)# no ip address trusted authenticate Device(conf-voi-serv)# allow-connections sip to sip Device(conf-voi-serv)# sip Device(conf-serv-sip)# midcall-signaling preserve-codec
```

| Note | This feature should be used as a last resort only when there is no other option in CUBE . This is because configuring this feature can break video-related features. For Delay-offer Re-INVITE, the configured codec
                                    will be passed as an offer in 200 message to change the codec, the transcoder is added in the answer. |
|---|---|

| Note | H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications. |
|---|---|

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| Mid-call
                                          				  Re-INVITE Consumption | Cisco IOS XE
                                          				  3.6S | The Mid-call
                                          				  Re-INVITE consumption feature consumes mid-call Re-INVITEs from CUBE and helps
                                          				  to avoid interoperability issues because of these re-invites The following
                                          				  commands were introduced or modified: midcall-signaling . |
| Mid-call
                                          				  Codec Preservation | Cisco IOS XE
                                          				  3.9S | The Mid-call
                                          				  Codec Preservation feature helps to disables codec negotiation in the middle of
                                          				  a call and preserves the codec negotiated before the call. The
                                          				  following commands were introduced or modified: midcall-signaling preserve-codec , voice-class sip midcall-signaling preserve-codec . |
| Mid-call
                                          				  Re-INVITE Consumption Enhancements | Cisco IOS XE
                                          				  3.16S | Mid-call signaling Re-INVITE consumption is enhanced to support: Re-INVITE based call transfer Call transfer with REFER Consume Normalization of call hold in a call set-up |

| Scenario | Behavior |
|---|---|
| If an Offer is received with 'sendonly' and mid-call block is configured on any or both call legs | Offer is sent with 'sendrecv'. |
| If an Answer is received with 'sendonly' and the peer leg supports mid-call signaling | Answer is sent with 'sendonly'. Resume transaction is end-to-end. |
| If an Answer is received with 'sendonly' and the peer leg does not supports mid-call signaling | Answer is sent with 'sendrecv'. Resume transaction is consumed. |
| If Offer as well as Answer is received with 'sendonly' and Offering leg does not support mid-call signaling | Answer is sent with 'recvonly'. Resume from Offering leg is end-to-end. Resume from answering leg is consumed. |
| If Offer as well as Answer is received with 'sendonly' and Answering leg does not support mid-call signaling | Answer is sent with 'inactive'. Resume from Offering leg is consumed. Resume from answering leg is end-to-end. |
| If Offer as well as Answer is received with 'sendonly' and both legs do not support mid-call signaling | Answer is sent with ' recvonly'. Resume transaction is consumed. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Configure
                                          			 passthrough of mid-call signaling changes only when bidirectional media is
                                          			 added. In Global VoIP SIP configuration mode midcall-signaling passthru media-change In dial-peer configuration mode voice-class sip midcall-signaling passthru media-change Example: In Global
                                          			 VoIP SIP configuration mode: Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# midcall-signaling passthru media-change Example: In Dial-peer configuration mode: Device(config)# dial-peer voice 2 voip
Device(config-dial-peer)# voice-class sip midcall-signaling passthru media-change | Re-Invites are passed through only when bidirectional media is
                                          			 added. |
| Step 4 | end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Configure
                                          			 blocking of mid-call signaling changes: In Global
                                                				  VoIP SIP configuration mode midcall-signaling block In dial-peer configuration mode voice-class sip midcall-signaling block Example: In Global
                                          			 VoIP SIP configuration mode: Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# midcall-signaling block Example: In Dial-peer configuration mode: Device(config)# dial-peer voice 2 voip
Device(config-dial-peer)# voice-class sip midcall-signaling block | Mid-call
                                          			 signaling is always blocked. |
| Step 4 | end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Enter one of
                                          			 the following to disable midcall codec renegotiation: In Global VoIP SIP configuration mode midcall-signaling preserve-codec In dial-peer configuration mode voice-class sip midcall-signaling preserve-codec Example: Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# midcall-signaling preserve-codec Example: Device(config)# dial-peer voice 10 voip
Device(conf-dial-peer)# voice-class sip midcall-signaling preserve-codec | Disables codec negotiation in the middle of a call and preserves
                                          			 the codec negotiated before the call. |
| Step 4 | end Example: Device(conf-serv-sip)# end | Exits to
                                             				privileged EXEC mode. |