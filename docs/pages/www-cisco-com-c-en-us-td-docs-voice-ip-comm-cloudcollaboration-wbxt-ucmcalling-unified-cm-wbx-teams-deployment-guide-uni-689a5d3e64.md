---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-wbxt-ucmcalling-unified-cm-wbx-teams-deployment-guide-uni-689a5d3e64
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_chapter_011.html
retrieved_at: 2026-08-16T19:34:14.908176+00:00
---

Deployment guide for Calling in Webex App (Unified CM)

# Deployment guide for Calling in Webex App (Unified CM)

Updated: November 10, 2025

Chapter: Prepare your environment for Calling in Webex App (Unified CM)

## Chapter: Prepare your environment for Calling in Webex App (Unified CM)

# Prepare your environment for Calling in Webex App (Unified CM)

## Call control environment requirements

To enable Calling in Webex App (Unified CM), you must use one of the supported Unified CM-based
                              Cisco call control solutions, and ensure that you're on the minimum
                              supported version or later.

Minimum

Unified CM Release 11.5(1) SU3 and later for
                                                      desktop.

While not mandatory, this minimum also release
                                                      supports Firebase Cloud Messaging (FCM) push
                                                      notifications on Android.

For an 11.5 release, Unified CM Release 11.5(1)
                                                      SU8 or a later SU is required minimum for Apple
                                                      Push Notification (APN) service on iOS mobile
                                                      devices. (This release is not supported in China.
                                                      See below.)

For a 12.5 release, Unified CM Release 12.5(1)
                                                      SU3 or a later SU is required for iOS APN
                                                      support.

Unified CM Release 12.5(1) and later

CAPF is not supported.

Recommended

Unified CM Release 12.5(1) SU3 or later.** This
                                                      recommended release ensures that push
                                                      notifications work for all mobile platforms in
                                                      your environment and that secure calling is
                                                      supported.

See Push Notifications for
                                                      more information.

If your organization is based in China, you
                                                                  must use this version at a minimum.

If you use Mobile Remote Access (MRA) and want
                                                      to configure MRA failover, Unified CM Release 14.0
                                                      or later is required.

Cisco Business Edition

Check the software load summary documentation
                                          for BE6K and BE7K to ensure the
                                          solution is running a supported version of Unified
                                          CM.

11.5 and later at a minimum.

12.5 and later is recommended for SIP Oath
                                          encrypted calls support. (CAPF is not
                                          supported.)

Cisco Unified Communications Manager Cloud

—

* For voicemail integration in Webex App , we recommend that the Cisco Unity Connection version
                                 match the Unified CM version. However, make sure the
                                 authentication method and credentials are the same across
                                 both servers.

** In alignment with Apple's changes to the iOS notification
                                 architecture, Cisco Webex App is implementing Apple Push Notification support for
                                 notifications. We highly recommend that customers upgrade
                                 Cisco Unified Communications Manager, Cisco Expressway, and
                                 Cisco Webex App as soon as possible. Failure to upgrade on time will
                                 result in loss of voice notification for Cisco Webex App users using Unified Communications Manager and IM
                                 notifications for Cisco Webex App iOS users. For up to date support information that is
                                 related to Push Notifications with iOS 13, including upgrade
                                 requirements, refer to Apple Push Notification Service
                                    Updates .

While not required, if you want Mobile and Remote Access (MRA) support
                              (so Webex App can be used in softphone mode outside the corporate network), you
                              must use a Cisco Expressway traversal pair, and ensure that you're
                              on the minimum supported version or later.

X8.11.4 or later is required for
                                          Calling in Webex App (Unified CM). See the "Important Information"
                                          section in the Expressway Release Notes for more information. This release and later
                                          provide added security.

X12.6 or later for Push Notifications.

If you use Mobile Remote Access (MRA) and want
                                          to configure MRA failover, Expressway Release
                                          X14.0 or later is required.

See the Mobile and Remote Access via Expressway Deployment Guide for more information.

## Unified CM feature requirements

Many Unified CM features are automatically available in Webex App after you configure your environment. However, certain features need to be preconfigured in Unified CM for them to work in Webex App .

### Auto answer with tone on connect

You can configure auto answer on a directory number that is assigned to the user. See
                                 the System Configuration Guide for Cisco Unified Communications Manager for your release at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html and see the Cisco Unified CM Administration
                                 online help for more information about the Auto Answer setting.

For an agent on Webex to hear a tone before the call connects, choose True for
                                 the Tone on connect Cisco CallManager service parameter. This parameter
                                 determines whether a tone plays to indicate that media starts to stream. The valid
                                 values for this parameter are True, which plays a tone, or False, which does not
                                 play a tone, and the default is False. This Global Parameter affects all the users
                                 in the cluster.

### Centralized call history

With this release, the use of centralized or synchronized or common call history is enabled on Webex App (Unified CM) and
                                 desk phones. It provides a better user experience. This feature is supported from Webex 44.11 and Unified CM 14 SU4 or 15
                                 SU2.

To use this feature, you must onboard the Unified Communications Manager node through Webex Cloud-Connected UC. For more information,
                                 see Set up Webex Cloud-Connected UC for on-premises devices .

#### Enable call history

Call History feature is enabled by default for Webex Calling and Unified CM Cloud customers.

You can configure the centralized call history on the Control Hub and the Unified CM user interface.

#### Control Hub

Perform the following steps:

Sign in to Control Hub .

Go to Services > Connected UC . On the UC Management card, click Inventory .

The list of cluster groups appears with the description, status, clusters, and nodes.

Click Details next to the Unified CM (CUCM) cluster group on which you need to enable call history toggle.

The Inventory page appears, showing the list of clusters belonging to the selected cluster group.

Click Details next to the cluster to which the particular product node belongs.

The Node name with the version, product, and status appears.

Click the ellipsis ⋮ icon next to Event History and choose Service Management .

The Service Management page appears with the list of services.

Use the toggle button to enable the Centralized Call History .

Click Submit .

If the Data Collection Confirmation pop-up is displayed, agree to it by enabling the check box and click Submit .

#### Unified CM

Perform the following steps:

Match the CI Webex email account the mailid of Unified CM user.

For example, the Webex email account alice@company.com should match with Unified CM user Alice's mailid alice@company.com .

Associate the user with each line on each device type.

Go to the CSF device configuration .

Select line 1 .

Associate this line to user ID alice .

Repeat the steps on each device type (SEP, CSF, TCT, BOT, TAB); if user ID alice has multiple lines configured, associate each line to the user ID.

For more information, see the Whitepaer on Bulk Configure Changes with Import/Export Feature .

#### Limitation

Only the Webex app gets the centralized call history from the cloud, IP phone don’t get any call history from the cloud.

#### Known Issues

