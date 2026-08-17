---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-administration-guide-b-15cucsag-b-15cucsag-chapter-01101-html-59577e04e6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag/b_15cucsag_chapter_01101.html
retrieved_at: 2026-08-17T02:19:47.276457+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 12, 2025

Chapter: SpeechView Cisco Webex in-house transcription service

## Chapter: SpeechView Cisco Webex in-house transcription service

# SpeechView Cisco Webex in-house transcription service

## Overview

The SpeechView feature enables the transcription of voice messages so that users can receive the voicemails in the form of
                           text. Users can access the transcripted voicemails using email clients. SpeechView is a feature of Cisco Unity Connection
                           unified messaging solution. Therefore, the audio part of each voice message is also available to the users.

When a voice message is sent from Web Inbox to ViewMail for Outlook, the voice message is delivered to the mailbox of the
                                       recipient along with the transcribed text both in the transcript view box and in the mail body.

Without this feature, the voice message delivered to the user mailbox has a blank text attachment. This feature requires the
                           use of a Cisco Webex in-house transcription service to convert the voice message to text. Therefore, the blank text attachment
                           is updated with the transcripted text or an error message if there was a problem with transcription.

The SpeechView feature supports Standard Transcription Service. It automatically converts the voice message to text and the
                           transcripted text received is sent to the user over email.

Unity Connection supports only (Universal Transformation Format) UTF-8 character set encoding for transcription.

The following messages are never transcribed:

Private messages

Broadcast messages

Dispatch messages

Secure messages 1

Messages with no recipients

Unity Connection can be configured to deliver transcriptions to an SMS device as a text message or to an SMTP address as an
                           email message. The fields to turn on transcription delivery are located on the SMTP and SMS Notification Device pages where
                           you set up message notification. For more information on notification devices, see the Configuring Notification Devices section.

Following are the considerations for effective use of transcription delivery:

In the From field, enter the number users dial to reach Unity Connection when they are not dialing from their desk phone.
                                 If users have a text-compatible mobile phone, they may be able to initiate a callback to Unity Connection in the event that
                                 they want to listen to the message.

Check the Include Message Information in Message Text check box to include call information such as caller name and caller
                                 ID (if available) and the time that the message was received. Otherwise, there is no indication in the message of when it
                                 was received.

In addition, if they have a text-compatible mobile phone, they may be able to initiate a callback when the caller ID is included
                           with the transcription.

In the Notify Me Of section, if you turn on notification for voice or dispatch messages, users are notified when a message
                                 arrives. The transcription soon follows. If you do not want notification before the transcription arrives, do not select the
                                 voice or dispatch message options.

Email messages that contain transcriptions have a subject line that is identical to notification messages. So if you have
                                 notification for voice or dispatch messages turned on, users have to open the messages to determine which one contains the
                                 transcription.

Unity Connection does not have a locale for language English Canada. Hence, for transcription to work well, use the configuration
                           below to send en-CA as the language to the Cisco Webex in-house transcription service server. For this, execute the below
                           CLI command on the Unity Connection server.

```
run cuc dbquery unitydirdb update tbl_configuration set valuebool ='1' where fullname='System.Conversations.ConfigParamForAlternateTranscriptionLanguage'
```

## SpeechView Security Considerations

Unity Connection sends the Transcription request over HTTPS protocol to Cisco Webex in-house transcription service. Unity
                           Connection generates RSA-2048 public & private key pair which are used for encryption and decryption of the data. The generated
                           public key is sent securely over HTTPS protocol to Cisco Webex in-house transcription service as JWK object while sending
                           the transcription request from Unity Connection.

Cisco Webex in-house transcription service sends the encrypted transcription response to Unity Connection via Cisco Webex
                           Cloud-Connected UC. Unity Connection decrypts the transcription response using private key stored internally at Unity Connection
                           .

The pair of private and public keys ensures that each time voice messages are sent to the transcription service, the user
                           information is not passed along with the message. Therefore, the transcription service is unaware of the specific user to
                           whom the voice message belongs to.

After sending the transcripted message to the Unity Connection server, the copy of voice message in the transcription service
                           is purged.

