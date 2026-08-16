---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-3-mra-exwy-b-mra-deployment-guide-x143-exwy-m-mr-6c8d0264a6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-3/mra/exwy_b_mra-deployment-guide-x143/exwy_m_mra-overview-and-planning.html
retrieved_at: 2026-08-16T15:15:49.082453+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X14.3)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X14.3)

Updated: May 23, 2023

Chapter: MRA Overview

## Chapter: MRA Overview

# MRA Overview

## About Mobile and Remote Access

Cisco Unified Communications Mobile and Remote Access (MRA) is part of the Cisco Collaboration Edge Architecture. MRA allows
                           endpoints such as Cisco Jabber to have their registration, call control, provisioning, messaging, and presence services provided by Cisco Unified Communications Manager ( Unified CM ) when the endpoint is outside the enterprise network. The Expressway provides secure firewall traversal and line-side support
                           for Unified CM registrations.

The MRA solution provides the following functions:

Off-premises access : a consistent experience outside the network for Jabber and EX/MX/SX Series clients

Security : secure business-to-business communications

Cloud services : enterprise grade flexibility and scalable solutions providing rich Cisco Webex integration and service provider offerings

Gateway and interoperability services : media and signaling normalization, and support for nonstandard endpoints

Third-party SIP or H.323 devices can register to the Expressway-C and, if necessary, interoperate with Unified CM -registered devices over a SIP trunk.

Unified CM provides call control for both mobile and on-premise endpoints. Signaling traverses, the Expressway solution between the
                           mobile endpoint and Unified CM . Media traverses the Expressway solution, which relays the media between the endpoints directly. All media is encrypted between
                           the Expressway-C and the mobile endpoint.

### Change History

Date

Change

Reason

May 2023

First published for X14.3.

Included a section on "Enable IPv6 Over MRA".

Unified CM is able to resolve automatically added Expressway-C hostname as MRA solution.

Addressed CDETs.

X14.3 release

August 2022

First published for X14.2.

Moved a few related sections from the Release Note to this guide.

X14.2 release

May 2021

First published for X14.0.

The following are the changes in this release:

Webex Client Embedded Browser Support

SIP Registration Failover for Cisco Jabber - MRA Deployments

X14.0 release

December 2020

First published for X12.7.

The following are the changes in this release:

Fast Path Registration for MRA (Caching Optimization for Registrations)

Webex VDI over MRA

X12.7 release

October 2020

First published for X12.6.3.

The following are the changes in this release:

Multiple Presence Domains over MRA

MRA Documentation Enhancements: The Expressway MRA Deployment Guide has been updated and enhanced with the following new material:

Multi-domain Scenarios — Overview, illustrations, and configuration summary designed to assist customers when deploying more
                                                         complex topologies in a multi-domain environment.

Multi-cluster Scenarios — Best practices section with configuration tips and requirements for multi-cluster scenarios.

Security Requirements — Clarifies the Unified CM security prerequisite for deploying Mobile and Remote Access.

Also included are updates and edits to the following sections:

Call Recording and Silent Monitoring support

Key Expansion Module support

Supported Clients

Supported Endpoints

X12.6.3 release

September 2020

First published for X12.6.2.

The following are the changes in this release:

Support for Whisper Coaching and Whisper Announcements Over MRA

Support for Agent Greeting Over MRA

Android PUSH for IMP over MRA is Disabled by Default

X12.6.2 release

July 2020

First published for X12.6.1.

The following are the changes in this release:

Display Active MRA Registrations Count

Support for BIB Silent Monitoring Over MRA

X12.6.1 release

July 2020

A correction in the "Which MRA Features are Supported" section.

Document correction

June 2020

Updated for the X12.6 release.

X12.6 release

April 2020

Various clarifications and corrections to the guide.

Document corrections & enhancements

December 2019

Various clarifications to the guide:

Reverse DNS requirement updates

