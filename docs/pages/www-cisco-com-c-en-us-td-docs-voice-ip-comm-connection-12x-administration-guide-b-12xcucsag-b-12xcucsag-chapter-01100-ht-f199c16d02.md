---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-administration-guide-b-12xcucsag-b-12xcucsag-chapter-01100-ht-f199c16d02
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag/b_12xcucsag_chapter_01100.html
retrieved_at: 2026-08-17T02:31:39.063020+00:00
---

System Administration Guide

# System Administration Guide

Updated: August 1, 2017

Chapter: SpeechView

## Chapter: SpeechView

# SpeechView

## Overview

The SpeechView feature enables the transcription of voice
                           		messages so that users can receive the voicemails in the form of text. Users
                           		can access the transcripted voicemails using email clients. SpeechView is a
                           		feature of Cisco Unity Connection unified messaging solution. Therefore, the
                           		audio part of each voice message is also available to the users.

When a voice message is sent from Web Inbox to ViewMail for
                                       		  Outlook, the voice message is delivered to the mailbox of the recipient along
                                       		  with the transcribed text both in the transcript view box and in the mail body.

Without this feature, the voice message delivered to the user
                           		mailbox has a blank text attachment. This feature requires the use of a third
                           		party transcription service to convert the voice message to text. Therefore,
                           		the blank text attachment is updated with the transcripted text or an error
                           		message if there was a problem with transcription.

The SpeechView feature supports the following types of
                           		transcription services:

Standard Transcription Service: The standard transcription
                                 			 service automatically converts the voice message to text and the transcripted
                                 			 text received is sent to the user over email.

Professional Transcription Service: The professional
                                 			 transcription or SpeechView Pro service automatically converts the voice
                                 			 message to text and then confirms the accuracy of transcription. If the
                                 			 accuracy of trancription is low at any part, the particular part of
                                 			 trancription text is sent to a human operator who reviews the audio and
                                 			 improves the quality of transcription.

As the professional transcription involves both automatic
                           		transcription and accuracy confirmation by a human operator, it delivers more
                           		accurate transcripted texts of voice messages.

Unity Connection supports only (Universal Transformation Format)
                                       		  UTF-8 character set encoding for transcription.

The following messages are never transcribed:

Private messages

Broadcast messages

Dispatch messages

Secure messages

Messages with no recipients

Unity Connection can
                           		be configured to deliver transcriptions to an SMS device as a text message or
                           		to an SMTP address as an email message. The fields to turn on transcription
                           		delivery are located on the SMTP and SMS Notification Device pages where you
                           		set up message notification. For more information on notification devices, see
                           		the Configuring Notification Devices section.

Following are the considerations for effective use of
                           		transcription delivery:

In the From field, enter the number users dial to reach Unity
                                 			 Connection when they are not dialing from their desk phone. If users have a
                                 			 text-compatible mobile phone, they may be able to initiate a callback to Unity
                                 			 Connection in the event that they want to listen to the message.

Check the Include Message Information in Message Text check box
                                 			 to include call information such as caller name and caller ID (if available)
                                 			 and the time that the message was received. Otherwise, there is no indication
                                 			 in the message of when it was received.

In addition, if they have a text-compatible mobile phone, they
                           		may be able to initiate a callback when the caller ID is included with the
                           		transcription.

In the Notify Me Of section, if you turn on notification for
                                 			 voice or dispatch messages, users are notified when a message arrives. The
                                 			 transcription soon follows. If you do not want notification before the
                                 			 transcription arrives, do not select the voice or dispatch message options.

Email messages that contain transcriptions have a subject line
                                 			 that is identical to notification messages. So if you have notification for
                                 			 voice or dispatch messages turned on, users have to open the messages to
                                 			 determine which one contains the transcription.

```
run cuc dbquery unitydirdb update tbl_configuration set valuebool ='1' where fullname='System.Conversations.ConfigParamForAlternateTranscriptionLanguage'
```

