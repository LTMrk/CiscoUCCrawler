---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-installation-guide-pcce-b-cisco-192c6a2251
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/installation/guide/pcce_b_cisco-pcce-installationandupgrade-guide-12_5/pcce_b_cisco-pcce-installationandupgrade-guide-12_5_chapter_01001.html
retrieved_at: 2026-08-21T16:39:22.593699+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: February 4, 2020

Chapter: Technology Refresh Upgrade Process

## Chapter: Technology Refresh Upgrade Process

# Technology Refresh Upgrade Process

Single-stage upgrade: set up all virtual machines (VMs) required for a Packaged CCE solution (rebuild) on a different hardware.

Multistage upgrade: set up or upgrade the required set of components on a different hardware.

Deploy components as per your requirements.

Migrate CCE databases using the Enhanced Database Migration Tool (EDMT) and upgrade the CCE components. You can upgrade the
                                 other solution components also.

Update the IP address or hostname of components.

Synchronize components and complete the upgrade on the destination server.

## Upgrade Path

Packaged CCE 12.0(1) to Packaged CCE 12.5(1)

Packaged CCE 12.5(1) to Packaged CCE 12.5(2)

To enable the Technology Refresh upgrade support in 12.5(1), install
                                          ICM_12.5(1)_ES12 on the 12.5(1) target system.

## Prerequisites and Important Considerations

You can upgrade to Cisco Packaged CCE 2000, 4000, and 12000 Agent deployments as per the supported upgrade path.

Components must be upgraded as per the supported versions detailed in the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

Before upgrading the Unified CCE Central Controller, do the following:

In the Unified CCE Router of the source server, Disable Configuration Changes .

Disable Outbound Option High Availability (if applicable) before the logger upgrade. For details, see Disable Outbound Options High Availability (If Applicable)

In the Unified CCE Rogger, AW-HDS-DDS, and Peripheral Gateways of the source server, Export the Server Registry .

Before you upgrade the Live Data server, check the Check and upgrade VMware Tools before each power on box in the VM's Options > Edit Settings .

For more information on VMware Tools upgrade, see the VMware documentation.

In Technology Refresh upgrade, both source and destination servers must be on the same domain.

This release contains an updated database schema. During the upgrade process, perform a schema upgrade using the Enhanced
                                 Database Migration Tool (EDMT).

For the upgrade utilities, see https://software.cisco.com/download/type.html?mdfid=268439622

If you are moving the existing VMs, take the required backups of components on both Side A and Side B before you begin your
                                 upgrade. You can take a snapshot of the virtual machines on which you are performing an upgrade.

If you already have a Customer Collaboration Platform added in the remote site, it is recommended to delete the Customer Collaboration Platform from the remote site and add it as an external machine in the Main site , before upgrade . For more information on how to delete and add an external machine, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Make sure that you are running the minimum supported version of ESXi. For information about supported ESXi versions, see the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html .

### NTP Configuration
                           	 Requirements

Packaged CCE relies on time synchronization.
                                 		  Properly configuring NTP is critical for reliability of reporting data and
                                 		  cross-component communication. It's important to implement the requirements
                                 		  outlined in NTP and Time Synchronization .

## Upgrade Tools

During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, SQL Server
                                       				Security Hardening optional configuration should not be selected as part of
                                       				installation. SQL Security Hardening should be applied post Unified CCE installation
                                       				using Security Wizard tool.

Unified CCE services should be started only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed.

During the upgrade process, use the following tools:

ICM-CCE-Installer—The main Unified CCE Installer. It copies all files into relevant folders, creates the base registries,
                                    and installs needed third-party software such as JRE, Apache Tomcat, and Microsoft .NET Framework.

You cannot run the installer remotely. Mount the installer ISO file only to a local machine.

Enhanced Database Migration Tool (EDMT)—A wizard application that is used for upgrades to migrate the Logger, BA, AW, and
                                    HDS databases.

You can download the EDMT from Cisco.com by clicking Cisco Enhanced Data Migration Tool Software Releases .

The EDMT displays status messages during the migration process, including warnings and errors. Warnings are displayed for
                                    informational purposes only and do not stop the migration. On the other hand, errors stop the migration process and leave
                                    the database in a corrupt state. If an error occurs, fix the error, and run the tool again.

Regutil Tool—Used in Technology Refresh upgrades, the tool exports the Cisco Systems, Inc. registry from the source machine
                                    during the preupgrade process. The output of the tool is required on the destination machine when running the Unified CCE
                                    Installer during the upgrade process.

You can
                                    				download the Regutil Tool from Cisco.com by clicking Contact Center Enterprise Tools .

## Packaged CCE 2000 Agents Deployment

Packaged CCE solution upgrade for 2000 Agent deployments can be done in single-stage on both main site and remote sites (if
                              applicable).  In a single-stage upgrade, all components are upgraded and taken to completion. For more information, see Single-stage Upgrade .

### Single-stage Upgrade

For single-stage upgrades, perform the tasks detailed in the following table.

Task

Upgrade Tasks

Technology Refresh Upgrade Task Flow

Postupgrade Tasks

See Post Technology Refresh Configurations section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

#### Technology Refresh Upgrade Task Flow

set up all virtual machines required for a Packaged CCE solution (rebuild) on a different hardware or

upgrade the existing components which have been moved (from the source server) to the destination server on a different hardware

On the destination server, follow the VM Layouts for 2000 Agent deployments as specified in the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .

The VM validations of hardware are turned off during Central Controller upgrade and are activated when cutover is initiated.

For co-resident configurations, upgrade CUIC-LD-IDS along with the Unified CCE Central Controller upgrade.

Component Group

Components

Notes

Platform Orchestration, Hybrid Features

Cloud Connect

If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Considerations for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component.

If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio)

For CVP installation or upgrade instructions, see the Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html

After upgrading the Unified CVP servers, add the CVP machines to the domain. For more information, see Add Machine to Domain .

Gateways

Cisco Virtualized Voice Browser (VVB)

For more information, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html .

IOS Gateways (If used for ingress access only)

IOS VXML Gateways

Upgrade Cisco Voice Gateway IOS Version

Agent and supervisor desktops and Reporting

ECE

For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

Cisco Finesse

For Finesse installation or upgrade instructions, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

CUIC-LD-IDS

CUIC (Reporting Templates)

Install or upgrade Cisco Unified Intelligence Center with Live Data and Identity Service (IdS).

After you upgrade Cisco Unified Intelligence Center (CUIC), you must:

Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC.

Import LD and Finesse certificates to CUIC.

Unified CCE Rogger and AW-HDS-DDS

First maintenance window to shut down services on Side A of source components.

Second maintenance window in the middle of the upgrade to cutover from Side B to Side A. You must bring down Side B before
                                                      you bring up Side A.

Unified CCE Rogger Side A

Migrate the Logger database and upgrade Side A Rogger

Migrate the Logger Database and Upgrade the Rogger

Unified CCE AW-HDS-DDS Side A

Migrate AW-HDS-DDS and then upgrade Side A Unified CCE Administration & Data Server

Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server

Unified CCE Rogger Side B

Migrate the Logger database and upgrade Side B Rogger

