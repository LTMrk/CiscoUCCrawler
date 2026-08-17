---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-chapter-01001-1-ht-0b0919528f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_chapter_01001-1.html
retrieved_at: 2026-08-17T02:38:53.463942+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting Transcription (SpeechView Cisco Webex in-house transcription service)

## Chapter: Troubleshooting Transcription (SpeechView Cisco Webex in-house transcription service)

# Troubleshooting Transcription (SpeechView Cisco Webex in-house transcription service)

## Task List for Troubleshooting SpeechView

To troubleshoot issues related to SpeechView, do the tasks mentioned in the sub-sections.

For more information on configuring SpeechView, see the SpeechView (Cisco Webex in-house transcription service) chapter of
                                       the System Administration Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

### Issues Related to Basic Configuration Settings

Check for warnings or errors in Cisco Unity Connection Administration:

On the System Settings > Licenses page. An error message on this page alerts you if you have a license violation. Confirm that your SpeechView usage is as
                                          you expect by looking at the number of SpeechView users listed under License Count. For more information about license issues,
                                          see the Troubleshooting Licensing chapter.

Ensure that Unity Connection cluster is onboarded on Cisco Webex Cloud - Connected UC. For more information, see the "Set
                                          up Webex Cloud-Connected UC for on-premises devices" in webex Help Center at https://help.webex.com/en-us/article/nzt6c0b/Set-up-Webex-Cloud-Connected-UC-for-on-premises-devices . To know about Network Requirements for Cisco Webex Cloud-Connected UC, refer https://help.webex.com/en-us/article/fg3qim/Network-Requirements-for-Webex-Cloud-Connected-UC .

Ensure that  " Speechview Voicemail Transcript " service is enabled on the Service Management Page of Cisco Webex Cloud-Connected UC. For more information, refer https://help.webex.com/en-us/article/oh49ck/Enable-or-Disable-Webex-Cloud-Connected-UC-Services-in-Control-Hub .

On the Unified Messaging > SpeechView Transcription> Service page. Confirm that SpeechView Status is Enabled on the Transcription Service for SpeechView page.

Confirm that the voicemail users for which SpeechView needs to be enabled have the class of service setting enabled. In Cisco Unity
                                    Connection Administration, expand Class of Service and select Class of Service. Select the applicable class of service. On
                                    the Edit Class of Service page, check the Allow Users to Access SpeechView Transcription Service check box and select Save .

Many of the warning and error messages on these pages also include information on how to resolve the problem.

### Troubleshooting the SpeechView in Networking

If accessing the transcription service via a proxy server, troubleshoot the proxy server:

In Cisco Unity Connection Serviceability, use the Voice Network Map tool to verify the health of the digital network. See
                                    the “ Using the Voice Network Map Tool ” chapter of the Administration Guide for Cisco Unity Connection Serviceability Release 15 , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag.html .

Verify that the server designated as a proxy system is configured to advertise transcription services.

Continue with Task List for Troubleshooting SpeechView on the proxy server.

### Issues with the Transcription Service Configuration

Select Sync License Status button and check for any warnings. If there are any resolve them.

Use the Test button to troubleshoot the transcription service configuration:

In Cisco Unity Connection Administration, expand Unified Messaging > SpeechView Transcription and select Services .

Select the Test button.

View the test task execution results for specific warnings and error messages.

Follow the Recommendations present on the task execution results page to resolve the warnings and error messages.

In Unity Connection Serviceability, verify that the Unity Connection SpeechView Processor is running. See the "Confirming that Connection SpeechView Processor is Running" section on page 11-3.

Generate the SpeechView Activity Summary Report to verify that the transcriptions are arriving at the Unity Connection server. For more information, see the “ Generating and Viewing Reports ” section in the “Using Reports” chapter of the Administration Guide for Cisco Unity Connection Serviceability Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag.html

### Issues Related to User Expectations

Confirm that the message in question is of a type that is transcribed. The following messages are never transcribed:

Private messages

Broadcast messages

Dispatch messages

Secure messages

Verify that the problem message was not already deleted by the user. When a transcription is received from the Cisco Webex
                                    in-house transcription service, the transcription text is attached to the original voice message. If users delete a voice
                                    message before the transcription is received from the transcription service, the transcription text is attached to the deleted
                                    message. It is not considered a new message and is not sent to a notification device.

If users belong to a class of service that is configured to move deleted messages to the Deleted Items folder, users can see
                                                the transcription in the Deleted Items folder of an IMAP client.

If the transcription service is unable to provide a transcription of a message, the user receives a message stating that the
                                    transcription cannot be provided and to call Unity Connection to listen to the message. See the "Messages that Cannot be Transcribed " section on page 11-5 for details.

### Issues with Transcription Notifications

Troubleshoot the notification device configuration. See the Troubleshooting Notification Devices .

### Enabling Traces and Contacting Cisco TAC

