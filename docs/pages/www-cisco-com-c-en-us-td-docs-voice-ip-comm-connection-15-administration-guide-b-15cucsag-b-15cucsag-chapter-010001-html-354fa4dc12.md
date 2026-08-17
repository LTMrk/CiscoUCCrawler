---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-administration-guide-b-15cucsag-b-15cucsag-chapter-010001-html-354fa4dc12
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag/b_15cucsag_chapter_010001.html
retrieved_at: 2026-08-17T02:20:03.675115+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 12, 2025

Chapter: Advanced System Settings

## Chapter: Advanced System Settings

# Advanced System Settings

## Advanced System Settings

The Advanced menu in Cisco Unity Connection Administration enables the administrator to manage the system wide settings for
                           different features and parameters, such as messaging and conversations in Cisco Unity Connection.

## SMPP Providers

The SMPP providers offer SMS messaging to Unity Connection users and enable message notifications.

## Conversations

You can configure several system-wide conversation settings that affects all users in Unity Connection.

### Applying Conversation Settings for All Users

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings> Advanced and select Conversation.

Step 2

Enter the values of the in the required
                                          			 conversation settings and select Save. (For information on each field, see
                                          			 Help> This Page).

### Conversation
                           	 Settings

Following are the conversation settings:

Accessibility Settings in Effect During PIN Entry Conversation:
                                    			 The individual user phone menu accessibility settings do not take effect until
                                    			 a user is authenticated by entering the voicemail PIN.

Addressing Priority Lists: When a user attempts to address a
                                    			 message to a recipient by saying a name or spelling part of a name, he/she may
                                    			 find multiple matching names. You can configure two mechanisms that to
                                    			 prioritize certain recipients, sorting the results and offering the names with
                                    			 higher weights first in the search results. You can customize how names are
                                    			 stored in addressing priority lists and how long the names are stored.

Addressing and Recording Order: The standard conversation can be
                                    			 customized in which users can address and record when they send or forward
                                    			 messages to other users or distribution lists. You can customize the user
                                    			 conversation to address a message before recording the message or an
                                    			 introduction. This setting change is applied systemwide to all users. You
                                    			 cannot change the order in which users address and record when they reply to
                                    			 messages.

Announcing to Users when Messages are Marked Secure: When the
                                    			 Announce Secure Status in Message Header check box is checked, Unity Connection
                                    			 plays a prompt to the user before playing a secure message, announcing that it
                                    			 is a secure message.

If you have configured Unity Connection such that all messages
                              		left by both users and outside callers are configured to be secure, consider
                              		unchecking this check box so that users do not hear the secure message prompt
                              		before every message that they listen to.

Announcing When a Message has been Sent to Multiple Recipients
                                    			 and Listing Message Recipients: The conversation can be customized so that when
                                    			 a message has been sent to multiple recipients, Unity Connection announces that
                                    			 fact to the user before playing the message.

Unity Connection can also be customized so that users can hear a
                              		list of all of the recipients of a message. By default, this functionality is
                              		not enabled for the touchtone conversation, and must be configured using the
                              		Custom Keypad Mapping tool. Depending on how you configure the key mapping,
                              		users can hear the list of message recipients when they press the applicable
                              		key while listening to the message header, body, footer, or after-message
                              		prompts.

Automatically Added Alternate Extensions: When a user signs in
                                    			 from a phone number other than a primary extension or alternate extension, the
                                    			 number is added to the calling party ID (CPID) history of the user. When a
                                    			 number is added as an alternate extension, the user can sign in to Unity
                                    			 Connection from the number without having to enter a user ID (the primary
                                    			 extension).

Call Holding Wait Time: With call holding, when the phone is
                                    			 busy, Unity Connection can ask callers to hold. Each caller remains in the
                                    			 queue according to the settings that you configure.

Announcing Message Status on Reply or Reply-All: Unity
                                    			 Connection announces message status to the users when they reply or reply-all
                                    			 to a message. By default, when a user replies or reply-all to a message, Unity
                                    			 Connection do not announce any message status.

Announcing Recipient List on Reply or Reply-All: When a message
                                    			 is sent to multiple recipients and/or distribution lists, recipients have the
                                    			 option to reply-all. Unity Connection announces the recipient list to the users
                                    			 when they reply-all to a message whose number of recipients is less than the
                                    			 number specified in the Maximum Number of Recipients Before Reply-all Warning
                                    			 field.

