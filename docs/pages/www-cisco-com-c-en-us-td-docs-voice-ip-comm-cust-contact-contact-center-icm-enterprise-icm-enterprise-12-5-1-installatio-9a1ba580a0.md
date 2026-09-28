---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-9a1ba580a0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_12_5_Install_upgrade_guide_ucce/ucce_b_cisco-unified-contact-center-enterprise12_5_chapter_01001.html
retrieved_at: 2026-08-16T19:53:20.850585+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: February 3, 2020

Chapter: Technology Refresh Upgrade

## Chapter: Technology Refresh Upgrade

# Technology Refresh Upgrade

## Preupgrade Overview

The preupgrade process ensures that your systems have the necessary software to support your contact center. These tasks prepare
                           the way for a successful upgrade of your Cisco contact center components to the new release.

During the Technology Refresh (TR) Upgrade process, the installer is designed to identify any unsupported features present
                                       in the source deployment. These features are then listed in a dialog box for you to review. You have two options on how to
                                       proceed:

Select "Yes": By choosing "Yes", you instruct the installer to exclude all the identified unsupported features during the
                                             upgrade process. The installer will proceed with the Technology Refresh Upgrade, ensuring that the unsupported features do
                                             not interfere with the updated system functionality.

Select "No": If you choose "No", the installer will terminate immediately without making any changes to the deployment.

For more information about the list of unsupported features, see the Removed and Unsupported Features topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html

If you need to upgrade from version 12.6(2) to 15.0(1) to leverage the capabilities of graceful shutdown, you must first install
                                       12.6(2) ES53 before proceeding with the upgrade to 15.0(1). For more information about the router graceful shutdown, see the Unified CCE Router graceful shutdown topic in the Administration Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) .

During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, SQL Server Security Hardening optional configuration
                                       should not be selected as part of an installation. SQL Security Hardening should be applied post Unified CCE installation
                                       using the Security Wizard tool.

Unified CCE services should be started only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed.

If AppDynamics Monitoring was enabled on the ICM source machine, it will not be automatically enabled based on the source
                                       machine’s configuration during the Technology Refresh Upgrade. For deployments using AppDynamics for monitoring, it is necessary
                                       to manually configure and enable performance monitoring on the destination machines after completing the Technology Refresh
                                       Upgrade.

Ensure that Internet Information Services (IIS) is disabled on Windows Server before installing Unified CCE software with
                                       the ICM-CCE-Installer.

If the system is enabled with TDE, see Enable and Disable TDE on a Database .

### Preupgrade Tools

During the preupgrade process, use the following tools as required:

User Migration Tool—A standalone Windows command-line application used for all upgrades that involve a change of domain. The
                                    tool exports all existing user accounts (config/setup and supervisors) from the source domain to a .bin file. The file is used in the target domain during the upgrade.

You can download the User Migration Tool from Cisco.com by clicking ICM User Migration Tool Software .

Regutil Tool—Used in Technology Refresh upgrades, the tool exports the Cisco Systems, Inc. registry from the source machine
                                    during the preupgrade process. The output of the tool is required on the destination machine when running the Unified CCE
                                    Installer during the upgrade process.

You can
                                    				download the Regutil Tool from Cisco.com by clicking Contact Center Enterprise Tools .

Cisco Unified Intelligent Contact Management Database Administration (ICMDBA) Tool—Used to create new databases, modify or
                                    delete existing databases, and perform limited SQL Server configuration tasks.

The ICMDBA Tool is delivered with the main installer.

Domain Manager—Used to provision Active Directory.

The Domain Manager Tool is delivered with the main installer.

Upgrade.exe—Used to upgrade the schema of the logger, AW DB, HDS DB, and BA databases to a version compatible with the current
                                    Unified CCE software version. It is typically used when the installer fails to automatically upgrade the schema.

Perform the following steps to use the tool:

<ICM install directory>:\icm\bin>upgrade.exe -s <Server Name> -d <Database name> -dt <Database Type> -i <Instance Name>

Where

<Database Type> - can be either " logger " or " hds " or " aw " or " ba ", depending on the database that requires the schema to be upgraded.

## Technology Refresh Preupgrade Task flow

### Disable
                           	 Configuration Changes

Step 1

To disable
                                          			 configuration changes during the upgrade, set the following registry key to 1
                                          			 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance
                                             				name>\Router
                                             				A\Router\CurrentVersion\Configuration\Global\DBMaintenance .

Step 2

Confirm that configuration changes are disabled by attempting to save a configuration change.

When you try to save the change, a message is displayed confirming the change failure.

### Export the Server
                           	 Registry

Export the Cisco registry on each source machine that is involved in a Technology Refresh upgrade.

During the upgrade
                                 		  process, you are prompted for the path to the exported registry file location.
                                 		  Perform the following procedure and note the location of the resulting file for
                                 		  later in the upgrade process.

Each time you run
                                 		  the RegUtil with the export option, if a RegUtil_<hostname>.dat file
                                 		  exists, the utility renames that file to
                                 		  RegUtil_<hostname>.dat.bak<number>.

Ensure to run the RegUtil tool with administrative privileges.

Step 1

Open a command
                                          			 prompt and change the directory to the location where the RegUtil.exe resides.

Step 2

Run the RegUtil tool to export the Cisco Systems, Inc. registry using the following command: RegUtil -export [target directory] , for example, <ICM install directory>:\icm\bin>RegUtil -export C:\RegUtil

