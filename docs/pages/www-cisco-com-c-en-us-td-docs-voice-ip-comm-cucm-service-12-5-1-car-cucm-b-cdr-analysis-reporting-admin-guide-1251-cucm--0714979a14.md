---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--0714979a14
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_01011.html
retrieved_at: 2026-08-21T01:34:08.150940+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Traffic System Reports

## Chapter: Traffic System Reports

# Traffic System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

Only CAR administrators can generate the traffic summary
                        		report. The report provides information about the call volume for a period that
                        		you specify. It includes only those call types and QoS voice-quality categories
                        		that you chose.

When you configure CAR to generate a traffic summary report, you can
                                    		  choose different call types (On Net, Internal, Local, Long Distance, and so
                                    		  on). CAR compares the traffic volume for every hour interval and identifies the
                                    		  hour with the highest traffic volume (the Busy Hour Call Completion [BHCC]
                                    		  number). To obtain the overall BHCC number, choose all call types when you
                                    		  configure CAR. Under the report title, a separate line displays the BHCC number
                                    		  for that day.

Only CAR administrators can generate the traffic summary by
                        		phone numbers report. The report provides information about the call volume for
                        		a period and set of phone numbers that you specify, and includes only those
                        		call types and phone numbers that you choose.

You can use this report to track call usage by a specified group of
                                    		  users, by a department, or by another criteria, such as lobby phones or
                                    		  conference room phones. You can set up this report to generate on a weekly
                                    		  basis. This report helps you determine high-usage users or groups by
                                    		  aggregating the usage level across the users that you specify.

## Generate Traffic Summary Reports

Only CAR administrators generate the Traffic Summary report.
                              		  The report provides information about the call volume for a period that you
                              		  specify.

You can either view reports that the system automatically
                              		  generates or generate new reports. See CAR System Scheduler ,
                              		  for more information.

This section describes how to generate, view, or mail summary
                              		  information about system traffic.

Choose System
                                             				  Reports > Traffic > Summary .

The Traffic Summary window displays.

In the Generate Report field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for hour of day.

If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour
                                                      						  interval and identifies the hour with the highest traffic volume as the BHCC
                                                      						  number for that day.

Day of Week

Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of the week.

Day of Month

Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of month.

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 8 or use the default setting, Generate New Report and go to Step 4 .

Choose the date range for the period for which you want to
                                       			 generate the report.

In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want to include in the report. To obtain the overall BHCC
                                       			 number for a particular hour or 24-hour period, choose all call types. The
                                       			 following table describes the call types.

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan .

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that route through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Others

All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911.

The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will designate the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report.

In the Select QoS area, check the check boxes for the voice-quality
                                       			 categories that you want to include in the report. The parameters that are set
                                       			 in the following table provide the basis for all voice-quality categories.

Voice Quality

Description

Good

QoS for these calls represents the highest
                                                      						  possible quality.

Acceptable

QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range.

Fair

QoS for these calls, although degraded, still
                                                      						  remains within a usable range.

Poor

Poor voice quality indicates that QoS for these
                                                      						  calls is unsatisfactory.

NA

These calls did not match any criteria for the
                                                      						  established QoS categories.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Generate Traffic Summary by Phone Number Reports

Only CAR administrators generate the Traffic Summary by Phone
                              		  Number report. The report provides information about the call volume for a
                              		  period and set of phone numbers that you specify.

This section describes how to generate, view, or mail a
                              		  traffic summary report based on user phone numbers.

Choose System
                                             				  Reports > Traffic > Summary By Phone
                                             				  Number .

The Traffic Summary that is based on Phone Number(s) window
                                          				displays.

In the Generate Report field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day.

Ensure that the date and time range does not exceed one
                                                                  							 month.

Day of Week

Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of week.

Ensure that the date and time range does not exceed one
                                                                  							 month.

Day of Month

Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of month.

Ensure that the date and time range does not exceed one
                                                                  							 month.

In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want to include in the report. The following table describes
                                       			 the call types.

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan .

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Others

All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911.

The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will represent the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report.

In the Select Phone Number(s) group box, you can either choose all
                                       			 phone numbers or search for phone numbers based on users.

