---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-547c2f33e2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_150_install_upgrade_guide/common_ground_upgrade.html
retrieved_at: 2026-08-16T19:56:55.501912+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Common Ground Upgrade

## Chapter: Common Ground Upgrade

# Common Ground Upgrade

## Preupgrade
                        	 Overview

The preupgrade process ensures that your systems have the necessary software to support your
                           			contact center. These tasks prepare the way for a successful upgrade of your Cisco
                           			contact center components to the new release.

The Common Ground upgrade process checks that your system is compatible with the latest updates and features. If the installer
                                       detects any unsupported features during the upgrade, it will exit the process and provide an error message specifying which
                                       components have unsupported configurations. Once these unsupported configurations are removed, you can attempt the Common
                                       Ground upgrade again. For more information about the list of unsupported features, see the Removed and Unsupported Features topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html

If you need to upgrade from version 12.6(2) to 15.0(1) and leverage the capabilities of graceful shutdown, you must install
                                       any one of the required corresponding Unified CCE component's ES release as mentioned below:

For Unified CCE Router Graceful Shutdown, install 12.6(2) ES68 or later.

For Unified CCE PG Graceful Shutdown, install 12.6(2) ES69 or later.

For Unified CCE AW Graceful Shutdown, install 12.6(2) ES70 or later.

For more information about the graceful shutdown, see the Graceful Shutdown chapter in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

### Upgrade Tools

During the preupgrade process, use the following tools as required:

User Migration Tool—A standalone Windows command-line application that is used for all upgrades that involve a change of domain.
                                    The tool exports all existing user accounts (config/setup and supervisors) from the source domain to a .bin file. The file is used in the target domain during the upgrade.

You can download the User Migration Tool from Cisco.com by clicking ICM User Migration Tool Software .

Regutil Tool—Used in Technology Refresh upgrades, exports the Cisco Systems, Inc. registry from the source machine during
                                    the preupgrade process. The output of the tool is required on the destination machine when running the Unified CCE Installer
                                    during the upgrade process.

You can download the Regutil Tool from Cisco.com by clicking Contact Center Enterprise Tools .

Domain Manager—Used to provision Active Directory.

The Domain Manager Tool is delivered with the main installer.

Upgrade.exe—Used to upgrade the schema of the logger, AW DB, HDS DB, and BA databases to a version compatible with the current
                                    Unified CCE Software version. It is typically used when the installer fails to automatically upgrade the schema of the AW
                                    database. The other databases are typically upgraded using EDMT and not the installer.

Perform the following steps to use the tool:

<ICM install directory>:\icm\bin>upgrade.exe -s <Server Name> -d <Database name> -dt <Database Type> -i <Instance Name>

Where

<Database Type> - can be either " logger " or " hds " or " aw " or " ba ", depending on the database that requires the schema to be upgraded.

Enhanced Database Migration Tool (EDMT)—A wizard application that is used for all upgrades to migrate the HDS, Logger, and
                                    BA databases during the upgrade process.

You can download the EDMT from Cisco.com by clicking Cisco Enhanced Data Migration Tool Software Releases .

The prerequisites for running EDMT are:

EDMT requires Microsoft® ODBC Driver 17.10 or later minor version of ODBC 17 for SQL Server® and Visual C++ Redistributable
                                    for Visual Studio 2015 (or higher). The latest version of these packages can be downloaded from the Microsoft website. However,
                                    a copy of the same is also available in the Prerequisites folder of EDMT.

The EDMT displays status messages during the migration process, including warnings and errors. Warnings are displayed for
                                    informational purposes only and do not stop the migration. Errors stop the migration process and leave the database in a corrupt
                                    state. If an error occurs, restore the database from your backup, fix the error, and run the tool again.

If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                                      SERVICE), you must run EDMT as an administrator.

The installer, not the EDMT, upgrades the AW database for the Administration & Data Server.

## Common Ground
                        	 Preupgrade Task Flow

Perform the
                              		  following Common Ground preupgrade tasks in any order.

The Common Ground upgrade assumes the host server runs on Windows Server.

Task

See

Review target Release Notes

ESXi Supportability

Virtual Machine Snapshot for Unified CCE Component Virtual Machines

Download the Enhanced Database Migration Tool

Notify all stakeholders, including:

Cisco Technical Assistance Center (TAC)

Local Cisco Representatives

Customer Operations and Emergency Management Center

Third-party vendors as applicable

## Common Ground Preupgrade Tasks

### Virtual Machine Snapshot for Unified CCE Component Virtual Machines

Uninstallation of Unified CCE 15.0(1) installed on server machines using the ICM-CCE-Installer ISO is not supported.

To revert to the previous versions that existed before you did a Common Ground in-place upgrade of installations to Unified
                                 CCE 15.0(1), perform one of the following tasks:

Step 1

Take a Virtual Machine Snapshot in the powered off state before the upgrade.

Step 2

Clone the Virtual Machine before the upgrade.

#### What to do next

Delete these snapshots or clones after the upgrades are successfully completed. Such deletions will prevent performance issues.

Uninstallation and re-installation of other packages like Administration Client and Internet Script Editor (ISE) will continue
                                 to be supported.

### VM Hardware Version Upgrade

Perform the following procedure to upgrade the hardware version of the virtual machine (VM).

#### Before you begin

Step 1

Launch the vSphere Web Client using the browser.

Step 2

Log in to your vCenter Server.

Step 3

Right-click on the VM that needs to be upgraded, and select Compatibility > Upgrade VM Compatibility from the menu.

Step 4

In the Compatible with field, select ESXi 7.0 U1 and later and click OK .

For all components, the supported VMware ESXi version is 7.0 U1 or later. Choosing ESXi 7.0 U1 and later will automatically set the VM hardware version to 18 .

Selecting a ESXi version is irreversible. For example, if you set it to ESXi 7.0 U1 and later , you can only upgrade; downgrading to a previous ESXi version will not be possible.

For more virtualization details, see Virtualization Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html

Step 5

Right-click the VM and select Edit Settings .

Step 6

Click the VM Options tab and expand General Options .

Step 7

Select the Guest OS as follows and then click OK .

For Unified CCE components and Unified CVP, you must select:

Guest OS Family —Windows

