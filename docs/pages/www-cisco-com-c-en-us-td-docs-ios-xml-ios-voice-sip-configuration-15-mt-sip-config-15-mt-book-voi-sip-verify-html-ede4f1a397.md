---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-sip-configuration-15-mt-sip-config-15-mt-book-voi-sip-verify-html-ede4f1a397
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/sip/configuration/15-mt/sip-config-15-mt-book/voi-sip-verify.html
retrieved_at: 2026-08-20T23:46:10.286658+00:00
---

SIP Configuration Guide, Cisco IOS Release 15M&T

# SIP Configuration Guide, Cisco IOS Release 15M&T

Updated: November 25, 2014

Chapter: Verifying and Troubleshooting SIP Features

## Chapter: Verifying and Troubleshooting SIP Features

# Verifying and Troubleshooting SIP Features

## Basic Troubleshooting Procedures

Cisco routers provide numerous integrated commands to assist you in monitoring and troubleshooting your internetwork:

show commands help you monitor installation behavior and normal network behavior, and isolate problem areas.

debug commands help you isolate protocol and configuration problems.

ping commands help you determine connectivity between devices on your network.

trace commands provide a method of determining the route by which packets reach their destination.

This chapter discusses use of show and debug commands.

Under moderate traffic loads, debug commands produce a high volume of output. We therefore recommend that, as a general rule, you use show commands first and use debug commands with caution.

Generally, you should proceed as follows:

Determine whether or not VoIP is working.

Determine whether or not you can make a voice call.

Verify that SIP-supported codecs are used. Support for codecs varies on different platforms; use the codec ? command to determine the codecs available on a specific platform.

Isolate and reproduce the failure.

Collect relevant information from show and debug commands, configuration files, and protocol analyzers.

Identify the first indication of failure in protocol traces or internal debug command output.

Look for the cause in configuration files.

General troubleshooting of problems affecting basic functionality such as dial peers, digit translation, and IP connectivity
                                       is beyond the scope of this chapter. For links to additional troubleshooting help, see "Additional References".

## Using show Commands

To verify SIP gateway status and configuration, perform the following steps as appropriate (commands are listed in alphabetical
                              order).

### SUMMARY STEPS

- show sip service

- show sip-ua register status

- show sip-ua statistics

- show sip-ua status

- show sip-ua timers

### DETAILED STEPS

show sip service

Use this command to display the status of SIP call service on a SIP gateway.

The following sample output shows that SIP call service is enabled:

### Example:

```
Router# show sip service SIP Service is up
```

The following sample output shows that SIP call service was shut down with the shutdown command:

### Example:

```
Router# show sip service SIP service is shut globally
under 'voice service voip'
```

The following sample output shows that SIP call service was shut down with the call service stop command:

### Example:

```
Router# show sip service SIP service is shut
under 'voice service voip', 'sip' submode
```

The following sample output shows that SIP call service was shut down with the shutdown forced command:

### Example:

```
Router# show sip service SIP service is forced shut globally
under 'voice service voip'
```

The following sample output shows that SIP call service was shut down with the call service stop forced command:

### Example:

```
Router# show sip service SIP service is forced shut
under 'voice service voip', 'sip' submode
```

show sip-ua register status

Use this command to display the status of E.164 numbers that a SIP gateway has registered with an external primary SIP registrar.

### Example:

```
Router# show sip-ua register status Line peer expires(sec) registered
4001 20001 596          no
4002 20002 596          no
5100 1     596          no
9998 2     596          no
```

show sip-ua statistics

Use this command to display response, traffic, and retry SIP statistics, including whether call redirection is disabled.

The following sample shows that four registers were sent:

### Example:

```
Router# show sip-ua statistics SIP Response Statistics (Inbound/Outbound)
    Informational:
      Trying 0/0, Ringing 0/0,
      Forwarded 0/0, Queued 0/0,
      SessionProgress 0/0
     Success:
      OkInvite 0/0, OkBye 0/0,
      OkCancel 0/0, OkOptions 0/0,
      OkPrack 0/0, OkPreconditionMet 0/0,
      OkSubscribe 0/0, OkNOTIFY 0/0,
      OkInfo 0/0, 202Accepted 0/0
      OkRegister 12/49
     Redirection (Inbound only except for MovedTemp(Inbound/Outbound)) :
      MultipleChoice 0, MovedPermanently 0,
      MovedTemporarily 0/0, UseProxy 0,
      AlternateService 0
      Client Error:
      BadRequest 0/0, Unauthorized 0/0,
      PaymentRequired 0/0, Forbidden 0/0,
      NotFound 0/0, MethodNotAllowed 0/0,
      NotAcceptable 0/0, ProxyAuthReqd 0/0,
      ReqTimeout 0/0, Conflict 0/0, Gone 0/0,
      ReqEntityTooLarge 0/0, ReqURITooLarge 0/0,
      UnsupportedMediaType 0/0, BadExtension 0/0,
      TempNotAvailable 0/0, CallLegNonExistent 0/0,
      LoopDetected 0/0, TooManyHops 0/0,
      AddrIncomplete 0/0, Ambiguous 0/0,
      BusyHere 0/0, RequestCancel 0/0,
      NotAcceptableMedia 0/0, BadEvent 0/0,
      SETooSmall 0/0
     Server Error:
      InternalError 0/0, NotImplemented 0/0,
      BadGateway 0/0, ServiceUnavail 0/0,
      GatewayTimeout 0/0, BadSipVer 0/0,
      PreCondFailure 0/0
     Global Failure:
      BusyEverywhere 0/0, Decline 0/0,
      NotExistAnywhere 0/0, NotAcceptable 0/0
      Miscellaneous counters:
      RedirectRspMappedToClientErr 0
SIP Total Traffic Statistics (Inbound/Outbound)
      Invite 0/0, Ack 0/0, Bye 0/0,
      Cancel 0/0, Options 0/0,
      Prack 0/0, Comet 0/0,
      Subscribe 0/0, NOTIFY 0/0,
      Refer 0/0, Info 0/0
      Register 49/16
Retry Statistics
      Invite 0, Bye 0, Cancel 0, Response 0,
      Prack 0, Comet 0, Reliable1xx 0, NOTIFY 0 Register 4 SDP application statistics:
Parses: 0, Builds 0
Invalid token order: 0, Invalid param: 0
Not SDP desc: 0, No resource: 0
Last time SIP Statistics were cleared: <never>
```

The following sample output shows the RedirectResponseMappedToClientError status message. An incremented number indicates
                                          that 3 xx responses are to be treated as 4 xx responses. When call redirection is enabled (default), the RedirectResponseMappedToClientError status message is not incremented.

### Example:

