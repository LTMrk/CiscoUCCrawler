---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-3-cluster-creation-maint-exwy-b-cisco-expressway-6d06a3bbf2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-3/cluster_creation_maint/exwy_b_cisco-expressway-cluster-creation-and-maintenance-deployment-guide-x143/exwy_m_clustering-requirements.html
retrieved_at: 2026-08-16T15:17:38.723516+00:00
---

Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X14.3)

# Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X14.3)

Updated: March 18, 2025

Chapter: Clustering Requirements

## Chapter: Clustering Requirements

# Clustering Requirements

Before setting up a cluster of Expressway peers or adding an Expressway to a cluster, ensure that the following requirements
                        are met:

This chapter explains the following:

## Do Not Mix Expressway-C and Expressway-E

A cluster must contain only Expressway-C nodes or only Expressway-E nodes. They cannot be mixed in the same cluster.

## Platform and Software Versions Match

All clusters peers are running the same Expressway software version. The only case when different peers are allowed to run
                                 different versions of code is for the short period of time while a cluster is being upgraded from one version of code to another,
                                 during which time the cluster operates in a partitioned fashion.

Each peer is using a hardware platform (appliance or virtual machine) with equivalent capabilities. For example, you can cluster
                                 peers that are running on standard appliances with peers running on 2 core Medium VMs, but you can't cluster a peer running
                                 on a standard appliance with peers running on 8 core Large VMs.

## Network Conditions Are Met

Each peer has a different LAN configuration (a different IPv4 address and a different IPv6 address, where enabled).

Expressway supports a round trip delay of up to 80ms. This means that each Expressway in the cluster must be within a 40ms
                                 hop of all other peers in the cluster.

Each peer in a cluster is directly routable to each and every other Expressway in or to be added to the cluster. (There must
                                 be no NAT between cluster peers – if there is a firewall ensure that the required ports are opened.)

External firewalls are configured to block access to the clustering TLS ports.

The network connections between the peers must be reliable during cluster forming or changing procedures.

Clustering procedures must be carried out in the correct sequence, and the primary peer must start first. If other peers start
                                 first they can try to assume control of the cluster, resulting in inconsistent configuration state that is hard to recover
                                 from.

## Basic Configuration Is Done

Each peer has a different system name to all other peers.

Configure all cluster peers in the same domain.

Each peer has a certificate that identifies it to other peers (minimum required for default of TLS Verification mode set to Permissive ).

Although we support using one certificate for multiple Expressways in one cluster, this isn't recommended due to the security
                                             risk. That is, if one private key is compromised on one device, all devices in the cluster are compromised.

If you have systems that still use option keys, all peers have the same set of option keys installed, with the following exceptions:

RMS licenses

Room system registration licenses

Desktop system registration licenses

Enable H.323 mode on each peer ( Configuration > Protocols > H.323 , and for H.323 mode select On ).

The cluster uses H.323 signaling between peers to determine the best route for calls, even if all endpoints are SIP endpoints.

Configure the firewall rules on each peer to block connections to clustering TLS ports, from all IP addresses except its peers.

## DNS Configuration Is Done

DNS server configuration does not replicate so you must enter the DNS server address(es) on each peer.

The DNS servers used by the Expressway peers must support both forward and reverse DNS lookups of Cisco TMS and all Expressway
                                 peer addresses. The DNS servers must also provide address lookup for any other DNS functionality required, such as:

NTP servers or the external manager if they configured using DNS names

Microsoft FE Server FQDN lookup

LDAP server forward and reverse lookup (reverse lookups are frequently provided through PTR records)

Expressway-E typically uses a public DNS, but it's undesirable to use the public DNS to resolve private IP addresses. It's also undesirable to cluster on the public addresses of the Expressway-E peers. For these reasons, we recommend
                                             you use cluster address mapping to resolve the peers' FQDNs to private IP addresses.

For details, see the Cisco Expressway Cluster Creation and Maintenance Deployment Guide for your version, on the Cisco Expressway Series Configuration Guides page.

A DNS SRV record is recommended for the cluster, which contains A or AAAA records for each peer.

This configuration is advised for video interoperability and business to business (B2B) video calling, but not  for Mobile and Remote Access .

(For MRA) Create a collab-edge SRV record for each peer in the Expressway-E cluster.

(For B2B only) The Expressway-E cluster has a DNS SRV record that defines all cluster peers.

## TMS Is Configured (When Essential)

Cisco TMS, if used, is running version 13.2 or later (12.6 or later is permitted if you are not using Cisco TMS for provisioning
                                 or FindMe).

If Cisco TMS is to be used for replicating FindMe and/or Provisioning data, ensure that Provisioning Extension mode functionality
                                 is enabled on Cisco TMS (see Cisco TMS Provisioning Extension Deployment Guide for details).

## Clusters With Mixed CE1200 and CE1100 Physical Appliances

To add a CE1200 appliance to an existing cluster that has CE1100 models in it, configure the Type option to

match the other peers (Expressway-E or Expressway-C) through the service setup wizard on the Status > Overview page, before you add the CE1200 to the cluster.

If you have clusters with mixed appliance types in them, be aware that every peer must run the same software version. Not all appliance types support all software versions - please check first in the appliance installation guides that the units you want to mix can all support the same software
                           version.

## Mix Cluster Deployment With Expressway and Expressway Select

Expressway clusters consisting of Expressway and Expressway Select peers are not supported. Instead, all peers within a cluster
                                          must either run the Expressway software image or the Expressway Select software image.

| Note | Although we support using one certificate for multiple Expressways in one cluster, this isn't recommended due to the security
                                             risk. That is, if one private key is compromised on one device, all devices in the cluster are compromised. |
|---|---|

| Note | Expressway-E typically uses a public DNS, but it's undesirable to use the public DNS to resolve private IP addresses. It's also undesirable to cluster on the public addresses of the Expressway-E peers. For these reasons, we recommend
                                             you use cluster address mapping to resolve the peers' FQDNs to private IP addresses. |
|---|---|

| Note | Expressway clusters consisting of Expressway and Expressway Select peers are not supported. Instead, all peers within a cluster
                                          must either run the Expressway software image or the Expressway Select software image. |
|---|---|