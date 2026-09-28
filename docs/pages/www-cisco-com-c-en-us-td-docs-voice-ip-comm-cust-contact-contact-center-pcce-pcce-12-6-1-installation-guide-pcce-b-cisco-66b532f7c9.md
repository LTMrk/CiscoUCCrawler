---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-installation-guide-pcce-b-cisco-66b532f7c9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/installation/guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_6_1/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_chapter_01001.html
retrieved_at: 2026-08-21T16:40:19.349634+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Common Ground Upgrade Process

## Chapter: Common Ground Upgrade Process

# Common Ground Upgrade Process

## Upgrade Path

The supported upgrade paths to Packaged CCE 12.6(1) are as follows:

Packaged CCE 12.0(1) to Packaged CCE 12.5(1) followed by Packaged CCE 12.6(1). Use EDMT during this upgrade process.

Packaged CCE 12.5(1) to Packaged CCE 12.6(1), where 12.6(1) is a patch installer on 12.5(1) base installer. EDMT is not required
                                 during this upgrade process.

## Prerequisites and Important Considerations

After you begin the migration and upgrade process, you cannot back out of it. If you want to go back to the previous release,
                                 you must restore your VMs from your backup.

You can upgrade only to Cisco Packaged CCE 2000 Agents deployment, Release 12.0(1) from Release 11.5(x), or 11.6(x) directly.
                                 To upgrade from the releases 11.0(x), you must first upgrade to 11.5 and then upgrade to 12.0. To upgrade from releases earlier
                                 than 11.0(1), you must first upgrade to 11.0(1) and then upgrade to 11.5(1).

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

### NTP Configuration
                           	 Requirements

Packaged CCE relies on time synchronization.
                                 		  Properly configuring NTP is critical for reliability of reporting data and
                                 		  cross-component communication. It's important to implement the requirements
                                 		  outlined in NTP and Time Synchronization .

## Upgrade Considerations

### Update VM
                              		  Properties

Rather than re-create the VMs in the new version of the OVA, you can manually update the VM properties to match the new OVA.
                              Before you upgrade the CCE or Cloud Connect components, update the properties of each VM to match the appropriate OVA, as follows:

Stop the VM.

Update the properties of each VM to match the properties of the appropriate OVA. Check the Virtualization for Packaged Cisco Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html for descriptions of each OVA. Save your changes.

See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-cloud-connect.html for details on Cloud Connect.

Restart the VM.

Caution

Be careful when you upgrade the virtual machine network adapters. Done incorrectly, this upgrade can compromise the fault
                                          tolerance of your Cisco Contact Center.

For version-specific information on the VM properties in an OVA, Check the Virtualization for Packaged Cisco Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html for descriptions of each OVA.

### SQL Security
                              		  Hardening

You can optionally apply SQL security hardening when running the installer. If your company
                              				employs custom security policies, bypass this option. Most other deployments benefit
                              				from SQL security hardening.

During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, you should not
                                          					select SQL Server Security Hardening optional configuration as a part of the
                                          					installation. You can apply the SQL Security Hardening post installation using
                                          					the Security Wizard tool.

For more
                              		  information about SQL security hardening, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

### Self-signed Certificate for Unified CCE Web Application

As part of the upgrade of Unified CCE servers, self-signed certificates employed by Unified CCE web applications such as Unified
                                          CCE web administration tool and Websetup, may get regenerated. You must add the new certificates to the trust list on the
                                          appropriate end devices.

### Upgrade
                              		  Tools

During the upgrade
                              		  process, use the following tools as required:

ICM12.6.1.exe—The Unified CCE patch installer. It copies all files into relevant folders, updates the registries, and installs
                                    needed third-party software such as JRE, Apache Tomcat, and Microsoft .NET Framework.

Enhanced Database Migration Tool (EDMT)—A wizard application that is used for all upgrades to migrate the HDS, Logger, and
                                    BA databases during the upgrade process.

You can download the EDMT from Cisco.com by clicking Cisco Enhanced Data Migration Tool Software Releases .

The prerequisites for running EDMT are:

EDMT requires Microsoft® ODBC Driver 17 for SQL Server® and Visual C++ Redistributable for Visual Studio 2015 (or higher).
                                             The latest version of these packages can be downloaded from the Microsoft website. However, a copy of the same is also available
                                             in the Prerequisites folder of EDMT.

