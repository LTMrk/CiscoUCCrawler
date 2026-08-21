---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-212429-configure-jabber-to-use-custom-audio-and-a1249a1306
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/212429-configure-jabber-to-use-custom-audio-and.html
retrieved_at: 2026-08-21T06:59:54.333576+00:00
---

Configure Jabber to Use Custom Audio and Video Port Range on CUCM 11.5.1

# Configure Jabber to Use Custom Audio and Video Port Range on CUCM 11.5.1

### Download Options

Updated: November 10, 2017

Document ID: 212429

Contents

## Contents

## Introduction

This document describes the procedure to configure Cisco Jabber to use custom audio and video port range on Cisco Unified Communications Manager (CUCM) 11.5.1.

Contributed by Domhnall MacCormac, Cisco TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of:

- Cisco Jabber

- Cisco Unified Communication Manager (CUCM)

### Components Used

The information in this document is based on these software versions:

- Cisco Jabber for Windows 11.9.x

- Cisco Unified Communications Manager 11.5.x

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure you understand the potential impact of any command.

## Configure

You can create a new SIP Profile or simply copy the Standard SIP Profile and modify the port range on your copied profile as follows:

- Navigate to Device > Device Settings > SIP Profile on the Cisco Unified CM Administration page

- Click on Find button to display all SIP profiles

- Click on the Standard SIP Profile and click on the Copy button

- Scroll down to the Media Port Ranges field and click on the radio button titled Separate Port Ranges for Audio and Video

- Specify the Start Audio Port, the Stop Audio Port, the Start Video Port and the Stop Video Port

Note : The Start port needs to be an even number and the Stop port needs to be odd number

## Verify

Place a call from Jabber and confirm in the Jabber log that the ports specified in the outbound INVITE Session Description Protocol (SDP) message falls within the configured port range.

```
CSeq: 101 INVITE User-Agent: Cisco-CSF Contact: <sip:1553c615-14d6-39e8-0399-af6fdd5ee447@10.66.87.207:50268;transport=tcp>;+u.sip!devicename.ccm.cisco.com="CSFwstest1";video;bfcp Expires: 180 Accept: application/sdp Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO Remote-Party-ID: "1000" <sip:1000@dmaccorm-ucmpub.myothertestdomain.net>;party=calling;id-type=subscriber;privacy=off;screen=yes Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1 Allow-Events: kpml,dialog Recv-Info: conference Recv-Info: x-cisco-conference Content-Length: 2246 Content-Type: application/sdp Content-Disposition: session;handling=optional v=0 o=Cisco-SIPUA 20391 0 IN IP4 10.66.87.207 s=SIP Call b=AS:4000 t=0 0 a=cisco-mari:v1 a=cisco-mari-rate m=audio 16390 RTP/AVP 114 9 104 105 0 8 18 111 101 c=IN IP4 10.66.87.207 a=rtpmap:114 opus/48000/2 a=rtpmap:9 G722/8000 a=rtpmap:104 G7221/16000 a=fmtp:104 bitrate=32000 a=rtpmap:105 G7221/16000 a=fmtp:105 bitrate=24000 a=rtpmap:0 PCMU/8000 a=rtpmap:8 PCMA/8000 a=rtpmap:18 G729/8000 a=fmtp:18 annexb=no a=rtpmap:111 x-ulpfecuc/8000 a=extmap:14/sendrecv http://protocols.cisco.com/timestamp#100us a=fmtp:111 max_esel=1420;m=8;max_n=32;FEC_ORDER=FEC_SRTP a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-15 a=sendrecv m=video 16398 RTP/AVP 126 97 111 c=IN IP4 10.66.87.207 b=TIAS:4000000 a=rtpmap:126 H264/90000 a=fmtp:126 profile-level-id=42E01F;packetization-mode=1;level-asymmetry-allowed=1;max-fs=3601;max-rcmd-nalu-size=32000 a=imageattr:126 recv [x=[32:1:1280],y=[18:1:720],par=1.7778,q=1.00] a=content:main a=label:11 a=rtpmap:97 H264/90000 a=fmtp:97 profile-level-id=42E01F;packetization-mode=0;level-asymmetry-allowed=1;max-fs=3601 a=imageattr:97 recv [x=[32:1:1280],y=[18:1:720],par=1.7778,q=1.00] a=rtpmap:111 x-ulpfecuc/8000 a=extmap:14/sendrecv http://protocols.cisco.com/timestamp#100us a=fmtp:111 max_esel=1420;m=8;max_n=32;FEC_ORDER=FEC_SRTP a=rtcp-fb:* ccm fir a=rtcp-fb:* ccm tmmbr a=rtcp-fb:* nack pli a=recvonly m=video 16394 RTP/AVP 126 97 111 c=IN IP4 10.66.87.207 b=TIAS:4000000 a=rtpmap:126 H264/90000 a=fmtp:126 profile-level-id=42E01F;packetization-mode=1;level-asymmetry-allowed=1;max-fs=3601;max-rcmd-nalu-size=32000 a=content:slides a=label:12 a=rtpmap:97 H264/90000 a=fmtp:97 profile-level-id=42E01F;packetization-mode=0;level-asymmetry-allowed=1;max-fs=3601 a=rtpmap:111 x-ulpfecuc/8000 a=extmap:14/sendrecv http://protocols.cisco.com/timestamp#100us a=fmtp:111 max_esel=1420;m=8;max_n=32;FEC_ORDER=FEC_SRTP a=rtcp-fb:* ccm fir a=rtcp-fb:* ccm tmmbr a=rtcp-fb:* nack pli a=sendrecv m=application 5904 UDP/BFCP * c=IN IP4 10.66.87.207 a=floorctrl:c-s a=confid:3 a=floorid:2 mstrm:12 a=userid:3 a=setup:actpass a=connection:new a=sendrecv m=application 39878 RTP/AVP 125 c=IN IP4 10.66.87.207 a=rtpmap:125 H224/4800 a=rtcp:39879 a=sendrecv
```

