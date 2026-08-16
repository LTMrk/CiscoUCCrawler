---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-windows-12-5-jabw-b-releasenotes-125-html-9acacc3b66
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Windows/12_5/jabw_b_releasenotes_125.html
retrieved_at: 2026-08-16T19:12:56.250344+00:00
---

Release Notes for Cisco Jabber for Windows 12.5

# Release Notes for Cisco Jabber for Windows 12.5

First Published: November 29, 2018

Last Updated: May 31, 2021

# Jabber End-User Content on Cisco Webex Help Center

You can find information on the Jabber client at https://help.webex.com/ld-n1uv5wq-CiscoJabber/Jabber . The
               Help Center contains articles on using Jabber features. You can provide feedback on
               individual articles or request new articles through the Help Center.

The Help Center search includes a set of filters to narrow your results by product, release, activities, operating system,
               and other categories.

## Build Number for 12.5

Version

Build Number

12.5(4)

12.5.4.39931 Build 289931

12.5(3)

12.5.3.39720 Build 289720

12.5(2)

12.5.2.39445 build 289445

12.5(1)

12.5.1.27406

12.5

12.5.0.272884

## Additional Maintenance Releases

For additional maintenance release information, refer to:

Feature enhancements  — see https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html for the latest version of release
                           notes.

Caveats — see https://bst.cloudapps.cisco.com/bugsearch/ for latest caveat updates.

Security Advisories — see https://tools.cisco.com/security/center/publicationListing.x for a listing of the latest advisories.

## What's New in Release 12.5(4)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.5(3)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.5(2)

This maintenance release contains security updates. See the Caveats for details.

## What’s New in Cisco Jabber for Windows 12.5(1)

### Resolved Caveats

This release provides fixes for a number of known issues. See the Resolved Caveats 12.5(1) section for a list of caveats fixed
                     in this release.

## What's New in Cisco Jabber for Windows 12.5

### Preview Features are now Fully Supported

With the release with Cisco Unified Communications Manager Release 12.5(1) and Cisco Expressway for Mobile and Remote Access X12.5 , the following features are now fully supported in Jabber:

UC Manager Configuration Tool —Move your configuration from the jabber-config.xml file into the UC Manager, using our new configuration tool to simplify Jabber deployment. This feature requires Cisco UC
                           Manager 12.5.

SIP OAuth Support —Jabber now supports the OAuth protocol to authorize Jabber clients to use secure tokens for RTP and SIP traffic. We've built
                           on the OAuth support from previous releases by now allowing SIP traffic to be encrypted. You set up SIP OAuth on the Cisco
                           Unified Communications Manager. This feature requires UC Manager 12.5.

ICE Media Support —Improve user experience when on the Expressway for Mobile and Remote Access. Clients that are outside the corporate network
                           can use the ICE protocol to share media directly with each other. This feature requires Cisco Expressway X12.5.

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

ActiveControl —ActiveControl provides enhanced conferencing features to Cisco Jabber, like the ability to choose the video layout, record
                           the call, mute and unmute yourself and others, and locking the conference call. You set up ActiveControl in Cisco Meeting
                           Server 2.3 or later and need Cisco Unified Communications Manager 10.5 or later. We've put more information in the Features Guide for Cisco Jabber 12.5 about how to set it up.

New User Experience —Jabber looks even better now, with updated icons and a better layout.

### Easier Client Configuration

Common Criteria —You can now run Jabber for Windows in Common Criteria mode, which ensures that the environment is compliant with Common Criteria
                           requirements. You turn on Common Criteria mode by using the CC_MODE installation argument. For more information, see Common Criteria in the Planning Guide for Cisco Jabber 12.5 .

### Accessories

Alert for USB Audio Connections —You'll get an alert to let you know when Jabber has connected to a new USB audio device so you can decide whether to change
                           your audio-out settings.

Firmware for Cisco Headsets —This release includes a firmware update for Cisco 500 Series headset models. Users are automatically prompted to update when
                           they connect to Jabber.

## Requirements

### Cisco Jabber Requirements

Many Cisco Jabber requirements are common between client types. Client specific requirements are documented in the Release Notes , all other requirements are documented in the Planning Guide for Cisco Jabber .

### Operating Systems for Cisco Jabber for Windows

You can install
                        		  Cisco Jabber for Windows on the following operating systems:

Microsoft Windows 10 (desktop mode)

Microsoft
                              				Windows 8.1 (desktop mode)

Microsoft
                              				Windows 8 (desktop mode)

Cisco Jabber for
                        		  Windows does not require the Microsoft .NET Framework or any Java modules.

