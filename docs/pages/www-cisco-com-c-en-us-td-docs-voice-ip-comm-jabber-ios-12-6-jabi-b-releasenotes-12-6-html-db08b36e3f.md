---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-ios-12-6-jabi-b-releasenotes-12-6-html-db08b36e3f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/iOS/12_6/jabi_b_releasenotes-12-6.html
retrieved_at: 2026-08-21T07:01:09.634484+00:00
---

Release Notes for Cisco Jabber for iPhone and iPad 12.6

# Release Notes for Cisco Jabber for iPhone and iPad 12.6

### Download Options

Updated: January 14, 2020

First Published: April 9, 2019

Last Updated: January 14, 2020

## What's New in Cisco Jabber for iPhone and iPad 12.6(2)

### Resolved Caveats

This release provides fixes for some known issues. See the Resolved Caveats 12.6(2) section for a list of caveats fixed in
                     this release.

## What's New in Cisco Jabber for iPhone and iPad 12.6(1)

### Support for Viewing ECM Files

In team messaging mode, users are now able to view files sent to them via Enterprise Content Management (ECM) rather than
                     from a local directory. Selecting a shared ECM file will cross-launch a web browser where the file can be viewed.

### Resolved Caveats

This release provides fixes for a number of known issues. See the Resolved Caveats 12.6(1) section for a list of caveats fixed
                     in this release.

## What's New in Cisco Jabber for iPhone and iPad 12.6

### Jabber Team Messaging Mode

Support on Jabber for iPhone and iPad —Jabber for iPhone and iPad users have a new cloud-based deployment option that lets them work together in a team messaging
                     mode from their Jabber client. In team messaging mode, users get a new Chats tab in their client that they can use for group discussions.

Users will be able to:

Send and receive direct messages and group messages, and get read receipts for them.

Use key messaging features like sending files, flagging messages, deleting messages, using @mentions, emoticons, gifs, announcement
                           mode, and message encryption.

Filter messages (All, Direct Messages, Spaces, Unread, @mention, Favorites, Notifications, Flags).

See the list of their spaces.

Turn a conversation into a Webex meeting.

Show and display the following presence states: Active, Inactive, In a meeting, In a call, Presenting, Do Not Disturb, and
                           Out of Office.

Search for people, spaces, messages and files.

Identify external contacts in a chat window.

Contact migration is not supported from a mobile device. Instead, users can sign in to Jabber from a Windows or Mac computer
                     and migrate their contacts from there, or they can add their contacts to their contact list manually on their mobile device.

For a detailed look at what Jabber team messaging mode is and how it works, see the Cloud-Based Deployment Scenarios in the Planning Guide for Cisco Jabber and the workflow for Hybrid Deployments with Cisco Webex Platform Service in Cloud and Hybrid Deployments for Cisco Jabber .

Upgrade Profiles —You can create upgrade profiles on the Webex Control Hub for individual users or for your organization. Use the upgrade profiles
                     to control which version of Jabber team messaging mode your users are on. For more information about setting up upgrade profiles,
                     see how to Add Upgrade Profiles in the Webex Control Hub in Cloud and Hybrid Deployments for Cisco Jabber 12.6 .

Search on CI, UDS and LDAP —Users with Jabber team messaging mode can now search for contacts and their profiles from the company directory (on UDS/LDAP),
                     even if the contact is not in the CI. With the search results, you'll see the person's profile picture, and be able to call
                     them. To define the scope of contacts search, CI-only search is the default behavior. For more information, check out the ContactProfileSource and ContactSearchSource parameters in the Parameters Reference Guide for Cisco Jabber 12.6.

File Policy —You can control the file policy for your users on Jabber team messaging mode by restricting if users can share files. Set
                     the file policy in the Cisco Webex Control Hub.

### Feature Improvements

Offline Message Support For Jabber and Webex Teams —We have improved the messaging experience for Webex Messenger users who are enabled for interoperability between Cisco Jabber
                     and Cisco Webex Teams. Now when users who have been using Cisco Webex Teams sign back in to Jabber after a period being offline,
                     they will no longer get an alert telling them that new messages are available in Webex Teams, with a link to the Webex Teams
                     web client. Instead, they will receive their new messages in Jabber for their missed one-to-one conversations.

