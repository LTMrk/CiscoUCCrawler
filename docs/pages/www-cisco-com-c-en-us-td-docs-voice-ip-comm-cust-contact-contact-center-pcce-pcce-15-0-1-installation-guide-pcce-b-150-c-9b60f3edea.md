---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-installation-guide-pcce-b-150-c-9b60f3edea
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/installation/guide/pcce_b_150_cisco_pcce_installationandupgrade_guide/pcce_m_150_migration-vmware-to-nutanix.html
retrieved_at: 2026-08-21T12:09:16.116840+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Migration from VMware to Nutanix

## Chapter: Migration from VMware to Nutanix

# Migration from VMware to Nutanix

## Introduction

This chapter describes the prerequisites, procedures, and post-configuration required to migrate the Cisco Packaged Contact Center Enterprise (Packaged CCE) and its components from VMware to Nutanix.

This section is organized into component-specific sections for Windows-based and VOS-based components.

The common procedures for VOS-based components describe how to export platform data from components deployed on VMware and
                           perform a fresh installation with import on Nutanix.

The VOS platform sections provide migration procedures for each supported VOS component.

The Windows platform section covers migration of the following components, as described in existing Cisco documentation.

Migrating CCE components using Technology Refresh upgrade or Nutanix Move.

Migrating Cisco Unified Customer Voice Portal (Unified CVP) using export and import data procedures or Nutanix Move.

Migrating Cisco Enterprise Chat and Email (ECE) and Cisco Unified Contact Center Management Portal (Unified CCMP) using data
                                 migration procedures.

### Nutanix Support for CCE Components

CCE Windows-based Components:

Packaged CCE components and Unified CVP are supported on Nutanix with version 15.0(1).

ECE and Unified CCMP are supported on Nutanix with 15.0(1) ES202511 or later.

CCE VOS-based Components:

Cisco Cloud Connect (Cloud Connect), Cisco Finesse (Finesse), Cisco Virtualized Voice Browser (Cisco VVB), and Cisco Unified
                                 Intelligence Center (Unified Intelligence Center) are supported on Nutanix starting with the 15.0(1) SU2 release.

#### VOS Platform Components

Migration Method: Migration is supported using the Fresh Install with Import option introduced in the 15.0(1) SU2.

Migration Process: CLI in 15.0(1) ES202511 or 12.6(2) with the latest ES (for more specific ES information, see the System Requirements section) allows administrators to export platform data and application data from components deployed on VMware to an SFTP
                                          server. This data is then imported into the components deployed on Nutanix. For more information, see the sections for the
                                          respective components.

Frequency of Data Migration:

Data migration is a two-step process. For each VOS-based component, migrate the platform data first, followed by the application data.

Platform data migration is a one-time event during component deployment on Nutanix. Application data can be exported from
                                                VMware and imported after deployment on Nutanix, and prior to or during the production cutover.

#### CCE Windows-based Components

Unified CCE components that run on Windows can be migrated from VMware to Nutanix by using the Technology Refresh procedure.

For more information, see the Technology Refresh Upgrade Process chapter.

Alternatively, Unified CCE and Unified CVP components that run on Windows can be migrated by using Nutanix Move, a virtual-to-virtual
                                    (V2V) migration tool. For Nutanix Move concepts, prerequisites, and procedures, see Nutanix Move Migration

## Important Considerations

### System Requirements

The source versions in the following table identify the VMware releases from which data can be exported.

CCE Components

Source (VMware) Version

Nutanix target version

Supported 15.0(1) VMware source version

Supported 12.6(2) VMware source version

CCE VOS-based Components

Cloud Connect

15.0(1) with ES202511

15.0(1) SU1

15.0(1) SU2

12.6(2) ES 04

15.0(1) SU2

Finesse

15.0(1) with ES202511

15.0(1) SU1

15.0(1) SU2

12.6(2) ES 07

Cisco VVB

15.0(1) with ES202511

15.0(1) SU1

15.0(1) SU2

12.6(2) ES 08

Unified Intelligence Center

Cisco Live Data

Cisco Identity Service (Cisco IdS)

15.0(1) with ES202511

15.0(1) SU1

15.0(1) SU2

12.6(2) ES 08

CCE Windows-based Components

Unified CCE

15.0(1) with ES202607 or later

12.6(2) with

ES 102 on AW, ES 108 on PG, ES 103 on Router, Logger, & Rogger

15.0(1) with ES202607 or later

Unified CVP

12.6(2) with ES 25 or later

ECE

12.6(1) ES 13 or later

Unified CCMP

12.6(1) ES 15 or later

For more information about installing an Engineering Special on 12.6(2) or 15.0(1), see the Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1) .

### Nutanix Requirements

Nutanix Cluster

Design the Nutanix Cluster with an appropriate number of servers in the cluster based on the CCE deployment VM specification
                                       and Nutanix specific system requirements.

Nutanix recommends a minimum of three servers per cluster to facilitate future expansion of the number of servers in the cluster.

Cisco recommends deploying the Side A and Side B CCE components on separate independent single-node Nutanix clusters.

Cisco recommends using Nutanix Prism Central, a centralized multicluster management platform, to manage the Nutanix Cluster.

Nutanix Specification

For details on the Nutanix software and the versions that Cisco validated with the CCE 15.0(1) release, see the Hypervisor
                                 Compatibility section in the Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) .

TCP Port 9440 is the default port used by Nutanix Prism Central for management of traffic, including web console access (HTTPS), REST API
                                             calls, and communication between Prism Element and Prism Central.

For more information, see the following Nutanix documentation:

AHV Administration Guide

Prism Central Guide

The administrator should be familiar with building and managing Nutanix clusters, deploying VMs on Nutanix clusters, and using
                                             Nutanix tools and technologies.

#### AHV Dynamic Scheduling and VM-to-Host Affinity

Cisco recommends using Nutanix Acropolis Dynamic Scheduler (ADS) for automatic workload balancing across AHV hosts. If you disable ADS to avoid automatic VM rebalancing and use VM-to-host
                                 affinity or configure VMs with CPU passthrough, be aware that appliances pinned to specific AHV hosts might fail during AHV
                                 upgrades or Virtual Machine High Availability (VMHA) events.

To ensure high availability when ADS is disabled, configure VMHA with VM-to-host affinity rules that span multiple AHV hosts:

For Replication Factor 2 (RF2), configure VM-to-host affinity rules for at least two AHV hosts to provide one-host failure
                                       tolerance.

For Replication Factor 3 (RF3), configure VM-to-host affinity rules for at least three AHV hosts to provide two-host failure
                                       tolerance.

This configuration allows VMHA to restart VMs on alternate hosts if a failure occurs. Manage affinity rules using Nutanix
                                 Prism Central. Cisco advises against pinning appliances to a single AHV host without appropriate affinity rules because doing
                                 so can cause failures during maintenance or failover. This approach balances workload mobility, strict VM placement control,
                                 and high availability.

### Hardware for Nutanix Deployment

Cisco validates the CCE 15.0(1) release on Cisco Compute Hyperconverged with Nutanix (CCHN) using Cisco UCS C220 M7N servers.

Supported Deployment Types:

We provide the following Cisco recommendations to optimize costs for running Nutanix Unified CCE deployments:

Unified CCE 2000 Agent Deployments : Use a single-node (ROBO/Edge) Nutanix solution with NCI Edge licensing. License only the required VMs, configured with Replication
                                    Factor 2 (RF2) across the drives of a single node.

Remote Sites : Use a single-node (ROBO/Edge) Nutanix solution with NCI Edge licensing. License only the required VMs, configured with Replication
                                    Factor 2 (RF2) across the drives of a single node.

Packaged CCE 4000 Agent Deployment and above : Use a 3+ node Nutanix solution (minimum 5 nodes for Replication Factor 3 (RF3)) with NCI Core licensing.

### SFTP Server

SFTP server is used for exporting and importing data between CCE VOS components deployed on VMware and Nutanix.

SFTP servers need to be accessible from both VMware and Nutanix deployments.

SFTP server should be configured with well-known strong cryptographic algorithms.

### Access and Permissions

To perform CCE migration from VMware to Nutanix, administrator privilege is required for accessing CLI and data migration. Refer to respective component sections for details.

### Backup Recommendation

Cisco recommends you take backup of the components as part of migration from VMware to Nutanix.

CCE on VMware:

Before exporting platform and application data, take a Disaster Recovery System (DRS) backup of each CCE VOS-based component.

CCE on Nutanix:

CCE Windows Components: Create recovery point on Nutanix (VM Snapshot).

Uninstallation of the Unified CCE base installation on Windows Server is not supported for Release 15.0(1). This limitation
                                                   does not apply to Unified CCE client packages, which can be removed and reinstalled. For more information, see the Uninstallation
                                                   chapter of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) .

CCE VOS Components:

Create a recovery point on Nutanix (VM Snapshot) after performing the platform migration to 15.0(1) SU2 using the Fresh Install with Import option, and before initiating the component application data migration.

Recovery Point

Create a recovery point on Nutanix (VM Snapshot) after performing the platform migration to 15.0(1) SU2 using the Fresh Install with Import option, and before initiating the component application data migration.

For UEFI Secure Boot requirements and initial VM boot behavior, see CCE Virtualization OVA .

#### DRS Backup Recommendations for VOS-based Components

Following are the important considerations when you perform the backup and restore procedures:

Before you run a backup or restore, ensure that all nodes in the cluster are running the same version of the VOS-based component.
                                       If different nodes are running different versions, you will have a certificate mismatch and your backup or restore fails.

Before restoring a VOS-based component, ensure that its hostname, IP address, DNS configuration, and deployment type match
                                       the corresponding values in the backup file.

Before you restore a VOS-based component, ensure that the version that is installed on the server matches the version of
                                       the backup file that you want to restore. Cisco DRS supports restore only for matching versions.

Schedule backups during off-peak hours to avoid call-processing interruptions and impact to service.

After you use the recovery disk to bring a server with a corrupted file system into a bootable and semi- functional state,
                                       rebuild the server.

If you do not rebuild the server, you may notice missing directories, lost permissions, or corrupted soft links.

For details on how to perform the backup, see the Backup Procedure Taskflow topic in the Tools chapter of the Administration Console User Guide for Cisco Unified Intelligence Center, Release 15.0(1) .

### Migration Planning and Preparation

Before beginning a migration from VMware to Nutanix, a comprehensive migration plan must be established.

A critical component of the migration plan is determining the deployment strategy:

Nutanix Cluster: Nutanix clusters for deploying CCE must be configured and ready.

IP and Hostname Strategy: Decide whether to reuse existing IP addresses and hostnames on the Nutanix platform or assign new ones.

Impact on Workflow: The decision to use the same or different IP addresses and hostnames will dictate specific additional steps required during
                                    the migration process as detailed in the respective component sections of this guide.

## CCE Virtualization OVA

Cisco has published OVAs for deploying CCE components on Nutanix. Use the appropriate OVA for the planned CCE deployment on
                           Nutanix.

There are no changes to resource requirements between the standard 15.0(1) release and the Nutanix-specific OVAs.

Nutanix does not support multiple deployment options within a single OVA file; the existing multi-option OVAs have been split
                                 into multiple, individual OVA files for Nutanix deployments.

CCE Components

Download Link

OVA

Cloud Connect

Download Cloud Connect OVA

CloudConnect_15.0.1-SU2_nutanix_v.3.0.zip

Unified CVP

Download Unified CVP OVA

CVP_15.0.1_nutanix_OVAPack_v3.0.zip

Cisco VVB

Download Cisco VVB OVA

vvb-15.0.1-SU2-nutanix_v3_OVAs.zip

Finesse

Download Finesse OVA

Finesse_15.0.1-SU2_nutanix_OVAPack_v3.0.zip

Cisco IdS

Download Cisco IdS OVA

cuic-ova-15.0.1-SU2-nutanix.zip

ECE

Download ECE OVA

ECE_15.0_Nutanix_v3.0_OVAs.zip

Unified CCMP

Download Unified CCMP OVA

Nutanix_CCMP_OVAs-v3.0.zip

Unified Intelligence Center

Download Unified Intelligence Center and Live Data OVAs

cuic-ova-15.0.1-SU2-nutanix.zip

Live Data

tempesta-ova-15.0.1-SU2-nutanix.zip

Logger, Router, Rogger, Administration and Data Server, PG, Administration Client

Download Unified CCE OVAs

UCCE_15.0.1_Nutanix_v3.0_OVAs.ova.zip

Starting with OVA version 2.0, Nutanix Rogger, Router, Logger, AW, PG OVAs use UEFI BIOS with Secure Boot enabled. This introduces
                           a one-time user interaction during the initial VM power-on. When the VM is powered on, the console displays a "Press any key
                           to continue" prompt before the operating system installation begins.

If the key press is not registered (for example, due to console latency), use Ctrl + Alt + Delete from the VM console to restart the VM, and press any key when the prompt appears again.

On Nutanix, the VM boot mode (Legacy or UEFI) cannot be changed after VM creation. If a VM was created using Legacy BIOS and
                                       UEFI Secure Boot is required, the VM must be deleted and recreated using the appropriate OVA and boot settings.

## Preinstallation

Before you Install Virtual machines on Nutanix for CCE solution, complete the following sections.

Sequence

Task

1

Upload OVA to Nutanix

2

Upload Images to Nutanix

3

Create a Virtual Machine from the OVA on Nutanix

4

Set Up Third-Party Software

5

Setup Nutanix Move

### Upload OVA to Nutanix

To upload OVA to Nutanix, perform the following:

Step 1

Log in to Prism Central with admin privileges.

Step 2

From the Application Switcher , select Infrastructure , and then navigate to Compute > OVAs from the navigation bar.

Step 3

Click Upload OVA .

Step 4

Specify the following field information in the Upload OVA screen:

Step 5

OVA Source : Select the OVA source. To upload OVA, there are 2 options available:

- OVA file (upload a file from the local folder)

- URL : If you choose URL in the OVA Source field, you can select multiple clusters in the Select AHV Cluster field.

Step 6

Name : Enter the name for the OVA file.

By default, Prism Central uses the file name of the OVA file that you upload, if you do not specify OVA file name in the Name
                                             field.

Step 7

Based on the selection in the OVA Source field, perform the following relevant action:

OVA file : Click Select File to navigate to the location of the OVA file in your local folder and open it.

URL : Enter the source URL from where you want to upload the OVA file.

#### What to do next

For more information on Uploading an OVA, see the Prism Central Infrastructure Guide . You need Nutanix Support Portal login to access this document.

### Upload Images to Nutanix

To upload images to Nutanix, perform the following steps:

Step 1

Log in to Prism Central as a user with admin privileges.

Step 2

Choose the Infrastructure application from the Application Switcher, and navigate to Compute > Images from the navigation bar.

Step 3

Click Add Image . The system displays the Add Images screen.

Step 4

Provide the following information in the Select Image step:Image Source - Select the Image File radio button.

Step 5

Click Add File . The system displays file attributes.

Step 6

Browse the location of the image file, and then click Open .

Step 7

Provide the following attributes for the image file:

Step 8

Image Name - Enter the image name. By default, the system pre-fills the name of the file you selected; however, you can change
                                          the image name as per your requirement.

Image Type - Select the type of image.

Image Description - Enter the description for the image file.

Step 9

Repeat the step if you want to add multiple image files.

Step 10

Click Next after you add all the image files. The system displays the Select Location step.

Step 11

Provide the following information in the Select Location step:

Step 12

Choose Place image directly on clusters to place the images directly on the selected clusters.

Step 13

Select the clusters where you want to add the image file in the Name column.

Step 14

Click Save .

The system adds the image files in batches to the selected clusters.

#### What to do next

For more information, see the Adding Images from a Workstation guide . You need Nutanix Support Portal login access to refer to this document.

### Create a Virtual Machine from the OVA on Nutanix

To create a VM using OVA, perform the following:

Step 1

Log in to Prism Central.

Step 2

From the Application Switcher, select Infrastructure, and then navigate to Compute > OVAs from the navigation bar.

Step 3

Select the target OVA and choose Deploy as VM from the Actions dropdown menu. The system displays the Deploy as a VM screen.

For more information on Uploading an OVA, see the Prism Central Infrastructure Guide . You need Nutanix Support Portal login access to refer to this document.

Step 4

In the Deploy as VM screen, specify the following information in the Configuration step:

Name : Enter the name of the VM that needs to be deployed.

Description : Enter that description such as Backup VM for Prism.

Cluster : Select the target cluster on which you intend to place the guest VM.

Step 5

Click Next . The system displays the Resources step.

Step 6

In the Resources step, go to the Normal NIC (network) section and click Edit (the three-dot icon on the right side of the table). Select the
                                          subnet on which the VM will be deployed, and attach the VM to the appropriate virtual network (VLAN).

Step 7

Click Next . The system displays the Management step.

Step 8

Click Next . The system displays the Review step.

Step 9

Review the deployment configuration in the Review step, and click Create VM .

You can check the progress of the deployment task in the Tasks page or from the Tasks icon.

Step 10

After the VM creation is complete, select the VM and click the Disks tab.

Step 11

Select the first CD-ROM device, and under Operation, choose Clone from Image .

Step 12

(For VOS-based components only) Select the required component ISO image from the Image drop-down list.

Step 13

(For Windows-based components only) Select the Windows operating system ISO image from the Image drop-down list.

Step 14

(For Windows based components only) Select the second CD-ROM device, choose Clone from Image, and select the Nutanix VirtIO driver ISO from the Image drop-down list.

For more information, see the Adding Images from a Workstation guide . You need Nutanix Support Portal login access to refer to this document

Step 15

Power on the VM.

For more information on Deploying an OVA as VM, see the Prism Central Infrastructure Guide . You need Nutanix Support Portal login access to refer to this document.

### Set Up Third-Party Software

Step 1

Install Microsoft Windows Server

Step 2

Install Microsoft Windows 11 for Administration Client

Step 3

Install Microsoft SQL Server

#### Install Microsoft Windows Server

Complete the following procedure to install Microsoft Windows Server on the virtual machines deployed for CCE and Unified
                                    CVP components.

Note: For information about supported editions, see the Contact Center Enterprise Compatibility Matrix.

Step 1

Select the VM where the Microsoft operating system installation is triggered.

Step 2

Click Launch Console .

The Windows console opens in a new window.

Step 3

Select the desired language, time and currency format, and keyboard information.

Step 4

Click Next > Install Now .

Step 5

If prompted, enter the product key for Windows Server and click Next .

Step 6

Select the Desktop Experience option for Windows Server and click Next .

Step 7

Accept the license terms and click Next .

Step 8

Click Next > Custom: Install Windows only (advanced) > Load Driver > OK > Browse .

Step 9

Choose the Nutanix VirtIO driver.

Step 10

Select the Nutanix VirtIO CD drive.

Step 11

Expand the Windows OS folder and click OK .

The Select the driver to install window appears.

Step 12

Select all the drivers shown on the Windows Setup screen and click Next .

The amd64 folder contains drivers for 64-bit operating systems. The x86 folder contains drivers for 32-bit operating systems.

Step 13

Select the allocated disk space for the VM and click Next .

Step 14

Enter and confirm the password for the administrator account, and then click Finish .

Step 15

Enable Remote Desktop connections as follows:

Step 16

Navigate to Control Panel > System and Security > System .

Step 17

Click Remote Settings .

Step 18

Click the Remote tab.

Step 19

Select the Allow remote connections to this computer radio button. The Remote Desktop Connection dialog displays a notification that the Remote Desktop Firewall exception is
                                             enabled.

Step 20

Click OK .

Note: If you are installing Windows SQL Server 2022, instead of Remote Settings, click Remote Desktop . Toggle the Enable Remote Desktop button. Click the Confirm button on the Remote Desktop settings pop-up box. Click Ok .

Step 21

Open the Network and Sharing Center and Click Ethernet in the View your active network info and set up connections section.

Step 22

In the Ethernet Status window, click Properties .

Step 23

In the Ethernet Properties dialog box, configure the following network settings and the Domain Name System (DNS) data:

Uncheck Internet Protocol Version 6 (TCP/IPv6) .

Select Internet Protocol Version 4 (TCP/IPv4) and click Properties .

Select Use the following IP Address .

Enter the IP address, subnet mask, and default gateway.

Select Use the following DNS Server Address .

Enter the preferred DNS server address and click OK .

Step 24

Navigate to Control Panel > System and Security > System . Follow the instructions:

Step 25

Click Change Settings .

Note: If you are installing Windows SQL Server 2022, click Rename this PC (advanced) .

Step 26

In the Computer name tab, click Change .

Step 27

Change the name of the computer from the name randomly generated during Microsoft Windows Server installation. The name does
                                             not contain underscores or spaces.

Step 28

Select Domain radio button to change the member from Workgroup to Domain.

Step 29

Enter qualified domain name and click OK .

Step 30

In the Windows security dialog, validate the domain credentials and click OK .

Step 31

Click Ok on successful authentication.

Step 32

Reboot the server and sign in with domain credentials.

Step 33

Go to Settings > Update & Security and run Microsoft Windows Update.

##### What to do next

Note: Edge Chromium (Microsoft Edge) is not installed by default on the Windows server. To install Edge Chromium (Microsoft Edge),
                                    see Microsoft documentation.

#### Install Microsoft Windows 11 for Administration Client

For more information, see the Install Microsoft Windows 11 for Administration Client section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

Perform the following additional steps to install Microsoft Windows 11 on Nutanix AHV. After completing Steps 1 through 7 in the Install Microsoft Windows 11 for Administration Client section, perform the following steps to ensure that the virtual
                                    disk drive is recognized:

Step 1

On the screen, Where do you want to install Windows , click Load Driver .

Step 2

Click Browse and navigate to the Nutanix VirtIO ISO (mounted as a second CD-ROM).

Step 3

Navigate to w11\amd64 and click OK .

Step 4

Select all the drivers and click Next .

##### What to do next

Once the disk appears, proceed with the remaining instructions from Step 8 of the Install Microsoft Windows 11 for Administration Client section.

#### Install Microsoft SQL Server

For more information, see Install Microsoft SQL Server

### Setup Nutanix Move

1

Download Nutanix Move

2

Deploy the Nutanix Move VM

3

Change the Default Password

4

Assign a Static IP Address

5

Log In to the Nutanix Move Console

6

Add Migration Environments

## Platform Data Migration Common Procedures for VOS-based Components

This following section provides procedure to perform Platform data migration for VOS based components such as Cloud Connect,
                              Finesse, Cisco VVB, Live Data, Cisco IdS, and Unified Intelligence Center from VMware to Nutanix.

Before starting the platform-data migration, record any customized client and server cipher lists, TLS-version settings, and
                                          certificate-type settings on the source node. Depending on the source release and whether the destination uses the same hostname
                                          and IP address, these settings might not be retained. After importing the platform data, verify and reapply the applicable
                                          settings on the destination node.

Sequence

Task

1

Export Platform Data from the Source VM to the Remote Server

2

Shutdown the Source VM(s)

3

Fresh Install VM with Import option on Nutanix Using Exported Platform Data

### Export Platform Data from the Source VM to the Remote Server

#### Before you begin

Before exporting platform data, record the following customized security settings on each source node being migrated:

Client cipher list

Server cipher list

client_tls_versions

server_tls_versions

cert_type , if it is configured with a value other than RSA

Use the recorded values (see Note in previous topic) to verify and, if required, restore the settings on the destination node
                                 after importing the platform data.

Step 1

Log in to the command-line-interface of the Source VM and run the following command:

Step 2

Enter the following SFTP server details:

Export Data Directory

Remote Server Name or IP

Remote Server Login ID

Remote Server Password

Step 3

Enter the following details of Nutanix destination VM:

New Hostname

New IP Address

Step 4

When prompted, enter yes to start the export operation.

Primary or standalone node:

During the export, the system automatically creates a directory on the remote server using the following format and copies
                                                   the exported platform data into it:

cluster-<source-IP-address>

Secondary node (if applicable):

After the primary-node export is complete, log in to the secondary node and repeat this procedure, beginning with utils system upgrade dataexport initiate . At the Export Data Directory prompt, enter the same directory path that you specified during the primary-node export. The subscriber platform data is
                                                   added to the directory created during the primary export:

The secondary-node platform data export fails if you specify a different Export Data Directory.

Step 5

To check whether the data export is complete or in progress, run the following command:

### (Optional) Shutdown the Source VM(s)

Perform this step only if the source and destination VMs are configured with the same IP address and are reachable on the
                              same network, to prevent an IP address conflict.

Shut down the source VM(s) after successful completion of the platform and component data export operation and power on the
                              respective destination VM(s) to prevent IP conflicts. For each component's data export procedure, see that component's topic
                              under Contact Center Enterprise Components Migration from VMware to Nutanix . To shut down the system, run the following command:

