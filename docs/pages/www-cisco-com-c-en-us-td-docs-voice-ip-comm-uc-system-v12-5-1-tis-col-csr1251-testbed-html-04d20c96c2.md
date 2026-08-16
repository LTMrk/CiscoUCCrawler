---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v12-5-1-tis-col-csr1251-testbed-html-04d20c96c2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V12-5-1/TIS/COL-CSR1251-TestBed.html
retrieved_at: 2026-08-16T18:27:38.061440+00:00
---

Collaboration Test Bed Description for CSR 12.5(1)

# Collaboration Test Bed Description for CSR 12.5(1)

### Download Options

Updated: February 11, 2019

# Collaboration Test Bed for Collaboration Systems Release 12.5(1)

First Published : February 11, 2019

## Overview

The Cisco Collaboration Systems test bed validates functionality applicable to a large cross section of collaboration customers. The test bed architecture is based on principles and design guidance documented in the Cisco Collaboration Systems Solution Reference Network Designs (SRND) . The set of functionality deployed in the test bed is a superset of functionality documented in Cisco Preferred Architecture Guides .

The test bed architecture allows continuous system test and integration, and critical system level feature testing.

In Cisco Collaboration Systems Release (CSR) 12.5(1), some changes include:

■ Architecture enhancements in edge for ICE enablement.

■ Support for Cisco WSA with iOS push notifications. .

■ Cisco Webex Teams and Jabber IM and Presence integration using IM and Presence Service connectors.

