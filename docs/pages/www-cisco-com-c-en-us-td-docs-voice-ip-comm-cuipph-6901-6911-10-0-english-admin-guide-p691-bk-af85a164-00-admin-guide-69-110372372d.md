---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-10-0-english-admin-guide-p691-bk-af85a164-00-admin-guide-69-110372372d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/10_0/english/admin_guide/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0_appendix_01100.html
retrieved_at: 2026-08-21T14:27:53.242228+00:00
---

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

# Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

Updated: May 9, 2025

Chapter: Basic Phone Administration Steps

## Chapter: Basic Phone Administration Steps

# Basic Phone Administration Steps

## Phone Administration Overview

This appendix provides minimum, basic configuration steps for
                           		you to do the following actions:

Add a new user to Cisco Unified Communications Manager

Configure a new phone for that user

Associate that user to that phone

Complete other basic end-user configuration tasks

The procedures provide one method for performing these tasks and
                           		are not the only way to perform these tasks. They are a streamlined approach to
                           		get a new user and the corresponding phone running on the system.

These procedures are designed to be used on a mature Cisco
                           		Unified Communications Manager system where calling search spaces, partitions,
                           		and other complicated configuration have already been done and are in place for
                           		existing users.

## Example User Information

In the procedures that follow, examples are given when possible to illustrate some of the steps. Sample user and phone information
                           used throughout these procedures includes:

User’s Name: John Doe

User ID: johndoe

Phone model: 6901

Protocol: SCCP

MAC address listed on phone: 00127F576611

Five-digit internal telephone number: 26640

## Cisco Unified Communications Manager User Addition

This section describes steps for adding a user to Cisco Unified Communications Manager. Follow one of the procedures in this
                           section, depending on your operating system and the manner in which you are adding the user.

### Add User from External LDAP Directory

If you added a user to an LDAP Directory (a non-Cisco Unified
                                 		  Communications Server directory), you can immediately synchronize that
                                 		  directory to the Cisco Unified Communications Manager on which you are adding
                                 		  this same user and the phone user by following these steps:

Step 1

Login to Cisco Unified Communications Manager.

Step 2

Choose System > LDAP > LDAP
                                                				  Directory .

Step 3

Use the Find button to locate your LDAP directory.

Step 4

Click the LDAP directory name .

Step 5

Click Perform Full Sync Now .

If you do not need to immediately synchronize the LDAP Directory
                                                         				  to the Cisco Unified Communications Manager, the LDAP Directory Synchronization
                                                         				  Schedule on the LDAP Directory window determines when the
                                                         				  next autosynchronization occurs. However, the synchronization must occur
                                                         				  before you can associate a new user to a device.

Step 6

Proceed to Phone Setup .

### Add User Directly to Cisco Unified Communications Manager

If you are not using an LDAP directory, you can add a user
                                 		  directly to Cisco Unified Communications Manager by following these steps:

Step 1

Choose User
                                                				  Management > End User .

Step 2

Click Add New .

The 
                                             				End User Configuration window appears.

Step 3

In the User Information pane of this window, enter the following:

User ID: Enter the user identification name. Cisco
                                                   					 Unified Communications Manager does not permit modifying the user ID after it
                                                   					 is created. You may use the following special characters: =, +, <, >, #, ;, \, , "" , and blank spaces.

Example: johndoe

Password and Confirm Password: Enter five or more alphanumeric
                                                   					 or special characters for the user password. You may use the following
                                                   					 special characters: =, +, <, >, #, ;, \, , "", and blank spaces.

Last Name: Enter the user last name. You may use the
                                                   					 following special characters: =, +, <, >, #, ;, \, , "" , and blank
                                                   					 spaces.

Example: doe

Telephone Number: Enter the primary directory number for the user. Users can have multiple lines on their phones.

Example: 26640 (John Doe’s internal company telephone
                                                   					 number)

Step 4

