---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-cucm-b-feature-configuration-guide-for-cisco1251su3-cuc-ac893bbc75
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/cucm_b_feature-configuration-guide-for-cisco1251su3/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0100010.html
retrieved_at: 2026-08-16T17:06:50.290328+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Accessing Hunt Groups

## Chapter: Accessing Hunt Groups

# Accessing Hunt Groups

## Hunt
                        	 Group Overview

A Hunt Group is a group of lines that are organized hierarchically, so that if the first number in the hunt group list is
                           busy, the system dials the second number. If the second number is busy, the system dials the next number, and so on.

The phone users can log in to or log out of the hunt groups by using the HLog softkey or the Hunt Group line button
                           		on the IP phone. 
                           	 The
                           		phone provides a visual status of the login state, so that the user can
                           		determine whether they are logged in to one or more of their line groups.

The Hunt Group feature provides the following functions:

The HLog softkey on the IP phone allows the user to toggle between login and logout of phone.

A hunt group allows a caller to automatically find an available line from amongst a group of extensions.

The Hunt Group Log Off feature allows phone users to prevent their phones from receiving incoming calls that get routed to
                                 directory numbers. Regardless of the phone status, the phone rings normally for incoming calls that are not calls to one or
                                 more line groups associated with the phone.

The directory numbers (DNs) belong to line groups that are associated with the phone.

System administrators can log in or log out the users from the phones that are automatically logged into hunt groups.

The HLog softkey allows a phone user to log a phone out of all line groups to which the phone directory numbers belong.

From Cisco Unified Communications Manager Release 9.0 onward, the Hunt Group Log Off feature enables the use of mobile device as a desk phone. When you use the Hlog
                                 softkey through your mobile client, you no longer receive calls that are placed to the hunt pilot.

## Hunt
                        	 Group Prerequisites

The phones must be running Skinny Client Control Protocol (SCCP) or Session Initiation Protocol (SIP).

The phone ringtone file must be located in the TFTP directory (/usr/local/cm/tftp).

## Hunt Group
                        	 Configuration Task Flow

### Before you begin

Review Hunt Group Prerequisites

Step 1

Configure a Softkey Template for Hunt Group

Configure a
                                          				softkey template for the HLog softkey.

Step 2

To Associate a Softkey Template with a Common Device Configuration ,
                                       			 complete the following subtasks:

- Add a Softkey Template to a Common Device Configuration

- Associate a Common Device Configuration with a Phone

Optional. To
                                          				make the softkey template available to phones, you must complete either this
                                          				step or the following step. Follow this step if your system uses a Common
                                          				Device Configuration to apply configuration options to phones. This is the most
                                          				commonly used method for making a softkey template available to phones.

Step 3

Associate a Softkey Template with a Phone

Optional. Use
                                          				this procedure either as an alternative to associating the softkey template
                                          				with the Common Device Configuration, or in conjunction with the Common Device
                                          				Configuration. Use this procedure in conjunction with the Common Device
                                          				Configuration if you need to assign a softkey template that overrides the
                                          				assignment in the Common Device Configuration or any other default softkey
                                          				assignment.

Step 4

Configure Phones for Hunt Group

Configure
                                          				phones to automatically log in to or log out of hunt groups and hunt lists.

### Configure a Softkey Template for Hunt Group

Connected

On Hook

Off Hook

Use this procedure to make the HLog softkey available:

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template .

Step 2

Perform the following steps to create a new softkey template; otherwise, proceed to the next step.

Click Add New .

Select a default template and click Copy .

Enter a new name for the template in the Softkey Template Name field.

Click Save .

Step 3

Perform the following steps to add softkeys to an existing template.

Click Find and enter the search criteria.

Select the required existing template.

Step 4

Check the Default Softkey Template check box to designate this softkey template as the default softkey template.

If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation.

Step 5

Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                          			 corner and click Go .

Step 6

