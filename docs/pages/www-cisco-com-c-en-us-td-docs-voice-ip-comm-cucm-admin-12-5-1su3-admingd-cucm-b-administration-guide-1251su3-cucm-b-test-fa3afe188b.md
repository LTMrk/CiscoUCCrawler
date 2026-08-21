---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-admingd-cucm-b-administration-guide-1251su3-cucm-b-test-fa3afe188b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/adminGd/cucm_b_administration-guide-1251su3/cucm_b_test-adminguide_chapter_011.html
retrieved_at: 2026-08-21T16:03:16.945286+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: April 8, 2025

Chapter: Manage End Users

## Chapter: Manage End Users

# Manage End Users

## End User
                        	 Overview

When administering
                              		  an up and running system, you may need to make updates to the list of
                              		  configured end users in your system. This includes:

Setting up a
                                    				new user

Setting up a
                                    				phone for a new end user

Changing
                                    				passwords or PINs for an end user

Enable end users for IM and Presence Service

The End User
                                 			 Configuration window in Cisco Unified CM Administration allows you
                              		  to add, search, display, and maintain information about Unified CM end users.
                              		  You can also use the Quick
                                 			 User/Phone Add window to quickly configure a new end user and
                              		  configure a new phone for that end user.

## End
                        	 User Management Tasks

Step 1

Configure User Templates

If you have not configured your system with user profiles or feature group templates that includes universal line and device
                                          templates, perform these tasks to set them up.

You can apply these templates to any new end users in order to quickly configure new users and phones.

Step 2

Add a new end user using one of the following methods

- Import an End User from LDAP

- Add an End User Manually

If you have configured and if your system is synchronized with a company LDAP directory, you can import the new end user
                                          directly from LDAP.

Else, you can add and configure the end user manually.

Step 3

Assign a phone
                                       			 to a new or existing end user by performing either of the following tasks:

- Add New Phone for End User

- Move an Existing Phone to a End User

You can use
                                          				the 'Add New Phone' procedure to configure a new phone for the end user using
                                          				settings from a universal device template.

You can also
                                          				use the 'Move' procedure to assign an existing phone that has already been
                                          				configured.

Step 4

Change the End User PIN

(Optional) To
                                          				change the pin for an end user in Cisco
                                             				  Unified Communications Manager Administration .

Step 5

Change the End User Password

(Optional) To
                                          				change the password for an end user in Cisco
                                             				  Unified Communications Manager Administration .

Step 6

Create a Cisco Unity Connection Voice Mailbox

(Optional) To
                                          				create individual Cisco
                                             				  Unity Connection voice mailboxes in Cisco Unified
                                             				  Communications Manager Administration .

### Configure User Templates

Perform the following tasks to set up a user profile and feature group template. When you add a new end user, you can use
                                 the line and device settings to quickly configure the end user and any phones for the end user.

Step 1

Configure Universal Line Template

Configure universal line templates with common settings that are typically applied to a directory number.

Step 2

Configure Universal Device Template

Configure universal device templates with common settings that are typically applied to a phone.

Step 3

Configure User Profiles

Assign universal line and universal device templates to a user profile. If you have the self-provisioning feature configured,
                                             you can enable self-provisioning for the users who use this profile.

Step 4

Configure Feature Group Template

Assign the user profile to a feature group template. For LDAP Synchronized Users, the feature group template associates the
                                             user profile settings to the end user.

#### Configure Universal Line Template

Universal Line Templates make it easy to apply common settings to newly assigned directory numbers. Configure different templates
                                    to meet the needs of different groups of users.

Step 1

In Cisco Unified CM Administration, choose User Management > User/Phone Add > Universal Line Template .

Step 2

Click Add
                                                				New .

Step 3

Configure the
                                             			 fields in the Universal Line Template Configuration window. See the
                                             			 online help for more information about the fields and their configuration
                                             			 options.

Step 4

If you are deploying Global Dial Plan Replication with alternate numbers expand the Enterprise Alternate Number and +E.164 Alternate Number sections and do the following:

Click the Add Enterprise Alternate Number button and/or Add +E.164 Alternate Number button.

Add the Number Mask that you want to use to assign to your alternate numbers. For example, a 4-digit extension might use 5XXXX as an enterprise
                                                   number mask and 1972555XXXX as an +E.164 alternate number mask.

Assign the partition where you want to assign alternate numbers.

