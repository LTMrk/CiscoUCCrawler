---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--4f9ed1f50c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_010101.html
retrieved_at: 2026-08-21T01:36:50.290993+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Conference Bridge Device Reports

## Chapter: Conference Bridge Device Reports

# Conference Bridge Device Reports

CAR provides reporting capabilities for three levels of users:
                        		administrators, managers, and individual users. Only CAR administrators
                        		generate the conference bridge device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, and gateways.

This chapter contains the following topics:

## Generate Conference Call Details

Only CAR administrators generate the Conference Call Details
                              		  report. The Conference Call Details report allows you to generate and view
                              		  details about conference calls.

This section describes how to generate, view, or mail a
                              		  Conference Call Details report.

Choose Device
                                                					 Reports > Conference Bridge > Call
                                                					 Details .

The Conference Call Details window displays.

In the Report Type drop-down menu, choose either Summary or Detail .

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 7 or use the default setting, Generate New Report, and go to Step 4 .

In Select Conference Types, check the check box of the conference
                                       			 type that you want to include in the report as described in the following
                                       			 table.

Parameter

Description

Ad-Hoc

Ad hoc conferences allow the conference
                                                      						  controller to let only certain participants into the conference.

Meet-Me

Meet-me conferences allow users to dial in to a
                                                      						  conference.

If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see conference call details.

Ensure the date and time range does not exceed one month.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Generate Conference Bridge Utilization Reports

Only CAR administrators generate the Conference Bridge
                              		  Utilization report. The report provides an estimate of the utilization
                              		  percentage of the conference bridges (cumulative utilization of all the
                              		  conference bridges that are selected for OnDemand reports) for the period and
                              		  not the exact utilization. For example, the system calculates the utilization
                              		  of a conference bridge between 11hrs and 12hrs as the ((Sum of duration of the
                              		  calls that used the conference bridge in that hour) / (Number of days between
                              		  the fromDate and toDate selected * Maximum number of streams in the conference
                              		  bridge * Maximum number of duration in seconds in an hour) * 100)). The value
                              		  that is calculated will display in the report as the utilization for the time
                              		  between 11hrs and 12hrs. You can examine the usage based on each hour of a day
                              		  or on a specified number of days for each week or month.

You can either view reports that the system automatically
                              		  generates or generate new reports. Only CAR administrators can schedule reports
                              		  for automatic generation. See CAR System Scheduler ,
                              		  for more information.

This section describes how to generate, view, or mail
                              		  Conference Bridge Utilization reports for each conference bridge type.

Choose Device
                                                					 Reports > Conference
                                                					 Bridge > Utilization .

The Conference Bridge Utilization window displays.

In the Generate Report field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 6 .

Day of Week

Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 6 .

Day of Month

Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 6 .

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 8 or use the default, Generate New Report, and go to Step 4 .

From the Conference Bridge Types column in the left pane, choose
                                       			 the conference bridge type(s) that you want to include in the utilization
                                       			 report.

The conference bridges of the particular conference bridge type
                                          				that you chose display in the List of Devices box.

For this report, choose a maximum of five conference bridges.

When you have chosen all the conference bridges that you want to
                                       			 include in the report, click the down arrow to add them to the Selected Devices
                                       			 box.

If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information.

Ensure the date and time range does not exceed one month.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure described in the Mail Reports .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Step 1 | Choose Device
                                                					 Reports > Conference Bridge > Call
                                                					 Details . The Conference Call Details window displays. |
|---|---|
| Step 2 | In the Report Type drop-down menu, choose either Summary or Detail . |
| Step 3 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 7 or use the default setting, Generate New Report, and go to Step 4 . |
| Step 4 | In Select Conference Types, check the check box of the conference
                                       			 type that you want to include in the report as described in the following
                                       			 table. Table 1. Conference Calls Detail Fields Parameter Description Ad-Hoc Ad hoc conferences allow the conference
                                                      						  controller to let only certain participants into the conference. Meet-Me Meet-me conferences allow users to dial in to a
                                                      						  conference. | Parameter | Description | Ad-Hoc | Ad hoc conferences allow the conference
                                                      						  controller to let only certain participants into the conference. | Meet-Me | Meet-me conferences allow users to dial in to a
                                                      						  conference. |
| Parameter | Description |
| Ad-Hoc | Ad hoc conferences allow the conference
                                                      						  controller to let only certain participants into the conference. |
| Meet-Me | Meet-me conferences allow users to dial in to a
                                                      						  conference. |
| Step 5 | If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see conference call details. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 6 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 7 | Click the View Report button. The report displays . |
| Step 8 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Ad-Hoc | Ad hoc conferences allow the conference
                                                      						  controller to let only certain participants into the conference. |
| Meet-Me | Meet-me conferences allow users to dial in to a
                                                      						  conference. |

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device
                                                					 Reports > Conference
                                                					 Bridge > Utilization . The Conference Bridge Utilization window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the
                                       			 following table. Table 2. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 6 . Day of Week Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 6 . Day of Month Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 6 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 6 . | Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 6 . | Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 6 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 6 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 6 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 6 . |
| Step 3 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 8 or use the default, Generate New Report, and go to Step 4 . |
| Step 4 | From the Conference Bridge Types column in the left pane, choose
                                       			 the conference bridge type(s) that you want to include in the utilization
                                       			 report. The conference bridges of the particular conference bridge type
                                          				that you chose display in the List of Devices box. Note For this report, choose a maximum of five conference bridges. | Note | For this report, choose a maximum of five conference bridges. |
| Note | For this report, choose a maximum of five conference bridges. |
| Step 5 | When you have chosen all the conference bridges that you want to
                                       			 include in the report, click the down arrow to add them to the Selected Devices
                                       			 box. |
| Step 6 | If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 7 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 8 | Click the View Report button. The report displays . |
| Step 9 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 6 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 6 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 6 . |

| Note | For this report, choose a maximum of five conference bridges. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|