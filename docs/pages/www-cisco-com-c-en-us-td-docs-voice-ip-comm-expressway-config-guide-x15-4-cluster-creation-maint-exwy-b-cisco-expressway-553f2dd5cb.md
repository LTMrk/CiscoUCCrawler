---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-4-cluster-creation-maint-exwy-b-cisco-expressway-553f2dd5cb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-4/cluster_creation_maint/exwy_b_cisco-expressway-cluster-creation-and-maintenance-deployment-guide-x154/exwy_m_clustering-basics.html
retrieved_at: 2026-08-16T15:11:49.660897+00:00
---

Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X15.4)

# Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X15.4)

Updated: February 9, 2026

Chapter: Clustering Basics

## Chapter: Clustering Basics

# Clustering Basics

This chapter explains the following:

## Overview

An Expressway can be part of a cluster of up to six Expressways. Each Expressway in the cluster is a peer of every other one
                           in that cluster. When you create a cluster you nominate one peer as the primary, from which its configuration is replicated
                           to the other peers.

Every Expressway peer in the cluster must have the same routing capabilities — if any Expressway can route a call to a destination
                           it is assumed that all Expressway peers in that cluster can route a call to that destination. If routing is different on different
                           Expressway peers, then you need to use separate Expressways / Expressway clusters.

### Benefits of Clustering

Clustered Expressways can provide benefits for both capacity and resilience:

Capacity . Clustering can increase the capacity of an Expressway deployment by a maximum factor of four, compared with a single Expressway.

Resilience . Clustering can provide redundancy while an Expressway is in maintenance mode, or in case it becomes inaccessible due to
                                    a network or power outage, or other reason. The Expressway peers in a cluster share bandwidth usage as well as routing, zone,
                                    and other configuration. Endpoints can register to any of the peers in the cluster, so if an endpoint loses connection to
                                    its initial peer, it can re-register to another one in the cluster.

### About Capacity Gain

There is no capacity gain after four peers. So in a six-peer cluster for example, the fifth and sixth Expressways do not add extra call capacity to the cluster. Resilience
                              is improved with the extra peers, but not capacity.

The Small Expressway VMs are intended for Cisco Business Edition 6000 customers, so clustering of Small VMs only provides redundancy and does not provide any additional scale benefit.

### About Licensing

Capacity licensing is done on a per-cluster basis, and all capacity licenses installed on a cluster peer are available to
                              any peer in the cluster. This includes Rich Media Session licenses and room system & desktop system registration licenses.
                              More details are provided in License Usage Within a Cluster