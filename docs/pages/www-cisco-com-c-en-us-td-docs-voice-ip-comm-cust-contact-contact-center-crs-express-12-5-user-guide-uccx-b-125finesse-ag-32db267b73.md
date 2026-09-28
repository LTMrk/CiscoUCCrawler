---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-user-guide-uccx-b-125finesse-ag-32db267b73
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/user/guide/uccx_b_125finesse-agent-supervisor-desktop-guide/uccx_b_125finesse-agent-supervisor-desktop-guide_chapter_0100.html
retrieved_at: 2026-08-16T21:24:56.265474+00:00
---

Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1)

# Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1)

Updated: February 9, 2020

Chapter: Chat and Email Related Tasks

## Chapter: Chat and Email Related Tasks

# Chat and Email Related Tasks

## Chat and Email
                        	 Control Gadget

Not Ready:

You are set to this state by default when you sign in to the Cisco Finesse desktop.

If you refresh the browser, all the active chat sessions are cleared, email sessions are requeued, and you are moved to this
                                                      state.

You can move to this state when you are not ready to handle chat and email.

Ready: You can move to this state when you are ready to handle chat and email.

The agent must be in Not Ready state to Logout from Finesse.

When an agent accepts the chat, the state of the agent changes to Reserved.

Time-to-accept counter: When you receive an incoming chat, the time counter is displayed in the pop-over notification and you must accept the chat within the specified time. If you do not accept the chat within the specified time, your state
                                    changes to Not Ready.

Customer details: When an incoming chat arrives on your desktop, the customer details are displayed.

The buttons in the control area:

When an incoming chat request arrives, the Accept button, time-to-accept counter, and customer details appear for you to accept
                                    the chat.

### Accept a
                           	 Chat

Sends incoming chat to an available agent.

Plays an audio alert (For a, new chat request and new message on an inactive chat).

With multiple chat session tabs, the selected chat session tab is considered as active. All other chat session tabs are considered
                                                   as inactive.

Displays contact details of the customer.

When a customer initiates a chat from Facebook Messenger, Unified CCX Web Chat:

Prompts agent to accept chat before the time counter expires.

Sends incoming chat from Facebook Messenger to an available agent with a distinct icon that differentiates Facebook Messenger
                                       chat from a regular chat.

Only agents can end Facebook Messenger chats. Customers can't end chat.

Agents cannot see typing indicator from Facebook users. However, Facebook users can see typing indicator from agents.

Facebook users see the business entity name in the chat. Agent name is not displayed to Facebook users.

Group chat is supported in Facebook Messenger chat, however Facebook users continue to see the business entity name.

You are presented with incoming chats until you reach the maximum active chat sessions that are set by administrator.

Click Accept in the incoming chat pop-over notification
                                             				box within the
                                          			 specified time to accept the chat.

The Manage Chat and Email gadget opens, chat session starts, and you are connected to the customer.

Repeat Step
                                                         				  1 when you are presented with a new incoming chat.

A new tab opens for the chat session and new chat session becomes the current session.

To end the chat session, click End .

### Accept an
                           	 Email

You must be in Ready state to receive an email contact. When an email contact arrives on your desktop, it is automatically
                                 accepted and you would be notified by a pop-over notifictaion .

To view the contact, you must click the Manage Chat and Email tab to go to the Manage Chat and Email gadget. If you have more than one contact assigned to you, in the left panel, click
                                 the tab for the email contact that you want to view.

## Manage Chat and Email Gadget

The following figure shows the Cisco Finesse Manage Chat and Email gadget for agents.

The Manage Chat and Email gadget allows you to manage chat and email contacts. Chat and email contacts that are assigned to
                              you appear in tabs on the left. You can click each individual tab to view and reply to the contact.

Chat contacts are denoted by a chat icon. The following information appears on each chat contact tab:

Customer name

Total chat time: Indicates the duration of the chat session.

New message indicator: If you receive a message on a chat contact that is not your current contact, the tab flashes for a
                                    few seconds. A number appears on the tab that indicates how many messages the customer sent since you last replied.

