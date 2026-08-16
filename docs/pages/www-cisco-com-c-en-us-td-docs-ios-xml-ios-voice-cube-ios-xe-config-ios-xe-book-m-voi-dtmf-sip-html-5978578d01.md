---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-dtmf-sip-html-5978578d01
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-dtmf-sip.html
retrieved_at: 2026-08-16T15:48:00.944699+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: DTMF Events through SIP Signaling

## Chapter: DTMF Events through SIP Signaling

# DTMF Events through SIP Signaling

The DTMF Events through SIP Signaling feature provides the following:

DTMF event notification for SIP messages.

Capability of receiving hookflash event notification through the SIP NOTIFY method.

Third-party call control, or other signaling mechanisms, to provide enhanced services, such as calling card and messaging
                              services.

Communication with the application outside of the media connection.

The DTMF Events through SIP Signaling feature allows telephone event notifications to be sent through SIP NOTIFY messages,
                        using the SIP SUBSCRIBE/NOTIFY method as defined in the Internet Engineering Task Force (IETF) draft, SIP-Specific Event Notification.

The feature also supports sending DTMF notifications based on the IETF draft: Signaled Telephony Events in the Session Initiation
                        Protocol (SIP) (draft-mahy-sip-signaled-digits-01.txt).

## Feature Information for DTMF Events through SIP Signaling

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

DTMF Events through SIP Signaling

Baseline Functionality

The DTMF Events through SIP Signaling feature provides the following:

DTMF event notification for SIP messages.

Capability of receiving hookflash event notification through the SIP NOTIFY method.

Third-party call control, or other signaling mechanisms, to provide enhanced services, such as calling card and messaging
                                                services.

Communication with the application outside of the media connection.

## Restrictions for DTMF Events through SIP Signaling

The DTMF Events through SIP Signaling feature adds support for sending telephone-event notifications via SIP NOTIFY messages
                           from a SIP gateway. The events for which notifications are sent out are DTMF events from the local Plain Old Telephone Service
                           (POTS) interface on the gateway. Notifications are not sent for DTMF events received in the Real-Time Transport Protocol (RTP)
                           stream from the recipient user agent.

## DTMF Dialing

DTMF dialing consists of simultaneous voice-band tones generated when a button is pressed on a telephone. The use of DTMF
                           signaling for this feature enables support for advanced telephony services. Currently there are a number of application servers
                           and service creation platforms that do not support media connections. To provide value-added services to the network, these
                           servers and platforms need to be aware of signaling events from a specific participant in the call. Once the server or platform
                           is aware of the DTMF events that are being signaled, it can use third-party call control, or other signaling mechanisms, to
                           provide enhanced services. Examples of the types of services and platforms that are supported by this feature are various
                           voice web browser services, Centrex switches or business service platforms, calling card services, and unified message servers.
                           All of these applications require a method for the user to communicate with the application outside of the media connection.
                           The DTMF Events Through SIP Signaling feature provides this signaling capability.

This feature is related to the SIP INFO Method for DTMF Tone Generation feature, which adds support for out-of-band DTMF tone
                           generation using the SIP INFO method. Together the two features provide a mechanism to both send and receive DTMF digits along
                           the signaling path.

## NOTIFY Messages

The SIP event notification mechanism uses NOTIFY messages to signal
                           		when certain telephony events take place. In order to send DTMF signals through
                           		NOTIFY messages, the gateway notifies the subscriber when DTMF digits are
                           		signaled by the originator. The notification contains a message body with a SIP
                           		response status line.

The following sample message shows a NOTIFY message from the Notifier
                           		letting the Subscriber know that the subscription is completed. The combination
                           		of the From, To, and Call-ID headers identifies the call leg. The Events header
                           		specifies the event type being signaled, and the Content-Type specifies the
                           		Internet media type. The Content-Length header indicates the number of octets
                           		in the message body.

