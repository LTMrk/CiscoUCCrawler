---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-dell-wyse-jvdi-b-release-notes-jvdi-dell-wyse-thin-os-html-e4cf64790f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/dell-wyse/jvdi_b_release-notes-jvdi-dell-wyse-thin-os.html
retrieved_at: 2026-08-22T00:41:45.771134+00:00
---

Release Notes for Cisco Jabber Softphone for VDI—Dell Wyse ThinOS

# Release Notes for Cisco Jabber Softphone for VDI—Dell Wyse ThinOS

### Download Options

Updated: April 16, 2020

First Published: March 10, 2020

Last Updated: October 12, 2022

# Important Change to Release Notes Process

We no longer update these Release Notes.

For information on new Jabber features, see the Jabber Release Notes .

For information on unsupported Jabber features, see the Help Center article, Jabber | Jabber Softphone for VDI Feature
                  Support .

For release notes on using the Jabber VDI, see "Dell Wyse ThinOS Version 8.6 and ThinOS
               Lite 2.6 Operating System Release Notes" at https://www.dell.com/support/manuals/en-us/wyse-5040/thinos_8.6.x_rn/cisco-jabber-softphone-for-vdi?guid=guid-e911198a-cec6-4819-b021-d61e1c47db1e .

## Build Numbers

Dell Wyse ThinOS Version

Cisco JVDI Version

Cisco Jabber Softphone Build Number

ThinOS 9.0.3030

Cisco JVDI Agent 12.9

Cisco JVDI Client 12.9

12.09.1142

ThinOS 9.0.1136

Cisco JVDI Agent 12.8

Cisco JVDI Client 12.8

12.08.1089

ThinOS 8.6_206

ThinOS Lite 2.6_206

Cisco JVDI Agent 12.6

Cisco JVDI Client 12.6

12.6.19091611

ThinOS 8.6_013

Cisco JVDI Agent 12.1

Cisco JVDI Client 12.1

12.1.0.266460

Cisco Jabber Softphone for VDI is bundled with the Dell Wyse ThinOS and Dell Wyse owns support. Documentation is available from Dell Wyse.

### Cisco Jabber Softphone for VDI Copyright

Copyright © 2018–2020 Cisco or its affiliated entities. All Rights Reserved.

## What's New

### Cisco Jabber Softphone for VDI 12.9

#### Cisco Jabber Support

This release adds support for Cisco Jabber for Windows Release 12.9.

This release supports the following new Cisco Jabber for Windows Release 12.9
                        features:

Block Earlier Versions of the Clients From Signing In

Cisco Headset Firmware Upgrade Notification

Cisco Sunkist 730 Headset Presence LED Syncs with Jabber

Custom Tab Refresh After Network Issue

Link to Jabber Help Center Added

Join up to 15 Minutes Before the Meeting Starts

Programmatically Adjust Custom Tabs to Match Client Theme

Remote Collection of PRT Logs

Remove Third Party in Unified CM Conference

Search Persistent Chat Rooms by Room Name

Users Forced to Sign In Again On Upgrade to TMM

XMPP Federated Contacts for Team Messaging Mode

With N-1 or N-2 support, the lower version determines the available feature
                                    set.

### Cisco Jabber Softphone for VDI 12.8

#### Cisco Headset Support for 64–bit

We enhanced call control support for Cisco headsets, with 64–bit versions of Microsoft Windows.

#### Cisco Jabber Support

This release adds support for Cisco Jabber for Windows Release 12.8.

This release supports the following new Cisco Jabber for Windows Release 12.8 features:

Audio Device Priority

Call Park

Cisco Headset Support

Global Shortcut Key for Conversation Window

Microsoft Office 2019 Support

Multiline Per Line Ringtones

With N-1 or N-2 support, the lower version determines the available feature set.

#### Deprecated Parameter

We added the HeadsetPreference parameter to specify how Cisco Jabber handles new audio devices.

The new parameter replaces the now deprecated HeadsetPreferenceOnVDI parameter.

By default, when you connect a new audio device, Cisco Jabber adds it to the top of the priority list. The default behavior is a problem in some hot-desking environments. When a user
                        moves their thin client and headset, the embedded microphone becomes the preferred device.

Modern meeting rooms are often equipped with a large wall mounted monitor with HDMI, which handles both audio and video. When
                        a Cisco Jabber user connects to a monitor using HDMI, by default the monitor becomes the preferred device.

You can set this parameter to ensure that the user's headset remains the preferred device. Users can override this setting
                        in their Audio preferences. For more information about the new parameter, see Parameters Reference Guide for Cisco Jabber Release 12.8 .

