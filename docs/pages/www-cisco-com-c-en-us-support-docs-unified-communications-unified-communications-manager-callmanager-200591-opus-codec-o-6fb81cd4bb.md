---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200591-opus-codec-o-6fb81cd4bb
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200591-OPUS-Codec-Overview.html
retrieved_at: 2026-08-21T13:55:13.560601+00:00
---

OPUS Codec Overview

# OPUS Codec Overview

### Download Options

Updated: July 27, 2016

Document ID: 200591

Contents

## Contents

## Introduction

This document describes the presence of OPUS codec, which was not available earlier, in Cisco Unified Communications Manager (CUCM) version 11.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software  versions:

- Cisco Unified Communications Manager version 11.0

Note : Not all end points support OPUS codec at the moment. Please review the feature guide for the corresponding end point.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Opus is an interactive speech and audio codec. It is designed to handle a wide range of interactive audio applications, which includes Voice over IP, videoconferencing, in-game chat, and even live distributed music performances. It scales from low bitrate narrowband speech at 6 kbit/s to very high quality stereo music at 510 kbit/s. Opus uses both Linear Prediction (LP) and the Modified Discrete Cosine Transform (MDCT) to achieve good compression of both speech and music. It is royalty free, and the algorithms are openly documented. A reference implementation, which includes the source code, is publicly available.

## Session Description Protocol (SDP) Syntax and Semantics

New encoding name (Media subtype):

OPUS (case insensitive)

Clock rate: Opus supports several clock rates; only the highest clock rate, 48000 Hz, is advertised in the SDP. The actual clock rate of the corresponding media is signaled inside the payload.

Opus defines these optional media format (fmtp) parameters.

These parameters are declarative in nature, which indicates either the receive capability or send capability.

- Maxaveragebitrate

- Maxplaybackrate

- Minptime

- Stereo

- Cbr

- Useinbandfec

- usedtxsprop-maxcapturerate

- sprop-stereo

CUCM passes through fmtp optional parameters from one side to other if opus codec is negotiated in the call.

Cisco recommends to use payload 114 for Opus codec.

## Sample SDP

Example 1:

```
m=audio 54312 RTP/AVP 100       a=rtpmap:100 opus/48000/2
```

Example 2:

```
m=audio 54312 RTP/AVP 99       a=rtpmap:99 opus/48000/2       a=fmtp:99 maxplaybackrate=16000; sprop-maxcapturerate=16000;       maxaveragebitrate=20000; stereo=1; useinbandfec=1; usedtx=0
```

## Offer/Answer Examples

Example 1:

Both sides offer a single packet-tracer (PT) but B-side offer does not have fmtp line. Unified Communications Manager (UCM) forwards the fmtp line in a transparent manner.

Example 2:

A side offers two Opus profiles (payloads) but B side offers only one profile. UCM shall forward both payloads from A’s offer to B regardless of the fact that B is can receive multiple codecs in the answer.

Example 3:

Both A and B offer two payloads. UCM passes on the both payloads in the respective answer regardless of their support for multiple payloads (codecs) in the answer SDP.

Example 4:

Offers from A and B contain opus codec amongst others and both can receive multiple codecs in the answer. UCM selects common sets of codecs from both offers and passes them in the respective answer.

## Configure

Admin Changes

Adds a new Service Parameter under CallManager as shown in the image:

Available Options:

- Enabled for All Devices

- Enabled for All Devices Except Recording-Enabled Devices

- Disabled

The default value for this Service Parameter is Enabled for All Devices .

Added Opus Codec in the Audio codec preference list.

- In Factory default Low loss.

- In Factory default Lossy.

## Verify

You can verify the call statistics option on the phone to ensure OPUS codec is negotiated for the call.

In SDL traces, Opus codec comes with enum number 90 as shown in these traces:

```
00935455.000 |11:21:48.017 |SdlSig   |SDPOfferInd                            |waitSDPResponse                |SIPInterface(1,100,76,60)        |SIPCdpc(1,100,82,79)             |1,100,14,38003.16^10.77.29.78^*          |[R:N-H:0,N:7,L:0,V:0,Z:0,D:0] ] nAudio=1 stackIdx=1 audioCapCount=11 Caps[43(0),44(0),40(0),41(0),6(20),10(10),11(20),12(20),2(20),4(20),90(20)] port=16474 IP= ipAddrType=0 ipv4=10.77.31.10 SDPMode=0 mediaAttr=0x0 SP=F RTP=T SRTP=F idle=F QoS=F enabledMask=0 rtcbFbCount=0LatentCaps=null TCL_UNSPECIFIED ptime=0 ~
```

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

27-Jul-2016

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-Jul-2016 | Initial Release |