If you want to advertise this number via ILS, check the Advertise Globally via ILS check box. Note that if you are using advertised patterns to summarize a range of alternate numbers, you may not need to
                                                   advertise individual alternate numbers.

Expand the PSTN Failover section and choose the Enterprise Number or +E.164 Alternate Number as the PSTN failover to use if normal call routing fails.

Step 5

Click Save .

##### What to do next

Configure Universal Device Template

#### Configure Universal Device Template

Universal device templates make it easy to apply configuration settings to newly provisioned devices. The provisioned device
                                    uses the settings of the universal device template. You can configure different device templates to meet the needs of different
                                    groups of users. You can also assign the profiles that you’ve configured to this template.

##### Before you begin

Configure Universal Line Template

Step 1

In Cisco Unified CM
                                             			 Administration, choose User
                                                   				  Management > User/Phone Add > Universal Device
                                                   				  Template .

Step 2

Click Add New .

Step 3

Enter the following mandatory fields:

Enter a Device Description for the template.

Select a Device Pool type from the drop-down list.

Select a Device Security Profile from the drop-down list.

Select a SIP Profile from the drop-down list.

Select a Phone Button Template from the drop-down list.

Step 4

Complete the remaining fields in the Universal Device Template Configuration window. For field descriptions, see the online help.

Step 5

Under Phone Settings , complete the following optional fields:

If you configured a Common Phone Profile , assign the profile.

If you configured a Common Device Configuration , assign the configuration.

If you configured a Feature Control Policy , assign the policy.

Step 6

Click Save .

##### What to do next

Configure User Profiles

#### Configure User Profiles

Assign universal line and universal device template to users through the User Profile. Configure multiple user profiles for
                                    different groups of users. You can also enable self-provisioning for users who use this service profile.

##### Before you begin

Configure Universal Device Template

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > User Profile .

Step 2

Click Add
                                                				New .

Step 3

Enter a Name and Description for the user profile.

Step 4

Assign a Universal Device Template to apply to users' Desk
                                                				Phones , Mobile
                                                				and Desktop Devices , and Remote
                                                				Destination/Device Profiles .

Step 5

Assign a Universal Line Template to apply to the phone lines
                                             			 for users in this user profile.

Step 6

If you want
                                             			 the users in this user profile to be able to use the self-provisioning feature
                                             			 to provision their own phones, do the following:

Check the Allow End User to Provision their own phones check box.

In the Limit Provisioning once End User has this many phones field, enter a maximum number of phones the user is allowed to provision. The maximum is 20.

Check the Allow Provisioning of a phone already assigned to a different End User check box to determine whether the user who is associated with this profile has the permission to migrate or reassign a device
                                                   that is already owned by another user. By default, this check box is unchecked.

Step 7

If you want Cisco Jabber users who are associated with this user profile, to be able to use the Mobile and Remote Access feature,
                                             check the Enable Mobile and Remote Access check box.

By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default.

This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                                  setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                                  and Remote Access users and not to any other endpoints or clients.

Step 8

Assign the Jabber policies for this user profile. From the Desktop Client Policy , and Mobile Client Policy drop-down list, choose one of the following options:

- No Service—This policy disables access to all Cisco Jabber services.

- IM & Presence only—This policy enables only instant messaging and presence capabilities.

- IM & Presence, Voice and Video calls—This policy enables instant messaging, presence, voicemail, and conferencing capabilities
                                                for all users with audio or video devices. This is the default option.

Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                            Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users.

Step 9

If you want the users in this user profile to set the maximum login time for Extension Mobility or Extension Mobility Cross
                                             Cluster through Cisco Unified Communications Self Care Portal, check the Allow End User to set their Extension Mobility maximum login time check box.

By default Allow End User to set their Extension Mobility maximum login time check box is unchecked.

Step 10

Click Save .

##### What to do next

Configure Feature Group Template

#### Configure Feature Group Template

Feature group templates aid in your system deployment by helping you to quickly configure phones, lines, and features for
                                    your provisioned users. If you are syncing users from a company LDAP directory, configure a feature group template with the
                                    User Profile and Service Profile that you want users synced from the directory to use. You can also enable the IM and Presence
                                    Service for synced users through this template.

Step 1

In Cisco
                                             			 Unified CM Administration, choose User
                                                   				  Management > User/Phone Add > Feature Group
                                                   				  Template .

Step 2

Click Add
                                                				New .

Step 3

Enter a Name and Description for the Feature Group Template.