## Troubleshoot

If the port specified in the INVITE SDP is not within the configured range, review the jabber.log file after a restart of the client to determine that the custom port range has been applied.

```
INFO [0x0000016c] [ource\cpve\src\main\engineimpl.cpp(1226)] [cpve] [CSF::media::rtp::EngineImpl::setPortRange] - Entering [mediaType=0, startPort=16384, endPort=16393]. INFO [0x0000016c] [ource\cpve\src\main\engineimpl.cpp(1274)] [cpve] [CSF::media::rtp::EngineImpl::setPortRange] - Exiting. Returning true : port range set DEBUG [0x0000016c] [rc\media\cpve\CpveVideoProvider.cpp(230)] [csf.ecc.media.term] [csf::ecc::CpveVideoProvider::setPortRange] - setPortRange(16394, 16403) DEBUG [0x0000016c] [rc\media\cpve\CpveVideoProvider.cpp(230)] [csf.ecc.media.term] [csf::ecc::CpveVideoProvider::setPortRange] - setPortRange(16394, 16403) INFO [0x0000016c] [ource\cpve\src\main\engineimpl.cpp(1226)] [cpve] [CSF::media::rtp::EngineImpl::setPortRange] - Entering [mediaType=1, startPort=16394, endPort=16403]. INFO [0x0000016c] [ource\cpve\src\main\engineimpl.cpp(1274)] [cpve] [CSF::media::rtp::EngineImpl::setPortRange] - Exiting. Returning true : port range set
```

If the custom port range is not applied as per above log snippet, review the Jabber device configuration XML file on the TFTP server with a web browser (http:// <TFTP_SERVER_ADDRESS> :6970/ <DEVICE_NAME> .cnf.xml).

```
<startMediaPort>16384</startMediaPort>
<stopMediaPort>16393</stopMediaPort>
<startVideoPort>16394</startVideoPort>
<stopVideoPort>16403</stopVideoPort>
```

### Contributed by Cisco Engineers

Domhnall MacCormac

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber for Windows

- Unified Communications Manager (CallManager)