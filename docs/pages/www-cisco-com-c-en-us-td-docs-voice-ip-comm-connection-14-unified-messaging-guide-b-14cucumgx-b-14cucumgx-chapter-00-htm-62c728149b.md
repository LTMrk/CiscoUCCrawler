---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-unified-messaging-guide-b-14cucumgx-b-14cucumgx-chapter-00-htm-62c728149b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx/b_14cucumgx_chapter_00.html
retrieved_at: 2026-08-16T18:39:12.831445+00:00
---

Unified Messaging Guide for Cisco Unity Connection Release 14

# Unified Messaging Guide for Cisco Unity Connection Release 14

Updated: February 19, 2025

Chapter: Introduction to Unified Messaging

## Chapter: Introduction to Unified Messaging

# Introduction to Unified Messaging

## Overview

The unified messaging feature provides a single storage for
                           		different types of messages, such as voicemails and emails that are accessible
                           		from a variety of devices. For example, a user can access a voicemail either
                           		from the email inbox using computer speakers or directly from the phone
                           		interface.

The following are the supported mail server with which you can
                           		integrate Unity Connection to enable unified messaging:

Microsoft Exchange (2010, 2013, 2016 and 2019) servers

Microsoft Office 365

Cisco Unified MeetingPlace

Gmail Server

Integrating Unity Connection with an Exchange or Office 365
                           		server provides the following functionalities:

Synchronization of voicemails between Unity Connection and
                                 			 Exchange/ Office 365 mailboxes.

Text-to-speech (TTS) access to Exchange/ Office 365 email.

Access to Exchange/ Office 365 calendars that allows users to do
                                 			 meeting-related tasks by phone, such as, hear a list of upcoming meetings and
                                 			 accept or decline meeting invitations.

Access to Exchange/ Office 365 contacts that allows users to
                                 			 import Exchange/ Office 365 contacts and use the contact information in
                                 			 personal call transfer rules and when placing outgoing calls using voice
                                 			 commands.

Transcription of Unity Connection voicemails.

Integrating Unity Connection with Cisco Unified MeetingPlace
                           		provides the following functionalities:

Join a meeting that is in progress.

Hear a list of the participants for a meeting.

Send a message to the meeting organizer and meeting
                                 			 participants.

Set up immediate meetings.

Cancel a meeting (applied to meeting organizers only).

Integrating Unity Connection with Gmail Server provides the following functionalities:

Synchronization of voicemails between Unity Connection and Gmailboxes.

Text-to-speech (TTS) access to Gmail.

Access to Gmail calendars that allows users to do meeting-related tasks by phone, such as, hear a list of upcoming meetings
                                 and accept or decline meeting invitations.

Access to Gmail contacts that allows users to import Gmail contacts and use the contact information in personal call transfer
                                 rules and when placing outgoing calls using voice commands.

Transcription of Unity Connection voicemails.

### Unified Messaging with Google Workspace

Unity Connection 14 and later provides a new way to users for accessing the voice messages on their Gmail account. For this,
                              you need to configure unified messaging with Google Worspace to synchronize the voice messages between Unity Connection and
                              Gmail server.

Integrating Unity Connection with Gmail server provides the following functionalities:

Synchronization of voicemails between Unity Connection and mailboxes

Transcription of Unity Connection voicemails.

## Single Inbox for Exchange/Office 365

The synchronization of user messages between Unity Connection and supported mail servers is known as Single Inbox. When the
                           single inbox feature is enabled on Unity Connection, voice mails are first delivered to the user mailbox in Unity Connection
                           and then the mails are replicated to the user mailbox on supported mail servers. For information on configuring the Single
                           Inbox in Unity Connection, refer Configuring Unified Messaging chapter.

- The single inbox feature is supported with both IPv4 and IPv6 addresses.

- When the single inbox feature is enabled for a user, the Outlook rules may not work for single inbox messages.

- To see the maximum number of users supported for Exchange and Office 365 server, see the section “ Specification for Virtual Platform Overlays” of the Cisco Unity Connection 14 Supported Platform List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html .

### Storing Voicemails for Single Inbox Configuration

All Unity Connection voicemails, including those sent from Cisco ViewMail for Microsoft Outlook, are first stored in Unity
                              Connection and are immediately replicated to the Exchange/ Office 365 mailbox for the recipient.

### Single Inbox with
                           	 ViewMail for Outlook

Consider the following points if you want to use Outlook for
                              		sending, replying, and forwarding voicemails and to synchronize the messages
                              		with Unity Connection:

