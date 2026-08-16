---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-dtmf-relay-html-f18b47fc0f
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/dtmf-relay.html
retrieved_at: 2026-08-16T15:44:51.853331+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: DTMF Relay

## Chapter: DTMF Relay

# DTMF Relay

## Overview

The DTMF Relay feature allows Cisco Unified Border Element (CUBE) to send dual-tone multifrequency (DTMF) digits over IP.

This chapter talks
                           		about DTMF tones, DTMF relay mechanisms, how to configure DTMF relays, and
                           		interoperability and priority with multiple relay methods.

H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

Support for sip-info to rtp-nte DTMF relay mechanism for SIP-SIP calls

Cisco IOS XE
                                          				  Everest 16.6.1

This feature
                                          				  adds support for sip-info to rtp-nte DTMF relay mechanism for SIP-SIP calls.

### DTMF Tones

DTMF tones are used during a call to signal to a far-end device; these signals is for navigating a menu system, entering data,
                              or for other types of manipulation. They are processed differently from the DTMF tones that are sent during the call setup
                              as part of the call control. TDM interfaces on Cisco devices support DTMF by default. Cisco VoIP dial-peers do not support
                              DTMF relay by default and require DTMF relay capabilities to be enabled.

DTMF tones sent by phones do not traverse the CUBE .

### DTMF Relay

Dual-Tone Multifrequency (DTMF) relay is the mechanism for sending DTMF digits over IP. The VoIP dial peer can pass the DTMF
                              digits either in a band or out of band.

In-band DTMF-Relay passes the DTMF digits using the RTP media stream and uses a special payload type identifier in the RTP
                              header to distinguish DTMF digits from voice communication. This method is more likely to work on lossless codecs, such as
                              G.711.

Out-of-band DTMF-Relay passes DTMF digits using a signaling protocol (SIP) instead of using the RTP media stream.

DTMF relay prevents loss of integrity of DTMF digits that are caused by VoIP compressed codecs. The relayed DTMF is then regenerated
                              transparently on the peer side.

DTMF relay mechanisms that are supported on VoIP dial-peers are listed below based on the keywords used to configure them.
                              The DTMF relay mechanism can be either out-of-band (SIP) or in-band (RTP).

sip-notify —This method is available on SIP dial peers only. This is a Cisco proprietary out-of-band DTMF relay mechanism that transports
                                    DTMF signals using SIP-Notify message. The SIP Call-Info header indicates the use of the SIP-Notify DTMF relay mechanism.
                                    The message is acknowledged with a 18x or 200 response message containing a similar SIP Call-Info header.

The Call-Info header for a NOTIFY-based out-of-band relay is as follows:

```
Call-Info: <sip: address>; method="NOTIFY;Event=telephone-event;Duration=msec"
```

DTMF relay digits are sent as 4 bytes in a binary encoded format.

This mechanism is useful for communicating with SCCP IP phones that do not support in-band DTMF digits and analog phones that
                                    are attached to analog voice ports (FXS) on the router.

If multiple DTMF relay mechanisms are enabled on a SIP dial peer and are negotiated successfully, NOTIFY-based out-of-band
                                    DTMF relay takes precedence.

If you configure KPML on the dial peer, the gateway sends INVITE messages with KPML in the Allow-Events header.

The use of this method is to register SIP endpoints to Cisco Unified Communications Manager(CUCM) or Cisco Unified Communications
                                    Manager Express(CME). This method is useful for nonconferencing calls and for interoperability between SIP products and SIP
                                    phones.

If you configure rtp-nte, sip-notify, and sip-kpml, the outgoing INVITE contains an SDP with rtp-nte payload, a SIP Call-Info
                                    header, and an Allow-Events header with KPML.

The following SIP-Notify message is a sample that is taken after the subscription has taken place. The endpoints transmit
                                    digits using SIP-Notify messages with KPML events through XML. In the following example, the digit “1” is being transmitted:

```
NOTIFY  sip:192.168.105.25:5060 SIP/2.0
Event: kpml <?xml version="1.0" encoding="UTF-8"?>
<kpml-response version="1.0" code="200" text="OK" digits="1" tag= "dtmf" />
```

