---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-user-guide-assistant-b-12xcucugasst-b-12xcucugasst-chapter-01-8b4404f038
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/assistant/b_12xcucugasst/b_12xcucugasst_chapter_01000.html
retrieved_at: 2026-08-21T07:55:19.434235+00:00
---

User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 12.x)

# User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 12.x)

Updated: August 9, 2017

Chapter: Managing Message Notification

## Chapter: Managing Message Notification

# Managing Message Notification

## About Message Notification

Cisco Unity Connection can call a phone or pager to notify you about new messages. Connection can also send message notifications
                           in the form of text, and SMS messages (for example, “Urgent message for Technical Support” or “You have new voice messages”)
                           to email addresses, text pagers, text-compatible mobile phones, and other such devices.

Connection calls a phone or pager or sends a text message based on the notification schedules and contact options that you
                           specify. You can use the Messaging Assistant web tool to set up the following notification devices: a home phone, a mobile
                           phone, a pager, an email device (such as a text pager or home email address), and a work phone. You may also be able to set
                           up additional devices, such as alternative phones, alternative email devices, or an SMS device. Your Connection administrator
                           can tell you whether these options are available to you.

If your text-compatible mobile phone has an email address for receiving text messages, you can set up an email or SMS notification
                                       device to use this phone as a text pager. SMS (SMPP) notifications are for use with GSM mobile phones and other SMS-compatible
                                       devices. SMS notifications are generally much faster than email (SMTP/HTML) text pager notifications, and some SMS service
                                       providers offer the additional benefit of replacing a previous notification with the latest one.

Cisco Unity Connection also allows you to deliver SMTP-based HTML notifications for a new voice message to the end users.
                           These notifications can be sent as an HTML format embedded in the email via SMTP. The users get the flexibility to receive
                           the HTML notifications that can include customized icons, header, and footer along with the link to access Cisco Unity Connection
                           Mini Web Inbox. Connection Mini Web Inbox is a player that allows the user to play the notified messages over a computer or
                           mobile devices.

Web email clients

Desktop email clients like Microsoft Outlook and IBM Lotus Notes

To receive the notifications in the form of the HTML notification templates, you must enable the HTML notification device
                           and assign a notification template. The user can only select a notification template if not restricted by the administrator.
                           In case the administrator has restricted the user from selecting a template, the required field
                           will be grayed out.

Cisco Unity Connection Administration, Cisco PCA,  and the CUPI APIs are used to create, update, and delete an HTML notification
                           device. The user can manage his or her own notification devices using Cisco PCA and also has the flexibility to perform certain
                           operations using the CUPI APIs. For more information, refer to http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_For_End_Users_--_HTML_Notification_Devices

## Setting Up Notification Devices

For Cisco Unity Connection to make notification calls, the notification device must be enabled. Disabling a notification device
                           does not delete its settings. Connection considers notification successful if the device answers, even when new messages remain.
                           (For example, notification is considered successful even when an answering machine picks up and records the message.)

You can change the type of events that Connection notifies you of, the callers or phone numbers that trigger a device, your
                           notification schedules, and the contact options for your notification devices only in the Messaging Assistant web tool, not
                           by phone.

### Setting Up or Changing a Phone or Pager Notification Device

In the Messaging Assistant, from the Notification Devices menu, select View Notification Devices .

On the Notification Devices page, select the device that you want to change or set up.

On the <Device name> Notification Device page, check the Notification Enabled check box to enable the device or uncheck it to disable the device.

In the Phone Number field, enter the phone number of the phone or pager, beginning with any access code needed to make an
                                          external call (for example, 9).

Use digits 0 through 9. Do not use spaces, dashes, or parentheses between digits. For long-distance numbers, include the applicable
                                             dialing codes (for example, 1 and the area code). You can also enter:

, (comma) to insert a one-second pause.

# and * to correspond to the # and * keys on the phone.

You may not be able to enter certain phone numbers or your phone system may require additional characters. If you are experiencing
                                             difficulties with this setting, contact your Connection administrator.

Check the Prompt for User ID on Notifications check box if you want Connection to ask for your phone extension before giving you the message.

In the Dial Extra Digits field, enter any extra digits that Connection will dial after the phone number. The digits could
                                          be a password or an access number that you enter to hear messages, or an ID required by a pager.

In the Dial After field, enter the number of seconds that Connection waits after dialing the phone or pager number before
                                          it dials the extra digits. (You may need to experiment with this setting. Try 6 seconds, then increase or decrease the time
                                          as needed.)

In the Notify Me Of section, select the types of events that will cause Connection to call this notification device:

Connection calls this device when any new message is received, including dispatch and other voice messages, and fax messages.

Connection calls this device when any new voice message is received (including dispatch messages).

Connection calls this device when any new voice message is received that is marked as a dispatch message.

Connection calls this device when any new fax message is received.

For each event type that you chose in Step 8, check the Urgent Only check box to have Connection send the notification only when the new message of that type is marked urgent.

To specify that this device receive notifications only for messages from specific Connection users, in the Where Call Is From
                                          section,  select Add Callers , then search for names:

In the Find Names dialog box, enter search criteria, then select Find .

In the search results, check the check box next to the user or remote contact that you want to add to your Callers list, and
                                                select Add Users .

To specify that this device receive notifications only for messages from specific phone numbers, enter a phone number in the
                                          Number Pattern field.

You can use the wildcard characters X and * to match more than one phone number:

The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                   numbers from 9000 through 9999.

The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                   55563040, 55563041, 5556304100, and so forth.

If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 8 and Step 9—that matches any of the callers or number patterns you specify.

To set up your notification schedule, use the Quick Add options to specify a schedule.

Or

Check or uncheck the check boxes in the schedule to specify the active and inactive hours for the notification device. Connection
                                             makes notification calls during the active hours, if you have new messages. When a new message arrives during inactive hours,
                                             Connection sends a message notification at the start of the next active hour in your schedule.

There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days.

Specify the timing and frequency of the calls made by Connection to notify you of new messages:

Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered.

If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect.

To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes.

For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc.

Hang Up After <x> Rings —Set to a minimum of 3 rings. Choose a higher number to give yourself more time to get to the phone.

Try Again <x> Times —Choose a higher number to accommodate when you step away from the phone briefly. Choose a lower number to avoid disturbing
                                                               others.

Try Again After <x> Minutes —Choose a higher number to accommodate when you step away from the phone for long periods of time.

Try Again <x> Times —Choose a higher number if you use the phone frequently.

Try Again After <x> Minutes —Choose a higher number if you have long phone conversations.

Select an option for an additional device to send notification to when the first device does not answer or is busy. Connection
                                                      calls the device only if it is enabled and its schedule is current.

Select Save .

### Setting Up or Changing an Email (or SMTP) Notification Device

