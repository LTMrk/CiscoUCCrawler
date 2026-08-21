---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-8-jabw-b-release-notes-128-html-abff7aa5a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_8/jabw_b_release-notes-128.html
retrieved_at: 2026-08-21T06:55:55.013157+00:00
---

Release Notes for Cisco Jabber for Windows 12.8

# Release Notes for Cisco Jabber for Windows 12.8

First Published: January 22, 2020

Last Updated: October 10, 2021

# Jabber End-User Content on Cisco Webex Help Center

You can find information on the Jabber client at https://help.webex.com/ld-n1uv5wq-CiscoJabber/Jabber . The
               Help Center contains articles on using Jabber features. You can provide feedback on
               individual articles or request new articles through the Help Center.

The Help Center search includes a set of filters to narrow your results by product, release, activities, operating system,
               and other categories.

## Build Number

Version

Build Number

12.8(7)

12.8.7.57305 Build 307305

12.8(6)

12.8.6.55855 Build 305855

12.8(5)

12.8.5.55433 Build 305433

12.8(4)

12.8.4.54812 Build 304812

12.8(3)

12.8.3.53968 build 303968

12.8(2)

12.8.2.52982 build 302982

12.8(1)

12.8.1.52494 build 302494

12.8

12.8.0.51973 Build 301973

## What's New in Release 12.8(7)

This maintenance release contains security updates. See the Caveats for details.

## What's New in Release 12.8(6)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

### Security improvement while joining a Webex meeting

To improve security, Jabber now launches the meetings client when joining a Webex
                     meeting.

## What's New in Release 12.8(5)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.8(4)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.8(3)

This maintenance release contains security updates and stability improvements. See the Caveats for details.

## What's New in Release 12.8(2)

This maintenance release contains defect fixes. See the Caveats section for details.

### Disable the Jabber Diagnostic Tool After Installation

In Jabber for Windows releases before 12.8(2), you can only disable the Jabber Diagnostic Tool by installing the client with
                     the DIAGNOSTICSTOOLENABLED installation argument set to false. This release adds the DiagnosticsToolEnabled parameter to enable you to disable the tool in jabber-config.xml . See the Parameter Guide for details.

### Disable the Voicemail Sent Box

Release 12.8 added the option for users to see their sent voicemails. The client makes periodic requests to your server to
                     refresh the Sent box. To eliminate this extra traffic, you can use the new DisableVoicemailSentBox parameter to disable the Sent box. See the Parameter Guide for details.

## What's New in Release 12.8(1)

This Maintenance Release includes only bug fixes. See the caveats lists for details.

## What's New in Release 12.8

### Microsoft Office 2019 Support

We added support for Microsoft Office 2019 desktop applications to Jabber for Windows.

### Call Park Support

We added support for the Call Park feature to the desktop clients. Earlier releases supported Call Park only on the mobile
                     clients.

### Separate Ringtones for Each Line on Multiline

We've enhanced Multiline support and now your users can assign a different ring tone for each of their configured lines. If
                     they don't want audible notification from some lines, they can assign the new silent ring tone.

### Audio Device Priority

You can choose to give newly registered audio devices the highest priority or continue using the current audio device. Jabber
                     only does this when first registering each audio device. Otherwise, Jabber uses the available device with the highest priority
                     in the device priority list. You can change the device priority list in the advanced Audio preferences.

Your administrator can use the HeadsetPreference parameter to specify this behavior, which defaults to putting the newly registered device at the top of the priority list.
                     But, each user can override this option in their Audio preferences.

### IM-only Screen Sharing

If your deployment allows IM-only screen shares, the Screen Share button starts an IM-only screen share when BFCP-based sharing is disabled. When you click the button, Jabber uses BFCP by
                     default. If BFCP is unavailable, Jabber now starts an IM-only screen share. Unlike BFCP shares, you can only share your full
                     screen.

Usually, the IM-only screen share continues until the original call ends. However, if you merge two calls as a conference,
                     any IM-only screen share ends.

If EnableP2PDesktopShare is false, you can’t use IM-only screen shares. In this case, the Screen Share button can't start an IM-only screen share when BFCP shares are unavailable.

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

### Global Shortcut Key for Conversation Window

You can use the new Control+Alt+Z shortcut to open an unread conversation or bring an existing conversation window to the
                     front.

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

