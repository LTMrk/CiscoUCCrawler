---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-border-element-217860-troubleshooting-busyout-dial-pee-de1b583dce
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-border-element/217860-troubleshooting-busyout-dial-peers-on-cu.html
retrieved_at: 2026-08-16T15:56:36.545163+00:00
---

Troubleshoot Busyout Dial Peers on CUBE or IOS Voice Gateway

# Troubleshoot Busyout Dial Peers on CUBE or IOS Voice Gateway

### Download Options

Updated: July 24, 2025

Document ID: 217860

Contents

## Contents

## Introduction

This document describes the issue of Cisco Unified Border Elements/voice gateway dial peer status busyout and call failures after Cisco IOS® upgrade.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on Cisco Unified Border Elements (CUBE).

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document covers failures after Cisco IOS® upgrade to 16.12.6/17.3.5/17.6.1 or higher versions.

## Problem

The calls are failing via Cisco IOS Voice Gateway or CUBE after Cisco IOS upgrade to 16.12.6/17.3.5/17.6.1/17.7.1 or higher versions.

### Symptoms

When CUBE receives a SIP call, ad matches an outgoing dial-peer with session server-group and sip options-keepalive configured, the call fails at the Call Control Application Programming Interface (CCAPI) layer with Cause Value 188.

The CUBE does not send out outbound INVITE to the destination servers that are part of the server group.

The incoming INVITE is responded to with TRYING and 503 Service Unavailable.

The same behavior is observed even when the dial-peer shows as busyout or active KEEPALIVE status under show dial-peer voice summary .

Sample configuration/dial-peer status/debug snippet:

```
dial-peer voice 1000 voip
 destination-pattern ^1000$
 session protocol sipv2
 session transport tcp
 session server-group 1
 voice-class sip options-keepalive profile 1
 voice-class sip bind control source-interface GigabitEthernet0/0/1
 voice-class sip bind media source-interface GigabitEthernet0/0/1
 dtmf-relay rtp-nte sip-kpml
 codec g711ulaw
 ip qos dscp cs3 signaling
 no vad  
voice class server-group 1
 ipv4 10.106.117.11
 ipv4 10.106.117.6 preference 1
```

```
show dial-peer voice summary

             AD                                    PRE PASS SESS-SER-GRP  OUT

TAG    TYPE  MIN  OPER PREFIX    DEST-PATTERN      FER THRU SESS-TARGET    STAT PORT    KEEPALIVE    VRF

3001   voip  up   up                                0  syst                                             NA                 
1000   voip  up   up             ^1000$             0  syst SESS-SVR-GRP: 1               busyout    NA

show dial-peer voice summary

             AD                                    PRE PASS SESS-SER-GRP  OUT

TAG    TYPE  MIN  OPER PREFIX    DEST-PATTERN      FER THRU SESS-TARGET    STAT PORT    KEEPALIVE    VRF

3001   voip  up   up                                0  syst                                                NA                 
1000   voip  up   up             ^1000$             0  syst SESS-SVR-GRP: 1               active     NA
```

