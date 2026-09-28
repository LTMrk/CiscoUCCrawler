---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-9dd15fe7c6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0101110.html
retrieved_at: 2026-08-16T17:32:44.442872+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Associate Users with Endpoints

## Chapter: Associate Users with Endpoints

# Associate Users with Endpoints

## Users to
                        	 Endpoints Association Overview

This chapter
                              		  describes how to associate devices with end users and application users. End
                              		  users can control the devices that you associate with them. Applications that
                              		  are identified as users can control devices, such as phones and Computer
                              		  Telephony Integration (CTI) ports.

## Associate Users with Endpoints Prerequisites

Configure end
                              		  users and application users before you associate them with endpoints. See Associate End Users with Devices and Associate Application Users with Devices .

## Users and Devices
                        	 Configuration Task Flow

Step 1

Associate End Users with Devices .

Step 2

Associate Application Users with Devices .

Associate
                                          				application users with devices.

### Associate End
                           	 Users with Devices

Cisco
                                    			 Unified Communications Manager does not allow duplicate end user IDs.

Step 1

From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > End User .

Step 2

From the Find
                                             				and List Application Users window, click Find .

Step 3

From the
                                          			 window that displays a list of end users, click the link for the relevant end
                                          			 user.

Step 4

From the End
                                             				User Configuration window, scroll down to the Device Information area and select the devices that
                                          			 you want to associate with the end user. In the Available Devices box, choose a device that you want
                                          			 to associate with the application user and click the down arrow below the box.

If no
                                                         				  devices exist in the Device Information area, click the Device Association button to open the User Device Association window. Select one or
                                                         				  multiple devices and click the Save Selected/Changes button. The selected devices
                                                         				  appear in the Controlled Devices list box of the Device Information area. Then, follow Steps 1 to 4
                                                         				  and associate a device.

Step 5

(Optional)
                                          			 To associate a line appearance to an end user for presence and to enable the
                                          			 on-the-phone status information to IM and Presence clients when this line
                                          			 appearance is off-hook, click the Line
                                             				Appearance Association from Presence button. The Line
                                             				Appearance Association for Presence window appears from where you
                                          			 can choose product type, device name, directory, partition, or description. The
                                          			 choices available in this window depend on the lines associated with the
                                          			 controlled devices. Click Save .

Step 6

Configure
                                          			 the fields from the End
                                             				User Configuration window. See the Related Topics section for more
                                          			 information about the fields and their configuration options.

Step 7

Click Save .

#### End User and Device Configuration Settings

Field

Description

User ID

Enter the end user identification name. Cisco Unified Communications Manager does not permit modifying the user ID after it
                                                is created. You may use the following special characters: =, +, <, >, #, ;, \, , “”, and blank spaces.

Password

Enter five or more alphanumeric or special characters for the end user password. You may use the following special characters:
                                                =, +, <, >, #, ;, \, , “”, and blank spaces

PIN

Enter five or more numeric characters for the Personal Identification Number.

Last Name

Enter the end user last name. You may use the following special characters: =,+, <, >, #, ;, \, , “”, and blank spaces

Middle Name

Enter the end user middle name. You may use the following special characters: =,+, <, >, #, ;, \, , “”, and blank spaces

First Name

Enter the end user first name. You may use the following special characters: =,+, <, >, #, ;, \, , “”, and blank spaces

Field

Description

Product Type

From the drop-down list, choose the type of device to associate with this end user.

MAC Address

Enter a unique MAC address for the new device that you are associating with the new user. The MAC address comprises exactly
                                                12 hexadecimal digits (0 to 9, A to F).

Calling Search Space DN

From the drop-down list, choose the calling search space for the directory number that you are associating with this user
                                                and device.

Calling Search Space Phone

From the drop-down list, choose the calling search space for the phone that you are associating with this user and device.

External Phone Number Mask

Specify the mask that is used to format caller ID information for external (outbound) calls that are made from the associated
                                                device.

The mask can contain up to 24 characters. Valid characters specify 0 to 9, *, #, and X.

Enter the literal digits that you want to appear in the caller ID information and use Xs to represent the directory number
                                                      of the associated device.

If you specify a mask of 972813XXXX, an external call from extension 1234 displays a caller ID number of 9728131234 if the
                                                      Use External Phone Number Mask option is checked on the route pattern that is used to make the external call. If you specify
                                                      a mask of all literal digits, such as 9728135000 to represent a main attendant number, that literal number (9728135000) displays
                                                      as the caller ID for an external call from any associated device.

Extension

Enter an extension for the new user and phone. You may use the following characters: 0 to 9, ?, [, ], +, -, *, ^, #, !.

This field represents the primary directory number for the end user. End users can have multiple lines on their phones.

Route Partition

From the drop-down list, choose a partition for the directory number that you specified in the Extension field.

Voice Mail Profile

From the drop-down list, choose a voice mail profile for the directory number.

Choose None to use the system default.

Enable Extension Mobility

