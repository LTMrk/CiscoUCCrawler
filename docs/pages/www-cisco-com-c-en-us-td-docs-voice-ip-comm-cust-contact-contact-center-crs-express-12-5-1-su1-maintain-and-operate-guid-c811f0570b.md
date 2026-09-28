---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-maintain-and-operate-guid-c811f0570b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/maintain_and_operate/guide/uccx_b_1251su1admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_010111.html
retrieved_at: 2026-08-16T21:39:48.416039+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

Updated: January 31, 2021

Chapter: CUIC Cluster Configuration

## Chapter: CUIC Cluster Configuration

- CUIC Cluster Configuration

- Cluster Configuration for JVM Using Hazelcast

- Troubleshooting Cluster Configuration

# CUIC Cluster Configuration

## Cluster Configuration for JVM Using Hazelcast

Cisco Unified Intelligence Center uses Hazelcast for application clustering. Hazelcast provides a second-level cache for the
                              Unified Intelligence Center application layer. When any entity (for example: report, report definition, and so on) cached
                              by Hazelcast is updated in one of the Unified Intelligence Center nodes, it must be invalidated and reloaded in all the other
                              Unified Intelligence Center nodes in the cluster. The Hazelcast cluster automatically takes care of it by publishing clusterwide
                              notifications containing the identifiers of such entities which must be invalidated.

In Unified Intelligence Center, the default mechanism for Hazelcast cluster discovery or formation is UDP multicast. Unified
                              Intelligence Center uses the Multicast group IP address 224.2.2.3 and port 54327. You cannot change these settings in Unified
                              Intelligence Center.

The UDP multicast based discovery mechanism will not work for the customer in the following scenarios:

When the network has multicasting disabled.

If the nodes in the Unified Intelligence Center cluster are in different subnets.

In such scenarios, you can change the discovery mechanism to TCP/IP. You can form the CUIC application cluster using TCP/IP
                              instead of the default UDP Multicast based discovery mechanism.

Use the following CLI commands to manage the cluster mode (UDP Multicast vs TCP/IP). That is, use the following CLI commands
                              to switch to TCP/IP only if the customer’s network does not support Multicasting:

utils cuic cluster show —This command shows the current cluster mode that is enabled on this node and the other member details.

The member details are available only in the TCP/IP mode. The member details displayed are of the configured members and does
                                                not represent the cluster in real time.

utils cuic cluster mode —This command is used to switch the Hazelcast cluster join configuration from Multicast to TCP/IP and the opposite way.

After changing the cluster mode in all the nodes, restart “Intelligence Center Reporting Service” in all the nodes starting
                                                from the publisher sequentially.

utils cuic cluster refresh —This command refreshes the cluster member information only when run in the TCP/IP mode. Run this command when there is an
                                    addition or deletion of nodes to the CUIC cluster, which is already in TCP/IP.

Usage

You can use these commands using to switch to TCP/IP only when the customer’s network does not support the Multicasting requirements
                              that are specified in Port Utilization Guide for Cisco Unified Contact Center Solutions > Intracluster Ports Between Cisco Unified Intelligence Center section available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

Stop the “ Cisco Unified Intelligence Center Reporting Service” on all the Unified Intelligence Center nodes before performing cluster configuration
                                                changes using these CLI commands.

When you have completed the cluster configuration changes on all nodes, use the “utils cuic cluster show” command to ensure
                                                that all nodes have identical configuration before starting “ Cisco Unified Intelligence Center Reporting Service” on any one of them.

Unified Intelligence Center cluster / application will work only if all the nodes use the same mode–that is, either Multicast
                                                or TCP/IP. Mixed mode is not allowed.

If the network is disconnected and after the cluster nodes retain the network, ensure to perform “synchronize cluster” from
                                                all the nodes after logging into the Unified Intelligence Center reporting application.

Steps

Run the following CLIs on all nodes in the given sequence starting from the Publisher node:

Run every step on all nodes before performing the subsequent step.

Step 1

utils service stop Cisco Unified Intelligence Center Reporting Service

Step 2

utils cuic cluster mode

Step 3

utils cuic cluster show

Ensure that all nodes have identical configuration.

Step 4

