---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-7e40b8bb49
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_12_6_1-install_upgrade_guide/ucce_b_12_6_1-install_upgrade_guide_chapter_0111.html
retrieved_at: 2026-08-16T20:01:18.591515+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Common Ground Upgrade

## Chapter: Common Ground Upgrade

# Common Ground Upgrade

## Preupgrade
                        	 Overview

The preupgrade process ensures that your systems have the necessary software to support your
                           			contact center. These tasks prepare the way for a successful upgrade of your Cisco
                           			contact center components to the new release.

Common Ground Upgrade is not supported if the platform upgrade from Windows Server 2016 and
                                       				SQL Server 2017 to Windows Server 2019 and SQL Server 2019 is planned as part of
                                       				upgrade process. Technology Refresh Upgrade is the supported upgrade option for
                                       				platform upgrade.

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

EDMT also requires Microsoft® ODBC Driver 17 for SQL Server® and Visual C++ Redistributable for Visual Studio 2015 (or higher). The latest version of these packages can
                                          be downloaded from the Microsoft website. However, a copy of the same is also available in the Prerequisites folder of EDMT.

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

### Disable Configuration Changes

Step 1

To disable configuration changes during the upgrade, set the following registry key to 1 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\Router A\Router\CurrentVersion\Configuration\Global\DBMaintenance .

Live data services connect to the new Central controller machines only after you upgrade both sides of Central controller,
                                                         and enable the configuration changes.

Step 2

Confirm that configuration changes are disabled by attempting to
                                          			 save a configuration change.

When you try to save the change, a message is displayed confirming
                                             				the change failure.

### Virtual Machine Snapshot for Unified CCE Component Virtual Machines

Uninstallation of Unified CCE 12.5(1) installed on server machines using the ICM-CCE-Installer ISO is not supported.

To revert to the previous versions that existed before you did a Common Ground in-place upgrade of installations to Unified
                                 CCE 12.5(1) , perform one of the following tasks:

Take a Virtual Machine Snapshot in the powered off state before the upgrade.

Clone the Virtual Machine before the upgrade.

Delete these snapshots or clones after the upgrades are successfully completed. Such deletions will prevent performance issues.

Uninstallation and re-installation of other packages like Administration Client and Internet Script Editor (ISE) will continue
                                 to be supported.

Uninstallation and re-installation are supported for Unified CCE 12.6(x).

### VM Hardware Version Upgrade

Perform the following procedure to upgrade the hardware version of the virtual machine (VM).

#### Before you begin

Power off the VM.

Step 1

Launch the vSphere Web Client using the browser.

Step 2

Log in to your vCenter Server.

Step 3

Right-click on the VM that needs to be upgraded, and select Compatibility > Upgrade VM Compatibility from the menu.

The Upgrade VM Compatibility option appears only if the hardware version on the VM is not the latest version supported.

Step 4

In the Compatible with field, select a 6.5 or later ESXi version.

For more virtualization details, see Vitualization Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html

Selecting a ESXi version is irreversible. For instance, if you set it to ESXi 7.0 U1 or later , you can only upgrade; downgrading ESXi version will not be possible.

Step 5

Click OK .

Step 6

Power on the VM.

If the system prompts, upgrade the VMware tools. For more information, see Install Vmware Tools .

### Increase the Provisioned Disk Size for Unified Intelligence Center VMs (Standalone and Coresident)

Step 1

Power off the virtual machine.

Step 2

Click Edit Settings .

Step 3

Click the Hardware tab, and select the hard disk to modify.

Step 4

In the Disk Provisioning pane, increase the provisioned size from 146 GB to 200 GB.

Step 5

Click OK to save your changes and close the dialog box.

Step 6

Start the virtual machine.

## Common Ground
                        	 Upgrade Task Flow

For the Unified CCE core components, there is a general flow for redundant systems to ensure that Cisco Contact Center operation
                              continues during the entire upgrade process. Sides A and B are brought down, upgraded, tested, and brought back up in a sequence
                              that ensures continuous operation of the Cisco Contact Center.

For coresident configurations, upgrade CUIC/LiveData/IdS server along with the Unified CCE Central Controller upgrade.

For Common Ground
                              		  upgrades, perform the following upgrade tasks:

Task

See

Install Cloud Connect