Install ViewMail for Outlook on user workstations. If ViewMail
                                    			 for Outlook is not installed, the voicemails that are sent by Outlook are
                                    			 treated as .wav file attachments by Unity Connection. For more information on
                                    			 installing ViewMail for Outlook, see the Release Notes for Cisco ViewMail for Microsoft Outlook for the
                                    			 latest release at http://www.cisco.com/en/US/products/ps6509/prod_release_notes_list.html .

Make sure to add SMTP proxy addresses for
                                    			 unified messaging users in Unity Connection. The SMTP proxy address of a user
                                    			 specified in Cisco Unity Connection Administration must match the Exchange/
                                    			 Office 365 email address specified in the unified messaging account in which
                                    			 single inbox is enabled.

Associate an email account of each user in the organization with
                                    			 a Unity Connection server domain.

The Outlook Inbox folder contains both voicemails and the other
                              		messages stored in Exchange/ Office 365. The voicemails also appear in the Web
                              		Inbox of a user.

A single inbox user has a Voice Outbox folder added to the Outlook mailbox. Unity Connection
                              		voicemails sent from Outlook do not appear in the Sent Items folder.

### Single Inbox without ViewMail for Outlook or with Other Email Clients

If you do not install ViewMail for Outlook or use another email client to access Unity Connection voicemails in Exchange/
                              Office 365:

The email client treats voicemails as emails with .wav file attachments.

When a user replies to or forwards a voicemail, the reply or forward also is treated as an email even if the user attaches
                                    a .wav file. Message routing is handled by Exchange/ Office 365, not by Unity Connection, so the message is never sent to
                                    the Unity Connection mailbox for the recipient.

Users cannot listen to secure voicemails.

It may be possible to forward private voicemails. (ViewMail for Outlook prevents private messages from being forwarded).

### Accessing Secure Voicemails in the Exchange/ Office 365 Mailbox

To play secure voicemails in the Exchange/ Office 365 mailbox, users must use Microsoft Outlook and Cisco ViewMail for Microsoft
                              Outlook. If ViewMail for Outlook is not installed, users accessing secure voicemails see only text in the body of a decoy
                              message which briefly explains the secure messages.

### Transcription of Voicemails Synchronized Between Unity Connection and Exchange/Office 365

A system administrator can enable the single inbox transcription functionality by configuring the unified messaging services
                              and the SpeechView transcription services on Unity Connection. "Synchronization of multiple forward messages” service is not
                              supported with Unity Connection, if configured with Single Inbox.

For information on configuring unified messaging services in Unity Connection, refer chapter " Configuring Unified Messaging ".  For information on configuring SpeechView transcription service, see the “ SpeechView ” chapter of the System Administration Guide for Cisco Unity Connection, Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

When sender sends voicemail to a user through Web Inbox or touchtone conversation user interface and the user views voicemail
                                          through various email clients, then the transcription of voicemails are synchronized as shown in the Table 1 .

When Sender Sends Voice Mail through Web Inbox or Touchtone Conversation User Interface

Scenarios

Web Inbox

Outlook WebMail Access/ Outlook without VMO

ViewMail for Outlook

Successful delivery of voicemails

The text of the transcription gets displayed in the reading pane of the email.

The text of transcription gets displayed in the reading pane of the email.

The text of the transcription gets displayed in the reading pane of the email and is also displayed in the transcription panel.

Failure or Response Time-out

The “Failure or Response Timeout” text gets displayed in the reading pane of the email.

The “Failure or Response Timeout” text gets displayed in the reading pane of the email.

The “Failure or Response Timeout” text gets displayed in the reading pane of the email and is also displayed in the transcription panel.

Transcription in Progress

The “Transcription in Progress” text gets displayed in the reading pane of the email.

The reading pane of the email is blank .text.

The “Transcription in Progress” text gets displayed in the transcription panel.

When sender sends voicemail to a Unity Connection user through ViewMail for Outlook and the Unity Connection user views voicemail
                                          through various email clients, then the transcription of voicemails are synchronized, as shown in the Table 2 :

When Sender Sends Voicemaill through ViewMail for Outlook

Scenarios

Web Inbox

Outlook WebMail Access/ Outlook without VMO

ViewMail for Outlook

Successful delivery of voicemails

The text of transcription gets displayed in the reading pane of the email.

The text of the transcription is the part of transcript file “Transcription.txt”.

The text of the transcription is the part of transcript file “Transcription.txt” and is also displayed in the transcription
                                                panel.

