---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--9fb6221df3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_011110.html
retrieved_at: 2026-08-21T01:37:28.563822+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR System Scheduler

## Chapter: CAR System Scheduler

# CAR System Scheduler

The CAR System Scheduler allows you to configure the CDR load
                        		schedule and schedule daily, weekly, and monthly reports.

## Set Up CDR Load Schedule

By default, CDR data loads continuously 24 hours a day, 7
                              		  days a week, and loads only CDR records.

The default batch size equals 600 CDR or CMR records. The default
                                          			 sleep time between each CDR batch equals 2500 ms and 3000 ms for each CMR
                                          			 batch. You can, however, configure the batch size from the
                                          			 tbl_system_preferences table "LOADER_BATCH" column to have any value between 50 and 2000.

This section describes how to customize the loading schedule,
                              		  how to restore the default loading schedule if it is customized, and how to
                              		  disable CDR loading.

Disable CDR loading when you are installing or upgrading the system. Of course, the CDR data does not get updated when CDR
                              loading is disabled. Be sure to enable CDR loading again as soon as possible. The CAR tool does not affect the CDR generation
                              in Unified Communications Manager .

To manually delete the CAR data and reload the database with CDRs.

Choose System > Scheduler > CDR
                                             				  Load .

The CDR Load window displays.

Choose one of the following options:

Disable Loader - To disable CDR data loading, check the Disable Loader check box and click the Update button.

CDR data will not load into CAR until you enable CDR loading.
                                                					 Changes take effect at midnight. You can force the change to take effect
                                                					 immediately by stopping and restarting the CAR Scheduler service.

To enable CDR data loading, uncheck the Disable Loader check box and continue
                                                					 with the next step to configure the load parameters.

Continuous Loading 24/7 - To enable the CDR Loader to run
                                             				  continuously 24 hours a day, 7 days a week to load CDRs into the CAR database,
                                             				  check the Continuous Loading 24/7 check box and
                                             				  click the Update button. This choice represents the
                                             				  default setting for the CDR Load Scheduler.

Under the default setting, only CDR records continuously
                                                            						load. The CMR records do not load. You must manually uncheck the Load CDR only check box to force the
                                                            						CMR records to continuously load with the CDR records.

The CAR Scheduler service stops, and the CAR Loader, as
                                                					 configured, runs immediately (within 1 to 2 minutes). The CAR Scheduler service
                                                					 restarts. If no new files for processing exist, the CDR Loader sleeps and then
                                                					 checks periodically for new files to be loaded.

If this option is chosen, it takes precedence over and
                                                            						ignores the other CDR and CMR load parameters on the screen, such as Time,
                                                            						Loading Interval, Duration, and Uninhibited Loading.

Load CDR Only - To load only CDR records into the CAR
                                             				  database, check the Load CDR only check box and click the Update button. Continue to the next step
                                             				  to configure the load parameters. With this option, CMR records do not load
                                             				  into the CAR database. This choice represents the default setting for the CDR
                                             				  Load Scheduler.

In the Load CDR & CMR area, complete the fields as described
                                       			 in the following table.

Field

Value

Time

Choose the hour and minute that you want CAR to
                                                      						  begin loading CDR data from the CDR flat files.

Loading Interval

Choose the interval at which you want records
                                                      						  loaded. The interval can range from every 15 minutes to every 24 hours.

Duration

Enter the number of minutes that you want to
                                                      						  allow CDR data to load. Depending on the size of the CDR flat files, CAR
                                                      						  performance may degrade when CDRs load. You can limit the time that is allowed
                                                      						  for loading, but in doing so, the possibility exists that only a portion of the
                                                      						  CDR data will be loaded in the time that you set. Be sure to reconcile the
                                                      						  duration limit that you place with the interval. For example, if you load CDR
                                                      						  data every 15 minutes, the duration of loading cannot exceed 15 minutes.

