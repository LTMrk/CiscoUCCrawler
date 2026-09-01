---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-border-element-212649-troubleshoot-cube-sp-rejects-int-f6bc578c1a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-border-element/212649-troubleshoot-cube-sp-rejects-internal-ca.html
retrieved_at: 2026-09-01T22:13:54.879444+00:00
---

Troubleshoot CUBE SP Rejects Internal Call which is Fowarded to a PSTN Number

# Troubleshoot CUBE SP Rejects Internal Call which is Fowarded to a PSTN Number

### Download Options

Updated: January 17, 2018

Document ID: 212649

Contents

## Contents

## Introduction

This document describes how to troubleshoot Cisco Unified Border Element (SP Edition) (CUBE SP) when it rejects the internal call, which is config fowarded to PSTN number.

Call Flow:  Internal IP phone 4002  calls internal IP phone 4001,  all calls on ip phone 4001 are foward to a configured PSTN number.

## Problem: Caller Hears Fast Busy Tone when Calls from IP Phone 4002 to 4001

Caller uses IP Phone 1  to call another IP Phone 2, the IP Phone 2 is configured to forwad all calls to an exteral PSTN number . the call failed to connect the PSTN Phone, PSTN phone does not ring and the caller hears fast busy tone.

## Solution

These are the steps to troubleshoot the issue.

### Step 1. Cisco Unified Communication Manager (CUCM) Log Analysis.

From CUCM logs, can see error message coming from CUBE  SP.

```
SIP/2.0 604 Does Not Exist Anywhere
```

Detail Message:

```
SIP/2.0 604 Does Not Exist Anywhere from cube SP 82645958 .001 |13:08:46.297 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.4.15.253 on port 5060 index 18491 
[19580587,NET]
INVITE sip:+612xxxxxxxx@10.x.x.x:5060 SIP/2.0
Via: SIP/2.0/TCP 10.4.15.5:5060;branch=z9hG4bK3cc7264a831cc4
From: <sip:+612xxxxxxx@10.x.x.x>;tag=8162255~9cbf8c07-9c9b-758f-e658-bebd74e53d96-40280558
To: <sip:+614xxxxxxx@10.4.15.253>
Date: Fri, 17 Nov 2017 02:08:46 GMT
Call-ID: 3cf99080-a0e144ae-3692cb-50f040a@10.x.x.x
Supported: 100rel,timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM10.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Call-Info: <sip:10.x.x.x:5060>;method="NOTIFY;Event=telephone-event;Duration=500"
Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=VIDEO_UNSPECIFIED
Cisco-Guid: 1022988416-0000065536-0000118822-0084870154
Session-Expires:  1800 Diversion: <sip:9180@10.x.x.x>;reason=unconditional;privacy=off;screen=yes P-Asserted-Identity: x <sip:+612xxxxxxxx@10.x.x.x>
Remote-Party-ID: x <sip:+612xxxxxxxxx@10.x.x.x>;party=calling;screen=yes;privacy=off
```

### Step 2. CUBE SP Log Analysis.

From CUBE SP logs, you can see that the call did not pass source number analsysis, as it does not match any entry.

inside   na-src-prefix-table

Diversion: <sip:9180@10.x.x.x>;reason=unknown;privacy=off;screen=yes

```
Routing fails.
SBC Index = 0X00000001
Config set Index = 0X0000270F
Source Account = CUCM-TL1
Source Adjacency = CUCM-cust01-1
Calling Address Type = 0X00030000
Called Address Type = 0X00030000
Calling Address = 9180
Called Address = +614xxxxxxxx
```

### Step 3. Base on Troubleshoot Step 1 and 2 Confirm it Hit Bug.

This hits the konwn bug CSCup67940

CUCM needs to send E.164 number in diversion header for extend&connect .

https://bst.cloudapps.cisco.com/bugsearch/bug/CSCup67940/?referring_site=bugquickviewredir

Workaround:

Unless we make modification in the CUBE to accept the invite from diversion header contains phone DN such as 26708 <sip:26708@58.162.59.181>;reason=unknown;privacy=off;screen=yes

## Workaround

According to the workaround, allow the number in Diversion header.

This can be done to add a new entry in this na-src-prefix-table .

```
na-src-prefix-table   xxxxx
 
     entry  10
     action accept 
     match-prefix  9
```

### New Issue after you Apply the Workaround

After you apply this workaroud, the call is successfully connected but a five digit extension number is sent to the Service Provider.

### Use SIP Header-Editor to Fix this Issue

Tested in the lab, as you use  SIP header-editor to modify Diversion header in CUBE SP, it connects the call successfully and sends e164 number to service provider.

In the lab testing,  IP Phone 4002  calls  4001, on IP phone 4001 call foward all to 60006009 ( PSTN ) number.

```
sip header-editor donnietest
    store-rule entry 1
     condition header-name Diversion header-value regex-match "sip:4\(...\)" store-as diversionuri
    header diversion entry 1
     action replace-value value "<sip:+888888884${diversionuri}@10.66.75.51>;reason=unconditional;
 
privacy=off;screen=yes"
      condition header-name Diversion header-value regex-match "sip:4\(...\)@"
  
 
 
 adjacency sip donniecucm
    editor-type editor
    header-editor inbound donnietest
```

## Verify

### No Diversion Header Modification

Without any Diversion Header modification, you can see the invite from CUCM the Diversion Header is  below