TLS verify subject name requirement

Minimum TLS version pre-11.5(1)SU3

No call preservation if node fails

Document corrections & enhancements

March 2019

Clarify that from X12.5, local DNS no longer requires _cisco-uds._tcp.<domain> SRV records (still recommended).

Document correction

February 2019

Clarify UID mapping is mandatory on IdP for single, cluster-wide SAML agreement.

Content enhancement

February 2019

Add Jabber 12.5 clients to supported endpoints for ICE passthrough (subject to Unified CM 12.5).

Software dependency change

January 2019

Fixed CE version for ICE support in MRA to 9.6.1 or later.

Removed Jabber endpoints from ICE for MRA supported components.

Correction to section Unsupported Expressway Features and Limitations for ICE for MRA with Static NAT.

Document correction

January 2019

Updated for X12.5.

X12.5 release

September 2018

Updated for X8.11.2 (change to Unsupported Expressway Features and Limitations for chat/messaging if user authentication by OAuth refresh).

X8.11.2 release

September 2018

Updated for Webex and Spark platform rebranding, and for X8.11.1 maintenance release.

Added, to Unsupported Expressway Features and Limitations section, a known issue with chat/messaging services over MRA if user authentication is by OAuth refresh (self-describing
                                             tokens).

X8.11.1 release

Clarification

July 2018

Included Hunt Group support, subject to Cisco Unified Communications Manager 11.5(1)SU5 or later fixed version.

Software dependency change

July 2018

Updated for X8.11. Also removed port reference topic, which is now available in the Cisco Expressway IP Port Usage Guide .

X8.11 release

May 2018

Clarify MFT over MRA is not supported when using an unrestricted version of IM and Presence Service .

Clarification

March 2018

Clarify no Jabber support for redundant UDS services.

Clarification

December 2017

Added configuration step to enable SIP protocol (disabled by default on new installs).

Content defect

November 2017

Clarified which Cisco IP Phones in the 88xx series support MRA (Configuration Overview section).

Content defect

September 2017

Added links to information about supported features for MRA-connected endpoints. Add information about Collaboration Solutions
                                             Analyzer.

Content enhancement

August 2017

Deskphone control functions bullet removed from "Unsupported Contact Center Features" as not applicable.

Content defect

July 2017

Clarify required versions for Unified Communications software. Corrected duplicated prerequisites for Push Notifications feature.

Content defect

July 2017

Updated.

X8.10 release

April 2017

Added details on partial support for Cisco Jabber SDK features.

Content defect

January 2017

Updated section on unsupported features when using MRA. Added description of Maintenance Mode. Clarified that Expressway-C
                                             and Expressway-E need separate IP addresses.

X8.9.1 release

December 2016

Updated.

X8.9 release

September 2016

Unsupported deployments section updated. Minimum versions note about TLS added.

Clarification to avoid misconfiguration

August 2016

Updated DNS prerequisite to create reverse lookup entries for Expressway-E.

Customer found defect

June 2016

HTTP Allow list feature updates.

X8.8 release

Entries before X8.8 are removed for clarity

### Related Documents

The following documents may help with setting up your environment:

Expressway Basic Configuration (Expressway-C with Expressway-E) Deployment Guide

Expressway Cluster Creation and Maintenance Deployment Guide

Certificate Creation and Use With Expressway Deployment Guide

Cisco Expressway IP Port Usage Configuration Guide , on the Cisco Expressway Series Configuration Guides .

Expressway Administrator Guide

Configuration and Administration of IM and Presence Service on Cisco Unified Communications Manager , at Cisco Unified Communications Manager Configuration Guides

"Directory Integration and Identity Management" chapter in the Design Guides (Cisco Collaboration System Solution Reference Network Designs (SRND)) document

SAML SSO Deployment Guide for Cisco Unified Communications Applications , at Cisco Unified Communications Manager Maintain and Operate Guides

Jabber client configuration details:

### Core Components

Any MRA solution requires Expressway and Unified CM, with MRA-compatible soft clients and/or fixed endpoints. The solution
                                 can optionally include the IM and Presence Service and Unity Connection. This guide assumes that you have already set up the
                                 following:

A basic Expressway-C and Expressway-E configuration, as specified in the Expressway Basic Configuration Deployment Guide (The document describes the networking options for deploying Expressway-E in the DMZ.)

Unified CM and IM and Presence Service are configured as specified in the configuration and management guides for your version, at Cisco Unified Communications Manager Configuration Guides .

If used, IM and Presence Service and/or Unity Connection are similarly configured as specified in the relevant Cisco Unified Communications Manager Configuration Guides .

### Protocol Summary

The following table lists the protocols and associated services used in the Unified Communications solution.

Protocol

Security

Services

SIP

TLS

Session establishment – Register, Invite etc.

HTTPS

TLS

Logon, provisioning, configuration, directory, Visual Voicemail

Media

SRTP

Media - audio, video, content sharing

XMPP

TLS

Instant Messaging, Presence, Federation

### Jabber Client Connectivity Without VPN

The MRA solution supports a hybrid on-premises and cloud-based service model, providing a consistent experience inside and
                                 outside the enterprise. MRA provides a secure connection for Jabber application traffic and other devices with the required capabilities to communicate without having to connect to the corporate
                                 network over a VPN. It is a device and operating system agnostic solution for Cisco Jabber clients on Windows, Mac, iOS and Android platforms.

MRA allows Jabber clients that are outside the enterprise to do the following:

Use Instant Messaging and Presence services

Make voice and video calls

Search the corporate directory

Share content

Launch a web conference

Access visual voicemail

Cisco Jabber Video for TelePresence ( Jabber Video ) does not work with MRA.

## Deployment Scenarios

This section describes the supported deployment environments:

Single network elements

Single clustered network elements

Multiple clustered network elements

Hybrid deployment

The only supported Mobile and Remote Access deployments are based on one-to-one Unified Communications zones between Expressway-C
                                       clusters and Expressway-E clusters.

### MRA with Standalone Network Elements

This scenario includes standalone (non-clustered) Unified CM , IM and Presence Service , Expressway-C, and Expressway-E servers.

### MRA with Clustered Network

In this scenario, each network element is clustered.

### MRA with Multiple Clustered Networks

In this scenario, there are multiple clusters of each network element.

Jabber clients can access their own cluster through any route.

Expressway-C uses round robin to select a node (publisher or subscriber) when routing home cluster discovery requests.

Each combination of Unified CM and IM and Presence Service clusters must use the same domain.

Intercluster peering must be set up between the IM and Presence Service clusters, and the Intercluster Sync Agent (ICSA) must be active.

#### Multiple Unified CM Clusters

If your MRA deployment includes multiple Unified CM clusters, configure Home Cluster Discovery for Unified CM. Expressway-C
                                 requires this configuration to direct MRA users to the correct home Unified CM cluster. Use either of the following configuration
                                 methods:

Configure an Intercluster Lookup Service (ILS) network between your remote Unified CM clusters. ILS cluster discovery finds
                                       and connects your remote Unified CM clusters into an intercluster network, populating the Cluster View on each cluster. ILS
                                       is the preferred option for larger intercluster networks, and also if you also want to replicate your enterprise dial plan
                                       across all Unified CM clusters. However, note that MRA doesn’t require dial plan replication to work.

Configure each Unified CM cluster with a list of all the remote clusters under the Unified CM Advanced Features > Cluster View menu. This option does not allow for dial plan replication.

## Unsupported Deployments

This topic highlights some deployments that are not supported over MRA.

### VPN Links

MRA doesn't support VPN links between the Expressway-C and the Unified CM services / clusters.

### Traversal Zones Between VCS Series and Expressway Series

