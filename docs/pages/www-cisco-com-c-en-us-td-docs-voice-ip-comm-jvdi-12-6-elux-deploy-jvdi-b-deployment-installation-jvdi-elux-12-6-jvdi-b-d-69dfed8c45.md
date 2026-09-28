---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-6-elux-deploy-jvdi-b-deployment-installation-jvdi-elux-12-6-jvdi-b-d-69dfed8c45
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_6/elux/deploy/jvdi_b_deployment-installation-jvdi-elux-12-6/jvdi_b_deployment-installation-jvdi-elux-12-6_chapter_01.html
retrieved_at: 2026-08-22T00:36:33.268889+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.6

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.6

Updated: April 9, 2019

Chapter: Requirements

## Chapter: Requirements

# Requirements

## Requirements

Each of the components listed in the following table must meet the requirements. Use of unsupported components can result
                                          in a nonfunctional deployment.

Only the components, versions, and minimum hardware requirements listed in the table are supported.

Component

Requirements

Unicon eLux thin clients—Hardware

The minimum hardware requirements for thin clients are:

1.6-GHz dual-core processor

2-GB RAM

The following client hardware was tested with eLux RP 5.7.0:

HP T620 Dual Core / Quad Core

HP T630 Dual Core / Quad Core

HP T730

Cisco VXC 6215

Dell Wyse Z50D

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

Citrix Virtual Apps and Desktops (formerly XenApp and XenDesktop) versions 6.x, 7.x–7 1811, and 7.15 LTSR—Published desktops
                                                only

VMware Horizon 6.0 (with View)—Published desktops only

VMware Horizon 6 versions 6.x–7.7—Published desktops only

Published Application is not supported with Cisco Jabber Softphone for VDI for Unicon eLux.

Citrix Workspace app or

VMware Horizon Client

(Installed on the thin client)

Unicon eLux 5.7 (eLuxRP-5.7.2000_AllPackages-1)

Unicon eLux contains the required Citrix and VMware versions.

The eLux package is available from Unicon eLux. For assistance locating the download, contact eLux support.

Cisco Unified Communications client on the hosted virtual desktop: Cisco Jabber for Windows.

Cisco Jabber for Windows 12.5 running on the hosted virtual desktop (HVD).

Cisco Jabber Softphone for VDI is compatible with all future 12.6(x) Cisco Jabber for Windows versions.

For complete information about virtual environment compatibility, see the Cisco Jabber documentation for your release.

Cisco Unified Communications Manager

Recommended CUCM Release 11.5(1)SU3 or later

Minimum CUCM Release 10.5

Cisco AnyConnect (Optional)

vpnsystem V4.5-1

Accessories

For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html .

Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com .

A connection broker is software that creates connections to hosted virtual desktops. A connection broker performs a number
                                    of tasks including the following:

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

The Citrix Workspace app or VMware Horizon Client provides a user interface for the corresponding connection broker.

## Considerations for Thin Clients

Unicon eLux thin clients must meet all system requirements. For more information, see Release Notes for Cisco Jabber Softphone for VDI —Unicon eLux for your release.

Unicon Scout Enterprise is the recommended deployment tool to deploy Cisco Jabber Softphone for VDI to Unicon eLux-based thin clients.

Cisco does not support any management administrative method to deploy Cisco Jabber Softphone for VDI to Unicon eLux-based thin clients. Support for adding and enabling add-ons is provided by Unicon, using Unicon Scout Enterprise
                                          or other methods supported by Unicon.

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
                                          in a nonfunctional deployment. Only the components, versions, and minimum hardware requirements listed in the table are supported. |
|---|---|

| Component | Requirements |
|---|---|
| Unicon eLux thin clients—Hardware | The minimum hardware requirements for thin clients are: 1.6-GHz dual-core processor 2-GB RAM The following client hardware was tested with eLux RP 5.7.0: HP T620 Dual Core / Quad Core HP T630 Dual Core / Quad Core HP T730 Cisco VXC 6215 Dell Wyse Z50D |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 32 bit Microsoft Windows 7 64 bit Microsoft Windows 8 32 bit Microsoft Windows 8 64 bit Microsoft Windows 8.1 32 bit Microsoft Windows 8.1 64 bit Microsoft Windows 10 32 bit Microsoft Windows 10 64 bit |
| Connection broker for the hosted virtual desktop 1 | Citrix Virtual Apps and Desktops (formerly XenApp and XenDesktop) versions 6.x, 7.x–7 1811, and 7.15 LTSR—Published desktops
                                                only VMware Horizon 6.0 (with View)—Published desktops only VMware Horizon 6 versions 6.x–7.7—Published desktops only Published Application is not supported with Cisco Jabber Softphone for VDI for Unicon eLux. |
| Citrix Workspace app or VMware Horizon Client 2 (Installed on the thin client) | Unicon eLux 5.7 (eLuxRP-5.7.2000_AllPackages-1) Unicon eLux contains the required Citrix and VMware versions. The eLux package is available from Unicon eLux. For assistance locating the download, contact eLux support. |
| Cisco Unified Communications client on the hosted virtual desktop: Cisco Jabber for Windows. | Cisco Jabber for Windows 12.5 running on the hosted virtual desktop (HVD). Cisco Jabber Softphone for VDI is compatible with all future 12.6(x) Cisco Jabber for Windows versions. For complete information about virtual environment compatibility, see the Cisco Jabber documentation for your release. |
| Cisco Unified Communications Manager | Recommended CUCM Release 11.5(1)SU3 or later Minimum CUCM Release 10.5 |
| Cisco AnyConnect (Optional) | vpnsystem V4.5-1 |
| Accessories | For a complete listing of supported audio and video accessories, see Unified Communications Endpoint and Client Accessories , at http://www.cisco.com/c/en/us/products/unified-communications/uc_endpoints_accessories.html . Important Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com . | Important | Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com . |
| Important | Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com . |

| Important | Ensure that all Jabra devices are running the latest firmware. You can use Jabra Direct to update the firmware. For more information
                                                      visit: http://www.jabra.com . |
|---|---|

| Important | Cisco does not support any management administrative method to deploy Cisco Jabber Softphone for VDI to Unicon eLux-based thin clients. Support for adding and enabling add-ons is provided by Unicon, using Unicon Scout Enterprise
                                          or other methods supported by Unicon. |
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