---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-3-cluster-creation-maint-exwy-b-cisco-expressway-7b5c28ac9c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-3/cluster_creation_maint/exwy_b_cisco-expressway-cluster-creation-and-maintenance-deployment-guide-x143/exwy_m_how-to-form-a-cluster.html
retrieved_at: 2026-08-16T15:17:43.755468+00:00
---

Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X14.3)

# Cisco Expressway Cluster Creation and Maintenance Deployment Guide (X14.3)

Updated: March 18, 2025

Chapter: How to Form a Cluster

## Chapter: How to Form a Cluster

# How to Form a Cluster

This chapter explains the following:

## Overview

You can have up to six Expressways in a cluster, including the primary.

Add the peers to the cluster one by one.

You should only make configuration changes on the primary Expressway.

Caution

Do not adjust any cluster-wide configuration until the cluster is stable with all peers running. Cluster database replication
                                             will be negatively impacted if any peers are upgrading, restarting, or out of service when you change the cluster's configuration.

Any changes made on other peers are not reflected across the cluster, and will be overwritten the next time the primary’s
                                 configuration is replicated across the peers. The only exceptions to this are some peer-specific configuration items .

You may need to wait up to one minute before changes are updated across all peers in the cluster.

Cluster communication failure alarms are raised while the cluster is forming. Alarms should clear when you are finished.

Configuration replication is suspended to new Expressways before they have properly joined the cluster.

If the new Expressway peer has two network interfaces, the Peer N address must not specify the external interface. If you need to enforce TLS between peers (that is, TLS verify is ON ), you have to use the Peer's FQDN as it appears on the peer's certificate for the Peer N address. You must also use Cluster
                                 Address Mapping because the DNS resolution of the FQDN will likely resolve to the public IP address. See Cluster Address Mapping for Expressway-E Clusters , to map FQDNs to the private IP addresses.

If Expressway server has single NIC and static NAT enabled on the server, Peer N address must not be the static NAT address. If you need to enforce TLS between peers (that is, TLS verify is ON ), you have to use the Peer's FQDN as it appears on the peer's certificate for the Peer N address. You must also use Cluster
                                 Address Mapping because the DNS resolution of the FQDN will likely resolve to the public IP address. See Cluster Address Mapping for Expressway-E Clusters , to map FQDNs to the private IP addresses.

### Preparing Expressway to Join a Cluster

If necessary, take the new peer out of service:

Enable maintenance mode ( Maintenance > Maintenance mode ) and wait for all calls to clear and registrations to timeout on this peer.

If the Expressway is in a cluster, remove it from its existing cluster then restart it.

Factory reset the Expressway (unless you already did this, because of the restart in previous step).

Check that the address of your Expressway is not a peer of any other Expressway in your organization.

Check that the Expressway is not a neighbor, traversal client, or traversal server of any other Expressway.

Review and modify the configuration to ensure that the Expressway has:

A valid Ethernet speed ( System > Network interfaces > Ethernet ).

Valid IP address and IP gateway ( System > Network interfaces > IP ).

A valid and working NTP server configured ( System > Time ; in the Status section, the State should be "Synchronized" ).

At least one valid DNS server configured, and that if unqualified DNS names are used elsewhere (e.g. for the NTP server),
                                          that the correct Domain name is also configured ( Domain name is added as a suffix to an unqualified DNS name to make it into an FQDN) ( System > DNS ).

Go to System > DNS and ensure that System host name is the DNS hostname for this Expressway (typically the same as the System name in System > Administration , but excluding spaces, and unique for each Expressway in the cluster). If it is not configured correctly, set it up appropriately
                                          and click Save .

<System host name>.<DNS domain name> = FQDN of this Expressway

No peers configured (on System > Clustering – all Peer N address fields on this page should be blank).

Caution

If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                      reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                      the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart.

If this Expressway is already a member of a cluster, you should remove it from that cluster and restart it before you use
                                          it in another cluster.

If you have systems that use option keys, ensure that the same set of option keys is installed as those that will be installed
                                          on all other peers of the cluster ( Maintenance > Option keys ). The number of call/RMS/device/room licenses may differ between peers; all other license keys must be identical on each
                                          peer.

