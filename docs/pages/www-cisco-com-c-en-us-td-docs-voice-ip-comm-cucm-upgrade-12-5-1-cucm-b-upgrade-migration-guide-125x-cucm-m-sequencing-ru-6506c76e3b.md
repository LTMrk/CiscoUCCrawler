---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-upgrade-12-5-1-cucm-b-upgrade-migration-guide-125x-cucm-m-sequencing-ru-6506c76e3b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-125x/cucm_m_sequencing-rules-time-requirements-1251.html
retrieved_at: 2026-08-17T00:06:35.294581+00:00
---

Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)

# Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)

Updated: July 25, 2025

Chapter: Sequencing Rules and Time Requirements

## Chapter: Sequencing Rules and Time Requirements

# Sequencing Rules and Time Requirements

Use this information in this appendix only if you need  information on sequencing and time requirements.

## Upgrade Sequence and Time Requirements

The sequence in which you perform upgrade procedures depends on your deployment, and on how you want to balance the level
                              of user impact with the amount of time required to complete the upgrade. You must identify the sequence that you will follow
                              before you are ready to perform the upgrade process.

The information in this section applies only if you are performing a direct upgrade using either the Unified CM OS Administration
                              interface or the PCD Upgrade task. PCD Migrations do not require this step.

### Understanding Version Switching

When you upgrade a node, the new software is installed as an inactive version. To activate the new software, you must switch
                                 the node to the new software version. There are two ways to switch to the new software version:

Automatic switching—the system switches the version automatically as part of the upgrade process

Manual switching—physically switch the version using the OS Administration interface after the upgrade process is complete

The method that you choose depends on the type of upgrade that you are doing. During the upgrade process, the wizard prompts
                                 you to choose whether to switch the software version automatically by rebooting to the upgraded partition, or whether to switch
                                 the version manually at a later time. The table below lists the switching method to use for each type of upgrade.

Upgrade type

Switching type

When prompted, choose . . .

Result

Standard upgrade

Automatic

GUI: Reboot to upgraded partition

CLI: Switch to new version after upgrade

When you choose this option, the system reboots to the new software version.

Manual

GUI: Do not reboot after upgrade

CLI: Do not switch to new version after upgrade

When you choose this option, the system continues to run the old software version when the upgrade is complete. You can manually
                                             switch to the new software later.

Refresh upgrade

Automatic

GUI: Reboot to upgraded partition

CLI: Switch to new version after upgrade

Choose this option to use the new software version immediately following the upgrade.

Manual

GUI: Do not reboot after upgrade

CLI: Do not switch to new version after upgrade

Use this option only if you are performing a refresh upgrade in stages. When you choose this option the system reboots to
                                             the old software version when the upgrade is complete, and you can manually switch to the new software later.

When you switch versions, your configuration information migrates automatically to the upgraded version on the active partition.

If for any reason you decide to back out of the upgrade, you
                                 		  can restart the system to the inactive partition that contains the older
                                 		  version of the software. However, any configuration changes that you made since
                                 		  you upgraded the software will be lost.

For a short period of time after you install Unified Communications Manager or switch over after upgrading to a different product version, any changes made by phone users may be lost. Examples of phone
                                 user settings include call forwarding and message waiting indication light settings. This can occur because Unified Communications Manager synchronizes the database after an installation or upgrade, which can overwrite phone user settings changes.

### Recommended Sequence (Refresh Upgrades)

The following table shows the recommended sequence for performing a refresh upgrade. This method provides the least time and
                                 impact for the upgrade.

Sequence

Unified Communications Manager Nodes

IM and Presence Service Nodes

1

Upgrade the publisher node to the new software version. The new software is inactive.

—

2

Upgrade the secondary subcriber nodes in parallel. The new software is inactive.

Upgrade the IM and Presence database publisher node in parallel with the Unified Communications Manager subscriber nodes.

3

Upgrade the primary subscriber nodes

Upgrade the subscriber nodes. The new software is inactive.

4

Switch the software version on the publisher node and reboot it. The new software is active.

—

5

Switch the software version on the secondary subscriber nodes in parallel and reboot them.

Switch the software version on the database publisher node and reboot it. The new software is active.

6

Switch the software version on the primary subscriber nodes in parallel and reboot them.

Switch the software version on the subscriber nodes in parallel and reboot them. The new software is active.

7

Ensure that database replication is complete and functioning between the publisher node and all subscriber nodes before proceeding.

Ensure that database replication is complete and functioning between the publisher node and all subscriber nodes.

