---
doc_id: www-cisco-com-c-en-us-support-docs-voice-h323-5244-understand-gatekeepers-html-db83277e21
source_url: https://www.cisco.com/c/en/us/support/docs/voice/h323/5244-understand-gatekeepers.html
retrieved_at: 2026-08-21T07:17:39.720681+00:00
---

Understanding H.323 Gatekeepers

# Understanding H.323 Gatekeepers

### Download Options

Updated: September 25, 2014

Document ID: 5244

Contents

## Contents

## Introduction

The ITU-T H.323 standard specifies four components:

gateway

gatekeeper

terminal

multipoint control unit (MCU)

This document provides a comprehensive introduction to the functionality and operation of the gatekeeper in H.323 Voice over IP (VoIP) networks.

Refer to the H.323 Tutorial for more information on H.323.

## Prerequisites

### Requirements

Ensure that you use the H.323 Gatekeeper functionality feature, which is denoted as x- on the Downloads ( registered customers only) . For example, a valid Cisco IOS® for the Cisco 2600 to act as a gatekeeper is c2600-ix-mz.122-11.

### Components Used

This document is not restricted to specific software and hardware versions.

### Conventions

Refer to the Cisco Technical Tips Conventions for more information on document conventions.

## Gatekeeper Definition

A gatekeeper is an H.323 entity on the network that provides services such as address translation and network access control for H.323 terminals, gateways, and MCUs. Also, they can provide other services such as bandwidth management, accounting, and dial plans that you can centralize in order to provide salability.

Gatekeepers are logically separated from H.323 endpoints such as terminals and gateways. They are optional in an H.323 network. But if a gatekeeper is present, endpoints must use the services provided.

## Gatekeeper Zones and Subnets

A zone is the collection of H.323 nodes such as gateways, terminals, and MCUs registered with the gatekeeper. There can only be one active gatekeeper per zone. These zones can overlay subnets and one gatekeeper can manage gateways in one or more of these subnets.

## Gatekeeper Functionality

The H.323 standard defines mandatory and optional gatekeeper functions:

### Mandatory Gatekeeper Functions

Address Translation —Translates H.323 IDs (such as gwy1@domain.com) and E.164 numbers (standard telephone numbers) to endpoint IP addresses.

Admission Control —Controls endpoint admission into the H.323 network. In order to achieve this, the gatekeeper uses these:

H.225 Registration, Admission, and Status (RAS) messages

See the H.225 RAS Signaling: Gatekeepers and Gateways section for more information about RAS Signaling.

Admission Request (ARQ)

Admission Confirm (ACF)

Admission Reject (ARJ)

Bandwidth Control —Consists of the management of endpoint bandwidth requirements. In order to achieve this, the gatekeeper uses these H.225 RAS messages:

Bandwidth Request (BRQ)

Bandwidth Confirm (BCF)

Bandwidth Reject (BRJ)

Zone Management —The gatekeeper provides zone management for all registered endpoints in the zone, for example, the control of the endpoint registration process.

### Optional Gatekeeper Functions

Call Authorization —With this option, the gatekeeper can restrict access to certain terminals or gateways and/or have time-of-day policies restrict access.

Call Management —With this option, the gatekeeper maintains active call information and uses it to indicate busy endpoints or redirect calls.

Bandwidth Management —With this option, the gatekeeper can reject admission when the required bandwidth is not available.

Call Control Signaling —With this option, the gatekeeper can route call-signaling messages between H.323 endpoints with the use of the Gatekeeper-Routed Call Signaling (GKRCS) model. Alternatively, it allows endpoints to send H.225 call-signaling messages directly to each other.

Note: Cisco IOS gatekeepers are Direct Endpoint Signaling based. They do not support GKRCS. See the Gatekeeper-Routed Call Signaling vs Direct Endpoint Signaling section of this document.

## H.323 Protocol Suite

The H.323 protocol suite is split into three main areas of control:

RAS (H.225) signaling

Call Control/Call Setup (H.225)

Media Control and Transport (H.245) signaling

### H.225 RAS Signaling

RAS is the signaling protocol used between gateways and gatekeepers. The RAS channel is opened before any other channel and is independent of the call setup and media transport channels.

RAS uses User Datagram Protocol (UDP) ports 1719 (H.225 RAS messages) and 1718 (multicast gatekeeper discovery).

See the H.225 RAS Signaling: Gatekeepers and Gateways section of this document for more detailed information.

### H.225 Call Control (Setup) Signaling

