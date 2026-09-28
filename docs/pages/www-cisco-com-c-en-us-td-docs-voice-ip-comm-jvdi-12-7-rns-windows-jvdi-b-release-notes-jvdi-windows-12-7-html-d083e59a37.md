---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-7-rns-windows-jvdi-b-release-notes-jvdi-windows-12-7-html-d083e59a37
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_7/rns/windows/jvdi_b_release-notes-jvdi-windows-12-7.html
retrieved_at: 2026-08-22T00:42:02.640510+00:00
---

Release Notes for Cisco Jabber Softphone for VDI—Windows Release 12.7

# Release Notes for Cisco Jabber Softphone for VDI—Windows Release 12.7

### Download Options

Updated: February 13, 2020

First Published: September 9, 2019

Last Updated: October 12, 2022

# Build Number for 12.7

Version

Build Number

JVDI Agent Release 12.7

12.7.0.288594

JVDI Client Release 12.7

12.7.0.288594

JVDI Agent Release 12.7(1)

12.7.1.301081

JVDI Client Release 12.7(1)

12.7.1.301081

## What's New in Cisco Jabber Softphone for VDI—Windows Release 12.7(1)

### Cisco Jabber Support

We've added support for Cisco Jabber for Windows Release 12.7(1).

### Cisco Headset Support for 64–bit

We've enhanced call control support for Cisco headsets, with 64–bit versions of Microsoft Windows.

## What's New in Cisco Jabber Softphone for VDI Windows Release 12.7

### Cisco Jabber Support

Cisco Jabber Softphone for VDI supports the following new Cisco Jabber for Windows Release 12.7 features:

BOT Support

Display Directory Number or Label for Single Lines

Call Progress Indicator for Extend & Connect

Chat Rooms Maintains Participant List Visibility

Configure Clients Through Cisco Webex Control Hub

Device Selection from the Conversation Window

Enhancement to Security Labels

Enterprise Content Management (ECM) Support

People Insights

Improved Office 365 Migration Authentication Notification

Improved Voicemail

Modern Design

OAuth Handling of Refresh Tokens

OAuth Sign-Out Behavior

On-Demand Recording

Presence Based on Non-Jabber Activity

Proxy Authentication Support

Quote Message

Themes

For more information about the new Cisco Jabber features, see Release Notes for Cisco Jabber for Windows : https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html .

For a list of Cisco Jabber features that are not supported with Cisco Jabber Softphone for VDI, see Cisco Jabber Features .

### CTI Failover Support

We've added support for CTI failover. When a failover occurs, from one Cisco Unified Communications Manager to another, Cisco Jabber for Windows retains phone functionality.

### Headset Preference Parameter

This release includes a new parameter for controlling headset selection. By default, when you connect a new headset Cisco
                        Jabber adds it to the top of the priority list. This is a problem in some hot-desking environments. When a user moves their
                        thin client and headset, the embedded microphone becomes the preferred device. You can set this parameter to ensure that the
                        user's headset remains the preferred device.

The parameter applies only to Cisco Jabber Softphone for VDI (all platforms)

You can use the parameter to specify whether Cisco Jabber adds a new device to the top, or to the bottom of the device priority
                        list in the Advanced settings.

PreferNewDevice (default)—Cisco Jabber adds the new headset to the top of the list, and makes it the preferred device.

PreferOldDevice—Cisco Jabber adds a new headset to the bottom of the list with no change to the configured preferred device

Example:

```
<HeadsetPreferenceOnVDI>PreferOldDevice</HeadsetPreferenceOnVDI>
```

### Multiline Support

We have added support for the Cisco Jabber Multiline feature. Multiline provides mid-call features such as hold, transfer,
                        and call forward, for users with more than one configured line. Multiline even works for video calls. You can configure up
                        to eight lines in softphone mode. Only the primary line is supported when users access Cisco Jabber using Mobile and Remote
                        Access (MRA).

Cisco Jabber for Windows supports Cisco Hosted Collaboration Solution (HCS), Cisco Packaged Contact Center Enterprise (PCCE),
                        Cisco Contact Center Enterprise (CCE), and Cisco Unified Contact Center Express (CCX) 11.6 (up to four lines). For more information,
                        see the Features Configuration Guide for Cisco Jabber .

### Roaming Profiles

In a virtual environment, users do not always access the same virtual desktop. To guarantee a consistent user experience,
                        their profiles must be accessible every time they start Cisco Jabber. We have added support for roaming profiles. Cisco Jabber
                        with Cisco Jabber Softphone for VDI stores data in the following locations:

%currentuser%\AppData\ Local \Cisco

Contacts —Contact cache files

