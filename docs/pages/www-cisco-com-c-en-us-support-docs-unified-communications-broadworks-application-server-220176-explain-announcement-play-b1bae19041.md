---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-application-server-220176-explain-announcement-play-b1bae19041
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks-application-server/220176-explain-announcement-playback-mechanism.html
retrieved_at: 2026-09-07T13:03:02.442115+00:00
---

Explain Announcement Playback Mechanism in BroadWorks

# Explain Announcement Playback Mechanism in BroadWorks

### Download Options

Updated: January 31, 2023

Document ID: 220176

Contents

## Contents

## Introduction

This document describes how BroadWorks Application Server (AS) interacts with Media Server (MS) for digit collection and announcement playback.

.

## Background Information

The announcements are commonly used during call handling. For example, it can be used to prompt for digit collection (Enter your PIN number followed by pound), or to inform caller about call failure (Your call cannot be completed as dialed). In BroadWorks solution, Media Server is responsible for playback of announcement, however, media files are stored in Application Server. It is Application Server's responsibility to instruct Media Server on what file is to be played. Similarly, MS can extract user input from audio stream so that AS can make proper call handling actions.

Announcement files are stored in this location of AS server: /usr/local/broadworks/apps/MediaFiles_ <SW_version> /sysprompts/ <language code> /. For example, US English announcements in AS R24 are located in /usr/local/broadworks/apps/MediaFiles_24.0_1.944/sysprompts/en directory. In Session Initiation Protocol (SIP) messages /usr/local/broadworks/apps/MediaFiles_24.0_1.944/sysprompts/en/ location is mapped to https://<AS_addres>/media/en/ .

You can read more about announcements available in Broadworks in Cisco BroadWorks Announcement Guide.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- SIP signaling.

- Basic Auto Attendant configuration in BroadWorks.

### Components Used

The information in this document is based on these software and hardware versions:

- AS version: R24

- MS version: RI_2022.08

However, behavior for other software versions is similar.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Network Topology and Call Flow

For simplicity, basic call scenario is used in this document:

- Softphone application is registered directly to AS.

- User (with extension 2011) dials into Auto Attendant (with extension 2010) and presses digit 5 . This user input triggers call disconnection as shown in this screencapture:

- User and Auto Attendant are in the same group.

## Explanation of SIP Message Flow

Note : Only relevant SIP messages are listed for clarity.

User dials 2010 and softphone sends Invite message to AS:

```
2023.01.26 16:51:41:106 CET | Info       | Sip | Call Half Input Adapter 5 | 2966060 | +15403362011 | callhalf-58591:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 1111 SIP Bytes IN from 10.61.205.219:58300
INVITE sip:2010@mleus.lab SIP/2.0
Via: SIP/2.0/UDP 10.61.205.219:58300;rport;branch=z9hG4bKPjgINPvPUvoBT57iTOBPsgCfEqE5GX1aj7
Max-Forwards: 70
From: "Marek Leus" <sip:5403362011@mleus.lab>;tag=6fU.VlLrWc6WI3JU8jWKS.25yeoWEhpc
To: sip:2010@mleus.lab
Contact: "Marek Leus" <sip:5403362011@10.61.205.219:58300;ob>
Call-ID: dTUVBWON9UjmftpGCOoJzhLfbajBm11C
CSeq: 6492 INVITE
Route: <sip:10.48.93.126;lr>
Allow: PRACK, INVITE, ACK, BYE, CANCEL, UPDATE, INFO, SUBSCRIBE, NOTIFY, REFER, MESSAGE, OPTIONS
Supported: replaces, 100rel, norefersub
User-Agent: Telephone 1.6
Content-Type: application/sdp
Content-Length:   480

v=0
o=- 3883737105 3883737105 IN IP4 10.61.205.219
s=pjmedia
b=AS:117
t=0 0
a=X-nat:0
m=audio 4012 RTP/AVP 96 9 8 0 101 102
c=IN IP4 10.61.205.219
b=TIAS:96000
a=rtcp:4013 IN IP4 10.61.205.219
a=sendrecv
a=rtpmap:96 opus/48000/2
a=fmtp:96 useinbandfec=1
a=rtpmap:9 G722/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/48000
a=fmtp:101 0-16
a=rtpmap:102 telephone-event/8000
a=fmtp:102 0-16
a=ssrc:2039250127 cname:43ec7f3b5b951d53
```