Migrate the Logger Database and Upgrade the Rogger

Unified CCE AW-HDS-DDS Side B

Migrate AW-HDS-DDS and then upgrade Side B Unified CCE Administration & Data Server

Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server

After you upgrade AW, import the certificate of all solution components (if applicable) to all AWs.

External HDS

Migrate the AW and HDS Database & Upgrade the External HDS

Unified CCE Router

Enable Configuration Changes

Database Performance Enhancement

Database Performance Enhancement

Peripheral Gateways

Upgrade Peripheral Gateways

You can have many PGs located on different virtual machines. Upgrade both Side A and Side B PGs.

Outbound Option Dialer

Upgrade the Outbound Option Dialer:

Upgrade Outbound Option Dialer

To enable Outbound Option High Availability in the Web Setup tool, see Configure the Logger for Outbound Option section in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

Customer Collaboration Platform

For Customer Collaboration Platform installation or upgrade instructions, see the Cisco SocialMiner Installation and Upgrade Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html .

Cisco Unified Communications Manager (Unified Communications Manager)

For installation or upgrade instructions, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service or Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

##### Disable
                                 	 Configuration Changes

To disable
                                                			 configuration changes during the upgrade, set the following registry key to 1
                                                			 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance
                                                   				name>\Router
                                                   				A\Router\CurrentVersion\Configuration\Global\DBMaintenance .

Caution

Make sure that you do not perform inventory 1 and configuration 2 changes on the source server before the cutover is complete. Else, you will have to do these updates manually in the inventory
                                                               on the destination server.

##### Export the Server
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

##### Migrate the Logger Database and Upgrade the Rogger

###### Before you begin

EDMT requires Microsoft® ODBC Driver 13 for SQL Server® and Visual C++ Redistributable for Visual Studio 2015 (or higher). The latest version of these packages can
                                             be downloaded from the Microsoft website. However, a copy of the same is also available in the Prerequisites folder of EDMT.

If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                             SERVICE), you must run EDMT as an administrator.

Create a shared folder in any desired location. Ensure that:

In the Properties window > Sharing tab > Advanced Sharing, the Share this folder check box is checked.

In the Properties window > Security tab > Advanced Sharing > Permission , the permission level is set as Full control for the user group everyone .

Step 1

Use Unified CCE Service Control to stop all Unified CCE services on the Router and Logger , on the source server .

Step 2

(Optional) If Outbound Option High Availability is deployed, disable Outbound Options High Availability. For details, see Disable Outbound Options High Availability (If Applicable) .

Step 3

Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. These
                                                include the ODBC Driver 13 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015.

Step 4

Run the EDMT from the server that will host the destination Logger and click Next .

Step 5

Select Technology Refresh and click Next .

Step 6

Under Source Database Connection , complete the following fields:

From the Authentication drop-down list, select SQL Server Authentication or Windows Authentication (default).

In the HostName/IP Address field, enter the IP address or hostname of the source server with the Logger database.

In the SQL Server Port Number field, enter the TCP or IP port in which the source SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port.

Enter the values in Domain Name , Username , and Password fields.

For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database.

For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database.

Click Refresh Database List to refresh the list of available Unified ICM databases on the server.

In the Database Name , select the Logger database.

Step 7

Under Destination Database Connection , complete the following fields:

In the Authentication drop-down list, use Windows Authentication (default).

In the SQL Server Port Number field, enter the TCP or IP port in which the destination SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port.

The rest of the fields are disabled (read-only) and the default values are displayed.

Click Next .

Step 8

Under Backup Connection , complete the following fields:

In the HostName/IP Address field, enter the backup server's IP address or hostname.

In the Windows Share Name field, enter the name of the shared folder where the backup database file is.

In the Windows Share Domain field, enter the domain name (if applicable).

In the Windows Share Username and Windows Share Password fields, enter the Windows credentials that has read or write access to the specified Windows share.

Step 9

In the Destination Restore Location , browse to select the folder where the system creates the database data files (.mdf) and translation log files (.ldf). The
                                                destination is prepopulated with the default location for database file storage for the running SQL Server.

Step 10

Click Next .

Step 11

Click Start Migration .

Step 12

Click Yes on the warning pop-up to start the data migration.

Step 13

Upon completion of the migration, click Exit to close the tool.

Step 14

(Optional) If Outbound Option High Availability is deployed, repeat steps 1 through 13 to migrate the BA database.

Step 15

Launch the ICM-CCE-Installer and click Next .

Step 16

Select Technology Refresh and click Next .

Step 17

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 18

(Optional) To apply any Minor/Maintenance Releases, click Browse and navigate to the Minor/Maintenance Release
                                                software. Click Next .

During Unified CCE installation on to Windows Server 2019 and SQL Server
                                                               2019, you should not select SQL Server Security Hardening optional
                                                               configuration as a part of the installation. You can apply the SQL
                                                               Security Hardening post installation using the Security Wizard tool.

Step 19

(Optional) Select SQL Server Security Hardening and click Next .

Step 20

Click OK on any informational messages that display.

Step 21

Click Install .

Step 22

Reboot the system after the upgrade completes.

##### Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server

To upgrade the Administration & Data Server, migrate the AW database and then the HDS database (if applicable). After successful
                                       migration, install the new software and import the Cisco registry information.

###### Before you begin

EDMT requires Microsoft® ODBC Driver 13 for SQL Server® and Visual C++ Redistributable for Visual Studio 2015 (or higher). The latest version of these packages can
                                             be downloaded from the Microsoft website. However, a copy of the same is also available in the Prerequisites folder of EDMT.

If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                             SERVICE), you must run EDMT as an administrator.

Create a shared folder in any desired location. Ensure that:

In the Properties window > Sharing tab > Advanced Sharing, the Share this folder check box is checked.

In the Properties window > Security tab > Advanced Sharing > Permission , the permission level is set as Full control for the user group everyone .

Step 1

Use Unified CCE Service Control to stop all Unified CCE services on the source server.

Step 2

Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. These
                                                include the ODBC Driver 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015.

Step 3

Launch the EDMT tool on the destination server that hosts the Administration and Data Server with AW and HDS database and click Next .

Step 4

Select Technology Refresh and click Next .

Step 5

Under Source Database Connection , complete the following fields:

From the Authentication drop-down list, select SQL Server Authentication or Windows Authentication (default).

In the HostName/IP Address field, enter the IP address or hostname of the source server with the database.

In the SQL Server Port Number field, enter the TCP or IP port in which the source SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port.

Enter the values in Domain Name , Username , and Password fields.

For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database.

For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database.

Click Refresh Database List to refresh the list of available Unified ICM databases on the server.

In the Database Name , select the AW database.

Step 6

Under Destination Database Connection , complete the following fields:

In the Authentication drop-down list, use Windows Authentication (default).

In the SQL Server Port Number field, enter the TCP or IP port in which the destination SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port.

The rest of the fields are disabled (read-only) and the default values are displayed.

Click Next .

Step 7

Under Backup Connection , complete the following fields:

In the HostName/IP Address field, enter the backup server's IP address or hostname.

In the Windows Share Name field, enter the name of the shared folder where the backup database file is.

