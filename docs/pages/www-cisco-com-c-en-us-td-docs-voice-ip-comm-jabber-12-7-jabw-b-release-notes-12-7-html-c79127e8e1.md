---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-7-jabw-b-release-notes-12-7-html-c79127e8e1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_7/jabw_b_release-notes-12-7.html
retrieved_at: 2026-08-21T06:55:59.058026+00:00
---

Release Notes for Cisco Jabber for Windows 12.7

# Release Notes for Cisco Jabber for Windows 12.7

First Published: September 9, 2019

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

12.7(6)

12.7.6.57310 Build 307310

12.7(5)

12.7.5.55797 Build 305797

12.7(4)

12.7.4.55432 Build 305432

12.7(3)

12.7.3.54811 Build 304811

12.7(2)

12.7.2.53984 build 303984

12.7(1)

12.7.1.51081

12.7

12.7.0.38632

## Security Advisories

You can find information on the latest security advisories at https://tools.cisco.com/security/center/publicationListing.x .

## What's New in Release 12.7(5)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

### Security improvement while joining a Webex meeting

To improve security, Jabber now launches the meetings client when joining a Webex
                     meeting.

## What's New in Release 12.7(4)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.7(3)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.7(2)

This maintenance release contains security updates. See the Caveats for details.

## What's New in Release 12.7(1)

### Resolved Caveats

This release provides fixes for a number of known issues. See the Resolved Caveats 12.7(1) section for a list of caveats fixed
                     in this release.

## What's New in Release 12.7

### Improved User Experience

#### Modern Design

We improved the user experience in this release with a new Modern Design. The Modern Design features a single-window UI. Jabber
                        defaults to the Modern Design in all deployments. Users in on-premises and Webex Messenger deployments can choose to use the
                        Classic Design.

Jabber Team Messaging Mode only supports the Modern Design view. Users cannot choose the Classic Design in Jabber Team Messaging
                        Mode.

If you want your on-premises or Webex Messenger deployment to default to the Classic Design, you can set the default with
                        the UXModel parameter. The allowed values are Modern (the default) and Classic . Each user's preference takes precedence over this parameter. For details, see the Parameters Reference Guide for Cisco Jabber .

Users can also customize their app by choosing their preferred design in Settings > Appearances .

#### Themes

We have added themes for the Jabber app. The available themes are:

Default

Dark

We don't support changing the color of chat text in this theme.

High Contrast

Users can switch between the available themes through Settings > Appearances .

#### Improved Prompts for Office 365 Migration

After administrators migrate user accounts to Office 365, users that use Save Chats to Outlook, will receive a message that
                        the account has been migrated and prompted to resubmit their credentials in order to continue using this feature.

#### Accessibility Improvements

We made accessibility improvements throughout the client, including the following:

Screen reader support

Improved the accessibility text for screen readers.

Improved keyboard navigation of the chat history.

Improved control labels.

The information panel announces the currently selected contact or the person with whom you are communicating.

The titles of detached conversations include the contact's name.

Visual improvements

Added a high contrast theme which improves the color contrast and supports larger font sizes.

New shortcut keys

Ctrl + Shift + M—Places focus on the screen share button. You can then choose to stop the share or share a different application.

Ctrl + Shift + N—Provides access to notification messages. This permits keyboard users to answer or decline a call, join meetings,
                                    and manage new locations.

#### Call Progress Indicator for Extend & Connect

When a user makes an outbound call with Extend & Connect, a call window now appears immediately after dialing. If the user
                        does not answer on their mobile device, the call terminates after receiving a PSTN timeout signal.

#### Chat Rooms Maintains Participant List Visibility

We changed participant list behavior for group chats and chat rooms in on-premises and Webex Messenger deployments. Now, when
                        you switch from one chat room to another chat room, it maintains the visibility of the participant list. If you open the participant
                        list in Chat A and then switch to Chat B, the participant list is visible when you return to Chat A.

Person-to-person chats do not behave this way.

#### Display Tab Labels