The following are the known issues:

[Centralized Call History] Webex UCM Calling enhance call history for mobile phone number

Call History record is not getting generated for Calling Party

Webex app and Webex plugin for MS Teams does not show call history for call made from EM profile

### Call Park

The Call Park feature allows you to place a call on hold so that can be retrieved
                                 from another phone or soft client in the Unified Communications Manager system (for
                                 example, a phone in another office or the Webex app). If you are on an active call,
                                 you can park the call to a call park extension by clicking Park in Webex. Another
                                 phone or soft client in your system can then dial the call park extension to
                                 retrieve the call.

For more information about call park configuration, see "Call Park and Directed
                                    Call Park" in the Feature Configuration Guide for Cisco Unified
                                    Communications Manager for your release at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

### Call Recording

Call Recording enables a recording server to archive agent conversations. Webex App supports this feature for Unified CM-based
                                 deployments.

Some releases of Unified CM require a device package to enable recording capabilities. To confirm, verify that the Built In Bridge field is available in the Phone Configuration window for the device. If the field isn’t available, download and apply the most recent device packages.

For detailed information about how to configure call recording, see the "Recording" chapter in the Feature Configuration Guide for Cisco Unified Communications Manager .

For configuration parameters that you can
                                 configure in the Jabber Config XML file or client
                                 configuration service, see the Feature Parameters
                                 table in the Appendix in this guide.

### Dial Plan
                              		Mapping

You configure dial
                                 		  plan mapping to ensure that dialing rules on 
                                 		  Cisco Unified Communications Manager match dialing rules on your
                                 		  directory.

#### Application
                                 		  Dial Rules

Application dial
                                 		  rules automatically add or remove digits in phone numbers that users dial.
                                 		  Application dialing rules manipulate numbers that users dial from the client.

For example, you
                                 		  can configure a dial rule that automatically adds the digit 9 to the start of a
                                 		  7 digit phone number to provide access to outside lines.

#### Directory
                                 		  Lookup Dial Rules

Directory lookup
                                 		  dial rules transform caller ID numbers into numbers that the client can lookup
                                 		  in the directory. Each directory lookup rule you define specifies which numbers
                                 		  to transform based on the initial digits and the length of the number.

For example, you
                                 		  can create a directory lookup rule that automatically removes the area code and
                                 		  two-digit prefix digits from 10-digit phone numbers. An example of this type of
                                 		  rule is to transform 4089023139 into 23139 .

### Dial Via Office Reverse

The Dial via Office (DvO) feature allows users to initiate Webex App outgoing calls with their work number using the mobile voice network for the device.

Mobile users having Mobile Identity (MI) configured cannot place or receive calls. Install the ciscocm.V15SU2_CSCwm77174-multiline_v1.zip file from CCO to use this feature. This feature is supported from Webex 44.12 and Unified CM 15 SU2.

Webex App supports DvO-R (DvO-Reverse) calls, which work as follows:

User initiates a DvO-R call.

The client notifies Cisco Unified Communications Manager to call the mobile phone number.

Cisco Unified Communications Manager calls and connects to the mobile phone number.

Cisco Unified Communications Manager calls and connects to the number that the user dialed.

Cisco Unified Communications Manager connects the two segments.

The user and the called party continue as with an ordinary call.

The users do not receive incoming calls on Webex App in the following situations:

If users select the Mobile Voice Network calling option on any network and the Single Number Reach (SNR) is not configured for their device, they will not receive
                                                   incoming calls on Webex App .

If users select the Mobile Voice Network calling option on any network and the Single Number Reach (SNR) is configured with the Ring Schedule , they will not receive incoming calls on Webex App beyond the time set in the Ring Schedule .

The following table describes the calling methods used for incoming and outgoing calls. The calling method (VoIP, DvO-R, or
                                 cellular call) varies depending on the selected Calling Options and the network connection.

Connection

Calling Options

Voice over IP

Mobile Voice Network

Autoselect

Wi-Fi

Outgoing: VoIP

Incoming: VoIP

Outgoing: DvO-R

Incoming: VoIP

Outgoing: VoIP

Incoming: VoIP

Mobile Network (3G, 4G, 5G)

Outgoing: DvO-R

To set up DvO-R, follow the steps in Configuring Dial via Office-Reverse to Work with Mobile and Remote Access .

### Extend and Connect

The Extend and Connect feature allows administrators to deploy Unified Communications Manager (UC) Computer Telephony Integration
                                 (CTI) applications that interoperate with any endpoint. With Extend and Connect, users can access UC applications from any
                                 location using any device.

Users can only add and edit numbers for existing devices. You
                                             must configure at least one device for users. If no device
                                             exists, then even if this feature is enabled, users won't
                                             see it as an option in Webex App .

See Configure Extend and Connect for more information.

### Move call to mobile

Users can transfer an active VoIP call from the Webex App to their mobile phone number on the mobile network. This feature is useful when a
                                 user on a call leaves the Wi-Fi network (for example, leaving the building to walk
                                 out to the car), or if there are voice quality issues over the Wi-Fi network.

#### Before you begin

Set up a mobile identity for users .

Mobile users having Mobile Identity (MI) configured cannot place or receive calls. Install the ciscocm.V15SU2_CSCwm77174-multiline_v1.zip file from CCO to use this feature. This feature is supported from Webex 44.12 and Unified CM 15 SU2.

Step 1

From Cisco Unified CM Administration, go to Devices > Phone , and then search for the user's Webex App for mobile (TCT or BOT) device.

Step 2

For Mobility User ID , choose the user's ID (typically
                                          the same as the Owner User ID .

Step 3

Choose the Associated mobile identity that you
                                          configured.

Step 4

For Transfer to Mobile Network , choose Use Mobility
                                             Softkey (user receives call)

When this setting is configured, Unified CM calls the phone number of the
                                             PSTN mobile service provider for the mobile device.

Step 5

Save your changes, then go to User Management > End User and locate any user accounts you want to add this feature
                                          to.

Step 6

Check the following settings:

- Enable Mobility

- Enable Mobile Voice Access

Step 7

Save your changes.

#### What to do next

Users can change the Destination in the Self Care Portal:

In the Webex App settings, go to Calling > Advanced Call Settings .

On the Self Care Portal page, select your mobile device.

Click Edit Single Number Reach , change the entry for Phone Number or URI , and then click Save .

### Multiline

#### Multi-line support for Webex App (Unified CM) on desktop

You can add up to 10 phone lines for each user. You can configure multiline for your users on the Cisco Services Framework
                                 (CSF) device for desktop clients.

Multiline on the desktop is supported on the Cisco Unified Communications Manager release 11.5 SU3 and later. However, if
                                 you are using Cisco Unified Communications Manager release 11.5 SU3 or release 12.0, you must manually install the Cisco Options Package (COP) file on all cluster nodes and restart Cisco Unified Communications Manager to enable multiline.

