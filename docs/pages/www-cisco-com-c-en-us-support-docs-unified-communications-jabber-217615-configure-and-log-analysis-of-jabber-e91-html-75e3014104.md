---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-217615-configure-and-log-analysis-of-jabber-e91-html-75e3014104
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/217615-configure-and-log-analysis-of-jabber-e91.html
retrieved_at: 2026-08-21T07:05:16.524137+00:00
---

Configure and Log Analysis of Jabber E911

# Configure and Log Analysis of Jabber E911

### Download Options

Updated: June 30, 2023

Document ID: 217615

Contents

## Contents

## Introduction

This document describes the E911 Jabber deployment along with a trace analysis in regards to how Jabber behaves when 911 or emergency numbers are dialled from the softphone.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of:

- Cisco Unified Communications Manager configuration.

- SIP protocol basics.

- Basic call routing on CUCM.

### Components Used

This document is not restricted to specific software and hardware versions.

pThe information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Basic Configuration of the E911 Number

The Remote Worker Emergency Calling (RWEC) feature enables you to provide reliable emergency calling support to remote workers with remote Virtual Private Network (VPN) connections. Emergency calls from off-premises users are routed to the Public Safety Answering Point (PSAP), and user-provided location information is delivered with each call.

You must configure Intrado (a third party application) on the Cisco Emergency Responder before you configure the RWEC feature. For information about how to configure Intrado on the Cisco Emergency Responder, refer to the Cisco Emergency Responder Administration Guide .

Step 1. Configure the User as a Remote Worker:

- Navigate to Cisco Unified CM Administration > Device > Phone.

- Enter the appropriate search criteria to find the phone and click Find . A list of phones that match the search criteria are displayed.

- Select the phone for which you want to configure RWEC. The Phone Configuration window is displayed.

- From the Device Information section, select the appropriate user ID from the Owner User ID drop-down list and check the Require off-premise location check box.

- Click Save .

Step 2. Specify an Alternate Route for Emergency Calling

- Navigate to Cisco Unified CM Administration > System > Service Parameters .

- From the Server drop-down list, select a server .

- From the Service drop-down list, select Cisco CallManager . The Service Parameter Configuration window appears.

- In the Clusterwide Parameters (Emergency Calling for Required Off-premise Location) section, specify Alternate Destination for Emergency Call .

- Specify an Alternate Calling Search Space for Emergency Call .

- Click Save .

Step 3. Configure the Application Server

Note : You must configure the application server to enable the E911 Proxy to communicate with the Cisco Emergency Responder. E911 proxy is used to direct the users to the application server where they enter the location of the device.

- Navigate to Cisco Unified CM Administration > System > Application Server .

- Click Add New . The Application Server window appears.

- From the Application Server Type drop-down list, select CER Location Management .

- Click Next

- In the Name field, specify a name to identify the application server to be configured.

- In the IP address field, specify the IP address of the server to be configured.

- From the list of Available Application Users, select the application user and click the Down arrow.

- In the End User URL field, enter a URL for the end-users that are associated with this application server.

- Click Save .

Step 4. Configure E911 Messages

- Navigate to Cisco Unified CM Administration > System > E911 Messages .

- Select the required language link of the E911 messages. The E911 Messages Configuration page displays the Agreement, Disclaimer, and Error messages.

- (Optional) Edit the E911 messages to be displayed on off-premises devices.

- Click Save .

### Deployment

If you use the Jabber internally, you can define it as you would a physical phone via the dial-plan or via the Cisco Emergency Responder (CER).

If you use it in a remote environment, there are a couple of ways to address it, and it differs from Jabber for Windows/MAC and Jabber on iPhone and Android.

For Windows and MAC remote users, the CER has a mobility page where users can manually update their E911 location. If, for example, you work from home, you can enter your home address as the Emergency Response Line (ERL) for your Directory number (DN), but you would have to change it when you return to the office or move to a different location.

For mobile devices, the default is to have Jabber use the cellular network and number when the 911 number is dialled so that the phone location is what is received by the Public Safety Answering Point (PSAP) and it can identify the caller’s location and return the call if necessary.

In addition, the system automatically tracks and updates equipment moves and changes. If you deploy this capability, it can help ensure more effective compliance with legal or regulatory obligations and reduce the risk of liability related to emergency calls as a result.

Note : Many of the E911 service providers such as Redsky also provide mobility services similar to CER.

On the Jabber configuration guide, you can observe this description:

## Verify

Use this section to confirm that your configuration works properly.

### Log Analysis

