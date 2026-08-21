---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-213413-configure-and-troubleshoot-dual-screen-f-html-160b6ca02a
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/213413-configure-and-troubleshoot-dual-screen-f.html
retrieved_at: 2026-08-21T13:12:40.968657+00:00
---

Configure and Troubleshoot Dual Screen Feature

# Configure and Troubleshoot Dual Screen Feature

### Download Options

Updated: April 30, 2020

Document ID: 213413

Contents

## Contents

## Introduction

This document describes how to setup Dual Screen feature with Cisco Meeting Server (CMS) and Cisco Telepresence Endpoints.

## Prerequisites

### Requirements

Cisco reommends that you have a knowledge of these topics:

- Callbridge component must be configured on CMS

- CMS must be running version 2.2.3 or later

- CE endpoint must be running CE9.1.3 or later

- Cisco Unified Communications Manager (CUCM) must be running 11.5.1 or later

- Calls routed via Expressway must have Expressway running 8.9 or later

- Calls must be working with CMS

### Components Used

This document is not restricted to specific software and hardware versions:

- CMS API (Application program interface)

- Postman (or any other API client)

- CUCM

- CMS

- Cisco Telepresence Endpoints (SX, MX)

- PuTTY Secure Shell (SSH) terminal emulation software for Mainboard Management Processor (MMP)

- A web browser such as Firefox, Chrome

The information in the document created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you  understand the potential impact of any command.

## Configure

Step 1.  Set up an administrator user account with API permission or can use the administrator account for Cisco Unified Communications Manager. Please find how to create a user with API access.

You can create additional user accounts for the MMP that have admin level rights using the MMP

Add user command user add <account name> <role>.

- SSH into the MMP.

- Add an admin level user account, for example

Step 2. Configure CMS to support dual screen feature using API.

POST, parameter compatibilityProfiles .

POSTMAN API is used but any API tool can be used for configuration.

Step 3. Use GET operation to get the unique id for compatibilityProfiles/<compatibilityProfiles id> .

Step 4. Use PUT operation for sipMultiStream=true .

Step 5. Apply the configured compatibilityprofile under system/profiles . This is applied to the profile at top level and isused as global profile.

This image shows the compatibilityprofile being applied successfully.

The above is the required configuration to setup DualScreen feature on CMS. Now, you need to also configure an ednpoint with required configuration. The endpoint must run CE9.1.3 or later version of software code.

Step 6. MultiStream Mode on an endpoint must be set as AUTO as shown in this image.

Step 7. On Call Manager when configuring Sip trunk please keep in mind the sip profile used must have following parameters.

SDP Transparency Profile Pass all unknown SDP attributes .

IX, must be enabled on the Sip Profile for trunk.

On Call Manager for endpoints, the Sip Profile used should be either Standard SIP Profile For TelePresence Endpoint or if you customize the sip profile to use for endpoints ensure that you have these parameters checked.

Note : When the system is in a three-screen setup, for example the Cisco Telepresence SX80, MX700 or MX800, the third screen is reserved for content while in a dual screen call.

## Verify

Use this section in order to confirm that your configuration works properly

Consider, SX, MX700/800 to work as a dual screen endpoint. The layout of participants would appear as shown in the image and if you have an additional third monitor connected, the presentation should appear on the third monitor.

## Troubleshoot

Ensure to verify the software version for an endpoint, CUCM & CMS. Once confirmed the versions are supported then further troubleshooting is required

https://www.cisco.com/c/dam/en/us/td/docs/telepresence/endpoint/software/ce9/release-notes/ce-software-release-notes-ce9.pdf

https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Release_Notes/Version-2-2/Cisco-Meeting-Server-Release-Notes-2-2-5.pdf

Scenario 1. Dual screen feature does not work.

Collect Sip detailed traces on CMS

RTMT from Call Manager

Log bundle from the endpoint

Check logs for a scenario where dual screen feature was not working for the customer. Analyzing, to check the cause of the issue

Invite message sent by an endpoint

```
2017-08-24T11:25:31.709+08:00 SX80 appl[1660]: 3939.20 SipPacket I: SIP Msg: Outgoing => INVITE, CSeq: 100 INVITE, Remote: 172.16.19.110:5060, CallId: 280004cfb801730726ec1a9e9941d0d8
2017-08-24T11:25:31.709+08:00 SX80 appl[1660]: 3939.20 SipPacket    INVITE sip:8001@172.16.19.110 SIP/2.0
2017-08-24T11:25:31.709+08:00 SX80 appl[1660]: 3939.20 SipPacket    Via: SIP/2.0/TCP 172.16.19.116:5060;branch=z9hG4bKe04a77c1ce5008a9c69d4c621c705bb6;rport
2017-08-24T11:25:31.709+08:00 SX80 appl[1660]: 3939.20 SipPacket    Call-ID: 280004cfb801730726ec1a9e9941d0d8
2017-08-24T11:25:31.710+08:00 SX80 appl[1660]: 3939.21 SipPacket    CSeq: 100 INVITE
2017-08-24T11:25:31.710+08:00 SX80 appl[1660]: 3939.21 SipPacket    Contact: <sip:1000@172.16.19.116:55245;transport=tcp>;sip.cisco.multistream;x-cisco-multiple-screen=2 2017-08-24T11:25:31.726+08:00 SX80 appl[1660]: 3939.22 SipPacket    a=rtcp-fb:* ccm cisco-scr 
2017-08-24T11:25:31.726+08:00 SX80 appl[1660]: 3939.22 SipPacket    a=sendrecv
2017-08-24T11:25:31.727+08:00 SX80 appl[1660]: 3939.22 SipPacket    a=sprop-simul:1 1 * 
2017-08-24T11:25:31.727+08:00 SX80 appl[1660]: 3939.22 SipPacket    a=sprop-source:1 csi=3364746240 2017-08-24T11:25:31.727+08:00 SX80 appl[1660]: 3939.22 SipPacket    m=video 2390 RTP/AVP 99 97 126 96 34 31 123
```

