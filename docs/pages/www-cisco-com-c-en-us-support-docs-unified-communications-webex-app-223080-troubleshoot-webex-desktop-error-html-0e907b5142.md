---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-app-223080-troubleshoot-webex-desktop-error-html-0e907b5142
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-app/223080-troubleshoot-webex-desktop-error.html
retrieved_at: 2026-08-16T22:05:51.270492+00:00
---

Troubleshoot Webex Desktop Error "Meeting Not Scheduled!" - Create Failed

# Troubleshoot Webex Desktop Error "Meeting Not Scheduled!" - Create Failed

### Download Options

Updated: June 9, 2025

Document ID: 223080

Contents

## Contents

## Introduction

This document describes how to identify and fix a "Create Failed" error in Webex app while trying to schedule a meeting.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Webex Organization.

- Webex Hybrid Calendar.

- Webex app.

### Components Used

The information in this document is based on these software and hardware versions:

- Webex app 44.7

- Hybrid Calendar with Microsoft 365

- Windows 10 Enterprise

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

Webex app users report inability to schedule meetings from the Webex app, encountering the error " Meeting not scheduled ".

## Webex app error

In the Webex app interface for Windows, go to Meetings > Schedule a meeting , provide meeting details, and click Schedule . The error " Meeting not scheduled! Create Failed " prevents scheduling the meeting.

Webex app error

Error

## Gathering logs

### Control Hub

Have the affected user send Webex app logs after getting the error and collect Feedback ID; Access admin.webex.com > Monitoring > Troubleshooting > Logs . Input the affected user email address and press Enter in the keyboard.

Webex logs

Click the blue User logs download icon to download the file. Make sure Feedback ID matches the one collected from the Webex app.

Feedback ID

## Reading logs

### Webex app

With the uncompressed logs stored locally, locate current_log.txt and lookup for calendar.schedule or scheduleAppointmentResponse .

```
2025-04-20T01:43:13.411Z <Debug> [38592:0xa6b4][]CalendarAdapter.cpp:350 CalendarAdapter::onDataArrived::Calendar event schedule response arrived: {"alertType":"full","data":{"eventType":"calendar.schedule","scheduleAppointmentResponse":{"callAnalyzerId":"9978ec6d-b3c7-4d9d-8e00-d7d9c3771074","errorMsg":"Access to OData is disabled: [RAOP] : Blocked by tenant configured AppOnly AccessPolicy settings.","errorType":"CREATE_FAILED","globalMeetingId":"1f0b7ebae7694824aff33455ade0ad23","meetingOccurrenceId":"1f0b7ebae7694824aff33455ade0ad23","operation":"CREATE","orgId":"2fdb923e-1d23-4e1b-a30f-e9cd88845744","requestUUID":"7411931d-d220-4277-b6df-0dfda93c49d2","requestedBy":"67264af4-1371-4dd2-8d6b-b63f923d36e8","serviceType":"squared-fusion-cal","siteName":"rtpcloudcollab.webex.com","success":false},"trackingId":"CLIENT_bcd08015-1769-41a0-8b61-a966796f1bbd"},"filterMessage":false,"headers":{},"id":"2986604b-aae5-4ebd-af63-900ad4088b24","sequenceNumber":200,"timestamp":1745113393302,"trackingId":"CLIENT_bcd08015-1769-41a0-8b61-a966796f1bbd","wsWriteTimestamp":1745113393302}
```

Error message Invalid user status refers to the Hybrid Calendar status from Control Hub.

```
"errorMsg":"Access to OData is disabled: [RAOP] : Blocked by tenant configured AppOnly AccessPolicy settings."
```

## Checking mailbox settings from Microsoft 365

### Connect to Exchange Online PowerShell

Open a PowerShell window and load the module Connect-ExchangeOnline . Confirm if there is an Access Policy applied to affected user.

```
Test-ApplicationAccessPolicy -Identity user@domain -AppId de8bc8b5-d9f9-48b1-a8ad-b748da725064 - Graph Explorer
Test-ApplicationAccessPolicy -Identity user@domain -AppId 189ea49b-75a4-4e53-a013-2aed74803405 - Webex Calendar
```

Graph Explorer

Webex calendar

## Root Cause

The affected user mailbox has applied an Application Access Policy in Microsoft Exchange Online.

## Solution

Temporary workaround: disable Hybrid Calendar for the affected user to use the basic Cloud scheduler service.

A Microsoft 365 Administrator needs to validate proper access of Graph Explorer and Webex Hybrid Calendar service for the affected user/users/resources or use a different email without a policy applied.

## Related Information

- Connect to Exchange Online PowerShell

- Hybrid Services and Connector Troubleshooting

### Revision History

1.0

09-Jun-2025

Initial Release

### Contributed by Cisco Engineers

Josue Jonathan Vizcaino Huape

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Control Hub

- Webex App

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 09-Jun-2025 | Initial Release |