```
Router# show sip-ua statistics SIP Response Statistics (Inbound/Outbound)
    Informational:
      Trying 0/0, Ringing 0/0,
      Forwarded 0/0, Queued 0/0,
      SessionProgress 0/0
    Success:
      OkInvite 0/0, OkBye 0/0,
      OkCancel 0/0, OkOptions 0/0,
      OkPrack 0/0, OkPreconditionMet 0/0,
      OKSubscribe 0/0, OkNotify 0/0,
      202Accepted 0/0
    Redirection (Inbound only):
      MultipleChoice 0, MovedPermanently 0,
      MovedTemporarily 0, UseProxy 0,
      AlternateService 0
    Client Error:
      BadRequest 0/0, Unauthorized 0/0,
      PaymentRequired 0/0, Forbidden 0/0,
      NotFound 0/0, MethodNotAllowed 0/0,
      NotAcceptable 0/0, ProxyAuthReqd 0/0,
      ReqTimeout 0/0, Conflict 0/0, Gone 0/0,
      ReqEntityTooLarge 0/0, ReqURITooLarge 0/0,
      UnsupportedMediaType 0/0, BadExtension 0/0,
      TempNotAvailable 0/0, CallLegNonExistent 0/0,
      LoopDetected 0/0, TooManyHops 0/0,
      AddrIncomplete 0/0, Ambiguous 0/0,
      BusyHere 0/0, RequestCancel 0/0
      NotAcceptableMedia 0/0, BadEvent 0/0
    Server Error:
      InternalError 0/0, NotImplemented 0/0,
      BadGateway 0/0, ServiceUnavail 0/0,
      GatewayTimeout 0/0, BadSipVer 0/0,
      PreCondFailure 0/0
    Global Failure:
      BusyEverywhere 0/0, Decline 0/0,
      NotExistAnywhere 0/0, NotAcceptable 0/0
    Miscellaneous counters:
      RedirectResponseMappedToClientError 1,
SIP Total Traffic Statistics (Inbound/Outbound)
    Invite 0/0, Ack 0/0, Bye 0/0,
    Cancel 0/0, Options 0/0,
    Prack 0/0, Comet 0/0,
    Subscribe 0/0, Notify 0/0,
    Refer 0/0
Retry Statistics
    Invite 0, Bye 0, Cancel 0, Response 0,
    Prack 0, Comet 0, Reliable1xx 0, Notify 0
SDP application statistics:
 Parses: 0,  Builds 0
 Invalid token order: 0,  Invalid param: 0
 Not SDP desc: 0,  No resource: 0
```

show sip-ua status

Use this command to display status for the SIP user agent (UA), including whether call redirection is enabled or disabled.

### Example:

```
Router# show sip-ua status SIP User Agent Status
SIP User Agent for UDP : ENABLED
SIP User Agent for TCP : ENABLED
SIP User Agent bind status(signaling): DISABLED
SIP User Agent bind status(media): DISABLED
SIP max-forwards : 6
SIP DNS SRV version: 1 (rfc 2052)
Redirection (3xx) message handling: ENABLED
```

show sip-ua timers

Use this command to display the current settings for the SIP user-agent (UA) timers.

The following sample output shows the waiting time before a register request is sent--that is, the value that is set with
                                          the timers register command:

### Example:

```
Router# show sip-ua timers SIP UA Timer Values (millisecs)
trying 500, expires 180000, connect 500, disconnect 500
comet 500, prack 500, rel1xx 500, notify 500 refer 500, register 500
```

## Using debug Commands

Commands are listed in alphabetical order.

Use the debug aaa authentication command to display high-level diagnostics related to AAA logins.

Use the debug asnl events command to verify that the SIP subscription server is up. The output displays a pending message if, for example, the client
                                 is unsuccessful in communicating with the server.

Use the debug call fallback family of commands to display details of VoIP call fallback.

Use the debug cch323 family of commands to provide debugging output for various components within an H.323 subsystem.

- debug ccsip all-- Enables all SIP-related debugging

- debug ccsip calls --Enables tracing of all SIP service-provider interface (SPI) calls

- debug ccsip error --Enables tracing of SIP SPI errors

- debug ccsip events --Enables tracing of all SIP SPI events

- debug ccsip info --Enables tracing of general SIP SPI information, including verification that call redirection is disabled

- debug ccsip media --Enables tracing of SIP media streams

- debug ccsip messages --Enables all SIP SPI message tracing, such as those that are exchanged between the SIP user-agent client (UAC) and the access
                                       server

- debug ccsip preauth --Enables diagnostic reporting of authentication, authorization, and accounting (AAA) preauthentication for SIP calls

- debug ccsip states --Enables tracing of all SIP SPI state tracing

- debug ccsip transport --Enables tracing of the SIP transport handler and the TCP or User Datagram Protocol (UDP) process

Use the debug isdn q931 command to display information about call setup and teardown of ISDN network connections (layer 3) between the local router
                                 (user side) and the network.

Use the debug kpm l command to enable debug tracing of KPML parser and builder errors.

