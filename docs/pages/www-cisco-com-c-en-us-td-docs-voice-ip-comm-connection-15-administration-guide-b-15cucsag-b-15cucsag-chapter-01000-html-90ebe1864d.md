---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-administration-guide-b-15cucsag-b-15cucsag-chapter-01000-html-90ebe1864d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag//b_15cucsag_chapter_01000.html
retrieved_at: 2026-08-21T00:36:36.680006+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 12, 2025

Chapter: Message Storage

## Chapter: Message Storage

# Message Storage

## Message Storage

### Overview

Cisco Unity Connection uses separate databases to store the system configuration and the information in voicemails.

### About Mailbox
                           	 Stores

Consider the following points to understand the importance of
                              		mailbox stores in Unity Connection:

During installation, Unity Connection automatically creates:

A directory database to store system configuration information,
                                          				  such as user data and templates.

A mailbox store database to store information, such as the
                                          				  sender of each message and the location of the .wav file associated with a
                                          				  particular voice message.

An operating system directory to store voice message .wav files.

A Unity Connection server or cluster supports up to 20,000
                                    			 users. You need to create a separate mailbox store for every 5000 users.
                                    			 Creating additional mailbox stores allow you to backup selected mailboxes and
                                    			 ensure that backup gets completed during non-business hours.

You can modify the default 15 GB size of the Unity Connection mailbox stores depending on your requirements. The maximum mailbox
                                    size recommended by Unity Connection is 30 GB.

An administrator with the required permissions can create up to
                                    			 four additional mailbox stores. Each additional mailbox store includes a
                                    			 separate mailbox store database and a separate operating system directory.

The directory information of all the users in a Unity Connection
                                    			 server or cluster remain in one directory database created during Unity
                                    			 Connection installation.

After you create a new mailbox store, you can either move the
                                    			 existing mailboxes into the new mailbox store or create new mailboxes in the
                                    			 new mailbox store. For more information, see the Moving Mailboxes between Mailbox Stores section.

In case of a Unity Connection cluster, all the mailbox stores
                                    			 are replicated to both publisher and subscriber.

#### User Templates
                              	 Settings

The user template selected at the time of creating a new user
                                 		account specifies some settings that are used as a default value for the user
                                 		account. The mailboxes of the user accounts based on the default user template
                                 		are created in the default mailbox store. If you create new mailbox stores, you
                                 		can change the mailbox settings in the default user templates or in any new
                                 		user templates that you create.

If a mailbox store is applied to one or more user templates, you
                                             		  cannot delete that mailbox store until the user template setting is changed or
                                             		  the user template is deleted.

For more information changing the mailbox settings in a user
                                 		template, see the Configuring User Templates .

#### Maximum Size Supported for a Mailbox Store

You must specify the maximum amount of disk space that the voice messages for a mailbox store can occupy at the time of creating
                                 a new mailbox store. The maximum size of mailbox store is not an absolute maximum but specifies a limit. On exceeding the
                                 limit specified for a mailbox, warnings or errors are logged into Unity Connection.

Consider the following information related to the maximum size supported for a mailbox store:

The size of a mailbox store is still less than the maximum specified value if:

Unity Connection saves new messages in the mailbox store.

You can create new mailboxes in the mailbox store.

You can move other mailboxes into the mailbox store.

When the size of the mailbox store reaches 90 percent of the specified maximum size, a warning is logged in the system log.

When the size of the store reaches 100 percent of the specified maximum size, an error is logged in the system log. In addition,
                                       in Cisco Unity Connection Administration, an error appears in the Status bar on the Edit Mailbox Store page.

If you want to maintain the mailbox store below 100 percent of the specified maximum limit, do any of the following:

Increase the maximum size of the mailbox store, if an additional space is available on the hard disk.

Create another mailbox store and move some mailboxes into the new mailbox store.

Revise the mailbox size quotas and message aging policy to reduce the individual mailbox size and the size of mailbox store.
                                             You can also delete the voice messages to reduce the size of the mailboxes that reduces the total size of the mailbox store.
                                             However, before deleting the mailboxes, make sure to backup the mailbox stores to preserve any important information.

When users delete messages, the deleted messages are not removed from the mailbox store until the next time the Clean Deleted
                                                         Messages task runs. The task runs every 30 minutes and the schedule for the task cannot be edited.

