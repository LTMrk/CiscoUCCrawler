---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-8-jabi-b-release-notes-128-html-fe9aad92e3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_8/jabi_b_release-notes-128.html
retrieved_at: 2026-08-21T07:01:01.098818+00:00
---

Release Notes for Cisco Jabber for iPhone and iPad 12.8

# Release Notes for Cisco Jabber for iPhone and iPad 12.8

First Published: January 22, 2020

Last Updated: May 31, 2021

## EMM Support for Microsoft Intune and BlackBerry Dynamics

Enterprise Mobility Management (EMM) supports two new clients:

Cisco Jabber for Intune

Cisco Jabber for BlackBerry

Your organization can deploy these clients to enforce policies for using Jabber on mobile devices in deployments that allow
                     "Bring Your Own Device".

Use the new EMMType parameter to control the Jabber clients on which your users can sign in.

For details, see the following guides:

Planning Guide for Cisco Jabber

Jabber deployment guides

Parameters Reference Guide for Cisco Jabber

### Cisco Jabber for Intune

For Microsoft Intune, your administrator sets up protection policies in Microsoft Azure to control use of the Jabber for Intune
                     client. Users download the new client from the App Store or Google Play Store. When the user runs the new client, it synchs
                     with the policies that the administrator created.

For Android devices, users first install and sign into the Intune Company Portal on their device to get the protection policies
                     from Azure.

### Cisco Jabber for BlackBerry

For BlackBerry Dynamics, your administrator sets up policies in the BlackBerry Unified Endpoint Management (UEM) to control
                     use of the Jabber for BlackBerry client. Users download the new client from the App Store or Google Play Store. The new client
                     has integrated the BlackBerry SDK and can directly fetch the policies from BlackBerry UEM.

### Cisco Jabber for BlackBerry Release 12.8(1)

Cisco Jabber for BlackBerry 12.8(1) is now available in the App Store and Google Play Store. Jabber for BlackBerry is undergoing
                        BlackBerry certification and isn’t yet available in BlackBerry Marketplace.

This release on iOS adds support for these features:

Using BlackBerry Works to send emails. Your administrator has to enable the DLP policy in the BlackBerry UEM.

Using BlackBerry Access for SSO authentication. Your administrator has to enable Use native browser for iOS on Expressway and Unified Communications Manager. They also have to the ciscojabber scheme to the BlackBerry access policies in the BlackBerry UEM.

Support for some MDM parameters, such as ServicesDomain , VoiceServicesDomain , ServiceDiscoveryExcludedServices , and ServicesDomainSsoEmailPrompt .

### Cisco Jabber for BlackBerry Release 12.8(2)

Cisco Jabber for BlackBerry 12.8(2) contains stability improvements.

## Additional Maintenance Releases

For additional maintenance release information, refer to:

Feature enhancements  — see https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html for the latest version of release
                           notes.

Caveats — see https://bst.cloudapps.cisco.com/bugsearch/ for latest caveat updates.

Security Advisories — see https://tools.cisco.com/security/center/publicationListing.x for a listing of the latest advisories.

## What's New in Release 12.8(3)

### Customized Deployments with Automatic Sign-In

We've added a way to deploy Jabber so that it signs in and connects to services automatically, without a user manually entering
                     a username and password. For these customized deployments, you must use a third-party enterprise mobility management (EMM)
                     system, such as Microsoft Intune. To set up this feature, your EMM configuration must include the ServicesDomain parameter and two new parameters: AutoLoginUserName and AutoLoginUserPassword . For more information, see the chapter "Deploy Cisco Jabber Applications and Jabber Softphone for VDI" in the deployment
                     guides.

## What's New in Release 12.8(2)

### Answer Calls Automatically with Guided Access

You can now configure Jabber for iPhone and iPad to answer calls automatically, which lets callers connect to users who aren't
                     able to answer calls on their own. The AutoAnswerForGuidedAccess parameter lets you add this option to the client settings. This parameter works together with Guided Access, an accessibility
                     feature of iOS that limits a device to a single app. See the Parameters Reference Guide for more information.

## What's New in Release 12.8(1)

### Force a Reset When User Signs Out

This release adds the ResetOnLogOutOnMobile parameter to force an automatic reset of the client when the user signs out. The Sign Out button changes to Reset Jabber when you set this parameter.

### More Visible Phone Service Disconnection Warnings

This release adds the GlobalPhoneServiceErrorOnMobile parameter to make the error message more visible to the user when the phone service is registered on another device. When
                     you set this parameter to true, the error message appears at the top of the client, rather than in the Calls tab.

## What's New in Release 12.8

### Call Pickup Support

