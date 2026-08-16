---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-b46b6af3c6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01000111.html
retrieved_at: 2026-08-16T17:36:40.755348+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Manual Phone Registration

## Chapter: Manual Phone Registration

# Manual Phone Registration

## Manual Phone
                        	 Registration Overview

To manually register a new Cisco IP Phone, you must add the phone to the Unified Communications Manager node using Unified Communications Manager , then configure the directory number for the phone.

You should have already set up the new phone with the proxy TFTP server IP address so that the new phone knows how to locate
                              the Unified Communications Manager node. See the Cisco IP Phone Administration Guide for your phone series.

## Manual Device Registration Task Flow

Step 1

See the Cisco IP Phone Administration Guide for your phone series

Set up the new phone with the proxy TFTP server IP address so that the new phone knows how to locate the Unified Communications Manager node.

Step 2

Add a Phone to the System Manually

Add the phone to the Unified Communications Manager node.

Step 3

Configure a Directory Number Manually for a Phone

Add a directory number for the phone and configure some basic settings for the directory number.

### Add  a Phone to the System Manually

Manually add a new phone to the Cisco Unified Communications Manager node.

Step 1

In Cisco Unified Communications Manager Administration , select Device > Phone , then click Add New .

Step 2

In the Add a New Phone window, select  your phone model in the Phone Type field, then click Next .

Step 3

In the Phone Configuration window, select the protocol type for your device in the Select the device protocol field, then click Next .

Step 4

In the Device Information area, perform the following actions.

Enter a name in the Device Name field.

The name entered here must match the Device Name that is configured on your phone. See the documentation that supports your
                                                   endpoint device for more information.

Select a device pool for the phone from the list of device pools.

Select the phone button template to use from the list of phone button templates.

Step 5

In the Protocol Specific Information area, select the non-secure profile for your type of phone in the Device Security Profile field.

Step 6

Click Save .

#### What to do next

Configure a Directory Number Manually for a Phone

### Configure a Directory Number Manually for a Phone

There are multiple ways to manually add and configure a directory number (DN) using Cisco Unified Communications Manager Administration .

From the Directory Number Configuration window using Call Routing > Directory Number .

From the Phone Configuration window using Device > Phone when you select either Line [1] - Add a new DN or Line [2] - Add a new DN link in the Association Information area.

From the Phone Configuration window using Call Routing > Phone after you add the phone under call routing.

From the CTI Route Point Configuration window when you configure a CTI route point using Device > CTI Route Point .

This procedure assumes that you are configuring a DN for a new phone using the Phone Configuration window that appeared after you added the new phone to the Unified Communications Manager node.

Only the settings
                                 		  that apply to your phone model display using this method.

Tip

You can
                                             			 configure phone features at the same time that you add the new DN for the
                                             			 phone. To see all available DN settings, you must access the Directory Number Configuration window from call
                                             			 routing in the user interface.

#### Before you begin

The phone is added
                                 		  to the node. The Phone
                                    			 Configuration window should still be visible for the new phone that
                                 		  you are registering.

If your system
                                 		  uses partitions, collect the route partition and calling search space
                                 		  information to use for the new phone.

Step 1

Click Line
                                             				[1] - Add a new DN in the Association area of the Phone
                                             				Configuration window.

Tip

If the Phone Configuration window is not already visible,
                                                         				  select Device > Phone , then click Find and select the phone from the list of phones.

Step 2

In the Directory Number Configuration window, enter a
                                          			 dialable phone number in the Directory Number field.

Step 3

(Optional) Select a
                                          			 partition in the Route
                                             				Partition field.

Step 4

(Optional) Select a
                                          			 calling search space in the Calling Search Space field in the Directory Number Settings area.

Step 5

(Optional) Configure
                                          			 other directory number features as applicable for the new phone, then click Save .

For example,
                                             				if you already know the user name for the new phone, you can enter that in the Display (Caller ID) field. See the online help for
                                             				field descriptions.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | See the Cisco IP Phone Administration Guide for your phone series | Set up the new phone with the proxy TFTP server IP address so that the new phone knows how to locate the Unified Communications Manager node. |
| Step 2 | Add a Phone to the System Manually | Add the phone to the Unified Communications Manager node. |
| Step 3 | Configure a Directory Number Manually for a Phone | Add a directory number for the phone and configure some basic settings for the directory number. |

| Step 1 | In Cisco Unified Communications Manager Administration , select Device > Phone , then click Add New . |
|---|---|
| Step 2 | In the Add a New Phone window, select  your phone model in the Phone Type field, then click Next . |
| Step 3 | In the Phone Configuration window, select the protocol type for your device in the Select the device protocol field, then click Next . |
| Step 4 | In the Device Information area, perform the following actions. Enter a name in the Device Name field. The name entered here must match the Device Name that is configured on your phone. See the documentation that supports your
                                                   endpoint device for more information. Select a device pool for the phone from the list of device pools. Select the phone button template to use from the list of phone button templates. |
| Step 5 | In the Protocol Specific Information area, select the non-secure profile for your type of phone in the Device Security Profile field. |
| Step 6 | Click Save . |

| Tip | You can
                                             			 configure phone features at the same time that you add the new DN for the
                                             			 phone. To see all available DN settings, you must access the Directory Number Configuration window from call
                                             			 routing in the user interface. |
|---|---|

| Step 1 | Click Line
                                             				[1] - Add a new DN in the Association area of the Phone
                                             				Configuration window. Tip If the Phone Configuration window is not already visible,
                                                         				  select Device > Phone , then click Find and select the phone from the list of phones. | Tip | If the Phone Configuration window is not already visible,
                                                         				  select Device > Phone , then click Find and select the phone from the list of phones. |
|---|---|---|---|
| Tip | If the Phone Configuration window is not already visible,
                                                         				  select Device > Phone , then click Find and select the phone from the list of phones. |
| Step 2 | In the Directory Number Configuration window, enter a
                                          			 dialable phone number in the Directory Number field. |
| Step 3 | (Optional) Select a
                                          			 partition in the Route
                                             				Partition field. |
| Step 4 | (Optional) Select a
                                          			 calling search space in the Calling Search Space field in the Directory Number Settings area. |
| Step 5 | (Optional) Configure
                                          			 other directory number features as applicable for the new phone, then click Save . For example,
                                             				if you already know the user name for the new phone, you can enter that in the Display (Caller ID) field. See the online help for
                                             				field descriptions. |

| Tip | If the Phone Configuration window is not already visible,
                                                         				  select Device > Phone , then click Find and select the phone from the list of phones. |
|---|---|