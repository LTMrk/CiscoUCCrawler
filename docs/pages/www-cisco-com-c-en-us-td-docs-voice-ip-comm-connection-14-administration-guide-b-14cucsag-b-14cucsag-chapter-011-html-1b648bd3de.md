---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-administration-guide-b-14cucsag-b-14cucsag-chapter-011-html-1b648bd3de
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag/b_14cucsag_chapter_011.html
retrieved_at: 2026-08-17T02:15:56.170083+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 18, 2025

Chapter: Users

## Chapter: Users

# Users

## Introduction

Users in Cisco Unity Connection are the user
                              		  accounts that determine who can access the system and which system features and
                              		  resources they can use (other than the ones already controlled by the
                              		  associated class of service). Unity Connection supports the following types of
                              		  users:

Users With Voice Mailboxes

Includes the users who need to send or
                                          						receive voice messages and use other Unity Connection features, such as
                                          						personal call transfer rules and Web Inbox or Messaging Inbox depending on the
                                          						class of service assigned to the user.

A user account that is set up with a
                                          						voice mailbox has a phone extension and is counted as a voicemail licensed
                                          						user.

Users Without Voice Mailboxes

Includes the users who do not need to
                                          						send or receive voice messages but need to administer the system. You can
                                          						determine the tasks that the administrators can do by assigning any of the
                                          						predefined roles to the user.

An account that is set up without a
                                          						voice mailbox does not have a phone extension and is not counted as a voicemail
                                          						licensed user.

## Default Users

By default, Unity Connection creates the following user accounts, which you use when setting up the system.

Administrator

The Administrator user account has the highest level of administrative privileges (System Administrator role) and is used
                                          to access Cisco Unity Connection Administration. The alias and password for this account are specified during installation.
                                          This account is configured as a user without a voice mailbox.

The default Administrator account can be deleted. However, be sure that you have assigned the System Administrator role to
                                          at least one other user before you delete this account.

Operator

The Operator user account is the message recipient for the Operator call handler. When calls to the operator go unanswered,
                                          callers can leave a message, depending on the call transfer settings for the Operator call handler. You should assign someone
                                          to monitor the mailbox for the Operator user account or reconfigure the Operator call handler to send messages to a different
                                          user or a distribution list.

This account cannot be deleted.

Undeliverable Messages Mailbox

By default, the Undeliverable Messages Mailbox user account is the only member of the Undeliverable Messages distribution
                                          list, which receives notification of undeliverable messages. You should assign someone to monitor this mailbox or add a user
                                          to the Undeliverable Messages distribution list to monitor and reroute (as appropriate) any messages that are delivered to
                                          the list.

This account cannot be deleted.

Unity Connection Messaging System

The Unity Connection Messaging System user account is configured as a user without a voice mailbox. It acts as a surrogate
                                          sender of messages from outside callers. Thus, messages from outside callers are identified as coming from the Unity Connection
                                          Messaging System mailbox.

This account cannot be deleted.

The default user accounts are not included in your user license count.

## Finding
                        	 Users

Cisco Unity Connection Administration allows you to find users
                              		  based on search criteria that you enter. You can enter all or part of a name,
                              		  extension, and/or user alias (ID) to find a user.

As a best practice, do not use wildcards such as * in search
                              		  strings. If you want to find a user, use Begins With, Contains, or Ends With to
                              		  match part of a string, or leave the search string blank to return all results.
                              		  Unity Connection attempts to match wildcard characters within the field you are
                              		  searching; if no objects contain such characters in that field, no results are
                              		  returned.

You can use the Search Limits fields on the search page to limit
                              		  the results that are displayed to a particular partition in which user
                              		  extensions are configured, or to a particular location if the directory
                              		  contains users from other digitally-networked Unity Connection locations. When
                              		  you search for users and limit the results by partition, you can also choose
                              		  whether to display only users whose primary extension is in the partition, or
                              		  users whose primary extension and any alternate extensions appear in the
                              		  partition. If you choose to display the primary extension and any alternate
                              		  extensions, multiple records may display for a single user in the search
                              		  results.

You can use the navigation
                              		  buttons at the bottom of the search results table to move between pages, and
                              		  use the Rows Per Page setting to display 25, 50, 100, 150, 200, or 250 rows per
                              		  page. Unity Connection saves your Rows Per Page setting so that on subsequent
                              		  sign-ins you receive the same number of results per page for this search page.

Step 1

In Cisco Unity Connection Administration, select Users .

Step 2

On the Search Users page, in the Search Results table, select
                                       			 the user alias to display the user account.

If you do not see the user alias listed in the Search Results
                                          				table, continue with Step 3.

Step 3

In the Find Users Where search fields, indicate whether to
                                       			 search by Alias, extension, First Name, Last Name, or Display Name. You can
                                       			 further refine your search by setting additional parameters, such as Begins
                                       			 With or Ends With. Enter the applicable characters to search for, and select Find .

Step 4

To limit the search results by partition or location, do the
                                       			 following:

In the Limit Search To list, select Partition or Location .

In the Where Name Is list, select the name of the partition or
                                             				  location in which you want to find the user.