See Table 17-1 , when the
                              		administrator enables or disables the Announce Message Status to User(s) while
                              		Replying option.

Message Status Announcement

User Action

Announce Message Status to User(s) while Replying

Expected Behavior of Unity Connection

Reply to a message

Disabled

Do not announce message status

Reply-all to a message

Disabled

Do not announce message status

Reply to a message

Enabled

Announces the status of the message

Reply-all to a message

Enabled

Announces the status of the message

Announcing Message Status on Reply or Reply-All: When a message
                                    			 is sent to multiple recipients and/or distribution lists, recipients have the
                                    			 option to reply-all. Unity Connection announces the recipient list to the users
                                    			 when they reply-all to a message whose number of recipients is less than the
                                    			 number specified in the Maximum Number of Recipients Before Reply-all Warning
                                    			 field.

Unity Connection 10.0(1) and later plays only the recipient
                              		name, when the user reply to a message. Reply to a message is irrespective of
                              		the value mentioned in the Maximum Number of Recipients Before Reply-all
                              		warning field.

See Table 17-2 , when the
                              		administrator enable or disable the Announce Message Status to User(s) while
                              		Replying option.

Message Status Announcement

User Action

Announce Message Status to User(s) while Replying

Expected Behavior of Unity Connection

Reply to a message

Disabled

Do not announce message status.

Reply-all to a message

Disabled

Do not announce message status.

Reply to a message

Enabled

Announces the status of the message.

Reply-all to a message

Enabled

Announces the status of the message.

Announcing Recipient List on Reply or Reply-All: When a message
                                    			 is sent to multiple recipients and/or distribution lists, recipients have the
                                    			 option to reply-all. Unity Connection 10.0(1) and later plays only the
                                    			 recipient name, when the user reply to a message. Reply to a message is
                                    			 irrespective of the value mentioned in the Maximum Number of Recipients Before
                                    			 Reply-all warning field.

See Table 17-3 , when the
                              		administrator enable or disable the Announce Recipients list to User(s) while
                              		Replying option.

Message Status Announcement

User Action

Announce Message Status to User(s) while Replying

Expected Behavior of Unity Connection

Reply to a message

Disabled

Do not play the recipient name.

Reply-all to a message

Disabled

Do not play the recipient list.

Reply to a message

Enabled

Plays the recipient name.

Reply-all to a message

Enabled

Plays the recipient list.

Warning users on Reply-All When Number of Recipients Exceeds
                                    			 Maximum: When a message is sent to multiple recipients and/or distribution
                                    			 lists, recipients have the option to reply-all. Unity Connection warns users
                                    			 when they reply-all to a message whose number of recipients is equal to or
                                    			 exceeds the number specified in the Maximum Number of Recipients Before
                                    			 Reply-all Warning field.

Caller Information: The user conversation can be customized so
                                    			 that it provides users with additional information about each caller who left a
                                    			 message, before it plays the message. See Table 17-4 for caller
                                    			 information.

For Messages Left by This Type of Caller

Message Type

Cisco Unity Connection Plays This by Default

Cisco Unity Connection Plays This When Additional Caller
                                          				  Information Is Offered

Identified user (including call handlers)

Voice, 
                                          				  receipts

The recorded name of the user (or call handler). If the user (or
                                          				  call handler) does not have a recorded name, Unity Connection uses Text to
                                          				  Speech to play the display name. If the user does not have a display name,
                                          				  Unity Connection plays the primary extension instead.

Both the recorded name (if available) and the primary extension
                                          				  (if available) before playing the message.

If the user (or call handler) does not have a recorded name,
                                          				  Unity Connection uses Text to Speech to play the display name of the user (or
                                          				  call handler) instead.

Outside caller

Voice

The message, without announcing who it is from or playing the
                                          				  phone number of the caller first.

The phone number (if available) of the caller before playing the
                                          				  message.

Dial Prefix Settings for Live Reply to Unidentified Callers:
                                    			 When live reply is enabled, users who are listening to messages by phone can
                                    			 reply to a message by calling the sender. When a user attempts to reply by
                                    			 calling an unidentified caller, Unity Connection checks the calling number
                                    			 provided by the phone system in the Automatic Number Identification (ANI)
                                    			 string against the transfer restriction table that is associated with the user
                                    			 class of service.

