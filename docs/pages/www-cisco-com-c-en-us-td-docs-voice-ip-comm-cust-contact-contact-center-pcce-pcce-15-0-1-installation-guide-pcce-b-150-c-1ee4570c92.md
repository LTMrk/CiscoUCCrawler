---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-installation-guide-pcce-b-150-c-1ee4570c92
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/installation/guide/pcce_b_150_cisco_pcce_installationandupgrade_guide/pcce_m_150_upgrade-overview.html
retrieved_at: 2026-08-21T12:09:19.596190+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Upgrade Overview

## Chapter: Upgrade Overview

# Upgrade Overview

Following are the two supported upgrade methods:

Common Ground Upgrades : The Common Ground method is an in-place upgrade performed on your existing virtual machine which involves upgrading the
                              Packaged CCE and all other associated software hosted on it. If your hardware meets the requirements for this release, you
                              can perform a Common Ground upgrade without acquiring additional hardware.

CCE components can be upgraded using common ground or technology refresh upgrade.

The Common Ground upgrade from Windows Server 2016 and SQL Server 2017 is only supported if an in-place platform upgrade is
                                                performed to Windows Server 2022 and SQL Server 2022, and not to Windows Server 2019 and SQL Server 2019.

The Common Ground upgrade process checks that your system is compatible with the latest updates and features. If the installer
                                                detects any unsupported features during the upgrade, it will exit the process and provide an error message specifying which
                                                components have unsupported configurations. Once these unsupported configurations are removed, you can attempt the Common
                                                Ground upgrade again. For more information about the list of unsupported features, see the Removed and Unsupported Features topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html

Technology Refresh Upgrades : Use the Technology Refresh upgrade method to set up all the virtual machines (VMs) or the required set of VMs on a different
                              hardware. You can also upgrade the solution components and the associated software hosted on it.

For better performance, install Media Routing PG (MR PG), Dialer, and Agent PG on the same VM.

During the Technology Refresh (TR) Upgrade process, the installer is designed to identify any unsupported features present
                                          in the source deployment. These features are then listed in a dialog box for you to review. You have two options on how to
                                          proceed:

Select "Yes": By choosing "Yes", you instruct the installer to exclude all the identified unsupported features during the
                                                upgrade process. The installer will proceed with the Technology Refresh Upgrade, ensuring that the unsupported features do
                                                not interfere with the updated system functionality.

Select "No": If you choose "No", the installer will terminate immediately without making any changes to the deployment.

For more information about the list of unsupported features, see the Removed and Unsupported Feature s topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html

## Upgrade Flow

### Upgrade Flowcharts for 2000 Agent Deployments

The following diagram illustrates the solution-level upgrade flow for the Packaged CCE 2000 Agent Deployment solution upgrade.

This flowchart is not applicable forredundant upgrade workflow.

Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments.

### Upgrade Flowcharts for 4000 Agents and above Deployments

The following diagram illustrates the solution-level upgrade flow for the Packaged CCE 4000 Agents and above Deployment solution
                              upgrade.

Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments.

## Silent
                        	 Upgrade

There are situations when silent upgrade can be used in running an installation wizard. You can
                              				run a silent installation while performing a fresh install or an upgrade.

For more information, see Silent Installation .

## Enable and Disable TDE on a Database

To enable Transparent Data Encryption (TDE) on a database, perform the
                              following:

These steps are to be performed with sysadmin user permission.

Create a server certificate data encryption key.

```
USE master
GO
CREATE CERTIFICATE DEKCert WITH SUBJECT = 'DEK Certificate'
GO
```

Create a backup of the server certificate data encryption key.

```
BACKUP CERTIFICATE DEKCert TO FILE = '<SystemDrive>:\DEKCert'
WITH PRIVATE KEY ( FILE = '<SystemDrive>:\temp\DEKCertPrivKey' ,
ENCRYPTION BY PASSWORD = 'C1sco123=' )
GO
```

Create database encryption key for the database to configure transparent data
                                 encryption. In the following query, ucce_sideA is the name of the active
                                 database.

```
USE ucce_sideA
GO
CREATE DATABASE ENCRYPTION KEY
WITH ALGORITHM = AES_256
ENCRYPTION BY SERVER CERTIFICATE DEKCert
GO
```

Enable database encryption. Run the following query where ucce_sideA is
                                 the name of the active database.