## SpeechView Security Considerations

S/MIME (Secure/ Multipurpose Internet Mail Extensions), a standard for public key encryption, secures the communication between
                           Unity Connection and the third party transcription service. A private key and public key is generated each time Unity Connection
                           registers with a third party transcription service.

The pair of private and public keys ensures that each time voice messages are sent to the transcription service, the user
                           information is not passed along with the message. Therefore, the transcription service is unaware of the specific user to
                           whom the voice message belongs to.

If human operator is involved during transcription, the user or the organization from which the message generated cannot be
                           determined. In addition to this, the audio part of a voice message is never stored in the workstation of the person processing
                           the transcription service. After sending the transcripted message to the Unity Connection server, the copy in the transcription
                           service is purged.

## Considerations for
                        	 Deploying SpeechView

Consider the following when deploying the SpeechView feature:

To enable SpeechView in a digital network deployment, consider
                                 			 configuring one of the Unity Connection servers in the network as a proxy
                                 			 server that registers with the third party transcription service.

This can make it easier to troubleshoot any problems with
                           		transcriptions, track your transcription usage and monitor the load it
                           		introduces to your network. If one of your Unity Connection servers has a lower
                           		call volume than others in the network, consider designating it as the proxy
                           		server for transcriptions. If you do not use a proxy server for transcriptions,
                           		you need a separate external facing SMTP address for each server (or cluster)
                           		in the network.

To extend the SpeechView functionality, users who want to
                                 			 transcribe the voice messages left on their personal number must configure
                                 			 their personal phones to forward calls to Unity Connection when a caller wants
                                 			 to leave a voicemail. This allows to collect all voicemails in one mailbox
                                 			 where they are transcribed. To configure the mobile phones for call forwarding,
                                 			 see the “Task List for Consolidating Your Voicemail from Multiple Phones into
                                 			 One Mailbox” section of the “Changing Your User Preferences” chapter of the
                                 			 User Guide for the Cisco Unity Connection Messaging Assistant Web Tool, Release
                                 			 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/assistant/b_12xcucugasst.html .

When personal phones are configured to forward callers to Unity
                                             				Connection to leave voice messages, callers may hear a lot of rings before
                                             				reaching the user mailbox. To avoid this problem, you can instead forward the
                                             				mobile phone to a special number that does not ring a phone and forwards
                                             				directly to the mailbox of the user. This can be accomplished by adding the
                                             				special number as an alternate extension for the user.

To allow both transcription and relay of voice messages,
                                 			 configure the Message Action in Cisco Unity Connection Administration> Users
                                 			 to accept and relay messages. For more information, see the Message
                                    				Actions section.

You can configure the SMTP notification devices to send the
                                 			 transcription text message to the SMTP address. This means users receive two
                                 			 emails at the SMTP address, first one is the relayed copy of the message.WAV
                                 			 file and the second one is the notification with transcription text. For more
                                 			 information on configuring SMTP notifications, see the Setting
                                    				Up SMTP Message Notification section.

## Task List for
                        	 Configuring SpeechView

This section contains a list of tasks to configure the
                           		SpeechView feature in Unity Connection:

Ensure that Unity Connection is registered with Cisco Smart
                                 			 Software Manager (CSSM) or Cisco Smart Software Manager satellite. You have
                                 			 acquired the proper licenses, SpeechView or SpeechViewPro from Cisco to use
                                 			 this feature. For more information, see the “Managing Licenses” chapter of the
                                 			 Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release
                                 			 12.x, available at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html

Assign users to a class of service that provides SpeechView
                                 			 transcription of voice messages. For more information, see the Enabling
                                    				SpeechView Transcription of Voice Messages in Class of Service section.

Configure an SMTP smart host to accept messages from the Unity
                                 			 Connection server. For more information, see the documentation for the SMTP
                                 			 server application that you are using.

