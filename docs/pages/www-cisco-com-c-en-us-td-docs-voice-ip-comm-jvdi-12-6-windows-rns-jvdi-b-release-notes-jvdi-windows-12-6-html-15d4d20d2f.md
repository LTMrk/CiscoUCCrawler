---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-6-windows-rns-jvdi-b-release-notes-jvdi-windows-12-6-html-15d4d20d2f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_6/windows/rns/jvdi_b_release-notes-jvdi-windows-12-6.html
retrieved_at: 2026-08-22T00:42:23.646747+00:00
---

Release Notes for Cisco Jabber Softphone for VDI—Windows Release 12.6

# Release Notes for Cisco Jabber Softphone for VDI—Windows Release 12.6

### Download Options

Updated: January 23, 2020

First Published: April 10, 2019

Last Updated: October 12, 2022

# Build Number for 12.6

Version

Build Number

Cisco JVDI Agent 12.6

12.6.0.281218

Cisco JVDI Client 12.6

12.6.0.281218

Cisco JVDI Agent 12.6(1)

12.6.1.34405

Cisco JVDI Client 12.6(1)

12.6.1.34405

## Cisco Jabber Softphone for VDI Copyright

Copyright © 2018–2020 Cisco or its affiliated entities. All Rights Reserved.

## What's New in Cisco Jabber Softphone for VDI—Windows 12.6(2)

### Cisco Jabber Support

## What's New in Cisco Jabber Softphone for VDI—Windows 12.6(1)

### Cisco Jabber Support

Cisco Jabber Softphone for VDI supports the following new Cisco Jabber features:

Support for Cisco Headsets

Display Cisco Headset Version

Reset Cisco Headset to Default Settings

Keypad Support Enhancements

For more information about the new Cisco Jabber features, see Release Notes for Cisco Jabber for Windows : https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html .

For a list of Cisco Jabber features that are not supported with Cisco Jabber Softphone for VDI, see Jabber Features .

## What's New in Cisco Jabber Softphone for VDI—Windows 12.6

### Binary Floor Control Protocol Support

Jabber Softphone for VDI supports Binary Floor Control Protocol (BFCP) screen sharing. Cisco Unified Communications Manager
                        controls this feature and handles the BFCP packets that are transmitted during BFCP screen sharing. During BFCP screen sharing,
                        the thin client screen is shared.

Remote screen control is not supported with this feature.

### Cisco Jabber Support

This release adds support for Cisco Jabber for Windows Release 12.6.

Cisco Jabber Softphone for VDI supports the following new Cisco Jabber features:

Accessory Call Control (adjust call volume, answer or end phone calls, and mute audio) for the following accessories:

Cisco

Jabra

Logitech

Plantronics

Sennheiser

ActiveControl Support Over the MRA Expressway

Hide Persistent Chat Room Members

High Contrast Mode

Interoperability for Jabber and Webex Teams

Jabber Team Messaging Mode

Keypad Support

Meeting Controls for Video Device-Enabled Meetings

Offline Messaging for Interoperability Users

Save Chat History to Office 365

SPAM Prevention

Support for Cisco Headsets

Cisco Headset Management

New Audio Controls for Cisco Headsets

Support for Special Characters

UDS Failover

For more information about the new Cisco Jabber features, see the Release Notes for Cisco Jabber for Windows : https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html .

For a list of Cisco Jabber features that are not supported with Cisco Jabber Softphone for VDI, see Jabber Features .

### Connection Status

The Connection Status window for Cisco Jabber for Windows includes information for Cisco Jabber Softpone for VDI. A green checkmark indicates a
                        successful connection. You can display more information by clicking JVDI Details .

### Meeting Controls for Cisco Meeting Server Meetings

Jabber Softphone for VDI users can use ActiveControl to participate in their meetings on the Cisco Meeting Server. ActiveControl
                        provides enhanced conferencing features, including the following management functions:

Choose the video layout.

Record calls.

Mute and unmute yourself and others.

Lock conference calls.

You set up ActiveControl in Cisco Meeting Server 2.3 or later and need Cisco Unified Communications Manager 10.5 or later.