```
ALTER DATABASE ucce_sideA SET ENCRYPTION ON
```

By setting encryption on, a background task starts encrypting all the data
                                             pages and the log file. This can take a considerable amount of time,
                                             depending on the size of the database. Database maintenance operations
                                             should not be performed when this encryption scan is running.

To query the status of the database encryption and its percentage completion,
                                 query the new sys.dm_database_encryption_keys.

```
SELECT DB_NAME(e.database_id) AS DatabaseName,
e.database_id,
e.encryption_state,
CASE e.encryption_state
WHEN 0 THEN 'No database encryption key present, no encryption'
WHEN 1 THEN 'Unencrypted'
WHEN 2 THEN 'Encryption in progress'
WHEN 3 THEN 'Encrypted'
WHEN 4 THEN 'Key change in progress'
WHEN 5 THEN 'Decryption in progress'
END AS encryption_state_desc,
c.name,
e.percent_complete
FROM sys.dm_database_encryption_keys AS e
LEFT JOIN master.sys.certificates AS c
ON e.encryptor_thumbprint = c.thumbprint
```

```
USE master;
GO
ALTER DATABASE ucce_sideA SET ENCRYPTION OFF;
GO
-- Remove Encryption Key from Database
USE ucce_sideA;
GO
DROP DATABASE ENCRYPTION KEY;
GO
```

## Custom Truststore to Store Component Certificates

Starting Unified CCE 12.6(x), a new custom truststore is created under the Unified ICM Installation directory <ICM install directory>\ssl\cacerts to store all the component certificates. With this new custom truststore, you don't need to export and import the certificates
                           each time Java is updated in the system.

After upgrading from Unified CCE 12.5(2) to Unified CCE 15.0(1), you should export the certificates from the Java truststore
                           to the custom truststore under the Unified ICM Installation directory <ICM install directory>\ssl\cacerts .

Export the certificate from the Java truststore:

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Export the certificates of all the components imported into the truststore.

Enter the truststore password when prompted.

Import the certificate to the custom truststore:

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Import the certificates for all the components that you exported from the Java truststore.

Enter the truststore password when prompted.

Enter 'yes' when prompted to trust the certificate.

### Customers Also Viewed

- Implement CA-Signed Certificates in a CCE 12.6 Solution

| Note | CCE components can be upgraded using common ground or technology refresh upgrade. The Common Ground upgrade from Windows Server 2016 and SQL Server 2017 is only supported if an in-place platform upgrade is
                                                performed to Windows Server 2022 and SQL Server 2022, and not to Windows Server 2019 and SQL Server 2019. The Common Ground upgrade process checks that your system is compatible with the latest updates and features. If the installer
                                                detects any unsupported features during the upgrade, it will exit the process and provide an error message specifying which
                                                components have unsupported configurations. Once these unsupported configurations are removed, you can attempt the Common
                                                Ground upgrade again. For more information about the list of unsupported features, see the Removed and Unsupported Features topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html |
|---|---|

| Note | For better performance, install Media Routing PG (MR PG), Dialer, and Agent PG on the same VM. During the Technology Refresh (TR) Upgrade process, the installer is designed to identify any unsupported features present
                                          in the source deployment. These features are then listed in a dialog box for you to review. You have two options on how to
                                          proceed: Select "Yes": By choosing "Yes", you instruct the installer to exclude all the identified unsupported features during the
                                                upgrade process. The installer will proceed with the Technology Refresh Upgrade, ensuring that the unsupported features do
                                                not interfere with the updated system functionality. Select "No": If you choose "No", the installer will terminate immediately without making any changes to the deployment. For more information about the list of unsupported features, see the Removed and Unsupported Feature s topic in the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html |
|---|---|

| Note | This flowchart is not applicable forredundant upgrade workflow. |
|---|---|

| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
|---|---|

| Note | Installing Cisco Reverse Proxy is optional and is applicable only for VPN-less Finesse and digital channels deployments. |
|---|---|

| Note | These steps are to be performed with sysadmin user permission. |
|---|---|

| Note | By setting encryption on, a background task starts encrypting all the data
                                             pages and the log file. This can take a considerable amount of time,
                                             depending on the size of the database. Database maintenance operations
                                             should not be performed when this encryption scan is running. |
|---|---|