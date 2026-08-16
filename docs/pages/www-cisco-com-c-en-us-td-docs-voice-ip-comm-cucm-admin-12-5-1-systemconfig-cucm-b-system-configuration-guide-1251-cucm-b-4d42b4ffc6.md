---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-4d42b4ffc6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01010100.html
retrieved_at: 2026-08-16T17:37:34.831633+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Automated Alternate Routing

## Chapter: Configure Automated Alternate Routing

# Configure Automated Alternate Routing

## Automated Alternate Routing Overview

Configure automated alternate routing (AAR) to
                              			 automatically reroute calls through the PSTN or other networks when the system blocks a call due to insufficient location
                              			 bandwidth. With automated alternate routing, the caller does not need to hang
                              			 up and redial the called party.

## AAR Configuration Task Flow

Step 1

Enable Clusterwide Automated Alternate Routing

Enable automated alternate routing for the cluster.

Step 2

Configure AAR Group

Configure automated alternate routing (AAR) to reroute calls through the PSTN or other network by using an alternate number
                                          when Cisco Unified Communications Manager blocks a call due to insufficient location bandwidth.

### Enable Clusterwide Automated Alternate Routing

Enable Automated Alternate Routing (AAR) for the cluster.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

Select a node in the Server drop-down box.

Step 3

From the Service drop-down list, select Cisco Call Manager.

Step 4

In the Clusterwide Parameters (System - CCM Automated Alternate Routing) area, set the Automated Alternate Routing Enable parameter to True .

### Configure AAR Group

Configure Automated Alternate Routing (AAR) to automatically reroute calls through the PSTN or other networks when the system
                                 blocks a call due to insufficient location bandwidth. With AAR, the caller does not need to hang up and redial the called
                                 party.

Step 1

From Cisco Unified CM Administration, choose Call Routing > AAR Group .

Step 2

Choose one of the following options:

- Click Add New , to add a new AAR group.

- Click Find and choose an AAR group from the resulting list, to modify the settings for an existing AAR group.

Step 3

In the Name field, enter the name that you want to assign to the new AAR group.

The name can contain up to 20 alphanumeric characters and can contain any combination of spaces, periods (.), hyphens (-),
                                             and underscore characters (_).

Step 4

Configure the fields on the AAR Group Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Clusterwide Automated Alternate Routing | Enable automated alternate routing for the cluster. |
| Step 2 | Configure AAR Group | Configure automated alternate routing (AAR) to reroute calls through the PSTN or other network by using an alternate number
                                          when Cisco Unified Communications Manager blocks a call due to insufficient location bandwidth. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | Select a node in the Server drop-down box. |
| Step 3 | From the Service drop-down list, select Cisco Call Manager. |
| Step 4 | In the Clusterwide Parameters (System - CCM Automated Alternate Routing) area, set the Automated Alternate Routing Enable parameter to True . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > AAR Group . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New , to add a new AAR group. Click Find and choose an AAR group from the resulting list, to modify the settings for an existing AAR group. The AAR Group Configuration window appears. |
| Step 3 | In the Name field, enter the name that you want to assign to the new AAR group. The name can contain up to 20 alphanumeric characters and can contain any combination of spaces, periods (.), hyphens (-),
                                             and underscore characters (_). The window refreshes and displays additional fields. |
| Step 4 | Configure the fields on the AAR Group Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . Note Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow . | Note | Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow . |
| Note | Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow . |

| Note | Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow . |
|---|---|