utils system shutdown

Consider the following points. They apply to all VOS-based components except the standalone Cisco VVB component:

After the primary VM is shut down, secondary nodes operate in a primary-unreachable state. No new cluster formation occurs
                                                during this period.

Before shutting down the primary VM, ensure that Maintenance Mode (MM) is initiated and successfully completed on all supported
                                                components, such as Finesse and Cisco IdS.

You do not need to shut down all secondary VMs in the cluster together. Shut down only the secondary VMs on which you are
                                                performing a fresh installation with import (migration) .

### Fresh Install VM with Import option on Nutanix Using Exported Platform Data

To perform a Fresh Install with Import for a standalone, primary, or secondary node, complete the following steps:

Fresh Install with Import Using an Answer File

To perform a Fresh Install with Import for a VOS-based component by using an answer file, open the Cisco Unified Communications Answer File Generator . In Software Location of Data to Import , select Configure Software Location of Data to Import , enter the remote SFTP server and export-data directory details, and generate the answer file for the destination component.

Step 1

Create a Virtual Machine using the OVA Template. Mount the 15.0(1) SU2 bootable image to the Virtual Machine (VM) and power
                                             on the VM. For more information, see the following sections in this guide:

Upload OVA to Nutanix

Upload Images to Nutanix

Create a Virtual Machine from the OVA on Nutanix

Step 2

Click OK after the media check succeeds.

Step 3

Choose the applicable VOS component and click OK .

Step 4

Click Yes to proceed with installation of the 15.0(1) SU2 build version.

Step 5

Click Import in the Platform Installation Wizard.

Step 6

After reading the displayed information, click OK in the Import Upgrade Configuration information.

Step 7

Choose the appropriate time zone and then click OK .

Step 8

Click Continue in the Auto Negotiation Configuration

Step 9

Click No to have the default value in MTU Configuration .

Step 10

Click No under DHCP Configuration .

Step 11

Provide the same Host Name and IP Address that was used during the export platform data operation; enter IP Mask and Gateway
                                          (GW) Address and then click OK . The destination hostname and IP address can differ from those of the source VM.

Step 12

Click Yes under the DNS Client Configuration .

Step 13

Provide the Primary DNS server's IP Address and Domain and then click OK .

Step 14

Enter the SFTP server IP address, the complete path to the exported platform-data directory, the login ID, and the password.
                                          Specify the platform-data directory in the following format:

Then click OK .

Step 15

Provide the organization information on the Certificate Information page and click OK .

During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                         and IP address as the source:

Same hostname and IP address: All source certificates are migrated, including:

Tomcat RSA and ECDSA certificates

Tomcat trust certificates

IPsec and IPsec trust certificates

CA-signed certificates, including root and intermediate CA certificates

Component certificates uploaded to the Tomcat trust store

Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x.

Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                               source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname.

The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                               issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management .

Verify the certificates on the destination node to ensure that all required trust relationships are established.

Step 16

For a standalone node such as Cisco VVB, skip this step. In the First Node Configuration screen, specify whether you are configuring the first node based on the following:

- If you are installing the primary node, click Yes under First Node Configuration .

If you are installing the secondary node, click No under First Node Configuration . A warning message states that you must configure the first node before continuing. If the first node is already configured,
                                                   click OK . On the Network Connectivity Test Configuration page, click No to proceed with the installation after connectivity is verified. Enter the primary hostname and IP address on the First Node Access Configuration page and click OK .

Step 17

For a secondary node, skip this step. Configure the Network Time Protocol (NTP) server and then click Proceed .

Step 18

On the SMTP Host Configuration screen, choose one of the following:

- To configure an SMTP host during installation, click Yes and enter the SMTP host information.

- To continue without configuring an SMTP host, click No .

Step 19

On the Platform Configuration Confirmation page, click OK .

#### What to do next

After successful installation, you can run the following commands:

To check the current version of the VOS-based component and verify the installation is successful, run the following command:

The displayed version is the 15.0(1) release version of the component that you installed . The following example shows Cloud Connect 15.0(1) SU2:

```
admin:show version
        active
 Active Master Version: 15.0.1.10200-97 Active Version Installed Software
        Options:
 No Installed Software Options Found.
```

To check the dbreplication state, run the following command and if the replication is successful the output will display "Setup
                                       Completed ":

Not applicable for single-node publisher-only systems. If the command is run on these systems, the following error message
                                                   will be displayed:

To check the system history and validate if the import is successful, run the following CLI command:

If the import is successful, the command output will display the following (the highlighted line indicates a successful import
                                       and shows the version numbers of the source and the destination):

The following output is from Cisco Unified Intelligence Center (CUIC). Output details vary by VOS-based component and release.

```
admin:show version active
Active Master Version: 15.0.1.10100-41
Active Version Installed Software Options:
No Installed Software Options Found.
admin:file view install system-history.log

=======================================
Product Name - Cisco Unified Intelligence Center with Live Data and IdS
Product Version - 15.0.1.10100-41
Kernel Image - 4.18.0-553.22.1.el8_10.x86_64
=======================================
02/23/2026 13:21:59 | root: Install 15.0.1.10100-41 Start
02/23/2026 13:33:28 | root: Boot 15.0.1.10100-41 Start
02/23/2026 14:20:09 | root: Import during Install 15.0.1.10000-196-to-15.0.1.10100-41 Success
02/23/2026 14:20:09 | root: Product Version 15.0.1.10100-41
02/23/2026 14:20:09 | root: Kernel Image 4.18.0-553.22.1.el8_10.x86_64
02/23/2026 14:20:09 | root: Restart 15.0.1.10100-41 Start
02/23/2026 14:21:46 | root: Boot 15.0.1.10100-41 Start
02/23/2026 14:22:42 | root: Restart 15.0.1.10100-41 Start
02/23/2026 14:24:27 | root: Boot 15.0.1.10100-41 Start
```

Verify and restore customized security settings

Verify and restore the applicable security settings on the destination node:

Custom cipher lists: Custom client and server cipher lists are not migrated. Configure the values recorded from the source node.

TLS-version settings: The server_tls_versions and client_tls_versions settings are preserved when migrating from 15.0(1) SU2 to 15.0(1) SU2. When migrating from 12.6(2), 15.0(1), or 15.0(1) SU1
                                             to 15.0(1) SU2, configure the values recorded from the source node.

Certificate type: For migrations from 12.6(2), 15.0(1), or 15.0(1) SU1, verify cert_type on the destination node. If the source and destination use the same hostname and IP address and the source used a certificate
                                             type other than RSA, manually restore the source cert_type setting.

For migrations from 15.0(1) SU2 to 15.0(1) SU2, no manual cert_type correction is required.

If the destination uses a different hostname or IP address, the certificates are regenerated. The destination uses the default
                                             RSA certificate and cert_type=RSA .

## Contact Center Enterprise Components Migration from VMware to Nutanix

Task

CCE Components Migration

Migration of Unified CVP

Platform Data Migration (Common for VOS Components)

Perform this once for each VOS-based component before the component data is migrated. See the respective sections for the exact sequence and procedure.

Migration of Cloud Connect

Migration of Cisco VVB

Migration of Finesse

Migration of Unified Intelligence Center

Migration of Live Data

Migration of standalone Cisco IdS

Migration of Enterprise Chat and Email

Migration of Unified CCMP

### CCE Components Migration

Sequence

Task

1

Before you Begin

2

CCE Components

3

Administration Client

4

Important Considerations

#### Before You Begin

Before you install CCE components, perform the following pre-installation tasks:

Pre-installation Task

Link

Download CCE OVA for Nutanix

Contact Center Enterprise OVA for Nutanix

Upload CCE OVA on Nutanix

Upload OVA to Nutanix

Upload CCE required ISO Images to Nutanix

Upload Images to Nutanix

Create a Virtual Machine from the CCE OVA on Nutanix

Create a Virtual Machine from the OVA on Nutanix

Install Microsoft Windows Server on the virtual machines deployed for CCE components

Install Microsoft Windows Server

Install Microsoft SQL Server for Rogger, Logger and Administration & Data Server VM(s)

Install Microsoft SQL Server

Install Microsoft Windows 11 for Administration Client

Install Microsoft Windows 11 for Administration Client

#### CCE Components

The CCE components (Router, Logger, Peripheral Gateway, and Administration & Data Server) can be migrated from VMware to Nutanix
                                    using either of the following methods:

Technology Refresh upgrade

For information, see Technology Refresh Upgrade Process

Nutanix Move

For information, see

#### Administration Client

As Technology Refresh is not supported for the Administration Client, perform a fresh installation of the Administration Client
                                 version 15.0(1) on Nutanix and then install ES202607 or later on Administration Client installed on Nutanix.

Microsoft Visual C++ Redistributable is a prerequisite to install Administration Client on Windows VM deployed on Nutanix.
                                             The latest version of Visual C++ Redistributable can be downloaded from Microsoft, also same is available in AdminClientInstaller
                                             folder.

For more information, see the Install Unified CCE Administration Client topic in the Installation chapter of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

#### Important Considerations

Use the Enhanced Database Migration Tool (EDMT) to transfer data and perform a schema upgrade during the technology upgrade
                                    process.

EDMT migrates the CCE database and its associated database-level users. Microsoft SQL Server backup and restore includes database-level
                                          users but does not transfer SQL Server-level logins from the source instance to the destination instance.

After the initial EDMT migration, administrators who wish to maintain identical logins and passwords on both the source and
                                          destination of SQL Server must follow Microsoft's recommended procedure for transferring server-level logins.

The procedure to transfer server-level logins is required to be executed only once, immediately after the first time EDMT
                                          migration and does not need to be repeated for subsequent EDMT runs used for database synchronization before or during cutover.
                                          For detailed instructions on SQL Server-level logins migration, refer Transfer logins and passwords between instances of SQL Server.

If an EDMT rerun is performed before or during cutover, any mappings for new users added to the destination database after
                                          the initial EDMT migration will be removed. This is expected behavior when using SQL Server backup and restore. Administrators
                                          will need to re-map the appropriate SQL logins to the corresponding database users after the rerun.

After migrating or freshly installing CCE Windows-based components, re-establish the required certificate trust relationships
                                          if certificates were regenerated or changed. Import the destination component certificates into all dependent CCE components.

For the certificate requirements and procedures, see the Certificate Management for Secured Connections chapter in the Security Guide for Cisco Unified Contact Center Enterprise .

#### Migrate Windows Components Using Nutanix Move

Nutanix Move migrates Windows-based Contact Center Enterprise components (Router, Logger, Rogger, Administration & Data Server,
                                 Peripheral Gateway, and Unified CVP servers) from VMware to Nutanix AHV.

Before you begin, ensure that the Nutanix Move appliance is deployed and configured, and that both the source (VMware) and
                                    target (Nutanix) environments are added in the Nutanix Move console. For more information, see Setup Nutanix Move .

The following table lists the tasks to migrate a Windows component using Nutanix Move:

Nutanix Move performs a virtual-to-virtual (V2V) migration. The cutover requires the source VM to be shut down on the source hypervisor , which results in service disruption. Schedule the migration during a planned maintenance window.

### Unified CVP- Migration from VMware to Nutanix

To migrate Cisco Unified CVP from VMware to Nutanix, use one of the following methods:

Export and import procedures — Migrate the Operations Console Server, Call Server, VXML Server, and Reporting Server using the export/import and backup/restore
                                       procedures described in this section.

To migrate the Cisco Unified CVP from VMware to Nutanix, perform the following:

Sequence

Task

1

Before you Begin

2

Migrate Operations Console Server, Call Server, and VXML Server from VMware to Nutanix

3

Migrate Reporting Server from VMware to Nutanix

Nutanix Move — Migrate Unified CVP components using the Nutanix Move tool. For the exact procedure, see Migrate Windows Components Using Nutanix Move .

Nutanix Move migrates all Unified CVP components, including the Reporting Server. The export and import procedures described
                                                   in this section are an alternative method, in which the Reporting Server is migrated separately using database backup and
                                                   restore.

#### Before You Begin

Before you install Unified CVP, perform the following pre-installation tasks:

Tasks

Link

Download Unified CVP OVA for Nutanix

Contact Center Enterprise OVA for Nutanix

Upload Unified CVP OVA on Nutanix

Upload OVA to Nutanix

Upload Unified CVP required ISO Images to Nutanix

Upload Images to Nutanix

Create a Virtual Machine from the Unified CVP OVA on Nutanix

Create a Virtual Machine from the OVA on Nutanix

Note: Importing or exporting the Unified CVP OAMP configuration is not supported when the Federal Information Processing Standard
                                    (FIPS) is enabled.

If Unified CVP on the source is configured for secure communication between Cisco Unified Border Element (CUBE), Cisco Unified
                                    Communications Manager (Unified CM), Peripheral Interface Manager (PIM), Cisco VVB, and Session Initiation Protocol (SIP)
                                    proxies such as Cisco Contact Center SIP Proxy (CCCSP), repeat the configuration process on the Unified CVP at the destination
                                    as well.

#### Migrate Unified CVP Servers from VMware to Nutanix

You can migrate Operations Console Server, Call Server, and VXML server from VMware to Nutanix. For more information about
                                    the migration process, see the Unified CVP Migration chapter of the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal .

After migrating the Operations Console Server, import the Web Service Management (WSM) certificate from the Call Server into
                                    the OAMP keystore before you access the Smart Licensing page in NOAMP. Restart the OAMP server and verify the registration
                                    status. The manual registration is needed in the new setup. For more information, see the Smart Licensing section in the Administration Guide for Cisco Unified Customer Voice Portal.

#### Migrate Reporting Server from VMware to Nutanix

Perform the following steps to backup and restore the Reporting Server data:

Step 1

Back up Reporting Server data in the source VMware environment. For more information, see the Database Backup section in the Reporting Guide for Unified CVP at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/reporting/guide/ccvp_b_150_reporting-guide-for-cisco-unified-customer-voice-portal/cvp_m_150_database-management.html#CCVP_RF_D0FBDA2C_00

Step 2

Restore Reporting Server data in the destination Nutanix environment. For more information about the restore command, see
                                             the Database Backup section in the Reporting Guide for Unified CVP at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/reporting/guide/ccvp_b_150_reporting-guide-for-cisco-unified-customer-voice-portal/cvp_m_150_database-management.html#CCVP_RF_D0FBDA2C_00

### Cloud Connect - Migration from VMware to Nutanix

Use the following task flow to migrate Cloud Connect:

Sequence

Task

1

Before you Begin

2

Export Platform Data Separately from the Source Publisher and Subscriber VMs to the Remote Server

3

Export Cloud Connect Application Data from the Source Publisher VM Only to the Remote Server

4

Upload OVA to Nutanix

5

Create a Virtual Machine from the OVA on Nutanix

6

Shutdown the Source VM(s)

7

Fresh Install Destination VM(s) with Import option on Nutanix Using Exported Platform Data

8

Import Cloud Connect Application Data from the Remote Server to the Destination Publisher VM

9

Post migration configuration of Cloud Connect

#### Before you Begin

CCE supports Cloud Connect migration, provided the source is on one of the following:

Version 15.0(1) ES202511

Version 15.0(1) SU1

Version 15.0(1) SU2

Version 12.6(2) ES04 or later

Verify that all required Platform services and containers (services of Cloud Connect) are up and running using the following
                                    commands:

To verify Platform services, run the following command:

utils service list

To verify the container services of Cloud Connect, run the following command:

utils cloudconnect list

Verify that the containers listed for the source release display the status Up .

Source release

Cloud Connect containers

15.0(1) ES202511 or later

certmgmt

dataconn

featureflagmgmt

cloudconnectmgmt

cache-service

cce-cdn

digitalrouting

inventory

12.6(2) ES04 or later

digitalrouting

cloudconnectmgmt

inventory

cherrypoint

dataconn

#### Export Platform Data from the Source VM to the Remote Server

Export platform data from both the Cloud Connect publisher and subscriber. Follow Export Platform Data from the Source VM to the Remote Server for each node.

#### Export Cloud Connect Application Data from the Source Publisher VM to the Remote Server

This procedure exports Cloud Connect application data and must be performed only on the publisher. It is separate from the
                                    platform-data export, which must be performed on both the publisher and subscriber. Specify an application-data export directory
                                    that is different from the Export Data Directory used for the platform-data export.

To export the Cloud Connect application data from the source publisher VM to the remote server, do the following:

Step 1

Log in to the CLI of the source Cloud Connect publisher using administrator credentials.

Step 2

Run the following command and verify that the Current Schema Version matches the Latest Schema Version for every configuration item displayed:

The configuration sources, file names, and schema versions displayed by this command vary depending on the Cloud Connect release
                                                and Engineering Special installed. The following output is an example from Cloud Connect 15.0(1) SU2 :

```
admin:utils cloudconnect config status
Source:
1)digitalrouting
2)cloudconnectmgmt
3)featureflagmgmt
q)quit

Please select an option(1-3 or "q" ): 1
Fetching existing configuration...
taskQueueSettings.json : Current Schema Version : 0 Latest Schema Version : 0
eccVariable.json : Current Schema Version : 0 Latest Schema Version : 0
notificationClients.json : Current Schema Version : 0 Latest Schema Version : 0
mediaChannels.json : Current Schema Version : 2 Latest Schema Version : 2
digitalRoutingConfig.json : Current Schema Version : 1 Latest Schema Version : 1
admin:utils cloudconnect config status
Source:
1)digitalrouting
2)cloudconnectmgmt
3)featureflagmgmt
q)quit

Please select an option(1-3 or "q" ): 2
Fetching existing configuration...
oauth2config.conf : Current Schema Version : 0 Latest Schema Version : 0
admin:utils cloudconnect config status
Source:
1)digitalrouting
2)cloudconnectmgmt
3)featureflagmgmt
q)quit

Please select an option(1-3 or "q" ): 3
Fetching existing configuration...
featureflagconfig.json : Current Schema Version : 1 Latest Schema Version : 1
admin:
```

Step 3

To initiate the export, run the following command:

```
utils component dataexport initiate
```

When prompted for the export directory, enter an absolute path that begins with a forward slash (/).

Step 4

Enter the remote server's IP address, login ID, and password.

Step 5

Specify the directory where the application data must be exported. Use a different directory from the Export Data Directory used for platform data.

Step 6

Enter the hostname and IP address of the destination VM. These values can differ from the source VM hostname and IP address.

Step 7

When prompted, enter yes to proceed with the data export. The data export begins.

Step 8

To check the data export status, run the following command:

```
utils component datamigration status
```

Verify that the output reports that the last component data export operation was successful.

#### Upload OVA on Nutanix

For more information, see the Upload OVA on Nutanix section in this guide.

#### Create a Virtual Machine from the OVA on Nutanix

For more information, see the Create a Virtual Machine from the OVA on Nutanix section in this guide.

#### Shutdown the Source VM(s)

Before shutting down the source Cloud Connect VMs, verify that:

Platform-data export is complete for the publisher and subscriber.

Cloud Connect application-data export is complete on the publisher.

The export directory and file corresponding to each source node have been recorded.

The Cloud Connect inventory has been exported to an SFTP server by running:

```
utils system inventory export
```

Retain the exported inventory.conf file for onboarding the VOS-based and Windows-based VMs after migration.

For more information, see the Shutdown the Source VM(s) section in this guide.

#### Fresh Install VM with Import option on Nutanix Using Exported Platform Data

Perform this procedure separately for the destination publisher and subscriber. Import the platform data exported from the
                                    corresponding source node:

Step 1

Create a Virtual Machine using the OVA Template.

Mount the UCSInstall_CLOUDCONNECT_15.0.1.10200-97 bootable image to the Virtual Machine (VM) and power on the VM. For more information, see the following sections in this
                                                   guide:

Upload OVA to Nutanix

Upload Images to Nutanix

Create a Virtual Machine from the OVA on Nutanix

Step 2

Click OK after the media check succeeds.

Step 3

Choose the applicable VOS component and click OK .

Step 4

Click Yes to proceed with installation of the 15.0(1) SU2 build version.

Step 5

Click Import in the Platform Installation Wizard.

Step 6

After reading the displayed information, click OK in the Import Upgrade Configuration information.

Step 7

Choose the appropriate time zone and then click OK .

Step 8

Click Continue in the Auto Negotiation Configuration .

Step 9

Click No to have the default value in MTU Configuration .

Step 10

Click No under DHCP Configuration .

Step 11

Enter the destination hostname and IP address specified during the platform data export. Enter the IP mask and gateway address,
                                             and click OK . The destination values can be different from those of the source VM.

Step 12

Click Yes under the DNS Client Configuration .

Step 13

Provide the Primary DNS server's IP Address and Domain and then click OK .

Step 14

Provide the SFTP server IP address, login ID, and password. For the directory, specify the cluster directory containing the
                                             exported platform data. Use the following format:

<Export-Data-Directory>/cluster-<source-publisher-IP-address>

For example:

/cloudconnect-export/cluster-10.10.10.20

Use this cluster directory when installing both the destination publisher and subscriber.

Step 15

Enter the organization information on the Certificate Information page, and click OK .

During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                               and IP address as the source:

Same hostname and IP address: All source certificates are migrated, including:

Tomcat RSA and ECDSA certificates

Tomcat trust certificates

IPsec and IPsec trust certificates

CA-signed certificates, including root and intermediate CA certificates

Component certificates uploaded to the Tomcat trust store

Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x.

Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                                     source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname.

The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                                     issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management .

Verify the certificates on the destination node to ensure that all required trust relationships are established.

Step 16

In the First Node Configuration screen, specify whether you are configuring the first node based on the following:

If you are installing a primary node, then click Yes under the First Node Configuration.

If you are installing a secondary node, then click No and provide the hostname and IP address of the destination publisher.

A warning message states that you must configure the first node before continuing. If the first node is already configured,
                                                         click OK .

On the Network Connectivity Test Configuration page, select No to proceed with the installation after connectivity is verified.

Provide the Primary host name and IP Address in the First Node Access Configuration page and click OK .

Step 17

For a standalone node such as Cisco VVB, skip this step. Configure the Network Time Protocol (NTP) server and then click Proceed .

Step 18

On the SMTP Host Configuration screen, choose one of the following:

To configure an SMTP host during installation, click Yes and enter the SMTP host information.

To continue without configuring an SMTP host, click No .

Step 19

On the Platform Configuration Confirmation page, click OK .

##### What to do next

After successful installation, you can run the following commands:

To check the current version of the system, run the following command:

```
show version active
```

Verify that Active Master Version displays the installed Cloud Connect 15.0(1) SU2 version:

```
Active Master Version: 15.0.1.10200-97
```

After installing the destination publisher and before installing the destination subscriber, verify that the publisher is
                                          mapped to the correct destination subscriber:

```
show cloudconnect subscriber
```

Example:

```
admin:show cloudconnect subscriber
Cloud Connect subscriber node is set to "cloudconnect65b".
```

If the displayed subscriber hostname does not match the destination subscriber, run the following command on the destination
                                             publisher:

```
set cloudconnect subscriber <destination-subscriber-FQDN-or-IP-address>
```

Run show cloudconnect subscriber again and verify that the displayed hostname matches the destination subscriber before installing the subscriber.

After the fresh installation of both the destination publisher and subscriber is complete, run the following command on the
                                             publisher:

```
utils dbreplication runtimestate
```

Verify that:

Sync Result shows SYNC COMPLETED for all tables.

Sync Status shows All Tables are in sync .

REPLICATION SETUP shows (2) Setup Completed for both the publisher and subscriber.

On each destination node, run the following command to verify that the platform-data import was successful:

```
file view install system-history.log
```

Verify that:

Product Version shows 15.0.1.10200-97 .

The Import during Install entry shows the destination version 15.0.1.10200-97 and ends with Success .

The subsequent Product Version entry shows 15.0.1.10200-97 .

#### Import Cloud Connect Application Data from the Remote Server to the Destination Publisher VM

To import the Cloud Connect application data from the remote server to the destination publisher VM, do the following:

Step 1

Log in to the CLI of the destination Cloud Connect publisher using administrator credentials.

Step 2

Verify that all required Cloud Connect services are running by using the following command:

```
utils service list
```

Service status varies by deployment. A service that displays STOPPED—Service Not Activated is not enabled on that node and does not prevent migration. Before proceeding, investigate any required service that displays STOPPED .

Step 3

On the publisher and subscriber, run the following command to obtain the container names:

```
utils cloudconnect list
```

Compare the output of utils cloudconnect list with the containers listed for your source release. If a required container does not display the status Up , do not begin the migration. To start a stopped container, run:

```
utils cloudconnect start <container-name>
```

