---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-ios-jabi-b-releasenotes-125-html-a535038b05
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/iOS/jabi_b_releasenotes_125.html
retrieved_at: 2026-08-21T07:01:13.899499+00:00
---

Release Notes for Cisco Jabber for iPhone and iPad 12.5

# Release Notes for Cisco Jabber for iPhone and iPad 12.5

### Download Options

Updated: January 29, 2019

First Published: November 29, 2018

Last Updated: January 29, 2019

# What’s New in Cisco Jabber for iPhone and iPad 12.5(1)

## Resolved Caveats

This release provides fixes for a number of known issues. See the Resolved Caveats 12.5(1) section for a list of caveats fixed
                  in this release.

## What's New in Cisco Jabber for iPhone and iPad 12.5

### Preview Features are now Fully Supported

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

### Better Conferencing

ActiveControl — ActiveControl provides enhanced conferencing features to Cisco Jabber, like the ability to choose the video layout, record
                     the call, mute and unmute yourself and others, and locking the conference call. You set up ActiveControl in Cisco Meeting
                     Server (CMS) 2.3 or later and need Cisco Unified Communications Manager 10.5 or later. We've put more information in the Features Guide for Cisco Jabber 12.5 about how to set it up.

New User Experience —Jabber looks even better now, with updated icons and a better layout.

### Easier Client Configuration

Common Criteria —You can now run Jabber for iPhone and iPad in Common Criteria mode, which ensures that the environment is compliant with
                           Common Criteria requirements. You turn on Common Criteria mode by using the CC_mode=true parameter in your EMM. For more information, see Common Criteria in the Planning Guide for Cisco Jabber 12.5 , and CC_mode in the section on Deploy Cisco Jabber Applications in the Deployment Guides.

### Mobile Management and Headsets

New Devices and OS Support —Jabber supports new iOS versions and phones, and no longer supports iOS version 10.

Easier Sign In —You can pre-define a user on a mobile device using the LastLoadedUserProfile parameter in your Enterprise Mobility Management, so that the user only needs to enter their password to sign in to the device.
                           More information about this parameter is in the On-Premises Deployment Guide for Cisco Jabber 12.5 or Cloud Deployment Guide for Cisco Jabber 12.5 .

## Requirements

### Cisco Jabber Requirements

Many Cisco Jabber requirements are common between client types. Client specific requirements are documented in the Release Notes , all other requirements are documented in the Planning Guide for Cisco Jabber .

### Operating Systems for Cisco Jabber for iPhone and iPad

Refer to the App Store for the latest supported operating system version information.

Cisco supports only the current App Store version of Cisco Jabber for iPhone and iPad. Defects found in any Cisco Jabber
                                    for iPhone and iPad release are evaluated against current versions.

### Hardware Requirements for Cisco Jabber for iPhone and iPad

The following Apple devices are supported for Cisco Jabber for iPhone and iPad on iOS 11.X . The devices that are not upgraded to these versions are not supported.

Apple Device

Generation

iPad

Third, fourth, fifth, sixth 12.9 inch iPad Pro (first and second) , 10.5 inch iPad Pro, 9.7 inch iPad Pro,

iPad Air

Air 1 and Air 2

iPad mini

Mini 2, mini 3, and mini 4

iPhone

5, 5c, 5s, 6, 6 Plus, iPhone SE , 6s, and 6s Plus, 7 and 7 Plus, 8 and 8 Plus , iPhone X, XR, XS, and XS Max, and Apple Watch

iPod touch

5 and 6

The following Bluetooth headsets are supported on iPhone and iPad:

Manufacturer

Model(s)

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

- The first usage of Secure
                        			 Phone functionality must be on the corporate network or VPN to ensure proper
                        			 certificate installation.

- Voice recognition for voicemail PIN is highly sensitive to the background noise and may interpret background noise as user
                        input when the user doesn't input anything. Refer to System Administration Guide for Cisco Unity Connection to disable this function. https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html

- Certificate validation
                        			 windows pop up when the certificate on Cisco Unified Communications Manager is
                        			 issued by an intermediate certificate authority. Use a certificate that is
                        			 signing with the root rather than an intermediate certificate authority.

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

iOS may shut down Cisco Jabber and other applications that are running in the background to preserve resources. While the
                                    client attempts to relaunch, there is a possibility that calls may be missed. To minimize the impact, it is recommended to
                                    enable Apple Push Notification service.

The device sometimes switches connection from the Wi-Fi data network to the mobile voice network while the device is in Sleep
                                    mode. Incoming calls may be missed due to this issue. To prevent this issue, go to the iPhone Settings and turn off Cellular Data or alternatively turn on SNR .

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

The
                                    					 feature only applies to iPhone; it is not supported on iPad or iPod Touch
                                    					 devices because it requires that the device can access a mobile network.

You can
                                    					 make DvO-R calls over Expressway for Mobile and Remote Access when you are
                                    					 outside corporate network. DVO-R is supported over Cisco Expressway X8.7 and
                                    					 Cisco Unified Communications Manager 11.0(1a)SU1.

DVO
                                    					 enabled devices may encounter issues registering with Cisco Unified
                                    					 Communications Manager 8.6 and above. Resetting the device from the Cisco
                                    					 Unified Communications Manager administrative interface fixes this issue.

The
                                    					 feature requires Cisco Unified Communications Manager Release 8.6.2 SU4, 9.1.2,
                                    					 or 10.x.

