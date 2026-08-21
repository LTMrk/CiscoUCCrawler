---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-installation-guide-pcce-b-150-c-e5c7d3d85d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/installation/guide/pcce_b_150_cisco_pcce_installationandupgrade_guide/common_ground_upgrade_process.html
retrieved_at: 2026-08-21T12:09:24.581098+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Common Ground Upgrade Process

## Chapter: Common Ground Upgrade Process

# Common Ground Upgrade Process

## Upgrade Path

The supported upgrade paths to Packaged CCE 15.0(1) are as follows:

Supported Upgrade Paths

In-place Upgrade Supported Platforms

(From)

In-place Upgrade Supported Platforms (To)

Windows Server 2016 and SQL Server 2017

Windows Server 2019 and SQL Server 2019

Windows Server 2022 and SQL Server 2022

The Common Ground upgrade from Windows Server 2016 and SQL Server 2017 is only supported if an in-place platform upgrade is
                                          performed to Windows Server 2022 and SQL Server 2022, and not to Windows Server 2019 and SQL Server 2019

Use 15.0(1) EDMT to upgrade to the above-mentioned supported Packaged CCE upgrade paths.

## Prerequisites and Important Considerations

After you begin the migration and upgrade process, you cannot back out of it. If you want to go back to the previous release,
                                 you must restore your VMs from your backup.

You can upgrade to Cisco Packaged CCE 2000, 4000, and 12000 Agent deployments as per the supported upgrade path .

Before you upgrade the Cisco VOS-based servers such as the Live Data server, check the Check and upgrade VMware Tools before each power on box in the VM's Options > Edit Settings .

For more information on VMware Tools upgrade, see the VMware documentation.

Before upgrading, close all the open Microsoft Windows Event Viewer instances. This prevents an installation failure with
                                 an error that the following DLLs are locked:

icrcat.dll

icrmsgs.dll

snmpeventcats.dll

snmpeventmsgs.dll

If the failure occurs, close the Event Viewer and retry the installation. If the failure persists, restart the Microsoft
                                 Windows Event Log service.

This release contains an updated database schema. During the upgrade process, perform a schema upgrade using the Enhanced
                                 Database Migration Tool (EDMT).

For the upgrade utilities, see https://software.cisco.com/download/type.html?mdfid=268439622

Make sure that you have backups of all components in both Side A and Side B before you begin your upgrade. You can take a
                                 snapshot of the virtual machines on which you are performing the upgrade.

After you configure the servers, you can move the VMs to the servers and complete the common ground upgrade.

Optionally, you can stage the Unified CCE Rogger off box before you begin the migration and upgrade to lessen your downtime.

If you already have a Customer Collaboration Platform added in the remote site, delete Customer Collaboration Platform from the remote site and add it as an External Machine in the main site. For more information on how to delete and add an
                                 external machine, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Make sure that you are running the minimum supported version of ESXi. For information about supported ESXi versions, see the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html .

In the Unified CCE Administration console, departments cannot be named Global or Service . If you have already created departments with these names, update the department names before upgrading ECE.

Following the upgrade of Packaged CCE, wait for a few minutes for the system to finish loading before logging in to the Unified
                                 CCE Administration console.

Before you upgrade from an earlier version to Packaged CCE 15.0(1), delete the custom reason code 50045 inorder to avoid conflicts
                                 with system reason code. For more information about the reason codes, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### NTP Configuration
                           	 Requirements

Packaged CCE relies on time synchronization.
                                 		  Properly configuring NTP is critical for reliability of reporting data and
                                 		  cross-component communication. It's important to implement the requirements
                                 		  outlined in NTP and Time Synchronization .

## Upgrade Considerations

### Update VM Properties

Rather than re-create the VMs in the new version of the OVA, you can manually update the VM properties to match the new OVA.
                              Before you upgrade the CCE components, update the properties of each VM to match the appropriate OVA, as follows:

Stop the VM.

Update the properties of each VM to match the properties of the appropriate OVA. Check the Virtualization for Packaged Cisco Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html for descriptions of each OVA. Save your changes.

To update the VM properties of specific components such as Cloud Connect, Cisco Finesse, Unified CVP, and so on, refer to
                                                the respective virtualization guide under the Contact Center section at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

Restart the VM.

Caution

Be careful when you upgrade the virtual machine network adapters. Done incorrectly, this upgrade can compromise the fault
                                          tolerance of your Cisco Contact Center.

### Expand Disk Space of Virtual Machines

Complete the following procedure to expand the virtual machines disk space on Unified CCE  virtual machines:

Power off the VM.

Launch the vSphere Web Client using the browser.

Log in to your vCenter Server.

Ensure that the virtual machine is switched off.

Right-click the Virtual Machine and choose Edit Settings .

Click the Virtual Hardware tab.

Select the Hard Disk where the product is deployed, and change the disk size value (in GB) of the Unified CCE virtual machines, as defined in https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html .

Click OK .

Power on the virtual machine.

Log into your operating system.

Right-click This PC and select Manage .

Select File and Storage Services > Disks .

In the Volumes area, right-click the drive where the product is deployed and select Extend Volume .

Change the disk size value (in GB) of the Unified CCE virtual machines as defined in the Unified Contact Center Enterprise Virtualization Document.

Click OK .

### Self-signed Certificate for Unified CCE Web Application

As part of the upgrade of Unified CCE servers, self-signed certificates employed by Unified CCE web applications such as Unified
                                          CCE web administration tool and Websetup, may get regenerated. You must add the new certificates to the trust list on the
                                          appropriate end devices.

### Upgrade
                              		  Tools

During the upgrade
                              		  process, use the following tools as required:

Enhanced Database Migration Tool (EDMT)—A wizard application that is used for all upgrades to migrate the HDS, Logger, and
                                    BA databases during the upgrade process.

You can download the EDMT from Cisco.com by clicking Cisco Enhanced Data Migration Tool Software Releases .

The prerequisites for running EDMT are:

EDMT requires Microsoft® ODBC Driver 17 .10.6 (or later versions of ODBC 17) for SQL Server® and Visual C++ Redistributable for Visual Studio 2022. The latest version of these packages can be downloaded
                                             from the Microsoft website. However, a copy of the same is also available in the Prerequisites folder of EDMT.

The EDMT displays status messages during the migration process, including warnings and errors. Warnings are displayed for
                                    informational purposes only and do not stop the migration. On the other hand, errors stop the migration process and leave
                                    the database in a corrupt state. If an error occurs, restore the database from your backup, fix the error, and run the tool
                                    again.

You can select either SQL Server Authentication or Windows Authentication during database migration. In certain scenarios, for example, where the source and destination machines are in different
                                                      domains, SQL Server Authentication can be used.

If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                                      SERVICE), you must run EDMT as an administrator.

The installer, not the EDMT, upgrades the AW database for the Administration & Data Server.

Unified CCE 15.0(1) installer and EDMT 15.0(1) will not allow the upgrade from the supported previous versions configured
                                                      with unsupported deployment type. Deployment type need to be updated before the upgrade. For the details on the list of unsupported
                                                      deployment type and replacement, check the Removed and Unsupported Features section in Release Notes for Cisco Contact Center Enterprise Solutions .

## Packaged CCE 2000 Agents Deployment

### Common Ground Upgrade Process

#### Redundant Upgrade Workflow

The redundant upgrade workflow is applicable to the solution deployments with Main site only.

Important

The upgrade requires four maintenance windows:

First maintenance window to shut down services on Side A and upgrade Side A

Second maintenance window in the middle of the upgrade to cut over from Side B to Side A. You must bring down Side B before
                                                   you bring up Side A.

Third maintenance window after you upgrade Side B to synchronize Side A to Side B.

Fourth maintenance window to upgrade Cisco Unified Communications Manager (CUCM).

##### Common Preupgrade Tasks

Perform the tasks in the following table in the order that they are listed.

Task

During upgrades, when the system first migrates your existing ECC variables to the Default payload, it does not check the
                                                CTI message size limit. The member names might exceed the extra 500 bytes that is allocated for ECC payloads to a CTI client.
                                                Manually check the CTI Message Size counter in the Expanded Call Variable Payload List tool to ensure that the Default payload
                                                does not exceed the limit. If the Default payload exceeds the limit, modify it to meet the limit.

Take a snapshot of each virtual machine you are upgrading from the VMware vSphere Client.

##### Preupgrade of Side A

Task

Reverse the Cisco IOS Enterprise Ingress Voice Gateway dial-peer priority configuration so that calls are sent to the Side
                                                B Unified CVP server.

Using the maintenance mode command , stop all Unified CCE services on the Unified CCE servers that you are upgrading, and set the startup type to Manual . For more information about the maintainence mode command, see the Invoking Maintainence Mode topic in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Side A Unified CCE Rogger

Side A Unified CCE AW-HDS-DDS

Side A PG

External HDS with Side A as the Central Controller preferred side (if used)

Verify that the services are stopped.

##### Upgrade Side A

Before you begin, check the following to confirm that call activity has ended on Side A:

On the Unified CVP Statistics portal, make sure that no Side A ports are in use.

Navigate to Unified CCE Administration > Infrastructure > Inventory .

Click the Statistics icon to view the statistics for CVP machine.

The Infrastructure tab for Call Server displays the port usage information.

In the Unified Communications Manager RTMT tool, check that phones have migrated to Side B.

Place upgrade media ISOs on local data stores. Make sure to remove them when the upgrade is complete.

Task

Upgrade to a supported version of ESXi version, if needed.

For the supported ESXi versions for this release, see the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html .

If you are using a supported ESXi version and want to upgrade to different supported ESXi version, you can upgrade now, or
                                                after the Packaged CCE upgrade is complete.

See Upgrade VMware vSphere ESXi .

Upgrade Unified CVP Server.

For more details, see the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

After upgrading the Unified CVP server, add the CVP machine to the domain. For more information, see Add Machine to Domain .

Upgrade all the Cisco Voice Gateways one after another.

See Upgrade Cisco Voice Gateway IOS Version .

The IOS version of the Cisco Voice Gateways must be upgraded to the minimum version required by Packaged CCE 12.0(1) . For more details, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html for IOS support information.

Upgrade all the Cisco Virtualized Voice Browsers one after another.

For more details, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html .

Upgrade the publishers/primary nodes of Cisco Finesse.

When upgrading from Cisco Finesse 12.6(2) to 15.0(1), Unified Intelligence Center gadgets won't load. To resolve this, Upgrade
                                                Unified Intelligence Center to either 12.6(2) ES 04 or to 15.0(1).

For details, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html

Upgrade the publishers/primary nodes of Cisco Unified Intelligence Center with Live Data and Identity Service (IdS).

For details, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Back up and export the Side A SQL database and the Outbound Option (if used) in Rogger VM.

Use Microsoft SQL Server Backup and Restore utilities for the back up.

Note the HDS customizable values.

Copy the backup files to a shared location.

Upgrade Microsoft Windows Server for CCE components. The supported Operating system is Windows Server 2022.

For details, see Upgrade Windows Server .

For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1)

Upgrade Microsoft SQL Server, supports SQL Server version 2022.

For details, see Upgrade SQL Server .

Run the Enhanced Database Migration Tool on rogger, external HDS (if used), and non-external HDS to perform a schema upgrade
                                                during the upgrade process.

See Run EDMT .

Run the Unified CCE Release installer on the Side A Unified CCE Rogger.

See Install Cisco Unified Contact Center Enterprise .

Run the Unified CCE Release installer on the Side A Unified CCE AW-HDS-DDS.

See Install Cisco Unified Contact Center Enterprise .

Run the Unified CCE installer on the Side A PG.

See Install Cisco Unified Contact Center Enterprise

Before upgrading the Side A PG, encrypt the JTAPI password. See Step 3 of the table Upgrade UCM in Side A and Side B

(Optional) Upgrade the External HDS associated with Side A (if used)

Run the Unified CCE Release installer the External HDS associated with Side A.

See Install Cisco Unified Contact Center Enterprise .

(Optional) Upgrade ECE.

See Enterprise Chat and Email Installation Guide (for Packaged Contact Center Enterprise) at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

(Optional) Install language pack

Install the language pack on the Side A AW-HDS-DDS and External HDS associated with Side A (if used).

See Install the Language Pack .

##### Side A Postupgrade Tasks

You must bring up Side A service before you bring down Side B services.

Task

Reverse the Cisco IOS Enterprise Ingress Voice Gateway dial-peer priority configuration so that calls are sent to the Side
                                                A Unified CVP server first and then to Side B.

Perform Database Performance Enhancement of TempDB, Logger Database, and AW-HDS Database. For more information, see Database Performance Enhancement .

Using Unified CCE Service Control, start all Unified CCE services on the Side A Unified CCE servers that you are upgrading,
                                                and set the startup type to Automatic .

Side A Unified CCE Rogger

Side A Unified CCE AW-HDS-DDS

Side A PG

External HDS with Side A as the Central Controller preferred side (if used)

When Side A router service starts, Side B router service will stop automatically.

Verify that the services have started.

Direct agents to sign into the Side A Finesse Primary node.

##### Preupgrade of Side B

Task

Using the maintenance mode command, stop all Unified CCE services on the Side B Unified CCE servers that you are upgrading,
                                                and set the startup type to Manual . For more information about the maintainence mode command, See the Invoking Maintainence Mode topic in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

Side B Unified CCE Rogger

Side B Unified CCE AW-HDS-DDS

Side B PG

External HDS with Side B as the Central Controller preferred side (if used)

Verify that the services have stopped.

##### Upgrade Side B

Before you begin, check the following to confirm that call activity has ended on Side B:

On the Unified CVP Statistics portal, make sure that no Side B ports are in use.

Navigate to Unified CCE Administration > Infrastructure > Inventory .

Click the Statistics icon to view the statistics for CVP machine.

The Infrastructure tab for Call Server displays the port usage information.

In the Unified Communications Manager RTMT tool, check that phones have migrated to Side A.

Place the upgrade media ISOs on local data stores. Ensure that you remove the media ISOs when the upgrade is complete.

Task

Upgrade to a supported version of ESXi version, if needed.

For the supported ESXi versions for this release, see the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html .

If you are using a supported ESXi version and want to upgrade to different supported ESXi version, you can upgrade now, or
                                                after the Packaged CCE upgrade is complete.

See Upgrade VMware vSphere ESXi .

Upgrade the Unified CVP Reporting Server

See Upgrade Unified CVP Reporting Server

After upgrading the Unified CVP Reporting server, add the CVP Reporting server to the domain. For more information, see Add Machine to Domain .

Upgrade Unified CVP Server.

For more details, see the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

