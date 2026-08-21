---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--ab65b7c846
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_010100.html
retrieved_at: 2026-08-21T01:36:46.602724+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Route Pattern and Hunt Pilot Device Reports

## Chapter: Route Pattern and Hunt Pilot Device Reports

# Route Pattern and Hunt Pilot Device Reports

CAR provides reporting capabilities for three levels of users:
                        		administrators, managers, and individual users. Only administrators generate
                        		the Route Pattern and Hunt Pilot device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, and gateways.

## Generate Route and Line Group Utilization Reports

Only CAR administrators generate the Route and Line Group
                              		  Utilization report. This report provides an estimate of the maximum utilization
                              		  percentage of the route and line group (cumulative utilization of all the
                              		  gateways under the route and line group) for the period and not the exact
                              		  utilization. The system calculates the utilization in the same manner as is
                              		  done for Gateway Utilization, but this calculation gives cumulative utilization
                              		  of all the gateways under the route groups and all the lines under the line
                              		  groups. You can examine the usage based on each hour of a day or on a specified
                              		  number of days for each week or month. Reports generate for each of the
                              		  selected route and line groups.

You can either view reports that the system automatically
                              		  generates or generate new reports. Only CAR administrators can schedule reports
                              		  for automatic generation. See the CAR System Parameters ,
                              		  for more information.

This section describes how to generate, view, or mail Route
                              		  and Line Group Utilization reports.

Choose Device Reports > Route
                                             				  Patterns/Hunt Pilots > Route and Line Group
                                             				  Utilization .

The Route and Line Group Utilization window displays.

In the Generate Reports field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 .

Day of Week

Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 .

Day of Month

Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 .

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 10 ,
                                       			 or use the default setting, Generate New Report, and go to Step 4 .

To choose only those route and line groups that use a particular
                                       			 route pattern, click Route Patterns/Hunt Pilots in the column on
                                       			 the left side of the window.

The tree structure expands and displays the route patterns/hunt
                                          				lists that you chose.

You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string.

Choose a route pattern/hunt list from the list.

The route and line groups for this route pattern/hunt list display
                                          				in the List of Route/Line Groups box.

The List of Route/Line Groups box will display up to 200 route
                                                      				  groups.

In the List of Route/Line Groups box, choose the route/line groups that
                                       			 you want to include in the report.

You can generate a report for up to five route/line groups at a
                                                      				  time.

To move the chosen gateway to the list of Selected Route/Line
                                       			 Groups box, click the down arrow.

The route/line groups that you chose display in the Selected Route
                                          				Groups box.

If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information.

Ensure the date and time range does not exceed one month.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report, follow
                                       			 the procedure that is described in the Mail Reports .

## Generate Route and Hunt List Utilization Reports

Only CAR administrators generate the Route/Hunt List
                              		  Utilization report. The Route/Hunt List Utilization report provides an estimate
                              		  of the maximum utilization percentage of the route/hunt list (cumulative
                              		  utilization of all the gateways under the route/hunt list) for the period and
                              		  not the exact utilization. The system calculates the cumulative utilization of
                              		  all the gateways under the route lists and all the lines under the hunt lists.

You can examine the usage based on each hour of a day or on a
                              		  specified number of days for each week or month. Reports generate for each of
                              		  the selected route/hunt lists.

You can either view reports that the system automatically
                              		  generates or generate new reports. Only CAR administrators can schedule reports
                              		  for automatic generation. See CAR System Scheduler ,
                              		  for more information.

This section describes how to generate, view, or mail the
                              		  Route/Hunt List Utilization reports.

Choose Device Reports > Route
                                             				  Patterns/Hunt Pilots > Route/Hunt List
                                             				  Utilization .

The Route/Hunt List Utilization window displays.

In the Generate Report field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 .

Day of Week

Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 .

Day of Month

Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 .

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 10 or use the default setting, Generate New Report, and go to Step 4 .

To choose the route/hunt lists that you want to include in the
                                       			 report, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree
                                       			 structure expands and displays the route patterns/hunt pilots that you chose.

You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt lists in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string.

Choose a route/hunt list from the list.

The route/hunt list name displays in the List of Route/Hunt Lists
                                          				box.

