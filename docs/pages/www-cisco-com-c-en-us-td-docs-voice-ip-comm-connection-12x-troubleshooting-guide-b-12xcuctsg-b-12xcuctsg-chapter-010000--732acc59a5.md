---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-010000--732acc59a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_010000.html
retrieved_at: 2026-08-17T02:29:27.219083+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting Notification Devices

## Chapter: Troubleshooting Notification Devices

# Troubleshooting Notification Devices

Troubleshooting Notification Devices

## Overview

Cisco Unity Connection can be configured to call a phone or pager or send text or SMS messages to notify users of new messages
                           and calendar events. See the following sections for information on troubleshooting problems with notification devices:

## Message Notifications through Phones is Slow for Multiple Users

When message notification through phones is slow for multiple users, use the following task list to determine the cause and
                           to resolve the problem.

Following are the tasks to troubleshoot slow message notifications through phones for multiple users:

Confirm that ports are not too busy to handle message notification. See the “Ports Too Busy to Make Notification Calls Promptly” section on page 16-1 .

Confirm that there are enough ports assigned to message notification. See the “Not Enough Ports Set for Message Notification Only” section on page 16-2 .

Confirm that the phone system sends calls to ports that are set to answer calls. See the “Confirm that Phone System Sends Calls to the Ports Set to Answer Calls” section on page 16-2 .

### Ports Too Busy to Make Notification Calls Promptly

When the ports that make notification calls are also set to perform other operations, they may be too busy to make notification
                              calls promptly. You can improve notification performance by dedicating a small number of ports to exclusively make notification
                              calls.

Systems that handle a large volume of calls may require additional ports to improve notification performance.

#### Reviewing Port
                              	 Configuration for Message Notification

In Cisco Unity Connection Administration, expand Telephony Integrations , then select Port .

On the Search Ports page, review the existing port configuration
                                             			 and determine whether one or more ports can be set to dial out for message
                                             			 notification only.

### Not Enough Ports Set for Message Notification Only

When a small number of ports are set to make notification calls and Unity Connection takes a lot of messages, the notification
                              ports may not always be able to dial out promptly.

If the percentage of ports used for dialing out for message notification exceeds 70 percent usage during peak periods, review
                              the existing port configuration and determine whether more ports can be set to dial out for message notification only.

If the percentage of ports used for dialing out for message notification does not exceed 70 percent usage during peak periods,
                              the number of notification ports is adequate. Contact Cisco TAC to resolve the problem.

#### Determining if
                              	 Number of Message Notification Ports is Adequate

In Cisco Unity Connection Serviceability, expand Tools and
                                             			 select Reports .

On the Serviceability Reports page, select Port Activity Report .

On the Port Activity Report page, select the applicable file
                                             			 format for the report output.

Set a date range by selecting the beginning and ending month,
                                             			 day, year, and time.

Select Generate Report .

View the report output, depending on the file format that you
                                             			 chose in Step 3 .

If the port usage during peak periods does not exceed 70
                                             			 percent, the number of message waiting indication ports is adequate. Skip the
                                             			 remaining steps in this procedure.

If the port usage during peak periods exceeds 70 percent, in
                                                				Cisco Unity Connection Administration, expand Telephony Integrations , then select Port .

On the Search Ports page, review the existing port configuration
                                             			 and determine whether more ports can be set to dial out for message
                                             			 notification only.

### Confirm that Phone System Sends Calls to the Ports Set to Answer Calls

If the phone system is programmed to send calls to a port on Unity Connection that is not configured to answer calls, it is
                              possible for a call collision to occur, which can freeze the port.

#### Confirming That
                              	 Calls Are Being Sent to the Correct Cisco Unity Connection Ports

In Cisco Unity Connection Administration, expand Telephony Integrations > and select Port .

In the phone system programming, confirm that calls are only
                                             			 being sent to ports set to answer calls. Change the phone system programming if
                                             			 necessary.

If you make a change to the phone system programming, in
                                             			 Cisco Unity Connection Administration, select the display name of the port that
                                             			 you changed in Step 2 .

On the Port Basics page, under Phone System Port, select Restart .

When prompted that restarting the port terminates any call that
                                             			 the port is currently handling, select OK .

Repeat Step 3 through Step 5 for all
                                             			 remaining ports that you changed in Step 2 .

