---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-216690-working-with-large-sip-packets-html-15386dc67e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/216690-working-with-large-sip-packets.html
retrieved_at: 2026-09-07T13:02:49.812148+00:00
---

Working with large SIP packets

# Working with large SIP packets

### Download Options

Updated: November 11, 2020

Document ID: 216690

Contents

## Contents

How do I deal with large SIP packet sizes?

Networks will segment UDP packets with a payload larger than 1480 Bytes to ensure the over packet will not exceed the MTU.

It is common router policy to block segmented UDP packets. Routers must hold each segment of the UDP message in memory until the last segment is received before forwarding the message on. This can be exploited by sending incomplete messages to the router until its memory is full causing the router to fail. For this reason routers that do not contain a fix for this condition often disallow segmented UDP packets.

A workaround to routers that do not (or cannot) handle UDP segmentation is to convert to SIP over TCP. BroadWorks can be set at various locations to send and/or to expect to receive on UDP, TCP or either (unspecified). Below are various locations where these settings are made:

```
AS_CLI/Interface/SIP> get […] supportTcp = true AS_CLI/System/Device/NetworkServers/Routing> get Net Address  Port    Transport   Poll  OpState  Description ===================================================================== ns1.ihs.broadsoft.com           tcp          false  enabled          ns1 ns2.ihs.broadsoft.com           tcp          false  enabled          ns2 AS_CLI/System/CallP/Routing/MediaServerSelection/MediaServerDevice> get Net Address  Port    Transport  Description ===================================================== ms1.ihs.broadsoft.com  5060    tcp          ms1 ms2.ihs.broadsoft.com  5060    tcp          ms2 NS_CLI/System/Device/RoutingNE/Address> get About to access 22 entries. Continue? Please confirm (Yes, Y, No, N): y Retrieving data... Please wait... Routing NE         Address  Cost  Weight  Port    Transport ======================================================================= […] test3        10.2.2.2     1      99  5060    tcp test1        10.6.6.6     1      90  5060    tcp test2        10.1.1.1     1      90  5060    tcp 22 entries found.
```

Many SBCs also support both UDP and TCP. Some SBCs can even convert UDP to TCP. Here is an example configuration from an ACME SD (various locations where protocol can be specified.

```
sip-interface state                          enabled realm-id                       access description                    Public to IHS ACCESS SIP Interface sip-port address                        64.212.220.94 port                           5060 transport-protocol             UDP tls-profile allow-anonymous                all sip-port address                        64.212.220.94 port                           5060 transport-protocol             TCP tls-profile allow-anonymous                all session-agent hostname                       10.48.7.56 ip-address                     10.48.7.56 port                           5060 state                          enabled app-protocol                   SIP app-type transport-method               TCP
```

Devices can also be set to specify protocol. For example, Polycom can be set to TCPonly, TCPpreffered or even allow the DNS response to specify the protocol (DNSnaptr)

Example of a large SIP UDP message

```
2010.08.17 08:22:44:815 EDT | Info       | Sip | +12403645153 | callhalf-171159287:1 udp 1580 Bytes OUT to 10.10.10.1:5060 INVITE sip:2403640001@10.10.10.1:5060;user=phone;transport=udp SIP/2.0 Via:SIP/2.0/UDP 10.10.10.2;branch=z9hG4bKBroadWorks.11l7pom-10.10.10.1V5060-0-13480-1064780560-1282047764815- From:\"test-cc1 travis\";tag=1064780560-1282047764815- To:\"Mike - Test Acct Inmon\" Call-ID:BW082244815170810-243190739@10.10.10.2 CSeq:13480 INVITE Contact: Remote-Party-ID:\"test-cc1 travis\";screen=yes;party=calling;privacy=off;id-type=subscriber RPID-Privacy:party=calling;privacy=off;id-type=subscriber Proxy-Require:privacy Diversion:\"Mike - Test Acct Inmon\";privacy=off;diversion-inhibited;reason=follow-me;counter=5,\"Mike - Test Acct Inmon\";privacy=off;reason=follow-me;counter=1,\"test-cc1 travis\";privacy=off;hg-cc;delay-ccm;reason=unknown;counter=1 Supported: Allow:ACK,BYE,CANCEL,INFO,INVITE,OPTIONS,PRACK,REFER,NOTIFY,UPDATE Accept:multipart/mixed,application/dtmf-relay,application/media_control+xml,application/sdp,application/x-broadworks-call-center+xml Max-Forwards:5 Content-Type:application/sdp Content-Length:283 v=0 o=BroadWorks 1618137 1 IN IP4 10.10.10.2 s=- c=IN IP4 10.10.10.2 t=0 0 m=audio 16580 RTP/AVP 0 8 18 101 a=rtpmap:0 PCMU/8000 a=rtpmap:8 PCMA/8000 a=rtpmap:18 G729/8000 a=rtpmap:101 telephone-event/8000 a=silenceSupp:on - - - - a=fmtp:101 0-15 a=ptime:20 a=sendrecv
```

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- BroadWorks