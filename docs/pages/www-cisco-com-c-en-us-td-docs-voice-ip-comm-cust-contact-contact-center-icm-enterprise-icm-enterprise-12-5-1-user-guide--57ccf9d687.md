---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--57ccf9d687
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting_user_guide-1251/ucce_b_cisco-unified-contact-center-enterprise-125_chapter_0101.html
retrieved_at: 2026-08-22T00:01:15.095661+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release12.5(1)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release12.5(1)

Updated: February 4, 2020

Chapter: Schedule a Report

## Chapter: Schedule a Report

# Schedule a Report

## Overview

You can automate the generation of reports on a regular and recurring basis by setting up a schedule. The Schedules entity
                              lets you run large dataset reports once to be sent to, and viewed by, many users.

Only users with Report Designer and System Configuration Administrator roles can access the Schedules entity. System Configuration
                              Administrators can perform all schedule related functions on any reports. They can view , edit, and run any scheduled report and can create a schedule for any report. Report designers can create a schedule only
                              for those reports that they created or for which they have View permissions.

Attention

You cannot schedule Live Data reports.

You can schedule reports to:

Run at predetermined times

Automatically email reports

Save reports to remote location

The schedules run based on the server time zone and hence on the Schedules page, the column Next Scheduled Run reflects the server time zone.

## Schedules Actions

Action

Description

Toolbar Actions

Search

Searches for a Schedule.

All

Lists all the schedules (Large, Disabled, Email, and SFTP).

Large Schedules

Lists all large schedules.

Disabled

Lists all disabled schedules.

Email

Lists all the schedules configured for email distribution.

SFTP

Lists all the schedules configured to be saved in a remote location.

Refresh

Refreshes the Schedules page.

New

Creates a new schedule. For more information, see Create a Schedule for a Report .

Ellipsis (…) Actions

Edit

Edits a schedule.

You can also click on the Schedule Name to edit the schedule details.

In the edit mode, you can click the icon next to the Schedule name to edit the Schedule properties; Name and Schedule Type.

Enable or Disable

Enables or disables a schedule.

Delete

## Create a Schedule for a Report

You cannot schedule Live Data reports.

Step 1

In the left navigation page, click Schedules .

Step 2

Click New .

Step 3

In the Create New Schedule dialog box, enter a name for the Scheduler, and select the Scheduler Type . The available Scheduler Types are:

Large Schedule

Visible only for System Configuration Administrator.

Use Large Schedules for large reports with over 8000 rows.

Large Schedules have an upper limit of 25000 rows.

Large Schedules support only the CSV file formats.

System Config Administrators can create a maximum of six Large Schedules. You can contact your administrator to increase or
                                                      decrease the number of Large Schedules.

You can limit Large Schedules to a frequency of once a day.

Important

When there are multiple Large Schedules, ensure not to schedule them simultaneously.

Regular Schedule

Step 4

Click Next .

Step 5

In the Report Scheduling tab, select the report to be scheduled, set the filter data,  and configure the schedule details.

Field

Description

Report

Report

Select the report to be scheduled.

Set Filter

Select this check box to enable the Filter Criteria button. Click the Filter Criteria button to set the filter criteria for the report.

For more information on setting filters for a report, see Report Filters .

If unchecked, the default filter is used.

Schedule

Start Date

Click the calendar icon to select the Start Date .

The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied.

End Date

Select an option for the End Date :

None —indicates no end date.

By —click the calendar icon to select the end date.

Recurrence

Specify the recurrence pattern for the scheduled report.

Schedules that reach the end date are purged after a 24-hour retention period.

Once —Specify the time of day for the single occurrence.

Daily —Specify a number for recurrence of days; for example, every four days.

Weekly —Specify the number of weeks and the days of the week that you want the scheduled report to be run.

Monthly —Select a day of the month and specify the number of months that you want the scheduled report to run.

Frequency

Specify the number of times the report must run on the scheduled days.

The maximum frequency with which you can schedule a report is once in every five minutes.

The maximum frequency with which you can run Large Schedule is once per day.

Step 6

Click Next .

Step 7

In the Destination Setting tab, set up a schedule to email the scheduled report and save the report CSV format in a remote location.

You can configure the email server in the Administration Console. Contact the administrator for assistance or for more information,
                                          see the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

Field

Description

Email

Enable the switch and enter the recipient email addresses.

Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field.

Select the view of the report that you want to email.

Only grid views can be scheduled.

Email Subject

Enter text for the subject line.

Email File Type

Select the type of file.

INLINE HTML —Sends the report in HTML format.

The historical report has an upper limit of 8000 rows.

The real-time report has an upper limit of 3000 rows.

XLS —Sends the report as a Microsoft Excel file attachment.

Scheduled reports sent in Excel format via email are delivered as ZIP files.

The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel.

The historical report has an upper limit of 8000 rows.