Cisco Jabber doesn't support configuration of two lines with same number associated with different partitions.

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

#### Joining Webex Meetings from Jabber

Webex site disclaimers don't appear when you join Webex meetings from Jabber. This limitation applies whether joining from
                        the meeting reminder popup, or by selecting Join in Webex in Jabber.

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

Step 1

To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search .

Step 2

Sign in with your Cisco.com user ID and password.

Step 3

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release.

For more information, select Help at the top right of
                                    the Bug Search page.

### Resolved caveats in 12.8(7)

CSCwc24382

### Open Caveats 12.8(5)

### Resolved Caveats in 12.8(5)

### Open Caveats in 12.8(4)

Identifier

Severity

Headline

### Resolved Caveats in 12.8(4)

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

### Open Caveats in Release 12.8(3)

Identifier

Severity

Headline

### Resolved Caveats in Release 12.8(3)

Identifier

Severity

Headline

### Closed Caveats in Release 12.8(3)

Identifier

Severity

Headline

### Open Caveats in Release 12.8(2)

Identifier

Severity

Headline

CSCvp28473

3

Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature)

CSCvs42313

3

Jabber on windows crashing during RDP screen sharing intermittently

CSCvs44353

3

J4W 12.7.1 crashes in PLT headset plugin dll when launch at Windows startup

CSCvs57616

3

Mute indicator not appear on Jabber call window when pressing mute button on Jabra Evolve 30 II

CSCvs88159

3

Jabber chat formatted incorrectly

CSCvt79915

3

Jabber 12.8.1 can open multiple instances on same PC

CSCvt93560

3

Jabber delays sending UpdateCapabilities CAST message on originating side causing video flapping

CSCvu20056

3

Nonfunctional admit button exposed when connected to CMS meeting

CSCvr25302

6

Photos are not displayed for contacts immediately after adding Directory Group

### Resolved Caveats in Release 12.8(2)

Identifier

Severity

Headline

CSCvt90771

2

Jabber Crashes in taa_h264decb_push_frame() when initiate a video call

CSCvt14775

3

Jabber 12.8 Voicemail notification counter not affected when voicemail is deleted.

CSCvt35528

3

Jabber Cannot find a saved location

CSCvt41136

3

Call history showing incorrect caller name

CSCvt55321

3

Jabber Team Messaging Mode contact migration prompt does not appear

CSCvt58143

3

Jabber doesn't sync sent item with Voicemail while message is composed, replyreply-all or forwarded

CSCvt61271

3

Jabber Windows uses Proxy Server IP as Unity Voicemail IP

CSCvt62545

3

Jabber phone service freezes after clicking on transfer

CSCvt81216

3

J4W is crashing when Polycom camera is being set

CSCvt85597

3

Timestamp is not displayed on some rooms in PChat room list

CSCvt86138

3

Extend and Connect configured RD is not listed under available devices

CSCvt89103

3

[protocol handler] ciscotel has problem to support phone number with space

CSCvt90948

3

Jabber on prem using Teams Message Mode can not connect to cloud account to use share from one drive

CSCvt94588

3

Phone Services are not connecting in IPv6 with Jabber version 12.8.1

CSCvt99050

3

LDAP connection does not reconnect after being restarted

CSCvu05272

3

J4Windows 12.8.1 UI doesn't allow chat to start with some contacts when App dial rules are used

CSCvu08030

3

Jabber 12.8 info disclosure with CTRL-Shift-D Keyboard Shortcut

CSCvu16402

3

Jabber for Windows crash when hide ClearSearchButton

CSCvu20159

3

Jabber 12.8.1 is crashing due to memcpy function in VCRUNTIME140.dll

CSCvt80399

6

Jabber doesn't handle all deleted message events leading to periodic polling and high load on Unity

CSCvu06716

6

Jabber cannot show correct presence on Outlook with 2 IM addresses

### Open Caveats in Release 12.8(1)

Identifier

Severity

Headline

CSCvp28473

3

Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature)

CSCvs42313

3

Jabber on windows crashing during RDP screen sharing intermittently

CSCvs56364

3

Jabber for Windows 12.7.0 crashes due to meeting SSO authentication taking long time for one user

CSCvs57616

3

Mute indicator not appear on Jabber call window when pressing mute button on Jabra Evolve 30 II

CSCvt35528

3