When limiting the search to a partition, select whether to
                                                					 display only primary extensions in the partition or both primary and alternate
                                                					 extensions in the partition.

If you select to display both the primary extension and any
                                                            						alternate extensions, multiple records may display for a single user in the
                                                            						search results.

Step 5

In the Search Results table, select the user alias to display
                                       			 the user account.

## Creating User
                        	 Accounts

Before creating user accounts, you must configure user templates
                           		and class of service that want to use to create the accounts. After creating a
                           		user account, the changes made to the associated user template does not apply
                           		to the account. For more information on user templates or class of service, see
                           		<User Attributes> chapter.

You can use either of the following methods to create users in
                           		Unity Connection:

Creating Users Manually: Allows to manually create each user
                                 			 through Search Users page. For information, see Creating User Accounts Manually .

Importing Users from Cisco Unified Communications Manager:
                                 			 Allows you to import users from Cisco Unified Communications Manager to Unity
                                 			 Connection using AXL. For information, see Importing Users through AXL .

Importing Users from LDAP Directory: Allows you to import users
                                 			 from LDAP directory to Unity Connection. For information, see Importing Users using LDAP Directory .

Creating Users through Bulk Administration Tool (BAT): Allows
                                 			 you to create multiple users using BAT at the same time. For information, see Creating User Accounts using BAT .

### Creating User
                           	 Accounts Manually

Users with voice mailboxes are end users and the users without
                              		voice mailboxes are system administrators. Before you add user accounts
                              		individually, you need to select and define a template and class of service
                              		(COS) for each type of account you need to add. For administrator accounts, you
                              		also need to select the roles that are assigned to each account. To learn more
                              		about the tasks you should do before adding a user account, see the User Attributes chapter.

In case of end users, the default voicemail PINs and web
                              		application passwords are applied to each user account that you create. These
                              		PINs and passwords are either the defaults set for the default Voicemail User
                              		Template during installation, or defaults that are set on the Change Password
                              		page for the user template that you select when creating the accounts. You need
                              		to give these PINs and passwords to users so that they can sign in to the Unity
                              		Connection conversation and to the Cisco Personal Communications Assistant
                              		(PCA). To increase system security, you need to instruct users to change both
                              		PIN and password as soon as possible and you need to enforce PIN and password
                              		complexity rules.

When you create administrator accounts, consider the following
                              		security issues:

By default, the user without a voice mailbox template specifies
                                    			 the System Administrator role, which is the administrator role with the highest
                                    			 privileges.

A default web application password is applied to each
                                    			 administrative account that you create. If you use the default Administrator
                                    			 Template to create a new account, keep in mind that the default password
                                    			 associated with that account is a randomly-generated string. Therefore, make
                                    			 sure to first enter a new default password for the template to replace the
                                    			 randomly-generated string or change the password for each new account that you
                                    			 create it based on the default Administrator Template. To increase system
                                    			 security, you must instruct administrators to change the password as soon as
                                    			 possible and you must enforce password complexity rules also.

If system administrators in your organization require voice
                                    			 mailboxes, you must set up separate accounts for each system administrator.
                                    			 This means that you must create a user account without voice account for
                                    			 signing in to Unity Connection Administration to do administrative tasks and a
                                    			 separate user account with a voice mailbox for sending and receiving voice
                                    			 messages.

Do the following procedure to add a user account with or without
                              		a voice mailbox.

The information in this section is not applicable for adding end
                                          		  user accounts in Cisco Business Edition.

### Adding a User
                           	 Account

Step 1

In Cisco Unity Connection Administration, select Users .

Step 2

On the Search Users page, select Add New . The New User page appears. (For information on each
                                          			 field, select Help > This Page.)

Step 3

In the User Type list, do either of the following:

- Select User With Mailbox to create an end user account.

- Select User Without Mailbox to create an administrator account.

Step 4

In the Based on Template list, do either of the following:

- Select VoiceMailUserTemplate for end user account.

- Select AdministratorTemplate for administrator account.

Step 5

Enter the required information in the fields.

Step 6

Select Save . The Edit User Basics page appears.

Step 7

Enter the additional information as applicable and select Save .

#### Importing Users
                              	 through AXL

Unity Connection requires an Administrative XML Layer (AXL)
                                 		server to access the Cisco Unified Communications Manager database, therefore,
                                 		you must configure an AXL server for the Cisco Unified CM server from which you
                                 		want to import the users. AXL is an Application Programming Interface (API)
                                 		that provides a mechanism for inserting, retrieving, updating, and removing
                                 		data from the database.

Prior to importing users, you must do the
                                 		following on the Cisco Unity Connection server:

Edit or add a user template. In the Phone System field for the
                                       			 template, select the Cisco Unified CM server from which you are importing
                                       			 users.

Configure an AXL server for the Cisco Unified CM server from
                                       			 which you are importing users. For details on configuring AXL servers, see the
                                       			 section Cisco Unified Communications Manager AXL Servers

