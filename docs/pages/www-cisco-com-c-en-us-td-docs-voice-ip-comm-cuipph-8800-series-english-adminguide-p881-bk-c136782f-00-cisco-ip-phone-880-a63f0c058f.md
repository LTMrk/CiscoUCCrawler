---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-a63f0c058f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_0100.html
retrieved_at: 2026-08-21T09:49:00.797747+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Cisco Unified Communications Manager Phone Setup

## Chapter: Cisco Unified Communications Manager Phone Setup

# Cisco Unified Communications Manager Phone Setup

## Set Up Cisco IP Phone

If
                              		  autoregistration is not enabled and the phone does not exist in the Cisco
                              		  Unified Communications Manager database, you must configure the Cisco IP Phone
                              		  in Cisco Unified Communications Manager manually. Some tasks in this procedure
                              		  are optional, depending on your system and user needs.

For more
                              		  information about Cisco Unified Communications Manager Administration, see the 
                              		  documentation for your particular Cisco Unified Communications Manager release.

Perform the
                              		  configuration steps in the following procedure using Cisco Unified
                              		  Communications Manager Administration.

Step 1

Gather the
                                       			 following information about the phone:

Phone
                                                					 model

MAC
                                                					 address

Physical
                                                					 location of the phone

Name or
                                                					 user ID of phone user

Device
                                                					 pool

Partition, calling search space, and location information

Number
                                                					 of lines and associated directory numbers (DNs) to assign to the phone

Cisco
                                                					 Unified Communications Manager user to associate with the phone

Phone
                                                					 usage information that affects phone button template, phone features, IP Phone
                                                					 services, or phone applications

The
                                          				information provides a list of configuration requirements for setting up phones
                                          				and identifies preliminary configuration that you need to perform before
                                          				configuring individual phones, such as phone button templates.

Step 2

Verify that
                                       			 you have sufficient unit licenses for your phone.

Step 3

Customize
                                       			 phone button templates (if required) by changing the number of line buttons,
                                       			 speed-dial buttons or service URL buttons. Select Device > Device
                                             				  Settings > Phone Button Template to create and
                                       			 update the templates.

You can add
                                          				a Privacy, All Calls, or Mobility button to meet user needs.

For more
                                          				information, see Phone Button Templates .

Step 4

Define the
                                       			 Device Pools. Select System > Device
                                             				  Pool .

Device Pools
                                          				define common characteristics for devices, such as region, date/time group,
                                          				softkey template, and MLPP information.

Step 5

Define the
                                       			 Common Phone Profile. Select Device > Device
                                             				  settings > Common Phone Profile .

Common phone
                                          				profiles provide data that the Cisco TFTP server requires, as well as common
                                          				phone settings, such as Do Not Disturb and feature control options.

Step 6

Define a
                                       			 Calling Search Space. In Cisco Unified Communications Manager Administration,
                                       			 click Call
                                             				  Routing > Class of Control > Calling Search
                                             				  Space .

A Calling
                                          				Search Space is a collection of partitions that are searched to determine how a
                                          				dialed number is routed. The calling search space for the device and the
                                          				calling search space for the directory number are used together. The directory
                                          				number CSS takes precedence over the device CSS.

Step 7

Configure a
                                       			 security profile for the device type and protocol. Select System > Security > Phone Security
                                             				  Profile .

Step 8

Add and
                                       			 configure the phone by completing the required fields in the Phone
                                       			 Configuration window. An asterisk (*) next to the field name indicates a
                                       			 required field; for example, MAC address and device pool.

This step
                                          				adds the device with the default settings to the Cisco Unified Communications
                                          				Manager database.

For
                                          				information about product-specific configuration fields, see the "?" Button Help in the Phone Configuration window.

If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release.

Step 9

Add and
                                       			 configure directory numbers (lines) on the phone by completing the required
                                       			 fields in the Directory Number Configuration window. An asterisk (*) next to
                                       			 the field name indicates a required field; for example, directory number and
                                       			 presence group.

