---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-core-config-bu-html-bf161726f2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/core_config_bu.html
retrieved_at: 2026-08-21T23:39:46.936921+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: Configuring Backup and Restore

## Chapter: Configuring Backup and Restore

## Configuring the Backup Server

Before you begin the backup process, set the backup configuration parameters.

Step 1 Select Administration > Backup / Restore > Configuration .

The system displays the Backup / Restore Configuration page.

Step 2 Enter the information shown in the following fields:

- Server URL—The URL of the server on the network where the backup files are stored. The format should be ftp://<server/directory>/ where < server/directory> is the IP address or hostname of the server.

- User ID—The account name or user ID on the backup server. You must have an account on the system to which you are backing up your data. Do not use an anonymous user ID.

- Password—The password for the account name or user ID on the backup server.

- Maximum revisions—The maximum number of revisions of the backup data to keep on the server. The maximum number is 50. The default value is 5.

Step 3 Click Apply to save the information.

## Manually Starting a Backup

Before You Begin

- Configure the server used to back up the data. See Configuring the Backup Server .

- Save your Cisco Unified SRST Manager configuration. See Saving and Reloading the Cisco Unified SRST Manager Configuration .

Step 1 Select Administration > Backup / Restore > Start Backup .

The system displays the Backup / Restore Start Backup page and automatically generates a backup ID. The backup ID increases by 1 every time you back up the server.

Step 2 Enter a description of the backup file; for example, “backupdata2012-10-01.”

Step 3 Select the check box for the types of data that you want to save. You can choose one or both:

- Configuration—Saves the system and application settings.

- Data—Saves the application data.

Step 4 Click Start Backup .

Step 5 Click OK at the confirmation message.

## Viewing and Removing Scheduled Backups

Step 1 Select Administration > Backup / Restore > Scheduled Backups .

If one or more backups have been scheduled, the system displays the Backup / Restore Scheduled Backups page with the following information:

- Name

- Description

- Schedule

- Next Run

- Categories of backup (type of data to save)

Step 2 To sort scheduled backups, click any of the headers.

Step 3 To modify an existing scheduled backup, click the underlined schedule name, edit the parameters, and click Apply .

Step 4 To add a new scheduled backup, click Schedule Backup . See Adding a Scheduled Backup .

Step 5 To disable all existing scheduled backups, which means that the system ignores all scheduled backups and does not collect any backup data, click Bulk Disable . See Disabling Scheduled Backups .

Note Disabling scheduled backups allows you to temporarily turn off backups without deleting the backup schedule.

Step 6 To remove a scheduled backup, do the following:

a. Select the check box next to the name of the backup.

b. Click Delete .

c. Click OK at the confirmation message.

## Adding a Scheduled Backup

You can configure scheduled backups to occur once or recurring jobs that repeat:

- Every n days at a specific time

- Every n weeks on specific day and time

- Every n months on a specific day of the month and time

- Every n years on specific day and time

Before You Begin

You must do the following before starting a backup:

- Configure the server used to back up the data. See Configuring the Backup Server .

- Save the Cisco Unified SRST Manager configuration. See Saving and Reloading the Cisco Unified SRST Manager Configuration .

Step 1 Select Administration > Backup / Restore > Scheduled Backups .

The system displays the Backup / Restore Scheduled Backups page.

Step 2 Click Schedule Backup .

The system displays the Backup / Restore Scheduled Backups page.

Step 3 Enter a name for the scheduled backup.

Step 4 Enter a description of the scheduled backup—for example, “backupdata2012-09-01.”

Step 5 Select the check box for the type of data that you want to save. You can select one or both:

- Configuration—Saves the configurations of the system and applications.

- Data—Saves your application data messages.

Step 6 Select whether the scheduled backup will occur:

- Once

- Daily

- Weekly

- Monthly

- Yearly

Step 7 Select whether the scheduled backup will start:

- Immediately

- On a specific date and time. If you choose this option, enter the date and time.

Step 8 Optionally, you can select the Disabled check box to disable the backup. The backup remains configured, but is not active. See Disabling Scheduled Backups .

Step 9 Click Add .

Step 10 If you choose Immediately, the system displays a message stating that running a backup will put the system in offline mode and disable management interfaces. Click OK to continue.

## Disabling Scheduled Backups

Step 1 Select Administration > Backup/Restore > Scheduled Backups .

The system displays the Backup / Restore Scheduled Backups page listing all the backups that are scheduled.

Step 2 To disable a single scheduled backup, do the following:

a. Click the underlined name of the scheduled backup. The system displays the Scheduled Backups page with information about this scheduled backup.

b. Select the Disabled check box.

c. Click Apply.

Step 3 To disable all scheduled backups, do the following:

a. Click Bulk Disable . The system displays the Scheduled Backups page with disabling information.

b. Select Disabled Range and enter a date range for when the scheduled backups will be disabled.

c. Click Apply.

## Starting a Restore

After you have backed up your configuration and data, you can restore it for a new installation or upgrade.

Restriction

After you perform a restore, you cannot run the Setup Wizard.

Before You Begin

Configure a backup server. See Configuring the Backup Server .

Step 1 Select Administration > Backup / Restore > Start Restore .

The system displays the Backup / Restore Start Restore page with the following fields:

- Backup ID—The backup ID of previous backups.

- Version—Version

- Description—Name of this backup.

- Backup Time and Date—Date and time when this backup was made.

- Categories—The type of data that you want to restore.

Step 2 Select the row containing the configuration that you want to restore.

Step 3 Select the check box for the type of data that you want to save. You can choose one or both:

- Configuration—Saves the configurations of the system and applications.

- Data—Saves your application data.

Step 4 Click Start Restore .

Step 5 After restoring the backup, you might need to console into Cisco Unified SRST Manager from the vSphere client/vCenter application, and re-configure the network credentials (interface Ethernet 0, and IP default gateway) before the system is ready for use.

Note In some cases, the backup includes the configuration of network credentials and no further configuration of network credentials is necessary after restoring the backup. If the backup does not include the network credentials, or if it has incorrect credentials, you will not be able to reach the Cisco Unified SRST Manager GUI remotely. You can access Cisco Unified SRST Manager using the VMware manager console.