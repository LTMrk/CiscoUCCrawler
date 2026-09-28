---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-10-0-english-admin-guide-ip05-bk-a6e3f5ab-00-adminguide-3905-10--03d14925ea
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/10_0/english/admin_guide/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0_chapter_0100.html
retrieved_at: 2026-08-21T14:35:04.785054+00:00
---

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

# Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

Updated: May 9, 2025

Chapter: Cisco Unified Communications Manager Phone Setup

## Chapter: Cisco Unified Communications Manager Phone Setup

# Cisco Unified Communications Manager Phone Setup

## Phone
                        	 Configuration Files

Configuration files for a phone are stored on the TFTP server
                           		and define parameters for connecting to Cisco Unified
                              				Communications Manager . In general, any time you make a
                           		change in Cisco Unified
                              				Communications Manager that requires the phone to be reset,
                           		a change is automatically made to the phone configuration file.

Configuration files also contain information about which image
                           		load the phone should be running. If this image load differs from the one
                           		currently loaded on a phone, the phone contacts the TFTP server to request the
                           		required load files.

If you
                           		configure security-related settings in Cisco Unified
                              				Communications Manager Administration , the phone configuration file will
                           		contain sensitive information. To ensure the privacy of a configuration file,
                           		you must configure it for encryption. For more information, see the documentation for your particular Cisco Unified Communications
                           Manager release. A phone
                           		requests a configuration file whenever it resets and registers with Cisco Unified
                              				Communications Manager .

A phone
                           		accesses a default configuration file named XmlDefault.cnf.xml from the TFTP
                           		server when the following conditions exist:

You have enabled
                                 			 autoregistration in Cisco Unified
                                    				Communications Manager

The phone has
                                 			 not been added to the Cisco Unified
                                    				Communications Manager database

The phone is
                                 			 registering for the first time

## Set Up Cisco Unified SIP Phone

If autoregistration is not enabled and the phone does not exist in the Cisco Unified
                                 				Communications Manager database, you must configure the Cisco IP Phone in Cisco Unified
                                 				Communications Manager manually. Some tasks in this procedure are optional, depending on your system and user needs.

For more information about Cisco Unified
                                 				Communications Manager Administration , see Cisco Unified
                                    				Communications Manager Administration Guide .

Perform the configuration steps in the following procedure using Cisco Unified
                                 				Communications Manager Administration .

Step 1

Gather the following information about the phone:

Phone model

MAC address

Physical location of the phone

Name or user ID of phone user

Device pool

Partition, calling search space, and location information

Associated directory number (DN) to assign to the phone

Cisco Unified
                                                   				Communications Manager user to associate with
                                                					 the phone

The information provides a list of configuration requirements for
                                          				setting up phones and identifies preliminary configuration that you need to
                                          				perform before configuring individual phones.

For more information, see the "CiscoUnified IP Phones" chapter in the Cisco Unified
                                                				Communications Manager System Guide and Telephony Features .

Step 2

Verify that you have sufficient unit licenses for your phone.

For more information, go to the "License Unit Report" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide .

Step 3

Define the  phone button templates that determine the configuration of buttons on a phone. Select Device > Device
                                             Settings > Phone Button Template to create and update the templates.

For more information, see the "Phone button template setup" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide .

Step 4

Define the Device Pools. Select System > Device Pool .

Device Pools define common characteristics for devices,
                                          such as region, date/time group, softkey template, and
                                          MLPP information. For information on Device Pool setup, see the "Device pool setup" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide .

Step 5

Define the Common Phone Profile. Select Device > Device settings > Common Phone Profile .

Common phone profiles provide data that the Cisco TFTP server requires, as well as common phone settings, such as Do Not Disturb
                                          and feature control options. For more information, see the "Common phone profile setup" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide .

Step 6

Define a Calling Search Space. In Cisco Unified
                                          				Communications Manager Administration , click Call Routing > Class of Control > Calling Search Space .

A Calling Search Space is a collection of partitions that are searched to determine how a dialed number is routed. The calling
                                          search space for the device and the calling search space for the directory number are used together. The directory number
                                          CSS takes precedence over the device CSS. For more information, see the "Calling search space setup" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide .

Step 7

Configure a security profile for the device type and protocol. Select System > Security > Phone Security Profile .

For more information, see the "Phone security profile setup" chapter in the Cisco Unified
                                                				Communications Manager Security Guide .

Step 8

Set up the phone.  Select Device > Phone .

Locate the phone you want to modify or add a new phone.

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

The device with its default settings is added to the Cisco Unified
                                                   				Communications Manager database.

For information about Product Specific Configuration fields, see 
                                                				the "?" Button Help in the Phone
                                                				  Configuration window.

If you want to add both the phone and user to the Cisco Unified
                                                               				Communications Manager database at the same time, see "End user phone addition" chapter in the Cisco Unified
                                                                  				Communications Manager Guide .

In the Protocol Specific Information area of this window, choose a Device Security Profile and set the security mode.

Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile.

In the Extension Information area, check the Enable Extension Mobility check box if this phone supports Cisco Extension Mobility.

Click Save .

Step 9

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

For more information, see 
                                          				the "Directory number setup" chapter in the Cisco Unified
                                                				Communications Manager Administration
                                             				  Guide and see Telephony Features .

Step 10

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

Select Save .

The user is now associated with Line
                                                				  1 on the phone.

If the phone has a second line, configure Line 2.

Step 11

Associate the user with the device:

Choose User Management > End User .

Use the search boxes and Find to locate the user you have
                                             						  added.

Click on the user ID.

In the Directory Number Associations area of the screen, set the
                                             			 Primary Extension from the drop-down list.

In the Mobility Information area, check the Enable Mobility box.

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

Step 12

Customize the softkey templates. Select Device > Device Settings > Softkey Template .

Use the page to add, delete, or change the order of
                                          			 softkey features that display on the user’s phone to meet feature usage needs.

For more information, see the "Softkey template setup" and "Cisco UnifiedIPPhone setup" chapters in the Cisco Unified
                                                				Communications Manager Administration
                                             				  Guide .

Step 13

Configure speed-dial buttons and assign
                                       			 speed-dial numbers. Select Device > Phone .

Users can change
                                                      			 speed-dial settings on their phones using their Self Care Portal .

Find the phone you want to set up.

In the Association Information area, click Add a new SD .

Set up the speed dial information.

Select Save .

Step 14

Configure Cisco IPPhone services
                                       			 and assign services. Select Device > Device Settings > Phone Services .

Provides IP Phone services to the phone.

Users can add or change services on their phones using the Cisco Unified
                                                         				Communications Self Care Portal .

Step 15

(Optional) Assign services to programmable buttons.  
                                       		  Select Device > Device Settings > Phone Button Profile .

Provides
                                          			 access to an IP phone service or URL.

Step 16

Add user information to the global directory for Cisco Unified
                                          				Communications Manager . Select User Management > End User and configure the required fields. Required
                                       			 fields are indicated by an asterisk (*); for example, User ID and last name.

If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure Cisco Unified
                                                         				Communications Manager to use your existing LDAP directory, see "Understanding
                                                         		  Directory Numbers" in the Cisco Unified
                                                         		  Communications Manager System Guide . 
                                                      	  After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified
                                                         				Communications Manager Administration .

If you want to add both the phone and user to the Cisco Unified
                                                         				Communications Manager database at the same time, see "End user phone addition" in Cisco Unified
                                                            				Communications Manager Administration
                                                         					 Guide .

Set the User ID and last name fields.

Assign a password (for Self Care Portal).

Assign a PIN (for
                                             				  Cisco Extension Mobility and Personal Directory).

Associate the user with a phone.

Provides
                                                			 users with control over their phone such a forwarding calls or adding speed-dial numbers or services.

Some phones, such as those in conference rooms, do not have an
                                                            				  associated user.

Step 17

Associate a user with a user group. Select User Management > User Settings > Access Control Group .

Assigns users a common list of
                                          			 roles and permissions that apply to all users in a user group. Administrators
                                          			 can manage user groups, roles, and permissions to control the level of access
                                          			 (and, therefore, the level of security) for system users. For more information, see Add a User to an End User Group .

In order for end users to access the Cisco Unified
                                             				Communications Self Care Portal , you must add users to the standard Cisco Communications
                                          				Manager End Users group.

