---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-app-220861-troubleshoot-error-couldn-t-save-the-mi-html-85986364fc
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-app/220861-troubleshoot-error-couldn-t-save-the-mi.html
retrieved_at: 2026-08-16T22:06:04.171468+00:00
---

Troubleshoot Error "Couldn't Save the Microsoft 365 Calendar Config"

# Troubleshoot Error "Couldn't Save the Microsoft 365 Calendar Config"

### Download Options

Updated: September 1, 2023

Document ID: 220861

Contents

## Contents

## Introduction

This document describes how to solve Hybrid Calendar deployment wizard error while testing an Office 365 account.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Control Hub.

- Microsoft 365 Tenant.

### Components Used

The information in this document is based on these software and hardware versions:

- Control Hub build 20230808-be08fd6 (mfe).

- Office 365 E3 licensing.

- Google Chrome 115.0.5790.170 x64 .

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

During the Hybrid Calendar with Office 365 deployment wizard after authorize with the Microsoft 365 global admin account it is required to test the connection with Office 365 calendar.

## Troubleshoot

### Hybrid Calendar Setup - Test Account

The next error is present after adding an email address to test the connection.

Error

```
Couldn't save the Microsoft 365 Calendar config. TrackingID: ATLAS_1b8fa3a2-5760-451e-86ea-e7b9b7758e62_13
```

Debug info:

```
Referrer: Control Hub notification toaster-links
Browser URL: https://admin.webex.com/hybrid-services?office365=success
Control Hub Build: 20230808-be08fd6
View Org ID: 2fdb923e-1d23-4e1b-a30f-e9cd88845744
Logged-in User ID: 09e7e177-3b96-47a9-bf96-9f607451d8a9
Logged-in User Org ID: 2fdb923e-1d23-4e1b-a30f-e9cd88845744
Logged-in User Clock UTC: Thu, 10 Aug 2023 02:34:31 GMT
Customer Type: Enterprise

Status: 400
Status Text: OK
URL: https://https://calendar-cloud-connector-r.wbx2.com/api/v1/orgs/2fdb923e-1d23-4e1b-a30f-e9cd88845744/services/squared-fusion-cal/provisioning/confirmO365Provisioning?testEmail=cconnector@rtpcloudcollab.com&schedulingAccount=
Tracking ID: ATLAS_1b8fa3a2-5760-451e-86ea-e7b9b7758e62_13
Error: {
  "errorCode": 6,
  "message": "Bad request",
  "errors": [
    {
      "errorCode": 6,
      "description": "Bad request"
    }
  ],
  "trackingId": "ATLAS_1b8fa3a2-5760-451e-86ea-e7b9b7758e62_13"
}

Message: Couldn't save the Microsoft 365 Calendar config. TrackingID: ATLAS_1b8fa3a2-5760-451e-86ea-e7b9b7758e62_13
```

### Microsoft 365 Admin Center

Navigate to the Microsoft 365 admin portal with an admin account. Navigate to Users > Active users > account used during test. Select the user and navigate to Licenses and apps tab.

Microsoft 365

## Conclusion

It is required to have a Microsoft 365 license assigned in order to test/activate users for Hybrid Calendar with Office 365 service.

Prerequisites

Assigning a license to the user and retry the Calendar integration can succeed now.

Office license

Error cleared

Note : It is not required to have the test account in Control Hub but in order to use Hybrid Calendar service the account needs to be in both sides Control Hub and Microsoft 365.

## Related Information

- Deploy cloud-based Hybrid Calendar for Office 365

- Cisco Technical Support & Downloads

### Revision History

1.0

01-Sep-2023

Initial Release

### Contributed by Cisco Engineers

Josue Vizcaino

Cisco TAC Engineer

### This Document Applies to These Products

- Webex App

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 01-Sep-2023 | Initial Release |