If you still have problems after following all the troubleshooting steps described in this chapter, enable traces and contact
                              the Cisco Technical Assistance Center (TAC). See the "Using Diagnostic Traces to Troubleshoot SpeechView" section on page 11-6 .

## Confirming that Connection SpeechView Processor is Running

The Connection SpeechView Processor service needs to be running only on the acting primary server of a Unity Connection cluster server pair.

Step 1

In Cisco Unity Connection Serviceability, on the Tools menu, select Service Management .

Step 2

On the Control Center – Feature Services page, under Optional Services, locate the Connection SpeechView Processor service.

Step 3

Confirm that the activate status for the Connection SpeechView Processor service is Activated . If the activate status is Deactivated, select Activate .

Step 4

Confirm that the service status for the Connection SpeechView Processor service is Started . If the service status is Stopped, select Start .

## Troubleshooting Transcription Notifications

The problem with transcription notifications may be solved by any of the steps in the procedure, which are arranged in order
                              of likelihood. After each step, retest transcription notifications, and if the problem has not been resolved, continue on
                              to the next step in the procedure.

Step 1

Confirm that messages are being transcribed by following the steps mentioned in "Task List for Configuring SpeechView" section on page 11-1 .

Step 2

Confirm that the Send Transcriptions of Voice Messages setting is enabled for the SMS or SMTP notification device on the Edit
                                       Notification Device page for the user account in Cisco Unity Connection Administration.

Step 3

If the message is a secure message, confirm that the user belongs to a class of service that allows transcriptions of secure
                                       messages to be sent to notification devices.

Step 4

Test to see whether the SMS or SMTP notification device receives non-transcription messages by doing the following sub-steps:

Verify that the device is configured to notify the user for All Voice Messages.

Send a voice message to the user.

If the device is not receiving any notifications, see the Troubleshooting Notification Devices chapter for further troubleshooting information.

Step 5

If these steps do not resolve the problem, enable traces and contact Cisco TAC. See the "Using Diagnostic Traces to Troubleshoot SpeechView" section on page 11-6 .

## Messages that Cannot be Transcribed

The Cisco Webex in-house transcription service may have problems transcribing messages if the recording is inaudible or if
                           the sender was speaking in a language that is not supported by the transcription service. In these cases, the service returns
                           a transcription that instructs the user to call Unity Connection to listen to the message.

## Transcription Not Synchronized on User Phones

If a user does not receive transcription on the mobile device not qualified with Unity Connection, make sure that the Hold
                           till transcription received option is enabled for the user. To enable the Hold till transcription received option, navigate
                           to Cisco Personal Communications Assistant > Message Assistant> Personal Options .

However, if the Hold till transcription received option is enabled for a Single Inbox (SIB) user with the SpeechView transcription
                           service, the synchronization of a new voice message between Unity Connection and Exchange mailboxes will be done only when
                           Unity Connection receives the transcription of the voice message from the Cisco Webex in-house transcription service.

## Transcription Issue after Upgrade

Do the following to resolve the transcription issue after Upgrade for Unity Connection 15:

Step 1

In Cisco Unity Connection Administration, expand Unified Messaging and select SpeechView Transcription Service. If the SpeechView
                                       Status is Disabled, verify if the following conditions are met.

Unity Connection is registered with Cisco Smart Software Manager (CSSM) or Cisco Smart Software Manager satellite. You have
                                                acquired the proper licenses from Cisco to use this feature.

Unity Connection cluster is onboarded on Cisco Webex Cloud-Connected UC and "Speechview Voicemail Transcript" service is enabled
                                                on the Service Management Page of Cisco Webex Cloud-Connected UC.

Step 2

Select Sync License Data field to sync the licenses from Cisco Smart Software Manager (CSSM) or Cisco Smart Software Manager
                                       satellite.

Step 3

If Unity Connection has been onboarded on Cisco Webex Cloud-Connected UC before upgrade to 15 SU2 or later, then after the
                                       upgrade Telemetry module may take up to 75 minutes to update its status online on Cisco Webex Cloud-Connected UC. To check
                                       the Telemetry module status, refer View the node status for Telemetry Module Inventory .

After upgrading to 15 SU2 or later and fulfilling all the prerequisites of SpeechView configuration, if you continue to see
                                                         the warning banner stating " Cisco Unity Connection server is not onboarded on Webex Cloud-Connected UC ", you will need to restart the "Connection SpeechView Processor" service on the Connection Serviceability page of the Pubisher
                                                         sever in the Unity Connection cluster.

## Troubleshooting Transcription Request Timed out

If a transcription request is sent successfully to the Cisco Webex in-house transcription service but the transcription response
                           is not received, then the transcription request from Unity Connection will be timed out in 15 minutes. " The transcription request timed out " will be displayed under Message Transcription in the Web Inbox.

To resolve this, check the Telemetry Module status on Cisco Webex Cloud-Connected UC. It should be online.

## Using Diagnostic Traces to Troubleshoot SpeechView

You can use Unity Connection traces to troubleshoot problems with the SpeechView transcription feature.

