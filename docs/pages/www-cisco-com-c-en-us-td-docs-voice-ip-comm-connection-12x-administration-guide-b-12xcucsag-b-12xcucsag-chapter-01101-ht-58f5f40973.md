---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-administration-guide-b-12xcucsag-b-12xcucsag-chapter-01101-ht-58f5f40973
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag/b_12xcucsag_chapter_01101.html
retrieved_at: 2026-08-17T02:31:44.350002+00:00
---

System Administration Guide

# System Administration Guide

Updated: August 1, 2017

Chapter: Notifications

## Chapter: Notifications

# Notifications

## Introduction

Cisco Unity Connection allows the users to be notified of the incoming voice messages and emails as soon as the message arrives
                           in the user mailbox.

Following are some of the types of notifications received by users:

Users receive message alerts through text notifications on pager.

Users receive a call on their configured phones to get notified about new messages.

Users receive messages and calendar notifications in the form of SMS messages to wireless devices using SMPP.

Users receive messages and missed call notifications as plain text or HTML emails.

User receives summary and scheduled summary of latest voicemail as HTML emails.

The notifications for events are delivered to the end users through various notification devices. The notification devices
                           can be enabled or disabled by the administrator for individual or multiple users through Cisco Unity Connection Administration
                           and a user can override their specific notification device settings through Messaging Assistant feature of Cisco Personal
                           Communications Assistant.

## Default Notification Devices

Unity Connection comes with a set of default notification devices that can be configured as required.

Following are the default notification devices:

Pager: Allows users to receive voice message alerts as a text notification.

Work Phone: Allows users to receive voice message alerts as a dial out call on work phone.

Home Phone: Allows users to receive voice message alerts as a dial out call on home phone.

Mobile Phone: Allows users to receive voice message alerts as a dial out call on mobile phone.

SMTP: Allows users to receive voice message alerts as an email notification.

HTML: Allows users to receive voice message alerts as an HTML email notification.

HTML Missed Call: Allows users to receive missed call alerts as an HTML email notification.

HTML Scheduled Summary: Allows users to receive summary of latest voice messages at a configured time as an HTML email notification.

The notification devices can be modified or enabled but cannot be deleted. An administrator can add, edit, or delete additional
                           notification devices whereas, a user can only edit the notification devices.

Caution

Do not change the display name of  default notification devices.

Missed call event type is pre-checked under Notify me of section of an HTML device when “Default_Missed_Call” template is
                                       used. Similarly, when “Default_Scheduled_Summary” template is used with HTML device, all the event types are un-checked.

User should not use the default notification devices in CSV file while using Bulk Administration Tool.

## Configuring
                        	 Notification Devices

Message notification settings for each user account or user
                              		  template allows you to control how and when Unity Connection notifies a user of
                              		  new messages. User accounts and user templates include notification devices for
                              		  a home phone, mobile phone, work phone, and one pager. Users can also use the
                              		  Messaging Assistant to set up phones and pagers to receive message
                              		  notifications.

Step 1

In Cisco Unity Connection Administration, find the user account
                                       			 that you want to edit.

Step 2

On the Search User Basics page of the user account, select the
                                       			 user account that you want to edit.

Step 3

On the Edit User Basics page, in the Edit menu, select
                                       			 Notification Devices.

Step 4

Configure a notification device.(Phone, Pager, SMTP, HTML, SMS)
                                       			 (For more information on each field, see Help> This Page)

To add a notification device:

On the Edit User Basics page, select Edit> Notification
                                                      						  Devices.

On the Notification Devices page, select Add New.

On the New Notification Device page, enter the fields as
                                                      						  applicable depending on the notification device you selected and Save.

To edit a notification device:

On the Edit User Basics page, select Edit> Notification
                                                      						  Devices.

On the Notification Device page, select the notification device
                                                      						  that you want to edit.

On the Edit Notification Device page, edit the required settings
                                                      						  and Save.

You can also schedule Bulk Edit for a later period using Bulk
                                                            						Edit Task scheduling and select Submit.

To delete one or more notification devices:

On the Edit User Basics page, select Edit> Notification
                                                      						  Devices.

On the Notification Device page, select the notification devices
                                                      						  you want to delete.

Select Delete Selected and OK to confirm deletion.

Similarly, you can configure the notification devices associated
                                                            						with a particular user template.

## Cascading Message Notification

Cascading message notification allows you to send notifications to a wide circle of recipients. Unity Connection continues
                           to send notifications until the message has been saved or deleted by a recipient.

For example, to create a cascade of message notifications for your Technical Support department, set the first message notification
                           to be sent immediately to the pager of the front-line technical support representative. If the message that triggered the
                           first notification has not been saved or deleted, then after a delay of 15 minutes, the next notification can be sent to the
                           pager of the department manager. A third notification can be set up to call an employee in the Problem Resolution Group if
                           the message is not saved or deleted after 30 minutes, and so on.

When a user receives a notification as part of the cascade, the notification prompts the user to sign in to the mailbox that
                                       is being monitored by the cascade.

An alternative to cascading message notification is to use dispatch messaging. For details, see the Dispatch Messages, page 11-3 section.

### Task List for
                           	 Cascading Message Notification

### SUMMARY STEPS

- For the first recipient in
                                 			 the notification chain, you need to set up the notification device in the
                                 			 following way:

- For each of the other recipients in the notification chain, you
                                 			 can repeat step 1 to setup the device till you reach the end
                                 			 of recipient list.

### DETAILED STEPS

Step 1

For the first recipient in
                                          			 the notification chain, you need to set up the notification device in the
                                          			 following way:

- Find the user account
                                                				  or user template to configure with chaining notifications.

- In the Notification
                                                				  Devices page for the user or template, for On Notification Failure, select Send
                                                				  To, and select the device that you want Unity Connection to notify next if
                                                				  notification to the device fails.

Uncheck all Notification Rule Events check boxes. If you
                                                   					 enable any notification events, message notification for the device starts
                                                   					 immediately and does not wait for the notification failure of the previous
                                                   					 device. Your notifications do not chain, they all trigger at once.

If you want to chain to a third device if notification to the
                                                   					 device fails, select Send To and the device that you want Unity Connection to
                                                   					 notify next if notification to the device fails. If not, select Do Nothing.

Step 2

For each of the other recipients in the notification chain, you
                                          			 can repeat step 1 to setup the device till you reach the end
                                          			 of recipient list.

## Chaining Message Notification

Message notification can be set to “chain” to a series of notification devices if an attempt to send a notification to the
                           first selected device fails. A failure occurs when a notification device is not answering or is busy and the retry attempts
                           to reach that device using various options has also failed

Do not configure SMTP devices for chaining message notification, except as the last device in the chain. Unity Connection
                                       does not detect notification failure for SMTP devices.

### Task List for
                           	 Chaining Message Notification

### SUMMARY STEPS

- For the first
                                 			 recipient in the notification chain, you need to set up the notification device
                                 			 in the following way:

- For each of
                                 			 the other recipients in the notification chain, you can repeat step 1 to setup the device till you reach the end
                                 			 of recipient list.

### DETAILED STEPS

Step 1

For the first
                                          			 recipient in the notification chain, you need to set up the notification device
                                          			 in the following way:

- Find the user account or
                                                				  user template to configure with chaining notifications.

- In the Notification Devices
                                                				  page for the user or template, for On Notification Failure, select Send To, and
                                                				  select the device that you want Unity Connection to notify next if notification
                                                				  to the device fails.

Uncheck
                                                   					 all Notification Rule Events check boxes. If you enable any notification
                                                   					 events, message notification for the device starts immediately and does not
                                                   					 wait for the notification failure of the previous device. Your notifications do
                                                   					 not chain, they all trigger at once.

If you
                                                   					 want to chain to a third device if notification to the device fails, select
                                                   					 Send To and the device that you want Unity Connection to notify next if
                                                   					 notification to the device fails. If not, select Do Nothing.

Step 2

For each of
                                          			 the other recipients in the notification chain, you can repeat step 1 to setup the device till you reach the end
                                          			 of recipient list.

## Setting Up SMTP Message Notification

Cisco Unity Connection can notify a user of new messages by calling a phone or pager. Also, you can set up Unity Connection
                           to send message and calendar event notifications in the form of text messages to text pagers and text-compatible mobile phones
                           using SMTP.

Users can receive notification of new messages by email. Unity Connection supports two types of notification emails: plain
                                       text using SMTP notification devices; or HTML using HTML notification devices. HTML notifications can only be used for new
                                       voice mail. For other types of messages, you must use plain text SMTP notifications. To enhance security, both types of devices
                                       require connection to an SMTP smart host.

### Enabling SMTP Notification

Step 1

Configure the SMTP smart host to accept
                                          			 messages from the Unity Connection server. See the documentation for the SMTP
                                          			 server application that you are using.

Step 2

Configure the Unity Connection server. See
                                          			 the Configuring
                                             				the Unity Connection Server to Relay Messages to a Smart Host section.

Step 3

Configure Unity Connection user accounts or
                                          			 user templates. See the Configuring Notification Devices,
                                             				page 14-2 section.

### Configuring the Unity Connection Server to Relay Messages to a Smart
                           	 Host

Step 1

In Cisco Unity Connection Administration, expand System Settings > SMTP Configuration, then select Smart Host.

Step 2

On the Smart Host page, in the Smart Host field, enter the IP address or fully qualified domain name of the SMTP smarthost
                                          server, for example, https://<domain name of server>.cisco.com. (Enter the fully qualified domain name of the server only
                                          if DNS is configured.)

