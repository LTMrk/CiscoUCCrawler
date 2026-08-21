---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-221643-troubleshoot-pdd-in-webex-calling-with-p-233776776e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/221643-troubleshoot-pdd-in-webex-calling-with-p.html
retrieved_at: 2026-08-21T07:16:40.074972+00:00
---

Troubleshoot PDD in Webex Calling with Premises Based PSTN

# Troubleshoot PDD in Webex Calling with Premises Based PSTN

### Download Options

Updated: February 6, 2024

Document ID: 221643

Contents

## Contents

## Introduction

This document describes how to troubleshoot a call failure when PSTN provider takes more than 12 seconds to answer with the Ringing.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Basic SIP.

- Access to a Cisco Local Gateway.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Post Dial Delay ( PDD ), which refers to the duration it takes for a caller to hear a ring back tone after the initiation of a call. This delay typically corresponds to the time it takes to receive either a 180 Ringing or 183 Session Progress response to a SIP Invite.

On occasions, users have reported experiences such as dead air or dropped calls, as the caller does not hear any response after dialing, confusion ensues.

In the context of Webex calling with Local Gateway, if the PSTN provider exceeds a Post Dial Delay of 12 seconds, the call is automatically canceled from the Webex Calling side.

## Get the logs from LGW

The steps to get the logs from the Local Gateway are the next:

Step 1. Log in to Local Gateway using Putty.

Step 2. Enable debug in Local Gateway.

gw-wxc# conf t

lgw-wxc(config)# no logging console

lgw-wxc(config)# no logging monitor

lgw-wxc(config)# no logging rate-limit

lgw-wxc(config)# no logging queue-limit

lgw-wxc(config)# logging buffer 400000000 debug

lgw-wxc(config)# end

lgw-wxc# clear log

lgw-wxc# debug ccsip messages. ===>> SIP Call messages tracing is enabled

lgw-wxc# debug voice ccapi inout ===>> voip ccapi in/out debugging is on

Step 3. Start recording the Putty session.

Go to Settings > Session > Logging and set:

Session logging: Select All session output.

Log file Name: Select Browse and select the directory where you want to save the file and the name.

Start Recording

Step 4. A ttempt to recreate or reproduce the outgoing call to PSTN.

Step 5. Get the output of the logs.

lgw-wxc# Terminal length 0

lgw-wxc# sh log

Step 6. Stop recording Putty session and Save the file.

Go to Settings > Session > Logging and Set:

Session logging: None.

Stop Recording

Step 7. Stop the debugs.

lgw-wxc# Undebug all

## Troubleshoot the LGW Logs

Step 1. Open the log you took using a text plain program like Notepad.

Step 2. Look the Invite coming from Webex Calling, in the next example you can see the Invite arrives at 12:09:48.

```
125670: *Jul 21 12:09:48.231 : //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg: Received: INVITE sip:+1XXXXXXXXXX@XX.XX.XX.XX:5061;transport=tls;dtg=sbc_lgu SIP/2.0 Via:SIP/2.0/TLS XXX.XXX.XX.XX:8934;branch=z9hG4bKBroadworksSSE.-XXX.X.XXX.XXV40413-0-100-1704852021-1689966652299- From:<sip:+1XXXXXXXXXX0@XXX.XXX.XX.XX;user=phone>;tag=1704852021-1689966652299- To:<sip:+1XXXXXXXXXX@XXXXXXXX.cisco-bcld.com;user=phone> Call-ID:SSE191052299210723-1072365917@XXX.XXX.XX.XX CSeq:100 INVITE Contact:<sip:XXX.XXX.XX.XX:8934;transport=tls> P-Asserted-Identity:<sip:+1XXXXXXXXXX@XX.XX.XXX.XXX;user=phone> Privacy:none P-Access-Network-Info:6307694336 Allow:ACK,BYE,CANCEL,INFO,INVITE,OPTIONS,PRACK,REFER,NOTIFY,UPDATE Recv-Info:x-broadworks-client-session-info,x-cisco-mute-status X-BroadWorks-Correlation-Info:64b1f41c-5b24-4865-9b00-c5a9acd0c1d8 Accept:application/media_control+xml,application/sdp,multipart/mixed Supported: Max-Forwards:69 Session-ID:7202892d00105000a000ac7e8ab6b729;remote=00000000000000000000000000000000 Content-Type:application/sdp Content-Length:2260
```

Step 3. Look the Invite is sent immediately to PSTN Provider at 12:09:48.

```
125749: *Jul 21 12:09:48.238 : //2058481/FED4647C9552/SIP/Msg/ccsipDisplayMsg: Sent: INVITE sip:+1XXXXXXXXXX@XXX.X.XXX.XX:5060 SIP/2.0 Via: SIP/2.0/UDP XXX.X.XXX.XX:5060;branch=z9hG4bK11B7E01FDE Remote-Party-ID: <sip:+1XXXXXXXXXX@XXX.X.XXX.XX>;party=calling;screen=yes;privacy=off From: <sip:+1XXXXXXXXXX@XXX.X.XXX.XX>;tag=91790161-DA8 To: <sip:+1XXXXXXXXXX@XXX.X.XXX.XX> Date: Fri, 21 Jul 2023 19:09:48 GMT Call-ID: FED527FA-273011EE-9558C2C2-D591E4CC@XXX.X.XXX.XX Supported: 100rel,timer,resource-priority,replaces,sdp-anat Min-SE: 1800 Cisco-Guid: 4275332220-0657461742-2505228994-3583108300 User-Agent: Cisco-SIPGateway/Cisco IOS 16.12.5 Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER CSeq: 101 INVITE Timestamp: 1689966588 Contact: <sip:+1XXXXXXXXXX@XXX.X.XXX.XX:5060> Expires: 180 Allow-Events: telephone-event Max-Forwards: 68 Session-ID: 7202892d00105000a000ac7e8ab6b729;remote=00000000000000000000000000000000 Session-Expires: 1800 Content-Type: application/sdp Content-Disposition: session;handling=required Content-Length: 666
```

Step 4. After 12 seconds at 12:10:00 you can see Webex Calling send to Local Gateway a Cancel.

```
125757: *Jul 21 12:10:00.218 : //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg: Received: CANCEL sip:+1XXXXXXXXXX@XXX.X.XXX.XX:5061;transport=tls;dtg=sbc_lgu SIP/2.0 Via:SIP/2.0/TLS XXX.XXX.XX.XX:8934;branch=z9hG4bKBroadworksSSE.-XXX.X.XXX.XXV40413-0-100-1704852021-1689966652299- From:<sip:+1XXXXXXXXXX@XXX.XXX.XX.XX;user=phone>;tag=1704852021-1689966652299- To:<sip:+1XXXXXXXXXX@XXXXXX.cisco-bcld.com;user=phone> Call-ID:SSE191052299210723-1072365917@XXX.XXX.XX.XX CSeq:100 CANCEL X-BroadWorks-Correlation-Info:64b1f41c-5b24-4865-9b00-c5a9acd0c1d8 Max-Forwards:69 Session-ID:7202892d00105000a000ac7e8ab6b729;remote=00000000000000000000000000000000 Content-Length:0
```

Step 5. In this instance, it is crucial to open a Webex Calling case to extend the PDD beyond 12 seconds. Include the Local Gateway trace for further analysis.

Step 6. This is the graphics trace of the call.

Trace

## Related Information

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

07-Feb-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Feb-2024 | Initial Release |