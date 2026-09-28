---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-3207842e3d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_011001.html
retrieved_at: 2026-08-16T17:31:06.891756+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Intercluster Lookup Service

## Chapter: Configure Intercluster Lookup Service

# Configure Intercluster Lookup Service

## Intercluster
                        	 Lookup Service Overview

The Intercluster
                           		Lookup Service (ILS) allows you to create networks of remote Cisco
                              		  Unified Communications Manager clusters. When you configure ILS on
                           		multiple clusters, it updates Cisco
                              		  Unified Communications Manager with the current status of remote
                           		clusters in the ILS network.

In Cisco Unified CM
                           		Administration, you can configure ILS on a pair of clusters and then join those
                           		clusters to form an ILS network. ILS allows you to join additional clusters to
                           		the network without having to configure the connections between each cluster.

- Hub clusters

- Spoke clusters

- Global dial plan imported
                                 		  catalogs

### Hub
                           	 Clusters

Hub clusters form the backbone of an ILS network. Hub clusters exchange
                              		ILS updates with the other hub clusters in the ILS network, and then relay that
                              		information to and from their spoke clusters.

When a new hub cluster registers to another hub cluster in an existing
                              		ILS network, ILS automatically creates a full mesh connection between the new
                              		hub cluster and all the existing hub clusters in the ILS network.

### Spoke
                           	 Clusters

A spoke cluster connects to the hub cluster in an ILS network to relay
                              		ILS updates to and from the rest of the ILS network. Spoke clusters contact
                              		only their local hub cluster and never directly contact other hub clusters or
                              		other spoke clusters.

### Global Dial Plan
                           	 Imported Catalogs

To provide URI dialing compatibility with third-party systems, you can
                              		manually import a third-party directory URI or +E.164 number catalog from a CSV
                              		file into any hub cluster in the ILS network. ILS maintains the imported
                              		catalog and replicates that catalog out to the other clusters in the network.
                              		You can dial one of the third-party directory URIs or +E.164 numbers catalog
                              		from any server in the ILS network.

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

## ILS
                        	 Prerequisites

You must study
                              		  your network and design an ILS topology.

For more
                              		  information about the Solution Reference Network Design, see the Cisco Unified
                                 			 Communications Solution Reference Network Design guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html .

## ILS Configuration
                        	 Task Flow

Step 1

Activate Intercluster Lookup Service

Step 2

Configure Cluster IDs

Step 3

Configure Remote Clusters

Step 4

To activate
                                       			 ILS on the various clusters, complete the following tasks:

- Activate ILS on the Hub Cluster

- Activate ILS on the Spoke Cluster

You must
                                                      				  configure each cluster in your ILS network as either a hub cluster or a spoke
                                                      				  cluster.

Step 5

(Optional)
                                       			 Configure authentication between your cluster. Select one of the following
                                       			 procedures:

- Enable TLS Authentication Between Clusters

- Enable Password Authentication Between Clusters

- Enable TLS with Password Authentication Between Clusters

Use TLS
                                          				authentication between clusters in the ILS network.

Use password
                                          				authentication between remote clusters in the ILS network.

Use TLS and
                                          				password authentication to setup a ILS network using common Certificate
                                          				Authority (CA) signed certificates without exchanging self-signed certificates
                                          				between clusters.

Step 6

Enable ILS Support for Global Dial Plan Replication

(Optional)
                                          				Enable ILS support for Global Dial Plan Replication to share dial plan
                                          				information between participating ILS enabled clusters.

Step 7

Import Catalogs in ILS Network

(Optional) To
                                          				provide URI dialing compatibility with third party systems, you can manually
                                          				import a third party directory URI or +E.164 number catalog from a csv file
                                          				into any hub cluster in the ILS network.

### Activate
                           	 Intercluster Lookup Service

You must activate
                                 		  the Intercluster Lookup Service to configure Cluster IDs and Remote Clusters.

Step 1