The Smart Host can contain up to 50 characters.

Step 3

Select Save.

If the Unity Connection server has not been properly enabled to use SMTP smart host for message notification, it places SMTP
                                                         notification messages in the Unity Connection SMTP server badmail folder

## Setting Up SMS
                        	 Message Notification

With the services and information provided by a wireless
                           		carrier, mobile messaging service provider, Unity Connection can use the Short
                           		Message Peer-to-Peer (SMPP) protocol to send message notifications in the Short
                           		Message Service (SMS) format to mobile phones and other SMS-compatible devices
                           		when users receive new messages.

Advantages Over SMTP Message Notifications

An advantage of using SMS is that the user device often receives
                           		message notifications much faster than when using SMTP. You can configure Unity
                           		Connection so that each SMS notification message replaces the previous one.
                           		Note that this functionality may not be supported by all mobile service
                           		providers.

SMS Message Length Limitations

The acceptable message length for an SMS message varies
                           		depending on the service provider, the character set used to compose the
                           		message text, and the specific characters used in the message text.

Character sets available include:

Default alphabet (GSM 3.38), 7-bit characters

IA5/ASCII, 7-bit characters

Latin 1 (ISO-8859-1), 8-bit characters

Japanese (JIS), multi-byte characters

Cyrillic (ISO-8859-5), 8-bit characters

Latin/Hebrew (ISO-8859-8), 8-bit characters

Unicode (USC-2), 16-bit characters

Korean (KS C 5601), multi-byte characters

For 7-bit character sets, a maximum of 160 characters can fit
                           		into an SMS message; for 8-bit character sets, the limit is 140 characters; for
                           		16-bit character sets, the limit is 70 characters; for multi-byte character
                           		sets, the limit is somewhere between 70 and 140 characters, depending on which
                           		characters make up the text of the message. (For multi-byte character sets,
                           		most characters are 16 bits; some of the more common characters are eight
                           		bits.)

Not all mobile phones support all character sets; most support
                                       		  the GSM 3.38 default alphabet.

Cost Considerations

The cost of setting up SMS(SMPP) message notifications depends
                           		directly on the number of SMS notifications that Unity Connection sends to user
                           		devices. More SMS notification implies higher cost as the service providers
                           		typically charge for each SMS message or group of messages sent.

To cut down cost, you can restrict the use SMS notifications to
                           		a group of users or inform users to limit the number of message notifications
                           		that they receive by message type or urgency. For example, users can specify in
                           		the Messaging Assistant that Unity Connection sends message notifications only
                           		when new urgent voice messages arrive.

### Enabling SMS Message Notifications

Step 1

Set up an account with a mobile messaging
                                          			 service provider that offers SMS messaging. Unity Connection supports the SMPP
                                          			 version 3.3 or SMPP version 3.4 protocols.

Step 2

Gather the information needed to allow Unity
                                          			 Connection to communicate with the SMPP server at the SMSC affiliated with your
                                          			 contracted service provider, and enter the information on the SMPP Provider
                                          			 page. See the To Set Up an SMPP Provider.

Step 3

When the Unity Connection server is set up
                                          			 behind a firewall, configure the TCP port used by the SMPP server when
                                          			 connecting to Unity Connection.

Step 4

Enable the SMPP provider on Cisco Unity
                                          			 Connection Administration. See the Setting Up an SMPP Provider,
                                             				page 14-6 section.

Step 5

Configure SMS message notification, set up
                                          			 an SMS notification device to receive notifications for a test user account.
                                          			 See the Configuring Notification Devices,
                                             				page 14-2 section.

### Setting Up an SMPP Provider

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced, then select SMPP Providers.

Step 2

On the Search SMPP Providers page, select
                                          			 Add New.

Step 3

Enable the new provider and enter the Name,
                                          			 System ID and Hostname of the provider and Save. For more information on
                                          			 settings, select Help > This Page).

Step 4

On the Edit SMPP Provider page, enter the
                                          			 Port, which is the TCP port number that is used by the SMSC to listen for
                                          			 incoming connections.

The port number should be in range of
                                                         				  >100 and <=99999.

## Setting Up HTML Message Notification

The HTML notification is triggered based on the HTML notification device settings and is received on the configured email
                           address.

The administrator can create or edit the content and format of the HTML notifications using notification templates, custom
                           variables, and custom graphics. Unity Connection sends HTML notifications to an email server over SMTP in the IPv4 mode only. Therefore,
                           the administrator must ensure that the HTML notifications are configured over IPv4.

Users can configure different types of HTML notifications:

HTML notification when a new voice message is received.

HTML notification when a new missed call is received.

HTML notification when a new voice message is received along with the summary of latest voice messages.

HTML notification when a new missed call is received along with the summary of latest voice messages

HTML notification at a configured time containing the summary of latest voice messages.

HTML notification configured for interview handler will contain the attachment of the last question answer.

### Notification Templates

HTML notification template includes the following:

Free flow HTML text.

HTML tags, the support of which depend on the email client that the user is using.

Custom Variables and Custom Graphics.

Status Items for Voice Message - MWI, Message Status as Icons within an HTML template.

Embedded links to external URIs or URLs.

#### Default Notification Templates

The default templates for HTML message notification are:

Default_Actionable_Links_Only template has the HTML tags along with the actionable links without any images, custom graphics,
                                       or status items. For example, the administrators can configure the HTML templates to include header, footer, logos, images,
                                       and hyperlinks to Mini Web Inbox.

Default_Dynamic_Icons template has the HTML tags along with the custom graphics and the status items. It allows Unity Connection
                                       to send details of new voicemail containing actionable links with image and message status.

Default_Missed_Call template allows Unity Connection to send details of missed call including timestamp and sender details.

Default_Voice_Message_With_Summary template allows Unity connection to send notification when a new voice message is received
                                       along with the summary of latest voicemails.

Default_Missed_Call_With_Summary template allows Unity Connection to send notification when a new missed call is received
                                       along with the summary of latest voicemails.

Default_Scheduled_Summary allows Unity Connection to send summary of voice messages at configured time(s) daily.

The administrator can assign a notification template to the users or can allow the users to select a template. But the users
                                 do not have the permissions to create or edit a template.The template selected can either be a default or a custom template
                                 that the administrator has created.

The use of images, MWI status, and Message status is not mandatory. However, if used, the administrators need to ensure that
                                             the image rendering when used with the HTML tags and the APIs is supported by their respective email clients.

#### Configuring
                              	 Notification Templates

Notification templates can be created, modified, and deleted
                                    		  that include status items, action items, static items, custom variables, custom
                                    		  graphics, and collection tags.

Step 1

In Cisco Unity Connection Administration, expand Templates >
                                             			 Notification Templates and select Notification Templates. The Search
                                             			 Notification Templates page appears displaying the list of currently configured
                                             			 templates.

Step 2

Configure notification template. (For more information on each
                                             			 field, see Help> This Page)

Select Add new and New Notification Template page appears.

Enter the Display name and HTML content.

Select and copy the required status, action, and/or static items
                                                            						  from the left panel of the HTML field and paste the items on the right panel.
                                                            						  See the table 14-1 for more information.

Description of Notification Templates

Items

Description

%MWI_STATUS%

Displays the image based on
                                                                        										MWI status.The default images are displayed as defined in the Administrative
                                                                        										Replaceable Images section.To insert the status items directly in the
                                                                        										notification template, you can use the <img src=”%MWI_STATUS%”>
                                                                        										</img> tag.

%MESSAGE_STATUS%

Displays the message status
                                                                        										as unread, read, unread urgent, read urgent, or deleted.The default images are
                                                                        										displayed as defined in the Administrative
                                                                           										  Replaceable Images, page 14-13 section.

To insert the status items
                                                                        										directly in the

notification template, you
                                                                        										can use the <img

src="%MESSAGE_STATUS%">
                                                                        										</img>tag.

%LAUNCH_MINI_INBOX%

Launches the Unity
                                                                        										Connection Mini Web Inbox. To insert this item directly in the notification
                                                                        										template, you can use the <a href="%LAUNCH_MINI_INBOX%"> Text
                                                                        										</a>tag.

%LAUNCH_WEB_INBOX%

Launches the Web Inbox only
                                                                        										on computer.

To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%LAUNCH_WEB_INBOX%"> Text </a>tag.

%MESSAGE_PLAY_MINI_INBOX%

Launches the Mini Web Inbox
                                                                        										for a specific message and auto plays the message.

To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_PLAY_MINI_INBOX%"> Text </a> tag.

%MESSAGE_DELETE%

Deletes the voice message.
                                                                        										To insert this item directly in the notification template, you can use the
                                                                        										<a href="%MESSAGE_DELETE%">Text </a> tag.

%MESSAGE_FORWARD%

Forwards a particular voice
                                                                        										message. To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_FORWARD%">Text </a> tag.

%MESSAGE_REPLY%

Launches the Mini Web Inbox
                                                                        										with the Reply to Message window to reply to a voice message.To insert this
                                                                        										item directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY%">Text </a> tag.

%MESSAGE_REPLY_ALL%

Launches the Mini Web Inbox
                                                                        										with the Reply to Message window. The To and Subject fields get populated
                                                                        										automatically with multiple recipients.

To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY_ALL%">Text </a> tag.

%MESSAGE_MARKUNREAD%

Launches the Mini Web
                                                                        										Inboxwith marking the message as unread and increasing the unread message
                                                                        										count.To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_MARKUNREAD%">Text </a> tag.

Custom Variables

