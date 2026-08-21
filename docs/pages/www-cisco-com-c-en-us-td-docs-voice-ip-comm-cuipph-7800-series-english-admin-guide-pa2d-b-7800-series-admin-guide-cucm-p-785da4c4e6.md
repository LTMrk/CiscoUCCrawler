---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-english-admin-guide-pa2d-b-7800-series-admin-guide-cucm-p-785da4c4e6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/english/admin-guide/pa2d_b_7800-series-admin-guide-cucm/pa2d_b_7800-series-admin-guide-cucm_chapter_0101.html
retrieved_at: 2026-08-21T13:26:13.453942+00:00
---

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Updated: May 29, 2025

Chapter: Cisco Unified Communications Manager Phone Setup

## Chapter: Cisco Unified Communications Manager Phone Setup

# Cisco Unified Communications Manager Phone Setup

## Set Up a Cisco IP Phone

If autoregistration is not enabled and the phone does not exist in the Cisco Unified Communications Manager database, you
                              must manually configure the Cisco IP Phone in Cisco Unified Communications Manager
                              		  Administration. Some tasks in this procedure are optional, depending on your system
                              		  and user needs.

For more information on any of the steps, see the documentation for your particular Cisco Unified Communications Manager release.

Perform the configuration steps in the following procedure using Cisco Unified Communications Manager Administration.

Step 1

Gather the following information about the phone:

Phone model

MAC address: see Determine the Phone MAC Address

Physical location of the phone

Name or user ID of phone user

Device pool

Partition, calling search space, and location information

Number of lines and associated directory numbers (DNs) to assign to the phone

Cisco Unified Communications Manager user to associate with
                                                					 the phone

Phone usage information that affects the phone button template, softkey template, phone features, IP Phone services, or phone
                                                applications

For more information, see 
                                          				the documentation for your particular Cisco Unified Communications Manager release and
                                          				see  
                                          				the related links.

Step 2

Verify that you have sufficient unit licenses for your phone.

For
                                          			 more information, see the licensing document for your particular Cisco Unified Communications Manager release.

Step 3

Define the phone button templates that determine the configuration of buttons on a phone. Select Device > Device Settings > Phone Button Template to create and update the templates.

For more information, see the documentation for your particular Cisco Unified Communications Manager release and the related
                                          links.

Step 4

Define the Device Pools. Select System > Device Pool .

Device Pools define common characteristics for devices, such as region, date/time group, softkey template, and MLPP information.

Step 5

Define the Common Phone Profile. Select Device > Device settings > Common Phone Profile .

Common phone profiles provide data that the Cisco TFTP server requires, as well as common phone settings, such as Do Not Disturb
                                          and feature control options.

Step 6

Define a Calling Search Space. In Cisco Unified Communications Manager Administration, click Call Routing > Class of Control > Calling Search Space .

A Calling Search Space is a collection of partitions that are searched to determine how a dialed number is routed. The calling
                                          search space for the device and the calling search space for the directory number are used together. The directory number
                                          CSS takes precedence over the device CSS.

Step 7

Configure a security profile for the device type and protocol. Select System > Security > Phone Security Profile .

Step 8

Set up the phone.  Select Device > Phone .

Locate the phone you want to modify, or add a new phone.

Configure the phone by completing the required fields in
                                             			 the 
                                             			 Device Information pane of the Phone Configuration window.

MAC Address (required): Make sure that the value comprises
                                                      12 hexadecimal characters.

Description: Enter a useful description to help  you if you need to search on information about
                                                      this user.

Device Pool
                                                      (required)

Phone Button Template: The phone button template determines the configuration of buttons on a phone.

Common Phone Profile

Calling Search Space

Location

Owner User ID

The device with its default settings is added to the Cisco
                                                			 Unified Communications Manager database.

For information about Product Specific Configuration fields, see the "?" Button Help in the Phone Configuration window.

If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the documentation for your particular Cisco Unified Communications
                                                            Manager release.

In the Protocol Specific Information area of this window, choose a Device Security Profile and set the security mode.

Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile.

In the Extension Information area, check the Enable Extension Mobility check box if this phone supports Cisco Extension Mobility.

Click Save .

Step 9

Select Device > Device Settings > SIP Profile to set up parameters such as Multilevel Precedence and Preemption (MLPP).

Step 10

Select Device > Phone to configure directory numbers (lines) on the phone by
                                       			 completing the required fields in the 
                                       			 Directory Number Configuration window.

Find the phone.

In the Phone Configuration window, click Line 1 on the left pane of the window.

In the Directory Number field, enter a valid number that can be dialed.

From the Route Partition drop-down list, choose the partition
                                             				  to which the directory number belongs. If you do not want to restrict access to
                                             				  the directory number, choose <None> for the partition.