Install Cloud Connect

If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Overview for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component.

Upgrade both the publisher and subscriber. For Cloud Connect upgrade instructions, see the Upgrade Cloud Connect section.

If you don’t have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                          Connect. For fresh install instructions, see the Install Cloud Connect section.

Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html

Installation and Upgrade Guide for Cisco Virtualized Voice Browser at

https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html

Identity Service (IdS)/Single Sign-On(SSO)

SSO is an optional feature and exchanges authentication and authorization details between an identity provider (IdP) and an
                                          identity service (IdS).

For more information, see Upgrade Flowcharts

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Upgrade Enterprise Chat and Email (ECE)

For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

Upgrade Finesse

For more information, see Cisco Finesse Installation and Upgrade Guide Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

Installation and Upgrade Guide for Cisco Unified Intelligence Center at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Migrate Unified CCE Logger Database and Upgrade Logger

Upgrade Side A Call Router.

Upgrade Unified CCE Call Router

Upgrade the Administration & Data Server connected to Side A.

Bring Side A Logger and Call Router into service, bring down Side B Logger and Call Router.

Migrate Side B Logger database and upgrade the Logger.

Migrate Unified CCE Logger Database and Upgrade Logger

Upgrade Side B Call Router.

Upgrade Unified CCE Call Router

Upgrade the Administration & Data Server connected to Side B.

Migrate HDS Database and Upgrade Unified CCE Administration & Data Server

Import Reports section in Cisco Unified
                                             										Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html

Installation and
                                                   				  Configuration Guide for Cisco Unified Contact Center Management
                                                   				  Portal at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/products-installation-guides-list.html

Upgrade Administration Client.

Upgrade Unified CCE Administration Client

Certificates for Unified CCE Web Administration

Certificates for Unified Contact Center Enterprise Web Administration

Upgrade Customer Collaboration Platform

Cisco Customer Collaboration Platform User Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html .

Upgrade CTI OS server.

Cisco Agent Desktop
                                                   				  Installation Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/computer-telephony-integration-option/products-installation-guides-list.html

Cisco Agent Desktop
                                                   				  Installation Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/agent-desktop/products-installation-guides-list.html

The CTI Toolkit Desktop is only supported for System PG and other TDM PG deployments like Avaya PG.

Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/ unified-communications-manager-callmanager/ products-installation-guides-list.html

## Common Ground  Upgrade Tasks

The following
                              		  section provides instructions about upgrading the virtual environment and the
                              		  Unified CCE components. For  instructions about upgrading non-Unified CCE
                              		  components in a Unified CCE solution, for example Finesse and CUIC, see the links to component-specific
                              		  documents in the Common Ground Upgrade Task Flow .

### Migrate Unified CCE Logger Database and Upgrade Logger

To upgrade the Logger, you do the following tasks:

Migrate the Logger database.

If you use Outbound Option High Availability, do the following:

Migrate the Outbound Option database.

For the enhancements in Outbound Option High Availability to work effectively, Outbound Option High Availablity must be disabled
                                             before the logger upgrade and then enabled after the upgrade. For more information, see Disable Outbound Options High Availability (If Applicable) .

Install the new software.

Step 1

Using Unified CCE Service Control, stop all Unified CCE services on the server and change to Manual Start.

Step 2

(Optional) If Outbound Option High Availability is deployed, disable Outbound Options High Availability. For details, see Disable Outbound Options High Availability (If Applicable) .

Step 3

Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the Logger system, prior to launching EDMT. These include
                                          the ODBC Driver 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015.

Step 4

Launch the EDMT and click Next .

Step 5

Select Common Ground , and click Next .

Step 6

On the warning message, click Yes if you have taken a backup of your database, and no services are currently running.

If you have not taken the backup of your database, click No to exit the installer.

Step 7

In the Database Connection section, highlight the database that you want to upgrade, and then click Next .

Step 8

Click Start Migration . A warning message is displayed asking for confirmation of the data migration.

Step 9

Click Yes to confirm.

Step 10

Click OK to acknowledge the message. After completion of the data migration, a warning message is displayed asking you to select a
                                          valid deployment type.

This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration.

Step 11

Exit the EDMT.

Step 12

(Optional) If Outbound Option High Availability is deployed, repeat steps 1 through 12 to migrate the BA database.