The administrator can store
                                                                        										values in the form of text and numbers in custom variables. For example, the
                                                                        										administrator can use custom variables for headers and footers. To insert a
                                                                        										variable directly in the notification template, as specified by the
                                                                        										administrator under the Templates > Notification Templates > Custom
                                                                        										Variables page, you can use the %Var1%.

For more information on
                                                                        										custom variables, see the Configuring
                                                                           										  Custom Variables, page 14-12 section.

Custom Graphics

The administrator can use
                                                                        										custom graphics for adding logos, images, within an HTML template. The images
                                                                        										could also be used to define Image based Template Structure.For example - See
                                                                        										Default_Dynamic_Icons.

To insert a graphic
                                                                        										directly in the notification template as specified by the administrator under
                                                                        										the Templates > Notification Templates > Custom Graphics page, you can
                                                                        										use the <img src="%GRAPHIC1%"></img> tag.For more information on
                                                                        										custom graphics, see the Configuring
                                                                           										  Custom Graphics, page 14-13 section.

%CALLER_ID%

Displays the alias name of
                                                                        										the caller who has received a voice message.

%SENDER_ALIAS%

Displays the alias name of
                                                                        										the sender who has dropped a voice message.

%RECEIVER_ALIAS%

Displays the alias name of
                                                                        										the receiver who has received a voice message.

%TIMESTAMP%

Displays the time when
                                                                        										voice message is received as per the time zone of the recipient.

%NEW_MESSAGE_COUNT%

Displays the total number
                                                                        										of new messages.

%SUBJECT%

Displays the subject of
                                                                        										the message.

%MISSED_CALL%

Displays the missed call
                                                                        										related information.

<VOICE_MESSAGE_SUMMARY>

</VOICE_MESSAGE_SUMMARY>

Displays the summary of
                                                                        										messages.

- The
                                                                           								administrator can upload a new image through the administrative replaceable
                                                                           								images option for %MWI_STATUS%, %MESSAGE_STATUS%. For more information refer to Administrative
                                                                              								  Replaceable Images, page 14-13 .

- If
                                                                           								%MESSAGE_STATUS% tag is enclosed within VOICE_MESSAGE_SUMMARY collection tags,
                                                                           								the status tag displays the status of the voice message at the time when
                                                                           								notification email was sent. If the message status changes later, it will not
                                                                           								reflect in the summary content of the notification email. However, if the tag
                                                                           								is used outside the summary tags, it displays the current status of the
                                                                           								message.

Select Validate after
                                                            						  creating or updating the notification template page to verify the HTML content.

The notification template
                                                                        							 does not get saved if any error is returned in the HTML validation. You must
                                                                        							 remove the error(s) returned by validation before saving the notification
                                                                        							 template. However, an HTML template with warnings can be saved successfully.

Select Save.

You can also preview the
                                                            						  template by selecting Preview. The Preview option displays the view as per your
                                                            						  default browser, however, the display may vary on the various email clients.

To edit a notification
                                                                  								template:

On the Search
                                                                        									 Notification Templates page, select the template that you want to edit.

On the Edit Notification
                                                                        									 Template <device> page, change the settings, as applicable.

Select Validate to verify
                                                                        									 the HTML content and Save.

To delete a notification
                                                                  								template:

On the Search Notification Templates page, check
                                                                        									 the check box next to the display name of the notification template that you
                                                                        									 want to delete.

Select Delete Selected
                                                                        									 and OK to confirm deletion.

If a template is assigned to an HTML notification device, then
                                                            				  you cannot delete the template unless all the existing associations with the
                                                            				  template are removed.

### Custom Variables

The custom variables can be used to define commonly used HTML fragments such as, company's name, address, web address.

You should not create more than 20 custom variables.

#### Configuring Custom
                              	 Variables

Step 1

In Cisco Unity Connection Administration, expand Templates >
                                             			 Notification Templates and select Custom Variables. The Search Custom Variables
                                             			 page appears.

Step 2

Configure a custom variable. (For more information on each
                                             			 field, see Help> This Page)

To add a custom variable:

Select Add New and the New Custom Variables page appears.

Enter the values of the required fields and select Save.

You can also add new custom
                                                                        							 variables in the notification templates. For more information, see the Notification
                                                                           								Templates, page 14-7 section.

To edit a custom variable:

On the Search Custom Variables page, select the custom variable
                                                            						  that you want to edit.

On the Edit Custom Variables page, enter the values of the
                                                            						  required fields and select Save.

To delete a custom variable:

On the Search Custom Variables page, check the check box next to
                                                            						  the display name of the custom variable that you want to delete.

Select Delete Selected and OK to confirm deletion.

If a notification template uses a custom variable that has been
                                                            				  deleted, then the variable gets displayed in the notification instead of its
                                                            				  value.

### Custom
                           	 Graphics

The custom graphics can be used to insert the company’s graphics
                              		into notifications including logos and product images.

You cannot create more than 20 custom graphics.

The default custom graphics are DEFAULT_BOTTOM and DEFAULT_TOP.
                              		You cannot edit or delete the default custom graphics.

Custom graphics display in email clients when they are correctly
                              		configured and are functionally capable of displaying graphics.

For more information refer to “Configuring Cisco Unity
                                          		  Connection for HTML-based Message Notification” section of the User Guide for
                                          		  Accessing Cisco Unity Connection Voice Messages in an Email Application,
                                          		  available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/email/b_12xcucugemailx.html .

#### Configuring Custom
                              	 Graphics

Step 1

In Cisco Unity Connection Administration, expand Templates >
                                             			 Notification Templates and select Custom Graphics. The Search Custom Graphics
                                             			 page appears.

Step 2

Configure a custom graphic (For more information on each field,
                                             			 see Help> This Page)

To add a custom graphic

Select Add New and the new Custom Graphics page appears.

Enter the value of the required fields and select Save.

To edit a custom graphic

On the Search Custom Graphics page, select the display name of
                                                            						  the custom graphic that you want to edit.

On the Edit Custom Graphics page, enter the value of the
                                                            						  required fields and select Save.

To delete a custom graphic:

On the Search Custom Graphics page, check the check box next to
                                                            						  the display name of the custom graphics that you want to delete.

Select Delete Selected and OK to confirm deletion.

The file must not be more than 1 MB in size and must be unique
                                                                  						in its display name and image. You cannot upload the same graphic again.

### Administrative Replaceable Images

The administrator can replace the default images for the following status items:

Deleted_message

MWI_OFF

MWI_ON

Read_message

Read_urgent_message

Unread_message

Unread_urgent_message

You can restore the images to the defaults using Restore button present on the Search Replaceable Images page. You cannot
                              add or delete any image in the default list.

#### Editing an Administrative Replaceable Image

Step 1

In Cisco Unity Connection Administration,
                                             			 expand Templates > Notification Templates and select Administrative
                                             			 Replaceable Image.

Step 2

On the Search Replaceable Image page, select
                                             			 the display name of the image that you want to edit.

Step 3

On the Edit Replaceable Image page, change
                                             			 the settings, as applicable. (For field information, see Help> This Page).

You are not allowed to edit the Display
                                                            				  Name field. The replaceable images are used in the notification templates for
                                                            				  the status items tags, for example, %MWI_STATUS% and %MESSAGE_STATUS% displays
                                                            				  the MWI status and message status of the voice message.

Step 4

Select Save after applying the settings.

## Configuring
                        	 HTML-based Message Notification

Unity Connection can be configured to send message notifications
                           		in the form of HTML template to an email address. The HTML-based templates can
                           		be selected and applied by the administrator to allow HTML notification for a
                           		device.

To get the HTML notifications exactly as per the template
                           		defined by the administrator, the user’s email client must support the display
                           		of images and icons. For more information on whether your email client support
                           		the display of images and icons, refer to documentation of your email service
                           		provider.

HTML notifications are supported with the following email
                           		clients:

Microsoft Outlook 2010

Microsoft Outlook 2013

Microsoft Outlook 2016

IBM Lotus Notes

Gmail (Web based access only)

The user must ensure to select the authentication or
                           		non-authentication mode as desired.

### Configuring the Authenticated and Non-Authenticated Mode

If the administrator has created a template that
                                 		  includes images, icons, or status items, then the authentication mode ensures
                                 		  that the user authenticates with the Unity Connection credentials before the
                                 		  images are displayed in an email notification.

The non-authentication mode does not prompt user
                                 		  for credentials and the embedded images or icons are displayed without
                                 		  authentication in the email notification.

By default, the system is configured for the
                                 		  authentication mode. The administrator can configure the settings through
                                 		  Cisco Unity Connection Administration.

Step 1

In Cisco Unity Connection Administration,
                                          			 select System Settings > General Configuration.

Step 2

On the Edit General Configuration page,
                                          			 select the Authenticate Graphics for HTML Notification option to turn on the
                                          			 authentication mode and Save.

### Configuring Unity
                           	 Connection to Send Voice Message as an Attachment with HTML
                           	 Notification

With Unity Connection 10.0(1) or later release, the
                                 		  administrator can configure Unity Connection to send the voice message as an
                                 		  attachment in the HTML notification to the user. Along with the link to access
                                 		  Unity Connection Mini Web Inbox through the HTML notification email, the user
                                 		  can now access the voice message attachment in the .wav format that can be
                                 		  played on a PC or mobile using any player. Prior to 10.0(1) version, the end
                                 		  user received only a link in the HTML notifications to access Unity Connection
                                 		  Mini Web Inbox and listen to voice messages through Mini Web Inbox only.