In the Messaging Assistant, from the Notification Devices menu, select View Notification Devices .

On the Notification Devices page, select the email (or SMTP) device that you want to change or set up.

On the <Device type> Notification Device page, check the Notification Enabled check box to enable the device, or uncheck it to disable the device.

In the To field, enter the email address of the text pager, text-compatible mobile phone, or another email account (such as
                                          a home email address).

In the From field, enter the phone number that you want to appear at the end of the text display. (For example, enter the
                                          number you dial to reach Connection when you are not dialing from your desk phone.)

If you have a text-compatible mobile phone that you set up as a text pager, you can activate the automatic callback function
                                                         available with your phone when this number is displayed.

In the Text field, enter any text you want displayed (for example, “You have voicemail”). Every time a message arrives that
                                          matches the criteria selected in the message notification settings, Connection sends this message.

Check the Include Message Counts in Message Text check box if you want Connection to include the number of new and total messages in the notification message.

Check the Include Message Information in Message Text check box if you want Connection to include information about the new message in the text string that is sent to the notification
                                          device. This information can include caller name and caller ID (if available); the type of message (voice, fax); the time
                                          that the message was received; and, if the message was marked private or urgent, an indication of this status.

Check the Include a Link to Full Inbox in Message Text check box if you want the notification to include a link to the Cisco Unity Connection Web Inbox in the text string that
                                          is sent to the SMTP notification device.

In the Notify Me Of section, select the types of event that will cause Connection to send a notification to this device:

Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages.

Connection sends a notification to this device when any new voice message is received (including dispatch messages).

Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message.

Connection sends a notification to this device when any new fax message is received.

Connection sends a notification to this device for an upcoming Outlook appointment.

Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting.

For each event type that you chose in Step 10, check the Urgent Only check box to have Connection send the notification only when the new message of that type is marked urgent.

If you specified either Calendar Appointments or Calendar Meetings in Step 10, in the Calendar Event Advance Notification
                                          Time field, enter the number of minutes before a meeting that you want to receive the notification.

If you want to receive transcriptions of your voice messages, check the Voice Messages check box under Send Transcriptions of Voice Messages.

(The Send Transcriptions of Voice Messages section is visible only if the SpeechView option has been made available to you.)

To receive transcriptions of only urgent voice messages, check the Urgent Only check box.

To specify that this device will receive notifications only for messages from specific Connection users, in the Where Call
                                          Is From section, select Add Callers , then search for names:

In the Find Names dialog box, enter search criteria, then select Find .

In the search results, select the check box next to the user or remote contact  that you want to add to your Callers list,
                                                then select Add Users .

To specify that this device receive notifications only for messages from specific phone numbers, enter a phone number in the Number Pattern field.

You can use the wildcard characters X and * to match more than one phone number:

The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                   numbers from 9000 through 9999.

The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                   55563040, 55563041, 5556304100, and so forth.

If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify.

To set up your notification schedule, use the Quick Add options to specify a schedule.

Or

Check or uncheck the check boxes in the schedule to specify the active and inactive hours for the notification device. Connection
                                             makes notification calls during the active hours, if you have new messages. When a new message arrives during inactive hours,
                                             Connection sends a message notification at the start of the next active hour in your schedule.

There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at
                                                         once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the
                                                         ones that you do have checked. You can use the Copy Day’s Schedule function—below the schedule—to copy a schedule for one
                                                         day to other days.

Specify the timing and frequency of the calls made by Connection to notify you of new messages:

Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered.

If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect.

To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes.

For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc.

If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device.

Select Save .

### Setting Up or Changing an SMS Notification Device

In the Messaging Assistant, from the Notification Devices menu, select View Notification Devices .

On the Notification Devices page, select the SMS device that you want to change or set up.

On the <Device name> Notification Device page, check the Notification Enabled check box to enable the device, or uncheck it to disable the service.

In the To field, enter the phone number for your SMS device.

The format and the number you enter depends on the SMPP provider. For example, you may need to include international country
                                             codes, beginning with a plus sign (+) and followed by the country code, area, city, or trunk code, and then the number for
                                             your device: +12065551234 . Do not start with a zero or the international dialing prefix. Do not include spaces, dashes, parentheses or other punctuation.
                                             Ask your Connection administrator for assistance if you experience difficulties.

In the From field, what you enter depends on the SMPP provider:

If the SMPP provider requires a source address for the server sending the message, enter the IP address of the Cisco Unity
                                                   Connection server.

If the SMPP provider does not require a source address, enter the phone number that you want to appear at the end of the text
                                                   display. (For example, enter the number you dial to reach Cisco Unity Connection when you are not dialing from your desk phone.)
                                                   Like the To field in Step 4, the format and the number you enter depends on the SMPP provider.

Ask your Connection administrator to assist you if you are not sure what to enter in this field.

For SMS devices, consider that some service providers replace the number that you enter in the From field with their own phone
                                                         number. For an alternative method of including a callback number, try entering the number within the text of your message.
                                                         For example, enter: tel:2065551234 in the Text field (see Step 6).

In the Text field, enter any text you want displayed (for example, You have voicemail ). Every time a message arrives that matches the criteria selected in the message notification settings, Cisco Unity Connection
                                          sends this message.

Check the Include Message Counts in Message Text check box if you want Connection to include the number of new and total messages in the notification message.

Check the Include Message Information in Message Text check box if you want Connection to include information about the new message in the text string that is sent to the notification
                                          device. This information can include caller name and caller ID (if available); the type of message (voice, fax); the time
                                          that the message was received; and, if the message was marked private or urgent, an indication of this status.

In the SMPP Provider list, select a provider.

If you are uncertain which one to choose, contact your Connection administrator.

Select the event types that will cause Connection to send a notification to this device:

Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages.

Connection sends a notification to this device when any new voice message is received (including dispatch messages).

Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message.

Connection sends a notification to this device when any new fax message is received.

Connection sends a notification to this device for an upcoming Outlook appointment.

Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting.

For each event type that you chose in Step 10, check the Urgent Only check box to have Connection send the notification only when the new message of that type is marked urgent.

If you specified either Calendar Appointments or Calendar Meetings in Step 10, in the Calendar Event Advance Notification Time field, enter the number of minutes before a meeting that you want to receive the notification.

If you want to receive transcriptions of your voice messages, check the Voice Messages check box under Send Transcriptions of Voice Messages.

(The Send Transcriptions of Voice Messages section is visible only if the SpeechView option has been made available to you.)

To receive transcriptions of only urgent voice messages, check the Urgent Only check box.

Check the Limit the Number of SMS Messages Per Transcription To check box and enter the maximum number of SMS messages you want for each message transcription.

This setting is useful for reducing costs if your mobile phone carrier or SMS service provider charges for each SMS message
                                             that you receive.

To specify that this device will receive notifications only for messages from specific Connection users, select Add Callers , then search for names:

