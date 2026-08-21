---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-9-rns-jvdi-b-release-notes-jvdi-129-jvdi-b-release-notes-jvdi-129-ch-390efb5ebc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_9/rns/jvdi_b_release-notes-jvdi-129/jvdi_b_release-notes-jvdi-129_chapter_00.html
retrieved_at: 2026-08-21T12:36:40.972811+00:00
---

Release Notes for Cisco Jabber Softphone for VDI Release 12.9

# Release Notes for Cisco Jabber Softphone for VDI Release 12.9

Updated: July 8, 2020

Chapter: What's New in Release 12.9

## Chapter: What's New in Release 12.9

# What's New in Release 12.9

## Build Number

Version

Build Number

Cisco Jabber Softphone for VDI Release 12.9(3)

Cisco JVDI Agent

Cisco JVDI Client

12.9.3.305062

Cisco Jabber Softphone for VDI Release 12.9(2)

Cisco JVDI Agent

Cisco JVDI Client

12.9.2.304552

Cisco Jabber Softphone for VDI Release 12.9(1)

Cisco JVDI Agent

Cisco JVDI Client

12.9.1.304247

Cisco Jabber Softphone for VDI Release 12.9

Cisco JVDI Agent

Cisco JVDI Client

12.9.0.303399

## New and Updated Features

### 12.9(3)

#### New Supported Platforms

Cisco Jabber Softphone for VDI 12.9(3) supports the following new platforms:

Citrix Virtual Desktop and Application 7 2012 (CR)

Citrix Virtual Desktop and Application 7 1912 Cu2 (LTSR)

#### Recording Tone Duration

You could already play recording notification tones in Jabber that only agents or
                                    customers could hear. You can now change the duration of the ringtone. You turn on
                                    this feature in Unified CM Administration under System > Service
                                       Parameters . See the monitoring and recording chapter of the Features
                                       and Services Guide for Cisco Unified Communications Manager for details
                                    on enabling recording tones.

After enabling recording tones, choose a Jabber client configuration profile in User Management > User Settings > UC Service . Add the
                                    following jabber-config.xml parameter to the profile:

Indicates the length of time in milliseconds for which the recording tone
                                          is inserted in the audio stream. The default for this parameter is set
                                          to the value in the Network locale file for this field. The valid range
                                          for this parameter is a value between 100 and 2000 milliseconds (ms).
                                          (The default is 500 ms.)

### 12.9(2)

#### New Supported Platforms

Cisco Jabber Softphone for VDI 12.9(2) supports the following new platforms:

Citrix XenApp and XenDesktop 7.15 Cu6 (LTSR)

Citrix Virtual Desktop and Application 7 2009 (CR)

VMware Horizon 7.13 and VMware Horizon Client 5.5

### 12.9(1)

#### Mac OS Thin Client Support

Cisco Jabber Softphone for VDI for VDI release 12.9(1) now supports MacBook (MacOS) platforms as thin clients. Users can use a Mac device (on MacOS 10.14
                                    or 10.15) to access the Hosted Virtual Desktop (HVD). Install the latest version of Citrix Workspace before installing the
                                    VDI client. If not, the VDI client installation fails. Cisco Jabber Softphone for VDI for VDI 12.9(1) for MacOS supports most calling features that are already supported on Windows and Linux platforms. For "Headset
                                    Call Control”, MacOS only supports Jabra Headsets.

Cisco Jabber Softphone for VDI for MacOS also supports using audio devices as accessory to do call control such as answer/end and mute/unmute. The support
                                    list is aligned with Jabber for Mac. See https://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html for more information.

##### Requirements—Mac OS

###### Supported Operating Systems

Cisco Jabber Softphone for VDI is supported on the following MacOS versions:

Mojave (10.14)

Catalina (10.15)

###### Hardware Requirements

Intel Core 2 Duo or later processors on any of the following Apple hardware:

iMac Pro

MacBook Pro

MacBook

MacBook Air

iMac

Mac Mini

###### Citrix Workspace Requirements

Cisco Jabber Softphone for VDI release 12.9(1) for Mac OS only works in the Citrix VDI environment. You must install the latest Citrix Workspace client
                                       (not the Citrix Receiver client) before you install the Cisco JVDI Client .

Citrix Receiver 13.0 and later

Citrix Workspace app 1808 and later

VMware Horizon View Client versions 4.x and 5.x

The Citrix Workspace app or VMware Horizon Client provides a user interface for the corresponding connection broker.

Published application mode and the scale to fit option are not supported.

##### Accept permissions

When users launch the Cisco JVDI Client on Mac OS for the first time, accept the following required permissions:

Permission

Description

Access Camera

Uses the camera in a video call, or trying to open the camera in Settings.

Access Microphone

Uses the microphone for voice in a call.

Record Screen

Uses the camera in a video call, or trying to open the camera in Settings.

