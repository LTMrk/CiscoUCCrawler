---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-ip-phone-7800-series-200903-troubleshoot-one-way-audio-issue--523fbd4eeb
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/ip-phone-7800-series/200903-Troubleshoot-One-Way-Audio-Issue-Using-C.html
retrieved_at: 2026-08-17T01:09:20.963185+00:00
---

Troubleshoot One Way Audio Issue Using CLI Debug Outputs from Cisco IP Phone 7800/8800 Series

# Troubleshoot One Way Audio Issue Using CLI Debug Outputs from Cisco IP Phone 7800/8800 Series

### Download Options

Updated: September 11, 2018

Document ID: 200903

Contents

## Contents

## Introduction

This document describes log analysis of the debugs generated in CLI for Cisco IP phone 7800/8800 series for one way audio issue.

## Troubleshoot Cisco Phone 7800/8800 Series One Way Audio Issues

When you troubleshoot one-way audio problem the very first task is to draw the topology and determine RTP media (Real-Time Protocol) path and devices that send and receive RTP streams. A particularly complex task is to figure out whether IP phone was sending and receiving the streams. The most common way is to collect a packet capture from Cisco IP phone as described in the respective article. But in most cases when the problem is intermittent it is challenging to determine the phone that will be affected by the one-way audio issue next time. In this article, an alternative method is used. It can be very useful especially when dealing with sporadic one-way audio issues.

### Capturing the Logs

Step 1. Enable SSH on the IP phone. Step 2. Optional step. Configure dumping the phone logs to Syslog server. As mentioned already, a one-way audio problem is usually intermittent. Having multiple phones affected requires to configure the option of dumping the logs to a remote Syslog server. In Cisco Unified Communications Manager (CUCM) enable the following parameters. Reset the phone. Step 3. Login to the phone's CLI via SSH protocol. Step 4. Enable phone logs.

```
DEBUG> settmask -p ms -t 0xfffff -b LOG_DEBUG DEBUG> debug lsm vcm fim fsm gsm debugs: fim fsm gsm lsm sip-state sip-messages sip-reg-state ccdefault vcm DEBUG> debug jvm SIPCC DEBUG> Successfully executed the command.
```

Step 5. Start dumping the logs.

```
DEBUG> sdump
```

Step 6. Cancel the log collection by resetting the phone.

### Call Details

```
Calling phone firmware: sip78xx.10-3-1-12

Calling phone ip address: 10.62.153.20

Calling phone number: 5035

 

Called phone ip address: 10.229.16.243

Called phone number: 2211

 

CUCM version: 11.0.1.20000-2

CUCM Publisher ip address: 10.48.47.143

CUCM Subscriber ip address:  10.48.47.136

CUBE: 10.62.150.10
```

### Signaling Analysis

Firstly there is a need to find the signaling for the call that has a one-way audio problem.

The easiest way is to use called number as a search parameter.

Note : In Cisco IP phone 7800/8800 series all sent and received SIP messages can be found with "sipio-sent" and "sipio-recv" search strings.

The phone sends an INVITE message towards CUCM Subscriber server. And receives standard replies. Call-ID record allows to track all related message for this particular call.