Jabber Cannot find a saved location

CSCvt41136

3

Call history showing incorrect caller name

### Resolved Caveats in Release 12.8(1)

Identifier

Severity

Headline

CSCvs80168

2

Unrecognized user joined a chat group

CSCvs92884

2

Sign-Out / Sign-in to Jabber leading to excessive GET Vmrest Messages call with Voicemail

CSCvp57968

3

Jabber not saving a Call forward number destination in history

CSCvr78421

3

Jabber 12.7 in Modern view opens a new chat after call

CSCvs40169

3

Jabber does not trust certificate for sip-oauth connection with IPv6

CSCvs49239

3

Jabber Windows 12.7.1 Losing Chat History when switching from classic view to modern view

CSCvs57647

3

Local contact in Outlook is not resolved upon incoming call if contact number is with prefix +

CSCvs67713

3

Presence status change to \"away\" immediately after any activity stops on PC

CSCvs74731

3

Jabber crashing when clicking Join Button for meeting

CSCvs79300

3

Active Control (UDT/IX) does not work for call from CMS space to Jabber via CCX

CSCvs88156

3

J4W 'Active Call' icon does not disappear from conversation tab when call ends

CSCvs93497

3

Jabber Doesn't Re-Use Session Cookie when Performing transition from Expressway-VPN switch

CSCvt05408

3

J4W: authenticateError should not be reset upon receipt of other error code.[enableadlockprevention]

CSCvt10285

3

Jabber not caching the Local IP Address on Sign-in or launch leading to re-connect on network event

CSCvt11237

3

Scheduling a meeting from Jabber for Windows is not triggering mail alert for host and participant

CSCvt17608

3

Configuration options not respected on first installation 12.8 Client

CSCvt20164

3

ForwardVoicemail parameter set to false not working

CSCvt22557

3

Unable to use special characters for the call pickup group on Jabber for windows 12.8

CSCvt36045

3

CSCvt37591

3

CSCvt38965

3

CSCvt43585

3

CSCvs42143

5

CSCvg56521

6

CSCvs24544

6

### Open Caveats in Release 12.8

Identifier

Severity

Headline

CSCvs92884

2

Sign-Out / Sign-in to Jabber leading to excessive GET Vmrest Messages call with Voicemail

CSCvp28473

3

Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature).

CSCvs40169

3

Jabber does not trust certificate for sip-oauth connection with IPv6

CSCvs42313

3

jabber on windows crashing during RDP screen sharing intermittently

CSCvs44353

3

J4W 12.7.1 crashes in PLT headset plugin dll when launch at Windows startup

CSCvs56364

3

Jabber for Windows 12.7.0 crashes due to meeting SSO authentication taking long time for one user

CSCvs57616

3

Mute indicator not appear on Jabber call window when pressing mute button on Jabra Evolve 30 II

CSCvs57622

3

Unexpected Cisco headset 532 firmware update prompt when Jabber is launched

CSCvs93497

3

Jabber Doesn't Re-Use Session Cookie when Performing transition from Expressway-VPN switch

CSCvt10285

3

Jabber not caching the Local IP Address on Sign-in or launch leading to re-connect on network event

CSCvs23062

4

"Copy to group" option is missing after editing contact's profile

### Resolved Caveats in Release 12.8

Identifier

Severity

Headline

CSCvr26715

2

Apostrophe character " ' " is showing as "&#39"; in email contact details in Jabber

CSCvr42648

2

Automute function does not work on Jabber for windows 12.5.0 and 12.7

CSCvs48285

2

Jabber did not stop the retry of the user bulk queries failed with code CONNECTION_TIMEOUT_ERROR

CSCvq11501

3

Jabber for Windows J4W does not refresh access token in failover scenario over MRA

CSCvr00981

3

JabberWin - Softphone Doesn't Re-Register When VPN Connection is Changed

CSCvr12341

3

Jabber 12.6 Emoticons window appears behind chat window or does not open at all in VDI environment

CSCvr32378

3

SQLite whereLoopAddBtreeIndex Denial of Service Vulnerability

CSCvr36499

3

OpenSSL ECDSA Remote Timing Attack Vulnerability

CSCvr36509

3

OpenSSL Padding Oracle Information Disclosure Vulnerability

CSCvr61262

3

Jabber csf windows sends headset inventory post to cucm server not in callmanager group

