---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-15-admingd-cucm-b-administration-guide-15-cucm-m-pre-change-tasks-918bbbf416
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/adminGd/cucm_b_administration-guide-15/cucm_m_pre-change-tasks.html
retrieved_at: 2026-08-17T00:38:09.630921+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 31, 2025

Chapter: Pre-Change Tasks and System Health Checks

## Chapter: Pre-Change Tasks and System Health Checks

# Pre-Change Tasks and System Health Checks

## Pre-Change Tasks

## IP Address, Hostname, and Other Network Identifier Changes

You can change the network-level IP address and hostname name of nodes in your deployment for a variety of reasons, including
                           moving the node from one cluster to another or resolving a duplicate IP address problem. The IP address is the network-level
                           Internet Protocol (IP) associated with the node, and the Hostname is the network-level hostname of the node.

All Unified Communications products such as Cisco Unified Communications Manager, Cisco Unity Connections, and Cisco IM and
                                       Presence, and so on, have only one interface. Thus, you can assign only one IP address for each of these products.

For changes to other network identifiers, such as the node name and domain name, see the following resources:

System Configuration Guide for Cisco Unified Communications Manager

Configuration and Administration Guide for the IM and Presence Service

Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service

For IM and Presence Service , instructions to change the node name and the network-level DNS default domain name for the node are also included in this
                           document.

### IM and Presence
                           	 Service Node Name and Default Domain Name Changes

The node name is configured using Cisco Unified CM Administration GUI and must be resolvable from all other IM and Presence Service nodes and from all client machines. Therefore, the recommended node name value is the network FQDN of the node. However,
                                 both IP address and hostname are also supported as values for the node name in certain deployments. See the Hostname Configuration for more information about node name recommendations and the supported deployment types.

The network-level DNS default domain name of the node is combined with
                                 		  the hostname to form the Fully Qualified Domain Name (FQDN) for the node. For
                                 		  example, a node with hostname "imp-server" and domain "example.com" has an FQDN of "imp-server.example.com" .

Do not confuse the network-level DNS default domain of the node with the enterprise-wide domain of the IM and Presence Service application.

The network-level DNS default domain is used only as a network identifier for the node.

The enterprise-wide IM and Presence Service domain is the application-level domain that is used in the end-user IM address.

You can configure the enterprise-wide domain using either Cisco
                                 		  Unified CM IM and Presence Administration GUI or Cisco Unified Communications Manager
                                    			 Administration . See the Deployment Guide for IM and Presence Service on Cisco Unified
                                    			 Communications Manager for more information about enterprise-wide
                                 		  domains and the supported deployment types.

### Hostname Configuration

The following table lists the locations where you can
                                 		  configure a host name for the Unified Communications Manager server, the
                                 		  allowed number of characters for the host name, and the recommended first and
                                 		  last characters for the host name. Be aware that, if you do not configure the
                                 		  host name correctly, some components in Unified Communications Manager ,
                                 		  such as the operating system, database, installation, and so on, may not work
                                 		  as expected.

Host Name Location

Allowed Configuration

Allowed Number of Characters

Recommended First Character for Host Name

Recommended Last Character for Host Name

Host Name/ IP Address field

System > Server in Cisco Unified Communications Manager Administration

You can add or change the host name for a server in the cluster.

2-63

alphabetic

alphanumeric

Hostname field

Cisco Unified Communications Manager installation wizard

You can add the host name for a server in the cluster.

1-63

alphabetic

alphanumeric

Hostname field

Settings > IP > Ethernet in Cisco Unified Communications Operating System

You can change, not add, the host name for a server in the cluster.

1-63

alphabetic

alphanumeric

set network hostname

hostname

Command Line Interface

You can change, not add, the host name for a server in the cluster.

1-63

alphabetic

alphanumeric

Tip

The host name must follow the rules for ARPANET host names. Between
                                             			 the first and last character of the host name, you can enter alphanumeric
                                             			 characters and hyphens.

Before you configure the host name in any location, review the following information:

After you install the Unified Communications Manager publisher node, the host name for the publisher automatically
                                       				displays in this field. Before you install a Unified Communications Manager subscriber node, enter either the IP address or the host name for the
                                       				subscriber node in this field on the Unified Communications Manager publisher node.

In this field, configure a host name only if Unified Communications Manager can access the DNS server to resolve host names to IP
                                       				addresses; make sure that you configure the Cisco Unified Communications
                                       				Manager name and address information on the DNS server.

