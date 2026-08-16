---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-install-15-cucm-b-install-guide-cucm-imp-15-cucm-m-planning-the-install-6ba0def366
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/install/15/cucm_b_install-guide-cucm-imp-15/cucm_m_planning-the-installation.html
retrieved_at: 2026-08-16T17:50:21.183870+00:00
---

Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 and SUs

# Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 and SUs

Updated: March 17, 2026

Chapter: Planning the Installation

## Chapter: Planning the Installation

# Planning the Installation

## Topology Options

This section
                              		  provides an overview of the system topology and describes the relationship
                              		  between the types of nodes in the topology.

### Clusters

Clusters provide a mechanism for distributing call processing, presence status, and database replication across multiple servers
                              for scalability and redundancy. They provide transparent sharing of resources and features, and enable system scalability.

A cluster comprises a set of Unified Communications Manager nodes and/or IM and Presence nodes that run compatible software versions.

If you are deploying the IM and Presence Service, you must decide before you begin the installation whether you want a Standard
                              Deployment (IM and Presence Service on Unified Communications Manager) or an IM and Presence Centralized Cluster Deployment.
                              Both deployment options require sizing the IM and Presence Service cluster(s) for all presence users across all telephony
                              clusters in the deployment.

IM and Presence Deployment

Description

Standard Deployment (de-centralized/distributed) )

The IM and Presence Service and Unified Communications Manager cluster nodes are part of the same cluster. The IM and Presence
                                          cluster shares a platform and many of the same services as the telephony cluster. Each cluster will have nodes of both. This
                                          option requires a 1x1 mapping of Unified CM telephony clusters to IM and Presence clusters.

Basic installations order followed is same as mentioned in the Attended Install method. For more information, see the "Installation
                                          Methods".

For touchless installations, you can install all Unified Communications Manager and IM and Presence Service cluster nodes
                                          concurrently in a single process.

IM and Presence Centralized Cluster Deployment

A single IM and Presence Service central cluster is installed separately from your Unified Communications Manager telephony
                                          cluster(s) and may be located on different hardware servers. The single IM and Presence Service cluster maps to all Unified
                                          Communications Manager telephony clusters. This allows you to scale your telephony deployment and IM and Presence deployment
                                          separately.

For basic installations:

Install a local Unified Communications Manager publisher node in the central IM and Presence Service cluster. This node is
                                                not a part of your telephony deployment. The node handles functions like database and user provisioning for the central cluster.

Install the IM and Presence Service database publisher node.

Install any IM and Presence subscriber nodes.

For touchless installations, you can install your local Unified Communications Manager publisher node and your IM and Presence
                                          Service central cluster in a single process. However, your telephony cluster must be installed separately.

For more information, see the "Configure Centralized Deployment" chapter at Configuration and Administration of the IM and Presence Service Guide .

Run the Collab Sizing Tool to get the required virtual machine count and specs of each virtual machine. If you don't want
                              to run the Collab Sizing Tool, follow the guidance in the OVA readme and the OVA wizard to select a predefined starting point,
                              which can be changed later if needed. For more information, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications<url TBD> .

### Cluster Size

Unified Communications Manager supports a megacluster that can support up to 8 primary call processing nodes and 8 secondary/standby call processing nodes.The
                              total number of servers in a cluster, including the Unified Communications Manager publisher node, TFTP server, and media servers, cannot exceed 21.

The maximum number of IM and Presence Service nodes in a Standard cluster is 6.

For more information, see "Cisco Collaboration Solutions Design Guidance" at http://www.cisco.com/go/ucsrnd .

### Publisher
                              		  Nodes and Subscriber Nodes

Within a cluster,
                              		  there is a database publisher for each type of node that you install.

When you install Unified
                                 			 Communications Manager , the installation wizard prompts you to
                              		  specify whether the node you are installing is the first node in the cluster.
                              		  The first Unified
                                 			 Communications Manager node that you install becomes the publisher
                              		  node, because it publishes the voice and video database to the other Unified
                                 			 Communications Manager nodes in the cluster. All subsequent nodes in
                              		  the cluster are called subscriber nodes. Each subscriber node must be
                              		  associated with the publisher node. You must set up all subscriber nodes in the
                              		  system topology on the publisher node before you install the software on the
                              		  subscriber nodes.

When you install IM and
                                 			 Presence nodes, the first node that you install functions as the
                              		  server for the IM and
                                 			 Presence database. Because this node publishes the database for all
                              		  of the IM and
                                 			 Presence nodes in the cluster, it is referred to as the IM and
                                 			 Presence database publisher; however, you must install this and all
                              		  other IM and
                                 			 Presence nodes as subscribers of the Unified
                                 			 Communications Manager publisher node. As with other subscriber
                              		  nodes, you must add these in the system topology before you install the
                              		  software.

### Topology Options

When installing your cluster, you must decide on the topology that you want to deploy. For example:

The number of cluster nodes required.

Whether you will install all cluster nodes in a single location, or if you will install your nodes in separate geographic
                                    sites connected via a WAN in order to provide geographic redundancy. For more information on scalability, see Megacluster .

### Supported Versions for Intra-cluster versions

Unified Communications Manager and the IM and Presence Service nodes in the same cluster must be running the supported builds
                              as mentioned in the Release Notes for Cisco Unified Communications Manager and the IM and Presence Service .

This release offers two main deployment options for this release of Unified Communications Manager and the IM and Presence Service :

Standard Deployments of IM and Presence Service—Both Unified Communications Manager and the IM and Presence Service must be running the supported versions for your deployment. A version mismatch is not supported.

Centralized Deployments of IM and Presence Service —If you have the Centralized Deployment option configured on the IM and Presence Service , then within the IM and Presence Service central cluster, both the Unified Communications Manager instance and the IM and Presence Service must be running the same version. However, the telephony cluster that the central cluster connects to does not have to be
                                    running the same version.

## Installation Methods

This guide covers the installation methods for Unified Communications Manager and IM and Presence Service .

These installation methods can be used for any of the following scenarios:

Fresh Install (first-time setup of a brand-new node or cluster, no existing deployment, and no existing customer data).

Expand a cluster (add a new subscriber node to an existing cluster).

Direct Migration from an older version. For more information, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service .

Installation Method

Description

Attended Install

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

A baseline-typical installation of one node of either Unified Communications Manager or IM and Presence Service , using the native Install Wizard graphical user interface (GUI). Unified Communications Manager only includes an option Apply a Patch During an Upgrade (for example, to apply a Service Update to the base release you are installing).

To install a cluster using this method, follow the Attended Installation steps in this sequence:

Unified Communications Manager publisher node

Unified Communications Manager subscriber nodes

IM and Presence Service publisher node

IM and Presence Service subscriber nodes

You can use this method with any of the following software media options:

Physical install DVD.

Bootable installer image for base release in ISO format (obtained from either Cisco Commerce Workspace, Cisco License Central,
                                                or a Cisco Business Edition appliance factory preload). This file applies for all the 3 hypervisors.

(Applicable only to VMware vSphere ESXi and Cisco NFVIS for UC) Base OVA containing all supported virtual machine configurations.

(Applicable only to Nutanix AHV) A set of base OVAs, each containing a supported virtual machine configuration.

(Applicable only to VMware vSphere ESXi) Partial skip-installed OVA. This OVA format file contains partially installed application
                                                up to the "skip" Install Wizard point where the application is ready to accept an Answer File and complete installation. OVA
                                                format file is obtained either from Cisco License Central or from a Cisco Business Edition appliance factory preload.

Touchless Install of a Single Node or a Cluster

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

A partially automated installation of one node or installation of clusterwide install of multiple nodes of Unified Communications
                                          Manager and IM and Presence Server.

Use this method to get basic automation for one node, where you can fill out all the information initially, start the Install
                                          Wizard with that information, and complete the rest of the installation automatically using the Answer File.

For clusterwide installations, use this method to generate pre-created Answer Files, that occurs in one seamless process with
                                          minimal intervention.

To install a single node or a cluster using this method, follow the Touchless Installation steps for the hypervisor selected:

Create an Answer File for each node in the cluster using the Unified Communications Answer File Generator.

Place all those Answer Files in well-known locations. See Generate Answer Files for Touchless Install .

Power on the node or all the cluster nodes simultaneously.

