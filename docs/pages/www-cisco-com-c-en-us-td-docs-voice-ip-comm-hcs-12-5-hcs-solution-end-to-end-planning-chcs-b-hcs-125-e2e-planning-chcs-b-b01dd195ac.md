---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-end-to-end-planning-chcs-b-hcs-125-e2e-planning-chcs-b-b01dd195ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/End_to_End_Planning/chcs_b_hcs-125-e2e-planning/chcs_b_hcs-125-e2e-planning_chapter_0110.html
retrieved_at: 2026-09-01T20:56:52.228809+00:00
---

Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

# Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

Updated: June 25, 2019

Chapter: Service Fulfillment Planning

## Chapter: Service Fulfillment Planning

# Service Fulfillment Planning

## Prerequisites

Before you plan
                           		Service Fulfillment for your Cisco HCS installation, make sure that you:

## Service
                        	 Fulfillment Workflow

## HCM-F Deployment
                        	 Models

Default
                                    			 Deployment

Node 1: SDR + Core HCM-F applications

- SBI (apps + dm) direct access

Node 1: SDR
                                          				  + Core HCM-F applications (App Node)

- HCM-F API access directly
                                       				to NBI-WS

- Node 1: SDR + Core HCM-F
                                       				applications

- Load Balancer

## Service Inventory Planning Considerations

Service Inventory is a Cisco HCM-F service that queries Cisco Unified Communications Domain Manager daily. It reports detailed configurations of customers, subscribers, and devices for all Unified Communications Manager and
                              Cisco Unity Connection application instances. The Service Inventory report also provides a summary of all customers, UC clusters,
                              users, and end devices deployed within HCS.

Complete the
                              		  following steps when planning service inventory:

Plan to deploy
                                       			 an SFTP server (and an optional backup SFTP server) with adequate capacity to
                                       			 receive Service Inventory report files. A typical compressed file size would be
                                       			 8-10 MB for 200,000 users.

Decide whether the files will be pushed, or pulled, scheduled, or automatic.

Decide which application can be used to parse the detailed inventory data into a form that can be used by your business system.

## Platform Manager
                        	 Planning Considerations

Platform Manager is a Cisco Hosted Collaboration Mediation Fulfillment service that allows you to schedule and monitor the
                              automated installation, upgrade, restart, and backup of multiple application instances across customers for the following
                              applications:

Cisco Unified Communications Manager

Cisco Unity Connection

Cisco Unified Presence / Cisco Unified IM and Presence

Take the following
                              		  actions for Platform Manager planning as you onboard each customer or cluster:

Determine the number of server groups needed.

Select server groups for backup tasks that avoid overloading blade hardware or I/O bandwidth to data storage LUNs.

Put all servers (for example, Publishers) on a specific ESXi-Host or blade into a common server group. This way the backup
                                    of the servers on the host is done serially, minimizing the backup CPU load on the host.

Spread the SFTP servers that are assigned to backup groups across different storage LUNs so that backup transfer load is spread
                                    out.

Ensure that no more than two applications are backed up on a specific blade at any one time.

For details on Platform Manager, see the Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide, Release 12.5 .

### Limitations and restrictions

The following list describes the current limitations for Platform Manager.

Platform Manager is not a diagnostic tool. An error message does appear on the task list page if a task fails; however, you
                                    should use your usual set of tools and procedures to diagnose and correct the problem.

The SOAP services do not replace the existing OS Administration and CLI upgrade processes.

#### Servers
                              	 functionality classification

Platform
                                 		Manager offers a wide range of different user-defined servers types to
                                 		accommodate the management of potentially thousands of servers. You can tag
                                 		servers with one or more roles such as publisher, subscriber, TFTP, music on
                                 		hold, secondary TFTP, secondary music on hold to help classify the different
                                 		servers in your system. You can then tag your servers with one or more server
                                 		roles for easier identification. Server roles allow you to classify each server
                                 		in your Platform Manager, making your task creation and viewing more efficient.

Server roles
                                 		include:

Call Processing

Backup Call
                                       			 Processing

Music on Hold

TFTP

