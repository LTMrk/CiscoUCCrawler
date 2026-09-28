---
doc_id: www-cisco-com-c-en-us-support-docs-voice-h323-14003-e-m-overview-html-d0749bfdf7
source_url: https://www.cisco.com/c/en/us/support/docs/voice/h323/14003-e-m-overview.html
retrieved_at: 2026-08-21T07:17:27.026237+00:00
---

Analog E&M Voice Signaling Overview

# Analog E&M Voice Signaling Overview

### Download Options

Updated: February 2, 2006

Document ID: 14003

Contents

## Contents

## Introduction

Analog trunk circuits connect automated systems, such as a private branch exchange (PBX) and the network such as a central office (CO). The most common form of analog trunking is the E&M interface. E&M Signaling is commonly referred to as "ear & mouth" or "recEive and transMit", but its origin comes from the term earth and magnet. Earth represents electrical ground and magnet represents the electromagnet used to generate tone.

E&M signaling defines a trunk circuit side and a signaling unit side for each connection similar to the data circuit-terminating equipment (DCE) and data terminal equipment (DTE) reference type. Usually the PBX is the trunk circuit side and the Telco, CO, channel-bank, or Cisco voice enabled platform is the signaling unit side.

Note: The Cisco analog E&M interface functions as the signaling unit side and it expects the other side to be a trunk circuit. When you use E&M interface models Type II and Type V, two signaling unit sides can be connected back to back by the appropriate crossing of the signaling leads. When you use E&M Type I interfaces, two signaling unit sides cannot be connected back to back.

For more information on the trunk circuit and signaling unit wiring, refer to Understanding and Troubleshooting Analog E&M Interface Types and Wiring Arrangements .

## Prerequisites

### Requirements

Readers of this document need to have knowledge of these topics:

Cisco 2600, 3600, and VG200 platforms require a voice network module and an E&M voice interface card (VIC).

Cisco 1750 and 1760 platforms only require the E&M VIC and a Packet Voice DSP Module (PVDM).

Cisco MC3810 platforms requires an analog voice module (AVM) with an E&M analog personality module (APM-EM) installed in the AVM and a Voice Compression Module (VCM).

For more information on the Voice Network Modules and the E&M VIC, refer to Understanding Voice Network Modules , and Understanding E&M Voice Interface Cards .

A typical analog E&M circuit is shown in this diagram:

### Components Used

Analog E&M is supported on Cisco 1750, 1760, 2600, 3600, VG200, and MC3810 models.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

### Conventions

For more information on document conventions, refer to the Cisco Technical Tips Conventions .

## Analog E&M Parameters

There are four main parameters that define the different analog E&M implementations. They are listed and explained here:

### E&M Interface Types and Wiring Arrangement

There are five different E&M interface types or models named Type I, II, III, IV, and V (Type IV is not supported on Cisco platforms). Each type has a different wiring arrangement, hence a different approach to transmit E&M supervision signaling (on-hook / off-hook signaling). The signaling side sends its on-hook/off-hook signal over the E-lead. The trunking side sends the on-hook/off-hook over the M-lead.

For more information and pinout diagrams of E&M types, refer to Understanding and Troubleshooting Analog E&M Interface Types and Wiring Arrangements.

E&M Type I —This is the most common interface in North America.

Type I uses two leads for supervisor signaling: E, and M.

During inactivity, the E-lead is open and the M-lead is connected to the ground.

The PBX (that acts as trunk circuit side) connects the M-lead to the battery in order to indicate the off-hook condition.

The Cisco router/gateway (signaling unit) connects the E-lead to the ground in order to indicate the off-hook condition.

E&M Type II —Two signaling nodes can be connected back-to-back.

Type II uses four leads for supervision signaling: E, M, SB, and SG.

During inactivity both the E-lead and M-lead are open.

The PBX (that acts as trunk circuit side) connects the M-lead to the signal battery (SB) lead connected to the battery of the signaling side in order to indicate the off-hook condition.

The Cisco router / gateway (signaling unit) connects the E-lead to the signal ground (SG) lead connected to the ground of the trunk circuit side in order to indicate the off-hook condition.

E&M Type III —This is not commonly used in modern systems.

Type III uses four leads for supervision signaling: E, M, SB, and SG.

During inactivity, the E-lead is open and the M-lead is set to the ground connected to the SG lead of the signaling side.

The PBX (that acts as trunk circuit side) disconnects the M-lead from the SG lead and connects it to the SB lead of the signaling side in order to indicate the off-hook condition.

The Cisco router / gateway (signaling unit) connects the E-lead to the ground in order to indicate the off-hook condition.

E&M Type IV —This is not supported by Cisco routers / gateways.

E&M Type V —Type V is symmetrical and allows two signaling nodes to be connected back-to-back. This is the most common interface type used outside of North America.

Type V uses two leads for supervisor signaling: E, and M.

During inactivity the E-lead and M-lead are open.

The PBX ( that acts as trunk circuit side) connects the M-lead to the ground in order to indicate the off-hook condition.

The Cisco router / gateway (signaling unit) connects the E-lead to the ground in order to indicate off-hook condition.

### Audio Implementation (two-wire / four-wire)

There are two distinct types of audio interface (two-wire or four-wire). These implementations describe the number of wires used in order to transmit audio signals.

With the two-wire implementation, full-duplex audio signals are transmitted over a single pair which consists of tip (T) and ring (R) leads.

The four-wire implementation provides separate paths to receive and send audio signals which consists of T, R and T1, R1 leads.

Note: Even though an E&M circuit can be called a four-wire E&M circuit, it is likely to have six to eight physical wires, based on the signaling type and audio implementation used.

### Start Dial Supervision Signaling

Start dial supervision is the line protocol that defines how the equipment seizes the E&M trunk and passes the address signaling information such as dual tone multifrequency (DTMF) digits. There are three main techniques used for E&M start dial signaling:

Immediate Start —This is the most basic protocol. In this technique, the originating switch goes off-hook, waits for a finite period of time (for example, 200 ms), then sends the dial digits to the far end.

Wink Start —Wink is the most commonly used protocol. In this technique, the originating switch goes off-hook, waits for a temporary off-hook pulse from the other end (which is interpreted as an indication to proceed), then sends the dial digits.

Delay Dial —In this technique, the originating side goes off-hook and waits for about 200 ms, then checks to see if the far end is on-hook. If the far end is on-hook, it then outputs dial digits. If the far end is off-hook, it waits until it goes on-hook, then outputs dial digits.

### Address Signaling

Address signaling typically represents the digits dialed (called number of the party). There are two options used in order to pass address information. Either Pulse dial (rotary dialing) or Tone dial (DTMF) can be used. The default for Cisco routers and gateways is DTMF.

## Related Information