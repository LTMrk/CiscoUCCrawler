---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-0eb87cf075
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_01000.html
retrieved_at: 2026-08-16T18:22:23.095910+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: Call Processing and Call Admission Control

## Chapter: Call Processing and Call Admission Control

# Call Processing and Call Admission Control

## Call Processing and Call Admission Control Overview

This chapter discusses aspects of call processing and call admission control that apply specifically to IPv6.

## Call Processing

This section describes a few changes to call processing operation for IPv6, along with some IPv6 configuration information.
                           For information on designing scalable and resilient call processing systems with Cisco Unified Communications Manager (Unified
                           CM), refer to the Cisco Collaboration System Solution Reference Network Design (SRND), available at Link .

### Enable Call Processing for IPv6

To enable call processing for IPv6, you must first enable IPv6 throughout the Cisco Unified Communications Manager (Unified
                                 CM) cluster, as outlined in the following steps:

Configure IPv6 on each server in the Unified CM cluster, either through the server operating system (OS) command line interface
                                       (CLI) or through the Cisco Unified Operating System Administration graphical user interface (GUI).

Configure IPv6 in Cisco Unified CM Administration.

#### Configure IPv6 on Each Server in Cluster Using CLI

Step 1

Enable IPv6 by using the set network ipv6 service enable command.

Step 2

Set a static IPv6 address for your server by using the set network ipv6 static_address <addr> <mask> command.

Step 3

To view the platform's IPv6 address settings, use the show network ipv6 settings command. Example output from this command is as follows:

```
IPv6 : enabled
DHCPv6 : disabled
IPv6 addresses:
Address:2001:db8:c18:1:21c:c4ff:feef:ca0 Mask:64
Scope:Global Duplicate:no
Address:fe80::21c:c4ff:feef:ca0 Mask:64
Scope:Link
```

#### Configure Unified CM Server IPv6 Address Using GUI

To set the address, select Settings > IP > Ethernet IPv6 .

The following figure shows how to configure the IPv6 address of the server platform by using the Cisco Unified Operating System
                                                Administration GUI.

#### Define Unified CM Server IPv6 Addresses

After you configure the server platform IPv6 address, define the IPv6 address for each Unified CM server by using Cisco Unified
                                    CM Administration. Select System > Server , and enter the IPv6 address in the IPv6 Name field. This IPv6 address allows IP phones to retrieve the IPv6 address of this Unified CM from the configuration file downloaded
                                    from the TFTP server.

### Cluster-Wide IPv6 Configuration

You can configure the following cluster-wide IPv6 settings for each Unified CM server through the Enterprise Parameters page
                                 for IPv6 and IPv6 for Phones in Unified CM Administration:

Enable IPv6 (Set to True )

IP Addressing Mode Preference for Media (Set to IPv6 )

IP Addressing Mode Preference for Signaling (Set to IPv6 )

Allow Auto-Configuration for Phones (Set to On )

#### Enable IPv6

Set this parameter to True to enable IPv6. The default setting is False.

#### IP Addressing Mode Preference for Media

This parameter has two setting options:

IPv4 (Default)

IPv6 (Set to IPv6 )

This cluster-wide IP Addressing Mode Preference for Media is different than the device-level IP addressing mode, and it serves
                                 two purposes:

The cluster-wide Addressing Mode Preference for Media is used to select which IP addressing version to use for media when
                                       a call is made between two dual-stack devices.

The cluster-wide Addressing Mode Preference for Media is also used when there is a mismatch in supported IP addressing versions
                                       between two devices. If an IPv6-only device calls an IPv4-only device, an MTP must be inserted into the media path to convert
                                       between IPv4 and IPv6. Typically both devices will have MTP media resources available to them in their media resource group
                                       (MRG). The cluster-wide Addressing Mode Preference for Media determines which device's MTP is used to convert between IPv4
                                       and IPv6 for the call.

MTP resource allocation is discussed in detail in Media Resources and Music on Hold Overview .

#### IP Addressing Mode Preference for Signaling

The cluster-wide IP Addressing Mode Preference for Signaling setting is used by devices whose IP Addressing Mode Preference
                                 for Signaling is set to Use System Default . The cluster-wide IP Addressing Mode Preference for Signaling has two setting options:

IPv4 (Default)

IPv6 (Set to IPv6 )

#### Allow Auto-Configuration for Phones

The cluster-wide setting of Allow Auto-Configuration for Phones is used by phones whose Allow Auto-Configuration for Phones
                                 parameter is set to Default . Allow Auto-Configuration for Phones has two settings:

On (Default)

Off

#### Intra-Cluster Communications

There are two primary types of intra-cluster communications, database replication and Intra-Cluster Communication Signaling
                                    (ICCS), both of which support IPv4-only.

#### TFTP Server

Within any Unified CM system, endpoints such as IP phones rely on a TFTP process to acquire configuration files, software
                                    images, and other endpoint-specific information. The Cisco TFTP service is a file serving system that can run on one or more
                                    Unified CM servers. It builds configuration files and serves firmware files, ringer files, device configuration files, and
                                    so forth, to endpoints.

