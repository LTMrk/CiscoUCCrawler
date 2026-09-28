---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-217230-what-is-expressway-cluster-and-how-it-wo-htm-93654959f7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217230-what-is-expressway-cluster-and-how-it-wo.html
retrieved_at: 2026-08-16T15:44:18.107020+00:00
---

What is Expressway Cluster and how it Works

# What is Expressway Cluster and how it Works

### Download Options

Updated: July 2, 2021

Document ID: 217230

Contents

## Contents

## Introduction

This document describes how the Expressway clusters are designed to extend the resilience and capacity of an Expressway installation.

## Background Information

Capacity . Expressway cluster can increase the capacity of an Expressway deployment by a maximum factor of four, compared with a single Expressway. Expressway peers in a cluster share bandwidth usage as well as routing, zone, FindMe and other configuration.

Resilience . Expressway cluster can provide redundancy while an Expressway is in maintenance mode, or in case it becomes inaccessible due to a network or power outage, or other reason. Endpoints can register to any of the peers in a cluster. If endpoints lose connection to their initial peer, they can re-register to another one in the cluster.

### Specifications

An Expressway can be part of a cluster of up to six Expressways. When you create a cluster you nominate one peer as the primary, from which its configuration is replicated to the other peers. Every Expressway peer in the cluster must have the same routing capabilities, if any Expressway can route a call to a destination it is assumed that all Expressway peers in that cluster can route a call to that destination.

### Capacity

There is no capacity gain after four peers. So in a six-peer cluster for example, the fifth and sixth Expressways do not add extra call capacity to the cluster. Resilience is improved with the extra peers, but not capacity.

- For Small Virtual Machines (VMs), the cluster is only for redundancy and not for scale and there is no capacity gain from cluster.

- Capacity based in 4 peers cluster configuration is shown in the next image:

### Important Page Elements

## Requirements

- Basic knowledge of Secure Shell (SSH)

- A cluster must contain only Expressway-C node or only Expressway-E nodes.

- All peers must use the same software version.

- All peers use hardware platform, Appliance or Virtual Machine (VM), with equivalent capabilities.

- Expressway supports a round trip delay of up to 80ms.

- H323 mode is enabled on each peer.

- All peers have the same set of option keys installed, with the next exceptions:

- For Video Control Server (VCS): Traversal and non-traversal call licenses

- For Expressway: Rich Media Sessions

- For Expressway: Room system and desktop system registration licenses

All other license keys must be identical on each peer.

- There must be no Network Address Translation (NAT) between cluster peers.

Note : If Expressway-E uses single Network Interface Controller (NIC), then it has to use public IP. If Expressway-E uses dual NIC, then internal interface has to be used to build the cluster.

- IP address, Domain Name Servivce (DNS) and Network Time Protocol (NTP) must be configured.

### Cluster Connections and Ports

## Configurations

### Create a New Cluster

- Open the Expressway web interface.

- Navigate to System > Clustering .

- Enter the next values:

Note : You must create a cluster of one (primary) peer first, and restart the primary, before you add other peers. You can add more peers after you have established a cluster of one .

Configuration primary: 1

Cluster IP version: Choose IPv4 or IPv6 to match with the network address scheme.

TLS verification mode Options: Permissive (default) or Enforce.

Permissive means that the peers do not validate each others' certificates when the intra-cluster Transport Layer Securoty (TLS) connections are stablished.

Enforce is more secure, but requires that each peer has a valid certificate and that the Certificate Authority (CA) is trusted by all other peers.

Peer 1 address: Enter the address of this Expressway (the primary peer). If TLS verification mode is set to Enforce, then you must enter a Fully Qualified Domain Name (FQDN) that matches the subject Common Name (CN) or a Subject Alternative Name (SAN) on this peer's certificate.

- Select Save .

- Restart the server.

- Navigate to Maintenance > Restart options , then select Restart and confirm OK .

- Validate the certificate is valid, as shown in the next image:

### Add Additional Peers to the cluster

In order to add an additional peer, follow the next steps:

- Navigate to System > Clustering on the primary Expressway.

- In the first empty field, enter the address of the new Expressway peer.

- Select Save .

- Peer 1 must indicate This system . The new peer must indicate Unknown and then with a refresh must indicate Failed because it has not fully joined the cluster yet.

- Navigate to System > Clustering on one of the subordinate peers already in the cluster, and edit the next fields:

- Repeat the previous step for each of the subordinate peers already in the cluster.

- Select Save .

- The Expressway raises a cluster communication failure alarm. The alarm clears after the required restart.

- Restart the Expressway.

- After the restart, wait approximately 2 minutes – this is the frequency with which configuration is copied from the primary.

- Validate the Cluster database status.

- Make sure, configuration is replicated on a suboridinate peer.

### Enforce TLS Verification

Caution : Before you proceed, verify that your certificate SANs contain the FQDNs that are in the Peer N address fields. You must see green status messages for clustering and certificate next to each address field before you proceed.

- On the primary peer, set TLS verification mode to Enforce .

Caution : A warning displays if any certificates are invalid and prevents the cluster to work properly in enforced TLS verification mode.

- The new TLS verification mode replicates throughout the cluster.

- Verify that TLS verification mode is now Enforce on each other peer.

- Select Save and restart the primary peer.

- After primary peer is back on line, restart each peer one by one.

- Wait for the cluster to stabilize, and validate that Clustering and Certificate status is green for all peers.

### Change the Primary Peer

Note : You can do this process even if the current primary peer is not accessible.

- On the new primary Expressway, navigate to System > Clustering .

- From the Configuration primary drop-down menu select the ID number of the peer entry that says This system .

- Select Save .

Note : While this process is performed, ignore any alarms on Expressway that report Cluster primary mismatch or Cluster replication error .

- On all other Expressway peers, start with the old primary peer (if it is still accessible).

- Navigate to System > Clustering .

- From the Configuration primary drop-down menu select the ID number of the new primary Expressway.

- Select Save .

- Confirm that the change to the Configuration primary has been accepted, navigate to System > Clustering and refresh the page.

- If any Expressways have not accepted the change, repeat the same procedure.

- Validate that the cluster database status reports as Active .

### Change Cluster to use FQDNs

Note : While this procedure is performed, communications between peers are temporarily impacted, this means that is expected to see alarms that persist until the changes are complete and the cluster agrees on the new addresses.

- Sign in to all the cluster peers and navigate to System > Clustering .

- Choose which peer address is changed. it is recomended to start with Peer 1 address .

- On every peer in the cluster follow the next procedure:

- Change the chosen peer address field from the IP address to its FQDN.

- Select Save .

- Switch to the peer that is identified by the changed peer address you and restart the server.

- Wait for any transient cluster alarms to resolve.

- Choose the next peer address to be changed and then repeat steps 3 - 7.

- Repeat this procedure until you have changed all peer addresses and restarted all of the peers.

### Cluster Address Mapping for Expressway-E

For secure deployments like Mobile and Remote Access (MRA), each Expressway-E peer must have a certificate with a SAN that contains its public FQDN. The FQDN is mapped in the public DNS to the Expressway-E's public IP address.

Note : If you simply want to cluster Cisco Expressway-E peers and you don't need TLS verification between them, then you can form the cluster with the nodes' private IP addresses. You don't need cluster Address Mapping .

Cluster Address Mappings are FQDN:IP pairs which are shared around the cluster, one pair for each peer. The peers consult the Mapping Table before they query DNS and, if they find a match, they do not query DNS.

If you choose to enforce TLS, the peers must also read the names from the SAN field of each other's certificates, and check each name against the FQDN side of the mapping.

It is strongly recommended that you enter the mappings on the primary peer. Address Mappings replicate dynamically through the cluster. In order to configure Adderss Mapping , follow the next procedure:

- Nabigate to System > Clustering on the primary peer, and change the Cluster address mapping enabled dropdown to On (default is Off ). The Cluster address mapping fields display.

- Edit the mappings so that the public FQDNs of the Expressway-E peers correspond to the IP addresses of their internal NICs.

- Select Save.

Caution : Do not try to use the public DNS to map the peers' public FQDNs to their private IP addresses, this action can break external connectivity.

### Cluster with Single NIC

If you want the Expressway-E peers in a cluster to verify each other's identities with certificates, you could allow them to use DNS to resolve cluster peer FQDNs to their public IP addresses. This is a perfectly acceptable way to form a cluster if the Expressway-E nodes have:

- Only one NIC

- No Static NAT configured

- Routable IP addresses

## Troubleshooting

### What Triggers a Factory Reset?

