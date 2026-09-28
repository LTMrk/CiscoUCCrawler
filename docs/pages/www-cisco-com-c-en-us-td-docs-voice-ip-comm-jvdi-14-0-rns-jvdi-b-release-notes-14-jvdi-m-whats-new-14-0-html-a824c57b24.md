---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-14-0-rns-jvdi-b-release-notes-14-jvdi-m-whats-new-14-0-html-a824c57b24
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/14_0/rns/jvdi_b_release-notes-14/jvdi_m_whats-new-14-0.html
retrieved_at: 2026-08-25T23:18:00.004108+00:00
---

Release Notes for Cisco Jabber Softphone for VDI Release 14.0

# Release Notes for Cisco Jabber Softphone for VDI Release 14.0

Updated: March 25, 2021

Chapter: What's New in Release 14.0

## Chapter: What's New in Release 14.0

# What's New in Release 14.0

## Build Number

Version

Build Number

Cisco Jabber Softphone for VDI Release 14.0(3)

Cisco JVDI Agent

Cisco JVDI Client

14.0.3.306553

Cisco Jabber Softphone for VDI Release 14.0(2)

Cisco JVDI Agent

Cisco JVDI Client

14.0.2.306216

Cisco Jabber Softphone for VDI Release 14.0(1)

Cisco JVDI Agent

Cisco JVDI Client

14.0.1.305989

Cisco Jabber Softphone for VDI Release 14.0

Cisco JVDI Agent

Cisco JVDI Client

14.0.0.305549

## New and Updated Features

### 14.0(3)

This release includes bug fixes and minor enhancements. For more information, see Resolved Caveats in Release 14.0(3) .

#### Supported platforms

Microsoft Windows 11

Apple MacOS 12

Unicon eLux RP6 2104 LTSR Cu2

#### VDI infrastructure builds

Citrix Virtual Applications & Desktops 7 CR 2112

Citrix Virtual Applications & Desktops 7 LTSR 1912 Cu4

Citrix Xendesktop & XenApp 7.15 LTSR Cu8

VMware Horizon 2111 (8.4)

#### Important notice about Citrix Virtual Applications & Desktops

Since Citrix Virtual Applications & Desktops 7 2109, "virtual channel allow list policy" is enabled by default. Either configure
                                 this policy for JVDI first (by adding Cisco Virtual Channel) for optimized mode to work properly or disable this policy.

```
CISCO,C:\Program Files (x86)\Cisco Systems\Vxc\hvdagent.exe
```

#### New JVDI configuration parameter

ENABLE_BFCP_DESKTOP_SHARE —Applies to JVDI Client for Windows and Linux

Added to fix CSCwa33411 . This parameter helps disable BFCP screen sharing if necessary.

You configure this parameter in the cisco.conf of JVDI Client. On Windows, cisco.conf is in C:\Program Files\Cisco Systems\Cisco VXME or C:\Program Files (x86)\Cisco Systems\Cisco VXME . On Linux, cisco.conf is in /etc/

true (default)—Enables BFCP screen sharing

false—Disables BFCP screen sharing

#### New Jabber configuration parameter

EnableVDIFullScan —Applies to Jabber for Windows 14.0.4

Added for CSCvz75206 . You must run JVDI 14.0.3 with Jabber for Windows 14.0.4 to use this parameter.

Certain third-party application window can make preview, remote video, and remote share display as gray when the window is
                                 close to a Jabber conversation window. If this issue occurs, enable this parameter.

true—Enables a full scan of JVDI to correct the display issue.

false (default)—Maintains the standard Jabber behavior.

### 14.0(2)

This release includes bug fixes and minor enhancements. For more information, see Resolved Caveats in Release 14.0(2) .

#### Supported Platforms

VMware horizon 8 2106

Citrix Virtual Apps and Desktop 7 CR 2106

Unicon eLux RP6 2104 LTSR

Thin clients of Microsoft Windows 11 64-bit

### 14.0(1)

This release includes bug fixes and minor enhancements. For more information, see Resolved Caveats in Release 14.0(1) .

#### Supported Platforms

Citrix Virtual Apps and Desktop 7 CR 2103 and LTSR 1912 Cu3

Unicon eLux RP 6 2104 LTSR

### 14.0

#### Supported Platforms

iGel OS support

See the iGel documentation for more information.

MacOS VDI client support in a VMware VDI environment

Apple MacOS Big Sur and M1 chip support for thin clients

#### Cisco Jabber Support

Cisco Meeting Server—Lobby Control

Cisco Headset Integration with Jabber VDI Client for Linux

| Version | Build Number |
|---|---|
| Cisco Jabber Softphone for VDI Release 14.0(3) Cisco JVDI Agent Cisco JVDI Client | 14.0.3.306553 |
| Cisco Jabber Softphone for VDI Release 14.0(2) Cisco JVDI Agent Cisco JVDI Client | 14.0.2.306216 |
| Cisco Jabber Softphone for VDI Release 14.0(1) Cisco JVDI Agent Cisco JVDI Client | 14.0.1.305989 |
| Cisco Jabber Softphone for VDI Release 14.0 Cisco JVDI Agent Cisco JVDI Client | 14.0.0.305549 |