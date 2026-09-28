---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-app-223105-ascertain-if-users-can-use-unmanaged-html-78698b1d74
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-app/223105-ascertain-if-users-can-use-unmanaged.html
retrieved_at: 2026-08-16T22:05:38.723163+00:00
---

Ascertain if Users Can Use Unmanaged Version of Webex App

# Ascertain if Users Can Use Unmanaged Version of Webex App

### Download Options

Updated: June 17, 2025

Document ID: 223105

Contents

## Contents

## Introduction

This document describes identifying if users belonging to a particular Webex org can use the unmanaged version of Webex app or not.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Control Hub

- Webex App

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Control Hub

- Webex App version 44.2.0.145

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document describes identifying if users belonging to a particular Webex org are able to use the unmanaged version of Webex app or not. While trying to log in to the Webex mobile application, you receive the error "You will automatically be signed out of the app shortly. App Management required. The application requires a managed device policy check to continue. Please install a Work Profile and try again".

The issue persists even after re-installing the Webex app.

Error Received on Webex App

## Troubleshooting Steps

- Validate if you are able to successfully log in to the Webex desktop application and the issue only occurs on mobile devices.

2. Navigate to Control Hub > Services > Messages .

3. Scroll down and search for Mobile Application Security .

4. Corresponding to Mobile Application Security , validate if Disable use of unmanaged app is checked or not.

Mobile Application Security Snippet From Control Hub

5. If Disable use of unmanaged app is checked, it confirms that your organization blocks the use of unmanaged apps and you cannot use the unmanaged app. You are required to use a corporate managed version of Webex. This is a global setting for the organization.

6. It is a good idea to also test if the Webex mobile application works by installing it in a Work profile.

## Root Cause

The root cause behind the error received on the mobile Webex app, is due to the setting Disable use of unmanaged app being checked on Control Hub.

This feature is available with Pro Pack for Control Hub. More information on the same is outlined here .

## Solution

In this case, the user's organization is using Microsoft Intune to manage Webex application however, the user installed Webex app through App Store/Google Play. The unmanaged version of Webex mobile application is uninstalled and subsequently, Webex Intune app is installed which resolves the issue.

Webex Intune is considered to be a managed app and no app config key is required.

Disable the Use of Unmanaged App

## Related Information

- Enable Security Settings For Mobile Versions of Webex App

- Webex App Secure Mobile Devices

- Webex App Installation With Microsoft Intune

### Revision History

1.0

17-Jun-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Jun-2025 | Initial Release |