The real-time report has an upper limit of 3000 rows.

PDF —Sends the report as a PDF file attachment in either landscape or portrait orientation.

The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10.

The generated PDF attachments have the following limitations:

Uses standard font sizes. 10 pixels for the landscape orientation and 8 pixels for the portrait orientation. The PDF bypasses
                                                                  the font size that is set in the grid view editor to keep the font output printer-friendly.

PDF supports images only in the HTTP format.

Retains rows that fit on the page for the selected orientation. Columns that do not fit on the page are truncated.

Only 1000 rows are supported for a PDF file attachment. An email message is sent if the scheduled report exceeds 1000 rows.

Does not support word-wrap for columns. In case of larger text, you can customize the column width in the grid editor to avoid
                                                                  overlaps. As a result, the customization may reduce the number of columns that are shown in the PDF.

Remote Location

Protocol

Enable the switch and select SFTP to establish secure connection to the remote location.

Report View

Select the view of the report to be posted.

Host

Enter the IP address of the remote location.

Port

Enter a Port number for the SFTP. The default port number is 22.

Directory Path

Enter the location on the host to save your .csv file. Directory Path must be an absolute path.

User Name, Password

Enter a username and the corresponding password for the host. Maximum Password Length: 50 characters.

Test Connection

Click to test the connection.

Date Time format in a scheduled report of type CSV is: Day_of_week Month Date_of_Month HH:MM:SS SERVER_TIMEZONE YYYY. For
                                                            Example, Fri Oct 24 01:00:00 EDT 2014.

The time field in a scheduled report of type CSV is displayed in seconds only.

Scheduled Reports generated using Remote Location option does not
                                                      support formatted reports. To get formatted reports, use Email as
                                                      the Destination Setting .

Step 8

Click Save .

## Daylight Saving Time
                        	 and Scheduled Reports

Daylight saving time affects the scheduled reports in the following ways:

Reports that are scheduled to run daily during a particular time of the day are skipped for the day when the clock advances
                                    (for example, due to daylight saving). For example, for a report that is scheduled to run at 10:30 p.m. daily, if the clock
                                    advances by 1 hour then the report that is scheduled to run at 10:30 p.m. will be skipped for that day.

Reports that are scheduled to run only once, are updated with a new schedule time with some offset if it falls in the period
                                    that advances. For example, if the clock advances by one hour for a report scheduled to run once at 10:30 p.m., then the schedule
                                    report run time updates to 11:30 p.m.

## Reports and Time
                        	 Zones

You can configure four time zones in Unified Intelligence Center: Server, Data Source, Report, and User.

### Server

The server time zone is defined during installation while running the installation wizard and it does not affect reports.
                              The server administrator can view and change the server time zone using these CLI commands: show timezone config and set timezone zone . For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html

### Data
                              		  Source

The data source
                              		  time zone is defined when the data source is configured. It is the time zone of
                              		  the database.

### Report

The report time
                              		  zone is defined in the report filter.

If your call center
                              		  spans several time zones and you intend to compare reports, run historical
                              		  reports using the absolute date range and a specific time period.

### User

The user's time
                              		  zone is set on the User Profile.

For example, when a user in New York is asked to review a report that was run by a colleague in the China office, the user
                              accesses the User Profile page to change the time zone to match the colleague's, and then runs the report using the same absolute
                              date range.

### Time Zone Considerations

The system treats the time-specific data that the user enters as local to the user's time zone and then converts this time
                              to the data source time zone when the filter query is formed.

The system treats
                              		  the time-specific data that it fetches from a data source as local to the data
                              		  source and then converts this time to the user time zone before displaying the
                              		  date and time in the report data.

If the user time zone or data source time zone is not configured, the system uses the time zone of the Unified Intelligence
                              Center server. The system performs these conversions only after the time zone normalization at data source level has occurred.

The schedule for Weekly and Monthly reports is based on the data source time zone, not the server time zone. That is, the
                                          week and month boundaries are midnight, in the time zone of the database, of the week or month beginning and end days.

When you generate historical reports, the aggregation of data (Daily/Weekly/Monthly/Yearly) is based on AW Datasource Timezone.

Consider the
                              		  following example, in which the user enters the date and time value in the
                              		  filter. Depending on the time zone setting, the system converts the time zones
                              		  in the filter query as shown below:

filter value = 1/1/2010
                                 			 12:00:00 AM

User Time Zone

User Time Zone

Data Source Time Zone

Data Source Time Zone

When set (+11 GMT)

When not set (Subtract
                                             						  Cisco Unified Intelligence Center server time zone)

When set (+2 GMT)

When not set (Add Cisco
                                             						  Unified Intelligence Center server time zone)

Thursday, December 31, 2009
                                             						  3:00:00 PM EET

Original Time – User time zone offset (+11 GMT) + Data source time zone (+2
                                          						GMT)