In this method, no interaction with the native Install Wizard is required. The nodes will communicate with each other and
                                          each node will read its Answer File for instructions.

You can use this method with any of the software media options available for Attended Install. Use this method to:

Get more automation—Unattended Install of the entire cluster + zero interaction with the native Install Wizard.

Faster installation—Cluster nodes undergo installation in parallel. This is especially useful if you have a large cluster
                                                with many nodes to install.

Cisco Prime Collaboration Deployment (PCD)

This installation method is applicable only for VMware vSphere ESXi.

Fresh install, add nodes to, or direct migrate a cluster of Unified Communications Manager and IM and Presence Server using
                                          Cisco Prime Collaboration Deployment. See the Cisco Prime Collaboration Deployment Administration Guide for the following:

Fresh Install Task (where PCD performs similar operation as Touchless Install of a Single Node or Cluster).

Edit/Expand Task (where PCD performs similar operation as Touchless Install to add a single node).

Migration Task (where PCD is performing direct migration of an entire cluster).

Use this method when:

You require assistance with multiple nodes of one cluster and/or multiple clusters, and a separate management application
                                                is acceptable.

(PCD Migration Task only) you are "repaving" an existing installation where you are dealing with one or more of the following:

Two or more of these factors as part of the same migration—site moves, hardware changes, VMware upgrades, application version
                                                      upgrades, application readdresses, and in scenarios where more flexibility is expected than what direct upgrades can provide.

You need to rebuild, restore or recover a cluster, or you need to revert configuration changes. Here, you are looking for
                                                      a more flexible approach than what Unified Communications Manager Disaster Recovery Solution can provide.

VMware OVF Tool

This installation method is applicable only for VMware vSphere ESXi.

Allows you to perform fully automated installation or direct migration of either a single node or an entire cluster, using
                                          the VMware OVF Tool.

To install or direct migrate a cluster, follow the procedures at Automated Installation using vApp properties and VMware OVF Tool :

Use the VMware OVF Tool to create a skip-install OVA for each cluster node (with OVA parameters filled in, instead of using
                                                Answer File Generator).

Deploy all cluster nodes skip-installed OVAs simultaneously.

Installation continues like Touchless Install of a Single Node or Cluster or Fresh Install with Data Import.

It is best to use this method with skip-install OVAs, as that provides the shortest duration and highest level of automation.

Use this method when you require a programmatic install or direct migration method on top of any of the factors that drive
                                          consideration of Touchless Install of Cluster or Fresh Install with Data Import.

Fresh Install with Data Import

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

Perform direct migration of either a single node or an entire cluster, using similar mechanisms as Prime Collaboration Deployment
                                          Migration task but native to Unified Communications Manager and IM and Presence.

To directly migrate a cluster, follow the Install with Data Import tasks:

On each cluster node, export your old version's data.

For each cluster node, provision a new virtual machine for your new version and follow either Attended Install or Touchless
                                                Install for a single node or the cluster node(s) of interest. Using the Data Import options available in Install Wizard and/or
                                                the Unified Communications Answer File Generator.

You can use this method with any of the software media options available for Attended Install.

Use this method for "native" direct migrations that don't require a separate management application like Prime Collaboration
                                          Deployment. You can have more granular control over individual nodes migration timing and sequencing. You may also use this
                                          method to avoid use of application readdress and temporary extra hardware footprint for direct migration.

Add a Node Install for cluster expansion

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

If you want to add a node to an existing Unified Communications Manager or IM and Presence Service cluster for attended or
                                          touchless installation, complete the tasks in: Add a New Node to an Existing Cluster

This guide provides the general installation procedures for Unified Communications Manager.

If your deployment integrates Unified CM with other Cisco solutions, such as Unified Contact Center Enterprise (UCCE), review
                                          the installation and upgrade documentation for each product. This ensures that you meet all integration requirements across
                                          platforms. For example, if you are integrating Unified CM with Cisco Contact Center, also refer to the Contact Center Enterprise Installation and Upgrade Guide .

## Requirements and Limitations

The following sections provide information about the requirements that your system must meet, and limitations that apply when
                              you install or upgrade Unified Communications Manager or IM and Presence Service .

By default, if your system is in non-FIPS mode, you must enable it, if desired.

Ensure that the security password length is a minimum of 14 characters before you enable FIPS, Common Criteria, or Enhanced
                                                Security mode on the cluster. Update the password even if the prior version was FIPS enabled.

Do not run Network Address Translation (NAT) or Port Address Translation (PAT) between servers where you are installing the
                                          Unified Communications Manager.

Ensure that the network interface card (NIC) speed and duplex settings on the switch port are the same as those that you plan
                                          to set on the new server.

For GigE (1000/FULL), you should set NIC and switch port settings to Auto/Auto ; do not set hard values.

You must enable PortFast on all switch ports that are connected to Cisco servers.

With PortFast enabled, the switch immediately brings a port from the blocking state into the forwarding state by eliminating
                                          the forwarding delay [the amount of time that a port waits before changing from its Spanning-Tree Protocol (STP) learning
                                          and listening states to the forwarding state].

### Virtualization Requirements

Unified Communications Manager and IM and Presence are supported on VMware vSphere ESXi, Cisco NFVIS-for-UC, and Nutanix AHV
                                 versions.

Cisco NFVIS-for-UC is a special edition of NFVIS that introduces a new commercial offer with a separate product ID, distinct
                                 pricing, new licensing, and a slightly different administrative GUI.

Cisco NFVIS-for-UC supports only select on-premises calling applications.

Cisco NFVIS-for-UC supports only select Cisco Calling Appliances.

For general virtualization software/hardware requirements, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

#### Application/Hypervisor Compatibility

See the following table for compatibility of Unified Communications Manager and the IM and Presence Service with hypervisor
                                 releases.

Only the listed major/minor releases are supported, with a minimum required maintenance or patch release.

Unlisted major/minor release trains are not supported.

For support of subsequent maintenance or patch releases, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

Compatible Hypervisor Major/Minor Releases with Minimum Maintenance/Patch Release

VMware vSphere ESXi

Cisco NFVIS-for-UC

Nutanix AHV

Unified Communications Manager

Release 15SU4

8.0 U1

7.0 U3

4.18.2a

AHV 10.0 + AOS/PC 7.0

Releases 15 FCS through 15SU3

8.0 U1

7.0 U3

Not supported

Not supported

IM and Presence Service

Release 15SU4

8.0 U1

7.0 U3

4.18.2a

AHV 10.0 + AOS/PC 7.0

Releases 15 FCS through 15SU3

8.0 U1

7.0 U3

Not supported

Not supported

Session Management Edition

Release 15SU4

8.0 U1

7.0 U3

4.18.2a

AHV 10.0 + AOS/PC 7.0

Releases 15 FCS through 15SU3

8.0 U1

7.0 U3

Not supported

Not supported

#### Virtual Machine Configurations and CPU Minimum Base Frequencies

Applications are supported only with specific virtual machine (VM) configurations.

You must deploy these VMs using the latest Cisco-provided OVA file (see the Readme file for important notes.)

For Unified Communications Manager nodes, the files are available here: https://software.cisco.com/download/home/286331940/type/283088407/release/15

For IM and Presence nodes, the files are available here: https://software.cisco.com/download/home/286331963/type/283757588/release/15

One base OVA is used for both VMware vSphere ESXi and Cisco NFVIS for UC, while a set of base OVAs is used for Nutanix AHV.

See the following table for the required and supported virtual machine configurations.

Each VM represents a particular application capacity point and has a minimum required CPU base frequency.

For more information on how these are used, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

Component and Capacity Point

vCPU

Physical CPU Required Minimum Base Frequency

vRAM

vDisk

vNIC

Small

2

2.00+ GHz

10 GB

1x 110 GB

1 (1GbE+)

Medium

2

*

12 GB

1x 110 GB

1 (1GbE+)

Large

4

*

14 GB

1x 110 GB

1 (1GbE+)

* 2.5+ GHz is recommended for simple sizing. Alternatively, run the Collaboration Sizing Tool to determine if your deployment
                                 meets the requirements for 2.00+ GHz at this capacity.

Component and Capacity Point

vCPU

Physical CPU Required Minimum Base Frequency

vRAM

vDisk

vNIC

Extra Small

(1000 devices)

1

2.00+ GHz

6 GB

1x 110 GB

1 (1GbE+)

Small