```
Debug snippet:

007592: Apr  7 07:28:56.046: //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:
Received:
INVITE sip:1000@10.106.117.5:5060 SIP/2.0
Via: SIP/2.0/UDP 10.106.117.2:5060;branch=z9hG4bK51889
Remote-Party-ID: <sip:3001@10.106.117.2>;party=calling;screen=no;privacy=off
From: <sip:3001@10.106.117.2>;tag=12EE76F8-154A
To: <sip:1000@10.106.117.5>
Date: Wed, 06 Apr 2022 18:28:16 GMT
Call-ID: 28E9846D-B50E11EC-8025D5B1-C2D1F237@10.106.117.2
Supported: 100rel,timer,resource-priority,replaces,sdp-anat
Min-SE:  1800
Cisco-Guid: 0678152134-3037598188-2149635505-3268538935
User-Agent: Cisco-SIPGateway/IOS-12.x
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
CSeq: 101 INVITE
Max-Forwards: 70
Timestamp: 1649269696
Contact: <sip:3001@10.106.117.2:5060>
Expires: 180
Allow-Events: telephone-event
Content-Type: application/sdp
Content-Disposition: session;handling=required
Content-Length: 247

v=0
o=CiscoSystemsSIP-GW-UserAgent 8965 7288 IN IP4 10.106.117.2
s=SIP Call
c=IN IP4 10.106.117.2
t=0 0
m=audio 18406 RTP/AVP 0 101
c=IN IP4 10.106.117.2
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=ptime:20

007649: Apr  7 07:28:56.050://-1/286BC7C68020/SIP/Info/info/2048/sipSPIGetCallConfig: Peer tag 3001 matched for incoming call

007872: Apr  7 07:28:56.061: //89/286BC7C68020/CCAPI/ccCallSetupRequest:
   Destination=, Calling IE Present=TRUE, Mode=0,
   Outgoing Dial-peer=1000, Params=0x7FF65E441DE8, Progress Indication=NULL(0)

007935: Apr  7 07:28:56.064: //-1/xxxxxxxxxxxx/SIP/Info/critical/8192/ccsip_call_setup_request: SIP Dialpeer 1000 busied out due to options-keepalive profile in server group

008160: Apr  7 07:28:56.073: //90/286BC7C68020/CCAPI/cc_api_call_disconnected:
   Cause Value=188, Interface=0x7FF64F4542E8, Call Id=90
008199: Apr  7 07:28:56.077: //89/286BC7C68020/CCAPI/ccCallDisconnect:
   Cause Value=188, Tag=0x0, Call Entry(Previous Disconnect Cause=0, Disconnect Cause=0)
008239: Apr  7 07:28:56.079: //89/286BC7C68020/SIP/Msg/ccsipDisplayMsg:
Sent:
SIP/2.0 503 Service Unavailable
Via: SIP/2.0/UDP 10.106.117.2:5060;branch=z9hG4bK51889
From: <sip:3001@10.106.117.2>;tag=12EE76F8-154A
To: <sip:1000@10.106.117.5>;tag=1C2F76-17F5
Date: Wed, 06 Apr 2022 17:28:56 GMT
Call-ID: 28E9846D-B50E11EC-8025D5B1-C2D1F237@10.106.117.2
Timestamp: 1649269696
CSeq: 101 INVITE
Allow-Events: telephone-event
Server: Cisco-SIPGateway/IOS-17.3.5
Reason: Q.850;cause=0
Session-ID: 00000000000000000000000000000000;remote=3c1f754eba075201a684fda2c51c04df
Content-Length: 0
```

## Workaround

- Configure the outgoing dial-peer with session target ip4 instead of session server-group . If needed, create a separate dial-peer for each IP of the server group.

```
dial-peer voice 1000 voip
 session target ipv4:x.x.x.x
dial-peer voice 1001 voip
 session target ipv4:x.x.x.x
```

- Remove the sip options-keepalive on the dial-peer.

```
dial-peer voice 1000 voip
 no voice-class sip options-keepalive profile 1
```

3. Downgrade to an earlier version. This issue was introduced after the commitment of Cisco bug ID CSCvx92872.

This issue is documented on Cisco bug ID CSCvz80171 .

Fix is available from 16.12.8/17.3.6/17.6.3/17.7.1/17.8.1

### Revision History

4.0

24-Jul-2025

Updated Formatting. Recertification

3.0

07-Aug-2024

Updated Title, Introduction, Branding Requirements, and Formatting. Bolded commands and took out single quotes.

2.0

12-Jun-2023

Updated tech content to make current.
Updated Title, Introduction, Branding Requirements, and Formatting.

1.0

09-May-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 4.0 | 24-Jul-2025 | Updated Formatting. Recertification |
| 3.0 | 07-Aug-2024 | Updated Title, Introduction, Branding Requirements, and Formatting. Bolded commands and took out single quotes. |
| 2.0 | 12-Jun-2023 | Updated tech content to make current.
Updated Title, Introduction, Branding Requirements, and Formatting. |
| 1.0 | 09-May-2022 | Initial Release |