The method is always enabled for SIP dial peers, and is invoked when a SIP INFO message is received with DTMF relay content.

This following sample message shows that a SIP INFO message received with specifics about the DTMF tone to be generated.
                                    The combination of the From, To, and Call-ID headers identifies the call leg. The signal and duration headers specify the
                                    digit, in this case 1, and duration, 160 milliseconds in the example, for DTMF tone play.

```
INFO sip:2143302100@172.17.2.33 SIP/2.0
Via: SIP/2.0/UDP 172.80.2.100:5060
From: <sip:9724401003@172.80.2.100>;tag=43
To: <sip:2143302100@172.17.2.33>;tag=9753.0207
Call-ID: 984072_15401962@172.80.2.100
CSeq: 25634 INFO
Supported: 100rel
Supported: timer
Content-Length: 26
Content-Type: application/dtmf-relay
Signal= 1
Duration= 160
```

rtp-nte —Real-Time Transport Protocol (RTP) Named phone Events (NTE). This is an in-band DTMF relay mechanism that is defined by RFC2833.
                                    RFC2833 defines formats of NTE-RTP packets that are used to transport DTMF digits, hookflash, and other telephony events between
                                    two peer endpoints. DTMF tones are sent as packet data after call media has been established using the RTP stream and are
                                    distinguished from the audio by the RTP payload type field, preventing compression of DTMF-based RTP packets. For example,
                                    the audio of a call is sent on a session with an RTP payload type that identifies it as G.711 data, and the DTMF packets are
                                    sent with an RTP payload type that identifies them as NTEs. The consumer of the stream utilizes the G.711 packets and the
                                    NTE packets separately.

The SIP NTE DTMF relay feature provides reliable digit relay.

Payload type 96 and 97 is used for fax by default in Cisco devices. A third-party device may use payload type 96 and 97 for
                                                DTMF. In such scenarios, we recommend you to perform one of the following:

Change the payload type for fax in both incoming and outgoing dial-peers using rtp payload-type command

Use assymetric payload dtmf command

For more information on configuring rtp payload-type and asymmetric payload DTMF, see Dynamic Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls.

Payload types and attributes of this method are negotiated between the two ends at call setup using the Session Description
                                    Protocol (SDP) within the body section of the SIP message.

cisco-rtp —This is an in-band DTMF relay mechanism that is Cisco proprietary, where the DTMF digits are encoded differently from the
                                    audio and are identified as a payload type 121. The DTMF digits are part of the RTP data stream and distinguished from the
                                    audio by the RTP payload type field. This method is not supported by CUCM and its use has been discontinued.

Digits are passed along just like the rest of your voice as normal audio tones with no special coding or markers using the
                                    same codec as your voice does and are generated by your phone.

## Interoperability
                        	 and Priority with Multiple DTMF Relay Methods

CUBE negotiates both rtp-nte and sip-kpml if both are supported and advertised in the incoming INVITE. However, CUBE relies on the rtp-nte DTMF method to receive digits and a SUBSCRIBE if sip-kpml is not initiated. CUBE still accepts SUBSCRIBEs for KPML. This prevents double-digit reporting problems at CUBE .

CUBE negotiates to one of the following:

cisco-rtp

rtp-nte

rtp-nte and kpml

kpml

sip-notify

If you configure
                                 			 rtp-nte, sip-notify, and sip-kpml, the outgoing INVITE contains a SIP Call-Info
                                 			 header, an Allow-Events header with KPML, and an sdp with rtp-nte payload.

If you configure more than one out-of-band DTMF method, preference goes from highest to lowest in the order of configuration.

CUBE selects DTMF relay mechanisms using the following priority:

sip-notify or sip-kpml

rtp-nte

None— Send DTMF in-band

### DTMF
                           	 Interoperability Table

This table provides the DTMF interoperability information between various DTMF relay types in different call flow scenarios.
                              For instance, if you need to configure sip-kpml on an inbound dial peer and RTP-NTE on an outbound dial peer in an RTP-RTP
                              Flow through configuration, refer table 3 to see that the combination is supported.  The call scenarios provided are as follows:

RTP-RTP
                                    			 Flow-Through