(5000 devices)

2

2.50+ GHz

10 GB

2x 80GB

1 (1GbE+)

Medium

(15,000 devices)

4

2.50+ GHz

14 GB

2x 80GB

1 (1GbE+)

Large

(25,000 devices)

6

2.50+ GHz

18 GB

2x 80GB

1 (1GbE+)

Component and Capacity Point

vCPU

Physical CPU Required Minimum Base Frequency

vRAM

vDisk

vNIC

Medium VM

2

2.50 GHz

12 GB

1x 110 GB

1

Large VM

4

2.50 GHz

14 GB

1x 110 GB

1

#### Platform Requirements

This section provides information about the platform requirements that you must meet before you can deploy Unified Communications Manager and the IM and Presence Service on virtual machines.

In this release, you cannot install or run Unified Communications Manager and the IM and Presence Service directly on server hardware; you must run these applications on virtual machines.

Before you can install or direct migrate the software on a virtual machine, you must:

Install and configure physical hardware.

Install and configure the virtualization software.

Deploy a virtual machine from the correct Cisco provided OVA file for the release.

Depending on the installation method used, additional steps are required. All methods require the correct Cisco-provided bootable
                                       ISO installation file for the release.

### Subnet
                           	 Limitations

Do not install Unified Communications Manager in a large Class A or Class B subnet that contains a large number of devices. For more information, see Cisco Collaboration System 12.x Solution Reference Network Designs (SRND) .

### IP Address
                           	 Requirements

A complete collaboration solution relies on DNS in order to function correctly for a number of services and thus requires
                                 a highly available DNS structure in place. If you have a basic IP telephony deployment and do not want to use DNS, you can
                                 configure Unified Communications Manager and IM and Presence Service to use IP addresses rather than hostnames to communicate with gateways and endpoint devices.

You must configure the server to use static IP addressing to ensure that the server obtains a fixed IP address. Using a static
                                 IP address also ensures that Cisco Unified IP Phones can register with the application when you plug the phones into the network.

### Verify DNS
                           	 Registration

Follow
                                 		  this procedure if you use a DNS in your topology. You must verify that all
                                 		  servers to be added are registered in DNS properly by performing the following
                                 		  actions:

Step 1

Open a command
                                          			 prompt.

Step 2

To ping each
                                          			 server by its DNS name, enter ping
                                             				DNS_name .

Step 3

To look up each
                                          			 server by IP address, enter nslookup IP_address .

### DNS
                           	 requirements

Note the
                                 		  following requirements:

Mixed-mode DNS deployments not supported—Cisco does not support mixed-mode deployments. Both Unified Communications Manager and IM and Presence Service must either use or not use DNS.

If your deployment uses DNS— Unified Communications Manager and IM and Presence Service should use the same DNS server. If you use different DNS servers between IM and Presence Service and Unified Communications Manager , it is likely to cause abnormal system behavior.

If your deployment does not use DNS, you will need to edit the following Host Name/IP Address fields:

Server—In the Cisco Unified CM Administration Server Configuration window, set IP addresses for your cluster nodes.

IM and Presence UC Service—In the Cisco Unified CM Administration UC Service Configuration window, create an IM and Presence UC service that points to the IP address of the IM and Presence database publisher node.

CCMCIP Profiles—In the Cisco Unified CM IM and Presence Administration CCMCIP Profile Configuration window, point any CCMCIP profiles to the IP address of the host.

Multinode considerations—If you are using the multinode feature in IM and Presence Service , see the section regarding multinode deployments in the Configuration and Administration of the IM and Presence Service Guide for DNS configuration options.

Ensure that the DNS server is configured on Windows 2019 or above or use the DNS server configured in any Linux Machine.

### Firewall Requirements

Ensure that you configure your firewall so that connections to port 22 are open, and aren't throttled. During the installation
                                 of Unified Communications Manager and IM and Presence subscriber nodes, multiple connections to the Unified Communications
                                 Manager publisher node are opened in quick succession. Throttling these connections could lead to a failed installation. For
                                 general security considerations, see the Security Guide for Cisco Unified Communications Manager .

For more information on the port usage, see the chapter 'Cisco Unified Communications Manager TCP and UDP Port Usage' in the System Configuration Guide for Cisco Unified Communications Manager .

Ensure that you complete the following firewall updates before pre-installation:

If a firewall is in the routing path between nodes, disable the firewall.

Increase the firewall timeout settings until after you complete the installation.

Temporarily allowing network traffic in and out of the nodes (for example, setting the firewall rule for these nodes to IP
                                 any/any) does not always suffice. The firewall might still close necessary network sessions between nodes due to timeouts.

### NTP Status

You must verify the NTP status on the publisher node.

If the publisher node fails to synchronize with an NTP server, subscriber node installation can fail. On the Unified Communications
                              Manager publisher node, run the utils ntp status CLI command.

### RTT Requirement

Ensure that you verify that the links between servers meet the 80-ms round-trip time (RTT) requirement and that you have enough
                              bandwidth to support database replication.

For more information on the 80-ms RTT requirement, see the Cisco Unified Communications Solutions Reference Network Design .

### NTP Status

You must verify the NTP status on the publisher node.

If the publisher node fails to synchronize with an NTP server, subscriber node installation can fail. On the Unified Communications
                              Manager publisher node, run the utils ntp status CLI command.

### Supported Versions

Unified Communications Manager and the IM and Presence Service nodes in the same cluster must be running the supported builds
                                 as mentioned in the Release Notes for Cisco Unified Communications Manager and the IM and Presence Service .

#### Version Mismatches

This release offers two main deployment options for this release of Unified Communications Manager and the IM and Presence Service :

Standard Deployments of IM and Presence Service—Both Unified Communications Manager and the IM and Presence Service must be running the supported versions for your deployment. A version mismatch is not supported.

Centralized Deployments of IM and Presence Service —If you have the Centralized Deployment option configured on the IM and Presence Service , then within the IM and Presence Service central cluster, both the Unified Communications Manager instance and the IM and Presence Service must be running the same version. However, the telephony cluster that the central cluster connects to does not have to be
                                       running the same version.

### Software
                           	 Restrictions

You cannot install or use third-party or Windows-based software applications. The system can upload and process only software
                                 that Cisco Systems provides and digitally signs. For more information, see the 'Operating System and Security Hardening' chapter
                                 in the Security Guide for Cisco Unified Communications Manager .

You must perform all software installations and upgrades using Cisco Unified Communications Operating System Administration.

For information about software compatibility for Unified Communications Manager and IM and Presence Service, see the Compatibility Matrix for Cisco Unified Communications Manager and the IM and Presence Service .

### Username and Password Requirements

During the installation, you must specify the following user names and passwords:

Administrator
                                       				Account user name and password

Application User
                                       				name and password

Security
                                       				password

We recommend that you use a different username for the Cisco Unified Communications Operating System Administration and the
                                             Cisco Unified CM Administration interfaces.

#### Administrator
                                 		  Account

You use
                                 		  the Administrator Account user name and password to log in to the following
                                 		  areas:

Cisco Unified Communications Operating System Administration

Disaster Recovery System

Command Line
                                       				Interface

To specify
                                 		  the Administrator Account user name and password, follow these guidelines:

Administrator Account user name—The Administrator Account user name must start with an alphabetic character and can contain
                                       alphanumeric characters, hyphens, and underscores.

Administrator Account password—The Administrator Account password must be at least eight characters long and can contain alphanumeric characters, hyphens, and underscores.

You can change the Administrator Account password or add a new Administrator account by using the command line interface.
                                 For more information, see the Command Line Interface Reference Guide for Cisco Unified Communications Solutions .

#### Application User

When you install Unified Communications Manager, you must enter an Application User name and password. You use the Application
                                 User name and password to access applications that are installed on the system, including the following areas:

Cisco Unified CM Administration

Cisco Unified Serviceability

Cisco Real-Time Monitoring Tool

Cisco
                                       			 Unified Reporting

To specify
                                 		  the Application User name and password, follow these guidelines:

Application User username—The Application User username must start with an alphabetic character and can contain alphanumeric
                                       characters, hyphens, and underscores.

Application User password—The Application User password must be at least eight characters long and can contain alphanumeric characters, hyphens, and underscores.

Caution

Do not use the system application name as the Application User name. Using a system application name causes the installation
                                             to fail with an unrecoverable error during the installation of the database.