### Support for Cisco Expressway for Mobile and Remote Access

Jabber Softphone for VDI supports the use of Expressway for Mobile and Remote Access (MRA) to connect to the corporate network.
                        Jabber Softphone for VDI supports Citrix NetScaler Gateway.

For supported versions, see the documentation for your version of Cisco Jabber for Windows.

We recommend VCS-E version X8.11.2. Earlier versions do not support CTI initial JOIN operations and cannot merge multiple
                                    calls into a meeting.

For more information, see the Mobile and Remote Access via Cisco Expressway Deployment Guide for your release:

https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html

### Version Support Strategy

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the JVDI Client version can be the
                        same, or up to two releases earlier (N-2 support). For example, the following version combinations are supported:

Cisco Jabber for Windows Release 12.6, Cisco JVDI Agent Release 12.6, and Cisco JVDI Client Release 12.6

Cisco Jabber for Windows Release 12.6, Cisco JVDI Agent Release 12.6, and Cisco JVDI Client Release 12.5

Cisco Jabber for Windows Release 12.6, Cisco JVDI Agent Release 12.6, and Cisco JVDI Client Release 12.1

The limitations and restrictions for the earlier JVDI Client release apply. The available features are limited to those available
                                    for the earlier release. For more information, see the , for the earlier release. For example, if your JVDI Client Release
                                    is 12.1, see the release notes document for Release 12.1.

### Windows 64-bit Support

You can install the 64–bit version of Cisco Jabber Softphone for VDI on thin clients running Windows 64-bit operating systems.

If you plan to install the 32–bit version of Jabber Softphone for VDI, see the "VMware Installation—Required Setting" section of the deployment guide.

## Requirements

Each of the components listed in the following table must meet the requirements. Use of unsupported components can result
                                 in a nonfunctional deployment.

Only the components, versions, and minimum hardware requirements listed in the table are supported.

Component

Requirements

Microsoft Windows-based thin client hardware

Installed RAM 2 GB

Free Physical Memory 128 MB

Free Disk Space 256 MB

CPU Mobile AMD Sempron Processor 3600+, 2-GHz Intel Core 2 CPU, or T7400 2.16 GHz

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules.

Microsoft Windows-based thin client OS

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

Windows Embedded Standard-based thin client hardware

Installed RAM 2 GB

Free Physical Memory 128 MB

Free Disk Space 256 MB

CPU performance affects the maximum video resolution. With Windows Embedded Standard thin clients, the expected resolution
                                       depends on the CPU:

Up to 720p with quad-core AMD GX-420CA SOC 2 GHz or similar

Up to 240p with dual-core AMD G-T56N 1.65 GHz or similar

Audio-only support with dual-core VIA Eden X2 U4200 1 GHz or similar CPU

These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution.

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules.

Windows Embedded Standard-based thin client OS

Windows Embedded Standard 7 32–bit

Requires Update for Windows Embedded Standard 7 (KB4019990)

Windows Embedded Standard 7 64–bit

Requires Update for Windows Embedded Standard 7 for 64–bit Systems (KB4019990)

Windows Embedded Standard 8 64–bit

Requires Update for Windows Embedded Standard 8 for 64–bit Systems (KB4019990)

Windows 10 IoT Enterprise

Hosted virtual desktop OS (server-side)

Microsoft Windows 7 32 bit

Microsoft Windows 7 64 bit

Microsoft Windows 8 32 bit

Microsoft Windows 8 64 bit

Microsoft Windows 8.1 32 bit

Microsoft Windows 8.1 64 bit

Microsoft Windows 10 32 bit

Microsoft Windows 10 64 bit

VCRUNTIME140.dll

and

MSVCP140.dll

Visual Studio C++ 2012 Redistributable Update 4 or later versions

Connection broker for the hosted virtual desktop

Citrix Virtual Apps and Desktops (formerly XenApp and XenDesktop) 7.5 and later 7.x versions—Published Desktop and Published
                                       Application

Published Application is not supported in full-screen mode.