The maximum number of phone lines that can be assigned to a desktop Webex application has been increased from 8 to 10. To
                                             use this enhancement, download and install the cmterm-webex-desktop-10-Lines-241115.k4.cop.sha512 COP file from CCO . This feature is supported by Webex 44.12 and Unified CM 15 SU2.

#### Multi-line support for Webex App (Unified CM) on mobile

You can configure up to 8 lines for your users on the TCT, BOT, and TAB devices for mobile clients.

This capability enables users to manage multiple calls simultaneously, thus enhancing efficiency and productivity. It is supported
                                 by Webex 44.12 and Unified CM 15 SU2.

#### Additional Information

To configure multiline, use the steps in Add a directory number to the device to add multiple lines to a device and then associate the device to users.

Multiline is supported when using the Webex App for desktop in Mobile and Remote Access (MRA) mode. This function can be enabled on the Expressway-C in the traversal pair
                                             ( Unified Communication > Configuration > SIP Path headers and set to On ).

You can also configure the RemoteInUsePresencePrimaryLineOnly parameter to modify the presence for shared line scenarios. See Policy parameters for more information.

This parameter is not a selectable preset in Unified CM. You must add it as a customer parameter under policies.

After you have installed and configured Multiline, your users can:

Select a preferred line for making calls.

View missed calls and visual voicemails.

View Message Waiting Indicators per line (desktop only)

Use call forwarding, transfers, and conference calls on all lines.

Assign custom ringtones to each line.(desktop only)

Multiline supports the following features on all lines:

CTI control for the desk phone(desktop only)

Hunt groups

Shared line, dial rules, and directory lookup

Accessory manager

If Multiline is enabled, these features are only available on the primary line:

Call pickup

Extend & Connect (desktop only)

Dial Via Office Reverse (mobile only)

### Calling Dock

Calling Dock (formerly known as multi call window) is a separate, floating window that helps Webex App users to manage multiple
                              or shared lines. As well as making and receiving calls on multiple or shared lines, users can see the status of all lines,
                              and they also have better access to features like hold, transfer, and barge, without changing to another window.

Configure the following features on Unified CM to give users the maximum benefit from the multi call window:

Multiline

Voicemail

Barge

Privacy

Message waiting indicator (MWI)

Read these articles:

Configure multi call window for Calling in Webex App (Unified CM)

Webex App | Manage all your phone calls in one place

### Push Notifications

When your cluster is enabled for Push Notifications, Cisco Unified Communications
                                 Manager use either the Apple or Google cloud’s Push Notification service to send
                                 push notifications to compatible Webex clients that run on iOS (Apple Push
                                 Notifications or APNs) or Android (Firebase Cloud Messaging or FCM) devices. Push
                                 Notifications let your system communicate with the client, even after it has entered
                                 into background mode (also known as suspended mode). Without Push Notifications, the
                                 system may not be able to send calls to clients that have entered into background
                                 mode.

For more information about how to configure Apple and Android push notifications
                                 (APNs), see Push Notifications (On-Premises
                                    Deployments) in the Push Notifications Deployment Guide .

### Location reporting for emergency calling

To comply with Ray Baum's act, in the US, you can require users to give accurate
                                 location information when they are outside the office.​

If the Webex App determines users moved to a new location, they are prompted to update their address. When users make an emergency call from Webex App , accurate location information is automatically sent through a National E911 Service Provider to the public-safety answering
                                 point (PSAP), which is the local emergency call center that responds to emergency calls. This way, first responders have the
                                 necessary information needed to pinpoint the "dispatchable location" and quickly reach an emergency caller regardless of the
                                 device they dial from, or their exact location inside a large building.

This feature is limited to Windows, Mac, Linux, VDI, iPad, Android Tablet and
                                             Chromebook.

For mobile soft phone device with cellular, Webex App cross-launches the built-in phone app to make the emergency call.

Users on MacOS Monterey need to grant network permission to Webex App , so that Webex can report the BSSID to Redsky. If BSSID cannot be reported
                                             automatically, each user must manually add their locations in the Webex App .

If you're environment uses Unified CM 12.5 or earlier, you must upgrade to the
                                 supported server version:

Unified CM 12.5SU6

Cisco Emergency Responder 12.5SU6

Cisco Expressway X14.1

Unified CM 12.5SU5a

Cisco Emergency Responder 12.5SU5a

Cisco Expressway X14.0.4

RedSky-related configuration goes through the Unified CM service profile powered by
                                 the UDS interface.

<EnableEmergencyCalling> (Yes/No)

<OrganizationId>

<Secret>

<LocationUrl>

<EmergencyNumbers>

If you're using Unified CM 14 or later, your users must install the Redsky MyE911 app
                                 and report location from there. If you're using CER to report the on-premises
                                 wireless location, you can keep CER and use the RedSky solution to only track
                                 off-premises location.

Webex App for Linux doesn't support CER. You must deploy RedSky to report both
                                             on-premises and off-premises location for emergency calling.

For mobile soft phone devices (TCT/BOT), you must provision the emergency number
                                 (such as 911) in your Unified CM server, so that Webex App launches the built in phone app to make the emergency call. See "Create and
                                 Configure Webex Softphone Devices" in the deployment chapter.

#### Further documentation

Configuring Emergency Responder with a National E911 Service Provider

Cisco Emergency Responder integrates with National E911 Service Provider like RedSky or Intrado for automated Location update,
                                 MSAG (Master Street Address Guide) for a User input location and Call Completion. Emergency Responder automatically finds
                                 and tracks the dispatchable locations of all your devices as they move throughout the enterprise so you can comply with E911
                                 regulations.

https://www.cisco.com/c/dam/td-xml/en_us/voice-ip-comm/ucm_cloud/WebexCallingDI_Islands/National_E911_for_DedicatedInstance.pdf

Configuring Unified Communications Manager for Nomadic E911 Support

Nomadic E911 enables administrators to address the requirements of RAY BAUM’S Act by
                                 letting users update their location natively in Webex App.

https://www.cisco.com/c/dam/td-xml/en_us/voice-ip-comm/ucm_cloud/WebexCallingDI_Islands/National_E911_WebexApp_AdminGuide.pdf

### Survivable Remote Site Telephony (SRST)

Cisco Unified Survivable Remote Site Telephony (SRST) provides Unified CM with
                                 fallback support for Webex App users. Cisco Unified SRST enables routers to provide call-handling support for Webex App users when they lose connection to remote primary, secondary, or tertiary Cisco
                                 Unified CM installations or when the WAN connection is down.