Enable the following micro traces to troubleshoot SpeechView problems:

MTA (level 10, 11, 12, 13)

SttClient (all levels)

SttService (all levels)

SysAgent (level 10, 11, 12, 16)

Notifier (level 16, 21, 25, 30) —if you are troubleshooting problems with delivery to notification devices.

For detailed instructions on enabling and collecting diagnostic traces, see the Using Diagnostic Traces for Troubleshooting section.

| Note | For more information on configuring SpeechView, see the SpeechView (Cisco Webex in-house transcription service) chapter of
                                       the System Administration Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . |
|---|---|

| Note | Secure messages are transcribed only if the user belongs to a class of service for which the Allow Transcriptions of Secure
                                                   Messages option is enabled. |
|---|---|

| Note | If users belong to a class of service that is configured to move deleted messages to the Deleted Items folder, users can see
                                                the transcription in the Deleted Items folder of an IMAP client. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability, on the Tools menu, select Service Management . |
|---|---|
| Step 2 | On the Control Center – Feature Services page, under Optional Services, locate the Connection SpeechView Processor service. |
| Step 3 | Confirm that the activate status for the Connection SpeechView Processor service is Activated . If the activate status is Deactivated, select Activate . |
| Step 4 | Confirm that the service status for the Connection SpeechView Processor service is Started . If the service status is Stopped, select Start . |

| Step 1 | Confirm that messages are being transcribed by following the steps mentioned in "Task List for Configuring SpeechView" section on page 11-1 . |
|---|---|
| Step 2 | Confirm that the Send Transcriptions of Voice Messages setting is enabled for the SMS or SMTP notification device on the Edit
                                       Notification Device page for the user account in Cisco Unity Connection Administration. |
| Step 3 | If the message is a secure message, confirm that the user belongs to a class of service that allows transcriptions of secure
                                       messages to be sent to notification devices. |
| Step 4 | Test to see whether the SMS or SMTP notification device receives non-transcription messages by doing the following sub-steps: Verify that the device is configured to notify the user for All Voice Messages. Send a voice message to the user. If the device is not receiving any notifications, see the Troubleshooting Notification Devices chapter for further troubleshooting information. |
| Step 5 | If these steps do not resolve the problem, enable traces and contact Cisco TAC. See the "Using Diagnostic Traces to Troubleshoot SpeechView" section on page 11-6 . |

| Step 1 | In Cisco Unity Connection Administration, expand Unified Messaging and select SpeechView Transcription Service. If the SpeechView
                                       Status is Disabled, verify if the following conditions are met. Unity Connection is registered with Cisco Smart Software Manager (CSSM) or Cisco Smart Software Manager satellite. You have
                                                acquired the proper licenses from Cisco to use this feature. Unity Connection cluster is onboarded on Cisco Webex Cloud-Connected UC and "Speechview Voicemail Transcript" service is enabled
                                                on the Service Management Page of Cisco Webex Cloud-Connected UC. |
|---|---|
| Step 2 | Select Sync License Data field to sync the licenses from Cisco Smart Software Manager (CSSM) or Cisco Smart Software Manager
                                       satellite. |
| Step 3 | If Unity Connection has been onboarded on Cisco Webex Cloud-Connected UC before upgrade to 15 SU2 or later, then after the
                                       upgrade Telemetry module may take up to 75 minutes to update its status online on Cisco Webex Cloud-Connected UC. To check
                                       the Telemetry module status, refer View the node status for Telemetry Module Inventory . Note After upgrading to 15 SU2 or later and fulfilling all the prerequisites of SpeechView configuration, if you continue to see
                                                         the warning banner stating " Cisco Unity Connection server is not onboarded on Webex Cloud-Connected UC ", you will need to restart the "Connection SpeechView Processor" service on the Connection Serviceability page of the Pubisher
                                                         sever in the Unity Connection cluster. | Note | After upgrading to 15 SU2 or later and fulfilling all the prerequisites of SpeechView configuration, if you continue to see
                                                         the warning banner stating " Cisco Unity Connection server is not onboarded on Webex Cloud-Connected UC ", you will need to restart the "Connection SpeechView Processor" service on the Connection Serviceability page of the Pubisher
                                                         sever in the Unity Connection cluster. |
| Note | After upgrading to 15 SU2 or later and fulfilling all the prerequisites of SpeechView configuration, if you continue to see
                                                         the warning banner stating " Cisco Unity Connection server is not onboarded on Webex Cloud-Connected UC ", you will need to restart the "Connection SpeechView Processor" service on the Connection Serviceability page of the Pubisher
                                                         sever in the Unity Connection cluster. |

| Note | After upgrading to 15 SU2 or later and fulfilling all the prerequisites of SpeechView configuration, if you continue to see
                                                         the warning banner stating " Cisco Unity Connection server is not onboarded on Webex Cloud-Connected UC ", you will need to restart the "Connection SpeechView Processor" service on the Connection Serviceability page of the Pubisher
                                                         sever in the Unity Connection cluster. |
|---|---|