If you clear all the peer address fields from the clustering page and save the configuration, Expressway by default performs a Factory Reset itself the next time you do a restart. This means that all configuration is deleted, except basic netowrk configuration for the Local Area Network 1 (LAN1) interface, that includes all configuration performed after you clear the fields and the next restart.

Tip : If you need to avoid the factory reset, restore the cluster peer address fields. Replace the original peer addresses in the same order, and then save the configuration to clear the banner.

The factory reset is automatically triggered when the peer restarts, to remove sensitive data and cluster configuration. The reset clears all configuration except the next basic network information:

Note : If you use the dual NIC option, be aware that any LAN2 configuration is removed completely by the reset.

- IP addresses • Admin and root accounts and passwords

- SSH keys

- Option keys

- Hypertext Transfer Protocol Secure (HTTPS) access enabled

- SSH access enabled

Note : From version X12.6 the factory reset removes the server certificate, associated private key, and CA trust store settings from the peer. In earlier Expressway software versions these settings are preserved.

### Factory Reset Failure

Factory Reset can fail, this can happen if the Expressway is a fresh install Open Virtualization Appliance (OVA), and haven't been upgraded.

In order to fix this please follow any of the next options:

- Upgrade all nodes to the same software version with tar.gz file . At the end of upgrade process, restart the server, which then trigger the Factory Reset.

- Upload tar.gz file directly to the factory reset folder with WinSCP (/mnt/harddisk/factory-reset/) . Then restart to initiate factory reset or issue factory reset from the CLI.

Note : Make sure to take proper backups before an Upgrade, Certificate change, or when there is a Factory Reset warning.

### Restart Sequence

If a restart of the cluster or any peer is needed, follow the next steps:

- Restart the primary peer, and wait for it to be accessible via web interface.

- Validate cluster replication status on the primary and status of all peers. Wait a few minutes, refresh the peer's web interfaces occasionally.

- Restart other peers, if required, one at a time. Each time, wait a few minutes after it is accessible and validate its replication status.

Note : You may need to wait about 5 minutes after make any cluste changes before the Expressway peers report successful status.

### Alarms and Warnings

The alarms of cluster erors, are shown in the format: Cluster replication error: (details) manual synchronization of configuration is required , some examples of these are the next:

- Cluster replication error: manual synchronization of configuration is required.

- Cluster replication error: cannot find primary or this subordinate's peer configuration file, manual synchronization of configuration is required.

- Cluster replication error: configuration primary ID is inconsistent, manual synchronization of configuration is required.

- Cluster replication error: this peer's configuration conflicts with the primary's configuration, manual synchronization of configuration is required.

If a subordinate Expressway reports the alarm mentioned, follow the next procedure:

- Log in as admin on an SSH or other CLI interface.

- Run the next command: xcommand ForceConfigUpdate

Note : Make sure to take proper backups before an Upgrade, Certificate change, or when there is a Factory Reset warning.

- This command deletes the subordinate Expressway configuration and then force it to update its configuration from the primary Expressway.

If the issue persist it could be related to the encryption key per cluster peer. Usually occurs when peers are upgraded in the wrong order, subordinates peers are not synchronized with the primary. So if xcommand forceconfigupdate doesn't work, follow the next procedure:

- Sign in to the primary peer and validate that it is in a good state.

- Ensure that the cluster configuration shows this peer to be the primary.

- Upgrade the primary again, use the same package that you originally used to upgrade.

The replication alarm clears after the primary peer has upgraded and rebooted. This normally happens within ten minutes after reboot, but could be up to twenty minutes after reboot.

### Common Alarms

Invalid clustering configuration: H.323 mode must be turned On - clustering uses H.323 communications between peers.

For this alarm to be cleared ensure that H.323 mode is on, navigate to Configuration > Protocols > H.323 .

Expressway database failure: Please contact your Cisco support representative.

In order to troubleshoot this kind of alarm, follow the next procedure:

- Take a system snapshot and provide it to your support representative.

- Remove the Expressway from the cluster.

- Restore that Expressway’s database from a backup taken on that Expressway previously.

- Add the Expressway back to the cluster.

A second method is possible if the database does not recover:

- Take a system snapshot and provide it to Technical Assistance Center (TAC).

- Remove the Expressway from the cluster.

- Log in as root and run the next command clusterdb_destroy_and_purge_data.sh .

- Restore that Expressway’s database from a backup taken on that Expressway previously.

- Add the Expressway back to the cluster.

