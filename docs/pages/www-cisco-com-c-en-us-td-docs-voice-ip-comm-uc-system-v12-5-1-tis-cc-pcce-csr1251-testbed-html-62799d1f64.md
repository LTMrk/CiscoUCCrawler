---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v12-5-1-tis-cc-pcce-csr1251-testbed-html-62799d1f64
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V12-5-1/TIS/CC-PCCE-CSR1251-TestBed.html
retrieved_at: 2026-08-16T18:27:46.586780+00:00
---

Packaged CCE Test Bed Description for CSR 12.5(1)

# Packaged CCE Test Bed Description for CSR 12.5(1)

### Download Options

Updated: February 11, 2019

# Cisco Packaged Contact Center Enterprise Test Bed for Collaboration Systems Release 12.5(1)

First Published : February, 2019

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

## Overview

This Cisco Packaged Contact Center Enterprise (Packaged CCE) is a predesigned, prepackaged deployment model of Cisco Unified Contact Center Enterprise (Unified CCE) that is easy to install, configure, and administer. It provides inbound and outbound voice and video, interactive voice response (IVR), and web interaction. It also supports customer relationship management (CRM), workforce management, recording, monitoring, and wallboard applications.

Packaged CCE 12.0(1) was used to test Cisco Collaboration Systems Release 12.5(1). Packaged CCE is designed for contact centers with fewer than 2000 seats. It includes Cisco Unified Communications Manager (Unified Communications Manager), Unified Contact Center Enterprise, and Cisco Unified Customer Voice Portal (Unified CVP).

This test bed is designed to implement and test some of the design considerations and guidelines of:

https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html

For information on how to install and configure Packaged CCE, see https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

More configuration information for contact center components is available at: Configuration Examples and TechNotes .

## Packaged CCE Test Bed and Deployment Architecture

This Packaged CCE test bed replicates a 2000 agent deployment contact center. This test bed is combined with a general collaboration office deployment on a Unified Communications Manager cluster. It uses a SIP-based Unified CVP deployment for prompting, collecting, and queuing. Agents use SCCP and SIP phones such as Cisco IP Phone 7800 and 8800 Series, video endpoints such as Cisco DX Series, and Cisco Jabber. Agents also use Cisco Finesse desktops.

The deployment uses two data centers connected through a high-speed public and private WAN for redundancy. Unified Communications Manager is clustered over the WAN. Packaged CCE is split over the WAN with an 80-ms delay and Cisco Finesse is also clustered over WAN with the same delay. Cisco Unified Border Element (CUBE) is deployed for both inbound and outbound calls. PSTN is also deployed for inbound calls.

The deployment follows Cisco Collaboration Edge Architecture to enable Mobile and Remote Access (MRA). This allows endpoints to have their registration, call control, provisioning, messaging and presence services provided by Cisco Unified Communications Manager (Unified CM) when the endpoint is not within the enterprise network. Cisco Expressway Series provides secure firewall traversal and line-side support for Unified CM registrations.

The deployment also uses a remote data center and two remote sites. Calls from Remote Site 1 route to Cisco Unified SIP Proxy in Data Center A. Calls from Remote Site 2 route to Unified CVP2 in the Remote Data Center. Cisco Virtualized Voice Browser, installed in both remote sites, interprets VXML documents.

For a Visio version of the test bed topology diagram, see Network Topology Diagrams for Contact Center .

Figure 1: Collaboration Systems Release 12.0(1): Packaged CCE Test Architecture

## Packaged Components

Packaged CCE includes Contact Center functionalities that provide value to customers.

### Cisco Unified Contact Center Enterprise

Cisco Unified Contact Center Enterprise (Unified CCE) provides intelligent routing and call treatment with transparent blending of multiple communication channels. These components also ease the transition from a traditional automatic call distributor (ACD) to an IP-based ACD.

Unified CCE is part of a strategic platform that helps you move into the next phase of customer contact, Customer Interaction Network. The Customer Interaction Network is a distributed, IP-based customer service infrastructure that comprises of a continuously evolving suite of innovative, multichannel services and customer-relationship-management (CRM) applications.

With Unified CCE, the contact center manager can configure agents to handle inbound and outbound voice calls. The agents can switch between these media on a task-by-task basis.

For the latest configuration options for Unified CCE, go to https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

### Cisco Unified Customer Voice Portal

Cisco Unified Customer Voice Portal (Unified CVP) provides interactive voice response and queuing capabilities in a contact center environment and supports automated speech recognition (ASR) and text-to-speech (TTS) capabilities. Unified CVP is implemented in this test environment in self-service mode, and the comprehensive mode. Comprehensive mode includes support for agent queuing, multisite call switching, and speech-enabled and touch tone applications. You can use touch tone signals or your own voice to request self-service information. Its components work together enabling you to create and deploy IVR applications that include voice interaction and traditional numeric inputs to provide intelligent, personalized self-service over the phone.