CSCvr75200

3

Call History contacts are not seen till user sign out and then sign in

CSCvr76764

3

Jabber does not trust certificate for sip-oauth connection

CSCvr82874

3

Jabber fails to authenticate BFCP if user id is changed in re-invite

CSCvr86141

3

Jabber error "Jabber stopped working" when moving chat window to external scale monitor

CSCvr87501

3

Race condition with presence statuses on Cisco Jabber for Windows

CSCvs01312

3

Jabber - proximity screen sharing picture is blurred

CSCvs01667

3

Jabber for Windows 12.8 cannot add users to the group chat by calling IM protocol handler

CSCvs07458

3

Jabber crash when a call from a CTI Route Point is answered

CSCvs12048

3

Offline messages appear as "pop-up" but doesn't appear in chat window

CSCvs12504

3

Jabber for Windows 'Your session has expired' on Outlook tab

CSCvs12601

3

Jabber for Windows crashes after performing a transfer

CSCvs15590

3

Crash in enhanced_callcontrol_MD!Udt::Connection::Priv::scheduleUdtTimer

CSCvs20247

3

Jabber for Windows fails to reconnect to voicemail following resume from Sleep

CSCvs20255

3

Jabber for Windows Built-In-Bridge intermittently fails to send audio stream to recorder

CSCvs22917

3

Jabber stop sending video streams after doing a hold and resume from REM browser

CSCvs28158

3

IO read/write issue in VDI environment for pre-download of Webex Meetings client

CSCvs29571

3

Jabber freezes during conference calls because it fails to respond to INVITE

CSCvs31210

3

Trying to stop Screen share during Jabber softphone call causes call to Mute instead of Stop Share

CSCvs31214

3

Jabber audio drop down menu is flickering during a Jabber softphone call

CSCvs47678

3

Cisco Jabber 12.7.1 "Dialpad" showing instead of "Record a Voicemail" button in Voicemail Tab

CSCvs49239

3

Jabber Windows 12.7.1 Losing Chat History when switching from classic view to modern view

CSCvt13830

3

Jabber issue with GetAdaptersAddresses() fail causing voicemail re-connect

CSCvs21185

5

Jabber 12.7 Dark mode - Status popup window request is unreadable

### This Document Applies to These Products

- Jabber for Windows

| Version | Build Number |
|---|---|
| 12.8(7) | 12.8.7.57305 Build 307305 |
| 12.8(6) | 12.8.6.55855 Build 305855 |
| 12.8(5) | 12.8.5.55433 Build 305433 |
| 12.8(4) | 12.8.4.54812 Build 304812 |
| 12.8(3) | 12.8.3.53968 build 303968 |
| 12.8(2) | 12.8.2.52982 build 302982 |
| 12.8(1) | 12.8.1.52494 build 302494 |
| 12.8 | 12.8.0.51973 Build 301973 |

| Note | If EnableP2PDesktopShare is false, you can’t use IM-only screen shares. In this case, the Screen Share button can't start an IM-only screen share when BFCP shares are unavailable. |
|---|---|

| Note | This release note describes a new feature in Webex Control Hub that impacts Jabber deployments. Because it’s a change in Control
                                 Hub, you can access this feature for any release of Jabber. |
|---|---|

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
| Step 3 | To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release. For more information, select Help at the top right of
                                    the Bug Search page. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCwc24382 | 3 | Cisco Jabber Security Vulnerability: XMPP Stanza Smuggling with stream:stream tag |

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
| CSCvu27580 | 2 | BFCP share intermittently fails to stop when user click stop
                                 share button on Jabber |
| CSCvu62704 | 2 | Jabber Windows high CPU usage for large CMS hosted conference
                                 with ActiveControl enabled |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the
                                 Whisper announcement (UCCE feature) |
| CSCvs44353 | 3 | J4W 12.7.1 crashes in PLT headset plugin dll when launch at
                                 Windows startup |
| CSCvs57616 | 3 | Mute indicator not appear on Jabber call window when pressing
                                 mute button on Jabra Evolve 30 II |
| CSCvs88159 | 3 | Jabber chat formatted incorrectly |
| CSCvt79915 | 3 | Jabber 12.8.1 can open multiple instances on same PC |
| CSCvu25845 | 3 | When user joins meeting from Jabber Meeting Pop Up the symbol ( '
                                 ) is added to the URL |