In the Windows Share Domain field, enter the domain name (if applicable).

In the Windows Share Username and Windows Share Password fields, enter the Windows credentials that has read or write access to the specified Windows share.

Step 8

In the Destination Restore Location , browse to select the folder where the system creates the database data files (.mdf) and translation log files (.ldf). The
                                                destination is prepopulated with the default location for database file storage for the running SQL Server.

Step 9

Click Next .

Step 10

Click Start Migration .

Step 11

Click Yes on the warning pop-up to start the data migration.

Step 12

Upon completion of the migration, click Exit to close the tool.

Step 13

To migrate the HDS database, repeat steps 1 to 12.

Under Source Database Connection, in Database Name , select the HDS database.

Step 14

Launch the ICM-CCE-Installer and click Next .

Step 15

Select Technology Refresh and click Next .

Step 16

Click Browse and specify the path for the RegUtil file you exported from the source machine
                                                					during the preupgrade process.

Step 17

To apply any Minor/Maintenance Releases, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 18

(Optional) Select SQL Server Security Hardening and click Next .

Step 19

Click OK on any informational messages that display.

Step 20

Click Install .

Step 21

Restart the server when the upgrade completes.

##### Migrate the AW and HDS Database & Upgrade the External HDS

To upgrade the external HDS, migrate the AW database, and then the HDS database. After successful migration, install the new
                                       software and import the Cisco registry information.

###### Before you begin

EDMT requires Microsoft® ODBC Driver 13 for SQL Server® and Visual C++ Redistributable for Visual Studio 2015 (or higher). The latest version of these packages can
                                             be downloaded from the Microsoft website. However, a copy of the same is also available in the Prerequisites folder of EDMT.

If you are configuring SQL services to run as Virtual account (NT SERVICE) or Network Service account (NT AUTHORITY\NETWORK
                                             SERVICE), you must run EDMT as an administrator.

Create a shared folder in any desired location. Ensure that:

In the Properties window > Sharing tab > Advanced Sharing, the Share this folder check box is checked.

In the Properties window > Security tab > Advanced Sharing > Permission , the permission level is set as Full control for the user group everyone .

Step 1

Use Unified CCE Service Control to stop all Unified CCE services on the source server.

Step 2

Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. These
                                                include the ODBC Driver 13 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015.

Step 3

Launch the EDMT tool on the destination server that hosts the Administration and Data Server with AW and HDS database and click Next .

Step 4

Select Technology Refresh and click Next .

Step 5

Under Source Database Connection , complete the following fields:

From the Authentication drop-down list, select SQL Server Authentication or Windows Authentication (default).

In the HostName/IP Address field, enter the IP address or hostname of the source server with the database.

In the SQL Server Port Number field, enter the TCP or IP port in which the source SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port.

Enter the values in Domain Name , Username , and Password fields.

For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database.

For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database.

Click Refresh Database List to refresh the list of available Unified ICM databases on the server.

In the Database Name , select the AW database.

Step 6

Under Destination Database Connection , complete the following fields:

In the Authentication drop-down list, use Windows Authentication (default).

In the SQL Server Port Number field, enter the TCP or IP port in which the destination SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port.

The rest of the fields are disabled (read-only) and the default values are displayed.

Click Next .

Step 7

Under Backup Connection , complete the following fields:

In the HostName/IP Address field, enter the backup server's IP address or hostname.

In the Windows Share Name field, enter the name of the shared folder where the backup database file is.

In the Windows Share Domain field, enter the domain name (if applicable).

In the Windows Share Username and Windows Share Password fields, enter the Windows credentials that has read or write access to the specified Windows share.

Step 8

In the Destination Restore Location , browse to select the folder where the system creates the database data files (.mdf) and translation log files (.ldf). The
                                                destination is prepopulated with the default location for database file storage for the running SQL Server.

Step 9

Click Next .

Step 10

Click Start Migration .

Step 11

Click Yes on the warning pop-up to start the data migration.

Step 12

Upon completion of the migration, click Exit to close the tool.

Step 13

To migrate the HDS database, repeat steps 1 to 12.

Under Source Database Connection, in Database Name , select the HDS database.

Step 14

Launch the ICM-CCE-Installer and click Next .

Step 15

Select Technology Refresh and click Next .

Step 16

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 17

(Optional) To apply any Minor/Maintenance Releases, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

SQL Security Hardening should not be applied during installation of
                                                               Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                               applied post installation using the Security Wizard tool.

Step 18

(Optional) Select SQL Server Security Hardening and click Next .

Step 19

Click OK on any informational messages that display.

Step 20

Click Install .

Step 21

Reboot the server when the upgrade completes.

##### Enable Configuration Changes

Step 1

To enable configuration changes during the upgrade, set the
                                                			 following registry key to 0 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                                   				Inc.\ICM\<instance name>\Router
                                                   				A\Router\CurrentVersion\Configuration\Global\DBMaintenance .

Step 2

To confirm that configuration changes are enabled, save a configuration change.

Save your changes.

##### Upgrade Peripheral Gateways

You can upgrade different Peripheral Gateways (PG) within a contact center at different times within different maintenance
                                       windows. However, upgrade all PGs that reside on the same virtual machine and redundant PGs (Side A and corresponding Side
                                       B) during the same maintenance window.

The following dependencies occur when upgrading the PG:

If your contact center uses the CTI OS component, upgrade the CTI OS server at the same time as the associated Avaya PG 3 .

If your contact center uses Outbound Option, upgrade any Outbound Option Dialers associated with Unified Communications Manager
                                             PGs at the same time.

If the Unified Communications Manager application is upgraded, upgrade the JTAPI client associated with the Unified Communications
                                             Manager PG at the same time.

To upgrade the Peripheral Gateways, install the new software and import the Cisco registry information.

Step 1

Use Unified CCE Service Control to stop all Unified CCE and CTI OS (if applicable when upgrading the Avaya PG ) services on the PG server. Change the services to Manual Start.

Step 2

Launch the ICM-CCE-Installer and click Next .

Step 3

Select Technology Refresh and click Next .

Step 4

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

The registry information for the Avaya PG also contains information for the CTI OS server (if applicable).

Step 5

(Optional) To apply any Minor/Maintenance Releases, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 6

Click OK on any informational messages that display.

Step 7

Click Install .

Step 8

Reboot the system after the upgrade completes.

Step 9

If Avaya PG is configured, after reboot, open the Peripheral Gateway Setup tool, and edit the Avaya PG as required.

Step 10

If CTI OS component is configured, after reboot, open the CTI OS Server setup tool, and edit the CTI OS component as required.

##### Disable Outbound Options High Availability (If Applicable)

###### Before you begin

Before proceeding with the following steps, ensure that Outbound Options feature is in maintenance mode. There must not be
                                       any customer records getting imported to Outbound database. The outbound campaigns must not be active and outbound callflow
                                       must not be in progress.

Perform the following steps on Side A:

Step 1

Launch Websetup . Navigate to Component Management > Loggers .

Step 2

Edit the Logger and navigate to Additional Options . Uncheck Enable High Availability under Outbound Option . Enter the SQL Server Admin credentials and click Next .

Step 3

