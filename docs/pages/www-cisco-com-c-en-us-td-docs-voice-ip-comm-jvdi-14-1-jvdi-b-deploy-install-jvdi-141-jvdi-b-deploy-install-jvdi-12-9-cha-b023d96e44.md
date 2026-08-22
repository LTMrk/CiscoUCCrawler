---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-14-1-jvdi-b-deploy-install-jvdi-141-jvdi-b-deploy-install-jvdi-12-9-cha-b023d96e44
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/14_1/jvdi_b_deploy-install-jvdi-141/jvdi_b_deploy-install-jvdi-12-9_chapter_01.html
retrieved_at: 2026-08-22T00:35:39.237576+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 14.1

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 14.1

Updated: March 14, 2022

Chapter: Planning

## Chapter: Planning

# Planning

## Cisco Jabber Softphone for VDI

The applications in the Cisco Jabber Softphone for VDI family of products are:

Cisco Jabber Softphone for VDI —HP Thin Pro and Ubuntu

Cisco Jabber Softphone for VDI —MacOS

Cisco Jabber Softphone for VDI —Unicon eLux

Cisco Jabber Softphone for VDI —Windows

Cisco Jabber Softphone for VDI —Dell Wyse Thin OS (Available from, and supported by Dell Wyse)

## Cisco Jabber and VDI

Cisco Jabber chat and presence are supported in Virtual Desktop Infrastructure deployments. However, because of a limitation known as
                              the hairpin effect , calling and video capability are not supported. The additional bandwidth required for calls and video creates a bottleneck
                              at the data center.

Cisco Jabber Softphone for VDI extends the Cisco collaboration experience to virtual deployments. With a supported version of Cisco Jabber for Windows, users can send and receive phone calls on their hosted virtual desktops (HVD). The Cisco Jabber Softphone for VDI software automatically detects the virtual environment. To reduce latency and to enhance media quality, Cisco Jabber Softphone for VDI streams media between the endpoints without going through the hosted virtual desktops.

The Cisco JVDI architecture consists of two primary components: the Cisco JVDI Agent and the Cisco JVDI Client. The Cisco
                              JVDI Client is installed on a thin client while the Cisco JVDI Agent is installed on the HVD.

When a user launches a virtual broker client (Citrix Workspace app or VMWare Horizon Client), the software initiates a virtual
                              channel. The JVDI Client and Agent use this virtual channel to communicate.

The diagrams below shows the architecture as well as the expected protocol sessions that are set up during normal use. In
                              this example, Jabber is deployed in full UC mode over Mobile Remote Access (MRA). The next diagram shows the data flow between
                              all components in a standard Cisco Jabber Softphone for VDI deployment.

To start a session, users launch their virtual broker client (Citrix Workspace App or VMware Horizon Client) and connect to
                                    the connection broker and select a HVD or virtual application. Once select, a virtual channel is set up between the users'
                                    Thin Client (Physical Machine) and the HVD (Virtual Machine) hosted on the Hypervisor.

Once Jabber and determines if is in a virtual environment, the JVDI Agent process (hvdagent.exe) starts and begins the service
                                    discovery. Once authenticated with Unified CM, Jabber performs all its normal UDS queries (Home Cluster, UDS Server, Unified
                                    CM End User, and Device lookup) and caches all the retrieved information.

The JVDI Client and JVDI Agent then go through the process of setting up all the control steams that are used to exchange
                                    data over the virtual channel. Once these channels are set up, Jabber retrieves the cached information (Email Address, Voice
                                    Service Domain, Credentials, TFTP Server, Device Name, CTL Info, and LSC Info) and provides it to the JVDI Client.

The JVDI Client performs service discovery. It references either or both the cached email address (entered on Jabber login)
                                    and the voice service domain information that the JVDI Agent provided. The JVDI Client is able to resolve the _collab-edge
                                    DNS SRV record because this connection is over MRA. Once service discovery is complete, the JVDI Client attempts to retrieve
                                    the CSF Device configuration, Application Dial Rules, and Directory Lookup Dial Rules from Unified CM TFTP through the Expressway.