```
NOTIFY sip:subscriber@example1.com SIP/2.0
Via: SIP/2.0/UDP example2.com:5060
From: Notifier <sip:notifier@example2.com>;tag=5678-EFGH
To: Subscriber <sip:subscriber@example1.com>;tag=1234-ABCD
Call-ID: 12345@example2.com
CSeq: 104 NOTIFY
Contact: Notifier <sip:notifier@example2.com>
Events: telephone-event;rate=1000
Content-Type: audio/telephone-event
Content-Length: 4
```

## Configure DTMF Events through SIP Signaling

To configure the DTMF Events through SIP Signaling feature, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- timers notify number

- retry notify number

- exit

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enters privileged EXEC mode or any other security level set by a system administrator.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

sip-ua

### Example:

```
Device(config)# sip-ua
```

Enters SIP user-agent configuration mode.

Step 4

timers notify number

### Example:

```
Device(config-sip-ua)# timers notify 100
```

Sets the amount of time that the user agent waits before retransmitting the Notify message. The argument is as follows:

number –Time, in milliseconds, to wait before retransmitting. Range: 100 to 1000. Default: 500.

Step 5

retry notify number

### Example:

```
Device(config-sip-ua)# retry notify 6
```

Sets the number of times that the Notify message is retransmitted to the user agent that initiated the transfer or Refer request.
                                          The argument is as follows:

number –Number of retries. Range: 1 to 10. Default: 10.

Step 6

exit

### Example:

```
Device(config-sip-ua)# exit
```

Exits the current mode.

### Verifying SIP DTMF Support

To verify SIP DTMF support, perform the following steps as appropriate (commands are listed in alphabetical order).

### SUMMARY STEPS

- show running-config

- show sip-ua retry

- show sip-ua statistics

- show sip-ua status

- show sip-ua timers

- show voip rtp connections

- show sip-ua calls

### DETAILED STEPS

Step 1

show running-config

Use this command to show dial-peer configurations.

The following sample output shows that the dtmf-relay sip-notify command is configured in dial peer 123:

#### Example:

```
Device# show running-config .
.
.
dial-peer voice 123 voip
 destination-pattern [12]...
 monitor probe icmp-ping
 session protocol sipv2
 session target ipv4:10.8.17.42
 dtmf-relay sip-notify
```

The following sample output shows that DTMF relay and NTE are configured on the dial peer.

#### Example:

```
Device# show running-config !
dial-peer voice 1000 pots
 destination-pattern 4961234
 port 1/0/0
!
dial-peer voice 2000 voip
 application session
 destination-pattern 4965678
 session protocol sipv2
 session target ipv4:192.0.2.34
 dtmf-relay rtp-nte
! RTP payload type value = 101 (default)
!
dial-peer voice 3000 voip
 application session
 destination-pattern 2021010101
 session protocol sipv2
 session target ipv4:192.0.2.34
 dtmf-relay rtp-nte
 rtp payload-type nte 110
! RTP payload type value = 110 (user assigned)
!
```

Step 2

show sip-ua retry

Use this command to display SIP retry statistics.

#### Example:

```
Device# show sip-ua retry SIP UA Retry Values
invite retry count = 6 response retry count = 1
bye retry count = 1 cancel retry count = 1
prack retry count = 10 comet retry count = 10
reliable 1xx count = 6 notify retry count = 10
```

Step 3

show sip-ua statistics

Use this command to display response, traffic, and retry SIP statistics.

Tip

To reset counters for the show sip-ua statistics display, use the clear sip-ua statistics command.

#### Example:

```
Device# show sip-ua statistics SIP Response Statistics (Inbound/Outbound)
Informational:
Trying 4/2, Ringing 2/1,
Forwarded 0/0, Queued 0/0,
SessionProgress 0/0
Success:
OkInvite 1/2, OkBye 0/1,
OkCancel 1/0, OkOptions 0/0,
OkPrack 2/0, OkPreconditionMet 0/0,
OkNotify 1/0, 202Accepted 0/1
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
Ambiguous 0/0, BusyHere 0/0
RequestCancel 1/0, NotAcceptableMedia 0/0
Server Error:
InternalError 0/1, NotImplemented 0/0,
BadGateway 0/0, ServiceUnavail 0/0,
GatewayTimeout 0/0, BadSipVer 0/0,
PreCondFailure 0/0
Global Failure:
BusyEverywhere 0/0, Decline 0/0,
NotExistAnywhere 0/0, NotAcceptable 0/0
SIP Total Traffic Statistics (Inbound/Outbound) /* Traffic Statistics
Invite 3/2, Ack 3/2, Bye 1/0,
Cancel 0/1, Options 0/0,
Prack 0/2, Comet 0/0,
Notify 0/1, Refer 1/0
Retry Statistics 							/* Retry Statistics
Invite 0, Bye 0, Cancel 0, Response 0,
Prack 0, Comet 0, Reliable1xx 0, Notify 0
```