Uninhibited loading allows you to set a time during which CDR data
                                          				will load continuously. CDR data does not load automatically in the duration that is specified. The CDR
                                          				data loads uninhibited in the specified duration only if loading starts at the
                                          				duration that is specified in the Load CDR and CMR area settings. If CDR data
                                          				loading starts at an uninhibited loading interval, loading continues to the end
                                          				of the uninhibited loading interval, plus the time in the duration field that
                                          				is set in the Load CDR and CMR area, or until no new files to process exist.

Uninhibited loading take precedence over any values that are set
                                          				for scheduled loading. If you do not want uninhibited loading of CDR data, set
                                          				the From and To values at 00:00.

In the Uninhibited Loading of CDR area, complete the fields as
                                       			 described in the following table:

Field

Value

From

Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to begin.

To

Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to end.

Click the Update button.

CAR will load CDR data based on the time, interval, and duration
                                          				that you have specified. Changes take effect at midnight. You can force the
                                          				change to take effect immediately by stopping and restarting the CAR Scheduler
                                          				service.

If Continuous Loading 24/7 is selected, the CAR Scheduler
                                                      				  service restarts automatically when the Update button is clicked. CAR will load
                                                      				  CDR data immediately (within 1 to 2 minutes).

## Schedule Daily Reports

The Daily Report Scheduler schedules the time and duration of
                              		  CAR daily reports.

### Before you begin

Specify the reports to be generated by using the Automatic
                              		  Generation/Alert Option.

This section describes how to schedule the time and duration
                              		  of the automatic daily reports.

Choose System > Scheduler > Daily .

The Daily Scheduler window displays.

From the Time drop-down list box, choose the hour and minute when
                                       			 you want daily reports to be generated.

A 24-hour clock represents time, where 0 equals midnight, and 1
                                          				through 11 represent a.m. hours, and 12 through 23 represent the p.m. hours of
                                          				1 p.m. through 11 p.m., respectively.

From the Life drop-down list box, choose the duration of the
                                       			 report from the range of 0 to 12 days.

If you set the life of the report to 00, the report does not
                                                      				  generate.

Click the Update button.

Reports with report generation interval of Daily in the Automatic
                                          				Generation/Alert Option and enabled automatically generate every day at the
                                          				time that you specify and get deleted after the number of days that you
                                          				specify.

Changes take effect at midnight. You can force the change to take
                                          				effect immediately by stopping and restarting the CAR Scheduler service.

To restore the defaults, click the Restore Defaults button. By default, the
                                                      				  daily reports run at 1 a.m. every day and get purged after two days.

## Schedule Weekly Reports

The Weekly Report Scheduler schedules the day, time, and
                              		  duration of the automatic weekly reports.

### Before you begin

Use the Automatic Generation/Alert Option to specify the
                              		  reports to be generated.

This section describes how to schedule the day, time, and
                              		  duration of the automatic weekly reports.

Choose System > Scheduler > Weekly .

The Weekly Scheduler window displays.

From the Day of Week drop-down list box, choose the day that you
                                       			 want reports to be generated.

From the Time drop-down list box, choose the hour and minute when
                                       			 you want reports to be generated.

A 24-hour clock represents time, where 0 equals midnight, and 1
                                          				through 11 represent a.m. hours, and 12 through 23 represent the p.m. hours of
                                          				1 p.m. through 11 p.m., respectively.

From the Life drop-down list box, choose the duration of the
                                       			 report from the range of 00 to 12 weeks. The option that you choose indicates
                                       			 how many weeks the report remains on the disk before the report gets deleted.

If you set the life of the report to 00, the report does not
                                                      				  generate.

Click the Update button.

Reports with report generation interval of Weekly in the Automatic
                                          				Generation/Alert Option and enabled automatically generate every week at the
                                          				time that you specify and get deleted after the number of weeks that you
                                          				specify.

Changes take effect at midnight. For the changes to take effect
                                          				immediately, stop and restart the CAR Scheduler service in the Control Center -
                                          				Feature Services window.

