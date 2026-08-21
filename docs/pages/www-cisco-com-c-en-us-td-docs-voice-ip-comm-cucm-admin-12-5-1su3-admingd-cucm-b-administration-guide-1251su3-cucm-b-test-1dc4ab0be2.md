---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-admingd-cucm-b-administration-guide-1251su3-cucm-b-test-1dc4ab0be2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/adminGd/cucm_b_administration-guide-1251su3/cucm_b_test-adminguide_chapter_0111.html
retrieved_at: 2026-08-21T16:03:33.231386+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: April 8, 2025

Chapter: Manage Infrastructure Devices

## Chapter: Manage Infrastructure Devices

# Manage Infrastructure Devices

## Manage Infrastructure Overview

This chapter provides tasks to manage network infrastructure devices such as switches and wireless access points as a part
                              of the Location Awareness feature. When Location Awareness is enabled, the Cisco Unified Communications Manager database saves
                              status information for the switches and access points in your  network, including the list of endpoints that currently associate
                              to each switch or access point.

The endpoint to infrastructure device mapping helps Cisco Unified Communications Manager and Cisco Emergency Responder to
                              determine the physical location of a caller. For example,  if a mobile client places an emergency call while in a roaming
                              situation, Cisco Emergency Responder uses the mapping to determine where to send emergency services.

The Infrastructure information that gets stored in the database also helps you to monitor your infrastructure usage. From
                              the  Unified Communications Manager interface, you can view network infrastructure devices such as switches and wireless access
                              points. You can also see the list of endpoints that currently associate to a specific access point or switch. If infrastructure
                              devices are not being used, you can deactivate infrastructure devices from tracking.

## Manage Infrastructure Prerequisites

You must configure the Location Awareness feature before you can manage wireless infrastructure within the Cisco Unified Communications
                              Manager interface. For your wired infrastructure, the feature is enabled by default.

For configuration details, see "Configure Location Awareness" chapter in the Feature Configuration Guide for Cisco Unified Communications Manager .

You must also install your network infrastructure. For details, see the hardware documentation that comes with your infrastructure
                              devices such as wireless LAN controllers, Access Points, and Switches.

## Manage Infrastructure Task Flow

Complete the following tasks to monitor and manage your network infrastructure devices.

Step 1

View Status for Infrastructure Device

Get the current status of a wireless access point or ethernet switch, including the list of associated endpoints.

Step 2

Deactivate Tracking for Infrastructure Device

If you have a switch or access point that is not being used, mark the device inactive. The system will stop updating the status
                                          or the list of associated endpoints for the infrastructure device.

Step 3

Activate Tracking for Deactivated Infrastructure Devices

Initiate tracking for an inactive infrastructure device.  Cisco Unified Communications Manager begins updating the database
                                          with the status and the list of associated endpoints for the infrastructure device.

### View Status for Infrastructure Device

Use this procedure to get the current status of an infrastructure device such as a wireless access point or an ethernet switch.
                                 Within the Cisco Unified Communications Manager interface, you can view the status for an access point or switch and see the
                                 current list of associated endpoints.

Step 1

In Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Switches and Access Points .

Step 2

Click Find .

Step 3

Click on the switch or access point for which you want the status.

### Deactivate Tracking for Infrastructure Device

Use this procedure to remove tracking for a specific infrastructure device such as a switch or access point. You may want
                                 to do this for switches or access points that are not being used.

Step 1

In Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Switches and Access Points .

Step 2

Click Find and select the switch or access point that you want to stop tracking.

Step 3

Click Deactivate Selected .

### Activate Tracking for Deactivated Infrastructure Devices

Use this procedure to initiate  tracking for an inactive infrastructure device that has been deactivated. Once the switch
                                 or access point becomes active, Cisco Unified Communications Manager begins to dynamically  track the status, including the
                                 list of endpoints that associate to the switch or access point.

#### Before you begin

Location Awareness must be configured. For details, see the "Location Awareness" chapter of the System Configuration Guide for Cisco Unified Communications Manager .

Step 1

In Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Switches and Access Points .

Step 2

From Related Links , choose Inactive Switches and Access Points and click Go .

Step 3

Select the switch or access point for which you want to initiate tracking.

Step 4

Click Reactivate Selected .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | View Status for Infrastructure Device | Get the current status of a wireless access point or ethernet switch, including the list of associated endpoints. |
| Step 2 | Deactivate Tracking for Infrastructure Device | If you have a switch or access point that is not being used, mark the device inactive. The system will stop updating the status
                                          or the list of associated endpoints for the infrastructure device. |
| Step 3 | Activate Tracking for Deactivated Infrastructure Devices | Initiate tracking for an inactive infrastructure device.  Cisco Unified Communications Manager begins updating the database
                                          with the status and the list of associated endpoints for the infrastructure device. |

| Step 1 | In Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Switches and Access Points . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Click on the switch or access point for which you want the status. The Switches and Access Point Configuration window displays the current status including the list of endpoints that currently associate to that access point or switch. |

| Note | If you remove tracking for an infrastructure device, the device remains in the database, but becomes inactive.  Cisco Unified
                                          Communications Manager no longer updates the status for the device, including the list of endpoints that associate to the
                                          infrastructure device. You can view your inactive switches and access points from the Related Links drop-down in the Switches and Access Points window. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Switches and Access Points . |
|---|---|
| Step 2 | Click Find and select the switch or access point that you want to stop tracking. |
| Step 3 | Click Deactivate Selected . |

| Step 1 | In Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Switches and Access Points . |
|---|---|
| Step 2 | From Related Links , choose Inactive Switches and Access Points and click Go . The Find and List Inactive Switches and Access Points window displays  infrastructure devices that are not being tracked. |
| Step 3 | Select the switch or access point for which you want to initiate tracking. |
| Step 4 | Click Reactivate Selected . |