---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214287-configure-an-612d5fae9c
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214287-configure-and-troubleshoot-cisco-unified.html
retrieved_at: 2026-08-21T13:58:46.876457+00:00
---

Configure and Troubleshoot Cisco Unified Communication Manager (CUCM) Backups

# Configure and Troubleshoot Cisco Unified Communication Manager (CUCM) Backups

### Download Options

Updated: September 17, 2019

Document ID: 214287

Contents

## Contents

## Introduction

This document describes the procedure to add a backup device to Cisco Unified Communication Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communication Manager (CUCM)

- Secure File Transfer Protocol (SFTP) server administration

### Components Used

- Cisco Unified Communications Manager 11.5

- Linux SFTP server

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The goal of backups available in your environment with any software is to be able to recover in case of disaster. Backups are important in order to prevent loss of data when software is corrupted, hardware fails, or natural disasters occur.

CUCM and SFTP topology as shown in the image:

## Configure

### Add Backup Device via GUI Procedure

Step 1. Navigate to CUCM > Disaster Recovery System > Backup > Backup Device and click on Add New as shown in the images :

Step 2. Add a Backup Device name, IP address, Path name, User name and Password as shown in the images:

- The IP Address must be the destination SFTP server where backups are stored.

- The Path name is the directory within the SFTP server where backups are stored.

- User name and Password must exist within the SFTP server for authentication purposes.

- The Number of backups to store in the Network Directory must be set to the number of backups that need to be kept within the SFTP directory.

When finished, click Save .

Confirm Update successful as shown in the image:

### Add Backup Device via CLI Procedure

Step 1. Secure Shell (SSH) into the IP address of the CUCM Publisher and authenticate with the Operating System (OS) username and password as shown in the images:

Step 2. Add the backup device with the syntax: utils disaster_recovery device add network <backup device name> <path> <ip-address of remote server> <username> [number of backups] as shown in the image:

At the time of this Add Backup Device procedure, these steps take place in CUCM:

- Contact the SFTP server and authenticate

- Transfer a test file to the directory

- Disconnect from the SFTP server

- Contact the SFTP server and authenticate

- Delete the test file in the directory

- Disconnect from the SFTP server

Note : If any of these steps fail, CUCM is unable to add the backup device.

#### Log Analysis of Add a Backup Device

+++++++++++++++++++++++++++++++++++++++++++++++++++ UpdateDestination request is sent to add new backup destination +++++++++++++++++++++++++++++++++++++++++++++++++++

2018-12-24 11:39:22,494 DEBUG [NetMessageDispatch] - drfMessageValidator.validateMessage(): Starting introspection for Message ID = 3200 Message Body = ========== BEGIN msgSubUpdateDestination_REQ ========== devicepath     : /UCM/Backups/ devicetype      : NETWORK hostname  : 192.X.X.250 m_iBackupSetCount : 1 password : 8f5fcb108a798014abff9ab4fc006f2a83027d6c858f0ac9b2720a32ba1b8d3c storagelocationname  : TAC-Backup username   : cisco version : 1.0.0 schedules : [] ========== END msgSubUpdateDestination_REQ ==========

++++++++++++++++++++++++++++++++++++++ CUCM attempts to connect to the SFTP server ++++++++++++++++++++++++++++++++++++++

2018-12-24 11:39:23,168 DEBUG [NetMessageDispatch] - drfUtils:establishSftpConnection: Trying to connect to the SFTP server. 2018-12-24 11:39:23,171 DEBUG [NetMessageDispatch] - drfUtils:establishSftpConnection: Connecting SFTP server...

+++++++++++++++++++++++++++++++ Authentication Completed Successfully +++++++++++++++++++++++++++++++

2018-12-24 11:39:23,373 DEBUG [NetMessageDispatch] - drfUtils:establishSftpConnection: Authentication Completed Successfully, connected to remote server. Now opening a SFTP channel. 2018-12-24 11:39:23,580 DEBUG [NetMessageDispatch] - drfUtils:sftpPutFile: SSH Authentication success for user cisco on 192.X.X.250

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ CUCM transfers files from: /common/drf/d3-sb-11pub_dUmmI_Drf to the server: 192.X.X.250 /UCM/Backups/d3-sb-11pub_dUmmI_Drf This is done to confirm if CUCM has read/write privileges. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