MRA doesn't support “Mixed” traversal connections. Even though it's possible to configure traversal zones between Cisco VCS
                              and Cisco Expressway, MRA doesn't support them.

Explicitly, we don't support VCS Control traversal to Expressway-E, nor do we support Expressway-C traversal to VCS Expressway.

### Unclustered or Many-to-One Traversal Connections

We don't support Unified Communications zones from one Expressway-C cluster to multiple unclustered Expressway-Es.

We also don't support multiple Unified Communications zones from one Expressway-C cluster to multiple Expressway-Es or Expressway-E
                              clusters.

### Nested Perimeter Networks

MRA doesn't support chained traversal connections (using multiple Expressway-Es to cross multiple firewalls). You can't use
                              Expressway-E to give Mobile and Remote Access to endpoints that must traverse a nested perimeter network to call internal
                              endpoints.

### Expressway-C in DMZ with Static NAT

We don't support Expressway-C in a DMZ that uses static NAT. Static NAT firewall traversal requires SDP rewriting, which Expressway-C
                              doesn't support—use the Expressway-E instead.

### Unsupported Expressway Combinations

The following major Expressway-based deployments don't work together. You can't implement them together on the same Expressway
                                 (or traversal pair):

Mobile and Remote Access

Microsoft interoperability, using the Expressway-C-based B2BUA

Jabber Guest services

## Capacity Information

For details on MRA registration limits and other capacity information, refer to "Cluster License Usage and Capacity Guidelines" section in Cisco Expressway Administrator Guide at Expressway configuration guides page.

| Note | Third-party SIP or H.323 devices can register to the Expressway-C and, if necessary, interoperate with Unified CM -registered devices over a SIP trunk. |
|---|---|

| Date | Change | Reason |
|---|---|---|
| May 2023 | First published for X14.3. Included a section on "Enable IPv6 Over MRA". Unified CM is able to resolve automatically added Expressway-C hostname as MRA solution. Addressed CDETs. | X14.3 release |
| August 2022 | First published for X14.2. Moved a few related sections from the Release Note to this guide. | X14.2 release |
| May 2021 | First published for X14.0. The following are the changes in this release: Webex Client Embedded Browser Support SIP Registration Failover for Cisco Jabber - MRA Deployments | X14.0 release |
| December 2020 | First published for X12.7. The following are the changes in this release: Fast Path Registration for MRA (Caching Optimization for Registrations) Webex VDI over MRA | X12.7 release |
| October 2020 | First published for X12.6.3. The following are the changes in this release: Multiple Presence Domains over MRA MRA Documentation Enhancements: The Expressway MRA Deployment Guide has been updated and enhanced with the following new material: Multi-domain Scenarios — Overview, illustrations, and configuration summary designed to assist customers when deploying more
                                                         complex topologies in a multi-domain environment. Multi-cluster Scenarios — Best practices section with configuration tips and requirements for multi-cluster scenarios. Security Requirements — Clarifies the Unified CM security prerequisite for deploying Mobile and Remote Access. Also included are updates and edits to the following sections: Call Recording and Silent Monitoring support Key Expansion Module support Supported Clients Supported Endpoints | X12.6.3 release |