History —Call and chat history

Photo cache —Caches the directory photos locally

%currentuser%\AppData\Roaming\Cisco

Config —Maintains user configuration files and stores configuration store cache

Credentials —Stores encrypted username and password file

Because file encryption and decryption are linked to the Windows user profile, ensure that the following folders are accessible:

C:\Users\ username \AppData\Roaming\Microsoft\Crypto

C:\Users\ username \AppData\Roaming\Microsoft\Credentials

C:\Users\ username \AppData\Local\Microsoft\Crypto

C:\Users\ username \AppData\local\Microsoft\Credentials

For more information, see the Planning Guide for Cisco Jabber .

### Updated Citrix Virtual Apps and Desktops Support

Citrix Virtual Apps and Desktops was formerly known as Citrix XenApp and Citrix XenDesktop.

Cisco Jabber Softphone for VDI Release 12.7 supports Citrix-based published desktops, shared desktops, and shared applications (full-screen and windows
                        modes).

### Version Support Strategy

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the JVDI Client version can be the
                        same, or the prior release (N-1 support). The following version combinations are supported:

Cisco Jabber for Windows Release 12.7, Cisco JVDI Agent Release 12.7, and Cisco JVDI Client Release 12.7

Cisco Jabber for Windows Release 12.7, Cisco JVDI Agent Release 12.7, and Cisco JVDI Client Release 12.6

## General Requirements

General requirements apply to all Cisco Jabber Softphone for VDI platforms.

Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment.

### Accessories

For a complete listing of recommended audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware.

### Cisco Jabber for Windows

Cisco Jabber for Windows 12.7 running on the hosted virtual desktop (HVD).

For complete information about virtual environment compatibility, see the Cisco Jabber documentation for your release.

### Cisco Unified Communications Manager

Recommended: CUCM Release 11.5(1)SU3 or later

Minimum: CUCM Release 10.5

### Connection Broker—Installed on the Hosted Virtual Desktops

Citrix Virtual Apps and Desktops (formerly XenApp and XenDesktop) versions 7.x–7.1909, and 7.15 LTSR up to CU4

Shared Desktop is supported only in full-screen mode. Published Application is supported in full-screen mode for Cisco Jabber
                           Softphone for VDI—Windows.

VMware Horizon 6 versions 6.x–7.10

A connection broker is software that creates connections to hosted virtual desktops. A connection broker performs a number
                     of tasks including the following:

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

### Operating Systems—Installed on the Hosted Virtual Desktops

Microsoft Windows 7 32–bit

Microsoft Windows 7 64–bit

Microsoft Windows 8 32–bit

Microsoft Windows 8 64–bit

Microsoft Windows 8.1 32–bit

Microsoft Windows 8.1 64 64–bit

Microsoft Windows 10 32–bit

Microsoft Windows 10 64–bit

### Server Operating Systems—Installed on the Hosted Virtual Desktops

Microsoft Windows Server 2012 R2

Microsoft Windows Server 2016

### Port Requirements

Cisco Jabber Softphone for VDI requires the same ports as Cisco Jabber does, and the following additional port range:

Port Range

Description

16384–32767

UDP Inbound and outbound traffic for RTP (audio and video streams)

You can configure the Cisco Unified Communications Manager to reduce this port range. Change the Start/Stop Media Port setting in the SIP Profile, which is associated with the CSF device.

### Supported Codecs

Audio Codecs:

G.722

G.722.1 (24 and 32k)

G.722.1 is supported on Cisco Unified Communications Manager 8.6.1 or later.

G.711 A-law

G.711 u-law

G.729a

Opus

Opus is supported on Cisco Unified Communications Manager 11.0 or later.

Video Codec: H.264/AVC

## Requirements—Windows Thin Clients

Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment.

### Microsoft Windows Thin Clients—Hardware

The minimum system requirements for thin clients are as follows:

Installed RAM 2 GB

Free Physical Memory 1 GB

Free Disk Space 256 MB

CPU Mobile AMD Sempron Processor 3600+, 2-GHz Intel Core 2 CPU, or T7400 2.16 GHz

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

### Microsoft Windows—Installed on the Thin Clients

Microsoft Windows 7 32–bit

Requires Update for Windows 7 (KB4019990)

Microsoft Windows 7 64–bit

Requires Update for Windows 7 for x64–based Systems (KB4019990)

Microsoft Windows 8 32–bit

Microsoft Windows 8 64–bit

Microsoft Windows 8.1 32–bit

Microsoft Windows 8.1 64–bit

Microsoft Windows 10 32–bit

Microsoft Windows 10 64–bit

Windows Thin PC 32–bit

Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules.

