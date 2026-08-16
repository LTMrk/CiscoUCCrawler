---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-7af4b6fb61
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_00.html
retrieved_at: 2026-08-16T18:21:41.521955+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: IPv6 Introduction

## Chapter: IPv6 Introduction

# IPv6 Introduction

## Documentation Changes

Date

Change

Link to Topic

October 2024

Updated the section "IPv6-only Supported and Not Supported Features". Moved "EMCC" from "IPv6-only Supported Features" to
                                          "IPv6-only Not Supported Features" as it is concluded that IPv6-only device profile login for EMCC is not supported.

Included "Support for Catalyst 8000 Series Edge Platforms" in the section "Supported IPv6 Addressing Modes".

November 2023

The entire guide is updated. The following are the updates to the guide. A few to mention -

Table 8 is updated.

Deleted “for DOD Network only”

Replaced “Recommended” to “Supported”

Removed “CSR 12” and “CSR 14” references

Removed release numbers across the guide to keep it generic

Removed occurrences of “Solution Tested”

Deleted all Deployment Gaps and created a new list

Jabber on IPv6, Expressway-E external on IPv6, Expressway-E internal interface on IPv4, UCM, IM&P, CUC on IPv4 are supported
                                                deployments

Dual-stack: Used for application servers, such as Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder,
                                                and Cisco Unified Survivable Remote Site Telephony (Unified SRST)

Table 8 and Table 10: Titles “Supported” instead of “Recommended”, remove “Solution Tested" column

Note: IPv6 NAT-based solution is not supported

DHCP v6 modify the text accordingly

MRA: Jabber on IPv6, Expressway-E external on IPv6, Expressway-E internal interface on IPv4, UCM, IM&P, CUC on IPv4 are supported
                                                deployments

The SIP Trunk configuration settings discussed in this section are applied through the Common Device Configuration profile
                                                that is created and assigned to the SIP trunk (IP Addressing Mode and IP Addressing Mode Preference for Signaling), and through
                                                the SIP Profile configuration assigned to the SIP trunk (Enable ANAT should be disabled). Change “Enable ANAT should be disabled”.
                                                This is confusing. Instead, mentioned "ANAT is not enabled."

Removed the following from ANAT section:

Media Selection for Outbound Early Offer Calls with ANAT

Media Selection for Inbound Early Offer Calls with ANAT

Media Selection for Delayed Offer Calls Over Unified CM SIP Trunks with ANAT

Media Selection for Outbound Delayed Offer Calls with ANAT

Inbound Delayed Offer Calls with ANAT

Inbound Delayed Offer Calls with ANAT and Supported: sdp anat

Inbound Delayed Offer Calls with ANAT and Require: sdp-anat

Included this: The SIP trunk uses either the Unified CM IPv4 address or the Unified CM IPv6 address for signaling, and an
                                                MTP. We recommend IPv6 Only for production environments.

Removed the media part. Instead mentioned, MTP or other trunk address for media.

Modified to: Outbound SIP best effort early offer (without MTP/TRP) in SIP trunk as we don’t support in IPv6 mode.

Removed this Note: In CSR 12.0, SIP Early Offer does not support IPv6. CUBE or Unified SRST gateways will not support ANAT.

The following changes are made to the section "IPv6-Only Phones":

Existing content is removed. Replaced with the following:

IPv6 only Supported Features: Mobility – MVA/IVR, CAPFv3, TVS and TFTP, Extension Mobility, EMCC, SRST, SIP GW, SIP Route
                                                      Pattern, Barge, Intercom, Phone NTP Reference, Device Mobility, Self Care Portal, Self Provisioning using with and without
                                                      IVR, Phone services - Corporate Directory, Missed Calls, Placed Calls, Intercom Calls, Personal Directory, Voicemail, Received
                                                      Calls, Web Dialer, Quality Report Tool (QRT), SNMPv6 MIB, Phone Config. download, CTI, IPVMS (Unicast MoH, software MTP, ANN,
                                                      Conference Bridge, IVR), CDR

