---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-116446-technote-product-00-html-48e8741869
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/116446-technote-product-00.html
retrieved_at: 2026-08-21T07:00:14.969495+00:00
---

Jabber for Windows Phone-Only Mode Feature Overview and Installation Tips

# Jabber for Windows Phone-Only Mode Feature Overview and Installation Tips

### Download Options

Updated: August 26, 2013

Document ID: 116446

Contents

## Contents

## Introduction

This document describes a new phone-only mode feature introduced in Cisco Jabber for Windows Version 9.2.1 and describes the installation procedures used in order to deploy clients in phone-only mode.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Jabber for Windows

- Cisco Unified Communication Manager (CUCM)

- Cisco Unified Presence Server (CUPS)

### Components Used

The information in this document is based on Cisco Jabber for Windows Version 9.2.1.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Phone-Only Mode Feature Overview

With Cisco Jabber for Windows Version 9.2.1, you now have the ability to deploy the client in phone-only mode, where the client authenticates directly with CUCM. In this mode, you are provisioned with audio or video capabilities without the functionality of presence or instant messaging (IM). Therefore, it is important to have the ability to determine when the Jabber client is deployed in phone-only mode, and to understand the features that are affected as well as the process used in order to restore full IM functionality.

Note : With Versions 9.2(2) and later, Jabber for Windows does not support meeting integration with phone-only mode.

## Deploy Jabber for Windows in Phone-Only Mode

In order to deploy Jabber for Windows in phone-only mode, you must install it via bootstrap with the these CLI commands:

```
msiexec.exe /i CiscoJabberSetup.msi CLEAR=1 PRODUCT_MODE=Phone_Mode TFTP=1.2.3.4 LANGUAGE=1033 /quiet
```

```
msiexec.exe /i CiscoJabberSetup.msi CLEAR=1 TYPE=WebEx SSO_ORG_DOMAIN=domain.com /quiet
```

Here are some imporatant notes to keep in mind:

- CLEAR=1 - Deletes any bootstrap files that exist.

- TYPE=WebEx - Specifies Cisco Webex Messenger as the presence server.

- SSO_ORG_DOMAIN=domain.com - Specifies domain.com as the domain name for Single Sign On (SSO).

- /quiet - Specifies a silent installation.

Tip : For additional information on installation commands for deployment, reference the Cisco Jabber for Windows 9.2.x Installation and Configuration Guide .

## Phone-Only Mode Verification

There are two methods used in order to determine if Jabber for Windows is currently deployed in phone-only mode: a visual inspection of connection settings, or a search of the Jabber problem report logs.

### Visual Inspection of Connection Settings

In the image to the left, Jabber is in full Unified Communications (UC) IM and Presence mode. You can select the Server type , and enter login information for the server.

In the image to the right, Jabber is in phone-only mode, and there are only Phone settings available.

### Search Jabber Problem Report Logs

When you search the problem report logs, you see a line that indicates there is a bootstrap file with a ProductMode value of Phone_Mode . This indicates that the client comes online in phone-only mode.

## Restore Full UC IM and Presence to Jabber

Complete these steps in order to restore full UC IM and Presence to Jabber for Windows:

- Navigate to Windows > Cisco Systems > Cisco Jabber .

- Open the ProgramData folder.

- Open the jabber-bootstrap file in Notepad.

- Delete the ProductMode: Phone_Mode line, and save the file.

- Exit the system and restart the client. Jabber for Windows is now in full UC IM and Presence mode.

Note : For additional information about phone-only mode, reference the Cisco Jabber for Windows 9.2.1 Release Notes .