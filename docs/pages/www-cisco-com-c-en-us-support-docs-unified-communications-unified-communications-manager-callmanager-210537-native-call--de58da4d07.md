---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-210537-native-call--de58da4d07
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/210537-Native-Call-Queueing-Enhancement-in-CUCM.html
retrieved_at: 2026-08-21T13:55:51.288025+00:00
---

Native Call Queueing Enhancement in CUCM 11.5

# Native Call Queueing Enhancement in CUCM 11.5

### Download Options

Updated: April 9, 2017

Document ID: 210537

Contents

## Contents

## Introduction

Cisco Unified Communications Manager(CUCM) provides Call Queuing to place callers in a queue until hunt members are available to answer them. An administrator can set the default so callers receive an initial greeting announcement before the call is extended to an agent or the default can be changed so the initial announcement plays only after the caller is put in the queue followed by Music On Hold or Tone On Hold. If the caller remains in queue for a specified period of time, a secondary announcement is played at a configured interval until the call can be answered or until the maximum wait timer expires.

## Components Used

- Cisco Unified Communication Manager Version 11.5.1

- Cisco IP Phone Version 8.6.6.0

## Background Information

This section describes the basic function of native call queuing prior to the enhancement in CUCM 11.5

When a call comes in and reaches the hunt pilot, these functions are provided:

- A caller can be connected to an initial customizable greeting announcement before proceed.

- If one or more line members are logged in to the hunt pilot and are in an idle state, and if no calls are queued, the call is extended to the line member that has been idle for the longest period of time.

- If no line members answer a call, that caller is not placed in queue. The call is routed to a new destination or disconnected, based on the setup When no hunt members answer, are logged in, or registered.

- If a line member does not answer a queue-enabled call, that line member is logged off the hunt group only if the option Automatically Logout Hunt Member on No Answer is selected in the Line Group setup window.

- Calls are placed in queue only if all members are busy.

- A caller who is connected in queue can hear Music On Hold and a repeating (customizable) periodic announcement.

- After a line member becomes idle, the caller with the longest wait time across multiple hunt groups is extended to the idle line member. If the idle line member does not answer the call, the caller is returned to the previous position in the queue.

- A hunt pilot DN with queuing either enabled or disabled

- A voicemail DN

- A line DN

- A shared DN

- Hunt pilot pattern

- Number of queued callers on each hunt pilot

- Longest waiting time

Call queuing works in conjunction with existing hunt pilots, but there are no changes in the behavior of the hunting operation for either queuing or nonqueuing hunt pilots. Hunt pilots that have call queuing enabled provide the following features:

- Queuing-enabled hunt pilot calls can only be received by line members one call at a time. Two queuing-enabled hunt pilot calls cannot be offered to a line member. A line member can receive calls directly to the DN or from non-queuing hunt pilots.

- Line members who do not answer calls that are routed by hunt pilots are automatically logged out. A line member is automatically logged out of a device if the line member receives a queuing-enabled hunt pilot call and does not answer the call before timeout occurs. In the case of a shared-line deployment, all devices configured with the same shared line are logged out. You can configure this behavior from the Line Group setting window by selecting Automatically Logout Hunt Member on No Answer. Line members are logged out only if this check box is checked.

With the working of call queuing as described there were many instances where the end user would hear dead air or silence during the initial announcement, thus causing the user to think that the call was not successful. This situation would arise when one end could not be able to support early media in the call.

## Feature Overview

Starting with Cisco Unified Communications Manager Release 11.5, you can configure the inbound calls to change to the connected call state before playing the queuing announcement, while the call is extended to a hunt member in the queuing-enabled hunt pilot. The new Connect Inbound Call before Playing Queuing Announcement check box is added to the following trunk and gateway configuration windows :

- H.225 Trunk (Gatekeeper Controlled)

- Inter-Cluster Trunk (Non- Gatekeeper Controlled)

- Inter Cluster Trunk(Gatekeeper Controlled)

- H.323 Gateway(Gateway Type)

- SIP Profile (Trunk Specific Configuration)

- MGCP (E1 PRI, T1 PRI, T1 CAS, and BRI)