## Message Notification Slow for a User

There are several possible reasons that message notification may appear to be slow for a user. Use the following task list
                           to troubleshoot the possible causes:

The user settings may not be adequate for the needs of the user. See the “Message Notification Setup is Inadequate” section on page 16-3 .

The user settings may need adjustment to more correctly map to the work schedule of the user. See the “Notification Attempts are Missed” section on page 16-3 .

The user may not clearly understand how repeat notifications are handled by Cisco Unity Connection. See the “Repeat Notification Option is Misunderstood” section on page 16-4 .

### Message Notification Setup is Inadequate

When a user complains that notification calls are not being received when expected, the problem may be with the notification
                              settings.

#### Determining
                              	 Whether Notification Setup is Adequate

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user.

On the Edit User Basics page, on the Edit menu, select Notification Devices .

On the Notification Devices page, select the display name of the
                                             			 correct notification device.

On the Edit Notification Device page, confirm that the
                                             			 notification device is configured to meet the needs of the user. If the user
                                             			 has selected a very busy phone for Unity Connection to call, ask the user if
                                             			 there is an alternate device to use for message notification.

In the Related Links list, select Edit Notification Device Details , and select Go . Verify with the user that the notification
                                             			 schedule that is specified on the Cisco Personal Communications Assistant page
                                             			 is consistent with the days and times that the user is available to receive
                                             			 notification calls.

### Notification Attempts are Missed

A user who is frequently away from or busy using a notification device (especially when the device is a phone) may repeatedly
                              miss notification attempts. To the user, it appears that Cisco Unity Connection has delayed message notification.

#### Resolving Missed
                              	 Notification Attempts

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user.

On the Edit User Basics page, on the Edit menu, select Notification Devices .

On the Notification Devices page, select the display name of the
                                             			 correct notification device.

On the Edit Notification Device page, check the Repeat Notification If There Are Still New Messages check box.

If the user has another notification device available, for On
                                             			 Notification Failure, select Send To , and select the device.

Because Unity Connection does not detect notification failure
                                                            				  for SMTP devices, the On Notification Failure field is not available for
                                                            				  notification devices of this type.

For phone or pager notification devices, in the Busy Retry Limit
                                             			 and RNA Retry Limit fields, increase the numbers so that Unity Connection makes
                                             			 more notification calls when the device does not answer or is busy.

For phone or pager notification devices, in the Busy Retry
                                             			 Interval and RNA Retry Interval fields, decrease the numbers so that Unity
                                             			 Connection makes notification calls more often when the device does not answer
                                             			 or is busy.

Select Save .

If you chose another device in Step 5 , do the
                                             			 following sub-steps:

On the Edit User Basics page, on the Edit menu, select Notification Devices .

On the Notification Devices page, select the display name of the
                                                   				  correct notification device.

On the Edit Notification Device page, enter settings for the
                                                   				  additional device and select Save .

For phone notification devices, suggest that the user set up an
                                             			 answering machine for the notification phone, so that notification calls are
                                             			 received even when the user is unavailable.

When Unity Connection is set to call a phone that has an
                                                				answering machine, verify with the user that the answering machine greeting is
                                                				short enough so that the machine starts recording before the notification
                                                				message is repeated.

### Repeat Notification Option is Misunderstood

Setting Unity Connection to repeat notification at a particular interval when there are still new messages can be useful for
                              users who receive a lot of messages but who do not need immediate notification. However, when a user chooses not to have Unity
                              Connection restart notification each time a new message arrives, setting a long interval between repeat notification calls
                              may lead the user to believe that Unity Connection is delaying notification.

#### Resolving a Repeat
                              	 Notification Problem

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user.

On the Edit User Basics page, on the Edit menu, select Notification Devices .

On the Notification Devices page, select the display name of the
                                             			 correct notification device.

On the Edit Notification Device page, in the Notification Repeat
                                             			 Interval box, set a shorter interval, such as 15 minutes and select Save .

## Message
                        	 Notification Not Working at All

There are several possible
                           		reasons that message notification may not work at all for a user or group of
                           		users. Use the following task list to troubleshoot the possible causes:

For all types of notification device: Confirm that the notification device is enabled and that the
                                 			 notification schedule is set correctly. See the “Notification
                                    				Device Disabled or the Schedule Inactive” section .

