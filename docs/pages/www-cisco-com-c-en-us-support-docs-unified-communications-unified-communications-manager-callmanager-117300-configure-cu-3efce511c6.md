---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-117300-configure-cu-3efce511c6
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/117300-configure-cube-00.html
retrieved_at: 2026-08-16T15:56:24.144642+00:00
---

Configure CUCM to CUBE Integration - Configuration Example

# Configure CUCM to CUBE Integration - Configuration Example

### Download Options

Updated: January 22, 2014

Document ID: 117300

Contents

## Contents

## Introduction

This document describes the basics of Cisco Unified Border Element (CUBE) configuration with Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that your system does not have Domain Name System (DNS) configuration and that you have knowledge of these topics:

- CUCM Version 8.6 through Version 10.x

- Cisco IOS ® Version 15.1(2)T and later

Note : The IP addresses vary based on the addressing schemes in the network.

### Components Used

The information in this document is based on the fact that any number of CUCM servers, any Cisco Integrated Services Router (ISR), ISR Generation 2 (G2), or Cisco Aggregation Services Router (ASR) can be a CUBE. No Digital Signal Processors (DSPs) are required for basic CUBE operation.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### The CUBE-Side of the CUCM-to-CUBE Integration

When you first set up a CUBE, you must enable the router in order to route calls like a CUBE. This image shows a basic Voice Service VoIP configuration on a CUBE:

Here are some important points about this configuration:

- The first line of the configuration is mode border-element , which enables CUBE on a router. Some devices do not have this configuration when they operate as a CUBE.

- Allow-connections sip to sip enables the CUBE to accept Session Initiation Protocol (SIP) calls and route them as SIP calls. There are options for H323 as well.

- Fax protocol t38 is a default configuration for ISR G2 routers. It is not needed for CUBE configuration.

- Early-offer forced allows CUBE to route calls in a Delayed Offer to Early Offer scenario. Almost all of the providers require Early Offer SIP calls. It is actually recommended to send Early Offer from CUCM in order to avoid early media cut-through issues.

- Midcall-signaling passthru is only for SIP-to-SIP calls. It is required for some supplementary services to work.

- G729 annexb-all is optimal in cases where CUBE negotiates with providers who do not adhere to the RFC format for G729r8 and G729br8 codecs.

### Dial-Peer Configuration on CUBE

Dial-peers on CUBE are like other dial-peers on Cisco IOS gateways. The difference is that the calls route from one VoIP dial-peer to another VoIP dial-peer.

Notice that there are two dial-peers here: incoming and outgoing. CUBE always matches two dial-peers. Incoming dial-peers are from the CUBE perspective, either from the CUCM or from the SIP provider. Outgoing dial-peers are sent towards the CUCM or to the SIP Provider.

ICisco recommends that you perform most of the digit manipulation on CUCM through Significant Digits, External Phone Number Mask, and Translations. Refer to the Understanding Inbound and Outbound Dial Peers Matching on IOS Platforms article for more information about dial-peers.

Digit manipulation can be performed on CUBE, the same way it is performed on Cisco IOS Voice Gateways. Refer to the Number Translation using Voice Translation Profiles article for more information.

### Basic IP Addressing

IP addressing on CUBE is accomplished the same way as on other Cisco IOS devices, but it uses the routing table in order to determine from which interface the CUBE sources SIP traffic. The show ip route A.B.C.D command provides information about the interface the CUBE uses in order to source SIP traffic. This is important when calls are sent to CUCM and when calls are sent to an SIP provider. Static routes can be needed in order to make this work.

In some cases, you have to bind SIP to a particular interface, such as a loopback interface on the CUBE. SIP binding can cause side effects, such as when the CUBE does not listen for SIP traffic on a particular interface. Cisco recommends that you not use bindings and let the routing table decide, but this is not always possible. You can apply SIP bindings under Voice Service VoIP > SIP , or on individual dial-peers. SIP bindings are explained more in the Configuring SIP Bind Features article.

### Voice-Class Codecs on CUBE

Voice-class codecs are used for CUBE in order to offer multiple codecs when calls use a particular VoIP dial-peer. This is the same as it was on a Cisco IOS Voice Gateway, but when it is a CUBE, codecs are filtered from one VoIP call leg to the other. It uses codecs that are available on both the incoming dial-peer and the outgoing dial-peer. The codecs that match both are sent offers. When CUBE receives a SIP message with Session Description Protocol (SDP), it also matches this against the voice-class codecs. This allows CUBE to filter codecs based on what is received from the SIP message with SDP, the inbound dial-peer, and the outbound dial-peer. The other SIP User Agent (UA) then responds to the codecs offered.

The voice-class codec in the previous image contains three codecs, g729r8 , g711ulaw , or g711alaw . The image shows them in the order in which the Cisco IOS gateway prioritizes how the codecs are offered to the far end.  Voice-class codecs are applied to dial-peers.

### Cisco IOS Toll-Fraud Application

The toll-fraud application in Cisco IOS is useful because it can prevent unwanted SIP access, but without proper planning, it can cause some issues with normal operation. The toll-fraud application in Cisco IOS allows the router to specify the devices that can communicate with it to make calls (H323 or SIP). IP addresses that are used as session targets on dial-peers are automatically allowed to send calls to the Cisco IOS Voice Gateway without extra configuration. This usually includes all of the SIP Providers and CUCM servers in the environment, but not always. If it does not, these must be manually added to the CUBE. Only the signaling addresses must be added, not the media addresses. Refer to the Toll-Fraud Prevention Feature in IOS Release 15.1(2)T article for more information.

### The CUCM-Side of the CUCM-to-CUBE Integration

Note : This checkbox is used when end users do not want to have an MTP used on every call.

## Verify

Make test calls in order to verify that your configuration works correctly. If the test calls fail, take detailed CUCM service traces or CUBE traces in order to understand the problem.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

13-Feb-2014

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 13-Feb-2014 | Initial Release |