#### Mute Notification Sounds During Calls or Meetings

Users in VDI deployments can now choose to mute notification sounds during their calls or meetings.

#### Presence Improvement

We improved how Cisco Jabber Softphone for VDI passes presence (status) information to the hosted virtual desktop. Now when
                        a user locks their thin client, their presence updates to Away . If their connection drops, their presence updates to Offline .

We also added a new parameter that controls how Cisco Jabber for Windows handles presence status when users disconnect from their HVDs.

True—When a user signs out or otherwise disconnects from their HVD, Cisco Jabber automatically signs out and presence status updates to Offline , within 10 seconds.

False (default)—When a user signs out, or otherwise disconnects from their HVD, Cisco Jabber remains signed in, and their presence status shows as Available .

For more information about the new parameter, see the Parameters Reference Guide for Cisco Jabber 12.8 .

#### Version Support Strategy

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the JVDI Client version can be the
                        same, or up to two releases earlier (N-2 support). For example, the following version combinations are supported:

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and Cisco JVDI Client Release 12.8

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and Cisco JVDI Client Release 12.7

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and Cisco JVDI Client Release 12.6

#### VDI Fallback Mode

Sometimes the Cisco JVDI Agent and the Cisco JVDI Client can't communicate. This issue occurs because of a network problem with the virtual channel, or because of a problem with
                        the Cisco Jabber Softphone for VDI installation. If the JVDI Agent and the JVDI Client can't communicate, Cisco Jabber can't operate in VDI-optimized mode. For more information about troubleshooting, see Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.8 .

This release introduces VDI Fallback mode, and a new parameter to enable this mode. Cisco Jabber Softphone for VDI checks the virtual channel every 10 seconds, to ensure that the JVDI Agent and the JVDI Client can communicate. If communication
                        is down, for two consecutive checks, Cisco Jabber Softphone for VDI switches Cisco Jabber to VDI Fallback mode. For more information about the new EnableVDIFallback parameter, see Parameters Reference Guide for Cisco Jabber Release 12.8 .

In VDI Fallback mode, users can make and receive calls, with audio traveling over the ICA channel. The connection status for Cisco Jabber changes from Softphone with VDI , to Softphone . Users can receive video; the ability to send video depends on the capabilities of your Citrix version. Audio and video quality
                        depend on network conditions, and the capabilities of your Citrix version. When Cisco Jabber operates in VDI Fallback mode, users see a notification message at the start of each call.

When Cisco Jabber Softphone for VDI detects communication between the JVDI Agent and the JVDI Client, it automatically switches Cisco Jabber back to VDI-optimized mode.

Cisco Jabber Softphone for VDI switches modes only between calls.

### Cisco Jabber Softphone for VDI 12.6

We enhanced call control support for
                        Cisco headsets, with 64–bit versions of Microsoft Windows.

This release adds support for Cisco Jabber for Windows Release
                        12.8.

This release supports the following new Cisco Jabber for Windows Release
                        12.8 features:

Audio Device Priority

Call Park

Cisco Headset Support

Global Shortcut Key for Conversation Window

Microsoft Office 2019 Support

Multiline Per Line Ringtones

With N-1 or N-2 support, the lower version determines the available feature
                                    set.

We added the HeadsetPreference parameter to
                        specify how Cisco Jabber handles new audio devices.

The new parameter replaces the now deprecated HeadsetPreferenceOnVDI parameter.

By default, when you connect a new audio device, Cisco Jabber adds it to the
                        top of the priority list. The default behavior is a problem in some hot-desking
                        environments. When a user moves their thin client and headset, the embedded
                        microphone becomes the preferred device.

Modern meeting rooms are often
                        equipped with a large wall mounted monitor with HDMI, which handles both audio and
                        video. When a Cisco Jabber user connects to a monitor using HDMI, by default the
                        monitor becomes the preferred device.

You can set this parameter to ensure
                        that the user's headset remains the preferred device. Users can override this
                        setting in their Audio preferences. For more information about the new
                        parameter, see Parameters Reference Guide for Cisco Jabber Release 12.8.

Users in VDI deployments can now
                        choose to mute notification sounds during their calls or meetings.

We improved how Cisco Jabber Softphone for VDI passes presence
                        (status) information to the hosted virtual desktop. Now when a user locks their thin
                        client, their presence updates to Away . If their connection drops, their
                        presence updates to Offline .