### Sequence Rules

When you are planning to perform an upgrade using either the Unified CM OS Admin interface or the PCD upgrade task, you must ensure that your plan takes the following sequencing rules into account.

The Unified Communications Manager publisher node must be the first node that you upgrade. The new software is installed as an inactive version.

You can begin upgrading Unified Communications Manager subscriber nodes as soon as the publisher node has been upgraded with an inactive version of the new software.

You must switch the Unified Communications Manager publisher node to the new software version and reboot it before you switch the version on any subscriber nodes. The publisher
                                       node must be the first node to switch to the new software version and reboot.

If you upgrade a group of subscriber nodes, after you switch the software version and reboot, you must wait for database replication
                                       to complete on all subscriber nodes before proceeding with any COP file installs or configuration changes.

If you are upgrading Unified Communications Manager nodes to a Maintenance Release (MR) or an Engineering Special (ES) Release and you are not upgrading IM and Presence Service nodes, you must reboot all IM and Presence nodes after the Unified Communications Manager upgrade is complete.

If you are upgrading IM and Presence Service nodes in addition to Unified Communications Manager nodes:

The IM and Presence Service database publisher node must be the first IM and Presence Service node that you upgrade. The new software is installed as an inactive version.

You can begin upgrading IM and Presence Service subscriber nodes as soon as the publisher node has been upgraded with an inactive version of the new software.

You can wait until all of the Unified Communications Manager nodes are upgraded to an inactive version before you upgrade the IM and Presence Service database publisher node, or you can choose to upgrade in parallel. If you upgrade in parallel, start upgrading the IM and Presence Service database publisher node at the same time that you upgrade the Unified Communications Manager subscriber nodes.

You must switch to the new software version and reboot all Unified Communications Manager nodes, starting with the publisher node, before you can switch versions on the IM and Presence Service nodes.

You must switch the IM and Presence Service database publisher node to the new software version and reboot it before you switch the software version on any IM and Presence Service subscriber nodes.

If you upgrade a group of IM and Presence Service subscriber nodes, after you switch the software version and reboot, you must wait for database replication to complete on
                                             all subscriber nodes before proceeding.

If you are upgrading IM and Presence Service nodes to a Maintenance Release (MR) or an Engineering Special (ES) Release and you are not upgrading Unified Communications Manager nodes, the following additional sequencing rules apply:

For upgrades using the Unified CM OS Admin interface, you must upgrade the Unified Communications Manager publisher node and then upgrade the IM and Presence Service nodes to the Maintenance Release (MR) or an Engineering Special (ES) Release.

If you are using the Prime Collaboration Deployment migration task, you must select the Unified Communications Manager publisher node in addition to the IM and Presence Service nodes.

If you are using the Prime Collaboration Deployment upgrade task, you do not need to select the Unified Communications Manager publisher node as long as the first 3 digits of new version of IM and Presence Service match the first 3 digits of the currently installed version of Unified Communications Manager .

## Upgrade time requirements

The time required to upgrade the software is variable and depends on a number of factors. Use the information in the following
                              sections to understand the steps you can take to optimize the upgrade process. The following sections also provide information
                              and examples to help you to estimate the time requirements for an upgrade.

### Factors that Affect Upgrade Time Requirements

The table below lists the factors that impact the amount of time that an upgrade requires. You can reduce the amount of time
                                 needed for an upgrade by ensuring that your system meets these conditions.

Item

Description

External Services and Tools

Time requirements are reduced when external services and tools, such as NTP servers, DNS servers, LDAP directories, and other
                                             network services are reachable with response times as short as possible with no dropped packets.

We recommend that you configure the ESXi server and the Unified Communications Manager publisher node to point to the same NTP server.

To avoid upgrade failures due to time sync issues with VM, disable the VM's NTP sync with the ESXi host using the workaround
                                                         mentioned in the following link: https://knowledge.broadcom.com/external/article?legacyId=1189 .

Accessibility of upgrade images

Save time by ensuring that ISO images are on DVD, or are already downloaded and staged on the same LAN as the Unified Communications Manager and IM and Presence Service virtual machines (VM).

System health

The virtual machine configuration impacts the time requirement for an upgrade. Use the virtual machine specifications that
                                             are correct for your deployment size. If your database exceeds the virtual machine's configuration limits, the upgrade process
                                             will take longer to complete or fail. For example, having too many devices for the VM configuration will impact the upgrade.

Low memory or memory leaks will impact the upgrade.

Round Trip Times (RTT) between nodes will extend the time required.