To
                                          						Original Time, -9 ( -11 +2) hours added

Thursday, December 31, 2009
                                             						  8:30:00 PM EET

Original Time – Cisco Unified Intelligence server time zone (+5.30 GMT) + Data
                                          						source time zone offset ( +2 GMT)

From
                                          						Original Time, 3.30 (– 5.30 +2) hours subtracted

Thursday, December 31, 2009
                                             						  3:00:00 PM EET

Original Time – User time zone offset (+11 GMT) + Data source time zone (+2
                                          						GMT)

To
                                          						Original Time, -9 ( -11 +2) hours added

Thursday, December 31, 2009
                                             						  6:30:00 PM IST

Original Time – User time zone offset (+11 GMT) + Cisco Unified Intelligence
                                          						server time zone (+5.30 GMT)

From
                                          						Original Time, 5.30 ( –11 +5.30) hours subtracted

Thursday, December 31, 2009
                                             						  6:30:00 PM IST

Original Time – User time zone offset (+11 GMT) + Cisco Unified Intelligence
                                          						server time zone (+5.30 GMT)

From
                                          						Original Time, 5.30 ( –11 +5.30) hours subtracted

Friday, January 1, 2010
                                             						  12:00:00 AM IST

To
                                          						Original Time, 0 (– 5.30 +5.30) hours added

Thursday, December 31, 2009
                                             						  8:30:00 PM EET

Original Time – Cisco Unified Intelligence server time zone (+5.30 GMT) + Data
                                          						source time zone offset ( +2 GMT)

From
                                          						Original Time, 3.30 (–5.30 +2) hours subtracted

Friday, January 1, 2010
                                             						  12:00:00 AM IST

To
                                          						Original Time, 0 (– 5.30 +5.30) hours added

The following
                              		  example shows a database with date and time values. Depending on your time zone
                              		  setting, the system converts and displays the time zones in the report data as
                              		  shown below:

Database value = 1/1/2010 12:00:00
                                 			 AM

Data Source Time Zone

Data Source Time Zone

User Time Zone

User Time Zone

When set (+11 GMT)

When not set (Subtract
                                             						  Unified Intelligence Center server time zone)

When set (+2 GMT)

When not set (Add Unified
                                             						  Intelligence Center server time zone)

Thursday, December 31, 2009
                                             						  3:00:00 PM EET

Original Time – Data source time zone offset (+11 GMT) + User time zone (+2
                                          						GMT)

To
                                          						Original Time, -9 ( -11 +2) hours added

Thursday, December 31, 2009
                                             						  8:30:00 PM EET

Original Time – Unified Intelligence Center server time zone (+5.30 GMT) + User
                                          						time zone offset ( +2 GMT)

From
                                          						Original Time, 3.30 (– 5.30 +2) hours subtracted

Thursday, December 31, 2009
                                             						  3:00:00 PM EET

Original
                                          						Time – Data source time zone offset (+11 GMT) + User time zone (+2 GMT)

To
                                          						Original Time, -9 ( -11 +2) hours added

Thursday, December 31, 2009
                                             						  6:30:00 PM IST

Original
                                          						Time – Data source time zone offset (+11 GMT) + Unified Intelligence Center
                                          						server time zone (+5.30 GMT)

From
                                          						Original Time, 5.30 ( –11 +5.30) hours subtracted

Thursday, December 31, 2009
                                             						  6:30:00 PM IST

Original Time – Data source time zone offset (+11 GMT) + Unified Intelligence
                                          						Center server time zone (+5.30 GMT)

From
                                          						Original Time, 5.30 ( –11 +5.30) hours subtracted

Friday, January 1, 2010
                                             						  12:00:00 AM IST

To
                                          						Original Time, 0 (– 5.30 +5.30) hours added

Thursday, December 31, 2009
                                             						  8:30:00 PM EET

Original
                                          						Time – Unified Intelligence Center server time zone(+5.30 GMT) + User time zone
                                          						offset ( +2 GMT)

From
                                          						Original Time, 3.30 (–5.30 +2) hours subtracted

Friday, January 1, 2010
                                             						  12:00:00 AM IST

To
                                          						Original Time, 0 (– 5.30 +5.30) hours added

| Attention | You cannot schedule Live Data reports. |
|---|---|

| Note | The schedules run based on the server time zone and hence on the Schedules page, the column Next Scheduled Run reflects the server time zone. |
|---|---|

| Action | Description |
|---|---|
| Toolbar Actions |
| Search | Searches for a Schedule. |
| All | Lists all the schedules (Large, Disabled, Email, and SFTP). |
| Large Schedules | Lists all large schedules. |
| Disabled | Lists all disabled schedules. |
| Email | Lists all the schedules configured for email distribution. |
| SFTP | Lists all the schedules configured to be saved in a remote location. |
| Refresh | Refreshes the Schedules page. |
| New | Creates a new schedule. For more information, see Create a Schedule for a Report . |
| Ellipsis (…) Actions |
| Edit | Edits a schedule. You can also click on the Schedule Name to edit the schedule details. In the edit mode, you can click the icon next to the Schedule name to edit the Schedule properties; Name and Schedule Type. |
| Enable or Disable | Enables or disables a schedule. |
| Delete | Deletes a schedule. |