System application
                                             			 names are:

CCMSysUser

WDSysUser

CCMQRTSysUser

IPMASysUser

WDSecureSysUser

CCMQRTSecureSysUser

IPMASecureSysUser

TabSyncSysUser

CUCService

You can change the Application User name and password by using the command line interface. For more information, see the Command Line Interface Reference Guide for Cisco Unified Communications Solutions .

#### Security
                                 		  Password

During the installation, you must specify a security password. Unified Communications Manager systems use this password to authorize communications between nodes in the cluster, including IM and Presence Service nodes.
                                 This password must be identical on all nodes in the cluster.

The Security password must be at least eight characters long and can contain alphanumeric characters, hyphens, and underscores.

#### Password
                              	 Recommendations

The installation wizard ensures that you enter a strong password. To create a strong password, follow these recommendations:

Password must be at least eight characters long and can contain alphanumeric characters, hyphens, and underscore.

Should not have the non-printable ASCII characters.

Contains at least one alphanumeric character.

Mix uppercase
                                          				and lowercase letters.

Mix letters and
                                          				numbers.

Include special
                                          				symbols.

Remember that
                                          				longer passwords are stronger and more secure than shorter ones.

Avoid the
                                    		  following types of passwords:

Do not use only alphanumeric characters.

Do not use any non-alphanumeric characters.

Do not use
                                          				recognizable words, such as proper names and dictionary words, even when
                                          				combined with numbers.

Do not invert-recognizable words.

Do not use word or number patterns, such as aaabbb, abc123, qwerty, zyxwvuts, and 123321.

Do not use
                                          				recognizable words from other languages.

Do not use personal information of any kind, including birthdays, postal codes, names of children, or pets.

### Installation Time
                           	 Requirements

#### Time Requirements for Unified Communications Manager

The
                                 		  entire installation process, excluding pre- and post-installation tasks, takes
                                 		  45 to 90 minutes, depending on your server type.

#### Time
                                 		  Requirements for IM and Presence Nodes

The entire IM and Presence Service installation process, excluding pre- and post-installation tasks, takes approximately 45 to 90 minutes per server, depending
                                 on your server type.

## Licensing Requirements

The following sections provide information about the licensing requirements for Unified Communications Manager and the IM
                           and Presence Service.

Make sure that your system has adequate licensing.

### Smart Software Licensing Overview

Cisco Smart Software Licensing is a new way of thinking about licensing. It adds flexibility to your licensing and simplifies
                              it across the enterprise. It also delivers visibility into your license ownership and consumption.

Cisco Smart Software Licensing helps you to procure, deploy, and manage licenses easily where devices self-register and report
                              license consumption, removing the need for product activation keys (PAK). It pools license entitlements in a single account
                              and allows you to move licenses freely through the network, wherever you need them. It is enabled across Cisco products and
                              managed by a direct cloud-based or mediated deployment model.

The Cisco Smart Software Licensing service registers the product instance, reports license usage, and obtains the necessary
                              authorization from Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

You can use Smart Licensing to:

See the license usage and count

See the status of each license type

See the product licenses available on Cisco Smart Software Manager or Cisco Smart Software Manager satellite

Renew License Authorization with Cisco Smart Software Manager or Cisco Smart Software Manager satellite

Renew the License Registration

Deregister with Cisco Smart Software Manager or Cisco Smart Software Manager satellite

The License authorization is valid for 90 days with a renewal at least once in 30 days. The authorization will expire after
                                          90 days if it is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                          Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                          Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync.

There are two main deployment options for Smart Licensing:

Cisco Smart Software Manager

Cisco Smart Software Manager satellite

#### Cisco Smart Software Manager

The Cisco Smart Software Manager is a cloud-based service that handles your system licensing. Use this option if Unified
                                 Communications Manager can connect to cisco.com, either directly or via a proxy server. Cisco Smart Software Manager allows
                                 you to:

Manage and track licenses

Move licenses across virtual account

Remove registered product instance

Optionally, if Unified Communications Manager cannot connect directly to Cisco Smart Software Manager, you can deploy a proxy
                                 server to manage the connection.

For additional information about Cisco Smart Software Manager, go to https://software.cisco.com .

#### Cisco Smart Software Manager Satellite

Cisco Smart Software Manager satellite is an on-premise deployment that can handle your licensing needs if Unified Communications
                                 Manager cannot connect to cisco.com directly, either for security or availability reasons. When this option is deployed, Unified
                                 Communications Manager registers and report license consumption to the satellite, which synchronizes its database regularly
                                 with the backend Cisco Smart Software Manager that is hosted on cisco.com.

The Cisco Smart Software Manager satellite can be deployed in either Connected or Disconnected mode, depending on whether
                                 the satellite can connect directly to cisco.com.

Connected—Used when there is connectivity to cisco.com directly from the Smart Software Manager satellite. Smart account synchronization
                                       occurs automatically.

Disconnected—Used when there is no connectivity to cisco.com from the Smart Software Manager satellite. Smart Account synchronization
                                       must be manually uploaded and downloaded.

For Cisco Smart Software Manager satellite information and documentation, go to https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html .

#### License Types

The following
                                    		licensing types are available to cover your needs:

Cisco
                                          				Unified Workspace Licensing (UWL) provides the most popular bundles of Cisco
                                          				Collaboration applications and services in a cost-effective, simple package. It
                                          				includes soft clients, applications server software, and licensing on a
                                          				per-user basis.

User Connect
                                          				Licensing (UCL) is a per-user based license for individual Cisco Unified
                                          				Communications applications, which includes the applications server software,
                                          				user licensing, and a soft client. Depending on the type of device and number
                                          				of devices that you require, UCL is available in Essential, Basic, Enhanced,
                                          				and Enhanced Plus versions.

For more
                                          				information about these license types and the versions in which they are
                                          				available, see http://www.cisco.com/c/en/us/products/unified-communications/unified-communications-licensing/index.html .

Session Management Edition can be registered to either Cisco Smart Software Manager or Cisco Smart Software Manager satellite.
                                          You can register Session Management Edition using the same processes as for Unified Communications Manager, register to a
                                          virtual account that Cisco Unified Communications Manager is registered or a separate virtual account, and fulfill a minimal
                                          set of licenses requirement.

The SME registered in Specific License Reservation (SLR) requires a minimum set of licenses reserved in CSSM while generating
                                                      an SLR authorization code.

#### Product Instance
                              	 Evaluation Mode

Evaluation period is before the product is registered.

### IM and Presence Service License Requirements

The IM and Presence Service does not require a server license or software version license. However, you must assign users and enable the IM and Presence Service for each assigned user.

With the Jabber for Everyone offer, no end user licenses are required to enable IM and Presence Service functionality. For
                                             more information, see Jabber for Everyone Quick Start Guide .

You can assign IM and Presence Service on a per user basis, regardless of the number of clients you associate with each user. When you assign IM and Presence Service to a user, this enables the user to send and receive IMs and availability updates. If users are not enabled for IM and Presence Service , they will not be able to log in to the IM and Presence Service server to view the availability of other users, send or receive IMs, and other users will not see their availability status.

You can enable a user for IM and Presence Service using any of the following options:

The End User Configuration window in Unified Communications Manager . For more information, see the Administration Guide for Cisco Unified Communications Manager .

The Bulk
                                       				Administration Tool (BAT)

Assign IM and Presence Service to a feature group template which you can reference from the Quick User/Phone Add window in Unified Communications Manager .

For more information, see the System Configuration Guide for Cisco Unified Communications Manager .

IM and Presence Service capabilities are included within both User Connect Licensing (UCL) and Cisco Unified Workspace Licensing (CUWL). IM and Presence Service capabilities can also be acquired for users that are not Unified Communications Manager IP Telephony users through the Jabber for Everyone Offer. For more information, see Jabber for Everyone Quick Start Guide .

## Required
                        	 Installation Information

When you install either Unified Communications Manager or the IM and Presence Service on a server, the installation process requires you to provide specific information. You can provide this information manually
                              during the installation process or you can provide it using an answer file. For each server that you install in a cluster,
                              you must gather this information before you begin the installation process.

The
                              		  following table lists the information that you must gather before you begin the
                              		  installation.

Because some of
                                          			 the fields are optional, they may not apply to your configuration. For example,
                                          			 if you decide not to set up an SMTP host during installation, the parameter
                                          			 still displays, but you do not need to enter a value.

