---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-8192688d0c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_150_install_upgrade_guide/technology_refresh_upgrade.html
retrieved_at: 2026-08-25T00:10:24.843101+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

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

## Technology Refresh Preupgrade Task flow

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

(Optional) Install Cisco Reverse Proxy

If you don't have Cisco Reverse Proxy in your environment and you want to use VPN-less desktop access feature or to upgrade
                                          Cisco Reverse Proxy 12.6(2) to 15.0(1), you must install Cisco Reverse Proxy 15.0(1). Refer to the Notes on VM Templates for 15.0(1) topic in the Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS page for the installer location. For more information on how to install Cisco Reverse Proxy, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) .

Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments.

Install Cloud Connect

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

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

If you are upgrading from 12.6(1) or earlier release, before bringing up the upgraded primary node, ensure that all the SSO
                                                      clients are logged out.

Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                      using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                      and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                      the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                      node is upgraded and in the IN_SERVICE status.

For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP.

Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 15.0(1) before Cisco IdS is upgraded to 15.0(1) .

For more information, see Upgrade Flowcharts .

For IdS upgrade, refer to the same steps as documented in the upgrades section of Unified Intelligence Center Installation
                                          and Upgrade Guide at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html

Upgrade Enterprise Chat and Email (ECE)

For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html

Upgrade Finesse

For more information, see Cisco Finesse Installation and Upgrade Guide Cisco Finesse Installation and Upgrade Guide at

https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html

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

### Migrate the Logger Database and Upgrade the Logger

To upgrade the Logger, do the following tasks:

Migrate the Logger database.

If you use Outbound Option High Availability, do the following:

Migrate the Outbound Option database.

Install the new software.

#### Before you begin

Create a shared folder in any desired location. Ensure that:

In the Properties window > Sharing tab > Advanced Sharing, the Share this folder check box is checked.

In the Properties window > Security tab > Advanced Sharing > Permission , the permission level is set as Full control for the user group everyone .

Step 1

Use Unified CCE Service Control to stop all Unified CCE services on the Logger.

Step 2

Download the EDMT tool from Cisco.com , and ensure prerequisites for the same are installed on the target/destination system, before launching EDMT. These include
                                          the ODBC Driver 17.10 or later minor versions of ODBC 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2022.

Step 3

Run the EDMT Tool as administrator from the server that will host the destination Logger and click Next .

Step 4

Select Technology Refresh and click Next .

Step 5

Under Source Database Connection , in the HostName\IP Address field, type the Source IP and click Refresh Database List .

Step 6

Select the Logger Database name, and click Next .

Step 7

In the Windows Share Name field, type the name of the shared folder that you created.

Step 8

In the Windows Share Password field, type the password of the destination machine.

Step 9

In the Destination Restore Location section, the destination fields for the database data file (.mdf) and the transaction log file (.ldf) are prepopulated with
                                          the default locations designated by the currently running SQL Server instance for database file storage. If you need to change
                                          these default locations, perform the following actions:

- In the Data Files Location field, browse to the folder where EDMT should create the database data file (.mdf).

In the Log Files Location field, browse to the folder where EDMT should create the transaction log file (.ldf).

Step 10

Click Next .

Step 11

Review or change the information as required and click Start Migration .

Step 12

Exit the EDMT Tool.

Step 13

(Optional) If Outbound Option High Availability is deployed, repeat steps 1
                                          					through 12 to
                                          					migrate the BA database.

Step 14

Run the setup.exe from ICM-CCE-Installer folder and click Next .

Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply .

Step 15

Select Technology Refresh and click Next .

Step 16

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 17

(Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 18

(Optional) Select SQL Server Security Hardening and click Next .

Step 19

Click OK on any informational messages that display.

Step 20

Click Install .

Step 21

Restart the server when the upgrade completes.

Step 22

Select the radio button to restart the system and click Finish .

Step 23

Open the Web Setup tool from the desktop shortcut.

Step 24

Edit the instance as necessary.

Step 25

(Optional) In case of Cross Domain upgrade, launch Web Setup , select instance and click on Change Domain to use the new domain for destination Unified CCE.

Edit instance and you might need to change the facility or instance number if required.

Step 26

(Optional) If you use Outbound Option High Availability, enable Outbound Option High Availability in the Web Setup tool. For
                                          details, see the Configure the Logger for Outbound Option topic in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

Step 27

Edit the Logger component as necessary.

Edit the Logger component. In the Summary window, update the service account management section, with a pre-existing domain user that the Logger service would run
                                             under.

If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information.

Caution

Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B.

Step 28

(Optional) If it's a Cross Domain upgrade, use the User Migration tool to import the users and OU information which you exported
                                          from the source machine during the pre-upgrade process. See User Migration Tool in Preupgrade Overview .

Step 29

Use Unified CCE Service Control to set all Unified CCE services on the new Logger to Manual Start.

### Upgrade Unified CCE Call Router

To upgrade the Call Router, do the following tasks:

Import the Cisco registry information.

Install the new software.

Set up the new Call Router using the Web Setup tool.

Step 1

Run the setup.exe from ICM-CCE-Installer folder and click Next .

Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply .

Step 2

Select Technology Refresh and click Next .

Step 3

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 4

(Optional)-To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 5

Click OK on any informational messages that display.

Step 6

Click Install .

Step 7

Restart the server when the upgrade completes.

Step 8

Select the radio button to restart the system and click Finish .

Step 9

Open the Web Setup tool from the desktop shortcut.

Step 10

Edit the instance as necessary.

For a domain change, change the domain of the instance. Additionally, you might need to change the facility or instance number
                                             as required.

Step 11

Edit the Call Router component as necessary.

If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Router, update this information.

Step 12

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

Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT.

Step 3

Run the EDMT tool as administrator on the destination server that hosts the Administration and Data Server with HDS database and click Next . For non-HDS Server configurations, skip to step 11.

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

In the Windows Share Password field, type the password of the destination machine.

Step 10

In the Destination Restore Location section, the destination fields for the database data file (.mdf) and the transaction log file (.ldf) are prepopulated with
                                          the default locations designated by the currently running SQL Server instance for database file storage. If you need to change
                                          these default locations, perform the following actions:

- In the Data Files Location field, browse to the folder where EDMT should create the database data file (.mdf).

In the Log Files Location field, browse to the folder where EDMT should create the transaction log file (.ldf).

Step 11

Click Next .

Step 12

Review or change the information as required, highlight the HDS database, and click Start Migration .

Step 13

Exit the EDMT tool.

Step 14

Run the setup.exe from ICM-CCE-Installer folder and click Next .

Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply .

Step 15

Select Technology Refresh and click Next .

Step 16

Click Browse and specify the path for the RegUtil file you exported from the source machine
                                          					during the preupgrade process.

Step 17

(Optional) To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 18

(Optional) Select SQL Server Security Hardening and click Next .

Step 19

Click OK on any informational messages that display.

Step 20

Click Install .

Step 21

Restart the server when the upgrade completes.

Step 22

Open the Web Setup tool from the desktop shortcut.

Step 23

Edit the instance as necessary.

Step 24

(Optional) In case of Cross Domain upgrade, launch Websetup , select the instance and click on Change Domain in order to use the new domain for destination Unified CCE.

Edit the instance. You might need to change the facility or instance number if required.

Step 25

Edit the Administration & Data Server component as necessary and in the Summary window, update the Service Account manager with the domain user to perform the service operation.

If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information.

Caution

Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B.

For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine .

Step 26

Use Unified CCE Service Control to set all Unified CCE services on the new Administration & Data Server to Manual Start.

Step 27

Start the Unified CCE services for Logger and Router on both Side A and Side B. Also, start the Distributor service for the
                                          all sites. Then, launch the Configuration Manager tool to check if it is working fine.

The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                               size, the longer it takes to migrate) and the server hardware performance level.

If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                               Side B Destination machines if both the sides have been migrated successfully.