Step 4

Check the Home Cluster check box if you want to use the local cluster as the home cluster for all users whom use this template.

Step 5

Check the Enable User for Unified CM IM and Presence check box to allow users whom use this template to exchange instant messaging and presence information.

Step 6

From the drop-down list, select a Services Profile and User Profile .

Step 7

Complete the
                                             			 remaining fields in the Feature
                                                				Group Template Configuration window. Refer to the online help for
                                             			 field descriptions.

Step 8

Click Save .

##### What to do next

Add a new end user. If your system is integrated with a company LDAP directory,  you can import the user directly from an
                                    LDAP directory. Otherwise, create the end user manually.

Import an End User from LDAP

Add an End User Manually

### Import an End User
                           	 from LDAP

Perform the following procedure to manually import a new end user from a company LDAP directory. If your LDAP synchronization
                                 configuration includes a feature group template with a user profile that includes universal line and device templates and
                                 a DN pool, the import process automatically configures the end user and primary extension.

You cannot add new configurations (for example, adding a feature group template) into an LDAP directory sync after the initial
                                             sync has occurred. If you want to edit an existing LDAP sync, you must either use Bulk Administration, or configure a new
                                             LDAP  sync.

#### Before you begin

Before you begin this procedure make sure that you have already synchronized Cisco Unified Communications Manager with a company
                                 LDAP directory. The LDAP synchronization must include a feature group template with universal line and device templates.

Step 1

In Cisco
                                          			 Unified CM Administration, choose System > LDAP > LDAP
                                                				  Directory .

Step 2

Click Find and select the LDAP directory to which the user
                                          			 is added.

Step 3

Click Perform Full Sync .

#### What to do next

If the user is enabled for self-provisioning, the end user can use the Self-Provisioning Interactive Voice Response (IVR)
                                 to provision a new phone. Otherwise, perform one of the following tasks to assign a phone to the end user:

Add New Phone for End User

Move an Existing Phone to a End User

### Add an End User
                           	 Manually

Perform the following procedure to add new end user and configure them with an access control group and a primary line extension.

#### Before you begin

Verify that you
                                 		  have a user profile configured that includes a universal line template. If you
                                 		  need to configure a new extension, Cisco Unified Communications Manager uses
                                 		  the settings from the universal line template to configure the primary
                                 		  extension.

Step 1

In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > User/Phone Add > Quick User/Phone
                                                				  Add .

Step 2

Enter the User ID and Last Name .

Step 3

From the Feature Group Template drop-down list, select a
                                          			 feature group template.

Step 4

Click Save .

Step 5

From the User
                                             				Profile drop-down list, verify that the selected user profile
                                          			 includes a universal line template.

Step 6

From the Access
                                             				Control Group Membership section, click the + icon.

Step 7

From the User
                                             				is a member of drop-down list, select an access control group.

Step 8

Under Primary Extension , click the + icon.

Step 9

From the Extension drop-down list, select a DN that displays as (available) .

Step 10

If all line
                                          			 extensions display as (used) , perform the following steps:

Click the New... button.

In the Directory Number field, enter a new line extension.

From the Line Template drop-down list, select a universal line template.

Click OK .

Step 11

(Optional) Complete any additional fields in the Quick User/Phone Add Configuration window.

Step 12

Click Save .

#### What to do next

Perform one of the
                                 		  following procedures to assign a phone to this end user:

Add New Phone for End User

Move an Existing Phone to a End User

### Add New Phone for
                           	 End User

Perform the following procedure to add a new phone for a new or existing end user. Make sure that the user profile for the
                                 end user includes a universal device template. Cisco Unified Communications Manager uses the universal device template settings
                                 to configure the phone.

#### Before you begin

Perform one of the following procedures to add an end user:

Add an End User Manually

Import an End User from LDAP

Step 1

In Cisco Unified CM Administration, choose User Management > User/Phone Add > Quick/User Phone Add .

Step 2

Click Find and select the end user for whom you want to
                                          			 add a new phone.

Step 3

Click the Manage Devices .

Step 4

Click Add
                                             				New Phone .

Step 5

From the Product Type drop-down list, select the phone model.

Step 6

From the Device Protocol drop-down list select SIP or SCCP as the protocol.

Step 7

In the Device
                                             				Name text box, enter the device MAC address.

Step 8

From the Universal Device Template drop-down list, select a
                                          			 universal device template.

Step 9