Ensure that there are no OutOfSynch (OOS) tables in the database.

Ensure that there are no SD link out-of -service events on the Unified Communications Manager node. These events typically indicate a network problem, which you must address before you begin the upgrade process.

System errors can impact upgrade time. In the Real Time Monitoring Tool (RTMT) interface, double-click Alert Central in the
                                             left navigation pane and ensure that there are no errors.

Physical and virtual hardware infrastructure

Upgrade time is reduced when your infrastructure is configured for high-capacity and low-latency, and when there is low contention
                                             from other traffic. For example, you can optimize the upgrade process by ensuring that:

There are no infrastructure bottlenecks from VMs sharing same ESXi host, the same Direct Attached Storage (DAS) volume, the
                                                   same Logical Unit Number (LUN), or the same congested network link.

Storage latencies meet the requirements specified at ../www.cisco.com/go/virtualized-collaboration .

The physical CPU cores and the virtualization design comply with virtualization requirements of Unified Communications Manager and IM and Presence Service . Do not oversubscribe CPUs by having VMs share the host resources; use logical cores or resource reservations

Unified Communications Manager and IM and Presence Service virtual machines are on same hosts, or on hosts wtih 1GbE LAN between them with low contention from other traffic.

If the cluster is over a WAN, ensure that you follow all bandwidth and latency rules listed in the Cisco Collaboration Systems Solution Reference Network Designs (SRND) for at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-implementation-design-guides-list.html .

System capacity

Reduce the upgrade time by purging unnecessary files, such as:

Call Detail Recording (CDR) records

Outdated files, such as TFTP files, firmware, and log files

Throttling

On IM and Presence Service nodes, the system throttles the upgrade process to preserve system stability during upgrades. Throttling may increase the
                                             time required to complete the upgrade. Although you can disable throttling to decrease the time it takes to perform the upgrade,
                                             doing so may degrade system performance.

### Estimating the Minimum Time Requirements

The table below lists the minimum amount of elapsed time to expect for each task in the upgrade process under ideal conditions.
                                 Your upgrade may take longer than the times listed in this table, depending on your network conditions and on the upgrade
                                 sequence that you follow.

Once you begin the upgrade process, you cannot make configuration changes until the upgrade is complete and you have performed
                                             all of the post-upgrade tasks. Configuration changes include:

changes made through any of the Unified Communications Manager or IM and Presence Service graphical user interfaces (GUI), the command line interface (CLI), or the AXL API

LDAP synchronizations, including incremental synchronizations that are pushed to Unified Communications Manager from an Oracle LDAP

automated jobs

devices attempting to autoregister

Task

Minimum Time

Service Impact

Upgrade the Unified Communications Manager publisher node to an inactive version

2 to 4 hours

Add 1 hour if a refresh upgrade

Refresh upgrades: no access to the UI

Upgrade the Unified Communications Manager subscriber nodes to an inactive version

1 to 2 hours

Refresh upgrades: phones are unavailable if no backup subscribers are configured

Switch the Unified Communications Manager publisher node to the new software version and reboot

30 minutes

—

Switch the Unified Communications Manager subscriber nodes to the new software version and reboot

30 minutes

Standard upgrades:  phones are unavailable if no backup subscribers are configured

Unified Communications Manager database replication

30 minutes for deployments with small clusters or small databases

2 hours for megaclusters or large databases

WAN latency of 80ms or more can significantly lengthen these times

Phones are available with dial tone but end-user features are unavailable until upgrade is complete

Upgrade the IM and Presence Service database publisher node to an inactive version

2 to 4 hours

Add 1 hour if a refresh upgrade

At the time of L2 upgrade neither phone services nor IM and Presence should be impacted

IM and Presence should be impacted only in the case of Refresh Upgrade

Upgrade the IM and Presence Service subscriber nodes to an inactive version

1 to 2 hours

During the switch version , irrespective of L2 or Refresh Upgrade phone services should continue to work while IM and Presence
                                             is impacted

Switch the IM and Presence Service publisher node to the new software version and reboot

30 minutes

IM and Presence high availability is disabled

Jabber is unavailable

Switch the IM and Presence Service subscriber nodes to the new software version and reboot

30 minutes

IM and Presence high availability is disabled

Jabber is unavailable

IM and Presence Service database replication

30 minutes for deployments with small clusters or small databases

2 hours for megaclusters or large databases

IM and Presence high availability is disabled

Jabber is unavailable

### Examples

The examples in this section are based on the following upgrade scenario:

a megacluster that includes Unified Communications Manager nodes as well as Instant Messaging and Presence  nodes

75,000 users

a system that is healthy and that has been optimized for the upgrade, as described in Factors that Affect Upgrade Time Requirements

| Upgrade type | Switching type | When prompted, choose . . . | Result |
|---|---|---|---|
| Standard upgrade | Automatic | GUI: Reboot to upgraded partition CLI: Switch to new version after upgrade | When you choose this option, the system reboots to the new software version. |
| Manual | GUI: Do not reboot after upgrade CLI: Do not switch to new version after upgrade | When you choose this option, the system continues to run the old software version when the upgrade is complete. You can manually
                                             switch to the new software later. |
| Refresh upgrade | Automatic | GUI: Reboot to upgraded partition CLI: Switch to new version after upgrade | Choose this option to use the new software version immediately following the upgrade. |
| Manual | GUI: Do not reboot after upgrade CLI: Do not switch to new version after upgrade | Use this option only if you are performing a refresh upgrade in stages. When you choose this option the system reboots to
                                             the old software version when the upgrade is complete, and you can manually switch to the new software later. |

| Sequence | Unified Communications Manager Nodes | IM and Presence Service Nodes |
|---|---|---|
| 1 | Upgrade the publisher node to the new software version. The new software is inactive. | — |
| 2 | Upgrade the secondary subcriber nodes in parallel. The new software is inactive. | Upgrade the IM and Presence database publisher node in parallel with the Unified Communications Manager subscriber nodes. |
| 3 | Upgrade the primary subscriber nodes | Upgrade the subscriber nodes. The new software is inactive. |
| 4 | Switch the software version on the publisher node and reboot it. The new software is active. | — |
| 5 | Switch the software version on the secondary subscriber nodes in parallel and reboot them. | Switch the software version on the database publisher node and reboot it. The new software is active. |
| 6 | Switch the software version on the primary subscriber nodes in parallel and reboot them. | Switch the software version on the subscriber nodes in parallel and reboot them. The new software is active. |
| 7 | Ensure that database replication is complete and functioning between the publisher node and all subscriber nodes before proceeding. | Ensure that database replication is complete and functioning between the publisher node and all subscriber nodes. |

| Item | Description |
|---|---|
| External Services and Tools | Time requirements are reduced when external services and tools, such as NTP servers, DNS servers, LDAP directories, and other
                                             network services are reachable with response times as short as possible with no dropped packets. We recommend that you configure the ESXi server and the Unified Communications Manager publisher node to point to the same NTP server. Note To avoid upgrade failures due to time sync issues with VM, disable the VM's NTP sync with the ESXi host using the workaround
                                                         mentioned in the following link: https://knowledge.broadcom.com/external/article?legacyId=1189 . | Note | To avoid upgrade failures due to time sync issues with VM, disable the VM's NTP sync with the ESXi host using the workaround
                                                         mentioned in the following link: https://knowledge.broadcom.com/external/article?legacyId=1189 . |
| Note | To avoid upgrade failures due to time sync issues with VM, disable the VM's NTP sync with the ESXi host using the workaround
                                                         mentioned in the following link: https://knowledge.broadcom.com/external/article?legacyId=1189 . |
| Accessibility of upgrade images | Save time by ensuring that ISO images are on DVD, or are already downloaded and staged on the same LAN as the Unified Communications Manager and IM and Presence Service virtual machines (VM). |
| System health | The virtual machine configuration impacts the time requirement for an upgrade. Use the virtual machine specifications that
                                             are correct for your deployment size. If your database exceeds the virtual machine's configuration limits, the upgrade process
                                             will take longer to complete or fail. For example, having too many devices for the VM configuration will impact the upgrade. |
| Low memory or memory leaks will impact the upgrade. |
| Round Trip Times (RTT) between nodes will extend the time required. |
| Ensure that there are no OutOfSynch (OOS) tables in the database. |
| Ensure that there are no SD link out-of -service events on the Unified Communications Manager node. These events typically indicate a network problem, which you must address before you begin the upgrade process. |
| System errors can impact upgrade time. In the Real Time Monitoring Tool (RTMT) interface, double-click Alert Central in the
                                             left navigation pane and ensure that there are no errors. |
