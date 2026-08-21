---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--2d38b41c33
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_010011.html
retrieved_at: 2026-08-21T01:36:43.057186+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Gateway Device Reports

## Chapter: Gateway Device Reports

# Gateway Device Reports

CAR provides reporting capabilities for three levels of users:
                        		administrators, managers, and individual users. Only administrators generate
                        		device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, and gateways.

Only CAR administrators generate the gateway reports. The
                        		following sections describe how to configure Gateway Detail, Gateway Summary,
                        		and Gateway Utilization reports.

## Generate Gateway Detail Reports

Only CAR administrators generate the Gateway Detail report.
                              		  Use the Gateway Detail report to track issues with specific gateways.

This section describes how to generate, view, or mail
                              		  detailed information about selected gateways.

Choose Device
                                             				  Reports > Gateway > Detail .

The Gateway Detail window appears.

To display the list of gateways that you can include in the
                                       			 report, in the List of Gateways box perform one of the following tasks:

To display all gateways in the List of Gateways box, click Gateway Types in the column on the left
                                             				  side of the window.

To display gateways for a particular gateway type in the List
                                             				  of Gateways box, click the icon next to Gateway Types in the column on the left side of the window. The
                                             				  tree structure expands, and a list of gateway types displays. Choose a gateway
                                             				  type from the list, and the gateway name displays in the List of Gateways box.

The List of Gateways box lists up to 200 gateways that
                                                            						are configured for the chosen gateway type.

To display all gateways that are associated with configured
                                             				  route patterns/hunt pilots, click the Route/Patterns/Hunt Pilots in the column
                                             				  on the left side of the window.

To display gateways that use a particular route pattern,
                                             				  rather than a gateway type, click the icon next to Route Patterns/Hunt Pilots in the column
                                             				  on the left side of the window. The tree structure expands and displays a list
                                             				  of route patterns/hunt lists. Choose a route pattern/hunt pilot from the list,
                                             				  and the gateway name displays in the List of Gateways box.

You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string.

In the List of Gateways box, choose the gateways that you want to
                                       			 include in the report.

You can generate a report for up to five gateways at a time.

To move the chosen gateway to the list of Selected Gateways box,
                                       			 click the down arrow.

The gateway or gateways that you chose appear in the Selected Gateways
                                          				box.

In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want to include in the report. The following table describes
                                       			 the call types.

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan .

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

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911.

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

QoS for these calls represents degraded quality
                                                      						  but still within a usable range.

Poor

QoS for these calls represents unsatisfactory
                                                      						  quality.

NA

These calls do not match any criteria for the
                                                      						  established QoS categories.

Choose the date range for the period for which you want to see
                                       			 call information.

Ensure the date and time range does not exceed one month.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report appears.

If you want to mail the report, click the Send Report button. To send the report, follow
                                       			 the procedure that is described in the Mail Reports .

## Generate Gateway Summary Reports

Only CAR administrators generate the Gateway Summary report.
                              		  This report provides a summary of all the calls that went through the gateways.
                              		  You can use this information for monitoring the traffic and QoS for calls
                              		  through the gateways.

You can either view reports that the system automatically
                              		  generates or generate new reports. Only CAR administrators can schedule reports
                              		  for automatic generation. See the CAR System Parameters ,
                              		  for more information.

This section describes how to generate, view, or mail summary
                              		  information about gateways.

Choose Device
                                             				  Reports > Gateway > Summary .

The Gateway Summary window displays.

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 6 or use the default setting, Generate New Report and go to Step 3 .

In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want to include in the report. The following table describes
                                       			 the call types.

To check all check boxes, click Select All ; to uncheck the check boxes,
                                                      				  click Clear All .

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

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911.

If you chose Generate New Report, choose the date range of the
                                       			 period for which you want to generate the report.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Generate Gateway Utilization Reports

Only CAR administrators generate the Gateway Utilization
                              		  report. The report provides an estimate of the utilization percentage of the
                              		  gateway for the period and not the exact utilization. For example, the system
                              		  calculates the utilization of a gateway between 11hrs-12hrs, as the (sum of the
                              		  duration of the calls that used the gateway in that hour / (maximum duration
                              		  seconds in an hour * maximum number of ports in a gateway * number of days
                              		  between the fromDate and toDate selected) * 100). Similarly, to get a
                              		  utilization for the whole day, the system calculates the utilization as
                              		  mentioned for each hour. You can examine the usage based on each hour of a day
                              		  or on a specified number of days for each week or month.

In the case of weekly utilization reports, the system
                              		  calculates the utilization as ((sum of the duration of the calls that used the
                              		  gateway in a day) / (maximum duration seconds in each day * number of each day
                              		  between the fromDate and toDate selected * maximum number of ports in a
                              		  gateway) * 100).

In case of monthly utilization reports, the system
                              		  calculates the utilization as ((sum of the duration of the calls that used the
                              		  gateway in a day) / (maximum duration seconds in each day * number of each day
                              		  between the fromDate and toDate selected * maximum number of ports in a
                              		  gateway) * 100).

Reports generate for each gateway that is chosen.

