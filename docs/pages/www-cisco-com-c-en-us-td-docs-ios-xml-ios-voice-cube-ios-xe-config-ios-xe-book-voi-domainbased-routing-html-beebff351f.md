---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-voi-domainbased-routing-html-beebff351f
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/voi-domainbased-routing.html
retrieved_at: 2026-08-16T15:46:03.904933+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Domain-Based Routing

## Chapter: Domain-Based Routing

# Domain-Based Routing

## Overview

The Domain-based routing feature provides support for matching an outbound dial peer based on the domain name or IP address
                           provided in the request URI of the incoming SIP message or an inbound dial peer.

Domain-based routing enables for calls to be routed on the outbound dialpeer based on the domain name or IP address provided
                           in the request Uniform Resource Identifier (URI) of incoming Session IP message.

When a dial peer has an application configured as a session application, then only the user parameter of the request URI
                           is used and is sent from the inbound SIP SPI to the application. The session application performs a match on an outbound dial
                           peer based on the user parameter of the request URI sent from the inbound dial peer. In the figure below, 567 is the user
                           portion of the request-URI that is passed from the inbound dial peer to the application and the matching outbound dial-peer
                           found is 1000.

With the introduction of the domain-based routing feature, all parameters including the domain name of the request URI will
                           be sent to the application and the outbound dial peer can be matched with any parameter. In Figure 1, when the domain name
                           example.com is used to match an outbound dial peer the resulting dial peer is 2000. The call route url command is used for configuring domain-based routing.

Translation rules should be applied to outgoing dial peers instead of inbound dial peers when the call route url command is configured. If the translation rule is applied to inbound dial peers, it becomes ineffective when call-route url is enabled. In this scenario, the call-route url takes precedence and selects the called number, disregarding the translated number. Therefore, the call-route url supersedes any translation rules applied to inbound dial peers.

Domain-based routing support is available only for SIP-SIP call flows.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator
                                 enables you to determine which software images support a specific software release, feature set, or platform. To access Cisco
                                 Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

Feature Name

Releases

Feature Information

Domain Based Routing Support on the CUBE

15.2(1)T

Cisco IOS XE Release 3.8S

The domain-based routing enables for calls to be routed on the outbound dial peer based on the domain name or IP address
                                             provided in the request URI (Uniform Resource Identifier) of incoming SIP message.

The following commands were introduced or modified: call-route , voice-class sip call-route .

Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command
                                 display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses
                                 in illustrative content is unintentional and coincidental. © 2011 Cisco Systems, Inc. All rights reserved

## Configure Domain-Based Routing

### Configure Domain-Based Routing at Global Level

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- call-route url

- exit

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

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters voice service configuration mode.

Step 4

sip

#### Example:

```
Device(conf-voi-serv)# sip
```

Enters voice service SIP configuration mode.

Step 5

call-route url

#### Example:

```
Device(conf-serv-sip)# call-route url
```

#### Example:

Routes calls based on the URL.

Step 6

exit

#### Example:

```
Device(conf-serv-sip)# exit
```

Exits the current mode.

### Configure Domain-Based Routing at Dial Peer Level

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice dial-peer tag voip

- voice-class sip call-route url

- exit

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

dial-peer voice dial-peer tag voip

#### Example:

```
Device(config)# dial-peer voice 2 voip
```

Enter dial peer voice configuration mode.

Step 4

voice-class sip call-route url

#### Example:

```
Device(config-dial-peer)#
```

#### Example:

Routes calls based on the URL

Step 5

exit

#### Example:

```
Device(config-dial-peer)# exit
```

Exits the current mode.

### Verify and Troubleshoot Domain-Based Routing

Use this procedure to verify and troubleshoot domain-based routing on CUBE.

### SUMMARY STEPS

- enable

- debug ccsip all

- debug voip dialpeer inout

### DETAILED STEPS

Step 1

enable

Enables privileged EXEC mode.