Email contacts are denoted by an envelope icon. When you begin typing a reply to the email contact, a pencil icon appears
                              on the envelope icon.

The following information appears on each email contact tab:

Customer information: Customer email address, customer name (if available).

Email timestamp: Indicates the time that the system received the email contact.

Email subject: Hovering the mouse over the email tab, displays the subject of the email in a tool tip.

When you accept a chat request, Finesse automatically switches to the Manage Chat and Email tab and the chat becomes the active
                                          contact. When you are assigned an email contact, Finesse does not switch tabs and the contact does not become the active contact.

### Chat Interaction Panel

The following figure shows the Chat Interaction panel of the Manage Chat and Email gadget.

The Chat Interaction panel provides the following functionality:

Typing area: Type your message in the typing area. Right-click to perform basic clipboard operations, and to check spelling.

The typing awareness indicator shows when the other participant is typing.

Group Chat icon: Allows you to initiate a group chat with another agent or supervisor.

Group Chat invite appears for the agent to accept or decline the invite.

In Group Chat, an agent can click Leave to leave the group chat whenever required.

Predefined responses: Click to select a predefined response from the list. When you insert a predefined response, it is placed at the position of your
                                       cursor.

End chat session: Click End to end a chat session.

Customer details area: Click the drop-down arrow next to the customer details to minimize or maximize this area.

### Initiate a Group Chat

Send a chat invite to an available agent of the selected CSQ.

Enter the summary of the ongoing chat for the invited agent. This helps the invited agent to understand the context of the
                                       ongoing chat.

Click Invite Agent icon to initiate a group chat with another agent or supervisor.

Select a Queue from the list to invite any available agent to join the chat session.

You may enter a summary of the chat in the Enter Notes text box. This helps the invited agent to know the context of the chat. This is optional.

The summary notes are visible only when the first agent enters the notes when the chat session was initiated.

The notes entered by the invitee is displayed only to the invited agent.

Click Invite Agent .

To leave the chat session, click Leave .

When there is only one agent and the customer in the chat session, the chat can be ended by the Customer or the Agent by clicking End .

### Accept a Group Chat

You will receive an incoming group chat notification on the Finesse desktop. You may see the notes of the ongoing chat along
                                 with the invite. This helps you to understand the issue for which the group chat was initiated by the inviting agent.

Click Accept when you see the new group chat pop-over notification to join the chat session.

The agent can see chat history upto 100 messages after joining the group chat.

You may now exchange information with the other two participants (inviting agent and the customer).

The Invite Agent icon is disabled till the time there are two agents in the ongoing chat. Only when one agent chooses to leave the chat session,
                                                               the Invite Agent icon will be enabled again. The agent who wishes to leave the chat session may choose to click Leave . The agent who is still active in the group chat session can initiate another group chat by following the steps detailed
                                                               in the Initiate a Group Chat section.

The maximum number of participants in a Group Chat including the customer is three (3).

The notes are not persisted for any subsequent chat sessions with the same customer.

### Decline a Group Chat

You will receive an incoming group chat notification on the Finesse desktop. You may also see a summary of the ongoing chat
                                 along with the invite. This will help you to know the issue for which the group chat was initiated by the inviting agent.

Click Decline when you see the new group chat pop-over notification to decline the chat invite.

The agent who declined the group chat invite is not offered any successive group chat invites for the same chat session till
                                                         another agent accepts a group chat invite for the same chat session.

### Apply Wrapup Reasons for Chat and Email

Wrap-Up Reasons are the logical explanations that you can apply when you wrap up the chats and emails handled by you. If your
                                 administrator has assigned Wrap-Up Reasons for you, the Wrap-Up Reasons appear in the drop-down list that can be selected.
                                 If there are no Wrap-Up Reasons configured by the administrator, it appears blank.

Wrap-Up Reasons that your administrator modifies is available only to the new contacts and not for the contacts that you are
                                 currently handling.

Click Wrap-Up .

In a chat interaction panel you see the Wrap-Up Reasons(0) beside the End and in a group chat interaction panel beside the Leave . In an email reply panel, this is found beside the Send . The number in brackets indicates the count of Wrap-Up Reasons selected. This dynamically changes based on your selection.

