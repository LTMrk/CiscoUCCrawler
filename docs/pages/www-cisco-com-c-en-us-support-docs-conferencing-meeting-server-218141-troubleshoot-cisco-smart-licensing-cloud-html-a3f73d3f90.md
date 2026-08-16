---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-218141-troubleshoot-cisco-smart-licensing-cloud-html-a3f73d3f90
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/218141-troubleshoot-cisco-smart-licensing-cloud.html
retrieved_at: 2026-08-16T14:21:57.953557+00:00
---

Troubleshoot Smart License Cloud Certificate Changes on CMS and CMM on Jan 15Th 2023

# Troubleshoot Smart License Cloud Certificate Changes on CMS and CMM on Jan 15Th 2023

Log in to Save Content

### Download Options

Updated: January 13, 2023

Document ID: 218141

Contents

## Contents

## Introduction

This document describes how the change of certificates on Cisco Smart Licensing Cloud Certificates affected your Cisco Meeting Server (CMS) and Cisco Meeting Management (CMM) deployment.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Meeting Server (CMS) and Cisco Meeting Management (CMM).

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

This article focusses on the note as written on the Smart Licensing section (section 1.5) on the CMM release notes and to which the FN72534 refers at:

"Cisco Smart Licensing Cloud Certificates will be updated on January 15, 2023.  Customers using Direct Mode for licensing between Meeting Management and Smart Licensing Portal should upgrade to version 3.6 to continue to use direct mode. If upgrade to version 3.6 is not possible, customers can opt for SLR/PLR mode or on-premise satellite mode. The certificate update will not impact deployments that are using SLR/PLR or on-premise satellite with Meeting Management (3.5 or below). If Meeting Management is not upgraded in time, Meeting Server will continue to work, but the license enforcement will be initiated. Meeting Management will be on a 90 day grace period, after which non-compliance notifications will be flashed on the participant's screen and audio prompts."

There are different deployment options for the CMM Smart Licensing as shown in the next section which each have their own characteristics. Your deployment option as set up on the Transport settings on Cisco Meeting Management Settings > Licensing , decides whether it is impacted or not. Some setups are not impacted because they do not have a direct connection to the Smart Licensing cloud, where the certificate change will take place.

## Available Options for CMM Smart Licensing

### Direct without proxy

To make sure CMM continues to function, you must upgrade CMM and CMS to version 3.6 or higher or move to Specific License Reservation type or use the Transport Gateway.

### Direct with Proxy

If the proxy terminates and re-establishes the TLS connection between CMM and Cisco cloud, then make sure that the proxy trusts the new certificate presented by the Cisco cloud.

Otherwise, if the proxy does not establish a new TLS connection to the Cisco cloud, then to make sure CMM continues to function, you must upgrade CMM and CMS to version 3.6.

### Transport Gateway

No impact, no action required.

### Specific License Reservation (SLR) / Permanent License Reservation (PLR)

No impact, no action required.

The URL that’s impacted is https://smartreceiver.cisco.com/licservice/license

## Solution

- Upgrade CMM to 3.6 or later ideally before January 15, 2023. Later works as well within the 90-day grace period.

- Use Specific License Reservation (SLR) mode on CMM OR

- Connect CMM to an on-premises Satellite server CSSM

Download Link for Cisco Meeting Server 3.6 release: https://software.cisco.com/download/home/286309725/type/280886992/release/CMS3.6

Download Link for Cisco Meeting Management 3.6 release: https://software.cisco.com/download/home/286318491/type/280886992/release/CMM3.6.0?i=!pp

Link to external Field Notice: https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72543.html

How to Upgrade Cisco Meeting Server: https://www.youtube.com/watch?v=t2qqdydN01c

## FAQ

### What happens if you do not upgrade before Jan 15th?

Unless you use Direct mode, your deployment will not be impacted. If you use Direct Mode via Proxy where the proxy terminates and re-establishes the TLS connection between CMM and Cisco cloud, then make sure that the proxy trusts the new certificate presented by the Cisco cloud.

In case of Direct mode, the system enters a 90-day grace period from Jan 15th and needs to be upgraded as soon as possible to CMM 3.6 or newer.

### Can you upgrade after Jan 15th?

Yes.

### If you are on CMM 3.5 or older after Jan 15th and you use SLR, can you still update the SLR allocations?

Yes, we expect there to be no issue with an update on your SLR license allocations since CMM does not need to make a secure connection to CSSM for this to be possible.

### Revision History

3.0

13-Jan-2023

FAQ added and different types

2.0

07-Dec-2022

A note about upgrading to CMS 3.6 prior to the Smart Licensing Cloud certificate update in February 2023 has been added.

1.0

05-Sep-2022

Initial Release

### Contributed by Cisco Engineers

Vikram Dutta

Cisco TAC Engineer

Dipin Divakaran

Cisco TAC Engineer

Darren McKinnon

Cisco TAC Engineer

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

### This Document Applies to These Products

- Meeting Management

- Meeting Server

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 13-Jan-2023 | FAQ added and different types |
| 2.0 | 07-Dec-2022 | A note about upgrading to CMS 3.6 prior to the Smart Licensing Cloud certificate update in February 2023 has been added. |
| 1.0 | 05-Sep-2022 | Initial Release |