After upgrading the Unified CVP server, add the CVP machine to the domain. For more information, see Add Machine to Domain .

Upgrade the subscribers/secondary nodes of Cisco Finesse.

When upgrading from Cisco Finesse 12.6(2) to 15.0(1), Unified Intelligence Center gadgets won't load. To resolve this, Upgrade
                                                Unified Intelligence Center to either 12.6(2) ES 04 or to 15.0(1).

For details, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html

Upgrade the subscribers/secondary nodes of Cisco Unified Intelligence Center with Live Data and Identity Service (IdS).

For details, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Back up and export the Side B SQL database and the Outbound Option (if used) database in the Rogger VM.

Use Microsoft SQL Server Backup and Restore utilities for the back up.

Note the HDS customizable values.

Copy the backup files to a shared location.

Upgrade Microsoft Windows Server for CCE components. The supported Operating system is Windows Server 2022.

For details, see Upgrade Windows Server .

For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1)

Upgrade Microsoft SQL Server, supports SQL Server version 2022.

For details, see Upgrade SQL Server .

Run the Enhanced Database Migration Tool on rogger, external HDS (if used), and non-external HDS to perform a schema upgrade
                                                during the upgrade process.

See Run EDMT .

Run the Unified CCE installer on the Side B Unified CCE Rogger.

See Install Cisco Unified Contact Center Enterprise

Run the Unified CCE installer on the Side B Unified CCE AW-HDS-DDS.

See Install Cisco Unified Contact Center Enterprise

Run the Unified CCE installer on the Side B PG.

See Install Cisco Unified Contact Center Enterprise

Before upgrading the Side B PG, encrypt the JTAPI password. See Step 6 of the table Upgrade UCM in Side A and Side B

(Optional) Upgrade the External HDS associated with Side B (if used)

See Install Cisco Unified Contact Center Enterprise

(Optional) Upgrade ECE.

##### Sync Side A to Side B

Perform these tasks during the third maintenance window to sync Side A and Side B.

Task

On each of the following VMs, select Unified CCE Service Control on the desktop. Start the Unified CCE services and change Startup to Automatic, in this order:

Side B Unified CCE Rogger

Side B Unified CCE AW-HDS-DDS

Side B PG

External HDS with Side B as the Central Controller preferred side (if used)

Verify that the services are started.

Perform Database Performance Enhancement of TempDB, Logger Database, and AW-HDS Database for Side B. For more information,
                                                see Database Performance Enhancement .

Run the UserRoleUpdate.PS1 tool in Powershell in any one of the distributor machines. This ensures that the User Role is updated in the database for
                                                the existing users.

To download UserRoleUpdate.PS1 script, go to the link https://software.cisco.com/download/home/268439622/type and select User Role Update Bulk Tool from the list.

Download the file UserRoleUpdateScript_1201.zip and extract the script.

##### Postupgrade Tasks

Task

Bring back Side A and Side B to call flow

Change the Cisco IOS Enterprise Voice Gateway dial-peer configuration to point to both Side A and Side B Unified CVP Servers.

##### Upgrade UCM in Side A and Side B

Perform these tasks to upgrade UCM in both Side A and Side B.

Important

Upgrade of CUCM requires a minimal maintenance window.

Step

Task

1

Upgrade the Side A CUCM Publisher and Subscriber.

2

Upgrade JTAPI on the Side A PG. See Upgrade Cisco JTAPI Client on PG .

Important

If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG .

3

For the Agent PG on the Side A , run the CceCrypTool to encrypt the JTAPI password.

To run CceCrypTool, open command prompt in administrator mode and run the following command:

For example:

CceCrypTool /instance ucce /component PG1A /proc jgw1 /mode encrypt

Side B

4

Upgrade the Side B CUCM Subscriber.

Important

The CUCM Publisher upgrade must be complete and the 14.0 software must be active before you upgrade the CUCM Subscriber.

5

Upgrade JTAPI on the Side B PG. See Upgrade Cisco JTAPI Client on PG .

Important

If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG .

6

For the Agent PG on the Side B, run the CceCrypTool to encrypt the JTAPI password.

To run CceCrypTool, open command prompt in administrator mode and run the following command:

For example:

CceCrypTool /instance ucce /component PG1A /proc jgw1 /mode encrypt

###### Cisco Unified Communications Manager 14.0 and above - Steps After Upgrade

Perform the following tasks if Cisco Unified Communications Manager (CUCM) is on-box and if you have upgraded to CUCM 14.0.
                                          This procedure is performed on the main site.

Do not change the IP address of both CUCM Publisher and Subscriber.

Step

Task

1

Move CUCM Publisher and Subscriber from Side A host to a different
                                                   host.

2

Move CUCM Subscriber from Side B host to a different host.

3

Delete CUCM references from all the location configurations.

4

Add CUCM Publisher as an external machine to the main site of the Packaged CCE Inventory .

#### Multistage Upgrade Workflow

The multistage upgrade workflow is applicable for solution deployments with both main site and remote site (if available).

A Unified CCE solution upgrade likely involves a multistage process; components are grouped in several stages for upgrading.
                                             At each stage in the upgrade, the upgraded components must interoperate with components that haven’t yet been upgraded to
                                             ensure the overall operation of the contact center. Therefore, it’s important to verify this interoperability during the planning
                                             stages of the upgrade.

Before upgrading a production system, perform the upgrade on a lab system that mirrors your production system to identify
                                             potential problems safely.

The following table details the required sequence for upgrading Packaged CCE 2000 Agent Deployments components, and the minimum component groupings that must occur together within each stage. Follow
                                 each stage to completion within each maintenance window. Each maintenance window must accommodate any testing required to
                                 ensure system integrity and contact center operation.

You can combine more than one complete stage into a single maintenance window, but you can’t break any one stage into multiple
                                 maintenance windows.

The sequence of upgrade is as per the Upgrade Flowcharts for 2000 Agent Deployments . Upgrade the Unified CCE components as follows:

Upgrade Agent Desktop, CUIC, Live Data, and IdS server along with the Unified CCE Central Controller upgrade.

After upgrading Finesse, IdS, and CUIC, import the IdS certificates to the Finesse and CUIC servers.

Run Stage 4 and Stage 5 upgrades in the same maintenance window.

Stage

Component Group

Components

Notes

1

(Optional) Reverse Proxy - VPN-less Access, Digital Channels

Cisco Reverse Proxy

If you don't have Cisco Reverse Proxy in your environment and you want to use VPN-less desktop access feature or to upgrade
                                             Cisco Reverse Proxy 12.6(2) to 15.0(1), you must install Cisco Reverse Proxy 15.0(1). Refer to the Notes on VM Templates for 15.0(1) topic in the Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS page for the installer location. For more information on how to install Cisco Reverse Proxy, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) .

Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments.

2

Platform Orchestration, Hybrid Features

Cloud Connect

If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Unified Customer Voice Portal (CVP) ( Reporting Server, Call Server/VXMLServer, Unified Call Studio)

You must upgrade all sites before proceeding to the next stage.

Before you upgrade to Unified CVP 12.6 and above, you must apply the latest ES of Packaged CCE 12.5 .

For more information, see Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see Stage 5 .)

Cisco Virtualized Voice Browser

ECE

Cisco Finesse

Unified CCE Rogger

Admin & Data server (AW/HDS/DDS)

CUIC-LD-IDS

CUIC Reporting Templates

CCMP

To increase the hard disk before you upgrade the Unified CCE Rogger and Admin & Data server, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations

After you upgrade AW, import the self-signed certificate of all solution components (if applicable) to all AWs.

For more information about performing in-place upgrade of Windows Server, see Upgrade Windows server and Upgrade SQL Server .

After you upgrade Finesse to Release 15.0(1), to load any gadgets to Finesse, you must first import all self-signed certificates
                                                   (if applicable) to Finesse.

After upgrading Finesse to 15.0(1), ensure that both ECDSA and RSA valid certificates are available in the certificate store
                                                   in PG. If not, you must export the Finesse Tomcat certificates and import them to CTI Gateway (CG) and Peripheral Gateway
                                                   (PG) systems. For more information, refer to the Add Certificate for HTTPS Gadget section in the Cisco Finesse Administration Guide .

After upgrading cuic-ld-ids to 15.0(1), run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL.

For more information about Finesse, see Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

For more information about ECE, see https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

If you are upgrading from Cisco IdS 12.6(1) or earlier, ensure that all SSO users log out of the Cisco Finesse Agent Desktop,
                                                   Unified CCE Administration Portal, and Unified Intelligence Center Dashboard before bringing the upgraded IdS nodes online.

Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                   using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                   and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                   the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                   node is upgraded and in the IN_SERVICE status.

For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP.

Deployments using VPN-less access to Finesse desktop should also upgrade the reverse-proxy to 15.0(1) before Cisco IdS is
                                                   upgraded to 15.0(1).

After you upgrade Cisco IdS, it is necessary to exchange metadata, especially if you are using SSO or integrating with other
                                                   identity providers. This process ensures that the upgraded system can properly communicate and authenticate with other services.

After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

To ensure the secure Finesse token works correctly for non-SSO agents, verify that CUIC, LD, and Reverse Proxy systems are
                                                   running the same version as Finesse. Also, ensure that you import the Finesse certificates into each of these systems.

Agent (Unified Communications Manager) PG

Outbound Option Dialer and SIP IOS Gateway

To increase the hard disk before you upgrade the Agent PG and Outbound Option Dialer, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations

You can have many PGs located on different virtual machines. You can upgrade each PG VMs by leveraging the capabilities of graceful shutdown feature. For more information about the graceful
                                                      shutdown, see the Graceful Shutdown chapter in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

MR PG, VRU PG

CRM connector

To increase the hard disk before you upgrade MR PG and VRU PG, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations

You can have many PGs located on different virtual machines. You can upgrade each PG VMs by leveraging the capabilities of graceful shutdown feature. For more information about the graceful
                                                      shutdown, see the Graceful Shutdown chapter in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

Cisco Unified Communications Manager (Unified Communications Manager)

JTAPI on Agent (Unified Communications Manager) PG

—

### Hardware Refresh with Common Ground Upgrade

Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html

After you configure the servers, you can move the VMs to the servers and complete the Common Ground Upgrade Process .

As a part of hardware refresh, if you are migrating from existing Cisco UCS C240 M5SX or Cisco UCS C240 M6SX or Cisco HX220c-M5SX or Cisco HX220c-M6S hardware, perform the following migration steps:

#### Pre-migration Steps

Step

Task

1

Upgrade to the latest release with the latest ES on old hardware.
                                             For upgrade procedure, refer the Cisco Packaged Contact
                                                Center Enterprise Installation and Upgrade Guide Release at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

2

Update the annotation of the core VMs as per requirement for
                                             Specification Based hardware. See Installation Tasks .

#### Migration Steps

Steps

Task

1

Move the VMs to the target hardware

2

Log in to the Packaged CCE Administration and open the
                                             Inventory.

3

Perform the following in the Packaged CCE Inventory:

Click Update Hosts.

Provide ESXI details of the target hardware.

Select the hardware type as M5 or HX M5 Tested Reference Configuration / Specification Based Configuration , to migrate to Cisco UCS C240 M5SX or Cisco UCS C240 M6SX or Cisco HX220c-M5SX or Cisco HX220c-M6S hardware .

Complete the wizard.

If CUCM and CVP Reporting Server were on-box in the old
                                                         hardware, you must add them back as external machines after
                                                         completing the deployment.

#### Post-migration Step

Step

Task

1

Complete the common ground hardware upgrade process. See Common Ground Upgrade Process .

## Packaged CCE 4000 Agents and above Deployment

### Multistage Upgrade Workflow

A CCE solution upgrade likely involves a multistage process; components are grouped in several stages for upgrading. At each
                                          stage in the upgrade, the upgraded components must interoperate with components that have not yet been upgraded to ensure
                                          the overall operation of the contact center. Therefore, it is important to verify this interoperability during the planning
                                          stages of the upgrade.

Before upgrading a production system, perform the upgrade on a lab system that mirrors your productionsystem to identify potential
                                          problems safely.

The following table details the required sequence for upgrading Packaged CCE 4000 Agent Deployments components, and the minimum
                              component groupings that must occur together within each stage. Follow each stage to completion within each maintenance window.
                              Each maintenance window must accommodate any testing required to ensure system integrity and contact center operation.

You can combine more than one complete stage into a single maintenance window, but you cannot break any one stage into multiple
                              maintenance windows.

The sequence of upgrade is as per the Upgrade Flowcharts for 4000 Agents and above Deployments . Upgrade the CCE components as follows:

In case of 4K deployment the CCE components consists of Rogger VM instead of Router and Logger VMs.

Stage

Component Group

Components

Notes

1

(Optional) Reverse Proxy - VPN-less Access, Digital Channels

Cisco Reverse Proxy

If you don't have Cisco Reverse Proxy in your environment and you want to use VPN-less desktop access feature or to upgrade
                                          Cisco Reverse Proxy 12.6(2) to 15.0(1), you must install Cisco Reverse Proxy 15.0(1). Refer to the Notes on VM Templates for 15.0(1) topic in the Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS page for the installer location. For more information on how to install Cisco Reverse Proxy, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) .

Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments.

2

Platform Orchestration, Hybrid Features

Cloud Connect

If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                          Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio)

You must upgrade all sites before proceeding to the next stage.

For more information, see Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see Stage 8 .)

Cisco Virtualized Voice Browser

Identity Service

IdS Server

If you are upgrading from Cisco IDS 12.6(1) or earlier, ensure that all SSO users log out of the Cisco Finesse Agent Desktop,
                                          Unified CCE Administration Portal, and Unified Intelligence Center Dashboard before bringing the upgraded IDS nodes online.

Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                          using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                          and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                          the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                          node is upgraded and in the IN_SERVICE status.

For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP.

Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 15.0(1) before Cisco IdS is
                                          upgraded to 15.0(1).

For IdS upgrade, see the procedure as documented in the Upgrades section of Unified Intelligence Center Installation and Upgrade Guide at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Agent and supervisor desktops

ECE

Cisco Finesse

After you upgrade Finesse to Release 
                                          15.0(1), to load any gadgets to Finesse, you must first import all self-signed certificates (if applicable) to Finesse.

For more information about Finesse, see Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

After upgrading Finesse to 15.0(1), ensure that both ECDSA and RSA valid certificates are available in the certificate store
                                          in PG. If not, you must export the Finesse Tomcat certificates and import them to CTI Gateway (CG) and Peripheral Gateway
                                          (PG) systems. For more information, refer to the Add Certificate for HTTPS Gadget section in the Cisco Finesse Administration Guide .

For more information about ECE, see https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

CUIC server

