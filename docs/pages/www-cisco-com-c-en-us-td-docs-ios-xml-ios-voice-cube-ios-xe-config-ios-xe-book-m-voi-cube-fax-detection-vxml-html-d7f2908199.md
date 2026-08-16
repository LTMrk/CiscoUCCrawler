---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-fax-detection-vxml-html-d7f2908199
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-fax-detection-vxml.html
retrieved_at: 2026-08-16T15:51:11.337440+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Fax Detection

## Chapter: Fax Detection

# Fax Detection

## Overview

The fax detection feature detects whether an inbound call is from a fax machine. If the inbound call is from a fax machine,
                           the call is rerouted appropriately.

### Feature Information for Fax Detection for SIP Call and Transfer

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Fax Detection for SIP Call and Transfer

Cisco IOS 15.4(2)T

Fax detection is the capability to detect automatically whether an incoming call is voice or fax. For calls coming from an
                                          IP trunk to CUBE, the Fax Detection for SIP Call and Transfer feature is used to detect CNG tones (calling tones) so that
                                          the fax server can handle the actual fax transmission or redirect the fax call to a configured fax number.

The following commands were introduced: cng-fax-detect and detect-fax mode .

Fax Detection for SIP Call and Transfer on Cisco IOS XE Platforms

Cisco IOS XE Amsterdam 17.2.1r

Support was introduced for SIP call and transfer for IP-to-IP calls on Cisco IOS XE platforms for Cisco Unified Border Element.

## Restrictions for Fax Detection for SIP Call and Transfer on Cisco IOS XE

The Fax Detect feature is supported with routers that are fitted with DSP modules.

Only the g711ulaw and g711alaw codecs are used for detecting the fax CNG tone.

Each destination number can be of maximum length of 32 characters.

Fax Detection is supported with LTI-based transcoding.

## Information About Fax Detection for SIP Call and Transfer

Fax detection is typically used if you need to have a single phone number for both voice and fax services. Incoming calls
                           are initially answered by an auto attendant or interactive voice response (IVR) service. At this point, the media stream is
                           monitored for fax tones. Calls identified as coming from a fax machine are then rerouted to a new destination, such as a fax
                           server.

For Fax detection to work, the cng-fax-detect command under DSP farm and the detect-fax command must be configured in the inbound dial-peer. The fax detection feature may be configured to redirect calls to a local
                           voice port or a remote application.

Fax detection on CUBE is also supported through a TCL script. The script answers an incoming call, plays a prompt and makes
                                       an outgoing voice or fax call. You can download the TCL script from the CiscoDevNet Github .

If the silence off attribute is received in the SDP and the fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback pass-through {g711alaw | g711ulaw} codec command is configured, CUBE interprets the received SDP as a fax switchover call.

### Local Redirect Mode

Local redirect may be used to transfer a fax call to either a local port or remote destination. Multiple destinations may
                              be used if required, allowing the CUBE to hunt for the first available resource. The configured hunt list can include any
                              number of destination ports.

An initial connection is made as a voice call through CUBE to the IVR. On detection of fax tones in the media path, CUBE closes
                              the connection to the IVR, then hunts through a list of numbers to establish a connection to a fax machine or fax server,
                              allowing the originating fax machine to complete its transmission. In a scenario where T.38 is not supported by CUBE, it will
                              fallback to passthrough.

For each call, a digital signal processor (DSP) channel is allocated to detect the fax CNG tone. This DSP remains allocated
                              until the original call leg clears at the end of the call. In the call flow example above, the first fax machine is busy,
                              so the CUBE establishes the call with the second fax machine.

For Local Redirect, new calls legs are negotiated as voice, not as fax session.

### Refer Redirect Mode

In this mode, calls are redirected to a fax service by the original calling party. The redirect is based on information provided
                              by CUBE in a SIP Refer message (similar to a blind transfer).

In this mode, only one redirection target can be configured.