The List of Route/Hunt Lists box will display up to 200
                                                      				  route/hunt lists.

In the List of Route/Hunt Lists box, choose the route/hunt lists that
                                       			 you want to include in the report.

You can generate a report for up to five route/hunt lists at a
                                                      				  time.

To move the chosen route/hunt lists to the list of Selected
                                       			 Route/Hunt Lists box, click the down arrow.

The route/hunt lists that you chose display in the Selected
                                          				Route/Hunt Lists box.

If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information.

Ensure the date and time range does not exceed one month.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Generate Route Pattern and Hunt Pilot Utilization Reports

Only CAR administrators generate the Route Pattern/Hunt Pilot
                              		  Utilization report. The report provides an estimate of the maximum utilization
                              		  percentage of the route pattern/hunt pilot (cumulative utilization of all the
                              		  gateways under the route pattern/hunt pilot) for the period and not the exact
                              		  utilization. The system calculates the utilization of all the gateways under
                              		  the route patterns and all the lines under the hunt pilots. You can examine the
                              		  usage based on each hour of a day or on a specified number of days for each
                              		  week or month. Reports generate for each of the selected route patterns/hunt
                              		  pilots.

You can either view reports that the system automatically
                              		  generates or generate new reports. Only CAR administrators can schedule reports
                              		  for automatic generation. See CAR System Scheduler ,
                              		  for more information.

This section describes how to generate, view, or mail Route
                              		  Pattern/Hunt Pilot Utilization reports.

Choose Device Reports > Route
                                             				  Pattern/Hunt Pilots > Route Pattern/Hunt Pilot
                                             				  Utilization .

The Route Pattern/Hunt Pilot Utilization window displays.

In the Generate Report field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each
                                                      						  hour in a 24-hour period for the period that you specify in Step 8 .

Day of Week

Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 .

Day of Month

Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 .

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 10 or use the default Generate New Report and go to Step 4 .

To choose the route pattern(s)/hunt list(s) that you want to
                                       			 include in the report, click Route Patterns/Hunt Pilots in the column on the left side of the window.

The tree structure expands and displays the route pattern(s)/hunt
                                          				list(s) that you chose.

You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns box in the column on the left side of the window. CAR searches for the
                                                      				  route pattern(s)/hunt list(s) that matches the search string.

Choose a route pattern/hunt pilot from the list.

The route pattern/hunt pilot name displays in the List of Route
                                          				Patterns/Hunt Pilots box.

The List of Route Patterns/Hunt Pilots box will display up to
                                                      				  200 route patterns/hunt lists.

In the List of Route Patterns/Hunt Pilots box, choose the route
                                       			 patterns/hunt lists that you want to include in the report.

You can generate a report for up to five route patterns/hunt
                                                      				  pilots at a time.

Click the down arrow to move the chosen route pattern/hunt pilot
                                       			 to the list of Selected Route Patterns/Hunt Pilots box.

The route pattern/hunt pilot that you chose displays in the
                                          				Selected Route Patterns/Hunt Pilots box.

If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information.

Ensure the date and time range does not exceed one month.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Generate Hunt Pilot Summary Report

Only CAR administrators generate the Hunt Pilot Summary
                              		  Report.The CDR Hunt Pilot Call Summary report displays the call details for the
                              		  specified hunt pilot. This report displays an only an overview of the calls for
                              		  the hunt pilots and hunt member information is not included. The CAR
                              		  administrator can generate report for a maximum of five hunt pilot DNs.

This section describes how to generate, view, or mail Hunt
                              		  Pilot Summary reports.

Choose Device Reports > Route
                                             				  Pattern/Hunt Pilots > Hunt Pilot
                                             				  Summary .

The Hunt Pilot Detail Summary displays.

Enter the hunt pilot number in the Hunt Pilots text box and press the Enter key.

The hunt pilot number is displayed below the text box.
                                          				Alternately, you can click the icon to display all the available hunt pilot
                                          				numbers.

Click on the required hunt pilot number, so that it is listed in
                                       			 the List of Hunt Pilots.

From the Generate Reports drop-down list, choose:

Hour of the day - Displays the call details for each hour in a
                                             				  24-hour period for the period that you specify in Step 7 .

