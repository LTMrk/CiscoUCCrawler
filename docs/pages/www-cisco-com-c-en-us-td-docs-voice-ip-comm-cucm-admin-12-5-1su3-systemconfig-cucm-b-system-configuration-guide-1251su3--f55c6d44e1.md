---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-systemconfig-cucm-b-system-configuration-guide-1251su3--f55c6d44e1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/systemConfig/cucm_b_system-configuration-guide-1251su3/cucm_m_intercluster-lookup-service.html
retrieved_at: 2026-08-16T17:42:05.070439+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Configure Intercluster Lookup Service

## Chapter: Configure Intercluster Lookup Service

# Configure Intercluster Lookup Service

## ILS Overview

The Cisco Intercluster Lookup Service (ILS) makes it easy to create a multi-cluster network of remote Cisco Unified Communications
                              Manager clusters that share data.

ILS eliminates the need for an administrator having to configure connections between clusters manually. Once you have ILS
                              configured on a hub cluster, you can connect new clusters by enabling ILS on the new cluster and pointing the new cluster
                              to an existing hub. ILS connects the clusters automatically and lets both clusters know the topology of the larger ILS network.

### ILS Network Components

An ILS network comprises the following components:

Hub clusters —Hub clusters form the backbone of an ILS network using automesh functionality to create a full mesh topology with the other
                                    hub clusters. Hub clusters relay and share information across the ILS network for a variety of features.

Spoke clusters —Spoke clusters connect only to their local hub cluster and never contact other hub or spoke clusters directly. Spoke clusters
                                    rely on their local hub to share and relay information across the network.

Global dial plan imported catalogs —This optional component applies if you have Global Dial Plan Replication configured, and you are interoperating with a Cisco
                                    TelePresence Video Communications Server, or a third-party call control system. Import a directory URI or +E.164 number catalog
                                    manually from a CSV file that was exported from the other system, thereby allowing users in the ILS network to call users
                                    from the other system.

### Cluster View

The remote cluster view functionality of ILS can be used to map the network. Each cluster exchanges update messages, called
                              peer info vectors, that inform remote clusters of the status of each cluster in the network. The update messages contain information
                              about the known clusters in the network, including:

Cluster IDs

Peer IDs for the publisher

Cluster descriptions and versions

Fully Qualified Domain Name (FQDN) of the host

IP addresses and host names for the cluster nodes that have ILS activated

### Feature Support

Features such as Global Dial Plan Replication and Extension Mobility Roaming are dependent on ILS to create intercluster networks
                              where the clusters share dial plan information. This lets you set up intercluster call networks with video calling, URI dialing,
                              and intercluster mobility.

ILS is also used by Centralized Deployments of the IM and Presence Service if you are connecting the IM and Presence central
                              cluster to multiple telephony clusters. ILS is used to create the connections between the IM and Presence central cluster
                              and the telephony clusters.

### ILS Networking Capacities

Following are recommended capacities to keep in mind when planning an ILS network:

ILS networking supports up to 10 hub clusters with 20 spoke clusters per hub, up to a 200 total cluster maximum. A hub and
                                       spoke combination topology is used to avoid many TCP connections created within each cluster.

There may be a performance impact with utilizing your hub and spoke clusters at, or above, their maximums. Adding too many
                                       spoke clusters to a single hub creates extra connections that may increase the amount of memory or CPU processing. We recommend
                                       that you connect to a hub cluster with no more than 20 spoke clusters.

ILS networking adds extra CPU processing to your system. The CPU utilization and sync time is dependent on the number of records
                                       that are being synced across the cluster. When planning your hub and spoke topology, make sure that your hub clusters have
                                       the CPU to handle the load.

## ILS Configuration Task Flow

### Before you begin

Step 1

Configure Cluster IDs

Each cluster within the ILS network must have a unique Cluster ID

Step 2

Configure ILS

Configure and activate ILS in the various clusters of your network.

Step 3

Verify that ILS is Running

Confiirm that the ILS network is up and running.

Step 4

Configure Remote Cluster View

Configure the remote cluster view for your ILS network.

### Configure Cluster IDs

Step 1

Log in to Cisco Unified CM Administration on the publisher node.

Step 2

Choose System > Enterprise Parameters .

Step 3

Set the value of the Cluster ID to a value that uniquely identifies the cluster.

Step 4

Click Save .

Step 5

Repeat this procedure on the publisher node of each cluster.

### Configure ILS

Step 1

Log into Cisco Unified CM Administration on the publisher node.

Step 2