An initial connection is made as a voice call through CUBE to the IVR. On detection of fax tones in the media path, CUBE closes
                              the connection to the IVR. To transfer the call, CUBE first sends a re-invite to put the original call leg on hold, then sends
                              a SIP REFER with details of the remote fax server. From this point, CUBE is no longer involved in the call flow as the originating
                              fax communicates directly with the destination server.

For each call, a DSP channel or resource is allocated to detect the CNG tone. This resource is released once the call transfer
                              has been initiated.

#### Transcoder Behavior for Cisco IOS XE

For the fax tone detection support offered for Cisco IOS XE, the DSP resource behavior for local and refer redirect is as
                                 follows:

For local redirect, CUBE doesn’t release the transcoder until the fax call disconnects.

For refer redirect, CUBE releases the transcoder when the REFER message is sent to the peer leg.

## Fax Detection with Cisco IOS XE High Availability

Fax detection and transfer are supported with CUBE High Availability (HA) deployments. In this mode, two CUBE routers are
                           configured to run in Active-Standby mode.

The following behaviors specific to this feature must be noted:

Failover after initial call has been established, but fax hasn’t been detected—The call is preserved, but tone detection is
                                 not available for the remainder of that call. The originating fax machine terminates the call after CNG time-out.

Failover after fax detection, but before the transferred call leg is established—The initial call is preserved and the transfer
                                 fails. The originating fax machine terminates the call after CNG time-out.

## Fax Detection Configuration for SIP Calls

### Configure DSP Resource to Detect Fax Tone

### SUMMARY STEPS

- enable

- configure terminal

- dspfarm profile tag transcode universal

- cng-fax-detect

- maximum sessions sessions

- asociate application CUBE

- end

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

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dspfarm profile tag transcode universal

#### Example:

```
Device(config)# dspfarm profile 5 transcode universal
```

Enters DSP farm profile configuration mode
                                             and enables the profile for transcoding.

Step 4

cng-fax-detect

#### Example:

```
Device(config-dspfarm-profile)# cng-fax-detect
```

Enables CNG tone detection.

Step 5

maximum sessions sessions

#### Example:

```
Device(config-dspfarm-profile)# maximum sessions 6
```

Configures maximum number of sessions.

Step 6

asociate application CUBE

#### Example:

```
Device(config-dspfarm-profile)# associate application CUBE
```

Configures an application to the profile for LTI-based transcoding.

Step 7

end

#### Example:

```
Device(config-dspfarm-profile)# end
```

Returns to privileged EXEC mode.

### Dial-peer Configuration to Redirect Fax Call

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice number voip

- description tag

- session protocol sipv2

- incoming called number number

- voice-class codec tag

- no vad

- detect-fax [ mode { refer number | local number } ]

- end

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

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice number voip

#### Example:

```
Device(config)# dial-peer voice 401 voip
```

Enters dial peer configuration mode for the specified VoIP dial peer.

Step 4

description tag

#### Example:

```
Device(config-dial-peer)# description Incoming dial-peer for Fax
```

Provides a description for the incoming dial-peer for Fax.

Step 5

session protocol sipv2

#### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Configures SIP as the session protocol type.

Step 6

incoming called number number

#### Example:

```
Device(config-dial-peer)# incoming called-number 903309
```

Creates inbound dial-peer.

Step 7

voice-class codec tag

#### Example:

```
Device(config-dial-peer)# voice-class codec 111
```

Applies the previously configured voice class and associated codecs to a dial peer. The voice class codec can only include
                                             g711ulaw and g711alaw.

Step 8

no vad

#### Example:

```
Device(config-dial-peer)# no vad
```

Disables voice activity detection (VAD) for the calls using the dial peer being configured.

Step 9

detect-fax [ mode { refer number | local number } ]

#### Example:

```
Device(config-dial-peer)# detect-fax refer 12101
```

Defines fax detection as local or refer mode and refers to the directory number of the fax machine.

If local mode is configured, then a list of numbers, separated by a space may be entered. Refer mode only allows a  destination
                                             number to be configured.

Step 10

end

#### Example:

```
Device(config-dial-peer)# end
```

Returns to privileged EXEC mode.