From the Calling Search Space drop-down list, choose the
                                             				  appropriate calling search space. The value that you choose applies to all devices that are using this
                                             				  directory number.

In the Call Forward and Call Pickup Settings area, choose the items (for example, Forward
                                             				  All, Forward Busy Internal) and corresponding destinations to which calls
                                             				  should be sent.

### Example:

If you want incoming internal and external calls that receive a busy signal to forward to the voice mail for this line, check
                                                the Voice Mail check box
                                                								next to the Forward Busy Internal and Forward Busy
                                                									External items in the left column of the Call Pickup and
                                                								Call Forward Settings area.

In the 
                                             				  Line 1 on Device pane, configure the following fields:

Display (Internal Caller ID field): You can enter the first
                                                      						  name and last name of the user of this device so that this name displays for
                                                      						  all internal calls. Leave this field blank to have the system
                                                      						  display the phone extension.

External Phone Number Mask: Indicate phone number (or mask)
                                                      						  that is used to send Caller ID information when a call is placed from this
                                                      						  line. You can enter a maximum of 24 numeric and "X" characters. The Xs represent the directory number and
                                                      					 must appear at the end of the pattern.

### Example:

If you specify a mask of 408902XXXX, an external call from extension
                                                					 6640 displays a caller ID number of 4089026640.

This setting applies only to the current device unless you
                                                						check the check box at the right (Update Shared Device Settings) and click Propagate Selected . The check box at the
                                                						right displays only if other devices share this directory number.

Select Save .

For more information about directory numbers, see the documentation for your particular Cisco Unified Communications Manager
                                          release and the related links.

Step 11

Associate the user with a phone. Click Associate End Users at the bottom of the
                                       				  Phone Configuration window to associate a user to the line that is being configured.

Use Find in
                                             				  conjunction with the Search fields to locate the user.

check the box next
                                             				  to the user name, and click Add Selected .

The user name and user ID appears in the 
                                                				  Users Associated With Line pane of the Directory Number
                                                				  Configuration window.

Select Save .

The user is now associated with Line
                                                				  1 on the phone.

If the phone has a second line, configure Line 2.

Step 12

Associate the user with the device:

Choose User Management > End User .

Use the search boxes and Find to locate the user you have
                                             						  added.

Click on the user ID.

In the Directory Number Associations area of the screen, set the
                                             			 Primary Extension from the drop-down list.

(Optional) In the Mobility Information area, check the Enable Mobility box.

In the Permissions Information area, use the Add to Access Control Group buttons to
                                             			 add this user to any user groups.

For example, you may want to add the user to
                                                			 a group that is defined as a Standard CCM End User Group.

To view the details of a group, select the group and click View Details .

In the Extension Mobility area, check the Enable Extension
                                             			 Mobility Cross Cluster box if the user can use for Extension Mobility Cross
                                             			 Cluster service.

In the Device Information area, click Device Associations .

Use the Search fields and Find to
                                             						  locate the device that  you want to associate to the user.

Select the
                                             						  device, and click Save Selected/Changes .

Click Go next to the "Back to User" Related link in the upper right corner
                                             						  of the screen.

Select Save .

Step 13

Customize the softkey templates. Select Device > Device Settings > Softkey Template .

Use the page to add, delete, or change the order of
                                          			 softkey features that display on the user’s phone to meet feature usage needs.

Step 14

Configure speed-dial buttons and assign speed-dial numbers. Select Device > Phone .

Users can change speed-dial settings on their phones using their Self Care Portal.

Find the phone you want to set up.

In the Association Information area, click Add a new SD .

Set up the speed dial information.

Select Save .

Step 15

Configure Cisco IPPhone services
                                       			 and assign services. Select Device > Device Settings > Phone Services .

Provides IP Phone services to the phone.

Users can add or change services on their phones using the Cisco Unified Communications Self Care Portal.

Step 16

(Optional) Assign services to programmable buttons. Select Device > Device Settings > Phone button template .

Provides access to an IP phone service or URL.

Step 17

Add user information to the global directory for Cisco UnifiedCommunications
                                       			 Manager. Select User Management > End User , and then click Add New and configure the required fields. Required
                                       			 fields are indicated by an asterisk (*).

If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure
                                                      				  Cisco Unified Communications to use your existing LDAP directory, see Corporate Directory Setup . After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified Communications
                                                      				  Manager Administration.

Set the User ID and last name fields.

Assign a password (for Self Care Portal).

Assign a PIN (for
                                             				  Cisco Extension Mobility and Personal Directory).

Associate the user with a phone.

Provides
                                                			 users with control over their phone such as forwarding calls or adding
                                                			 speed-dial numbers or services.