Click Save .

Step 5

Proceed to the section Phone Setup .

## Phone Setup

To identify the user phone model and protocol, follow these
                              		  steps:

Step 1

From Cisco Unified Communications Manager, choose Device > Phone .

Step 2

Click Add New .

Step 3

Select the user phone model from the Phone Type drop-down list,
                                       			 then click Next .

The Phone Configuration window appears.

On the Phone Configuration  window, you can
                                                      				  use the default values for most of the fields.

Step 4

For the required fields, possible values can be configured as
                                       			 follows:

The configuration is based on the example of user johndoe .

In the Device Information pane of this window:

Enter the MAC address of the phone, listed on a sticker on the back of phone.

The MAC address is 12 hexadecimal characters long.

Example: 00127F576611 (MAC address on John Doe’s phone)

This is an optional field where you can
                                                      						  enter a useful description. This will help you if you need to search for
                                                      						  information about this user.

Choose the device pool for which you want to
                                                      						  assign this phone. The device pool defines sets of common characteristics for
                                                      						  devices, such as region, date/time group, and MLPP information.

Device Pools are defined on the 
                                                                  						Device Pool Configuration window of
                                                                  						Cisco Unified Communications Server Administration
                                                                  						( System > Device
                                                                        							 Pool ).

Choose the appropriate phone
                                                      						  button template from the drop-down list. The phone button template determines
                                                      						  the configuration of features on a phone and identifies the predetermined
                                                      						  number to be dialed after pressing the feature button. To configure the
                                                      						  Predetermined Number for a feature, navigate to the Phone Button Template of
                                                      						  Cisco Unified IP Phone 6911. In the template, 1 is always assigned to the line,
                                                      						  so the button number minus 1 is the predetermined number that is provided by
                                                      						  your system administrator.

Phone button templates are defined on the Phone Button
                                                                  						Template Configuration window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Phone Button
                                                                        							 Template ). You can use the search fields and the Find button to find all configured
                                                                  						phone button templates and their current settings.

From the drop-down list, choose a
                                                      						  common phone profile from the list of available common phone profiles.

Common Phone Profiles are defined on the 
                                                                  						Common Phone Profile Configuration
                                                                  						window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Common Phone Profile ).
                                                                  						You can use the search fields and the Find button to
                                                                  						find all configured common phone profiles and their current settings.

From the drop-down list, choose the
                                                      						  appropriate calling search space (CSS). A calling search space comprises a
                                                      						  collection of partitions (analogous to a collection of available phone books)
                                                      						  that are searched to determine how a dialed number should be routed. The
                                                      						  calling search space for the device and the calling search space for the
                                                      						  directory number get used together. The directory number CSS takes precedence
                                                      						  over the device CSS.

Calling Search Spaces are defined on the 
                                                                  						Calling Search Space Configuration
                                                                  						window of Cisco Unified Communications Manager ( Calling
                                                                        							 routing > Class of Control > Calling
                                                                        							 Search Space ). You can use the search fields and the Find button to find all configured
                                                                  						Calling Search Spaces and their current settings.

Choose the appropriate location for this Cisco
                                                      						  Unified IP Phone.

From the drop-down list, choose the user
                                                      						  ID of the assigned phone user.

In the Protocol Specific Information pane of this window,
                                             				  choose a Device Security Profile from the drop-down list. To enable security
                                             				  features for a phone, you must configure a new security profile for the device
                                             				  type and protocol and apply it to the phone. If the phone does not support
                                             				  security, choose a nonsecure profile.

To identify the settings that are contained in the profile,
                                                					 choose System > Security
                                                      						  Profile > Phone Security Profile .

The security profile chosen should be based on the overall
                                                            						security strategy of the company.

In the Extension Information pane of this window, check the
                                             				  Enable Extension Mobility box if this phone supports Cisco Extension Mobility.

Click Save .

Step 5

Configure line settings:

On the 
                                             				  Phone Configuration window, click Line 1 on
                                             				  the left pane of the window. The 
                                             				  Directory Number Configuration window
                                             				  appears.

In the Directory Number field, enter a valid number that can
                                             				  be dialed.

This field should contain the same number that appears in
                                                            						the Telephone Number field on the 
                                                            						User Configuration window.

Example : 26640 is the directory number of user John Doe
                                                					 in the example above.

From the Route Partition drop-down list, choose the partition
                                             				  to which the directory number belongs. If you do not want to restrict access to
                                             				  the directory number, choose <None> for the partition.

From the Calling Search Space drop-down list (Directory Number
                                             				  Settings pane of the 
                                             				  Directory Number Configuration window),
                                             				  choose the appropriate calling search space. A calling search space comprises a
                                             				  collection of partitions that are searched for numbers that are called from
                                             				  this directory number. The value that you choose applies to all devices that
                                             				  are using this directory number.

In the Call Pickup and Call Forward Settings pane of the 
                                             				  Directory Number Configuration window,
                                             				  choose the items (for example, Forward All, Forward Busy Internal) and
                                             				  corresponding destinations to which calls should be sent.

Example: If you want incoming internal and external calls that
                                                					 receive a busy signal to be forwarded to the voice mail for this line, check
                                                					 the Voice Mail box next to the 
                                                					 Forward Busy Internal and 
                                                					 Forward Busy External items in the left
                                                					 column of the Call Pickup and Call Forward Settings pane.

In the 
                                             				  Line 1 on Device... pane of the 
                                             				  Directory Number Configuration window,
                                             				  configure the following parameters:

You can enter the
                                                      						  first name and last name of the user of this device so that this name will be
                                                      						  displayed for all internal calls. You can also leave this field blank to have
                                                      						  the system display the phone extension.

Indicate phone number (or
                                                      						  mask) that is used to send Caller ID information when a call is placed from
                                                      						  this line.

You can enter a maximum of 24 number and "X" characters. The X characters represent the directory number and must appear
                                                      					 at the end of the pattern.

Example: Using the John Doe extension in the example
                                                      					 above, if you specify a mask of 408902XXXX, an external call from extension
                                                      					 6640 displays a caller ID number of 4089026640.

This setting applies only to the current device unless you
                                                      						check the Update Shared Device Settings check box at right and click the Propagate Selected button. The check box only displays if
                                                      						other devices share this directory number.

Click Save .

Click Associate End Users at the bottom of the
                                             				  window to associate a user to the line being configured.

Use the Find button and the Search fields to locate the user, check the box
                                             				  next to the user name, and then click Add Selected .

The user’s name and user ID
                                                				  should appear in the 
                                                				  Users Associated With Line pane of the 
                                                				  Directory Number Configuration window.

Click Save . The user is now associated with Line
                                             				  1 on the phone.

If the phone has a second line, configure Line 2.

Associate the user with the device:

Choose User Management > End
                                                            							 User .

Use the search boxes and the Find button to locate the
                                                      						  user you have added (for example, doe for the last name).

Click on the user ID (for example, johndoe ). The 
                                                      						  End User Configuration window appears.

Click Device Associations .

Use the Search fields and the Find button to locate the device
                                                      						  with which you want to associate to the user.

Select the device, then click Save Selected/Changes . The user is
                                                      						  now associated with the device.

Click the Go button next to the Back to User
                                                      						  Related link in the upper-right corner of the screen.

Step 6

Proceed to Perform Final End User Configuration Steps .

## Perform Final End User Configuration Steps

If you are not already on the End User Configuration page,
                              		  choose User Management > End
                                    				User to perform some final configuration tasks. Use
                              		  the Search fields and the Find button to locate the user (for example,
                              		  John Doe), then click on the user ID to get to the End User Configuration window for the user. In the End User configuration window, do the following:

Step 1

