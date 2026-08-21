---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--c32b4d1326
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_011001.html
retrieved_at: 2026-08-21T01:37:07.615305+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CDRs

## Chapter: CDRs

# CDRs

## CDR Data

Call detail records (CDRs) detail the called number, the number that places the call, the date and time that the call starts,
                              the time that the call connects, and the time that the call ends. Call management records (CMRs), or diagnostic records, detail
                              the jitter, lost packets, the amount of data sent and received during the call, and latency. CDR data comprises CDRs and CMRs
                              collectively. A single call can result in the generation of several CDRs and CMRs. Unified Communications Manager records information regarding each call in CDRs and CMRs. CDRs and CMRs, known collectively as CDR data, serve as the basic
                              information source for CAR.

The Cisco CDR Agent service transfers CDR and CMR files that Unified Communications Manager generates from the local host to the CDR repository node, where the CDR Repository Manager service runs over a SFTP connection.
                              If the SFTP connection fails, the Cisco CDR Agent services continue to make connection attempts to the CDR repository node
                              until a connection is made. The Cisco CDR Agent service sends any accumulated CDR files when the connection to the CDR Repository
                              node resumes. The CDR Repository Manager service maintains the CDR and CMR files, allocates the amount of disk space for use
                              by CMRs and CDRs, sends the files to up to three configured destinations, and tracks the delivery result for each destination.
                              CAR accesses the CDR/CMR files in the directory structure that the CDR Repository Manager service creates.

The high and low water mark settings that you configure
                              		  specify percentages of the total disk space that are allocated for the CDR
                              		  repository. Although the preserved folder under the CDR repository folder
                              		  contributes to the high and low water mark percentages, Log Partition
                              		  Monitoring never deletes the folder if the high water mark gets reached. If the
                              		  high water mark gets reached, the CDR Repository Manager deletes processed CDR
                              		  files until the low water mark is reached or all processed files are deleted,
                              		  whichever comes first. If all processed CDR files are deleted but the low water
                              		  mark has not been reached, the deletion stops. The CDRHighWaterMarkExceeded
                              		  alarm gets generated until the system reaches the maximum disk allocation. If
                              		  the maximum disk allocation gets reached, the system deletes undelivered files,
                              		  and files within the preservation duration, starting with the oldest files,
                              		  until disk utilization falls below the high water mark. If you receive the
                              		  CDRMaximumDiskSpaceExceeded alarm repeatedly for this scenario, either increase
                              		  the disk allocation or lower the number of preservation days.

When the disk allocation usage exceeds the configured high water mark threshold value, LMP also purges the CDR and CMR data
                                          that are exported at the following path automatically: /var/log/active/tomcat/logs/car/carreports/reports/ondemand/temp .

Customers or any third-party applications should ensure to retrieve the exported files immediately to avoid losing their buffered
                                          historical data.

Information on these alarms is found in the CDR Repository Alarm Catalog (CDRRepAlarmCatalog). The following table displays
                              the alarms and alerts in this catalog.

To configure these alarms, go to Cisco Unified Serviceability > Alarm > Configuration > CDR Services .

Name

Severity

Description

CDRFileDeliveryFailed

ERROR_ALARM

SFTP delivery of CDR files to the outside billing
                                          					 server failed.

CDRAgentSendFileFailed

ERROR_ALARM

The CDR Agent cannot send CDR files from the Cisco Unified CM node to the CDR Repository node within the Unified Communications Manager cluster.

CDRHWMExceeded

WARNING_ALARM

The high water mark (HWM) for CDR files was reached;
                                          					 some successfully delivered CDR files have been deleted.

CDRMaximumDiskSpaceExceeded

CRITICAL_ALARM

The CDR files disk usage exceeded the maximum disk
                                          					 allocation. Some undelivered files may have been deleted to bring disk usage
                                          					 down.

CDRFileDeliveryFailureContinues

ERROR_ALARM

SFTP delivery of CDR files failed on retries.

CDRAgentSendFileFailureContinues

ERROR_ALARM

The CDR Agent cannot send CDR files from the Cisco
                                          					 Unified CM node to the CDR Repository node on retries.

For additional information on these alarms and recommended
                              		  action, see the alarm definitions at Cisco Unified Serviceability > Alarm > Definitions > CDRRepAlarmCatalog .

For more information on CDR services and alarms, see the Cisco Unified Serviceability Administration Guide .

## CAR Database

If you upgrade from Unified Communications Manager 4.x, Unified Communications Manager saves the content of the Unified Communications Manager 4.x CAR database to CSV files. The Unified Communications Manager 4.x CAR database has part of the CDR information. The Unified Communications Manager 4.x CDR database stores the complete information about CDRs. This database does not migrate. The Data Migration Tool uses
                              the CAR database CSV files to migrate the CAR database. The system stores the CSV files in the /common/download/windows/car
                              directory. The system stores the pregenerated reports in the /common/download/windows/pregenerated database. Because no corresponding
                              CDR database exists in Unified Communications Manager 5.x and later releases, the complete CDR data does not migrate to the Unified Communications Manager 5.x, 6.x, or 7.x system. The Unified Communications Manager 5.x, 6.x, and 7.x CAR database schema gets extended to contain complete CDR information, but only for the new CDRs that are
                              generated by the Unified Communications Manager 5.x, 6.x, and 7.x system.