Day of the Week - Displays the call details for the days of
                                             				  the week that occur within the period that you specify in Step 7 .

Day of the Month - Displays the call details for the days of
                                             				  the month that occur within the period that you specify in Step 7 .

Choose any of the available reports or the Generate New Report
                                       			 option from the Available Reports drop-down list.

From the list of hunt pilots available, choose the required ones
                                       			 and click the down arrow.

The hunt pilots chosen are displayed in the Selected Hunt Pilots list.

Choose the From Date and the To Date from the drop-down lists available.

Choose the required report format.

It can either be CSV or PDF . PDF is the default report option.

Click View Report to view the report.

To view the report results, see Hunt Pilot Summary Report Results .

If you want to mail the report, click Send Report.

To send the report, perform the procedure that is described in the Mail Reports .

## Generate Hunt Pilot Detail Report

Only CAR administrators generate the Hunt Pilot Detailed
                              		  Call Report. This report displays call details for a hunt pilot number or a
                              		  hunt member dn.

This section describes how to generate, view, or mail Hunt
                              		  Pilot Detail reports.

Choose Device Reports > Route
                                             				  Pattern/Hunt Pilots > Hunt Pilot
                                             				  Detail .

The Hunt Pilot Detail window displays.

Select the HuntPilot or the MemberDn for generating the report.

Enter the hunt pilot number in the Hunt Pilots text box and press the Enter key.

The hunt pilot number is displayed below the text box.
                                          				Alternately, you can click the icon to display the hunt pilot numbers.

If you had selected the hunt pilot option, click on the required
                                       			 hunt pilot number, so that it is listed in the SelectedHuntPilot/MemberDn list box. Proceed to Step 7 .

If you had selected the member dn option, click on the required
                                       			 hunt pilot number to list the member dn numbers in it.

From the list of member dns, click on the required ones so that
                                       			 they get listed in the SelectedHuntPilot/MemberDn list box.

Choose any of the available reports or the Generate New Report
                                       			 option from the Available Reports drop-down list.

Choose the From Date and the To Date from the drop-down lists available.

Choose the required report format.

It can either be CSV or PDF. PDF is the default report option.

Click View Report to view the report.

To view the report results, see Hunt Pilot Detail Report Results .

If you want to mail the report, click Send Report.

To send the report, perform the procedure that is described in the Mail Reports .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Step 1 | Choose Device Reports > Route
                                             				  Patterns/Hunt Pilots > Route and Line Group
                                             				  Utilization . The Route and Line Group Utilization window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the
                                       			 following table. Table 1. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 . Day of Week Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . Day of Month Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 . | Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . | Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |
| Step 3 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 10 ,
                                       			 or use the default setting, Generate New Report, and go to Step 4 . |
| Step 4 | To choose only those route and line groups that use a particular
                                       			 route pattern, click Route Patterns/Hunt Pilots in the column on
                                       			 the left side of the window. The tree structure expands and displays the route patterns/hunt
                                          				lists that you chose. Note You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string. | Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string. |
| Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string. |
| Step 5 | Choose a route pattern/hunt list from the list. The route and line groups for this route pattern/hunt list display
                                          				in the List of Route/Line Groups box. Note The List of Route/Line Groups box will display up to 200 route
                                                      				  groups. | Note | The List of Route/Line Groups box will display up to 200 route
                                                      				  groups. |
| Note | The List of Route/Line Groups box will display up to 200 route
                                                      				  groups. |
| Step 6 | In the List of Route/Line Groups box, choose the route/line groups that
                                       			 you want to include in the report. Note You can generate a report for up to five route/line groups at a
                                                      				  time. | Note | You can generate a report for up to five route/line groups at a
                                                      				  time. |
| Note | You can generate a report for up to five route/line groups at a
                                                      				  time. |
| Step 7 | To move the chosen gateway to the list of Selected Route/Line
                                       			 Groups box, click the down arrow. The route/line groups that you chose display in the Selected Route
                                          				Groups box. |
| Step 8 | If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 9 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 10 | Click the View Report button. The report displays . |
| Step 11 | If you want to mail the report, click the Send Report button. To send the report, follow
                                       			 the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |

| Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string. |
|---|---|