Choose Advanced Features > ILS Configuration .

Step 3

From the Role drop-down list box, select Hub Cluster or Spoke Cluster depending on which type of cluster you are setting up.

Step 4

If you want to enable Global Dial Plan Replication, check the Exchange Global Dial Plan Replication Data with Remote Clusters check box.

When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS.

Step 5

Configure ILS Authentication Details between the various clusters in the network:

- For TLS authentication, check the Use TLS Certificates check box. Note that if you choose this option, you must also exchange CA-signed certificates between the nodes in your cluster.

- For password authentication (regardless of whether TLS is used), check the Use Password check box and enter the password details.

Step 6

Click Save .

Step 7

In the ILS Cluster Registration popup, configure your registration details:

In the Registration Server text box, enter the publisher node IP address or FQDN for the hub cluster to which you want to connect this cluster. If this
                                                is the first hub cluster in your network, you can leave the field blank

Make sure that the Activate the Intercluster Lookup Service on the publisher in this cluster check box is checked.

Click OK .

Step 8

Repeat this procedure on the publisher node of each cluster that you want to add to the ILS network. Add the new cluster as
                                          a hub or spoke cluster.

If you chose to use Transport Layer Security (TLS) authentication between clusters, you must exchange Tomcat certificates
                                 between the publisher node of each cluster in the ILS network. From Cisco Unified Operating System Administration, use the
                                 Bulk Certificate Management feature to:

Export certificates from the publisher node of each cluster to a central location

Consolidate exported certificates in the ILS network

Import certificates onto the publisher node of each cluster in your network

For details, see the "Manage Certificates" chapter of the Administration Guide for Cisco Unified Communications Manager .

### Verify that ILS is Running

Step 1

Log in to the publisher node on any of your telephony clusters.

Step 2

From Cisco Unified CM Administration choose Advanced Features > ILS Configuration .

Step 3

Check the ILS Clusters and Global Dial Plan Imported Catalogs section. Your ILS network topology should appear.

### Configure Remote Cluster View

Step 1

In Cisco Unified CM Administration, choose Advanced Features > Cluster View .

Step 2

In the Find and List Remote Clusters window, choose any previously created remote cluster.

Step 3

From the Remote Cluster Service Configuration window, check the appropriate check box to configure services such as Extension
                                          Mobility Cross Cluster, TFTP, and RSVP Agent for remote clusters.

Step 4

Click Save .

## ILS Interactions
                        	 and Restrictions

### ILS
                           	 Interactions

Feature

Interaction

Cluster
                                             					 discovery

ILS
                                             					 cluster discovery allows Cisco Unified Communications Manager clusters to learn
                                             					 dynamically about remote clusters without the need for an administrator to
                                             					 manually configure connections between those clusters.

Each cluster in an ILS network exchange update messages, called peer info vectors, that are designed to inform remote clusters
                                             of the status of each cluster in the network. The update messages contain information about the known clusters in the network,
                                             including:

- Cluster IDs

- Cluster descriptions and versions

- Fully qualified domain name of the host

- IP addresses and hostnames for the cluster nodes that have ILS activated

The ILS
                                             					 cluster discovery feature automatically populates the list of remote clusters
                                             					 that can be viewed in Cisco Unified CM Administration by choosing Advanced
                                                   						  Features > Cluster View . From this window, you
                                             					 can configure services such as Extension Mobility Cross Cluster, TFTP, and RSVP
                                             					 Agent for remote clusters.

A fully qualified domain name of the remote cluster, as seen in the Cluster View, must be DNS resolvable for ILS discovery
                                                         to work.

Global
                                             					 Dial Plan Replication

When
                                             					 Global Dial Plan Replication is enabled across an ILS network, remote clusters
                                             					 in an ILS network share global dial plan data, including the following:

- Directory URIs

- Alternate numbers

- Alternate number patterns

- Route strings

- PSTN failover numbers

Block Inbound Calls

To block Inbound calls based on calling party number in an ILS-based network, you must include the SIP route pattern's partition
                                             in the calling party's CSS. For example, if the call originates from SIP Trunk then SIP trunk inbound CSS must have SIP route
                                             pattern's partition.

### ILS
                           	 Restrictions

Restriction

Description

ILS
                                             					 Service

The ILS
                                             					 Service runs only on the Unified Communications manager publisher node.

Clusters

A hub
                                             					 cluster can have many spokes but, a spoke cluster can have only one hub
                                             					 cluster.

ILS
                                             					 Network

You cannot
                                             					 connect a third-party call control system into an ILS network.