Failure or Response Time-out

The “Failure or Response Timeout” text gets displayed in the reading pane of the email.

The “Failure or Response Time-out” text is the part of transcript file “Trancription.txt” attached in the voicemail.

The “Failure or Response Time-out” text is the part of transcript file “Trancription.txt” attached in the voicemail and is also displayed in the transcription
                                                panel.

Transcription in Progress

The “Transcription in Progress” text gets displayed in the reading pane of the email.

The attachment “Transcription_pending.txt” indicates the progress of transcription.

The attachment “Transcription_pending.txt” indicates the progress of transcription and the text “Transcription in Progress” is also displayed in transcription panel.

When a sender sends a voicemail to Unity Connection through third party email clients, the receiver can view the voicemail
                                          through various clients after synchronizing the transcription of voicemails.

Do the following steps to synchronize the new voicemails between Unity Connection and mailboxes for a unified messaging user
                                    with SpeechView transcription service:

Navigate to Cisco Personal Communications Assistant and select Messaging Assistant .

In the Messaging Assistant tab, select Personal Options and enable the Hold till transcription received option.

The Hold till transcription received option enables the synchronization of voicemail between Unity Connection and mail server only when Unity Connection receives
                                          time-out/ failure transcription response from the third party external service.

#### Transcription of
                              	 Voicemails in Secure and Private Messages

Secure Messages : The secure messages are stored only on
                                       			 the Unity Connection server. Secure messages are transcribed only if the user
                                       			 belongs to a class of service for which the Allow Transcriptions of Secure Messages option are enabled.
                                       			 This option, however, does not allow the synchronization of transcribed secure
                                       			 messages on the Exchange server integrated with the Unity Connection server.

Private Messages : The transcription of private messages
                                       			 is not supported.

### Synchronization with Outlook Folders

The voicemails of a user are visible in the Outlook Inbox folder. Unity Connection synchronizes voicemails in the following
                              Outlook folders with the Unity Connection Inbox folder for the user:

Subfolders under the Outlook Inbox folder

Subfolders under the Outlook Deleted Items folder

The Outlook Junk Email folder

Messages in the Outlook Deleted Items folder appear in the Unity Connection Deleted Items folder. If the user moves voicemails
                              (except secure voicemails) into Outlook folders that are not under the Inbox folder, the messages are moved to the deleted
                              items folder in Unity Connection. However, the messages can still be played using ViewMail for Outlook because a copy of the
                              message still exists in the Outlook folder. If the user moves the messages back into the Outlook Inbox folder or into an Outlook
                              folder that is synchronized with the Unity Connection Inbox folder, and:

If the message is in the deleted items folder in Unity Connection, the message is synchronized back into the Unity Connection
                                    Inbox for that user.

If the message is not in the deleted items folder in Unity Connection, the message is still playable in Outlook but not resynchronized
                                    into Unity Connection.

Unity Connection synchronizes voicemails in the Sent Items folder of Outlook with the Exchange/ Office 365 Sent Items folder
                              for the user. However, the changes to the subject line, the priority, and the status (for example, from unread to read) are
                              replicated from Unity Connection to Exchange/ Office 365 only on an hourly basis.When a user sends a voicemail from Unity
                              Connection to Exchange/ Office 365 or vice versa, the voicemail in the Unity Connection Sent Items folder remains unread and
                              the voicemail in the Exchange/ Office 365 Sent Items folder is marked as read.

By default, the synchronization of voicemails in the Exchange/ Office 365 Sent Items folder with the Unity Connection Sent
                              Items folder is not enabled.

#### Enabling the Sent
                              	 Items Folder Synchronization

Secure voicemails behave differently. When Unity Connection
                                    		  replicates a secure voicemail to Exchange/ Office 365 mailbox, it replicates
                                    		  only a decoy message that briefly explains secure messages; only a copy of the
                                    		  voicemail remains on the Unity Connection server. When a user plays a secure
                                    		  message using ViewMail for Outlook, ViewMail retrieves the message from the
                                    		  Unity Connection server and plays it without ever storing the message in
                                    		  Exchange/ Office 365 or on the computer of the user.

If a user moves a secure message to an Outlook folder that is
                                    		  not synchronized with the Unity Connection Inbox folder, only the copy of the
                                    		  voicemail is moved to the Deleted Items folder in Unity Connection. Such secure
                                    		  messages cannot be played in Outlook. If the user moves the message back into
                                    		  the Outlook Inbox folder or into an Outlook folder that is synchronized with
                                    		  the Unity Connection Inbox folder, and:

If the message exists in the Deleted items folder in Unity
                                          				Connection, the message is synchronized back into the Unity Connection Inbox of
                                          				the user and the message becomes playable again in Outlook.

If the message does not exisit in the Deleted items folder in
                                          				Unity Connection, the message is not resynchronized into Unity Connection and
                                          				can no longer be played in Outlook.

Step 1

In Cisco Unity Connection Administration, expand System Settings
                                             			 > Advanced, select Messaging.

Step 2

On the Messaging Configuration page, enter a value greater than
                                             			 zero in the Sent Messages: Retention Period (in Days) field.

Step 3

Select Save.

When a user sends the voicemail to the Exchange/ Office 365
                                                            				  voice mailbox, the voicemail is not synchronized with the Sent Items folder in
                                                            				  Exchange/ Office 365 server. The voicemail remains in the Unity Connection Sent
                                                            				  Items folder.

### Working of Message Routing Using SMTP Domain Name

Unity Connection uses SMTP domain name to route messages between digitally networked Unity Connection servers and to construct
                              the SMTP address of the sender on outgoing SMTP messages. For each user, Unity Connection creates an SMTP address of <Alias>@<SMTP
                              Domain>. This SMTP address is displayed on the Edit User Basics page for the user. Examples of outgoing SMTP messages that
                              use this address format include messages sent by users on this server to recipients on other digitally networked Unity Connection
                              servers and messages that are sent from the Unity Connection phone interface or Messaging Inbox and relayed to an external
                              server based on the Message Actions setting of the recipient.

Unity Connection also uses the SMTP Domain to create sender VPIM addresses on outgoing VPIM messages, and to construct the
                              From address for notifications that are sent to SMTP notification devices.

When Unity Connection is first installed, the SMTP Domain is automatically set to the fully qualified host name of the server.

Make sure that the SMTP domain of Unity Connection is different from the Corporate Email domain to avoid issues in message
                              routing for Unity Connection.

Some scenarios in which you may encounter issues with the same domain are listed below:

Routing of the voice messages between digitally networked Unity Connection servers.

Relaying of the messages.

Replying and Forwarding of the voice messages using ViewMail for Outlook.

Routing of the SpeechView messages to Cisco Unity Connection server.

Sending the SMTP message Notifications.

Routing of the VPIM messages.

Unity Connection requires a unique SMTP domain for every user, which is different from the corporate email domain. Due to
                                          same domain name configuration on Microsoft Exchange and Unity Connection, the users who are configured for Unified Messaging
                                          may face issues in adding recipient while composing, replying and forwarding of messages.For more information on resolving
                                          domain name configuration issues, see the Resolving SMTP Domain Name Configuration Issues section

### Location for Deleted Messages

By default, when a user deletes a voicemail in Unity Connection, the message is sent to the Unity Connection deleted items
                              folder and synchronized with the Outlook Deleted Items folder. When the message is deleted from the Unity Connection Deleted
                              Items folder (you can either do this manually or configure message aging to do it automatically), it is also deleted from
                              the Outlook Deleted Items folder.

When a user deletes a voicemail from any Outlook folder, the message is not permanently deleted but it is moved to the Deleted
                              Items folder. No operation in Outlook causes a message to be permanently deleted in Unity Connection.

To permanently delete messages using Web Inbox or Unity Connection phone interface, you must configure Unity Connection to
                              permanently delete messages without saving them in the Deleted Items folder.

When Unity Connection synchronizes with Exchange/ Office 365, the message is moved to the Unity Connection Deleted items folder
                              but not permanently deleted.

We can also permanently delete messages from the Unity Connection Deleted Items folder using Web Inbox.

To permanently delete messages from the Unity Connection Deleted Items folder, do either or both of the following steps:

Configure message aging to permanently delete messages in the Unity Connection Deleted Items folder.

Configure message quotas so that Unity Connection prompts users to delete messages when their mailboxes approach a specified
                                    size.

### Types of Messages Not Synchronized with Exchange/ Office 365

The following types of Unity Connection messages are not synchronized:

Draft messages

Messages configured for future delivery but not yet delivered

Broadcast messages

Unaccepted dispatch messages

When a dispatch message is accepted by a recipient, it becomes a normal message and is synchronized with Exchange/ Office
                                                365 for the user who accepted it and deleted for all other recipients. Until someone in the distribution list accepts a dispatch
                                                message, the message waiting indicator for everyone in the distribution list remains on, even when users have no other unread
                                                messages.