For calculation of the utilization of H.323 gateways, the system uses the port numbers from the CAR Gateway Configuration
                              window. To find this window, choose System > System Parameters > Gateway Configuration . You cannot take port details for H.323 gateways from the Unified Communications Manager database because the H.323 port number always equals zero in the database. The user must update H.323 gateway ports information
                              in the CAR Gateway Configuration window.

Be aware that the only port detail information that is taken from the CAR Gateway Configuration window is only for those gateways
                              that do not have port details that are available or that show zero in the Unified Communications Manager database.

You can either view reports that the system automatically
                              		  generates or generate new reports. Only CAR administrators can schedule reports
                              		  for automatic generation. See the CAR System Parameters ,
                              		  for more information.

This section describes how to generate, view, or mail
                              		  Gateway Utilization reports.

Choose Device
                                             				  Reports > Gateway > Utilization .

The Gateway Utilization window displays.

In the Generate Reports field, choose a time as described in the
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

To display the list of gateways that you can include in the report
                                       			 in the List of Gateways box, perform one of the following tasks:

To display all gateways in the List of Gateways box, click Gateway Types in the column on the left
                                             				  side of the window.

To display gateways for a particular gateway type in the List
                                             				  of Gateways box, click the icon next to Gateway Types in the column on the left side of the window. The
                                             				  tree structure expands, and a list of gateway types displays. Choose a gateway
                                             				  type from the list, and the gateway name displays in the List of Gateways box.

The List of Gateways box will list up to 200 gateways that
                                                            						are configured for the chosen gateway type.

To display all gateways that are associated with configured
                                             				  route patterns/hunt pilots, click the Route Patterns/Hunt Pilots in the column
                                             				  on the left side of the window.

To display gateways that use a particular route pattern,
                                             				  rather than a gateway type, click the icon next to Route Patterns/Hunt Pilots in the column
                                             				  on the left side of the window. The tree structure expands and displays a list
                                             				  of route patterns/hunt lists. Choose a route pattern/hunt pilot from the list,
                                             				  and the gateway name displays in the List of Gateways box.

You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string.

Choose a gateway type from the list.

The gateway name displays in the List of Gateways box.

The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type.

In the List of Gateways box, choose the gateways that you want to
                                       			 include in the report.

You can generate a report for up to five gateways at a time.

To move the chosen gateway to the list of Selected Gateways box,
                                       			 click the down arrow.

The gateway(s) that you chose displays in the Selected Gateways
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
                                             				  Reports > Gateway > Detail . The Gateway Detail window appears. |
|---|---|
| Step 2 | To display the list of gateways that you can include in the
                                       			 report, in the List of Gateways box perform one of the following tasks: To display all gateways in the List of Gateways box, click Gateway Types in the column on the left
                                             				  side of the window. To display gateways for a particular gateway type in the List
                                             				  of Gateways box, click the icon next to Gateway Types in the column on the left side of the window. The
                                             				  tree structure expands, and a list of gateway types displays. Choose a gateway
                                             				  type from the list, and the gateway name displays in the List of Gateways box. Note The List of Gateways box lists up to 200 gateways that
                                                            						are configured for the chosen gateway type. To display all gateways that are associated with configured
                                             				  route patterns/hunt pilots, click the Route/Patterns/Hunt Pilots in the column
                                             				  on the left side of the window. To display gateways that use a particular route pattern,
                                             				  rather than a gateway type, click the icon next to Route Patterns/Hunt Pilots in the column
                                             				  on the left side of the window. The tree structure expands and displays a list
                                             				  of route patterns/hunt lists. Choose a route pattern/hunt pilot from the list,
                                             				  and the gateway name displays in the List of Gateways box. Note You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string. | Note | The List of Gateways box lists up to 200 gateways that
                                                            						are configured for the chosen gateway type. | Note | You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string. |
| Note | The List of Gateways box lists up to 200 gateways that
                                                            						are configured for the chosen gateway type. |
| Note | You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string. |
| Step 3 | In the List of Gateways box, choose the gateways that you want to
                                       			 include in the report. Note You can generate a report for up to five gateways at a time. | Note | You can generate a report for up to five gateways at a time. |
| Note | You can generate a report for up to five gateways at a time. |
| Step 4 | To move the chosen gateway to the list of Selected Gateways box,
                                       			 click the down arrow. The gateway or gateways that you chose appear in the Selected Gateways
                                          				box. |
| Step 5 | In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want to include in the report. The following table describes
                                       			 the call types. Table 1. Gateway Details by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . Local Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . | Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
| Step 6 | In the Select QoS area, check the check boxes for the voice-quality
                                       			 categories that you want to include in the report. The parameters that are set
                                       			 in the following table provide the basis for all voice-quality categories. Table 2. Gateway Detail Voice Quality Voice Quality Description Good QoS for these calls represents the highest
                                                      						  possible quality. Acceptable QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range. Fair QoS for these calls represents degraded quality
                                                      						  but still within a usable range. Poor QoS for these calls represents unsatisfactory
                                                      						  quality. NA These calls do not match any criteria for the
                                                      						  established QoS categories. | Voice Quality | Description | Good | QoS for these calls represents the highest
                                                      						  possible quality. | Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range. | Fair | QoS for these calls represents degraded quality
                                                      						  but still within a usable range. | Poor | QoS for these calls represents unsatisfactory
                                                      						  quality. | NA | These calls do not match any criteria for the
                                                      						  established QoS categories. |