## Considerations for Deploying SpeechView

Consider the following when deploying the SpeechView feature:

To enable SpeechView in a digital network deployment, consider onboarding one of the Unity Connection Cluster or Server in
                                 the Networking to Cisco Webex Cloud-Connected UC, this would act as Proxy server for other nodes in the Networking.

This can make it easier to troubleshoot any problems with transcriptions, track your transcription usage and monitor the load
                                 it introduces to your network. If one of your Unity Connection servers has a lower call volume than others in the network,
                                 consider designating it as the proxy server for transcriptions. If you do not use a proxy sever for transcriptions, Unity
                                 Connection server  onboarding to Cisco Webex Cloud-Connected UC will be required for each cluster in the network.

To extend the SpeechView functionality, users who want to transcribe the voice messages left on their personal number must
                                 configure their personal phones to forward calls to Unity Connection when a caller wants to leave a voicemail. This allows
                                 to collect all voicemails in one mailbox where they are transcribed. To configure the mobile phones for call forwarding, see
                                 the “Task List for Consolidating Your Voicemail from Multiple Phones into One Mailbox” section of the “Changing Your User
                                 Preferences” chapter of the User Guide for the Cisco Unity Connection Messaging Assistant Web Tool, Release 15, available
                                 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user/guide/assistant/b_15cucugasst/b_15cucugasst_index.html .

When personal phones are configured to forward callers to Unity Connection to leave voice messages, callers may hear a lot
                                             of rings before reaching the user mailbox. To avoid this problem, you can instead forward the mobile phone to a special number
                                             that does not ring a phone and forwards directly to the mailbox of the user. This can be accomplished by adding the special
                                             number as an alternate extension for the user.

To allow both transcription and relay of voice messages, configure the Message Action in Cisco Unity Connection Administration>
                                 Users to accept and relay messages. For more information, see the Message Actions section.

You can configure the SMTP notification devices to send the transcription text message to the SMTP address. This means users
                                 receive two emails at the SMTP address, first one is the relayed copy of the message.WAV file and the second one is the notification
                                 with transcription text. For more information on configuring SMTP notifications, see the Setting Up SMTP Message Notification section.

## Task List for Configuring SpeechView

This section contains a list of tasks to configure the SpeechView feature in Unity Connection:

Ensure that Unity Connection is registered with Cisco Smart Software Manager (CSSM) or Cisco Smart Software Manager satellite.
                                 You have acquired the proper licenses, SpeechView from Cisco to use this feature. For more information, see the “Managing
                                 Licenses” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

"Speechview Voicemail Transcription" feature option will only be visible on Cisco Webex Cloud-Connected UC when Unity Connection
                                                      is running on Release 15 SU2 and later.

Both the Nodes in Unity Connection Cluster should be onboarded to Cisco Webex Cloud Connected UC for High Availability of
                                                      Transcription.

Assign users to a class of service that provides SpeechView transcription of voice messages. For more information, see the Enabling SpeechView Transcription of Voice Messages in Class of Service .

Configure SpeechView transcription service. For more information, see the Configuring SpeechView Transcription Service .

### Enabling SpeechView Transcription of Voice Messages in Class of Service

The members of the class of service can view the transcriptions of the voice messages using an IMAP client configured to access
                                 the user messages.

Step 1

In Cisco Unity Connection Administration, expand Class of Service and select Class of Service.

Step 2

In the Search Class of Service page, select the class of service in which you want to enable SpeechView transcription or create
                                             a new one selecting Add New.

Step 3

On the Edit Class of Service page, under Licensing Features section, select the Use Standard SpeechView Transcription Service
                                             option to enable the standard transcription.

Step 4

Select the applicable options under transcription service section and select Save. (For information on each field, see Help>
                                             This Page).

### Configuring SpeechView Transcription Service

Step 1

In Cisco Unity Connection Administration, expand Unified Messaging and select SpeechView Transcription Service.

Step 2

In the SpeechView Transcription Service page, verify that the speechview status is enabled.

Step 3

Configure SpeechView transcription service (For more information, see Help> This Page):