By default in Release 12.6, the client didn't display tab labels in the hub window. Users can enable tab labels through their
                        preferences.

If you want to change the default behavior for displaying tabs, use the new ShowTabLabel parameter. Each user's preference takes precedence over this parameter. For details, see the Parameters Reference Guide for Cisco Jabber .

### Jabber Team Messaging Mode

#### Configure Clients Through Cisco Webex Control Hub

You can run Jabber Team Messaging Mode in IM-Only Mode which doesn't need Cisco Unified Communications Manager and its calling
                        capabilities. To replace Unified CM as the deployment site for the Jabber configuration file, you can upload your Jabber configuration
                        file to the Control Hub. You can upload one configuration file for each organization.

Go to Services , then select the Message card, and choose Settings . Then, select Upload Configuration File . The file must be in .xml format.

If you have Jabber configuration files in both the Control Hub and Unified CM, the value of a parameter from the Unified CM
                        takes precedence.

#### People Insights

People Insights provides Jabber Team Message Mode users with professional profiles of their contacts. Anywhere a contact card
                        appears, user can access People Insights: contact lists, in conversations, from the call history, and voicemail history.

The feature only displays publicly available information in profiles, and internal company directory information to users
                        in the same company. This internal directory information is not visible to users outside the company. Users can edit their
                        own profiles to add more data. For more information, see What Is People Insights .

To enable People Insights, go to the Control Hub, and select Settings > Directory Synchronization and People Insights and turn on the Show People Insights toggle.

#### Do Not Disturb Setting

We changed the intervals in the Do Not Disturb setting to 30 minutes, 1 hour, 2 hours, 4 hours, 8 hours, and 24 hours.

#### Presence Based on Non-Jabber Activity

In previous releases, Jabber team messaging mode reported users presence based only on their activity in the Jabber app. Jabber
                        now reports your presence based on activity across your computer.

#### Enterprise Content Management (ECM) Support

You can view, send, and receive ECM files. Upload ECM files from OneDrive or SharePoint Online, and send them via chat to
                        other Jabber users who are authorized to view them. When users send attachments, they can choose to upload files from their
                        computer or ECM account. Users can choose to send the files to other people in their organization, or to specific people who
                        have access to the file. When the recipient gets the message with the ECM attachment, they'll need to be logged in to that
                        ECM service before they can view or open the file.

For more information, see https://help.webex.com/en-us/nfia8at/Configure-Enterprise-Content-Management-Settings-in-Cisco-Webex-Control-Hub and https://help.webex.com/en-us/nuvy9lb/Enterprise-Content-Management-in-Cisco-Webex-Control-Hub .

#### Quote Message

You can add context to a message by quoting another message in the same space. To quote a message, hover the cursor over the
                        message you want to quote and select Quote message . After you send the message, the quoted message appears above your message in the space.

#### BOT Support

BOTs now appear in your search results, and you can add them to spaces and to an existing conversation, and create a new conversion
                        with a BOT . To find a BOT, go to the search bar and type the first few letters of its name. BOTs appear in their own category
                        underneath results from your contacts and directory.

Jabber Team Messaging Mode users can search for and use BOTs that are deployed as part of the Webex Platform Service. You
                        can find these BOTs on the Cisco Webex App Hub or develop your own for your users. BOTs from the Cisco Jabber BOT SDK work only for on-premises and Webex Messenger deployments.

#### Proxy Authentication Support

Earlier releases do not support proxy authentication. Jabber now supports proxy authentication as outlined in this table:

Product

Supported Authentication Types

Supported Proxy Configuration Methods

Cisco Jabber for Windows

No Auth, Basic, NTLM, Negotiate

Manual, PAC

Cisco Jabber for Mac

No Auth, Basic, NTLM

Manual, PAC

Cisco Jabber Softphone for VDI

No Auth, Basic, NTLM, Negotiate

Manual, PAC

For NTLM authentication on Mac, users are prompted for a password if the computer is not signed in to the domain. For Windows
                                    or Jabber Softphone for VDI, the computer must be signed in to the domain.

