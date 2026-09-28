---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-01110-h-a570f1a26c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_01110.html
retrieved_at: 2026-08-17T02:29:19.060741+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting Message Waiting Indicators (MWIs)

## Chapter: Troubleshooting Message Waiting Indicators (MWIs)

# Troubleshooting Message Waiting Indicators (MWIs)

Troubleshooting Message Waiting Indicators (MWIs)

## Triggers for
                        	 Turning MWIs On and Off

An MWI is a
                           		lamp, flashing LCD panel, or special dial tone on user phones that lets users
                           		know a voice message is waiting. The type of indicator depends on the phone
                           		system and the user phones. Phone systems that support message counts may also
                           		display the number of messages that the user has.

MWIs are not the same as message notification, which is the
                           		feature that notifies a user of new voice messages by calling a phone, pager,
                           		or other device, or by sending an email message.

The following events trigger Unity Connection to turn MWIs on
                           		and off:

When a message for a user arrives on the Unity Connection
                                 			 message store, Unity Connection notifies the phone system to turn on an MWI on
                                 			 the phone for that user.

Any message that arrives on the Unity Connection message store
                           		(for example, voice messages, emails, and faxes) trigger turning MWIs on and
                           		off.

When the user saves or deletes a read message, Unity Connection
                                 			 notifies the phone system to turn off the MWI on the phone.

When a user deletes a new message without listening to it, Unity
                                 			 Connection notifies the phone system to turn off the MWI on the phone.

When MWIs are synchronized, Unity Connection queries the message
                                 			 store to determine the status of MWIs on all phones, and resets the applicable
                                 			 MWIs.

However, an MWI remains on under the following conditions:

More messages are waiting to be heard. When all new messages are
                                 			 listened to, the MWI is turned off.

A new message arrives while the user is listening to the
                                 			 original message. When all new messages are listened to, the MWI is turned off.

The user listens on the phone to only part of the message, then
                                 			 either hangs up or skips to the next message before hearing the entire message.

The user listens
                                 			 the entire message. You can perform either of the following to turn off the
                                 			 MWI:

- Save or Delete the message
                                       				after listening it.

- In Cisco Unity Connection
                                       				Administration, Select Users .
                                       				On the Search Users page, Select the alias of the user. On the Edit User Basics
                                       				page of the user, navigate Edit > Playback Message Settings. On the Playback
                                       				Message Settings page, Select Saved under When
                                          				  Disconnected or User Hangs Up During Message Playback field.

In an email application, in the Web Inbox, or Messaging Inbox ,
                                 			 the user marks a listened-to message as unread.

Messages in an external message store do not trigger Unity
                           		Connection to turn MWIs on and off.

## MWI Problems

See the following sections for information on troubleshooting problems with MWIs.

### MWIs Do Not Turn
                           	 On or Off

When MWIs do not turn on or off, use
                              		the following task list to determine the cause and to resolve the problem. Do
                              		the tasks in the order presented until the problem is resolved.

Following are the tasks to troubleshoot when MWIs do not turn on
                              		or off:

Run the Check Telephony Configuration test. See the “Running
                                       				the Check Telephony Configuration Test” section on page 15-3 .

Confirm that there are voice messaging ports for the phone
                                    			 system integration that are assigned to send MWI requests. To view the
                                    			 settings, in Cisco Unity Connection Administration, select Telephony Integrations > Ports .

PIMG/TIMG serial integrations do not send MWI requests through
                                                				voice messaging ports.

Confirm that the voice messaging ports that are assigned to send
                                    			 MWI requests are enabled. To view the settings, in Cisco Unity Connection
                                    			 Administration, select Telephony Integrations > Ports .

Confirm that an adequate number of voice messaging ports for the
                                    			 phone system integration are assigned to send MWI requests. Otherwise, the
                                    			 ports may be too busy to dial out immediately to turn MWIs on and off. To view
                                    			 the ports, in Cisco Unity Connection Administration, select Telephony Integrations > Ports .

Confirm that the port groups for the phone system integration
                                    			 enable MWIs. To view the Enable Message Waiting Indicators check box, in
                                    			 Cisco Unity Connection Administration, select Telephony Integrations > Port
                                          				  Group > Port Group
                                          				  Basics .

