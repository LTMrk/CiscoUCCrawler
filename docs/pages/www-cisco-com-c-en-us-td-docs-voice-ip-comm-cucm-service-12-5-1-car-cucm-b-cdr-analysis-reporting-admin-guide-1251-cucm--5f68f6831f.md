---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--5f68f6831f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_01.html
retrieved_at: 2026-08-21T01:33:25.787577+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CDR Analysis and Reporting

## Chapter: CDR Analysis and Reporting

# CDR Analysis and Reporting

Cisco Unified Serviceability supports CDR Analysis and Reporting (CAR) under the
                        		Tools menu. CAR generates reports for Quality of Service (QoS), traffic, and
                        		billing information.

CAR is not intended to replace call accounting and billing
                        		solutions that third-party companies provide. You can find the companies that
                        		provide these solutions and that are members of the Cisco Technology Developer
                        		Program by searching the home page of the Cisco Developer Community.

CAR does not handle iDivert calls (feature that diverts calls to a
                                    		  voice-messaging system) and treats them as normal calls. The part of the call
                                    		  after the iDivert feature gets activated may not get charged to the correct
                                    		  party.

## CDR Analysis and Reporting Overview

As its primary function, CAR generates reports about the users of Unified Communications Manager and generates reports on the system status with respect to call processing. CAR also performs CAR database management activities.
                              You can perform these tasks in one of the following ways:

Automatically configure the required tasks to take place.

Manually perform the tasks by using the web interface.

You access CAR from the Tools menu of Cisco Unified Serviceability after you activate the appropriate services as described in the Activate CAR .

All CAR reports use CDR data. CAR processes the CDRs from
                              		  flat files that the CDR Repository service places in the CDR repository folder
                              		  structure. CAR processes CDRs at a scheduled time and frequency. By default,
                              		  CDR data loads continuously 24 hours per day and seven days per week; however,
                              		  you can set the loading time, interval, and duration as needed. In addition,
                              		  the default setting loads only CDR records. CMR records do not get loaded by
                              		  default.

An option allows you to uncheck the "Load CDR Only" check box in the CAR System Scheduler window to
                                          			 allow CMR records to load. See Set Up CDR Load Schedule for additional information.

CAR retrieves information that is required for various reports from CDRs, CMRs, and the Unified Communications Manager database.

### Scheduling Reports

After CAR is activated on your system, you can schedule CAR
                              		  reports to generate automatically at a regular time. Each report that can be
                              		  scheduled has its own report generation interval. You can make the report
                              		  generation interval be daily, weekly, or monthly. Scheduling Daily reports
                              		  schedules all the reports that have report generation intervals of daily.
                              		  Similarly, scheduling Weekly or Monthly reports would schedule the reports that
                              		  have report generation intervals of weekly or monthly. You can also specify the
                              		  time to keep a report before it gets automatically deleted.

By default, CAR uses the following report generation and
                              		  deletion schedule:

Daily reports run at 1 a.m. every day. These reports get purged
                                    				after two days.

Weekly reports run at 4 a.m. every Sunday. These reports get
                                    				purged after four weeks.

Monthly bill reports run at 3 a.m. on the first day of every
                                    				month. These reports get purged after two months.

Other monthly reports run at 2 a.m. on the first day of every
                                    				month. These reports get purged after two months.

If you upgrade your system to a new version of Unified Communications Manager , you must disable the CAR reports that generate automatically, so you conserve system resources during the upgrade process.

For a list of reports and the default generation schedule,
                              		  see the Enable Automatic Generation Reports .

For system monitoring, automatically generate various
                              		  reports, such as QoS reports, and review them at regular intervals, perhaps
                              		  every day if you have a very large system, or every week or every two weeks for
                              		  smaller systems. QoS reports help you determine the quality of calls that run
                              		  on your network and judge whether you need additional hardware to improve
                              		  performance. You can use utilization reports for gateways, voice messaging,
                              		  conference bridge, route groups, route lists, and route patterns to provide a
                              		  picture of the usage to help with system handling.

You can also customize the report parameters and enable a
                              		  mailing option, so reports get emailed when they are created. The Customize
                              		  Parameters option allows you to customize the report parameters for particular
                              		  reports in the Customize Parameters window. For each individual report, you can
                              		  customize the parameters for that report.

### Setting Up Alerts

CAR provides email alerts for various events, including the
                              		  following events:

Charge Limit Notification indicates when the daily charge limit
                                    				for a user exceeds the specified maximum. You can set the maximum in the Report
                                          					 Config > Notification Limits window.

