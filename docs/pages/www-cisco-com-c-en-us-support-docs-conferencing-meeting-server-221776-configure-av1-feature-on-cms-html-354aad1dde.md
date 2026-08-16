---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-221776-configure-av1-feature-on-cms-html-354aad1dde
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/221776-configure-av1-feature-on-cms.html
retrieved_at: 2026-08-16T14:21:07.634726+00:00
---

Configure CMS AV1 Feature

# Configure CMS AV1 Feature

Log in to Save Content

### Download Options

Updated: April 8, 2024

Document ID: 221776

Contents

## Contents

## Introduction

This document describes how to enable the AOMedia Video 1 (AV1) codec on the Cisco Meeting Server (CMS).

Note : This AV1 is a beta feature on CMS 3.9.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of the CMS configuration.

### Components Used

The information in this document is based on these software and hardware versions:

- CMS version 3.9 service Callbridge

- Chrome browser 122.0.6261.112

- Firefox browser 123.0.1 (20240304104836)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

1. This is an example of the default AV1 codec status on CMS logs:

```
2024-03-05T16:50:25.736 user.info cms01 host:server: INFO : AV1 Video Codec Enabled for Content: 0
```

2. Enable AV1 codec on the Callbridge of CMS through the Secure Shell (SSH) command callbridge av1 enable .

```
cms01> callbridge av1 enable
```

This is an example of enabling AV1 on CMS logs:

```
2024-03-06T09:34:45.395 local0.info cms01 cli: User admin from 10.140.249.233:63290 issued command < callbridge av1 enable>: permission granted
```

3. Restart Callbridge service on CMS through SSH command in order to activate the new feature AV1 codec.

```
cms01> callbridge restart
```

4. Verify the Callbridge status from both the CMS SSH command line and CMS logs in order to confirm AV1 Video Codec is enabled .

This is an example of CMS SSH command line status:

```
cms01> callbridge
Listening interfaces  : a
Preferred interface   : none
Key file              : cms.key
Certificate file      : cms.cer
Address               : none
CA Bundle file        : root.cer
C2W trusted certs                   : cms.cer
Callbridge cluster trusted certs    : cms.cer
Callbridge trust branding certs     : none
UCM trusted certs         : cucmtomcat.cer
UCM verification mode     : enabled
IMPS trusted certs        : impcup.cer
IMPS verification mode    : enabled
WC3 JWT Expiry in hours   : 24 AV1 Video Codec : enabled
```

This is an example of enabling AV1 codec status on CMS logs:

```
2024-03-06T09:35:42.003 user.info cms01 host:server: INFO : AV1 Video Codec Enabled for Content: 1
```

Note : AV1 codec must be enabled on all Callbridge servers in the CMS cluster.

## Verify

1. The media health statistics of the content presenter show the content negotiate codec is AV1 on the Chrome browser.

Presenter content codec is AV1 on chrome

2. The media health statistics of the content receiver show the content negotiate codec is AV1 on Chrome browser when receiving the content from CMS servers.

Receiver content codec is AV1 on chrome

3. If AV1 is enabled on CMS but browsers do not support AV1, content transmission between CMS and browser picks up the browser-supported codec.

This example shows the CMS and Firefox browser content negotiation codec is H.264.

Receiver content codec is H.264 on firefox

## Troubleshooting

1. From CMS logs it can be seen that the presenter started sharing content:

```
2024-03-06  12:36:05.737  Info     call 49: new video presentation request from user "guest3577572234"
2024-03-06  12:36:05.737  Info     call 49: becoming floor
```

2. From presenter webrtc logs on Chrome browser, you can see that CMS supports AV1 codec in Session Description Protocol (SDP) message and the content sharing codec is AV1 .

You can collect webrtc logs through chrome://webrtc-internals/ on Chrome browser.

This is an example of the CMS SDP message in webrtc logs.

