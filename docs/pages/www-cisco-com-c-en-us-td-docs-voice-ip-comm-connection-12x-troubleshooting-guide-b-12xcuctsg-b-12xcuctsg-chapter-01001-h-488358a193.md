---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-01001-h-488358a193
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_01001.html
retrieved_at: 2026-08-17T02:28:57.466823+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting Transcription (SpeechView)

## Chapter: Troubleshooting Transcription (SpeechView)

# Troubleshooting Transcription (SpeechView)

Troubleshooting Transcription (SpeechView)

## Task List for
                        	 Troubleshooting SpeechView

To troubleshoot issues related to SpeechView, do the tasks
                           		mentioned in the sub-sections.

For more information on configuring SpeechView, see the
                                       		  SpeechView chapter of the System Administration Guide for Cisco Unity
                                       		  Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

### Issues Related to
                           	 Basic Configuration Settings

Check for
                                    			 warnings or errors in Cisco Unity Connection Administration:

On the System Settings > Licenses page. An error message on
                                          				  this page alerts you if you have a license violation. Confirm that your
                                          				  SpeechView usage is as you expect by looking at the number of SpeechView users
                                          				  listed under License Count. For more information about license issues, see the Troubleshooting Licensing chapter.

On the Unified Messaging > SpeechView Transcription>
                                          				  Service page. Make sure that on the Transcription Service for SpeechView page,
                                          				  the Enabled check box is checked.

On the System Settings > Advanced System Settings >
                                          				  Unified Messaging Services page> Transcriptions: Time to Wait for a
                                          				  Transcription Response before Timing Out (In Seconds) field.

Many of the warning and error messages on these pages also
                              		include information on how to resolve the problem.

Confirm that the voicemail users for which SpeechView needs to
                                    			 be enabled have the class of service setting enabled. In Cisco Unity Connection
                                    			 Administration, expand Class of Service and select Class of Service. Select the
                                    			 applicable class of service. On the Edit Class of Service page, check the Allow
                                    			 Users to Access SpeechView Transcription Service check box and select Save.

### Issues with a
                           	 Proxy Server

If accessing the
                              		transcription service via a proxy server, troubleshoot the proxy server:

In Cisco Unity Connection Serviceability, use the Voice Network
                                    			 Map tool to verify the health of the digital network. See the “ Using the Voice Network Map
                                       				Tool ” chapter of the Administration Guide for Cisco Unity Connection
                                    			 Serviceability Release 12.x , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/serv_administration/b_12xcucservag.html .

Verify that the server designated as a proxy system is
                                    			 configured to advertise transcription services.

Continue with this task list on the proxy server.

### Issues with the
                           	 Transcription Service Configuration

If
                                    			 the transcription service registration is failing or times out, review the
                                    			 registration task execution results window for specific error messages.

If registration has succeeded, use the Test button to
                                    			 troubleshoot the transcription service configuration:

In Cisco Unity Connection Administration, expand Unified Messaging > SpeechView Transcription and select Services .

Select the Test button.

View the test task execution results for specific warnings and
                                    			 error messages.

If the test you ran above fails and the transcription service
                                    			 was previously working successfully but has suddenly stopped working, use the
                                    			 Register button to reestablish the registration with the external transcription
                                    			 service:

In Cisco Unity Connection Administration, expand Unified Messaging > SpeechView Transcription and select Services .

Select the Register button. Another window displaying the
                                    			 results open. The registration process normally takes several minutes.

View the registration task execution results for specific
                                    			 warnings and error messages.

In Unity Connection Serviceability, verify that the Unity
                                    			 Connection SpeechView Processor and the Unity Connection SMTP Server services
                                    			 are running. See the “Confirming
                                       				that Connection SpeechView Processor and Connection SMTP Server Services are
                                       				Running” section on page 10-3 .