The target directory must have write access. Therefore, you cannot select the install media on a DVD. The target directory
                                             is optional. If it is not specified, the tool outputs the result of the Registry export to the current directory. The output
                                             filename is of the format RegUtil_<hostname>.dat, where hostname is the name of the source machine.

## Technology Refresh
                        	 Upgrade Task Flow

For the Unified CCE core components, there is a general flow for redundant systems; Sides A and B are brought down, upgraded,
                              tested, and brought back up in sequence. That sequence ensures the operation of the Cisco Contact Center during the entire
                              upgrade process.

For coresident configurations, upgrade CUIC/LiveData/IdS server along with the Unified CCE Central Controller upgrade.

For Technology
                              		  Refresh upgrades, perform the following upgrade tasks:

Task

See

Install Cloud Connect

Install Cloud Connect

If you plan to reuse the existing Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Overview for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component.

If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                          Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Queuing and self-service components

Upgrade Cisco Unified Customer Voice Portal 1

Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html

Infrastructure and media resource components

Upgrade voice and data gateways

Upgrade Voice and Data Gateways

Identity Service/SSO

Identity Service (IdS) /Single Sign-On(SSO)

SSO is an optional feature and exchanges authentication and authorization details between an identity provider (IdP) and an
                                          identity service (IdS).

Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 12.6(2) before Cisco IdS is upgraded to 12.6(2) .

For more information, see Upgrade Flowcharts .

For IdS upgrade, refer to the same steps as documented in the upgrades section of Unified Intelligence Center Installation
                                          and Upgrade Guide at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Upgrade Enterprise Chat and Email (ECE)

For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

Upgrade Finesse

For more information, see Cisco Finesse Installation and Upgrade Guide Cisco Finesse Installation and Upgrade Guide at

https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html

ES42 provides
                                                      										the ability to connect a maximum of two versions of Finesse
                                                      										to the same PG during the upgrade or migration process to
                                                      										facilitate the migration of agents and supervisors to the
                                                      										new Finesse version. However, this mode of operation is not
                                                      										supported for production use beyond the upgrade or migration
                                                      										phase.

Reporting server

Upgrade Cisco Unified Intelligence Center server

Installation and Upgrade Guide for Cisco Unified Intelligence Center at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Unified CCE Central Controller and Administration & Data Server components

Bring down Side A Logger, migrate Logger database, and upgrade Logger

Migrate the Logger Database and Upgrade the Logger

Bring down Side A Call Router, and upgrade

Upgrade Unified CCE Call Router

Upgrade Administration & Data Server connected to Side A.

Migrate the HDS Database and Upgrade the Unified CCE Administration & Data Server

Bring Side A Logger and Call Router into service, bring down Side B Logger and Call Router

Bring Upgraded Side A into Service

Migrate Side B Logger database and upgrade Logger

Migrate the Logger Database and Upgrade the Logger

Upgrade Side B Call Router

Upgrade Unified CCE Call Router

Bring Side B Call Router into service and verify operation

Verify Operation of Upgraded Side B Call Router and Logger

Bring Side B Logger into service and verify operation.

Upgrade Administration & Data Server connected to Side B.

Migrate the HDS Database and Upgrade the Unified CCE Administration & Data Server

Upgrade Cisco Unified Intelligence Center reporting templates

Installation and Upgrade Guide for Cisco Unified Intelligence Center at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Upgrade Cisco Unified Contact Center Management Portal

Upgrading Dual Sided Unified CCMP at

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

Upgrade Administration Client

Upgrade Unified CCE Administration Client

Database Performance Enhancement

Database Performance Enhancement

Unified CCE Peripheral Gateways and associated components

Upgrade PGs

Upgrade Peripheral Gateways

Upgrade Customer Collaboration Platform

Cisco Customer Collaboration Platform User Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html .

Upgrade Outbound Option Dialer (if applicable)

Upgrade Outbound Option Dialer

Upgrade CTI OS server

CTI OS System Manager Guide for Cisco Unified ICM at

https://www.cisco.com/c/en/us/support/customer-collaboration/computer-telephony-integration-option/products-installation-guides-list.html

Desktop Client components

Upgrade CTI OS Agent and Supervisor Desktops

CTI OS System Manager Guide for Cisco Unified ICM at

https://www.cisco.com/c/en/us/support/customer-collaboration/computer-telephony-integration-option/products-installation-guides-list.html

Call Processing components

Upgrade Cisco Unified Communications Manager

Upgrade Guide for Cisco
                                                   				  Unified Communications Manager at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/tsd-products-support-install-and-upgrade-technotes-list.html

(Install) the JTAPI client on the Cisco Unified Communications Manager PG

Upgrade Cisco JTAPI Client on PG

## Technology Refresh Upgrade Tasks

The following section provides instructions about upgrading Unified CCE components. For instructions about upgrading non-Unified
                              CCE components in a Unified CCE solution, see the links to component-specific documents in the Technology Refresh Upgrade Task Flow .

The EDMT tool migrates the CCE database along with its associated users, which are considered database-level objects which
                                    is similar to Microsoft SQL Server backup and restore functionality, includes only database-level users. SQL Server-level
                                    logins from the source of SQL Server are not transferred to destination SQL Server as part of migration.

After the initial EDMT migration, administrators who wish to maintain identical logins and passwords on both the source and
                                    destination of SQL Server must follow Microsoft’s recommended procedure for transferring server-level logins.

The procedure to transfer server-level logins is required to be executed only once, immediately after the first time EDMT
                                    migration and does not need to be repeated for subsequent EDMT runs used for database synchronization before or during cutover.
                                    For detailed instructions on SQL Server-level logins migration, refer to https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/security/transfer-logins-passwords-between-instances .