(Cisco Unified CM SCCP integrations only) Confirm that the
                                    			 settings are correct for the MWI On Extension field and the MWI Off Extension
                                    			 field. To view the Cisco Unified CM settings, in Cisco Unified Communications
                                    			 Manager Administration, select Voice
                                          				  Mail > Message
                                          				  Waiting . To view the Unity Connection settings, in
                                    			 Cisco Unity Connection Administration, select Telephony Integrations > Port
                                          				  Group > Port Group
                                          				  Basics .

(PIMG/TIMG serial integrations only) Confirm that a separate
                                    			 port group exists to send MWI requests to the master PIMG/TIMG unit. To view
                                    			 the port groups, in Connection Administration, select Telephony Integrations > Port
                                          				  Group . For details on the MWI port group, see the
                                    			 applicable Integration Guide for Cisco Unity Connection at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html .

Confirm that MWIs for the phone system are not forced off. To
                                    			 view the Force All MWIs Off for This Phone System check box, in Cisco Unity
                                    			 Connection Administration, select Telephony Integrations > Phone System > Phone System
                                          				  Basics .

Confirm that the MWI is enabled for the user. To view the
                                    			 Enabled check box, in Cisco Unity Connection Administration, select Users > Users > Messaging Waiting
                                          				  Indicators .

Confirm that the correct phone system is assigned to the MWI for
                                    			 the user. To view the Phone System field, in Cisco Unity Connection
                                    			 Administration, select Users > Users > Messaging Waiting
                                          				  Indicators .

(Cisco Unified CM SCCP integrations only) Confirm that the
                                    			 extensions that turn MWIs on and off are in the same calling search space that
                                    			 contains the phones and voicemail ports. From a phone, dial the extension that
                                    			 turns on the MWI. If you hear the reorder tone, the extension for turning on
                                    			 MWIs is not assigned to the correct calling search space in Cisco Unified CM
                                    			 Administration. If you do not hear the reorder tone, but the MWI is not turned
                                    			 on or off, a route plan may be causing the problem.

To view the calling search space for the MWI extensions, in
                                    			 Cisco Unified CM Administration, select Voice Mail > Message Waiting .

(Cisco Unified CM SCCP integrations only) Confirm that the
                                    			 dial plan does not overlap with the MWI extensions. MWI extensions must be
                                    			 unique. To view the dial plan, in Cisco Unified CM Administration, select Call
                                          				  Routing > Dial Plan
                                          				  Installer .

(PIMG/TIMG serial integrations only) Confirm that the RS-232
                                    			 serial cable is firmly seated in the serial port of the master PIMG/TIMG unit
                                    			 and in the serial port of the phone system.

Verify whether the Unity Connection server was upgraded,
                                    			 restored using the Disaster Recovery System, or experienced an event that
                                    			 disrupted MWI synchronization. See the “Synchronizing
                                       				MWIs” section on page 15-3 .

If the preceding tasks did not resolve the MWI problem, enable
                                    			 macro traces for MWIs. For detailed instructions on enabling the applicable
                                    			 traces and viewing the trace logs, see the Troubleshooting Cisco Unity Connection chapter.

#### Running the Check
                              	 Telephony Configuration Test

The Check Telephony Configuration test does not test IPv6
                                                			 connectivity. (IPv6 is supported in Unity Connection for Cisco Unified
                                                			 Communications Manager integrations.) The test confirms that Unity Connection
                                                			 can communicate with the phone system using IPv4 addressing.

In Cisco Unity Connection Administration, in the Related Links
                                             			 list in the upper right corner of any Telephony Integrations page, select Check Telephony Configuration and select Go .

If the test is not successful, the Task Execution Results
                                                				displays one or more messages with troubleshooting steps. After correcting the
                                                				problems, run the test again.

In the Task Execution Results window, select Close .

#### Synchronizing MWIs

We recommend resynchronizing MWIs for the system in the following circumstances:

After a server is restored using the Disaster Recovery System.

After upgrading a system.

