---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sip-enhance180-prov-html-37962832ab
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sip-enhance180-prov.html
retrieved_at: 2026-08-16T15:47:14.916573+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP  Enhanced 180 Provisional Response Handling

## Chapter: SIP  Enhanced 180 Provisional Response Handling

# SIP  Enhanced 180 Provisional Response Handling

The SIP: Enhanced 180 Provisional Response Handling feature enables early media cut-through on Cisco IOS gateways for Session
                        Initiation Protocol (SIP) 180 response messages.

## Feature Information for SIP Enhanced 180 Provisional Response Handling

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP - Enhanced 180 Provisional Response Handling

Baseline Functionality

The Session Initiation Protocol (SIP) Enhanced 180 Provisional Response Handling feature provides the ability to enable or
                                          disable early media cut-through on Cisco IOS gateways for SIP 180 response messages.

The following commands were introduced or modified: disable-early-media 180 , and show sip-ua status

## Information About SIP Enhanced 180 Provisional Response Handling

The Session Initiation Protocol (SIP) feature allows you to specify whether 180 messages with Session Description Protocol
                           (SDP) are handled in the same way as 183 responses with SDP. The 180 Ringing message is a provisional or informational response
                           used to indicate that the INVITE message has been received by the user agent and that alerting is taking place. The 183 Session
                           Progress response indicates that information about the call state is present in the message body media information. Both 180
                           and 183 messages may contain SDP, which allows an early media session to be established prior to the call being answered.

Prior to this feature, Cisco gateways handled a 180 Ringing response with SDP in the same manner as a 183 Session Progress
                           response; that is, the SDP was assumed to be an indication that the far end would send early media. Cisco gateways handled
                           a 180 response without SDP by providing local ringback, rather than early media cut-through. This feature provides the capability
                           to ignore the presence or absence of SDP in 180 messages, and as a result, treat all 180 messages in a uniform manner. The
                           SIP: Enhanced 180 Provisional Response Handling feature allows you to specify which call treatment, early media or local ringback,
                           is provided for 180 responses with SDP:

The table below shows the call treatments available with this feature:

Response Message

SIP Enhanced 180 Provisional Response Handling Status

Treatment

180 response with SDP

Enabled (default)

Early media cut-through

180 response with SDP

Disabled

Local ringback

180 response without SDP

Not affected by the SIP--Enhanced 180 Provisional Response Handlingfeature

Local ringback

183 response with SDP

Not affected by the SIP--Enhanced 180 Provisional Response Handling feature

Early media cut-through

## How to Disable the SIP Enhanced 180 Provisional Response Handling Feature

### Disabling Early Media Cut-Through

The early media cut-through feature is enabled by default. To disable early media cut-through, perform the following task:

### SUMMARY STEPS

- enable

- configure terminal

- interface type number

- sip ua

- disable-early-media 180

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

interface type number

#### Example:

```
Router(config)# ethernet 0/0/0
```

Configures an interface type and enters interface configuration mode.

Step 4

sip ua

#### Example:

```
Router(config-sip-ua)# sip ua
```

Enables SIP UA configuration commands in order to configure the user agent.

Step 5

disable-early-media 180

#### Example:

```
Router(config-sip-ua)# disable-early-media 180
```

Disables the gateway’s ability to process SDP in a 180 response as a request for early media cut-through.

## Verify SIP Enhanced 180 Provisional Response Handling

To verify the SIP Enhanced 180 Provisional Response Handling feature, use the show running configuration or show sip-ua status or show logging command to display the output.

If early media is enabled, which is the default setting, the show running-config output does not show any information related to the new feature.

To monitor this feature, use the show sip-ua statistics , and show sip-ua status EXEC commands.

## Configuration Examples for SIP - Enhanced 180 Provisional Response Handling

### show running-config Command

The following is sample output from the show running-config command after the disable-early-media 180 command was used:

```
Router# show running-config
.
.
.
dial-peer voice 223 pots
 application session
 destination-pattern 223
 port 1/0/0
!
gateway 
!
sip-ua 
 disable-early-media 180
```

### show sip-ua status Command

The following is sample output from the show sip-ua status command after the disable-early-media 180 command was used.

