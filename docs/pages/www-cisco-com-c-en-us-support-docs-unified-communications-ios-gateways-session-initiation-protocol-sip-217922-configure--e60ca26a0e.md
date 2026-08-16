---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-ios-gateways-session-initiation-protocol-sip-217922-configure--e60ca26a0e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/ios-gateways-session-initiation-protocol-sip/217922-configure-sip-local-gateway-with-audio-c.html
retrieved_at: 2026-08-16T15:56:03.593806+00:00
---

Configure SIP Local Gateway with Audio Codecs Only for WebEx Calling

# Configure SIP Local Gateway with Audio Codecs Only for WebEx Calling

### Download Options

Updated: June 17, 2022

Document ID: 217922

Contents

## Contents

## Introduction

This document describes how to configure the Cisco Unified Border Element (CUBE) to not forward video codecs to the IP Telefony Service Provider (ITSP) when the ITSP informs that they are not supported as part of the INVITE message and the integration is done via Session Initiation Protocol (SIP).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco WebEx Calling (formerly BroadCloud)

- Cisco Unified Border Element (CUBE)

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Cloud Service Router 1000v

- Cisco Internetwork Operating System (Cisco IOS® XE) 17.03.04a

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

It is assumed that the integration between WebEx Calling, Local Gateway (LGW), and the ITSP is already up and functional.

## Configure

Step 1. Access to the configuration mode of the device:

```
device# configure terminal
```

Step 2. Navigate into the voice service voip configuration mode:

```
device(config)# voice service voip
```

Step 3. Navigate into the sip sub-configuration mode:

```
device(conf-voi-serv)# sip
```

Step 4. Enable the audio forced function in the sip sub-configuration mode:

```
device(conf-serv-sip)# audio forced
```

## Verify

To verify that no video codecs are sent to the ITSP, this debug can be enabled to check the INVITE offered to the ITSP:

```
device# debug ccsip messages
```

For example:

```
device# debug ccsip messages Received:
INVITE sip:123456@X.X.X.X:5061;transport=tls;dtg=XXXXX SIP/2.0
Via:SIP/2.0/TLS X.X.X.X:8934;
From:"Caller"<sip:987654@X.X.X.X;user=phone>;tag=1396950124-1643195813910-
To:<sip:123456@25105600.eu10.bcld.webex.com;user=phone>
Call-ID:SSE111653910260122-2086314723@X.X.X.X
CSeq:100 INVITE
Contact:<sip:X.X.X.X:8934;transport=tls>
P-Asserted-Identity:"Caller"<sip:123456@X.X.X.X;user=phone>
Privacy:none
Allow:ACK,BYE,CANCEL,INFO,INVITE,OPTIONS,PRACK,REFER,NOTIFY,UPDATE
Recv-Info:x-broadworks-client-session-info
X-Cisco-Region-ID:eu
X-Cisco-Org-Id:4b11285e-4879-4ed3-bfe7-331ea8affabe
X-BroadWorks-Correlation-Info:bfaffbad-7d4c-42ad-8a7f-7e74c1db8a1d
Accept:application/media_control+xml,application/sdp,multipart/mixed
Supported:
Max-Forwards:69
Session-ID:86acc1810080432799428436deb94327;remote=00000000000000000000000000000000
Content-Type:application/sdp
Content-Length:1241

v=0
o=Agent IN IP4 X.X.X.X
s=-
c=IN IP4 X.X.X.X
b=AS:4064
t=0 0
m=audio 36796 RTP/SAVP 99 9 8 0 18 101 108
b=TIAS:64000
a=rtpmap:99 opus/48000/2
a=fmtp:99 maxplaybackrate=16000;sprop-maxcapturerate=16000;maxaveragebitrate=64000;stereo=0;sprop-stereo=0;usedtx=0
a=rtpmap:9 G722/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:0 PCMU/8000
a=rtpmap:18 G729/8000
a=fmtp:18 annexb=no
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=rtpmap:108 telephone-event/48000
a=fmtp:108 0-15
a=ptime:20
a=sendrecv
a=crypto:1 AES_CM_128_HMAC_SHA1_80 inline:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
a=video 36840 RTP/SAVP 112 111 110
b=TIAS:4000000
a=rtpmap:112 H264/90000
a=fmtp:112 profile-level-id=640c16;packetization-mode=1;max-fs=3600;max-mbps=108000
a=rtpmap:111 H264/90000
a=fmtp:111 profile-level-id=428016;packetization-mode=1;max-fs=3600;max-mbps=108000
a=rtpmap:110 H264/90000
a=fmtp:110 profile-level-id=428016;packetization-mode=0;max-fs=3600;max-mbps=108000
a=imageattr:* recv [x=800,y=480,q=0.60] [x=1280,y=720,q=0.50]
a=rtcp-fb:* nack pli
a=rtcp-fb:* ccm fir
a=rtcp-fb:* ccm tmmbr
a=sendrecv
a=crypto:1 AES_CM_128_HMAC_SHA1_80 inline:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Sent:
INVITE sip:123456@X.X.X.X:5061;transport=tls;dtg=XXXXX SIP/2.0
Via:SIP/2.0/UDP X.X.X.X:8934;
From:"Caller"<sip:987654@X.X.X.X>;tag=AC42468-22E3
To:<sip:123456@25105600.eu10.bcld.webex.com>;tag=soos4o7b
Call-ID:726BDDE6-7DCE11EC-BC5BC09B-9E9BA404@X.X.X.X
CSeq:100 INVITE
Contact:<sip:X.X.X.X:8934;transport=udp>
P-Asserted-Identity:"Caller"<sip:123456@X.X.X.X;user=phone>
Privacy:none
Allow:ACK,BYE,CANCEL,INFO,INVITE,OPTIONS,PRACK,REFER,NOTIFY,UPDATE
Accept:application/media_control+xml,application/sdp,multipart/mixed
Supported:
Max-Forwards:69
Session-ID:86acc1810080432799428436deb94327;remote=00000000000000000000000000000000
Content-Type:application/sdp
Content-Length:1241

v=0
o=Agent IN IP4 X.X.X.X
s=-
c=IN IP4 X.X.X.X
b=AS:4064
t=0 0
m=audio 36796 RTP/SAVP 99 9 8 0 18 101 108
b=TIAS:64000
a=rtpmap:99 opus/48000/2
a=fmtp:99 maxplaybackrate=16000;sprop-maxcapturerate=16000;maxaveragebitrate=64000;stereo=0;sprop-stereo=0;usedtx=0
a=rtpmap:9 G722/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:0 PCMU/8000
a=rtpmap:18 G729/8000
a=fmtp:18 annexb=no
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=rtpmap:108 telephone-event/48000
a=fmtp:108 0-15
a=ptime:20
a=sendrecv
```

## Troubleshoot

There is currently no specific information available for this configuration.

### Revision History

1.0

17-Jun-2022

Initial Release

### Contributed by Cisco Engineers

Leonardo Correa

Cisco TAC Engineer

### This Document Applies to These Products

- IOS Gateways with Session Initiation Protocol (SIP)

- Unified Border Element

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Jun-2022 | Initial Release |