Access Accessibility

Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                               (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                               this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI.

##### Run the MacOS Installer

Run the MacOS installer (PKG) to install Cisco JVDI Client .

Double-click the Install_Cisco_JVDI_Client.pkg file.

Read the EULA and, if you agree, click Continue .

Click Install , and if a prompt appears that Citrix Viewer must be closed first, click Close Application and Install .

You can also click Install Later if you cannot close Citrix at the time.

Click through the remaining screens to complete the installation.

#### New Supported Platforms

Cisco Jabber Softphone for VDI 12.9(1) supports the following new platforms:

Windows Server 2019 as a Hosted Virtual Desktop (HVD)

VMWare Horizon 8 as a connection broker

Citrix Virtual Apps and Desktops CR up to 2006 as a connection broker

#### Recording Tone

You could already play recording notification tones that only agents could hear. You can now play recording tones to the customer
                                    also. You turn on this feature in Unified CM Administration under System > Service Parameters . See the Cisco Jabber Release Notes for more information and see the monitoring and recording chapter of the Features and Services Guide for Cisco Unified Communications Manager for details on enabling recording tones.

### 12.9

#### All Platform Features

##### Cisco Jabber Support

This release supports the following new Cisco Jabber for Windows Release 12.9 features:

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

#### HP Thin Pro Features

##### Non-Full Screen (Windowed) Mode Support For Jabber VDI (Linux Only)

In earlier releases of Jabber VDI for Linux, we only supported full screen mode. If you set non-full screen mode, this affected
                                       the functionality. Now, we also support non-full screen mode.

#### Ubuntu Features

##### Presence Improvement for Linux Thin Clients (Ubuntu and eLux Only)

We've improved how Cisco Jabber Softphone for VDI passes presence (status) information from the Linux thin client (Ubuntu
                                       and eLux) o the hosted virtual desktop. Now when a user locks their thin client, their presence updates to Away . If their connection is lost, their presence updates to Offline .

New Parameter —HVDDisconnectSignout

Value —True or False

Default —False

If the parameter is set to True, Jabber signs out when the HVD disconnects.

If the parameter is set to False, Jabber still shows as available when the HVD disconnects.

| Version | Build Number |
|---|---|
| Cisco Jabber Softphone for VDI Release 12.9(3) Cisco JVDI Agent Cisco JVDI Client | 12.9.3.305062 |
| Cisco Jabber Softphone for VDI Release 12.9(2) Cisco JVDI Agent Cisco JVDI Client | 12.9.2.304552 |
| Cisco Jabber Softphone for VDI Release 12.9(1) Cisco JVDI Agent Cisco JVDI Client | 12.9.1.304247 |
| Cisco Jabber Softphone for VDI Release 12.9 Cisco JVDI Agent Cisco JVDI Client | 12.9.0.303399 |

| Hardware | Requirement |
|---|---|
| Installed RAM | 2 GB RAM |
| Free physical memory | 1 GB |
| Free disk space | 300 MB |
| CPU speed and type | Intel Core 2 Duo or later processors on any of the following Apple hardware: iMac Pro MacBook Pro MacBook MacBook Air iMac Mac Mini |
| I/O ports | USB 2.0 for USB camera and audio devices |

| When users launch the Cisco JVDI Client on Mac OS for the first time, accept the following required permissions: Table 1. Required permissions Permission Description Access Camera Uses the camera in a video call, or trying to open the camera in Settings. Access Microphone Uses the microphone for voice in a call. Record Screen Uses the camera in a video call, or trying to open the camera in Settings. Access Accessibility Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                               (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                               this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI. | Permission | Description | Access Camera | Uses the camera in a video call, or trying to open the camera in Settings. | Access Microphone | Uses the microphone for voice in a call. | Record Screen | Uses the camera in a video call, or trying to open the camera in Settings. | Access Accessibility | Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                               (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                               this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI. |
|---|---|---|---|---|---|---|---|---|---|---|
| Permission | Description |
| Access Camera | Uses the camera in a video call, or trying to open the camera in Settings. |
| Access Microphone | Uses the microphone for voice in a call. |
| Record Screen | Uses the camera in a video call, or trying to open the camera in Settings. |
| Access Accessibility | Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                               (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                               this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI. |

| Permission | Description |
|---|---|
| Access Camera | Uses the camera in a video call, or trying to open the camera in Settings. |
| Access Microphone | Uses the microphone for voice in a call. |
| Record Screen | Uses the camera in a video call, or trying to open the camera in Settings. |
| Access Accessibility | Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                               (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                               this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI. |

| Step 1 | Double-click the Install_Cisco_JVDI_Client.pkg file. |
|---|---|
| Step 2 | Read the EULA and, if you agree, click Continue . |
| Step 3 | Click Install , and if a prompt appears that Citrix Viewer must be closed first, click Close Application and Install . You can also click Install Later if you cannot close Citrix at the time. |
| Step 4 | Click through the remaining screens to complete the installation. |