Enable Stop and then start(cycle) the Logger Service for this instance (if it is running) checkbox . Click Next to complete the setup.

Step 4

Repeat similar steps (steps 1, 2, and 3) for side B.

###### What to do next

You can enable Outbound Options High Availability after the upgrade is successful.

##### Upgrade Outbound
                                 	 Option Dialer

To upgrade the Outbound Option Dialer, install the new software and import the Cisco registry information.

###### Before you begin

Step 1

Launch the ICM-CCE-Installer and click Next .

Step 2

Select Technology Refresh and click Next .

Step 3

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 4

(Optional) To apply any Maintenance Releases, click Browse and navigate to the Maintenance Release software. Click Next .

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

## Packaged CCE 4000 Agents and above Deployment

Packaged CCE solution upgrade for 4000 Agents and above deployments can be done in single-stage or in multiple stages (multistage)
                              on both main site and remote sites (if applicable).

In a single-stage upgrade, all components are upgraded and taken to completion. For more information, see Single-stage Upgrade .

In a multistage upgrade, components are grouped into several stages for upgrading. You must follow the upgrade sequence and
                              the minimum component groupings that must occur together within each stage. At each stage in the upgrade, the upgraded components
                              must interoperate with components that have not yet been upgraded to ensure the overall operation of the contact center. Therefore,
                              it is important to verify this interoperability during the planning stages of the upgrade. For more information, see Multistage Upgrade .

### Single-stage Upgrade

For single-stage upgrades, perform the tasks detailed in the following table.

Task

Upgrade Tasks

Technology Refresh Upgrade Task Flow

Postupgrade Tasks

See Post Technology Refresh Configurations section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

#### Technology Refresh Upgrade Task Flow

set up all virtual machines required for a Packaged CCE solution (rebuild) on a different hardware or

upgrade the existing components which have been moved (from the source server) to the destination server on a different hardware

Component Group

Components

Notes

Platform Orchestration, Hybrid Features

Cloud Connect

If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Considerations for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component.

If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio)

For CVP installation or upgrade instructions, see the Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html

Gateways

Cisco Virtualized Voice Browser

For VVB installation or upgrade instructions, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html .

IOS Gateways (If used for ingress access only.)

IOS VXML Gateways

Upgrade Cisco Voice Gateway IOS Version

Identity Service (IdS)/SSO

IdS Server

SSO is an optional feature. It exchanges authentication and authorization details between an identity provider (IdP) and an
                                             identity service (IdS).

For IdS installation or upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Agent and supervisor desktops

ECE

For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

Cisco Finesse

For Finesse installation or upgrade instructions, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

Cisco Unified Intelligence Center (CUIC) Reporting Server

After you upgrade Cisco Unified Intelligence Center (CUIC), you must:

Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname.

Import LD and Finesse certificates to CUIC.

Unified CCE Central Controller

Unified CCE Rogger and AW-HDS-DDS

First maintenance window to shut down services on Side A of source components.

Second maintenance window in the middle of the upgrade to cut over from Side B to Side A. You must bring down Side B before
                                                      you bring up Side A.

Unified CCE Rogger Side A

Migrate the Logger database and upgrade Side A Rogger

Migrate the Logger Database and Upgrade the Rogger

Unified CCE AW-HDS-DDS Side A

Migrate AW-HDS-DDS and then upgrade Side A Unified CCE Administration & Data Server

Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server

Unified CCE Rogger Side B

Migrate the Logger database and upgrade Side B Rogger

Migrate the Logger Database and Upgrade the Rogger

Unified CCE AW-HDS-DDS Side B

Migrate AW-HDS-DDS and then upgrade Side B Unified CCE Administration & Data Server

Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server

After you upgrade AW, import the certificate of all solution components (if applicable) to all AWs.

External HDS

Migrate the AW and HDS Database & Upgrade the External HDS

Unified CCE Router

Enable Configuration Changes

CUIC (Reporting Templates)

Standalone Live Data

To install or upgrade Live Data, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

After you upgrade Live Data (LD), you must enable CORS on the LD server, and add cors allowed_origin with Finesse hostname.

Database Performance Enhancement

Database Performance Enhancement

Collocated Peripheral Gateways and associated components

Upgrade Peripheral Gateways

You can have many PGs located on different virtual machines. Upgrade both Side A and Side B PGs.

Outbound Option Dialer

Upgrade Outbound Option Dialer

To enable Outbound Option High Availability in the Web Setup tool, see Configure the Logger for Outbound Option section in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

CTI Server

CTI OS Server

CTI OS Server is applicable only if Avaya PG is used.

For installation instructions, see the CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Peripheral Gateways and associated components not collocated

Customer Collaboration Platform

For Customer Collaboration Platform installation or upgrade instructions, see the Cisco SocialMiner Installation and Upgrade Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html .

CTI OS Desktops

For CTI OS Desktop client installation instructions, see the CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Unified Communications Manager (Unified Communications Manager)

For installation or upgrade instructions, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service or Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

JTAPI client on Agent (Cisco Unified Communications Manager) PG

Upgrade Cisco JTAPI Client on PG

After upgrading the Central Controller to 12.5(1) , if you intend to keep the PGs in 12.0(1), you must install ICM_12.0(1)_ES49 on the PG machines for an inventory update.

### Multistage Upgrade

For multistage upgrades, perform the tasks detailed in the following table.

Task

Upgrade Tasks

Technology Refresh Upgrade Task Flow

Postupgrade Tasks

Follow the post upgrade tasks after each stage of upgrade.

For more information, see Post Technology Refresh Configurations section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

#### Technology Refresh Upgrade Task Flow

set up the required virtual machines (rebuild) on a different hardware or

upgrade the existing components which have been moved (from the source server) to the destination server on a different hardware

Maintenance window is applicable for each component until the inventory update and configurations are complete.

Stage

Component Group

Components

Notes

1

Cloud Connection Components

Cloud Connect

For Cloud Connect installation instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

2

Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio)

For CVP installation or upgrade instructions, see the Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html

3

Gateways

Cisco Virtualized Voice Browser

For VVB installation or upgrade instructions, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html .

IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see stage 6 in Upgrade Flowcharts for 4000 Agents and above Deployments .)

IOS VXML Gateways

Upgrade Cisco Voice Gateway IOS Version

4

Identity Service (IdS)/SSO

IdS Server

SSO is an optional feature. It exchanges authentication and authorization details between an identity provider (IdP) and an
                                             identity service (IdS).

For IdS installation or upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

5

Agent and supervisor desktops

ECE

For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

Cisco Finesse

For Finesse installation or upgrade instructions, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

6

Cisco Unified Intelligence Center (CUIC) Reporting Server

After you upgrade Cisco Unified Intelligence Center (CUIC), you must:

Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname.

Import LD and Finesse certificates to CUIC.

7

Unified CCE Central Controller

Unified CCE Rogger and AW-HDS-DDS

First maintenance window to shut down services on Side A of source components.

Second maintenance window in the middle of the upgrade to cut over from Side B to Side A. You must bring down Side B before
                                                      you bring up Side A.

Unified CCE Rogger Side A

Migrate the Logger database and upgrade Side A Rogger

