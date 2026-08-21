---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-222698-troubleshoot-saml-response-error-in-dire-html-0c66ff09a1
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/222698-troubleshoot-saml-response-error-in-dire.html
retrieved_at: 2026-08-21T06:32:35.351445+00:00
---

Troubleshoot SAML Response Error in Directory Connector.

# Troubleshoot SAML Response Error in Directory Connector.

### Download Options

Updated: January 16, 2025

Document ID: 222698

Contents

## Contents

## Introduction

This document describes troubleshooting error "Submit SAML response Data/Cannot connect securely to this page" while Cisco Directory Connector login.

## Prerequisites

### Requirement

Cisco recommends that you have knowledge of these topics:

- Cisco Directory Connector

- Webex Control Hub

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Directory Connector application on version 3.8.2000.64687

- Webex Control Hub

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

This document describes how to troubleshoot "Submit SAML response Data/Cannot connect securely to this page error", while trying to launch the Cisco Directory Connector application. After entering the email ID, the erroris presented.

Clicking the error message displays a blank page and it does not move past that.

## Troubleshooting Steps

- Ensure you are able to log in to Control Hub using the same admin credentials (which are being used for Cisco Directory Connector application) using a web browser on the same server/desktop where Directory Connector application is running.

- If the log in works from the web browser on the same server however, the log in still does not work for Cisco Directory Connector application, then it could point to an issue with the Directory Connector application itself.

- It is a good practice to check if the application is running the latest version. If not, kindly check for available updates and ensure that the update is installed.

- Reproduce the issue and collect Event Viewer logs .

## Logs Analysis

These warnings and information messages can be seen in the Event Viewer logs:

```
The operation cannot be performed on an offline library. [sessionId: ] [DirSyncWorker DSWorker] DirSyncService waiting to be configured The operation completed successfully 2023-12-14 14:20:58,515 [1] WARN Cisco.CoDev.Identity.DirSync.Update.Lib.UpdateUtil [(null)] - Failed to save the update status. Error: An error occurred loading a configuration file: Access to the path 'C:\Program Files (x86)\Cisco Systems\Cisco Directory Connector\vyh34ft3.tmp' is denied. (C:\Program Files (x86)\Cisco Systems\Cisco Directory Connector\CloudConnectorCommon.dll.config) Trace: at System.Configuration.MgmtConfigurationRecord.SaveAs(String filename, ConfigurationSaveMode saveMode, Boolean forceUpdateAll) at Cisco.CoDev.Identity.DirSync.Update.Lib.UpdateUtil.SaveUpgradeStatus(Boolean hasUpgraded)
```

These events are also seen in the logs:

```
[sessionId: ] [DirSyncWorker DirSyncWorker] 1 DirSync Plugin(s) Loaded. [sessionId: ] [DirSyncWorker DirSyncWorker] Started DirSyncService version 3.8.2000.64687
```

```
The operation cannot be performed on an offline library. [sessionId: ] [DirSyncWorker DSWorker] DirSyncService waiting to be configured
```

```
Cannot create another system semaphore. [sessionId: ] [ CheckWebView2Supported] WebView2 runtime not being installed
```

Errors related to WebView2 are seen in the Event Viewer logs , as shown above. These log lines also indicate the same error:

```
- <System> <Provider Name=" Cisco Directory Connector - Manager" /> <EventID Qualifiers="0">100</EventID> <Version>0</Version> <Level>4</Level> <Task>0</Task> <Opcode>0</Opcode> <Keywords>0x80000000000000</Keywords> <TimeCreated SystemTime="2023-12-14T03:24:03.4691316Z" /> <EventRecordID>106</EventRecordID> <Correlation /> <Execution ProcessID="0" ThreadID="0" /> <Channel>Cisco Directory Connector</Channel> <Security /> </System> - <EventData> <Data>[sessionId: ] [ CheckWebView2Supported] WebView2 runtime not being installed </Data> </EventData> </Event>
```

## Root Cause

WebView2 runtime is required to be installed on the system running the Cisco Directory Connector Application. The logs clearly indicate WebView2 runtime not installed on the system.

## Solution

Install the WebView2 Evergreen Bootstrapper on the server running the Cisco Directory Connector Application. It can be downloaded from this link .

After installing the WebView2 Evergreen Bootstrapper , please exit the Cisco Directory Connector Application(from the up arrow found at the bottom of the desktop) and then re-run the Cisco Directory Connector Application as an admin and try signing in again.

This resolves the issue.

## Related Information

- Deployment Guide for Directory Connector

- Directory Connector Release Notes

### Revision History

1.0

16-Jan-2025

Initial Release

### Contributed by Cisco Engineers

Jagatbir Singh Jaijee

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Control Hub

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 16-Jan-2025 | Initial Release |