```
Router# show sip-ua status
SIP User Agent Status
SIP User Agent for UDP :ENABLED
SIP User Agent for TCP :ENABLED
SIP User Agent bind status(signaling):ENABLED 10.0.0.0
SIP User Agent bind status(media):ENABLED 0.0.0.0
SIP early-media for 180 responses with SDP:DISABLED
SIP max-forwards :6
SIP DNS SRV version:2 (rfc 2782)
NAT Settings for the SIP-UA
Role in SDP:NONE
Check media source packets:DISABLED
Redirection (3xx) message handling:ENABLED
SDP application configuration:
 Version line (v=) required
 Owner line (o=) required
 Timespec line (t=) required
 Media supported:audio image 
 Network types supported:IN 
 Address types supported:IP4 
 Transport types supported:RTP/AVP udptl
```

### show logging Command

The following is partial sample output from the show logging command. The outgoing gateway is receiving a 180 message with SDP and is configured to ignore the SDP.

```
Router# show logging
Log Buffer (600000 bytes):
00:12:19:%SYS-5-CONFIG_I:Configured from console by console
00:12:19:%SYS-5-CONFIG_I:Configured from console by console
00:12:20:0x639F6EEC :State change from (STATE_NONE, SUBSTATE_NONE)  to 
(STATE_IDLE, SUBSTATE_NONE)
00:12:20:****Adding to UAC table
00:12:20:adding call id 2 to table
00:12:20: Queued event from SIP SPI :SIPSPI_EV_CC_CALL_SETUP
00:12:20:CCSIP-SPI-CONTROL: act_idle_call_setup
00:12:20: act_idle_call_setup:Not using Voice Class Codec
00:12:20:act_idle_call_setup:preferred_codec set[0] type :g711ulaw 
bytes:160
00:12:20:sipSPICopyPeerDataToCCB:From CLI:Modem NSE payload = 100, 
Passthrough = 0,Modem relay = 0, Gw-Xid = 1
SPRT latency 200, SPRT Retries = 12, Dict Size = 1024
String Len = 32, Compress dir = 3
00:12:20:sipSPICanSetFallbackFlag - Local Fallback is not active
00:12:20:****Deleting from UAC table
00:12:20:****Adding to UAC table
00:12:20: Queued event from SIP SPI :SIPSPI_EV_CREATE_CONNECTION
00:12:20:0x639F6EEC :State change from (STATE_IDLE, SUBSTATE_NONE)  to 
(STATE_IDLE, SUBSTATE_CONNECTING)
00:12:20:0x639F6EEC :State change from (STATE_IDLE, 
SUBSTATE_CONNECTING)  to (STATE_IDLE, SUBSTATE_CONNECTING)
00:12:20:sipSPIUsetBillingProfile:sipCallId for billing records = 
41585FCE-14F011CC-8005AF80-D4AA3153@172.31.1.42
00:12:20:CCSIP-SPI-CONTROL: act_idle_connection_created
00:12:20:CCSIP-SPI-CONTROL: act_idle_connection_created:Connid(1) 
created to 172.31.1.15:5060, local_port 57838
00:12:20:CCSIP-SPI-CONTROL: sipSPIOutgoingCallSDP
00:12:20:sipSPISetMediaSrcAddr: media src addr for stream 1 = 10.1.1.42
00:12:20:sipSPIReserveRtpPort:reserved port 18978 for stream 1
00:12:20: convert_codec_bytes_to_ptime:Values :Codec:g711ulaw 
codecbytes :160, ptime:20
00:12:20:sip_generate_sdp_xcaps_list:Modem Relay disabled. X-cap not 
needed
00:12:20:Received Octet3A=0x00 -> Setting ;screen=no ;privacy=off
00:12:20:sipSPIAddLocalContact
00:12:20: Queued event from SIP SPI :SIPSPI_EV_SEND_MESSAGE
00:12:20:sip_stats_method
00:12:20:sipSPIProcessRtpSessions
00:12:20:sipSPIAddStream:Adding stream 1 (callid 2) to the VOIP RTP 
library
00:12:20:sipSPISetMediaSrcAddr: media src addr for stream 1 = 10.1.1.42
00:12:20:sipSPIUpdateRtcpSession:for m-line 1
00:12:20:sipSPIUpdateRtcpSession:rtcp_session info
laddr = 10.1.1.42, lport = 18978, raddr = 0.0.0.0, 
rport=0, do_rtcp=FALSE
src_callid = 2, dest_callid = -1
00:12:20:sipSPIUpdateRtcpSession:No rtp session, creating a new one
00:12:20:sipSPIAddStream:In State Idle
00:12:20:act_idle_connection_created:Transaction active. Facilities will 
be queued.
00:12:20:0x639F6EEC :State change from (STATE_IDLE, 
SUBSTATE_CONNECTING)  to (STATE_SENT_INVITE, SUBSTATE_NONE)
00:12:20:Sent:
INVITE sip:222@172.31.1.15:5060 SIP/2.0
Via:SIP/2.0/UDP  10.1.1.42:5060
From:"111" <sip:111@172.31.1.42>;tag=B4DC4-9E1
To:<sip:222@172.31.1.15>
Date:Mon, 01 Mar 1993 00:12:20 GMT
Call-ID:41585FCE-14F011CC-8005AF80-D4AA3153@172.31.1.42
Supported:timer
Min-SE: 1800
Cisco-Guid:1096070726-351277516-2147659648-3567923539
User-Agent:Cisco-SIPGateway/IOS-12.x
Allow:INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, COMET, REFER, SUBSCRIBE, 
NOTIFY, INFO
CSeq:101 INVITE
Max-Forwards:6
Remote-Party-ID:<sip:111@172.31.1.42>;party=calling;screen=no;privacy=off
Timestamp:730944740
Contact:<sip:111@172.31.1.42:5060>
Expires:180
Allow-Events:telephone-event
Content-Type:application/sdp
Content-Length:230
v=0
o=CiscoSystemsSIP-GW-UserAgent 4629 354 IN IP4 172.31.1.42
s=SIP Call
c=IN IP4 172.31.1.42
t=0 0
m=audio 18978 RTP/AVP 0 100
c=IN IP4 10.1.1.42
a=rtpmap:0 PCMU/8000
a=rtpmap:100 X-NSE/8000
a=fmtp:100 192-194
a=ptime:20
00:12:21:Received:
SIP/2.0 100 Trying
Via:SIP/2.0/UDP  10.1.1.42:5060
From:"111" <sip:111@172.31.1.42>;tag=B4DC4-9E1
To:<sip:222@172.31.1.15>;tag=442AC-22
Date:Wed, 16 Feb 2000 18:19:56 GMT
Call-ID:41585FCE-14F011CC-8005AF80-D4AA3153@172.31.1.42
Timestamp:730944740
Server:Cisco-SIPGateway/IOS-12.x
CSeq:101 INVITE
Allow-Events:telephone-event
Content-Length:0
00:12:21:HandleUdpSocketReads :Msg enqueued for SPI with IPaddr:
10.1.1.15:5060
00:12:21:CCSIP-SPI-CONTROL: act_sentinvite_new_message
00:12:21:CCSIP-SPI-CONTROL: sipSPICheckResponse
00:12:21:sip_stats_status_code
00:12:21: Roundtrip delay 420 milliseconds for method INVITE
00:12:21:0x639F6EEC :State change from (STATE_SENT_INVITE, 
SUBSTATE_NONE)  to (STATE_RECD_PROCEEDING, SUBSTATE_PROCEEDING_PROCEEDING)
00:12:21:Received:
SIP/2.0 180 Ringing
Via:SIP/2.0/UDP  10.1.1.42:5060
From:"111" <sip:111@10.1.1.42>;tag=B4DC4-9E1
To:<sip:222@172.31.1.15>;tag=442AC-22
Date:Wed, 16 Feb 2000 18:19:56 GMT
Call-ID:41585FCE-14F011CC-8005AF80-D4AA3153@172.31.1.42
Timestamp:730944740
Server:Cisco-SIPGateway/IOS-12.x
CSeq:101 INVITE
Allow-Events:telephone-event
Contact:<sip:222@172.31.1.59:5060>
Record-Route:<sip:222@10.1.1.15:5060;maddr=10.1.1.15>
Content-Length:230
Content-Type:application/sdp
v=0
o=CiscoSystemsSIP-GW-UserAgent 4629 354 IN IP4 10.1.1.42
s=SIP Call
c=IN IP4 10.1.1.42
t=0 0
m=audio 18978 RTP/AVP 0 100
c=IN IP4 10.1.1.42
a=rtpmap:0 PCMU/8000
a=rtpmap:100 X-NSE/8000
a=fmtp:100 192-194
a=ptime:20
00:12:21:HandleUdpSocketReads :Msg enqueued for SPI with IPaddr:
10.1.1.15:5060
00:12:21:CCSIP-SPI-CONTROL: act_recdproc_new_message
00:12:21:CCSIP-SPI-CONTROL: act_recdproc_new_message_response
00:12:21:CCSIP-SPI-CONTROL: sipSPICheckResponse
00:12:21:sip_stats_status_code
00:12:21: Roundtrip delay 496 milliseconds for method INVITE
00:12:21:CCSIP-SPI-CONTROL: act_recdproc_new_message_response :Early 
media disabled for 180:Ignoring SDP if present
00:12:21:HandleSIP1xxRinging:SDP in 180 will be ignored if present: No 
early media cut through
00:12:21:HandleSIP1xxRinging:SDP Body either absent or ignored in 180 
RINGING:- would wait for 200 OK to do negotiation.
00:12:21:HandleSIP1xxRinging:MediaNegotiation expected in 200 OK
00:12:21:sipSPIGetGtdBody:No valid GTD body found.
00:12:21:sipSPICreateRawMsg:No GTD passed.
00:12:21:0x639F6EEC :State change from (STATE_RECD_PROCEEDING, 
SUBSTATE_PROCEEDING_PROCEEDING)  to (STATE_RECD_PROCEEDING, 
SUBSTATE_PROCEEDING_ALERTING)
00:12:21:HandleSIP1xxRinging:Transaction Complete. Lock on Facilities 
released.
00:12:22:Received:
SIP/2.0 200 OK
Via:SIP/2.0/UDP  10.1.1.42:5060
From:"111" <sip:111@10.1.1.42>;tag=B4DC4-9E1
To:<sip:222@10.1.1.15>;tag=442AC-22
Date:Wed, 16 Feb 2000 18:19:56 GMT
Call-ID:41585FCE-14F011CC-8005AF80-D4AA3153@172.31.1.42
Timestamp:730944740
Server:Cisco-SIPGateway/IOS-12.x
CSeq:101 INVITE
Allow:INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, COMET, REFER, SUBSCRIBE, 
NOTIFY, INFO
Allow-Events:telephone-event
Contact:<sip:222@10.1.1.59:5060>
Record-Route:<sip:222@10.1.1.15:5060;maddr=10.1.1.15>
Content-Type:application/sdp
Content-Length:231
v=0
o=CiscoSystemsSIP-GW-UserAgent 9600 4816 IN IP4 10.1.1.59
s=SIP Call
c=IN IP4 10.1.1.59
t=0 0
m=audio 19174 RTP/AVP 0 100
c=IN IP4 10.1.1.59
a=rtpmap:0 PCMU/8000
a=rtpmap:100 X-NSE/8000
a=fmtp:100 192-194
a=ptime:20
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP - Enhanced 180 Provisional Response Handling | Baseline Functionality | The Session Initiation Protocol (SIP) Enhanced 180 Provisional Response Handling feature provides the ability to enable or
                                          disable early media cut-through on Cisco IOS gateways for SIP 180 response messages. The following commands were introduced or modified: disable-early-media 180 , and show sip-ua status |

| Response Message | SIP Enhanced 180 Provisional Response Handling Status | Treatment |
|---|---|---|
| 180 response with SDP | Enabled (default) | Early media cut-through |
| 180 response with SDP | Disabled | Local ringback |
| 180 response without SDP | Not affected by the SIP--Enhanced 180 Provisional Response Handlingfeature | Local ringback |
| 183 response with SDP | Not affected by the SIP--Enhanced 180 Provisional Response Handling feature | Early media cut-through |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | interface type number Example: Router(config)# ethernet 0/0/0 | Configures an interface type and enters interface configuration mode. |
| Step 4 | sip ua Example: Router(config-sip-ua)# sip ua | Enables SIP UA configuration commands in order to configure the user agent. |
| Step 5 | disable-early-media 180 Example: Router(config-sip-ua)# disable-early-media 180 | Disables the gateway’s ability to process SDP in a 180 response as a request for early media cut-through. |