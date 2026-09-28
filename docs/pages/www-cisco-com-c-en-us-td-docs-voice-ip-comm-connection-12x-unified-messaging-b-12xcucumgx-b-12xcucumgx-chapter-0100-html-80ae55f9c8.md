---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-unified-messaging-b-12xcucumgx-b-12xcucumgx-chapter-0100-html-80ae55f9c8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/unified_messaging/b_12xcucumgx/b_12xcucumgx_chapter_0100.html
retrieved_at: 2026-08-17T03:45:17.339756+00:00
---

Unified Messaging Guide for Cisco Unity Connection Release 12.x

# Unified Messaging Guide for Cisco Unity Connection Release 12.x

Updated: August 30, 2023

Chapter: Moving and Restoring Exchange Mailboxes

## Chapter: Moving and Restoring Exchange Mailboxes

# Moving and Restoring Exchange Mailboxes

Moving and Restoring Exchange Mailboxes

## Overview

The mailboxes for unified messaging users in Cisco Unity Connection can be moved from one Exchange server to another. You
                           may want to move the mailboxes from one Exchange server to another due to any reason. Consider an instance in which after
                           adding the latest supported version of Exchange server to the existing Exchange environment of your organization, you want
                           to move the user mailboxes to the latest version.

To move the user mailboxes from one version of Exchange to another, you need to update some specific settings for the Unity
                           Connection users. This enables Unity Connection to automatically detect the migration of user mailboxes automatically. If
                           Unity Connection fails to detect the migration of mailboxes, you need to manually replace the existing mailboxes of unified
                           messaging users with new mailboxes on the migrated Exchange server.

## Updating User
                        	 Settings After Moving Exchange Mailboxes

As covered in the “ Configuring
                              		  Unified Messaging ” chapter, the administrators can create one or more
                           		unified messaging services with Exchange. Following are the two settings that
                           		identify how Unity Connection manually updates user settings after the Exchange
                           		mailboxes are moved:

Unity Connection searches for Exchange servers: If you select to
                                 			 allow Unity Connection to search for Exchange servers, Unity Connection
                                 			 automatically detects when you move mailboxes to another version of Exchange
                                 			 and automatically updates Unity Connection user settings.

Unity Connection selects a specific Exchange server: If you
                                 			 select a specific Exchange server, either Unity Connection detects mailbox move
                                 			 from one Exchange server to another or it fails to detect. The administrator
                                 			 needs to manually replace the old unified messaging account with a new unified
                                 			 messaging account to access the specific Exchange server.

If Unity
                                                   					 Connection is not able to automatically detect mailbox moves, see the Replacing
                                                      						Unity Connection Unified Messaging Accounts After Moving Exchange Mailboxes,
                                                      						page 5-2 section.

If Unity Connection automatically detects mailbox moves, see the Moving
                                                      						Exchange Mailboxes to a New Exchange Server, page 5-2 section.

Table 5-1 lists the
                           		scenarios when Unity Connection can and cannot automatically detect mailbox
                           		moves between Exchange servers.

If you select a specific

Unity Connection can automatically detect mailbox moves between
                                       				  the following Exchange versions

2010 and 2010

2010 and 2013

2013 and 2013

Exchange 2010 server

Yes

No

No

Exchange 2013 server

Yes

Yes

Yes

## Moving Exchange Mailboxes to a New Exchange Server

In an organization, you can add an Exchange server by moving the Exchange mailboxes to the new server. If the Exchange mailboxes
                           are associated with Unity Connection users who are configured for single inbox, you must grant the permissions that Unity
                           Connection requires before you move the mailboxes. Otherwise, Unity Connection users cannot access their voicemails from the
                           new location. This is true regardless of whether you allow Unity Connection to search for Exchange servers or you configure
                           Unity Connection to communicate with a specific Exchange server.

For information on granting the necessary permissions depending on the Exchange server, see the Configuring Unified Messaging in Active Directory, page 2-5 section.

