---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1su3-english-administration-guide-cer0-b-cisco-emergency-responder--3dad3d0323
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1su3/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251su3/cer0_b_cisco-emergency-responder-administration-guide-1251su3_appendix_010011.html
retrieved_at: 2026-08-21T15:45:36.852851+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU3

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU3

Updated: November 23, 2021

Chapter: Disaster Recovery System Web Interface

## Chapter: Disaster Recovery System Web Interface

# Disaster Recovery System Web Interface

## Backup Device
                        	 List

The Backup
                              		  Device List page appears when you choose Backup > Backup
                                 			 Device .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Backup Device List page to list, add, and delete backup devices.

The
                              		  following table describes the Backup Device List page.

Field

Description

Lists the configured backup devices and displays the Device
                                          					 Name, Device Type, and Device Path. Click on the Device Name link to bring up
                                          					 the Backup Device page for that device.

Add
                                          					 New button

Adds a new backup device. When you click the Add icon, the
                                          					 Backup Device page appears. See Table 2 for information about the Backup
                                          					 Device page.

Select All button and icon

Selects all the listed backup devices.

Clear All button and icon

Deselects all selected backup devices.

Delete Selected button and icon

Deletes the selected backup devices.

The
                              		  following table describes the Backup Device page, which you use to add new
                              		  backup devices.

Field

Description

Enter the device name in the text box (required).

To
                                          					 select the backup destination, click the Tape
                                             						Device or Network
                                             						Directory radio button (required).

Tape Device

Select the name of the tape device from the pull-down menu.

Network Directory

In
                                          					 the fields provided, enter the Server name, Path name, User name, and Password
                                          					 for the Network Directory.

Number of backups to store on the Network Directory

Select the number of backups using the pull-down menu.

Save button and icon

Saves the information about the new backup device.

Back button and icon

Returns to the Backup Device List page.

## Schedule
                        	 List

The
                              		  Schedule List page appears when you choose Backup >
                                 			 Scheduler .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Schedule List page to list currently scheduled backups, to add new schedules,
                              		  to enable schedules, and to disable schedules. You can schedule a backup to
                              		  start at a specified date and time and configure it either to run once or at a
                              		  specified frequency, as well as specifying the features to be backed up.

The
                              		  following table describes the Schedule List page.

Field

Description

Lists all scheduled backups. Displays the Schedule List name,
                                          					 the Device Path, and the Schedule Status. Click the Schedule List name link to
                                          					 view the details of that schedule.

After you
                                                      						have created a scheduled backup, you must enable the schedule. To do so, select
                                                      						the schedule in the Schedule List and click the Enable
                                                         						  Selected Schedules button or icon.

Add
                                          					 New button or icon

Adds a new schedule. When you click the Add button or icon, the
                                          					 Scheduler page appears. See Table 2 for information about the Scheduler
                                          					 page.

Select All button or icon

Selects all the listed schedules.

The Select
                                                      						All button only appears if no schedules have been configured.

Clear All button or icon

Deselects all selected schedules.

The Clear
                                                      						All button only appears if no schedules have been configured.

Delete Selected button or icon

Deletes the selected schedules.

The Delete
                                                      						Selected button only appears if no schedules have been configured.

Enable Selected Schedules button or icon

Enables the selected schedules.

The Enable
                                                      						Selected Schedules icon only appears if no schedules have been configured.

Disable Selected Schedules button or icon

Disables the selected schedules.

The
                                                      						Disable Selected Schedules button only appears if no schedules have been
                                                      						configured.

The
                              		  following table describes the Scheduler page.

Field

Description

Displays the status of the Scheduler page.

Enter the name of the schedule in the text box.

Select the name of the backup device from the pull-down menu.

Select Emergency Responder as the feature to be backed up.

Date

From the pull-down menus, enter the year, month, and day on
                                          					 which the backup starts.

Time

From the pull-down menus, enter the hour and minute at which the
                                          					 backup starts.