Use the debug radius command to enable debug tracing of RADIUS attributes.

Use the debug rpms-proc preauth command to enable debug tracing on the RPMS process for H.323 calls, SIP calls, or both H.323 and SIP calls.

Use the debug rtr trace command to trace the execution of an SAA operation.

- debug voip ccapi protoheaders -- Displays messages sent between the originating and terminating gateways. If no headers are being received by the terminating
                                       gateway, verify that the header-passing command is enabled on the originating gateway.

- debug voip ivr script-- Displays any errors that might occur when the Tcl script is run

- debug voip rtp session named-event 101 -- Displays information important to DTMF-relay debugging, if you are using codec types g726r16 or g726r24. Be sure to append
                                       the argument 101 to the command to prevent the console screen from flooding with messages and all calls from failing.

Sample output for some of these commands follows:

### Sample Output for the debug ccsip events Command

The example shows how the Proxy-Authorization header is broken down into a decoded username and password.

```
Router# debug ccsip events CCSIP SPI: SIP Call Events tracing is enabled
21:03:21: sippmh_parse_proxy_auth: Challenge is 'Basic'.
21:03:21: sippmh_parse_proxy_auth: Base64 user-pass string is 'MTIzNDU2Nzg5MDEyMzQ1Njou'.
21:03:21: sip_process_proxy_auth: Decoded user-pass string is '1234567890123456:.'.
21:03:21: sip_process_proxy_auth: Username is '1234567890123456'.
21:03:21: sip_process_proxy_auth: Pass is '.'.
21:03:21: sipSPIAddBillingInfoToCcb: sipCallId for billing records =
10872472-173611CC-81E9C73D-F836C2B6@172.18.192.19421:03:21: ****Adding to UAS Request table
```

### Sample Output for the debug ccsip info Command

This example shows only the portion of the debug output that shows that call redirection is disabled. When call redirection
                              is enabled (default), there are no debug line changes.

```
Router# debug ccsip info 00:20:32: HandleUdpSocketReads :Msg enqueued for SPI with IPaddr: 172.18.207.10
:5060
00:20:32: CCSIP-SPI-CONTROL:  act_sentinvite_new_message
00:20:32: CCSIP-SPI-CONTROL:  sipSPICheckResponse
00:20:32: sip_stats_status_code
00:20:32: ccsip_get_code_class: !!Call Redirection feature is disabled on the GW
00:20:32: ccsip_map_call_redirect_responses: !!Mapping 302 response to 480
00:20:32:  Roundtrip delay 4 milliseconds for method INVITE
```

## Additional References

Cisco IOS
                                       				  Debug Command Reference, Release 12.3T

Cisco IOS
                                       				  Voice Troubleshooting and Monitoring Guide at
                                    				http://www.cisco.com/univercd/cc/td/doc/product/software/ios123/123cgcr/vvfax_c/voipt_c/

Cisco IOS
                                       				  Voice, Video, and Fax Configuration Guide , Release 12.2 at
                                    				http://www.cisco.com/univercd/cc/td/doc/product/software/ios122/122cgcr/fvvfax_c/index.htm

Cisco Technical
                                    				Support at http://www.cisco.com/en/US/support/index.html

Troubleshooting and Debugging VoIP Call Basics at
                                    				http://www.cisco.com/warp/public/788/voip/voip_debugcalls.html

VoIP Debug
                                       				  Commands at
                                    				http://www.cisco.com/univercd/cc/td/doc/product/access/acs_mod/1700/1750/1750voip/debug.htm

| Note | Under moderate traffic loads, debug commands produce a high volume of output. We therefore recommend that, as a general rule, you use show commands first and use debug commands with caution. |
|---|---|

| Note | General troubleshooting of problems affecting basic functionality such as dial peers, digit translation, and IP connectivity
                                       is beyond the scope of this chapter. For links to additional troubleshooting help, see "Additional References". |
|---|---|

