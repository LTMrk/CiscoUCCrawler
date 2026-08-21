---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-admingd-cucm-b-administration-guide-1251su1-cucm-b-test-037993cd9e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/adminGd/cucm_b_administration-guide-1251SU1/cucm_b_test-adminguide_chapter_01010.html
retrieved_at: 2026-08-21T08:34:33.205099+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: April 8, 2025

Chapter: Back Up the System

## Chapter: Back Up the System

# Back Up the System

## Backup
                        	 Overview

Cisco
                           		recommends performing regular backups. You can use the Disaster Recovery System
                           		(DRS) to do a full data backup for all servers in a cluster. You can set up
                           		automatic backups or invoke a backup at any time.

The
                           		Disaster Recovery System performs a cluster-level backup, which means that it
                           		collects backups for all servers in a Cisco Unified Communications Manager
                           		cluster to a central location and archives the backup data to physical storage
                           		device. Backup files are encrypted and can be opened only by the system
                           		software.

DRS
                           		restores its own settings (backup device settings and schedule settings) as
                           		part of the platform backup/restore. DRS backs up and restores the
                           		drfDevice.xml and drfSchedule.xml files. When the server is restored with these
                           		files, you do not need to reconfigure DRS backup device and schedule.

When you perform a system data restoration, you can choose which nodes
                           		in the cluster you want to restore.

The
                           		Disaster Recovery System includes the following capabilities:

A user interface
                                 			 for performing backup and restore tasks.

A distributed
                                 			 system architecture for performing backup functions.

Scheduled
                                 			 backups or manual (user-invoked) backups.

It archives
                                 			 backups to a remote sftp server.

The table displays the features and components that the Disaster Recovery System can back up and restore. For each feature
                           that you choose, the system backs up all its components automatically.

Feature

Components

CCM - Unified Communications Manager

Unified Communications Manager database

Platform

Serviceability

Music On Hold (MOH)

Cisco Emergency Responder

Bulk Tool (BAT)

Preference

Phone device files (TFTP)

syslogagt (SNMP syslog agent)

cdpagent (SNMP cdp agent)

tct (trace collection tool)

Call Detail Records (CDRs)

CDR Reporting and Analysis (CAR)

Feature

Components

IM and Presence Service

IM and Presence database

syslogagt (SNMP syslog agent)

cdpagent (SNMP cdp agent)

Platform

Reporter (Serviceability Reporter)

CUP SIP Proxy

XCP

CLM

Bulk Tool (BAT)

Preference

tct (trace collection tool)

## Backup
                        	 Prerequisites

Make sure that you meet the version requirements:

All Cisco Unified Communications Manager cluster nodes must be running the same version of 
                                          				 the Cisco Unified Communications Manager application.

All IM and Presence Service cluster nodes must be running the same version of 
                                          				 the IM and Presence Service application.

The software version saved in the backup file must match the version that is  running on the cluster nodes.

The entire version string must match. For example, if the IM and Presence database publisher node is at version 11.5.1.10000-1,
                                    then all IM and Presence subscriber nodes must be 11.5.1.10000-1, and the backup file must also be must be 11.5.1.10000-1.
                                    If you try to restore the system from a backup file that does not match the current version, the restore will fail. Ensure
                                    that you backup the system whenever you upgrade the software version so that the version saved in the backup file matches
                                    the version that is running on the cluster nodes.

Be aware
                                    				the DRS encryption depends on the cluster security password. When running the
                                    				backup, DRS generates a random password for encryption and then encrypts the
                                    				random password with the cluster security password. If the cluster security
                                    				password ever gets changed between the backup and this restore, you will need
                                    				to know what the password was at the time of the backup in order to use that
                                    				backup file to restore your system or take a backup immediately after the
                                    				security password change/reset.

If you want
                                    				to back up to a remote device, make sure that you have an SFTP server set up.
                                    				For more information on the available SFTP servers, see SFTP Servers for Remote Backups

## Backup Task
                        	 Flow

Complete these
                              		  tasks to configure and run a backup. Do not perform any OS Administration tasks
                              		  while a backup is running. This is because Disaster Recovery System blocks all
                              		  OS Administration requests by locking platform API. However, Disaster Recovery
                              		  System does not block most CLI commands, because only the CLI-based upgrade
                              		  commands use the Platform API locking package.

Step 1

Configure Backup Devices

Step 2

Estimate Size of Backup File

Step 3

Choose one of
                                       			 the following options:

- Configure a Scheduled Backup

