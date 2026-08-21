---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-mac-12-6-jabm-b-release-notes-12-6-html-4bf01be7dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/mac/12_6/jabm_b_release-notes_12-6.html
retrieved_at: 2026-08-21T07:00:35.694377+00:00
---

Release Notes for Cisco Jabber for Mac 12.6

# Release Notes for Cisco Jabber for Mac 12.6

### Download Options

Updated: January 14, 2020

First Published: April 9, 2019

Last Updated: January 14, 2020

# Build Number for 12.6

Version

Build Number

12.6(1)

12.6.1.284405

12.6

12.6.0.281201

The DownloadURL file element in the XML file for automatic updates is:

Release

File Name

12.6

## DownloadURL

The DownloadURL file element refers to the Cisco Jabber for Mac installation file. The installation file on the update server
                  must be renamed to match this DownloadURL file element name.

You can also download the manual installation file, if your users install the client manually.

To ensure the DSA signature succeeds, configure Web servers to escape special characters. For example, on Microsoft IIS the
                              option is: Allow double spacing .

## What's New in Cisco Jabber for Mac 12.6(1)

### Cisco Headset Controls

There are new audio settings available for users of Cisco 561 and 562 headsets. Users can adjust the sidetone and equalizer
                     settings of the headset, check what firmware version is installed, and reset the headset to its default state. These features
                     require Headset Firmware Release 1.5 and Cisco Unified Call Manager 12.5(1)SU1. For more information, see the Cisco Unified Communications Manager Administration Guide .

### Disable Mute Tone

You can now turn off the audio tone that plays by default when a user mutes themselves during a call. For more information,
                     refer to the SelfMuteTone parameter in the Parameters Reference Guide for Cisco Jabber 12.6 .

### Keypad Enhancements

We've expanded the Jabber keypad to include two symbols: the comma (,) and the plus sign (+).

### Support for Viewing ECM Files

In team messaging mode, users are now able to view files sent to them via Enterprise Content Management (ECM) rather than
                     from a local directory. Selecting a shared ECM file will cross-launch a web browser where the file can be viewed.

### Resolved Caveats

This release provides fixes for a number of known issues. See the Resolved Caveats 12.6(1) section for a list of caveats fixed
                     in this release.

## What's New in Cisco Jabber for Mac 12.6

### Jabber Team Messaging Mode

This feature was released in 12.5 as a preview, and in 12.6, we are happy to announce it is a fully supported feature, with
                     support on mobile clients now also added.

Chat features —You can now format text and flag messages.

Upgrade Profiles —You can create upgrade profiles on the Webex Control Hub for individual users. Use the upgrade profiles to control which
                     version of Jabber team messaging mode your users are on. For more information about setting up upgrade profiles, see how to Add Upgrade Profiles in the Webex Control Hub in Cloud and Hybrid Deployments for Cisco Jabber 12.6 .

Search on CI, UDS and LDAP —Users with Jabber team messaging mode can now search for contacts and their profiles from the company directory (on UDS/LDAP),
                     even if the contact is not in the CI. With the search results, you'll see the person's profile picture, and be able to call
                     them. To define the scope of contacts search, CI-only search is the default behavior. For more information, check out the ContactProfileSource and ContactSearchSource parameters in the Parameters Reference Guide for Cisco Jabber 12.6.

File Policy —You can control the file policy for your users on Jabber team messaging mode by restricting if users can share files. Set
                     the file policy in the Cisco Webex Control Hub.

### Meetings

Meeting Controls for Video Device-Enabled Meetings —Users can join Cisco Collaboration Meeting Rooms from Jabber, where they can see the participant list, change the video layout,
                     lock and record the meeting, mute, unmute, and remove participants, and assign host privileges. Jabber supports using PIN
                     numbers to access video device-enabled Webex meetings.

ActiveControl Support Over the MRA Expressway —ActiveControl is accessible to users who are outside of the corporate network by using the Expressway for Mobile and Remote
                     Access (MRA). Using ActiveControl over MRA is done using SIP oAuth or CAPF enrollment. For environments without secure phones,
                     users can now authenticate to the network using their username and password when moving onto MRA.

For information about setting up ActiveControl, see Feature Configuration for Cisco Jabber 12.6.

Improved Video Resolution —Jabber now supports HD video at 1080p/30FPS bidirectionally (transmit/receive) at the same time. The CPU must be Intel Core
                     i5 or later, with a bandwidth of between 2 and 4 Mbps.

Keypad Support —When users go to their Call tab in Jabber, a keypad is now available for them to use to make a call using their mouse, if they don't want to use their
                     keyboard for the Search or Call bar.

On-Premises Proximity and Wireless Screen Sharing —Users can now share their screen with this on-premises proximity feature to share the screen from their computers on a video
                     device using ultrasound. If the Auto-connection toggle is on, the Jabber client will connect automatically to a nearby video
                     device. Supported devices include Cisco MX, SX, DX, IX, and the Cisco Webex Room Series.

This feature is on by default. To turn it off, change the EnableProximity parameter to false . For more information about the parameter, see the Parameters Reference Guide for Cisco Jabber 12.6 .

Screen Sharing in Webex —We've improved screen sharing for Mac users in IM only desktop share for Webex messenger deployment, to bring the experience
                     inline with what you can do in Cisco Jabber for Windows.

### Feature Improvements