The
                                    					 feature cannot be used in conjunction with the Secure Call feature. Secure
                                    					 calls cannot be established if DVO-R is enabled.

Due to a
                                    					 limitation with Cisco Unified Communications Manager, if the user places a
                                    					 DVO-R call to an invalid phone number over a SIP trunk, the user hears several
                                    					 seconds of silence instead of an audio message stating the number was invalid.

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

- Voice and video quality
                        			 over non-corporate Wi-Fi or mobile data networks cannot be guaranteed.

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

- SIP Digest Authentication
                        			 is not supported.

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

Provision two media regions with the first region for CTS using
                                                      										a maximum video call bit rate of 32000 Kbps and second region for iPad using a
                                                      										maximum video call bit rate of 768 Kbps.

Create a region relationship from the CTS region to the iPad
                                                      										region, described in step 1, using a maximum video call bit rate of 512 Kbps.

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

- When on a Cisco Jabber
                        			 call and you put Cisco Jabber to the background, sometimes the call indicator
                        			 will show Cisco Jabber recording, depending on the iOS versions.

### Performance and Behavior Notes

#### Multiple Resource Login

- The first incoming chat message is sent to all the clients.

- The first client to reply to the incoming chat message gets all the subsequent messages. The other clients do not get these
                              subsequent incoming messages.

- If the client does not use the chat feature for 5 minutes, the next incoming message is sent to all the clients again.

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

### Resolved Caveats in Release 12.5(1)

### Open Caveats in Release 12.5(1)

### Resolved Caveats in Release 12.5

### Open Caveats in Release 12.5

### This Document Applies to These Products

- Jabber for iPhone and iPad

| Important | Cisco supports only the current App Store version of Cisco Jabber for iPhone and iPad. Defects found in any Cisco Jabber
                                    for iPhone and iPad release are evaluated against current versions. |
|---|---|

| Apple Device | Generation |
|---|---|
| iPad | Third, fourth, fifth, sixth 12.9 inch iPad Pro (first and second) , 10.5 inch iPad Pro, 9.7 inch iPad Pro, |
| iPad Air | Air 1 and Air 2 |
| iPad mini | Mini 2, mini 3, and mini 4 |
| iPhone | 5, 5c, 5s, 6, 6 Plus, iPhone SE , 6s, and 6s Plus, 7 and 7 Plus, 8 and 8 Plus , iPhone X, XR, XS, and XS Max, and Apple Watch |
| iPod touch | 5 and 6 |

| Manufacturer | Model(s) |
|---|---|
| Jabra | BIZ 2400, Easygo, Evolve 65 UC Stereo, EXTREME 2, Motion 1 , PRO 9470, Speak 450 for Cisco, Speak 510, Stealth Supreme UC, Wave + |
| Jawbone | ICON for Cisco Bluetooth Headset |
| Plantronics | Voyager Edge, Voyager Edge UC, Voyager Legend, Voyager Legend UC |
| Sony Eriksson | MW-600 |

| Required versions and settings for CTS interoperability |
|---|
| VCS call control environment: All CTS devices must be using 1.9.1(68) or a later firmware
                                       							 version. |
| Cisco Unified Communications Manager call control environment: All CTS devices must be using 1.9.1(68) or a later firmware
                                             								  version. Create Media Regions for iPad and CTS by following these steps: Provision two media regions with the first region for CTS using
                                                      										a maximum video call bit rate of 32000 Kbps and second region for iPad using a
                                                      										maximum video call bit rate of 768 Kbps. Create a region relationship from the CTS region to the iPad
                                                      										region, described in step 1, using a maximum video call bit rate of 512 Kbps. |
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
| CSCvn85471 | 2 | Call entries are replaced with the name of the user where the call is forwarded. |
| CSCvn88873 | 2 | Jabber on mobile 12.5 over MRA dropping calls randomly. |
| CSCvn83242 | 3 | DTMF digits RTP packets with incorrect timestamp. |
| CSCvn57594 | 3 | Jabber IOS does not show Hunt Pilot Number. |
| CSCvn45734 | 3 | Jabber "All Rooms" tab does not load. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvn82423 | 3 | Could not reach 20fps when using high definition video even in good network. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvn20659 | 2 | Jabber is case sensitive with server name. |
| CSCvj58867 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after hold/resume. |
| CSCvj58876 | 3 | Jabber keeps Rollover Counter and SSRC of SRTP stream after transfer. |
| CSCvk48133 | 3 | Jabber SIP Header Missing IP Address after '@'. |
| CSCvk48728 | 3 | Jabber for iPhone user authentication with IM&P does not time out. |
| CSCvk54389 | 3 | Jabber voicemail does not consider ipSecVPN sometimes. |
| CSCvm21505 | 3 | The ringtone set on the Jabber for iphone client is ignored. |
| CSCvm84398 | 3 | jabber over MRA not sending Content-Length on REGISTER signaling. |
| CSCvm91213 | 3 | Jabber for iPhone one way audio when the recording is enabled. |
| CSCvi23850 | 4 | Jabber sending query to external DNS when connecting via MRA. |
| CSCvk64132 | 6 | Jabber for iOS APNS does not work because Jabber does not return ACK for TCP FIN from CUCM. |

| Identifier | Severity | Headline |
|---|---|---|
| CSCvk79433 | 3 | Crash at NSProgress which is Apple's issue. |
| CSCvn45734 | 3 | Jabber All Rooms tab does not load. |