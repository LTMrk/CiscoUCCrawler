---
doc_id: www-cisco-com-c-en-us-support-docs-voice-call-routing-dial-plans-12425-in-out-dial-peers-html-b216997fc9
source_url: https://www.cisco.com/c/en/us/support/docs/voice/call-routing-dial-plans/12425-in-out-dial-peers.html
retrieved_at: 2026-08-20T23:24:23.924967+00:00
---

Understanding Inbound and Outbound Dial Peers on Cisco IOS Platforms

# Understanding Inbound and Outbound Dial Peers on Cisco IOS Platforms

### Download Options

Updated: February 2, 2006

Document ID: 12425

Contents

## Contents

## Introduction

This document describes the differences between inbound and outbound dial-peers and call legs. Also, this document stresses the importance of inbound dial peer(s) that match when you use non-default services, applications, and/or capabilities to setup and complete voice calls.

## Prerequisites

### Requirements

Readers of this document need to have knowledge of Understanding Dial Peers and Call Legs on Cisco IOS® Platforms .

### Components Used

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command. This document is not restricted to specific software and hardware versions.

### Conventions

For more information on document conventions, refer to the Cisco Technical Tips Conventions .

## Inbound and Outbound Dial Peers and Call Legs

Dial peers are used for both inbound and outbound call legs. It is important to remember that these terms are defined from the perspective of the router/gateway. An inbound call leg originates when an incoming call comes into the router orgateway. An outbound call leg originates when a call is placed or bridged from the router/gateway.

#### Figure 1. Call Legs from the Perspective of the Originating Router/Gateway

For inbound calls from a plain old telephone service (POTS) interface that are destined for the packet network, the originating router/gateway matches an inbound POTS dial peer for the inbound call leg first. Next, the originating router/gateway creates an outbound Voice-Network dial peer such as Voice over IP (VoIP) or Voice over Frame relay (VoFR) for the outbound call leg . After this, the router/gateway bridges the two call legs.

#### Figure 2. Call Legs from the Perspective of the Terminating Router/Gateway

For inbound calls from a Voice Network interface that are destined for a POTS interface, the terminating router/gateway matches an inbound Voice Network dial peer for the inbound call leg. Next, an outbound POTS dial peer is created for the outbound call leg.

## Importance of Inbound Dial Peers

A common misunderstanding with voice dial peers is that they are only configured for outbound functionality, that is, to map a dial string to a remote network device (with the Cisco IOS commands destination-pattern and session target ) or a POTS voice port (with the Cisco IOS commands destination-pattern and port ). However, dial peers need to be configured for inbound functionality when you deal with scenarios where non-default services, applications, and/or capabilities are present.

On inbound POTS call legs received at the originating router/gateway, some non-default services and applications of incoming calls include:

Direct-inward-dial (DID). For more information on this subject, refer to Understanding Direct-Inward-Dial (DID) on Cisco IOS Digital (T1/E1) Interfaces.

Tool Command Language (TCL) Based Applications: Interactive Voice Response (IVR), VoIP Session Initiation Protocol (SIP) transfer, On-Ramp Faxing (in the context of store and forward fax).

When you use such services or applications, it is important to ensure that the correct inbound POTS dial peer configured with the appropriate service or application is matched. For more information, refer to Understanding Inbound and Outbound Dial Peers Matching on IOS Platforms .

When non-default Voice Network capabilities or TCL applications are requested by the originating router/gateway, the terminating router/gateway must match those capabilities and applications configured with an inbound Voice Network dial peer. If the Cisco IOS Software is unable to match a non-default configured inbound dial peer, the software uses an internally defined default dial peer to match the inbound voice calls. The call setup can fail if the incoming call leg has non-default capabilities, services, or applications, and is matched to a default dial peer.

Default Voice-Network capabilities include:

codec g729r8 (payload 20 bytes)

vad enable

dtmf-relay disable

fax-relay disable

fax rate voice

req-qos best-effort

acc-qos best-effort

huntstop disabled

preference 0

playout-delay 40 ms

register E.164 number with GK

digit-strip enabled

session protocol cisco (for H.323).

Note: Default capabilities are not displayed in the router/gateway IOS configuration output. Issue the command show dial-peer voice number in order to view the configured capabilities, services, and applications on POTS and Voice Network dial peers.

Note: The default DSCP for voice is ef codepoint 101110 (RFC 2598) and the default DSCP for signaling is af31 codepoint 011010 (RFC 2597). The default dial-peer, PID 0, does not mark packets to DSCP 0. All voice packets on the routers are marked by default (can be overridden by the dial-peer), signaling with AF31 and media with EF. Calls that match the default dial-peer 0 should also have this behavior.

For more information and a practical example, refer to the case study in Understanding Inbound and Outbound Dial Peers Matching on IOS Platforms .

### Revision History

1.0

06-Dec-2001

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 06-Dec-2001 | Initial Release |