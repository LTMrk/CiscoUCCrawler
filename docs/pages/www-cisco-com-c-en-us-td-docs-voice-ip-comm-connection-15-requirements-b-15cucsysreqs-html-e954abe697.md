---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-requirements-b-15cucsysreqs-html-e954abe697
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html
retrieved_at: 2026-08-16T18:50:55.866855+00:00
---

System Requirements for Cisco Unity Connection Release 15

# System Requirements for Cisco Unity Connection Release 15

### Download Options

Updated: August 12, 2025

First Published: December 18, 2023

Last Updated: August 12, 2025

# System Requirements for Cisco Unity Connection Release 15

This document lists requirements for a Cisco Unity Connection version 15 system. It contains the following sections:

## Hardware
               	 Requirements

A server that meets Cisco Unity Connection specifications. See the Cisco Unity Connection 15 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

Caution

If you try to install version 15 on an unsupported platform, Unity Connection will not be displayed as an option in the Product
                                 Deployment Selection window of the installation program. See the server-specific table in the “Unity Connection Supported
                                 Servers” section of Cisco Unity Connection 15 Supported Platforms List to verify platform specifications, particularly regarding memory and processor speed.

Unity Connection 15 can only be installed on virtual servers. If you are upgrading from an earlier version of Unity Connection
                        or migrating from Cisco Unity to Unity Connection 15, you need to replace the existing server with a virtual machine. For
                        information on migrating a physical server to virtual server, see the “ Migrating from Cisco Unity 4.x and Later to Unity Connection 7.x and Later ” section of the “Maintaining Cisco Unity Connection Server” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity
                        Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

If you are adding features, for example, Unity Connection Networking, a Unity Connection cluster, or single inbox, you may
                        need to replace hard disks or add memory to the Unity Connection server for the feature to be supported. For more information,
                        see the applicable server-specific table in the Cisco Unity Connection 15 Supported Platforms List .

The list of supported virtual platform is listed in the Cisco Unity Connection 15 Supported Platforms List .

## Software Requirements

This section contains the following information:

### Software Requirements-Unity Connection Server

Unity Connection software and any required
                     		third-party software are installed by Unity Connection Setup.

### Software
                  	 Requirements—Administrator Workstations (Unity Connection and Unity Connection
                  	 SRSV )

To access web
                        		  applications on the Unity Connection and Unity Connection SRSV server, the
                        		  operating system and web browser must be compatible with the version of Unity
                        		  Connection that you are installing. Table 1 lists supported operating-system and browser combinations.

Browser on Administrator Workstation

Mac OS 13 (macOS Ventura)

Safari

Microsoft Windows 11 (32-bit and 64-bit)

Enterprise

Professional

Mozilla Firefox

Chrome

Edge

Microsoft Windows 10 (32-bit and 64-bit)

Enterprise

Professional

Mozilla Firefox

Chrome

Edge

On CentOS, the
                                    			 IPv6 address is supported only through DNS.

For more information on supported operating systems and
                        		  browsers, see the Compatibility Matrix: Cisco Unity Connection and the Software
                        		  on User Workstations Guide at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

### Software
                  	 Requirements—User Workstations

The operating system and Web browser(s) on user workstations
                              				must be compatible with the version of Unity Connection that you are
                              				installing, to allow users to access the Unity Connection web tools through the
                              				Cisco Personal Communications Assistant. See the Compatibility Matrix for
                              				Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

If you are using Cisco Unity Connection ViewMail for Microsoft
                              				Outlook, the ViewMail version must be compatible with the version of Unity
                              				Connection that you are installing.

If you are using an IMAP email application to access Unity
                              				Connection voice messages, the email application must be compatible with the
                              				version of Unity Connection that you are installing.

## Requirements for
               	 the Phone System Integration

Unity Connection can
                  		be integrated with Cisco Unified Communications Manager and Cisco Unified
                  		Communications Manager Express.

In addition, Cisco
                  		Unified CM integrations with Unity Connection support the use at remote sites
                  		of Cisco Unified CM Express in Survivable Remote Site Telephony (SRST) mode or
                  		of SRST installed on Cisco IOS platforms.

For supported versions of Cisco Unified CM and Cisco Unified CM
                  		Express, see the Compatibility Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

The SIP Trunk can also be referred for PIMG/TIMG integrations.
                        			 For information on PIMG/TIMG integrations , see the applicable Cisco Unity
                        			 Connection integration guides at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html

Unity connection PIMG/TIMG integration supports Version 6.0,
                                 			 SU10 for Dialogic® 1000 and 2000 Media Gateway Series.

Unity Connection can also be integrated with other supported
                        			 phone systems and with multiple phone systems simultaneously. For information
                        			 on other supported phone systems, see the applicable Cisco Unity Connection
                        			 integration guides at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html .

## Licensing
               	 Requirements

In Unity Connection, the licenses for Unity Connection are
                  		managed by the Cisco Smart Software Manager (CSSM). The following are the
                  		license tags supported by Unity Connection in conjunction with the CSSM:

CUC_BasicMessaging: Allows you to use the following Unity
                        			 Connection features:

Synchronization of Unity Connection and Exchange mailboxes
                              				  (single inbox)

Calendar information for meetings

Exchange contact information

Intrasite/intersite networking

HTTPS Networking

VPIM networking

Personal call transfer rules

Users with Unity Connection mailboxes

Users with IMAP or Single Inbox access to voice messages

Recording length

Phone interface (TUI)

Mini Web Inbox

Web Inbox

Cisco Unity Connection ViewMail for Microsoft Outlook 11.5(1)
                              				  and later

IMAP email client

Cisco Mobile and Cisco Unified Mobile Communicator

Cisco Unified Messaging with IBM Lotus Sametime

Visual Voicemail

RSS readers

Cisco Unity Connection Phone View

Video Greetings and messaging

Tenant Partitioning

SAML Single Sign-On

CUC_SpeechView: Allows you to use SpeechView standard
                        			 transcription service.

CUC_SpeechConnectPort: Allows you to use Speech Connect and
                        			 voice-recognition features.

CUC_EnhancedMessaging: Allows you to use Unity Connection SRSV
                        			 feature along with Basic Messaging features.

CUC_SpeechConnectGuestUser : Allows you to specify the maximum number of local contacts, along with VPIM contacts created
                        from Non Unity Connection Server.

- CUC_BasicMessaging

- CUC_SpeechConnectPort

- CUC_EnhancedMessaging

## Requirements for Using Unified Messaging Features

The following are the supported mail servers with which you can integrate Unity Connection to enable Unified Messaging:

- Microsoft Exchange 2019 and 2016 Servers.

- Microsoft Office 365.

- Gmail Server.

Following versions of Microsoft Exchange servers are supported:

Exchange Server 2019 Cumulative Update 14 and earlier.

Exchange Server 2016 Cumulative Update 23 and earlier.

The Unified Messaging requirements are as follows.

### Unified Messaging Requirements: Synchronizing Unity Connection and supported mail servers(Single Inbox)

Microsoft Exchange 2016, 2019 servers can be integrated with Unity Connection to synchronize voice messages in Unity Connection
                           and user mailbox on Exchange servers. For more information on Unity Connection integration with Microsoft Exchange, see the
                           section Task List for Configuring Unified Messaging with Exchange 2016 or Exchange 2019 in the chapter “Configuring Unified Messaging" of Unified Messaging Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html .

Microsoft Office 365 can be integrated with Unity Connection to synchronize voice messages in Unity Connection and user mailbox
                           on Microsoft Office 365. It is a cloud hosted collaboration solution provided by Microsoft. Using Microsoft Office 365, you
                           can access emails and calendars anywhere. For more information on Unity Connection integration with Microsoft Office 365,
                           see the section Task List for Configuring Unified Messaging with Office 365 in the chapter “Configuring Unified Messaging" of Unified Messaging Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html .

Gmail server can be integrated with Unity Connection to synchronize voice messages in Unity Connection and user mailbox on
                           Gmail server. Administrative account is required for accessing Google Workspace services of Google Cloud. For more information
                           on Unity Connection integration with Gmail server, see the section Task List for Configuring Unified Messaging with Google Workspace in the chapter "Configuring Unified Messaging" of Unified Messaging Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html

Exchange servers and Active Directory domain controllers/global
                           			 catalog servers (DC/GCs) can be installed in any hardware virtualization
                           			 environment supported by Microsoft. (Cisco does not provide technical support
                           			 for message-store servers or for DC/GCs.)

The Microsoft Exchange message store can be stored in any
                           			 storage area network configuration supported by Microsoft. (Cisco does not
                           			 provide technical support for message-store servers.)

Exchange clusters are supported.

To access Exchange servers in more than one forest, you must
                           			 create at least one unified messaging service for each forest. Unity Connection
                           			 supports a maximum of 20 unified messaging services per Unity Connection
                           			 server.

Depending on the number of voice messaging ports on each Unity
                           			 Connection server, the path of connectivity must have the following guaranteed
                           			 bandwidth with no steady-state congestion:

For 50 voice messaging ports on each server—7 Mbps

For 100 voice messaging ports on each server—14 Mbps

For 150 voice messaging ports on each server—21 Mbps

For 200 voice messaging ports on each server—28 Mbps

For 250 voice messaging ports on each server—35 Mbps