If new VOS components are being deployed, remove the older VOS components from CCE Administration and then add the new ones.

### Synchronizing or Updating Configuration and Historical Data from Production Server to Staged Server During Cut Over

The EDMT tool can also be used to migrate data from a Logger or HDS production server, to the one that has already been staged
                              on version 15.0(1) . These two pronged upgrade steps are typically performed to reduce the downtime needed during cut-over to the new version.

While the parallel 15.0(1) systems are staged and tested, the 12.5(x) and 12.6(x) production servers continue to process calls.
                              On the day of the cut-over, the data in the 15.0(1) staged servers can be updated or synchronized with that of the production
                              server, by running the EDMT tool, for each of the Logger and HDS database.

Stop the Logger, AW-HDS, and Apache Tomcat services on 15.0(1) staged systems, before running EDMT tool to synchronize the
                                          data from production server.

### Upgrade Peripheral Gateways

You can upgrade different Peripheral Gateways (PG) within a contact center at different times within different maintenance
                                 windows. However, upgrade all PGs that reside on the same virtual machine and redundant PGs (Side A and corresponding Side
                                 B) during the same maintenance window.

The following dependencies occur when upgrading the Unified Communications Manager PG:

If your contact center uses Outbound Option, upgrade any Outbound Option Dialers associated with Unified Communications Manager
                                       PGs at the same time.

If the Unified Communications Manager application is upgraded, upgrade the JTAPI client associated with the Unified Communications
                                       Manager PG at the same time.

Step 1

Use Unified CCE Service Control to stop all Unified CCE  services on the PG server. Change the services to Manual Start.

Step 2

Run setup.exe from the ICM-CCE-Installer and click Next .

Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply .

Step 3

Select Technology Refresh and click Next .

Step 4

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 5

(Optional) To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

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

Open the Peripheral Gateway Setup tool from the Installer dialog or desktop shortcut, and edit the Dialer and Agent PG as
                                             needed. When editing Agent PG, remove the user password and re-enter the same password under CUCM parameters to encrypt the
                                             JTAPI password.

Step 11

Use Unified CCE Service Control to set all Unified CCE services to Automatic Start.

Step 12

For the Agent PG, run the CceCrypTool to encrypt the JTAPI password.

To run CceCrypTool, open command prompt in administrator mode and run the following command:

For example:

CceCrypTool /instance ucce /component PG1A /proc jgw1 /mode encrypt

### Upgrade Outbound
                           	 Option Dialer

To upgrade the Outbound Option Dialer, import the Cisco registry information, install the new software, and set up the new
                                 Dialer using the PG Setup tool.

#### Before you begin

Step 1

Run the setup.exe from ICM-CCE-Installer folder and click Next .

Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply .

Step 2

Select Technology Refresh and click Next .

Step 3

Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process.

Step 4

(Optional) To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next .

Step 5

Click OK on any informational messages that display.

Step 6

Click Install .

Step 7

Reboot the
                                          			 system after the upgrade completes.

Step 8

Open the Peripheral Gateway Setup tool from the Installer dialog box or desktop shortcut and edit the Dialer as required.

Step 9

Use Unified CCE Service Control to set all Unified CCE services to Automatic
                                          					Start.

### Upgrade Unified CCE Administration Client

Microsoft supports in-place Operating System upgrade from Windows 10 to Windows 11. Before perfroming in-place Operating System
                                 upgrade to Windows 11, refer to Unified CCE Virtualisation and modify the VM specification applicable for Windows 11 Operating System.

For Windows 11, the SecureBoot and TPM devices are mandatory which must be added before performing in-place Operating System
                                             upgrade from Windows 10 to Windows 11. For more information about installing Microsoft Windows 11, see the Install Microsoft Windows 11 for Administration Client .