After a WAN outage in a system that has distributed voice messaging through Cisco Unified Survivable Remote Site Telephony
                                       (SRST) routers or Cisco Unified Communications Manager Express routers in SRST mode.

##### Synchronizing MWIs
                                 	 for a Phone System Integration

In Cisco Unity Connection Administration, expand Telephony Integrations and select Phone System . On the Search Phone Systems page,
                                                			 select the name of the phone system for which you want to synchronize all MWIs.

On the Phone System Basics page, under Message Waiting
                                                			 Indicators, select Run .

Synchronizing MWIs for the phone system may affect system
                                                               				  performance. We recommend that you do this task when phone traffic is light.

### MWIs Turn On but Do Not Turn Off

Use the troubleshooting information in this section if MWIs turn on but do not turn off. See the following possible causes:

For PIMG/TIMG integrations, certain phone systems require that Unity Connection use port memory to turn off MWIs so that the
                                    same port is used for turning off an MWI that was used for turning on the MWI. See the “Confirm that Unity Connection Uses Port Memory (PIMG/TIMG Integrations)” section on page 15-4 .

For PIMG/TIMG integrations, if the phone system requires port memory, one or more of the ports used to set MWIs were deleted
                                    or were reconfigured not to set MWIs. You must have the phone system turn off all MWIs, then have Unity Connection resynchronize
                                    all MWIs.

To avoid this problem when deleting or reconfiguring MWI ports not to set MWIs, see the “Deleting or Reconfiguring MWI Ports When Port Memory is Used (PIMG/TIMG Integrations)” section on page 15-5 .

#### Confirm that Unity
                              	 Connection Uses Port Memory (PIMG/TIMG Integrations)

When MWIs turn on
                                    		  but do not turn off, the cause may be port memory. For Avaya, Rolm, and Siemens
                                    		  Hicom phone system integrations, Cisco Unity Connection must use the same port
                                    		  for turning off an MWI that was used for turning on the MWI. When Unity
                                    		  Connection is integrated with one of these phone systems and uses a different
                                    		  port for turning off an MWI, the MWI request for turning off the MWI fails.

This problem does not apply to PIMG/TIMG serial integrations.

In Cisco Unity Connection Administration, expand Telephony Integrations > and select Phone System .

On the Search Phone Systems page, select the name of the phone
                                             			 system.

On the Phone System Basics page, under Message Waiting
                                             			 Indicators, confirm that the Use Same Port for Enabling and Disabling MWIs check
                                             			 box is checked and select Save .

#### Deleting or
                              	 Reconfiguring MWI Ports When Port Memory is Used (PIMG/TIMG
                              	 Integrations)

If Unity Connection must use the same port
                                    		  for turning off an MWI that was used for turning on the MWI, and you want to
                                    		  delete an MWI port or reconfigure an MWI port not to set MWIs, do the
                                    		  applicable procedure.

In Cisco Unity Connection Administration, expand Telephony Integrations and select Phone System . On the Search Phone Systems page,
                                             			 select the name of the phone system.

On the Phone System Basics page, under Message Waiting
                                             			 Indicators, check the Force All MWIs Off for This Phone System check box
                                             			 and select Save . All MWIs for the phone system are turned off.

In the left pane, select Port .

On the Search Ports page, check the check boxes of the MWI ports
                                             			 that you want to delete and select Delete Selected .

In the left pane, select Phone System . On the Search Phone Systems page,
                                             			 select the name of the phone system.

On the Phone System Basics page, under Message Waiting
                                             			 Indicators, uncheck the Force All MWIs Off for This Phone System check box
                                             			 and select Save .

To the right of Synchronize All MWIs on This Phone System,
                                             			 select Run . All MWIs for the phone system are synchronized.

##### Reconfiguring MWI
                                 	 Ports When Port Memory is Used (PIMG/TIMG Integrations)

In Cisco Unity Connection Administration, expand Telephony Integrations > and select Phone System . On the Search Phone Systems page,
                                                			 select the name of the phone system.

On the Phone System Basics page, under Message Waiting
                                                			 Indicators, check the Force All MWIs Off for This Phone System check box
                                                			 and select Save . All MWIs for the phone system are turned off.

