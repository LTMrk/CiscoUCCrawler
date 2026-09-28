---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-user-setup-guide-b-14cucuwsx-b-14cucuwsx-chapter-0100-html-e8ecff0f5e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user_setup/guide/b_14cucuwsx/b_14cucuwsx_chapter_0100.html
retrieved_at: 2026-08-17T03:38:53.726737+00:00
---

User Workstation Setup Guide for Cisco Unity Connection Release 14

# User Workstation Setup Guide for Cisco Unity Connection Release 14

Updated: March 31, 2021

Chapter: Operator and Support Desk Orientation

## Chapter: Operator and Support Desk Orientation

# Operator and Support Desk Orientation

## Operator and Support Desk Orientation

### Overview

Operators in your organization need information about Cisco Unity Connection that is specific to your installation. In addition,
                              if your organization has a support desk, the staff need to be prepared to answer the questions that users may ask, and to
                              be aware of the resources that are available to assist them in answering user questions.

### Operator
                           	 Orientation

Operator orientation should address the same points as
                              		user orientation, but in greater detail. Operators must be familiar with how
                              		users use Unity Connection. Depending on the size of your organization, the
                              		operator may be the person users are likely to ask when they have questions
                              		about Unity Connection.

In addition to the information in the User
                                 		  Orientation chapter and the “Support
                                 		  Desk Orientation” (as applicable), operators also need to understand the
                              		following concepts and tasks.

Roles of the Operator and
                                 		  the Automated Attendant

The way your organization uses the automated attendant
                              		determines what the operator responsibilities are. The automated attendant is a
                              		call handler that is used in place of a human operator to answer and direct
                              		calls by playing greetings and responding to caller input. The automated
                              		attendant can provide a menu of options (for example, “For Sales, press 1; for
                              		Service, press 2.”), and it can also provide information (for example, “Our
                              		normal business hours are Monday through Friday, 8 a.m. to 5 p.m.”).

Directing Calls

Regardless of how your organization uses the automated
                              		attendant, many calls go to the operator. The operator must know how to direct
                              		calls to voicemail and to user phones. With Cisco Unified Communications
                              		Manager, you can program the phone to direct calls to voicemail. For details on
                              		setting this up, see the tech note How to Transfer a Caller Directly into a Cisco Unity
                                 		  Mailbox , available at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_tech_notes_list.html .

Forwarding Messages to
                                 		  Intended Recipients

If an operator also owns a call handler or system distribution
                              		list, make sure that the operator knows to review messages frequently, and to
                              		forward messages as necessary to the applicable recipients.

Using the Cisco Unity
                                 		  Greetings Administrator

An operator who is responsible for changing call handler
                              		greetings for the organization can use the Cisco Unity Greetings Administrator
                              		when it is not practical to change a greeting in Cisco Unity Connection
                              		Administration. For example, if the office is unexpectedly closed because of
                              		bad weather, the operator can call from home to use the Cisco Unity Greetings
                              		Administrator to enable the alternate Opening Greeting, or to rerecord a call
                              		handler greeting stating that the office is closed.

Using the Cisco Unity
                                 		  Broadcast Message Administrator

If an operator is responsible for sending recorded announcements
                              		to everyone in an organization (or to particular locations within an
                              		organization), explain how to access and use the Cisco Unity Broadcast Message
                              		Administrator to send broadcast messages.

### Support Desk
                           	 Orientation

Support desk orientation
                              		should address the same points as user and operator orientation, but in greater
                              		detail. Support desk staff must be familiar with how users and operators use
                              		Unity Connection, and the common problems that users may encounter when using
                              		Unity Connection. Instead of using the Unity Connection server, it may be
                              		helpful to set up a test server that support desk staff can use to browse to
                              		Cisco Unity Connection Administration, and troubleshoot and test client
                              		applications.

