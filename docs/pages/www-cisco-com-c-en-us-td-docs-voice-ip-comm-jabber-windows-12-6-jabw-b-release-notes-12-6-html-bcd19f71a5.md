---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-windows-12-6-jabw-b-release-notes-12-6-html-bcd19f71a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Windows/12_6/jabw-b-release-notes-12-6.html
retrieved_at: 2026-08-21T06:56:03.279036+00:00
---

Release Notes for Cisco Jabber for Windows 12.6

# Release Notes for Cisco Jabber for Windows 12.6

First Published: April 9, 2019

Last Updated: May 31, 2021

# Jabber End-User Content on Cisco Webex Help Center

You can find information on the Jabber client at https://help.webex.com/ld-n1uv5wq-CiscoJabber/Jabber . The
               Help Center contains articles on using Jabber features. You can provide feedback on
               individual articles or request new articles through the Help Center.

The Help Center search includes a set of filters to narrow your results by product, release, activities, operating system,
               and other categories.

## Build Number for 12.6

Version

Build Number

12.6(6)

12.6.6.57309 Build 307309

12.6(5)

12.6.5.39930 Build 289930

12.6(4)

12.6.4.39721 Build 289721

12.6(3)

12.6.3.39417 build 289417

12.6(2)

12.6.2.38119

12.6(1)

12.6.1.34405

12.6

12.6.0.31246

## Security Advisories

You can find information on the latest security advisories at https://tools.cisco.com/security/center/publicationListing.x .

## What's New in Release 12.6(5)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.6(4)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.6(3)

This maintenance release contains security updates. See the Caveats for details.

## What's New in Cisco Jabber for Windows 12.6(2)

### New Parameter—BrowserEngineForCustomTab

Applies to Cisco Jabber for Windows

Jabber uses Chrome as the default browser engine for custom tabs. But, the Chrome engine might not work well in some deployments.

In Release 12.6(2) and later, you can choose the browser engine for custom tabs with BrowserEngineForCustomTab . The allowed values are:

Chrome (default)—Use Chrome as the browser engine for custom tabs.

IE—Use IE as the browser engine for custom tabs.

Example: <BrowserEngineForCustomTab>Chrome</BrowserEngineForCustomTab>

### Resolved Caveats

This release provides fixes for a number of known issues. See the Resolved Caveats 12.6(2) section for a list of caveats fixed
                     in this release.

## What's New in Cisco Jabber for Windows 12.6(1)

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

## What's New in Cisco Jabber for Windows 12.6

### Jabber Team Messaging Mode

This feature was released in 12.5 as a preview, and in 12.6, we are happy to announce it is a fully supported feature, with
                     support on mobile clients now also added.

Upgrade Profiles —You can create upgrade profiles on the Webex Control Hub for individual users. Use the upgrade profiles to control which
                     version of Jabber team messaging mode your users are on. For more information about setting up upgrade profiles, see how to Add Upgrade Profiles in the Webex Control Hub in Cloud and Hybrid Deployments for Cisco Jabber 12.6 .

Search on CI, UDS and LDAP —Users with Jabber team messaging mode can now search for contacts and their profiles from the company directory (on UDS/LDAP),
                     even if the contact is not in the CI. With the search results, you'll see the person's profile picture, and be able to call
                     them. To define the scope of contacts search, CI-only search is the default behavior. For more information, check out the ContactProfileSource and ContactSearchSource parameters in the Parameters Reference Guide for Cisco Jabber 12.6.

### Meetings

Meeting Controls for Video Device-Enabled Webex Meetings —Users can join Cisco Collaboration Meeting Rooms from Jabber, where they can see the participant list, change the video layout,
                     lock and record the meeting, mute, unmute, and remove participants, and assign host privileges. Jabber supports using PIN
                     numbers to access video device-enabled Webex meetings.

ActiveControl Support Over the MRA Expressway —ActiveControl is accessible to users who are outside of the corporate network by using the Expressway for Mobile and Remote
                     Access (MRA). Using ActiveControl over MRA is done using SIP oAuth or CAPF enrollment. For environments without secure phones,
                     users can now authenticate to the network using their username and password when moving onto MRA.

For information about setting up ActiveControl, see Feature Configuration for Cisco Jabber 12.6.

