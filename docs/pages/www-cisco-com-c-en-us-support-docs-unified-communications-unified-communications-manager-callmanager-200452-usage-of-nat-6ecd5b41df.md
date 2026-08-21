---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200452-usage-of-nat-6ecd5b41df
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200452-Usage-of-Native-Emergency-Call-Routing-F.html
retrieved_at: 2026-08-21T13:55:30.285323+00:00
---

Usage of Native Emergency Call Routing Feature in CUCM

# Usage of Native Emergency Call Routing Feature in CUCM

### Download Options

Updated: July 15, 2021

Document ID: 200452

Contents

## Contents

## Introduction

This document describes the Native Emergency Call Routing feature in Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM 11.X and higher.

- Requirement of pool of Direct Inward Dial ( DID) numbers that have been registered in the Public Safety Answering Point (PSAP).

Phones that support Emergency Location Identification Numbers ( ELINs):

SIP and SCCP IP Phones

- CTI Ports

- MGCP and SCCP Analog Phones

- H323 Phones

### Components Used

The information in this document is based on CUCM 11.X and higher versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

Caution : We should not enable this feature if we are already using an external emergency calling solution such as Cisco Emergency Responder. If we decide to enable this feature, we need to ensure we disable the external one. We would also require a pool of DID numbers that should be registered in the PSAP.

## Background Information

Customers that require accurate location identification but have a single site or small number of locations that need to be identified can use the CUCM Native Emergency Call Routing feature. The Native Emergency Call Routing feature allows an administrator to define ELINs at the device pool level or device level so that a device's location can be determined and identified at the PSAP.

When an emergency call is made, this is required:

- The call must be routed to the local PSAP based on the location of the caller.

- The caller's location information must be displayed at the emergency operator terminal, which can be obtained from an Automatic Location Information (ALI) database.

The caller's location is determined by the ELIN. An ELIN is a DID number that the PSAP can dial to reconnect to the emergency caller if the emergency call is cut off or if the PSAP needs to talk to the caller again. The emergency call is routed to the PSAP based on the location information associated with this number.

## Configure

Step 1.

On Cisco Unified CM Administration, choose Call Routing > Emergency Call Handler > Emergency Location Configuration .

To enable the Emergency Call Handler feature, on the Emergency Location Configuration window, check the ELIN Support check box, as shown in this image. The setting default is set to disabled.

Step 2.

Configure an ELIN group along with ELIN number as shown in the image. You can have multiple groups that signify different locations. The number should be one of them from the pool of DID numbers registered to the PSAP. An ELIN group in Emergency Call Handler identifies a location. The ELINs under this ELIN group must be mapped to the location in the Automatic Location Information (ALI) database.

Each location should have ELINs created as needed to support simultaneous emergency calls. For example, to support five simultaneous calls, five ELINs will be needed in an ELIN group.

Note : Emergency Call Handler supports maximum of 100 ELINs per cluster.

Step 3.

Configure the Route Pattern (RP) to route the call during an emergency. Check the box Is an Emergency Services Number (used by Emergency Call Handler) as shown in this image.

If the requirement arises for a Translation Pattern configuration, check the above parameter for the TP configuration.

Step 4.

Assign the ELIN group on the Device Configuration/Device Pool Configuration as shown in the image:

For a Device:

For a Device Pool:

## Verify

Use this section to confirm that your configuration works properly.

### Preliminary Test

You configured a Route Pattern 911 in CUCM and that routed the call to the correct PSAP/service provider, Within this Route Pattern, you can set the Called Party Transformations > Called Party Transformation Mask to another number you want the call to forwarded. This will prevent from the call to connect to PSAP a lot of times. On the completion of the test, be sure to remove the Called Party Transform Mask number.

### Final Test

When your CUCM configuration is complete, you must test all sites to ensure that each site receives the correct PSAP, and the PSAP sees the correct information. The test is simple; dial 911 and say something like:

I am testing a new emergency responding solution. Could you please let me know what call back number and address you see and for what area or town your response unit is listed?

The PSAP answers your questions, and you can adjust your configuration as needed. Ensure that the PSAP knows if you plan to call back more than once, and/or whether the test is complete. This keeps the PSAP informed and allows them to decide if they should dispatch any emergency responses for other 911 calls.

Ensure you do this when you are confident that your CUCM configuration is complete. PSAPs are extremely busy, and though they are agreeable to assist, their first priority is to respond to actual emergency calls.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

27-Apr-2016

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-Apr-2016 | Initial Release |