To prepare for possible calls to the support desk at your
                              		organization, familiarize the support desk staff with the resources listed in
                              		the following “Support Desk Resources” section, and with the potential user concerns and misconceptions listed in the “Potential User Concerns and
                                 		  Misconceptions” section . (See also the “Operator Orientation”
                                 		  section and the “User Orientation” chapter.)

#### Support Desk
                              	 Resources

User documentation is available
                                       			 at http://www.cisco.com/en/US/products/ps6509/products_user_guide_list.html .

The
                                       			 Compatibility Matrix: Cisco Unity Connection and the Software on User
                                       			 Workstations is available at http://www.cisco.com/en/US/products/ps6509/products_device_support_tables_list.html .

The following chapters in this guide provide information on how
                                       			 user workstations should be set up, and describes how users use Unity
                                       			 Connection client applications:

Setting
                                                					 Up Access to Cisco Peronal Communications Assistant

Setting
                                                					 Up Playback and Recording Devices for the Media Master

Configuring
                                                					 an Email Account to Acess Unity Connection Voice Messages

The Troubleshooting Guide for Cisco Unity Connection Release 14 is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg.html .

For descriptions and the URLs of all Unity Connection documentation on Cisco.com, see the Documentation Guide for Cisco Unity
                                       Connection Release 14 . The document is shipped with Unity Connection and is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/roadmap/b_14cucdg.html .

#### Potential User
                              	 Concerns and Misconceptions

Table 5-1 describes potential user issues, which are typically based on misconceptions
                                 		about how Cisco Unity Connection works. Users who encounter such issues are
                                 		often those who are accustomed to another voice messaging system, have not yet
                                 		completed Unity Connection training, or are unaware of a new feature or
                                 		functionality change to an existing system.

Potential Issue

Description

Delayed messages

Users may believe that their messages are delayed for the
                                             				  following reasons:

While listening to new messages, users may skip a message and
                                                   						inadvertently mark it new. Later, when they check messages again, they hear the
                                                   						skipped message and believe that the message arrived after a delay.

Users may skip more messages than they intend while listening to
                                                   						their messages, and later check messages again only to hear one or more of the
                                                   						skipped messages, and believe that the messages arrived after a delay.

While listening to messages, other new messages arrive that
                                                   						users may not be aware of. Later, when they check messages again, they hear the
                                                   						new messages and believe that they were delayed.

Deleted messages

By default, when users delete a new or saved message, Unity
                                             				  Connection does not ask them to confirm the deletion. You may want to enable
                                             				  Unity Connection to request confirmation from users before proceeding with the
                                             				  deletion, especially if many users do not belong to a class of service that
                                             				  allows them to retain and review their deleted messages. You can set up Unity
                                             				  Connection to confirm deletion of messages on the System Settings > Advanced
                                             				  > Conversations page in Cisco Unity Connection Administration.

For information on deleted messages, see the “ Managing Deleting Messages ” chapter of the User Guide for the Cisco Unity Connection Phone Interface (Release 14) , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/phone/b_14cucugphone.html .

Deleted messages: IMAP and MAPI behavior

When users access messages stored on a Microsoft Exchange server
                                             				  both from a Microsoft Outlook client and from Unity Connection, they may
                                             				  experience unexpected and confusing behavior when deleting messages. The
                                             				  difference in behavior occurs when the Microsoft Outlook client is configured
                                             				  to use MAPI, the Microsoft interface for connecting to Exchange, and stems from
                                             				  the fact that MAPI and IMAP—the protocol used by Unity Connection—use different
                                             				  mechanisms for marking messages as deleted.

If you have users who access a Microsoft Exchange server using
                                             				  Outlook (with MAPI) or Outlook Web Access, and who also use Unity Connection to
                                             				  manage messages on the same message store, be sure to alert them to this
                                             				  behavior.

Deleted Messages—IMAP
                                                					 Behavior

When a user deletes a message from Microsoft Outlook, the
                                             				  message is moved from the Inbox to the Deleted Items folder. At this point,
                                             				  Unity Connection can no longer access the message, and no longer indicates that
                                             				  the message exists either as a new, saved, or deleted message.