IPv6-Only Not Supported Features

Best Effort Early Offer over SIP Trunk

External MoH, Multicast MoH, Video On Hold, Voicemail, Recording (BIB Recording, GW Recording), Enhanced E911

SSH, Cluster Manager, LDAP, Syslog Server/Alarm Library, Serviceability Applications - IPMA, RTMT

DRS, IPSec

Media Resources (IOS Xcoder/ hardware MTP/TRP)/Conference Bridge), Video conference resource (MCU/Conductor), FAX/ATA

MRA (Jabber in IPv6 and Expressway-E external interface in v6 and enterprise network in v4 is supported)

Silent Monitoring, Whisper Coaching, Agent Greeting, VG as analog line interface using SCCP (pending test)

Removed ISR 4000 references

IPv6 endpoints should be configured as IPv6 with preference

Dual Stack with preference IPv6

Removed "with no telephony services provided over an IP WAN."

Remove CSR 12.0

Addressed CDET "CSCwh69667"

Removed SRST 12.0

Table 8: Added row for "Cisco Room Series, Board Series, and Desk Series". All "Yes"

Change 7832 - "Yes"

Removed row Wi-Fi enabled devices: Cisco IP Phone 8861, 8865

The first row "Dual- Stacks: IPv4 and IPv6" is "Yes" for all 78xx and 88xx. Added the following phones to this row: 7811,
                                                7821, 7841, 7861

For 7832 and 8832: YES to Dual-Stack

For 7832 - "Yes" in 8861 all columns

Removed the entire row that says "Cisco Unified IP Phone 6901, 7945G, 7965G, 7975G …" It is End of Support

Removed "Cisco DX70 and DX80"

Removed row "Cisco TelePresence MX Series, SX Series"

Removed row "Cisco TelePresence System EX Series"

Removed row "Cisco Webex Share"

Remove row "Cisco IP Communicator"

Remove row Wi-Fi enabled devices: Cisco IP Phone 8861, 8865

Document direction

Removed "We recommend Stateful DHCP host configuration for both IPv4 or IPv6 IP phones."

Remove dual-stack IP Phones that require ANAT, which is not supported in Unified SRST call agents

Removed the "Security and IPv6 Traffic" section

Removed ISR 4000 G3

Include row for "Cisco Room Series, Board Series, and Desk Series". All "Yes"

Removed "Cisco ATA 190 Series Analog Telephone Adapters"

-

June 08, 2022

Updated the table "Table 9: Supported Addressing Modes Communication Gateways".

Table 9: Supported Addressing Modes for,Communication Gateways

April 01, 2021

Removed redundant topics from Call Processing and Call Admission Control chapter.

-

April 10, 2019

Changed book title to include Cisco Collaboration System Release.

-

April 30, 2018

Updated overview based on Cisco Collaboration Systems Release.

IPv6 Deployment Overview

Updated deployment gaps.

Deployment Recommendations for Enterprise Networks

Added a note about IPv6 multicast application.

IPv6 Multicast Addresses

Updated the supported IPv6 addressing modes for endpoints.

Added Cisco Meeting Server and Cisco TelePresence Management Suite.

Supported IPv6 Addressing Modes for Products

Updated the note.

IPv6 Bandwidth Provisioning

Added Cisco Meeting Server and Cisco TelePresence Management Suite in Video Conferencing section.

Added Multistream video section.

Updated Unified CM IM and Presence Service section to include dual-stack.

Applications Overview

Added:

Cisco TelePresence EX Series

Cisco Meeting Server

Cisco TelePresence Management Suite

Product Configuration Resources for IPv6

## IPv6 Deployment Overview

This document describes our recommendations on how to transition your Cisco Collaboration network design to use IPv6 in a
                           dual-stack (IPv4 and IPv6) environment.

This document does not describe how to implement IPv6 in the campus and WAN, but does refer you to other documents for those
                           details. It is assumed that data IPv6 desktop services are deployed first, for example internet access when Collaboration
                           IPv6 upgrade is initiated in a dual-stack mode.