##### Changing the
                                 	 Maximum Size Supported for a Mailbox Store

Step 1

In Cisco Unity Connection Administration, expand Message Storage
                                                			 and select Mailbox Stores.

Step 2

On the Search Mailbox Store page, select the applicable mailbox
                                                			 store.

Step 3

On the Edit Mailbox Store page, change the value in the Maximum
                                                			 Size Before Warning field. (For more information on each field, see Help>
                                                			 This Page).

Do not change the value of this field if the mailbox store is
                                                               				  already at the maximum size that can be backed up during non-business hours.

Step 4

Select Save.

#### Backup with
                              	 Multiple Mailbox Stores

The duration of backup depends on the size of a mailbox store. The Disaster Recovery System takes the backup of an entire
                                 mailbox store and the corresponding database during a single backup session. The default size of a mailbox store is limited
                                 to 15 GB so that the backup can be completed during non business hours. For more information on how to backup the multiple
                                 mailbox stores, see the “Backing Up and Restoring Cisco Unity Connection Components” chapter of the Install, Upgrade, and Maintenance Guide, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html

### Configuring Mailbox Stores

Consider the following points when creating,
                                 		  editing, or deleting the mailbox stores:

You can create or edit the settings of one
                                       				mailbox store at a time.

You cannot delete a mailbox store if:

The mailbox store still contains one or
                                             					 more mailboxes.

The mailbox store is still referenced by
                                             					 one or more user templates.

The administrator is trying to delete
                                             					 the default mailbox store (UnityMbxDb1).

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Message Storage and select Mailbox Stores.

The Search Mailbox Store page displays the
                                             				currently configured mailbox stores.

A user account without the System
                                                         				  Administrator role cannot create a new mailbox store.

Step 2

Configure one or mailbox stores (For more
                                          			 information on each field, see Help> This Page):

To add a new mailbox store:

On the Search Mailbox Store page, select Add
                                       				New.

On the New Mailbox Store page, enter the
                                       				values of the required fields and select Save.

The new mailbox store appears on the Search
                                       				Mailbox Stores page. The value in the Access Enabled column is Yes and the
                                       				value of the Status column is OK.

To edit an existing mailbox store:

On the Search Mailbox Store page, select the
                                       				mailbox store that you want to edit.

On the Edit Mailbox Store page, enter the
                                       				values of the required fields and select Save.

To delete one or more mailbox stores:

On the Search Mailbox Store page, check the
                                       				check boxes to select the users with mailboxes that you want to delete.

Select Delete Selected and OK to confirm.

### Moving Mailboxes between Mailbox Stores

When moving mailboxes from one mailbox store to
                                 		  another, note the following:

The MWI status is retained after a mailbox
                                       				is moved from one mailbox store to another.

(Unity Connection cluster only) Sign in to
                                       				the server with Primary status to move the mailboxes.

Moving the mailboxes from one mailbox store
                                       				to another fails, if:

The user do not have sufficient
                                             					 permissions in Cisco Unity Connection Administration and is not authorized to
                                             					 move a mailbox.

The source or the target mailbox store
                                             					 is disabled.

The user with mailbox that you are
                                             					 moving is a system user. System mailboxes cannot be moved out of the default
                                             					 mailbox store(UnityMbxDb1).

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Message Storage and select Mailbox Stores Membership.

Step 2

On the Search Mailbox Stores Membership
                                          			 page, in the Choose Membership Type list, select User Mailbox.

Step 3

In the User Mailbox Search Results section,
                                          			 specify the mailbox store from which you want to move the mailboxes.

Step 4

Select the mailbox store to which you want
                                          			 to move the mailboxes and check the applicable check boxes for the users with
                                          			 mailboxes that you want to move.

Step 5

Select Move Selected Mailboxes.

### Disabling and Re-Enabling a Mailbox Store

Each mailbox store is automatically disabled
                                 		  when you take the backup of that mailbox store using Disaster Recovery System.
                                 		  When a mailbox store is disabled:

You cannot create a new mailbox in the
                                       				store.

You cannot move existing mailboxes into or
                                       				out of the store.

