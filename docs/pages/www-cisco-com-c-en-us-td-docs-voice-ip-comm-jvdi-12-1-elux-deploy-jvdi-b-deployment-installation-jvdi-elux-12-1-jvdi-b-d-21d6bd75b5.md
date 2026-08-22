---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-1-elux-deploy-jvdi-b-deployment-installation-jvdi-elux-12-1-jvdi-b-d-21d6bd75b5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_1/elux/deploy/jvdi_b_deployment-installation-jvdi-elux-12-1/jvdi_b_deployment-installation-jvdi-elux-12-1_chapter_01.html
retrieved_at: 2026-08-22T00:37:27.792153+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.1

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.1

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

Unicon eLux thin clients—Hardware

The minimum hardware requirements for thin clients are:

1.6-GHz dual-core processor

2-GB RAM

The following client hardware was tested with eLux RP 5.2.0, RP 5.3.0, RP 5.5.0, RP 5.5.1, and RP 5.7.0:

HP T620 Dual Core / Quad Core

HP T630 Dual Core / Quad Core

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

Citrix XenDesktop 6.5, 7.5, and later 7.x versions

Citrix XenApp 6.5, 7.5, and later 7.x versions—Published desktops only

VMware Horizon 6.0 (with View)—Published desktops only

VMware Horizon 6 version 6.1.0, 6.2.0, 7.0 and later 7.x versions—Published desktops only

Citrix XenApp Published Application is not supported with Cisco Jabber Softphone for VDI for Unicon eLux.

Citrix Receiver or

VMware Horizon Client

(Installed on the thin client)

Unicon eLux contains the required Citrix Receiver and VMware Horizon Client.

For Unicon eLux 5.2.0

ICA Client V13.3.0.1-9 and later 13.x versions

VMware Horizon View Client V5.7.1.1-3 and later 5.x versions

For Unicon eLux 5.3.0, 5.5.0, 5.5.1, and 5.7.0

ICA Client V13.3.9.1-13 and later 13.x versions

VMware Horizon View Client V6.0.0.3-1 and later 6.x versions

Cisco Unified Communications client on the hosted virtual desktop:

Cisco Jabber for Windows or Cisco UC Integration™ for Microsoft Lync .

Cisco Jabber for Windows 12.1 running on the hosted virtual desktop (HVD).

Cisco Jabber Softphone for VDI is compatible with all future 12.1(x) Cisco Jabber for Windows versions.

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
                                    of tasks that include

Validating the username and providing a connection for the user.

Allowing the user to connect to a specific virtual desktop.

The Citrix Receiver or VMware Horizon Client provides a user interface for the corresponding connection broker.

(PCoIP only)

## Considerations for Thin Clients

Unicon eLux thin clients must meet all system requirements. For more information, see Release Notes for Cisco Jabber Softphone for VDI —Unicon eLux for your release.

Unicon Scout Enterprise is the recommended deployment tool to deploy Cisco Jabber Softphone for VDI to Unicon eLux-based thin clients.

Cisco does not support any management administrative method to deploy Cisco Jabber Softphone for VDI to Unicon eLux-based thin clients. Support for adding and enabling add-ons is provided by Unicon, using Unicon Scout Enterprise
                                          or other methods supported by Unicon.

## Port Requirements

The following table lists the ports or port ranges used by Cisco Jabber Softphone for VDI .

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
| Unicon eLux thin clients—Hardware | The minimum hardware requirements for thin clients are: 1.6-GHz dual-core processor 2-GB RAM The following client hardware was tested with eLux RP 5.2.0, RP 5.3.0, RP 5.5.0, RP 5.5.1, and RP 5.7.0: HP T620 Dual Core / Quad Core HP T630 Dual Core / Quad Core Cisco VXC 6215 Dell Wyse Z50D |
| Hosted virtual desktop OS (server-side) | Microsoft Windows 7 32 bit Microsoft Windows 7 64 bit Microsoft Windows 8 32 bit Microsoft Windows 8 64 bit Microsoft Windows 8.1 32 bit Microsoft Windows 8.1 64 bit Microsoft Windows 10 32 bit Microsoft Windows 10 64 bit |
| Connection broker for the hosted virtual desktop 1 | Citrix XenDesktop 6.5, 7.5, and later 7.x versions Citrix XenApp 6.5, 7.5, and later 7.x versions—Published desktops only VMware Horizon 6.0 (with View)—Published desktops only VMware Horizon 6 version 6.1.0, 6.2.0, 7.0 and later 7.x versions—Published desktops only Citrix XenApp Published Application is not supported with Cisco Jabber Softphone for VDI for Unicon eLux. |
| Citrix Receiver or VMware Horizon Client 2 (Installed on the thin client) | Unicon eLux contains the required Citrix Receiver and VMware Horizon Client. For Unicon eLux 5.2.0 ICA Client V13.3.0.1-9 and later 13.x versions VMware Horizon View Client V5.7.1.1-3 and later 5.x versions For Unicon eLux 5.3.0, 5.5.0, 5.5.1, and 5.7.0 ICA Client V13.3.9.1-13 and later 13.x versions VMware Horizon View Client V6.0.0.3-1 and later 6.x versions |
| Cisco Unified Communications client on the hosted virtual desktop: Cisco Jabber for Windows or Cisco UC Integration™ for Microsoft Lync . | Cisco Jabber for Windows 12.1 running on the hosted virtual desktop (HVD). Cisco Jabber Softphone for VDI is compatible with all future 12.1(x) Cisco Jabber for Windows versions. For complete information about virtual environment compatibility, see the Cisco Jabber documentation for your release. |
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