You use the Users > Import Users page in Cisco Unity
                                 		Connection Administration to create multiple user with voicemail accounts from
                                 		Cisco Unified CM users. For more information see, Using Import Users and Synch Users Functionalities .

Cisco Unified CM users must have a Primary Extension defined
                                             		  otherwise the users do not appear on the Users > Import Users page in
                                             		  Cisco Unity Connection Administration.

When user accounts are created using this method, Unity
                                 		Connection takes the user Alias, Extension, First Name, Last Name, and all the
                                 		other available data from the end user table of Cisco Unified CM and fills the
                                 		remaining information from the user template that you specify. The data from
                                 		the fields that are taken from Cisco Unified CM cannot be modified using Unity
                                 		Connection Administration. The method that you can use to update the data in
                                 		Unity Connection depends on whether Cisco Unified CM is integrated with an LDAP
                                 		directory:

If Cisco Unified CM is not integrated with an LDAP
                                          				directory: You must change the data in Cisco Unified Communications Manager
                                       			 Administration and then use the Synch Users page in Unity
                                       			 Connection Administration to manually refresh information from Cisco Unified CM
                                       			 for voicemail users that were created using the Import Users page.

If Cisco Unified CM is integrated with an LDAP directory: You must update the data in the LDAP directory, resynchronize the Cisco
                                       			 Unified CM database with the LDAP directory, and then use the Synch Users page
                                       			 in Unity Connection Administration to manually refresh information from Cisco
                                       			 Unified CM for voicemail users that were created using the Import Users page.

#### Considerations
                              	 While Importing Data From LDAP Directory Integrated with Cisco
                              	 Unified CM

An alternative of creating users by importing data from Cisco
                                 		Unified Communications Manager is to integrate Unity Connection with an LDAP
                                 		directory and then import user data from the LDAP directory as described in the LDAP chapter. Note the
                                 		following:

If you import users from Cisco Unified CM and if Cisco
                                       			 Unified CM is integrated with the LDAP directory, Unity Connection does not
                                       			 automatically have access to LDAP synchronization or authentication. If you
                                       			 want Unity Connection users to authenticate against the LDAP directory, you
                                       			 must integrate Unity Connection with the LDAP directory, too.

If you import users from Cisco Unified CM, updates to Cisco
                                       			 Unified CM data do not automatically replicate to the Unity Connection server,
                                       			 so you must use the Synch Users page in Cisco Unity Connection Administration
                                       			 to manually synchronize Unity Connection user data with Cisco Unified CM user
                                       			 data from time to time. If you integrate Unity Connection with an LDAP
                                       			 directory, you can define a synchronization schedule that specifies when data
                                       			 in the Unity Connection database is automatically resynchronized with data in
                                       			 the LDAP directory.

Note that when you add users to the LDAP directory, you still
                                 		need to manually import them into Unity Connection; automatic synchronization
                                 		only updates the Unity Connection database with new data for existing users,
                                 		not new data for new users.

When you integrate Unity Connection with an LDAP directory, you
                                       			 can configure Unity Connection to authenticate passwords for web applications
                                       			 against the LDAP database. When you import data from Cisco Unified CM, you must
                                       			 maintain passwords for Unity Connection web applications in Unity Connection
                                       			 and for Cisco Unified CM web applications in Cisco Unified CM.

### Importing Users
                           	 using LDAP Directory

You can use Import Users functionality to import users from the
                              		LDAP directory to Unity Connection server. For more information on configuring
                              		LDAP, see the LDAP chapter.

### Creating User
                           	 Accounts using BAT

Cisco Unity Connection provides the Bulk Administration Tool
                              		that allows you to create, update, and delete multiple user accounts or
                              		contacts at the same time by importing information contained in a comma
                              		separated value (CSV) file. In addition, it allows you to export information
                              		about users or contacts from Cisco Unity Connection to a CSV file.

For information on how to create users using BAT, see the Bulk Administration Tool section.

## Using Import Users and Synch Users Functionalities

You can use the Import Users functionality to import existing Cisco Unified CM users in Unity Connection. After importing
                           users from Cisco Unified CM, you can use the Synch Users functionality to manually refresh the information you imported from
                           Cisco Unified CM.

In Cisco Business Edition configurations, synchronization happens automatically. You are not required to manually synchronize
                                       the users.

You can also use Import Users functionality to import users from an LDAP directory.

A Cisco Unified CM or LDAP directory server must be integrated with Unity Connection before importing the users.

### Accessing the Import and Synch Users Tools

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Users .

Step 2

Select Import Users or Synch Users , as
                                          			 applicable.

## Editing User Account

After a Cisco Unity Connection user account has been created, you may need to adjust settings (for example, to reset a user
                           PIN or password or to set up new notification devices for the user) or delete the account.

### Editing Individual
                           	 User Account

You can edit settings for an individual user account from the
                                 		  pages available on the Edit menu in Cisco Unity Connection Administration.

Do the following procedure to edit
                                 		  individual user account settings.

Step 1

In Cisco Unity Connection Administration, select Users .

Step 2

On the Search Users page, select the alias of the user account
                                          			 that you want to edit.

If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find .

Step 3