Unified CVP Call Server consists of SIP services, plays media files to the caller, and collects information in return.

Through an operations console, Unified CVP also allows you to monitor, manage, and configure all Unified CVP solution components from a central, single operations console.

For additional information about Unified CVP, see https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

### Cisco Unified Intelligence Center

Cisco Unified Intelligence Center (Unified Intelligence Center) is a web-based reporting application that provides real-time and historical reporting. It provides precise and comprehensive contact center reports. The default deployment pulls Unified Intelligence Center data from the Logger database on the Unified CCE Data Server, where real-time, historical, and call detail data is stored. Retention is 400 days for historical data and 40 days for call detail data. If you need a longer retention period, you can optionally install the AW-HDS-DDS on a maximum of two separate, external servers.

In contact center environments, supervisors can view reports to see agents’ current or past performance. Reports can be displayed in different views such as Grid, Gauge, Pie, or Line charts. First step is to design the views (how and what data to be presented on screen) of report in Unified Intelligence Center. This step is a one-time activity. Once it is done, you can sign in anytime to Unified Intelligence Center and run the report to see data in a particular view. While running a report, specify the filter such as, show data between dates or show data for agents having agent id in a particular range. Unified Intelligence Center provides permalink to each view of the report so you can directly see the report by specifying the link in web browser.

For additional information about Unified Intelligence Center, see https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html .

### Cisco Finesse

Cisco Finesse is a next-generation agent and supervisor desktop designed to provide a collaborative experience for the communities that interact with your customer service organization.

Agents sign on to the Cisco Finesse server from Microsoft Internet Explorer 9.0 using a laptop or a desktop connected directly to the data center or remotely using Virtual Desktop Infrastructure (VDI) devices.

For all support information on Cisco Finesse, see https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html .

## External Components

Various external components enhance the Contact Center functionalities of Packaged CCE.

### Cisco Expressway Series

For MRA, Cisco Expressway Series (Expressway) provides secure firewall traversal and lineside support for Unified CM registrations.

For more information about Expressway, see: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/tsd-products-support-series-home.html .

### Cisco Finesse Agent Desktop

Cisco Finesse Agent Desktop testing includes handling of inbound calls, transfer, and conference.

For all support information for Packaged CCE Desktop, see https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html .

### Cisco Virtualized Voice Browser

Cisco Virtualized Voice Browser (Virtualized Voice Browser) provides a platform for interpreting VXML documents. When an incoming call arrives at the contact center, Virtualized Voice Browser allocates a VXML port that represents the VoIP endpoint. Virtualized Voice Browser sends HTTP requests to the Unified CVP VXML server. The Unified CVP VXML server executes the request and sends back a dynamically generated VXML document.

For more information about Virtualized Voice Browser, see: https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html .

### Cisco SocialMiner

Note : Not tested in 12.0.

Cisco SocialMiner (SocialMiner) is a social media customer care solution. SocialMiner can help you proactively respond to customers who communicate through public networks. SocialMiner and Unified CCE work in tandem to process the Agent Request (Voice CallBack) from its inception through the receipt of the callback.

The role of SocialMiner in the Agent Request feature:

■ Provide a notification mechanism (the Connection to Unified CCE notification type) used to forward callback requests to Unified CCE through a Media Routing (MR) connection.

■ Provide the API used by custom applications to start a callback.

■ Forward the callback details to Unified CCE.

■ Provide an API used by custom applications to retrieve the state of the callback. This API includes a field in the GET call that can communicate to the caller the estimated wait time until an agent becomes available.

■ Provide an API used by custom applications to cancel a requested callback.

For more information about SocialMiner, see: https://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/tsd-products-support-series-home.html .

### Cisco Unified Border Element

SIP trunking is used for the Unified CVP deployment with Cisco IOS gateways and Cisco Unified Border Element (Unified Border Element). Stand-alone Unified Border Element is placed in Data Center A and Data Center B respectively. From each Unified Border Element, there is a SIP trunk on Transmission Control Protocol (TCP) (using VoIP dial-peer) to Unified CVP in Data Center A and Data Center B respectively.

From Unified CVP, there is a SIP trunk on TCP to Unified Border Element. In addition, from each Unified Border Element (in Data Center A and B), there is another SIP trunk on User Datagram Protocol (using VoIP Dial-peers) to accept the IP calls from IP PSTN Service Provider network.

For more information about Unified Border Element, see https://www.cisco.com/c/en/us/support/unified-communications/unified-border-element/tsd-products-support-series-home.html .

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