Migrate the Logger Database and Upgrade the Rogger

Unified CCE AW-HDS-DDS Side A

Migrate AW-HDS-DDS and then upgrade Side A Unified CCE Administration & Data Server

Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server

Unified CCE Rogger Side B

Migrate the Logger database and upgrade Side B Rogger

Migrate the Logger Database and Upgrade the Rogger

Unified CCE AW-HDS-DDS Side B

Migrate AW-HDS-DDS and then upgrade Side B Unified CCE Administration & Data Server

Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server

After you upgrade AW, import the certificate of all solution components (if applicable) to all AWs.

External HDS

Migrate the AW and HDS Database & Upgrade the External HDS

Unified CCE Router

Enable Configuration Changes

CUIC (Reporting Templates)

Standalone Live Data

To install or upgrade Live Data, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

After you upgrade Live Data (LD), you must enable CORS on the LD server, and add cors allowed_origin with Finesse hostname.

Database Performance Enhancement

Database Performance Enhancement

8

Collocated Peripheral Gateways and associated components

Upgrade Peripheral Gateways

You can have many PGs located on different virtual machines. Upgrade both Side A and Side B PGs.

Outbound Option Dialer

Upgrade Outbound Option Dialer

To enable Outbound Option High Availability in the Web Setup tool, see Configure the Logger for Outbound Option section in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

CTI Server

CTI OS Server

CTI OS Server is applicable only if

Avaya PG is used.

For installation instructions, see the CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

9

Peripheral Gateways and associated components not collocated

Customer Collaboration Platform

For Customer Collaboration Platform installation or upgrade instructions, see the Cisco SocialMiner Installation and Upgrade Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html .

10

CTI OS Desktops

For CTI OS Desktop client installation instructions, see the CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

11

Cisco Unified Communications Manager (Unified Communications Manager)

For installation or upgrade instructions, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service or Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

JTAPI client on Agent (Cisco Unified Communications Manager) PG

Upgrade Cisco JTAPI Client on PG

After upgrading the Central Controller to 12.5(1) , if you intend to keep the PGs in 12.0(1), you must install ICM_12.0(1)_ES49 on the PG machines for an inventory update.

| Note | To enable the Technology Refresh upgrade support in 12.5(1), install
                                          ICM_12.5(1)_ES12 on the 12.5(1) target system. |
|---|---|

| Note | During Unified CCE installation on to Windows Server 2019 and SQL Server 2019, SQL Server
                                       				Security Hardening optional configuration should not be selected as part of
                                       				installation. SQL Security Hardening should be applied post Unified CCE installation
                                       				using Security Wizard tool. Unified CCE services should be started only after 12.5(2) for Windows Server 2019 and SQL Server 2019 support is installed. |
|---|---|

| Task |
|---|
| Upgrade Tasks |
| Technology Refresh Upgrade Task Flow |
| Postupgrade Tasks |
| See Post Technology Refresh Configurations section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |

| Note | On the destination server, follow the VM Layouts for 2000 Agent deployments as specified in the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html . The VM validations of hardware are turned off during Central Controller upgrade and are activated when cutover is initiated. For co-resident configurations, upgrade CUIC-LD-IDS along with the Unified CCE Central Controller upgrade. |
|---|---|

| Component Group | Components | Notes |
|---|---|---|
| Platform Orchestration, Hybrid Features | Cloud Connect | If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Considerations for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component. If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| Queuing and self-service | Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio) | For CVP installation or upgrade instructions, see the Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html After upgrading the Unified CVP servers, add the CVP machines to the domain. For more information, see Add Machine to Domain . |
| Gateways | Cisco Virtualized Voice Browser (VVB) | For more information, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html . |
| IOS Gateways (If used for ingress access only) IOS VXML Gateways | Upgrade Cisco Voice Gateway IOS Version |
| Agent and supervisor desktops and Reporting | ECE | For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| Cisco Finesse | For Finesse installation or upgrade instructions, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . |
| CUIC-LD-IDS CUIC (Reporting Templates) | Install or upgrade Cisco Unified Intelligence Center with Live Data and Identity Service (IdS). For CUIC upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade Cisco Unified Intelligence Center (CUIC), you must: Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname. For more information, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade Live Data (LD), you must enable CORS on the LD box for Finesse and CUIC. Import LD and Finesse certificates to CUIC. |
| Unified CCE Controller | Unified CCE Rogger and AW-HDS-DDS | The CCE components upgrade requires the following maintenance windows on the source server: First maintenance window to shut down services on Side A of source components. Second maintenance window in the middle of the upgrade to cutover from Side B to Side A. You must bring down Side B before
                                                      you bring up Side A. |
| Unified CCE Rogger Side A | Migrate the Logger database and upgrade Side A Rogger Migrate the Logger Database and Upgrade the Rogger |
| Unified CCE AW-HDS-DDS Side A | Migrate AW-HDS-DDS and then upgrade Side A Unified CCE Administration & Data Server Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server |
| Unified CCE Rogger Side B | Migrate the Logger database and upgrade Side B Rogger Migrate the Logger Database and Upgrade the Rogger |
| Unified CCE AW-HDS-DDS Side B | Migrate AW-HDS-DDS and then upgrade Side B Unified CCE Administration & Data Server Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server After you upgrade AW, import the certificate of all solution components (if applicable) to all AWs. |
| External HDS | Migrate the AW and HDS Database & Upgrade the External HDS |
| Unified CCE Router | Enable Configuration Changes |
| Database Performance Enhancement | Database Performance Enhancement |
| Unified CCE Peripheral Gateways and associated components | Peripheral Gateways | Upgrade Peripheral Gateways You can have many PGs located on different virtual machines. Upgrade both Side A and Side B PGs. |
| Outbound Option Dialer | Upgrade the Outbound Option Dialer: Upgrade Outbound Option Dialer To enable Outbound Option High Availability in the Web Setup tool, see Configure the Logger for Outbound Option section in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html . |
| Customer Collaboration Platform | For Customer Collaboration Platform installation or upgrade instructions, see the Cisco SocialMiner Installation and Upgrade Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html . |
| Call Processing Components | Cisco Unified Communications Manager (Unified Communications Manager) | For installation or upgrade instructions, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service or Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |

| To disable
                                                			 configuration changes during the upgrade, set the following registry key to 1
                                                			 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance
                                                   				name>\Router
                                                   				A\Router\CurrentVersion\Configuration\Global\DBMaintenance . Caution Make sure that you do not perform inventory 1 and configuration 2 changes on the source server before the cutover is complete. Else, you will have to do these updates manually in the inventory
                                                               on the destination server. | Caution | Make sure that you do not perform inventory 1 and configuration 2 changes on the source server before the cutover is complete. Else, you will have to do these updates manually in the inventory
                                                               on the destination server. |
|---|---|---|
| Caution | Make sure that you do not perform inventory 1 and configuration 2 changes on the source server before the cutover is complete. Else, you will have to do these updates manually in the inventory
                                                               on the destination server. |

| Caution | Make sure that you do not perform inventory 1 and configuration 2 changes on the source server before the cutover is complete. Else, you will have to do these updates manually in the inventory
                                                               on the destination server. |