Run utils cloudconnect list again. If a required container is missing or does not start, resolve the issue before proceeding with the migration.

Step 4

On the publisher only, run the following command to reset all containers:

```
utils cloudconnect reinit services
```

Step 5

Stop all containers on the publisher and subscriber by running the following command:

```
utils cloudconnect stop <container-name>
```

Step 6

On the publisher only, run the following CLI command to initiate the import:

```
utils component dataimport initiate
```

Step 7

Enter the remote server's IP address, login ID, and password.

Step 8

For Data Directory and Data filename , enter the path and name of the directory to which the data was exported (tar file).

Step 9

When prompted, enter yes to proceed with the data import. The data import begins.

Step 10

To verify completion, run the following CLI command:

```
utils component datamigration status
```

Step 11

Restart the destination Cloud Connect publisher and subscriber nodes by running the following command:

```
utils system restart
```

Run the command on both the publisher and subscriber. Restarting each node automatically restarts its containers.

Step 12

After both nodes restart, validate that the required containers are running on the publisher and subscriber:

```
utils cloudconnect list
```

Verify that the required containers display the status Up . For the expected containers, see Before you Begin .

##### What to do next

FEDRAMP Keys Exclusion : FEDRAMP keys are excluded from the migration process and are not transferred during export or import.

Re-import Behavior : The re-import operation is not incremental. It resets the destination Cloud Connect environment to the base installation
                                                      state before importing data from the source VM.

Import Failure Handling : In the event of an import failure, the destination VM will automatically revert to the base fresh installation state, retaining
                                                      only the platform-imported data.

#### Post-Migration Configuration for Cloud Connect

Cloud Connect Onboarding

Prerequisite: Ensure that the Cloud Connect destination instance is part of the Packaged CCE Administrator Console inventory. If it is not, add the instance to the inventory.

If the destination Cloud Connect instance uses a different hostname or IP address, update the Cloud Connect details in Finesse
                                    Administration (cfadmin) and the Media Routing Peripheral Gateway (MR PG) configuration to point to the destination instance.

For more information, see the Web-Based CCE Administration chapter of the Administration Guide for Cisco Unified Contact Center Enterprise .

Procedure: Register the Cloud Connect instance, configure the proxy settings, and activate the required devices or services to establish
                                       secure communication with the cloud services used by the enabled Cloud Connect features.

HTTP Proxy settings must be reconfigured during onboarding.

For more information on the onboarding process and activating necessary devices or services, see the Cloud Connect Onboarding Procedure .

Re-Enabling Digital Channels - Synchronize CCE agents to Webex Engage

During migration between the Cloud Connect source and destination, the Digital Agent status, such as synced or pending, is
                                          exported and restored after successful execution of the import.

The transfer of Digital Agent status occurs only after both export and import operations are completed successfully.

Following data migration, all necessary configuration steps must be re-applied on the destination Cloud Connect instance.

For more information, see the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide

Certificate Management

Establish secure connections between Cloud Connect and the Media Routing Peripheral Gateway (MR PG).

For more information, see the Certificate Management for Digital Channels Integration section of the Security Guide for Cisco Unified Contact Center Enterprise .

Set up the Nginx reverse proxy server certificate for digital channel interaction.

Certificate Management must be performed every time Cloud Connect data is migrated.

For more information, see the Certificate Management for Digital Channels Integration section of the Security Guide for Cisco Unified Contact Center Enterprise .

##### Update the Webex Connect Integration

Perform the following steps if your deployment is integrated with Webex Connect:

From the destination Cisco IdS CLI, run the following command to retrieve the Cisco IdS token certificate:

```
show ids token certificate
```

Save the certificate as a PEM file and upload it to Control Hub to replace the certificate associated with the Cloud Connect
                                    integration. Verify the reverse proxy configuration and, if necessary, update it to point to the destination Cloud Connect
                                    instance.

For more information, see the Digital Channels Integration Using Webex Connect chapter in the Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1) .

Cloud Connect Configuration for Orchestration feature

This section is applicable only if you have enabled the Orchestration feature.

Configure the following after migration to ensure that the Orchestration feature functions as before:

Sequence

Configuration

1

Configure API Key / Identity Token

To establish a connection with Artifactory, you must reconfigure the API Key or Identity Token on the Cloud Connect Publisher
                                                VM using the CLI command utils image-repository set .

For more information, see CLI to Configure Artifactory URL and Artifactory Authentication Credentials in the CCE Orchestration chapter.

2

Onboard CCE Solution Components to Cloud Connect

Onboarding all the CCE solution components to Cloud Connect is required to enable Orchestration.

For more information, see the following topics in the CCE Orchestration chapter:

Onboard VOS Nodes to Orchestration Control Node

Onboard Windows Nodes to Orchestration Control Node

3

Initiate Software Download on Both Cloud Connect Components

Run the CLI command utils initiate software-download on both Publisher and Subscriber Cloud Connect components to download software from Artifactory.

Periodic software download is automatically scheduled every day at 2 AM or at the time configured by the administrator.

For more information, see Enforce Software Download from Cisco-Hosted Software Artifactory in the CCE Orchestration chapter.

4

SMTP Password

If SMTP authentication is enabled, you must set up the SMTP password after migration, as sensitive data such as passwords
                                                are excluded during Cloud Connect data migration.

Run the CLI command set smtp-pswd to set the password for the SMTP server connection.

For more information, see Set Up Email Notification in the CCE Orchestration chapter.

5

Enable Auto-Rotate of Identity Token

If auto-rotate of the Identity Token was enabled on the source Cloud Connect, you must explicitly re-enable it after migration.

For more information, see Configure Identity Token Auto Rotation in the CCE Orchestration chapter.

6

Reconfigure Software Download Time and Cron Job Schedules

If you customized any Orchestration job schedules prior to migration, you must reconfigure them using the Orchestration Scheduled
                                                Job CLI after the migration is complete.

Migration Requirements

Releases earlier than 15.0(1) SU1 : If you previously customized the Software Download schedule, you must reconfigure it using the Orchestration Scheduled Job
                                                CLI.

Releases 15.0(1) SU1 or later : If you customized any Orchestration job schedules, you must reconfigure them using the Orchestration Scheduled Job CLI.

Starting with release 15.0(1) SU1 , the CLI supports scheduling for the following jobs:

Software Download from Cisco Artifactory

Deployment Cache Update

Software Update Email Notification

Auto-rotate Cisco Artifactory Token

For detailed instructions, see CLI to Configure Orchestration Scheduled Jobs in the CCE Orchestration chapter.

Cloud Connect Configuration for AppDynamics Monitoring

Perform this step only if you need to integrate with AppDynamics.

Configure the following after migration to ensure that AppDynamics monitoring functions as before:

Sequence

Configuration

1

Onboard CCE Solution Components to Cloud Connect

Onboarding all the CCE solution components to Cloud Connect is required to enable AppDynamics features.

For more information, see the following topics in the CCE Orchestration chapter:

Onboard VOS Nodes to Orchestration Control Node

Onboard Windows Nodes to Orchestration Control Node

2

Import and Update AppDynamics Agents

Importing the AppDynamics Agents into Cloud Connect is required. This includes the Machine Agent, Java Agent, .NET Agent,
                                                and DotNetAgentExtensionManager for Windows, and the Machine Agent and Java Agent for VOS components. After the agents are
                                                imported, you must update the AppDynamics Agents on the respective Windows and VOS components.

For more information, see the Import AppDynamics Agents and Update AppDynamics Agents sections in the CCE Serviceability and
                                                Monitoring using AppDynamics chapter of the Serviceability Guide for Cisco Unified Contact Center Enterprise .

3

Enable AppDynamics Performance Monitoring

Ensure that you disable AppDynamics performance monitoring on the Cloud Connect source for both VOS-based and Windows-based
                                                            components before enabling it on the destination.

You need to enable performance monitoring for both VOS and Windows components and provide the following fields during the
                                                process:

Account Access Key

Beacon Access Key

Password

For more information, see the Enable Performance Monitoring section in the CCE Serviceability and Monitoring using AppDynamics
                                                chapter of the Serviceability Guide for Cisco Unified Contact Center Enterprise .

### Cisco VVB - Migration from VMware to Nutanix

To migrate Cisco VVB from VMware to Nutanix, repeat the following steps for each source VM :

Sequence

Steps Involved

1

Before you Begin

2

Export Platform Data from the Source VM to the Remote Server

3

Export Cisco VVB Data from the Source VM to the Remote Server

4

Upload OVA on Nutanix

5

Create a Virtual Machine from the OVA on Nutanix

6

Shutdown the Source VM(s)

7

Fresh Install VM with Import option on Nutanix Using Exported Platform Data

8

Import Cisco VVB Data from the Remote Server to the Destination VM

9

Post-Migration Configuration for Cisco VVB

#### Before you Begin

OVA Profile Consistency

Ensure that data migration is performed between source and destination Virtual Machine (VM) using the OVA having the same
                                    profile size (such as small or medium).

Supported Versions

CCE supports Cisco VVB migration, provided the source is on one of the following versions:

Version 15.0(1) ES202511

Version 15.0(1) SU1

Version 15.0(1) SU2

Version 12.6(2) ES07

Verify Cisco VVB Service Status

Perform the following from the source (VMware) environment:

Log in to the Cisco VVB Admin Console using administrator credentials.

Use the following CLI commands to verify that all platform and component services are up and running:

utils service list

#### Export Platform Data from the Source to the Remote Server

For more information, see the Export Platform Data from the Source to the Remote Server.

#### Export Cisco VVB Data from the Source VM to the Remote Server

To export Cisco VVB data from the source VM to the remote server, do the following:

Before you begin the export, run the following command on the source VM:

```
utils service list
```

Verify that all required platform and component services show the status STARTED .

Step 1

Log in to the Cisco VVB CLI using administrator credentials.

Step 2

Initiate the export by running the following CLI command:

```
utils component dataexport initiate
```

When prompted for the export directory, enter an absolute path that begins with a forward slash (/).

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the absolute path of the directory to which the data must be exported. The path must begin with a forward slash (/).

Step 5

Enter the IP address and hostname of the destination VM.

Step 6

When prompted, enter "yes" to proceed with the export. The data export begins. Monitor the data export progress in the log
                                                using the following command:

```
file tail activelog platform/log/component_dataexport_<YYYYMMDD>_<HHMMSS>.log
```

Replace <YYYYMMDD>_<HHMMSS> with the timestamp in the log-file name generated for your export operation.

Step 7

To check the data export status, run the following command:

```
utils component datamigration status
```

Verify that the output reports that the last component data export operation was successful.

The component data export is complete.

#### Upload OVA on Nutanix

For more information, see the Upload OVA on Nutanix section in this guide.

#### Create a Virtual Machine from the OVA on Nutanix

For more information, see the Create a Virtual Machine from the OVA on Nutanix section in this guide.

#### Shutdown the Source VM(s)

(Optional) Execute this step only if the source and destination VMs have the same IP address, as this creates an IP address
                                       conflict.

To shut down the system, run the following CLI command:

```
utils system shutdown
```

#### Fresh Install VM with Import Option on Nutanix Using Exported Platform Data

For more information, see the Fresh Install VM With Import Option on Nutanix Using Exported Platform Data section in this guide.

#### Import Cisco VVB Data from the Remote Server to the Destination VM

Platform data migration must be completed before migrating component data, as Cisco VVB depends on the successful migration
                                                   of platform data, especially certificates. Before you begin the component import, run the following command on the destination
                                                   VM:

```
utils service list
```

Verify that all required platform services show the status STARTED .

To import Cisco VVB data from the remote server to the destination VM, do the following:

Step 1

Log in to the destination Cisco VVB CLI using administrator credentials.

Step 2

Run the following command to initiate the import:

```
utils component dataimport initiate
```

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the name of the directory to which the data was exported.

Step 5

When prompted, enter Yes to proceed with the import. The data import begins. To monitor data import progress in the log, run the following CLI command:

```
file tail activelog platform/log/component_dataimport_<YYYYMMDD>_<HHMMSS>.log
```

Replace <YYYYMMDD>_<HHMMSS> with the timestamp in the log-file name generated for your import operation.

Step 6

To check the component data import status, run the following command:

```
utils component datamigration status
```

Verify that the output shows Last component dataimport operation was SUCCESS at <timestamp> . After the import succeeds, complete the applicable tasks in Post-Migration Configuration for Cisco VVB and verify Cisco VVB call flows and AppAdmin access.

##### What to do next

FEDRAMP Keys Exclusion: FEDRAMP keys are excluded from the migration process and are not transferred during export or import.

Re-import Behavior : The re-import operation is not incremental. It resets the destination Cisco VVB environment to the base installation state
                                                      before importing data from the source VM.

Import Failure Handling : In the event of an import failure, the destination VM will automatically revert to the base fresh installation state, retaining
                                                      only the platform-imported data.

#### Post-Migration Configuration for Cisco VVB

After importing the Cisco VVB component data, complete the applicable
                                    post-migration configuration tasks.

##### DNS Configuration

If DNS was not configured during Fresh
                                       Install VM with Import Option on Nutanix Using Exported Platform Data ,
                                    configure DNS on the destination Cisco VVB VM.

If the source Cisco VVB VM used a customized DNS configuration,
                                    reconfigure those settings on the destination Cisco VVB VM after the
                                    import.

For more information, see the Configure DNS Server section in the
                                    Cisco VVB Installation chapter of the Installation and Upgrade Guide for Cisco Virtualized
                                       Voice Browser .

##### Update Cisco VVB Inventory and Configuration

If the Cisco VVB hostname or IP address changes during migration,
                                    verify that the destination Cisco VVB instance is listed in the Packaged CCE inventory.

If the destination Cisco VVB instance is not present in the
                                          Packaged CCE deployment, configure Cisco VVB.

For more information, see the Configure Cisco VVB section in the Post
                                          Installation Configuration chapter of the Cisco Packaged Contact Center Enterprise
                                             Administration and Configuration Guide .

##### Certificate Exchange

If the Cisco VVB hostname, IP address, or certificate changes during
                                    migration, exchange the destination Cisco VVB certificate as applicable
                                    to your Packaged CCE deployment.

Import the destination Cisco VVB certificate into the Unified CVP
                                          Operations Console.

Import the destination Cisco VVB certificate into the
                                          Administration & Data Server.

Comprehensive Call Flow Scenario

Import the destination Cisco VVB certificate into the Call Server
                                          and the VXML Server.

Standalone Call Flow Scenario

Import the destination Cisco VVB certificate into Cisco Unified
                                          Border Element.

For more information about importing the certificate into the Unified
                                       CVP Operations Console and the Administration & Data Server, see Exchange Self-Signed Certificates in a Unified CCE
                                          12.6 Solution .

For more information about certificate exchange for standalone and
                                    comprehensive call-flow deployments, see the Secure HTTP Communication
                                    between VXML Server and Cisco VVB section in the Unified CVP Security
                                    chapter of the Configuration Guide for Cisco Unified Customer Voice
                                       Portal .

### Finesse - Migration from VMware to Nutanix

To migrate Finesse from VMware to Nutanix, perform the following steps:

Sequence

Tasks

1

Before you Begin

2

Export Platform Data from the Source VM to the Remote Server

3

Upload OVA on Nutanix

4

Create a Virtual Machine from the OVA on Nutanix

5

Export Finesse Data from the Source Publisher VM to the Remote Server

6

Export Finesse Data from the Source Subscriber VM to the Remote Server

7

Shutdown the Source VM(s)

8

Fresh Install VM with Import option on Nutanix Using Exported Platform Data

9

Import Finesse Data from Remote Server to the Destination VM (Publisher)

10

Import Finesse Data from Remote Server to the Destination VM (Subscriber)

11

Post-Migration Configuration of Finesse

#### Before you Begin

The database export happens only from the Finesse Primary node but not on the Subscriber node.

Configuration files will be migrated first, then database migration will begin.

If configuration migration fails, the export will terminate, and database migration will be skipped.

A tar.gz file will be created and exported to the given SFTP directory.

The logs will display all details regarding exported configuration files, tables, and sequence names, along with statistics
                                          showing the total counts of tables exported and skipped optional configurations.

Supported Versions : CCE supports Finesse migration, provided the source is on one of the following versions:

Version 15.0(1) ES202511

Version 15.0(1) SU1

Version 15.0(1) SU2

Version 12.6(2) ES07

#### Export Platform Data from the Source to the Remote Server

For more information, see the Export Platform Data from the Source to the Remote Server section in this guide.

#### Upload OVA on Nutanix

For more information, see the Upload OVA on Nutanix section in this guide.

#### Create a Virtual Machine from the OVA on Nutanix

For more information, see the Create a Virtual Machine from the OVA on Nutanix section in this guide.

#### Export Finesse Data from the Source Publisher VM to the Remote Server

To export the Finesse configuration from the source publisher to the remote server, do the following:

Step 1

Log in to the Finesse CLI using administrator credentials.

Step 2

To initiate the export, run the following command:

```
utils component dataexport initiate
```

When prompted for the export directory, enter an absolute path that begins with a forward slash (/).

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the name and path for the directory to which data must be exported.

Step 5

Enter the IP address and hostname of the destination VM.

Step 6

Enter yes when prompted to proceed with the export. The data export begins. Monitor its progress in the log.

Step 7

To check the data export status, run the following command:

```
utils component datamigration status
```

#### Export Finesse Data from the Source Subscriber VM to the Remote Server

The Finesse data export procedure is the same for the Publisher and Subscriber. To export data from the Subscriber, follow Export Finesse Data from the Source Publisher VM to the Remote Server on the Subscriber VM.

#### Shutdown the Source VM(s)

For more information, see the Shutdown the Source VM(s) section in this guide.

#### Fresh Install VM with Import option on Nutanix Using Exported Platform Data

For more information, see the Fresh Install VM with Import option on Nutanix Using Exported Platform Data section in this guide.

#### Import Finesse Data from Remote Server to the Destination VM (Publisher)

To import Finesse data from the remote server to the destination publisher VM, do the following:

Step 1

Log in to the Finesse CLI using administrator credentials .

Step 2

To initiate the import, run the following command:

```
utils component dataimport initiate
```

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the name and path for the directory to which data must be imported.

Step 5

Confirm the data import by entering "yes" when prompted. The data import begins. Monitor its progress in the log.

Step 6

To check the component data import status, run the following command:

```
utils component datamigration status
```

#### Import Finesse Data from Remote Server to the Destination VM (Subscriber)

The Finesse data import procedure is the same for the Publisher and Subscriber. To import data on the Subscriber, follow Import Finesse Data from Remote Server to the Destination VM (Publisher) on the Subscriber VM.

#### Post-Migration Configuration for Finesse

Verify Database Replication Status

Step 1

The database is not exported from the Finesse Subscriber so you must perform the database replication by running the following
                                             CLI command on the Primary VM (Publisher) to force database synchronization to the subscriber:

Step 2

The database replication status must indicate that all tables are in sync.

Check the database replication status on all the Finesse cluster components to ensure that all servers are replicating database
                                                changes successfully.

Step 3

On the Finesse Primary (Publisher) VM, run the following CLI command:

##### What to do next

Update Server Details if Migrated to Nutanix If the CTI server, Data server, Chat server, and Cloud Connect server have been migrated to Nutanix and their IP addresses
                                    or hostnames have changed, update these details in the Finesse Administration Console. Reconfigure the new IP addresses or
                                    hostnames for all servers along with the required certificates exchange.

For more information about configuration, see the Manage System Settings chapter in Cisco Finesse Administration Guide .

Certificate Exchange

Perform these steps only if self-signed certificates are used.

When the destination Agent PG or Administration & Data Server Database (AWDB) is deployed through a fresh installation, the
                                    destination VM generates new certificates. Import the destination Agent PG and AWDB certificates into the Finesse platform
                                    trust store regardless of whether the hostname or IP address has changed.

For Cisco IdS, Cloud Connect, and Live Data, import the corresponding destination certificates into Finesse when the hostname,
                                    IP address, or certificate changes.

Use Cisco Unified Operating System Administration to import the certificates.

Restart Finesse Tomcat Service

Restart the Finesse Tomcat service on both the publisher and subscriber.

### Cisco IdS - Migration from VMware to Nutanix

This migration sequence applies only to a standalone Cisco IdS deployment. In a co-resident deployment, Cisco IdS is packaged
                                             with Unified Intelligence Center and Live Data. Migrate the packaged VM by following Unified Intelligence Center - Migration from VMware to Nutanix . Configuration performed on the Unified Intelligence Center co-resident VM also applies to the co-resident Live Data and
                                             Cisco IdS components. Do not perform the standalone Cisco IdS sequence for a co-resident deployment.

To migrate a standalone Cisco IdS deployment from VMware to Nutanix, perform the following steps:

Sequence

Tasks

1

Before you Begin

2

Export Platform Data from the Source VM to the Remote Server

3

Upload OVA on Nutanix

4

Create a Virtual Machine from the OVA on Nutanix

5

Export Cisco IdS Data from the Source Publisher VM to the Remote Server

6

Export Cisco IdS Data from the Source Subscriber VM to the Remote Server

7

Shutdown the Source VM(s)

8

Fresh Install VM with Import option on Nutanix Using Exported Platform Data

9

Import Cisco IdS Data from Remote Server to the Destination VM (Publisher)

10

Import Cisco IdS Data from Remote Server to the Destination VM (Subscriber)

11

Post-Migration Configuration of Cisco IdS

#### Before you Begin

This topic applies only to a standalone Cisco IdS deployment. For a co-resident deployment, migrate Cisco IdS as part of the
                                                packaged Unified Intelligence Center, Live Data, and Cisco IdS VM.

The database export occurs only on the Cisco IdS Publisher, not on the Subscriber.

Configuration files are migrated first, followed by database migration.

If configuration migration fails, the export terminates and database migration is skipped.

A tar.gz file is created and exported to the specified SFTP directory.

The logs display details about exported configuration files, tables, and sequence names, together with export and skip statistics.

Supported Versions : CCE supports standalone Cisco IdS migration when the source is on one of the following versions:

Version 15.0(1) ES202511

Version 15.0(1) SU1

Version 15.0(1) SU2

Version 12.6(2) ES07

#### Export Platform Data from the Source to the Remote Server

For more information, see the Export Platform Data from the Source to the Remote Server section in this guide.

#### Upload OVA on Nutanix

For more information, see the Upload OVA on Nutanix section in this guide.

#### Create a Virtual Machine from the OVA on Nutanix

For more information, see the Create a Virtual Machine from the OVA on Nutanix section in this guide.

#### Export Cisco IdS Data from the Source Publisher VM to the Remote Server

To export the Cisco IdS configuration from the standalone source publisher to the remote server, do the following:

Step 1

Log in to the Cisco IdS CLI using administrator credentials.

Step 2

To initiate the export, run the following command:

```
utils component dataexport initiate
```

When prompted for the export directory, enter an absolute path that begins with a forward slash (/).

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the name and path for the directory to which data must be exported.

Step 5

Enter the IP address and hostname of the destination VM.

Step 6

Enter yes when prompted to proceed with the export. The data export begins. Monitor its progress in the log.

Step 7

To check the data export status, run the following command:

```
utils component datamigration status
```

#### Export Cisco IdS Data from the Source Subscriber VM to the Remote Server

The standalone Cisco IdS data export procedure is the same for the Publisher and Subscriber. To export data from the Subscriber,
                                       follow Export Cisco IdS Data from the Source Publisher VM to the Remote Server on the Subscriber VM.

#### Shutdown the Source VM(s)

For more information, see the Shutdown the Source VM(s) section in this guide.

#### Fresh Install VM with Import option on Nutanix Using Exported Platform Data

For more information, see the Fresh Install VM with Import option on Nutanix Using Exported Platform Data section in this guide.

#### Import Cisco IdS Data from Remote Server to the Destination VM (Publisher)

To import Cisco IdS data from the remote server to the standalone destination publisher VM, do the following:

Step 1

Log in to the Cisco IdS CLI using administrator credentials .

Step 2

To initiate the import, run the following command:

```
utils component dataimport initiate
```

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the name and path for the directory to which data must be imported.

Step 5

Confirm the data import by entering "yes" when prompted. The data import begins. Monitor its progress in the log.

Step 6

To check the component data import status, run the following command:

```
utils component datamigration status
```

#### Import Cisco IdS Data from Remote Server to the Destination VM (Subscriber)

The standalone Cisco IdS data import procedure is the same for the Publisher and Subscriber. To import data on the Subscriber,
                                    follow Import Cisco IdS Data from Remote Server to the Destination VM (Publisher) on the Subscriber VM.

#### Post-Migration Configuration for Cisco IdS

Reconfigure Single Sign-On (SSO) in Cisco IdS For more information, see the Cisco IdS for Single Sign-On chapter, see Cisco Packaged Contact Center Enterprise Features Guide .