For more information, see "End user setup" and "Access control group setup" in the Cisco Unified
                                                				Communications Manager Administration
                                             				  Guide .

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

## Perform Final End User Configuration Steps

If you are not already on the End User Configuration page,
                              		  choose User Management > End
                                    				User to perform some final configuration tasks. Use
                              		  the Search fields and Find to locate the user (for
                              		  example, John Doe), then click on the user ID to get to the End User Configuration window for the user.

In the 
                              		  End User configuration window, do the following:

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

| Step 1 | Gather the following information about the phone: Phone model MAC address Physical location of the phone Name or user ID of phone user Device pool Partition, calling search space, and location information Associated directory number (DN) to assign to the phone Cisco Unified
                                                   				Communications Manager user to associate with
                                                					 the phone The information provides a list of configuration requirements for
                                          				setting up phones and identifies preliminary configuration that you need to
                                          				perform before configuring individual phones. For more information, see the "CiscoUnified IP Phones" chapter in the Cisco Unified
                                                				Communications Manager System Guide and Telephony Features . |
|---|---|
| Step 2 | Verify that you have sufficient unit licenses for your phone. For more information, go to the "License Unit Report" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide . |
| Step 3 | Define the  phone button templates that determine the configuration of buttons on a phone. Select Device > Device
                                             Settings > Phone Button Template to create and update the templates. For more information, see the "Phone button template setup" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide . |
| Step 4 | Define the Device Pools. Select System > Device Pool . Device Pools define common characteristics for devices,
                                          such as region, date/time group, softkey template, and
                                          MLPP information. For information on Device Pool setup, see the "Device pool setup" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide . |
| Step 5 | Define the Common Phone Profile. Select Device > Device settings > Common Phone Profile . Common phone profiles provide data that the Cisco TFTP server requires, as well as common phone settings, such as Do Not Disturb
                                          and feature control options. For more information, see the "Common phone profile setup" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide . |
| Step 6 | Define a Calling Search Space. In Cisco Unified
                                          				Communications Manager Administration , click Call Routing > Class of Control > Calling Search Space . A Calling Search Space is a collection of partitions that are searched to determine how a dialed number is routed. The calling
                                          search space for the device and the calling search space for the directory number are used together. The directory number
                                          CSS takes precedence over the device CSS. For more information, see the "Calling search space setup" chapter in the Cisco Unified
                                                				Communications Manager Administration Guide . |
| Step 7 | Configure a security profile for the device type and protocol. Select System > Security > Phone Security Profile . For more information, see the "Phone security profile setup" chapter in the Cisco Unified
                                                				Communications Manager Security Guide . |
| Step 8 | Set up the phone.  Select Device > Phone . Locate the phone you want to modify or add a new phone. Configure the phone by completing the required fields in
                                             			 the 
                                             			 Device Information pane of the Phone Configuration window. MAC Address (required): Make sure that the value comprises
                                                      12 hexadecimal characters. Description: Enter a useful description to help  you if you need to search on information about
                                                      this user. Device Pool
                                                      (required) Phone Button Template: The phone button template determines the configuration of buttons on a phone. Common Phone Profile Calling Search Space Location Owner User ID The device with its default settings is added to the Cisco Unified
                                                   				Communications Manager database. For information about Product Specific Configuration fields, see 
                                                				the "?" Button Help in the Phone
                                                				  Configuration window. Note If you want to add both the phone and user to the Cisco Unified
                                                               				Communications Manager database at the same time, see "End user phone addition" chapter in the Cisco Unified
                                                                  				Communications Manager Guide . In the Protocol Specific Information area of this window, choose a Device Security Profile and set the security mode. Note Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile. In the Extension Information area, check the Enable Extension Mobility check box if this phone supports Cisco Extension Mobility. Click Save . | Note | If you want to add both the phone and user to the Cisco Unified
                                                               				Communications Manager database at the same time, see "End user phone addition" chapter in the Cisco Unified
                                                                  				Communications Manager Guide . | Note | Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile. |
| Note | If you want to add both the phone and user to the Cisco Unified
                                                               				Communications Manager database at the same time, see "End user phone addition" chapter in the Cisco Unified
                                                                  				Communications Manager Guide . |