In case of forwarded messages, the attachment is sent only for
                                             			 the latest voice message. The secure and private voice messages cannot be sent
                                             			 as an attachment.

Following mobile clients are supported to access voice messages
                                 		  from mobile devices:

iPhone 4 and above

Android

### Configuring Unity
                           	 Connection to Send Voice Message as an Attachment

### SUMMARY STEPS

- In Cisco Unity Connection
                                 			 Administration, expand Advanced and select Messaging.

- On the Messaging Configuration page, select the Allow voice mail
                                 			 as attachments to HTML notifications option to send the voice message as an
                                 			 attachment and Save.

### DETAILED STEPS

Step 1

In Cisco Unity Connection
                                          			 Administration, expand Advanced and select Messaging.

Step 2

On the Messaging Configuration page, select the Allow voice mail
                                          			 as attachments to HTML notifications option to send the voice message as an
                                          			 attachment and Save.

### Configuring the Size of Voice Messages Sent as an Attachment

Unity Connection is configured to send the voice
                                 		  message as an attachment upto 2048KB with HTML notification. The administrator
                                 		  can configure the size of the voice message using the Cisco Unity Connection
                                 		  Administration.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Advanced and select Messaging.

Step 2

On the Messaging Configuration page, enter
                                          			 the size of voice message in the Max size of voice mail as attachment to HTML
                                          			 notifications (KB) text box.

Step 3

Select Save. You should restart the
                                          			 Connection Notifier service for changes to take effect.

## Notifications Subject Line Format

Notification subject line format is a feature that enables you to configure the subject lines of the notification emails.

The subject line of the following Notification types can be configured:

Message Notifications: This includes email notifications that are sent to the Unity Connection users for new voice messages.

Missed Call Notifications: This includes the email Notifications for missed calls.

Scheduled Summary Notifications: This includes the email Notifications sent at scheduled time.

The subject line for Message Notifications can only be customized for All Voice Messages. For other events, like Dispatch
                                             Messages, Fax Messages, Calender Appointments, and Calender Meetings, system generated subject is used.

### Subject Line Parameters

The below table describes the parameters that can be specified in the subject line of the notification emails.

Description of Subject Line Format Parameters

%CALLERID%

(When Unknown)

Enter text to be used in subject lines when the Caller ID of the sender of a message is not known.

When the %CALLERID% parameter is used in the subject line format, it is automatically replaced with the ANI Caller ID of the
                                                   sender of the message.

If the ANI Caller ID is not available and the sender is a Unity Connection user, the primary extension of the caller is used.

If the ANI Caller ID is not available and the sender is a non Unity Connection user, the text that you enter in this field
                                                   is inserted into the subject line.For example, if you enter ‘Unknown Caller ID’ in this field, same appears on the screen.

You can also leave this field blank.

%NAME%

(When Unknown)

Enter text to be used in subject lines when both the display name and ANI Caller Name of the sender of the message is not
                                             known.

When an outside caller sends a voice message and %NAME% parameter is used in the subject line format of the notification,
                                                   it is automatically replaced with the ANI Caller Name of the sender of the message.If the ANI Caller Name is not available,
                                                   Unity Connection inserts the value specified in the %NAME% (When Unknown) field.

When Unity Connection user sends a voice message and %NAME% parameter is used in the subject line format of the notification,
                                                   it is automatically replaced with the display Name of the sender of the message.If the display Name is not available, Unity
                                                   Connection inserts the ANI Caller Name. If the ANI Caller Name is not available, the SMTP address of the Unity Connection
                                                   user is used.

%U%

Enter text to be used in subject lines when the message is flagged as Urgent.

When the %U% parameter is used in the subject line, it is automatically replaced with the text that you enter in this field
                                             if the message is flagged as urgent. If the message is not urgent, this parameter is omitted.

%P%

Enter text to be used in subject lines when the message is flagged as Private.

When the %P% parameter is used in the subject line, it is automatically replaced with the text that you enter in this field
                                             if the message is flagged as private. If the message is not private, this parameter is omitted.

%S%

Enter text to be used in subject lines when the message is flagged as secure message.

When the %S% parameter is used in the subject line, it is automatically replaced with the text that you enter in this field
                                             if the message is flagged as secure. If the message is not a secure message, this parameter is omitted.

%D%

Enter text to be used in subject lines when the message is flagged as dispatch message.

When the %D% parameter is used in the subject line, it is automatically replaced with the text that you enter in this field
                                             if the message is flagged as dispatch message. If the message is not a dispatch message, this parameter is omitted.

%TIMESTAMP%

When %TIMESTAMP% parameter is used in the subject line format of Message Notification or Missed call Notification, its value
                                             is the delivery time of the message for which the notification is sent as per the timezone of the recipient.

When %TIMESTAMP% parameter is used in the subject line of Scheduled Summary Notification, then its value is the time at which
                                             scheduled notification is sent.

### Subject Line
                           	 Format Examples

Subject Line Format Examples

Type of Notification

Subject Line Format

Subject Line of the Message Received

Message Notification

Message notification: Voice message from %NAME% %CALLERID%

Message notification: Voice message from John 4132

Missed Call Notification

Missed Call from %NAME% (%CALLERID%) TIMESTAMP%

Missed Call from John (4132) 11.12 hrs

Scheduled Summary Notification

Missed Call from %NAME% (%CALLERID%)

Message Summary Notification

### Subject Line
                           	 Format Configuration

You should consider the following when defining the subject line
                                 		  formats:

You must include a % before and after the parameter.

You can define a separate subject line format for each language
                                       				that is installed on the system.

When a subject line format is not defined for the preferred
                                       				language of the user, the subject line format definition for the system default
                                       				language is used instead.

Step 1

In Cisco Unity Connection Administration page, expand System
                                          			 Settings > Subject Line Formats.

Step 2

On the Edit Subject Line Formats page, select Notifications from
                                          			 Choose Message Type drop down to select the required message type.

Step 3

Select the applicable language from Choose Language drop down
                                          			 menu.

Step 4

Enter text and parameters in the Subject Line Formats fields, as
                                          			 applicable. (For more information on each parameter, see Help> This Page).

Step 5

Enter texts in the Parameter Definitions field, as applicable.

Step 6

Select Save.

Step 7

Repeat Step 2 through Step 5 as needed for the other languages.

| Caution | Do not change the display name of  default notification devices. |
|---|---|

| Note | Missed call event type is pre-checked under Notify me of section of an HTML device when “Default_Missed_Call” template is
                                       used. Similarly, when “Default_Scheduled_Summary” template is used with HTML device, all the event types are un-checked. |
|---|---|

| Note | User should not use the default notification devices in CSV file while using Bulk Administration Tool. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, find the user account
                                       			 that you want to edit. |
|---|---|
| Step 2 | On the Search User Basics page of the user account, select the
                                       			 user account that you want to edit. |
| Step 3 | On the Edit User Basics page, in the Edit menu, select
                                       			 Notification Devices. |
| Step 4 | Configure a notification device.(Phone, Pager, SMTP, HTML, SMS)
                                       			 (For more information on each field, see Help> This Page) To add a notification device: On the Edit User Basics page, select Edit> Notification
                                                      						  Devices. On the Notification Devices page, select Add New. On the New Notification Device page, enter the fields as
                                                      						  applicable depending on the notification device you selected and Save. To edit a notification device: On the Edit User Basics page, select Edit> Notification
                                                      						  Devices. On the Notification Device page, select the notification device
                                                      						  that you want to edit. On the Edit Notification Device page, edit the required settings
                                                      						  and Save. Note To edit
                                                         					 the notification devices for more than one user, on the Search Users page,
                                                         					 check the check boxes for the applicable users and select Bulk Edit. You can also schedule Bulk Edit for a later period using Bulk
                                                            						Edit Task scheduling and select Submit. To delete one or more notification devices: On the Edit User Basics page, select Edit> Notification
                                                      						  Devices. On the Notification Device page, select the notification devices
                                                      						  you want to delete. Select Delete Selected and OK to confirm deletion. Note Similarly, you can configure the notification devices associated
                                                            						with a particular user template. | Note | To edit
                                                         					 the notification devices for more than one user, on the Search Users page,
                                                         					 check the check boxes for the applicable users and select Bulk Edit. You can also schedule Bulk Edit for a later period using Bulk
                                                            						Edit Task scheduling and select Submit. | Note | Similarly, you can configure the notification devices associated
                                                            						with a particular user template. |
| Note | To edit
                                                         					 the notification devices for more than one user, on the Search Users page,
                                                         					 check the check boxes for the applicable users and select Bulk Edit. You can also schedule Bulk Edit for a later period using Bulk
                                                            						Edit Task scheduling and select Submit. |
| Note | Similarly, you can configure the notification devices associated
                                                            						with a particular user template. |

| Note | To edit
                                                         					 the notification devices for more than one user, on the Search Users page,
                                                         					 check the check boxes for the applicable users and select Bulk Edit. You can also schedule Bulk Edit for a later period using Bulk
                                                            						Edit Task scheduling and select Submit. |
|---|---|

| Note | Similarly, you can configure the notification devices associated
                                                            						with a particular user template. |
|---|---|