■ ECC support for some collaboration products. (TLS 1.2 support for various Cisco Collaboration products. For more details, see the TLS 1.2 Compatibility Matrix for Cisco Collaboration Products ._

For more details about system-wide features tested for Cisco Collaboration Systems Release 12.5(1), see System Release Notes for Cisco Collaboration Systems, Release 12.5(1) . For details about the new and changed product features, see individual product releases notes: Product Documentation .

## Collaboration Test Bed and Deployment Architecture

This figure provides an overview of the Cisco Collaboration Systems Release 12.5(1) test bed. This high-level topology centers on the Cisco Unified Communications Manager (Unified Communications Manager). To address global customer needs, the test bed contains collaboration elements spread across different Unified Communications Manager clusters in multiple time zones and geographical boundaries.

For a Visio version of the test bed topology, click here .

For text files that contain the output from issuing a show running-config IOS command on various components in the collaboration test bed deployments, click here .

Figure 1: Collaboration Systems Release 12.5(1) Test Bed Architecture

The test bed addresses collaboration functionality wanted by large customers.

■ Call Processing (including Emergency Services)

■ Endpoints, Collaboration Edge, Cloud

■ IM and Presence

■ Messaging

■ Conferencing

## Call Processing (including Emergency Services)

Call control is the core element for any communications deployment. It provides endpoint registration, call processing, and call admission control. It is important to design collaboration deployments to ensure that call-processing systems are distributed and scalable enough to handle the required number of users and devices. For more details, see the Cisco Collaboration Systems Solution Reference Network Designs (SRND) . The deployments are resilient enough to handle various network and application outages or failures. The following are some of the key call processing components deployed in the Cisco Collaboration Systems test bed.

### Unified CM and Unified CM SME

Typical to very large customers, the test bed has Unified Communications Manager as distributed session manager clusters. SEA/WDC represents a megacluster in the American region that has Unified Communication Manager deployment leveraging the clustering over WAN (CoW) model. Eight of the 16 subscriber nodes in the mega cluster are in SEA (west coast data center). The remaining eight subscriber nodes are in WDC (East Coast Data Center). LHR represents a medium size Unified Communications Manager cluster with four nodes in the EMEA region.

The Unified CM SME is an eight-subscriber node cluster. Half of the nodes are in JFK (East Coast Data Center) and other half are in SFO (West Coast Data Center) leveraging a CoW mechanism. Unified CM SME provides interconnectivity services among various Unified Communications Manager clusters, Cisco Unified Communications Manager Express (Unified CME) nodes, and other components. Several trunk connectivity arrangements are commonly in place at various collaboration customer deployments in this test bed.

The Unified CM SME serves as egress point from a Business-to-Business (B2B) perspective. The Unified Communications Manager site at PDX in the West Coast represents a partner location that has B2B communications with the main enterprise customer.

### Cisco Expressway

A leaf cluster based on Cisco Expressway is associated with SEA/WDC. It provides support to a branch cluster that hosts legacy 323 endpoints. Cisco Expressway is connected to parent SEA/WDC through SIP trunk.

### Cisco Unified Communication Manager Express

Cisco Unified Communication Manager Express (Unified CME) represents a branch cluster that is connected to other components in the test bed through Unified CM SME. Some endpoints are located in small branch offices based on Unified CME. 3

### Cisco Unified Survivable Remote Site Telephony (Unified SRST)

Certain endpoints are located in remote branch office locations that use Cisco Unified Survivable Remote Site Telephony (Unified SRST). Since the Unified SRST node provides the call control, if the endpoint encounters a loss in WAN connectivity to the Unified Communications Manager cluster, it remains functional. SRST branches utilize both ISR G2 3945 and ISR G3 4451 components.

## Cisco Emergency Responder

Cisco Emergency Responder helps assure that Unified Communications Manager sends emergency calls to the appropriate Public Safety Answering Point (PSAP) for the caller's location. It also helps ensure that the PSAP can identify the caller's location and, if necessary, return the call. Cisco Emergency Responder can also notify customer security personnel of an active emergency call and the caller's location. Location tracking is used with Unified Communications Manager.

## Endpoints, Edge, and Cloud

Various endpoints are used in the Cisco Collaboration deployment. These endpoints are spread throughout the deployment models. The endpoints in SEA/WDC and LHR clusters can be located on-premise, in remote branch offices, or on the Internet. Remote endpoints located on Internet can ingress through two mechanisms: VPN access through Cisco AnyConnect VPN or VPN less access through Cisco Expressway Collaboration Edge.

For a detailed list of all the endpoints that are part of the Cisco Collaboration Systems Release 12.0(1), see the Cisco Collaboration Systems Release Compatibility Matrix .

### Cisco Expressway Collaboration Edge

Cisco Expressway Collaboration Edge Architecture combines the capabilities of Cisco gateway offerings with the core capabilities of Cisco Collaboration solutions and the network.

### Cisco Webex Hybrid Services

For more information about Cisco Webex Hybrid Services, see the product and support documents.

## Instant Messaging (IM) and Presence

The main presence component of the solution is the Unified Communications Manager IM and Presence Service.

### Cisco Unified Communications Manager IM and Presence Service

IM and Presence Service enables Cisco Jabber, Unified Communications Manager applications, and third-party applications to increase user productivity. IM and Presence Service determines the most effective form of communication to help connect collaborating partners more efficiently. It incorporates the Extensible Communications Platform (XCP) and supports SIP/SIMPLE and Extensible Messaging and Presence Protocol (XMPP) to collect information about a user's availability status and communications capabilities.

IM and Presence Service is deployed with the equivalent version of Unified Communications Manager in SEA/WDC and LHR sites. In SEA/WDC cluster, IM and Presence Service functionality is provided by six IM and Presence Service nodes that are split across WAN (3:3) leveraging CoW. In the LHR cluster, IM and Presence Service functionality is provided by two IM and Presence Service nodes. Second enterprise has a PDX cluster. In the PDX cluster, IM and Presence Service functionality is provided by a single IM and Presence Service node. Cisco Expressway C/E nodes located in SFO and PDX facilitate XMPP federation between SEA/WDC cluster and PDX cluster.

### Jabber for iOS Push Notifications

Cisco Jabber on iPhone and iPad clients use TCP socket connections to Unified Communication Manager IM and Presence Service or Cisco Webex Messenger to maintain connections for instant messaging and voice while running in back ground mode. Release 11 of iOS does not support this connection mechanism, and Apple’s cloud-based Push Notifications is needed to push instant message and voice notifications to Cisco Jabber iOS clients that are running in the background.

## Voicemail and Messaging

Cisco products provide several voice messaging options for large and small collaboration systems, and the ability to integrate with third-party voicemail systems using standard protocols. The voice messaging portfolio for Cisco Collaboration Systems test bed consists of two main messaging products: Cisco Unity Connection and Cisco Unity Express.

### Cisco Unity Connection

Cisco Unity Express is added to the Cisco Unified Communications Manager Express (Unified CME) router and integrated with Unified CME to provide voicemail services to users and phones registered to Unified CME.

SEA/WDC mega cluster leverages Cisco Unity Connection cluster for messaging capabilities. This two node Cisco Unity Connection cluster is split (1:1) across the WAN and provides messaging capabilities using SCCP and SIP connectivity. A single node Cisco Unity Connection provides messaging capabilities for the LHR cluster. This Cisco Unity Connection is centrally located in SFO and is connected to Unified CM SME through SIP trunking.

## Conferencing

Ability for three or more people to participate and communicate in real time by using voice and video technologies is an essential component of collaboration. The conferencing architecture takes advantage of call processing capabilities of Unified Communication Manager. Cisco rich media conferencing uses the existing infrastructure for point-to-point calls and provides three types of conferences:

■ Ad-hoc or instant conference - A conference that is not scheduled or organized in advance. For example, a call between two parties who add other parties to the call is an ad-hoc conference.

■ Rendezvous or permanent conference - A conference that requires callers to dial a predetermined number or URI to reach a shared conferencing resource. Meet-me, static, and permanent are other names for this type of conference.

■ Scheduled conference - A conference scheduled in advance with a predetermined start time. Typically, conference resources are guaranteed to be available upon the start of the scheduled conference.

The conferencing topology in Cisco Collaboration Systems Release 12.5(1) addresses:

■ Cisco Meeting Server based conferences

■ Cisco TelePresence Conductor and Cisco Virtual Telepresence Server based conferences

■ Unified Communications Manager based ad-hoc Conference

## Cisco Meeting Server

Cisco Meeting Server (Meeting Server) brings video, audio, and web communication together to meet the collaboration needs of the modern workplace. It has been optimized to be deployed with Cisco Unified Communications Manager and Cisco Expressway. Cisco TelePresence Management Suite is used for scheduling conferences. Meeting Server scales easily for small or large deployments, allowing you to add capacity incrementally as needed.

## Cisco TelePresence Conductor (EOS)

Cisco TelePresence Conductor enables simple, reliable, and efficient multiparty conferencing. It orchestrates the allocation of conferencing resources such as Cisco TelePresence Server and Cisco Multipoint Control Unit (MCU) to every user in a meeting. The Cisco TelePresence Conductor helps ensure intelligent conference placement and optimum resource utilization, and delivers powerful, comprehensive administrative control, making simple natural conferencing a reality.

The test topology supports Cisco TelePresence Conductor ad-hoc, rendezvous, and scheduled conferencing functionality. The conference bridge resources are arranged in different pools that are spread across multiple Unified Communications Manager clusters and Unified CM SME locations.

### Cisco TelePresence Server on Virtual Machine (EOS)

Cisco TelePresence Server on Virtual Machine components serve as conference bridges in various pools and are deployed along with Cisco TelePresence Conductor.

### Cisco TMS/Cisco TMSPE/Cisco TMSXE

Cisco TelePresence Management Suite (TMS) is a software product used by customers to manage, maintain, log, and schedule Cisco TelePresence conferences. The Cisco TMS application also provides users with enhanced features such as directories and one button to push (OBTP) on controlled endpoints.

Cisco TelePresence Management Suite Provisioning Extension (TMSPE) creates collaboration meeting rooms (CMRs) for users according to the permissions and feature limits defined by the administrator. Cisco TelePresence Management Suite Extension for Microsoft Exchange (TMSXE) allows users to schedule meetings using their Microsoft Outlook clients. It also allows users to include the room device video resources by selecting the room as a resource.

## PSTN/IP PSTN

PSTN/IP PSTN routing can be provided through local or centralized gateways. In the current deployment, PSTN connectivity for Unified Communications Manager clusters is provided through local PSTN gateways (3945 and 4451) using different protocols. Localized IP PSTN connectivity is provided through CUBE – ISR 4451 in one of the Unified Communications Manager clusters. Centralized IP PSTN connectivity is provided through CUBE – ISR 3945 and ASR 1004 and Unified CM SME.

## Business-to-Business (B2B) and Cloud Collaboration Meeting Room (CMR) Interoperability

The Unified CM SME serves as egress point for Business-to-Business (B2B) communications. Cisco Expressway-E (in DMZ) and Cisco Expressway-C nodes connected to Unified CM SME provides B2B capabilities (voice, video, and IM and Presence). Endpoints off a main enterprise can reach a midmarket enterprise through B2B. The midmarket enterprise site also has its own Cisco Expressway-E and C pair for B2B purposes. The Cisco Expressway-E (in DMZ) and Cisco Expressway C pair provides connectivity to Cisco Webex Cloud.

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at https://www.cisco.com/cisco/web/siteassets/contacts/index.html .

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: https://www.cisco.com/c/en/us/about/legal/trademarks.html . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

© 2019 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Collaboration Systems Release 12.5