```
0611 DEB Dec 21 14:33:00.127717 JAVA-sipio-sent---> INVITE sip:2211@10.48.47.136;user=phone SIP/2.0^M
        Via: SIP/2.0/TCP 10.62.153.20:52464;branch=z9hG4bK2037857c^M
        From: "5035" <sip:5035@10.48.47.136>;tag=c80084aa872103164b6d6bb1-699aac4f^M
        To: <sip:2211@10.48.47.136>^M
        Call-ID: c80084aa-8721000b-302564ee-403d3d01@10.62.153.20^M
        Max-Forwards: 70^M
        Date: Wed, 21 Dec 2016 14:33:00 GMT^M
        CSeq: 101 INVITE^M
        User-Agent: Cisco-CP7821/10.3.1^M
        Contact: <sip:2fbf6265-bffc-4f99-b8b2-40dce7ed2d19@10.62.153.20:52464;transport=tcp>^M
        Expires: 180^M
        Accept: application/sdp^M
        Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO^M
        Remote-Party-ID: "5035" <sip:5035@10.48.47.136>;party=calling;id-type=subscriber;privacy=off;screen=yes^M
        Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1^M
        Allow-Events: kpml,dialog^M
        Content-Length: 348^M
        Content-Type: application/sdp^M
        Content-Disposition: session;handling=optional^M
        ^M
        v=0^M
        o=Cisco-SIPUA 7726 0 IN IP4 10.62.153.20^M
        s=SIP Call^M
        t=0 0^M
        m=audio 27986 RTP/AVP 9 0 8 116 18 101^M
        c=IN IP4 10.62.153.20^M
        a=rtpmap:9 G722/8000^M
        a=rtpmap:0 PCMU/8000^M
        a=rtpmap:8 PCMA/8000^M
        a=rtpmap:116 iLBC/8000^M
        a=fmtp:116 mode=20^M
        a=rtpmap:18 G729/8000^M
        a=fmtp:18 annexb=yes^M
        a=rtpmap:101 telephone-event/8000^M
        a=fmtp:101 0-15^M
        a=sendrecv^M

0650 DEB Dec 21 14:33:00.171483 JAVA-sipio-recv<--- SIP/2.0 100 Trying^M
0782 DEB Dec 21 14:33:00.249127 JAVA-sipio-recv<--- SIP/2.0 180 Ringing^M
```

In eight seconds called party answers the call and the audio streams are established. It is important to note down negotiated media addresses. Media addresses are negotiated in INVITE and 200 OK messages for early offer SIP mode, and in 200 OK followed by ACK for delayed offer mode.

```
1150 DEB Dec 21 14:33:08.179266 JAVA-sipio-recv<--- SIP/2.0 200 OK^M
        Via: SIP/2.0/TCP 10.62.153.20:52464;branch=z9hG4bK2037857c^M
        From: "5035" <sip:5035@10.48.47.136>;tag=c80084aa872103164b6d6bb1-699aac4f^M
        To: <sip:2211@10.48.47.136>;tag=59591~c6f18c49-d13e-4c97-aefc-039c35dcaca0-37698453^M
        Date: Wed, 21 Dec 2016 14:32:59 GMT^M
        Call-ID: c80084aa-8721000b-302564ee-403d3d01@10.62.153.20^M
        CSeq: 101 INVITE^M
        Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY^M
        Allow-Events: presence^M
        Supported: replaces^M
        Server: Cisco-CUCM11.0^M
        Call-Info: ; security= NotAuthenticated; orientation= to; gci= 2-6064; isVoip; call-instance= 1^M
        Send-Info: conference, x-cisco-conference^M
        Remote-Party-ID: <sip:2211@10.48.47.136>;party=called;screen=no;privacy=off^M
        Session-ID: f329a19bdd6e9960881d66e6bab59592;remote=7d416919fab94807bcc061c4baa59591^M
        Remote-Party-ID: <sip:2211@10.48.47.136;user=phone>;party=x-cisco-original-called;privacy=off^M
        Contact: <sip:2211@10.48.47.136:5060;transport=tcp>^M
        Content-Type: application/sdp^M
        Content-Length: 236^M
        ^M
        v=0^M
        o=CiscoSystemsCCM-SIP 59591 1 IN IP4 10.48.47.136^M
        s=SIP Call^M
        c=IN IP4 10.62.150.10^M
        b=TIAS:64000^M
        b=AS:64^M
        t=0 0^M
        m=audio 23672 RTP/AVP 0 101^M
        a=ptime:20^M
        a=rtpmap:0 PCMU/8000^M
        a=rtpmap:101 telephone-event/8000^M
        a=fmtp:101 0-15^M
```

Lastly, find the call termination message.