New messages for users with mailboxes that
                                       				are in the disabled store are queued for delivery until the store is
                                       				re-enabled.

Cisco Unity Connection Administration provides
                                 		  an option to manually disable a mailbox store but you should not disable a
                                 		  mailbox store that is in use.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Message Storage and select Mailbox Stores.

Step 2

On the Search Mailbox Stores page, select
                                          			 the mailbox store that you want to disable.

Step 3

To disable a mailbox store:

On the Edit Mailbox Store page, uncheck the
                                             				Mounted check box and select Save.

Step 4

To re-enable a mailbox store:

On the Edit Mailbox Store page, check the
                                             				Mounted check box and select Save.

### Controlling the Size of Mailboxes

You can specify mailbox size quotas and change the message aging policy in Cisco Unity Connection Administration to control
                              the size of the user voice mailboxes.

#### Mailbox Size
                              	 Quotas

To help control the size of the user voice mailboxes, Unity
                                    		  Connection allows you to specify quotas or limits on the maximum size of voice
                                    		  mailbox. You can configure quotas so that Unity Connection:

Issues a warning when a mailbox reaches a specified size.

Prevents a user from sending messages when the mailbox reaches
                                          				the limit.

Prevents a user from sending or receiving messages when the
                                          				mailbox reaches the limit.

By default, Unity Connection is configured with the system-wide
                                    		  mailbox size quotas listed in below Table . However, to handle the varying
                                    		  needs of users in your organization, you can override the system-wide quotas
                                    		  for individual mailboxes and for user templates.

Mailbox Size Quotas Defined in Unity Connection

Quota Level

Recording Time Before Quota is Reached/ Disk Space Used 1

G.711 Mu-Law

G.711 A-Law

G.726

PCM 8 kHz

PCM 16
                                                   						kHz 2

G.729a

GSM 6.10

Warning

12 MB

The user is warned that the mailbox is reaching the maximum size
                                                   						allowed.

18 min./ 11 KB/sec

18 min./ 11 KB/sec

37 min./ 5.53 KB/sec

9 min./ 22 KB/sec

4.5
                                                   						min./ 44 KB/sec

122 min./ 1.67 KB/sec

91 min./ 2.25 KB/sec

Send

13 MB

The user is prevented from sending any more voice messages.

20 min./ 11 KB/sec

20 min./ 11 KB/sec

40 min./ 5.53 KB/sec

10 min./ 22 KB/sec

5
                                                   						min./ 44 KB/sec

132 min./ 1.67 KB/sec

98 min./ 2.25 KB/sec

Send/ Receive

14 MB

The user is prevented from sending or receiving any more voice
                                                   						messages.

21 min./ 11 KB/sec

21 min./ 11 KB/sec

43 min./ 5.53 KB/sec

10 min./ 22 KB/sec

5
                                                   						min./ 44 KB/sec

143 min./ 1.67 KB/sec

106 min./ 2.25 KB/sec

Caution

Quotas alone can control the size of mailboxes for the users who
                                                			 regularly check Unity Connection voice messages using the telephone user
                                                			 interface. Web Inbox and Cisco ViewMail for Microsoft Outlook do not notify
                                                			 users that the mailbox has reached its limit. If users check messages using Web
                                                			 Inbox or Cisco ViewMail for Microsoft Outlook, you need to configure message
                                                			 aging so that the old messages are automatically deleted.

##### Changing the
                                 	 Default System-wide Mailbox Quotas in Unity Connection

Step 1

In Cisco Unity Connection Administration, expand Message Storage > > > Mailbox Quotas > and select Mailbox Quotas.

Step 2

On the Edit System-wide Mailbox Quotas page, enter the values of
                                                			 the required settings. (For more information on each field, see Help> This
                                                			 Page).

Step 3

Select Save.

For information to override system-wide mailbox quota settings
                                                               				  for Unity Connection users and user templates, see the “User Attributes” and
                                                               				  “Users” chapters.

#### Mailbox Quota Alert

Unity Connection allows you to specify the maximum quota for the voice mailbox of every user. In Unity Connection 10.0(1)
                                 and later releases, when the mailbox size of a user starts reaching its specified threshold limit, the user receives a quota
                                 notification message.