| Note | You cannot schedule Live Data reports. |
|---|---|

| Step 1 | In the left navigation page, click Schedules . |
|---|---|
| Step 2 | Click New . |
| Step 3 | In the Create New Schedule dialog box, enter a name for the Scheduler, and select the Scheduler Type . The available Scheduler Types are: Large Schedule Visible only for System Configuration Administrator. Use Large Schedules for large reports with over 8000 rows. Note Large Schedules have an upper limit of 25000 rows. Large Schedules support only the CSV file formats. System Config Administrators can create a maximum of six Large Schedules. You can contact your administrator to increase or
                                                      decrease the number of Large Schedules. You can limit Large Schedules to a frequency of once a day. Important When there are multiple Large Schedules, ensure not to schedule them simultaneously. Regular Schedule | Note | Large Schedules have an upper limit of 25000 rows. | Important | When there are multiple Large Schedules, ensure not to schedule them simultaneously. |
| Note | Large Schedules have an upper limit of 25000 rows. |
| Important | When there are multiple Large Schedules, ensure not to schedule them simultaneously. |
| Step 4 | Click Next . |
| Step 5 | In the Report Scheduling tab, select the report to be scheduled, set the filter data,  and configure the schedule details. Field Description Report Report Select the report to be scheduled. Set Filter Select this check box to enable the Filter Criteria button. Click the Filter Criteria button to set the filter criteria for the report. For more information on setting filters for a report, see Report Filters . Note If unchecked, the default filter is used. Schedule Start Date Click the calendar icon to select the Start Date . Note The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. End Date Select an option for the End Date : None —indicates no end date. By —click the calendar icon to select the end date. Recurrence Specify the recurrence pattern for the scheduled report. Note Schedules that reach the end date are purged after a 24-hour retention period. Once —Specify the time of day for the single occurrence. Daily —Specify a number for recurrence of days; for example, every four days. Weekly —Specify the number of weeks and the days of the week that you want the scheduled report to be run. Monthly —Select a day of the month and specify the number of months that you want the scheduled report to run. Note Use Last to specify the last day of the month. Frequency Specify the number of times the report must run on the scheduled days. Note The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. | Field | Description | Report | Report | Select the report to be scheduled. | Set Filter | Select this check box to enable the Filter Criteria button. Click the Filter Criteria button to set the filter criteria for the report. For more information on setting filters for a report, see Report Filters . Note If unchecked, the default filter is used. | Note | If unchecked, the default filter is used. | Schedule | Start Date | Click the calendar icon to select the Start Date . Note The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. | Note | The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. | End Date | Select an option for the End Date : None —indicates no end date. By —click the calendar icon to select the end date. | Recurrence | Specify the recurrence pattern for the scheduled report. Note Schedules that reach the end date are purged after a 24-hour retention period. Once —Specify the time of day for the single occurrence. Daily —Specify a number for recurrence of days; for example, every four days. Weekly —Specify the number of weeks and the days of the week that you want the scheduled report to be run. Monthly —Select a day of the month and specify the number of months that you want the scheduled report to run. Note Use Last to specify the last day of the month. | Note | Schedules that reach the end date are purged after a 24-hour retention period. | Note | Use Last to specify the last day of the month. | Frequency | Specify the number of times the report must run on the scheduled days. Note The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. | Note | The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. |
| Field | Description |
| Report |
| Report | Select the report to be scheduled. |
| Set Filter | Select this check box to enable the Filter Criteria button. Click the Filter Criteria button to set the filter criteria for the report. For more information on setting filters for a report, see Report Filters . Note If unchecked, the default filter is used. | Note | If unchecked, the default filter is used. |
| Note | If unchecked, the default filter is used. |
| Schedule |
| Start Date | Click the calendar icon to select the Start Date . Note The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. | Note | The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. |
| Note | The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. |
| End Date | Select an option for the End Date : None —indicates no end date. By —click the calendar icon to select the end date. |
| Recurrence | Specify the recurrence pattern for the scheduled report. Note Schedules that reach the end date are purged after a 24-hour retention period. Once —Specify the time of day for the single occurrence. Daily —Specify a number for recurrence of days; for example, every four days. Weekly —Specify the number of weeks and the days of the week that you want the scheduled report to be run. Monthly —Select a day of the month and specify the number of months that you want the scheduled report to run. Note Use Last to specify the last day of the month. | Note | Schedules that reach the end date are purged after a 24-hour retention period. | Note | Use Last to specify the last day of the month. |
| Note | Schedules that reach the end date are purged after a 24-hour retention period. |
| Note | Use Last to specify the last day of the month. |
| Frequency | Specify the number of times the report must run on the scheduled days. Note The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. | Note | The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. |
| Note | The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. |
| Step 6 | Click Next . |
| Step 7 | In the Destination Setting tab, set up a schedule to email the scheduled report and save the report CSV format in a remote location. You can configure the email server in the Administration Console. Contact the administrator for assistance or for more information,
                                          see the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html . Field Description Email Email Distribution Enable the switch and enter the recipient email addresses. Note Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. Email View Select the view of the report that you want to email. Note Only grid views can be scheduled. Email Subject Enter text for the subject line. Email File Type Select the type of file. INLINE HTML —Sends the report in HTML format. The historical report has an upper limit of 8000 rows. The real-time report has an upper limit of 3000 rows. XLS —Sends the report as a Microsoft Excel file attachment. Note Scheduled reports sent in Excel format via email are delivered as ZIP files. Note The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. The historical report has an upper limit of 8000 rows. The real-time report has an upper limit of 3000 rows. PDF —Sends the report as a PDF file attachment in either landscape or portrait orientation. Note The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. The generated PDF attachments have the following limitations: Uses standard font sizes. 10 pixels for the landscape orientation and 8 pixels for the portrait orientation. The PDF bypasses
                                                                  the font size that is set in the grid view editor to keep the font output printer-friendly. Note PDF supports images only in the HTTP format. Retains rows that fit on the page for the selected orientation. Columns that do not fit on the page are truncated. Only 1000 rows are supported for a PDF file attachment. An email message is sent if the scheduled report exceeds 1000 rows. Does not support word-wrap for columns. In case of larger text, you can customize the column width in the grid editor to avoid
                                                                  overlaps. As a result, the customization may reduce the number of columns that are shown in the PDF. Remote Location Protocol Enable the switch and select SFTP to establish secure connection to the remote location. Report View Select the view of the report to be posted. Host Enter the IP address of the remote location. Port Enter a Port number for the SFTP. The default port number is 22. Directory Path Enter the location on the host to save your .csv file. Directory Path must be an absolute path. User Name, Password Enter a username and the corresponding password for the host. Maximum Password Length: 50 characters. Test Connection Click to test the connection. Note Date Time format in a scheduled report of type CSV is: Day_of_week Month Date_of_Month HH:MM:SS SERVER_TIMEZONE YYYY. For
                                                            Example, Fri Oct 24 01:00:00 EDT 2014. The time field in a scheduled report of type CSV is displayed in seconds only. Note Scheduled Reports generated using Remote Location option does not
                                                      support formatted reports. To get formatted reports, use Email as
                                                      the Destination Setting . Note When you edit a scheduled report and click Save , the scheduler runs and emails the scheduled report to all the recipients that are configured in the Email Distribution field. | Field | Description | Email | Email Distribution | Enable the switch and enter the recipient email addresses. Note Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. | Note | Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. | Email View | Select the view of the report that you want to email. Note Only grid views can be scheduled. | Note | Only grid views can be scheduled. | Email Subject | Enter text for the subject line. | Email File Type | Select the type of file. INLINE HTML —Sends the report in HTML format. The historical report has an upper limit of 8000 rows. The real-time report has an upper limit of 3000 rows. XLS —Sends the report as a Microsoft Excel file attachment. Note Scheduled reports sent in Excel format via email are delivered as ZIP files. Note The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. The historical report has an upper limit of 8000 rows. The real-time report has an upper limit of 3000 rows. PDF —Sends the report as a PDF file attachment in either landscape or portrait orientation. Note The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. The generated PDF attachments have the following limitations: Uses standard font sizes. 10 pixels for the landscape orientation and 8 pixels for the portrait orientation. The PDF bypasses
                                                                  the font size that is set in the grid view editor to keep the font output printer-friendly. Note PDF supports images only in the HTTP format. Retains rows that fit on the page for the selected orientation. Columns that do not fit on the page are truncated. Only 1000 rows are supported for a PDF file attachment. An email message is sent if the scheduled report exceeds 1000 rows. Does not support word-wrap for columns. In case of larger text, you can customize the column width in the grid editor to avoid
                                                                  overlaps. As a result, the customization may reduce the number of columns that are shown in the PDF. | Note | Scheduled reports sent in Excel format via email are delivered as ZIP files. | Note | The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. | Note | The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. | Note | PDF supports images only in the HTTP format. | Remote Location | Protocol | Enable the switch and select SFTP to establish secure connection to the remote location. | Report View | Select the view of the report to be posted. | Host | Enter the IP address of the remote location. | Port | Enter a Port number for the SFTP. The default port number is 22. | Directory Path | Enter the location on the host to save your .csv file. Directory Path must be an absolute path. | User Name, Password | Enter a username and the corresponding password for the host. Maximum Password Length: 50 characters. | Test Connection | Click to test the connection. | Note | Date Time format in a scheduled report of type CSV is: Day_of_week Month Date_of_Month HH:MM:SS SERVER_TIMEZONE YYYY. For
                                                            Example, Fri Oct 24 01:00:00 EDT 2014. The time field in a scheduled report of type CSV is displayed in seconds only. | Note | Scheduled Reports generated using Remote Location option does not
                                                      support formatted reports. To get formatted reports, use Email as
                                                      the Destination Setting . | Note | When you edit a scheduled report and click Save , the scheduler runs and emails the scheduled report to all the recipients that are configured in the Email Distribution field. |