In the left pane, select Port . On the Search Ports page, select the display
                                                			 name of the first MWI port that you want to reconfigure not to set MWIs.

On the Port Basics page, under Port Behavior, enter the
                                                			 applicable settings and select Save .

If there are more MWI ports that you want to reconfigure not to
                                                			 set MWIs, select Next . Otherwise, skip to Step 7 .

Repeat Step 4 and Step 5 for all
                                                			 remaining MWI ports that you want to configure not to set MWIs.

In the left pane, select Phone System .

On the Search Phone Systems page, select the name of the phone
                                                			 system.

On the Phone System Basics page, under Message Waiting
                                                			 Indicators, uncheck the Force All MWIs Off for This Phone System check box
                                                			 and select Save .

To the right of Synchronize All MWIs on This Phone System,
                                                			 select Run . All MWIs for the phone system are synchronized.

### Delay for MWIs to Turn On or Off

Use the troubleshooting information in this section if there is a delay for MWIs to turn on or off. See the following possible
                              causes:

If MWIs are being synchronized for a phone system integration, this may result in delayed MWIs for messages. This is due to
                                    the additional MWI requests that are being processed.

The number of ports assigned to handle MWI requests is insufficient. To evaluate the current MWI port activity, see the “Determining the MWI Port Activity” section on page 15-6 .

For systems that handle a large volume of calls, you may need to install additional ports.

(Cisco Unified CM SCCP integrations only) If there are two or more port groups in the phone system integration, the port groups may not all be configured correctly
                                    for MWIs. See the “Configuring the MWI On and Off Extensions for Port Groups (SCCP Integrations Only)” section on page 15-6 .

#### Determining the
                              	 MWI Port Activity

In Cisco Unity Connection Serviceability, on the Tools menu,
                                             			 select Reports .

On the Serviceability Reports page, select Port Activity Report .

On the Port Activity Report page, select the applicable options
                                             			 for the report.

Select Generate Report .

#### Configuring the MWI On and Off Extensions for Port Groups (SCCP Integrations Only)

For Cisco Unified CM SCCP integrations, the phone system integration may have two or more port groups, one of which might
                                 be missing the MWI on and off extension settings.

In Cisco Unity Connection Administration, expand Telephony Integrations , then select Port Group . On the Search Port Groups page, select the name of the first port group for the SCCP integration.

On the Port Group Basics page, under Message Waiting Indicator Settings, in the MWI On Extension field, confirm that the extension
                                       for turning on MWIs is entered. If the field is blank, enter the MWI On extension.

In the MWI Off Extension field, confirm that the extension for turning off MWIs is entered. If the field is blank, enter the
                                       MWI Off extension and select Save .

Select Next .

Repeat Step 2 through Step 3 for the remaining port groups in the SCCP integration.

### No Message Count Sent on Phone When MWI is On

For Cisco Unified CM integrations, Unity Connection typically provides a message count when the user signs in by phone. If
                              the message count is not given, message counts have not been enabled for new messages or for the type of new message that
                              is in the user voice mailbox. For example, if message counts are enabled only for voice messages, no message count is given
                              when a new email or fax message arrives, even if the MWI is on.

#### Enabling Message Counts for the Applicable New Messages

### SUMMARY STEPS

- In Cisco Unity Connection Administration, expand Users > and select Users . On the Search Users page, select the alias of the applicable user.

- On the Edit User Basics page, on the Edit menu, select Playback Message Settings .

- On the Playback Message Settings page, under For New Messages, Play, check the applicable check boxes:

- Select Save .

### DETAILED STEPS

In Cisco Unity Connection Administration, expand Users > and select Users . On the Search Users page, select the alias of the applicable user.

On the Edit User Basics page, on the Edit menu, select Playback Message Settings .

On the Playback Message Settings page, under For New Messages, Play, check the applicable check boxes:

Message Count Totals —Unity Connection announces the total number of messages that are marked new, including voice, email, and fax messages.

Voice Message Counts —Unity Connection announces the total number of voice messages that are marked new.

Email Message Counts —Unity Connection announces the total number of email messages that are marked new.

Fax Message Counts —Unity Connection announces the total number of fax messages that are marked new.