On the Edit User Basics page, change the applicable settings.
                                          			 When you have finished, select Save .

Step 4

On the Edit menu, select any of the following settings that you
                                          			 want to edit and select Save :

User Basics

Password Settings

Change Password

Roles

Message Waiting Indicators

Transfer Rules

Message Settings

Caller Input

Mailbox

Phone Menu

Playback Message Settings

Send Message Settings

Message Actions

Greetings

Post Greeting Recording

Notification Devices

Alternate Extensions

Alternate Names

Private Distribution Lists

Unified Messaging Accounts

Video Services Accounts

SMTP Proxy Addresses

For information on each user settings, see the Settings for User Accounts and User Templates section.

### Editing User
                           	 Accounts in Bulk Edit Mode

Bulk Edit option on the Search Users page allows you to
                                 		  select large numbers of user accounts and quickly make the same changes to the
                                 		  selected user account at one time.

If you have multiple locations in your network and want to edit
                                 		  the data across the network in Bulk Edit mode, you need to configure remote
                                 		  access to other locations in your network before attempting a Bulk Edit
                                 		  operation. For more information on configuring location passwords, see the Connection Location Passwords section of the Networking chapter.

The following procedure provides instructions for beginning a
                                 		  Bulk Edit operation.

Step 1

In Cisco Unity Connection Administration, on the Search Users
                                          			 page, check the applicable user check boxes, and select Bulk Edit .

Step 2

On the Edit User Basics page, change settings as applicable.

While updating settings for multiple video service accounts
                                                               						in Bulk Edit mode, you can only map or unmap the video service for the
                                                               						accounts. To create or update the video service accounts for multiple users
                                                               						simultaneously, you can use Bulk Administration Tool. For more information, see Bulk Administration Tool

You can also set the Bulk Edit Task Scheduling field to
                                                               						schedule the Bulk Edit operation for a later date and/or time.

Step 3

Select Submit .

Step 4

If applicable, continue to change settings for these user
                                          			 accounts on the related pages available from the Edit menu. As you make changes
                                          			 on each page, select Submit before going on to the next page to make
                                          			 additional changes.

### Editing User
                           	 Accounts through BAT

BAT allows you to edit Unity Connection user accounts (with or
                              		without voice mailboxes) using the information contained in a comma separated
                              		value (CSV) file. For more information on using BAT tool and CSV file, see the Bulk Administration Tool section.

## Deleting User Accounts

In Cisco Business Edition, you delete Cisco Unity Connection user accounts in Cisco Unified CM Administration. (Use the applicable
                                       User Management page to find the user or application user, then delete.)

To learn more about deleting Unity Connection accounts in Cisco Unified CM Administration, see the online Help or the “Application
                                       User Deletion” and “End User Setup” chapters of the applicable Cisco Unified Communications Manager Administration Guide.
                                       The guide is available at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

When a user leaves the organization or otherwise no longer needs a Unity Connection account, delete the account in Cisco Unity
                           Connection Administration.

Note the following considerations for deleting an account:

All messages in the Unity Connection voice mailbox for the user are automatically deleted. However, if Unity Connection and
                                 Exchange mailbox synchronization (single inbox) is configured for the user, Unity Connection voice messages are not deleted
                                 from the corresponding Exchange mailbox (the single-inbox feature is available in Unity Connection).

If a user account is referenced by other objects in Unity Connection (for example, if the user is set to be a recipient of
                                 messages left in an interview handler or if a call handler is set to transfer incoming calls to the user phone), you are not
                                 allowed to delete the user account until you have changed settings on the other objects to remove references to the user account
                                 you want to delete. If you try to delete a user account without first changing settings on objects that reference the user
                                 account, the delete operation fails.

An administrator is prohibited from deleting his or her own account from Unity Connection Administration.

When you delete the account of a user with a voice mailbox, that user is automatically deleted from the All Voice Mail Users
                                 distribution list.

If the account for a user has a voice mailbox and if the mailbox store for that voice mailbox is disabled (for example, because
                                 the mailbox store is being backed up), the user account cannot be deleted.

If the user account that you are deleting is for a user who is listed as a caller in a personal call transfer rule of another
                                 user, the user is removed from the rule and no notice is sent to the user who set up the rule. In addition, if you search
                                 for dependencies prior to deleting user accounts, the presence of those users in personal call transfer rules are not reported.

The behavior is different when Unity Connection or Cisco Business Edition is integrated with an LDAP directory:

If Unity Connection is integrated with an LDAP directory, you must delete the user both in the LDAP directory and in Unity
                                 Connection. If you delete the user only in Unity Connection, the LDAP user is unaffected. If you delete the user only in the
                                 LDAP directory, in Unity Connection Administration, the Status area on the Edit User Basics page for that user indicates that
                                 the Unity Connection user is inactive. The status cannot be changed manually, but after 48 hours, the user is automatically
                                 converted to a regular Unity Connection user, and the message in the Status area no longer appears.