| September 2020 | First published for X12.6.2. The following are the changes in this release: Support for Whisper Coaching and Whisper Announcements Over MRA Support for Agent Greeting Over MRA Android PUSH for IMP over MRA is Disabled by Default | X12.6.2 release |
| July 2020 | First published for X12.6.1. The following are the changes in this release: Display Active MRA Registrations Count Support for BIB Silent Monitoring Over MRA | X12.6.1 release |
| July 2020 | A correction in the "Which MRA Features are Supported" section. | Document correction |
| June 2020 | Updated for the X12.6 release. | X12.6 release |
| April 2020 | Various clarifications and corrections to the guide. | Document corrections & enhancements |
| December 2019 | Various clarifications to the guide: Reverse DNS requirement updates TLS verify subject name requirement Minimum TLS version pre-11.5(1)SU3 No call preservation if node fails | Document corrections & enhancements |
| March 2019 | Clarify that from X12.5, local DNS no longer requires _cisco-uds._tcp.<domain> SRV records (still recommended). | Document correction |
| February 2019 | Clarify UID mapping is mandatory on IdP for single, cluster-wide SAML agreement. | Content enhancement |
| February 2019 | Add Jabber 12.5 clients to supported endpoints for ICE passthrough (subject to Unified CM 12.5). | Software dependency change |
| January 2019 | Fixed CE version for ICE support in MRA to 9.6.1 or later. Removed Jabber endpoints from ICE for MRA supported components. Correction to section Unsupported Expressway Features and Limitations for ICE for MRA with Static NAT. | Document correction |
| January 2019 | Updated for X12.5. | X12.5 release |
| September 2018 | Updated for X8.11.2 (change to Unsupported Expressway Features and Limitations for chat/messaging if user authentication by OAuth refresh). | X8.11.2 release |
| September 2018 | Updated for Webex and Spark platform rebranding, and for X8.11.1 maintenance release. Added, to Unsupported Expressway Features and Limitations section, a known issue with chat/messaging services over MRA if user authentication is by OAuth refresh (self-describing
                                             tokens). | X8.11.1 release Clarification |
| July 2018 | Included Hunt Group support, subject to Cisco Unified Communications Manager 11.5(1)SU5 or later fixed version. | Software dependency change |
| July 2018 | Updated for X8.11. Also removed port reference topic, which is now available in the Cisco Expressway IP Port Usage Guide . | X8.11 release |
| May 2018 | Clarify MFT over MRA is not supported when using an unrestricted version of IM and Presence Service . | Clarification |
| March 2018 | Clarify no Jabber support for redundant UDS services. | Clarification |
| December 2017 | Added configuration step to enable SIP protocol (disabled by default on new installs). | Content defect |
| November 2017 | Clarified which Cisco IP Phones in the 88xx series support MRA (Configuration Overview section). | Content defect |
| September 2017 | Added links to information about supported features for MRA-connected endpoints. Add information about Collaboration Solutions
                                             Analyzer. | Content enhancement |
| August 2017 | Deskphone control functions bullet removed from "Unsupported Contact Center Features" as not applicable. | Content defect |
| July 2017 | Clarify required versions for Unified Communications software. Corrected duplicated prerequisites for Push Notifications feature. | Content defect |
| July 2017 | Updated. | X8.10 release |
| April 2017 | Added details on partial support for Cisco Jabber SDK features. | Content defect |
| January 2017 | Updated section on unsupported features when using MRA. Added description of Maintenance Mode. Clarified that Expressway-C
                                             and Expressway-E need separate IP addresses. | X8.9.1 release |
| December 2016 | Updated. | X8.9 release |
| September 2016 | Unsupported deployments section updated. Minimum versions note about TLS added. | Clarification to avoid misconfiguration |
| August 2016 | Updated DNS prerequisite to create reverse lookup entries for Expressway-E. | Customer found defect |
| June 2016 | HTTP Allow list feature updates. | X8.8 release |
|  | Entries before X8.8 are removed for clarity |  |

| Protocol | Security | Services |
|---|---|---|
| SIP | TLS | Session establishment – Register, Invite etc. |
| HTTPS | TLS | Logon, provisioning, configuration, directory, Visual Voicemail |
| Media | SRTP | Media - audio, video, content sharing |
| XMPP | TLS | Instant Messaging, Presence, Federation |

| Note | Cisco Jabber Video for TelePresence ( Jabber Video ) does not work with MRA. |
|---|---|

| Note | The only supported Mobile and Remote Access deployments are based on one-to-one Unified Communications zones between Expressway-C
                                       clusters and Expressway-E clusters. |
|---|---|