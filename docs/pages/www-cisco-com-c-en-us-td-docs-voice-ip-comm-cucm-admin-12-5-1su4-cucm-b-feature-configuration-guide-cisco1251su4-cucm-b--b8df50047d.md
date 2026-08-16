---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-feature-configuration-guide-cisco1251su4-cucm-b--b8df50047d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_feature-configuration-guide-cisco1251su4/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0111.html
retrieved_at: 2026-08-16T16:57:34.797578+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: July 31, 2025

Chapter: Wireless LAN

## Chapter: Wireless LAN

# Wireless LAN

## Wireless LAN Overview

This feature removes the need for users to configure WiFi parameters on their phones. You can configure WiFi profiles for
                              them. Devices can then automatically download and apply the WiFi configuration from your system. You can configure a network
                              access profile, which contains further security layers that are related to VPN connectivity and HTTP proxy settings.

## Wireless LAN
                        	 Configuration Task Flow

Step 1

Generate a Phone Feature List

Generate a
                                          				report to identify devices that wireless LAN profiles.

Step 2

Configure a Network Access Profile

Optional: Configure a network access profile if you want to configure VPN and HTTP proxy settings that you can link to a wireless LAN
                                          profile.

Step 3

Configure a Wireless LAN Profile

Configure a wireless LAN profile with common WiFi settings to apply to devices or device pools in the enterprise.

Step 4

Configure a Wireless LAN Profile Group

Group wireless
                                          				LAN profiles together.

Step 5

To Link a Wireless LAN Profile Group to a Device or Device Pool ,
                                       			 perform one of the following subtasks:

- Link a Wireless LAN Profile Group to a Device

- Link a Wireless LAN Profile Group to a Device Pool

After you complete the device link, TFTP adds the wireless LAN profile group to the existing device configuration file, which
                                          the device (or devices that are tied to a device pool) proceeds to download.

### Configure a Network Access Profile

Configure a network access profile if you want to configure VPN and HTTP proxy settings that you can link to a wireless LAN
                                 profile.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Network Access Profile

Step 2

Click Add New .

Step 3

Configure the fields in the Network Access Profile Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

### Configure a Wireless LAN Profile

Configure a wireless LAN profile with common WiFi settings to apply to devices or device pools in enterprise.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Wireless LAN Profile

Step 2

Click Add New .

Step 3

Configure the fields in the Wireless LAN Profile Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

### Configure a Wireless LAN Profile Group

Group your wireless LAN profiles.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Wireless LAN Profile Group .

Step 2

Click Add New .

Step 3

Configure the fields in the Wireless LAN Profile Group Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

### Link a Wireless LAN Profile Group to a Device or Device Pool

After you complete the device link, TFTP adds the wireless LAN profile group to the existing device configuration file, which
                                 the device (or devices tied to a device pool) proceeds to download.

Step 1

Link a Wireless LAN Profile Group to a Device

Step 2

Link a Wireless LAN Profile Group to a Device Pool

#### Link a Wireless
                              	 LAN Profile Group to a Device

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Perform one of
                                             			 the following tasks:

- Click Find to enter search criteria and choose an existing device from the resulting list.

- Click Add New , and choose the device type from the Phone Type drop-down list.

Step 3

From the Wireless LAN Profile Group drop-down list, choose a
                                             			 wireless LAN profile group that you created.

Step 4

Click Save .

#### Link a Wireless LAN Profile Group to a  Device Pool

If you link a wireless LAN profile group at the device and device pool level, your system uses the device pool setting.

Step 1

From Cisco Unified CM Administration, choose System > Device Pool .

Step 2

Perform one of the following tasks:

- Click Find to enter search criteria and choose an existing device pool from the resulting list.

- Click Add New .

Step 3

From the Wireless LAN Profile Group drop-down list, choose a wireless LAN profile group that you created.

Step 4

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Generate a
                                          				report to identify devices that wireless LAN profiles. |
| Step 2 | Configure a Network Access Profile | Optional: Configure a network access profile if you want to configure VPN and HTTP proxy settings that you can link to a wireless LAN
                                          profile. |
| Step 3 | Configure a Wireless LAN Profile | Configure a wireless LAN profile with common WiFi settings to apply to devices or device pools in the enterprise. |
| Step 4 | Configure a Wireless LAN Profile Group | Group wireless
                                          				LAN profiles together. |
| Step 5 | To Link a Wireless LAN Profile Group to a Device or Device Pool ,
                                       			 perform one of the following subtasks: Link a Wireless LAN Profile Group to a Device Link a Wireless LAN Profile Group to a Device Pool | After you complete the device link, TFTP adds the wireless LAN profile group to the existing device configuration file, which
                                          the device (or devices that are tied to a device pool) proceeds to download. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Network Access Profile |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Configure the fields in the Network Access Profile Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Wireless LAN Profile |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Configure the fields in the Wireless LAN Profile Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Wireless LAN Profile Group . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Configure the fields in the Wireless LAN Profile Group Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Link a Wireless LAN Profile Group to a Device |  |
| Step 2 | Link a Wireless LAN Profile Group to a Device Pool |  |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Perform one of
                                             			 the following tasks: Click Find to enter search criteria and choose an existing device from the resulting list. Click Add New , and choose the device type from the Phone Type drop-down list. |
| Step 3 | From the Wireless LAN Profile Group drop-down list, choose a
                                             			 wireless LAN profile group that you created. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Device Pool . |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to enter search criteria and choose an existing device pool from the resulting list. Click Add New . |
| Step 3 | From the Wireless LAN Profile Group drop-down list, choose a wireless LAN profile group that you created. |
| Step 4 | Click Save . |