- Start a Manual Backup

Create a
                                          				backup schedule to back up data on a schedule.

Optionally,
                                          				run a manual backup.

Step 4

View Current Backup Status

Optional.
                                          				Check the Status of the Backup. While a backup is running, you can check the
                                          				status of the current backup job.

Step 5

View Backup History

### Configure Backup
                           	 Devices

You can configure
                                 		  up to 10 backup devices. Perform the following steps to configure the location
                                 		  where you want to store backup files.

#### Before you begin

Ensure you
                                       				have write access to the directory path in the SFTP server to store the backup
                                       				file.

Ensure that
                                       				the username, password, server name, and directory path are valid as the DRS
                                       				Master Agent validates the configuration of the backup device.

Step 1

From Disaster
                                          			 Recovery System, select Backup > Backup
                                                				  Device .

Step 2

In the Backup
                                             				Device List window, do either of the following:

- To configure a new device,
                                             				click Add
                                                				  New .

- To edit an existing backup
                                             				device, enter the search criteria, click Find, and Edit
                                                				  Selected .

- To delete a backup device,
                                             				select it in the Backup Device list and click Delete Selected .

You cannot
                                             				delete a backup device that is configured as the backup device in a backup
                                             				schedule.

Step 3

Enter a backup
                                          			 name in the Backup
                                             				Device Name field.

The backup
                                             				device name contains only alphanumeric characters, spaces (), dashes (-) and
                                             				underscores (_). Do not use any other characters.

Step 4

In the Select
                                             				Destination area, under Network Directory perform the following:

- In the Host
                                                				  name/IP Address field, enter the hostname or IP address for the
                                             				network server.

- In the Path
                                                				  name field, enter the directory path where you want to store the
                                             				backup file.

- In the User
                                                				  name field, enter a valid username.

- In the Password field, enter a valid password.

- From the Number of backups to store on Network Directory drop-down list, choose the required number of backups.

Step 5

Click Save .

#### What to do next

Estimate Size of Backup File

### Estimate Size of
                           	 Backup File

Cisco Unified
                                 		  Communications Manager will estimate the size of the backup tar, only if a
                                 		  backup history exists for one or more selected features.

The calculated
                                 		  size is not an exact value but an estimated size of the backup tar. Size is
                                 		  calculated based on the actual backup size of a previous successful backup and
                                 		  may vary if the configuration changed since the last backup.

You can use this
                                 		  procedure only when the previous backups exist and not when you back up the
                                 		  system for the first time.

Follow this
                                 		  procedure to estimate the size of the backup tar that is saved to a SFTP
                                 		  device.

Step 1

From the
                                          			 Disaster Recovery System, select Backup > Manual
                                                				  Backup .

Step 2

In the Select
                                             				Features area, select the features to back up.

Step 3

Click Estimate Size to view the estimated size of backup
                                          			 for the selected features.

#### What to do next

Perform one of the
                                 		  following procedures to backup your system:

Configure a Scheduled Backup

Start a Manual Backup

### Configure a
                           	 Scheduled Backup

You can create up
                                 		  to 10 backup schedules. Each backup schedule has its own set of properties,
                                 		  including a schedule for automatic backups, the set of features to back up, and
                                 		  a storage location.

Be aware that
                                 		  your backup .tar files are encrypted by a randomly generated password. This
                                 		  password is then encrypted by using the cluster security password and gets
                                 		  saved along with the backup .tar files. You must remember this security
                                 		  password or take a backup immediately after the security password change or
                                 		  reset.

Caution

Schedule
                                             			 backups during off-peak hours to avoid call processing interruptions and impact
                                             			 to service.

#### Before you begin

Configure Backup Devices

Step 1

From the
                                          			 Disaster Recovery System, choose Backup Scheduler .

Step 2

In the Schedule List window, do one of the following steps
                                          			 to add a new schedule or edit an existing schedule.

- To create a new schedule,
                                             				click Add New .

- To configure an existing
                                             				schedule, click the name in the Schedule List column.

Step 3

In the scheduler window, enter a schedule name in the Schedule Name field.

You cannot
                                                         				  change the name of the default schedule.

Step 4

Select the
                                          			 backup device in the Select Backup Device area.

Step 5

Select the
                                          			 features to back up in the Select Features area. You must choose at least one
                                          			 feature.

Step 6

Choose the
                                          			 date and time when you want the backup to begin in the Start Backup at area.

Step 7

