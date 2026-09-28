---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-0101-ht-486f1e0e39
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_0101.html
retrieved_at: 2026-08-17T02:28:40.287008+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting
	 Messages

## Chapter: Troubleshooting
	 Messages

# Troubleshooting
                     	 Messages

## User Hears Full
                        	 Mailbox Warnings

When users hear a prompt related to
                           		a full mailbox, it means that the limit of at least one of the following
                           		mailbox quotas, which limit the size of voice mailboxes, has reached:

Warning Quota: If a mailbox has
                                 			 reached the size of the warning quota, the user hears a warning that the
                                 			 mailbox is almost full. To resolve the issue, delete the messages until the
                                 			 mailbox size becomes less than the warning quota.

Send Quota: If a mailbox has reached the size of the send quota, the
                                 			 user is unable to send messages and hears a warning that messages cannot be
                                 			 sent. If the user mailbox contains deleted messages, Cisco Unity Connection
                                 			 offers the option to remove all deleted messages to reduce the mailbox size.

Send/Receive quota: If a mailbox has reached the size of the
                                 			 send/receive quota:

- The user is unable to
                                    				send messages.

- The user hears a warning
                                    				that messages cannot be sent.

- Unidentified callers are
                                    				not allowed to leave messages for the user.

- Messages from other
                                    				users generate nondelivery receipts to the senders.

- If the user mailbox
                                    				contains deleted messages, Unity Connection offers the option to remove all
                                    				deleted messages. If necessary, the user can also remove saved or new messages
                                    				individually until the mailbox size is below the quotas.

## Nondelivery
                        	 Receipt (NDR) Not Received for Undelivered Message

Occasionally, messages cannot be
                           		delivered to the recipient that the caller intended to reach. The system
                           		behavior in this case depends on the type of sender and the reason that the
                           		message could not be delivered.

In general, if Unity Connection cannot deliver the message because of
                           		issues that are not likely to be resolved (for example, the caller was
                           		disconnected before addressing the message or the recipient mailbox has been
                           		deleted), the message is sent to the Undeliverable Messages distribution list,
                           		and Unity Connection sends a nondelivery receipt (NDR) to the sender. However,
                           		the sender does not receive a nondelivery receipt in the following cases:

When the sender of the original
                                 			 message is an unidentified caller

When the sender is a user, but the user is configured to not accept
                                 			 NDRs

While the mailstore of the user is offline (in this case, the NDR is
                                 			 delivered when the database becomes available).

If the original message is malformed, rather than sending the message to
                           		the Undeliverable Messages list, Unity Connection places the message in the MTA
                           		bad mail folder (UmssMtaBadMail). This folder is automatically checked nightly
                           		by the Monitor Bad Mail Folders task and if messages are found, an error is
                           		written to the application event log indicating troubleshooting steps.

## Messages Are
                        	 Delayed

Following are the
                              		  tasks to troubleshoot the possible causes for the apparent delay of messages.

To verify the
                                       			 arrival times of messages, generate a user message activity report for the
                                       			 user. For more information, see the " Generating and Viewing
                                          				Reports " section in the "Using Reports" chapter of the Administration
                                       			 Guide for Cisco Unity Connection Serviceability Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/serv_administration/b_12xcucservag.html

See the
                                       			 applicable information in the " Orientation Task List for
                                          				Unity Connection Users " section in the "User Orientation" chapter of
                                       			 the User Workstation Setup Guide for Cisco Unity ConnectionRelease 12.x,
                                       			 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user_setup/guide/b_12xcucuwsx.html .

## Messages Are Not
                        	 Delivered

See the following
                           		troubleshooting steps for investigating messages that are not being delivered
                           		to the intended recipients.

Confirm that the
                                 			 users who are assigned to the Undeliverable Messages distribution list have
                                 			 been forwarding messages to the intended recipients. See the Undeliverable Messages Not Forwarded to Recipients section.

- Confirm that the user
                              		  mailbox is not full. See the User Has a Full Mailbox

