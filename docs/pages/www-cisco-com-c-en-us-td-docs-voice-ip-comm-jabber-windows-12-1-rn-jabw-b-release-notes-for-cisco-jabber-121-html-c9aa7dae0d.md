---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-windows-12-1-rn-jabw-b-release-notes-for-cisco-jabber-121-html-c9aa7dae0d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Windows/12_1/RN/jabw_b_release-notes-for-cisco-jabber_121.html
retrieved_at: 2026-08-21T06:56:07.921989+00:00
---

Release Notes for Cisco Jabber for Windows 12.1

# Release Notes for Cisco Jabber for Windows 12.1

First Published: July 19, 2018

Last Updated: May 31, 2021

# Introduction

Information for a maintenance release includes the features, requirements, restrictions, and bug fixes of the previous releases
                  unless mentioned otherwise.

The article does not include updates for patches or hot fixes.

Before you install Cisco Jabber for Windows, we recommend that you review the release notes for information regarding issues
                  that may affect your system.

## Jabber End-User Content on Cisco Webex Help Center

You can find information on the Jabber client at https://help.webex.com/ld-n1uv5wq-CiscoJabber/Jabber . The
                  Help Center contains articles on using Jabber features. You can provide feedback on
                  individual articles or request new articles through the Help Center.

The Help Center search includes a set of filters to narrow your results by product, release, activities, operating system,
                  and other categories.

## Build Number

Release

Build Number

12.1(5)

12.1.5.39932 Build 289932

12.1(4)

12.1.4.39719 Build 289719

12.1(3)

12.1.3.39452 build 289452

12.1(2)

12.1.2.24692

12.1(1)

12.1.1.19866

12.1

12.1.0.266460

## Additional Maintenance Releases

For additional maintenance release information, refer to:

Feature enhancements  — see https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html for the latest version of release
                           notes.

Caveats — see https://bst.cloudapps.cisco.com/bugsearch/ for latest caveat updates.

Security Advisories — see https://tools.cisco.com/security/center/publicationListing.x for a listing of the latest advisories.

## What's New in Release 12.1(5)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.1(4)

This maintenance release contains security updates and stability improvements. See
                     the Caveats for details.

## What's New in Release 12.1(3)

This maintenance release contains security updates. See the Caveats for details.

## What's New in Release 12.1(2)

### Resolved Caveats

This release provides fixes for a number of known issues. See the Resolved Caveats in Release 12.1(2) section for a list of caveats fixed in this release.

## What’s New in Release 12.1(1)

### New Values for Saving Chat History

The parameter SaveChatHistoryToExchangeOperationMode has additional values that affect how you can save Cisco Jabber chats to a folder in Microsoft Outlook. For more information,
                     see the Parameters Reference Guide for Cisco Jabber 12.1 .

### Reset Switch in Windows Installer

Now you have the option to reset Jabber when you’re pushing a new version to your users. Include the RESET_JABBER installer
                     switch in a command line installation. For more information, see the chapter Deploy Cisco Jabber Applications in On-Premises Deployment for Cisco Jabber 12.1 .

### Mobile Client Promotion

The parameter EnablePromoteMobile is now disabled by default. Users will no longer be prompted to install the mobile client. For more information, see the Parameters Reference Guide for Cisco Jabber 12.1 .

### Resolved Caveats

This release provides fixes for several known defects.

## What’s New in Release 12.1

### Administrator

Jabber Mobile App Promotion —You can enable a notification for Cisco Jabber for Windows users to promote the use of the Cisco Jabber for Mobile clients.
                              Clicking the notification lets the user download the app from Google Play or the Apple App Store. You can configure this notification
                              using the EnablePromoteMobile parameter.

This parameter is enabled by default.

You can change the default text of the user notification by configuring the PromotionWelcomeText key. You can also change the download link by configuring the AndroidDownloadURL parameter for Android, and the IOSDownloadURL parameter for iOS.

For more information, see the Parameter Reference Guide for Cisco Jabber 12.1 .

### Telephony

Multiline Support for All Lines Over MRA —Multiline is supported on all lines (primary and secondary) when using Cisco Jabber for desktop in Mobile and Remote Access
                           (MRA) mode.

For more information on configuring this feature, see the Feature Configuration Guide for Cisco Jabber 12.1 .

TelephonyOnlyDiscovery —This is a new parameter for Cisco Jabber operating in an on-premises and cloud deployment modes. This parameter specifies
                           if your users have access to phone only mode or the default configuration that you have set up in your environment. For more
                           information, see the Parameter Reference Guide for Cisco Jabber 12.1.

EnableSingleNumberReach —This is a new parameter that specifies if users can access Single Number Reach from the user interface. For more information,
                           see the Parameter Reference Guide for Cisco Jabber 12.1.

### Administrator

Retain Secure Phone Certificate during a Cisco Jabber Reset —Users must retain the secure phone certificate during a Cisco Jabber reset. If users have not retained the secure phone certificate,
                              they have to contact you to configure the phone service.

EnableConvertNumberToURI —This is a new parameter that specifies if Cisco Jabber converts numbers into SIP URI when a user enters numbers in the chat
                              window.

### Chat and Presence

@Mention Notifications in Persistent Chat Rooms —Users will continue to receive notifications in Cisco Jabber when someone mentions them in chat rooms, even if the chat room
                           is muted.

Mute or Unmute Persistent Chat Rooms —You and your users can mute or unmute chat rooms in Cisco Jabber.

Add Participant Button Removed from the Persistent Chat Room Toolbar — Chat room users in Cisco Jabber already have an option within the chat rooms to add participants. Therefore, the Add Participant
                           button on the chat room toolbar is removed.

