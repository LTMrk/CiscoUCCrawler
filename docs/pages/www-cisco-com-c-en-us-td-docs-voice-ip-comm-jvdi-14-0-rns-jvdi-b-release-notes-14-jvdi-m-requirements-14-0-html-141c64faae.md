---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-14-0-rns-jvdi-b-release-notes-14-jvdi-m-requirements-14-0-html-141c64faae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/14_0/rns/jvdi_b_release-notes-14/jvdi_m_requirements-14-0.html
retrieved_at: 2026-08-25T23:18:04.473128+00:00
---

Release Notes for Cisco Jabber Softphone for VDI Release 14.0

# Release Notes for Cisco Jabber Softphone for VDI Release 14.0

Updated: March 25, 2021

Chapter: Requirements

## Chapter: Requirements

# Requirements

## General Requirements

General requirements apply to all Cisco Jabber Softphone for VDI platforms.

Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                          can result in a nonfunctional deployment.

### Accessories

For a complete listing of recommended audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware.

### Cisco Jabber for Windows

This release of Cisco Jabber for Windows, running on the hosted virtual desktop (HVD).

For complete information about virtual environment compatibility, see the Cisco Jabber documentation for your release.

### Cisco Unified Communications Manager

Recommended: Unified CM Release 11.5(1)SU3 or later

Minimum: Unified CM Release 10.5

### Cisco Expressway for Mobile and Remote Access (MRA)

Recommended: Expressway X12.5

Minimum: Expressway X8.11.4

Cisco Jabber Softphone for VDI with MRA only supports OAuth 2.0 for authentication. See the Deploying OAuth with Cisco Collaboration Solution guide for more information.

JVDI over MRA does not support collab-edge SRV
                                             being resolveable from the HVD. Softphone
                                             registration with JVDI fails in this case.

When using JVDI over MRA deployments with Split
                                             DNS (different domains for inside and outside the
                                             network), the HVD must not discover the internal
                                             domain. If it does, Cisco Jabber Softphone for VDI registration also fails. To ensure the client
                                             does not discover the internal domain, disable UPN
                                             during Jabber installation on HVD.

### Connection Broker—Installed on the Hosted Virtual Desktops

Citrix XenApp and XenDesktop 6.x, 7.x (CR—up to 7.18; LTSR—up to 7.15 CU7),
                                       and Citrix Virtual Apps and Desktops 7 (CR—up to 2012, LTSR—up to 1912
                                       CU2)

VMware Horizon versions 6.x to 8.x.

A connection broker is software that creates connections to hosted virtual desktops. A connection broker performs a number
                                 of tasks including the following:

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

### Operating Systems—Installed on the Hosted Virtual Desktops

Microsoft Windows 8.1 32–bit

Microsoft Windows 8.1 64 64–bit

Microsoft Windows 10 32–bit

Microsoft Windows 10 64–bit

Microsoft Windows 11 64–bit (as of Jabber VDI 14.0.3)

### Server Operating Systems—Installed on the Hosted Virtual Desktops

Microsoft Windows Server 2012 R2

Microsoft Windows Server 2016

Microsoft Windows Sever 2019

### Port Requirements

Cisco Jabber Softphone for VDI requires the same ports as Cisco Jabber does, and the following additional port range:

Port Range

Description

16384–32767

UDP Inbound and outbound traffic for RTP (audio and video streams)

You can configure the Cisco Unified Communications Manager to reduce this port range. Change the Start/Stop Media Port setting in the SIP Profile, which is associated with the CSF device.

### Supported Codecs

#### Supported Codecs

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

## Requirements—MacOS

### Supported Operating Systems

Cisco Jabber Softphone for VDI 14.0 is supported on the following MacOS versions:

Mojave (10.14)

Catalina (10.15)

Big Sur (11)

Monterey (12)—As of 14.0.3

### Hardware Requirements

Intel Core 2 Duo or later processors on any of the following
                                          Apple hardware:

iMac Pro

MacBook Pro

MacBook

MacBook Air

iMac

Mac Mini

Cisco Jabber Softphone for VDI also supports Apple M1 processors.

### Citrix and VMware Requirements

This release Cisco Jabber Softphone for VDI for Mac OS works in Citrix and VMware VDI environments. You must install
                              the latest Citrix Workspace client (not the Citrix Receiver client) or VMware
                              Horizon client before you install the Cisco JVDI Client .

Citrix Receiver 13.0 and later

Citrix Workspace app 1808 and later

VMware Horizon View Client versions 5.5, 8.0, or 8.1

The Citrix Workspace app or VMware Horizon Client provides a user interface for the
                              corresponding connection broker.

Published application mode and the scale to fit option are not supported.

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

## Requirements—Unicon eLux

Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                          can result in a nonfunctional deployment.

### Unicon eLux Platform Image

64–bit: Unicon eLux 6.5

64–bit: Unicon eLux 6.8

64–bit: Unicon eLux 6.9

64–bit: Unicon eLux RP6 LTSR 2104 Cu2 (as of Release 14.0.4)

The eLux packages are available from Unicon eLux. For assistance locating a download, contact eLux support.

### Unicon eLux Thin Clients—Hardware

The minimum hardware requirements for thin clients are:

1.6 GHz dual-core processor

2 GB RAM

We recommend the following client hardware, which was tested with eLux RP 5.7.0:

HP T620 Dual Core / Quad Core

HP T630 Dual Core / Quad Core

HP T730

Cisco VXC 6215

Dell Wyse Z50D

### Citrix Workspace App or VMware Horizon Client—Installed on the Thin Clients

Unicon eLux includes the required Citrix and VMware versions.

The Citrix Workspace app or VMware Horizon Client provides a user interface for the corresponding connection broker.

Published application mode and the scale to fit option are not supported.

### Cisco Anyconnect (Optional)

vpnsystem V4.5-1

## Requirements—Windows

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

Microsoft Windows 8.1 32–bit

Microsoft Windows 8.1 64–bit

Microsoft Windows 10 32–bit

Microsoft Windows 10 64–bit

Microsoft Windows 11 64–bit

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

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

### Windows Embedded Standard—Installed on the Thin Clients

Windows Embedded Standard 8 64–bit

Requires Update for Windows Embedded Standard 8 for 64–bit Systems (KB4019990)

Windows 10 IoT Enterprise

### Citrix Workspace App or VMware Horizon Client—Installed on the Thin Clients

Citrix Receiver (ICA) for Windows 4.4 and later

Citrix Workspace App (ICA) for Windows 1808 and later

Cisco Jabber Softphone for VDI does not support Citrix Workspace App downloaded from the Microsoft Store.

VMware Horizon Client for Windows 4.1.0 and later

(Versions 4.3 and 4.4 are not supported.)

The Citrix Workspace app or VMware Horizon Client provides a user interface for the corresponding connection broker.

Before you install the Cisco JVDI Client, install the Citrix Receiver or VMware Horizon Client on the thin client.

If you change from a Citrix environment to a VMware environment (or from VMware to Citrix), reinstall the Cisco JVDI Client.

Cisco Jabber Softphone for VDI supports full-screen and windowed display for Windows and Linux thin clients in both VMWare
                              and Citrix VDI environments.

## Version Support Strategy

The Cisco Jabber for Windows and Cisco JVDI Agent major versions (N.A) must
                                    always match. However, the JVDI Client version can be the same, or up to two
                                    releases earlier (N-2 support).

N.A-C denotes the range of major releases. x-z denotes the numbers of different maintenance
                                                releases. These numbers are used for example purposes only.

For example, the following version combinations are supported within a
                                    release range:

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.A(y), and Cisco JVDI Client Release N.A(z)

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.A(y), and Cisco JVDI Client Release N.B(z)

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.A(y), and Cisco JVDI Client Release N.C(z)

The above examples cover the supported range within a single major
                                                release. For a major release that starts at a new release number (for
                                                example, 14.0), the JVDI client is also supported on the two previous
                                                releases (for example, 12.9 and 12.8).

The following version combinations are not supported within a release
                                    range:

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.A(y), and Cisco JVDI Client Release N.D(z)

Cisco Jabber for Windows Release N.A(x), Cisco JVDI Agent Release
                                          N.B(y), and Cisco JVDI Client Release N.C(z)

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                          can result in a nonfunctional deployment. |
|---|---|

| Note | JVDI over MRA does not support collab-edge SRV
                                             being resolveable from the HVD. Softphone
                                             registration with JVDI fails in this case. When using JVDI over MRA deployments with Split
                                             DNS (different domains for inside and outside the
                                             network), the HVD must not discover the internal
                                             domain. If it does, Cisco Jabber Softphone for VDI registration also fails. To ensure the client
                                             does not discover the internal domain, disable UPN
                                             during Jabber installation on HVD. |
|---|---|

| Port Range | Description |
|---|---|
| 16384–32767 | UDP Inbound and outbound traffic for RTP (audio and video streams) You can configure the Cisco Unified Communications Manager to reduce this port range. Change the Start/Stop Media Port setting in the SIP Profile, which is associated with the CSF device. |

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                          can result in a nonfunctional deployment. |
|---|---|

| Requirement | Cisco Jabber for Mac |
|---|---|
| Installed RAM | 2 GB RAM |
| Free physical memory | 1 GB |
| Free disk space | 300 MB |
| CPU speed and type | Intel Core 2 Duo or later processors on any of the following
                                          Apple hardware: iMac Pro MacBook Pro MacBook MacBook Air iMac Mac Mini Cisco Jabber Softphone for VDI also supports Apple M1 processors. |
| I/O ports | USB 2.0 for USB camera and audio devices |

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                          can result in a nonfunctional deployment. |
|---|---|

| Note | The supported versions do not include Ubuntu Minimal. |
|---|---|

| Important | Only the components, versions, and minimum hardware requirements listed in this guide are supported. Use of unsupported components
                                          can result in a nonfunctional deployment. |
|---|---|

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

| Note | N.A-C denotes the range of major releases. x-z denotes the numbers of different maintenance
                                                releases. These numbers are used for example purposes only. |
|---|---|

| Note | The above examples cover the supported range within a single major
                                                release. For a major release that starts at a new release number (for
                                                example, 14.0), the JVDI client is also supported on the two previous
                                                releases (for example, 12.9 and 12.8). |
|---|---|