Deleting Messages: You can customize the standard conversation
                                    			 to change what users hear when they manage their deleted messages in the
                                    			 following ways:

As alternatives to the default, you can specify that Unity
                              		Connection does not prompt users to choose, and instead permanently deletes the
                              		type of messages that you specify: either deleted voice messages or all deleted
                              		messages (voice and email, as applicable). To set up either alternative, change
                              		the Multiple Message Delete Mode setting by entering one of the following
                              		values:

1 —Users choose which messages are deleted; Unity Connection
                                    			 prompts them: “To delete only your voice messages, press 1. To delete all
                                    			 messages, press 2.” (Default setting)

2 —Unity Connection does not prompt users to choose which
                                    			 messages to delete; instead, Unity Connection deletes all of their deleted
                                    			 voice messages.

3 —Unity Connection does not prompt users to choose which
                                    			 messages to delete; instead, Unity Connection deletes all of their deleted
                                    			 messages (voice messages, receipts, and email messages, as applicable).

Language of System Prompts: Phone languages are the languages in
                                    			 which Unity Connection can play system prompts to users and callers. The phone
                                    			 language setting is available for the following Unity Connection components:
                                    			 user accounts, routing rules, call handlers, interview handlers, and directory
                                    			 handlers.

Sign in from a User Greeting: Caller input settings allow you to
                                    			 specify how users sign in to Unity Connection when they are listening to a user
                                    			 greeting. Using the caller input settings you can specify which keys users can
                                    			 press to interrupt a user greeting so that they can sign in to Unity
                                    			 Connection, and what users hear after Unity Connection prompts them to sign in.

The Table 17-5 summarizes
                              		the options available to you for specifying how users sign in to Unity
                              		Connection from their own greeting or from another user greeting.

Conversation

Description

Use

Best Practice

Sign-In

Prompts users to enter an ID and PIN when they press * during
                                          				  any user greeting.

Enabled by default.

To avoid leaving a message as an unidentified caller, users can
                                          				  sign in to Unity Connection from another user greeting when they call the user
                                          				  from a phone that is not associated with their account. (Unity Connection users
                                          				  cannot reply to messages from unidentified callers.)

Continue to offer the Sign-In conversation.

If you are considering reassigning the key used to access the
                                          				  Sign-In conversation, consider that users also access the Sign-In conversation
                                          				  by pressing * from the Opening Greeting.

Easy Sign-In

Prompts users to enter a PIN when they press a key during any
                                          				  user greeting.

Disabled by default. (No key is mapped to the Easy Sign-In
                                          				  conversation.)

Users can dial their extensions and sign in quickly without
                                          				  having to remember the pilot number to access Unity Connection by phone.

Users may prefer Easy Sign-In to the Sign-In conversation
                                          				  because it saves them from having to re-enter an extension during the sign-in
                                          				  process. Note that Unity Connection uses the calling extension (rather than the
                                          				  dialed extension) to determine which mailbox the user is trying to sign in to.

Provide Easy Sign-In to users who want a faster way to sign in
                                          				  from their own greeting or to accommodate users who are accustomed to another
                                          				  voice messaging system.

Keys 1–9 are unmapped, and are therefore good choices for
                                          				  assigning to the Easy Sign-In conversation. Consider the following if you are
                                          				  thinking of using the *, 0, or # key instead:

Avoid reassigning the * key so that you can continue to offer
                                                						the Sign-In conversation.

The # key is already set up to skip greetings. It is also the
                                                						key that users use to skip ahead throughout the Unity Connection conversation.

The 0 key is already set up to send callers to the Operator call
                                                						handler.

## Messaging

The Messaging settings page enables to manage the message
                           		configuration values. For more information on each field, see Help> This
                           		Page. For information on messaging, see the Messaging chapter.

## Intrasite
                        	 Networking

The Intrasite Networking settings page enables to manage the intrasite networking configuration. For more information, see
                           the Networking Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html .

## Telephony

The Telephony settings enables to manage the telephony
                           		integration settings of Unity Connection. For more information on each field,
                           		see Help> This Page.