Note : Make sure to take proper backups before an Upgrade, Certificate change, or when there is a Factory Reset warning.

Caution : clusterdb_destroy_and_purge_data.sh is as dangerous as it sounds — use this option as last resort.

### System Key Related Issues

Note : The next information applies for version X14 onwards.

Failed to update key file alarms are raised on Expressways on a single node scenario.

Follow the next procedure to troubleshoot this kind of alarm:

- Log in as admin through the CLI (available by default over SSH and through the serial port on hardware versions).

- Run the next command: xCommand ForceSystemKeyUpdate .

Failed to update key file alarms are raised on Expressways on a cluster scenario.

Follow the next procedure to troubleshoot this kind of alarm:

- Log in to node as admin through the CLI (available by default over SSH and through the serial port on hardware versions) where this alarm is not raised.

- Run the next command: xCommand ForceSystemKeyUpdate .

### Logs Details

Like any other log on Expressway, you can enable diagnostics logs, with TCP Dumps.

In a normal state DB Synchronization on Master node is shown in the logs as the next output:

```
2020-07-21T15:16:50.321-05:00 expc01 replication: UTCTime="2020-07-21 20:16:50,321" Module="developer.replication" Level="INFO" CodeLocation="clusterconfigurationsynchroniser(270)" Detail="Starting synchronisation"
2020-07-21T15:16:50.330-05:00 expc01 replication: UTCTime="2020-07-21 20:16:50,330" Module="developer.replication" Level="INFO" CodeLocation="clusterconfigurationutils(750)" AlternateIPAddresses="[u'(10.15.13.15 expc01)', u'(10.15.13.16 expc02)']" ConfigurationMasterIndex="0" LocalPeerIndex="0" 
2020-07-21T15:16:50.433-05:00 expc01 replication: UTCTime="2020-07-21 20:16:50,433" Module="developer.replication" Level="INFO" CodeLocation="clusterconfigurationsynchroniser(257)" Detail="This peer is the cluster master, local configuration has already been replicated to the other peers"
2020-07-21T15:16:50.437-05:00 expc01 replication: UTCTime="2020-07-21 20:16:50,437" Module="developer.replication" Level="INFO" CodeLocation="clusterconfigurationsynchroniser(336)" Detail="Synchronisation completed successfully"
```

From Peer node perspective it is shown as the next output:

```
2020-07-21T15:16:46.900-05:00 expc02 replication: UTCTime="2020-07-21 20:16:46,899" Module="developer.replication" Level="INFO" CodeLocation="clusterconfigurationsynchroniser(270)" Detail="Starting synchronisation"
2020-07-21T15:16:46.908-05:00 expc02 replication: UTCTime="2020-07-21 20:16:46,908" Module="developer.replication" Level="INFO" CodeLocation="clusterconfigurationutils(750)" AlternateIPAddresses="[u'(10.15.13.15 expc01)', u'(10.15.13.16 expc02)']" ConfigurationMasterIndex="0" LocalPeerIndex="1" 
2020-07-21T15:16:46.947-05:00 expc02 replication: UTCTime="2020-07-21 20:16:46,946" Module="developer.replication" Level="INFO" CodeLocation="clusterconfigurationsynchroniser(254)" Detail="This peer is not the cluster master, local configuration is already up to date"
2020-07-21T15:16:46.950-05:00 expc02 replication: UTCTime="2020-07-21 20:16:46,950" Module="developer.replication" Level="INFO" CodeLocation="clusterconfigurationsynchroniser(336)" Detail="Synchronisation completed successfully"
```

A Peer Disconnection is shown in the next output:

```
2020-08-12T14:57:43.353-05:00 expc01 UTCTime="2020-08-12 19:57:43,353" Module="developer.clusterdb.cdb" Level="INFO" Node="clusterdb@expc01.apolo.local" PID="<0.159.0>" Detail="Processed mnesia_down event from accessible node" Node="clusterdb@expc02.apolo.local"
2020-08-12T14:57:43.354-05:00 expc01 UTCTime="2020-08-12 19:57:43,353" Module="developer.clusterdb.cdb" Level="ERROR" Node="clusterdb@expc01.apolo.local" PID="<0.159.0>" Detail="Inconsistent Database" Context="from mnesia system - mnesia down" Node="clusterdb@expc02.apolo.local"
2020-08-12T14:57:43.354-05:00 expc01 UTCTime="2020-08-12 19:57:43,354" Module="developer.clusterdb.cdb" Level="INFO" Node="clusterdb@expc01.apolo.local" PID="<0.159.0>" Detail="Connecting database on mnesia running_partitioned_network event" Node="clusterdb@expc02.apolo.local"
2020-08-12T14:57:43.354-05:00 expc01 UTCTime="2020-08-12 19:57:43,354" Module="developer.clusterdb.cdb" Level="INFO" Node="clusterdb@expc01.apolo.local" PID="<0.14215.425>" Detail="Ready to perform node connection transaction" Node="clusterdb@expc02.apolo.local"
2020-08-12T14:57:43.354-05:00 expc01 UTCTime="2020-08-12 19:57:43,354" Module="developer.clusterdb.cdb" Level="INFO" Node="clusterdb@expc01.apolo.local" PID="<0.14215.425>" Detail="Running node connection transaction" Node="clusterdb@expc02.apolo.local"
2020-08-12T14:57:43.354-05:00 expc01 UTCTime="2020-08-12 19:57:43,354" Module="developer.clusterdb.synchronise" Level="WARN" Node="clusterdb@expc01.apolo.local" PID="<0.14215.425>" Detail="Failed connecting to node" Node="clusterdb@expc02.apolo.local" Reason="{ badrpc, { EXIT, { aborted, { noproc, { gen_server, call, [ kernel_safe_sup, { start_child, { dets_sup, { dets_sup, start_link,  }, permanent, 1000, supervisor, [ dets_sup ] } }, infinity ] } } } } }"
2020-08-12T14:57:43.524-05:00 expc01 alarm: Level="WARN" Event="Alarm Raised" Id="20006" UUID="0f96695e-d954-4f6f-85c1-2ef1eae6f764" Severity="warning" Detail="Cluster database communication failure: The database is unable to replicate with one or more of the cluster peers" UTCTime="2020-08-12 19:57:43,524"
2020-08-12T14:57:43.771-05:00 expc01 alarm: Level="WARN" Event="Alarm Raised" Id="20004" UUID="3bca6888-f622-11df-93be-07cc953d7b99" Severity="warning" Detail="Cluster communication failure: The system is unable to communicate with one or more of the cluster peers" UTCTime="2020-08-12 19:57:43,771"
```

```
2020-08-12T14:57:53.872-05:00 expc01 tvcs: UTCTime="2020-08-12 19:57:53,871" Module="network.h323" Level="INFO":  Action="Sent" Dst-ip="10.15.13.16" Dst-port="1719" Detail="Sending RAS SCI  SeqNum=52319 Retransmit=True"
2020-08-12T14:57:54.872-05:00 expc01 tvcs: UTCTime="2020-08-12 19:57:54,871" Module="network.h323" Level="INFO":  Action="Sent" Dst-ip="10.15.13.16" Dst-port="1719" Detail="Sending RAS LRQ  SeqNum=52320 Retransmit=True"
2020-08-12T14:57:56.872-05:00 expc01 tvcs: UTCTime="2020-08-12 19:57:56,871" Module="network.h323" Level="INFO":  Action="Sent" Dst-ip="10.15.13.16" Dst-port="1719" Detail="Sending RAS LRQ  SeqNum=52320 Retransmit=True"
2020-08-12T14:57:57.871-05:00 expc01 tvcs: UTCTime="2020-08-12 19:57:57,871" Module="network.h323" Level="INFO":  Action="Sent" Dst-ip="10.15.13.16" Dst-port="1719" Detail="Sending RAS SCI  SeqNum=52319 Retransmit=True"
2020-08-12T14:57:58.871-05:00 expc01 tvcs: Event="External Server Communications Failure" Reason="gatekeeper timed out" Service="NeighbourGatekeeper" Detail="name:10.15.13.16:1719" Level="1" UTCTime="2020-08-12 19:57:58,871"
2020-08-12T14:57:58.871-05:00 expc01 tvcs: UTCTime="2020-08-12 19:57:58,871" Module="network.h323" Level="INFO":  Action="Sent" Dst-ip="10.15.13.16" Dst-port="1719" Detail="Sending RAS LRQ  SeqNum=52320 Timeout=True"
2020-08-12T14:57:59.601-05:00 expc01 UTCTime="2020-08-12 19:57:59,601" Module="developer.clusterdb.peernameresolver" Level="INFO" Node="clusterdb@expc01.apolo.local" PID="<0.145.0>" Detail="Triggering forced peer update of peers which failed DNS and queueing next run" Queue-Time-ms="300000"
2020-08-12T14:58:01.871-05:00 expc01 tvcs: UTCTime="2020-08-12 19:58:01,871" Module="network.h323" Level="INFO":  Action="Sent" Dst-ip="10.15.13.16" Dst-port="1719" Detail="Sending RAS SCI  SeqNum=52319 Timeout=True"
```