Following is sample output verifying configuration of the SIP INFO Method for DTMF Tone Generation feature:

#### Example:

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

Step 4

show sip-ua status

Use this command to display status for the SIP user agent.

#### Example:

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

The following sample output shows that the time interval between consecutive NOTIFY messages for a telephone event is the
                                             default of 2000 ms:

#### Example:

```
Device# show sip-ua status SIP User Agent Status
SIP User Agent for UDP : ENABLED
SIP User Agent for TCP : ENABLED
SIP User Agent bind status(signaling): DISABLED
SIP User Agent bind status(media): DISABLED
SIP early-media for 180 responses with SDP: ENABLED
SIP max-forwards : 6
SIP DNS SRV version: 2 (rfc 2782)
NAT Settings for the SIP-UA
Role in SDP: NONE
Check media source packets: DISABLED
Maximum duration for a telephone-event in NOTIFYs: 2000 ms
SIP support for ISDN SUSPEND/RESUME: ENABLED
Redirection (3xx) message handling: ENABLED
 SDP application configuration:
 Version line (v=) required
 Owner line (o=) required
 Timespec line (t=) required
 Media supported: audio image
 Network types supported: IN
 Address types supported: IP4
 Transport types supported: RTP/AVP udptl
```

The following sample output shows configuration of the SIP INFO Method for DTMF Tone Generation feature:

#### Example:

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

Step 5

show sip-ua timers

Use this command to display the current settings for SIP user-agent timers.

#### Example:

```
Device# show sip-ua timers SIP UA Timer Values (millisecs)
trying 500, expires 300000, connect 500, disconnect 500
comet 500, prack 500, rel1xx 500, notify 500
```

Step 6

show voip rtp connections

Use this command to show local and remote Calling ID and IP address and port information.

Step 7

show sip-ua calls

Use this command to ensure the DTMF method is SIP-KPML.

The following sample output shows that the DTMF method is SIP-KPML.

#### Example:

```
Device# show sip-ua calls SIP UAC CALL INFO
Call 1
SIP Call ID                : 57633F68-2BE011D6-8013D46B-B4F9B5F6@172.18.193.251
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 
   Called Number           : 8888
   Bit Flags               : 0xD44018 0x100 0x0
   CC Call ID              : 6
   Source IP Address (Sig ): 192.0.2.1
   Destn SIP Req Addr:Port : 192.0.2.2:5060
   Destn SIP Resp Addr:Port: 192.0.2.3:5060
   Destination Name        : 192.0.2.4.250
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 6
     Stream Type              : voice-only (0)
     Negotiated Codec         : g711ulaw (160 bytes)
	Codec Payload Type       : 0 
     Negotiated Dtmf-relay    : sip-kpml
     Dtmf-relay Payload Type  : 0
     Media Source IP Addr:Port: 192.0.2.5:17576
     Media Dest IP Addr:Port  : 192.0.2.6:17468
     Orig Media Dest IP Addr:Port : 0.0.0.0:0
   Number of SIP User Agent Client(UAC) calls: 1
SIP UAS CALL INFO
   Number of SIP User Agent Server(UAS) calls: 0
```

## Troubleshooting Tips

To enable debugging for RTP named-event packets, use the debug voip rtp command.

To enable KPML debugs, use the debug kpml command.

To enable SIP debugs, use the debug ccsip command.

Collect debugs while the call is being established and during digit presses.