Deleted Messages—MAPI
                                                					 Behavior

When a user deletes a message from Unity Connection, the message
                                             				  remains in the Inbox but is flagged to indicate that it has been marked deleted
                                             				  by the user. However, when configured to use MAPI, Microsoft Outlook does not
                                             				  recognize this flag as a deletion, and continues to display the message as a
                                             				  new or saved message in the Inbox.

Device for recording or playback does not show in ViewMail for
                                             				  Outlook device lists

When users add or turn on a new recording or playback device,
                                             				  they must restart the ViewMail for Outlook add-in so it can recognize the new
                                             				  device. To restart ViewMail, restart Outlook.

Directory listing: users are not listed as
                                             				  expected

When users do not have a recorded name, they are not listed in
                                             				  the corporate directory and as a result, outside callers are not be able to
                                             				  find them when searching for them by name. By default, Unity Connection prompts
                                             				  users to record a name during first-time enrollment, but it does not prevent
                                             				  them from completing the enrollment process if they do not.

To address this issue, consider the following options:

You can change whether recording a name is required to complete
                                                   						first-time enrollment on the System Settings > Advanced > Conversations
                                                   						page in Cisco Unity Connection Administration.

You can provide recorded names for users in Cisco Unity
                                                   						Connection Administration.

Users with class of service rights can record their own names
                                                   						using the Unity Connection conversation or the Unity Connection Messaging
                                                   						Assistant.

Fax: attached files are not delivered to fax machines

(fax integrations only)

Users may be unaware that when they add attachments to an email
                                             				  message and then send the message to a fax machine, Unity Connection renders
                                             				  only those attachments with the file extensions specified during Unity
                                             				  Connection setup. All other attachments are removed.

IMAP client: Differences in client behavior

Users who use different third-party IMAP clients to access voice
                                             				  messages from their desktop machines may note the following discrepancies in
                                             				  behavior:

Microsoft Outlook client:

For new messages, the “Mark
                                                         							 as Unread” feature marks messages as new on the Unity Connection server,
                                                         							 regardless of whether the WAV file message attachment is downloaded or not.

Voice messages that are
                                                         							 deleted by phone are marked for deletion in the Outlook client and are changed
                                                         							 to strikethrough text when users select the “Send/Receive” command.

Novell GroupWise client:

When new messages with the
                                                         							 WAV file message attachment have been downloaded to the GroupWise client, the
                                                         							 “Read Later” feature no longer marks the message as new on the Unity Connection
                                                         							 server.

Voice messages that are
                                                         							 deleted by phone are not marked for deletion in GroupWise; users need to
                                                         							 manually delete them from this client.

GroupWise users need to use
                                                         							 the “Send/Retrieve” command to update message status from the Unity Connection
                                                         							 server.

Mailbox fills up quickly

Users may complain that their mailboxes are filling up too
                                             				  quickly, for any of the following reasons:

Unity Connection does not automatically delete messages when they reach a certain age. This means that user messages are saved
                                                   until the user deletes them permanently. (For information on how to permanently delete messages, see the “ Managing the Size of Your Mailbox ” chapter of the User Guide for the Cisco Unity Connection Phone Interface (Release 14), available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/phone/b_14cucugphone.html ).

When users receive nondelivery receipts (NDRs) to messages that
                                                   						they send, their email client mailbox can quickly increase in size—especially
                                                   						if the original message included large attachments. For users who have access
                                                   						to email messages via TTS, if their email clients are configured to save their
                                                   						sent messages, the original message and attachments are stored in their Sent
                                                   						Items folders and another copy is sent to their Inboxes along with the NDR,
                                                   						increasing their mailbox size accordingly.

