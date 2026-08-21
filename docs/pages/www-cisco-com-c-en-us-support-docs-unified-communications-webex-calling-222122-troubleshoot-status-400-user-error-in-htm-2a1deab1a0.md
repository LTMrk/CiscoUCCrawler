---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-222122-troubleshoot-status-400-user-error-in-htm-2a1deab1a0
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/222122-troubleshoot-status-400-user-error-in.html
retrieved_at: 2026-08-21T07:16:27.611853+00:00
---

Troubleshoot "Status: 400" User Error in Control Hub

# Troubleshoot "Status: 400" User Error in Control Hub

### Download Options

Updated: July 17, 2024

Document ID: 222122

Contents

## Contents

## Introduction

This document describes how to troubleshoot a “Status: 400” user error when manually assigning a Webex Calling license in Control Hub.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Webex Control Hub

- HTTP Archive (HAR) Analyzer

### Components Used

This document is not restricted to specific hardware and software versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Webex Control Hub is a web-based management portal for the Webex portfolio of products. It provides a centralized platform to manage users, licenses, and devices.

For Webex Calling services, it is through Control Hub that administrators can create and assign users with Webex Calling licenses.

Whenever an administrator encounters issues within the Control Hub platform, particularly during the user creation process for Webex Calling services, one of the initial steps in the troubleshooting procedure is to generate a HAR file. A HAR file captures a record of the interaction between Control Hub and the web browser during the session in which the issue occurred. This file includes detailed information about each web request and response, which is used for diagnosing and resolving problems.

## Problem

### User Creation Error

Step 1. Under MANAGEMENT > Users .

Step 2. Click Manage Users > Manually add users .

Step 3. Start with the creation process for the user.

Step 4. At the last screen, this error screen is presented.

User Creation Error

### Webex Calling License Assignment Error

Step 1. Under MANAGEMENT > Users, select the User .

Step 2. Scroll to Summary > License.

Step 3. C lick Edit Licenses > Edit Licenses > Calling .

Step 4. Click the checkbox to add the Webex Calling license.

Step 5. Click Save .

Step 6. At the last screen, this pop-up error is presented.

License Assignment Error

## Troubleshoot

### Generate the HAR File

In order to start with the troublshooting process, you need to Generate a HAR File in Your Browser that contains the information when the issue occurs.

In order to reproduce the issue, choose one of these options.

- For this option, you can start to generate the HAR file since the Step 2: Assign license for users screen and until the error message screen is presented.

- For this option, you can start to generate the HAR file since the Edit Licenses button is clicked and until the pop-up error message is presented.

### Analyze the HAR File

Step 1. Use a HAR Analyzer to open the previously generated HAR file and review all its content.

Step 2. Check the POST request made to the Uniform Resource Locator (URL) finishing in /users/onboard.

POST Request in HAR File

Step 3. Check the POST response, which can have content similar to this.

```
[
    {
        "email": "<user e-mail>",
        "uuid": "<user uuid>",
        "status": 400,
        "errorList": [
            {
                "errorCode": 5302,
                "description": "POST failed: HTTP/1.1 409 Conflict (url = https://cpapi-r.wbx2.example/api/v1/customers/<org-id>/users, request/response TrackingId = ATLAS_8666bff8-a5f2-4a6c-a31d-c7dccea7315c_30, errorCode = '5302', error = '[Error 10991] Url already exists: <user e-mail>')"
            }
        ]
    }
]
```

### Review the Error Description in the HAR File

The error details are specified in the description section. Inside here the error message is error = '[Error 10991] Url already exists: ' , and the e-mail of the user.

## Solution

This is occurring due to the e-mail already being associated with a Webex Calling account.

On most occasions, the account belongs to a Webex Calling Carrier, so for this account to be correctly provisioned within an organization in Control Hub, the e-mail must first be deleted from the Webex Calling Carrier account to which it is associated.

Note : In case the e-mail of the user is already associated to an organization inside Control Hub, the error message displayed is different. In this case, the error message includes the description of the problem along with the documentation to claim the user in another organization.

## Recommended Information for a TAC Case

If the issue persists after the troubleshooting steps in this document have been performed, or the POST response in the HAR file contains a different message, open a case with TAC.

Cisco recommends you to include this information:

- Organization ID

- E-mail of the affected user.

- A description of the issue experienced.

- Attach HAR file replicating the issue.

- POST response content from the HAR file.

## Related Information

- Add users manually in Control Hub

- Edit service licenses in Control Hub for individual users

### Revision History

1.0

17-Jul-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Jul-2024 | Initial Release |