For more information, see how to Set Up Interoperability for Cisco Webex Teams and Jabber .

ActiveControl Support Over the MRA Expressway —ActiveControl is only accessible to users who are outside of the corporate network by using the Expressway for Mobile and
                     Remote Access (MRA). Using ActiveControl over MRA is done using SIP oAuth or CAPF enrollment. For environments without secure
                     phones, users can now authenticate to the network using their username and password when moving onto MRA.

For information about setting up ActiveControl, see Feature Configuration for Cisco Jabber 12.6.

Hide Persistent Chat Room Members —Jabber now supports a setting in Cisco Unified Communications Manager that lets you decide whether members and administrators
                     of a persistent chat room are listed in the room even when they don't have the chat window open. Changes to this setting apply
                     only to restricted rooms that are created after the change has been made. For more information, see the Persistent Chat Rooms section in Feature Configuration for Cisco Jabber 12.6 .

Support for Special Characters —Jabber now supports the use of special characters in usernames during login.

UDS Failover —In the event that your Cisco Unified Communications Manager User Data Service - UDS1(UCM1) - server becomes unavailable,
                     Jabber can now dynamically failover to the UDS2(UCM2) server for contact resolution and search. For more information, see
                     the Planning Guide for Cisco Jabber .

SIP-URI Display —It is now possible to display SIP-URI details for all users, even those in the same domain.

Disable Embedded Social Media Links —To comply with industry guidelines, the social media links in pages, such as the End User License Agreement and Privacy Policy,
                     are now disabled.

### Accessories and Devices

Device Support —We added support for the following devices:

3rd generation iPad Pro: 11-inch and 12.9-inch

Apple Watch series 4

For a full list of supported iPhone and iPad devices, see Hardware Requirements for Cisco Jabber for iPhone and iPad in the Planning Guide for Cisco Jabber 12.6 .

## Requirements

### Cisco Jabber Requirements

Many Cisco Jabber requirements are common between client types. Client specific requirements are documented in the Release Notes , all other requirements are documented in the Planning Guide for Cisco Jabber .

### Operating Systems for Cisco Jabber for iPhone and iPad

Refer to the App Store for the latest supported operating system version information.

Cisco supports only the current App Store version of Cisco Jabber for iPhone and iPad. Defects found in any Cisco Jabber
                                    for iPhone and iPad release are evaluated against current versions.

### Hardware Requirements for Cisco Jabber for iPhone and iPad

The following Apple devices are supported for Cisco Jabber for iPhone and iPad on iOS 11.X and iOS 12.X . The devices that are not upgraded to these versions are not supported.

Apple Device

Version

iPad

5th and 6th generation

iPad Air

Air 1 and Air 2

iPad Pro

9.7 and 10.5 inch

12.9 inch, 1st, 2nd and 3rd generation

iPad mini

Mini 2, mini 3, and mini 4

iPhone

5s, 6, 6 Plus, 6s, 6s Plus, 7, 7 Plus , 8, 8 Plus, X, Xs, Xs Max, XR and SE

iPod touch

6th generation

Apple Watch

WatchOS 5 running on Apple Watch and Apple Watch 2, 3 and 4.

The following Bluetooth headsets are supported on iPhone and iPad:

Manufacturer

Model(s)

Cisco

561, 562

Jabra

BIZ 2400, Easygo, Evolve 65 UC Stereo, EXTREME 2, Motion 1 , PRO 9470, Speak 450 for Cisco, Speak 510, Stealth Supreme UC, Wave +

Jawbone

ICON for Cisco Bluetooth Headset

Plantronics

Voyager Edge, Voyager Edge UC, Voyager Legend, Voyager Legend UC

Sony Eriksson

MW-600

1 Supports Bluetooth control for Cisco Jabber calls. This feature is only supported with firmware version 3.72.

### Accessibility

#### Screen Readers

