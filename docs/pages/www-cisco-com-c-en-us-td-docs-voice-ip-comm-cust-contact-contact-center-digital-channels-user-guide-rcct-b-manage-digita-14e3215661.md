---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-digital-channels-user-guide-rcct-b-manage-digita-14e3215661
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/digital-channels/user/guide/rcct_b_manage-digital-channels/rcct_m_manage-digital-channels.html
retrieved_at: 2026-08-16T20:33:35.819814+00:00
---

Cisco Contact Center Enterprise Manage Digital Channels Gadget User Guide

# Cisco Contact Center Enterprise Manage Digital Channels Gadget User Guide

Book Contents

- Book Title Page

- Preface

- Manage Digital Channels gadget

Find Matches in This Book

## Results

Updated: April 30, 2025

Chapter: Manage Digital Channels gadget

## Chapter: Manage Digital Channels gadget

# Manage Digital Channels gadget

As agents and supervisors, use the Manage Digital Channels gadget to interact with customers through digital channels. The gadget is available only with SSO login. The gadget is available
                        when your administrator has configured and assigned at least one digital channel to you. The following digital channels are
                        available:

Chat/Social Channels —This is a media type on the Finesse Desktop to provide a common interface to control multiple underlying digital channels.
                              This media type represents the following digital channels:

Live Chat

SMS

Facebook Messenger

WhatsApp

Apple Messages for Business

Email —Represents the media type for the Email digital channel.

## Get started with Manage Digital Channels gadget

After signing in to the Finesse desktop, you must explicitly sign in to the Manage Digital Channels gadget and manually change the digital channels state to Ready . You must be in the Ready state to receive tasks for interaction. There's no explicit sign-out for this gadget.

To sign out of Finesse desktop, all the channels (voice and digital) must be in Not Ready state.

### Before you begin

Ensure that your administrator has configured the Manage Digital Channels gadget and you have access to it.

Ensure that your Finesse desktop has internet connectivity with the required bandwidth and latency as specified in the Cisco Finesse Administration Guide , so that it can load the Manage Digital Channels gadget from the cloud datacenter.

Step 1

Sign in to Finesse desktop.

Step 2

From the left pane, select Manage Digital Channels . The Manage Digital Channels Sign In dialog appears.

Step 3

Click Sign In .

The gadget signs in to all the digital channels ( Chat/Social Channels and Email ) that are configured for the user. The digital channel icons that are available at the top of the window, display your status.

After you successfully sign in, by default all the digital channels are in Not Ready state.

When there's a sign-in failure for any of the media types, notifications appear with the sign-in failure reason. Sign-in is
                                                      retried automatically for the configured number of times.

Step 4

Click the drop-down arrow next to the Chat/Social Channels and Email icons.

The following list appears:

All

Chat/Social Channels

Email

Under each channel, there's an option to move the channel to Ready or Not Ready state. The Not Ready reasons for voice and digital channels are the same.

The drop-down doesn't list the already selected reason. For example, if the status is Not Ready Lunch , this option isn't listed.

Step 5

Select Ready to be available for the required digital channel.

If any of the digital channels fail to change their state to Ready , a pop over notification appears on the top-right corner of the window. The gadget retries to sign in for the configured
                              number of times.

The digital channels have a visual representation for different states as shown in the following table:

### State change of digital channels

If you don’t accept an interaction before a stipulated time, a pop-over notification appears at the top-right corner of the
                                 window and the digital channels state changes to Not Ready automatically.

When any of the Chat/Social Channels go to the Not Ready state, all the Chat/Social Channels go to the Not Ready state. You can continue to use the active tasks but no new tasks are presented. If you sign out, the active tasks are Closed or Transferred as per the administration configuration. You must manually change the respective channel state to Ready to start receiving tasks again.

When you manually change your state to Not Ready , you must select an appropriate reason to indicate why you’re changing your state to Not Ready . Always select a Not Ready reason specifically for Chat/Social Channels and Email . The specific Not Ready reasons aren’t available for the All option. The specific Not Ready reasons take precedence over the Not Ready option for All . For example, if you’ve selected a custom not ready reason such as Not Ready Lunch , when you select the Not Ready option from the All option, there’s no change. However, if you have selected Not Ready from the All option and later select Not Ready Lunch , then the state changes to Not Ready Lunch .

When changing the state, it’s possible for any of the media types that are under Chat/Social Channels to fail due to network issues or other such conditions. If this happens, the icon indicates the partial state as shown in
                                 the table. You must manually change the respective media state to Ready to start receiving tasks again.

### Accept Tasks

When you're in Ready state, you start receiving pop over notifications from customers for all the digital channels. The notifications are presented
                                 at the bottom-right corner of the window. The notifications display the customer details (that the administrator has configured)
                                 with the Accept button.

Click Accept to start an interaction. When you accept a new task, the new task is appended to the existing Tasks list and becomes active.
                                 Ensure that you accept the incoming interactions within the predefined time as shown in the countdown timer. Otherwise, the
                                 interactions get routed to the next available agent and your state changes to Not Ready automatically.

