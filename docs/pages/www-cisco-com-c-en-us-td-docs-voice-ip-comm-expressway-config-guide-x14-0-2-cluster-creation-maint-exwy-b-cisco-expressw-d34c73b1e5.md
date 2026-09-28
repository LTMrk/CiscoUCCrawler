---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-2-cluster-creation-maint-exwy-b-cisco-expressw-d34c73b1e5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0-2/cluster_creation_maint/exwy_b_cisco-expressway-cluster-creation-and-maintenance-deployment-guide-x1402/exwy_b_cluster-creation-maintenance-deployment-guide_chapter_0111.html
retrieved_at: 2026-08-16T15:22:20.198475+00:00
---

Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X14.0.2)

# Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X14.0.2)

Updated: July 23, 2021

Chapter: How to Change a Cluster

## Chapter: How to Change a Cluster

# How to Change a Cluster

## How to Change a Cluster

When your cluster is connected to other systems, any changes to the cluster could impact the integrated systems. When you
                           change a cluster, remember to:

Check other Expressways that are neighbors, clients, or servers of this cluster and update their zone configurations. For
                                 example, you need to update the peer address lists on neighbor zones towards this cluster when you add or remove peers from
                                 it.

Check connections to other systems that integrate with the cluster. For example, Cisco Unified Communications Manager may
                                 have trunks to the cluster, or there may be auto-generated MRA zones that need to be refreshed on new cluster peers

Check that endpoints which register to the Expressway cluster are aware of new or removed peers, so that they register equally
                                 to the changed cluster's peers.

Change the DNS entries for this cluster if you add or remove peers, or change IP addresses or FQDNs.

If you use Expressway physical appliances:

To add a CE1200 appliance to an existing cluster that has CE1100 models in it, configure the Type option to match the other
                                       peers (Expressway-E or Expressway-C) through the service setup wizard on the Status > Overview page, before you add the CE1200 to the cluster.

If you are adding a more recent model than existing appliances in the cluster, upgrade the Expressway software on the existing
                                       peers to the same version as the new appliance, before you create the backup to be later restored onto the new appliance.
                                       (A backup can only be restored onto the same software version that it was created on.) Not all appliance types support all software versions - please check first in the appliance installation guides that the units you want to mix can all support the same software
                                       version.

Re-export SAML metadata and copy it to the IDP. Whenever you add, remove, or replace a peer in a cluster of Expressway-Cs,
                                       you will change the SAML metadata of the cluster. If the cluster is configured for SSO of MRA-connected clients, then SSO
                                       will fail some of the time until you update the IDP with the cluster's new SAML metadata. This is because the (unique) serial
                                       numbers of the peers are used to generate the cluster's metadata. For details, see the Mobile and Remote Access Through Cisco Expressway Deployment Guide on the Expressway configuration guides page.

With the cluster wide SAML metadata, it is not sufficient to export metadata, you need to regenerate SAML certificate which
                                                   contains FQDN information for all expressway cluster peers.

For instructions about upgrading a cluster to a new software version, please refer to the release notes for the relevant version.

### Before You Change a Cluster

Systems that are configured as peers must not also be configured as neighbors to each other, and vice versa.

If peers are deployed on different LANs, there must be sufficient connectivity between the networks to ensure a low degree
                                    of latency between the peers.

Cluster peers can be in separate subnets. Peers communicate with each other using H.323 messaging, which can be transmitted
                                    across subnet boundaries.

Deploying all peers in a cluster on the same LAN means they can be configured with the same routing information such as local
                                    domain names and local domain subnet masks.

To remove a peer from the cluster you must clear all peer address fields on that peer, save, then restart.

If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                          reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                          the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart.

The Expressway displays a banner to remind you that it is pending a factory reset.

If you need to prevent the factory reset, restore the clustering peer address fields exactly as they were. Replace the original
                              peer addresses in the same order, and then save the configuration to clear the banner and prevent the reset.

### Remove a Live Peer From a Cluster (Permanently)