Some phones, such as those in conference rooms, do not have an
                                                            				  associated user.

Step 18

Associate a user with a user group. Select User Management > User Settings > Access Control Group .

Assigns users a common list of
                                          			 roles and permissions that apply to all users in a user group. Administrators
                                          			 can manage user groups, roles, and permissions to control the level of access
                                          			 (and, therefore, the level of security) for system users. For more information, see Add a User to an End User Group .

In order for end users to access the  Cisco Unified Communications Self Care Portal, you must add users to the standard Cisco
                                          Communications
                                          				Manager End Users group.

## Determine the Phone
                        	 MAC Address

To add phones to Cisco Unified Communications Manager, you must determine the MAC address of a phone.

Perform one of
                                       			 the following actions:

On the phone, press Applications , select Phone Information and look at the MAC Address field.

Look at the MAC label on the back of the phone.

Display the web page for the phone and click Device Information .

## Phone Addition
                        	 Methods

After you
                           		install the Cisco IP Phone, you can choose one of the following options to add
                           		phones to the Cisco Unified Communications Manager database.

Add phones individually with Cisco Unified Communications Manager Administration

Add multiple phones with the Bulk Administration Tool (BAT)

Autoregistration

BAT and the Tool for Auto-Registered Phones Support (TAPS)

Before you add phones individually or with BAT, you need the MAC address of the phone. For more information, see Determine the Phone MAC Address .

For more
                           		information about the Bulk Administration Tool, see the documentation for your particular Cisco Unified Communications Manager
                           release.

### Add Phones Individually

Collect the MAC address and phone information for the phone that you will add to the Cisco Unified Communications Manager.

Step 1

In
                                          		Cisco Unified Communications Manager Administration, choose Device > Phone .

Step 2

Click Add New .

Step 3

Select the phone type.

Step 4

Select Next .

Step 5

Complete the information about the phone including the MAC Address.

For complete instructions and conceptual information about
                                             		Cisco Unified Communications Manager, see the 
                                             		documentation for your particular Cisco Unified Communications Manager release.

Step 6

Select Save .

### Add Phones with a BAT Phone Template

The Cisco Unified Communications Bulk Administration Tool
                                 		  (BAT) enables you to perform batch operations, including registration of
                                 		  multiple phones.

To add phones using BAT only (not in conjunction with TAPS),
                                 		  you must obtain the appropriate MAC address for each phone.

For more information about using BAT, see the documentation for your particular Cisco Unified Communications Manager release.

Step 1

From Cisco Unified Communications Administration, choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template .

Step 2

Click Add New .

Step 3

Choose a Phone Type and click Next .

Step 4

Enter the details of phone-specific parameters, such as Device Pool, Phone Button Template, and Device Security Profile.

Step 5

Click Save .

Step 6

Select Device > Phone > Add
                                                				  New to add a phone using the BAT phone
                                          			 template.

## Add Users to Cisco Unified Communications Manager

You can display and maintain information about the users registered in Cisco Unified Communications Manager. Cisco Unified
                              Communications Manager also allows each user to
                              		  perform these tasks:

Access the corporate
                                    			 directory and other customized directories from a Cisco IP Phone.

Create a personal
                                    			 directory.

Set up speed dial and call
                                    			 forwarding numbers.

Subscribe to services that
                                    			 are accessible from a Cisco IP Phone.

Step 1

To add users individually,
                                       			 see Add a User Directly to Cisco Unified Communications Manager .

Step 2

To add users in batches,
                                       			 use the Bulk Administration Tool. This method also enables you to set an
                                       			 identical default password for all users.

For more information, see the 
                                          				documentation for your particular Cisco Unified Communications Manager release.

### Add a User from an External LDAP Directory

If you added a user to an LDAP Directory (a non-Cisco Unified
                                 		  Communications Server directory), you can immediately synchronize the LDAP
                                 		  directory to the Cisco Unified Communications Manager on which you are adding
                                 		  the user and the user phone.

If you do not synchronize the LDAP Directory
                                             				  to the Cisco Unified Communications Manager immediately, the LDAP Directory Synchronization
                                             				  Schedule on the LDAP Directory window determines when the next
                                             				  autosynchronization is scheduled. Synchronization must occur
                                             				  before you can associate a new user to a device.

Step 1

Sign into Cisco Unified Communications Manager Administration.

Step 2

Select System > LDAP > LDAP
                                                				  Directory .

Step 3

Use Find to locate your LDAP directory.

Step 4

Click on the LDAP directory name.

Step 5

Click Perform Full Sync Now .

### Add a User Directly to Cisco Unified Communications Manager

If you
                                 		  are not using a Lightweight Directory Access Protocol (LDAP) directory, you can
                                 		  add a user directly with Cisco Unified Communications Manager Administration by
                                 		  following these steps.