Backup TFTP

Primary Presence

Secondary Presence

Primary Voicemail

Secondary
                                       			 Voicemail

Server roles are
                                             		  labels to help users identify a server. Setting a server role does not activate
                                             		  any services. Mislabeling a server does not cause any service outages.

#### Server group usage

Server groups allow you to logically join together different servers that you want to perform tasks on as a group. You have
                                 the flexibility to group servers to accommodate the varied requests for installation, backup, upgrades and restart tasks.

A task is applied to all servers under the same server group. If you do not want to lose a service, do not put your Active
                                             Call Control server in the same server group as its backup when you run a switch version or reboot task.

Server groups allow you to logically combine various servers; for example, you can create server groups for the following
                                 areas:

Server Group by Role - Create call processing server groups and a backup processing server group.

Server Group by Product - Create product A and product B groups.

Server Group by Customer and Product - Create customer A-product A and customer A-product B groups.

You can have as many servers as you like in a group; however, all servers must be of the same product type. A server can be
                                             a member of more than one group.

##### Limitation in server groups

The following limitations apply when you create server groups:

You cannot have multiple products in the same server group. For example, if you have a customer that has Cisco Unified Communications
                                          Manager and Cisco Unified Communications Manager IM and Presence Service, you must create two groups for this customer.

You cannot have publisher servers in the same group as subscriber servers if you want to run upgrade or switch version tasks
                                          on the group. For example, if you want to upgrade all of a customer’s services, you must create at least two groups: a publisher
                                          server group and at least one subscriber server group to execute the task on the publisher servers before the subscriber servers.
                                          This does not apply to restart server tasks. Publishers and subscribers can be in the same group if that group is used for
                                          restart server task.

#### Task
                              	 creation

Tasks are the main function of Platform Manager. For example, you may want your publisher servers to back up your subscriber
                                 servers within a certain application group. The create tasks pages can help you with this.

The Backup Schedule
                                 		task feature provides a central location to schedule and monitor backups while
                                 		reusing of the existing backup infrastructure-the Disaster Recovery System.
                                 		This feature also enables backup load balancing.

#### Data filtering

Platform Manager has a powerful filtering capabilities to
                                    		  allow you to view specific information. The following pages have filter options
                                    		  available:

Servers

Server Groups

Task List

Field

Description

Quick Filter

View the data by any column on the page. For
                                                						example, if you want to only see a specific customer servers, you can filter on
                                                						a customer name. If you want to see all of your Unified Communications Manager servers, you can
                                                						filter on product and only your Unified Communications Manager servers appear.

Advanced Filter

View data by multiple columns and multiple terms
                                                						in the same column. For example, perhaps you want to see all the Unified Communications Manager and
                                                						Cisco Unified Presence server groups for customer A and customer B. Add all of
                                                						the details in the search boxes and your results appear.

Set Default Filter

Set a default view for your content. For example,
                                                						you may want the Quick Filter screen to be the default view on the servers page
                                                						to it does not have to load all of servers every time to you go the page.

### Best
                           	 practices

The
                              		following are recommendations for configuring your systems as suggested by
                              		Cisco development and testing teams.

Use the SDR Synchronization, the Server Import functionality, or the VCenter Sync operation to populate the servers in your
                                    system if possible.

You can perform the VCenter Sync operation through a manual sync request from the Administration menu, or by enabling vCenter Sync from the Data Center Management menu.

Ensure that the cluster applications are associated with the correct VMs in the Cluster Applications page of Application Management menu. For more information, see the Configure HCMF section in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide

Create groups with multiple servers that you perform similar tasks on.

When you name groups, keep the terminology simple and use easy-to-recognize names.

Use the sequencing feature in a task when you want a second group of servers to wait until the first group is done before
                                    performing that task.

Use the Backup Schedule task for a more efficient and powerful way to run backups. It helps to control multiple servers that
                                    are backed up at the same time and enables load balancing. SFTP servers for DRS backup are configured in Disaster Recovery
                                    System (DRS). All the first nodes that use the same SFTP server should be assigned to the same server group for backup, or
                                    should be scheduled for backups on different days of the week.