For No Auth authentication types, you can set up the computer with a proxy address, but no authentication is used.

For information on Proxy Auto-Config (PAC) files, see https://www.cisco.com/c/en/us/td/docs/security/web_security/connector/connector2972/PACAP.html .

Proxy Authentication and Certificates

If you deploy a TLS-inspecting proxy, install a CA certificate into the OS of the device with a trust chain that allows a
                        successful certificate validation.

Jabber validates the certificates of the systems with which it communicates. Jabber validates the certificates for a TLS session
                        against the list of trusted root certificate authorities in the other system's OS. Jabber also checks the certificates against
                        known malicious or compromised certificate authorities.

### Meetings

#### On-Demand Recording

In previous releases, you could only enable or disable recording for all calls in Jabber. On-demand recording gives you the
                        option to enable users to selectively record calls over Jabber's Built-In Bridge (BiB). When you enable this feature, the
                        call control menu includes a Record option for the user to start and stop recording at any time.

You need Cisco Unified Communications Manager Release 12.5(1) to support this feature.

For information on using on-demand recording, see the Feature Configuration for Cisco Jabber guide.

You can force all recording to occur on the Jabber BiB with the Prefer_BIB_recorder parameter. For details, see the Parameters Reference Guide for Cisco Jabber .

#### Application Sharing

When you share your screen during a call, CMR meeting call, or CMS meeting call, you can limit what you share to a specific
                        application, instead of sharing the entire screen. Now, from the Share Screen, you have the option of choosing which application
                        to share.

#### Updates to Collaboration Meeting Room Controls

This release includes several new CMR controls. Hosts can now:

Mute or unmute all participants

Pause and resume the meeting recording

All participants can do the following:

Start or stop sending video

Copy the meeting link

Use the Meeting Info icon to display details about the meeting

### Calling

#### Voicemail Improvements

We improved the voicemail capabilities in the desktop clients.

Users can create voicemails without making a call and then send the voicemail to one or more contacts. The voicemail server's
                        administrator can also create distribution lists to which users can send voicemails. Users can select recipients from the
                        voicemail server's catalog.

Users can directly reply to the sender of a voicemail or to all recipients of that message. Users can also forward voicemails
                        to new recipients.

#### Display Directory Number or Label for Single Lines

In multiline operation, users choose between their configured lines in a selection list. The selection list displays the directory
                        number or the label for each line. In earlier releases, the selection list does not appear for users who only have a single
                        line.

Now, for Phone-Only Mode and Phone Mode with Contacts deployments, the single line's number or label appears by default. For
                        Full UC Mode deployments, the single line's number or label is hidden by default.

You can override the default behavior for single-line operation with the new SingleLinePhoneLabel parameter. For details, see the Parameters Reference Guide for Cisco Jabber .

#### Multiline Improvements

In earlier releases, Jabber has these multiline limitations:

CTI-enabled users can only control the primary line on their desk phone.

You couldn't configure two lines with the same number that are associated with different partitions.

As of Release 12.7, users can control all lines on their desk phone. You can also configure two lines with the same number
                        that are associated with different partitions.

### Security

#### Enhancement to Security Labels

We enhanced our support for security labels, based on the XEP-0258 standard, for instant messages. The InstantMessageLabels parameter now supports <label> elements. You can assign more metadata to the security labels. You can use the <label> element to identify the security compliance
                        server, such as Apache NiFi, that screens the messages before delivery.

For more information about using the InstantMessageLabels parameter, see the Parameters Reference Guide for Cisco Jabber . You can configure this setting in the Unified CM Administration or in the jabber-config.xml configuration file.

For information on using security labels in your deployment, see the Feature Configuration for Cisco Jabber guide.

#### Updated Sign-Out Behavior

If users sign out of Jabber, they must now re-authenticate when they next sign in.

Users do not have to re-authenticate in these cases:

A configuration change requires them to sign out.

They kill the Jabber app and restart it. (For desktop users, this includes when you choose Exit Jabber .)