H.323 Mode set to On ( Configuration > Protocols > H.323 )

If this Expressway is joining a cluster that is integrated with Cisco TMSPE, Add the Expressway to Cisco TMS , then:

Check that the new Expressway can see Cisco TMS.

To do this, go to System > External manager and in the Status section, ensure that the State is 'Active'.

Check that Cisco TMS knows the Host Name of the Expressway:

Go to Systems > Navigator (and any required sub folders).

Select this Expressway.

Select the Connection tab.

Set Host Name to be the FQDN of this subordinate peer, for example vcs3.uk.company.com.

Click Save / Try .

You can ignore any error messages such as " DNS config failure resolving <DNS name>: Did not find system IP address () in DNS: <Server IP> "

Ensure that Cisco TMS updates its DNS.

Select the Settings tab.

Click Force Refresh

Check that Cisco TMS can communicate with the new Expressway.

To do this, on Cisco TMS go to System > Navigator (and any required sub folders) then click on the name of the Expressway and ensure that it says:

"✓System has no open or acknowledged tickets"

Go to System > Alarms . If there is an alarm that the Expressway must be restarted, go to Maintenance > Restart options and then click Restart .

### Create a New Cluster of Expressway Peers

This process initiates a cluster of a single Expressway. Do not use this process if the cluster already exists.

Important

You must create a cluster of one (primary) peer first, and restart the primary, before you add other peers. You can add more
                                          peers after you have established a "cluster of one" .

Decide which Expressway will be the primary peer. The primary Expressway peer will be the source of the configuration information
                                    for all Expressway peers in the cluster. Subordinate Expressway peers will have most of their configuration deleted and replaced
                                    by that from the primary.

Check that the Expressway is running the latest software.

Backup the Expressway ( Maintenance > Back and restore ).

Review and modify the configuration to ensure that the Expressway has:

A valid Ethernet speed ( System > Network interfaces > Ethernet ).

Valid IP address and IP gateway ( System > Network interfaces > IP ).

A valid and working NTP server configured ( System > Time ; in the Status section, the State should be "Synchronized" ).

At least one valid DNS server configured, and that if unqualified DNS names are used elsewhere (e.g. for the NTP server),
                                          that the correct Domain name is also configured ( Domain name is added as a suffix to an unqualified DNS name to make it into an FQDN) ( System > DNS ).

Go to System > DNS and ensure that System host name is the DNS hostname for this Expressway (typically the same as the System name in System > Administration , but excluding spaces, and unique for each Expressway in the cluster). If it is not configured correctly, set it up appropriately
                                          and click Save .

<System host name>.<DNS domain name> = FQDN of this Expressway

No peers configured (on System > Clustering – all Peer N address fields on this page should be blank).

Caution

If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                      reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                      the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart.

If this Expressway is already a member of a cluster, you should remove it from that cluster and restart it before you use
                                          it in another cluster.

If you have systems that use option keys, ensure that the same set of option keys is installed as those that will be installed
                                          on all other peers of the cluster ( Maintenance > Option keys ). The number of call/RMS/device/room licenses may differ between peers; all other license keys must be identical on each
                                          peer.

H.323 Mode set to On ( Configuration > Protocols > H.323 )

Ensure that this Expressway does not list any of the Expressways that are to be peers in this new cluster in any of its neighbor
                                    zones or traversal zones ( Configuration > Zones > Zones , then check each neighbor and traversal zone).

Set the H.323 Time to live to an appropriate value for the size of your deployment. A smaller number, like 60 (seconds), means that if one Expressway
                                    becomes inaccessible, the endpoint will quickly register with another peer ( Configuration > Protocols > H.323 ).

By reducing the registration time to live too much, you risk flooding the Expressway with registration requests, which will
                                                severely impact performance. This impact is proportional to the number of endpoints, so you should balance the need for occasional
                                                quick failover against the need for continuous good performance.

Go to System > DNS and ensure that System host name is the DNS hostname for this Expressway (typically the same as the System name in System > Administration , but excluding spaces, and unique for each Expressway in the cluster). If it is not configured correctly, set it up appropriately
                                    and click Save .

