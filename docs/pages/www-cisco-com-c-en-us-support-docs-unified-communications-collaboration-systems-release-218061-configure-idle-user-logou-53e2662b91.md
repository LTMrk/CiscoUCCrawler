---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-collaboration-systems-release-218061-configure-idle-user-logou-53e2662b91
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/collaboration-systems-release/218061-configure-idle-user-logout-timer-in-epnm.html
retrieved_at: 2026-08-16T18:27:55.167523+00:00
---

Configure Idle User Logout Timer in EPNM GUI

# Configure Idle User Logout Timer in EPNM GUI

### Download Options

Updated: August 19, 2022

Document ID: 218061

Contents

## Contents

## Introduction

This document describes the steps to change the idle user logout timer in Evolved Programmable Network Manager (EPNM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of EPN Manager.

Note : Need to have access to EPNM GUI.

### Components Used

The information in this document is based on EPNM.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

You must make this change at two levels (System Level and User Level).

### System Level

Navigate to Administration > Setting > System Settings. Under General, select Server and change the timeout value as shown in this image:

### User Level

Click the Settings icon on the top right and select My Preferences.

Change the timeout value as desired and click Save.

Log out and log back in for the changes to take effect.

### Revision History

1.0

23-Aug-2022

Initial Release

### Contributed by Cisco Engineers

Sancho Felix

### This Document Applies to These Products

- Collaboration Systems Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Aug-2022 | Initial Release |