Mobile Jabber users with touch, fingerprint, or face ID enabled.

#### OAuth Handling of Refresh Tokens

If you have OAuth enabled in your deployment, Jabber now checks, by default, for expired refresh tokens when users sign in.
                        If a refresh token has expired, the user must re-authenticate. If the refresh token expires while a user is signed in, Jabber
                        signs them out with a message that their session expired.

The LegacyOAuthLogout parameter controls this behavior. The default value of false checks for expired refresh tokens. If you set the value to true , Jabber never checks for expired refresh tokens. For details, see the Parameters Reference Guide for Cisco Jabber .

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

To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search .

Sign in with your Cisco.com user ID and password.

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release.

For more information, select Help at the top right of
                                    the Bug Search page.

### Resolved Caveats in Release 12.7(6)

Identifier

Severity

Headline

CSCwc24382

3

Cisco Jabber Security Vulnerability: XMPP Stanza Smuggling with stream:stream tag

### Open Caveats in 12.7(4)

### Resolved Caveats in 12.7(4)

### Open Caveats in 12.7(3)

Identifier

Severity

Headline

### Resolved Caveats in 12.7(3)

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

### Resolved Caveats in Release 12.7(2)

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

### Open Caveats in Release 12.7(1)

Identifier

Severity

Headline

### Resolved Caveats in Release 12.7(1)

Identifier

Severity

Headline

### Closed Caveats in Release 12.7(1)

Identifier

Severity

Headline

CSCvq65042

3

JDV 4.1.8 msidriver.sys has expired certificate signature

### Open Caveats in Release 12.7

Identifier

Severity

Headline

CSCvr12260

2

Jabber Windows 12.6.1 UDS lookup failing

CSCvp28473

3

Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature).

CSCvq11501

3

Jabber for Windows J4W does not refresh access token in failover scenario over MRA

CSCvq65042

3

JDV 4.1.8 msidriver.sys has expired certificate signature

CSCvq97257

3

Wrong IM address showing up for users and saved chats displaying with wrong user

CSCvr04041

3

Share screen&take control option-after closing the sharing, user is not able to type in non-english

CSCvr12034

3

Forced Authorization Codes (FAC) are not supported on Jabber clients

CSCvr12341

3

JVDI 12.6 Emoticons window very often behind Jabber or does not open at all

CSCvr09198

6

Unable to access custom tab over Expressway when BrowserEngineForCustomTab is configured to IE

### Resolved Caveats in Release 12.7

Identifier

Severity

Headline

CSCvq85116

2

Jabber spell check breaks when detecting multiple grammatical Errors

CSCvr12348

2

Save History Button not-working

CSCvn82915

3

Jabber causing high CPU usage and log looping over SSL_read() when connected of MRA

CSCvp25412

3

Chat button is missing in incoming call notification of Cisco Jabber for Windows

CSCvp40099

3

Flickering conference video in Jabber for Windows with RTL locale

CSCvp40120

3

Participant list not displayed for conference in Jabber for Windows with RTL locale

CSCvp42087

3

Collapse selfview string is not localized to Japanese in Cisco Jabber for Windows.

CSCvp64715

3

Jabber can not login after Webex Messenger server is migrated

CSCvq08500

3

Line id is showing wrong for unassigned directory numbers in calls tab

CSCvq18192

3

Multiline drop down shows invisible line numbers in high contrast mode

CSCvq33250

3

Login related error notifications are not visible in high contrast mode

CSCvq36974

3

Location inputs are not visible when adding new location

CSCvq61400

3

Recents call history icons are not visible in high contrast mode

CSCvq90806

3

Jabber 12.X P2P file transfer and screen capture not working

CSCvr02221

3

Jabber for Windows Unable to see Participant list when calling into Webex

CSCvr04172

3

Voice quality issue when recording is enabled on jabber

CSCvr04176

3

Jabber 12.6 in deskphone mode does not display hunt-pilot name

CSCvr08269

3

Jabber changes UDS server list on config refetch with manual login