Once the user checks this box, CUCM will send 200OK after the 100Trying in case of SIP and in case of H323/MGCP CUCM will send a Connect in the Hunt Pilot call flow. This will ensure that the user can hear the initial announcement instead of silence or dead air in case the other end is not able to support Early Media.

## Configuration

Below are the configuration snapshots with the newly added parameter on the CUCM

### H.225 Trunk (Gatekeeper Controlled)

### Inter-Cluster Trunk (Non-Gatekeeper Controlled)

### Inter-Cluster Trunk (Gatekeeper Controlled)

### H.323 Gateway

### SIP Profile

### MGCP (E1 PRI, T1 PRI, T1 CAS, and BRI)

## Log Analysis

The below section focuses on the differences seen in the trace files when the " Connect Inbound Call before Playing Queuing Announcement " is checked and unchecked.

```
SIP Normal Call Flow Incoming Invite to the CUCM 00455394.002 |18:33:30.036 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.127.227.7 on port 55522 index 16 with 1182 bytes: [14599,NET] INVITE sip:0000@10.106.111.105:5060 SIP/2.0 Via: SIP/2.0/TCP 10.127.227.7:5060;branch=z9hG4bK4e222dea4e0 From: <sip:888819@10.127.227.7>;tag=107999~6c65cba7-94a0-4069-84c7-4774aecf0647-33198813 To: <sip:0000@10.106.111.105> . . //Truncated Output 100 Trying Sent 00455398.001 |18:33:30.037 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.127.227.7 on port 55522 index 16 [14600,NET] SIP/2.0 100 Trying Via: SIP/2.0/TCP 10.127.227.7:5060;branch=z9hG4bK4e222dea4e0 From: <sip:888819@10.127.227.7>;tag=107999~6c65cba7-94a0-4069-84c7-4774aecf0647-33198813 To: <sip:0000@10.106.111.105> . . //Truncated Output Digit Analysis takes place 00455415.007 |18:33:30.038 |AppInfo  |Digit analysis: match(pi="2", fqcn="", cn="888819",plv="5", pss="", TodFilteredPss="", dd="0000",dac="0") 00455415.008 |18:33:30.038 |AppInfo  |Digit analysis: analysis results 00455415.009 |18:33:30.038 |AppInfo  ||PretransformCallingPartyNumber=888819 |CallingPartyNumber=888819 |DialingPartition= |DialingPattern=0000 |FullyQualifiedCalledPartyNumber=0000 Allocate Annunciater for the Initial Announcement 00455426.001 |18:33:30.039 |AppInfo  |QueueControlCdrc(17) - get_call_info_SsCallInfoRes, huntPilotQueueProfile.alwaysplayinitialannouncement=1 00455432.001 |18:33:30.039 |AppInfo  |MediaResourceCdpc(22)::waiting_MrmAllocateAnnResourceReq - CI = 21438416 Media Negotiation takes place for initial announcement 00455454.001 |18:33:30.041 |AppInfo  |ARBTRY-ConnectionManager-wait_MediaConnectRequest(21438414,21438416) 00455478.001 |18:33:30.041 |AppInfo  |ARBTRY-ConnectionManager- wait_MediaConnectReply(21438414,21438416) 183 Session Progress sent for early media with SDP a=sendonly 00455494.001 |18:33:30.143 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.127.227.7 on port 55522 index 16 [14601,NET] SIP/2.0 183 Session Progress Via: SIP/2.0/TCP 10.127.227.7:5060;branch=z9hG4bK4e222dea4e0 From: <sip:888819@10.127.227.7>;tag=107999~6c65cba7-94a0-4069-84c7-4774aecf0647-33198813 To: <sip:0000@10.106.111.105>;tag=4705~8b68bd5c-f78f-44c5-b1ce-8ea93a8efbb6-21438414 . . //Truncated Output . . v=0 o=CiscoSystemsCCM-SIP 4705 1 IN IP4 10.106.111.105 s=SIP Call c=IN IP4 10.106.111.105 t=0 0 m=audio 4000 RTP/AVP 0 8 18 a=X-cisco-media:umoh+ConnSendOnly a=rtpmap:0 PCMU/8000 a=rtpmap:8 PCMA/8000 a=rtpmap:18 G729/8000 a=fmtp:18 annexb=no a=sendonly SIP Call Flow with "Connect Inbound Call before Playing Queuing Announcement" checked Incoming Invite to the CUCM 00452822.002 |18:22:22.842 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.127.227.7 on port 56658 index 14 with 1182 bytes: [14494,NET] INVITE sip:0000@10.106.111.105:5060 SIP/2.0 Via: SIP/2.0/TCP 10.127.227.7:5060;branch=z9hG4bK4d2425c95ba From: <sip:888819@10.127.227.7>;tag=107977~6c65cba7-94a0-4069-84c7-4774aecf0647-33198808 To: <sip:0000@10.106.111.105> . . //Truncated Output 100 Trying sent 00452826.001 |18:22:22.843 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.127.227.7 on port 56658 index 14 [14495,NET] SIP/2.0 100 Trying Via: SIP/2.0/TCP 10.127.227.7:5060;branch=z9hG4bK4d2425c95ba From: <sip:888819@10.127.227.7>;tag=107977~6c65cba7-94a0-4069-84c7-4774aecf0647-33198808 To: <sip:0000@10.106.111.105> . . //Truncated Output Digit Analysis takes place 00452843.007 |18:22:22.844 |AppInfo  |Digit analysis: match(pi="2", fqcn="", cn="888819",plv="5", pss="", TodFilteredPss="", dd="0000",dac="0") 00452843.008 |18:22:22.844 |AppInfo  |Digit analysis: analysis results 00452843.009 |18:22:22.844 |AppInfo  ||PretransformCallingPartyNumber=888819 |CallingPartyNumber=888819 |DialingPartition= |DialingPattern=0000 |FullyQualifiedCalledPartyNumber=0000 Annunciater allocated for Initial announcement 00452854.001 |18:22:22.845 |AppInfo  |QueueControlCdrc(15) - get_call_info_SsCallInfoRes, huntPilotQueueProfile.alwaysplayinitialannouncement=1 00452860.001 |18:22:22.845 |AppInfo  |MediaResourceCdpc(19)::waiting_MrmAllocateAnnResourceReq - CI = 21438406 Media Negotiation for the initial announcement 00452882.001 |18:22:22.846 |AppInfo  |ARBTRY-ConnectionManager-wait_MediaConnectRequest(21438404,21438406) 00452906.001 |18:22:22.847 |AppInfo  |ARBTRY-ConnectionManager- wait_MediaConnectReply(21438404,21438406) 200 OK with SDP a=sendonly sent instead of 183 session progress thus connecting the call rather than an early media. 00452928.001 |18:22:22.848 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.127.227.7 on port 56658 index 14 [14496,NET] SIP/2.0 200 OK Via: SIP/2.0/TCP 10.127.227.7:5060;branch=z9hG4bK4d2425c95ba From: <sip:888819@10.127.227.7>;tag=107977~6c65cba7-94a0-4069-84c7-4774aecf0647-33198808 To: <sip:0000@10.106.111.105>;tag=4690~8b68bd5c-f78f-44c5-b1ce-8ea93a8efbb6-21438404 . . //Truncated Output . . v=0 o=CiscoSystemsCCM-SIP 4690 1 IN IP4 10.106.111.105 s=SIP Call c=IN IP4 10.106.111.105 t=0 0 m=audio 4000 RTP/AVP 0 8 18 a=X-cisco-media:umoh+ConnSendOnly a=rtpmap:0 PCMU/8000 a=rtpmap:8 PCMA/8000 a=rtpmap:18 G729/8000 a=fmtp:18 annexb=no a=sendonly
```