The bandwidth numbers above are intended as guidelines to ensure
                     		proper operation of mailbox synchronization. For information on bandwidth
                     		requirements for Unity Connection clusters, see the Requirements
                        		  for a Unity Connection Cluster . Additional conditions such as network
                     		congestion, CPU utilization, and message size may contribute to lower
                     		throughput than expected. Call-control and call-quality requirements are in
                     		addition to the guidelines above and should be calculated using the bandwidth
                     		recommendations in the applicable Cisco Unified Communications SRND at http://www.cisco.com/en/US/solutions/ns340/ns414/ns742/ns818/landing_uc_mgr.html .

The default Unity Connection configuration is sufficient for a maximum of 2000 users and 80 milliseconds of round-trip latency
                           between Unity Connection and Exchange servers. For more than 2000 users and/or more than 80 milliseconds of latency, you can
                           change the default configuration. For more information, see the section “ Latency ” in the chapter “Single Inbox” of the Design Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html .

Users must be assigned to a class of service that is enabled for
                           			 using single inbox.

For each user configured for single inbox, an email client that
                           			 is configured to access the user’s Exchange mailbox. For full single-inbox
                           			 functionality, we recommend that you use Microsoft Outlook and install Cisco
                           			 ViewMail for Microsoft Outlook. ViewMail for Outlook is required to:

Review secure Unity Connection voice messages using Outlook.

Compose, reply to, or forward synchronized voice messages using
                                 				  Outlook.

Other email clients can be used to access Unity Connection voice
                     		messages in Exchange, but users will not have the functionality provided by
                     		ViewMail for Outlook.

For information on Unity Connection support for Outlook, see the “Requirements
                        		  for Accessing Voice Messages Using Cisco ViewMail for Microsoft
                        		  Outlook" .

For users who are configured for single inbox and SpeechView
                           			 transcriptions, the message in Exchange is not updated with the transcribed
                           			 text. You can configure Unity Connection to send a notification message that
                           			 contains the transcription.

When message expiration and single inbox are configured,
                           			 the .wav file is not deleted from the message in Exchange. Voice messages in
                           			 Unity Connection are still removed from user mailboxes and are replaced with a
                           			 recording that tells the user “This message is expired.”

Single Inbox over IPv4 and IPv6 is supported for Exchange,Microsoft Office 365 and Gmail server.

### Unified Messaging
                  	 Requirements: SpeechView Transcriptions

The SpeechView feature—which provides transcriptions of voice
                     		messages—is supported with Unity Connection.

Unity Connection integrated with a supported version of Microsoft Exchange Server.

Unity Connection integrated with Gmail server supports SpeechView feature.

Microsoft Business Productivity Online Suite is not supported.

Exchange servers and Active Directory domain controllers/global
                           			 catalog servers (DC/GCs) can be installed in any hardware virtualization
                           			 environment supported by Microsoft. (Cisco does not provide technical support
                           			 for message-store servers or for DC/GCs.)

The Microsoft Exchange message store can be stored in any
                           			 storage area network configuration supported by Microsoft. (Cisco does not
                           			 provide technical support for message-store servers.)

Exchange clusters are supported.

To access Exchange servers in more than one forest, you must
                           			 create at least one unified messaging service for each forest.

(Applicable for Releases before 15 SU2) For more information, see "SpeechView" chapter of the System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

(Applicable for Releases 15 SU2 and later) For more information, see "SpeechView Cisco Webex in-house transcription service" chapter of the System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

For Unity Connection requirements, see the Requirements for Using SpeechView Transcriptions .

### Unified Messaging
                  	 Requirements: Accessing Exchange Email Messages Using Text to Speech

Unity Connection integrated with a supported version of
                           			 Microsoft Exchange Server:

Microsoft Business Productivity Online Suite is not supported.

Microsoft Office 365 emails configured with Unity Connection are
                     		supported.

Exchange servers and Active Directory domain controllers/global
                           			 catalog servers (DC/GCs) can be installed in any hardware virtualization
                           			 environment supported by Microsoft. (Cisco does not provide technical support
                           			 for message-store servers or for DC/GCs.)

The Microsoft Exchange message store can be stored in any
                           			 storage area network configuration supported by Microsoft. (Cisco does not
                           			 provide technical support for message-store servers.)

Exchange clusters are supported.

To access Exchange servers in more than one forest, you must
                           			 create at least one unified messaging service for each forest.

The Text-to-Speech feature is supported with Exchange 2019, 2016 and 2013 over both IPv4 and IPv6. However, to access the
                                    transcripted text over IPv6, Unity Connection platform must be configured in Dual (IPv4/IPv6) mode.

For Unity Connection requirements, see the Requirements for Accessing Exchange Email Messages Using Text to Speech .

### Unified Messaging
                  	 Requirements: Accessing Calendar Information for Meetings

Unity Connection integrated with a supported application for
                     		calendar information:

When accessing Exchange calendars, Unity Connection integrated with a supported version of Microsoft Exchange Server.

Microsoft Business Productivity Online Suite is not supported.

Microsoft Office 365 calendars configured with Unity Connection
                     		are supported.

Exchange servers and Active Directory domain controllers/global
                           			 catalog servers (DC/GCs) can be installed in any hardware virtualization
                           			 environment supported by Microsoft. (Cisco does not provide technical support
                           			 for message-store servers or for DC/GCs.)

The Microsoft Exchange message store can be stored in any
                           			 storage area network configuration supported by Microsoft. (Cisco does not
                           			 provide technical support for message-store servers.)

Exchange clusters are supported.

To access Exchange servers in more than one forest, you must
                           			 create at least one unified messaging service for each forest.

Accessing calendars is supported with Exchange 2019, 2016 and 2013 over both IPv4 and IPv6. However, to access the calendars
                                    over IPv6, Unity Connection platform must be configured in Dual (IPv4/IPv6) mode.

For Unity Connection requirements, see the Requirements for Accessing Calendar Information for Meetings .

### Unified Messaging
                  	 Requirements: Accessing Exchange Contact Information

Exchange contacts can be imported into Unity Connection,
                     		allowing users to place outgoing calls using voice commands and to create
                     		personal call transfer rules based on the contact information.

Unity Connection integrated with a supported version of Microsoft Exchange Server.

Exchange servers and Active Directory domain controllers/global
                           			 catalog servers (DC/GCs) can be installed in any hardware virtualization
                           			 environment supported by Microsoft. (Cisco does not provide technical support
                           			 for message-store servers or for DC/GCs.)

The Microsoft Exchange message store can be stored in any
                           			 storage area network configuration supported by Microsoft. (Cisco does not
                           			 provide technical support for message-store servers.)

Exchange clusters are supported.

To access Exchange servers in more than one forest, you must
                           			 create at least one unified messaging service for each forest.

Microsoft Office 365 contacts configured with Unity Connection
                           			 are supported.

Accessing contacts is supported with Exchange servers over both IPv4 and IPv6. However, to access the contacts over IPv6,
                                    Unity Connection platform must be configured in Dual (IPv4/IPv6) mode.

For Unity Connection requirements, see the Requirements for Accessing Exchange Contact Information .

## Requirements for
               	 Using Video Messaging

Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                              feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html .

Unity Connection must be integrated with supported version of
                        			 Cisco MediaSense Primary node. Cisco MediaSense cluster is not supported.

Unity Connection users must be assigned a class of service with
                        			 video parameters enabled.

Unity Connection is configured in IPv4 mode only.

Unity Connection supports the following codecs in a video call

H.264 video codec

G.711ulaw audio codec

Video messaging and video greetings are supported only over SIP
                        			 Integration with Cisco Unified Communications Manager.

The Primary DNS server should not have a response delay of more
                        			 than 500 milliseconds.

The MediaSense
                        			 server must be co-located with Unity Connection server with 1Gbps connectivity
                        			 between the servers and less than 10ms Round Trip Time (RTT) latency.

## Requirements for
               	 Using Voice-Recognition Features

You must have required licenses on Cisco Smart Software Manager
                        			 (CSSM).

Users must be assigned to a class of service enabled for using
                        			 voice recognition.

Phone systems must be configured to send calls to Unity
                        			 Connection in any of the supported audio codecs except G729a. The G.729a audio
                        			 codec is not supported with the voice-recognition features.

Remote Message Monitor is only supported if all end points
                                 			 (incoming, Unity, and outgoing) are using the same codec.

## Requirements for
               	 Using SpeechView Transcriptions

The SpeechView feature—which provides transcriptions of voice
                  		messages—is supported with Unity Connection.

Unity Connection must be registered with Cisco Smart Software Manager(CSSM) or Cisco Smart Software Manager satellite and
                        must have aquired proper licenses to use SpeechView service.

(Applicable to 15 SU2 and later releases) Unity Connection server must be onboarded on Cisco Webex Cloud-Connected UC.

"SpeechView Voicemail Transcript" service must be enabled on the Service Management Page of Cisco Webex Cloud-Connected UC.

"SpeechView Voicemail Transcript" service option will only be visible on Cisco Webex Cloud-Connected UC when Unity Connection
                                    server is running on Release 15 SU2 or later.

Users must be assigned to a class of service enabled for using SpeechView transcriptions of voice messages.

Make sure that Domain Name Server (DNS) is configured on Unity Connection as SpeechView Cisco Webex in-house transcription
                              service is not supported with only IP address configuration of Unity Connection.

