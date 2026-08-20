---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-222952-troubleshoot-webex-scheduling-error-html-cb1a9fad6b
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/222952-troubleshoot-webex-scheduling-error.html
retrieved_at: 2026-08-20T21:10:03.594485+00:00
---

Troubleshoot Webex Scheduling Error "Not Found" from O365. Admin Action is Required

# Troubleshoot Webex Scheduling Error "Not Found" from O365. Admin Action is Required

### Download Options

Updated: April 15, 2025

Document ID: 222952

Contents

## Contents

## Introduction

This document describes how to identify and fix the error "Not Found" from O365. Admin action is required on Webex Users or Workspaces.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Webex Organization.

- Webex Hybrid Calendar.

- Microsoft 365 Admin

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Control Hub b uild 20250411-201f9f2 .

- Hybrid Calendar with Office 365.

- Microsoft 365 admin

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

During the first use of the set-up wizard for Hybrid Calendar, also known as Scheduling in Webex Control Hub, Administrators possibly face the error "Received error 'Not Found' from O365. Admin action is required." for either a Webex user or a Workspace.

## Error for a User

In the Users section, under the users setting, go to Hybrid Services card > Status displays an "error by admin" message but no additional logging.

User Error

## Error for a Workspace

In the Workspaces section, under the Workspaces Overview , the error " No operational connector found for user. Check the cluster configuration and then try again " can be found in Issues & Information card or at the bottom in the Scheduling card.

Workspace Error

## Troubleshooting

### User account

Under the Hybrid Services of the affected user, open Developers Tools on FireFox or Web Developer Tools on Chrome; see Related Information for detailed steps.

Choose the Network tab in the Inspection console and click the Status button for the user.

Inspecting Status button

Locate the request URL containing "xxx& serviceId=squared-fusion-cal ".

Calendar Error status

Select the request URL containing "xxx& serviceId=squared-fusion-cal " and click the Response tab to see the entries.

Response entries

Correlating the first error after enabling the service with the response queries, the full detailed error status is located.

Activation Error

Caution : The Timestamp in Control Hub shows local PC time; the HTTP inspection timestamp shows Zulu time, also known as UTC.

```
"description": "Received error 'Not Found' from O365. Admin action is required."
```

Tip : Hover over the error message to show the full description; however it is good to know how to get it from an HTTP Inspection.

Hover

### Workspace account

In the Overview tab of the affected workspace, open Developers Tools on FireFox or Web Developer Tools on Chrome; see Related Information for detailed steps.

Choose the Network tab in the Inspection console and click See history for the user.

Workspace history

Locate the request URL containing "xxx& serviceId=squared-fusion-cal ".

Status History

Select the request URL containing "xxx& serviceId=squared-fusion-cal " and click on Response tab to see the entries.

Correlate the first error after enabling the service with the response queries where the full detailed error status is located.

Response entry

Caution : The Timestamp in Control Hub shows local PC time; the HTTP inspection timestamp shows Zulu time, also known as UTC.

```
"Received error 'Not Found' from O365. Admin action is required."
```

## Root Cause

The message 'Not Found' from O365 means Webex throughout Microsoft Graph cannot find a mailbox for the user/workspace. It is now time to confirm the mailbox from Microsoft.

## Validate User Mailbox

### Microsoft Graph

Go to Microsoft Graph API , select GET as an HTTP request method, and run a query with one of these URLs:

```
https://graph.microsoft.com/v1.0/me/mailboxSettings 
https://graph.microsoft.com/v1.0/users/{id|userPrincipalName}/mailboxSettings
```

Graph Explorer

Caution : A Global Administrator is required to provide Admin consent in the Modify Permissions tab before click Run query.

The HTTP 404 Not Found client error response status code indicates that the server cannot find the requested resource.

```
"error":
"code": "MailboxNotEnabledForRESTAPI",
"message": "The mailbox is either inactive, soft-deleted, or is hosted on-premise."
```

### Microsoft 365 admin

Go to Microsoft 365 admin > Users > Active users and locate the affected user.

Active users

Select the user and click the Licenses and apps tab in the users settings.

Licenses and apps

The license assigned does not contain an Exchange mailbox, which is a prerequisite for the Hybrid Calendar. Assign a valid license with Mailbox storage.

User with license + mailbox

## Validate Workspace Mailbox

### Microsoft Graph

Go to Microsoft Graph API , select GET as an HTTP request method, and run a query with one of these URLs:

```
https://graph.microsoft.com/v1.0/places/{objectId}
https://graph.microsoft.com/v1.0/places/{roommailbox}
```

Room Mailbox

Caution : A Global Administrator is required to provide Admin consent in the Modify Permissions tab before click Run query.

The HTTP 404 Not Found client error response status code indicates that the server cannot find the requested resource.

```
"error": {
"code": "UnknownError",
```

### Exchange admin

Go to Exchange admin > Recipients > Resources and locate the affected workspace.

Resources

The Room email address does not match the one configured in Control Hub, which is a prerequisite for the Hybrid Calendar. Either edit the email address from Exchange admin or re-enable Workspace with the correct email address.

Workspace fixed

## Related Information

Requirements for Hybrid Calendar with Microsoft Office 365

Use Graph Explorer to try Microsoft Graph APIs

- How to open DevTools - Chrome

- How to open DevTools - FireFox

### Revision History

2.0

15-Apr-2025

Initial Release

1.0

14-Apr-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 15-Apr-2025 | Initial Release |
| 1.0 | 14-Apr-2025 | Initial Release |