To restore the defaults, click the Restore Defaults button. By default,
                                                      				  weekly reports run at 4 a.m. every Sunday and get purged after four weeks.

## Schedule Monthly Reports

The Monthly Report Scheduler schedules the day, time, and
                              		  duration of CAR monthly reports.

### Before you begin

Use the Automatic Generation/Alert Option to specify the
                              		  reports to be generated.

This section describes how to schedule the day, time, and
                              		  duration of the automatic monthly reports.

Choose System > Scheduler > Monthly .

The Monthly Scheduler window displays.

From the Day of Month drop-down list box in the Monthly Bill
                                       			 Generation row, choose the day of the month on which you want the report to be
                                       			 generated.

If you set the value to a day that does not occur in a given month
                                          				(such as 29, 30, or 31), the report generates on the last day of that month.

From the Time drop-down list box in the Monthly Bill Generation
                                       			 row, choose the hour and minute when you want the report to be generated.

A 24-hour clock represents time, where 0 equals midnight, and 1
                                          				through 11 represent a.m. hours, and 12 through 23 represent the p.m. hours of
                                          				1 p.m. through 11 p.m., respectively.

From the Life drop-down list box in the Monthly Bill Generation
                                       			 row, choose the duration of the report from the range of 00 to 12 months. The
                                       			 option that you choose indicates how many months the report remains on the disk
                                       			 before the report gets deleted.

If you set the life of the report to 00, the report does not
                                                      				  generate.

From the Day of Month drop-down list box in the Other Monthly
                                       			 Reports row, choose the day of the month on which you want the reports to be
                                       			 generated.

If you set this value to a day that does not occur in a given
                                          				month (such as 29, 30, or 31), the report generates on the last day of that
                                          				month.

From the Time drop-down list box in the Other Monthly Reports row,
                                       			 choose the hour and minute that you want reports to be generated.

A 24-hour clock represents time, where 0 equals midnight, and 1
                                          				through 11 represent a.m. hours, and 12 through 23 represent the p.m. hours of
                                          				1 p.m. through 11 p.m., respectively.

From the Life drop-down list box in the Other Monthly Reports row,
                                       			 choose the life of the report from the range of 00 to 12 months. The option
                                       			 that you choose indicates how many months the report remains on the disk before
                                       			 the report gets deleted.

If you set the life of the report to 00, the report does not
                                                      				  generate.

Click the Update button.

Reports with report generation interval of Monthly in Automatic
                                          				Generation/Alert Option and enabled automatically generate every month at the
                                          				time that you specify and are deleted after the number of months that you
                                          				specify.

Changes take effect at midnight. For the changes to take effect
                                          				immediately, stop and restart the CAR Scheduler service in the Control Center -
                                          				Feature Services window.

To restore the defaults, click the Restore Defaults button. By default,
                                                      				  monthly bill reports run at 3 a.m. on the first day of every month and get
                                                      				  purged after two months, and other monthly reports run at 2 a.m. on the first
                                                      				  day of every month and get purged after two months.

## Alarms

This release of Unified Communications Manager introduces a CAR alarm catalog (CARAlarmCatalog.xml) for the CAR Scheduler.

The following table displays the alarms/alerts in this
                              		  catalog.

To configure these alarms, go to Cisco Unified Serviceability > Alarm > Configuration > CDR Services .

Name

Severity

Description

CARSchedulerJobFailed

ERROR_ALARM

A critical CAR scheduled job failed. An alert gets
                                          					 raised when critical CDR Scheduler jobs and tasks fail (for example,
                                          					 DailyCdrLoad, PopulateSchedules, etc.).

CARSchedulerJobError

ERROR_ALARM

A CAR scheduled job failed. An alarm gets sent for
                                          					 all other noncritical CAR Scheduler jobs and tasks (for example, daily, weekly,
                                          					 and monthly reports, QoSNotification, ChargeLimitNotification, etc.).