utils service start Cisco Unified Intelligence Center Reporting Service

If there is a network disconnect and reconnect, check if the database replication is successfully set up across all nodes
                                                      in the cluster and then perform "Synchronize Cluster" from the legacy Cisco Unified Intelligence Center. This ensures that
                                                      cache is in sync across the cluster.

## Troubleshooting Cluster Configuration

Verify the Hazlecast Cluster Formation using Hazelcast REST client. To verify, replace <CUIC-IP> with the IP address of any
                           CUIC member in the following URL.

http://<CUIC-IP>:57011/hazelcast/rest/cluster

The Unified Intelligence Center application cluster can be down in the following cases:

Common Cases:

Node is not reachable

Unified Intelligence Center Reporting Service is down

Hazelcast default Port 57011 is not enabled in Unified Intelligence Center nodes in the customer environment, which is used
                                       to communicate between cluster members.

When multicasting is being used for the member discovery (Default method):

Network has UDP multicast disabled

UDP port 54327 used for Hazelcast member discovery is disabled

Multicast default group IP 224.2.2.3 is not allowed in the network

UCCX nodes are distributed across different subnets

If any of the above mentioned cases cause issue because of the restrictions on multicasting in the customer environment, you
                                             can use TCP/IP for Hazelcast discovery.

For more information, contact Cisco support to troubleshoot and reset the cluster.

| Note | The member details are available only in the TCP/IP mode. The member details displayed are of the configured members and does
                                                not represent the cluster in real time. |
|---|---|

| Note | After changing the cluster mode in all the nodes, restart “Intelligence Center Reporting Service” in all the nodes starting
                                                from the publisher sequentially. |
|---|---|

| Note | Stop the “ Cisco Unified Intelligence Center Reporting Service” on all the Unified Intelligence Center nodes before performing cluster configuration
                                                changes using these CLI commands. When you have completed the cluster configuration changes on all nodes, use the “utils cuic cluster show” command to ensure
                                                that all nodes have identical configuration before starting “ Cisco Unified Intelligence Center Reporting Service” on any one of them. Unified Intelligence Center cluster / application will work only if all the nodes use the same mode–that is, either Multicast
                                                or TCP/IP. Mixed mode is not allowed. If the network is disconnected and after the cluster nodes retain the network, ensure to perform “synchronize cluster” from
                                                all the nodes after logging into the Unified Intelligence Center reporting application. |
|---|---|

| Note | Run every step on all nodes before performing the subsequent step. |
|---|---|

| Step 1 | utils service stop Cisco Unified Intelligence Center Reporting Service |
|---|---|
| Step 2 | utils cuic cluster mode |
| Step 3 | utils cuic cluster show Note Ensure that all nodes have identical configuration. | Note | Ensure that all nodes have identical configuration. |
| Note | Ensure that all nodes have identical configuration. |
| Step 4 | utils service start Cisco Unified Intelligence Center Reporting Service Note If there is a network disconnect and reconnect, check if the database replication is successfully set up across all nodes
                                                      in the cluster and then perform "Synchronize Cluster" from the legacy Cisco Unified Intelligence Center. This ensures that
                                                      cache is in sync across the cluster. | Note | If there is a network disconnect and reconnect, check if the database replication is successfully set up across all nodes
                                                      in the cluster and then perform "Synchronize Cluster" from the legacy Cisco Unified Intelligence Center. This ensures that
                                                      cache is in sync across the cluster. |
| Note | If there is a network disconnect and reconnect, check if the database replication is successfully set up across all nodes
                                                      in the cluster and then perform "Synchronize Cluster" from the legacy Cisco Unified Intelligence Center. This ensures that
                                                      cache is in sync across the cluster. |

| Note | Ensure that all nodes have identical configuration. |
|---|---|

| Note | If there is a network disconnect and reconnect, check if the database replication is successfully set up across all nodes
                                                      in the cluster and then perform "Synchronize Cluster" from the legacy Cisco Unified Intelligence Center. This ensures that
                                                      cache is in sync across the cluster. |
|---|---|

| Note | If any of the above mentioned cases cause issue because of the restrictions on multicasting in the customer environment, you
                                             can use TCP/IP for Hazelcast discovery. |
|---|---|