Within the Jabber Problem Report, the default map behaviour of the E911 emergency number can be seen. Here is the digit analysis and call process:

```
2021-09-14 14:53:26,773 DEBUG [0x0000000107573880] [nyservice/TelephonyAdapterVoice.cpp(317)] [jcf.tel.adapter] [applyDirectoryLookupRules] - Number BEFORE applying directory lookup rules: [9911] 2021-09-14 14:53:26,773 DEBUG [0x0000000107573880] [ory/ContactResolutionFeatureSet.cpp(424)] [ContactService-ContactsAdapter] [resolveBySipUriOrNumber] - sip uri=, number=9911 , display name=9911 2021-09-14 14:53:37,252 DEBUG [0x0000000107573880] [pl/CommunicationHistoryItemImpl.cpp(151)] [CommunicationHistoryService-CommunicationHistoryAdapter] [CommunicationHistoryItemImpl] - New item contains: jid = dialedNumber = 9911 displayName = 9911 contact picked from phone number
```

Two Jabber Problem Reports were collected, one goes through the GSM network and the other one via the SIP trunk to the CUCM. Both were compared.

```
2021-09-29 12:38:53,644 INFO  [0x000000010b6db880] [ager/TelephonyConfigManagerImpl.cpp(561)] [jcf.tel.config] [setUptheConfigListeners] - Config notifier added for Value property Key: [E911NotificationUrl] 2021-09-29 12:38:53,644 DEBUG [0x000000010b6db880] [ager/TelephonyConfigManagerImpl.cpp(675)] [jcf.tel.config] [cacheAllConfigFromService] - Config not found for Key: [E911NotificationUrl]. Using default value: [] 2021-09-29 12:38:53,646 INFO  [0x000000010b6db880] [ager/TelephonyConfigManagerImpl.cpp(561)] [jcf.tel.config] [setUptheConfigListeners] - Config notifier added for Value property Key: [EnableE911OnPremLocationPolicy] 2021-09-29 12:38:53,646 INFO  [0x000000010b6db880] [ager/TelephonyConfigManagerImpl.cpp(568)] [jcf.tel.config] [setUptheConfigListeners] - Config notifier added for isDefined property for key: [EnableE911OnPremLocationPolicy] 2021-09-29 12:38:53,646 INFO  [0x000000010b6db880] [ager/TelephonyConfigManagerImpl.cpp(561)] [jcf.tel.config] [setUptheConfigListeners] - Config notifier added for Value property Key: [EnableE911EdgeLocationPolicy] 2021-09-29 12:38:53,646 INFO  [0x000000010b6db880] [ager/TelephonyConfigManagerImpl.cpp(568)] [jcf.tel.config] [setUptheConfigListeners] - Config notifier added for isDefined property for key: [EnableE911EdgeLocationPolicy] 2021-09-29 12:38:53,646 INFO  [0x000000010b6db880] [ager/TelephonyConfigManagerImpl.cpp(561)] [jcf.tel.config] [setUptheConfigListeners] - Config notifier added for Value property Key: [E911EdgeLocationWhiteList] 2021-09-29 12:38:53,646 INFO  [0x000000010b6db880] [ager/TelephonyConfigManagerImpl.cpp(568)] [jcf.tel.config] [setUptheConfigListeners] - Config notifier added for isDefined property for key: 2021-09-29 12:38:53,688 DEBUG [0x000000010b6db880] [nyservice/TelephonyAdapterVoice.cpp(317)] [jcf.tel.adapter] [applyDirectoryLookupRules] - Number BEFORE applying directory lookup rules: [9911] 2021-09-29 12:38:53,688 DEBUG [0x000000010b6db880] [nyservice/TelephonyAdapterVoice.cpp(321)] [jcf.tel.adapter] [applyDirectoryLookupRules] - Number AFTER applying directory lookup rules: [9911]
```

These policy configurations identify that 911 is dialled on the Jabber and it acts as the default behaviour.

This behaviour can be identified if you navigate to the TCT or BOT device in CUCM, where you can find the Emergency Numbers field under the Product Specific Configuration Layout section. You can press ? next to the section header, which takes you to the online help page where you can find a very clear statement of how it is supposed to work:

Emergency Numbers:

A ',' delimited list of emergency numbers (e.g. 911). These numbers will be dialled through GSM rather than the softphone.

Default: 999,911,112

Maximum length: 32”.

Image from the path for configuration:

This scenario does not cover the SIP call handling as it is redirected to the CER to perform the appropriate call routing.