The invite looks good which suggested the required software and configuration is correct on and endpoint.

It was a delayed offer from CUCM to CMS. CMS sent 200 OK

```
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: connection 23: outgoing SIP TCP data to 172.16.19.110:52560 from 172.16.19.123:5060, size 3830:
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: SIP/2.0 200 OK
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: Via: SIP/2.0/TCP 172.16
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: Max-Forwards: 70
```

In SDP

```
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=sendrecv 
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=sprop-source:1 count=2;policies=cs:1 
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=sprop-simul:1 1 * 
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=rtcp-fb:* nack pli 
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=rtcp-fb:* ccm fir 
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=rtcp-fb:* ccm cisco-scr Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=extmap:1  http://protocols.cisco.com/virtualid
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=extmap:2  http://protocols.cisco.com/framemarking
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=rtpmap:97 H264/90000
Aug 24 11:25:29 user.info< http://user.info>; acano host:server:  INFO : SIP trace: a=fmtp:97
```

The 200 OK from CMS has required attributes listed. The following attributes must be received by an endpoint to make the "dualscreen" feature to work effectively.

On endpoint when we checked the 200 Ok. We found the attributes were missing

```
2017-08-24T11:25:31.823+08:00 SX80 appl[1660]: 3939.32 SipPacket    m=video 34794 RTP/AVP 97 116 96 34 31
2017-08-24T11:25:31.823+08:00 SX80 appl[1660]: 3939.32 SipPacket    b=TIAS:1889000
2017-08-24T11:25:31.823+08:00 SX80 appl[1660]: 3939.32 SipPacket    a=label:11
2017-08-24T11:25:31.823+08:00 SX80 appl[1660]: 3939.32 SipPacket    a=rtpmap:97 H264/90000
2017-08-24T11:25:31.824+08:00 SX80 appl[1660]: 3939.32 SipPacket    a=fmtp:97 profile-level-id=428014;max-mbps=489600;max-fs=8160;max-dpb=4752;max-fps=6000
2017-08-24T11:25:31.824+08:00 SX80 appl[1660]: 3939.32 SipPacket    a=rtpmap:116 H264/90000
2017-08-24T11:25:31.824+08:00 SX80 appl[1660]: 3939.32 SipPacket    a=fmtp:116 profile-level-id=428014;packetization-mode=1;max-mbps=489600;max-fs=8160;max-dpb=4752;max-fps=6000
```

To check further, check the Call Manager traces. Analysed the following attributes are unrecognized.

```
00267759.030 |13:55:03.641 |AppInfo  |DET-SDPMsg- TCL_UNSPECIFIED (0)
00267759.031 |13:55:03.641 |AppInfo  |DET-SDPMsg- Unrecognized attributes list: a=extmap:1   http://protocols.cisco.com/virtualid a=extmap:14   http://protocols.cisco.com/timestamp#100us a=rtcp-fb:* ccm cisco-scr a=sprop-simul:1 1 * a=sprop-source:1 csi=51132416 00267759.032 |13:55:03.641 |AppInfo  |DET-SDPMsg- mAudiomLines(i).bandwidth.enabledMask=TIAS, TIAS=128000, AS=0, CT=0, RS=0, RR=0
00267759.033 |13:55:03.641 |AppInfo  |DET-SDPMsg- nVideo=2
00267759.034 |13:55:03.641 |AppInfo  |DET-SDPMsg- remoteIpAddr=172.16.19.116 remoteRtpPortNumber=2370 stackIdx=2 telephonyEvent=0 silenceSuppressionFlag=0 mSDPMode=0 idleFlag=0 vcId=1 mid=-1
```

Checked the Sip Profile to make sure the following parameters as mentioned above in the document are checked.

SDP Transparency Profile Pass all unknown SDP attributes . This parameter is setup on the configured sip profile. However, Allow iX Application Media is not checked.

Check the Allow iX Application Media and this fixed the issue.

Scenario 2. Dual screen feature not working.

In second scenario the problem is the same. However, the cause is different.

Endpoint sends the INVITE with required header and attributes in SDP. However; CUCM is unable to recognized the attributes in the SDP.