#### Example:

```
Device> enable
```

Step 2

debug ccsip all

Enables all SIP-related debugging.

#### Example:

```
Device# debug ccsip all Received:
INVITE sip:5555555555@[2208:1:1:1:1:1:1:1118]:5060 SIP/2.0
Via: SIP/2.0/UDP [2208:1:1:1:1:1:1:1115]:5060;branch=z9hG4bK83AE3
Remote-Party-ID: <sip:2222222222@[2208:1:1:1:1:1:1:1115]>;party=calling;screen=no;privacy=off
From: <sip:2222222222@[2208:1:1:1:1:1:1:1115]>;tag=627460F0-1259
To: <sip:5555555555@[2208:1:1:1:1:1:1:1118]>
Date: Tue, 01 Mar 2011 08:49:48 GMT
Call-ID: B30FCDEB-431711E0-8EDECB51-E9F6B1F1@2208:1:1:1:1:1:1:1115
Supported: 100rel,timer,resource-priority,replaces
Require: sdp-anat
Min-SE:  1800
Cisco-Guid: 2948477781-1125585376-2396638033-3925258737
User-Agent: Cisco-SIPGateway/IOS-15.1(3.14.2)PIA16
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
CSeq: 101 INVITE
Max-Forwards: 70
Timestamp: 1298969388
Contact: <sip:2222222222@[2208:1:1:1:1:1:1:1115]:5060>
Expires: 180
Allow-Events: telephone-event
Content-Type: application/sdp
Content-Disposition: session;handling=required
Content-Length: 495
v=0
o=CiscoSystemsSIP-GW-UserAgent 7880 7375 IN IP6 2208:1:1:1:1:1:1:1115
s=SIP Call
c=IN IP6 2208:1:1:1:1:1:1:1115
t=0 0
a=group:ANAT 1 2
m=audio 17836 RTP/AVP 0 101 19
c=IN IP6 2208:1:1:1:1:1:1:1115
a=mid:1                                                
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=rtpmap:19 CN/8000
a=ptime:20
m=audio 18938 RTP/AVP 0 101 19
c=IN IP4 9.45.36.111
a=mid:2                                                
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=rtpmap:19 CN/8000
a=ptime:20
“Received: 
INVITE sip:2222222222@[2208:1:1:1:1:1:1:1117]:5060 SIP/2.0
Via: SIP/2.0/UDP [2208:1:1:1:1:1:1:1116]:5060;branch=z9hG4bK38ACE
Remote-Party-ID: <sip:5555555555@[2208:1:1:1:1:1:1:1116]>;party=calling;screen=no;privacy=off
From: <sip:5555555555@[2208:1:1:1:1:1:1:1116]>;tag=4FE8C9C-1630
To: <sip:2222222222@[2208:1:1:1:1:1:1:1117]>;tag=1001045C-992
Date: Thu, 10 Feb 2011 12:15:08 GMT
Call-ID: 5DEDB77E-ADC11208-808BE770-8FCACF34@2208:1:1:1:1:1:1:1117
Supported: 100rel,timer,resource-priority,replaces,sdp-anat
Min-SE:  1800
Cisco-Guid: 1432849350-0876876256-2424621905-3925258737
User-Agent: Cisco-SIPGateway/IOS-15.1(3.14.2)PIA16
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
CSeq: 101 INVITE
Max-Forwards: 70
Timestamp: 1297340108
Contact: <sip:5555555555@[2208:1:1:1:1:1:1:1116]:5060>
Expires: 180
Allow-Events: telephone-event
Content-Type: application/sdp
Content-Length: 424
v=0
o=CiscoSystemsSIP-GW-UserAgent 8002 7261 IN IP6 2208:1:1:1:1:1:1:1116
s=SIP Call
c=IN IP6 2208:1:1:1:1:1:1:1116
t=0 0
m=image 17278 udptl t38
c=IN IP6 2208:1:1:1:1:1:1:1116
a=T38FaxVersion:0
a=T38MaxBitRate:14400
a=T38FaxFillBitRemoval:0
a=T38FaxTranscodingMMR:0
a=T38FaxTranscodingJBIG:0
a=T38FaxRateManagement:transferredTCF
a=T38FaxMaxBuffer:200
a=T38FaxMaxDatagram:320
a=T38FaxUdpEC:t38UDPRedundancy”
```