Receipt Message Counts —Unity Connection announces the total number of receipts that are marked new.

Select Save .

### Incorrect Message Count and False MWI Notification Sent on Phone

If a user gets MWI on and there is no new voice messages in the mailbox of the user. The user may get this issue in the following
                              scenarios:

Scenario 1:

Users may have same MWI Extension and different primary extension in a Phone System

If two or more users have different primary extension and same MWI extension within a Phone System, any of the user will get
                              false MWI notification and incorrect message count on the phone. For example, a user A has primary extension and MWI extension
                              as 1001 and another user B has primary extension 1002 and MWI extension as 1001. If user B gets a new voice message, the MWI
                              notification turns on for extension 1001, which is the primary extension of the user A. Hence user A also gets MWI notification
                              but there is no new message in his mailbox.

To stop the false MWI notification on the phone, do the following:

Execute the below command to identify the users having same MWI extension.

```
run cuc dbquery unitydirdb select u.alias, n.mwiextension from tbl_notificationmwi n inner join vw_user u on n.subscriberobjectid=u.objectid where n.mwiextension='<Extension on which user get false MWI notification>'
```

```
run cuc dbquery unitydirdb select u.alias, n.mwiextension from tbl_notificationmwi n inner join vw_user u on n.subscriberobjectid=u.objectid where n.mwiextension= 1001
```

On the Search Users page of  Cisco Unity Connection Administrator, check the primary extension of the users that have same MWI extension.

The configuration is incorrect for the user, which have different primary and MWI extension. This causes the false MWI notification
                                    on the phone.

To change the MWI extension of the user, go to Edit User Basics page of that user and navigate Edit > Message Waiting Indicators . In Extension field of Edit Message Waiting Indicators page, update the correct extension for MWI notification.

Scenario 2

User may exist in different partition having same primary extension

If two or more users have same primary extension in different partition, one of the user will get the false MWI notification
                              on the phone. For example, a user A has primary as well as MWI extension as 1001 in partition A and other user B also has
                              same extension 1001 as primary and MWI extension in partition B. If user B gets a new voice message, the MWI notification
                              turns on for extension 1001, which is also the MWI extension of user A. Hence user A gets false MWI notification on the phone.

To stop the false MWI notification in different partition, do the following:

Execute the below command to get the list of extension numbers and number of users corresponding to each extension (dtmfaccessid)

```
run cuc dbquery unitydirdb select first 10 dtmfaccessid,count(dtmfaccessid) from vw_user group by dtmfaccessid order by count(dtmfaccessid) desc
```

Execute the below command to get the alias of the users having same extension (dtmfaccessid)

```
run cuc dbquery unitydirdb select first 10 dtmfaccessid,count(dtmfaccessid),alias from vw_user group by dtmfaccessid,alias order by count(dtmfaccessid)
```

Check the Phone System associated with the users having same extension on Edit User Basics page of the users.

If the users have same Phone System then select the different Phone System for each user through Edit User Basics page of Cisco Unity Connection Administrator.

| Note | PIMG/TIMG serial integrations do not send MWI requests through
                                                				voice messaging ports. |
|---|---|

| Note | The Check Telephony Configuration test does not test IPv6
                                                			 connectivity. (IPv6 is supported in Unity Connection for Cisco Unified
                                                			 Communications Manager integrations.) The test confirms that Unity Connection
                                                			 can communicate with the phone system using IPv4 addressing. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, in the Related Links
                                             			 list in the upper right corner of any Telephony Integrations page, select Check Telephony Configuration and select Go . If the test is not successful, the Task Execution Results
                                                				displays one or more messages with troubleshooting steps. After correcting the
                                                				problems, run the test again. |
|---|---|
| Step 2 | In the Task Execution Results window, select Close . |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations and select Phone System . On the Search Phone Systems page,
                                                			 select the name of the phone system for which you want to synchronize all MWIs. |
|---|---|
| Step 2 | On the Phone System Basics page, under Message Waiting
                                                			 Indicators, select Run . Note Synchronizing MWIs for the phone system may affect system
                                                               				  performance. We recommend that you do this task when phone traffic is light. | Note | Synchronizing MWIs for the phone system may affect system
                                                               				  performance. We recommend that you do this task when phone traffic is light. |