This process removes one Expressway peer from an existing cluster.

If you are disbanding the whole cluster, see Disband a Cluster instead.

If you want to remove the primary peer, make a different peer the primary before you remove this one. See Change the Primary Peer

If you cannot access the peer you want to remove, see Remove a Dead Peer From a Cluster (Permanently) .

If you want to recover an expressway cluster peer, see Recovery of an Expressway Cluster Peer .

#### On the Expressway that you are removing from the cluster

Go to System > Clustering .

Delete all entries in the Peer N address fields.

Save .

If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                            reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                            the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart.

If you need to avoid the factory reset, restore the clustering peer address fields as they were. Replace the original peer
                                                addresses in the same order, and then save the configuration to clear the banner.

Restart the Expressway (go to Maintenance > Restart options , then click Restart and confirm OK ).

The factory reset is automatically triggered when the peer restarts, to remove sensitive data and clustering configuration.
                                                The reset clears all configuration except the basic networking information listed below, which is preserved for the LAN1 interface
                                                so that you can still access the Expressway. If you use the dual-NIC option, be aware that any LAN2 configuration is removed
                                                completely by the reset.

Configuration that is preserved (for LAN1) after the reset:

IP addresses

Admin and root accounts and passwords

SSH keys

Option keys

HTTPS access enabled

SSH access enabled

From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                            the peer. In earlier Expressway software versions these settings were preserved.

#### On the primary Expressway

Go to System > Clustering .

Delete the address of the Expressway that has been removed.

If the Expressway being removed is not the last field in the list, move any other addresses up the list so that there are
                                             no empty fields between entries.

If the primary Expressway peer’s address has been moved up the list in the previous step, alter the Configuration primary value to match its new location.

Click Save .

#### On all the remaining subordinate Expressway peers

Go to System > Clustering .

Edit the Peer N address and Configuration primary fields so that they are identical to those configured on the primary Expressway

Click Save .

Repeat for all remaining subordinate Expressway peers until they all have identical clustering configuration.

You have finished removing the live Expressway from the cluster.

### Remove a Dead Peer From a Cluster (Permanently)

This procedure removes an out-of-service peer from a cluster if it needs to be RMAd, or cannot be accessed for some other
                              reason.

If you are disbanding the whole cluster, see Disband a Cluster .

If you can access the peer you want to remove, see Remove a Live Peer From a Cluster (Permanently)

If you want to remove the primary peer, make a different peer the primary before you remove this one. See Change the Primary Peer .

If you want to recover an expressway cluster peer, see Recovery of an Expressway Cluster Peer .

This procedure does not clear configuration from the Expressway. If you manage to revive the system, you must not start using
                                          it until you have reset its default configuration (factory reset).

#### On the primary Expressway:

Go to System > Clustering .

Delete the address of the Expressway that has been removed.

If the Expressway being removed is not the last field in the list, move any other addresses up the list so that there are
                                       no empty fields between entries.

If the primary Expressway peer’s address has been moved up the list in the previous step, alter the Configuration primary value to match its new location.

Click Save .

#### On all the remaining subordinate Expressway peers:

Go to System > Clustering .

Edit the Peer N address and Configuration primary fields so that they are identical to those configured on the primary Expressway.

Click Save .

Repeat for all remaining subordinate Expressway peers until they all have identical clustering configuration.

You have removed the inaccessible peer from the Expressway cluster.

#### Clear Configuration From This Peer

Go to System > Clustering .

Delete all entries in the Peer N address fields.

Click Save .

Restart the Expressway (go to Maintenance > Restart options , then click Restart and confirm OK ). The Expressway initiates a factory reset when you do the restart. It comes back up with all configuration removed, except:

The factory reset is automatically triggered when the peer restarts, to remove sensitive data and clustering configuration.
                                                The reset clears all configuration except the basic networking information listed below, which is preserved for the LAN1 interface
                                                so that you can still access the Expressway. If you use the dual-NIC option, be aware that any LAN2 configuration is removed completely by the reset .