| Note | During the Technology Refresh (TR) Upgrade process, the installer is designed to identify any unsupported features present
                                       in the source deployment. These features are then listed in a dialog box for you to review. You have two options on how to
                                       proceed: Select "Yes": By choosing "Yes", you instruct the installer to exclude all the identified unsupported features during the
                                             upgrade process. The installer will proceed with the Technology Refresh Upgrade, ensuring that the unsupported features do
                                             not interfere with the updated system functionality. Select "No": If you choose "No", the installer will terminate immediately without making any changes to the deployment. For more information about the list of unsupported features, see the Removed and Unsupported Features topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html |
|---|---|

| Note | Ensure that Internet Information Services (IIS) is disabled on Windows Server before installing Unified CCE software with
                                       the ICM-CCE-Installer. |
|---|---|

| Note | If the system is enabled with TDE, see Enable and Disable TDE on a Database . |
|---|---|

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
| (Optional) Install Cisco Reverse Proxy | If you don't have Cisco Reverse Proxy in your environment and you want to use VPN-less desktop access feature or to upgrade
                                          Cisco Reverse Proxy 12.6(2) to 15.0(1), you must install Cisco Reverse Proxy 15.0(1). Refer to the Notes on VM Templates for 15.0(1) topic in the Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS page for the installer location. For more information on how to install Cisco Reverse Proxy, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) . Note Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. | Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
| Cloud Connection Components |
| Install Cloud Connect | https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
| Queuing and self-service components |
| Upgrade Cisco Unified Customer Voice Portal 1 | Installation and Upgrade
                                                   				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html |
| Infrastructure and media resource components |
| Upgrade voice and data gateways | Upgrade Voice and Data Gateways |
| Identity Service/SSO |
| Identity Service (IdS) /Single Sign-On(SSO) | SSO is an optional feature and exchanges authentication and authorization details between an identity provider (IdP) and an
                                          identity service (IdS). Note If you are upgrading from 12.6(1) or earlier release, before bringing up the upgraded primary node, ensure that all the SSO
                                                      clients are logged out. Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                      using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                      and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                      the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                      node is upgraded and in the IN_SERVICE status. For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP. Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 15.0(1) before Cisco IdS is upgraded to 15.0(1) . For more information, see Upgrade Flowcharts . For IdS upgrade, refer to the same steps as documented in the upgrades section of Unified Intelligence Center Installation
                                          and Upgrade Guide at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html | Note | If you are upgrading from 12.6(1) or earlier release, before bringing up the upgraded primary node, ensure that all the SSO
                                                      clients are logged out. Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                      using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                      and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                      the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                      node is upgraded and in the IN_SERVICE status. For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP. Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 15.0(1) before Cisco IdS is upgraded to 15.0(1) . |
| Note | If you are upgrading from 12.6(1) or earlier release, before bringing up the upgraded primary node, ensure that all the SSO
                                                      clients are logged out. Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                      using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                      and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                      the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                      node is upgraded and in the IN_SERVICE status. For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP. Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 15.0(1) before Cisco IdS is upgraded to 15.0(1) . |
| Upgrade Enterprise Chat and Email (ECE) | For ECE installation or upgrade instructions, see the Enterprise Chat and Email Installation and Configuration Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html |
| Upgrade Finesse | For more information, see Cisco Finesse Installation and Upgrade Guide Cisco Finesse Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html |
| Reporting server |
| Upgrade Cisco Unified Intelligence Center server | Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html |
| Unified CCE Central Controller and Administration & Data Server components |
|  |
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
|  |  |
|  |
|  |  |
| Call Processing components |
| Upgrade Cisco Unified Communications Manager | Upgrade Guide for Cisco
                                                   				  Unified Communications Manager at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/tsd-products-support-install-and-upgrade-technotes-list.html |
| (Install) the JTAPI client on the Cisco Unified Communications Manager PG | Upgrade Cisco JTAPI Client on PG |

| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
|---|---|

| Note | If you are upgrading from 12.6(1) or earlier release, before bringing up the upgraded primary node, ensure that all the SSO
                                                      clients are logged out. Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                      using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                      and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                      the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                      node is upgraded and in the IN_SERVICE status. For SSO login using OKTA Identity Provider, execute admin cli utils ids set_property IS_IdP_OKTA true and reestablish IdS-IdP trust by exchanging metadata between IdS and IdP. Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 15.0(1) before Cisco IdS is upgraded to 15.0(1) . |