Once

Click this radio button to schedule a single backup.

Daily

Click this radio button to schedule a daily backup.

Weekly

Click this radio button to schedule a weekly backup. Check the
                                          					 check boxes to specify the days on which the weekly backup is scheduled.

Monthly

Click this radio button to schedule a monthly backup.

Save button or icon

Saves the backup schedule information.

Set Default button or icon

Saves the information entered as the default for scheduled
                                          					 backups.

Disable Schedule button or icon

Disables the Schedule. If the Schedule is currently disabled,
                                          					 this button is grayed out.

Enable Schedule button or icon

Enables the Schedule. If the Schedule is currently enabled, this
                                          					 button is grayed out.

Back button or icon

Returns to the Scheduler List page.

## Manual
                        	 Backup

The Manual
                              		  Backup page appears when you choose Backup > Manual
                                 			 Backup .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Manual Backup page to start a manual backup.

The
                              		  following table describes the Manual Backup page.

Field

Description

Select the name of the backup device from the pulldown menu.

Check Emergency
                                             						Responder as the feature to be backed up.

Start Backup button or icon

Starts a manual backup.

Estimate
                                          					 Size button or icon

Estimates
                                          					 the backup size for the selected feature

Select All button or icon

Selects all the listed features.

Clear All button or icon

Deselects all selected features.

## Backup History and
                        	 Restore History

The Backup
                              		  History page appears when you choose Backup >
                                 			 History . The Restore History page appears when you choose Restore >
                                 			 History .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Backup History page to view information about past backups. Use the Restore
                              		  History page to view information about past restore operations.

The
                              		  following table describes the Backup History page.

Field

Description

Backup History information

The following information about past backups is displayed:

Tar Filename

Backup Device

Completed On

Result

Backup Type

Version

Features Backed Up

Features Returned Warning

Failed Features

Refresh button or icon

Refreshes the information in the Backup History page.

The
                              		  following table describes the Restore History page.

Field

Description

Restore History information

The following information about past backups is displayed:

Tar Filename

Backup Device

Version

Completed On

Result

Features Restored

Failed Features

Refresh button or icon

Refreshes the information in the Restore History page.

## Backup
                        	 Status

The Backup
                              		  Status page appears when you choose Backup >
                                 			 Current Status .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Backup Status page to view status information about the current backup.

The
                              		  following table describes the Backup Status page.

Field

Description

Provides information about the status of the current backup.

Backup Details

The following information about the current backup is displayed:

- Tar Filename

- Backup Device

- Operation

- Percentage Complete

- Feature

- Server

- Component

- Status

- Result

- Start Time

- Log File

Refresh button or icon

Refreshes the information about the current backup.

Cancel Backup button or icon

Cancels the current backup.

## Restore
                        	 Wizard

The
                              		  Restore Wizard page appears when you choose Restore >
                                 			 Restore Wizard .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Restore Wizard page to restore a backup file to a server or to restore all
                              		  servers in a cluster. The Restore Wizard consists of four web pages.

Use the
                              		  Step1 Restore—Choose Backup Device page to select the backup device to be used
                              		  for the backup.

The following table describes the Step1
                              		  Restore—Choose Backup Device page.

Field

Description

Status

Indicates the current status of the recovery operation.

Select the backup device using the pull-down menu.

Next button or icon

Advances to the next page in the Restore Wizard.

Cancel button or icon

Cancels the restore operation.

Use the
                              		  Step2 Restore—Choose the Backup Tar File page to select the backup tar file to be restored.

The
                              		  following table describes the Step2 Restore—Choose the Backup Tar File page.

Field

Description

Indicates the current status of the restore operation.

Select Backup File

Use the pull-down menu to select the tar file for backup

Back button or icon

Returns to the previous page in the Restore Wizard.

Next button or icon

Advances to the next page in the Restore Wizard.

Cancel button or icon

Cancels the restore operation.

