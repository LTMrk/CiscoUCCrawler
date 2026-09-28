---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-213398-configure-cvp-and-ipivr-i-829f06b68f
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal/213398-configure-cvp-and-ipivr-in-a-dual-indepe.html
retrieved_at: 2026-08-16T19:23:03.743587+00:00
---

Configure CVP and IPIVR in a Dual Independant VRU Setup

# Configure CVP and IPIVR in a Dual Independant VRU Setup

Updated: May 29, 2018

Document ID: 213398

Contents

## Contents

## Introduction

This document describes how to address the problem of Customer Voice Portal (CVP) and IP Interactive Voice Response (IPIVR) co-existing with each other on Intelligent Contact Management (ICM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CVP

- IPIVR

- ICM

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Due to migration or testing co-existence of IPIVR and CVP as a Voice Response Unit (VRU) in ICM, there can be a need for them to work side by side. The rules for VRU selection are the following:

Step 1.  The Router first checks to see which customer instance is configured for the dialed number that executed the script.

Step 2.  If a customer instance is configured, it checks to see which VRU is associated with that customer instance.

In order to see which VRU is associated with a customer instance, navigate to Configuration Manager and browse to Configure ICM > Enterprise > ICM Node > ICM Instance Explorer . Select the customer definition and on the right you can see the Network VRU associated with the customer instance.

Step 3.  If there is no Network VRU associated with the customer instance, or the dialed number has the customer instance set to None, the Router chooses the default Network VRU.

In order to see the Default Network VRU, navigate to Configuration Manager and browse to Configure ICM > Enterprise > System Information > System Information .

Step 4.  Once the Router determines what the Network VRU is, it then checks to see what label is configured for the routing client that sent in the initial route request.

In order to see what labels are configured for the Network VRU, navigate to Configuration Manager and browse to Tools > Explorer Tools > Network VRU Explorer and locate the appropriate Network VRU . Look for the label configured for the routing client that sent in the initial route request.

## Configure

Once you understand how this works, you can easily configure this co-existence.

Step 1. Create your CVP and IPIVR VRU in VRU Explorer.

Step 2. Create two Customer Definitions under ICM Instance .

- One for IPIVR with IPIVR VRU

- One for CVP with CVP VRU

Step 3. Associate the Customer Definitions on Dialed numbers .

- For IPIVR based trans-routing

- For CVP based post routing or pre-routing

## Verify

- Make a call to the CVP Routing client dialed number in CVP comprehensive call flow and call must work with CVP as IVR.

- Make a call to the CUCM Routing client dialed number from CUCM and call should work towards IPIVR script.

## Troubleshoot

For some reason, if correct VRU is not selected, you can check ICM Router logs:

16:01:37:990 ra-rtr Trace: (65536 x 0 : 0 0) NewCall: CID=(152454,501), DN=4150, ANI=3003, CED=, RCID=5000 , MRDID=1, CallAtVRU=0, OpCode=0. 16:01:38:054 ra-rtr Trace: (65536 x 0 : 0 0) TranRouteToVRU: Label=4100, CorID=1, VRUID=5001 .

RCID is CUCM since call is routing from CUCM and VRUID is IPIVR.

If VRU ID is incorrect, then configuration should be corrected.

### Revision History

1.0

10-Jun-2018

Initial Release

### Contributed by Cisco Engineers

Shikhar Choudhary

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Customer Voice Portal

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Jun-2018 | Initial Release |