Run the SMTP test to verify that messages can successfully be
                                    			 sent from Unity Connection to an external email account outside of your
                                    			 organization. This SMTP test helps you determine whether the registration
                                    			 problem is due to issues in the communication path to the third-party
                                    			 transcription service. See the “Running
                                       				SMTP Test to Verify Outgoing and Incoming SMTP Path” section on
                                       				page 10-4 .

Generate the SpeechView Activity Summary Report to verify that
                                    			 the transcriptions are arriving at the Unity Connection server. For more
                                    			 information, see the “ Generating and Viewing
                                       				Reports ” section in the “Using Reports” chapter of the Administration
                                    			 Guide for Cisco Unity Connection Serviceability Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/serv_administration/b_12xcucservag.html .

### Issues Related to User Expectations

Confirm that the message in question is of a type that is transcribed. The following messages are never transcribed:

Private messages

Broadcast messages

Dispatch messages

Secure messages are transcribed only if the user belongs to a class of service for which the Allow Transcriptions of Secure
                              Messages option is enabled.

Verify that the problem message was not already deleted by the user. When a transcription is received from the third-party
                                    transcription service, the transcription text is attached to the original voice message. If users delete a voice message before
                                    the transcription is received from the transcription service, the transcription text is attached to the deleted message. It
                                    is not considered a new message and is not sent to a notification device.

If users belong to a class of service that is configured to move deleted messages to the Deleted Items folder, users can see
                                                the transcription in the Deleted Items folder of an IMAP client.

If the transcription service is unable to provide a transcription of a message, the user receives a message stating that the
                                    transcription cannot be provided and to call Unity Connection to listen to the message. See the “Messages that Cannot be Transcribed” section on page 10-5 for details.

### Issues with
                           	 Transcription Notifications

Troubleshoot
                              		the notification device configuration. See the Troubleshooting Notification Devices .

### Enabling Traces and Contacting Cisco TAC

If you still have problems after following all the troubleshooting steps described in this chapter, enable traces and contact
                              the Cisco Technical Assistance Center (TAC). See the “Using Diagnostic Traces to Troubleshoot SpeechView” section on page 10-6 .

## Confirming that Connection SpeechView Processor and Connection SMTP
                        	 Server Services are Running

The Connection SpeechView Processor service needs to be running only on the acting primary server of a
                              		  Unity Connection cluster server pair.

The Connection SMTP Server service needs to be running on both servers in a Unity Connection
                              		  cluster server pair.

In Cisco Unity Connection Serviceability, on
                                       			 the Tools menu, select Service Management .

On the Control Center – Feature Services
                                       			 page, under Optional Services, locate the Connection SpeechView Processor service.

Confirm that the activate status for the Connection SpeechView Processor service is Activated . If the
                                       			 activate status is Deactivated, select Activate .

Confirm that the service status for the Connection SpeechView Processor service is Started . If the service
                                       			 status is Stopped, select Start .

Confirm that the activate status for the Connection SMTP Server service is Activated . If the
                                       			 activate status is Deactivated, select Activate .

Confirm that the service status for the Connection SMTP Server service is Started . If the service
                                       			 status is Stopped, select Start .

If using a Unity Connection cluster, repeat Step 5 and Step 6 on the secondary
                                       			 server.

## Running SMTP Test
                        	 to Verify Outgoing and Incoming SMTP Path

The SMTP
                              		  test is a CLI command that sends a test message to a specified email address.
                              		  You then access the email account and reply to the test message without
                              		  changing the subject line. The test passes when the response is received by the
                              		  Unity Connection server. The success or failure of parts of the test help to
                              		  narrow down whether the source of the problem is in the outgoing or incoming
                              		  SMTP configuration.

On the Unity Connection server, use the CLI (Command Line
                                       			 Interface) command run cuc smtptest <email address . Use an email
                                       			 address that is outside of your organization.

For example, enter “run cuc smtptest johndoe@isp.com”.

For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified
                                                         					 Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

Sign in to the email account that you used in Step 1 .

If the outgoing message is not received at the email address
                                       			 that you specified in Step 1 , do the
                                       			 following sub-steps to troubleshoot the problem:

Verify that the SMTP smart host setting is configured in
                                             				  Cisco Unity Connection Administration. For details, see the “ Task List for
                                                					 Configuring SpeechView ” section in the “SpeechView” chapter of the
                                             				  System Administration Guide for Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

Verify that Unity Connection can reach the smart host using the
                                             				  CLI command utils network ping <smarthost>.

Verify that the smart host is configured to route messages from
                                             				  the Unity Connection server to the outside world.

Review the logs on the smart host server.

Repeat Step 1 through Step 3 until the test
                                       			 message successfully arrives at the email address you specified in Step 1 .

Reply to the test message. Do not change the subject line.

If the incoming reply message is not received by the CLI test,
                                       			 do the following sub-steps to troubleshoot the problem:

Verify that the email address entered in the Incoming SMTP
                                             				  Address field on the Unified Messaging > SpeechView Transcription >
                                             				  Service page in Cisco Unity Connection Administration is being routed
                                             				  correctly. It must be routed by your email infrastructure to the “stt-service”
                                             				  account on the Unity Connection server domain.

For example, if the Incoming SMTP Address is
                                                					 “transcriptions@example.com,” the email system must be configured to route
                                                					 transcriptions@example.com to stt-service@connection.example.com.

View the Unity Connection SMTP Server component log files to see
                                             				  if the message reached Unity Connection. The SMTP logs are located in
                                             				  diag_SMTP_*.uc. If you see “untrusted client Unity Connection refused” messages
                                             				  in the log files, you need to configure Unity Connection to trust incoming
                                             				  traffic from your email system.

For details on configuring Unity Connection to trust incoming
                                                					 traffic from your email system, see the “ Task List for
                                                   						Configuring SpeechView ” section in the “SpeechView” chapter of the
                                                					 System Administration Guide for Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

View the log files for your email infrastructure for additional
                                             				  clues.

Repeat Step 5 through Step 6 until the test
                                       			 message reply is received.

If the test continues to fail, enable traces and contact
                                       			 Cisco TAC. See the “Using
                                          				Diagnostic Traces to Troubleshoot SpeechView” section on page 10-6 .

## Troubleshooting
                        	 Transcription Notifications

The problem with transcription notifications may be solved by
                              		  any of the steps in the procedure, which are arranged in order of likelihood.
                              		  After each step, retest transcription notifications, and if the problem has not
                              		  been resolved, continue on to the next step in the procedure.

Confirm that messages are being transcribed by following Step 1. through Step 3. in the “Task
                                          				List for Troubleshooting SpeechView” section on page 10-1 .

Confirm that the Send Transcriptions of Voice Messages setting
                                       			 is enabled for the SMS or SMTP notification device on the Edit Notification
                                       			 Device page for the user account in Cisco Unity Connection Administration.

If the message is a secure message, confirm that the user
                                       			 belongs to a class of service that allows transcriptions of secure messages to
                                       			 be sent to notification devices.

Test to see whether the SMS or SMTP notification device receives
                                       			 non-transcription messages by doing the following sub-steps:

Verify that the device is configured to notify the user for All
                                             				  Voice Messages.

Send a voice message to the user.

If the device is not receiving any notifications, see the Troubleshooting Notification Devices chapter for further troubleshooting information.

If these steps do not resolve the problem, enable traces and
                                       			 contact Cisco TAC. See the “Using
                                          				Diagnostic Traces to Troubleshoot SpeechView” section on page 10-6 .

## Messages that Cannot be Transcribed

The third-party transcription service may have problems transcribing messages if the recording is inaudible or if the sender
                           was speaking in a language that is not supported by the transcription service. In these cases, the service returns a transcription
                           that instructs the user to call Unity Connection to listen to the message.

## Transcription Not Synchronized on User Phones

If a user does not receive transcription on the mobile device not qualified with Unity Connection, make sure that the Hold
                           till transcription received option is enabled for the user. To enable the Hold till transcription received option, navigate
                           to Cisco Personal Communications Assistant > Message Assistant> Personal Options.