#### Windows 10 Servicing Options

Cisco Jabber for Windows supports  the following Windows 10 servicing options:

Current Branch (CB)

Current Branch for Business (CBB)

Long-Term Servicing Branch (LTSB)—with this option, it is your responsibility to ensure that any relevant service updates
                              are deployed.

For more information about Windows 10 servicing options, see  the following Microsoft documentation: https://technet.microsoft.com/en-us/library/mt598226(v=vs.85).aspx .

%temp%\Cisco Systems\Cisco Jabber-Bootstrap.properties file and installation log

%LOCALAPPDATA%\Cisco\Unified Communications-Logs and temporary telemetry data

%APPDATA%\Cisco\Unified Communications-Cached configurations and account credentials

%ProgramFiles%\Cisco Systems\Cisco Jabber-Installation files for x86 Windows

%ProgramFiles(x86)%\Cisco Systems\Cisco Jabber-Installation files for x64 Windows

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

### Limitations and Restrictions All Deployments

#### LDAP Credential Delivery with Unified Communications Manager 12.5(1) SU2

In Unified Communications Manager Release 12.5(1) SU2, Unified CM added support for securely passing encrypted LDAP credentials
                        in the Service Profile. This update secures access to your directory by ensuring that the password is always stored and sent
                        in an encrypted format. This change includes encryption during directory access authentication, client configuration file
                        downloads, BAT imports/exports, and upgrades.

In Jabber 12.8 with this Unified CM release or later, we take advantage of this capability by downloading the LDAP credentials
                        as part of User Profile after end-user authentication.

In Jabber 12.7 and earlier with this Unified CM release or later, we can’t use these credentials from the Service Profile
                        as we did before. They pass an encrypted password to Active Directory which causes a connection failure. For these Jabber
                        releases with the upgraded Unified CM, provide the LDAP credentials through the jabber-config.xml file.

For more details, see the Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1) SU2 and the section on LDAP Service Accounts in the Planning Guide for Cisco Jabber .

#### Device Name with Extension Mobility

When Extension Mobility is enabled, the controlled devices menu in Jabber displays the phone type only, instead of the phone
                        type and user name.

#### Cisco IP Communicator

Cisco IP Communicator isn’t supported as a controlled device on Jabber when users choose to use their desk phone for calls.

#### Multiline

Cisco Jabber can't make calls from any line, while there's an incoming call ringing on another line. While another line is
                        ringing, the green Call button is dimmed and not available. Users can wait for the ringing to stop, or decline the incoming call.

#### Allow Paste Operations via Script

Jabber versions 11.8.5 and later may have issues with Copy/Paste when the policy Allow paste operations via script is enabled for Internet Explorer at Windows Components > Internet Explorer > Internet Control Panel > Security Page > Internet zone .

#### Single Number Reach

For Cisco TelePresence Video Communication Server Control (VCS) versions earlier than 8.10.X, configure the editable inbound
                        rules to enable the single number reach for users who are using Cisco Jabber over Mobile and Remote Access. For more information,
                        see Limitations in Enable Single Number Reach section from the Feature Configuration Guide for Cisco Jabber 12.0 .

#### Voicemail Credential Popup during Sign-in

In a hybrid deployment, if Webex messenger, Call Manager and Unity connection are all SSO enabled, and voicemail credentials
                        have been previously saved to cloud, users may see the Update Credentials popup for voicemail during the sign-in process. The workaround is not to configure voicemail server address on the cloud
                        server but only configure it in the service profile or the jabber-config.xml file.

#### IBM Notes Contact Search

When searching for an IBM Notes contact, entering either " or \ as the first character in the search string won't find the
                        correct contact.

#### Real-Time Transport Control Protocol (RTCP)

Jabber sends RTCP packets even when disabled. RTCP is an integral component of Jabber Telephony services.

#### Cannot Copy Image

You can’t right-click over an image in a conversation in Jabber and select copy. Instead, highlight the image and then right-click
                        to copy it.

#### Microsoft Outlook OST File

Intermittently Cisco Jabber for Windows is unable to access the Microsoft Outlook OST file. To resolve this issue, restart
                        Jabber and restart Outlook.

#### Automatic Detection of Proxy Settings (WPAD)

Cisco Jabber doesn’t support Web Proxy Auto-Discovery (WPAD) proxy discovery. For information about how to configure proxy
                        settings for Cisco Jabber, see Configure Proxy Settings in the On-Premises Deployment for Cisco Jabber guide.

#### Call Transfers

When you’re transferring a call to a third party, the third party must respond to the call before you can complete the transfer.
                        You can’t currently dial the third party and connect the first party while waiting for the call to connect (also known as
                        a blind transfer).