2018-12-24 11:39:23,581 DEBUG [NetMessageDispatch] - drfUtils:sftpPutFile: Transferring files from: /common/drf/d3-sb-11pub_dUmmI_Drf to the server: 192.X.X.250 /UCM/Backups/d3-sb-11pub_dUmmI_Drf 2018-12-24 11:39:23,581 DEBUG [NetMessageDispatch] - drfSftpProgressMonitor:: STARTING: 0 /common/drf/d3-sb-11pub_dUmmI_Drf -> /UCM/Backups/d3-sb-11pub_dUmmI_Drf total: 0

+++++++++++++++++++ File Transfer Completed +++++++++++++++++++

2018-12-24 11:39:23,585 DEBUG [NetMessageDispatch] - drfSftpProgressMonitor:: ...File Transfer Completed

++++++++++++++++++++++ CUCM closes ChannelSftp... ++++++++++++++++++++++

2018-12-24 11:39:23,586 DEBUG [NetMessageDispatch] - drfUtils:closeSFTPConnections: Closing ChannelSftp... 2018-12-24 11:39:23,586 DEBUG [NetMessageDispatch] - drfUtils:closeSFTPConnections: Disconnecting Channel... 2018-12-24 11:39:23,586 DEBUG [NetMessageDispatch] - drfUtils:closeSFTPConnections: Closing Session...

++++++++++++++++++++++++++++++++++++ CUCM attempts to connect to the SFTP server ++++++++++++++++++++++++++++++++++++

2018-12-24 11:39:23,586 DEBUG [NetMessageDispatch] - drfUtils:establishSftpConnection: Trying to connect to the SFTP server. 2018-12-24 11:39:23,587 DEBUG [NetMessageDispatch] - drfUtils:establishSftpConnection: Connecting SFTP server...

+++++++++++++++++++++++++++++++ Authentication Completed Successfully +++++++++++++++++++++++++++++++

2018-12-24 11:39:23,733 DEBUG [NetMessageDispatch] - drfUtils:establishSftpConnection: Authentication Completed Successfully, connected to remote server. Now opening a SFTP channel.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ CUCM deletes files /UCM/Backups/d3-sb-11pub_dUmmI_Drf from the server: 192.X.X.250 This is done to confirm if CUCM has read/write privileges. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

2018-12-24 11:39:24,277 DEBUG [NetMessageDispatch] - drfUtils:sftpDeleteFile: Deleting files /UCM/Backups/d3-sb-11pub_dUmmI_Drf from the server: 192.X.X.250

+++++++++++++++++ Successfully deleted +++++++++++++++++

2018-12-24 11:39:24,277 INFO [NetMessageDispatch] - drfutils.sftpDeleteFiles: Successfully deleted /UCM/Backups/d3-sb-11pub_dUmmI_Drf on the Server 192.X.X.250

++++++++++++++++++++++ CUCM closes ChannelSftp... ++++++++++++++++++++++

2018-12-24 11:39:24,278 DEBUG [NetMessageDispatch] - drfUtils:closeSFTPConnections: Closing ChannelSftp... 2018-12-24 11:39:24,278 DEBUG [NetMessageDispatch] - drfUtils:closeSFTPConnections: Disconnecting Channel... 2018-12-24 11:39:24,278 DEBUG [NetMessageDispatch] - drfUtils:closeSFTPConnections: Closing Session... 2018-12-24 11:39:24,278 DEBUG [NetMessageDispatch] - drfUtils:isSftpLocationAccessible: Closing SFTP Client...

### Start a Manual Backup via GUI Procedure

Step 1. Navigate to CUCM > Disaster Recovery System > Backup > Manual Backup as shown in the images :

Step 2. Select the Backup Device, the features to be backed up and click Start . For this example, only the UCM feature is backed up as shown in the image:

- When the backup is in progress, you see a status indication as shown in the image:

- When the backup is complete, you see a SUCCESS message that indicates the Backup Completed in CUCM as shown in the image:

- When the backup is complete, you see the .TAR files in the SFTP directory as shown in the image. These files are used later one, if a restore is required:

### Start a Manual Backup via CLI Procedure

Step 1. Secure Shell (SSH) into the IP address of the CUCM Publisher and authenticate with the OS username and password as shown in the image:

Step 2. Start a Manual backup with the command syntax: utils disaster_recovery backup network <featurelist> <backup device name> as shown in the image:

- When the backup is in progress, you see a status indication with the command syntax: utils disaster_recovery status backup as shown in the image:

- When the backup is complete, you see a success message with the command syntax: utils disaster_recovery status backup as shown in the image:

### Enable Scheduled Backup via GUI Procedure

Step 1. Navigate to CUCM > Disaster Recovery System > Backup > Scheduler >> Add New as shown in the images :

Step 2. Add a name for the automatic backup task as shown in the image:

Step 3 . Select a backup device

Step 4 . Select the features to be backed up

Step 5. Choose a start date and choose the frequency :

Step 6. Save

Step 7. Enable the scheduled backup:

### Enable Scheduled Backup via CLI Procedure

Step 1. Secure Shell (SSH) into the IP address of the CUCM Publisher and authenticate with the OS username and password as shown in the image:

Step 2. Add the scheduled backup with the command syntax: utils disaster_recovery schedule add < schedulename> < devicename> < featurelist> < datetime> < frequency> as shown in the image:

Step 3. Enable the scheduled backup with the command syntax: utils disaster_recovery schedule enable < schedulename > as shown in the image:

### CUCM Delete an Old Backup Example

Backup device configuration with Number of Backups set to 1 as shown in the image:

Backup directory with only 1 backup available (16 files) as shown in the image:

CUCM first starts to transfer backup files before it deletes the old backup (Reaches 32 files):

Once the backup is complete, DRS deletes the old backup to be in compliance with the number of backups to store in Network Directory (16 files):

#### Log Analysis of Successful New Backup Created and Old Backup Deleted

++++++++++++ The message you see when a manual backup is started: BEGIN MANUAL ++++++++++++

2018-12-25 11:11:59,486 DEBUG [NetMessageDispatch] - drfMessageValidator.validateMessage(): Starting introspection for Message ID = 1700 Message Body = ========== BEGIN msgSubBackup_REQ ========== m_bLeaveTempBackupDirectoryInPlace     : false destinationId     : TAC-Backup backupType : MANUAL featuresTobeBackedup : [UCM] ========== END msgSubBackup_REQ ==========

++++++++++++++++ This is the device that was added as a backup device: TAC-Backup ++++++++++++++++

2018-12-25 11:11:59,486 DEBUG [NetMessageDispatch] - drfMessageHandler:HandleBackup: The backup is being processed for the device: TAC-Backup

++++++++++++++++++++++ Ensure SFTP is accessible ++++++++++++++++++++++

2018-12-25 11:11:59,487 DEBUG [NetMessageDispatch] - drfMessageHandler:HandleBackup: Executing sftpLsFiles to make sure SFTP is accessible. 2018-12-25 11:11:59,487 INFO [NetMessageDispatch] - drfUtils:sftpLsFiles-: Executing JSCH SFTP ls command for: User: ciscoHostName: 192.X.X.250 from source :/UCM/Backups/ with pattern  -l 2018-12-25 11:11:59,487 DEBUG [NetMessageDispatch] - drfUtils:establishSftpConnection: Trying to connect to the SFTP server.

+++++++++++++++++++++++++++++++++ CUCM connects to remote SFTP server +++++++++++++++++++++++++++++++++

2018-12-25 11:11:59,617 DEBUG [NetMessageDispatch] - drfUtils:establishSftpConnection: Authentication Completed Successfully, connected to remote server. Now opening a SFTP channel.

+++++++++++++++++++++ Number of features that were selected: Found 1 features selected Feature Name: UCM +++++++++++++++++++++

2018-12-25 11:11:59,834 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Found 1 features selected for Restore 2018-12-25 11:11:59,834 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: CDPAGTDirectBackup set to : yes 2018-12-25 11:11:59,834 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: SYSLOGAGTDirectBackup set to : yes 2018-12-25 11:11:59,834 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: PLATFORMDirectBackup set to : yes 2018-12-25 11:11:59,834 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: CLMDirectBackup set to : yes 2018-12-25 11:11:59,834 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: CCMDBDirectBackup set to : yes 2018-12-25 11:11:59,834 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: TCTDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: CCMPREFSDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: TFTPDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: MOHDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: ANNDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: BATDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: CEFDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: REPORTERDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: DNALIASLOOKUPDirectBackup set to : yes 2018-12-25 11:11:59,835 DEBUG [NetMessageDispatch] - drfMessageHandler:setComponentBackupType: Feature Name: UCM. Server Name: D3-SB-11PUB. Component Name: DNALIASSYNCDirectBackup set to : yes