| Note | When a user receives a notification as part of the cascade, the notification prompts the user to sign in to the mailbox that
                                       is being monitored by the cascade. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | For the first recipient in
                                          			 the notification chain, you need to set up the notification device in the
                                          			 following way: | Find the user account
                                                				  or user template to configure with chaining notifications. In the Notification
                                                				  Devices page for the user or template, for On Notification Failure, select Send
                                                				  To, and select the device that you want Unity Connection to notify next if
                                                				  notification to the device fails. Select the device that
                                                				  you specified for Send To in the Edit Notification devices page Uncheck all Notification Rule Events check boxes. If you
                                                   					 enable any notification events, message notification for the device starts
                                                   					 immediately and does not wait for the notification failure of the previous
                                                   					 device. Your notifications do not chain, they all trigger at once. If you want to chain to a third device if notification to the
                                                   					 device fails, select Send To and the device that you want Unity Connection to
                                                   					 notify next if notification to the device fails. If not, select Do Nothing. |
| Step 2 | For each of the other recipients in the notification chain, you
                                          			 can repeat step 1 to setup the device till you reach the end
                                          			 of recipient list. |  |

| Note | Do not configure SMTP devices for chaining message notification, except as the last device in the chain. Unity Connection
                                       does not detect notification failure for SMTP devices. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | For the first
                                          			 recipient in the notification chain, you need to set up the notification device
                                          			 in the following way: | Find the user account or
                                                				  user template to configure with chaining notifications. In the Notification Devices
                                                				  page for the user or template, for On Notification Failure, select Send To, and
                                                				  select the device that you want Unity Connection to notify next if notification
                                                				  to the device fails. Select the device that you
                                                				  specified for Send To in the Edit Notification devices page. Uncheck
                                                   					 all Notification Rule Events check boxes. If you enable any notification
                                                   					 events, message notification for the device starts immediately and does not
                                                   					 wait for the notification failure of the previous device. Your notifications do
                                                   					 not chain, they all trigger at once. If you
                                                   					 want to chain to a third device if notification to the device fails, select
                                                   					 Send To and the device that you want Unity Connection to notify next if
                                                   					 notification to the device fails. If not, select Do Nothing. |
| Step 2 | For each of
                                          			 the other recipients in the notification chain, you can repeat step 1 to setup the device till you reach the end
                                          			 of recipient list. |  |

| Note | Users can receive notification of new messages by email. Unity Connection supports two types of notification emails: plain
                                       text using SMTP notification devices; or HTML using HTML notification devices. HTML notifications can only be used for new
                                       voice mail. For other types of messages, you must use plain text SMTP notifications. To enhance security, both types of devices
                                       require connection to an SMTP smart host. |
|---|---|

| Step 1 | Configure the SMTP smart host to accept
                                          			 messages from the Unity Connection server. See the documentation for the SMTP
                                          			 server application that you are using. |
|---|---|
| Step 2 | Configure the Unity Connection server. See
                                          			 the Configuring
                                             				the Unity Connection Server to Relay Messages to a Smart Host section. |
| Step 3 | Configure Unity Connection user accounts or
                                          			 user templates. See the Configuring Notification Devices,
                                             				page 14-2 section. |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings > SMTP Configuration, then select Smart Host. |
|---|---|
| Step 2 | On the Smart Host page, in the Smart Host field, enter the IP address or fully qualified domain name of the SMTP smarthost
                                          server, for example, https://<domain name of server>.cisco.com. (Enter the fully qualified domain name of the server only
                                          if DNS is configured.) Note The Smart Host can contain up to 50 characters. | Note | The Smart Host can contain up to 50 characters. |
| Note | The Smart Host can contain up to 50 characters. |
| Step 3 | Select Save. What to do next Note If the Unity Connection server has not been properly enabled to use SMTP smart host for message notification, it places SMTP
                                                         notification messages in the Unity Connection SMTP server badmail folder | Note | If the Unity Connection server has not been properly enabled to use SMTP smart host for message notification, it places SMTP
                                                         notification messages in the Unity Connection SMTP server badmail folder |
| Note | If the Unity Connection server has not been properly enabled to use SMTP smart host for message notification, it places SMTP
                                                         notification messages in the Unity Connection SMTP server badmail folder |

| Note | The Smart Host can contain up to 50 characters. |
|---|---|

| Note | If the Unity Connection server has not been properly enabled to use SMTP smart host for message notification, it places SMTP
                                                         notification messages in the Unity Connection SMTP server badmail folder |
|---|---|

| Note | Not all mobile phones support all character sets; most support
                                       		  the GSM 3.38 default alphabet. |
|---|---|

| Step 1 | Set up an account with a mobile messaging
                                          			 service provider that offers SMS messaging. Unity Connection supports the SMPP
                                          			 version 3.3 or SMPP version 3.4 protocols. |
|---|---|
| Step 2 | Gather the information needed to allow Unity
                                          			 Connection to communicate with the SMPP server at the SMSC affiliated with your
                                          			 contracted service provider, and enter the information on the SMPP Provider
                                          			 page. See the To Set Up an SMPP Provider. |
| Step 3 | When the Unity Connection server is set up
                                          			 behind a firewall, configure the TCP port used by the SMPP server when
                                          			 connecting to Unity Connection. |
| Step 4 | Enable the SMPP provider on Cisco Unity
                                          			 Connection Administration. See the Setting Up an SMPP Provider,
                                             				page 14-6 section. |
| Step 5 | Configure SMS message notification, set up
                                          			 an SMS notification device to receive notifications for a test user account.
                                          			 See the Configuring Notification Devices,
                                             				page 14-2 section. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > Advanced, then select SMPP Providers. |
|---|---|
| Step 2 | On the Search SMPP Providers page, select
                                          			 Add New. |
| Step 3 | Enable the new provider and enter the Name,
                                          			 System ID and Hostname of the provider and Save. For more information on
                                          			 settings, select Help > This Page). |
| Step 4 | On the Edit SMPP Provider page, enter the
                                          			 Port, which is the TCP port number that is used by the SMSC to listen for
                                          			 incoming connections. Note The port number should be in range of
                                                         				  >100 and <=99999. | Note | The port number should be in range of
                                                         				  >100 and <=99999. |
| Note | The port number should be in range of
                                                         				  >100 and <=99999. |

| Note | The port number should be in range of
                                                         				  >100 and <=99999. |
|---|---|

| Note | The use of images, MWI status, and Message status is not mandatory. However, if used, the administrators need to ensure that
                                             the image rendering when used with the HTML tags and the APIs is supported by their respective email clients. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Templates >
                                             			 Notification Templates and select Notification Templates. The Search
                                             			 Notification Templates page appears displaying the list of currently configured
                                             			 templates. |