Prior to Release 12.7(1), Cisco Jabber doesn’t correctly inform Unified Communications Manager that a call being transferred
                        is on hold. This behavior results in incorrect reporting when you use Jabber with Cisco Finesse.

#### Chat Reply and No Voicemail Profile

If the user has no voicemail profile configured, the chat reply feature doesn’t work. If the user selects Chat reply in an incoming call, the call continues to ring and the Chat reply and Answer options are grayed out. CSCux75667 documents this limitation.

#### Cisco AnyConnect Secure Mobility Client

Cisco Jabber for Windows supports Cisco AnyConnect Secure Mobility Client version 4.0 and later. CSCuy14721 documents this
                        limitation.

#### Cisco Unity Connection Dispatch Messages

In Cisco Unity Connection, a dispatch message is sent to a distribution list with the message configured in such a way that
                        only one user responds to that message. A user can accept, decline, or postpone the dispatch message. Cisco Jabber for Windows
                        doesn’t support Cisco Unity Connection dispatch messages. CSCuw31908 documents this limitation..

#### Emails to a Group of Contacts

There’s a limit of 2083 characters in the To field when sending an email to a group of contacts. With long email addresses or many recipients, not all contacts may be
                        added to the email. For more information about the 2083 character limitation, see https://support.microsoft.com/en-ie/kb/208427 .

#### Location Feature and Multiple Domain Support

Consider the following deployment scenario:

When you deployed your Cisco Unified Communications Manager IM and Presence Service node, all users were imported with single
                        domain support. You later changed the address scheme to Directory URI (multiple domain support).

The location feature now doesn't work for newly added domain users. Users in the initial domain are unaffected. CSCuu63734
                        documents this limitation.

#### Logitech Keyboard Display Changes

The built-in display for Logitech UC keyboard K725-C doesn’t display caller or device information on incoming calls. Instead,
                        the Cisco logo is displayed.

#### Microsoft Outlook Local Contacts and Presence

Users' presence is unknown when the contact is manually added to contacts in Microsoft Outlook 2010 and 2013, when the contact
                        is added to local (custom) contacts with an email address type of SMTP. To resolve this issue, delete the contact and add
                        it again manually, ensuring the email address type is Exchange (EX). CSCuo57172 documents this limitation.

#### Phone Mode Deployments with Microsoft Lync

Disable Click-to-x functionality if you want to deploy Cisco Jabber for Windows in phone mode on the same computer as Microsoft
                        Lync. See the Common Installation Arguments section of the Deployment Guide for more information about the CLICK2X installer switch.

#### Plantronics Accessories and Software

If you use Plantronics accessories for Cisco Jabber call management, and if you have Plantronics Hub installed, ensure that
                        at least version 3.5 is installed. Download Plantronics Hub 3.5 from the Plantronics website.

#### Remote Desktop Control over Mobile and Remote Access

Remote desktop control over Mobile and Remote Access isn’t supported. This limitation is documented in CSCuz19139.

#### SAML Single Sign-On Limitations

When configuring SAML SSO on Cisco Unified Communications Manager servers, use a fully qualified domain name (FQDN) instead
                        of an IP Address to define the server name. If you use an IP Address, the client displays a warning message that the certificate
                        isn’t valid. The requirement to use an FQDN is because the embedded Internet Explorer browser isn’t able to validate IP addresses
                        in the Subject Alternate Name (SAN) certificate.

For the same reason, when you configure SAML SSO on Cisco Unity Connection servers, use a fully qualified domain name (FQDN)
                        in Cisco Unified Communications Manager Service Profile instead of an IP Address to define the server name. If you use an
                        IP Address, the client displays a warning message that the certificate isn't valid.

#### Space Characters in Credentials

The following rules apply to space characters and credentials:

Usernames can contain spaces in on-premises deployments.

Usernames can’t contain spaces in cloud-based deployments.

Passwords can’t contain spaces in any deployment scenario.

The first and last characters of usernames in on-premises deployments must not be spaces. This rule is also true for usernames
                              synchronized from a directory source.

#### Standard CTI Secure Connection User Group

Cisco Jabber for Windows doesn’t currently support CTI connections over transport layer security (TLS). As a result, Cisco
                        Jabber for Windows users can’t switch from using a CSF device to using a desk phone device if they belong to the Standard
                        CTI Secure Connection user group. This limitation is documented in CSCux83786.

#### .TIFF Images Not Supported

In this release, if users have a .tiff image as their avatar, then Jabber displays the default icon image instead. To use
                        a personal avatar, users must upload an image in a supported format, such as jpg, bmp, or png.

