---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-installation-guide-pcce-b-1262--92e00751d4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/installation/guide/pcce_b_1262_cisco_pcce_installationandupgrade_guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_chapter_0111.html
retrieved_at: 2026-08-21T04:50:48.063099+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: March 9, 2026

Chapter: Upgrade Overview

## Chapter: Upgrade Overview

# Upgrade Overview

Following are the two supported upgrade methods:

Common Ground Upgrades : The Common Ground method is an in-place upgrade performed on your existing virtual machine which involves upgrading the
                              Packaged CCE and all other associated software hosted on it. If your hardware meets the requirements for this release, you
                              can perform a Common Ground upgrade without acquiring additional hardware.

CCE components can be upgraded using common ground or technology refresh upgrade.

Common Ground Upgrade is not supported if the platform upgrade from Windows Server 2016 and SQL Server 2017 to Windows Server
                                                2019 and SQL Server 2019 is planned as part of upgrade process.

Technology Refresh Upgrades : Use the Technology Refresh upgrade method to set up all the virtual machines (VMs) or the required set of VMs on a different
                              hardware. You can also upgrade the solution components and the associated software hosted on it.

For better performance, Media Routing PG (MR PG), Dialer, and Agent PG should be on the same VM.

## Upgrade Flow

### Upgrade Flowcharts for 2000 Agent Deployments

The following diagram illustrates the solution-level upgrade flow for the Packaged CCE 2000 Agent Deployment solution upgrade.

This flowchart is not applicable for redundant upgrade workflow.

The following diagrams illustrate the stages of the component-level upgrade flows for the Packaged CCE 2000 Agent Deployment solution upgrade. Each diagram covers one of the stages. The letter at the end of each flow indicates
                              the start of the next flow that you are required to perform.

### Upgrade Flowcharts for 4000 Agents and above Deployments

The following diagram illustrates the solution-level upgrade flow for the Packaged CCE 4000 Agents and above Deployment solution
                              upgrade.

The following diagrams illustrate the stages of the component-level upgrade flows for the Packaged CCE 4000 Agents and above
                              Deployment solution upgrade. Each diagram covers one of the stages. The letter at the end of each flow indicates the start
                              of the next flow that you are required to perform.

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

## Upgrade CCE Minor/Maintenance Release Software

To perform the upgrade from CCE 12.5(x) or CCE 12.6(1) release, do the following:

Step 1

Log in to your system using domain credentials with administrative privileges.

Step 2

Launch the CCE 12.6(2) installation wizard. Click Next to proceed.

Step 3

Select the radio button to accept the license agreement and click Next .

Step 4

Click Install to begin the installation.

Step 5

Select the radio button to restart the system and click Finish .

## Custom Truststore to Store Component Certificates

Starting Unified CCE 12.6(x), a new custom truststore is created under the Unified ICM Installation directory <ICM install directory>\ssl\cacerts to store all the component certificates. With this new custom truststore, you don't need to export and import the certificates
                           each time Java is updated in the system.

After upgrading from Unified CCE 12.5(x) to Unified CCE 12.6(x), you should export the certificates from the Java truststore
                           to the custom truststore under the Unified ICM Installation directory <ICM install directory>\ssl\cacerts .

Export the certificate from the Java truststore:

Run the command at the command prompt: cd %JAVA_HOME%\bin .

Important

Export the certificates of all the components imported into the truststore.

Enter the truststore password when prompted.

Import the certificate to the custom truststore:

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Import the certificates for all the components that you exported from the Java truststore.

Enter the truststore password when prompted.

Enter 'yes' when prompted to trust the certificate.

| Note | CCE components can be upgraded using common ground or technology refresh upgrade. Common Ground Upgrade is not supported if the platform upgrade from Windows Server 2016 and SQL Server 2017 to Windows Server
                                                2019 and SQL Server 2019 is planned as part of upgrade process. |
|---|---|

| Note | For better performance, Media Routing PG (MR PG), Dialer, and Agent PG should be on the same VM. |
|---|---|

| Note | This flowchart is not applicable for redundant upgrade workflow. |
|---|---|

| Note | These steps are to be performed with sysadmin user permission. |
|---|---|

| Note | By setting encryption on, a background task starts encrypting all the data
                                             pages and the log file. This can take a considerable amount of time,
                                             depending on the size of the database. Database maintenance operations
                                             should not be performed when this encryption scan is running. |
|---|---|

| Step 1 | Log in to your system using domain credentials with administrative privileges. |
|---|---|
| Step 2 | Launch the CCE 12.6(2) installation wizard. Click Next to proceed. |
| Step 3 | Select the radio button to accept the license agreement and click Next . |
| Step 4 | Click Install to begin the installation. |
| Step 5 | Select the radio button to restart the system and click Finish . |

| Important | Use CCE_JAVA_HOME if upgrading from Unified CCE 12.5(1a) or Unified CCE 12.5(1) with ES55 (mandatory OpenJDK ES). |
|---|---|