A quota notification message is an email that is sent automatically by Unity Connection to the corporate email address of
                                 the mailbox of the user when its exceeds the threshold limit. You can use Cisco Unity Connection Administration to view the
                                 default quota notification message or to create, view, and edit the quota notification messages. The quota notification message
                                 is sent by the Quota Notification Mail task to the configured corporate addresses of the users whose mailbox has reached the
                                 size specified for warning quota.

#### Configuring the Quota Notification Settings

Step 1

In Cisco Unity Connection Administration,
                                             			 expand Tools and select Task Management.

Step 2

On the Task Definitions page, select Quota
                                             			 Notification Mail.

Step 3

On the Task Definition Basics (Quota
                                             			 Notification Mail) page, select Edit > Task Schedules.

Step 4

On the Task Schedule page, enter the values
                                             			 of the required fields and select Save. (For more information on each field,
                                             			 see Help> This Page).

The quota notification messages are not
                                                            				  sent to the users that do not have corporate email addresses configured.

You can also execute the following command
                                                				through CLI to run the Quota Notification Mail task:

```
run cuc sysagent task Umss.QuotaNotificationMailTask
```

Umss.QuotaNotificationMailTask is the name
                                                				of the Quota Notification Mail task.

For more information on the above command,
                                                				see the “run cuc sysagent task” section of the “Run commands” chapter of
                                                				Command Line Interface Reference Guide for Cisco Unified Communications
                                                				Solutions, Release 10.0(1), available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/10_0_1/CUCM_BK_CBEED39F_00_cucm-cli-reference-guide-100/CUCM_BK_CBEED39F_00_cucm-cli-reference-guide-100_chapter_0101.html#CUCM_CL_R812A687_00 .

#### Customizing the
                              	 Subject Line or Body Text of Mailbox Quota Alert Text

Step 1

In Cisco Unity Connection Administration, expand Message
                                             			 Storage> Mailbox Quotas and then select Quota Alert Text.

Step 2

On the Edit Mailbox Quota Alert Text page, in the Language list,
                                             			 enter the values of the required fields. (For more information on each field,
                                             			 see Help> This Page).

Step 3

Select Save.

Step 4

Repeat Step2 through Step3 for each language installed on the
                                             			 system.

#### Message Aging
                              	 Policies

In a single inbox configuration, messages that users delete
                                 		using Outlook are only moved to the Deleted Items folder in Outlook but are not
                                 		permanently deleted. To keep a check on the mailbox size for users, you need to
                                 		configure a message aging policy for the Unity Connection users.

Message aging policies
                                 		ensure that the databases storing the voice messages are not filled up. The
                                 		message aging policies are managed through Cisco Unity Connection
                                 		Administration> Message Storage> Message Aging> Aging Policies.

Each policy allows you to specify message aging rules that
                                 		automatically perform the following operations mentioned on the Message Aging
                                 		Policy page:

Move New Messages to the Saved Messages Folder after the
                                       			 specified number of days.

Move Saved Messages to the Deleted Items Folder after the
                                       			 specified number of days.

Permanently Delete Messages in the Deleted Items Folder after
                                       			 the specified number of days. This is the only rule enabled in the Default
                                       			 System Policy message aging policy, this is the only rule that is enabled.

Permanently Delete Secure Touched Messages That are Older Than a
                                       			 specified number of days. The secure messages are considered as touched
                                       			 messages if we mark the messages as new, read or deleted messages.

Permanently Delete All Secure Messages That are Older Than a
                                       			 specified number of days. This policy is regardless of whether users have
                                       			 listened to or touched the messages in any way.

For each policy, you can enable or disable each message aging
                                 		rule and can specify a different number of days for each rule. For each message
                                 		aging rule, you can also specify whether Unity Connection sends an email alert
                                 		to the users prior to aging the message.

Depending on the system requirement of a company, Unity
                                 		Connection may need only one or additional message aging rules. If you are
                                 		using only one set of message aging rules, you can change the specifications
                                 		for the default message aging policy and apply it to all users and user
                                 		templates. If you need to allow some users to retain messages longer than other
                                 		users or send messaging alerts only to a few users, you can create additional
                                 		policies and assign different policies to user templates and to individual
                                 		users.

You can also enable or disable an entire message aging policy.
                                 		Unity Connection includes a default policy, Do Not Age Messages, that is
                                 		disabled and for which all of the rules are disabled.