In the Directory Number Associations pane of the screen, set the
                                       			 primary extension from the drop-down list.

Step 2

In the Mobility Information pane, check the Enable Mobility box.

Step 3

In the Permissions Information pane, use the User Group buttons to
                                       			 add this user to any user groups. For example, you may want to add the user to
                                       			 a group that has been defined as a Standard CCM End User Group.

To view all configured user groups, choose User Management > User
                                                					 Group .

Step 4

Click Save .

| Step 1 | Login to Cisco Unified Communications Manager. |
|---|---|
| Step 2 | Choose System > LDAP > LDAP
                                                				  Directory . |
| Step 3 | Use the Find button to locate your LDAP directory. |
| Step 4 | Click the LDAP directory name . |
| Step 5 | Click Perform Full Sync Now . Note If you do not need to immediately synchronize the LDAP Directory
                                                         				  to the Cisco Unified Communications Manager, the LDAP Directory Synchronization
                                                         				  Schedule on the LDAP Directory window determines when the
                                                         				  next autosynchronization occurs. However, the synchronization must occur
                                                         				  before you can associate a new user to a device. | Note | If you do not need to immediately synchronize the LDAP Directory
                                                         				  to the Cisco Unified Communications Manager, the LDAP Directory Synchronization
                                                         				  Schedule on the LDAP Directory window determines when the
                                                         				  next autosynchronization occurs. However, the synchronization must occur
                                                         				  before you can associate a new user to a device. |
| Note | If you do not need to immediately synchronize the LDAP Directory
                                                         				  to the Cisco Unified Communications Manager, the LDAP Directory Synchronization
                                                         				  Schedule on the LDAP Directory window determines when the
                                                         				  next autosynchronization occurs. However, the synchronization must occur
                                                         				  before you can associate a new user to a device. |
| Step 6 | Proceed to Phone Setup . |

| Note | If you do not need to immediately synchronize the LDAP Directory
                                                         				  to the Cisco Unified Communications Manager, the LDAP Directory Synchronization
                                                         				  Schedule on the LDAP Directory window determines when the
                                                         				  next autosynchronization occurs. However, the synchronization must occur
                                                         				  before you can associate a new user to a device. |
|---|---|

| Step 1 | Choose User
                                                				  Management > End User . |
|---|---|
| Step 2 | Click Add New . The 
                                             				End User Configuration window appears. |
| Step 3 | In the User Information pane of this window, enter the following: User ID: Enter the user identification name. Cisco
                                                   					 Unified Communications Manager does not permit modifying the user ID after it
                                                   					 is created. You may use the following special characters: =, +, <, >, #, ;, \, , "" , and blank spaces. Example: johndoe Password and Confirm Password: Enter five or more alphanumeric
                                                   					 or special characters for the user password. You may use the following
                                                   					 special characters: =, +, <, >, #, ;, \, , "", and blank spaces. Last Name: Enter the user last name. You may use the
                                                   					 following special characters: =, +, <, >, #, ;, \, , "" , and blank
                                                   					 spaces. Example: doe Telephone Number: Enter the primary directory number for the user. Users can have multiple lines on their phones. Example: 26640 (John Doe’s internal company telephone
                                                   					 number) |
| Step 4 | Click Save . |
| Step 5 | Proceed to the section Phone Setup . |

| Step 1 | From Cisco Unified Communications Manager, choose Device > Phone . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Select the user phone model from the Phone Type drop-down list,
                                       			 then click Next . The Phone Configuration window appears. Note On the Phone Configuration  window, you can
                                                      				  use the default values for most of the fields. | Note | On the Phone Configuration  window, you can
                                                      				  use the default values for most of the fields. |
| Note | On the Phone Configuration  window, you can
                                                      				  use the default values for most of the fields. |