The EDMT displays status messages during the migration process, including warnings and errors. Warnings are displayed for
                                    informational purposes only and do not stop the migration. On the other hand, errors stop the migration process and leave
                                    the database in a corrupt state. If an error occurs, restore the database from your backup, fix the error, and run the tool
                                    again.

You can select either SQL Server Authentication or Windows Authentication during database migration. In certain scenarios, for example, where the source and destination machines are in different
                                                      domains, SQL Server Authentication can be used.

If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                                      SERVICE), you must run EDMT as an administrator.

The installer, not the EDMT, upgrades the AW database for the Administration & Data Server.

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

Disable configuration changes on the Unified CCE. Change the following registry key to 1:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\RouterA\Router\CurrentVersion\Configuration\Global\DBMaintenance

Reverse the Cisco IOS Enterprise Ingress Voice Gateway dial-peer priority configuration so that calls are sent to the Side
                                                B Unified CVP server.

Using Unified CCE Service Control , stop all Unified CCE services on the Unified CCE servers that you are upgrading, and set the startup type to Manual .

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

For details, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html

Upgrade the publishers/primary nodes of Cisco Unified Intelligence Center with Live Data and Identity Service (IdS).

For details, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Back up and export the Side A SQL database and the Outbound Option (if used) in Rogger VM.

Use Microsoft SQL Server Backup and Restore utilities for the back up.

Note the HDS customizable values.

Copy the backup files to a shared location.

Run the Enhanced Database Migration Tool on rogger, external HDS (if used), and non-external HDS to perform a schema upgrade
                                                during the upgrade process.

See Run EDMT .

If you use Outbound Option High Availablity, for the enhancements in Outbound Option High Availability to work effectively,
                                                disable Outbound Option High Availablity before the logger upgrade and then enable it after the upgrade. For details, see Disable Outbound Options High Availability (If Applicable)

Run the Unified CCE Release installer on the Side A Unified CCE Rogger.

See Install Cisco Unified Contact Center Enterprise .

Run the Unified CCE Release installer on the Side A Unified CCE AW-HDS-DDS.

See Install Cisco Unified Contact Center Enterprise .

Run the Unified CCE installer on the Side A PG.

See Install Cisco Unified Contact Center Enterprise .

(Optional) Upgrade the External HDS associated with Side A (if used)

Run the Unified CCE Release installer the External HDS associated with Side A.

See Install Cisco Unified Contact Center Enterprise .

(Optional) Upgrade ECE.

##### Side A Postupgrade Tasks

You must bring down Side B before you bring up Side A. Perform these tasks during maintenance window to cut over from Side
                                    B to Side A.

Task

Reverse the Cisco IOS Enterprise Ingress Voice Gateway dial-peer priority configuration so that calls are sent to the Side
                                                A Unified CVP server first and then to Side B.

Using Unified CCE Service Control, stop all Unified CCE services on the Side B Unified CCE servers that you are upgrading,
                                                and set the startup type to Manual .

Side B Unified CCE Rogger

Side B Unified CCE AW-HDS-DDS

Side B PG

External HDS with Side B as the Central Controller preferred side (if used)

Verify that the services have stopped.

Perform Database Performance Enhancement of TempDB, Logger Database, and AW-HDS Database. For more information, see Database Performance Enhancement .

Using Unified CCE Service Control, start all Unified CCE services on the Side A Unified CCE servers that you are upgrading,
                                                and set the startup type to Automatic .

Side A Unified CCE Rogger

Side A Unified CCE AW-HDS-DDS

Side A PG

External HDS with Side A as the Central Controller preferred side (if used)

Verify that the services have started.

Set the following registry key to 0 on Side A Unified CCE Rogger:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\RouterA\Router\CurrentVersion\Configuration\Global\DBMaintenance

Direct agents to sign into the Side A Finesse Primary node.

##### Preupgrade of Side B

Task

Disable configuration changes on the Side B Unified CCE Rogger. Change the following registry key to 1:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\RouterB\Router\CurrentVersion\Configuration\Global\DBMaintenance

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

For details, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html

Upgrade the subscribers/secondary nodes of Cisco Unified Intelligence Center with Live Data and Identity Service (IdS).

For details, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Back up and export the Side B SQL database and the Outbound Option (if used) database in the Rogger VM.

Use Microsoft SQL Server Backup and Restore utilities for the back up.

Note the HDS customizable values.

Copy the backup files to a shared location.

