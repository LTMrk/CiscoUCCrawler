---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-8-rns-hp-ubuntu-jvdi-b-release-notes-jvdi-hp-ubuntu-12-8-html-0498311e9c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_8/rns/hp-ubuntu/jvdi_b_release-notes-jvdi-hp-ubuntu-12-8.html
retrieved_at: 2026-08-22T00:41:58.331477+00:00
---

Release Notes for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.8

# Release Notes for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.8

### Download Options

Updated: March 27, 2020

First Published: January 21, 2020

Last Updated: October 12, 2022

# Build Number for 12.8

Version

Build Number

Cisco Jabber Softphone for VDI Release 12.8

Cisco JVDI Agent

Cisco JVDI Client

12.8.0.301886

Cisco Jabber Softphone for VDI Release 12.8(1)

Cisco JVDI Agent

Cisco JVDI Client

12.8.1.302494

## What's New in Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.8(1)

This release includes bug fixes and minor enhancements. For more information, see Resolved Caveats for Release 12.8(1) .

## What's New in Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.8

### Cisco Jabber Support

This release supports the following new Cisco Jabber for Windows Release 12.8 features:

Audio Device Priority

Call Park

Cisco Headset Support

Global Shortcut Key for Conversation Window

Microsoft Office 2019 Support

Multiline Per Line Ringtones

With N-1 or N-2 support, the lower version determines the available feature set.

### Deprecated Parameter

We added the HeadsetPreference parameter to specify how Cisco Jabber handles new audio devices.

The new parameter replaces the now deprecated HeadsetPreferenceOnVDI parameter.

By default, when you connect a new audio device, Cisco Jabber adds it to the top of the priority list. The default behavior is a problem in some hot-desking environments. When a user
                     moves their thin client and headset, the embedded microphone becomes the preferred device.

Modern meeting rooms are often equipped with a large wall mounted monitor with HDMI, which handles both audio and video. When
                     a Cisco Jabber user connects to a monitor using HDMI, by default the monitor becomes the preferred device.

You can set this parameter to ensure that the user's headset remains the preferred device. Users can override this setting
                     in their Audio preferences. For more information about the new parameter, see Parameters Reference Guide for Cisco Jabber Release 12.8 .

### Mute Notification Sounds During Calls or Meetings

Users in VDI deployments can now choose to mute notification sounds during their calls or meetings.

### Version Support Strategy

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the JVDI Client version can be the
                     same, or up to two releases earlier (N-2 support). For example, the following version combinations are supported:

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and Cisco JVDI Client Release 12.8

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and Cisco JVDI Client Release 12.7

Cisco Jabber for Windows Release 12.8, Cisco JVDI Agent Release 12.8, and Cisco JVDI Client Release 12.6

### VDI Fallback Mode

Sometimes the Cisco JVDI Agent and the Cisco JVDI Client can't communicate. This issue occurs because of a network problem with the virtual channel, or because of a problem with
                     the Cisco Jabber Softphone for VDI installation. If the JVDI Agent and the JVDI Client can't communicate, Cisco Jabber can't operate in VDI-optimized mode. For more information about troubleshooting, see Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.8 .

This release introduces VDI Fallback mode, and a new parameter to enable this mode. Cisco Jabber Softphone for VDI checks the virtual channel every 10 seconds, to ensure that the JVDI Agent and the JVDI Client can communicate. If communication
                     is down, for two consecutive checks, Cisco Jabber Softphone for VDI switches Cisco Jabber to VDI Fallback mode. For more information about the new EnableVDIFallback parameter, see Parameters Reference Guide for Cisco Jabber Release 12.8 .

In VDI Fallback mode, users can make and receive calls, with audio traveling over the ICA channel. The connection status for Cisco Jabber changes from Softphone with VDI , to Softphone . Users can receive video; the ability to send video depends on the capabilities of your Citrix or VMware version. Audio and
                     video quality depend on network conditions, and the capabilities of your Citrix or VMware version. When Cisco Jabber operates in VDI Fallback mode, users see a notification message at the start of each call.

When Cisco Jabber Softphone for VDI detects communication between the JVDI Agent and the JVDI Client, it automatically switches Cisco Jabber back to VDI-optimized mode.

Cisco Jabber Softphone for VDI switches modes only between calls.

## General Requirements

General requirements apply to all Cisco Jabber Softphone for VDI platforms.

Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment.

### Accessories

For a complete listing of recommended audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware.

### Cisco Jabber for Windows

Cisco Jabber for Windows 12.8 running on the hosted virtual desktop (HVD).

For complete information about virtual environment compatibility, see the Cisco Jabber documentation for your release.

### Cisco Unified Communications Manager

Recommended: CUCM Release 11.5(1)SU3 or later

Minimum: CUCM Release 10.5

### Cisco Expressway for Mobile and Remote Access (MRA)

Recommended: Expressway X12.5

Minimum: Expressway X8.11.4

### Connection Broker—Installed on the Hosted Virtual Desktops

Citrix Virtual Apps and Desktops (formerly XenApp and XenDesktop) versions 7.x and later (latest LTSR 1912), and 7.15 CU5
                           LTSR