|---|---|
| Step 2 | Configure notification template. (For more information on each
                                             			 field, see Help> This Page) To add new notification template: Select Add new and New Notification Template page appears. Enter the Display name and HTML content. Select and copy the required status, action, and/or static items
                                                            						  from the left panel of the HTML field and paste the items on the right panel.
                                                            						  See the table 14-1 for more information. Description of Notification Templates Items Description %MWI_STATUS% Displays the image based on
                                                                        										MWI status.The default images are displayed as defined in the Administrative
                                                                        										Replaceable Images section.To insert the status items directly in the
                                                                        										notification template, you can use the <img src=”%MWI_STATUS%”>
                                                                        										</img> tag. %MESSAGE_STATUS% Displays the message status
                                                                        										as unread, read, unread urgent, read urgent, or deleted.The default images are
                                                                        										displayed as defined in the Administrative
                                                                           										  Replaceable Images, page 14-13 section. To insert the status items
                                                                        										directly in the notification template, you
                                                                        										can use the <img src="%MESSAGE_STATUS%">
                                                                        										</img>tag. %LAUNCH_MINI_INBOX% Launches the Unity
                                                                        										Connection Mini Web Inbox. To insert this item directly in the notification
                                                                        										template, you can use the <a href="%LAUNCH_MINI_INBOX%"> Text
                                                                        										</a>tag. %LAUNCH_WEB_INBOX% Launches the Web Inbox only
                                                                        										on computer. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%LAUNCH_WEB_INBOX%"> Text </a>tag. %MESSAGE_PLAY_MINI_INBOX% Launches the Mini Web Inbox
                                                                        										for a specific message and auto plays the message. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_PLAY_MINI_INBOX%"> Text </a> tag. %MESSAGE_DELETE% Deletes the voice message.
                                                                        										To insert this item directly in the notification template, you can use the
                                                                        										<a href="%MESSAGE_DELETE%">Text </a> tag. %MESSAGE_FORWARD% Forwards a particular voice
                                                                        										message. To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_FORWARD%">Text </a> tag. %MESSAGE_REPLY% Launches the Mini Web Inbox
                                                                        										with the Reply to Message window to reply to a voice message.To insert this
                                                                        										item directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY%">Text </a> tag. %MESSAGE_REPLY_ALL% Launches the Mini Web Inbox
                                                                        										with the Reply to Message window. The To and Subject fields get populated
                                                                        										automatically with multiple recipients. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY_ALL%">Text </a> tag. %MESSAGE_MARKUNREAD% Launches the Mini Web
                                                                        										Inboxwith marking the message as unread and increasing the unread message
                                                                        										count.To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_MARKUNREAD%">Text </a> tag. Custom Variables The administrator can store
                                                                        										values in the form of text and numbers in custom variables. For example, the
                                                                        										administrator can use custom variables for headers and footers. To insert a
                                                                        										variable directly in the notification template, as specified by the
                                                                        										administrator under the Templates > Notification Templates > Custom
                                                                        										Variables page, you can use the %Var1%. For more information on
                                                                        										custom variables, see the Configuring
                                                                           										  Custom Variables, page 14-12 section. Custom Graphics The administrator can use
                                                                        										custom graphics for adding logos, images, within an HTML template. The images
                                                                        										could also be used to define Image based Template Structure.For example - See
                                                                        										Default_Dynamic_Icons. To insert a graphic
                                                                        										directly in the notification template as specified by the administrator under
                                                                        										the Templates > Notification Templates > Custom Graphics page, you can
                                                                        										use the <img src="%GRAPHIC1%"></img> tag.For more information on
                                                                        										custom graphics, see the Configuring
                                                                           										  Custom Graphics, page 14-13 section. %CALLER_ID% Displays the alias name of
                                                                        										the caller who has received a voice message. %SENDER_ALIAS% Displays the alias name of
                                                                        										the sender who has dropped a voice message. %RECEIVER_ALIAS% Displays the alias name of
                                                                        										the receiver who has received a voice message. %TIMESTAMP% Displays the time when
                                                                        										voice message is received as per the time zone of the recipient. %NEW_MESSAGE_COUNT% Displays the total number
                                                                        										of new messages. %SUBJECT% Displays the subject of
                                                                        										the message. %MISSED_CALL% Displays the missed call
                                                                        										related information. <VOICE_MESSAGE_SUMMARY> </VOICE_MESSAGE_SUMMARY> Displays the summary of
                                                                        										messages. Note The
                                                                           								administrator can upload a new image through the administrative replaceable
                                                                           								images option for %MWI_STATUS%, %MESSAGE_STATUS%. For more information refer to Administrative
                                                                              								  Replaceable Images, page 14-13 . If
                                                                           								%MESSAGE_STATUS% tag is enclosed within VOICE_MESSAGE_SUMMARY collection tags,
                                                                           								the status tag displays the status of the voice message at the time when
                                                                           								notification email was sent. If the message status changes later, it will not
                                                                           								reflect in the summary content of the notification email. However, if the tag
                                                                           								is used outside the summary tags, it displays the current status of the
                                                                           								message. Select Validate after
                                                            						  creating or updating the notification template page to verify the HTML content. Note The notification template
                                                                        							 does not get saved if any error is returned in the HTML validation. You must
                                                                        							 remove the error(s) returned by validation before saving the notification
                                                                        							 template. However, an HTML template with warnings can be saved successfully. Select Save. You can also preview the
                                                            						  template by selecting Preview. The Preview option displays the view as per your
                                                            						  default browser, however, the display may vary on the various email clients. To edit a notification
                                                                  								template: On the Search
                                                                        									 Notification Templates page, select the template that you want to edit. On the Edit Notification
                                                                        									 Template <device> page, change the settings, as applicable. Select Validate to verify
                                                                        									 the HTML content and Save. To delete a notification
                                                                  								template: On the Search Notification Templates page, check
                                                                        									 the check box next to the display name of the notification template that you
                                                                        									 want to delete. Select Delete Selected
                                                                        									 and OK to confirm deletion. Note If a template is assigned to an HTML notification device, then
                                                            				  you cannot delete the template unless all the existing associations with the
                                                            				  template are removed. | Items | Description | %MWI_STATUS% | Displays the image based on
                                                                        										MWI status.The default images are displayed as defined in the Administrative
                                                                        										Replaceable Images section.To insert the status items directly in the
                                                                        										notification template, you can use the <img src=”%MWI_STATUS%”>
                                                                        										</img> tag. | %MESSAGE_STATUS% | Displays the message status
                                                                        										as unread, read, unread urgent, read urgent, or deleted.The default images are
                                                                        										displayed as defined in the Administrative
                                                                           										  Replaceable Images, page 14-13 section. To insert the status items
                                                                        										directly in the notification template, you
                                                                        										can use the <img src="%MESSAGE_STATUS%">
                                                                        										</img>tag. | %LAUNCH_MINI_INBOX% | Launches the Unity
                                                                        										Connection Mini Web Inbox. To insert this item directly in the notification
                                                                        										template, you can use the <a href="%LAUNCH_MINI_INBOX%"> Text
                                                                        										</a>tag. | %LAUNCH_WEB_INBOX% | Launches the Web Inbox only
                                                                        										on computer. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%LAUNCH_WEB_INBOX%"> Text </a>tag. | %MESSAGE_PLAY_MINI_INBOX% | Launches the Mini Web Inbox
                                                                        										for a specific message and auto plays the message. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_PLAY_MINI_INBOX%"> Text </a> tag. | %MESSAGE_DELETE% | Deletes the voice message.
                                                                        										To insert this item directly in the notification template, you can use the
                                                                        										<a href="%MESSAGE_DELETE%">Text </a> tag. | %MESSAGE_FORWARD% | Forwards a particular voice
                                                                        										message. To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_FORWARD%">Text </a> tag. | %MESSAGE_REPLY% | Launches the Mini Web Inbox
                                                                        										with the Reply to Message window to reply to a voice message.To insert this
                                                                        										item directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY%">Text </a> tag. | %MESSAGE_REPLY_ALL% | Launches the Mini Web Inbox
                                                                        										with the Reply to Message window. The To and Subject fields get populated
                                                                        										automatically with multiple recipients. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY_ALL%">Text </a> tag. | %MESSAGE_MARKUNREAD% | Launches the Mini Web
                                                                        										Inboxwith marking the message as unread and increasing the unread message
                                                                        										count.To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_MARKUNREAD%">Text </a> tag. | Custom Variables | The administrator can store
                                                                        										values in the form of text and numbers in custom variables. For example, the
                                                                        										administrator can use custom variables for headers and footers. To insert a
                                                                        										variable directly in the notification template, as specified by the
                                                                        										administrator under the Templates > Notification Templates > Custom
                                                                        										Variables page, you can use the %Var1%. For more information on
                                                                        										custom variables, see the Configuring
                                                                           										  Custom Variables, page 14-12 section. | Custom Graphics | The administrator can use
                                                                        										custom graphics for adding logos, images, within an HTML template. The images
                                                                        										could also be used to define Image based Template Structure.For example - See
                                                                        										Default_Dynamic_Icons. To insert a graphic
                                                                        										directly in the notification template as specified by the administrator under
                                                                        										the Templates > Notification Templates > Custom Graphics page, you can
                                                                        										use the <img src="%GRAPHIC1%"></img> tag.For more information on
                                                                        										custom graphics, see the Configuring
                                                                           										  Custom Graphics, page 14-13 section. | %CALLER_ID% | Displays the alias name of
                                                                        										the caller who has received a voice message. | %SENDER_ALIAS% | Displays the alias name of
                                                                        										the sender who has dropped a voice message. | %RECEIVER_ALIAS% | Displays the alias name of
                                                                        										the receiver who has received a voice message. | %TIMESTAMP% | Displays the time when
                                                                        										voice message is received as per the time zone of the recipient. | %NEW_MESSAGE_COUNT% | Displays the total number
                                                                        										of new messages. | %SUBJECT% | Displays the subject of
                                                                        										the message. | %MISSED_CALL% | Displays the missed call
                                                                        										related information. | <VOICE_MESSAGE_SUMMARY> </VOICE_MESSAGE_SUMMARY> | Displays the summary of
                                                                        										messages. | Note | The
                                                                           								administrator can upload a new image through the administrative replaceable
                                                                           								images option for %MWI_STATUS%, %MESSAGE_STATUS%. For more information refer to Administrative
                                                                              								  Replaceable Images, page 14-13 . If
                                                                           								%MESSAGE_STATUS% tag is enclosed within VOICE_MESSAGE_SUMMARY collection tags,
                                                                           								the status tag displays the status of the voice message at the time when
                                                                           								notification email was sent. If the message status changes later, it will not
                                                                           								reflect in the summary content of the notification email. However, if the tag
                                                                           								is used outside the summary tags, it displays the current status of the
                                                                           								message. | Note | The notification template
                                                                        							 does not get saved if any error is returned in the HTML validation. You must
                                                                        							 remove the error(s) returned by validation before saving the notification
                                                                        							 template. However, an HTML template with warnings can be saved successfully. | Note | If a template is assigned to an HTML notification device, then
                                                            				  you cannot delete the template unless all the existing associations with the
                                                            				  template are removed. |
| Items | Description |
| %MWI_STATUS% | Displays the image based on
                                                                        										MWI status.The default images are displayed as defined in the Administrative
                                                                        										Replaceable Images section.To insert the status items directly in the
                                                                        										notification template, you can use the <img src=”%MWI_STATUS%”>
                                                                        										</img> tag. |
| %MESSAGE_STATUS% | Displays the message status
                                                                        										as unread, read, unread urgent, read urgent, or deleted.The default images are
                                                                        										displayed as defined in the Administrative
                                                                           										  Replaceable Images, page 14-13 section. To insert the status items
                                                                        										directly in the notification template, you
                                                                        										can use the <img src="%MESSAGE_STATUS%">
                                                                        										</img>tag. |
| %LAUNCH_MINI_INBOX% | Launches the Unity
                                                                        										Connection Mini Web Inbox. To insert this item directly in the notification
                                                                        										template, you can use the <a href="%LAUNCH_MINI_INBOX%"> Text
                                                                        										</a>tag. |
| %LAUNCH_WEB_INBOX% | Launches the Web Inbox only
                                                                        										on computer. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%LAUNCH_WEB_INBOX%"> Text </a>tag. |
| %MESSAGE_PLAY_MINI_INBOX% | Launches the Mini Web Inbox
                                                                        										for a specific message and auto plays the message. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_PLAY_MINI_INBOX%"> Text </a> tag. |
| %MESSAGE_DELETE% | Deletes the voice message.
                                                                        										To insert this item directly in the notification template, you can use the
                                                                        										<a href="%MESSAGE_DELETE%">Text </a> tag. |