VMware Horizon 6.0 (with View)—Published desktops only

VMware Horizon 6 version 6.1.0—Published desktops only

VMware Horizon 6 version 6.2.0—Published desktops only

VMware Horizon 7 version 7.x—Published desktops only

For information about an issue that occurs when using some VMware Horizon 7.3.x versions, see CSCvk30137 .

Citrix Receiver, Citrix Workspace App, or

VMware Horizon Client

(Installed on the thin client)

Citrix Receiver (ICA) for Windows 4.4, and up to 4.12

Citrix Workspace App (ICA) for Windows 1808, and up to 1907

Cisco Jabber Softphone for VDI does not support Citrix Workspace App downloaded from the Microsoft Store.

VMware Horizon Client for Windows 4.1.0, 4 and later 4.x version. (Versions 4.3 and 4.4 are not supported.)

Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client.

If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client.

Cisco Unified Communications client on the hosted virtual desktop:

Cisco Jabber for Windows.

Cisco Jabber for Windows 12.6 running on the hosted virtual desktop (HVD).

Cisco Jabber Softphone for VDI is compatible with all future 12.6(x) Cisco Jabber for Windows versions.

For complete information about virtual environment compatibility, see the documentation for Cisco Jabber .

Cisco Unified Communications Manager

Recommended CUCM Release 11.5(1)SU3 or later

Minimum CUCM Release 10.5

Accessories

For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

Ensure that all Jabra devices are running the latest firmware. You can use the Jabra Direct to update the firmware. For more
                                          information visit: http://www.jabra.com .

A connection broker is software that creates connections to hosted virtual desktops. A connection broker performs a number
                           of tasks that include

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

The Citrix Workspace app or VMware Horizon Client provides a user interface for the corresponding connection broker.

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

### Cisco Unified Communications Manager Failover

When a failover from one Cisco Unified Communications Manager to another occurs, Cisco Jabber for Windows retains phone functionality. However, with Cisco Jabber Softphone for VDI , phone functionality is lost. This issue occurs because CTI failover is not supported in the virtual environment.

### Citrix Virtual Apps and Desktops Support

Citrix Virtual Apps and Desktops was formerly known as XenApp and XenDesktop.

### Citrix XenApp Support

Citrix XenApp Published Application is not supported in full-screen mode. You can disable full-screen mode in the Citrix Receiver
                        > Connection Center, on the thin client.

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

### Display Settings

For optimal video performance, use the recommended settings for Citrix or VMware.

With Citrix XenDesktop and VMware, only full-screen mode is supported on the Linux-based platforms:

Cisco Virtualization Experience Client—HP Thin Pro and Ubuntu

Cisco Virtualization Experience Client—SUSE Linux

Cisco Virtualization Experience Client—Unicon eLux

Citrix XenApp Published Application is supported only on Cisco Virtualization Experience Client —Windows, in windows mode only.

#### Citrix

Cisco Virtualization Experience Client supports only the Preferences > Display > Best resolution (Recommended) display option.

#### VMware

Have users check their VMware options to ensure that the Allow Display Scaling option is unchecked.

### Jabra Firmware

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information,
                        visit the Jabra website.

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

### Open Caveats in Release 12.6(2)

### Resolved Caveats in Release 12.6(2)

### Open Caveats in Release 12.6(1)

There are no open caveats (bugs) for this maintenance release.

### Resolved Caveats in Release 12.6(1)

The following table lists caveats (bugs) that are fixed for this maintenance release.

Caveat ID Number

Severity

Description

CSCvp53311

2

JVDI user can't see fat client video when they share on webex. Video goes black

CSCvp64224

2

DTMF digits not transferred in time (within 50ms)

CSCvk25632

3

Jabber a split second of video from previous call is seen

CSCvp53045

3

JVDI is not working after VDI reset

CSCvq00090

3

ringer "all device" settings not sticking

### Closed Caveats in Release 12.6

There are no closed caveats (bugs) for this release.

### Open Caveats in Release 12.6

There are no open caveats for this release.

### Resolved Caveats in Release 12.6