If LDAP is
                                             			 synchronized, you cannot add a user with Cisco Unified Communications Manager
                                             			 Administration.

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, choose User
                                                				  Management > End User .

Step 2

Click Add
                                             				New .

Step 3

In the User
                                          			 Information pane, enter the following:

User ID:
                                                   					 Enter the end user identification name. Cisco Unified Communications Manager
                                                   					 does not permit modifying the user ID after it is created. You may use the
                                                   					 following special characters: =, +, <, >, #,;, \,, "" , and blank spaces. Example : johndoe

Password
                                                   					 and Confirm Password: Enter five or more alphanumeric or special characters for
                                                   					 the end user password. You may use the following special characters: =, +,
                                                   					 <, >, #, ;, \, , "" , and blank spaces.

Last Name:
                                                   					 Enter the end user last name. You may use the following special characters: =,
                                                   					 +, <, >, #, ;, \, , "" , and blank spaces. Example : doe

Telephone
                                                   					 Number: Enter the primary directory number for the end user. End users can have
                                                   					 multiple lines on their phones. Example : 26640 (John Doe’s internal company telephone
                                                   					 number)

Step 4

Click Save .

## Add a User to an End User Group

To add a user to the Cisco Unified Communications
                              		  Manager Standard End User group, perform these steps:

Step 1

From Cisco Unified Communications Manager Administration, choose User Management > User
                                             				  Settings > Access Control Group .

The Find and List Users window displays.

Step 2

Enter the appropriate search criteria and click Find .

Step 3

Select the Standard CCM End Users link. The User Group
                                       			 Configuration window for the Standard CCM End Users appears.

Step 4

Select Add End Users to Group . The Find and List
                                       			 Users window appears.

Step 5

Use the Find User drop-down list boxes to find the users that
                                       			 you want to add and click Find .

A list of users that matches your search criteria appears.

Step 6

In the list of records that appear, click the check box next to
                                       			 the users that you want to add to this user group. If the list is long, use the links at the bottom to see more results.

The list of search results does not display users that
                                                      				  already belong to the user group.

Step 7

Choose Add Selected .

## Associate Phones with Users

You associate phones with users from the Cisco Unified
                              		  Communications Manager End User window.

Step 1

From Cisco Unified Communications Manager Administration,
                                       			 choose User Management > End
                                             				  User .

The Find and List Users window appears.

Step 2

Enter the appropriate search criteria and click Find .

Step 3

In the list of records that appear, select the link for the user.

Step 4

Select Device Association .

The User Device Association window appears.

Step 5

Enter the appropriate search criteria and click Find .

Step 6

Choose the device that you want to associate with the user by
                                       			 checking the box to the left of the device.

Step 7

Choose Save Selected/Changes to associate the device
                                       			 with the user.

Step 8

From the Related Links drop-down list in the upper, right corner of
                                       			 the window, select Back to User , and click Go .

The End User Configuration window appears and the associated
                                          				devices that you chose display in the Controlled Devices pane.

Step 9

Choose Save Selected/Changes .

## Surviveable Remote
                        	 Site Telephony

Survivable Remote Site Telephony (SRST) ensures that basic phone
                              		  functions remain accessible when communications with the controlling Cisco
                              		  Unified Communications Manager are broken. In this scenario, the phone can keep
                              		  an in-progress call active, and the user can access a subset of the features
                              		  available. When failover occurs, the user receives an alert message on the
                              		  phone.

The following table describes the availability of features during
                              		  failover.

Feature

Supported

Notes

New Call

Yes

End Call

Yes

Redial

Yes

Answer

Yes

Hold

Yes

Resume

Yes

Conference

Yes

3 way only and local mixing only.

Conference List

No

Transfer

Yes

Consult only.

Transfer to Active Calls (Direct Transfer)

No

Auto Answer

Yes

Call Waiting

Yes

Caller ID

Yes

Unified Session Presentation

Yes

Conference is the only feature supported due to other feature limitations.

Voicemail

Yes

Voicemail will not be synchronized with other users in the Cisco Unified Communications Manager cluster.

Call Forward All

Yes

Forward state is only available on the phone that sets the forward because there are no shared line appearances in SRST mode.
                                          The Call Forward All settings are not preserved on failover to SRST from the Cisco Unified Communications Manager, or from
                                          SRST fail-back to the Communications Manager. Any original Call Forward All still active on the Communications Manager should
                                          be indicated when the device reconnects to the Communications Manager after failover.

Speed Dial

Yes

To Voicemail (iDivert)

No

The iDivert softkey does not display.

Line Filters

Partial

Lines are supported but cannot be shared.

Park Monitoring

No