Step 13

To upgrade the Logger, launch the ICM-CCE-Installer, and click Next .

Step 14

To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of  Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed from step 20.

Step 15

(Optional) Select SQL Server Security Hardening and click Next .

Step 16

Click OK on any informational messages that display.

Step 17

Click Install .

Step 18

Reboot the server when the upgrade completes.

Step 19

Log in to your system using domain credentials with administrative
                                          					privileges.

Step 20

Wait for the Unified CCE 12.6(1) installation wizard to launch. Click Next to proceed.

Step 21

Select the radio button to accept the license agreement and click Next .

Step 22

Click Install to begin the installation.

Step 23

Select the radio button to restart the system and click Finish .

You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 20.

Step 24

(Optional) If you use Outbound
                                          					Option High Availability, enable Outbound Option High Availablity in the Web
                                          					Setup tool. For details, see the Configure the Logger for Outbound
                                             						Option topic in the Outbound Option Guide for Unified Contact
                                             						Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

### Upgrade Unified  CCE Call Router

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed from step 7.

Step 3

Click OK on any informational messages that display.

Step 4

Click Install .

Step 5

Reboot the
                                          			 server when the upgrade completes.

Step 6

Log in to your system using domain credentials with administrative
                                          privileges.

Step 7

Wait for the Unified CCE 12.6(1) installation wizard to launch. Click Next to proceed.

Step 8

Select the radio button to accept the license agreement and click Next .

Step 9

Click Install to begin the installation.

Step 10

Select the radio button to restart the system and click Finish .

You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 7.

### Migrate HDS Database and Upgrade Unified CCE Administration & Data Server

The deployment of the Administration & Database Server determines which tools to use for an upgrade:

For an AW-only deployment, the EDMT is not required; the ICM-CCE-Installer completes the upgrade.

For any
                                       				deployment that involves an HDS database, use the EDMT to migrate the HDS
                                       				database before running the installer.

Step 1

Using Unified CCE Service Control, stop all Unified CCE services on the Server and change to Manual Start.

Step 2

For HDS-related deployments. Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same
                                          					have been installed on the Administration & Database Server system, before
                                          					launching EDMT. These include the ODBC Driver 17 for SQL Server, and Visual C++
                                          					Redistributable for Visual Studio 2015.

For more information about EDMT, see Preupgrade Overview .

Step 3

Launch the EDMT and click Next . Select Common Ground and click Next . Review or change the information that is displayed as required and click Start Migration . Click Yes on the warning message that displays. Exit the EDMT.

This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in
                                                         							the Congestion_Control table during data
                                                         							migration.

Step 4

Launch the ICM-CCE-Installer and click Next .

Step 5

To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed from step 11.

Step 6

(Optional) Select SQL Server Security Hardening and click Next .

Step 7

Click OK on any informational messages that display.

Step 8

Click Install .

Step 9

Reboot the server when the upgrade completes.

For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine .

Step 10

Log in to your system using domain credentials with administrative
                                          					privileges.

Step 11

Wait for the Unified CCE 12.6(1) installation wizard to launch. Click Next to proceed.

Step 12

Select the radio button to accept the license agreement and click Next .

Step 13

Click Install to begin the installation.

Step 14

Select the radio button to restart the system and click Finish .

You can upgrade from Unified ICM version 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 11.

### Upgrade Unified CCE Administration Client

Step 1

Launch the 12.5 AdminClientInstaller and click Next .

Step 2

To apply any 12.6(1) Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Administration Client 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed from step 6.

Step 3

Click OK on any informational messages that display.

Step 4

Click Install .

Step 5

Reboot the server when the upgrade completes.

For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine .

Step 6

Log in to your system using domain credentials with administrative privileges. The Unified CCE Release 12.6(1) installation wizard to launches. Click Next to proceed.

Step 7

Select the radio button to accept the license agreement and click Next .

Step 8

Click Install to begin the installation.

Step 9

Select the radio button to restart the system and click Finish .

### Enable Configuration Changes

Step 1

To enable configuration changes during the upgrade, set the
                                          			 following registry key to 0 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                             				Inc.\ICM\<instance name>\Router
                                             				A\Router\CurrentVersion\Configuration\Global\DBMaintenance .