Improved Video Resolution —Jabber now supports HD video at 1080p/30FPS bidirectionally (transmit/receive) at the same time. The CPU must be Intel Core
                     i5 or later, with a bandwidth of between 2 and 4 Mbps.

Keypad Support —When users go to their Call tab in Jabber, a keypad is now available for them to use to make a call using their mouse, if they don't want to use their
                     keyboard for the the Search or Call bar.

On-Premises Proximity and Wireless Screen Sharing —Users can now share their screen with this on-premises proximity feature to share the screen from their computers on a video
                     device using ultrasound. If the Auto-connection toggle is on, the Jabber client will connect automatically to a nearby video
                     device. Supported devices include Cisco MX, SX, DX, IX, and the Cisco Webex Room Series.

This feature is on by default. To turn it off, change the EnableProximity parameter to false . For more information about the parameter, see the Parameters Reference Guide for Cisco Jabber 12.6 .

### Feature Improvements

Interoperability For Jabber and Webex Teams —We have improved the experience for Webex Messenger users who are enabled for interoperability between Cisco Jabber and Cisco
                     Webex Teams. When users who have been using Cisco Webex Teams sign back in to Jabber after a period being offline, they will
                     no longer get an alert telling them that new messages are available in Webex Teams, with a link to the Webex Teams web client.
                     Instead, they will receive their new messages in Jabber for their missed one-to-one conversations.

To enable this feature, see how to Set Up Interoperability for Cisco Webex Teams and Jabber .

Save Chat History to Office 365 —We've added support for modern authentication with Office 365, which means that users can save their Jabber chat history
                     to cloud-based Exchange servers. For more information on setting this up, see the Chat History in Microsoft Outlook section in Feature Configuration for Cisco Jabber 12.6 .

Spam Prevention —We’ve enhanced the privacy settings available for users in Cisco Webex Messenger deployments. Users can choose to block incoming
                     messages globally and add trusted contacts or domains to their allow list.

Hide Persistent Chat Room Members —Jabber now supports a setting in Cisco Unified Communications Manager that lets you decide whether members and administrators
                     of a persistent chat room are listed in the room even when they don't have the chat window open. Changes to this setting apply
                     only to restricted rooms that are created after the change has been made. For more information, see the Persistent Chat Rooms section in Feature Configuration for Cisco Jabber 12.6 .

UDS Failover —If your Cisco Unified Communications Manager User Data Service - UDS1(UCM1) - server becomes unavailable, Jabber can now
                     dynamically failover to the UDS2(UCM2) server for contact resolution and search. For more information, see Planning Guide for Cisco Jabber 12.6 .

High Contrast Mode —Jabber now supports some of the Windows system high contrast modes. We support these modes:

High Contrast #1

High Contrast #2

High Contrast Black

When users enable high contrast mode on Windows, Jabber runs in high contrast mode. This mode shows sharper contrast of colors
                     to improve use for visually impaired users. Supported on Windows 10, 8, 8.1, and 7.

Support for Special Characters —Jabber now supports special characters in usernames during sign in.

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

For more information, select Help at the top right of
                                    the Bug Search page.

### Resolved caveats in 12.6(6)

CSCwc24382

Cisco Jabber Security Vulnerability: XMPP Stanza Smuggling with stream:stream tag

### Open Caveats in 12.6(4)

### Resolved Caveats in 12.6(5)

### Open Caveats in 12.6(4)

Identifier

Severity

Headline

CSCvq85116

2

Jabber spell check breaks when detecting multiple grammatical
                                    Errors

CSCvp28473

3

Jabber doesn't play 300 milliseconds of initial audio in the
                                    Whisper announcement (UCCE feature)

CSCvp40099

3

Flickering conference video in Jabber for Windows with RTL
                                    locale

CSCvp40120

3

Participant list not displayed for conference in Jabber for
                                    Windows with RTL locale

CSCvp64715

3

Jabber can not login after webex messager server is migrated

CSCvq11501

3

Jabber for Windows J4W does not refresh access token in failover
                                    scenario over MRA

CSCvq65042

3

JDV 4.1.8 msidriver.sys has expired certificate signature

CSCvq81886

3

Jabber sometimes does not show last message, have to scroll down
                                    to see it

### Resolved Caveats in 12.6(4)

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

### Resolved Caveats in Release 12.6(3)

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