Check this check box to enable extension mobility.

After you add the new user, you can use the User Management > End User menu option to choose an Extension Mobility profile.

### Associate
                           	 Application Users with Devices

You can associate
                                 		  devices over which application users have control. Application users can
                                 		  control devices, such as phones. Applications that are identified as users can
                                 		  control other devices, such as CTI ports. When application users have control
                                 		  of a phone, they can control certain settings for that phone, such as speed
                                 		  dial and call forwarding.

#### Before you begin

Associate End Users with Devices .

Step 1

From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User .

Step 2

From the Find
                                             				and List Application Users window, click Find .

Step 3

From the list
                                          			 of application users, click the link for the relevant Application User.

Step 4

From the Application User Configuration window, scroll down to
                                          			 the Device
                                             				Information area. In the Available Devices box, choose a device that you want
                                          			 to associate with the application user and click the down arrow below the box.

Step 5

To add to the
                                          			 list of available devices, click one of the following buttons:

- Find more
                                                				  Phones —To find the phones to associate with this application user.

- Find more Route
                                                				  Points —To find the CTI route points to associate with this
                                             				application user.

- Find more Pilot
                                                				  Points —To find the pilot points to associate with this application
                                             				user.

Step 6

Repeat Step 5
                                          			 for each device that you want to assign to the application user.

Step 7

Click Save .

## Interactions and Restrictions for Associating Users with Endpoints

### Interactions for Associating Users with Endpoints

Feature

Interaction

Non-CTI-controllable devices

For
                                             					 devices that are not CTI-controllable, such as H.323 devices, an asterisk (*)
                                             					 appears next to the device icon in the list of available devices.

Cisco
                                             					 Extension Mobility

Use Cisco Extension Mobility feature to configure a Cisco IP Phone to temporarily display as the phone of an end user. The
                                             end user can sign in to a phone, and the Extension Mobility profile (including line and speed-dial numbers) for the end user
                                             resides on the phone. This feature applies primarily in environments where end users are not permanently assigned to physical
                                             phones.

IM and
                                             					 Presence Service

Use Cisco
                                             					 Unified Communications Manager Administration to assign end users to IM and
                                             					 Presence Service server nodes and clusters for end users to receive the
                                             					 availability and Instant Messaging services of IM and Presence Service.

### Restrictions for Associating Users with Endpoints

Restriction

Description

Modification of end user information

You can modify end user information only if synchronization
                                             					 with an LDAP server is not enabled. To check whether synchronization with an
                                             					 LDAP server is enabled, choose System > LDAP > LDAP
                                                   						  System .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Associate End Users with Devices . | Associate end
                                       			 users with devices. |
| Step 2 | Associate Application Users with Devices . | Associate
                                          				application users with devices. |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > End User . |
|---|---|
| Step 2 | From the Find
                                             				and List Application Users window, click Find . |
| Step 3 | From the
                                          			 window that displays a list of end users, click the link for the relevant end
                                          			 user. |
| Step 4 | From the End
                                             				User Configuration window, scroll down to the Device Information area and select the devices that
                                          			 you want to associate with the end user. In the Available Devices box, choose a device that you want
                                          			 to associate with the application user and click the down arrow below the box. Note If no
                                                         				  devices exist in the Device Information area, click the Device Association button to open the User Device Association window. Select one or
                                                         				  multiple devices and click the Save Selected/Changes button. The selected devices
                                                         				  appear in the Controlled Devices list box of the Device Information area. Then, follow Steps 1 to 4
                                                         				  and associate a device. | Note | If no
                                                         				  devices exist in the Device Information area, click the Device Association button to open the User Device Association window. Select one or
                                                         				  multiple devices and click the Save Selected/Changes button. The selected devices
                                                         				  appear in the Controlled Devices list box of the Device Information area. Then, follow Steps 1 to 4
                                                         				  and associate a device. |
| Note | If no
                                                         				  devices exist in the Device Information area, click the Device Association button to open the User Device Association window. Select one or
                                                         				  multiple devices and click the Save Selected/Changes button. The selected devices
                                                         				  appear in the Controlled Devices list box of the Device Information area. Then, follow Steps 1 to 4
                                                         				  and associate a device. |
| Step 5 | (Optional)
                                          			 To associate a line appearance to an end user for presence and to enable the
                                          			 on-the-phone status information to IM and Presence clients when this line
                                          			 appearance is off-hook, click the Line
                                             				Appearance Association from Presence button. The Line
                                             				Appearance Association for Presence window appears from where you
                                          			 can choose product type, device name, directory, partition, or description. The
                                          			 choices available in this window depend on the lines associated with the
                                          			 controlled devices. Click Save . |
| Step 6 | Configure
                                          			 the fields from the End
                                             				User Configuration window. See the Related Topics section for more
                                          			 information about the fields and their configuration options. |
| Step 7 | Click Save . |