In the Find Names dialog box, enter search criteria, then select Find .

In the search results, select the check box next to the user or remote contact  that you want to add to your Callers list,
                                                then select Add Users .

To specify that this device receive notifications only for messages from specific phone numbers, enter a phone number in the Number Pattern field.

You can use the wildcard characters X and * to match more than one phone number:

The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                   numbers from 9000 through 9999.

The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                   55563040, 55563041, 5556304100, and so forth.

If you specify both Callers and Phone Numbers for a device, Connection will send the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify.

To set up your notification schedule, use the Quick Add options to specify a schedule.

Or

Check or uncheck the check boxes in the schedule to specify the active and inactive hours for the notification device. Connection
                                             makes notification calls during the active hours, if you have new messages. When a new message arrives during inactive hours,
                                             Connection sends a message notification at the start of the next active hour in your schedule.

There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check boxes at once. Alternatively, select Invert Schedule to check all the boxes that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days.

Specify the timing and frequency of the calls made by Connection to notify you of new messages:

Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered.

If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect.

To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes.

For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc.

If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device.

Select Save .

### Setting Up or
                           	 Changing an HTML Notification Device

In the
                                          			 Messaging Assistant, from the Notification Devices menu, select View
                                             				Notification Devices .

On the
                                          			 Notification Devices page, select the HTML device that you want to change or set up.

On the
                                          			 <Device name> Notification Device page, check the Notification
                                             				Enabled check box to enable the device, or uncheck it to disable the
                                          			 service.

In the To
                                          			 field, enter a valid email address.

In the Select
                                          			 HTML Template drop-down list, select a default or customized template. The
                                          			 default templates are Default_Actionable_Links_Only, Default_Missed_Call,
                                          			 Default_Missed_Call_With_Summary, Default_Scheduled_Summary,
                                          			 Default_Voice_Message_With_Summary and Default_Dynamic_Icons.

Note that this
                                             				field will be inactive if the administrator has not given rights to the user to
                                             				select an HTML template.

Click Preview to
                                          			 view format of an HTML notification for the selected template.

The Preview option is available only after creating and saving a template.

In the Outdial
                                          			 Number field, enter the phone number that you will use to check the
                                          			 notifications. This field will be inactive if the administrator has not given
                                          			 rights to the user to enter mobile number from PCA. The number entered over
                                          			 here must be E164 compliance.

To specify
                                          			 that device will receive notifications as per the Event Type section under Notify Me
                                             				Of field:

Check All Voice
                                                   					 Messages event type check box to send the notification of new voice
                                                				  message.

Check the Urgent
                                                   					 Only check box to send the notification only when the new voice message is
                                                				  marked urgent.

Check Missed
                                                   					 Call event type check box to send the notification of new missed call.

To specify
                                          			 that this device receive notifications only for messages from specific
                                          			 Connection users, select Add
                                             				Callers , and then search for names:

Select the users to be added to receive notification and click Add Member(s) .

Select the user to be removed from the notification list and
                                                				  click Delete Selected button.

To specify
                                          			 that this device receive notifications only for messages from specific phone
                                          			 numbers, enter a phone number in the Number
                                             				Pattern field.

You can use
                                             				the wildcard characters X and * to match more than one phone number:

The X
                                                   					 character matches any single digit in the range 0 through 9. For example, the
                                                   					 pattern 9XXX matches the range of phone numbers from 9000 through 9999.

The
                                                   					 asterisk (*) character matches any sequence of digits. For example, the pattern
                                                   					 5556304* matches the phone numbers 5556304, 55563040, 55563041, 5556304100, and
                                                   					 so forth.

If you
                                                         				  specify both callers and phone numbers for a device, Connection will send the
                                                         				  device a notification for any message, irrespective of the types you specified
                                                         				  in Step 9 that matches any of the callers or number patterns you specify.

To set up
                                          			 your Summary Notification schedule:

Enter a value less than or equal to 100 in the Max Message Count field to specify the maximum number of
                                                				  messages that can be included in a Summary Notification. By default, the Max
                                                				  message count is set to 10.

Click Add to specify a schedule.

Enter the time when you want Unity Connection to send Summary
                                                				  Notification in the Send Notification At field. Multiple time slots can
                                                				  also be added.

Select Clear All to uncheck all the check boxes at once. Alternatively, click Select
                                                            					 All to check all the boxes at once. You can also delete the scheduled time
                                                         				  by selecting the check boxes and clicking Delete
                                                            					 Selected .

To set up
                                          			 your notification schedule, do either of the following:

Use the Add options to specify a schedule, or

Check or
                                                      					 uncheck the check boxes in the schedule to specify the active and inactive
                                                      					 hours for the notification device.

There are
                                                         				  several ways to set up your notification schedule quickly. Select Clear
                                                            					 Schedule to uncheck all check boxes at once. Alternatively, click Invert
                                                            					 Schedule to check all the boxes that you currently do not have checked and
                                                         				  uncheck the ones that you do have checked. You can use the Copy Day's
                                                            					 Schedule option to copy a schedule from one day to other days.

## Cascading and Chaining Message Notification

Cascading message notification allows you to set up a series of notifications to a widening circle of recipients.

Alternatively, message notification can be set to “chain” to a series of notification devices if an attempt to send notification
                           to the first selected device fails. (The definition of failure to a notification device is based on the options you select
                           for retrying a device that is not answered or is busy.)

When setting up a chain of message notification devices, select the types of messages and message urgency for which Cisco
                           Unity Connection will call only for the first device. If any message types are selected for a device other than the first,
                           message notification for the device will begin immediately and will not wait for the notification failure of the previous
                           device. Therefore, your notifications will not occur as a chain but will all be activated simultaneously.

To include an email or SMS device in a chaining message notification, you must specify the device as last in the chain, because
                                       Connection may not be able to detect notification failure for these types of devices.

To set up multiple notification devices to function in a cascading or chaining sequence, you may need to contact your Connection
                           administrator for instructions. Without certain settings, cascading or chaining notification may not work correctly.

## Considerations for Setting Up SMS (SMPP) Text Message Notification

Note the following considerations before you set up SMS (SMPP) text message notification:

SMS (SMPP) notifications are for use with GSM mobile phones and other SMS-compatible devices. SMS notifications are generally
                                 much faster than (SMTP) text pager notifications, and some SMS service providers offer the additional benefit of replacing
                                 a previous notification with the latest one.

SMS service providers often charge for each SMS message or group of messages that Cisco Unity Connection sends. To reduce
                                 costs to your organization, consider limiting the number of notifications that you receive by a particular message type or
                                 urgency (for example, only urgent voice messages or only voice messages from specific callers or phone numbers).