| %MESSAGE_FORWARD% | Forwards a particular voice
                                                                        										message. To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_FORWARD%">Text </a> tag. |
| %MESSAGE_REPLY% | Launches the Mini Web Inbox
                                                                        										with the Reply to Message window to reply to a voice message.To insert this
                                                                        										item directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY%">Text </a> tag. |
| %MESSAGE_REPLY_ALL% | Launches the Mini Web Inbox
                                                                        										with the Reply to Message window. The To and Subject fields get populated
                                                                        										automatically with multiple recipients. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY_ALL%">Text </a> tag. |
| %MESSAGE_MARKUNREAD% | Launches the Mini Web
                                                                        										Inboxwith marking the message as unread and increasing the unread message
                                                                        										count.To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_MARKUNREAD%">Text </a> tag. |
| Custom Variables | The administrator can store
                                                                        										values in the form of text and numbers in custom variables. For example, the
                                                                        										administrator can use custom variables for headers and footers. To insert a
                                                                        										variable directly in the notification template, as specified by the
                                                                        										administrator under the Templates > Notification Templates > Custom
                                                                        										Variables page, you can use the %Var1%. For more information on
                                                                        										custom variables, see the Configuring
                                                                           										  Custom Variables, page 14-12 section. |
| Custom Graphics | The administrator can use
                                                                        										custom graphics for adding logos, images, within an HTML template. The images
                                                                        										could also be used to define Image based Template Structure.For example - See
                                                                        										Default_Dynamic_Icons. To insert a graphic
                                                                        										directly in the notification template as specified by the administrator under
                                                                        										the Templates > Notification Templates > Custom Graphics page, you can
                                                                        										use the <img src="%GRAPHIC1%"></img> tag.For more information on
                                                                        										custom graphics, see the Configuring
                                                                           										  Custom Graphics, page 14-13 section. |
| %CALLER_ID% | Displays the alias name of
                                                                        										the caller who has received a voice message. |
| %SENDER_ALIAS% | Displays the alias name of
                                                                        										the sender who has dropped a voice message. |
| %RECEIVER_ALIAS% | Displays the alias name of
                                                                        										the receiver who has received a voice message. |
| %TIMESTAMP% | Displays the time when
                                                                        										voice message is received as per the time zone of the recipient. |
| %NEW_MESSAGE_COUNT% | Displays the total number
                                                                        										of new messages. |
| %SUBJECT% | Displays the subject of
                                                                        										the message. |
| %MISSED_CALL% | Displays the missed call
                                                                        										related information. |
| <VOICE_MESSAGE_SUMMARY> </VOICE_MESSAGE_SUMMARY> | Displays the summary of
                                                                        										messages. |
| Note | The
                                                                           								administrator can upload a new image through the administrative replaceable
                                                                           								images option for %MWI_STATUS%, %MESSAGE_STATUS%. For more information refer to Administrative
                                                                              								  Replaceable Images, page 14-13 . If
                                                                           								%MESSAGE_STATUS% tag is enclosed within VOICE_MESSAGE_SUMMARY collection tags,
                                                                           								the status tag displays the status of the voice message at the time when
                                                                           								notification email was sent. If the message status changes later, it will not
                                                                           								reflect in the summary content of the notification email. However, if the tag
                                                                           								is used outside the summary tags, it displays the current status of the
                                                                           								message. |
| Note | The notification template
                                                                        							 does not get saved if any error is returned in the HTML validation. You must
                                                                        							 remove the error(s) returned by validation before saving the notification
                                                                        							 template. However, an HTML template with warnings can be saved successfully. |
| Note | If a template is assigned to an HTML notification device, then
                                                            				  you cannot delete the template unless all the existing associations with the
                                                            				  template are removed. |

| Items | Description |
|---|---|
| %MWI_STATUS% | Displays the image based on
                                                                        										MWI status.The default images are displayed as defined in the Administrative
                                                                        										Replaceable Images section.To insert the status items directly in the
                                                                        										notification template, you can use the <img src=”%MWI_STATUS%”>
                                                                        										</img> tag. |
| %MESSAGE_STATUS% | Displays the message status
                                                                        										as unread, read, unread urgent, read urgent, or deleted.The default images are
                                                                        										displayed as defined in the Administrative
                                                                           										  Replaceable Images, page 14-13 section. To insert the status items
                                                                        										directly in the notification template, you
                                                                        										can use the <img src="%MESSAGE_STATUS%">
                                                                        										</img>tag. |
| %LAUNCH_MINI_INBOX% | Launches the Unity
                                                                        										Connection Mini Web Inbox. To insert this item directly in the notification
                                                                        										template, you can use the <a href="%LAUNCH_MINI_INBOX%"> Text
                                                                        										</a>tag. |
| %LAUNCH_WEB_INBOX% | Launches the Web Inbox only
                                                                        										on computer. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%LAUNCH_WEB_INBOX%"> Text </a>tag. |
| %MESSAGE_PLAY_MINI_INBOX% | Launches the Mini Web Inbox
                                                                        										for a specific message and auto plays the message. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_PLAY_MINI_INBOX%"> Text </a> tag. |
| %MESSAGE_DELETE% | Deletes the voice message.
                                                                        										To insert this item directly in the notification template, you can use the
                                                                        										<a href="%MESSAGE_DELETE%">Text </a> tag. |
| %MESSAGE_FORWARD% | Forwards a particular voice
                                                                        										message. To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_FORWARD%">Text </a> tag. |
| %MESSAGE_REPLY% | Launches the Mini Web Inbox
                                                                        										with the Reply to Message window to reply to a voice message.To insert this
                                                                        										item directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY%">Text </a> tag. |
| %MESSAGE_REPLY_ALL% | Launches the Mini Web Inbox
                                                                        										with the Reply to Message window. The To and Subject fields get populated
                                                                        										automatically with multiple recipients. To insert this item
                                                                        										directly in the notification template, you can use the <a
                                                                        										href="%MESSAGE_REPLY_ALL%">Text </a> tag. |
| %MESSAGE_MARKUNREAD% | Launches the Mini Web
                                                                        										Inboxwith marking the message as unread and increasing the unread message
                                                                        										count.To insert this item directly in the notification template, you can use
                                                                        										the <a href="%MESSAGE_MARKUNREAD%">Text </a> tag. |
| Custom Variables | The administrator can store
                                                                        										values in the form of text and numbers in custom variables. For example, the
                                                                        										administrator can use custom variables for headers and footers. To insert a
                                                                        										variable directly in the notification template, as specified by the
                                                                        										administrator under the Templates > Notification Templates > Custom
                                                                        										Variables page, you can use the %Var1%. For more information on
                                                                        										custom variables, see the Configuring
                                                                           										  Custom Variables, page 14-12 section. |
| Custom Graphics | The administrator can use
                                                                        										custom graphics for adding logos, images, within an HTML template. The images
                                                                        										could also be used to define Image based Template Structure.For example - See
                                                                        										Default_Dynamic_Icons. To insert a graphic
                                                                        										directly in the notification template as specified by the administrator under
                                                                        										the Templates > Notification Templates > Custom Graphics page, you can
                                                                        										use the <img src="%GRAPHIC1%"></img> tag.For more information on
                                                                        										custom graphics, see the Configuring
                                                                           										  Custom Graphics, page 14-13 section. |
| %CALLER_ID% | Displays the alias name of
                                                                        										the caller who has received a voice message. |
| %SENDER_ALIAS% | Displays the alias name of
                                                                        										the sender who has dropped a voice message. |
| %RECEIVER_ALIAS% | Displays the alias name of
                                                                        										the receiver who has received a voice message. |
| %TIMESTAMP% | Displays the time when
                                                                        										voice message is received as per the time zone of the recipient. |
| %NEW_MESSAGE_COUNT% | Displays the total number
                                                                        										of new messages. |
| %SUBJECT% | Displays the subject of
                                                                        										the message. |
| %MISSED_CALL% | Displays the missed call
                                                                        										related information. |
| <VOICE_MESSAGE_SUMMARY> </VOICE_MESSAGE_SUMMARY> | Displays the summary of
                                                                        										messages. |

| Note | The
                                                                           								administrator can upload a new image through the administrative replaceable
                                                                           								images option for %MWI_STATUS%, %MESSAGE_STATUS%. For more information refer to Administrative
                                                                              								  Replaceable Images, page 14-13 . If
                                                                           								%MESSAGE_STATUS% tag is enclosed within VOICE_MESSAGE_SUMMARY collection tags,
                                                                           								the status tag displays the status of the voice message at the time when
                                                                           								notification email was sent. If the message status changes later, it will not
                                                                           								reflect in the summary content of the notification email. However, if the tag
                                                                           								is used outside the summary tags, it displays the current status of the
                                                                           								message. |
|---|---|

| Note | The notification template
                                                                        							 does not get saved if any error is returned in the HTML validation. You must
                                                                        							 remove the error(s) returned by validation before saving the notification
                                                                        							 template. However, an HTML template with warnings can be saved successfully. |
|---|---|

| Note | If a template is assigned to an HTML notification device, then
                                                            				  you cannot delete the template unless all the existing associations with the
                                                            				  template are removed. |
|---|---|

| Note | You should not create more than 20 custom variables. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Templates >
                                             			 Notification Templates and select Custom Variables. The Search Custom Variables
                                             			 page appears. |