If the phone
                                          			 supports expansion modules, enter the number of expansion modules that you want
                                          			 to deploy.

Step 10

If you want to
                                          			 use Extension Mobility to access the phone, check the In
                                             				Extension Mobility check box.

Step 11

Click Add
                                             				Phone .

Step 12

If you want to make additional edits to the phone configuration, click the corresponding Pencil icon to open the phone in
                                          the Phone Configuration window.

### Move an Existing
                           	 Phone to a End User

Perform this
                                 		  procedure to move an existing phone to a new or existing end user.

Step 1

In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > User/Phone Add > Quick/User Phone
                                                				  Add .

Step 2

Click Find and select the user to whom you want to move an
                                          			 existing phone.

Step 3

Click the Manage
                                             				Devices button.

Step 4

Click the Find a
                                             				Phone to Move To This User button.

Step 5

Select the
                                          			 phone that you want to move to this user.

Step 6

Click Move
                                             				Selected .

### Change the End
                           	 User PIN

Step 1

In Cisco
                                          			 Unified Communications Manager Administration, choose User Management > End User .

Step 2

To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, click Find to retrieve a list of users, and then select
                                          			 the user from the list.

Step 3

In the PIN field, double-click the existing PIN, which is
                                          			 encrypted, and enter the new PIN. You must enter at least the minimum number of
                                          			 characters that are specified in the assigned credential policy (1-127
                                          			 characters).

Step 4

In the Confirm PIN field, double-click the existing,
                                          			 encrypted PIN and enter the new PIN again.

Step 5

Click Save .

You can
                                                         				  login to Extension Mobility, Conference Now, Mobile Connect, and Cisco Unity
                                                         				  Connection voicemail with the same end user PIN, if End User Pin synchronization checkbox is enabled in
                                                         				  the Application Server Configuration window for Cisco Unity Connection. End users can use the same PIN to log in
                                                            					 to Extension Mobility and to access their voicemail.

### Change the End
                           	 User Password

You cannot change
                                 		  an end user password when LDAP authentication is enabled.

Step 1

In Cisco
                                          			 Unified Communications Manager Administration, choose User Management > End User .

Step 2

To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, click Find to retrieve a list of users, and then select
                                          			 the user from the list.

Step 3

In the Password field, double-click the existing password,
                                          			 which is encrypted, and enter the new password. You must enter at least the
                                          			 minimum number of characters that are specified in the assigned credential
                                          			 policy (1-127 characters).

Step 4

In the Confirm Password field, double-click the existing,
                                          			 encrypted password and enter the new password again.

Step 5

Click Save .

### Create a Cisco
                           	 Unity Connection Voice Mailbox

#### Before you begin

You must configure Cisco Unified Communications Manager for voice messaging. For more information about configuring Cisco Unified Communications Manager to use Cisco Unity Connection , see the System Configuration Guide for Cisco Unified Communications Manager at:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html

You must associate a device and a Primary Extension Number with
                                       				the end user.

You can use the import feature that is available in Cisco Unity
                                          				  Connection instead of performing the procedure that is described in
                                       				this section. For information about how to use the import feature, see the User
                                          				  Moves, Adds, and Changes Guide for Cisco Unity Connection .

Step 1

In Cisco
                                          			 Unified Communications Manager Administration, choose User Management > End User .

Step 2

To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, click Find to retrieve a list of users, and then select
                                          			 the user from the list.

Step 3

Verify that a
                                          			 primary extension number is associated with this user.

You must
                                                         				  define a primary extension; otherwise, the Create Cisco Unity User
                                                         				  link does not appear in the Related Links drop-down list.

Step 4

From the Related Links drop-down list, choose the Create Cisco Unity User
                                          			 link, and then click Go .

The Add Cisco Unity User
                                             				dialog box appears.

Step 5

From
                                          			 the Application Server drop-down list, choose the Cisco Unity
                                             				Connection server on which you want to create a Cisco Unity
                                             				Connection user, and then click Next .

Step 6

From the Subscriber Template drop-down list, choose the
                                          			 subscriber template that you want to use.

Step 7

Click Save .

The mailbox is
                                             				created. The link in the Related Links drop-down list changes to Edit Cisco Unity User
                                             				in the End
                                                				  User Configuration window. In Cisco Unity Connection
                                                				  Administration , you can now view the user that you created.