### Affect of Disabling and Re-enabling Single Inbox

When you configure unified messaging, you can create one or more unified messaging services. Each unified messaging service
                              has a set of specific unified messaging features enabled. You can create only one unified messaging account for each user
                              and associate it with a unified messaging service.

Single inbox can be disabled in the following three ways:

Entirely disable a unified messaging service in which single inbox is enabled. This disables all enabled unified messaging
                                    features (including single inbox) for all users that are associated with the service.

Disable only the single inbox feature for a unified messaging service, which disables only the single inbox feature for all
                                    users that are associated with that service.

Disable single inbox for a unified messaging account, which disables single inbox only for the associated user.

If you disable and later re-enable single inbox using any of these methods, Unity Connection resynchronizes the Unity Connection
                              and Exchange/ Office 365 mailboxes for the affected users. Note the following:

If users delete messages in Exchange/ Office 365 but do not delete the corresponding messages in Unity Connection while single
                                    inbox is disabled, the messages gets resynchronized into the Exchange mailbox when single inbox is re-enabled.

If messages are hard deleted from Exchange/ Office 365 (deleted from the Deleted Items folder) before single inbox is disabled,
                                    the corresponding messages that are still in the deleted items folder in Unity Connection when single inbox is re-enabled
                                    are resynchronized into the Exchange/ Office 365 Deleted Items folder.

If users hard delete the messages in Unity Connection but do not delete the corresponding messages in Exchange/ Office 365
                                    while single inbox is disabled, the messages remain in Exchange/ Office 365 when single inbox is re-enabled. Users must delete
                                    the messages from Exchange/ Office 365 manually.

If users change the status of messages in Exchange/ Office 365 (for example, from unread to read) while single inbox is disabled,
                                    the status of Exchange/ Office 365 messages is changed to the current status of the corresponding Unity Connection messages
                                    when single inbox is re-enabled.

When you re-enable single inbox, depending on the number of users associated with the service and the size of their Unity
                                    Connection and Exchange/ Office 365 mailboxes, resynchronization for existing messages may affect synchronization performance
                                    for new messages.

When you re-enable single inbox, depending on the number of users associated with the service and the size of their Unity
                                    Connection and Exchange/ Office 365 mailboxes, resynchronization for existing messages may affect synchronization performance
                                    for new messages.

### Synchronization of
                           	 Read/Heard Receipts, Delivery Receipts, and Non-delivery Receipts

Unity Connection can send read/heardreceipts, delivery receipts,
                              		and non-delivery receipts to Unity Connection users who send voicemails. If the
                              		sender of a voicemail is configured for single inbox, the applicable receipt is
                              		sent to the Unity Connection mailbox of the sender. The receipt is then
                              		synchronized into the Exchange/ Office 365 mailbox of the sender.

Note the following.

Read/heard receipts: When sending a voicemail, a
                                    			 sender can request a read/heard receipt.

Do the following steps to prevent Unity Connection to respond to
                                    			 requests for read receipts:

In Unity Connection Administration, either expand Users and select Users , or expand Templates and select User Templates .

If you selected Users , then select an applicable user and open the Edit
                                          				  User Basics page. If you selected User Templates , then select an applicable template and
                                          				  open the Edit User Template Basics page.

On the Edit User Basics page or the Edit User Template Basics
                                          				  page, select Edit > Mailbox .

On the Edit Mailbox page, uncheck the Respond to Requests for
                                             					 Read Receipts check box.

Delivery receipts: A sender can request a delivery
                                    			 receipt only when sending a voicemail from ViewMail for Outlook. You cannot
                                    			 prevent Unity Connection from responding to a request for a delivery receipt.

Non-delivery receipts (NDR): A sender receives an NDR
                                    			 when a voicemail cannot be delivered.

Do the following steps to prevent Unity Connection to send an
                                    			 NDR when a message is not delivered:

In Unity Connection Administration, either expand Users and select Users , or expand Templates and select User Templates .

If you selected Users , then select an applicable user and open the Edit
                                          				  User Basics page. If you selected User Templates , then select an applicable template and
                                          				  open the Edit User Template Basics page.

On the Edit User Basics page or the Edit User Template Basics
                                          				  page, uncheck the Send Non-Delivery Receipts for Message Failed Delivery check box and select Save.

When the sender accesses Unity Connection using the TUI, the NDR
                                                				includes the original voicemail that allows the sender to resend the message at
                                                				a later time or to a different recipient.