Users can now use Call Pickup on their mobile devices. Call Pickup allows users to pick up others' incoming calls in various
                     answer groups. You configure answer groups on the server side. You configure this feature in Jabber using the following existing
                     parameters:

EnableCallPickup (default: false)

EnableOtherGroupPickup (default: false)

EnableGroupCallPickup (default: false)

For more information about how call pickup works, see the Feature Configuration for Cisco Jabber guide.

### Hunt Group Enhancements

You can now sign in or out of hunt groups on mobile clients.

For more information, see the hunt group section in the Feature Configuration for Cisco Jabber guide.

### Voicemail Improvements

We extended the Release 12.7 voicemail improvements from the desktop clients to the mobile clients.

Users can create voicemails without making a call and then send the voicemail to one or more contacts. The voicemail server's
                     administrator can also create distribution lists to which users can send voicemails. Users can select recipients from the
                     voicemail server's catalog.

Users can directly reply to the sender of a voicemail or to all recipients of that message. Users can also forward voicemails
                     to new recipients.

### Custom Contacts for Team Messaging Mode

Jabber Team Messaging Mode deployments support custom contacts. You can now create, edit, and delete custom contacts on a
                     desktop client. These contacts are also available in your mobile client. But, you can't create, edit, or delete custom contacts
                     from the mobile client.

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

### Operating Systems for Cisco Jabber for iPhone and iPad

Refer to the App Store for the latest supported operating system version information.

Cisco supports only the current App Store version of Cisco Jabber for iPhone and iPad. Defects found in any Cisco Jabber
                                    for iPhone and iPad release are evaluated against current versions.

### Hardware Requirements for Cisco Jabber for iPhone and iPad

The following Apple devices are supported for Cisco Jabber for iPhone and iPad on iOS 12.X, iOS 13.X, and iPadOS. The devices that are not upgraded to these versions are not supported.

Apple Device

Version

iPad

5th, 6th, and 7th generation

iPad Air

Air 1, Air 2, and Air 3

iPad Pro

9.7 and 10.5 inch

12.9 inch, 1st, 2nd and 3rd generation

iPad mini

Mini 2, mini 3, mini 4, and mini 5

iPhone

5s, 6, 6 Plus, 6s, 6s Plus, 7, 7 Plus , 8, 8 Plus, X, Xs, Xs Max, 11, 11 Pro, 11 Pro Max, XR and SE

iPod touch

6th generation

Apple Watch

WatchOS 5 running on Apple Watch and Apple Watch 2, 3 and 4.

The following Bluetooth headsets are supported on iPhone and iPad:

Manufacturer

Model(s)

Apple

AirPod

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