This step
                                          				adds primary and secondary directory numbers and features associated with
                                          				directory numbers to the phone.

If you do not configure the primary directory number, the user sees the message Unprovisioned on the phone.

Step 10

Configure speed-dial buttons and assign speed-dial numbers.

Users can
                                          				change speed-dial settings on their phones by using Cisco Unified
                                          				Communications Self Care Portal.

Step 11

Configure
                                       			 Cisco Unified IP Phone services and assign services (optional) to provide IP
                                       			 Phone services.

Users can
                                          				add or change services on their phones by using the Cisco Unified
                                          				Communications Self Care Portal.

Users can
                                                      				  subscribe to the IP Phone service only if the Enterprise Subscription check box
                                                      				  is unchecked when the IP Phone service is first configured in Cisco Unified
                                                      				  Communications Manager Administration.

Some
                                                      				  Cisco-provided default services are classified as enterprise subscriptions, so
                                                      				  the user cannot add them through the Self Care Portal. Such services are
                                                      				  on the phone by default, and they can only be removed from the phone if you
                                                      				  disable them in Cisco Unified Communications Manager Administration.

Step 12

Assign
                                       			 services to programmable buttons (optional) to provide access to an IP Phone
                                       			 service or URL.

Step 13

Add user
                                       			 information by configuring required fields. An asterisk (*) next to the field
                                       			 name indicates a required field; for example, User ID and last name. This step
                                       			 adds user information to the global directory for Cisco Unified Communications
                                       			 Manager.

Assign a
                                                      				  password (for Self Care Portal) and PIN (for Cisco Extension Mobility and
                                                      				  Personal Directory).

If your
                                                      				  company uses a Lightweight Directory Access Protocol (LDAP) directory to store
                                                      				  information about users, you can install and configure Cisco Unified
                                                      				  Communications to use your existing LDAP directory.

If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release.

Step 14

Associate a
                                       			 user to a user group. This step assigns users a common list of roles and
                                       			 permissions that apply to all users in a user group. Administrators can manage
                                       			 user groups, roles, and permissions to control the level of access (and,
                                       			 therefore, the level of security) for system users. For example, you must add
                                       			 users to the standard Cisco CCM End Users group so users can access Cisco
                                       			 Unified Communications Manager Self Care Portal.

Step 15

Associate a
                                       			 user with a phone (optional). This step provides users with control over their
                                       			 phone such a forwarding calls or adding speed-dial numbers or services.

Some phones,
                                          				such as those in conference rooms, do not have an associated user.

Step 16

If you are
                                       			 not already in the End User Configuration window, choose User
                                             				  Management > End User to perform some final
                                       			 configuration tasks. Use the Search fields and Find to locate the user (for example, John Doe),
                                       			 then click on the user ID to get to the End User Configuration window for the
                                       			 user.

Step 17

In the
                                       			 Directory Number Associations area of the screen, set the primary extension
                                       			 from the drop-down list.

Step 18

In the
                                       			 Mobility Information area, check the Enable Mobility box.

Step 19

In the
                                       			 Permissions Information area, use the User Group buttons to add this user to
                                       			 any user groups.

For example,
                                          				you may want to add the user to a group that is defined as a Standard CCM End
                                          				User Group.

Step 20

To view all
                                       			 configured user groups, choose User
                                             				  Management > User Group .

Step 21

In the
                                       			 Extension Mobility area, check the Enable Extension Mobility Cross Cluster box
                                       			 if the user is allowed for Extension Mobility Cross Cluster service.

Step 22

Select Save .

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

## Survivable Remote
                        	 Site Telephony

Survivable Remote
                              		  Site Telephony (SRST) ensures that basic phone functions remain accessible when
                              		  WAN connectivity is lost. In this scenario, the phone can keep an in-progress call active, and
                              		  the user can access a subset of the features available. When failover occurs,
                              		  the user receives an alert message on the phone.