BadCDRFileFound

ERROR_ALARM

Bad CDR or CMR flat file was found during CDR Load
                                          					 to the CAR database. The CDR Loader can detect bad or corrupted CDR and/or CMR
                                          					 flat files and log the specified error. Information on the failure cause
                                          					 (specified reason for the bad record) and the failure summary (tracks number of
                                          					 bad records in comparison to the total records in the file) gets provided.

CARIDSEngineDebug

DEBUG_ALARM

Indicates debug events from CAR IDS database engine.
                                          					 This alarm provides low-level debugging information from CAR IDS database
                                          					 engine. System administrator can disregard this alarm.

CARIDSEngineInformation

INFORMATION_ALARM

No error has occurred but some routine event has
                                          					 completed in CAR IDS database engine.

CARIDSEngineCritical

CRITICAL_ALARM

This alarm does not compromise data or prevent the
                                          					 use of the system but requires monitoring by the CAR DB adminstrator.

CARIDSEngineFailure

ERROR_ALARM

Combined alarm for emergency and error situations.
                                          					 This alarm indicates that something unexpected occurred that can compromise
                                          					 data, or access to data, or cause CAR IDS to fail.

For additional information on these alarms and recommended
                              		  action, see the alarm definitions at Cisco Unified Serviceability > Alarm > Definitions > CARAlarmCatalog .

## Related Topics

## Additional
                        	 documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Note | The default batch size equals 600 CDR or CMR records. The default
                                          			 sleep time between each CDR batch equals 2500 ms and 3000 ms for each CMR
                                          			 batch. You can, however, configure the batch size from the
                                          			 tbl_system_preferences table "LOADER_BATCH" column to have any value between 50 and 2000. |
|---|---|

| Tip | To manually delete the CAR data and reload the database with CDRs. |
|---|---|

| Step 1 | Choose System > Scheduler > CDR
                                             				  Load . The CDR Load window displays. |
|---|---|
| Step 2 | Choose one of the following options: Disable Loader - To disable CDR data loading, check the Disable Loader check box and click the Update button. CDR data will not load into CAR until you enable CDR loading.
                                                					 Changes take effect at midnight. You can force the change to take effect
                                                					 immediately by stopping and restarting the CAR Scheduler service. To enable CDR data loading, uncheck the Disable Loader check box and continue
                                                					 with the next step to configure the load parameters. Continuous Loading 24/7 - To enable the CDR Loader to run
                                             				  continuously 24 hours a day, 7 days a week to load CDRs into the CAR database,
                                             				  check the Continuous Loading 24/7 check box and
                                             				  click the Update button. This choice represents the
                                             				  default setting for the CDR Load Scheduler. Note Under the default setting, only CDR records continuously
                                                            						load. The CMR records do not load. You must manually uncheck the Load CDR only check box to force the
                                                            						CMR records to continuously load with the CDR records. The CAR Scheduler service stops, and the CAR Loader, as
                                                					 configured, runs immediately (within 1 to 2 minutes). The CAR Scheduler service
                                                					 restarts. If no new files for processing exist, the CDR Loader sleeps and then
                                                					 checks periodically for new files to be loaded. Note If this option is chosen, it takes precedence over and
                                                            						ignores the other CDR and CMR load parameters on the screen, such as Time,
                                                            						Loading Interval, Duration, and Uninhibited Loading. Load CDR Only - To load only CDR records into the CAR
                                             				  database, check the Load CDR only check box and click the Update button. Continue to the next step
                                             				  to configure the load parameters. With this option, CMR records do not load
                                             				  into the CAR database. This choice represents the default setting for the CDR
                                             				  Load Scheduler. | Note | Under the default setting, only CDR records continuously
                                                            						load. The CMR records do not load. You must manually uncheck the Load CDR only check box to force the
                                                            						CMR records to continuously load with the CDR records. | Note | If this option is chosen, it takes precedence over and
                                                            						ignores the other CDR and CMR load parameters on the screen, such as Time,
                                                            						Loading Interval, Duration, and Uninhibited Loading. |