Some SMS service providers replace the phone number that you enter in the From field on the SMS (SMPP) Notification Device
                                 page in the Messaging Assistant web tool with their own phone number. For an alternative way to include a callback number,
                                 see the Tip in Step 5 in Setting Up or Changing an SMS Notification Device .

The time stamp for an SMS (SMPP) notification on some phones reflects the time that the SMS message was sent by the SMS service
                                 provider to your SMS device. For this reason, the time stamp may not reflect your local time zone or preferred time format.

## About Transcription Delivery with SpeechView

Cisco SpeechView provides a transcription service that converts your voice messages to text, which you can have sent to an
                           email address or to your mobile phone.

If you have an email application configured to access your Connection voice messages, you can also view the transcriptions
                           there. The original voice message is attached to the transcribed message.

To take full advantage of SpeechView, configure your mobile phones to forward to Connection so that all of your voice messages
                           are available in one mailbox and are transcribed.

## Considerations for Setting Up Email and SMS Devices to Receive Transcriptions with SpeechView

Devices that have an email address (for example, text pagers and text-compatible mobile phones) receive voice message transcriptions
                           as email messages or text messages, depending on the device.

SMS-compatible devices receive voice message transcriptions as text messages.

The fields to turn on transcription delivery are located on the Email Notification Device and SMS Notification Device pages
                           where you set up message notification in the Messaging Assistant. (See the applicable procedure in Setting Up Notification Devices .)

Note the following considerations for the most effective use of transcription delivery with SpeechView:

In the From field, enter the number you dial to reach Connection when you are not dialing from your desk phone. If you have a text-compatible
                                 mobile phone, you may be able to initiate a callback to Connection in the event that you want to listen to the message.

Check the Include Message Information in Message Text check box to include call information such as caller name and caller ID (if available) and the time that the message was
                                 received. Otherwise, there will be no indication in the message of when it was received.

In addition, if you have a text-compatible mobile phone, you may be able to initiate a callback when the caller ID is included
                                 with the transcription.

In the Notify Me Of section, if you turn on notification for voice or dispatch messages, you are notified when a message arrives. The transcription
                                 will soon follow. If you do not want notification before the transcription arrives, do not select the voice or dispatch message
                                 options.

Email messages that contain transcriptions have a subject line that is identical to notification messages. So, if you have
                                 notification for voice or dispatch messages turned on, you will have to open the messages to determine which one contains
                                 the transcription.

| Tip | If your text-compatible mobile phone has an email address for receiving text messages, you can set up an email or SMS notification
                                       device to use this phone as a text pager. SMS (SMPP) notifications are for use with GSM mobile phones and other SMS-compatible
                                       devices. SMS notifications are generally much faster than email (SMTP/HTML) text pager notifications, and some SMS service
                                       providers offer the additional benefit of replacing a previous notification with the latest one. |
|---|---|

| Step 1 | In the Messaging Assistant, from the Notification Devices menu, select View Notification Devices . |
|---|---|
| Step 2 | On the Notification Devices page, select the device that you want to change or set up. |
| Step 3 | On the <Device name> Notification Device page, check the Notification Enabled check box to enable the device or uncheck it to disable the device. |
| Step 4 | In the Phone Number field, enter the phone number of the phone or pager, beginning with any access code needed to make an
                                          external call (for example, 9). Use digits 0 through 9. Do not use spaces, dashes, or parentheses between digits. For long-distance numbers, include the applicable
                                             dialing codes (for example, 1 and the area code). You can also enter: , (comma) to insert a one-second pause. # and * to correspond to the # and * keys on the phone. You may not be able to enter certain phone numbers or your phone system may require additional characters. If you are experiencing
                                             difficulties with this setting, contact your Connection administrator. |
| Step 5 | Check the Prompt for User ID on Notifications check box if you want Connection to ask for your phone extension before giving you the message. |
| Step 6 | In the Dial Extra Digits field, enter any extra digits that Connection will dial after the phone number. The digits could
                                          be a password or an access number that you enter to hear messages, or an ID required by a pager. |
| Step 7 | In the Dial After field, enter the number of seconds that Connection waits after dialing the phone or pager number before
                                          it dials the extra digits. (You may need to experiment with this setting. Try 6 seconds, then increase or decrease the time
                                          as needed.) |
| Step 8 | In the Notify Me Of section, select the types of events that will cause Connection to call this notification device: Option Description All Messages Connection calls this device when any new message is received, including dispatch and other voice messages, and fax messages. All Voice Messages Connection calls this device when any new voice message is received (including dispatch messages). Dispatch Messages Connection calls this device when any new voice message is received that is marked as a dispatch message. Fax Messages Connection calls this device when any new fax message is received. | Option | Description | All Messages | Connection calls this device when any new message is received, including dispatch and other voice messages, and fax messages. | All Voice Messages | Connection calls this device when any new voice message is received (including dispatch messages). | Dispatch Messages | Connection calls this device when any new voice message is received that is marked as a dispatch message. | Fax Messages | Connection calls this device when any new fax message is received. |
| Option | Description |
| All Messages | Connection calls this device when any new message is received, including dispatch and other voice messages, and fax messages. |
| All Voice Messages | Connection calls this device when any new voice message is received (including dispatch messages). |
| Dispatch Messages | Connection calls this device when any new voice message is received that is marked as a dispatch message. |
| Fax Messages | Connection calls this device when any new fax message is received. |
| Step 9 | For each event type that you chose in Step 8, check the Urgent Only check box to have Connection send the notification only when the new message of that type is marked urgent. |
| Step 10 | To specify that this device receive notifications only for messages from specific Connection users, in the Where Call Is From
                                          section,  select Add Callers , then search for names: In the Find Names dialog box, enter search criteria, then select Find . In the search results, check the check box next to the user or remote contact that you want to add to your Callers list, and
                                                select Add Users . |
| Step 11 | To specify that this device receive notifications only for messages from specific phone numbers, enter a phone number in the
                                          Number Pattern field. You can use the wildcard characters X and * to match more than one phone number: The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                   numbers from 9000 through 9999. The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                   55563040, 55563041, 5556304100, and so forth. Tip If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 8 and Step 9—that matches any of the callers or number patterns you specify. | Tip | If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 8 and Step 9—that matches any of the callers or number patterns you specify. |
| Tip | If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 8 and Step 9—that matches any of the callers or number patterns you specify. |
| Step 12 | To set up your notification schedule, use the Quick Add options to specify a schedule. Or Check or uncheck the check boxes in the schedule to specify the active and inactive hours for the notification device. Connection
                                             makes notification calls during the active hours, if you have new messages. When a new message arrives during inactive hours,
                                             Connection sends a message notification at the start of the next active hour in your schedule. Tip There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days. | Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days. |
| Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days. |
| Step 13 | Specify the timing and frequency of the calls made by Connection to notify you of new messages: Option Description Attempt First Contact After <x> Minutes Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. If There Are Still New Messages, Try Again Every <x> Minutes To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. If Does Not Answer Connection follows your settings for an unanswered device. Indicate settings for: Hang Up After <x> Rings —Set to a minimum of 3 rings. Choose a higher number to give yourself more time to get to the phone. Try Again <x> Times —Choose a higher number to accommodate when you step away from the phone briefly. Choose a lower number to avoid disturbing
                                                               others. Try Again After <x> Minutes —Choose a higher number to accommodate when you step away from the phone for long periods of time. If Is Busy Connection follows your settings for a busy device. Indicate settings for: Try Again <x> Times —Choose a higher number if you use the phone frequently. Try Again After <x> Minutes —Choose a higher number if you have long phone conversations. If Notification Fails Try Select an option for an additional device to send notification to when the first device does not answer or is busy. Connection
                                                      calls the device only if it is enabled and its schedule is current. | Option | Description | Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. | If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. | If Does Not Answer | Connection follows your settings for an unanswered device. Indicate settings for: Hang Up After <x> Rings —Set to a minimum of 3 rings. Choose a higher number to give yourself more time to get to the phone. Try Again <x> Times —Choose a higher number to accommodate when you step away from the phone briefly. Choose a lower number to avoid disturbing
                                                               others. Try Again After <x> Minutes —Choose a higher number to accommodate when you step away from the phone for long periods of time. | If Is Busy | Connection follows your settings for a busy device. Indicate settings for: Try Again <x> Times —Choose a higher number if you use the phone frequently. Try Again After <x> Minutes —Choose a higher number if you have long phone conversations. | If Notification Fails Try | Select an option for an additional device to send notification to when the first device does not answer or is busy. Connection
                                                      calls the device only if it is enabled and its schedule is current. |
| Option | Description |
| Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. |
| If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. |
| If Does Not Answer | Connection follows your settings for an unanswered device. Indicate settings for: Hang Up After <x> Rings —Set to a minimum of 3 rings. Choose a higher number to give yourself more time to get to the phone. Try Again <x> Times —Choose a higher number to accommodate when you step away from the phone briefly. Choose a lower number to avoid disturbing
                                                               others. Try Again After <x> Minutes —Choose a higher number to accommodate when you step away from the phone for long periods of time. |
| If Is Busy | Connection follows your settings for a busy device. Indicate settings for: Try Again <x> Times —Choose a higher number if you use the phone frequently. Try Again After <x> Minutes —Choose a higher number if you have long phone conversations. |
| If Notification Fails Try | Select an option for an additional device to send notification to when the first device does not answer or is busy. Connection
                                                      calls the device only if it is enabled and its schedule is current. |
| Step 14 | Select Save . |

| Option | Description |
|---|---|
| All Messages | Connection calls this device when any new message is received, including dispatch and other voice messages, and fax messages. |
| All Voice Messages | Connection calls this device when any new voice message is received (including dispatch messages). |
| Dispatch Messages | Connection calls this device when any new voice message is received that is marked as a dispatch message. |
| Fax Messages | Connection calls this device when any new fax message is received. |

| Tip | If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 8 and Step 9—that matches any of the callers or number patterns you specify. |
|---|---|

| Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days. |
|---|---|

| Option | Description |
|---|---|
| Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. |
| If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. |
| If Does Not Answer | Connection follows your settings for an unanswered device. Indicate settings for: Hang Up After <x> Rings —Set to a minimum of 3 rings. Choose a higher number to give yourself more time to get to the phone. Try Again <x> Times —Choose a higher number to accommodate when you step away from the phone briefly. Choose a lower number to avoid disturbing
                                                               others. Try Again After <x> Minutes —Choose a higher number to accommodate when you step away from the phone for long periods of time. |
| If Is Busy | Connection follows your settings for a busy device. Indicate settings for: Try Again <x> Times —Choose a higher number if you use the phone frequently. Try Again After <x> Minutes —Choose a higher number if you have long phone conversations. |
| If Notification Fails Try | Select an option for an additional device to send notification to when the first device does not answer or is busy. Connection
                                                      calls the device only if it is enabled and its schedule is current. |

| Step 1 | In the Messaging Assistant, from the Notification Devices menu, select View Notification Devices . |
|---|---|
| Step 2 | On the Notification Devices page, select the email (or SMTP) device that you want to change or set up. |
| Step 3 | On the <Device type> Notification Device page, check the Notification Enabled check box to enable the device, or uncheck it to disable the device. |
| Step 4 | In the To field, enter the email address of the text pager, text-compatible mobile phone, or another email account (such as
                                          a home email address). |
| Step 5 | In the From field, enter the phone number that you want to appear at the end of the text display. (For example, enter the
                                          number you dial to reach Connection when you are not dialing from your desk phone.) Tip If you have a text-compatible mobile phone that you set up as a text pager, you can activate the automatic callback function
                                                         available with your phone when this number is displayed. | Tip | If you have a text-compatible mobile phone that you set up as a text pager, you can activate the automatic callback function
                                                         available with your phone when this number is displayed. |
| Tip | If you have a text-compatible mobile phone that you set up as a text pager, you can activate the automatic callback function
                                                         available with your phone when this number is displayed. |
| Step 6 | In the Text field, enter any text you want displayed (for example, “You have voicemail”). Every time a message arrives that
                                          matches the criteria selected in the message notification settings, Connection sends this message. |
| Step 7 | Check the Include Message Counts in Message Text check box if you want Connection to include the number of new and total messages in the notification message. |
| Step 8 | Check the Include Message Information in Message Text check box if you want Connection to include information about the new message in the text string that is sent to the notification
                                          device. This information can include caller name and caller ID (if available); the type of message (voice, fax); the time
                                          that the message was received; and, if the message was marked private or urgent, an indication of this status. |
| Step 9 | Check the Include a Link to Full Inbox in Message Text check box if you want the notification to include a link to the Cisco Unity Connection Web Inbox in the text string that
                                          is sent to the SMTP notification device. |
| Step 10 | In the Notify Me Of section, select the types of event that will cause Connection to send a notification to this device: Option Description All Messages Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages. All Voice Messages Connection sends a notification to this device when any new voice message is received (including dispatch messages). Dispatch Messages Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message. Fax Messages Connection sends a notification to this device when any new fax message is received. Calendar Appointments Connection sends a notification to this device for an upcoming Outlook appointment. Calendar Meetings Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting. | Option | Description | All Messages | Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages. | All Voice Messages | Connection sends a notification to this device when any new voice message is received (including dispatch messages). | Dispatch Messages | Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message. | Fax Messages | Connection sends a notification to this device when any new fax message is received. | Calendar Appointments | Connection sends a notification to this device for an upcoming Outlook appointment. | Calendar Meetings | Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting. |
| Option | Description |
| All Messages | Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages. |
| All Voice Messages | Connection sends a notification to this device when any new voice message is received (including dispatch messages). |
| Dispatch Messages | Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message. |
| Fax Messages | Connection sends a notification to this device when any new fax message is received. |
| Calendar Appointments | Connection sends a notification to this device for an upcoming Outlook appointment. |
| Calendar Meetings | Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting. |
| Step 11 | For each event type that you chose in Step 10, check the Urgent Only check box to have Connection send the notification only when the new message of that type is marked urgent. |
| Step 12 | If you specified either Calendar Appointments or Calendar Meetings in Step 10, in the Calendar Event Advance Notification
                                          Time field, enter the number of minutes before a meeting that you want to receive the notification. |
