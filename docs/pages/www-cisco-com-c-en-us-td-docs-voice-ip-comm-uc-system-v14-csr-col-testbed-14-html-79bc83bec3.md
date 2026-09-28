---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v14-csr-col-testbed-14-html-79bc83bec3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V14/CSR_COL_TestBed_14.html
retrieved_at: 2026-08-16T18:27:16.980768+00:00
---

Collaboration Test Bed for Collaboration Systems Release 14

# Collaboration Test Bed for Collaboration Systems Release 14

### Download Options

Updated: May 5, 2021

Collaboration Test Bed for Collaboration Systems Release 14

First Published : April 16, 2021

## Overview

This document covers the test bed topology that was completed for Cisco Collaborations System Release 14 testing.

The Cisco Collaboration Systems test bed validates functionality applicable to a large cross section of collaboration customers. The test bed architecture is based on principles and design guidance documented in Cisco Collaboration Solutions Design Guidance . The functionality deployed in the test bed is a superset of functionality documented in Cisco Preferred Architecture Guides .

The test bed architecture was updated for this release and includes support for:

· Support for Cisco Headset Management and Headset-based Extension Mobility

· iOS 13 support for the Apple Push Notification service

· Emergency Locations call routing updates for Kari’s Law compliance

· Support for new Phone Migration services

· OAuth support for Office 365 calendar integration with the IM and Presence Service

For more details about system-wide features tested for Cisco Collaboration Systems Release 14, see Release Notes for Cisco Collaboration Systems, Release 14 . For details about the new and changed product features, see Release Notes for the product.

## Collaboration Test Bed and Deployment Architecture

This figure provides an overview of the test bed topology that was used for Cisco Collaboration Systems Release 14. This high-level topology centers on the Cisco Unified Communications Manager (Unified Communications Manager). To address global customer needs, the test bed contains collaboration elements spread across different Unified Communications Manager clusters in multiple time zones and geographical boundaries.

Figure 1: Collaboration Systems Release 14 Test Bed Architecture

This test bed is designed to be very flexible and is built to meet specific test requirements. It provides a basic enterprise solution with a number of optional components, such as server applications, high availability, gateways, and UCS hardware. You can add or subtract these optional components wherever required.

Following is another view of the test bed topology from a more functional level:

## Collaboration Components

The test bed addresses collaboration functionality wanted by large customers.

■ Call Processing — Call control is the core element for any communications deployment. Unified CM provides endpoint registration, call processing, and call admission control, while Cisco Emergency Responder adds optional E911 services. It is important to design collaboration deployments to ensure that call-processing systems are distributed and scalable enough to handle the required number of users and devices. For more details, see Cisco Collaboration Solutions Design Guidance . The deployments are resilient enough to handle various network and application outages or failures.

■ IM and Presence —The IM and Presence Service is the main on-premises component for IM and Presence with Cisco Jabber and other IM clients. For optional cloud deployments, Cisco Webex Messenger provides IM and Presence via the Webex Teams client.

■ Collaboration Edge —Applications such as Cisco Emergency Responder and Cisco Unified Border Element sit at the edge of your enterprise network, providing secure firewall traversal for remote endpoints, secure Business-to-Business communications, or gateway connectivity between different VoIP networks or to the PSTN.

■ Voicemail and Messaging —Cisco Unity Connection provides voicemail and messaging services.

■ Endpoints —Cisco provides a wide variety of Collaboration endpoints that can be used with this topology.

■ Conferencing —Conferencing components let three or more people communicate in real time using voice, video and collaboration technologies. The conferencing architecture leverages conferencing applications such as Cisco Meeting Server, Cisco TelePresence Management Suite, Cisco TelePresence Server, or Cisco TelePresence Conductor to provide ad hoc, scheduled, or rendezvous conferencing.

■ Cloud —Cloud deployments can use Cisco Webex Hybrid Services with Webex calling and messaging via Webex Teams to provide cloud-connected collaboration services from the cloud.

