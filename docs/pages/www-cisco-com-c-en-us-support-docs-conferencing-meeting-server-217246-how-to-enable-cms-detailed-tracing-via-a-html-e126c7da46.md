---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-217246-how-to-enable-cms-detailed-tracing-via-a-html-e126c7da46
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/217246-how-to-enable-cms-detailed-tracing-via-a.html
retrieved_at: 2026-08-21T13:13:01.309146+00:00
---

How to Enable CMS Detailed Tracing via API

# How to Enable CMS Detailed Tracing via API

### Download Options

Updated: July 8, 2021

Document ID: 217246

Contents

## Contents

## Introduction

This document describes how to enable detailed tracing for Cisco Meeting Server (CMS) logs via Application Programing Interface (API). With this feature, the current detailed tracing available from web admin page, can now be enabled via management API as well.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CMS configuration.

- API configuration.

- Postman configuration.

### Components Used

The information in this document is based on CMS version 3.2.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

Step 1. Open CMS Graphical User Interface (GUI) and navigate to Configuration > API .

Step 2. From the list, select the parameter /api/v1/system/timedLogging .

Step 3. Select View or edit .

Step 4. Modify the desired parameter and select Modify .

Note : The timedLogging parameter corresponds to the duration of seconds for which that logging subsystem is activated. Setting a parameter to 0 or to nothing deactivates a logging subsystem.

### Configure via Postman

Step 1 . Open Postman configuration and connect to CMS.

Step 2 . Send a GET request to https://CMS-IP:8443/api/v1/system/timedLogging.

Step 3. Identify the parameter you want to change and copy the value. For example activeControl .

Step 4. Navigate to Body tab and paste the parameter copied on step 3, activeControl , into the KEY column.

Step 5. Configure the new value into Value column, and select the PUT method in order to send the request to https://CMS-IP:8443/api/v1/system/timedLogging as shown in the next image:

## Verify

Step 1. Navigate to CMS > Logs > Detailed tracing , and verify the debug is enabled.

Step 2. Once you enable the debugs, the CMS logs show the next lines:

```
Line 217707: Jul 3 15:01:22.811 user.info cms1 host:server: INFO : Active control tracing now enabled Line 217708: Jul 3 15:01:42.994 user.info cms1 host:server: INFO : BFCP tracing now enabled
```

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

08-Jul-2021

Initial Release

### Contributed by Cisco Engineers

Fernando Garrido

### This Document Applies to These Products

- Meeting Server

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 08-Jul-2021 | Initial Release |