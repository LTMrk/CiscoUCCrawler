---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-1-windows-deploy-jvdi-b-deployment-installation-jvdi-windows-12-1-jv-65ef3cb1de
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_1/windows/deploy/jvdi_b_deployment-installation-jvdi-windows-12-1/jvdi_b_deployment-installation-jvdi-windows-12-1_chapter_01.html
retrieved_at: 2026-08-22T00:38:32.033584+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Windows Release 12.1

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Windows Release 12.1

Updated: July 18, 2018

Chapter: Requirements

## Chapter: Requirements

# Requirements

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

DirectX 11 compatible GPU

USB 2.0 for USB camera and audio devices

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

A connection broker is software that creates connections to hosted virtual desktops. A connection broker performs a number
                                    of tasks that include

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

The Citrix Receiver or VMware Horizon Client provides a user interface for the corresponding connection broker.

(PCoIP only)

## Considerations for Thin Clients

Windows thin clients, including older PCs, must meet all system requirements. For more information, see Release Notes for Cisco Jabber Softphone for VDI —Windows for your release.

## Port Requirements

The Cisco JVDI Client installer does not add firewall rules.

If the Windows Firewall is enabled on the thin clients, you must add the Cisco JVDI Client (vxc.exe) as an exception. The first time that you start Cisco JVDI Client , a Windows Security Alert appears. To add the exception, check the networks for which you want to allow Cisco JVDI Client . For more information about how to configure the Windows Firewall, see the Microsoft documentation.

This requirement applies to all versions of the Windows Firewall, including Windows Defender.

The following table lists the ports and port ranges used by Cisco Jabber Softphone for VDI .

Port

Description

69 and Ephemeral

UDP Outbound traffic for TFTP

An ephemeral port is a short-lived transport protocol port for IP communications. IP software can allocate ephemeral ports
                                                      automatically from a predefined range. The following protocols can use an ephemeral port assignment for the client end of
                                                      a communication, to a well-known port on a server.

Stream Control Transmission Protocol (SCTP)

Transmission Control Protocol (TCP)

User Datagram Protocol (UDP)

A well-known port is a port reserved by the Internet Corporation for Assigned Names and Numbers (ICANN) for assignment for
                                                      specific applications.

5060

TCP (default) or UDP Outbound traffic for Session Initiation Protocol (SIP) call signaling

5061

TCP Outbound traffic for Secure SIP call signaling

6970

TCP Outbound traffic for HTTP

16384–32767

UDP Inbound and outbound traffic for RTP (audio and video streams)

You can configure the Cisco Unified Communications Manager to reduce this port range. Change the Start/Stop Media Port setting in the SIP Profile, which is associated with the CSF device.

## Supported Codecs

Audio Codec

Video Codec

G.722

H.264/AVC

G.722.1 (24 and 32k)

G.722.1 is supported on  Cisco Unified Communications
                                          Manager 8.6.1 or later.

G.711 A-law

G.711 u-law

G.729a

Opus

Opus is supported on Cisco Unified Communications
                                          Manager 11.0 or later.

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

| Important | The Cisco JVDI Client installer does not add firewall rules. If the Windows Firewall is enabled on the thin clients, you must add the Cisco JVDI Client (vxc.exe) as an exception. The first time that you start Cisco JVDI Client , a Windows Security Alert appears. To add the exception, check the networks for which you want to allow Cisco JVDI Client . For more information about how to configure the Windows Firewall, see the Microsoft documentation. This requirement applies to all versions of the Windows Firewall, including Windows Defender. |
|---|---|

| Port | Description |
|---|---|
| 69 and Ephemeral | UDP Outbound traffic for TFTP Note An ephemeral port is a short-lived transport protocol port for IP communications. IP software can allocate ephemeral ports
                                                      automatically from a predefined range. The following protocols can use an ephemeral port assignment for the client end of
                                                      a communication, to a well-known port on a server. Stream Control Transmission Protocol (SCTP) Transmission Control Protocol (TCP) User Datagram Protocol (UDP) A well-known port is a port reserved by the Internet Corporation for Assigned Names and Numbers (ICANN) for assignment for
                                                      specific applications. | Note | An ephemeral port is a short-lived transport protocol port for IP communications. IP software can allocate ephemeral ports
                                                      automatically from a predefined range. The following protocols can use an ephemeral port assignment for the client end of
                                                      a communication, to a well-known port on a server. Stream Control Transmission Protocol (SCTP) Transmission Control Protocol (TCP) User Datagram Protocol (UDP) A well-known port is a port reserved by the Internet Corporation for Assigned Names and Numbers (ICANN) for assignment for
                                                      specific applications. |
| Note | An ephemeral port is a short-lived transport protocol port for IP communications. IP software can allocate ephemeral ports
                                                      automatically from a predefined range. The following protocols can use an ephemeral port assignment for the client end of
                                                      a communication, to a well-known port on a server. Stream Control Transmission Protocol (SCTP) Transmission Control Protocol (TCP) User Datagram Protocol (UDP) A well-known port is a port reserved by the Internet Corporation for Assigned Names and Numbers (ICANN) for assignment for
                                                      specific applications. |
| 5060 | TCP (default) or UDP Outbound traffic for Session Initiation Protocol (SIP) call signaling |
| 5061 | TCP Outbound traffic for Secure SIP call signaling |
| 6970 | TCP Outbound traffic for HTTP |
| 16384–32767 | UDP Inbound and outbound traffic for RTP (audio and video streams) You can configure the Cisco Unified Communications Manager to reduce this port range. Change the Start/Stop Media Port setting in the SIP Profile, which is associated with the CSF device. |

| Note | An ephemeral port is a short-lived transport protocol port for IP communications. IP software can allocate ephemeral ports
                                                      automatically from a predefined range. The following protocols can use an ephemeral port assignment for the client end of
                                                      a communication, to a well-known port on a server. Stream Control Transmission Protocol (SCTP) Transmission Control Protocol (TCP) User Datagram Protocol (UDP) A well-known port is a port reserved by the Internet Corporation for Assigned Names and Numbers (ICANN) for assignment for
                                                      specific applications. |
|---|---|

| Audio Codec | Video Codec |
|---|---|
| G.722 | H.264/AVC |
| G.722.1 (24 and 32k) G.722.1 is supported on  Cisco Unified Communications
                                          Manager 8.6.1 or later. |  |
| G.711 A-law |  |
| G.711 u-law |  |
| G.729a |  |
| Opus Opus is supported on Cisco Unified Communications
                                          Manager 11.0 or later. |  |