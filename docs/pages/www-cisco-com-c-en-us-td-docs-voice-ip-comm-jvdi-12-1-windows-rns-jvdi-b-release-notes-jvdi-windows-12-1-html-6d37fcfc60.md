---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-1-windows-rns-jvdi-b-release-notes-jvdi-windows-12-1-html-6d37fcfc60
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_1/windows/rns/jvdi_b_release-notes-jvdi-windows-12-1.html
retrieved_at: 2026-08-22T00:42:15.130343+00:00
---

Release Notes for Cisco Jabber Softphone for VDI—Windows Release 12.1

# Release Notes for Cisco Jabber Softphone for VDI—Windows Release 12.1

### Download Options

Updated: January 24, 2020

First Published: July 12, 2018

Last Updated: January 24, 2020

# Release and General Information

These release notes describe new features, requirements, restrictions, and caveats for Cisco Jabber Softphone for VDI for Windows Release 12.1. These release notes are updated for every maintenance release but not for patches or hot fixes.

Before you install Cisco Jabber Softphone for VDI , we recommend that you review this document for information about issues that may affect your system.

## Introduction to Cisco Jabber Softphone for VDI

In this release notes document, the term thin client refers to any supported device (including reused PCs) used to access the hosted virtual desktops (HVD).

Cisco Jabber Softphone for VDI extends the Cisco collaboration experience to virtual deployments. With supported versions of Cisco Jabber for Windows, users can send and receive phone calls on their hosted virtual desktops (HVD). The software routes all audio
                     and video streams directly from one thin client to another, or to a phone, without going through the HVD.

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

For more information about Cisco Jabber , see the Release Notes for Cisco Jabber for Windows for your release:

https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html

### Languages

The Cisco JVDI Agent and Cisco JVDI Client installation programs, and Device Selector are localized in the following languages:

Arabic

Bulgarian

Catalan

Chinese Simplified

Chinese Traditional

Croatian

Czech

Danish

Dutch

English(US)

Finnish

French

German

Greek

Hebrew

Hungarian

Italian

Japanese

Korean

Norwegian

Polish

Portuguese Brazil

Portuguese Portugal

Romanian

Russian

Serbian

Slovak

Slovenian

Spanish

Swedish

Thai

Turkish

### Cisco Jabber Softphone for VDI Copyright

Copyright © 2018–2019 Cisco or its affiliated entities. All Rights Reserved.

## Finding Documentation

Provide employees with the following URL: https://collaborationhelp.cisco.com/article/en-us/plvruj .

You can also add the link to the Citrix landing page or to the VMware Horizon View prelogin banner.

To find documentation for your release, visit https://www.cisco.com/c/en/us/support/collaboration-endpoints/virtualization-experience-media-engine/tsd-products-support-series-home.html .

## Documentation Updates

The following table provides information about changes to this document.

Date

Change

January 16, 2019

Added Citrix XenApp Support .

## New in This Release for Cisco Jabber Softphone for VDI

Cisco Jabber Softphone for VDI for Windows Release 12.1 adds support for the following programs and features.

### Cisco Jabber Support

This release supports Cisco Jabber for Windows Release 12.1.

Cisco Jabber Softphone for VDI supports all Cisco Jabber for Windows  features, except the following:

Audio device selection from the Hub Menu

Binary Floor Control Protocol (BFCP) Desktop Share

Cisco Unified Survivable Remote Site Telephony (SRST)

Collaboration Edge

Device Selection menu on the Call Conversation window

Direct Pickup and Group Pickup

Far End Camera Control (FECC)

Federal Information Processing Standard, Publication 140-2 (FIPS 140-2) and Information Assurance (IA) Compliance

Jabber to Jabber Call