From Cisco
                                          			 Unified Serviceability, choose Tools > Service
                                                				  Activation .

Step 2

From the Server drop-down list, choose the node on which you
                                          			 want to activate Cisco Intercluster Lookup Service, and then click Go .

Step 3

Check the Cisco
                                             				Intercluster Lookup Service check box.

Step 4

Click Save .

#### What to do next

Configure Cluster IDs

### Configure Cluster
                           	 IDs

You must configure a unique cluster ID for each cluster in the ILS network. You must also ensure that you have a unique peer
                                 ID. The clusters use this unique cluster ID and peer ID when they exchange status messages.

For example, if
                                 		  you have an existing ILS network of four Cisco
                                    			 Unified Communications Manager clusters and you want to add an
                                 		  additional cluster, you can configure ILS on the new cluster and then register
                                 		  that cluster to any hub cluster in the existing ILS network. ILS automatically
                                 		  informs the new cluster of all clusters in the existing network.

Cluster IDs

Peer IDs for the publisher

Cluster descriptions and versions

Fully Qualified Domain Name (FQDN) of the host

IP addresses and host names for the cluster nodes that have ILS activated

Perform the
                                 		  following procedure to configure a unique identifier for each cluster in the
                                 		  network.

#### Before you begin

Activate Intercluster Lookup Service

Step 1

Log in to the Unified
                                             				Communications Manager publisher node.

Step 2

In Cisco
                                             				Unified Communications Manager Administration , choose System > Enterprise
                                                				  Parameters .

Step 3

In the Enterprise Parameters Configuration window Cluster ID field, enter a name of the cluster that
                                          			 you want to configure in your network.

You can enter
                                             				up to 50 characters. You can enter alphanumeric characters, period (.), and
                                             				hyphen (-). The default value is StandAloneCluster.

Step 4

Click Save .

#### What to do next

Configure Remote Clusters

### Configure Remote
                           	 Clusters

Perform the
                                 		  following steps to configure remote clusters in the ILS network.

#### Before you begin

Configure Cluster IDs

Step 1

In Cisco
                                          			 Unified Communications Manager Administration, choose Advanced
                                                				  Features > Cluster View .

Step 2

In the Find and List Remote Clusters window, choose any
                                          			 previously created remote cluster.

Step 3

From the Remote Cluster Service Configuration window,
                                          			 check the appropriate check box to configure services such as Extension
                                          			 Mobility Cross Cluster, TFTP, and RSVP Agent for remote clusters.

#### What to do next

Perform one of the
                                 		  following procedures:

- Activate ILS on the Hub Cluster

- Activate ILS on the Spoke Cluster

### Activate ILS on
                           	 the Hub Cluster

Configure each cluster in your ILS network as either a hub cluster or a spoke cluster. Each ILS network must have at least
                                 one hub cluster. You can connect a hub cluster to other hub clusters, or you can configure a hub cluster as the only hub cluster
                                 in the network. In addition, you can connect a hub cluster to multiple spoke clusters, or you can configure the hub cluster
                                 with no spoke clusters.

Perform the
                                 		  following procedure to activate the ILS on the hub cluster in the ILS network.

#### Before you begin

Configure Remote Clusters

Step 1

Log in to the Cisco
                                             				Unified Communications Manager publisher node.

Step 2

Choose Advanced
                                                				  Features > ILS Configuration .

Step 3

In the ILS Configuration window, in the Role drop-down list, select Hub Cluster and click Save .

To remove a specific cluster in the ILS network, in the ILS Configuration window, in the Role drop-down list, select Standalone and click Save .

Step 4

In the ILS Configuration Registration pop-up window, leave the Registration Server text box empty and click OK .

#### What to do next

Activate ILS on the Spoke Cluster

### Activate ILS on
                           	 the Spoke Cluster

A spoke cluster
                                 		  connects to the hub cluster in an ILS network to relay ILS updates to and from
                                 		  the rest of the ILS network. Follow this procedure to activate ILS on the spoke
                                 		  cluster.