Configuration that is preserved (for LAN1) after the reset:

IP addresses

Admin and root accounts and passwords

SSH keys

Option keys

HTTPS access enabled

SSH access enabled

Now you can bring it back into the cluster, see Add a Peer to a Cluster

### Recovery of an Expressway Cluster Peer

Expressways are in a cluster. You cannot re-insert a peer involuntarily taken out of a cluster to its original position. In
                              such situations,

Remove the peer from the cluster before re-inserting

Make it the last peer in the cluster list

Any back-up of such a peer becomes useless since it bears a different Fully Qualified Domain Name (FQDN) in the cluster list
                                    after re-insertion.

### Disband a Cluster

Each Expressway will retain enough configuration to enable you to access the web interface, but all other configuration is
                                 cleared.

The procedure involves removing peers one by one, and finally clearing the clustering configuration from the primary peer.
                                 In X8.11 and later, clearing the clustering configuration prepares the Expressway for a factory reset. You must be certain
                                 you want to factory reset the primary, because there are some situations where you need to have Expressway configured as a
                                 'cluster of one'.

To disband the cluster:

Remove any peers that you cannot access. See Remove a Dead Peer From a Cluster (Permanently) .

If you're using Cisco TMSPE, sign in to Cisco TMS and stop provisioning to the cluster:

Select Systems > Navigator (and any required sub folders), then click on any Expressway in the cluster.

Select the Provisioning tab.

Disable all 4 services (clear checkboxes).

Click Save .

Remove each of the subordinate peers turn. See Remove a Live Peer From a Cluster (Permanently) .

When you remove the last subordinate peer, you should only have the primary peer remaining in the cluster.

The cluster is now a 'cluster of one' and you can stop here if you want to retain this Expressway with its configuration.

If you want to factory reset the primary peer, sign in to it and follow the process to Remove a Live Peer From a Cluster (Permanently) .

You've finished disbanding the cluster.

### Change the Primary Peer

Typically you only need to change the Configuration primary to take the primary Expressway unit out of service or if the original primary peer fails.

On the "new" primary Expressway, go to System > Clustering .

From the Configuration primary drop-down menu select the ID number of the peer entry that says ‘This system’.

Click Save .

While changing the primary peer, ignore any alarms on Expressway that report 'Cluster primary mismatch' or 'Cluster replication
                                             error' – they will be rectified as part of this procedure.

On all other Expressway peers, starting with the "old" primary peer (if it is still accessible), go to System > Clustering .

From the Configuration primary drop-down menu select the ID number of the "new" primary Expressway.

Click Save .

Any alarms raised on the Expressway peers that relate to 'Cluster primary mismatch' and 'Cluster replication error' should
                                             clear automatically after approximately 2 minutes

Confirm that the change to the Configuration primary has been accepted by going to System > Clustering and refreshing the page.

If any Expressways have not accepted the change, repeat the steps above.

Check that the cluster database status reports as Active.

If you are changing the primary peer because the "old" primary is not accessible, see Remove a Dead Peer From a Cluster (Permanently) procedure.

If there is any chance of reviving the "old" primary, you must isolate it from the other peers and factory reset it if possible.

No further steps are required if you are using FQDNs, with valid cluster address mapping configured.

### Change the Address of a Peer

The process is as follows:

Ensure that the Expressway whose address you want to change is not the primary Expressway.

If it is the primary Expressway, follow the steps in Change the Primary Peer to make a different peer the primary.

Carry out the process documented in Remove a Live Peer From a Cluster (Permanently)

Change the address of the Expressway.

Carry out the process documented in Add a Peer to a Cluster .

### Replace a Peer

Ensure that the Expressway to be replaced is not the primary Expressway.

If it is the primary Expressway, follow the steps in Change the Primary Peer to make a different peer the primary.

Remove the existing peer from the cluster:

If the cluster peer to be replaced is not accessible, use the procedure defined in Remove a Dead Peer From a Cluster (Permanently) .