| Physical and virtual hardware infrastructure | Upgrade time is reduced when your infrastructure is configured for high-capacity and low-latency, and when there is low contention
                                             from other traffic. For example, you can optimize the upgrade process by ensuring that: There are no infrastructure bottlenecks from VMs sharing same ESXi host, the same Direct Attached Storage (DAS) volume, the
                                                   same Logical Unit Number (LUN), or the same congested network link. Storage latencies meet the requirements specified at ../www.cisco.com/go/virtualized-collaboration . The physical CPU cores and the virtualization design comply with virtualization requirements of Unified Communications Manager and IM and Presence Service . Do not oversubscribe CPUs by having VMs share the host resources; use logical cores or resource reservations Unified Communications Manager and IM and Presence Service virtual machines are on same hosts, or on hosts wtih 1GbE LAN between them with low contention from other traffic. If the cluster is over a WAN, ensure that you follow all bandwidth and latency rules listed in the Cisco Collaboration Systems Solution Reference Network Designs (SRND) for at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-implementation-design-guides-list.html . |
| System capacity | Reduce the upgrade time by purging unnecessary files, such as: Call Detail Recording (CDR) records Outdated files, such as TFTP files, firmware, and log files |
| Throttling | On IM and Presence Service nodes, the system throttles the upgrade process to preserve system stability during upgrades. Throttling may increase the
                                             time required to complete the upgrade. Although you can disable throttling to decrease the time it takes to perform the upgrade,
                                             doing so may degrade system performance. |

| Note | To avoid upgrade failures due to time sync issues with VM, disable the VM's NTP sync with the ESXi host using the workaround
                                                         mentioned in the following link: https://knowledge.broadcom.com/external/article?legacyId=1189 . |
|---|---|

| Note | Once you begin the upgrade process, you cannot make configuration changes until the upgrade is complete and you have performed
                                             all of the post-upgrade tasks. Configuration changes include: changes made through any of the Unified Communications Manager or IM and Presence Service graphical user interfaces (GUI), the command line interface (CLI), or the AXL API LDAP synchronizations, including incremental synchronizations that are pushed to Unified Communications Manager from an Oracle LDAP automated jobs devices attempting to autoregister |
|---|---|

| Task | Minimum Time | Service Impact |
|---|---|---|
| Upgrade the Unified Communications Manager publisher node to an inactive version | 2 to 4 hours Add 1 hour if a refresh upgrade | Refresh upgrades: no access to the UI |
| Upgrade the Unified Communications Manager subscriber nodes to an inactive version | 1 to 2 hours | Refresh upgrades: phones are unavailable if no backup subscribers are configured |
| Switch the Unified Communications Manager publisher node to the new software version and reboot | 30 minutes | — |
| Switch the Unified Communications Manager subscriber nodes to the new software version and reboot | 30 minutes | Standard upgrades:  phones are unavailable if no backup subscribers are configured |
| Unified Communications Manager database replication | 30 minutes for deployments with small clusters or small databases 2 hours for megaclusters or large databases Note WAN latency of 80ms or more can significantly lengthen these times | Note | WAN latency of 80ms or more can significantly lengthen these times | Phones are available with dial tone but end-user features are unavailable until upgrade is complete |
| Note | WAN latency of 80ms or more can significantly lengthen these times |
| Upgrade the IM and Presence Service database publisher node to an inactive version | 2 to 4 hours Add 1 hour if a refresh upgrade | At the time of L2 upgrade neither phone services nor IM and Presence should be impacted IM and Presence should be impacted only in the case of Refresh Upgrade |
| Upgrade the IM and Presence Service subscriber nodes to an inactive version | 1 to 2 hours | During the switch version , irrespective of L2 or Refresh Upgrade phone services should continue to work while IM and Presence
                                             is impacted |
| Switch the IM and Presence Service publisher node to the new software version and reboot | 30 minutes | IM and Presence high availability is disabled Jabber is unavailable |
| Switch the IM and Presence Service subscriber nodes to the new software version and reboot | 30 minutes | IM and Presence high availability is disabled Jabber is unavailable |
| IM and Presence Service database replication | 30 minutes for deployments with small clusters or small databases 2 hours for megaclusters or large databases Note WAN latency can significantly lengthen these times. The maximum WAN latency accepted is 80m. | Note | WAN latency can significantly lengthen these times. The maximum WAN latency accepted is 80m. | IM and Presence high availability is disabled Jabber is unavailable |
| Note | WAN latency can significantly lengthen these times. The maximum WAN latency accepted is 80m. |

| Note | WAN latency of 80ms or more can significantly lengthen these times |
|---|---|

| Note | WAN latency can significantly lengthen these times. The maximum WAN latency accepted is 80m. |
|---|---|