Select the appropriate Wrap-Up Reasons from the drop-down list.

Click OK to close the Wrap-Up Reasons selection pane.

You can change your selection at any time. Click Wrap-Up Reasons(0) ; to open the Wrap-Up Reasons selection pane. You can select a maximum number of five (5) Wrap-Up Reasons.

### Email Reply Panel

The customer email appears on the left. The area where you type the response appears on the right. After you begin your reply,
                                 Finesse automatically saves a draft of your message every 3 minutes.

Do not close or reload the browser when you reply to an email or when the email loads on the desktop.

The Email Reply panel provides the following functionality:

Name

Description

Requeue

Requeues an email contact to a new CSQ.

Discard

Discards an email.

Reply

Sends a reply to the email address of the customer.

Reply All

Sends a reply to the customer and to all other email addresses that the customer had included in the original email.

Cc

Allows to include other email addresses to send a copy of the email to them.

Bcc

Allows to include other email addresses to send a blind copy of the email to them.

Forward

Forwards an email to other email addresses.

Bold

Applies bold to the selected text.

Italic

Applies italics to the selected text.

Underline

Underlines the selected text.

Bulleted List

Inserts a bulleted list.

Numbered List

Inserts a numbered list.

Increase Indent

Increases the space between the left margin and the content.

Decrease Indent

Decreases the space between the left margin and the content.

Align Left

Aligns the content to the left margin.

Align Center

Aligns the content to the center.

Align Right

Aligns the content to the right margin.

Add/Edit Link

Creates or modifies a hyperlink of the selected text to the specified URL.

Add Image

Adds a specified image to your reply.

Attach a file

Attaches a specified file to the email reply.

Predefined Response

Inserts the selected predefined response at the end of your reply. You can insert multiple predefined responses. Each time
                                             you select a predefined response, it adds to your reply.

If a Predefined Response is not configured, this button is disabled.

If the email is in Plain text format, this button is disabled.

Send

Sends your reply to the customer.

### Reply to an Email
                           	 Contact

On the Manage
                                          			 Chat and Email gadget, click the email contact that you want to reply to.

Click Reply/Reply All to reply to the email address of the
                                          			 customer or to any other email addresses copied by the customer. You may modify
                                          			 or add email addresses in the To field. You may also include Cc and Bcc to include more email addresses by clicking the
                                          			 respective fields.

The maximum
                                             				number of recipients allowed per field ( To , Cc , and Bcc ) is 20.

In the Email
                                          			 Response area, enter your response to the customer.

If you select a predefined response, it is inserted at the end of your email.

If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender.

When you are finished, click Send .

### Forward an
                           	 Email

On the Manage
                                          			 Chat and Email gadget, click the email contact that you want to reply to.

Click Forward to forward an email to add any other email
                                          			 addresses that you may want to send the email to. You may modify or add email
                                          			 addresses in the To field. You may also include Cc and Bcc to include more email addresses by clicking the
                                          			 respective fields.

The
                                                               						maximum number of recipients allowed per field ( To , Cc , and Bcc ) is 20.

No further attachments
                                                               						can be attached to the outgoing emails.

The Reply To field is modified
                                                               						appropriately such that the recipient of the forwarded email can reply to the
                                                               						original sender of the email directly and not send it back to the Contact
                                                               						Center.

The Requeue is disabled if you have
                                                               						initiated to forward the email. You must cancel Forward and click Reply/Reply All to requeue the email.

In the Email
                                          			 Response area, enter your response.

You can use a predefined response or type your own response.

If you select a predefined response, it is inserted at the end of your email.

If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender.

When you are
                                          			 finished, click Send .

### Download Customer Attachments

If a customer includes attachments in an email, the attachment filenames appear under the subject of the email. Finesse imposes
                                 the following limitations on customer email attachments:

The total file size limit in an agent's reply is 20 MB.

Images within the body of the email are counted as attachments.

The size limit of a single file attachment is 10 MB.