H323 Normal Call Flow

```
Incoming H323 Setup Message 00091345.011 |09:03:06.341 |AppInfo  |SPROCRas - { h323-uu-pdu { h323-message-body setup : { protocolIdentifier { 0 0 8 2250 0 5 }, sourceAddress { dialedDigits : "999919", h323-ID : {"999919", {0, 0, 0, 0}, ...} . . //Truncated Output Digit Analysis takes place 00091367.006 |09:03:06.384 |AppInfo  |Digit analysis: match(pi="2", fqcn="", cn="999919",plv="5", pss="", TodFilteredPss="", dd="0000",dac="0") 00091367.007 |09:03:06.384 |AppInfo  |Digit analysis: analysis results 00091367.008 |09:03:06.384 |AppInfo  ||PretransformCallingPartyNumber=999919 |CallingPartyNumber=999919 |DialingPartition= |DialingPattern=0000 Annunciator Allocated for initial announcement 00091378.001 |09:03:06.388 |AppInfo  |QueueControlCdrc(1) - get_call_info_SsCallInfoRes, huntPilotQueueProfile.alwaysplayinitialannouncement=1 00091384.001 |09:03:06.388 |AppInfo  |MediaResourceCdpc(1)::waiting_MrmAllocateAnnResourceReq - CI = 25333775 Call Proceeding Message sent 00091386.005 |09:03:06.389 |AppInfo  |{ h323-uu-pdu { h323-message-body callProceeding : { protocolIdentifier { 0 0 8 2250 0 5 }, . . //Truncated Output Media Negotiation takes place for the initial announcement 00091407.001 |09:03:06.392 |AppInfo  |ARBTRY-ConnectionManager-wait_MediaConnectRequest(25333773,25333775) 00091447.001 |09:03:06.411 |AppInfo  |ARBTRY-ConnectionManager- wait_MediaConnectReply(25333773,25333775) H323 Progress message sent for early media, which is followed by the H245 messages for media negotiation 00091456.005 |09:03:06.411 |AppInfo  |SPROCRas - { h323-uu-pdu { h323-message-body progress : { protocolIdentifier { 0 0 8 2250 0 5 }, . . //Truncated Output H323 Call flow with the "Connect Inbound Call before Playing Queuing Announcement" checked Incoming setup message to the CUCM 00092572.010 |09:07:25.234 |AppInfo  |SPROCRas - { h323-uu-pdu { h323-message-body setup : { protocolIdentifier { 0 0 8 2250 0 5 }, sourceAddress { dialedDigits : "999919", h323-ID : {"999919", {0, 0, 0, 0}, ...} }, . . //Truncated Output Digit Analysis takes place 00092594.006 |09:07:25.236 |AppInfo  |Digit analysis: match(pi="2", fqcn="", cn="999919",plv="5", pss="", TodFilteredPss="", dd="0000",dac="0") 00092594.007 |09:07:25.236 |AppInfo  |Digit analysis: analysis results 00092594.008 |09:07:25.236 |AppInfo  ||PretransformCallingPartyNumber=999919 |CallingPartyNumber=999919 |DialingPartition= |DialingPattern=0000 Annunciator is invoked for initial announcement 00092605.001 |09:07:25.236 |AppInfo  |QueueControlCdrc(2) - get_call_info_SsCallInfoRes, huntPilotQueueProfile.alwaysplayinitialannouncement=1 00092611.001 |09:07:25.237 |AppInfo  |MediaResourceCdpc(2)::waiting_MrmAllocateAnnResourceReq - CI = 25333779 H323 Proceeding message sent out 00092612.005 |09:07:25.237 |AppInfo  |{ h323-uu-pdu { h323-message-body callProceeding : { protocolIdentifier { 0 0 8 2250 0 5 }, . . //Truncated Output Media negotiation takes place 00092634.001 |09:07:25.238 |AppInfo  |ARBTRY-ConnectionManager-wait_MediaConnectRequest(25333777,25333779) 00092674.001 |09:07:25.240 |AppInfo  |ARBTRY-ConnectionManager- wait_MediaConnectReply(25333777,25333779) Connect message is sent out instead of H323 Progress message placing the call in connected state rather than early media. The H245 messages will be exchanged post this message. 00092686.006 |09:07:25.240 |AppInfo  |SPROCRas - { h323-uu-pdu { h323-message-body connect : { protocolIdentifier { 0 0 8 2250 0 5 }, h245Address ipAddress : { ip '0A6A6F69'H, port 34408 }, . . //Truncated Output
```

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- Unified Communications Manager (CallManager)