For Unity Connection speechview transcription requirements, see
                  		the Unified Messaging Requirements: SpeechView Transcriptions

## Requirements for
               	 Accessing the Unity Connection Web Tools through Cisco PCA

Messaging Assistant web
                     		  tool

Users must be assigned to a class of service enabled for using
                        			 the Messaging Assistant.

A supported operating system and web browser(s) on user
                        			 workstations. See Compatibility Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

Web Inbox web tool

Users must be assigned to a class of service enabled for using
                        			 the Web Inbox and RSS feeds.

A supported operating system and web browser(s) on user
                        			 workstations. See Compatibility Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

### Personal Call
                     		  Transfer Rules web tool

Unity
                           				Connection must be integrated with a supported version of the Cisco Unified
                           				Communications Manager phone system. (Cisco Unified Communications Manager
                           				Express is not supported.)

Users must be
                           				assigned to a class of service enabled for using the Personal Call Transfer
                           				Rules web tool.

A supported
                           				operating system and web browser(s) on user workstations. See Compatibility
                           				Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

Cisco Personal Communications Assistant (CPCA) is now supported
                                    				both over IPv4 and IPv6. However, to access Cisco PCA over IPv6, Unity
                                    				Connection platform must be configured in Dual (IPv4/IPv6) mode.

## Requirements for
               	 Accessing Voice Messages Using Web Inbox

Users must be assigned to a class of service enabled for using
                        			 the Web Inbox and RSS feeds.

A supported operating system and web browser(s) on user
                        			 workstations. See Compatibility Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

Web Inbox is now supported over both IPv4 and IPv6. However, to
                                    				access Web Inbox over IPv6, Unity Connection platform must be configured in
                                    				Dual (IPv4/IPv6) mode.

Caveats:

The Internet
                        			 Explorer does not support playback functionality for voice messages using Web
                        			 Inbox.

## Requirements for
               	 Accessing Voice Messages Using Mini Web Inbox

Make sure the trusted certificate of the certification authority is added to the Trusted Root Store on the user workstations
                        in order to access the notifications via email and the voice message via Mini Web Inbox. For more information on how to configure
                        the trusted certificate on Unity Connection, see the section “ Securing Unity Connection Administration, Cisco PCA, Unity Connection SRSV, and IMAP Client Access to Unity Connection ” of chapter “Using SSL to Secure Client/ Server Connections” of Security Guide for Cisco Unity Connection, Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx.html .

Make sure to perform the steps to configure the HTML notification on user workstation. For more information on how to configure
                        the HTML notifications, see the section “ Configuring Unity Connection for HTML Based Message Notification ” of the chapter “Configuring an Email Account to Access Cisco Unity Connection Voice Messages” of User Workstation Setup Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user_setup/guide/b_15cucuwsx.html .

Make sure to perform the steps to configure the Mini Web Inbox on user workstation. For more information on how to configure
                        the Mini Web Inbox, see the “Configuring Unity Connection for Mini Web Inbox” section of the “Configuring an Email Account
                        to Access Cisco Unity Connection Voice Messages” chapter of the User Workstation Setup Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user_setup/guide/b_15cucuwsx.html .

Audio Playback on Computer

Mozilla Firefox plays voice messages on Mini Web Inbox using
                              				  HTML 5 Audio (.wav format).

Audio Recording on Computer

Caveats:

On MAC OS - The recording on MAC OS is supported by telephone
                        			 record and playback functionality only, computer based recording is not
                        			 supported.

For supported operating system and web browser(s) on user
                  		workstations, see Compatibility Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html

Mini Web Inbox is supported over both IPv4 and IPv6. However, to
                           		access Mini Web Inbox over IPv6, Unity Connection platform must be configured
                           		in Dual (IPv4/IPv6) mode.

## Requirements for
               	 Accessing Voice Messages Using Cisco Unity Connection ViewMail for Microsoft
               	 Outlook

IMAP users only: Users must be assigned to a class of
                        			 service that is enabled for accessing voice messages using an IMAP client.

IMAP users only: Users must have email accounts in Outlook
                        			 configured to access Unity Connection voice messages.

Single-inbox users only: Users must have Exchange email
                        			 accounts in Outlook pointing to their Exchange mailboxes.

A ViewMail for Outlook version supported for use with the
                        			 Outlook version and operating system on user workstations. See Requirements for Accessing Unity Connection Voice Messages Using an IMAP Email Client .

For workstation and other software-related requirements, and for
                  		installation and upgrade information, see Release Notes for Cisco ViewMail for
                  		Microsoft Outlook at http://www.cisco.com/en/US/products/ps6509/prod_release_notes_list.html .

Cisco Unity Connection ViewMail for Microsoft Outlook supports the single sign-on functionality.

Cisco Unity Connection ViewMail for Microsoft Outlook (VMO) is supported over both IPv4 and IPv6. However, to access voice
                           messages using IMAP clients over IPv6, Unity Connection platform must be configured in Dual (IPv4/IPv6) mode.

## Requirements for
               	 Accessing Unity Connection Voice Messages Using an IMAP Email Client

Users must be assigned to a class of service that is enabled for
                        			 accessing voice messages using an IMAP client.

A supported IMAP email client on user workstations. See
                        			 Compatibility Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

Sound card, speakers, and media player on user workstations.

Accessing Unity Connection voice messages using IMAP clients is
                                 			 now supported over both IPv4 and IPv6. However, to access voice messages using
                                 			 IMAP clients over IPv6, Unity Connection platform must be configured in Dual
                                 			 (IPv4/IPv6) mode.

## Requirements for
               	 Accessing Unity Connection Voice Messages Using Cisco Unified Personal
               	 Communicator

Users must be assigned to a class of service that is enabled for
                        			 accessing voice messages using a unified client.

A supported version of Cisco Unified Personal Communicator on
                        			 user workstations. See Compatibility Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

For workstation, system, and other software-related
                  		requirements, see the applicable Release Notes for Cisco Unified Personal Communicator at http://www.cisco.com/c/en/us/support/unified-communications/unified-personal-communicator/products-release-notes-list.html .

Cisco Unified Personal Communicator 8.x support secure messaging
                        			 with Unity Connection.

Cisco Unified Personal Communicator versions 8.0 and later
                        			 support IMAP IDLE.

## Requirements for
               	 Accessing Cisco Jabber

Unity Connection supports Cisco Jabber 12.0(1) and later as client.

For more information on Cisco Jabber with operating systems, see the windows release notes at https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/tsd-products-support-series-home.html .

and for Macintosh, see the release notes at https://www.cisco.com/c/en/us/support/unified-communications/jabber-mac/tsd-products-support-series-home.html .

## Requirements for Accessing Cisco Webex

Unity Connection supports Cisco Webex as client.

For more information on Cisco Webex with operating systems, see the windows release notes at https://help.webex.com/en-us/mqkve8/Webex-Release-Notes

and for Macintosh, see the release notes at https://help.webex.com/en-us/mqkve8/Webex-Release-Notes#sprk_2022796 .

## Requirements for Accessing Unity Connection Voice Messages Using
               	 Visual VoiceMail

This section contains the following information:

- A supported Cisco Unified IP
                     		  Phone model. (See the “Cisco Unified IP Phone Requirements” section under
                     		  “System Requirements” in the Release Notes for Visual Voicemail .)

For server and phone firmware requirements, and
                  		other information about using Visual Voicemail, see the applicable Release
                  		Notes for Visual Voicemail at http://www.cisco.com/en/US/products/ps9929/prod_release_notes_list.html .

## Requirements for Accessing Unity Connection Voice Messages Using RSS
               	 Readers

Users must be assigned to a class of service
                        			 enabled for using the Messaging Inbox and RSS feeds.

Sound card, speakers, and media player on user
                        			 workstations.

RSS feeds is now supported over both IPv4 and IPv6.
                                 			 However, to access RSS feeds over IPv6, Unity Connection platform must be
                                 			 configured in Dual (IPv4/IPv6) mode.

## Requirements for
               	 Accessing Exchange Email Messages Using Text to Speech

Unity Connection integrated with a supported version of
                           				Microsoft Exchange Server:

Exchange server(s) in a supported Windows domain configuration. Table 2 lists the supported configurations.

Exchange Configuration

Supported Windows Domain Configurations

One server running Exchange Server 2019

Exchange server is a Windows Server 2008, or 2012 domain
                                       						  controller/global catalog server.

Exchange server is a Windows Server 2008, or 2012 member server.

One server running Exchange Server 2016

Exchange server is a Windows Server 2008, or 2012 domain controller/global catalog server.

Exchange server is a Windows Server 2008, or 2012 member server.

The Unity Connection server and the Exchange server(s) must be
                           				located in the same local-area network.

For Unity Connection requirements, see the Unified Messaging Requirements: Accessing Exchange Email Messages Using Text to Speech .

Text-to-speech over Exchange servers is now supported over both IPv4 and IPv6. However, to access Text-to-speech over IPv6,
                              Unity Connection platform must be configured in Dual (IPv4/IPv6) mode.

## Requirements for
               	 Accessing Calendar Information for Meetings

Unity Connection integrated with a supported application for
                  		calendar information:

For Unity Connection requirements, see the “Unified
                     		  Messaging Requirements: Accessing Calendar Information for Meetings” section on
                     		  page 10 .