| Note | Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile. |
| Step 9 | Select Device > Phone to configure directory numbers (lines) on the phone by
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
                                                						right displays only if other devices share this directory number. Select Save . For more information, see 
                                          				the "Directory number setup" chapter in the Cisco Unified
                                                				Communications Manager Administration
                                             				  Guide and see Telephony Features . | Note | This field should contain the same number that appears in the Telephone Number field in the End User Configuration window. |
| Note | This field should contain the same number that appears in the Telephone Number field in the End User Configuration window. |
| Step 10 | Associate the user with a phone. Click Associate End Users at the bottom of the
                                       				  Phone Configuration window to associate a user to the line that is being configured. Use Find in
                                             				  conjunction with the Search fields to locate the user. check the box next
                                             				  to the user name, and click Add Selected . The user name and user ID appears in the 
                                                				  Users Associated With Line pane of the Directory Number
                                                				  Configuration window. Select Save . Select Save . The user is now associated with Line
                                                				  1 on the phone. If the phone has a second line, configure Line 2. |
| Step 11 | Associate the user with the device: Choose User Management > End User . Use the search boxes and Find to locate the user you have
                                             						  added. Click on the user ID. In the Directory Number Associations area of the screen, set the
                                             			 Primary Extension from the drop-down list. In the Mobility Information area, check the Enable Mobility box. In the Permissions Information area, use the Add to Access Control Group buttons to
                                             			 add this user to any user groups. For example, you may want to add the user to
                                                			 a group that is defined as a Standard CCM End User Group. To view the details of a group, select the group and click View Details . In the Extension Mobility area, check the Enable Extension
                                             			 Mobility Cross Cluster box if the user can use for Extension Mobility Cross
                                             			 Cluster service. In the Device Information area, click Device Associations . Use the Search fields and Find to
                                             						  locate the device that  you want to associate to the user. Select the
                                             						  device, and click Save Selected/Changes . Click Go next to the "Back to User" Related link in the upper right corner
                                             						  of the screen. Select Save . |
| Step 12 | Customize the softkey templates. Select Device > Device Settings > Softkey Template . Use the page to add, delete, or change the order of
                                          			 softkey features that display on the user’s phone to meet feature usage needs. For more information, see the "Softkey template setup" and "Cisco UnifiedIPPhone setup" chapters in the Cisco Unified
                                                				Communications Manager Administration
                                             				  Guide . |
| Step 13 | Configure speed-dial buttons and assign
                                       			 speed-dial numbers. Select Device > Phone . Note Users can change
                                                      			 speed-dial settings on their phones using their Self Care Portal . Find the phone you want to set up. In the Association Information area, click Add a new SD . Set up the speed dial information. Select Save . | Note | Users can change
                                                      			 speed-dial settings on their phones using their Self Care Portal . |
| Note | Users can change
                                                      			 speed-dial settings on their phones using their Self Care Portal . |
| Step 14 | Configure Cisco IPPhone services
                                       			 and assign services. Select Device > Device Settings > Phone Services . Provides IP Phone services to the phone. Note Users can add or change services on their phones using the Cisco Unified
                                                         				Communications Self Care Portal . | Note | Users can add or change services on their phones using the Cisco Unified
                                                         				Communications Self Care Portal . |
| Note | Users can add or change services on their phones using the Cisco Unified
                                                         				Communications Self Care Portal . |
| Step 15 | (Optional) Assign services to programmable buttons.  
                                       		  Select Device > Device Settings > Phone Button Profile . Provides
                                          			 access to an IP phone service or URL. |