The following table lists caveats (bugs) that are fixed for this release.

Caveat ID

Severity

Heading

| Version | Build Number |
|---|---|
| Cisco JVDI Agent 12.6 | 12.6.0.281218 |
| Cisco JVDI Client 12.6 | 12.6.0.281218 |
| Cisco JVDI Agent 12.6(1) | 12.6.1.34405 |
| Cisco JVDI Client 12.6(1) | 12.6.1.34405 |

| Attention | We recommend VCS-E version X8.11.2. Earlier versions do not support CTI initial JOIN operations and cannot merge multiple
                                    calls into a meeting. |
|---|---|

| Important | The limitations and restrictions for the earlier JVDI Client release apply. The available features are limited to those available
                                    for the earlier release. For more information, see the , for the earlier release. For example, if your JVDI Client Release
                                    is 12.1, see the release notes document for Release 12.1. |
|---|---|

| Important | Each of the components listed in the following table must meet the requirements. Use of unsupported components can result
                                 in a nonfunctional deployment. Only the components, versions, and minimum hardware requirements listed in the table are supported. |
|---|---|

| Component | Requirements |
|---|---|
| Microsoft Windows-based thin client hardware | Installed RAM 2 GB Free Physical Memory 128 MB Free Disk Space 256 MB CPU Mobile AMD Sempron Processor 3600+, 2-GHz Intel Core 2 CPU, or T7400 2.16 GHz DirectX 11 compatible GPU USB 2.0 for USB camera and audio devices Note Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. | Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Microsoft Windows-based thin client OS | Microsoft Windows 7 32–bit Requires Update for Windows 7 (KB4019990) Microsoft Windows 7 64–bit Requires Update for Windows 7 for x64–based Systems (KB4019990) Microsoft Windows 8 32–bit Microsoft Windows 8 64–bit Microsoft Windows 8.1 32–bit Microsoft Windows 8.1 64–bit Microsoft Windows 10 32–bit Microsoft Windows 10 64–bit Windows Thin PC 32–bit |
| Windows Embedded Standard-based thin client hardware | Installed RAM 2 GB Free Physical Memory 128 MB Free Disk Space 256 MB CPU performance affects the maximum video resolution. With Windows Embedded Standard thin clients, the expected resolution
                                       depends on the CPU: Up to 720p with quad-core AMD GX-420CA SOC 2 GHz or similar Up to 240p with dual-core AMD G-T56N 1.65 GHz or similar Audio-only support with dual-core VIA Eden X2 U4200 1 GHz or similar CPU Note These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. DirectX 11 compatible GPU USB 2.0 for USB camera and audio devices Note Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. | Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. | Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. |
| Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Windows Embedded Standard-based thin client OS | Windows Embedded Standard 7 32–bit Requires Update for Windows Embedded Standard 7 (KB4019990) Windows Embedded Standard 7 64–bit Requires Update for Windows Embedded Standard 7 for 64–bit Systems (KB4019990) Windows Embedded Standard 8 64–bit Requires Update for Windows Embedded Standard 8 for 64–bit Systems (KB4019990) Windows 10 IoT Enterprise |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 32 bit Microsoft Windows 7 64 bit Microsoft Windows 8 32 bit Microsoft Windows 8 64 bit Microsoft Windows 8.1 32 bit Microsoft Windows 8.1 64 bit Microsoft Windows 10 32 bit Microsoft Windows 10 64 bit |
| VCRUNTIME140.dll and MSVCP140.dll | Visual Studio C++ 2012 Redistributable Update 4 or later versions |
| Connection broker for the hosted virtual desktop 1 | Citrix Virtual Apps and Desktops (formerly XenApp and XenDesktop) 7.5 and later 7.x versions—Published Desktop and Published
                                       Application Important Published Application is not supported in full-screen mode. VMware Horizon 6.0 (with View)—Published desktops only VMware Horizon 6 version 6.1.0—Published desktops only VMware Horizon 6 version 6.2.0—Published desktops only VMware Horizon 7 version 7.x—Published desktops only Attention For information about an issue that occurs when using some VMware Horizon 7.3.x versions, see CSCvk30137 . | Important | Published Application is not supported in full-screen mode. | Attention | For information about an issue that occurs when using some VMware Horizon 7.3.x versions, see CSCvk30137 . |