After receiving the CSF device configuration, the JVDI Client begins softphone registration process by performing the SIP
                                    registration process with the Unified CM CallManager services. Once completed, the CSF device shows as registered in the Cisco
                                    Unified CM Administration interface.

Jabber attempts to CTI control the registered CSF device. Jabber establishes a CTI QBE control session between the Jabber
                                    device and the Unified CM CTIManager service. When completed successfully, Jabber gains CTI control of the CSF device and
                                    line. Thie step enables Jabber to be able to make and receive calls.

The XMPP connection between Jabber and IM and Presence does not traverse the virtual channel. All XMPP traffic remains on
                                    the LAN directly between the HVD and the IM and Presence server.

JVDI over MRA does not support collab-edge SRV being resolveable from the
                                                hosted virtual desktop (HVD).

For MRA deployments with Split DNS, the HVD must not discover the
                                                external domain. Do one of the following:

Configure SERVICES_DOMAIN and VOICE_SERVICES_DOMAIN during Jabber
                                                      software installation on the HVD.

Configure servicesDomain and voiceServicesDomain parameters in
                                                      the jabber-config.xml file.

Use the following flowchart to determine whether you require Cisco Jabber Softphone for VDI .

## The User Experience

Cisco Jabber Softphone for VDI detects the virtual environment at run time and Cisco Jabber starts  in virtualization mode. The user experience with Cisco Jabber for Windows and Cisco Jabber Softphone for VDI is similar to the non-VDI experience. However, in a virtual environment there are some minor differences:

Device Selector , which is located in the Windows notification area, allows users to quickly switch their active camera and audio devices.
                                    Device management is also available from within Cisco Jabber .

Headset Priority —By default, Cisco Jabber adds a newly connected device to the top of the priority list, and makes the new device active. You can set the HeadsetPreference parameter so that Cisco Jabber adds new devices to the bottom of the priority list. For more information, see Parameters Reference Guide for Cisco Jabber .

Feature Support — Cisco Jabber Softphone for VDI supports most Cisco Jabber for Windows features, with some exceptions. For more information, see the notes for your platform in Release Notes for Cisco Jabber Softphone for VDI .

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

Citrix XenApp and XenDesktop 6.x, 7.x (CR—up to 7.18; LTSR—up to 7.15 CU8), and Citrix Virtual Apps and Desktops 7 (CR—up
                                       to 2112, LTSR—up to 1912 CU4)

VMware Horizon versions 6.x to 8.x.

Since Citrix Virtual Applications & Desktops 7 2109, "virtual channel allow list policy" is enabled by default. Either configure
                                             this policy for JVDI first (by adding Cisco Virtual Channel) for optimized mode to work properly or disable this policy.

```
CISCO,C:\Program Files (x86)\Cisco Systems\Vxc\hvdagent.exe
```

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

When HP releases Thinpro 8.0, we will support it.

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

| Note | JVDI over MRA does not support collab-edge SRV being resolveable from the
                                                hosted virtual desktop (HVD). For MRA deployments with Split DNS, the HVD must not discover the
                                                external domain. Do one of the following: Configure SERVICES_DOMAIN and VOICE_SERVICES_DOMAIN during Jabber
                                                      software installation on the HVD. Configure servicesDomain and voiceServicesDomain parameters in
                                                      the jabber-config.xml file. |
|---|---|

| Note | Users can override this setting in their Audio preferences. |
|---|---|

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

| Important | Since Citrix Virtual Applications & Desktops 7 2109, "virtual channel allow list policy" is enabled by default. Either configure
                                             this policy for JVDI first (by adding Cisco Virtual Channel) for optimized mode to work properly or disable this policy. CISCO,C:\Program Files (x86)\Cisco Systems\Vxc\hvdagent.exe |
|---|---|

| Port Range | Description |
|---|---|
| 16384–32767 | UDP Inbound and outbound traffic for RTP (audio and video streams) You can configure the Cisco Unified Communications Manager to reduce this port range. Change the Start/Stop Media Port setting in the SIP Profile, which is associated with the CSF device. |

| Note | When HP releases Thinpro 8.0, we will support it. |
|---|---|

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