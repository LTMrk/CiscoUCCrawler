---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-220632-configure-and-dial-international-calling--ee054deb68
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/220632-configure-and-dial-international-calling.html
retrieved_at: 2026-08-21T07:15:40.933881+00:00
---

Configure and Dial International Calling Using Access Code

# Configure and Dial International Calling Using Access Code

### Download Options

Updated: July 25, 2023

Document ID: 220632

Contents

## Contents

## Introduction

This document describes how to configure and dial International Calling using an access code.

## Prerequisites

### Requirements

A full admin with access to admin.webex.com is required to configured the settings mentioned in the document.

- Must be a Webex Calling organisation

- Must have a Webex Calling Plan configured

### Components Used

This document is not restricted to specific hardware or software versions. The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

To configure for international Calling using authorization code, these steps are to be performed.

1. Log in to admin.webex.com and navigate to Locations. Choose the location for which you want to enable International Calling.

2. Scroll down to Call handling permissions and select Outgoing Call Permissions.

3. Under this option, navigate to International Calling, under the drop down choose the options that better suit the needs of the organization.

4. Choosing Allow, automatically allow all the dialed International Calls.

### Using Authorization Codes for International Calling

When you choose the option require authorization code, additional steps are to be completed.

1. Select Manage authorization code under the section Authorization Code, add  the  code for the users to use while dialing internationally. Example Description > Call to Africa Code > 1234

The code can be 2-6 numbers.

## Verify

To verify if the configuration is working and users are able to dial internationally using the authorization code.

- First dial the international number.

- An audio is played to Input the authorization code, followed by the # key.

- Users are requested to enter the same authorization code configured by the admin. A second audio is played letting you know if the audio code is accepted or not authorization code is accepted.

- Once accepted,the ringer to establish the call is played.

## Troubleshoot

To troubleshoot:

1) If the authorization code is not accepted. > Please contact the admin to provide you with the correct code

> Request the admin to delete the old code and re-add a new one

2) International calls are failing

> The most common reason for this failure is because the call is set to Block under outgoing calling permissions.

### Revision History

1.0

26-Jul-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Jul-2023 | Initial Release |