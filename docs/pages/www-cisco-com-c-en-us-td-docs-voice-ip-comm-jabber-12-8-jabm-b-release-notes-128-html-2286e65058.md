---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-8-jabm-b-release-notes-128-html-2286e65058
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_8/jabm_b_release-notes-128.html
retrieved_at: 2026-08-21T07:00:27.734117+00:00
---

Release Notes for Cisco Jabber for Mac 12.8

# Release Notes for Cisco Jabber for Mac 12.8

First Published: January 22, 2020

Last Updated: May 31, 2021

# Jabber End-User Content on Cisco Webex Help Center

You can find information on the Jabber client at https://help.webex.com/ld-n1uv5wq-CiscoJabber/Jabber . The
               Help Center contains articles on using Jabber features. You can provide feedback on
               individual articles or request new articles through the Help Center.

The Help Center search includes a set of filters to narrow your results by product, release, activities, operating system,
               and other categories.

## Build Number

Version

Build Number

12.8(8)

12.8.8.307305

12.8(6)

12.8.6.305104

12.8(5)

12.8.5.304791

12.8(4)

12.8.4.304226

12.8(3)

12.8.3.303943

12.8(2)

12.8.2.302955

12.8(1)

12.8.1.302494

12.8

12.8.0.301920

### DownloadURL

The DownloadURL file element in the XML file for automatic updates is:

Release

File Name

12.8(8)

Install_Cisco-Jabber-Mac-12.8.8.307305-104891550-MCwCFCkHFcfQS0F4mWlCNsiR3jJQmLxmAhRuu6C4moIjkImRbgLfSKPbpmDXXA!!.zip

12.8(6)

Install_Cisco-Jabber-Mac-12.8.6.305104-103927905-MCwCFCAP3bbDiSbI73bur370uwiMSP1yAhQcucpHvL+hrADeWqn_HS1rKd_vqQ!!.zip

12.8(5)

Install_Cisco-Jabber-Mac-12.8.5.304791-104091957-MCwCFC+tb3a1EVmnBT3oKcPzSmAM_zyTAhQRu62CVxVFq0T+iM_aWQt72sBOlA!!.zip

12.8(4)

Install_Cisco-Jabber-Mac-12.8.4.304226-104043304-MCwCFAqEFRGrFFVk3vvSvgu5uMnffo4+AhR1ezHEPS5zPXwwMHHk4RObTw9oYg!!.zip

12.8(3)

Install_Cisco-Jabber-Mac-12.8.3.303934-104037296-MC0CFQCWUv5b62c6gtyo8qUDaJfRn8Tn+QIUPSBDWb+FbEWXhUfcx7GEwwavDoY!.zip

12.8(2)

Install_Cisco-Jabber-Mac-12.8.2.302955-103628328-MCwCFAWT+J2Kw7be6k2oRie4vJk5ktklAhRqeqP7jbEQczONDtRplNBHhz7B3A!!.zip

12.8(1)

Install_Cisco-Jabber-Mac-12.8.1.302494-103496141-MCwCFHQpjW_pS1KJfypGKamBGhtdhD96AhRoBmTZHpN+e72uiIL3PjW7HKwI_Q!!.zip

12.8

Install_Cisco-Jabber-Mac-12.8.0.301920-104215537-MCwCFEgGeORDMaAA_GAmBlIo3HuFXbDnAhQuS6valIDo00brmrTjR99TFjCGNw!!.zip

The DownloadURL file element refers to the Cisco Jabber for Mac installation file. The installation file on the update server
                     must be renamed to match this DownloadURL file element name.

You can also download the manual installation file, if your users install the client manually.

To ensure the DSA signature succeeds, configure Web servers to escape special characters. For example, on Microsoft IIS the
                                 option is: Allow double spacing .

## Security Advisories

You can find information on the latest security advisories at https://tools.cisco.com/security/center/publicationListing.x .

## What's New in Release 12.8(8)

This maintenance release contains security updates. See the Caveats for details.

## What's New in Release 12.8(7)