Some of the message aging rules are based on when a message was
                                 		last modified. To edit a message, you must do one of the following:

In the Web Inbox mark the message as new, mark the message as deleted, or change
                                       			 the message subject, and select Save.

From the phone interface, select the options to mark the message
                                       			 as new, save the message again, delete the message, or restore a deleted
                                       			 message as saved.

The schedule for message aging is controlled by the message
                                                   				aging task that can be managed from the Task Management page in Cisco Unity
                                                   				Connection Administration.

##### Configuring a
                                 	 Message Aging Policy in Unity Connection

Step 1

In Cisco Unity Connection Administration, expand Message Storage > Message Aging > and select Aging Policies .

Step 2

Configure message aging policies, do the following steps (For
                                                			 more information on each field, see Help> This Page):

To add a new message aging policy:

On the Search Message Aging Policy page, select Add New .

Enter the display name of the policy and select Save.

On the Message Aging Policy page, enter the values of the
                                             				required fields and check the Enabled check box. Select Save to apply the
                                             				changes in the policy.

To edit an existing message aging policy:

On the Search Message Aging Policy page, select the policy that
                                             				you want to edit.

On the Message Aging Policy page, change the values of the
                                             				required fields and select Save.

Caution

Do not change the settings of the Do Not Age Messages policy.

To delete a message aging policy:

On the Search Message Aging Policy page, check the check boxes
                                             				for the policies you want to delete.

Select Delete Selected and OK to confirm.

You should not delete the Default System Policy and the Do Not
                                                         				  Age Messages policy. If you do not want to age messages, disable the Default
                                                         				  System Policy instead of deleting it.

#### Message Aging
                              	 Alerts

For each message aging rule,
                                 		you can specify whether Unity Connection sends email alerts to users prior to
                                 		taking the aging action associated with the rule. This gives the users time to
                                 		review and act on the applicable messages. You specify the number of days
                                 		between the time that Unity Connection sends the alert and the time that the
                                 		message aging action takes place.

Alerts cannot be sent to users unless the Corporate Email
                                 		Address field for each user on the Users > Users > Edit User Basics page
                                 		contains a valid email address. Unity Connection must also be configured to
                                 		relay messages through an SMTP smart host.

You can customize the text in the email alerts or you can use
                                 		the default text. The default subject line and body text are different for the
                                 		alerts related to each aging rule and they can be customized separately.

As all the message aging policies use the same five rules, if
                                             		  you customize the alert text for a rule, the text is the same for any policy
                                             		  that uses that rule. (For example, if you customize the email subject line and
                                             		  body text for the Move Saved Messages to the Deleted Items Folder rule, that
                                             		  text is used for all alerts that are sent to users who are assigned to any
                                             		  message aging policy for which that rule is enabled with alerts.)

Message aging alerts can be customized for multiple languages.To
                                 		enable Unity Connection to send message aging alert emails to users, you must
                                 		configure the Unity Connection server to relay messages through an SMTP smart
                                 		host. For more information on SMTP smart host, see the Messaging chapter.

##### Customizing the Message Aging Alert Text in Unity Connection

Step 1

In Cisco Unity Connection Administration,
                                                			 expand Message Storage > Message Aging and select Aging Alert Text .

Step 2

On the Edit Message Aging Alert Text page,
                                                			 in the Language list, select the applicable language.

Step 3

Enter the values of the required fields.
                                                			 (For more information on each field, see Help> This Page).

Step 4

Select Save.

Step 5

Repeat all the above steps for each language
                                                			 installed on the system.

#### Message Recording
                              	 Expiration

The Message Recording Expiration feature
                                 		allows you to specify an expiration date after which the voice message stored
                                 		in Unity Connection database is not accessible, regardless of whether the
                                 		message has been forwarded to another Unity Connection recipient. Message
                                 		recording expiration is a system-wide setting and cannot be applied only to a
                                 		subset of users. At expiration, message recordings are automatically replaced
                                 		with a decoy recording that says, “The message has expired.”

You can specify the Message Recording Expiration policy for video messages also. This feature allows you to specify the expiration
                                 days for video messages, after which the video part of a video message get expired and only audio part is retained as a voice
                                 message.