##### Certificate Exchange

Perform this step only if self-signed certificates are in use.

All certificates are migrated to the target systems during data migration. Cisco IdS stores certificates for Cloud Connect
                                    in the platform trust store.

If the hostname for Cloud Connect changes during migration, import the corresponding certificate into Cisco IdS using Cisco
                                    Unified OS Administration.

In case the Cisco IdS hostname is different:

If the Cisco IdS hostname has changed after migration, re-establish the trust between the Cisco IdS (Cisco IdS) and the Identity
                                    Provider (AD FS) by performing the following procedures:

Integrate Cisco IdS with AD FS topic in the Cisco IdS for Single Sign-On chapter of the Unified CCE Features Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Enable Signed SAML Assertions topic in the Cisco IdS for Single Sign-On chapter of the Unified CCE Features Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

In case the Cisco IdS hostname is same:

If the Cisco IdS hostname remains unchanged after migration, refresh the metadata exchanged  between the Cisco IdS and the
                                    Identity Provider (AD FS):

Upload the IdP metadata in Cisco IdS:

Download the IdP metadata file, federationmetadata.xml, from the following location:

```
https://<ADFS Server FQDN>/federationmetadata/2007-06/federationmetadata.xml
```

Do one of the following to upload the IdP metadata file, you downloaded at step 1, to the Cisco IdS server:

In the Identity Service Management console, select Settings > Cisco IdS Trust .

Click Next and then click Upload IdP Metadata .

In the Unified CCE Administration console, navigate to Infrastructure Settings > Device Configuration > Identity Service > Identity Service Settings > Cisco IdS Trust .

Click Next and then click Upload IdP Metadata .

Download LAN SP metadata and reverse-proxy cluster SP metadata from the primary node of the Cisco IdS publisher.

Open the Identity Service Management console at https://<CiscoIdS server address>:8553/idsadmin

From the menu on the left, select Settings . In the Cisco IdS Trust tab, download the XML file.

In Unified CCE Administration, go to Infrastructure Settings > Device Configuration > Identity Service > Identity Service Settings .

In the Cisco IdS Trust tab, download the XML file.

Update the Cisco IdS metadata in the IdP by running the following command:

```
Update-AdfsRelyingPartyTrust -MetadataFile <path to downloaded Cisco IdS metadata file>  -TargetName  <Relying Party Trust Display Name>
```

### Unified Intelligence Center - Migration from VMware to Nutanix

To migrate Unified Intelligence Center from VMware to Nutanix, perform the following tasks in the specified sequence.

In a 2000-agent deployment, Unified Intelligence Center, Live Data, and Cisco IdS are co-resident. The component data export and import in this sequence migrate all three components together. Do not run the standalone Live Data or standalone
                                             Cisco IdS export and import procedures for a co-resident deployment. After migration, complete the post-migration configuration
                                             for both Unified Intelligence Center and Live Data.

Sequence

Task

1

Before you Begin

2

Export Platform Data from the Source VM to the Remote Server

3

Upload OVA on Nutanix

4

Create a Virtual Machine from the OVA on Nutanix

5

Export Unified Intelligence Center Data from the Source Publisher VM to the Remote Server

6

Export Unified Intelligence Center Data from the Source Subscriber VM to the Remote Server

7

Shut Down the Source VM(s)

8

Fresh Install the Publisher VM on Nutanix Using Exported Platform Data

9

Import Unified Intelligence Center Data from the Remote Server to the Destination VM (Publisher)

10

Fresh Install the Subscriber VM on Nutanix Using Exported Platform Data

11

Import Unified Intelligence Center Data from the Remote Server to the Destination VM (Subscriber)

12

Post-Migration Configuration for Unified Intelligence Center

#### Before you Begin

Verify the following before proceeding with the Unified Intelligence Center export:

Supported Versions : CCE supports Unified Intelligence Center migration when the source is on one of the following versions:

Version 15.0(1) ES202511

Version 15.0(1) SU1

Version 15.0(1) SU2

Version 12.6(2) ES06

Ensure that the Cisco DB, Cisco DB Replicator, and Unified Intelligence Center Reporting Service services are started.

Verify that the services are started by running the following CLI command:

Confirm that database replication is functioning correctly on the Unified Intelligence Center publisher VM. Run the following
                                          command:

For more information, see the utils dbreplication runtimestate section in the Command Line Interface chapter of the Administration Console User Guide for Cisco Unified Intelligence Center .

The data export from the Unified Intelligence Center publisher VM may take time depending on the size of the Unified Intelligence
                                                Center database.

Data migration depends on the deployment model:

2000-agent deployment: The co-resident VM migrates Unified Intelligence Center, Live Data, and Cisco IdS in a single component data export and import.

4000-agent and larger deployments: Run the component data export and import separately on each standalone component VM.

#### Export Platform Data from the Source VM to the Remote Server

For more information, see the Export Platform Data from the Source VM to the Remote Server section in this guide.

#### Upload OVA on Nutanix

For more information, see the Upload OVA on Nutanix section in this guide.

#### Create a Virtual Machine from the OVA on Nutanix

For more information, see the Create a Virtual Machine from the OVA on Nutanix section in this guide.

#### Export Unified Intelligence Center Data from the Source Publisher VM to the Remote Server

To export the Unified Intelligence Center configuration from the source publisher to the remote server, perform the following
                                    steps:

Step 1

Log in to the Unified Intelligence Center CLI using administrator credentials.

Step 2

To initiate the export, run the following CLI command:

```
utils component dataexport initiate
```

When prompted for the export directory, enter an absolute path that begins with a forward slash (/).

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the path of the directory to which the data should be exported.

Step 5

Enter the hostname and IP address of the destination VM.

Step 6

Enter "yes" when prompted to proceed with the export. The data export begins. Monitor its progress in the log by running the
                                                file tail command available on the CLI interface.

Step 7

To check the data export status, run the following command:

```
utils component datamigration status
```

#### Export Unified Intelligence Center Data from the Source Subscriber VM to the Remote Server

To export the Unified Intelligence Center configuration from a source subscriber to the remote server, perform the following
                                    steps:

Step 1

Log in to the Unified Intelligence Center CLI using administrator credentials.

Step 2

Run the following CLI command to initiate the export:

```
utils component dataexport initiate
```

When prompted for the export directory, enter an absolute path that begins with a forward slash (/).

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the path of the directory to which the data should be exported.

Step 5

Enter the hostname and IP address of the destination VM.

Step 6

Enter "yes" when prompted to proceed with the export. The data export begins .

Step 7

Monitor the data export progress in the log by running the file tail command available on the CLI interface.

Step 8

To check the data export status, run the following command:

```
utils component datamigration status
```

#### Shut down the Source VM(s)

For more information, see the Shut down in the Source VM(s) section in this guide.

#### Fresh Install VM with Import option on Nutanix Using Exported Platform Data

For more information, see the Fresh Install VM with Import option on Nutanix Using Exported Platform Data section in this guide.

#### Import Unified Intelligence Center Data from the Remote Server to the Destination VM (Publisher)

To import the Unified Intelligence Center configuration from the remote server to the destination publisher VM, perform the
                                    following steps:

Step 1

Log in to the Unified Intelligence Center publisher CLI using administrator credentials.

Step 2

Run the following CLI command to initiate the import:

```
utils component dataimport initiate
```

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

For the Data Directory, specify name and path.

Step 5

Confirm the data import by entering "yes" when prompted. The data import begins. Monitor the data import progress in the log
                                                by running the file tail command available on the CLI interface.

Step 6

To check the component data import status, run the following command:

```
utils component datamigration status
```

##### What to do next

Before installing the destination subscriber, verify the subscriber VM details on the destination publisher.

If the destination subscriber uses a different hostname or IP address from the source subscriber, configure its details as
                                    follows:

2000-agent deployment: Configure the subscriber details in the Unified Intelligence Center Administration Console on the publisher Unified Intelligence
                                          Center co-resident VM. The configuration automatically also applies to Live Data and Cisco IdS.

Other deployment models: Configure the standalone Unified Intelligence Center subscriber details in the Unified Intelligence Center Administration
                                          Console.

If the destination subscriber retains the source hostname and IP address, no manual subscriber configuration is required.

For more details, see the Define Member Node in Administration Console topic in the Admin Console Sign-in chapter in the Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 15.0(1) .

#### Import Unified Intelligence Center Data from the Remote Server to the Destination VM (Subscriber)

A Subscriber import does not restore the Unified Intelligence Center database; instead, data from the Publisher database is
                                    replicated to all Subscribers. Only property file changes are restored during the Subscriber import process. As a result,
                                    Subscriber imports can be performed concurrently on all nodes, in any order.

To import the Unified Intelligence Center configuration from the remote server to a destination subscriber VM, perform the
                                    following steps:

Step 1

Log in to the Unified Intelligence Center subscriber CLI using administrator credentials.

Step 2

Run the following CLI command to initiate the import:

```
utils component dataimport initiate
```

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

For the Data Directory, specify name and path.

Step 5

Confirm the data import by entering "yes" when prompted. The data import begins. Monitor the data import progress in the log
                                             by running the file tail command available on the CLI interface.

Step 6

To check the component data import status, run the following command:

```
utils component datamigration status
```

Step 7

When importing data to the Publisher, Subscriber nodes are not yet available; therefore, configuration data is not synchronized
                                             at that stage.

##### What to do next

To replicate the migrated Unified Intelligence Center configuration database from the Publisher to the Subscriber nodes, execute
                                    the following command:

After the initial component data import and database synchronization, restart all Unified Intelligence Center nodes. This also restarts the co-resident Cisco
                                                IdS components. After subsequent imports on the publisher, restart only the subscriber nodes.

#### Post Migration configuration for Unified Intelligence Center

After importing the configurations, complete the following steps:

Step 1

Data Source Configuration

During Unified Intelligence Center data migration, all data source details-including database hostname, username, and password
                                                are migrated seamlessly. If the details for the data sources such as hostnames and credentials are unchanged, reconfiguration
                                                is not needed. However, if any data source details are modified on the target system, reconfiguration will be required. 
                                                
                                                For more information, see the Data Source Actions section in the Configure chapter of Cisco Unified Intelligence Center Report Customization Guide.

Data Source Hostname to IP mapping Unified Intelligence Center can be configured to connect to different AWDB or HDS servers to distribute reporting load. The
                                                Unified Intelligence Center-to-AWDB mapping is migrated during the data migration process. If AWDB or HDS details are changed
                                                on destination, you must reconfigure the host-to-IP mapping on all Unified Intelligence Center nodes using the following CLI
                                                command: 
                                                
                                                set cuic properties host-to-ip 
                                                
                                                For more information, see the set cuic properties host-to-ip section in the Command Line Interface chapter in Administration Console User Guide for Cisco Unified Intelligence Center.

Step 2

Active Directory Configuration

Active Directory configuration in OAMP is fully migrated, eliminating the need for any post-migration reconfiguration. 
                                                
                                                For more information, see Configure Active Directory section in Cluster Configuration Chapter of Administration Console User Guide for Cisco Unified Intelligence Center.

Step 3

SMTP Configuration

SMTP details-including username, password, and hostname-are migrated automatically. No further changes are required if the
                                                target system uses the same SMTP server.

For more information, see Configure SMTP Settings section in Cluster Configuration Chapter of Administration Console User Guide for Cisco Unified Intelligence Center.

Step 4

Cross-Origin Resource Sharing (CORS) Configuration

Unified Intelligence Center CORS configuration stores the hostnames of Finesse servers hosting the Unified Intelligence Center
                                                gadget. These hostname details are migrated during the Unified Intelligence Center data migration process.

If the Finesse hostnames remain the same between source and target, no reconfiguration is necessary.

```
utils cuic cors allowed_origin add utils live-data cors allowed_origin list
```

For more details, see the utils cuic cors section of Command Line Interface chapter in Administration Console User Guide for Cisco Unified Intelligence Center.

Step 5

Certificate Exchange

(Perform this step only if self-signed certificates are in use.)

All certificates are migrated to the target systems during data migration. Unified Intelligence Center stores certificates
                                                for Live Data, Cisco IdS, and Finesse in the platform trust store.

If the hostnames for Live Data, Cisco IdS, or Finesse change, the corresponding certificates must be imported into Unified
                                                Intelligence Center using Cisco Unified OS Administration.

For more information about Self-Signed Certificates, see the Post Installation section in Installation chapter of Installation and Upgrade Guide for Cisco Unified Intelligence Center.

Step 6

Unified Intelligence Center Gadgets in Finesse

Gadget URLs in Finesse Administration Console must be updated to reference the new Unified Intelligence Center FQDN.

For more information, see the Gadgets and Components section in the Manage Desktop Layout chapter of Cisco Finesse Administration Guide .

### Live Data - Migration from VMware to Nutanix

For a standalone Live Data deployment, perform the following tasks in the specified sequence.

In a 2000-agent deployment, Live Data is co-resident with Unified Intelligence Center and Cisco IdS. Migrate the co-resident
                                             VM by following Unified Intelligence Center - Migration from VMware to Nutanix . Configuration performed on the Unified Intelligence Center co-resident VM also applies to the co-resident Live Data and
                                             Cisco IdS components. Do not repeat the Live Data export and import procedures. After migrating the co-resident VM, complete Post-Migration Configuration for Live Data .

Sequence

Task

1

Before you Begin

2

Export Platform Data from the Source VM to the Remote Server

3

Upload OVA on Nutanix

4

Create a Virtual Machine from the OVA on Nutanix

5

Export Live Data from the Source Publisher VM to the Remote Server

6

Export Live Data from the Source Subscriber VM to the Remote Server

7

Shut Down the Source VM(s)

8

Fresh Install the Publisher VM on Nutanix Using Exported Platform Data

9

Import Live Data from the Remote Server to the Destination VM (Publisher)

10

Fresh Install the Subscriber VM on Nutanix Using Exported Platform Data

11

Import Live Data from the Remote Server to the Destination VM (Subscriber)

12

Post-Migration Configuration for Live Data

#### Before you Begin

Verify the following before proceeding with the standalone Live Data export:

Supported Versions : CCE supports standalone Live Data migration when the source is on one of the following versions:

Version 15.0(1) ES202511

Version 15.0(1) SU1

Version 15.0(1) SU2

Version 12.6(2) ES08

Ensure that Live Data failover is configured correctly by running the following command:

For more information, see the show live-data failover section in the Live Data Serviceability chapter of the Serviceability Guide for Cisco Unified Contact Center Enterprise .

Verify that the Live Data Administration and Data Server Database (AWDB) configuration is correct. Run the following CLI command:

For more information, see the CLI commands chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Use this workflow only for a standalone Live Data deployment. For a 2000-agent co-resident deployment, follow the Unified
                                                Intelligence Center migration workflow.

#### Export Platform Data from the Source VM to the Remote Server

For more information, see the Export Platform Data from the Source VM to the Remote Server section in this guide.

#### Upload OVA on Nutanix

For more information, see the Upload OVA on Nutanix section in this guide.

#### Create a Virtual Machine from the OVA on Nutanix

For more information, see the Create a Virtual Machine from the OVA on Nutanix section in this guide.

#### Export Live Data from the Source Publisher VM to the Remote Server

To export the Live Data configuration from the source publisher to the remote server, perform the following steps:

Step 1

Log in to the Live Data publisher CLI using administrator credentials.

Step 2

To initiate the export, run the following CLI command:

```
utils component dataexport initiate
```

When prompted for the export directory, enter an absolute path that begins with a forward slash (/).

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the path of the directory to which the data should be exported.

Step 5

Enter the hostname and IP address of the destination VM.

Step 6

Enter "yes" when prompted to proceed with the export. The data export begins. Monitor its progress in the log by running the
                                                file tail command available on the CLI interface.

Step 7

To check the data export status, run the following command:

```
utils component datamigration status
```

#### Export Live Data from the Source Subscriber VM to the Remote Server

To export the Live Data configuration from the source subscriber to the remote server, perform the following steps:

Step 1

Log in to the Live Data subscriber CLI using administrator credentials.

Step 2

Run the following CLI command to initiate the export:

```
utils component dataexport initiate
```

When prompted for the export directory, enter an absolute path that begins with a forward slash (/).

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

Enter the path of the directory to which the data should be exported.

Step 5

Enter the hostname and IP address of the destination VM.

Step 6

Enter "yes" when prompted to proceed with the export. The data export begins .

Step 7

Monitor the data export progress in the log by running the file tail command available on the CLI interface.

Step 8

To check the data export status, run the following command:

```
utils component datamigration status
```

#### Shut down the Source VM(s)

For more information, see the Shut down in the Source VM(s) section in this guide.

#### Fresh Install VM with Import option on Nutanix Using Exported Platform Data

For more information, see the Fresh Install VM with Import option on Nutanix Using Exported Platform Data section in this guide.

#### Import Live Data from the Remote Server to the Destination VM (Publisher)

To import the Live Data configuration from the remote server to the destination publisher VM, perform the following steps:

Step 1

Log in to the Live Data publisher CLI using administrator credentials.

Step 2

Run the following CLI command to initiate the import:

```
utils component dataimport initiate
```

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

For the Data Directory, specify the directory name and path.

Step 5

Confirm the data import by entering "yes" when prompted. The data import begins. Monitor its progress in the log by running
                                             the file tail command available on the CLI interface.

Step 6

To check the component data import status, run the following command:

```
utils component datamigration status
```

##### What to do next

Before installing the destination subscriber, verify the subscriber information on the destination publisher.

If the destination subscriber uses a different hostname or IP address from the source subscriber, add the destination secondary
                                    node by using the supported Live Data CLI procedure. For more information, see the Set Live Data Secondary Node section in the Installation chapter.

If the destination subscriber retains the source hostname and IP address, no manual subscriber configuration is required.

#### Import Live Data from the Remote Server to the Destination VM (Subscriber)

To import the Live Data configuration from the remote server to the destination subscriber VM, perform the following steps:

Step 1

Log in to the Live Data subscriber CLI using administrator credentials.

Step 2

Run the following CLI command to initiate the import:

```
utils component dataimport initiate
```

Step 3

Enter the remote server's IP address, login ID, and password.

Step 4

For the Data Directory, specify the directory name and path.

Step 5

Confirm the data import by entering "yes" when prompted. The data import begins. Monitor its progress in the log by running
                                             the file tail command available on the CLI interface.

Step 6

To check the component data import status, run the following command:

```
utils component datamigration status
```

##### What to do next

After the initial component data import, restart all Live Data nodes. After subsequent imports on the publisher, restart only the subscriber nodes.

#### Post Migration configuration for Live Data

After importing the configurations, complete the following steps:

Step 1

Inventory addition (Only for 2000 deployment models)

Live Data configuration is managed through CCE inventory management. You must reconfigure the inventory by deleting the old
                                                entries for the Unified Intelligence Center-LD-Cisco IdS publisher nodes (which also deletes the subscriber) and adding new
                                                Unified Intelligence Center-LD-Cisco IdS publisher and subscriber nodes.

For more information, see the Configure Live Data with AW topic.

For more information, see the Migrate from Co-Resident Deployment to Standalone Deployment topic.

Step 2

AWDB Access configuration

After Live Data migration, run the following CLI command:

Step 3

Machine Service Configuration (4000 and above deployment models only)

The Machine Services CLI stores Live Data information.

After Live Data migration, run the following command:

Step 4

CORS Configuration

Live Data CORS configuration saves the hostnames where Finesse is hosted. These values are migrated during Live Data migration.
                                                If the Finesse hostnames remain the same on both source and target systems, no reconfiguration is required.

If the Finesse hostnames differ between source and target, reconfiguration is necessary. Run the following CORS command:

Step 5

Data source Details in Unified Intelligence Center

Store Live Data source details in Unified Intelligence Center to enable live data reporting. If Live Data hostnames change,
                                                update the data source details in Unified Intelligence Center by running the following CLI command on the Live Data server:

Step 6

Certificate Exchange

(Perform this step only if self-signed certificates are in use.)

All certificates are migrated to the target systems during Live Data migration.

Live Data stores the certificates for the Unified Intelligence Center and the AWDB in the platform trust store. If the hostnames
                                                for the Unified Intelligence Center or AWDB change, import their certificates into Live Data using Cisco Unified OS Administration.

For more information about Self-Signed Certificates, see the Post Installation section in the Installation chapter of Installation and Upgrade Guide for Cisco Unified Intelligence Center.

##### Example

### Enterprise Chat and Email-Migration from VMware to Nutanix

To migrate Enterprise Chat & Email from VMware to Nutanix, see the procedures described in the following ECE guides at https://www.cisco.com/c/en/us/support/contact-center/enterprise-chat-email-15-0-1/model.html .

### Unified CCMP - Migration from VMware to Nutanix

To migrate Unified CCMP from VMware to Nutanix, see the procedures described in the following Unified CCMP guides at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/series.html .

## Nutanix Move Migration

Nutanix Move migrates virtual machines (VMs) from VMware ESXi to Nutanix AHV with minimal downtime.

Nutanix Move operations require the appliances to be shut down on the source hypervisor , which results in service disruption. Schedule these activities during a planned maintenance window.

### Prerequisites

Ensure that the Nutanix Element cluster and Prism Central are reachable from both hypervisor networks .

Download the Nutanix Move QCOW2 or OVA image from the Nutanix Support Portal .

Ensure that network access and static IP addressing are ready for the Nutanix Move appliance configuration.

Ensure that the user has administrator-level privileges for the source environment, such as vCenter administrator credentials,
                                    and target Nutanix administrator credentials for Prism Central and the cluster.

Ensure that the Nutanix Move VM has network connectivity to the vCenter Server to discover and retrieve metadata for the VMs
                                    targeted for migration.

Ensure that the required network ports are open and that the system has sufficient bandwidth and compute capacity to support
                                    the migration.

Disable backup solutions, including snapshot schedules and third-party tools such as Cohesity or Veeam, for the duration of
                                    the Nutanix Move operation.

Nutanix Move uses VMware snapshots and Changed Block Tracking (CBT) to perform incremental data synchronization. Nutanix Move takes its own snapshots, labeled "Move-Snap-", to track data changes during the migration . After cutover, Nutanix Move removes these temporary snapshots as part of its cleanup process.

If another backup application takes or deletes snapshots while a Nutanix Move operation is in progress , the migration may fail. Before Nutanix Move starts migration, current snapshots for that VM are automatically removed.

For details on Microsoft SQL Server migration guidance applicable to CCE AW-HDS-DDS and HDS-DDS servers, see the Nutanix best practices for Microsoft SQL Server .

### Nutanix Move BIOS Mode Compatibility and Migration Considerations

Windows-based CCE VMs deployed using the CCE OVA on VMware use Legacy BIOS mode. The OVAs published for Nutanix are configured
                              with UEFI BIOS mode with Secure Boot enabled.

Migration Behavior

When customers use Nutanix Move to migrate Windows-based CCE VMs from VMware to Nutanix, the migrated VM on Nutanix retains
                              the Legacy BIOS mode from the source VMware VM.

After migration using Nutanix Move, switching from Legacy BIOS mode to UEFI BIOS mode with Secure Boot enabled on Nutanix
                              is not supported.

Recommendations

Windows VMs migrated using Nutanix Move operate in Legacy BIOS mode.

Customers who require UEFI BIOS mode with Secure Boot enabled on Nutanix must perform a fresh installation using the Nutanix-specific
                                    component OVA instead of using Nutanix Move.

### Download Nutanix Move

Download the Nutanix Move image before you deploy the Nutanix Move appliance on Nutanix.

Step 1

Download the Nutanix Move QCOW2 file for AHV from the Nutanix Support Portal .

Step 2

Upload the image to the Nutanix image service in Prism Element or Prism Central.

### Deploy the Nutanix Move VM

Deploy the Nutanix Move VM on Prism Central.

Step 1

Log in to Prism Central for your AHV cluster.

Step 2

Go to VM > Create VM .

Step 3

Select the Nutanix Move QCOW2 image as a disk.

For Disk Operation , choose Clone from Image Service .

Add the required CPU and memory, for example 2 vCPUs and 8 GB RAM.

Step 4

Add a network interface card (NIC) for the management network.

Step 5

Power on the VM.

For more information, see the Nutanix documentation at Deploying Nutanix Move on AHV .

### Change the Default Password

Change the default password after you deploy the Nutanix Move VM.

Step 1

Launch the Nutanix Move VM console from Prism Central or Prism Element .

Step 2

Use the default password nutanix/4u to log in.

For more information, see Changing Admin User Password .

Step 3

Run the following command:

```
passwd
```

Step 4

Enter and reenter the new password when prompted.

Step 5

Verify that the following confirmation appears:

```
passwd: all authentication tokens updated successfully
```

### Assign a Static IP Address

If DHCP is not enabled, you can assign a static IP address for the Nutanix Move VM.

To assign a static IP address, do the following:

Step 1

Log in to the Prism Element UI of the cluster where the Nutanix Move VM is deployed using the admin user credentials.

Step 2

Go to Entity > Virtual Infrastructure > VMs .

Step 3

Select the VM named Nutanix-Move .

Step 4

Open a remote console on the Nutanix Move VM and log in with the Nutanix Move admin user credentials.

For more information about credential details, see Change the Default Password of Nutanix Move .

Step 5

Run the following command to switch to the root user and enter the password of the Nutanix Move VM.

admin@move on ~ $ rs

The first time that the Nutanix Move CLI is launched , the script runs automatically.

Step 6

Run the following command to configure the static IP address.

root@move on ~ $ configure-static-ip

Step 7

Enter the required IP address and netmask values.

### Log In to the Nutanix Move Console

Log in to the Nutanix Move console after the Nutanix Move appliance is deployed and reachable on the network.

Step 1

In a browser, enter https://<Nutanix-Move-VM-IP>/ .

Step 2

Accept the EULA and set the initial administrator password.

Step 3

Log in to the Nutanix Move dashboard.

### Add Migration Environments

Add the source and target migration environments in Nutanix Move.

Source environment: VMware vCenter Server or a standalone ESXi host.

Target environment: Nutanix AOS cluster.

Step 1

In the Nutanix Move UI, go to Environments > Add Environment .

Step 2

Choose the environment type.

Step 3

Enter the following environment details:

Environment name

Environment IP address

Administrator user name and password

Step 4

Click Add .

The user must have administrator-level privileges on both the source and destination environments.

For more information, see Adding vCenter Server or Standalone ESXi Host Environment .

For more information about adding the target environment, see Adding a Nutanix AOS Cluster Environment .

### Create and Execute a Migration Plan

A migration plan defines what is migrating, the source environment, the target environment, and the migration settings.

Step 1

In the Nutanix Move dashboard, click New Migration Plan .

Step 2

In the Plan Name field, enter a unique name for the migration plan and click Proceed .

Step 3

On the Source & Target screen, configure the source and target environment details.

From the Select a Source drop-down list, select the VMware source environment.

From the Select a Target drop-down list, select the Nutanix target environment.

From the Target Project drop-down list, select the target project, if applicable.

From the Target Cluster drop-down list, select the Nutanix target cluster.

From the Target Container drop-down list, select the storage container for the migrated VMs.

Review the Security Policy section.

If no NSX or FNS environment is configured for the selected source or target, no security policy is applied from this screen.

Click Next .

Step 4

On the Select VMs screen, add the VMs that you want to migrate.

Use the search field or filter options to locate the required VMs.

Select the add icon or checkbox for each VM that you want to include in the migration plan.

Review the Added VMs pane and verify that all required VMs are listed.

Review any warnings that are shown for the selected VMs.

Click Next .

Step 5

On the Network and Policy screen, configure the network mapping.

For each Source Network , select the corresponding Target Network .

If you are creating a test migration, select the required subnet from the Test Network drop-down list.

The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts.

Review the Security Policies section.

If no NSX or FNS environment is found for the selected source or target, no security policy is applied from this screen.

Click Next .

Step 6

On the VM Preparation screen, configure the VM preparation and guest operation settings.

From the Preparation Mode drop-down list, select the preparation mode.

If you select Automatic , Nutanix Move prepares the VMs using the credentials that you provide.

From the IP Configurations for target VMs drop-down list, select whether to retain the source IP configurations.

Select Uninstall VMware tools on target VMs .

If this option is not selected, migration can fail with a VMware Tools unrecoverable error.

Select Install Nutanix Guest Tools (NGT) on target VMs , if required.

Select Bypass guest operations on source VMs , if required.

In the Credentials for Source VMs section, provide the required credentials.

For Windows VMs, provide administrator credentials. For Linux VMs, provide root credentials, or select Use Private (.PEM) file to authenticate if private key authentication is used.

For Linux VMs, credentials are not required if guest operations are not used.

In the Post Migration Automation section, select Configure a Runbook to automate post-migration tasks on VMs , if required.

In the Override individual VM Preparation section, click Change settings if you need to change the preparation mode or credentials for individual VMs.

Click Next .

Step 7

On the VM Settings screen, configure migration settings for the VMs.

From the VMs Priority drop-down list, select the migration priority.

From the Timezone drop-down list, select the timezone.

If you select Default , Nutanix Move configures the UTC timezone for Linux VMs and the cluster timezone for Windows VMs.

Select Retain MAC addresses from the source VMs , if required.

Select Skip CDROM Addition on target VMs , if required.

Select Enable Memory Overcommit , if required.

In the Category/Tag Settings section, select one of the category or tag options.

You can select and apply target categories for all VMs in the migration plan, or assign source tags and categories to the
                                                   target based on mappings.

In the VM Migration Type section, select one of the VM property options.

You can configure target VM properties, or retain source VM properties.

In the Settings for Individual VMs section, click Change settings if you need to configure settings for individual VMs.

Select Schedule Data Seeding , if required.

Click Next .

Step 8

On the Summary screen, validate the migration plan details.

Review the Source Environment Details , including the environment type, name, source IP, and number of VMs to migrate.

Review the Target Environment Details , including the target cluster and container.

Review the Network Mapping , including the source network and target network.

Click Save to save the plan, or click Save and Start to save the plan and start data seeding.

Step 9

Monitor the migration plan until the VM status changes to Ready to Cutover .

The migration plan shows the migrated data size, migration status, and estimated cutover time for each VM.

Step 10

Perform the production cutover.

Select the VM that is ready for cutover.

Click Cutover .

Review the confirmation message and click Continue .

After you continue, the source VMs shut down, the virtual NICs of the source VMs are disconnected, and each source VM is updated
                                                               with a migration note. The operation can take some time to update the VM state in the UI.

Step 11

Validate that the migrated VM is available on Nutanix Prism Element or Prism Central.

### Create a Test Migration

Test migration in Nutanix Move creates a temporary cloned VM on the target Nutanix AHV cluster while the source production
                                 VM continues to run. Use test migration for validation, application testing, and pre-cutover checks without impacting production
                                 workloads.

Create the migration plan as described in Create a Migration Plan , with the differences described in this task.

Step 1

On the Network and Policy screen, select a test network.

From the Test Network drop-down list, select the subnet to use for test migration.

The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts.

Step 2

Complete the remaining migration plan screens and click Save and Start .

Use the same source, target, VM preparation, VM settings, and summary validation workflow described in Create a Migration Plan .

Step 3

Monitor the migration plan until the VM status changes to Ready to Cutover .

Step 4

Select the VM for which you want to create a test VM.

Step 5

From the Test Actions menu, select Create Test VM .

Nutanix Move creates the test VM on the target Nutanix cluster. Test VM names are suffixed with -MoveTest in the target network.

Step 6

Validate that the test VM is available in Nutanix Prism Element or Prism Central.

Step 7

Perform the required application validation on the test VM.

Step 8

After validation is complete, return to the Nutanix Move dashboard and continue with cutover when you are ready to migrate to the production environment.

When you proceed with cutover, Nutanix Move removes the test VM that was created on the Nutanix cluster.

### Restore the Source VM After Migration Failure

Use this procedure to restore the source VM if migration fails.

The source VMware virtual machine is powered off, and its network interface is changed to a disconnected state.

Step 1

Log in to VMware vCenter and locate the source virtual machine used for migration.

Step 2

Edit the VM settings and update the network adapter.

Set the network adapter to Connected .

Select Connect At Power On .

Step 3

Power on the virtual machine.

## Troubleshooting

Sequence

Troubleshooting

1

Common Issues for Windows-based CCE Components

2

Common Issues for VOS-based Components

3

Cisco VVB

4

Unified Intelligence Center and Live Data

5

Finesse

6

Cisco IdS

7

Restore the Source VM After Migration Failure (Nutanix Move)

### Common Issues for Windows-based CCE Components

This section provides information for troubleshooting Windows-based CCE components, including Cisco Unified Intelligent Contact
                                 Management (ICM) Enterprise (Unified ICM), Unified CVP, ECE, and Unified CCMP.

Issue

Resolution

When a user attempts to revert a VM to a snapshot with UUID <ID>, they may encounter the error "Failed to revert the VM with
                                             UUID <ID>" if Nutanix Guest Tools (NGT) tools are installed on the VM but not present in the snapshot. This issue arises because
                                             the snapshot does not contain the NGT tools required by the VM.

Uninstall the NGT tools from the VM, then revert to the desired snapshot.

If the timezone of the deployed Windows CCE VM differs from the default UTC timezone of the hardware clock in AHV, a temporary
                                             flip to the UTC timezone may occur during the restart of the Windows CCE VM. This time difference can be observed in application
                                             logs that capture events before and after the power cycle.

For detailed recommendations on handling timezone settings for Windows VMs deployed in Nutanix AHV environments, see the Nutanix Knowledge Base article .

Ensure that NTP is properly configured on the Windows VMs, and apply relevant Microsoft timezone updates as part of regular
                                             maintenance to keep timezone information current.

### Common Issues for VOS-based Components

This section provides information for troubleshooting VOS-based components.

Issue

Resolution

SFTP validation error- SSH algorithm negotiation failure During the export and import operation of data migration, if you encounter the SFTP validation error-SSH algorithm negotiation
                                             failed.

Ensure deployed SFTP server is configured with strong cryptographic algorithms.

#### Upgrade Failures in VOS-based Components

For common VOS-based upgrade errors and how to fix them, see the Troubleshooting Unified Communications Manager Upgrades topic in the Troubleshooting chapter of the Upgrade and Migration Guide for Unified CM and the IM and Presence Service, Release 15 and SUs guide at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/15/cucm_b_upgrade-and-migration-guide_15/cucm_m_troubleshooting.html

### Cisco VVB

This section provides information for troubleshooting Cisco VVB.

Issues

Resolution

Export CLI failure: The export CLI command exited with a failure status.

Ensure that all the services are up and running by using the following CLI command:

```
utils service list
```

Retry the export CLI command.

Cisco VVB import fails due to backup issues: Corrupted or incomplete export data can cause import failures.

Redo the export and re-run the following CLI command:

```
utils component dataexport initiate
```

Component import fails when platform data is not imported first:

Cisco VVB depends on platform services and certificates.

Complete and verify platform data import is successful before starting component import.

Issues arise from network and host configuration conflicts:

IP, DNS, and hosts mismatch causes service and UI access failures.

Verify network settings and update the hosts file post-import if needed.

Import is interrupted, or configurations change during migration: VM reboot, power loss, or any administrator changes can leave Cisco VVB in an inconsistent state.

Maintain a stable environment and freeze all Cisco VVB configuration changes during export/import.

OVA profile or resource mismatches affect Cisco VVB migration

Incorrect OVA size or insufficient CPU or RAM leads to unstable services.

Ensure source and destination use the same OVA profile with adequate resources.

### Unified Intelligence Center and Live Data

This section provides information for troubleshooting Unified Intelligence Center and Live Data.

Issues

Resolution

Unified Intelligence Center

Data Sources are offline

As part of the Unified Intelligence Center data migration, all data source configurations have been migrated.

If configuration details such as IP/hostname, username, or credentials are different on the Nutanix system, modify the data
                                          sources accordingly and validate that the data sources come online. For more information, see the Data Sources section in
                                          the Configure chapter of the Cisco Unified Intelligence Center Report Customization Guide.

Scheduled report mails are not working

The SMTP configuration in OAMP is migrated as part of the Unified Intelligence Center data migration upgrade. If the SMTP
                                          server details on the Nutanix system are different, reconfigure them in OAMP.

If SMTP over TLS is used, import the new SMTP server TLS certificate from source. For more information, see the Configure
                                          SMTP Settings section in the Cluster Configuration chapter of the Administration Console User Guide for Cisco Unified Intelligence Center.

LDAP login does not work

Active Directory settings are migrated as part of the Unified Intelligence Center data upgrade. If a different Active Directory
                                          is used on the Nutanix system, reconfigure the Active Directory settings in OAMP. For more information, see the Configure
                                          Active Directory Settings section in the Cluster Configuration chapter of the Administration Console User Guide for Cisco Unified Intelligence Center .

Unified Intelligence Center Historical Gadgets in Finesse desktop does not load

Check the Unified Intelligence Center CORS configuration by running the following CLI command:

```
utils cuic cors allowed_origins list
```

Ensure the correct Finesse hostnames are listed in the URLs. For more information, see the utils cuic cors section in the Command Line Interface chapter of the Administration Console User Guide for Cisco Unified Intelligence Center, Release 15.0(1) .

Live Data

Live Data Gadgets in Finesse desktop does not load

Check the LD CORS configuration by running the following CLI command:

```
utils live-data cors allowed_origins list
```

For more information, see the Configure Cross Origin Resource Sharing (CORS) for Live Data section in the Installation chapter of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Ensure that the correct Finesse hostnames are listed in the URLs.

Ensure Live Data failover state is either Active or Standby by running the following CLI command:

```
show live-data failover
```

If LD is shown as out-of-service

Check Live Data aw-access configuration by running the following CLI command:

```
show live-data aw-access
```

Ensure that the test connection is successful.

If Test connection fails, run the following CLI command to re-configure the AWDB details:

```
set live-data aw-access primary
```

```
set live-data aw-access secondary
```

Only for 4000 and above deployment models

To register LD details on AWDB, run the following CLI command:

```
set live-data machine-services
```

To update the Live Data configuration on Unified Intelligence Center, run the following CLI command:

```
set live-data cuic-datasource
```

For more information on the CLI commands, see the CLI commands chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Live Data reports do not load

Ensure Live Data failover state is either Active or Standby by running the following CLI command:

```
show live-data failover
```

If LD is shown as out-of-service check Live Data aw-access configuration by running the following CLI command:

```
show live-data aw-access
```

Ensure that the test connection is successful.

If Test connection fails, run the following CLI command to re-configure the AWDB details:

```
set live-data aw-access primary
```

```
set live-data aw-access secondary
```

Only on 4000 and above deployment models

Run the following CLI command to register LD details on AWDB:

```
set live-data machine-services
```

To update the LD configuration on Unified Intelligence Center, run the set live-data cuic-datasource .

For more information on the CLI commands, see the CLI commands chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

### Finesse

This section provides information for troubleshooting Finesse.

Issues

Resolution

Finesse data sources or the CTI server are offline.

During Finesse data migration, AWDB server configurations are migrated. If configurations such as IP address, hostname, port,
                                             username, or credentials differ on the Nutanix system, update the data sources accordingly. Then, restart the "Finesse Tomcat"
                                             service to confirm that the data sources are online. 
                                             
                                             For more information, see the Contact Center Enterprise CTI Server Settings section in the Manage System Settings chapter
                                             of Cisco Finesse Administration Guide.

Database replication failure

On the Publisher node, run the following admin CLI command:

```
utils dbreplication runtimestate
```

If replication is out of sync, follow these steps:

Stop database replication on the publisher node by running the following CLI command:

```
utils dbreplication stop all
```

Reset database replication on the publisher node by running the CLI command:

```
utils dbreplication reset all
```

After a few minutes, monitor the rebuild process by running the following CLI command:

```
utils dbreplication runtimestate
```

For more information, see the Replication Status section in the Finesse CLI chapter of Cisco Finesse Administration Guide.

The Finesse subscriber node is out of service.

In cfadmin, verify that the secondary Finesse server is configured with the correct hostname.

If the Finesse publisher node is in service and database replication is synchronized, but the subscriber node is out of service,
                                             run the following admin CLI command to force synchronization of the database from the publisher to the subscriber node:

```
utils dbreplication forcedatasyncsub
```

A third-party Finesse gadget fails to load.

Log in to cfadmin and verify that there are no errors on the Desktop Layout page and that the gadget is included in the XML
                                             configuration. 
                                             
                                             For more information, see the Gadgets and Components section in the Manage Desktop Layout chapter of Cisco Finesse Administration Guide.

Log into 3rdpartygadget Account to verify that the third-party gadgets are configured with required permissions. 
                                             
                                             For more information, see the 3rdpartygadget Account section in Manage Third-Party Gadgets chapter of Cisco Finesse Administration Guide.

After logging into the Finesse desktop, the desktop layout, reason codes, phonebook, or workflows are not found.

Log in to Finesse Administrator Console and verify that the desktop layout, reason codes, phonebook, and workflows are available
                                             and have been migrated from the source Finesse VM.

Review the Finesse data migration import logs for any errors.

Perform the export and import again or manually add the failed configurations. 
                                                   For more information, see the Cisco Finesse Administration Guide.

### Cisco IdS

This section provides information for troubleshooting Cisco IdS.

Issues

Resolution

Invalid SSO client configuration

As part of the Cisco IdS data migration, all Cisco IdS client data has been migrated. If the IP address, hostname, or port
                                          configuration of the SSO clients differs on the Nutanix system, modify or add those clients accordingly and validate the changes.
                                          
                                          
                                          For more information, see the Hostname or IP Address Change section in the Cisco IdS for Single Sign-On chapter of

Cisco Unified Contact Center Enterprise Features Guide .

Unknown certificate error

Upload the Cisco IdS Tomcat certificate to the SSO clients' trust store. 
                                          
                                          For more information, see the Certificates for Cisco IdS chapter of Cisco Finesse Administration Guide .

Cisco IdS-to-IdP trust failure

It is necessary to regenerate the SAML certificate in Cisco IdS and establish trust between Cisco IdS and the IdP. 
                                          
                                          For more information, see the Configure an Identity Provider section in the Cisco IdS for Single Sign-On chapter

of Cisco Unified Contact Center Enterprise Features Guide.

## Caveats

This section contains caveats that are specific to data migration from VMware to Nutanix.

Component

Description

Any Impact

Unified Intelligence Center

Unified Intelligence Center VM exhibits a surge in CPU usage in the Nutanix environment.

No functional impact

Finesse

Finesse VM exhibits a surge in CPU usage on the Nutanix environment.

No functional impact

| Note | Platform data migration is a one-time event during component deployment on Nutanix. Application data can be exported from
                                                VMware and imported after deployment on Nutanix, and prior to or during the production cutover. |
|---|---|

| CCE Components | Source (VMware) Version | Nutanix target version |
|---|---|---|
|  | Supported 15.0(1) VMware source version | Supported 12.6(2) VMware source version |
| CCE VOS-based Components |
| Cloud Connect | 15.0(1) with ES202511 (or) 15.0(1) SU1 (or) 15.0(1) SU2 | 12.6(2) ES 04 | 15.0(1) SU2 |
| Finesse | 15.0(1) with ES202511 (or) 15.0(1) SU1 (or) 15.0(1) SU2 | 12.6(2) ES 07 |
| Cisco VVB | 15.0(1) with ES202511 (or) 15.0(1) SU1 (or) 15.0(1) SU2 | 12.6(2) ES 08 |
| Unified Intelligence Center Cisco Live Data Cisco Identity Service (Cisco IdS) | 15.0(1) with ES202511 (or) 15.0(1) SU1 (or) 15.0(1) SU2 | 12.6(2) ES 08 |  |
| CCE Windows-based Components |
| Unified CCE | 15.0(1) with ES202607 or later | 12.6(2) with ES 102 on AW, ES 108 on PG, ES 103 on Router, Logger, & Rogger | 15.0(1) with ES202607 or later |
| Unified CVP | 12.6(2) with ES 25 or later |
| ECE | 12.6(1) ES 13 or later |
| Unified CCMP | 12.6(1) ES 15 or later |

| Note | TCP Port 9440 is the default port used by Nutanix Prism Central for management of traffic, including web console access (HTTPS), REST API
                                             calls, and communication between Prism Element and Prism Central. For more information, see the following Nutanix documentation: AHV Administration Guide Prism Central Guide |
|---|---|

| Note | The administrator should be familiar with building and managing Nutanix clusters, deploying VMs on Nutanix clusters, and using
                                             Nutanix tools and technologies. |
|---|---|

| Note | Uninstallation of the Unified CCE base installation on Windows Server is not supported for Release 15.0(1). This limitation
                                                   does not apply to Unified CCE client packages, which can be removed and reinstalled. For more information, see the Uninstallation
                                                   chapter of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) . |
|---|---|

| Note | If you do not rebuild the server, you may notice missing directories, lost permissions, or corrupted soft links. |
|---|---|

| CCE Components | Download Link | OVA |
|---|---|---|
| Cloud Connect | Download Cloud Connect OVA | CloudConnect_15.0.1-SU2_nutanix_v.3.0.zip |
| Unified CVP | Download Unified CVP OVA | CVP_15.0.1_nutanix_OVAPack_v3.0.zip |
| Cisco VVB | Download Cisco VVB OVA | vvb-15.0.1-SU2-nutanix_v3_OVAs.zip |
| Finesse | Download Finesse OVA | Finesse_15.0.1-SU2_nutanix_OVAPack_v3.0.zip |
| Cisco IdS | Download Cisco IdS OVA | cuic-ova-15.0.1-SU2-nutanix.zip |
| ECE | Download ECE OVA | ECE_15.0_Nutanix_v3.0_OVAs.zip |
| Unified CCMP | Download Unified CCMP OVA | Nutanix_CCMP_OVAs-v3.0.zip |
| Unified Intelligence Center | Download Unified Intelligence Center and Live Data OVAs | cuic-ova-15.0.1-SU2-nutanix.zip |
| Live Data | tempesta-ova-15.0.1-SU2-nutanix.zip |
| Logger, Router, Rogger, Administration and Data Server, PG, Administration Client | Download Unified CCE OVAs | UCCE_15.0.1_Nutanix_v3.0_OVAs.ova.zip |

| Note | On Nutanix, the VM boot mode (Legacy or UEFI) cannot be changed after VM creation. If a VM was created using Legacy BIOS and
                                       UEFI Secure Boot is required, the VM must be deleted and recreated using the appropriate OVA and boot settings. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Upload OVA to Nutanix |
| 2 | Upload Images to Nutanix |
| 3 | Create a Virtual Machine from the OVA on Nutanix |
| 4 | Set Up Third-Party Software |
| 5 | Setup Nutanix Move |

| Step 1 | Log in to Prism Central with admin privileges. |
|---|---|
| Step 2 | From the Application Switcher , select Infrastructure , and then navigate to Compute > OVAs from the navigation bar. |
| Step 3 | Click Upload OVA . |
| Step 4 | Specify the following field information in the Upload OVA screen: |
| Step 5 | OVA Source : Select the OVA source. To upload OVA, there are 2 options available: OVA file (upload a file from the local folder) URL : If you choose URL in the OVA Source field, you can select multiple clusters in the Select AHV Cluster field. |
| Step 6 | Name : Enter the name for the OVA file. By default, Prism Central uses the file name of the OVA file that you upload, if you do not specify OVA file name in the Name
                                             field. |
| Step 7 | Based on the selection in the OVA Source field, perform the following relevant action: OVA file : Click Select File to navigate to the location of the OVA file in your local folder and open it. URL : Enter the source URL from where you want to upload the OVA file. |

| Step 1 | Log in to Prism Central as a user with admin privileges. |
|---|---|
| Step 2 | Choose the Infrastructure application from the Application Switcher, and navigate to Compute > Images from the navigation bar. |
| Step 3 | Click Add Image . The system displays the Add Images screen. |
| Step 4 | Provide the following information in the Select Image step:Image Source - Select the Image File radio button. |
| Step 5 | Click Add File . The system displays file attributes. |
| Step 6 | Browse the location of the image file, and then click Open . |
| Step 7 | Provide the following attributes for the image file: |
| Step 8 | Image Name - Enter the image name. By default, the system pre-fills the name of the file you selected; however, you can change
                                          the image name as per your requirement. Image Type - Select the type of image. Image Description - Enter the description for the image file. |
| Step 9 | Repeat the step if you want to add multiple image files. |
| Step 10 | Click Next after you add all the image files. The system displays the Select Location step. |
| Step 11 | Provide the following information in the Select Location step: |
| Step 12 | Choose Place image directly on clusters to place the images directly on the selected clusters. |
| Step 13 | Select the clusters where you want to add the image file in the Name column. |
| Step 14 | Click Save . The system adds the image files in batches to the selected clusters. |