Guest OS Version — For Unified ICM and Unified CVP, choose Microsoft Windows Server 2019 (64-bit) or Microsoft Windows Server 2022 (64-bit).

For Unified Intelligence Center, Finesse, Cisco VVB, and Cloud Connect, you must select:

Guest OS Family —Linux

Guest OS Version —Other 4.x or later Linux (64-bit)

For ECE, you must select:

Guest OS Family —Windows

Guest OS Version — Microsoft Windows Server 2022 (64-bit).

Step 8

Power on the VM.

## Prerequisite for In-Place Windows OS Upgrade

Before you start an in-place upgrade of the Windows Operating System to Windows Server version 2022, do the following:

To stop all Unified CCE services on the Unified CCE servers that you're upgrading, you must invoke maintenance mode using
                                    the maintenance mode command.

For more information about the maintenance mode command, see the Invoking Maintenance Mode topic in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

Set the startup type of all Unified CCE services to Manual .

Close any open ICM applications.

Run the following command to manually delete the registry hive link created by Unified CCE 12.5(2) or 12.6(x) between 32-bit
                                    and 64-bit registry hive:

<installDrive>\icm\bin\RegUtil.exe -link -delete

Ensure to run the RegUtil tool with administrative privileges.

## Common Ground Upgrade Task Flow

For the Unified CCE core components, there is a general flow for redundant systems to ensure that Cisco Contact Center operation
                              continues during the entire upgrade process. Sides A and B are brought down, upgraded, tested, and brought back up in a sequence
                              that ensures continuous operation of the Cisco Contact Center.

For coresident configurations, upgrade CUIC/LiveData/IdS server along with the Unified CCE Central Controller upgrade.

For Common Ground upgrades, perform the following upgrade tasks:

Task

See

(Optional) Install Cisco Reverse Proxy

If you don't have Cisco Reverse Proxy in your environment and you want to use VPN-less desktop access feature or to upgrade
                                       Cisco Reverse Proxy 12.6(2) to 15.0(1), you must install Cisco Reverse Proxy 15.0(1). Refer to the Notes on VM Templates for 15.0(1) topic in the Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS page for the installer location. For more information on how to install Cisco Reverse Proxy, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) .

Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments.

Install Cloud Connect

Install Cloud Connect

If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Overview for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component.

Upgrade both the publisher and subscriber. For Cloud Connect upgrade instructions, see the Upgrade Cloud Connect section.

If you don’t have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                       Connect. For fresh install instructions, see the Install Cloud Connect section.

Check the disk size by running the command show hardware in the Cloud Connect admin console. SDA1 and SDA2 should be at least 44 GB. If not, contact Cisco TAC team for support.

Queuing and self-service components

Installation and Upgrade
                                                				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html

Installation and Upgrade Guide for Cisco Virtualized Voice Browser at

https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html

Identity Service (IdS)/Single Sign-On(SSO)

SSO is an optional feature and exchanges authentication and authorization details between an identity provider (IdP) and an
                                       identity service (IdS).

For more information, see Upgrade Flowcharts .

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Upgrade Enterprise Chat and Email (ECE)

For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

Upgrade Finesse

For more information, see Cisco Finesse Installation and Upgrade Guide Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

When upgrading from Cisco Finesse 12.6(2) to 15.0(1), Unified Intelligence Center gadgets won't load. To resolve this, Upgrade
                                       Unified Intelligence Center to either 12.6(2) ES 04 or to 15.0(1).

Installation and Upgrade Guide for Cisco Unified Intelligence Center at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

If you want to leverage the capabilities of graceful shutdown to bring down the Unified CCE services, use the maintenance
                                                   mode command. For more information, see the Invoking Maintenance Mode topic in the AdministrationGuide for Cisco Unified Contact Center Enterprise at the https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html

Bring down Side A Logger, and upgrade the VM to the new platform of Windows Server and SQL Server.

If you want to leverage the capabilities of graceful shutdown to bring down  Side A Logger, use the maintenance mode command
                                                   to invoke  maintenance mode.

Upgrade Windows Server

Upgrade SQL Server

Migrate Unified CCE Logger Database and Upgrade Logger

Bring down Side A Call Router, and upgrade the VM to new platform of Windows Server.

If you want to leverage the capabilities of graceful shutdown to bring down  Side A Call Router, use  the maintenance mode
                                                   command to invoke  maintenance mode.

Upgrade Windows Server

Upgrade Side A Call Router.

Upgrade Unified CCE Call Router

Upgrade the VM for the Administration & Data Server connected to Side A to the new platform of Windows Server and SQL Server.

Upgrade Windows Server

Upgrade SQL Server

Upgrade the Administration & Data Server connected to Side A.

Bring Side A Logger and Call Router into service, bring down Side B Logger and Call Router.

Upgrade the VM for the Side B Logger to the new platform of Windows Server and SQL Server.

Upgrade Windows Server

Upgrade SQL Server

Migrate Side B Logger database and upgrade the Logger.

Migrate Unified CCE Logger Database and Upgrade Logger

Upgrade the VM for the Side B Call Router to new platform of Windows Server.

Upgrade Windows Server

Upgrade Side B Call Router.

Bring Side B Call Router into service and verify operation. Bring Side B Logger into service and verify operation.

Upgrade the VM for the Administration & Data Server connected to Side B to the new platform of Windows Server and SQL Server.

Upgrade Windows Server

Upgrade SQL Server

Upgrade the Administration & Data Server connected to Side B.

Import Reports section in Cisco Unified Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html

Installation and
                                                				  Configuration Guide for Cisco Unified Contact Center Management
                                                				  Portal at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/products-installation-guides-list.html

Upgrade Administration Client.

Upgrade Unified CCE Administration Client

For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html

Bring down Side A PG and Outbound Dialer

If you want to leverage the capabilities of graceful shutdown to bring down Side A PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode.

Upgrade Peripheral Gateways

Upgrade Outbound Option Dialer

Upgrade Windows Server

Bring up Side A PG and Outbound Dialer to service.

Upgrade Peripheral Gateways

Upgrade Outbound Option Dialer

Bring down Side B PG and Outbound Dialer.

If you want to leverage the capabilities of graceful shutdown to bring down Side B PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode.

Upgrade Side B VM for the PG to the new Platform of Windows Server.

Upgrade PGs on Side B.