You
                              		  cannot change some of the fields after the installation without reinstalling
                              		  the software, so be sure to enter the values that you want. The last column in
                              		  the table shows whether you can change a parameter after installation, and if
                              		  you can, it provides the appropriate menu path or Command Line Interface (CLI)
                              		  command.

We recommend that you make copies of this table and record your entries for each server in a separate table, even if you are
                              planning to use the DMABackupInfo.inf file to configure your system.

Configuration Data

Description

Editable after Installation

Administrator
                                             						Credentials

Administrator Login

Specifies the name that you want to assign to the Administrator
                                          					 account.

No

After
                                          					 installation, you can create additional administrator accounts, but you cannot
                                          					 change the original administrator account user ID.

Administrator Password

Specifies the password for the Administrator account.

Yes

CLI: set password user admin

Application User
                                             						Credentials

Application User Username

Specifies the user ID for applications installed on the system.

Yes

CLI: utils reset_application_ui_administrator_name

Application User Password

Specifies the password for applications on the system.

Yes

CLI: utils reset_application_ui_administrator_password

Security Password

Security password for Unified Communications Manager

Servers in the cluster use the security password to communicate with one another. Set this password on the Unified Communications Manager publisher node, and enter it when you install each additional node in the cluster, including IM and Presence nodes.

Yes. You can change the security password on all nodes in the cluster using the following command:

CLI: set password user security

Certificate Information

Organization

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

Unit

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

Location

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

State

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

Country

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality]
                                             						[state]

(Optional) SMTP

SMTP Location

Specifies the name of the SMTP host that is used for outbound
                                          					 email.

You must fill in this field if you plan to use electronic
                                          					 notification. If not, you can leave it blank.

Yes

In Cisco Unified Communications Operating System Administration: select Settings > SMTP and enter the IP address or Hostname in the SMTP Host Field.

CLI: set smtp [host]

NIC Interface
                                             						Settings

NIC Speed

If you do not enable automatic negotiation of the ethernet
                                          					 Network Interface Card (NIC) speed, you must select the NIC speed (either 10
                                          					 megabit or 100 megabit).

Yes

CLI: set network nic eth0 {auto | {en| dis}} {speed| {10| 100}} {duplex half| {half| full}}

1000BASE-T can only be enabled via
                                                      auto-negotiation.

Virtual machines do not support this
                                                      command.

NIC Duplex

If you do not enable automatic negotiation of the ethernet
                                          					 Network Interface Card (NIC) duplex setting, you must select the NIC duplex
                                          					 setting (either Full or Half).

Yes

CLI: set network nic eth0 {auto | {en| dis}} {speed| {10| 100}} {duplex half| {half| full}}

1000BASE-T can only be enabled via
                                                      auto-negotiation.

Virtual machines do not support this
                                                      command.

MTU Size

The
                                                      						MTU setting must be the same on all nodes in a cluster.

The maximum transmission unit (MTU) represents the largest packet, in bytes, that this host transmits on the network.

The value must not exceed the lowest MTU size that is configured
                                          					 on any link in your network.

Default:
                                          					 1500 bytes

Yes

CLI: set network mtu [size]

Network Information

DHCP

(Dynamic Host Configuration Protocol)

Select Yes if you want to use DHCP to automatically configure the
                                          					 network settings on your server.

If you select No , you must enter a hostname, IP Address, IP Mask, Gateway,
                                          					 and DNS configuration.

Yes.

In Cisco Unified Operating System Administration: select Settings > IP > Ethernet .

CLI: set network dhcp eth0 [enable]

CLI: set network dhcp eth0 disable [node_ip]
                                                   [net_mask] [gateway_ip]

Hostname

If DHCP is set to No, you must enter a hostname for this
                                          					 machine.

Yes; for Unified Communications Manager nodes, choose one of the following:

In Cisco Unified Communications Operating System Administration, select Settings > IP > Ethernet .

CLI: set network hostname

You will be prompted to enter the parameters.

To change the hostname on Unified Communications Manager or IM and Presence server, see the 'IP Address, Hostname, and Domain Name Changes' section in the Administration Guide for Cisco Unified Communications Manager .

IP Address

If DHCP is set to No, you must enter the IP address of this
                                          					 machine.

Yes; for Unified Communications Manager nodes, choose one of the following:

In Cisco Unified Communications Operating System Administration, select Settings > IP > Ethernet .

CLI: set network IP eth0 [ip-address] [ip-mask]

To change the IP address on Unified Communications Manager or IM and Presence server, see see the 'IP Address, Hostname, and Domain Name Changes' section in the Administration Guide for Cisco Unified Communications Manager .

IP Mask

If DHCP is set to No, you must enter the IP subnet mask of this
                                          					 machine. The subnet mask together with the IP address defines the network
                                          					 address and the host address.

The
                                          					 subnet mask must use the following format: 255.255.255.0

Yes

In Cisco Unified Communications Operating System Administration, select Settings > IP > Ethernet .

CLI: set network IP eth0 [ip-address] [ip-mask]

Gateway Address

If DHCP is set to No, you must enter the gateway address.

Yes

In Cisco Unified Communications Operating System Administration, select Settings > IP > Ethernet .

CLI: set network gateway [addr]

(Optional) DNS

DNS Primary

If you have a Domain Name Server (DNS), IM and Presence contacts this DNS server first when
                                          					 attempting to resolve hostnames.

Yes

CLI: set network dns primary [address]

DNS Secondary

When a primary DNS server fails, IM and Presence will attempt to connect to the
                                          					 secondary DNS server.

Yes

CLI: set network dns secondary [address]

Domain

Represents the name of the domain in which this machine is
                                          					 located

Yes

CLI: set network domain [name]

Timezone

Time Zone

Reflects the local time zone and offset from Greenwich Mean Time
                                          					 (GMT). Select the time zone that most closely matches the location of your
                                          					 machine.

Yes

CLI: set timezone [zone

Network Time Protocol

NTP Server IP Address

During installation of the IM and Presence publisher node, you must specify the IP address of an external Network Time Protocol (NTP) server. We recommend that you
                                          use the Unified Communications Manager publisher node as the NTP server.

Yes

In Cisco Unified Communications Operating System Administration, select Settings > NTP Servers .

## Export Restricted and Export
                        	 Unrestricted Software

This release of Unified Communications Manager and IM and Presence Service supports an export unrestricted (XU) version, in addition to the export restricted (K9) version.

Export unrestricted versions differs from restricted versions as follows:

Encryption of user payload (information exchange) is not supported.

External SIP interdomain federation with Microsoft OCS/Lync or AOL is not supported.

After you install an unrestricted release, you can never upgrade to a restricted version. A fresh install of a restricted
                                    version on a system that contains an unrestricted version is also not supported.

All nodes within a single cluster must be in the same mode. For example, Unified Communications Manager and IM and Presence Service in the same cluster must either all be in unrestricted mode or all be in restricted mode.

IP Phone security configurations are modified to disable signaling and media encryption (including encryption provided by
                                    the VPN phone feature).

For all Graphical User Interfaces (GUIs) and Command Line Interfaces (CLIs), the Administrator can view the product version
                              (restricted or export unrestricted).

The following table describes the GUI items that are not available for the export unrestricted version of Unified Communications Manager and IM and Presence Service .

GUI Item

Location

Description

Cisco Unified CM Administration

VPN Configuration

Advanced Features > VPN

This menu and its options are not available.

Phone Security Profile Configuration

System > Security > Phone Security Profile

The Device Security Mode is set to Non Secure and is not configurable.

Cisco
                                             						Unified CM IM and Presence Administration

Security Settings

You
                                                						cannot check the Enable XMPP Client to IM/P Service Secure Mode setting.

You
                                                						cannot check the Enable XMPP Router-to-Router Secure Mode setting.

You
                                                						cannot check the Enable Web Client to IM/P Service Secure Mode setting.

The option to set SIP intra-cluster Proxy-to-Proxy Transport Protocol to TLS have been removed.

Service Parameter Configuration for Cisco SIP Proxy service

System > Service Parameters and choose Cisco SIP Proxy as the Service

All TLS
                                                						options have been removed for the Transport Preferred Order parameter.

The TLS option have been removed from the SIP Route Header Transport Type parameter.

SIP Federated Domains

Presence > Inter-domain
                                                						  Federation > SIP Federation

When you
                                          						configure interdomain federation to OCS/Lync, you will receive warning popup to
                                          						indicate that it is only possible to directly federate with another OCS/Lync
                                          						within the enterprise. Interdomain federation to OCS/Lync outside the
                                          						enterprise is not supported in unrestricted mode.

XMPP Federation Settings

Presence > Inter-domain
                                                						  Federation > XMPP Federation > Settings

You cannot configure the security mode. It is set to NO TLS .

Proxy Configuration Settings

Presence > Routing > Settings

You
                                          						cannot set any TLS or HTTPS listeners as the preferred proxy listener.

| IM and Presence Deployment | Description |
|---|---|
| Standard Deployment (de-centralized/distributed) ) | The IM and Presence Service and Unified Communications Manager cluster nodes are part of the same cluster. The IM and Presence
                                          cluster shares a platform and many of the same services as the telephony cluster. Each cluster will have nodes of both. This
                                          option requires a 1x1 mapping of Unified CM telephony clusters to IM and Presence clusters. Basic installations order followed is same as mentioned in the Attended Install method. For more information, see the "Installation
                                          Methods". For touchless installations, you can install all Unified Communications Manager and IM and Presence Service cluster nodes
                                          concurrently in a single process. |