You can also interact with multiple customers on multiple channels at the same time. Accept the notifications that are presented
                                 to you for various digital channels.

If you are not active on the Finesse desktop and don't accept an incoming interaction within the configured time, a toaster
                                 notification appears on the system once the interaction times out, indicating that you missed the interaction and your status
                                 is changed to Not Ready.

The number of tasks that are presented to you for each digital channel (LiveChat, SMS, Email, Facebook Messenger, WhatsApp,
                                             and Apple Messages for Business is configured by your administrator.

Different media may have different accept timers as per the configuration.

The following table lists the results of not accepting a task within the predefined time for each channel:

Media Notification

State Change to Not Ready

Notes

Email

Email

Only Email channel is changed to the Not Ready state.

Live Chat

Chat/Social Channels

First the Live Chat becomes Not Routable and then all the media under Chat/Social Channels are changed to the Not Ready state.

SMS

Facebook Messenger

WhatsApp

Apple Messages for Business

### View Tasks window

When you accept any digital interaction, a Task window is displayed. For example, if you accept an email task, a Task window is displayed for the Email channel.

By default, the Task window is maximized and includes the following:

Tasks list

Customer details

Interaction pane

Typing area

When the Task window is loaded, if you accept a voice call, the voice channel displays at the top and the Task window is pushed down. This happens only when the voice channel is configured as a page level gadget.

#### Tasks list

The Tasks list appears on the left side of the Task window. It lists all your digital channel interactions. The number of tasks that has to be handled by you for each digital
                                    channel (Live Chat, SMS, Email, Facebook Messenger, WhatsApp, and Apple Messages for Business) is configured by your administrator.

When you accept a new task, the new task is appened to the existing Tasks list and becomes active. All digital channels have
                                    their specific icons for identification. By default, all the interactions display the following:

Icon

Queue name

Timer

Customer name or any other data that is configured by the administrator

This field is always in bold font.

The timer indicates the time duration of the interaction. Below the timer of each interaction, the unread messages number
                                    is highlighted. When you select an interaction that has unread messages, the highlight and the number are removed for that
                                    interaction. If you receive a voice call, the timer may stop as per the configuration.

Administrators can configure more details that have to be displayed, so that it's easy for you to identify and interact. Some
                                    of the details that the administrator can configure are as follows:

Customer name

Contact number

You can collapse and expand this list using a mouse or shortcut keys. Expand the list to view any new messages from existing
                                    interactions. You can traverse through the list using the Up and down arrows of the keyboard. In between interactions, if
                                    you've moved out of the Manage Digital Channels gadget and then receive messages from ongoing interactions:

If you haven't pinned the navigation pane, a pop over notification is displayed at the top-right corner of the Task window,
                                          the unread messages number is incremented and highlighted.

If you’ve pinned the navigation pane, displays a red dot next to the Manage Digital Channels gadget in the navigation pane.

If the gadget is part of a multi-tab, displays a red dot on top of the Manage Digital Channels gadget tab.

#### Customer details

The customer details display the customer information that is configured by your administrator. It also displays the customer
                                    name (or any other data that is configured by the administrator), timer, Transfer button, and End button at the top of the details. It is next to the Tasks list. It displays a maximum of 10 fields. If more than 10 fields are configured, a scroll bar appears. You can collapse and
                                    expand the customer details area using a mouse or shortcut keys.

As per the configuration, you can edit some or all the customer details. When you hover the mouse over an editable field,
                                    the color of the field is shaded and displays a copy icon. To edit the customer details:

Click on the editable field.

Make the necessary changes and click Save .

Displays the success or failure messages at the bottom-left corner in the Customer details area.

Click Revert to cancel the changes and retain the previous values.

If you edit any of the fields, not save, and click Transfer or End , the gadget displays the Unsaved Changes dialog box. You can continue without saving or cancel to come back to the Task window and save the changes.

#### Interaction pane

The interaction pane appears on the right side of the Tasks list and below the Customer Details area. This pane lists all the interactions that you’re having with a particular customer. When loading for the first time,
                                    it displays a loading message. If there’s a failure to load the data and if you think that it’s a temporary issue, click Try Again to reload the data.

## Manage SMS conversations

The Short Message Service (SMS) channel enables customers to reach out to agents by sending an SMS. Customers can send SMS
                              to a Longcode, Shortcode, or toll-free number. A new conversation is created in the SMS widget when a customer sends a message.
                              Agents can then handle the chat and send a response to the customer.

The SMS widget enables agents to respond to SMS messages through the conversation pane in the Agent Desktop.

You can use the agent desktop to transfer and end an SMS conversation.

You can send SMS even when there is no internet connectivity.

### About SMS widget

For a list of features supported on the SMS widget and detailed instructions on how to use them, refer to Common Functionalities of Digital Channel Interactions .

### Respond to SMS conversation

After an SMS conversation is assigned to an agent, the popover displays the Queue Name, Phone Number, Source Number, Timer,
                                 and Accept button. The timer indicates the time that has elapsed since you were offered the SMS conversation.

Once an SMS conversation is assigned to an agent, it lands in the Task List pane available in the left pane of the Agent Desktop.
                                 An agent can view the Queue Name, Phone Number, Source Number, Timer, and Accept button. The timer indicates the time elapsed
                                 since you were assigned the SMS conversation.

Before you begin

After you successfully sign in to the Manage Digital Channels on the Cisco Finesse desktop, the configured digital channels
                                 are in the Not Ready state. You must manually change your state from Not Ready to Ready to receive requests.

To respond to a chat :

Click the Accept button in the request. The request opens in the compose box, and an interaction pane is displayed.

The agent can then view the following details in the interaction pane:

Customer Name

Queue Name

Message Thread

Agent Name

Date

Timer

The customer’s messages are represented by a gray bubble with the initials of the customer name inside the bubble. A solid
                                                   blue bubble represents the agent messages.

Enter your response in the compose box.

The compose box supports a maximum of 1000 characters. Whenever the character count exceeds the configured limit, the Send button is disabled, and an error message is displayed below the composer box in red to correct the character limit.

Click Send or press CTRL + Enter .

The customer receives the response.

## Manage Chat Conversations

You can use digital chat channels such as Live Chat, Facebook Messenger, WhatsApp, and Apple Messages for Business digital
                              channels as Customer Support channels within Cisco Finesse. You can integrate Facebook Messenger as a customer support channel
                              in Cisco Finesse by connecting your Facebook pages.

Customers can initiate a coverstation with any of the supported digital channels with an agent and send chat messages. Agents
                              can then handle the chat and send a response to the customer from the chat widget on the Desktop.

The chat widget enables agents to respond to chat messages through the conversation pane.

You can use the desktop to transfer and end a chatconversation.

### About Chat widgets

For a list of features supported for the Live Chat, Facebook Messenger, and WhatsApp widgets and detailed instructions on
                                 how to use them, refer to Common Functionalities of Digital Channel Interactions .

### Respond to a Chat conversation

When a chat via a digital channel such as Live Chat, Facebook Messenger, WhatsApp, or Apple Messages for Business is assigned
                                 to an agent, if configured, the popover shows the customer's name, email, queue name, timer, and an accept button. The timer
                                 tracks how long it's been since the chat was received.

Before you begin:

After you successfully sign in to the Cisco Finesse Desktop, the configured digital channels are in the Not Ready state. You must manually change your state from Not Ready to Ready to receive requests.

To respond to a chat :

Click the Accept button in the request. The request opens in the compose box, and an interaction pane is displayed.

The agent can then view the following details in the interaction pane:

Customer Name

Queue Name

Message Thread

Agent Name

Date

Timer

The customer’s messages are represented by a gray bubble with the initials of the customer name inside the bubble. A solid
                                                   blue bubble represents the agent messages.

All previous conversations that the customer had with self-service or Bot is available to the agent.

Enter your response in the compose box.

The compose box supports a maximum of 1000 characters. Whenever the character count exceeds the configured limit, the Send button is disabled, and an error message is displayed below the composer box in red to correct the character limit.

Click Send or press Enter .

The customer receives the response.

## Manage Email conversations

The Email channel enables customers to send emails with tables, embedded links, and attachments.

The email widget enables agents to respond to email messages through the conversation pane.

You can use the desktop to respond, transfer, and end email conversations.

### About Email widget

For a list of features supported on the Email widget and detailed instructions on how to use them, refer to Common Functionalities of Digital Channel Interactions .

### Respond to an email conversation

Once you receive an email conversation, a popover appears on the bottom-right corner of the screen. The popover displays the
                                 Customers Name, Email ID, Account Number, Address, and Issue details.

Before you begin

To respond to a chat:

Click the Accept button in the request. The request opens in the composer box, and an interaction pane is displayed.

The agent can then view the following details in the interaction pane:

From email address

To email address

Email subject

Email thread (if any)

Timestamp and status of the email (Sent/Received/DRs)

Announcements

Attachments (if any, in the inbound email)

Reply, Reply All, Forward, and Cc icons

Transfer button

Click Send .

The customer receives the response.

### Send a reply

You can respond to add email by adding images and attachments or adding more recipients.

Before you begin

You must be in a Ready state to receive an email request.

Click Accept button in the email request. The request opens in the email composer, and an interaction pane is displayed.

Click the icon to expand and collapse each email and its history.

Select the Reply option to send a reply only to the sender or select the Reply All option to respond to all the recipients or select the Forward option to send it to a new recipient.

If you receive a new email while replying (to an email), a banner message View all messages to take further action appears
                                             above the email composer. The new email is shown in blue at the top of the thread.

When you Reply to an email, the To and Subject fields are auto-populated and cannot be edited.

When you Reply All to an email, the To and Subject fields are auto-populated and cannot be edited. The Cc field gets auto-populated.
                                             You can add or remove email ids in the Cc field. Moreover, you can hide the Cc field completely.

When you Forward an email, the subject field is auto-populated. You can add or remove email ids in the To and Cc fields. The
                                             email body gets loaded with the latest email in the composer.

When you switch from Reply to Reply All, the To and Cc fields are automatically populated. You can add or remove the email
                                             ids in the To and Cc fields. The email body is retained in the composer.

When you switch from Reply to Forward, the To and Cc field are emptied, and the email body is retained in the composer.

When you switch from Reply All to Forward, the To and Cc field are emptied, and the email body is retained in the composer.

When you switch from Reply All to Reply, the To field is automatically populated, the Cc field is emptied, and the email body
                                             is retained in the composer.

When you switch from Forward to Reply, the To field auto-populates, and the email body is retained in the composer.

When you switch from Forward to Reply All, the To and Cc fields auto populate, and the email body is retained in the composer.

When a user composes a message and doesn't send it, such email messages are saved as a draft and available in the composer.
                                             When a user composes a message and navigates/switches to another conversation without performing any action, such messages
                                             are saved as a draft and available in the composer until the user clears it manually.

(Optional) Click Cc to send a carbon copy of the email to more recipients.

Compose the email in the email body.

(Optional) You can apply Rich Formatting styles to the email body.

(Optional) You can add Email Attachments.

(Optional) You can attach Templates.

If you enter the text in the composer and then select a template, the existing text will be replaced with the template.

(Optional) You can Trigger Workflow.

You can click the Ellipses icon below the email body to view the complete history of the email conversation.

You can click Minimize icon to minimize the compose box.

You can click Maximize icon to maximize the compose box.

You can click Discard icon to discard an email.

Click Send .

## Common Functionalities of Digital Channel Interactions

Functionality

Email

SMS

Chat (Live Chat , Facebook Messenger, WhatsApp , Apple Messages for Business )

No

Yes

Yes

Yes

No

No

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

Yes

No

Yes

Yes

Yes

No

Yes

No

Respond to an Email Conversation

Yes

No

No

No

Yes

Yes

Delivery Receipts

No

Yes

No

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

### Text with attachments

An attachment is a file that is sent along with a text message.

To add a text attachment :

Agents can either Drag and Drop the attachments into the compose box or click the icon and browse the file to upload an attachment along with the response in the compose box.

You can send multiple attachments with a text message.

Agents can preview the file and its size before sending it to the customer.

Click the X icon to delete an attachment.

### Email attachments

An attachment is a file that is sent along with an email message. Attachments can be inline with the email body or attached
                                 as a regular attachment.

To add an email attachment:

Click the icon and browse the file to upload an attachment.

The administrator configures the maximum file size, formats, and the maximum number of files you can upload.

You can view and download the attachments from the received emails from the email thread.

Outbound attachments that do not fulfill the PCI rule will be dropped. Inbound attachments that fail to pass the PCI validation
                                             will be greyed out. When you select such attachments, a banner message is displayed above the email composer to inform the
                                             reason for the disabled attachment(s).

Agents can preview the file and its size before sending it to the customer.

Click the X icon to delete an attachment.

### Templates

Agents can use canned responses in the form of message templates. These templates help maintain consistency in agent responses
                                 and reduce the time taken to send commonly used messages.

#### Attach a template

To use a template in a conversation, follow these steps:

Click the (Template) icon in the compose box.

A modal with the list of configured template groups appears on the screen.

The All Templates tab consists of a list of all the templates configured for a team.

Click More to view the complete list of template groups configured for a team.

Select a template group to view the list of templates created under that template group.

Select the template. The respective information is loaded into the composer.

You can use the search field to filter the template names by entering a keyword in the search field and selecting a template
                                                      based on the results.

Click Send .

#### Locked templates

Administrators have the privilege to lock the templates while creating them on the Webex Engage Admin Console. You can view
                                    the (Lock) icon beside the locked templates. You can use these locked templates as-is and cannot edit these templates. If you
                                    try to perform an edit action, an error message will appear on the screen.

#### Templates with replaceable parameters

Administrators can create templates with replaceable parameters for agents to send personalized messages to the customers.
                                    You can load these templates into the composer and use the Tab key to traverse between the replaceable parameters and change
                                    them.

#### Templates with dynamic substitution of system parameters in the agent desktop

You can use the templates that administrators configure with system parameters in the template body. When these templates
                                    are used in the chat conversations, the respective system parameters are dynamically substituted in the composer.

### Rich formatting in social channels

You can click the (formatting) icon to apply rich formatting styles to the Social Channels text before replying to the message. You can select
                                 the required rich formatting style from the list above the compose box for email channel text before replying to the message.

You can apply the following rich formatting styles to the reply message in the compose box:

Formatting Style

Description

Bold

Makes the text bold

Italics

Italicizes the text

Strikethrough

Draws a line through the text

You can apply only one style to the selected text. For example, if you choose to make a certain word or sentence bold, you
                                             cannot italicize the same.

### Rich formatting in email messages

You can apply the following rich formatting styles to the reply message in the email body:

Formatting Style

Description

Heading 1

Applies a pre-set font and style to the text.

Bold

Makes the text bold.

Italics

Italicizes the text.

Underline

Underlines the text.

Strikethrough

Draws a line through the text.

Font color

Changes the font color.

List by ordered

Creates an ordered list.

List by bullet

Creates a bulleted list.

Blockquote

Indents the text and marks it as a quotation with a vertical line at the left margin.

Emojis

Inserts an emoji.

Link

Inserts a hyperlink on the selected text.

Indent left

Indents the text to the left.

Indent right

Indents the text to the right.

Table

Inserts a table in the text area.

### Trigger workflows

Workflow is an automation and fulfilment framework geared towards automation in the contact center. Workflow can be running
                                 an API call or JavaScript code triggered on demand by an agent on the Agent Desktop.

You can easily integrate Cisco Finesse Gadget with external systems to ensure that customer records are synchronized in real
                                 time. This can be achieved with the help of workflows. You can trigger these workflows when you are in the middle of a conversation
                                 with the customer.

To trigger a workflow, follow these steps:

Click the (Trigger workflow) icon in the compose box for Social Channels and above the compose box for the email channel.

A pop-up window with the list of pre-configured workflows appears on the screen.

Select a workflow and click the Trigger button.

If the workflow has been configured to accept input parameters from the agent, a pop-up window appears. Enter the required
                                       parameters and click the Trigger button.

Once the workflow is triggered, an audit trail in the form of an announcement is appended to the chat thread.

Click Send .

### Announcements

You can view audit trails of conversation lifecycle events/ journey milestone summaries (appended via the Append conversation
                                 node) with the help of announcements. You can view the announcements in the chat thread on the Agent Desktop.

When a conversation is CLOSED, the announcement "Conversation CLOSED" is displayed with the timestampin in the chat thread.

### Delivery receipts

A delivery receipt is recorded against each outbound message in the message thread whenever you send a message to the customer.

### Typing area

By default, the Typing area appears below the Interaction pane. Use this area to type the messages. Click Enter or click Send to send the messages to the customers. Emojis and attachment icons are available for interaction. The following are the options
                                 that are available for each channel:

Digital Channel

Option

Live Chat

Attachment

Emoji

Event trigger

SMS

Emoji

Event trigger

Template

Facebook Messenger

Emoji

Event trigger

Template

WhatsApp

Emoji

Event trigger

Template

Apple Messages for Business

Attachment

Rich Text

Emoji

Event trigger

Template

Email

Attachment

Rich Text

Emoji

Event trigger

### End interactions

Click End to close an interaction.

If force wrap-up is not enabled, the interaction closes successfully and the focus is shifted to the latest accepted interaction.

If force wrap-up is enabled, a reverse-timer starts on the Wrap-up Reasons drop-down. A disabled Close button appears on the right side of the Wrap-up Reasons drop-down.

Select an appropriate wrap-up reason. A green button appears on the Wrap-up Reasons drop-down. The Close button is enabled.

Click Close to close the interaction. Else, after the timer reaches zero, the interaction is closed automatically.

### Transfer interactions

While interacting with customers, you can transfer the interactions to one of the configured route points. If you get a voice
                                 call and accept the call, you may experience one of the following as per the configuration:

The Transfer button is disabled and the timer of the interaction is stopped.

The Transfer button is available and the timer continues.

When you get a voice call, the behavior of Transfer may vary for each digital channel (Live Chat, SMS, Email, Facebook Messenger, WhatsApp, and Apple Messages for Business).
                                             This change depends on the configuration of the respective media set as interruptible or non-interruptible.

Step 1

Click Transfer .

The list of available route points aren't the same as that of the voice phone book that is available on the desktop.

Step 2

If force wrap-up is configured, select an appropriate wrap-up reason from the Wrap-up Reasons list, and click Apply .

A green button appears on the Wrap-up Reasons drop-down.

Step 3

Select the required route point to transfer the interaction.

When interactions are transferred and an agent accepts from the queue, all previous interactions between the customer and
                                                         the previous agents are available for the new agent.

## Keyboard Shortcuts

Use the keyboard shortcuts for easy access to the Manage Digital Channels gadget. The keyboard shortcuts are available for both agents and supervisors.

Group

Action

Shortcut Key

Notes

Interaction Control

Expand/Collapse

Ctrl + Alt + 8

—

Agent State

Ready for Email

Ctrl + Shift + 4

—

Ready for Chat/Social Channels

Ctrl + Shift + 5

—

Not Ready for Email

Ctrl + Shift + 6

—

Not Ready for Chat/Social Channels

Ctrl + Shift + 7

—

Task List

Shift focus to the next active task

Ctrl + Shift + 8

—

Shift the focus to the previous task

Ctrl + Shift + 9

—

Send Chat/Social Channels messages

Send Chat and SMS

Ctrl + Enter (in Windows)

OR

Cmd + Enter (in Mac)

—

Application

Expand/Collapse the Task Panel

Ctrl + Alt + T

—

Ready for All Digital Channels

Ctrl + Shift + V

—

Open Digital Channels State Control

Ctrl + Shift + L

—

Not Ready for All Digital Channels

Ctrl + Shift + Z

—

Call Handling and Digital Handling

Answer/Accept Call

Accept for all digital channels

Ctrl + Alt + 9

—

## Finesse Failover

If the Finesse server that you’re currently signed-in to goes out of service, a banner appears at the top of the desktop notifying
                              that the desktop has lost connection to the server. After reconnecting (failover or failback), the Manage Digital Channels
                              gadget and the state controls are unavailable. The gadget is unavailable to the users until it is able to determine and retain
                              the previous state across all the channels. The desktop reload starts only after a healthy connection is reestablished with
                              the Finesse server.

The agents state and the tasks that they are working on are retained after the failover or failback. The call variables and
                              wrap-up reasons selected and the timers for how long the agents are active on a particular task are retained.

After restarting the Cisco Finesse Tomcat service or Finesse server post-maintenance, the agents handling active Chat or Social
                                          Media Routing Domain (MRD) tasks may see a Connection Failure with a yellow exclamation mark in Finesse Notification Center (FNC). To fix this, the agents must manually select the Chat
                                          and Social channels and set their FNC status to Ready .

For more information about failover, see the Finesse Desktop Failover section in the Cisco Finesse Agent and Supervisor Desktop User Guide .

## Accessibility

Cisco Finesse Desktop supports a robust set of accessibility features to ensure that all users can interact with the Finesse
                           desktop effectively. The following sections outline the new enhancements and best practices that align with the Web Content
                           Accessibility Guidelines (WCAG) and other accessibility standards.

Cisco Finesse Desktop adopts the Web Content Accessibility Guidelines (WCAG) 2.1, Level A and Level AA. For more information,
                           refer to https://www.cisco.com/c/en/us/about/accessibility.html . They provide recommendations to make web content more accessible to users with vision, hearing, and cognitive impairments,
                           enhancing overall usability.

The following are the various accessibility enhancements in Cisco Finesse Desktop:

Web Accessibility

Screen Reader Support

Localization

Color Contrast

Focus Indicators

Display Headers, Titles and Accessible Labels

Display Tool-tips on Hover

If you are using Mac keyboard, then press Option instead of Alt . For example, for Language Selector Drop-Down press Option–Down Arrow.

### Screen Reader Support

Cisco Finesse also supports JAWS screen reading software for the following elements.

For more information on the supported JAWS version, see Voluntary Product Accessibility Templates (VPAT) report for Contact
                              Center at https://www.cisco.com/c/en/us/about/accessibility/voluntary-product-accessibility-templates.html .

### Localization

Cisco Finesse Desktop supports the localization of labels. This ensures that users who rely on screen readers or other assistive
                              technologies can accurately identify and interact with these elements, regardless of the language or regional settings.

### Color Contrast

High color contrast is crucial for users with visual impairments, including color blindness. Cisco Finesse desktop ensures
                              a contrast ratio of at least 4.5:1 for normal text and 3:1 for large text and a contrast ratio of at least 3:1 for graphics
                              and user interface components, as recommended by WCAG. The application avoids using color as the sole method of conveying
                              information and conducts regular testing to ensure compliance with contrast requirements.

### Focus Indicators

Focus indicators are visual markers that help users navigate through the application using a keyboard. Cisco Finesse desktop
                              provides clear and consistent focus indicators for all interactive elements.

Keyboard Navigation : Users can navigate through all interactive elements using the Tab key or other keyboard shortcuts.

Visible Focus Indicators : When an element receives focus, a visible outline or highlight is displayed to indicate that it is active.

### Display Headers, Titles, and Accessible Labels

Properly structured headers, titles, and labels are crucial for accessibility, as they help users navigate content more easily.
                              Cisco Finesse desktop ensures that all pages and sections are appropriately labeled and organized.

Hierarchical Structure : Headers are used to organize content hierarchically, allowing screen reader users to navigate through sections efficiently.

Descriptive Titles : Page titles and section headers are descriptive, providing users with a clear understanding of the content.

Accessible Labels : Form fields and interactive elements are labeled with clear and descriptive text, ensuring that all users can understand
                                    their purpose.

Cisco Finesse Desktop provides accessible labels for drop-down list with values identical to their visual labels to provide
                                    a consistent experience for all users, including those using screen readers. This alignment helps both visual and non-visual
                                    users to have the same experience.

### Display Tooltips on Hover

Tooltips provide additional information about interface elements when a user hovers over them. Cisco Finesse desktop supports
                              accessible tooltips that are easily readable and discoverable.

Tooltips appear when users hover over or focus on an element, making them accessible to both mouse users and those navigating
                              via keyboard. They are designed with sufficient contrast and displayed in a readable font size, ensuring readability. Additionally,
                              tooltips are announced by screen readers when the associated element receives focus, providing access to the same information
                              for users relying on assistive technology.

| Note | To sign out of Finesse desktop, all the channels (voice and digital) must be in Not Ready state. |
|---|---|

| Step 1 | Sign in to Finesse desktop. |
|---|---|
| Step 2 | From the left pane, select Manage Digital Channels . The Manage Digital Channels Sign In dialog appears. |
| Step 3 | Click Sign In . The gadget signs in to all the digital channels ( Chat/Social Channels and Email ) that are configured for the user. The digital channel icons that are available at the top of the window, display your status. After you successfully sign in, by default all the digital channels are in Not Ready state. Note When there's a sign-in failure for any of the media types, notifications appear with the sign-in failure reason. Sign-in is
                                                      retried automatically for the configured number of times. | Note | When there's a sign-in failure for any of the media types, notifications appear with the sign-in failure reason. Sign-in is
                                                      retried automatically for the configured number of times. |
| Note | When there's a sign-in failure for any of the media types, notifications appear with the sign-in failure reason. Sign-in is
                                                      retried automatically for the configured number of times. |
| Step 4 | Click the drop-down arrow next to the Chat/Social Channels and Email icons. The following list appears: All Chat/Social Channels Email Under each channel, there's an option to move the channel to Ready or Not Ready state. The Not Ready reasons for voice and digital channels are the same. Note The drop-down doesn't list the already selected reason. For example, if the status is Not Ready Lunch , this option isn't listed. Figure 1. Digital Channels State Change Selection | Note | The drop-down doesn't list the already selected reason. For example, if the status is Not Ready Lunch , this option isn't listed. |
| Note | The drop-down doesn't list the already selected reason. For example, if the status is Not Ready Lunch , this option isn't listed. |
| Step 5 | Select Ready to be available for the required digital channel. |

| Note | When there's a sign-in failure for any of the media types, notifications appear with the sign-in failure reason. Sign-in is
                                                      retried automatically for the configured number of times. |
|---|---|

| Note | The drop-down doesn't list the already selected reason. For example, if the status is Not Ready Lunch , this option isn't listed. |
|---|---|

| Note | The number of tasks that are presented to you for each digital channel (LiveChat, SMS, Email, Facebook Messenger, WhatsApp,
                                             and Apple Messages for Business is configured by your administrator. Different media may have different accept timers as per the configuration. |
|---|---|

| Media Notification | State Change to Not Ready | Notes |
|---|---|---|
| Email | Email | Only Email channel is changed to the Not Ready state. |
| Live Chat | Chat/Social Channels | First the Live Chat becomes Not Routable and then all the media under Chat/Social Channels are changed to the Not Ready state. |
| SMS | When Live Chat is set up alongside other social media channels, Live Chat switches to "Not Ready" before the others. However,
                                          if Live Chat and social media channels are mapped to the same MRD, the state change happens instantly. |
| Facebook Messenger |
| WhatsApp |
| Apple Messages for Business |

| Note | When the Task window is loaded, if you accept a voice call, the voice channel displays at the top and the Task window is pushed down. This happens only when the voice channel is configured as a page level gadget. |
|---|---|

| Note | This field is always in bold font. |
|---|---|

| Note | The customer’s messages are represented by a gray bubble with the initials of the customer name inside the bubble. A solid
                                                   blue bubble represents the agent messages. |
|---|---|

| Note | The compose box supports a maximum of 1000 characters. Whenever the character count exceeds the configured limit, the Send button is disabled, and an error message is displayed below the composer box in red to correct the character limit. |
|---|---|

| Note | The customer’s messages are represented by a gray bubble with the initials of the customer name inside the bubble. A solid
                                                   blue bubble represents the agent messages. All previous conversations that the customer had with self-service or Bot is available to the agent. |
|---|---|

| Note | The compose box supports a maximum of 1000 characters. Whenever the character count exceeds the configured limit, the Send button is disabled, and an error message is displayed below the composer box in red to correct the character limit. |
|---|---|

| Functionality | Email | SMS | Chat (Live Chat , Facebook Messenger, WhatsApp , Apple Messages for Business ) |
|---|---|---|---|
| Text Attachments | No | Yes | Yes |
| Email Attachments | Yes | No | No |
| Attach a Template | No | Yes | Yes |
| Locked Templates | Yes | Yes | Yes |
| Templates with Replaceable Parameters | Yes | Yes | Yes |
| Templates with Dynamic Substitution of System Parameters in the Agent Desktop | Yes | Yes | Yes |
| Rich Formatting in Email Messages | No | Yes | No |
| Trigger Workflows | Yes | Yes | Yes |
| Respond to SMS Conversation | No | Yes | No |
| Respond to an Email Conversation | Yes | No | No |
| Announcements | No | Yes | Yes |
| Delivery Receipts | No | Yes | No |
| Keyboard Shortcuts | Yes | Yes | Yes |
| Transfer Conversation | Yes | Yes | Yes |
| End Conversation | Yes | Yes | Yes |

| Note | You can send multiple attachments with a text message. |
|---|---|

| Note | You can use the search field to filter the template names by entering a keyword in the search field and selecting a template
                                                      based on the results. |
|---|---|

| Formatting Style | Description |
|---|---|
| Bold | Makes the text bold |
| Italics | Italicizes the text |
| Strikethrough | Draws a line through the text |

| Note | You can apply only one style to the selected text. For example, if you choose to make a certain word or sentence bold, you
                                             cannot italicize the same. |
|---|---|

| Formatting Style | Description |
|---|---|
| Heading 1 | Applies a pre-set font and style to the text. |
| Bold | Makes the text bold. |
| Italics | Italicizes the text. |
| Underline | Underlines the text. |
| Strikethrough | Draws a line through the text. |
| Font color | Changes the font color. |
| List by ordered | Creates an ordered list. |
| List by bullet | Creates a bulleted list. |
| Blockquote | Indents the text and marks it as a quotation with a vertical line at the left margin. |
| Emojis | Inserts an emoji. |
| Link | Inserts a hyperlink on the selected text. |
| Indent left | Indents the text to the left. |
| Indent right | Indents the text to the right. |
| Table | Inserts a table in the text area. |

| Digital Channel | Option |
|---|---|
| Live Chat | Attachment Emoji Event trigger |
| SMS | Emoji Event trigger Template |
| Facebook Messenger | Emoji Event trigger Template |
| WhatsApp | Emoji Event trigger Template |
| Apple Messages for Business | Attachment Rich Text Emoji Event trigger Template |
| Email | Attachment Rich Text Emoji Event trigger |

| Note | When you get a voice call, the behavior of Transfer may vary for each digital channel (Live Chat, SMS, Email, Facebook Messenger, WhatsApp, and Apple Messages for Business).
                                             This change depends on the configuration of the respective media set as interruptible or non-interruptible. |
|---|---|

| Step 1 | Click Transfer . The Transfer drop-down lists the route points that are configured for the specific media type. Note The list of available route points aren't the same as that of the voice phone book that is available on the desktop. | Note | The list of available route points aren't the same as that of the voice phone book that is available on the desktop. |
|---|---|---|---|
| Note | The list of available route points aren't the same as that of the voice phone book that is available on the desktop. |
| Step 2 | If force wrap-up is configured, select an appropriate wrap-up reason from the Wrap-up Reasons list, and click Apply . A green button appears on the Wrap-up Reasons drop-down. |
| Step 3 | Select the required route point to transfer the interaction. The interaction is moved to the selected route point and moves out of your list. Note When interactions are transferred and an agent accepts from the queue, all previous interactions between the customer and
                                                         the previous agents are available for the new agent. | Note | When interactions are transferred and an agent accepts from the queue, all previous interactions between the customer and
                                                         the previous agents are available for the new agent. |
| Note | When interactions are transferred and an agent accepts from the queue, all previous interactions between the customer and
                                                         the previous agents are available for the new agent. |

| Note | The list of available route points aren't the same as that of the voice phone book that is available on the desktop. |
|---|---|

| Note | When interactions are transferred and an agent accepts from the queue, all previous interactions between the customer and
                                                         the previous agents are available for the new agent. |
|---|---|

| Group | Action | Shortcut Key | Notes |
|---|---|---|---|
| Interaction Control | Expand/Collapse | Ctrl + Alt + 8 | — |
| Agent State | Ready for Email | Ctrl + Shift + 4 | — |
| Ready for Chat/Social Channels | Ctrl + Shift + 5 | — |
| Not Ready for Email | Ctrl + Shift + 6 | — |
| Not Ready for Chat/Social Channels | Ctrl + Shift + 7 | — |
| Task List | Shift focus to the next active task | Ctrl + Shift + 8 | — |
| Shift the focus to the previous task | Ctrl + Shift + 9 | — |
| Send Chat/Social Channels messages | Send Chat and SMS | Ctrl + Enter (in Windows) OR Cmd + Enter (in Mac) | — |
| Application | Expand/Collapse the Task Panel | Ctrl + Alt + T | — |
| Ready for All Digital Channels | Ctrl + Shift + V | — |
| Open Digital Channels State Control | Ctrl + Shift + L | — |
| Not Ready for All Digital Channels | Ctrl + Shift + Z | — |
| Call Handling and Digital Handling | Answer/Accept Call Accept for all digital channels | Ctrl + Alt + 9 | — |

| Note | After restarting the Cisco Finesse Tomcat service or Finesse server post-maintenance, the agents handling active Chat or Social
                                          Media Routing Domain (MRD) tasks may see a Connection Failure with a yellow exclamation mark in Finesse Notification Center (FNC). To fix this, the agents must manually select the Chat
                                          and Social channels and set their FNC status to Ready . |
|---|---|

| Note | If you are using Mac keyboard, then press Option instead of Alt . For example, for Language Selector Drop-Down press Option–Down Arrow. |
|---|---|