#### Before you begin

- Configure Cluster IDs

- Configure Remote Clusters

Step 1

Log in to the Unified
                                             				Communications Manager publisher node.

Step 2

In Cisco
                                             				Unified CM Administration , choose Advanced
                                                				  Features > ILS Configuration .

Step 3

From the Role drop-down list, select Spoke
                                             				Cluster and click Save .

Step 4

In the ILS
                                             				Configuration Registration popup window, enter the IP address or
                                          			 fully qualified domain name of the publisher node for an existing hub cluster
                                          			 in your ILS network in the Registration Server text box and click OK .

Step 5

Confirm that
                                          			 your ILS network is configured by viewing the network in the ILS Clusters and
                                          			 Global Dial Plan Imported Catalogs section.

When the full
                                             				network appears, your ILS network is configured for cluster discovery.

### Enable TLS
                           	 Authentication Between Clusters

(Optional) Use
                                 		  this procedure for the TLS authentication to encrypt communications between
                                 		  remote clusters in the ILS network:

#### Before you begin

- export certificates from
                                       			 the publisher node to a central location, for each cluster in your network

- consolidate exported
                                       			 certificates from any publisher node server in your ILS network

- import certificates into
                                       			 the publisher node for each cluster in your network

For more
                                             			 information about enabling TLS Authentication Between Clusters, see the Administration Guide for Cisco Unified Communications
                                                				Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 1

Log in to the Unified
                                             				Communications Manager publisher node.

Step 2

In Cisco
                                             				Unified CM Administration , choose Advanced
                                                				  Features > ILS Configuration .

Step 3

In the ILS
                                             				Configuration window, check the Use
                                             				TLS Certificates check box under ILS Authentication.

Step 4

Click Save .

#### What to do next

Perform any of
                                 		  these optional procedures:

Enable Password Authentication Between Clusters

Enable ILS Support for Global Dial Plan Replication

### Enable Password
                           	 Authentication Between Clusters

(Optional) To use
                                 		  password authentication between remote clusters, you must assign a password for
                                 		  all communications between clusters in your ILS network.

Step 1

Log in to the Unified
                                             				Communications Manager publisher node.

Step 2

In Cisco
                                             				Unified CM Administration , choose Advanced
                                                				  Features > ILS Configuration .

Step 3

In the ILS
                                             				Configuration window, check the Use
                                             				Password check box under ILS Authentication.

Step 4

Enter a
                                          			 password in the Use
                                             				Password text box.

Step 5

Re-enter the
                                          			 password in the Confirm Password text box.

Step 6

Click Save .

#### What to do next

Perform any of
                                 		  these optional procedures:

- Enable TLS Authentication Between Clusters

- Enable ILS Support for Global Dial Plan Replication

### Enable TLS with
                           	 Password Authentication Between Clusters

#### Before you begin

To use Transport
                                 		  Layer Security (TLS) and password authentication without exchanging
                                 		  certificates between clusters, you must upload the certificate authority root
                                 		  certificates to the Tomcat trust and get the Tomcat certificate signed by the
                                 		  certificate authority root certificate. The certificate is then imported back
                                 		  on the same cluster. The clusters can be connected to Intercluster Lookup
                                 		  Service (ILS) network once the certificates are uploaded with the same password
                                 		  for all the clusters.

For more
                                             			 information about enabling TLS Authentication Between Clusters, see the Administration Guide for Cisco Unified Communications
                                                				Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 1

Log in to the Cisco
                                             				Unified Communications Manager publisher node.

Step 2

In Cisco
                                             				Unified CM Administration , choose Advanced
                                                				  Features > ILS Configuration .

Step 3

In the ILS
                                             				Configuration window, check the Use
                                             				TLS Certificates check box under ILS Authentication..

Step 4

In the ILS
                                             				Configuration window, check the Use
                                             				Password check box under ILS Authentication.