Application Server Addressing Mode

All Collaborations applications servers are deployed in IPv4 and IPv6 stacks to support IPv4 or IPv6 devices and components.

Branch Office Addressing Mode

In Cisco Collaboration Systems Release, a branch office can be in one of the following IP addressing modes. A cluster can
                           support the following types of IP addressing modes and all can co-exist.

Traditional IPv4-only configuration where the LAN is IPv4-only or dual-stack.

IPv6-only configuration where the LAN is dual-stack.

Dual-stack sites that support IPv4 stack or IPv6 stack devices, where the LAN is dual-stack.

Provides IPv6-only site or branch offices that can have the following components:

Cisco Integrated Services Routers (ISR) Edge Routers

PSTN GW

SRST

Audio Conference

MTP

Endpoints

Video TP CE (Cisco DX Series, Cisco TelePresence MX, SX, and EX and Series)

Cisco IP Phone 7800 and 8800 Series

Conference IP Phone (8832)

On-premise Cisco Jabber (Jabber)

ATA FAX

We strongly recommend that you use this document with following guides that provide in-depth guidance on Collaboration deployments
                           using IPv4:

Cisco Collaboration System Solution Reference Network Design (SRND) , available at: Link .

Cisco Preferred Architecture for Enterprise Collaboration 11.6 Design Overview , available at: Link

Cisco Collaboration IPv6 transition follows the Cisco Preferred Architecture (PA) recommended deployment of IPv4 products:

Cisco Unified Communications Manager (Unified CM) is the call control server.

Cisco IP Phones, Jabber clients, and Cisco TelePresence video endpoints use SIP to register directly to Unified CM.

Unified CM cluster’s failover mechanism provides endpoint registration redundancy. If a WAN failure occurs, and endpoints
                                 at remote locations cannot register to Unified CM, they use SRST functionality for local and PSTN calls. However, some services
                                 such as Jabber presence might not be available.

As of Cisco Collaboration Systems Release, some default settings have not been adjusted for IPv6-only as a default, so follow
                                       the directions in this guide to ensure that you use the recommended settings for IPv6 deployment. Also some labels in the
                                       Admin Configuration UI have not been updated, but changes are noted in this document. For example, the Allow Auto-Configuration
                                       for Phones label has not been updated to Allow Stateless Auto-Configuration for Phones.

## Move Toward IPv6-Only Network

In Cisco Collaboration Systems Release, the deployment of IPv6-only stack devices reduces dependency on IPv4 addresses. For
                              all applications servers, emphasis is given to the deployment of dual-stack (IPv4 and IPv6) applications servers. Dual-stack
                              applications servers offer a greater degree of functionality and interoperability with existing traditional IPv4-only devices
                              that may not support IPv6-only stack because they are not developed.

The ultimate goal is for all collaboration endpoints, servers, and gateways to be configured as IPv6-only stack, meaning that
                              they can provide collaboration functions without using any IPv4 addresses and they do not require IPv4 to IPv6 media interworking
                              functions.

Scale of Deployment (Endpoints)

Servers and Gateways (Dual-stack or IPv4)

IPv4 Addresses Before Deploying IPv6-only Endpoints

IPv4 Addresses After Deploying IPv6-only Endpoints

Percent Reduction in IPv4 Addresses

500

6

506

6

98.8%

5,000

13

5,013

13

99.7%

10,000

25

10,025

25

99.8%

The scope of this document is limited to the solutions approved by Cisco. Supported IPv4-only stack applications are limited
                                          to those stated in this document. It is assumed that IP phones and gateways are configured with either an IPv4-only stack
                                          or IPv6-only stack using SIP signaling. Supported application servers support IPv4-only and IPv6-only stacks (dual-stack).
                                          Any applications that we did not develop or test are not supported by Cisco TAC. In IPv6 supported network configurations,
                                          Skinny Client Control Protocol (SCCP) for IP phones, voice gateways (Cisco VG Series Gateways), and Cisco Unity Connection
                                          are not configured except for the use of media termination points (MTP) by Cisco Unified Communications Manager.