You can enter a wildcard pattern like "!" or "X" to search on
                                                      				  phone numbers. The "!" represents any n digit that has 0-9 as each of its
                                                      				  digits, and the "X" represents a single digit in the range 0-9.

To choose all phone numbers, check the Select All Phone
                                             				  Number(s) check box. To choose phone numbers based on users, enter the phone
                                          				number of the individual in the Phone Number field and click the Add Phone Number button. You can also use a provided search function, as
                                          				described in the User Search .

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays .

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

| Note | Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter. |
|---|---|

| Tip | When you configure CAR to generate a traffic summary report, you can
                                    		  choose different call types (On Net, Internal, Local, Long Distance, and so
                                    		  on). CAR compares the traffic volume for every hour interval and identifies the
                                    		  hour with the highest traffic volume (the Busy Hour Call Completion [BHCC]
                                    		  number). To obtain the overall BHCC number, choose all call types when you
                                    		  configure CAR. Under the report title, a separate line displays the BHCC number
                                    		  for that day. |
|---|---|

| Tip | You can use this report to track call usage by a specified group of
                                    		  users, by a department, or by another criteria, such as lobby phones or
                                    		  conference room phones. You can set up this report to generate on a weekly
                                    		  basis. This report helps you determine high-usage users or groups by
                                    		  aggregating the usage level across the users that you specify. |
|---|---|

| Step 1 | Choose System
                                             				  Reports > Traffic > Summary . The Traffic Summary window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the
                                       			 following table. Table 1. Generate Report Fields Parameter Description Hour of Day Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for hour of day. If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour
                                                      						  interval and identifies the hour with the highest traffic volume as the BHCC
                                                      						  number for that day. Day of Week Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of the week. Day of Month Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of month. | Parameter | Description | Hour of Day | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for hour of day. If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour
                                                      						  interval and identifies the hour with the highest traffic volume as the BHCC
                                                      						  number for that day. | Day of Week | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of the week. | Day of Month | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of month. |
| Parameter | Description |
| Hour of Day | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for hour of day. If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour
                                                      						  interval and identifies the hour with the highest traffic volume as the BHCC
                                                      						  number for that day. |
| Day of Week | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of the week. |
| Day of Month | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of month. |
| Step 3 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 8 or use the default setting, Generate New Report and go to Step 4 . |
| Step 4 | Choose the date range for the period for which you want to
                                       			 generate the report. |
| Step 5 | In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want to include in the report. To obtain the overall BHCC
                                       			 number for a particular hour or 24-hour period, choose all call types. The
                                       			 following table describes the call types. Table 2. Traffic Summary by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that route through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Others All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. Note The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will designate the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that route through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. | Note | The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will designate the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that route through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
| Note | The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will designate the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report. |
| Step 6 | In the Select QoS area, check the check boxes for the voice-quality
                                       			 categories that you want to include in the report. The parameters that are set
                                       			 in the following table provide the basis for all voice-quality categories. Table 3. QoS Detail Report Voice Quality Voice Quality Description Good QoS for these calls represents the highest
                                                      						  possible quality. Acceptable QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range. Fair QoS for these calls, although degraded, still
                                                      						  remains within a usable range. Poor Poor voice quality indicates that QoS for these
                                                      						  calls is unsatisfactory. NA These calls did not match any criteria for the
                                                      						  established QoS categories. | Voice Quality | Description | Good | QoS for these calls represents the highest
                                                      						  possible quality. | Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range. | Fair | QoS for these calls, although degraded, still
                                                      						  remains within a usable range. | Poor | Poor voice quality indicates that QoS for these
                                                      						  calls is unsatisfactory. | NA | These calls did not match any criteria for the
                                                      						  established QoS categories. |
| Voice Quality | Description |
| Good | QoS for these calls represents the highest
                                                      						  possible quality. |
| Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range. |
| Fair | QoS for these calls, although degraded, still
                                                      						  remains within a usable range. |
| Poor | Poor voice quality indicates that QoS for these
                                                      						  calls is unsatisfactory. |
| NA | These calls did not match any criteria for the
                                                      						  established QoS categories. |