For more information, refer to the HCS Maintain and Operate Guide at http://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html .

## Prime
                        	 Collaboration Deployment for UC Applications

Cisco Prime Collaboration Deployment helps you to manage Unified Communications (UC) applications. Its functions are to:

Migrate a cluster of UC servers to a new cluster (such as MCS to virtual, or virtual to virtual).

Cisco Prime Collaboration Deployment does not delete the source cluster VMs after migration is complete. You can fail over
                                             to the source VMs if there is a problem with the new VMs. When you are satisfied with the migration, you can manually delete
                                             the source VMs.

Perform operations on clusters, such as:

Upgrade

Switch version

Restart

Fresh install a new release UC cluster

Change IP addresses or hostnames in clusters (for a network migration).

Cisco Prime Collaboration Deployment supports simple migration and network migration. Changing IP addresses or hostnames
                                 is not required for a simple migration. For more information, see the Prime Collaboration Deployment Guide .

The functions that are supported by the Cisco Prime Collaboration Deployment can be found in the Prime Collaboration Deployment Administration Guide .

Use the Cluster
                              		  Discovery feature to find application clusters on which to perform
                           		fresh installs, migration, and upgrade functions. Perform this discovery on a
                           		blade-by-blade basis.

For more information about features, installation, configuration and administration, best practices, and troubleshooting,
                           see the following documents:

Prime Collaboration Deployment Administration Guide

Release Notes for Cisco Prime Collaboration Deployment

## Compatibility Considerations

See the Service Fulfillment compatibility table in the Cisco Hosted Collaboration
                                 			 Solution Compatibility Matrix .

## Call Detail
                        	 Records

Service Providers
                           		(SPs) can use Usage-based billing, using call detail records (CDRs) or Call
                           		Manager Management Records (CMRs) for the enterprise.

If a service provider is interested in usage type billing, they can direct CDRs from Unified Communications Manager to their
                           billing system. If Cisco Prime Collaboration Assurance is configured as a management application, the Cisco HCS CAA CUCM Service
                           configures any CUCM (release 9.0(1) or higher) to send CDRs to Cisco Prime Collaboration Assurance. The option also exists
                           to work with our third-party vendor to consume CDRs and CMRs to produce necessary billing information or invoices.

Cisco Prime
                                       		  Collaboration Assurance uses CDR and CMR for diagnostic purpose only (not for
                                       		  billing).

The Cisco
                           		TelePresence Exchange System collects and displays call detail records (CDRs)
                           		for calls that are placed on the system. From the administration console, you
                           		can view CDR details for the system and export a comma-separated value (.csv)
                           		file of that information.

The Cisco
                           		TelePresence Exchange System retains CDRs for up to 30 days from the recorded
                           		end time of the CDR. The system automatically purges CDRs that exceed this
                           		30-day limit. If the total number of CDRs retained by the system reaches
                           		100,000, the system retains only the most recent 100,000 records and
                           		automatically purges the rest.

The Cisco
                           		TelePresence Exchange System also provides an Application Programming Interface
                           		(API) for managing and retrieving call records. For more details, see the API User Guide
                              		  for the Cisco TelePresence Exchange System .

## LDAP Integration
                        	 Considerations

If you intend to integrate LDAP users into Cisco Unified Communications Domain Manager ,
                           		you need to identify the LDAP servers that will be used. LDAP servers can be
                           		integrated at the provider, reseller, customer, or site level in Cisco Unified Communications Domain Manager .
                           		The User Distinguished Name and Base Distinguished Name for LDAP search must be
                           		identified for LDAP servers being integrated.

## Single Sign On
                        	 Considerations

If you intend to
                           		deploy Single Sign On (SSO) in Cisco Unified Communications Domain Manager ,
                           		you need to identify the Identity Provider (IdP) servers that will be used.
                           		IdPs can be located at the provider, reseller, or customer levels in Cisco Unified Communications Domain Manager .
                           		You will need to be able to upload Service Provider metadata to the IdP and
                           		also download IdP metadata.

