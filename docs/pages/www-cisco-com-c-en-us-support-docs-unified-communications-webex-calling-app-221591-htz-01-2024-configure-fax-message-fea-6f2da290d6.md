---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-app-221591-htz-01-2024-configure-fax-message-fea-6f2da290d6
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling-app/221591-htz-01-2024-configure-fax-message-featu.html
retrieved_at: 2026-08-16T21:59:55.642294+00:00
---

Configure Fax Message Feature for Webex Calling Users

# Configure Fax Message Feature for Webex Calling Users

### Download Options

Updated: January 31, 2024

Document ID: 221591

Contents

## Contents

## Introduction

This document describes how to configure Fax messaging for Webex calling users.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Knowledge about configuration in Control hub

- Have a location with Webex Calling service and with the Voiceportal enable.

- Have a user with a calling license enabled and the Voicemail feature turned on.

### Components Used

The information in this document is based on these software and hardware versions:

- Webex calling user

- Control hub

- User portal

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Extends the Messaging service to allow users to receive, store, review, and manage Fax messages. Users are notified of new Fax messages like they are notified of new voice messages. Fax messages can be retrieved by email or retrieved directly on the user portal

## How to Enable Fax Messaging for Webex Calling Users

Webex Calling Users can receive Faxes on a new and unassociated number( different from their number). It is included in their Calling License, you need to enable it in the Voicemail section of the user configuration.

### Through Configuration

Step 1 . Sign in to Control Hub

Control Hub login

Step 2. Click on Users and search for the user you want to enable to receive Faxes.

Select user

Step 3 . Click on the user, go to Calling , and click on Voicemail.

Voicemail

Step 4 . Scroll to the bottom of the page, where it says Fax Messaging .

Fax messaging

Step 5 . Toggle the bar to enable Receive Fax Messages .

enabkle toggle

Step 6 . Enter the phone number you want to receive Fax messages on then click on Save .

Set number

### Retrieve the Fax Messaging

#### By Email

Step 1. Sign in to Control Hub.

Control Hub login

Step 2 . Click on Users and search for the user you want to enable to receive Faxes.

Select user

Step 3 . Click on the user, go to Calling , and click on Voicemail .

Voicemail

Step 4. Scroll to Aditional Settings

Carbon copy

Step 5 . Mark Email a copy of  voicemail message and set the email where receive the Faxes, then click on save

email copy

#### Through the User Portal

Step 1 . Sign in to the User Portal (with the user account).

user portal sign in

Step 2 . Navigate to Webex calling .

user portal

Step 3 . Click on Voicemail .

Step 4 . Search for the Fax that you want to retrieve.

Step 5 . Click on Download .

Download image

Note : The Fax content  be in .tiff image format.

## Related Information

- Manage a Shared Voicemail and Inbound Fax Box for Webex Calling

### Revision History

1.0

31-Jan-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 31-Jan-2024 | Initial Release |