QoS Notification indicates when the percentage of good calls drops
                                    				below a specified range or the percentage of poor calls exceeds a specified
                                    				limit. You can set the range in the Report Config > Notification Limits window.

Enabling the system for email alerts comprises a two-step
                              		  process. First, you must specify the mail server configuration information
                              		  ( System > System
                                    				Parameters > Mail Parameters ).
                              		  CAR uses the configuration information to successfully connect to the email
                              		  server. Next, you must enable the email alerts on the Automatic Report
                              		  Generation/Alert window ( Report
                                    				Config > Automatic
                                    				Generation/Alert ). By default, CAR enables email
                              		  alerts for some, but not all, reports.

Be sure to disable the automatic email alerts to conserve system resources while you upgrade your system to a later version
                              of Unified Communications Manager .

The system does not provide email alerts to application users
                                          			 because no mail ID exists for an application user.

### Purging CAR Data

This section contains information on the following topics:

Automatic purging

Manual purging

Event log purging

CAR provides automatic and manual purging of the CAR
                              		  database. By default, the system enables automatic purging. Before and after
                              		  loading CDRs/CMRs, CAR checks the size of the CAR database and invokes
                              		  automatic purging, if necessary, to control the CAR database size.

With automatic purging, CAR continuously monitors the number
                              		  of days that the CDRs are kept in the CAR database; when the CDR age exceeds
                              		  the maximum number of days as configured in the maximum age setting in the
                              		  Configure Automatic Database Purge window, CAR deletes all CDRs that are older
                              		  than the number of days that you configured.

In the Configure Automatic Database Purge window, you specify
                              		  the percentages of the CAR database that you want to allot for CAR data; the
                              		  system maintains the CAR database size between the high water mark and low
                              		  water mark that you specify. When the CAR database size exceeds the low water
                              		  mark, CAR sends an email to CAR administrators. When the CAR database size exceeds the high water mark, CAR begins to
                              delete the partitions from billing data and billing error tables, starting from the oldest date partitions until under the
                              specified limit, allowing the system to continue loading the latest records.  In cases where there are a large number of CDRs
                              present in the CAR database and deleting the partitions does not lower the limit, CAR will keep at least two days worth of
                              data and send an email to CAR administrators.

Version

Maximum Number of CDR Records

Maximum Size of Database

Maximum Aggregate Busy Hour Call Attempts (BHCA)

Unified Communications Manager

2 million records

6 GB

10,000

Cisco Unified Communications Manager Business Edition 5000

1 million records

3 GB

5,000

Configure manual database purge when you want to delete
                              		  records that are older than a particular date or that fall in a specific date
                              		  range, but you do not want to change the automatic purging schedule. You can
                              		  also reload the CAR database with CDR records by clicking the Reload button in
                              		  the Manual Purge window. You may want to reload the database to reclassify
                              		  calls after dial-plan updates, user-device association changes, call rate
                              		  changes, and so on. After the system loads the new records, the system loads
                              		  the records according to the schedule in the configured CDR load schedule. By
                              		  default, CDR data loads 24 hours per day, 7 days per week.

Event log purging, which is a daily scheduled job that
                              		  monitors the tbl_event_log table, automatically deletes the tbl_event_ log
                              		  records to keep the latest 3 days of daily jobs, the latest 3 weeks of weekly
                              		  jobs, and the latest 3 months of monthly jobs; that is, if more than 1500 rows
                              		  exist in the tbl_event_log table, CAR automatically enables event log purging
                              		  and does not send an e-mail when event log purging occurs.

### Call Costs

You can use CAR to set a base monetary rate for the cost of
                              		  calls on the basis of a time increment. Then, you can further qualify the cost
                              		  by applying the time-of-day and voice-quality factors. Service providers who
                              		  must account for service to subscribers use this feature. Some organizations
                              		  also use this information to establish billing costs for users and departments
                              		  in the organization for accounting or budgeting purposes.

Reports that use these rating parameters include Individual
                              		  Bill, Department Bill, Top N by Charge, Top N by Number, and Top N by Duration.

If you do not change the default value for charge base/block, the
                                          			 cost will always remain zero because the default base charge per block equals
                                          			 zero.

If you do not want to increase call cost by voice quality, you can
                                          			 use the default values. The default multiplication factor specifies 1.00, so no
                                          			 increase in call cost for voice quality occurs.

For more information on setting call rates, see CAR Rating Engine .

### Tracking Activity

CAR provides logs that can track the status of the various
                              		  activities. The event log tracks events that the CAR Scheduler triggers, such
                              		  as automatically generated reports, loading of CDRs, notifications, report
                              		  deletions, database purging and monitoring, and event tracking.