Cisco Jabber for iPhone and iPad is compatible with the VoiceOver screen reader. Users who require screen readers should always
                        use the most recent version to ensure the best possible user experience.

#### Assistive Touch

You can navigate Cisco Jabber for iPhone and iPad using Explore by Touch.

## Limitations and Restrictions

Apple has new
                           						requirements for trusted certificates in iOS 13 (see https://support.apple.com/en-us/HT210176 ). Ensure that the certificates
                           						on the Unified Communications Mananger, IM & Presence, and Expressway
                           						servers meet these requirements. If your certificates don't meet these
                           						requirements, users are prompted to accept the certificates for each
                           						session.

If you make a Cisco Jabber for iPhone and iPad call using Expressway for
                           						Mobile and Remote Access over a 2G, 3G, or 4G network, you may experience
                           						audio quality issues from network instability.

For Cisco TelePresence Video Communication Server Control (VCS) versions earlier than 8.10.X, you have to configure the editable
                           inbound rules to enable the single number reach for users who are using Cisco Jabber over Mobile and Remote Access. For more
                           information, see Limitations in Enable Single Number Reach section from the Feature Configuration Guide for Cisco Jabber 12.0 .

Cisco
                           				Jabber for mobile clients do not show Favorite icon for users with Phone Only
                           				account.

Without Apple Push Notifications (APNs), when Cisco Jabber is suspended and receives an incoming call or chat, the iOS does
                           not wake up Cisco Jabber. The call or instant message appears on the device after several minutes or when Cisco Jabber is
                           taken to the foreground. As a workaround, reset the network settings using Settings > General > Reset > Reset Network Settings in the iOS device.

Users can no
                           				longer edit their Phone Services servers manually, except when they are in
                           				hybrid cloud mode. In hybrid deployments, administrators can configure the
                           				Phone Services servers to be editable.

The first usage of Secure Phone functionality must be on the corporate network or VPN to ensure proper certificate installation.

Voice recognition for voicemail PIN is highly sensitive to the background noise and may interpret background noise as user
                           input when the user doesn't input anything. Refer to System Administration Guide for Cisco Unity Connection to disable this function. https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html

Certificate validation windows pop up when the certificate on Cisco Unified Communications Manager is issued by an intermediate
                           certificate authority. Use a certificate that is signing with the root rather than an intermediate certificate authority.

From 10.5
                           				release onwards, all the Cisco Jabber account related files, including
                           				Configuration, Contacts, Credentials, History, Logs, Photo and so on, are not
                           				backed up on the iCloud and iTunes due to privacy reasons.

Creating
                           				and Configuring Devices for Users in Cisco Unified Communications Manager 11.0
                           				— If you are creating devices for users in Cisco Unified Communications Manager
                           				11.0, you can now specify a key order as RSA Only, EC Only, EC Preferred, or
                           				RSA Backup. However, the EC Only option is not currently supported by Cisco
                           				Jabber, and if you select it, the client fails to connect to the server.

With Jabber running in the background, if users try moving between networks; for example, from WiFi to 3G, the client disconnects
                           from the servers. It can take up to 11 minutes to reconnect and can lead to missed calls. To avoid missed calls, it is recommended
                           to enable Apple Push Notification service.

There is a
                           				known issue with signing into Cisco Jabber for some users who have migrated to
                           				Common Identity. If users receive an Incorrect user name or password error
                           				message when entering their username and password, see the following knowledge
                           				base article, https://cisco-support.webex.com/guest/articles/en_US/Troubleshooting/WBX000019555/myr=false .

CallKit functionality is deactivated in China due to government regulations.

### iPhone

Due to some limitations when Cisco Jabber for iPhone and iPad is running on iOS, Configure the Single Number Reach (SNR)
                           feature within Cisco Unified Communications Manager for users that require 100% reliability in call notifications. The limitations
                           include:

iOS may shut down Cisco Jabber and
                                 								other applications that are running in the background to preserve
                                 								resources. While the client attempts to relaunch, there is a
                                 								possibility that calls may be missed. To minimize the impact, it is
                                 								recommended to enable Apple Push Notification service.

Without Apple Push Notifications
                                 								(APNs), the device sometimes switches connection from the Wi-Fi data
                                 								network to the mobile voice network while the device is in Sleep
                                 								mode. Incoming calls may be missed due to this issue. To prevent
                                 								this issue, go to the iPhone Settings and turn off Cellular
                                    									Data or alternatively turn on SNR .

The VPN can disconnect when Connect-On-Demand is enabled and the user changes networks. Cisco Jabber for iPhone and iPad may
                                 take up to 11 minutes to reconnect through the VPN. This issue can lead to missing incoming calls. This occurs when the Wi-Fi
                                 signal is not stable or sometimes the mobile network takes priority and it switches between Wi-Fi and mobile network, while
                                 Jabber is unable to quickly connect to phone services during the handover. After Cisco Jabber for iPhone and iPad reconnects,
                                 users who have voicemail enabled in their account receive voicemail notifications for any missed calls that went to voicemail.
                                 To minimize the time to reconnect, users can bring the app to the foreground after changing connection environments. It is
                                 also recommended to enable Apple Push Notification service.

Cisco Webex Meetings — If the meeting siteType is ORION, then Cisco Jabber for iPhone and iPad cannot start Webex Meetings over Expressway for Mobile and Remote Access network.

If Cisco Jabber on iPhone is unable to reach the primary subscriber due to packet loss, it does not failover to secondary
                           CM node. For more information, see CSCux83785 .

If you are setting up Dial via Office - Reverse (DVO-R) on Cisco Unified Communications Manager consider the following:

The feature only applies to iPhone; it is not supported on iPad or iPod Touch devices because it requires that the device
                                 can access a mobile network.

You can make DvO-R calls over Expressway for Mobile and Remote Access when you are outside corporate network. DVO-R is supported
                                 over Cisco Expressway X8.7 and Cisco Unified Communications Manager 11.0(1a)SU1.

DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager 8.6 and above. Resetting the
                                 device from the Cisco Unified Communications Manager administrative interface fixes this issue.

The feature requires Cisco Unified Communications Manager Release 8.6.2 SU4, 9.1.2, or 10.x.

The feature cannot be used in conjunction with the Secure Call feature. Secure calls cannot be established if DVO-R is enabled.

Due to a limitation with Cisco Unified Communications Manager, if the user places a DVO-R call to an invalid phone number
                                 over a SIP trunk, the user hears several seconds of silence instead of an audio message stating the number was invalid.

If the user
                           				is on a Cisco Unified Communications Manager call and receives an incoming
                           				mobile call, iPhone starts ringing and prompts the user to answer or decline
                           				the mobile call. At the same time, the Cisco Unified Communications Manager
                           				call on Cisco Jabber goes on hold automatically.

To ensure that
                           				you do not miss incoming Cisco Jabber chats and calls, go to iOS
                                 					 Settings > Notification Center and check that the
                           				Cisco Jabber sound setting is turned on.

If you receive
                           				a Cisco Unified Communication Manager call, while placing a VoIP call, Cisco
                           				Jabber for iPhone and iPad sends the incoming call to voicemail. If you do not
                           				have voicemail, Cisco Jabber for iPhone and iPad ignores the call.

The maximum
                           				number of participants for ad-hoc conferences is limited to three; this is the
                           				maximum number of calls for TCT devices. The maximum participants for ad-hoc
                           				conference is configured on Cisco Unified Communication Manager in Service Parameter
                                 					 Configuration > Clusterwide Parameters > Maximum Ad Hoc Conference
                                 					 Required .

Voice and video quality over non-corporate Wi-Fi or mobile data networks cannot be guaranteed.

The quality of video calls varies depending on the network connection. Cisco Technical Assistance Center (TAC) cannot troubleshoot
                           video quality when you use 3G or 4G networks to connect Cisco Jabber for iPhone and iPad with Cisco AnyConnect Secure Mobility
                           Client or another VPN client.

If you receive
                           				an incoming call on your iPhone, the iPhone automatically disables the
                           				microphone for all other applications, and there is no time to inform your
                           				current caller that you need to take another call. If you accept the new
                           				incoming call, your Cisco Jabber for iPhone and iPad Cisco Unified
                           				Communications Manager call is automatically placed on hold, and you cannot
                           				return to it until you end the iPhone call. To work around this issue, decline
                           				the call and then tap Resume so that your current caller can hear you again. If
                           				your device is locked, quickly press the On/Off Sleep/Wake button twice to
                           				decline the call, and then tap Resume.

SIP Digest Authentication is not supported.

Cisco Unified
                           				Communications Manager as a directory source is capable of scaling to 50% of
                           				the device capacity that a Cisco Unified Communications Manager node can
                           				handle.

When the
                           				device is in Do Not Disturb (DND) mode and locked, then it vibrates upon
                           				receiving a Cisco Jabber call.

With iOS versions 10 and 11 with Cisco Jabber 12.0, you cannot receive call notifications on Apple Watch because CallKit can’t
                           work with Apple Watch. This is an Apple iOS limitation.

When in the background for a few hours, Jabber relaunches without
                           				notification.

### iPad

When users
                           				transition between networks, their availability status may not be accurate.

Cisco Jabber
                           				for iPhone and iPad supports interoperability and optimal video quality with
                           				Cisco TelePresence System (CTS) devices if you use a TelePresence or video
                           				bridge to connect the devices. The number of devices that you can use for
                           				joining a video call will be determined by the Multipoint Control Unit (MCU)
                           				and settings defined for the conference bridge.

All CTS devices must be using 1.9.1(68) or a later firmware
                                       							 version.

All CTS devices must be using 1.9.1(68) or a later firmware
                                             								  version.

Create Media Regions for iPad and CTS by following these steps:

Provision two media regions with the first region for CTS using a maximum video call bit rate of 32000 Kbps and second region
                                                   for iPad using a maximum video call bit rate of 768 Kbps.

Create a region relationship from the CTS region to the iPad region, described in step 1, using a maximum video call bit rate
                                                   of 512 Kbps.

Consult the
                           				Cisco Unified Communications Manager Administration documentation for details
                           				about setup.

You cannot
                           				block contacts who are within your own organization.

If you
                           				delete a group of contacts on another device other than an iPad, they may still
                           				appear in Cisco Jabber for iPhone and iPad. You will need to sign out and sign
                           				in for the changes to take effect.

If you start an action, such as signing in or tapping Webex Meeting to start a meeting, and then bring Cisco Jabber for iPhone and iPad to the background before the action is completed, you
                           cannot successfully complete the action.

If you tap Webex Meeting to start a meeting, a meeting invitation is sent when either the meeting starts or 60 seconds has elapsed.

When on a Cisco Jabber call and you put Cisco Jabber to the background, sometimes the call indicator will show Cisco Jabber
                           recording, depending on the iOS versions.

### Apple Watch

Notifications are not supported on Apple Watch in Jabber team messaging mode.

### Performance and Behavior Notes

#### Multiple Resource Login

When a user signs in to multiple instances of the client at the same time, the chat feature behaves as follows:

The first incoming chat message is sent to all the clients.

The first client to reply to the incoming chat message gets all the subsequent messages. The other clients do not get these
                              subsequent incoming messages.

If the client does not use the chat feature for 5 minutes, the next incoming message is sent to all the clients again.

#### Contact Resolution for Enterprise Groups

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

### Open Caveats in Release 12.6(2)

There are no new open caveats for this maintenance release.

### Resolved Caveats in Release 12.6(2)

Identifier

Severity

Headline

CSCvq55546

2

Jabber for iPhone has No MOH when it gets held by other phone

CSCvq65242

3

No audio issue raised by "Encountered severe clipping, resetting AEC."

### Open Caveats in Release 12.6(1)

There are no new open caveats for this maintenance release.

### Resolved Caveats in Release 12.6(1)

### Open Caveats in Release 12.6

### Resolved Caveats in Release 12.6

### This Document Applies to These Products

- Jabber for iPhone and iPad

| Important | Cisco supports only the current App Store version of Cisco Jabber for iPhone and iPad. Defects found in any Cisco Jabber
                                    for iPhone and iPad release are evaluated against current versions. |
|---|---|

| Apple Device | Version |
|---|---|
| iPad | 5th and 6th generation |
| iPad Air | Air 1 and Air 2 |
| iPad Pro | 9.7 and 10.5 inch 12.9 inch, 1st, 2nd and 3rd generation |
| iPad mini | Mini 2, mini 3, and mini 4 |
| iPhone | 5s, 6, 6 Plus, 6s, 6s Plus, 7, 7 Plus , 8, 8 Plus, X, Xs, Xs Max, XR and SE |
| iPod touch | 6th generation |
| Apple Watch | WatchOS 5 running on Apple Watch and Apple Watch 2, 3 and 4. |

| Manufacturer | Model(s) |
|---|---|
| Cisco | 561, 562 |
| Jabra | BIZ 2400, Easygo, Evolve 65 UC Stereo, EXTREME 2, Motion 1 , PRO 9470, Speak 450 for Cisco, Speak 510, Stealth Supreme UC, Wave + |
| Jawbone | ICON for Cisco Bluetooth Headset |
| Plantronics | Voyager Edge, Voyager Edge UC, Voyager Legend, Voyager Legend UC |
| Sony Eriksson | MW-600 |

| Required versions and settings for CTS interoperability |
|---|
| VCS call control environment: All CTS devices must be using 1.9.1(68) or a later firmware
                                       							 version. |
| Cisco Unified Communications Manager call control environment: All CTS devices must be using 1.9.1(68) or a later firmware
                                             								  version. Create Media Regions for iPad and CTS by following these steps: Provision two media regions with the first region for CTS using a maximum video call bit rate of 32000 Kbps and second region
                                                   for iPad using a maximum video call bit rate of 768 Kbps. Create a region relationship from the CTS region to the iPad region, described in step 1, using a maximum video call bit rate
                                                   of 512 Kbps. |
| To verify your VCS firmware and hardware codec versions, check
                                    						  the Device information screen in the Cisco TelePresence System Administration. |

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
| CSCvq55546 | 2 | Jabber for iPhone has No MOH when it gets held by other phone |
| CSCvq65242 | 3 | No audio issue raised by "Encountered severe clipping, resetting AEC." |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvp45050 | 2 | DTMF digits not transferred in time (within 50ms) |
| CSCvp42829 | 3 | Jabber for iphone 12.6 "Search for Call" field not displayed without a contact/group |
| CSCvp24475 | 3 | Unable to place a call with native call application after iPhone wakes up |
| CSCvq13803 | 3 | Jabber does not show hunt pilot information |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvp13523 | 3 | Messages & Files search results fetched are not the same as Teams client. |
| CSCvp13630 | 3 | Contact service 'search more' API return empty result. |
| CSCvp13640 | 3 | Inconsistent presence in Jabber teams mode against Webex Teams client. |
| CSCvp13659 | 3 | No space list is shown after login. |
| CSCvp13684 | 3 | Unexpected unread status for one old space after sign out. |
| CSCvp13698 | 3 | Many trivial threads created by cpprest when day0 login. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvo43104 | 2 | Jabber with Hybrid (WebEx Messenger) and on-prem phone services is getting forced to sign-out. |
| CSCvn75049 | 3 | Jabber for iPad BFCP share does not allow Single layout by default. |
| CSCvn76823 | 3 | Missing Call State Notification With Custom Java Script on Jabber for iOS. |
| CSCvn82423 | 3 | Could not reach 20fps when using high definition video even in a good network. |
| CSCvo13245 | 3 | J4IOS- Add contact failed warn 'Adding this contact will exceed the maximum limit of 1000 contacts'. |
| CSCvo31907 | 3 | Jabber sending non-batch request after receiving 200 ok for batch request. |
| CSCvo42923 | 3 | Jabber sends single number UDS query if batch number query returns empty results. |