The Park softkey does not display.

Enhanced Message Waiting Indication

No

Message count badges do not appear on the phone screen.

Only the Message Waiting icon displays.

Directed Call Park

No

The softkey does not display.

BLF

Partial

BLF feature key works like Speed Dial keys.

Hold Reversion

No

Calls remain on hold indefinitely.

Remote Hold

No

Calls appear as Local Hold calls.

Meet Me

No

The Meet Me softkey does not display.

PickUp

No

The softkey causes no action.

Group PickUp

No

The softkey causes no action.

Other PickUp

No

The softkey causes no action.

Malicious Call ID

No

The softkey causes no action.

QRT

No

The softkey causes no action.

Hunt Group

No

The softkey causes no action.

Intercom

No

The softkey causes no action.

Mobility

No

The softkey causes no action.

Privacy

No

The softkey causes no action.

Call Back

No

The Call Back softkey does not display.

Service URL

Yes

The programmable line key with a Service URL assigned is displayed.

| Step 1 | Gather the following information about the phone: Phone model MAC address: see Determine the Phone MAC Address Physical location of the phone Name or user ID of phone user Device pool Partition, calling search space, and location information Number of lines and associated directory numbers (DNs) to assign to the phone Cisco Unified Communications Manager user to associate with
                                                					 the phone Phone usage information that affects the phone button template, softkey template, phone features, IP Phone services, or phone
                                                applications For more information, see 
                                          				the documentation for your particular Cisco Unified Communications Manager release and
                                          				see  
                                          				the related links. |
|---|---|
| Step 2 | Verify that you have sufficient unit licenses for your phone. For
                                          			 more information, see the licensing document for your particular Cisco Unified Communications Manager release. |
| Step 3 | Define the phone button templates that determine the configuration of buttons on a phone. Select Device > Device Settings > Phone Button Template to create and update the templates. For more information, see the documentation for your particular Cisco Unified Communications Manager release and the related
                                          links. |
| Step 4 | Define the Device Pools. Select System > Device Pool . Device Pools define common characteristics for devices, such as region, date/time group, softkey template, and MLPP information. |
| Step 5 | Define the Common Phone Profile. Select Device > Device settings > Common Phone Profile . Common phone profiles provide data that the Cisco TFTP server requires, as well as common phone settings, such as Do Not Disturb
                                          and feature control options. |
| Step 6 | Define a Calling Search Space. In Cisco Unified Communications Manager Administration, click Call Routing > Class of Control > Calling Search Space . A Calling Search Space is a collection of partitions that are searched to determine how a dialed number is routed. The calling
                                          search space for the device and the calling search space for the directory number are used together. The directory number
                                          CSS takes precedence over the device CSS. |
| Step 7 | Configure a security profile for the device type and protocol. Select System > Security > Phone Security Profile . |
| Step 8 | Set up the phone.  Select Device > Phone . Locate the phone you want to modify, or add a new phone. Configure the phone by completing the required fields in
                                             			 the 
                                             			 Device Information pane of the Phone Configuration window. MAC Address (required): Make sure that the value comprises
                                                      12 hexadecimal characters. Description: Enter a useful description to help  you if you need to search on information about
                                                      this user. Device Pool
                                                      (required) Phone Button Template: The phone button template determines the configuration of buttons on a phone. Common Phone Profile Calling Search Space Location Owner User ID The device with its default settings is added to the Cisco
                                                			 Unified Communications Manager database. For information about Product Specific Configuration fields, see the "?" Button Help in the Phone Configuration window. Note If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the documentation for your particular Cisco Unified Communications
                                                            Manager release. In the Protocol Specific Information area of this window, choose a Device Security Profile and set the security mode. Note Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile. In the Extension Information area, check the Enable Extension Mobility check box if this phone supports Cisco Extension Mobility. Click Save . | Note | If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the documentation for your particular Cisco Unified Communications
                                                            Manager release. | Note | Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile. |
| Note | If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the documentation for your particular Cisco Unified Communications
                                                            Manager release. |