RTP-RTP with
                                    			 transcoder Flow-Through

RTP-RTP Flow
                                    			 Around

SRTP-RTP Flow
                                    			 Through

outbound dial-peer protocol

inbound dial-peer protocol

SIP

Supported

Supported

Supported

Supported*

Supported

Supported

Supported

Supported

Supported

Inband

Supported*

Supported

* Media resource is required (Transcoder) for Cisco IOS and IOS XE versions.

outbound dial-peer protocol

inbound dial-peer protocol

SIP

Supported

Supported

Supported

Supported

Inband

Supported

outbound dial-peer protocol

inbound dial-peer protocol

SIP

Supported

Supported*

Supported

Supported

Inband

Supported*

Supported

* Media resource is required (Transcoder) for Cisco IOS and IOS XE versions. CUBE falls back to flow-through mode if media resource is unavailable.

outbound dial-peer protocol

inbound dial-peer protocol

SIP

Supported

Supported

Supported

Supported

Supported

Supported

Supported

Supported

Inband

Supported

Supported

For calls sent from an in-band (RTP-NTE) to an out-of band method, configure the dtmf-relay rtp-nte digit-drop command on the inbound dial-peer and the desired out-of-band method on the outgoing dial-peer. Otherwise, the same digit
                                          is sent in OOB as well as in-band, and gets interpreted as duplicate digits by the receiving end. When the digit-drop option
                                          is configured on the inbound leg, CUBE suppresses NTE packets and only relay digits using the OOB method configured on the outbound leg.

## Configure DTMF Relay

You can configure
                           		DTMF relay using the dtmf-relay method1 [...[ method6 ]] command in the VoIP dial peer.

DTMF negotiation is performed based on the matching inbound dial-peer configuration.

The method variable used here can be any of the following:

sip-notify

sip-kpml

sip-info

rtp-nte [digit-drop]

ciso-rtp

Multiple DTMF methods may be configured on CUBE simultaneously in order to minimize MTP requirements. If you configure more than one out-of-band DTMF method, preference
                           goes from highest to lowest in the order of configuration. If an endpoint does not support any of the DTMF relay mechanism
                           configured on CUBE , an MTP or transcoder is required.

The following table lists the DTMF relay types supported.

## Verify DTMF Relay

### SUMMARY STEPS

- show sip-ua calls

- show sip-ua
                                    				  calls dtmf-relay sip-info

- show sip-ua
                                    				  history dtmf-relay kpml

- show sip-ua
                                    				  history dtmf-relay sip-notify

### DETAILED STEPS

Step 1

show sip-ua calls

The following sample output shows that the DTMF method is SIP-KPML.

### Example:

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

Step 2

show sip-ua
                                             				  calls dtmf-relay sip-info

The following
                                          				sample output displays active SIP calls with INFO DTMF Relay mode.

### Example:

```
Device# show sip-ua calls dtmf-relay sip-info Total SIP call legs:2, User Agent Client:1, User Agent Server:1
SIP UAC CALL INFO
Call 1
SIP Call ID                : 9598A547-5C1311E2-8008F709-2470C996@172.27.161.122
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : sipp
   Called Number           : 3269011111
   CC Call ID              : 2
No.         Timestamp         Digit           Duration      
======================================================= 
0    01/12/2013 17:23:25.615  2                   250            
1    01/12/2013 17:23:25.967  5                   300            
2    01/12/2013 17:23:26.367  6                   300            

Call 2
SIP Call ID                : 1-29452@172.25.208.177
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : sipp
   Called Number           : 3269011111
   CC Call ID              : 1
No.         Timestamp         Digit           Duration      
======================================================= 
0    01/12/2013 17:23:25.615  2                   250            
1    01/12/2013 17:23:25.967  5                   300            
2    01/12/2013 17:23:26.367  6                   300            

   Number of SIP User Agent Client(UAC) calls: 2

SIP UAS CALL INFO
Call 1
SIP Call ID                : 1-29452@172.25.208.177
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : sipp
   Called Number           : 3269011111
   CC Call ID              : 1
No.         Timestamp         Digit           Duration      
======================================================= 
0    01/12/2013 17:23:25.615  2                   250            
1    01/12/2013 17:23:25.967  5                   300            
2    01/12/2013 17:23:26.367  6                   300            

Call 2
SIP Call ID                : 9598A547-5C1311E2-8008F709-2470C996@172.27.161.122
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : sipp
   Called Number           : 3269011111
   CC Call ID              : 2
No.         Timestamp         Digit           Duration      
======================================================= 
0    01/12/2013 17:23:25.615  2                   250            
1    01/12/2013 17:23:25.967  5                   300            
2    01/12/2013 17:23:26.367  6                   300            

   Number of SIP User Agent Server(UAS) calls: 2
```