### Verify Fax Detection Configuration for SIP Calls

### SUMMARY STEPS

- enable

- show call active voice compact

- show dspfarm dsp active

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Step 2

show call active voice compact

#### Example:

This is a sample output of call setup when the call is connected:

```
Device# show call active voice compact <callID>  A/O FAX T<sec> Codec     type     Peer Address       IP R<ip>:<udp>
	      Total call-legs: 3
          	9    ANS   T4      g711ulaw    VOIP        P808808      9.42.25.145:17940
        		10    ORG   T4      g711ulaw    VOIP        P309903      9.42.25.149:16396
        		11    ANS   T4      g711ulaw    VOIP        P808808      9.42.25.149:16394
```

Step 3

show dspfarm dsp active

#### Example:

This is a sample output of  the DSP channel reserved to detect CNG tone after the call is set up.

```
Device# show dspfarm dsp active SLOT   DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID PKTS_TXED PKTS_RXED
	           0      2   36.1.0   UP     1   USED  xcode    1      9         228       119      
	           0      2   36.1.0   UP     1   USED  xcode    1      10        113       251      
 	    Total number of DSPFARM DSP channel(s) 1
```

### Troubleshoot Fax Failures due to Multiple M-Lines on the CUBE

The CUBE doesn't understand multiple m-lines during a voice-to-fax switch-over. To resolve this issue, you can adopt the following
                              workaround using Session Initiation Protocol (SIP) profiles.

#### Problem

When a provider sends an Invite message to the CUBE during a voice-to-fax switch-over, it includes a Session Description Protocol
                                 (SDP) with two m-lines. If the m-lines are in an unexpected format, then the CUBE fails to process it. As a result, it sends
                                 a malformed SDP to the fax server in the Invite message. Therefore, all calls fail.

Here is an example of an unaccepted m-line format:

m=image

m=audio

#### Solution

The workaround to troubleshoot fax failures due to multiple m-lines issue:

Use only one m-line for the voice-to-fax switch-over.

Use protocol-based pass-through.

Have the provider place the m=audio line above the m=image line.

Use the fax server in order to initiate the switch-over with the use of CNG in a T.30 indicator packet.

The CUBE version 10.0 uses a new feature for inbound SIP profiles. These profiles are applied to inbound SIP messages before
                                 it's presented to the SIP stack. The idea behind the use of the inbound SIP profiles in this scenario is to remove the m=audio line, so that the CUBE can work with a single m=image line.

Here is an example of the re-Invite message when the provider desires to escalate the voice call to fax:

```
Received:
INVITE sip:025027141@192.0.2.2:5060 SIP/2.0
Via: SIP/2.0/UDP 192.0.2.1:5060;branch=z9hG4bKnm30rd10dofho0fo9011sb0000g00.1
Call-ID: 6B6CB982-B41D11E3-898F851F-F1ADD198@192.0.2.2
From: <sip:026455288@25027100.xyz>;tag=7qapqh6u-CC-36
To: "Administrator" <sip:025027141@25027100.xyz>;tag=85A6C018-2489
CSeq: 1 INVITE
Contact: <sip:192.0.2.1:5060;transport=udp>
Max-Forwards: 69
Content-Length: 431
Content-Type: application/sdp
v=0
o=HuaweiSoftX3000 22157305 22157306 IN IP4 192.0.2.1
s=Sip Call
c=IN IP4 192.0.2.1
t=0 0
m=image 53200 udptl t38
a=T38FaxVersion:0
a=T38MaxBitRate:14400
a=T38FaxRateManagement:transferredTCF
a=T38FaxUdpEC:t38UDPRedundancy
m=audio 53190 RTP/AVP 8 0 101
a=rtpmap:8 PCMA/8000
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=ptime:20
a=silenceSupp:off - - - -
a=ecan:fb on -
a=X-fax
```

This SIP profile configuration can be applied in order to remove the m=audio line:

```
voice class sip-profiles 966
request REINVITE sdp-header Audio-Media modify "(.*)" "a=sendrecv"
voice service voip
sip
voice-class sip profiles 966 inbound
or 
dial-peer voice XYZ voip
voice-class sip profiles 966 inbound
```