<System host name>.<DNS domain name> = FQDN of this Expressway

Go to Configuration > Call routing and set Call signaling optimization to On .

Click Save .

Enable maintenance mode ( Maintenance > Maintenance mode ) and wait for all calls to clear and registrations to timeout on this peer.

(Not applicable to MRA deployments) Go to System > Clustering and ensure that Cluster name is the routable Fully Qualified Domain Name used in SRV records that address this Expressway cluster, for example cluster1.example.com (See Cluster Name and DNS SRV Records .

Change the Cluster name if necessary.

Click Save .

On the Clustering page configure the fields as follows:

Configuration Primary

1

Cluster IP version

Choose IPv4 or IPv6 to match the underlying network addressing scheme.

TLS Verification mode

Options: Permissive (default) or Enforce .

Permissive means that the peers do not validate each others' certificates when establishing intracluster TLS connections.

Enforce is more secure, but requires that each peer has a valid certificate and that the signing CA is trusted by all other peers.

We recommend you form a cluster using FQDN and TLS verification as follows: form your cluster using IP addresses in Permissive mode and then change the peer addresses to FQDNs. You can then switch TLS verification mode to Enforce .

If you are clustering Expressway-E peers in an isolated network, you also need to configure cluster address mappings. For
                                                detailed steps, see Cluster Address Mapping for Expressway-E Clusters .

Peer 1 address

Enter the address of this Expressway (the primary peer).

If TLS verification mode is set to Enforce , then you must enter an FQDN that matches the subject CN or a SAN on this peer's certificate.

Click Save .

To the right of the Peer 1 address field the words "This system" should appear (though this may require the page to be refreshed before they appear).

Restart the Expressway (go to Maintenance > Restart options , then click Restart and confirm OK ).

Check that configuration data exists as expected:

If FindMe is in use, check that the expected FindMe entries still exist ( Status > Applications > TMS Provisioning Extension Services > FindMe > Accounts ).

Check configuration for items from the System , Configuration and Application menus.

Check that maintenance mode is disabled.

Go to Maintenance > Maintenance mode .

Set Maintenance mode to Off .

Click Save .

Backup the Expressway ( Maintenance > Backup and restore ).

You've now finished forming a cluster (of one Expressway)

#### Next Steps

Go to Status > Alarms and ensure that all alarms are acted upon and cleared.

Add other Expressways to the cluster using Add a Peer to a Cluster .

### Add a Peer to a Cluster

This procedure adds a new peer to an existing cluster (of one or more peers) and replicates the primary peer’s configuration
                              onto the Expressway.

If you do not have an existing cluster, see Create a New Cluster of Expressway Peers .

Go to System > Clustering on the primary Expressway.

One or more of the Peer N address fields should be empty.

In the first empty field, enter the address of the new Expressway peer.

Click Save .

Peer 1 should indicate 'This system'. The new peer may indicate 'Unknown' and then with a refresh should indicate 'Failed'
                                    because it has not fully joined the cluster yet.

Go to System > Clustering on one of the subordinate peers already in the cluster, and edit the following fields:

Cluster name

Identical to the Cluster name configured on the primary Expressway

Configuration primary

Same number as chosen on the primary Expressway

Cluster IP version

Same version as chosen on the primary Expressway

TLS verification mode

Same setting as chosen on the primary Expressway*

Peer 1 address …Peer 6 address

The addresses should be the same, and in the same order, as those entered on the primary Expressway

*If you intend to use cluster address mapping, all devices in the cluster should be in Permissive mode initially. For more
                                    information, see Cluster Address Mapping for Expressway-E Clusters .

Save the new clustering configuration.

Repeat the previous step for each of the subordinate peers already in the cluster.

Go to System > Clustering on the new peer:

Cluster name

Identical to the Cluster name configured on the primary Expressway

Configuration primary

Same number as chosen on the primary Expressway

Cluster IP version

Same version as chosen on the primary Expressway

TLS verification mode

Same setting as chosen on the primary Expressway*

Peer 1 address …Peer 6 address

The addresses should be the same, and in the same order, as those entered on the primary Expressway

*If you intend to use cluster address mapping, all devices in the cluster should be in Permissive mode initially. For more
                                    information, see Cluster Address Mapping for Expressway-E Clusters .

Save the new clustering configuration.

The Expressway raises a cluster communication failure alarm. The alarm clears after the required restart.

Restart the Expressway (go to Maintenance > Restart options , click Restart and confirm OK ).

#### Checks

After the restart, wait approximately 2 minutes – this is the frequency with which configuration is copied from the primary.

Check the Cluster database status.

Check that configuration data exists as expected:

If FindMe is in use, check that the expected FindMe entries still exist ( Status > Applications > TMS Provisioning Extension Services > FindMe > Accounts ).

Check configuration for items from the System , Configuration , and Application menus.

#### Next Steps

Add more peers if necessary.

If you are using Conference Factory (Multiway™) in your cluster, see Impact of Clustering on Other Expressway Applications .

If you want peers to resolve their FQDNs to their private IP addresses, see Cluster Address Mapping for Expressway-E Clusters .

| Caution | Do not adjust any cluster-wide configuration until the cluster is stable with all peers running. Cluster database replication
                                             will be negatively impacted if any peers are upgrading, restarting, or out of service when you change the cluster's configuration. |
|---|---|

| Note | <System host name>.<DNS domain name> = FQDN of this Expressway |
|---|---|

| Caution | If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                      reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                      the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart. |
|---|---|

| Important | You must create a cluster of one (primary) peer first, and restart the primary, before you add other peers. You can add more
                                          peers after you have established a "cluster of one" . |
|---|---|

| Note | <System host name>.<DNS domain name> = FQDN of this Expressway |
|---|---|

| Caution | If you clear all the peer address fields from the clustering page and save the configuration, then the Expressway will factory
                                                      reset itself the next time you do a restart. This means you will lose all existing configuration except basic networking for
                                                      the LAN1 interface, including all configuration that you do between when you clear the fields and the next restart. |
|---|---|

| Note | By reducing the registration time to live too much, you risk flooding the Expressway with registration requests, which will
                                                severely impact performance. This impact is proportional to the number of endpoints, so you should balance the need for occasional
                                                quick failover against the need for continuous good performance. |
|---|---|

| Note | <System host name>.<DNS domain name> = FQDN of this Expressway |
|---|---|

| Configuration Primary | 1 |
|---|---|
| Cluster IP version | Choose IPv4 or IPv6 to match the underlying network addressing scheme. |
| TLS Verification mode | Options: Permissive (default) or Enforce . Permissive means that the peers do not validate each others' certificates when establishing intracluster TLS connections. Enforce is more secure, but requires that each peer has a valid certificate and that the signing CA is trusted by all other peers. We recommend you form a cluster using FQDN and TLS verification as follows: form your cluster using IP addresses in Permissive mode and then change the peer addresses to FQDNs. You can then switch TLS verification mode to Enforce . If you are clustering Expressway-E peers in an isolated network, you also need to configure cluster address mappings. For
                                                detailed steps, see Cluster Address Mapping for Expressway-E Clusters . |
| Peer 1 address | Enter the address of this Expressway (the primary peer). If TLS verification mode is set to Enforce , then you must enter an FQDN that matches the subject CN or a SAN on this peer's certificate. |

| Cluster name | Identical to the Cluster name configured on the primary Expressway |
|---|---|
| Configuration primary | Same number as chosen on the primary Expressway |
| Cluster IP version | Same version as chosen on the primary Expressway |
| TLS verification mode | Same setting as chosen on the primary Expressway* |
| Peer 1 address …Peer 6 address | The addresses should be the same, and in the same order, as those entered on the primary Expressway |

| Cluster name | Identical to the Cluster name configured on the primary Expressway |
|---|---|
| Configuration primary | Same number as chosen on the primary Expressway |
| Cluster IP version | Same version as chosen on the primary Expressway |
| TLS verification mode | Same setting as chosen on the primary Expressway* |
| Peer 1 address …Peer 6 address | The addresses should be the same, and in the same order, as those entered on the primary Expressway |