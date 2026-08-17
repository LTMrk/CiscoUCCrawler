---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-222835-troubleshoot-webex-workspace-scheduling-html-abf6fa5a56
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/222835-troubleshoot-webex-workspace-scheduling.html
retrieved_at: 2026-08-17T00:53:54.337118+00:00
---

Troubleshoot Webex Workspace Scheduling error "The booking request failed"

# Troubleshoot Webex Workspace Scheduling error "The booking request failed"

### Download Options

Updated: October 21, 2025

Document ID: 222835

Contents

## Contents

## Introduction

This document describes how to identify and fix the error "The booking request failed" on Webex Workspaces.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Webex Organization.

- Webex Hybrid Calendar.

- Webex Workspaces.

### Components Used

The information in this document is based on these software and hardware versions:

- RoomOS 11.23.1.8 3963b07b5c5 Stable release.

- Hybrid Calendar with Office 365.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

Webex Users are unable to schedule meetings directly from a Webex Room device with error "The booking request failed - The cloud used too much time responding." in the screen.

## In-room booking

In the Workspace touch controller, while using the Book room wizard to schedule a Webex meeting and asserting Confirm meeting title , the error " The booking request failed - The cloud used too much time responding. " does not let the process finish.

Scheduling Error

## Control Hub troubleshooting

### Workspace scheduling settings

Navigate to admin.webex.com > Management > Workspaces > Workspace affected > Scheduling settings . Ad-hoc Booking is Disabled .

Ad-hoc booking status

### Hybrid Calendar settings

Navigate to admin.webex.com > Services > Hybrid > Hybrid Calendar > Edit settings .

Calendar settings

Click the tenant name to open the settings menu. Check Scheduling Account field.

Scheduling Account

### Device logs lookup

Navigate to admin.webex.com > Devices > device affected > Support > Device Logs > + Generate Log to get a Full Log file and download it locally.

Device Logs

Decompress the downloaded log file, locate the file all.log , and open it.

```
log-bundle-XXX > var > log > eventlog > all.log
```

All.log file

Make sure to have the timestamp of the failure which can be pulled from the error reported or by lookup for "Org Scheduling Account not configured" in the all.log file.

```
2025-03-13T13:31:59.765-04:00 main[2343]: Wx2 W: POST failed: HTTP/1.1 400 Bad Request (url = https://calendar-cloud-connector-r.wbx2.com/api/orgs/2fdb923e-1d23-4e1b-a30f-e9cd88845744/machines/08700e00-6c83-4032-b261-250673f09f13/services/squared-fusion-cal/appointments, request/response TrackingId = CLIENT-libwx2_976691dd-5f28-4c47-a0d0-5a064afcf758_156, error = 'Org Scheduling Account not configured')
```

## Root Cause

Scheduling Account is required to allow In-Room booking for Workspaces. It is configured in the Hybrid Calendar first deployment or can be added at any time later from admin.webex.com .

## Solution

Enter the email address of the organizer for meetings scheduled from Workspaces.

Scheduling Account

Note : Workspaces without In-room booking enabled need manual intervention to enable it.

## Known Issues

After a Scheduling Account is configured error, "The booking request failed - The cloud used too much time responding." is still present.

Note : Scheduling Account needs to be a user activated for the Hybrid Calendar service in Control Hub with a valid mailbox in Exchange.

## Related Information

Enable and configure Hybrid Calendar with Microsoft 365

In-room booking with a touch controller

### Revision History

2.0

21-Oct-2025

Initial Release

1.0

14-Mar-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 21-Oct-2025 | Initial Release |
| 1.0 | 14-Mar-2025 | Initial Release |