Configure the Unity Connection server to relay messages to the
                                 			 smart host. For more information, see the Configuring
                                    				Unity Connection to Relay Messages to a Smart Host section.

(When Unity Connection is configured to refuse connections from
                                 			 untrusted IP addresses) Configure Unity Connection to receive messages from the
                                 			 user email address. For more information, see the Configuring
                                    				Unity Connection to Accept Messages from Email System section.

Configure the user email system to route incoming SpeechView
                                 			 traffic to Unity Connection. For more information, see the Configuring
                                    				Email System to Route Incoming SpeechView Traffic section.

Configure SpeechView transcription service. For more
                                 			 information, see the Configuring
                                    				SpeechView Transcription Service, page 13-5 section.

Configure SMS or SMTP notification devices for users and user
                                 			 templates. For more information, see the Setting Up SMTP Message
                                    				Notification section.

### Enabling SpeechView Transcription of Voice Messages in Class of
                           	 Service

The members of the class of service can view the
                                 		  transcriptions of the voice messages using an IMAP client configured to access
                                 		  the user messages.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Class of Service and select Class of Service.

Step 2

In the Search Class of Service page, select
                                          			 the class of service in which you want to enable SpeechView transcription or
                                          			 create a new one selecting Add New.

Step 3

On the Edit Class of Service page, under Licensing Features section, select the Use Standard SpeechView Transcription Service
                                          option to enable the standard transcription. Similarly, you may select Use SpeechView Pro Transcription Service option to
                                          enable professional transcription.

Cisco Unity Connection 12.5(1) Service Update 4 and later, supports only Standard SpeechView Transcription Service in HCS mode.

Step 4

Select the applicable options under
                                          			 transcription service section and select Save. (For information on each field,
                                          			 see Help> This Page).

### Configuring Unity Connection to Relay Messages to a Smart Host

To enable Unity Connection to send messages to
                                 		  the third party transcription service, you must configure the Unity Connection
                                 		  server to relay messages through a smart host.

If we configure SpeechView on Unity Connection with Exchange Server as Microsoft Office 365, then on prem Microsoft Exchange
                                             as Smart Host is not a essential requirement.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings> SMTP Configuration and select Smart Host.

Step 2

In the Smart Host page, in the Smart Host
                                          			 field, enter the IP address or fully qualified domain name of the SMTP smart
                                          			 host server and select Save. (For more information on each field, see Help>
                                          			 This Page).

The Smart Host can contain up to 50 characters.

### Configuring Unity Connection to Accept Messages from Email
                           	 System

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings> SMTP Configuration and select Server.

Step 2

In the SMTP Server Configuration page, in
                                          			 the Edit menu, select Search IP Address Access
                                             				List .

Step 3

On the Search IP Address Access List page,
                                          			 select Add New to add a new IP
                                          			 address to the list.

Step 4

On the New Access IP Address page, enter the
                                          			 IP address of your email server and select Save .

Step 5

To allow connections from the IP address
                                          			 that you entered in Step 4 , check the Allow Unity Connection check box and select Save .

Step 6

If you have more than one email server in
                                          			 your organization, repeat Step 2 through Step 6 to add each additional
                                          			 IP address to the access list.

### Configuring Email System to Route Incoming SpeechView Traffic

Step 1

Set up an external facing SMTP address that
                                          			 the third party transcription service can use to send transcriptions to Unity
                                          			 Connection. For example, “transcriptions@<yourdomain.com>”

If you have more than one Unity Connection
                                             				server or cluster, you need a separate external facing SMTP address for each
                                             				server. Alternatively, you can configure one Unity Connection server or cluster
                                             				to act as a proxy for the remaining servers or clusters in the digital network.
                                             				For example, if the SMTP domain for the Unity Connection server is “Unity
                                             				Connectionserver1.cisco.com,” the email infrastructure must be configured to
                                             				route “transcriptions@cisco.com” to “stt-service@connectionserver1.cisco.com.”