From the Select
                                             				a Call State to Configure drop-down list, choose the call state for
                                          			 which you want the softkey to display.

Step 7

From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                          			 to change the position of the new softkey.

Step 8

Repeat the previous step to display the softkey in additional call states.

Step 9

Click Save .

Step 10

Perform one
                                          			 of the following tasks:

- Click Apply Config if you modified a template that is already associated with devices to restart the devices.

- If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                             see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections.

#### What to do next

Perform one of the
                                 		  following procedures:

Add a Softkey Template to a Common Device Configuration

Associate a Softkey Template with a Phone

### Associate a
                           	 Softkey Template with a Common Device Configuration

Optional.
                                 		  There are two ways to associate a softkey template with a phone:

Add the
                                       				softkey template to the Phone Configuration .

Add the
                                       				softkey template to the Common Device Configuration .

The
                                 		  procedures in this section describe how to associate the softkey template with
                                 		  a Common
                                    			 Device Configuration . Follow these procedures if your system uses a Common
                                    			 Device Configuration to apply configuration options to phones. This
                                 		  is the most commonly used method for making a softkey template available to
                                 		  phones.

To use the
                                 		  alternative method, see Associate a Softkey Template with a Phone .

#### Before you begin

Configure a Softkey Template for Hunt Group

Step 1

Add a Softkey Template to a Common Device Configuration

Step 2

Associate a Common Device Configuration with a Phone

#### Add a Softkey Template to a Common Device Configuration

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration .

Step 2

Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                             proceed to the next step.

Click Add New .

Enter a name for the Common Device Configuration in the Name field.

Click Save .

Step 3

Perform the following steps to add the softkey template to an existing Common Device Configuration.

Click Find and enter the search criteria.

Click an existing Common Device Configuration.

Step 4

In the Softkey Template drop-down list, choose the softkey
                                             			 template that contains the softkey that you want to make available.

Step 5

Click Save .

Step 6

Perform one
                                             			 of the following tasks:

- If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices.

- If you created a new Common Device Configuration, associate the configuration with devices and then restart them.

#### Associate a Common
                              	 Device Configuration with a Phone

##### Before you begin

Add a Softkey Template to a Common Device Configuration

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the phone device to add the softkey template.

Step 3

From the Common Device Configuration drop-down list, choose
                                             				  the common device configuration that contains the new softkey template.

Step 4

Click Save .

Step 5

Click Reset to update the phone settings.

### Associate a
                           	 Softkey Template with a Phone

This procedure is
                                 		  optional. You can use this procedure as an alternative to associating the
                                 		  softkey template with the Common Device Configuration. This procedure also
                                 		  works in conjunction with the Common Device Configuration: use it when you need
                                 		  to assign a softkey template that overrides the assignment in the Common Device
                                 		  Configuration or any other default softkey assignment.

#### Before you begin

Configure a Softkey Template for Hunt Group

Step 1

From Cisco
                                          			 Unified CM Administration, choose Device > Phone .

Step 2

Choose the
                                          			 phone to which you want to add the softkey template.

Step 3

From the Softkey Template drop-down list, choose the template
                                          			 that contains the new softkey.

Step 4

Click Save .

### Configure Phones
                           	 for Hunt Group

Use this
                                 		  procedure to configure phones to automatically log in to or log out of hunt
                                 		  groups and hunt lists.

#### Before you begin

Ensure the phone
                                 		  directory numbers belong to one or more hunt groups.

See the Administration Guide for Cisco Unified Communications Manager for information on hunt groups and hunt lists.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Perform one of
                                          			 the following tasks:

To modify
                                                				  the fields for an existing phone, enter search criteria and choose a phone from
                                                				  the resulting list. The Phone Configuration window appears.

To add a
                                                				  new phone, click Add New .

The Add a New Phone window appears.

Step 3

In the Phone
                                             				Configuration window, perform one of the following tasks:

To log out
                                                				  the phone from the hunt group, uncheck the Logged Into Hunt Group check box.