When the sender accesses Unity Connection using Web Inbox, the
                                                				NDR includes the original voicemail but the sender cannot resend it.

When the sender uses ViewMail for Outlook to access Unity
                                                				Connection voicemails that have been synchronized into Exchange, the NDR is a
                                                				receipt that contains only an error code, not the original voicemail, so the
                                                				sender cannot resend the voicemail.

When the sender is an outside caller, NDRs are sent to Unity
                                                				Connection users on the Undeliverable Messages distribution list. Verify that
                                                				the Undeliverable Messages distribution list includes one or more users who
                                                				regularly monitors and reroutes undelivered messages.

## Single Inbox with Google Workspace

The synchronization of user messages between Unity Connection and Gmail mail server is known as Single Inbox. When the single
                           inbox feature is enabled on Unity Connection, voice mails are first delivered to the user mailbox in Unity Connection and
                           then the mails are replicated to the Gmail account of the user. For information on configuring the Single Inbox in Unity Connection,
                           refer Configuring Unified Messaging “Configuring Unified Messaging” chapter.

The single inbox feature with Google Workspace is supported with both IPv4 and IPv6 addresses.

- To see the maximum number of users supported for Google Workspace, see the section “ Specification for Virtual Platform Overlays” of the Cisco Unity Connection 14 Supported Platform List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html .

### Single Inbox with Gmail Client

If you do not install ViewMail for Outlook or use another email client to access Unity Connection voicemails in Exchange/
                              Office 365/Gmail server:

The Gmail client treats voicemails as emails with .wav file attachments.

When a user replies to or forwards a voicemail, the reply or forward also is treated as an email even if  the user attaches
                                    a .wav file. Message routing is handled by Gmail server, not by Unity Connection, so the message is never sent to the Unity
                                    Connection mailbox for the recipient.

Users cannot listen to secure voicemails.

It may be possible to forward private voicemails.

### Accessing Secure Voicemails

To play secure vocemails when Google Worspace is configured, users must use Telephony User Interface (TUI). The users accessing
                              secure voicemails on Gmail account see only text message which indicates that message is secured and can be listen through
                              TUI.

### Transcription of Voicemails Synchronized Between Unity Connection and Gmail Server

A system administrator can enable the single inbox transcription functionality by configuring the unified messaging services
                              and the SpeechView transcription services on Unity Connection. "Synchronization of multiple forward messages” service is not
                              supported with Unity Connection, if configured with Single Inbox.

For information on configuring unified messaging services in Unity Connection, refer chapter " Configuring Unified Messaging ". For information on configuring SpeechView transcription service, see the “ SpeechView ” chapter of the System Administration Guide for Cisco Unity Connection, Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

In Single Inbox, the transcription of voicemails is synchronized with Gmail server when sender sends voicemail to a user through
                              Web Inbox or touchtone conversation user interface and the user views voicemail through Gmail client, then the transcription
                              of voicemails are synchronized as below:

For successful delivery of voicemails, the text of the transcription gets displayed in the reading pane of the email.

For failure or response time-out, the “Failure or Response Timeout” text gets displayed in the reading pane of the email.

Do the following steps to synchronize the new voicemails between Unity Connection and Google Workspace mailboxes for a unified
                              messaging user with SpeechView transcription service:

Navigate to Cisco Personal Communications Assistant and select Messaging Assistant .

In the Messaging Assistant tab, select Personal Options and enable the Hold till transcription received option.

By default, the Hold till transcription received option is disabled.

The Hold till transcription received option enables the synchronization of voicemail between Unity Connection and Google Workspace only when Unity Connection
                                    receives response from the third party external service.

## Text-to-Speech

The Text-to-Speech feature allows the unified messaging users to
                           		listen to their emails when they sign in to Unity Connection using phone.

Unity Connection supports text-to-speech feature with the following mailbox stores:

Office 365

Exchange 2016

Exchange 2019

Unity Connection can be configured to deliver transcriptions to an SMS device as a text message or to an SMTP address as an
                           email message. The fields to turn on transcription delivery are located on the SMTP and SMS Notification Device pages where
                           you set up message notification. For more information on notification devices, see the “ Configuring Notification Devices ” section in the “Notifications” chapter of the System Administration Guide for Cisco Unity Connection, Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

Following are the considerations for effective use of
                           		transcription delivery:

In the From field, enter the number you dial to reach Unity Connection when you are not
                                 			 dialing from the desk phone. If you have a text-compatible mobile phone, can
                                 			 initiate a callback to Unity Connection in the event that you want to listen to
                                 			 the message.