Prevent Contact Duplication for Custom Contacts —Cisco Jabber displays a notification if the custom contact details you’re trying to add already exists. You can however add
                           a duplicate contact if the user is already a directory contact.

### UI Enhancements

Contact Lookup Enhancement —Support for base64-encoded thumbnail photos. Cisco Jabber contact lookup now supports base64-encoded contact photos when
                           using LDAP or HTTP photo retrieval. Cisco Jabber will determine if the server response is a text URL (for LDAP only), an image,
                           or a base64-encoded image, and displays it accordingly.

## Requirements

### Software Requirements

Server

Software

Operating systems

Microsoft Windows 10, 32 and 64 bit (Desktop OS x86)

- Microsoft Windows 8.x, 32 and 64 bit

- Microsoft Windows 7 SP1 or later, 32 and 64 bit

On-premises servers

Cisco Unified Communications Manager version 10.5(2) or later (Minimum)

Cisco Unified Communications Manager version 11.5(1) SU3 or later (Recommended)

Cisco Unified Communications Manager IM & Presence version 10.5(2) or later

Cisco Unity Connection version 10.5 or later

- Cisco WebEx Meetings Server version 2.6 MR1 or later

Cisco Expressway Series for Cisco Unified Communications Manager

X8.10.1 or later (Recommended)

X8.10.1 or later (Recommended)

- Cisco TelePresence Video Communication Server 8.1.1 or later

Cisco Meeting Server (CMS) 2.2 or later

Virtual servers

- Citrix XenDesktop 6.5, 7.5, and later 7.x versions

- Citrix XenApp 6.5, 7.5, and later 7.x versions for published apps and desktop

- VMware Horizon 6.0 (with View)

- VMware Horizon 6 version 6.1.0, 6.2.0, 7.0, and later 7.x versions

Cloud-based servers

- Cisco WebEx Messenger service

- Cisco WebEx Meeting Center, version WBS31 or later

- Cisco WebEx Meetings Server 2.8 and later

Directory servers

- Active Directory Domain Services for Windows Server 2016

- Active Directory Domain Services for Windows Server 2012 R2

- Active Directory Domain Services for Windows Server 2008 R2

- Any server that supports the LDAPv3 protocol

- Active Directory Lightweight Directory Service (AD LDS) or Active Directory Application Mode (ADAM)

User Data Service

Cisco Unified Communications Manager User Data Service (UDS) with Cisco Unified Communications Manager 10.5(2) or later

Instant Messaging

Microsoft Internet Explorer 9 or later

### Hardware Requirements

Hardware

Requirement

Installed RAM

2 GB RAM

Free
                                    						Physical Memory

128 MB

Free
                                    						Disk Space

256 MB

CPU
                                    						Speed and Type

- Mobile AMD Sempron
                                       						  Processor 3600+ 2 GHz

- Intel Core2 CPU T7400 at
                                       						  2. 16 GHz

- Intel Atom

GPU

DirectX11 on Microsoft Windows 7

I/O
                                    						Ports

USB 2.0
                                    						for USB camera and audio devices.

### Network Requirements

#### Ports and Protocols

The client uses
                           		  the ports and protocols listed in the following table. If you plan to deploy a
                           		  firewall between the client and a server, configure the firewall to allow these
                           		  ports and protocols.

Port

Application Layer Protocol

Transport Layer Protocol

Description

Configuration

6970

HTTP

TCP

Connect
                                       						to the TFTP server to download client configuration files.

6972

HTTPS

TCP

Connects to the TFTP server to download client configuration files securely for
                                       						Cisco Unified Communications Manager release 11.0 and later.

53

DNS

UDP

Hostname
                                       						resolution.

3804

CAPF

TCP

Issues
                                       						Locally Significant Certificates (LSC) to IP phones. This port is the listening
                                       						port for Cisco Unified Communications Manager Certificate Authority Proxy
                                       						Function (CAPF) enrollment.

8443

HTTPS

Traffic to Cisco Unified Communications Manager and Cisco
                                       						Unified Communications Manager IM and Presence Service.

8191

SOAP

TCP

Connects
                                       						to local port to provide Simple Object Access Protocol (SOAP) web services.

Directory
                                          						  Integration —For LDAP contact resolution one of the following ports are used
                                       						based on LDAP configuration.

389

LDAP

TCP

LDAP TCP
                                       						(UDP) Connects to an LDAP directory service.

3268

LDAP

TCP

Connects
                                       						to a Global Catalog server for contact searches.

636

LDAPS

TCP

LDAPS
                                       						TCP Connects securely to an LDAP directory service.

3269

LDAPS

TCP

LDAPS
                                       						TCP Connects securely to the Global Catalog server.

Instant Messaging and
                                          						  Presence

443

XMPP

TCP

XMPP traffic to the Webex Messenger service. The client sends XMPP through this port in cloud-based deployments only. If port 443 is blocked, the client falls
                                       back to port 5222.

5222

XMPP

TCP

Connects to Cisco Unified Communications Manager IM and Presence
                                       						Service for instant messaging and presence.

37200

SOCKS5
                                       						Bytestream

TCP

Peer
                                       						to Peer file transfer, In on-premises deployments, the client also uses this
                                       						port to send screen captures.

7336

HTTPS

TCP

MFT
                                       						File transfer (On-Premises only).

Communication Manager
                                          						  Signaling

2748

CTI

TCP

Computer Telephony Interface (CTI) used for desk phone control.

5060

SIP

TCP

Provides Session Initiation Protocol (SIP) call signaling.

5061

SIP
                                       						over TLS

TCP

SIP
                                       						over TCP Provides secure SIP call signaling. (Used if Secure SIP is enabled for
                                       						device.)

30000
                                       						to 39999