| Note | The List of Route/Line Groups box will display up to 200 route
                                                      				  groups. |
|---|---|

| Note | You can generate a report for up to five route/line groups at a
                                                      				  time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Route
                                             				  Patterns/Hunt Pilots > Route/Hunt List
                                             				  Utilization . The Route/Hunt List Utilization window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the
                                       			 following table. Table 2. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 . Day of Week Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . Day of Month Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 . | Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . | Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |
| Step 3 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 10 or use the default setting, Generate New Report, and go to Step 4 . |
| Step 4 | To choose the route/hunt lists that you want to include in the
                                       			 report, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree
                                       			 structure expands and displays the route patterns/hunt pilots that you chose. Note You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt lists in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string. | Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt lists in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string. |
| Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt lists in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string. |
| Step 5 | Choose a route/hunt list from the list. The route/hunt list name displays in the List of Route/Hunt Lists
                                          				box. Note The List of Route/Hunt Lists box will display up to 200
                                                      				  route/hunt lists. | Note | The List of Route/Hunt Lists box will display up to 200
                                                      				  route/hunt lists. |
| Note | The List of Route/Hunt Lists box will display up to 200
                                                      				  route/hunt lists. |
| Step 6 | In the List of Route/Hunt Lists box, choose the route/hunt lists that
                                       			 you want to include in the report. Note You can generate a report for up to five route/hunt lists at a
                                                      				  time. | Note | You can generate a report for up to five route/hunt lists at a
                                                      				  time. |
| Note | You can generate a report for up to five route/hunt lists at a
                                                      				  time. |
| Step 7 | To move the chosen route/hunt lists to the list of Selected
                                       			 Route/Hunt Lists box, click the down arrow. The route/hunt lists that you chose display in the Selected
                                          				Route/Hunt Lists box. |
| Step 8 | If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 9 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 10 | Click the View Report button. The report displays . |
| Step 11 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour
                                                      						  in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |

| Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt lists in the Route
                                                      				  Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                      				  searches for the route pattern(s)/hunt list(s) that matches the search string. |
|---|---|

| Note | The List of Route/Hunt Lists box will display up to 200
                                                      				  route/hunt lists. |
|---|---|

| Note | You can generate a report for up to five route/hunt lists at a
                                                      				  time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Route
                                             				  Pattern/Hunt Pilots > Route Pattern/Hunt Pilot
                                             				  Utilization . The Route Pattern/Hunt Pilot Utilization window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the
                                       			 following table. Table 3. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each
                                                      						  hour in a 24-hour period for the period that you specify in Step 8 . Day of Week Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . Day of Month Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each
                                                      						  hour in a 24-hour period for the period that you specify in Step 8 . | Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . | Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each
                                                      						  hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |
| Step 3 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 10 or use the default Generate New Report and go to Step 4 . |
| Step 4 | To choose the route pattern(s)/hunt list(s) that you want to
                                       			 include in the report, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays the route pattern(s)/hunt
                                          				list(s) that you chose. Note You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns box in the column on the left side of the window. CAR searches for the
                                                      				  route pattern(s)/hunt list(s) that matches the search string. | Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns box in the column on the left side of the window. CAR searches for the
                                                      				  route pattern(s)/hunt list(s) that matches the search string. |
| Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns box in the column on the left side of the window. CAR searches for the
                                                      				  route pattern(s)/hunt list(s) that matches the search string. |
| Step 5 | Choose a route pattern/hunt pilot from the list. The route pattern/hunt pilot name displays in the List of Route
                                          				Patterns/Hunt Pilots box. Note The List of Route Patterns/Hunt Pilots box will display up to
                                                      				  200 route patterns/hunt lists. | Note | The List of Route Patterns/Hunt Pilots box will display up to
                                                      				  200 route patterns/hunt lists. |
| Note | The List of Route Patterns/Hunt Pilots box will display up to
                                                      				  200 route patterns/hunt lists. |
| Step 6 | In the List of Route Patterns/Hunt Pilots box, choose the route
                                       			 patterns/hunt lists that you want to include in the report. Note You can generate a report for up to five route patterns/hunt
                                                      				  pilots at a time. | Note | You can generate a report for up to five route patterns/hunt
                                                      				  pilots at a time. |