++++++++++++++++++++++++ 33 files found at the given path ++++++++++++++++++++++++

2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 33 files found at the given path 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_PLATFORM.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_drfComponent.xml 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_REPORTER.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CLM.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_DNALIASSYNC.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_REPORTER.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_MOH.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_BAT.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_CCMDB.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_SYSLOGAGT.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CEF.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CCMPREFS.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_CCMPREFS.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_TCT.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_CEF.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_PLATFORM.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CDPAGT.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_ANN.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_SYSLOGAGT.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_TFTP.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_TFTP.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CCMDB.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_ANN.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_DNALIASSYNC.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_DNALIASLOOKUP.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_CDPAGT.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_MOH.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_CLM.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_DNALIASLOOKUP.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_BAT.tar 2018-12-25 11:16:23,886 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-24-13-21-17_D3-SB-11PUB_UCM_TCT.tar

+++++++++++++++++++++++++++++++++ This is used to keep track of number of backups: DRS gets a list of its previous backup IDs: 2018-12-24-13-21-17 2018-12-25-11-12-03 +++++++++++++++++++++++++++++++++

2018-12-25 11:16:23,887 INFO [TarWorkerThread] - drfSftpManager:drfGetListOfBackups: Adding the backup id after the _pubhostname filtering:2018-12-24-13-21-17 2018-12-25 11:16:23,887 INFO [TarWorkerThread] - drfSftpManager:drfGetListOfBackups: Adding the backup id after the _pubhostname filtering:2018-12-25-11-12-03

+++++++++++++ list size : 1 +++++++++++++

2018-12-25 11:16:24,852 INFO [TarWorkerThread] - drfSftpManager.RemoveOldBackupSet: list size : 1

+++++++++++++++++++++++++++++++++++++++++++++++++++++++ CUCM removes: /UCM/Backups/2018-12-24-13-21-17_D3-SB-11PUB* +++++++++++++++++++++++++++++++++++++++++++++++++++++++

2018-12-25 11:16:24,852 INFO [TarWorkerThread] - drfSftpManager.RemoveOldBackupSet: Removing: /UCM/Backups/2018-12-24-13-21-17_D3-SB-11PUB*

+++++++++++++++++++++ List now only has 1 backup +++++++++++++++++++++

2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 18 files found at the given path 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_REPORTER.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CLM.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_MOH.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_BAT.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CEF.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CCMPREFS.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_TCT.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_PLATFORM.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CDPAGT.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_ANN.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_SYSLOGAGT.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_TFTP.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_CCMDB.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_DNALIASSYNC.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_UCM_DNALIASLOOKUP.tar 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: 2018-12-25-11-12-03_D3-SB-11PUB_drfComponent.xml 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfutils.sftpLsFiles-: Found 16 matching the search criteria.

++++++++++++++++++++++ CUCM closes ChannelSftp... ++++++++++++++++++++++

2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfUtils:closeSFTPConnections: Closing ChannelSftp... 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfUtils:closeSFTPConnections: Disconnecting Channel... 2018-12-25 11:16:26,405 DEBUG [TarWorkerThread] - drfUtils:closeSFTPConnections: Closing Session...

++++++++++++++++++++++++++ BACKUP operation COMPLETED ++++++++++++++++++++++++++

2018-12-25 11:16:26,572 INFO [TarWorkerThread] - {STATE_IDLE} drfBackup:CompleteBackup(Device=-): === BACKUP operation COMPLETED ===

## Verify

In order to verify that the backup was successful, you need to see the status message SUCCESS: Backup completed as shown in the image:

## Troubleshoot

In order to troubleshoot Backups in CUCM, you need:

- DRF Local logs

- DRF Master logs

In RTMT, navigate to Trace and Log Central > Collect Files > Cisco DRF Local & Cisco DRF Master for all servers as shown in the image:

You can find details in How to Collect Traces for CUCM 9.x or Later

Access to the remote SFTP is recommended.