Upgrade Side B Outbound Option Dialer.

Bring up Side B PG and outbound dialer services .

Upgrade Customer Collaboration Platform

Cisco Customer Collaboration Platform User Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html .

Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/ unified-communications-manager-callmanager/ products-installation-guides-list.html

## Common Ground  Upgrade Tasks

The following section provides instructions about upgrading the virtual environment and the Unified CCE components. For instructions
                              about upgrading non-Unified CCE components in a Unified CCE solution, for example Finesse and CUIC, see the links to component-specific
                              documents in the Common Ground Upgrade Task Flow .

### Upgrade Windows Server

Follow these steps to change the guest operating system to Microsoft Windows Server 2022 (64 bit):

#### Before you begin

Use the maintenance mode command to invoke maintenance mode and bring down all the Unified CCE services on the Unified CCE
                                       servers that you are upgrading. Now set the startup type of all Unified CCE services as Manual . For more information about the maintenance mode command, see the Invoking Maintenance Mode topic in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

To perform an in-place upgrade to Windows Server 2022, select the Windows Server 2022 (Desktop Experience) option and then select Keep personal files and apps option. For more information, see the Microsoft documentation at https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview . After performing an in-place upgrade to Windows Server 2022, make sure to install the latest Windows updates.

Ensure that the virtual machine has enough space before the upgrade. Operating System upgrade to Windows Server 2022 requires
                                       minimum 32 GB of free space in the primary hard disk. If the virtual machine is a Logger/Distributor machine, the upgrade
                                       to SQL Server 2022 Standard or Enterprise edition requires an additional 6 GB of free space. For more information, see Hardware
                                       requirements for Windows Server at https://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html .

Step 1

Power off the VM.

Step 2

Right-click the VM and select Edit Settings .

Step 3

Click the VM Options tab and expand General Options .

Step 4

From the Guest OS drop-down menu, select the guest operating system family.

Step 5

From the Guest OS Version drop-down menu, select Microsoft Windows Server 2022 (64 bit) .

To be able to select the Microsoft Windows Server 2022 (64 bit) guest operating system, you must set the VM hardware compatibility to ESXi 7.0 U1 and later.

Step 6

Click OK .

#### What to do next

If your Windows Server supports the Multilingual language pack, it will be uninstalled during in-place Windows Server upgrade.
                                 You must install the language pack manually post Windows Server in-place upgrade. For more information on installing language
                                 pack, see the Microsoft Device Partner Center documentation.

### Upgrade SQL Server

#### Before you begin

Upgrading SQL Server requires a minimum of 6 GB of free hard disk space. Ensure that the virtual machine has the required
                                       free space before you begin the upgrade.

For VMs with SQL Server Enterprise, in-place upgrade only to the Enterprise version is supported. For VMs with SQL Standard
                                       Edition, either in-place upgrade to SQL Server Standard Edition or SQL Enterprise Edition is supported. For more information,
                                       see Microsoft SQL Server 2022 documentation.

Remove Microsoft SQL Server 2022 Unsupported features before upgrading SQL Server.

The steps to select features for Microsoft SQL Server 2022 are as follows:

Navigate to the Control Panel and select Programs and Features .

Right-click on Microsoft SQL Server (Version) (Bit) and select the Uninstall option.

Click Remove on the SQL Server dialog box to initiate the Microsoft SQL Server installation wizard.

On the Select Instance page, choose an SQL Server instance to remove from the drop-down menu. Then, click Next to continue.

On the Select Features page, select all the features except the following:

Database Engine Services

Client Tools Connectivity

Client Tools SDK

SQL Client Connectivity SDK

If you are installing Microsoft SQL Server 2022, select only Database Engine Services.

On the Ready to Remove page, check the components and features set for uninstallation. Click Remove to start the process.

Microsoft supports in-place upgrade of the Windows Operating System and the SQL Server. After you upgrade the operating system,
                                       upgrade SQL Server.

Remove any previous versions of ODBC 17 if they are installed on a different drive from SQL Server. If both are on the same
                                       drive, no removal is needed.

Step 1

Launch the SQL Server installer and refer to the Microsoft documentation for any necessary guidance.

Step 2

Follow the wizard steps. Choose the default or correct instance for your deployment.

Step 3

After upgrading SQL Server, install the latest SQL cumulative update.

#### What to do next

If the Database Engine Services fail during a Microsoft SQL Server upgrade, open the SQL Server Installer , choose Maintenance , and perform the edition upgrade to complete the installation. For more information, see the Upgrade SQL Server topic in Microsoft documentation.

Microsoft SQL Server does not contain SQL Server Management Studio in the default toolkit.

Re-run the SQL Server setup to install Management Studio by navigating to the SQL Selection Center > Installation > Install SQL Server Management Tools . If your computer has no internet connection, download and install the SQL server Management Studio manually.

When connecting to SQL Server through the latest version of SQL Server Management Studio (SSMS), it's important to note that the default option for encryption and the Trust Server Certificate feature are not supported by CCE, as outlined in the Contact Center Enterprise Solution Compatibility Matrix . To ensure a successful connection, be sure to select the optional encryption setting and refrain from checking the Trust Server Certificate check box.

### Migrate Unified CCE Logger Database and Upgrade Logger

To upgrade the Logger, you do the following tasks:

Migrate the Logger database.

If you use Outbound Option High Availability, do the following:

Migrate the Outbound Option database.

Install the new software.

Step 1

Use the maintenance mode command to invoke maintenance mode and bring down all the Unified CCE services on the Unified CCE
                                             servers that you are upgrading. Now set the startup type of all Unified CCE services as Manual .

For more information, see the Invoking Maintainence Mode topic in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

Step 2

Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the Logger system, prior to launching EDMT. These include
                                          the ODBC Driver 17.10 or later minor versions of ODBC 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2022.

Step 3

Launch the EDMT and click Next .

Step 4

Select Common Ground , and click Next .

Step 5

On the warning message, click Yes if you have taken a backup of your database, and no services are currently running.

If you have not taken the backup of your database, click No to exit the installer.

Step 6

In the Database Connection section, highlight the database that you want to upgrade, and then click Next .

Step 7

Click Start Migration . A warning message is displayed asking for confirmation of the data migration.

Step 8

Click Yes to confirm.

Step 9