Accessing calendars is supported with Exchange servers over both IPv4 and IPv6. However, to access the calendars over IPv6,
                           Unity Connection platform must be configured in Dual (IPv4/IPv6) mode.

## Requirements for
               	 Accessing Exchange Contact Information

Exchange contacts can be imported into Unity Connection,
                  		allowing users to place outgoing calls using voice commands and to create
                  		personal call transfer rules based on the contact information.

Unity Connection integrated with a supported version of Microsoft Exchange Server is required.

For Unity Connection 11.x requirements, see the Unified Messaging Requirements: Accessing Exchange Contact Information .

Accessing contacts is supported with Exchange over both IPv4 and IPv6. However, to access the contacts over IPv6, Unity Connection
                           platform must be configured in Dual (IPv4/IPv6) mode.

## Requirements for
               	 Unity Connection Phone View

Unity Connection
                        			 integrated with a supported version of the Cisco Unified Communications Manager
                        			 phone system. For supported versions, see the Compatibility Matrix for
                        			 Cisco Unity Connection depending on the integration type at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

A supported Cisco Unified IP Phone model, with the supported Cisco Unified Communications Manager version firmware installed.
                        Supported IP Phone models are 8865, 8845, 7821.

Note: Phone models that have reached EOL status are no longer supported.

## Requirements for URI Dialing

Unity Connection must be integrated with the URI dialing supported version of Cisco Unified Communications Manager.

Unity Connection supports URI Dialing over SIP Integration with Cisco Unified Communications Manager.

Configure URI supported IP Phones (89xx or 99xx series) or Jabber/Webex using Cisco Unified Presence Server and CUCM, in order
                        to dial via URI directly.

## Requirements for a Cisco Fax Server Integration

Cisco Fax Server version 10.x (available from
                        			 Cisco until May 2011)

OpenText Fax Server, RightFax Edition, version
                        			 10.x and later.

Sagemcom Xmedius Fax SP version 6.5.5.

Cisco will no longer be selling Cisco Fax Server
                                 			 version 10.x after May 2011; however, support for Cisco Fax Server will
                                 			 continue until May 2014. For detailed information on end-of-sale and end-of
                                 			 life dates for the Cisco Fax Server, see the information at http://www.cisco.com/c/en/us/products/collateral/unified-communications/unity/end_of_life_notice_c51-630608.html .

## Requirements for
               	 an LDAP Directory Integration

The last column in the table indicates whether an LDAP directory supports specifying additional LDAP directory servers to
                           act as backup in case the LDAP directory servers that Unity Connection accesses for synchronization and for authentication
                           become unavailable.

Microsoft Active Directory 2019 Lightweight Directory Services

Yes

Microsoft Active Directory 2019

Yes

Microsoft Active Directory 2016

Yes

When you are
                           				using Active Directory, you can integrate a single Unity Connection server with
                           				more than one user search base, but all user search bases must be in the same
                           				Active Directory forest. To integrate Unity Connection with more than one
                           				forest, you must install one digitally networked Unity Connection server per
                           				forest .

When you are configuring Unity Connection for Microsoft Active
                           				Directory 2008 Lightweight Directory Services, choose the “Microsoft Active
                           				Directory Application Mode” option in Cisco Unity Connection Administration.

When you are configuring Unity Connection for Novell e-Directory
                           				Services, choose the "Sun iPlanet or other OpenLDAP directory server
                           				Application Mode" option in Cisco Unity Connection Administration.

When you are
                           				using a Sun iPlanet or ONE directory server, you can integrate a single Unity
                           				Connection server with more than one user search base, but all user search
                           				bases must be in the same tree. To integrate Unity Connection with more than
                           				one tree, you must install one digitally networked Unity Connection server per
                           				tree.

## Requirements for a Unity Connection Cluster

If your system is configured for a Unity
                  		Connection cluster, consider how the requirements varies in the following
                  		scenarios.

### Cluster
                  	 Requirements When Both Servers are Installed in the Same Building or
                  	 Site

- Both servers must meet specifications according to the Cisco Unity Connection 15 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

- For a cluster with two
                        		  virtual machines, both must have the same virtual platform overlay.

- Both Unity Connection
                        		  servers must be collocated.

- Both Unity Connection
                        		  servers must be located in the same local-area network.

- Both Unity Connection
                        		  servers must have a minimum 100 Mbps Unity Connection to the network.

- The maximum round-trip
                        		  latency must be no more than 5 ms.

- The Unity Connection
                              				servers are assigned a common DNS name with the publisher server first.

- All user client and
                              				administrator sessions connect to the publisher server. If the publisher server
                              				stops functioning, the user client and administrator sessions must connect to
                              				the subscriber server.

- Phone systems must attempt
                              				to route incoming calls to the subscriber server. If no voice messaging ports
                              				are available to answer calls on the subscriber server, the phone systems must
                              				route calls to the publisher server.

- The Unity Connection
                        		  servers must not be separated by a firewall.

- Both Unity Connection
                        		  servers must have the same software and engineering-special versions installed.

- Both Unity Connection
                        		  servers must have the same enabled features and configurations.

- Both Unity Connection
                        		  servers must connect to the same phone system(s).

- If the Unity Connection
                        		  servers contain dual NICs, the two NICs on each Unity Connection server must be
                        		  configured for fault tolerance using a single IP address, or one of the NICs
                        		  must be disabled. Configuring the two NICs with distinct IP addresses for
                        		  network load balancing is not supported.

- For selected servers supported for earlier versions of Unity Connection, a memory upgrade. To determine whether your server
                        requires a memory upgrade, see the applicable server-specific table in the Cisco Unity Connection 15 Supported Platforms List .

The Unity Connection cluster feature is not supported for use with  SAML SSO.

### Cluster
                  	 Requirements When Both Servers are in Separate Buildings or Sites

- Both servers must meet specifications according to the Cisco Unity Connection 15 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

- For a cluster with two
                        		  virtual machines, both must have the same virtual platform overlay.

- For 50 voice messaging
                              				ports on each server—7 Mbps

- For 100 voice messaging
                              				ports on each server—14 Mbps

- For 150 voice messaging
                              				ports on each server—21 Mbps

- For 200 voice messaging
                              				ports on each server—28 Mbps

- For 250 voice messaging
                              				ports on each server—35 Mbps

The bandwidth
                              		numbers above are intended as guidelines to ensure proper operation of an
                              		active-active cluster with respect to synchronization traffic between the two
                              		servers. Additional conditions such as network congestion, CPU utilization, and
                              		message size may contribute to lower throughput than expected. Call-control and
                              		call-quality requirements are in addition to the guidelines above and should be
                              		calculated using the bandwidth recommendations in the applicable Cisco Unified Communications SRND at http://www.cisco.com/c/en/us/solutions/enterprise/unified-communication-system/index.html .

- When both the subscriber
                        		  and publisher are taking calls, the maximum round-trip latency must be no more
                        		  than 100 ms. When only the publisher is taking calls, subscriber is idle but
                        		  replicating with publisher, the maximum round-trip latency must be no more than
                        		  150 ms.

- The Unity Connection servers are assigned a common DNS name with the publisher server first.

- All user clients like Jabber, WebInbox etc and administrator sessions connect to the publisher server. If the publisher server
                              stops functioning, the user client and administrator sessions must connect to the subscriber server.

Caution

If failover happens and publisher node of Unity Connection cluster is not completely down then subscriber node will become
                                          primary node and user clients (Jabber,Web Inbox etc..) will still connect to publisher node.However, users may experience
                                          delay in accessing the voicemail through clients. In this case administrator should configure the RTMT alerts "AutoFailbackInitiated
                                          and AutoFailbackSucceeded" to troubleshoot failover. For more information on configuration of these alarms refer Alarm Message
                                          Definitions for Cisco Unity Connection Release 15 guide available at link https://www.cisco.com/c/td-xml/en_us/voice-ip-comm/connections/15/alarm_messages/15cucalrmmsgdef.html . In order to experience seamless voicemail access experience through user clients(Jabber, Web Inbox etc.. ) for Cisco Unity
                                          Connection failover scenario as mentioned above, it is recommended to either deploy the Unity Connection Cluster with maximum
                                          round-trip latency for not more than 5ms when both servers are in separate buildings or sites. Or customer should plan to
                                          install both servers in same building or sites. For more information, see section “ Cluster Requirements When Both Servers are Installed in the Same Building or Site " of System Requirements for Cisco Unity Connection Release 15 guide.

- Phone systems must attempt to route incoming calls to the subscriber server. If no voice messaging ports are available to
                              answer calls on the subscriber server, the phone systems must route calls to the publisher server.

- The TCP and UDP ports of the firewall must be open as listed in the IP Communications Required by Cisco Unity connection chapter of the Security Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx.html .

- Both Unity Connection
                        		  servers must have the same software and engineering-special versions installed.

- Both Unity Connection
                        		  servers must have the same enabled features and configurations.

- Both Unity Connection
                        		  servers must be configured to be in the same time zone.

- Both Unity Connection
                        		  servers must connect to the same phone system(s).

- If the Unity Connection
                        		  servers contain dual NICs, the two NICs on each Unity Connection server must be
                        		  configured for fault tolerance using a single IP address, or one of the NICs
                        		  must be disabled. Configuring the two NICs with distinct IP addresses for
                        		  network load balancing is not supported.

