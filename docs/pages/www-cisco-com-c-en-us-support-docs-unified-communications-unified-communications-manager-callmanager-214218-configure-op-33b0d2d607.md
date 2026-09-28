---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214218-configure-op-33b0d2d607
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214218-configure-options-ping-between-cucm-and.html
retrieved_at: 2026-08-16T15:56:12.123453+00:00
---

Configure Options Ping Between CUCM and CUBE

# Configure Options Ping Between CUCM and CUBE

### Download Options

Updated: February 6, 2019

Document ID: 214218

Contents

## Contents

## Introduction

This document describes how to enable feature Options Ping between Cisco Unified Communications Manager (CUCM) and Cisco Unified Border Element (CUBE).

Contributed by Luis J. Esquivel Blanco, Cisco TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Call Manager Administration

- Cisco Unified Border Element or Gateway Administration

- Session Initiation Protocol ( SIP)

### Components Used

- Cisco Integrated Services Router (ISR4351/K9)

- Cisco Unified Communications Manager 12.0

- Cisco Unified IP Phone

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

It is important to review how CUCM extends a call out of a SIP Trunk as shown below:

For CUCM to extend a call out of a SIP trunk, it proceeds to establish a Transmission Control Protocol (TCP) 3-way handshake with the IP address specified in the Trunk Configuration page as shown in the image:

TCP 3-way handshake in wireshark looks as shown in the image :

This is done on a per-call, per node basis; so CUCM is forced to wait for a timeout on the Synchronize (SYN) message or an error from the SIP service before it tries an alternate trunk or GW (Gateway).

In order to solve this issue, you enable Options Ping and proactively check the status of your SIP trunks.

When you enable Options Ping on your SIP trunk, you also add SIP Trunk Status and uptime statistics where it is possible to monitor the state of each SIP trunk and troubleshoot the moment a trunk goes down.  These statistics are seen on the SIP trunk Configuration page.

## Configure

Step 1. Enable SIP Options Ping in the SIP Profile Configuration:

- Navigate to Cisco Unified CM Administration >> Device >> Device Settings >> SIP Profile as shown in the image:

- Click find and decide if you want to create a new SIP Profile , edit a SIP Profile that already exists or make a copy of a SIP Profile. For this example, create a copy of the Standard SIP Profile as shown in the images:

- Rename the new SIP Profile and enable Options Ping as shown in the image:

Step 2. Add the SIP Profile to the SIP trunk in question and click Save :

Note : Keep in mind that this trunk must have been previously configured. If you need guidance on how to configure a SIP trunk, visit the link: System Configuration Guide

- Navigate to Device >> Trunk and choose the trunk you want to edit as shown in the image:

- Notice that the Status, Status Reason, and Duration are set to N/A.

- Choose the correct SIP Profile, and click Save

- At this point CUCM must be able to monitor the status of the SIP trunk as shown in the image:

Step 3. (Optional)  Enable SIP Options Ping on the far end of the SIP Trunk. In this case: 192.X.X.57 (ISR 4351)

- Navigate to the ISR Cisco Unified Border Element or Gateway and confirm what dial-peer you want to add the Options Ping to as shown in the image:

- Add Options Ping with the command: voice-class sip options-keepalive as shown in the image:

## Verify

Use this section in order to confirm that Options messages are exchanged correctly.

Note : If you need to understand how to run a packet capture on CUCM eth0 port, follow the instructions in this link: Packet Capture on CUCM Appliance Model

- Notice that the TCP 3-way handshake is only done once, when the trunk is restarted and afterwards we only have OPTIONS messages sent from CUCM to ISR where a 200 OK is expected as a response. These messages are exchanged every 60 seconds by default.

- Notice that Options messages are only sent from 192.X.X.26 (CUCM) to 192.X.X.57 (ISR) because only CUCM is configured to monitor the trunk status:

- Now when a call is made, CUCM already knows the trunk is in an operational status and sends an Invite right away:

- If you did step 3 (Optional configuration on CUBE) you see Options messages sent both ways:

## Troubleshoot

- In order to troubleshoot Options Ping in CUCM, you need:

- The best option to start is with a Packet Captures from CUCM Eth0 port, more details: Packet Capture on CUCM Appliance Model

Open the capture with 3party free software Wireshark, and filter with SIP

- You can also check detailed Cisco Callmanager traces, download them with RTMT, find steps here: How to Collect Traces for CUCM 9.x or Later

- Verify the SIPTrunkOOS Reason codes in this link: System Error Message

- Local=1 (request timeout)

- Local=2 (local SIP stack is not able to create a socket connection with the remote peer)

- Local=3 (DNS query failed)

- In order to troubleshoot Options Ping in ISR4351, you need:

- Debug ccsip messages

- Debug ccapi inout

- Packet Captures from interface that points towards CUCM