After you
                                                         				  integrate the Cisco Unity
                                                            					 Connection user with the Cisco Unified
                                                            					 Communications Manager end user, you cannot edit fields in Cisco Unity Connection
                                                            					 Administration such as Alias (User ID in Cisco Unified CM
                                                         				  Administration), First Name, Last Name, and Extension (Primary Extension in
                                                         				  Cisco Unified CM Administration). You can only update these fields in Cisco
                                                         				  Unified CM Administration.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure User Templates | If you have not configured your system with user profiles or feature group templates that includes universal line and device
                                          templates, perform these tasks to set them up. You can apply these templates to any new end users in order to quickly configure new users and phones. |
| Step 2 | Add a new end user using one of the following methods Import an End User from LDAP Add an End User Manually | If you have configured and if your system is synchronized with a company LDAP directory, you can import the new end user
                                          directly from LDAP. Else, you can add and configure the end user manually. |
| Step 3 | Assign a phone
                                       			 to a new or existing end user by performing either of the following tasks: Add New Phone for End User Move an Existing Phone to a End User | You can use
                                          				the 'Add New Phone' procedure to configure a new phone for the end user using
                                          				settings from a universal device template. You can also
                                          				use the 'Move' procedure to assign an existing phone that has already been
                                          				configured. |
| Step 4 | Change the End User PIN | (Optional) To
                                          				change the pin for an end user in Cisco
                                             				  Unified Communications Manager Administration . |
| Step 5 | Change the End User Password | (Optional) To
                                          				change the password for an end user in Cisco
                                             				  Unified Communications Manager Administration . |
| Step 6 | Create a Cisco Unity Connection Voice Mailbox | (Optional) To
                                          				create individual Cisco
                                             				  Unity Connection voice mailboxes in Cisco Unified
                                             				  Communications Manager Administration . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Universal Line Template | Configure universal line templates with common settings that are typically applied to a directory number. |
| Step 2 | Configure Universal Device Template | Configure universal device templates with common settings that are typically applied to a phone. |
| Step 3 | Configure User Profiles | Assign universal line and universal device templates to a user profile. If you have the self-provisioning feature configured,
                                             you can enable self-provisioning for the users who use this profile. |
| Step 4 | Configure Feature Group Template | Assign the user profile to a feature group template. For LDAP Synchronized Users, the feature group template associates the
                                             user profile settings to the end user. |

| Step 1 | In Cisco Unified CM Administration, choose User Management > User/Phone Add > Universal Line Template . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | Configure the
                                             			 fields in the Universal Line Template Configuration window. See the
                                             			 online help for more information about the fields and their configuration
                                             			 options. |
| Step 4 | If you are deploying Global Dial Plan Replication with alternate numbers expand the Enterprise Alternate Number and +E.164 Alternate Number sections and do the following: Click the Add Enterprise Alternate Number button and/or Add +E.164 Alternate Number button. Add the Number Mask that you want to use to assign to your alternate numbers. For example, a 4-digit extension might use 5XXXX as an enterprise
                                                   number mask and 1972555XXXX as an +E.164 alternate number mask. Assign the partition where you want to assign alternate numbers. If you want to advertise this number via ILS, check the Advertise Globally via ILS check box. Note that if you are using advertised patterns to summarize a range of alternate numbers, you may not need to
                                                   advertise individual alternate numbers. Expand the PSTN Failover section and choose the Enterprise Number or +E.164 Alternate Number as the PSTN failover to use if normal call routing fails. |
| Step 5 | Click Save . |

| Step 1 | In Cisco Unified CM
                                             			 Administration, choose User
                                                   				  Management > User/Phone Add > Universal Device
                                                   				  Template . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter the following mandatory fields: Enter a Device Description for the template. Select a Device Pool type from the drop-down list. Select a Device Security Profile from the drop-down list. Select a SIP Profile from the drop-down list. Select a Phone Button Template from the drop-down list. |
| Step 4 | Complete the remaining fields in the Universal Device Template Configuration window. For field descriptions, see the online help. |
| Step 5 | Under Phone Settings , complete the following optional fields: If you configured a Common Phone Profile , assign the profile. If you configured a Common Device Configuration , assign the configuration. If you configured a Feature Control Policy , assign the policy. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > User Profile . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | Enter a Name and Description for the user profile. |
| Step 4 | Assign a Universal Device Template to apply to users' Desk
                                                				Phones , Mobile
                                                				and Desktop Devices , and Remote
                                                				Destination/Device Profiles . |