- For selected servers supported for earlier versions of Unity Connection, a memory upgrade or replacement of hard disks. To
                        determine whether your server requires a memory upgrade or replacement of hard disks, see the applicable server-specific table
                        in the Cisco Unity Connection 15 Supported Platforms List .

The Unity
                              		Connection cluster feature is not supported for use with the SAML SSO feature.

## Requirements for Unity Connection Networking

Unity Connection servers can be joined through intrasite networking to
                  		form a single site (known as a Digital Network). you may add upto a maximum of
                  		ten Untiy Connection server or cluster per site. In addition, two Unity
                  		Connection sites can be linked together through intersite networking for a
                  		total of up to 20 Unity Connection servers sharing the same directory
                  		information

Alternatively, you can use intersite networking to link a single Unity
                  		Connection site of up to ten servers with a single Cisco Unity server or
                  		Digital Network. (In a Unity Connection cluster, only the publisher server is
                  		joined to the network, so a cluster counts as a single server toward the limit
                  		of ten in each site.)

HTTPS networking can be used to link up to 25
                  		Unity Connection servers or clusters in a single site network, referred to as
                  		HTTPS Unity Connection network.

### Requirements for
                  	 Intrasite Networking

Intrasite networking
                     		uses SMTP to provide directory synchronization and message networking among
                     		Unity Connection servers.

Unity Connection version 11.x and version 12.x servers can coexist in the same site as long as each server meets all the applicable
                     requirements in the System Requirements for Cisco Unity Connection Guide.

Intrasite networking
                     		has the following requirements:

- Each version 12.x server in
                        		  the site must meet all applicable requirements listed in this document.

- Each server in the site
                        		  must be able to access the other servers in the site directly through TCP/IP
                        		  port 25 (SMTP), or SMTP messages must be routed among the servers through an
                        		  SMTP smart host.

- If your site includes one
                        		  or more Unity Connection clusters, you must have a smart host available to
                        		  resolve the SMTP domain of the cluster to both the publisher and subscriber
                        		  servers in order for message traffic to reach the cluster subscriber server in
                        		  the event that the publisher server is down.

SAML SSO feature is not supported to access all the nodes of Intrasite networking. Only a local administrator can configure
                                    the Intrasite networking in Unity Connection..

### Requirements for
                  	 Intersite Networking

You can use intersite networking to link one Unity Connection site to another Unity Connection site. You can also use it to
                     link a Unity Connection site to a Cisco Unity server or Cisco Unity Digital Network. The linked sites are called a Cisco Voicemail
                     Organization.

Intersite networking
                     		has the following requirements:

- Each Unity Connection server or cluster in the Cisco Voicemail Organization must be at version 15 and must meet all applicable
                        requirements listed in this document.

- Each Unity Connection site
                        		  must meet the requirements listed in the Requirements
                           			 for Intersite Networking .

For more information on virtual servers and the specifications on the memory that must be added, see the Cisco Unity Connection 15 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

- The virtual directory created by the networked sites must not exceed the maximum total numbers of objects listed in Table 4
                        in the “Directory Object Limits for Unity Connection” .

- Intersite networking can be
                        		  used to link a maximum of two sites. (Adding more than one intersite link per
                        		  site is not supported.)

SAML SSO feature
                              		is not supported to access all the nodes of Intersite networking. Only a local
                              		administrator can configure the Intersite networking in Unity Connection.

### Requirements for
                  	 HTTPS Networking

You can use HTTPS networking to link one or more Unity
                     		Connection servers or clusters to form a well-connected network based on
                     		hub-spoke topology. The servers that are joined together in the network are
                     		referred as locations (Unity Connection cluster counts as one location in the
                     		network). Within a network, each location uses HTTP or HTTPS to exchange
                     		directory information and SMTP to exchange voice messages with each other.

HTTPS networking has the following requirements:

Each Unity Connection server or cluster in the HTTPS network
                           			 must be at version 10.x or later, and must meet all applicable requirements
                           			 listed in this document.

Each server in the network must be IP addressable and able to
                           			 exchange directory information using HTTP on port 8081 or HTTPS on port 8444.

The servers in the network must be able to route SMTP messages
                           			 to the other servers in the network directly through TCP/IP port 25 or through
                           			 an SMTP smart host.

If your network includes one or more Unity Connection clusters,
                           			 you must have a smart host available to resolve the SMTP domain of the cluster
                           			 to both the publisher and subscriber servers, which helps divert message
                           			 traffic to the subscriber server when the publisher server is down.

The virtual directory created by the networked Unity Connection servers must not exceed the maximum numbers of objects listed
                           in Table 5 and Table 6 in the “Directory Object Limits for Unity Connection” section.

HTTPS networking can be used to link a maximum of 25 Unity
                           			 Connection locations.

HTTPS networking supports single site network only. (Connecting
                           			 multiple Unity Connection sites in a network is not supported.)

HTTPS networking is not supported with intrasite or intersite
                           			 networking.

HTTPS networking is not supported for use with Cisco Business
                                    			 Edition version 3000. Before using HTTPS networking, ensure that directory
                                    			 replication takes place properly in Intrasite or Intersite Networking. Also,
                                    			 the Unity Connection servers should be using appropriate OVA as per topology
                                    			 and directory size.

SAML SSO
                                    			 feature is not supported to access all the nodes of HTTPS networking. Only a
                                    			 local administrator can configure the HTTPS networking in Unity Connection.

## Requirements for
               	 Using Security Assertion Markup Language Single Sign-On (SAML SSO)

SAML SSO allows a user to gain single sign-on access with Unity
                  		Connection subscriber web interfaces and across the administrative web
                  		applications on the following Unified Communication products:

Cisco Unity Connection

Cisco Unified Communications Manager

Cisco Unified IM/Presence

Cisco Unified Communications OS Administration

Disaster Recovery System

For more information on accessing web application pages through SAML SSO, see the Quick Start Guide for SAML SSO in Cisco Unity
                  Connection , Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/quick_start/guide/b_15cucqssamlsso.html .

The SAML SSO feature requires the following third party
                  		applications:

LDAP Directory.

The Identity Provider authenticates an end user and returns SAML assertions. SAML Assertion shows either Yes (authenticated)
                        or No (authentication fails) response. When an end user enters the username and password, the user credentials authenticates
                        on Identity Provider. This further gives access to web applications on the Unity Connection server.

For information on currently supported Identity Providers, see "SAML-Based SSO Solution" chapter of SAML SSO Deployment Guide for Cisco Unified Communications Applications available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

To enable the SAML SSO feature from Cisco Unity Connection
                        			 Administration, make sure you have at least one LDAP user in Unity Connection
                        			 with administrator rights.

Unity Connection supports SAML 2.0 protocol for the SAML SSO
                                 			 feature.

The third party products mentioned above must meet the following
                  		configuration requirements:

Active directory domain controllers/global catalog servers and
                        			 Active Directory Federated Services (ADFS) can be installed in any hardware
                        			 virtualization environment supported by Microsoft. (Cisco does not provide
                        			 technical support for DC/ GCs or ADFS that acts as an Identity Provider).

The Identity Provider that you are using must be accessible by
                        			 its hostname on the network to all the client systems like Unity Connection.

The clocks of all entities participating in SAML SSO must be
                        			 synchronized.

See the third-party product documentation for more information
                  		about the above products.

Make
                           		sure that Domain Name Server (DNS) is configured on Unity Connection as SAML
                           		SSO is not supported with only IP address configuration of Unity Connection.

All web browsers that are currently supported with Unity Connection 15, allows SAML SSO access to web client applications.

## Requirements for
               	 VPIM Networking

Unity Connection supports Voice Profile for Internet Mail (VPIM)
                  		version 2 that allows the exchange of voice and text messages with other
                  		messaging systems.

VPIM Networking can be used to provide message networking
                  		between Unity Connection and the following messaging systems:

Unity Connection 15,14,12.x, 11.x and 10.x.

Third-party voice messaging systems that support the VPIM
                        			 version 2 protocol, as defined in Internet RFC 3801.

For information on using VPIM in Unity Connection Unity Connection in Cisco Business Edition, see the “ VPIM Networking ” chapter of the Networking Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html .

## Requirements for Using a Provisioning Application

A supported provisioning application:

Unimax Second Nature version 6.8 B0 and later.

Any technical support or troubleshooting required on the provisioning software must be obtained from the manufacturer. Cisco
                  is responsible for providing technical support only on the Unity Connection application.

## Requirements for Migrating from Unity Connection 10.x to Version 15

During the
                  		migration, only user data and, optionally, voice messages are preserved.
                  		System-level configuration data (for example, templates and classes of service)
                  		must be manually configured.

Caution

Requirements for Unity Connection 15 are different from requirements for Unity Connection 10.x. The system must meet Unity
                           Connection 15 requirements to receive support from Cisco TAC.

A migration from Unity Connection version 10.x to 15 has the following requirements:

- All applicable requirements
                     		  listed in this document.

- A server that is supported for use with Unity Connection and that meets Unity Connection 15 specifications, particularly regarding
                     memory and processor speed. For information on supported Unity Connection servers, including specifications on individual
                     servers, see the Cisco Unity Connection 15 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

With Cisco Unity Connection release 15 and later, direct upgrade from versions 10.5, 11.5 to 15 is not supported. To upgrade
                              from version 10.5 to 15 or from version 11.5 to 15, you must follow an intermediate upgrade path such as going from 10.5 to
                              12.5 or later and then from 12.5 or later to 15.