FECC

UDP

Far
                                       						end camera control (FECC).

5070
                                       						to 6070

BFCP

UDP

Binary
                                       						Floor Control Protocol (BFCP) for video screen sharing capabilities.

Voice or Video Media
                                          						  Exchange

16384
                                       						to 32766

RTP/SRTP

UDP

Cisco
                                       						Unified Communications Manager media port range used for audio, video, and BFCP
                                       						video desktop share.

33434 to 33598

RTP/SRTP

UDP

Cisco Hybrid Services (Jabber to Jabber calling) media port
                                       						range used for audio and video.

49152 to 65535

RDP

TCP

IM-only desktop share. Applies to Cisco Jabber for Windows
                                       						only.

8000

RTP/SRTP

TCP

Used by Jabber Desk Phone Video Interface, allows users to receive video transmitted to their desk phone devices on their
                                       computers through the client.

Unity Connection

7080

HTTP

TCP

Used
                                       						for Cisco Unity Connection to receive notifications of voice messages (new
                                       						message, message update, and message deleted).

7443

HTTPS

TCP

Used
                                       						for Cisco Unity Connection to securely receive notifications of voice messages
                                       						(new message, message update, and message deleted).

443

HTTPS

TCP

Connects to Cisco Unity Connection for voicemail.

Cisco Webex Meetings

80

HTTP

TCP

Connects to Cisco Webex Meetings Center for meetings.

443

HTTPS

TCP

Connects to Cisco Webex Meetings Center for meetings.

8443

HTTPS

TCP

Web
                                       						access to Cisco Unified Communications Manager and includes connections for the
                                       						following:

Cisco Unified Communications Manager IP Phone (CCMCIP) server for assigned
                                             							 devices.

User Data Service (UDS) for contact resolution.

Accessories Manager

8001

TCP

In Cisco Jabber for Windows and Mac, Sennheiser plugin uses this port for Localhost traffic for call controls.

##### Ports for
                           		  Other Services and Protocols

In addition to
                           		  the ports listed in this section, review the required ports for all protocols
                           		  and services in your deployment. You can find the port and protocol
                           		  requirements for different servers in the following documents:

For Cisco
                                 				Unified Communications Manager, Cisco Unified Communications Manager IM and
                                 				Presence Service, see the TCP and
                                    				  UDP Port Usage Guide .

For Cisco
                                 				Unity Connection, see the System
                                    				  Administration Guide .

For Cisco Webex Meetings Server, see the Administration Guide .

For Cisco Meeting Server , see Cisco Meeting Server Release 2.6 and 2.7: Single Combined Meeting Server Deployments .

For Cisco Webex services, see the Administrator's Guide .

For
                                 				Expressway for Mobile and Remote Access, refer to Cisco
                                    				  Expressway IP Port Usage for Firewall Traversal .

For file
                                 				transfer port usage, see the Configuration and Administration of IM and Presence Service on
                                    				  Cisco Unified Communications Manager .

### Third-Party Requirements

Third-Party Software

Requirement

Microsoft Internet Explorer

Microsoft Internet Explorer 9 or later

Browser Click to Call is not supported on Microsoft Edge.

Microsoft Office

Microsoft Office 2016 Desktop OS Version, 32 and 64 bit

Microsoft Office 2013, 32 and 64 bit

Microsoft Office 2010, 32 and 64 bit

Microsoft Exchange integrates directly with Cisco Unified
                                    						Communications Manager. For more information, see the Configuration Guides for
                                    						the appropriate version of Cisco Unified Communications Manager.

Microsoft SharePoint

Microsoft SharePoint 2013

Microsoft SharePoint 2010

Microsoft 365

Cisco
                                    						Jabber for Windows supports client-side integration with Microsoft Office 365
                                    						with the following applications using an on-premises Active Directory (AD)
                                    						deployment:

Microsoft Office 2016 Desktop OS Version, 32 and 64 bit

Microsoft Office 2013

Microsoft Office 2010

Third-party calendars

Microsoft Outlook 2016, 32 and 64 bit

Microsoft Outlook 2013, 32 and 64 bit

Microsoft Outlook 2010, 32 and 64 bit

IBM Lotus Notes 9 32 bit

IBM Lotus Notes 8.5.3 32 bit

IBM Lotus Notes 8.5.2 32 bit

IBM Lotus Notes 8.5.1 32 bit

Google Calendar

#### Antivirus Exclusions

If you deploy antivirus software, include the following folder locations in the antivirus exclusion list:

C:\Users\<User>\AppData\Local\Cisco\Unified Communications\Jabber

C:\Users\<User>\AppData\Roaming\Cisco\Unified Communications\Jabber

C:\ProgramData\Cisco Systems\Cisco Jabber

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

### Limitations and Restrictions for On-Premises Deployments

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

### Open Caveats in 12.1(5)

### Resolved Caveats in 12.1(5)

### Open Caveats in 12.1(4)

### Resolved Caveats in 12.1(4)

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

### Resolved Caveats in Release 12.1(3)

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

### Open Caveats in Release 12.1(2)

### Resolved Caveats in Release 12.1(2)

Identifier

Severity

Headline

2

2

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

### Open Caveats in Release 12.1(1)

Identifier

Severity

Headline

CSCvm51685

3

Jabber steals focus when receiving chat notification.

CSCvm44162

3

Jabber tries to reconnect while getting 403 error response from Cisco Unity Connection.

CSCvm41653

3

Jabber uses cached UDS records to sign in even when SRV records have changed.

CSCvm12053

3

Remote screen doesn't maximize on screenshare on Surface Pro.

CSCvi49056

3

Directory search is slow because of an inaccurate search filter.

CSCvk23475