To log in
                                                				  the phone to the hunt group, ensure that the Logged Into Hunt Group check box is checked.

Step 4

Click Save .

#### Configure Hunt Group Service Parameter

The Hunt
                                       			 Group Logoff Notification service parameter provides the option to
                                    		  turn audible ringtones on or off when calls that come in to a line group arrive
                                    		  at a phone that is currently logged out. This ringtone alerts a logged-out user
                                    		  that there is an incoming call to a hunt list to which the line is a member,
                                    		  but the call will not ring at the phone of that line group member because of
                                    		  the logged-out status.

To configure the Hunt
                                       			 Group Logoff Notification service parameter, perform the following
                                    		  steps.

Step 1

From Cisco
                                                				Unified CM Administration , choose System > Service
                                                   				  Parameters .

Step 2

From the Server drop-down list, choose the server that is
                                             			 running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco
                                                				CallManager .

Step 4

In the
                                             			 Clusterwide Parameters ( Device - Phone ) section, configure values for the following Hunt
                                             			 Group Logoff Notification service parameter:

Step 5

Click Save .

## Hunt Group Interactions

Non-shared-line Directory Number

If a
                                          						phone is logged out of a line group and an extension on the phone is not
                                          						shared, the line group does not ring that directory number (DN) in the line
                                          						group. When the line group would normally offer the call to the DN, call
                                          						processing skips the DN and acts as if the DN does not belong to the line
                                          						group.

Shared-line Directory Number

- The DN does not ring if
                                                						  all phones that share that DN are logged out.

- The DN does ring if one or
                                                						  more phones that share the DN are logged in.

- The audible ring on a phone
                                                						  that is logged out is turned off by default. Cisco Unified Communications Manager provides a system
                                                						  parameter that can be set, so that a different ring tone plays when a call
                                                						  comes in to a logged-out hunt group member.

## Hunt Group Restrictions

Multiple Line Groups

When the user enables the Hunt Group Log Off feature by
                                          						pressing the HLog softkey, the phone gets logged out from all associated line
                                          						groups. This is because Hunt Group Log Off is a device-based feature. If a
                                          						phone has DNs that belong to multiple line groups, pressing the HLog softkey
                                          						logs the phone out of all associated line groups.

7940, 7960, and third-party SIP phones

- When a phone
                                             						  that is running SIP (7906, 7911, 7941, 7961, ) is logged in to
                                             						  hunt groups and Call Forward All is activated, the call gets presented to the
                                             						  phone that is running SIP.

- When 7940 and
                                             						  7960 phones that are running SIP are logged in to hunt groups and Call Forward
                                             						  All is activated, the phones get skipped and the next phone in the line group
                                             						  rings.

- 7940 and 7960
                                             						  phones that are running SIP and third-party phones that are running SIP can be
                                             						  logged in to or logged out of hunt groups by using the Phone Configuration window, but no
                                             						  softkey support exists.

- 7940 and 7960
                                             						  phones that are running SIP and third-party phones that are running SIP do not
                                             						  show "Logged out of hunt groups" on the status line.

- 7940 and 7960
                                             						  phones that are running SIP and third-party phones that are running SIP do not
                                             						  play the Hunt Group Logoff Notification tone regardless of whether the tone is
                                             						  configured.

| Note | The directory numbers (DNs) belong to line groups that are associated with the phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Softkey Template for Hunt Group | Configure a
                                          				softkey template for the HLog softkey. |
| Step 2 | To Associate a Softkey Template with a Common Device Configuration ,
                                       			 complete the following subtasks: Add a Softkey Template to a Common Device Configuration Associate a Common Device Configuration with a Phone | Optional. To
                                          				make the softkey template available to phones, you must complete either this
                                          				step or the following step. Follow this step if your system uses a Common
                                          				Device Configuration to apply configuration options to phones. This is the most
                                          				commonly used method for making a softkey template available to phones. |