### Windows Embedded Standard Thin Clients—Hardware

The minimum system requirements for thin clients are as follows:

Installed RAM 2 GB

Free Physical Memory 1 GB

Free Disk Space 256 MB

CPU performance affects the maximum video resolution. With Windows Embedded Standard thin clients, the expected resolution
                           depends on the CPU:

Up to 720p with quad-core AMD GX-420CA SOC 2 GHz or similar

Up to 240p with dual-core AMD G-T56N 1.65 GHz or similar

Audio-only support with dual-core VIA Eden X2 U4200 1 GHz or similar CPU

These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution.

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

### Windows Embedded Standard—Installed on the Thin Clients

Windows Embedded Standard 7 32–bit

Requires Update for Windows Embedded Standard 7 (KB4019990)

Windows Embedded Standard 7 64–bit

Requires Update for Windows Embedded Standard 7 for 64–bit Systems (KB4019990)

Windows Embedded Standard 8 64–bit

Requires Update for Windows Embedded Standard 8 for 64–bit Systems (KB4019990)

Windows 10 IoT Enterprise

### Citrix Workspace App or VMware Horizon Client—Installed on the Thin Clients

Citrix Receiver (ICA) for Windows 4.4, and up to 4.12

Citrix Workspace App (ICA) for Windows 1808, and up to 1907

Cisco Jabber Softphone for VDI does not support Citrix Workspace App downloaded from the Microsoft Store.

VMware Horizon Client for Windows 4.1.0, 4 and up to 5.0

(Versions 4.3 and 4.4 are not supported.)

The Citrix Workspace app or VMware Horizon Client provides a user interface for the corresponding connection broker.

Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client.

If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client.

## Limitations and Restrictions

### Accessory Call Control

Accessory call control (adjust call volume, answer or end phone calls, and mute audio) is supported for compatible headsets.
                        Some other headsets provide basic functionality, but the accessory call control features do not work with Cisco Jabber Softphone for VDI . For a complete list of compatible headsets and other accessories, see https://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

### Call Preservation Mode

Cisco Jabber Softphone for VDI does not support Call Preservation, also known as "survivability" . If a network interruption occurs and Cisoc Jabber goes into Call Preservation mode, the calls drop for VDI users.

### Changes to Your Connection Method

You must always install Citrix or VMware before you install the JVDI Client. Therefore, you must reinstall the JVDI Client
                        after one of the following changes:

Linux platforms

Upgrading Citrix or VMware

Switching from Citrix to VMware, or from VMware to Citrix

Windows and Mac platforms

Switching from Citrix to VMware, or from VMware to Citrix

### Cisco Jabber Features

Cisco Jabber Softphone for VDI Release 12.7 supports all Cisco Jabber for Windows Release 12.7 features, except the following:

Application Sharing

Audio device selection from the Hub Menu

Cisco Unified Survivable Remote Site Telephony (SRST)

Migrate Custom Contacts

Far End Camera Control (FECC)

Federal Information Processing Standard, Publication 140-2 (FIPS 140-2) and Information Assurance (IA) Compliance

Improved Video Resolution

Cisco Jabber to Jabber Call