Tip

In addition to configuring Unified Communications Manager information on the DNS server, you enter DNS information during the Cisco
                                             			 Unified Communications Manager installation.

During the installation of a Unified Communications Manager subscriber node, you enter the hostname and IP address of the Unified Communications Manager publisher
                                       				node, so that Unified Communications Manager can verify network
                                       				connectivity and publisher-subscriber validation. Additionally, you must enter
                                       				the host name and the IP address for the subscriber node. When the Unified Communications Manager installation prompts you for the host name of
                                       				the subscriber server, enter the value that displays in the Server
                                       				Configuration window in Cisco Unified Communications Manager Administration;
                                       				that is, if you configured a host name for the subscriber server in the Host
                                       				Name/IP Address field.

### Procedure workflows

## Cisco Unified
                        	 Communications Manager Workflow

Change the IP address of a node

Change the hostname of a node

Task lists are provided for each of these procedures that summarize
                              		  the steps to perform.

You must complete all pre-change tasks and system health checks
                                          			 before you make these changes, and you must complete the post-change tasks
                                          			 after you make any of these changes.

## IM and Presence
                        	 Service Workflow

Change the IP address of a node

Change the hostname of a node

Change the DNS default domain name

Change the node name of a node

Task lists are provided for each of these procedures that summarize
                              		  the steps to perform.

You must complete all pre-change tasks and system health checks
                                          			 before you make these changes, and you must complete the post-change tasks
                                          			 after you make any of these changes.

## Pre-Change Tasks for Cisco Unified Communications
                        Manager Nodes

The following procedure explains the tasks to change the IP address and hostname for Cisco Unified Communications Manager nodes. You must perform these procedures during a scheduled maintenance window.

Caution

If you do not receive the results that you expect when you perform these tasks, do not continue until you have resolved the
                                          issue.

Step 1

If you have DNS configured anywhere on the Cisco Unified Communications Manager servers, ensure that forward and reverse records
                                       (for example, A record and PTR record) are configured and that the DNS is reachable and working.

Step 2

Check for any active ServerDown alerts to ensure that all servers in the cluster are up and available. Use either the Cisco
                                       Unified Real-Time Monitoring Tool (RTMT) or the command line interface (CLI) on the first node.

To check using Unified RTMT, access Alert Central and check for ServerDown alerts.

To check using the CLI on the first node, enter the following CLI command and inspect the application event log:

```
file search activelog syslog/CiscoSyslog ServerDown
```

For example output, see topics related to example database replication output. For detailed procedures and troubleshooting,
                                          see topics related to verifying database replication and troubleshooting database replication.

Step 3

Check the database replication status of all Cisco Unified Communications Manager nodes in the cluster to ensure that all
                                       servers are replicating database changes successfully. For IM and Presence Service, check the database replication status
                                       on the database publisher node using the CLI if you have more than one node in your deployment. Use either Unified RTMT or
                                       the CLI. All nodes should show a status of 2.

To check by using RTMT, access the Database Summary and inspect the replication status.

To check by using the CLI, enter utils dbreplication runtimestate .

Step 4

Enter the CLI command utils diagnose as shown in the following example to check network connectivity and DNS server configuration.

Example :

```
admin: utils diagnose module validate_network
Log file: /var/log/active/platform/log/diag1.log
Starting diagnostic test(s)
===========================
test - validate_network : Passed
Diagnostics Completed
admin:
```

Step 5

In Cisco Unified Reporting, generate the Unified CM Database Status report. Look for any errors or warnings in this report.

Step 6

In Cisco Unified Reporting, generate the Unified CM Cluster Overview report. Look for any errors or warnings in this report.

Step 7

From Cisco Unified Communications Manager Administration on the first node, select System > Server and click Find . A list of all servers in the cluster displays. Retain this list of servers for future reference. Ensure that you save an
                                       inventory of both the hostname and IP address of each node in your cluster.

Step 8

Run a manual Disaster Recovery System backup and ensure that all nodes and active services are backed up successfully. For
                                       more information, see the Administration Guide for Cisco Unified Communications Manager

Step 9

If you are changing the hostname, disable SAML single sign-on (SSO). For more information about SAML SSO, see the Deployment Guide for IM and Presence Service on Cisco Unified Communications Manager .

Step 10