### Open Caveats in Release 12.6(2)

Identifier

Severity

Headline

CSCvq85116

2

Jabber spell check breaks when detecting multiple grammatical Errors

CSCvp28473

3

Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature)

CSCvp40099

3

Flickering conference video in Jabber for Windows with RTL locale

CSCvp40120

3

Participant list not displayed for conference in Jabber for Windows with RTL locale

CSCvp64715

3

Jabber can not login after webex messager server is migrated

CSCvq11501

3

Jabber for Windows J4W does not refresh access token in failover scenario over MRA

CSCvq65042

3

JDV 4.1.8 msidriver.sys has expired certificate signature

CSCvq81886

3

Jabber sometimes does not show last message, have to scroll down to see it

### Resolved Caveats in Release 12.6(2)

Identifier

Severity

Headline

CSCvo55994

2

Cisco Jabber for Windows DLL Preloading Vulnerability

CSCvk79826

3

No close button (x) to remove one chat session sometimes when there are multiple chats ongoing

CSCvp61478

3

Jabber in Phone Mode doesn't show Display Name correctly in flexible JID deployment

CSCvq05352

3

Jabber Windows 12.6 Crash when video source changes from JPEG to YUV2

CSCvq12459

3

Jabber for Windows in Team Messaging mode does not show alert when new messages come in

CSCvq12982

3

Jabber do not show green dial button after entering dialstring followed by pin

CSCvq14897

3

Cisco Jabber has stopped working when accessing certain custom Tab url

CSCvq26619

3

Jabber Windows Fast Login option causing intermittent re-registrations on CUCM and 50003 error

CSCvq27867

3

Previously added enterprise group randomly do not show up after Jabber login

CSCvq27976

3

Jabber bot element <text> or <textarea> cannot enter character w

CSCvq28387

3

Jabber embedded browser for custom tab cannot open document without downloading it

CSCvq29452

3

Persistent Chatroom participant names are not resolved in chatroom open conversation

CSCvq32671

3

Jabber for Windows 12.x CTRL+C "space" causes crash

CSCvq44837

3

Users getting an error "Your message could not be delivered because the contact is offline"

CSCvq48567

3

Join button translation has wrong position in German locale - "lnehmen" insted of "Teilnehmen"

CSCvq63542

3

Jabber for windows unable to play video from custom tab

CSCvq71477

3

Number of files in Photo Cache folder is growing over time

CSCvq73525

3

Unable to delete custom status in Hebrew

CSCvq73610

3

Micro call control window is not sticky if it is moved

CSCvq74681

3

Jabber for Windows 12.6.1 crashes on either sign out or exit application

CSCvq80101

3

Jabber Windows 12.6 Crash due to thread deadlock

CSCvq88433

3

Jabber is unable to save your chats due to OpenClipboard failure

CSCvq90517

3

Unable to add directory group if IM and Presence are disabled on IM&P server

CSCvm49708

4

Jabber usage of expired access_tokens for UDS requests causes 401 errors in CUCM

CSCvq68390

4

Jabber dock window always appears at a different screen position after sign out then sign in

CSCvq91464

6

Jabber 12.6 dock window hides vm notification by default

### Open Caveats in Release 12.6(1)

CSCvo55994

2

Cisco Jabber for Windows DLL Preloading Vulnerability

### Resolved Caveats in Release 12.6(1)

CSCvq67238

3

Jabber 12.6.0 Choppy audio when calling CWMS

### Open Caveats in Release 12.6

CSCvo55994

2

Cisco Jabber for Windows DLL Preloading Vulnerability

### Resolved Caveats in Release 12.6

3

Jabber for Windows randomly sending UDS bulk search query in a loop causing high CPU in CUCM tomcat.

### This Document Applies to These Products

- Jabber for Windows

| Version | Build Number |
|---|---|
| 12.6(6) | 12.6.6.57309 Build 307309 |
| 12.6(5) | 12.6.5.39930 Build 289930 |
| 12.6(4) | 12.6.4.39721 Build 289721 |
| 12.6(3) | 12.6.3.39417 build 289417 |
| 12.6(2) | 12.6.2.38119 |
| 12.6(1) | 12.6.1.34405 |
| 12.6 | 12.6.0.31246 |

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
| CSCvq85116 | 2 | Jabber spell check breaks when detecting multiple grammatical
                                    Errors |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the
                                    Whisper announcement (UCCE feature) |