| Step 13 | If you want to receive transcriptions of your voice messages, check the Voice Messages check box under Send Transcriptions of Voice Messages. (The Send Transcriptions of Voice Messages section is visible only if the SpeechView option has been made available to you.) |
| Step 14 | To receive transcriptions of only urgent voice messages, check the Urgent Only check box. |
| Step 15 | To specify that this device will receive notifications only for messages from specific Connection users, in the Where Call
                                          Is From section, select Add Callers , then search for names: In the Find Names dialog box, enter search criteria, then select Find . In the search results, select the check box next to the user or remote contact  that you want to add to your Callers list,
                                                then select Add Users . |
| Step 16 | To specify that this device receive notifications only for messages from specific phone numbers, enter a phone number in the Number Pattern field. You can use the wildcard characters X and * to match more than one phone number: The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                   numbers from 9000 through 9999. The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                   55563040, 55563041, 5556304100, and so forth. Tip If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify. | Tip | If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify. |
| Tip | If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify. |
| Step 17 | To set up your notification schedule, use the Quick Add options to specify a schedule. Or Check or uncheck the check boxes in the schedule to specify the active and inactive hours for the notification device. Connection
                                             makes notification calls during the active hours, if you have new messages. When a new message arrives during inactive hours,
                                             Connection sends a message notification at the start of the next active hour in your schedule. Tip There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at
                                                         once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the
                                                         ones that you do have checked. You can use the Copy Day’s Schedule function—below the schedule—to copy a schedule for one
                                                         day to other days. | Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at
                                                         once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the
                                                         ones that you do have checked. You can use the Copy Day’s Schedule function—below the schedule—to copy a schedule for one
                                                         day to other days. |
| Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at
                                                         once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the
                                                         ones that you do have checked. You can use the Copy Day’s Schedule function—below the schedule—to copy a schedule for one
                                                         day to other days. |
| Step 18 | Specify the timing and frequency of the calls made by Connection to notify you of new messages: Option Description Attempt First Contact After <x> Minutes Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. If There Are Still New Messages, Try Again Every <x> Minutes To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. Caution If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. | Option | Description | Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. | If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. Caution If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. | Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
| Option | Description |
| Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. |
| If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. Caution If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. | Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
| Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
| Step 19 | Select Save . |

| Tip | If you have a text-compatible mobile phone that you set up as a text pager, you can activate the automatic callback function
                                                         available with your phone when this number is displayed. |
|---|---|

| Option | Description |
|---|---|
| All Messages | Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages. |
| All Voice Messages | Connection sends a notification to this device when any new voice message is received (including dispatch messages). |
| Dispatch Messages | Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message. |
| Fax Messages | Connection sends a notification to this device when any new fax message is received. |
| Calendar Appointments | Connection sends a notification to this device for an upcoming Outlook appointment. |
| Calendar Meetings | Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting. |

| Tip | If you specify both Callers and Phone Numbers for a device, Connection sends the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify. |
|---|---|

| Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check blocks at
                                                         once. Alternatively, select Invert Schedule to check all the blocks that you currently do not have checked and uncheck the
                                                         ones that you do have checked. You can use the Copy Day’s Schedule function—below the schedule—to copy a schedule for one
                                                         day to other days. |
|---|---|

| Option | Description |
|---|---|
| Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. |
| If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. Caution If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. | Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
| Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |

| Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
|---|---|

| Step 1 | In the Messaging Assistant, from the Notification Devices menu, select View Notification Devices . |
|---|---|
| Step 2 | On the Notification Devices page, select the SMS device that you want to change or set up. |
| Step 3 | On the <Device name> Notification Device page, check the Notification Enabled check box to enable the device, or uncheck it to disable the service. |
| Step 4 | In the To field, enter the phone number for your SMS device. The format and the number you enter depends on the SMPP provider. For example, you may need to include international country
                                             codes, beginning with a plus sign (+) and followed by the country code, area, city, or trunk code, and then the number for
                                             your device: +12065551234 . Do not start with a zero or the international dialing prefix. Do not include spaces, dashes, parentheses or other punctuation.
                                             Ask your Connection administrator for assistance if you experience difficulties. |
| Step 5 | In the From field, what you enter depends on the SMPP provider: If the SMPP provider requires a source address for the server sending the message, enter the IP address of the Cisco Unity
                                                   Connection server. If the SMPP provider does not require a source address, enter the phone number that you want to appear at the end of the text
                                                   display. (For example, enter the number you dial to reach Cisco Unity Connection when you are not dialing from your desk phone.)
                                                   Like the To field in Step 4, the format and the number you enter depends on the SMPP provider. Ask your Connection administrator to assist you if you are not sure what to enter in this field. Tip For SMS devices, consider that some service providers replace the number that you enter in the From field with their own phone
                                                         number. For an alternative method of including a callback number, try entering the number within the text of your message.
                                                         For example, enter: tel:2065551234 in the Text field (see Step 6). | Tip | For SMS devices, consider that some service providers replace the number that you enter in the From field with their own phone
                                                         number. For an alternative method of including a callback number, try entering the number within the text of your message.
                                                         For example, enter: tel:2065551234 in the Text field (see Step 6). |
| Tip | For SMS devices, consider that some service providers replace the number that you enter in the From field with their own phone
                                                         number. For an alternative method of including a callback number, try entering the number within the text of your message.
                                                         For example, enter: tel:2065551234 in the Text field (see Step 6). |
| Step 6 | In the Text field, enter any text you want displayed (for example, You have voicemail ). Every time a message arrives that matches the criteria selected in the message notification settings, Cisco Unity Connection
                                          sends this message. |
| Step 7 | Check the Include Message Counts in Message Text check box if you want Connection to include the number of new and total messages in the notification message. |
| Step 8 | Check the Include Message Information in Message Text check box if you want Connection to include information about the new message in the text string that is sent to the notification
                                          device. This information can include caller name and caller ID (if available); the type of message (voice, fax); the time
                                          that the message was received; and, if the message was marked private or urgent, an indication of this status. |