Note : You can also remove 911 to be recognized as an emergency number for the CUCM according to the Feature Configuration Guide . When the Jabber emergency number is removed from the call handler, the call processing would be performed like a regular call.

In this scenario, where the call is routed to CER and to the PSAP, the call processing must generate an INVITE to initiate a call like a regular SIP call:

The SIP INVITE IS generated, the number is taken as “911” and routed via the SIP trunk.

```
2021-09-29 13:11:30,890 DEBUG [0x00000001705f7000] [/sipcc/core/sipstack/ccsip_debug.c(1735)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-sent---> INVITE sip:911@daviher2.domain.com;user=phone SIP/2.0 Via: SIP/2.0/TCP 10.1.10.15:50748;branch=z9hG4bK0f77f9f5 From: "Edward Blake 5518" sip:5518@ daviher2.domain.com ;tag=5e2487c68e45000957e9a9ab-2d8246a4 To: sip:911@ daviher2.domain.com Call-ID: 5e2487c6-8e450004-07c6c702-0b33584b@10.1.10.15Max-Forwards: 70 Session-ID: 726dd14700105000a0005e2487c68e45;remote=00000000000000000000000000000000 Date: Wed, 29 Sep 2021 17:11:30 GMT CSeq: 101 INVITE User-Agent: Cisco-TCT Contact: sip:e1a29201-56bf-2042-32c5-75b15ba90785@10.1.10.15:50748;transport=tcp;+u.sip!devicename.ccm.cisco.com= "TCTEDWBLK";video;bfcp Expires: 180 Accept: application/sdp Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO Remote-Party-ID: "Edward Blake 5518" sip:5518@daviher2.domain.com ;party=calling;id-type=subscriber;privacy=off;screen=yes Call-Info: <urn:x-cisco-remotecc:callinfo>; security=NotAuthenticated; orientation=to; call-instance=1; isVoip Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri, X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0, X-cisco-xsi-8.5.1 Allow-Events: kpml,dialog Recv-Info: conference Recv-Info: x-cisco-conference Content-Length: 2730 Content-Type: application/sdp Content-Disposition: session;handling=optional
```

The SIP TRYING from the CUCM server means it has contacted the remote device to establish the SIP call.

```
2021-09-29 13:11:30,953 DEBUG [0x00000001705f7000] [/sipcc/core/sipstack/ccsip_debug.c(1735)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-recv<--- SIP/2.0 100 Trying Via: SIP/2.0/TCP 10.1.10.24:50748;branch=z9hG4bK0f77f9f5 From: "Edward Blake 5518" sip:5518@ daviher2.domain.com >;tag=5e2487c68e45000957e9a9ab-2d8246a4 To: sip:911@ daviher2.domain.com Date: Wed, 29 Sep 2021 17:11:30 GMT Call-ID: 5e2487c6-8e450004-07c6c702-0b33584b@10.1.10.24 CSeq: 101 INVITE Allow-Events: presence Content-Length: 0
```

The SIP 180 Ringing shows that the initial SIP call negotiation happened and the remote device is alerted.

```
[SIP][MSG]                                                     [SOCK][.]<--- SIP/2.0 180 Ringing 2021-09-29 13:11:38,824 DEBUG [0x00000001705f7000] [/sipcc/core/sipstack/ccsip_debug.c(1735)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-recv<--- SIP/2.0 180 Ringing Via: SIP/2.0/TCP 10.1.10.24:50748;branch=z9hG4bK0f77f9f5 From: "Edward Blake 5518" sip:5518@ daviher2.domain.com >;tag=5e2487c68e45000957e9a9ab-2d8246a4 To: < To: sip:911@ daviher2.domain.com >;tag=331350799~1551199b-213c-4609-83c4-4420b55caf48-39377222 Date: Wed, 29 Sep 2021 17:11:30 GMT Call-ID: 5e2487c6-8e450004-07c6c702-0b33584b@10.1.10.24 CSeq: 101 INVITE Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY Allow-Events: presence Server: Cisco-CUCM12.5 Call-Info: <urn:x-cisco-remotecc:callinfo>; security= Unknown; orientation= to; ui-state= ringout; gci= 2-11891177; isVoip; call-instance= 1 Send-Info: conference, x-cisco-conference Session-ID: 00000000000000000000000000000000;remote=726dd14700105000a0005e2487c68e45 Remote-Party-ID: <sip:919082059688@10.1.10.11>;party=called;screen=no;privacy=off Contact: <sip:911@10.1.10.11:5060;transport=tcp> Content-Length: 0
```