Confirm that message notification is enabled for the correct
                           		types of messages. See the “Only
                              		  Certain Types of Messages Set to Trigger Notification” section .

For phone or pager notification devices: Confirm that the message notification phone number is correct and
                                 			 that it includes the access code for an external line if notification is to an
                                 			 external phone. See the “Notification
                                    				Number Incorrect or Access Code for an External Line Missing (Phone and Pager
                                    				Notification Devices Only)” section .

Confirm that the notification device is assigned to the correct
                           		phone system. See the Message Notification Not Working at All section.

For SMS notification devices: See the “SMS
                                    				Notifications Not Working” section for additional troubleshooting steps.

For SMTP notification devices: See the “SMTP
                                    				Message Notification Not Working at All for Multiple Users” section for
                                 			 additional troubleshooting steps.

### Notification Device Disabled or the Schedule Inactive

When you are troubleshooting message notifications, start by confirming that the device is enabled, and that the notification
                              schedule for the device is currently active.

#### Verifying a Device
                              	 Status and Schedule

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user.

On the Edit User Basics page, on the Edit menu, select Notification Devices .

On the Notification Devices page, select the display name of the
                                             			 correct notification device.

On the Edit Notification Device page, confirm that the Enabled check box is checked.

In the Related Links list, select Edit Notification Device Details , and select Go . Verify with the user that the notification
                                             			 schedule that is specified on the Cisco Personal Communications Assistant page
                                             			 is consistent with the days and times that the user is available to receive
                                             			 notification calls.

### Only Certain Types of Messages Set to Trigger Notification

Unity Connection can be set so that a user is notified only of certain types of messages. For example, if user notification
                              is set up only for urgent voice messages, regular voice messages do not trigger the notification device.

#### Changing the
                              	 Message Types That Trigger a Notification Device

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user.

On the Edit User Basics page, on the Edit menu, select Notification Devices .

On the Notification Devices page, select the display name of the
                                             			 correct notification device.

On the Edit Notification Device page, under Notification Rule
                                             			 Events, verify the selected message types with the user.

### Notification Number Incorrect or Access Code for an External Line Missing (Phone and Pager Notification Devices Only)

If notifications to a phone or pager are not working at all, the user may have entered a wrong phone number for Unity Connection
                              to call.

To place an external call, a user usually must dial an access code (for example, 9) to get an external line. When the phone
                              system requires an access code, an external message notification phone number set in Unity Connection must include the access
                              code.

In addition, some phone systems may require a brief pause between dialing the access code and being connected to an external
                              line.

#### Verifying the
                              	 Device Phone Number and Access Code for a Phone or Pager Notification
                              	 Device

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user.

On the Edit User Basics page, on the Edit menu, select Notification Devices .

On the Notification Devices page, select the display name of the
                                             			 correct notification device.

On the Edit Notification Device page, under Phone Settings,
                                             			 confirm that the correct access code and phone number are entered in the Phone
                                             			 Number field for the device.

If the phone system requires a pause, enter two commas between
                                                				the access code and the phone number (for example, 9,,5551234).

#### Testing a Phone or
                              	 Pager Notification Device

If the notification device is a home phone or another phone away
                                    		  from the office, ask the user to have someone available to answer the phone
                                    		  during the test.

Confirm that the notification device is on.

Set up a test phone (Phone 1) for single-line testing. Use a
                                          				line connected to a port that is set to dial out for message notification.

On Phone 1, dial the notification number set in Unity Connection
                                          				for the device.

If the pager is activated or the phone rings, you have confirmed
                                    		  that Unity Connection can call the device.

If the pager is not activated or the phone does not ring, there
                                    		  may be a problem with the device. Consult the documentation from the device
                                    		  manufacturer, or ask the user to obtain a different notification device and
                                    		  repeat the test.

If the notification device is a mobile phone or pager, ask the
                                             			 user to have it available for the test.

#### Notification Device Phone System Assignment Incorrect (Phone and Pager Notification Devices Only)

##### Verifying Notification Device Phone System Assignment

### SUMMARY STEPS

- In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search Results table, select the alias of the applicable user.

- On the Edit User Basics page, on the Edit menu, select Notification Devices .

