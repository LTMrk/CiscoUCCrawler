---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-support-223083-troubleshoot-webex-scheduling-error-html-010e227ed5
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-support/223083-troubleshoot-webex-scheduling-error.html
retrieved_at: 2026-09-01T14:57:06.951747+00:00
---

Troubleshoot Webex Scheduling Error "Unauthorized from O365. Admin Action is Required."

# Troubleshoot Webex Scheduling Error "Unauthorized from O365. Admin Action is Required."

### Download Options

Updated: June 10, 2025

Document ID: 223083

Contents

## Contents

## Introduction

This document describes how to identify and fix the error "Unauthorized from O365. Admin action is required." on Webex Users or Workspaces.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Webex Organization.

- Webex Hybrid Calendar.

- Microsoft 365 Admin

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Control Hub b uild 20250411-201f9f2 .

- Hybrid Calendar with Microsoft 365.

- Microsoft 365 admin

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

During the first use of the set-up wizard for Hybrid Calendar, also known as Scheduling in Webex Control Hub, Administrators possibly face the error "Received error 'Unauthorized' from O365. Admin action is required." for either a Webex user or a Workspace.

## Error from Control Hub

In the Workspaces section, under the users setting, Overview tab > Scheduling displays an "Unauthorized" message but no additional logging.

Workspace Error

## Troubleshooting

### HTTP Inspection

Under Overview tab > Scheduling section of the affected Workspace, open Developers Tools on FireFox or Web Developer Tools on Chrome; see Related Information for detailed steps.

Choose the Network tab in the Inspection console and click the See history button for the Workspace.

Getting HTTP Inspection

Select the request URL containing "xxx& serviceId=squared-fusion-cal " and click the Response tab to see the entries.

HTTP inspection

Caution : The Timestamp in Control Hub shows local PC time; the HTTP inspection timestamp shows Zulu time, also known as UTC.

```
"description": "Received error 'Unauthorized' from O365. Admin action is required."
```

## Root Cause

The message 'Unauthorized' from O365 means Webex throughout Microsoft Graph cannot find a mailbox for the user/workspace or; the domain mailbox is not part of tenant domains.

It is now time to confirm the mailbox from Microsoft.

## Validate Workspace Mailbox

### Microsoft Graph

Go to Microsoft Graph API , select GET as an HTTP request method, and run a query with one of these URLs:

```
https://graph.microsoft.com/v1.0/places/{objectId}
https://graph.microsoft.com/v1.0/places/{roommailbox}
```

Graph Explorer

Caution : A Global Administrator is required to provide Admin consent in the Modify Permissions tab before click Run query.

The HTTP 404 Not Found client error response status code indicates that the server cannot find the requested resource.

```
"error":
"code": "UnknownError",
"message": ""
```

## Validate Domain Mailbox

### Control Hub

Go to admin.webex.com > Services > Hybrid > Hybrid Calendar with O365 > Edit settings . Click domain tenants to expland Tenant Details.

Domain Tenants

The Room email address does not match the one configured in Control Hub, which is a prerequisite for the Hybrid Calendar. Either edit the email address from Exchange admin or re-enable Workspace with the correct email address.

Activation Succeded

## Related Information

Requirements for Hybrid Calendar with Microsoft Office 365

Use Graph Explorer to try Microsoft Graph APIs

- How to open DevTools - Chrome

- How to open DevTools - FireFox

### Revision History

1.0

10-Jun-2025

Initial Release

### Contributed by Cisco Engineers

Josue Jonathan Vizcaino Huape

Technical Consulting Engineer

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Jun-2025 | Initial Release |