```
INVITE sip:95101@192.168.11.2<mailto:sip%3A95101@192.168.11.2> SIP/2.0
Via: SIP/2.0/TCP 192.168.11.9:58911;branch=z9hG4bK64fdaf0987c59765f74b7f8f2673adfe;rport
Call-ID: ca81ed904b80cf18528e5b0a4e4a4c01
CSeq: 100 INVITE
Contact: <sip:7436254f-c370-ccad-745d-110f8f59bee2@192.168.11.9<mailto:110f8f59bee2@192.168.11.9>:58911;transport=tcp>; sip.cisco.multistream;x-cisco-multiple-screen=2 From: "Sala 5 Cota" <sip:571317@192.168.11.2<mailto:sip%3A571317@192.168.11.2>>;tag=0edc947e1b7a916a
To: <sip:95101@192.168.11.2<mailto:sip%3A95101@192.168.11.2>>
Max-Forwards: 70
Route: <sip:192.168.11.2;lr>
Allow: INVITE,ACK,CANCEL,BYE,UPDATE,INFO,OPTIONS,REFER,NOTIFY
User-Agent: TANDBERG/529 (ce9.1.4.3ae3106) Cisco-MX700ST
Supported: replaces,100rel,timer,gruu,path,outbound,X-cisco-serviceuri,X-cisco-callinfo,X-cisco-service-control,X-cisco-sis-7.1.1,norefersub,extended-refer,sdp-anat
Recv-Info: x-cisco-conference
Session-Expires: 1800
Allow-Events: dialog
Remote-Party-ID: "Sala 5 Cota" <sip:571317@192.168.11.2<mailto:sip%3A571317@192.168.11.2>>;privacy=off;id-type=subscriber;screen=yes;party=calling
Content-Type: application/sdp
Content-Length: 4166
 
04323021.031 |21:05:59.460 |AppInfo  |//SIP/SIPHandler/ccbId=0/scbId=0/getTrunInfoByRouteHdr: Route header userPart is missing
04323021.032 |21:05:59.460 |AppInfo  |//SIP/SIPHandler/ccbId=0/scbId=0/getRel1xxType: No matching SIP trunk found in hash table, returning rel1xx disabled
04323021.033 |21:05:59.460 |AppInfo  |//SIP/SIPHandler/ccbId=4294967295/scbId=0/sipSPIGetCallExtensionSupported: SIPRel1xxEnabledServiceParamSetting=0 , ccb->pld.outboundRel1xx=1
04323021.034 |21:05:59.460 |AppInfo  |//SIP/SIPHandler/ccbId=0/scbId=0/sip_stop_timer: timerContext=0xdbc4a3c type=SIP_TIMER_EXPIRES value=1800000 retries=0
04323021.035 |21:05:59.461 |AppInfo  |//SIP/SIPHandler/ccbId=0/scbId=0/sip_start_timer: timerContext=0xdbc4a3c type=SIP_TIMER_EXPIRES value=1800000 retries=0
04323021.036 |21:05:59.461 |AppInfo  |//SIP/SIPHandler/ccbId=0/scbId=0/extractAssertedInfo: parseResult[1] 04323021.037 |21:05:59.475 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_attr_rtcpfb: rtcp-fb ccm has unrecognized param token: cisco-scr 
04323021.038 |21:05:59.475 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_attr_rtcpfb: rtcp-fb ccm has unrecognized param token: cisco-scr 
04323021.039 |21:05:59.475 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_attr_rtcpfb: rtcp-fb ccm has unrecognized param token: cisco-scr 
04323021.040 |21:05:59.476 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_fmtp_line_params:  Warning: Invalid maxbr specified for fmtp attribute. 
04323021.041 |21:05:59.476 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_fmtp_line_params:  Warning: Invalid maxbr specified for fmtp attribute. 
04323021.042 |21:05:59.476 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_fmtp_line_params:  Warning: Invalid maxbr specified for fmtp attribute. 
04323021.043 |21:05:59.476 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_fmtp_line_params:  Warning: Invalid maxbr specified for fmtp attribute. 
04323021.044 |21:05:59.476 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_fmtp_line_params:  Warning: Invalid maxbr specified for fmtp attribute. 04323021.045 |21:05:59.476 |AppInfo  |//SIP/SDPLib/Warning/0x0/sdp_parse_fmtp_line_params:  Warning: Invalid maxbr specified for fmtp attribute. 
04323021.046 |21:05:59.477 |AppInfo  |//SIP/SIPHandler/ccbId=0/scbId=0/getMP4ALATMParameters: Saved payload(107) as Media_Payload_MP4ALATM_128, clock=90000, profile=25,
```

CUCM is unable to recognized parameter like cisco-scr which is required for DualScreen feature to work. As the following endpoint is registered to Call Manager and there is no trunk in between. Checked the "SipProfile" configured for an endpoint analysed and found the setup using Standard Sip Profile rather it should use "Standard SIP Profile For Telepresence Endpoint"

Change to correct Sip Profile.