During EDMT re-run is performed before or during cutover, any mappings for new users added to the destination database after
                                    the initial EDMT migration will be removed, This is an expected behaviour when using SQL Server backup and restore functionality.

ACTION : Administrators must re-map the appropriate SQL logins to the corresponding database users after EDMT rerun.

### Migrate the Logger
                           	 Database and Upgrade the Logger

To upgrade the Logger, do the following tasks:

Migrate the Logger database.

If you use Outbound Option High Availability, do the following:

Migrate the Outbound Option database.

For the enhancements in Outbound Option High Availability to work effectively, Outbound Option High Availability must be disabled
                                             before the logger upgrade and then enabled after the upgrade. For more information, see Disable Outbound Options High Availability (If Applicable) .

Install the new software.

#### Before you begin

Create a shared folder in any desired location. Ensure that:

In the Properties window > Sharing tab > Advanced Sharing, the Share this folder check box is checked.

In the Properties window > Security tab > Advanced Sharing > Permission , the permission level is set as Full control for the user group everyone .

Step 1

Use Unified CCE Service Control to stop all Unified CCE services on the Logger.

Step 2

(Optional) If Outbound Option High Availability is deployed, disable Outbound Options High Availability. For details, see Disable Outbound Options High Availability (If Applicable) .

Step 3

Download the EDMT tool from Cisco.com , and ensure prerequisites for the same are installed on the target/destination system, before launching EDMT. These include
                                          the ODBC Driver 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015.

Step 4

Run the EDMT from the server that will host the destination Logger and click Next .

Step 5

Select Technology Refresh and click Next .

Step 6

Under Source Database Connection , in the HostName\IP Address field, type the Source IP and click Refresh Database List .

Step 7

Select the Logger Database name, and click Next .

Step 8

In the Windows Share Name field, type the name of the shared folder that you created.

Step 9

In the Windows Share Password field, type the password of the destination machine, and click Next .

Step 10

Review or change the information as required and click Start Migration .

Step 11

Exit the EDMT.

Set the TempDB AutoGrowth of Data files to 100 MB manually.

Step 12

(Optional) If Outbound Option High Availability is deployed, repeat steps 1
                                          					through 12 to
                                          					migrate the BA database.

Step 13

Launch the ICM-CCE-Installer and click Next .

Step 14

Select Technology Refresh and click Next .

Step 15

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 16

To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 17

(Optional) Select SQL Server Security Hardening and click Next .

SQL Security Hardening shouldn't be applied during installation of Windows Server 2019 and SQL Server 2019. SQL Security Hardening
                                                         can be applied post installation using the Security Wizard tool.

Step 18

Click OK on any informational messages that display.

Step 19

Click Install .

Step 20

Restart the server when the upgrade completes.

Step 21

Open the Web Setup tool from the desktop shortcut.

Step 22

Edit the instance as necessary.

Step 23

(Optional) In case of Cross Domain upgrade, launch Web Setup , select instance and click on Change Domain to use the new domain for destination Unified CCE.

Edit instance and you might need to change the facility or instance number if required.

Step 24

(Optional) If you use Outbound Option High Availability, enable Outbound Option High Availability in the Web Setup tool. For
                                          details, see the Configure the Logger for Outbound Option topic in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

Step 25

Edit the Logger component as necessary.

Edit the Logger component. In the Summary window, update the service account management section, with a pre-existing domain user that the Logger service would run
                                             under.

If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information.

Caution

Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B.

Step 26

(Optional) If it's a Cross Domain upgrade, use the User Migration tool to import the users and OU information which you exported
                                          from the source machine during the pre-upgrade process. See User Migration Tool in Preupgrade Overview .

Step 27

Use Unified CCE Service Control to set all Unified CCE services on the new Logger to Manual Start.

### Upgrade Unified CCE Call Router

To upgrade the Call Router, do the following tasks:

Import the Cisco registry information.

Install the new software.

Set up the new Call Router using the Web Setup tool.

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

Select Technology Refresh and click Next .

Step 3

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 4

To apply the Unified ICM Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 5

Click OK on any informational messages that display.

Step 6

Click Install .

Step 7

Restart the server when the upgrade completes.

Step 8

Open the Web Setup tool from the desktop shortcut.

Step 9

Edit the instance as necessary.

For a domain change, change the domain of the instance. Additionally, you might need to change the facility or instance number
                                             as required.

Step 10

Edit the Call Router component as necessary.

If there are references to out-of-date network interfce names or IP addresses for the public and private networks for the
                                             Router, update this information.

Step 11

Use Unified CCE Service Control to set all Unified CCE services on the new Call Router to Manual Start.

### Migrate the HDS Database and Upgrade the Unified CCE Administration & Data Server

To upgrade the Administration & Data Server, do the following tasks:

Migrate the HDS database (if applicable. Non-HDS configurations do not require this action.)

Import the Cisco registry information.

Install the new software.

Set up the new Administration & Data Server through the Web Setup tool.

The Installer upgrades the AW database that is associated with the Administration & Data server. The EDMT does not upgrade
                                 the AW database.

#### Before you begin

Create a shared folder in any desired location. Ensure that:

In the Properties window > Sharing tab > Advanced Sharing, the Share this folder check box is checked.

In the Properties window > Security tab > Advanced Sharing > Permission , the permission level is set as Full control for the user group everyone .

Step 1

Use Unified CCE Service Control to stop all Unified CCE services on the server.

Step 2

Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. These
                                          include the ODBC Driver 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015.

Step 3