Step 3

show sip-ua
                                             				  history dtmf-relay kpml

The following
                                          				sample output displays SIP call history with KMPL DTMF Relay mode.

### Example:

```
Device# show sip-ua history dtmf-relay kpml Total SIP call legs:2, User Agent Client:1, User Agent Server:1
SIP UAC CALL INFO
Call 1
SIP Call ID                : D0498774-F01311E3-82A0DE9F-78C438FF@10.86.176.119
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 257
No.         Timestamp         Digit           Duration      
======================================================= 

Call 2
SIP Call ID                : 22BC36A5-F01411E3-81808A6A-5FE95113@10.86.176.142
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 256
No.         Timestamp         Digit           Duration      
======================================================= 

   Number of SIP User Agent Client(UAC) calls: 2

SIP UAS CALL INFO
Call 1
SIP Call ID                : 22BC36A5-F01411E3-81808A6A-5FE95113@10.86.176.142
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 256
No.         Timestamp         Digit           Duration      
======================================================= 

Call 2
SIP Call ID                : D0498774-F01311E3-82A0DE9F-78C438FF@10.86.176.119
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 257
No.         Timestamp         Digit           Duration      
======================================================= 

   Number of SIP User Agent Server(UAS) calls: 2
```

Step 4

show sip-ua
                                             				  history dtmf-relay sip-notify

The following
                                          				sample output displays SIP call history with SIP Notify DTMF Relay mode.

### Example:

```
Device# show sip-ua history dtmf-relay sip-notify Total SIP call legs:2, User Agent Client:1, User Agent Server:1
SIP UAC CALL INFO
Call 1
SIP Call ID                : 29BB98C-F01311E3-8297DE9F-78C438FF@10.86.176.119
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 252
No.         Timestamp         Digit           Duration      
======================================================= 

Call 2
SIP Call ID                : 550E973B-F01311E3-817A8A6A-5FE95113@10.86.176.142
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 251
No.         Timestamp         Digit           Duration      
======================================================= 

   Number of SIP User Agent Client(UAC) calls: 2

SIP UAS CALL INFO
Call 1
SIP Call ID                : 550E973B-F01311E3-817A8A6A-5FE95113@10.86.176.142
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 251
No.         Timestamp         Digit           Duration      
======================================================= 

Call 2
SIP Call ID                : 29BB98C-F01311E3-8297DE9F-78C438FF@10.86.176.119
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 252
No.         Timestamp         Digit           Duration      
======================================================= 

   Number of SIP User Agent Server(UAS) calls: 2
```

| Note | H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications. |
|---|---|

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| Support for sip-info to rtp-nte DTMF relay mechanism for SIP-SIP calls | Cisco IOS XE
                                          				  Everest 16.6.1 | This feature
                                          				  adds support for sip-info to rtp-nte DTMF relay mechanism for SIP-SIP calls. |

| Note | DTMF tones sent by phones do not traverse the CUBE . |
|---|---|

| Note | The main advantage of DTMF relay is that low-bandwidth codecs like G.729 and G.723 is sent with greater fidelity when sent
                                       using in-band DTMF relay. Without the use of DTMF relay, calls established with low-bandwidth codecs may have trouble accessing
                                       automated DTMF-based systems, such as voicemail, menu-based Automatic Call Distributor (ACD) systems, and automated banking
                                       systems. |
|---|---|