Step 2

To confirm that configuration changes are enabled, save a configuration change.

Save your changes.

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

When you
                                       				upgrade the Unified Communications Manager application, upgrade the JTAPI
                                       				client that is associated with the Unified Communications Manager PG at the
                                       				same time.

When the CTI server that is associated with the PG gets upgraded, the CTI server connection mode is set to the Mixed mode
                                 by default. The Mixed mode enables both Secured and Non-Secured mode of connection. For the Secured mode of connection, a
                                 new port is selected based on the port selection logic. For more information on Port Utilization, see the Port Utilization Guide for Cisco Unified Contact Center Solutions . If the port that is selected by default conflicts with the existing ports, then you need to either release the default port
                                 or change the Secured mode port to an available port after the upgrade.

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed with the installation.

Step 3

Click OK on any informational messages that display.

Step 4

Click Install .

Step 5

Reboot the
                                          			 server when the upgrade completes.

### Upgrade Outbound Option Dialer

During the upgrade, information about which contacts were called and which you need call is lost for in-process outbound campaigns.
                                 Plan the timing of the upgrade accordingly.

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed with the installation.

Step 3

Click OK on any informational messages that display.

Step 4

Click Install .

Step 5

Reboot the server when the upgrade completes.

Step 6

Use Unified CCE Service Control to set all Unified CCE services to Automatic Start.

| Note | Common Ground Upgrade is not supported if the platform upgrade from Windows Server 2016 and
                                       				SQL Server 2017 to Windows Server 2019 and SQL Server 2019 is planned as part of
                                       				upgrade process. Technology Refresh Upgrade is the supported upgrade option for
                                       				platform upgrade. |
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
| Notify all stakeholders, including: Cisco Technical Assistance Center (TAC) Local Cisco Representatives Customer Operations and Emergency Management Center Third-party vendors as applicable |  |

| Step 1 | To disable configuration changes during the upgrade, set the following registry key to 1 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\Router A\Router\CurrentVersion\Configuration\Global\DBMaintenance . Note Live data services connect to the new Central controller machines only after you upgrade both sides of Central controller,
                                                         and enable the configuration changes. | Note | Live data services connect to the new Central controller machines only after you upgrade both sides of Central controller,
                                                         and enable the configuration changes. |
|---|---|---|---|
| Note | Live data services connect to the new Central controller machines only after you upgrade both sides of Central controller,
                                                         and enable the configuration changes. |
| Step 2 | Confirm that configuration changes are disabled by attempting to
                                          			 save a configuration change. When you try to save the change, a message is displayed confirming
                                             				the change failure. |

| Note | Live data services connect to the new Central controller machines only after you upgrade both sides of Central controller,
                                                         and enable the configuration changes. |
|---|---|

| Note | Uninstallation and re-installation are supported for Unified CCE 12.6(x). |
|---|---|

| Step 1 | Launch the vSphere Web Client using the browser. |
|---|---|
| Step 2 | Log in to your vCenter Server. |
| Step 3 | Right-click on the VM that needs to be upgraded, and select Compatibility > Upgrade VM Compatibility from the menu. Note The Upgrade VM Compatibility option appears only if the hardware version on the VM is not the latest version supported. | Note | The Upgrade VM Compatibility option appears only if the hardware version on the VM is not the latest version supported. |
| Note | The Upgrade VM Compatibility option appears only if the hardware version on the VM is not the latest version supported. |
| Step 4 | In the Compatible with field, select a 6.5 or later ESXi version. For more virtualization details, see Vitualization Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html Note Selecting a ESXi version is irreversible. For instance, if you set it to ESXi 7.0 U1 or later , you can only upgrade; downgrading ESXi version will not be possible. | Note | Selecting a ESXi version is irreversible. For instance, if you set it to ESXi 7.0 U1 or later , you can only upgrade; downgrading ESXi version will not be possible. |
| Note | Selecting a ESXi version is irreversible. For instance, if you set it to ESXi 7.0 U1 or later , you can only upgrade; downgrading ESXi version will not be possible. |
| Step 5 | Click OK . This sets the hardware version of the VM to 13 . |
| Step 6 | Power on the VM. Note If the system prompts, upgrade the VMware tools. For more information, see Install Vmware Tools . | Note | If the system prompts, upgrade the VMware tools. For more information, see Install Vmware Tools . |
| Note | If the system prompts, upgrade the VMware tools. For more information, see Install Vmware Tools . |