Launch the EDMT tool on the destination server that hosts the Administration and Data Server with HDS database and click Next . For non-HDS Server configurations, skip to step 11.

Step 4

Select Technology Refresh and click Next .

Step 5

Under Source Database Connection , in the HostName\IP Address field, type the Source IP, and click Refresh Database List .

Step 6

Under Destination Database Connection , in the SQL Server Port Number field, enter the destination SQL server port number, and then click Next .

Step 7

Select the HDS Database name, and click Next .

Step 8

In the Windows Share Name field, type the name of the shared folder that you created.

Step 9

In the Windows Share Password field, type the password of the destination machine, and click Next .

Step 10

Review or change the information as required, highlight the HDS database, and click Start Migration .

Step 11

Exit the EDMT .

Set the TempDB AutoGrowth of Data files to 100 MB manually.

Step 12

Launch the ICM-CCE-Installer and click Next .

Step 13

Select Technology Refresh and click Next .

Step 14

Click Browse and specify the path for the RegUtil file you exported from the source machine
                                          					during the preupgrade process.

Step 15

To apply the Unified ICM Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 16

(Optional) Select SQL Server Security Hardening and click Next .

SQL Security Hardening should not be applied during installation of
                                                         							Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                         							applied post installation using the Security Wizard tool.

Step 17

Click OK on any informational messages that display.

Step 18

Click Install .

Step 19

Restart the server when the upgrade completes.

Step 20

Open the Web Setup tool from the desktop shortcut.

Step 21

Edit the instance as necessary.

Step 22

(Optional) In case of Cross Domain upgrade, launch Websetup , select the instance and click on Change Domain in order to use the new domain for destination Unified CCE.

Edit the instance. You might need to change the facility or instance number if required.

Step 23

Edit the Administration & Data Server component as necessary and in the Summary window, update the Service Account manager with the domain user to perform the service operation.

If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information.

Caution

Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B.

For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine .

Step 24

Use Unified CCE Service Control to set all Unified CCE services on the new Administration & Data Server to Manual Start.

Step 25

Start the Unified CCE services for Logger and Router on both Side A and Side B. Also, start the Distributor service for the
                                          all sites. Then, launch the Configuration Manager tool to check if it is working fine.

During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, Unified CCE services should be started only
                                                         after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed.

If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                         Side B Destination machines if both the sides have been migrated successfully.

### Synchronizing or Updating Configuration and Historical Data from Production Server to Staged Server During Cut Over

You can use the EDMT tool to migrate data from a Logger or HDS production server, to the
                              one that has already been staged on version 12.5(x). These two pronged upgrade steps are
                              typically performed to reduce the downtime needed during cut-over to the new version.
                              While the parallel 12.5(x) systems are staged and tested, the 12.0(1)/12.5(x) production
                              servers continue to process calls. On the day of the cut-over, the data in the
                              12.5(x)staged servers, can be updated or synchronized with that of the production
                              server, by running the 12.5(x) EDMT tool, for each of the Logger and HDS database. Stop
                              the Logger, AW-HDS, and Apache Tomcat services on 12.5(x) staged systems, before running
                              EDMT tool while changing over to synchronize.

### Upgrade Peripheral Gateways

You can upgrade different Peripheral Gateways (PG) within a contact center at different times within different maintenance
                                 windows. However, upgrade all PGs that reside on the same virtual machine and redundant PGs (Side A and corresponding Side
                                 B) during the same maintenance window.

The following dependencies occur when upgrading the Unified Communications Manager PG:

If your contact center uses the CTI OS component, upgrade the CTI OS server at the same time as the associated Unified Communications Manager PG .

If your contact center uses Outbound Option, upgrade any Outbound Option Dialers associated with Unified Communications Manager
                                       PGs at the same time.

If the Unified Communications Manager application is upgraded, upgrade the JTAPI client associated with the Unified Communications
                                       Manager PG at the same time.

Step 1

Use Unified CCE Service Control to stop all Unified CCE and CTI OS (if applicable when upgrading the Unified Communications Manager PG ) services on the PG server. Change the services to Manual Start.

Step 2

Launch the ICM-CCE-Installer and click Next .

Step 3

(Optional) To apply the Unified ICM Minor Minor/Maintenance Release, click Browse and navigate to the Minor Minor/Maintenance Release software. Click Next .

Step 4

Select Technology Refresh and click Next .

Step 5

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

The registry information for the Unified Communications Manager PG also contains information for the CTI OS server (if applicable).

Step 6

Click OK on any informational messages that display.

Step 7

Click Install .

Step 8

Reboot the system after the upgrade completes.

Step 9

After reboot, open the Peripheral Gateway Setup tool from the desktop shortcut and make any necessary changes. See the "Install"
                                          section of this document for specific information.

If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information.

Step 10

Open the Peripheral Gateway Setup tool from the Installer dialog box or desktop shortcut and edit the Dialer as required.

During Peripheral Gateway installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step-11
                                                         only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed.

Step 11

Use Unified CCE Service Control to set all Unified CCE services to Automatic Start.

### Upgrade Outbound
                           	 Option Dialer

To upgrade the Outbound Option Dialer, import the Cisco registry information, install the new software, and set up the new
                                 Dialer using the PG Setup tool.

#### Before you begin

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

(Optional) To apply any Maintenance Releases, click Browse and navigate to the Maintenance Release software. Click Next .

Step 3

Select Technology Refresh and click Next .

Step 4

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 5

Click OK on any informational messages that display.

Step 6

Click Install .

Step 7