| Step 1 | Log in to Prism Central. |
|---|---|
| Step 2 | From the Application Switcher, select Infrastructure, and then navigate to Compute > OVAs from the navigation bar. |
| Step 3 | Select the target OVA and choose Deploy as VM from the Actions dropdown menu. The system displays the Deploy as a VM screen. For more information on Uploading an OVA, see the Prism Central Infrastructure Guide . You need Nutanix Support Portal login access to refer to this document. |
| Step 4 | In the Deploy as VM screen, specify the following information in the Configuration step: Name : Enter the name of the VM that needs to be deployed. Description : Enter that description such as Backup VM for Prism. Cluster : Select the target cluster on which you intend to place the guest VM. |
| Step 5 | Click Next . The system displays the Resources step. |
| Step 6 | In the Resources step, go to the Normal NIC (network) section and click Edit (the three-dot icon on the right side of the table). Select the
                                          subnet on which the VM will be deployed, and attach the VM to the appropriate virtual network (VLAN). |
| Step 7 | Click Next . The system displays the Management step. |
| Step 8 | Click Next . The system displays the Review step. |
| Step 9 | Review the deployment configuration in the Review step, and click Create VM . You can check the progress of the deployment task in the Tasks page or from the Tasks icon. |
| Step 10 | After the VM creation is complete, select the VM and click the Disks tab. |
| Step 11 | Select the first CD-ROM device, and under Operation, choose Clone from Image . |
| Step 12 | (For VOS-based components only) Select the required component ISO image from the Image drop-down list. |
| Step 13 | (For Windows-based components only) Select the Windows operating system ISO image from the Image drop-down list. |
| Step 14 | (For Windows based components only) Select the second CD-ROM device, choose Clone from Image, and select the Nutanix VirtIO driver ISO from the Image drop-down list. For more information, see the Adding Images from a Workstation guide . You need Nutanix Support Portal login access to refer to this document |
| Step 15 | Power on the VM. For more information on Deploying an OVA as VM, see the Prism Central Infrastructure Guide . You need Nutanix Support Portal login access to refer to this document. |

| Step 1 | Install Microsoft Windows Server |
|---|---|
| Step 2 | Install Microsoft Windows 11 for Administration Client |
| Step 3 | Install Microsoft SQL Server |

| Step 1 | Select the VM where the Microsoft operating system installation is triggered. |
|---|---|
| Step 2 | Click Launch Console . The Windows console opens in a new window. |
| Step 3 | Select the desired language, time and currency format, and keyboard information. |
| Step 4 | Click Next > Install Now . |
| Step 5 | If prompted, enter the product key for Windows Server and click Next . |
| Step 6 | Select the Desktop Experience option for Windows Server and click Next . |
| Step 7 | Accept the license terms and click Next . |
| Step 8 | Click Next > Custom: Install Windows only (advanced) > Load Driver > OK > Browse . |
| Step 9 | Choose the Nutanix VirtIO driver. |
| Step 10 | Select the Nutanix VirtIO CD drive. |
| Step 11 | Expand the Windows OS folder and click OK . The Select the driver to install window appears. |
| Step 12 | Select all the drivers shown on the Windows Setup screen and click Next . The amd64 folder contains drivers for 64-bit operating systems. The x86 folder contains drivers for 32-bit operating systems. |
| Step 13 | Select the allocated disk space for the VM and click Next . |
| Step 14 | Enter and confirm the password for the administrator account, and then click Finish . |
| Step 15 | Enable Remote Desktop connections as follows: |
| Step 16 | Navigate to Control Panel > System and Security > System . |
| Step 17 | Click Remote Settings . |
| Step 18 | Click the Remote tab. |
| Step 19 | Select the Allow remote connections to this computer radio button. The Remote Desktop Connection dialog displays a notification that the Remote Desktop Firewall exception is
                                             enabled. |
| Step 20 | Click OK . Note: If you are installing Windows SQL Server 2022, instead of Remote Settings, click Remote Desktop . Toggle the Enable Remote Desktop button. Click the Confirm button on the Remote Desktop settings pop-up box. Click Ok . |
| Step 21 | Open the Network and Sharing Center and Click Ethernet in the View your active network info and set up connections section. |
| Step 22 | In the Ethernet Status window, click Properties . |
| Step 23 | In the Ethernet Properties dialog box, configure the following network settings and the Domain Name System (DNS) data: Uncheck Internet Protocol Version 6 (TCP/IPv6) . Select Internet Protocol Version 4 (TCP/IPv4) and click Properties . Select Use the following IP Address . Enter the IP address, subnet mask, and default gateway. Select Use the following DNS Server Address . Enter the preferred DNS server address and click OK . |
| Step 24 | Navigate to Control Panel > System and Security > System . Follow the instructions: |
| Step 25 | Click Change Settings . Note: If you are installing Windows SQL Server 2022, click Rename this PC (advanced) . |
| Step 26 | In the Computer name tab, click Change . |
| Step 27 | Change the name of the computer from the name randomly generated during Microsoft Windows Server installation. The name does
                                             not contain underscores or spaces. |
| Step 28 | Select Domain radio button to change the member from Workgroup to Domain. |
| Step 29 | Enter qualified domain name and click OK . |
| Step 30 | In the Windows security dialog, validate the domain credentials and click OK . |
| Step 31 | Click Ok on successful authentication. |
| Step 32 | Reboot the server and sign in with domain credentials. |
| Step 33 | Go to Settings > Update & Security and run Microsoft Windows Update. |

| Step 1 | On the screen, Where do you want to install Windows , click Load Driver . |
|---|---|
| Step 2 | Click Browse and navigate to the Nutanix VirtIO ISO (mounted as a second CD-ROM). |
| Step 3 | Navigate to w11\amd64 and click OK . |
| Step 4 | Select all the drivers and click Next . |

| Sequence | Task |
|---|---|
| 1 | Download Nutanix Move |
| 2 | Deploy the Nutanix Move VM |
| 3 | Change the Default Password |
| 4 | Assign a Static IP Address |
| 5 | Log In to the Nutanix Move Console |
| 6 | Add Migration Environments |

| Note | Before starting the platform-data migration, record any customized client and server cipher lists, TLS-version settings, and
                                          certificate-type settings on the source node. Depending on the source release and whether the destination uses the same hostname
                                          and IP address, these settings might not be retained. After importing the platform data, verify and reapply the applicable
                                          settings on the destination node. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Export Platform Data from the Source VM to the Remote Server |
| 2 | Shutdown the Source VM(s) |
| 3 | Fresh Install VM with Import option on Nutanix Using Exported Platform Data |

| Step 1 | Log in to the command-line-interface of the Source VM and run the following command: utils system upgrade dataexport initiate |
|---|---|
| Step 2 | Enter the following SFTP server details: Export Data Directory Remote Server Name or IP Remote Server Login ID Remote Server Password |
| Step 3 | Enter the following details of Nutanix destination VM: New Hostname New IP Address |
| Step 4 | When prompted, enter yes to start the export operation. Primary or standalone node: During the export, the system automatically creates a directory on the remote server using the following format and copies
                                                   the exported platform data into it: cluster-<source-IP-address> Secondary node (if applicable): After the primary-node export is complete, log in to the secondary node and repeat this procedure, beginning with utils system upgrade dataexport initiate . At the Export Data Directory prompt, enter the same directory path that you specified during the primary-node export. The subscriber platform data is
                                                   added to the directory created during the primary export: cluster-<source-primary-IP-address> Note The secondary-node platform data export fails if you specify a different Export Data Directory. | Note | The secondary-node platform data export fails if you specify a different Export Data Directory. |
| Note | The secondary-node platform data export fails if you specify a different Export Data Directory. |
| Step 5 | To check whether the data export is complete or in progress, run the following command: utils system upgrade dataexport status |

| Note | The secondary-node platform data export fails if you specify a different Export Data Directory. |
|---|---|

| Note | Consider the following points. They apply to all VOS-based components except the standalone Cisco VVB component: After the primary VM is shut down, secondary nodes operate in a primary-unreachable state. No new cluster formation occurs
                                                during this period. Before shutting down the primary VM, ensure that Maintenance Mode (MM) is initiated and successfully completed on all supported
                                                components, such as Finesse and Cisco IdS. You do not need to shut down all secondary VMs in the cluster together. Shut down only the secondary VMs on which you are
                                                performing a fresh installation with import (migration) . |
|---|---|

| Step 1 | Create a Virtual Machine using the OVA Template. Mount the 15.0(1) SU2 bootable image to the Virtual Machine (VM) and power
                                             on the VM. For more information, see the following sections in this guide: Upload OVA to Nutanix Upload Images to Nutanix Create a Virtual Machine from the OVA on Nutanix |
|---|---|
| Step 2 | Click OK after the media check succeeds. |
| Step 3 | Choose the applicable VOS component and click OK . |
| Step 4 | Click Yes to proceed with installation of the 15.0(1) SU2 build version. |
| Step 5 | Click Import in the Platform Installation Wizard. |
| Step 6 | After reading the displayed information, click OK in the Import Upgrade Configuration information. |
| Step 7 | Choose the appropriate time zone and then click OK . |
| Step 8 | Click Continue in the Auto Negotiation Configuration |
| Step 9 | Click No to have the default value in MTU Configuration . |
| Step 10 | Click No under DHCP Configuration . |
| Step 11 | Provide the same Host Name and IP Address that was used during the export platform data operation; enter IP Mask and Gateway
                                          (GW) Address and then click OK . The destination hostname and IP address can differ from those of the source VM. |
| Step 12 | Click Yes under the DNS Client Configuration . |
| Step 13 | Provide the Primary DNS server's IP Address and Domain and then click OK . |
| Step 14 | Enter the SFTP server IP address, the complete path to the exported platform-data directory, the login ID, and the password.
                                          Specify the platform-data directory in the following format: cluster-<source-primary-IP-address> Then click OK . |
| Step 15 | Provide the organization information on the Certificate Information page and click OK . Note During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                         and IP address as the source: Same hostname and IP address: All source certificates are migrated, including: Tomcat RSA and ECDSA certificates Tomcat trust certificates IPsec and IPsec trust certificates CA-signed certificates, including root and intermediate CA certificates Component certificates uploaded to the Tomcat trust store Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x. Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                               source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname. The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                               issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management . Verify the certificates on the destination node to ensure that all required trust relationships are established. | Note | During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                         and IP address as the source: Same hostname and IP address: All source certificates are migrated, including: Tomcat RSA and ECDSA certificates Tomcat trust certificates IPsec and IPsec trust certificates CA-signed certificates, including root and intermediate CA certificates Component certificates uploaded to the Tomcat trust store Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x. Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                               source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname. The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                               issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management . Verify the certificates on the destination node to ensure that all required trust relationships are established. |
| Note | During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                         and IP address as the source: Same hostname and IP address: All source certificates are migrated, including: Tomcat RSA and ECDSA certificates Tomcat trust certificates IPsec and IPsec trust certificates CA-signed certificates, including root and intermediate CA certificates Component certificates uploaded to the Tomcat trust store Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x. Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                               source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname. The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                               issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management . Verify the certificates on the destination node to ensure that all required trust relationships are established. |
| Step 16 | For a standalone node such as Cisco VVB, skip this step. In the First Node Configuration screen, specify whether you are configuring the first node based on the following: If you are installing the primary node, click Yes under First Node Configuration . If you are installing the secondary node, click No under First Node Configuration . A warning message states that you must configure the first node before continuing. If the first node is already configured,
                                                   click OK . On the Network Connectivity Test Configuration page, click No to proceed with the installation after connectivity is verified. Enter the primary hostname and IP address on the First Node Access Configuration page and click OK . |
| Step 17 | For a secondary node, skip this step. Configure the Network Time Protocol (NTP) server and then click Proceed . |
| Step 18 | On the SMTP Host Configuration screen, choose one of the following: To configure an SMTP host during installation, click Yes and enter the SMTP host information. To continue without configuring an SMTP host, click No . |
| Step 19 | On the Platform Configuration Confirmation page, click OK . |

| Note | During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                         and IP address as the source: Same hostname and IP address: All source certificates are migrated, including: Tomcat RSA and ECDSA certificates Tomcat trust certificates IPsec and IPsec trust certificates CA-signed certificates, including root and intermediate CA certificates Component certificates uploaded to the Tomcat trust store Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x. Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                               source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname. The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                               issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management . Verify the certificates on the destination node to ensure that all required trust relationships are established. |
|---|---|

| Note | Not applicable for single-node publisher-only systems. If the command is run on these systems, the following error message
                                                   will be displayed: Runtime state cannot be performed on a cluster with a single active node; aborting operation |
|---|---|

| Note | The following output is from Cisco Unified Intelligence Center (CUIC). Output details vary by VOS-based component and release. |
|---|---|

|  | Task |
|---|---|
| 1 | CCE Components Migration |
| 2 | Migration of Unified CVP |
| 3 | Platform Data Migration (Common for VOS Components) Note Perform this once for each VOS-based component before the component data is migrated. See the respective sections for the exact sequence and procedure. | Note | Perform this once for each VOS-based component before the component data is migrated. See the respective sections for the exact sequence and procedure. |
| Note | Perform this once for each VOS-based component before the component data is migrated. See the respective sections for the exact sequence and procedure. |
| 4 | Migration of Cloud Connect |
| 5 | Migration of Cisco VVB |
| 6 | Migration of Finesse |
| 7 | Migration of Unified Intelligence Center |
| 8 | Migration of Live Data |
| 9 | Migration of standalone Cisco IdS |
| 10 | Migration of Enterprise Chat and Email |
| 11 | Migration of Unified CCMP |

| Note | Perform this once for each VOS-based component before the component data is migrated. See the respective sections for the exact sequence and procedure. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Before you Begin |
| 2 | CCE Components |
| 3 | Administration Client |
| 4 | Important Considerations |

| Pre-installation Task | Link |
|---|---|
| Download CCE OVA for Nutanix | Contact Center Enterprise OVA for Nutanix |
| Upload CCE OVA on Nutanix | Upload OVA to Nutanix |
| Upload CCE required ISO Images to Nutanix | Upload Images to Nutanix |
| Create a Virtual Machine from the CCE OVA on Nutanix | Create a Virtual Machine from the OVA on Nutanix |
| Install Microsoft Windows Server on the virtual machines deployed for CCE components | Install Microsoft Windows Server |
| Install Microsoft SQL Server for Rogger, Logger and Administration & Data Server VM(s) | Install Microsoft SQL Server |
| Install Microsoft Windows 11 for Administration Client | Install Microsoft Windows 11 for Administration Client |

| Note | Microsoft Visual C++ Redistributable is a prerequisite to install Administration Client on Windows VM deployed on Nutanix.
                                             The latest version of Visual C++ Redistributable can be downloaded from Microsoft, also same is available in AdminClientInstaller
                                             folder. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Create and Execute a Migration Plan |
| 2 | (Optional) Create a Test Migration |

| Note | Nutanix Move performs a virtual-to-virtual (V2V) migration. The cutover requires the source VM to be shut down on the source hypervisor , which results in service disruption. Schedule the migration during a planned maintenance window. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Before you Begin |
| 2 | Migrate Operations Console Server, Call Server, and VXML Server from VMware to Nutanix |
| 3 | Migrate Reporting Server from VMware to Nutanix |

| Note | Nutanix Move migrates all Unified CVP components, including the Reporting Server. The export and import procedures described
                                                   in this section are an alternative method, in which the Reporting Server is migrated separately using database backup and
                                                   restore. |
|---|---|

| Tasks | Link |
|---|---|
| Download Unified CVP OVA for Nutanix | Contact Center Enterprise OVA for Nutanix |
| Upload Unified CVP OVA on Nutanix | Upload OVA to Nutanix |
| Upload Unified CVP required ISO Images to Nutanix | Upload Images to Nutanix |
| Create a Virtual Machine from the Unified CVP OVA on Nutanix | Create a Virtual Machine from the OVA on Nutanix |

| Step 1 | Back up Reporting Server data in the source VMware environment. For more information, see the Database Backup section in the Reporting Guide for Unified CVP at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/reporting/guide/ccvp_b_150_reporting-guide-for-cisco-unified-customer-voice-portal/cvp_m_150_database-management.html#CCVP_RF_D0FBDA2C_00 |
|---|---|
| Step 2 | Restore Reporting Server data in the destination Nutanix environment. For more information about the restore command, see
                                             the Database Backup section in the Reporting Guide for Unified CVP at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/reporting/guide/ccvp_b_150_reporting-guide-for-cisco-unified-customer-voice-portal/cvp_m_150_database-management.html#CCVP_RF_D0FBDA2C_00 |

| Sequence | Task |
|---|---|
| 1 | Before you Begin |
| 2 | Export Platform Data Separately from the Source Publisher and Subscriber VMs to the Remote Server |
| 3 | Export Cloud Connect Application Data from the Source Publisher VM Only to the Remote Server |
| 4 | Upload OVA to Nutanix |
| 5 | Create a Virtual Machine from the OVA on Nutanix |
| 6 | Shutdown the Source VM(s) |
| 7 | Fresh Install Destination VM(s) with Import option on Nutanix Using Exported Platform Data |
| 8 | Import Cloud Connect Application Data from the Remote Server to the Destination Publisher VM |
| 9 | Post migration configuration of Cloud Connect |

| Source release | Cloud Connect containers |
|---|---|
| 15.0(1) ES202511 or later | certmgmt dataconn featureflagmgmt cloudconnectmgmt cache-service cce-cdn digitalrouting inventory |
| 12.6(2) ES04 or later | digitalrouting cloudconnectmgmt inventory cherrypoint dataconn |

| Step 1 | Log in to the CLI of the source Cloud Connect publisher using administrator credentials. |
|---|---|
| Step 2 | Run the following command and verify that the Current Schema Version matches the Latest Schema Version for every configuration item displayed: utils cloudconnect config status The configuration sources, file names, and schema versions displayed by this command vary depending on the Cloud Connect release
                                                and Engineering Special installed. The following output is an example from Cloud Connect 15.0(1) SU2 : admin:utils cloudconnect config status
Source:
1)digitalrouting
2)cloudconnectmgmt
3)featureflagmgmt
q)quit

Please select an option(1-3 or "q" ): 1
Fetching existing configuration...
taskQueueSettings.json : Current Schema Version : 0 Latest Schema Version : 0
eccVariable.json : Current Schema Version : 0 Latest Schema Version : 0
notificationClients.json : Current Schema Version : 0 Latest Schema Version : 0
mediaChannels.json : Current Schema Version : 2 Latest Schema Version : 2
digitalRoutingConfig.json : Current Schema Version : 1 Latest Schema Version : 1
admin:utils cloudconnect config status
Source:
1)digitalrouting
2)cloudconnectmgmt
3)featureflagmgmt
q)quit

Please select an option(1-3 or "q" ): 2
Fetching existing configuration...
oauth2config.conf : Current Schema Version : 0 Latest Schema Version : 0
admin:utils cloudconnect config status
Source:
1)digitalrouting
2)cloudconnectmgmt
3)featureflagmgmt
q)quit

Please select an option(1-3 or "q" ): 3
Fetching existing configuration...
featureflagconfig.json : Current Schema Version : 1 Latest Schema Version : 1
admin: |
| Step 3 | To initiate the export, run the following command: utils component dataexport initiate When prompted for the export directory, enter an absolute path that begins with a forward slash (/). |
| Step 4 | Enter the remote server's IP address, login ID, and password. |
| Step 5 | Specify the directory where the application data must be exported. Use a different directory from the Export Data Directory used for platform data. |
| Step 6 | Enter the hostname and IP address of the destination VM. These values can differ from the source VM hostname and IP address. |
| Step 7 | When prompted, enter yes to proceed with the data export. The data export begins. |
| Step 8 | To check the data export status, run the following command: utils component datamigration status Verify that the output reports that the last component data export operation was successful. |

| Step 1 | Create a Virtual Machine using the OVA Template. Mount the UCSInstall_CLOUDCONNECT_15.0.1.10200-97 bootable image to the Virtual Machine (VM) and power on the VM. For more information, see the following sections in this
                                                   guide: Upload OVA to Nutanix Upload Images to Nutanix Create a Virtual Machine from the OVA on Nutanix |
|---|---|
| Step 2 | Click OK after the media check succeeds. |
| Step 3 | Choose the applicable VOS component and click OK . |
| Step 4 | Click Yes to proceed with installation of the 15.0(1) SU2 build version. |
| Step 5 | Click Import in the Platform Installation Wizard. |
| Step 6 | After reading the displayed information, click OK in the Import Upgrade Configuration information. |
| Step 7 | Choose the appropriate time zone and then click OK . |
| Step 8 | Click Continue in the Auto Negotiation Configuration . |
| Step 9 | Click No to have the default value in MTU Configuration . |
| Step 10 | Click No under DHCP Configuration . |
| Step 11 | Enter the destination hostname and IP address specified during the platform data export. Enter the IP mask and gateway address,
                                             and click OK . The destination values can be different from those of the source VM. |
| Step 12 | Click Yes under the DNS Client Configuration . |
| Step 13 | Provide the Primary DNS server's IP Address and Domain and then click OK . |
| Step 14 | Provide the SFTP server IP address, login ID, and password. For the directory, specify the cluster directory containing the
                                             exported platform data. Use the following format: <Export-Data-Directory>/cluster-<source-publisher-IP-address> For example: /cloudconnect-export/cluster-10.10.10.20 Use this cluster directory when installing both the destination publisher and subscriber. |
| Step 15 | Enter the organization information on the Certificate Information page, and click OK . Note During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                               and IP address as the source: Same hostname and IP address: All source certificates are migrated, including: Tomcat RSA and ECDSA certificates Tomcat trust certificates IPsec and IPsec trust certificates CA-signed certificates, including root and intermediate CA certificates Component certificates uploaded to the Tomcat trust store Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x. Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                                     source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname. The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                                     issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management . Verify the certificates on the destination node to ensure that all required trust relationships are established. | Note | During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                               and IP address as the source: Same hostname and IP address: All source certificates are migrated, including: Tomcat RSA and ECDSA certificates Tomcat trust certificates IPsec and IPsec trust certificates CA-signed certificates, including root and intermediate CA certificates Component certificates uploaded to the Tomcat trust store Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x. Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                                     source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname. The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                                     issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management . Verify the certificates on the destination node to ensure that all required trust relationships are established. |
| Note | During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                               and IP address as the source: Same hostname and IP address: All source certificates are migrated, including: Tomcat RSA and ECDSA certificates Tomcat trust certificates IPsec and IPsec trust certificates CA-signed certificates, including root and intermediate CA certificates Component certificates uploaded to the Tomcat trust store Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x. Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                                     source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname. The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                                     issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management . Verify the certificates on the destination node to ensure that all required trust relationships are established. |
| Step 16 | In the First Node Configuration screen, specify whether you are configuring the first node based on the following: If you are installing a primary node, then click Yes under the First Node Configuration. If you are installing a secondary node, then click No and provide the hostname and IP address of the destination publisher. A warning message states that you must configure the first node before continuing. If the first node is already configured,
                                                         click OK . On the Network Connectivity Test Configuration page, select No to proceed with the installation after connectivity is verified. Provide the Primary host name and IP Address in the First Node Access Configuration page and click OK . |
| Step 17 | For a standalone node such as Cisco VVB, skip this step. Configure the Network Time Protocol (NTP) server and then click Proceed . |
| Step 18 | On the SMTP Host Configuration screen, choose one of the following: To configure an SMTP host during installation, click Yes and enter the SMTP host information. To continue without configuring an SMTP host, click No . |
| Step 19 | On the Platform Configuration Confirmation page, click OK . |

| Note | During a fresh installation with data import, certificate migration depends on whether the destination uses the same hostname
                                                               and IP address as the source: Same hostname and IP address: All source certificates are migrated, including: Tomcat RSA and ECDSA certificates Tomcat trust certificates IPsec and IPsec trust certificates CA-signed certificates, including root and intermediate CA certificates Component certificates uploaded to the Tomcat trust store Unified Intelligence Center JMS and server certificates ( intelligencecenter-jms , intelligencecenter-jms-trust , intelligencecenter-srvr , and intelligencecenter-srvr-trust ) are not migrated because these services are not present in Release 15.x. Different hostname or IP address: Only certificates in the Tomcat trust store, including component certificates uploaded for trust, are migrated. No other
                                                                     source certificates are migrated. The destination generates a new self-signed RSA certificate based on the new hostname. The migrated Tomcat trust store can contain obsolete source-node certificates. These certificates do not cause functional
                                                                     issues. You can remove them from Cisco Unified OS Administration by choosing Security > Certificate Management . Verify the certificates on the destination node to ensure that all required trust relationships are established. |
|---|---|