The SIP 200 OK is received to complete the call and advise which codecs were negotiated.

```
2021-09-29 13:11:47,577 DEBUG [0x00000001705f7000] [/sipcc/core/sipstack/ccsip_debug.c(1735)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-recv<--- SIP/2.0 200 OK Via: SIP/2.0/TCP 10.1.10.24:50748;branch=z9hG4bK0f77f9f5 From: "Edward Blake 5518" sip:5518@ daviher2.domain.com >;tag=5e2487c68e45000957e9a9ab-2d8246a4 To: < To: sip:911@ daviher2.domain.com >;tag=331350799~1551199b-213c-4609-83c4-4420b55caf48-39377222 Date: Wed, 29 Sep 2021 17:11:30 GMT Call-ID: 5e2487c6-8e450004-07c6c702-0b33584b@10.1.10.24 CSeq: 101 INVITE Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY Allow-Events: presence Supported: replaces Server: Cisco-CUCM12.5 Call-Info: <urn:x-cisco-remotecc:callinfo>; security= NotAuthenticated; orientation= to; gci= 2-11891177; isVoip; call-instance= 1 Send-Info: conference, x-cisco-conference Session-ID: 42582595f8ee52f7a033f11b6679f7ed;remote=726dd14700105000a0005e2487c68e45 Remote-Party-ID: <sip:9082059688@10.1.10.11>;party=called;screen=yes;privacy=off Contact: <sip:911@10.1.10.11:5060;transport=tcp> Content-Type: application/sdp Content-Length: 733 v=0 o=CiscoSystemsCCM-SIP 331350799 1 IN IP4 10.1.10.11 s=SIP Call c=IN IP4 172.22.191.3 b=AS:80 t=0 0 m=audio 18594 RTP/AVP 0 101 a=ptime:20 a=rtpmap:0 PCMU/8000 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-15 a=trafficclass:conversational.audio.aq:admitted m=video 0 RTP/AVP 31 34 96 97 a=rtpmap:31 H261/90000 a=rtpmap:34 H263/90000 a=rtpmap:96 H263-1998/90000 a=rtpmap:97 H264/90000 a=content:main a=inactive m=video 0 RTP/AVP 31 34 96 97 a=rtpmap:31 H261/90000 a=rtpmap:34 H263/90000 a=rtpmap:96 H263-1998/90000 a=rtpmap:97 H264/90000 a=content:slides a=inactive m=application 0 UDP/BFCP * c=IN IP4 0.0.0.0 m=application 0 RTP/AVP 96 a=rtpmap:96 H224/0 a=inactive m=application 0 UDP/UDT/IX
```

Finally, the Jabber device sends a SIP ACK to the server, which states that the call was completed successfully.

```
2021-09-29 13:11:47,591 DEBUG [0x00000001705f7000] [/sipcc/core/sipstack/ccsip_debug.c(1735)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-sent---> ACK sip:911@10.1.10.11:5060;transport=tcp SIP/2.0 Via: SIP/2.0/TCP 10.1.10.24:50748;branch=z9hG4bK0dbb4bc2 From: "Edward Blake 5518" sip:5518@ daviher2.domain.com >;tag=5e2487c68e45000957e9a9ab-2d8246a4 To: < To: sip:911@ daviher2.domain.com >;tag=331350799~1551199b-213c-4609-83c4-4420b55caf48-39377222 Call-ID: 5e2487c6-8e450004-07c6c702-0b33584b@10.1.10.24 Max-Forwards: 70 Session-ID: 726dd14700105000a0005e2487c68e45;remote=42582595f8ee52f7a033f11b6679f7ed Date: Wed, 29 Sep 2021 17:11:47 GMT CSeq: 101 ACK User-Agent: Cisco-TCT Remote-Party-ID: "Edward Blake 5518" sip:5518@ daviher2.domain.com >;party=calling;id-type=subscriber; privacy=off;screen=yes Recv-Info: conference Recv-Info: x-cisco-conference Content-Length: 0
```

With this procedure, the call goes through the SIP trunk registered on the CUCM.

Note : It is important to mention that you have the option to remove the 911 or any other emergency number to be recognized as a non-emergency number and in that scenario, the call might be routed as explained on this latest log analysis.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

2.0

30-Jun-2023

Removed broken hyperlinks.

1.0

03-Jan-2022

Initial Release

### Contributed by Cisco Engineers

David Hernandez

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 30-Jun-2023 | Removed broken hyperlinks. |
| 1.0 | 03-Jan-2022 | Initial Release |