| IM and Presence Centralized Cluster Deployment | A single IM and Presence Service central cluster is installed separately from your Unified Communications Manager telephony
                                          cluster(s) and may be located on different hardware servers. The single IM and Presence Service cluster maps to all Unified
                                          Communications Manager telephony clusters. This allows you to scale your telephony deployment and IM and Presence deployment
                                          separately. For basic installations: Install a local Unified Communications Manager publisher node in the central IM and Presence Service cluster. This node is
                                                not a part of your telephony deployment. The node handles functions like database and user provisioning for the central cluster. Install the IM and Presence Service database publisher node. Install any IM and Presence subscriber nodes. For touchless installations, you can install your local Unified Communications Manager publisher node and your IM and Presence
                                          Service central cluster in a single process. However, your telephony cluster must be installed separately. For more information, see the "Configure Centralized Deployment" chapter at Configuration and Administration of the IM and Presence Service Guide . |

| Note | The Centralized IM and Presence Service cluster requires a Unified CM publisher node, for a total of seven servers in the
                                             cluster: three IM and Presence Service sub-cluster pairs (six servers) + the Unified CM publisher node. |
|---|---|

| Installation Method | Description |
|---|---|
| Attended Install | Note This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. A baseline-typical installation of one node of either Unified Communications Manager or IM and Presence Service , using the native Install Wizard graphical user interface (GUI). Unified Communications Manager only includes an option Apply a Patch During an Upgrade (for example, to apply a Service Update to the base release you are installing). To install a cluster using this method, follow the Attended Installation steps in this sequence: Unified Communications Manager publisher node Unified Communications Manager subscriber nodes IM and Presence Service publisher node IM and Presence Service subscriber nodes You can use this method with any of the following software media options: Physical install DVD. Bootable installer image for base release in ISO format (obtained from either Cisco Commerce Workspace, Cisco License Central,
                                                or a Cisco Business Edition appliance factory preload). This file applies for all the 3 hypervisors. (Applicable only to VMware vSphere ESXi and Cisco NFVIS for UC) Base OVA containing all supported virtual machine configurations. (Applicable only to Nutanix AHV) A set of base OVAs, each containing a supported virtual machine configuration. (Applicable only to VMware vSphere ESXi) Partial skip-installed OVA. This OVA format file contains partially installed application
                                                up to the "skip" Install Wizard point where the application is ready to accept an Answer File and complete installation. OVA
                                                format file is obtained either from Cisco License Central or from a Cisco Business Edition appliance factory preload. Note Use this method when manual installation without automation is acceptable, such as labs or small deployments. | Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. | Note | Use this method when manual installation without automation is acceptable, such as labs or small deployments. |
| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Note | Use this method when manual installation without automation is acceptable, such as labs or small deployments. |
| Touchless Install of a Single Node or a Cluster | Note This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. A partially automated installation of one node or installation of clusterwide install of multiple nodes of Unified Communications
                                          Manager and IM and Presence Server. Use this method to get basic automation for one node, where you can fill out all the information initially, start the Install
                                          Wizard with that information, and complete the rest of the installation automatically using the Answer File. For clusterwide installations, use this method to generate pre-created Answer Files, that occurs in one seamless process with
                                          minimal intervention. To install a single node or a cluster using this method, follow the Touchless Installation steps for the hypervisor selected: Create an Answer File for each node in the cluster using the Unified Communications Answer File Generator. Place all those Answer Files in well-known locations. See Generate Answer Files for Touchless Install . Power on the node or all the cluster nodes simultaneously. In this method, no interaction with the native Install Wizard is required. The nodes will communicate with each other and
                                          each node will read its Answer File for instructions. You can use this method with any of the software media options available for Attended Install. Use this method to: Get more automation—Unattended Install of the entire cluster + zero interaction with the native Install Wizard. Faster installation—Cluster nodes undergo installation in parallel. This is especially useful if you have a large cluster
                                                with many nodes to install. | Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Cisco Prime Collaboration Deployment (PCD) | Note This installation method is applicable only for VMware vSphere ESXi. Fresh install, add nodes to, or direct migrate a cluster of Unified Communications Manager and IM and Presence Server using
                                          Cisco Prime Collaboration Deployment. See the Cisco Prime Collaboration Deployment Administration Guide for the following: Fresh Install Task (where PCD performs similar operation as Touchless Install of a Single Node or Cluster). Edit/Expand Task (where PCD performs similar operation as Touchless Install to add a single node). Migration Task (where PCD is performing direct migration of an entire cluster). Use this method when: You require assistance with multiple nodes of one cluster and/or multiple clusters, and a separate management application
                                                is acceptable. (PCD Migration Task only) you are "repaving" an existing installation where you are dealing with one or more of the following: Two or more of these factors as part of the same migration—site moves, hardware changes, VMware upgrades, application version
                                                      upgrades, application readdresses, and in scenarios where more flexibility is expected than what direct upgrades can provide. You need to rebuild, restore or recover a cluster, or you need to revert configuration changes. Here, you are looking for
                                                      a more flexible approach than what Unified Communications Manager Disaster Recovery Solution can provide. | Note | This installation method is applicable only for VMware vSphere ESXi. |
| Note | This installation method is applicable only for VMware vSphere ESXi. |
| VMware OVF Tool | Note This installation method is applicable only for VMware vSphere ESXi. Allows you to perform fully automated installation or direct migration of either a single node or an entire cluster, using
                                          the VMware OVF Tool. To install or direct migrate a cluster, follow the procedures at Automated Installation using vApp properties and VMware OVF Tool : Use the VMware OVF Tool to create a skip-install OVA for each cluster node (with OVA parameters filled in, instead of using
                                                Answer File Generator). Deploy all cluster nodes skip-installed OVAs simultaneously. Installation continues like Touchless Install of a Single Node or Cluster or Fresh Install with Data Import. It is best to use this method with skip-install OVAs, as that provides the shortest duration and highest level of automation. Use this method when you require a programmatic install or direct migration method on top of any of the factors that drive
                                          consideration of Touchless Install of Cluster or Fresh Install with Data Import. | Note | This installation method is applicable only for VMware vSphere ESXi. |
| Note | This installation method is applicable only for VMware vSphere ESXi. |
| Fresh Install with Data Import | Note This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. Perform direct migration of either a single node or an entire cluster, using similar mechanisms as Prime Collaboration Deployment
                                          Migration task but native to Unified Communications Manager and IM and Presence. To directly migrate a cluster, follow the Install with Data Import tasks: On each cluster node, export your old version's data. For each cluster node, provision a new virtual machine for your new version and follow either Attended Install or Touchless
                                                Install for a single node or the cluster node(s) of interest. Using the Data Import options available in Install Wizard and/or
                                                the Unified Communications Answer File Generator. You can use this method with any of the software media options available for Attended Install. Use this method for "native" direct migrations that don't require a separate management application like Prime Collaboration
                                          Deployment. You can have more granular control over individual nodes migration timing and sequencing. You may also use this
                                          method to avoid use of application readdress and temporary extra hardware footprint for direct migration. | Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Add a Node Install for cluster expansion | Note This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. If you want to add a node to an existing Unified Communications Manager or IM and Presence Service cluster for attended or
                                          touchless installation, complete the tasks in: Add a New Node to an Existing Cluster | Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

