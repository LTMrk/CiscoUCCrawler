---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-14-2-jvdi-b-jvdi-release-notes-142-jvdi-m-limit-and-restrict-142-html-40c3a96839
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/14_2/jvdi_b_jvdi-release-notes-142/jvdi_m_limit-and-restrict-142.html
retrieved_at: 2026-08-25T23:18:38.233507+00:00
---

Release Notes for Cisco Jabber Softphone for VDI Release 14.2

# Release Notes for Cisco Jabber Softphone for VDI Release 14.2

Updated: October 12, 2023

Chapter: Limitations and restrictions

## Chapter: Limitations and restrictions

# Limitations and restrictions

## General Limitations and Restrictions

### Accessory Call Control

Accessory call control (adjust call volume, answer or end phone calls, and mute audio) is supported for compatible headsets.
                                 Some other headsets provide basic functionality, but the accessory call control features do not work with Cisco Jabber Softphone for VDI . For a complete list of compatible headsets and other accessories, see https://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

### Adjust Settings for Jabra Bluetooth Devices

Most Jabra Bluetooth devices introduce a short delay in bringing up the audio path (about 1 to 3 seconds). For supported Jabra
                                 Bluetooth devices, you can eliminate the delay by changing the device settings in Jabra Direct. For more information, visit
                                 the Jabra website.

#### Before you begin

Jabra Direct  must be installed.

Step 1

Open Jabra Direct.

Step 2

Click the Jabra device for which you want to modify the settings.

Step 3

Click Settings .

Step 4

Click to expand Softphone (PC) .

Step 5

From the Preferred softphone list, select Cisco Jabber .

Step 6

Set Open phone line to On.

Step 7

Set PC audio to Off.

Step 8

Click Apply .

### BFCP Share and Citrix Workspace App Protection

App Protection in supported releases of Citrix Workspace conflicts with BFCP shares in Cisco Jabber Softphone for VDI. For
                                 users to use BFCP share, App Protection must be disabled in Citrix Workspace.

### Call Preservation Mode

Cisco Jabber Softphone for VDI does not support Call Preservation, also known as "survivability" . If a network interruption occurs and Cisoc Jabber goes into Call Preservation mode, the calls drop for VDI users.

### Camera Hot Swap

Cisco Jabber Softphone for VDI establishes video quality at the start of a call. If you start a call with one of the supported HD cameras, and then switch
                                 to a standard-definition camera, video quality is affected. We recommend that you switch cameras between calls.

### Changes to Your Connection Method

You must always install Citrix or VMware before you install the JVDI Client. Therefore, you must reinstall the JVDI Client
                                 after one of the following changes:

Linux platforms

Upgrading Citrix or VMware

Switching from Citrix to VMware, or from VMware to Citrix

Windows and Mac platforms

Switching from Citrix to VMware, or from VMware to Citrix

### Cisco Jabber Features

Cisco Jabber Softphone for VDI Release 14.0 supports all Cisco Jabber for Windows
                                 Release 14.0 features, except the following:

Agent Greeting

Application Sharing

Audio device selection from the Hub Menu

Cisco Headset Firmware Upgrade Notification (Linux)

Cisco Sunkist 730 Headset Presence LED Syncs with Jabber
                                       (Linux)

Cisco Unified Survivable Remote Site Telephony (SRST)

Custom Contacts for Team Messaging
                                       Mode

Far End Camera Control (FECC)

Federal Information Processing Standard, Publication 140-2 (FIPS 140-2) and
                                       Information Assurance (IA) Compliance

H.264 High Profile Support

IM-only Screen Sharing

Improved Video Resolution

Cisco Jabber to Jabber Call