Run the Enhanced Database Migration Tool on rogger, external HDS (if used), and non-external HDS to perform a schema upgrade
                                                during the upgrade process.

See Run EDMT .

If you use Outbound Option High Availablity, for the enhancements in Outbound Option High Availability to work effectively,
                                                disable Outbound Option High Availablity before the logger upgrade and then enable it after the upgrade. For details, see Disable Outbound Options High Availability (If Applicable)

Run the Unified CCE installer on the Side B Unified CCE Rogger.

See Install Cisco Unified Contact Center Enterprise

Run the Unified CCE installer on the Side B Unified CCE AW-HDS-DDS.

See Install Cisco Unified Contact Center Enterprise

Run the Unified CCE installer on the Side B PG.

See Install Cisco Unified Contact Center Enterprise

(Optional) Upgrade the External HDS associated with Side B (if used)

See Install Cisco Unified Contact Center Enterprise

(Optional) Upgrade ECE.

##### Sync Side A to Side B

Perform these tasks during the third maintenance window to sync Side A and Side B.

Task

Set the following registry key to 0 on either the Side B Unified CCE Rogger:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\Router B\Router\CurrentVersion\Configuration\Global\DBMaintenance

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

If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG .

Side B

3

Upgrade the Side B CUCM Subscriber.

Important

The CUCM Publisher upgrade must be complete and the 12.5 software must be active before you upgrade the CUCM Subscriber.

4

Upgrade JTAPI on the Side B PG. See Upgrade Cisco JTAPI Client on PG .

Important

If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG .

###### Cisco Unified Communications Manager 12.5 - Steps After Upgrade

Perform the following tasks if Cisco Unified Communications Manager (CUCM) is on-box and if you have upgraded to CUCM 12.5
                                          and above on the Cisco UCS C240 M4SX server. This procedure is performed on the main site.

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

Run Stage 3 and Stage 4 upgrades in the same maintenance window.

Components of the same type within a particular stage of the upgrade sequence should
                                             be on the same application and operating system version before proceeding to the
                                             next stage in upgrade sequence.

Stage

Component Group

Components

Notes

1

Platform Orchestration, Hybrid Features

Cloud Connect

If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Considerations for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component.

If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Unified Customer Voice Portal (CVP) ( Reporting Server, Call Server/VXMLServer, Unified Call Studio)

You must upgrade all sites before proceeding to the next stage.

For more information, see Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see Stage 5 .)

IOS VXML Gateways

Cisco Virtualized Voice Browser

ECE

Cisco Finesse

Unified CCE Rogger

Admin & Data server (AW/HDS/DDS)

CUIC-LD-IDS

CUIC Reporting Templates

CCMP

After you upgrade AW, import the self-signed certificate of all solution components (if applicable) to all AWs.

After you upgrade Finesse to Release 12.6(x) , to load any gadgets to Finesse, you must first import all self-signed certificates (if applicable) to Finesse.

After upgrading cuic-ld-ids to 12.6, run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL.

For more information about Finesse, see Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

For more information about ECE, see https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

After you upgrade LD, you must import the Finesse certificate to LD.

Agent (Unified Communications Manager) PG

CTI Server

Outbound Option Dialer and SIP IOS Gateway

You can have many PGs located on different virtual machines. You can upgrade each PG virtual machine in its own maintenance
                                             window.

MR PG, VRU PG

CRM connector

You can have many PGs located on different virtual machines. You can upgrade each PG virtual machine in its own maintenance
                                             window.

Cisco Unified Communications Manager (Unified Communications Manager)

JTAPI on Agent (Unified Communications Manager) PG

You must install JTAPI client only when you upgrade to UCM 12.5.

If you upgrade to CUCM 12.5 on the M4 servers, ensure that you deploy CUCM off-box.

For more information, refer to Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html .

### Hardware Refresh with Common Ground Upgrade

Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html

After you configure the servers, you can move the VMs to the servers and complete the Common Ground Upgrade Process .

As a part of hardware refresh, if you are migrating from existing Cisco UCS C240 M3S/Cisco UCS C240 M4SX to Cisco UCS C240
                                 M5SX or Cisco UCS C240 M6SX or Cisco HX220c-M5SX or Cisco HX220c-M6S hardware, perform the following migration steps:

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

### Common Ground Upgrade Process

#### Multistage Upgrade Workflow

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

Platform Orchestration, Hybrid Features

Cloud Connect

If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Considerations for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component.