Cluster
                                             					 Import

You can
                                             					 import a third-party catalog into a hub cluster only.

Duplicated
                                             					 URI

If a
                                             					 learned ILS cluster contains duplicated URIs from a different remote cluster
                                             					 and when a call is placed to that URI, it will be routed to the cluster whose
                                             					 URI has been learned and inserted into the database first.

Database
                                             					 Replication Status

Although
                                             					 the Global dial plan data is exchanged successfully on the ILS Network, an ILS
                                             					 receiving cluster will not write learned information into the database until it
                                             					 completes its database replication status.

Import

For
                                             					 imported third-party directory URIs and patterns, the CSV file format must
                                             					 match the exact syntax as shown in the administration window sample file
                                             					 otherwise, the import fails.

ILS Hub

When adding an additional hub cluster into the ILS network ensure to verify the following conditions are met for the primary
                                             ILS hub node:

Cluster ID is unique across all the hub nodes in the ILS cluster.

Fully Qualified Domain Name (FQDN) is configured.

UDS and EM services are running on the all of the hub nodes in the ILS cluster

DNS primary and reverse resolution are working fine.

Import consolidated Tomcat certificates from all the hub nodes.

Else, the "version" information will not get displayed in the Find and List Remote Clusters window even
                                             					 after rebooting the clusters or correcting the errors. The workaround is to
                                             					 remove the hub cluster from the ILS network, comply with the above requirements
                                             					 and add the hub cluster back into the ILS network.

| Note | These recommendations are based on system testing and taking resource utilization into account. Although the system does not
                                          prevent you from exceeding these recommendations, by doing so you would risk the overutilization of resources. Cisco recommends
                                          the above capacities for optimal performance. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Cluster IDs | Each cluster within the ILS network must have a unique Cluster ID |
| Step 2 | Configure ILS | Configure and activate ILS in the various clusters of your network. |
| Step 3 | Verify that ILS is Running | Confiirm that the ILS network is up and running. |
| Step 4 | Configure Remote Cluster View | Configure the remote cluster view for your ILS network. |

| Step 1 | Log in to Cisco Unified CM Administration on the publisher node. |
|---|---|
| Step 2 | Choose System > Enterprise Parameters . |
| Step 3 | Set the value of the Cluster ID to a value that uniquely identifies the cluster. |
| Step 4 | Click Save . |
| Step 5 | Repeat this procedure on the publisher node of each cluster. |

| Note | The first cluster that you configure must be a hub cluster. |
|---|---|

| Step 1 | Log into Cisco Unified CM Administration on the publisher node. |
|---|---|
| Step 2 | Choose Advanced Features > ILS Configuration . |
| Step 3 | From the Role drop-down list box, select Hub Cluster or Spoke Cluster depending on which type of cluster you are setting up. |
| Step 4 | If you want to enable Global Dial Plan Replication, check the Exchange Global Dial Plan Replication Data with Remote Clusters check box. Note When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS. | Note | When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS. |
| Note | When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS. |
| Step 5 | Configure ILS Authentication Details between the various clusters in the network: For TLS authentication, check the Use TLS Certificates check box. Note that if you choose this option, you must also exchange CA-signed certificates between the nodes in your cluster. For password authentication (regardless of whether TLS is used), check the Use Password check box and enter the password details. |
| Step 6 | Click Save . |
| Step 7 | In the ILS Cluster Registration popup, configure your registration details: In the Registration Server text box, enter the publisher node IP address or FQDN for the hub cluster to which you want to connect this cluster. If this
                                                is the first hub cluster in your network, you can leave the field blank Make sure that the Activate the Intercluster Lookup Service on the publisher in this cluster check box is checked. Click OK . |
| Step 8 | Repeat this procedure on the publisher node of each cluster that you want to add to the ILS network. Add the new cluster as
                                          a hub or spoke cluster. Note Depending on the sync values that you configured, there may be a delay while the cluster information propagates throughout
                                                      the network. | Note | Depending on the sync values that you configured, there may be a delay while the cluster information propagates throughout
                                                      the network. |
| Note | Depending on the sync values that you configured, there may be a delay while the cluster information propagates throughout
                                                      the network. |

| Note | When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS. |
|---|---|

| Note | Depending on the sync values that you configured, there may be a delay while the cluster information propagates throughout
                                                      the network. |
|---|---|

| Step 1 | Log in to the publisher node on any of your telephony clusters. |
|---|---|
| Step 2 | From Cisco Unified CM Administration choose Advanced Features > ILS Configuration . |
| Step 3 | Check the ILS Clusters and Global Dial Plan Imported Catalogs section. Your ILS network topology should appear. |

