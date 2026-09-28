---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-mac-12-5-jabm-b-releasenotes-125-html-988953069d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/mac/12_5/jabm_b_releasenotes_125.html
retrieved_at: 2026-08-21T07:00:39.719604+00:00
---

Release Notes for Cisco Jabber for Mac 12.5

# Release Notes for Cisco Jabber for Mac 12.5

### Download Options

Updated: January 29, 2019

First Published: November 29, 2018

Last Updated: January 29, 2019

# Build Number for 12.5

Version

Build Number

12.5(1)

12.5.1.277406

12.5

12.5.0.272870

The DownloadURL file element in the XML file for automatic updates is:

Release

File Name

12.5(1)

Install_Cisco-Jabber-Mac-12.5.1.277406-98008072-

12.5

Install_Cisco-Jabber-Mac-12.5.0.272870-97969984-

MCwCFEpX2mM7UcqJQ++DVyNhtZa0YQy1AhQQMJEU6_kg8UjZ9PZVQTAO3JDwxw!!.zip

## DownloadURL

The DownloadURL file element refers to the Cisco Jabber for Mac installation file. The installation file on the update server
                  must be renamed to match this DownloadURL file element name.

You can also download the manual installation file, if your users install the client manually.

To ensure the DSA signature succeeds, configure Web servers to escape special characters. For example, on Microsoft IIS the
                              option is: Allow double spacing .

## What’s New in Cisco Jabber for Mac 12.5(1)

### Resolved Caveats

This release provides fixes for a number of known issues. See the Resolved Caveats 12.5(1) section for a list of caveats fixed
                     in this release.

## What's New in Cisco Jabber for Mac 12.5

### Newly Supported Features

With the release with Cisco Unified Communications Manager Release 12.5(1) and Cisco Expressway for Mobile and Remote Access X12.5 , the following features are now fully supported in Jabber:

UC Manager Configuration Tool —Move your configuration from the jabber-config.xml file into the UC Manager, using our new configuration tool to simplify Jabber deployment. This feature requires Cisco UC
                           Manager 12.5.

For more information about how it works and how to use it, see the Parameters Reference Guide for Cisco Jabber 12.5 .

SIP OAuth Support —Jabber now supports the OAuth protocol to authorize Jabber clients to use secure tokens for RTP and SIP traffic. We've built
                           on the OAuth support from previous releases by now allowing SIP traffic to be encrypted. You set up SIP OAuth on the Cisco
                           Unified Communications Manager. This feature requires UC Manager 12.5.

For more information, see the Planning Guide for Cisco Jabber 12.5 . To set up SIP Oauth, see the Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1) .

ICE Media Support —Improve user experience when on the Expressway for Mobile and Remote Access. Clients that are outside the corporate network
                           can use the ICE protocol to share media directly with each other. This feature requires Cisco Expressway X12.5.

To find out more about how ICE media works, see the Planning Guide for Cisco Jabber 12.5 . To set up ICE media, see the Mobile and Remote Access via Expressway Deployment Guide X12.5 and later .

### Preview Features

Preview Features Disclaimer: Some features in this release are provided in preview status only, because they have known limitations
                     or incomplete software dependencies. Cisco reserves the right to disable preview features at any time without notice. Preview
                     features should not be relied on in your production environment. Cisco Technical Support will provide limited assistance (Severity
                     4) to customers who want to use preview features.

Jabber team messaging mode —Jabber for Mac and Windows users have a new cloud-based deployment option that lets your users work together in a team messaging
                     mode from their Jabber client. In team messaging mode, users get a new Chats tab in their client that they can use for group discussions. They'll be able to collaborate together by sending and reading
                     messages, and create new spaces, add people, mute and moderate spaces. For a detailed look at what Jabber team messaging mode
                     is and how it works, see the Cloud-Based Deployment Scenarios in the Planning Guide for Cisco Jabber 12.5 and the new workflow in the Cloud and Hybrid Deployments for Cisco Jabber 12.5 .

For team messaging mode, Jabber will only support the last two versions of Jabber team messaging mode. Four months after a
                        major version is released, the version from two releases prior will go end-of-support. For other deployments, Jabber will follow the standard end-of-support strategy. Check the End-Of-Support Notices for details.

### Improved Collaboration

ActiveControl — ActiveControl provides enhanced conferencing features to Cisco Jabber, like the ability to choose the video layout, record
                           the call, mute and unmute yourself and others, and locking the conference call. You set up ActiveControl in Cisco Meeting
                           Server 2.3 or later and need Cisco Unified Communications Manager 10.5 or later. We've put more information in the Features Guide for Cisco Jabber 12.5 about how to set it up.

New User Experience —Jabber looks even better now, with updated icons and a better layout.

### Hardware

Firmware for Cisco Headsets —This release includes a firmware update for Cisco 500 Series headset models. Users are automatically prompted to update when
                           they connect to Jabber.

## Requirements

### Cisco Jabber Requirements

Many Cisco Jabber requirements are common between client types. Client specific requirements are documented in the Release Notes , all other requirements are documented in the Planning Guide for Cisco Jabber .

### Operating System for Cisco Jabber for Mac

macOS Mojave 10.14 or later

macOS High Sierra 10.13 (or later)

macOS Sierra 10.12 (or later)

OS X El Capitan 10.11 (or later)

### Hardware
                  	 Requirements for Desktop Clients

Requirement

Cisco Jabber for
                                       				  Windows

Cisco Jabber for Mac

Installed RAM

2-GB RAM
                                    						on Microsoft Windows 7 and Windows 8

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