This maintenance release includes stability improvements.

## What's New in Release 12.8(6)

This maintenance release contains caveat updates.

## What's New in Release 12.8(5)

This maintenance release contains caveat updates.

## What's New in Release 12.8(4)

This maintenance release includes stability improvements.

### Jabber-to-Teams Migration Tool

Supported from 12.8(3)

If you're moving Jabber users to Webex Teams, you can use a new built-in tool to help
                     				your Jabber users migrate contacts and common settings. For information on how to
                     				set the tool up, see Configure
                           						Users to Move Jabber Contacts and Common Settings to Webex
                           					Teams . End users can learn how to use the tool by reading Move Contacts and Common Settings to Webex Teams .

## What's New in Release 12.8(3)

This maintenance release contains caveat updates.

## What's New in Release 12.8(2)

This maintenance release contains defect fixes. See the Caveats section for details.

## What's New in Release 12.8(1)

This Maintenance Release includes only bug fixes. See the caveats lists for details.

## What's New in Release 12.8

### H.264 High Profile Support

We added support for the H.264 codec's High profile. The High profile uses less bandwidth to provide the same video quality
                     as the Baseline profile that we already support.

By default, Jabber uses the Baseline profile. You can enable High profile with the H264HighProfileEnable parameter.

### Microsoft Office 2019 Support

We added support for Microsoft Office 2019 desktop applications to Jabber for Mac.

### Call Park Support

We added support for the Call Park feature to the desktop clients. Earlier releases supported Call Park only on the mobile
                     clients.

### Separate Ringtones for Each Line on Multiline

We've enhanced Multiline support and now your users can assign a different ring tone for each of their configured lines. If
                     they don't want audible notification from some lines, they can assign the new silent ring tone.

### Updates to Collaboration Meeting Room Controls

This release includes several new CMR controls.

Hosts can now pause and resume the meeting recording.

All participants can do the following:

See who has an open camera in the participant list.

Copy the meeting link.

Use the Meeting Info icon to display details about the meeting.

### Presence Status

We added a toggle in the General settings to show or hide presence information. When you uncheck Show Status , you don’t share your status with your organization and you don’t see their statuses.

### Audio Device Priority

You can choose to give newly registered audio devices the highest priority or continue using the current audio device. Jabber
                     only offers this choice when first registering each audio device. Otherwise, Jabber uses the available device with the highest
                     priority in the device priority list.

Your administrator can use the HeadsetPreference parameter to specify this behavior. It defaults to putting the newly registered device at the top of the priority list. But,
                     each user can override this option in their Audio preferences.

### Custom Contacts for Team Messaging Mode

You can now create, edit, and delete custom contacts in Jabber Team Messaging Mode deployments.

You can migrate existing custom contacts and custom contact groups into your Jabber Team Messaging Mode deployment. The migration
                     operates as follows:

Custom contacts without display names don’t migrate.

For custom contacts with email addresses or phone numbers matching someone in Common Identity (CI), Jabber changes the custom
                           contact to the normal contacts from CI. Any customized information for those contacts is removed.

The custom contacts that you create on a desktop client are also available in your mobile client. But, you can't create, edit,
                     or delete custom contacts from the mobile client.

### New Cisco Headset Support

We've added support for the new Cisco Headset 730 Series.

The Advanced settings dialog dynamically includes settings specific to some Cisco headsets. For more information, visit https://www.cisco.com/c/en/us/products/collaboration-endpoints/headset-700-series/index.html .

### Show Sent Voice Messages

We added the ability to see your sent voice messages in your Jabber voicemail box.

To enable this feature, the administrator must set Sent Messages: Retention Period (in Days) on the Messaging Configuration page in Cisco Unity Connection Administration .

### Jabber Analytics through Webex Control Hub

This release note describes a new feature in Webex Control Hub that impacts Jabber deployments. Because it’s a change in Control
                                 Hub, you can access this feature for any release of Jabber.

If your deployment has Webex Control Hub configured, you can access Jabber analytics through the Control Hub. This feature
                     is available for the following deployment modes:

On-premises with full UC

On-premises IM-Only

On-premises Phone-Only

Jabber with Webex Messenger

Jabber analytics provides key performance indicators with trending, such as:

Active users​

Messages sent

Calls made or received from Jabber

Screen share from Jabber

See the Feature Configuration for Cisco Jabber guide for more information.

## Requirements

### Cisco Jabber Requirements

Many Cisco Jabber requirements are common between client types. Client specific requirements are documented in the Release Notes , all other requirements are documented in the Planning Guide for Cisco Jabber .

### Operating System for Cisco Jabber for Mac

You can install Cisco Jabber for Mac on the following operating systems:

macOS Catalina 10.15  (or later)

macOS Mojave 10.14 (or later)

macOS High Sierra 10.13 (or later)

We notarized Cisco Jabber for Mac 12.7 with Apple.

### Hardware
                  	 Requirements for Desktop Clients

Requirement

Cisco Jabber for
                                       				  Windows

Cisco Jabber for Mac

Installed RAM

2-GB RAM

2-GB RAM

Free
                                    						physical memory

128 MB

1 GB

Free
                                    						disk space

256 MB

300 MB

CPU
                                    						speed and type

AMD
                                    						Mobile Sempron Processor 3600+ 2 GHz

Intel
                                    						Core 2 Duo Processor T7400 @ 2. 16 GHz

Intel
                                    						Core 2 Duo or later processors in any of the following Apple hardware:

iMac Pro

MacBook Pro (including Retina Display model)

MacBook

MacBook Air

iMac

Mac
                                          							 Mini

I/O
                                    						ports

USB 2.0
                                    						for USB camera and audio devices.

USB 2.0
                                    						for USB camera and audio devices

#### CTI Supported
                     	 Devices

To view the list of Computer Telephony Integration (CTI) supported devices for your Unified Communications Manager:

From the Cisco Unified Reporting page, select Unified CM Phone Feature List from the System Reports menu.

After opening the report, select CTI controlled from the Feature drop-down list.

## Limitations and Restrictions

### New Certificate Requirements for macOS 10.15