You must check the Include
                                    				Message Information in Message Text check box to include call information,
                                 			 such as caller name, caller ID (if available), and the time that the message
                                 			 was received. If the check box is unchecked, the message received does not
                                 			 indicate the call information.

In addition, if you have a text-compatible mobile phone, you can
                           		initiate a callback when the caller ID is included with the transcription.

In the Notify Me
                                    				Of section, if you turn on notification for voice or dispatch messages, you
                                 			 are notified when a message arrives and the transcription soon follows. If you
                                 			 do not want notification before the transcription arrives, do not select the
                                 			 voice or dispatch message options.

Email messages that contain transcriptions have a subject line
                                 			 that is identical to notification messages. So, if you have notification for
                                 			 voice or dispatch messages turned on, you have to open the messages to
                                 			 determine which one contains the transcription.

## Calendar and Contact Integration

For information on configuring calendar and contact integration in Unity Connection, see the Configuring Calendar and Contact Integration chapter.

### About Calendar
                           	 Integration

The calendar integration feature enables the unified messaging
                              		users to do the following tasks over phone:

Hear a list of upcoming meetings (Outlook meetings only).

Hear a list of the participants for a meeting.

Send a message to the meeting organizer.

Send a message to the meeting participants.

Accept or decline meeting invitations (Outlook meetings only).

Cancel a meeting (meeting organizers only).

Unity Connection supports calendar applications when integrated with the following mail servers:

Office 365

Exchange 2016

Exchange 2019

For listing, joining, and scheduling meetings, see the “ Cisco Unity Connection Phone Menus and Voice Commands ” chapter of the User Guide for the Cisco Unity Connection Phone Interface, Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/phone/b_14cucugphone.html .

For using Personal Call Transfer Rules, see the User Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool, Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/pctr/b_14cucugpctr.html .

### About Contact
                           	 Integrations

Unity Connection allows users to import Exchange contacts and
                              		use the contact information in Personal Call Transfer Rules and when placing
                              		outgoing calls using voice commands. Unity Connection supports contact
                              		applications when integrated with the following mail servers:

Office 365

Exchange 2016

Exchange 2019

For importing Exchange contacts, see the “ Managing Your Contacts ” chapter of the User Guide for the Cisco Unity Connection Messaging Assistant Web Tool, Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/assistant/b_14cucugasst.html .

| Note | The single inbox feature is supported with both IPv4 and IPv6 addresses. When the single inbox feature is enabled for a user, the Outlook rules may not work for single inbox messages. To see the maximum number of users supported for Exchange and Office 365 server, see the section “ Specification for Virtual Platform Overlays” of the Cisco Unity Connection 14 Supported Platform List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html . |
|---|---|

| Note | Private messages
                                       		cannot be forwarded. |
|---|---|

| Scenarios | Web Inbox | Outlook WebMail Access/ Outlook without VMO | ViewMail for Outlook |
|---|---|---|---|
| Successful delivery of voicemails | The text of the transcription gets displayed in the reading pane of the email. | The text of transcription gets displayed in the reading pane of the email. | The text of the transcription gets displayed in the reading pane of the email and is also displayed in the transcription panel. |
| Failure or Response Time-out | The “Failure or Response Timeout” text gets displayed in the reading pane of the email. | The “Failure or Response Timeout” text gets displayed in the reading pane of the email. | The “Failure or Response Timeout” text gets displayed in the reading pane of the email and is also displayed in the transcription panel. |
| Transcription in Progress | The “Transcription in Progress” text gets displayed in the reading pane of the email. | The reading pane of the email is blank .text. | The “Transcription in Progress” text gets displayed in the transcription panel. |

| Scenarios | Web Inbox | Outlook WebMail Access/ Outlook without VMO | ViewMail for Outlook |
|---|---|---|---|
| Successful delivery of voicemails | The text of transcription gets displayed in the reading pane of the email. | The text of the transcription is the part of transcript file “Transcription.txt”. | The text of the transcription is the part of transcript file “Transcription.txt” and is also displayed in the transcription
                                                panel. |
| Failure or Response Time-out | The “Failure or Response Timeout” text gets displayed in the reading pane of the email. | The “Failure or Response Time-out” text is the part of transcript file “Trancription.txt” attached in the voicemail. | The “Failure or Response Time-out” text is the part of transcript file “Trancription.txt” attached in the voicemail and is also displayed in the transcription
                                                panel. |