Use the
                              		  Step3 Restore—Select the Type of Restore page to select the features to be restored.

The
                              		  following table describes the Step3 Restore—Select the Type of Restore page.

Field

Description

Indicates the current status of the restore operation.

Click the box to the left of the Emergency Responder feature
                                          					 name to select the Emergency Responder feature for backup.

Back button or icon

Returns to the previous page in the Restore Wizard.

Next button or icon

Advances to the next page in the Restore Wizard.

Cancel button or icon

Cancels the restore operation.

Use the
                              		  Step4 Restore—Final Warning for Restore page to select the servers to be restored.

The
                              		  following table describes the Step4 Restore—Final Warning for Restore page.

Field

Description

Indicates the current status of the restore operation.

Displays a warning message stating that the restore operation
                                          					 overwrites all existing data on the selected servers.

Under the Emergency Responder feature name, select the servers
                                          					 to be restored. To do so, click the check box to the left of the server name.

Back button or icon

Returns to the previous page in the Restore Wizard.

Restore button or icon

Initiates the restore operation. Before you click Restore , you must first select the server to be restored.
                                          					 You can select a Publisher or a Subscriber to be restored, but not both.

Caution

The
                                                      						restore operation overwrites any existing data on the selected servers.

Cancel button or icon

Cancels the restore operation.

## Restore
                        	 Status

The
                              		  Restore Status page appears when you choose Restore >
                                 			 Status .

### Authorization
                              		  Requirements

You must
                              		  have platform administrator authority to access this page.

### Description

Use the
                              		  Restore Status page to view the status of restore operations.

The
                              		  following table describes the Restore Status page.

Field

Description

Provides information about the status of the current restore
                                          					 operation.

The following information about the current restore operation is
                                          					 displayed:

- Tar Filename

- Backup Device

- Operation

- Percentage Complete

- Feature

- Server

- Component

- Status

- Result

- Start Time

- Log File

Refresh button or icon

Refreshes the information about the current restore operation.

| Field | Description |
|---|---|
| Backup Device List | Lists the configured backup devices and displays the Device
                                          					 Name, Device Type, and Device Path. Click on the Device Name link to bring up
                                          					 the Backup Device page for that device. |
| Add
                                          					 New button | Adds a new backup device. When you click the Add icon, the
                                          					 Backup Device page appears. See Table 2 for information about the Backup
                                          					 Device page. |
| Select All button and icon | Selects all the listed backup devices. |
| Clear All button and icon | Deselects all selected backup devices. |
| Delete Selected button and icon | Deletes the selected backup devices. |

| Field | Description |
|---|---|
| Backup device name | Enter the device name in the text box (required). |
| Select Destination | To
                                          					 select the backup destination, click the Tape
                                             						Device or Network
                                             						Directory radio button (required). |
| Tape Device | Select the name of the tape device from the pull-down menu. |
| Network Directory | In
                                          					 the fields provided, enter the Server name, Path name, User name, and Password
                                          					 for the Network Directory. |
| Number of backups to store on the Network Directory | Select the number of backups using the pull-down menu. |
| Save button and icon | Saves the information about the new backup device. |
| Back button and icon | Returns to the Backup Device List page. |

| Field | Description |
|---|---|
| Schedule List | Lists all scheduled backups. Displays the Schedule List name,
                                          					 the Device Path, and the Schedule Status. Click the Schedule List name link to
                                          					 view the details of that schedule. Note After you
                                                      						have created a scheduled backup, you must enable the schedule. To do so, select
                                                      						the schedule in the Schedule List and click the Enable
                                                         						  Selected Schedules button or icon. | Note | After you
                                                      						have created a scheduled backup, you must enable the schedule. To do so, select
                                                      						the schedule in the Schedule List and click the Enable
                                                         						  Selected Schedules button or icon. |
| Note | After you
                                                      						have created a scheduled backup, you must enable the schedule. To do so, select
                                                      						the schedule in the Schedule List and click the Enable
                                                         						  Selected Schedules button or icon. |