For information on telephony integration, see the Telephony Integration chapter.

## Reports

Reports in Unity Connection are generated to gather information about the system configuration and call management components,
                           such as call handlers and users. Unity Connection is automatically set to gather and store the data from which you can generate
                           reports.

To manage reports in Unity Connection, sign in to Cisco Unity Connection Administration, expand System Settings > Advanced
                           and select Reports. (For more information on each field, see Help> This Page).

### Available Reports

You can generate and view reports in Cisco Unity Connection Serviceability. To go to Cisco Unity Connection Serviceability,
                                 select Cisco Unity Connection Serviceability in the navigation pane and select Go.

For details on generating and viewing reports for Cisco Unity Connection Serviceability, see the Administration Guide for
                                 Cisco Unity Connection Serviceability at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

The Table 17-6 describes the reports available in Unity Connection.

Reports Available in Unity Connection

Report Name

Description of Output

Phone Interface Failed Sign-In

Includes the following information for every failed attempt to sign in to Unity Connection by phone:

Username, alias, caller ID, and extension or URI of user who failed to sign in.

Date and time the failed sign in occurred.

Whether the maximum number of failed sign in has reached for the user.

Users

Includes the following information for each user:

Last name, first name, and alias.

Information that identifies the Unity Connection or Cisco Unified CMBE server associated with the user.

Billing ID, class of service, and extension or URI.

Whether the account is locked.

Whether the user has enabled personal call transfer rules.

Message Traffic

Includes totals for the following traffic categories:

Voice.

Fax.

Email.

Non-delivery receipt (NDR).

Delivery receipt.

Read receipt.

Hourly totals.

Daily totals.

Port Activity

Includes the following information for voice messaging ports:

Name.

Number of inbound calls handled.

Number of outbound MWI calls handled.

Number of outbound AMIS calls handled.

Number of outbound notification calls handled.

Number of outbound TRAP calls handled.

Total number of calls handled.

Mailbox Store

Includes the following information about the specified mailbox stores:

Mail database name.

Display name.

Server name.

Whether access is enabled.

Mailbox store size.

Last error.

Status.

Whether the mail database can be deleted.

Dial Plan

Includes a list of the search spaces configured on the Unity Connection or Cisco Unified CMBE server with an ordered list
                                             of partitions assigned to each search space.

If the server is part of a digital network, the report also lists the search spaces and associated partition membership on
                                             every other Unity Connection location on the network.

Dial Search Scope

Includes a list of all the users and the extensions or URIs in the specified partition that is configured in the Unity Connection
                                             directory. If a partition is not specified, the report lists all users and their extensions for all partitions that are configured
                                             in the directory.

User Phone Sign-In and MWI

Includes the following information about phone sign-ins, MWI activity, and message notifications to phone devices per user:

Name, extension, and class of service.

Date and time for each activity.

The source of each activity.

Action completed (for example, Sign-in, MWI On or Off, and Phone Dialout).

Dial out number and results (applicable only for message notifications to phone devices).

The number of new messages for a user at the time of sign in.

User Message Activity

Includes the following information about messages sent and received per user:

Name, extension, and class of service.

Date and time for each message.

Type of message.

Action completed, such as received new message or message saved.

Information on the message sender.

Distribution Lists

Includes the following information of a distribution list:

Name and display name of the list.

Date and time the list was created. (Date and time are given in Greenwich Mean Time.)

A count of the number of users included in the list.

If the Include List Members check box is checked, a listing of the alias of each user who is a member of the list.

User Lockout

Includes user alias, the number of failed sign-in attempts for the user, credential type (a result of “4” indicates a sign-in
                                             attempt from the Unity Connection conversation; a result of “3” indicates a sign-in attempt from a web application), and the
                                             date and time that the account was locked.

(Date and time are given in Greenwich Mean Time.)

Unused Voice Mail Accounts

Includes the user alias, display name, date and time when the user account was created.

(Date and time are given in Greenwich Mean Time.)

Transfer Call Billing

Includes the following information for each call:

Name, extension, and billing ID of the user.

Date and time that the call occurred.

The phone number dialed.

The result of the transfer (connected, ring-no-answer (RNA), busy, or unknown).

Outcall Billing Detail