| Note | The Upgrade VM Compatibility option appears only if the hardware version on the VM is not the latest version supported. |
|---|---|

| Note | Selecting a ESXi version is irreversible. For instance, if you set it to ESXi 7.0 U1 or later , you can only upgrade; downgrading ESXi version will not be possible. |
|---|---|

| Note | If the system prompts, upgrade the VMware tools. For more information, see Install Vmware Tools . |
|---|---|

| Step 1 | Power off the virtual machine. |
|---|---|
| Step 2 | Click Edit Settings . |
| Step 3 | Click the Hardware tab, and select the hard disk to modify. |
| Step 4 | In the Disk Provisioning pane, increase the provisioned size from 146 GB to 200 GB. |
| Step 5 | Click OK to save your changes and close the dialog box. |
| Step 6 | Start the virtual machine. |

| Note | For coresident configurations, upgrade CUIC/LiveData/IdS server along with the Unified CCE Central Controller upgrade. |
|---|---|

| Task | See |
|---|---|
| Cloud Connection
                                          									Components |
| Install Cloud Connect | Install Cloud Connect If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Overview for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component. Upgrade both the publisher and subscriber. For Cloud Connect upgrade instructions, see the Upgrade Cloud Connect section. If you don’t have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                          Connect. For fresh install instructions, see the Install Cloud Connect section. |
| Queuing and self-service components |
| Upgrade Cisco Unified Customer Voice Portal. 1 | Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html |
| Infrastructure and media resource components |
| Cisco Virtualized Voice Browser | Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html |
| Upgrade voice and data gateways. | Upgrade Voice and Data Gateways |
| Identity Service/SSO |
| Identity Service (IdS)/Single Sign-On(SSO) | SSO is an optional feature and exchanges authentication and authorization details between an identity provider (IdP) and an
                                          identity service (IdS). For more information, see Upgrade Flowcharts https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Upgrade Enterprise Chat and Email (ECE) | For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| Upgrade Finesse | For more information, see Cisco Finesse Installation and Upgrade Guide Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . |
| Reporting server |
| Upgrade Cisco Unified Intelligence Center server. | Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Unified CCE Central Controller and Administration & Data Server components |
| Migrate Side A Logger database, and upgrade the Logger. | Migrate Unified CCE Logger Database and Upgrade Logger |
| Upgrade Side A Call Router. | Upgrade Unified CCE Call Router |
| Upgrade the Administration & Data Server connected to Side A. | Migrate HDS Database and Upgrade Unified CCE Administration & Data Server |
| Bring Side A Logger and Call Router into service, bring down Side B Logger and Call Router. | Bring Upgraded Side A into Service |
| Migrate Side B Logger database and upgrade the Logger. | Migrate Unified CCE Logger Database and Upgrade Logger |
| Upgrade Side B Call Router. | Upgrade Unified CCE Call Router |
| Bring Side B Call Router into service and verify operation. Bring Side B Logger into service and verify operation. | Verify Operation of Upgraded Side B Call Router and Logger |
| Upgrade the Administration & Data Server connected to Side B. | Migrate HDS Database and Upgrade Unified CCE Administration & Data Server |
| Upgrade Cisco Unified Intelligence Center reporting templates. | Import Reports section in Cisco Unified
                                             										Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html |
| Upgrade Unified Contact Center Management Portal(Unified CCMP). | Installation and
                                                   				  Configuration Guide for Cisco Unified Contact Center Management
                                                   				  Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/products-installation-guides-list.html |
| Upgrade Administration Client. | Upgrade Unified CCE Administration Client |
| Database Performance Enhancement. | Database Performance Enhancement |
| Certificates for Unified CCE Web Administration | Certificates for Unified Contact Center Enterprise Web Administration |
| Unified CCE Peripheral Gateways and associated components |
| Upgrade PGs. | Upgrade Peripheral Gateways |
| Upgrade Outbound Option Dialer. | Upgrade Outbound Option Dialer |
| Upgrade Customer Collaboration Platform | Cisco Customer Collaboration Platform User Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html . |
| Upgrade CTI OS server. | Cisco Agent Desktop
                                                   				  Installation Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/computer-telephony-integration-option/products-installation-guides-list.html |