■ Contact Center —The enterprise solution includes Cisco Unified Contact Center Express deployed at the Remote Site.

### Unified CM and Unified CM SME

The test bed simulates an intercluster deployment that utilizes two leaf clusters, along with a Session Management Edition cluster. The deployment uses three sites in total (two sites for the main cluster and a single remote site).

The Core Site cluster is a five-node Unified CM cluster that is clustered over the WAN between the Core-A and Core-B sites for geographic redundancy. The Core Site provides a large highly available Collaboration deployment. The Remote Site cluster comprises a smaller three-node Unified CM cluster for simple collaboration.

Both clusters connect over trunks to a two-node Session Management Edition (SME) cluster. The SME cluster aggregates essential services and applications, such as Active Directory, DNS, ADFS and others. The Unified CM SME also provides an egress point for Business-to-Business communication that travels over vCUBE and the egress gateway.

### Instant Messaging (IM) and Presence

The main presence component of the solution is the Unified Communications Manager IM and Presence Service, which enables Cisco Jabber, Unified Communications Manager applications, and third-party applications to increase user productivity. The IM and Presence Service incorporates the Extensible Communications Platform (XCP) and supports SIP/SIMPLE and Extensible Messaging and Presence Protocol (XMPP) to collect information about a user's availability status and communications capabilities.

The basic deployment involves a pair of IM and Presence nodes clustered over the WAN between Core Site A and Core Site B for geographic redundancy. In addition, a single node deployment of the IM and Presence Service is located in the Remote Site. With this deployment, all nodes must be deployed with the same version as Unified CM. However, there is an option to use the Centralized Deployment feature, which allows you to deploy an IM and Presence Service version that is different from your Unified CM cluster. Additional options include:

· Deploying Calendar Integration, connecting the IM and Presence Service to Microsoft Exchange

· Deploying an external database (Oracle or Microsoft SQL Server) for IM and Presence features.

### Cisco Expressway

Cisco Expressway is utilized as part of the Collaboration Edge infrastructure, providing proven and highly secure firewall-traversal technology to extend your organizational reach. In addition, Expressway, helps to enable business-to-business, business-to-consumer, and business-to-cloud-service-provider connections.

The Enterprise Solution provides an Expressway-C and Expressway-E pair for each Unified CM cluster, providing firewall traversal and secure signaling for Mobile and Remote Access endpoints. Optionally, you can deploy a clustered Expressway (three Expressway-E nodes and three Expressway-C nodes), providing Mobile and Remote Access as well as Business-to-Business communication (voice, video, IM and Presence).

### Cisco Unified Border Element

Cisco Unified Border Element (CUBE) is deployed as part of the Collaboration Edge infrastructure using the vCUBE option. The CUBE bridges voice and video connectivity between two separate VoIP networks and is often used to connect enterprise networks to Internet telephony service providers (ITSPs).

In this topology, CUBE provides PSTN/IP PSTN routing through centralized gateways. You also have the option to deploy CUBE on additional hardware gateways, such as ISR and ASR routers.

### Cisco Unity Connection

Cisco Unity Connection adds voicemail and messaging options to your deployment. A single Cisco Unity Connection node is added to the Remote Site, providing voicemail and messaging options for the collaboration environment. Unity Connection also provides the ability to integrate with third-party voicemail systems using standard protocols.

### Endpoints

Various Collaboration endpoints can be used in the Cisco Collaboration deployment. These endpoints are spread throughout the deployment models and can be located on-premise, in remote branch offices, or on the Internet. Remote endpoints located on Internet can ingress through two mechanisms: VPN access through Cisco AnyConnect VPN or VPN-less access through Mobile and Remote Access via Expressway.

For a detailed list of all the endpoints that are part of the Cisco Collaboration Systems Release, see the Cisco Collaboration Systems Release Compatibility Matrix .

