---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-dymc-payld-dtmf-html-8a853ae752
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-dymc-payld-dtmf.html
retrieved_at: 2026-08-16T15:50:54.610945+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Payload Type Interoperability

## Chapter: Payload Type Interoperability

# Payload Type Interoperability

## Overview

The Dynamic Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls feature provides dynamic payload type
                           interworking for dual tone multifrequency (DTMF) and codec packets for Session Initiation Protocol (SIP) to SIP calls.

Based on this feature, the Cisco Unified Border Element (CUBE) interworks between different dynamic payload type values across the call legs for the same codec. Also, CUBE supports any payload type value for audio, video, named signaling events (NSEs), and named telephone events (NTEs) in the
                           dynamic payload type range 96 to 127.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

Dynamic
                                             					 Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls

Baseline Functionality

The Dynamic
                                             					 Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls
                                             					 feature provides dynamic payload type interworking for DTMF and codec packets
                                             					 for SIP-to-SIP calls.

The
                                             					 following commands were introduced or modified: asymmetric payload and voice-class sip asymmetric payload .

## Restrictions

The Dynamic Payload
                           		Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls feature is
                           		not supported for the following:

Transcoded calls in releases prior to Cisco IOS XE Bengaluru 17.6.1a .

Secure Real-Time
                                 			 Protocol (SRTP) pass-through calls.

Flow-around
                                 			 calls.

Asymmetric
                                 			 payload types are not supported on early-offer (EO) call legs in a
                                 			 delayed-offer to early-offer (DO-EO) scenario.

Cisco fax relay.

Multiple m lines with
                                 			 the same dynamic payload types, where m is:

m = audio
                           		<media-port1> RTP/AVP XXX m = video <media-port2> RTP/AVP XXX

## Symmetric and Asymmetric Calls

CUBE supports dynamic payload type negotiation and interworking for all symmetric and asymmetric payload type combinations. A
                           call leg on CUBE is considered as symmetric or asymmetric based on the payload type value exchanged during the offer and answer with the endpoint:

A symmetric endpoint accepts and sends the same payload type.

An asymmetric endpoint can accept and send different payload types.

The Dynamic Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls feature is enabled by default for a
                           symmetric call. An offer is sent with a payload type based on the dial-peer configuration. The answer is sent with the same
                           payload type as was received in the incoming offer. When the payload type values negotiated during the signaling are different,
                           the CUBE changes the Real-Time Transport Protocol (RTP) payload value in the VoIP to RTP media path.

To support asymmetric call legs, you must enable The  Dynamic Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP
                           Calls feature. The dynamic payload type value is passed across the call legs, and the RTP payload type interworking is not
                           required. The RTP payload type handling is dependent on the endpoint receiving them.

## High Availability Checkpointing Support for Asymmetric Payload

## Configure Dynamic Payload Type Passthrough for DTMF and Codec Packets for SIP-to-SIP Calls

### Configure Dynamic Payload Type Passthrough at the Global Level

Perform this task
                                 		  to configure the pass through of DTMF or codec payload to the other call leg
                                 		  (instead of performing dynamic payload type interworking) feature at the global
                                 		  level.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- asymmetric payload { dtmf | dynamic-codecs | full | system }

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device# enable
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

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters voice
                                             				service configuration mode.

Step 4

sip

#### Example:

```
Device(conf-voi-serv)# sip
```

Enters voice
                                             				service SIP configuration mode.

Step 5

asymmetric payload { dtmf | dynamic-codecs | full | system }

#### Example:

```
Device(conf-serv-sip)# asymmetric payload full
```

Configures
                                             				global SIP asymmetric payload support.

The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs.

Step 6

end

#### Example:

```
Device(conf-serv-sip)# end
```

Exits voice
                                             				service SIP configuration mode and enters privileged EXEC mode.

### Configure Dynamic Payload Type Passthrough for a Dial Peer

