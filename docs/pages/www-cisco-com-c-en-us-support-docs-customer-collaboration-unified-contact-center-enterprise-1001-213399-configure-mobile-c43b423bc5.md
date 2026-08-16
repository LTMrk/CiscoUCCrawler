---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-enterprise-1001-213399-configure-mobile-c43b423bc5
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-enterprise-1001/213399-configure-mobile-agent-on-ucce.html
retrieved_at: 2026-08-16T19:21:37.571035+00:00
---

Configure Mobile Agent on UCCE

# Configure Mobile Agent on UCCE

### Download Options

Updated: June 27, 2018

Document ID: 213399

Contents

## Contents

## Introduction

This document describes how to configure and verify Mobile Agent feature on Cisco Unified Contact Center Enterprise (UCCE).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Customer Voice Portal (CVP) dial plan configuration

- Cisco Intelligent Contact Management (ICM) Configuration Manager

- Cisco Unified Communications Manager (CUCM) dial plan and Phone Configuration

- Cisco Computer Telephony Integration Object Server (CTI OS) Setup on UCCE Peripheral Gateway (PG)

### Components Used

The information in this document is based on these software versions:

- CVP 9.0

- ICM 9.0

- CUCM 9.1

- CTI OS 9.0

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any configuration change.

## Configure

### Add LCP (Local CTI Port) and RCP (Remote CTI Port) ports in CUCM

Step 1. Create LCP and RCP ports in CUCM.

Although not required, for best practices, use this naming convention: For a local CTI Port pool name, configure a name in the format LCPxxxxFyyyy, where LCP identifies a local CTI Port Pool, xxxx is the peripheral ID for the Unified CM PIM, and yyyy is the number of local CTI Port. Example: LCP5000F0000 represents CTI Port: 0 in a local CTI Port pool for the Unified CM PIM with the peripheral ID 5000.

For a network CTI Port pool name, use the same format, except substitute RCP as the first three characters.

Note : While you do not require a naming convention, the substrings identifying the Unified CM PIM peripheral ID and the CTI Port must match for each local/network pair.

Step 2. Add Directory Numbers (DN's) to LCP/RCP ports and associate them with the PGuser . Ensure Max Number of Calls and Busy Trigger are set to 2 and 1 respectively.

As shown in the image from lab:

Note : If a caller must hear music when a Mobile Agent places the caller on hold, you must assign Music on Hold (MoH) resources to the ingress voice gateway or trunk that is connected to the caller (as you do with traditional agents). In this case, the user or network audio source is specified on the local CTI port configuration. Similarly, if a Mobile Agent must hear music when the agent is put on hold, you must assign MoH resources to the ingress voice gateway or trunk that is connected to the Mobile Agent. In this case, the user or network audio source is specified on the remote CTI port configuration.

Step 3. If agents are anticipated to stay logged on for more than 12 hours in Nailed connection(default), ensure this parameter in CUCM CallManager Service Parameters is increased or disabled. Put zero in order to disable it. Click Save .

Default value as shows in the image below.

### Configure UCCE/CVP for Mobile Agent

Step 1.

Create Agent Targeting rules for the DN range of LCP/RCP ports as shows in the image.

Step 2. Create Dialed Number Patterns for LCP ports in CVP Operate, Administer, Maintain, Provision (OAMP) console as shows in the image.

Example: Routing range 32> to CUCM. You can select a SIP Server group or a static IP for call routing to specific CUCM server.

Step 3: Enable Mobile agent on Agent Desk Settings . Also select Mobile Agent Mode as shown in the image. Click Save .

Step 4. Run the CTI OS setup on PG and Enable Mobile Agent and the Mode selected as shown in the image.

Note : Call delivery mode that’s used by agent at log in must match the agent desk setting mode

Note : If you use SIP trunks, you must configure MTPs. This also applies if you use TDM trunks, in order to interact with service providers. Mobile Agent cannot use an MTP with codec pass through. When you configure the MTP, you must select No pass through. KPML is not supported with Mobile Agent.

Step 5. Enable Connect Tone (Nailed Connection only):

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\ICM\<instance name>\PG1A\PG\CurrentVersion\JGWS\jgw1\JGWData\Config\ PlayMAConnectTone

In order to enable this, set it to 1 and cycle PG

## Verify

Use this section in order to confirm that your configuration works properly

- Log in the agent via both modes one by one(Instrument is the LCP DN).

- In call by call mode, when there is a call in queue, agents receive a new call on their PSTN phone.

- In nailed connection mode, as soon as the agent logs in and goes ready, agent’s PSTN phone gets a call and agent hears MOH. As soon as there is a call in queue, agents get a tone and they receive the call.

## Troubleshoot

This section provides information you can use in order  to troubleshoot your configuration.

Issue 1. Calls do not reach Agent Mobile phone and as a result, agent log in fails.

You have to ensure that calls are succesfully routing from RCP to Egress SIP trunk for next hop.

If call does not connect successfully, agent log in fails.

Issue 2. Call drops on agent mobile phone as soon as agent picks up the call.

Ensure that Egress MTP resources are allocated accordingly. Since the RCP call has to be pinned down to an MTP while it is taken off hold, call drop behaviour might be seen.

Issue 3. No audio on Mobile agent calls

Ensure that Ingress MTP and Egress MTP, if invoked, are able to allocate resources and negociate media.

### Revision History

1.0

27-Jun-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-Jun-2018 | Initial Release |