For security-enabled clusters (Cluster Security Mode 1 - Mixed), update the Certificate Trust List (CTL) file. For detailed
                                       instructions on updating and managing the CTL file, including adding a new TFTP server to an existing CTL file, see the Cisco Unified Communications Manager Security Guide .

To avoid unnecessary delays, you must update the CTL file with the new IP address of your TFTP servers before you change the
                                                      IP address of the TFTP servers. If you do not perform this step, you will have to update all secure IP phones manually.

All IP phones that support security always download the CTL file, which includes the IP address of the TFTP servers with which
                                                      the phones are allowed to communicate. If you change the IP address of one or more TFTP servers, you must first add the new
                                                      IP addresses to the CTL file so that the phones can communicate with their TFTP server.

## Pre-Change Setup Tasks for IM and Presence Service Nodes

Perform the applicable pre-change setup tasks to ensure that your system is prepared for a successful IP address, hostname,
                              domain, or node name change. You must perform these tasks during a scheduled maintenance window.

Caution

If you do not receive the results that you expect when you perform these tasks, do not continue until you have resolved the
                                          issue.

You do not need to perform the steps to verify that the Cisco AXL Web service and the IM and Presence Cisco Sync Agent services
                                          are started unless you are changing the domain name or the node name. See the pre-change task list for a complete list of
                                          the tasks to perform.

Step 1

Check the database replication status on all nodes in the cluster to ensure that all servers are replicating database changes
                                       successfully.

For IM and Presence Service , check the database replication status on the database publisher node using the CLI if you have more than one node in your
                                          deployment.

Use either Unified RTMT or the CLI. All nodes should show a status of 2 .

To check by using RTMT, access the Database Summary and inspect the replication status.

To check by using the CLI, enter utils dbreplication runtimestate .

Step 2

Enter the CLI command utils diagnose as shown in the following example to check network connectivity and DNS server configuration.

### Example:

```
admin: utils diagnose module validate_network
Log file: /var/log/active/platform/log/diag1.log

Starting diagnostic test(s)
===========================
test - validate_network    : Passed                      

Diagnostics Completed
admin:
```

Step 3

Run a manual Disaster Recovery System backup and ensure that all nodes and active services are backed up successfully.

For more information, see the Administration Guide for Cisco Unified Communications Manager .

Step 4

Disable High Availability (HA) on all presence redundancy groups. For information on Presence Redundancy Groups configuration, see the "Configure Presence Redundancy Groups" chapter in the System Configuration Guide for Cisco Unified Communications Manager .

Before you disable HA, take a record of the number of users in each node and subcluster. You can find this information in
                                                            the System > Presence Topology window of Cisco Unified CM IM and Presence Administration.

After you disable HA, wait at least 2 minutes for the settings to sync across the cluster before completing any further changes.

Step 5

If you are changing the hostname, disable SAML single sign-on (SSO). For more information about SAML SSO, see the Deployment Guide for IM and Presence Service on Cisco Unified Communications Manager .

Step 6

Compile a list of all services that are currently activated. Retain these lists for future reference.

To view the list of activated network services using Cisco Unified Serviceability, select Tools > Control Center - Network Services .

To view the list of activated feature services using Cisco Unified Serviceability, select Tools > Control Center - Feature Services .

Step 7

Stop all feature services using Cisco Unified Serviceability, select Tools > Control Center - Feature Services . The order in which you stop feature services is not important.

Tip

You do not need to complete this step if you are changing the IP address, hostname, or both the IP address and hostname. Feature
                                                      services are automatically stopped for these name changes.

Step 8

Stop the following network services that are listed under the IM and Presence Service services group using Cisco Unified Serviceability when you select Tools > Control Center - Network Services .

- Cisco Config Agent

- Cisco Intercluster Sync Agent

- Cisco Client Profile Agent

- Cisco OAM Agent

- Cisco XCP Config Manager

- Cisco XCP Router

- Cisco Presence Datastore

- Cisco SIP Registration Datastore

- Cisco Login Datastore

- Cisco Route Datastore

- Cisco Server Recovery Manager

- Cisco IM and Presence Data Monitor

Step 9

Verify that the Cisco AXL Web Service is started on the Cisco Unified Communications Manager publisher node using Cisco Unified Serviceability, Tools > Control Center - Feature Services .

Perform this step only if you are changing the domain name or node name.

Step 10

Verify that the IM and Presence Cisco Sync Agent service has started and that synchronization is complete.

Perform this step only if you are changing the domain name or node name.