Caution

If you try to install version 15 on an unsupported platform, Unity Connection will not be displayed as an option in the Product
                           Deployment Selection window of the installation program.

## Requirements for
               	 Installing Unity Connection on a Virtual Machine

For information on installing other Cisco Unified Communications applications on the same physical server on which Unity Connection
                  is installed, see the Unified Communications Virtualization wiki at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unity-connection.html .

- If you are running Unity Connection on a physical server and want to migrate over to Unity Connection 15, then it is required
                     to migrate from a physical server to a virtual server since the physical Unity Connection server is not supported for use
                     with Unity Connection 15.

Unity Connection 15 supports ESXi version of 7.0 U3 or 8.0 U1 with minimum VM Hardware version of 17.

- For VMware configurations
                        			 supporting 300GB and 500GB vDisks: The datastore where the Unity Connection
                     		  virtual machine will reside must be formatted with a VMware VMFS block size
                     		  large enough to allow for the intended size of the virtual hard disk for the
                     		  Unity Connection virtual machine. For example, a block size of 1MB limits the
                     		  maximum virtual hard disk size to 256GB. A block size of 2MB allows 512GB
                     		  virtual disks.

- Unity Connection 8.0(2) and later can be run on specification based hardware from Cisco, HP and IBM. However, some restrictions
                     are applied. See http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html for more information.

- The support for the Input/Output devices on the servers that are running Unity Connection as a virtual appliance has been
                     enhanced to include FCoE and Cisco Converged Network adapters. See http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html for more information.

- Unity Connection 8.0(2) and later now support FC, FCOE, iSCSI, and NFS SAN environments with some restrictions. See http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-collaboration-storage-design-requirements.html for more information.

- For list of VMware features that are supported for Unity Connection, see http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-collaboration-storage-design-requirements.html .

- Accessing a USB key is not
                     		  supported.

- Oversubscribing processors
                     		  and memory is not supported.

- For VMware vSphere ESXi 7.0 and later, Latency Sensitivity function is included to reduce virtual machine latency. When the
                     Latency Sensitivity value is set to high you do not need to leave any unused processor core for the ESXi hypervisor / scheduler.

- All virtual disks assigned
                     		  to the Unity Connection virtual machine must be configured in
                     		  independent-persistent mode, which provides the best storage performance.

- A network time protocol
                     		  (NTP) server must be accessible to the Unity Connection server.

- When configuring a Unity
                     		  Connection cluster, you can install Unity Connection on one physical server and
                     		  one virtual machine, or on two virtual machines, but the two virtual machines
                     		  must be on separate physical hosts. When using blades as hosts, we recommend
                     		  that the blades be on separate chassis.

- If the hyper-threading
                     		  feature is available on the CPU, you should enable the feature to create
                     		  logical cores. However, the logical cores do not change the Unity Connection
                     		  rule that is based on 1:1 mapping of physical cores to vcpu not the logical
                     		  cores to vcpu.

## Directory Object
               	 Limits for Unity Connection

This section
                     		  contains two tables that list directory object limits.

Table 4 lists the maximum numbers of certain objects that can be created on a Unity Connection server. For these objects, the limits
                     apply regardless of the platform overlay in use by the server.

If you are using legacy (intrasite or intersite networking) or HTTPS networking to link Unity Connection servers, the limits
                     in Table 4 apply to each Unity Connection server in the site or organization.

Table 4 applies to the virtual directory created by the networked Unity Connection servers. When Unity Connection servers
                     are networked together using intrasite networking, replication between locations creates the virtual directory consisting
                     of the users, administrator-defined contacts, system distribution lists, partitions, search spaces, and VPIM locations that
                     are homed on each location, along with data about the locations themselves. When servers are networked together using intersite
                     networking, the virtual directory for an individual server consists of all users from both sites plus the administrator-defined
                     contacts local to the site to which the server belongs, along with the system distribution lists, partitions, and search spaces
                     on both sites, plus the VPIM locations on the local site.

Table 5 and Table 6 apply to the virtual directory created by the Unity Connection servers connected in an HTTPS network. When Unity Connection
                     servers are linked together using HTTPS networking, replication between locations creates the virtual directory consisting
                     of the users, administrator-defined contacts, system distribution lists, partitions, search spaces, VPIM locations, and VPIM
                     contacts homed on each location along with the data about the locations themselves. The directory object limits for other
                     objects that depend on the platform overlay are listed in the Cisco Unity Connection 15 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

Directory Object

Unity Connection Limit

Classes of service

3.000

Call handlers

40,000

Call routing rules

1,200

Mailbox stores

5

Search spaces

2000

Partitions

2000

VPIM locations

100

The limits in Table 4 apply to the entire site or Cisco Voicemail Organization, regardless of whether the network comprises
                     only two locations or the maximum number of supported locations. (For example, in Unity Connection version 12.x, if the individual
                     server platforms support the limits, you can have 10 locations in one site with 10,000 Unity Connection users each, or 20
                     locations in two sites with 5,000 Unity Connection users each.)

The limits in Table 5 apply to the entire network assuming that the locations use virtual platform overlay supporting 20,000 users.

Directory Object

Unity Connection Limit

Connection locations

25 1

VPIM locations

100

System distribution lists

100,000

Members per system distribution list

25,000

Total number of distribution list members across all system
                                 					 distribution lists

1.5 million

Nested lists within a distribution list

20

Partitions

10,000*

1 The limits of Unity Connection locations that can be connected in an HTTPS network differ as per their platform specifications
                        mentioned in Table 6

- Searching for Search
                                    				Spaces in the System Administration slows down

- Modifying and saving
                                    				search spaces can take over 6 minutes.

- Changing/ Saving/ Reordering Search spaces can take upto 20 mins to replicate across the site.

Table 6 lists the maximum number of certain objects in HTTPS network supported with different platform overlays. The limits mentioned
                     in the table apply to the network assuming that all the Unity Connection locations in the network are of same platform overlay.

Virtual

Platform Overlay for

up to 1,000

Users

Virtual Platform Overlay for up to 5,000 Users

Virtual Platform Overlay for up to 10,000 Users

Virtual Platform Overlay for up to 20,000 Users

Connection locations in the network

3

10

10

25

HTTPS links Note

1

3

3

5

Unity Connection local users

1000

5000

10,000

20,000

Remote users

9000

35,000

40,000

80,000

Contacts (administrator-defined and VPIM contacts)

-

20,000

30,000

150,000

Maximum Unity Connection locations supported in HTTPS network are determined based on the following criteria:

Depth of HTTPS network can reach up to second level.

Servers used in the network are of same virtual platform overlay.

HTTPS links supported at each location are same as mentioned in Table 6 .

Maximum of 25 locations can be connected in the network.

For example, if an HTTPS network is created with only 2vCPU
                     		  servers and each location supports a maximum of 3 HTTPS links then up to 10
                     		  locations can be connected in the network. Similarly, the number of Unity
                     		  Connection locations supported in an HTTPS network is calculated for other
                     		  virtual platform overlays used by the servers.

The number of locations that can be connected in an HTTPS
                                       				  Network is governed by the highest platform overlay used in the network.

The directory size depends upon the lowest platform overlay used
                                       				  in the network.

## Available
               	 Languages for Unity Connection Components

Languages are not licensed, and Unity Connection does not enforce a limit on the number of languages you can install and use.
                           However, the more languages you install, the less hard-disk space is available for storing voice messages. In the Cisco Unity Connection 14 Supported Platforms List available at link https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html , information on the number of minutes of storage available on each server assumes that you have installed no more than five
                           languages.

This section lists the languages in which Unity Connection
                  		components are available.

Cisco Personal
                     		  Communications Assistant (PCA)

Arabic-Saudi Arabia, Catalan, Chinese-Hong Kong, Chinese-PRC,
                  		Chinese-Taiwan, Czech, Danish, Dutch-Netherlands, English-United States,
                  		Finnish, French-Canada, French-France, German, Greek, Hebrew, Hungarian,
                  		Italian, Japanese, Korean, Norwegian, Polish, Portuguese-Brazil,
                  		Portuguese-Europe, Russian, Spanish-Latin America, Spanish-Spain, Swedish,
                  		Turkish

Cisco Personal
                     		  Communications Assistant (PCA) Help

Arabic-Saudi Arabia, Chinese-PRC, Chinese-Taiwan, Czech, Danish,
                  		Dutch-Netherlands, English-United States, French-Canada, French-France, German,
                  		Hungarian, Italian, Japanese, Korean, Polish, Portuguese-Brazil, Russian,
                  		Spanish-Latin America, Spanish-Spain, Swedish, Turkish

Cisco Unity Connection
                     		  Administration

English-United States, Japanese

Cisco Unity Connection
                     		  Administration Help

English-United States

Cisco ViewMail for Microsoft Outlook 12.0 and later

Arabic-Saudi Arabia, Catalan, Chinese-Hong Kong, Chinese-PRC,
                  		Chinese-Taiwan, Czech, Danish, Dutch-Netherlands, Finnish, French-Canada,
                  		French-France, German, Greek, Hebrew, Hungarian, Italian, Japanese, Korean,
                  		Norwegian, Polish, Portuguese-Brazil, Portuguese-Europe, Russian, Spanish-Latin
                  		America, Spanish-Spain, Swedish, Turkish