Perform this task
                                 		  to configure the pass through of DTMF or codec payload to the other call leg
                                 		  (instead of performing dynamic payload type interworking) feature at the
                                 		  dial-peer level.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- voice-class sip asymmetric payload { dtmf | dynamic-codecs | full | system }

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

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer voice 77 voip
```

Enters dial
                                             				peer voice configuration mode.

Step 4

voice-class sip asymmetric payload { dtmf | dynamic-codecs | full | system }

#### Example:

```
Device(config-dial-peer)# voice-class sip asymmetric payload full
```

Configures the
                                             				dynamic SIP asymmetric payload support.

The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs.

Step 5

end

#### Example:

```
Device(config-dial-peer)# end
```

(Optional)
                                             				Exits dial peer voice configuration mode and enters privileged EXEC mode.

### Verify Dynamic Payload Interworking for DTMF and Codec Packets Support

This task shows how to display information to verify Dynamic Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP
                                 Calls configuration feature. These show commands need not be entered in any specific order.

### SUMMARY STEPS

- enable

- show call active voice compact

- show call active voice

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

show call active voice compact

#### Example:

```
Device# show call active voice compact
```

(Optional) Displays a compact version of call information.

Step 3

show call active voice

#### Example:

```
Device# show call active voice
```

(Optional) Displays call information for voice calls in progress.

### Tips to Troubleshoot

Use the following commands to debug errors while configuring the Dynamic Payload Type Interworking for DTMF and Codec Packets
                              for SIP-to-SIP Calls feature:

debug ccsip all

debug voip ccapi inout

debug voip rtp

Use the following debug commands to troubleshoot HA Checkpointing for Asymmetric Payload:

debug voip ccapi all

debug voice high-availability all

debug voip rtp error

debug voip rtp inout

debug voip rtp packet

debug voip rtp high-availability

debug voip rtp function

debug ccsip all

Use the following show commands to troubleshoot HA Checkpointing for Asymmetric Payload:

show redundancy state

show redundancy inter-device

show standby brief

show voice high-availability summary

show voip rtp stats

show voip rtp high-availability stats

show voip rtp connection detail

show call active voice brief

show call active voice [summary]

show call active video brief

show call active video [summary]

show align

show memory debug leak

## Configuration
                        	 Examples for Assymetric Payload Interworking

### Example:
                           	 Asymmetric Payload Interworking—Passthrough Configuration

```
!
voice service voip 
 allow-connections sip to sip
sip
  rel1xx disable
  asymmetric payload full
  midcall-signaling passthru
!
dial-peer voice 1 voip
 voice-class sip asymmetric payload full
 session protocol sipv2
 rtp payload-type cisco-codec-fax-ind 110
 rtp payload-type cisco-codec-video-h264 112
 session target ipv4:9.13.8.23
!
```

In the above example, it is assumed that 110 and 112 are not used for
                                 		  any other payload.

### Example:
                           	 Asymmetric Payload Interworking—Interworking Configuration

```
!
voice service voip 
 allow-connections sip to sip
!
dial-peer voice 1 voip
 session protocol sipv2
 rtp payload-type cisco-codec-fax-ind 110
 rtp payload-type cisco-codec-video-h264 112
 session target ipv4:9.13.8.23
!
```

In the above example, it is assumed that 110 and 112 are not used for
                                 		  any other payload.

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| Dynamic
                                             					 Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls | Baseline Functionality | The Dynamic
                                             					 Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls
                                             					 feature provides dynamic payload type interworking for DTMF and codec packets
                                             					 for SIP-to-SIP calls. The
                                             					 following commands were introduced or modified: asymmetric payload and voice-class sip asymmetric payload . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters voice
                                             				service configuration mode. |
| Step 4 | sip Example: Device(conf-voi-serv)# sip | Enters voice
                                             				service SIP configuration mode. |
| Step 5 | asymmetric payload { dtmf \| dynamic-codecs \| full \| system } Example: Device(conf-serv-sip)# asymmetric payload full | Configures
                                             				global SIP asymmetric payload support. Note The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs. | Note | The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs. |
| Note | The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs. |
| Step 6 | end Example: Device(conf-serv-sip)# end | Exits voice
                                             				service SIP configuration mode and enters privileged EXEC mode. |

| Note | The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 77 voip | Enters dial
                                             				peer voice configuration mode. |
| Step 4 | voice-class sip asymmetric payload { dtmf \| dynamic-codecs \| full \| system } Example: Device(config-dial-peer)# voice-class sip asymmetric payload full | Configures the
                                             				dynamic SIP asymmetric payload support. Note The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs. | Note | The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs. |
| Note | The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs. |
| Step 5 | end Example: Device(config-dial-peer)# end | (Optional)
                                             				Exits dial peer voice configuration mode and enters privileged EXEC mode. |

| Note | The dtmf and dynamic-codecs keywords are internally mapped to the full keyword to
                                                         				  provide asymmetric payload type support for audio and video codecs, DTMF, and
                                                         				  NSEs. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | show call active voice compact Example: Device# show call active voice compact | (Optional) Displays a compact version of call information. |
| Step 3 | show call active voice Example: Device# show call active voice | (Optional) Displays call information for voice calls in progress. |