3

Evaluation of Jabber for Windows for OpenSSL.

CSCvk75843

3

Evaluation of Jabber for Windows for libxml2.

CSCvh29610

3

Memory leaks occur when switching front and rear cameras on the Surface Pro.

CSCvj26171

3

Typing Korean Unicode characters in the search box results in invalid data.

CSCvk59161

3

The user's FirstName LastName does not resolve correctly and appears as "Display Name."

### Resolved Caveats in Release 12.1(1)

Identifier

Severity

Headline

CSCvk41609

2

Jabber ends call when calling an E.164-formatted PSTN number that is resolved from a contact source.

CSCvg77054

3

Jabber closed unexpectedly when transformImage in contact service.

CSCvh97506

3

The button that disables screen sharing is not visible.

CSCvi31585

3

Chat messages are blank because of a global ID counter overflow.

CSCvj74965

3

Jabber call notification window automatically becomes active when receiving a call as part of a hunt group.

CSCvj87574

3

The More Options button is blank when there are multiple conversations in the window.

CSCvk06672

3

Jabber doesn't detect the stored location after the client system restarts.

CSCvk11361

3

There was no information about a multi-forest environment support parameter in the Jabber 12.X guides.

CSCvk20364

3

PRT decryption results in a no OpenSSL_Applink error message.

CSCvk22771

3

The chat window randomly goes blank because of a Chromium JS issue.

CSCvk29917

3

Crash in JabberMeeting!jm_register_network.

CSCvk37163

3

Jabber doesn’t show the presence of a contact in chat history until it is searched

CSCvk38897

3

unable to navigate to credential input box using tab

CSCvk50102

3

The chat history is not grayed out when a conversation is resumed on the same day.

CSCvk50577

3

Jabber unexpectedly closes when a user logs in to a PC that has been in sleep mode.

CSCvk59428

3

USB peripherals are not recognized when they are reconnected.

CSCvk69008

3

Jabber will not save a screen capture if the directory path includes the "&" symbol.

CSCvk76350

3

Jabber unexpectedly closes when the computer is locked or goes to sleep.

CSCvk78201

3

Ignore button should not appear for hunt group calls.

CSCvk78206

3

EnablePromoteMobile need be changed to off by default

CSCvk79333

3

Extend and Connect number can't be changed.

CSCvm01173

3

The Decline button is still displayed when a hunt group's Alerting Name is not set.

CSCvm01227

3

Jabber does not indicate that a meeting is starting.

CSCvm03588

3

Jabber over MRA loses audio 15 to 30 minutes into an ad hoc conference call.

CSCvm09049

3

Jabber does not use a batch API to query telephoneNumber in UDS directory search to CUCM.

CSCvm10476

3

Sign-in to Webex meeting account fails if password has special characters.

CSCvm10574

3

Jabber doesn’t download a custom config.xml if the device security profile is set to Secure.

CSCvm13840

3

A single HTTPS UDS query for a custom contact is made each time a contact record source is added.

CSCvm18430

3

Presence does not display correctly and chat messages are not being sent in a cloud deployment.

CSCvm21016

3

A user, after joining a persistent chat room, is missing from the persistent chat room roster.

CSCvm38534

3

The Meet Now function fails after a CWMS Server is upgraded or downgraded.

CSCvm41976

3

Jabber unexpectedly closes for Windows 10 users.

CSCvm00602

3

Jabber unexpectedly closes at launch when using Chinese locale.

CSCvj80212

3

Jabber queries non-batch UDS API before the UDS capability query response comes back.

CSCvd04176

4

The screen-sharing toolbar prevents access to the Windows Taskbar.

CSCvj97749

4

Errors are not appearing in the error notifications box.

CSCvk64385

4

The jabber-update.xml file is garbled if Japanese is used.

CSCvm07147

4

Jabber does not set EnableMari parameter until the user has signed out and signed in again.

CSCvh90442

6

Enhancement that balances UDS requests to all UDS servers.

### Closed Caveats in Release 12.1(1)

Identifier

Severity

Headline

CSCvm00602

3

Jabber unexpectedly closes at launch when using Chinese locale.

### Open Caveats in Release 12.1

Identifier

Severity

Headline

CSCvh29610

3

Memory leak detected while switching front and rear camera on Surface.

CSCvk22771

3

Jabber for Windows 12.0 persistent chat window randomly goes blank.

CSCvj26171

3

Input of Unicode characters in search box on Windows 10 results in invalid data.

### Resolved Caveats in Release 12.1

Identifier

Severity

Headline

CSCvj68256

2

Jabber for Windows 11.9.2, 11.9.3, 12.x clients do not enforce Contact limit size.

CSCvj83299

2

In Multiple Forest Environment scenario Jabber fails to bind with directory server in PhoneOnly mode.

CSCvf91342

3

Jabber 11.9 throws invalid Voicemail credentials popup for user with no voicemail access.

CSCvg72905

3

Jabber for Windows 11.9.1 SSO cookie refresh failure, request too long.

CSCvh95323

3

Jabber does not reconnect to LDAP in dual-DNS environment.

CSCvj14813

3

Jabber 12.0 default favicon not loading.

CSCvj35791

3

Jabber in Hybrid Cloud Expressway-E SSO authentication fails when Service and Voice Services domains do not match.

CSCvj44197

3

Jabber crashes when a new directory server is associated to the service profile.

CSCvj44261

3

Jabber 12.0 crashes while trying to store chat discussion.

CSCvj48856

3

Unable to search contacts after resuming computer from Sleep.

CSCvj53330

3

Cache initial DNS results and reuse results for every connection in a session.

CSCvj57038

3

Jabber cannot negotiate RFC 5285 and does not send RTP packets with that extension.