To access a new Exchange server, either you need to create a new unified messaging services account or grant necessary permissions
                                       to the existing unified messaging services account.

## Replacing Unity
                        	 Connection Unified Messaging Accounts After Moving Exchange Mailboxes

Following are the steps the administrators must do when Unity
                              		  Connection cannot detect Exchange mailbox moves and cannot automatically update
                              		  the location of the Exchange mailbox for a Unity Connection user:

Manually
                                    				create a new unified messaging account that accesses the new mailbox location.

Delete the
                                    				unified messaging account that accessed the old mailbox location.

Caution

Do the following procedure to replace Unity Connection unified
                              		  messaging accounts after moving exchange mailboxes:

Step 1

Review
                                       			 the Updating
                                          				User Settings After Moving Exchange Mailboxes, page 5-1 to determine
                                       			 whether Unity Connection can automatically detect mailbox moves for your
                                       			 Exchange configuration.

Step 2

Do either of the following steps:

If Unity Connection can detect mailbox
                                                					 moves, skip the rest of this procedure.

If Unity Connection cannot detect
                                                					 mailbox moves, continue with Step 3 .

Step 3

If you moved the Exchange mailbox to an Exchange server for
                                       			 which there is currently no unified messaging service in Unity Connection,
                                       			 create the service. For more information, see the Creating
                                          				a Unified Messaging Service to Access Mail Server, page 2-27 section.

Step 4

Create a new unified messaging account for the user and select a
                                       			 unified messaging service that accesses the new Exchange server to which the
                                       			 mailbox was moved. For more information, see the Unified
                                          				Messaging Account for Users, page 2-30 section.

Step 5

Delete the unified messaging account that accessed the old
                                       			 Exchange server from where the mailbox was moved:

In Cisco Unity Connection
                                             				  Administration, expand Users and select Users .

On the Search Users page, select the
                                             				  alias of a user.

On the Edit User Basics page, from the Edit menu, select Unified Messaging Accounts .

On the Unified Messaging Accounts page,
                                             				  check the check box to the left of the unified messaging account that you want
                                             				  to delete. Select Delete Selected .

Step 6

Repeat Step 3 through Step 5 for the other users
                                       			 whose Exchange mailboxes you moved.

## Restoring Exchange Mailboxes

Restoring exchange mailboxes in Unity Connection requires you to take the backup of the current unified messaging accounts
                           of the users. The following section shows how to restore unified messaging capabilities for individual users or multiple users.
                           The most important aspect while restoring is to disable single inbox to stop the synchronization between Exchange and Unity
                           Connection.

### Task List for Restoring Microsoft Exchange Mailboxes

Disable single inbox for selected users or for a unified messaging service. See the Disabling Single Inbox for Unity Connection, page 5-5 section.

Restore Exchange mailboxes. For more information, see the applicable Microsoft documentation.

Re-enable single inbox selecting the applicable option:

If you disabled single inbox for individual users using Unity Connection\\ Administration, repeat the Disable Single Inbox for Individual Users, page 5-6 section, but check the Synchronize Unity Connection and Exchange Mailboxes (Single Inbox) check box.

If you disabled single inbox for a unified messaging service, repeat the “Disable Single Inbox for All Users” procedure on page 5-6 , but check either the Synchronize Connection and Exchange Mailboxes (Single Inbox) check box or the Enabled check box, as applicable.

If you disabled single inbox for individual users using the Bulk Administration Tool, repeat the “Disable Single Inbox for a Large Numbers of Selected Users Using the Bulk Administration Tool” procedure on page 5-6 , but change the value of enableMbxSynch to 1 .

## Disabling Single Inbox Before Restoring Exchange Mailboxes

You must disable single inbox for the Unity Connection users whose Exchange mailboxes and other unified messaging service
                           capabilities are being restored. If single inbox is not disabled, Unity Connection is unable to synchronize voicemails received
                           from the time the backup initiates till the restore completes.