H.225 call control signaling is used to setup connections between H.323 endpoints. The ITU H.225 recommendation specifies the use and support of Q.931 signaling messages.

A reliable (TCP) call control channel is created across an IP network on TCP port 1720. This port initiates the Q.931 call control messages for the purpose of the connection, maintenance, and disconnection of calls.

When a gatekeeper is present in the network zone, H.225 call setup messages are exchanged either via Direct Call Signaling or GKRCS. See the Gatekeeper-Routed Call Signaling vs Direct Endpoint Signaling section of this document for more information. The method chosen is decided by the gatekeeper during the RAS admission message exchange.

If no gatekeeper is present, H.225 messages are exchanged directly between the endpoints.

### H.245 Media Control and Transport

H.245 handles end-to-end control messages between H.323 entities. H.245 procedures establish logical channels for transmission of audio, video, data, and control channel information. It is used to negotiate channel usage and capabilities such as:

flow control

capabilities exchange messages

A detailed explanation of H.245 is beyond the scope of this document.

### H.323 Protocol Suite Overview

## H.225 RAS Signaling: Gatekeepers and Gateways

### RAS Gatekeeper Discovery

Thisis the processes by which H.323 terminals/gateways discover their zone gatekeepers Automatic Gatekeeper Discovery :

If an H.323 endpoint does not know its gatekeeper, then it can send a Gatekeeper Request (GRQ). This is a UDP datagram addressed to the well-known destination port 1718 and transmitted in the form of an IP multicast with the multicast group address 224.0.1.41.

One or several gatekeepers can answer the request with either a positive Gatekeeper Confirmation (GCF) message or a negative Gatekeeper Reject (GRJ) message. A reject message contains the reason for the rejection and can optionally return information about alternative gatekeepers. Auto discovery enables an endpoint to discover its gatekeeper through a multicast Gatekeeper Request (GRQ) message. Because endpoints do not have to be statically configured for gatekeepers, this method has less administrative overhead. A gatekeeper replies with a GCF or GRJ message. A gatekeeper can be configured to respond only to certain subnets.

Note: A Cisco IOS gatekeeper always replies to a GRQ with a GCF/GRJ message. It never remains silent.

If a gatekeeper is not available, the gateway periodically attempts to rediscover a gatekeeper. If a gateway discovers the gatekeeper has gone off-line, it ceases to accept new calls and attempts to rediscover a gatekeeper. Active calls are not affected.

This table defines the RAS gatekeeper discovery messages:

### RAS Registration and Unregistration

Registration is the process by which gateways, terminals, and/or MCUs join a zone and inform the gatekeeper of their IP and alias addresses. Registration occurs after the discovery process. Every gateway can register with only one active gatekeeper. There is only one active gatekeeper per zone.

The H.323 gateway registers with an H.323 ID (email ID) or an E.164 address. For example:

EmailID (H.323 ID): gwy-01@domain.com

E.164 Address: 5125551212

This table defines the RAS gatekeeper registration and unregistration messages:

### RAS Admissions

Admission messages between endpoints and gatekeepers provide the basis for call admissions and bandwidth control. Gatekeepers authorize access to H.323 networks with the confirmation of or rejection of an admission request.

This table defines the RAS admission messages:

See the Gatekeeper to Gateways Call Flow section of this document for more information.

### RAS Endpoint Location

Location Request messages are commonly used between inter-zone gatekeepers in order to get the IP addresses of different zone endpoints. This table defines the RAS location request messages:

See the Gatekeeper to Gateways Call Flow section for more information.

### RAS Status Information

The gatekeeper can use the RAS channel in order to obtain status information from endpoints. You can use the RAS in order to monitor whether the endpoint is online or off-line. This table defines the RAS status information messages:

### RAS Bandwidth Control

Bandwidth control is initially managed through the Admission Messages (ARQ/ACF/ARJ) sequence. However, bandwidth can change during the call. This table defines the RAS bandwidth control messages:

Refer to Understanding, Configuring, and Troubleshooting Resource Allocation Indication for more information about RAI.

## Gatekeeper-Routed Call Signaling vs Direct Endpoint Signaling

There are two types of gatekeeper call signaling methods:

Direct Endpoint Signaling —This method directs call setup messages to the terminating gateway or endpoint.

Gatekeeper-Routed Call Signaling (GKRCS) —This method directs the call setup messages through the gatekeeper.

Note: Cisco IOS gatekeepers are Direct Endpoint signaling based and do not support GKRCS.

These diagrams illustrate the differences between these two methods:

## Gatekeeper to Gateways Call Flow