## Deployment Recommendations for Enterprise Networks

IPv4-only stack or IPv6-only stack devices support:

Single-site call processing deployments.

Multi-site distributed call processing deployments.

Multi-site deployments with centralized call processing.

To move toward an IPv6 deployment and reduce dependency on IPv4 addresses, we recommend that you deploy:

IPv6-only stack SIP phones, SIP gateways, and SIP trunks.

Dual-stack Cisco Unified Communications Manager (Unified CM) clusters and other application servers.

### Deployment Gaps

When you transition from a traditional IPv4 network to an IPv6 dual-stack network deployment, the following functionality
                              is not supported.

IPv6-only stack site or branch office  (LAN)

IPv6-only data center

All IP phones with SCCP signaling

Secure IP phones, CE endpoints, and gateways

Applications based on ISR and ISR G2 Routers

IP phone VPN

IP phones with NTP

Video conference deployment based on Cisco TelePresence Conductor, Cisco TelePresence MCU, and Cisco TelePresence Server

Mobile Remote Access

Off-premise Cisco Jabber

Cisco Meeting Server

Cisco TelePresence Management Suite

SCCP signaling configuration IP phones

RSVP call admission control

Cisco Spark Hybrid Services

Third-party API products

Media Gateway Control Protocol (MGCP) gateways

Unified CM supported H.323 gateways

Products that are End-of-Support

Cisco Jabber on IPv6

Expressway-E external on IPv6

Expressway-E internal interface on IPv4

Unified CM , IM & Presence, CUC on IPv4

## Comparison of IPv4 and IPv6

This section provides a brief description of the motivation behind deploying IPv6, and a summary comparison of IPv4 and IPv6.

### Why Deploy IPv6?

The deployment of IPv6 is primarily driven by IPv4 address exhaustion. As the worldwide usage of IP networks increases, the
                              number of applications, devices, and services requiring IP addresses is rapidly increasing. According to the Internet Assigned
                              Numbers Authority (IANA) and Regional Internet Registries, their pool of unallocated IPv4 addresses is exhausted. For example,
                              all area wireless networks in the American Registry for Internet Numbers (ARIN) are IPv6-only stack.

Because the current IPv4 address space is unable to satisfy the potential huge increase in the number of users and the geographical
                              needs of the Internet expansion, many companies are either migrating to or planning their migration to IPv6, which offers
                              a virtually unlimited supply of IP addresses.

Transforming the Internet from IPv4 to IPv6 is likely to take several years. During this period, IPv4 will co-exist with and
                              then gradually be replaced by IPv6.

### Advantages of IPv6 Over IPv4

As a new version of the Internet Protocol, IPv6 provides the following advantages over IPv4:

Larger address space (Supported in Cisco Collaboration Systems Release)

The main feature of IPv6 that is driving adoption today is the larger address space. Addresses in IPv6 are 128 bits long compared
                                       to 32 bits in IPv4. The larger address space avoids the potential exhaustion of the IPv4 address space without the need for
                                       network address translation (NAT) or other devices that break the end-to-end nature of Internet traffic. By avoiding the need
                                       for complex sub-netting schemes, IPv6 addressing schemes are easier to understand, making administration of medium and large
                                       networks simpler.

Address scopes (Supported)

IPv6 introduces the concept of address scopes. An address scope defines the region, or span, where an address can be defined
                                       as a unique identifier of an interface. These spans are the link, the site network, and the global network, corresponding
                                       to link-local, site-local (or unique local unicast), and global addresses.

Stateless Address Auto-Configuration (SLAAC) (Supported)

IPv6 hosts can be configured automatically when connected to a routed IPv6 network using ICMPv6 router discovery messages.
                                       Address reconfiguration is also simplified. If IPv6 auto-configuration is not suitable, a host  can be configured manually.

Multicast ( Not supported)