The version of CAR that runs on Unified Communications Manager 5.x, 6.x, and 7.x does not retain CDRs that are older than the ART database age that gets configured in the Unified Communications Manager 4.x ART database. The ART database age gets configured in the Configure Automatic Database Purge window of ART. The default ART database age is 180 days. If the ART database age is greater than 180 days, the CAR database
                                          in Unified Communications Manager 5.x, 6.x, and 7.x will retain only 180 days of data. However, if the ART database age is less than 180 days, only data within
                                          the specified age limit get retained in the Unified Communications Manager 5.x, 6.x, or 7.x CAR database after migration. If you migrate records older than 180 days, the system deletes these records
                                          immediately after you upgrade.

The Unified Communications Manager installation program limits the time period for the migration of the CAR records from the CSV files in the Data Migration
                              Assistant (DMA) TAR file to the CAR database on the upgraded system. The migration time period is 60 minutes. To allow the
                              migration of the highest number of CSV files in the allotted time period, CAR record migration uses the following steps:

Data migration
                                    				begins with the migration of the billing records from the tbl_billing_data CSV
                                    				file to the tbl_billing_data table of the CAR database. Data migration begins
                                    				with the youngest record and proceeds toward the oldest record in the CSV file.
                                    				The billing data migration stops when there are no more billing records to
                                    				migrate or the migration time period reaches 60 minutes.

If time remains
                                    				after the billing data gets migrated, data migration proceeds with the
                                    				migration of error records from the tbl_billing_error CSV file to the
                                    				tbl_billing_error table of the CAR database. Data migration begins with the
                                    				youngest record and proceeds toward the oldest record in the CSV file. For each
                                    				error record that gets migrated, CAR migrates the data that corresponds to the
                                    				error_record_id that is present in the tbl_error_id_map CSV file into the
                                    				tbl_error_id_map table of the CAR database. This action ensures that error
                                    				record data migration stays consistent with data in the tbl_error_id_map. The
                                    				error record data migration stops when there are no more error records to
                                    				migrate or the migration period reaches 60 minutes.

If the 60
                              		  minute migration time limit occurs at any point in the migration process, CAR
                              		  data migration ceases and the tbl_system_preferences of the CAR database gets
                              		  updated to reflect the data present in the upgraded system database.

You can integrate a Windows version of Unified Communications Manager with a standalone Cisco Unity Connection system. In this particular situation, the CAR installation program will detect this option. CAR does not get supported on
                                          a Cisco Unity Connection system and will not get installed. When CAR is not installed, Cisco Unified CM Administration cannot activate, deactivate, start, stop, or restart CAR Web Service and CAR Scheduler from Cisco Unified Serviceability .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Note | When the disk allocation usage exceeds the configured high water mark threshold value, LMP also purges the CDR and CMR data
                                          that are exported at the following path automatically: /var/log/active/tomcat/logs/car/carreports/reports/ondemand/temp . Customers or any third-party applications should ensure to retrieve the exported files immediately to avoid losing their buffered
                                          historical data. |
|---|---|

| Name | Severity | Description |
|---|---|---|
| CDRFileDeliveryFailed | ERROR_ALARM | SFTP delivery of CDR files to the outside billing
                                          					 server failed. |
| CDRAgentSendFileFailed | ERROR_ALARM | The CDR Agent cannot send CDR files from the Cisco Unified CM node to the CDR Repository node within the Unified Communications Manager cluster. |
| CDRHWMExceeded | WARNING_ALARM | The high water mark (HWM) for CDR files was reached;
                                          					 some successfully delivered CDR files have been deleted. |
| CDRMaximumDiskSpaceExceeded | CRITICAL_ALARM | The CDR files disk usage exceeded the maximum disk
                                          					 allocation. Some undelivered files may have been deleted to bring disk usage
                                          					 down. |
| CDRFileDeliveryFailureContinues | ERROR_ALARM | SFTP delivery of CDR files failed on retries. |
| CDRAgentSendFileFailureContinues | ERROR_ALARM | The CDR Agent cannot send CDR files from the Cisco
                                          					 Unified CM node to the CDR Repository node on retries. |

| Note | The version of CAR that runs on Unified Communications Manager 5.x, 6.x, and 7.x does not retain CDRs that are older than the ART database age that gets configured in the Unified Communications Manager 4.x ART database. The ART database age gets configured in the Configure Automatic Database Purge window of ART. The default ART database age is 180 days. If the ART database age is greater than 180 days, the CAR database
                                          in Unified Communications Manager 5.x, 6.x, and 7.x will retain only 180 days of data. However, if the ART database age is less than 180 days, only data within
                                          the specified age limit get retained in the Unified Communications Manager 5.x, 6.x, or 7.x CAR database after migration. If you migrate records older than 180 days, the system deletes these records
                                          immediately after you upgrade. |
|---|---|

| Note | You can integrate a Windows version of Unified Communications Manager with a standalone Cisco Unity Connection system. In this particular situation, the CAR installation program will detect this option. CAR does not get supported on
                                          a Cisco Unity Connection system and will not get installed. When CAR is not installed, Cisco Unified CM Administration cannot activate, deactivate, start, stop, or restart CAR Web Service and CAR Scheduler from Cisco Unified Serviceability . |
|---|---|