| Note | Under the default setting, only CDR records continuously
                                                            						load. The CMR records do not load. You must manually uncheck the Load CDR only check box to force the
                                                            						CMR records to continuously load with the CDR records. |
| Note | If this option is chosen, it takes precedence over and
                                                            						ignores the other CDR and CMR load parameters on the screen, such as Time,
                                                            						Loading Interval, Duration, and Uninhibited Loading. |
| Step 3 | In the Load CDR & CMR area, complete the fields as described
                                       			 in the following table. Table 1. Load CDR and CMR Values Field Value Time Choose the hour and minute that you want CAR to
                                                      						  begin loading CDR data from the CDR flat files. Loading Interval Choose the interval at which you want records
                                                      						  loaded. The interval can range from every 15 minutes to every 24 hours. Duration Enter the number of minutes that you want to
                                                      						  allow CDR data to load. Depending on the size of the CDR flat files, CAR
                                                      						  performance may degrade when CDRs load. You can limit the time that is allowed
                                                      						  for loading, but in doing so, the possibility exists that only a portion of the
                                                      						  CDR data will be loaded in the time that you set. Be sure to reconcile the
                                                      						  duration limit that you place with the interval. For example, if you load CDR
                                                      						  data every 15 minutes, the duration of loading cannot exceed 15 minutes. Uninhibited loading allows you to set a time during which CDR data
                                          				will load continuously. CDR data does not load automatically in the duration that is specified. The CDR
                                          				data loads uninhibited in the specified duration only if loading starts at the
                                          				duration that is specified in the Load CDR and CMR area settings. If CDR data
                                          				loading starts at an uninhibited loading interval, loading continues to the end
                                          				of the uninhibited loading interval, plus the time in the duration field that
                                          				is set in the Load CDR and CMR area, or until no new files to process exist. Uninhibited loading take precedence over any values that are set
                                          				for scheduled loading. If you do not want uninhibited loading of CDR data, set
                                          				the From and To values at 00:00. | Field | Value | Time | Choose the hour and minute that you want CAR to
                                                      						  begin loading CDR data from the CDR flat files. | Loading Interval | Choose the interval at which you want records
                                                      						  loaded. The interval can range from every 15 minutes to every 24 hours. | Duration | Enter the number of minutes that you want to
                                                      						  allow CDR data to load. Depending on the size of the CDR flat files, CAR
                                                      						  performance may degrade when CDRs load. You can limit the time that is allowed
                                                      						  for loading, but in doing so, the possibility exists that only a portion of the
                                                      						  CDR data will be loaded in the time that you set. Be sure to reconcile the
                                                      						  duration limit that you place with the interval. For example, if you load CDR
                                                      						  data every 15 minutes, the duration of loading cannot exceed 15 minutes. |
| Field | Value |
| Time | Choose the hour and minute that you want CAR to
                                                      						  begin loading CDR data from the CDR flat files. |
| Loading Interval | Choose the interval at which you want records
                                                      						  loaded. The interval can range from every 15 minutes to every 24 hours. |
| Duration | Enter the number of minutes that you want to
                                                      						  allow CDR data to load. Depending on the size of the CDR flat files, CAR
                                                      						  performance may degrade when CDRs load. You can limit the time that is allowed
                                                      						  for loading, but in doing so, the possibility exists that only a portion of the
                                                      						  CDR data will be loaded in the time that you set. Be sure to reconcile the
                                                      						  duration limit that you place with the interval. For example, if you load CDR
                                                      						  data every 15 minutes, the duration of loading cannot exceed 15 minutes. |
| Step 4 | In the Uninhibited Loading of CDR area, complete the fields as
                                       			 described in the following table: Table 2. Uninhibited Loading of CDR Values Field Value From Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to begin. To Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to end. | Field | Value | From | Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to begin. | To | Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to end. |