Multicast is part of the base specifications in IPv6, unlike IPv4, where it was introduced later. Like IPv6 unicast addresses,
                                       the IPv6 multicast address range is much larger than that of IPv4. IPv6 does not have a link-local broadcast facility; the
                                       same effect can be achieved by multicasting to the all-hosts group address (FF02::1).

Streamlined header format and flow identification ( Not supported)

The IPv6 header format reduces router processing overhead by using a fixed header length, performing fragmentation on hosts
                                       instead of routers, and using an improved header extension method and a new flow label to identify traffic flows requiring
                                       special treatment.

Mobile IPv6 ( Not supported)

Mobile IPv6 allows a mobile node to change its locations and addresses, while maintaining a connection to a specific address
                                       that is always assigned to the mobile node and through which the mobile node is always reachable. Mobile IPv6 provides transport
                                       layer connection survivability when a node moves from one link to another by performing address maintenance for mobile nodes
                                       at the Internet layer.

Mobile IPv6 is not supported by Cisco IP Phones or other collaboration components.

Network-layer security ( Not supported)

IPsec, the protocol for IP network-layer encryption and authentication, is part of the base protocol suite in IPv6. This is
                                       unlike IPv4, where IPsec is optional. Because of its reduced payload and performance overhead, products use TLS and SRTP for
                                       authentication and encryption.

The following table summarizes the differences between IPv4 and IPv6 services.

IP Service

IPv4 Feature

IPv6 Feature

Address range

32-bit, NAT

128-bit, multiple scopes

Auto-configuration

DHCP

Stateless, Easy Reconfiguration, DHCP

Routing

RIP, OSPFv2, IS-IS, EIGRP, MP-BGP

RIPng, OSPFv3, IS-IS, EIGRP, MP-BGP

IP Security

IPsec

IPsec

Mobility

Mobile IP

Mobile IP with direct routing

Quality of Service (QoS)

Differentiated Service, Integrated Service

Differentiated Service, Integrated Service

IP multicast

IGMP, PIM, and Multicast BGP

MLD, PIM, and Multicast BGP; Scope Identifier

### Customers Also Viewed

- IPv6 Deployment Guide --- IPv6 Basics

| Date | Change | Link to Topic |
|---|---|---|
| October 2024 | Updated the section "IPv6-only Supported and Not Supported Features". Moved "EMCC" from "IPv6-only Supported Features" to
                                          "IPv6-only Not Supported Features" as it is concluded that IPv6-only device profile login for EMCC is not supported. |  |