| Field | Description |
| Email |
| Email Distribution | Enable the switch and enter the recipient email addresses. Note Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. | Note | Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. |
| Note | Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. |
| Email View | Select the view of the report that you want to email. Note Only grid views can be scheduled. | Note | Only grid views can be scheduled. |
| Note | Only grid views can be scheduled. |
| Email Subject | Enter text for the subject line. |
| Email File Type | Select the type of file. INLINE HTML —Sends the report in HTML format. The historical report has an upper limit of 8000 rows. The real-time report has an upper limit of 3000 rows. XLS —Sends the report as a Microsoft Excel file attachment. Note Scheduled reports sent in Excel format via email are delivered as ZIP files. Note The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. The historical report has an upper limit of 8000 rows. The real-time report has an upper limit of 3000 rows. PDF —Sends the report as a PDF file attachment in either landscape or portrait orientation. Note The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. The generated PDF attachments have the following limitations: Uses standard font sizes. 10 pixels for the landscape orientation and 8 pixels for the portrait orientation. The PDF bypasses
                                                                  the font size that is set in the grid view editor to keep the font output printer-friendly. Note PDF supports images only in the HTTP format. Retains rows that fit on the page for the selected orientation. Columns that do not fit on the page are truncated. Only 1000 rows are supported for a PDF file attachment. An email message is sent if the scheduled report exceeds 1000 rows. Does not support word-wrap for columns. In case of larger text, you can customize the column width in the grid editor to avoid
                                                                  overlaps. As a result, the customization may reduce the number of columns that are shown in the PDF. | Note | Scheduled reports sent in Excel format via email are delivered as ZIP files. | Note | The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. | Note | The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. | Note | PDF supports images only in the HTTP format. |
