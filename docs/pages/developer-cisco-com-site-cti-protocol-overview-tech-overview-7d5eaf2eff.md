---
doc_id: developer-cisco-com-site-cti-protocol-overview-tech-overview-7d5eaf2eff
source_url: https://developer.cisco.com/site/cti-protocol/overview/tech-overview/
retrieved_at: 2026-08-25T21:04:25.052939+00:00
---

## Introduction

The purpose of the CTI Server Protocol is to provide a message based interface to the CTI Server. The protocol provides for Session and Application Management. Once a TCP/IP Session is established, a client application can utilize any of the following services:

- Client Events. This service provides real-time call and agent state change, and status information related to a specific ACD agent position, to a CTI client..

- All Events. This service provides real-time call and agent state change, and status information for all ACD calls and agent positions, to a CTI client

- Peripheral Monitor. This service lets a CTI client dynamically change the list of calls and devices that it wishes to receive call and agent state change messages for.

- Client Monitor. This service lets a CTI client receive notifications whenever any other CTI Client session is opened or closed. This service also enables the CTI Client to monitor the activity of other CTI Client sessions.

- Supervisor. This service lets a CTI client perform agent supervisory functions. (for Cisco Unified Contact Center Eneterprise only. TDM ACDs are not supported).

- Call Data Update. This service lets a CTI client modify certain variable parts of the call state while a call is active.

- Miscellaneous. This service informs CTI clients of significant Peripheral Gateway events.

- Connection Monitor. This service monitors the CTI client connection and generates alarm events whenever the CTI client connection is established or terminated.

- Client Control. This service permits direct control of agent state (such as ACD login and logout), as well as control of inbound and outbound calls from the CTI client application.

- Server Service. This service enables the CTI Server to resigster a service that it wishes to provide.

### Benefits

The CTI Server Protocol enables you to create CTI Applications such as

- Call Recording applications

- Wall Board Applications

- WFM realtime-adherence integrations

- CTI Bridge mode integrations

Depending on your application and the environment you are supporting., you may wish to consider using the CTIOS Server and the CTIOS Toolkit for creating integrations. Also, Cisco Advanced Services provides a realtime WFM adherence application for purchase which may save you or your customer from needing to create a new CTI Server application.

## Technology/Solution Details

The CTI Server provides for integration of CTI Applications that can open a session, request a set of services, send requests and receive confirmations and asynchronous events. CTI Server is the Cisco Unified Contact Center Enterprise/Intelligent Contact Manager (ICM) component that delivers agent, call, and customer data in real time and enables third-party call control.

## CTISP Architecture

Below is a diagram that illustrates the architecture of CTI Server Protocol