### Cisco Emergency Responder

Cisco Emergency Responder is an optional deployment with the Full Enterprise Solution, helping Unified CM to manage emergency calls thereby meeting E911 standards. Emergency Responder assures that Unified CM sends emergency calls to the appropriate Public Safety Answering Point (PSAP) that corresponds to the caller's location. Emergency Responder helps to ensure that the PSAP can identify the caller location and, if necessary, return the call. Cisco Emergency Responder can also notify customer security personnel of the active emergency call and the caller's location. To fulfill this function, Cisco Emergency Responder integrates with location tracking services within Unified CM.

### Conferencing

Ability for three or more people to participate and communicate in real time by using voice and video technologies is an essential component of collaboration. The conferencing architecture takes advantage of call processing capabilities of Unified Communication Manager. Cisco rich media conferencing uses the existing infrastructure for point-to-point calls and provides three types of conferences:

■ Ad-hoc or instant conference - A conference that is not scheduled or organized in advance. For example, a call between two parties who add other parties to the call is an ad-hoc conference.

■ Rendezvous or permanent conference - A conference that requires callers to dial a predetermined number or URI to reach a shared conferencing resource. Meet-me, static, and permanent are other names for this type of conference.

■ Scheduled conference - A conference scheduled in advance with a predetermined start time. Typically, conference resources are guaranteed to be available upon the start of the scheduled conference.

### Cisco Meeting Server

Cisco Meeting Server is the main conferencing component, bringing audio, video, and web communication together to meet the collaboration needs of the modern workplace. It has been optimized to be deployed with Cisco Unified Communications Manager and Cisco Expressway. Cisco Meeting Server scales easily for small or large deployments, allowing you to add capacity incrementally as needed.

### Cisco Webex Hybrid Services

For Cloud deployments, you have the option to deploy Cisco Webex Hybrid Services. This option accesses the Cisco Webex cloud, providing Webex-based calling and messaging via Webex Teams. For more information about Cisco Webex Hybrid Services, see the product and support documents

### Cisco Unified Contact Center Express

The Enterprise Solution includes Cisco Unified Contact Center Express deployed at the Remote Site. Cisco Unified Contact Center Express provides a medium-sized inbound and outbound contact center for up to 400 agents. These deployments provide inbound and outbound voice and video, interactive voice response (IVR), and web interaction. They also support additional Contact Center applications such as Social Miner that support customer relationship management (CRM), workforce management, recording, monitoring, and wallboard applications. High availability is an optional deployment.

### Prime Collaboration Deployment

You have the option to deploy Cisco Prime Collaboration Deployment for platform management. Prime Collaboration Deployment provides tools for managing installs, upgrades and other platform tasks for your deployment.

### PSTN/IP PSTN

PSTN/IP PSTN routing can be provided through local or centralized gateways. In the current deployment, PSTN connectivity for Unified Communications Manager clusters is provided through local PSTN gateways (3945 and 4451) using different protocols. Localized IP PSTN connectivity is provided through CUBE – ISR 4451 in one of the Unified Communications Manager clusters. Centralized IP PSTN connectivity is provided through CUBE – ISR 3945 and ASR 1004 and Unified CM SME.

### Jabber for Push Notifications

Release 13 and 14 of iOS deprecated legacy VoiP sockets that allow Cisco Unified Communications Manager or the IM and Presence Service to maintain connections for calling and messaging while Jabber on iOS is operating in background mode. Apple’s cloud-based Push Notification service is needed to push message and voice notifications to Cisco Jabber iOS clients that are running in the background.

Push Notifications are now supported as well on Android devices. Google’s cloud-based Android Push Notification service is used to push message and voice notifications to Cisco Jabber Android clients that are running in the background.

### Business-to-Business (B2B) and Cloud Collaboration Meeting Room (CMR) Interoperability

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

© 2021 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Collaboration Systems Release 14