For more information about this feature, see "Configure SRST" in the System Configuration Guide for your
                                 Unified CM release and see the Cisco Unified SCCP and SIP SRST System
                                    Administrator Guide (All Versions) for IOS configuration, feature
                                 support, and restrictions.

### Voicemail

For voicemail to work in Webex App , you must ensure that Cisco Unity Connection and
                                 Unified CM use a matching authentication method (for
                                 example, legacy SSO, oAuth SSO, or non-SSO). When
                                 integrated with Unified CM, Cisco Unity Connection
                                 (the voicemail and messaging system) provides
                                 voice-messaging features for users that you
                                 configure manually, through AXL services, or through
                                 LDAP integration. After receiving voice messages in
                                 their mailboxes, users receive message-waiting
                                 lights on their phones and integrated
                                 applications—in this case, Webex App .

For server performance considerations, don't use Visual Voicemail with both Jabber and Webex App at the same time.

Users get a visual voicemail inbox in Webex App . They can play messages, delete messages, mark as
                                 read, and respond with an audio or video call:

Users can also click Call Voicemail , which accesses the voicemail system with an internal or external call.
                                 Users can then retrieve, listen to, reply to, forward, and delete their messages. For more
                                 information about this feature for your users, see the Webex App Voicemail documentation.

Voicemail always uses Unified CM end user credentials. These credentials and the voicemail credentials on Unity Connection
                                             must be consistent—either set up both with single sign-on (SSO) or with non-SSO credentials, so that the sign in experience
                                             is the same. See Recommended configuration for more information.

For information about setting up Cisco Unity Connection and integrated it with your Unified CM environment, see the following
                                 documentation:

Cisco Unified Communications Manager SIP Integration Guide for Cisco Unity Connection for your release at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html

"Managing the Phone System Integrations in Cisco Unity Connection" in the System Administration Guide for Cisco Unity Connection for your release at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html .

### Wi-Fi to LTE Call Network Handoff

Wi-Fi to LTE Call Handoff provides flexibility for Calling in Webex App (Unified CM) users to switch between different networks (such as Wi-Fi and LTE) without
                                 disconnecting any active calls that the user may be while switching network.

This feature is automatically enabled for desktop and mobile users. Your calling
                                 environment must be on Unified CM 14 and later. See the Unified CM release notes for more
                                 information.

For known issues and limitations for this feature, see the known issues in the
                                 deployment chapter.

### Wireless Location Monitoring Service

Webex App supports wireless access point (AP) location monitoring. Wireless location
                                 monitoring service allows you to determine the physical location from where your Webex App users connect to the corporate network. This information is stored in
                                 Cisco Unified Communications Manager.

This feature is supported with on-premises and Mobile and Remote Access (MRA) Edge
                                 wireless connections.

Webex App monitors your users’ locations, gathers Service Set ID (SSID) and Basic Service
                                 Set ID (BSSID) information, and sends this information to Unified CM at least every
                                 24 hours (desktop only), or whenever:

Their current access point changes.

They sign in to Webex App .

They switch between networks for on-premises and Expressway for MRA.

Webex App resumes from sleep or is made active.

If Webex App for mobile gets suspended, it may not send the location every 24 hours.

For on-premises deployments , configure wireless location monitoring
                                       using EnableE911OnPremLocationPolicy parameter with the
                                       value true.

For Expressway for MRA deployments —you can configure wireless location
                                       monitoring using the EnableE911EdgeLocationPolicy with the
                                       value true and E911EdgeLocationWhiteList with a list of up
                                       to 30 SSIDs, separated by a semicolon.

For more details on these parameters, see the Appendix in this guide.

For more information about how to configure Cisco Emergency Responder (CER), see the Cisco Emergency Responder Administration Guide for your release at https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/products-maintenance-guides-list.html .

## Contact Center feature requirements

Webex App can integrate into your Cisco Contact Center solution (Unified Contact Center
                              Enterprise or Express) and be controlled in Finesse desktop as a softphone client.
                              This integration supports contact center features such as multiline, recording,
                              conferencing, and more.

To see the latest supported features in the Webex App , see Contact Center integration for Webex App .

For information about how to configure your Cisco Contact Center solution, see the
                              Feature Guide documentation for your specific product and release:

Cisco Unified Contact Center Enterprise
                                       (UCCE)

Cisco Unified Contact Center Express
                                       (UCCX)

## Network requirements

When using Calling in Webex App (Unified CM) over your corporate Wi-Fi network, we recommend that you do the following:

Design your Wi-Fi network to eliminate gaps in coverage as much as possible, including in areas such as elevators, stairways,
                                    and outside corridors.

Ensure that all access points assign the same IP address to the mobile device. Calls are dropped if the IP address changes
                                    during the call.

Ensure that all access points have the same service set identifier (SSID). Hand-off may be much slower if the SSIDs do not
                                    match.

Ensure that all access points broadcast their SSID. If the access points do not broadcast their SSID, the mobile device may
                                    prompt the user to join another Wi-Fi network, which interrupts the call.

Ensure that the Enterprise firewall is configured to allow the passage of Session Traversal Utilities for NAT (STUN) packets.

Conduct a thorough site survey to minimize network problems that could affect voice quality. We recommend that you do the
                              following:

Verify nonoverlapping channel configurations, access point coverage, and required data and traffic rates.

Eliminate rogue access points.

Identify and mitigate the impact of potential interference sources.

For more information, see the following documentation:

The "VoWLAN Design Recommendations" section in the Enterprise Mobility Design Guide .

The Cisco Unified Wireless IP Phone 7925G Deployment Guide .

The Capacity Coverage & Deployment Considerations for IEEE 802.11g white paper.

The Solutions Reference Network Design (SRND) for your Cisco Unified
                                       				  Communications Manager release.

### Ports and protocols

Calling in Webex App (Unified CM) uses the ports and protocols listed in the following table. If you plan to deploy a firewall between the client and a server,
                                 configure the firewall to allow these ports and protocols.

Port

Application layer protocol

Transport layer protocol

Description

Configuration

6970

HTTP

TCP

Connect to the TFTP server to download client configuration files.

6972

HTTPS

TCP

Connects to the TFTP server to download client configuration files securely for Cisco Unified Communications Manager.

8443

HTTPS

TCP

Traffic to Cisco Unified Communications Manager.

Communication Manager
                                                signaling

2748

CTI

TCP

Computer Telephony Interface (CTI) used for desk phone control.

5060

SIP

TCP

Provides Session Initiation Protocol (SIP) call signaling.

5061

SIP over TLS

TCP

SIP over TLS provides secure SIP call signaling. (Used if Secure SIP is enabled for device.)

5070 to 6070

BFCP

UDP

Binary Floor Control Protocol (BFCP) for video screen sharing capabilities.

Voice or video media
                                                exchange

16384 to 32766

