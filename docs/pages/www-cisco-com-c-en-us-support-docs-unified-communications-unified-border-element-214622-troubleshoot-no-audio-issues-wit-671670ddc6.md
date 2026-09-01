---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-border-element-214622-troubleshoot-no-audio-issues-wit-671670ddc6
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-border-element/214622-troubleshoot-no-audio-issues-with-hairpi.html
retrieved_at: 2026-09-01T17:32:03.058889+00:00
---

Troubleshoot No-way Audio Issue with Hairpin Calls on CUBE

# Troubleshoot No-way Audio Issue with Hairpin Calls on CUBE

### Download Options

Updated: July 18, 2023

Document ID: 214622

Contents

## Contents

## Introduction

This document describes how to troubleshoot the no-way audio issue with hairpin calls on Cisco Unified Border Element (CUBE).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Session Initiation Protocol (SIP)

- How to configure and use the CUBE

- Media Flow-Through and Flow-Around

### Components Used

The information in this document is based on these hardware and software versions:

- Cisco Unified Communications Manager (CUCM) - 11.5.1.10000-5

- CUBE - 15.5(3)S5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Network Topology

## Problem

A hairpin call is an incoming call from an Internet Telephony Service Provider (ITSP) forwarded or transferred back to the ITSP, this results in no-way audio, regular calls to ITSP from IP phones work fine.

As per SIP RFC 3264, the media socket negotiations between the SIP User Agent Client (UAC) and SIP User Agent Server (UAS) happen through Session Description Protocol (SDP) in Offer/Answer model, this is followed by every Voice ove IP (VoIP) product manufacturer.

Some ITSPs do not consider the IP address and port information in the SDP because of their firewall implementation, therefore, the socket has to be initiated by the far end (in this case, CUBE). ITSP requires the far end to send some Real-Time Transport Protocol (RTP) packets towards it, once ITSP receives the RTP packets, it transmits the packets to the source IP of the received packets.

In a call between an IP phone and the ITSP, which does not feature the hairpin, this problem does not occur, this is because the IP phone sends dummy RTP packets after it opens the required ports.

When a call comes from the ITSP and sent back to them, both, the call initiator and the call receiver don't send any streams unless they receive a stream from someone in the path of the call, this is a deadlock situation.

## Verify

In order to validate that the connection is succesfully established, run this command: show voip rtp connections .

```
Max Ports Available: 19999, Ports Reserved: 101, Ports in Use: 4
Port range not configured, Min: 8000, Max: 48199

                                                Ports       Ports       Ports     
Media-Address Range                             Available   Reserved    In-use    

Default Address-Range                           19999       101         4         

VoIP RTP active connections :
No. CallId     dstCallId  LocalRTP RmtRTP LocalIP                                       RemoteIP                               
1     21         22         16424    16568  10.106.36.169                               10.106.108.72                          
2     22         21         16426    24602  10.106.36.169                               10.106.123.29                          
3     23         24         16428    24600  10.106.36.169                               10.106.123.29                          
4     24         23         16430    16570  10.106.36.169                               10.106.108.72                          
Found 4 active RTP connections
```

Run the command show call active voice brief in order to see the Rx/Tx counters of all the 4 call legs from the perspective of CUBE as 0/0.

```
Total call-legs: 4
35E9 : 21 7441740ms.1 (*13:00:22.857 UTC Sat May 20 2017) +4080 pid:123 Answer 5655 connected
 dur 00:24:17 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0                                            <<<<
 IP 10.106.108.72:16568 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms g711ulaw TextRelay: off Transcoded: No
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00

35E9 : 22 7441740ms.2 (*13:00:22.857 UTC Sat May 20 2017) +4080 pid:123 Originate 7961 connected
 dur 00:24:17 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0                                            <<<< 
 IP 10.106.123.29:24602 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms g711ulaw TextRelay: off Transcoded: No
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00

0    : 23 7441780ms.1 (*13:00:22.897 UTC Sat May 20 2017) +4020 pid:124 Answer 5655 connected
 dur 00:24:17 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0                                            <<<<
 IP 10.106.123.29:24600 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms g711ulaw TextRelay: off Transcoded: No
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00

0    : 24 7441780ms.2 (*13:00:22.897 UTC Sat May 20 2017) +4010 pid:124 Originate 7961 connected
 dur 00:24:17 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0                                            <<<<
 IP 10.106.108.72:16570 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms g711ulaw TextRelay: off Transcoded: No
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
```