#### Using Click-To-X Feature with Contacts in Microsoft Outlook

If you use UDS as a directory source, users can only use Click-To-X capabilities, such as Click-To-Call and Click-To-IM, to
                        contact Microsoft Outlook users if they are already in the cache file. A cache file is created for someone if they are in
                        the users' Cisco Jabber contacts list, or have a Cisco Jabber history created by the user previously searching, IMing, or
                        calling them, or by leaving a voice message.

#### Supported Characters in a Cisco Jabber User ID/E-mail Address

The following characters are supported in a Cisco Jabber user ID/E-mail Address:

Uppercase characters (A to Z)

Lowercase characters (a to z)

Numbers (0-9)

Period (.)

Hyphen (-)

Underscore (_)

Tilde (~)

#### Extension Mobility

Jabber doesn’t support the Cisco Extension Mobility Cross Cluster (EMCC) feature.

#### Bluetooth Connectivity Unsupported with Cisco Headset 56x

Cisco Jabber doesn’t support the use of Bluetooth with Model 56x Cisco headsets. You can use these headsets with a USB-C to
                        USB connector cable.

#### Cisco Headset Support with Multiple VoIP Apps

If you use Cisco Jabber with a Cisco Headset, you can’t install any other VoIP app, such as Cisco Webex Teams or Skype for
                        Business, on your computer.

#### Windows 10 Crash Using Cisco 700 Series Headsets

If you use Cisco 700 Series headsets, you might experience Windows OS crashes (Blue screen). This occurs on Windows 10 version
                        1803 and earlier versions. Update to a later version of Windows 10 to correct the problem.

#### Joining Meetings by Meeting Number

In deployments that use a Cisco Webex Meeting Server, you cannot use the meeting number when joining by Webex. Use the meeting
                        URL instead.

### Limitations and Restrictions for On-Premises Deployments

#### Port Contention Disrupts Sennheiser Plug-In

Call control with the Sennheiser plug-in uses port 8001 by default. If another application uses this port, it can cause issues.

As a workaround, you can change the EPOS SDK's PortNumber parameter to another port in the appropriate file:

Windows— %LOCALAPPDATA%\Sennheiser\SDKCore\PDS\config.dat

Mac— /Library/Application Support/Sennheiser/SenncomSDK/secomSFSDK.dat

Consult Sennheiser for more information about these files.

Shut down Jabber before changing the port in the SDK. Then, restart Jabber after you change the port.

#### Adding Federated Contacts

When adding federated contacts, Cisco recommends that users add the federated contacts as company contacts ( File > New > Contact ), rather than as custom contacts. Adding federated contacts as custom contacts can cause intermittent presence issues. This
                        issue is documented in CSCuz59060.

#### Creating and Configuring Devices for Users in Cisco Unified Communications Manager 11.0

If you are creating devices for users in Cisco Unified Communications Manager 11.0, you can now specify a key order as RSA Only , EC Only or EC Preferred, RSA Backup . However, the EC Only option is not currently supported by Cisco Jabber, and if you select it, the client will fail to connect to the server.

#### Multiple Resource Login

When a user signs in to multiple instances of the client at the same time, the chat feature behaves as follows in on-premises
                        deployments (more on multiple resource login in Common Deployment Scenarios):

Signing in on one client changes custom availability states to 'Available' on other clients.

If you set the availability  state from 'On a call' to another state while on a call, the availability  state does not automatically
                              change to 'On a call' for subsequent calls.

#### SIP Trunk for Phone Presence

From Release 11.5(3), you must configure a SIP trunk between Cisco Unified Communications Manager and IM and Presence Service
                        if you want Cisco Jabber users to see phone presence. In previous releases, a SIP trunk was not required for phone presence.
                        This limitation is documented in CSCuz85578.

### Limitations and Restrictions for Cloud Deployments

#### Blocking Users in  Enterprise Groups

Blocking users does not prevent a blocked user's status from being displayed if the blocked users are in a contact list as
                        part of an enterprise group. For example, User A blocks User B. However, User A is in User B's contact list as part of an
                        enterprise group. As a result, User B can view User A's availability status.

#### Invitees to Instant Webex Meetings

Invitees to instant Webex meetings must be provisioned with Webex accounts before they can join an instant Webex meeting.
                        For example, User A has a Webex account and starts an instant Webex meeting from Cisco Jabber. Use A then invites User B,
                        who does not have a Webex account, to the meeting. When User B clicks on the meeting link in Cisco Jabber, an error message
                        is displayed and the user can't join the meeting. User B must be provisioned with a Webex account before attempting to join
                        any instant Webex meetings. This limitation is documented in CSCux52068.

