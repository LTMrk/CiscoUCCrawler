---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-ios-gateways-session-initiation-protocol-sip-212411-how-to-get-d28a9c53e4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/ios-gateways-session-initiation-protocol-sip/212411-how-to-get-packet-capture-from-vxml-gate.html
retrieved_at: 2026-08-16T15:56:57.352251+00:00
---

How to Get Packet Capture from VXML Gateway for Signal and Voice Analysis

# How to Get Packet Capture from VXML Gateway for Signal and Voice Analysis

### Download Options

Updated: October 24, 2017

Document ID: 212411

Contents

## Contents

## Introduction

This document describes how to get a packet capture (pcap) from a VXML Gateway for signal and voice analysis.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Unified Customer Voice Portal (CVP)

Voice Extensible Markup Language Gateway (VXML GW)

- Whireshark tool

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Take Packet Capture on VXML Gateway

You can get a pcap to check signaling and media from the Cisco VXML GW with this procedure for interface g0/0 . You need to change inteface name in the command to the appropriate one.

```
conf t ip traffic profile test mode capture bidirectional exit int g0/0 ip traffic apply test size 20000000 end traffic int g0/0 clear traffic int g0/0 start
```

VXML gateway capturing traffic, so make a test call and quickly stop the packet capture.

```
traffic int g0/0 stop
```

In order to copy the pcap to an TFTP server type this command.

```
traffic int g0/0 copy tftp://x.x.x.x/g00.pcap
```

In order to copy the pcap to an FTP server type this command.

```
traffic int g0/0copy ftp://username:password@x.x.x.x/g00.pcap
```

The screenshot shows the pcap file port1.pcap opened with Wireshark tool.

## Verify

In order to verify that the packet capture is valid use this procedure.

Step 1. Filter sip signalling.

Enter sip keyword in Filter textbox.

Step 2. Open the RTP streams with Wireshark Player.

- Navigate to Telephony - Voip Calls

- Choose the call in question

- Select Player

Step 3. Click Decode.

Step 4. Playback the recording.

In order to playback the recorded conversation select the decoded graph for the call in question and select Play .

The procedure described can be used to troubleshoot issues with audio quality, one-way audio or dead air conditions.

These debug commands can be typed on the VXML gateway for additional diagnosis.

```
debug ccsip mess debug ccsip error debug voip ccapi inout debug voip dialpeer inout debug http client all debug voip application script debug voip application vxml debug voip rtp session named-events debug voip rtp sess nse debug voip rtp
```

### Contributed by Cisco Engineers

Ricardo Mancera

Cisco TAC Engineer

Edited by Natalia Fuentes Fuentes

### This Document Applies to These Products

- IOS Gateways with Session Initiation Protocol (SIP)

- Unified Border Element