```
v=0 (11 more lines) o=Acano 0 0 IN IP4 10.124.56.212 s=-
c=IN IP4 10.124.56.212
b=CT:6000
t=0 0
a=setup:active
a=msid-semantic: WMS ef86aaf0-f732-40ca-a65a-484dd196864d 494ba500-d708-4048-80f3-2820b1503423
a=ice-ufrag:CONP
a=ice-pwd:n++OtYUn97Vt8rkqwhUhPv
a=fingerprint:sha-256 2B:84:FF:34:56:54:55:AC:3D:57:D0:27:B6:E3:F5:4F:CF:00:1B:AC:8C:9F:55:02:93:F8:45:CA:E9:58:B7:21
a=group:BUNDLE 0 1 2 m=audio 35648 RTP/SAVPF 111 9 0 8 13 126 (16 more lines) mid=0 a=rtcp-mux
a=sendrecv
a=extmap:1 urn:ietf:params:rtp-hdrext:ssrc-audio-level
a=candidate:1 1 udp 2130706431 10.124.56.212 35648 typ host 
a=candidate:1 2 udp 2130706431 10.124.56.212 35648 typ host 
a=rtpmap:111 opus/48000/2
a=fmtp:111 useinbandfec=1
a=rtpmap:9 G722/8000
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:13 CN/8000
a=rtpmap:126 telephone-event/8000
a=fmtp:126 0-15
a=ssrc:849856969 cname:8db99900-7685-4b58-8df7-f6254f6679dc
a=ssrc:849856969 msid:ef86aaf0-f732-40ca-a65a-484dd196864d main_audio_track
a=mid:0 m=video 35648 RTP/SAVPF 104 102 45 96 (24 more lines) mid=1 b=TIAS:6000000
a=rtcp-mux
a=content:main
a=sendrecv
a=rtcp-fb:* nack
a=rtcp-fb:* nack pli
a=rtcp-fb:* ccm fir
a=rtcp-fb:* goog-remb
a=extmap:2 http://www.example.com/experiments/rtp-hdrext/abs-send-time
a=candidate:1 1 udp 2130706431 10.124.56.212 35648 typ host 
a=candidate:1 2 udp 2130706431 10.124.56.212 35648 typ host 
a=rtpmap:104 H264/90000
a=fmtp:104 profile-level-id=428015;max-mbps=244800;max-fs=8160;max-br=5000;max-fps=6000;x-google-start-bitrate=6000;x-google-max-bitrate=6000
a=rtpmap:102 H264/90000
a=fmtp:102 profile-level-id=428015;max-mbps=244800;max-fs=8160;max-br=5000;max-fps=6000;packetization-mode=1;x-google-start-bitrate=6000;x-google-max-bitrate=6000 a=rtpmap:45 AV1/90000 a=fmtp:45 profile=0;level-idx=31
a=rtpmap:96 VP8/90000
a=fmtp:96 max-fs=8160;max-fr=30
a=ssrc:2217027374 cname:8db99900-7685-4b58-8df7-f6254f6679dc
a=ssrc:2217027374 msid:ef86aaf0-f732-40ca-a65a-484dd196864d main_video_track
a=ssrc:2217027374 label:main
a=label:11
a=mid:1 m=video 35648 RTP/SAVPF 45 104 105 102 103 96 97 (42 more lines) mid=2 b=TIAS:6000000
a=rtcp-mux a=content:slides a=sendonly
a=extmap:2/sendrecv http://www.example.com/experiments/rtp-hdrext/abs-send-time
a=candidate:1 1 udp 2130706431 10.124.56.212 35648 typ host 
a=candidate:1 2 udp 2130706431 10.124.56.212 35648 typ host a=rtpmap:45 AV1/90000 a=fmtp:45 profile=0;level-idx=31
a=rtcp-fb:45 nack
a=rtcp-fb:45 nack pli
a=rtcp-fb:45 ccm fir
a=rtcp-fb:45 goog-remb
a=rtpmap:104 H264/90000
a=fmtp:104 profile-level-id=428015;max-mbps=244800;max-fs=8160;max-br=5000;max-fps=6000;x-google-start-bitrate=6000;x-google-max-bitrate=6000
a=rtcp-fb:104 nack
a=rtcp-fb:104 nack pli
a=rtcp-fb:104 ccm fir
a=rtcp-fb:104 goog-remb
a=rtpmap:105 rtx/90000
a=fmtp:105 apt=104
a=rtpmap:102 H264/90000
a=fmtp:102 profile-level-id=428015;max-mbps=244800;max-fs=8160;max-br=5000;max-fps=6000;packetization-mode=1;x-google-start-bitrate=6000;x-google-max-bitrate=6000
a=rtcp-fb:102 nack
a=rtcp-fb:102 nack pli
a=rtcp-fb:102 ccm fir
a=rtcp-fb:102 goog-remb
a=rtpmap:103 rtx/90000
a=fmtp:103 apt=102
a=rtpmap:96 VP8/90000
a=fmtp:96 max-fs=8160;max-fr=30
a=rtcp-fb:96 nack
a=rtcp-fb:96 nack pli
a=rtcp-fb:96 ccm fir
a=rtcp-fb:96 goog-remb
a=rtpmap:97 rtx/90000
a=fmtp:97 apt=96
a=ssrc:910559423 cname:8db99900-7685-4b58-8df7-f6254f6679dc
a=ssrc:910559423 msid:494ba500-d708-4048-80f3-2820b1503423 presentation_video_track
a=ssrc:910559423 label:slides
a=label:12
a=mid:2
```