Choose the
                                          			 frequency at which you want the backup to occur in the Frequency area. The frequency can be set to Once
                                          			 Daily, Weekly, and Monthly. If you choose Weekly , you can also choose the days of the week
                                          			 when the backup will occur.

Tip

To set the
                                                         				  backup frequency to Weekly , occurring Tuesday through Saturday, click Set Default .

Step 8

To update
                                          			 these settings, click Save .

Step 9

Choose one
                                          			 of the following options:

- To enable the selected
                                             				schedules, click Enable Selected Schedules .

- To disable the selected
                                             				schedules, click Disable Selected Schedules .

- To delete the selected
                                             				schedules, click Delete Selected .

Step 10

To enable the
                                          			 schedule, click Enable Schedule .

The next
                                             				backup occurs automatically at the time that you set.

Ensure that
                                                         				  all servers in the cluster are running the same version of Cisco Unified Communications Manager or Cisco IM and Presence Service and are reachable
                                                         				  through the network. Servers that are not reachable at the time of the
                                                         				  scheduled backup will not get backed up.

#### What to do next

Estimate Size of Backup File

(Optional) View Current Backup Status

### Start a Manual
                           	 Backup

#### Before you begin

Ensure that you use a network device as the storage location for the
                                       			 backup files. Virtualized deployments of Unified Communications Manager do not support the use
                                       			 of tape drives to store backup files.

Ensure that
                                       				all cluster nodes have the same installed version of Cisco
                                          				  Unified Communications Manager or IM
                                          				  and Presence Service .

The backup
                                       				process can fail due to non availability of space on a remote server or due to
                                       				interruptions in the network connectivity. You need to start a fresh backup
                                       				after addressing the issues that caused the backup to fail.

Ensure that
                                       				there are no network interruptions.

Configure Backup Devices

Estimate Size of Backup File

Make sure
                                       				that you have a record of the cluster security password. If the cluster
                                       				security password changes after you complete this backup, you will need to know
                                       				the password or you will not be able to use the backup file to restore your
                                       				system.

While a backup
                                             			 is running, you cannot perform any tasks in Cisco Unified OS Administration or
                                             			 Cisco Unified IM and Presence OS Administration because Disaster
                                                				Recovery System locks the platform API to block all requests.
                                             			 However, Disaster
                                                				Recovery System does not block most CLI commands because only the
                                             			 CLI-based upgrade commands use the Platform API locking package.

Step 1

From the
                                          			 Disaster Recovery System, select Backup > Manual
                                                				  Backup .

Step 2

In the Manual
                                             				Backup window, select a backup device from the Backup
                                             				Device Name area.

Step 3

Choose a
                                          			 feature from the Select
                                             				Features area.

Step 4

Click Start
                                             				Backup.

#### What to do next

(Optional) View Current Backup Status

### View Current
                           	 Backup Status

Perform
                                 		  the following steps to check the status of the current backup job.

Caution

Be aware that if
                                             			 the backup to the remote server is not completed within 20 hours, the backup
                                             			 session times out and you must begin a fresh backup.

Step 1

From the
                                          			 Disaster Recovery System, select Backup > Current Status .

Step 2

To view the
                                          			 backup log file, click the log filename link.

Step 3

To cancel the
                                          			 current backup, click Cancel
                                             				Backup .

The backup
                                                         				  cancels after the current component completes its backup operation.

#### What to do next

View Backup History

### View Backup
                           	 History

Perform
                                 		  the following steps to view the backup history.

Step 1

From the
                                          			 Disaster Recovery System, select Backup > History .

Step 2

From the Backup
                                             				History window, you can view the backups that you have performed,
                                          			 including filename, backup device, completion date, result, version, features
                                          			 that are backed up, and failed features.

The Backup History window displays only the last 20
                                                         				  backup jobs.

## Backup
                        	 Interactions and Restrictions

### Backup
                           	 Restrictions

The following restrictions apply to backups:

Restriction

Description

Cluster Security Password

We recommend that you run a backup whenever you change the
                                             					 cluster security password.

Backup encryption uses the cluster security password to
                                             					 encrypt data on the backup file. If you edit the cluster security password
                                             					 after a backup file is created, you will not be able to use that backup file to
                                             					 restore data unless you remember the old password.

Certificate Management