Includes the following information, arranged by day and the extension of the user who placed the call:

Name, extension, and billing ID.

Date and time the call was placed.

The phone number called.

The result of the call (connected, ring-no-answer (RNA), busy, or unknown).

The duration of the call in seconds.

Outcall Billing Summary

Arranged by date and according to the name, extension or URI, and billing ID of the user who placed the call. It is listed
                                             24 hours of the day with a dialout time in seconds specified for each hour span.

Call Handler  Traffic

Includes the following information for each call handler:

Total number of calls.

Number of times each key on the phone keypad was pressed.

Extension.

Invalid extension.

Number of times the after greeting action occurred.

Number of times the caller hung up.

System Configuration

Includes detailed information about all aspects of the configuration of the Unity Connection system.

SpeechView Activity Report by User

Includes the total number of transcribed messages, failed transcriptions, and truncated transcriptions for a given user during
                                             a given time period. If the report is run for all users, then the output is broken out by user.

SpeechView Activity Summary Report

Includes the total number of transcribed messages, failed transcriptions, and truncated transcriptions for the entire system
                                             during a given time period. When messages are sent to multiple recipients, the message is transcribed only once, so the transcription
                                             activity is counted only once.

## Connection
                        	 Administration

Connection Administration modifies the following administration
                           		settings:

Database Proxy

Voice Mail Web Service

Cisco Unified Mobile Advantage

Session Timeout

Display Schedules

User Inactivity Timeout

### Editing Administration Settings using Cisco Unity Connection
                           	 Administration

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select Connection Administration.

Step 2

On the Connection Administration
                                          			 Configuration page, enter the applicable settings and select Save. (For more
                                          			 information on each field, see Help> This Page).

## TRAP

TRAP modifies the Telephone Record and Play settings for session time out and dial-out.

### Editing Telephone Record and Play Settings

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select TRAP.

Step 2

On the TRAP Configuration page, enter the
                                          			 applicable settings and select Save. (For more information on each field, see
                                          			 Help> This Page).

## Disk
                        	 Capacity

The information about the messages in a database and the message
                           		content is stored as files on the Unity Connection server. Depending on the
                           		number of Unity Connection users, the number and duration of messages they
                           		receive, and the settings that you specify for the message aging policy and for
                           		quotas, it may be possible for the hard disk on which messages and greetings
                           		are stored to fill up. This would cause Unity Connection to stop functioning.
                           		As the hard disk approaches maximum capacity, you may also encounter unexpected
                           		behavior.

The disk capacity page describes the maximum capacity of the
                           		hard disk on which messages and greetings can be stored. The disk capacity can
                           		be managed in Cisco Unity Connection Administration> System Settings>
                           		Advanced> Disk Capacity. For more information, see Help> This Page.

When the hard disk fills to the specified percentage limit,
                           		neither users nor outside callers are allowed to leave voice messages. Unity
                           		Connection also logs an error that can be viewed on the Tools > SysLog
                           		Viewer page in the Real-Time Monitoring Tool.

You can still send a broadcast message even when the hard disk
                                       		  exceeds the specified limit.

If the disk capacity settings are changed, you need to restart
                           		the Connection Message Transfer Agent service in Cisco Unity Connection
                           		Serviceability.

If the hard disk exceeds the value that you specify, users
                           		should immediately delete unnecessary voice messages. In addition, to prevent a
                           		recurrence, you may want to re-evaluate message-aging policy and mailbox
                           		quotas. For more information, see the Controlling
                              		  the Size of Mailboxes section of the Message Storage chapter.

## PCA

Cisco Personal Communications Assistant (PCA) modifies the settings for Cisco Personal Communications Assistant Inbox and
                           session time out. For more information, see the “Setting Up Access to the Cisco Personal Communications Assistant” chapter
                           of the User Workstation Setup Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user_setup/guide/b_15cucuwsx.html .

### Editing the Settings for Cisco PCA Inbox

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select PCA.

Step 2

On the PCA Configuration page, enter the
                                          			 applicable settings and select Save. (For information on each field, see
                                          			 Help> This Page).

## RSS

Really Simple Syndication (RSS) is a web application that enables access to voice messaging. The RSS setting enables the insecure
                           RSS connections.