| Step 3 | Associate a Softkey Template with a Phone | Optional. Use
                                          				this procedure either as an alternative to associating the softkey template
                                          				with the Common Device Configuration, or in conjunction with the Common Device
                                          				Configuration. Use this procedure in conjunction with the Common Device
                                          				Configuration if you need to assign a softkey template that overrides the
                                          				assignment in the Common Device Configuration or any other default softkey
                                          				assignment. |
| Step 4 | Configure Phones for Hunt Group | Configure
                                          				phones to automatically log in to or log out of hunt groups and hunt lists. |

| Note | You must
                                          		  create a new softkey template to configure the HLog softkey. You cannot
                                          		  configure the HLog softkey in a standard softkey template. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Softkey Template . |
|---|---|
| Step 2 | Perform the following steps to create a new softkey template; otherwise, proceed to the next step. Click Add New . Select a default template and click Copy . Enter a new name for the template in the Softkey Template Name field. Click Save . |
| Step 3 | Perform the following steps to add softkeys to an existing template. Click Find and enter the search criteria. Select the required existing template. |
| Step 4 | Check the Default Softkey Template check box to designate this softkey template as the default softkey template. Note If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. | Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
| Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
| Step 5 | Choose Configure Softkey Layout from the Related Links drop-down list in the upper right
                                          			 corner and click Go . |
| Step 6 | From the Select
                                             				a Call State to Configure drop-down list, choose the call state for
                                          			 which you want the softkey to display. |
| Step 7 | From the Unselected Softkeys list, choose the softkey to add and click the right arrow to move the softkey to the Selected Softkeys list. Use the up and down arrows
                                          			 to change the position of the new softkey. |
| Step 8 | Repeat the previous step to display the softkey in additional call states. |
| Step 9 | Click Save . |
| Step 10 | Perform one
                                          			 of the following tasks: Click Apply Config if you modified a template that is already associated with devices to restart the devices. If you created a new softkey template, associate the template with the devices and then restart them. For more information,
                                             see Add a Softkey Template to a Common Device Configuration and Associate a Softkey Template with a Phone sections. |

| Note | If you
                                                         				  designate a softkey template as the default softkey template, you cannot delete it unless you first remove the default
                                                         designation. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add a Softkey Template to a Common Device Configuration |  |
| Step 2 | Associate a Common Device Configuration with a Phone |  |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Perform the following steps to create a new Common Device Configuration and associate the softkey template with it; otherwise,
                                             proceed to the next step. Click Add New . Enter a name for the Common Device Configuration in the Name field. Click Save . |
| Step 3 | Perform the following steps to add the softkey template to an existing Common Device Configuration. Click Find and enter the search criteria. Click an existing Common Device Configuration. |
| Step 4 | In the Softkey Template drop-down list, choose the softkey
                                             			 template that contains the softkey that you want to make available. |
| Step 5 | Click Save . |
| Step 6 | Perform one
                                             			 of the following tasks: If you modified a Common Device Configuration that is already associated with devices, click Apply Config to restart the devices. If you created a new Common Device Configuration, associate the configuration with devices and then restart them. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the phone device to add the softkey template. |
| Step 3 | From the Common Device Configuration drop-down list, choose
                                             				  the common device configuration that contains the new softkey template. |
| Step 4 | Click Save . |
| Step 5 | Click Reset to update the phone settings. |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Device > Phone . The Find
                                             				and List Phones window appears. |
|---|---|
| Step 2 | Choose the
                                          			 phone to which you want to add the softkey template. The Phone
                                             				Configuration window appears. |
| Step 3 | From the Softkey Template drop-down list, choose the template
                                          			 that contains the new softkey. |
| Step 4 | Click Save . A
                                          			 dialog box appears with a message to press Reset to update the phone settings. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Perform one of
                                          			 the following tasks: To modify
                                                				  the fields for an existing phone, enter search criteria and choose a phone from
                                                				  the resulting list. The Phone Configuration window appears. To add a
                                                				  new phone, click Add New . The Add a New Phone window appears. |