| Step 5 | Assign a Universal Line Template to apply to the phone lines
                                             			 for users in this user profile. |
| Step 6 | If you want
                                             			 the users in this user profile to be able to use the self-provisioning feature
                                             			 to provision their own phones, do the following: Check the Allow End User to Provision their own phones check box. In the Limit Provisioning once End User has this many phones field, enter a maximum number of phones the user is allowed to provision. The maximum is 20. Check the Allow Provisioning of a phone already assigned to a different End User check box to determine whether the user who is associated with this profile has the permission to migrate or reassign a device
                                                   that is already owned by another user. By default, this check box is unchecked. |
| Step 7 | If you want Cisco Jabber users who are associated with this user profile, to be able to use the Mobile and Remote Access feature,
                                             check the Enable Mobile and Remote Access check box. Note By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default. This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                                  setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                                  and Remote Access users and not to any other endpoints or clients. | Note | By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default. This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                                  setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                                  and Remote Access users and not to any other endpoints or clients. |
| Note | By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default. This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                                  setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                                  and Remote Access users and not to any other endpoints or clients. |
| Step 8 | Assign the Jabber policies for this user profile. From the Desktop Client Policy , and Mobile Client Policy drop-down list, choose one of the following options: No Service—This policy disables access to all Cisco Jabber services. IM & Presence only—This policy enables only instant messaging and presence capabilities. IM & Presence, Voice and Video calls—This policy enables instant messaging, presence, voicemail, and conferencing capabilities
                                                for all users with audio or video devices. This is the default option. Note Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                            Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. | Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                            Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
| Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                            Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
| Step 9 | If you want the users in this user profile to set the maximum login time for Extension Mobility or Extension Mobility Cross
                                             Cluster through Cisco Unified Communications Self Care Portal, check the Allow End User to set their Extension Mobility maximum login time check box. Note By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. | Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
| Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
| Step 10 | Click Save . |

| Note | By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default. This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                                  setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                                  and Remote Access users and not to any other endpoints or clients. |
|---|---|

| Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                            Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
|---|---|

| Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
|---|---|

| Step 1 | In Cisco
                                             			 Unified CM Administration, choose User
                                                   				  Management > User/Phone Add > Feature Group
                                                   				  Template . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | Enter a Name and Description for the Feature Group Template. |
| Step 4 | Check the Home Cluster check box if you want to use the local cluster as the home cluster for all users whom use this template. |
| Step 5 | Check the Enable User for Unified CM IM and Presence check box to allow users whom use this template to exchange instant messaging and presence information. |
| Step 6 | From the drop-down list, select a Services Profile and User Profile . |
| Step 7 | Complete the
                                             			 remaining fields in the Feature
                                                				Group Template Configuration window. Refer to the online help for
                                             			 field descriptions. |
| Step 8 | Click Save . |

| Note | You cannot add new configurations (for example, adding a feature group template) into an LDAP directory sync after the initial
                                             sync has occurred. If you want to edit an existing LDAP sync, you must either use Bulk Administration, or configure a new
                                             LDAP  sync. |
|---|---|

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose System > LDAP > LDAP
                                                				  Directory . |
|---|---|
| Step 2 | Click Find and select the LDAP directory to which the user
                                          			 is added. |
| Step 3 | Click Perform Full Sync . Cisco
                                          			 Unified Communications Manager synchronizes with the external LDAP directory.
                                          			 Any new end users in the LDAP directory are imported into the Cisco Unified
                                          			 Communications Manager database. |

| Note | Make sure that you have already set up an access control groups that has the role permissions to which you want to assign
                                          your user. For details, see the "Manage User Access" chapter. |
|---|---|

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > User/Phone Add > Quick User/Phone
                                                				  Add . |
|---|---|
| Step 2 | Enter the User ID and Last Name . |
| Step 3 | From the Feature Group Template drop-down list, select a
                                          			 feature group template. |
| Step 4 | Click Save . |
| Step 5 | From the User
                                             				Profile drop-down list, verify that the selected user profile
                                          			 includes a universal line template. |
| Step 6 | From the Access
                                             				Control Group Membership section, click the + icon. |
| Step 7 | From the User
                                             				is a member of drop-down list, select an access control group. |
