---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213943-manage-endpo-fe5fbd4f7c
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213943-manage-endpoints-from-pcp-without-end-us.html
retrieved_at: 2026-08-21T13:58:13.776364+00:00
---

Manage Endpoints from PCP without End User Association in CUCM

# Manage Endpoints from PCP without End User Association in CUCM

### Download Options

Updated: November 30, 2018

Document ID: 213943

Contents

## Contents

## Introduction

This document describes the procedure to assign the endpoints in Prime Collaboration Provisioning (PCP) which are not associated with the end users in Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have basic knowledge of PCP.

### Components Used

The information in this document is based on these software and hardware versions:

- PCP Version 12.3

- Mozilla Firefox 55.0

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

Step 1. Login to PCP and navigate to Administration > Advanced Provisioning > Manage Endpoints .

Step 2. Select the Call Processor and click on Search Endpoints Without Associated User .

Step 3. Select the required endpoint which is associated with a specific user, as shown in the image.

Step 4. Click on Assign Selected Endpoints to User .

Step 5. Associate User for the selected endpoint, as shown in the image.

Step 6. Click on Save .

## Verify

Here are the steps to verify that the endpoint is associated with the user successfully.

### From Prime Collaboration Provisioning

- Under User Provisioning , click on Add and check the box with the user who is associated with the endpoint.

- Under Actions , click on the Synchronize User .

Confirm that the endpoint is associated

### From CallManager

Step 1. Login to the CallManager administrator page.

- Navigate to User Management > End User .

- Search for the end user and click on the User ID.

- Check the device information and confirm that the Endpoint is under controlled devices.

Step 2. Navigate to Device > Phone .

- Search for the endpoint and click on it.

- Under Device Information , confirm the Owner User ID .

## Troubleshoot

From PCP 12.X, there is no access to CLI/SSH as root.

If any issue still persists please contact the Cisco Technical Assistance Center (TAC).

## Related Information

- Cisco Prime Collaboration Provisioning

- Collect ShowTech Logs from the GUI of Prime Collaboration Provisioning

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

29-Nov-2018

Initial Release

### Contributed by Cisco Engineers

Abhishek Tomar

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 29-Nov-2018 | Initial Release |