### Behavior of Synchronization Cache when Single Inbox is Disabled

Unity Connection maintains a synchronization cache that tracks the voicemails already forwarded to Exchange. When you disable
                              single inbox, the synchronization cache is automatically cleared.

Do the following steps to understand the behaviour of synchronization cache when single inbox is disabled:

You take the backup of the Exchange server.

A new voicemail arrives.

Unity Connection synchronizes the voicemail with the Exchange mailbox associated with the Unity Connection user.

Unity Connection updates the synchronization cache for the user to indicate that the message has been synchronized with Exchange.

A hard disk in the Exchange server fails.

You disable single inbox for the Unity Connection user whose Exchange mailbox was on the failed hard disk.

Unity Connection clears the synchronization cache for that user.

You replace the hard disk and restore Exchange from the backup that you made in step 1.

You re-enable single inbox for the user.

Unity Connection performs a periodic comparison of the synchronization cache with the voicemails currently in Exchange.

Because the cache is empty, Unity Connection concludes that voicemails that are in the Unity Connection mailbox but not in
                                    the Exchange mailbox have not yet been synchronized with Exchange.

Unity Connection resynchronizes the Unity Connection mailbox with the Exchange mailbox and rebuilds the synchronization cache.

### Behavior of Synchronization Cache when Single Inbox is Enabled

If you restore Exchange mailboxes without disabling single inbox for the Unity Connection users, Unity Connection deletes
                              all voicemails received after the backup from which you are restoring. Do the following steps to understand the behaviour
                              of synchronization cache with single inbox:

You can take the backup of the Exchange server.

A new voicemail arrives.

Unity Connection synchronizes the voicemail with the Exchange mailbox associated with the Unity Connection user.

Unity Connection updates the synchronization cache for the user to indicate that the message has been synchronized with Exchange.

A hard disk in the Exchange server fails.

You replace the hard disk and restore Exchange from the backup that you made in 1.

Unity Connection performs a periodic comparison of the synchronization cache with the voicemails currently in Exchange. The
                                    voicemail that arrived in 2. is not in the Exchange mailbox for the associated Unity Connection user.

Unity Connection concludes that the voicemail has already been synchronized with Exchange and does not resynchronize the message
                                    into the Exchange mailbox.

### Disabling Single Inbox for Unity Connection

The first step in restoring Exchange mailboxes is to disable single inbox. Depending on the number of Exchange servers that
                              you are restoring or the effect of restore on Unity Connection functionality, you can disable single inbox in either of the
                              following ways:

#### Restoring Exchange Mailboxes for a Small Number of Users

If you are restoring Exchange mailboxes for a small number of users, you can disable single inbox on individual user accounts
                                 using Unity Connection\\ Administration. See the Disable Single Inbox for Individual Users, page 5-6 .

#### Restoring Exchange
                              	 Mailboxes for All the Unified Messaging Users or When Unity Connection
                              	 Functionality is Not a Concern

You can disable the single inbox functionality of all unified
                                 		messaging users in either of the following conditions:

While you are restoring mailboxes for all of the users
                                       			 associated with a unified messaging service.

While you are restoring mailboxes for selected users associated
                                       			 with a unified messaging service during non-business hours when interrupting
                                       			 single inbox functionality has less impact on users.

There are two ways to disable single inbox for a unified
                                 		messaging service:

Disable only single inbox for a unified messaging
                                             				  service : If you disable only single inbox, the Unity Connection
                                       			 conversation continues to play the options for the other unified messaging
                                       			 features. If a user selects one of these features while Exchange is
                                       			 unavailable, the Unity Connection conversation announces that access to
                                       			 messages is unavailable at this time.

Disable the entire unified messaging service : If the unified messaging service has other unified messaging features enabled,
                                       			 such as text-to-speech or contact integration, and you disable the service,
                                       			 Unity Connection conversation stops playing the options for those features
                                       			 until the unified messaging service is re-enabled, which could be confusing for
                                       			 users.