| Note | Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile. |
| Step 9 | Select Device > Device Settings > SIP Profile to set up parameters such as Multilevel Precedence and Preemption (MLPP). |
| Step 10 | Select Device > Phone to configure directory numbers (lines) on the phone by
                                       			 completing the required fields in the 
                                       			 Directory Number Configuration window. Find the phone. In the Phone Configuration window, click Line 1 on the left pane of the window. In the Directory Number field, enter a valid number that can be dialed. Note This field should contain the same number that appears in the Telephone Number field in the End User Configuration window. From the Route Partition drop-down list, choose the partition
                                             				  to which the directory number belongs. If you do not want to restrict access to
                                             				  the directory number, choose <None> for the partition. From the Calling Search Space drop-down list, choose the
                                             				  appropriate calling search space. The value that you choose applies to all devices that are using this
                                             				  directory number. In the Call Forward and Call Pickup Settings area, choose the items (for example, Forward
                                             				  All, Forward Busy Internal) and corresponding destinations to which calls
                                             				  should be sent. Example: If you want incoming internal and external calls that receive a busy signal to forward to the voice mail for this line, check
                                                the Voice Mail check box
                                                								next to the Forward Busy Internal and Forward Busy
                                                									External items in the left column of the Call Pickup and
                                                								Call Forward Settings area. In the 
                                             				  Line 1 on Device pane, configure the following fields: Display (Internal Caller ID field): You can enter the first
                                                      						  name and last name of the user of this device so that this name displays for
                                                      						  all internal calls. Leave this field blank to have the system
                                                      						  display the phone extension. External Phone Number Mask: Indicate phone number (or mask)
                                                      						  that is used to send Caller ID information when a call is placed from this
                                                      						  line. You can enter a maximum of 24 numeric and "X" characters. The Xs represent the directory number and
                                                      					 must appear at the end of the pattern. Example: If you specify a mask of 408902XXXX, an external call from extension
                                                					 6640 displays a caller ID number of 4089026640. This setting applies only to the current device unless you
                                                						check the check box at the right (Update Shared Device Settings) and click Propagate Selected . The check box at the
                                                						right displays only if other devices share this directory number. Select Save . For more information about directory numbers, see the documentation for your particular Cisco Unified Communications Manager
                                          release and the related links. | Note | This field should contain the same number that appears in the Telephone Number field in the End User Configuration window. |
| Note | This field should contain the same number that appears in the Telephone Number field in the End User Configuration window. |
| Step 11 | Associate the user with a phone. Click Associate End Users at the bottom of the
                                       				  Phone Configuration window to associate a user to the line that is being configured. Use Find in
                                             				  conjunction with the Search fields to locate the user. check the box next
                                             				  to the user name, and click Add Selected . The user name and user ID appears in the 
                                                				  Users Associated With Line pane of the Directory Number
                                                				  Configuration window. Select Save . The user is now associated with Line
                                                				  1 on the phone. If the phone has a second line, configure Line 2. |
| Step 12 | Associate the user with the device: Choose User Management > End User . Use the search boxes and Find to locate the user you have
                                             						  added. Click on the user ID. In the Directory Number Associations area of the screen, set the
                                             			 Primary Extension from the drop-down list. (Optional) In the Mobility Information area, check the Enable Mobility box. In the Permissions Information area, use the Add to Access Control Group buttons to
                                             			 add this user to any user groups. For example, you may want to add the user to
                                                			 a group that is defined as a Standard CCM End User Group. To view the details of a group, select the group and click View Details . In the Extension Mobility area, check the Enable Extension
                                             			 Mobility Cross Cluster box if the user can use for Extension Mobility Cross
                                             			 Cluster service. In the Device Information area, click Device Associations . Use the Search fields and Find to
                                             						  locate the device that  you want to associate to the user. Select the
                                             						  device, and click Save Selected/Changes . Click Go next to the "Back to User" Related link in the upper right corner
                                             						  of the screen. Select Save . |
| Step 13 | Customize the softkey templates. Select Device > Device Settings > Softkey Template . Use the page to add, delete, or change the order of
                                          			 softkey features that display on the user’s phone to meet feature usage needs. |
| Step 14 | Configure speed-dial buttons and assign speed-dial numbers. Select Device > Phone . Note Users can change speed-dial settings on their phones using their Self Care Portal. Find the phone you want to set up. In the Association Information area, click Add a new SD . Set up the speed dial information. Select Save . | Note | Users can change speed-dial settings on their phones using their Self Care Portal. |
| Note | Users can change speed-dial settings on their phones using their Self Care Portal. |
| Step 15 | Configure Cisco IPPhone services
                                       			 and assign services. Select Device > Device Settings > Phone Services . Provides IP Phone services to the phone. Note Users can add or change services on their phones using the Cisco Unified Communications Self Care Portal. | Note | Users can add or change services on their phones using the Cisco Unified Communications Self Care Portal. |