The total size limit of attachments in the incoming email from the customer is 20 MB.

Click the filename of the attachment you want to open or download.

Choose whether to open the file or save the file to your computer.

Repeat Step 1 and Step 2 for each attachment that you want to open or download.

### Insert a Hyperlink to an Email

In your email reply, select the text that you want to turn into a hyperlink.

Click the Insert/Edit Link icon.

In the dialogue box, enter the URL for the link.

Click Add .

### Insert an Image to an Email

Place your cursor where you want the image to appear.

Click the Insert Image icon.

In the dialogue box, enter the URL.

Click Add .

You can also copy and paste an image into the email response.

### Add an Attachment to an Email

You can add up to 10 attachments to an email reply to a customer. The following limitations apply:

The size of a single attachment must not exceed 10 MB.

The total size of all attachments must not exceed 20MB.

Click the Attach File icon.

Navigate to the file that you want to attach to the email.

Click Open .

Repeat Step 1 and Step 2 for each file that you want to attach (up to 10).

If you want to remove an attachment, click the X to the right of the attachment filename.

### Requeue an Email Contact

You can requeue an email contact either to the same Contact Service Queue (CSQ) or to any other CSQ. After you initiate the
                                 requeue from the agent desktop, the contacts are requeued to a CSQ.

Last-agent email routing is a mechanism to route an email message to the agent who last handled the email conversation. When
                                 you requeue an email, the email will be routed to the intended CSQ to be handled by any available agent, and last-agent email
                                 routing is not considered.

The requeued contact is not requeued to the same agent even if the agent is part of the requeued CSQ and is available to handle
                                             more contacts.

When you sign out or refresh your browser, any contacts that you were handling are disassociated from you and requeued to
                                 the same CSQ.

Select the email that you want to requeue.

Click Requeue .

Type the CSQ name in the Search box to select the desired CSQ from the list.

Click Yes to confirm.

### Discard an Email Message

On the Manage Chat and Email gadget, select the email message that you want to discard.

Click Discard icon on the Email Reply panel.

You are prompted to discard the selected email message.

Click Yes to confirm.

The email message is discarded.

When you discard an unsent reply that has attachments, the draft of the reply from the agent and the attachments are deleted.
                                             The original email message sent by the email contact remains in the Exchange mailbox.

| Note | With multiple chat session tabs, the selected chat session tab is considered as active. All other chat session tabs are considered
                                                   as inactive. |
|---|---|

| Note | The maximum length of a chat message from the agent is 1500 unicode characters. |
|---|---|

| Step 1 | Click Accept in the incoming chat pop-over notification
                                             				box within the
                                          			 specified time to accept the chat. The Manage Chat and Email gadget opens, chat session starts, and you are connected to the customer. Note Repeat Step
                                                         				  1 when you are presented with a new incoming chat. A new tab opens for the chat session and new chat session becomes the current session. | Note | Repeat Step
                                                         				  1 when you are presented with a new incoming chat. A new tab opens for the chat session and new chat session becomes the current session. |
|---|---|---|---|
| Note | Repeat Step
                                                         				  1 when you are presented with a new incoming chat. A new tab opens for the chat session and new chat session becomes the current session. |
| Step 2 | To end the chat session, click End . |

| Note | Repeat Step
                                                         				  1 when you are presented with a new incoming chat. A new tab opens for the chat session and new chat session becomes the current session. |
|---|---|

| Note | When you accept a chat request, Finesse automatically switches to the Manage Chat and Email tab and the chat becomes the active
                                          contact. When you are assigned an email contact, Finesse does not switch tabs and the contact does not become the active contact. |
|---|---|

| Step 1 | Click Invite Agent icon to initiate a group chat with another agent or supervisor. |
|---|---|
| Step 2 | Select a Queue from the list to invite any available agent to join the chat session. |
| Step 3 | You may enter a summary of the chat in the Enter Notes text box. This helps the invited agent to know the context of the chat. This is optional. Note The summary notes are visible only when the first agent enters the notes when the chat session was initiated. The notes entered by the invitee is displayed only to the invited agent. | Note | The summary notes are visible only when the first agent enters the notes when the chat session was initiated. |
| Note | The summary notes are visible only when the first agent enters the notes when the chat session was initiated. |
| Step 4 | Click Invite Agent . The available agent gets a notification to Accept or Decline the chat. When an available agent accepts the group chat, the three participants (the two agents and the customer) may exchange
                                          information in the chat window. |