| CSCvu38469 | 3 | Jabber is crashing with error "OpenSSL internal error, assertion
                                 failed: 0" |
| CSCvu40378 | 3 | Jabber for VDI seeing black screen during RDP
                                 automatically |
| CSCvu60143 | 3 | Jabber does not allow leaving Space when right-click 1:1
                                 space |
| CSCvu67532 | 3 | Jabber Install Error: Install fails due to "Sennheiser" folder in
                                 programdata/application |
| CSCvu96763 | 3 | Jabber contact photo refresh for all group chat members |
| CSCvv04594 | 3 | Persistent chat room is displaying as joined even after entering
                                 the wrong password |
| CSCvv17590 | 3 | Contacts are randomly shown as URI instead of Display
                                 Name |
| CSCvv48257 | 3 | both local ringback and remote media are heard if SIP 183 is
                                 followed by 180 |
| CSCvv50578 | 3 | JabberCallHistory is missing:ChangeClientUser shouldn't be
                                 executed w/o 'PresenceDomain' configured |
| CSCvv53586 | 3 | Jabber shows shared screen red outline on wrong screen |
| CSCvr25302 | 6 | Photos are not displayed for contacts immediately after adding
                                 Directory Group |
| CSCvs58596 | 6 | Original Called Number not shown in Jabber Popup when call via
                                 Hunt Group |

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
| CSCvu27580 | 2 | BFCP share intermittently fails to stop when user click stop share button on Jabber |
| CSCvu62704 | 2 | Jabber Windows high CPU usage for large CMS hosted conference with ActiveControl enabled |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature) |
| CSCvs44353 | 3 | J4W 12.7.1 crashes in PLT headset plugin dll when launch at Windows startup |
| CSCvs57616 | 3 | Mute indicator not appear on Jabber call window when pressing mute button on Jabra Evolve 30 II |
| CSCvs88159 | 3 | Jabber chat formatted incorrectly |
| CSCvt79915 | 3 | Jabber 12.8.1 can open multiple instances on same PC |
| CSCvu25845 | 3 | When user joins meeting from Jabber Meeting Pop Up the symbol ( ' ) is added to the URL |
| CSCvu38469 | 3 | Jabber is crashing with error "OpenSSL internal error, assertion failed: 0" |
| CSCvu40378 | 3 | Jabber for VDI seeing black screen during RDP automatically |
| CSCvu60143 | 3 | Jabber does not allow leaving Space when right-click 1:1 space |
| CSCvu67532 | 3 | Jabber Install Error: Install fails due to "Sennheiser" folder in programdata/application |
| CSCvu96763 | 3 | Jabber contact photo refresh for all group chat members |
| CSCvv04594 | 3 | Persistent chat room is displaying as joined even after entering the wrong password |
| CSCvv17590 | 3 | Contacts are randomly shown as URI instead of Display Name |
| CSCvv48257 | 3 | both local ringback and remote media are heard if SIP 183 is followed by 180 |
| CSCvv50578 | 3 | JabberCallHistory is missing:ChangeClientUser shouldn't be executed w/o 'PresenceDomain' configured |
| CSCvv53586 | 3 | Jabber shows shared screen red outline on wrong screen |
| CSCvr25302 | 6 | Photos are not displayed for contacts immediately after adding Directory Group |
| CSCvs58596 | 6 | Original Called Number not shown in Jabber Popup when call via Hunt Group |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvu25647 | 2 | Jabber VDI changes the Status within 1 minute |
| CSCvu33113 | 2 | Jabber does not stop sending CTI request,with invalid access token to CUCM, causing high CPU on CUCM |
| CSCvu64467 | 2 | J4W 12.8.x via AnyConnect VPN is not registering for phone services |
| CSCvu71173 | 2 | Cisco Jabber for Windows Message Handling Arbitrary Code Execution Vulnerability |
| CSCvu71188 | 2 | Jabber Sensitive Data Disclosure Through malicious link |
| CSCvu74172 | 2 | Jabber - Plantronics Savi 700 Headsets Disconnect in Desk Phone Mode w/Accessories Manager Enabled |
| CSCvu96368 | 2 | Cisco Jabber for Windows Protocol Handler Command Injection Vulnerability |
| CSCvu71180 | 2 | Jabber Sensitive Data Disclosure through crafted chat message |
| CSCvt01967 | 3 | cannot control mute button when calling in to a webex meeting without a webex account |
| CSCvu30275 | 3 | Jabber becomes the active window unexpectedly after switching to another app |
| CSCvu37567 | 3 | chat bubble not visible when Jabber calls to CMS cospace |
| CSCvu48152 | 3 | Persistent Chat rooms refresh is timing out as the number of persistent chat rooms increase |
| CSCvu54694 | 3 | Jabber does not blink on taskbar if its in the system tray |
| CSCvu61316 | 3 | Incoming call shows SIP uri instead of number when Jabber is deskphone mode |
| CSCvu61968 | 3 | Jabber 12.8.1.302494 in Teams Mode will disable file sharing and screenshot |
| CSCvu73173 | 3 | ForceLogoutTimer does not clean the Oauth token store |
| CSCvu99870 | 3 | Chat messages from SfB or Lync clients are not rendered by Jabber client intermittently |
| CSCvv04450 | 3 | Alert when available feature doesn't work for temp contact |
| CSCvv04694 | 3 | Refresh icon in persistent chat room is not displaying in High Contrast Mode of CJW |
| CSCvv10379 | 3 | Ldap person record source did not bind successfully after VPN connected |
| CSCvv15165 | 3 | No Line number on the bottom left corner of Jabber window |
| CSCvv45086 | 3 | headset firmware upgrade issue on jabber ver 12.8 |
| CSCvv51458 | 3 | Jabber Meetings Tab missing "Join in Webex" option |
| CSCvu38455 | 3 | J4W crashing with AMX camera |
| CSCvu20056 | 3 | Nonfunctional admit button exposed when connected to CMS meeting |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvs42313 | 3 | Jabber on windows crashing during RDP screen sharing intermittently |
| CSCvt93560 | 6 | Jabber delays sending UpdateCapabilities CAST message on originating side causing video flapping |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature) |
| CSCvs42313 | 3 | Jabber on windows crashing during RDP screen sharing intermittently |
| CSCvs44353 | 3 | J4W 12.7.1 crashes in PLT headset plugin dll when launch at Windows startup |
| CSCvs57616 | 3 | Mute indicator not appear on Jabber call window when pressing mute button on Jabra Evolve 30 II |
| CSCvs88159 | 3 | Jabber chat formatted incorrectly |
| CSCvt79915 | 3 | Jabber 12.8.1 can open multiple instances on same PC |
| CSCvt93560 | 3 | Jabber delays sending UpdateCapabilities CAST message on originating side causing video flapping |
| CSCvu20056 | 3 | Nonfunctional admit button exposed when connected to CMS meeting |
| CSCvr25302 | 6 | Photos are not displayed for contacts immediately after adding Directory Group |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvt90771 | 2 | Jabber Crashes in taa_h264decb_push_frame() when initiate a video call |
| CSCvt14775 | 3 | Jabber 12.8 Voicemail notification counter not affected when voicemail is deleted. |
| CSCvt35528 | 3 | Jabber Cannot find a saved location |
| CSCvt41136 | 3 | Call history showing incorrect caller name |
| CSCvt55321 | 3 | Jabber Team Messaging Mode contact migration prompt does not appear |
| CSCvt58143 | 3 | Jabber doesn't sync sent item with Voicemail while message is composed, replyreply-all or forwarded |
| CSCvt61271 | 3 | Jabber Windows uses Proxy Server IP as Unity Voicemail IP |
| CSCvt62545 | 3 | Jabber phone service freezes after clicking on transfer |
| CSCvt81216 | 3 | J4W is crashing when Polycom camera is being set |
| CSCvt85597 | 3 | Timestamp is not displayed on some rooms in PChat room list |
| CSCvt86138 | 3 | Extend and Connect configured RD is not listed under available devices |
| CSCvt89103 | 3 | [protocol handler] ciscotel has problem to support phone number with space |
| CSCvt90948 | 3 | Jabber on prem using Teams Message Mode can not connect to cloud account to use share from one drive |
| CSCvt94588 | 3 | Phone Services are not connecting in IPv6 with Jabber version 12.8.1 |
| CSCvt99050 | 3 | LDAP connection does not reconnect after being restarted |
| CSCvu05272 | 3 | J4Windows 12.8.1 UI doesn't allow chat to start with some contacts when App dial rules are used |
| CSCvu08030 | 3 | Jabber 12.8 info disclosure with CTRL-Shift-D Keyboard Shortcut |
| CSCvu16402 | 3 | Jabber for Windows crash when hide ClearSearchButton |
| CSCvu20159 | 3 | Jabber 12.8.1 is crashing due to memcpy function in VCRUNTIME140.dll |
| CSCvt80399 | 6 | Jabber doesn't handle all deleted message events leading to periodic polling and high load on Unity |
| CSCvu06716 | 6 | Jabber cannot show correct presence on Outlook with 2 IM addresses |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature) |
| CSCvs42313 | 3 | Jabber on windows crashing during RDP screen sharing intermittently |
| CSCvs56364 | 3 | Jabber for Windows 12.7.0 crashes due to meeting SSO authentication taking long time for one user |
| CSCvs57616 | 3 | Mute indicator not appear on Jabber call window when pressing mute button on Jabra Evolve 30 II |
| CSCvt35528 | 3 | Jabber Cannot find a saved location |
| CSCvt41136 | 3 | Call history showing incorrect caller name |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvs80168 | 2 | Unrecognized user joined a chat group |
| CSCvs92884 | 2 | Sign-Out / Sign-in to Jabber leading to excessive GET Vmrest Messages call with Voicemail |
| CSCvp57968 | 3 | Jabber not saving a Call forward number destination in history |
| CSCvr78421 | 3 | Jabber 12.7 in Modern view opens a new chat after call |
| CSCvs40169 | 3 | Jabber does not trust certificate for sip-oauth connection with IPv6 |
| CSCvs49239 | 3 | Jabber Windows 12.7.1 Losing Chat History when switching from classic view to modern view |
| CSCvs57647 | 3 | Local contact in Outlook is not resolved upon incoming call if contact number is with prefix + |
| CSCvs67713 | 3 | Presence status change to \"away\" immediately after any activity stops on PC |
| CSCvs74731 | 3 | Jabber crashing when clicking Join Button for meeting |
| CSCvs79300 | 3 | Active Control (UDT/IX) does not work for call from CMS space to Jabber via CCX |
| CSCvs88156 | 3 | J4W 'Active Call' icon does not disappear from conversation tab when call ends |
| CSCvs93497 | 3 | Jabber Doesn't Re-Use Session Cookie when Performing transition from Expressway-VPN switch |
| CSCvt05408 | 3 | J4W: authenticateError should not be reset upon receipt of other error code.[enableadlockprevention] |
| CSCvt10285 | 3 | Jabber not caching the Local IP Address on Sign-in or launch leading to re-connect on network event |
| CSCvt11237 | 3 | Scheduling a meeting from Jabber for Windows is not triggering mail alert for host and participant |
| CSCvt17608 | 3 | Configuration options not respected on first installation 12.8 Client |
| CSCvt20164 | 3 | ForwardVoicemail parameter set to false not working |
| CSCvt22557 | 3 | Unable to use special characters for the call pickup group on Jabber for windows 12.8 |
| CSCvt36045 | 3 | J4W - Toolbar Buttons are cutting in half during Jabber video call in full screen |
| CSCvt37591 | 3 | RDP sharing from call control strip should allow to choose screen |
| CSCvt38965 | 3 | Chat conversations should be kept regardless of 'Remember my open conversations' in modern UI |
| CSCvt43585 | 3 | Jabber 12.7.1 call settings - device for calls returns to use my computer after signing out and in |
| CSCvs42143 | 5 | Contact images are duplicated when last name returns multiple matches. |
| CSCvg56521 | 6 | Enhancement: J4W-No notification or re-signing after password expired and changed in LDAP |
| CSCvs24544 | 6 | need to disable Join across line on Jabber 12.7.1 |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvs92884 | 2 | Sign-Out / Sign-in to Jabber leading to excessive GET Vmrest Messages call with Voicemail |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature). |
| CSCvs40169 | 3 | Jabber does not trust certificate for sip-oauth connection with IPv6 |
| CSCvs42313 | 3 | jabber on windows crashing during RDP screen sharing intermittently |
| CSCvs44353 | 3 | J4W 12.7.1 crashes in PLT headset plugin dll when launch at Windows startup |
| CSCvs56364 | 3 | Jabber for Windows 12.7.0 crashes due to meeting SSO authentication taking long time for one user |
| CSCvs57616 | 3 | Mute indicator not appear on Jabber call window when pressing mute button on Jabra Evolve 30 II |
| CSCvs57622 | 3 | Unexpected Cisco headset 532 firmware update prompt when Jabber is launched |
| CSCvs93497 | 3 | Jabber Doesn't Re-Use Session Cookie when Performing transition from Expressway-VPN switch |
| CSCvt10285 | 3 | Jabber not caching the Local IP Address on Sign-in or launch leading to re-connect on network event |
| CSCvs23062 | 4 | "Copy to group" option is missing after editing contact's profile |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvr26715 | 2 | Apostrophe character " ' " is showing as "&#39"; in email contact details in Jabber |
| CSCvr42648 | 2 | Automute function does not work on Jabber for windows 12.5.0 and 12.7 |
| CSCvs48285 | 2 | Jabber did not stop the retry of the user bulk queries failed with code CONNECTION_TIMEOUT_ERROR |
| CSCvq11501 | 3 | Jabber for Windows J4W does not refresh access token in failover scenario over MRA |
| CSCvr00981 | 3 | JabberWin - Softphone Doesn't Re-Register When VPN Connection is Changed |
| CSCvr12341 | 3 | Jabber 12.6 Emoticons window appears behind chat window or does not open at all in VDI environment |
| CSCvr32378 | 3 | SQLite whereLoopAddBtreeIndex Denial of Service Vulnerability |
| CSCvr36499 | 3 | OpenSSL ECDSA Remote Timing Attack Vulnerability |
| CSCvr36509 | 3 | OpenSSL Padding Oracle Information Disclosure Vulnerability |
| CSCvr61262 | 3 | Jabber csf windows sends headset inventory post to cucm server not in callmanager group |
| CSCvr75200 | 3 | Call History contacts are not seen till user sign out and then sign in |
| CSCvr76764 | 3 | Jabber does not trust certificate for sip-oauth connection |
| CSCvr82874 | 3 | Jabber fails to authenticate BFCP if user id is changed in re-invite |
| CSCvr86141 | 3 | Jabber error "Jabber stopped working" when moving chat window to external scale monitor |
| CSCvr87501 | 3 | Race condition with presence statuses on Cisco Jabber for Windows |
| CSCvs01312 | 3 | Jabber - proximity screen sharing picture is blurred |
| CSCvs01667 | 3 | Jabber for Windows 12.8 cannot add users to the group chat by calling IM protocol handler |
| CSCvs07458 | 3 | Jabber crash when a call from a CTI Route Point is answered |
| CSCvs12048 | 3 | Offline messages appear as "pop-up" but doesn't appear in chat window |
| CSCvs12504 | 3 | Jabber for Windows 'Your session has expired' on Outlook tab |
| CSCvs12601 | 3 | Jabber for Windows crashes after performing a transfer |
| CSCvs15590 | 3 | Crash in enhanced_callcontrol_MD!Udt::Connection::Priv::scheduleUdtTimer |
| CSCvs20247 | 3 | Jabber for Windows fails to reconnect to voicemail following resume from Sleep |
| CSCvs20255 | 3 | Jabber for Windows Built-In-Bridge intermittently fails to send audio stream to recorder |
| CSCvs22917 | 3 | Jabber stop sending video streams after doing a hold and resume from REM browser |
| CSCvs28158 | 3 | IO read/write issue in VDI environment for pre-download of Webex Meetings client |
| CSCvs29571 | 3 | Jabber freezes during conference calls because it fails to respond to INVITE |
| CSCvs31210 | 3 | Trying to stop Screen share during Jabber softphone call causes call to Mute instead of Stop Share |
| CSCvs31214 | 3 | Jabber audio drop down menu is flickering during a Jabber softphone call |
| CSCvs47678 | 3 | Cisco Jabber 12.7.1 "Dialpad" showing instead of "Record a Voicemail" button in Voicemail Tab |
| CSCvs49239 | 3 | Jabber Windows 12.7.1 Losing Chat History when switching from classic view to modern view |
| CSCvt13830 | 3 | Jabber issue with GetAdaptersAddresses() fail causing voicemail re-connect |
| CSCvs21185 | 5 | Jabber 12.7 Dark mode - Status popup window request is unreadable |