## Cisco Unified
                        	 Communications Domain Manager Planning Considerations

Cisco Unified Communications Domain Manager is an integral part of the service fulfillment subsystem. It is primarily responsible
                              for the configuration and registration of users, subscribers, and endpoints with the back-end Cisco Unified Communications
                              Manager, Cisco Unity Connection, and IM and Presence Service servers. Cisco Unified Communications Domain Manager  provides
                              the day-to-day service and device provisioning and management tools. One instance supports all deployment sizes up to 200,000
                              subscribers.

Consider the steps in the following procedure for Cisco Unified Communications Domain Manager planning:

Determine if Webex and Contact Center will be integrated.

Cisco Unified Communications Domain Manager is deployed either as a single node, or a cluster of multiple nodes with High Availability (HA) and/or Disaster Recovery
                                       (DR) qualities. Each node can be assigned one or more of the following functional roles:

WebProxy – load balancing across multiple application roles

Application – transactional business logic

Database – persistent storage of data

The following combined roles are defined:

Standalone – combines the Application and Database roles for use in a non-clustered environment

Unified – similar to the Standalone role combining Application and Database roles, but clustered with other nodes to provide
                                                HA and DR capabilities.

Determine which dial plan to use. See Cisco Hosted Collaboration Solution End-to-End Planning Guide .

For user activations, decide if you will use automated system activations based on system inventory or the Cisco Unified Communications Domain Manager admin interface.

Decide if you want to use the Cisco Unified Communications Domain Manager user self service portal. If yes, you should allow
                                       access for customers or end-users.

Check to see what the static deployment requirements are on Cisco Unified Communications Manager clusters before managing
                                       a cluster from Cisco Unified Communications Domain Manager. Gather the following information:

Location of the Cisco Unified Communications Domain Manager

Determine latency between Cisco Unified Communications Domain Manager and UC applications, which must be within defined limits.
                                             The maximum supported latency is 200-ms Round Trip Time (RTT).

Determine
                                       			 if additional languages are required for the system other than English.

Determine
                                       			 if custom branding is desired.

## Cisco Unified Communications Domain Manager Resource Requirements

The following table lists the resource requirements for the listed service fulfillment components.

20 GB for OS

50 GB for application

10 GB for logs

50 GB for compressed backups

250 GB for database

150 GB

565 (web server)

The Database
                           		storage partition is sized at the initial installation to support the maximum
                           		deployment size for the release. Further increase in the size of the partition
                           		is not required as new customers are on-boarded.

To set up the disk requirements, the disk has to be set up on the VMWare GUI Resources tab where a disk can be created. This task can be done after the OVA import but prior to the system boots.

|  |
|---|

| Note | Service Inventory pulls customer information from the Cisco Unified Communications Domain Manager , and generates a report file (or files) for all the customers. |
|---|---|

| Step 1 | Plan to deploy
                                       			 an SFTP server (and an optional backup SFTP server) with adequate capacity to
                                       			 receive Service Inventory report files. A typical compressed file size would be
                                       			 8-10 MB for 200,000 users. |
|---|---|
| Step 2 | Decide whether the files will be pushed, or pulled, scheduled, or automatic. |
| Step 3 | Decide which application can be used to parse the detailed inventory data into a form that can be used by your business system. For more details on Service Inventory reports and their formatting, see Cisco Hosted Collaboration Mediation Fulfillment Maintain and Operate Guide . |

| Note | Server roles are
                                             		  labels to help users identify a server. Setting a server role does not activate
                                             		  any services. Mislabeling a server does not cause any service outages. |
|---|---|

| Note | A task is applied to all servers under the same server group. If you do not want to lose a service, do not put your Active
                                             Call Control server in the same server group as its backup when you run a switch version or reboot task. |
|---|---|

| Note | You can have as many servers as you like in a group; however, all servers must be of the same product type. A server can be
                                             a member of more than one group. |
|---|---|

| Field | Description |
|---|---|
| Quick Filter | View the data by any column on the page. For
                                                						example, if you want to only see a specific customer servers, you can filter on
                                                						a customer name. If you want to see all of your Unified Communications Manager servers, you can
                                                						filter on product and only your Unified Communications Manager servers appear. |