| Desktop client components |
| CTI OS Client desktop applications. | Cisco Agent Desktop
                                                   				  Installation Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/agent-desktop/products-installation-guides-list.html Note The CTI Toolkit Desktop is only supported for System PG and other TDM PG deployments like Avaya PG. | Note | The CTI Toolkit Desktop is only supported for System PG and other TDM PG deployments like Avaya PG. |
| Note | The CTI Toolkit Desktop is only supported for System PG and other TDM PG deployments like Avaya PG. |
| Call processing components |
| Upgrade Cisco Unified Communications Manager. | Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/ unified-communications-manager-callmanager/ products-installation-guides-list.html |
| Upgrade (uninstall and reinstall) the JTAPI client on the Cisco Unified Communications Manager PG. | Upgrade Cisco JTAPI Client on PG |

| Note | The CTI Toolkit Desktop is only supported for System PG and other TDM PG deployments like Avaya PG. |
|---|---|

| Step 1 | Using Unified CCE Service Control, stop all Unified CCE services on the server and change to Manual Start. |
|---|---|
| Step 2 | (Optional) If Outbound Option High Availability is deployed, disable Outbound Options High Availability. For details, see Disable Outbound Options High Availability (If Applicable) . |
| Step 3 | Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the Logger system, prior to launching EDMT. These include
                                          the ODBC Driver 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015. For more information about EDMT, see Preupgrade Overview . |
| Step 4 | Launch the EDMT and click Next . |
| Step 5 | Select Common Ground , and click Next . |
| Step 6 | On the warning message, click Yes if you have taken a backup of your database, and no services are currently running. Note If you have not taken the backup of your database, click No to exit the installer. | Note | If you have not taken the backup of your database, click No to exit the installer. |
| Note | If you have not taken the backup of your database, click No to exit the installer. |
| Step 7 | In the Database Connection section, highlight the database that you want to upgrade, and then click Next . |
| Step 8 | Click Start Migration . A warning message is displayed asking for confirmation of the data migration. |
| Step 9 | Click Yes to confirm. |
| Step 10 | Click OK to acknowledge the message. After completion of the data migration, a warning message is displayed asking you to select a
                                          valid deployment type. Note This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration. | Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration. |
| Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration. |
| Step 11 | Exit the EDMT. |
| Step 12 | (Optional) If Outbound Option High Availability is deployed, repeat steps 1 through 12 to migrate the BA database. |
| Step 13 | To upgrade the Logger, launch the ICM-CCE-Installer, and click Next . |
| Step 14 | To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of  Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed from step 20. |
| Step 15 | (Optional) Select SQL Server Security Hardening and click Next . |
| Step 16 | Click OK on any informational messages that display. |
| Step 17 | Click Install . |
| Step 18 | Reboot the server when the upgrade completes. |
| Step 19 | Log in to your system using domain credentials with administrative
                                          					privileges. |
| Step 20 | Wait for the Unified CCE 12.6(1) installation wizard to launch. Click Next to proceed. |
| Step 21 | Select the radio button to accept the license agreement and click Next . |
| Step 22 | Click Install to begin the installation. |
| Step 23 | Select the radio button to restart the system and click Finish . Note You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 20. | Note | You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 20. |
| Note | You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 20. |
| Step 24 | (Optional) If you use Outbound
                                          					Option High Availability, enable Outbound Option High Availablity in the Web
                                          					Setup tool. For details, see the Configure the Logger for Outbound
                                             						Option topic in the Outbound Option Guide for Unified Contact
                                             						Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html . |

| Note | If you have not taken the backup of your database, click No to exit the installer. |
|---|---|

| Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in the Congestion_Control table during data
                                                         							migration. |
|---|---|

| Note | You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 20. |
|---|---|

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed from step 7. |
| Step 3 | Click OK on any informational messages that display. |
| Step 4 | Click Install . |
| Step 5 | Reboot the
                                          			 server when the upgrade completes. |
| Step 6 | Log in to your system using domain credentials with administrative
                                          privileges. |