| Important | Published Application is not supported in full-screen mode. |
| Attention | For information about an issue that occurs when using some VMware Horizon 7.3.x versions, see CSCvk30137 . |
| Citrix Receiver, Citrix Workspace App, or VMware Horizon Client 2 (Installed on the thin client) | Citrix Receiver (ICA) for Windows 4.4, and up to 4.12 Citrix Workspace App (ICA) for Windows 1808, and up to 1907 Important Cisco Jabber Softphone for VDI does not support Citrix Workspace App downloaded from the Microsoft Store. VMware Horizon Client for Windows 4.1.0, 4 and later 4.x version. (Versions 4.3 and 4.4 are not supported.) Important Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. | Important | Cisco Jabber Softphone for VDI does not support Citrix Workspace App downloaded from the Microsoft Store. | Important | Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. |
| Important | Cisco Jabber Softphone for VDI does not support Citrix Workspace App downloaded from the Microsoft Store. |
| Important | Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. |
| Cisco Unified Communications client on the hosted virtual desktop: Cisco Jabber for Windows. | Cisco Jabber for Windows 12.6 running on the hosted virtual desktop (HVD). Cisco Jabber Softphone for VDI is compatible with all future 12.6(x) Cisco Jabber for Windows versions. For complete information about virtual environment compatibility, see the documentation for Cisco Jabber . |
| Cisco Unified Communications Manager | Recommended CUCM Release 11.5(1)SU3 or later Minimum CUCM Release 10.5 |
| Accessories | For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html . Important Ensure that all Jabra devices are running the latest firmware. You can use the Jabra Direct to update the firmware. For more
                                          information visit: http://www.jabra.com . | Important | Ensure that all Jabra devices are running the latest firmware. You can use the Jabra Direct to update the firmware. For more
                                          information visit: http://www.jabra.com . |
| Important | Ensure that all Jabra devices are running the latest firmware. You can use the Jabra Direct to update the firmware. For more
                                          information visit: http://www.jabra.com . |

| Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
|---|---|

| Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. |
|---|---|

| Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
|---|---|

| Important | Published Application is not supported in full-screen mode. |
|---|---|

| Attention | For information about an issue that occurs when using some VMware Horizon 7.3.x versions, see CSCvk30137 . |
|---|---|

| Important | Cisco Jabber Softphone for VDI does not support Citrix Workspace App downloaded from the Microsoft Store. |
|---|---|

| Important | Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. |
|---|---|

| Important | Ensure that all Jabra devices are running the latest firmware. You can use the Jabra Direct to update the firmware. For more
                                          information visit: http://www.jabra.com . |
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
| CSCvp53311 | 2 | JVDI user can't see fat client video when they share on webex. Video goes black |
| CSCvp64224 | 2 | DTMF digits not transferred in time (within 50ms) |
| CSCvk25632 | 3 | Jabber a split second of video from previous call is seen |
| CSCvp53045 | 3 | JVDI is not working after VDI reset |
| CSCvq00090 | 3 | ringer "all device" settings not sticking |

| Caveat ID | Severity | Heading |
|---|---|---|
| CSCvn31572 | 3 | Jabber softphone not registering in Virtual Environment |
| CSCvn73837 | 3 | JVDI 12.1.X - Volume changes after unplugging the headset |
| CSCvo11181 | 3 | J4W:Network change breaks registration |
| CSCvo31711 | 3 | Saved ringer volume does not take effect |
| CSCvo33026 | 3 | Jabber 12.5 on VMWare VDI crashing while on calls |
| CSCvo41918 | 3 | Jabber VXME calling wrong API to distinguish between Citrix published desktop and published app |
| CSCvo51948 | 3 | Jabber for Windows has incorrect verification process for VXME mode |
| CSCvo61811 | 3 | Jabber soft phone would not register after being idle for some time |