CSCvj58638

3

Save Chats to Outlook Autodiscovery failing on Autodiscover::GetDomainSettings.

CSCvj68824

3

Disabling availability sharing in IMP server disables IM functionality.

CSCvj75841

3

Jabber doesn't display correct presence, and IM messages are not being sent for cloud deployments.

CSCvj90657

3

LDAP does not unbind when the process does not get a response from the LDAP server.

CSCvj92713

3

Contact search is not working. SR number 684452711.

CSCvj95514

3

Jabber custom contacts can cause high CPU usage on LDAP or CUCM server.

CSCvk04627

3

Jabber quits unexpectedly on receiving calls.

CSCvk20364

3

PRT decryption results in no OpenSSL_Applink.

CSCvk08387

3

Mandatory upgrade task is not being advertised on initial sign-in.

CSCvn11462

3

Jabber does not get SIP invite in a CUCM fail-over situation, causing no audio.

### This Document Applies to These Products

- Jabber for Windows

| Release | Build Number |
|---|---|
| 12.1(5) | 12.1.5.39932 Build 289932 |
| 12.1(4) | 12.1.4.39719 Build 289719 |
| 12.1(3) | 12.1.3.39452 build 289452 |
| 12.1(2) | 12.1.2.24692 |
| 12.1(1) | 12.1.1.19866 |
| 12.1 | 12.1.0.266460 |

| Server | Software |
|---|---|
| Operating systems | Microsoft Windows 10, 32 and 64 bit (Desktop OS x86) Microsoft Windows 8.x, 32 and 64 bit Microsoft Windows 7 SP1 or later, 32 and 64 bit |
| On-premises servers | Cisco Unified Communications Manager version 10.5(2) or later (Minimum) Cisco Unified Communications Manager version 11.5(1) SU3 or later (Recommended) Cisco Unified Communications Manager IM & Presence version 10.5(2) or later Cisco Unity Connection version 10.5 or later Cisco WebEx Meetings Server version 2.6 MR1 or later Cisco Expressway Series for Cisco Unified Communications Manager Cisco Expressway-E: X8.10.1 or later (Recommended) Cisco Expressway-C: X8.10.1 or later (Recommended) Cisco TelePresence Video Communication Server 8.1.1 or later Cisco Meeting Server (CMS) 2.2 or later |
| Virtual servers | Citrix XenDesktop 6.5, 7.5, and later 7.x versions Citrix XenApp 6.5, 7.5, and later 7.x versions for published apps and desktop VMware Horizon 6.0 (with View) VMware Horizon 6 version 6.1.0, 6.2.0, 7.0, and later 7.x versions |
| Cloud-based servers | Cisco WebEx Messenger service Cisco WebEx Meeting Center, version WBS31 or later Cisco WebEx Meetings Server 2.8 and later |
| Directory servers | Active Directory Domain Services for Windows Server 2016 Active Directory Domain Services for Windows Server 2012 R2 Active Directory Domain Services for Windows Server 2008 R2 Any server that supports the LDAPv3 protocol Active Directory Lightweight Directory Service (AD LDS) or Active Directory Application Mode (ADAM) |
| User Data Service | Cisco Unified Communications Manager User Data Service (UDS) with Cisco Unified Communications Manager 10.5(2) or later |
| Instant Messaging | Microsoft Internet Explorer 9 or later |

| Hardware | Requirement |
|---|---|
| Installed RAM | 2 GB RAM |
| Free
                                    						Physical Memory | 128 MB |
| Free
                                    						Disk Space | 256 MB |
| CPU
                                    						Speed and Type | Mobile AMD Sempron
                                       						  Processor 3600+ 2 GHz Intel Core2 CPU T7400 at
                                       						  2. 16 GHz Intel Atom |
| GPU | DirectX11 on Microsoft Windows 7 |
| I/O
                                    						Ports | USB 2.0
                                    						for USB camera and audio devices. |

|  | Port | Application Layer Protocol | Transport Layer Protocol | Description |
|---|---|---|---|---|
| Configuration |
|  | 6970 | HTTP | TCP | Connect
                                       						to the TFTP server to download client configuration files. |
| 6972 | HTTPS | TCP | Connects to the TFTP server to download client configuration files securely for
                                       						Cisco Unified Communications Manager release 11.0 and later. |
| 53 | DNS | UDP | Hostname
                                       						resolution. |
| 3804 | CAPF | TCP | Issues
                                       						Locally Significant Certificates (LSC) to IP phones. This port is the listening
                                       						port for Cisco Unified Communications Manager Certificate Authority Proxy
                                       						Function (CAPF) enrollment. |
| 8443 | HTTPS |  | Traffic to Cisco Unified Communications Manager and Cisco
                                       						Unified Communications Manager IM and Presence Service. |
| 8191 | SOAP | TCP | Connects
                                       						to local port to provide Simple Object Access Protocol (SOAP) web services. |
| Directory
                                          						  Integration —For LDAP contact resolution one of the following ports are used
                                       						based on LDAP configuration. |
|  | 389 | LDAP | TCP | LDAP TCP
                                       						(UDP) Connects to an LDAP directory service. |
| 3268 | LDAP | TCP | Connects
                                       						to a Global Catalog server for contact searches. |
| 636 | LDAPS | TCP | LDAPS
                                       						TCP Connects securely to an LDAP directory service. |
| 3269 | LDAPS | TCP | LDAPS
                                       						TCP Connects securely to the Global Catalog server. |
| Instant Messaging and
                                          						  Presence |
|  | 443 | XMPP | TCP | XMPP traffic to the Webex Messenger service. The client sends XMPP through this port in cloud-based deployments only. If port 443 is blocked, the client falls
                                       back to port 5222. |