| Note | Payload type 96 and 97 is used for fax by default in Cisco devices. A third-party device may use payload type 96 and 97 for
                                                DTMF. In such scenarios, we recommend you to perform one of the following: Change the payload type for fax in both incoming and outgoing dial-peers using rtp payload-type command Use assymetric payload dtmf command For more information on configuring rtp payload-type and asymmetric payload DTMF, see Dynamic Payload Type Interworking for DTMF and Codec Packets for SIP-to-SIP Calls. |
|---|---|

| Note | This method should not be confused with the “Voice in-band audio/G711” transport because the latter is just the audible tones
                                             is passed as normal audio without any relay signaling method being “aware” or involved in the process. This is plain audio
                                             passing through end-to-end using the G711Ulaw/Alaw codec. |
|---|---|

|  | outbound dial-peer protocol | SIP | Inband |
|---|---|---|---|
| inbound dial-peer protocol | DTMF Relay Type | rtp-nte | sip-kpml | sip- notify | sip-info | Voice Inband (G.711) |
| SIP | rtp-nte | Supported | Supported | Supported |  | Supported* |
| sip-kpml | Supported | Supported |  |  |  |
| sip-notify | Supported |  | Supported |  |  |
| sip-info | Supported 1 |  |  |  |  |
| Inband | Voice Inband (G.711) | Supported* |  |  |  | Supported |

|  | outbound dial-peer protocol | SIP | Inband |
|---|---|---|---|
| inbound dial-peer protocol | DTMF Relay Type | rtp-nte | sip-kpml | sip- notify | sip-info | Voice Inband (G.711) |
| SIP | rtp-nte | Supported |  |  |  | Supported |
| sip-kpml |  | Supported |  |  |  |
| sip-notify |  |  | Supported |  |  |
| sip-info |  |  |  |  |  |
| Inband | Voice Inband (G.711) | Supported |  |  |  |  |

|  | outbound dial-peer protocol | SIP | Inband |
|---|---|---|---|
| inbound dial-peer protocol | DTMF Relay Type | rtp-nte | sip-kpml | sip- notify | sip-info | Voice Inband (G.711) |
| SIP | rtp-nte | Supported |  |  |  | Supported* |
| sip-kpml |  | Supported |  |  |  |
| sip-notify |  |  | Supported |  |  |
| sip-info |  |  |  |  |  |
| Inband | Voice Inband (G.711) | Supported* |  |  |  | Supported |

|  | outbound dial-peer protocol | SIP | Inband |
|---|---|---|---|
| inbound dial-peer protocol | DTMF Relay Type | rtp-nte | sip-kpml | sip- notify | sip-info | Voice Inband (G.711) |
| SIP | rtp-nte | Supported | Supported | Supported |  | Supported |
| sip-kpml | Supported | Supported |  |  |  |
| sip-notify | Supported |  | Supported |  |  |
| sip-info |  |  |  |  |  |
| Inband | Voice Inband (G.711) | Supported |  |  |  | Supported |

| Note | For calls sent from an in-band (RTP-NTE) to an out-of band method, configure the dtmf-relay rtp-nte digit-drop command on the inbound dial-peer and the desired out-of-band method on the outgoing dial-peer. Otherwise, the same digit
                                          is sent in OOB as well as in-band, and gets interpreted as duplicate digits by the receiving end. When the digit-drop option
                                          is configured on the inbound leg, CUBE suppresses NTE packets and only relay digits using the OOB method configured on the outbound leg. |
|---|---|

| In-band | rtp-nte |
|---|---|
| Out-of-band | sip-notify, sip-kpml, sip-info |

| Step 1 | show sip-ua calls The following sample output shows that the DTMF method is SIP-KPML. Example: Device# show sip-ua calls SIP UAC CALL INFO
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
|---|---|
| Step 2 | show sip-ua
                                             				  calls dtmf-relay sip-info The following
                                          				sample output displays active SIP calls with INFO DTMF Relay mode. Example: Device# show sip-ua calls dtmf-relay sip-info Total SIP call legs:2, User Agent Client:1, User Agent Server:1
SIP UAC CALL INFO
Call 1
SIP Call ID                : 9598A547-5C1311E2-8008F709-2470C996@172.27.161.122
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : sipp
   Called Number           : 3269011111
   CC Call ID              : 2