If the cluster peer to be replaced is accessible, use the procedure defined in Remove a Live Peer From a Cluster (Permanently) .

Add the replacement peer to the cluster using the procedure defined in Add a Peer to a Cluster .

additional information if you have clusters with physical appliances

To add a CE1200 appliance to an existing cluster that has CE1100 models in it, configure the Type option to match the other
                                             peers (Expressway-E or Expressway-C) through the service setup wizard on the Status > Overview page, before you add the CE1200 to the cluster.

If you are adding a more recent model than existing appliances in the cluster, upgrade the Expressway software on the existing
                                             peers to the same version as the new appliance, before you create the backup to be later restored onto the new appliance.
                                             (A backup can only be restored onto the same software version that it was created on.) Not all appliance types support all
                                             software versions - please check first in the appliance installation guides that the units you want to mix can all support
                                             the same software version.

#### Replace a Peer and Migrate its Configuration

Ensure that the Expressway to be replaced is not the primary Expressway.

If it is the primary Expressway, follow the steps in Change the Primary Peer to make a different peer the primary.

Remove the peer by deleting its clustering configuration, but do not restart it yet . See Remove a Live Peer From a Cluster (Permanently) .

Backup the configuration of the removed peer before you restart it.

If required, generate and apply any option keys needed for the new Expressway. Apply the same set of keys that are applied
                                             to the other peers.

Restore the backup from the removed peer onto the new Expressway.

Check the DNS configuration of the new Expressway is the same as the other peers, and synchronize it with the same NTP servers.

Add the replacement peer to the cluster using the procedure defined in Add a Peer to a Cluster .

You should use the new peer's address in place of the removed peer's address when following that procedure.

The most important steps are summarized here:

Add the new peer's address to the clustering configuration on the primary, in place of the old peer's address.

Add the new peer's address to the clustering configuration on other existing peers, in place of the old peer's address.

Enter the new clustering configuration on the new peer (cluster name, shared secret, ordered peer list).

Restart the new peer.

Wait for approximately five minutes, then check the cluster status and resolve any alarms.

Restart the removed peer to initiate a factory reset and clear the old configuration.

| Note | With the cluster wide SAML metadata, it is not sufficient to export metadata, you need to regenerate SAML certificate which
                                                   contains FQDN information for all expressway cluster peers. |
|---|---|

| Note | For instructions about upgrading a cluster to a new software version, please refer to the release notes for the relevant version. |
|---|---|

| Caution | If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                          reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                          the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart. |
|---|---|

| Step 1 | Go to System > Clustering . |
|---|---|
| Step 2 | Delete all entries in the Peer N address fields. |
| Step 3 | Save . Caution If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                            reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                            the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart. If you need to avoid the factory reset, restore the clustering peer address fields as they were. Replace the original peer
                                                addresses in the same order, and then save the configuration to clear the banner. | Caution | If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                            reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                            the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart. |
| Caution | If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                            reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                            the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart. |
| Step 4 | Restart the Expressway (go to Maintenance > Restart options , then click Restart and confirm OK ). The factory reset is automatically triggered when the peer restarts, to remove sensitive data and clustering configuration.
                                                The reset clears all configuration except the basic networking information listed below, which is preserved for the LAN1 interface
                                                so that you can still access the Expressway. If you use the dual-NIC option, be aware that any LAN2 configuration is removed
                                                completely by the reset. Configuration that is preserved (for LAN1) after the reset: IP addresses Admin and root accounts and passwords SSH keys Option keys HTTPS access enabled SSH access enabled Note From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                            the peer. In earlier Expressway software versions these settings were preserved. | Note | From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                            the peer. In earlier Expressway software versions these settings were preserved. |
| Note | From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                            the peer. In earlier Expressway software versions these settings were preserved. |

| Caution | If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                            reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                            the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart. |
|---|---|

| Note | From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                            the peer. In earlier Expressway software versions these settings were preserved. |
|---|---|