This is an example of webrtc content sharing codec information.

```
outbound-rtp (kind=video, mid=2, ssrc=1277302382, scalabilityMode=L1T1, encoderImplementation=libaom, powerEfficientEncoder=false, [codec]=AV1 (45, level-idx=31;profile=0), id=OT01V1277302382)
Statistics OT01V1277302382
timestamp	3/6/2024, 1:15:33 PM
ssrc	1277302382
kind	video
transportId	T01
codecId	COT01_45_level-idx=31;profile=0 [codec] AV1 (45, level-idx=31;profile=0)
packetsSent	3964
[packetsSent/s]	48.982867749455345
bytesSent	145005
[bytesSent_in_bits/s]	399.860144893513
mediaSourceId	SV20
remoteId	RIV1277302382
mid	2
retransmittedPacketsSent	0
[retransmittedPacketsSent/s]	0
headerBytesSent	1027880
[headerBytesSent_in_bits/s]	105723.02230984485
retransmittedBytesSent	0
[retransmittedBytesSent_in_bits/s]	0
targetBitrate	500000
framesEncoded	151
[framesEncoded/s]	0.9996503622337826
keyFramesEncoded	1
totalEncodeTime	0.627
[totalEncodeTime/framesEncoded_in_ms]	2.0000000000000018
totalEncodedBytesTarget	0
[totalEncodedBytesTarget_in_bits/s]	0
frameWidth	1778
frameHeight	800
framesPerSecond	1
framesSent	151
[framesSent/s]	0.9996503622337826
hugeFramesSent	1
totalPacketSendDelay	1.6430509999999998
[totalPacketSendDelay/packetsSent_in_ms]	0
qualityLimitationReason	none
qualityLimitationDurations	{"bandwidth":0,"cpu":0,"none":87.68899999999999,"other":0}
qualityLimitationResolutionChanges	0 contentType screenshare encoderImplementation	libaom
firCount	0
pliCount	0
nackCount	0
qpSum	9208
[qpSum/framesEncoded]	40
active	true
powerEfficientEncoder	false
scalabilityMode	L1T1
```

## Related Information

- Cisco-Meeting-Server-and-web-app-Release-Notes-3-9

- Cisco Technical Support & Downloads

Note : Cisco does not guarantee that a beta feature transitions into a fully supported feature in the future. Beta features are subject to change based on feedback, and functionality can change or be removed in the future.

Note :

- This feature is not supported for SIP endpoints .

- AV1 transmission has been tested and qualified on Chrome browser only.

- If AV1 is enabled in the Meeting Server but the browsers do not support it, content transmission picks up the browser-supported codec.

- After enabling the Mainboard Management Processor (MMP) command, restart the Callbridge in order to ensure the change is applied.

### Revision History

1.0

08-Apr-2024

Initial Release

### Contributed by Cisco Engineers

Foster Song

Cisco TAC Engineer

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

### This Document Applies to These Products

- Meeting Server

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 08-Apr-2024 | Initial Release |