| Step 3 | In the Phone
                                             				Configuration window, perform one of the following tasks: To log out
                                                				  the phone from the hunt group, uncheck the Logged Into Hunt Group check box. To log in
                                                				  the phone to the hunt group, ensure that the Logged Into Hunt Group check box is checked. Note The Logged Into Hunt Group check box remains checked by default for all phones. | Note | The Logged Into Hunt Group check box remains checked by default for all phones. |
| Note | The Logged Into Hunt Group check box remains checked by default for all phones. |
| Step 4 | Click Save . |

| Note | The Logged Into Hunt Group check box remains checked by default for all phones. |
|---|---|

| Step 1 | From Cisco
                                                				Unified CM Administration , choose System > Service
                                                   				  Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is
                                             			 running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco
                                                				CallManager . The Service
                                                				Parameter Configuration window appears. |
| Step 4 | In the
                                             			 Clusterwide Parameters ( Device - Phone ) section, configure values for the following Hunt
                                             			 Group Logoff Notification service parameter: Enter a name
                                             			 for the ringtone file that Cisco IP Phones play when a member of a line group
                                             			 (hunt group) has logged out. The default value for this service parameter is
                                             			 None, which indicates no ringtone. You can enter a maximum of 255 characters. |
| Step 5 | Click Save . The
                                             			 window refreshes, and Cisco
                                                				Unified Communications Manager updates the service parameter with
                                             			 your changes. |

| Feature | Interaction |
|---|---|
| Non-shared-line Directory Number | If a
                                          						phone is logged out of a line group and an extension on the phone is not
                                          						shared, the line group does not ring that directory number (DN) in the line
                                          						group. When the line group would normally offer the call to the DN, call
                                          						processing skips the DN and acts as if the DN does not belong to the line
                                          						group. |
| Shared-line Directory Number | Because
                                          						the Log Out of Hunt Group feature is device-based, when a user logs a phone
                                          						out, the feature affects only the logged-out phone. Calls to a line group that
                                          						contains a shared-line directory number behave as follows: The DN does not ring if
                                                						  all phones that share that DN are logged out. The DN does ring if one or
                                                						  more phones that share the DN are logged in. The audible ring on a phone
                                                						  that is logged out is turned off by default. Cisco Unified Communications Manager provides a system
                                                						  parameter that can be set, so that a different ring tone plays when a call
                                                						  comes in to a logged-out hunt group member. |

| Restriction | Description |
|---|---|
| Multiple Line Groups | When the user enables the Hunt Group Log Off feature by
                                          						pressing the HLog softkey, the phone gets logged out from all associated line
                                          						groups. This is because Hunt Group Log Off is a device-based feature. If a
                                          						phone has DNs that belong to multiple line groups, pressing the HLog softkey
                                          						logs the phone out of all associated line groups. |
| 7940, 7960, and third-party SIP phones | When a phone
                                             						  that is running SIP (7906, 7911, 7941, 7961, ) is logged in to
                                             						  hunt groups and Call Forward All is activated, the call gets presented to the
                                             						  phone that is running SIP. When 7940 and
                                             						  7960 phones that are running SIP are logged in to hunt groups and Call Forward
                                             						  All is activated, the phones get skipped and the next phone in the line group
                                             						  rings. 7940 and 7960
                                             						  phones that are running SIP and third-party phones that are running SIP can be
                                             						  logged in to or logged out of hunt groups by using the Phone Configuration window, but no
                                             						  softkey support exists. 7940 and 7960
                                             						  phones that are running SIP and third-party phones that are running SIP do not
                                             						  show "Logged out of hunt groups" on the status line. 7940 and 7960
                                             						  phones that are running SIP and third-party phones that are running SIP do not
                                             						  play the Hunt Group Logoff Notification tone regardless of whether the tone is
                                             						  configured. |