We also added a new parameter that
                        controls how Cisco Jabber for Windows handles presence status when users disconnect
                        from their HVDs.

True—When a user signs out or otherwise disconnects from their HVD, Cisco
                              Jabber automatically signs out and presence status updates to Offline , within 10 seconds.

False (default)—When a user signs out, or otherwise disconnects from their
                              HVD, Cisco Jabber remains signed in, and their presence status shows as Available .

For more information about the new parameter, see the Parameters Reference Guide
                        for Cisco Jabber 12.8.

The Cisco Jabber for
                        Windows and Cisco JVDI Agent versions must always match. However, the JVDI Client
                        version can be the same, or up to two releases earlier (N-2 support). For example,
                        the following version combinations are supported:

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and
                              Cisco JVDI Client Release 12.8

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and
                              Cisco JVDI Client Release 12.7

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and
                              Cisco JVDI Client Release 12.6

Sometimes the Cisco JVDI Agent and the Cisco JVDI Client
                        can't communicate. This issue occurs because of a network problem with the virtual
                        channel, or because of a problem with the Cisco Jabber Softphone for VDI
                        installation. If the JVDI Agent and the JVDI Client can't communicate, Cisco Jabber
                        can't operate in VDI-optimized mode. For more information about troubleshooting, see
                        Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release
                        12.8.

This release introduces VDI Fallback mode, and a new parameter to enable
                        this mode. Cisco Jabber Softphone for VDI checks the virtual channel every 10
                        seconds, to ensure that the JVDI Agent and the JVDI Client can communicate. If
                        communication is down, for two consecutive checks, Cisco Jabber Softphone for VDI
                        switches Cisco Jabber to VDI Fallback mode. For more information about the new EnableVDIFallback parameter, see Parameters Reference Guide for Cisco
                        Jabber Release 12.8.

In VDI Fallback mode, users can make and receive calls,
                        with audio traveling over the ICA channel. The connection status for Cisco Jabber
                        changes from Softphone with VDI , to Softphone . Users can receive
                        video; the ability to send video depends on the capabilities of your Citrix version.
                        Audio and video quality depend on network conditions, and the capabilities of your
                        Citrix version. When Cisco Jabber operates in VDI Fallback mode, users see a
                        notification message at the start of each call.

When Cisco Jabber Softphone
                        for VDI detects communication between the JVDI Agent and the JVDI Client, it
                        automatically switches Cisco Jabber back to VDI-optimized mode.

Cisco Jabber Softphone for VDI switches modes only between calls.

### Cisco Jabber Softphone for VDI 12.1

This is the first release of Cisco Jabber Softphone for VDI to support Dell Wyse Thin OS. Cisco Jabber Softphone for VDI —Dell Wyse ThinOS ThinOS 8.6_013 supports Cisco Jabber for Windows Release 12.1.

## Requirements

Each of the components listed in the following table must meet the requirements. Use of unsupported components can result
                                 in a nonfunctional deployment. Only the components, versions, and minimum hardware requirements listed in the table are supported.
                                 For more information about this solution, see the Dell Wyse ThinOS documentation.

The Cisco JVDI Agent, Cisco JVDI Client, and Cisco Jabber for Windows versions must all be the same.

Component

Requirements

Dell Wyse thin clients—Hardware

Wyse ThinOS 8.6_013-based models for 12.1; Wyse ThinOS 8.6_206 or ThinOS Lite 2.6_206-based models for 12.6:

3040

5060

5070

Cisco recommends these models for audio only calls:

3030

5010

5040

Hosted virtual desktop OS (server-side)

Microsoft Windows 7 32 bit

Microsoft Windows 7 64 bit

Microsoft Windows 8 32 bit

Microsoft Windows 8 64 bit

Microsoft Windows 8.1 32 bit

Microsoft Windows 8.1 64 bit

Microsoft Windows 10 32 bit

Microsoft Windows 10 64 bit

Connection broker for the hosted virtual desktop

Citrix Virtual Apps and Desktops (formerly XenApp and XenDesktop) version 7.x and later (1808, 1811, 1903, 1906, 1909, 1912).

7.15 CU5 LTSR Shared Desktop is supported only in full-screen mode.

Citrix Receiver

(Installed on the thin client)

The ICA Client is installed with the Dell-Wyse ThinOS. For version information and more details, see the Dell Wyse ThinOS
                                 Version 8.6 and ThinOS Lite 2.6 documentation.

Citrix Workspace App for Windows is supported, except for the Monitor Layout setting in preferences.

Cisco Unified Communications client on the hosted virtual desktop:

Cisco Jabber for Windows

Cisco Jabber for Windows 12.1 or 12.6 running on the hosted virtual desktop (HVD).

Cisco Jabber Softphone for VDI is compatible with all future 12.1(x) Cisco Jabber for Windows versions.

For complete information about virtual environment compatibility, see the Cisco Jabber documentation for your release.

Cisco Unified Communications Manager

Recommended CUCM Release 11.5(1)SU3 or later

Minimum CUCM Release 10.5

Accessories

For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

Ensure that all Jabra devices are running the latest firmware.

A connection broker is software that creates connections to hosted virtual desktops. A connection broker performs a number
                           of tasks that include

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

The Citrix Receiver provides a user interface for the corresponding connection broker.

## Limitations and Restrictions

### Cisco Expressway

Cisco Jabber Softphone for VDI does not support the use of Mobile Remote Access and Cisco Expressway.

### HDX RealTime Webcam with Citrix

Cisco Jabber Softphone for VDI does not support HDX Plug-n-Play for cameras. Citrix recommends using HDX Webcam for camera interactions.

### Jabber Features

Cisco Jabber Softphone for VDI Release 12.6 supports all Cisco Jabber for Windows Release 12.6 features, except the following:

Audio device selection from the Hub Menu

Cisco Unified Survivable Remote Site Telephony (SRST)

Device Selection menu on the Call Conversation window

Far End Camera Control (FECC)

Federal Information Processing Standard, Publication 140-2 (FIPS 140-2) and Information Assurance (IA) Compliance

Improved Video Resolution (New in Jabber for Windows Release 12.6)

Jabber to Jabber Call