Users may receive messages that have been forwarded many times
                                                   						over, which increases message size. The original message plus all recorded
                                                   						introductions that were added during forwarding equal the total message size.
                                                   						As a result, users who have relatively few messages stored in their mailboxes
                                                   						may still find that their mailboxes exceed the storage limits.

User mailboxes can fill up while users are on vacation or on an
                                                   						extended leave of absence. To prevent this, specify that Unity Connection
                                                   						prevents callers from leaving messages when users have their alternate
                                                   						greetings enabled.

Message notification: repeat notification
                                             				  options

When a user chooses not to have Unity Connection restart
                                             				  notification each time a new message arrives, setting a long interval between
                                             				  repeat notification calls may lead the user to believe that Unity Connection is
                                             				  delaying notification.

Media Master: opening a file that is saved on a
                                             				  workstation

When a user attempts to use a previously recorded WAV file (for
                                             				  example, an announcement that was recorded earlier) rather than recording using
                                             				  a phone or a computer microphone, the Media Master may display an error
                                             				  message. The error occurs when the WAV file was recorded in the G.729a audio
                                             				  format. To resolve the problem, the user must do one of the following:

Convert the WAV file to another audio format (for example,
                                                   						convert it to the G.711 audio format).

Use a WAV file that is recorded in a supported audio format
                                                   						other than G.729a.

Make the recording using a phone or a computer microphone.

MWIs

To gain an understanding of when MWIs turn on and off, what causes them to turn on and off, and what causes MWIs to behave
                                             differently than expected, see the “ Troubleshooting the Message Waiting Indicators (MWIs) ” chapter of the Troubleshooting Guide for Cisco Unity Connection, Release 14 , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg.html .

Passwords and PINs are not secure, or users use the
                                             				  wrong password or PIN

Users may assume that their phone PINs and Cisco Personal
                                             				  Communications Assistant (PCA) passwords are the same or are synchronized. As a
                                             				  result, they may think that they are changing both PIN and password when Unity
                                             				  Connection prompts them to change their phone PIN during first-time enrollment.
                                             				  Additionally, they may try to use their phone PIN to sign in to the Cisco PCA.

Speed for elements of the Unity Connection
                                             				  conversation varies

Users may report that the speed at which Unity Connection plays
                                             				  menus, recorded names, greetings, and messages is inconsistent. For example,
                                             				  users may report that when they listen to their messages, the message is played
                                             				  at a different speed than the recorded names of users who leave them messages
                                             				  and the message properties (for example, the time stamp and message number).

Such inconsistencies are expected when you consider the
                                             				  following:

Unity Connection plays recorded names and greetings at the speed
                                                   						at which they were recorded. Neither you nor users can affect the playback
                                                   						speed of recorded names and greetings.

Messages played via Text to Speech (TTS) are always played at
                                                   						normal speed by default, regardless of message playback settings.

The speed that you or a user specifies for system prompts—the
                                                   						standard recordings that come with the Unity Connection system, including
                                                   						prompts for message properties—does not affect the playback speed of messages.

The speed that users specify for message playback does not
                                                   						affect system prompts.

Unread messages

Depending on how Unity Connection is set up at your
                                             				  organization, users may be surprised at how Unity Connection handles messages
                                             				  when calls are intentionally or unintentionally disconnected (for example, when
                                             				  a user hangs up or when a mobile phone loses its charge or signal) while users
                                             				  are in the process of listening to new messages. Some users may incorrectly
                                             				  assume that Unity Connection marks the message as read, which is not the case.

You can change how Unity Connection handles unread messages when
                                             				  calls are disconnected by adjusting the Mark Message Saved If User Hangs Up
                                             				  setting on the System Settings > Advanced > Conversations page of
                                             				  Cisco Unity Connection Administration.

Unsent messages

Depending on how Unity Connection is set up at your
                                             				  organization, users may be surprised at how Unity Connection handles messages
                                             				  when calls are intentionally or unintentionally disconnected (for example, when
                                             				  a user hangs up or when a mobile phone loses its charge or signal) while users
                                             				  are in the process of sending, replying to, or forwarding a message. Some users
                                             				  may incorrectly assume that Unity Connection offers a draft folder for unsent
                                             				  messages, which is not the case.