| Step 1 | Go to System > Clustering . |
|---|---|
| Step 2 | Delete the address of the Expressway that has been removed. |
| Step 3 | If the Expressway being removed is not the last field in the list, move any other addresses up the list so that there are
                                             no empty fields between entries. |
| Step 4 | If the primary Expressway peer’s address has been moved up the list in the previous step, alter the Configuration primary value to match its new location. |
| Step 5 | Click Save . |

| Step 1 | Go to System > Clustering . |
|---|---|
| Step 2 | Edit the Peer N address and Configuration primary fields so that they are identical to those configured on the primary Expressway |
| Step 3 | Click Save . |
| Step 4 | Repeat for all remaining subordinate Expressway peers until they all have identical clustering configuration. You have finished removing the live Expressway from the cluster. |

| Note | This procedure does not clear configuration from the Expressway. If you manage to revive the system, you must not start using
                                          it until you have reset its default configuration (factory reset). |
|---|---|

| Step 1 | Go to System > Clustering . |
|---|---|
| Step 2 | Delete all entries in the Peer N address fields. |
| Step 3 | Click Save . |
| Step 4 | Restart the Expressway (go to Maintenance > Restart options , then click Restart and confirm OK ). The Expressway initiates a factory reset when you do the restart. It comes back up with all configuration removed, except: The factory reset is automatically triggered when the peer restarts, to remove sensitive data and clustering configuration.
                                                The reset clears all configuration except the basic networking information listed below, which is preserved for the LAN1 interface
                                                so that you can still access the Expressway. If you use the dual-NIC option, be aware that any LAN2 configuration is removed completely by the reset . Configuration that is preserved (for LAN1) after the reset: IP addresses Admin and root accounts and passwords SSH keys Option keys HTTPS access enabled SSH access enabled Note From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                         the peer. In earlier Expressway software versions these settings were preserved. Now you can bring it back into the cluster, see Add a Peer to a Cluster | Note | From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                         the peer. In earlier Expressway software versions these settings were preserved. |
| Note | From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                         the peer. In earlier Expressway software versions these settings were preserved. |

| Note | From version X12-6 the factory reset removes the server certificate, associated private key, and CA trust store settings from
                                                         the peer. In earlier Expressway software versions these settings were preserved. |
|---|---|

| Step 1 | Remove any peers that you cannot access. See Remove a Dead Peer From a Cluster (Permanently) . |
|---|---|
| Step 2 | If you're using Cisco TMSPE, sign in to Cisco TMS and stop provisioning to the cluster: Select Systems > Navigator (and any required sub folders), then click on any Expressway in the cluster. Select the Provisioning tab. Disable all 4 services (clear checkboxes). Click Save . |
| Step 3 | Remove each of the subordinate peers turn. See Remove a Live Peer From a Cluster (Permanently) . When you remove the last subordinate peer, you should only have the primary peer remaining in the cluster. The cluster is now a 'cluster of one' and you can stop here if you want to retain this Expressway with its configuration. |
| Step 4 | If you want to factory reset the primary peer, sign in to it and follow the process to Remove a Live Peer From a Cluster (Permanently) . You've finished disbanding the cluster. |

| Note | No changes are required for Cisco TMS, which will see the primary change on the Expressway cluster and report this appropriately. |
|---|---|

| Step 1 | On the "new" primary Expressway, go to System > Clustering . |
|---|---|
| Step 2 | From the Configuration primary drop-down menu select the ID number of the peer entry that says ‘This system’. |
| Step 3 | Click Save . While changing the primary peer, ignore any alarms on Expressway that report 'Cluster primary mismatch' or 'Cluster replication
                                             error' – they will be rectified as part of this procedure. |
| Step 4 | On all other Expressway peers, starting with the "old" primary peer (if it is still accessible), go to System > Clustering . |
| Step 5 | From the Configuration primary drop-down menu select the ID number of the "new" primary Expressway. |
| Step 6 | Click Save . Any alarms raised on the Expressway peers that relate to 'Cluster primary mismatch' and 'Cluster replication error' should
                                             clear automatically after approximately 2 minutes |