If you are configuring SpeechView on a Unity
                                             				Connection cluster, configure the smart host to resolve the SMTP domain of the
                                             				cluster to both the publisher and subscriber servers in order for incoming
                                             				transcriptions to reach the cluster subscriber server in the event that the
                                             				publisher server is down.

Step 2

Add “nuancevm.com” to the “safe senders” list in the email
                                          			 infrastructure so that incoming transcriptions do not get filtered out as spam.

In Unity Connection, to avoid timeout or
                                                         				  failure of the registration request with the Nuance server, make sure to:

Remove the email disclaimers from the
                                                               						inbound and outbound email messages between Unity Connection and the Nuance
                                                               						server.

Maintain SpeechView registration
                                                               						messages in the S/MIME format.

### Configuring
                           	 SpeechView Transcription Service

Step 1

In Cisco Unity Connection Administration, expand Unified
                                          			 Messaging and select SpeechView Transcription Service.

Step 2

In the SpeechView Transcription Service page, check the Enabled
                                          			 check box.

Step 3

Configure SpeechView transcription service (For more
                                          			 information, see Help> This Page):

If this server access the transcription services through another
                                                   					 Unity Connection location that is digitally networked, select the Access
                                                   					 Transcription Services Through Unity Connection Proxy Location field. Select
                                                   					 the name of the Unity Connection location from the list and select Save. Skip
                                                   					 to Step 4 .

If the server is going to access trancription services through
                                                   					 another location that isdigitally networked, do the given steps:

Select Access Transcription Service Directly field.

In the Incoming SMTP Address field, enter the email address
                                                   					 recognized by the email system and routed to the “stt-service” alias on the
                                                   					 Unity Connection server.

In the Registration Name field, enter a name that identifies the
                                                   					 Unity Connection server within your organization. This name is used by the
                                                   					 third party transcription service to identify this server for registration and
                                                   					 subsequent transcription requests.

If you want this server to offer transcription proxy services to
                                                   					 other Unity Connection locations in a digital network, check the Advertise
                                                   					 Transcription Proxy Services to Other Unity Connection Locations check box.
                                                   					 Select Save and then Register.

Another window displaying the results open. Wait for the
                                                   					 registration process to complete successfully before going on to the next step.
                                                   					 If registration does not complete within 5 minutes, there may be a
                                                   					 configuration issue. The registration process timeout after 30 minutes.

Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data with PLM.

Step 4

Select Test. Another window displaying the results open. The test
                                          			 usually takes several minutes but can take up to 30 minutes.

## SpeechView Reports

Unity Connection can generate the following reports about SpeechView usage:

SpeechView Activity Report by User —Shows the total number of transcribed messages, failed transcriptions, and truncated transcriptions
                                 for a given user during a given time period.

SpeechView Activity Summary Report—Shows the total number of transcribed messages, failed transcriptions, and truncated transcriptions
                                 for the entire system during a given time period. Note that when messages are sent to multiple recipients, the message is
                                 transcribed only once, so the transcription activity is counted only once.

## SpeechView
                        	 Transcription Error Codes

Whenever a transcription fails, the third party external
                           		transcription service sends an error code to Unity Connection.

Cisco Unity Connection Administration interface shows the five
                           		default error codes that can modified or deleted by an administrator. In
                           		addition, user has the privilege to add a new error code. Whenever a new error
                           		code is sent by the third party external transcription service, the
                           		administrator needs to add a new error code along with the appropriate
                           		description.

- The error code and
                                          			 description should be in the default system language.

- If the error code
                                          			 provisioning is not done, then the error code received from the third party
                                          			 external transcription service is displayed.

The default error codes are sent by the third party external
                           		transcription service to the SpeechView user. The Table 13-1 shows the
                           		default error codes in the Cisco Unity Connection Administration interface.

Default Error Codes

Error Code Name

Description

Fault