| Included "Support for Catalyst 8000 Series Edge Platforms" in the section "Supported IPv6 Addressing Modes". |
| November 2023 | The entire guide is updated. The following are the updates to the guide. A few to mention - Table 8 is updated. Deleted “for DOD Network only” Replaced “Recommended” to “Supported” Removed “CSR 12” and “CSR 14” references Removed release numbers across the guide to keep it generic Removed occurrences of “Solution Tested” Deleted all Deployment Gaps and created a new list Jabber on IPv6, Expressway-E external on IPv6, Expressway-E internal interface on IPv4, UCM, IM&P, CUC on IPv4 are supported
                                                deployments Dual-stack: Used for application servers, such as Cisco Unified Communications Manager, Cisco Unity Connection, Cisco Emergency Responder,
                                                and Cisco Unified Survivable Remote Site Telephony (Unified SRST) Table 8 and Table 10: Titles “Supported” instead of “Recommended”, remove “Solution Tested" column Note: IPv6 NAT-based solution is not supported DHCP v6 modify the text accordingly MRA: Jabber on IPv6, Expressway-E external on IPv6, Expressway-E internal interface on IPv4, UCM, IM&P, CUC on IPv4 are supported
                                                deployments The SIP Trunk configuration settings discussed in this section are applied through the Common Device Configuration profile
                                                that is created and assigned to the SIP trunk (IP Addressing Mode and IP Addressing Mode Preference for Signaling), and through
                                                the SIP Profile configuration assigned to the SIP trunk (Enable ANAT should be disabled). Change “Enable ANAT should be disabled”.
                                                This is confusing. Instead, mentioned "ANAT is not enabled." Removed the following from ANAT section: Media Selection for Outbound Early Offer Calls with ANAT Media Selection for Inbound Early Offer Calls with ANAT Media Selection for Delayed Offer Calls Over Unified CM SIP Trunks with ANAT Media Selection for Outbound Delayed Offer Calls with ANAT Inbound Delayed Offer Calls with ANAT Inbound Delayed Offer Calls with ANAT and Supported: sdp anat Inbound Delayed Offer Calls with ANAT and Require: sdp-anat Included this: The SIP trunk uses either the Unified CM IPv4 address or the Unified CM IPv6 address for signaling, and an
                                                MTP. We recommend IPv6 Only for production environments. Removed the media part. Instead mentioned, MTP or other trunk address for media. Modified to: Outbound SIP best effort early offer (without MTP/TRP) in SIP trunk as we don’t support in IPv6 mode. Removed this Note: In CSR 12.0, SIP Early Offer does not support IPv6. CUBE or Unified SRST gateways will not support ANAT. The following changes are made to the section "IPv6-Only Phones": Existing content is removed. Replaced with the following: IPv6 only Supported Features: Mobility – MVA/IVR, CAPFv3, TVS and TFTP, Extension Mobility, EMCC, SRST, SIP GW, SIP Route
                                                      Pattern, Barge, Intercom, Phone NTP Reference, Device Mobility, Self Care Portal, Self Provisioning using with and without
                                                      IVR, Phone services - Corporate Directory, Missed Calls, Placed Calls, Intercom Calls, Personal Directory, Voicemail, Received
                                                      Calls, Web Dialer, Quality Report Tool (QRT), SNMPv6 MIB, Phone Config. download, CTI, IPVMS (Unicast MoH, software MTP, ANN,
                                                      Conference Bridge, IVR), CDR IPv6-Only Not Supported Features Best Effort Early Offer over SIP Trunk External MoH, Multicast MoH, Video On Hold, Voicemail, Recording (BIB Recording, GW Recording), Enhanced E911 SSH, Cluster Manager, LDAP, Syslog Server/Alarm Library, Serviceability Applications - IPMA, RTMT DRS, IPSec Media Resources (IOS Xcoder/ hardware MTP/TRP)/Conference Bridge), Video conference resource (MCU/Conductor), FAX/ATA MRA (Jabber in IPv6 and Expressway-E external interface in v6 and enterprise network in v4 is supported) Silent Monitoring, Whisper Coaching, Agent Greeting, VG as analog line interface using SCCP (pending test) Removed ISR 4000 references IPv6 endpoints should be configured as IPv6 with preference Dual Stack with preference IPv6 Removed "with no telephony services provided over an IP WAN." Remove CSR 12.0 Addressed CDET "CSCwh69667" Removed SRST 12.0 Table 8: Added row for "Cisco Room Series, Board Series, and Desk Series". All "Yes" Change 7832 - "Yes" Removed row Wi-Fi enabled devices: Cisco IP Phone 8861, 8865 The first row "Dual- Stacks: IPv4 and IPv6" is "Yes" for all 78xx and 88xx. Added the following phones to this row: 7811,
                                                7821, 7841, 7861 For 7832 and 8832: YES to Dual-Stack For 7832 - "Yes" in 8861 all columns Removed the entire row that says "Cisco Unified IP Phone 6901, 7945G, 7965G, 7975G …" It is End of Support Removed "Cisco DX70 and DX80" Removed row "Cisco TelePresence MX Series, SX Series" Removed row "Cisco TelePresence System EX Series" Removed row "Cisco Webex Share" Remove row "Cisco IP Communicator" Remove row Wi-Fi enabled devices: Cisco IP Phone 8861, 8865 Document direction Removed "We recommend Stateful DHCP host configuration for both IPv4 or IPv6 IP phones." Remove dual-stack IP Phones that require ANAT, which is not supported in Unified SRST call agents Removed the "Security and IPv6 Traffic" section Removed ISR 4000 G3 Include row for "Cisco Room Series, Board Series, and Desk Series". All "Yes" Removed "Cisco ATA 190 Series Analog Telephone Adapters" | - |