| Step 9 | In the SMPP Provider list, select a provider. If you are uncertain which one to choose, contact your Connection administrator. |
| Step 10 | Select the event types that will cause Connection to send a notification to this device: Option Description All Messages Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages. All Voice Messages Connection sends a notification to this device when any new voice message is received (including dispatch messages). Dispatch Messages Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message. Fax Messages Connection sends a notification to this device when any new fax message is received. Calendar Appointments Connection sends a notification to this device for an upcoming Outlook appointment. Calendar Meetings Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting. | Option | Description | All Messages | Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages. | All Voice Messages | Connection sends a notification to this device when any new voice message is received (including dispatch messages). | Dispatch Messages | Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message. | Fax Messages | Connection sends a notification to this device when any new fax message is received. | Calendar Appointments | Connection sends a notification to this device for an upcoming Outlook appointment. | Calendar Meetings | Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting. |
| Option | Description |
| All Messages | Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages. |
| All Voice Messages | Connection sends a notification to this device when any new voice message is received (including dispatch messages). |
| Dispatch Messages | Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message. |
| Fax Messages | Connection sends a notification to this device when any new fax message is received. |
| Calendar Appointments | Connection sends a notification to this device for an upcoming Outlook appointment. |
| Calendar Meetings | Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting. |
| Step 11 | For each event type that you chose in Step 10, check the Urgent Only check box to have Connection send the notification only when the new message of that type is marked urgent. |
| Step 12 | If you specified either Calendar Appointments or Calendar Meetings in Step 10, in the Calendar Event Advance Notification Time field, enter the number of minutes before a meeting that you want to receive the notification. |
| Step 13 | If you want to receive transcriptions of your voice messages, check the Voice Messages check box under Send Transcriptions of Voice Messages. (The Send Transcriptions of Voice Messages section is visible only if the SpeechView option has been made available to you.) |
| Step 14 | To receive transcriptions of only urgent voice messages, check the Urgent Only check box. |
| Step 15 | Check the Limit the Number of SMS Messages Per Transcription To check box and enter the maximum number of SMS messages you want for each message transcription. This setting is useful for reducing costs if your mobile phone carrier or SMS service provider charges for each SMS message
                                             that you receive. |
| Step 16 | To specify that this device will receive notifications only for messages from specific Connection users, select Add Callers , then search for names: In the Find Names dialog box, enter search criteria, then select Find . In the search results, select the check box next to the user or remote contact  that you want to add to your Callers list,
                                                then select Add Users . |
| Step 17 | To specify that this device receive notifications only for messages from specific phone numbers, enter a phone number in the Number Pattern field. You can use the wildcard characters X and * to match more than one phone number: The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                   numbers from 9000 through 9999. The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                   55563040, 55563041, 5556304100, and so forth. Tip If you specify both Callers and Phone Numbers for a device, Connection will send the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify. | Tip | If you specify both Callers and Phone Numbers for a device, Connection will send the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify. |
| Tip | If you specify both Callers and Phone Numbers for a device, Connection will send the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify. |
| Step 18 | To set up your notification schedule, use the Quick Add options to specify a schedule. Or Check or uncheck the check boxes in the schedule to specify the active and inactive hours for the notification device. Connection
                                             makes notification calls during the active hours, if you have new messages. When a new message arrives during inactive hours,
                                             Connection sends a message notification at the start of the next active hour in your schedule. Tip There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check boxes at once. Alternatively, select Invert Schedule to check all the boxes that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days. | Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check boxes at once. Alternatively, select Invert Schedule to check all the boxes that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days. |
| Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check boxes at once. Alternatively, select Invert Schedule to check all the boxes that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days. |
| Step 19 | Specify the timing and frequency of the calls made by Connection to notify you of new messages: Option Description Attempt First Contact After <x> Minutes Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. If There Are Still New Messages, Try Again Every <x> Minutes To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. Caution If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. | Option | Description | Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. | If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. Caution If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. | Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
| Option | Description |
| Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. |
| If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. Caution If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. | Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
| Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
| Step 20 | Select Save . |

| Tip | For SMS devices, consider that some service providers replace the number that you enter in the From field with their own phone
                                                         number. For an alternative method of including a callback number, try entering the number within the text of your message.
                                                         For example, enter: tel:2065551234 in the Text field (see Step 6). |
|---|---|

| Option | Description |
|---|---|
| All Messages | Connection sends a notification to this device when any new message is received, including dispatch and other voice messages,
                                                      and fax messages. |
| All Voice Messages | Connection sends a notification to this device when any new voice message is received (including dispatch messages). |
| Dispatch Messages | Connection sends a notification to this device when any new voice message is received that is marked as a dispatch message. |
| Fax Messages | Connection sends a notification to this device when any new fax message is received. |
| Calendar Appointments | Connection sends a notification to this device for an upcoming Outlook appointment. |
| Calendar Meetings | Connection sends a notification to this device for an upcoming Cisco Unified MeetingPlace or Cisco Unified MeetingPlace Express
                                                      meeting. |

| Tip | If you specify both Callers and Phone Numbers for a device, Connection will send the device a notification for any message—of
                                                         the types you specified in Step 10 and Step 11—that matches any of the callers or number patterns you specify. |
|---|---|

| Tip | There are several ways to set up your notification schedule quickly. Select Clear Schedule to uncheck all check boxes at once. Alternatively, select Invert Schedule to check all the boxes that you currently do not have checked and uncheck the ones that you do have checked. You can use
                                                         the Copy Day’s Schedule function—below the schedule—to copy a schedule for one day to other days. |
|---|---|

| Option | Description |
|---|---|
| Attempt First Contact After <x> Minutes | Enter the number of minutes that Connection waits to make the first notification call once message notification is triggered. If the delay time takes the notification out to a time when the device schedule is no longer active, the notification does
                                                      not take place until the schedule becomes active again (as long as the message is still new). You can space notifications
                                                      on different devices at regular intervals, such as 15 minutes, to achieve a cascading message notification effect. |
| If There Are Still New Messages, Try Again Every <x> Minutes | To have Connection repeat the notification as long as you have new messages, check this check box and enter the number of
                                                      minutes that Connection waits before repeating the notification. The range for the redial frequency field is 1 to 60 minutes. For example, if you set the repeat notification interval to 5 minutes at 11:47 a.m., Connection will notify you of new messages
                                                      at 11:50 a.m., 11:55 a.m., 12:00 p.m., 12:05 p.m., 12:10 p.m., 12:15 p.m., 12:20 p.m., 12:25 p.m., etc. Caution If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. | Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
| Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |

| Caution | If you are using the transcription delivery option, do not enable this setting. Checking the check box disables transcription
                                                                  delivery to this device. |
|---|---|

| Step 1 | In the
                                          			 Messaging Assistant, from the Notification Devices menu, select View
                                             				Notification Devices . |
|---|---|
| Step 2 | On the
                                          			 Notification Devices page, select the HTML device that you want to change or set up. |