When Unity Connection tries to register with the third party
                                       					 external transcription service and the registration fails.

Inaudible

When a voice mail sent by a SpeechView user is inaudible at the
                                       					 third party external transcription service site and system was unable to
                                       					 transcribe the message.

Rejected

When the conversion request contains more than one audio file
                                       					 attachment, the third party external transcription service rejects the
                                       					 messages.

Time-out

Whenever there is a response timeout from the third party
                                       					 external transcription service.

Unconverted

When the third party external transcription service is not able
                                       					 to transcript the voice mail sent by a SpeechView user.

### Configuring Transcription Error Codes

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Unified Messaging > SpeechView Transcription, and select Error Codes .

Step 2

The Search Transcription Error Codes appears
                                          			 displaying the currently configured error codes.

Step 3

Configure transcription error code (For more
                                          			 information on each field, see Help> This Page):

To add a transcription error code,
                                                   					 select Add New .

On the New Transcription Error Code
                                                   					 page, enter the error code and the error code description to create a new error
                                                   					 code.

Select Save .

To edit a transcription error code,
                                                   					 select the error code that you want to edit.

On the Edit Transcription Error Code
                                                   					 (Fault) page, change the error code or the error code description, as
                                                   					 applicable.

Select Save .

To delete a transcription error code,
                                                   					 check the check box adjacent to the display name of the schedule that you want
                                                   					 to delete. Select Delete Selected and OK to confirm
                                                   					 deletion.

| Note | When a voice message is sent from Web Inbox to ViewMail for
                                       		  Outlook, the voice message is delivered to the mailbox of the recipient along
                                       		  with the transcribed text both in the transcript view box and in the mail body. |
|---|---|

| Note | Unity Connection supports only (Universal Transformation Format)
                                       		  UTF-8 character set encoding for transcription. |
|---|---|

| Note | Secure messages are not transcribed by default, however the Class of Service provides an option under Licensed Features which
                                    enables the SpeechView Transcription Service. |
|---|---|

| Note | For Speechview
                                       		  feature, it is recommended not to use any interference device, such as Email
                                       		  Scanner as the device might modify the content of the data being exchanged with
                                       		  the nuance server. Using such devices may lead to the failure of audio message
                                       		  transcriptions. |
|---|---|

| Note | Nuance server converts the voice message to text into the phone language in which Unity Connection plays system prompts to
                                    users and callers. If phone language is not supported by nuance, it recognizes the audio of the message and converts into
                                    the language of the audio. You can set the phone language for the following Unity Connection components: user accounts, routing
                                    rules, call handlers, interview handlers, and directory handlers. For information on supported language for SpeechView, see Available Languages for Unity Connection Components section of System Requirements for Cisco Unity Connection Release 12.x available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html |
|---|---|

| Note | When personal phones are configured to forward callers to Unity
                                             				Connection to leave voice messages, callers may hear a lot of rings before
                                             				reaching the user mailbox. To avoid this problem, you can instead forward the
                                             				mobile phone to a special number that does not ring a phone and forwards
                                             				directly to the mailbox of the user. This can be accomplished by adding the
                                             				special number as an alternate extension for the user. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Class of Service and select Class of Service. |
|---|---|
| Step 2 | In the Search Class of Service page, select
                                          			 the class of service in which you want to enable SpeechView transcription or
                                          			 create a new one selecting Add New. |
| Step 3 | On the Edit Class of Service page, under Licensing Features section, select the Use Standard SpeechView Transcription Service
                                          option to enable the standard transcription. Similarly, you may select Use SpeechView Pro Transcription Service option to
                                          enable professional transcription. Note Cisco Unity Connection 12.5(1) Service Update 4 and later, supports only Standard SpeechView Transcription Service in HCS mode. | Note | Cisco Unity Connection 12.5(1) Service Update 4 and later, supports only Standard SpeechView Transcription Service in HCS mode. |
