---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-220390-troubleshoot-single-sign-on-admin-self-r-html-fa526c467b
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/220390-troubleshoot-single-sign-on-admin-self-r.html
retrieved_at: 2026-08-16T22:06:07.905386+00:00
---

Troubleshoot Single Sign-On Admin Self Recovery Option

# Troubleshoot Single Sign-On Admin Self Recovery Option

### Download Options

Updated: April 14, 2023

Document ID: 220390

Contents

## Contents

## Introduction

This document describes the Admin Self recovery for Control Hub if Single Sign-On does not work.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Control Hub.

- Single Sign-On.

### Components Used

The information in this document is based on these software and hardware versions:

- Azure AD ldP.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

Previously when an Administrator had a failed log in with Single Sign-On when the ldP or SP certificate expires or if there is an outage for misconfiguration, a user was required to contact Cisco TAC to disable Single SIgn-On from the backend to repair the configuration.

The Self Recovery option allows users to update or disable Single Sign-On with a secure backdoor API.

## Log In Error

Single Sign-On compromised: unable to access admin.webex.com or Webex app.

Error

## Single Sign-On bypass

Preferably on an incognito browser tab, go to admin.webex.com/manage-sso and enter the admin email.

Login

Select Send One Time Password .

Login 2

A One Time Password PIN sent from webex_comm@webex.com

Login 3

Enter the one-time PIN received and click the Sign In button.

Login 4

In the SSO Recovery Option choose Option 1: disable SSO or Option 2: update certificate and download metadata as needed.

Login 5

### Option 1

Select the toggle Modify your organization's SSO authentication .

Option 1

Confirm action and select the Deactivate button.

Option 1 - 2

Single Sign-On is successfully disabled and basic Webex authentication is in place.

### Option 2

Choose a Certificate and upload updated ldP Metadata file.

Option 2

Click Test SSO setup button.

Option 2 - 2

Once Single Sign-On succeeds, it is safe to Sign Out from the Manage-SSO portal.

Option 2 - 3

## Related Information

Single Sign-On Integration in Control Hub

Manage Single Sign-On integration in Control Hub

### Revision History

1.0

14-Apr-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 14-Apr-2023 | Initial Release |