You can change how Unity Connection handles unsent messages when
                                             				  calls are disconnected by adjusting the Send Message If User Hangs Up During
                                             				  Recording setting on the System Settings > Advanced > Conversations page
                                             				  of Cisco Unity Connection Administration.

| Potential Issue | Description |
|---|---|
| Delayed messages | Users may believe that their messages are delayed for the
                                             				  following reasons: While listening to new messages, users may skip a message and
                                                   						inadvertently mark it new. Later, when they check messages again, they hear the
                                                   						skipped message and believe that the message arrived after a delay. Users may skip more messages than they intend while listening to
                                                   						their messages, and later check messages again only to hear one or more of the
                                                   						skipped messages, and believe that the messages arrived after a delay. While listening to messages, other new messages arrive that
                                                   						users may not be aware of. Later, when they check messages again, they hear the
                                                   						new messages and believe that they were delayed. |
| Deleted messages | By default, when users delete a new or saved message, Unity
                                             				  Connection does not ask them to confirm the deletion. You may want to enable
                                             				  Unity Connection to request confirmation from users before proceeding with the
                                             				  deletion, especially if many users do not belong to a class of service that
                                             				  allows them to retain and review their deleted messages. You can set up Unity
                                             				  Connection to confirm deletion of messages on the System Settings > Advanced
                                             				  > Conversations page in Cisco Unity Connection Administration. For information on deleted messages, see the “ Managing Deleting Messages ” chapter of the User Guide for the Cisco Unity Connection Phone Interface (Release 14) , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/phone/b_14cucugphone.html . |
| Deleted messages: IMAP and MAPI behavior | When users access messages stored on a Microsoft Exchange server
                                             				  both from a Microsoft Outlook client and from Unity Connection, they may
                                             				  experience unexpected and confusing behavior when deleting messages. The
                                             				  difference in behavior occurs when the Microsoft Outlook client is configured
                                             				  to use MAPI, the Microsoft interface for connecting to Exchange, and stems from
                                             				  the fact that MAPI and IMAP—the protocol used by Unity Connection—use different
                                             				  mechanisms for marking messages as deleted. If you have users who access a Microsoft Exchange server using
                                             				  Outlook (with MAPI) or Outlook Web Access, and who also use Unity Connection to
                                             				  manage messages on the same message store, be sure to alert them to this
                                             				  behavior. Deleted Messages—IMAP
                                                					 Behavior When a user deletes a message from Microsoft Outlook, the
                                             				  message is moved from the Inbox to the Deleted Items folder. At this point,
                                             				  Unity Connection can no longer access the message, and no longer indicates that
                                             				  the message exists either as a new, saved, or deleted message. Deleted Messages—MAPI
                                                					 Behavior When a user deletes a message from Unity Connection, the message
                                             				  remains in the Inbox but is flagged to indicate that it has been marked deleted
                                             				  by the user. However, when configured to use MAPI, Microsoft Outlook does not
                                             				  recognize this flag as a deletion, and continues to display the message as a
                                             				  new or saved message in the Inbox. |
| Device for recording or playback does not show in ViewMail for
                                             				  Outlook device lists | When users add or turn on a new recording or playback device,
                                             				  they must restart the ViewMail for Outlook add-in so it can recognize the new
                                             				  device. To restart ViewMail, restart Outlook. |