| Step 16 | Add user information to the global directory for Cisco Unified
                                          				Communications Manager . Select User Management > End User and configure the required fields. Required
                                       			 fields are indicated by an asterisk (*); for example, User ID and last name. Note If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure Cisco Unified
                                                         				Communications Manager to use your existing LDAP directory, see "Understanding
                                                         		  Directory Numbers" in the Cisco Unified
                                                         		  Communications Manager System Guide . 
                                                      	  After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified
                                                         				Communications Manager Administration . Note If you want to add both the phone and user to the Cisco Unified
                                                         				Communications Manager database at the same time, see "End user phone addition" in Cisco Unified
                                                            				Communications Manager Administration
                                                         					 Guide . Set the User ID and last name fields. Assign a password (for Self Care Portal). Assign a PIN (for
                                             				  Cisco Extension Mobility and Personal Directory). Associate the user with a phone. Provides
                                                			 users with control over their phone such a forwarding calls or adding speed-dial numbers or services. Note Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. | Note | If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure Cisco Unified
                                                         				Communications Manager to use your existing LDAP directory, see "Understanding
                                                         		  Directory Numbers" in the Cisco Unified
                                                         		  Communications Manager System Guide . 
                                                      	  After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified
                                                         				Communications Manager Administration . | Note | If you want to add both the phone and user to the Cisco Unified
                                                         				Communications Manager database at the same time, see "End user phone addition" in Cisco Unified
                                                            				Communications Manager Administration
                                                         					 Guide . | Note | Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. |
| Note | If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure Cisco Unified
                                                         				Communications Manager to use your existing LDAP directory, see "Understanding
                                                         		  Directory Numbers" in the Cisco Unified
                                                         		  Communications Manager System Guide . 
                                                      	  After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified
                                                         				Communications Manager Administration . |
| Note | If you want to add both the phone and user to the Cisco Unified
                                                         				Communications Manager database at the same time, see "End user phone addition" in Cisco Unified
                                                            				Communications Manager Administration
                                                         					 Guide . |
| Note | Some phones, such as those in conference rooms, do not have an
                                                            				  associated user. |
| Step 17 | Associate a user with a user group. Select User Management > User Settings > Access Control Group . Assigns users a common list of
                                          			 roles and permissions that apply to all users in a user group. Administrators
                                          			 can manage user groups, roles, and permissions to control the level of access
                                          			 (and, therefore, the level of security) for system users. For more information, see Add a User to an End User Group . In order for end users to access the Cisco Unified
                                             				Communications Self Care Portal , you must add users to the standard Cisco Communications
                                          				Manager End Users group. For more information, see "End user setup" and "Access control group setup" in the Cisco Unified
                                                				Communications Manager Administration
                                             				  Guide . |

| Note | If you want to add both the phone and user to the Cisco Unified
                                                               				Communications Manager database at the same time, see "End user phone addition" chapter in the Cisco Unified
                                                                  				Communications Manager Guide . |
|---|---|

| Note | Choose a security profile based on the overall security strategy of the company. If the phone does not support security, choose
                                                            a nonsecure profile. |
|---|---|

| Note | This field should contain the same number that appears in the Telephone Number field in the End User Configuration window. |
|---|---|

| Note | Users can change
                                                      			 speed-dial settings on their phones using their Self Care Portal . |
|---|---|

| Note | Users can add or change services on their phones using the Cisco Unified
                                                         				Communications Self Care Portal . |
|---|---|

| Note | If your company uses a  Lightweight Directory Access Protocol
                                                      				  (LDAP) directory to store information on users, you can install and configure Cisco Unified
                                                         				Communications Manager to use your existing LDAP directory, see "Understanding
                                                         		  Directory Numbers" in the Cisco Unified
                                                         		  Communications Manager System Guide . 
                                                      	  After the Enable Synchronization from the LDAP Server field is enabled,
                                                      				  you will not be able to add additional users from Cisco Unified
                                                         				Communications Manager Administration . |
|---|---|

| Note | If you want to add both the phone and user to the Cisco Unified
                                                         				Communications Manager database at the same time, see "End user phone addition" in Cisco Unified
                                                            				Communications Manager Administration
                                                         					 Guide . |
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

| Step 1 | In the Directory Number Associations pane of the screen, set the
                                       			 primary extension from the drop-down list. |
|---|---|
| Step 2 | In the Mobility Information pane, check the Enable Mobility box. |
| Step 3 | In the Permissions Information pane, use the User Group buttons to
                                       			 add this user to any user groups. For example, you may want to add the user to
                                       			 a group that has been defined as a Standard CCM End User Group. To view all configured user groups, choose User Management > User
                                                					 Group . |
| Step 4 | Click Save . |