|---|---|
| Step 2 | Configure a custom variable. (For more information on each
                                             			 field, see Help> This Page) To add a custom variable: Select Add New and the New Custom Variables page appears. Enter the values of the required fields and select Save. Note You can also add new custom
                                                                        							 variables in the notification templates. For more information, see the Notification
                                                                           								Templates, page 14-7 section. To edit a custom variable: On the Search Custom Variables page, select the custom variable
                                                            						  that you want to edit. On the Edit Custom Variables page, enter the values of the
                                                            						  required fields and select Save. To delete a custom variable: On the Search Custom Variables page, check the check box next to
                                                            						  the display name of the custom variable that you want to delete. Select Delete Selected and OK to confirm deletion. Note If a notification template uses a custom variable that has been
                                                            				  deleted, then the variable gets displayed in the notification instead of its
                                                            				  value. | Note | You can also add new custom
                                                                        							 variables in the notification templates. For more information, see the Notification
                                                                           								Templates, page 14-7 section. | Note | If a notification template uses a custom variable that has been
                                                            				  deleted, then the variable gets displayed in the notification instead of its
                                                            				  value. |
| Note | You can also add new custom
                                                                        							 variables in the notification templates. For more information, see the Notification
                                                                           								Templates, page 14-7 section. |
| Note | If a notification template uses a custom variable that has been
                                                            				  deleted, then the variable gets displayed in the notification instead of its
                                                            				  value. |

| Note | You can also add new custom
                                                                        							 variables in the notification templates. For more information, see the Notification
                                                                           								Templates, page 14-7 section. |
|---|---|

| Note | If a notification template uses a custom variable that has been
                                                            				  deleted, then the variable gets displayed in the notification instead of its
                                                            				  value. |
|---|---|

| Note | You cannot create more than 20 custom graphics. |
|---|---|

| Note | For more information refer to “Configuring Cisco Unity
                                          		  Connection for HTML-based Message Notification” section of the User Guide for
                                          		  Accessing Cisco Unity Connection Voice Messages in an Email Application,
                                          		  available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/email/b_12xcucugemailx.html . |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Templates >
                                             			 Notification Templates and select Custom Graphics. The Search Custom Graphics
                                             			 page appears. |
|---|---|
| Step 2 | Configure a custom graphic (For more information on each field,
                                             			 see Help> This Page) To add a custom graphic Select Add New and the new Custom Graphics page appears. Enter the value of the required fields and select Save. To edit a custom graphic On the Search Custom Graphics page, select the display name of
                                                            						  the custom graphic that you want to edit. On the Edit Custom Graphics page, enter the value of the
                                                            						  required fields and select Save. To delete a custom graphic: On the Search Custom Graphics page, check the check box next to
                                                            						  the display name of the custom graphics that you want to delete. Select Delete Selected and OK to confirm deletion. Note The file must not be more than 1 MB in size and must be unique
                                                                  						in its display name and image. You cannot upload the same graphic again. | Note | The file must not be more than 1 MB in size and must be unique
                                                                  						in its display name and image. You cannot upload the same graphic again. |
| Note | The file must not be more than 1 MB in size and must be unique
                                                                  						in its display name and image. You cannot upload the same graphic again. |

| Note | The file must not be more than 1 MB in size and must be unique
                                                                  						in its display name and image. You cannot upload the same graphic again. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Templates > Notification Templates and select Administrative
                                             			 Replaceable Image. |
|---|---|
| Step 2 | On the Search Replaceable Image page, select
                                             			 the display name of the image that you want to edit. |
| Step 3 | On the Edit Replaceable Image page, change
                                             			 the settings, as applicable. (For field information, see Help> This Page). Note You are not allowed to edit the Display
                                                            				  Name field. The replaceable images are used in the notification templates for
                                                            				  the status items tags, for example, %MWI_STATUS% and %MESSAGE_STATUS% displays
                                                            				  the MWI status and message status of the voice message. | Note | You are not allowed to edit the Display
                                                            				  Name field. The replaceable images are used in the notification templates for
                                                            				  the status items tags, for example, %MWI_STATUS% and %MESSAGE_STATUS% displays
                                                            				  the MWI status and message status of the voice message. |
| Note | You are not allowed to edit the Display
                                                            				  Name field. The replaceable images are used in the notification templates for
                                                            				  the status items tags, for example, %MWI_STATUS% and %MESSAGE_STATUS% displays
                                                            				  the MWI status and message status of the voice message. |
| Step 4 | Select Save after applying the settings. |

| Note | You are not allowed to edit the Display
                                                            				  Name field. The replaceable images are used in the notification templates for
                                                            				  the status items tags, for example, %MWI_STATUS% and %MESSAGE_STATUS% displays
                                                            				  the MWI status and message status of the voice message. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 select System Settings > General Configuration. |
|---|---|
| Step 2 | On the Edit General Configuration page,
                                          			 select the Authenticate Graphics for HTML Notification option to turn on the
                                          			 authentication mode and Save. |

| Note | In case of forwarded messages, the attachment is sent only for
                                             			 the latest voice message. The secure and private voice messages cannot be sent
                                             			 as an attachment. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | In Cisco Unity Connection
                                          			 Administration, expand Advanced and select Messaging. |  |
| Step 2 | On the Messaging Configuration page, select the Allow voice mail
                                          			 as attachments to HTML notifications option to send the voice message as an
                                          			 attachment and Save. |  |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Advanced and select Messaging. |
|---|---|
| Step 2 | On the Messaging Configuration page, enter
                                          			 the size of voice message in the Max size of voice mail as attachment to HTML
                                          			 notifications (KB) text box. |
| Step 3 | Select Save. You should restart the
                                          			 Connection Notifier service for changes to take effect. |

| Note | The subject line for Message Notifications can only be customized for All Voice Messages. For other events, like Dispatch
                                             Messages, Fax Messages, Calender Appointments, and Calender Meetings, system generated subject is used. |
|---|---|

| %CALLERID% (When Unknown) | Enter text to be used in subject lines when the Caller ID of the sender of a message is not known. When the %CALLERID% parameter is used in the subject line format, it is automatically replaced with the ANI Caller ID of the
                                                   sender of the message. If the ANI Caller ID is not available and the sender is a Unity Connection user, the primary extension of the caller is used. If the ANI Caller ID is not available and the sender is a non Unity Connection user, the text that you enter in this field
                                                   is inserted into the subject line.For example, if you enter ‘Unknown Caller ID’ in this field, same appears on the screen. You can also leave this field blank. |
|---|---|
| %NAME% (When Unknown) | Enter text to be used in subject lines when both the display name and ANI Caller Name of the sender of the message is not
                                             known. When an outside caller sends a voice message and %NAME% parameter is used in the subject line format of the notification,
                                                   it is automatically replaced with the ANI Caller Name of the sender of the message.If the ANI Caller Name is not available,
                                                   Unity Connection inserts the value specified in the %NAME% (When Unknown) field. When Unity Connection user sends a voice message and %NAME% parameter is used in the subject line format of the notification,
                                                   it is automatically replaced with the display Name of the sender of the message.If the display Name is not available, Unity
                                                   Connection inserts the ANI Caller Name. If the ANI Caller Name is not available, the SMTP address of the Unity Connection
                                                   user is used. |
| %U% | Enter text to be used in subject lines when the message is flagged as Urgent. When the %U% parameter is used in the subject line, it is automatically replaced with the text that you enter in this field
                                             if the message is flagged as urgent. If the message is not urgent, this parameter is omitted. |
| %P% | Enter text to be used in subject lines when the message is flagged as Private. When the %P% parameter is used in the subject line, it is automatically replaced with the text that you enter in this field
                                             if the message is flagged as private. If the message is not private, this parameter is omitted. |
| %S% | Enter text to be used in subject lines when the message is flagged as secure message. When the %S% parameter is used in the subject line, it is automatically replaced with the text that you enter in this field
                                             if the message is flagged as secure. If the message is not a secure message, this parameter is omitted. |
| %D% | Enter text to be used in subject lines when the message is flagged as dispatch message. When the %D% parameter is used in the subject line, it is automatically replaced with the text that you enter in this field
                                             if the message is flagged as dispatch message. If the message is not a dispatch message, this parameter is omitted. |
| %TIMESTAMP% | When %TIMESTAMP% parameter is used in the subject line format of Message Notification or Missed call Notification, its value
                                             is the delivery time of the message for which the notification is sent as per the timezone of the recipient. When %TIMESTAMP% parameter is used in the subject line of Scheduled Summary Notification, then its value is the time at which
                                             scheduled notification is sent. |

| Type of Notification | Subject Line Format | Subject Line of the Message Received |
|---|---|---|
| Message Notification | Message notification: Voice message from %NAME% %CALLERID% | Message notification: Voice message from John 4132 |
| Missed Call Notification | Missed Call from %NAME% (%CALLERID%) TIMESTAMP% | Missed Call from John (4132) 11.12 hrs |
| Scheduled Summary Notification | Missed Call from %NAME% (%CALLERID%) | Message Summary Notification |

| Step 1 | In Cisco Unity Connection Administration page, expand System
                                          			 Settings > Subject Line Formats. |
|---|---|
| Step 2 | On the Edit Subject Line Formats page, select Notifications from
                                          			 Choose Message Type drop down to select the required message type. |
| Step 3 | Select the applicable language from Choose Language drop down
                                          			 menu. |
| Step 4 | Enter text and parameters in the Subject Line Formats fields, as
                                          			 applicable. (For more information on each parameter, see Help> This Page). |
| Step 5 | Enter texts in the Parameter Definitions field, as applicable. |
| Step 6 | Select Save. |
| Step 7 | Repeat Step 2 through Step 5 as needed for the other languages. |