| Add
                                          					 New button or icon | Adds a new schedule. When you click the Add button or icon, the
                                          					 Scheduler page appears. See Table 2 for information about the Scheduler
                                          					 page. |
| Select All button or icon | Selects all the listed schedules. Note The Select
                                                      						All button only appears if no schedules have been configured. | Note | The Select
                                                      						All button only appears if no schedules have been configured. |
| Note | The Select
                                                      						All button only appears if no schedules have been configured. |
| Clear All button or icon | Deselects all selected schedules. Note The Clear
                                                      						All button only appears if no schedules have been configured. | Note | The Clear
                                                      						All button only appears if no schedules have been configured. |
| Note | The Clear
                                                      						All button only appears if no schedules have been configured. |
| Delete Selected button or icon | Deletes the selected schedules. Note The Delete
                                                      						Selected button only appears if no schedules have been configured. | Note | The Delete
                                                      						Selected button only appears if no schedules have been configured. |
| Note | The Delete
                                                      						Selected button only appears if no schedules have been configured. |
| Enable Selected Schedules button or icon | Enables the selected schedules. Note The Enable
                                                      						Selected Schedules icon only appears if no schedules have been configured. | Note | The Enable
                                                      						Selected Schedules icon only appears if no schedules have been configured. |
| Note | The Enable
                                                      						Selected Schedules icon only appears if no schedules have been configured. |
| Disable Selected Schedules button or icon | Disables the selected schedules. Note The
                                                      						Disable Selected Schedules button only appears if no schedules have been
                                                      						configured. | Note | The
                                                      						Disable Selected Schedules button only appears if no schedules have been
                                                      						configured. |
| Note | The
                                                      						Disable Selected Schedules button only appears if no schedules have been
                                                      						configured. |

| Note | After you
                                                      						have created a scheduled backup, you must enable the schedule. To do so, select
                                                      						the schedule in the Schedule List and click the Enable
                                                         						  Selected Schedules button or icon. |
|---|---|

| Note | The Select
                                                      						All button only appears if no schedules have been configured. |
|---|---|

| Note | The Clear
                                                      						All button only appears if no schedules have been configured. |
|---|---|

| Note | The Delete
                                                      						Selected button only appears if no schedules have been configured. |
|---|---|

| Note | The Enable
                                                      						Selected Schedules icon only appears if no schedules have been configured. |
|---|---|

| Note | The
                                                      						Disable Selected Schedules button only appears if no schedules have been
                                                      						configured. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the status of the Scheduler page. |
| Schedule Name | Enter the name of the schedule in the text box. |
| Select Backup Device | Select the name of the backup device from the pull-down menu. |
| Select Features | Select Emergency Responder as the feature to be backed up. |
| Start Backup at |  |
| Date | From the pull-down menus, enter the year, month, and day on
                                          					 which the backup starts. |
| Time | From the pull-down menus, enter the hour and minute at which the
                                          					 backup starts. |
| Frequency |  |
| Once | Click this radio button to schedule a single backup. |
| Daily | Click this radio button to schedule a daily backup. |
| Weekly | Click this radio button to schedule a weekly backup. Check the
                                          					 check boxes to specify the days on which the weekly backup is scheduled. |
| Monthly | Click this radio button to schedule a monthly backup. |
| Save button or icon | Saves the backup schedule information. |
| Set Default button or icon | Saves the information entered as the default for scheduled
                                          					 backups. |
| Disable Schedule button or icon | Disables the Schedule. If the Schedule is currently disabled,
                                          					 this button is grayed out. |
| Enable Schedule button or icon | Enables the Schedule. If the Schedule is currently enabled, this
                                          					 button is grayed out. |
| Back button or icon | Returns to the Scheduler List page. |

| Note | Before starting a manual backup, make sure that all servers in the clusters are running and are reachable over the network.
                                       Servers that are not running or are not reachable over the network are not backed up. |