| Note | Scheduled reports sent in Excel format via email are delivered as ZIP files. |
| Note | The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. |
| Note | The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. |
| Note | PDF supports images only in the HTTP format. |
| Remote Location |
| Protocol | Enable the switch and select SFTP to establish secure connection to the remote location. |
| Report View | Select the view of the report to be posted. |
| Host | Enter the IP address of the remote location. |
| Port | Enter a Port number for the SFTP. The default port number is 22. |
| Directory Path | Enter the location on the host to save your .csv file. Directory Path must be an absolute path. |
| User Name, Password | Enter a username and the corresponding password for the host. Maximum Password Length: 50 characters. |
| Test Connection | Click to test the connection. |
| Note | Date Time format in a scheduled report of type CSV is: Day_of_week Month Date_of_Month HH:MM:SS SERVER_TIMEZONE YYYY. For
                                                            Example, Fri Oct 24 01:00:00 EDT 2014. The time field in a scheduled report of type CSV is displayed in seconds only. |
| Note | Scheduled Reports generated using Remote Location option does not
                                                      support formatted reports. To get formatted reports, use Email as
                                                      the Destination Setting . |
| Note | When you edit a scheduled report and click Save , the scheduler runs and emails the scheduled report to all the recipients that are configured in the Email Distribution field. |
| Step 8 | Click Save . |

| Note | Large Schedules have an upper limit of 25000 rows. |
|---|---|

| Important | When there are multiple Large Schedules, ensure not to schedule them simultaneously. |
|---|---|

| Field | Description |
|---|---|
| Report |
| Report | Select the report to be scheduled. |
| Set Filter | Select this check box to enable the Filter Criteria button. Click the Filter Criteria button to set the filter criteria for the report. For more information on setting filters for a report, see Report Filters . Note If unchecked, the default filter is used. | Note | If unchecked, the default filter is used. |
| Note | If unchecked, the default filter is used. |
| Schedule |
| Start Date | Click the calendar icon to select the Start Date . Note The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. | Note | The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. |
| Note | The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. |
| End Date | Select an option for the End Date : None —indicates no end date. By —click the calendar icon to select the end date. |
| Recurrence | Specify the recurrence pattern for the scheduled report. Note Schedules that reach the end date are purged after a 24-hour retention period. Once —Specify the time of day for the single occurrence. Daily —Specify a number for recurrence of days; for example, every four days. Weekly —Specify the number of weeks and the days of the week that you want the scheduled report to be run. Monthly —Select a day of the month and specify the number of months that you want the scheduled report to run. Note Use Last to specify the last day of the month. | Note | Schedules that reach the end date are purged after a 24-hour retention period. | Note | Use Last to specify the last day of the month. |
| Note | Schedules that reach the end date are purged after a 24-hour retention period. |
| Note | Use Last to specify the last day of the month. |
| Frequency | Specify the number of times the report must run on the scheduled days. Note The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. | Note | The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. |
| Note | The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. |