## Roles

CAR provides reporting capabilities for three levels of
                              		  users:

Administrators use all the features of CDR Analysis and Reporting;
                                    				for example, they can generate system reports to help with load balancing,
                                    				system performance, and troubleshooting.

Managers can generate reports for users, departments, and QoS to
                                    				help with call monitoring for budgeting or security purposes and for
                                    				determining the voice quality of the calls.

Individual users can generate a billing report for calls.

Any user can act as a CAR administrator. Users who have been
                              		  identified as CAR administrators have full control over the CAR system. The
                              		  administrator can modify all the parameters that relate to the system and the
                              		  reports.

CAR requires a minimum of one administrator.

You set up administrators, managers, and users in Cisco Unified CM Administration . For more information, see the Generate CAR Users .

## Reports

From CAR, you can generate reports on demand, or if you are an
                           		administrator, you can schedule reports for automatic generation. You can view
                           		reports in comma separated values (CSV) format or portable document format
                           		(PDF). If you choose PDF, you must have Adobe Acrobat Reader installed on your
                           		PC.

### Report Information

For all CAR reports that show the pattern for Hour of Day,
                                 		  Day of Week, and Day of Month, the charts and tables get shown according to the
                                 		  following conditions:

When no records match the time range that is specified (hour of
                                       				day, day of week, or day of month) in the search criteria, the report displays
                                       				a value of 0.00 for all of the days/hours.

If all records that are returned have a value of 0.00, CAR does
                                       				not display the charts. CAR displays the charts if any record contains a
                                       				non-zero value.

When records get generated (for at least one day in the chosen
                                       				date range) and the number of days that is chosen is more than the number of
                                       				days that the report can show (more than seven for weekly and more than 31 for
                                       				monthly), the chart displays all the days (with 0 value for the days that do
                                       				not generate records). A table displays for all the days with relevant value
                                       				and 0.00 for the days that do not contain data.

When records generate (for at least one day in the chosen date
                                       				range) and the number of days that is chosen is less than the number of days
                                       				that the report can show (less than 7 for weekly and less than 31 for monthly),
                                       				the chart displays all the days (with 0 value for the days that do not generate
                                       				records). A table displays all the days with relevant value and 0.00 for the
                                       				days that do not contain data.

In all the CAR reports that display username, userid
                                 		  displays if CAR cannot retrieve the username. This situation can occur when the
                                 		  report gets generated for prior data where the user that was involved in a call
                                 		  at that time no longer exists in the system ( Cisco Unified Communications Manager database).

### Generated Report Schedule

Automatically generating reports comprises a two-step
                                 		  process. First, you must enable the reports that you want to have generated.
                                 		  Second, you must schedule the reports for the day and time that you want them
                                 		  to generate. CAR provides a default schedule, so if the default schedule is
                                 		  acceptable, you need only enable the reports that you want to automatically
                                 		  generate.

Reports and e-mail alerts do not automatically get enabled
                                 		  on a new installation. You must enable the reports that you want to
                                 		  automatically generate. To enable or disable report generation, see the Enable Automatic Generation Reports for instructions on how to generate reports and e-mails automatically.

To change the specific time each day, week, or month that
                                 		  reports get generated and get purged from the system, see CAR System Scheduler .

## Audit Logging

With audit logging, any configuration change to the Unified Communications Manager system gets logged in separate log files for auditing. An audit event is any event that is required to be logged. Cisco Unified
                              CDR Analysis and Reporting creates audit logs for these events:

Scheduling the CDR Loader.

Scheduling the daily, weekly, and monthly user reports, system reports, and device reports.

Mail parameters configurations.

Dial plan configurations.

Gateway configurations.

System preferences configurations.

Autopurge configurations.

Rating engine configurations for duration, time of day, and voice quality.

QoS configurations.

Automatic generation/alert of pregenerated reports configurations.

Notification limits configurations.

Refer to the "Configuring the Audit Log" chapter in the Cisco Unified Serviceability Administration Guide for information on how to configure the Audit Log. Refer to the "Working With Trace and Log Central" chapter in the Cisco Unified Real-Time Monitoring Tool Administration Guide for information on how to view the audit logs.

## Log-On
                        	 Message

You can upload a text file that contains a customized log-on message that appears on the initial Cisco Unified Communications Manager CDR Analysis and Reporting window.

For
                              		  more information and the procedure for uploading your customized log-on
                              		  message, see the Administration Guide for Cisco Unified Communications
                                 			 Manager .