| Note | Cisco Unity Connection 12.5(1) Service Update 4 and later, supports only Standard SpeechView Transcription Service in HCS mode. |
| Step 4 | Select the applicable options under
                                          			 transcription service section and select Save. (For information on each field,
                                          			 see Help> This Page). |

| Note | Cisco Unity Connection 12.5(1) Service Update 4 and later, supports only Standard SpeechView Transcription Service in HCS mode. |
|---|---|

| Note | If we configure SpeechView on Unity Connection with Exchange Server as Microsoft Office 365, then on prem Microsoft Exchange
                                             as Smart Host is not a essential requirement. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings> SMTP Configuration and select Smart Host. |
|---|---|
| Step 2 | In the Smart Host page, in the Smart Host
                                          			 field, enter the IP address or fully qualified domain name of the SMTP smart
                                          			 host server and select Save. (For more information on each field, see Help>
                                          			 This Page). Note The Smart Host can contain up to 50 characters. | Note | The Smart Host can contain up to 50 characters. |
| Note | The Smart Host can contain up to 50 characters. |

| Note | The Smart Host can contain up to 50 characters. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings> SMTP Configuration and select Server. |
|---|---|
| Step 2 | In the SMTP Server Configuration page, in
                                          			 the Edit menu, select Search IP Address Access
                                             				List . |
| Step 3 | On the Search IP Address Access List page,
                                          			 select Add New to add a new IP
                                          			 address to the list. |
| Step 4 | On the New Access IP Address page, enter the
                                          			 IP address of your email server and select Save . |
| Step 5 | To allow connections from the IP address
                                          			 that you entered in Step 4 , check the Allow Unity Connection check box and select Save . |
| Step 6 | If you have more than one email server in
                                          			 your organization, repeat Step 2 through Step 6 to add each additional
                                          			 IP address to the access list. |

| Step 1 | Set up an external facing SMTP address that
                                          			 the third party transcription service can use to send transcriptions to Unity
                                          			 Connection. For example, “transcriptions@<yourdomain.com>” If you have more than one Unity Connection
                                             				server or cluster, you need a separate external facing SMTP address for each
                                             				server. Alternatively, you can configure one Unity Connection server or cluster
                                             				to act as a proxy for the remaining servers or clusters in the digital network.
                                             				For example, if the SMTP domain for the Unity Connection server is “Unity
                                             				Connectionserver1.cisco.com,” the email infrastructure must be configured to
                                             				route “transcriptions@cisco.com” to “stt-service@connectionserver1.cisco.com.” If you are configuring SpeechView on a Unity
                                             				Connection cluster, configure the smart host to resolve the SMTP domain of the
                                             				cluster to both the publisher and subscriber servers in order for incoming
                                             				transcriptions to reach the cluster subscriber server in the event that the
                                             				publisher server is down. |
|---|---|
| Step 2 | Add “nuancevm.com” to the “safe senders” list in the email
                                          			 infrastructure so that incoming transcriptions do not get filtered out as spam. Note In Unity Connection, to avoid timeout or
                                                         				  failure of the registration request with the Nuance server, make sure to: Remove the email disclaimers from the
                                                               						inbound and outbound email messages between Unity Connection and the Nuance
                                                               						server. Maintain SpeechView registration
                                                               						messages in the S/MIME format. | Note | In Unity Connection, to avoid timeout or
                                                         				  failure of the registration request with the Nuance server, make sure to: Remove the email disclaimers from the
                                                               						inbound and outbound email messages between Unity Connection and the Nuance
                                                               						server. Maintain SpeechView registration
                                                               						messages in the S/MIME format. |
| Note | In Unity Connection, to avoid timeout or
                                                         				  failure of the registration request with the Nuance server, make sure to: Remove the email disclaimers from the
                                                               						inbound and outbound email messages between Unity Connection and the Nuance
                                                               						server. Maintain SpeechView registration
                                                               						messages in the S/MIME format. |

