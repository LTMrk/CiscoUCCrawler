---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-217563-enable-jabber-log-in-for-cucm-local-user-61a442f581
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/217563-enable-jabber-log-in-for-cucm-local-user.html
retrieved_at: 2026-08-21T06:57:18.983483+00:00
---

Enable Jabber Log in for CUCM Local Users in an SSO Environment

# Enable Jabber Log in for CUCM Local Users in an SSO Environment

### Download Options

Updated: November 17, 2021

Document ID: 217563

Contents

## Contents

## Introduction

This document describes what actions to take to enable Cisco Unified Call Manager (CUCM) local end-users (not Lightweight Directory Access Protocol ( LDAP) synced) to log into Jabber in a Single Sign-On (SSO) enabled cluster.

Applies for Jabber for Windows only.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager

- Single Sign-On (SSO)

- Cisco Jabber

- Windows Command Prompt (CMD)

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Solution

Previously, the SSO_Enabled Jabber Parameter was available to be used under the Jabber configuration file ( jabber-config.xml ) to disable the SSO feature for specific users via the Cisco Support Field within the Jabber device configuration under the CUCM, but this parameter has been deprecated since March 2021, refer to the Parameter reference guide for Jabber 12.9.

The only workaround consists of completely disable the SSO feature in the local computer client via the CMD install switch:

msiexec.exe /i CiscoJabberSetup.msi CLEAR=1 SSO_ENABLED=FALSE

Alternatively, the Jabber Bootstrap file (jabber-bootstrap.properties) located in C:\ProgramData\Cisco Systems\Cisco Jabber can be manually modified (line 28) as shown here:

```
NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED SSO_Enabled: FALSE NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED EnableDPIAware: TRUE NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED STARTUP_AUTHENTICATION_REQUIRED: FALSE NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED NOT_SPECIFIED UXModel: Modern NOT_SPECIFIED
```

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

2.0

17-Nov-2021

Initial Release

1.0

17-Nov-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 17-Nov-2021 | Initial Release |
| 1.0 | 17-Nov-2021 | Initial Release |