|---|---|

| Note | If the user group everyone is not available, add it using the Add button. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE services on the Logger. |
|---|---|
| Step 2 | Download the EDMT tool from Cisco.com , and ensure prerequisites for the same are installed on the target/destination system, before launching EDMT. These include
                                          the ODBC Driver 17.10 or later minor versions of ODBC 17 for SQL Server, and Visual C++ Redistributable for Visual Studio 2022. |
| Step 3 | Run the EDMT Tool as administrator from the server that will host the destination Logger and click Next . |
| Step 4 | Select Technology Refresh and click Next . |
| Step 5 | Under Source Database Connection , in the HostName\IP Address field, type the Source IP and click Refresh Database List . |
| Step 6 | Select the Logger Database name, and click Next . |
| Step 7 | In the Windows Share Name field, type the name of the shared folder that you created. |
| Step 8 | In the Windows Share Password field, type the password of the destination machine. |
| Step 9 | In the Destination Restore Location section, the destination fields for the database data file (.mdf) and the transaction log file (.ldf) are prepopulated with
                                          the default locations designated by the currently running SQL Server instance for database file storage. If you need to change
                                          these default locations, perform the following actions: In the Data Files Location field, browse to the folder where EDMT should create the database data file (.mdf). In the Log Files Location field, browse to the folder where EDMT should create the transaction log file (.ldf). |
| Step 10 | Click Next . |
| Step 11 | Review or change the information as required and click Start Migration . |
| Step 12 | Exit the EDMT Tool. |
| Step 13 | (Optional) If Outbound Option High Availability is deployed, repeat steps 1
                                          					through 12 to
                                          					migrate the BA database. |
| Step 14 | Run the setup.exe from ICM-CCE-Installer folder and click Next . Note Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . | Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
| Step 15 | Select Technology Refresh and click Next . |
| Step 16 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 17 | (Optional) To apply the Unified ICM  Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 18 | (Optional) Select SQL Server Security Hardening and click Next . |
| Step 19 | Click OK on any informational messages that display. |
| Step 20 | Click Install . |
| Step 21 | Restart the server when the upgrade completes. |
| Step 22 | Select the radio button to restart the system and click Finish . |
| Step 23 | Open the Web Setup tool from the desktop shortcut. |
| Step 24 | Edit the instance as necessary. |
| Step 25 | (Optional) In case of Cross Domain upgrade, launch Web Setup , select instance and click on Change Domain to use the new domain for destination Unified CCE. Edit instance and you might need to change the facility or instance number if required. |
| Step 26 | (Optional) If you use Outbound Option High Availability, enable Outbound Option High Availability in the Web Setup tool. For
                                          details, see the Configure the Logger for Outbound Option topic in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html . |
| Step 27 | Edit the Logger component as necessary. Edit the Logger component. In the Summary window, update the service account management section, with a pre-existing domain user that the Logger service would run
                                             under. If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information. Note Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. Caution Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. | Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. | Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
| Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. |
| Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
| Step 28 | (Optional) If it's a Cross Domain upgrade, use the User Migration tool to import the users and OU information which you exported
                                          from the source machine during the pre-upgrade process. See User Migration Tool in Preupgrade Overview . |
| Step 29 | Use Unified CCE Service Control to set all Unified CCE services on the new Logger to Manual Start. |

| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
|---|---|

| Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. |
|---|---|

| Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
|---|---|

| Step 1 | Run the setup.exe from ICM-CCE-Installer folder and click Next . Note Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . | Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
|---|---|---|---|
| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
| Step 2 | Select Technology Refresh and click Next . |
| Step 3 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 4 | (Optional)-To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 5 | Click OK on any informational messages that display. |
| Step 6 | Click Install . |
| Step 7 | Restart the server when the upgrade completes. |
| Step 8 | Select the radio button to restart the system and click Finish . |
| Step 9 | Open the Web Setup tool from the desktop shortcut. |
| Step 10 | Edit the instance as necessary. For a domain change, change the domain of the instance. Additionally, you might need to change the facility or instance number
                                             as required. |