After you upgrade Cisco Unified Intelligence Center (CUIC), you must:

Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname.

Import LD and Finesse certificates to CUIC.

Unified CCE Rogger

Admin & Data server (AW/HDS/DDS)

Standalone Live Data

CUIC Reporting Templates

Administration Client

To increase the hard disk before you upgrade the Unified CCE Rogger and Admin & Data server, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations

After you upgrade AW, import the self-signed certificate of all solution components (if applicable) to all AWs.

After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

After you upgrade LD, you must import the Finesse certificate to LD.

For Live Data VM, you have to increase the RAM before upgrading. See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html

Agent (Unified Communications Manager) PG

CTI Server

Outbound Option Dialer and SIP IOS Gateway

To increase the hard disk before you upgrade Agent PG, CTI Server and Outbound Option Dialer, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations

You can have many PGs located on different virtual machines. You can upgrade each PG VMs by leveraging the capabilities of
                                                graceful shutdown feature. For more information about the graceful shutdown, see the Graceful Shutdown chapter in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

MR PG, VRU PG

CRM connector

To increase the hard disk before you upgrade MR PG and VRU PG, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations

You can have many PGs located on different virtual machines. You can upgrade each PG VMs by leveraging the capabilities of
                                                graceful shutdown feature. For more information about the graceful shutdown, see the Graceful Shutdown chapter in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

Cisco Unified Communications Manager (Unified Communications Manager)

JTAPI on Agent (Unified Communications Manager) PG

If you upgrade to CUCM 12.5 on the servers, ensure that you deploy CUCM off-box. CUCM 12.5 on-box deployment are only supported for M5 servers.

### Customers Also Viewed

- Implement CA-Signed Certificates in a CCE 12.6 Solution

| Supported Upgrade Paths | In-place Upgrade Supported Platforms (From) | In-place Upgrade Supported Platforms (To) |
|---|---|---|
| Packaged CCE 12.5(2)/12.6(x) to Packaged CCE 15.0(1). | Windows Server 2016 and SQL Server 2017 Windows Server 2019 and SQL Server 2019 | Windows Server 2022 and SQL Server 2022 |

| Note | The Common Ground upgrade from Windows Server 2016 and SQL Server 2017 is only supported if an in-place platform upgrade is
                                          performed to Windows Server 2022 and SQL Server 2022, and not to Windows Server 2019 and SQL Server 2019 |
|---|---|

| Note | To update the VM properties of specific components such as Cloud Connect, Cisco Finesse, Unified CVP, and so on, refer to
                                                the respective virtualization guide under the Contact Center section at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . |
|---|---|

| Caution | Be careful when you upgrade the virtual machine network adapters. Done incorrectly, this upgrade can compromise the fault
                                          tolerance of your Cisco Contact Center. |
|---|---|

| Note | As part of the upgrade of Unified CCE servers, self-signed certificates employed by Unified CCE web applications such as Unified
                                          CCE web administration tool and Websetup, may get regenerated. You must add the new certificates to the trust list on the
                                          appropriate end devices. |
|---|---|

| Note | You can select either SQL Server Authentication or Windows Authentication during database migration. In certain scenarios, for example, where the source and destination machines are in different
                                                      domains, SQL Server Authentication can be used. If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                                      SERVICE), you must run EDMT as an administrator. The installer, not the EDMT, upgrades the AW database for the Administration & Data Server. Unified CCE 15.0(1) installer and EDMT 15.0(1) will not allow the upgrade from the supported previous versions configured
                                                      with unsupported deployment type. Deployment type need to be updated before the upgrade. For the details on the list of unsupported
                                                      deployment type and replacement, check the Removed and Unsupported Features section in Release Notes for Cisco Contact Center Enterprise Solutions . |
|---|---|

| Note | The redundant upgrade workflow is applicable to the solution deployments with Main site only. |
|---|---|

| Important | The upgrade requires four maintenance windows: First maintenance window to shut down services on Side A and upgrade Side A Second maintenance window in the middle of the upgrade to cut over from Side B to Side A. You must bring down Side B before
                                                   you bring up Side A. Third maintenance window after you upgrade Side B to synchronize Side A to Side B. Fourth maintenance window to upgrade Cisco Unified Communications Manager (CUCM). |
|---|---|

| Task |
|---|
| During upgrades, when the system first migrates your existing ECC variables to the Default payload, it does not check the
                                                CTI message size limit. The member names might exceed the extra 500 bytes that is allocated for ECC payloads to a CTI client.
                                                Manually check the CTI Message Size counter in the Expanded Call Variable Payload List tool to ensure that the Default payload
                                                does not exceed the limit. If the Default payload exceeds the limit, modify it to meet the limit. |
| Take a snapshot of each virtual machine you are upgrading from the VMware vSphere Client. |

| Task |
|---|
|  |
| Reverse the Cisco IOS Enterprise Ingress Voice Gateway dial-peer priority configuration so that calls are sent to the Side
                                                B Unified CVP server. |
| Using the maintenance mode command , stop all Unified CCE services on the Unified CCE servers that you are upgrading, and set the startup type to Manual . For more information about the maintainence mode command, see the Invoking Maintainence Mode topic in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . Side A Unified CCE Rogger Side A Unified CCE AW-HDS-DDS Side A PG External HDS with Side A as the Central Controller preferred side (if used) Verify that the services are stopped. |

| Task |
|---|
| Upgrade to a supported version of ESXi version, if needed. For the supported ESXi versions for this release, see the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html . If you are using a supported ESXi version and want to upgrade to different supported ESXi version, you can upgrade now, or
                                                after the Packaged CCE upgrade is complete. See Upgrade VMware vSphere ESXi . |
| Upgrade Unified CVP Server. For more details, see the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . After upgrading the Unified CVP server, add the CVP machine to the domain. For more information, see Add Machine to Domain . |
| Upgrade all the Cisco Voice Gateways one after another. See Upgrade Cisco Voice Gateway IOS Version . The IOS version of the Cisco Voice Gateways must be upgraded to the minimum version required by Packaged CCE 12.0(1) . For more details, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html for IOS support information. |
| Upgrade all the Cisco Virtualized Voice Browsers one after another. For more details, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html . |
| Upgrade the publishers/primary nodes of Cisco Finesse. When upgrading from Cisco Finesse 12.6(2) to 15.0(1), Unified Intelligence Center gadgets won't load. To resolve this, Upgrade
                                                Unified Intelligence Center to either 12.6(2) ES 04 or to 15.0(1). For details, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html |
| Upgrade the publishers/primary nodes of Cisco Unified Intelligence Center with Live Data and Identity Service (IdS). For details, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Back up and export the Side A SQL database and the Outbound Option (if used) in Rogger VM. Use Microsoft SQL Server Backup and Restore utilities for the back up. Note the HDS customizable values. Copy the backup files to a shared location. |
| Upgrade Microsoft Windows Server for CCE components. The supported Operating system is Windows Server 2022. For details, see Upgrade Windows Server . Note To increase the hard disk before you upgrade the component, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1) | Note | To increase the hard disk before you upgrade the component, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1) |
| Note | To increase the hard disk before you upgrade the component, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1) |
| Upgrade Microsoft SQL Server, supports SQL Server version 2022. For details, see Upgrade SQL Server . |
| Run the Enhanced Database Migration Tool on rogger, external HDS (if used), and non-external HDS to perform a schema upgrade
                                                during the upgrade process. See Run EDMT . |