Transcription services can be accessed by Unity Connection server directly or through proxy location.

If this server is going to access trancription services directly, do the given steps:

Select Access Transcription Service Directly field.

If you want this server to offer transcription proxy services to other Unity Connection locations in a digital network, check
                                                         the Advertise Transcription Proxy Services to Other Unity Connection Locations check box.

If this server accesses the transcription services through another digitally networked Unity Connection location, select the
                                                   Access Transcription Services through Unity Connection Proxy Location field. Select the name of the Unity Connection location
                                                   from the list.

Select Save and then Sync License Data.

Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data.

Step 4

To verify the configuration of SpeechView Transcription Service, click on Test. Another window displaying the results open.
                                          The test usually takes several minutes but can take up to 15 minutes.

## SpeechView Reports

Unity Connection can generate the following reports about SpeechView usage:

SpeechView Activity Report by User —Shows the total number of transcribed messages, failed transcriptions, and truncated transcriptions
                                 for a given user during a given time period.

SpeechView Activity Summary Report—Shows the total number of transcribed messages, failed transcriptions, and truncated transcriptions
                                 for the entire system during a given time period. Note that when messages are sent to multiple recipients, the message is
                                 transcribed only once, so the transcription activity is counted only once.

## SpeechView Transcription Error Codes

Whenever a transcription fails, the Cisco Webex in-house transcription service sends an error code to Unity Connection.

Cisco Unity Connection Administration interface shows the five default error codes that can modified or deleted by an administrator.
                           In addition, user has the privilege to add a new error code. Whenever a new error code is sent by the Cisco Webex in-house
                           transcription service, the administrator needs to add a new error code along with the appropriate description.

- The error code and description should be in the default system language.

- If the error code provisioning is not done, then the error code received from the Cisco Webex in-house transcription service
                                          is displayed.

The default error codes are sent by the Cisco Webex in-house transcription service to the SpeechView user. The Table 14-1 shows the default error codes in the Cisco Unity Connection Administration interface.

Default Error Codes

Error Code Name

Description

Fault

When Unity Connection tries to register with the Cisco Webex in-house transcription service and the registration fails.

Inaudible

When a voice mail sent by a SpeechView user is inaudible at the Cisco Webex in-house transcription service site and system
                                       was unable to transcribe the message.

Rejected

When the conversion request contains more than one audio file attachment, Cisco Webex in-house transcription service rejects
                                       the messages.

Time-out

Whenever there is a response timeout from the Cisco Webex in-house transcription service.

Unconverted

When the Cisco Webex in-house transcription service is not able to transcript the voice mail sent by a SpeechView user.

### Configuring Transcription Error Codes

Step 1

In Cisco Unity Connection Administration, expand Unified Messaging > SpeechView Transcription, and select Error Codes .

Step 2

The Search Transcription Error Codes appears displaying the currently configured error codes.

Step 3

Configure transcription error code (For more information on each field, see Help> This Page):

To add a transcription error code, select Add New .

On the New Transcription Error Code page, enter the error code and the error code description to create a new error code.

Select Save .

To edit a transcription error code, select the error code that you want to edit.

On the Edit Transcription Error Code (Fault) page, change the error code or the error code description, as applicable.

Select Save .

To delete a transcription error code, check the check box adjacent to the display name of the schedule that you want to delete.
                                                   Select Delete Selected and OK to confirm deletion.

| Note | When a voice message is sent from Web Inbox to ViewMail for Outlook, the voice message is delivered to the mailbox of the
                                       recipient along with the transcribed text both in the transcript view box and in the mail body. |
|---|---|

| Note | Unity Connection supports only (Universal Transformation Format) UTF-8 character set encoding for transcription. |
|---|---|

| Note | Cisco Webex in-house transcription service server converts the voice message to text into the phone language in which Unity
                                    Connection plays system prompts to users and callers.You can set the phone language for the following Unity Connection components:
                                    user accounts, routing rules, call handlers, interview handlers, and directory handlers. For information on supported language
                                    for SpeechView, see Available Languages for Unity Connection Components section of System Requirements for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html . |
|---|---|

