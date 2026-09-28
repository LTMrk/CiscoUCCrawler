---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-dtmf-ton-gen-html-046ea9df6e
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-dtmf-ton-gen.html
retrieved_at: 2026-08-16T15:47:56.492130+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP  INFO Method for DTMF Tone Generation

## Chapter: SIP  INFO Method for DTMF Tone Generation

# SIP  INFO Method for DTMF Tone Generation

The SIP: INFO Method for DTMF Tone Generation feature uses the Session Initiation Protocol (SIP) INFO method to generate dual
                        tone multifrequency (DTMF) tones on the telephony call leg. SIP info methods, or request message types, request a specific
                        action be taken by another user agent (UA) or proxy server. The SIP INFO message is sent along the signaling path of the call.
                        Upon receipt of a SIP INFO message with DTMF relay content, the gateway generates the specified DTMF tone on the telephony
                        end of the call.

## Feature Information for SIP INFO Method for DTMF Tone Generation

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP: INFO Method for DTMF Tone Generation

Baseline Functionality

The SIP: INFO Method for DTMF Tone Generation feature uses the Session Initiation Protocol (SIP) INFO method to generate dual-tone
                                          multifrequency (DTMF) tones on the telephony call leg. SIP methods, or request message types, request a specific action be
                                          taken by another user agent (UA) or proxy server. The SIP INFO message is sent along the signaling path of the call.

The following command was introduced: show sip-ua

## Prerequisites for SIP INFO Method for DTMF Tone Generation

You cannot configure, enable, or disable this feature. No configuration tasks are required to configure the SIP - INFO Method
                           for DTMF Tone Generation feature. The feature is enabled by default.

## Restrictions for SIP INFO Methods for DTMF Tone Generation

The SIP: INFO Method for DTMF Tone Generation feature includes the following signal duration parameters:

Minimum signal duration is 100 milliseconds (ms). If a request is received with a duration less than 100 ms, the minimum
                                 duration of 100 ms is used by default.

Maximum signal duration is 5000 ms. If a request is received with a duration longer than 5000 ms, the maximum duration of
                                 5000 ms is used by default.

If no duration parameter is included in a request, the gateway defaults to a signal duration of 250 ms.

## Information About SIP INFO Method for DTMF Tone Generation

The SIP: INFO Method for DTMF Tone Generation feature is always enabled, and is invoked when a SIP INFO message is received
                           with DTMF relay content. This feature is related to the DTMF Events Through SIP Signaling feature, which allows an application
                           to be notified about DTMF events using SIP NOTIFY messages. Together, the two features provide a mechanism to both send and
                           receive DTMF digits along the signaling path. For more information on sending DTMF event notification using SIP NOTIFY messages,
                           refer to the DTMF Events Through SIP Signaling feature.

## How to Review SIP INFO Messages

The SIP INFO method is used by a UA to send call signaling information to another UA with which it has an established media
                           session. The following example shows a SIP INFO message with DTMF content:

```
INFO sip:2143302100@172.17.2.33 SIP/2.0
Via: SIP/2.0/UDP 172.80.2.100:5060
From:  <sip:9724401003@172.80.2.100>;tag=43
To:  <sip:2143302100@172.17.2.33>;tag=9753.0207
Call-ID: 984072_15401962@172.80.2.100
CSeq: 25634 INFO
Supported: 100rel
Supported: timer
Content-Length: 26
Content-Type: application/dtmf-relay
Signal= 1
Duration= 160
```

This sample message shows a SIP INFO message received by the gateway with specifics about the DTMF tone to be generated. The
                           combination of the "From", "To", and "Call-ID" headers identifies the call leg. The signal and duration headers specify the
                           digit, in this case 1, and duration, 160 milliseconds in the example, for DTMF tone play.

## Configure for SIP INFO Method for DTMF Tone Generation