No.         Timestamp         Digit           Duration      
======================================================= 
0    01/12/2013 17:23:25.615  2                   250            
1    01/12/2013 17:23:25.967  5                   300            
2    01/12/2013 17:23:26.367  6                   300            

Call 2
SIP Call ID                : 1-29452@172.25.208.177
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : sipp
   Called Number           : 3269011111
   CC Call ID              : 1
No.         Timestamp         Digit           Duration      
======================================================= 
0    01/12/2013 17:23:25.615  2                   250            
1    01/12/2013 17:23:25.967  5                   300            
2    01/12/2013 17:23:26.367  6                   300            

   Number of SIP User Agent Client(UAC) calls: 2

SIP UAS CALL INFO
Call 1
SIP Call ID                : 1-29452@172.25.208.177
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : sipp
   Called Number           : 3269011111
   CC Call ID              : 1
No.         Timestamp         Digit           Duration      
======================================================= 
0    01/12/2013 17:23:25.615  2                   250            
1    01/12/2013 17:23:25.967  5                   300            
2    01/12/2013 17:23:26.367  6                   300            

Call 2
SIP Call ID                : 9598A547-5C1311E2-8008F709-2470C996@172.27.161.122
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : sipp
   Called Number           : 3269011111
   CC Call ID              : 2
No.         Timestamp         Digit           Duration      
======================================================= 
0    01/12/2013 17:23:25.615  2                   250            
1    01/12/2013 17:23:25.967  5                   300            
2    01/12/2013 17:23:26.367  6                   300            

   Number of SIP User Agent Server(UAS) calls: 2 |
| Step 3 | show sip-ua
                                             				  history dtmf-relay kpml The following
                                          				sample output displays SIP call history with KMPL DTMF Relay mode. Example: Device# show sip-ua history dtmf-relay kpml Total SIP call legs:2, User Agent Client:1, User Agent Server:1
SIP UAC CALL INFO
Call 1
SIP Call ID                : D0498774-F01311E3-82A0DE9F-78C438FF@10.86.176.119
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 257
No.         Timestamp         Digit           Duration      
======================================================= 

Call 2
SIP Call ID                : 22BC36A5-F01411E3-81808A6A-5FE95113@10.86.176.142
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 256
No.         Timestamp         Digit           Duration      
======================================================= 

   Number of SIP User Agent Client(UAC) calls: 2

SIP UAS CALL INFO
Call 1
SIP Call ID                : 22BC36A5-F01411E3-81808A6A-5FE95113@10.86.176.142
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 256
No.         Timestamp         Digit           Duration      
======================================================= 

Call 2
SIP Call ID                : D0498774-F01311E3-82A0DE9F-78C438FF@10.86.176.119
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 257
No.         Timestamp         Digit           Duration      
======================================================= 

   Number of SIP User Agent Server(UAS) calls: 2 |
| Step 4 | show sip-ua
                                             				  history dtmf-relay sip-notify The following
                                          				sample output displays SIP call history with SIP Notify DTMF Relay mode. Example: Device# show sip-ua history dtmf-relay sip-notify Total SIP call legs:2, User Agent Client:1, User Agent Server:1
SIP UAC CALL INFO
Call 1
SIP Call ID                : 29BB98C-F01311E3-8297DE9F-78C438FF@10.86.176.119
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 252
No.         Timestamp         Digit           Duration      
======================================================= 

Call 2
SIP Call ID                : 550E973B-F01311E3-817A8A6A-5FE95113@10.86.176.142
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 251
No.         Timestamp         Digit           Duration      
======================================================= 

   Number of SIP User Agent Client(UAC) calls: 2

SIP UAS CALL INFO
Call 1
SIP Call ID                : 550E973B-F01311E3-817A8A6A-5FE95113@10.86.176.142
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 251
No.         Timestamp         Digit           Duration      
======================================================= 

Call 2
SIP Call ID                : 29BB98C-F01311E3-8297DE9F-78C438FF@10.86.176.119
   State of the call       : STATE_ACTIVE (7)
   Calling Number          : 2017
   Called Number           : 1011
   CC Call ID              : 252
No.         Timestamp         Digit           Duration      
======================================================= 

   Number of SIP User Agent Server(UAS) calls: 2 |