To view the list of Computer Telephony Integration (CTI)  supported devices: From Cisco Unified Reporting, select Unified CM Phone Feature List . From the Feature drop-down list, select CTI controlled .

## Limitations and Restrictions

### Single Number Reach

For Cisco TelePresence Video Communication Server Control (VCS) versions earlier than 8.10.X, you need to configure the editable
                     inbound rules to enable the single number reach for users who are using Cisco Jabber over Mobile and Remote Access. For more
                     information, see Limitations in Enable Single Number Reach section from the Feature Configuration Guide for Cisco Jabber 12.0 .

### Save Chats to Outlook

When you use Outlook 2016, all images sent in chats are not saved in Outlook, however any emoji sent in chats are saved in
                     Outlook.

### Audio Device Setting After Upgrade

When users upgrade the client, intermittently this results in a reset of their selected audio devices. To resolve this issue,
                     set the audio devices in the Audio/Video Preferences window. This limitation is documented in CSCva48136.

### Antivirus

When the client connects to Cisco Unity Connection on a device that has antivirus software, users can have issues with voicemail
                     connections. To resolve this issue, add the Cisco Unity Connection server information to the exceptions list for the antivirus
                     software.

### Users in Common Identity

There is a known issue signing into Cisco Jabber for some users who have migrated to Common Identity. If users receive an Incorrect user name or password error message when entering their username and password, see the following knowledge base article https://cisco-support.webex.com/guest/articles/en_US/Troubleshooting/WBX000019555/myr=false .

### Creating and Configuring Devices for Users in Cisco Unified Communications Manager 11.0

If you are creating devices for users in Cisco Unified Communications Manager 11.0, you can now specify a key order as RSA Only , EC Only or EC Preferred, RSA Backup . However, the EC Only option is not supported by Cisco Jabber, and if you select it, the client fails to connect to the server.

### Certificate Validation for CTI Connections

Cisco Jabber uses certificate validation for CTI connections. We recommend using either Public CA or Private CA to sign certificates.

Connecting to Cisco Unified Communications Manager using a self-signed certificate, results in a certificate validation failure,
                     to resolve this issue do one of the following:

The user accepts the invalid Cisco Unified Communications Manager self-signed certificate on first certificate validation
                           failure and Cisco Jabber saves this certificate to the trust store.

Deploy the certificates using a certificate deployment management application.

### Expressway for Mobile and Remote Access Deployment

For an Expressway for Mobile and Remote Access deployment, when using an online certificate status protocol (OCSP) or online
                     certificate revocation lists (CRL) to obtain the revocation status of the certificates, the Cisco Jabber client expects a response time of less than 5 seconds. Connections will fail if the response time is greater than the expected
                     5 seconds.

### Network Disconnection When Using Cisco Jabber on Audio or Video Call

There is a known issue in the Mac OS where network interfaces drop intermittently when DSCP is enabled.

If you encounter this issue, do the following:

- Select Preferences > Calls > Advanced .

- Uncheck Enable Differentiated Service for Calls .

### Standard CTI Secure Connection User Group

Cisco Jabber for Mac does not currently support CTI connections over transport layer security (TLS). As a result, Cisco Jabber
                     for Mac users cannot switch from using a CSF device to using a desk phone device if they belong to the Standard CTI Secure
                     Connection user group.

### Contact Resolution for Enterprise Groups

Jabber resolves contacts in enterprise groups individually rather than all at once. As a result, when you add an enterprise
                     group to your users' contact lists—or if they clear their local cache—they'll only see the username and domain for each person
                     until they hover over or interact with them.

## Caveats

Caveats describe unexpected behavior. The following sections describe how to obtain the latest information.

### Search for Bugs

To search for bugs not listed here, use the Bug Search Tool.

To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search .

Sign in with your Cisco.com user ID and password.

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release.

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

### Resolved Caveats in Release 12.5(1)

### Resolved Caveats in Release 12.5

### This Document Applies to These Products

- Jabber for Mac

| Version | Build Number |
|---|---|
| 12.5(1) | 12.5.1.277406 |
| 12.5 | 12.5.0.272870 |

| Release | File Name |
|---|---|
| 12.5(1) | Install_Cisco-Jabber-Mac-12.5.1.277406-98008072- MC0CFFuLzVBAsF9xMKT_SVcsZ32a2C7KAhUAlbmMrIYWsbhhR60IS1GlFTgn7B4!.zip |
| 12.5 | Install_Cisco-Jabber-Mac-12.5.0.272870-97969984- MCwCFEpX2mM7UcqJQ++DVyNhtZa0YQy1AhQQMJEU6_kg8UjZ9PZVQTAO3JDwxw!!.zip |

| Note | To ensure the DSA signature succeeds, configure Web servers to escape special characters. For example, on Microsoft IIS the
                              option is: Allow double spacing . |
|---|---|

| Requirement | Cisco Jabber for
                                       				  Windows | Cisco Jabber for Mac |
|---|---|---|
| Installed RAM | 2-GB RAM
                                    						on Microsoft Windows 7 and Windows 8 | 2-GB RAM |
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
| Step 3 | To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release. |

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
| CSCvn57810 | 3 | Jabber Does Not Sync 1404 Credentials Even if 2100 Phone Credentials is Obtained. |
| CSCvn45751 | 3 | Jabber "All Rooms" tab does not load. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvj58903 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after transfer. |
| CSCvj58906 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after hold/resume. |
| CSCvk48746 | 3 | Jabber for Mac user authentication with IM&P does not time out. |
| CSCvm77105 | 3 | Typing a complete phone number may result in dialing a number from 'Contacts and recents' list. |
| CSCvm85867 | 3 | Webex meeting call-in Jabber doesn't work on Mac. |