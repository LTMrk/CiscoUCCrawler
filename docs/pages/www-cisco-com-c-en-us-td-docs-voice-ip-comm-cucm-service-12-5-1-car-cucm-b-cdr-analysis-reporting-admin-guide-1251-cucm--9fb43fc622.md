---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--9fb43fc622
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_010111.html
retrieved_at: 2026-08-21T01:36:59.041600+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Trunk Device Reports

## Chapter: Trunk Device Reports

# Trunk Device Reports

CAR provides reporting capabilities for three levels of users:
                        		administrators, managers, and individual users. Only administrators generate
                        		device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, gateways, and trunks.

Only CAR administrators generate the trunk reports. The
                        		following section describes how to configure Trunk Utilization reports.

## Generate Trunk Utilization Reports

Only CAR administrators generate the Trunk Utilization
                              		  report. This report calculates the utilization reports for devices based on the
                              		  duration of calls that passed through the devices.

You can generate this report on an hourly, daily, or monthly
                              		  basis. The system calculates the utilization of a trunk for each hour in the
                              		  selected date range. For example, the system calculates the utilization of a
                              		  trunk between 11hrs-12hrs, using the formula, (Sum of the duration of calls
                              		  that used the trunk in that hour / (total seconds in an hour * maximum number
                              		  of ports in a trunk * number of days between the fromDate and toDate selected)
                              		  * 100).

Similarly, to get the utilization for each day in a week, the
                              		  system calculates the utilization using the formula, ((sum of the duration of
                              		  calls that used the trunk in a day) / (total seconds in each day * number of
                              		  each day between the fromDate and toDate selected * maximum number of ports in
                              		  a trunk) * 100).

In the case of monthly utilization reports, the system
                              		  calculates the utilization for each day in a month, using the formula, ((sum of
                              		  the duration of calls that used the trunk in a day) / (total seconds in each
                              		  day * number of each day between the fromDate and toDate selected * maximum
                              		  number of ports in a trunk) * 100).

Reports generate for each trunk that is chosen.

For calculation of the trunk utilization, the system uses the port numbers from the CAR Trunk Configuration window. To find
                              this window, choose System > System Parameters > Trunk Configuration . You cannot take port details for H.323 trunks from the Unified Communications Manager database because the H.323 port number always equals zero in the database. The user must update H.323 trunk ports information
                              in the CAR Trunk Configuration window.

Be aware that the only port detail information that is taken from the CAR Trunk Configuration window is only for those trunks
                              that do not have port details that are available or that show zero in the Unified Communications Manager database.

This section describes how to generate, view, or mail Trunk
                              		  Utilization reports.

Choose Device
                                             				  Reports > Trunk > Utilization .

The Trunk Utilization window displays.

In the Generate Reports field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 7 .

Day of Week

Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 7 .

Day of Month

Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 7 .

The Trunk Utilization report is not generated automatically.

To display the list of trunks that you can include in the report
                                       			 in the List of Trunks box, perform one of the following tasks:

To display all trunks in the List of Trunks box, click Trunk Types in the column on the left side
                                             				  of the window.

To display trunks for a particular trunk type in the List of
                                             				  Trunks box, click the icon next to Trunk Types in the column on the left side
                                             				  of the window. The tree structure expands, and a list of trunk types displays.
                                             				  Choose a trunk type from the list, and the trunk name displays in the List of
                                             				  Trunks box.

The List of Trunks box will list up to 200 trunks that are
                                                            						configured for the chosen trunk type.

You can generate the trunk utilization reports for route
                                                            						groups, route lists, and route patterns that are connected through trunks.

Choose a trunk type from the list.

The trunk name displays in the List of Trunks box.

The List of Trunks box displays up to 200 trunks that are
                                                      				  configured for the chosen trunk type.

In the List of Trunks box, choose the trunks that you want to include in
                                       			 the report.

You can generate a report for up to five trunks at a time.

To move the chosen trunk to the list of Selected Trunks box, click
                                       			 the down arrow.

The trunk(s) that you chose displays in the Selected Trunks box.

If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information.

Ensure the date and time range does not exceed one month.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays.

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Step 1 | Choose Device
                                             				  Reports > Trunk > Utilization . The Trunk Utilization window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the
                                       			 following table. Table 1. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 7 . Day of Week Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 7 . Day of Month Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 7 . Note The Trunk Utilization report is not generated automatically. | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 7 . | Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 7 . | Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 7 . | Note | The Trunk Utilization report is not generated automatically. |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 7 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 7 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 7 . |
| Note | The Trunk Utilization report is not generated automatically. |
| Step 3 | To display the list of trunks that you can include in the report
                                       			 in the List of Trunks box, perform one of the following tasks: To display all trunks in the List of Trunks box, click Trunk Types in the column on the left side
                                             				  of the window. To display trunks for a particular trunk type in the List of
                                             				  Trunks box, click the icon next to Trunk Types in the column on the left side
                                             				  of the window. The tree structure expands, and a list of trunk types displays.
                                             				  Choose a trunk type from the list, and the trunk name displays in the List of
                                             				  Trunks box. Note The List of Trunks box will list up to 200 trunks that are
                                                            						configured for the chosen trunk type. Note You can generate the trunk utilization reports for route
                                                            						groups, route lists, and route patterns that are connected through trunks. | Note | The List of Trunks box will list up to 200 trunks that are
                                                            						configured for the chosen trunk type. | Note | You can generate the trunk utilization reports for route
                                                            						groups, route lists, and route patterns that are connected through trunks. |
| Note | The List of Trunks box will list up to 200 trunks that are
                                                            						configured for the chosen trunk type. |
| Note | You can generate the trunk utilization reports for route
                                                            						groups, route lists, and route patterns that are connected through trunks. |
| Step 4 | Choose a trunk type from the list. The trunk name displays in the List of Trunks box. Note The List of Trunks box displays up to 200 trunks that are
                                                      				  configured for the chosen trunk type. | Note | The List of Trunks box displays up to 200 trunks that are
                                                      				  configured for the chosen trunk type. |
| Note | The List of Trunks box displays up to 200 trunks that are
                                                      				  configured for the chosen trunk type. |
| Step 5 | In the List of Trunks box, choose the trunks that you want to include in
                                       			 the report. Note You can generate a report for up to five trunks at a time. | Note | You can generate a report for up to five trunks at a time. |
| Note | You can generate a report for up to five trunks at a time. |
| Step 6 | To move the chosen trunk to the list of Selected Trunks box, click
                                       			 the down arrow. The trunk(s) that you chose displays in the Selected Trunks box. |
| Step 7 | If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 8 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 9 | Click the View Report button. The report displays. |
| Step 10 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 7 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 7 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 7 . |

| Note | The Trunk Utilization report is not generated automatically. |
|---|---|

| Note | The List of Trunks box will list up to 200 trunks that are
                                                            						configured for the chosen trunk type. |
|---|---|

| Note | You can generate the trunk utilization reports for route
                                                            						groups, route lists, and route patterns that are connected through trunks. |
|---|---|

| Note | The List of Trunks box displays up to 200 trunks that are
                                                      				  configured for the chosen trunk type. |
|---|---|

| Note | You can generate a report for up to five trunks at a time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|