| Step 5 | To leave the chat session, click Leave . When there is only one agent and the customer in the chat session, the chat can be ended by the Customer or the Agent by clicking End . |

| Note | The summary notes are visible only when the first agent enters the notes when the chat session was initiated. |
|---|---|

| Step 1 | Click Accept when you see the new group chat pop-over notification to join the chat session. The agent can see chat history upto 100 messages after joining the group chat. |
|---|---|
| Step 2 | You may now exchange information with the other two participants (inviting agent and the customer). Note The Invite Agent icon is disabled till the time there are two agents in the ongoing chat. Only when one agent chooses to leave the chat session,
                                                               the Invite Agent icon will be enabled again. The agent who wishes to leave the chat session may choose to click Leave . The agent who is still active in the group chat session can initiate another group chat by following the steps detailed
                                                               in the Initiate a Group Chat section. The maximum number of participants in a Group Chat including the customer is three (3). The notes are not persisted for any subsequent chat sessions with the same customer. | Note | The Invite Agent icon is disabled till the time there are two agents in the ongoing chat. Only when one agent chooses to leave the chat session,
                                                               the Invite Agent icon will be enabled again. The agent who wishes to leave the chat session may choose to click Leave . The agent who is still active in the group chat session can initiate another group chat by following the steps detailed
                                                               in the Initiate a Group Chat section. The maximum number of participants in a Group Chat including the customer is three (3). The notes are not persisted for any subsequent chat sessions with the same customer. |
| Note | The Invite Agent icon is disabled till the time there are two agents in the ongoing chat. Only when one agent chooses to leave the chat session,
                                                               the Invite Agent icon will be enabled again. The agent who wishes to leave the chat session may choose to click Leave . The agent who is still active in the group chat session can initiate another group chat by following the steps detailed
                                                               in the Initiate a Group Chat section. The maximum number of participants in a Group Chat including the customer is three (3). The notes are not persisted for any subsequent chat sessions with the same customer. |

| Note | The Invite Agent icon is disabled till the time there are two agents in the ongoing chat. Only when one agent chooses to leave the chat session,
                                                               the Invite Agent icon will be enabled again. The agent who wishes to leave the chat session may choose to click Leave . The agent who is still active in the group chat session can initiate another group chat by following the steps detailed
                                                               in the Initiate a Group Chat section. The maximum number of participants in a Group Chat including the customer is three (3). The notes are not persisted for any subsequent chat sessions with the same customer. |
|---|---|

| Click Decline when you see the new group chat pop-over notification to decline the chat invite. Note The agent who declined the group chat invite is not offered any successive group chat invites for the same chat session till
                                                         another agent accepts a group chat invite for the same chat session. | Note | The agent who declined the group chat invite is not offered any successive group chat invites for the same chat session till
                                                         another agent accepts a group chat invite for the same chat session. |
|---|---|---|
| Note | The agent who declined the group chat invite is not offered any successive group chat invites for the same chat session till
                                                         another agent accepts a group chat invite for the same chat session. |

| Note | The agent who declined the group chat invite is not offered any successive group chat invites for the same chat session till
                                                         another agent accepts a group chat invite for the same chat session. |
|---|---|

| Step 1 | Click Wrap-Up . In a chat interaction panel you see the Wrap-Up Reasons(0) beside the End and in a group chat interaction panel beside the Leave . In an email reply panel, this is found beside the Send . The number in brackets indicates the count of Wrap-Up Reasons selected. This dynamically changes based on your selection. |
|---|---|
| Step 2 | Select the appropriate Wrap-Up Reasons from the drop-down list. |
| Step 3 | Click OK to close the Wrap-Up Reasons selection pane. You can change your selection at any time. Click Wrap-Up Reasons(0) ; to open the Wrap-Up Reasons selection pane. You can select a maximum number of five (5) Wrap-Up Reasons. |