When IPv6 is enabled in the Unified CM cluster, the TFTP server inherits its IPv6 server address from the configured server
                                    address. This allows the TFTP server to serve files to devices using IPv6 signaling.

#### Unified CM CTI

Computer Telephony Integration (CTI) provides IP address information through the JTAPI and TAPI interfaces, which can support
                                    IPv4 and IPv6 addresses. To support IPv6, applications need to use a JTAPI/TAPI client interface version that supports IPv6.

#### Unified CM AXL/SOAP

Unified CM's Administrative XML (AXL) Simple Object Access Protocol (SOAP) interface is IPv6-aware. The AXL/SOAP interface
                                    communicates with IPv4 addresses, but it can receive and understand IPv6 addresses embedded in application protocol data units
                                    (PDUs).

#### SNMP

Simple Network Management Protocol (SNMP) for Unified CM includes:

SNMPv6 MIB support.

Ability to accept SNMP requests from v6-only hosts.

Ability to configure v6-only SNMP Notification Destination.

IPv6 support for SNMP V1/V2C/V3 protocols.

#### Cisco Collaboration Applications

#### Unified CM Platform Capacity Planning

IPv6 addresses require more Unified CM server memory when compared with IPv4 addresses. Therefore, in a Unified CM deployment
                                    with many IPv6 devices, the busy hour call completion (BHCC) capacity is approximately 3% to 5% less than the capacity of
                                    IPv4-only deployments.

#### Interoperability of Unified CM and Unified CM Express

Cisco Unified Communications Manager Express (Unified CME) supports IPv4-only. If you are deploying Unified CME with Unified
                                    CM, the interface is IPv4-only. Follow the design guidance in the Cisco Collaboration System Solution Reference Network Design (SRND) , available at Link .

## Call Admission Control (CAC)

IPv6-enabled Unified CM supports single-site deployments, multi-site WAN deployments with distributed call processing, and
                              multi site deployments with centralized call processing. Call admission control is required where calls are made over a WAN
                              between remote sites on the same cluster or between Unified CM clusters.

### Call Admission Control with Unified Communications IPv6 Deployments

Collaboration IPv6 deployments with Unified CM support locations-based topology-unaware call admission control only for calls
                                 between remote sites in the same cluster and over intercluster trunks. Topology-unaware call admission control requires the
                                 WAN to be hub-and-spoke, or a spokeless hub in the case of a Multiprotocol Label Switching (MPLS) virtual private network
                                 (VPN). This topology ensures that call admission control, provided by the locations configuration mechanism in Unified CM,
                                 works properly in tracking the bandwidth available between any two sites in the WAN. For general guidance on topology-unaware
                                 call admission control, refer to the Cisco Collaboration System Solution Reference Network Design (SRND) , available at Link .

Topology-aware Resource Reservation Protocol (RSVP) cannot be used within the cluster or between clusters as a call admission
                                 control technique. For IPv6-enabled Unified CM clusters:

Locations-based call admission control must be used between sites controlled by the same Unified CM cluster.

Unified CM SIP trunks support only locations-based call admission control (IPv4 and/or IPv6).

Unified CM MGCP trunks support only locations-based call admission control (IPv4-only).

Unified CM H.323 trunks support locations-based call admission control and gatekeeper-controlled call admission (IPv4-only).

For IPv6 traffic, Unified CM uses the values shown in Table 1 in its locations-based call admission control algorithm.

### Locations-Based Call Counting Call Admission Control

Unified CM also supports a type of locations-based, topology-unaware call admission control known as call counting. Less sophisticated
                                 than standard Unified CM locations-based call admission control, call counting uses a fixed bandwidth value for each voice
                                 and video call, irrespective of the codec or actual bandwidth used.

For call counting, the following default values are used for Layer 3 voice and video bandwidth when calculating the amount
                                 of available bandwidth at a location:

Voice calls = 102 kbps

Video calls = 500 kbps

Although call counting provides a simplified form of call admission control, it also has the disadvantage that bandwidth reserved
                                 for voice and video in the WAN might not be used efficiently.

To enable call counting in Unified CM Administration, select Service Parameters > Clusterwide Parameters (Call Admission Control) . The default setting for Call Counting CAC Enabled is False. The voice and video bandwidth values for call counting are configurable.

| Step 1 | Enable IPv6 by using the set network ipv6 service enable command. |
|---|---|
| Step 2 | Set a static IPv6 address for your server by using the set network ipv6 static_address <addr> <mask> command. |
| Step 3 | To view the platform's IPv6 address settings, use the show network ipv6 settings command. Example output from this command is as follows: IPv6 : enabled
DHCPv6 : disabled
IPv6 addresses:
Address:2001:db8:c18:1:21c:c4ff:feef:ca0 Mask:64
Scope:Global Duplicate:no
Address:fe80::21c:c4ff:feef:ca0 Mask:64
Scope:Link |

| To set the address, select Settings > IP > Ethernet IPv6 . The following figure shows how to configure the IPv6 address of the server platform by using the Cisco Unified Operating System
                                                Administration GUI. Figure 1. Configuring the Server Platform IPv6 Address in Cisco Unified Operating System Administration |
|---|