#### Jabber to Jabber  Calls

We recommend running Internet Explorer 10 or greater while using the Jabber to Jabber calling feature. Using this feature
                        with previous versions of Internet Explorer or with Internet Explorer in Compatibility Mode can cause issues with Cisco Jabber
                        client login (non-SSO setup) or Jabber to Jabber calling capability (SSO setup).

#### Users in Common Identity

There is a known issue with signing into Cisco Jabber for some users who have migrated to Common Identity. If users receive
                        an Incorrect user name or password error message when entering their username and password, see the following article, https://help.webex.com/en-us/yhq7pw/Reset-Forgotten-Password-in-Cisco-Jabber .

## Performance and Behavior Notes

### Presence indicators on Sharepoint 2016

When you sign-out of Jabber, the presence indicator bubbles are grayed out and do not refresh after signing back into Jabber.

You can resolve this behavior by refreshing the webpage. This will ensure that accurate presence information is displayed.

### Do Not Disturb (DND)

If Jabber is controlling the Deskphone and if Do Not Disturb (DND) is set on the Deskphone,the presence status of the Jabber
                     client does not change.

This behavior indicates that the Jabber client is functioning as designed. No action is required from the user.

### Jabber to Jabber Calls and Symantec Host IDS (HIDS)

Jabber to Jabber calls can trigger errors in Symantec HIDS.

Symantec HIDS has a rule that disables connections from internet-based servers if it receives 5 connection requests from the
                     same internet-based server within 200 seconds. For example, 3 Jabber to Jabber calls within 200 seconds will trigger Symantec
                     HIDS. When this happens, ongoing Jabber to Jabber calls are dropped and Jabber to Jabber calls are disabled for 600 seconds.

To avoid this scenario, you must add Cisco Jabber to the Symantec exception list. This behavior is documented in CSCuw32007.

### HTML Sanitization Code

The Jabber HTML sanitization code has been modified to disallow 'masked' links in XMPP message payloads due to its potential
                     abuse in phishing attacks. These links are no longer allowed for security reasons.

It is recommended that Jabber Administrators educate potential users who may be affected by this feature enhancement.

### Meeting Reminders

Cisco Jabber displays pop-up reminders for Cisco Webex meetings only. Reminders for non-Cisco Webex meetings are not displayed.

If the URL for a Webex meeting is changed (for example, by URL filter software), attempts to join the meeting from the meeting
                     reminder or from the Meetings tab fail. This behavior is documented in CSCux03658.

### Schedule Meeting Button Disabled on Phone-Only Mode

When Outlook is installed, and the MacCalendarIntegrationType parameter is set to Outlook, the Schedule Meeting button is displayed. However in phone-only mode, the button is not shown.

### Removing Participants During Conference Calls

Users can only remove participants from a conference call when using a softphone (CSF) device for calls in a non-VDI deployment.
                     Users can't remove participants from conference calls in desk phone control mode or using extend and connect.

### Video Calls

The Start My Video button doesn't work immediately after a call connects. Users must wait approximately 6 seconds after the call starts before
                     clicking the Start My Video button. This behavior is documented in CSCuz06415.

### Contact Resolution for Enterprise Groups

Jabber resolves contacts in enterprise groups individually rather than all at once. As a result, when you add an enterprise
                     group to your users' contact lists—or if they clear their local cache—they'll only see the username and domain for each person
                     until they hover over or interact with them.

## Caveats

Caveats describe unexpected behavior. The following sections describe how to obtain the latest information.

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

### Search for Bugs

To search for bugs not listed here, use the Bug Search Tool.

To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search .

Sign in with your Cisco.com user ID and password.

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release.

### Open Caveats 12.5(4)

### Resolved Caveats in 12.5(4)

### Open Caveats in 12.5(3)

### Resolved Caveats in 12.5(3)

Identifier

Severity

Headline

CSCvv88490

1

Cisco Jabber Cross-Site Scripting leading to RCE

CSCvv88491

3

Cisco Jabber Password Hash Stealing Information Disclosure

CSCvv88492

2

Cisco Jabber Custom Protocol Handler Command Injection

CSCvw38030

1

Jabber Client Empty a Tags Not Processed by the Hyperlink Replacer
                                 Leads to XSS

CSCvw39218

3

Jabber Client Clickjacking

CSCvw39231

3

Jabber Client Javascript Functions for Downloading and Opening Files
                                 Need No Confirmation

### Resolved Caveats in Release 12.5(2)

Identifier

Severity

Headline

2