| Note | Do not close or reload the browser when you reply to an email or when the email loads on the desktop. |
|---|---|

| Name | Description |
|---|---|
| Requeue | Requeues an email contact to a new CSQ. |
| Discard | Discards an email. |
| Reply | Sends a reply to the email address of the customer. |
| Reply All | Sends a reply to the customer and to all other email addresses that the customer had included in the original email. |
| Cc | Allows to include other email addresses to send a copy of the email to them. |
| Bcc | Allows to include other email addresses to send a blind copy of the email to them. |
| Forward | Forwards an email to other email addresses. |
| Bold | Applies bold to the selected text. |
| Italic | Applies italics to the selected text. |
| Underline | Underlines the selected text. |
| Bulleted List | Inserts a bulleted list. |
| Numbered List | Inserts a numbered list. |
| Increase Indent | Increases the space between the left margin and the content. |
| Decrease Indent | Decreases the space between the left margin and the content. |
| Align Left | Aligns the content to the left margin. |
| Align Center | Aligns the content to the center. |
| Align Right | Aligns the content to the right margin. |
| Add/Edit Link | Creates or modifies a hyperlink of the selected text to the specified URL. |
| Add Image | Adds a specified image to your reply. |
| Attach a file | Attaches a specified file to the email reply. |
| Predefined Response | Inserts the selected predefined response at the end of your reply. You can insert multiple predefined responses. Each time
                                             you select a predefined response, it adds to your reply. Note If a Predefined Response is not configured, this button is disabled. If the email is in Plain text format, this button is disabled. | Note | If a Predefined Response is not configured, this button is disabled. If the email is in Plain text format, this button is disabled. |
| Note | If a Predefined Response is not configured, this button is disabled. If the email is in Plain text format, this button is disabled. |
| Send | Sends your reply to the customer. |

| Note | If a Predefined Response is not configured, this button is disabled. If the email is in Plain text format, this button is disabled. |
|---|---|

| Step 1 | On the Manage
                                          			 Chat and Email gadget, click the email contact that you want to reply to. |
|---|---|
| Step 2 | Click Reply/Reply All to reply to the email address of the
                                          			 customer or to any other email addresses copied by the customer. You may modify
                                          			 or add email addresses in the To field. You may also include Cc and Bcc to include more email addresses by clicking the
                                          			 respective fields. The maximum
                                             				number of recipients allowed per field ( To , Cc , and Bcc ) is 20. |
| Step 3 | In the Email
                                          			 Response area, enter your response to the customer. You can use a predefined response or type your own response. Note If you select a predefined response, it is inserted at the end of your email. If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender. | Note | If you select a predefined response, it is inserted at the end of your email. If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender. |
| Note | If you select a predefined response, it is inserted at the end of your email. If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender. |
| Step 4 | When you are finished, click Send . |

| Note | If you select a predefined response, it is inserted at the end of your email. If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender. |
|---|---|

| Step 1 | On the Manage
                                          			 Chat and Email gadget, click the email contact that you want to reply to. |
|---|---|
| Step 2 | Click Forward to forward an email to add any other email
                                          			 addresses that you may want to send the email to. You may modify or add email
                                          			 addresses in the To field. You may also include Cc and Bcc to include more email addresses by clicking the
                                          			 respective fields. Note The
                                                               						maximum number of recipients allowed per field ( To , Cc , and Bcc ) is 20. No further attachments
                                                               						can be attached to the outgoing emails. The Reply To field is modified
                                                               						appropriately such that the recipient of the forwarded email can reply to the
                                                               						original sender of the email directly and not send it back to the Contact
                                                               						Center. The Requeue is disabled if you have
                                                               						initiated to forward the email. You must cancel Forward and click Reply/Reply All to requeue the email. | Note | The
                                                               						maximum number of recipients allowed per field ( To , Cc , and Bcc ) is 20. No further attachments
                                                               						can be attached to the outgoing emails. The Reply To field is modified
                                                               						appropriately such that the recipient of the forwarded email can reply to the
                                                               						original sender of the email directly and not send it back to the Contact
                                                               						Center. The Requeue is disabled if you have
                                                               						initiated to forward the email. You must cancel Forward and click Reply/Reply All to requeue the email. |