| Step 1 | Log in to the CLI of the destination Cloud Connect publisher using administrator credentials. |
|---|---|
| Step 2 | Verify that all required Cloud Connect services are running by using the following command: utils service list Note Service status varies by deployment. A service that displays STOPPED—Service Not Activated is not enabled on that node and does not prevent migration. Before proceeding, investigate any required service that displays STOPPED . | Note | Service status varies by deployment. A service that displays STOPPED—Service Not Activated is not enabled on that node and does not prevent migration. Before proceeding, investigate any required service that displays STOPPED . |
| Note | Service status varies by deployment. A service that displays STOPPED—Service Not Activated is not enabled on that node and does not prevent migration. Before proceeding, investigate any required service that displays STOPPED . |
| Step 3 | On the publisher and subscriber, run the following command to obtain the container names: utils cloudconnect list Compare the output of utils cloudconnect list with the containers listed for your source release. If a required container does not display the status Up , do not begin the migration. To start a stopped container, run: utils cloudconnect start <container-name> Run utils cloudconnect list again. If a required container is missing or does not start, resolve the issue before proceeding with the migration. |
| Step 4 | On the publisher only, run the following command to reset all containers: utils cloudconnect reinit services |
| Step 5 | Stop all containers on the publisher and subscriber by running the following command: utils cloudconnect stop <container-name> |
| Step 6 | On the publisher only, run the following CLI command to initiate the import: utils component dataimport initiate |
| Step 7 | Enter the remote server's IP address, login ID, and password. |
| Step 8 | For Data Directory and Data filename , enter the path and name of the directory to which the data was exported (tar file). |
| Step 9 | When prompted, enter yes to proceed with the data import. The data import begins. |
| Step 10 | To verify completion, run the following CLI command: utils component datamigration status |
| Step 11 | Restart the destination Cloud Connect publisher and subscriber nodes by running the following command: utils system restart Run the command on both the publisher and subscriber. Restarting each node automatically restarts its containers. |
| Step 12 | After both nodes restart, validate that the required containers are running on the publisher and subscriber: utils cloudconnect list Verify that the required containers display the status Up . For the expected containers, see Before you Begin . |

| Note | Service status varies by deployment. A service that displays STOPPED—Service Not Activated is not enabled on that node and does not prevent migration. Before proceeding, investigate any required service that displays STOPPED . |
|---|---|

| Note | FEDRAMP Keys Exclusion : FEDRAMP keys are excluded from the migration process and are not transferred during export or import. Re-import Behavior : The re-import operation is not incremental. It resets the destination Cloud Connect environment to the base installation
                                                      state before importing data from the source VM. Import Failure Handling : In the event of an import failure, the destination VM will automatically revert to the base fresh installation state, retaining
                                                      only the platform-imported data. |
|---|---|

| Note | HTTP Proxy settings must be reconfigured during onboarding. |
|---|---|

| Note | Certificate Management must be performed every time Cloud Connect data is migrated. |
|---|---|

| Sequence | Configuration |
|---|---|
| 1 | Configure API Key / Identity Token To establish a connection with Artifactory, you must reconfigure the API Key or Identity Token on the Cloud Connect Publisher
                                                VM using the CLI command utils image-repository set . For more information, see CLI to Configure Artifactory URL and Artifactory Authentication Credentials in the CCE Orchestration chapter. |
| 2 | Onboard CCE Solution Components to Cloud Connect Onboarding all the CCE solution components to Cloud Connect is required to enable Orchestration. For more information, see the following topics in the CCE Orchestration chapter: Onboard VOS Nodes to Orchestration Control Node Onboard Windows Nodes to Orchestration Control Node |
| 3 | Initiate Software Download on Both Cloud Connect Components Run the CLI command utils initiate software-download on both Publisher and Subscriber Cloud Connect components to download software from Artifactory. Note Periodic software download is automatically scheduled every day at 2 AM or at the time configured by the administrator. For more information, see Enforce Software Download from Cisco-Hosted Software Artifactory in the CCE Orchestration chapter. | Note | Periodic software download is automatically scheduled every day at 2 AM or at the time configured by the administrator. |
| Note | Periodic software download is automatically scheduled every day at 2 AM or at the time configured by the administrator. |
| 4 | SMTP Password If SMTP authentication is enabled, you must set up the SMTP password after migration, as sensitive data such as passwords
                                                are excluded during Cloud Connect data migration. Run the CLI command set smtp-pswd to set the password for the SMTP server connection. For more information, see Set Up Email Notification in the CCE Orchestration chapter. |
| 5 | Enable Auto-Rotate of Identity Token If auto-rotate of the Identity Token was enabled on the source Cloud Connect, you must explicitly re-enable it after migration. For more information, see Configure Identity Token Auto Rotation in the CCE Orchestration chapter. |
| 6 | Reconfigure Software Download Time and Cron Job Schedules If you customized any Orchestration job schedules prior to migration, you must reconfigure them using the Orchestration Scheduled
                                                Job CLI after the migration is complete. Migration Requirements Releases earlier than 15.0(1) SU1 : If you previously customized the Software Download schedule, you must reconfigure it using the Orchestration Scheduled Job
                                                CLI. Releases 15.0(1) SU1 or later : If you customized any Orchestration job schedules, you must reconfigure them using the Orchestration Scheduled Job CLI. Starting with release 15.0(1) SU1 , the CLI supports scheduling for the following jobs: Software Download from Cisco Artifactory Deployment Cache Update Software Update Email Notification Auto-rotate Cisco Artifactory Token For detailed instructions, see CLI to Configure Orchestration Scheduled Jobs in the CCE Orchestration chapter. |

| Note | Periodic software download is automatically scheduled every day at 2 AM or at the time configured by the administrator. |
|---|---|

| Sequence | Configuration |
|---|---|
| 1 | Onboard CCE Solution Components to Cloud Connect Onboarding all the CCE solution components to Cloud Connect is required to enable AppDynamics features. For more information, see the following topics in the CCE Orchestration chapter: Onboard VOS Nodes to Orchestration Control Node Onboard Windows Nodes to Orchestration Control Node |
| 2 | Import and Update AppDynamics Agents Importing the AppDynamics Agents into Cloud Connect is required. This includes the Machine Agent, Java Agent, .NET Agent,
                                                and DotNetAgentExtensionManager for Windows, and the Machine Agent and Java Agent for VOS components. After the agents are
                                                imported, you must update the AppDynamics Agents on the respective Windows and VOS components. For more information, see the Import AppDynamics Agents and Update AppDynamics Agents sections in the CCE Serviceability and
                                                Monitoring using AppDynamics chapter of the Serviceability Guide for Cisco Unified Contact Center Enterprise . |
| 3 | Enable AppDynamics Performance Monitoring Note Ensure that you disable AppDynamics performance monitoring on the Cloud Connect source for both VOS-based and Windows-based
                                                            components before enabling it on the destination. You need to enable performance monitoring for both VOS and Windows components and provide the following fields during the
                                                process: Account Access Key Beacon Access Key Password For more information, see the Enable Performance Monitoring section in the CCE Serviceability and Monitoring using AppDynamics
                                                chapter of the Serviceability Guide for Cisco Unified Contact Center Enterprise . | Note | Ensure that you disable AppDynamics performance monitoring on the Cloud Connect source for both VOS-based and Windows-based
                                                            components before enabling it on the destination. |
| Note | Ensure that you disable AppDynamics performance monitoring on the Cloud Connect source for both VOS-based and Windows-based
                                                            components before enabling it on the destination. |

| Note | Ensure that you disable AppDynamics performance monitoring on the Cloud Connect source for both VOS-based and Windows-based
                                                            components before enabling it on the destination. |
|---|---|

| Sequence | Steps Involved |
|---|---|
| 1 | Before you Begin |
| 2 | Export Platform Data from the Source VM to the Remote Server |
| 3 | Export Cisco VVB Data from the Source VM to the Remote Server |
| 4 | Upload OVA on Nutanix |
| 5 | Create a Virtual Machine from the OVA on Nutanix |
| 6 | Shutdown the Source VM(s) |
| 7 | Fresh Install VM with Import option on Nutanix Using Exported Platform Data |
| 8 | Import Cisco VVB Data from the Remote Server to the Destination VM |
| 9 | Post-Migration Configuration for Cisco VVB |

| Step 1 | Log in to the Cisco VVB CLI using administrator credentials. |
|---|---|
| Step 2 | Initiate the export by running the following CLI command: utils component dataexport initiate When prompted for the export directory, enter an absolute path that begins with a forward slash (/). |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the absolute path of the directory to which the data must be exported. The path must begin with a forward slash (/). |
| Step 5 | Enter the IP address and hostname of the destination VM. |
| Step 6 | When prompted, enter "yes" to proceed with the export. The data export begins. Monitor the data export progress in the log
                                                using the following command: file tail activelog platform/log/component_dataexport_<YYYYMMDD>_<HHMMSS>.log Replace <YYYYMMDD>_<HHMMSS> with the timestamp in the log-file name generated for your export operation. |
| Step 7 | To check the data export status, run the following command: utils component datamigration status Verify that the output reports that the last component data export operation was successful. The component data export is complete. |

| Note | Platform data migration must be completed before migrating component data, as Cisco VVB depends on the successful migration
                                                   of platform data, especially certificates. Before you begin the component import, run the following command on the destination
                                                   VM: utils service list Verify that all required platform services show the status STARTED . |
|---|---|

| Step 1 | Log in to the destination Cisco VVB CLI using administrator credentials. |
|---|---|
| Step 2 | Run the following command to initiate the import: utils component dataimport initiate |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the name of the directory to which the data was exported. |
| Step 5 | When prompted, enter Yes to proceed with the import. The data import begins. To monitor data import progress in the log, run the following CLI command: file tail activelog platform/log/component_dataimport_<YYYYMMDD>_<HHMMSS>.log Replace <YYYYMMDD>_<HHMMSS> with the timestamp in the log-file name generated for your import operation. Note The import process takes 15 to 30 minutes. During this time, you must avoid closing the platform CLI window or making configuration
                                                         changes. Cisco VVB services are restarted as part of this process, so no separate reboot is needed once the import process
                                                         is completed successfully. | Note | The import process takes 15 to 30 minutes. During this time, you must avoid closing the platform CLI window or making configuration
                                                         changes. Cisco VVB services are restarted as part of this process, so no separate reboot is needed once the import process
                                                         is completed successfully. |
| Note | The import process takes 15 to 30 minutes. During this time, you must avoid closing the platform CLI window or making configuration
                                                         changes. Cisco VVB services are restarted as part of this process, so no separate reboot is needed once the import process
                                                         is completed successfully. |
| Step 6 | To check the component data import status, run the following command: utils component datamigration status Verify that the output shows Last component dataimport operation was SUCCESS at <timestamp> . After the import succeeds, complete the applicable tasks in Post-Migration Configuration for Cisco VVB and verify Cisco VVB call flows and AppAdmin access. |

| Note | The import process takes 15 to 30 minutes. During this time, you must avoid closing the platform CLI window or making configuration
                                                         changes. Cisco VVB services are restarted as part of this process, so no separate reboot is needed once the import process
                                                         is completed successfully. |
|---|---|

| Note | FEDRAMP Keys Exclusion: FEDRAMP keys are excluded from the migration process and are not transferred during export or import. Re-import Behavior : The re-import operation is not incremental. It resets the destination Cisco VVB environment to the base installation state
                                                      before importing data from the source VM. Import Failure Handling : In the event of an import failure, the destination VM will automatically revert to the base fresh installation state, retaining
                                                      only the platform-imported data. |
|---|---|

| Sequence | Tasks |
|---|---|
| 1 | Before you Begin |
| 2 | Export Platform Data from the Source VM to the Remote Server |
| 3 | Upload OVA on Nutanix |
| 4 | Create a Virtual Machine from the OVA on Nutanix |
| 5 | Export Finesse Data from the Source Publisher VM to the Remote Server |
| 6 | Export Finesse Data from the Source Subscriber VM to the Remote Server |
| 7 | Shutdown the Source VM(s) |
| 8 | Fresh Install VM with Import option on Nutanix Using Exported Platform Data |
| 9 | Import Finesse Data from Remote Server to the Destination VM (Publisher) |
| 10 | Import Finesse Data from Remote Server to the Destination VM (Subscriber) |
| 11 | Post-Migration Configuration of Finesse |

| Step 1 | Log in to the Finesse CLI using administrator credentials. |
|---|---|
| Step 2 | To initiate the export, run the following command: utils component dataexport initiate When prompted for the export directory, enter an absolute path that begins with a forward slash (/). |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the name and path for the directory to which data must be exported. |
| Step 5 | Enter the IP address and hostname of the destination VM. |
| Step 6 | Enter yes when prompted to proceed with the export. The data export begins. Monitor its progress in the log. |
| Step 7 | To check the data export status, run the following command: utils component datamigration status |

| Step 1 | Log in to the Finesse CLI using administrator credentials . |
|---|---|
| Step 2 | To initiate the import, run the following command: utils component dataimport initiate |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the name and path for the directory to which data must be imported. |
| Step 5 | Confirm the data import by entering "yes" when prompted. The data import begins. Monitor its progress in the log. |
| Step 6 | To check the component data import status, run the following command: utils component datamigration status |

| Step 1 | The database is not exported from the Finesse Subscriber so you must perform the database replication by running the following
                                             CLI command on the Primary VM (Publisher) to force database synchronization to the subscriber: utils dbreplication forcedatasyncsub <subscriber-node-name> |
|---|---|
| Step 2 | The database replication status must indicate that all tables are in sync. Check the database replication status on all the Finesse cluster components to ensure that all servers are replicating database
                                                changes successfully. |
| Step 3 | On the Finesse Primary (Publisher) VM, run the following CLI command: utils dbreplication runtimestate Note All components should display a Replicate_State value of 2, which indicates a healthy replication state. If replication issues persist, contact Cisco Technical Support for
                                                         help. | Note | All components should display a Replicate_State value of 2, which indicates a healthy replication state. If replication issues persist, contact Cisco Technical Support for
                                                         help. |
| Note | All components should display a Replicate_State value of 2, which indicates a healthy replication state. If replication issues persist, contact Cisco Technical Support for
                                                         help. |

| Note | All components should display a Replicate_State value of 2, which indicates a healthy replication state. If replication issues persist, contact Cisco Technical Support for
                                                         help. |
|---|---|

| Note | This migration sequence applies only to a standalone Cisco IdS deployment. In a co-resident deployment, Cisco IdS is packaged
                                             with Unified Intelligence Center and Live Data. Migrate the packaged VM by following Unified Intelligence Center - Migration from VMware to Nutanix . Configuration performed on the Unified Intelligence Center co-resident VM also applies to the co-resident Live Data and
                                             Cisco IdS components. Do not perform the standalone Cisco IdS sequence for a co-resident deployment. |
|---|---|

| Sequence | Tasks |
|---|---|
| 1 | Before you Begin |
| 2 | Export Platform Data from the Source VM to the Remote Server |
| 3 | Upload OVA on Nutanix |
| 4 | Create a Virtual Machine from the OVA on Nutanix |
| 5 | Export Cisco IdS Data from the Source Publisher VM to the Remote Server |
| 6 | Export Cisco IdS Data from the Source Subscriber VM to the Remote Server |
| 7 | Shutdown the Source VM(s) |
| 8 | Fresh Install VM with Import option on Nutanix Using Exported Platform Data |
| 9 | Import Cisco IdS Data from Remote Server to the Destination VM (Publisher) |
| 10 | Import Cisco IdS Data from Remote Server to the Destination VM (Subscriber) |
| 11 | Post-Migration Configuration of Cisco IdS |

| Note | This topic applies only to a standalone Cisco IdS deployment. For a co-resident deployment, migrate Cisco IdS as part of the
                                                packaged Unified Intelligence Center, Live Data, and Cisco IdS VM. |
|---|---|

| Step 1 | Log in to the Cisco IdS CLI using administrator credentials. |
|---|---|
| Step 2 | To initiate the export, run the following command: utils component dataexport initiate When prompted for the export directory, enter an absolute path that begins with a forward slash (/). |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the name and path for the directory to which data must be exported. |
| Step 5 | Enter the IP address and hostname of the destination VM. |
| Step 6 | Enter yes when prompted to proceed with the export. The data export begins. Monitor its progress in the log. |
| Step 7 | To check the data export status, run the following command: utils component datamigration status |

| Step 1 | Log in to the Cisco IdS CLI using administrator credentials . |
|---|---|
| Step 2 | To initiate the import, run the following command: utils component dataimport initiate |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the name and path for the directory to which data must be imported. |
| Step 5 | Confirm the data import by entering "yes" when prompted. The data import begins. Monitor its progress in the log. |
| Step 6 | To check the component data import status, run the following command: utils component datamigration status |

| Note | Cisco IdS supports SAML self-signed certificates for authorization and authentication. |
|---|---|

| Note | In a 2000-agent deployment, Unified Intelligence Center, Live Data, and Cisco IdS are co-resident. The component data export and import in this sequence migrate all three components together. Do not run the standalone Live Data or standalone
                                             Cisco IdS export and import procedures for a co-resident deployment. After migration, complete the post-migration configuration
                                             for both Unified Intelligence Center and Live Data. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Before you Begin |
| 2 | Export Platform Data from the Source VM to the Remote Server |
| 3 | Upload OVA on Nutanix |
| 4 | Create a Virtual Machine from the OVA on Nutanix |
| 5 | Export Unified Intelligence Center Data from the Source Publisher VM to the Remote Server |
| 6 | Export Unified Intelligence Center Data from the Source Subscriber VM to the Remote Server |
| 7 | Shut Down the Source VM(s) |
| 8 | Fresh Install the Publisher VM on Nutanix Using Exported Platform Data |
| 9 | Import Unified Intelligence Center Data from the Remote Server to the Destination VM (Publisher) |
| 10 | Fresh Install the Subscriber VM on Nutanix Using Exported Platform Data |
| 11 | Import Unified Intelligence Center Data from the Remote Server to the Destination VM (Subscriber) |
| 12 | Post-Migration Configuration for Unified Intelligence Center |

| Note | The data export from the Unified Intelligence Center publisher VM may take time depending on the size of the Unified Intelligence
                                                Center database. |
|---|---|

| Note | Data migration depends on the deployment model: 2000-agent deployment: The co-resident VM migrates Unified Intelligence Center, Live Data, and Cisco IdS in a single component data export and import. 4000-agent and larger deployments: Run the component data export and import separately on each standalone component VM. |
|---|---|

| Step 1 | Log in to the Unified Intelligence Center CLI using administrator credentials. |
|---|---|
| Step 2 | To initiate the export, run the following CLI command: utils component dataexport initiate When prompted for the export directory, enter an absolute path that begins with a forward slash (/). |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the path of the directory to which the data should be exported. |
| Step 5 | Enter the hostname and IP address of the destination VM. |
| Step 6 | Enter "yes" when prompted to proceed with the export. The data export begins. Monitor its progress in the log by running the
                                                file tail command available on the CLI interface. |
| Step 7 | To check the data export status, run the following command: utils component datamigration status |

| Step 1 | Log in to the Unified Intelligence Center CLI using administrator credentials. |
|---|---|
| Step 2 | Run the following CLI command to initiate the export: utils component dataexport initiate When prompted for the export directory, enter an absolute path that begins with a forward slash (/). |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the path of the directory to which the data should be exported. |
| Step 5 | Enter the hostname and IP address of the destination VM. |
| Step 6 | Enter "yes" when prompted to proceed with the export. The data export begins . |
| Step 7 | Monitor the data export progress in the log by running the file tail command available on the CLI interface. |
| Step 8 | To check the data export status, run the following command: utils component datamigration status |

| Step 1 | Log in to the Unified Intelligence Center publisher CLI using administrator credentials. |
|---|---|
| Step 2 | Run the following CLI command to initiate the import: utils component dataimport initiate |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | For the Data Directory, specify name and path. |
| Step 5 | Confirm the data import by entering "yes" when prompted. The data import begins. Monitor the data import progress in the log
                                                by running the file tail command available on the CLI interface. |
| Step 6 | To check the component data import status, run the following command: utils component datamigration status |

| Step 1 | Log in to the Unified Intelligence Center subscriber CLI using administrator credentials. |
|---|---|
| Step 2 | Run the following CLI command to initiate the import: utils component dataimport initiate |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | For the Data Directory, specify name and path. |
| Step 5 | Confirm the data import by entering "yes" when prompted. The data import begins. Monitor the data import progress in the log
                                             by running the file tail command available on the CLI interface. |
| Step 6 | To check the component data import status, run the following command: utils component datamigration status |
| Step 7 | When importing data to the Publisher, Subscriber nodes are not yet available; therefore, configuration data is not synchronized
                                             at that stage. |

| Note | After the initial component data import and database synchronization, restart all Unified Intelligence Center nodes. This also restarts the co-resident Cisco
                                                IdS components. After subsequent imports on the publisher, restart only the subscriber nodes. |
|---|---|

| Step 1 | Data Source Configuration During Unified Intelligence Center data migration, all data source details-including database hostname, username, and password
                                                are migrated seamlessly. If the details for the data sources such as hostnames and credentials are unchanged, reconfiguration
                                                is not needed. However, if any data source details are modified on the target system, reconfiguration will be required. 
                                                
                                                For more information, see the Data Source Actions section in the Configure chapter of Cisco Unified Intelligence Center Report Customization Guide. Data Source Hostname to IP mapping Unified Intelligence Center can be configured to connect to different AWDB or HDS servers to distribute reporting load. The
                                                Unified Intelligence Center-to-AWDB mapping is migrated during the data migration process. If AWDB or HDS details are changed
                                                on destination, you must reconfigure the host-to-IP mapping on all Unified Intelligence Center nodes using the following CLI
                                                command: 
                                                
                                                set cuic properties host-to-ip 
                                                
                                                For more information, see the set cuic properties host-to-ip section in the Command Line Interface chapter in Administration Console User Guide for Cisco Unified Intelligence Center. |
|---|---|
| Step 2 | Active Directory Configuration Active Directory configuration in OAMP is fully migrated, eliminating the need for any post-migration reconfiguration. 
                                                
                                                For more information, see Configure Active Directory section in Cluster Configuration Chapter of Administration Console User Guide for Cisco Unified Intelligence Center. |
| Step 3 | SMTP Configuration SMTP details-including username, password, and hostname-are migrated automatically. No further changes are required if the
                                                target system uses the same SMTP server. For more information, see Configure SMTP Settings section in Cluster Configuration Chapter of Administration Console User Guide for Cisco Unified Intelligence Center. |
| Step 4 | Cross-Origin Resource Sharing (CORS) Configuration Unified Intelligence Center CORS configuration stores the hostnames of Finesse servers hosting the Unified Intelligence Center
                                                gadget. These hostname details are migrated during the Unified Intelligence Center data migration process. If the Finesse hostnames remain the same between source and target, no reconfiguration is necessary. If the Finesse hostnames differ, run the following CORS CLI command to update the configuration: utils cuic cors allowed_origin add utils live-data cors allowed_origin list For more details, see the utils cuic cors section of Command Line Interface chapter in Administration Console User Guide for Cisco Unified Intelligence Center. |
| Step 5 | Certificate Exchange (Perform this step only if self-signed certificates are in use.) All certificates are migrated to the target systems during data migration. Unified Intelligence Center stores certificates
                                                for Live Data, Cisco IdS, and Finesse in the platform trust store. If the hostnames for Live Data, Cisco IdS, or Finesse change, the corresponding certificates must be imported into Unified
                                                Intelligence Center using Cisco Unified OS Administration. For more information about Self-Signed Certificates, see the Post Installation section in Installation chapter of Installation and Upgrade Guide for Cisco Unified Intelligence Center. |
| Step 6 | Unified Intelligence Center Gadgets in Finesse Gadget URLs in Finesse Administration Console must be updated to reference the new Unified Intelligence Center FQDN. For more information, see the Gadgets and Components section in the Manage Desktop Layout chapter of Cisco Finesse Administration Guide . |

| Note | In a 2000-agent deployment, Live Data is co-resident with Unified Intelligence Center and Cisco IdS. Migrate the co-resident
                                             VM by following Unified Intelligence Center - Migration from VMware to Nutanix . Configuration performed on the Unified Intelligence Center co-resident VM also applies to the co-resident Live Data and
                                             Cisco IdS components. Do not repeat the Live Data export and import procedures. After migrating the co-resident VM, complete Post-Migration Configuration for Live Data . |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Before you Begin |
| 2 | Export Platform Data from the Source VM to the Remote Server |
| 3 | Upload OVA on Nutanix |
| 4 | Create a Virtual Machine from the OVA on Nutanix |
| 5 | Export Live Data from the Source Publisher VM to the Remote Server |
| 6 | Export Live Data from the Source Subscriber VM to the Remote Server |
| 7 | Shut Down the Source VM(s) |
| 8 | Fresh Install the Publisher VM on Nutanix Using Exported Platform Data |
| 9 | Import Live Data from the Remote Server to the Destination VM (Publisher) |
| 10 | Fresh Install the Subscriber VM on Nutanix Using Exported Platform Data |
| 11 | Import Live Data from the Remote Server to the Destination VM (Subscriber) |
| 12 | Post-Migration Configuration for Live Data |

