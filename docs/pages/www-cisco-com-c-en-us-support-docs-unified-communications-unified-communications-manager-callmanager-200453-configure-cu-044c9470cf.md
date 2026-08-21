---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200453-configure-cu-044c9470cf
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200453-Configure-CUCM-Native-Call-Queuing-Featu.html
retrieved_at: 2026-08-21T13:54:52.190318+00:00
---

Configure CUCM Native Call Queuing Feature

# Configure CUCM Native Call Queuing Feature

### Download Options

Updated: April 28, 2016

Document ID: 200453

Contents

## Contents

## Introduction

This document describes how to configure the Cisco Unified Communications Manager (CUCM) Native Call Queuing feature.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM 9 and higher versions

- Basic Call Hunt feature

### Components Used

The information in this document is based on CUCM 11.X and higher versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

For CUCM, often its hunt pilot has more calls than its hunt member can handle at a given time. CUCM Native Call Queuing feature introduces the ability to hold hunt pilot callers in queue while they wait for an agent to become available.

Note : Native Call queuing feature allows up to 100 callers to be queued per hunt pilot.

## Configure

Step 1. Navigate to Media resources > Music on Hold Source Page , as shown in the image:

Step 2. Create a new audio source, as shown in the image:

Step 3. Set Multicasting to the desired setting and set announcement parameters , as shown in the image:

Step 4. Select the Initial Announcement, as shown in the image:

Step 5. Select the Periodic Announcement, as shown in the image:

Step 6. Select the periodic announcement interval (the default is 30 seconds), as shown in the image:

Step 7: Select the locale for announcements, as shown in the image:

While the calling party is in queue the caller gets Music On Hold (MOH) treatment which depends upon the network MOH settings for that hunt pilot. There is option ( Music on Hold audio source page and field is Initial announcement played) to first play initial announcement and then offer a call to hunt pilot. If the call is not answered by any of the agents, it places the caller on hold ( in queue)  and on success provided, it repeates the announcement (periodically provided) and music on hold.

Second option is to first offer the call to hunt pilot Directory Number (DN) and if the call is not answered,it places caller on hold (in queue) and on success provides an Initial announcement, repeated announcement (periodically provided) and music on hold.

Step 8. In the configuration page, navigate to Call Routing > Route/Hunt > Hunt Pilot, as shown in the image:

Step 9. A Hunt List must be defined and selected, as shown in the image:

Step 10. Select Queue Calls on the Hunt Pilot page to enable queuing for this Hunt Pilot, as shown in the image:

The Maximum number of simultaneous callers in queue for each Hunt Pilot is configurable from 1-100 (Default 32)

The maximum wait time in queue for each hunt pilot is configurable from 0 - 3600 (default 900)

For each hunt pilot, callers can be routed to configurable secondary destinations if:

- The Maximum queue wait is met

- The maximum queue capacity has been reached

- No agents are logged in or registered

Step 11. Select an audio source for MOH and Announcements, as shown in the image:

Step 12. Set the maximum number of calleers and maximum queue wait time, as shown in the image:

Step 13. Lastly, configure the secondary routing if required, as shown in the image:

## Verify

### Queue Status Softkey

You can configure a new phone button template which has Queue Status option configured on any line of the phone. You are required to apply the phone button template on the corresponding phone, as shown in the image:

Once the phone button teamplate is assigned to the phone, you can see Queue Status on the line, as shown in the image,

Queue statistics are displayed, as shown in the image:

### Serviceability Counters

New serviceability counters are added in the Real-Time Monitoring Tool (RTMT) under Cisco Hunt Pilots to the monitor queuing.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

28-Apr-2016

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 28-Apr-2016 | Initial Release |