However, if the Hold till transcription received option is enabled for a Single Inbox (SIB) user with the SpeechView transcription
                           service, the synchronization of a new voice message between Unity Connection and Exchange mailboxes will be done only when
                           Unity Connection receives the transcription of the voice message from the third-party external service.

## Transcription
                        	 Issue after Upgrade

If SpeechView services are enabled on Unity Connection 11.x or later
                              		  and you are upgrading Cisco Unity Connection to 12.x, you may face the
                              		  SpeechView transcription issues. After upgrade, you must register Unity
                              		  Connection with nuance server.

Do the following to resolve the transcription issue for Unity
                              		  Connection 12.x:

In Cisco Unity Connection
                                       			 Administration, expand Unified Messaging and select SpeechView Transcription
                                       			 Service.

In the SpeechView
                                          				Transcription Service page, uncheck the Enabled check box to disable the
                                          				SpeechView services.

In the SpeechView
                                       			 Transcription Service page, check the Enabled check box.

Select Get License Data
                                       			 field to acquire the licenses from Cisco Smart Software Manager (CSSM) or Cisco
                                       			 Smart Software Manager satellite.

Select Register button to register with the external
                                       			 transcription service.

## Using Diagnostic
                        	 Traces to Troubleshoot SpeechView

You can use
                           		Unity Connection traces to troubleshoot problems with the SpeechView
                           		transcription feature.

Enable the following micro traces to troubleshoot SpeechView
                           		problems:

MTA (level 10, 11, 12, 13)

SMTP (all levels)

SttClient (all levels)

SttService (all levels)

SysAgent (level 10, 11, 12, 16)

Notifier (level 16, 21, 25, 30) —if you are troubleshooting
                                 			 problems with delivery to notification devices.

For detailed instructions on enabling and collecting diagnostic
                           		traces, see the Using Diagnostic Traces for Troubleshooting section.

| Note | For more information on configuring SpeechView, see the
                                       		  SpeechView chapter of the System Administration Guide for Cisco Unity
                                       		  Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html . |
|---|---|

| Note | If users belong to a class of service that is configured to move deleted messages to the Deleted Items folder, users can see
                                                the transcription in the Deleted Items folder of an IMAP client. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability, on
                                       			 the Tools menu, select Service Management . |
|---|---|
| Step 2 | On the Control Center – Feature Services
                                       			 page, under Optional Services, locate the Connection SpeechView Processor service. |
| Step 3 | Confirm that the activate status for the Connection SpeechView Processor service is Activated . If the
                                       			 activate status is Deactivated, select Activate . |
| Step 4 | Confirm that the service status for the Connection SpeechView Processor service is Started . If the service
                                       			 status is Stopped, select Start . |
| Step 5 | Confirm that the activate status for the Connection SMTP Server service is Activated . If the
                                       			 activate status is Deactivated, select Activate . |
| Step 6 | Confirm that the service status for the Connection SMTP Server service is Started . If the service
                                       			 status is Stopped, select Start . |
| Step 7 | If using a Unity Connection cluster, repeat Step 5 and Step 6 on the secondary
                                       			 server. |

| Step 1 | On the Unity Connection server, use the CLI (Command Line
                                       			 Interface) command run cuc smtptest <email address . Use an email
                                       			 address that is outside of your organization. For example, enter “run cuc smtptest johndoe@isp.com”. Note For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified
                                                         					 Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . | Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified
                                                         					 Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
|---|---|---|---|
| Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified
                                                         					 Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
| Step 2 | Sign in to the email account that you used in Step 1 . |
| Step 3 | If the outgoing message is not received at the email address
                                       			 that you specified in Step 1 , do the
                                       			 following sub-steps to troubleshoot the problem: Verify that the SMTP smart host setting is configured in
                                             				  Cisco Unity Connection Administration. For details, see the “ Task List for
                                                					 Configuring SpeechView ” section in the “SpeechView” chapter of the
                                             				  System Administration Guide for Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html . Verify that Unity Connection can reach the smart host using the
                                             				  CLI command utils network ping <smarthost>. Verify that the smart host is configured to route messages from
                                             				  the Unity Connection server to the outside world. Review the logs on the smart host server. |