Unity Connection functionality is mostly unaffected by the deletion of an LDAP user. However, if you use LDAP authentication
                           for Unity Connection web applications or for IMAP access to Unity Connection voice messages, the user cannot access Unity
                           Connection web applications for the 48 hours after the LDAP user is deleted and before the Unity Connection user is converted
                           to a regular Unity Connection user. After 48 hours, you must enter a new web application password for the user in Unity Connection Administration.

If Cisco Business Edition is integrated with an LDAP directory, you must start by deleting the LDAP user that corresponds
                                 with the Unity Connection user. When Cisco Unified CM data is next synchronized with the LDAP directory, the user is deleted
                                 from the Cisco Unified CM database. When the user no longer appears in Cisco Unified CM Administration, you can use Unity
                                 Connection Administration to delete the user from the Unity Connection database.

If LDAP synchronization is not enabled and if you do not manually synchronize Cisco Unified CM data with the LDAP directory,
                                             the deletion of an LDAP user is never replicated to the Cisco Unified CM database, and the corresponding Unity Connection
                                             user cannot be deleted.

See the following procedures:

### Deleting User
                           	 Accounts Manually

Step 1

In Cisco Unity Connection Administration, select Users > Users.

Step 2

On the Search Users page, check the check box next to the user
                                          			 account that you want to delete.

If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find .

Step 3

Select Show Dependencies to search for any database objects that
                                          			 have dependencies on the user you want to delete.

Step 4

From the dependencies search results, follow links to the
                                          			 affected objects and reassign the dependency to another user.

Step 5

Select Tools > Show Dependency Results.

Step 6

On the Show Dependency Results page, select Display Previous
                                          			 Results.

Step 7

Repeat Step 4 through Step 6 until all dependencies have been
                                          			 reassigned.

Step 8

Select Users > Users.

Step 9

On the Search Users page, check the check box next to the user
                                          			 account that you want to delete.

Step 10

Select Delete Selected .

Step 11

In the dialog box that opens, asking you to confirm the
                                          			 deletion, select OK .

You can also use BAT to delete multiple users at the same time.
                                                         				  For more information, see the Bulk Administration Tool section.

## Moving or Migrating Users Between Locations in Cisco Unity Connection

Occasionally, you may need to move one or more user accounts from one Unity Connection server or cluster to another, for load
                           balancing or other reasons. Or, you may need to migrate many or all of the users from one server or cluster to another. In
                           this chapter, the server or cluster from which you move users is referred to as the source location, and the server or cluster
                           to which you move the users is referred to as the target location.

The information in this chapter is not applicable to Cisco Business Edition.

### Moving One or
                           	 Several Users Between Networked Unity Connection Locations

The information in this section is not applicable to Cisco
                                          		  Business Edition.

To move users with voice mailboxes between Cisco Unity
                              		Connection locations (where a location represents either a server or cluster on
                              		the network), you use Cisco Object Backup and Restore Application Suite
                              		(COBRAS) Hot Mode. Hot Mode moves the user profile information and the user
                              		mailbox (including all new and saved voice messages, but not including deleted
                              		voice messages, receipts, faxes or email messages) from the source location to
                              		the target location. In the process, information about the moved users is
                              		modified on both the source and target locations, and when replication is
                              		complete, all locations in the site or organization are appropriately updated.
                              		To use Hot Mode, both the source and target locations must be running Unity
                              		Connection, and the locations must be networked via intrasite or intersite
                              		networking.

Hot Mode is designed to be used on a single user or a small
                              		group of users at a time. Compared to COBRAS Briefcase Mode, Hot Mode has the
                              		advantage of preserving relationships between objects (for example, the private
                              		distribution lists of a user and personal call transfer rules that reference
                              		the user being moved are updated automatically to point to the new location).
                              		However, Hot Mode moves can be slow. If you need to move large groups of users
                              		or migrate servers and are not concerned about preserving such relationships,
                              		consider using the COBRAS Briefcase Mode method explained in the Migrating Users Between Unity Connection Locations section. If you are concerned about preserving such relationships, split large
                              		groups of users into small batches when using Hot Mode.

To use Hot Mode, download the latest version of COBRAS, and view
                              		training videos and Help at http://www.ciscounitytools.com/Applications/General/COBRAS/COBRAS.html .

Caution

Before moving users, read the COBRAS help file and the COBRAS
                                          		  Hot Mode for Unity Connection to Unity Connection help file carefully and
                                          		  thoroughly.

### Migrating Users Between Unity Connection Locations

The information in this section is not applicable to Cisco Business Edition.

If the source or target server is running different versions of Unity Connection or if the locations are not networked via
                              intrasite or intersite networking, you use Briefcase Mode in the Cisco Object Backup and Restore Application Suite (COBRAS)
                              tool to move users with voice mailboxes. Rather than moving all pertinent objects from one location to another and cleaning
                              up the original location automatically, Briefcase Mode requires that you copy information from the source location, remove
                              the objects, and then restore them on the target location.

When migrating users in Briefcase Mode, you can choose whether to copy the user voice names and voice messages.

#### Task List for
                              	 Migrating Users Using COBRAS Briefcase Mode

Use the following high-level task list to migrate users in
                                    		  Briefcase Mode:

Step 1