```
2081 DEB Dec 21 14:33:18.688956 JAVA-sipio-recv<--- BYE sip:2fbf6265-bffc-4f99-b8b2-40dce7ed2d19@10.62.153.20:52464;transport=tcp SIP/2.0^M
        Via: SIP/2.0/TCP 10.48.47.136:5060;branch=z9hG4bK17c47b18ed76^M
        From: <sip:2211@10.48.47.136>;tag=59591~c6f18c49-d13e-4c97-aefc-039c35dcaca0-37698453^M
        To: "5035" <sip:5035@10.48.47.136>;tag=c80084aa872103164b6d6bb1-699aac4f^M
        Date: Wed, 21 Dec 2016 14:33:07 GMT^M
        Call-ID: c80084aa-8721000b-302564ee-403d3d01@10.62.153.20^M
        User-Agent: Cisco-CUCM11.0^M
        Max-Forwards: 70^M
        CSeq: 101 BYE^M
        Reason: Q.850;cause=16^M
        Session-ID: f329a19bdd6e9960881d66e6bab59592;remote=7d416919fab94807bcc061c4baa59591^M
        Remote-Party-ID: <sip:2211@10.48.47.136;user=phone>;party=x-cisco-original-called;privacy=off^M
        Content-Length: 0^M
        ^M
```

### Media Stream Analysis

When analyzing any black box device pay attention to the timestamps especially with a relation to a call context.

Find confirmation that the transmission is not active yet.

```
0407 NOT Dec 21 14:33:00.082822 ms-RTCPMGR.rtcpm_getSr[A:17] TX stream state not connected [ingress=0][state=0]
1144 NOT Dec 21 14:33:08.152988 ms-RTCPMGR.rtcpm_getSr[A:17] TX stream state not connected [ingress=7][state=1]
```

Messages to update receiving (RX) audio streams parameters.

```
1380 NOT Dec 21 14:33:08.220957 ms-RTPSESSION.ms_updateRTPRxParam[A:17] UPDATE RX [mediaType(codec)=4][dynamicPayloadType=0][hootNumTalkers=0][dtmfPayloadType=101][pktperiod=20][security=0]
1481 INF Dec 21 14:33:08.282028 ms-RCVMGR.receiveManagerStartReceive[A:17] Start RX 5: syncId 5, codec 16, rtnCode 0
```

Messages that display information regarding transmitted (TX) audio stream.

```
1668 DEB Dec 21 14:33:08.380273 ms-RTPSESSION.startRTPSessionTx[A:17] enter
1670 DEB Dec 21 14:33:08.380395 ms-RTPMGR.rtpmgr_txStart[A:17] [streamId=7] enter
1673 INF Dec 21 14:33:08.380609 ms-MGRRTP.rtpTransmitStart[A:17] TX [CT=1][msPktSz=20][Ssrc=0xE322D7C2][Csrc=0x0][fTyp=0][SPF=80][FPP=2][pktSz=236][Buf=Y]
1674 INF Dec 21 14:33:08.380670 ms-MGRRTP.rtpTransmitStart[A:17] RFC2833: [PT=101][tsscale=8][pktPeriod=20][step=10][sizeof=4]

1771 NOT Dec 21 14:33:08.407650 ms-RTPSESSION.ms_startRTPSessionTx[A:17] START TX: [mediaType(codec)=4][pkt size=20][remote IPv4=10.62.150.10][rport=23672][groupid=8][callid=8]
```

Call termination can be found with ONHOOK state transition.

```
2113 NOT Dec 21 14:33:18.699974 JAVA-SIPCC-CC_API: 1/8, cc_int_onhook: GSM -> SIP: ONHOOK              

After the call is terminated RTP statistics will be displayed. From this message it is clear that the phone did not receive any packets, so the next step would be to enable packet captures on the CUBE. 
2121 NOT Dec 21 14:33:18.701225 ms-MS.statm_printDecoderStats[A:17] 
                [Rx Count=0][Rx Lost=0][Pkts Discarded=0][Rx Octets=0]
                [Avg Jitter=0][Max Jitter=0]
                [RFC2833=0]
                [CCR=0.0000][ICR=0.0000][MaxCR=0.0000][CS=0][SCS=0]

Encoder stats display that 514 packets were sent.

2124 NOT Dec 21 14:33:18.701897 ms-MS.statm_printEncoderStats[A:17] 
                [Tx Count=514][TX Octets=82240]
```

Tip : Call duration can be counted by dividing the number of transmitted packets on the packetization period. In the example 514 / 50 = 10.28 seconds.

## Related Information

- Troubleshoot Cisco Phone 7800/8800 Series Intermittent Registration Issues

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- IP Phone 7800 Series

- IP Phone 8800 Series