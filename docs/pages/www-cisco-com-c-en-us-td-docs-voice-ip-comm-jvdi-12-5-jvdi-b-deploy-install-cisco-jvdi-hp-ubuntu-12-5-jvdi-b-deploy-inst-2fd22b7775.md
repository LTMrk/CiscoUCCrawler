---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-5-jvdi-b-deploy-install-cisco-jvdi-hp-ubuntu-12-5-jvdi-b-deploy-inst-2fd22b7775
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_5/jvdi_b_deploy-install-cisco-jvdi-hp-ubuntu-12-5/jvdi_b_deploy-install-cisco-jvdi-hp-ubuntu-12-5_chapter_01.html
retrieved_at: 2026-08-22T00:34:52.431077+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.5

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.5

Updated: November 29, 2018

Chapter: Requirements

## Chapter: Requirements

# Requirements

## System Requirements

Each of the components listed in the following table must meet the requirements. Use of unsupported components can result
                                          in a nonfunctional deployment.

Only the components and requirements listed in the table are supported.

Component

Requirements

HP Thin Pro thin clients—Hardware

The following client hardware is supported with HP Thin Pro 6.2:

HP t520

HP t530

HP t620

HP t630

HP t730

HP mt21

The following client hardware is supported with HP Thin Pro 7:

HP t430

HP t520

HP t530

HP t630

HP t730

HP mt21

HP ThinPro platform image

HP ThinPro 6.2: T7X62022

HP ThinPro 7: T7X70015

Support is limited for HP Thin Pro 7.

Ubuntu thin clients—Hardware

The following hardware is supported with Ubuntu 14.04 32b LTS:

Installed RAM 2 GB

Free Physical Memory 256 MB

Free Disk Space 256 MB

CPU: AMD G-T56N 1.65Ghz, or Intel Core2Duo T7500 2.2 GHz

USB 2.0 for USB camera and audio devices

Ubuntu

Ubuntu 14.04 i386

Ubuntu 16.04 i386

Support is limited for Ubuntu 16.04.

Hosted virtual desktop OS (server-side)

Microsoft Windows 7 32 bit

Microsoft Windows 7 64 bit

Microsoft Windows 8 32 bit

Microsoft Windows 8 64 bit

Microsoft Windows 8.1 32 bit

Microsoft Windows 8.1 64 bit

Microsoft Windows 10 32 bit

Microsoft Windows 10 64 bit

Citrix XenDesktop 6.5, 7.5, and later 7.x versions

Citrix XenApp 6.5, 7.5, and later 7.x versions—Published desktops only

VMware Horizon 6.0 (with View)—Published desktops only

VMware Horizon 6 version 6.1.0, 6.2.0, 7.0 and later 7.x versions—Published desktops only

Citrix XenApp Published Application is not supported with Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu.

Citrix Receiver or

(Installed on the thin client)

For HP Thin Pro 6.2.0

The HP Thin Pro image includes Citrix and VMware:

ICA Client: 13.5.0 or later (32 bit version required)

VMware 4.4.0 or later (32 bit version required)

For HP Thin Pro 7

ICA Client is 13.10 (32 bit version required)

VMWare Horizon Client is 4.8 (32 bit version required)

For Ubuntu

ICA Client V–13.3.0.344519 or later 13.3 versions

VMware Horizon View Client V–4.0.1-3698616

Cisco Unified Communications client on the hosted virtual desktop: Cisco Jabber for Windows

Cisco Jabber for Windows 12.5 running on the hosted virtual desktop (HVD).

Cisco Jabber Softphone for VDI is compatible with all future 12.5(X) Cisco Jabber for Windows versions.

For complete information about virtual environment compatibility, see the Jabber installation documentation for your release.

Cisco Unified Communications Manager

Recommended CUCM Release 11.5(1)SU3 or later

Minimum CUCM Release 10.5

Accessories

For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com .

A connection broker is software that creates connections to hosted virtual desktops. A connection broker performs a number
                                    of tasks that include

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