Reboot the
                                          			 system after the upgrade completes.

Step 8

Open the Peripheral Gateway Setup tool from the Installer dialog box or desktop shortcut and edit the Dialer as required.

During Unified CCE installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step 9 only after
                                                         Unified ICM 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed.

Step 9

Use Unified CCE Service Control to set all Unified CCE services to Automatic
                                          					Start.

### Upgrade Unified CCE Administration Client

There’s no support for Administration Clients to be upgraded via Technology Refresh upgrade. Either perform an in-place common
                                 ground upgrade of Administration Clients, and make edits as necessary using the Administration Client setup, or perform a
                                 fresh installation of Administration Client on a new system.

To upgrade the Operating System from Windows 10 to Windows 11, you must follow the Unified CCE Virtualisation to get the Latest OVA configuration details. Modify the VM specifications for Windows 11. For Windows 11, the SecureBoot
                                             and TPM devices are mandatory which must be added before upgrading the OS from Windows 10 to Windows 11.

| Note | During the Technology Refresh (TR) Upgrade process, the installer is designed to identify any unsupported features present
                                       in the source deployment. These features are then listed in a dialog box for you to review. You have two options on how to
                                       proceed: Select "Yes": By choosing "Yes", you instruct the installer to exclude all the identified unsupported features during the
                                             upgrade process. The installer will proceed with the Technology Refresh Upgrade, ensuring that the unsupported features do
                                             not interfere with the updated system functionality. Select "No": If you choose "No", the installer will terminate immediately without making any changes to the deployment. For more information about the list of unsupported features, see the Removed and Unsupported Features topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html |
|---|---|

| Note | If you need to upgrade from version 12.6(2) to 15.0(1) to leverage the capabilities of graceful shutdown, you must first install
                                       12.6(2) ES53 before proceeding with the upgrade to 15.0(1). For more information about the router graceful shutdown, see the Unified CCE Router graceful shutdown topic in the Administration Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) . |
|---|---|

| Note | During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, SQL Server Security Hardening optional configuration
                                       should not be selected as part of an installation. SQL Security Hardening should be applied post Unified CCE installation
                                       using the Security Wizard tool. Unified CCE services should be started only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
|---|---|

| Note | If AppDynamics Monitoring was enabled on the ICM source machine, it will not be automatically enabled based on the source
                                       machine’s configuration during the Technology Refresh Upgrade. For deployments using AppDynamics for monitoring, it is necessary
                                       to manually configure and enable performance monitoring on the destination machines after completing the Technology Refresh
                                       Upgrade. |
|---|---|

| Note | Ensure that Internet Information Services (IIS) is disabled on Windows Server before installing Unified CCE software with
                                       the ICM-CCE-Installer. |
|---|---|

| Note | If the system is enabled with TDE, see Enable and Disable TDE on a Database . |
|---|---|

| Step 1 | To disable
                                          			 configuration changes during the upgrade, set the following registry key to 1
                                          			 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance
                                             				name>\Router
                                             				A\Router\CurrentVersion\Configuration\Global\DBMaintenance . |
|---|---|
| Step 2 | Confirm that configuration changes are disabled by attempting to save a configuration change. When you try to save the change, a message is displayed confirming the change failure. |

| Note | Ensure to run the RegUtil tool with administrative privileges. |
|---|---|

| Step 1 | Open a command
                                          			 prompt and change the directory to the location where the RegUtil.exe resides. |
|---|---|
| Step 2 | Run the RegUtil tool to export the Cisco Systems, Inc. registry using the following command: RegUtil -export [target directory] , for example, <ICM install directory>:\icm\bin>RegUtil -export C:\RegUtil The target directory must have write access. Therefore, you cannot select the install media on a DVD. The target directory
                                             is optional. If it is not specified, the tool outputs the result of the Registry export to the current directory. The output
                                             filename is of the format RegUtil_<hostname>.dat, where hostname is the name of the source machine. |

| Note | For coresident configurations, upgrade CUIC/LiveData/IdS server along with the Unified CCE Central Controller upgrade. |
|---|---|

| Task | See |
|---|---|
| Cisco Reverse Proxy Components |
| Cloud Connection Components |
| Install Cloud Connect | Install Cloud Connect If you plan to reuse the existing Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Overview for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component. If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                          Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| Queuing and self-service components |
| Upgrade Cisco Unified Customer Voice Portal 1 | Note Before you upgrade to Unified CVP 12.5 , the ES84 patch has to be applied to Cisco VVB 11.6 in order to maintain compatibility between Unified CVP 12.5 and Cisco VVB 11.6. Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html | Note | Before you upgrade to Unified CVP 12.5 , the ES84 patch has to be applied to Cisco VVB 11.6 in order to maintain compatibility between Unified CVP 12.5 and Cisco VVB 11.6. |
| Note | Before you upgrade to Unified CVP 12.5 , the ES84 patch has to be applied to Cisco VVB 11.6 in order to maintain compatibility between Unified CVP 12.5 and Cisco VVB 11.6. |
| Infrastructure and media resource components |
| Upgrade voice and data gateways | Upgrade Voice and Data Gateways |
| Identity Service/SSO |
| Identity Service (IdS) /Single Sign-On(SSO) | SSO is an optional feature and exchanges authentication and authorization details between an identity provider (IdP) and an
                                          identity service (IdS). Note Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 12.6(2) before Cisco IdS is upgraded to 12.6(2) . For more information, see Upgrade Flowcharts . For IdS upgrade, refer to the same steps as documented in the upgrades section of Unified Intelligence Center Installation
                                          and Upgrade Guide at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html | Note | Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 12.6(2) before Cisco IdS is upgraded to 12.6(2) . |