Jabber desk phone video (display of video on the desktop when the thin client is connected to the user's desk phone)

Kerberos and Common Access Card (CAC) with Single Sign On (SSO)

Multiline

Only the first line of a multiline account is available. If a second call comes in, while the first line is in use, the second
                              line rings, but no incoming call notification appears.

PreferP2PDesktopShare (configuration parameter to prioritize person to person screen sharing over video sharing in the Jabber
                              configuration file)

Wireless Screen Sharing (New in Jabber for Windows Release 12.6)

### No Supported Upgrade Path

For more information about installation and configuration, see the Dell Wyse ThinOS documentation for your release.

### SIP Profiles

When you create a Cisco Unified Client Services Framework (CSF) device, you specify a SIP Profile for the device. SIP profiles provide specific SIP information for the phone, such as registration and keepalive timers, media
                        ports, and Do Not Disturb control.

You can use Certificate Authority Proxy Function (CAPF) to manage the phone certificates for the hosted desktop versions of
                        Jabber for Windows. When you change the CAPF Certificate Operation from No Pending Operation to Install/Upgrade , the users must reset Jabber for Windows and sign in to complete the certificate installation.

Do not choose Authentication Mode By Null string when using the Certificate Authority Proxy Function (CAPF).

This setting breaks Cisco Jabber Softphone for VDI registration to Cisco Unified Communications Manager.

## Performance and Behavior Notes

### Camera Hot Swap

Cisco Jabber Softphone for VDI establishes video quality at the start of a call. If you start a call with one of the supported HD cameras, and then switch
                        to a standard-definition camera, video quality is affected. We recommend that you switch cameras between calls.

### Echo Cancellation

Echo cancellation is enabled only for audio calls.

### Jabra Firmware

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information,
                        visit the Jabra website.

### Adjust Settings for Jabra Bluetooth Devices

Most Jabra Bluetooth devices introduce a short delay in bringing up the audio path (about 1 to 3 seconds). For supported Jabra
                        Bluetooth devices, you can eliminate the delay by changing the device settings in Jabra Direct. For more information, visit
                        the Jabra website.

Before you begin

#### Before you begin

Jabra Direct  must be installed.

Open Jabra Direct.

Click the Jabra device for which you want to modify the settings.

Click Settings .

Click to expand Softphone (PC) .

From the Preferred softphone list, select Cisco Jabber .

Set Open phone line to On.

Set PC audio to Off.

Click Apply .

## Caveats

Dell Wyse owns support for Cisco Jabber Softphone for VDI installed on Wyse ThinOS. For information about known issues and
                     bugs, see the Wyse ThinOS documentation for your release.

| Dell Wyse ThinOS Version | Cisco JVDI Version | Cisco Jabber Softphone Build Number |
|---|---|---|
| ThinOS 9.0.3030 | Cisco JVDI Agent 12.9 Cisco JVDI Client 12.9 | 12.09.1142 |
| ThinOS 9.0.1136 | Cisco JVDI Agent 12.8 Cisco JVDI Client 12.8 | 12.08.1089 |
| ThinOS 8.6_206 ThinOS Lite 2.6_206 | Cisco JVDI Agent 12.6 Cisco JVDI Client 12.6 | 12.6.19091611 |
| ThinOS 8.6_013 | Cisco JVDI Agent 12.1 Cisco JVDI Client 12.1 | 12.1.0.266460 |

| Note | Cisco Jabber Softphone for VDI is bundled with the Dell Wyse ThinOS and Dell Wyse owns support. Documentation is available from Dell Wyse. |
|---|---|

| Attention | With N-1 or N-2 support, the lower version determines the available feature
                                    set. |
|---|---|

| Attention | With N-1 or N-2 support, the lower version determines the available feature set. |
|---|---|

| Note | The new parameter replaces the now deprecated HeadsetPreferenceOnVDI parameter. |
|---|---|

| Note | Cisco Jabber Softphone for VDI switches modes only between calls. |
|---|---|

| Attention | With N-1 or N-2 support, the lower version determines the available feature
                                    set. |
|---|---|

| Note | The new parameter replaces the now deprecated HeadsetPreferenceOnVDI parameter. |
|---|---|

| Note | Cisco Jabber Softphone for VDI switches modes only between calls. |
|---|---|

| Important | Each of the components listed in the following table must meet the requirements. Use of unsupported components can result
                                 in a nonfunctional deployment. Only the components, versions, and minimum hardware requirements listed in the table are supported.
                                 For more information about this solution, see the Dell Wyse ThinOS documentation. The Cisco JVDI Agent, Cisco JVDI Client, and Cisco Jabber for Windows versions must all be the same. |
|---|---|

| Component | Requirements |
|---|---|
| Dell Wyse thin clients—Hardware | Wyse ThinOS 8.6_013-based models for 12.1; Wyse ThinOS 8.6_206 or ThinOS Lite 2.6_206-based models for 12.6: 3040 5060 5070 Cisco recommends these models for audio only calls: 3030 5010 5040 |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 32 bit Microsoft Windows 7 64 bit Microsoft Windows 8 32 bit Microsoft Windows 8 64 bit Microsoft Windows 8.1 32 bit Microsoft Windows 8.1 64 bit Microsoft Windows 10 32 bit Microsoft Windows 10 64 bit |
| Connection broker for the hosted virtual desktop 1 | Citrix Virtual Apps and Desktops (formerly XenApp and XenDesktop) version 7.x and later (1808, 1811, 1903, 1906, 1909, 1912). 7.15 CU5 LTSR Shared Desktop is supported only in full-screen mode. |
| Citrix Receiver 2 (Installed on the thin client) | The ICA Client is installed with the Dell-Wyse ThinOS. For version information and more details, see the Dell Wyse ThinOS
                                 Version 8.6 and ThinOS Lite 2.6 documentation. Citrix Workspace App for Windows is supported, except for the Monitor Layout setting in preferences. |
| Cisco Unified Communications client on the hosted virtual desktop: Cisco Jabber for Windows | Cisco Jabber for Windows 12.1 or 12.6 running on the hosted virtual desktop (HVD). Cisco Jabber Softphone for VDI is compatible with all future 12.1(x) Cisco Jabber for Windows versions. For complete information about virtual environment compatibility, see the Cisco Jabber documentation for your release. |
| Cisco Unified Communications Manager | Recommended CUCM Release 11.5(1)SU3 or later Minimum CUCM Release 10.5 |
| Accessories | For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html . Important Ensure that all Jabra devices are running the latest firmware. | Important | Ensure that all Jabra devices are running the latest firmware. |
| Important | Ensure that all Jabra devices are running the latest firmware. |

| Important | Ensure that all Jabra devices are running the latest firmware. |
|---|---|

| Important | Do not choose Authentication Mode By Null string when using the Certificate Authority Proxy Function (CAPF). This setting breaks Cisco Jabber Softphone for VDI registration to Cisco Unified Communications Manager. |
|---|---|

| Step 1 | Open Jabra Direct. |
|---|---|
| Step 2 | Click the Jabra device for which you want to modify the settings. |
| Step 3 | Click Settings . |
| Step 4 | Click to expand Softphone (PC) . |
| Step 5 | From the Preferred softphone list, select Cisco Jabber . |
| Step 6 | Set Open phone line to On. |
| Step 7 | Set PC audio to Off. |
| Step 8 | Click Apply . |