- On the Notification Devices page, select the display name of the correct notification device.

- On the Edit Notification Device page, under Phone Settings, note the phone system that is specified in the Phone System field.

- In Cisco Unity Connection Administration, expand Telephony Integrations , then select Port .

- On the Search Ports page, confirm that the phone system assigned to the notification device has at least one port designated
                                       for message notification. Correct the port settings if necessary.

### DETAILED STEPS

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search Results table, select the alias of the applicable user.

On the Edit User Basics page, on the Edit menu, select Notification Devices .

On the Notification Devices page, select the display name of the correct notification device.

On the Edit Notification Device page, under Phone Settings, note the phone system that is specified in the Phone System field.

In Cisco Unity Connection Administration, expand Telephony Integrations , then select Port .

On the Search Ports page, confirm that the phone system assigned to the notification device has at least one port designated
                                                for message notification. Correct the port settings if necessary.

### SMS Notifications Not Working

If SMS notifications are not working, in Cisco Unity Connection Administration, check the settings on the System Settings >
                              Advanced > SMPP Providers > Edit SMPP Provider page to confirm that the settings match the settings specified by the provider.

If settings on the Edit SMPP Provider page are correct, enable the SMS Device (level 30) micro trace to collect trace information
                              that helps you troubleshoot the problem. For detailed instructions on enabling and collecting diagnostic traces, see the “Diagnostic Traces” chapter.

Common error codes and explanations for SMS problems are listed in the following table:

SmppConnect failed

Unity Connection was unable to connect to the SMPP provider.

SmppBindTransmitter failed

Unity Connection was unable to sign in to the SMPP provider.

SmppSubmitSm failed

Unity Connection was unable to submit the SMS message to the SMPP provider.

### SMTP Message Notification Not Working at All for Multiple Users

If SMTP notifications are not working, in Cisco Unity Connection Administration, check the System Settings > SMTP Configuration >
                              Smart Host page to confirm that a smart host is configured. To enable Unity Connection to send text message notifications
                              using SMTP, your Unity Connection server must be configured to relay messages through a smart host.

If a smart host is already configured on the Smart Host page, note the IP address or host name of the smart host and check
                              to make sure that this smart host is configured to accept messages from the Unity Connection server.

If the smart host settings are configured correctly, you can use traces to track whether the SMTP notification messages are
                              being sent by the Unity Connection server. The default SMTP micro traces (levels 10, 11, 12 and 13) indicate if there is a
                              permanent problem with delivery of a notification message to the smart host. The SMTP micro trace level 18 (Network Messages)
                              shows the details if the notification message is delivered to the smart host. For detailed instructions on enabling and collecting
                              diagnostic traces, see the “Diagnostic Traces” chapter.

## HTML Notifications
                        	 Not Working

If HTML notifications are not
                           		working, in Cisco Unity Connection Administration, check the HTML notification
                           		device under User > Edit > Notification Devices page is enabled and valid
                           		email address is added.

Also, verify that SMTP smart host is configured on Unity Connection
                           		Administration page and the Connection SMTP Server and Connection Notifier
                           		services are up and running.

## HTML Summary
                        	 Notification Not Working

If HTML Summary
                           		notifications are not working, verify that the correct template for Summary
                           		Notification is used under User > Edit > Notification Devices page on
                           		Connection Administration page. If the correct template is used, verify that
                           		valid <VOICE_MESSAGE_SUMMARY> tags are present inside the notification
                           		template with valid replaceable parameters are used inside the
                           		<VOICE_MESSAGE_SUMMARY> tags. For more information on missed call
                           		notification templates, see the Notifications chapter
                           		of System Administration Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html

## Message
                        	 Notifications Function Intermittently

A possible cause for notification devices (such
                           		as phones, pagers, SMTP, and SMS) to function intermittently is that the
                           		schedule for the notification device for the user is not active during the time
                           		in question.

To correct the problem, edit the schedules of the notification
                           		devices for the user so that the notification devices are active when the user
                           		wants message notifications delivered. You must sign in to the user account in
                           		the Cisco Personal Communications Assistant (PCA) to modify the schedule for
                           		notification devices.

Cisco Unity Connection Administration does not expose schedules
                           		for notification devices. From the Notification Device page for the user in
                           		Unity Connection Administration, you can navigate to the Cisco PCA page for the
                           		user by selecting the Edit Notification Device Details link in the Related
                           		Links list.