| Advanced Filter | View data by multiple columns and multiple terms
                                                						in the same column. For example, perhaps you want to see all the Unified Communications Manager and
                                                						Cisco Unified Presence server groups for customer A and customer B. Add all of
                                                						the details in the search boxes and your results appear. |
| Set Default Filter | Set a default view for your content. For example,
                                                						you may want the Quick Filter screen to be the default view on the servers page
                                                						to it does not have to load all of servers every time to you go the page. |

| Note | Ensure that the cluster applications are associated with the correct VMs in the Cluster Applications page of Application Management menu. For more information, see the Configure HCMF section in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide . |
|---|---|

| Tip | Cisco Prime Collaboration Deployment does not delete the source cluster VMs after migration is complete. You can fail over
                                             to the source VMs if there is a problem with the new VMs. When you are satisfied with the migration, you can manually delete
                                             the source VMs. |
|---|---|

| Note | Cisco Prime
                                       		  Collaboration Assurance uses CDR and CMR for diagnostic purpose only (not for
                                       		  billing). |
|---|---|

| Step 1 | Determine if Webex and Contact Center will be integrated. |
|---|---|
| Step 2 | Cisco Unified Communications Domain Manager is deployed either as a single node, or a cluster of multiple nodes with High Availability (HA) and/or Disaster Recovery
                                       (DR) qualities. Each node can be assigned one or more of the following functional roles: WebProxy – load balancing across multiple application roles Application – transactional business logic Database – persistent storage of data The following combined roles are defined: Standalone – combines the Application and Database roles for use in a non-clustered environment Unified – similar to the Standalone role combining Application and Database roles, but clustered with other nodes to provide
                                                HA and DR capabilities. |
| Step 3 | Determine which dial plan to use. See Cisco Hosted Collaboration Solution End-to-End Planning Guide . |
| Step 4 | For user activations, decide if you will use automated system activations based on system inventory or the Cisco Unified Communications Domain Manager admin interface. |
| Step 5 | Decide if you want to use the Cisco Unified Communications Domain Manager user self service portal. If yes, you should allow
                                       access for customers or end-users. |
| Step 6 | Check to see what the static deployment requirements are on Cisco Unified Communications Manager clusters before managing
                                       a cluster from Cisco Unified Communications Domain Manager. Gather the following information: Location of the Cisco Unified Communications Domain Manager Determine latency between Cisco Unified Communications Domain Manager and UC applications, which must be within defined limits.
                                             The maximum supported latency is 200-ms Round Trip Time (RTT). Note A higher latency (e.g. 250-ms RTT) may work in certain instances, but this must be tested prior to deployment. | Note | A higher latency (e.g. 250-ms RTT) may work in certain instances, but this must be tested prior to deployment. |
| Note | A higher latency (e.g. 250-ms RTT) may work in certain instances, but this must be tested prior to deployment. |
| Step 7 | Determine
                                       			 if additional languages are required for the system other than English. |
| Step 8 | Determine
                                       			 if custom branding is desired. |

| Note | A higher latency (e.g. 250-ms RTT) may work in certain instances, but this must be tested prior to deployment. |
|---|---|

| HCS 11.5(x)/12.5(x) |
|---|
| Fulfillment component | vCPU | RAM (GB) | Storage | IOPS | OS |
| Unified CDM Multi-node | 4 vCPU @ 2 GHz | 8 GB | 370 GB partitioned as follows: 20 GB for OS 50 GB for application 10 GB for logs 50 GB for compressed backups 250 GB for database | 300 |  |
| WebProxy Nodes | 2 vCPU @ 2 GHz | 4 GB | 150 GB |  |  |
| HCM-F | 4 x 1.8 GHz | 16 (Res) | 80 | 200 |  |
| PLM | 1 vCPU x 1.8 GHz | 4 | 50 | - |  |
| CCDM | 8 | 32 | 100 | 775 (DB server) 565 (web server) | Microsoft Windows |