|  |
| Run the Unified CCE Release installer on the Side A Unified CCE Rogger. See Install Cisco Unified Contact Center Enterprise . |
| Run the Unified CCE Release installer on the Side A Unified CCE AW-HDS-DDS. See Install Cisco Unified Contact Center Enterprise . |
| Run the Unified CCE installer on the Side A PG. See Install Cisco Unified Contact Center Enterprise Note Before upgrading the Side A PG, encrypt the JTAPI password. See Step 3 of the table Upgrade UCM in Side A and Side B | Note | Before upgrading the Side A PG, encrypt the JTAPI password. See Step 3 of the table Upgrade UCM in Side A and Side B |
| Note | Before upgrading the Side A PG, encrypt the JTAPI password. See Step 3 of the table Upgrade UCM in Side A and Side B |
| (Optional) Upgrade the External HDS associated with Side A (if used) Run the Unified CCE Release installer the External HDS associated with Side A. See Install Cisco Unified Contact Center Enterprise . |
| (Optional) Upgrade ECE. See Enterprise Chat and Email Installation Guide (for Packaged Contact Center Enterprise) at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| (Optional) Install language pack Install the language pack on the Side A AW-HDS-DDS and External HDS associated with Side A (if used). See Install the Language Pack . |
|  |

| Note | To increase the hard disk before you upgrade the component, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1) |
|---|---|

| Note | Before upgrading the Side A PG, encrypt the JTAPI password. See Step 3 of the table Upgrade UCM in Side A and Side B |
|---|---|

| Task |
|---|
| Reverse the Cisco IOS Enterprise Ingress Voice Gateway dial-peer priority configuration so that calls are sent to the Side
                                                A Unified CVP server first and then to Side B. |
|  |
|  |
| Perform Database Performance Enhancement of TempDB, Logger Database, and AW-HDS Database. For more information, see Database Performance Enhancement . |
| Using Unified CCE Service Control, start all Unified CCE services on the Side A Unified CCE servers that you are upgrading,
                                                and set the startup type to Automatic . Side A Unified CCE Rogger Side A Unified CCE AW-HDS-DDS Side A PG External HDS with Side A as the Central Controller preferred side (if used) Note When Side A router service starts, Side B router service will stop automatically. Verify that the services have started. | Note | When Side A router service starts, Side B router service will stop automatically. |
| Note | When Side A router service starts, Side B router service will stop automatically. |
|  |
| Direct agents to sign into the Side A Finesse Primary node. |

| Note | When Side A router service starts, Side B router service will stop automatically. |
|---|---|

| Task |
|---|
|  |
| Using the maintenance mode command, stop all Unified CCE services on the Side B Unified CCE servers that you are upgrading,
                                                and set the startup type to Manual . For more information about the maintainence mode command, See the Invoking Maintainence Mode topic in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html Side B Unified CCE Rogger Side B Unified CCE AW-HDS-DDS Side B PG External HDS with Side B as the Central Controller preferred side (if used) Verify that the services have stopped. |

| Task |
|---|
| Upgrade to a supported version of ESXi version, if needed. For the supported ESXi versions for this release, see the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html . If you are using a supported ESXi version and want to upgrade to different supported ESXi version, you can upgrade now, or
                                                after the Packaged CCE upgrade is complete. See Upgrade VMware vSphere ESXi . |
| Upgrade the Unified CVP Reporting Server See Upgrade Unified CVP Reporting Server After upgrading the Unified CVP Reporting server, add the CVP Reporting server to the domain. For more information, see Add Machine to Domain . |
| Upgrade Unified CVP Server. For more details, see the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . After upgrading the Unified CVP server, add the CVP machine to the domain. For more information, see Add Machine to Domain . |
| Upgrade the subscribers/secondary nodes of Cisco Finesse. When upgrading from Cisco Finesse 12.6(2) to 15.0(1), Unified Intelligence Center gadgets won't load. To resolve this, Upgrade
                                                Unified Intelligence Center to either 12.6(2) ES 04 or to 15.0(1). For details, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html |
| Upgrade the subscribers/secondary nodes of Cisco Unified Intelligence Center with Live Data and Identity Service (IdS). For details, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Back up and export the Side B SQL database and the Outbound Option (if used) database in the Rogger VM. Use Microsoft SQL Server Backup and Restore utilities for the back up. Note the HDS customizable values. Copy the backup files to a shared location. |
| Upgrade Microsoft Windows Server for CCE components. The supported Operating system is Windows Server 2022. For details, see Upgrade Windows Server . Note To increase the hard disk before you upgrade the component, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1) | Note | To increase the hard disk before you upgrade the component, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1) |
| Note | To increase the hard disk before you upgrade the component, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1) |
| Upgrade Microsoft SQL Server, supports SQL Server version 2022. For details, see Upgrade SQL Server . |
| Run the Enhanced Database Migration Tool on rogger, external HDS (if used), and non-external HDS to perform a schema upgrade
                                                during the upgrade process. See Run EDMT . |
|  |
| Run the Unified CCE installer on the Side B Unified CCE Rogger. See Install Cisco Unified Contact Center Enterprise |
| Run the Unified CCE installer on the Side B Unified CCE AW-HDS-DDS. See Install Cisco Unified Contact Center Enterprise |
| Run the Unified CCE installer on the Side B PG. See Install Cisco Unified Contact Center Enterprise Note Before upgrading the Side B PG, encrypt the JTAPI password. See Step 6 of the table Upgrade UCM in Side A and Side B | Note | Before upgrading the Side B PG, encrypt the JTAPI password. See Step 6 of the table Upgrade UCM in Side A and Side B |
| Note | Before upgrading the Side B PG, encrypt the JTAPI password. See Step 6 of the table Upgrade UCM in Side A and Side B |
| (Optional) Upgrade the External HDS associated with Side B (if used) See Install Cisco Unified Contact Center Enterprise |
| (Optional) Upgrade ECE. See Enterprise Chat and Email Installation Guide (for Packaged Contact Center Enterprise) at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html . |
|  |

| Note | To increase the hard disk before you upgrade the component, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations For more information on hard disk capacity, see Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html#Version_15.0(1) |
|---|---|

| Note | Before upgrading the Side B PG, encrypt the JTAPI password. See Step 6 of the table Upgrade UCM in Side A and Side B |
|---|---|

| Task |
|---|
|  |
|  |
| On each of the following VMs, select Unified CCE Service Control on the desktop. Start the Unified CCE services and change Startup to Automatic, in this order: Side B Unified CCE Rogger Side B Unified CCE AW-HDS-DDS Side B PG External HDS with Side B as the Central Controller preferred side (if used) Verify that the services are started. |
| Perform Database Performance Enhancement of TempDB, Logger Database, and AW-HDS Database for Side B. For more information,
                                                see Database Performance Enhancement . |
| Run the UserRoleUpdate.PS1 tool in Powershell in any one of the distributor machines. This ensures that the User Role is updated in the database for
                                                the existing users. To download UserRoleUpdate.PS1 script, go to the link https://software.cisco.com/download/home/268439622/type and select User Role Update Bulk Tool from the list. Download the file UserRoleUpdateScript_1201.zip and extract the script. |

| Task |
|---|
| Bring back Side A and Side B to call flow |
|  |
| Change the Cisco IOS Enterprise Voice Gateway dial-peer configuration to point to both Side A and Side B Unified CVP Servers. |