| Note | Users can add or change services on their phones using the Cisco Unified Communications Self Care Portal. |
| Step 16 | (Optional) Assign services to programmable buttons. Select Device > Device Settings > Phone button template . Provides access to an IP phone service or URL. |
| Step 17 | Add user information to the global directory for Cisco UnifiedCommunications
                                       			 Manager. Select User Management > End User , and then click Add New and configure the required fields. Required
                                       			 fields are indicated by an asterisk (*). Note If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure
                                                      				  Cisco Unified Communications to use your existing LDAP directory, see Corporate Directory Setup . After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified Communications
                                                      				  Manager Administration. Set the User ID and last name fields. Assign a password (for Self Care Portal). Assign a PIN (for
                                             				  Cisco Extension Mobility and Personal Directory). Associate the user with a phone. Provides
                                                			 users with control over their phone such as forwarding calls or adding
                                                			 speed-dial numbers or services. Note Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. | Note | If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure
                                                      				  Cisco Unified Communications to use your existing LDAP directory, see Corporate Directory Setup . After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified Communications
                                                      				  Manager Administration. | Note | Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. |
| Note | If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure
                                                      				  Cisco Unified Communications to use your existing LDAP directory, see Corporate Directory Setup . After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified Communications
                                                      				  Manager Administration. |
| Note | Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. |
| Step 18 | Associate a user with a user group. Select User Management > User Settings > Access Control Group . Assigns users a common list of
                                          			 roles and permissions that apply to all users in a user group. Administrators
                                          			 can manage user groups, roles, and permissions to control the level of access
                                          			 (and, therefore, the level of security) for system users. For more information, see Add a User to an End User Group . In order for end users to access the  Cisco Unified Communications Self Care Portal, you must add users to the standard Cisco
                                          Communications
                                          				Manager End Users group. |

| Note | If you want to add both the phone and user to the Cisco Unified
                                                            				  Communications Manager database at the same time, see the documentation for your particular Cisco Unified Communications
                                                            Manager release. |
|---|---|

| Note | Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile. |
|---|---|

| Note | This field should contain the same number that appears in the Telephone Number field in the End User Configuration window. |
|---|---|

| Note | Users can change speed-dial settings on their phones using their Self Care Portal. |
|---|---|

| Note | Users can add or change services on their phones using the Cisco Unified Communications Self Care Portal. |
|---|---|

| Note | If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure
                                                      				  Cisco Unified Communications to use your existing LDAP directory, see Corporate Directory Setup . After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified Communications
                                                      				  Manager Administration. |
|---|---|

| Note | Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. |
|---|---|

| Perform one of
                                       			 the following actions: On the phone, press Applications , select Phone Information and look at the MAC Address field. Look at the MAC label on the back of the phone. Display the web page for the phone and click Device Information . |
|---|

| Step 1 | In
                                          		Cisco Unified Communications Manager Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Select the phone type. |
| Step 4 | Select Next . |
| Step 5 | Complete the information about the phone including the MAC Address. For complete instructions and conceptual information about
                                             		Cisco Unified Communications Manager, see the 
                                             		documentation for your particular Cisco Unified Communications Manager release. |
| Step 6 | Select Save . |

| Step 1 | From Cisco Unified Communications Administration, choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Choose a Phone Type and click Next . |
| Step 4 | Enter the details of phone-specific parameters, such as Device Pool, Phone Button Template, and Device Security Profile. |
| Step 5 | Click Save . |
| Step 6 | Select Device > Phone > Add
                                                				  New to add a phone using the BAT phone
                                          			 template. |

| Step 1 | To add users individually,
                                       			 see Add a User Directly to Cisco Unified Communications Manager . |
|---|---|
| Step 2 | To add users in batches,
                                       			 use the Bulk Administration Tool. This method also enables you to set an
                                       			 identical default password for all users. For more information, see the 
                                          				documentation for your particular Cisco Unified Communications Manager release. |

| Note | If you do not synchronize the LDAP Directory
                                             				  to the Cisco Unified Communications Manager immediately, the LDAP Directory Synchronization
                                             				  Schedule on the LDAP Directory window determines when the next
                                             				  autosynchronization is scheduled. Synchronization must occur
                                             				  before you can associate a new user to a device. |
|---|---|

| Step 1 | Sign into Cisco Unified Communications Manager Administration. |
|---|---|
| Step 2 | Select System > LDAP > LDAP
                                                				  Directory . |
| Step 3 | Use Find to locate your LDAP directory. |
| Step 4 | Click on the LDAP directory name. |
| Step 5 | Click Perform Full Sync Now . |

| Note | If LDAP is
                                             			 synchronized, you cannot add a user with Cisco Unified Communications Manager
                                             			 Administration. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, choose User
                                                				  Management > End User . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | In the User
                                          			 Information pane, enter the following: User ID:
                                                   					 Enter the end user identification name. Cisco Unified Communications Manager
                                                   					 does not permit modifying the user ID after it is created. You may use the
                                                   					 following special characters: =, +, <, >, #,;, \,, "" , and blank spaces. Example : johndoe Password
                                                   					 and Confirm Password: Enter five or more alphanumeric or special characters for
                                                   					 the end user password. You may use the following special characters: =, +,
                                                   					 <, >, #, ;, \, , "" , and blank spaces. Last Name:
                                                   					 Enter the end user last name. You may use the following special characters: =,
                                                   					 +, <, >, #, ;, \, , "" , and blank spaces. Example : doe Telephone
                                                   					 Number: Enter the primary directory number for the end user. End users can have
                                                   					 multiple lines on their phones. Example : 26640 (John Doe’s internal company telephone
                                                   					 number) |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration, choose User Management > User
                                             				  Settings > Access Control Group . The Find and List Users window displays. |
