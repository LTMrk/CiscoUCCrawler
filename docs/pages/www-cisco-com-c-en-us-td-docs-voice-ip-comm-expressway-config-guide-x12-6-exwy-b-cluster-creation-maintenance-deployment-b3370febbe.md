---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-6-exwy-b-cluster-creation-maintenance-deployment-b3370febbe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-6/exwy_b_cluster-creation-maintenance-deployment-guide/exwy_b_cluster-creation-maintenance-deployment-guide_chapter_011.html
retrieved_at: 2026-08-16T15:32:19.919163+00:00
---

Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X12.6)

# Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X12.6)

Updated: June 3, 2020

Chapter: Clustering Requirements

## Chapter: Clustering Requirements

# Clustering Requirements

## Clustering Requirements

Before setting up a cluster of Expressway peers or adding an Expressway to a cluster, ensure that the following requirements
                           are met:

### Do Not Mix Expressway-C and Expressway-E

A cluster must contain only Expressway-C nodes or only Expressway-E nodes. They cannot be mixed in the same cluster.

### Platform and software versions match

All clusters peers are running the same Expressway software version. The only case when different peers are allowed to run
                                    different versions of code is for the short period of time while a cluster is being upgraded from one version of code to another,
                                    during which time the cluster operates in a partitioned fashion.

Each peer is using a hardware platform (appliance or virtual machine) with equivalent capabilities. For example, you can cluster
                                    peers that are running on standard appliances with peers running on 2 core Medium VMs, but you can't cluster a peer running
                                    on a standard appliance with peers running on 8 core Large VMs.

### Network conditions are met

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

### Basic configuration is done

Each peer has a different system name to all other peers.

All cluster peers are configured in the same domain.

Each peer has a certificate that identifies it to other peers (minimum required for default of TLS verification mode set to Permissive ).

If you want authenticated TLS connections, the certificate must also be valid and be issued by an authority that is trusted
                                    by all peers ( TLS Verification mode set to Enforce ). We recommend populating the CN of all peer certificates with the same cluster FQDN, and populating each peer certificate's
                                    SAN with that peer's FQDN.

Although using one certificate for multiple Expressways in one cluster is supported, this is not recommended due to the security
                                                risk. That is, if one private key is compromised on one device, it means all devices in the cluster are compromised.

If you have systems that still use option keys, all peers have the same set of option keys installed, with the following exceptions:

RMS licenses

Room system registration licenses

Desktop system registration licenses

H.323 mode is enabled on each peer ( Configuration > Protocols > H.323 , and for H.323 mode select On ).

The cluster uses H.323 signaling between peers to determine the best route for calls, even if all endpoints are SIP endpoints.

The firewall rules on each peer are configured to block connections to the clustering TLS ports, from all IP addresses except
                                    those of its peers.

### DNS configuration is done

DNS server configuration does not replicate so you must enter the DNS server address(es) on each peer.

The DNS servers used by the Expressway peers must support both forward and reverse DNS lookups of Cisco TMS and all Expressway
                                    peer addresses. The DNS servers must also provide address lookup for any other DNS functionality required, such as:

NTP servers or the external manager if they configured using DNS names

Microsoft FE Server FQDN lookup

LDAP server forward and reverse lookup (reverse lookups are frequently provided through PTR records)

Expressway-E typically uses a public DNS, but it's undesirable to use the public DNS to resolve private IP addresses. It's also undesirable to cluster on the public addresses of the Expressway-E peers. For these reasons, we recommend
                                                you use cluster address mapping to resolve the peers' FQDNs to private IP addresses.

For details, see the Cisco Expressway Cluster Creation and Maintenance Deployment Guide for your version, on the Cisco Expressway Series configuration guides page.

A DNS SRV record is recommended for the cluster, which contains A or AAAA records for each peer.

This configuration is advised for video interoperability and business to business (B2B) video calling, but not  for Mobile and Remote Access .

(For MRA) Create a collab-edge SRV record for each peer in the Expressway-E cluster.

(For B2B only) The Expressway-E cluster has a DNS SRV record that defines all cluster peers.

### TMS is configured (if necessary)

Cisco TMS, if used, is running version 13.2 or later (12.6 or later is permitted if you are not using Cisco TMS for provisioning
                                    or FindMe).

If Cisco TMS is to be used for replicating FindMe and/or Provisioning data, ensure that Provisioning Extension mode functionality
                                    is enabled on Cisco TMS (see Cisco TMS Provisioning Extension Deployment Guide for details).

### Clusters with mixed CE1200 and CE1100 physical appliances

To add a CE1200 appliance to an existing cluster that has CE1100 models in it, configure the Type option to match the other
                              peers (Expressway-E or Expressway-C) through the service setup wizard on the Status > Overview page, before you add the CE1200 to the cluster.

If you have clusters with mixed appliance types in them, be aware that every peer must run the same software version. Not all appliance types support all software versions - please check first in the appliance installation guides that the units you want to mix can all support the same software
                              version.

| Note | Although using one certificate for multiple Expressways in one cluster is supported, this is not recommended due to the security
                                                risk. That is, if one private key is compromised on one device, it means all devices in the cluster are compromised. |
|---|---|

| Note | Expressway-E typically uses a public DNS, but it's undesirable to use the public DNS to resolve private IP addresses. It's also undesirable to cluster on the public addresses of the Expressway-E peers. For these reasons, we recommend
                                                you use cluster address mapping to resolve the peers' FQDNs to private IP addresses. |
|---|---|