RTP/SRTP

UDP

Cisco Unified Communications Manager media port range used for audio, video, and BFCP video desktop share.

33434 to 33598

RTP/SRTP

UDP

Cisco Webex Hybrid Services media port range used for audio and video.

8000

RTP/SRTP

TCP

Allows users to receive video transmitted to their desk phone devices on their computers through the client.

### Supported codecs

Type

Codec

Codec type

Webex App for Android

Webex App for iPhone and iPad

Webex App for Mac

Webex App for Windows

Audio

G.711

A-law

Yes

Yes

Yes

µ-law/Mu-law

Yes

Yes

Yes

G.722

Yes

Yes

Yes

G.722.1

24 kb/s and 32 kb/s

Yes

Yes

Yes

G.729

No

No

No

G.729a

Yes

Yes

Yes

Opus

Yes

Yes

Yes

Video

H.264/AVC

Baseline profile

Yes

Yes

Yes

High profile

No

Yes

Yes

## Certificate requirements

### Unified CM certificates (no MRA in deployment)

To establish a secure connection with Unified CM, Webex App validates the certificate that is presented by the server during
                                 the connection process. Unlike Jabber, Webex App does not prompt users with the option to accept an untrusted
                                 certificate.

Unified CM must be configured with certificates that Webex App can validate, preferably a CA root that signed the tomcat
                                 certificate (which is known to the operating system that Webex App is on, Windows or MacOS by default). or a self-signed trusted
                                 certificate (which must be deployed to the OS in advance by the
                                 enterprise administrator).

The Tomcat certificate is also used for secure SIP when Webex App is enabled for encrypted calls (SIP Oauth operates on the
                                             default port 5090). See "Configure the Phone Security
                                                Profile for Encrypted Calls" in this guide for
                                             more details.

Certificates issued with a deprecated signature algorithm (such as SHA-1) do not work; you must use a supported secure signature
                                 algorithm such as SHA-256 or later, as documented in the Certificates chapter in the Administration Guide for Cisco Unified Communications Manager .

The certificates that are deployed on Unified CM servers must include the fully qualified domain name (FQDN) as the server
                                             identity rather than a simple hostname or IP address (for example, cucm-server-1.example.com rather than cucm-server-1 or 203.0.113.1).

In Cisco Unified CM Administration > System > Server , the Unified CM server names must be defined as FQDN.

See High Level View of Certificates and Authorities in CUCM and CUCM Certificate Management and Change Notification for information about certificate management in Unified CM.

### Unified CM certificates (with MRA in deployment)

The Unified CM Tomcat certificate is significant for Mobile and Remote
                                 Access (MRA). This certificate is automatically installed on the
                                 Cisco Unified Communications Manager. By default, it is self-signed
                                 and has the same common name (CN).

The Tomcat certificate is also used for secure SIP when Webex App is enabled for encrypted calls (SIP Outh operates on the
                                             default port 5091 for MRA). See "Configure the Phone
                                                Security Profile for Encrypted Calls" in this
                                             guide for more details.

We recommend using CA-signed certificates. However, if you do use self-signed certificates, the two certificates must have
                                 different common names. The Expressway does not allow two self-signed certificates with the same CN. So if the CallManager
                                 and tomcat self-signed certificates have the same CN in the Expressway's trusted CA list, the Expressway can only trust one
                                 of them. This means that either secure HTTP or secure SIP, between Expressway-C and Cisco Unified Communications Manager,
                                 will fail.

### Expressway certificates (with MRA in deployment)

For MRA scenarios, certificates only need to be validated on the Expressway.

The Expressway certificate signing request (CSR) tool prompts for and incorporates the relevant Subject Alternative Name (SAN)
                                 entries as appropriate for the Unified Communications features that are supported on that Expressway.

The following table shows which CSR alternative name elements apply to which Unified Communications features.

Add these items as Subject
                                             Alternative Names (SANs)

When generating a CSR for MRA

Unified CM registrations domains (despite their name, these have more in common with service discovery domains than with Unified CM Unified CM SIP registration domains)

Required on Expressway-E only

(Clustered systems only) Expressway cluster name

Required on Expressway-C only

You must restart the Expressway for any new uploaded server certificate to take effect.

#### Expressway-E server certificate requirements

The Expressway-E server certificate needs to include the following element in its list of subject alternative names (SAN):

Unified CM registrations domains : all of the domains which are configured on the Expressway-C for Unified CM registrations. Required for secure communications between endpoint devices and Expressway-E.

The Unified CM registration domains used in the Expressway configuration and Expressway-E certificate, are used by Mobile and Remote Access
                                       clients to lookup the _collab-edge DNS SRV record during service discovery. They enable MRA registrations on Unified CM , and are primarily for service discovery.

These service discovery domains may or may not match the SIP registration domains. It depends on the deployment, and they
                                       don't have to match. One example is a deployment that uses a .local or similar private domain with Unified CM on the internal network, and public domain names for the Expressway-E FQDN and service discovery. In this case, you need
                                       to include the public domain names in the Expressway-E certificate as SANs. There is no need to include the private domain
                                       names used on Unified CM . You only need to list the edge domain as a SAN.

Select the DNS format and manually specify the required FQDNs. Separate the FQDNs by commas if you need multiple domains.
                                       You may select CollabEdgeDNS format instead, which simply adds the prefix collab-edge to the domain that you enter. This format is recommended if you
                                       do not want to include your top level domain as a SAN (see example in following screenshot).

#### Requirements when migrating from Jabber to Webex App