Step 5

Enter a
                                          			 password in the Use
                                             				Password text box.

Step 6

Re-enter the
                                          			 password in the Confirm Password text box.

Step 7

Click Save .

#### What to do next

(Optional) Enable ILS Support for Global Dial Plan Replication

### Enable ILS Support
                           	 for Global Dial Plan Replication

(Optional) To
                                 		  enable ILS support for Global Dial Plan Replication in the local cluster,
                                 		  follow this procedure:

Step 1

Log in to the Unified
                                             				Communications Manager publisher node.

Step 2

In Cisco
                                             				Unified Communications Manager Administration , choose Advanced
                                                				  Features > ILS Configuration .

Step 3

In the ILS Configuration window, check the Exchange Global Dial Plan Replication Data with Remote
                                             				Clusters check box.

Step 4

In the Advertised Route String text box, enter a route
                                          			 string for the local cluster.

Step 5

Click Save .

When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS.

#### What to do next

Import Catalogs in ILS Network

### Import Catalogs in
                           	 ILS Network

(Optional) To
                                 		  provide URI dialing compatibility with third party systems, you can manually
                                 		  import a third party directory URI or +E.164 number catalog from a csv file
                                 		  into any hub cluster in the ILS network. To Import Catalogs in the ILS network,
                                 		  follow this procedure:

Step 1

In Cisco
                                             				Unified Communications Manager Administration , choose Call
                                                				  Routing > Global Dial Plan Replication > Imported Global Dial Plan Catalogs .

Step 2

In the Find
                                             				and List Imported Global Dial Plan Catalogs window, click Add
                                             				New .

Step 3

Enter a Name,
                                          			 Description and Route String for the catalog and click Save .

Step 4

In Cisco
                                             				Unified Communications Manager Administration , choose Bulk
                                                				  Administration > Upload/Download Files .

Step 5

Click Choose and select the CSV file that you want to import for the
                                          			 catalogs.

Step 6

From the Select
                                             				the Target drop-down list, choose Imported Directory URIs and Patterns .

Step 7

From
                                          			 the Select
                                             				Transaction Type drop-down list, choose Insert Imported Directory URIs and Patterns .

Step 8

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
| Step 1 | Activate Intercluster Lookup Service | Activate
                                       			 Intercluster Lookup Service to configure cluster IDs and remote clusters. |
| Step 2 | Configure Cluster IDs | Provide a
                                       			 unique identifier for each cluster in the ILS network. |
| Step 3 | Configure Remote Clusters | Configure
                                       			 remote clusters in the ILS network. |
| Step 4 | To activate
                                       			 ILS on the various clusters, complete the following tasks: Activate ILS on the Hub Cluster Activate ILS on the Spoke Cluster | Activate ILS
                                       			 on the hub cluster and spoke cluster in the ILS network. Note You must
                                                      				  configure each cluster in your ILS network as either a hub cluster or a spoke
                                                      				  cluster. | Note | You must
                                                      				  configure each cluster in your ILS network as either a hub cluster or a spoke
                                                      				  cluster. |
| Note | You must
                                                      				  configure each cluster in your ILS network as either a hub cluster or a spoke
                                                      				  cluster. |
| Step 5 | (Optional)
                                       			 Configure authentication between your cluster. Select one of the following
                                       			 procedures: Enable TLS Authentication Between Clusters Enable Password Authentication Between Clusters Enable TLS with Password Authentication Between Clusters | Use TLS
                                          				authentication between clusters in the ILS network. Use password
                                          				authentication between remote clusters in the ILS network. Use TLS and
                                          				password authentication to setup a ILS network using common Certificate
                                          				Authority (CA) signed certificates without exchanging self-signed certificates
                                          				between clusters. |
| Step 6 | Enable ILS Support for Global Dial Plan Replication | (Optional)
                                          				Enable ILS support for Global Dial Plan Replication to share dial plan
                                          				information between participating ILS enabled clusters. |