| Step 3 | On the
                                          			 <Device name> Notification Device page, check the Notification
                                             				Enabled check box to enable the device, or uncheck it to disable the
                                          			 service. |
| Step 4 | In the To
                                          			 field, enter a valid email address. |
| Step 5 | In the Select
                                          			 HTML Template drop-down list, select a default or customized template. The
                                          			 default templates are Default_Actionable_Links_Only, Default_Missed_Call,
                                          			 Default_Missed_Call_With_Summary, Default_Scheduled_Summary,
                                          			 Default_Voice_Message_With_Summary and Default_Dynamic_Icons. Note that this
                                             				field will be inactive if the administrator has not given rights to the user to
                                             				select an HTML template. |
| Step 6 | Click Preview to
                                          			 view format of an HTML notification for the selected template. The Preview option is available only after creating and saving a template. |
| Step 7 | In the Outdial
                                          			 Number field, enter the phone number that you will use to check the
                                          			 notifications. This field will be inactive if the administrator has not given
                                          			 rights to the user to enter mobile number from PCA. The number entered over
                                          			 here must be E164 compliance. |
| Step 8 | To specify
                                          			 that device will receive notifications as per the Event Type section under Notify Me
                                             				Of field: Check All Voice
                                                   					 Messages event type check box to send the notification of new voice
                                                				  message. Check the Urgent
                                                   					 Only check box to send the notification only when the new voice message is
                                                				  marked urgent. Check Missed
                                                   					 Call event type check box to send the notification of new missed call. |
| Step 9 | To specify
                                          			 that this device receive notifications only for messages from specific
                                          			 Connection users, select Add
                                             				Callers , and then search for names: Select the users to be added to receive notification and click Add Member(s) . Select the user to be removed from the notification list and
                                                				  click Delete Selected button. |
| Step 10 | To specify
                                          			 that this device receive notifications only for messages from specific phone
                                          			 numbers, enter a phone number in the Number
                                             				Pattern field. You can use
                                             				the wildcard characters X and * to match more than one phone number: The X
                                                   					 character matches any single digit in the range 0 through 9. For example, the
                                                   					 pattern 9XXX matches the range of phone numbers from 9000 through 9999. The
                                                   					 asterisk (*) character matches any sequence of digits. For example, the pattern
                                                   					 5556304* matches the phone numbers 5556304, 55563040, 55563041, 5556304100, and
                                                   					 so forth. Tip If you
                                                         				  specify both callers and phone numbers for a device, Connection will send the
                                                         				  device a notification for any message, irrespective of the types you specified
                                                         				  in Step 9 that matches any of the callers or number patterns you specify. | Tip | If you
                                                         				  specify both callers and phone numbers for a device, Connection will send the
                                                         				  device a notification for any message, irrespective of the types you specified
                                                         				  in Step 9 that matches any of the callers or number patterns you specify. |
| Tip | If you
                                                         				  specify both callers and phone numbers for a device, Connection will send the
                                                         				  device a notification for any message, irrespective of the types you specified
                                                         				  in Step 9 that matches any of the callers or number patterns you specify. |
| Step 11 | To set up
                                          			 your Summary Notification schedule: Enter a value less than or equal to 100 in the Max Message Count field to specify the maximum number of
                                                				  messages that can be included in a Summary Notification. By default, the Max
                                                				  message count is set to 10. Click Add to specify a schedule. Enter the time when you want Unity Connection to send Summary
                                                				  Notification in the Send Notification At field. Multiple time slots can
                                                				  also be added. Tip Select Clear All to uncheck all the check boxes at once. Alternatively, click Select
                                                            					 All to check all the boxes at once. You can also delete the scheduled time
                                                         				  by selecting the check boxes and clicking Delete
                                                            					 Selected . | Tip | Select Clear All to uncheck all the check boxes at once. Alternatively, click Select
                                                            					 All to check all the boxes at once. You can also delete the scheduled time
                                                         				  by selecting the check boxes and clicking Delete
                                                            					 Selected . |
| Tip | Select Clear All to uncheck all the check boxes at once. Alternatively, click Select
                                                            					 All to check all the boxes at once. You can also delete the scheduled time
                                                         				  by selecting the check boxes and clicking Delete
                                                            					 Selected . |
| Step 12 | To set up
                                          			 your notification schedule, do either of the following: Use the Add options to specify a schedule, or Check or
                                                      					 uncheck the check boxes in the schedule to specify the active and inactive
                                                      					 hours for the notification device. Connection makes notification calls during the active hours, if
                                             			 you have new messages. When a new message arrives during inactive hours,
                                             			 Connection sends a message notification at the start of the next active hour in
                                             			 your schedule. Tip There are
                                                         				  several ways to set up your notification schedule quickly. Select Clear
                                                            					 Schedule to uncheck all check boxes at once. Alternatively, click Invert
                                                            					 Schedule to check all the boxes that you currently do not have checked and
                                                         				  uncheck the ones that you do have checked. You can use the Copy Day's
                                                            					 Schedule option to copy a schedule from one day to other days. | Tip | There are
                                                         				  several ways to set up your notification schedule quickly. Select Clear
                                                            					 Schedule to uncheck all check boxes at once. Alternatively, click Invert
                                                            					 Schedule to check all the boxes that you currently do not have checked and
                                                         				  uncheck the ones that you do have checked. You can use the Copy Day's
                                                            					 Schedule option to copy a schedule from one day to other days. |
| Tip | There are
                                                         				  several ways to set up your notification schedule quickly. Select Clear
                                                            					 Schedule to uncheck all check boxes at once. Alternatively, click Invert
                                                            					 Schedule to check all the boxes that you currently do not have checked and
                                                         				  uncheck the ones that you do have checked. You can use the Copy Day's
                                                            					 Schedule option to copy a schedule from one day to other days. |

| Tip | If you
                                                         				  specify both callers and phone numbers for a device, Connection will send the
                                                         				  device a notification for any message, irrespective of the types you specified
                                                         				  in Step 9 that matches any of the callers or number patterns you specify. |
|---|---|

| Tip | Select Clear All to uncheck all the check boxes at once. Alternatively, click Select
                                                            					 All to check all the boxes at once. You can also delete the scheduled time
                                                         				  by selecting the check boxes and clicking Delete
                                                            					 Selected . |
|---|---|

| Tip | There are
                                                         				  several ways to set up your notification schedule quickly. Select Clear
                                                            					 Schedule to uncheck all check boxes at once. Alternatively, click Invert
                                                            					 Schedule to check all the boxes that you currently do not have checked and
                                                         				  uncheck the ones that you do have checked. You can use the Copy Day's
                                                            					 Schedule option to copy a schedule from one day to other days. |
|---|---|

| Tip | To include an email or SMS device in a chaining message notification, you must specify the device as last in the chain, because
                                       Connection may not be able to detect notification failure for these types of devices. |
|---|---|