| Step 4 | For the required fields, possible values can be configured as
                                       			 follows: Note The configuration is based on the example of user johndoe . In the Device Information pane of this window: MAC Address Enter the MAC address of the phone, listed on a sticker on the back of phone. The MAC address is 12 hexadecimal characters long. Example: 00127F576611 (MAC address on John Doe’s phone) Description This is an optional field where you can
                                                      						  enter a useful description. This will help you if you need to search for
                                                      						  information about this user. Device Pool Choose the device pool for which you want to
                                                      						  assign this phone. The device pool defines sets of common characteristics for
                                                      						  devices, such as region, date/time group, and MLPP information. Note Device Pools are defined on the 
                                                                  						Device Pool Configuration window of
                                                                  						Cisco Unified Communications Server Administration
                                                                  						( System > Device
                                                                        							 Pool ). Phone Button Template Choose the appropriate phone
                                                      						  button template from the drop-down list. The phone button template determines
                                                      						  the configuration of features on a phone and identifies the predetermined
                                                      						  number to be dialed after pressing the feature button. To configure the
                                                      						  Predetermined Number for a feature, navigate to the Phone Button Template of
                                                      						  Cisco Unified IP Phone 6911. In the template, 1 is always assigned to the line,
                                                      						  so the button number minus 1 is the predetermined number that is provided by
                                                      						  your system administrator. Note Phone button templates are defined on the Phone Button
                                                                  						Template Configuration window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Phone Button
                                                                        							 Template ). You can use the search fields and the Find button to find all configured
                                                                  						phone button templates and their current settings. Common Phone Profile From the drop-down list, choose a
                                                      						  common phone profile from the list of available common phone profiles. Note Common Phone Profiles are defined on the 
                                                                  						Common Phone Profile Configuration
                                                                  						window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Common Phone Profile ).
                                                                  						You can use the search fields and the Find button to
                                                                  						find all configured common phone profiles and their current settings. Calling Search Space From the drop-down list, choose the
                                                      						  appropriate calling search space (CSS). A calling search space comprises a
                                                      						  collection of partitions (analogous to a collection of available phone books)
                                                      						  that are searched to determine how a dialed number should be routed. The
                                                      						  calling search space for the device and the calling search space for the
                                                      						  directory number get used together. The directory number CSS takes precedence
                                                      						  over the device CSS. Note Calling Search Spaces are defined on the 
                                                                  						Calling Search Space Configuration
                                                                  						window of Cisco Unified Communications Manager ( Calling
                                                                        							 routing > Class of Control > Calling
                                                                        							 Search Space ). You can use the search fields and the Find button to find all configured
                                                                  						Calling Search Spaces and their current settings. Location Choose the appropriate location for this Cisco
                                                      						  Unified IP Phone. Owner User ID From the drop-down list, choose the user
                                                      						  ID of the assigned phone user. In the Protocol Specific Information pane of this window,
                                             				  choose a Device Security Profile from the drop-down list. To enable security
                                             				  features for a phone, you must configure a new security profile for the device
                                             				  type and protocol and apply it to the phone. If the phone does not support
                                             				  security, choose a nonsecure profile. To identify the settings that are contained in the profile,
                                                					 choose System > Security
                                                      						  Profile > Phone Security Profile . Note The security profile chosen should be based on the overall
                                                            						security strategy of the company. In the Extension Information pane of this window, check the
                                             				  Enable Extension Mobility box if this phone supports Cisco Extension Mobility. Click Save . | Note | The configuration is based on the example of user johndoe . | Note | Device Pools are defined on the 
                                                                  						Device Pool Configuration window of
                                                                  						Cisco Unified Communications Server Administration
                                                                  						( System > Device
                                                                        							 Pool ). | Note | Phone button templates are defined on the Phone Button
                                                                  						Template Configuration window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Phone Button
                                                                        							 Template ). You can use the search fields and the Find button to find all configured
                                                                  						phone button templates and their current settings. | Note | Common Phone Profiles are defined on the 
                                                                  						Common Phone Profile Configuration
                                                                  						window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Common Phone Profile ).
                                                                  						You can use the search fields and the Find button to
                                                                  						find all configured common phone profiles and their current settings. | Note | Calling Search Spaces are defined on the 
                                                                  						Calling Search Space Configuration
                                                                  						window of Cisco Unified Communications Manager ( Calling
                                                                        							 routing > Class of Control > Calling
                                                                        							 Search Space ). You can use the search fields and the Find button to find all configured
                                                                  						Calling Search Spaces and their current settings. | Note | The security profile chosen should be based on the overall
                                                            						security strategy of the company. |
