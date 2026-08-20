---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-220504-deploy-and-use-of-webex-call-integration-html-6cf88413aa
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/220504-deploy-and-use-of-webex-call-integration.html
retrieved_at: 2026-08-20T21:10:28.666890+00:00
---

Deploy and Use of Webex Call Integration with Microsoft Teams

# Deploy and Use of Webex Call Integration with Microsoft Teams

### Download Options

Updated: June 8, 2023

Document ID: 220504

Contents

## Contents

## Introduction

This document describes how to deploy the Webex Calling integration with Microsoft Teams and explains common issues of this deployment.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Control Hub.

- Microsoft Admin Center.

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Control Hub with Webex Calling subscription.

- Office 365 E3 licensing.

- Webex app for Windows 43.5.0.26155 (64-bit)

- Microsoft Teams for Windows 1.6.00.11166 (64-bit)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Deployment

### Teams Admin Center

To activate the Webex app, navigate to admin.teams.microsoft.com  > Teams apps > Manage apps . Search for and select the Webex Call app.

Webex Call app

In the Webex Call status setting, slide the toggle from Blocked to Allowed .

Status

Next, set the Webex Call to Allow under permission policies to make it available to users. To do so, navigate to Teams apps > Permission policies and choose the default policy or create a new one.

Permission policies

Select Third-party apps drop-down menu, then choose Allow specific apps and block all others.

Allow apps

drop-down menu

Under Add apps, select Allow apps .

Allow apps

Search for Webex Call, click Add .

Add app

Make sure Webex Call is listed in Apps to add and click Allow to return to the policy settings.

Apps to add

In the policy settings, click Save to apply the changes.

Apply changes

It can take a few hours for changes to take effect, click Confirm to acknowledge the final prompt.

Confirm button

Install Webex Call for Teams users and choose the order you want it to appear. Navigate to Teams apps > Setup policies . Choose the default policy or create a new one.

Setup policies

Locate Installed apps, click on Add apps.

Add apps

In the Add installed apps menu, search Webex Call and click Add .

Search Webex Call

Make sure Webex Call is listed in Apps to add and click Add to return to the policy settings.

Add app

Locate Pinned apps , click on Add apps button.

Add apps

In the Add installed apps menu, search Webex Call and click Add .

Search Webex Call

Make sure Webex Call is listed in Apps to add and click Add to return to the policy settings.

Add app

Webex Call  is now present in the app bar and can be move with Move up and Move down buttons. Click Save .

Pinned apps

It can take a few hours for changes to take effect, click Confirm to acknowledge the prompt and apply the change.

Confirm button

## Optional

### Disable the Built-in Calling Option and Make Webex Call the Only Option

If there are Microsoft Teams Calling plans, built-in Calling can be disabled to make Webex Call the default app. Navigate to Voice > Calling policies . Choose the default policy or create a new one. Turn Make private calls to Off , click Save to apply.

### Configure to Hide Webex App Window for Microsoft Teams users

For organizations that have chosen to use the Webex Call integration with Microsoft Teams, the integration is the users primary interface to Webex services. See References to know more.

## User Experience

### Teams App

Log into Microsoft Teams, in the default page locate the Webex Call button pinned in the left menu. Click Webex Call button.

Teams app

It is required to sign into Webex the first time you use it or whenever you sign into Teams App, you must grant permissions to search contacts and interact with Microsoft Teams once.

Sign In

Confirm user password and click Sign in .

Password

Provide a valid email address to authenticate to Webex App. This email address must match between Teams and Webex.

Webex login

PSTN number appear under My number section. Make a call available, Recent calls and Voicemail menu at the bottom.

Teams app

### Webex App

User needs to have both Teams and Webex app open.

## Known Issues

### After Enter a Number and Start Call Nothing Happen

Verify user is authenticated in Webex App.

### There is no Error Received in the Log in but still it Does not Show the Assigned Number in My number

Email address to authenticate into Webex App must match.

## Related Information

### Revision History

1.0

08-Jun-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 08-Jun-2023 | Initial Release |