| Note | Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 12.6(2) before Cisco IdS is upgraded to 12.6(2) . |
| Upgrade Enterprise Chat and Email (ECE) | For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| Upgrade Finesse | For more information, see Cisco Finesse Installation and Upgrade Guide Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html Note ES42 provides
                                                      										the ability to connect a maximum of two versions of Finesse
                                                      										to the same PG during the upgrade or migration process to
                                                      										facilitate the migration of agents and supervisors to the
                                                      										new Finesse version. However, this mode of operation is not
                                                      										supported for production use beyond the upgrade or migration
                                                      										phase. | Note | ES42 provides
                                                      										the ability to connect a maximum of two versions of Finesse
                                                      										to the same PG during the upgrade or migration process to
                                                      										facilitate the migration of agents and supervisors to the
                                                      										new Finesse version. However, this mode of operation is not
                                                      										supported for production use beyond the upgrade or migration
                                                      										phase. |
| Note | ES42 provides
                                                      										the ability to connect a maximum of two versions of Finesse
                                                      										to the same PG during the upgrade or migration process to
                                                      										facilitate the migration of agents and supervisors to the
                                                      										new Finesse version. However, this mode of operation is not
                                                      										supported for production use beyond the upgrade or migration
                                                      										phase. |
| Reporting server |
| Upgrade Cisco Unified Intelligence Center server | Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Unified CCE Central Controller and Administration & Data Server components |
| Note To perform upgrade from 12.5(x) to 12.6(2) or from 12.6(1) to 12.6(2), refer Upgrade CCE Minor/Maintenance Release Software. | Note | To perform upgrade from 12.5(x) to 12.6(2) or from 12.6(1) to 12.6(2), refer Upgrade CCE Minor/Maintenance Release Software. |
| Note | To perform upgrade from 12.5(x) to 12.6(2) or from 12.6(1) to 12.6(2), refer Upgrade CCE Minor/Maintenance Release Software. |
| Bring down Side A Logger, migrate Logger database, and upgrade Logger | Migrate the Logger Database and Upgrade the Logger |
| Bring down Side A Call Router, and upgrade | Upgrade Unified CCE Call Router |
| Upgrade Administration & Data Server connected to Side A. | Migrate the HDS Database and Upgrade the Unified CCE Administration & Data Server |
| Bring Side A Logger and Call Router into service, bring down Side B Logger and Call Router | Bring Upgraded Side A into Service |
| Migrate Side B Logger database and upgrade Logger | Migrate the Logger Database and Upgrade the Logger |
| Upgrade Side B Call Router | Upgrade Unified CCE Call Router |
| Bring Side B Call Router into service and verify operation | Verify Operation of Upgraded Side B Call Router and Logger |
| Bring Side B Logger into service and verify operation. |
| Upgrade Administration & Data Server connected to Side B. | Migrate the HDS Database and Upgrade the Unified CCE Administration & Data Server |
| Upgrade Cisco Unified Intelligence Center reporting templates | Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Upgrade Cisco Unified Contact Center Management Portal | Upgrading Dual Sided Unified CCMP at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| Upgrade Administration Client | Upgrade Unified CCE Administration Client |
| Database Performance Enhancement | Database Performance Enhancement |
| Unified CCE Peripheral Gateways and associated components |
| Upgrade PGs | Upgrade Peripheral Gateways |
| Upgrade Customer Collaboration Platform | Cisco Customer Collaboration Platform User Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html . |
| Upgrade Outbound Option Dialer (if applicable) | Upgrade Outbound Option Dialer |
| Upgrade CTI OS server | CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/computer-telephony-integration-option/products-installation-guides-list.html |
| Desktop Client components |
| Upgrade CTI OS Agent and Supervisor Desktops | CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/computer-telephony-integration-option/products-installation-guides-list.html |
| Call Processing components |
| Upgrade Cisco Unified Communications Manager | Upgrade Guide for Cisco
                                                   				  Unified Communications Manager at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/tsd-products-support-install-and-upgrade-technotes-list.html |
| (Install) the JTAPI client on the Cisco Unified Communications Manager PG | Upgrade Cisco JTAPI Client on PG |

| Note | Before you upgrade to Unified CVP 12.5 , the ES84 patch has to be applied to Cisco VVB 11.6 in order to maintain compatibility between Unified CVP 12.5 and Cisco VVB 11.6. |
|---|---|

| Note | Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 12.6(2) before Cisco IdS is upgraded to 12.6(2) . |
|---|---|

| Note | ES42 provides
                                                      										the ability to connect a maximum of two versions of Finesse
                                                      										to the same PG during the upgrade or migration process to
                                                      										facilitate the migration of agents and supervisors to the
                                                      										new Finesse version. However, this mode of operation is not
                                                      										supported for production use beyond the upgrade or migration
                                                      										phase. |
|---|---|

| Note | To perform upgrade from 12.5(x) to 12.6(2) or from 12.6(1) to 12.6(2), refer Upgrade CCE Minor/Maintenance Release Software. |
|---|---|

| Note | If the user group everyone is not available, add it using the Add button. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE services on the Logger. |
|---|---|
| Step 2 | (Optional) If Outbound Option High Availability is deployed, disable Outbound Options High Availability. For details, see Disable Outbound Options High Availability (If Applicable) . |
| Step 3 | Download the EDMT tool from Cisco.com , and ensure prerequisites for the same are installed on the target/destination system, before launching EDMT. These include
                                          the ODBC Driver 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015. |