In migration scenarios, you may encounter an issue if you're using a
                                 private CA with the Certificate Revocation List (CRL) default format
                                 ( ldap :/// ) for the Expressway-E
                                 certificate.

In that deployment, after migrating from Jabber to the Webex App , Webex App on iOS devices does not register to Unified CM phone services.
                                 The registration fails because the iOS client tries to reach the CRL
                                 URL from the Internet, but the CRL format ldap:/// is not supported by iOS
                                 clients.

Tip

If you're using a private CA for issuing certificates for
                                             Expressway-E, we recommend that the Expressway-E is issued
                                             by a public CA, and then you can migrate users from Jabber
                                             to the Webex App .

If you must use certificates signed by a private CA for your Expressway-E
                                 setup (in particular, a CRL with the format ldap:/// ), follow these steps to ensure
                                 a successful migration from Jabber to the Webex App :

Remove the CRL parameter, if any, from the private CA
                                       template.

Reissue Expressway-E server certificates without the CRL
                                       parameter.

Make sure certificates that the private CA signs support
                                       the following requirements for iOS:

Minimum key size of 2048

SHA-2 signature

Server DNS name as SAN

Extended key usage extension containing the
                                             id-kp-serverAuth OID

Validity period of 398 or fewer days

Install the root CA file on mobile devices

For Apple iOS devices, you must also enable full trust
                                                      for root certificates .

## Headset requirements

Unified CM calling in Webex App supports the following Cisco series headsets. Click the links for
                              more information on each model:

Some Jabra headsets are supported. See Details about headset support for more
                              information.

When using a supported headset in Webex App , the headset firmware can get updated automatically. Users get a message that pops up letting them know that an update is
                                          available, and then they'll get confirmation after it's updated.

## License requirements

You require a Cisco Webex organization (managed in Control Hub ) with a paid subscription. User accounts must be managed in your organization but they don't require a specific license assignment
                              to use Calling in Webex App (Unified CM) .

Additionally, for softphone functionality, each Webex App registers to Unified CM as a softphone client. Like Cisco Jabber, this registration uses
                              the Cisco Unified Client Services Framework (CSF) client for desktop and a BOT, TCT, or TAB
                              device for mobile, and counts as a device toward Unified CM licensing. Users with three or
                              more apps and/or devices require CUWL perpetual licensing or for the organization to be on a
                              Flex Calling subscription.

Tip

We recommend Flex Calling as the subscription channel for Calling in Webex App (Unified CM) .

## Webex App requirements

To ensure that Calling in Webex App (Unified CM) functions correctly and the latest features, functionality, and
                              other fixes are continuously delivered, users must be on the latest
                              release of the Webex App for desktop or mobile , or the latest VDI thin client .

The Web app (web.webex.com) does not allow users to call phone
                                          numbers.

For installation and upgrade instructions, see Installation and automatic
                                       upgrade .

For managing the frequency of Webex App updates for users in your organization, see Product update
                                       controls for Webex App .

Chromebooks on both ARM and x86 architecture are
                                    supported for Calling in Webex App (Unified CM) . Users can also be signed into phone service on
                                    both a Chromebook and Android phone at the same
                                    time.

For VDI deployment steps, see the Deployment guide for Virtual
                                       Desktop Infrastructure (VDI) .

For release information, see the Release notes and What's new documentation
                                    for the Webex App and the VDI release
                                       notes for Webex App for VDI.

## Recommended configuration

### Single sign-on (SSO) and IdP integration

For Calling in Webex App (Unified CM) , SSO is supported with Unified CM and Expressway. You must either enable
                                       or disable SSO on both. For a consistent user experience with SSO, we
                                       recommend that you extend your Identity Provider (IdP) integration to Webex App so that users can sign in with the same credentials. With Single Sign-On
                                       (SSO) integration between your IdP, your premises environment, and the Webex
                                       cloud, users can sign in across applications with one set of credentials.

For premises Unified CM configuration, see the SAML SSO Deployment Guide for Cisco Unified
                                          Communications Applications for your release. We recommend
                                       applying this configuration to Unified CM and any Unity Connection voicemail
                                       servers in your deployment.

For Expressway configuration, see the Mobile and Remote Access via Cisco Expressway
                                          Deployment Guide for your release.

For cloud ( Webex App ) configuration, see Single
                                          Sign-On Integration with Webex Control Hub

See the following table for supported authentication types:

Type

Windows

Mac

iOS

Android

✓

✓

✓

See the SSO Redirect URI requirements

✓

✓

✓

✓

✓

✓

✓

✓

✓

See the SSO Redirect URI requirements

✓

### SSO redirect URI

The Webex App supports SSO redirect URI, an enhancement to the app's embedded browser
                                 support.

This feature provides the following enhancements:

Provides protection against "Authorization Code Interception Attack" using RFC7636 .

Allows Webex App running on an Operating Systems other than iOS to use the Embedded
                                       Browser (For example: Android).

Allows Webex App to use the Embedded browser for Unified Communications Manager (and MRA)
                                       OAuth flow. This support prevents dual login when SSO is enabled.

#### Requirements

This feature requires the following minimum versions:

Unified CM 12.5(x) releases-12.5(1) SU4 and Unified CM 14.0(x) releases-14.0(1) SU1 and later

Expressway X14 and later

Webex App 41.4 and later

For more information, see the following documentation:

Expressway Release Notes

Unified CM Release Notes

#### Configuration

For Unified CM—No configuration is required.

For Expressway—On the Expressway-C, you must set the parameter Webex
                                    Client Embedded Browser Support to Yes to
                                 enable this feature. For more information, see Configure MRA Access Control in the Mobile and Remote Access Through Cisco Expressway Deployment Guide (X14.0)
                                    .

### Directory synchronization and contact cards

We recommend using the Cisco Directory Connector for user synchronization from your Active Directory into Control Hub .

You can also synchronize user phone numbers. Their numbers appear in contact cards in
                                 the Webex App for Windows and Mac:

For iOS and Android, users can access someone's contact card from a space by just
                                             tapping a profile picture. See Verify Who You're Contacting for more
                                             information.

For the numbers to appear, you must deploy Cisco Directory Connector to synchronize the numbers from an existing Active Directory attribute into the
                                 cloud. See the attribute mapping information in the Deployment Guide for Cisco
                                    Directory Connector at https://www.cisco.com/go/hybrid-services-directory .

### Overview of Auto-Provisioning of Webex App

The auto-provisioning feature in Control Hub allows the users to self-provision the devices for Calling in Webex (Unified
                              CM) with zero or minimal intervention. This feature avoids over-provisioning of multiple devices in Unified CM that helps
                              to minimize the impact on cluster scaling and licensing usage. Devices are auto created in Unified CM, when a user provisioned
                              for Calling in Webex (Unified CM) signs in with their registered email address or User ID to Webex App.

Administrators don't need to go to Unified CM to pre-provision any of the Webex App devices for users in their organization.
                              When the user signs in to the Webex App with any device for the first time, and if the device isn’t already available in the
                              Unified CM server, the new device type is auto created for the user.

This feature allows auto-provisioning of following devices types in Unified CM for the users when they sign into Webex App
                              from various device platforms:

Android Device (BOT)

Chromebook/iPad Devices (TAB)

Windows/MAC Devices (CSF)

iPhone Device (TCT)

#### Prerequisite

Before you plan to allow auto-provision of Webex App for the users, make sure that you meet the following requirements:

Activate Cloud-Connected UC and set up the on-premises devices in your organization to communicate with the Control Hub. For
                                       more information, see Set Up Cloud-Connected UC for On-Premises Devices .

For the user account in Control Hub, add either a Basic or Professional Webex Calling license.

Cisco Unified Communications Manager clusters should be version 11.5 or above. See the supported Unified CM version for Calling
                                       in Webex (Unified CM) at Deployment Guide for Calling in Webex (Unified CM) .

The minimum supported Webex App version is 41.12 and higher.

The minimum supported Cisco Expressway Release version is X14.0.2. If the Expressway version is below the recommended version,
                                       Expressway should add the following URLs manually to the Allow List to allow external clients (Cisco Jabber or Webex App)
                                       to access the Unified Communications nodes discovered having MRA configuration:

POST : https://{{cucmip}}:8443/devicemanagement/v1/clientAutoProv/createDevice

GET : https://{{cucmip}}:8443/ucmservices/v1/supportedServices

Ensure that the User ID or email ID of Unified CM users matches with the User ID of the user records entity in Webex Identity
                                       Service. Also, the users configured in the Unified CM server should be available in the organizations’ Webex Identity Service.

### Additional configuration

We recommend the following additional configuration to provide further benefits for
                                 your Calling in Webex App (Unified CM) deployment:

Quality of Service (QoS), covered in the Appendix in this guide. QoS helps manage packet
                                       loss, delay and jitter on your network infrastructure.

Call Admission Control (CAC) on Unified CM, covered in the System Configuration Guide for Cisco Unified
                                          Communications Manager . CAC enables you to control the audio
                                       quality and video quality of calls over a wide-area (IP WAN) link by
                                       limiting the number of calls that are allowed on that link at the same time.

| Call solution | Version |
|---|---|
| Cisco Unified Communications
                                       Manager* | Minimum |
| Desktop and mobile (Android) Unified CM Release 11.5(1) SU3 and later for
                                                      desktop. While not mandatory, this minimum also release
                                                      supports Firebase Cloud Messaging (FCM) push
                                                      notifications on Android. Desktop and mobile (iOS) For an 11.5 release, Unified CM Release 11.5(1)
                                                      SU8 or a later SU is required minimum for Apple
                                                      Push Notification (APN) service on iOS mobile
                                                      devices. (This release is not supported in China.
                                                      See below.) For a 12.5 release, Unified CM Release 12.5(1)
                                                      SU3 or a later SU is required for iOS APN
                                                      support. Secure calls (SIP Oauth) Unified CM Release 12.5(1) and later Note CAPF is not supported. | Note | CAPF is not supported. |
| Note | CAPF is not supported. |
| Recommended |
| Desktop and mobile Unified CM Release 12.5(1) SU3 or later.** This
                                                      recommended release ensures that push
                                                      notifications work for all mobile platforms in
                                                      your environment and that secure calling is
                                                      supported. See Push Notifications for
                                                      more information. Note If your organization is based in China, you
                                                                  must use this version at a minimum. If you use Mobile Remote Access (MRA) and want
                                                      to configure MRA failover, Unified CM Release 14.0
                                                      or later is required. SSO Redirect URI This enhancement has specific Unified CM and
                                             Expressway requirements. See the SSO Redirect URI
                                             section in Recommended Configuration for more
                                             information. | Note | If your organization is based in China, you
                                                                  must use this version at a minimum. |
| Note | If your organization is based in China, you
                                                                  must use this version at a minimum. |
| Cisco Business Edition | Check the software load summary documentation
                                          for BE6K and BE7K to ensure the
                                          solution is running a supported version of Unified
                                          CM. |
| Cisco Hosted Collaboration Solution | 11.5 and later at a minimum. 12.5 and later is recommended for SIP Oath
                                          encrypted calls support. (CAPF is not
                                          supported.) |
| Cisco Unified Communications Manager Cloud | — |

| Note | CAPF is not supported. |
|---|---|

| Note | If your organization is based in China, you
                                                                  must use this version at a minimum. |
|---|---|

| Call solution | Version |
|---|---|
| Cisco Expressway E and C traversal pair for Mobile and Remote Access (MRA) | X8.11.4 or later is required for
                                          Calling in Webex App (Unified CM). See the "Important Information"
                                          section in the Expressway Release Notes for more information. This release and later
                                          provide added security. X12.6 or later for Push Notifications. If you use Mobile Remote Access (MRA) and want
                                          to configure MRA failover, Expressway Release
                                          X14.0 or later is required. See the Mobile and Remote Access via Expressway Deployment Guide for more information. |

| Note | Mobile users having Mobile Identity (MI) configured cannot place or receive calls. Install the ciscocm.V15SU2_CSCwm77174-multiline_v1.zip file from CCO to use this feature. This feature is supported from Webex 44.12 and Unified CM 15 SU2. |
|---|---|

| Note | The users do not receive incoming calls on Webex App in the following situations: If users select the Mobile Voice Network calling option on any network and the Single Number Reach (SNR) is not configured for their device, they will not receive
                                                   incoming calls on Webex App . If users select the Mobile Voice Network calling option on any network and the Single Number Reach (SNR) is configured with the Ring Schedule , they will not receive incoming calls on Webex App beyond the time set in the Ring Schedule . |
|---|---|

| Connection | Calling Options |
|---|---|
| Voice over IP | Mobile Voice Network | Autoselect |
| Wi-Fi | Outgoing: VoIP | Incoming: VoIP | Outgoing: DvO-R | Incoming: VoIP | Outgoing: VoIP | Incoming: VoIP |
| Mobile Network (3G, 4G, 5G) | Outgoing: DvO-R | Incoming: VoIP |

| Note | Users can only add and edit numbers for existing devices. You
                                             must configure at least one device for users. If no device
                                             exists, then even if this feature is enabled, users won't
                                             see it as an option in Webex App . |
|---|---|

| Note | Mobile users having Mobile Identity (MI) configured cannot place or receive calls. Install the ciscocm.V15SU2_CSCwm77174-multiline_v1.zip file from CCO to use this feature. This feature is supported from Webex 44.12 and Unified CM 15 SU2. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, go to Devices > Phone , and then search for the user's Webex App for mobile (TCT or BOT) device. |
|---|---|
| Step 2 | For Mobility User ID , choose the user's ID (typically
                                          the same as the Owner User ID . |
| Step 3 | Choose the Associated mobile identity that you
                                          configured. |
| Step 4 | For Transfer to Mobile Network , choose Use Mobility
                                             Softkey (user receives call) When this setting is configured, Unified CM calls the phone number of the
                                             PSTN mobile service provider for the mobile device. |
| Step 5 | Save your changes, then go to User Management > End User and locate any user accounts you want to add this feature
                                          to. |
| Step 6 | Check the following settings: Enable Mobility Enable Mobile Voice Access |
| Step 7 | Save your changes. |

| Note | The maximum number of phone lines that can be assigned to a desktop Webex application has been increased from 8 to 10. To
                                             use this enhancement, download and install the cmterm-webex-desktop-10-Lines-241115.k4.cop.sha512 COP file from CCO . This feature is supported by Webex 44.12 and Unified CM 15 SU2. |
|---|---|

| Note | Multiline is supported when using the Webex App for desktop in Mobile and Remote Access (MRA) mode. This function can be enabled on the Expressway-C in the traversal pair
                                             ( Unified Communication > Configuration > SIP Path headers and set to On ). |
|---|---|

| Note | This parameter is not a selectable preset in Unified CM. You must add it as a customer parameter under policies. |
|---|---|

| Note | This feature is limited to Windows, Mac, Linux, VDI, iPad, Android Tablet and
                                             Chromebook. For mobile soft phone device with cellular, Webex App cross-launches the built-in phone app to make the emergency call. Users on MacOS Monterey need to grant network permission to Webex App , so that Webex can report the BSSID to Redsky. If BSSID cannot be reported
                                             automatically, each user must manually add their locations in the Webex App . |
|---|---|

| Customer type | Required components and supported versions |
|---|---|
| Unified CM on-premises | Unified CM 12.5SU6 Cisco Emergency Responder 12.5SU6 Cisco Expressway X14.1 |
| Unified CM Cloud | Unified CM 12.5SU5a Cisco Emergency Responder 12.5SU5a Cisco Expressway X14.0.4 |

| Note | Webex App for Linux doesn't support CER. You must deploy RedSky to report both
                                             on-premises and off-premises location for emergency calling. |
|---|---|

| Note | For server performance considerations, don't use Visual Voicemail with both Jabber and Webex App at the same time. |
|---|---|

| Note | Voicemail always uses Unified CM end user credentials. These credentials and the voicemail credentials on Unity Connection
                                             must be consistent—either set up both with single sign-on (SSO) or with non-SSO credentials, so that the sign in experience
                                             is the same. See Recommended configuration for more information. |
|---|---|

| Note | If Webex App for mobile gets suspended, it may not send the location every 24 hours. |
|---|---|

| Port | Application layer protocol | Transport layer protocol | Description |
|---|---|---|---|
| Configuration |
| 6970 | HTTP | TCP | Connect to the TFTP server to download client configuration files. |
| 6972 | HTTPS | TCP | Connects to the TFTP server to download client configuration files securely for Cisco Unified Communications Manager. |
| 8443 | HTTPS | TCP | Traffic to Cisco Unified Communications Manager. |
| Communication Manager
                                                signaling |
| 2748 | CTI | TCP | Computer Telephony Interface (CTI) used for desk phone control. |
| 5060 | SIP | TCP | Provides Session Initiation Protocol (SIP) call signaling. |
| 5061 | SIP over TLS | TCP | SIP over TLS provides secure SIP call signaling. (Used if Secure SIP is enabled for device.) |
| 5070 to 6070 | BFCP | UDP | Binary Floor Control Protocol (BFCP) for video screen sharing capabilities. |
| Voice or video media
                                                exchange |
| 16384 to 32766 | RTP/SRTP | UDP | Cisco Unified Communications Manager media port range used for audio, video, and BFCP video desktop share. |
| 33434 to 33598 | RTP/SRTP | UDP | Cisco Webex Hybrid Services media port range used for audio and video. |
| 8000 | RTP/SRTP | TCP | Allows users to receive video transmitted to their desk phone devices on their computers through the client. |

| Type | Codec | Codec type | Webex App for Android | Webex App for iPhone and iPad | Webex App for Mac | Webex App for Windows |
|---|---|---|---|---|---|---|
| Audio | G.711 | A-law | Yes | Yes | Yes |
| µ-law/Mu-law | Yes | Yes | Yes |
| G.722 |  | Yes | Yes | Yes |
| G.722.1 | 24 kb/s and 32 kb/s | Yes | Yes | Yes |
| G.729 |  | No | No | No |
| G.729a |  | Yes | Yes | Yes |
| Opus |  | Yes | Yes | Yes |
| Video | H.264/AVC | Baseline profile | Yes | Yes | Yes |
| High profile | No | Yes | Yes |

|  |  |
|---|---|

| Note | The Tomcat certificate is also used for secure SIP when Webex App is enabled for encrypted calls (SIP Oauth operates on the
                                             default port 5090). See "Configure the Phone Security
                                                Profile for Encrypted Calls" in this guide for
                                             more details. |
|---|---|

| Note | The certificates that are deployed on Unified CM servers must include the fully qualified domain name (FQDN) as the server
                                             identity rather than a simple hostname or IP address (for example, cucm-server-1.example.com rather than cucm-server-1 or 203.0.113.1). |
|---|---|

| Note | The Tomcat certificate is also used for secure SIP when Webex App is enabled for encrypted calls (SIP Outh operates on the
                                             default port 5091 for MRA). See "Configure the Phone
                                                Security Profile for Encrypted Calls" in this
                                             guide for more details. |
|---|---|

| Note | For MRA scenarios, certificates only need to be validated on the Expressway. |
|---|---|

| Add these items as Subject
                                             Alternative Names (SANs) | When generating a CSR for MRA |
|---|---|
| Unified CM registrations domains (despite their name, these have more in common with service discovery domains than with Unified CM Unified CM SIP registration domains) | Required on Expressway-E only |
| (Clustered systems only) Expressway cluster name | Required on Expressway-C only |

| Note | You must restart the Expressway for any new uploaded server certificate to take effect. |
|---|---|

| Tip | If you're using a private CA for issuing certificates for
                                             Expressway-E, we recommend that the Expressway-E is issued
                                             by a public CA, and then you can migrate users from Jabber
                                             to the Webex App . |
|---|---|

| Note | For Apple iOS devices, you must also enable full trust
                                                      for root certificates . |
|---|---|

| Note | When using a supported headset in Webex App , the headset firmware can get updated automatically. Users get a message that pops up letting them know that an update is
                                          available, and then they'll get confirmation after it's updated. |
|---|---|

| Tip | We recommend Flex Calling as the subscription channel for Calling in Webex App (Unified CM) . |
|---|---|

| Note | The Web app (web.webex.com) does not allow users to call phone
                                          numbers. |
|---|---|

| Type | Windows | Mac | iOS | Android |
|---|---|---|---|---|
| IWA Auth with NTLM | ✓ | ✓ | ✓ See the SSO Redirect URI requirements | ✓ |
| IWA Auth with Kerberos | ✓ |  |  |  |
| Form-based Auth | ✓ | ✓ | ✓ | ✓ |
| Cert-based Auth | ✓ | ✓ | ✓ See the SSO Redirect URI requirements | ✓ |

| Note | For iOS and Android, users can access someone's contact card from a space by just
                                             tapping a profile picture. See Verify Who You're Contacting for more
                                             information. |
|---|---|

| Note | After the deletion of a device, it is recommended that you wait for 5-10 minutes before you auto-provision a device of the
                                       same type. Also, you can reset the device from Webex App before you auto-provision it again (Go to Help > Health Checker and click the Reset button.) |
|---|---|