| Note | Use this method when manual installation without automation is acceptable, such as labs or small deployments. |
|---|---|

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

| Note | This installation method is applicable only for VMware vSphere ESXi. |
|---|---|

| Note | This installation method is applicable only for VMware vSphere ESXi. |
|---|---|

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

| Note | This guide provides the general installation procedures for Unified Communications Manager. If your deployment integrates Unified CM with other Cisco solutions, such as Unified Contact Center Enterprise (UCCE), review
                                          the installation and upgrade documentation for each product. This ensures that you meet all integration requirements across
                                          platforms. For example, if you are integrating Unified CM with Cisco Contact Center, also refer to the Contact Center Enterprise Installation and Upgrade Guide . |
|---|---|

| Note | By default, if your system is in non-FIPS mode, you must enable it, if desired. Ensure that the security password length is a minimum of 14 characters before you enable FIPS, Common Criteria, or Enhanced
                                                Security mode on the cluster. Update the password even if the prior version was FIPS enabled. |
|---|---|

| Note | Do not run Network Address Translation (NAT) or Port Address Translation (PAT) between servers where you are installing the
                                          Unified Communications Manager. |
|---|---|

| Note | Ensure that the network interface card (NIC) speed and duplex settings on the switch port are the same as those that you plan
                                          to set on the new server. For GigE (1000/FULL), you should set NIC and switch port settings to Auto/Auto ; do not set hard values. |
|---|---|

| Note | You must enable PortFast on all switch ports that are connected to Cisco servers. With PortFast enabled, the switch immediately brings a port from the blocking state into the forwarding state by eliminating
                                          the forwarding delay [the amount of time that a port waits before changing from its Spanning-Tree Protocol (STP) learning
                                          and listening states to the forwarding state]. |
|---|---|

|  | Compatible Hypervisor Major/Minor Releases with Minimum Maintenance/Patch Release |
|---|---|
|  | VMware vSphere ESXi | Cisco NFVIS-for-UC | Nutanix AHV |
| Unified Communications Manager |  |  |  |
| Release 15SU4 | 8.0 U1 7.0 U3 | 4.18.2a | AHV 10.0 + AOS/PC 7.0 |
| Releases 15 FCS through 15SU3 | 8.0 U1 7.0 U3 | Not supported | Not supported |
| IM and Presence Service |  |  |  |
| Release 15SU4 | 8.0 U1 7.0 U3 | 4.18.2a | AHV 10.0 + AOS/PC 7.0 |
| Releases 15 FCS through 15SU3 | 8.0 U1 7.0 U3 | Not supported | Not supported |
| Session Management Edition |  |  |  |
| Release 15SU4 | 8.0 U1 7.0 U3 | 4.18.2a | AHV 10.0 + AOS/PC 7.0 |
| Releases 15 FCS through 15SU3 | 8.0 U1 7.0 U3 | Not supported | Not supported |

| Component and Capacity Point | vCPU | Physical CPU Required Minimum Base Frequency | vRAM | vDisk | vNIC |
|---|---|---|---|---|---|
| Small | 2 | 2.00+ GHz | 10 GB | 1x 110 GB | 1 (1GbE+) |
| Medium | 2 | * | 12 GB | 1x 110 GB | 1 (1GbE+) |
| Large | 4 | * | 14 GB | 1x 110 GB | 1 (1GbE+) |

| Component and Capacity Point | vCPU | Physical CPU Required Minimum Base Frequency | vRAM | vDisk | vNIC |
|---|---|---|---|---|---|
| Extra Small (1000 devices) | 1 | 2.00+ GHz | 6 GB | 1x 110 GB | 1 (1GbE+) |
| Small (5000 devices) | 2 | 2.50+ GHz | 10 GB | 2x 80GB | 1 (1GbE+) |
| Medium (15,000 devices) | 4 | 2.50+ GHz | 14 GB | 2x 80GB | 1 (1GbE+) |
| Large (25,000 devices) | 6 | 2.50+ GHz | 18 GB | 2x 80GB | 1 (1GbE+) |

| Component and Capacity Point | vCPU | Physical CPU Required Minimum Base Frequency | vRAM | vDisk | vNIC |
|---|---|---|---|---|---|
| Medium VM | 2 | 2.50 GHz | 12 GB | 1x 110 GB | 1 |
| Large VM | 4 | 2.50 GHz | 14 GB | 1x 110 GB | 1 |

| Step 1 | Open a command
                                          			 prompt. |
|---|---|
| Step 2 | To ping each
                                          			 server by its DNS name, enter ping
                                             				DNS_name . |
| Step 3 | To look up each
                                          			 server by IP address, enter nslookup IP_address . |

| Note | We recommend that you disable the "Intruder/Intrusion Detection" and/or "Brut Force Attack" features during upgrade and installs
                                          because these Firewall features are known to cause upgrades and installations to fail. |
|---|---|

| Note | The Centralized IM and Presence Service cluster requires a Unified CM publisher node, for a total of seven servers in the
                                                cluster: three IM and Presence Service sub-cluster pairs (six servers) + the Unified CM publisher node. |
|---|---|

| Note | We recommend that you use a different username for the Cisco Unified Communications Operating System Administration and the
                                             Cisco Unified CM Administration interfaces. |
|---|---|

| Caution | Do not use the system application name as the Application User name. Using a system application name causes the installation
                                             to fail with an unrecoverable error during the installation of the database. System application
                                             			 names are: CCMSysUser WDSysUser CCMQRTSysUser IPMASysUser WDSecureSysUser CCMQRTSecureSysUser IPMASecureSysUser TabSyncSysUser CUCService |
|---|---|

| Note | If you plan to enable FIPS, Common Criteria, or Enhanced Security mode on any cluster, you must ensure that the security password
                                                   is at least 14 characters long. |
|---|---|

| Note | The License authorization is valid for 90 days with a renewal at least once in 30 days. The authorization will expire after
                                          90 days if it is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                          Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                          Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync. |
|---|---|

| Note | If you are upgrading Unified Communications Manager registered to Cisco Smart Software Manager from Pre-15 releases to Release
                                          15 or higher, Cisco Unified Communications Manager will not update the product version to 15 in the Cisco Smart Software Manager
                                          UI for the Product Instance. Refer to CSCwf94088 for more details. |
|---|---|

| Note | If you are upgrading Unified Communications Manager registered to Cisco Smart Software Manager Satellite from Pre-15 releases
                                          to Release 15 or higher, Cisco Unified Communications Manager will not update the product version to 15 in the Cisco Smart
                                          Software Manager UI for the Product Instance. Refer to CSCwf94088 for more details. |
|---|---|

| Note | The SME registered in Specific License Reservation (SLR) requires a minimum set of licenses reserved in CSSM while generating
                                                      an SLR authorization code. |
|---|---|

| Note | Evaluation period is before the product is registered. |
|---|---|

| Note | With the Jabber for Everyone offer, no end user licenses are required to enable IM and Presence Service functionality. For
                                             more information, see Jabber for Everyone Quick Start Guide . |
|---|---|

| Note | Because some of
                                          			 the fields are optional, they may not apply to your configuration. For example,
                                          			 if you decide not to set up an SMTP host during installation, the parameter
                                          			 still displays, but you do not need to enter a value. |
|---|---|

| Configuration Data | Description | Editable after Installation |
|---|---|---|
| Administrator
                                             						Credentials |
| Administrator Login | Specifies the name that you want to assign to the Administrator
                                          					 account. | No After
                                          					 installation, you can create additional administrator accounts, but you cannot
                                          					 change the original administrator account user ID. |
| Administrator Password | Specifies the password for the Administrator account. | Yes CLI: set password user admin |
| Application User
                                             						Credentials |
| Application User Username | Specifies the user ID for applications installed on the system. | Yes CLI: utils reset_application_ui_administrator_name |
| Application User Password | Specifies the password for applications on the system. | Yes CLI: utils reset_application_ui_administrator_password |
| Security Password |
| Security password for Unified Communications Manager | Servers in the cluster use the security password to communicate with one another. Set this password on the Unified Communications Manager publisher node, and enter it when you install each additional node in the cluster, including IM and Presence nodes. | Yes. You can change the security password on all nodes in the cluster using the following command: CLI: set password user security |
| Certificate Information |
| Organization | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| Unit | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| Location | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| State | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| Country | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality]
                                             						[state] |