The SIP profile changes the m=audio line to a=sendrecv , which acts as a line in the SDP that isn't relevant. This allows the CUBE to send a re-Invite message to the fax server
                                 and await the 200 OK response.

When sending a 200 OK message as a response to the received re-Invite, it includes both m-lines that adhere to RFC standards. The response message
                                 contains the same number of media attributes as the offer message.

This can be accomplished using a standard outbound SIP profile that is applied on the dial-peer of the provider:

```
voice class sip-profiles 200
response 200 method re-invite sdp-header Attribute modify "t38UDPRedundancy"
 "t38UDPRedundancy\x0D\x0Am=audio 0 RTP/AVP"
```

Replace the "t38UDPRedundancy" to ensure that the re-Invite with multiple m-lines is correctly handled and the response to the provider is RFC-compliant:

```
"t38UDPRedundancy"
New line ( \x0D\x0A )
m=audio 0 RTP/AVP
```

In order to resolve the issue of multiple m-lines, employ the workarounds that are discussed (most of which are provider-dependent).
                                 Also, it's observed that the Xmedius Server can initiate the switch-over, as it forces the server to send the T.38 re-Invite
                                 message avoiding multiple m-lines.

### Fax Detection Troubleshooting for SIP Calls

You can enable the logs of the following debug or show commands, which are helpful in debugging fax detection for SIP calls:

debug voip ipipgw all

debug ccsip verbose

debug voip ccapi all

debug voip dsmp all

debug voip hpi all

debug media resource provisioning all

show call active voice compact

show dspfarm dsp active

show voip rtp connections

## Configuration Examples for Fax Detection for SIP Calls

### Example: Configuring Local Redirect

The following is a sample configuration in local redirect mode for fax detection. In this example, the dial-peer has to be
                                 configured for the FAX directory numbers 9033010 and 9033011.

```
dspfarm profile 10 transcode universal  
 codec g729abr8
 codec g729ar8
 codec g711alaw
 codec g711ulaw
 codec g729r8
 codec ilbc
 codec g722-64
 cng-fax-detect
 maximum sessions 6
 associate application CUBE
!
dial-peer voice 401 voip
 description "Incoming dial-peer to ASR"
 session protocol sipv2
 incoming called-number 903309
 voice-class codec 111  
 dtmf-relay rtp-nte
 no vad
 detect-fax mode local 9033010 9033011 

dial-peer voice 406 voip
 description "Outbound dialpeer for ..."
 destination-pattern 9033010
 session protocol sipv2
 session target ipv4:9.41.36.11:14762
 voice-class codec 111  
 dtmf-relay rtp-nte
 fax protocol pass-through g711ulaw
 no vad

dial-peer voice 406 voip
 description "Outbound dialpeer for ..."
 destination-pattern 9033011 
 session protocol sipv2
 session target ipv4:9.41.36.11:14765
 voice-class codec 111  
 dtmf-relay rtp-nte
 fax protocol pass-through g711ulaw
 no vad
```

### Example: Configuring Refer Redirect

In Refer mode, only one fax number can be configured.