| Note | The configuration is based on the example of user johndoe . |
| Note | Device Pools are defined on the 
                                                                  						Device Pool Configuration window of
                                                                  						Cisco Unified Communications Server Administration
                                                                  						( System > Device
                                                                        							 Pool ). |
| Note | Phone button templates are defined on the Phone Button
                                                                  						Template Configuration window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Phone Button
                                                                        							 Template ). You can use the search fields and the Find button to find all configured
                                                                  						phone button templates and their current settings. |
| Note | Common Phone Profiles are defined on the 
                                                                  						Common Phone Profile Configuration
                                                                  						window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Common Phone Profile ).
                                                                  						You can use the search fields and the Find button to
                                                                  						find all configured common phone profiles and their current settings. |
| Note | Calling Search Spaces are defined on the 
                                                                  						Calling Search Space Configuration
                                                                  						window of Cisco Unified Communications Manager ( Calling
                                                                        							 routing > Class of Control > Calling
                                                                        							 Search Space ). You can use the search fields and the Find button to find all configured
                                                                  						Calling Search Spaces and their current settings. |
| Note | The security profile chosen should be based on the overall
                                                            						security strategy of the company. |
| Step 5 | Configure line settings: On the 
                                             				  Phone Configuration window, click Line 1 on
                                             				  the left pane of the window. The 
                                             				  Directory Number Configuration window
                                             				  appears. In the Directory Number field, enter a valid number that can
                                             				  be dialed. Note This field should contain the same number that appears in
                                                            						the Telephone Number field on the 
                                                            						User Configuration window. Example : 26640 is the directory number of user John Doe
                                                					 in the example above. From the Route Partition drop-down list, choose the partition
                                             				  to which the directory number belongs. If you do not want to restrict access to
                                             				  the directory number, choose <None> for the partition. From the Calling Search Space drop-down list (Directory Number
                                             				  Settings pane of the 
                                             				  Directory Number Configuration window),
                                             				  choose the appropriate calling search space. A calling search space comprises a
                                             				  collection of partitions that are searched for numbers that are called from
                                             				  this directory number. The value that you choose applies to all devices that
                                             				  are using this directory number. In the Call Pickup and Call Forward Settings pane of the 
                                             				  Directory Number Configuration window,
                                             				  choose the items (for example, Forward All, Forward Busy Internal) and
                                             				  corresponding destinations to which calls should be sent. Example: If you want incoming internal and external calls that
                                                					 receive a busy signal to be forwarded to the voice mail for this line, check
                                                					 the Voice Mail box next to the 
                                                					 Forward Busy Internal and 
                                                					 Forward Busy External items in the left
                                                					 column of the Call Pickup and Call Forward Settings pane. In the 
                                             				  Line 1 on Device... pane of the 
                                             				  Directory Number Configuration window,
                                             				  configure the following parameters: Display (Internal Caller ID field) You can enter the
                                                      						  first name and last name of the user of this device so that this name will be
                                                      						  displayed for all internal calls. You can also leave this field blank to have
                                                      						  the system display the phone extension. External Phone Number Mask Indicate phone number (or
                                                      						  mask) that is used to send Caller ID information when a call is placed from
                                                      						  this line. You can enter a maximum of 24 number and "X" characters. The X characters represent the directory number and must appear
                                                      					 at the end of the pattern. Example: Using the John Doe extension in the example
                                                      					 above, if you specify a mask of 408902XXXX, an external call from extension
                                                      					 6640 displays a caller ID number of 4089026640. This setting applies only to the current device unless you
                                                      						check the Update Shared Device Settings check box at right and click the Propagate Selected button. The check box only displays if
                                                      						other devices share this directory number. Click Save . Click Associate End Users at the bottom of the
                                             				  window to associate a user to the line being configured. Use the Find button and the Search fields to locate the user, check the box
                                             				  next to the user name, and then click Add Selected . The user’s name and user ID
                                                				  should appear in the 
                                                				  Users Associated With Line pane of the 
                                                				  Directory Number Configuration window. Click Save . The user is now associated with Line
                                             				  1 on the phone. If the phone has a second line, configure Line 2. Associate the user with the device: Choose User Management > End
                                                            							 User . Use the search boxes and the Find button to locate the
                                                      						  user you have added (for example, doe for the last name). Click on the user ID (for example, johndoe ). The 
                                                      						  End User Configuration window appears. Click Device Associations . Use the Search fields and the Find button to locate the device
                                                      						  with which you want to associate to the user. Select the device, then click Save Selected/Changes . The user is
                                                      						  now associated with the device. Click the Go button next to the Back to User
                                                      						  Related link in the upper-right corner of the screen. | Note | This field should contain the same number that appears in
                                                            						the Telephone Number field on the 
                                                            						User Configuration window. |