Cisco Jabber for Windows Message Handling Arbitrary Code Execution Vulnerability

2

Jabber Sensitive Data Disclosure through crafted chat message

2

Jabber Sensitive Data Disclosure Through malicious link

2

Cisco Jabber for Windows Protocol Handler Command Injection Vulnerability

### Open Caveats in Release 12.5(1)

### Resolved Caveats in Release 12.5(1)

### Closed Caveats in Release 12.5(1)

Switch front and rear camera Surface, the memory leak detects each time.

### Open Caveats in Release 12.5

### Resolved Caveats in Release 12.5

### This Document Applies to These Products

- Jabber for Windows

| Version | Build Number |
|---|---|
| 12.5(4) | 12.5.4.39931 Build 289931 |
| 12.5(3) | 12.5.3.39720 Build 289720 |
| 12.5(2) | 12.5.2.39445 build 289445 |
| 12.5(1) | 12.5.1.27406 |
| 12.5 | 12.5.0.272884 |

| Note | Cisco Jabber installs the required files to the following directories by default: %temp%\Cisco Systems\Cisco Jabber-Bootstrap.properties file and installation log %LOCALAPPDATA%\Cisco\Unified Communications-Logs and temporary telemetry data %APPDATA%\Cisco\Unified Communications-Cached configurations and account credentials %ProgramFiles%\Cisco Systems\Cisco Jabber-Installation files for x86 Windows %ProgramFiles(x86)%\Cisco Systems\Cisco Jabber-Installation files for x64 Windows |
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

| Step 1 | To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search . |
|---|---|
| Step 2 | Sign in with your Cisco.com user ID and password. |
| Step 3 | To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvm76932 | 2 | Jabber for Windows 12.1.0/12.1.1 Does Not Send
                                 setEnableInAMeetingStatus update to CUCM. |
| CSCvj26171 | 3 | Input of Unicode characters on search box on Windows 10 results
                                 in invalid data. |
| CSCvn17374 | 3 | Jabber sending https request to loginp.webexconnect.com
                                 overwhelming IDP. |
| CSCvm44162 | 3 | Jabber tries to reconnect while get 403 error response from Cisco
                                 Unity Connection. |
| CSCvm76042 | 3 | Pchat tab appears on Jabber even when it is not provisioned on
                                 the jabber-config.xml file. |
| CSCvj58896 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after
                                 transfer. |
| CSCvj58894 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after
                                 hold/resume. |
| CSCvi49056 | 3 | Directory search takes 5 seconds due to inaccurate search
                                 filter. |
| CSCvm83363 | 3 | First login to redirected Expressway cluster fails. |
| CSCve40856 | 3 | Desktop share button is grayed out during a call(BFCP) via
                                 MRA. |
| CSCvk79498 | 3 | Jabber crashed in
                                 HubWindowPlugin!TabButtonItem::CalculateImageSize. |
| CSCvn36100 | 3 | Jabber for windows Automatic update fails in phone mode. |
| CSCvn59476 | 3 | Peer-to-Peer file transfer causes Blank Chat IM session
                                 Jabber-Windows. |
| CSCvm85272 | 3 | Jabber "All Rooms" tab does not load Jabber-windows. |
| CSCvm84307 | 3 | MSVCR120.dll missing error pop-ups always when Jabber is launched
                                 Jabber-Windows. |
| CSCvm5498 | 3 | Jabber stuck when enabling audio-ducking Jabber-Windows. |
| CSCvk23475 | 3 | Evaluation of Jabber-windows for OpenSSL Jan 2018
                                 Jabber-Windows. |
| CSCvh29610 | 3 | Switch front and rear camera Surface, the memory leak detects
                                 each time Jabber-Windows. |
| CSCvk48738 | 4 | Jabber for Windows user authentication with IM&P does not
                                 time out. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvw96073 | 1 | Cisco Jabber for Windows Arbitrary Program Execution
                                 Vulnerability |
| CSCvw96075 | 3 | Cisco Jabber for Windows Information Disclosure
                                 Vulnerability |
| CSCvw96079 | 3 | Cisco Jabber for Windows Denial of Service Vulnerability |
| CSCvx43270 | 2 | Improper Handling of Null Characters when Parsing
                                 Certificate |
| CSCvx36438 | 3 | CEF Network Restriction Bypasses |
| CSCvx36433 | 3 | Jabber Client Robot Message Cross-Site Scripting |
| CSCvx36425 | 2 | Run Arbitrary Commands via window.open |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvo06329 | 3 | File transfer takes long time or times out unless we disable virtual
                              NICs. |
| CSCvn82915 | 3 | Jabber causing high CPU usage and log looping over SSL_read() when
                              connected of MRA. |