To verify using Cisco Unified Serviceability, perform the following steps:

Select Tools > Control Center - Network Services .

Select the IM and Presence database publisher node.

Select IM and Presence Service Services .

Verify that the Cisco Sync Agent service has started.

From the Cisco Unified CM IM and Presence Administration GUI, select Diagnostics > System Dashboard > Sync Status .

Verify that synchronization is complete and that no errors display in the synchronization status area.

To verify using the Cisco Unified CM IM and Presence Administration GUI on the IM and Presence database publisher node, select Diagnostics > System Dashboard .

| Note | All Unified Communications products such as Cisco Unified Communications Manager, Cisco Unity Connections, and Cisco IM and
                                       Presence, and so on, have only one interface. Thus, you can assign only one IP address for each of these products. |
|---|---|

| Host Name Location | Allowed Configuration | Allowed Number of Characters | Recommended First Character for Host Name | Recommended Last Character for Host Name |
|---|---|---|---|---|
| Host Name/ IP Address field System > Server in Cisco Unified Communications Manager Administration | You can add or change the host name for a server in the cluster. | 2-63 | alphabetic | alphanumeric |
| Hostname field Cisco Unified Communications Manager installation wizard | You can add the host name for a server in the cluster. | 1-63 | alphabetic | alphanumeric |
| Hostname field Settings > IP > Ethernet in Cisco Unified Communications Operating System | You can change, not add, the host name for a server in the cluster. | 1-63 | alphabetic | alphanumeric |
| set network hostname hostname Command Line Interface | You can change, not add, the host name for a server in the cluster. | 1-63 | alphabetic | alphanumeric |

| Tip | The host name must follow the rules for ARPANET host names. Between
                                             			 the first and last character of the host name, you can enter alphanumeric
                                             			 characters and hyphens. |
|---|---|

| Tip | In addition to configuring Unified Communications Manager information on the DNS server, you enter DNS information during the Cisco
                                             			 Unified Communications Manager installation. |
|---|---|

| Note | You must complete all pre-change tasks and system health checks
                                          			 before you make these changes, and you must complete the post-change tasks
                                          			 after you make any of these changes. |
|---|---|

| Note | You must complete all pre-change tasks and system health checks
                                          			 before you make these changes, and you must complete the post-change tasks
                                          			 after you make any of these changes. |
|---|---|

| Caution | If you do not receive the results that you expect when you perform these tasks, do not continue until you have resolved the
                                          issue. |
|---|---|

| Step 1 | If you have DNS configured anywhere on the Cisco Unified Communications Manager servers, ensure that forward and reverse records
                                       (for example, A record and PTR record) are configured and that the DNS is reachable and working. |
|---|---|
| Step 2 | Check for any active ServerDown alerts to ensure that all servers in the cluster are up and available. Use either the Cisco
                                       Unified Real-Time Monitoring Tool (RTMT) or the command line interface (CLI) on the first node. To check using Unified RTMT, access Alert Central and check for ServerDown alerts. To check using the CLI on the first node, enter the following CLI command and inspect the application event log: file search activelog syslog/CiscoSyslog ServerDown For example output, see topics related to example database replication output. For detailed procedures and troubleshooting,
                                          see topics related to verifying database replication and troubleshooting database replication. |
| Step 3 | Check the database replication status of all Cisco Unified Communications Manager nodes in the cluster to ensure that all
                                       servers are replicating database changes successfully. For IM and Presence Service, check the database replication status
                                       on the database publisher node using the CLI if you have more than one node in your deployment. Use either Unified RTMT or
                                       the CLI. All nodes should show a status of 2. To check by using RTMT, access the Database Summary and inspect the replication status. To check by using the CLI, enter utils dbreplication runtimestate . |
| Step 4 | Enter the CLI command utils diagnose as shown in the following example to check network connectivity and DNS server configuration. Example : admin: utils diagnose module validate_network
Log file: /var/log/active/platform/log/diag1.log
Starting diagnostic test(s)
===========================
test - validate_network : Passed
Diagnostics Completed
admin: |
| Step 5 | In Cisco Unified Reporting, generate the Unified CM Database Status report. Look for any errors or warnings in this report. |
| Step 6 | In Cisco Unified Reporting, generate the Unified CM Cluster Overview report. Look for any errors or warnings in this report. |
| Step 7 | From Cisco Unified Communications Manager Administration on the first node, select System > Server and click Find . A list of all servers in the cluster displays. Retain this list of servers for future reference. Ensure that you save an
                                       inventory of both the hostname and IP address of each node in your cluster. |