|---|---|

| Note | Ensure to run the RegUtil tool with administrative privileges. |
|---|---|

| Step 1 | Open a command
                                                			 prompt and change the directory to the location where the RegUtil.exe resides. |
|---|---|
| Step 2 | Run the RegUtil tool to export the Cisco Systems, Inc. registry using the following command: RegUtil -export [target directory] , for example, <ICM install directory>:\icm\bin>RegUtil -export C:\RegUtil The target directory must have write access. Therefore, you cannot select the install media on a DVD. The target directory
                                                   is optional. If it is not specified, the tool outputs the result of the Registry export to the current directory. The output
                                                   filename is of the format RegUtil_<hostname>.dat, where hostname is the name of the source machine. |

| Note | If the user group everyone is not available, add it using the Add button. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE services on the Router and Logger , on the source server . |
|---|---|
| Step 2 | (Optional) If Outbound Option High Availability is deployed, disable Outbound Options High Availability. For details, see Disable Outbound Options High Availability (If Applicable) . |
| Step 3 | Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. These
                                                include the ODBC Driver 13 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015. |
| Step 4 | Run the EDMT from the server that will host the destination Logger and click Next . |
| Step 5 | Select Technology Refresh and click Next . |
| Step 6 | Under Source Database Connection , complete the following fields: From the Authentication drop-down list, select SQL Server Authentication or Windows Authentication (default). In the HostName/IP Address field, enter the IP address or hostname of the source server with the Logger database. In the SQL Server Port Number field, enter the TCP or IP port in which the source SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port. Enter the values in Domain Name , Username , and Password fields. Note For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. Click Refresh Database List to refresh the list of available Unified ICM databases on the server. In the Database Name , select the Logger database. | Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
| Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
| Step 7 | Under Destination Database Connection , complete the following fields: In the Authentication drop-down list, use Windows Authentication (default). In the SQL Server Port Number field, enter the TCP or IP port in which the destination SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port. Note The rest of the fields are disabled (read-only) and the default values are displayed. Click Next . | Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
| Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
| Step 8 | Under Backup Connection , complete the following fields: In the HostName/IP Address field, enter the backup server's IP address or hostname. In the Windows Share Name field, enter the name of the shared folder where the backup database file is. In the Windows Share Domain field, enter the domain name (if applicable). In the Windows Share Username and Windows Share Password fields, enter the Windows credentials that has read or write access to the specified Windows share. |
| Step 9 | In the Destination Restore Location , browse to select the folder where the system creates the database data files (.mdf) and translation log files (.ldf). The
                                                destination is prepopulated with the default location for database file storage for the running SQL Server. |
| Step 10 | Click Next . |
| Step 11 | Click Start Migration . |
| Step 12 | Click Yes on the warning pop-up to start the data migration. |
| Step 13 | Upon completion of the migration, click Exit to close the tool. |
| Step 14 | (Optional) If Outbound Option High Availability is deployed, repeat steps 1 through 13 to migrate the BA database. |
| Step 15 | Launch the ICM-CCE-Installer and click Next . |
| Step 16 | Select Technology Refresh and click Next . |
| Step 17 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 18 | (Optional) To apply any Minor/Maintenance Releases, click Browse and navigate to the Minor/Maintenance Release
                                                software. Click Next . Note During Unified CCE installation on to Windows Server 2019 and SQL Server
                                                               2019, you should not select SQL Server Security Hardening optional
                                                               configuration as a part of the installation. You can apply the SQL
                                                               Security Hardening post installation using the Security Wizard tool. | Note | During Unified CCE installation on to Windows Server 2019 and SQL Server
                                                               2019, you should not select SQL Server Security Hardening optional
                                                               configuration as a part of the installation. You can apply the SQL
                                                               Security Hardening post installation using the Security Wizard tool. |
| Note | During Unified CCE installation on to Windows Server 2019 and SQL Server
                                                               2019, you should not select SQL Server Security Hardening optional
                                                               configuration as a part of the installation. You can apply the SQL
                                                               Security Hardening post installation using the Security Wizard tool. |
| Step 19 | (Optional) Select SQL Server Security Hardening and click Next . |
| Step 20 | Click OK on any informational messages that display. |
| Step 21 | Click Install . |
| Step 22 | Reboot the system after the upgrade completes. |

| Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
|---|---|

| Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
|---|---|

| Note | During Unified CCE installation on to Windows Server 2019 and SQL Server
                                                               2019, you should not select SQL Server Security Hardening optional
                                                               configuration as a part of the installation. You can apply the SQL
                                                               Security Hardening post installation using the Security Wizard tool. |
|---|---|

| Note | If the user group everyone is not available, add it using the Add button. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE services on the source server. |
|---|---|
| Step 2 | Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. These
                                                include the ODBC Driver 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015. |
| Step 3 | Launch the EDMT tool on the destination server that hosts the Administration and Data Server with AW and HDS database and click Next . |
| Step 4 | Select Technology Refresh and click Next . |
| Step 5 | Under Source Database Connection , complete the following fields: From the Authentication drop-down list, select SQL Server Authentication or Windows Authentication (default). In the HostName/IP Address field, enter the IP address or hostname of the source server with the database. In the SQL Server Port Number field, enter the TCP or IP port in which the source SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port. Enter the values in Domain Name , Username , and Password fields. Note For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. Click Refresh Database List to refresh the list of available Unified ICM databases on the server. In the Database Name , select the AW database. | Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
| Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
| Step 6 | Under Destination Database Connection , complete the following fields: In the Authentication drop-down list, use Windows Authentication (default). In the SQL Server Port Number field, enter the TCP or IP port in which the destination SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port. Note The rest of the fields are disabled (read-only) and the default values are displayed. Click Next . | Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
| Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
| Step 7 | Under Backup Connection , complete the following fields: In the HostName/IP Address field, enter the backup server's IP address or hostname. In the Windows Share Name field, enter the name of the shared folder where the backup database file is. In the Windows Share Domain field, enter the domain name (if applicable). In the Windows Share Username and Windows Share Password fields, enter the Windows credentials that has read or write access to the specified Windows share. |
| Step 8 | In the Destination Restore Location , browse to select the folder where the system creates the database data files (.mdf) and translation log files (.ldf). The
                                                destination is prepopulated with the default location for database file storage for the running SQL Server. |
| Step 9 | Click Next . |
| Step 10 | Click Start Migration . |
| Step 11 | Click Yes on the warning pop-up to start the data migration. |
| Step 12 | Upon completion of the migration, click Exit to close the tool. |
| Step 13 | To migrate the HDS database, repeat steps 1 to 12. Under Source Database Connection, in Database Name , select the HDS database. |
| Step 14 | Launch the ICM-CCE-Installer and click Next . |
| Step 15 | Select Technology Refresh and click Next . |
| Step 16 | Click Browse and specify the path for the RegUtil file you exported from the source machine
                                                					during the preupgrade process. |
| Step 17 | To apply any Minor/Maintenance Releases, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 18 | (Optional) Select SQL Server Security Hardening and click Next . |
| Step 19 | Click OK on any informational messages that display. |
| Step 20 | Click Install . |
| Step 21 | Restart the server when the upgrade completes. |

| Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
|---|---|

| Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
|---|---|

| Note | If the user group everyone is not available, add it using the Add button. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE services on the source server. |
|---|---|
| Step 2 | Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. These
                                                include the ODBC Driver 13 for SQL Server, and Visual C++ Redistributable for Visual Studio 2015. |
| Step 3 | Launch the EDMT tool on the destination server that hosts the Administration and Data Server with AW and HDS database and click Next . |
| Step 4 | Select Technology Refresh and click Next . |
| Step 5 | Under Source Database Connection , complete the following fields: From the Authentication drop-down list, select SQL Server Authentication or Windows Authentication (default). In the HostName/IP Address field, enter the IP address or hostname of the source server with the database. In the SQL Server Port Number field, enter the TCP or IP port in which the source SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port. Enter the values in Domain Name , Username , and Password fields. Note For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. Click Refresh Database List to refresh the list of available Unified ICM databases on the server. In the Database Name , select the AW database. | Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
| Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
| Step 6 | Under Destination Database Connection , complete the following fields: In the Authentication drop-down list, use Windows Authentication (default). In the SQL Server Port Number field, enter the TCP or IP port in which the destination SQL Server runs. This field defaults to1433, the standard SQL Server
                                                         port. Note The rest of the fields are disabled (read-only) and the default values are displayed. Click Next . | Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
| Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
| Step 7 | Under Backup Connection , complete the following fields: In the HostName/IP Address field, enter the backup server's IP address or hostname. In the Windows Share Name field, enter the name of the shared folder where the backup database file is. In the Windows Share Domain field, enter the domain name (if applicable). In the Windows Share Username and Windows Share Password fields, enter the Windows credentials that has read or write access to the specified Windows share. |
| Step 8 | In the Destination Restore Location , browse to select the folder where the system creates the database data files (.mdf) and translation log files (.ldf). The
                                                destination is prepopulated with the default location for database file storage for the running SQL Server. |
| Step 9 | Click Next . |
| Step 10 | Click Start Migration . |
| Step 11 | Click Yes on the warning pop-up to start the data migration. |
| Step 12 | Upon completion of the migration, click Exit to close the tool. |
| Step 13 | To migrate the HDS database, repeat steps 1 to 12. Under Source Database Connection, in Database Name , select the HDS database. |
| Step 14 | Launch the ICM-CCE-Installer and click Next . |
| Step 15 | Select Technology Refresh and click Next . |
| Step 16 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 17 | (Optional) To apply any Minor/Maintenance Releases, click Browse and navigate to the Minor/Maintenance Release software. Click Next . Note SQL Security Hardening should not be applied during installation of
                                                               Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                               applied post installation using the Security Wizard tool. | Note | SQL Security Hardening should not be applied during installation of
                                                               Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                               applied post installation using the Security Wizard tool. |
| Note | SQL Security Hardening should not be applied during installation of
                                                               Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                               applied post installation using the Security Wizard tool. |
| Step 18 | (Optional) Select SQL Server Security Hardening and click Next . |
| Step 19 | Click OK on any informational messages that display. |
| Step 20 | Click Install . |
| Step 21 | Reboot the server when the upgrade completes. |

| Note | For SQL Server Authentication, enter the SQL Server credentials and the domain name (if applicable) for the selected database. For Windows Authentication, the Domain Name, Username, and Password fields are disabled. Windows Single Sign-On (SSO) uses
                                                                           your Windows authentication cached credentials to connect to the selected database. |
|---|---|

| Note | The rest of the fields are disabled (read-only) and the default values are displayed. |
|---|---|

| Note | SQL Security Hardening should not be applied during installation of
                                                               Windows Server 2019 and SQL Server 2019. SQL Security Hardening can be
                                                               applied post installation using the Security Wizard tool. |
|---|---|

| Step 1 | To enable configuration changes during the upgrade, set the
                                                			 following registry key to 0 on the Side A Call Router: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,
                                                   				Inc.\ICM\<instance name>\Router
                                                   				A\Router\CurrentVersion\Configuration\Global\DBMaintenance . |
|---|---|
| Step 2 | To confirm that configuration changes are enabled, save a configuration change. Save your changes. |

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE and CTI OS (if applicable when upgrading the Avaya PG ) services on the PG server. Change the services to Manual Start. |
|---|---|
| Step 2 | Launch the ICM-CCE-Installer and click Next . |
| Step 3 | Select Technology Refresh and click Next . |
| Step 4 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. The registry information for the Avaya PG also contains information for the CTI OS server (if applicable). |
| Step 5 | (Optional) To apply any Minor/Maintenance Releases, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 6 | Click OK on any informational messages that display. |
| Step 7 | Click Install . |
| Step 8 | Reboot the system after the upgrade completes. |
| Step 9 | If Avaya PG is configured, after reboot, open the Peripheral Gateway Setup tool, and edit the Avaya PG as required. |
| Step 10 | If CTI OS component is configured, after reboot, open the CTI OS Server setup tool, and edit the CTI OS component as required. |

| Step 1 | Launch Websetup . Navigate to Component Management > Loggers . |
|---|---|
| Step 2 | Edit the Logger and navigate to Additional Options . Uncheck Enable High Availability under Outbound Option . Enter the SQL Server Admin credentials and click Next . |
| Step 3 | Enable Stop and then start(cycle) the Logger Service for this instance (if it is running) checkbox . Click Next to complete the setup. |
| Step 4 | Repeat similar steps (steps 1, 2, and 3) for side B. |

| Step 1 | Launch the ICM-CCE-Installer and click Next . |
|---|---|
| Step 2 | Select Technology Refresh and click Next . |
| Step 3 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 4 | (Optional) To apply any Maintenance Releases, click Browse and navigate to the Maintenance Release software. Click Next . |
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

| Task |
|---|
| Upgrade Tasks |
| Technology Refresh Upgrade Task Flow |
| Postupgrade Tasks |
| See Post Technology Refresh Configurations section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |

| Component Group | Components | Notes |
|---|---|---|
| Platform Orchestration, Hybrid Features | Cloud Connect | If you have Cloud Connect in your environment, refer the Update VM Properties section in Upgrade Considerations for Cloud connect upgrade prerequisite to increase the hard disk and RAM before you upgrade the component. If you don't have Cloud Connect in your environment, and you use any Hybrid feature or Orchestration, fresh install Cloud
                                             Connect. For fresh install instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| Queuing and self-service | Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio) | For CVP installation or upgrade instructions, see the Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html |
| Gateways | Cisco Virtualized Voice Browser | For VVB installation or upgrade instructions, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html . |
| IOS Gateways (If used for ingress access only.) IOS VXML Gateways | Upgrade Cisco Voice Gateway IOS Version |
| Identity Service (IdS)/SSO | IdS Server | SSO is an optional feature. It exchanges authentication and authorization details between an identity provider (IdP) and an
                                             identity service (IdS). For IdS installation or upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Agent and supervisor desktops | ECE | For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| Cisco Finesse | For Finesse installation or upgrade instructions, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . |
| Reporting Management | Cisco Unified Intelligence Center (CUIC) Reporting Server | For CUIC installation or upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade Cisco Unified Intelligence Center (CUIC), you must: Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname. Import LD and Finesse certificates to CUIC. |
| Unified CCE Central Controller | Unified CCE Rogger and AW-HDS-DDS | The CCE components upgrade requires the following maintenance windows on the source server: First maintenance window to shut down services on Side A of source components. Second maintenance window in the middle of the upgrade to cut over from Side B to Side A. You must bring down Side B before
                                                      you bring up Side A. |
| Unified CCE Rogger Side A | Migrate the Logger database and upgrade Side A Rogger Migrate the Logger Database and Upgrade the Rogger |
| Unified CCE AW-HDS-DDS Side A | Migrate AW-HDS-DDS and then upgrade Side A Unified CCE Administration & Data Server Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server |
| Unified CCE Rogger Side B | Migrate the Logger database and upgrade Side B Rogger Migrate the Logger Database and Upgrade the Rogger |
| Unified CCE AW-HDS-DDS Side B | Migrate AW-HDS-DDS and then upgrade Side B Unified CCE Administration & Data Server Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server After you upgrade AW, import the certificate of all solution components (if applicable) to all AWs. |
| External HDS | Migrate the AW and HDS Database & Upgrade the External HDS |
| Unified CCE Router | Enable Configuration Changes |
| CUIC (Reporting Templates) | For CUIC installation or upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . |
| Standalone Live Data | To install or upgrade Live Data, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade Live Data (LD), you must enable CORS on the LD server, and add cors allowed_origin with Finesse hostname. |
| Database Performance Enhancement | Database Performance Enhancement |
| Collocated Peripheral Gateways and associated components | Peripheral Gateways 4 | Upgrade Peripheral Gateways You can have many PGs located on different virtual machines. Upgrade both Side A and Side B PGs. |
| Outbound Option Dialer | Upgrade Outbound Option Dialer To enable Outbound Option High Availability in the Web Setup tool, see Configure the Logger for Outbound Option section in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html . |
| CTI Server CTI OS Server | CTI OS Server is applicable only if Avaya PG is used. For installation instructions, see the CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Peripheral Gateways and associated components not collocated | Customer Collaboration Platform | For Customer Collaboration Platform installation or upgrade instructions, see the Cisco SocialMiner Installation and Upgrade Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html . |
| Agent and Supervisor Desktops | CTI OS Desktops | For CTI OS Desktop client installation instructions, see the CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Call Processing Components | Cisco Unified Communications Manager (Unified Communications Manager) | For installation or upgrade instructions, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service or Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| JTAPI client on Agent (Cisco Unified Communications Manager) PG | Upgrade Cisco JTAPI Client on PG |

| Task |
|---|
| Upgrade Tasks |
| Technology Refresh Upgrade Task Flow |
| Postupgrade Tasks |
| Follow the post upgrade tasks after each stage of upgrade. For more information, see Post Technology Refresh Configurations section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |

| Note | Maintenance window is applicable for each component until the inventory update and configurations are complete. |
|---|---|

| Stage | Component Group | Components | Notes |
|---|---|---|---|
| 1 | Cloud Connection Components | Cloud Connect | For Cloud Connect installation instructions, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| 2 | Queuing and self-service | Cisco Unified Customer Voice Portal (CVP) (Reporting Server, Call Server/VXMLServer, Unified Call Studio) | For CVP installation or upgrade instructions, see the Installation and Upgrade
                                                      				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html |
| 3 | Gateways | Cisco Virtualized Voice Browser | For VVB installation or upgrade instructions, see the Installation and Upgrade Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html . |
| IOS Gateways (If used for ingress access only. If used for Outbound Option Dialer, see stage 6 in Upgrade Flowcharts for 4000 Agents and above Deployments .) IOS VXML Gateways | Upgrade Cisco Voice Gateway IOS Version |
| 4 | Identity Service (IdS)/SSO | IdS Server | SSO is an optional feature. It exchanges authentication and authorization details between an identity provider (IdP) and an
                                             identity service (IdS). For IdS installation or upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| 5 | Agent and supervisor desktops | ECE | For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| Cisco Finesse | For Finesse installation or upgrade instructions, see the Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . |
| 6 | Reporting Management | Cisco Unified Intelligence Center (CUIC) Reporting Server | For CUIC installation or upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade Cisco Unified Intelligence Center (CUIC), you must: Enable CORS on the CUIC server, and add cors allowed_origin with the Finesse hostname. Import LD and Finesse certificates to CUIC. |
| 7 | Unified CCE Central Controller | Unified CCE Rogger and AW-HDS-DDS | The CCE components upgrade requires the following maintenance windows on the source server: First maintenance window to shut down services on Side A of source components. Second maintenance window in the middle of the upgrade to cut over from Side B to Side A. You must bring down Side B before
                                                      you bring up Side A. |
| Unified CCE Rogger Side A | Migrate the Logger database and upgrade Side A Rogger Migrate the Logger Database and Upgrade the Rogger |
| Unified CCE AW-HDS-DDS Side A | Migrate AW-HDS-DDS and then upgrade Side A Unified CCE Administration & Data Server Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server |
| Unified CCE Rogger Side B | Migrate the Logger database and upgrade Side B Rogger Migrate the Logger Database and Upgrade the Rogger |
| Unified CCE AW-HDS-DDS Side B | Migrate AW-HDS-DDS and then upgrade Side B Unified CCE Administration & Data Server Migrate the AW and HDS Database and Upgrade the Unified CCE Administration & Data Server After you upgrade AW, import the certificate of all solution components (if applicable) to all AWs. |
| External HDS | Migrate the AW and HDS Database & Upgrade the External HDS |
| Unified CCE Router | Enable Configuration Changes |
| CUIC (Reporting Templates) | For CUIC installation or upgrade instructions, see Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . |
| Standalone Live Data | To install or upgrade Live Data, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . After you upgrade Live Data (LD), you must enable CORS on the LD server, and add cors allowed_origin with Finesse hostname. |
| Database Performance Enhancement | Database Performance Enhancement |
| 8 | Collocated Peripheral Gateways and associated components | Peripheral Gateways 5 | Upgrade Peripheral Gateways You can have many PGs located on different virtual machines. Upgrade both Side A and Side B PGs. |
| Outbound Option Dialer | Upgrade Outbound Option Dialer To enable Outbound Option High Availability in the Web Setup tool, see Configure the Logger for Outbound Option section in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html . |
| CTI Server CTI OS Server | CTI OS Server is applicable only if Avaya PG is used. For installation instructions, see the CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| 9 | Peripheral Gateways and associated components not collocated | Customer Collaboration Platform | For Customer Collaboration Platform installation or upgrade instructions, see the Cisco SocialMiner Installation and Upgrade Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-installation-guides-list.html . |
| 10 | Agent and Supervisor Desktops | CTI OS Desktops | For CTI OS Desktop client installation instructions, see the CTI OS System Manager Guide for Cisco Unified ICM at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| 11 | Call Processing Components | Cisco Unified Communications Manager (Unified Communications Manager) | For installation or upgrade instructions, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service or Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| JTAPI client on Agent (Cisco Unified Communications Manager) PG | Upgrade Cisco JTAPI Client on PG |