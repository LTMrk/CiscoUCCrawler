---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-border-element-118939-technote-cube-00-html-74b9ea8eae
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-border-element/118939-technote-cube-00.html
retrieved_at: 2026-08-16T15:57:05.779916+00:00
---

Troubleshoot Fax Failures Due to Multiple M-Lines on the CUBE

# Troubleshoot Fax Failures Due to Multiple M-Lines on the CUBE

### Download Options

Updated: April 24, 2015

Document ID: 118939

Contents

## Contents

## Introduction

This document describes how to resolve an issue on the Cisco Unified Border Element (CUBE) when outbound fax failures occur due to multiple m-lines from a provider. The CUBE does not understand multiple m-lines, but a workaround can be implemented on the CUBE in order to resolve the issue with the use of Session Initiation Protocol (SIP) profiles.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these hardware and software versions:

- Fax Server

- Cisco Unified Communications Manager (CUCM)

- CUBE

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Network Topology

The example that is described in this document uses this network topology:

## Problem

When a provider sends an Invite message to the CUBE during a voice-to-fax switch-over, and it includes a Session Description Protocol (SDP) that contains two m-lines, the original behavior of the CUBE was to reject the call with an SIP 488 Not Acceptable Here message.

After Cisco bug ID CSCtw96549 , this behavior has changed. Now, if a provider sends an SDP with two m-lines, the call goes through as expected.

Here is an example of an accepted m-line format:

m=audio m=image

However, if a provider sends an SDP with the m-line format reversed, the CUBE does not process it correctly and sends a malformed SDP to the fax server in the Invite message. Therefore, all calls fail.

Here is an example of an unaccepted m-line format:

m=image m=audio

Tip : For further details, refer to Cisco bug ID CSCue70469 .

## Solution

In order to troubleshoot this issue, make a outbound fax test call and collect the SIP debugs ( debug ccsip messages). From the debug output, these observations can be made:

- The voice call establishes with no issues.

Note : It is not always mandatory for the side that is called to initiate the switch-over. Several fax servers have the capability to initiate the switch-over, even though they are the terminal from which the call originate s. This is done via the encapsulation of the calling (CNG) tone in the T.30 Indicator packets.

- The re-invite for the switch-over has two media lines (m=) such that the m=image line is placed above the m=audio line, in which case the defect that is described in Cisco bug ID CSCue70469 arises and the CUBE disconnects the call.

Currently, there is no resolution for this issue on the CUBE, but you can alter the external factors in order to workaround the issue:

- Use only one m-line for the voice-to-fax switch-over.

- Use protocol-based pass-through.

- Have the provider place the m=audio line above the m=image line.

- Use the fax server in order to initiate the switch-over with the use of CNG in a T.30 Indicator packet.

The CUBE Version 10.0 leverages a new feature for inbound SIP profiles, where the SIP profiles are applied on an inbound SIP message before it is presented to the SIP stack and processed. The idea behind the use of the inbound SIP profiles in this scenario is to remove the m=audio line all together so that the CUBE can work with only a single m=image line.

Here is an example of the re-Invite message when the provider desires to escalate the voice call to fax:

```
Received: INVITE sip:025027141@192.0.2.2:5060 SIP/2.0 Via: SIP/2.0/UDP 192.0.2.1:5060;branch=z9hG4bKnm30rd10dofho0fo9011sb0000g00.1 Call-ID: 6B6CB982-B41D11E3-898F851F-F1ADD198@192.0.2.2 From: <sip:026455288@25027100.xyz>; tag=7qapqh6u-CC-36 To: "Administrator" <sip:025027141@25027100.xyz>; tag=85A6C018-2489 CSeq: 1 INVITE Contact: <sip:192.0.2.1:5060;transport=udp> Max-Forwards: 69 Content-Length: 431 Content-Type: application/sdp v=0 o=HuaweiSoftX3000 22157305 22157306 IN IP4 192.0.2.1 s=Sip Call c=IN IP4 192.0.2.1 t=0 0 m=image 53200 udptl t38 a=T38FaxVersion:0 a=T38MaxBitRate:14400 a=T38FaxRateManagement:transferredTCF a=T38FaxUdpEC:t38UDPRedundancy m=audio 53190 RTP/AVP 8 0 101 a=rtpmap:8 PCMA/8000 a=rtpmap:0 PCMU/8000 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-15 a=ptime:20 a=silenceSupp:off - - - - a=ecan:fb on - a=X-fax ================================
```

This SIP profile configuration can be applied in order to remove the m=audio line:

```
voice class sip-profiles 966 request REINVITE sdp-header Audio-Media modify "(.*)" "a=sendrecv" voice service voip sip voice-class sip profiles 966 inbound or dial-peer voice XYZ voip voice-class sip profiles 966 inbound
```

This SIP profile changes the m=audio line to a=sendrecv , which acts as a line in the SDP that is not relevant. This allows the CUBE to send a re-Invite message to the fax server side and await the 200 OK response.

You must also address one more important aspect: When the 200 OK message is sent to the provider in response to the received re-Invite, it must present both of the m-lines in order to comply with RFC and ensure that the response message has the same number of media attributes as the offer message.

You can accomplish this via a standard outbound SIP profile that is applied on the dial-peer that points to the provider:

```
voice class sip-profiles 200 response 200 method re-invite sdp-header Attribute modify "t38UDPRedundancy" "t38UDPRedundancy\x0D\x0Am=audio 0 RTP/AVP"
```

This ensures that the re-Invite with multiple m-lines is correctly handled and that the response to the provider is RFC-compliant because the "t38UDPReddundancy" is replaced by:

```
"t38UDPRedundancy" New line ( \x0D\x0A ) m=audio 0 RTP/AVP
```

In summary, employ the use of the the workarounds that are described in this document (most of which are provider-dependent) in order to the resolve issue of multiple m-lines. Also, it has been observed that the Xmedius Server can also initiate the switch-over, as it forces the server to send the T.38 re-Invite message and avoids the presentation of multiple m-lines.

### Revision History

1.0

24-Apr-2015

Initial Release

### Contributed by Cisco Engineers

Kaustubh Inamdar and Mudit Mathur

Cisco TAC Engineers.

### This Document Applies to These Products

- Unified Border Element

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 24-Apr-2015 | Initial Release |