| Step 4 | Run the EDMT from the server that will host the destination Logger and click Next . |
| Step 5 | Select Technology Refresh and click Next . |
| Step 6 | Under Source Database Connection , in the HostName\IP Address field, type the Source IP and click Refresh Database List . |
| Step 7 | Select the Logger Database name, and click Next . |
| Step 8 | In the Windows Share Name field, type the name of the shared folder that you created. |
| Step 9 | In the Windows Share Password field, type the password of the destination machine, and click Next . |
| Step 10 | Review or change the information as required and click Start Migration . |
| Step 11 | Exit the EDMT. Note Set the TempDB AutoGrowth of Data files to 100 MB manually. | Note | Set the TempDB AutoGrowth of Data files to 100 MB manually. |
| Note | Set the TempDB AutoGrowth of Data files to 100 MB manually. |
| Step 12 | (Optional) If Outbound Option High Availability is deployed, repeat steps 1
                                          					through 12 to
                                          					migrate the BA database. |
| Step 13 | Launch the ICM-CCE-Installer and click Next . |
| Step 14 | Select Technology Refresh and click Next . |
| Step 15 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 16 | To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 17 | (Optional) Select SQL Server Security Hardening and click Next . Note SQL Security Hardening shouldn't be applied during installation of Windows Server 2019 and SQL Server 2019. SQL Security Hardening
                                                         can be applied post installation using the Security Wizard tool. | Note | SQL Security Hardening shouldn't be applied during installation of Windows Server 2019 and SQL Server 2019. SQL Security Hardening
                                                         can be applied post installation using the Security Wizard tool. |
| Note | SQL Security Hardening shouldn't be applied during installation of Windows Server 2019 and SQL Server 2019. SQL Security Hardening
                                                         can be applied post installation using the Security Wizard tool. |
| Step 18 | Click OK on any informational messages that display. |
| Step 19 | Click Install . |
| Step 20 | Restart the server when the upgrade completes. |
| Step 21 | Open the Web Setup tool from the desktop shortcut. |
| Step 22 | Edit the instance as necessary. |
| Step 23 | (Optional) In case of Cross Domain upgrade, launch Web Setup , select instance and click on Change Domain to use the new domain for destination Unified CCE. Edit instance and you might need to change the facility or instance number if required. |
| Step 24 | (Optional) If you use Outbound Option High Availability, enable Outbound Option High Availability in the Web Setup tool. For
                                          details, see the Configure the Logger for Outbound Option topic in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html . |
| Step 25 | Edit the Logger component as necessary. Edit the Logger component. In the Summary window, update the service account management section, with a pre-existing domain user that the Logger service would run
                                             under. If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information. Note Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. Caution Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. | Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. | Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
| Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. |
| Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
| Step 26 | (Optional) If it's a Cross Domain upgrade, use the User Migration tool to import the users and OU information which you exported
                                          from the source machine during the pre-upgrade process. See User Migration Tool in Preupgrade Overview . |
| Step 27 | Use Unified CCE Service Control to set all Unified CCE services on the new Logger to Manual Start. |

| Note | Set the TempDB AutoGrowth of Data files to 100 MB manually. |
|---|---|

| Note | SQL Security Hardening shouldn't be applied during installation of Windows Server 2019 and SQL Server 2019. SQL Security Hardening
                                                         can be applied post installation using the Security Wizard tool. |
|---|---|

| Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. |
|---|---|

| Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
|---|---|

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | Select Technology Refresh and click Next . |
| Step 3 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 4 | To apply the Unified ICM Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 5 | Click OK on any informational messages that display. |
| Step 6 | Click Install . |
| Step 7 | Restart the server when the upgrade completes. |
| Step 8 | Open the Web Setup tool from the desktop shortcut. |
| Step 9 | Edit the instance as necessary. For a domain change, change the domain of the instance. Additionally, you might need to change the facility or instance number
                                             as required. |
| Step 10 | Edit the Call Router component as necessary. If there are references to out-of-date network interfce names or IP addresses for the public and private networks for the
                                             Router, update this information. |
| Step 11 | Use Unified CCE Service Control to set all Unified CCE services on the new Call Router to Manual Start. |

| Note | If the user group everyone is not available, add it using the Add button. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE services on the server. |
|---|---|
| Step 2 | Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. These
                                          include the ODBC Driver 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015. |
| Step 3 | Launch the EDMT tool on the destination server that hosts the Administration and Data Server with HDS database and click Next . For non-HDS Server configurations, skip to step 11. |
| Step 4 | Select Technology Refresh and click Next . |
| Step 5 | Under Source Database Connection , in the HostName\IP Address field, type the Source IP, and click Refresh Database List . |
| Step 6 | Under Destination Database Connection , in the SQL Server Port Number field, enter the destination SQL server port number, and then click Next . |
| Step 7 | Select the HDS Database name, and click Next . |
| Step 8 | In the Windows Share Name field, type the name of the shared folder that you created. |
| Step 9 | In the Windows Share Password field, type the password of the destination machine, and click Next . |
| Step 10 | Review or change the information as required, highlight the HDS database, and click Start Migration . |
| Step 11 | Exit the EDMT . Note Set the TempDB AutoGrowth of Data files to 100 MB manually. | Note | Set the TempDB AutoGrowth of Data files to 100 MB manually. |
| Note | Set the TempDB AutoGrowth of Data files to 100 MB manually. |
| Step 12 | Launch the ICM-CCE-Installer and click Next . |
| Step 13 | Select Technology Refresh and click Next . |
| Step 14 | Click Browse and specify the path for the RegUtil file you exported from the source machine
                                          					during the preupgrade process. |