By default, Unity Connection only supports secure connections to the RSS feed using SSL. Some RSS readers, for example Apple
                           iTunes, do not support secure connections.

If you want to allow users to be able to use RSS readers that do not support secure connections, see the Enabling Insecure RSS Connections, page 17-11 section.

### Enabling Insecure RSS Connections

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select RSS.

Step 2

On the RSS Configuration page, check the
                                          			 Allow Insecure RSS Connections check box and select Save. (For information on
                                          			 each field, see Help> This Page).

### Configuring an RSS Reader to View Voice Messages

Users can configure an RSS reader to view voice messages. Following are some important considerations:

Use the following URL in the RSS Reader:

– https://<Unity Connection server name>/cisco-unity-rss/rss.do

The server name can either be the hostname, IPv4 address, or IPv6 address of the Unity Connection server.

When users connect to the RSS feed, they are required to provide the following:

Username: Enter the user alias.

Password: Enter the Cisco PCA password of the user (also known as the web application password).

### RSS Feed Limitations and Behavioral Notes

Only the 20 most recent unread messages are presented in the RSS feed.

If the message is secure or private, a decoy message plays instead of the actual message. The decoy message indicates that
                                    the message is secure or private and that the user must retrieve the message by calling in by phone.

Broadcast messages are not included in the RSS feed.

Messages cannot be deleted. Messages can only be marked read.

Marking a message read removes it from the RSS feed.

US English is the only language supported at this time.

Dispatch messages cannot be accepted, declined or postponed. Dispatch messages cannot be marked as read. A dispatch message
                                    remains in the RSS feed until it is handled via another interface or accepted by another recipient.

Some RSS readers do not allow the description of the message to contain hyperlinks. For those readers, the feed does not offer
                                    the option to mark the message as read.

For messages with multiple parts (for example a forwarded message with an introduction), not all parts of the message can
                                    be played. Only the first part (for example, the introduction) is played and the subject line indicates that there are more
                                    attachments. Users must retrieve the remaining message parts by calling in by phone.

## Cluster
                        	 Configuration

The Cluster Configuration settings page enables to manage the cluster during a maintenance window scenario when one of the
                           server is not functional. For more information, see the “ Configuring Cisco Unity Connection Cluster ” chapter in Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

## Fax

The Fax Settings page enables to manage the subject prefix for a
                           		successful or failed fax and the fax file types. For more information, see the Fax Server chapter.

## Unified Messaging
                        	 Services

The Unified Messaging Services settings define the settings for
                           		calendar and contact integrations that are supported with the unified messaging
                           		feature. For more information, see the Unified Messaging section.

## API
                        	 Settings

Application Programming Interface (API) provides provisioning, messaging, and telephony access to Unity Connection. It is
                           used to enable or disable the settings for Cisco Unity Connection Messaging Interface (CUMI) API. For more information, see
                           the “Cisco Unity Connection Overview” chapter of Design Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html .

### Enabling or Disable CUMI API Settings

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select API Settings.

Step 2

On the API Configuration page, enter the
                                          			 applicable settings and select Save. (For information on each field, see
                                          			 Help> This Page).

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings> Advanced and select Conversation. |
|---|---|
| Step 2 | Enter the values of the in the required
                                          			 conversation settings and select Save. (For information on each field, see
                                          			 Help> This Page). |

| User Action | Announce Message Status to User(s) while Replying | Expected Behavior of Unity Connection |
|---|---|---|
| Reply to a message | Disabled | Do not announce message status |
| Reply-all to a message | Disabled | Do not announce message status |
| Reply to a message | Enabled | Announces the status of the message |
| Reply-all to a message | Enabled | Announces the status of the message |

| User Action | Announce Message Status to User(s) while Replying | Expected Behavior of Unity Connection |
|---|---|---|
| Reply to a message | Disabled | Do not announce message status. |
| Reply-all to a message | Disabled | Do not announce message status. |
| Reply to a message | Enabled | Announces the status of the message. |
| Reply-all to a message | Enabled | Announces the status of the message. |

| User Action | Announce Message Status to User(s) while Replying | Expected Behavior of Unity Connection |
|---|---|---|
| Reply to a message | Disabled | Do not play the recipient name. |
| Reply-all to a message | Disabled | Do not play the recipient list. |
| Reply to a message | Enabled | Plays the recipient name. |
| Reply-all to a message | Enabled | Plays the recipient list. |