| Step 7 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 8 | Click the View Report button. The report displays . |
| Step 9 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for hour of day. If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour
                                                      						  interval and identifies the hour with the highest traffic volume as the BHCC
                                                      						  number for that day. |
| Day of Week | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of the week. |
| Day of Month | Displays the average number of calls in the
                                                      						  system for the period that you specify in Step 4 ,
                                                      						  the call types that you specify in Step 5 ,
                                                      						  and the QoS values that you specify in Step 6 for day of month. |

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that route through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |

| Note | The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will designate the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report. |
|---|---|

| Voice Quality | Description |
|---|---|
| Good | QoS for these calls represents the highest
                                                      						  possible quality. |
| Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range. |
| Fair | QoS for these calls, although degraded, still
                                                      						  remains within a usable range. |
| Poor | Poor voice quality indicates that QoS for these
                                                      						  calls is unsatisfactory. |
| NA | These calls did not match any criteria for the
                                                      						  established QoS categories. |

| Step 1 | Choose System
                                             				  Reports > Traffic > Summary By Phone
                                             				  Number . The Traffic Summary that is based on Phone Number(s) window
                                          				displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the
                                       			 following table. Table 4. Generate Report Fields Parameter Description Hour of Day Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day. Note Ensure that the date and time range does not exceed one
                                                                  							 month. Day of Week Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of week. Note Ensure that the date and time range does not exceed one
                                                                  							 month. Day of Month Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of month. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Parameter | Description | Hour of Day | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. | Day of Week | Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of week. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. | Day of Month | Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of month. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Parameter | Description |
| Hour of Day | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Day of Week | Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of week. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Day of Month | Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of month. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Step 3 | In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want to include in the report. The following table describes
                                       			 the call types. Table 5. Traffic Summary (Phone Number) by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Others All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. Note The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will represent the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. | Note | The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will represent the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
| Note | The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will represent the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report. |
| Step 4 | In the Select Phone Number(s) group box, you can either choose all
                                       			 phone numbers or search for phone numbers based on users. Note You can enter a wildcard pattern like "!" or "X" to search on
                                                      				  phone numbers. The "!" represents any n digit that has 0-9 as each of its
                                                      				  digits, and the "X" represents a single digit in the range 0-9. To choose all phone numbers, check the Select All Phone
                                             				  Number(s) check box. To choose phone numbers based on users, enter the phone
                                          				number of the individual in the Phone Number field and click the Add Phone Number button. You can also use a provided search function, as
                                          				described in the User Search . | Note | You can enter a wildcard pattern like "!" or "X" to search on
                                                      				  phone numbers. The "!" represents any n digit that has 0-9 as each of its
                                                      				  digits, and the "X" represents a single digit in the range 0-9. |
| Note | You can enter a wildcard pattern like "!" or "X" to search on
                                                      				  phone numbers. The "!" represents any n digit that has 0-9 as each of its
                                                      				  digits, and the "X" represents a single digit in the range 0-9. |
| Step 5 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 6 | Click the View Report button. The report displays . |
| Step 7 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Day of Week | Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of week. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Day of Month | Displays the average calls in the system for the
                                                      						  selected phone numbers for the date range that was chosen for day of month. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |

| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
|---|---|

| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
|---|---|

| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
|---|---|

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |

| Note | The calls that the chart/table shows comprise an average number
                                                      				  of calls per day. If the data that is generated is less and you have chosen a
                                                      				  wide date range, the report shows negligible values that are treated as 0, and
                                                      				  the graph does not display. For example, if a Day of Week report gets generated
                                                      				  for eight days that comprise two Mondays, the data that is shown for Monday
                                                      				  represents the average number of calls for both the Mondays (the sum of all the
                                                      				  calls in each Monday divided by 2). Similarly, in an Hour of Day report, the
                                                      				  data that displays against 05-06 will represent the average number of calls per
                                                      				  day between the time 05 and 06 of the date range that was chosen for the
                                                      				  report. |
|---|---|

| Note | You can enter a wildcard pattern like "!" or "X" to search on
                                                      				  phone numbers. The "!" represents any n digit that has 0-9 as each of its
                                                      				  digits, and the "X" represents a single digit in the range 0-9. |
|---|---|