If an established call is not sending digits through KPML, use the show sip-ua calls command to ensure SIP-KPML is included in the negotiation process.

| Feature Name | Releases | Feature Information |
|---|---|---|
| DTMF Events through SIP Signaling | Baseline Functionality | The DTMF Events through SIP Signaling feature provides the following: DTMF event notification for SIP messages. Capability of receiving hookflash event notification through the SIP NOTIFY method. Third-party call control, or other signaling mechanisms, to provide enhanced services, such as calling card and messaging
                                                services. Communication with the application outside of the media connection. The following commands were introduced or modified: timers notify , and retry notify |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enters privileged EXEC mode or any other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | sip-ua Example: Device(config)# sip-ua | Enters SIP user-agent configuration mode. |
| Step 4 | timers notify number Example: Device(config-sip-ua)# timers notify 100 | Sets the amount of time that the user agent waits before retransmitting the Notify message. The argument is as follows: number –Time, in milliseconds, to wait before retransmitting. Range: 100 to 1000. Default: 500. |
| Step 5 | retry notify number Example: Device(config-sip-ua)# retry notify 6 | Sets the number of times that the Notify message is retransmitted to the user agent that initiated the transfer or Refer request.
                                          The argument is as follows: number –Number of retries. Range: 1 to 10. Default: 10. |
| Step 6 | exit Example: Device(config-sip-ua)# exit | Exits the current mode. |

| Step 1 | show running-config Use this command to show dial-peer configurations. The following sample output shows that the dtmf-relay sip-notify command is configured in dial peer 123: Example: Device# show running-config .
.
.
dial-peer voice 123 voip
 destination-pattern [12]...
 monitor probe icmp-ping
 session protocol sipv2
 session target ipv4:10.8.17.42
 dtmf-relay sip-notify The following sample output shows that DTMF relay and NTE are configured on the dial peer. Example: Device# show running-config !
dial-peer voice 1000 pots
 destination-pattern 4961234
 port 1/0/0
!
dial-peer voice 2000 voip
 application session
 destination-pattern 4965678
 session protocol sipv2
 session target ipv4:192.0.2.34
 dtmf-relay rtp-nte
! RTP payload type value = 101 (default)
!
dial-peer voice 3000 voip
 application session
 destination-pattern 2021010101
 session protocol sipv2
 session target ipv4:192.0.2.34
 dtmf-relay rtp-nte
 rtp payload-type nte 110