Since extension 2010 belongs to Auto Attendant, AS extends call to MS:

```
2023.01.26 16:51:41:117 CET | Info       | Sip | Sip EncodeQ 0 | 2966113 | +15403362010 | callhalf-58599:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 1044 SIP Bytes OUT to 10.48.93.18:5060
INVITE sip:ivr@10.48.93.18 SIP/2.0
Via:SIP/2.0/UDP 10.48.93.126;branch=z9hG4bKBroadWorks.-iom24c-10.48.93.18V5060-0-929269663-1018158145-1674748301117-
From:<sip:+15403362011@10.48.93.126;user=phone>;tag=1018158145-1674748301117-
To:<sip:ivr@10.48.93.18>
Call-ID:BW165141117260123-861893333@10.48.93.126
CSeq:929269663 INVITE
Contact:<sip:10.48.93.126:5060>
X-BroadWorks-Correlation-Info:7492cbd3-b8a1-4c10-a543-b01f275be0b0
Allow:ACK,BYE,CANCEL,INFO,INVITE,OPTIONS,PRACK,REFER,NOTIFY
Supported:
Max-Forwards:10
Content-Type:application/sdp
Content-Length:469

v=0
o=BroadWorks 14605 1 IN IP4 10.61.205.219
s=-
b=AS:117
t=0 0
a=X-nat:0
m=audio 4012 RTP/AVP 96 9 8 0 101 102
c=IN IP4 10.61.205.219
b=TIAS:96000
a=rtcp:4013 IN IP4 10.61.205.219
a=sendrecv
a=rtpmap:96 opus/48000/2
a=fmtp:96 useinbandfec=1
a=rtpmap:9 G722/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/48000
a=fmtp:101 0-16
a=rtpmap:102 telephone-event/8000
a=fmtp:102 0-16
a=ssrc:2039250127 cname:43ec7f3b5b951d53
```

Call is answered by MS:

```
2023.01.26 16:51:41:128 CET | Info       | SipMedia | Call Half Input Adapter 2 | 2966114 | +15403362010 | callhalf-58599:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 673 SIP Bytes IN from 10.48.93.18:5060
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.48.93.126;branch=z9hG4bKBroadWorks.-iom24c-10.48.93.18V5060-0-929269663-1018158145-1674748301117-
From: <sip:+15403362011@10.48.93.126;user=phone>;tag=1018158145-1674748301117-
To: <sip:ivr@10.48.93.18>;tag=213817675
Call-ID: BW165141117260123-861893333@10.48.93.126
CSeq: 929269663 INVITE
Contact: <sip:10.48.93.18:5060>
Content-Type: application/sdp
Allow: INVITE, ACK, BYE, INFO, OPTIONS, CANCEL
Content-Length:   205

v=0
o=BroadWks 20 0 IN IP4 10.48.93.18
s=Media Server SDP
t=0 0
m=audio 10234 RTP/AVP 8 102
c=IN IP4 10.48.93.18
a=rtpmap:8 PCMA/8000
a=rtpmap:102 telephone-event/8000
a=fmtp:102 0-15
a=ptime:20
```

AS extends 200 OK message to the softphone:

```
2023.01.26 16:51:41:132 CET | Info       | Sip | Sip EncodeQ 1 | 2966146 | +15403362011 | callhalf-58591:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 864 SIP Bytes OUT to 10.61.205.219:58300
SIP/2.0 200 OK
Via:SIP/2.0/UDP 10.61.205.219:58300;branch=z9hG4bKPjgINPvPUvoBT57iTOBPsgCfEqE5GX1aj7;rport
From:"Marek Leus"<sip:5403362011@mleus.lab>;tag=6fU.VlLrWc6WI3JU8jWKS.25yeoWEhpc
To:<sip:2010@mleus.lab>;tag=749498253-1674748301131
Call-ID:dTUVBWON9UjmftpGCOoJzhLfbajBm11C
CSeq:6492 INVITE
Supported:
Contact:<sip:10.48.93.126:5060>
P-Asserted-Identity:"GroupB1 AA"<sip:2010@10.48.93.126;user=phone>
Privacy:none
Call-Info:<sip:10.48.93.126>;appearance-index=1
Allow:ACK,BYE,CANCEL,INFO,INVITE,OPTIONS,PRACK,REFER,NOTIFY,UPDATE
Accept:application/media_control+xml,application/sdp,multipart/mixed
Content-Type:application/sdp
Content-Length:195

v=0
o=BroadWorks 14606 1 IN IP4 10.48.93.18
s=-
t=0 0
m=audio 10234 RTP/AVP 8 102
c=IN IP4 10.48.93.18
a=rtpmap:8 PCMA/8000
a=rtpmap:102 telephone-event/8000
a=fmtp:102 0-15
a=ptime:20​
```

At this point, direct two way audio stream is established between softphone and MS; G711a codec and inbound DTMF are negotiated for this call. SIP signalling is still handled by AS.

AS instructs MS to play default Auto Attendant greetings (AAdefaultBusinessHoursGreeting.wav) and to collect digits (only digits from 0 to 5 are allowed as per Auto Attendant menu configuration):

```
2023.01.26 16:51:41:248 CET | Info       | Sip | Sip EncodeQ 0 | 2966172 | +15403362010 | callhalf-58599:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 934 SIP Bytes OUT to 10.48.93.18:5060
INFO sip:10.48.93.18:5060 SIP/2.0
Via:SIP/2.0/UDP 10.48.93.126;branch=z9hG4bKBroadWorks.-iom24c-10.48.93.18V5060-0-929269664-1018158145-1674748301117-
From:<sip:+15403362011@10.48.93.126;user=phone>;tag=1018158145-1674748301117-
To:<sip:ivr@10.48.93.18>;tag=213817675
Call-ID:BW165141117260123-861893333@10.48.93.126
CSeq:929269664 INFO
Contact:<sip:10.48.93.126:5060>
Max-Forwards:10
Content-Type:application/mediaservercontrol+xml
Content-Length:470

<?xml version="1.0" encoding="utf-8"?>
<MediaServerControl version="1.0-bw">
 <request>
  <playcollect
      cleardigits="no"
      escapekey=""
      firstdigittimer="10000"
      interdigittimer="2000"
      returnkey="">
   <prompt>
    <audio url="https://10.48.93.126/media/en/AAdefaultBusinessHoursGreeting.wav"/>
   </prompt>
   <regex
       type="mgcpdigitmap"
       value="(0|1|2|3|4|5)"/>
  </playcollect>
 </request>
</MediaServerControl>
```

During greetings, user presses digit 5 . It is transmitted within audio stream, so MS extracts digit from audio and sends it to AS in Info message:

```
2023.01.26 16:51:43:878 CET | Info       | SipMedia | Call Half Input Adapter 2 | 2966183 | +15403362010 | callhalf-58599:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 703 SIP Bytes IN from 10.48.93.18:5060
INFO sip:10.48.93.126:5060 SIP/2.0
Via: SIP/2.0/UDP 10.48.93.18:5060;branch=z9hG4bK-BroadWorks-MS-325794538
From: <sip:ivr@10.48.93.18>;tag=213817675
To: <sip:+15403362011@10.48.93.126;user=phone>;tag=1018158145-1674748301117-
Call-ID: BW165141117260123-861893333@10.48.93.126
CSeq: 2037464779 INFO
Content-Type: application/mediaservercontrol+xml
Max-Forwards: 70
Content-Length:   305

<?xml version="1.0" encoding="utf-8"?>
  <MediaServerControl version="1.0">
    <response
              request="playcollect"
              code="200"
              text="OK"
              reason="match"
              digits="5"
              playduration="2620"
    />
  </MediaServerControl>
```

Auto Attendant is configured to disconnect call when digit 5 is received. In order to make it more user friendly, it instructs MS to play "Thank you for calling" message first:

```
2023.01.26 16:51:43:880 CET | Info       | Sip | Sip EncodeQ 0 | 2966197 | +15403362010 | callhalf-58599:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 712 SIP Bytes OUT to 10.48.93.18:5060
INFO sip:10.48.93.18:5060 SIP/2.0
Via:SIP/2.0/UDP 10.48.93.126;branch=z9hG4bKBroadWorks.-iom24c-10.48.93.18V5060-0-929269665-1018158145-1674748301117-
From:<sip:+15403362011@10.48.93.126;user=phone>;tag=1018158145-1674748301117-
To:<sip:ivr@10.48.93.18>;tag=213817675
Call-ID:BW165141117260123-861893333@10.48.93.126
CSeq:929269665 INFO
Contact:<sip:10.48.93.126:5060>
Max-Forwards:10
Content-Type:application/mediaservercontrol+xml
Content-Length:248

<?xml version="1.0" encoding="utf-8"?>
<MediaServerControl version="1.0-bw">
 <request>
  <play>
   <prompt>
    <audio url="https://10.48.93.126/media/en/ThankYouForCalling.wav"/>
   </prompt>
  </play>
 </request>
</MediaServerControl>
```

MS informs AS that announcement playback is completed:

```
2023.01.26 16:51:45:294 CET | Info       | SipMedia | Call Half Input Adapter 2 | 2966207 | +15403362010 | callhalf-58599:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 632 SIP Bytes IN from 10.48.93.18:5060
INFO sip:10.48.93.126:5060 SIP/2.0
Via: SIP/2.0/UDP 10.48.93.18:5060;branch=z9hG4bK-BroadWorks-MS-30863660
From: <sip:ivr@10.48.93.18>;tag=213817675
To: <sip:+15403362011@10.48.93.126;user=phone>;tag=1018158145-1674748301117-
Call-ID: BW165141117260123-861893333@10.48.93.126
CSeq: 2037464780 INFO
Content-Type: application/mediaservercontrol+xml
Max-Forwards: 70
Content-Length:   235

<?xml version="1.0" encoding="utf-8"?>
  <MediaServerControl version="1.0">
    <response
              request="play"
              code="200"
              text="OK"
              reason="EOF"
    />
  </MediaServerControl>
```

When playback is completed, AS disconnects both call legs:

```
2023.01.26 16:51:45:296 CET | Info       | Sip | Sip EncodeQ 0 | 2966228 | +15403362010 | callhalf-58599:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 378 SIP Bytes OUT to 10.48.93.18:5060
BYE sip:10.48.93.18:5060 SIP/2.0
Via:SIP/2.0/UDP 10.48.93.126;branch=z9hG4bKBroadWorks.-iom24c-10.48.93.18V5060-0-929269666-1018158145-1674748301117-
From:<sip:+15403362011@10.48.93.126;user=phone>;tag=1018158145-1674748301117-
To:<sip:ivr@10.48.93.18>;tag=213817675
Call-ID:BW165141117260123-861893333@10.48.93.126
CSeq:929269666 BYE
Max-Forwards:10
Content-Length:0

2023.01.26 16:51:45:297 CET | Info       | Sip | Sip EncodeQ 1 | 2966238 | +15403362011 | callhalf-58591:0 | 
7492cbd3-b8a1-4c10-a543-b01f275be0b0

	udp 404 SIP Bytes OUT to 10.61.205.219:58300
BYE sip:5403362011@10.61.205.219:58300;ob SIP/2.0
Via:SIP/2.0/UDP 10.48.93.126;branch=z9hG4bKBroadWorks.-iom24c-10.61.205.219V58300-0-929269658-749498253-1674748301131
From:<sip:2010@mleus.lab>;tag=749498253-1674748301131
To:"Marek Leus"<sip:5403362011@mleus.lab>;tag=6fU.VlLrWc6WI3JU8jWKS.25yeoWEhpc
Call-ID:dTUVBWON9UjmftpGCOoJzhLfbajBm11C
CSeq:929269658 BYE
Max-Forwards:10
Content-Length:0
```

### Revision History

1.0

31-Jan-2023

Initial Release

### Contributed by Cisco Engineers

Marek Leus

Cisco TAC Engineer

### This Document Applies to These Products

- BroadWorks Application Server

- BroadWorks Media Server

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 31-Jan-2023 | Initial Release |