```
dial-peer voice 401 voip
 description "Incoming dial-peer to ASR"
 session protocol sipv2
 incoming called-number 903309
 voice-class codec 111  
 dtmf-relay rtp-nte
 no vad
 detect-fax mode refer 9033010 

dial-peer voice 406 voip
 description "Outbound dialpeer for ..."
 destination-pattern 9033010
 session protocol sipv2
 session target ipv4:9.41.36.11:14762
 voice-class codec 111  
 dtmf-relay rtp-nte
 fax protocol pass-through g711ulaw
 no vad
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| Fax Detection for SIP Call and Transfer | Cisco IOS 15.4(2)T | Fax detection is the capability to detect automatically whether an incoming call is voice or fax. For calls coming from an
                                          IP trunk to CUBE, the Fax Detection for SIP Call and Transfer feature is used to detect CNG tones (calling tones) so that
                                          the fax server can handle the actual fax transmission or redirect the fax call to a configured fax number. The following commands were introduced: cng-fax-detect and detect-fax mode . |
| Fax Detection for SIP Call and Transfer on Cisco IOS XE Platforms | Cisco IOS XE Amsterdam 17.2.1r | Support was introduced for SIP call and transfer for IP-to-IP calls on Cisco IOS XE platforms for Cisco Unified Border Element. |

| Note | Fax detection on CUBE is also supported through a TCL script. The script answers an incoming call, plays a prompt and makes
                                       an outgoing voice or fax call. You can download the TCL script from the CiscoDevNet Github . |
|---|---|

| Note | If the silence off attribute is received in the SDP and the fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback pass-through {g711alaw \| g711ulaw} codec command is configured, CUBE interprets the received SDP as a fax switchover call. |
|---|---|---|

| Note | For Local Redirect, new calls legs are negotiated as voice, not as fax session. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dspfarm profile tag transcode universal Example: Device(config)# dspfarm profile 5 transcode universal | Enters DSP farm profile configuration mode
                                             and enables the profile for transcoding. |
| Step 4 | cng-fax-detect Example: Device(config-dspfarm-profile)# cng-fax-detect | Enables CNG tone detection. |
| Step 5 | maximum sessions sessions Example: Device(config-dspfarm-profile)# maximum sessions 6 | Configures maximum number of sessions. |
| Step 6 | asociate application CUBE Example: Device(config-dspfarm-profile)# associate application CUBE | Configures an application to the profile for LTI-based transcoding. |
| Step 7 | end Example: Device(config-dspfarm-profile)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice number voip Example: Device(config)# dial-peer voice 401 voip | Enters dial peer configuration mode for the specified VoIP dial peer. |
| Step 4 | description tag Example: Device(config-dial-peer)# description Incoming dial-peer for Fax | Provides a description for the incoming dial-peer for Fax. |
| Step 5 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Configures SIP as the session protocol type. |
| Step 6 | incoming called number number Example: Device(config-dial-peer)# incoming called-number 903309 | Creates inbound dial-peer. |
| Step 7 | voice-class codec tag Example: Device(config-dial-peer)# voice-class codec 111 | Applies the previously configured voice class and associated codecs to a dial peer. The voice class codec can only include
                                             g711ulaw and g711alaw. |
| Step 8 | no vad Example: Device(config-dial-peer)# no vad | Disables voice activity detection (VAD) for the calls using the dial peer being configured. |
| Step 9 | detect-fax [ mode { refer number \| local number } ] Example: Device(config-dial-peer)# detect-fax refer 12101 | Defines fax detection as local or refer mode and refers to the directory number of the fax machine. If local mode is configured, then a list of numbers, separated by a space may be entered. Refer mode only allows a  destination
                                             number to be configured. |
| Step 10 | end Example: Device(config-dial-peer)# end | Returns to privileged EXEC mode. |

| Step 1 | enable Example: Device> enable Enables privileged EXEC mode. |
|---|---|
| Step 2 | show call active voice compact Example: This is a sample output of call setup when the call is connected: Device# show call active voice compact <callID>  A/O FAX T<sec> Codec     type     Peer Address       IP R<ip>:<udp>
	      Total call-legs: 3
          	9    ANS   T4      g711ulaw    VOIP        P808808      9.42.25.145:17940
        		10    ORG   T4      g711ulaw    VOIP        P309903      9.42.25.149:16396
        		11    ANS   T4      g711ulaw    VOIP        P808808      9.42.25.149:16394 |
| Step 3 | show dspfarm dsp active Example: This is a sample output of  the DSP channel reserved to detect CNG tone after the call is set up. Device# show dspfarm dsp active SLOT   DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID PKTS_TXED PKTS_RXED
	           0      2   36.1.0   UP     1   USED  xcode    1      9         228       119      
	           0      2   36.1.0   UP     1   USED  xcode    1      10        113       251      
 	    Total number of DSPFARM DSP channel(s) 1 |