## Internationalization

CAR,
                              		  designed to be internationalized to handle any locale (or language), includes a
                              		  database that can also handle any locale.

CAR supports all Latin-1 language and Unicode language locales as Unified Communications Manager help specifies. Latin-1 languages include English and Western European languages. Unicode languages include Japanese and
                                          Chinese.

Two types
                              		  of locale exists: user and network. Each locale comprises a set of locale
                              		  files. The following definitions describe the two types of files:

User - Files
                                    				that relate to user-related functions, such as phone display text, user
                                    				applications, and user web pages.

Network - Files
                                    				that relate to network-related functions, such as phone and gateway tones.
                                    				Country names designate network locales.

CAR
                              		  supports the locales only if the Locale Installer has installed locales.

For Unified Communications Manager , make sure that you have first installed the Cisco Unified Communications Manager Locale Installer on every server in the cluster. Installing the Locale Installer ensures that you have the latest translated
                                          text available for CAR.

For more information about
                                          			 the Cisco Unified Communications Manager Locale Installer,
                                          			 see the Administration Guide for Cisco Unified Communications
                                             				Manager .

Only User
                              		  and Manager windows support multiple locales. Administrator windows display in
                              		  English.

In the Cisco Unified CM Administration , set the user-preferred locale in the Unified Communications Manager database. You do this when you create a user from the End User Configuration window. Specify the preferred locale along with
                              the user name, user ID, and so on. The Unified Communications Manager database stores this information.

For
                              		  more detailed information, see the Cisco Unified Communications Manager Online Help .

These
                              		  sections describe the elements that make up the internationalization of CAR.

### Logon
                              		  Page

When the client (browser) requests the logon information, the logon window header includes the most preferred locale of the
                              client. The CAR system checks whether the CAR UI supports this locale. If the CAR UI does not support the locale, or if the
                              locale is not installed in the system, the logon window displays in the Unified Communications Manager system default locale that is set in the Cisco Communications Manager Enterprise parameter. If CAR does not also support
                              this locale, or the locale is not installed in the system, the locale gets set to English_United_States.

### Authenticate and
                              		  Show CAR Pages for Post Logon Windows

User credentials (in any language) get authenticated through the Unified Communications Manager database, and then CAR windows for non-administrative users (users or managers) display the user preferred locale. If the
                              CAR UI does not support this locale, or if the locale is not installed in the system, the Unified Communications Manager system default locale gets used. If this locale is not supported by CAR, or is not installed in the system, windows display
                              in the most preferred locale of the browser. When the browser-preferred locale is also not supported or not installed, the
                              locale gets set to English_United_States. All information on the UI windows, including labels, number formats, and so on.,
                              displays based on the locale. The administrator windows always display in English.

### Reports

Reports,
                              		  which are generated in both CSV and PDF formats, display in the user preferred
                              		  locale for non-administrative users (users or managers). However, the dynamic
                              		  data (like the Company Name shown in the report header) displays in the same
                              		  language as was used to enter it in the database. The locale provides the basis
                              		  for the header, footers, number formats, and some static data (like call
                              		  classification). Reports for administrators display in English.

## Web Browsers

The CAR program supports the following web browsers:

Microsoft Internet Explorer Release 7.0

From any user PC in your network, browse into a server where
                              		  CDR Analysis and Reporting displays in Cisco Unified Serviceability and log in as a CAR administrator, manager, or user.

## Online Help

To access CAR documentation online help, choose Help > Contents and
                                    				Index (for a list of contents) or Help > For this
                                    				page (for information that is specific to the page
                              		  that displays.)

## Upgrade

When you upgrade from an earlier version of Unified Communications Manager to a later version of Unified Communications Manager , you may not be able to upgrade all your CDR data. For additional information about the limitations that affect the amount
                              of CDR data that may be available after upgrade, see the CAR Database . You may also need to refer to the latest Data Migration Assistant User Guide .

## Backup
                        	 Database

The CAR and CDR Disaster Recovery Service (DRS) now integrates into the Unified Communications Manager DRS. The DRS includes the backup of the CAR database, pregenerated reports, and the CDR preserved flat files.

The CAR
                              		  Web Service and CAR Scheduler automatically stop before the backup and restore
                              		  process begin, and automatically restart after the backup and restore process
                              		  is complete.

The table
                              		  displays the features and components that the Disaster Recovery System can back
                              		  up and restore. For each feature that you choose, the system backs up all its
                              		  components automatically.

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

For
                              		  more detailed information, see the Administration Guide for Cisco Unified Communications
                                 			 Manager .

## CPU Utilization