| Step 8 | Run a manual Disaster Recovery System backup and ensure that all nodes and active services are backed up successfully. For
                                       more information, see the Administration Guide for Cisco Unified Communications Manager |
| Step 9 | If you are changing the hostname, disable SAML single sign-on (SSO). For more information about SAML SSO, see the Deployment Guide for IM and Presence Service on Cisco Unified Communications Manager . |
| Step 10 | For security-enabled clusters (Cluster Security Mode 1 - Mixed), update the Certificate Trust List (CTL) file. For detailed
                                       instructions on updating and managing the CTL file, including adding a new TFTP server to an existing CTL file, see the Cisco Unified Communications Manager Security Guide . Note To avoid unnecessary delays, you must update the CTL file with the new IP address of your TFTP servers before you change the
                                                      IP address of the TFTP servers. If you do not perform this step, you will have to update all secure IP phones manually. Note All IP phones that support security always download the CTL file, which includes the IP address of the TFTP servers with which
                                                      the phones are allowed to communicate. If you change the IP address of one or more TFTP servers, you must first add the new
                                                      IP addresses to the CTL file so that the phones can communicate with their TFTP server. | Note | To avoid unnecessary delays, you must update the CTL file with the new IP address of your TFTP servers before you change the
                                                      IP address of the TFTP servers. If you do not perform this step, you will have to update all secure IP phones manually. | Note | All IP phones that support security always download the CTL file, which includes the IP address of the TFTP servers with which
                                                      the phones are allowed to communicate. If you change the IP address of one or more TFTP servers, you must first add the new
                                                      IP addresses to the CTL file so that the phones can communicate with their TFTP server. |
| Note | To avoid unnecessary delays, you must update the CTL file with the new IP address of your TFTP servers before you change the
                                                      IP address of the TFTP servers. If you do not perform this step, you will have to update all secure IP phones manually. |
| Note | All IP phones that support security always download the CTL file, which includes the IP address of the TFTP servers with which
                                                      the phones are allowed to communicate. If you change the IP address of one or more TFTP servers, you must first add the new
                                                      IP addresses to the CTL file so that the phones can communicate with their TFTP server. |

| Note | To avoid unnecessary delays, you must update the CTL file with the new IP address of your TFTP servers before you change the
                                                      IP address of the TFTP servers. If you do not perform this step, you will have to update all secure IP phones manually. |
|---|---|

| Note | All IP phones that support security always download the CTL file, which includes the IP address of the TFTP servers with which
                                                      the phones are allowed to communicate. If you change the IP address of one or more TFTP servers, you must first add the new
                                                      IP addresses to the CTL file so that the phones can communicate with their TFTP server. |
|---|---|

| Caution | If you do not receive the results that you expect when you perform these tasks, do not continue until you have resolved the
                                          issue. |
|---|---|

| Note | You do not need to perform the steps to verify that the Cisco AXL Web service and the IM and Presence Cisco Sync Agent services
                                          are started unless you are changing the domain name or the node name. See the pre-change task list for a complete list of
                                          the tasks to perform. |
|---|---|

| Step 1 | Check the database replication status on all nodes in the cluster to ensure that all servers are replicating database changes
                                       successfully. For IM and Presence Service , check the database replication status on the database publisher node using the CLI if you have more than one node in your
                                          deployment. Use either Unified RTMT or the CLI. All nodes should show a status of 2 . To check by using RTMT, access the Database Summary and inspect the replication status. To check by using the CLI, enter utils dbreplication runtimestate . For example output, see topics related to example database replication output. For detailed procedures and troubleshooting,
                                             see topics related to verifying database replication and troubleshooting database replication. |
|---|---|
| Step 2 | Enter the CLI command utils diagnose as shown in the following example to check network connectivity and DNS server configuration. Example: admin: utils diagnose module validate_network
Log file: /var/log/active/platform/log/diag1.log

Starting diagnostic test(s)
===========================
test - validate_network    : Passed                      

