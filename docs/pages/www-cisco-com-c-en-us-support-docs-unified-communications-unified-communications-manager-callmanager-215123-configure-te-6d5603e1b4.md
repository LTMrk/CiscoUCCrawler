---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-215123-configure-te-6d5603e1b4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/215123-configure-tertiary-redundancy-for-cisco.html
retrieved_at: 2026-08-21T06:40:22.917416+00:00
---

Configure Tertiary Redundancy for Cisco Emergency Responder with Different Calling Numbers for Each Site

# Configure Tertiary Redundancy for Cisco Emergency Responder with Different Calling Numbers for Each Site

### Download Options

Updated: December 19, 2019

Document ID: 215123

Contents

## Contents

## Introduction

This document describes how to configure tertiary redundancy for Cisco Emergency Responder (CER) where both the Primary CER server and also the Secondary CER server are no longer available.  It allows for each site within an organisation that uses Cisco Unified Communications Manager (CUCM) to continue to use a different Calling Number—also known as an Emergency Location Identification Number (ELIN)—rather than all calls to the Public Safety Access Point (PSAP) routed with the same ELIN.

## Prerequisites

### Requirements

Cisco recommends you have a knowledge of:

- Cisco Emergency Responder (CER)

- Cisco Unified Communications Manager (CUCM)

A pre-requisite to Tertiary Redundancy is to first configure both a Primary and Secondary CER server as documented in the Cisco Emergency Responder Administration Guide for your version of CER.

### Components Used

The information in this document is based on the following software versions (but is also applicable to other versions):

- Cisco Unified Communications Manager (CUCM) version 12.5.1.11900-146 (12.5(1)SU1)

- Cisco Emergency Responder (CER) version 12.5.1.19000-38 (12.5(1)SU1)

The information in this document was created from the devices in a specific lab environment.  All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

The configuration documented in the various Cisco Emergency Responder Administration Guides allows for secondary redundancy of CER via a CER cluster—with a second CER server.   If this second CER server is also down, or CUCM connectivity with both CER servers is not working, then CUCM can still be configured to re-route the calls to the PSAP (911)—through exactly the same SIP Trunk—with Calling Numbers that are based on the callers physical location.

Note : This configuration example assumes that each physical location also has its own Device Pool already configured in CUCM.   It also assumes that CER has already first been configured to use a Route Pattern of 10.911 with the ELIN provided by CER.

If both CER's are down then the following can be used to route the call to the PSAP with a 11.911 Route Pattern and Calling Numbers that are specific to each location.  i.e. If the CER 911 CTI route point (RP911) fails, it must be configured to route calls to the CER 912 CTI route point (RP912).  If this has also failed, then it is configured to route to 11911.

The CER 912 CTI route point (RP912) has its Directory Number configured with the following Call Forward and Call Pickup Settings :

Create a Local Route Group for each location, e.g.

Create a CER-Down-RL Route List and add the Local Route Groups previously configured:

Click the link for each Local Route Group under Route List Details — one by one from within the above Route List — and add a different Calling Party Transform Mask for each Local Route Group:

...and continue for all of the remaining Route Groups in the above CER-Down-RL Route List.

For the following Route Patterns, 10.911 sends calls directly to the usual SIP "head end" Route List (in this case PSTN-RL ) when the CER servers are up. 11.911 sends calls to the CER-Down-RL (for the tertiary redundancy):

Next, navigate to each Device Pool and set only one Local Route Group for each site.  These point to the usual SIP "head end" route group (in this case CUBE iTSP PSTN Route Group ). There is no need to configure more route groups as it uses this group with the mask applied inside the route list/route group mask settings:

...and continue for all of the remaining Device Pools.

## Verify

In order to test, first ensure first ensure you have a phone in each of the Device Pools, then disable both CER servers.

This works with a single CER-911-PT partition and a single CER-911-CSS calling search space (CSS).

Note : Calls back from the PSAP to each ELIN must normally use Translation Patterns to prefix 913 and route calls back to CER via a CTI Route Point.   If CER is down, then the Call Forward settings of the CTI Route Point must already be configured with the "Onsite security number" (per the Cisco Emergency Responder Administration Guides).

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Craig Cooper

Cisco TAC

Chris Horne

ConvergeOne

### This Document Applies to These Products

- Emergency Responder

- Unified Communications Manager (CallManager)