Cisco has performed basic testing to measure CPU utilization
                              		  when CDRs and/or CMRs are enabled. The CPU utilization testing was measured on
                              		  subscribers and was not measured on the publishers. Your actual results can
                              		  vary because of the CDR Loader settings and the CDR Management settings for
                              		  external billing servers. Table 1 displays the results of these tests.

Be aware that these tests were performed with Unified Communications Manager Release 8.0(1).

CDRs and CMRs Enabled/Disabled

Average % Increase in Cisco Unified CM CPU
                                          					 Utilization

Average % Increase in Total CPU Utilization

% Increase in Cisco Unified CM CPU

% Increase in Total CPU

CDRs disabled, CMRs disabled

6.17

11.15

-

-

CDRs enabled, CMRs disabled

6.99

12.10

13.18

8.57

CDRs disabled, CMRs enabled

6.38

11.24

3.43

0.86

CDRs enabled, CMRs enabled

7.71

13.04

24.92

17.02

## Related Topics

Generate CDR Analysis and Reporting

Activate CAR

CAR System Scheduler

## Additional
                        	 Documentation

Cisco Unified Serviceability Administration Guide

Cisco
                                       				  Unified Real-Time Monitoring Tool Administration Guide

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Communications Manager Online Help

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

Data Migration Assistant User Guide

### Customers Also Viewed

- Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1) --- CDR Analysis and Reporting Tool

| Note | CAR does not handle iDivert calls (feature that diverts calls to a
                                    		  voice-messaging system) and treats them as normal calls. The part of the call
                                    		  after the iDivert feature gets activated may not get charged to the correct
                                    		  party. |
|---|---|

| Note | An option allows you to uncheck the "Load CDR Only" check box in the CAR System Scheduler window to
                                          			 allow CMR records to load. See Set Up CDR Load Schedule for additional information. |
|---|---|

| Note | If you upgrade your system to a new version of Unified Communications Manager , you must disable the CAR reports that generate automatically, so you conserve system resources during the upgrade process. |
|---|---|

| Note | The system does not provide email alerts to application users
                                          			 because no mail ID exists for an application user. |
|---|---|

| Version | Maximum Number of CDR Records | Maximum Size of Database | Maximum Aggregate Busy Hour Call Attempts (BHCA) |
|---|---|---|---|
| Unified Communications Manager | 2 million records | 6 GB | 10,000 |
| Cisco Unified Communications Manager Business Edition 5000 | 1 million records | 3 GB | 5,000 |

| Note | If you do not change the default value for charge base/block, the
                                          			 cost will always remain zero because the default base charge per block equals
                                          			 zero. |
|---|---|

| Note | If you do not want to increase call cost by voice quality, you can
                                          			 use the default values. The default multiplication factor specifies 1.00, so no
                                          			 increase in call cost for voice quality occurs. |
|---|---|

| Note | Refer to the "Configuring the Audit Log" chapter in the Cisco Unified Serviceability Administration Guide for information on how to configure the Audit Log. Refer to the "Working With Trace and Log Central" chapter in the Cisco Unified Real-Time Monitoring Tool Administration Guide for information on how to view the audit logs. |
|---|---|

| Note | CAR supports all Latin-1 language and Unicode language locales as Unified Communications Manager help specifies. Latin-1 languages include English and Western European languages. Unicode languages include Japanese and
                                          Chinese. |
|---|---|

| Note | For Unified Communications Manager , make sure that you have first installed the Cisco Unified Communications Manager Locale Installer on every server in the cluster. Installing the Locale Installer ensures that you have the latest translated
                                          text available for CAR. For more information about
                                          			 the Cisco Unified Communications Manager Locale Installer,
                                          			 see the Administration Guide for Cisco Unified Communications
                                             				Manager . |
|---|---|

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

| Note | Be aware that these tests were performed with Unified Communications Manager Release 8.0(1). |
|---|---|

| CDRs and CMRs Enabled/Disabled | Average % Increase in Cisco Unified CM CPU
                                          					 Utilization | Average % Increase in Total CPU Utilization | % Increase in Cisco Unified CM CPU | % Increase in Total CPU |
|---|---|---|---|---|
| CDRs disabled, CMRs disabled | 6.17 | 11.15 | - | - |
| CDRs enabled, CMRs disabled | 6.99 | 12.10 | 13.18 | 8.57 |
| CDRs disabled, CMRs enabled | 6.38 | 11.24 | 3.43 | 0.86 |
| CDRs enabled, CMRs enabled | 7.71 | 13.04 | 24.92 | 17.02 |