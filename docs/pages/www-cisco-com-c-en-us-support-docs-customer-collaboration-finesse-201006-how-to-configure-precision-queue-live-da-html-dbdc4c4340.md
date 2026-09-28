---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-finesse-201006-how-to-configure-precision-queue-live-da-html-dbdc4c4340
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/finesse/201006-How-To-Configure-Precision-Queue-Live-Da.html
retrieved_at: 2026-08-16T19:24:48.026900+00:00
---

How To Configure Precision Queue Live Data Gadget in PCCE 10.5

# How To Configure Precision Queue Live Data Gadget in PCCE 10.5

Updated: March 2, 2017

Document ID: 201006

Contents

## Contents

## Introduction

This document describes the steps to configure Precision Queue Live Data Gadget in Finesse for Packaged Contact Center Enterprise (PCCE) 10.5. In PCCE 10.5, Finesse default Layout lists specific gadgets for Cisco Unified Intelligence Center (CUIC) reports. However, Finesse does not include the configuration for Live data precision queue report which exists on CUIC.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Finesse gadgets

- PCCE

### Components Required

The information in this document is based on these software and hardware versions:

- PCCE Version 10.5

- Finesse version 10.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem: CUIC is not Included in the Live Data Precision Queue Report

These four gadgets for two CUIC reports,  Agent and Agent SkillGroup exist on Finesse, but the Live data precision queue report of CUIC is not included.

## Solution

These steps show how to identify view ID and configure Precision Queue Live Data report:

Step 1. Identify the ViewID for Precision Queue report.

There are a couple of ways to identify the ViewID. The most common way to find ViewID is as follow:

- Download the PCCE 10.5 Live Data template from CCO. CUIC_10_5_1_Templates_PCCE_10.5_LD_10.5.2.zip https://software.cisco.com/download/release.html?mdfid=282163829&flowid=73207&softwareid=284697222&release=10.5%281%29&relind=AVAILABLE&rellifecycle=&reltype=latest

- Extract the zip file and open Precision Queue.xml .

- Search for viewes id. Once you are at Viewes id, you can see this as an id :

<id>B71A630C10000144000002480A0007C5</id> Step 2. Log in to Finesse CFAdmin and click on Desktop Layout , as shown in the second image:

Step 3. Add the Precision Queue gadget under Live Data Gadget section, as shown in the image:

- Ensure that the view id is exactly the same as the one found in Step 1.

- Usually default view id for Live Data Precision Queue report is B71A630C10000144000002480A0007C5

https Gadget: <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?gadgetHeight=310&viewId=B71A630C10000144000002480A0007C5&filterId=precisionQueue.id=CL%20</gadget>

http Gadget:

<gadget>https://my-cuic-server:8081/cuic/gadget/LiveData/LiveDataGadget.jsp?gadgetHeight=310&viewId=B71A630C10000144000002480A0007C5&filterId=precisionQueue.id=CL%20</gadget>

Step 4. Click Save , to save the configuration, as shown in the image.

This is also being tracked via Cisco BugID CSCur70829 PCCE Live Data Queue and SkillGroup Gadgets, not in a desktop template.

### Revision History

1.0

02-Mar-2017

Initial Release

### Contributed by Cisco Engineers

Mayur Vyas

Cisco

### This Document Applies to These Products

- Finesse

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 02-Mar-2017 | Initial Release |