| Note | If no
                                                         				  devices exist in the Device Information area, click the Device Association button to open the User Device Association window. Select one or
                                                         				  multiple devices and click the Save Selected/Changes button. The selected devices
                                                         				  appear in the Controlled Devices list box of the Device Information area. Then, follow Steps 1 to 4
                                                         				  and associate a device. |
|---|---|

| Field | Description |
|---|---|
| User ID | Enter the end user identification name. Cisco Unified Communications Manager does not permit modifying the user ID after it
                                                is created. You may use the following special characters: =, +, <, >, #, ;, \, , “”, and blank spaces. |
| Password | Enter five or more alphanumeric or special characters for the end user password. You may use the following special characters:
                                                =, +, <, >, #, ;, \, , “”, and blank spaces |
| PIN | Enter five or more numeric characters for the Personal Identification Number. |
| Last Name | Enter the end user last name. You may use the following special characters: =,+, <, >, #, ;, \, , “”, and blank spaces |
| Middle Name | Enter the end user middle name. You may use the following special characters: =,+, <, >, #, ;, \, , “”, and blank spaces |
| First Name | Enter the end user first name. You may use the following special characters: =,+, <, >, #, ;, \, , “”, and blank spaces |

| Field | Description |
|---|---|
| Product Type | From the drop-down list, choose the type of device to associate with this end user. |
| MAC Address | Enter a unique MAC address for the new device that you are associating with the new user. The MAC address comprises exactly
                                                12 hexadecimal digits (0 to 9, A to F). |
| Calling Search Space DN | From the drop-down list, choose the calling search space for the directory number that you are associating with this user
                                                and device. |
| Calling Search Space Phone | From the drop-down list, choose the calling search space for the phone that you are associating with this user and device. |
| External Phone Number Mask | Specify the mask that is used to format caller ID information for external (outbound) calls that are made from the associated
                                                device. The mask can contain up to 24 characters. Valid characters specify 0 to 9, *, #, and X. Enter the literal digits that you want to appear in the caller ID information and use Xs to represent the directory number
                                                      of the associated device. If you specify a mask of 972813XXXX, an external call from extension 1234 displays a caller ID number of 9728131234 if the
                                                      Use External Phone Number Mask option is checked on the route pattern that is used to make the external call. If you specify
                                                      a mask of all literal digits, such as 9728135000 to represent a main attendant number, that literal number (9728135000) displays
                                                      as the caller ID for an external call from any associated device. |
| Extension | Enter an extension for the new user and phone. You may use the following characters: 0 to 9, ?, [, ], +, -, *, ^, #, !. This field represents the primary directory number for the end user. End users can have multiple lines on their phones. |
| Route Partition | From the drop-down list, choose a partition for the directory number that you specified in the Extension field. |
| Voice Mail Profile | From the drop-down list, choose a voice mail profile for the directory number. Choose None to use the system default. |
| Enable Extension Mobility | Check this check box to enable extension mobility. After you add the new user, you can use the User Management > End User menu option to choose an Extension Mobility profile. |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > Application User . appears. |
|---|---|
| Step 2 | From the Find
                                             				and List Application Users window, click Find . |
| Step 3 | From the list
                                          			 of application users, click the link for the relevant Application User. |
| Step 4 | From the Application User Configuration window, scroll down to
                                          			 the Device
                                             				Information area. In the Available Devices box, choose a device that you want
                                          			 to associate with the application user and click the down arrow below the box. The
                                          			 device is moved to the Controlled Devices box. |
| Step 5 | To add to the
                                          			 list of available devices, click one of the following buttons: Find more
                                                				  Phones —To find the phones to associate with this application user. Find more Route
                                                				  Points —To find the CTI route points to associate with this
                                             				application user. Find more Pilot
                                                				  Points —To find the pilot points to associate with this application
                                             				user. |
| Step 6 | Repeat Step 5
                                          			 for each device that you want to assign to the application user. |
| Step 7 | Click Save . |

| Feature | Interaction |
|---|---|
| Non-CTI-controllable devices | For
                                             					 devices that are not CTI-controllable, such as H.323 devices, an asterisk (*)
                                             					 appears next to the device icon in the list of available devices. |
| Cisco
                                             					 Extension Mobility | Use Cisco Extension Mobility feature to configure a Cisco IP Phone to temporarily display as the phone of an end user. The
                                             end user can sign in to a phone, and the Extension Mobility profile (including line and speed-dial numbers) for the end user
                                             resides on the phone. This feature applies primarily in environments where end users are not permanently assigned to physical
                                             phones. |
| IM and
                                             					 Presence Service | Use Cisco
                                             					 Unified Communications Manager Administration to assign end users to IM and
                                             					 Presence Service server nodes and clusters for end users to receive the
                                             					 availability and Instant Messaging services of IM and Presence Service. |

| Restriction | Description |
|---|---|
| Modification of end user information | You can modify end user information only if synchronization
                                             					 with an LDAP server is not enabled. To check whether synchronization with an
                                             					 LDAP server is enabled, choose System > LDAP > LDAP
                                                   						  System . |