For more information about supported firmware and Survivable Remote Site Telephony, see Cisco Unified Survivable Remote Site Telephony
                                 Compatibility Information page on Cisco.com ( http://www.cisco.com/c/en/us/support/unified-communications/unified-survivable-remote-site-telephony/products-device-support-tables-list.html ).

The following
                              		  table describes the availability of features during failover.

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

Conference to Active Calls (Join)

No

The Active Calls softkey does not display.

Conference List

No

Transfer

Yes

Transfer to Active Calls (Direct Transfer)

No

Auto Answer

Yes

Call Waiting

Yes

Caller ID

Yes

Audible Message Waiting Indicator

Yes

All Calls Programmable Line Key

Yes

Answer Programmable Line Key

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

Service IRL Programmable Line Key

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

Barge

No

The Barge softkey does not display.

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

Video

Yes

Video conference is not supported.

Video

Yes

Video conference is not supported.

Shared Line

No

BLF Speed Dial

Yes

Service URL

Yes

The programmable line key with a Service URL assigned is displayed.

## Enhanced Survivable Remote Site Telephony

Shared-Line

Busy-Lamp-Field (BLF)

Video Calls

For more information about supported firmware and Survivable Remote Site Telephony, see Cisco Unified Survivable Remote Site Telephony
                                 Compatibility Information page on Cisco.com ( http://www.cisco.com/c/en/us/support/unified-communications/unified-survivable-remote-site-telephony/products-device-support-tables-list.html ).

## Application Dial Rules

Application Dial Rules are used to convert numbers for shared mobile contacts to network dialable numbers.  Application Dial
                              Rules do not apply when the user is dialing a number manually, or if the number is edited before the user places the call.

Application Dial Rules are set in Cisco Unified Communications Manager .

For additional information about dial rules, see System Configuration Guide for Cisco Unified Communications Manager , "Configure Dial Rules" chapter.

### Configure Application Dial Rules

Step 1

In Cisco Unified Communications Manager Administration, go to Call Routing > Dial Rules > Application Dial Rules .

Step 2

Choose Add New to create a new application dial rule, or choose an existing application dial rule to edit it.

Step 3

Fill in the following fields:

- Name This field comprises a unique name for the dial rule that can contain up to 20 alphanumeric characters and any combination
                                                   of spaces, periods (.), hyphens (-), and underscore characters (_).

- Description This field comprises a brief description that you enter for the dial rule.

- Number Begins With This field comprises the initial digits of the directory numbers to which you want to apply this application dial rule.

- Number of Digits This required field comprises the initial digits of the directory numbers to which you want to apply this application dial
                                                   rule.

- Total Digits to be Removed This required field comprises the number of digits that you want Cisco Unified Communications Manager to remove from directory
                                                   numbers that apply to this dial rule.

- Prefix With Pattern This required field comprises the pattern to prepend to directory numbers that apply to this application dial rule.

- Application Dial Rule Priority This field displays when you enter the Prefix With Pattern information. The field allows you to set the priority order of
                                                   the application dial rules.

Step 4

Restart Cisco Unified Communications Manager .

| Step 1 | Gather the
                                       			 following information about the phone: Phone
                                                					 model MAC
                                                					 address Physical
                                                					 location of the phone Name or
                                                					 user ID of phone user Device
                                                					 pool Partition, calling search space, and location information Number
                                                					 of lines and associated directory numbers (DNs) to assign to the phone Cisco
                                                					 Unified Communications Manager user to associate with the phone Phone
                                                					 usage information that affects phone button template, phone features, IP Phone
                                                					 services, or phone applications The
                                          				information provides a list of configuration requirements for setting up phones
                                          				and identifies preliminary configuration that you need to perform before
                                          				configuring individual phones, such as phone button templates. |
|---|---|
| Step 2 | Verify that
                                       			 you have sufficient unit licenses for your phone. |
| Step 3 | Customize
                                       			 phone button templates (if required) by changing the number of line buttons,
                                       			 speed-dial buttons or service URL buttons. Select Device > Device
                                             				  Settings > Phone Button Template to create and
                                       			 update the templates. You can add
                                          				a Privacy, All Calls, or Mobility button to meet user needs. For more
                                          				information, see Phone Button Templates . |
| Step 4 | Define the
                                       			 Device Pools. Select System > Device
                                             				  Pool . Device Pools
                                          				define common characteristics for devices, such as region, date/time group,
                                          				softkey template, and MLPP information. |
| Step 5 | Define the
                                       			 Common Phone Profile. Select Device > Device
                                             				  settings > Common Phone Profile . Common phone
                                          				profiles provide data that the Cisco TFTP server requires, as well as common
                                          				phone settings, such as Do Not Disturb and feature control options. |
| Step 6 | Define a
                                       			 Calling Search Space. In Cisco Unified Communications Manager Administration,
                                       			 click Call
                                             				  Routing > Class of Control > Calling Search
                                             				  Space . A Calling
                                          				Search Space is a collection of partitions that are searched to determine how a
                                          				dialed number is routed. The calling search space for the device and the
                                          				calling search space for the directory number are used together. The directory
                                          				number CSS takes precedence over the device CSS. |
| Step 7 | Configure a
                                       			 security profile for the device type and protocol. Select System > Security > Phone Security
                                             				  Profile . |
| Step 8 | Add and
                                       			 configure the phone by completing the required fields in the Phone
                                       			 Configuration window. An asterisk (*) next to the field name indicates a
                                       			 required field; for example, MAC address and device pool. This step
                                          				adds the device with the default settings to the Cisco Unified Communications
                                          				Manager database. For
                                          				information about product-specific configuration fields, see the "?" Button Help in the Phone Configuration window. Note If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release. | Note | If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release. |
| Note | If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release. |
| Step 9 | Add and
                                       			 configure directory numbers (lines) on the phone by completing the required
                                       			 fields in the Directory Number Configuration window. An asterisk (*) next to
                                       			 the field name indicates a required field; for example, directory number and
                                       			 presence group. This step
                                          				adds primary and secondary directory numbers and features associated with
                                          				directory numbers to the phone. Note If you do not configure the primary directory number, the user sees the message Unprovisioned on the phone. | Note | If you do not configure the primary directory number, the user sees the message Unprovisioned on the phone. |
| Note | If you do not configure the primary directory number, the user sees the message Unprovisioned on the phone. |
| Step 10 | Configure speed-dial buttons and assign speed-dial numbers. Users can
                                          				change speed-dial settings on their phones by using Cisco Unified
                                          				Communications Self Care Portal. |
| Step 11 | Configure
                                       			 Cisco Unified IP Phone services and assign services (optional) to provide IP
                                       			 Phone services. Users can
                                          				add or change services on their phones by using the Cisco Unified
                                          				Communications Self Care Portal. Note Users can
                                                      				  subscribe to the IP Phone service only if the Enterprise Subscription check box
                                                      				  is unchecked when the IP Phone service is first configured in Cisco Unified
                                                      				  Communications Manager Administration. Note Some
                                                      				  Cisco-provided default services are classified as enterprise subscriptions, so
                                                      				  the user cannot add them through the Self Care Portal. Such services are
                                                      				  on the phone by default, and they can only be removed from the phone if you
                                                      				  disable them in Cisco Unified Communications Manager Administration. | Note | Users can
                                                      				  subscribe to the IP Phone service only if the Enterprise Subscription check box
                                                      				  is unchecked when the IP Phone service is first configured in Cisco Unified
                                                      				  Communications Manager Administration. | Note | Some
                                                      				  Cisco-provided default services are classified as enterprise subscriptions, so
                                                      				  the user cannot add them through the Self Care Portal. Such services are
                                                      				  on the phone by default, and they can only be removed from the phone if you
                                                      				  disable them in Cisco Unified Communications Manager Administration. |
| Note | Users can
                                                      				  subscribe to the IP Phone service only if the Enterprise Subscription check box
                                                      				  is unchecked when the IP Phone service is first configured in Cisco Unified
                                                      				  Communications Manager Administration. |
| Note | Some
                                                      				  Cisco-provided default services are classified as enterprise subscriptions, so
                                                      				  the user cannot add them through the Self Care Portal. Such services are
                                                      				  on the phone by default, and they can only be removed from the phone if you
                                                      				  disable them in Cisco Unified Communications Manager Administration. |
| Step 12 | Assign
                                       			 services to programmable buttons (optional) to provide access to an IP Phone
                                       			 service or URL. |
| Step 13 | Add user
                                       			 information by configuring required fields. An asterisk (*) next to the field
                                       			 name indicates a required field; for example, User ID and last name. This step
                                       			 adds user information to the global directory for Cisco Unified Communications
                                       			 Manager. Note Assign a
                                                      				  password (for Self Care Portal) and PIN (for Cisco Extension Mobility and
                                                      				  Personal Directory). Note If your
                                                      				  company uses a Lightweight Directory Access Protocol (LDAP) directory to store
                                                      				  information about users, you can install and configure Cisco Unified
                                                      				  Communications to use your existing LDAP directory. Note If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release. | Note | Assign a
                                                      				  password (for Self Care Portal) and PIN (for Cisco Extension Mobility and
                                                      				  Personal Directory). | Note | If your
                                                      				  company uses a Lightweight Directory Access Protocol (LDAP) directory to store
                                                      				  information about users, you can install and configure Cisco Unified
                                                      				  Communications to use your existing LDAP directory. | Note | If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release. |
| Note | Assign a
                                                      				  password (for Self Care Portal) and PIN (for Cisco Extension Mobility and
                                                      				  Personal Directory). |
| Note | If your
                                                      				  company uses a Lightweight Directory Access Protocol (LDAP) directory to store
                                                      				  information about users, you can install and configure Cisco Unified
                                                      				  Communications to use your existing LDAP directory. |
| Note | If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release. |
| Step 14 | Associate a
                                       			 user to a user group. This step assigns users a common list of roles and
                                       			 permissions that apply to all users in a user group. Administrators can manage
                                       			 user groups, roles, and permissions to control the level of access (and,
                                       			 therefore, the level of security) for system users. For example, you must add
                                       			 users to the standard Cisco CCM End Users group so users can access Cisco
                                       			 Unified Communications Manager Self Care Portal. |
| Step 15 | Associate a
                                       			 user with a phone (optional). This step provides users with control over their
                                       			 phone such a forwarding calls or adding speed-dial numbers or services. Some phones,
                                          				such as those in conference rooms, do not have an associated user. |
| Step 16 | If you are
                                       			 not already in the End User Configuration window, choose User
                                             				  Management > End User to perform some final
                                       			 configuration tasks. Use the Search fields and Find to locate the user (for example, John Doe),
                                       			 then click on the user ID to get to the End User Configuration window for the
                                       			 user. |
| Step 17 | In the
                                       			 Directory Number Associations area of the screen, set the primary extension
                                       			 from the drop-down list. |
| Step 18 | In the
                                       			 Mobility Information area, check the Enable Mobility box. |
| Step 19 | In the
                                       			 Permissions Information area, use the User Group buttons to add this user to
                                       			 any user groups. For example,
                                          				you may want to add the user to a group that is defined as a Standard CCM End
                                          				User Group. |
| Step 20 | To view all
                                       			 configured user groups, choose User
                                             				  Management > User Group . |
| Step 21 | In the
                                       			 Extension Mobility area, check the Enable Extension Mobility Cross Cluster box
                                       			 if the user is allowed for Extension Mobility Cross Cluster service. |
| Step 22 | Select Save . |

| Note | If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release. |
|---|---|

| Note | If you do not configure the primary directory number, the user sees the message Unprovisioned on the phone. |
|---|---|

| Note | Users can
                                                      				  subscribe to the IP Phone service only if the Enterprise Subscription check box
                                                      				  is unchecked when the IP Phone service is first configured in Cisco Unified
                                                      				  Communications Manager Administration. |
|---|---|

| Note | Some
                                                      				  Cisco-provided default services are classified as enterprise subscriptions, so
                                                      				  the user cannot add them through the Self Care Portal. Such services are
                                                      				  on the phone by default, and they can only be removed from the phone if you
                                                      				  disable them in Cisco Unified Communications Manager Administration. |
|---|---|

| Note | Assign a
                                                      				  password (for Self Care Portal) and PIN (for Cisco Extension Mobility and
                                                      				  Personal Directory). |
|---|---|

| Note | If your
                                                      				  company uses a Lightweight Directory Access Protocol (LDAP) directory to store
                                                      				  information about users, you can install and configure Cisco Unified
                                                      				  Communications to use your existing LDAP directory. |
|---|---|

| Note | If you
                                                      				  want to add both the phone and user to the Cisco Unified Communications Manager
                                                      				  database at the same time, see the 
                                                      				  documentation for your particular Cisco Unified Communications Manager release. |
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
| Conference | Yes |  |
| Conference to Active Calls (Join) | No | The Active Calls softkey does not display. |
| Conference List | No |  |
| Transfer | Yes |  |
| Transfer to Active Calls (Direct Transfer) | No |  |
| Auto Answer | Yes |  |
| Call Waiting | Yes |  |
| Caller ID | Yes |  |
| Audible Message Waiting Indicator | Yes |  |
| All Calls Programmable Line Key | Yes |  |
| Answer Programmable Line Key | Yes |  |
| Unified Session Presentation | Yes | Conference is the only feature supported due to other feature limitations. |
| Voicemail | Yes | Voicemail will not be synchronized with other users in the Cisco Unified Communications Manager cluster. |
| Call Forward All | Yes | Forward state is only available on the phone that sets the forward because there are no shared line appearances in SRST mode.
                                          The Call Forward All settings are not preserved on failover to SRST from the Cisco Unified Communications Manager, or from
                                          SRST fail-back to the Communications Manager. Any original Call Forward All still active on the Communications Manager should
                                          be indicated when the device reconnects to the Communications Manager after failover. |
| Speed Dial | Yes |  |
| Service IRL Programmable Line Key | Yes |  |
| To Voicemail (iDivert) | No | The iDivert softkey does not display. |
| Line Filters | Partial | Lines are supported but cannot be shared. |
| Park Monitoring | No | The Park softkey does not display. |
| Barge | No | The Barge softkey does not display. |
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
| Video | Yes | Video conference is not supported. |
| Video | Yes | Video conference is not supported. |
| Shared Line | No |  |
| BLF Speed Dial | Yes |  |
| Service URL | Yes | The programmable line key with a Service URL assigned is displayed. |

| Step 1 | In Cisco Unified Communications Manager Administration, go to Call Routing > Dial Rules > Application Dial Rules . |
|---|---|
| Step 2 | Choose Add New to create a new application dial rule, or choose an existing application dial rule to edit it. |
| Step 3 | Fill in the following fields: Name This field comprises a unique name for the dial rule that can contain up to 20 alphanumeric characters and any combination
                                                   of spaces, periods (.), hyphens (-), and underscore characters (_). Description This field comprises a brief description that you enter for the dial rule. Number Begins With This field comprises the initial digits of the directory numbers to which you want to apply this application dial rule. Number of Digits This required field comprises the initial digits of the directory numbers to which you want to apply this application dial
                                                   rule. Total Digits to be Removed This required field comprises the number of digits that you want Cisco Unified Communications Manager to remove from directory
                                                   numbers that apply to this dial rule. Prefix With Pattern This required field comprises the pattern to prepend to directory numbers that apply to this application dial rule. Application Dial Rule Priority This field displays when you enter the Prefix With Pattern information. The field allows you to set the priority order of
                                                   the application dial rules. |
| Step 4 | Restart Cisco Unified Communications Manager . |