| Important | Upgrade of CUCM requires a minimal maintenance window. |
|---|---|

| Step | Task |
|---|---|
| 1 | Upgrade the Side A CUCM Publisher and Subscriber. For detailed upgrade steps, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html . |
| 2 | Upgrade JTAPI on the Side A PG. See Upgrade Cisco JTAPI Client on PG . Important If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG . | Important | If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG . |
| Important | If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG . |
| 3 | For the Agent PG on the Side A , run the CceCrypTool to encrypt the JTAPI password. To run CceCrypTool, open command prompt in administrator mode and run the following command: CceCrypTool /instance <instance_name> /component <name of the component> /proc <name of the process> /mode <encrypt> For example: CceCrypTool /instance ucce /component PG1A /proc jgw1 /mode encrypt |
| Side B |
| 4 | Upgrade the Side B CUCM Subscriber. For detailed upgrade steps, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html . Important The CUCM Publisher upgrade must be complete and the 14.0 software must be active before you upgrade the CUCM Subscriber. | Important | The CUCM Publisher upgrade must be complete and the 14.0 software must be active before you upgrade the CUCM Subscriber. |
| Important | The CUCM Publisher upgrade must be complete and the 14.0 software must be active before you upgrade the CUCM Subscriber. |
| 5 | Upgrade JTAPI on the Side B PG. See Upgrade Cisco JTAPI Client on PG . Important If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG . | Important | If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG . |
| Important | If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG . |
| 6 | For the Agent PG on the Side B, run the CceCrypTool to encrypt the JTAPI password. To run CceCrypTool, open command prompt in administrator mode and run the following command: CceCrypTool /instance <instance_name> /component <name of the component> /proc <name of the process> /mode <encrypt> For example: CceCrypTool /instance ucce /component PG1A /proc jgw1 /mode encrypt |

| Important | If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG . |
|---|---|

| Important | The CUCM Publisher upgrade must be complete and the 14.0 software must be active before you upgrade the CUCM Subscriber. |
|---|---|

| Important | If you are installing CUCM 14.0 and above, download the Cisco JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG . |
|---|---|

| Note | Do not change the IP address of both CUCM Publisher and Subscriber. |
|---|---|

| Step | Task |
|---|---|
| 1 | Move CUCM Publisher and Subscriber from Side A host to a different
                                                   host. |
| 2 | Move CUCM Subscriber from Side B host to a different host. |
| 3 | Delete CUCM references from all the location configurations. |
| 4 | Add CUCM Publisher as an external machine to the main site of the Packaged CCE Inventory . |

| Note | The multistage upgrade workflow is applicable for solution deployments with both main site and remote site (if available). A Unified CCE solution upgrade likely involves a multistage process; components are grouped in several stages for upgrading.
                                             At each stage in the upgrade, the upgraded components must interoperate with components that haven’t yet been upgraded to
                                             ensure the overall operation of the contact center. Therefore, it’s important to verify this interoperability during the planning
                                             stages of the upgrade. Before upgrading a production system, perform the upgrade on a lab system that mirrors your production system to identify
                                             potential problems safely. |
|---|---|

| Note | Upgrade Agent Desktop, CUIC, Live Data, and IdS server along with the Unified CCE Central Controller upgrade. After upgrading Finesse, IdS, and CUIC, import the IdS certificates to the Finesse and CUIC servers. Run Stage 4 and Stage 5 upgrades in the same maintenance window. |
|---|---|

| Stage | Component Group | Components | Notes |
|---|---|---|---|
| 1 | (Optional) Reverse Proxy - VPN-less Access, Digital Channels | Cisco Reverse Proxy | If you don't have Cisco Reverse Proxy in your environment and you want to use VPN-less desktop access feature or to upgrade
                                             Cisco Reverse Proxy 12.6(2) to 15.0(1), you must install Cisco Reverse Proxy 15.0(1). Refer to the Notes on VM Templates for 15.0(1) topic in the Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS page for the installer location. For more information on how to install Cisco Reverse Proxy, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) . Note Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. | Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
| 2 | Platform Orchestration, Hybrid Features | Cloud Connect | If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| 3 | Queuing and self-service | Cisco Unified Customer Voice Portal (CVP) ( Reporting Server, Call Server/VXMLServer, Unified Call Studio) | You must upgrade all sites before proceeding to the next stage. Before you upgrade to Unified CVP 12.6 and above, you must apply the latest ES of Packaged CCE 12.5 . For more information, see Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . |
| 4 | Gateways | IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see Stage 5 .) Cisco Virtualized Voice Browser |  |
| 5 | Agent/Supervisor Desktop, Central Controller, and Reporting | ECE Cisco Finesse Unified CCE Rogger Admin & Data server (AW/HDS/DDS) CUIC-LD-IDS CUIC Reporting Templates CCMP | To increase the hard disk before you upgrade the Unified CCE Rogger and Admin & Data server, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations After you upgrade AW, import the self-signed certificate of all solution components (if applicable) to all AWs. Note For more information about performing in-place upgrade of Windows Server, see Upgrade Windows server and Upgrade SQL Server . After you upgrade Finesse to Release 15.0(1), to load any gadgets to Finesse, you must first import all self-signed certificates
                                                   (if applicable) to Finesse. After upgrading Finesse to 15.0(1), ensure that both ECDSA and RSA valid certificates are available in the certificate store
                                                   in PG. If not, you must export the Finesse Tomcat certificates and import them to CTI Gateway (CG) and Peripheral Gateway
                                                   (PG) systems. For more information, refer to the Add Certificate for HTTPS Gadget section in the Cisco Finesse Administration Guide . Note After upgrading cuic-ld-ids to 15.0(1), run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL. For more information about Finesse, see Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . For more information about ECE, see https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html If you are upgrading from Cisco IdS 12.6(1) or earlier, ensure that all SSO users log out of the Cisco Finesse Agent Desktop,
                                                   Unified CCE Administration Portal, and Unified Intelligence Center Dashboard before bringing the upgraded IdS nodes online. Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                   using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                   and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                   the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                   node is upgraded and in the IN_SERVICE status. For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP. Deployments using VPN-less access to Finesse desktop should also upgrade the reverse-proxy to 15.0(1) before Cisco IdS is
                                                   upgraded to 15.0(1). After you upgrade Cisco IdS, it is necessary to exchange metadata, especially if you are using SSO or integrating with other
                                                   identity providers. This process ensures that the upgraded system can properly communicate and authenticate with other services. After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . To ensure the secure Finesse token works correctly for non-SSO agents, verify that CUIC, LD, and Reverse Proxy systems are
                                                   running the same version as Finesse. Also, ensure that you import the Finesse certificates into each of these systems. | Note | For more information about performing in-place upgrade of Windows Server, see Upgrade Windows server and Upgrade SQL Server . | Note | After upgrading cuic-ld-ids to 15.0(1), run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL. |
| Note | For more information about performing in-place upgrade of Windows Server, see Upgrade Windows server and Upgrade SQL Server . |
| Note | After upgrading cuic-ld-ids to 15.0(1), run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL. |
| 6 | Peripherals | Agent (Unified Communications Manager) PG Outbound Option Dialer and SIP IOS Gateway | To increase the hard disk before you upgrade the Agent PG and Outbound Option Dialer, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations You can have many PGs located on different virtual machines. You can upgrade each PG VMs by leveraging the capabilities of graceful shutdown feature. For more information about the graceful
                                                      shutdown, see the Graceful Shutdown chapter in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |
| 7 | Peripherals | MR PG, VRU PG CRM connector | To increase the hard disk before you upgrade MR PG and VRU PG, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations You can have many PGs located on different virtual machines. You can upgrade each PG VMs by leveraging the capabilities of graceful shutdown feature. For more information about the graceful
                                                      shutdown, see the Graceful Shutdown chapter in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |
| 8 | Call Processing | Cisco Unified Communications Manager (Unified Communications Manager) JTAPI on Agent (Unified Communications Manager) PG | — |

| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
|---|---|

| Note | For more information about performing in-place upgrade of Windows Server, see Upgrade Windows server and Upgrade SQL Server . |
|---|---|

| Note | After upgrading cuic-ld-ids to 15.0(1), run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL. |
|---|---|

| Step | Task |
|---|---|
| 1 | Upgrade to the latest release with the latest ES on old hardware.
                                             For upgrade procedure, refer the Cisco Packaged Contact
                                                Center Enterprise Installation and Upgrade Guide Release at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html . |
| 2 | Update the annotation of the core VMs as per requirement for
                                             Specification Based hardware. See Installation Tasks . |

| Steps | Task |
|---|---|
| 1 | Move the VMs to the target hardware |
| 2 | Log in to the Packaged CCE Administration and open the
                                             Inventory. |
| 3 | Perform the following in the Packaged CCE Inventory: Click Update Hosts. Provide ESXI details of the target hardware. Select the hardware type as M5 or HX M5 Tested Reference Configuration / Specification Based Configuration , to migrate to Cisco UCS C240 M5SX or Cisco UCS C240 M6SX or Cisco HX220c-M5SX or Cisco HX220c-M6S hardware . Complete the wizard. Note If CUCM and CVP Reporting Server were on-box in the old
                                                         hardware, you must add them back as external machines after
                                                         completing the deployment. | Note | If CUCM and CVP Reporting Server were on-box in the old
                                                         hardware, you must add them back as external machines after
                                                         completing the deployment. |
| Note | If CUCM and CVP Reporting Server were on-box in the old
                                                         hardware, you must add them back as external machines after
                                                         completing the deployment. |

| Note | If CUCM and CVP Reporting Server were on-box in the old
                                                         hardware, you must add them back as external machines after
                                                         completing the deployment. |
|---|---|

| Step | Task |
|---|---|
| 1 | Complete the common ground hardware upgrade process. See Common Ground Upgrade Process . |

| Note | A CCE solution upgrade likely involves a multistage process; components are grouped in several stages for upgrading. At each
                                          stage in the upgrade, the upgraded components must interoperate with components that have not yet been upgraded to ensure
                                          the overall operation of the contact center. Therefore, it is important to verify this interoperability during the planning
                                          stages of the upgrade. Before upgrading a production system, perform the upgrade on a lab system that mirrors your productionsystem to identify potential
                                          problems safely. |
|---|---|

| Note | In case of 4K deployment the CCE components consists of Rogger VM instead of Router and Logger VMs. |
|---|---|

| Stage | Component Group | Components | Notes |
|---|---|---|---|
| 1 | (Optional) Reverse Proxy - VPN-less Access, Digital Channels | Cisco Reverse Proxy | If you don't have Cisco Reverse Proxy in your environment and you want to use VPN-less desktop access feature or to upgrade
                                          Cisco Reverse Proxy 12.6(2) to 15.0(1), you must install Cisco Reverse Proxy 15.0(1). Refer to the Notes on VM Templates for 15.0(1) topic in the Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS page for the installer location. For more information on how to install Cisco Reverse Proxy, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) . Note Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. | Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
| 2 | Platform Orchestration, Hybrid Features | Cloud Connect | In 15.0(1), the RAM requirement for Cloud Connect has changed. See the Update VM Properties section in the Upgrade Considerations for instructions on increasing hard disk and RAM before upgrading Cloud Connect. If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                          Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| 3 | Queuing and self-service | Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio) | You must upgrade all sites before proceeding to the next stage. For more information, see Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . |
| 4 | Gateways | IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see Stage 8 .) Cisco Virtualized Voice Browser |  |
| 5 | Identity Service | IdS Server | If you are upgrading from Cisco IDS 12.6(1) or earlier, ensure that all SSO users log out of the Cisco Finesse Agent Desktop,
                                          Unified CCE Administration Portal, and Unified Intelligence Center Dashboard before bringing the upgraded IDS nodes online. Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                          using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                          and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                          the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                          node is upgraded and in the IN_SERVICE status. For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP. Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 15.0(1) before Cisco IdS is
                                          upgraded to 15.0(1). For IdS upgrade, see the procedure as documented in the Upgrades section of Unified Intelligence Center Installation and Upgrade Guide at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| 6 | Agent and supervisor desktops | ECE Cisco Finesse | After you upgrade Finesse to Release 
                                          15.0(1), to load any gadgets to Finesse, you must first import all self-signed certificates (if applicable) to Finesse. For more information about Finesse, see Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . After upgrading Finesse to 15.0(1), ensure that both ECDSA and RSA valid certificates are available in the certificate store
                                          in PG. If not, you must export the Finesse Tomcat certificates and import them to CTI Gateway (CG) and Peripheral Gateway
                                          (PG) systems. For more information, refer to the Add Certificate for HTTPS Gadget section in the Cisco Finesse Administration Guide . For more information about ECE, see https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| 7 | Reporting server | CUIC server | After you upgrade Cisco Unified Intelligence Center (CUIC), you must: Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname. Import LD and Finesse certificates to CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . |
| 8 | Central Controller | Unified CCE Rogger Admin & Data server (AW/HDS/DDS) Standalone Live Data CUIC Reporting Templates Administration Client | To increase the hard disk before you upgrade the Unified CCE Rogger and Admin & Data server, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations After you upgrade AW, import the self-signed certificate of all solution components (if applicable) to all AWs. After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade LD, you must import the Finesse certificate to LD. Note For Live Data VM, you have to increase the RAM before upgrading. See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html | Note | For Live Data VM, you have to increase the RAM before upgrading. See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html |
| Note | For Live Data VM, you have to increase the RAM before upgrading. See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html |
| 9 | Peripherals | Agent (Unified Communications Manager) PG CTI Server Outbound Option Dialer and SIP IOS Gateway | To increase the hard disk before you upgrade Agent PG, CTI Server and Outbound Option Dialer, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations You can have many PGs located on different virtual machines. You can upgrade each PG VMs by leveraging the capabilities of
                                                graceful shutdown feature. For more information about the graceful shutdown, see the Graceful Shutdown chapter in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |
| 10 | Peripherals | MR PG, VRU PG CRM connector | To increase the hard disk before you upgrade MR PG and VRU PG, refer the Expand Disk Space for Virtual Machines section in Upgrade Considerations You can have many PGs located on different virtual machines. You can upgrade each PG VMs by leveraging the capabilities of
                                                graceful shutdown feature. For more information about the graceful shutdown, see the Graceful Shutdown chapter in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |
| 11 | Call Processing | Cisco Unified Communications Manager (Unified Communications Manager) JTAPI on Agent (Unified Communications Manager) PG | If you upgrade to CUCM 12.5 on the servers, ensure that you deploy CUCM off-box. CUCM 12.5 on-box deployment are only supported for M5 servers. |

| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
|---|---|

| Note | For Live Data VM, you have to increase the RAM before upgrading. See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html |
|---|---|