| Step 15 | To apply the Unified ICM Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 16 | (Optional) Select SQL Server Security Hardening and click Next . Note SQL Security Hardening should not be applied during installation of
                                                         							Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                         							applied post installation using the Security Wizard tool. | Note | SQL Security Hardening should not be applied during installation of
                                                         							Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                         							applied post installation using the Security Wizard tool. |
| Note | SQL Security Hardening should not be applied during installation of
                                                         							Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                         							applied post installation using the Security Wizard tool. |
| Step 17 | Click OK on any informational messages that display. |
| Step 18 | Click Install . |
| Step 19 | Restart the server when the upgrade completes. |
| Step 20 | Open the Web Setup tool from the desktop shortcut. |
| Step 21 | Edit the instance as necessary. |
| Step 22 | (Optional) In case of Cross Domain upgrade, launch Websetup , select the instance and click on Change Domain in order to use the new domain for destination Unified CCE. Edit the instance. You might need to change the facility or instance number if required. |
| Step 23 | Edit the Administration & Data Server component as necessary and in the Summary window, update the Service Account manager with the domain user to perform the service operation. If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information. Note Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. Caution Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine . | Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. | Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
| Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. |
| Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
| Step 24 | Use Unified CCE Service Control to set all Unified CCE services on the new Administration & Data Server to Manual Start. |
| Step 25 | Start the Unified CCE services for Logger and Router on both Side A and Side B. Also, start the Distributor service for the
                                          all sites. Then, launch the Configuration Manager tool to check if it is working fine. Note During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, Unified CCE services should be started only
                                                         after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. Note The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                      size, the longer it takes to migrate) and the server hardware performance level. Note If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                         Side B Destination machines if both the sides have been migrated successfully. | Note | During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, Unified CCE services should be started only
                                                         after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. | Note | The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                      size, the longer it takes to migrate) and the server hardware performance level. | Note | If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                         Side B Destination machines if both the sides have been migrated successfully. |
| Note | During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, Unified CCE services should be started only
                                                         after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
| Note | The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                      size, the longer it takes to migrate) and the server hardware performance level. |
| Note | If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                         Side B Destination machines if both the sides have been migrated successfully. |

| Note | Set the TempDB AutoGrowth of Data files to 100 MB manually. |
|---|---|

| Note | SQL Security Hardening should not be applied during installation of
                                                         							Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                         							applied post installation using the Security Wizard tool. |
|---|---|

| Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. |
|---|---|

| Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
|---|---|

| Note | During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, Unified CCE services should be started only
                                                         after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
|---|---|

| Note | The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                      size, the longer it takes to migrate) and the server hardware performance level. |
|---|---|

| Note | If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                         Side B Destination machines if both the sides have been migrated successfully. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE and CTI OS (if applicable when upgrading the Unified Communications Manager PG ) services on the PG server. Change the services to Manual Start. |
|---|---|
| Step 2 | Launch the ICM-CCE-Installer and click Next . |
| Step 3 | (Optional) To apply the Unified ICM Minor Minor/Maintenance Release, click Browse and navigate to the Minor Minor/Maintenance Release software. Click Next . |
| Step 4 | Select Technology Refresh and click Next . |
| Step 5 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. The registry information for the Unified Communications Manager PG also contains information for the CTI OS server (if applicable). |
| Step 6 | Click OK on any informational messages that display. |
| Step 7 | Click Install . |
| Step 8 | Reboot the system after the upgrade completes. |
| Step 9 | After reboot, open the Peripheral Gateway Setup tool from the desktop shortcut and make any necessary changes. See the "Install"
                                          section of this document for specific information. If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information. |
| Step 10 | Open the Peripheral Gateway Setup tool from the Installer dialog box or desktop shortcut and edit the Dialer as required. Note During Peripheral Gateway installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step-11
                                                         only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. | Note | During Peripheral Gateway installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step-11
                                                         only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
| Note | During Peripheral Gateway installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step-11
                                                         only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
| Step 11 | Use Unified CCE Service Control to set all Unified CCE services to Automatic Start. |

| Note | During Peripheral Gateway installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step-11
                                                         only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
|---|---|

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | (Optional) To apply any Maintenance Releases, click Browse and navigate to the Maintenance Release software. Click Next . |
| Step 3 | Select Technology Refresh and click Next . |
| Step 4 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 5 | Click OK on any informational messages that display. |
| Step 6 | Click Install . |
| Step 7 | Reboot the
                                          			 system after the upgrade completes. |
| Step 8 | Open the Peripheral Gateway Setup tool from the Installer dialog box or desktop shortcut and edit the Dialer as required. Note During Unified CCE installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step 9 only after
                                                         Unified ICM 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. | Note | During Unified CCE installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step 9 only after
                                                         Unified ICM 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
| Note | During Unified CCE installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step 9 only after
                                                         Unified ICM 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
| Step 9 | Use Unified CCE Service Control to set all Unified CCE services to Automatic
                                          					Start. |

| Note | During Unified CCE installation on Windows Server 2019, Unified CCE services to be set to Automatic Start in Step 9 only after
                                                         Unified ICM 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
|---|---|

| Note | To upgrade the Operating System from Windows 10 to Windows 11, you must follow the Unified CCE Virtualisation to get the Latest OVA configuration details. Modify the VM specifications for Windows 11. For Windows 11, the SecureBoot
                                             and TPM devices are mandatory which must be added before upgrading the OS from Windows 10 to Windows 11. |
|---|---|