| Step 8 | Under Primary Extension , click the + icon. |
| Step 9 | From the Extension drop-down list, select a DN that displays as (available) . |
| Step 10 | If all line
                                          			 extensions display as (used) , perform the following steps: Click the New... button. The Add
                                                   					 New Extension popup displays. In the Directory Number field, enter a new line extension. From the Line Template drop-down list, select a universal line template. Click OK . Cisco Unified Communications Manager configures the directory
                                                				  number with the settings from the universal line template. |
| Step 11 | (Optional) Complete any additional fields in the Quick User/Phone Add Configuration window. |
| Step 12 | Click Save . |

| Step 1 | In Cisco Unified CM Administration, choose User Management > User/Phone Add > Quick/User Phone Add . |
|---|---|
| Step 2 | Click Find and select the end user for whom you want to
                                          			 add a new phone. |
| Step 3 | Click the Manage Devices . The Manage Devices window appears. |
| Step 4 | Click Add
                                             				New Phone . The Add
                                          			 Phone to User popup displays. |
| Step 5 | From the Product Type drop-down list, select the phone model. |
| Step 6 | From the Device Protocol drop-down list select SIP or SCCP as the protocol. |
| Step 7 | In the Device
                                             				Name text box, enter the device MAC address. |
| Step 8 | From the Universal Device Template drop-down list, select a
                                          			 universal device template. |
| Step 9 | If the phone
                                          			 supports expansion modules, enter the number of expansion modules that you want
                                          			 to deploy. |
| Step 10 | If you want to
                                          			 use Extension Mobility to access the phone, check the In
                                             				Extension Mobility check box. |
| Step 11 | Click Add
                                             				Phone . The Add
                                          			 New Phone popup closes. Cisco Unified Communications Manager adds the phone to
                                          			 the user and uses the universal device template to configure the phone. |
| Step 12 | If you want to make additional edits to the phone configuration, click the corresponding Pencil icon to open the phone in
                                          the Phone Configuration window. |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > User/Phone Add > Quick/User Phone
                                                				  Add . |
|---|---|
| Step 2 | Click Find and select the user to whom you want to move an
                                          			 existing phone. |
| Step 3 | Click the Manage
                                             				Devices button. |
| Step 4 | Click the Find a
                                             				Phone to Move To This User button. |
| Step 5 | Select the
                                          			 phone that you want to move to this user. |
| Step 6 | Click Move
                                             				Selected . |

| Step 1 | In Cisco
                                          			 Unified Communications Manager Administration, choose User Management > End User . The Find
                                             				and List Users window appears. |
|---|---|
| Step 2 | To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, click Find to retrieve a list of users, and then select
                                          			 the user from the list. The End
                                             				User Configuration window is displayed. |
| Step 3 | In the PIN field, double-click the existing PIN, which is
                                          			 encrypted, and enter the new PIN. You must enter at least the minimum number of
                                          			 characters that are specified in the assigned credential policy (1-127
                                          			 characters). |
| Step 4 | In the Confirm PIN field, double-click the existing,
                                          			 encrypted PIN and enter the new PIN again. |
| Step 5 | Click Save . Note You can
                                                         				  login to Extension Mobility, Conference Now, Mobile Connect, and Cisco Unity
                                                         				  Connection voicemail with the same end user PIN, if End User Pin synchronization checkbox is enabled in
                                                         				  the Application Server Configuration window for Cisco Unity Connection. End users can use the same PIN to log in
                                                            					 to Extension Mobility and to access their voicemail. | Note | You can
                                                         				  login to Extension Mobility, Conference Now, Mobile Connect, and Cisco Unity
                                                         				  Connection voicemail with the same end user PIN, if End User Pin synchronization checkbox is enabled in
                                                         				  the Application Server Configuration window for Cisco Unity Connection. End users can use the same PIN to log in
                                                            					 to Extension Mobility and to access their voicemail. |
| Note | You can
                                                         				  login to Extension Mobility, Conference Now, Mobile Connect, and Cisco Unity
                                                         				  Connection voicemail with the same end user PIN, if End User Pin synchronization checkbox is enabled in
                                                         				  the Application Server Configuration window for Cisco Unity Connection. End users can use the same PIN to log in
                                                            					 to Extension Mobility and to access their voicemail. |

| Note | You can
                                                         				  login to Extension Mobility, Conference Now, Mobile Connect, and Cisco Unity
                                                         				  Connection voicemail with the same end user PIN, if End User Pin synchronization checkbox is enabled in
                                                         				  the Application Server Configuration window for Cisco Unity Connection. End users can use the same PIN to log in
                                                            					 to Extension Mobility and to access their voicemail. |