| Note | Synchronizing MWIs for the phone system may affect system
                                                               				  performance. We recommend that you do this task when phone traffic is light. |

| Note | Synchronizing MWIs for the phone system may affect system
                                                               				  performance. We recommend that you do this task when phone traffic is light. |
|---|---|

| Note | This problem does not apply to PIMG/TIMG serial integrations. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations > and select Phone System . |
|---|---|
| Step 2 | On the Search Phone Systems page, select the name of the phone
                                             			 system. |
| Step 3 | On the Phone System Basics page, under Message Waiting
                                             			 Indicators, confirm that the Use Same Port for Enabling and Disabling MWIs check
                                             			 box is checked and select Save . |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations and select Phone System . On the Search Phone Systems page,
                                             			 select the name of the phone system. |
|---|---|
| Step 2 | On the Phone System Basics page, under Message Waiting
                                             			 Indicators, check the Force All MWIs Off for This Phone System check box
                                             			 and select Save . All MWIs for the phone system are turned off. |
| Step 3 | In the left pane, select Port . |
| Step 4 | On the Search Ports page, check the check boxes of the MWI ports
                                             			 that you want to delete and select Delete Selected . |
| Step 5 | In the left pane, select Phone System . On the Search Phone Systems page,
                                             			 select the name of the phone system. |
| Step 6 | On the Phone System Basics page, under Message Waiting
                                             			 Indicators, uncheck the Force All MWIs Off for This Phone System check box
                                             			 and select Save . |
| Step 7 | To the right of Synchronize All MWIs on This Phone System,
                                             			 select Run . All MWIs for the phone system are synchronized. |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations > and select Phone System . On the Search Phone Systems page,
                                                			 select the name of the phone system. |
|---|---|
| Step 2 | On the Phone System Basics page, under Message Waiting
                                                			 Indicators, check the Force All MWIs Off for This Phone System check box
                                                			 and select Save . All MWIs for the phone system are turned off. |
| Step 3 | In the left pane, select Port . On the Search Ports page, select the display
                                                			 name of the first MWI port that you want to reconfigure not to set MWIs. |
| Step 4 | On the Port Basics page, under Port Behavior, enter the
                                                			 applicable settings and select Save . |
| Step 5 | If there are more MWI ports that you want to reconfigure not to
                                                			 set MWIs, select Next . Otherwise, skip to Step 7 . |
| Step 6 | Repeat Step 4 and Step 5 for all
                                                			 remaining MWI ports that you want to configure not to set MWIs. |
| Step 7 | In the left pane, select Phone System . |
| Step 8 | On the Search Phone Systems page, select the name of the phone
                                                			 system. |
| Step 9 | On the Phone System Basics page, under Message Waiting
                                                			 Indicators, uncheck the Force All MWIs Off for This Phone System check box
                                                			 and select Save . |
| Step 10 | To the right of Synchronize All MWIs on This Phone System,
                                                			 select Run . All MWIs for the phone system are synchronized. |

| Step 1 | In Cisco Unity Connection Serviceability, on the Tools menu,
                                             			 select Reports . |
|---|---|
| Step 2 | On the Serviceability Reports page, select Port Activity Report . |
| Step 3 | On the Port Activity Report page, select the applicable options
                                             			 for the report. |
| Step 4 | Select Generate Report . |

| Step 1 | In Cisco Unity Connection Administration, expand Users > and select Users . On the Search Users page, select the alias of the applicable user. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit menu, select Playback Message Settings . |
| Step 3 | On the Playback Message Settings page, under For New Messages, Play, check the applicable check boxes: Message Count Totals —Unity Connection announces the total number of messages that are marked new, including voice, email, and fax messages. Voice Message Counts —Unity Connection announces the total number of voice messages that are marked new. Email Message Counts —Unity Connection announces the total number of email messages that are marked new. Fax Message Counts —Unity Connection announces the total number of fax messages that are marked new. Receipt Message Counts —Unity Connection announces the total number of receipts that are marked new. |
| Step 4 | Select Save . |