Shared Desktop is supported only in full-screen mode. Published Application is supported in full-screen mode for Cisco Jabber
                           Softphone for VDI—Windows.

VMware Horizon versions 6.x to 7.11.

A connection broker is software that creates connections to hosted virtual desktops. A connection broker performs a number
                     of tasks including the following:

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

### Operating Systems—Installed on the Hosted Virtual Desktops

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

## Requirements—HP Thin Pro

### Citrix Workspace app or VMware Horizon Client—Installed on the Thin Clients

The HP Thin Pro image includes the required Citrix and VMware versions.

The Citrix Workspace app or VMware Horizon Client provides a user interface for the corresponding connection broker.

Published application mode and the scale to fit option are not supported.

### HP Thin Pro Thin Clients—Hardware

We recommend the following client hardware, which was tested with HP Thin Pro 6.2:

HP t520

HP t530

HP t620

HP t630

HP t730

HP mt21

We recommend the following client hardware, which was tested with HP Thin Pro 7.1 SP3.3:

HP t430

HP t520

HP t530

HP t630

HP t730

HP mt21

### HP ThinPro Platform Image

32–bit: HP ThinPro 6.2

64–bit: HP ThinPro 7.1 SP3.3 and 7.x versions

Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment.

## Requirements—Ubuntu

Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment.

### Ubuntu Desktop Image

Ubuntu 14.04 32b LTS (i386)

Ubuntu 16.04 64b LTS (AMD64)

Ubuntu 18.04 64b LTS (AMD64)

Ubuntu 20.04 64b LTS (AMD64)

The supported versions do not include Ubuntu Minimal.

### Ubuntu Thin Clients—Hardware

The minimum hardware requirements for thin clients are as follows:

Installed RAM 2 GB

Free Physical Memory 1 GB

Free Disk Space 256 MB

CPU: AMD G-T56N 1.65Ghz, or Intel Core2Duo T7500 2.2 GHz

USB 2.0 for USB camera and audio devices

### Citrix Workspace app or VMware Horizon Client—Installed on the Thin Clients

Citrix Receiver 13.0 and later

Citrix Workspace app 1808 and later

VMware Horizon View Client versions 4.x, 5.x, and 8.x

The Citrix Workspace app or VMware Horizon Client provides a user interface for the corresponding connection broker.

Published application mode and the scale to fit option are not supported.

## Limitations and Restrictions

### BFCP Share and Citrix Workspace App Protection

App Protection in supported releases of Citrix Workspace conflicts with BFCP shares in Cisco Jabber Softphone for VDI. For
                        users to use BFCP share, App Protection must be disabled in Citrix Workspace.

### Accessory Call Control

Accessory call control (adjust call volume, answer or end phone calls, and mute audio) is supported for compatible headsets.
                        Some other headsets provide basic functionality, but the accessory call control features do not work with Cisco Jabber Softphone for VDI . For a complete list of compatible headsets and other accessories, see https://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

### Call Preservation Mode

Cisco Jabber Softphone for VDI does not support Call Preservation, also known as "survivability" . If a network interruption occurs and Cisoc Jabber goes into Call Preservation mode, the calls drop for VDI users.

### Cisco Media Services Interface and Dual VLAN

Cisco Media Services Interface (MSI) and Dual VLAN are not supported for this release.

### GPU Passthrough

Cisco Jabber Softphone for VDI depends on the display adapter name to determine whether Cisco Jabber operates in VDI-optimized mode. Cisco Jabber Softphone for VDI supports only display adapter names that include the substring "Citrix" or "VMWare".

After you set up GPU passthrough to give the HVD direct access to the display adapter, the display adapter name doesn't include
                        the required substring. Therefore, Cisco Jabber Softphone for VDI mistakenly identifies the deployment as non-VDI.

You can work around this issue by adding the following to the Windows registry on the HVDs:

[HKEY_CURRENT_USER\Software\Cisco Systems, Inc.\JVDI] "isVDIEnabled"="true"

After you edit the registry, restart Cisco Jabber .

### HDX RealTime Webcam with Citrix

Cisco Jabber Softphone for VDI does not support HDX Plug-n-Play for cameras. Citrix recommends using HDX Webcam for camera interactions.

### Cisco Jabber Features

Cisco Jabber Softphone for VDI Release 12.8 supports all Cisco Jabber for Windows Release 12.8 features, except the following:

Application Sharing

Audio device selection from the Hub Menu

Cisco Unified Survivable Remote Site Telephony (SRST)

Custom Contacts for Team Messaging Mode

Far End Camera Control (FECC)

Federal Information Processing Standard, Publication 140-2 (FIPS 140-2) and Information Assurance (IA) Compliance

H.264 High Profile Support

IM-only Screen Sharing

Improved Video Resolution

Cisco Jabber to Jabber Call