| Step 7 | Import Catalogs in ILS Network | (Optional) To
                                          				provide URI dialing compatibility with third party systems, you can manually
                                          				import a third party directory URI or +E.164 number catalog from a csv file
                                          				into any hub cluster in the ILS network. |

| Note | You must
                                                      				  configure each cluster in your ILS network as either a hub cluster or a spoke
                                                      				  cluster. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified Serviceability, choose Tools > Service
                                                				  Activation . |
|---|---|
| Step 2 | From the Server drop-down list, choose the node on which you
                                          			 want to activate Cisco Intercluster Lookup Service, and then click Go . |
| Step 3 | Check the Cisco
                                             				Intercluster Lookup Service check box. |
| Step 4 | Click Save . |

| Step 1 | Log in to the Unified
                                             				Communications Manager publisher node. |
|---|---|
| Step 2 | In Cisco
                                             				Unified Communications Manager Administration , choose System > Enterprise
                                                				  Parameters . |
| Step 3 | In the Enterprise Parameters Configuration window Cluster ID field, enter a name of the cluster that
                                          			 you want to configure in your network. You can enter
                                             				up to 50 characters. You can enter alphanumeric characters, period (.), and
                                             				hyphen (-). The default value is StandAloneCluster. |
| Step 4 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified Communications Manager Administration, choose Advanced
                                                				  Features > Cluster View . |
|---|---|
| Step 2 | In the Find and List Remote Clusters window, choose any
                                          			 previously created remote cluster. |
| Step 3 | From the Remote Cluster Service Configuration window,
                                          			 check the appropriate check box to configure services such as Extension
                                          			 Mobility Cross Cluster, TFTP, and RSVP Agent for remote clusters. |

| Step 1 | Log in to the Cisco
                                             				Unified Communications Manager publisher node. |
|---|---|
| Step 2 | Choose Advanced
                                                				  Features > ILS Configuration . |
| Step 3 | In the ILS Configuration window, in the Role drop-down list, select Hub Cluster and click Save . Note To remove a specific cluster in the ILS network, in the ILS Configuration window, in the Role drop-down list, select Standalone and click Save . | Note | To remove a specific cluster in the ILS network, in the ILS Configuration window, in the Role drop-down list, select Standalone and click Save . |
| Note | To remove a specific cluster in the ILS network, in the ILS Configuration window, in the Role drop-down list, select Standalone and click Save . |
| Step 4 | In the ILS Configuration Registration pop-up window, leave the Registration Server text box empty and click OK . |

| Note | To remove a specific cluster in the ILS network, in the ILS Configuration window, in the Role drop-down list, select Standalone and click Save . |
|---|---|

| Step 1 | Log in to the Unified
                                             				Communications Manager publisher node. |
|---|---|
| Step 2 | In Cisco
                                             				Unified CM Administration , choose Advanced
                                                				  Features > ILS Configuration . |
| Step 3 | From the Role drop-down list, select Spoke
                                             				Cluster and click Save . |
| Step 4 | In the ILS
                                             				Configuration Registration popup window, enter the IP address or
                                          			 fully qualified domain name of the publisher node for an existing hub cluster
                                          			 in your ILS network in the Registration Server text box and click OK . |
| Step 5 | Confirm that
                                          			 your ILS network is configured by viewing the network in the ILS Clusters and
                                          			 Global Dial Plan Imported Catalogs section. When the full
                                             				network appears, your ILS network is configured for cluster discovery. |

| Note | For more
                                             			 information about enabling TLS Authentication Between Clusters, see the Administration Guide for Cisco Unified Communications
                                                				Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | Log in to the Unified
                                             				Communications Manager publisher node. |
|---|---|
| Step 2 | In Cisco
                                             				Unified CM Administration , choose Advanced
                                                				  Features > ILS Configuration . |
| Step 3 | In the ILS
                                             				Configuration window, check the Use
                                             				TLS Certificates check box under ILS Authentication. |
