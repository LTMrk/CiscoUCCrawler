---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-teams-218148-troubleshoot-phone-services-disconnected-ht-4964431eae
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-teams/218148-troubleshoot-phone-services-disconnected.html
retrieved_at: 2026-08-20T23:21:27.882664+00:00
---

Troubleshoot Phone Services Disconnected in Webex Teams for WxC

# Troubleshoot Phone Services Disconnected in Webex Teams for WxC

### Download Options

Updated: November 25, 2024

Document ID: 218148

Contents

## Contents

## Introduction

This document describes how to troubleshoot phone services error in Webex teams that use Webex Calling (WxC) licenses.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub (CH). Ensure you have Admin Access.

- Webex Teams

## Background Information

One of the most common issues related to Webex Teams that use Webex Calling services is that Phone Services show as Disconnected. This means your user is not registered to Webex Calling Services and you are not able to receive or make any calls until the issue is resolved. This document is focused on how to troubleshoot PC and Mobile, but you can use the same steps if you have an issue with a tablet.

How to validate if your phones services are disconnected:

- PC Mac/Windows

In your Webex teams, in the lower left corner, the message You are not signed in to phone services is shown.

Phone services disconnected

- Mobile iOs/Android

Step 1. Select the profile image on the upper left corner.

Step 2. Phone services are disconnected.

## Common Configuration Issues

### Webex Calling Licenses Assigned

Verify user has Wxc licenses assigned.

Step 1. In Control Hub, select Users .

Step 2. Select [Your-user] .

Step 3. In Profile, review the Licenses configuration. This must show Webex Calling licenses.

### Validate the Webex Calling Applications

Verify user has Webex Calling application licenses assigned.

Step 1. In Control Hub, select Users .

Step 2. Select [Your-user] .

Step 3. Select Calling Tab .

Step 4. Select Advanced Call Settings .

Step 5. Select Applications .

Step 6. Verify Webex Applications box Desktop/Mobile or Tablet is checked.

### Verify That You Have the Latest Webex Teams Version

Ensure that you have the latest version. It is recommended to reinstall the app.

Download this link for Webex Teams in your PC or reinstall the app through the App Store for your iPhone or the Play Store for your Android.

### Try to Force the Phone Services Sign In

PC Mac

Step 1. In Webex teams, in the lower left corner, see the message, You are not signed in to phone services . Select sign in .

Mobile iOS

Step 1. Select the profile image on the upper left corner.

Step 2. Select Settings .

Step 3. Select Calling .

Step 4. Select Phone Services .

Step 5. Select Sign in .

Note : WxC does not support to be registered on 2 different PC or mobile devices at the same time.

### Validate Your Network and Device

Ensure your networks meet the Webex Calling Port Reference Requirements

## What is Next

After you review these configurations, if you have any issues, open a case with TAC.

You must add this information:

- Your OrgID

- Specific email address with the problem.

- Provide the webex teams logs.

Then, these are the steps:

Webex Teams PC Mac logs

Step 1. On the top corner, select Help .

Step 2. Select Send logs .

Webex Teams PC Windows logs

Step 1. Select the profile image on the upper left corner.

Step 2. Select Help .

Step 3. Select Send logs .

Webex Teams mobile iOs/Android logs

Step 1. Select the profile image on the top left corner.

Step 2. Select Send logs .

### Revision History

3.0

25-Nov-2024

Updated Alt Text, Machine Translation, and Formatting.

2.0

23-Oct-2023

Updated Style Requirements and Formatting.

1.0

06-Sep-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 25-Nov-2024 | Updated Alt Text, Machine Translation, and Formatting. |
| 2.0 | 23-Oct-2023 | Updated Style Requirements and Formatting. |
| 1.0 | 06-Sep-2022 | Initial Release |