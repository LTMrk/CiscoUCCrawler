---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-212334-how-to-deploy-and-configu-83f288d912
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal/212334-how-to-deploy-and-configure-with-the-tru.html
retrieved_at: 2026-08-16T19:23:20.914637+00:00
---

How to Deploy and Configure with the Trunk Utilization Feature with Customer Voice Portal (CVP)

# How to Deploy and Configure with the Trunk Utilization Feature with Customer Voice Portal (CVP)

Updated: October 19, 2017

Document ID: 212334

Contents

## Contents

## Introduction

This document describes how to deploy and configure the trunk utilization feature with CVP.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CVP

- Voice gateway

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

Trunk Utilization Feature Overview

Through the Trunk Utilization feature, a gateway is used for real-time Unified CVP routing and Unified Intelligent Contact Management (ICM) reporting and scripting. A gateway pushes the status of memory, Digital Signal 0 (DS0), Digital Signal Processor (DSP), and Central Processing Unit (CPU) to Unified CVP. Because this feature uses a push method to send resource data to Unified CVP, resources are monitored more closely and failover can occur faster when a device goes down or is out of resources.

This feature has the following characteristics:

• Each gateway can publish an Session Initiation Protocol (SIP) OPTIONS message with CPU, Memory, DS0, and DSP information to Unified CVP every three minutes when operation conditions are normal on the gateway

• The push interval is configurable through the Cisco IOS Command Line Interface (CLI) on the gateway

• If a high watermark level is reached, the gateway sends the SIP OPTIONS message immediately with an Out-Of-Service = true indication, and does not send another OPTIONS message until the low watermark level is reached with an Out-Of-Service = false indication

• You can set up to five Resource Availability Indication (RAI) targets on the gateway. You can also use Trunk Utilization Routing to update trunk group status in the Unified Contact Center Enterprise (CCE) router. A Public Switched Telephone Network (PSTN) call (through the ICM script) can query the router with a preroute from a Network Interface Controller (NIC) to use the available ingress gateway for the post route to Unified CVP

## DS0 Trunk Information

Through Unified CVP, Unified ICM passes the gateway trunk and DS0 information from the arriving SIP call. PSTN gateway trunk and DS0 information received at ICM has the following purposes:

• Reporting • Routing in the Unified CCE Script Editor where TrunkGroupID and TrunkGroupChannelNum information is available for routing decisions

This message is used in the examples: The PSTN trunk group data comes from the PSTN Gateway in the SIP INVITE:

```
Via: SIP/2.0/UDP 192.168.1.79:5060;x-route-tag="tgrp:2811-b-000";x-ds0num="ISDN 0/0/0:15 0/0/0:DS1 1:DS0";branch
```

This logic is used in Unified CVP to parse and pass the PSTN trunk group information to Unified ICM:

• For TrunkGroupID, look for tgrp: in the x-route-tag field

# If tgrp: found TrunkGroupID=value after tgrp:> + <data between ISDN and :DS1 tags>· Using the above example: TrunkGroupID = 2811-b-000<space>0/0/0:15 0/0/0.

# TrunkGroupID = <IP addr of originating device in Via header> + <data between ISDN and:DS1tags> Using the above example: TrunkGroupID=192.168.1.79<space>0/0/0:15 0/0/0.

• For TrunkGroupChannelNum, look for DS0 in x-ds0nun field # If found, TrunkGroupChannelNum = <value before the :DS0>· Using the above example: TrunkGroupChannelNum = 1

# TrunkGroupChannelNum = <max int value> to indicate we did not find the DS0 value.

# Using the above example: TrunkGroupChannelNum = Integer.MAX_VALUE (2^31 - 1)

## Use of Trunk Utilization

IOS 15.1(2) and later introduces toll fraud prevention. This feature is recommended that for the RAI resource settings on the gateway, use the 60% low watermark and the 80% high watermark.

IOS Gateway configuration example:

```
voice class resource-group 1 resource cpu 1-min-avg threshold high 80 low 60 resource ds0 resource dsp resource mem total-mem periodic-report interval 30 sip-ua rai target ipv4:< ip address of CVP server > resource-group 1 #configure this for each CVP server.
```

Ensure that the pots dial peers have the trunk serial interface configured or else DS0 information is not be sent.

```
dial-peer voice 10 pots destination-pattern 10T port 1/0:23 ! dial-peer voice 11 pots destination-pattern 11T port 1/1:23 ! dial-peer voice 20 pots destination-pattern 20T port 2/0:23 ! dial-peer voice 21 pots destination-pattern 21T port 2/1:23 ! dial-peer voice 30 pots destination-pattern 30T port 3/0:23 ! dial-peer voice 31 pots destination-pattern 31T port 3/1:23 ! dial-peer voice 40 pots destination-pattern 40T port 4/0:23 ! dial-peer voice 41 pots destination-pattern 41T port 4/1:23
```

Example of OPTIONS message with RAI headers:

```
OPTIONS sip:20.20.205.223:5060 SIP/2.0 Date: Fri, 01 Jun 2016 02:11:04 GMT From: <sip:20.20.205.1>;tag=1AF2C70-792 X-cisco-rai: SYSTEM ; almost-out-of-resource=false;identity=20.20.205.1 X-cisco-rai: CPU ; almost-out-of-resource=false;available=99%;total=100%;used=1% X-cisco-rai: DS0 ; almost-out-of-resource=false;available=23;total=23;used=0% X-cisco-rai: DSP ; almost-out-of-resource=false;available=384;total=384;used=0% X-cisco-rai: MEM ; almost-out-of-resource=false;available=86%;total=100%;used=14% Supported: x-cisco-rai Content-Length: 0 User-Agent: Cisco-SIPGateway/IOS-12.x To: <sip:20.20.205.223> Contact: <sip:20.20.205.1:5060> Call-ID: DD292D1E-839A98AF-9DD011DE-29B4F520@10.86.129.44 Via: SIP/2.0/UDP 20.20.205.1:5060;branch=z9hG4bK3931109 CSeq: 101 OPTIONS Max-Forwards: 70
```

## CVP & ICM Setup

Step 1. Create the Gateways for reporting in the  Operate Administer Maintain Provision (OAMP) console.

Step 2. On the ICM Subsystem tab for the Call Server, select all the gateways for reporting trunk data.

Step 3. The SIP subsystem tab has 2 checkboxes, leave the defaults for both of them checked off.

Step 4. Create the Network Trunk Groups on the ICM Configuration Manager.

Note : Use the same Peripheral Number as the Trunk Group ID on the CVP OAMP side.

### Revision History

1.0

19-Oct-2017

Initial Release

### Contributed by Cisco Engineers

Mayur Vyas

Cisco TAC Engineer

Edited by Maria Jose Mendez Vazquez

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Customer Voice Portal

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Oct-2017 | Initial Release |