| Note | If unchecked, the default filter is used. |
|---|---|

| Note | The Start Date uses the user's time zone settings. If no time zone is set for the user, the reporting server time zone is
                                                                  applied. |
|---|---|

| Note | Schedules that reach the end date are purged after a 24-hour retention period. |
|---|---|

| Note | Use Last to specify the last day of the month. |
|---|---|

| Note | The maximum frequency with which you can schedule a report is once in every five minutes. The maximum frequency with which you can run Large Schedule is once per day. |
|---|---|

| Field | Description |
|---|---|
| Email |
| Email Distribution | Enable the switch and enter the recipient email addresses. Note Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. | Note | Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. |
| Note | Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. |
| Email View | Select the view of the report that you want to email. Note Only grid views can be scheduled. | Note | Only grid views can be scheduled. |
| Note | Only grid views can be scheduled. |
| Email Subject | Enter text for the subject line. |
| Email File Type | Select the type of file. INLINE HTML —Sends the report in HTML format. The historical report has an upper limit of 8000 rows. The real-time report has an upper limit of 3000 rows. XLS —Sends the report as a Microsoft Excel file attachment. Note Scheduled reports sent in Excel format via email are delivered as ZIP files. Note The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. The historical report has an upper limit of 8000 rows. The real-time report has an upper limit of 3000 rows. PDF —Sends the report as a PDF file attachment in either landscape or portrait orientation. Note The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. The generated PDF attachments have the following limitations: Uses standard font sizes. 10 pixels for the landscape orientation and 8 pixels for the portrait orientation. The PDF bypasses
                                                                  the font size that is set in the grid view editor to keep the font output printer-friendly. Note PDF supports images only in the HTTP format. Retains rows that fit on the page for the selected orientation. Columns that do not fit on the page are truncated. Only 1000 rows are supported for a PDF file attachment. An email message is sent if the scheduled report exceeds 1000 rows. Does not support word-wrap for columns. In case of larger text, you can customize the column width in the grid editor to avoid
                                                                  overlaps. As a result, the customization may reduce the number of columns that are shown in the PDF. | Note | Scheduled reports sent in Excel format via email are delivered as ZIP files. | Note | The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. | Note | The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. | Note | PDF supports images only in the HTTP format. |
| Note | Scheduled reports sent in Excel format via email are delivered as ZIP files. |
| Note | The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. |
| Note | The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. |
| Note | PDF supports images only in the HTTP format. |
| Remote Location |
| Protocol | Enable the switch and select SFTP to establish secure connection to the remote location. |
| Report View | Select the view of the report to be posted. |
| Host | Enter the IP address of the remote location. |
| Port | Enter a Port number for the SFTP. The default port number is 22. |
| Directory Path | Enter the location on the host to save your .csv file. Directory Path must be an absolute path. |
| User Name, Password | Enter a username and the corresponding password for the host. Maximum Password Length: 50 characters. |
| Test Connection | Click to test the connection. |

| Note | Email page validation occurs when the email address is entered in the Email Distribution field. No validation is performed if there is no email ID entered in the Email Distribution field. |
|---|---|

| Note | Only grid views can be scheduled. |
|---|---|

| Note | Scheduled reports sent in Excel format via email are delivered as ZIP files. |
|---|---|

| Note | The custom formatting of DECIMAL data type is
                                                                        not applied for reports exported in excel. |
|---|---|

| Note | The maximum number of PDF reports that you can schedule to be sent by email at a given time is 10. |
|---|---|

| Note | PDF supports images only in the HTTP format. |
|---|---|

| Note | Date Time format in a scheduled report of type CSV is: Day_of_week Month Date_of_Month HH:MM:SS SERVER_TIMEZONE YYYY. For
                                                            Example, Fri Oct 24 01:00:00 EDT 2014. The time field in a scheduled report of type CSV is displayed in seconds only. |
|---|---|

| Note | Scheduled Reports generated using Remote Location option does not
                                                      support formatted reports. To get formatted reports, use Email as
                                                      the Destination Setting . |
|---|---|

| Note | When you edit a scheduled report and click Save , the scheduler runs and emails the scheduled report to all the recipients that are configured in the Email Distribution field. |
|---|---|

| Note | Scheduler relies on the Refresh Rate parameter in the Report Definition. You can configure the Refresh Rate parameter lower
                                       than the Scheduler Frequency. |
