---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-04b2f689e6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_011.html
retrieved_at: 2026-08-16T18:22:01.873766+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: Collaboration Deployment Models for IPv6

## Chapter: Collaboration Deployment Models for IPv6

# Collaboration Deployment Models for IPv6

## Collaboration Deployment Models for IPv6 Overview

This chapter describes the deployment models you can use with IPv6 in Cisco Collaboration networks. Cisco Unified Communications
                           Manager (Unified CM) supports the following traditional IPv4 deployment model examples:

Single-site deployments

Multi-site WAN deployments with distributed call processing

Multi-site deployments with centralized call processing and Cisco Unified Survivable Remote Site Telephony (Unified SRST)

With all of these deployment models, IPv6 endpoints should be configured as IPv6 with a preference of IPv6 for signaling and
                           media. This configuration maximizes the amount of IPv6 traffic with the use of media termination points (MTPs) for conversions
                           between IPv4 and IPv6.

## Single-Site Deployments

An enterprise would typically deploy the single-site model over a LAN or metropolitan area network (MAN), which carries the
                           voice, video, and IM traffic within the site. In this model, calls beyond the LAN or MAN use the public switched telephone
                           network (PSTN).

The characteristics and benefits of the IPv6 single-site model are the same as for IPv4 single-site deployments, as described
                           in the Cisco Collaboration Solution Reference Network Design (SRND), available at Link . The IPv6 single-site model includes the additional IPv6-only endpoints and dual stack application servers' product capabilities
                           and features discussed throughout this document. As shown in Supported IPv6 Addressing Modes ,

### Best Practices for IPv6 Single-Site Deployments

Single-site IPv6 deployments can contain a mixture of IPv4 and IPv6 devices. Phones can be configured as:

IPv4-only

IPv6 only

One or more ISDN PSTN gateways can be deployed in a single-site deployment.

Both the Unified CM SIP trunk and Cisco IOS SIP gateway should be configured as follows:

IPv6-only stack

ANAT disabled

To use IPv6 for signaling and media is to maximize the amount of IPv6 traffic.

The Unified CM SIP trunk and the SIP gateway can be configured to use:

SIP Delayed Offer (With MTP Required unchecked, although MTPs may be inserted dynamically for some calls for conversions between IPv4 and IPv6 addresses.)

SIP Early Offer IPv6-only trunk is not supported.

If a single IPv6 gateway is used and the cluster-wide preference for media is set to IPv6, an MTP is used for all calls to
                                 IPv4-only devices to convert from IPv4 to IPv6 protocol. If the widespread use of MTPs is not acceptable in the single-site
                                 deployment, configure two PSTN gateways instead of just one. Configure one as IPv4-only SIP gateway using SIP Delayed Offer
                                 as described above, and the other as a standard IPv6-only gateway. Calling search spaces and partitions can then be used to
                                 direct PSTN calls from IPv4-only and IPv6-only devices to their respective gateways.

For specific device configuration options and preferences, refer to the chapters on Trunks , and Collaboration Endpoints .

### The Campus LAN

If the campus LAN also includes Layer 3 routing devices, configure these devices to support dual-stack (IPv4 and IPv6) routing.
                              IPv6-only stack is not supported.

If a single PSTN gateway (as previously described) is used in this deployment model, then all Layer 3 LAN routing devices
                                          must be configured as dual-stack. If two gateways are used (one IPv6-only and one IPv4-only), then the portions of the network
                                          that contain IPv4-only devices do not have to be configured for dual-stack routing.

## Multi-Site WAN Deployments with Distributed Call Processing

The model for a multi-site WAN deployment with distributed call processing consists of multiple independent sites, each with
                              its own call processing cluster connected to an IP WAN that carries voice traffic between the distributed sites.

Each site in the distributed call processing model can be one of the following:

A single site with its own call processing agent, which can be either a:

Dual-stack (IPv4 and IPv6) Cisco Unified Communications Manager (Unified CM)

Standard (IPv4-only) Cisco Unified Communications Manager (Unified CM)

Standard (IPv4-only) Cisco Unified Communications Manager Express (Unified CME)

Other IP PBX:

A standard (IPv4-only) centralized call processing site and all of its associated remote sites

A legacy PBX with Voice over IP (VoIP) gateway (IPv4-only or IPv6-only)

For dual-stack (IPv4 and IPv6) sites, the devices can be configured as either IPv4-only or IPv6-only. This configuration maximizes
                              the amount of IPv6 traffic with the use of MTPs for conversions between IPv4 and IPv6 addresses.

The characteristics and benefits of an IPv6 multi-site WAN deployment with distributed call processing are the same as those
                              for IPv4 multi-site WAN deployments with distributed call processing, as described in the Cisco Collaboration System Solution
                              Reference Network Design (SRND), available at Link . The IPv6 multi-site model includes the additional IPv6-only and IPv6-only product capabilities and features discussed in
                              this document.

### Best Practices: Multi-Site WAN Deployments with Distributed Call Processing

A multi-site WAN deployment with distributed call processing has many of the same requirements as a single site. Follow the
                                 best practices from the single site model in addition to the ones listed here for the distributed call processing model.