| Note | For the above configuration to take effect, restart the "Connection SpeechView Processor" service from the Connection Serviceability
                                       page of the Publisher server in the Unity Connection cluster. |
|---|---|

| Note | In order to use SpeechView in Digital Networking, all nodes in the network must be running on release 15 SU2or later. |
|---|---|

| Note | When personal phones are configured to forward callers to Unity Connection to leave voice messages, callers may hear a lot
                                             of rings before reaching the user mailbox. To avoid this problem, you can instead forward the mobile phone to a special number
                                             that does not ring a phone and forwards directly to the mailbox of the user. This can be accomplished by adding the special
                                             number as an alternate extension for the user. |
|---|---|

| Note | "Speechview Voicemail Transcription" feature option will only be visible on Cisco Webex Cloud-Connected UC when Unity Connection
                                                      is running on Release 15 SU2 and later. Both the Nodes in Unity Connection Cluster should be onboarded to Cisco Webex Cloud Connected UC for High Availability of
                                                      Transcription. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Class of Service and select Class of Service. |
|---|---|
| Step 2 | In the Search Class of Service page, select the class of service in which you want to enable SpeechView transcription or create
                                             a new one selecting Add New. |
| Step 3 | On the Edit Class of Service page, under Licensing Features section, select the Use Standard SpeechView Transcription Service
                                             option to enable the standard transcription. |
| Step 4 | Select the applicable options under transcription service section and select Save. (For information on each field, see Help>
                                             This Page). |

| Step 1 | In Cisco Unity Connection Administration, expand Unified Messaging and select SpeechView Transcription Service. |
|---|---|
| Step 2 | In the SpeechView Transcription Service page, verify that the speechview status is enabled. |
| Step 3 | Configure SpeechView transcription service (For more information, see Help> This Page): Transcription services can be accessed by Unity Connection server directly or through proxy location. If this server is going to access trancription services directly, do the given steps: Select Access Transcription Service Directly field. If you want this server to offer transcription proxy services to other Unity Connection locations in a digital network, check
                                                         the Advertise Transcription Proxy Services to Other Unity Connection Locations check box. If this server accesses the transcription services through another digitally networked Unity Connection location, select the
                                                   Access Transcription Services through Unity Connection Proxy Location field. Select the name of the Unity Connection location
                                                   from the list. Select Save and then Sync License Data. Note Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data. | Note | Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data. |
| Note | Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data. |
| Step 4 | To verify the configuration of SpeechView Transcription Service, click on Test. Another window displaying the results open.
                                          The test usually takes several minutes but can take up to 15 minutes. |

| Note | Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data. |
|---|---|

| Note | The error code and description should be in the default system language. If the error code provisioning is not done, then the error code received from the Cisco Webex in-house transcription service
                                          is displayed. |
|---|---|

| Error Code Name | Description |
|---|---|
| Fault | When Unity Connection tries to register with the Cisco Webex in-house transcription service and the registration fails. |
| Inaudible | When a voice mail sent by a SpeechView user is inaudible at the Cisco Webex in-house transcription service site and system
                                       was unable to transcribe the message. |
| Rejected | When the conversion request contains more than one audio file attachment, Cisco Webex in-house transcription service rejects
                                       the messages. |
| Time-out | Whenever there is a response timeout from the Cisco Webex in-house transcription service. |
| Unconverted | When the Cisco Webex in-house transcription service is not able to transcript the voice mail sent by a SpeechView user. |

| Step 1 | In Cisco Unity Connection Administration, expand Unified Messaging > SpeechView Transcription, and select Error Codes . |
|---|---|
| Step 2 | The Search Transcription Error Codes appears displaying the currently configured error codes. |
| Step 3 | Configure transcription error code (For more information on each field, see Help> This Page): To add a transcription error code, select Add New . On the New Transcription Error Code page, enter the error code and the error code description to create a new error code. Select Save . To edit a transcription error code, select the error code that you want to edit. On the Edit Transcription Error Code (Fault) page, change the error code or the error code description, as applicable. Select Save . To delete a transcription error code, check the check box adjacent to the display name of the schedule that you want to delete.
                                                   Select Delete Selected and OK to confirm deletion. |