| Field | Value |
| From | Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to begin. |
| To | Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to end. |
| Step 5 | Click the Update button. CAR will load CDR data based on the time, interval, and duration
                                          				that you have specified. Changes take effect at midnight. You can force the
                                          				change to take effect immediately by stopping and restarting the CAR Scheduler
                                          				service. Note If Continuous Loading 24/7 is selected, the CAR Scheduler
                                                      				  service restarts automatically when the Update button is clicked. CAR will load
                                                      				  CDR data immediately (within 1 to 2 minutes). | Note | If Continuous Loading 24/7 is selected, the CAR Scheduler
                                                      				  service restarts automatically when the Update button is clicked. CAR will load
                                                      				  CDR data immediately (within 1 to 2 minutes). |
| Note | If Continuous Loading 24/7 is selected, the CAR Scheduler
                                                      				  service restarts automatically when the Update button is clicked. CAR will load
                                                      				  CDR data immediately (within 1 to 2 minutes). |

| Note | Under the default setting, only CDR records continuously
                                                            						load. The CMR records do not load. You must manually uncheck the Load CDR only check box to force the
                                                            						CMR records to continuously load with the CDR records. |
|---|---|

| Note | If this option is chosen, it takes precedence over and
                                                            						ignores the other CDR and CMR load parameters on the screen, such as Time,
                                                            						Loading Interval, Duration, and Uninhibited Loading. |
|---|---|

| Field | Value |
|---|---|
| Time | Choose the hour and minute that you want CAR to
                                                      						  begin loading CDR data from the CDR flat files. |
| Loading Interval | Choose the interval at which you want records
                                                      						  loaded. The interval can range from every 15 minutes to every 24 hours. |
| Duration | Enter the number of minutes that you want to
                                                      						  allow CDR data to load. Depending on the size of the CDR flat files, CAR
                                                      						  performance may degrade when CDRs load. You can limit the time that is allowed
                                                      						  for loading, but in doing so, the possibility exists that only a portion of the
                                                      						  CDR data will be loaded in the time that you set. Be sure to reconcile the
                                                      						  duration limit that you place with the interval. For example, if you load CDR
                                                      						  data every 15 minutes, the duration of loading cannot exceed 15 minutes. |

| Field | Value |
|---|---|
| From | Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to begin. |
| To | Choose the hour and minute that you want
                                                      						  continuous loading of CDR data to end. |

| Note | If Continuous Loading 24/7 is selected, the CAR Scheduler
                                                      				  service restarts automatically when the Update button is clicked. CAR will load
                                                      				  CDR data immediately (within 1 to 2 minutes). |
|---|---|

| Step 1 | Choose System > Scheduler > Daily . The Daily Scheduler window displays. |
|---|---|
| Step 2 | From the Time drop-down list box, choose the hour and minute when
                                       			 you want daily reports to be generated. A 24-hour clock represents time, where 0 equals midnight, and 1
                                          				through 11 represent a.m. hours, and 12 through 23 represent the p.m. hours of
                                          				1 p.m. through 11 p.m., respectively. |
| Step 3 | From the Life drop-down list box, choose the duration of the
                                       			 report from the range of 0 to 12 days. Tip If you set the life of the report to 00, the report does not
                                                      				  generate. | Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
| Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
| Step 4 | Click the Update button. Reports with report generation interval of Daily in the Automatic
                                          				Generation/Alert Option and enabled automatically generate every day at the
                                          				time that you specify and get deleted after the number of days that you
                                          				specify. Changes take effect at midnight. You can force the change to take
                                          				effect immediately by stopping and restarting the CAR Scheduler service. Tip To restore the defaults, click the Restore Defaults button. By default, the
                                                      				  daily reports run at 1 a.m. every day and get purged after two days. | Tip | To restore the defaults, click the Restore Defaults button. By default, the
                                                      				  daily reports run at 1 a.m. every day and get purged after two days. |