| Step 1 | show sip service Use this command to display the status of SIP call service on a SIP gateway. The following sample output shows that SIP call service is enabled: Example: Router# show sip service SIP Service is up The following sample output shows that SIP call service was shut down with the shutdown command: Example: Router# show sip service SIP service is shut globally
under 'voice service voip' The following sample output shows that SIP call service was shut down with the call service stop command: Example: Router# show sip service SIP service is shut
under 'voice service voip', 'sip' submode The following sample output shows that SIP call service was shut down with the shutdown forced command: Example: Router# show sip service SIP service is forced shut globally
under 'voice service voip' The following sample output shows that SIP call service was shut down with the call service stop forced command: Example: Router# show sip service SIP service is forced shut
under 'voice service voip', 'sip' submode |
|---|---|
| Step 2 | show sip-ua register status Use this command to display the status of E.164 numbers that a SIP gateway has registered with an external primary SIP registrar. Example: Router# show sip-ua register status Line peer expires(sec) registered
4001 20001 596          no
4002 20002 596          no
5100 1     596          no
9998 2     596          no |
| Step 3 | show sip-ua statistics Use this command to display response, traffic, and retry SIP statistics, including whether call redirection is disabled. The following sample shows that four registers were sent: Example: Router# show sip-ua statistics SIP Response Statistics (Inbound/Outbound)
    Informational:
      Trying 0/0, Ringing 0/0,
      Forwarded 0/0, Queued 0/0,
      SessionProgress 0/0
     Success:
      OkInvite 0/0, OkBye 0/0,
      OkCancel 0/0, OkOptions 0/0,
      OkPrack 0/0, OkPreconditionMet 0/0,
      OkSubscribe 0/0, OkNOTIFY 0/0,
      OkInfo 0/0, 202Accepted 0/0
      OkRegister 12/49
     Redirection (Inbound only except for MovedTemp(Inbound/Outbound)) :
      MultipleChoice 0, MovedPermanently 0,
      MovedTemporarily 0/0, UseProxy 0,
      AlternateService 0
      Client Error:
      BadRequest 0/0, Unauthorized 0/0,
      PaymentRequired 0/0, Forbidden 0/0,
      NotFound 0/0, MethodNotAllowed 0/0,
      NotAcceptable 0/0, ProxyAuthReqd 0/0,
      ReqTimeout 0/0, Conflict 0/0, Gone 0/0,
      ReqEntityTooLarge 0/0, ReqURITooLarge 0/0,
      UnsupportedMediaType 0/0, BadExtension 0/0,
      TempNotAvailable 0/0, CallLegNonExistent 0/0,
      LoopDetected 0/0, TooManyHops 0/0,
      AddrIncomplete 0/0, Ambiguous 0/0,
      BusyHere 0/0, RequestCancel 0/0,
      NotAcceptableMedia 0/0, BadEvent 0/0,
      SETooSmall 0/0
     Server Error:
      InternalError 0/0, NotImplemented 0/0,
      BadGateway 0/0, ServiceUnavail 0/0,
      GatewayTimeout 0/0, BadSipVer 0/0,
      PreCondFailure 0/0
     Global Failure:
      BusyEverywhere 0/0, Decline 0/0,
      NotExistAnywhere 0/0, NotAcceptable 0/0
      Miscellaneous counters:
      RedirectRspMappedToClientErr 0
SIP Total Traffic Statistics (Inbound/Outbound)
      Invite 0/0, Ack 0/0, Bye 0/0,
      Cancel 0/0, Options 0/0,
      Prack 0/0, Comet 0/0,
      Subscribe 0/0, NOTIFY 0/0,
      Refer 0/0, Info 0/0
      Register 49/16
Retry Statistics
      Invite 0, Bye 0, Cancel 0, Response 0,
      Prack 0, Comet 0, Reliable1xx 0, NOTIFY 0 Register 4 SDP application statistics:
Parses: 0, Builds 0
Invalid token order: 0, Invalid param: 0
Not SDP desc: 0, No resource: 0
Last time SIP Statistics were cleared: <never> The following sample output shows the RedirectResponseMappedToClientError status message. An incremented number indicates
                                          that 3 xx responses are to be treated as 4 xx responses. When call redirection is enabled (default), the RedirectResponseMappedToClientError status message is not incremented. Example: Router# show sip-ua statistics SIP Response Statistics (Inbound/Outbound)
    Informational:
      Trying 0/0, Ringing 0/0,
      Forwarded 0/0, Queued 0/0,
      SessionProgress 0/0
    Success:
      OkInvite 0/0, OkBye 0/0,
      OkCancel 0/0, OkOptions 0/0,
      OkPrack 0/0, OkPreconditionMet 0/0,
      OKSubscribe 0/0, OkNotify 0/0,
      202Accepted 0/0
    Redirection (Inbound only):
      MultipleChoice 0, MovedPermanently 0,
      MovedTemporarily 0, UseProxy 0,
      AlternateService 0
    Client Error:
      BadRequest 0/0, Unauthorized 0/0,
      PaymentRequired 0/0, Forbidden 0/0,
      NotFound 0/0, MethodNotAllowed 0/0,
      NotAcceptable 0/0, ProxyAuthReqd 0/0,
      ReqTimeout 0/0, Conflict 0/0, Gone 0/0,
      ReqEntityTooLarge 0/0, ReqURITooLarge 0/0,
      UnsupportedMediaType 0/0, BadExtension 0/0,
      TempNotAvailable 0/0, CallLegNonExistent 0/0,
      LoopDetected 0/0, TooManyHops 0/0,
      AddrIncomplete 0/0, Ambiguous 0/0,
      BusyHere 0/0, RequestCancel 0/0
      NotAcceptableMedia 0/0, BadEvent 0/0
    Server Error:
      InternalError 0/0, NotImplemented 0/0,
      BadGateway 0/0, ServiceUnavail 0/0,
      GatewayTimeout 0/0, BadSipVer 0/0,
      PreCondFailure 0/0
    Global Failure:
      BusyEverywhere 0/0, Decline 0/0,
      NotExistAnywhere 0/0, NotAcceptable 0/0
    Miscellaneous counters:
      RedirectResponseMappedToClientError 1,
SIP Total Traffic Statistics (Inbound/Outbound)
    Invite 0/0, Ack 0/0, Bye 0/0,
    Cancel 0/0, Options 0/0,
    Prack 0/0, Comet 0/0,
    Subscribe 0/0, Notify 0/0,
    Refer 0/0
Retry Statistics
    Invite 0, Bye 0, Cancel 0, Response 0,
    Prack 0, Comet 0, Reliable1xx 0, Notify 0
SDP application statistics:
 Parses: 0,  Builds 0
 Invalid token order: 0,  Invalid param: 0
 Not SDP desc: 0,  No resource: 0 |
| Step 4 | show sip-ua status Use this command to display status for the SIP user agent (UA), including whether call redirection is enabled or disabled. Example: Router# show sip-ua status SIP User Agent Status
SIP User Agent for UDP : ENABLED
SIP User Agent for TCP : ENABLED
SIP User Agent bind status(signaling): DISABLED
SIP User Agent bind status(media): DISABLED
SIP max-forwards : 6
SIP DNS SRV version: 1 (rfc 2052)
Redirection (3xx) message handling: ENABLED |
| Step 5 | show sip-ua timers Use this command to display the current settings for the SIP user-agent (UA) timers. The following sample output shows the waiting time before a register request is sent--that is, the value that is set with
                                          the timers register command: Example: Router# show sip-ua timers SIP UA Timer Values (millisecs)
trying 500, expires 180000, connect 500, disconnect 500
comet 500, prack 500, rel1xx 500, notify 500 refer 500, register 500 |

| Note | Commands are listed in alphabetical order. |
|---|---|