```
Diversion: <sip:4001@10.66.75.51>;reason=unconditional;privacy=off;screen=yes
INVITE sip:60006099@10.66.75.33:5068 SIP/2.0
Via: SIP/2.0/TCP 10.66.75.51:5060;branch=z9hG4bK1ef607cac8bd6
From: "agent2-4002" <sip:4002@10.66.75.51>;tag=194346~4c742393-721f-476b-82c3-bc13f8a9c6cd-22765770
To: <sip:60006099@10.66.75.33>
Date: Sun, 19 Nov 2017 23:39:16 GMT
Call-ID: d9ad6f80-a1211624-1eee8-334b420a@10.66.75.51
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Call-Info: <sip:10.66.75.51:5060>;method="NOTIFY;Event=telephone-event;Duration=500"
Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=DESKTOP
Session-ID: 223cb8ec818c0c0dd669d19baa194344;remote=00000000000000000000000000000000
Cisco-Guid: 3652022144-0000065536-0000000027-0860570122
Session-Expires:  1800
Diversion: <sip:4001@10.66.75.51>;reason=unconditional;privacy=off;screen=yes
P-Asserted-Identity: "agent2-4002" <sip:4002@10.66.75.51>
Remote-Party-ID: "agent2-4002" <sip:4002@10.66.75.51>;party=calling;screen=yes;privacy=off
Contact: <sip:4002@10.66.75.51:5060;transport=tcp>
Max-Forwards: 69
Content-Length: 0
```

### SIP Hearder-Editor Match Diversion Header

SIP header-editor match  the Diversion Header Start with sip:4xxx@ , then make it +E164 format

It can be seen after sip header-editor. In Diversion Header, 4001  has been modified to +888888884001

Diversion: <sip: +888888884001@10.66.75.51 >;reason=unconditional;privacy=off;screen=yes

MSG-6401-0027-69FECA-0747 at 01:48:38, 20 November 2017 (491542613 ms):  0X01000E2059EBD60A

A module has returned a message after editing. Editor name                    = donnietest Editor config set              = 0X00000000 This is the message after you edit.

```
INVITE sip:60006099@10.66.75.33:5068 SIP/2.0
Supported: X-cisco-srtp-fallback
Via: SIP/2.0/TCP 10.66.75.51:5060;branch=z9hG4bK1f11c18671c97
From: "agent2-4002" <sip:4002@10.66.75.51>;tag=194931~4c742393-721f-476b-82c3-bc13f8a9c6cd-22765859
To: <sip:60006099@10.66.75.33>
Date: Mon, 20 Nov 2017 02:13:12 GMT
Call-ID: 5ac33180-a1213a38-1f045-334b420a@10.66.75.51
Min-SE: 1800
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Call-Info: <sip:10.66.75.51:5060>;method="NOTIFY;Event=telephone-event;Duration=500"
Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=DESKTOP
Session-ID: 223cb8ec818c0c0dd669d19baa194929;remote=00000000000000000000000000000000
Cisco-Guid: 1522741632-0000065536-0000000050-0860570122
Session-Expires: 1800
Diversion: <sip:+888888884001@10.66.75.51>;reason=unconditional;privacy=off;screen=yes
P-Asserted-Identity: "agent2-4002" <sip:4002@10.66.75.51>
 
Remote-Party-ID: "agent2-4002" <sip:4002@10.66.75.51>;party=calling;screen=yes;privacy=off
Contact: <sip:4002@10.66.75.51:5060;transport=tcp>
Max-Forwards: 69
Content-Length: 0
```

MSG-6401-0028-69FECA-0885 at 01:48:38, 20 November 2017 (491542613 ms):  0X01000E2059EBD60A

The edits are made on the message.

This is the message after you edit

```
INVITE sip:60006099@10.66.75.33:5068 SIP/2.0
Supported: X-cisco-srtp-fallback
Via: SIP/2.0/TCP 10.66.75.51:5060;branch=z9hG4bK1f11c18671c97
From: "agent2-4002" <sip:4002@10.66.75.51>;tag=194931~4c742393-721f-476b-82c3-bc13f8a9c6cd-22765859
To: <sip:60006099@10.66.75.33>
Date: Mon, 20 Nov 2017 02:13:12 GMT
Call-ID: 5ac33180-a1213a38-1f045-334b420a@10.66.75.51
Min-SE: 1800
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Call-Info: <sip:10.66.75.51:5060>;method="NOTIFY;Event=telephone-event;Duration=500"
Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=DESKTOP
Session-ID: 223cb8ec818c0c0dd669d19baa194929;remote=00000000000000000000000000000000
Cisco-Guid: 1522741632-0000065536-0000000050-0860570122
Session-Expires: 1800
Diversion: <sip:+888888884001@10.66.75.51>;reason=unconditional;privacy=off;screen=yes
P-Asserted-Identity: "agent2-4002" <sip:4002@10.66.75.51>
Remote-Party-ID: "agent2-4002" <sip:4002@10.66.75.51>;party=calling;screen=yes;privacy=off
Contact: <sip:4002@10.66.75.51:5060;transport=tcp>
Max-Forwards: 69
Content-Length: 0
```

### Revision History

1.0

17-Jan-2018

Initial Release

### Contributed by Cisco Engineers

Mingze Yan

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Border Element

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Jan-2018 | Initial Release |