| Note | Use this workflow only for a standalone Live Data deployment. For a 2000-agent co-resident deployment, follow the Unified
                                                Intelligence Center migration workflow. |
|---|---|

| Step 1 | Log in to the Live Data publisher CLI using administrator credentials. |
|---|---|
| Step 2 | To initiate the export, run the following CLI command: utils component dataexport initiate When prompted for the export directory, enter an absolute path that begins with a forward slash (/). |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the path of the directory to which the data should be exported. |
| Step 5 | Enter the hostname and IP address of the destination VM. |
| Step 6 | Enter "yes" when prompted to proceed with the export. The data export begins. Monitor its progress in the log by running the
                                                file tail command available on the CLI interface. |
| Step 7 | To check the data export status, run the following command: utils component datamigration status |

| Step 1 | Log in to the Live Data subscriber CLI using administrator credentials. |
|---|---|
| Step 2 | Run the following CLI command to initiate the export: utils component dataexport initiate When prompted for the export directory, enter an absolute path that begins with a forward slash (/). |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | Enter the path of the directory to which the data should be exported. |
| Step 5 | Enter the hostname and IP address of the destination VM. |
| Step 6 | Enter "yes" when prompted to proceed with the export. The data export begins . |
| Step 7 | Monitor the data export progress in the log by running the file tail command available on the CLI interface. |
| Step 8 | To check the data export status, run the following command: utils component datamigration status |

| Step 1 | Log in to the Live Data publisher CLI using administrator credentials. |
|---|---|
| Step 2 | Run the following CLI command to initiate the import: utils component dataimport initiate |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | For the Data Directory, specify the directory name and path. |
| Step 5 | Confirm the data import by entering "yes" when prompted. The data import begins. Monitor its progress in the log by running
                                             the file tail command available on the CLI interface. |
| Step 6 | To check the component data import status, run the following command: utils component datamigration status |

| Step 1 | Log in to the Live Data subscriber CLI using administrator credentials. |
|---|---|
| Step 2 | Run the following CLI command to initiate the import: utils component dataimport initiate |
| Step 3 | Enter the remote server's IP address, login ID, and password. |
| Step 4 | For the Data Directory, specify the directory name and path. |
| Step 5 | Confirm the data import by entering "yes" when prompted. The data import begins. Monitor its progress in the log by running
                                             the file tail command available on the CLI interface. |
| Step 6 | To check the component data import status, run the following command: utils component datamigration status |

| Note | After the initial component data import, restart all Live Data nodes. After subsequent imports on the publisher, restart only the subscriber nodes. |
|---|---|

| Step 1 | Inventory addition (Only for 2000 deployment models) Live Data configuration is managed through CCE inventory management. You must reconfigure the inventory by deleting the old
                                                entries for the Unified Intelligence Center-LD-Cisco IdS publisher nodes (which also deletes the subscriber) and adding new
                                                Unified Intelligence Center-LD-Cisco IdS publisher and subscriber nodes. For more information, see the Configure Live Data with AW topic. For more information, see the Migrate from Co-Resident Deployment to Standalone Deployment topic. |
|---|---|
| Step 2 | AWDB Access configuration After Live Data migration, run the following CLI command: set live-data aw-access |
| Step 3 | Machine Service Configuration (4000 and above deployment models only) The Machine Services CLI stores Live Data information. After Live Data migration, run the following command: set live-data machine-services |
| Step 4 | CORS Configuration Live Data CORS configuration saves the hostnames where Finesse is hosted. These values are migrated during Live Data migration.
                                                If the Finesse hostnames remain the same on both source and target systems, no reconfiguration is required. If the Finesse hostnames differ between source and target, reconfiguration is necessary. Run the following CORS command: utils live-data cors allowed_origin add |
| Step 5 | Data source Details in Unified Intelligence Center Store Live Data source details in Unified Intelligence Center to enable live data reporting. If Live Data hostnames change,
                                                update the data source details in Unified Intelligence Center by running the following CLI command on the Live Data server: set live-data cuic-datasource |
| Step 6 | Certificate Exchange (Perform this step only if self-signed certificates are in use.) All certificates are migrated to the target systems during Live Data migration. Live Data stores the certificates for the Unified Intelligence Center and the AWDB in the platform trust store. If the hostnames
                                                for the Unified Intelligence Center or AWDB change, import their certificates into Live Data using Cisco Unified OS Administration. For more information about Self-Signed Certificates, see the Post Installation section in the Installation chapter of Installation and Upgrade Guide for Cisco Unified Intelligence Center. |

| Note | Nutanix Move operations require the appliances to be shut down on the source hypervisor , which results in service disruption. Schedule these activities during a planned maintenance window. |
|---|---|

| Note | Nutanix Move uses VMware snapshots and Changed Block Tracking (CBT) to perform incremental data synchronization. Nutanix Move takes its own snapshots, labeled "Move-Snap-", to track data changes during the migration . After cutover, Nutanix Move removes these temporary snapshots as part of its cleanup process. If another backup application takes or deletes snapshots while a Nutanix Move operation is in progress , the migration may fail. Before Nutanix Move starts migration, current snapshots for that VM are automatically removed. |
|---|---|

| Step 1 | Download the Nutanix Move QCOW2 file for AHV from the Nutanix Support Portal . |
|---|---|
| Step 2 | Upload the image to the Nutanix image service in Prism Element or Prism Central. |

| Step 1 | Log in to Prism Central for your AHV cluster. |
|---|---|
| Step 2 | Go to VM > Create VM . |
| Step 3 | Select the Nutanix Move QCOW2 image as a disk. For Disk Operation , choose Clone from Image Service . Add the required CPU and memory, for example 2 vCPUs and 8 GB RAM. |
| Step 4 | Add a network interface card (NIC) for the management network. |
| Step 5 | Power on the VM. For more information, see the Nutanix documentation at Deploying Nutanix Move on AHV . |

| Step 1 | Launch the Nutanix Move VM console from Prism Central or Prism Element . |
|---|---|
| Step 2 | Use the default password nutanix/4u to log in. For more information, see Changing Admin User Password . |
| Step 3 | Run the following command: passwd |
| Step 4 | Enter and reenter the new password when prompted. |
| Step 5 | Verify that the following confirmation appears: passwd: all authentication tokens updated successfully |

| Step 1 | Log in to the Prism Element UI of the cluster where the Nutanix Move VM is deployed using the admin user credentials. |
|---|---|
| Step 2 | Go to Entity > Virtual Infrastructure > VMs . |
| Step 3 | Select the VM named Nutanix-Move . |
| Step 4 | Open a remote console on the Nutanix Move VM and log in with the Nutanix Move admin user credentials. For more information about credential details, see Change the Default Password of Nutanix Move . |
| Step 5 | Run the following command to switch to the root user and enter the password of the Nutanix Move VM. admin@move on ~ $ rs Note The first time that the Nutanix Move CLI is launched , the script runs automatically. | Note | The first time that the Nutanix Move CLI is launched , the script runs automatically. |
| Note | The first time that the Nutanix Move CLI is launched , the script runs automatically. |
| Step 6 | Run the following command to configure the static IP address. root@move on ~ $ configure-static-ip |
| Step 7 | Enter the required IP address and netmask values. |

| Note | The first time that the Nutanix Move CLI is launched , the script runs automatically. |
|---|---|

| Step 1 | In a browser, enter https://<Nutanix-Move-VM-IP>/ . |
|---|---|
| Step 2 | Accept the EULA and set the initial administrator password. |
| Step 3 | Log in to the Nutanix Move dashboard. |

| Step 1 | In the Nutanix Move UI, go to Environments > Add Environment . |
|---|---|
| Step 2 | Choose the environment type. |
| Step 3 | Enter the following environment details: Environment name Environment IP address Administrator user name and password |
| Step 4 | Click Add . Note The user must have administrator-level privileges on both the source and destination environments. For more information, see Adding vCenter Server or Standalone ESXi Host Environment . For more information about adding the target environment, see Adding a Nutanix AOS Cluster Environment . | Note | The user must have administrator-level privileges on both the source and destination environments. |
| Note | The user must have administrator-level privileges on both the source and destination environments. |

| Note | The user must have administrator-level privileges on both the source and destination environments. |
|---|---|

| Step 1 | In the Nutanix Move dashboard, click New Migration Plan . |
|---|---|
| Step 2 | In the Plan Name field, enter a unique name for the migration plan and click Proceed . |
| Step 3 | On the Source & Target screen, configure the source and target environment details. From the Select a Source drop-down list, select the VMware source environment. From the Select a Target drop-down list, select the Nutanix target environment. From the Target Project drop-down list, select the target project, if applicable. From the Target Cluster drop-down list, select the Nutanix target cluster. From the Target Container drop-down list, select the storage container for the migrated VMs. Review the Security Policy section. If no NSX or FNS environment is configured for the selected source or target, no security policy is applied from this screen. Click Next . |
| Step 4 | On the Select VMs screen, add the VMs that you want to migrate. Use the search field or filter options to locate the required VMs. Select the add icon or checkbox for each VM that you want to include in the migration plan. Review the Added VMs pane and verify that all required VMs are listed. Review any warnings that are shown for the selected VMs. Click Next . |
| Step 5 | On the Network and Policy screen, configure the network mapping. For each Source Network , select the corresponding Target Network . If you are creating a test migration, select the required subnet from the Test Network drop-down list. Note The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts. Review the Security Policies section. If no NSX or FNS environment is found for the selected source or target, no security policy is applied from this screen. Click Next . | Note | The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts. |
| Note | The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts. |
| Step 6 | On the VM Preparation screen, configure the VM preparation and guest operation settings. From the Preparation Mode drop-down list, select the preparation mode. If you select Automatic , Nutanix Move prepares the VMs using the credentials that you provide. From the IP Configurations for target VMs drop-down list, select whether to retain the source IP configurations. Select Uninstall VMware tools on target VMs . Note If this option is not selected, migration can fail with a VMware Tools unrecoverable error. Select Install Nutanix Guest Tools (NGT) on target VMs , if required. Select Bypass guest operations on source VMs , if required. In the Credentials for Source VMs section, provide the required credentials. For Windows VMs, provide administrator credentials. For Linux VMs, provide root credentials, or select Use Private (.PEM) file to authenticate if private key authentication is used. Note For Linux VMs, credentials are not required if guest operations are not used. In the Post Migration Automation section, select Configure a Runbook to automate post-migration tasks on VMs , if required. In the Override individual VM Preparation section, click Change settings if you need to change the preparation mode or credentials for individual VMs. Click Next . | Note | If this option is not selected, migration can fail with a VMware Tools unrecoverable error. | Note | For Linux VMs, credentials are not required if guest operations are not used. |
| Note | If this option is not selected, migration can fail with a VMware Tools unrecoverable error. |
| Note | For Linux VMs, credentials are not required if guest operations are not used. |
| Step 7 | On the VM Settings screen, configure migration settings for the VMs. From the VMs Priority drop-down list, select the migration priority. From the Timezone drop-down list, select the timezone. If you select Default , Nutanix Move configures the UTC timezone for Linux VMs and the cluster timezone for Windows VMs. Select Retain MAC addresses from the source VMs , if required. Select Skip CDROM Addition on target VMs , if required. Select Enable Memory Overcommit , if required. In the Category/Tag Settings section, select one of the category or tag options. You can select and apply target categories for all VMs in the migration plan, or assign source tags and categories to the
                                                   target based on mappings. In the VM Migration Type section, select one of the VM property options. You can configure target VM properties, or retain source VM properties. In the Settings for Individual VMs section, click Change settings if you need to configure settings for individual VMs. Select Schedule Data Seeding , if required. Click Next . |
| Step 8 | On the Summary screen, validate the migration plan details. Review the Source Environment Details , including the environment type, name, source IP, and number of VMs to migrate. Review the Target Environment Details , including the target cluster and container. Review the Network Mapping , including the source network and target network. Click Save to save the plan, or click Save and Start to save the plan and start data seeding. |
| Step 9 | Monitor the migration plan until the VM status changes to Ready to Cutover . The migration plan shows the migrated data size, migration status, and estimated cutover time for each VM. |
| Step 10 | Perform the production cutover. Select the VM that is ready for cutover. Click Cutover . Review the confirmation message and click Continue . Note After you continue, the source VMs shut down, the virtual NICs of the source VMs are disconnected, and each source VM is updated
                                                               with a migration note. The operation can take some time to update the VM state in the UI. | Note | After you continue, the source VMs shut down, the virtual NICs of the source VMs are disconnected, and each source VM is updated
                                                               with a migration note. The operation can take some time to update the VM state in the UI. |
| Note | After you continue, the source VMs shut down, the virtual NICs of the source VMs are disconnected, and each source VM is updated
                                                               with a migration note. The operation can take some time to update the VM state in the UI. |
| Step 11 | Validate that the migrated VM is available on Nutanix Prism Element or Prism Central. |

| Note | The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts. |
|---|---|

| Note | If this option is not selected, migration can fail with a VMware Tools unrecoverable error. |
|---|---|

| Note | For Linux VMs, credentials are not required if guest operations are not used. |
|---|---|

| Note | After you continue, the source VMs shut down, the virtual NICs of the source VMs are disconnected, and each source VM is updated
                                                               with a migration note. The operation can take some time to update the VM state in the UI. |
|---|---|

| Step 1 | On the Network and Policy screen, select a test network. From the Test Network drop-down list, select the subnet to use for test migration. Note The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts. Figure 2. Test Network Selection | Note | The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts. |
|---|---|---|---|
| Note | The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts. |
| Step 2 | Complete the remaining migration plan screens and click Save and Start . Use the same source, target, VM preparation, VM settings, and summary validation workflow described in Create a Migration Plan . |
| Step 3 | Monitor the migration plan until the VM status changes to Ready to Cutover . |
| Step 4 | Select the VM for which you want to create a test VM. |
| Step 5 | From the Test Actions menu, select Create Test VM . Nutanix Move creates the test VM on the target Nutanix cluster. Test VM names are suffixed with -MoveTest in the target network. Figure 3. Create Test VM |
| Step 6 | Validate that the test VM is available in Nutanix Prism Element or Prism Central. |
| Step 7 | Perform the required application validation on the test VM. |
| Step 8 | After validation is complete, return to the Nutanix Move dashboard and continue with cutover when you are ready to migrate to the production environment. Note When you proceed with cutover, Nutanix Move removes the test VM that was created on the Nutanix cluster. Figure 4. Test Migration Cutover | Note | When you proceed with cutover, Nutanix Move removes the test VM that was created on the Nutanix cluster. |
| Note | When you proceed with cutover, Nutanix Move removes the test VM that was created on the Nutanix cluster. |

| Note | The test network must be non-routable and isolated from the rest of the network to avoid IP address or MAC address conflicts. |
|---|---|

| Note | When you proceed with cutover, Nutanix Move removes the test VM that was created on the Nutanix cluster. |
|---|---|

| Step 1 | Log in to VMware vCenter and locate the source virtual machine used for migration. |
|---|---|
| Step 2 | Edit the VM settings and update the network adapter. Set the network adapter to Connected . Select Connect At Power On . |
| Step 3 | Power on the virtual machine. |

| Sequence | Troubleshooting |
|---|---|
| 1 | Common Issues for Windows-based CCE Components |
| 2 | Common Issues for VOS-based Components |
| 3 | Cisco VVB |
| 4 | Unified Intelligence Center and Live Data |
| 5 | Finesse |
| 6 | Cisco IdS |
| 7 | Restore the Source VM After Migration Failure (Nutanix Move) |

| Issue | Resolution |
|---|---|
| When a user attempts to revert a VM to a snapshot with UUID <ID>, they may encounter the error "Failed to revert the VM with
                                             UUID <ID>" if Nutanix Guest Tools (NGT) tools are installed on the VM but not present in the snapshot. This issue arises because
                                             the snapshot does not contain the NGT tools required by the VM. | Uninstall the NGT tools from the VM, then revert to the desired snapshot. |
| If the timezone of the deployed Windows CCE VM differs from the default UTC timezone of the hardware clock in AHV, a temporary
                                             flip to the UTC timezone may occur during the restart of the Windows CCE VM. This time difference can be observed in application
                                             logs that capture events before and after the power cycle. | For detailed recommendations on handling timezone settings for Windows VMs deployed in Nutanix AHV environments, see the Nutanix Knowledge Base article . Ensure that NTP is properly configured on the Windows VMs, and apply relevant Microsoft timezone updates as part of regular
                                             maintenance to keep timezone information current. |

| Issue | Resolution |
|---|---|
| SFTP validation error- SSH algorithm negotiation failure During the export and import operation of data migration, if you encounter the SFTP validation error-SSH algorithm negotiation
                                             failed. | Ensure deployed SFTP server is configured with strong cryptographic algorithms. |

| Issues | Resolution |
|---|---|
| Export CLI failure: The export CLI command exited with a failure status. | Ensure that all the services are up and running by using the following CLI command: utils service list Retry the export CLI command. |
| Cisco VVB import fails due to backup issues: Corrupted or incomplete export data can cause import failures. | Redo the export and re-run the following CLI command: utils component dataexport initiate |
| Component import fails when platform data is not imported first: Cisco VVB depends on platform services and certificates. | Complete and verify platform data import is successful before starting component import. |
| Issues arise from network and host configuration conflicts: IP, DNS, and hosts mismatch causes service and UI access failures. | Verify network settings and update the hosts file post-import if needed. |
| Import is interrupted, or configurations change during migration: VM reboot, power loss, or any administrator changes can leave Cisco VVB in an inconsistent state. | Maintain a stable environment and freeze all Cisco VVB configuration changes during export/import. |
| OVA profile or resource mismatches affect Cisco VVB migration Incorrect OVA size or insufficient CPU or RAM leads to unstable services. | Ensure source and destination use the same OVA profile with adequate resources. |

| Issues | Resolution |
|---|---|
| Unified Intelligence Center |
| Data Sources are offline | As part of the Unified Intelligence Center data migration, all data source configurations have been migrated. If configuration details such as IP/hostname, username, or credentials are different on the Nutanix system, modify the data
                                          sources accordingly and validate that the data sources come online. For more information, see the Data Sources section in
                                          the Configure chapter of the Cisco Unified Intelligence Center Report Customization Guide. |
| Scheduled report mails are not working | The SMTP configuration in OAMP is migrated as part of the Unified Intelligence Center data migration upgrade. If the SMTP
                                          server details on the Nutanix system are different, reconfigure them in OAMP. If SMTP over TLS is used, import the new SMTP server TLS certificate from source. For more information, see the Configure
                                          SMTP Settings section in the Cluster Configuration chapter of the Administration Console User Guide for Cisco Unified Intelligence Center. |
| LDAP login does not work | Active Directory settings are migrated as part of the Unified Intelligence Center data upgrade. If a different Active Directory
                                          is used on the Nutanix system, reconfigure the Active Directory settings in OAMP. For more information, see the Configure
                                          Active Directory Settings section in the Cluster Configuration chapter of the Administration Console User Guide for Cisco Unified Intelligence Center . |
| Unified Intelligence Center Historical Gadgets in Finesse desktop does not load | Check the Unified Intelligence Center CORS configuration by running the following CLI command: utils cuic cors allowed_origins list Ensure the correct Finesse hostnames are listed in the URLs. For more information, see the utils cuic cors section in the Command Line Interface chapter of the Administration Console User Guide for Cisco Unified Intelligence Center, Release 15.0(1) . |
| Live Data |
| Live Data Gadgets in Finesse desktop does not load | Check the LD CORS configuration by running the following CLI command: utils live-data cors allowed_origins list For more information, see the Configure Cross Origin Resource Sharing (CORS) for Live Data section in the Installation chapter of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html Ensure that the correct Finesse hostnames are listed in the URLs. Ensure Live Data failover state is either Active or Standby by running the following CLI command: show live-data failover If LD is shown as out-of-service Check Live Data aw-access configuration by running the following CLI command: show live-data aw-access Ensure that the test connection is successful. If Test connection fails, run the following CLI command to re-configure the AWDB details: set live-data aw-access primary set live-data aw-access secondary Only for 4000 and above deployment models To register LD details on AWDB, run the following CLI command: set live-data machine-services To update the Live Data configuration on Unified Intelligence Center, run the following CLI command: set live-data cuic-datasource For more information on the CLI commands, see the CLI commands chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| Live Data reports do not load | Ensure Live Data failover state is either Active or Standby by running the following CLI command: show live-data failover If LD is shown as out-of-service check Live Data aw-access configuration by running the following CLI command: show live-data aw-access Ensure that the test connection is successful. If Test connection fails, run the following CLI command to re-configure the AWDB details: set live-data aw-access primary set live-data aw-access secondary Only on 4000 and above deployment models Run the following CLI command to register LD details on AWDB: set live-data machine-services To update the LD configuration on Unified Intelligence Center, run the set live-data cuic-datasource . For more information on the CLI commands, see the CLI commands chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |

| Issues | Resolution |
|---|---|
| Finesse data sources or the CTI server are offline. | During Finesse data migration, AWDB server configurations are migrated. If configurations such as IP address, hostname, port,
                                             username, or credentials differ on the Nutanix system, update the data sources accordingly. Then, restart the "Finesse Tomcat"
                                             service to confirm that the data sources are online. 
                                             
                                             For more information, see the Contact Center Enterprise CTI Server Settings section in the Manage System Settings chapter
                                             of Cisco Finesse Administration Guide. |
| Database replication failure | On the Publisher node, run the following admin CLI command: utils dbreplication runtimestate If replication is out of sync, follow these steps: Stop database replication on the publisher node by running the following CLI command: utils dbreplication stop all Reset database replication on the publisher node by running the CLI command: utils dbreplication reset all After a few minutes, monitor the rebuild process by running the following CLI command: utils dbreplication runtimestate For more information, see the Replication Status section in the Finesse CLI chapter of Cisco Finesse Administration Guide. |
| The Finesse subscriber node is out of service. | In cfadmin, verify that the secondary Finesse server is configured with the correct hostname. If the Finesse publisher node is in service and database replication is synchronized, but the subscriber node is out of service,
                                             run the following admin CLI command to force synchronization of the database from the publisher to the subscriber node: utils dbreplication forcedatasyncsub |
| A third-party Finesse gadget fails to load. | Log in to cfadmin and verify that there are no errors on the Desktop Layout page and that the gadget is included in the XML
                                             configuration. 
                                             
                                             For more information, see the Gadgets and Components section in the Manage Desktop Layout chapter of Cisco Finesse Administration Guide. Log into 3rdpartygadget Account to verify that the third-party gadgets are configured with required permissions. 
                                             
                                             For more information, see the 3rdpartygadget Account section in Manage Third-Party Gadgets chapter of Cisco Finesse Administration Guide. |
| After logging into the Finesse desktop, the desktop layout, reason codes, phonebook, or workflows are not found. | Log in to Finesse Administrator Console and verify that the desktop layout, reason codes, phonebook, and workflows are available
                                             and have been migrated from the source Finesse VM. Review the Finesse data migration import logs for any errors. Perform the export and import again or manually add the failed configurations. 
                                                   For more information, see the Cisco Finesse Administration Guide. |

| Issues | Resolution |
|---|---|
| Invalid SSO client configuration | As part of the Cisco IdS data migration, all Cisco IdS client data has been migrated. If the IP address, hostname, or port
                                          configuration of the SSO clients differs on the Nutanix system, modify or add those clients accordingly and validate the changes.
                                          
                                          
                                          For more information, see the Hostname or IP Address Change section in the Cisco IdS for Single Sign-On chapter of Cisco Unified Contact Center Enterprise Features Guide . |
| Unknown certificate error | Upload the Cisco IdS Tomcat certificate to the SSO clients' trust store. 
                                          
                                          For more information, see the Certificates for Cisco IdS chapter of Cisco Finesse Administration Guide . |
| Cisco IdS-to-IdP trust failure | It is necessary to regenerate the SAML certificate in Cisco IdS and establish trust between Cisco IdS and the IdP. 
                                          
                                          For more information, see the Configure an Identity Provider section in the Cisco IdS for Single Sign-On chapter of Cisco Unified Contact Center Enterprise Features Guide. |

| Component | Description | Any Impact |
|---|---|---|
| Unified Intelligence Center | Unified Intelligence Center VM exhibits a surge in CPU usage in the Nutanix environment. | No functional impact |
| Finesse | Finesse VM exhibits a surge in CPU usage on the Nutanix environment. | No functional impact |