Apple has new requirements for trusted certificates in macOS 10.15 (see https://support.apple.com/en-us/HT210176 ). Ensure that the certificates on the Unified Communications Mananger, IM & Presence, and Expressway servers meet these requirements.
                     If your certificates don't meet these requirements, users are prompted to accept the certificates for each session.

### Webex Site Disclaimers

Webex site disclaimers don't appear when you join Webex meetings from Jabber. This limitation applies whether joining from
                     the meeting reminder popup, or by selecting Join in Webex in Jabber.

### Single Number Reach

For Cisco TelePresence Video Communication Server Control (VCS) versions earlier than 8.10.X, configure the editable inbound
                     rules to enable the single number reach for users who are using Cisco Jabber over Mobile and Remote Access. For more information,
                     see Limitations in Enable Single Number Reach section from the Feature Configuration Guide for Cisco Jabber 12.0 .

### Save Chats to Outlook

When you use Outlook 2016, Outlook won't save images that are sent in chats. However, Outlook does save any emoji in the chats.

### Audio Device Setting After Upgrade

When users upgrade the client, it can intermittently result in a reset of their selected audio devices. To resolve this issue,
                     set the audio devices in the Audio/Video Preferences window. CSCva48136 documents this limitation.

### Antivirus

When the client connects to Cisco Unity Connection on a device that has antivirus software, users can have issues with voicemail
                     connections. To resolve this issue, add the Cisco Unity Connection server information to the exceptions list for the antivirus
                     software.

### Users in Common Identity

There’s a known issue signing into Cisco Jabber for some users who have migrated to Common Identity. If users receive an Incorrect username or password error message when entering their username and password, see the following knowledge base article https://cisco-support.webex.com/guest/articles/en_US/Troubleshooting/WBX000019555/myr=false .

### Creating and Configuring Devices for Users in Cisco Unified Communications Manager 11.0

If you’re creating devices for users in Cisco Unified Communications Manager 11.0, you can now specify a key order as either:

RSA Only

EC Only

EC Preferred, RSA Backup

However, Cisco Jabber doesn't support the EC Only option. If you select it, the client fails to connect to the server.

### Certificate Validation for CTI Connections

Cisco Jabber uses certificate validation for CTI connections. We recommend using either Public CA or Private CA to sign certificates.

Connecting to Cisco Unified Communications Manager using a self-signed certificate, results in a certificate validation failure,
                     to resolve this issue do one of the following:

The user accepts the invalid Cisco Unified Communications Manager self-signed certificate on first certificate validation
                           failure and Cisco Jabber saves this certificate to the trust store.

Deploy the certificates using a certificate deployment management application.

### Expressway for Mobile and Remote Access Deployment

For an Expressway for Mobile and Remote Access deployment, when using an online certificate status protocol (OCSP) or online
                     certificate revocation lists (CRL) to verify certificate status, Cisco Jabber expects a response time of less than 5 seconds. Connections fail if the response time is greater than the 5 seconds.

### Network Disconnection When Using Cisco Jabber on Audio or Video Call

There’s a known issue in the Mac OS where network interfaces drop intermittently when DSCP is enabled.

If you encounter this issue, do the following:

Select Preferences > Calls > Advanced .

Uncheck Enable Differentiated Service for Calls .

### Standard CTI Secure Connection User Group

Cisco Jabber for Mac doesn’t currently support CTI connections over transport layer security (TLS). As a result, Cisco Jabber
                     for Mac users can’t switch from using a CSF device to using a desk phone device if they belong to the Standard CTI Secure
                     Connection user group.

### Contact Resolution for Enterprise Groups

Jabber resolves contacts in enterprise groups individually rather than all at once. When you add an enterprise group to your
                     users' contact lists or they clear their local cache, they originally only see each person's username and domain. More information
                     appears when they next hover over or interact with a person.

### Bluetooth Connectivity Unsupported with Cisco Headset 56x

Cisco Jabber doesn’t support the use of Bluetooth with Model 56x Cisco headsets. You can use these headsets with a USB-C to
                     USB connector cable.

### Cisco Headset Support with Multiple VoIP Apps

If you use Cisco Jabber with a Cisco Headset, you can’t install any other VoIP app, such as Cisco Webex Teams or Skype for
                     Business, on your computer.

### Poly Headset Plug-in Removed

Cisco Jabber for Mac 12.8 removed the Poly headset plug-in. The plug-in caused a monitor keyboard input alert on macOS 10.15.
                     Without the plug-in, we can't support call controls (answer, decline, hold, and resume) on the headsets.

When there's a fix for the plug-in, we’ll add it back into Jabber.

### Windows 10 Crash Using Cisco 700 Series Headsets

If you use Cisco 700 Series headsets, you might experience Windows OS crashes (Blue screen). This occurs on Windows 10 version
                     1803 and earlier versions. Update to a later version of Windows 10 to correct the problem.

### Joining Meetings by Meeting Number

In deployments that use a Cisco Webex Meeting Server, you cannot use the meeting number when joining by Webex. Use the meeting
                     URL instead.

### Port Contention Disrupts Sennheiser Plug-In

Call control with the Sennheiser plug-in uses port 8001 by default. If another application uses this port, it can cause issues.

As a workaround, you can change the EPOS SDK's PortNumber parameter to another port in the appropriate file:

Windows— %LOCALAPPDATA%\Sennheiser\SDKCore\PDS\config.dat

Mac— /Library/Application Support/Sennheiser/SenncomSDK/secomSFSDK.dat

Consult Sennheiser for more information about these files.

Shut down Jabber before changing the port in the SDK. Then, restart Jabber after you change the port.

## Caveats

Caveats describe unexpected behavior. The following sections describe how to obtain the latest information.

### Search for Bugs

To search for bugs not listed here, use the Bug Search Tool.

To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search .

Sign in with your Cisco.com user ID and password.

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release.

For more information, select Help at the top right of
                                    the Bug Search page.

### Bug Severity Levels

Known defects, or bugs, have a severity level that indicates the priority of the defect. These release notes include the following
                        bug types:

All severity level 1 or 2 bugs

Significant severity level 3 bugs

All customer-found bugs except severity level 6 enhancement requests

Severity Level

Description

1 Catastrophic

Reasonably common circumstances cause the entire system to fail, or a major subsystem to stop working, or other devices on
                                    the network to be disrupted. No workarounds exist.

2 Severe

Important functions are unusable and workarounds do not exist. Other functions and the rest of the network is operating normally.

3 Moderate

Failures occur in unusual circumstances, or minor features do not work at all, or other failures occur but low-impact workarounds
                                    exist.

This is the highest level for documentation bugs.

4 Minor

Failures occur under very unusual circumstances, but operation essentially recovers without intervention. Users do not need
                                    to install any workarounds and performance impact is tolerable.

5 Cosmetic

Defects do not cause any detrimental effect on system functionality.

6 Enhancement

Requests for new functionality or feature improvements.

### Resolved caveats in 12.8(8)

CSCwc24382

### Resolved Caveats in 12.8(6)

Identifier

Severity

Headline

CSCvw93559

3

Jabber Mac: Most of strings are unlocalized for Italian language

### Resolved Caveats in 12.8(5)

Identifier

Severity

Headline

CSCvv88490

1

Cisco Jabber Cross-Site Scripting leading to RCE

CSCvv88491

3

Cisco Jabber Password Hash Stealing Information Disclosure

CSCvw38030

1

Jabber Client Empty a Tags Not Processed by the Hyperlink Replacer
                                 Leads to XSS

### Resolved Caveats in Release 12.8(3)

Identifier

Severity

Headline

CSCvu89568

3

Jabber for Mac not accepting all SIP URI pattern

CSCvv06604

3

Jabber chats display in 24 hour (military) time regardless of OS setting

### Resolved Caveats in Release 12.8(2)

Identifier

Severity

Headline

CSCvu00490

3

Jabber 12.8.1 and 12.8.2 fails to get phone services over MRA

CSCvu00496

3

Jabber Mac does not clear the Active Call count causing the CUCM to reject further calls with 486

### Closed Caveats in Release 12.8(1)

Identifier

Severity

Headline

CSCvq52820

3

Jabber process using High CPU on MAC OS Mojave and Catalina

### Open Caveats in Release 12.8

Identifier

Severity

Headline

CSCvs58600

3

Mute all in CMR meeting cannot work after assign host

### Resolved Caveats in Release 12.8

Identifier

Severity

Headline

3

Jabber did not stop the retry of the user bulk queries failed with code CONNECTION_TIMEOUT_ERROR.

CSCvr12551

3

Jabber does not refresh access token in failover scenario over MRA

CSCvr39510

3

Jabber needs to mask the option to start a conversation when IM is disabled

CSCvr42550

3

"Start meeting" does not dial the Personal Meeting Room if "Join in Jabber" option is selected

CSCvr44644

3

Jabber 12.6.1/12.7 for Mac crashes when # (option key + 3) pressed on UK keyboard

CSCvr52618

3

Jabber 12.7 Meetings displayed do not show as hyperlink.

CSCvr82895

3

Jabber for MAC fails to authenticate BFCP if user id is changed in re-invite

CSCvr87405

3

When hover the mouse on share screen icon the share screen button tagging says "Start meetings"

CSCvr88304

3

Unable to share the screen on jabber 12.7 in first instance on Mac Catalina Version 10.15

CSCvs05055

3

Jabber for Mac crashing when performing Reset

CSCvs06450

3

Jabber for Mac does not load chat history list when switched from Classic to Modern appearance

CSCvs09317

3

Error when clicks on Join in the invite from a Jabber Meeting(MAC)

CSCvs18528

3

Classic UXModel parameter not applied on Jabber MAC

CSCvs39539

3

Jaber for MAC 12 IM service logs out when making changes to IM account settings on Jabber settings

CSCvs51098

4

On Jabber 12.7.1 MAC the notification badge does not loads if the preload parameter is set to true

### This Document Applies to These Products

- Jabber for Mac

| Version | Build Number |
|---|---|
| 12.8(8) | 12.8.8.307305 |
| 12.8(6) | 12.8.6.305104 |
| 12.8(5) | 12.8.5.304791 |
| 12.8(4) | 12.8.4.304226 |
| 12.8(3) | 12.8.3.303943 |
| 12.8(2) | 12.8.2.302955 |
| 12.8(1) | 12.8.1.302494 |
| 12.8 | 12.8.0.301920 |

| Release | File Name |
|---|---|
| 12.8(8) | Install_Cisco-Jabber-Mac-12.8.8.307305-104891550-MCwCFCkHFcfQS0F4mWlCNsiR3jJQmLxmAhRuu6C4moIjkImRbgLfSKPbpmDXXA!!.zip |
| 12.8(6) | Install_Cisco-Jabber-Mac-12.8.6.305104-103927905-MCwCFCAP3bbDiSbI73bur370uwiMSP1yAhQcucpHvL+hrADeWqn_HS1rKd_vqQ!!.zip |
| 12.8(5) | Install_Cisco-Jabber-Mac-12.8.5.304791-104091957-MCwCFC+tb3a1EVmnBT3oKcPzSmAM_zyTAhQRu62CVxVFq0T+iM_aWQt72sBOlA!!.zip |
| 12.8(4) | Install_Cisco-Jabber-Mac-12.8.4.304226-104043304-MCwCFAqEFRGrFFVk3vvSvgu5uMnffo4+AhR1ezHEPS5zPXwwMHHk4RObTw9oYg!!.zip |
| 12.8(3) | Install_Cisco-Jabber-Mac-12.8.3.303934-104037296-MC0CFQCWUv5b62c6gtyo8qUDaJfRn8Tn+QIUPSBDWb+FbEWXhUfcx7GEwwavDoY!.zip |
| 12.8(2) | Install_Cisco-Jabber-Mac-12.8.2.302955-103628328-MCwCFAWT+J2Kw7be6k2oRie4vJk5ktklAhRqeqP7jbEQczONDtRplNBHhz7B3A!!.zip |
| 12.8(1) | Install_Cisco-Jabber-Mac-12.8.1.302494-103496141-MCwCFHQpjW_pS1KJfypGKamBGhtdhD96AhRoBmTZHpN+e72uiIL3PjW7HKwI_Q!!.zip |
| 12.8 | Install_Cisco-Jabber-Mac-12.8.0.301920-104215537-MCwCFEgGeORDMaAA_GAmBlIo3HuFXbDnAhQuS6valIDo00brmrTjR99TFjCGNw!!.zip |

| Note | To ensure the DSA signature succeeds, configure Web servers to escape special characters. For example, on Microsoft IIS the
                                 option is: Allow double spacing . |
|---|---|

| Note | This release note describes a new feature in Webex Control Hub that impacts Jabber deployments. Because it’s a change in Control
                                 Hub, you can access this feature for any release of Jabber. |
|---|---|

| Requirement | Cisco Jabber for
                                       				  Windows | Cisco Jabber for Mac |
|---|---|---|
| Installed RAM | 2-GB RAM | 2-GB RAM |
| Free
                                    						physical memory | 128 MB | 1 GB |
| Free
                                    						disk space | 256 MB | 300 MB |
| CPU
                                    						speed and type | AMD
                                    						Mobile Sempron Processor 3600+ 2 GHz Intel
                                    						Core 2 Duo Processor T7400 @ 2. 16 GHz | Intel
                                    						Core 2 Duo or later processors in any of the following Apple hardware: iMac Pro MacBook Pro (including Retina Display model) MacBook MacBook Air iMac Mac
                                          							 Mini |
| I/O
                                    						ports | USB 2.0
                                    						for USB camera and audio devices. | USB 2.0
                                    						for USB camera and audio devices |

| Note | Consult Sennheiser for more information about these files. |
|---|---|

| Step 1 | To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search . |
|---|---|
| Step 2 | Sign in with your Cisco.com user ID and password. |
| Step 3 | To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release. For more information, select Help at the top right of
                                    the Bug Search page. |

| Severity Level | Description |
|---|---|
| 1 Catastrophic | Reasonably common circumstances cause the entire system to fail, or a major subsystem to stop working, or other devices on
                                    the network to be disrupted. No workarounds exist. |
| 2 Severe | Important functions are unusable and workarounds do not exist. Other functions and the rest of the network is operating normally. |
| 3 Moderate | Failures occur in unusual circumstances, or minor features do not work at all, or other failures occur but low-impact workarounds
                                    exist. This is the highest level for documentation bugs. |
| 4 Minor | Failures occur under very unusual circumstances, but operation essentially recovers without intervention. Users do not need
                                    to install any workarounds and performance impact is tolerable. |
| 5 Cosmetic | Defects do not cause any detrimental effect on system functionality. |
| 6 Enhancement | Requests for new functionality or feature improvements. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCwc24382 | 3 | Cisco Jabber Security Vulnerability: XMPP Stanza Smuggling with stream:stream tag |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvw93559 | 3 | Jabber Mac: Most of strings are unlocalized for Italian language |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvv88490 | 1 | Cisco Jabber Cross-Site Scripting leading to RCE |
| CSCvv88491 | 3 | Cisco Jabber Password Hash Stealing Information Disclosure |
| CSCvw38030 | 1 | Jabber Client Empty a Tags Not Processed by the Hyperlink Replacer
                                 Leads to XSS |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvu89568 | 3 | Jabber for Mac not accepting all SIP URI pattern |
| CSCvv06604 | 3 | Jabber chats display in 24 hour (military) time regardless of OS setting |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvu00490 | 3 | Jabber 12.8.1 and 12.8.2 fails to get phone services over MRA |
| CSCvu00496 | 3 | Jabber Mac does not clear the Active Call count causing the CUCM to reject further calls with 486 |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvq52820 | 3 | Jabber process using High CPU on MAC OS Mojave and Catalina |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvs58600 | 3 | Mute all in CMR meeting cannot work after assign host |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvs48285 | 3 | Jabber did not stop the retry of the user bulk queries failed with code CONNECTION_TIMEOUT_ERROR. |
| CSCvr12551 | 3 | Jabber does not refresh access token in failover scenario over MRA |
| CSCvr39510 | 3 | Jabber needs to mask the option to start a conversation when IM is disabled |
| CSCvr42550 | 3 | "Start meeting" does not dial the Personal Meeting Room if "Join in Jabber" option is selected |
| CSCvr44644 | 3 | Jabber 12.6.1/12.7 for Mac crashes when # (option key + 3) pressed on UK keyboard |
| CSCvr52618 | 3 | Jabber 12.7 Meetings displayed do not show as hyperlink. |
| CSCvr82895 | 3 | Jabber for MAC fails to authenticate BFCP if user id is changed in re-invite |
| CSCvr87405 | 3 | When hover the mouse on share screen icon the share screen button tagging says "Start meetings" |
| CSCvr88304 | 3 | Unable to share the screen on jabber 12.7 in first instance on Mac Catalina Version 10.15 |
| CSCvs05055 | 3 | Jabber for Mac crashing when performing Reset |
| CSCvs06450 | 3 | Jabber for Mac does not load chat history list when switched from Classic to Modern appearance |
| CSCvs09317 | 3 | Error when clicks on Join in the invite from a Jabber Meeting(MAC) |
| CSCvs18528 | 3 | Classic UXModel parameter not applied on Jabber MAC |
| CSCvs39539 | 3 | Jaber for MAC 12 IM service logs out when making changes to IM account settings on Jabber settings |
| CSCvs51098 | 4 | On Jabber 12.7.1 MAC the notification badge does not loads if the preload parameter is set to true |