| June 08, 2022 | Updated the table "Table 9: Supported Addressing Modes Communication Gateways". | Table 9: Supported Addressing Modes for,Communication Gateways |
| April 01, 2021 | Removed redundant topics from Call Processing and Call Admission Control chapter. | - |
| April 10, 2019 | Changed book title to include Cisco Collaboration System Release. | - |
| April 30, 2018 | Updated overview based on Cisco Collaboration Systems Release. | IPv6 Deployment Overview |
| Updated deployment gaps. | Deployment Recommendations for Enterprise Networks |
| Added a note about IPv6 multicast application. | IPv6 Multicast Addresses |
| Updated the supported IPv6 addressing modes for endpoints. Added Cisco Meeting Server and Cisco TelePresence Management Suite. | Supported IPv6 Addressing Modes for Products |
| Updated the note. | IPv6 Bandwidth Provisioning |
| Added Cisco Meeting Server and Cisco TelePresence Management Suite in Video Conferencing section. Added Multistream video section. Updated Unified CM IM and Presence Service section to include dual-stack. | Applications Overview |
| Added: Cisco TelePresence EX Series Cisco Meeting Server Cisco TelePresence Management Suite | Product Configuration Resources for IPv6 |

| Note | As of Cisco Collaboration Systems Release, some default settings have not been adjusted for IPv6-only as a default, so follow
                                       the directions in this guide to ensure that you use the recommended settings for IPv6 deployment. Also some labels in the
                                       Admin Configuration UI have not been updated, but changes are noted in this document. For example, the Allow Auto-Configuration
                                       for Phones label has not been updated to Allow Stateless Auto-Configuration for Phones. |
|---|---|

| Scale of Deployment (Endpoints) | Servers and Gateways (Dual-stack or IPv4) | IPv4 Addresses Before Deploying IPv6-only Endpoints | IPv4 Addresses After Deploying IPv6-only Endpoints | Percent Reduction in IPv4 Addresses |
|---|---|---|---|---|
| 500 | 6 | 506 | 6 | 98.8% |
| 5,000 | 13 | 5,013 | 13 | 99.7% |
| 10,000 | 25 | 10,025 | 25 | 99.8% |

| Note | The scope of this document is limited to the solutions approved by Cisco. Supported IPv4-only stack applications are limited
                                          to those stated in this document. It is assumed that IP phones and gateways are configured with either an IPv4-only stack
                                          or IPv6-only stack using SIP signaling. Supported application servers support IPv4-only and IPv6-only stacks (dual-stack).
                                          Any applications that we did not develop or test are not supported by Cisco TAC. In IPv6 supported network configurations,
                                          Skinny Client Control Protocol (SCCP) for IP phones, voice gateways (Cisco VG Series Gateways), and Cisco Unity Connection
                                          are not configured except for the use of media termination points (MTP) by Cisco Unified Communications Manager. |
|---|---|

| Note | Mobile IPv6 is not supported by Cisco IP Phones or other collaboration components. |
|---|---|

| IP Service | IPv4 Feature | IPv6 Feature |
|---|---|---|
| Address range | 32-bit, NAT | 128-bit, multiple scopes |
| Auto-configuration | DHCP | Stateless, Easy Reconfiguration, DHCP |
| Routing | RIP, OSPFv2, IS-IS, EIGRP, MP-BGP | RIPng, OSPFv3, IS-IS, EIGRP, MP-BGP |
| IP Security | IPsec | IPsec |
| Mobility | Mobile IP | Mobile IP with direct routing |
| Quality of Service (QoS) | Differentiated Service, Integrated Service | Differentiated Service, Integrated Service |
| IP multicast | IGMP, PIM, and Multicast BGP | MLD, PIM, and Multicast BGP; Scope Identifier |