| Step 1 | In Cisco Unified CM Administration, choose Advanced Features > Cluster View . |
|---|---|
| Step 2 | In the Find and List Remote Clusters window, choose any previously created remote cluster. |
| Step 3 | From the Remote Cluster Service Configuration window, check the appropriate check box to configure services such as Extension
                                          Mobility Cross Cluster, TFTP, and RSVP Agent for remote clusters. |
| Step 4 | Click Save . |

| Feature | Interaction |
|---|---|
| Cluster
                                             					 discovery | ILS
                                             					 cluster discovery allows Cisco Unified Communications Manager clusters to learn
                                             					 dynamically about remote clusters without the need for an administrator to
                                             					 manually configure connections between those clusters. Each cluster in an ILS network exchange update messages, called peer info vectors, that are designed to inform remote clusters
                                             of the status of each cluster in the network. The update messages contain information about the known clusters in the network,
                                             including: Cluster IDs Cluster descriptions and versions Fully qualified domain name of the host IP addresses and hostnames for the cluster nodes that have ILS activated The ILS
                                             					 cluster discovery feature automatically populates the list of remote clusters
                                             					 that can be viewed in Cisco Unified CM Administration by choosing Advanced
                                                   						  Features > Cluster View . From this window, you
                                             					 can configure services such as Extension Mobility Cross Cluster, TFTP, and RSVP
                                             					 Agent for remote clusters. Note A fully qualified domain name of the remote cluster, as seen in the Cluster View, must be DNS resolvable for ILS discovery
                                                         to work. | Note | A fully qualified domain name of the remote cluster, as seen in the Cluster View, must be DNS resolvable for ILS discovery
                                                         to work. |
| Note | A fully qualified domain name of the remote cluster, as seen in the Cluster View, must be DNS resolvable for ILS discovery
                                                         to work. |
| Global
                                             					 Dial Plan Replication | When
                                             					 Global Dial Plan Replication is enabled across an ILS network, remote clusters
                                             					 in an ILS network share global dial plan data, including the following: Directory URIs Alternate numbers Alternate number patterns Route strings PSTN failover numbers |
| Block Inbound Calls | To block Inbound calls based on calling party number in an ILS-based network, you must include the SIP route pattern's partition
                                             in the calling party's CSS. For example, if the call originates from SIP Trunk then SIP trunk inbound CSS must have SIP route
                                             pattern's partition. |

| Note | A fully qualified domain name of the remote cluster, as seen in the Cluster View, must be DNS resolvable for ILS discovery
                                                         to work. |
|---|---|

| Restriction | Description |
|---|---|
| ILS
                                             					 Service | The ILS
                                             					 Service runs only on the Unified Communications manager publisher node. |
| Clusters | A hub
                                             					 cluster can have many spokes but, a spoke cluster can have only one hub
                                             					 cluster. |
| ILS
                                             					 Network | You cannot
                                             					 connect a third-party call control system into an ILS network. |
| Cluster
                                             					 Import | You can
                                             					 import a third-party catalog into a hub cluster only. |
| Duplicated
                                             					 URI | If a
                                             					 learned ILS cluster contains duplicated URIs from a different remote cluster
                                             					 and when a call is placed to that URI, it will be routed to the cluster whose
                                             					 URI has been learned and inserted into the database first. |
| Database
                                             					 Replication Status | Although
                                             					 the Global dial plan data is exchanged successfully on the ILS Network, an ILS
                                             					 receiving cluster will not write learned information into the database until it
                                             					 completes its database replication status. |
| Import | For
                                             					 imported third-party directory URIs and patterns, the CSV file format must
                                             					 match the exact syntax as shown in the administration window sample file
                                             					 otherwise, the import fails. |
| ILS Hub | When adding an additional hub cluster into the ILS network ensure to verify the following conditions are met for the primary
                                             ILS hub node: Cluster ID is unique across all the hub nodes in the ILS cluster. Fully Qualified Domain Name (FQDN) is configured. UDS and EM services are running on the all of the hub nodes in the ILS cluster DNS primary and reverse resolution are working fine. Import consolidated Tomcat certificates from all the hub nodes. Else, the "version" information will not get displayed in the Find and List Remote Clusters window even
                                             					 after rebooting the clusters or correcting the errors. The workaround is to
                                             					 remove the hub cluster from the ILS network, comply with the above requirements
                                             					 and add the hub cluster back into the ILS network. |