For details on using the Cisco PCA, see the User Guide for the
                           		Cisco Unity Connection Messaging Assistant Web Tool (Release 12.x) at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/assistant/b_12xcucugasst.html .

## Notification
                        	 Devices Added in Unity Connection Administration Triggered at All Hours

When a notification device is added for a
                           		user in Cisco Unity Connection Administration, by default, the device is active
                           		at all times. If a user is receiving notifications at unexpected times, you can
                           		modify the notification device schedule to prevent this. You must sign in to
                           		the user account in the Cisco Personal Communications Assistant (PCA) to modify
                           		the schedule for notification devices.

Unity Connection Administration does not expose schedules for
                           		notification devices. From the Notification Device page for the user in Unity
                           		Connection Administration, you can navigate to the Cisco PCA page for the user
                           		by selecting the Edit Notification Device Details link in the Related Links
                           		list.

For details on using the Cisco PCA, see the User Guide for the
                           		Cisco Unity Connection Messaging Assistant Web Tool (Release 12.x) at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/assistant/b_12xcucugasst.html .

## Message
                        	 Notification Received When No Unread Messages

When users are members of a distribution list that is the
                           		recipient of a call handler that is configured to mark messages for dispatch
                           		delivery, it is possible for a user to receive a message notification for a
                           		message that no longer appears in the user inbox when he or she attempts to
                           		access it. This can happen because another member of the distribution list has
                           		accepted the message between the time that the notification was sent and the
                           		time that the user tries to listen to the message.

When configuring message notification rules to include dispatch
                           		messages, make users aware that by the time they receive the notification and
                           		call in to retrieve the message, it may be gone from their mailboxes because
                           		another user has already accepted the message.

For more information on dispatch messages, see the “ Dispatch Messages ”
                           		section in the “Messaging” chapter of the System Administration Guide for
                           		Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations , then select Port . |
|---|---|
| Step 2 | On the Search Ports page, review the existing port configuration
                                             			 and determine whether one or more ports can be set to dial out for message
                                             			 notification only. |

| Step 1 | In Cisco Unity Connection Serviceability, expand Tools and
                                             			 select Reports . |
|---|---|
| Step 2 | On the Serviceability Reports page, select Port Activity Report . |
| Step 3 | On the Port Activity Report page, select the applicable file
                                             			 format for the report output. |
| Step 4 | Set a date range by selecting the beginning and ending month,
                                             			 day, year, and time. |
| Step 5 | Select Generate Report . |
| Step 6 | View the report output, depending on the file format that you
                                             			 chose in Step 3 . |
| Step 7 | If the port usage during peak periods does not exceed 70
                                             			 percent, the number of message waiting indication ports is adequate. Skip the
                                             			 remaining steps in this procedure. If the port usage during peak periods exceeds 70 percent, in
                                                				Cisco Unity Connection Administration, expand Telephony Integrations , then select Port . |
| Step 8 | On the Search Ports page, review the existing port configuration
                                             			 and determine whether more ports can be set to dial out for message
                                             			 notification only. |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations > and select Port . |
|---|---|
| Step 2 | In the phone system programming, confirm that calls are only
                                             			 being sent to ports set to answer calls. Change the phone system programming if
                                             			 necessary. |
| Step 3 | If you make a change to the phone system programming, in
                                             			 Cisco Unity Connection Administration, select the display name of the port that
                                             			 you changed in Step 2 . |
| Step 4 | On the Port Basics page, under Phone System Port, select Restart . |
| Step 5 | When prompted that restarting the port terminates any call that
                                             			 the port is currently handling, select OK . |
| Step 6 | Repeat Step 3 through Step 5 for all
                                             			 remaining ports that you changed in Step 2 . |

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the display name of the
                                             			 correct notification device. |
| Step 4 | On the Edit Notification Device page, confirm that the
                                             			 notification device is configured to meet the needs of the user. If the user
                                             			 has selected a very busy phone for Unity Connection to call, ask the user if
                                             			 there is an alternate device to use for message notification. |
