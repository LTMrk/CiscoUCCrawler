---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--35229a59d3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_011111.html
retrieved_at: 2026-08-17T00:50:46.833644+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR System Database

## Chapter: CAR System Database

# CAR System Database

You can configure CAR to notify you when the CAR database size
                        		exceeds a percentage of the maximum number of records. You can set the message
                        		and the maximum number of records and specify the alert percentage.

You can configure the system to maintain the CAR database size
                        		between the low water mark and the high water mark values that you configure
                        		through the Configure Automatic Database Purge window. When the database size
                        		reaches the low water mark, CAR sends an alert to the user. When the database
                        		size reaches the high water mark, the system deletes records based on the
                        		deletion age and sends an e-mail.

To configure the CAR system database, go to Cisco Unified Serviceability > Tools > CDR Analysis and
                              			 Reporting > System or Report
                              			 Config .

## Purge CAR Database

This section describes how to manually purge selected records
                              		  from the CAR database and how to delete all of the CAR data and reload the
                              		  database with new CDR data. You may want to reload the database to reclassify
                              		  calls after dial-plan updates, user-device association changes, call rate
                              		  changes, and so on.

Before you begin to manually purge data, disable the CDR
                              		  Loader.

Choose System > Scheduler > CDR Load .

Chosse either of the following:

Disable Loader - check the Disable Loader check box and click the Update .

Enable CDR loading to load the data into CAR. Changes take effect at midnight. You can force the change to take effect immediately
                                          by stopping and restarting the CAR Scheduler service.

Enable Loader - uncheck the Disable Loader check box.

Manual purging of the CDRs gets stopped if the CAR Web
                              		  Service is stopped during the manual purge process. Manual purging cannot begin
                              		  again until the CAR Web Service restarts. Then you must begin the manual purge
                              		  process again.

There are two ways to intentionally stop the CAR Web Service:

Deactivate the CAR Web Service in the Serviceability Service Activation window ( Cisco Unified Serviceability > Service Activation ).

Stop the CAR Web Service in the Feature Services window of the Serviceability Control Center ( Cisco Unified Serviceability > Tools > Control Center - Feature Services ).

The CDR Loader cannot begin again until either the CAR Web
                              		  Service or the CAR Scheduler gets restarted.

A CAR administrator can no longer generate CAR reports when a
                              		  manual purge of the CAR database is in process or CDR records are reloading.
                              		  The following error message displays when you try to run reports during these
                              		  processes:

```
10023: Manual Purge/Reload is in process. Please run the reports once the Manual Purge/Reload is over.
```

Both the Purge button and the Reload All Call Detail Records button get
                              		  disabled, and the following alert message displays on the Manual Purge window,
                              		  when either a manual purge or CDR reload occurs:

```
Manual Purge/Reload is still running. User will not be allowed to run another instance of Manual Purge/Reload. So, both Purge and Reload All Call Detail Records buttons are disabled.
```

Choose System > Database > Manual Purge .

The Manual Database Purge window displays.

Choose one of the following actions:

To delete the existing CAR data and reload the CAR database,
                                             				  click the Reload All Call Detail Records button.

The system displays a message that indicates that deleting the
                                                					 records may impact system performance. To continue the reload process, click OK .

The system begins loading the CDRs into the CAR database
                                                					 within 5 minutes and continues uninterrupted for up to 6 hours. To monitor the
                                                					 progress of the reload, generate the CDR Load event log.

After the system loads the new records, the system loads the
                                                					 records according to the schedule that is configured. By default, CDR data
                                                					 loads 24 hours per day and 7 days per week.

To manually purge selected CAR records, continue with the next
                                             				  step.

In the Select Table field, choose the table in the database that you
                                       			 want purged.

To view the tables for which manual purge is permitted, the total
                                          				number of records in the table, and the latest record and oldest record in the
                                          				table, click the Table Information button.

The Table Information window displays. You will see a table with
                                          				the following information:

Database Name

Table Name

Total No. of Records

Latest Record

Oldest Record

CAR

Tbl_billing_data

0

0

0

CAR

Tbl_billing_error

0

0

0

CAR

Tbl_purge_history

0

0

0

To return to the Manual Database Purge window, click the Close button.

In the Delete records field, choose a date that will determine
                                       			 which records will be purged by clicking one of the following radio buttons:

Older than - Choose a date for which all records before that
                                             				  date will be deleted.

Between - Choose a range of dates between which all records
                                             				  will be deleted.

Choose the date range of the CAR records that you want to delete.

To delete all records older than or between the dates that you
                                       			 specified, click the Purge button.

A prompt advises you that you are about to permanently delete the
                                          				specified records.

To purge the records, click the OK button or click the Cancel button to abort the purge operation.

If you click OK , the records get purged from the selected
                                          				table. After successful deletion of records, the status message shows the
                                          				number of records that were deleted from the table.