Change to TLS Enforcing on the Master node is shown in the next output:

```
2020-08-12T15:13:24.970-05:00 expc01 UTCTime="2020-08-12 20:13:24,969" Module="developer.cdbtable.cdb.clusterConfiguration" Level="DEBUG" Node="clusterdb@expc01.apolo.local" PID="<0.345.0>" Detail="Inserting into table" TableName="clusterConfiguration"
2020-08-12T15:13:24.976-05:00 expc01 UTCTime="2020-08-12 20:13:24,975" Event="System Configuration Changed" Node="clusterdb@expc01.apolo.local" PID="<0.345.0>" Detail="xconfiguration clusterConfiguration tls_verify - changed from: Permissive to: Enforcing"
2020-08-12T15:13:24.976-05:00 expc01 httpd[15060]: web: Event="System Configuration Changed" Detail="configuration/cluster/tls_verify - changed from: 'Permissive' to: 'Enforcing'" Src-ip="10.15.13.30" Src-port="53155" User="admin" Level="1" UTCTime="2020-08-12 20:13:24" 
2020-08-12T15:13:24.979-05:00 expc01 management: UTCTime="2020-08-12 20:13:24,978" Module="developer.management.databasemanager" Level="INFO" CodeLocation="databasemanager(312)" Detail="Cluster configuration change detected"
2020-08-12T15:13:24.980-05:00 expc01 UTCTime="2020-08-12 20:13:24,980" Module="developer.cdbtable.cdb.clusterConfiguration" Level="DEBUG" Node="clusterdb@expc01.apolo.local" PID="<0.345.0>" Detail="Inserting into table" TableName="clusterConfiguration"
2020-08-12T15:13:24.986-05:00 expc01 management: UTCTime="2020-08-12 20:13:24,986" Module="developer.management.databasemanager" Level="INFO" CodeLocation="databasemanager(405)" Detail="TLS Verify change status" Startup="False" New="True"
2020-08-12T15:13:25.022-05:00 expc01 UTCTime="2020-08-12 20:13:25,022" Event="System Configuration Changed" Node="clusterdb@expc01.apolo.local" PID="<0.557.0>" Detail="xconfiguration alternatesConfiguration - Changed"
2020-08-12T15:13:25.022-05:00 expc01 UTCTime="2020-08-12 20:13:25,022" Module="developer.clusterdb.peernameresolver" Level="INFO" Node="clusterdb@expc01.apolo.local" PID="<0.145.0>" Detail="Notifying databasemanager (Management Framework)"
2020-08-12T15:13:25.022-05:00 expc01 UTCTime="2020-08-12 20:13:25,022" Module="developer.clusterdb.alternatesmanager" Level="INFO" Node="clusterdb@expc01.apolo.local" PID="<0.142.0>" Detail="alternate peer changed info recieved"
2020-08-12T15:13:25.031-05:00 expc01 UTCTime="2020-08-12 20:13:25,031" Event="System Configuration Changed" Node="clusterdb@expc01.apolo.local" PID="<0.557.0>" Detail="xconfiguration alternatesConfiguration - Changed" 
2020-08-12T15:13:25.192-05:00 expc01 management: UTCTime="2020-08-12 20:13:25,192" Module="developer.diagnostics.alarmmanager" Level="INFO" CodeLocation="alarmmanager(173)" Detail="Raising alarm" UUID="e2b8e3d1-b731-4d7d-b606-4682a8f0c2e6" Parameters="null"
2020-08-12T15:13:25.195-05:00 expc01 management: Level="WARN" Event="Alarm Raised" Id="20007" UUID="e2b8e3d1-b731-4d7d-b606-4682a8f0c2e6" Severity="warning" Detail="Restart required: Cluster configuration has been changed, however a restart is required for this to take effect" UTCTime="2020-08-12 20:13:25,194"
```

From the Peer node perspective it is shown in the next output:

```
2020-08-12T15:13:24.976-05:00 expc02 UTCTime="2020-08-12 20:13:24,976" Event="System Configuration Changed" Node="clusterdb@expc02.apolo.local" PID="<0.390.0>" Detail="xconfiguration clusterConfiguration tls_verify - changed from: Permissive to: Enforcing"
2020-08-12T15:13:24.979-05:00 expc02 management: UTCTime="2020-08-12 20:13:24,978" Module="developer.management.databasemanager" Level="INFO" CodeLocation="databasemanager(312)" Detail="Cluster configuration change detected"
2020-08-12T15:13:24.982-05:00 expc02 management: UTCTime="2020-08-12 20:13:24,982" Module="developer.management.databasemanager" Level="INFO" CodeLocation="databasemanager(405)" Detail="TLS Verify change status" Startup="False" New="True"
2020-08-12T15:13:25.040-05:00 expc02 UTCTime="2020-08-12 20:13:25,040" Module="developer.clusterdb.peernameresolver" Level="INFO" Node="clusterdb@expc02.apolo.local" PID="<0.136.0>" Detail="Notifying databasemanager (Management Framework)"
2020-08-12T15:13:25.040-05:00 expc02 UTCTime="2020-08-12 20:13:25,040" Module="developer.clusterdb.alternatesmanager" Level="INFO" Node="clusterdb@expc02.apolo.local" PID="<0.143.0>" Detail="alternate peer changed info recieved"
2020-08-12T15:13:25.041-05:00 expc02 UTCTime="2020-08-12 20:13:25,041" Event="System Configuration Changed" Node="clusterdb@expc02.apolo.local" PID="<0.543.0>" Detail="xconfiguration alternatesConfiguration - Changed"
2020-08-12T15:13:25.042-05:00 expc02 UTCTime="2020-08-12 20:13:25,042" Event="System Configuration Changed" Node="clusterdb@expc02.apolo.local" PID="<0.543.0>" Detail="xconfiguration alternatesConfiguration - Changed"
2020-08-12T15:13:25.046-05:00 expc02 UTCTime="2020-08-12 20:13:25,046" Module="developer.clusterdb.alternatesmanager" Level="INFO" Node="clusterdb@expc02.apolo.local" PID="<0.143.0>" Detail="alternate peer changed info recieved"
2020-08-12T15:13:25.047-05:00 expc02 UTCTime="2020-08-12 20:13:25,046" Module="developer.clusterdb.peernameresolver" Level="INFO" Node="clusterdb@expc02.apolo.local" PID="<0.136.0>" Detail="Notifying databasemanager (Management Framework)"
2020-08-12T15:13:25.047-05:00 expc02 UTCTime="2020-08-12 20:13:25,047" Event="System Configuration Changed" Node="clusterdb@expc02.apolo.local" PID="<0.543.0>" Detail="xconfiguration alternatesConfiguration - Changed"
2020-08-12T15:13:25.049-05:00 expc02 UTCTime="2020-08-12 20:13:25,049" Event="System Configuration Changed" Node="clusterdb@expc02.apolo.local" PID="<0.543.0>" Detail="xconfiguration alternatesConfiguration - Changed"
 2020-08-12T15:13:25.136-05:00 expc02 management: UTCTime="2020-08-12 20:13:25,136" Module="developer.diagnostics.alarmmanager" Level="INFO" CodeLocation="alarmmanager(173)" Detail="Raising alarm" UUID="e2b8e3d1-b731-4d7d-b606-4682a8f0c2e6" Parameters="null"
2020-08-12T15:13:25.139-05:00 expc02 management: Level="WARN" Event="Alarm Raised" Id="20007" UUID="e2b8e3d1-b731-4d7d-b606-4682a8f0c2e6" Severity="warning" Detail="Restart required: Cluster configuration has been changed, however a restart is required for this to take effect" UTCTime="2020-08-12 20:13:25,139"
```

### Videos

The next vieos could be useful:

How to Create and Add a Peer to an Expressway Cluster

Removing a Peer from an Expressway Cluster

Fixing Expressway Replication Error "Peer's Configuration Conflicts With Primary"

Expressway Cluster Restart Procedure

How to Upgrade an Expressway Cluster Generating CSR for MRA/ Clustered Expressways

### Revision History

1.0

02-Jul-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 02-Jul-2021 | Initial Release |