For more information, see the “Disable
                                    		  Single Inbox for All Users” procedure on page 5-6 .

#### Restoring Exchange Mailboxes for Some Users Associated with a Unified Messaging Service When Unity Connection Functionality
                              is a Concern

When you are restoring Exchange mailboxes for a large number of users associated with a unified messaging service, you can
                                 use the Bulk Administration Tool to disable single inbox for individual users, if both the following conditions are true:

The unified messaging service also includes users whose mailboxes you are not restoring.

You are restoring the mailboxes during business hours, when you want to minimize the impact on users whose mailboxes you are
                                       not restoring.

#### Disable Single
                              	 Inbox for Individual Users

Step 1

In Cisco Unity Connection Administration, expand Users and select Users . On the Search Users page, select the alias of
                                             			 the user account that you want to modify.

Step 2

On the Edit Users page, in the Edit menu, select Unified Messaging Accounts . Select the unified
                                             			 messaging account that enables single inbox for the user.

Step 3

Uncheck the Synchronize Unity Connection and Exchange Mailboxes (Single
                                                				Inbox) check box.

Step 4

Select Save .

Step 5

Repeat Step 1 through Step 4 for the
                                             			 remaining users.

#### Disable Single
                              	 Inbox for All Users

To disable the entire unified messaging service, uncheck the Enabled check box.

Step 1

In Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services .

Step 2

On the Search Unified Messaging Services page, select the alias
                                             			 of the unified messaging service that you want to modify.

Step 3

To disable single inbox for the users associated with this
                                             			 unified messaging service, uncheck the Synchronize Connection and Exchange Mailboxes (Single
                                                				Inbox) check box.

Step 4

Select Save .

Step 5

Repeat Step 1 through Step 4 for other
                                             			 unified messaging services for which you want to disable single inbox.

#### Disable Single
                              	 Inbox for a Large Numbers of Selected Users Using the Bulk Administration
                              	 Tool

Step 1

In Cisco Unity Connection Administration, expand Tools and select Bulk Administration Tool .

Step 2

Under Select Operation , select Export .

Step 3

Under Select Object Type , select Unified Messaging Accounts .

Step 4

Specify a filename for the CSV file to which unified messaging
                                             			 accounts are exported.

Step 5

Select Submit .

Step 6

Follow the onscreen prompts to save the CSV file.

Step 7

Open the CSV file.

Step 8

For the users for whom you want to disable the single inbox
                                             			 feature, change the value of enableMbxSynch to 0 .

Step 9

In Cisco Unity Connection Administration, select Tools > Bulk Administration
                                                   				  Tool .

Step 10

Under Select Operation, select Update .

Step 11

Under Select Object Type, select Unified Messaging Accounts .

Step 12

Specify the name of the CSV file that you updated in Step 8 .

Step 13

Select Submit .

| Note | If Unity
                                                   					 Connection is not able to automatically detect mailbox moves, see the Replacing
                                                      						Unity Connection Unified Messaging Accounts After Moving Exchange Mailboxes,
                                                      						page 5-2 section. If Unity Connection automatically detects mailbox moves, see the Moving
                                                      						Exchange Mailboxes to a New Exchange Server, page 5-2 section. |
|---|---|

| If you select a specific | Unity Connection can automatically detect mailbox moves between
                                       				  the following Exchange versions |
|---|---|
| 2010 and 2010 | 2010 and 2013 | 2013 and 2013 |
| Exchange 2010 server | Yes | No | No |
| Exchange 2013 server | Yes | Yes | Yes |

| Note | To access a new Exchange server, either you need to create a new unified messaging services account or grant necessary permissions
                                       to the existing unified messaging services account. |
|---|---|

| Caution | Unity Connection does not synchronize voicemails with the
                                             				corresponding Exchange mailboxes during the time you move the Exchange
                                             				mailboxes and update Unity Connection settings for the affected users. |