|---|---|

| Note | From Release 14SU2 onwards, tomcat and tomcat-ecdsa certificate must be exchanged between the publisher and subscriber nodes
                                       before taking drs backup. Certificate exchange is also required if the ipaddress/hostname changes. |
|---|---|

| Field | Description |
|---|---|
| Select Backup Device | Select the name of the backup device from the pulldown menu. |
| Select Features | Check Emergency
                                             						Responder as the feature to be backed up. |
| Start Backup button or icon | Starts a manual backup. |
| Estimate
                                          					 Size button or icon | Estimates
                                          					 the backup size for the selected feature |
| Select All button or icon | Selects all the listed features. |
| Clear All button or icon | Deselects all selected features. |

| Field | Description |
|---|---|
| Backup History information | The following information about past backups is displayed: Tar Filename Backup Device Completed On Result Backup Type Version Features Backed Up Features Returned Warning Failed Features |
| Refresh button or icon | Refreshes the information in the Backup History page. |

| Field | Description |
|---|---|
| Restore History information | The following information about past backups is displayed: Tar Filename Backup Device Version Completed On Result Features Restored Failed Features |
| Refresh button or icon | Refreshes the information in the Restore History page. |

| Field | Description |
|---|---|
| Status | Provides information about the status of the current backup. |
| Backup Details | The following information about the current backup is displayed: Tar Filename Backup Device Operation Percentage Complete Feature Server Component Status Result Start Time Log File |
| Refresh button or icon | Refreshes the information about the current backup. |
| Cancel Backup button or icon | Cancels the current backup. |

| Field | Description |
|---|---|
| Status | Indicates the current status of the recovery operation. |
| Select Backup Device | Select the backup device using the pull-down menu. |
| Next button or icon | Advances to the next page in the Restore Wizard. |
| Cancel button or icon | Cancels the restore operation. |

| Field | Description |
|---|---|
| Status | Indicates the current status of the restore operation. |
| Select Backup File | Use the pull-down menu to select the tar file for backup |
| Back button or icon | Returns to the previous page in the Restore Wizard. |
| Next button or icon | Advances to the next page in the Restore Wizard. |
| Cancel button or icon | Cancels the restore operation. |

| Field | Description |
|---|---|
| Status | Indicates the current status of the restore operation. |
| Select Features | Click the box to the left of the Emergency Responder feature
                                          					 name to select the Emergency Responder feature for backup. |
| Back button or icon | Returns to the previous page in the Restore Wizard. |
| Next button or icon | Advances to the next page in the Restore Wizard. |
| Cancel button or icon | Cancels the restore operation. |

| Field | Description |
|---|---|
| Status | Indicates the current status of the restore operation. |
| Warning | Displays a warning message stating that the restore operation
                                          					 overwrites all existing data on the selected servers. |
| Select the Servers to be restored for each Feature | Under the Emergency Responder feature name, select the servers
                                          					 to be restored. To do so, click the check box to the left of the server name. |
| Back button or icon | Returns to the previous page in the Restore Wizard. |
| Restore button or icon | Initiates the restore operation. Before you click Restore , you must first select the server to be restored.
                                          					 You can select a Publisher or a Subscriber to be restored, but not both. Caution The
                                                      						restore operation overwrites any existing data on the selected servers. | Caution | The
                                                      						restore operation overwrites any existing data on the selected servers. |
| Caution | The
                                                      						restore operation overwrites any existing data on the selected servers. |
| Cancel button or icon | Cancels the restore operation. |

| Caution | The
                                                      						restore operation overwrites any existing data on the selected servers. |
|---|---|

| Field | Description |
|---|---|
| Status | Provides information about the status of the current restore
                                          					 operation. |
| Restore Details | The following information about the current restore operation is
                                          					 displayed: Tar Filename Backup Device Operation Percentage Complete Feature Server Component Status Result Start Time Log File |
| Refresh button or icon | Refreshes the information about the current restore operation. |