Typically, message aging rules are sufficient for enforcing
                                 		message-retention policies. However, when a message is forwarded, it is
                                 		considered as a new message and its age is reset. If you are concerned that
                                 		users may forward messages in an attempt to circumvent the message-retention
                                 		policy, consider enabling the Message Recording Expiration feature. The message
                                 		recording and transcription (if any) expire based on the date when the original
                                 		copy of the message has arrived, regardless of user forwarding.

By default, the Message Recording Expiration feature is not
                                 		enabled.

##### Enabling and
                                 	 Configuring Message Recording Expiration in Unity Connection

Step 1

In Cisco Unity Connection Administration, expand Message Storage> Message Aging and select Message Recording Expiration .

Step 2

On the Edit Message Recording Expiration page, specify the
                                                			 number of message expiry days and check the Enabled check box. (For more
                                                			 information on each field, see Help> This Page ).

Step 3

Specify the number of message expiry days for a video messages in
                                                			 Video Message Recordings Expire in field (For more information on each field,
                                                			 see Help> This Page ).

Step 4

Select Save .

The Message Recording Expiration feature does not apply to
                                                               				  messages that have been forwarded to personal email addresses or to message
                                                               				  recordings that have been saved locally to user workstations.

To prevent users from saving local copies or forwarding voice
                                                   				messages to personal email addresses, consider configuring Unity Connection to
                                                   				mark all messages as secure. Unity Connection applies the Message Recording
                                                   				Expiration feature to messages in the mailboxes of recipients that are homed on
                                                   				the Unity Connection server. For example, if User A homed on Unity Connection
                                                   				server A sends a message to User B homed on Unity Connection server B, the
                                                   				message is subject to message expiration only if the Message Recording
                                                   				Expiration feature is enabled on server B.

| Note | If a mailbox store is applied to one or more user templates, you
                                             		  cannot delete that mailbox store until the user template setting is changed or
                                             		  the user template is deleted. |
|---|---|

| Note | When users delete messages, the deleted messages are not removed from the mailbox store until the next time the Clean Deleted
                                                         Messages task runs. The task runs every 30 minutes and the schedule for the task cannot be edited. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Message Storage
                                                			 and select Mailbox Stores. |
|---|---|
| Step 2 | On the Search Mailbox Store page, select the applicable mailbox
                                                			 store. |
| Step 3 | On the Edit Mailbox Store page, change the value in the Maximum
                                                			 Size Before Warning field. (For more information on each field, see Help>
                                                			 This Page). Note Do not change the value of this field if the mailbox store is
                                                               				  already at the maximum size that can be backed up during non-business hours. | Note | Do not change the value of this field if the mailbox store is
                                                               				  already at the maximum size that can be backed up during non-business hours. |
| Note | Do not change the value of this field if the mailbox store is
                                                               				  already at the maximum size that can be backed up during non-business hours. |
| Step 4 | Select Save. |

| Note | Do not change the value of this field if the mailbox store is
                                                               				  already at the maximum size that can be backed up during non-business hours. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Message Storage and select Mailbox Stores. The Search Mailbox Store page displays the
                                             				currently configured mailbox stores. Note A user account without the System
                                                         				  Administrator role cannot create a new mailbox store. | Note | A user account without the System
                                                         				  Administrator role cannot create a new mailbox store. |
|---|---|---|---|
| Note | A user account without the System
                                                         				  Administrator role cannot create a new mailbox store. |
| Step 2 | Configure one or mailbox stores (For more
                                          			 information on each field, see Help> This Page): |

| Note | A user account without the System
                                                         				  Administrator role cannot create a new mailbox store. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Message Storage and select Mailbox Stores Membership. |
|---|---|
| Step 2 | On the Search Mailbox Stores Membership
                                          			 page, in the Choose Membership Type list, select User Mailbox. |
| Step 3 | In the User Mailbox Search Results section,
                                          			 specify the mailbox store from which you want to move the mailboxes. |
| Step 4 | Select the mailbox store to which you want
                                          			 to move the mailboxes and check the applicable check boxes for the users with
                                          			 mailboxes that you want to move. |
| Step 5 | Select Move Selected Mailboxes. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Message Storage and select Mailbox Stores. |
|---|---|
| Step 2 | On the Search Mailbox Stores page, select
                                          			 the mailbox store that you want to disable. |