|---|---|
| Step 2 | Enter the appropriate search criteria and click Find . |
| Step 3 | Select the Standard CCM End Users link. The User Group
                                       			 Configuration window for the Standard CCM End Users appears. |
| Step 4 | Select Add End Users to Group . The Find and List
                                       			 Users window appears. |
| Step 5 | Use the Find User drop-down list boxes to find the users that
                                       			 you want to add and click Find . A list of users that matches your search criteria appears. |
| Step 6 | In the list of records that appear, click the check box next to
                                       			 the users that you want to add to this user group. If the list is long, use the links at the bottom to see more results. Note The list of search results does not display users that
                                                      				  already belong to the user group. | Note | The list of search results does not display users that
                                                      				  already belong to the user group. |
| Note | The list of search results does not display users that
                                                      				  already belong to the user group. |
| Step 7 | Choose Add Selected . |

| Note | The list of search results does not display users that
                                                      				  already belong to the user group. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration,
                                       			 choose User Management > End
                                             				  User . The Find and List Users window appears. |
|---|---|
| Step 2 | Enter the appropriate search criteria and click Find . |
| Step 3 | In the list of records that appear, select the link for the user. |
| Step 4 | Select Device Association . The User Device Association window appears. |
| Step 5 | Enter the appropriate search criteria and click Find . |
| Step 6 | Choose the device that you want to associate with the user by
                                       			 checking the box to the left of the device. |
| Step 7 | Choose Save Selected/Changes to associate the device
                                       			 with the user. |
| Step 8 | From the Related Links drop-down list in the upper, right corner of
                                       			 the window, select Back to User , and click Go . The End User Configuration window appears and the associated
                                          				devices that you chose display in the Controlled Devices pane. |
| Step 9 | Choose Save Selected/Changes . |

| Feature | Supported | Notes |
|---|---|---|
| New Call | Yes |  |
| End Call | Yes |  |
| Redial | Yes |  |
| Answer | Yes |  |
| Hold | Yes |  |
| Resume | Yes |  |
| Conference | Yes | 3 way only and local mixing only. |
| Conference List | No |  |
| Transfer | Yes | Consult only. |
| Transfer to Active Calls (Direct Transfer) | No |  |
| Auto Answer | Yes |  |
| Call Waiting | Yes |  |
| Caller ID | Yes |  |
| Unified Session Presentation | Yes | Conference is the only feature supported due to other feature limitations. |
| Voicemail | Yes | Voicemail will not be synchronized with other users in the Cisco Unified Communications Manager cluster. |
| Call Forward All | Yes | Forward state is only available on the phone that sets the forward because there are no shared line appearances in SRST mode.
                                          The Call Forward All settings are not preserved on failover to SRST from the Cisco Unified Communications Manager, or from
                                          SRST fail-back to the Communications Manager. Any original Call Forward All still active on the Communications Manager should
                                          be indicated when the device reconnects to the Communications Manager after failover. |
| Speed Dial | Yes |  |
| To Voicemail (iDivert) | No | The iDivert softkey does not display. |
| Line Filters | Partial | Lines are supported but cannot be shared. |
| Park Monitoring | No | The Park softkey does not display. |
| Enhanced Message Waiting Indication | No | Message count badges do not appear on the phone screen. Only the Message Waiting icon displays. |
| Directed Call Park | No | The softkey does not display. |
| BLF | Partial | BLF feature key works like Speed Dial keys. |
| Hold Reversion | No | Calls remain on hold indefinitely. |
| Remote Hold | No | Calls appear as Local Hold calls. |
| Meet Me | No | The Meet Me softkey does not display. |
| PickUp | No | The softkey causes no action. |
| Group PickUp | No | The softkey causes no action. |
| Other PickUp | No | The softkey causes no action. |
| Malicious Call ID | No | The softkey causes no action. |
| QRT | No | The softkey causes no action. |
| Hunt Group | No | The softkey causes no action. |
| Intercom | No | The softkey causes no action. |
| Mobility | No | The softkey causes no action. |
| Privacy | No | The softkey causes no action. |
| Call Back | No | The Call Back softkey does not display. |
| Service URL | Yes | The programmable line key with a Service URL assigned is displayed. |