| For Messages Left by This Type of Caller | Message Type | Cisco Unity Connection Plays This by Default | Cisco Unity Connection Plays This When Additional Caller
                                          				  Information Is Offered |
|---|---|---|---|
| Identified user (including call handlers) | Voice, 
                                          				  receipts | The recorded name of the user (or call handler). If the user (or
                                          				  call handler) does not have a recorded name, Unity Connection uses Text to
                                          				  Speech to play the display name. If the user does not have a display name,
                                          				  Unity Connection plays the primary extension instead. | Both the recorded name (if available) and the primary extension
                                          				  (if available) before playing the message. If the user (or call handler) does not have a recorded name,
                                          				  Unity Connection uses Text to Speech to play the display name of the user (or
                                          				  call handler) instead. |
| Outside caller | Voice | The message, without announcing who it is from or playing the
                                          				  phone number of the caller first. | The phone number (if available) of the caller before playing the
                                          				  message. |

| Conversation | Description | Use | Best Practice |
|---|---|---|---|
| Sign-In | Prompts users to enter an ID and PIN when they press * during
                                          				  any user greeting. Enabled by default. | To avoid leaving a message as an unidentified caller, users can
                                          				  sign in to Unity Connection from another user greeting when they call the user
                                          				  from a phone that is not associated with their account. (Unity Connection users
                                          				  cannot reply to messages from unidentified callers.) | Continue to offer the Sign-In conversation. If you are considering reassigning the key used to access the
                                          				  Sign-In conversation, consider that users also access the Sign-In conversation
                                          				  by pressing * from the Opening Greeting. |
| Easy Sign-In | Prompts users to enter a PIN when they press a key during any
                                          				  user greeting. Disabled by default. (No key is mapped to the Easy Sign-In
                                          				  conversation.) | Users can dial their extensions and sign in quickly without
                                          				  having to remember the pilot number to access Unity Connection by phone. Users may prefer Easy Sign-In to the Sign-In conversation
                                          				  because it saves them from having to re-enter an extension during the sign-in
                                          				  process. Note that Unity Connection uses the calling extension (rather than the
                                          				  dialed extension) to determine which mailbox the user is trying to sign in to. | Provide Easy Sign-In to users who want a faster way to sign in
                                          				  from their own greeting or to accommodate users who are accustomed to another
                                          				  voice messaging system. Keys 1–9 are unmapped, and are therefore good choices for
                                          				  assigning to the Easy Sign-In conversation. Consider the following if you are
                                          				  thinking of using the *, 0, or # key instead: Avoid reassigning the * key so that you can continue to offer
                                                						the Sign-In conversation. The # key is already set up to skip greetings. It is also the
                                                						key that users use to skip ahead throughout the Unity Connection conversation. The 0 key is already set up to send callers to the Operator call
                                                						handler. |

| Report Name | Description of Output |
|---|---|
| Phone Interface Failed Sign-In | Includes the following information for every failed attempt to sign in to Unity Connection by phone: Username, alias, caller ID, and extension or URI of user who failed to sign in. Date and time the failed sign in occurred. Whether the maximum number of failed sign in has reached for the user. |
| Users | Includes the following information for each user: Last name, first name, and alias. Information that identifies the Unity Connection or Cisco Unified CMBE server associated with the user. Billing ID, class of service, and extension or URI. Whether the account is locked. Whether the user has enabled personal call transfer rules. |
| Message Traffic | Includes totals for the following traffic categories: Voice. Fax. Email. Non-delivery receipt (NDR). Delivery receipt. Read receipt. Hourly totals. Daily totals. |
| Port Activity | Includes the following information for voice messaging ports: Name. Number of inbound calls handled. Number of outbound MWI calls handled. Number of outbound AMIS calls handled. Number of outbound notification calls handled. Number of outbound TRAP calls handled. Total number of calls handled. |
| Mailbox Store | Includes the following information about the specified mailbox stores: Mail database name. Display name. Server name. Whether access is enabled. Mailbox store size. Last error. Status. Whether the mail database can be deleted. |
| Dial Plan | Includes a list of the search spaces configured on the Unity Connection or Cisco Unified CMBE server with an ordered list
                                             of partitions assigned to each search space. If the server is part of a digital network, the report also lists the search spaces and associated partition membership on
                                             every other Unity Connection location on the network. |