| Step 11 | Edit the Call Router component as necessary. If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Router, update this information. |
| Step 12 | Use Unified CCE Service Control to set all Unified CCE services on the new Call Router to Manual Start. |

| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
|---|---|

| Note | If the user group everyone is not available, add it using the Add button. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE services on the server. |
|---|---|
| Step 2 | Download the EDMT tool from Cisco.com , and ensure pre-requisites for the same have been installed on the target/destination system, prior to launching EDMT. |
| Step 3 | Run the EDMT tool as administrator on the destination server that hosts the Administration and Data Server with HDS database and click Next . For non-HDS Server configurations, skip to step 11. |
| Step 4 | Select Technology Refresh and click Next . |
| Step 5 | Under Source Database Connection , in the HostName\IP Address field, type the Source IP, and click Refresh Database List . |
| Step 6 | Under Destination Database Connection , in the SQL Server Port Number field, enter the destination SQL server port number, and then click Next . |
| Step 7 | Select the HDS Database name, and click Next . |
| Step 8 | In the Windows Share Name field, type the name of the shared folder that you created. |
| Step 9 | In the Windows Share Password field, type the password of the destination machine. |
| Step 10 | In the Destination Restore Location section, the destination fields for the database data file (.mdf) and the transaction log file (.ldf) are prepopulated with
                                          the default locations designated by the currently running SQL Server instance for database file storage. If you need to change
                                          these default locations, perform the following actions: In the Data Files Location field, browse to the folder where EDMT should create the database data file (.mdf). In the Log Files Location field, browse to the folder where EDMT should create the transaction log file (.ldf). |
| Step 11 | Click Next . |
| Step 12 | Review or change the information as required, highlight the HDS database, and click Start Migration . |
| Step 13 | Exit the EDMT tool. |
| Step 14 | Run the setup.exe from ICM-CCE-Installer folder and click Next . Note Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . | Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
| Step 15 | Select Technology Refresh and click Next . |
| Step 16 | Click Browse and specify the path for the RegUtil file you exported from the source machine
                                          					during the preupgrade process. |
| Step 17 | (Optional) To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 18 | (Optional) Select SQL Server Security Hardening and click Next . |
| Step 19 | Click OK on any informational messages that display. |
| Step 20 | Click Install . |
| Step 21 | Restart the server when the upgrade completes. |
| Step 22 | Open the Web Setup tool from the desktop shortcut. |
| Step 23 | Edit the instance as necessary. |
| Step 24 | (Optional) In case of Cross Domain upgrade, launch Websetup , select the instance and click on Change Domain in order to use the new domain for destination Unified CCE. Edit the instance. You might need to change the facility or instance number if required. |
| Step 25 | Edit the Administration & Data Server component as necessary and in the Summary window, update the Service Account manager with the domain user to perform the service operation. If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information. Note Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. Caution Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. For more information about configuring permissions in your local machine, see Configure Permissions in the Local Machine . | Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. | Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
| Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. |
| Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
| Step 26 | Use Unified CCE Service Control to set all Unified CCE services on the new Administration & Data Server to Manual Start. |
| Step 27 | Start the Unified CCE services for Logger and Router on both Side A and Side B. Also, start the Distributor service for the
                                          all sites. Then, launch the Configuration Manager tool to check if it is working fine. Note The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                               size, the longer it takes to migrate) and the server hardware performance level. If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                               Side B Destination machines if both the sides have been migrated successfully. If new VOS components are being deployed, remove the older VOS components from CCE Administration and then add the new ones. | Note | The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                               size, the longer it takes to migrate) and the server hardware performance level. If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                               Side B Destination machines if both the sides have been migrated successfully. If new VOS components are being deployed, remove the older VOS components from CCE Administration and then add the new ones. |