| Step 3 | To disable a mailbox store: On the Edit Mailbox Store page, uncheck the
                                             				Mounted check box and select Save. |
| Step 4 | To re-enable a mailbox store: On the Edit Mailbox Store page, check the
                                             				Mounted check box and select Save. |

| Quota Level |  |  | Recording Time Before Quota is Reached/ Disk Space Used 1 |
|---|---|---|---|
| G.711 Mu-Law | G.711 A-Law | G.726 | PCM 8 kHz | PCM 16
                                                   						kHz 2 | G.729a | GSM 6.10 |
| Warning | 12 MB | The user is warned that the mailbox is reaching the maximum size
                                                   						allowed. | 18 min./ 11 KB/sec | 18 min./ 11 KB/sec | 37 min./ 5.53 KB/sec | 9 min./ 22 KB/sec | 4.5
                                                   						min./ 44 KB/sec | 122 min./ 1.67 KB/sec | 91 min./ 2.25 KB/sec |
| Send | 13 MB | The user is prevented from sending any more voice messages. | 20 min./ 11 KB/sec | 20 min./ 11 KB/sec | 40 min./ 5.53 KB/sec | 10 min./ 22 KB/sec | 5
                                                   						min./ 44 KB/sec | 132 min./ 1.67 KB/sec | 98 min./ 2.25 KB/sec |
| Send/ Receive | 14 MB | The user is prevented from sending or receiving any more voice
                                                   						messages. | 21 min./ 11 KB/sec | 21 min./ 11 KB/sec | 43 min./ 5.53 KB/sec | 10 min./ 22 KB/sec | 5
                                                   						min./ 44 KB/sec | 143 min./ 1.67 KB/sec | 106 min./ 2.25 KB/sec |
|  |  |  |  |  |  |  |  |  |  |

| Caution | Quotas alone can control the size of mailboxes for the users who
                                                			 regularly check Unity Connection voice messages using the telephone user
                                                			 interface. Web Inbox and Cisco ViewMail for Microsoft Outlook do not notify
                                                			 users that the mailbox has reached its limit. If users check messages using Web
                                                			 Inbox or Cisco ViewMail for Microsoft Outlook, you need to configure message
                                                			 aging so that the old messages are automatically deleted. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Message Storage > > > Mailbox Quotas > and select Mailbox Quotas. |
|---|---|
| Step 2 | On the Edit System-wide Mailbox Quotas page, enter the values of
                                                			 the required settings. (For more information on each field, see Help> This
                                                			 Page). |
| Step 3 | Select Save. Note For information to override system-wide mailbox quota settings
                                                               				  for Unity Connection users and user templates, see the “User Attributes” and
                                                               				  “Users” chapters. | Note | For information to override system-wide mailbox quota settings
                                                               				  for Unity Connection users and user templates, see the “User Attributes” and
                                                               				  “Users” chapters. |
| Note | For information to override system-wide mailbox quota settings
                                                               				  for Unity Connection users and user templates, see the “User Attributes” and
                                                               				  “Users” chapters. |

| Note | For information to override system-wide mailbox quota settings
                                                               				  for Unity Connection users and user templates, see the “User Attributes” and
                                                               				  “Users” chapters. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Tools and select Task Management. |
|---|---|
| Step 2 | On the Task Definitions page, select Quota
                                             			 Notification Mail. |
| Step 3 | On the Task Definition Basics (Quota
                                             			 Notification Mail) page, select Edit > Task Schedules. |
| Step 4 | On the Task Schedule page, enter the values
                                             			 of the required fields and select Save. (For more information on each field,
                                             			 see Help> This Page). Note The quota notification messages are not
                                                            				  sent to the users that do not have corporate email addresses configured. You can also execute the following command
                                                				through CLI to run the Quota Notification Mail task: run cuc sysagent task Umss.QuotaNotificationMailTask Umss.QuotaNotificationMailTask is the name
                                                				of the Quota Notification Mail task. For more information on the above command,
                                                				see the “run cuc sysagent task” section of the “Run commands” chapter of
                                                				Command Line Interface Reference Guide for Cisco Unified Communications
                                                				Solutions, Release 10.0(1), available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/10_0_1/CUCM_BK_CBEED39F_00_cucm-cli-reference-guide-100/CUCM_BK_CBEED39F_00_cucm-cli-reference-guide-100_chapter_0101.html#CUCM_CL_R812A687_00 . | Note | The quota notification messages are not
                                                            				  sent to the users that do not have corporate email addresses configured. |