| Note | You can generate a report for up to five route patterns/hunt
                                                      				  pilots at a time. |
| Step 7 | Click the down arrow to move the chosen route pattern/hunt pilot
                                       			 to the list of Selected Route Patterns/Hunt Pilots box. The route pattern/hunt pilot that you chose displays in the
                                          				Selected Route Patterns/Hunt Pilots box. |
| Step 8 | If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 9 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 10 | Click the View Report button. The report displays . |
| Step 11 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each
                                                      						  hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days
                                                      						  of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days
                                                      						  of the month that occur within the period that you specify in Step 8 . |

| Note | You can also search for specific route patterns/hunt lists by
                                                      				  entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                      				  Patterns box in the column on the left side of the window. CAR searches for the
                                                      				  route pattern(s)/hunt list(s) that matches the search string. |
|---|---|

| Note | The List of Route Patterns/Hunt Pilots box will display up to
                                                      				  200 route patterns/hunt lists. |
|---|---|

| Note | You can generate a report for up to five route patterns/hunt
                                                      				  pilots at a time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Route
                                             				  Pattern/Hunt Pilots > Hunt Pilot
                                             				  Summary . The Hunt Pilot Detail Summary displays. |
|---|---|
| Step 2 | Enter the hunt pilot number in the Hunt Pilots text box and press the Enter key. The hunt pilot number is displayed below the text box.
                                          				Alternately, you can click the icon to display all the available hunt pilot
                                          				numbers. |
| Step 3 | Click on the required hunt pilot number, so that it is listed in
                                       			 the List of Hunt Pilots. |
| Step 4 | From the Generate Reports drop-down list, choose: Hour of the day - Displays the call details for each hour in a
                                             				  24-hour period for the period that you specify in Step 7 . Day of the Week - Displays the call details for the days of
                                             				  the week that occur within the period that you specify in Step 7 . Day of the Month - Displays the call details for the days of
                                             				  the month that occur within the period that you specify in Step 7 . |
| Step 5 | Choose any of the available reports or the Generate New Report
                                       			 option from the Available Reports drop-down list. |
| Step 6 | From the list of hunt pilots available, choose the required ones
                                       			 and click the down arrow. The hunt pilots chosen are displayed in the Selected Hunt Pilots list. |
| Step 7 | Choose the From Date and the To Date from the drop-down lists available. |
| Step 8 | Choose the required report format. It can either be CSV or PDF . PDF is the default report option. |
| Step 9 | Click View Report to view the report. To view the report results, see Hunt Pilot Summary Report Results . |
| Step 10 | If you want to mail the report, click Send Report. To send the report, perform the procedure that is described in the Mail Reports . |

| Step 1 | Choose Device Reports > Route
                                             				  Pattern/Hunt Pilots > Hunt Pilot
                                             				  Detail . The Hunt Pilot Detail window displays. |
|---|---|
| Step 2 | Select the HuntPilot or the MemberDn for generating the report. |
| Step 3 | Enter the hunt pilot number in the Hunt Pilots text box and press the Enter key. The hunt pilot number is displayed below the text box.
                                          				Alternately, you can click the icon to display the hunt pilot numbers. |
| Step 4 | If you had selected the hunt pilot option, click on the required
                                       			 hunt pilot number, so that it is listed in the SelectedHuntPilot/MemberDn list box. Proceed to Step 7 . |
| Step 5 | If you had selected the member dn option, click on the required
                                       			 hunt pilot number to list the member dn numbers in it. |
| Step 6 | From the list of member dns, click on the required ones so that
                                       			 they get listed in the SelectedHuntPilot/MemberDn list box. |
| Step 7 | Choose any of the available reports or the Generate New Report
                                       			 option from the Available Reports drop-down list. |
| Step 8 | Choose the From Date and the To Date from the drop-down lists available. |
| Step 9 | Choose the required report format. It can either be CSV or PDF. PDF is the default report option. |
| Step 10 | Click View Report to view the report. To view the report results, see Hunt Pilot Detail Report Results . |
| Step 11 | If you want to mail the report, click Send Report. To send the report, perform the procedure that is described in the Mail Reports . |