Diagnostics Completed
admin: |
| Step 3 | Run a manual Disaster Recovery System backup and ensure that all nodes and active services are backed up successfully. For more information, see the Administration Guide for Cisco Unified Communications Manager . |
| Step 4 | Disable High Availability (HA) on all presence redundancy groups. For information on Presence Redundancy Groups configuration, see the "Configure Presence Redundancy Groups" chapter in the System Configuration Guide for Cisco Unified Communications Manager . Note Before you disable HA, take a record of the number of users in each node and subcluster. You can find this information in
                                                            the System > Presence Topology window of Cisco Unified CM IM and Presence Administration. After you disable HA, wait at least 2 minutes for the settings to sync across the cluster before completing any further changes. | Note | Before you disable HA, take a record of the number of users in each node and subcluster. You can find this information in
                                                            the System > Presence Topology window of Cisco Unified CM IM and Presence Administration. After you disable HA, wait at least 2 minutes for the settings to sync across the cluster before completing any further changes. |
| Note | Before you disable HA, take a record of the number of users in each node and subcluster. You can find this information in
                                                            the System > Presence Topology window of Cisco Unified CM IM and Presence Administration. After you disable HA, wait at least 2 minutes for the settings to sync across the cluster before completing any further changes. |
| Step 5 | If you are changing the hostname, disable SAML single sign-on (SSO). For more information about SAML SSO, see the Deployment Guide for IM and Presence Service on Cisco Unified Communications Manager . |
| Step 6 | Compile a list of all services that are currently activated. Retain these lists for future reference. To view the list of activated network services using Cisco Unified Serviceability, select Tools > Control Center - Network Services . To view the list of activated feature services using Cisco Unified Serviceability, select Tools > Control Center - Feature Services . |
| Step 7 | Stop all feature services using Cisco Unified Serviceability, select Tools > Control Center - Feature Services . The order in which you stop feature services is not important. Tip You do not need to complete this step if you are changing the IP address, hostname, or both the IP address and hostname. Feature
                                                      services are automatically stopped for these name changes. | Tip | You do not need to complete this step if you are changing the IP address, hostname, or both the IP address and hostname. Feature
                                                      services are automatically stopped for these name changes. |
| Tip | You do not need to complete this step if you are changing the IP address, hostname, or both the IP address and hostname. Feature
                                                      services are automatically stopped for these name changes. |
| Step 8 | Stop the following network services that are listed under the IM and Presence Service services group using Cisco Unified Serviceability when you select Tools > Control Center - Network Services . You must stop these IM and Presence Service network services in the following order: Cisco Config Agent Cisco Intercluster Sync Agent Cisco Client Profile Agent Cisco OAM Agent Cisco XCP Config Manager Cisco XCP Router Cisco Presence Datastore Cisco SIP Registration Datastore Cisco Login Datastore Cisco Route Datastore Cisco Server Recovery Manager Cisco IM and Presence Data Monitor |
| Step 9 | Verify that the Cisco AXL Web Service is started on the Cisco Unified Communications Manager publisher node using Cisco Unified Serviceability, Tools > Control Center - Feature Services . Note Perform this step only if you are changing the domain name or node name. | Note | Perform this step only if you are changing the domain name or node name. |
| Note | Perform this step only if you are changing the domain name or node name. |
| Step 10 | Verify that the IM and Presence Cisco Sync Agent service has started and that synchronization is complete. Note Perform this step only if you are changing the domain name or node name. To verify using Cisco Unified Serviceability, perform the following steps: Select Tools > Control Center - Network Services . Select the IM and Presence database publisher node. Select IM and Presence Service Services . Verify that the Cisco Sync Agent service has started. From the Cisco Unified CM IM and Presence Administration GUI, select Diagnostics > System Dashboard > Sync Status . Verify that synchronization is complete and that no errors display in the synchronization status area. To verify using the Cisco Unified CM IM and Presence Administration GUI on the IM and Presence database publisher node, select Diagnostics > System Dashboard . | Note | Perform this step only if you are changing the domain name or node name. |
| Note | Perform this step only if you are changing the domain name or node name. |

| Note | Before you disable HA, take a record of the number of users in each node and subcluster. You can find this information in
                                                            the System > Presence Topology window of Cisco Unified CM IM and Presence Administration. After you disable HA, wait at least 2 minutes for the settings to sync across the cluster before completing any further changes. |
|---|---|

| Tip | You do not need to complete this step if you are changing the IP address, hostname, or both the IP address and hostname. Feature
                                                      services are automatically stopped for these name changes. |
|---|---|

| Note | Perform this step only if you are changing the domain name or node name. |
|---|---|

| Note | Perform this step only if you are changing the domain name or node name. |
|---|---|