| Dial Search Scope | Includes a list of all the users and the extensions or URIs in the specified partition that is configured in the Unity Connection
                                             directory. If a partition is not specified, the report lists all users and their extensions for all partitions that are configured
                                             in the directory. |
| User Phone Sign-In and MWI | Includes the following information about phone sign-ins, MWI activity, and message notifications to phone devices per user: Name, extension, and class of service. Date and time for each activity. The source of each activity. Action completed (for example, Sign-in, MWI On or Off, and Phone Dialout). Dial out number and results (applicable only for message notifications to phone devices). The number of new messages for a user at the time of sign in. |
| User Message Activity | Includes the following information about messages sent and received per user: Name, extension, and class of service. Date and time for each message. Type of message. Action completed, such as received new message or message saved. Information on the message sender. |
| Distribution Lists | Includes the following information of a distribution list: Name and display name of the list. Date and time the list was created. (Date and time are given in Greenwich Mean Time.) A count of the number of users included in the list. If the Include List Members check box is checked, a listing of the alias of each user who is a member of the list. |
| User Lockout | Includes user alias, the number of failed sign-in attempts for the user, credential type (a result of “4” indicates a sign-in
                                             attempt from the Unity Connection conversation; a result of “3” indicates a sign-in attempt from a web application), and the
                                             date and time that the account was locked. (Date and time are given in Greenwich Mean Time.) |
| Unused Voice Mail Accounts | Includes the user alias, display name, date and time when the user account was created. (Date and time are given in Greenwich Mean Time.) |
| Transfer Call Billing | Includes the following information for each call: Name, extension, and billing ID of the user. Date and time that the call occurred. The phone number dialed. The result of the transfer (connected, ring-no-answer (RNA), busy, or unknown). |
| Outcall Billing Detail | Includes the following information, arranged by day and the extension of the user who placed the call: Name, extension, and billing ID. Date and time the call was placed. The phone number called. The result of the call (connected, ring-no-answer (RNA), busy, or unknown). The duration of the call in seconds. |
| Outcall Billing Summary | Arranged by date and according to the name, extension or URI, and billing ID of the user who placed the call. It is listed
                                             24 hours of the day with a dialout time in seconds specified for each hour span. |
| Call Handler  Traffic | Includes the following information for each call handler: Total number of calls. Number of times each key on the phone keypad was pressed. Extension. Invalid extension. Number of times the after greeting action occurred. Number of times the caller hung up. |
| System Configuration | Includes detailed information about all aspects of the configuration of the Unity Connection system. |
| SpeechView Activity Report by User | Includes the total number of transcribed messages, failed transcriptions, and truncated transcriptions for a given user during
                                             a given time period. If the report is run for all users, then the output is broken out by user. |
| SpeechView Activity Summary Report | Includes the total number of transcribed messages, failed transcriptions, and truncated transcriptions for the entire system
                                             during a given time period. When messages are sent to multiple recipients, the message is transcribed only once, so the transcription
                                             activity is counted only once. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select Connection Administration. |
|---|---|
| Step 2 | On the Connection Administration
                                          			 Configuration page, enter the applicable settings and select Save. (For more
                                          			 information on each field, see Help> This Page). |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select TRAP. |
|---|---|
| Step 2 | On the TRAP Configuration page, enter the
                                          			 applicable settings and select Save. (For more information on each field, see
                                          			 Help> This Page). |

| Note | You can still send a broadcast message even when the hard disk
                                       		  exceeds the specified limit. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select PCA. |
|---|---|
| Step 2 | On the PCA Configuration page, enter the
                                          			 applicable settings and select Save. (For information on each field, see
                                          			 Help> This Page). |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select RSS. |
|---|---|
| Step 2 | On the RSS Configuration page, check the
                                          			 Allow Insecure RSS Connections check box and select Save. (For information on
                                          			 each field, see Help> This Page). |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced and select API Settings. |
|---|---|
| Step 2 | On the API Configuration page, enter the
                                          			 applicable settings and select Save. (For information on each field, see
                                          			 Help> This Page). |