| Step 4 | Click Save . |

| Step 1 | Log in to the Unified
                                             				Communications Manager publisher node. |
|---|---|
| Step 2 | In Cisco
                                             				Unified CM Administration , choose Advanced
                                                				  Features > ILS Configuration . |
| Step 3 | In the ILS
                                             				Configuration window, check the Use
                                             				Password check box under ILS Authentication. |
| Step 4 | Enter a
                                          			 password in the Use
                                             				Password text box. Note You must
                                                      				configure all clusters in your network with the same password. | Note | You must
                                                      				configure all clusters in your network with the same password. |
| Note | You must
                                                      				configure all clusters in your network with the same password. |
| Step 5 | Re-enter the
                                          			 password in the Confirm Password text box. |
| Step 6 | Click Save . |

| Note | You must
                                                      				configure all clusters in your network with the same password. |
|---|---|

| Note | For more
                                             			 information about enabling TLS Authentication Between Clusters, see the Administration Guide for Cisco Unified Communications
                                                				Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | Log in to the Cisco
                                             				Unified Communications Manager publisher node. |
|---|---|
| Step 2 | In Cisco
                                             				Unified CM Administration , choose Advanced
                                                				  Features > ILS Configuration . |
| Step 3 | In the ILS
                                             				Configuration window, check the Use
                                             				TLS Certificates check box under ILS Authentication.. |
| Step 4 | In the ILS
                                             				Configuration window, check the Use
                                             				Password check box under ILS Authentication. |
| Step 5 | Enter a
                                          			 password in the Use
                                             				Password text box. Note You must
                                                      				configure all clusters in your network with the same password. | Note | You must
                                                      				configure all clusters in your network with the same password. |
| Note | You must
                                                      				configure all clusters in your network with the same password. |
| Step 6 | Re-enter the
                                          			 password in the Confirm Password text box. |
| Step 7 | Click Save . |

| Note | You must
                                                      				configure all clusters in your network with the same password. |
|---|---|

| Step 1 | Log in to the Unified
                                             				Communications Manager publisher node. |
|---|---|
| Step 2 | In Cisco
                                             				Unified Communications Manager Administration , choose Advanced
                                                				  Features > ILS Configuration . |
| Step 3 | In the ILS Configuration window, check the Exchange Global Dial Plan Replication Data with Remote
                                             				Clusters check box. |
| Step 4 | In the Advertised Route String text box, enter a route
                                          			 string for the local cluster. |
| Step 5 | Click Save . Note When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS. | Note | When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS. |
| Note | When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS. |

| Note | When advertising URI patterns ( user@domain ), in the SIP Profile Configuration window, make sure that the Dial String Interpretation field is set to Always treat all dial strings as URI addresses to prevent the devices to dial URI learned patterns with only numbers in the user section as Directory Number patterns. Alternatively,
                                                         you can advertise only URI patterns with text strings in the user section through ILS. |
|---|---|

| Step 1 | In Cisco
                                             				Unified Communications Manager Administration , choose Call
                                                				  Routing > Global Dial Plan Replication > Imported Global Dial Plan Catalogs . |
|---|---|
| Step 2 | In the Find
                                             				and List Imported Global Dial Plan Catalogs window, click Add
                                             				New . |
| Step 3 | Enter a Name,
                                          			 Description and Route String for the catalog and click Save . |
| Step 4 | In Cisco
                                             				Unified Communications Manager Administration , choose Bulk
                                                				  Administration > Upload/Download Files . |
| Step 5 | Click Choose and select the CSV file that you want to import for the
                                          			 catalogs. |
| Step 6 | From the Select
                                             				the Target drop-down list, choose Imported Directory URIs and Patterns . |
| Step 7 | From
                                          			 the Select
                                             				Transaction Type drop-down list, choose Insert Imported Directory URIs and Patterns . |
| Step 8 | Click Save . |

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