Apple has new requirements for trusted certificates in iOS 13 (see https://support.apple.com/en-us/HT210176 ). Ensure that the certificates on the Unified Communications Mananger, IM & Presence, and Expressway servers meet these requirements.
                           If your certificates don't meet these requirements, Jabber prompts users to accept the certificates for each session.

Webex site disclaimers don't appear when you join Webex meetings from Jabber. This limitation applies whether joining from
                           the meeting reminder popup, or by selecting Join in Webex in Jabber.

If you make a Cisco Jabber for iPhone and iPad call using Expressway for
                           						Mobile and Remote Access over a 2G, 3G, or 4G network, you may experience
                           						audio quality issues from network instability.

Applies to Cisco TelePresence Video Communication Server Control (VCS) versions earlier than 8.10.X.

Configure the editable inbound rules to enable single number reach for those who use Cisco Jabber over Mobile and Remote Access.
                           For more information, see Limitations in Enable Single Number Reach section from the Feature Configuration Guide for Cisco Jabber 12.0 .

Cisco Jabber for mobile clients don't show the Favorite icon for users with Phone Only account.

Without Apple Push Notifications (APNs), when Cisco Jabber receives an incoming call or chat, the iOS doesn't wake Cisco Jabber.
                           The call or instant message appears on the device after several minutes or when you bring Cisco Jabber the foreground. As
                           a workaround, reset the network settings for your iOS device by going to Settings > General > Reset > Reset Network Settings .

Users can no
                           				longer edit their Phone Services servers manually, except when they are in
                           				hybrid cloud mode. In hybrid deployments, administrators can configure the
                           				Phone Services servers to be editable.

The first usage of Secure Phone functionality must be on the corporate network or VPN to ensure proper certificate installation.

Voice recognition for voicemail PIN is highly sensitive to background noise. The system may interpret background noise as
                           user input, even when the user doesn't input anything. See System Administration Guide for Cisco Unity Connection to disable this function. https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html

Certificate validation windows pop up when the certificate on Cisco Unified Communications Manager is issued by an intermediate
                           certificate authority. Use a certificate that is signing with the root rather than an intermediate certificate authority.

From Release 10.5 onward, all the Cisco Jabber account related files, including Configuration, Contacts, Credentials, History,
                           Logs, Photo and so on, aren't backed up on the iCloud and iTunes due to privacy reasons.

Creating and Configuring Devices for Users in Cisco Unified Communications Manager 11.0—If you are creating devices for users
                           in Cisco Unified Communications Manager 11.0, you can now specify a key order as RSA Only, EC Only, EC Preferred, or RSA Backup.
                           However, the EC Only option is not currently supported by Cisco Jabber, and if you select it, the client fails to connect
                           to the server.

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

If you delete a group of contacts on another device other than an iPad, they may still appear in Cisco Jabber for iPhone
                           and iPad. Sign out and then sign in again for the changes to take effect.

If you start an action, such as signing in or tapping Webex Meeting to start a meeting, and then bring Cisco Jabber for iPhone and iPad to the background before the action completes, you can't
                           successfully complete the action.

If you tap Webex Meeting to start a meeting, the system sends a meeting invitation when either the meeting starts or 60 seconds has elapsed.

When on a Cisco Jabber call and you put Cisco Jabber to the background, sometimes the call indicator shows Cisco Jabber recording,
                           depending on the iOS versions.

### Apple Watch

Notifications aren't supported on Apple Watch in Jabber team messaging mode.

## Performance and Behavior Notes

### Multiple Resource Login

When a user signs in to multiple instances of the client at the same time, the chat feature behaves as follows:

The first incoming chat message is sent to all the clients.

The first client to reply to the incoming chat message gets all the subsequent messages. The other clients do not get these
                           subsequent incoming messages.

If the client does not use the chat feature for 5 minutes, the next incoming message is sent to all the clients again.

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

### Resolved Caveats in Release 12.8(3)

Identifier

Severity

Headline

CSCvt95763

3

Jabber 12.8.1 and 12.8.2 fails to get phone services over MRA

### Resolved Caveats in Release 12.8(1)

Identifier

Severity

Headline

CSCvt17368

3

Jabber for iOS 12.8 unable to login via MRA using OAuth2.0

### Open Caveats in Release 12.8

Identifier

Severity

Headline

CSCvs56188

3

Jabber iOS (Non APNS setup) goes offline after keeping Jabber Idle for 3-8 Mins - after iOS upgrade

CSCvs58595

3

Mute all in CMR meeting cannot work after assign host

### Resolved Caveats in Release 12.8

Identifier

Severity

Headline

CSCvr12542

3

Jabber does not refresh access token in failover scenario over MRA

CSCvr97701

3

Jabber for iOS crashes when searching contacts

CSCvs51394

3

Jabber for iPhone version 12.7 the search menu disappears when seraching contacts

### This Document Applies to These Products

- Jabber for iPhone and iPad

| Note | This release note describes a new feature in Webex Control Hub that impacts Jabber deployments. Because it’s a change in Control
                                 Hub, you can access this feature for any release of Jabber. |
|---|---|

| Important | Cisco supports only the current App Store version of Cisco Jabber for iPhone and iPad. Defects found in any Cisco Jabber
                                    for iPhone and iPad release are evaluated against current versions. |
|---|---|

| Apple Device | Version |
|---|---|
| iPad | 5th, 6th, and 7th generation |
| iPad Air | Air 1, Air 2, and Air 3 |
| iPad Pro | 9.7 and 10.5 inch 12.9 inch, 1st, 2nd and 3rd generation |
| iPad mini | Mini 2, mini 3, mini 4, and mini 5 |
| iPhone | 5s, 6, 6 Plus, 6s, 6s Plus, 7, 7 Plus , 8, 8 Plus, X, Xs, Xs Max, 11, 11 Pro, 11 Pro Max, XR and SE |
| iPod touch | 6th generation |
| Apple Watch | WatchOS 5 running on Apple Watch and Apple Watch 2, 3 and 4. |

| Manufacturer | Model(s) |
|---|---|
| Apple | AirPod |
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
| CSCvt95763 | 3 | Jabber 12.8.1 and 12.8.2 fails to get phone services over MRA |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvt17368 | 3 | Jabber for iOS 12.8 unable to login via MRA using OAuth2.0 |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvs56188 | 3 | Jabber iOS (Non APNS setup) goes offline after keeping Jabber Idle for 3-8 Mins - after iOS upgrade |
| CSCvs58595 | 3 | Mute all in CMR meeting cannot work after assign host |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvr12542 | 3 | Jabber does not refresh access token in failover scenario over MRA |
| CSCvr97701 | 3 | Jabber for iOS crashes when searching contacts |
| CSCvs51394 | 3 | Jabber for iPhone version 12.7 the search menu disappears when seraching contacts |