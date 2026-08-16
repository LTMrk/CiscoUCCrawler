---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-6-exwy-b-mra-expressway-deployment-guide-exwy-b--9d1651393e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-6/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_011.html
retrieved_at: 2026-08-16T15:34:43.189066+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

Updated: June 3, 2020

Chapter: MRA Deployment Scenarios

## Chapter: MRA Deployment Scenarios

# MRA Deployment Scenarios

## Deployment Scope

The following major Expressway-based deployments don't work together. You can't implement them together on the same Expressway
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

### VPN Links

MRA doesn't support VPN links between the Expressway-C and the Unified CM services / clusters.

### Traversal Zones Between VCS Series and Expressway Series

MRA doesn't support "Mixed" traversal connections. Even though it's possible to configure traversal zones between Cisco VCS and Cisco Expressway , MRA doesn't support them.

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

You could potentially place the Expressway-C in a DMZ that doesn't use static NAT. However, we strongly discourage this deployment
                              because it requires extensive management on the inmost firewall. We always recommend placing the Expressway-C in the internal
                              network.

| Note | The only supported Mobile and Remote Access deployments are based on one-to-one Unified Communications zones between Expressway-C
                                       clusters and Expressway-E clusters. |
|---|---|