The Disaster Recovery System (DRS) uses an
                                             					 SSL-based communication between the Master Agent and the Local Agent for
                                             					 authentication and encryption of data between the Cisco Unified Communications Manager cluster nodes. DRS makes use of the IPsec
                                             					 certificates for its Public/Private Key encryption. Be aware that if you delete
                                             					 the IPSEC truststore(hostname.pem) file from the Certificate Management pages,
                                             					 then DRS will not work as expected. If you delete the IPSEC-trust file
                                             					 manually, you must ensure that you upload the IPSEC certificate to the
                                             					 IPSEC-trust. For more details, see the "Certificate management" section in the Security Guide for Cisco Unified Communications
                                                						Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

### SFTP Servers for
                           	 Remote Backups

To back up data to a remote device on the network, you must have an SFTP server that is configured. For internal testing,
                                 Cisco uses the SFTP Server on Cisco Prime Collaboration Deployment (PCD) which is provided by Cisco, and which is supported
                                 by Cisco TAC. Refer to the following table for a summary of the SFTP server options:

Use the information in the following table to determine which SFTP server solution to use in your system.

SFTP Server

Information

SFTP Server on Cisco Prime Collaboration Deployment

This server is the only SFTP server that is provided and tested by Cisco, and fully supported by Cisco TAC.

Version compatibility depends on your version of Unified Communications Manager and Cisco Prime Collaboration Deployment.
                                             See the Cisco Prime Collaboration Deployment Administration Guide before you upgrade its version (SFTP) or Unified Communications Manager to ensure that the versions are compatible.

SFTP Server from a Technology Partner

These SFTP servers from a technology partner are third-party provided and third-party tested. Version compatibility depends
                                             on the third party test. See the Technology Partner page if you upgrade their SFTP product and/or upgrade Unified Communications
                                             Manager for which versions are compatible.

SFTP Server from another Third Party

These SFTP servers are provided by a third party and are not officially supported by Cisco TAC.

Version compatibility is on a best effort basis to establish compatible SFTP versions and Unified Communications Manager versions.

#### Cipher Support

For Unified Communications Manager 11.5, Unified Communications Manager advertises the following CBC and CTR ciphers for SFTP
                                 connections:

aes128-cbc

3des-cbc

aes128-ctr

aes192-ctr

aes256-ctr

From Unified Communications Manager 12.0 release onwards, CBC ciphers are not supported. Unified Communications Manager supports
                                 and advertises only the following CTR ciphers:

aes256-ctr

aes128-ctr

aes192-ctr

| Feature | Components |
|---|---|
| CCM - Unified Communications Manager | Unified Communications Manager database |
| Platform |
| Serviceability |
| Music On Hold (MOH) |
| Cisco Emergency Responder |
| Bulk Tool (BAT) |
| Preference |
| Phone device files (TFTP) |
| syslogagt (SNMP syslog agent) |
| cdpagent (SNMP cdp agent) |
| tct (trace collection tool) |
| Call Detail Records (CDRs) |
| CDR Reporting and Analysis (CAR) |

| Feature | Components |
|---|---|
| IM and Presence Service | IM and Presence database |
| syslogagt (SNMP syslog agent) |
| cdpagent (SNMP cdp agent) |
| Platform |
| Reporter (Serviceability Reporter) |
| CUP SIP Proxy |
| XCP |
| CLM |
| Bulk Tool (BAT) |
| Preference |
| tct (trace collection tool) |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Backup Devices | Specify the
                                       			 devices on which to back up data. |
| Step 2 | Estimate Size of Backup File | Estimate size
                                       			 of backup file created on the SFTP device. |
| Step 3 | Choose one of
                                       			 the following options: Configure a Scheduled Backup Start a Manual Backup | Create a
                                          				backup schedule to back up data on a schedule. Optionally,
                                          				run a manual backup. |
| Step 4 | View Current Backup Status | Optional.
                                          				Check the Status of the Backup. While a backup is running, you can check the
                                          				status of the current backup job. |
| Step 5 | View Backup History | Optional.
                                       			 View Backup History |

| Note | Schedule backups during periods when you expect less network traffic. |
|---|---|

| Step 1 | From Disaster
                                          			 Recovery System, select Backup > Backup
                                                				  Device . |
|---|---|
| Step 2 | In the Backup
                                             				Device List window, do either of the following: To configure a new device,
                                             				click Add
                                                				  New . To edit an existing backup
                                             				device, enter the search criteria, click Find, and Edit
                                                				  Selected . To delete a backup device,
                                             				select it in the Backup Device list and click Delete Selected . You cannot
                                             				delete a backup device that is configured as the backup device in a backup
                                             				schedule. |