The Citrix Receiver or VMware Horizon Client provides a user interface for the corresponding connection broker.

(PCoIP only)

## Considerations for Thin Clients

Thin clients must meet all system requirements. For more information, see Release Notes for Cisco Jabber Softphone for VDI —HP Thin Pro and Ubuntu for your release.

### HP Thin Pro

HP Device Manager is the recommended deployment tool to deploy Virtualization Experience Media Edition to HP Thin Pro-based
                              thin clients.

Cisco does not support any management administrative method to deploy Cisco Jabber Softphone for VDI to HP Thin Pro-based thin clients. Support for adding and enabling add-ons is provided by HP, using HP Device Manager or
                                          other methods supported by HP.

## Port Requirements

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
                                          in a nonfunctional deployment. Only the components and requirements listed in the table are supported. |
|---|---|

| Component | Requirements |
|---|---|
| HP Thin Pro thin clients—Hardware | The following client hardware is supported with HP Thin Pro 6.2: HP t520 HP t530 HP t620 HP t630 HP t730 HP mt21 The following client hardware is supported with HP Thin Pro 7: HP t430 HP t520 HP t530 HP t630 HP t730 HP mt21 |
| HP ThinPro platform image | HP ThinPro 6.2: T7X62022 HP ThinPro 7: T7X70015 Support is limited for HP Thin Pro 7. |
| Ubuntu thin clients—Hardware | The following hardware is supported with Ubuntu 14.04 32b LTS: Installed RAM 2 GB Free Physical Memory 256 MB Free Disk Space 256 MB CPU: AMD G-T56N 1.65Ghz, or Intel Core2Duo T7500 2.2 GHz USB 2.0 for USB camera and audio devices |
| Ubuntu | Ubuntu 14.04 i386 Ubuntu 16.04 i386 Support is limited for Ubuntu 16.04. |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 32 bit Microsoft Windows 7 64 bit Microsoft Windows 8 32 bit Microsoft Windows 8 64 bit Microsoft Windows 8.1 32 bit Microsoft Windows 8.1 64 bit Microsoft Windows 10 32 bit Microsoft Windows 10 64 bit |
| Connection broker for the hosted virtual desktop 1 | Citrix XenDesktop 6.5, 7.5, and later 7.x versions Citrix XenApp 6.5, 7.5, and later 7.x versions—Published desktops only VMware Horizon 6.0 (with View)—Published desktops only VMware Horizon 6 version 6.1.0, 6.2.0, 7.0 and later 7.x versions—Published desktops only Citrix XenApp Published Application is not supported with Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu. |
| Citrix Receiver or VMware Horizon Client 2 (Installed on the thin client) | For HP Thin Pro 6.2.0 The HP Thin Pro image includes Citrix and VMware: ICA Client: 13.5.0 or later (32 bit version required) VMware 4.4.0 or later (32 bit version required) For HP Thin Pro 7 ICA Client is 13.10 (32 bit version required) VMWare Horizon Client is 4.8 (32 bit version required) For Ubuntu ICA Client V–13.3.0.344519 or later 13.3 versions VMware Horizon View Client V–4.0.1-3698616 |
| Cisco Unified Communications client on the hosted virtual desktop: Cisco Jabber for Windows | Cisco Jabber for Windows 12.5 running on the hosted virtual desktop (HVD). Cisco Jabber Softphone for VDI is compatible with all future 12.5(X) Cisco Jabber for Windows versions. For complete information about virtual environment compatibility, see the Jabber installation documentation for your release. |
| Cisco Unified Communications Manager | Recommended CUCM Release 11.5(1)SU3 or later Minimum CUCM Release 10.5 |
| Accessories | For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html . Important Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com . | Important | Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com . |
| Important | Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com . |

| Important | Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com . |
|---|---|

| Important | Cisco does not support any management administrative method to deploy Cisco Jabber Softphone for VDI to HP Thin Pro-based thin clients. Support for adding and enabling add-ons is provided by HP, using HP Device Manager or
                                          other methods supported by HP. |
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