| Directory listing: users are not listed as
                                             				  expected | When users do not have a recorded name, they are not listed in
                                             				  the corporate directory and as a result, outside callers are not be able to
                                             				  find them when searching for them by name. By default, Unity Connection prompts
                                             				  users to record a name during first-time enrollment, but it does not prevent
                                             				  them from completing the enrollment process if they do not. To address this issue, consider the following options: You can change whether recording a name is required to complete
                                                   						first-time enrollment on the System Settings > Advanced > Conversations
                                                   						page in Cisco Unity Connection Administration. You can provide recorded names for users in Cisco Unity
                                                   						Connection Administration. Users with class of service rights can record their own names
                                                   						using the Unity Connection conversation or the Unity Connection Messaging
                                                   						Assistant. Note This problem does not occur
                                                            						for internal users, but only for outside callers; Unity Connection users who
                                                            						address messages by name are still able to find other users even if they have
                                                            						not recorded a name. | Note | This problem does not occur
                                                            						for internal users, but only for outside callers; Unity Connection users who
                                                            						address messages by name are still able to find other users even if they have
                                                            						not recorded a name. |
| Note | This problem does not occur
                                                            						for internal users, but only for outside callers; Unity Connection users who
                                                            						address messages by name are still able to find other users even if they have
                                                            						not recorded a name. |
| Fax: attached files are not delivered to fax machines (fax integrations only) | Users may be unaware that when they add attachments to an email
                                             				  message and then send the message to a fax machine, Unity Connection renders
                                             				  only those attachments with the file extensions specified during Unity
                                             				  Connection setup. All other attachments are removed. |
| IMAP client: Differences in client behavior | Users who use different third-party IMAP clients to access voice
                                             				  messages from their desktop machines may note the following discrepancies in
                                             				  behavior: Microsoft Outlook client: For new messages, the “Mark
                                                         							 as Unread” feature marks messages as new on the Unity Connection server,
                                                         							 regardless of whether the WAV file message attachment is downloaded or not. Voice messages that are
                                                         							 deleted by phone are marked for deletion in the Outlook client and are changed
                                                         							 to strikethrough text when users select the “Send/Receive” command. Novell GroupWise client: When new messages with the
                                                         							 WAV file message attachment have been downloaded to the GroupWise client, the
                                                         							 “Read Later” feature no longer marks the message as new on the Unity Connection
                                                         							 server. Voice messages that are
                                                         							 deleted by phone are not marked for deletion in GroupWise; users need to
                                                         							 manually delete them from this client. GroupWise users need to use
                                                         							 the “Send/Retrieve” command to update message status from the Unity Connection
                                                         							 server. |
| Mailbox fills up quickly | Users may complain that their mailboxes are filling up too
                                             				  quickly, for any of the following reasons: Unity Connection does not automatically delete messages when they reach a certain age. This means that user messages are saved
                                                   until the user deletes them permanently. (For information on how to permanently delete messages, see the “ Managing the Size of Your Mailbox ” chapter of the User Guide for the Cisco Unity Connection Phone Interface (Release 14), available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/phone/b_14cucugphone.html ). When users receive nondelivery receipts (NDRs) to messages that
                                                   						they send, their email client mailbox can quickly increase in size—especially
                                                   						if the original message included large attachments. For users who have access
                                                   						to email messages via TTS, if their email clients are configured to save their
                                                   						sent messages, the original message and attachments are stored in their Sent
                                                   						Items folders and another copy is sent to their Inboxes along with the NDR,
                                                   						increasing their mailbox size accordingly. Users may receive messages that have been forwarded many times
                                                   						over, which increases message size. The original message plus all recorded
                                                   						introductions that were added during forwarding equal the total message size.
                                                   						As a result, users who have relatively few messages stored in their mailboxes
                                                   						may still find that their mailboxes exceed the storage limits. User mailboxes can fill up while users are on vacation or on an
                                                   						extended leave of absence. To prevent this, specify that Unity Connection
                                                   						prevents callers from leaving messages when users have their alternate
                                                   						greetings enabled. |
| Message notification: repeat notification
                                             				  options | When a user chooses not to have Unity Connection restart
                                             				  notification each time a new message arrives, setting a long interval between
                                             				  repeat notification calls may lead the user to believe that Unity Connection is
                                             				  delaying notification. |