If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio)

You must upgrade all sites before proceeding to the next stage.

Before you upgrade to Unified CVP 12.6 , you must apply the latest ES of Packaged CCE 12.5 .

For more information, see Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see Stage 8 .)

IOS VXML Gateways

Cisco Virtualized Voice Browser

Identity Service

IdS Server

For IdS upgrade, see the procedure as documented in the Upgrades section of Unified Intelligence
                                                Center Installation and Upgrade Guide at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Agent and supervisor desktops

ECE

Cisco Finesse

After you upgrade Finesse to Release 12.6 , to load any
                                             gadgets to Finesse, you must first import all self-signed
                                             certificates (if applicable) to Finesse.

For more information about Finesse, see Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

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

After you upgrade AW, import the self-signed certificate of all solution components (if applicable) to all AWs.

After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

After you upgrade LD, you must import the Finesse certificate to LD.

For Live Data VM, you have to increase the RAM before upgrading.
                                                         See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html

Agent (Unified Communications Manager) PG

CTI Server

CTI OS Server

Outbound Option Dialer and SIP IOS Gateway

CTI OS Server is applicable only if Avaya PG is used.

You can have many PGs located on different virtual machines. You can upgrade each PG virtual machine in its own maintenance
                                                   window.

MR PG, VRU PG

CRM connector

You can have many PGs located on different virtual machines. You can upgrade each PG virtual machine in its own maintenance
                                             window.

Agent desktop client software

CTI OS (Agent/Supervisor Desktops)

CTI OS is applicable only if Avaya PG is used.

You can have many desktops located in many different sites. You can upgrade CTI OS desktops in multiple maintenance windows;
                                                   the later upgrade stages are not dependent on the completion of this stage.

Cisco Unified Communications Manager (Unified Communications Manager)

JTAPI on Agent (Unified Communications Manager) PG

You must install JTAPI client only when you upgrade to UCM 12.5.

If you upgrade to CUCM 12.5 on the M4 servers, ensure that you deploy CUCM off-box. CUCM 12.5 on-box deployment are only supported for M5 servers.

For more information, refer to Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html .

| Note | Use 12.5(x) EDMT to upgrade from Packaged CCE 12.0(1) to Packaged CCE 12.5(1). |
|---|---|

| Caution | Be careful when you upgrade the virtual machine network adapters. Done incorrectly, this upgrade can compromise the fault
                                          tolerance of your Cisco Contact Center. |
|---|---|

| Note | During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, you should not
                                          					select SQL Server Security Hardening optional configuration as a part of the
                                          					installation. You can apply the SQL Security Hardening post installation using
                                          					the Security Wizard tool. |
|---|---|

| Note | As part of the upgrade of Unified CCE servers, self-signed certificates employed by Unified CCE web applications such as Unified
                                          CCE web administration tool and Websetup, may get regenerated. You must add the new certificates to the trust list on the
                                          appropriate end devices. |
|---|---|

| Note | You can select either SQL Server Authentication or Windows Authentication during database migration. In certain scenarios, for example, where the source and destination machines are in different
                                                      domains, SQL Server Authentication can be used. If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                                      SERVICE), you must run EDMT as an administrator. The installer, not the EDMT, upgrades the AW database for the Administration & Data Server. |
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
| Disable configuration changes on the Unified CCE. Change the following registry key to 1: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\RouterA\Router\CurrentVersion\Configuration\Global\DBMaintenance |
| Reverse the Cisco IOS Enterprise Ingress Voice Gateway dial-peer priority configuration so that calls are sent to the Side
                                                B Unified CVP server. |
| Using Unified CCE Service Control , stop all Unified CCE services on the Unified CCE servers that you are upgrading, and set the startup type to Manual . Side A Unified CCE Rogger Side A Unified CCE AW-HDS-DDS Side A PG External HDS with Side A as the Central Controller preferred side (if used) Verify that the services are stopped. |

| Task |
|---|
| Upgrade to a supported version of ESXi version, if needed. For the supported ESXi versions for this release, see the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html . If you are using a supported ESXi version and want to upgrade to different supported ESXi version, you can upgrade now, or
                                                after the Packaged CCE upgrade is complete. See Upgrade VMware vSphere ESXi . |
