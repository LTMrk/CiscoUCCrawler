---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-212640-troubleshoot-1946ce78d9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/212640-troubleshoot-music-on-hold-failure-when.html
retrieved_at: 2026-08-16T23:12:25.256177+00:00
---

Troubleshoot Music On Hold Failure When Gateway is Integrated Service Router 4431

# Troubleshoot Music On Hold Failure When Gateway is Integrated Service Router 4431

Updated: January 4, 2018

Document ID: 212640

Contents

## Contents

## Introduction

This document describes the configuration needed when call flow includes Integrated Service Router (ISR) 4431 as the gateway and the Music On Hold (MOH) fails with silence for the held party.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of:

- Cisco Unified Communications Manager (CUCM)

- H.323 signaling

### Components Used

The information in this document is based on these software versions:

- CUCM versions 9.x and above

- ISR4431 with IOS XE software

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure you understand the potential impact of any command.

## Problem

Multicast MOH is configured on CUCM and ISR4431 is configured as H.323 gateway. When external callers are placed on hold, they do not hear music but instead hear silence.

## Solution

Step 1. Enable the H.323 debugs on the gateway to be logged to the buffer as shown below.

```
config t no logging console no logging monitor no logging rate-limit no logging queue-limit logging buffered 2000000 debug exit debug voip ccapi inout debug h225 asn1 debug h245 asn1 debug isdn q931
```

Step 2. Run the command clear log to clear the log. Step 3. Run the command show log to confirm that the buffer is cleared. Step 4. Place a test call and when the call is placed on hold, check if the gateway receives H.245 OpenLogicalChannelAck message with IP set to “network '00000000'H”

```
Jan 26 03:12:07.558: H245 MSC INCOMING PDU ::= value MultimediaSystemControlMessage ::= response : openLogicalChannelAck : { forwardLogicalChannelNumber 4 forwardMultiplexAckParameters h2250LogicalChannelAckParameters : } mediaControlChannel unicastAddress : iPAddress : { network '00000000'H tsapIdentifier 1 }
```

Step 5. The snippet shown above indicate:

- CUCM sends OpenLogicalChannelAck with a fake IP address, either all zeros (as shown above) or <CUCM_ip_address> as a place-holder for MOH

- This is the default behavior of sending media simplex streaming

- If there is ISR 4431 in the call flow, whether or not it is one-way or two-way direction, CUCM needs to let the gateway know the MOH IP address and port to avoid a malicious attack

- ISR Generation 2 (G2) platforms (e.g. 2900 and 3900) never check the source IP address and port for incoming Real-time Transport Protocol (RTP) packets. However ISR 4431 is a Generation 3 (G3) platform which checks incoming RTP packets against the media IP address/port determined in the signaling

- If they do not match, ISR G3 drops the packets and this results in silence when call is placed on hold

Step 6. Thus to avoid failure with MOH, use the workaround below on CUCM to enable duplex streaming for the MOH

- Log in to Cisco Unified CM Administration page

- Select System > Service Parameters

- Select Server dropdown and choose the Publisher node

- Select Service dropdown and choose Cisco CallManager (Active)

- Click on the Advanced button

- Locate the Clusterwide Parameters (Service) section

- Duplex Streaming Enabled: Default is False (change to True ) and click Save

Note: There is no requirement to restart any service after above configuration change and has no business impact so can be done in production hours.

### Revision History

1.0

12-Jan-2018

Initial Release

### Contributed by Cisco Engineers

Prashanthi Velpula

Cisco TAC

### This Document Applies to These Products

- 4431 Integrated Services Router

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 12-Jan-2018 | Initial Release |