| 5222 | XMPP | TCP | Connects to Cisco Unified Communications Manager IM and Presence
                                       						Service for instant messaging and presence. |
| 37200 | SOCKS5
                                       						Bytestream | TCP | Peer
                                       						to Peer file transfer, In on-premises deployments, the client also uses this
                                       						port to send screen captures. |
| 7336 | HTTPS | TCP | MFT
                                       						File transfer (On-Premises only). |
| Communication Manager
                                          						  Signaling |
|  | 2748 | CTI | TCP | Computer Telephony Interface (CTI) used for desk phone control. |
| 5060 | SIP | TCP | Provides Session Initiation Protocol (SIP) call signaling. |
| 5061 | SIP
                                       						over TLS | TCP | SIP
                                       						over TCP Provides secure SIP call signaling. (Used if Secure SIP is enabled for
                                       						device.) |
| 30000
                                       						to 39999 | FECC | UDP | Far
                                       						end camera control (FECC). |
| 5070
                                       						to 6070 | BFCP | UDP | Binary
                                       						Floor Control Protocol (BFCP) for video screen sharing capabilities. |
| Voice or Video Media
                                          						  Exchange |
|  | 16384
                                       						to 32766 | RTP/SRTP | UDP | Cisco
                                       						Unified Communications Manager media port range used for audio, video, and BFCP
                                       						video desktop share. |
| 33434 to 33598 | RTP/SRTP | UDP | Cisco Hybrid Services (Jabber to Jabber calling) media port
                                       						range used for audio and video. |
| 49152 to 65535 | RDP | TCP | IM-only desktop share. Applies to Cisco Jabber for Windows
                                       						only. |
| 8000 | RTP/SRTP | TCP | Used by Jabber Desk Phone Video Interface, allows users to receive video transmitted to their desk phone devices on their
                                       computers through the client. |
| Unity Connection |
|  | 7080 | HTTP | TCP | Used
                                       						for Cisco Unity Connection to receive notifications of voice messages (new
                                       						message, message update, and message deleted). |
| 7443 | HTTPS | TCP | Used
                                       						for Cisco Unity Connection to securely receive notifications of voice messages
                                       						(new message, message update, and message deleted). |
| 443 | HTTPS | TCP | Connects to Cisco Unity Connection for voicemail. |
| Cisco Webex Meetings |
|  | 80 | HTTP | TCP | Connects to Cisco Webex Meetings Center for meetings. |
| 443 | HTTPS | TCP | Connects to Cisco Webex Meetings Center for meetings. |
| 8443 | HTTPS | TCP | Web
                                       						access to Cisco Unified Communications Manager and includes connections for the
                                       						following: Cisco Unified Communications Manager IP Phone (CCMCIP) server for assigned
                                             							 devices. User Data Service (UDS) for contact resolution. |
| Accessories Manager |
|  | 8001 |  | TCP | In Cisco Jabber for Windows and Mac, Sennheiser plugin uses this port for Localhost traffic for call controls. |

| Third-Party Software | Requirement |
|---|---|
| Microsoft Internet Explorer | Microsoft Internet Explorer 9 or later Note Browser Click to Call is not supported on Microsoft Edge. | Note | Browser Click to Call is not supported on Microsoft Edge. |
| Note | Browser Click to Call is not supported on Microsoft Edge. |
| Microsoft Office | Microsoft Office 2016 Desktop OS Version, 32 and 64 bit Microsoft Office 2013, 32 and 64 bit Microsoft Office 2010, 32 and 64 bit Microsoft Exchange integrates directly with Cisco Unified
                                    						Communications Manager. For more information, see the Configuration Guides for
                                    						the appropriate version of Cisco Unified Communications Manager. |
| Microsoft SharePoint | Microsoft SharePoint 2013 Microsoft SharePoint 2010 |
| Microsoft 365 | Cisco
                                    						Jabber for Windows supports client-side integration with Microsoft Office 365
                                    						with the following applications using an on-premises Active Directory (AD)
                                    						deployment: Microsoft Office 2016 Desktop OS Version, 32 and 64 bit Microsoft Office 2013 Microsoft Office 2010 |
| Third-party calendars | Microsoft Outlook 2016, 32 and 64 bit Microsoft Outlook 2013, 32 and 64 bit Microsoft Outlook 2010, 32 and 64 bit IBM Lotus Notes 9 32 bit IBM Lotus Notes 8.5.3 32 bit IBM Lotus Notes 8.5.2 32 bit IBM Lotus Notes 8.5.1 32 bit Google Calendar |

