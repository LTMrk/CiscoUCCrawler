---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-14-1-jvdi-b-jvdi-release-notes-141-jvdi-m-whats-new-141-html-0fbc4961ca
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/14_1/jvdi_b_jvdi-release-notes-141/jvdi_m_whats-new-141.html
retrieved_at: 2026-08-25T23:18:16.855363+00:00
---

Release Notes for Cisco Jabber Softphone for VDI Release 14.1

# Release Notes for Cisco Jabber Softphone for VDI Release 14.1

Updated: March 9, 2022

Chapter: What's new in Release 14.1

## Chapter: What's new in Release 14.1

# What's new in Release 14.1

## Build numbers

Version

Build Number

Cisco Jabber Softphone for VDI Release 14.1.4

Cisco JVDI Agent

Cisco JVDI Client

14.1.4.57909 build 307909

Cisco Jabber Softphone for VDI Release 14.1.3

Cisco JVDI Agent

Cisco JVDI Client

14.1.3.57560 build 307560

Cisco Jabber Softphone for VDI Release 14.1.2

Cisco JVDI Agent

Cisco JVDI Client

14.1.2.57144 Build 307144

Cisco Jabber Softphone for VDI Release 14.1.1

Cisco JVDI Agent

Cisco JVDI Client

14.1.1.56904 Build 306904

Cisco Jabber Softphone for VDI Release 14.1

Cisco JVDI Agent

Cisco JVDI Client

14.1.0.56686 Build 306686

## New and updated features

### 14.1.4

#### VDI infrastructure builds

Citrix Virtual Applications & Desktops 7 CR 2305

Citrix Virtual Applications & Desktops 7 LTSR 2203 Cu3

Citrix Virtual Applications & Desktops 7 LTSR 1912 Cu7

VMware Horizon 2303 (8.9)

#### Thin client OS support

Unicon eLux RP6 LTSR 2302.2

#### Hosted Virtual Desktop OS support

Microsoft Windows 11

#### Hardware support

Apple devices with M2 chips

### 14.1.3

#### VDI infrastructure builds

Citrix Virtual Applications & Desktops 7 CR 2212

Citrix Virtual Applications & Desktops 7 LTSR 2203 Cu2

Citrix Virtual Applications & Desktops 7 LTSR 1912 Cu6

VMware Horizon 2209 (8.7)

### 14.1.2

#### VDI infrastructure builds

Citrix Virtual Applications & Desktops 7 LTSR 2206

VMware Horizon 2206 (8.6)

If you upgrade to VMware Horizon Client 2206 (8.6), you must upgrade the JVDI Client for Windows to 14.1 MR2.

#### Hosted virtual desktop operating system

Use Windows 2022 with Jabber VDI 14.1.2.

### 14.1.1

#### VDI infrastructure builds

Citrix Virtual Applications & Desktops 7 LTSR 2203

Citrix Virtual Applications & Desktops 7 LTSR 1912 Cu5

VMware Horizon 2203 (8.5)

### 14.1

#### Supported platforms

Microsoft Windows 11

Apple MacOS 12

Unicon eLux RP6 2104 LTSR Cu2

When HP releases Thinpro 8.0, we will support it.

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

| Version | Build Number |
|---|---|
| Cisco Jabber Softphone for VDI Release 14.1.4 Cisco JVDI Agent Cisco JVDI Client | 14.1.4.57909 build 307909 |
| Cisco Jabber Softphone for VDI Release 14.1.3 Cisco JVDI Agent Cisco JVDI Client | 14.1.3.57560 build 307560 |
| Cisco Jabber Softphone for VDI Release 14.1.2 Cisco JVDI Agent Cisco JVDI Client | 14.1.2.57144 Build 307144 |
| Cisco Jabber Softphone for VDI Release 14.1.1 Cisco JVDI Agent Cisco JVDI Client | 14.1.1.56904 Build 306904 |
| Cisco Jabber Softphone for VDI Release 14.1 Cisco JVDI Agent Cisco JVDI Client | 14.1.0.56686 Build 306686 |

| Note | If you upgrade to VMware Horizon Client 2206 (8.6), you must upgrade the JVDI Client for Windows to 14.1 MR2. |
|---|---|

| Note | When HP releases Thinpro 8.0, we will support it. |
|---|---|