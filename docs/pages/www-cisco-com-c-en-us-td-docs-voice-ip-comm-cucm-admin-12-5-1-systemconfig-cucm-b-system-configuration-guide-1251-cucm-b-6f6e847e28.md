---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-6f6e847e28
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01000101.html
retrieved_at: 2026-08-16T17:36:32.315563+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Update Device Defaults

## Chapter: Update Device Defaults

# Update Device Defaults

## Device Defaults Overview

Each device that registers with a Cisco Unified Communications Manager node is configured with the  defaults for that type of device. Device defaults are applied to all auto-registering devices
                              in the cluster. After registration, you can change the device's configuration.

You cannot create new device defaults or delete existing ones, but you can change the default settings that get applied to
                              devices that auto-register.

Device load

Device pool

Phone button template

Installing a Cisco Unified Communications Manager automatically sets device defaults.

## Update Device Defaults Task Flow

Update Device Default Settings

You can change the default settings that are applied to  devices that  auto-register with a Cisco Unified Communications Manager node. Each type of device has a specific set of defaults.

### Update Device Default Settings

#### Before you begin

Before updating the device default settings, perform any of the following tasks that apply to your system.

Add new firmware files for the devices to the TFTP server.

If you use device defaults to assign a firmware load that does not exist in the directory, those devices will fail to load
                                       the assigned firmware.

Configure new device pools. If the device is a phone, configure new phone templates.

Step 1

In Cisco Unified CM Administration, select Device > Device Settings > Device Defaults .

Step 2

In the Device Defaults Configuration window, modify the applicable settings for the type of device that you want to update, then click Save . For field descriptions, see the online help.

Load Information

Device Pool

Phone Template

Step 3

Click the Reset icon that appears to the left of the device name to reset all the devices of that type and load the new defaults to all devices
                                          of that type on all nodes in the cluster.

If you do not reset all devices, then only new devices that auto-register on the node are configured with  the updated default
                                             values.

#### Device Defaults Settings

Field Name

Description

Device Type

This field displays the type of device to which the defaults apply.

Protocol

This field displays the protocol that is used for this type of  device.

Load Information

Enter the ID number of the firmware load that is used with a particular type of hardware device. If you install an upgrade
                                                or patch load, you must update the load information for each type of device that uses the new load.

Device Pool

Choose the device pool to associate with each type of device. The device pool defines common characteristics for all devices
                                                in the pool.

Phone Template

Choose the phone button template that each type of Cisco IP Phone uses. The template defines the function of the keys on the
                                                phone.

| Command or Action | Purpose |
|---|---|
| Update Device Default Settings | You can change the default settings that are applied to  devices that  auto-register with a Cisco Unified Communications Manager node. Each type of device has a specific set of defaults. |

| Step 1 | In Cisco Unified CM Administration, select Device > Device Settings > Device Defaults . |
|---|---|
| Step 2 | In the Device Defaults Configuration window, modify the applicable settings for the type of device that you want to update, then click Save . For field descriptions, see the online help. Load Information Device Pool Phone Template |
| Step 3 | Click the Reset icon that appears to the left of the device name to reset all the devices of that type and load the new defaults to all devices
                                          of that type on all nodes in the cluster. If you do not reset all devices, then only new devices that auto-register on the node are configured with  the updated default
                                             values. |

| Field Name | Description |
|---|---|
| Device Type | This field displays the type of device to which the defaults apply. |
| Protocol | This field displays the protocol that is used for this type of  device. |
| Load Information | Enter the ID number of the firmware load that is used with a particular type of hardware device. If you install an upgrade
                                                or patch load, you must update the load information for each type of device that uses the new load. |
| Device Pool | Choose the device pool to associate with each type of device. The device pool defines common characteristics for all devices
                                                in the pool. |
| Phone Template | Choose the phone button template that each type of Cisco IP Phone uses. The template defines the function of the keys on the
                                                phone. |