| Step 3 | Enter a backup
                                          			 name in the Backup
                                             				Device Name field. The backup
                                             				device name contains only alphanumeric characters, spaces (), dashes (-) and
                                             				underscores (_). Do not use any other characters. |
| Step 4 | In the Select
                                             				Destination area, under Network Directory perform the following: In the Host
                                                				  name/IP Address field, enter the hostname or IP address for the
                                             				network server. In the Path
                                                				  name field, enter the directory path where you want to store the
                                             				backup file. In the User
                                                				  name field, enter a valid username. In the Password field, enter a valid password. From the Number of backups to store on Network Directory drop-down list, choose the required number of backups. |
| Step 5 | Click Save . |

| Step 1 | From the
                                          			 Disaster Recovery System, select Backup > Manual
                                                				  Backup . |
|---|---|
| Step 2 | In the Select
                                             				Features area, select the features to back up. |
| Step 3 | Click Estimate Size to view the estimated size of backup
                                          			 for the selected features. |

| Caution | Schedule
                                             			 backups during off-peak hours to avoid call processing interruptions and impact
                                             			 to service. |
|---|---|

| Step 1 | From the
                                          			 Disaster Recovery System, choose Backup Scheduler . |
|---|---|
| Step 2 | In the Schedule List window, do one of the following steps
                                          			 to add a new schedule or edit an existing schedule. To create a new schedule,
                                             				click Add New . To configure an existing
                                             				schedule, click the name in the Schedule List column. |
| Step 3 | In the scheduler window, enter a schedule name in the Schedule Name field. Note You cannot
                                                         				  change the name of the default schedule. | Note | You cannot
                                                         				  change the name of the default schedule. |
| Note | You cannot
                                                         				  change the name of the default schedule. |
| Step 4 | Select the
                                          			 backup device in the Select Backup Device area. |
| Step 5 | Select the
                                          			 features to back up in the Select Features area. You must choose at least one
                                          			 feature. |
| Step 6 | Choose the
                                          			 date and time when you want the backup to begin in the Start Backup at area. |
| Step 7 | Choose the
                                          			 frequency at which you want the backup to occur in the Frequency area. The frequency can be set to Once
                                          			 Daily, Weekly, and Monthly. If you choose Weekly , you can also choose the days of the week
                                          			 when the backup will occur. Tip To set the
                                                         				  backup frequency to Weekly , occurring Tuesday through Saturday, click Set Default . | Tip | To set the
                                                         				  backup frequency to Weekly , occurring Tuesday through Saturday, click Set Default . |
| Tip | To set the
                                                         				  backup frequency to Weekly , occurring Tuesday through Saturday, click Set Default . |
| Step 8 | To update
                                          			 these settings, click Save . |
| Step 9 | Choose one
                                          			 of the following options: To enable the selected
                                             				schedules, click Enable Selected Schedules . To disable the selected
                                             				schedules, click Disable Selected Schedules . To delete the selected
                                             				schedules, click Delete Selected . |
| Step 10 | To enable the
                                          			 schedule, click Enable Schedule . The next
                                             				backup occurs automatically at the time that you set. Note Ensure that
                                                         				  all servers in the cluster are running the same version of Cisco Unified Communications Manager or Cisco IM and Presence Service and are reachable
                                                         				  through the network. Servers that are not reachable at the time of the
                                                         				  scheduled backup will not get backed up. | Note | Ensure that
                                                         				  all servers in the cluster are running the same version of Cisco Unified Communications Manager or Cisco IM and Presence Service and are reachable
                                                         				  through the network. Servers that are not reachable at the time of the
                                                         				  scheduled backup will not get backed up. |
| Note | Ensure that
                                                         				  all servers in the cluster are running the same version of Cisco Unified Communications Manager or Cisco IM and Presence Service and are reachable
                                                         				  through the network. Servers that are not reachable at the time of the
                                                         				  scheduled backup will not get backed up. |

| Note | You cannot
                                                         				  change the name of the default schedule. |
|---|---|

| Tip | To set the
                                                         				  backup frequency to Weekly , occurring Tuesday through Saturday, click Set Default . |
|---|---|

| Note | Ensure that
                                                         				  all servers in the cluster are running the same version of Cisco Unified Communications Manager or Cisco IM and Presence Service and are reachable
                                                         				  through the network. Servers that are not reachable at the time of the
                                                         				  scheduled backup will not get backed up. |
|---|---|