CSCvs70284

3

Jabber 12.6 Audio crackling

CSCvq93015

5

Jabber - Spelling error in an error message in the German translation.

### This Document Applies to These Products

- Jabber for Windows

| Version | Build Number |
|---|---|
| 12.7(6) | 12.7.6.57310 Build 307310 |
| 12.7(5) | 12.7.5.55797 Build 305797 |
| 12.7(4) | 12.7.4.55432 Build 305432 |
| 12.7(3) | 12.7.3.54811 Build 304811 |
| 12.7(2) | 12.7.2.53984 build 303984 |
| 12.7(1) | 12.7.1.51081 |
| 12.7 | 12.7.0.38632 |

| Note | We don't support changing the color of chat text in this theme. |
|---|---|

| Product | Supported Authentication Types | Supported Proxy Configuration Methods |
|---|---|---|
| Cisco Jabber for Windows | No Auth, Basic, NTLM, Negotiate | Manual, PAC |
| Cisco Jabber for Mac | No Auth, Basic, NTLM | Manual, PAC |
| Cisco Jabber Softphone for VDI | No Auth, Basic, NTLM, Negotiate | Manual, PAC |
| For NTLM authentication on Mac, users are prompted for a password if the computer is not signed in to the domain. For Windows
                                    or Jabber Softphone for VDI, the computer must be signed in to the domain. For No Auth authentication types, you can set up the computer with a proxy address, but no authentication is used. |

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
| CSCvr42648 | 2 | Automute function does not work on Jabber for windows |
| CSCva93690 | 3 | "Invalid Exchange credentials" when Saving chats to O365 |
| CSCvm82709 | 3 | Jabber "show connnection status' not using CUCM |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the
                                 Whisper announcement (UCCE feature) |
| CSCvq11501 | 3 | Jabber for Windows J4W does not refresh access token in failover
                                 scenario over MRA |
| CSCvr00981 | 3 | JabberWin - Softphone Doesn't Re-Register When VPN Connection is
                                 Changed |
| CSCvr04041 | 3 | Share screen&take control option-after closing the sharing,
                                 user is not able to type in non-english |
| CSCvr12341 | 3 | Jabber 12.6 Emoticons window appears behind chat window or does
                                 not open at all in VDI environment |
| CSCvr25302 | 3 | Photos are not displayed for contacts immediately after adding
                                 Directory Group |
| CSCvr75200 | 3 | Call History contacts are not seen till user sign out and then
                                 sign in |
| CSCvr76764 | 3 | Jabber does not trust certificate for sip-oauth
                                 connection |
| CSCvr82552 | 3 | Unable to share the screen from contacts tab in Cisco Jabber for
                                 Windows |
| CSCvr82874 | 3 | Jabber fails to authenticate BFCP if user id is changed in
                                 re-invite |
| CSCvr86141 | 3 | Jabber error "Jabber stopped working" when moving chat window to
                                 external scale monitor |
| CSCvr87501 | 3 | Race condition with presence statuses on Cisco Jabber for
                                 Windows |
