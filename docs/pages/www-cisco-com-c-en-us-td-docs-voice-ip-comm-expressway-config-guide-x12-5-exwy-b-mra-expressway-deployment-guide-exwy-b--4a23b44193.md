---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-5-exwy-b-mra-expressway-deployment-guide-exwy-b--4a23b44193
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-5/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_011.html
retrieved_at: 2026-08-16T15:35:46.726390+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

Updated: May 1, 2019

Chapter: MRA Deployment Scenarios

## Chapter: MRA Deployment Scenarios

# MRA Deployment Scenarios

## Deployment Scope

The following major Expressway-based deployments do not work together. They cannot be implemented together on the same Expressway
                           (or traversal pair):

Mobile and Remote Access

Microsoft interoperability, using the Expressway-C-based B2BUA

Jabber Guest services

## Deployment Scenarios

This section describes the supported deployment environments:

Single network elements

Single clustered network elements

Multiple clustered network elements

Hybrid deployment

The only supported Mobile and Remote Access deployments are based on one-to-one Unified Communications zones between Expressway-C
                                       clusters and Expressway-E clusters.

### MRA with Standalone Network Elements

In this scenario there are single (non-clustered) Unified CM , IM and Presence Service , Expressway-C, and Expressway-E servers.

### MRA with Clustered Network

In this scenario each network element is clustered.

### MRA with Multiple Clustered Networks

In this scenario there are multiple clusters of each network element.

Jabber clients can access their own cluster through any route.

Expressway-C uses round robin to select a node (publisher or subscriber) when routing home cluster discovery requests.

Each combination of Unified CM and IM and Presence Service clusters must use the same domain.

Intercluster Lookup Service (ILS) must be active on the Unified CM clusters.

Intercluster peer links must be configured between the IM and Presence Service clusters, and the Intercluster Sync Agent (ICSA) must be active.

### MRA as a Hybrid Deployment (using WebEx Cloud)

In this scenario, IM and Presence Service for Jabber clients are provided via the Webex cloud.

### Jabber with Team Messaging Mode

## Unsupported Deployments

### VPN Links

VPN links, between the Expressway-C and the Unified CM services / clusters, are not supported.

### Traversal Zones Between VCS Series and Expressway Series

"Mixed" traversal connections are not supported. That is, we do not support traversal zones, or Unified Communications traversal
                              zones, between Cisco VCS and Cisco Expressway even though it is possible to configure these zones .

Explicitly, we do not support VCS Control traversal to Expressway-E, nor do we support Expressway-C traversal to VCS Expressway.

### Unclustered or Many-to-One Traversal Connections

We do not support Unified Communications zones from one Expressway-C cluster to multiple unclustered Expressway-Es.

We also do not support multiple Unified Communications zones from one Expressway-C cluster to multiple Expressway-Es or Expressway-E
                              clusters.

### Nested Perimeter Networks

MRA is not currently supported over chained traversal connections (using multiple Expressway-Es to cross multiple firewalls).

This means that you cannot use Expressway-E to give Mobile and Remote Access to endpoints that must traverse a nested perimeter
                              network to call internal endpoints.

### Expressway-C in DMZ with Static NAT

We do not support Expressway-C in a DMZ that uses static NAT. This is because the Expressway-C does not perform the SDP rewriting
                              that is required to traverse static NAT-enabled firewalls. You should use the Expressway-E for this purpose.

You could potentially place the Expressway-C in a DMZ that does not use static NAT, but we strongly discourage this deployment
                              because it requires a lot of management on the inmost firewall. We always recommend placing the Expressway-C in the internal
                              network.

| Note | The only supported Mobile and Remote Access deployments are based on one-to-one Unified Communications zones between Expressway-C
                                       clusters and Expressway-E clusters. |
|---|---|