Cisco Unity Connection Web
                     		  Inbox

Catalan,
                  		Chinese-Hong Kong, Chinese-PRC, Chinese-Taiwan, Czech, Danish,
                  		Dutch-Netherlands, English-United States, Finnish, French-Canada,
                  		French-France, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian,
                  		Polish, Portuguese-Brazil, Portuguese-Europe, Russian, Spanish-Latin America,
                  		Spanish-Spain, Swedish, Turkish

Cisco Unity Connection
                     		  Mini Web Inbox

English-United States

Text-to-speech engine

Arabic-Saudi Arabia, Chinese-PRC, Catalan, Chinese-Hong Kong,
                  		Chinese-Taiwan, Czech, Danish, Dutch-Netherlands, English-Australia,
                  		English-United States, English-United Kingdom, Finnish, French-Canada,
                  		French-France, German, Hungarian, Italian, Japanese, Korean, Norwegian, Polish,
                  		Portuguese-Brazil, Portuguese-Europe, Russian, Spanish-Latin America,
                  		Spanish-Spain, Swedish, Turkish, Hebrew.

Transcription service for
                     		  Cisco SpeechView

English-Australia, English-United States, English-United Kingdom, French-Canada, French-France, German, Spanish-Latin America,
                  Spanish-Spain, Italian.

Voice-recognition
                     		  engine

English-United States

Product documentation for
                     		  administrators/installers

English-United States, Japanese

Product documentation for
                     		  end users

Chinese-PRC, Chinese-Taiwan, Danish, Dutch-Netherlands,
                  		English-United States, French-France, German, Italian, Japanese, Korean,
                  		Portuguese-Brazil, Russian, Spanish-Latin America, Spanish-Spain, Swedish

Translated versions of the five Cisco Unity Connection user
                  		guides are available at http://www.cisco.com/en/US/products/ps6509/tsd_products_support_translated_end_user_guides_list.html .

## Numeric and
               	 Alphabetic Codes for Supported Languages

Use the numeric codes in Table 7 when you are using the Bulk Administration Tool and a CSV file to create or update users. Enter the applicable four- or five-digit
                     numeric code in the Language column for each user. For more information, see the “ Bulk Administration Tool ” chapter of the System Administration Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

Use the alphabetic codes to interpret language-related log
                     		  entries and error codes.

Language

Numeric Code

Alphabetic Code

Arabic-Saudi Arabia

1025

ARA

Catalan

1027

CAT

Chinese-Hong Kong

3076

ZHH

Chinese-PRC

2052

CHS

Chinese-Taiwan

1028

CHT

Czech

1029

CSY

Danish

1030

DAN

Dutch-Netherlands

1043

NLD

English-Australia

3081

ENA

English-United Kingdom

2057

ENG

English-United States

1033

ENU

English TTY/TDD-United States

33801

ENX

Finnish

1035

FIN

French-Canada

3084

FRC

French-France

1036

FRA

German

1031

DEU

Greek

1032

ELL

Hebrew

1037

HEB

Hungarian

1038

HUN

Italian

1040

ITA

Japanese

1041

JPN

Korean

1042

KOR

Norwegian

1044

NOR

Polish

1045

PLK

Portuguese-Brazil

1046

PTB

Portuguese-Europe

2070

PTG

Russian

1049

RUS

Spanish-Latin America

9226

ESO

Spanish-Spain

1034

ESP

Swedish

1053

SVE

Turkish

1055

TRK

Cisco and the Cisco logo
                        			 are trademarks or registered trademarks of Cisco and/or its affiliates in the
                        			 U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks .
                        			 Third-party trademarks mentioned are the property of their respective owners.
                        			 The use of the word partner does not imply a partnership relationship between
                        			 Cisco and any other company. (1110R)

Any Internet Protocol
                        			 (IP) addresses and phone numbers used in this document are not intended to be
                        			 actual addresses and phone numbers. Any examples, command display output,
                        			 network topology diagrams, and other figures included in the document are shown
                        			 for illustrative purposes only. Any use of actual IP addresses or phone numbers
                        			 in illustrative content is unintentional and coincidental.

| Caution | If you try to install version 15 on an unsupported platform, Unity Connection will not be displayed as an option in the Product
                                 Deployment Selection window of the installation program. See the server-specific table in the “Unity Connection Supported
                                 Servers” section of Cisco Unity Connection 15 Supported Platforms List to verify platform specifications, particularly regarding memory and processor speed. |
|---|---|

| Operating System  on Administrator Workstation | Browser on Administrator Workstation |
|---|---|
| Mac OS 13 (macOS Ventura) | Safari |
| Microsoft Windows 11 (32-bit and 64-bit) Enterprise Professional | Mozilla Firefox Chrome Edge |
| Microsoft Windows 10 (32-bit and 64-bit) Enterprise Professional | Mozilla Firefox Chrome Edge |

| Note | Cisco Unity
                                 		  Connection Administration (CUCA) is now supported over both IPv4 and IPv6.
                                 		  However, to access CUCA over IPv6, Unity Connection platform must be configured
                                 		  in Dual (IPv4/IPv6) mode. On CentOS, the
                                    			 IPv6 address is supported only through DNS. |
|---|---|

| Note | Unity connection PIMG/TIMG integration supports Version 6.0,
                                 			 SU10 for Dialogic® 1000 and 2000 Media Gateway Series. |
|---|---|

| Note | Single Inbox over IPv4 and IPv6 is supported for Exchange,Microsoft Office 365 and Gmail server. |
|---|---|

| Note | (Applicable for Releases before 15 SU2) For more information, see "SpeechView" chapter of the System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . (Applicable for Releases 15 SU2 and later) For more information, see "SpeechView Cisco Webex in-house transcription service" chapter of the System Administration Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . |
|---|---|

| Note | The Text-to-Speech feature is supported with Exchange 2019, 2016 and 2013 over both IPv4 and IPv6. However, to access the
                                    transcripted text over IPv6, Unity Connection platform must be configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Accessing calendars is supported with Exchange 2019, 2016 and 2013 over both IPv4 and IPv6. However, to access the calendars
                                    over IPv6, Unity Connection platform must be configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Accessing contacts is supported with Exchange servers over both IPv4 and IPv6. However, to access the contacts over IPv6,
                                    Unity Connection platform must be configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                              feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html . |
|---|---|

| Note | Remote Message Monitor is only supported if all end points
                                 			 (incoming, Unity, and outgoing) are using the same codec. |
|---|---|

| Note | "SpeechView Voicemail Transcript" service option will only be visible on Cisco Webex Cloud-Connected UC when Unity Connection
                                    server is running on Release 15 SU2 or later. |
|---|---|

| Note | Make sure that Domain Name Server (DNS) is configured on Unity Connection as SpeechView Cisco Webex in-house transcription
                              service is not supported with only IP address configuration of Unity Connection. |
|---|---|

| Note | Cisco Personal Communications Assistant (CPCA) is now supported
                                    				both over IPv4 and IPv6. However, to access Cisco PCA over IPv6, Unity
                                    				Connection platform must be configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Web Inbox is now supported over both IPv4 and IPv6. However, to
                                    				access Web Inbox over IPv6, Unity Connection platform must be configured in
                                    				Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Mini Web Inbox is supported over both IPv4 and IPv6. However, to
                           		access Mini Web Inbox over IPv6, Unity Connection platform must be configured
                           		in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Cisco Unity Connection ViewMail for Microsoft Outlook (VMO) is supported over both IPv4 and IPv6. However, to access voice
                           messages using IMAP clients over IPv6, Unity Connection platform must be configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Accessing Unity Connection voice messages using IMAP clients is
                                 			 now supported over both IPv4 and IPv6. However, to access voice messages using
                                 			 IMAP clients over IPv6, Unity Connection platform must be configured in Dual
                                 			 (IPv4/IPv6) mode. |
|---|---|

| Note | RSS feeds is now supported over both IPv4 and IPv6.
                                 			 However, to access RSS feeds over IPv6, Unity Connection platform must be
                                 			 configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Exchange Configuration | Supported Windows Domain Configurations |
|---|---|
| One server running Exchange Server 2019 | Exchange server is a Windows Server 2008, or 2012 domain
                                       						  controller/global catalog server. Exchange server is a Windows Server 2008, or 2012 member server. |
| One server running Exchange Server 2016 | Exchange server is a Windows Server 2008, or 2012 domain controller/global catalog server. Exchange server is a Windows Server 2008, or 2012 member server. |

| Note | Text-to-speech over Exchange servers is now supported over both IPv4 and IPv6. However, to access Text-to-speech over IPv6,
                              Unity Connection platform must be configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Accessing calendars is supported with Exchange servers over both IPv4 and IPv6. However, to access the calendars over IPv6,
                           Unity Connection platform must be configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Accessing contacts is supported with Exchange over both IPv4 and IPv6. However, to access the contacts over IPv6, Unity Connection
                           platform must be configured in Dual (IPv4/IPv6) mode. |
|---|---|

| Note | Cisco will no longer be selling Cisco Fax Server
                                 			 version 10.x after May 2011; however, support for Cisco Fax Server will
                                 			 continue until May 2014. For detailed information on end-of-sale and end-of
                                 			 life dates for the Cisco Fax Server, see the information at http://www.cisco.com/c/en/us/products/collateral/unified-communications/unity/end_of_life_notice_c51-630608.html . |