| Note | The
                                                               						maximum number of recipients allowed per field ( To , Cc , and Bcc ) is 20. No further attachments
                                                               						can be attached to the outgoing emails. The Reply To field is modified
                                                               						appropriately such that the recipient of the forwarded email can reply to the
                                                               						original sender of the email directly and not send it back to the Contact
                                                               						Center. The Requeue is disabled if you have
                                                               						initiated to forward the email. You must cancel Forward and click Reply/Reply All to requeue the email. |
| Step 3 | In the Email
                                          			 Response area, enter your response. You can use a predefined response or type your own response. Note If you select a predefined response, it is inserted at the end of your email. If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender. | Note | If you select a predefined response, it is inserted at the end of your email. If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender. |
| Note | If you select a predefined response, it is inserted at the end of your email. If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender. |
| Step 4 | When you are
                                          			 finished, click Send . |

| Note | The
                                                               						maximum number of recipients allowed per field ( To , Cc , and Bcc ) is 20. No further attachments
                                                               						can be attached to the outgoing emails. The Reply To field is modified
                                                               						appropriately such that the recipient of the forwarded email can reply to the
                                                               						original sender of the email directly and not send it back to the Contact
                                                               						Center. The Requeue is disabled if you have
                                                               						initiated to forward the email. You must cancel Forward and click Reply/Reply All to requeue the email. |
|---|---|

| Note | If you select a predefined response, it is inserted at the end of your email. If Email Signature is configured, it gets appended at the end of the email before sending. The Email Signature is not visible to the sender. |
|---|---|

| Note | Images within the body of the email are counted as attachments. |
|---|---|

| Step 1 | Click the filename of the attachment you want to open or download. You are prompted to open or save the file. |
|---|---|
| Step 2 | Choose whether to open the file or save the file to your computer. |
| Step 3 | Repeat Step 1 and Step 2 for each attachment that you want to open or download. |

| Step 1 | In your email reply, select the text that you want to turn into a hyperlink. |
|---|---|
| Step 2 | Click the Insert/Edit Link icon. A dialog box opens where you can enter the URL for the link. |
| Step 3 | In the dialogue box, enter the URL for the link. |
| Step 4 | Click Add . |

| Step 1 | Place your cursor where you want the image to appear. |
|---|---|
| Step 2 | Click the Insert Image icon. A dialog box opens where you can enter a URL for the image. |
| Step 3 | In the dialogue box, enter the URL. |
| Step 4 | Click Add . The image appears inline in the email response. You can also copy and paste an image into the email response. |

| Step 1 | Click the Attach File icon. |
|---|---|
| Step 2 | Navigate to the file that you want to attach to the email. |
| Step 3 | Click Open . The file appears below the reply panel. |
| Step 4 | Repeat Step 1 and Step 2 for each file that you want to attach (up to 10). If you want to remove an attachment, click the X to the right of the attachment filename. |

| Note | The requeued contact is not requeued to the same agent even if the agent is part of the requeued CSQ and is available to handle
                                             more contacts. |
|---|---|

| Step 1 | Select the email that you want to requeue. |
|---|---|
| Step 2 | Click Requeue . The list of CSQs is displayed with a search option. |
| Step 3 | Type the CSQ name in the Search box to select the desired CSQ from the list. A confirmation dialog appears. |
| Step 4 | Click Yes to confirm. |

| Step 1 | On the Manage Chat and Email gadget, select the email message that you want to discard. |
|---|---|
| Step 2 | Click Discard icon on the Email Reply panel. You are prompted to discard the selected email message. |
| Step 3 | Click Yes to confirm. The email message is discarded. When you discard an unsent reply that has attachments, the draft of the reply from the agent and the attachments are deleted.
                                             The original email message sent by the email contact remains in the Exchange mailbox. |