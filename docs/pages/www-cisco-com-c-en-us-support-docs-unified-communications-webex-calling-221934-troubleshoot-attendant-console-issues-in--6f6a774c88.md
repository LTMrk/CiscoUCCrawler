---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-221934-troubleshoot-attendant-console-issues-in--6f6a774c88
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/221934-troubleshoot-attendant-console-issues-in.html
retrieved_at: 2026-08-21T07:16:31.905914+00:00
---

Troubleshoot Attendant Console Issues in Webex Calling

# Troubleshoot Attendant Console Issues in Webex Calling

### Download Options

Updated: April 24, 2024

Document ID: 221934

Contents

## Contents

## Introduction

This document describes the most common issues faced with the Attendant Console tool in Webex Calling (WxC).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub

- Receptionist Client

### Components Used

This document is not restricted to specific hardware and software version. The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The Attendant Console for Webex Calling is an application designed to help receptionists or operators manage incoming calls efficiently. This console provides a user-friendly interface that allows the attendant to handle multiple calls simultaneously, easily transfer calls to the appropriate party, monitor the status of lines within the organization, and access directories for quick call routing.

## Common Attendant Console Issues

### Ensure the Organization and the User have the Attendant Console Licenses

The user must have Webex Calling Professional license and Attendant Console license.

Step 1. Under MANAGEMENT > Users click the User .

Step 2. Scroll to Summary > License .

Step 3. Ensure that both Webex Calling Professional license and Attendant Console license are assigned.

Licenses Summary

Step 4. If the necessary Licenses are not added, click Edit Licenses > Edit Licenses > Calling .

Edit User Calling Licenses

Step 5. Click the checkbox for the needed Licenses.

Step 6. Click Save .

### Attendant Console License not Available for the User

If the Attendant Console is not available for the user, this could be because the organization does not have any Attendant Console Licenses available.

Step 1. Under MANAGEMENT > Account > Subscriptions > License Summary > Calling .

Account Calling License Summary

Step 2. Ensure Attendant Console Assigned licenses have not reached the Account's limit.

Step 3. If the Attendant Console Assigned licenses do not show in the Summary or more Licenses are needed, refer to Provisioning the Attendant Console license .

### After Provisioning with Attendant Console Licenses, Receptionist Still Appears in Control Hub

Trial organizations that were originally provisioned with Receptionist Client feature and provided with Attendant Console trial licenses afterwards, continue to see the Receptionist Client in SERVICES > Calling > Features > Receptionist Client .

Receptionis Client Feature

In the User level at MANAGEMENT > Users > Calling > User call experience , the Receptionist Client appears as well.

User Receptionist Client

These organizations can use the Attendant Console client in the Webex App. Once the Attendant Console license has been purchased, the Receptionist Client and the user's calling setting under User call experience is expected to change to the Attendant Console option.

### Attendant Console not Available in the Webex App

Embedded Apps are required for the Attendant Console to display in the Webex App to ensure that these are allowed in the organization:

Step 1. Go to MANAGEMENT > General > Embedded Apps .

Step 2. Ensure that Allow users access to Embedded Apps from meetings, spaces, and the Webex App sidebar toggle is Allowed .

Organization Embbeded Apps

Step 3. Re-Sign In the Webex App.

## Collect Logs from the Attendant Console Client

Collect logs to troubleshoot any issue not mentioned in this document:

Step 1. Reproduce the issue in the Attendant Console Client.

Step 2. Click Profile and Settings on top right.

Porfile and Settings

f

Step 3. Click Help > Download application logs .

Download Application Logs

Step 4. Logs can be found on your Downloads as a Zip file.

## Recommended Information for a TAC Case

If an issue persists after the troubleshooting steps in this document have been performed and a TAC case is needed, Cisco recommends to include this information:

- Organization ID

- Location ID or Location Name

- Attendant Console User's Number, extension and mail

- A detailed description of the issue experienced.

- Time zone and Timestamp of the Issue experienced.

- Attach the Attendant Console application logs from the User.

## Related Information

Get Started with the Attendant Console

### Revision History

1.0

24-Apr-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 24-Apr-2024 | Initial Release |