|---|---|

| Supported LDAP Directory | Supports Redundant
                              				  Directory Servers |
|---|---|
| Microsoft Active Directory 2019 Lightweight Directory Services | Yes |
| Microsoft Active Directory 2019 | Yes |
| Microsoft Active Directory 2016 Lightweight Directory Services | Yes |
| Microsoft Active Directory 2016 | Yes |
| Microsoft Active Directory
                              				  2012 Lightweight Directory Services | Yes |
| Microsoft Active Directory
                              				  2012 and Active Directory 2012 R2 | Yes |
| Microsoft Active Directory
                              				  2008 and Active Directory 2008 R2 | Yes |
| Microsoft Active Directory
                              				  2008 Lightweight Directory Services | Yes |
| Microsoft Active Directory
                              				  2003 | Yes |
| Microsoft Active Directory
                              				  Application Mode (Windows Server 2003 and Windows XP Professional) | Yes |
| OpenLDAP 2.3.39 and 2.4 | Yes |
| Other LDAPv3 Compliant
                              				  Directories | Yes |
| Sun iPlanet or other
                              				  OpenLDAP directory server | Yes |
| Sun ONE Directory Server
                              				  5.2 and later | No |

| Note | The Unity Connection cluster feature is not supported for use with  SAML SSO. |
|---|---|

| Note | The bandwidth
                              		numbers above are intended as guidelines to ensure proper operation of an
                              		active-active cluster with respect to synchronization traffic between the two
                              		servers. Additional conditions such as network congestion, CPU utilization, and
                              		message size may contribute to lower throughput than expected. Call-control and
                              		call-quality requirements are in addition to the guidelines above and should be
                              		calculated using the bandwidth recommendations in the applicable Cisco Unified Communications SRND at http://www.cisco.com/c/en/us/solutions/enterprise/unified-communication-system/index.html . |
|---|---|

| Caution | If failover happens and publisher node of Unity Connection cluster is not completely down then subscriber node will become
                                          primary node and user clients (Jabber,Web Inbox etc..) will still connect to publisher node.However, users may experience
                                          delay in accessing the voicemail through clients. In this case administrator should configure the RTMT alerts "AutoFailbackInitiated
                                          and AutoFailbackSucceeded" to troubleshoot failover. For more information on configuration of these alarms refer Alarm Message
                                          Definitions for Cisco Unity Connection Release 15 guide available at link https://www.cisco.com/c/td-xml/en_us/voice-ip-comm/connections/15/alarm_messages/15cucalrmmsgdef.html . In order to experience seamless voicemail access experience through user clients(Jabber, Web Inbox etc.. ) for Cisco Unity
                                          Connection failover scenario as mentioned above, it is recommended to either deploy the Unity Connection Cluster with maximum
                                          round-trip latency for not more than 5ms when both servers are in separate buildings or sites. Or customer should plan to
                                          install both servers in same building or sites. For more information, see section “ Cluster Requirements When Both Servers are Installed in the Same Building or Site " of System Requirements for Cisco Unity Connection Release 15 guide. |
|---|---|

| Note | The Unity
                              		Connection cluster feature is not supported for use with the SAML SSO feature. |
|---|---|

| Note | SAML SSO feature is not supported to access all the nodes of Intrasite networking. Only a local administrator can configure
                                    the Intrasite networking in Unity Connection.. |
|---|---|

| Note | SAML SSO feature
                              		is not supported to access all the nodes of Intersite networking. Only a local
                              		administrator can configure the Intersite networking in Unity Connection. |
|---|---|

| Note | HTTPS networking is not supported for use with Cisco Business
                                    			 Edition version 3000. Before using HTTPS networking, ensure that directory
                                    			 replication takes place properly in Intrasite or Intersite Networking. Also,
                                    			 the Unity Connection servers should be using appropriate OVA as per topology
                                    			 and directory size. |
|---|---|

| Note | SAML SSO
                                    			 feature is not supported to access all the nodes of HTTPS networking. Only a
                                    			 local administrator can configure the HTTPS networking in Unity Connection. |
|---|---|

| Note | Unity Connection supports SAML 2.0 protocol for the SAML SSO
                                 			 feature. |
|---|---|

| Note | Make
                           		sure that Domain Name Server (DNS) is configured on Unity Connection as SAML
                           		SSO is not supported with only IP address configuration of Unity Connection. |
|---|---|

| Caution | Requirements for Unity Connection 15 are different from requirements for Unity Connection 10.x. The system must meet Unity
                           Connection 15 requirements to receive support from Cisco TAC. |
|---|---|

| Note | With Cisco Unity Connection release 15 and later, direct upgrade from versions 10.5, 11.5 to 15 is not supported. To upgrade
                              from version 10.5 to 15 or from version 11.5 to 15, you must follow an intermediate upgrade path such as going from 10.5 to
                              12.5 or later and then from 12.5 or later to 15. |
|---|---|

| Caution | If you try to install version 15 on an unsupported platform, Unity Connection will not be displayed as an option in the Product
                           Deployment Selection window of the installation program. |
|---|---|

| Note | Unity Connection 15 supports ESXi version of 7.0 U3 or 8.0 U1 with minimum VM Hardware version of 17. |
|---|---|

| Directory Object | Unity Connection Limit |
|---|---|
| Classes of service | 3.000 |
| Call handlers | 40,000 |
| Call routing rules | 1,200 |
| Mailbox stores | 5 |
| Search spaces | 2000 |
| Partitions | 2000 |
| VPIM locations | 100 |

| Directory Object | Unity Connection Limit |
|---|---|
| Connection locations | 25 1 |
| VPIM locations | 100 |
| System distribution lists | 100,000 |
| Members per system distribution list | 25,000 |
| Total number of distribution list members across all system
                                 					 distribution lists | 1.5 million |
| Nested lists within a distribution list | 20 |
| Partitions | 10,000* |

| Note | When using
                              		  more than 2000 search spaces and partitions in a single site, the following
                              		  activities slow down: Searching for Search
                                    				Spaces in the System Administration slows down Modifying and saving
                                    				search spaces can take over 6 minutes. Changing/ Saving/ Reordering Search spaces can take upto 20 mins to replicate across the site. |
|---|---|

|  | Virtual Platform Overlay for up to 1,000 Users | Virtual Platform Overlay for up to 5,000 Users | Virtual Platform Overlay for up to 10,000 Users | Virtual Platform Overlay for up to 20,000 Users |
|---|---|---|---|---|
| Connection locations in the network | 3 | 10 | 10 | 25 |
| HTTPS links Note | 1 | 3 | 3 | 5 |
| Unity Connection local users | 1000 | 5000 | 10,000 | 20,000 |
| Remote users | 9000 | 35,000 | 40,000 | 80,000 |
| Contacts (administrator-defined and VPIM contacts) | - | 20,000 | 30,000 | 150,000 |

| Note | Maximum Unity Connection locations supported in HTTPS network are determined based on the following criteria: Depth of HTTPS network can reach up to second level. Servers used in the network are of same virtual platform overlay. HTTPS links supported at each location are same as mentioned in Table 6 . Maximum of 25 locations can be connected in the network. |
|---|---|

| Note | An
                              		  HTTPS Network can be created with a combination of different platform overlays
                              		  based on the following considerations: The number of locations that can be connected in an HTTPS
                                       				  Network is governed by the highest platform overlay used in the network. The directory size depends upon the lowest platform overlay used
                                       				  in the network. |
|---|---|

| Note | Languages are not licensed, and Unity Connection does not enforce a limit on the number of languages you can install and use.
                           However, the more languages you install, the less hard-disk space is available for storing voice messages. In the Cisco Unity Connection 14 Supported Platforms List available at link https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html , information on the number of minutes of storage available on each server assumes that you have installed no more than five
                           languages. |
|---|---|

| Language | Numeric Code | Alphabetic Code |
|---|---|---|
| Arabic-Saudi Arabia | 1025 | ARA |
| Catalan | 1027 | CAT |
| Chinese-Hong Kong | 3076 | ZHH |
| Chinese-PRC | 2052 | CHS |
| Chinese-Taiwan | 1028 | CHT |
| Czech | 1029 | CSY |
| Danish | 1030 | DAN |
| Dutch-Netherlands | 1043 | NLD |
| English-Australia | 3081 | ENA |
| English-United Kingdom | 2057 | ENG |
| English-United States | 1033 | ENU |
| English TTY/TDD-United States | 33801 | ENX |
| Finnish | 1035 | FIN |
| French-Canada | 3084 | FRC |
| French-France | 1036 | FRA |
| German | 1031 | DEU |
| Greek | 1032 | ELL |
| Hebrew | 1037 | HEB |
| Hungarian | 1038 | HUN |
| Italian | 1040 | ITA |
| Japanese | 1041 | JPN |
| Korean | 1042 | KOR |
| Norwegian | 1044 | NOR |
| Polish | 1045 | PLK |
| Portuguese-Brazil | 1046 | PTB |
| Portuguese-Europe | 2070 | PTG |
| Russian | 1049 | RUS |
| Spanish-Latin America | 9226 | ESO |
| Spanish-Spain | 1034 | ESP |
| Swedish | 1053 | SVE |
| Turkish | 1055 | TRK |