! RTP payload type value = 110 (user assigned)
! |
|---|---|
| Step 2 | show sip-ua retry Use this command to display SIP retry statistics. Example: Device# show sip-ua retry SIP UA Retry Values
invite retry count = 6 response retry count = 1
bye retry count = 1 cancel retry count = 1
prack retry count = 10 comet retry count = 10
reliable 1xx count = 6 notify retry count = 10 |
| Step 3 | show sip-ua statistics Use this command to display response, traffic, and retry SIP statistics. Tip To reset counters for the show sip-ua statistics display, use the clear sip-ua statistics command. Example: Device# show sip-ua statistics SIP Response Statistics (Inbound/Outbound)
Informational:
Trying 4/2, Ringing 2/1,
Forwarded 0/0, Queued 0/0,
SessionProgress 0/0
Success:
OkInvite 1/2, OkBye 0/1,
OkCancel 1/0, OkOptions 0/0,
OkPrack 2/0, OkPreconditionMet 0/0,
OkNotify 1/0, 202Accepted 0/1
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
Ambiguous 0/0, BusyHere 0/0
RequestCancel 1/0, NotAcceptableMedia 0/0
Server Error:
InternalError 0/1, NotImplemented 0/0,
BadGateway 0/0, ServiceUnavail 0/0,
GatewayTimeout 0/0, BadSipVer 0/0,
PreCondFailure 0/0
Global Failure:
BusyEverywhere 0/0, Decline 0/0,
NotExistAnywhere 0/0, NotAcceptable 0/0
SIP Total Traffic Statistics (Inbound/Outbound) /* Traffic Statistics
Invite 3/2, Ack 3/2, Bye 1/0,
Cancel 0/1, Options 0/0,
Prack 0/2, Comet 0/0,
Notify 0/1, Refer 1/0
Retry Statistics 							/* Retry Statistics
Invite 0, Bye 0, Cancel 0, Response 0,
Prack 0, Comet 0, Reliable1xx 0, Notify 0 Following is sample output verifying configuration of the SIP INFO Method for DTMF Tone Generation feature: Example: Device# show sip-ua statistics SIP Response Statistics (Inbound/Outbound)
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
Invite 0, Bye 0, Cancel 0, Response 0, Notify 0 | Tip | To reset counters for the show sip-ua statistics display, use the clear sip-ua statistics command. |
| Tip | To reset counters for the show sip-ua statistics display, use the clear sip-ua statistics command. |
| Step 4 | show sip-ua status Use this command to display status for the SIP user agent. Example: Device# show sip-ua status SIP User Agent Status
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
 Transport types supported: RTP/AVP udptl The following sample output shows that the time interval between consecutive NOTIFY messages for a telephone event is the
                                             default of 2000 ms: Example: Device# show sip-ua status SIP User Agent Status
SIP User Agent for UDP : ENABLED
SIP User Agent for TCP : ENABLED
SIP User Agent bind status(signaling): DISABLED
SIP User Agent bind status(media): DISABLED
SIP early-media for 180 responses with SDP: ENABLED
SIP max-forwards : 6
SIP DNS SRV version: 2 (rfc 2782)
NAT Settings for the SIP-UA
Role in SDP: NONE
Check media source packets: DISABLED
Maximum duration for a telephone-event in NOTIFYs: 2000 ms
SIP support for ISDN SUSPEND/RESUME: ENABLED
Redirection (3xx) message handling: ENABLED
 SDP application configuration:
 Version line (v=) required
 Owner line (o=) required
 Timespec line (t=) required
 Media supported: audio image
 Network types supported: IN
 Address types supported: IP4
 Transport types supported: RTP/AVP udptl The following sample output shows configuration of the SIP INFO Method for DTMF Tone Generation feature: Example: Device# show sip-ua status SIP User Agent Status
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
 Transport types supported: RTP/AVP udptl |
| Step 5 | show sip-ua timers Use this command to display the current settings for SIP user-agent timers. Example: Device# show sip-ua timers SIP UA Timer Values (millisecs)
trying 500, expires 300000, connect 500, disconnect 500
comet 500, prack 500, rel1xx 500, notify 500 |
| Step 6 | show voip rtp connections Use this command to show local and remote Calling ID and IP address and port information. |
| Step 7 | show sip-ua calls Use this command to ensure the DTMF method is SIP-KPML. The following sample output shows that the DTMF method is SIP-KPML. Example: Device# show sip-ua calls SIP UAC CALL INFO
Call 1
SIP Call ID                : 57633F68-2BE011D6-8013D46B-B4F9B5F6@172.18.193.251
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 
   Called Number           : 8888
   Bit Flags               : 0xD44018 0x100 0x0
   CC Call ID              : 6
   Source IP Address (Sig ): 192.0.2.1
   Destn SIP Req Addr:Port : 192.0.2.2:5060
   Destn SIP Resp Addr:Port: 192.0.2.3:5060
   Destination Name        : 192.0.2.4.250
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 6
     Stream Type              : voice-only (0)
     Negotiated Codec         : g711ulaw (160 bytes)
	Codec Payload Type       : 0 
     Negotiated Dtmf-relay    : sip-kpml
     Dtmf-relay Payload Type  : 0
     Media Source IP Addr:Port: 192.0.2.5:17576
     Media Dest IP Addr:Port  : 192.0.2.6:17468
     Orig Media Dest IP Addr:Port : 0.0.0.0:0
   Number of SIP User Agent Client(UAC) calls: 1
SIP UAS CALL INFO
   Number of SIP User Agent Server(UAS) calls: 0 |

| Tip | To reset counters for the show sip-ua statistics display, use the clear sip-ua statistics command. |
|---|---|