| Step 4 | Repeat Step 1 through Step 3 until the test
                                       			 message successfully arrives at the email address you specified in Step 1 . |
| Step 5 | Reply to the test message. Do not change the subject line. |
| Step 6 | If the incoming reply message is not received by the CLI test,
                                       			 do the following sub-steps to troubleshoot the problem: Verify that the email address entered in the Incoming SMTP
                                             				  Address field on the Unified Messaging > SpeechView Transcription >
                                             				  Service page in Cisco Unity Connection Administration is being routed
                                             				  correctly. It must be routed by your email infrastructure to the “stt-service”
                                             				  account on the Unity Connection server domain. For example, if the Incoming SMTP Address is
                                                					 “transcriptions@example.com,” the email system must be configured to route
                                                					 transcriptions@example.com to stt-service@connection.example.com. View the Unity Connection SMTP Server component log files to see
                                             				  if the message reached Unity Connection. The SMTP logs are located in
                                             				  diag_SMTP_*.uc. If you see “untrusted client Unity Connection refused” messages
                                             				  in the log files, you need to configure Unity Connection to trust incoming
                                             				  traffic from your email system. For details on configuring Unity Connection to trust incoming
                                                					 traffic from your email system, see the “ Task List for
                                                   						Configuring SpeechView ” section in the “SpeechView” chapter of the
                                                					 System Administration Guide for Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html . View the log files for your email infrastructure for additional
                                             				  clues. |
| Step 7 | Repeat Step 5 through Step 6 until the test
                                       			 message reply is received. |
| Step 8 | If the test continues to fail, enable traces and contact
                                       			 Cisco TAC. See the “Using
                                          				Diagnostic Traces to Troubleshoot SpeechView” section on page 10-6 . |

| Note | For details on using CLI commands, see the applicable Command Line Interface Reference Guide for Cisco Unified
                                                         					 Communications Solutions at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html . |
|---|---|

| Step 1 | Confirm that messages are being transcribed by following Step 1. through Step 3. in the “Task
                                          				List for Troubleshooting SpeechView” section on page 10-1 . |
|---|---|
| Step 2 | Confirm that the Send Transcriptions of Voice Messages setting
                                       			 is enabled for the SMS or SMTP notification device on the Edit Notification
                                       			 Device page for the user account in Cisco Unity Connection Administration. |
| Step 3 | If the message is a secure message, confirm that the user
                                       			 belongs to a class of service that allows transcriptions of secure messages to
                                       			 be sent to notification devices. |
| Step 4 | Test to see whether the SMS or SMTP notification device receives
                                       			 non-transcription messages by doing the following sub-steps: Verify that the device is configured to notify the user for All
                                             				  Voice Messages. Send a voice message to the user. If the device is not receiving any notifications, see the Troubleshooting Notification Devices chapter for further troubleshooting information. |
| Step 5 | If these steps do not resolve the problem, enable traces and
                                       			 contact Cisco TAC. See the “Using
                                          				Diagnostic Traces to Troubleshoot SpeechView” section on page 10-6 . |

| Step 1 | In Cisco Unity Connection
                                       			 Administration, expand Unified Messaging and select SpeechView Transcription
                                       			 Service. In the SpeechView
                                          				Transcription Service page, uncheck the Enabled check box to disable the
                                          				SpeechView services. |
|---|---|
| Step 2 | In the SpeechView
                                       			 Transcription Service page, check the Enabled check box. |
| Step 3 | Select Get License Data
                                       			 field to acquire the licenses from Cisco Smart Software Manager (CSSM) or Cisco
                                       			 Smart Software Manager satellite. |
| Step 4 | Select Register button to register with the external
                                       			 transcription service. |