| Upgrade Unified CVP Server. For more details, see the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . After upgrading the Unified CVP server, add the CVP machine to the domain. For more information, see Add Machine to Domain . |
| Upgrade all the Cisco Voice Gateways one after another. See Upgrade Cisco Voice Gateway IOS Version . The IOS version of the Cisco Voice Gateways must be upgraded to the minimum version required by Packaged CCE 12.0(1) . For more details, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html for IOS support information. |
| Upgrade all the Cisco Virtualized Voice Browsers one after another. For more details, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html . |
| Upgrade the publishers/primary nodes of Cisco Finesse. For details, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html |
| Upgrade the publishers/primary nodes of Cisco Unified Intelligence Center with Live Data and Identity Service (IdS). For details, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Back up and export the Side A SQL database and the Outbound Option (if used) in Rogger VM. Use Microsoft SQL Server Backup and Restore utilities for the back up. Note the HDS customizable values. Copy the backup files to a shared location. |
| Run the Enhanced Database Migration Tool on rogger, external HDS (if used), and non-external HDS to perform a schema upgrade
                                                during the upgrade process. See Run EDMT . |
| If you use Outbound Option High Availablity, for the enhancements in Outbound Option High Availability to work effectively,
                                                disable Outbound Option High Availablity before the logger upgrade and then enable it after the upgrade. For details, see Disable Outbound Options High Availability (If Applicable) |
| Run the Unified CCE Release installer on the Side A Unified CCE Rogger. See Install Cisco Unified Contact Center Enterprise . |
| Run the Unified CCE Release installer on the Side A Unified CCE AW-HDS-DDS. See Install Cisco Unified Contact Center Enterprise . |
| Run the Unified CCE installer on the Side A PG. See Install Cisco Unified Contact Center Enterprise . |
| (Optional) Upgrade the External HDS associated with Side A (if used) Run the Unified CCE Release installer the External HDS associated with Side A. See Install Cisco Unified Contact Center Enterprise . |
| (Optional) Upgrade ECE. See Enterprise Chat and Email Installation Guide (for Packaged Contact Center Enterprise) at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
|  |

| Task |
|---|
| Reverse the Cisco IOS Enterprise Ingress Voice Gateway dial-peer priority configuration so that calls are sent to the Side
                                                A Unified CVP server first and then to Side B. |
| (Optional) If you use Outbound Option High Availablity, enable Outbound Option High Availablity in the Web Setup tool. For
                                             details, see the Configure the Logger for Outbound Option topic in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html |
| Using Unified CCE Service Control, stop all Unified CCE services on the Side B Unified CCE servers that you are upgrading,
                                                and set the startup type to Manual . Side B Unified CCE Rogger Side B Unified CCE AW-HDS-DDS Side B PG External HDS with Side B as the Central Controller preferred side (if used) Verify that the services have stopped. |
| Perform Database Performance Enhancement of TempDB, Logger Database, and AW-HDS Database. For more information, see Database Performance Enhancement . |
| Using Unified CCE Service Control, start all Unified CCE services on the Side A Unified CCE servers that you are upgrading,
                                                and set the startup type to Automatic . Side A Unified CCE Rogger Side A Unified CCE AW-HDS-DDS Side A PG External HDS with Side A as the Central Controller preferred side (if used) Verify that the services have started. |
| Set the following registry key to 0 on Side A Unified CCE Rogger: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\RouterA\Router\CurrentVersion\Configuration\Global\DBMaintenance |
| Direct agents to sign into the Side A Finesse Primary node. |

| Task |
|---|
| Disable configuration changes on the Side B Unified CCE Rogger. Change the following registry key to 1: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\RouterB\Router\CurrentVersion\Configuration\Global\DBMaintenance |

| Task |
|---|
| Upgrade to a supported version of ESXi version, if needed. For the supported ESXi versions for this release, see the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html . If you are using a supported ESXi version and want to upgrade to different supported ESXi version, you can upgrade now, or
                                                after the Packaged CCE upgrade is complete. See Upgrade VMware vSphere ESXi . |
| Upgrade the Unified CVP Reporting Server See Upgrade Unified CVP Reporting Server After upgrading the Unified CVP Reporting server, add the CVP Reporting server to the domain. For more information, see Add Machine to Domain . |
| Upgrade Unified CVP Server. For more details, see the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . After upgrading the Unified CVP server, add the CVP machine to the domain. For more information, see Add Machine to Domain . |
| Upgrade the subscribers/secondary nodes of Cisco Finesse. For details, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html |
| Upgrade the subscribers/secondary nodes of Cisco Unified Intelligence Center with Live Data and Identity Service (IdS). For details, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Back up and export the Side B SQL database and the Outbound Option (if used) database in the Rogger VM. Use Microsoft SQL Server Backup and Restore utilities for the back up. Note the HDS customizable values. Copy the backup files to a shared location. |
| Run the Enhanced Database Migration Tool on rogger, external HDS (if used), and non-external HDS to perform a schema upgrade
                                                during the upgrade process. See Run EDMT . |