Download the latest version of COBRAS, and view training videos
                                             			 and Help at http://www.ciscounitytools.com/Applications/General/COBRAS/COBRAS.html .

Caution

Before migrating users, read the COBRAS help file and the COBRAS
                                                            				  Briefcase Mode help file carefully and thoroughly.

Step 2

Back up the source and target locations using the Disaster Recovery System. The source backup is not used to restore data
                                             on the target location; you should take back up of each location so you can revert to the previous state of the location if
                                             necessary. For more information, see the Install, Upgrade, and Maintenance Guide Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

Step 3

Use COBRAS Briefcase Mode to export the users to be moved from
                                             			 the source location. See the COBRAS Briefcase Mode help file for instructions.

Step 4

If the source and target locations are connected via any type of
                                             			 networking, delete the users to be moved from the source location. To delete
                                             			 accounts one at a time, see the Deleting User Accounts section.

If the source and target are connected via any type of
                                                            				  networking, it is critical that you delete the users and verify that the
                                                            				  deletion has completed on all networked locations before importing the users on
                                                            				  the target location.

Step 5

Use COBRAS Briefcase Mode to import users on the target
                                             			 location. See the COBRAS Briefcase Mode help file for instructions.

Step 6

If you did not delete the original user accounts from the source
                                             			 location in Task 4. ,
                                             			 delete them now. To delete accounts one at a time, see the Deleting User Accounts .

| Users With Voice Mailboxes | Includes the users who need to send or
                                          						receive voice messages and use other Unity Connection features, such as
                                          						personal call transfer rules and Web Inbox or Messaging Inbox depending on the
                                          						class of service assigned to the user. A user account that is set up with a
                                          						voice mailbox has a phone extension and is counted as a voicemail licensed
                                          						user. |
|---|---|
| Users Without Voice Mailboxes | Includes the users who do not need to
                                          						send or receive voice messages but need to administer the system. You can
                                          						determine the tasks that the administrators can do by assigning any of the
                                          						predefined roles to the user. An account that is set up without a
                                          						voice mailbox does not have a phone extension and is not counted as a voicemail
                                          						licensed user. |

| Administrator | The Administrator user account has the highest level of administrative privileges (System Administrator role) and is used
                                          to access Cisco Unity Connection Administration. The alias and password for this account are specified during installation.
                                          This account is configured as a user without a voice mailbox. The default Administrator account can be deleted. However, be sure that you have assigned the System Administrator role to
                                          at least one other user before you delete this account. |
|---|---|
| Operator | The Operator user account is the message recipient for the Operator call handler. When calls to the operator go unanswered,
                                          callers can leave a message, depending on the call transfer settings for the Operator call handler. You should assign someone
                                          to monitor the mailbox for the Operator user account or reconfigure the Operator call handler to send messages to a different
                                          user or a distribution list. This account cannot be deleted. |
| Undeliverable Messages Mailbox | By default, the Undeliverable Messages Mailbox user account is the only member of the Undeliverable Messages distribution
                                          list, which receives notification of undeliverable messages. You should assign someone to monitor this mailbox or add a user
                                          to the Undeliverable Messages distribution list to monitor and reroute (as appropriate) any messages that are delivered to
                                          the list. This account cannot be deleted. |
| Unity Connection Messaging System | The Unity Connection Messaging System user account is configured as a user without a voice mailbox. It acts as a surrogate
                                          sender of messages from outside callers. Thus, messages from outside callers are identified as coming from the Unity Connection
                                          Messaging System mailbox. This account cannot be deleted. |

| Note | The default user accounts are not included in your user license count. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, select Users . |
|---|---|
| Step 2 | On the Search Users page, in the Search Results table, select
                                       			 the user alias to display the user account. If you do not see the user alias listed in the Search Results
                                          				table, continue with Step 3. |
| Step 3 | In the Find Users Where search fields, indicate whether to
                                       			 search by Alias, extension, First Name, Last Name, or Display Name. You can
                                       			 further refine your search by setting additional parameters, such as Begins
                                       			 With or Ends With. Enter the applicable characters to search for, and select Find . |
| Step 4 | To limit the search results by partition or location, do the
                                       			 following: In the Limit Search To list, select Partition or Location . In the Where Name Is list, select the name of the partition or
                                             				  location in which you want to find the user. When limiting the search to a partition, select whether to
                                                					 display only primary extensions in the partition or both primary and alternate
                                                					 extensions in the partition. Note If you select to display both the primary extension and any
                                                            						alternate extensions, multiple records may display for a single user in the
                                                            						search results. | Note | If you select to display both the primary extension and any
                                                            						alternate extensions, multiple records may display for a single user in the
                                                            						search results. |
| Note | If you select to display both the primary extension and any
                                                            						alternate extensions, multiple records may display for a single user in the
                                                            						search results. |
| Step 5 | In the Search Results table, select the user alias to display
                                       			 the user account. |

| Note | If you select to display both the primary extension and any
                                                            						alternate extensions, multiple records may display for a single user in the
                                                            						search results. |
|---|---|