| CSCvp40099 | 3 | Flickering conference video in Jabber for Windows with RTL
                                    locale |
| CSCvp40120 | 3 | Participant list not displayed for conference in Jabber for
                                    Windows with RTL locale |
| CSCvp64715 | 3 | Jabber can not login after webex messager server is migrated |
| CSCvq11501 | 3 | Jabber for Windows J4W does not refresh access token in failover
                                    scenario over MRA |
| CSCvq65042 | 3 | JDV 4.1.8 msidriver.sys has expired certificate signature |
| CSCvq81886 | 3 | Jabber sometimes does not show last message, have to scroll down
                                    to see it |

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
| CSCvq85116 | 2 | Jabber spell check breaks when detecting multiple grammatical Errors |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature) |
| CSCvp40099 | 3 | Flickering conference video in Jabber for Windows with RTL locale |
| CSCvp40120 | 3 | Participant list not displayed for conference in Jabber for Windows with RTL locale |
| CSCvp64715 | 3 | Jabber can not login after webex messager server is migrated |
| CSCvq11501 | 3 | Jabber for Windows J4W does not refresh access token in failover scenario over MRA |
| CSCvq65042 | 3 | JDV 4.1.8 msidriver.sys has expired certificate signature |
| CSCvq81886 | 3 | Jabber sometimes does not show last message, have to scroll down to see it |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvo55994 | 2 | Cisco Jabber for Windows DLL Preloading Vulnerability |
| CSCvk79826 | 3 | No close button (x) to remove one chat session sometimes when there are multiple chats ongoing |
| CSCvp61478 | 3 | Jabber in Phone Mode doesn't show Display Name correctly in flexible JID deployment |
| CSCvq05352 | 3 | Jabber Windows 12.6 Crash when video source changes from JPEG to YUV2 |
| CSCvq12459 | 3 | Jabber for Windows in Team Messaging mode does not show alert when new messages come in |
| CSCvq12982 | 3 | Jabber do not show green dial button after entering dialstring followed by pin |
| CSCvq14897 | 3 | Cisco Jabber has stopped working when accessing certain custom Tab url |
| CSCvq26619 | 3 | Jabber Windows Fast Login option causing intermittent re-registrations on CUCM and 50003 error |
| CSCvq27867 | 3 | Previously added enterprise group randomly do not show up after Jabber login |
| CSCvq27976 | 3 | Jabber bot element <text> or <textarea> cannot enter character w |
| CSCvq28387 | 3 | Jabber embedded browser for custom tab cannot open document without downloading it |
| CSCvq29452 | 3 | Persistent Chatroom participant names are not resolved in chatroom open conversation |
| CSCvq32671 | 3 | Jabber for Windows 12.x CTRL+C "space" causes crash |
| CSCvq44837 | 3 | Users getting an error "Your message could not be delivered because the contact is offline" |
| CSCvq48567 | 3 | Join button translation has wrong position in German locale - "lnehmen" insted of "Teilnehmen" |
| CSCvq63542 | 3 | Jabber for windows unable to play video from custom tab |
| CSCvq71477 | 3 | Number of files in Photo Cache folder is growing over time |
| CSCvq73525 | 3 | Unable to delete custom status in Hebrew |
| CSCvq73610 | 3 | Micro call control window is not sticky if it is moved |
| CSCvq74681 | 3 | Jabber for Windows 12.6.1 crashes on either sign out or exit application |
| CSCvq80101 | 3 | Jabber Windows 12.6 Crash due to thread deadlock |
| CSCvq88433 | 3 | Jabber is unable to save your chats due to OpenClipboard failure |
| CSCvq90517 | 3 | Unable to add directory group if IM and Presence are disabled on IM&P server |
| CSCvm49708 | 4 | Jabber usage of expired access_tokens for UDS requests causes 401 errors in CUCM |
| CSCvq68390 | 4 | Jabber dock window always appears at a different screen position after sign out then sign in |
| CSCvq91464 | 6 | Jabber 12.6 dock window hides vm notification by default |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvo55994 | 2 | Cisco Jabber for Windows DLL Preloading Vulnerability |
| CSCvk79826 | 3 | No close button (x) to remove one chat session sometimes when there are multiple chats ongoing |
| CSCvo60160 | 3 | PRT tool crashes intermittent on a special machine |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature). |
| CSCvp40099 | 3 | Flickering conference video in Jabber for Windows with RTL locale |
| CSCvp40120 | 3 | Participant list not displayed for conference in Jabber for Windows with RTL locale |
| CSCvp42087 | 3 | Collapse selfview string is not localized to Japanese in Cisco Jabber for Windows. |
| CSCvp61809 | 3 | Jabber minimize Self-view Window icon permanently in foreground |
| CSCvp64715 | 3 | jabber can not login after webex messager server is migrated |
| CSCvp71423 | 3 | Jabber for Windows cuts audio when the PC is locked |
| CSCvp98336 | 3 | Jabber in Deskphone mode always shows last dialed number |
| CSCvq05352 | 3 | Jabber Windows 12.6 Crash During Screen Share |
| CSCvm49708 | 4 | Jabber usage of expired access_tokens for UDS requests causes 401 errors in CUCM |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvp26612 | 2 | DTMF digits not transferred in time (within 50ms) |
| CSCvp37226 | 2 | Windows Jabber is crashing when calling from Persistent Chat Room |
| CSCvp67119 | 2 | Jabber for Windows Randomly Crashes with MAPI_E_CALL_FAILED error |
| CSCvp95229 | 2 | Change in DNS/proxy behaviour results in user failing to login in 12.6 |
| CSCvf32185 | 3 | Jabber incorrectly sends DTMF flash event even when peer doesn't support it |
| CSCvk79827 | 3 | Conference capability is not disabled in SRST environment |
| CSCvk79840 | 3 | crash while pop out the filter result window of pchat room |
| CSCvm84172 | 3 | Jabber for Windows does not show hunt pilot information |
| CSCvo70815 | 3 | Jabber sending to SSO token causing 401 at Unity Connection Server |
| CSCvp21166 | 3 | Unable to start group conference from contact list when it only has offline or custom contacts |
| CSCvp31010 | 3 | Jabber for Windows removing local icon file for custom Tab |
| CSCvp34998 | 3 | Accessibility: cannot stop screen share with keyboard |
| CSCvp35299 | 3 | Jabber 12.6 continiously consuming around 30MB/hour with Video Call using Logitech Camera |
| CSCvp35525 | 3 | Jabber in Multiline always initiates conference leg call from selected line |
| CSCvp38288 | 3 | Jabber for Windows reports crash when using Click2Call |
| CSCvp38488 | 3 | Jabber CEF log is not limited in size and has no log rotation |
| CSCvp41347 | 3 | Jabber for Windows 12.6 does not recognize USB headset Logitech Stereo H650e |
| CSCvp44001 | 3 | Unable to receive notification while adding contact without specifying any contact group |
| CSCvp44881 | 3 | Drag chat items to adjust order can't work |
| CSCvp51101 | 3 | Unable to search contacts using comma when backend LDAP server is openLDAP |
| CSCvp57690 | 3 | #NAME? |
| CSCvp57968 | 3 | Jabber not saving a Call forward number destination in history |
| CSCvp59796 | 3 | Wrong focus when clicking search text box in chat window |
| CSCvp60146 | 3 | Jabber Windows crash on WCL Library |
| CSCvp61478 | 3 | Jabber in Phone Mode doesn't show Display Name correctly |
| CSCvp61671 | 3 | Jabber install error \" \"The coded execution cannot proceed because VCRUNTIEM140.dll was not found\" |
| CSCvp69317 | 3 | Jabber auto-save functionality intermittently disappearing in Jabber 12.5. |
| CSCvp70542 | 3 | Jabber crashed when switching wifi network if open the window MediaStatisticsWindow |
| CSCvp74180 | 3 | When deleting multiple PCR it will cause Jabber to crash |
| CSCvp74639 | 3 | Jabber 12.6 fails to call URIs containing webex.com if conference profile applied. |
| CSCvp79096 | 3 | Jabber Multiline is transfering incomming call to Line 2 with Line 1 |
| CSCvp96864 | 3 | Jabber shows shared screen red outline on wrong screen |
| CSCvp98710 | 3 | Jabber users see \"Configuration change detected\" and have to redo logon |
| CSCvq00079 | 3 | BFCP fails because Jabber is not including a floor ID in the FloorRequest |
| CSCvq67238 | 3 | Jabber 12.6.0 Choppy audio when calling CWMS |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvo55994 | 2 | Cisco Jabber for Windows DLL Preloading Vulnerability |
| CSCvp20017 | 2 | Jabber 12.x & 12.5.x Crashes Often After March Microsoft Updates/Patches. |
| CSCva98286 | 3 | "Disable_IM_HIstory" Set to True Nullifies Persistent Chat Notification. |
| CSCvk79746 | 3 | Location notification always pops up even it is ignored. |
| CSCvp13806 | 3 | Jabber for windows: Celebration emoticon is send and receive. |
| CSCvp26612 | 3 | DTMF digits not transferred in time (within 50ms). |
| CSCvk79800 | 3 | Random crash in Sennheiser plugin. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCut40545 | 3 | Calls with 'No Name' are to be logged in Call History. |
| CSCvk79709 | 3 | Contact photoes are not downloaded automatically after inputting ldap credentials. |
| CSCvk79710 | 3 | Mention dropdown menu doesn't show contact photo. |
| CSCvk79711 | 3 | No external contact indicator in teams room sometimes due to server ratelimit. |
| CSCvk79780 | 3 | Location and presence icon should not appear when presence is disabled on server. |
| CSCvn25789 | 3 | Multiple "The starts the Space" messages. |
| CSCvn26123 | 3 | ALL-LANG: Jabber Win: Untranslated strings in the status window. |
| CSCvn59476 | 3 | Peer-to-Peer file transfer causes Blank Chat IM session when multiple large photos are transferred. |
| CSCvn75790 | 3 | Click to call options not using set language preference. |
| CSCvo06329 | 3 | File transfer takes long time or times out unless we disable virtual NICs. |
| CSCvo15653 | 3 | Ability to drag a contact to an active call to initiate a conference. |
| CSCvo15653 | 3 | Jabber 12.5 Drag-and-drop contact to join conference call feature not working. |
| CSCvo19259 | 3 | Jabber could cause high CPU on CUCM after Receiving HTTP 503 from Unity with oAuth 2.0 enabled. |
| CSCvo19758 | 3 | User incorrectly sees presence as "available" instead of "available" with mobile icon. |
| CSCvo21803 | 3 | Network Interface up/down causing Jabber to repeatedly reconnect to Unity Server. |
| CSCvo27145 | 3 | Jabber Win doesn't refresh phone-only display number after directoryuri config change. |
| CSCvo27149 | 3 | Jabber bot HTML formatted messages do not render/work correctly. |
| CSCvo30091 | 3 | Command line installation with switch LOG_DIRECTORY not working. |
| CSCvo30091 | 3 | Command line installation with switch LOG_DIRECTORY not working. |
| CSCvo33578 | 3 | Jabber for Windows randomly sending UDS bulk search query in a loop causing high CPU in CUCM tomcat. |
| CSCvo33844 | 3 | Unable to re-connect Phone server after moving from MRA to VPN (on-prem). |
| CSCvo42444 | 3 | Private room member-list maxes out at seven users. |
| CSCvo44222 | 3 | wapi.login_failed when retrieving jabber conf file from Jabber client Diagnostics. |
| CSCvo46542 | 3 | Jabber Windows Problem Report not saved when file path has Japanese characters (multi-byte). |
| CSCvo48049 | 3 | J4W 12.5.1: Locking PC does NOT change the status to Away. |
| CSCvo57100 | 3 | Jabber crashed on Windows 10 showing error message: "Cisco Jabber appears to be unresponsive." |
| CSCvo58422 | 3 | Jabber not getting JOIN IN WEBEX option when a meeting is made from outlook with Location="@webex" |
| CSCvo70815 | 3 | Jabber sending to SSO token causing 401 at Unity. |
| CSCvo72202 | 3 | Jabber doing delay in reconnect when moving from VPN to MRA network. |
| CSCvo72202 | 3 | Jabber delay in reconnect when moving from VPN to MRA network. |
| CSCvo88091 | 3 | Presence won't change to unavailable for users who added you as temp buddy becomes offline. |
| CSCvo92221 | 3 | Jabber is not prompting for a sign-out to re-login into the new server. |
| CSCvp17557 | 3 | Memory Leak seen with Jabber Video calls. |