Jabber desk phone video (display of video on the desktop when the thin client is connected to the user's desk phone)

Kerberos and Common Access Card (CAC) with Single Sign On (SSO)

Multiline

Only the first line of a multiline account is available. If a second call comes in, while the first line is in use, the second
                              line rings, but no incoming call notification appears.

PreferP2PDesktopShare (configuration parameter to prioritize person to person screen sharing over video sharing in the Jabber
                              configuration file)

## System Requirements

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

Microsoft Windows 7 32 bit

Microsoft Windows 7 64 bit

Microsoft Windows 8 32 bit

Microsoft Windows 8 64 bit

Microsoft Windows 8.1 32 bit

Microsoft Windows 8.1 64 bit

Microsoft Windows 10 32 bit

Microsoft Windows 10 64 bit

Windows Thin PC 32 bit

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

Windows Embedded Standard 7 32 bit

Windows Embedded Standard 7 64 bit

Windows Embedded Standard 8 64 bit

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

Connection broker for the hosted virtual desktop

Citrix XenDesktop 7.5 and later 7.x versions

Citrix XenApp 7.5 and later 7.x versions—Published Desktop and Published Application

Published Application is not supported in full-screen mode.

VMware Horizon 6.0 (with View)—Published desktops only

VMware Horizon 6 version 6.1.0—Published desktops only

VMware Horizon 6 version 6.2.0—Published desktops only

VMware Horizon 7 version 7.x—Published desktops only

Citrix Receiver or

VMware Horizon Client

(Installed on the thin client)

Citrix Receiver (ICA) for Windows 4.4.1000 and later 4.x versions

VMware Horizon Client for Windows 4.1.0, 4 and later 4.x version. (Versions 4.3 and 4.4 are not supported.)

To enable JVDI support with versions 4.5 and later, check 32-bit Core Remote Experience on this 64-bit machine during the VMWare Horizon installation (new install or upgrade). For more information about this setting, see the VMWare
                                       Horizon documentation.

Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client.

If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client.

Cisco Unified Communications client on the hosted virtual desktop:

Cisco Jabber for Windows or Cisco UC Integration™ for Microsoft Lync .

Cisco Jabber for Windows 12.1 running on the hosted virtual desktop (HVD).

Cisco Jabber Softphone for VDI is compatible with all future 12.1(x) Cisco Jabber for Windows versions.

For complete information about virtual environment compatibility, see the documentation for Cisco Jabber or Cisco UC Integration™ for Microsoft Lync .

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

The Citrix Receiver or VMware Horizon Client provides a user interface for the corresponding connection broker.

(PCoIP only)

## Installation and Upgrade Notes

For assistance obtaining the required downloads from HP, contact HP support.

The following upgrade paths are supported:

Cisco Virtualization Experience Media Edition for HP Thin Pro and Ubuntu Release 11.5 to Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu Release 12.1.

Cisco Virtualization Experience Media Edition for HP Thin Pro and Ubuntu Release 11.7 to Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu Release 12.1.

Cisco Virtualization Experience Media Edition for HP Thin Pro and Ubuntu Release 11.8 to Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu Release 12.1.

Cisco Virtualization Experience Media Edition for HP Thin Pro and Ubuntu Release 11.9 to Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu Release 12.1.

From Cisco Jabber Softphone for VDI —HP Thin Pro and Ubuntu Release 12.0 to Cisco Jabber Softphone for VDI —Thin Pro and Ubuntu Release 12.1

## Important Notes

### Cisco Audio Session Tunnel

Cisco Audio Session Tunnel (CAST) connection to the HVD is not supported.

### Cisco Jabber Installed on the Thin Client

We recommend that you do not install Cisco Jabber on the thin clients. If you do install Cisco Jabber on the thin clients, ensure that users sign out of Cisco Jabber before they sign in to their hosted virtual desktops. Cisco Jabber Softphone for VDI works only with Cisco Jabber installed on the HVD.

### Cisco Unified Communications Manager Failover

When a failover from one Cisco Unified Communications Manager to another occurs, Cisco Jabber for Windows retains phone functionality. However, with Cisco Jabber Softphone for VDI , phone functionality is lost. This issue occurs because CTI failover is not supported in the virtual environment.

### Cisco Expressway

Cisco Jabber Softphone for VDI does not support the use of Mobile Remote Access and Cisco Expressway.

### Citrix XenApp Support

Citrix XenApp Published Application is not supported in full-screen mode. You can disable full-screen mode in the Citrix Receiver
                        > Connection Center, on the thin client.

### Display Settings

For optimal video performance, use the recommended settings for Citrix or VMware.

With Citrix XenDesktop and VMware, only full-screen mode is supported on the Linux-based platforms:

Cisco Jabber Softphone for VDI —HP Thin Pro and Ubuntu

Cisco Jabber Softphone for VDI —Unicon eLux

Citrix XenApp Published Application is supported only on Cisco Jabber Softphone for VDI —Windows, in windows mode only.

#### Citrix

Cisco Jabber Softphone for VDI supports only the Preferences > Display > Best resolution (Recommended) display option.

#### VMware

Cisco Jabber Softphone for VDI —Windows Release 12. 8 (and later) supports the Display Scaling feature for VMware. For earlier versions, have users check
                        their VMware options to ensure that the Allow Display Scaling option is unchecked.

### Echo Cancellation

Echo cancellation is enabled only for audio calls.

### Remote Display Protocol Support

Cisco Jabber Softphone for VDI supports only the following protocols:

Citrix: ICA

VMware: PC-over-IP (PCoIP) and VMware Blast Extreme

### SIP Profiles

When you create a Cisco Unified Client Services Framework (CSF) device, you specify a SIP Profile for the device. SIP profiles provide specific SIP information for the phone, such as registration and keepalive timers, media
                        ports, and Do Not Disturb control.

If you choose Secure Phone Profile , do not specify the Certificate Authority Proxy Function (CAPF) authentication mode By Null string . Use of this setting, with Cisco Jabber Softphone for VDI , causes Cisco Jabber registration with Cisco Unified Communications Manager to fail.

### USB Camera Redirection Not Supported with VMware View

USB camera redirection is not supported with VMware View.

### HDX RealTime Webcam with Citrix

Cisco Jabber Softphone for VDI does not support HDX Plug-n-Play for cameras. Citrix recommends using HDX Webcam for camera interactions.

### Silent Monitoring and Call Recording

Cisco Jabber Softphone for VDI supports silent monitoring and call recording. To enable these audio path functions for a device, you configure Cisco Unified
                        Communications Manager. For step-by-step instructions, the Cisco Unified Communications Manager Features and Services Guide for your release.

Cisco Jabber does not provide any interface to start silent monitoring or call recording. Use the appropriate software to
                              silently monitor or record calls.

Cisco Jabber does not currently support monitoring notification tone or recording notification tone.

You can use silent monitoring and call recording functionality only. Cisco Jabber does not support other functionality such
                              as barging or whisper coaching.

You might need to download and apply a device package to enable monitoring and recording capabilities on the device, depending
                              on your version of Cisco Unified Communications Manager.

#### Determine Device Package Requirements

Navigate to and open the Phone Configuration window for the device, for which you want to enable monitoring and recording.

Locate the Built-in-Bridge field.

If the Built-in-Bridge field is not available, download and install a device package for the device.

### Accessories

#### Jabra Firmware

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                           visit: http://www.jabra.com .

#### Adjust Settings for Jabra Bluetooth Devices

Most Jabra Bluetooth devices introduce a short delay in bringing up the audio path (about 1 to 3 seconds). For supported Jabra
                           Bluetooth devices, you can eliminate the delay by changing the device settings in Jabra Direct. For more information, visit http://www.jabra.com .

Before you begin

##### Before you begin

Jabra Direct  must be installed.

Open Jabra Direct.

Click the Jabra device for which you want to modify the settings.

Click Settings .

Click to expand Softphone (PC) .

From the Preferred softphone list, select Cisco Jabber .

Set Open phone line to On.

Set PC audio to Off.

Click Apply .

#### Camera Hot Swap

Cisco Jabber Softphone for VDI establishes video quality at the start of a call. If you start a call with one of the supported HD cameras, and then switch
                           to a standard-definition camera, video quality is affected. We recommend that you switch cameras between calls.

## Caveats

### Search for Bugs

#### Bug Classification

Known defects, or bugs, have a severity level that indicates the priority of the defect. Development managers usually define
                        bug severity. Severity helps the product team focus on bug fixes for future releases and prioritize fixes.

This is the highest level for documentation bugs.

#### Search for Bugs

- Go to https://tools.cisco.com/bugsearch .

- Sign in with your Cisco.com user ID and password.

- Enter a bug ID or specify search parameters.

### Closed Caveats

There are no closed caveats for Cisco Jabber Softphone for VDI—Windows Release 12.1.

### Open Caveats

The following table lists the open bugs for this release.

Caveat ID

Severity

Description

CSCvj22005

3

Jabber answer button grayed out

CSCvj80899

3

Jabber softphone services doesn't register the first time in VXME environment intermittently

CSCvk02825

3

JVDI no remote video and mute audio not work

CSCvk25632

3

Jabber a split second of video from previous call is seen

CSCvk30137

3

JVDI Agent fail to launch on specific VMWare VDI

### Resolved Caveats

The following table lists bugs that are fixed in this release.

Caveat ID

Severity

Description

CSCvi38157

3

VXME causes Citrix crash

CSCvi74603

3

Jabber VXME loses configured audio devices

CSCvj55836

3

Duplicate devices seen in advanced audio options

CSCvk30206

3

VXME didn't work after thin client change network

| Arabic Bulgarian Catalan Chinese Simplified Chinese Traditional Croatian Czech Danish Dutch English(US) Finnish French German Greek Hebrew Hungarian | Italian Japanese Korean Norwegian Polish Portuguese Brazil Portuguese Portugal Romanian Russian Serbian Slovak Slovenian Spanish Swedish Thai Turkish |
|---|---|

| Date | Change |
|---|---|
| January 16, 2019 | Added Citrix XenApp Support . |

| Important | Each of the components listed in the following table must meet the requirements. Use of unsupported components can result
                                 in a nonfunctional deployment. Only the components, versions, and minimum hardware requirements listed in the table are supported. |
|---|---|

| Component | Requirements |
|---|---|
| Microsoft Windows-based thin client hardware | Installed RAM 2 GB Free Physical Memory 128 MB Free Disk Space 256 MB CPU Mobile AMD Sempron Processor 3600+, 2-GHz Intel Core 2 CPU, or T7400 2.16 GHz DirectX 11 compatible GPU USB 2.0 for USB camera and audio devices Note Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. | Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Microsoft Windows-based thin client OS | Microsoft Windows 7 32 bit Microsoft Windows 7 64 bit Microsoft Windows 8 32 bit Microsoft Windows 8 64 bit Microsoft Windows 8.1 32 bit Microsoft Windows 8.1 64 bit Microsoft Windows 10 32 bit Microsoft Windows 10 64 bit Windows Thin PC 32 bit |
| Windows Embedded Standard-based thin client hardware | Installed RAM 2 GB Free Physical Memory 128 MB Free Disk Space 256 MB CPU performance affects the maximum video resolution. With Windows Embedded Standard thin clients, the expected resolution
                                       depends on the CPU: Up to 720p with quad-core AMD GX-420CA SOC 2 GHz or similar Up to 240p with dual-core AMD G-T56N 1.65 GHz or similar Audio-only support with dual-core VIA Eden X2 U4200 1 GHz or similar CPU Note These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. DirectX 11 compatible GPU USB 2.0 for USB camera and audio devices Note Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. | Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. | Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Note | These hardware specifications are only guidelines for the expected resolutions. Other factors can affect video resolution. |
| Note | Cisco Jabber Softphone for VDI for Windows does not require the Microsoft .NET Framework or any Java modules. |
| Windows Embedded Standard-based thin client OS | Windows Embedded Standard 7 32 bit Windows Embedded Standard 7 64 bit Windows Embedded Standard 8 64 bit Windows 10 IoT Enterprise |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 32 bit Microsoft Windows 7 64 bit Microsoft Windows 8 32 bit Microsoft Windows 8 64 bit Microsoft Windows 8.1 32 bit Microsoft Windows 8.1 64 bit Microsoft Windows 10 32 bit Microsoft Windows 10 64 bit |
| Connection broker for the hosted virtual desktop 1 | Citrix XenDesktop 7.5 and later 7.x versions Citrix XenApp 7.5 and later 7.x versions—Published Desktop and Published Application Important Published Application is not supported in full-screen mode. VMware Horizon 6.0 (with View)—Published desktops only VMware Horizon 6 version 6.1.0—Published desktops only VMware Horizon 6 version 6.2.0—Published desktops only VMware Horizon 7 version 7.x—Published desktops only | Important | Published Application is not supported in full-screen mode. |
| Important | Published Application is not supported in full-screen mode. |
| Citrix Receiver or VMware Horizon Client 2 (Installed on the thin client) | Citrix Receiver (ICA) for Windows 4.4.1000 and later 4.x versions VMware Horizon Client for Windows 4.1.0, 4 and later 4.x version. (Versions 4.3 and 4.4 are not supported.) To enable JVDI support with versions 4.5 and later, check 32-bit Core Remote Experience on this 64-bit machine during the VMWare Horizon installation (new install or upgrade). For more information about this setting, see the VMWare
                                       Horizon documentation. Important Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. | Important | Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. |
| Important | Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. |
| Cisco Unified Communications client on the hosted virtual desktop: Cisco Jabber for Windows or Cisco UC Integration™ for Microsoft Lync . | Cisco Jabber for Windows 12.1 running on the hosted virtual desktop (HVD). Cisco Jabber Softphone for VDI is compatible with all future 12.1(x) Cisco Jabber for Windows versions. For complete information about virtual environment compatibility, see the documentation for Cisco Jabber or Cisco UC Integration™ for Microsoft Lync . |
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

| Important | Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client. If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client. |
|---|---|

| Important | Ensure that all Jabra devices are running the latest firmware. You can use the Jabra Direct to update the firmware. For more
                                          information visit: http://www.jabra.com . |
|---|---|

| Note | For assistance obtaining the required downloads from HP, contact HP support. |
|---|---|

| Important | If you choose Secure Phone Profile , do not specify the Certificate Authority Proxy Function (CAPF) authentication mode By Null string . Use of this setting, with Cisco Jabber Softphone for VDI , causes Cisco Jabber registration with Cisco Unified Communications Manager to fail. |
|---|---|

| Step 1 | Navigate to and open the Phone Configuration window for the device, for which you want to enable monitoring and recording. |
|---|---|
| Step 2 | Locate the Built-in-Bridge field. If the Built-in-Bridge field is not available, download and install a device package for the device. |

| Step 1 | Open Jabra Direct. |
|---|---|
| Step 2 | Click the Jabra device for which you want to modify the settings. |
| Step 3 | Click Settings . |
| Step 4 | Click to expand Softphone (PC) . |
| Step 5 | From the Preferred softphone list, select Cisco Jabber . |
| Step 6 | Set Open phone line to On. |
| Step 7 | Set PC audio to Off. |
| Step 8 | Click Apply . |

| Severity level | Description |
|---|---|
| 1 | Catastrophic | Reasonably common circumstances cause the entire system to fail, or a major subsystem to stop working, or other devices on
                                    the network  to be disrupted. No workarounds exist. |
| 2 | Severe | Important functions are unusable and workarounds do not exist. Other functions and the rest of the network is operating normally. |
| 3 | Moderate | Failures occur in unusual circumstances, or minor features do not work at all, or other failures occur but low-impact workarounds
                                    exist. This is the highest level for documentation bugs. |
| 4 | Minor | Failures occur under very unusual circumstances, but operation essentially recovers without intervention. Users do not need
                                    to install any workarounds and performance impact is tolerable. |
| 5 | Cosmetic | Defects do not cause any detrimental effect on system functionality. |
| 6 | Enhancement | Requests for new functionality or feature improvements. |

| Caveat ID | Severity | Description |
|---|---|---|
| CSCvj22005 | 3 | Jabber answer button grayed out |
| CSCvj80899 | 3 | Jabber softphone services doesn't register the first time in VXME environment intermittently |
| CSCvk02825 | 3 | JVDI no remote video and mute audio not work |
| CSCvk25632 | 3 | Jabber a split second of video from previous call is seen |
| CSCvk30137 | 3 | JVDI Agent fail to launch on specific VMWare VDI |

| Caveat ID | Severity | Description |
|---|---|---|
| CSCvi38157 | 3 | VXME causes Citrix crash |
| CSCvi74603 | 3 | Jabber VXME loses configured audio devices |
| CSCvj55836 | 3 | Duplicate devices seen in advanced audio options |
| CSCvk30206 | 3 | VXME didn't work after thin client change network |