## Set Up Automatic Database Purge

This section describes how to schedule and disable automatic
                              		  purging of the CAR database. By default, the system enables automatic database
                              		  purge.

Choose System > Database > Configure Automatic
                                             				  Purge .

The Configure Automatic Database Purge window displays. At the top
                                          				of the window, the percentage amount of the CAR database space that has been
                                          				used gets displayed. The maximum CAR Database space that is available gets
                                          				displayed in megabytes.

From the Low Water Mark drop-down list box, choose the minimum
                                       			 percentage of the maximum CAR database size that you want the system to use for
                                       			 CAR data. The default value specifies 80 percent.

The system notifies you when the CAR database size reaches the
                                                      				  low or the high water mark; it also notifies you when the CAR database size
                                                      				  exceeds the maximum number of records. For information on configuring an e-mail
                                                      				  alert.

From the High Water Mark drop-down list box, choose the maximum
                                       			 percentage of the maximum CAR database size that you want the system to use for
                                       			 CAR data. The default value specifies 90 percent.

In the Max Age of Call Detail Records field, enter the maximum
                                       			 number of days that you want to keep the CDRs in the CAR database. Enter a
                                       			 number between 1 and 180. The default value specifies 60 days.

CAR deletes all CDRs that are older than the specified number of
                                          				days.

To restore the default values for the fields in this window,
                                                      				  click the Restore Defaults button.

Click the Update button.

The changes take effect at midnight. To make changes take effect
                                          				immediately, restart the Cisco CAR Scheduler service.

When the 2M or HWM limit is breached:

CAR deletes the database partitions one by one, starting from
                                                					 the oldest date partition.

CAR stops purging under one of the following conditions:

When the record count falls below the 2M or HWM limit.

When there is only last two days partitions left on the
                                                      						  billing tables.

In cases where there are large number of CDRs present in the
                                          				billing tables and deleting the partitions does not bring the record count
                                          				below the 2M or HWM limit, CAR holds at least two days data in the database.

When the record count in the database reaches the 2M or HWM limit:

CAR loader stops processing the new records.

CAR starts purging the records from the oldest partition till
                                                					 the record count reaches 2M or HWM limit.

If the record count does not fall below the 2M or HWM limit even
                                          				after deleting the records, CAR holds at least two days records and stops the
                                          				CAR loader. Also, CAR sends an e-mail notification to CAR administrator to
                                          				proceed with manual purge.

Following an upgrade, the Configure Automatic Database Purge > MAX DATABASE AGE parameter will be changed to one of the following:

If the MAX DATABASE AGE in the old version is between 1
                                                and 60, it will be configured to 60 in the new version.

If the MAX DATABASE AGE in the old version is between
                                                60 and 180, it will be configured to the same age in the new
                                                version.

If the MAX DATABASE AGE in the old version is more than
                                                180, it will be configured to 180 in the new version.

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Step 1 | Choose System > Database > Manual Purge . The Manual Database Purge window displays. |
|---|---|
| Step 2 | Choose one of the following actions: To delete the existing CAR data and reload the CAR database,
                                             				  click the Reload All Call Detail Records button. The system displays a message that indicates that deleting the
                                                					 records may impact system performance. To continue the reload process, click OK . The system begins loading the CDRs into the CAR database
                                                					 within 5 minutes and continues uninterrupted for up to 6 hours. To monitor the
                                                					 progress of the reload, generate the CDR Load event log. After the system loads the new records, the system loads the
                                                					 records according to the schedule that is configured. By default, CDR data
                                                					 loads 24 hours per day and 7 days per week. To manually purge selected CAR records, continue with the next
                                             				  step. |
| Step 3 | In the Select Table field, choose the table in the database that you
                                       			 want purged. To view the tables for which manual purge is permitted, the total
                                          				number of records in the table, and the latest record and oldest record in the
                                          				table, click the Table Information button. The Table Information window displays. You will see a table with
                                          				the following information: Database Name Table Name Total No. of Records Latest Record Oldest Record CAR Tbl_billing_data 0 0 0 CAR Tbl_billing_error 0 0 0 CAR Tbl_purge_history 0 0 0 To return to the Manual Database Purge window, click the Close button. | Database Name | Table Name | Total No. of Records | Latest Record | Oldest Record | CAR | Tbl_billing_data | 0 | 0 | 0 | CAR | Tbl_billing_error | 0 | 0 | 0 | CAR | Tbl_purge_history | 0 | 0 | 0 |
| Database Name | Table Name | Total No. of Records | Latest Record | Oldest Record |
| CAR | Tbl_billing_data | 0 | 0 | 0 |
| CAR | Tbl_billing_error | 0 | 0 | 0 |
| CAR | Tbl_purge_history | 0 | 0 | 0 |
| Step 4 | In the Delete records field, choose a date that will determine
                                       			 which records will be purged by clicking one of the following radio buttons: Older than - Choose a date for which all records before that
                                             				  date will be deleted. Between - Choose a range of dates between which all records
                                             				  will be deleted. |
