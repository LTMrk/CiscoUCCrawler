---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-webex-telepresence-html-92ed9f4e7a
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-webex-telepresence.html
retrieved_at: 2026-08-16T15:51:49.064017+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter:  WebEx Telepresence Media Support Over Single SIP Session

## Chapter:  WebEx Telepresence Media Support Over Single SIP Session

# WebEx Telepresence Media Support Over Single SIP Session

The WebEx Telepresence Media Support over Single SIP Session feature provides support for end-to-end negotiation of up to
                        6 m-lines or media lines over a single Session Initiation Protocol (SIP) session. The media types can be audio, video, or
                        application.

## Feature Information for WebEx Telepresence Media Support Over Single SIP Session

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

WebEx Telepresence Media Support Over Single SIP Session

Baseline Functionality

The WebEx Telepresence Media Support over Single SIP Session feature provides support for end-to-end negotiation of up to
                                       6 m-lines or media lines over a single Session Initiation Protocol (SIP) session. The media types can be audio, video, or
                                       application.

## Restrictions for WebEx Telepresence Media Support Over Single SIP Session

High availability  is not supported with multiple m-lines.

Only single dynamic payload type in the m-line for H.224 protocol is supported.

Payload type interworking for Aggregation Service Routers (ASR) is not supported, so dynamic payload type is negotiated end-to-end.

## Information About WebEx Telepresence Media Support Over Single SIP Session

The WebEx Telepresence Media Support over Single SIP Session feature provides the following support:

End-to-end negotiation of multiple m-lines.

Negotiation of Binary Floor Control  Protocol (BFCP), IX, and H.224 protocol m-lines (m=application)
                                 and creation of Real-time Transport Protocol (RTP) or UDP streams for the same.

Early-Offer (EO-EO) and Delayed-Offer (DO-DO) calls' support by the Cisco Unified Border Element (Cisco UBE) with multiple
                                 m-lines.

End-to-end negotiation of multiple m-lines of same media type for video and application (but not audio).

Mid-call escalation and de-escalation for multiple application and video m-lines.

Secure RTP (SRTP) passthrough for all RTP streams (audio, video, and application).

SRTP-RTP interworking for video (ASR only).

Multiple dynamic payload types in the same m-line for the H.264 codec.

You can use the show voip rtp connections and show call active video compact commands to see the details about additional video and application streams.

## Monitoring WebEx Telepresence Media Support Over Single SIP Session

Perform this task to see the details about additional video and application streams. The show commands can be entered in any order.

### SUMMARY STEPS

- enable

- show call active video compact

- show voip rtp connections

- show sip-ua calls

### DETAILED STEPS

Step 1

enable

Enables privileged EXEC mode.

### Example:

```
Device> enable
```

Step 2

show call active video compact

Displays a compact version of  call information for Skinny Call Control Protocol
                                          (SCCP), SIP, and H.323 video calls in
                                          progress. 
                                          			 The codec type, negotiated codec, and remote media ports are displayed.

### Example:

```
Device# show call active video compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 2
         1 ANS     T5     H264        VOIP-VIDEO  P332211       9.45.38.39:2448
         6 ORG     T5     H264        VOIP-VIDEO  P1111         9.45.38.39:2438
```

Step 3

show voip rtp connections

Displays RTP named event packets. In the following sample output, two RTP connections are displayed for each m-line and a
                                          total of 10 RTP connections are displayed for 5 m-lines.

### Example:

```
Device# show voip rtp connections VoIP RTP active connections :
No. CallId     dstCallId  LocalRTP  RmtRTP   LocalIP                      RemoteIP
1     1          6          16384    54024  192.0.2.123                   192.0.2.39
2     2          7          16386    2448   192.0.2.123                   192.0.2.39
3     3          8          16400    5070   192.0.2.123                   192.0.2.39
4     4          9          16388    2450   192.0.2.123                   192.0.2.39
5     5          10         16402    2452   192.0.2.123                   192.0.2.39
6     6          1          16390    58121  192.0.2.123                   192.0.2.39
7     7          2          16392    2438   192.0.2.123                   192.0.2.39
8     8          3          16394    5070   192.0.2.123                   192.0.2.39
9     9          4          16396    2440   192.0.2.123                   192.0.2.39
10    10         5          16398    2442   192.0.2.123                   192.0.2.39
Found 10 active RTP connections
```

Step 4

show sip-ua calls

Displays active user agent client (UAC) and user agent server
                                          (UAS) information on Session Initiation Protocol (SIP) calls.

### Example:

```
Device# show sip-ua calls Total SIP call legs:2, User Agent Client:1, User Agent Server:1 SIP UAC CALL INFO Call 1
SIP Call ID                : 72B6C784-753E11E2-FFFFFFFF8008B555-FFFFFFFFE340699E@9.45.47.123
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 332211
   Called Number           : 1111
   Bit Flags               : 0xC04018 0x10000100 0x80
   CC Call ID              : 6
   Source IP Address (Sig ): 9.45.47.123
   Destn SIP Req Addr:Port : [9.45.38.39]:5267
   Destn SIP Resp Addr:Port: [9.45.38.39]:5267
   Destination Name        : 9.45.38.39
   Number of Media Streams : 5
   Number of Active Streams: 5
   RTP Fork Object         : 0x0
   Media Mode              : flow-through Media Stream 1 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 6
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g711ulaw (160 bytes)
     Codec Payload Type       : 0
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : NoneLocal QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16390
     Media Dest IP Addr:Port  : [9.45.38.39]:58121 Media Stream 2 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 7
     Stream Type              : video (7)
     Stream Media Addr Type   : 1
     Negotiated Codec         : h263 (0 bytes)
     Codec Payload Type       : 97
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16392
     Media Dest IP Addr:Port  : [9.45.38.39]:2438 Media Stream 3 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 8
     Stream Type              : application (8)
     Stream Media Addr Type   : 1
     Negotiated Codec         : No Codec    (0 bytes)
           Codec Payload Type       : 255 (None)
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16394
     Media Dest IP Addr:Port  : [9.45.38.39]:5070 Media Stream 4 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 9
     Stream Type              : video (7)
     Stream Media Addr Type   : 1
     Negotiated Codec         : h263 (0 bytes)
     Codec Payload Type       : 97
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16396
     Media Dest IP Addr:Port  : [9.45.38.39]:2440 Media Stream 5 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 10
     Stream Type              : application (8)
     Stream Media Addr Type   : 1
     Negotiated Codec         : H.224 (0 bytes)
     Codec Payload Type       : 107
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16398
     Media Dest IP Addr:Port  : [9.45.38.39]:2442

Options-Ping    ENABLED:NO    ACTIVE:NO
   Number of SIP User Agent Client(UAC) calls: 1
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| WebEx Telepresence Media Support Over Single SIP Session | Baseline Functionality | The WebEx Telepresence Media Support over Single SIP Session feature provides support for end-to-end negotiation of up to
                                       6 m-lines or media lines over a single Session Initiation Protocol (SIP) session. The media types can be audio, video, or
                                       application. |

| Step 1 | enable Enables privileged EXEC mode. Example: Device> enable |
|---|---|
| Step 2 | show call active video compact Displays a compact version of  call information for Skinny Call Control Protocol
                                          (SCCP), SIP, and H.323 video calls in
                                          progress. 
                                          			 The codec type, negotiated codec, and remote media ports are displayed. Example: Device# show call active video compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 2
         1 ANS     T5     H264        VOIP-VIDEO  P332211       9.45.38.39:2448
         6 ORG     T5     H264        VOIP-VIDEO  P1111         9.45.38.39:2438 |
| Step 3 | show voip rtp connections Displays RTP named event packets. In the following sample output, two RTP connections are displayed for each m-line and a
                                          total of 10 RTP connections are displayed for 5 m-lines. Example: Device# show voip rtp connections VoIP RTP active connections :
No. CallId     dstCallId  LocalRTP  RmtRTP   LocalIP                      RemoteIP
1     1          6          16384    54024  192.0.2.123                   192.0.2.39
2     2          7          16386    2448   192.0.2.123                   192.0.2.39
3     3          8          16400    5070   192.0.2.123                   192.0.2.39
4     4          9          16388    2450   192.0.2.123                   192.0.2.39
5     5          10         16402    2452   192.0.2.123                   192.0.2.39
6     6          1          16390    58121  192.0.2.123                   192.0.2.39
7     7          2          16392    2438   192.0.2.123                   192.0.2.39
8     8          3          16394    5070   192.0.2.123                   192.0.2.39
9     9          4          16396    2440   192.0.2.123                   192.0.2.39
10    10         5          16398    2442   192.0.2.123                   192.0.2.39
Found 10 active RTP connections |
| Step 4 | show sip-ua calls Displays active user agent client (UAC) and user agent server
                                          (UAS) information on Session Initiation Protocol (SIP) calls. Example: Device# show sip-ua calls Total SIP call legs:2, User Agent Client:1, User Agent Server:1 SIP UAC CALL INFO Call 1
SIP Call ID                : 72B6C784-753E11E2-FFFFFFFF8008B555-FFFFFFFFE340699E@9.45.47.123
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 332211
   Called Number           : 1111
   Bit Flags               : 0xC04018 0x10000100 0x80
   CC Call ID              : 6
   Source IP Address (Sig ): 9.45.47.123
   Destn SIP Req Addr:Port : [9.45.38.39]:5267
   Destn SIP Resp Addr:Port: [9.45.38.39]:5267
   Destination Name        : 9.45.38.39
   Number of Media Streams : 5
   Number of Active Streams: 5
   RTP Fork Object         : 0x0
   Media Mode              : flow-through Media Stream 1 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 6
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g711ulaw (160 bytes)
     Codec Payload Type       : 0
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : NoneLocal QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16390
     Media Dest IP Addr:Port  : [9.45.38.39]:58121 Media Stream 2 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 7
     Stream Type              : video (7)
     Stream Media Addr Type   : 1
     Negotiated Codec         : h263 (0 bytes)
     Codec Payload Type       : 97
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16392
     Media Dest IP Addr:Port  : [9.45.38.39]:2438 Media Stream 3 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 8
     Stream Type              : application (8)
     Stream Media Addr Type   : 1
     Negotiated Codec         : No Codec    (0 bytes)
           Codec Payload Type       : 255 (None)
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16394
     Media Dest IP Addr:Port  : [9.45.38.39]:5070 Media Stream 4 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 9
     Stream Type              : video (7)
     Stream Media Addr Type   : 1
     Negotiated Codec         : h263 (0 bytes)
     Codec Payload Type       : 97
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16396
     Media Dest IP Addr:Port  : [9.45.38.39]:2440 Media Stream 5 State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 10
     Stream Type              : application (8)
     Stream Media Addr Type   : 1
     Negotiated Codec         : H.224 (0 bytes)
     Codec Payload Type       : 107
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [9.45.47.123]:16398
     Media Dest IP Addr:Port  : [9.45.38.39]:2442

Options-Ping    ENABLED:NO    ACTIVE:NO
   Number of SIP User Agent Client(UAC) calls: 1 |