| CSCvn75790 | 3 | Click to call options not using set language preference. |
| CSCvn75531 | 3 | J4W: VLC/Media Player releases PAUSE automatically after we End
                              Jabber call. |
| CSCvm54982 | 3 | Jabber stuck when enabling audio-ducking. |
| CSCvk79711 | 3 | No external contact indicator in teams room sometimes due to server
                              ratelimit in team messaging mode. |
| CSCvn59281 | 3 | ALL-LANG: Jabber Win: Strings '20 minutes', '1 hour', '8 hours', '24
                              hours' appear in English in team messaging mode. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvv88490 | 1 | Cisco Jabber Cross-Site Scripting leading to RCE |
| CSCvv88491 | 3 | Cisco Jabber Password Hash Stealing Information Disclosure |
| CSCvv88492 | 2 | Cisco Jabber Custom Protocol Handler Command Injection |
| CSCvw38030 | 1 | Jabber Client Empty a Tags Not Processed by the Hyperlink Replacer
                                 Leads to XSS |
| CSCvw39218 | 3 | Jabber Client Clickjacking |
| CSCvw39231 | 3 | Jabber Client Javascript Functions for Downloading and Opening Files
                                 Need No Confirmation |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvu71173 | 2 | Cisco Jabber for Windows Message Handling Arbitrary Code Execution Vulnerability |