| (Optional) SMTP |
| SMTP Location | Specifies the name of the SMTP host that is used for outbound
                                          					 email. You must fill in this field if you plan to use electronic
                                          					 notification. If not, you can leave it blank. | Yes In Cisco Unified Communications Operating System Administration: select Settings > SMTP and enter the IP address or Hostname in the SMTP Host Field. CLI: set smtp [host] |
| NIC Interface
                                             						Settings |
| NIC Speed | If you do not enable automatic negotiation of the ethernet
                                          					 Network Interface Card (NIC) speed, you must select the NIC speed (either 10
                                          					 megabit or 100 megabit). | Yes CLI: set network nic eth0 {auto \| {en\| dis}} {speed\| {10\| 100}} {duplex half\| {half\| full}} Note 1000BASE-T can only be enabled via
                                                      auto-negotiation. Note Virtual machines do not support this
                                                      command. | Note | 1000BASE-T can only be enabled via
                                                      auto-negotiation. | Note | Virtual machines do not support this
                                                      command. |
| Note | 1000BASE-T can only be enabled via
                                                      auto-negotiation. |
| Note | Virtual machines do not support this
                                                      command. |
| NIC Duplex | If you do not enable automatic negotiation of the ethernet
                                          					 Network Interface Card (NIC) duplex setting, you must select the NIC duplex
                                          					 setting (either Full or Half). | Yes CLI: set network nic eth0 {auto \| {en\| dis}} {speed\| {10\| 100}} {duplex half\| {half\| full}} Note 1000BASE-T can only be enabled via
                                                      auto-negotiation. Note Virtual machines do not support this
                                                      command. | Note | 1000BASE-T can only be enabled via
                                                      auto-negotiation. | Note | Virtual machines do not support this
                                                      command. |
| Note | 1000BASE-T can only be enabled via
                                                      auto-negotiation. |
| Note | Virtual machines do not support this
                                                      command. |
| MTU Size Note The
                                                      						MTU setting must be the same on all nodes in a cluster. | Note | The
                                                      						MTU setting must be the same on all nodes in a cluster. | The maximum transmission unit (MTU) represents the largest packet, in bytes, that this host transmits on the network. The value must not exceed the lowest MTU size that is configured
                                          					 on any link in your network. Default:
                                          					 1500 bytes | Yes CLI: set network mtu [size] |
| Note | The
                                                      						MTU setting must be the same on all nodes in a cluster. |
| Network Information |
| DHCP (Dynamic Host Configuration Protocol) | Select Yes if you want to use DHCP to automatically configure the
                                          					 network settings on your server. If you select No , you must enter a hostname, IP Address, IP Mask, Gateway,
                                          					 and DNS configuration. | Yes. In Cisco Unified Operating System Administration: select Settings > IP > Ethernet . CLI: set network dhcp eth0 [enable] CLI: set network dhcp eth0 disable [node_ip]
                                                   [net_mask] [gateway_ip] |
| Hostname | If DHCP is set to No, you must enter a hostname for this
                                          					 machine. | Yes; for Unified Communications Manager nodes, choose one of the following: In Cisco Unified Communications Operating System Administration, select Settings > IP > Ethernet . CLI: set network hostname You will be prompted to enter the parameters. To change the hostname on Unified Communications Manager or IM and Presence server, see the 'IP Address, Hostname, and Domain Name Changes' section in the Administration Guide for Cisco Unified Communications Manager . |
| IP Address | If DHCP is set to No, you must enter the IP address of this
                                          					 machine. | Yes; for Unified Communications Manager nodes, choose one of the following: In Cisco Unified Communications Operating System Administration, select Settings > IP > Ethernet . CLI: set network IP eth0 [ip-address] [ip-mask] To change the IP address on Unified Communications Manager or IM and Presence server, see see the 'IP Address, Hostname, and Domain Name Changes' section in the Administration Guide for Cisco Unified Communications Manager . |
| IP Mask | If DHCP is set to No, you must enter the IP subnet mask of this
                                          					 machine. The subnet mask together with the IP address defines the network
                                          					 address and the host address. The
                                          					 subnet mask must use the following format: 255.255.255.0 | Yes In Cisco Unified Communications Operating System Administration, select Settings > IP > Ethernet . CLI: set network IP eth0 [ip-address] [ip-mask] |
| Gateway Address | If DHCP is set to No, you must enter the gateway address. | Yes In Cisco Unified Communications Operating System Administration, select Settings > IP > Ethernet . CLI: set network gateway [addr] |
| (Optional) DNS |
| DNS Primary | If you have a Domain Name Server (DNS), IM and Presence contacts this DNS server first when
                                          					 attempting to resolve hostnames. | Yes CLI: set network dns primary [address] |
| DNS Secondary | When a primary DNS server fails, IM and Presence will attempt to connect to the
                                          					 secondary DNS server. | Yes CLI: set network dns secondary [address] |
| Domain | Represents the name of the domain in which this machine is
                                          					 located | Yes CLI: set network domain [name] |
| Timezone |
| Time Zone | Reflects the local time zone and offset from Greenwich Mean Time
                                          					 (GMT). Select the time zone that most closely matches the location of your
                                          					 machine. | Yes CLI: set timezone [zone |
| Network Time Protocol |
| NTP Server IP Address | During installation of the IM and Presence publisher node, you must specify the IP address of an external Network Time Protocol (NTP) server. We recommend that you
                                          use the Unified Communications Manager publisher node as the NTP server. | Yes In Cisco Unified Communications Operating System Administration, select Settings > NTP Servers . |

| Note | 1000BASE-T can only be enabled via
                                                      auto-negotiation. |
|---|---|

| Note | Virtual machines do not support this
                                                      command. |
|---|---|

| Note | 1000BASE-T can only be enabled via
                                                      auto-negotiation. |
|---|---|

| Note | Virtual machines do not support this
                                                      command. |
|---|---|

| Note | The
                                                      						MTU setting must be the same on all nodes in a cluster. |
|---|---|

| Note | Unrestricted versions of software are intended only for a specific set of customers who do not want various security capabilities;
                                       unrestricted versions are not intended for general deployments. |
|---|---|

| Note | Be aware that after you install an unrestricted release, you can never upgrade to a restricted version. You are not allowed
                                       to perform a fresh installation of a restricted version on a system that contains an unrestricted version. |
|---|---|

| GUI Item | Location | Description |
|---|---|---|
| Cisco Unified CM Administration |
| VPN Configuration | Advanced Features > VPN | This menu and its options are not available. |
| Phone Security Profile Configuration | System > Security > Phone Security Profile | The Device Security Mode is set to Non Secure and is not configurable. |
| Cisco
                                             						Unified CM IM and Presence Administration |
| Security Settings | System > Security > Settings | You
                                                						cannot check the Enable XMPP Client to IM/P Service Secure Mode setting. You
                                                						cannot check the Enable XMPP Router-to-Router Secure Mode setting. You
                                                						cannot check the Enable Web Client to IM/P Service Secure Mode setting. The option to set SIP intra-cluster Proxy-to-Proxy Transport Protocol to TLS have been removed. |
| Service Parameter Configuration for Cisco SIP Proxy service | System > Service Parameters and choose Cisco SIP Proxy as the Service | All TLS
                                                						options have been removed for the Transport Preferred Order parameter. The TLS option have been removed from the SIP Route Header Transport Type parameter. |
| SIP Federated Domains | Presence > Inter-domain
                                                						  Federation > SIP Federation | When you
                                          						configure interdomain federation to OCS/Lync, you will receive warning popup to
                                          						indicate that it is only possible to directly federate with another OCS/Lync
                                          						within the enterprise. Interdomain federation to OCS/Lync outside the
                                          						enterprise is not supported in unrestricted mode. |
| XMPP Federation Settings | Presence > Inter-domain
                                                						  Federation > XMPP Federation > Settings | You cannot configure the security mode. It is set to NO TLS . |
| Proxy Configuration Settings | Presence > Routing > Settings | You
                                          						cannot set any TLS or HTTPS listeners as the preferred proxy listener. |