| CSCvr88725 | 3 | Jabber 12.7.0 notifications not showing intermittently |

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
| CSCvr42648 | 2 | Automute function does not work on Jabber for windows |
| CSCva93690 | 3 | "Invalid Exchange credentials" when Saving chats to O365 |
| CSCvm82709 | 3 | Jabber "show connnection status' not using CUCM |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature) |
| CSCvq11501 | 3 | Jabber for Windows J4W does not refresh access token in failover scenario over MRA |
| CSCvr00981 | 3 | JabberWin - Softphone Doesn't Re-Register When VPN Connection is Changed |
| CSCvr04041 | 3 | Share screen&take control option-after closing the sharing, user is not able to type in non-english |
| CSCvr12341 | 3 | Jabber 12.6 Emoticons window appears behind chat window or does not open at all in VDI environment |
| CSCvr25302 | 3 | Photos are not displayed for contacts immediately after adding Directory Group |
| CSCvr75200 | 3 | Call History contacts are not seen till user sign out and then sign in |
| CSCvr76764 | 3 | Jabber does not trust certificate for sip-oauth connection |
| CSCvr82552 | 3 | Unable to share the screen from contacts tab in Cisco Jabber for Windows |
| CSCvr82874 | 3 | Jabber fails to authenticate BFCP if user id is changed in re-invite |
| CSCvr86141 | 3 | Jabber error "Jabber stopped working" when moving chat window to external scale monitor |
| CSCvr87501 | 3 | Race condition with presence statuses on Cisco Jabber for Windows |
| CSCvr88725 | 3 | Jabber 12.7.0 notifications not showing intermittently |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvr31928 | 1 | Jabber Not sending the JSESSIONID/Cookie in the Keep Alive Request causing the voicemail outage |
| CSCvr47127 | 1 | Jabber 12.7.0 is causing finesse login failure |
| CSCvr12260 | 2 | Jabber Windows 12.6.1 UDS lookup failing when mobile/home phone numbers in UDS search response |
| CSCvr26715 | 2 | Apostrophe character \" ' \" is showing as \"&#39\"; in email contact details in Jabber |
| CSCvr35285 | 2 | Webex Customer Jabber do random sort 12 CUCM UDS Servers and trigger phone service issue. |
| CSCvr60384 | 2 | Jabber does not clear outlook temp presence correctly |
| CSCvr78497 | 2 | Jabber loosing Phone services randomly |
| CSCvr89022 | 2 | J4W CTI does not re-connect after network change |
| CSCvr94513 | 2 | Upgrade Profiles in Cisco Webex Control Hub are not applied to Jabber Client |
| CSCvq97257 | 3 | Wrong IM address showing up for users and saved chats displaying with wrong user |
| CSCvr02609 | 3 | Unable to connect to phone service when switch from wired ethernet to wifi with Pluse VPN |
| CSCvr16971 | 3 | Jabber Windows is typing icon in the chat tab does not look like a pen or pencil as intended |
| CSCvr18004 | 3 | Jabber is not switching to shared screen automatically |
| CSCvr23547 | 3 | Jabber Clic2Call Firefox Issues |
| CSCvr25756 | 3 | Jabber should handle 400 errors better when cucm doesn't support bulk search |
| CSCvr27954 | 3 | jabber meeting spelling error 'Tentaticve' |
| CSCvr36510 | 3 | Newly created location details are not displaying in dark mode of Cisco Jabber for Windows |
| CSCvr37192 | 3 | Jabber for Windows with Agent Line - SIP notify dialog information incorrect. |
| CSCvr38541 | 3 | libexpat Improper Parsing Denial of Service Vulnerability |
| CSCvr41074 | 3 | Jabber Windows 12.7 crashes after unlocking the Windows PC |
| CSCvr46303 | 3 | ShowTabLabel key not working |
| CSCvr46492 | 3 | Jabber Windows Video to DX, 8865, 8945 etc. Gets No Video in Secure Mode |
| CSCvr50146 | 3 | Jabber windows dtmf digit press tone not played when using kpml |
| CSCvr53811 | 3 | Jabber 12.7 Transfer button not highlighted |
| CSCvr57224 | 3 | Jabber application crash in teams mode |
| CSCvr60593 | 3 | Message not getting deleted when user clicks enter key. |
| CSCvr60708 | 3 | Jabber 12.6.X and Above crashes when sending images in FIPS mode |
| CSCvr66558 | 3 | J4W Locations are not recognized when connected via VPN |
| CSCvr66707 | 3 | Remember my open conversations option missing in single-window UI settings |
| CSCvr67084 | 3 | Unable to find the information(i) icon of the user in High contrast Setting mode in CJW |
| CSCvr70692 | 3 | Unable to move to different flag messages under same user in JTMM for Windows |
| CSCvr71711 | 3 | Jabber 12.7 sender sometimes seeing incorrect thumbnail when send an image file or screenshot |
| CSCvr73994 | 3 | Jabber for Windows 12.7 incorrectly spells Wednesday in Call History as Vednesday |
| CSCvr74101 | 3 | J4W 12.7.0: Non-ASCII characters displayed incorrectly in Meetings tab |
| CSCvr76323 | 3 | Jabber 12.7 Teams mode crash when call attempted from history |
| CSCvr84060 | 3 | Jabber windows crashing when clicked on unknown caller record from missed call history |
| CSCvr85921 | 3 | Jabber for Windows 12.6.X and 12.7.0 crashes when user trying to call IM protocol handler |
| CSCvr88003 | 3 | Jabber for Windows 12.6.2 Outlook tab new session button is gray/ghosted and cannot be clicked |
| CSCvr36509 | 4 | OpenSSL Padding Oracle Information Disclosure Vulnerability |
| CSCvr45704 | 5 | Jabber 12.7 Hebrew locale cursor is in the wrong place, (RTL language) |
| CSCvq67717 | 6 | Jabber Voicemail Service enhancement to reduce oversubscription |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvq65042 | 3 | JDV 4.1.8 msidriver.sys has expired certificate signature |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvr12260 | 2 | Jabber Windows 12.6.1 UDS lookup failing |
| CSCvp28473 | 3 | Jabber doesn't play 300 milliseconds of initial audio in the Whisper announcement (UCCE feature). |
| CSCvq11501 | 3 | Jabber for Windows J4W does not refresh access token in failover scenario over MRA |
| CSCvq65042 | 3 | JDV 4.1.8 msidriver.sys has expired certificate signature |
| CSCvq97257 | 3 | Wrong IM address showing up for users and saved chats displaying with wrong user |
| CSCvr04041 | 3 | Share screen&take control option-after closing the sharing, user is not able to type in non-english |
| CSCvr12034 | 3 | Forced Authorization Codes (FAC) are not supported on Jabber clients |
| CSCvr12341 | 3 | JVDI 12.6 Emoticons window very often behind Jabber or does not open at all |
| CSCvr09198 | 6 | Unable to access custom tab over Expressway when BrowserEngineForCustomTab is configured to IE |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvq85116 | 2 | Jabber spell check breaks when detecting multiple grammatical Errors |
| CSCvr12348 | 2 | Save History Button not-working |
| CSCvn82915 | 3 | Jabber causing high CPU usage and log looping over SSL_read() when connected of MRA |
| CSCvp25412 | 3 | Chat button is missing in incoming call notification of Cisco Jabber for Windows |
| CSCvp40099 | 3 | Flickering conference video in Jabber for Windows with RTL locale |
| CSCvp40120 | 3 | Participant list not displayed for conference in Jabber for Windows with RTL locale |
| CSCvp42087 | 3 | Collapse selfview string is not localized to Japanese in Cisco Jabber for Windows. |
| CSCvp64715 | 3 | Jabber can not login after Webex Messenger server is migrated |
| CSCvq08500 | 3 | Line id is showing wrong for unassigned directory numbers in calls tab |
| CSCvq18192 | 3 | Multiline drop down shows invisible line numbers in high contrast mode |
| CSCvq33250 | 3 | Login related error notifications are not visible in high contrast mode |
| CSCvq36974 | 3 | Location inputs are not visible when adding new location |
| CSCvq61400 | 3 | Recents call history icons are not visible in high contrast mode |
| CSCvq90806 | 3 | Jabber 12.X P2P file transfer and screen capture not working |
| CSCvr02221 | 3 | Jabber for Windows Unable to see Participant list when calling into Webex |
| CSCvr04172 | 3 | Voice quality issue when recording is enabled on jabber |
| CSCvr04176 | 3 | Jabber 12.6 in deskphone mode does not display hunt-pilot name |
| CSCvr08269 | 3 | Jabber changes UDS server list on config refetch with manual login |
| CSCvs70284 | 3 | Jabber 12.6 Audio crackling |
| CSCvq93015 | 5 | Jabber - Spelling error in an error message in the German translation. |