Note : In case routers use IOS-XE, run tthis command in order to validate the Rx/Tx counters:

```
voice service voip
 media bulk-stats
```

It is not recommended to run this command when the call volume is high, ensure you run this command when the CPU is less than 30%.

## Solution

### Software Media Termination Point (MTP)

This is the preferred method to overcome the problem. CUCM software MTPs are capable to send dummy RTP packets. In a hairpin call, the software MTP supply dummy RTP packets to both, the call initiator and the call receiver, therefore, the ITSP receives these packets and replies with RTP to the software MTP.

Ensure that Media Termination Point Required checkbox is checked on the Trunk Configuration page. Navigate to Device > SIP trunk and select the Media Resource Group List (MRGL) of that trunk, validate that it contains at least one software MTP.

- Note : Hardware MTP cannot send dummy RTP streams. Ensure that the MRGL associated with the trunk invokes only software MTP. Software MTP can only bridge G711 calls, ensure the end to end call flow must use G711 for this workaround to work.

The next image shows how Dummy RTP payload looks in Wireshark:

### Media Flow-Around

With Media Flow-Around, the signaling packets terminate and originate on CUBE but media packets bypass CUBE and flow directly between endpoints.

```
voice service voip
 media flow-around
```

Call with Media Flow-Around

Caution : This can impact CUBE functionality as it can't terminate media for any calls. RTP bypasses the CUBE and flows directly between the endpoints. In this case, i t flows directly between the ITSPs.

Dial-peer configuration mode for Media Flow-Through doesn’t take effect if you have Media Flow-Around configured under global configuration.

Configuration

- Configure Media Flow-Around under global configuration.

- Create a Voice-Class Media with Media Flow-Through.

- Apply Voice-Class Media on all the dial-peers in which Media Flow-Through is expected to be used.

- The dial-peers which don't have this configuration falls to Media Flow-Around as it is configured globally.

```
Voice service voip media flow-around voice-class media 10
 media flow-through

dial-peer voice 1 voip
 Description ** Inbound dial-peer **
 voice class media 10

dial-peer voice 2 voip
 Description ** Outbound dial-peer **
 voice class media 10
```

### Media Anti-Trombone

This feature works similar to Media Flow-Around, however, it impacts less. First, it looks for looped or hairpin calls, if a hairpin call is found, this feature triggers another round of media negotiation for the identified call. At the end of this negotiation, the CUBE is no longer part of the media path.

Both parties, CUBE and ITSP, need to support the Anti-Trombone feature in order for this to work.

```
voice service voip
 media anti-trombone
```

Call with Media Anti-Trombone

Note : Validate the restrictions before you configure Media Anti-Trombone at http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/media-path.html

### Enable CUBE to send STUN packets in the negotiated media IP/Port

Enable the CUBE to send locally generated STUN requests/packets (these stun packets are UDP packets with the same media IP/port numbers) to be sent over the negotiated media path, the devices in the media path can clear the path after getting these stun packets after verifying the IP/Port/transport protocol if these devices are not verifying the actual application data:

voice service voip

stun

stun flowdata agent-id 1 boot-count 4

stun flowdata shared-secret 0 Password123$

voice class stun-usage 1

stun usage firewall-traversal flowdata

dial-peer voice 2000 voip

Description ** Inbound dial-peer from ITSP **

voice-class stun-usage 1

This can be done on the dial-peer used to rerceive the call from ITSP or dial-peer used to send the call to ITSP or both of them.

### Revision History

1.0

19-Jul-2023

Initial Release

### Contributed by Cisco Engineers

Rajarshee Dhar

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Border Element

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Jul-2023 | Initial Release |