| Step 7 | Wait for the Unified CCE 12.6(1) installation wizard to launch. Click Next to proceed. |
| Step 8 | Select the radio button to accept the license agreement and click Next . |
| Step 9 | Click Install to begin the installation. |
| Step 10 | Select the radio button to restart the system and click Finish . Note You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 7. | Note | You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 7. |
| Note | You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 7. |

| Note | You can upgrade from Unified ICM 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 7. |
|---|---|

| Step 1 | Using Unified CCE Service Control, stop all Unified CCE services on the Server and change to Manual Start. |
|---|---|
| Step 2 | For HDS-related deployments. Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same
                                          					have been installed on the Administration & Database Server system, before
                                          					launching EDMT. These include the ODBC Driver 17 for SQL Server, and Visual C++
                                          					Redistributable for Visual Studio 2015. For more information about EDMT, see Preupgrade Overview . |
| Step 3 | Launch the EDMT and click Next . Select Common Ground and click Next . Review or change the information that is displayed as required and click Start Migration . Click Yes on the warning message that displays. Exit the EDMT. Note This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in
                                                         							the Congestion_Control table during data
                                                         							migration. | Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in
                                                         							the Congestion_Control table during data
                                                         							migration. |
| Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in
                                                         							the Congestion_Control table during data
                                                         							migration. |
| Step 4 | Launch the ICM-CCE-Installer and click Next . |
| Step 5 | To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed from step 11. |
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
| Step 10 | Log in to your system using domain credentials with administrative
                                          					privileges. |
| Step 11 | Wait for the Unified CCE 12.6(1) installation wizard to launch. Click Next to proceed. |
| Step 12 | Select the radio button to accept the license agreement and click Next . |
| Step 13 | Click Install to begin the installation. |
| Step 14 | Select the radio button to restart the system and click Finish . Note You can upgrade from Unified ICM version 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 11. | Note | You can upgrade from Unified ICM version 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 11. |
| Note | You can upgrade from Unified ICM version 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 11. |

| Note | This message notification is applicable only when EDMT finds the DeploymentType as 0(Zero) in
                                                         							the Congestion_Control table during data
                                                         							migration. |
|---|---|

| Note | The time required to complete a data migration varies in a direct
                                                      						relationship to the database size (the larger the database size, the longer
                                                      						it takes to migrate) and the server hardware performance level. |
|---|---|

| Note | You can upgrade from Unified ICM version 12.5(1) to Unified ICM 12.6(1) by double-clicking the Unified ICM 12.6(1) installer, and proceeding from Step 11. |
|---|---|

| Step 1 | Launch the 12.5 AdminClientInstaller and click Next . |
|---|---|
| Step 2 | To apply any 12.6(1) Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Administration Client 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed from step 6. |
| Step 3 | Click OK on any informational messages that display. |
| Step 4 | Click Install . |
| Step 5 | Reboot the server when the upgrade completes. For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine . |
| Step 6 | Log in to your system using domain credentials with administrative privileges. The Unified CCE Release 12.6(1) installation wizard to launches. Click Next to proceed. |
| Step 7 | Select the radio button to accept the license agreement and click Next . |
| Step 8 | Click Install to begin the installation. |
| Step 9 | Select the radio button to restart the system and click Finish . |

| Step 1 | To enable configuration changes during the upgrade, set the
                                          			 following registry key to 0 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                             				Inc.\ICM\<instance name>\Router
                                             				A\Router\CurrentVersion\Configuration\Global\DBMaintenance . |
|---|---|
| Step 2 | To confirm that configuration changes are enabled, save a configuration change. Save your changes. |

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed with the installation. |
| Step 3 | Click OK on any informational messages that display. |
| Step 4 | Click Install . |
| Step 5 | Reboot the
                                          			 server when the upgrade completes. |

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | To apply the Unified ICM 12.6 Minor Release, click Browse and navigate to the Minor Release software. Click Next . You can also proceed with the installation of Unified ICM 12.5(1) without selecting the Unified ICM 12.6(1) installer in this step. After installing Unified ICM 12.5(1), double-click the Unified ICM 12.6(1) installer, and proceed with the installation. |
| Step 3 | Click OK on any informational messages that display. |
| Step 4 | Click Install . |
| Step 5 | Reboot the server when the upgrade completes. |
| Step 6 | Use Unified CCE Service Control to set all Unified CCE services to Automatic Start. |