| If you use Outbound Option High Availablity, for the enhancements in Outbound Option High Availability to work effectively,
                                                disable Outbound Option High Availablity before the logger upgrade and then enable it after the upgrade. For details, see Disable Outbound Options High Availability (If Applicable) |
| Run the Unified CCE installer on the Side B Unified CCE Rogger. See Install Cisco Unified Contact Center Enterprise |
| Run the Unified CCE installer on the Side B Unified CCE AW-HDS-DDS. See Install Cisco Unified Contact Center Enterprise |
| Run the Unified CCE installer on the Side B PG. See Install Cisco Unified Contact Center Enterprise |
| (Optional) Upgrade the External HDS associated with Side B (if used) See Install Cisco Unified Contact Center Enterprise |
| (Optional) Upgrade ECE. See Enterprise Chat and Email Installation Guide (for Packaged Contact Center Enterprise) at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html . |
|  |

| Task |
|---|
| Set the following registry key to 0 on either the Side B Unified CCE Rogger: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\Router B\Router\CurrentVersion\Configuration\Global\DBMaintenance |
| (Optional) If you use Outbound Option High Availability, enable Outbound Option High Availability in the Web Setup tool. For
                                             details, see the Configure the Logger for Outbound Option topic in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html |
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
| 2 | Upgrade JTAPI on the Side A PG. See Upgrade Cisco JTAPI Client on PG . Important If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG . | Important | If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG . |
| Important | If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG . |
| Side B |
| 3 | Upgrade the Side B CUCM Subscriber. For detailed upgrade steps, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html . Important The CUCM Publisher upgrade must be complete and the 12.5 software must be active before you upgrade the CUCM Subscriber. | Important | The CUCM Publisher upgrade must be complete and the 12.5 software must be active before you upgrade the CUCM Subscriber. |
| Important | The CUCM Publisher upgrade must be complete and the 12.5 software must be active before you upgrade the CUCM Subscriber. |
| 4 | Upgrade JTAPI on the Side B PG. See Upgrade Cisco JTAPI Client on PG . Important If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG . | Important | If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG . |
| Important | If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. For
                                                            more information, see Install Cisco JTAPI Client on PG . |

| Important | If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. See Install Cisco JTAPI Client on PG . |
|---|---|

| Important | The CUCM Publisher upgrade must be complete and the 12.5 software must be active before you upgrade the CUCM Subscriber. |
|---|---|

| Important | If you are installing CUCM 12.5 and above, download the Cisco
                                                            JTAPI Client from CUCM and install it on the PG machine. For
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

| Note | Upgrade Agent Desktop, CUIC, Live Data, and IdS server along with the Unified CCE Central Controller upgrade. After upgrading Finesse, IdS, and CUIC, import the IdS certificates to the Finesse and CUIC servers. Run Stage 3 and Stage 4 upgrades in the same maintenance window. |
|---|---|

| Note | Components of the same type within a particular stage of the upgrade sequence should
                                             be on the same application and operating system version before proceeding to the
                                             next stage in upgrade sequence. |
|---|---|

| Stage | Component Group | Components | Notes |
|---|---|---|---|
| 1 | Platform Orchestration, Hybrid Features | Cloud Connect | If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Considerations for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component. If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| 2 | Queuing and self-service | Cisco Unified Customer Voice Portal (CVP) ( Reporting Server, Call Server/VXMLServer, Unified Call Studio) | You must upgrade all sites before proceeding to the next stage. For more information, see Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . |
| 3 | Gateways | IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see Stage 5 .) IOS VXML Gateways Cisco Virtualized Voice Browser |  |
| 4 | Agent/Supervisor Desktop, Central Controller, and Reporting | ECE Cisco Finesse Unified CCE Rogger Admin & Data server (AW/HDS/DDS) CUIC-LD-IDS CUIC Reporting Templates CCMP | After you upgrade AW, import the self-signed certificate of all solution components (if applicable) to all AWs. After you upgrade Finesse to Release 12.6(x) , to load any gadgets to Finesse, you must first import all self-signed certificates (if applicable) to Finesse. Note After upgrading cuic-ld-ids to 12.6, run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL. For more information about Finesse, see Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . For more information about ECE, see https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade LD, you must import the Finesse certificate to LD. | Note | After upgrading cuic-ld-ids to 12.6, run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL. |
| Note | After upgrading cuic-ld-ids to 12.6, run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL. |
| 5 | Peripherals | Agent (Unified Communications Manager) PG CTI Server Outbound Option Dialer and SIP IOS Gateway | You can have many PGs located on different virtual machines. You can upgrade each PG virtual machine in its own maintenance
                                             window. |