|---|---|

| Step 1 | Review
                                       			 the Updating
                                          				User Settings After Moving Exchange Mailboxes, page 5-1 to determine
                                       			 whether Unity Connection can automatically detect mailbox moves for your
                                       			 Exchange configuration. |
|---|---|
| Step 2 | Do either of the following steps: If Unity Connection can detect mailbox
                                                					 moves, skip the rest of this procedure. If Unity Connection cannot detect
                                                					 mailbox moves, continue with Step 3 . |
| Step 3 | If you moved the Exchange mailbox to an Exchange server for
                                       			 which there is currently no unified messaging service in Unity Connection,
                                       			 create the service. For more information, see the Creating
                                          				a Unified Messaging Service to Access Mail Server, page 2-27 section. |
| Step 4 | Create a new unified messaging account for the user and select a
                                       			 unified messaging service that accesses the new Exchange server to which the
                                       			 mailbox was moved. For more information, see the Unified
                                          				Messaging Account for Users, page 2-30 section. |
| Step 5 | Delete the unified messaging account that accessed the old
                                       			 Exchange server from where the mailbox was moved: In Cisco Unity Connection
                                             				  Administration, expand Users and select Users . On the Search Users page, select the
                                             				  alias of a user. On the Edit User Basics page, from the Edit menu, select Unified Messaging Accounts . On the Unified Messaging Accounts page,
                                             				  check the check box to the left of the unified messaging account that you want
                                             				  to delete. Select Delete Selected . |
| Step 6 | Repeat Step 3 through Step 5 for the other users
                                       			 whose Exchange mailboxes you moved. |

| Step 1 | In Cisco Unity Connection Administration, expand Users and select Users . On the Search Users page, select the alias of
                                             			 the user account that you want to modify. |
|---|---|
| Step 2 | On the Edit Users page, in the Edit menu, select Unified Messaging Accounts . Select the unified
                                             			 messaging account that enables single inbox for the user. |
| Step 3 | Uncheck the Synchronize Unity Connection and Exchange Mailboxes (Single
                                                				Inbox) check box. |
| Step 4 | Select Save . |
| Step 5 | Repeat Step 1 through Step 4 for the
                                             			 remaining users. |

| Step 1 | In Unity Connection Administration, expand Unified Messaging and select Unified Messaging Services . |
|---|---|
| Step 2 | On the Search Unified Messaging Services page, select the alias
                                             			 of the unified messaging service that you want to modify. |
| Step 3 | To disable single inbox for the users associated with this
                                             			 unified messaging service, uncheck the Synchronize Connection and Exchange Mailboxes (Single
                                                				Inbox) check box. To disable the entire unified messaging service, uncheck the Enabled check box. |
| Step 4 | Select Save . |
| Step 5 | Repeat Step 1 through Step 4 for other
                                             			 unified messaging services for which you want to disable single inbox. |

| Step 1 | In Cisco Unity Connection Administration, expand Tools and select Bulk Administration Tool . |
|---|---|
| Step 2 | Under Select Operation , select Export . |
| Step 3 | Under Select Object Type , select Unified Messaging Accounts . |
| Step 4 | Specify a filename for the CSV file to which unified messaging
                                             			 accounts are exported. |
| Step 5 | Select Submit . |
| Step 6 | Follow the onscreen prompts to save the CSV file. |
| Step 7 | Open the CSV file. |
| Step 8 | For the users for whom you want to disable the single inbox
                                             			 feature, change the value of enableMbxSynch to 0 . |
| Step 9 | In Cisco Unity Connection Administration, select Tools > Bulk Administration
                                                   				  Tool . |
| Step 10 | Under Select Operation, select Update . |
| Step 11 | Under Select Object Type, select Unified Messaging Accounts . |
| Step 12 | Specify the name of the CSV file that you updated in Step 8 . |
| Step 13 | Select Submit . |