| Media Master: opening a file that is saved on a
                                             				  workstation | When a user attempts to use a previously recorded WAV file (for
                                             				  example, an announcement that was recorded earlier) rather than recording using
                                             				  a phone or a computer microphone, the Media Master may display an error
                                             				  message. The error occurs when the WAV file was recorded in the G.729a audio
                                             				  format. To resolve the problem, the user must do one of the following: Convert the WAV file to another audio format (for example,
                                                   						convert it to the G.711 audio format). Use a WAV file that is recorded in a supported audio format
                                                   						other than G.729a. Make the recording using a phone or a computer microphone. |
| MWIs | To gain an understanding of when MWIs turn on and off, what causes them to turn on and off, and what causes MWIs to behave
                                             differently than expected, see the “ Troubleshooting the Message Waiting Indicators (MWIs) ” chapter of the Troubleshooting Guide for Cisco Unity Connection, Release 14 , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg.html . |
| Passwords and PINs are not secure, or users use the
                                             				  wrong password or PIN | Users may assume that their phone PINs and Cisco Personal
                                             				  Communications Assistant (PCA) passwords are the same or are synchronized. As a
                                             				  result, they may think that they are changing both PIN and password when Unity
                                             				  Connection prompts them to change their phone PIN during first-time enrollment.
                                             				  Additionally, they may try to use their phone PIN to sign in to the Cisco PCA. |
| Speed for elements of the Unity Connection
                                             				  conversation varies | Users may report that the speed at which Unity Connection plays
                                             				  menus, recorded names, greetings, and messages is inconsistent. For example,
                                             				  users may report that when they listen to their messages, the message is played
                                             				  at a different speed than the recorded names of users who leave them messages
                                             				  and the message properties (for example, the time stamp and message number). Such inconsistencies are expected when you consider the
                                             				  following: Unity Connection plays recorded names and greetings at the speed
                                                   						at which they were recorded. Neither you nor users can affect the playback
                                                   						speed of recorded names and greetings. Messages played via Text to Speech (TTS) are always played at
                                                   						normal speed by default, regardless of message playback settings. The speed that you or a user specifies for system prompts—the
                                                   						standard recordings that come with the Unity Connection system, including
                                                   						prompts for message properties—does not affect the playback speed of messages. The speed that users specify for message playback does not
                                                   						affect system prompts. |
| Unread messages | Depending on how Unity Connection is set up at your
                                             				  organization, users may be surprised at how Unity Connection handles messages
                                             				  when calls are intentionally or unintentionally disconnected (for example, when
                                             				  a user hangs up or when a mobile phone loses its charge or signal) while users
                                             				  are in the process of listening to new messages. Some users may incorrectly
                                             				  assume that Unity Connection marks the message as read, which is not the case. You can change how Unity Connection handles unread messages when
                                             				  calls are disconnected by adjusting the Mark Message Saved If User Hangs Up
                                             				  setting on the System Settings > Advanced > Conversations page of
                                             				  Cisco Unity Connection Administration. |
| Unsent messages | Depending on how Unity Connection is set up at your
                                             				  organization, users may be surprised at how Unity Connection handles messages
                                             				  when calls are intentionally or unintentionally disconnected (for example, when
                                             				  a user hangs up or when a mobile phone loses its charge or signal) while users
                                             				  are in the process of sending, replying to, or forwarding a message. Some users
                                             				  may incorrectly assume that Unity Connection offers a draft folder for unsent
                                             				  messages, which is not the case. You can change how Unity Connection handles unsent messages when
                                             				  calls are disconnected by adjusting the Send Message If User Hangs Up During
                                             				  Recording setting on the System Settings > Advanced > Conversations page
                                             				  of Cisco Unity Connection Administration. |

| Note | This problem does not occur
                                                            						for internal users, but only for outside callers; Unity Connection users who
                                                            						address messages by name are still able to find other users even if they have
                                                            						not recorded a name. |
|---|---|