| Step 5 | In the Related Links list, select Edit Notification Device Details , and select Go . Verify with the user that the notification
                                             			 schedule that is specified on the Cisco Personal Communications Assistant page
                                             			 is consistent with the days and times that the user is available to receive
                                             			 notification calls. |

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the display name of the
                                             			 correct notification device. |
| Step 4 | On the Edit Notification Device page, check the Repeat Notification If There Are Still New Messages check box. |
| Step 5 | If the user has another notification device available, for On
                                             			 Notification Failure, select Send To , and select the device. Note Because Unity Connection does not detect notification failure
                                                            				  for SMTP devices, the On Notification Failure field is not available for
                                                            				  notification devices of this type. | Note | Because Unity Connection does not detect notification failure
                                                            				  for SMTP devices, the On Notification Failure field is not available for
                                                            				  notification devices of this type. |
| Note | Because Unity Connection does not detect notification failure
                                                            				  for SMTP devices, the On Notification Failure field is not available for
                                                            				  notification devices of this type. |
| Step 6 | For phone or pager notification devices, in the Busy Retry Limit
                                             			 and RNA Retry Limit fields, increase the numbers so that Unity Connection makes
                                             			 more notification calls when the device does not answer or is busy. |
| Step 7 | For phone or pager notification devices, in the Busy Retry
                                             			 Interval and RNA Retry Interval fields, decrease the numbers so that Unity
                                             			 Connection makes notification calls more often when the device does not answer
                                             			 or is busy. |
| Step 8 | Select Save . |
| Step 9 | If you chose another device in Step 5 , do the
                                             			 following sub-steps: On the Edit User Basics page, on the Edit menu, select Notification Devices . On the Notification Devices page, select the display name of the
                                                   				  correct notification device. On the Edit Notification Device page, enter settings for the
                                                   				  additional device and select Save . |
| Step 10 | For phone notification devices, suggest that the user set up an
                                             			 answering machine for the notification phone, so that notification calls are
                                             			 received even when the user is unavailable. When Unity Connection is set to call a phone that has an
                                                				answering machine, verify with the user that the answering machine greeting is
                                                				short enough so that the machine starts recording before the notification
                                                				message is repeated. |

| Note | Because Unity Connection does not detect notification failure
                                                            				  for SMTP devices, the On Notification Failure field is not available for
                                                            				  notification devices of this type. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the display name of the
                                             			 correct notification device. |
| Step 4 | On the Edit Notification Device page, in the Notification Repeat
                                             			 Interval box, set a shorter interval, such as 15 minutes and select Save . |

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the display name of the
                                             			 correct notification device. |
| Step 4 | On the Edit Notification Device page, confirm that the Enabled check box is checked. |
| Step 5 | In the Related Links list, select Edit Notification Device Details , and select Go . Verify with the user that the notification
                                             			 schedule that is specified on the Cisco Personal Communications Assistant page
                                             			 is consistent with the days and times that the user is available to receive
                                             			 notification calls. |

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the display name of the
                                             			 correct notification device. |
| Step 4 | On the Edit Notification Device page, under Notification Rule
                                             			 Events, verify the selected message types with the user. |

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search
                                             			 Results table, select the alias of the applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the display name of the
                                             			 correct notification device. |
| Step 4 | On the Edit Notification Device page, under Phone Settings,
                                             			 confirm that the correct access code and phone number are entered in the Phone
                                             			 Number field for the device. If the phone system requires a pause, enter two commas between
                                                				the access code and the phone number (for example, 9,,5551234). |

| If the notification device is a mobile phone or pager, ask the
                                             			 user to have it available for the test. |
|---|

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, in the Search Results table, select the alias of the applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the display name of the correct notification device. |
| Step 4 | On the Edit Notification Device page, under Phone Settings, note the phone system that is specified in the Phone System field. |
| Step 5 | In Cisco Unity Connection Administration, expand Telephony Integrations , then select Port . |
| Step 6 | On the Search Ports page, confirm that the phone system assigned to the notification device has at least one port designated
                                                for message notification. Correct the port settings if necessary. |

| SmppConnect failed | Unity Connection was unable to connect to the SMPP provider. |
|---|---|
| SmppBindTransmitter failed | Unity Connection was unable to sign in to the SMPP provider. |
| SmppSubmitSm failed | Unity Connection was unable to submit the SMS message to the SMPP provider. |