Step 3

debug voip dialpeer inout

The debug ccsip all and debug voip dialpeer inout commands can be entered in any order and any of the commands can be used for debugging depending on the requirement.

#### Example:

```
Displays information about the voice dial peers
Device# debug voip dialpeer inout voip dialpeer inout debugging is on
```

The following event shows the calling and called numbers:

#### Example:

```
*May  1 19:32:11.731: //-1/6372E2598012/DPM/dpAssociateIncomingPeerCore:
   Calling Number=4085550111, Called Number=3600, Voice-Interface=0x0,
   Timeout=TRUE, Peer Encap Type=ENCAP_VOIP, Peer Search Type=PEER_TYPE_VOICE,
   Peer Info Type=DIALPEER_INFO_SPEECH
```

The following event shows the incoming dial peer:

#### Example:

```
*May  1 19:32:11.731: //-1/6372E2598012/DPM/dpAssociateIncomingPeerCore:
   Result=Success(0) after DP_MATCH_INCOMING_DNIS; Incoming Dial-peer=100
*May  1 19:32:11.731: //-1/6372E2598012/DPM/dpAssociateIncomingPeerCore:
   Calling Number=4085550111, Called Number=3600, Voice-Interface=0x0,
   Timeout=TRUE, Peer Encap Type=ENCAP_VOIP, Peer Search Type=PEER_TYPE_VOICE,
   Peer Info Type=DIALPEER_INFO_SPEECH
*May  1 19:32:11.731: //-1/6372E2598012/DPM/dpAssociateIncomingPeerCore:
   Result=Success(0) after DP_MATCH_INCOMING_DNIS; Incoming Dial-peer=100
*May  1 19:32:11.735: //-1/6372E2598012/DPM/dpMatchPeersCore:
   Calling Number=, Called Number=3600, Peer Info Type=DIALPEER_INFO_SPEECH
*May  1 19:32:11.735: //-1/6372E2598012/DPM/dpMatchPeersCore:
   Match Rule=DP_MATCH_DEST; Called Number=3600
*May  1 19:32:11.735: //-1/6372E2598012/DPM/dpMatchPeersCore:
   Result=Success(0) after DP_MATCH_DEST
*May  1 19:32:11.735: //-1/6372E2598012/DPM/dpMatchPeersMoreArg:
   Result=SUCCESS(0)
```

The following event shows the matched dial peers in the order of priority:

#### Example:

```
List of Matched Outgoing Dial-peer(s):
     1: Dial-peer Tag=3600
     2: Dial-peer Tag=36
```

## Configuration Examples for Domain-Based Routing

### Example Configuring Domain-Based Routing