| Note | While a backup
                                             			 is running, you cannot perform any tasks in Cisco Unified OS Administration or
                                             			 Cisco Unified IM and Presence OS Administration because Disaster
                                                				Recovery System locks the platform API to block all requests.
                                             			 However, Disaster
                                                				Recovery System does not block most CLI commands because only the
                                             			 CLI-based upgrade commands use the Platform API locking package. |
|---|---|

| Step 1 | From the
                                          			 Disaster Recovery System, select Backup > Manual
                                                				  Backup . |
|---|---|
| Step 2 | In the Manual
                                             				Backup window, select a backup device from the Backup
                                             				Device Name area. |
| Step 3 | Choose a
                                          			 feature from the Select
                                             				Features area. |
| Step 4 | Click Start
                                             				Backup. |

| Caution | Be aware that if
                                             			 the backup to the remote server is not completed within 20 hours, the backup
                                             			 session times out and you must begin a fresh backup. |
|---|---|

| Step 1 | From the
                                          			 Disaster Recovery System, select Backup > Current Status . |
|---|---|
| Step 2 | To view the
                                          			 backup log file, click the log filename link. |
| Step 3 | To cancel the
                                          			 current backup, click Cancel
                                             				Backup . Note The backup
                                                         				  cancels after the current component completes its backup operation. | Note | The backup
                                                         				  cancels after the current component completes its backup operation. |
| Note | The backup
                                                         				  cancels after the current component completes its backup operation. |

| Note | The backup
                                                         				  cancels after the current component completes its backup operation. |
|---|---|

| Step 1 | From the
                                          			 Disaster Recovery System, select Backup > History . |
|---|---|
| Step 2 | From the Backup
                                             				History window, you can view the backups that you have performed,
                                          			 including filename, backup device, completion date, result, version, features
                                          			 that are backed up, and failed features. Note The Backup History window displays only the last 20
                                                         				  backup jobs. | Note | The Backup History window displays only the last 20
                                                         				  backup jobs. |
| Note | The Backup History window displays only the last 20
                                                         				  backup jobs. |

| Note | The Backup History window displays only the last 20
                                                         				  backup jobs. |
|---|---|

| Restriction | Description |
|---|---|
| Cluster Security Password | We recommend that you run a backup whenever you change the
                                             					 cluster security password. Backup encryption uses the cluster security password to
                                             					 encrypt data on the backup file. If you edit the cluster security password
                                             					 after a backup file is created, you will not be able to use that backup file to
                                             					 restore data unless you remember the old password. |
| Certificate Management | The Disaster Recovery System (DRS) uses an
                                             					 SSL-based communication between the Master Agent and the Local Agent for
                                             					 authentication and encryption of data between the Cisco Unified Communications Manager cluster nodes. DRS makes use of the IPsec
                                             					 certificates for its Public/Private Key encryption. Be aware that if you delete
                                             					 the IPSEC truststore(hostname.pem) file from the Certificate Management pages,
                                             					 then DRS will not work as expected. If you delete the IPSEC-trust file
                                             					 manually, you must ensure that you upload the IPSEC certificate to the
                                             					 IPSEC-trust. For more details, see the "Certificate management" section in the Security Guide for Cisco Unified Communications
                                                						Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |

| SFTP Server | Information |
|---|---|
| SFTP Server on Cisco Prime Collaboration Deployment | This server is the only SFTP server that is provided and tested by Cisco, and fully supported by Cisco TAC. Version compatibility depends on your version of Unified Communications Manager and Cisco Prime Collaboration Deployment.
                                             See the Cisco Prime Collaboration Deployment Administration Guide before you upgrade its version (SFTP) or Unified Communications Manager to ensure that the versions are compatible. |
| SFTP Server from a Technology Partner | These SFTP servers from a technology partner are third-party provided and third-party tested. Version compatibility depends
                                             on the third party test. See the Technology Partner page if you upgrade their SFTP product and/or upgrade Unified Communications
                                             Manager for which versions are compatible. |
| SFTP Server from another Third Party | These SFTP servers are provided by a third party and are not officially supported by Cisco TAC. Version compatibility is on a best effort basis to establish compatible SFTP versions and Unified Communications Manager versions. Note These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                                      For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. | Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                                      For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |
| Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                                      For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |

| Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                                      For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |
|---|---|

| Note | Make sure that the backup SFTP Server supports one of these ciphers to communicate with Unified Communications Manager. |
|---|---|

| Note | Make sure that the backup SFTP Server supports one of these CTR ciphers to communicate with Unified Communications Manager. |
|---|---|