| Step 7 | Confirm that the change to the Configuration primary has been accepted by going to System > Clustering and refreshing the page. |
| Step 8 | If any Expressways have not accepted the change, repeat the steps above. |
| Step 9 | Check that the cluster database status reports as Active. |
| Step 10 | If you are changing the primary peer because the "old" primary is not accessible, see Remove a Dead Peer From a Cluster (Permanently) procedure. |
| Step 11 | If there is any chance of reviving the "old" primary, you must isolate it from the other peers and factory reset it if possible. No further steps are required if you are using FQDNs, with valid cluster address mapping configured. |

| Step 1 | Ensure that the Expressway whose address you want to change is not the primary Expressway. If it is the primary Expressway, follow the steps in Change the Primary Peer to make a different peer the primary. |
|---|---|
| Step 2 | Carry out the process documented in Remove a Live Peer From a Cluster (Permanently) |
| Step 3 | Change the address of the Expressway. |
| Step 4 | Carry out the process documented in Add a Peer to a Cluster . |

| Step 1 | Ensure that the Expressway to be replaced is not the primary Expressway. If it is the primary Expressway, follow the steps in Change the Primary Peer to make a different peer the primary. |
|---|---|
| Step 2 | Remove the existing peer from the cluster: If the cluster peer to be replaced is not accessible, use the procedure defined in Remove a Dead Peer From a Cluster (Permanently) . If the cluster peer to be replaced is accessible, use the procedure defined in Remove a Live Peer From a Cluster (Permanently) . |
| Step 3 | Add the replacement peer to the cluster using the procedure defined in Add a Peer to a Cluster . Important additional information if you have clusters with physical appliances To add a CE1200 appliance to an existing cluster that has CE1100 models in it, configure the Type option to match the other
                                             peers (Expressway-E or Expressway-C) through the service setup wizard on the Status > Overview page, before you add the CE1200 to the cluster. If you are adding a more recent model than existing appliances in the cluster, upgrade the Expressway software on the existing
                                             peers to the same version as the new appliance, before you create the backup to be later restored onto the new appliance.
                                             (A backup can only be restored onto the same software version that it was created on.) Not all appliance types support all
                                             software versions - please check first in the appliance installation guides that the units you want to mix can all support
                                             the same software version. | Important | additional information if you have clusters with physical appliances |
| Important | additional information if you have clusters with physical appliances |

| Important | additional information if you have clusters with physical appliances |
|---|---|

| Step 1 | Ensure that the Expressway to be replaced is not the primary Expressway. If it is the primary Expressway, follow the steps in Change the Primary Peer to make a different peer the primary. |
|---|---|
| Step 2 | Remove the peer by deleting its clustering configuration, but do not restart it yet . See Remove a Live Peer From a Cluster (Permanently) . |
| Step 3 | Backup the configuration of the removed peer before you restart it. |
| Step 4 | If required, generate and apply any option keys needed for the new Expressway. Apply the same set of keys that are applied
                                             to the other peers. |
| Step 5 | Restore the backup from the removed peer onto the new Expressway. |
| Step 6 | Check the DNS configuration of the new Expressway is the same as the other peers, and synchronize it with the same NTP servers. |
| Step 7 | Add the replacement peer to the cluster using the procedure defined in Add a Peer to a Cluster . You should use the new peer's address in place of the removed peer's address when following that procedure. The most important steps are summarized here: Add the new peer's address to the clustering configuration on the primary, in place of the old peer's address. Add the new peer's address to the clustering configuration on other existing peers, in place of the old peer's address. Enter the new clustering configuration on the new peer (cluster name, shared secret, ordered peer list). |
| Step 8 | Restart the new peer. |
| Step 9 | Wait for approximately five minutes, then check the cluster status and resolve any alarms. |
| Step 10 | Restart the removed peer to initiate a factory reset and clear the old configuration. |