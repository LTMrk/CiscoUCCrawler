---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-211427-configure-ja-8edec1b6a2
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/211427-Configure-Jabber-Extend-and-Connect-and.html
retrieved_at: 2026-08-21T07:05:45.456190+00:00
---

Configure Jabber Extend and Connect  and Modify Calling Party Display

# Configure Jabber Extend and Connect  and Modify Calling Party Display

### Download Options

Updated: June 30, 2017

Document ID: 211427

Contents

## Contents

## Introduction

This document describes how to configure Extend and Connect feature in Jabber and modify the calling party displayed at the remote destination.

## Prerequisites

Cisco Unified Communications Manager (CUCM) 9.1 or above.

Jabber 9.1 or above.

### Requirements

Previous experience and knowledge on configuring Jabber with Cisco Unified Communications Manager and IM and Presence Server is required.

### Components Used

The information in this document is based on these software versions:

Jabber 11.8.2

Cisco Unified Communications Manager 11.0.1.10000-10

IM and Presence Server (IMP) 11.0.1.10000-6

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any configuration.

## Configure

Step 1. Configure the CTI Remote Device (CTI RD) phone profile for the same user who has Jabber already configured.

- When you configure the CTI RD, associate to the same Jabber user. The line configuration will be same as the Jabber Client Services Framework (CSF) device line

- Rerouting calling search space needs to be configured correctly for the remote destination calls to work

Step 2. Configure the remote destination.

- In this example I have used 3001 as the remote destination number. This remote destination number should be an external number (number external to the CUCM cluster where Jabber is registered, for example another telephony system)

Step 3. Associate the CTI RD profile to the end user.

Step 4. Once you login to Jabber you will see an option to set the Jabber phone services to use the Extend and Connect device (Use other number for calls). When using "Edit number" option there should be a matching route pattern for the new number.

- Once we set the Jabber to use Extend and Connect device, the phone icon will display on Jabber as below.

### Network Diagram

- Call flow for an outbound Jabber Extend and Connect call is illustrated in below image

## Troubleshooting example

In this example when the remote destination ("other number") rings, it does not have a calling party number displayed. Due to this, they cannot distinguish whether the call is from an external party or from Jabber using Extend and Connect. When using Extend and Connect, CUCM initiates the call to the remote device and does not send calling party information by default.

We can see in the following Digit Analysis excerpt for an Extend and Connect call that the CallingPartyNumber field is empty.

```
16766318.007 |19:17:23.127 |AppInfo |Digit analysis: patternUsage=5 16766318.008 |19:17:23.127 |AppInfo |Digit analysis: match(pi="1", fqcn="", cn="",plv="5", pss="test:Phones", TodFilteredPss="test:Phones", dd="3001",dac="0") 16766318.009 |19:17:23.127 |AppInfo |Digit analysis: analysis results 16766318.010 |19:17:23.127 |AppInfo ||PretransformCallingPartyNumber= | CallingPartyNumber= |DialingPartition=Phones |DialingPattern=3001 |FullyQualifiedCalledPartyNumber=3001 |DialingPatternRegularExpression=(3001) |DialingWhere= |PatternType=Enterprise |PotentialMatches=NoPotentialMatchesExist |DialingSdlProcessId=(0,0,0) |PretransformDigitString=3001 |PretransformTagsList=SUBSCRIBER |PretransformPositionalMatchList=3001 |CollectedDigits=3001 |UnconsumedDigits= |TagsList=SUBSCRIBER |PositionalMatchList=3001 |VoiceMailbox= |VoiceMailCallingSearchSpace=Global Learned E164 Numbers:Directory URI:Phones |VoiceMailPilotNumber=88800 |RouteBlockFlag=RouteThisPattern |RouteBlockCause=0 |AlertingName= |UnicodeDisplayName= |DisplayNameLocale=1 |OverlapSendingFlagEnabled=0 |WithTags=
```

In a SIP INVITE, the calling party number can be seen following the sip: tag in the From header.

In the excerpt below, it can be seen that the calling party number is not contained in the INVITE ( sip:10.66.87.195 ) and the calling party name display being sent is VoiceConnect .