| Note | The quota notification messages are not
                                                            				  sent to the users that do not have corporate email addresses configured. |

| Note | The quota notification messages are not
                                                            				  sent to the users that do not have corporate email addresses configured. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Message
                                             			 Storage> Mailbox Quotas and then select Quota Alert Text. |
|---|---|
| Step 2 | On the Edit Mailbox Quota Alert Text page, in the Language list,
                                             			 enter the values of the required fields. (For more information on each field,
                                             			 see Help> This Page). |
| Step 3 | Select Save. |
| Step 4 | Repeat Step2 through Step3 for each language installed on the
                                             			 system. |

| Note | The schedule for message aging is controlled by the message
                                                   				aging task that can be managed from the Task Management page in Cisco Unity
                                                   				Connection Administration. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Message Storage > Message Aging > and select Aging Policies . |
|---|---|
| Step 2 | Configure message aging policies, do the following steps (For
                                                			 more information on each field, see Help> This Page): |

| Caution | Do not change the settings of the Do Not Age Messages policy. |
|---|---|

| Note | You should not delete the Default System Policy and the Do Not
                                                         				  Age Messages policy. If you do not want to age messages, disable the Default
                                                         				  System Policy instead of deleting it. |
|---|---|

| Note | As all the message aging policies use the same five rules, if
                                             		  you customize the alert text for a rule, the text is the same for any policy
                                             		  that uses that rule. (For example, if you customize the email subject line and
                                             		  body text for the Move Saved Messages to the Deleted Items Folder rule, that
                                             		  text is used for all alerts that are sent to users who are assigned to any
                                             		  message aging policy for which that rule is enabled with alerts.) |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                                			 expand Message Storage > Message Aging and select Aging Alert Text . |
|---|---|
| Step 2 | On the Edit Message Aging Alert Text page,
                                                			 in the Language list, select the applicable language. |
| Step 3 | Enter the values of the required fields.
                                                			 (For more information on each field, see Help> This Page). |
| Step 4 | Select Save. |
| Step 5 | Repeat all the above steps for each language
                                                			 installed on the system. |

| Step 1 | In Cisco Unity Connection Administration, expand Message Storage> Message Aging and select Message Recording Expiration . |
|---|---|
| Step 2 | On the Edit Message Recording Expiration page, specify the
                                                			 number of message expiry days and check the Enabled check box. (For more
                                                			 information on each field, see Help> This Page ). |
| Step 3 | Specify the number of message expiry days for a video messages in
                                                			 Video Message Recordings Expire in field (For more information on each field,
                                                			 see Help> This Page ). |
| Step 4 | Select Save . Note The Message Recording Expiration feature does not apply to
                                                               				  messages that have been forwarded to personal email addresses or to message
                                                               				  recordings that have been saved locally to user workstations. To prevent users from saving local copies or forwarding voice
                                                   				messages to personal email addresses, consider configuring Unity Connection to
                                                   				mark all messages as secure. Unity Connection applies the Message Recording
                                                   				Expiration feature to messages in the mailboxes of recipients that are homed on
                                                   				the Unity Connection server. For example, if User A homed on Unity Connection
                                                   				server A sends a message to User B homed on Unity Connection server B, the
                                                   				message is subject to message expiration only if the Message Recording
                                                   				Expiration feature is enabled on server B. | Note | The Message Recording Expiration feature does not apply to
                                                               				  messages that have been forwarded to personal email addresses or to message
                                                               				  recordings that have been saved locally to user workstations. |
| Note | The Message Recording Expiration feature does not apply to
                                                               				  messages that have been forwarded to personal email addresses or to message
                                                               				  recordings that have been saved locally to user workstations. |

| Note | The Message Recording Expiration feature does not apply to
                                                               				  messages that have been forwarded to personal email addresses or to message
                                                               				  recordings that have been saved locally to user workstations. |
|---|---|