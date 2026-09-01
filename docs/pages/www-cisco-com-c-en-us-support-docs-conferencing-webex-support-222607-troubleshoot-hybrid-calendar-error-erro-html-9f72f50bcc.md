---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-support-222607-troubleshoot-hybrid-calendar-error-erro-html-9f72f50bcc
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-support/222607-troubleshoot-hybrid-calendar-error-erro.html
retrieved_at: 2026-09-01T14:57:11.222036+00:00
---

Troubleshoot Hybrid Calendar error "Error validating specified account with the organizations verified domains."

# Troubleshoot Hybrid Calendar error "Error validating specified account with the organizations verified domains."

### Download Options

Updated: November 21, 2024

Document ID: 222607

Contents

## Contents

## Introduction

This document describes error resolution and root cause analysis enable Scheduling Account with Hybrid Calendar for Cloud devices in Control Hub.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Webex Organization.

- Webex Hybrid Calendar (Google or Microsoft 365).

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Control Hub build 20240919-84b27c9

- Hybrid Calendar with Microsoft 365

- Chrome browser 129.0.6668.58 (Official Build) (arm64)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

This document describes how to identify root cause and resolve errors while enabling Scheduling Account for Hybrid Calendar with either Google or Microsoft 365 for Cloud devices in Control Hub .

Enabling Scheduling Account for Hybrid Calendar requires an email address to use as the organizer for meetings scheduled from Workspaces .

## Control Hub error

Navigate to Control Hub > Services > Hybrid > Hybrid Calendar (Microsoft 365)  > Edit settings > Tenant Details > Scheduling Account , add an email address, and click Save .

This error is shown " Error validating specified account with the organization’s verified domains. "

Control Hub error

## Gathering logs

### Control Hub

Open a new browser session in incognito mode.

If using Chrome, open DevTools > Network ; for FireFox, open Web Developer Tools > Network .

Navigate to Control Hub > Services > Hybrid > Hybrid Calendar (Microsoft 365)  > Edit settings > Tenant Details > Scheduling Account , add an email address, and click Save .

HAR file

### HTTP Error Message

```
{message: "schedulingAccount not verified in Org's domains",…}
errors: [{description: "schedulingAccount not verified in Org's domains"}]
message: "schedulingAccount not verified in Org's domains"
trackingId: "ATLAS_5480b17c-9211-4ddf-9b1b-89bbfacd32fb_3"
```

## Root Cause

Scheduling Account requires tenant domain to be verified or claimed in Control Hub .

## Solution

Navigate to Control Hub > Management > Organization Settings > Domains . Verify or Claim domain use to configure Scheduling Account .

Claim Domain

Navigate to Control Hub > Services > Hybrid > Hybrid Calendar (Microsoft 365)  > Edit settings > Tenant Details > Scheduling Account . Add an email address and click Save . A 200 API response confirms the change.

Error fixed

### HTTP Message

```
Successfully updated the Calendar Scheduling account.
```

Scheduling Account is now enabled.

## Related Information

- Enable room booking for shared mode Board and Room Series devices

- Manage your domains

- Enable and configure Hybrid Calendar with Microsoft 365

Chrome DevTools

Firefox DevTools

### Revision History

1.0

21-Nov-2024

Initial Release

### Contributed by Cisco Engineers

Josue Jonathan Vizcaino Huape

Technical Consulting Engineer

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Nov-2024 | Initial Release |