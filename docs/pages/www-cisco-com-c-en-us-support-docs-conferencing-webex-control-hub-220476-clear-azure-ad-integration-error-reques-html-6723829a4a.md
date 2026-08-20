---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-220476-clear-azure-ad-integration-error-reques-html-6723829a4a
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/220476-clear-azure-ad-integration-error-reques.html
retrieved_at: 2026-08-20T21:12:32.779968+00:00
---

Clear Azure AD Integration Error "Request Was Unauthorized"

# Clear Azure AD Integration Error "Request Was Unauthorized"

### Download Options

Updated: May 23, 2023

Document ID: 220476

Contents

## Contents

## Introduction

This document describes how to clear the message "The request was unauthorized" in the Azure AD integration.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Control Hub.

- Exchange of user identity information between identity domains a.k.a. System for Cross-domain Identity Management (SCIM).

### Components Used

The information in this document is based on these software and hardware versions:

- Control Hub build: 20230519-182b260.

- Azure Active Directory SCIM.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

If users and groups are managed in Microsoft Azure Active Directory, the Azure AD service can be configured within the Control Hub to synchronize them.

## Azure AD integration Error

If Cisco Webex Identity Syncrhonization Enterprise application was deleted from Microsoft Azure Active Directory, the service is inoperable as stated in this error message:

```
Azure AD integration error. The request was unauthorized. Please sign out and try again. TrackingID: ATLAS_497d70df-8811-4b6b-9b6a-ef4f438b57f6_136
```

Control Hub error

Error

### Debug Detailed Information

```
Referrer: Control Hub notification toaster-links
Browser URL: https://admin.webex.com/settings
Control Hub Build: 20230519-182b260
View Org ID: 2fdb923e-1d23-4e1b-a30f-e9cd88845744
Logged-in User ID: 09e7e177-3b96-47a9-bf96-9f607451d8a9
Logged-in User Org ID: 2fdb923e-1d23-4e1b-a30f-e9cd88845744
Logged-in User Clock UTC: Sun, 21 May 2023 22:44:59 GMT
Customer Type: Enterprise

Status: 401
Status Text: Unauthorized
URL: https://identity-b-us.webex.com/extIntegration/azureAD/2fdb923e-1d23-4e1b-a30f-e9cd88845744/v1/WebexApplications/status
Tracking ID: ATLAS_497d70df-8811-4b6b-9b6a-ef4f438b57f6_136
Error: {
  "error": {
    "key": "401",
    "message": [
      {
        "code": "701018",
        "description": "Request unauthorized. client-request-id: 9afc732a-2dcf-44e0-8bd8-49db92e483b7"
      }
    ]
  },
  "trackingId": "ATLAS_497d70df-8811-4b6b-9b6a-ef4f438b57f6_136"
}

Message: Azure AD integration error. The request was unauthorized. Please sign out and try again. TrackingID: ATLAS_497d70df-8811-4b6b-9b6a-ef4f438b57f6_136
```

SCIM GET Request error 401 refers to:

```
401 	The request is unauthenticated. The user’s credentials are missing or incorrect.
```

## Problem

### Azure Active Directory

Log into the Azure portal and navigate to Azure Active Directory > Enterprise Applications . Azure AD integration requires two Enterprise applications for this new deployment:

- Cisco Webex Identity

- Cisco Webex Identity Integration

Azure AD

Cisco Webex Identity Integration Enterprise application was removed by an Azure Administrator.

### Azure Active Directory Audit Logs

If required, audit logs can show details that confirm the deletion.

Audit logs

## Solution

### Rebuilt Identity Synchronization

You can provide Administrator consent with this URL in an incognito browser tab:

```
https://login.microsoftonline.com/common/adminconsent?client_id=90db942a-c1eb-4e8d-82e4-eebf64a7e2ae
```

With Azure Administrator credentials, click on Accept to confirm the action.

Consent

Click Accept and close the browser tab after the message below:

Error

## Validate Service

### Azure Active Directory

Log into the Azure portal and navigate to Azure Active Directory > Enterprise Applications . Cisco Webex Identity Integration is restored.

Azure AD check

### Webex Control Hub

Log into the admin.webex.com and navigate to Management > Organization Settings > Directory Synchronization > Allow Azure AD Sync . If only Cisco Webex Identity Integration was deleted, the original configuration is restored.

Control Hub check

## Related Information

- Set up Azure AD Wizard App in Control Hub

- SCIM API 2.0 Error Codes

Cisco Technical Support & Downloads

### Revision History

1.0

23-May-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-May-2023 | Initial Release |