Cisco Jabber desk phone video (display of video on the desktop when the thin client is
                                       connected to the user's desk phone)

Kerberos and Common Access Card (CAC) with Single Sign On (SSO)

Cisco Jabber Softphone for VDI does not support CAC, and supports Kerberos only with SSO.

MRA Registration Failover

PreferP2PDesktopShare (configuration parameter to prioritize person to
                                       person screen sharing over video sharing in the Cisco Jabber configuration file)

Supervisor Barge

Wireless Screen Sharing

Whisper Announcements

XMPP Federation for Team Messaging Mode

### Cisco Jabber Installed on the Thin Client

We recommend that you do not install Cisco Jabber on the thin clients. If you do install Cisco Jabber on the thin clients, ensure that users sign out of Cisco Jabber before they sign in to their hosted virtual desktops. Cisco Jabber Softphone for VDI works only with Cisco Jabber installed on the HVD.

### Cisco Media Services Interface and Dual VLAN

Cisco Media Services Interface (MSI) and Dual VLAN are not supported for this release.

### Echo Cancellation

Echo cancellation is enabled only for audio calls.

### GPU Passthrough

Cisco Jabber Softphone for VDI depends on the display adapter name to determine whether Cisco Jabber operates in VDI-optimized mode. Cisco Jabber Softphone for VDI supports only display adapter names that include the substring "Citrix" or "VMWare".

After you set up GPU passthrough to give the HVD direct access to the display adapter, the display adapter name doesn't include
                                 the required substring. Therefore, Cisco Jabber Softphone for VDI mistakenly identifies the deployment as non-VDI.

You can work around this issue by adding the following to the Windows registry on the HVDs:

[HKEY_CURRENT_USER\Software\Cisco Systems, Inc.\JVDI] "isVDIEnabled"="true"

After you edit the registry, restart Cisco Jabber .

### HDX RealTime Webcam with Citrix

Cisco Jabber Softphone for VDI does not support HDX Plug-n-Play for cameras. Citrix recommends using HDX Webcam for camera interactions.

### Jabra Firmware

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information,
                                 visit the Jabra website.

### Jabber VDI Fallback Mode

Jabber VDI fallback mode offers short-term support for basic audio and video calls
                                 when VDI can't establish the virtual channel. Fallback mode supports standard calls
                                 and call recording. The full feature set isn't supported. For example, you can't
                                 forward a call that you're recording in fallback mode. Call quality is lower because
                                 of the server or network issues that cause the switch to fallback mode.

### Microphone Levels in Fallback Mode

Microphone levels are reset to 54% in VDI fallback mode when a user unplus and replugs a headset. This is a Citrix audio device
                                 mapping issue.

### Self View in Fallback Mode

In VDI fallback mode, the self view may not appear with Citrix HDX Web Camera, or VMware Virtual Webcam,

### Multiple Hosted Virtual Desktop Sessions

Cisco Jabber Softphone for VDI may not work as expected with multiple HVD sessions. The phone service connection should be unaffected but the video or self-view
                                 position might be incorrect when in a call or when previewing the video.

### Remote Display Protocol Support

Cisco Jabber Softphone for VDI supports only PC-over-IP (PCoIP) for VMware and ICA for Citrix.

### Remote Problem Report Tool (PRT)

The remote PRT feature won't work when the virtual channel connection is broken.

### Single Session Hosted Virtual Desktop (Windows Server 2019)

This version of Cisco Jabber Softphone for VDI doesn't support Windows 2019 as a single session hosted virtual
                                 desktop (HVD). If Windows 2019 is a single-session desktop in the
                                 VMware VDI environment, use the following workaround when Jabber for
                                 Windows isn't running in VDI mode.

Add the following to the Windows registries on the HVD:

```
[HKEY_CURRENT_USER\Software\Cisco Systems, Inc.\JVDI] "isVDIEnabled"="true"
```

After you edit the registry, restart Cisco Jabber.

### SIP Profiles

When you create a Cisco Unified Client Services Framework (CSF) device, you specify a SIP Profile for the device. SIP profiles provide specific SIP information for the phone, such as registration and keepalive timers, media
                                 ports, and Do Not Disturb control.

You can use Certificate Authority Proxy Function (CAPF) to manage the phone certificates for the hosted desktop versions of
                                 Jabber for Windows. When you change the CAPF Certificate Operation from No Pending Operation to Install/Upgrade , the users must reset Jabber for Windows and sign in to complete the certificate installation.

Important

Do not choose Authentication Mode By Null string when using the Certificate Authority Proxy Function (CAPF).

This setting breaks Cisco Jabber Softphone for VDI registration to Cisco Unified Communications Manager.

### USB camera or audio device redirection not supported with VMware Horizon client

USB camera or audio device redirection is not supported with VMware Horizon client.

### Video Codec Performance

Software decoding relies heavily on the CPU. Estimated CPU usage for the Cisco JVDI Client with lower-end CPUs is as follows:

1.5Ghz, Dual core CPU—65% (55 to 75%)

1.5Ghz, Quad core CPU—35% (25 to 45%)

Use of a camera with a built-in hardware decoder reduces the load on the CPU.

### VMWare Support

Cisco Jabber Softphone for VDI does not support Display Scaling mode. Users should check their VMware Options menu and ensure
                                 that Allow Display Scaling is not checked.

Cisco Jabber Softphone for VDI supports full-screen and windowed display for Windows and Linux thin clients in both VMWare
                                 and Citrix VDI environments.

### Voice Message Recording

In a Windows Server 2019 environment, Cisco Jabber Softphone for VDI may not be able to record a voice message. To fix this issue, check the microphone privacy settings on the HVD and allow
                                 apps to access the microphone if needed.

## Linux Limitations and Restrictions

### Duplicate Audio Devices

Cisco Jabber Softphone for VDI releases 12.9(3) and later show all of the available
                                 internal speakers and microphones. The interface may duplicated entries for input
                                 and output sources because of how devices are managed in the VDI environment.

### Presence Enhancement

The presence enhancement does not work on HP Thin Pro.

### Unsupported Citrix Workspace app feature

As of Citrix Workspace App for Linux 2112, you can enable a Citrix parameter, AudioRedirectionV4 , to display all available local audio devices in a Citrix session with their names.

JVDI doesn't support this Citrix feature.

### Ubuntu on Wayland

JVDI client does not work under Wayland display server. JVDI currently supports Xorg / X11.

## MacOS Limitations and Restrictions

### Multiple Monitors

For MacOS, Cisco Jabber Softphone for VDI doesn't support multiple physical monitors
                                 under full screen mode. You must uncheck the "use
                                 all displays in full screen" setting in Citrix
                                 Workspace. This configuration supports full screen
                                 mode on the current display.

## Windows Limitations and Restrictions

### Multiple Monitors

For Windows, Cisco Jabber Softphone for VDI for VDI does not support mutiple virtual monitors ("the monitor layout" function) in the Citrix Workspace App.

| Step 1 | Open Jabra Direct. |
|---|---|
| Step 2 | Click the Jabra device for which you want to modify the settings. |
| Step 3 | Click Settings . |
| Step 4 | Click to expand Softphone (PC) . |
| Step 5 | From the Preferred softphone list, select Cisco Jabber . |
| Step 6 | Set Open phone line to On. |
| Step 7 | Set PC audio to Off. |
| Step 8 | Click Apply . |

| Important | Do not choose Authentication Mode By Null string when using the Certificate Authority Proxy Function (CAPF). This setting breaks Cisco Jabber Softphone for VDI registration to Cisco Unified Communications Manager. |
|---|---|