| Tip | To restore the defaults, click the Restore Defaults button. By default, the
                                                      				  daily reports run at 1 a.m. every day and get purged after two days. |

| Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
|---|---|

| Tip | To restore the defaults, click the Restore Defaults button. By default, the
                                                      				  daily reports run at 1 a.m. every day and get purged after two days. |
|---|---|

| Step 1 | Choose System > Scheduler > Weekly . The Weekly Scheduler window displays. |
|---|---|
| Step 2 | From the Day of Week drop-down list box, choose the day that you
                                       			 want reports to be generated. |
| Step 3 | From the Time drop-down list box, choose the hour and minute when
                                       			 you want reports to be generated. A 24-hour clock represents time, where 0 equals midnight, and 1
                                          				through 11 represent a.m. hours, and 12 through 23 represent the p.m. hours of
                                          				1 p.m. through 11 p.m., respectively. |
| Step 4 | From the Life drop-down list box, choose the duration of the
                                       			 report from the range of 00 to 12 weeks. The option that you choose indicates
                                       			 how many weeks the report remains on the disk before the report gets deleted. Tip If you set the life of the report to 00, the report does not
                                                      				  generate. | Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
| Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
| Step 5 | Click the Update button. Reports with report generation interval of Weekly in the Automatic
                                          				Generation/Alert Option and enabled automatically generate every week at the
                                          				time that you specify and get deleted after the number of weeks that you
                                          				specify. Changes take effect at midnight. For the changes to take effect
                                          				immediately, stop and restart the CAR Scheduler service in the Control Center -
                                          				Feature Services window. Tip To restore the defaults, click the Restore Defaults button. By default,
                                                      				  weekly reports run at 4 a.m. every Sunday and get purged after four weeks. | Tip | To restore the defaults, click the Restore Defaults button. By default,
                                                      				  weekly reports run at 4 a.m. every Sunday and get purged after four weeks. |
| Tip | To restore the defaults, click the Restore Defaults button. By default,
                                                      				  weekly reports run at 4 a.m. every Sunday and get purged after four weeks. |

| Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
|---|---|

| Tip | To restore the defaults, click the Restore Defaults button. By default,
                                                      				  weekly reports run at 4 a.m. every Sunday and get purged after four weeks. |
|---|---|

| Step 1 | Choose System > Scheduler > Monthly . The Monthly Scheduler window displays. |
|---|---|
| Step 2 | From the Day of Month drop-down list box in the Monthly Bill
                                       			 Generation row, choose the day of the month on which you want the report to be
                                       			 generated. If you set the value to a day that does not occur in a given month
                                          				(such as 29, 30, or 31), the report generates on the last day of that month. |
| Step 3 | From the Time drop-down list box in the Monthly Bill Generation
                                       			 row, choose the hour and minute when you want the report to be generated. A 24-hour clock represents time, where 0 equals midnight, and 1
                                          				through 11 represent a.m. hours, and 12 through 23 represent the p.m. hours of
                                          				1 p.m. through 11 p.m., respectively. |
| Step 4 | From the Life drop-down list box in the Monthly Bill Generation
                                       			 row, choose the duration of the report from the range of 00 to 12 months. The
                                       			 option that you choose indicates how many months the report remains on the disk
                                       			 before the report gets deleted. Tip If you set the life of the report to 00, the report does not
                                                      				  generate. | Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
| Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
| Step 5 | From the Day of Month drop-down list box in the Other Monthly
                                       			 Reports row, choose the day of the month on which you want the reports to be
                                       			 generated. If you set this value to a day that does not occur in a given
                                          				month (such as 29, 30, or 31), the report generates on the last day of that
                                          				month. |
| Step 6 | From the Time drop-down list box in the Other Monthly Reports row,
                                       			 choose the hour and minute that you want reports to be generated. A 24-hour clock represents time, where 0 equals midnight, and 1
                                          				through 11 represent a.m. hours, and 12 through 23 represent the p.m. hours of
                                          				1 p.m. through 11 p.m., respectively. |