| Note | The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                               size, the longer it takes to migrate) and the server hardware performance level. If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                               Side B Destination machines if both the sides have been migrated successfully. If new VOS components are being deployed, remove the older VOS components from CCE Administration and then add the new ones. |

| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
|---|---|

| Note | Ensure that the domain user is created in the new domain to perform the service operation of Loggers and Administration & Data Servers component. |
|---|---|

| Caution | Use the same domain user account for all the distributor and logger services. If you want to use different domain accounts
                                                         for the logger and the distributor, ensure that the distributor service user account is added to the local logger UcceService groups on Side A and Side B. |
|---|---|

| Note | The time required to complete a data migration varies in a direct relationship to the database size (the larger the database
                                                               size, the longer it takes to migrate) and the server hardware performance level. If Outbound Options High Availability was disabled on source machines prior to the upgrade, you can enable it on Side A and
                                                               Side B Destination machines if both the sides have been migrated successfully. If new VOS components are being deployed, remove the older VOS components from CCE Administration and then add the new ones. |
|---|---|

| Note | Stop the Logger, AW-HDS, and Apache Tomcat services on 15.0(1) staged systems, before running EDMT tool to synchronize the
                                          data from production server. |
|---|---|

| Step 1 | Use Unified CCE Service Control to stop all Unified CCE  services on the PG server. Change the services to Manual Start. |
|---|---|
| Step 2 | Run setup.exe from the ICM-CCE-Installer and click Next . Note Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . | Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
| Step 3 | Select Technology Refresh and click Next . |
| Step 4 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 5 | (Optional) To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 6 | Click OK on any informational messages that display. |
| Step 7 | Click Install . |
| Step 8 | Reboot the system after the upgrade completes. |
| Step 9 | After reboot, open the Peripheral Gateway Setup tool from the desktop shortcut and make any necessary changes. See the "Install"
                                          section of this document for specific information. If there are references to out-of-date network interface names or IP addresses for the public and private networks for the
                                             Logger, update this information. |
| Step 10 | Open the Peripheral Gateway Setup tool from the Installer dialog or desktop shortcut, and edit the Dialer and Agent PG as
                                             needed. When editing Agent PG, remove the user password and re-enter the same password under CUCM parameters to encrypt the
                                             JTAPI password. |
| Step 11 | Use Unified CCE Service Control to set all Unified CCE services to Automatic Start. |
| Step 12 | For the Agent PG, run the CceCrypTool to encrypt the JTAPI password. To run CceCrypTool, open command prompt in administrator mode and run the following command: CceCrypTool /instance <instance_name> /component <name of the component> /proc <name of the process> /mode <encrypt> For example: CceCrypTool /instance ucce /component PG1A /proc jgw1 /mode encrypt |

| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
|---|---|

| Step 1 | Run the setup.exe from ICM-CCE-Installer folder and click Next . Note Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . | Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
|---|---|---|---|
| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
| Step 2 | Select Technology Refresh and click Next . |
| Step 3 | Click Browse and specify the path for the RegUtil file you exported from the source machine during the preupgrade process. |
| Step 4 | (Optional) To apply any Minor/Maintenance Release, click Browse and navigate to the Minor/Maintenance Release software. Click Next . |
| Step 5 | Click OK on any informational messages that display. |
| Step 6 | Click Install . |
| Step 7 | Reboot the
                                          			 system after the upgrade completes. |
| Step 8 | Open the Peripheral Gateway Setup tool from the Installer dialog box or desktop shortcut and edit the Dialer as required. |
| Step 9 | Use Unified CCE Service Control to set all Unified CCE services to Automatic
                                          					Start. |

| Note | Before running setup.exe, right-click on the setup.exe and check its properties to ensure that it is not marked as blocked,
                                                         else select the unblock checkbox and click Apply . |
|---|---|

| Note | For Windows 11, the SecureBoot and TPM devices are mandatory which must be added before performing in-place Operating System
                                             upgrade from Windows 10 to Windows 11. For more information about installing Microsoft Windows 11, see the Install Microsoft Windows 11 for Administration Client . |
|---|---|