Cisco Jabber desk phone video (display of video on the desktop when the thin client is connected to the user's desk phone)

Kerberos and Common Access Card (CAC) with Single Sign On (SSO)

Cisco Jabber Softphone for VDI does not support CAC, and supports Kerberos only with SSO.

PreferP2PDesktopShare (configuration parameter to prioritize person to person screen sharing over video sharing in the Cisco Jabber configuration file)

Wireless Screen Sharing

### HDX RealTime Webcam with Citrix

Cisco Jabber Softphone for VDI does not support HDX Plug-n-Play for cameras. Citrix recommends using HDX Webcam for camera interactions.

### Remote Display Protocol Support

Cisco Jabber Softphone for VDI supports only PC-over-IP (PCoIP) for VMware and ICA for Citrix.

### SIP Profiles

When you create a Cisco Unified Client Services Framework (CSF) device, you specify a SIP Profile for the device. SIP profiles provide specific SIP information for the phone, such as registration and keepalive timers, media
                        ports, and Do Not Disturb control.

You can use Certificate Authority Proxy Function (CAPF) to manage the phone certificates for the hosted desktop versions of
                        Jabber for Windows. When you change the CAPF Certificate Operation from No Pending Operation to Install/Upgrade , the users must reset Jabber for Windows and sign in to complete the certificate installation.

Do not choose Authentication Mode By Null string when using the Certificate Authority Proxy Function (CAPF).

This setting breaks Cisco Jabber Softphone for VDI registration to Cisco Unified Communications Manager.

### USB Camera Redirection Not Supported with VMware View

USB camera redirection is not supported with VMware View.

### VMware Support

Cisco Jabber Softphone for VDI does not support Display Scaling mode. Users should check their VMware Options menu and ensure that Allow Display Scaling is not checked.

Cisco Jabber Softphone for VDI supports full-screen display only; windows mode is not supported.

## Performance and Behavior Notes

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

### Camera Hot Swap

Cisco Jabber Softphone for VDI establishes video quality at the start of a call. If you start a call with one of the supported HD cameras, and then switch
                        to a standard-definition camera, video quality is affected. We recommend that you switch cameras between calls.

### Cisco Jabber Installed on the Thin Client

We recommend that you do not install Cisco Jabber on the thin clients. If you do install Cisco Jabber on the thin clients, ensure that users sign out of Cisco Jabber before they sign in to their hosted virtual desktops. Cisco Jabber Softphone for VDI works only with Cisco Jabber installed on the HVD.

### Echo Cancellation

Echo cancellation is enabled only for audio calls.

### Jabra Firmware

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information,
                        visit the Jabra website.

### Video Codec Performance

Software decoding relies heavily on the CPU. Estimated CPU usage for the Cisco JVDI Client with lower-end CPUs is as follows:

1.5Ghz, Dual core CPU—65% (55 to 75%)

1.5Ghz, Quad core CPU—35% (25 to 45%)

Use of a camera with a built-in hardware decoder reduces the load on the CPU.

## Caveats

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

### Open Caveats in Release 12.7(1)

There are no open caveats (bugs) for this release.

### Resolved Caveats in Release 12.7(1)

The following table lists caveats (bugs) that are fixed for this release.

Caveat ID Number

Severity

Description

CSCvr46635

2

JVDI Client Windows 7 Call Controls not visible in a Video Call

CSCvr63558

3

VXME Video starts automatically despite being disabled

### Open Caveats in Release 12.7

Caveat ID Number

Severity

Description

CSCvq33970

2

SIP delays coming from VXME 11.9.

### Resolved Caveats in Release 12.7

The following table lists caveats (bugs) that are fixed for this release.

Caveat ID Number

Severity

Description

CSCvk25632

3

Jabber a split second of video from previous call is seen

CSCvq22868

3

Caller ID presentation of redirected calls for Jabber for Windows in VDI

CSCvq59211

3

[VMware]JVDI softphone not reconnecting

CSCvr15121

3

Jabber HVD is not able to verify Exp-E certificate

CSCvr13324

4

VXME for Windows 12.6.1 - jabber.log file saved in thin client desktop

CSCvp95567

6

JVDI - Device Selection menu on the Call Conversation window

| Version | Build Number |
|---|---|
| JVDI Agent Release 12.7 | 12.7.0.288594 |
| JVDI Client Release 12.7 | 12.7.0.288594 |
| JVDI Agent Release 12.7(1) | 12.7.1.301081 |
| JVDI Client Release 12.7(1) | 12.7.1.301081 |

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment. |
|---|---|

| Port Range | Description |
|---|---|
| 16384–32767 | UDP Inbound and outbound traffic for RTP (audio and video streams) You can configure the Cisco Unified Communications Manager to reduce this port range. Change the Start/Stop Media Port setting in the SIP Profile, which is associated with the CSF device. |

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment. |
|---|---|

| Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
|---|---|

| Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. |
|---|---|

| Important | Cisco Jabber Softphone for VDI does not support Citrix Workspace App downloaded from the Microsoft Store. |
|---|---|

| Important | Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. |
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

| Caveat ID Number | Severity | Description |
|---|---|---|
| CSCvr46635 | 2 | JVDI Client Windows 7 Call Controls not visible in a Video Call |
| CSCvr63558 | 3 | VXME Video starts automatically despite being disabled |

| Caveat ID Number | Severity | Description |
|---|---|---|
| CSCvq33970 | 2 | SIP delays coming from VXME 11.9. |

| Caveat ID Number | Severity | Description |
|---|---|---|
| CSCvk25632 | 3 | Jabber a split second of video from previous call is seen |
| CSCvq22868 | 3 | Caller ID presentation of redirected calls for Jabber for Windows in VDI |
| CSCvq59211 | 3 | [VMware]JVDI softphone not reconnecting |
| CSCvr15121 | 3 | Jabber HVD is not able to verify Exp-E certificate |
| CSCvr13324 | 4 | VXME for Windows 12.6.1 - jabber.log file saved in thin client desktop |
| CSCvp95567 | 6 | JVDI - Device Selection menu on the Call Conversation window |