| Step 7 | From the Life drop-down list box in the Other Monthly Reports row,
                                       			 choose the life of the report from the range of 00 to 12 months. The option
                                       			 that you choose indicates how many months the report remains on the disk before
                                       			 the report gets deleted. Tip If you set the life of the report to 00, the report does not
                                                      				  generate. | Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
| Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
| Step 8 | Click the Update button. Reports with report generation interval of Monthly in Automatic
                                          				Generation/Alert Option and enabled automatically generate every month at the
                                          				time that you specify and are deleted after the number of months that you
                                          				specify. Changes take effect at midnight. For the changes to take effect
                                          				immediately, stop and restart the CAR Scheduler service in the Control Center -
                                          				Feature Services window. Tip To restore the defaults, click the Restore Defaults button. By default,
                                                      				  monthly bill reports run at 3 a.m. on the first day of every month and get
                                                      				  purged after two months, and other monthly reports run at 2 a.m. on the first
                                                      				  day of every month and get purged after two months. | Tip | To restore the defaults, click the Restore Defaults button. By default,
                                                      				  monthly bill reports run at 3 a.m. on the first day of every month and get
                                                      				  purged after two months, and other monthly reports run at 2 a.m. on the first
                                                      				  day of every month and get purged after two months. |
| Tip | To restore the defaults, click the Restore Defaults button. By default,
                                                      				  monthly bill reports run at 3 a.m. on the first day of every month and get
                                                      				  purged after two months, and other monthly reports run at 2 a.m. on the first
                                                      				  day of every month and get purged after two months. |

| Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
|---|---|

| Tip | If you set the life of the report to 00, the report does not
                                                      				  generate. |
|---|---|

| Tip | To restore the defaults, click the Restore Defaults button. By default,
                                                      				  monthly bill reports run at 3 a.m. on the first day of every month and get
                                                      				  purged after two months, and other monthly reports run at 2 a.m. on the first
                                                      				  day of every month and get purged after two months. |
|---|---|

| Name | Severity | Description |
|---|---|---|
| CARSchedulerJobFailed | ERROR_ALARM | A critical CAR scheduled job failed. An alert gets
                                          					 raised when critical CDR Scheduler jobs and tasks fail (for example,
                                          					 DailyCdrLoad, PopulateSchedules, etc.). |
| CARSchedulerJobError | ERROR_ALARM | A CAR scheduled job failed. An alarm gets sent for
                                          					 all other noncritical CAR Scheduler jobs and tasks (for example, daily, weekly,
                                          					 and monthly reports, QoSNotification, ChargeLimitNotification, etc.). |
| BadCDRFileFound | ERROR_ALARM | Bad CDR or CMR flat file was found during CDR Load
                                          					 to the CAR database. The CDR Loader can detect bad or corrupted CDR and/or CMR
                                          					 flat files and log the specified error. Information on the failure cause
                                          					 (specified reason for the bad record) and the failure summary (tracks number of
                                          					 bad records in comparison to the total records in the file) gets provided. |
| CARIDSEngineDebug | DEBUG_ALARM | Indicates debug events from CAR IDS database engine.
                                          					 This alarm provides low-level debugging information from CAR IDS database
                                          					 engine. System administrator can disregard this alarm. |
| CARIDSEngineInformation | INFORMATION_ALARM | No error has occurred but some routine event has
                                          					 completed in CAR IDS database engine. |
| CARIDSEngineCritical | CRITICAL_ALARM | This alarm does not compromise data or prevent the
                                          					 use of the system but requires monitoring by the CAR DB adminstrator. |
| CARIDSEngineFailure | ERROR_ALARM | Combined alarm for emergency and error situations.
                                          					 This alarm indicates that something unexpected occurred that can compromise
                                          					 data, or access to data, or cause CAR IDS to fail. |