| Transcription in Progress | The “Transcription in Progress” text gets displayed in the reading pane of the email. | The attachment “Transcription_pending.txt” indicates the progress of transcription. | The attachment “Transcription_pending.txt” indicates the progress of transcription and the text “Transcription in Progress” is also displayed in transcription panel. |

| Note | The message body of the voicemails composed using ViewMail for Outlook and received by Unity Connection are either blank or
                                             contain text. |
|---|---|

| Note | By default, the Hold till transcription received option is disabled for Exchange/Office 365. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand System Settings
                                             			 > Advanced, select Messaging. |
|---|---|
| Step 2 | On the Messaging Configuration page, enter a value greater than
                                             			 zero in the Sent Messages: Retention Period (in Days) field. |
| Step 3 | Select Save. Note When a user sends the voicemail to the Exchange/ Office 365
                                                            				  voice mailbox, the voicemail is not synchronized with the Sent Items folder in
                                                            				  Exchange/ Office 365 server. The voicemail remains in the Unity Connection Sent
                                                            				  Items folder. | Note | When a user sends the voicemail to the Exchange/ Office 365
                                                            				  voice mailbox, the voicemail is not synchronized with the Sent Items folder in
                                                            				  Exchange/ Office 365 server. The voicemail remains in the Unity Connection Sent
                                                            				  Items folder. |
| Note | When a user sends the voicemail to the Exchange/ Office 365
                                                            				  voice mailbox, the voicemail is not synchronized with the Sent Items folder in
                                                            				  Exchange/ Office 365 server. The voicemail remains in the Unity Connection Sent
                                                            				  Items folder. |

| Note | When a user sends the voicemail to the Exchange/ Office 365
                                                            				  voice mailbox, the voicemail is not synchronized with the Sent Items folder in
                                                            				  Exchange/ Office 365 server. The voicemail remains in the Unity Connection Sent
                                                            				  Items folder. |
|---|---|

| Note | Unity Connection requires a unique SMTP domain for every user, which is different from the corporate email domain. Due to
                                          same domain name configuration on Microsoft Exchange and Unity Connection, the users who are configured for Unified Messaging
                                          may face issues in adding recipient while composing, replying and forwarding of messages.For more information on resolving
                                          domain name configuration issues, see the Resolving SMTP Domain Name Configuration Issues section |
|---|---|

| Note | We can also permanently delete messages from the Unity Connection Deleted Items folder using Web Inbox. |
|---|---|

| Note | When a dispatch message is accepted by a recipient, it becomes a normal message and is synchronized with Exchange/ Office
                                                365 for the user who accepted it and deleted for all other recipients. Until someone in the distribution list accepts a dispatch
                                                message, the message waiting indicator for everyone in the distribution list remains on, even when users have no other unread
                                                messages. |
|---|---|

| Note | When the sender accesses Unity Connection using the TUI, the NDR
                                                				includes the original voicemail that allows the sender to resend the message at
                                                				a later time or to a different recipient. When the sender accesses Unity Connection using Web Inbox, the
                                                				NDR includes the original voicemail but the sender cannot resend it. When the sender uses ViewMail for Outlook to access Unity
                                                				Connection voicemails that have been synchronized into Exchange, the NDR is a
                                                				receipt that contains only an error code, not the original voicemail, so the
                                                				sender cannot resend the voicemail. When the sender is an outside caller, NDRs are sent to Unity
                                                				Connection users on the Undeliverable Messages distribution list. Verify that
                                                				the Undeliverable Messages distribution list includes one or more users who
                                                				regularly monitors and reroutes undelivered messages. |
|---|---|

| Note | The single inbox feature with Google Workspace is supported with both IPv4 and IPv6 addresses. To see the maximum number of users supported for Google Workspace, see the section “ Specification for Virtual Platform Overlays” of the Cisco Unity Connection 14 Supported Platform List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html . |
|---|---|

| Note | By default, the Hold till transcription received option is disabled. |
|---|---|

| Note | Text-to-Speech over Office 365, Exchange 2016, Exchange 2019 supports both the IPv4 and IPv6 addresses. However, the IPv6
                                    address works only when Unity Connection platform is compatible and configured in dual (IPv4/IPv6) mode. |
|---|---|

| Note | For information on configuring the text-to-speech feature in Unity Connection, see the Configuring Text-to-Speech chapter. |
|---|---|

| Note | For information on configuring calendar and contact integration in Unity Connection, see the Configuring Calendar and Contact Integration chapter. |
|---|---|