| Step 5 | Choose the date range of the CAR records that you want to delete. |
| Step 6 | To delete all records older than or between the dates that you
                                       			 specified, click the Purge button. A prompt advises you that you are about to permanently delete the
                                          				specified records. |
| Step 7 | To purge the records, click the OK button or click the Cancel button to abort the purge operation. If you click OK , the records get purged from the selected
                                          				table. After successful deletion of records, the status message shows the
                                          				number of records that were deleted from the table. |

| Database Name | Table Name | Total No. of Records | Latest Record | Oldest Record |
|---|---|---|---|---|
| CAR | Tbl_billing_data | 0 | 0 | 0 |
| CAR | Tbl_billing_error | 0 | 0 | 0 |
| CAR | Tbl_purge_history | 0 | 0 | 0 |

| Step 1 | Choose System > Database > Configure Automatic
                                             				  Purge . The Configure Automatic Database Purge window displays. At the top
                                          				of the window, the percentage amount of the CAR database space that has been
                                          				used gets displayed. The maximum CAR Database space that is available gets
                                          				displayed in megabytes. |
|---|---|
| Step 2 | From the Low Water Mark drop-down list box, choose the minimum
                                       			 percentage of the maximum CAR database size that you want the system to use for
                                       			 CAR data. The default value specifies 80 percent. Tip The system notifies you when the CAR database size reaches the
                                                      				  low or the high water mark; it also notifies you when the CAR database size
                                                      				  exceeds the maximum number of records. For information on configuring an e-mail
                                                      				  alert. | Tip | The system notifies you when the CAR database size reaches the
                                                      				  low or the high water mark; it also notifies you when the CAR database size
                                                      				  exceeds the maximum number of records. For information on configuring an e-mail
                                                      				  alert. |
| Tip | The system notifies you when the CAR database size reaches the
                                                      				  low or the high water mark; it also notifies you when the CAR database size
                                                      				  exceeds the maximum number of records. For information on configuring an e-mail
                                                      				  alert. |
| Step 3 | From the High Water Mark drop-down list box, choose the maximum
                                       			 percentage of the maximum CAR database size that you want the system to use for
                                       			 CAR data. The default value specifies 90 percent. |
| Step 4 | In the Max Age of Call Detail Records field, enter the maximum
                                       			 number of days that you want to keep the CDRs in the CAR database. Enter a
                                       			 number between 1 and 180. The default value specifies 60 days. CAR deletes all CDRs that are older than the specified number of
                                          				days. Note To restore the default values for the fields in this window,
                                                      				  click the Restore Defaults button. | Note | To restore the default values for the fields in this window,
                                                      				  click the Restore Defaults button. |
| Note | To restore the default values for the fields in this window,
                                                      				  click the Restore Defaults button. |
| Step 5 | Click the Update button. The changes take effect at midnight. To make changes take effect
                                          				immediately, restart the Cisco CAR Scheduler service. Note When the 2M or HWM limit is breached: CAR deletes the database partitions one by one, starting from
                                                					 the oldest date partition. CAR stops purging under one of the following conditions: When the record count falls below the 2M or HWM limit. When there is only last two days partitions left on the
                                                      						  billing tables. In cases where there are large number of CDRs present in the
                                          				billing tables and deleting the partitions does not bring the record count
                                          				below the 2M or HWM limit, CAR holds at least two days data in the database. When the record count in the database reaches the 2M or HWM limit: CAR loader stops processing the new records. CAR starts purging the records from the oldest partition till
                                                					 the record count reaches 2M or HWM limit. If the record count does not fall below the 2M or HWM limit even
                                          				after deleting the records, CAR holds at least two days records and stops the
                                          				CAR loader. Also, CAR sends an e-mail notification to CAR administrator to
                                          				proceed with manual purge. Following an upgrade, the Configure Automatic Database Purge > MAX DATABASE AGE parameter will be changed to one of the following: If the MAX DATABASE AGE in the old version is between 1
                                                and 60, it will be configured to 60 in the new version. If the MAX DATABASE AGE in the old version is between
                                                60 and 180, it will be configured to the same age in the new
                                                version. If the MAX DATABASE AGE in the old version is more than
                                                180, it will be configured to 180 in the new version. | Note | When the 2M or HWM limit is breached: |
| Note | When the 2M or HWM limit is breached: |

| Tip | The system notifies you when the CAR database size reaches the
                                                      				  low or the high water mark; it also notifies you when the CAR database size
                                                      				  exceeds the maximum number of records. For information on configuring an e-mail
                                                      				  alert. |
|---|---|

| Note | To restore the default values for the fields in this window,
                                                      				  click the Restore Defaults button. |
|---|---|

| Note | When the 2M or HWM limit is breached: |
|---|---|