|---|---|

| Step 1 | In Cisco
                                          			 Unified Communications Manager Administration, choose User Management > End User . The Find
                                             				and List Users window appears. |
|---|---|
| Step 2 | To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, click Find to retrieve a list of users, and then select
                                          			 the user from the list. The End
                                             				User Configuration window is displayed. |
| Step 3 | In the Password field, double-click the existing password,
                                          			 which is encrypted, and enter the new password. You must enter at least the
                                          			 minimum number of characters that are specified in the assigned credential
                                          			 policy (1-127 characters). |
| Step 4 | In the Confirm Password field, double-click the existing,
                                          			 encrypted password and enter the new password again. |
| Step 5 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified Communications Manager Administration, choose User Management > End User . The Find
                                             				and List Users window appears. |
|---|---|
| Step 2 | To select an
                                          			 existing user, specify the appropriate filters in the Find
                                             				User Where field, click Find to retrieve a list of users, and then select
                                          			 the user from the list. The End
                                             				User Configuration window is displayed. |
| Step 3 | Verify that a
                                          			 primary extension number is associated with this user. Note You must
                                                         				  define a primary extension; otherwise, the Create Cisco Unity User
                                                         				  link does not appear in the Related Links drop-down list. | Note | You must
                                                         				  define a primary extension; otherwise, the Create Cisco Unity User
                                                         				  link does not appear in the Related Links drop-down list. |
| Note | You must
                                                         				  define a primary extension; otherwise, the Create Cisco Unity User
                                                         				  link does not appear in the Related Links drop-down list. |
| Step 4 | From the Related Links drop-down list, choose the Create Cisco Unity User
                                          			 link, and then click Go . The Add Cisco Unity User
                                             				dialog box appears. |
| Step 5 | From
                                          			 the Application Server drop-down list, choose the Cisco Unity
                                             				Connection server on which you want to create a Cisco Unity
                                             				Connection user, and then click Next . |
| Step 6 | From the Subscriber Template drop-down list, choose the
                                          			 subscriber template that you want to use. |
| Step 7 | Click Save . The mailbox is
                                             				created. The link in the Related Links drop-down list changes to Edit Cisco Unity User
                                             				in the End
                                                				  User Configuration window. In Cisco Unity Connection
                                                				  Administration , you can now view the user that you created. Note After you
                                                         				  integrate the Cisco Unity
                                                            					 Connection user with the Cisco Unified
                                                            					 Communications Manager end user, you cannot edit fields in Cisco Unity Connection
                                                            					 Administration such as Alias (User ID in Cisco Unified CM
                                                         				  Administration), First Name, Last Name, and Extension (Primary Extension in
                                                         				  Cisco Unified CM Administration). You can only update these fields in Cisco
                                                         				  Unified CM Administration. | Note | After you
                                                         				  integrate the Cisco Unity
                                                            					 Connection user with the Cisco Unified
                                                            					 Communications Manager end user, you cannot edit fields in Cisco Unity Connection
                                                            					 Administration such as Alias (User ID in Cisco Unified CM
                                                         				  Administration), First Name, Last Name, and Extension (Primary Extension in
                                                         				  Cisco Unified CM Administration). You can only update these fields in Cisco
                                                         				  Unified CM Administration. |
| Note | After you
                                                         				  integrate the Cisco Unity
                                                            					 Connection user with the Cisco Unified
                                                            					 Communications Manager end user, you cannot edit fields in Cisco Unity Connection
                                                            					 Administration such as Alias (User ID in Cisco Unified CM
                                                         				  Administration), First Name, Last Name, and Extension (Primary Extension in
                                                         				  Cisco Unified CM Administration). You can only update these fields in Cisco
                                                         				  Unified CM Administration. |

| Note | You must
                                                         				  define a primary extension; otherwise, the Create Cisco Unity User
                                                         				  link does not appear in the Related Links drop-down list. |
|---|---|

| Note | After you
                                                         				  integrate the Cisco Unity
                                                            					 Connection user with the Cisco Unified
                                                            					 Communications Manager end user, you cannot edit fields in Cisco Unity Connection
                                                            					 Administration such as Alias (User ID in Cisco Unified CM
                                                         				  Administration), First Name, Last Name, and Extension (Primary Extension in
                                                         				  Cisco Unified CM Administration). You can only update these fields in Cisco
                                                         				  Unified CM Administration. |
|---|---|