| 6 | Peripherals | MR PG, VRU PG CRM connector | You can have many PGs located on different virtual machines. You can upgrade each PG virtual machine in its own maintenance
                                             window. |
| 7 | Call Processing | Cisco Unified Communications Manager (Unified Communications Manager) JTAPI on Agent (Unified Communications Manager) PG | You must install JTAPI client only when you upgrade to UCM 12.5. If you upgrade to CUCM 12.5 on the M4 servers, ensure that you deploy CUCM off-box. For more information, refer to Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html . |

| Note | After upgrading cuic-ld-ids to 12.6, run the utils finesse layout updateCuicGadgetUrl command to update the gadget URL. |
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
| 1 | Platform Orchestration, Hybrid Features | Cloud Connect | If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Considerations for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component. If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| 2 | Queuing and self-service | Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio) | You must upgrade all sites before proceeding to the next stage. Before you upgrade to Unified CVP 12.6 , you must apply the latest ES of Packaged CCE 12.5 . For more information, see Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . |
| 3 | Gateways | IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see Stage 8 .) IOS VXML Gateways Cisco Virtualized Voice Browser |  |
| 4 | Identity Service | IdS Server | For IdS upgrade, see the procedure as documented in the Upgrades section of Unified Intelligence
                                                Center Installation and Upgrade Guide at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| 5 | Agent and supervisor desktops | ECE Cisco Finesse | After you upgrade Finesse to Release 12.6 , to load any
                                             gadgets to Finesse, you must first import all self-signed
                                             certificates (if applicable) to Finesse. For more information about Finesse, see Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . For more information about ECE, see https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| 6 | Reporting server | CUIC server | After you upgrade Cisco Unified Intelligence Center (CUIC), you must: Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname. Import LD and Finesse certificates to CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . |
| 7 | Central Controller | Unified CCE Rogger Admin & Data server (AW/HDS/DDS) Standalone Live Data CUIC Reporting Templates Administration Client | After you upgrade AW, import the self-signed certificate of all solution components (if applicable) to all AWs. After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade LD, you must import the Finesse certificate to LD. Note For Live Data VM, you have to increase the RAM before upgrading.
                                                         See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html | Note | For Live Data VM, you have to increase the RAM before upgrading.
                                                         See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html |
| Note | For Live Data VM, you have to increase the RAM before upgrading.
                                                         See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html |
| 8 | Peripherals | Agent (Unified Communications Manager) PG CTI Server CTI OS Server Outbound Option Dialer and SIP IOS Gateway | CTI OS Server is applicable only if Avaya PG is used. You can have many PGs located on different virtual machines. You can upgrade each PG virtual machine in its own maintenance
                                                   window. |
| 9 | Peripherals | MR PG, VRU PG CRM connector | You can have many PGs located on different virtual machines. You can upgrade each PG virtual machine in its own maintenance
                                             window. |
| 10 | Agent desktop client software | CTI OS (Agent/Supervisor Desktops) | CTI OS is applicable only if Avaya PG is used. You can have many desktops located in many different sites. You can upgrade CTI OS desktops in multiple maintenance windows;
                                                   the later upgrade stages are not dependent on the completion of this stage. |
| 11 | Call Processing | Cisco Unified Communications Manager (Unified Communications Manager) JTAPI on Agent (Unified Communications Manager) PG | You must install JTAPI client only when you upgrade to UCM 12.5. If you upgrade to CUCM 12.5 on the M4 servers, ensure that you deploy CUCM off-box. CUCM 12.5 on-box deployment are only supported for M5 servers. For more information, refer to Virtualization for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html . |

| Note | For Live Data VM, you have to increase the RAM before upgrading.
                                                         See https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html |
|---|---|