| Note | The information in this section is not applicable for adding end
                                          		  user accounts in Cisco Business Edition. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, select Users . The Search Users page appears displaying the currently
                                          			 configured user accounts. |
|---|---|
| Step 2 | On the Search Users page, select Add New . The New User page appears. (For information on each
                                          			 field, select Help > This Page.) |
| Step 3 | In the User Type list, do either of the following: Select User With Mailbox to create an end user account. Select User Without Mailbox to create an administrator account. |
| Step 4 | In the Based on Template list, do either of the following: Select VoiceMailUserTemplate for end user account. Select AdministratorTemplate for administrator account. |
| Step 5 | Enter the required information in the fields. Note that the SMTP Address field is optional which means that if
                                          			 you do not enter a value, Unity Connection uses the alias to form the SMTP
                                          			 address. However, the SMTP address cannot include non-ASCII characters. Thus,
                                          			 if the user alias contains non-ASCII characters, you must provide an acceptable
                                          			 SMTP address. |
| Step 6 | Select Save . The Edit User Basics page appears. |
| Step 7 | Enter the additional information as applicable and select Save . |

| Note | Cisco Unified CM users must have a Primary Extension defined
                                             		  otherwise the users do not appear on the Users > Import Users page in
                                             		  Cisco Unity Connection Administration. |
|---|---|

| Note | In Cisco Business Edition configurations, synchronization happens automatically. You are not required to manually synchronize
                                       the users. |
|---|---|

| Note | A Cisco Unified CM or LDAP directory server must be integrated with Unity Connection before importing the users. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Users . |
|---|---|
| Step 2 | Select Import Users or Synch Users , as
                                          			 applicable. |

| Step 1 | In Cisco Unity Connection Administration, select Users . |
|---|---|
| Step 2 | On the Search Users page, select the alias of the user account
                                          			 that you want to edit. Note If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find . | Note | If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find . |
| Note | If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find . |
| Step 3 | On the Edit User Basics page, change the applicable settings.
                                          			 When you have finished, select Save . |
| Step 4 | On the Edit menu, select any of the following settings that you
                                          			 want to edit and select Save : User Basics Password Settings Change Password Roles Message Waiting Indicators Transfer Rules Message Settings Caller Input Mailbox Phone Menu Playback Message Settings Send Message Settings Message Actions Greetings Post Greeting Recording Notification Devices Alternate Extensions Alternate Names Private Distribution Lists Unified Messaging Accounts Video Services Accounts SMTP Proxy Addresses Note For information on each user settings, see the Settings for User Accounts and User Templates section. | Note | For information on each user settings, see the Settings for User Accounts and User Templates section. |
| Note | For information on each user settings, see the Settings for User Accounts and User Templates section. |

| Note | If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find . |
|---|---|

| Note | For information on each user settings, see the Settings for User Accounts and User Templates section. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, on the Search Users
                                          			 page, check the applicable user check boxes, and select Bulk Edit . |
|---|---|
| Step 2 | On the Edit User Basics page, change settings as applicable. Note While updating settings for multiple video service accounts
                                                               						in Bulk Edit mode, you can only map or unmap the video service for the
                                                               						accounts. To create or update the video service accounts for multiple users
                                                               						simultaneously, you can use Bulk Administration Tool. For more information, see Bulk Administration Tool You can also set the Bulk Edit Task Scheduling field to
                                                               						schedule the Bulk Edit operation for a later date and/or time. | Note | While updating settings for multiple video service accounts
                                                               						in Bulk Edit mode, you can only map or unmap the video service for the
                                                               						accounts. To create or update the video service accounts for multiple users
                                                               						simultaneously, you can use Bulk Administration Tool. For more information, see Bulk Administration Tool You can also set the Bulk Edit Task Scheduling field to
                                                               						schedule the Bulk Edit operation for a later date and/or time. |
| Note | While updating settings for multiple video service accounts
                                                               						in Bulk Edit mode, you can only map or unmap the video service for the
                                                               						accounts. To create or update the video service accounts for multiple users
                                                               						simultaneously, you can use Bulk Administration Tool. For more information, see Bulk Administration Tool You can also set the Bulk Edit Task Scheduling field to
                                                               						schedule the Bulk Edit operation for a later date and/or time. |
| Step 3 | Select Submit . |
| Step 4 | If applicable, continue to change settings for these user
                                          			 accounts on the related pages available from the Edit menu. As you make changes
                                          			 on each page, select Submit before going on to the next page to make
                                          			 additional changes. |

| Note | While updating settings for multiple video service accounts
                                                               						in Bulk Edit mode, you can only map or unmap the video service for the
                                                               						accounts. To create or update the video service accounts for multiple users
                                                               						simultaneously, you can use Bulk Administration Tool. For more information, see Bulk Administration Tool You can also set the Bulk Edit Task Scheduling field to
                                                               						schedule the Bulk Edit operation for a later date and/or time. |
|---|---|