These sections only present Directed Call Signaling call flow scenarios. Also, assume the gateways have already completed discovery and registration with their gatekeepers.

### Intra-Zone Call Setup

### Inter-Zone Call Setup

### Inter-Zone Call Setup with a Directory Gatekeeper

A major functionality of gatekeepers is to keep track of other H.323 zones and forward calls appropriately. When many H.323 zones are present, gatekeeper configurations can become administratively intensive. In such large VoIP installations it is possible to configure a centralized directory gatekeeper that contains a registry of all the different zones and coordinates LRQ-forwarding processes. No full mesh is needed between inter-zone gatekeepers with directory gatekeepers.

Note: A directory gatekeeper is not an industry standard, but is a Cisco implementation.

See the H.323 Network Scaling with Gatekeepers section for more information .

### Proxy-Assisted Call Setup

### Call Disconnect

## H.323 Network Scaling with Gatekeepers

This diagram illustrates the concept of VoIP Network scaling with gatekeepers and directory gatekeepers:

## H.225 RAS Protocol Elements Table

Note: Refer to Understanding Cisco IOS Gatekeeper Call Routing for more information on gatekeeper sample configurations.

## Related Information

| Gatekeeper Discovery |
|---|
| GRQ (Gatekeeper_Request) | A message sent by endpoint to gatekeeper. |
| GCF (Gatekeeper_Confirm) | A reply from gatekeeper to endpoint which indicates the transport address of the gatekeeper RAS channel. |
| GRJ (Gatekeeper_Reject) | A reply from gatekeeper to endpoint that rejects the endpoint's request for registration. Usually due to gateway or gatekeeper configuration error. |

| Gatekeeper Discovery |
|---|
| RRQ (Registration_Request) | Sent from an endpoint to a gatekeeper RAS channel address. |
| RCF (Registration_Confirm) | A reply from the gatekeeper that confirms endpoint registration. |
| RRJ (Registration_Reject) | A reply from the gatekeeper that rejects endpoint registration. |
| URQ (Unregister_Request) | Sent from endpoint or gatekeeper to cancel registration. |
| UCF (Unregister_Confirm) | Sent from endpoint or gatekeeper to confirm an unregistration. |
| URJ (Unregister_Reject) | Indicates that the endpoint was not preregistered with the gatekeeper. |

| Admission Messages |
|---|
| ARQ (Admission_Request) | An attempt by an endpoint to initiate a call. |
| ACF (Admission_Confirm) | An authorization by the gatekeeper to admit the call. This message contains the IP address of the terminating gateway or gatekeeper and enables the original gateway to initiate call control signaling procedures. |
| ARJ (Admission_Reject) | Denies the request of the endpoint to gain access to the network for this particular call. |

| Location Request |
|---|
| LRQ (Location_Request) | Sent to request the gatekeeper contact information for one or more E.164 addresses. |
| LCF (Location_Confirm) | Sent by the gatekeeper and contains the call signaling channel or RAS channel address of itself or the requested endpoint. LCF uses its own address when GKRCS is used. LCF uses the requested endpoint address when Directed Endpoint Call Signaling is used. |
| LRJ (Location_Reject) | Sent by gatekeepers that received an LRQ for which the requested endpoint is not registered or has unavailable resources. |

| Status Information |
|---|
| IRQ (Information_Request) | A status request sent from gatekeeper to endpoint. |
| IRR (Information_Request_Response) | Sent from endpoint to gatekeeper in response to IRQ. This message is also sent from endpoint to gatekeeper if the gatekeeper requests periodic status updates. The IRR is used by gateways to inform the gatekeeper about the active calls. |
| IACK (Info_Request_Acknowledge) | Used by the gatekeeper in order to respond to IRR messages. |
| INACK (Info_Request_Neg_Acknowledge) | Used by the gatekeeper in order to respond to IRR messages. |

| Bandwidth Control |
|---|
| BRQ (Bandwidth_Request) | A request for an increase/decrease in call bandwidth sent by the endpoint to the gatekeeper. |
| BCF (Bandwidth_Confirm) | Sent by the gatekeeper and confirms the acceptance of the bandwidth change request. |
| BRJ (Bandwith_Reject) | Sent by the gatekeeper and rejects the bandwidth change request. |
| RAI (Resource Availability Indicator) | This is used by gateways to inform the gatekeeper whether resources are available in the gateway to take on additional calls. |
| RAC (Resource Availability Confirm) | Notification from the gatekeeper to the gateway that acknowledges the reception of the RAI message. |