|---|---|

| Note | The schedule for Weekly and Monthly reports is based on the data source time zone, not the server time zone. That is, the
                                          week and month boundaries are midnight, in the time zone of the database, of the week or month beginning and end days. When you generate historical reports, the aggregation of data (Daily/Weekly/Monthly/Yearly) is based on AW Datasource Timezone. |
|---|---|

| User Time Zone | User Time Zone | Data Source Time Zone | Data Source Time Zone |
|---|---|---|---|
| When set (+11 GMT) | When not set (Subtract
                                             						  Cisco Unified Intelligence Center server time zone) | When set (+2 GMT) | When not set (Add Cisco
                                             						  Unified Intelligence Center server time zone) |
| Thursday, December 31, 2009
                                             						  3:00:00 PM EET Original Time – User time zone offset (+11 GMT) + Data source time zone (+2
                                          						GMT) To
                                          						Original Time, -9 ( -11 +2) hours added | Thursday, December 31, 2009
                                             						  8:30:00 PM EET Original Time – Cisco Unified Intelligence server time zone (+5.30 GMT) + Data
                                          						source time zone offset ( +2 GMT) From
                                          						Original Time, 3.30 (– 5.30 +2) hours subtracted | Thursday, December 31, 2009
                                             						  3:00:00 PM EET Original Time – User time zone offset (+11 GMT) + Data source time zone (+2
                                          						GMT) To
                                          						Original Time, -9 ( -11 +2) hours added | Thursday, December 31, 2009
                                             						  6:30:00 PM IST Original Time – User time zone offset (+11 GMT) + Cisco Unified Intelligence
                                          						server time zone (+5.30 GMT) From
                                          						Original Time, 5.30 ( –11 +5.30) hours subtracted |
| Thursday, December 31, 2009
                                             						  6:30:00 PM IST Original Time – User time zone offset (+11 GMT) + Cisco Unified Intelligence
                                          						server time zone (+5.30 GMT) From
                                          						Original Time, 5.30 ( –11 +5.30) hours subtracted | Friday, January 1, 2010
                                             						  12:00:00 AM IST To
                                          						Original Time, 0 (– 5.30 +5.30) hours added | Thursday, December 31, 2009
                                             						  8:30:00 PM EET Original Time – Cisco Unified Intelligence server time zone (+5.30 GMT) + Data
                                          						source time zone offset ( +2 GMT) From
                                          						Original Time, 3.30 (–5.30 +2) hours subtracted | Friday, January 1, 2010
                                             						  12:00:00 AM IST To
                                          						Original Time, 0 (– 5.30 +5.30) hours added |

| Data Source Time Zone | Data Source Time Zone | User Time Zone | User Time Zone |
|---|---|---|---|
| When set (+11 GMT) | When not set (Subtract
                                             						  Unified Intelligence Center server time zone) | When set (+2 GMT) | When not set (Add Unified
                                             						  Intelligence Center server time zone) |
| Thursday, December 31, 2009
                                             						  3:00:00 PM EET Original Time – Data source time zone offset (+11 GMT) + User time zone (+2
                                          						GMT) To
                                          						Original Time, -9 ( -11 +2) hours added | Thursday, December 31, 2009
                                             						  8:30:00 PM EET Original Time – Unified Intelligence Center server time zone (+5.30 GMT) + User
                                          						time zone offset ( +2 GMT) From
                                          						Original Time, 3.30 (– 5.30 +2) hours subtracted | Thursday, December 31, 2009
                                             						  3:00:00 PM EET Original
                                          						Time – Data source time zone offset (+11 GMT) + User time zone (+2 GMT) To
                                          						Original Time, -9 ( -11 +2) hours added | Thursday, December 31, 2009
                                             						  6:30:00 PM IST Original
                                          						Time – Data source time zone offset (+11 GMT) + Unified Intelligence Center
                                          						server time zone (+5.30 GMT) From
                                          						Original Time, 5.30 ( –11 +5.30) hours subtracted |
| Thursday, December 31, 2009
                                             						  6:30:00 PM IST Original Time – Data source time zone offset (+11 GMT) + Unified Intelligence
                                          						Center server time zone (+5.30 GMT) From
                                          						Original Time, 5.30 ( –11 +5.30) hours subtracted | Friday, January 1, 2010
                                             						  12:00:00 AM IST To
                                          						Original Time, 0 (– 5.30 +5.30) hours added | Thursday, December 31, 2009
                                             						  8:30:00 PM EET Original
                                          						Time – Unified Intelligence Center server time zone(+5.30 GMT) + User time zone
                                          						offset ( +2 GMT) From
                                          						Original Time, 3.30 (–5.30 +2) hours subtracted | Friday, January 1, 2010
                                             						  12:00:00 AM IST To
                                          						Original Time, 0 (– 5.30 +5.30) hours added |