Click OK to acknowledge the message. After completion of the data migration, a warning message is displayed asking you to select a
                                          valid deployment type.

This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration.

Step 10

Exit the EDMT.

Step 11

(Optional) If Outbound Option High Availability is deployed, repeat steps 1 through 12 to migrate the BA database.

If you are upgrading Logger from 12.6(x), you don't need to upgrade the BA database.

Step 12

To upgrade the Logger, launch the ICM-CCE-Installer, and click Next .

Step 13

(Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 14

(Optional) Select SQL Server Security Hardening and click Next .

Step 15

Click OK on any informational messages that display.

Step 16

Click Install .

Step 17

Reboot the server when the upgrade completes.

### Upgrade Unified  CCE Call Router

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

(Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 3

Click OK on any informational messages that display.

Step 4

Click Install .

Step 5

Reboot the
                                          			 server when the upgrade completes.

### Migrate HDS Database and Upgrade Unified CCE Administration & Data Server

The deployment of the Administration & Database Server determines which tools to use for an upgrade:

For an AW-only deployment, the EDMT is not required; the ICM-CCE-Installer completes the upgrade.

For any
                                       				deployment that involves an HDS database, use the EDMT to migrate the HDS
                                       				database before running the installer.

Step 1

Use the maintenance mode command to invoke maintenance mode and bring down all the Unified CCE services on the Unified CCE
                                             servers that you are upgrading. Now set the startup type of all Unified CCE services as Manual .

For more information, see the Invoking Maintainence Mode topic in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

Step 2

For HDS-related deployments. Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the Administration & Database Server system, before launching
                                          EDMT. These include the ODBC Driver 17.10 or later minor versions of ODBC 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2022.

For more information about EDMT, see Preupgrade Overview .

Step 3

Launch the EDMT and click Next . Select Common Ground and click Next . Review or change the information that is displayed as required and click Start Migration . Click Yes on the warning message that displays. Exit the EDMT.

The warning message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data migration.

Step 4

Launch the ICM-CCE-Installer and click Next .

Step 5

(Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 6

(Optional) Select SQL Server Security Hardening and click Next .

Step 7

Click OK on any informational messages that display.

Step 8

Click Install .

Step 9

Reboot the server when the upgrade completes.

For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine .

### Upgrade Unified CCE Administration Client

Step 1

Launch the  AdminClientInstaller and click Next .

Step 2

(Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 3

Click OK on any informational messages that display.

Step 4

Click Install .

Step 5

Reboot the server when the upgrade completes.

For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine .

### Upgrade Peripheral
                           	 Gateways

You can upgrade
                                 		  different Peripheral Gateways (PGs) within a contact center within different
                                 		  maintenance windows. However, upgrade all PGs that reside on the same virtual
                                 		  machine and their redundant PGs (Side A and then the corresponding Side B; or
                                 		  vice-versa) during the same maintenance window.

The following dependencies occur when upgrading the Unified Communications Manager PG:

If your
                                       				contact center uses Outbound Option, upgrade any Outbound Option Dialers that
                                       				are associated with Unified Communications Manager PGs at the same time.

When you upgrade the Unified Communications Manager application, upgrade the JTAPI client that is associated with the Unified
                                       Communications Manager PG at the same time.

When the CTI server that is associated with the PG gets upgraded, the CTI server connection mode is set to the Mixed mode
                                 by default. The Mixed mode enables both Secured and Non-Secured mode of connection. For the Secured mode of connection, a
                                 new port is selected based on the port selection logic. For more information on Port Utilization, see the Port Utilization Guide for Cisco Unified Contact Center Solutions . If the port that is selected by default conflicts with the existing ports, then you need to either release the default port
                                 or change the Secured mode port to an available port after the upgrade.

VRU PG uses an existing maintenance mode from Unified CVP.

Ensure you stop all the existing calls gracefully on the VRU PG by initiating the maintenance mode in Unified CVP to which
                                             the VRU PG is connected. For more information about maintenance mode in Unified CVP, see the Shut Down Server topic in Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

You must use the maintenance mode command to invoke maintenance mode in all PGs that reside on the same virtual machine. For
                                             more information, see the Invoking Maintenace Mode topic in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

(Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 3

Click OK on any informational messages that display.

Step 4

Click Install .

Step 5

Reboot the server when the upgrade completes.

Step 6

For the Agent PG, run the CceCrypTool to encrypt the JTAPI password.

To run CceCrypTool, open command prompt in administrator mode and run the following command:

For example:

CceCrypTool /instance ucce /component PG1A /proc jgw1 /mode encrypt

### Upgrade Outbound Option Dialer

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

(Optional)To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 3

Click OK on any informational messages that display.

Step 4

Click Install .

Step 5

Reboot the server when the upgrade completes.

Step 6

Use Unified CCE Service Control to set all Unified CCE services to Automatic Start.

| Note | The Common Ground upgrade process checks that your system is compatible with the latest updates and features. If the installer
                                       detects any unsupported features during the upgrade, it will exit the process and provide an error message specifying which
                                       components have unsupported configurations. Once these unsupported configurations are removed, you can attempt the Common
                                       Ground upgrade again. For more information about the list of unsupported features, see the Removed and Unsupported Features topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html |
|---|---|

| Note | If you need to upgrade from version 12.6(2) to 15.0(1) and leverage the capabilities of graceful shutdown, you must install
                                       any one of the required corresponding Unified CCE component's ES release as mentioned below: For Unified CCE Router Graceful Shutdown, install 12.6(2) ES68 or later. For Unified CCE PG Graceful Shutdown, install 12.6(2) ES69 or later. For Unified CCE AW Graceful Shutdown, install 12.6(2) ES70 or later. For more information about the graceful shutdown, see the Graceful Shutdown chapter in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|

| Note | If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                                      SERVICE), you must run EDMT as an administrator. The installer, not the EDMT, upgrades the AW database for the Administration & Data Server. |
|---|---|

| Note | The Common Ground upgrade assumes the host server runs on Windows Server. |
|---|---|

| Task | See |
|---|---|
| Review target Release Notes | Release Notes for Cisco Unified Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html |
| ESXi Supportability | ESXi Supportability |
| Virtual Machine Snapshot for Unified CCE Component Virtual Machines | Virtual Machine Snapshot for Unified CCE Component Virtual Machines |
| Download the Enhanced Database Migration Tool | Upgrade Overview |
| Notify all stakeholders, including: Cisco Technical Assistance Center (TAC) Local Cisco Representatives Customer Operations and Emergency Management Center Third-party vendors as applicable |

| Step 1 | Take a Virtual Machine Snapshot in the powered off state before the upgrade. |
|---|---|
| Step 2 | Clone the Virtual Machine before the upgrade. |

| Step 1 | Launch the vSphere Web Client using the browser. |
|---|---|
| Step 2 | Log in to your vCenter Server. |
| Step 3 | Right-click on the VM that needs to be upgraded, and select Compatibility > Upgrade VM Compatibility from the menu. |
| Step 4 | In the Compatible with field, select ESXi 7.0 U1 and later and click OK . Note For all components, the supported VMware ESXi version is 7.0 U1 or later. Choosing ESXi 7.0 U1 and later will automatically set the VM hardware version to 18 . Selecting a ESXi version is irreversible. For example, if you set it to ESXi 7.0 U1 and later , you can only upgrade; downgrading to a previous ESXi version will not be possible. For more virtualization details, see Virtualization Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html | Note | For all components, the supported VMware ESXi version is 7.0 U1 or later. Choosing ESXi 7.0 U1 and later will automatically set the VM hardware version to 18 . Selecting a ESXi version is irreversible. For example, if you set it to ESXi 7.0 U1 and later , you can only upgrade; downgrading to a previous ESXi version will not be possible. For more virtualization details, see Virtualization Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
| Note | For all components, the supported VMware ESXi version is 7.0 U1 or later. Choosing ESXi 7.0 U1 and later will automatically set the VM hardware version to 18 . Selecting a ESXi version is irreversible. For example, if you set it to ESXi 7.0 U1 and later , you can only upgrade; downgrading to a previous ESXi version will not be possible. For more virtualization details, see Virtualization Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
| Step 5 | Right-click the VM and select Edit Settings . |
| Step 6 | Click the VM Options tab and expand General Options . |
| Step 7 | Select the Guest OS as follows and then click OK . Note For Unified CCE components and Unified CVP, you must select: Guest OS Family —Windows Guest OS Version — For Unified ICM and Unified CVP, choose Microsoft Windows Server 2019 (64-bit) or Microsoft Windows Server 2022 (64-bit). For Unified Intelligence Center, Finesse, Cisco VVB, and Cloud Connect, you must select: Guest OS Family —Linux Guest OS Version —Other 4.x or later Linux (64-bit) For ECE, you must select: Guest OS Family —Windows Guest OS Version — Microsoft Windows Server 2022 (64-bit). | Note | For Unified CCE components and Unified CVP, you must select: Guest OS Family —Windows Guest OS Version — For Unified ICM and Unified CVP, choose Microsoft Windows Server 2019 (64-bit) or Microsoft Windows Server 2022 (64-bit). For Unified Intelligence Center, Finesse, Cisco VVB, and Cloud Connect, you must select: Guest OS Family —Linux Guest OS Version —Other 4.x or later Linux (64-bit) For ECE, you must select: Guest OS Family —Windows Guest OS Version — Microsoft Windows Server 2022 (64-bit). |
| Note | For Unified CCE components and Unified CVP, you must select: Guest OS Family —Windows Guest OS Version — For Unified ICM and Unified CVP, choose Microsoft Windows Server 2019 (64-bit) or Microsoft Windows Server 2022 (64-bit). For Unified Intelligence Center, Finesse, Cisco VVB, and Cloud Connect, you must select: Guest OS Family —Linux Guest OS Version —Other 4.x or later Linux (64-bit) For ECE, you must select: Guest OS Family —Windows Guest OS Version — Microsoft Windows Server 2022 (64-bit). |
| Step 8 | Power on the VM. |

| Note | For all components, the supported VMware ESXi version is 7.0 U1 or later. Choosing ESXi 7.0 U1 and later will automatically set the VM hardware version to 18 . Selecting a ESXi version is irreversible. For example, if you set it to ESXi 7.0 U1 and later , you can only upgrade; downgrading to a previous ESXi version will not be possible. For more virtualization details, see Virtualization Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
|---|---|

| Note | For Unified CCE components and Unified CVP, you must select: Guest OS Family —Windows Guest OS Version — For Unified ICM and Unified CVP, choose Microsoft Windows Server 2019 (64-bit) or Microsoft Windows Server 2022 (64-bit). For Unified Intelligence Center, Finesse, Cisco VVB, and Cloud Connect, you must select: Guest OS Family —Linux Guest OS Version —Other 4.x or later Linux (64-bit) For ECE, you must select: Guest OS Family —Windows Guest OS Version — Microsoft Windows Server 2022 (64-bit). |
|---|---|

| Note | Ensure to run the RegUtil tool with administrative privileges. |
|---|---|

| Note | For coresident configurations, upgrade CUIC/LiveData/IdS server along with the Unified CCE Central Controller upgrade. |
|---|---|

| Task | See |
|---|---|
| Cisco Reverse Proxy |
| (Optional) Install Cisco Reverse Proxy | If you don't have Cisco Reverse Proxy in your environment and you want to use VPN-less desktop access feature or to upgrade
                                       Cisco Reverse Proxy 12.6(2) to 15.0(1), you must install Cisco Reverse Proxy 15.0(1). Refer to the Notes on VM Templates for 15.0(1) topic in the Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS page for the installer location. For more information on how to install Cisco Reverse Proxy, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) . Note Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. | Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
| Cloud Connect |
| Install Cloud Connect | Install Cloud Connect If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Overview for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component. Upgrade both the publisher and subscriber. For Cloud Connect upgrade instructions, see the Upgrade Cloud Connect section. If you don’t have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                       Connect. For fresh install instructions, see the Install Cloud Connect section. Note Check the disk size by running the command show hardware in the Cloud Connect admin console. SDA1 and SDA2 should be at least 44 GB. If not, contact Cisco TAC team for support. | Note | Check the disk size by running the command show hardware in the Cloud Connect admin console. SDA1 and SDA2 should be at least 44 GB. If not, contact Cisco TAC team for support. |
| Note | Check the disk size by running the command show hardware in the Cloud Connect admin console. SDA1 and SDA2 should be at least 44 GB. If not, contact Cisco TAC team for support. |
| Queuing and self-service components |
| Upgrade Cisco Unified Customer Voice Portal. 1 | Installation and Upgrade
                                                				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html |
| Infrastructure and media resource components |
| Cisco Virtualized Voice Browser | Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html |
| Upgrade voice and data gateways. | Upgrade Voice and Data Gateways |
| Identity Service/SSO |
| Identity Service (IdS)/Single Sign-On(SSO) | SSO is an optional feature and exchanges authentication and authorization details between an identity provider (IdP) and an
                                       identity service (IdS). For more information, see Upgrade Flowcharts . https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Upgrade Enterprise Chat and Email (ECE) | For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| Upgrade Finesse | For more information, see Cisco Finesse Installation and Upgrade Guide Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . When upgrading from Cisco Finesse 12.6(2) to 15.0(1), Unified Intelligence Center gadgets won't load. To resolve this, Upgrade
                                       Unified Intelligence Center to either 12.6(2) ES 04 or to 15.0(1). |
| Reporting server |
| Upgrade Cisco Unified Intelligence Center server. | Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Unified CCE Central Controller and Administration & Data Server components Note You can perform a Common Ground upgrade for CCE either by upgrading the operating system to Windows Server 2022 or by upgrading
                                                CCE to version 15.0(1) while retaining Windows Server 2019. An in-place upgrade to Windows Server 2022 is now supported. However,
                                                note that an in-place upgrade to Windows Server 2019 is not supported. Note If you want to leverage the capabilities of graceful shutdown to bring down the Unified CCE services, use the maintenance
                                                   mode command. For more information, see the Invoking Maintenance Mode topic in the AdministrationGuide for Cisco Unified Contact Center Enterprise at the https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . Note Refer the Expand Disk Space for Virtual Machines section in Upgrade Overview to increase the hard disk before you upgrade the component. For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html | Note | You can perform a Common Ground upgrade for CCE either by upgrading the operating system to Windows Server 2022 or by upgrading
                                                CCE to version 15.0(1) while retaining Windows Server 2019. An in-place upgrade to Windows Server 2022 is now supported. However,
                                                note that an in-place upgrade to Windows Server 2019 is not supported. | Note | If you want to leverage the capabilities of graceful shutdown to bring down the Unified CCE services, use the maintenance
                                                   mode command. For more information, see the Invoking Maintenance Mode topic in the AdministrationGuide for Cisco Unified Contact Center Enterprise at the https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . | Note | Refer the Expand Disk Space for Virtual Machines section in Upgrade Overview to increase the hard disk before you upgrade the component. For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
| Note | You can perform a Common Ground upgrade for CCE either by upgrading the operating system to Windows Server 2022 or by upgrading
                                                CCE to version 15.0(1) while retaining Windows Server 2019. An in-place upgrade to Windows Server 2022 is now supported. However,
                                                note that an in-place upgrade to Windows Server 2019 is not supported. |
| Note | If you want to leverage the capabilities of graceful shutdown to bring down the Unified CCE services, use the maintenance
                                                   mode command. For more information, see the Invoking Maintenance Mode topic in the AdministrationGuide for Cisco Unified Contact Center Enterprise at the https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
| Note | Refer the Expand Disk Space for Virtual Machines section in Upgrade Overview to increase the hard disk before you upgrade the component. For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
| Bring down Side A Logger, and upgrade the VM to the new platform of Windows Server and SQL Server. Note If you want to leverage the capabilities of graceful shutdown to bring down  Side A Logger, use the maintenance mode command
                                                   to invoke  maintenance mode. | Note | If you want to leverage the capabilities of graceful shutdown to bring down  Side A Logger, use the maintenance mode command
                                                   to invoke  maintenance mode. | Upgrade Windows Server Upgrade SQL Server |
| Note | If you want to leverage the capabilities of graceful shutdown to bring down  Side A Logger, use the maintenance mode command
                                                   to invoke  maintenance mode. |
| Migrate Side A Logger database, and upgrade the Logger. | Migrate Unified CCE Logger Database and Upgrade Logger |
| Bring down Side A Call Router, and upgrade the VM to new platform of Windows Server. Note If you want to leverage the capabilities of graceful shutdown to bring down  Side A Call Router, use  the maintenance mode
                                                   command to invoke  maintenance mode. | Note | If you want to leverage the capabilities of graceful shutdown to bring down  Side A Call Router, use  the maintenance mode
                                                   command to invoke  maintenance mode. | Upgrade Windows Server |
| Note | If you want to leverage the capabilities of graceful shutdown to bring down  Side A Call Router, use  the maintenance mode
                                                   command to invoke  maintenance mode. |
| Upgrade Side A Call Router. | Upgrade Unified CCE Call Router |
| Upgrade the VM for the Administration & Data Server connected to Side A to the new platform of Windows Server and SQL Server. | Upgrade Windows Server Upgrade SQL Server |
| Upgrade the Administration & Data Server connected to Side A. | Migrate HDS Database and Upgrade Unified CCE Administration & Data Server |
| Bring Side A Logger and Call Router into service, bring down Side B Logger and Call Router. | Bring Upgraded Side A into Service |
| Upgrade the VM for the Side B Logger to the new platform of Windows Server and SQL Server. | Upgrade Windows Server Upgrade SQL Server |
| Migrate Side B Logger database and upgrade the Logger. | Migrate Unified CCE Logger Database and Upgrade Logger |
| Upgrade the VM for the Side B Call Router to new platform of Windows Server. | Upgrade Windows Server |
| Upgrade Side B Call Router. | Upgrade Unified CCE Call Router |
| Bring Side B Call Router into service and verify operation. Bring Side B Logger into service and verify operation. | Verify Operation of Upgraded Side B Call Router and Logger |
| Upgrade the VM for the Administration & Data Server connected to Side B to the new platform of Windows Server and SQL Server. | Upgrade Windows Server Upgrade SQL Server |
| Upgrade the Administration & Data Server connected to Side B. | Migrate HDS Database and Upgrade Unified CCE Administration & Data Server |
| Upgrade Cisco Unified Intelligence Center reporting templates. | Import Reports section in Cisco Unified Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html |
| Upgrade Unified Contact Center Management Portal(Unified CCMP). | Installation and
                                                				  Configuration Guide for Cisco Unified Contact Center Management
                                                				  Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/products-installation-guides-list.html |
| Upgrade Administration Client. | Upgrade Unified CCE Administration Client |
| Database Performance Enhancement. | Database Performance Enhancement |
| Unified CCE Peripheral Gateways and associated components Note Refer the Expand Disk Space for Virtual Machines section in Upgrade Overview to increase the hard disk before you upgrade the component. For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html | Note | Refer the Expand Disk Space for Virtual Machines section in Upgrade Overview to increase the hard disk before you upgrade the component. For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
| Note | Refer the Expand Disk Space for Virtual Machines section in Upgrade Overview to increase the hard disk before you upgrade the component. For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
| Bring down Side A PG and Outbound Dialer Note If you want to leverage the capabilities of graceful shutdown to bring down Side A PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode. | Note | If you want to leverage the capabilities of graceful shutdown to bring down Side A PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode. | Upgrade Peripheral Gateways Upgrade Outbound Option Dialer |
| Note | If you want to leverage the capabilities of graceful shutdown to bring down Side A PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode. |
| Upgrade Side A VM for the PG to the new Platform of Windows Server. | Upgrade Windows Server |
| Upgrade PGs on Side A. | Upgrade Peripheral Gateways |
| Upgrade Outbound Option Dialer on Side A. | Upgrade Outbound Option Dialer |
| Bring up Side A PG and Outbound Dialer to service. | Upgrade Peripheral Gateways Upgrade Outbound Option Dialer |
| Bring down Side B PG and Outbound Dialer. Note If you want to leverage the capabilities of graceful shutdown to bring down Side B PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode. | Note | If you want to leverage the capabilities of graceful shutdown to bring down Side B PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode. |
| Note | If you want to leverage the capabilities of graceful shutdown to bring down Side B PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode. |
| Upgrade Side B VM for the PG to the new Platform of Windows Server. |
| Upgrade PGs on Side B. |
| Upgrade Side B Outbound Option Dialer. |
| Bring up Side B PG and outbound dialer services . |
| Upgrade Customer Collaboration Platform | Cisco Customer Collaboration Platform User Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html . |
| Call processing components |
| Upgrade Cisco Unified Communications Manager. | Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/ unified-communications-manager-callmanager/ products-installation-guides-list.html |
| Upgrade (uninstall and reinstall) the JTAPI client on the Cisco Unified Communications Manager PG. | Upgrade Cisco JTAPI Client on PG |

| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
|---|---|

| Note | Check the disk size by running the command show hardware in the Cloud Connect admin console. SDA1 and SDA2 should be at least 44 GB. If not, contact Cisco TAC team for support. |
|---|---|

| Note | You can perform a Common Ground upgrade for CCE either by upgrading the operating system to Windows Server 2022 or by upgrading
                                                CCE to version 15.0(1) while retaining Windows Server 2019. An in-place upgrade to Windows Server 2022 is now supported. However,
                                                note that an in-place upgrade to Windows Server 2019 is not supported. |
|---|---|

| Note | If you want to leverage the capabilities of graceful shutdown to bring down the Unified CCE services, use the maintenance
                                                   mode command. For more information, see the Invoking Maintenance Mode topic in the AdministrationGuide for Cisco Unified Contact Center Enterprise at the https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|

| Note | Refer the Expand Disk Space for Virtual Machines section in Upgrade Overview to increase the hard disk before you upgrade the component. For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
|---|---|

| Note | If you want to leverage the capabilities of graceful shutdown to bring down  Side A Logger, use the maintenance mode command
                                                   to invoke  maintenance mode. |
|---|---|

| Note | If you want to leverage the capabilities of graceful shutdown to bring down  Side A Call Router, use  the maintenance mode
                                                   command to invoke  maintenance mode. |
|---|---|

| Note | Refer the Expand Disk Space for Virtual Machines section in Upgrade Overview to increase the hard disk before you upgrade the component. For more information on hard disk capacity, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html |
|---|---|

| Note | If you want to leverage the capabilities of graceful shutdown to bring down Side A PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode. |
|---|---|

| Note | If you want to leverage the capabilities of graceful shutdown to bring down Side B PG and Outbound Dialer, use the maintenance
                                                   mode command to invoke  maintenance mode. |
|---|---|

| Step 1 | Power off the VM. |
|---|---|
| Step 2 | Right-click the VM and select Edit Settings . |
| Step 3 | Click the VM Options tab and expand General Options . |
| Step 4 | From the Guest OS drop-down menu, select the guest operating system family. |
| Step 5 | From the Guest OS Version drop-down menu, select Microsoft Windows Server 2022 (64 bit) . Note To be able to select the Microsoft Windows Server 2022 (64 bit) guest operating system, you must set the VM hardware compatibility to ESXi 7.0 U1 and later. | Note | To be able to select the Microsoft Windows Server 2022 (64 bit) guest operating system, you must set the VM hardware compatibility to ESXi 7.0 U1 and later. |
| Note | To be able to select the Microsoft Windows Server 2022 (64 bit) guest operating system, you must set the VM hardware compatibility to ESXi 7.0 U1 and later. |
| Step 6 | Click OK . |

| Note | To be able to select the Microsoft Windows Server 2022 (64 bit) guest operating system, you must set the VM hardware compatibility to ESXi 7.0 U1 and later. |
|---|---|

| Note | If you are installing Microsoft SQL Server 2022, select only Database Engine Services. |
|---|---|

| Step 1 | Launch the SQL Server installer and refer to the Microsoft documentation for any necessary guidance. |
|---|---|
| Step 2 | Follow the wizard steps. Choose the default or correct instance for your deployment. |
| Step 3 | After upgrading SQL Server, install the latest SQL cumulative update. |

| Note | If the Database Engine Services fail during a Microsoft SQL Server upgrade, open the SQL Server Installer , choose Maintenance , and perform the edition upgrade to complete the installation. For more information, see the Upgrade SQL Server topic in Microsoft documentation. Microsoft SQL Server does not contain SQL Server Management Studio in the default toolkit. Re-run the SQL Server setup to install Management Studio by navigating to the SQL Selection Center > Installation > Install SQL Server Management Tools . If your computer has no internet connection, download and install the SQL server Management Studio manually. When connecting to SQL Server through the latest version of SQL Server Management Studio (SSMS), it's important to note that the default option for encryption and the Trust Server Certificate feature are not supported by CCE, as outlined in the Contact Center Enterprise Solution Compatibility Matrix . To ensure a successful connection, be sure to select the optional encryption setting and refrain from checking the Trust Server Certificate check box. |
|---|---|

| Step 1 | Use the maintenance mode command to invoke maintenance mode and bring down all the Unified CCE services on the Unified CCE
                                             servers that you are upgrading. Now set the startup type of all Unified CCE services as Manual . For more information, see the Invoking Maintainence Mode topic in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|
| Step 2 | Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the Logger system, prior to launching EDMT. These include
                                          the ODBC Driver 17.10 or later minor versions of ODBC 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2022. For more information about EDMT, see Preupgrade Overview . |
| Step 3 | Launch the EDMT and click Next . |
| Step 4 | Select Common Ground , and click Next . |
| Step 5 | On the warning message, click Yes if you have taken a backup of your database, and no services are currently running. Note If you have not taken the backup of your database, click No to exit the installer. | Note | If you have not taken the backup of your database, click No to exit the installer. |
| Note | If you have not taken the backup of your database, click No to exit the installer. |
| Step 6 | In the Database Connection section, highlight the database that you want to upgrade, and then click Next . |
| Step 7 | Click Start Migration . A warning message is displayed asking for confirmation of the data migration. |
| Step 8 | Click Yes to confirm. |
| Step 9 | Click OK to acknowledge the message. After completion of the data migration, a warning message is displayed asking you to select a
                                          valid deployment type. Note This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration. | Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration. |
| Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration. |
| Step 10 | Exit the EDMT. |
| Step 11 | (Optional) If Outbound Option High Availability is deployed, repeat steps 1 through 12 to migrate the BA database. Note If you are upgrading Logger from 12.6(x), you don't need to upgrade the BA database. | Note | If you are upgrading Logger from 12.6(x), you don't need to upgrade the BA database. |
| Note | If you are upgrading Logger from 12.6(x), you don't need to upgrade the BA database. |
| Step 12 | To upgrade the Logger, launch the ICM-CCE-Installer, and click Next . |
| Step 13 | (Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 14 | (Optional) Select SQL Server Security Hardening and click Next . |
| Step 15 | Click OK on any informational messages that display. |
| Step 16 | Click Install . |
| Step 17 | Reboot the server when the upgrade completes. |

| Note | If you have not taken the backup of your database, click No to exit the installer. |
|---|---|

| Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration. |
|---|---|

| Note | If you are upgrading Logger from 12.6(x), you don't need to upgrade the BA database. |
|---|---|

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | (Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 3 | Click OK on any informational messages that display. |
| Step 4 | Click Install . |
| Step 5 | Reboot the
                                          			 server when the upgrade completes. |

| Step 1 | Use the maintenance mode command to invoke maintenance mode and bring down all the Unified CCE services on the Unified CCE
                                             servers that you are upgrading. Now set the startup type of all Unified CCE services as Manual . For more information, see the Invoking Maintainence Mode topic in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|
| Step 2 | For HDS-related deployments. Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the Administration & Database Server system, before launching
                                          EDMT. These include the ODBC Driver 17.10 or later minor versions of ODBC 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2022. For more information about EDMT, see Preupgrade Overview . |
| Step 3 | Launch the EDMT and click Next . Select Common Ground and click Next . Review or change the information that is displayed as required and click Start Migration . Click Yes on the warning message that displays. Exit the EDMT. Note The warning message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data migration. | Note | The warning message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data migration. |
| Note | The warning message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data migration. |
| Step 4 | Launch the ICM-CCE-Installer and click Next . |
| Step 5 | (Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 6 | (Optional) Select SQL Server Security Hardening and click Next . |
| Step 7 | Click OK on any informational messages that display. |
| Step 8 | Click Install . |
| Step 9 | Reboot the server when the upgrade completes. Note The time required to complete a data migration varies in a direct
                                                      						relationship to the database size (the larger the database size, the longer
                                                      						it takes to migrate) and the server hardware performance level. For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine . | Note | The time required to complete a data migration varies in a direct
                                                      						relationship to the database size (the larger the database size, the longer
                                                      						it takes to migrate) and the server hardware performance level. |
| Note | The time required to complete a data migration varies in a direct
                                                      						relationship to the database size (the larger the database size, the longer
                                                      						it takes to migrate) and the server hardware performance level. |

| Note | The warning message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data migration. |
|---|---|

| Note | The time required to complete a data migration varies in a direct
                                                      						relationship to the database size (the larger the database size, the longer
                                                      						it takes to migrate) and the server hardware performance level. |
|---|---|

| Step 1 | Launch the  AdminClientInstaller and click Next . |
|---|---|
| Step 2 | (Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 3 | Click OK on any informational messages that display. |
| Step 4 | Click Install . |
| Step 5 | Reboot the server when the upgrade completes. For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine . |

| Note | VRU PG uses an existing maintenance mode from Unified CVP. Ensure you stop all the existing calls gracefully on the VRU PG by initiating the maintenance mode in Unified CVP to which
                                             the VRU PG is connected. For more information about maintenance mode in Unified CVP, see the Shut Down Server topic in Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
|---|---|

| Note | You must use the maintenance mode command to invoke maintenance mode in all PGs that reside on the same virtual machine. For
                                             more information, see the Invoking Maintenace Mode topic in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | (Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 3 | Click OK on any informational messages that display. |
| Step 4 | Click Install . |
| Step 5 | Reboot the server when the upgrade completes. |
| Step 6 | For the Agent PG, run the CceCrypTool to encrypt the JTAPI password. To run CceCrypTool, open command prompt in administrator mode and run the following command: CceCrypTool /instance <instance_name> /component <name of the component> /proc <name of the process> /mode <encrypt> For example: CceCrypTool /instance ucce /component PG1A /proc jgw1 /mode encrypt |

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | (Optional)To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 3 | Click OK on any informational messages that display. |
| Step 4 | Click Install . |
| Step 5 | Reboot the server when the upgrade completes. |
| Step 6 | Use Unified CCE Service Control to set all Unified CCE services to Automatic Start. |