```
16766935.001 |19:17:25.831 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.66.87.204 on port 5060 index 1146 [1276581,NET] INVITE sip:3001@10.66.87.204:5060;transport=tcp SIP/2.0 Via: SIP/2.0/TCP 10.66.87.195:5060;branch=z9hG4bK6dae5b551945 From: "VoiceConnect" <sip:10.66.87.195> ;tag=634549~59c9c4bc-724d-e1f0-017a-a8992d4fc521-19395629 To: <sip:3001@10.66.87.204>;tag=325889~2a8670d1-cf49-4a53-ae8f-36c41a8e75cf-23913736 Date: Thu, 18 May 2017 09:17:25 GMT Call-ID: cbe81900-91d166a3-6d704-c357420a@10.66.87.195 Supported: timer,resource-priority,replaces User-Agent: Cisco-CUCM10.5 Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY CSeq: 105 INVITE Max-Forwards: 70 Expires: 180 Allow-Events: presence Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=VIDEO_UNSPECIFIED Supported: X-cisco-srtp-fallback Supported: Geolocation Session-Expires: 1800;refresher=uas Min-SE: 1800 P-Asserted-Identity: <sip:1003@10.66.87.195> Remote-Party-ID: <sip:1003@10.66.87.195>;party=calling;screen=yes;privacy=off Contact: <sip:10.66.87.195:5060;transport=tcp> Content-Length: 0
```

To receive a calling party number on the remote device, it will need to be configured as one of the following:

- Calling Party Transform Mask on trunk configuration

- Calling Party Transform Mask on the route pattern

- Voice translation rule on the Cisco Gateway

When the trunk Direct Inward Dial (DID) number is configured on the route pattern (Calling Party Transform Mask), the Digit Analysis shows that the CallingPartyNumber field is updated.

```
16759993.008 |19:12:08.414 |AppInfo |Digit analysis: match(pi="1", fqcn="", cn="",plv="5", pss="test:Phones", TodFilteredPss="test:Phones", dd="3001",dac="0") 16759993.009 |19:12:08.414 |AppInfo |Digit analysis: analysis results 16759993.010 |19:12:08.414 |AppInfo ||PretransformCallingPartyNumber= | CallingPartyNumber=777777 |DialingPartition=Phones |DialingPattern=3001 |FullyQualifiedCalledPartyNumber=3001 |DialingPatternRegularExpression=(3001) |DialingWhere= |PatternType=Enterprise |PotentialMatches=NoPotentialMatchesExist |DialingSdlProcessId=(0,0,0) |PretransformDigitString=3001 |PretransformTagsList=SUBSCRIBER |PretransformPositionalMatchList=3001 |CollectedDigits=3001 |UnconsumedDigits= |TagsList=SUBSCRIBER |PositionalMatchList=3001 |VoiceMailbox= |VoiceMailCallingSearchSpace=Global Learned E164 Numbers:Directory URI:Phones |VoiceMailPilotNumber=88800 |RouteBlockFlag=RouteThisPattern |RouteBlockCause=0 |AlertingName= |UnicodeDisplayName= |DisplayNameLocale=1 |OverlapSendingFlagEnabled=0 |WithTags=
```

The SIP INVITE to the remote destination shows the calling party number as trunk DID. This results in the trunk DID being displayed as the calling party number when CTI RD rings.

```
16484506.001 |18:32:10.720 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.66.87.204 on port 5060 index 951 [1255331,NET] INVITE sip:3001@10.66.87.204:5060 SIP/2.0 Via: SIP/2.0/TCP 10.66.87.195:5060;branch=z9hG4bK6bd621bee81d7 From: "VoiceConnect" <sip:777777@10.66.87.195>;t ag=624206~59c9c4bc-724d-e1f0-017a-a8992d4fc521-19395539 To: <sip:3001@10.66.87.204> Date: Wed, 17 May 2017 08:32:10 GMT Call-ID: 506b6680-91c10a8a-6ba4d-c357420a@10.66.87.195 Supported: timer,resource-priority,replaces Min-SE: 1800 User-Agent: Cisco-CUCM10.5 Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY CSeq: 101 INVITE Expires: 180 Allow-Events: presence, kpml Supported: X-cisco-srtp-fallback,X-cisco-original-called Call-Info: <sip:10.66.87.195:5060>;method="NOTIFY;Event=telephone-event;Duration=500" Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=VIDEO_UNSPECIFIED Cisco-Guid: 1349215872-0000065536-0000000144-3277275658 Session-Expires: 1800 P-Asserted-Identity: "VoiceConnect" <sip:777777@10.66.87.195> Remote-Party-ID: "VoiceConnect" <sip:777777@10.66.87.195>;party=calling;screen=yes;privacy=off Contact: <sip:777777@10.66.87.195:5060;transport=tcp>;isFocus Max-Forwards: 70 Content-Length: 0
```

### Contributed by Cisco Engineers

Purna Wijenayaka

Cisco TAC

### This Document Applies to These Products

- Jabber

- Unified Communications Manager (CallManager)