Offline Message Support For Jabber and Webex Teams —We have improved the experience for Webex Messenger users who are enabled for interoperability between Cisco Jabber and Cisco
                     Webex Teams. Now when users who have been using Cisco Webex Teams sign back in to Jabber after a period being offline, they
                     will no longer get an alert telling them that new messages are available in Webex Teams, with a link to the Webex Teams web
                     client. Instead, they will receive their new messages in Jabber for their missed one-to-one conversations.

To enable this feature, see how to Set Up Interoperability for Cisco Webex Teams and Jabber .

Save Chat History to Office 365 —We've added support for modern authentication with Office 365, which means that users can save their Jabber chat history
                     to cloud-based Exchange servers. For more information on setting this up, see the Chat History in Microsoft Outlook section in Feature Configuration for Cisco Jabber 12.6 .

Spam Prevention —We’ve enhanced the privacy settings available for users in Cisco Webex Messenger deployments. Users can choose to block incoming
                     messages globally and add trusted contacts or domains to their allow list.

Hide Persistent Chat Room Members —Jabber now supports a setting in Cisco Unified Communications Manager that lets you decide whether members and administrators
                     of a persistent chat room are listed in the room even when they don't have the chat window open. Changes to this setting apply
                     only to restricted rooms that are created after the change has been made. For more information, see the Persistent Chat Rooms section in Feature Configuration for Cisco Jabber 12.6 .

UDS Failover —If your Cisco Unified Communications Manager User Data Service server ( UDS1(UCM1) becomes unavailable, Jabber can now dynamically
                     failover to the UDS2(UCM2) server for contact resolution and search. For more information, see Planning Guide for Cisco Jabber 12.6 .

Support for Special Characters —Jabber now supports special characters in usernames during login.

## Requirements

### Cisco Jabber Requirements

Many Cisco Jabber requirements are common between client types. Client specific requirements are documented in the Release Notes , all other requirements are documented in the Planning Guide for Cisco Jabber .

### Operating System for Cisco Jabber for Mac

You can install Cisco Jabber for Mac on the following operating systems:

macOS Catalina 10.15  (or later)

macOS Mojave 10.14 (or later)

macOS High Sierra 10.13 (or later)

macOS Sierra 10.12 (or later)

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

GPU

DirectX11 on Microsoft Windows 7

N/A

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

### Open Caveats in Release 12.6(1)

### Open Caveats in Release 12.6

### Resolved Caveats in Release 12.6.x

#### Resolved caveats in release 12.6.1

#### Resolved caveats in release 12.6

### This Document Applies to These Products

- Jabber for Mac

| Version | Build Number |
|---|---|
| 12.6(1) | 12.6.1.284405 |
| 12.6 | 12.6.0.281201 |

| Release | File Name |
|---|---|
| 12.6(1) | Install_Cisco-Jabber-Mac-12.6.1.284405-107214898-MC0CFCd7spWTv7JzVJVqy_Yo+Ds61BpxAhUAiPafL7_VOczXLv28XUxLFjC_mcM!.zip |
| 12.6 | Install_Cisco-Jabber-Mac-12.6.0.281201-107094431-MCwCFCMMahfarJf5Jk7Y3E0zYsVbpODKAhRJZpRTvJpS_otbrNfntjLyggJ5PQ!!.zip |

| Note | To ensure the DSA signature succeeds, configure Web servers to escape special characters. For example, on Microsoft IIS the
                              option is: Allow double spacing . |
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
| GPU | DirectX11 on Microsoft Windows 7 | N/A |
| I/O
                                    						ports | USB 2.0
                                    						for USB camera and audio devices. | USB 2.0
                                    						for USB camera and audio devices |

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
| CSCvp22805 | 3 | Random Crash when perform jabber call in macOS 10.14.4 and machine with 2 graphics cards |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvp13607 | 3 | Messages & Files search results fetched are not same as Teams client. |
| CSCvp13633 | 3 | Contact service 'search more' API return empty result. |
| CSCvp13646 | 3 | Inconsistent presence in Jabber teams mode against Webex Teams client. |
| CSCvp13667 | 3 | No space list is shown after login. |
| CSCvp13693 | 3 | Unexpected unread status for one old space after sign out. |
| CSCvp13702 | 3 | Many trivial threads created by cpprest when day0 login. |
| CSCvp22805 | 3 | [J4M] Random Crash when performing a Jabber call in macOS 10.14.4 and machine with 2 graphics cards. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvp45112 | 2 | DTMF digits not transferred in time (within 50ms) |
| CSCvp74650 | 3 | Jabber 12.6 fails to call URIs containing webex.com if conference profile applied |
| CSCvp95654 | 3 | Jabber 12.6 choppy audio for outbound calls |
| CSCvq13800 | 3 | Jabber does not show hunt pilot information |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvo43107 | 2 | Jabber with Hybrid (WebEx Messenger) and on-prem phone services is getting forced to sign-out. |
| CSCvm60187 | 3 | Cisco Jabber Client Framework (JCF) Insecure Directory Permissions Vulnerability. |
| CSCvn42926 | 3 | Jabber would generate a Webex trace in /tmp folder when  signed in. |
| CSCvn50852 | 3 | [J4M] Incorrect CSS style leads to bullet points < li > in wrong vertical position in chat window |
| CSCvo13089 | 3 | Cisco Jabber for Mac has incorrect year in call History. |
| CSCvo27156 | 3 | Jabber bot HTML formatted messages do not render/work correctly. |
| CSCvo59911 | 4 | Jabber for Mac is wrongly resolving numbers in format +99(0)12 3123456. |