---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-7-exwy-b-mra-deployment-exwy-m-mra-overview-and--85a0534885
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-7/exwy_b_mra-deployment/exwy_m_mra-overview-and-planning.html
retrieved_at: 2026-08-16T15:33:57.065414+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.7)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.7)

Updated: December 11, 2020

Chapter: MRA Overview

## Chapter: MRA Overview

# MRA Overview

## About Mobile and Remote Access

Cisco Unified Communications Mobile and Remote Access (MRA) is part of the Cisco Collaboration Edge Architecture. MRA allows
                           endpoints such as Cisco Jabber to have their registration, call control, provisioning, messaging and presence services provided by Cisco Unified Communications Manager ( Unified CM ) when the endpoint is outside the enterprise network. The Expressway provides secure firewall traversal and line-side support
                           for Unified CM registrations.

The MRA solution provides the following functions:

Off-premises access : a consistent experience outside the network for Jabber and EX/MX/SX Series clients

Security : secure business-to-business communications

Cloud services : enterprise grade flexibility and scalable solutions providing rich Cisco Webex integration and service provider offerings

Gateway and interoperability services : media and signaling normalization, and support for nonstandard endpoints

Third-party SIP or H.323 devices can register to the Expressway-C and, if necessary, interoperate with Unified CM -registered devices over a SIP trunk.

Unified CM provides call control for both mobile and on-premises endpoints. Signaling traverses the Expressway solution between the
                           mobile endpoint and Unified CM . Media traverses the Expressway solution, which relays the media between the endpoints directly. All media is encrypted between
                           the Expressway-C and the mobile endpoint.

### Core Components

Any MRA solution requires Expressway and Unified CM, with MRA-compatible soft clients and/or fixed endpoints. The solution
                                 can optionally include the IM and Presence Service and Unity Connection. This guide assumes that you have already set up the
                                 following:

A basic Expressway-C and Expressway-E configuration, as specified in the Expressway Basic Configuration (Expressway-C with Expressway-E) Deployment Guide (The document describes the networking options for deploying Expressway-E in the DMZ.)

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

This scenario includes standalone (nonclustered) Unified CM , IM and Presence Service , Expressway-C, and Expressway-E servers.

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

For details on MRA registration limits and other capacity information, refer to "Cluster License Usage and Capacity Guidelines" in Cisco Expressway Administrator Guide . You can find this guide on the Expressway configuration guides page.

| Note | Third-party SIP or H.323 devices can register to the Expressway-C and, if necessary, interoperate with Unified CM -registered devices over a SIP trunk. |
|---|---|

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