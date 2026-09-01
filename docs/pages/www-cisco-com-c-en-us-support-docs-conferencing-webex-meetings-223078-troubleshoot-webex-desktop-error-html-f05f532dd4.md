---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-223078-troubleshoot-webex-desktop-error-html-f05f532dd4
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/223078-troubleshoot-webex-desktop-error.html
retrieved_at: 2026-09-01T14:56:11.916663+00:00
---

Troubleshoot Webex Desktop Error "Meeting Not Scheduled!" - General Server Error

# Troubleshoot Webex Desktop Error "Meeting Not Scheduled!" - General Server Error

### Download Options

Updated: June 5, 2025

Document ID: 223078

Contents

## Contents

## Introduction

This document describes how to identity and fix General server error in Webex app while tying to schedule a meeting.

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

Webex app users report inability to schedule meetings from the Webex app, encountering the error " Meeting isn't scheduled ".

## Webex app error

In the Webex app interface for Windows, go to Meetings > Schedule a meeting , fill meeting details, and click Schedule . The error Meeting not scheduled! General server error prevents scheduling the meeting.

Webex app Error

## Gathering logs

### Control Hub

Have the affected user send Webex app logs after getting the error and collect Feedback ID; Access admin.webex.com > Monitoring > Troubleshooting > Logs . Input the affected user email address and press Enter in the keyboard.

Webex logs

Click the User logs blue icon to download the file. Make sure Feedback ID matches the one collected from the Webex app.

Feedback ID

## Reading logs

### Webex app

With the uncompressed logs stored locally, locate current_log.txt and lookup for calendar.schedule or scheduleAppointmentResponse .

```
2025-06-05T02:21:08.700Z <Debug> [113164:0x14618][]CalendarAdapter.cpp:350 CalendarAdapter::onDataArrived::Calendar event schedule response arrived: {"alertType":"full","data":{"eventType":"calendar.schedule","scheduleAppointmentResponse":{"errorMsg":"Invalid user status: error for user, stop processing","errorType":"SERVER_ERROR","operation":"CREATE","orgId":"2fdb923e-1d23-4e1b-a30f-e9cd88845744","requestUUID":"2211a39a-cab0-4a65-9c23-ec6cf1ac8f1b","requestedBy":"66cc49f0-d3e6-4de7-8299-480fcbfc2176","success":false},"trackingId":"CLIENT_9f63aa00-081b-49ac-bddc-2a2a2374fa5c"},"filterMessage":false,"headers":{},"id":"16b04afb-b5c7-484b-a406-c7cb00bae031","sequenceNumber":31,"timestamp":1749090068519,"trackingId":"CLIENT_9f63aa00-081b-49ac-bddc-2a2a2374fa5c","wsWriteTimestamp":1749090068519}
```

Error message Invalid user status refers to the Hybrid Calendar status from Control Hub.

```
"errorMsg":"Invalid user status: error for user, stop processing","errorType":"SERVER_ERROR"
```

### Control Hub user status

Go to admin.webex.com > Management > Users > affected user > Hybrid Services to see current status for Calendar service.

User status error

## Root Cause

Because the Hybrid Calendar service is not operational for the user, meetings cannot be processed until service is fully activated.

## Solution

Temporary workaround: disable Hybrid Calendar for the affected user to use the basic Cloud scheduler service.

The integrity of the Hybrid Calendar service needs to be reviewed to have the users re-enabled to be able to schedule meetings from Webex app.

Check the mailbox status from Microsoft 365 Admin portal.

## Related Information

- Troubleshoot Webex Scheduling Error "Not Found" from O365. Admin Action is Required

- Hybrid Services and Connector Troubleshooting

### Revision History

1.0

05-Jun-2025

Initial Release

### Contributed by Cisco Engineers

Josue Jonathan Vizcaino Huape

Technical Consulting Engineer

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Jun-2025 | Initial Release |