| Note | In Unity Connection, to avoid timeout or
                                                         				  failure of the registration request with the Nuance server, make sure to: Remove the email disclaimers from the
                                                               						inbound and outbound email messages between Unity Connection and the Nuance
                                                               						server. Maintain SpeechView registration
                                                               						messages in the S/MIME format. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Unified
                                          			 Messaging and select SpeechView Transcription Service. |
|---|---|
| Step 2 | In the SpeechView Transcription Service page, check the Enabled
                                          			 check box. |
| Step 3 | Configure SpeechView transcription service (For more
                                          			 information, see Help> This Page): If this server access the transcription services through another
                                                   					 Unity Connection location that is digitally networked, select the Access
                                                   					 Transcription Services Through Unity Connection Proxy Location field. Select
                                                   					 the name of the Unity Connection location from the list and select Save. Skip
                                                   					 to Step 4 . If the server is going to access trancription services through
                                                   					 another location that isdigitally networked, do the given steps: Select Access Transcription Service Directly field. In the Incoming SMTP Address field, enter the email address
                                                   					 recognized by the email system and routed to the “stt-service” alias on the
                                                   					 Unity Connection server. In the Registration Name field, enter a name that identifies the
                                                   					 Unity Connection server within your organization. This name is used by the
                                                   					 third party transcription service to identify this server for registration and
                                                   					 subsequent transcription requests. If you want this server to offer transcription proxy services to
                                                   					 other Unity Connection locations in a digital network, check the Advertise
                                                   					 Transcription Proxy Services to Other Unity Connection Locations check box.
                                                   					 Select Save and then Register. Another window displaying the results open. Wait for the
                                                   					 registration process to complete successfully before going on to the next step.
                                                   					 If registration does not complete within 5 minutes, there may be a
                                                   					 configuration issue. The registration process timeout after 30 minutes. Note Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data with PLM. | Note | Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data with PLM. |
| Note | Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data with PLM. |
| Step 4 | Select Test. Another window displaying the results open. The test
                                          			 usually takes several minutes but can take up to 30 minutes. |

| Note | Make sure to save all the configuration of Speech View Transcription Services before synchronizing the license data with PLM. |
|---|---|

| Note | The error code and
                                          			 description should be in the default system language. If the error code
                                          			 provisioning is not done, then the error code received from the third party
                                          			 external transcription service is displayed. |
|---|---|

| Error Code Name | Description |
|---|---|
| Fault | When Unity Connection tries to register with the third party
                                       					 external transcription service and the registration fails. |
| Inaudible | When a voice mail sent by a SpeechView user is inaudible at the
                                       					 third party external transcription service site and system was unable to
                                       					 transcribe the message. |
| Rejected | When the conversion request contains more than one audio file
                                       					 attachment, the third party external transcription service rejects the
                                       					 messages. |
| Time-out | Whenever there is a response timeout from the third party
                                       					 external transcription service. |
| Unconverted | When the third party external transcription service is not able
                                       					 to transcript the voice mail sent by a SpeechView user. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Unified Messaging > SpeechView Transcription, and select Error Codes . |
|---|---|
| Step 2 | The Search Transcription Error Codes appears
                                          			 displaying the currently configured error codes. |
| Step 3 | Configure transcription error code (For more
                                          			 information on each field, see Help> This Page): To add a transcription error code,
                                                   					 select Add New . On the New Transcription Error Code
                                                   					 page, enter the error code and the error code description to create a new error
                                                   					 code. Select Save . To edit a transcription error code,
                                                   					 select the error code that you want to edit. On the Edit Transcription Error Code
                                                   					 (Fault) page, change the error code or the error code description, as
                                                   					 applicable. Select Save . To delete a transcription error code,
                                                   					 check the check box adjacent to the display name of the schedule that you want
                                                   					 to delete. Select Delete Selected and OK to confirm
                                                   					 deletion. |