| Note | Browser Click to Call is not supported on Microsoft Edge. |
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
| CSCvm76932 | 2 | Jabber for Windows 12.1.0/12.1.1 Does Not Send setEnableInAMeetingStatus update to CUCM. |
| CSCvj26171 | 3 | Input of Unicode characters on search box on Windows 10 results in invalid data. |
| CSCvn17374 | 3 | Jabber sending https request to loginp.webexconnect.com overwhelming IDP. |
| CSCvm44162 | 3 | Jabber tries to reconnect while get 403 error response from Cisco Unity Connection. |
| CSCvm76042 | 3 | Pchat tab appears on Jabber even when it is not provisioned on the jabber-config.xml file. |
| CSCvj58896 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after transfer. |
| CSCvj58894 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after hold/resume. |
| CSCvi49056 | 3 | Directory search takes 5 seconds due to inaccurate search filter. |
| CSCvm83363 | 3 | First login to redirected Expressway cluster fails. |
| CSCve40856 | 3 | Desktop share button is grayed out during a call(BFCP) via MRA. |
| CSCvk79498 | 3 | Jabber crashed in HubWindowPlugin!TabButtonItem::CalculateImageSize. |
| CSCvn36100 | 3 | Jabber for windows Automatic update fails in phone mode. |
| CSCvn59476 | 3 | Peer-to-Peer file transfer causes Blank Chat IM session Jabber-Windows. |
| CSCvm85272 | 3 | Jabber "All Rooms" tab does not load Jabber-windows. |
| CSCvm84307 | 3 | MSVCR120.dll missing error pop-ups always when Jabber is launched Jabber-Windows. |
| CSCvm5498 | 3 | Jabber stuck when enabling audio-ducking Jabber-Windows. |
| CSCvk23475 | 3 | Evaluation of Jabber-windows for OpenSSL Jan 2018 Jabber-Windows. |
| CSCvh29610 | 3 | Switch front and rear camera Surface, the memory leak detects each time Jabber-Windows. |
| CSCvk48738 | 4 | Jabber for Windows user authentication with IM&P does not time out. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvn47352 | 2 | Jabber missing Cookie header for Voicemail HTTP requests leading to High CPU on Expressway-C. |
| CSCvn47527 | 2 | Jabber for Windows J4W does not refresh access token in failover scenario when primary node is down. |
| CSCvk79417 | 3 | CUCM cannot parse crypto capabilities provided by Jabber in SDP of last 200OK message. |
| CSCvk79452 | 3 | Filters doesn't direct to the opened conversation. |
| CSCvk79629 | 3 | Equivalent search filter is incorrect at the beginning of Jabber launched. |
| CSCvk79635 | 3 | Jabber Does Not Sync 1404 Credentials Even if 2100 Phone Credentials is Obtained. |
| CSCvm41653 | 3 | Jabber using cached UDS records for login even when SRV records have changed. |
| CSCvm51685 | 3 | Jabber steals focus when receiving chat notifcation. |
| CSCvm68457 | 3 | Jabber for Windows Crashes on Voicemail Plugin from Windows 7. |
| CSCvm82911 | 3 | Jabber attribute mapping should not be case sensitive. |
| CSCvn01127 | 3 | Goolge calendar access token is print in log. |
| CSCvn01149 | 3 | Goolge calendar credential file is not deleted after resetting Jabber. |
| CSCvn04975 | 3 | Google Calendar integration does not work in Jabber. |
| CSCvn05357 | 3 | Non-member disappears from admin's participant list after being muted. |
| CSCvn18692 | 3 | Notification does not appear in 'Chats' icon for P2P and Persistent Chat IMs. |
| CSCvn22235 | 3 | Jabber voicemail failure on SSO would show Presence connectivity to Expired as well. |
| CSCvn26127 | 3 | ENG: Jabber Win: Sentence begins with a lowercase letter '... you will have to be invited back.' |
| CSCvn30437 | 3 | Jabber does not transition from "In a Meeting" to "Away" when user locks PC and meeting ends. |
| CSCvn53649 | 3 | Jabber Windows Intermittently Downloads the Incorrect Contact Photo. |
| CSCvn56005 | 3 | Jabber does not select right Unity Server after CUCM Service Profile change. |
| CSCvn57177 | 3 | Presence not seen for conversation window. |
| CSCvn62888 | 3 | Host cannot see the only scheduled meetings in Jabber12.1.1 client. |
| CSCvn57707 | 3 | Jabber shows outlook presence offline for temp-presence contact after some time. |
| CSCvk79500 | 3 | Jabber crashed in NewMeetingService!CSFUnified::MeetingAccountConditionTimerStep. |
| CSCvn68292 | 3 | Meeting can not be launched if Orion meeting is not launched correctly. |
| CSCvk59161 | 3 | Jabber users FirstName LastName does not resolve correctly, instead it shows "Display Name". |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvm51685 | 3 | Jabber steals focus when receiving chat notification. |
| CSCvm44162 | 3 | Jabber tries to reconnect while getting 403 error response from Cisco Unity Connection. |
| CSCvm41653 | 3 | Jabber uses cached UDS records to sign in even when SRV records have changed. |
| CSCvm12053 | 3 | Remote screen doesn't maximize on screenshare on Surface Pro. |
| CSCvi49056 | 3 | Directory search is slow because of an inaccurate search filter. |
| CSCvk23475 | 3 | Evaluation of Jabber for Windows for OpenSSL. |
| CSCvk75843 | 3 | Evaluation of Jabber for Windows for libxml2. |
| CSCvh29610 | 3 | Memory leaks occur when switching front and rear cameras on the Surface Pro. |
| CSCvj26171 | 3 | Typing Korean Unicode characters in the search box results in invalid data. |
| CSCvk59161 | 3 | The user's FirstName LastName does not resolve correctly and appears as "Display Name." |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvk41609 | 2 | Jabber ends call when calling an E.164-formatted PSTN number that is resolved from a contact source. |
| CSCvg77054 | 3 | Jabber closed unexpectedly when transformImage in contact service. |
| CSCvh97506 | 3 | The button that disables screen sharing is not visible. |
| CSCvi31585 | 3 | Chat messages are blank because of a global ID counter overflow. |
| CSCvj74965 | 3 | Jabber call notification window automatically becomes active when receiving a call as part of a hunt group. |
| CSCvj87574 | 3 | The More Options button is blank when there are multiple conversations in the window. |
| CSCvk06672 | 3 | Jabber doesn't detect the stored location after the client system restarts. |
| CSCvk11361 | 3 | There was no information about a multi-forest environment support parameter in the Jabber 12.X guides. |
| CSCvk20364 | 3 | PRT decryption results in a no OpenSSL_Applink error message. |
| CSCvk22771 | 3 | The chat window randomly goes blank because of a Chromium JS issue. |
| CSCvk29917 | 3 | Crash in JabberMeeting!jm_register_network. |
| CSCvk37163 | 3 | Jabber doesn’t show the presence of a contact in chat history until it is searched |
| CSCvk38897 | 3 | unable to navigate to credential input box using tab |
| CSCvk50102 | 3 | The chat history is not grayed out when a conversation is resumed on the same day. |
| CSCvk50577 | 3 | Jabber unexpectedly closes when a user logs in to a PC that has been in sleep mode. |
| CSCvk59428 | 3 | USB peripherals are not recognized when they are reconnected. |
| CSCvk69008 | 3 | Jabber will not save a screen capture if the directory path includes the "&" symbol. |
| CSCvk76350 | 3 | Jabber unexpectedly closes when the computer is locked or goes to sleep. |
| CSCvk78201 | 3 | Ignore button should not appear for hunt group calls. |
| CSCvk78206 | 3 | EnablePromoteMobile need be changed to off by default |
| CSCvk79333 | 3 | Extend and Connect number can't be changed. |
| CSCvm01173 | 3 | The Decline button is still displayed when a hunt group's Alerting Name is not set. |
| CSCvm01227 | 3 | Jabber does not indicate that a meeting is starting. |
| CSCvm03588 | 3 | Jabber over MRA loses audio 15 to 30 minutes into an ad hoc conference call. |
| CSCvm09049 | 3 | Jabber does not use a batch API to query telephoneNumber in UDS directory search to CUCM. |
| CSCvm10476 | 3 | Sign-in to Webex meeting account fails if password has special characters. |
| CSCvm10574 | 3 | Jabber doesn’t download a custom config.xml if the device security profile is set to Secure. |
| CSCvm13840 | 3 | A single HTTPS UDS query for a custom contact is made each time a contact record source is added. |
| CSCvm18430 | 3 | Presence does not display correctly and chat messages are not being sent in a cloud deployment. |
| CSCvm21016 | 3 | A user, after joining a persistent chat room, is missing from the persistent chat room roster. |
| CSCvm38534 | 3 | The Meet Now function fails after a CWMS Server is upgraded or downgraded. |
| CSCvm41976 | 3 | Jabber unexpectedly closes for Windows 10 users. |
| CSCvm00602 | 3 | Jabber unexpectedly closes at launch when using Chinese locale. |
| CSCvj80212 | 3 | Jabber queries non-batch UDS API before the UDS capability query response comes back. |
| CSCvd04176 | 4 | The screen-sharing toolbar prevents access to the Windows Taskbar. |
| CSCvj97749 | 4 | Errors are not appearing in the error notifications box. |
| CSCvk64385 | 4 | The jabber-update.xml file is garbled if Japanese is used. |
| CSCvm07147 | 4 | Jabber does not set EnableMari parameter until the user has signed out and signed in again. |
| CSCvh90442 | 6 | Enhancement that balances UDS requests to all UDS servers. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvm00602 | 3 | Jabber unexpectedly closes at launch when using Chinese locale. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvh29610 | 3 | Memory leak detected while switching front and rear camera on Surface. |
| CSCvk22771 | 3 | Jabber for Windows 12.0 persistent chat window randomly goes blank. |
| CSCvj26171 | 3 | Input of Unicode characters in search box on Windows 10 results in invalid data. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvj68256 | 2 | Jabber for Windows 11.9.2, 11.9.3, 12.x clients do not enforce Contact limit size. |
| CSCvj83299 | 2 | In Multiple Forest Environment scenario Jabber fails to bind with directory server in PhoneOnly mode. |
| CSCvf91342 | 3 | Jabber 11.9 throws invalid Voicemail credentials popup for user with no voicemail access. |
| CSCvg72905 | 3 | Jabber for Windows 11.9.1 SSO cookie refresh failure, request too long. |
| CSCvh95323 | 3 | Jabber does not reconnect to LDAP in dual-DNS environment. |
| CSCvj14813 | 3 | Jabber 12.0 default favicon not loading. |
| CSCvj35791 | 3 | Jabber in Hybrid Cloud Expressway-E SSO authentication fails when Service and Voice Services domains do not match. |
| CSCvj44197 | 3 | Jabber crashes when a new directory server is associated to the service profile. |
| CSCvj44261 | 3 | Jabber 12.0 crashes while trying to store chat discussion. |
| CSCvj48856 | 3 | Unable to search contacts after resuming computer from Sleep. |
| CSCvj53330 | 3 | Cache initial DNS results and reuse results for every connection in a session. |
| CSCvj57038 | 3 | Jabber cannot negotiate RFC 5285 and does not send RTP packets with that extension. |
| CSCvj58638 | 3 | Save Chats to Outlook Autodiscovery failing on Autodiscover::GetDomainSettings. |
| CSCvj68824 | 3 | Disabling availability sharing in IMP server disables IM functionality. |
| CSCvj75841 | 3 | Jabber doesn't display correct presence, and IM messages are not being sent for cloud deployments. |
| CSCvj90657 | 3 | LDAP does not unbind when the process does not get a response from the LDAP server. |
| CSCvj92713 | 3 | Contact search is not working. SR number 684452711. |
| CSCvj95514 | 3 | Jabber custom contacts can cause high CPU usage on LDAP or CUCM server. |
| CSCvk04627 | 3 | Jabber quits unexpectedly on receiving calls. |
| CSCvk20364 | 3 | PRT decryption results in no OpenSSL_Applink. |
| CSCvk08387 | 3 | Mandatory upgrade task is not being advertised on initial sign-in. |
| CSCvn11462 | 3 | Jabber does not get SIP invite in a CUCM fail-over situation, causing no audio. |