You cannot configure, enable, or disable this feature. No configuration tasks are required to configure the SIP - INFO Method
                           for DTMF Tone Generation feature. The feature is enabled by default.

## Troubleshooting Tips

You can display SIP statistics, including SIP INFO method statistics, by using the show sip-ua statistics and show sip-ua status commands in privileged EXEC mode. See the following fields for SIP INFO method statistics:

OkInfo 0/0, under SIP Response Statistics, Success, displays the number of successful responses to an INFO request.

Info 0/0, under SIP Total Traffic Statistics, displays the number of INFO messages received and sent by the gateway.

The following is sample output from the show sip-ua statistics command:

```
Device# show sip-ua statistics SIP Response Statistics (Inbound/Outbound)
Informational:
Trying 1/1, Ringing 0/0,
Forwarded 0/0, Queued 0/0,
SessionProgress 0/1
Success:
OkInvite 0/1, OkBye 1/0,
OkCancel 0/0, OkOptions 0/0,
OkPrack 0/0, OkPreconditionMet 0/0
OkSubscibe 0/0, OkNotify 0/0,
OkInfo 0/0, 202Accepted 0/0
Redirection (Inbound only):
MultipleChoice 0, MovedPermanently 0,
MovedTemporarily 0, SeeOther 0,
UseProxy 0, AlternateService 0
Client Error:
BadRequest 0/0, Unauthorized 0/0,
PaymentRequired 0/0, Forbidden 0/0,
NotFound 0/0, MethodNotAllowed 0/0,
NotAcceptable 0/0, ProxyAuthReqd 0/0,
ReqTimeout 0/0, Conflict 0/0, Gone 0/0,
LengthRequired 0/0, ReqEntityTooLarge 0/0,
ReqURITooLarge 0/0, UnsupportedMediaType 0/0,
BadExtension 0/0, TempNotAvailable 0/0,
CallLegNonExistent 0/0, LoopDetected 0/0,
TooManyHops 0/0, AddrIncomplete 0/0,
Ambiguous 0/0, BusyHere 0/0,
BadEvent 0/0
Server Error:
InternalError 0/0, NotImplemented 0/0,
BadGateway 0/0, ServiceUnavail 0/0,
GatewayTimeout 0/0, BadSipVer 0/0
Global Failure:
BusyEverywhere 0/0, Decline 0/0,
NotExistAnywhere 0/0, NotAcceptable 0/0
SIP Total Traffic Statistics (Inbound/Outbound)
    Invite 0/0, Ack 0/0, Bye 0/0,
    Cancel 0/0, Options 0/0,
    Prack 0/0, Comet 0/0,
    Subscribe 0/0, Notify 0/0,
    Refer 0/0, Info 0/0
Retry Statistics
Invite 0, Bye 0, Cancel 0, Response 0, Notify 0
```

The following is sample output from the show sip-ua status command:

```
Device# show sip-ua status SIP User Agent Status 
SIP User Agent for UDP : ENABLED 
SIP User Agent for TCP : ENABLED 
SIP User Agent bind status(signaling): DISABLED 
SIP User Agent bind status(media): DISABLED 
SIP max-forwards : 6 
SIP DNS SRV version: 2 (rfc 2782) 
SDP application configuration: 
 Version line (v=) required 
 Owner line (o=) required 
 Session name line (s=) required 
 Timespec line (t=) required 
 Media supported: audio image 
 Network types supported: IN 
 Address types supported: IP4 
 Transport types supported: RTP/AVP udptl
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP: INFO Method for DTMF Tone Generation | Baseline Functionality | The SIP: INFO Method for DTMF Tone Generation feature uses the Session Initiation Protocol (SIP) INFO method to generate dual-tone
                                          multifrequency (DTMF) tones on the telephony call leg. SIP methods, or request message types, request a specific action be
                                          taken by another user agent (UA) or proxy server. The SIP INFO message is sent along the signaling path of the call. The following command was introduced: show sip-ua |