| Note | This field should contain the same number that appears in
                                                            						the Telephone Number field on the 
                                                            						User Configuration window. |
| Step 6 | Proceed to Perform Final End User Configuration Steps . |

| Note | On the Phone Configuration  window, you can
                                                      				  use the default values for most of the fields. |
|---|---|

| Note | The configuration is based on the example of user johndoe . |
|---|---|

| Note | Device Pools are defined on the 
                                                                  						Device Pool Configuration window of
                                                                  						Cisco Unified Communications Server Administration
                                                                  						( System > Device
                                                                        							 Pool ). |
|---|---|

| Note | Phone button templates are defined on the Phone Button
                                                                  						Template Configuration window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Phone Button
                                                                        							 Template ). You can use the search fields and the Find button to find all configured
                                                                  						phone button templates and their current settings. |
|---|---|

| Note | Common Phone Profiles are defined on the 
                                                                  						Common Phone Profile Configuration
                                                                  						window of Cisco Unified Communications Manager
                                                                  						( Device > Device
                                                                        							 Settings > Common Phone Profile ).
                                                                  						You can use the search fields and the Find button to
                                                                  						find all configured common phone profiles and their current settings. |
|---|---|

| Note | Calling Search Spaces are defined on the 
                                                                  						Calling Search Space Configuration
                                                                  						window of Cisco Unified Communications Manager ( Calling
                                                                        							 routing > Class of Control > Calling
                                                                        							 Search Space ). You can use the search fields and the Find button to find all configured
                                                                  						Calling Search Spaces and their current settings. |
|---|---|

| Note | The security profile chosen should be based on the overall
                                                            						security strategy of the company. |
|---|---|

| Note | This field should contain the same number that appears in
                                                            						the Telephone Number field on the 
                                                            						User Configuration window. |
|---|---|

| Step 1 | In the Directory Number Associations pane of the screen, set the
                                       			 primary extension from the drop-down list. |
|---|---|
| Step 2 | In the Mobility Information pane, check the Enable Mobility box. |
| Step 3 | In the Permissions Information pane, use the User Group buttons to
                                       			 add this user to any user groups. For example, you may want to add the user to
                                       			 a group that has been defined as a Standard CCM End User Group. To view all configured user groups, choose User Management > User
                                                					 Group . |
| Step 4 | Click Save . |