---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-webex-desk-pro-217223-collaboration-endpoint-file-is-too-larg-5a092aa9af
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/webex-desk-pro/217223-collaboration-endpoint-file-is-too-larg.html
retrieved_at: 2026-08-21T12:39:21.672545+00:00
---

Collaboration Endpoint "File is too large" Upgrade Error

# Collaboration Endpoint "File is too large" Upgrade Error

### Download Options

Updated: June 30, 2021

Document ID: 217223

Contents

## Contents

## Introduction

This document describes the details about the Cisco Collaboration Endpoint (CE) software upgrade error “File too large”, and guides through the possible workarounds to upgrade the endpoint to the desired version.

## Problem: "File is too large" upgrade error

When you attempt to upgrade a collaboration endpoint on a software version of CE9.7 (or earlier) to a version of CE9.13 (or later) through the Graphical User Interface (GUI), the error “File too large” is observed as per the image.

File is too large

## Cause

The cause of this error is due to the software file size exceeding the 1GB limit imposed on the earlier CE versions. It is important to note that this is expected when attempting to upgrade via the web interface.

## Solution

There are two ways to work around this issue, see below:

- Upgrade the endpoint via a provisioning server CUCM or TMS.

- Step upgrade to CE9.8.2 or CE9.9.2 (or similar) and then to the desired software of CE9.13.x (or later).

### Option 1. Upgrade via CUCM or Cisco TMS

To address the issue with the upgrade procedure via a provisioning server like Cisco Unified Communication Manager (CUCM) or TelePresence Management Suite (TMS), you can find the instructions on these videos:

Video - CUCM Endpoint Upgrade

Video - TMS Endpoint Upgrade

### Option 2. Step Upgrade to CE9.8.2/CE9.9.2 then to the desired version

Upgrade the collaboration endpoint to a software version of CE9.8.2 or CE9.9.2 first and then to the desired software version. You may need to open a TAC case if the proper upgrade file is not available.

Note : This procedure includes an upgrade to a deferred software version, thus please be sure to upgrade to an officially supported software version once done with the upgrade to CE9.8.2/CE9.9.2.

Video Player is loading.

0:00

0:00

LIVE

0:00

Follow the normal upgrade procedure from CE9.8.2 or CE9.9.2 to the desired version, it is recommended to upgrade to the latest version. You can find a video on this upgrade procedure via the GUI on this link .

## Related Information

- Open a TAC Case to request access to CE9.8.2 or CE9.9.2 software versions

- Support Case Manager

### Revision History

1.0

30-Jun-2021

Initial Release

### Contributed by Cisco Engineers

Elias Sevilla Duarte

Cisco TAC Engineer

### This Document Applies to These Products

- Desk Pro

- Room Kit

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 30-Jun-2021 | Initial Release |