Cisco Jabber desk phone video (display of video on the desktop when the thin client is connected to the user's desk phone)

Kerberos and Common Access Card (CAC) with Single Sign On (SSO)

Cisco Jabber Softphone for VDI does not support CAC, and supports Kerberos only with SSO.

PreferP2PDesktopShare (configuration parameter to prioritize person to person screen sharing over video sharing in the Cisco Jabber configuration file)

Wireless Screen Sharing

XMPP Federation for Team Messaging Mode

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

### Open Caveats in Release 12.8(1)

There are no open caveats (bugs) for this release.

### Resolved Caveats for Release 12.8(1)

The following table lists caveats (bugs) that are fixed for this release.

Caveat ID Number

Severity

Description

CSCvs56982

3

JVDI 12.7 service delays

CSCvs64535

3

Jabber not applying Application Dial Rules intermittently

CSCvs77883

3

JVDI 12.7.1 use wrong speaker to play ringback tone for the first outgoing call intermittently

CSCvs87113

3

Jabber 12.7.1 VDI: Artefacts in Outlook GUI slow to refresh

CSCvs98123

3

JVDI Client log collection failed because the collection timed-out

CSCvt15602

3

vxc does`t startup due to missing some of dependent dlls in Windows OS

CSCvr15121

4

Jabber HVD is not able to verify Exp-E certificate

### Open Caveats in Release 12.8

Caveat ID Number

Severity

Description

CSCvs64535

3

Jabber not applying Application Dial Rules intermittently

CSCvs49186

6

Jabber 12.7 while using HVD via JVDI, Remove from Conference Feature Unavailable

### Resolved Caveats in Release 12.8

Caveat ID Number

Severity

Description

CSCvr42142

2

On JVDI client 12.6 phone services will not register if ServicesDomain is enabled on the bootstrap

CSCvr46635

2

JVDI Client Windows 7 Call Controls not visible in a Video Call

CSCvs60963

2

Jabber VDI Cannot communicate with Client

CSCvr73949

3

[VMWare]JVDI softphone not working

CSCvs28536

3

VDI client is not reachable error notification on JVDI version 12.7

CSCvs44378

3

The handles of JabberCisco.exe increases fast due to openprocess leak

CSCvs50906

3

12.7 JVDI on eLux - call drops when minimizing J4W window

| Version | Build Number |
|---|---|
| Cisco Jabber Softphone for VDI Release 12.8 Cisco JVDI Agent Cisco JVDI Client | 12.8.0.301886 |
| Cisco Jabber Softphone for VDI Release 12.8(1) Cisco JVDI Agent Cisco JVDI Client | 12.8.1.302494 |

| Attention | With N-1 or N-2 support, the lower version determines the available feature set. |
|---|---|

| Note | The new parameter replaces the now deprecated HeadsetPreferenceOnVDI parameter. |
|---|---|

| Note | Cisco Jabber Softphone for VDI switches modes only between calls. |
|---|---|

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment. |
|---|---|

| Port Range | Description |
|---|---|
| 16384–32767 | UDP Inbound and outbound traffic for RTP (audio and video streams) You can configure the Cisco Unified Communications Manager to reduce this port range. Change the Start/Stop Media Port setting in the SIP Profile, which is associated with the CSF device. |

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment. |
|---|---|

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                 can result in a nonfunctional deployment. |
|---|---|

| Note | The supported versions do not include Ubuntu Minimal. |
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

| Caveat ID Number | Severity | Description |
|---|---|---|
| CSCvs56982 | 3 | JVDI 12.7 service delays |
| CSCvs64535 | 3 | Jabber not applying Application Dial Rules intermittently |
| CSCvs77883 | 3 | JVDI 12.7.1 use wrong speaker to play ringback tone for the first outgoing call intermittently |
| CSCvs87113 | 3 | Jabber 12.7.1 VDI: Artefacts in Outlook GUI slow to refresh |
| CSCvs98123 | 3 | JVDI Client log collection failed because the collection timed-out |
| CSCvt15602 | 3 | vxc does`t startup due to missing some of dependent dlls in Windows OS |
| CSCvr15121 | 4 | Jabber HVD is not able to verify Exp-E certificate |

| Caveat ID Number | Severity | Description |
|---|---|---|
| CSCvs64535 | 3 | Jabber not applying Application Dial Rules intermittently |
| CSCvs49186 | 6 | Jabber 12.7 while using HVD via JVDI, Remove from Conference Feature Unavailable |

| Caveat ID Number | Severity | Description |
|---|---|---|
| CSCvr42142 | 2 | On JVDI client 12.6 phone services will not register if ServicesDomain is enabled on the bootstrap |
| CSCvr46635 | 2 | JVDI Client Windows 7 Call Controls not visible in a Video Call |
| CSCvs60963 | 2 | Jabber VDI Cannot communicate with Client |
| CSCvr73949 | 3 | [VMWare]JVDI softphone not working |
| CSCvs28536 | 3 | VDI client is not reachable error notification on JVDI version 12.7 |
| CSCvs44378 | 3 | The handles of JabberCisco.exe increases fast due to openprocess leak |
| CSCvs50906 | 3 | 12.7 JVDI on eLux - call drops when minimizing J4W window |