| CSCvu71180 | 2 | Jabber Sensitive Data Disclosure through crafted chat message |
| CSCvu71188 | 2 | Jabber Sensitive Data Disclosure Through malicious link |
| CSCvu96368 | 2 | Cisco Jabber for Windows Protocol Handler Command Injection Vulnerability |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvo06329 | 3 | File transfer takes long time or times out unless we disable virtual NICs. |
| CSCvn82915 | 3 | Jabber causing high CPU usage and log looping over SSL_read() when connected of MRA. |
| CSCvn75790 | 3 | Click to call options not using set language preference. |
| CSCvn75531 | 3 | J4W: VLC/Media Player releases PAUSE automatically after we End Jabber call. |
| CSCvm54982 | 3 | Jabber stuck when enabling audio-ducking. |
| CSCvk79711 | 3 | No external contact indicator in teams room sometimes due to server ratelimit in team messaging mode. |
| CSCvn59281 | 3 | ALL-LANG: Jabber Win: Strings '20 minutes', '1 hour', '8 hours', '24 hours' appear in English in team messaging mode. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvn47352 | 2 | Jabber missing Cookie header for Voicemail HTTP requests leading to High CPU on Expressway-C. |
| CSCvn47527 | 2 | Jabber for Windows J4W does not refresh access token in failover scenario when primary node is down. |
| CSCvo05631 | 3 | Jabber falls back to non-batch search if bulkSearch query returns 200 response with no records. |
| CSCvk23475 | 3 | Evaluation of jabber-windows for OpenSSL Jan 2018. |
| CSCvk59161 | 3 | Jabber users FirstName LastName does not resolve correctly, instead it shows "Display Name". |
| CSCvk79611 | 3 | Mute sound setting can't be persistent after restart. |
| CSCvk79616 | 3 | No stop sharing button occasionally after starting desktop sharing. |
| CSCvk79629 | 3 | Equivalent search filter is incorrect at the beginning of jabber launched. |
| CSCvk79635 | 3 | Jabber Does Not Sync 1404 Credentials Even if 2100 Phone Credentials is Obtained. |
| CSCvk79677 | 3 | Jabber crashes at getMixerControlStruct() intermittently. |
| CSCvk79703 | 3 | Jabber 12.5 DTFM RTP packets with incorrect timestamp if using RTP-NTE. |
| CSCvm41653 | 3 | Jabber using cached UDS records for login even when SRV records have changed. |
| CSCvm42226 | 3 | Jabber Feature Configuration Guide for 12.1 Custom Emoticons does not mention High DPI Changes. |
| CSCvm84307 | 3 | MSVCR120.dll missing error pop-ups always when Jabber is launched. |
| CSCvm85272 | 3 | Jabber "All Rooms" tab does not load. |
| CSCvn30437 | 3 | Jabber does not transition from "In a Meeting" to "Away" when user locks PC and meeting ends. |
| CSCvn53649 | 3 | Jabber Windows Intermittently Downloads the Incorrect Contact Photo. |
| CSCvn56005 | 3 | Jabber does not select right Unity Server after CUCM Service Profile change. |
| CSCvn57177 | 3 | Presence not seen for conversation window. |
| CSCvn57714 | 3 | Jabber 12.5 do not automatically select the first contacts in the search result. |
| CSCvn59148 | 3 | MULTI-LANG: Jabber Win: Too narrow button 'Resume' during the call and conference cause truncation. |
| CSCvn59166 | 3 | ALL-LANG: Jabber Win: Options - Meetings: Truncation of 'Add your Webex Meetings account...'. |
| CSCvn59281 | 3 | ALL-LANG: Jabber Win: Strings '20 minutes', '1 hour', '8 hours', '24 hours' appear in English. |
| CSCvn61611 | 3 | ALL-LANG: Jabber Win: Position of the string depends on scaling in Audio and Video tabs from Options. |
| CSCvn63035 | 3 | Email address is empty in the meeting invitation link when start instant meeting. |
| CSCvn68292 | 3 | Meeting can not be launched after Orion meeting is not launched correctly. |
| CSCvn71324 | 3 | Jabber version 12.5 - Screen share quit icon not visible. |
| CSCvn73056 | 3 | Shift+2 opens a search prompt in Jabber chat with Canadian French Keyboard in Windows. |
| CSCvn77523 | 3 | Temp presence becomes incorrect after a call is made to a user with call forwarding set. |
| CSCvn77563 | 3 | Pop up old desktop share dialog when attendee exits desktop share. |
| CSCvn85610 | 3 | Jabber 12.5 Call voicemail button disappears. |
| CSCvn92191 | 3 | [JW MRA] E911 prompt doesn't load correctly after changing user password. |
| CSCvn93528 | 4 | On-Prem J4W Contact card displays non-greyed out Webex Meeting button. |
| CSCvn70683 | 6 | Jabber for Windows 12.5 - minimum chat window size was changed between releases. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvh29610 | 3 | Switch front and rear camera Surface, the memory leak detects each time. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvn25789 | 3 | Multiple "The starts the Space" messages. |
| CSCvm54982 | 3 | Jabber stuck when enabling audio-ducking. |
| CSCvh29610 | 3 | Switch front and rear camera Surface, the memory leak detects each time. |
| CSCvn39038 | 3 | ARA+HEB: call strip will blink when move mouse on. |
| CSCvk79561 | 3 | Cannot disable Click2X function for new Chrome and Firefox through configure key. |
| CSCvm85272 | 3 | Jabber "All Rooms" tab does not load. |
| CSCvm41653 | 3 | Jabber using cached UDS records for login even when SRV records have changed. |
| CSCvk79362 | 3 | Mobile icon should not appear if active client is J4W when both contact's J4W and J4I login. |
| CSCvn45751 | 3 | Jabber "All Rooms" tab does not load. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvm76932 | 2 | Jabber for Windows 12.1.0/12.1.1 Does Not Send setEnableInAMeetingStatus update to CUCM. |
| CSCvm84307 | 3 | MSVCR120.dll missing error pop-ups always when Jabber is launched. |
| CSCve40856 | 3 | Desktop share button is grayed out during a call(BFCP) via MRA. |
| CSCvj58896 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after transfer. |
| CSCvm82911 | 3 | Jabber attribute mapping should not be case sensitive. |
| CSCvi49056 | 3 | Directory search takes 5 seconds due to inaccurate search filter. |
| CSCvn17374 | 3 | Jabber sending https request to loginp.webexconnect.com overwhelming IDP. |
| CSCvm44162 | 3 | Jabber tries to reconnect while get 403 error response from Cisco Unity Connection. |
| CSCvm69959 | 3 | Jabber for Windows Does Not Remember previous Locations when matching mode is MacAddressWithSubnet. |
| CSCvm83363 | 3 | First login to redirected Expressway cluster fails. |
| CSCvm76042 | 3 | Pchat tab appears on Jabber even when it is not provisioned on the jabber-config.xml file. |
| CSCvj26171 | 3 | Input of Unicode characters on search box on Windows 10 results in invalid data. |
| CSCvk79417 | 3 | CUCM cannot parse crypto capabilities provided by Jabber in SDP of last 200OK message. |
| CSCvj58894 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after hold/resume. |
| CSCvm51685 | 3 | Jabber steals focus when receiving chat notification. |
| CSCvn04975 | 3 | Google Calendar integration does not work in Jabber. |
| CSCvm68457 | 3 | Jabber for Windows Crashes on Voicemail Plugin from Windows 7. |
| CSCvn05357 | 3 | Non-member disappears from admin's participant list after being muted. |
| CSCvn36100 | 3 | Jabber for windows Automatic update fails in phone mode. |
| CSCvk48738 | 4 | Jabber for Windows user authentication with IM&P does not time out. |