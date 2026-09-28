---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-15-221563-d-87b785f45f
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service-15/221563-decommission-im-and-presence-nodes.html
retrieved_at: 2026-08-16T23:36:28.922095+00:00
---

Decommission IM and Presence nodes

# Decommission IM and Presence nodes

### Download Options

Updated: January 17, 2024

Document ID: 221563

Contents

## Contents

## Introduction

This document describes the process to perform when decommissioning Cisco IM and Presence nodes.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unified Communications Manager (CUCM) and Cisco IM and Presence (IM&P).

### Components Used

The information in this document is based on the listed software versions:

- Cisco Unified Communications Manager 12.5.1 SU5

- Cisco IM and Presence 12.5.1 SU5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Decommissioning IM and Presence Nodes

### Unassign Users from IM&P

Start by logging into CUCM and navigating to Cisco Unified CM Administration > User Management > Assign Presence Users .

CUCM Assign Presence Users

From the presence user assignment configuration select the option to Assign All Users .

CUCM Assign All Users

When presented with the assign users prompt select the unassigned radio button and save.

Assign Users

Once all users have been unassigned from the IM&P servers, verify the change has occurred by logging into the IM&P administration and verifying all users show as unassigned.

IM&P Unassigned User Validation

### Remove IM&Ps from Service Profile

Navigate to Cisco Unified CM Administration > User Management > User Settings > Service Profile.

CUCM Service Profile

After selecting the service profile change the IM and Presence Profiles to <None> and Save.

Service Profile IM&P Profile

Note : Remove the IM&P nodes from all configured service profiles.

### Disable User IM Capabilities

Navigate to Cisco Unified CM Administration > Bulk Administration > Users > Update Users > Query.

CUCM Bulk Admin Update Users

Select all the user that are enabled for IM&P. When presented with the update users configuration page disable the "Enable Users for Unified CM IM and Presence" configuration and submit the changes to run immediately or at a later time.

Bulk Admin Disable IM&P

Navigate to IM&P Administration > System > Presence Topology page and verify that there are no users shown as assigned or unassigned.

IM&P All Users Unassigned

### Disable Feature Group IM Capabilities

Navigate to User Management > User/Phone Add > Feature Group Template.

CUCM Feature Group Template

Once the feature group template is selected remove the check near the "Enable User for Unified CM IM and Presence" selection and save.

Feature Group Template Disable IM&P

### Delete IM&P SIP Trunk

Navigate to Cisco Unified CM Administration > Device > Trunk.

CUCM SIP Trunk

Check the box by the IM&P SIP trunk and select the option to delete selected.

CUCM Delete SIP Trunk

### Delete the Presence Redundancy Group

Navigate to Cisco Unified CM Administration  > System > Presence Redundancy Groups.

CUCM Presence Redundancy Group

Disable high availability and save.

CUCM Disable High Availability

Next, select the option to delete the Presence Redundancy Group

CUCM Delete Presence Redundancy Group

### Delete the IM&Ps

Navigate to Cisco Unified CM Administration  > System > Server.

CUCM System Server

Select the option to delete the IM&P node.

CUCM Delete IM&P

Note : Once the IM&Ps have been decommissioned, make sure to power down and remove the virtual machines as they are no longer needed.

### Revision History

1.0

17-Jan-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Jan-2024 | Initial Release |