Confirm that you
                                 			 or another administrator did not inadvertently delete a user who was assigned
                                 			 to review the messages for Cisco Unity Connection entities. See the Users Assigned to Unity Connection Entities Deleted and No Replacements Assigned section.

Review message
                                 			 aging settings. See the " Message Aging Policies " section in the "Message Storage" chapter of the System Administration Guide
                                 			 for Cisco Unity Connection Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

Verify that the
                                 			 message, which got removed from the mailbox, is not flagged for dispatch
                                 			 delivery. If the two users belongs to a distribution list that is the recipient
                                 			 of a call handler configured to mark messages for dispatch delivery, then a
                                 			 message is removed from the mailbox of the user as soon as the message is
                                 			 accepted by another user of the distribution list. See the " Dispatch Messages "
                                 			 section in the "Messaging" chapter of the System Administration Guide for Cisco
                                 			 Unity Connection Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

The user account
                                 			 may be configured to relay one or more message types to another SMTP address,
                                 			 but the message relay is failing. See the Unity Connection Unable to Relay Messages

### User Has a Full Mailbox

If a user mailbox is no longer allowed to receive messages, Unity
                              		Connection handles the message in either of the following ways:

By default, when an unidentified caller attempts to send a message
                                    			 to a user whose mailbox has exceeded the send/receive quota, Unity Connection
                                    			 still delivers the message. For such scenarios, you can configure Unity
                                    			 Connection to indicate the caller that the recipient mailbox is full, and
                                    			 prevent the caller from recording a message for that recipient. To do this, log
                                    			 in to Cisco Unity Connection Administration, navigate to the Message Storage
                                    			 > Mailbox Quotas page, and check the Full Mailbox Check for Outside Caller
                                    			 Messages check box.)

If the recipient mailbox has not yet exceeded the send/receive quota
                                    			 at the time an unidentified caller records a message but the quota is exceeded
                                    			 in the act of delivering the message, Unity Connection delivers the message
                                    			 regardless of the quota.

When a user tries to leave a message for another user whose mailbox
                                    			 has exceeded the send/receive quota, Unity Connection allows the user to record
                                    			 and send the message. However, if the mailbox for the recipient is full, he or
                                    			 she does not receive the message. In addition, if the user account for the
                                    			 recipient is configured to send non-delivery receipts when message delivery
                                    			 fails, Unity Connection sends the message sender a non-delivery receipt.

If the recipient mailbox has not yet exceeded the send/receive quota
                                    			 at the time a Unity Connection user records a message, but the quota is
                                    			 exceeded in the act of delivering the message, Unity Connection delivers the
                                    			 message regardless of the quota.

If a user whose voice mailbox has exceeded the send quota logs in to
                              		Unity Connection and attempts to send a message to another user, Unity
                              		Connection indicates that the send quota has been exceeded and does not allow
                              		the sender to record the message. If a user calls another user and the call is
                              		forwarded to a voice mailbox, the user is able to leave a message but the
                              		message is sent as an outside caller message.

Read receipts and non-delivery receipts are sent and delivered
                              		regardless of the status of the mailbox quota.

Encourage the user to dispose of messages promptly so that the Unity
                              		Connection mailbox does not fill up, and explain to users on the Undeliverable
                              		Messages distribution list the importance of regularly checking for and
                              		forwarding undeliverable messages.

### Undeliverable
                           	 Messages Not Forwarded to Recipients

Messages returned to the Unity
                              		Messaging System mailbox are forwarded automatically to users whose names
                              		appear on the Undeliverable Messages system distribution list. The messages
                              		then must be forwarded to the intended recipients. Therefore, the users of the
                              		Undeliverable Messages distribution list should regularly check and forward
                              		undeliverable messages.

### Users Assigned to
                           	 Unity Connection Entities Deleted and No Replacements Assigned

When you delete a user who was
                              		assigned to review the messages that are sent to any of the following Unity
                              		Connection entities, make sure that you assign another user or a distribution
                              		list to replace the deleted user; otherwise, messages may be lost:

Undeliverable Messages
                                    			 distribution list (by default, the UndeliverableMessagesMailbox user account is
                                    			 the only member of this distribution list)

- Operator call handler

- Opening Greeting call
                                 		  handler

- Goodbye call handler

- Example Interview call
                                 		  handler

### Unity Connection
                           	 Unable to Relay Messages

Unity Connection uses the settings
                              		on the Message Actions page for a user in Cisco Unity Connection Administration
                              		to determine how to handle the different types of messages that it receives for
                              		the user. The relay action instructs Unity Connection to send all the messages
                              		of a certain type to a relay address on a different messaging system (such as a
                              		corporate email server) for storage and user access.

If the relay address that is configured for a user matches one of the
                              		user SMTP proxy addresses that is configured on the system, Unity Connection
                              		does not relay messages to the relay address to avoid possible delivery loops.
                              		For example, if Unity Connection needs to relay a message to a proxy address,
                              		it is possible that the proxy address would resolve back to the same Unity
                              		Connection mailbox that relayed the original message, thus creating an infinite
                              		loop.

When configuring relay addresses for message relay, we recommend that
                              		you use the precise email address of the destination mailbox, for example,
                              		alias@mailserver. If a Unity Connection server is unable to relay message to
                              		the correct address, make sure the smarthost entered on the server is correct
                              		and reachable. However, if the problem is still not resolved, review the
                              		message relay logs mentioned in Micro Traces for Selected Problems section.

## Unable to Play
                        	 Message Audio in Outlook Web Access

When Unity Connection is configured
                           		to relay messages to a Microsoft Exchange server (using the Relay the Message
                           		or the Accept and Relay the Message action), users who use Outlook Web Access
                           		to access their Exchange mailboxes may not be able to play the message audio.
                           		When this occurs, the message header indicates that the audio attachment is
                           		available for the message, but the user cannot view or play the attachment when
                           		the message is opened.

## Unable to Receive
                        	 Notification Emails for Quota Overflow

If a user is unable to receive
                           		notification emails for quota overflow, verify the following:

Verify that the sender (Unity
                                 			 Connection) is not getting an NDR in the mailbox. If the sender is getting an
                                 			 NDR, check the NDR code and take action accordingly. For more information on
                                 			 NDR codes, refer to the " Troubleshooting Non-Delivery Receipts "chapter of this guide.

Verify that the corporate email address specified for the user is
                                 			 valid and correctly spelled.

Verify that the corporate mailbox of the user has some free space.

| Step 1 | To verify the
                                       			 arrival times of messages, generate a user message activity report for the
                                       			 user. For more information, see the " Generating and Viewing
                                          				Reports " section in the "Using Reports" chapter of the Administration
                                       			 Guide for Cisco Unity Connection Serviceability Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/serv_administration/b_12xcucservag.html |
|---|---|
| Step 2 | See the
                                       			 applicable information in the " Orientation Task List for
                                          				Unity Connection Users " section in the "User Orientation" chapter of
                                       			 the User Workstation Setup Guide for Cisco Unity ConnectionRelease 12.x,
                                       			 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user_setup/guide/b_12xcucuwsx.html . |

| Caution | If the mailboxes of the users who are assigned to
                                       		check the Undeliverable Messages list exceed the send/receive quota, the
                                       		messages sent to the Undeliverable Messages distribution list are lost. To
                                       		avoid this problem, specify a generous value for the send/receive quota for at
                                       		least one user who is a member of the Undeliverable Messages list and encourage
                                       		the user to dispose of messages promptly. |
|---|---|

| Caution | If the mailboxes of the users who are assigned to
                                       		check the Undeliverable Messages list exceed the send/receive quota, the
                                       		messages sent to the Undeliverable Messages distribution list are lost. To
                                       		avoid this problem, specify a generous value for the send/receive quota for at
                                       		least one user who is a member of the Undeliverable Messages list and encourage
                                       		the user to dispose of messages promptly. |
|---|---|