The following example shows how to enable domain-based routing support on the CUBE :

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# sip Device(conf-serv-sip)# call-route url Device(conf-serv-sip)# exit Device(config)# dial-peer voice 2 voip Device(config-dial-peer)# voice-class sip call-route url Device(config-dial-peer)# exit
```

| Note | Translation rules should be applied to outgoing dial peers instead of inbound dial peers when the call route url command is configured. If the translation rule is applied to inbound dial peers, it becomes ineffective when call-route url is enabled. In this scenario, the call-route url takes precedence and selects the called number, disregarding the translated number. Therefore, the call-route url supersedes any translation rules applied to inbound dial peers. |
|---|---|

| Feature Name | Releases | Feature Information |
|---|---|---|
| Domain Based Routing Support on the CUBE | 15.2(1)T Cisco IOS XE Release 3.8S | The domain-based routing enables for calls to be routed on the outbound dial peer based on the domain name or IP address
                                             provided in the request URI (Uniform Resource Identifier) of incoming SIP message. The following commands were introduced or modified: call-route , voice-class sip call-route . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters voice service configuration mode. |
| Step 4 | sip Example: Device(conf-voi-serv)# sip | Enters voice service SIP configuration mode. |
| Step 5 | call-route url Example: Device(conf-serv-sip)# call-route url Example: | Routes calls based on the URL. |
| Step 6 | exit Example: Device(conf-serv-sip)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice dial-peer tag voip Example: Device(config)# dial-peer voice 2 voip | Enter dial peer voice configuration mode. |
| Step 4 | voice-class sip call-route url Example: Device(config-dial-peer)# Example: Routes calls based on the URL |  |
| Step 5 | exit Example: Device(config-dial-peer)# exit | Exits the current mode. |

| Step 1 | enable Enables privileged EXEC mode. Example: Device> enable |
|---|---|
| Step 2 | debug ccsip all Enables all SIP-related debugging. Example: Device# debug ccsip all Received:
INVITE sip:5555555555@[2208:1:1:1:1:1:1:1118]:5060 SIP/2.0
Via: SIP/2.0/UDP [2208:1:1:1:1:1:1:1115]:5060;branch=z9hG4bK83AE3
Remote-Party-ID: <sip:2222222222@[2208:1:1:1:1:1:1:1115]>;party=calling;screen=no;privacy=off
From: <sip:2222222222@[2208:1:1:1:1:1:1:1115]>;tag=627460F0-1259
To: <sip:5555555555@[2208:1:1:1:1:1:1:1118]>
Date: Tue, 01 Mar 2011 08:49:48 GMT
Call-ID: B30FCDEB-431711E0-8EDECB51-E9F6B1F1@2208:1:1:1:1:1:1:1115
Supported: 100rel,timer,resource-priority,replaces
Require: sdp-anat
Min-SE:  1800
Cisco-Guid: 2948477781-1125585376-2396638033-3925258737
User-Agent: Cisco-SIPGateway/IOS-15.1(3.14.2)PIA16
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
CSeq: 101 INVITE
Max-Forwards: 70
Timestamp: 1298969388
Contact: <sip:2222222222@[2208:1:1:1:1:1:1:1115]:5060>
Expires: 180
Allow-Events: telephone-event
Content-Type: application/sdp
Content-Disposition: session;handling=required
Content-Length: 495
v=0
o=CiscoSystemsSIP-GW-UserAgent 7880 7375 IN IP6 2208:1:1:1:1:1:1:1115
s=SIP Call
c=IN IP6 2208:1:1:1:1:1:1:1115
t=0 0
a=group:ANAT 1 2
m=audio 17836 RTP/AVP 0 101 19
c=IN IP6 2208:1:1:1:1:1:1:1115
a=mid:1                                                
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=rtpmap:19 CN/8000
a=ptime:20
m=audio 18938 RTP/AVP 0 101 19
c=IN IP4 9.45.36.111
a=mid:2                                                
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=rtpmap:19 CN/8000
a=ptime:20
“Received: 
INVITE sip:2222222222@[2208:1:1:1:1:1:1:1117]:5060 SIP/2.0
Via: SIP/2.0/UDP [2208:1:1:1:1:1:1:1116]:5060;branch=z9hG4bK38ACE
Remote-Party-ID: <sip:5555555555@[2208:1:1:1:1:1:1:1116]>;party=calling;screen=no;privacy=off
From: <sip:5555555555@[2208:1:1:1:1:1:1:1116]>;tag=4FE8C9C-1630
To: <sip:2222222222@[2208:1:1:1:1:1:1:1117]>;tag=1001045C-992
Date: Thu, 10 Feb 2011 12:15:08 GMT
Call-ID: 5DEDB77E-ADC11208-808BE770-8FCACF34@2208:1:1:1:1:1:1:1117
Supported: 100rel,timer,resource-priority,replaces,sdp-anat
Min-SE:  1800
Cisco-Guid: 1432849350-0876876256-2424621905-3925258737
User-Agent: Cisco-SIPGateway/IOS-15.1(3.14.2)PIA16
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
CSeq: 101 INVITE
Max-Forwards: 70
Timestamp: 1297340108
Contact: <sip:5555555555@[2208:1:1:1:1:1:1:1116]:5060>
Expires: 180
Allow-Events: telephone-event
Content-Type: application/sdp
Content-Length: 424
v=0
o=CiscoSystemsSIP-GW-UserAgent 8002 7261 IN IP6 2208:1:1:1:1:1:1:1116
s=SIP Call
c=IN IP6 2208:1:1:1:1:1:1:1116
t=0 0
m=image 17278 udptl t38
c=IN IP6 2208:1:1:1:1:1:1:1116
a=T38FaxVersion:0
a=T38MaxBitRate:14400
a=T38FaxFillBitRemoval:0
a=T38FaxTranscodingMMR:0
a=T38FaxTranscodingJBIG:0
a=T38FaxRateManagement:transferredTCF
a=T38FaxMaxBuffer:200
a=T38FaxMaxDatagram:320
a=T38FaxUdpEC:t38UDPRedundancy” |
| Step 3 | debug voip dialpeer inout The debug ccsip all and debug voip dialpeer inout commands can be entered in any order and any of the commands can be used for debugging depending on the requirement. Example: Displays information about the voice dial peers
Device# debug voip dialpeer inout voip dialpeer inout debugging is on The following event shows the calling and called numbers: Example: *May  1 19:32:11.731: //-1/6372E2598012/DPM/dpAssociateIncomingPeerCore:
   Calling Number=4085550111, Called Number=3600, Voice-Interface=0x0,
   Timeout=TRUE, Peer Encap Type=ENCAP_VOIP, Peer Search Type=PEER_TYPE_VOICE,
   Peer Info Type=DIALPEER_INFO_SPEECH The following event shows the incoming dial peer: Example: *May  1 19:32:11.731: //-1/6372E2598012/DPM/dpAssociateIncomingPeerCore:
   Result=Success(0) after DP_MATCH_INCOMING_DNIS; Incoming Dial-peer=100
*May  1 19:32:11.731: //-1/6372E2598012/DPM/dpAssociateIncomingPeerCore:
   Calling Number=4085550111, Called Number=3600, Voice-Interface=0x0,
   Timeout=TRUE, Peer Encap Type=ENCAP_VOIP, Peer Search Type=PEER_TYPE_VOICE,
   Peer Info Type=DIALPEER_INFO_SPEECH
*May  1 19:32:11.731: //-1/6372E2598012/DPM/dpAssociateIncomingPeerCore:
   Result=Success(0) after DP_MATCH_INCOMING_DNIS; Incoming Dial-peer=100
*May  1 19:32:11.735: //-1/6372E2598012/DPM/dpMatchPeersCore:
   Calling Number=, Called Number=3600, Peer Info Type=DIALPEER_INFO_SPEECH
*May  1 19:32:11.735: //-1/6372E2598012/DPM/dpMatchPeersCore:
   Match Rule=DP_MATCH_DEST; Called Number=3600
*May  1 19:32:11.735: //-1/6372E2598012/DPM/dpMatchPeersCore:
   Result=Success(0) after DP_MATCH_DEST
*May  1 19:32:11.735: //-1/6372E2598012/DPM/dpMatchPeersMoreArg:
   Result=SUCCESS(0) The following event shows the matched dial peers in the order of priority: Example: List of Matched Outgoing Dial-peer(s):
     1: Dial-peer Tag=3600
     2: Dial-peer Tag=36 |