| Note | In Cisco Business Edition, you delete Cisco Unity Connection user accounts in Cisco Unified CM Administration. (Use the applicable
                                       User Management page to find the user or application user, then delete.) To learn more about deleting Unity Connection accounts in Cisco Unified CM Administration, see the online Help or the “Application
                                       User Deletion” and “End User Setup” chapters of the applicable Cisco Unified Communications Manager Administration Guide.
                                       The guide is available at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Note | If LDAP synchronization is not enabled and if you do not manually synchronize Cisco Unified CM data with the LDAP directory,
                                             the deletion of an LDAP user is never replicated to the Cisco Unified CM database, and the corresponding Unity Connection
                                             user cannot be deleted. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, select Users > Users. |
|---|---|
| Step 2 | On the Search Users page, check the check box next to the user
                                          			 account that you want to delete. Note If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find . | Note | If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find . |
| Note | If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find . |
| Step 3 | Select Show Dependencies to search for any database objects that
                                          			 have dependencies on the user you want to delete. |
| Step 4 | From the dependencies search results, follow links to the
                                          			 affected objects and reassign the dependency to another user. |
| Step 5 | Select Tools > Show Dependency Results. |
| Step 6 | On the Show Dependency Results page, select Display Previous
                                          			 Results. |
| Step 7 | Repeat Step 4 through Step 6 until all dependencies have been
                                          			 reassigned. |
| Step 8 | Select Users > Users. |
| Step 9 | On the Search Users page, check the check box next to the user
                                          			 account that you want to delete. |
| Step 10 | Select Delete Selected . |
| Step 11 | In the dialog box that opens, asking you to confirm the
                                          			 deletion, select OK . Note You can also use BAT to delete multiple users at the same time.
                                                         				  For more information, see the Bulk Administration Tool section. | Note | You can also use BAT to delete multiple users at the same time.
                                                         				  For more information, see the Bulk Administration Tool section. |
| Note | You can also use BAT to delete multiple users at the same time.
                                                         				  For more information, see the Bulk Administration Tool section. |

| Note | If the user does not appear in the search results table, set the
                                                         				  applicable parameters in the search fields at the top of the page, and select Find . |
|---|---|

| Note | You can also use BAT to delete multiple users at the same time.
                                                         				  For more information, see the Bulk Administration Tool section. |
|---|---|

| Note | The information in this chapter is not applicable to Cisco Business Edition. |
|---|---|

| Note | The information in this section is not applicable to Cisco
                                          		  Business Edition. |
|---|---|

| Caution | Before moving users, read the COBRAS help file and the COBRAS
                                          		  Hot Mode for Unity Connection to Unity Connection help file carefully and
                                          		  thoroughly. |
|---|---|

| Note | The information in this section is not applicable to Cisco Business Edition. |
|---|---|

| Step 1 | Download the latest version of COBRAS, and view training videos
                                             			 and Help at http://www.ciscounitytools.com/Applications/General/COBRAS/COBRAS.html . Caution Before migrating users, read the COBRAS help file and the COBRAS
                                                            				  Briefcase Mode help file carefully and thoroughly. | Caution | Before migrating users, read the COBRAS help file and the COBRAS
                                                            				  Briefcase Mode help file carefully and thoroughly. |
|---|---|---|---|
| Caution | Before migrating users, read the COBRAS help file and the COBRAS
                                                            				  Briefcase Mode help file carefully and thoroughly. |
| Step 2 | Back up the source and target locations using the Disaster Recovery System. The source backup is not used to restore data
                                             on the target location; you should take back up of each location so you can revert to the previous state of the location if
                                             necessary. For more information, see the Install, Upgrade, and Maintenance Guide Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html . |
| Step 3 | Use COBRAS Briefcase Mode to export the users to be moved from
                                             			 the source location. See the COBRAS Briefcase Mode help file for instructions. |
| Step 4 | If the source and target locations are connected via any type of
                                             			 networking, delete the users to be moved from the source location. To delete
                                             			 accounts one at a time, see the Deleting User Accounts section. Note If the source and target are connected via any type of
                                                            				  networking, it is critical that you delete the users and verify that the
                                                            				  deletion has completed on all networked locations before importing the users on
                                                            				  the target location. | Note | If the source and target are connected via any type of
                                                            				  networking, it is critical that you delete the users and verify that the
                                                            				  deletion has completed on all networked locations before importing the users on
                                                            				  the target location. |
| Note | If the source and target are connected via any type of
                                                            				  networking, it is critical that you delete the users and verify that the
                                                            				  deletion has completed on all networked locations before importing the users on
                                                            				  the target location. |
| Step 5 | Use COBRAS Briefcase Mode to import users on the target
                                             			 location. See the COBRAS Briefcase Mode help file for instructions. |
| Step 6 | If you did not delete the original user accounts from the source
                                             			 location in Task 4. ,
                                             			 delete them now. To delete accounts one at a time, see the Deleting User Accounts . |

| Caution | Before migrating users, read the COBRAS help file and the COBRAS
                                                            				  Briefcase Mode help file carefully and thoroughly. |
|---|---|

| Note | If the source and target are connected via any type of
                                                            				  networking, it is critical that you delete the users and verify that the
                                                            				  deletion has completed on all networked locations before importing the users on
                                                            				  the target location. |
|---|---|