| Voice Quality | Description |
| Good | QoS for these calls represents the highest
                                                      						  possible quality. |
| Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range. |
| Fair | QoS for these calls represents degraded quality
                                                      						  but still within a usable range. |
| Poor | QoS for these calls represents unsatisfactory
                                                      						  quality. |
| NA | These calls do not match any criteria for the
                                                      						  established QoS categories. |
| Step 7 | Choose the date range for the period for which you want to see
                                       			 call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 8 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 9 | Click the View Report button. The report appears. |
| Step 10 | If you want to mail the report, click the Send Report button. To send the report, follow
                                       			 the procedure that is described in the Mail Reports . |

| Note | The List of Gateways box lists up to 200 gateways that
                                                            						are configured for the chosen gateway type. |
|---|---|

| Note | You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string. |
|---|---|

| Note | You can generate a report for up to five gateways at a time. |
|---|---|

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |

| Voice Quality | Description |
|---|---|
| Good | QoS for these calls represents the highest
                                                      						  possible quality. |
| Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still falls within an acceptable range. |
| Fair | QoS for these calls represents degraded quality
                                                      						  but still within a usable range. |
| Poor | QoS for these calls represents unsatisfactory
                                                      						  quality. |
| NA | These calls do not match any criteria for the
                                                      						  established QoS categories. |

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device
                                             				  Reports > Gateway > Summary . The Gateway Summary window displays. |
|---|---|
| Step 2 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 6 or use the default setting, Generate New Report and go to Step 3 . |
| Step 3 | In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want to include in the report. The following table describes
                                       			 the call types. Tip To check all check boxes, click Select All ; to uncheck the check boxes,
                                                      				  click Clear All . Table 3. Gateway Summary by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. | Tip | To check all check boxes, click Select All ; to uncheck the check boxes,
                                                      				  click Clear All . | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
| Tip | To check all check boxes, click Select All ; to uncheck the check boxes,
                                                      				  click Clear All . |
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
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
| Step 4 | If you chose Generate New Report, choose the date range of the
                                       			 period for which you want to generate the report. |
| Step 5 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 6 | Click the View Report button. The report displays . |
| Step 7 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Tip | To check all check boxes, click Select All ; to uncheck the check boxes,
                                                      				  click Clear All . |
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
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |

| Step 1 | Choose Device
                                             				  Reports > Gateway > Utilization . The Gateway Utilization window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the
                                       			 following table. Table 4. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each
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
| Step 4 | To display the list of gateways that you can include in the report
                                       			 in the List of Gateways box, perform one of the following tasks: To display all gateways in the List of Gateways box, click Gateway Types in the column on the left
                                             				  side of the window. To display gateways for a particular gateway type in the List
                                             				  of Gateways box, click the icon next to Gateway Types in the column on the left side of the window. The
                                             				  tree structure expands, and a list of gateway types displays. Choose a gateway
                                             				  type from the list, and the gateway name displays in the List of Gateways box. Note The List of Gateways box will list up to 200 gateways that
                                                            						are configured for the chosen gateway type. To display all gateways that are associated with configured
                                             				  route patterns/hunt pilots, click the Route Patterns/Hunt Pilots in the column
                                             				  on the left side of the window. To display gateways that use a particular route pattern,
                                             				  rather than a gateway type, click the icon next to Route Patterns/Hunt Pilots in the column
                                             				  on the left side of the window. The tree structure expands and displays a list
                                             				  of route patterns/hunt lists. Choose a route pattern/hunt pilot from the list,
                                             				  and the gateway name displays in the List of Gateways box. Note You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string. | Note | The List of Gateways box will list up to 200 gateways that
                                                            						are configured for the chosen gateway type. | Note | You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string. |
| Note | The List of Gateways box will list up to 200 gateways that
                                                            						are configured for the chosen gateway type. |
| Note | You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string. |
| Step 5 | Choose a gateway type from the list. The gateway name displays in the List of Gateways box. Note The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type. | Note | The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type. |
| Note | The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type. |
| Step 6 | In the List of Gateways box, choose the gateways that you want to
                                       			 include in the report. Note You can generate a report for up to five gateways at a time. | Note | You can generate a report for up to five gateways at a time. |
| Note | You can generate a report for up to five gateways at a time. |
| Step 7 | To move the chosen gateway to the list of Selected Gateways box,
                                       			 click the down arrow. The gateway(s) that you chose displays in the Selected Gateways
                                          				box. |
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

| Note | The List of Gateways box will list up to 200 gateways that
                                                            						are configured for the chosen gateway type. |
|---|---|

| Note | You can also search for specific route patterns/hunt lists
                                                            						by entering part of the name of the route pattern(s)/hunt list(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt list(s) that matches the search string. |
|---|---|

| Note | The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type. |
|---|---|

| Note | You can generate a report for up to five gateways at a time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|