IPv6 Unified CM clusters in multi-site WAN deployments with distributed call processing can use IPv6-only enabled SIP Delayed
                                 Offer intercluster trunks to connect to other IPv6 Unified CM clusters. However, for intercluster trunk connections to IPv4-only
                                 Unified CM clusters, we recommend using IPv4 SIP trunk delayed offer, not IPv6 intercluster trunks.

If IPv6-enabled SIP intercluster trunks are used, the WAN must support dual-stack (IPv4 and IPv6) routing.

Configure the Unified CM SIP intercluster trunks as follows:

IPv6-only or IPv4-only.

With ANAT disabled.

To use IPv6 for signaling and media is to maximize the amount of IPv6 traffic.

Configure the Unified CM SIP intercluster trunk to use:

SIP Delayed Offer with MTP Required unchecked. Although MTPs may be inserted dynamically for some calls for conversions between IPv4 and IPv6 addresses.

SIP IPv6-only trunk Early Offer with MTP Required checked and used for every call is not supported.

For specific device configuration options and preferences, refer to Trunks , and Collaboration Endpoints .

## Multi-Site Deployments with Centralized Call Processing and Unified SRST

In this call processing deployment model, endpoints can be located remotely from the call processing service (Unified CM cluster),
                              across a QoS-enabled Wide Area Network (WAN). Due to the limited quantity of bandwidth available across the WAN, call admission
                              control is required to manage the number of calls admitted on any given WAN link, to keep the load within the limits of the
                              available bandwidth. On-net communication between the endpoints traverses either a LAN/MAN (when endpoints are located in
                              the same site) or a WAN (when endpoints are located in different sites). Communication outside the enterprise goes over an
                              external network such as the PSTN, through a gateway that is typically co-located with the endpoint.

The IP WAN also carries call control signaling between the central site and the remote sites. The following figure illustrates
                              a typical centralized call processing deployment, with a Unified CM cluster as the call processing agent at the central site
                              and an IP WAN to connect all the sites.

For IPv6-enabled multi-site centralized call processing deployments, the centralized Unified CM cluster is enabled for IPv4
                              and IPv6. Each site may be configured as dual-stacks or IPv4-only. For dual-stack (IPv4 and IPv6) sites, IPv6 devices should
                              be configured as IPv6-only with a preference of IPv6 for signaling and media. This configuration maximizes the amount of IPv6
                              traffic using MTPs for conversions between IPv4 and IPv6 addresses.

The characteristics and benefits of an IPv6 multi-site centralized call processing deployment are the same as for IPv4 multi-site
                              centralized call processing deployments, as described in the Cisco Collaboration System Solution Reference Network Design (SRND) , available at Link . However, the IPv6 multi-site centralized call processing deployment model includes the additional IPv6-only product capabilities
                              and features discussed in this document.

### Best Practices: Multi-Site Deployments with Centralized Call Processing

IPv6 multi-site deployments with centralized call processing can contain sites with a mixture of traditional IPv4 and IPv6
                                 devices. In each IPv6-enabled site, follow the best practices from the single-site model in addition to the ones listed here
                                 for the centralized call processing model.

You can configure phones as:

IPv4-only

IPv6-only

The IP WAN in IPv6 multi-site deployments with centralized call processing must support dual-stack (IPv4 and IPv6) routing.

Unified SRST routers at remote sites support IPv6-only or IPv4-only IP Phones in SRST mode. These SRST routers revert to original
                                 mode when the Unified CM cluster is restored. They operate in IPv6-only mode.

## Call Admission Control

For multi-site deployments with distributed or centralized call processing, use locations-based call admission control and
                           a WAN based on either Multiprotocol Label Switching (MPLS) or a hub-and-spoke topology. For more information on call admission
                           control, refer to the Cisco Collaboration System Solution Reference Network Design (SRND), available at Link .

## Intra-Cluster Communications

All intra-cluster server-to-server communications, such as Intra-Cluster Communication Signaling (ICCS) traffic, database
                           traffic, and firewall management real-time traffic, use IPv4-only.

## Clustering Over the WAN

We have clustering over the WAN with dual-stack Unified Communications Manager clusters, where IPv4 is used for intra-cluster
                           communication such as ICCS and IPv6 is used for inter-cluster communication over SIP trunks.

## Call Detail Records and Call Management Records

Call detail records (CDR) and call management records (CMR), when enabled, are collected by each subscriber server and are
                           uploaded periodically to the publisher server, which stores the records in the CDR Analysis and Reporting (CAR) database.
                           CDR and CMR collect and store both IPv4 and IPv6 addresses. These servers interface with IPv4 addresses that are IPv6-aware.

| Note | SIP Early Offer IPv6-only trunk is not supported. |
|---|---|

| Note | If a single PSTN gateway (as previously described) is used in this deployment model, then all Layer 3 LAN routing devices
                                          must be configured as dual-stack. If two gateways are used (one IPv6-only and one IPv4-only), then the portions of the network
                                          that contain IPv4-only devices do not have to be configured for dual-stack routing. |
|---|---|

| Note | If IPv6-enabled SIP intercluster trunks are used, the WAN must support dual-stack (IPv4 and IPv6) routing. |
|---|---|

| Note | SIP IPv6-only trunk Early Offer with MTP Required checked and used for every call is not supported. |
|---|---|