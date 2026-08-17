---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-callreportingbillingadmin-15-cucm-b-reporting-billing-administration-gu-8687d4b7ee
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/callReportingBillingAdmin/15/cucm_b_reporting-billing-administration-guide-15/cucm_b_reporting-and-billing-administration-guide_chapter_0100.html
retrieved_at: 2026-08-17T00:25:20.040748+00:00
---

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: April 9, 2026

Chapter: Device Reports

## Chapter: Device Reports

# Device Reports

## CAR Device Reports

CAR provides reporting capabilities for three levels of users: administrators, managers, and individual users. Only administrators
                           generate device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, gateways, and trunks.

### Device Reports Summary Descriptions

Device reports help CAR administrators track the load and performance of Unified Communications Manager -related devices, such as conference bridges, voice-messaging server, gateways, and trunks. This section describes the device
                                 reports:

Gateway

Detail - Available for CAR administrators. Use the Gateway Detail report to track issues with specific gateways. The report
                                             provides a list of calls that used the specified gateways. Use this report to review detailed information about chosen gateways.
                                             You can specify gateways by type, such as all or some of the VG200 gateways in your system, or by only those gateways that
                                             use a particular route pattern. You can also specify search criteria based on call types and QoS values.

Summary - Available for CAR administrators. The Gateway Summary report provides a summary of all the calls that went through
                                             the gateways. It also provides the total number of calls and duration for each of the categories, namely Incoming, Tandem,
                                             and Outgoing (Long Distance, Local, International, Others, OnNet), and, also, the total calls for each QoS value for each
                                             gateway in the system. Use this report to track the functionality of the system on a daily basis. If you discover issues that
                                             need to be studied further, use the gateway detail report.

Utilization - Available for CAR administrators. The Gateway Utilization report provides an estimate of the utilization percentage
                                             of the gateway(s). You can examine the usage on the basis of each hour of a day or by a specified number of days of the week
                                             or month. Reports generate for each gateway that is chosen. Use this report for load balancing or capacity planning (to evaluate
                                             the need for adding or removing gateways, depending on their utilization). You can specify gateways by type, such as all or
                                             some of the VG200 gateways in your system, or by only those gateways that use a particular route pattern.

Route Patterns/Hunt Pilots

Route and Line Group Utilization - Only CAR administrators can generate the Route and Line Group Utilization report. This
                                             report provides an estimated utilization percentage of the chosen route and line group(s). You can examine the usage on the
                                             basis of each hour of a day or by a specified number of days of the week or month. Reports generate for each chosen route
                                             and line group. Use the report to analyze whether the route and line group capacity is sufficient to meet the usage requirements.
                                             Based on the results, you can decide whether additions are required. If you are load balancing gateways by using different
                                             route and line groups or route patterns and hunt lists that are assigned to the gateways, you can use this report to see the
                                             load for the whole grouping. This report also provides a convenient way of generating utilization information for a grouping
                                             of gateways by a particular route and line group; the group will also include any H.323 fallback gateways that are using the
                                             specified route and line group.

Route/Hunt List Utilization - Available for CAR administrators. The Route/Hunt List Utilization report provides an estimated
                                             utilization percentage of the chosen route/hunt list(s). You can examine the usage on the basis of each hour of a day or by
                                             a specified number of days of the week or month. Reports generate for each chosen route/hunt list. Use the report to analyze
                                             whether the route and line group capacity is sufficient to meet the usage requirements. Based on the results, you can decide
                                             whether additions are required. If you are load balancing gateways by using different route/hunt lists that are assigned to
                                             the gateways, you can use this report to see the load for the whole grouping. This report also provides a convenient way of
                                             generating utilization information for a grouping of gateways by a particular route/hunt list; the group will also include
                                             any H.323 fallback gateways that are using the chosen route/hunt list.

Route Pattern/Hunt Pilot Utilization - Available for CAR administrators. The Route Pattern/Hunt Pilot Utilization report provides
                                             an estimated utilization percentage of the chosen route pattern(s)/hunt pilot(s). You can examine the usage on the basis of
                                             each hour of a day or by a specified number of days of the week or month. Reports generate for each chosen route pattern/hunt
                                             pilot. Use the report to analyze system usage on the chosen route pattern/hunt pilot.

Hunt Pilot Summary - Only CAR administrators generate the Hunt Pilot Summary Report.The CDR Hunt Pilot Call Summary report
                                             displays the call details for the specified hunt pilot. This report displays an only an overview of the calls for the hunt
                                             pilots and hunt member information is not included. The CAR administrator can generate report for a maximum of five hunt pilot
                                             DNs.

Hunt Pilot Detail - Only CAR administrators generate the Hunt Pilot Detailed Call Report. This report displays call details
                                             for a hunt pilot number or a hunt member dn.

Conference Call Details - Available for CAR administrators. The Conference Call Details report allows you to generate and
                                       view details about conference calls and conference bridges. The Summary Report displays the summary information of conference
                                       calls within a chosen date/time range but does not contain information about each individual conference participant call leg.
                                       The Detailed Report displays the detailed information about the conference calls within a chosen date/time range and includes
                                       information about each individual conference participant call leg.

Conference Bridge Utilization - Available for CAR administrators. The Conference Bridge Utilization report provides an estimate
                                       of the utilization percentage of the conference bridge(s). You can examine the usage on the basis of each hour of a day or
                                       by a specified number of days of the week or month. Generate reports for all the conference bridges in the system. Use this
                                       report to determine the activity on the conference bridge(s) and whether you need to add additional resources. This report
                                       helps you identify usage patterns, so you can plan capacity when you discover recurring peaks in the usage pattern.

Voice Messaging Utilization - Available for CAR administrators. The Voice Messaging Utilization report provides an estimate
                                       of the utilization percentage of the voice-messaging device(s). You can examine the usage on the basis of each hour of a day
                                       or by a specified number of days of the week or month. Reports generate for each voice-messaging device. Use this report to
                                       determine the activity on the voice messaging device(s) and whether you need to add additional resources. This report helps
                                       you to identify usage patterns, so you can plan capacity when you discover recurring peaks in the usage pattern.

Trunk Utilization - Available for CAR administrators. Only CAR administrators generate the Trunk Utilization report. This
                                       report calculates the utilization reports for devices based on the duration of calls that passed through the devices. You
                                       can generate this report on an hourly, daily, or monthly basis. Reports generate for each trunk that is chosen. You can use
                                       this report for capacity assessment. You can also generate utilization reports for route groups, route lists and route patterns
                                       that are connected through trunks.

## Gateway Device Reports

CAR provides reporting capabilities for three levels of users: administrators, managers, and individual users. Only administrators
                           generate device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, and gateways.

Only CAR administrators generate the gateway reports. The following sections describe how to configure Gateway Detail, Gateway
                           Summary, and Gateway Utilization reports.

### Generate Gateway Detail Reports

Only CAR administrators generate the Gateway Detail report. Use the Gateway Detail report to track issues with specific gateways.

This section describes how to generate, view, or mail detailed information about selected gateways.

Step 1

Choose Device Reports > Gateway > Detail .

The Gateway Detail window appears.

Step 2

To display the list of gateways that you can include in the report, in the List of Gateways box perform one of the following
                                          tasks:

To display all gateways in the List of Gateways box, click Gateway Types in the column on the left side of the window.

To display gateways for a particular gateway type in the List of Gateways box, click the icon next to Gateway Types in the column on the left side of the window. The tree structure expands, and a list of gateway types displays. Choose a
                                                gateway type from the list, and the gateway name displays in the List of Gateways box.

The List of Gateways box lists up to 200 gateways that are configured for the chosen gateway type.

To display all gateways that are associated with configured route patterns/hunt pilots, click the Route/Patterns/Hunt Pilots in the column on the left side of the window.

To display gateways that use a particular route pattern, rather than a gateway type, click the icon next to Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays a list of route patterns/hunt lists.
                                                Choose a route pattern/hunt pilot from the list, and the gateway name displays in the List of Gateways box.

You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string.

Step 3

In the List of Gateways box, choose the gateways that you want to include in the report.

You can generate a report for up to five gateways at a time.

Step 4

To move the chosen gateway to the list of Selected Gateways box, click the down arrow.

The gateway or gateways that you chose appear in the Selected Gateways box.

Step 5

In the Select Call Types area, check the check boxes for the types of calls that you want to include in the report. The following table describes
                                          the call types.

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan .

Local

Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

Step 6

In the Select QoS area, check the check boxes for the voice-quality categories that you want to include in the report. The parameters that are
                                          set in the following table provide the basis for all voice-quality categories.

Voice Quality

Description

Good

QoS for these calls represents the highest possible quality.

Acceptable

QoS for these calls, although slightly degraded, still falls within an acceptable range.

Fair

QoS for these calls represents degraded quality but still within a usable range.

Poor

QoS for these calls represents unsatisfactory quality.

NA

These calls do not match any criteria for the established QoS categories.

Step 7

Choose the date range for the period for which you want to see call information.

Ensure the date and time range does not exceed one month.

Step 8

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 9

Click View Report .

Step 10

Click Send Report , if you want to mail the report. To send the report, follow the procedure that is described in the Mail Reports .

### Generate Gateway Summary Reports

Only CAR administrators generate the Gateway Summary report. This report provides a summary of all the calls that went through
                                 the gateways. You can use this information for monitoring the traffic and QoS for calls through the gateways.

You can either view reports that the system automatically generates or generate new reports. Only CAR administrators can schedule
                                 reports for automatic generation. For more information, see CAR System Parameters .

This section describes how to generate, view, or mail summary information about gateways.

Step 1

Choose Device Reports > Gateway > Summary .

The Gateway Summary window displays.

Step 2

In the Available Reports field, choose an automatically generated report (if available) and go to Step 6 or use the default setting, Generate New Report and go to Step 3 .

Step 3

In the Select Call Types area, check the check boxes for the types of calls that you want to include in the report. The following table describes
                                          the call types.

Tip

To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All .

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan .

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

Step 4

If you chose Generate New Report, choose the date range of the period for which you want to generate the report.

Step 5

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 6

Click View Report .

Step 7

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

### Generate Gateway Utilization Reports

Only CAR administrators generate the Gateway Utilization report. The report provides an estimate of the utilization percentage
                                 of the gateway for the period and not the exact utilization. For example, the system calculates the utilization of a gateway
                                 between 11hrs-12hrs, as the (sum of the duration of the calls that used the gateway in that hour / (maximum duration seconds
                                 in an hour * maximum number of ports in a gateway * number of days between the fromDate and toDate selected) * 100). Similarly,
                                 to get a utilization for the whole day, the system calculates the utilization as mentioned for each hour. You can examine
                                 the usage based on each hour of a day or on a specified number of days for each week or month.

In the case of weekly utilization reports, the system calculates the utilization as ((sum of the duration of the calls that
                                 used the gateway in a day) / (maximum duration seconds in each day * number of each day between the fromDate and toDate selected
                                 * maximum number of ports in a gateway) * 100).

In the case of monthly utilization reports, the system calculates the utilization as ((sum of the duration of the calls that
                                 used the gateway in a day) / (maximum duration seconds in each day * number of each day between the fromDate and toDate selected
                                 * maximum number of ports in a gateway) * 100).

Reports generate for each gateway that is chosen.

For calculation of the utilization of H.323 gateways, the system uses the port numbers from the CAR Gateway Configuration
                                 window. To find this window, choose System > System Parameters > Gateway Configuration . You cannot take port details for H.323 gateways from the Unified Communications Manager database because the H.323 port number always equals zero in the database. The user must update H.323 gateway ports information
                                 in the CAR Gateway Configuration window.

Be aware that the only port detail information that is taken from the CAR Gateway Configuration window is only for those gateways
                                 that do not have port details that are available or that show zero in the Unified Communications Manager database.

You can either view reports that the system automatically generates or generate new reports. Only CAR administrators can schedule
                                 reports for automatic generation. For more information, see CAR System Parameters .

This section describes how to generate, view, or mail Gateway Utilization reports.

Step 1

Choose Device Reports > Gateway > Utilization .

The Gateway Utilization window displays.

Step 2

In the Generate Reports field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 .

Day of Week

Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 .

Day of Month

Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 .

Step 3

In the Available Reports field, choose an automatically generated report (if available) and go to Step 10 or use the default Generate New Report and go to Step 4 .

Step 4

To display the list of gateways that you can include in the report in the List of Gateways box, perform one of the following
                                          tasks:

To display all gateways in the List of Gateways box, click Gateway Types in the column on the left side of the window.

To display gateways for a particular gateway type in the List of Gateways box, click the icon next to Gateway Types in the column on the left side of the window. The tree structure expands, and a list of gateway types displays. Choose a gateway
                                                type from the list, and the gateway name displays in the List of Gateways box.

The List of Gateways box will list up to 200 gateways that are configured for the chosen gateway type.

To display all gateways that are associated with configured route patterns/hunt pilots, click Route Patterns/Hunt Pilots in the column on the left side of the window.

To display gateways that use a particular route pattern, rather than a gateway type, click the icon next to Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays a list of route patterns/hunt lists.
                                                Choose a route pattern/hunt pilot from the list, and the gateway name displays in the List of Gateways box.

You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string.

Step 5

Choose a gateway type from the list.

The gateway name displays in the List of Gateways box.

The List of Gateways box will display up to 200 gateways that are configured for the chosen gateway type.

Step 6

In the List of Gateways box, choose the gateways that you want to include in the report.

You can generate a report for up to five gateways at a time.

Step 7

To move the chosen gateway to the list of Selected Gateways box, click the down arrow.

The gateway(s) that you chose displays in the Selected Gateways box.

Step 8

If you chose Generate New Report , enter the date range of the period for which you want to see call information.

Ensure the date and time range does not exceed one month.

Step 9

If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area.

Step 10

Click View Report .

Step 11

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

## Route Pattern and Hunt Pilot Device Reports

CAR provides reporting capabilities for three levels of users: administrators, managers, and individual users. Only administrators
                           generate the Route Pattern and Hunt Pilot device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, and gateways.

### Generate Route and Line Group Utilization Reports

Only CAR administrators generate the Route and Line Group Utilization report. This report provides an estimate of the maximum
                                 utilization percentage of the route and line group (cumulative utilization of all the gateways under the route and line group)
                                 for the period and not the exact utilization. The system calculates the utilization in the same manner as is done for Gateway
                                 Utilization, but this calculation gives cumulative utilization of all the gateways under the route groups and all the lines
                                 under the line groups. You can examine the usage based on each hour of a day or on a specified number of days for each week
                                 or month. Reports generate for each of the selected route and line groups.

You can either view reports that the system automatically generates or generate new reports. Only CAR administrators can schedule
                                 reports for automatic generation. For more information, see CAR System Parameters .

This section describes how to generate, view, or mail Route and Line Group Utilization reports.

Step 1

Choose Device Reports > Route Patterns/Hunt Pilots > Route and Line Group Utilization .

The Route and Line Group Utilization window displays.

Step 2

In the Generate Reports field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 .

Day of Week

Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 .

Day of Month

Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 .

Step 3

In the Available Reports field, choose an automatically generated report (if available) and go to Step 10 , or use the default setting, Generate New Report, and go to Step 4 .

Step 4

To choose only those route and line groups that use a particular route pattern, click Route Patterns/Hunt Pilots in the column on the left side of the window.

The tree structure expands and displays the route patterns/hunt lists that you chose.

You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string.

Step 5

Choose a route pattern/hunt list from the list.

The route and line groups for this route pattern/hunt list display in the List of Route/Line Groups box.

The List of Route/Line Groups box will display up to 200 route groups.

Step 6

In the List of Route/Line Groups box, choose the route/line groups that you want to include in the report.

You can generate a report for up to five route/line groups at a time.

Step 7

To move the chosen gateway to the list of Selected Route/Line Groups box, click the down arrow.

The route/line groups that you chose to display in the Selected Route Groups box.

Step 8

If you chose Generate New Report, enter the date range of the period for which you want to see call information.

Ensure the date and time range does not exceed one month.

Step 9

If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area.

Step 10

Click View Report .

Step 11

Click Send Report , if you want to mail the report. To send the report, follow the procedure that is described in the Mail Reports .

### Generate Route and Hunt List Utilization Reports

Only CAR administrators generate the Route/Hunt List Utilization report. The Route/Hunt List Utilization report provides an
                                 estimate of the maximum utilization percentage of the route/hunt list (cumulative utilization of all the gateways under the
                                 route/hunt list) for the period and not the exact utilization. The system calculates the cumulative utilization of all the
                                 gateways under the route lists and all the lines under the hunt lists.

You can examine the usage based on each hour of a day or on a specified number of days for each week or month. Reports generate
                                 for each of the selected route/hunt lists.

You can either view reports that the system automatically generates or generate new reports. Only CAR administrators can schedule
                                 reports for automatic generation. For more information, see Set Up CDR Load Schedule .

This section describes how to generate, view, or mail the Route/Hunt List Utilization reports.

Step 1

Choose Device Reports > Route Patterns/Hunt Pilots > Route/Hunt List Utilization .

The Route/Hunt List Utilization window displays.

Step 2

In the Generate Report field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 .

Day of Week

Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 .

Day of Month

Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 .

Step 3

In the Available Reports field, choose an automatically generated report (if available) and go to Step 10 or use the default setting, Generate New Report, and go to Step 4 .

Step 4

To choose the route/hunt lists that you want to include in the report, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays the route patterns/hunt pilots that
                                          you chose.

You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt lists
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string.

Step 5

Choose a route/hunt list from the list.

The route/hunt list name displays in the List of Route/Hunt Lists box.

The List of Route/Hunt Lists box will display up to 200 route/hunt lists.

Step 6

In the List of Route/Hunt Lists box, choose the route/hunt lists that you want to include in the report.

You can generate a report for up to five route/hunt lists at a time.

Step 7

To move the chosen route/hunt lists to the list of Selected Route/Hunt Lists box, click down arrow.

The route/hunt lists that you chose to display in the Selected Route/Hunt Lists box.

Step 8

If you chose Generate New Report, enter the date range of the period for which you want to see call information.

Ensure the date and time range does not exceed one month.

Step 9

If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area.

Step 10

Click View Report .

Step 11

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

### Generate Route Pattern and Hunt Pilot Utilization Reports

Only CAR administrators generate the Route Pattern/Hunt Pilot Utilization report. The report provides an estimate of the maximum
                                 utilization percentage of the route pattern/hunt pilot (cumulative utilization of all the gateways under the route pattern/hunt
                                 pilot) for the period and not the exact utilization. The system calculates the utilization of all the gateways under the route
                                 patterns and all the lines under the hunt pilots. You can examine the usage based on each hour of a day or on a specified
                                 number of days for each week or month. Reports generate for each of the selected route patterns/hunt pilots.

You can either view reports that the system automatically generates or generate new reports. Only CAR administrators can schedule
                                 reports for automatic generation. For more information, see Set Up CDR Load Schedule .

This section describes how to generate, view, or mail Route Pattern/Hunt Pilot Utilization reports.

Step 1

Choose Device Reports > Route Pattern/Hunt Pilots > Route Pattern/Hunt Pilot Utilization .

The Route Pattern/Hunt Pilot Utilization window displays.

Step 2

In the Generate Report field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 .

Day of Week

Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 .

Day of Month

Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 .

Step 3

In the Available Reports field, choose an automatically generated report (if available) and go to Step 10 or use the default Generate New Report and go to Step 4 .

Step 4

To choose the route pattern(s)/hunt list(s) that you want to include in the report, click Route Patterns/Hunt Pilots in the column on the left side of the window.

The tree structure expands and displays the route pattern(s)/hunt list(s) that you chose.

You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt list(s)
                                                         that matches the search string.

Step 5

Choose a route pattern/hunt pilot from the list.

The route pattern/hunt pilot name displays in the List of Route Patterns/Hunt Pilots box.

The List of Route Patterns/Hunt Pilots box will display up to 200 route patterns/hunt lists.

Step 6

In the List of Route Patterns/Hunt Pilots box, choose the route patterns/hunt lists that you want to include in the report.

You can generate a report for up to five route patterns/hunt pilots at a time.

Step 7

Click the down arrow to move the chosen route pattern/hunt pilot to the list of Selected Route Patterns/Hunt Pilots box.

The route pattern/hunt pilot that you chose displays in the Selected Route Patterns/Hunt Pilots box.

Step 8

If you chose Generate New Report, enter the date range of the period for which you want to see call information.

Ensure the date and time range does not exceed one month.

Step 9

If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area.

Step 10

Click View Report .

Step 11

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

### Generate Hunt Pilot Summary Report

Only CAR administrators generate the Hunt Pilot Summary Report. The CDR Hunt Pilot Call Summary report displays the call details
                                 for the specified hunt pilot. This report displays only an overview of the calls for the hunt pilots and hunt member information
                                 is not included. The CAR administrator can a generate report for a maximum of five hunt pilot DNs.

This section describes how to generate, view, or mail Hunt Pilot Summary reports.

Step 1

Choose Device Reports > Route Pattern/Hunt Pilots > Hunt Pilot Summary .

The Hunt Pilot Detail Summary displays.

Step 2

Enter the hunt pilot number in the Hunt Pilots text box and press the Enter key.

The hunt pilot number is displayed below the text box. Alternately, you can click the icon to display all the available hunt
                                             pilot numbers.

Step 3

Click on the required hunt pilot number, so that it is listed in the List of Hunt Pilots.

Step 4

From the Generate Reports drop-down list, choose:

Hour of the day - Displays the call details for each hour in a 24-hour period for the period that you specify in Step 7 .

Day of the Week - Displays the call details for the days of the week that occur within the period that you specify in Step 7 .

Day of the Month - Displays the call details for the days of the month that occur within the period that you specify in Step 7 .

Step 5

Choose any of the available reports or the Generate New Report option from the Available Reports drop-down list.

Step 6

From the list of hunt pilots available, choose the required ones and click the down arrow.

The hunt pilots chosen are displayed in the Selected Hunt Pilots list.

Step 7

Choose the From Date and the To Date from the drop-down lists available.

Step 8

Choose the required report format.

It can either be CSV or PDF . PDF is the default report option.

Step 9

Click View Report to view the report.

To view the report results, see Generate Hunt Pilot Summary Report .

Step 10

Click Send Report , if you want to mail the report.

To send the report, perform the procedure that is described in the Mail Reports .

### Generate Hunt Pilot Detail Report

Only CAR administrators generate the Hunt Pilot Detailed Call Report. This report displays call details for a hunt pilot number
                                 or a hunt member dn.

This section describes how to generate, view, or mail Hunt Pilot Detail reports.

Step 1

Choose Device Reports > Route Pattern/Hunt Pilots > Hunt Pilot Detail .

The Hunt Pilot Detail window displays.

Step 2

Select the HuntPilot or the MemberDn for generating the report.

Step 3

Enter the hunt pilot number in the Hunt Pilots text box and press the Enter key.

The hunt pilot number is displayed below the text box. Alternately, you can click the icon to display the hunt pilot numbers.

Step 4

If you had selected the hunt pilot option, click on the required hunt pilot number, so that it is listed in the SelectedHuntPilot/MemberDn list box. Proceed to Step 7 .

Step 5

If you had selected the member dn option, click on the required hunt pilot number to list the member dn numbers in it.

Step 6

From the list of member dns, click on the required ones so that they get listed in the SelectedHuntPilot/MemberDn list box.

Step 7

Choose any of the available reports or the Generate New Report option from the Available Reports drop-down list.

Step 8

Choose the From Date and the To Date from the drop-down lists available.

Step 9

Choose the required report format.

It can either be CSV or PDF. PDF is the default report option.

Step 10

Click View Report to view the report.

To view the report results, see Hunt Pilot Detail Report Results .

Step 11

Click Send Report , if you want to mail the report.

To send the report, perform the procedure that is described in the Mail Reports .

## Conference Bridge Device Reports

CAR provides reporting capabilities for three levels of users: administrators, managers, and individual users. Only CAR administrators
                           generate the conference bridge device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, and gateways.

### Generate Conference Call Details

Only CAR administrators generate the Conference Call Details report. The Conference Call Details report allows you to generate
                                 and view details about conference calls.

This section describes how to generate, view, or mail a Conference Call Details report.

Step 1

Choose Device Reports > Conference Bridge > Call Details .

The Conference Call Details window displays.

Step 2

In the Report Type drop-down menu, choose either Summary or Detail .

Step 3

In the Available Reports field, choose an automatically generated report (if available) and go to Step 7 or use the default setting, Generate New Report, and go to Step 4 .

Step 4

In Select Conference Types, check the check box of the conference type that you want to include in the report as described
                                          in the following table.

Parameter

Description

Ad-Hoc

Ad hoc conferences allow the conference controller to let only certain participants into the conference.

Meet-Me

Meet-me conferences allow users to dial in to a conference.

Step 5

If you chose Generate New Report, enter the date range of the period for which you want to see conference call details.

Ensure that the date and time range does not exceed one month.

Step 6

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want
                                          the report in PDF format.

Step 7

Click View Report .

Step 8

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

### Generate Conference Bridge Utilization Reports

Only CAR administrators generate the Conference Bridge Utilization report. The report provides an estimate of the utilization
                                 percentage of the conference bridges (cumulative utilization of all the conference bridges that are selected for OnDemand
                                 reports) for the period and not the exact utilization. For example, the system calculates the utilization of a conference
                                 bridge between 11hrs and 12hrs as the ((Sum of duration of the calls that used the conference bridge in that hour) / (Number
                                 of days between the fromDate and toDate selected * Maximum number of streams in the conference bridge * Maximum number of
                                 duration in seconds in an hour) * 100)). The value that is calculated will display in the report as the utilization for the
                                 time between 11hrs and 12hrs. You can examine the usage based on each hour of a day or on a specified number of days for each
                                 week or month.

You can either view reports that the system automatically generates or generate new reports. Only CAR administrators can schedule
                                 reports for automatic generation. For more information, see Set Up CDR Load Schedule .

This section describes how to generate, view, or mail Conference Bridge Utilization reports for each conference bridge type.

Step 1

Choose Device Reports > Conference Bridge > Utilization .

The Conference Bridge Utilization window displays.

Step 2

In the Generate Report field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 6 .

Day of Week

Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 6 .

Day of Month

Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 6 .

Step 3

In the Available Reports field, choose an automatically generated report (if available) and go to Step 8 or use the default, Generate New Report, and go to Step 4 .

Step 4

From the Conference Bridge Types column in the left pane, choose the conference bridge type(s) that you want to include in
                                          the utilization report.

The conference bridges of the particular conference bridge type that you chose to display in the List of Devices box.

For this report, choose a maximum of five conference bridges.

Step 5

When you have chosen all the conference bridges that you want to include in the report, click the down arrow to add them to
                                          the Selected Devices box.

Step 6

If you chose Generate New Report, enter the date range of the period for which you want to see call information.

Ensure the date and time range does not exceed one month.

Step 7

If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area.

Step 8

Click View Report .

Step 9

Click Send Report , if you want to mail the report. To send the report, perform the procedure described in the Mail Reports .

## Voice Messaging Utilization Device Reports

CAR provides reporting capabilities for three levels of users: administrators, managers, and individual users. Only administrators
                           generate device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, and gateways.

### Generate Voice Messaging Utilization Reports

Only CAR administrators generate the Voice Messaging Utilization report. The report provides an estimate of the maximum utilization
                                 percentage of the voice-messaging devices for the period and not the exact utilization. For example, the system calculates
                                 the utilization of a voice-messaging port/voice-messaging DNs between 11hrs and 12hrs by using the duration of the calls that
                                 used the voice-messaging port/voice messaging DNs. The system calculates utilization for the voice-messaging port as the (sum
                                 of duration of calls that used the voice-messaging port in that hour*100) / (maximum duration seconds in an hour * number
                                 of days between the fromDate and toDate selected). The utilization calculation for voice-messaging DNs represents the (sum
                                 of duration of calls that used the voice-messaging DNs in that hour * 100) / (maximum duration seconds in an hour * number
                                 of days between the fromDate and toDate selected * maximum number of ports in a gateway that is connected to the voice-messaging
                                 DN). The same value will display in the report as the utilization for the time between 11hrs and 12hrs.

You can review the Voice Messaging Utilization report for Voice Messaging Ports only as a newly generated report and not as
                                 a report that the system automatically generates.

You can automatically generate the Voice Messaging Utilization report for Voice Messaging DNs, or you can generate it as a
                                 new report. Only CAR administrators can schedule reports for automatic generation. For more information, see Set Up CDR Load Schedule .

The CAR Voice Messaging Utilization report supports the Cisco Unity and Cisco Unity Connection voice-messaging systems.

This section describes how to generate, mail, or view Voice Messaging Utilization reports.

Step 1

Choose Device Reports > Voice Messaging > Utilization .

The Voice Messaging Utilization window displays.

Step 2

In the Generate Report field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the utilization results for each hour in a 24-hour period for the period that you specify in Step 10 .

Day of Week

Displays the utilization for the days of the week that occur within the period that you specify in Step 10 .

Day of Month

Displays the utilization for the days of the month that occur within the period that you specify in Step 10 .

Step 3

In the Available Reports field, choose an automatically generated report (if available) and go to Step 12 or use the default setting, Generate New Report, and go to Step 4 .

Step 4

To choose a voice-messaging DN, click Voice Messaging DNs in the Voice Utilization pane.

The previously configured voice-messaging DN displays.

The Voice Messaging DN that displays in this window represents the Voice Messaging DN that you configure in the VoiceMailDn
                                                         service parameter, which supports the Cisco Messaging Interface service. Set the parameter name VoiceMailDn to the routing
                                                         pattern that you have created on the machine. Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the service Cisco Messaging Interface .

Step 5

Choose the voice-messaging DN.

The DN that you chose displays in the List of DNs/Ports list box.

Step 6

To choose a voice-messaging port, click Voice Messaging Ports in the Voice Utilization pane.

A list of configured voice-messaging ports displays.

Step 7

From the list of ports, choose a voice-messaging port.

The port that you chose displays in the List of DNs/Ports list box.

Step 8

In Select Voice Messaging DNs/Ports, click the down arrow.

The port that you chose displays in the Selected DNs/Ports list box.

Step 9

Repeat Step 7 and Step 8 until you have chosen the ports that you want to include in the report.

For this report, you can choose a maximum of five Voice Messaging Ports/Voice Messaging DNs. You can choose the default Voice
                                                         Messaging DN and four Voice Messaging Ports, or you can choose five Voice Messaging Ports.

Step 10

If you chose Generate New Report , enter the date range of the period for which you want to see call information.

Ensure the date and time range does not exceed one month.

Step 11

Choose CSV in the Report Format area, if you want the report in CSV format. If you want the report in PDF format, choose PDF in the Report Format area.

Step 12

Click View Report .

Step 13

Click Send Report , if you want to mail the report. To send the report, perform the procedure described in the Mail Reports .

## Trunk Device Reports

CAR provides reporting capabilities for three levels of users: administrators, managers, and individual users. Only administrators
                           generate device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, gateways, and trunks.

Only CAR administrators generate the trunk reports. The following section describes how to configure Trunk Utilization reports.

### Generate Trunk Utilization Reports

Only CAR administrators generate the Trunk Utilization report. This report calculates the utilization reports for devices
                                 based on the duration of calls that passed through the devices.

You can generate this report on an hourly, daily, or monthly basis. The system calculates the utilization of a trunk for each
                                 hour in the selected date range. For example, the system calculates the utilization of a trunk between 11hrs-12hrs, using
                                 the formula, (Sum of the duration of calls that used the trunk in that hour / (total seconds in an hour * maximum number of
                                 ports in a trunk * number of days between the fromDate and toDate selected) * 100).

Similarly, to get the utilization for each day in a week, the system calculates the utilization using the formula, ((sum of
                                 the duration of calls that used the trunk in a day) / (total seconds in each day * number of each day between the fromDate
                                 and toDate selected * maximum number of ports in a trunk) * 100).

In the case of monthly utilization reports, the system calculates the utilization for each day in a month, using the formula,
                                 ((sum of the duration of calls that used the trunk in a day) / (total seconds in each day * number of each day between the
                                 fromDate and toDate selected * maximum number of ports in a trunk) * 100).

Reports generate for each trunk that is chosen.

For calculation of the trunk utilization, the system uses the port numbers from the CAR Trunk Configuration window. To find
                                 this window, choose System > System Parameters > Trunk Configuration . You cannot take port details for H.323 trunks from the Unified Communications Manager database because the H.323 port number always equals zero in the database. The user must update H.323 trunk ports information
                                 in the CAR Trunk Configuration window.

Be aware that the only port detail information that is taken from the CAR Trunk Configuration window is only for those trunks
                                 that do not have port details that are available or that show zero in the Unified Communications Manager database.

This section describes how to generate, view, or mail Trunk Utilization reports.

Step 1

Choose Device Reports > Trunk > Utilization .

The Trunk Utilization window displays.

Step 2

In the Generate Reports field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 7 .

Day of Week

Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 7 .

Day of Month

Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 7 .

The Trunk Utilization report is not generated automatically.

Step 3

To display the list of trunks that you can include in the report in the List of Trunks box, perform one of the following tasks:

To display all trunks in the List of Trunks box, click Trunk Types in the column on the left side of the window.

To display trunks for a particular trunk type in the List of Trunks box, click the icon next to Trunk Types in the column on the left side of the window. The tree structure expands, and a list of trunk types displays. Choose a trunk
                                                type from the list, and the trunk name displays in the List of Trunks box.

The List of Trunks box will list up to 200 trunks that are configured for the chosen trunk type.

You can generate the trunk utilization reports for route groups, route lists, and route patterns that are connected through
                                                               trunks.

Step 4

Choose a trunk type from the list.

The trunk name displays in the List of Trunks box.

The List of Trunks box displays up to 200 trunks that are configured for the chosen trunk type.

Step 5

In the List of Trunks box, choose the trunks that you want to include in the report.

You can generate a report for up to five trunks at a time.

Step 6

To move the chosen trunk to the list of Selected Trunks box, click the down arrow.

The trunk(s) that you chose displays in the Selected Trunks box.

Step 7

If you chose Generate New Report , enter the date range of the period for which you want to see call information.

Ensure the date and time range does not exceed one month.

Step 8

If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area.

Step 9

Click View Report .

Step 10

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

## CAR Device Reports Results

This chapter describes report output information for each device report.

### Gateway Detail Report Results

The Gateway Detail report includes the following fields. See the table.

Field

Description

Date

The date when the call went through the gateway.

Orig. Time

The time when the call went through the gateway.

Term. Time

The time that the call terminated.

Duration(s)

The duration, in seconds, that the call was connected. The duration specifies the difference between the Dest Connect and
                                             the Dest Disconnect times.

Orig

The directory number from which the call was placed.

Dest

The directory number to which the call was originally placed. If the call was not forwarded, this directory number should
                                             match the Final Destination number. If the call was forwarded, this field contains the original destination number of the
                                             call before it was forwarded.

Orig. Codec

The codec code (compression or payload code) that the call originator used on its sending side during this call. This code
                                             may differ from the codec code that was used on its receiving side.

Dest. Codec

The codec code (compression or payload code) that the destination used on its sending side during this call. This code may
                                             differ from the codec code that was used on its receiving side.

Orig. Device

The device name of the device that placed the call. For incoming and tandem calls, this field specifies the device name of
                                             the gateway.

Dest Device

The device name of the device that received the call. For outgoing and tandem calls, this field specifies the device name
                                             of a gateway. For conference calls, this field specifies the device name of the conference bridge.

Orig QoS

QoS depicts the voice-quality grade that was achieved for the calls.

Dest QoS

The QoS category that was experienced by the receiver of the call.

Gateway Detail Report displays sample output of the Gateway Detail Report in PDF format.

### Gateway Summary Report Results

The Gateway Summary report includes the following fields. See the following table.

The Gateway Summary report segregates calls for each call classification that the user selects and divides the calls based
                                             on QoS type.

Field

Description

Call Classification

Shows the type of call (internal, incoming, and tandem.)

Quality of Service

Shows a summary of the performance of the various gateways with the total number of calls for each voice-quality category.
                                             The parameters set in the Define QoS Values provide the basis for all voice-quality categories.

Good - QoS for these calls specifies the highest possible quality.

Acceptable - QoS for these calls, although slightly degraded, still falls within an acceptable range.

Fair - QoS for these calls, although degraded, still falls within a usable range.

Poor - QoS for these calls was unsatisfactory.

NA - These calls did not match any criteria for the established QoS categories.

Calls

Shows the total calls for the particular call classification.

Duration (sec)

Shows the total duration for all the calls for the particular call classification.

The following figure displays sample output of the Gateway Summary Report in PDF format.

### Gateway and Route Utilization Report Results

The Gateway, Route Group, Route List, and Route Pattern Utilization reports provide similar output. If you choose to display
                                 the report in PDF format, the report shows the utilization as a bar chart. A graph displays for each selected gateway or route
                                 group. See the table.

Field

Description

Time/Day

Time in one-hour blocks if you chose Hourly or one-day blocks if you chose weekly or monthly. The results show the utilization
                                             for each hour or day for the entire period that is shown in the from and to dates.

%

Gateway, route group, route list, or route pattern utilization percentage. This field gives the estimated utilization percentage
                                             of the gateways or route groups or route lists or route patterns relative to the total number of calls that all the gateways
                                             put together can support at any one time.

Gateway Utilization Report displays sample output of the Gateway Utilization Report in PDF format.

Route/Hunt List Utilization Report displays sample output of the Route/Hunt List Utilization report in PDF format.

Route and Line Group Utilization Report displays sample output from the Route and Line Group Utilization report in PDF format.

Route Pattern/Hunt Path Utilization Report displays sample output of the Route Pattern/Hunt Path Utilization report in PDF format.

### Hunt Pilot Summary Report Results

The Hunt Pilot Summary report includes the following fields. See the table.

Field

Description

Time

Time in one-hour blocks if you chose Hourly or one-day blocks if you chose weekly or monthly. The results show the call details
                                             for each hour or day for the entire period that is shown in the from and to dates.

No.of Calls Presented/Received

Number of calls presented and received at the specified time duration/day.

Number of calls received = Number of calls handled + Number of calls abandoned + Number of calls Forwarded due to no Answer
                                             + Number of calls Forwarded due to Busy + Number of calls Failed.

No.of Calls Handled/Answered

Number of calls answered.

No.of Calls Abandoned (Not Answered nor Redirected)

Number of calls that went on/off hook but were never connected or answered.

No.of Calls Forwarded due to no Answer (FONA)

Number of calls that were forwarded due to no reply.

No.of Calls Forwarded due to Busy (FOB)

Number of calls that were forwarded since the receiving end was busy.

No.of Calls Failed

Number of calls that failed to go through.

Hunt Pilot Name

Lists the name of the available Hunt Pilots.

Line Number

List the line numbers of the hunt members.

Hunt Pilot Summary Report displays sample output of the Hunt Pilot Summary report in PDF format.

### Hunt Pilot Detail Report Results

The Hunt Pilot Detail report includes the following fields. See the table.

Field

Description

Date/Time connected

Date and Time when the call was received

Date/Time disconnected

Date and Time when the call ended

Duration

Time duration of the call

Calling Party

Directory number (DN) of the caller

Called Party

Hunt Pilot Directory number (DN)

Final Called Party Number

Directory Number where the call landed in the end. If the call is landed in Hunt Pilot, then it will show its member DN. Suppose
                                             the call forward is set from member DN to some other DN, it will show that DN where the call got forwarded.

The number of the hunt member is displayed only when the Show Line Group Member DN in finalCalledPartyNumber CDR Field is
                                             set to true. If the value is set to false, the Hunt Pilot DN is displayed in this field. For details on setting this parameter
                                             see, Service Parameters Configuration in Cisco Unified CM Administration Guide.

Dest. Device Name

Device identifier of the device that answered the call.

Call Answered

Indicates if the call was answered or not. Values could be Yes or No.

Call Abandoned

Indicates if the call was abandoned. Values could be Yes or No.

Call Forwarded Due to No Answer (FONA)

Indicates if the call was forwarded due to no reply. Values could be Yes or No.

Call Forwarded Due to Busy (FOB)

Indicates if the call was forwarded since the answering end was busy. Values could be Yes or No.

Call Failed

Indicates if the call failed to get through. Values could be Yes or No.

Call Reference

Identification number to trace the call. This is the globalcallid_callid value in the CDR database.

Hunt Pilot Details Report displays sample output of the Hunt Pilot Details report in the PDF format.

### Conference Call Detail Report Results

You can choose to generate Conference Call information in either a summary or a detailed report. The reports display the call
                                 details in a table when you generate the report in PDF format. The following tables show the fields in the Conference Call
                                 Detail and Summary reports. See the tables.

The report criteria include the type of conference (ad hoc and/or meet-me) and the From and To date range.

Field

Description

Orig. Time

Time that the first participant enters the conference.

Term. Time

Time that the last participant leaves the conference.

No. of Participants

Number of participants in the conference.

Duration

Sum of the duration of individual participants in the conference in seconds.

Device Name

Names of the conference devices that were used.

Field

Description

Conference Start Time

Time at which conference started.

Conference End Time

Time at which conference ended.

Connect Time

Time at which conference participants connected to conference.

Disconnect Time

Time at which conference participants disconnected from conference.

Duration

Total time of conference.

Directory Number

Directory number of participants.

Call Classification

Call types of conference (internal, incoming, and so on.)

Device Name

Names of the conference devices that were used.

QoS

Quality of service.

Conference Call Details Summary Report displays sample output of the Conference Call Details Summary report in PDF format.

### Conference Bridge Utilization Report Results

The Conference Bridge Utilization report provides the following fields. If you choose PDF format, the report shows the utilization
                                 as a table. See the table.

Field

Description

Time/Day

Time in one-hour blocks if you chose Hourly or one-day blocks if you chose day of week or daily.

% Usage

Conference bridge utilization percentage.

Conf. Bridge

The conference bridge device that is used to hold conference calls.

Type

Either hardware or software conference bridge.

Max Streams

The number of conferences that can be held at a time along with the number of people per conference.

Conference Bridge Utilization Report displays sample output of the Conference Bridge Utilization report in PDF format.

### Voice Messaging Utilization Report Results

The Voice Messaging Utilization report provides the following fields. See the table.

Field

Description

Time/Day

Time in one-hour blocks if you chose Hourly or one-day blocks if you chose day of week or daily.

% Usage

Voice-messaging percentage.

Voice Messaging Ports

The sum of the maximum number of ports for all the gateways under the route patterns that are configured for the voice-messaging
                                             systems and the entries in the Device table of Unified Communications Manager that have type Class as 8.

Voice Messaging Gateways

The originating or destination device name of the gateways under the route patterns that are configured for the voice-messaging
                                             systems.

Number of Ports

The number of ports that the voice-messaging gateway supports.

Voice Messaging Utilization Report displays sample output of the Voice Messaging Utilization report in PDF format.

### Trunk Utilization Report Results

The Trunk Utilization report provides the following fields. If you choose to display the report in PDF format, the report
                                 shows the utilization as a bar chart. A graph displays for each selected trunk. See the table.

Field

Description

Time/Day

Time in one-hour blocks if you chose Hourly or one-day blocks if you chose weekly or monthly. The results show the utilization
                                             for each hour or day for the entire period that is shown in the from and to dates.

%

Trunk utilization percentage. This field gives the estimated utilization of the trunks relative to the total number of calls
                                             that passed through the devices.

Trunk Utilization Report Sample 1 to Trunk Utilization Report Sample 4 display sample output pages of the Trunk Utilization Report in PDF format.

| Step 1 | Choose Device Reports > Gateway > Detail . The Gateway Detail window appears. |
|---|---|
| Step 2 | To display the list of gateways that you can include in the report, in the List of Gateways box perform one of the following
                                          tasks: To display all gateways in the List of Gateways box, click Gateway Types in the column on the left side of the window. To display gateways for a particular gateway type in the List of Gateways box, click the icon next to Gateway Types in the column on the left side of the window. The tree structure expands, and a list of gateway types displays. Choose a
                                                gateway type from the list, and the gateway name displays in the List of Gateways box. Note The List of Gateways box lists up to 200 gateways that are configured for the chosen gateway type. To display all gateways that are associated with configured route patterns/hunt pilots, click the Route/Patterns/Hunt Pilots in the column on the left side of the window. To display gateways that use a particular route pattern, rather than a gateway type, click the icon next to Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays a list of route patterns/hunt lists.
                                                Choose a route pattern/hunt pilot from the list, and the gateway name displays in the List of Gateways box. Note You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. | Note | The List of Gateways box lists up to 200 gateways that are configured for the chosen gateway type. | Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
| Note | The List of Gateways box lists up to 200 gateways that are configured for the chosen gateway type. |
| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
| Step 3 | In the List of Gateways box, choose the gateways that you want to include in the report. Note You can generate a report for up to five gateways at a time. | Note | You can generate a report for up to five gateways at a time. |
| Note | You can generate a report for up to five gateways at a time. |
| Step 4 | To move the chosen gateway to the list of Selected Gateways box, click the down arrow. The gateway or gateways that you chose appear in the Selected Gateways box. |
| Step 5 | In the Select Call Types area, check the check boxes for the types of calls that you want to include in the report. The following table describes
                                          the call types. Table 1. Gateway Details by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . Local Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . | Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Step 6 | In the Select QoS area, check the check boxes for the voice-quality categories that you want to include in the report. The parameters that are
                                          set in the following table provide the basis for all voice-quality categories. Table 2. Gateway Detail Voice Quality Voice Quality Description Good QoS for these calls represents the highest possible quality. Acceptable QoS for these calls, although slightly degraded, still falls within an acceptable range. Fair QoS for these calls represents degraded quality but still within a usable range. Poor QoS for these calls represents unsatisfactory quality. NA These calls do not match any criteria for the established QoS categories. | Voice Quality | Description | Good | QoS for these calls represents the highest possible quality. | Acceptable | QoS for these calls, although slightly degraded, still falls within an acceptable range. | Fair | QoS for these calls represents degraded quality but still within a usable range. | Poor | QoS for these calls represents unsatisfactory quality. | NA | These calls do not match any criteria for the established QoS categories. |
| Voice Quality | Description |
| Good | QoS for these calls represents the highest possible quality. |
| Acceptable | QoS for these calls, although slightly degraded, still falls within an acceptable range. |
| Fair | QoS for these calls represents degraded quality but still within a usable range. |
| Poor | QoS for these calls represents unsatisfactory quality. |
| NA | These calls do not match any criteria for the established QoS categories. |
| Step 7 | Choose the date range for the period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 8 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 9 | Click View Report . |
| Step 10 | Click Send Report , if you want to mail the report. To send the report, follow the procedure that is described in the Mail Reports . |

| Note | The List of Gateways box lists up to 200 gateways that are configured for the chosen gateway type. |
|---|---|

| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
|---|---|

| Note | You can generate a report for up to five gateways at a time. |
|---|---|

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |

| Voice Quality | Description |
|---|---|
| Good | QoS for these calls represents the highest possible quality. |
| Acceptable | QoS for these calls, although slightly degraded, still falls within an acceptable range. |
| Fair | QoS for these calls represents degraded quality but still within a usable range. |
| Poor | QoS for these calls represents unsatisfactory quality. |
| NA | These calls do not match any criteria for the established QoS categories. |

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Gateway > Summary . The Gateway Summary window displays. |
|---|---|
| Step 2 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 6 or use the default setting, Generate New Report and go to Step 3 . |
| Step 3 | In the Select Call Types area, check the check boxes for the types of calls that you want to include in the report. The following table describes
                                          the call types. Tip To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All . Table 3. Gateway Summary by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free numbers or emergency calls such as 911. | Tip | To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All . | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Tip | To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All . |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Step 4 | If you chose Generate New Report, choose the date range of the period for which you want to generate the report. |
| Step 5 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 6 | Click View Report . |
| Step 7 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Tip | To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All . |
|---|---|

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |

| Step 1 | Choose Device Reports > Gateway > Utilization . The Gateway Utilization window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the following table. Table 4. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . Day of Week Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . Day of Month Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . | Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . | Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |
| Step 3 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 10 or use the default Generate New Report and go to Step 4 . |
| Step 4 | To display the list of gateways that you can include in the report in the List of Gateways box, perform one of the following
                                          tasks: To display all gateways in the List of Gateways box, click Gateway Types in the column on the left side of the window. To display gateways for a particular gateway type in the List of Gateways box, click the icon next to Gateway Types in the column on the left side of the window. The tree structure expands, and a list of gateway types displays. Choose a gateway
                                                type from the list, and the gateway name displays in the List of Gateways box. Note The List of Gateways box will list up to 200 gateways that are configured for the chosen gateway type. To display all gateways that are associated with configured route patterns/hunt pilots, click Route Patterns/Hunt Pilots in the column on the left side of the window. To display gateways that use a particular route pattern, rather than a gateway type, click the icon next to Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays a list of route patterns/hunt lists.
                                                Choose a route pattern/hunt pilot from the list, and the gateway name displays in the List of Gateways box. Note You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. | Note | The List of Gateways box will list up to 200 gateways that are configured for the chosen gateway type. | Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
| Note | The List of Gateways box will list up to 200 gateways that are configured for the chosen gateway type. |
| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
| Step 5 | Choose a gateway type from the list. The gateway name displays in the List of Gateways box. Note The List of Gateways box will display up to 200 gateways that are configured for the chosen gateway type. | Note | The List of Gateways box will display up to 200 gateways that are configured for the chosen gateway type. |
| Note | The List of Gateways box will display up to 200 gateways that are configured for the chosen gateway type. |
| Step 6 | In the List of Gateways box, choose the gateways that you want to include in the report. Note You can generate a report for up to five gateways at a time. | Note | You can generate a report for up to five gateways at a time. |
| Note | You can generate a report for up to five gateways at a time. |
| Step 7 | To move the chosen gateway to the list of Selected Gateways box, click the down arrow. The gateway(s) that you chose displays in the Selected Gateways box. |
| Step 8 | If you chose Generate New Report , enter the date range of the period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 9 | If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area. |
| Step 10 | Click View Report . |
| Step 11 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |

| Note | The List of Gateways box will list up to 200 gateways that are configured for the chosen gateway type. |
|---|---|

| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               list(s) that matches the search string. |
|---|---|

| Note | The List of Gateways box will display up to 200 gateways that are configured for the chosen gateway type. |
|---|---|

| Note | You can generate a report for up to five gateways at a time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Route Patterns/Hunt Pilots > Route and Line Group Utilization . The Route and Line Group Utilization window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the following table. Table 5. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . Day of Week Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . Day of Month Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . | Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . | Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |
| Step 3 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 10 , or use the default setting, Generate New Report, and go to Step 4 . |
| Step 4 | To choose only those route and line groups that use a particular route pattern, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays the route patterns/hunt lists that you chose. Note You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string. | Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string. |
| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string. |
| Step 5 | Choose a route pattern/hunt list from the list. The route and line groups for this route pattern/hunt list display in the List of Route/Line Groups box. Note The List of Route/Line Groups box will display up to 200 route groups. | Note | The List of Route/Line Groups box will display up to 200 route groups. |
| Note | The List of Route/Line Groups box will display up to 200 route groups. |
| Step 6 | In the List of Route/Line Groups box, choose the route/line groups that you want to include in the report. Note You can generate a report for up to five route/line groups at a time. | Note | You can generate a report for up to five route/line groups at a time. |
| Note | You can generate a report for up to five route/line groups at a time. |
| Step 7 | To move the chosen gateway to the list of Selected Route/Line Groups box, click the down arrow. The route/line groups that you chose to display in the Selected Route Groups box. |
| Step 8 | If you chose Generate New Report, enter the date range of the period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 9 | If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area. |
| Step 10 | Click View Report . |
| Step 11 | Click Send Report , if you want to mail the report. To send the report, follow the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |

| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string. |
|---|---|

| Note | The List of Route/Line Groups box will display up to 200 route groups. |
|---|---|

| Note | You can generate a report for up to five route/line groups at a time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Route Patterns/Hunt Pilots > Route/Hunt List Utilization . The Route/Hunt List Utilization window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the following table. Table 6. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . Day of Week Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . Day of Month Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . | Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . | Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |
| Step 3 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 10 or use the default setting, Generate New Report, and go to Step 4 . |
| Step 4 | To choose the route/hunt lists that you want to include in the report, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays the route patterns/hunt pilots that
                                          you chose. Note You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt lists
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string. | Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt lists
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string. |
| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt lists
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string. |
| Step 5 | Choose a route/hunt list from the list. The route/hunt list name displays in the List of Route/Hunt Lists box. Note The List of Route/Hunt Lists box will display up to 200 route/hunt lists. | Note | The List of Route/Hunt Lists box will display up to 200 route/hunt lists. |
| Note | The List of Route/Hunt Lists box will display up to 200 route/hunt lists. |
| Step 6 | In the List of Route/Hunt Lists box, choose the route/hunt lists that you want to include in the report. Note You can generate a report for up to five route/hunt lists at a time. | Note | You can generate a report for up to five route/hunt lists at a time. |
| Note | You can generate a report for up to five route/hunt lists at a time. |
| Step 7 | To move the chosen route/hunt lists to the list of Selected Route/Hunt Lists box, click down arrow. The route/hunt lists that you chose to display in the Selected Route/Hunt Lists box. |
| Step 8 | If you chose Generate New Report, enter the date range of the period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 9 | If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area. |
| Step 10 | Click View Report . |
| Step 11 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |

| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt lists
                                                         in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                         list(s) that matches the search string. |
|---|---|

| Note | The List of Route/Hunt Lists box will display up to 200 route/hunt lists. |
|---|---|

| Note | You can generate a report for up to five route/hunt lists at a time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Route Pattern/Hunt Pilots > Route Pattern/Hunt Pilot Utilization . The Route Pattern/Hunt Pilot Utilization window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the following table. Table 7. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . Day of Week Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . Day of Month Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . | Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . | Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |
| Step 3 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 10 or use the default Generate New Report and go to Step 4 . |
| Step 4 | To choose the route pattern(s)/hunt list(s) that you want to include in the report, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays the route pattern(s)/hunt list(s) that you chose. Note You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt list(s)
                                                         that matches the search string. | Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt list(s)
                                                         that matches the search string. |
| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt list(s)
                                                         that matches the search string. |
| Step 5 | Choose a route pattern/hunt pilot from the list. The route pattern/hunt pilot name displays in the List of Route Patterns/Hunt Pilots box. Note The List of Route Patterns/Hunt Pilots box will display up to 200 route patterns/hunt lists. | Note | The List of Route Patterns/Hunt Pilots box will display up to 200 route patterns/hunt lists. |
| Note | The List of Route Patterns/Hunt Pilots box will display up to 200 route patterns/hunt lists. |
| Step 6 | In the List of Route Patterns/Hunt Pilots box, choose the route patterns/hunt lists that you want to include in the report. Note You can generate a report for up to five route patterns/hunt pilots at a time. | Note | You can generate a report for up to five route patterns/hunt pilots at a time. |
| Note | You can generate a report for up to five route patterns/hunt pilots at a time. |
| Step 7 | Click the down arrow to move the chosen route pattern/hunt pilot to the list of Selected Route Patterns/Hunt Pilots box. The route pattern/hunt pilot that you chose displays in the Selected Route Patterns/Hunt Pilots box. |
| Step 8 | If you chose Generate New Report, enter the date range of the period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 9 | If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area. |
| Step 10 | Click View Report . |
| Step 11 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 8 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 8 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 8 . |

| Note | You can also search for specific route patterns/hunt lists by entering part of the name of the route pattern(s)/hunt list(s)
                                                         in the Route Patterns box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt list(s)
                                                         that matches the search string. |
|---|---|

| Note | The List of Route Patterns/Hunt Pilots box will display up to 200 route patterns/hunt lists. |
|---|---|

| Note | You can generate a report for up to five route patterns/hunt pilots at a time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Route Pattern/Hunt Pilots > Hunt Pilot Summary . The Hunt Pilot Detail Summary displays. |
|---|---|
| Step 2 | Enter the hunt pilot number in the Hunt Pilots text box and press the Enter key. The hunt pilot number is displayed below the text box. Alternately, you can click the icon to display all the available hunt
                                             pilot numbers. |
| Step 3 | Click on the required hunt pilot number, so that it is listed in the List of Hunt Pilots. |
| Step 4 | From the Generate Reports drop-down list, choose: Hour of the day - Displays the call details for each hour in a 24-hour period for the period that you specify in Step 7 . Day of the Week - Displays the call details for the days of the week that occur within the period that you specify in Step 7 . Day of the Month - Displays the call details for the days of the month that occur within the period that you specify in Step 7 . |
| Step 5 | Choose any of the available reports or the Generate New Report option from the Available Reports drop-down list. |
| Step 6 | From the list of hunt pilots available, choose the required ones and click the down arrow. The hunt pilots chosen are displayed in the Selected Hunt Pilots list. |
| Step 7 | Choose the From Date and the To Date from the drop-down lists available. |
| Step 8 | Choose the required report format. It can either be CSV or PDF . PDF is the default report option. |
| Step 9 | Click View Report to view the report. To view the report results, see Generate Hunt Pilot Summary Report . |
| Step 10 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Step 1 | Choose Device Reports > Route Pattern/Hunt Pilots > Hunt Pilot Detail . The Hunt Pilot Detail window displays. |
|---|---|
| Step 2 | Select the HuntPilot or the MemberDn for generating the report. |
| Step 3 | Enter the hunt pilot number in the Hunt Pilots text box and press the Enter key. The hunt pilot number is displayed below the text box. Alternately, you can click the icon to display the hunt pilot numbers. |
| Step 4 | If you had selected the hunt pilot option, click on the required hunt pilot number, so that it is listed in the SelectedHuntPilot/MemberDn list box. Proceed to Step 7 . |
| Step 5 | If you had selected the member dn option, click on the required hunt pilot number to list the member dn numbers in it. |
| Step 6 | From the list of member dns, click on the required ones so that they get listed in the SelectedHuntPilot/MemberDn list box. |
| Step 7 | Choose any of the available reports or the Generate New Report option from the Available Reports drop-down list. |
| Step 8 | Choose the From Date and the To Date from the drop-down lists available. |
| Step 9 | Choose the required report format. It can either be CSV or PDF. PDF is the default report option. |
| Step 10 | Click View Report to view the report. To view the report results, see Hunt Pilot Detail Report Results . |
| Step 11 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Step 1 | Choose Device Reports > Conference Bridge > Call Details . The Conference Call Details window displays. |
|---|---|
| Step 2 | In the Report Type drop-down menu, choose either Summary or Detail . |
| Step 3 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 7 or use the default setting, Generate New Report, and go to Step 4 . |
| Step 4 | In Select Conference Types, check the check box of the conference type that you want to include in the report as described
                                          in the following table. Table 8. Conference Calls Detail Fields Parameter Description Ad-Hoc Ad hoc conferences allow the conference controller to let only certain participants into the conference. Meet-Me Meet-me conferences allow users to dial in to a conference. | Parameter | Description | Ad-Hoc | Ad hoc conferences allow the conference controller to let only certain participants into the conference. | Meet-Me | Meet-me conferences allow users to dial in to a conference. |
| Parameter | Description |
| Ad-Hoc | Ad hoc conferences allow the conference controller to let only certain participants into the conference. |
| Meet-Me | Meet-me conferences allow users to dial in to a conference. |
| Step 5 | If you chose Generate New Report, enter the date range of the period for which you want to see conference call details. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Step 6 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want
                                          the report in PDF format. |
| Step 7 | Click View Report . |
| Step 8 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Ad-Hoc | Ad hoc conferences allow the conference controller to let only certain participants into the conference. |
| Meet-Me | Meet-me conferences allow users to dial in to a conference. |

| Note | Ensure that the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Conference Bridge > Utilization . The Conference Bridge Utilization window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the following table. Table 9. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 6 . Day of Week Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 6 . Day of Month Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 6 . | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 6 . | Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 6 . | Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 6 . |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 6 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 6 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 6 . |
| Step 3 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 8 or use the default, Generate New Report, and go to Step 4 . |
| Step 4 | From the Conference Bridge Types column in the left pane, choose the conference bridge type(s) that you want to include in
                                          the utilization report. The conference bridges of the particular conference bridge type that you chose to display in the List of Devices box. Note For this report, choose a maximum of five conference bridges. | Note | For this report, choose a maximum of five conference bridges. |
| Note | For this report, choose a maximum of five conference bridges. |
| Step 5 | When you have chosen all the conference bridges that you want to include in the report, click the down arrow to add them to
                                          the Selected Devices box. |
| Step 6 | If you chose Generate New Report, enter the date range of the period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 7 | If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area. |
| Step 8 | Click View Report . |
| Step 9 | Click Send Report , if you want to mail the report. To send the report, perform the procedure described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 6 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 6 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 6 . |

| Note | For this report, choose a maximum of five conference bridges. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Note | The CAR Voice Messaging Utilization report supports the Cisco Unity and Cisco Unity Connection voice-messaging systems. |
|---|---|

| Step 1 | Choose Device Reports > Voice Messaging > Utilization . The Voice Messaging Utilization window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the following table. Table 10. Generate Report Fields Parameter Description Hour of Day Displays the utilization results for each hour in a 24-hour period for the period that you specify in Step 10 . Day of Week Displays the utilization for the days of the week that occur within the period that you specify in Step 10 . Day of Month Displays the utilization for the days of the month that occur within the period that you specify in Step 10 . | Parameter | Description | Hour of Day | Displays the utilization results for each hour in a 24-hour period for the period that you specify in Step 10 . | Day of Week | Displays the utilization for the days of the week that occur within the period that you specify in Step 10 . | Day of Month | Displays the utilization for the days of the month that occur within the period that you specify in Step 10 . |
| Parameter | Description |
| Hour of Day | Displays the utilization results for each hour in a 24-hour period for the period that you specify in Step 10 . |
| Day of Week | Displays the utilization for the days of the week that occur within the period that you specify in Step 10 . |
| Day of Month | Displays the utilization for the days of the month that occur within the period that you specify in Step 10 . |
| Step 3 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 12 or use the default setting, Generate New Report, and go to Step 4 . |
| Step 4 | To choose a voice-messaging DN, click Voice Messaging DNs in the Voice Utilization pane. The previously configured voice-messaging DN displays. Note The Voice Messaging DN that displays in this window represents the Voice Messaging DN that you configure in the VoiceMailDn
                                                         service parameter, which supports the Cisco Messaging Interface service. Set the parameter name VoiceMailDn to the routing
                                                         pattern that you have created on the machine. Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the service Cisco Messaging Interface . | Note | The Voice Messaging DN that displays in this window represents the Voice Messaging DN that you configure in the VoiceMailDn
                                                         service parameter, which supports the Cisco Messaging Interface service. Set the parameter name VoiceMailDn to the routing
                                                         pattern that you have created on the machine. Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the service Cisco Messaging Interface . |
| Note | The Voice Messaging DN that displays in this window represents the Voice Messaging DN that you configure in the VoiceMailDn
                                                         service parameter, which supports the Cisco Messaging Interface service. Set the parameter name VoiceMailDn to the routing
                                                         pattern that you have created on the machine. Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the service Cisco Messaging Interface . |
| Step 5 | Choose the voice-messaging DN. The DN that you chose displays in the List of DNs/Ports list box. |
| Step 6 | To choose a voice-messaging port, click Voice Messaging Ports in the Voice Utilization pane. A list of configured voice-messaging ports displays. |
| Step 7 | From the list of ports, choose a voice-messaging port. The port that you chose displays in the List of DNs/Ports list box. |
| Step 8 | In Select Voice Messaging DNs/Ports, click the down arrow. The port that you chose displays in the Selected DNs/Ports list box. |
| Step 9 | Repeat Step 7 and Step 8 until you have chosen the ports that you want to include in the report. Note For this report, you can choose a maximum of five Voice Messaging Ports/Voice Messaging DNs. You can choose the default Voice
                                                         Messaging DN and four Voice Messaging Ports, or you can choose five Voice Messaging Ports. | Note | For this report, you can choose a maximum of five Voice Messaging Ports/Voice Messaging DNs. You can choose the default Voice
                                                         Messaging DN and four Voice Messaging Ports, or you can choose five Voice Messaging Ports. |
| Note | For this report, you can choose a maximum of five Voice Messaging Ports/Voice Messaging DNs. You can choose the default Voice
                                                         Messaging DN and four Voice Messaging Ports, or you can choose five Voice Messaging Ports. |
| Step 10 | If you chose Generate New Report , enter the date range of the period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 11 | Choose CSV in the Report Format area, if you want the report in CSV format. If you want the report in PDF format, choose PDF in the Report Format area. |
| Step 12 | Click View Report . |
| Step 13 | Click Send Report , if you want to mail the report. To send the report, perform the procedure described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the utilization results for each hour in a 24-hour period for the period that you specify in Step 10 . |
| Day of Week | Displays the utilization for the days of the week that occur within the period that you specify in Step 10 . |
| Day of Month | Displays the utilization for the days of the month that occur within the period that you specify in Step 10 . |

| Note | The Voice Messaging DN that displays in this window represents the Voice Messaging DN that you configure in the VoiceMailDn
                                                         service parameter, which supports the Cisco Messaging Interface service. Set the parameter name VoiceMailDn to the routing
                                                         pattern that you have created on the machine. Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the service Cisco Messaging Interface . |
|---|---|

| Note | For this report, you can choose a maximum of five Voice Messaging Ports/Voice Messaging DNs. You can choose the default Voice
                                                         Messaging DN and four Voice Messaging Ports, or you can choose five Voice Messaging Ports. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Step 1 | Choose Device Reports > Trunk > Utilization . The Trunk Utilization window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the following table. Table 11. Generate Report Fields Parameter Description Hour of Day Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 7 . Day of Week Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 7 . Day of Month Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 7 . Note The Trunk Utilization report is not generated automatically. | Parameter | Description | Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 7 . | Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 7 . | Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 7 . | Note | The Trunk Utilization report is not generated automatically. |
| Parameter | Description |
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 7 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 7 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 7 . |
| Note | The Trunk Utilization report is not generated automatically. |
| Step 3 | To display the list of trunks that you can include in the report in the List of Trunks box, perform one of the following tasks: To display all trunks in the List of Trunks box, click Trunk Types in the column on the left side of the window. To display trunks for a particular trunk type in the List of Trunks box, click the icon next to Trunk Types in the column on the left side of the window. The tree structure expands, and a list of trunk types displays. Choose a trunk
                                                type from the list, and the trunk name displays in the List of Trunks box. Note The List of Trunks box will list up to 200 trunks that are configured for the chosen trunk type. Note You can generate the trunk utilization reports for route groups, route lists, and route patterns that are connected through
                                                               trunks. | Note | The List of Trunks box will list up to 200 trunks that are configured for the chosen trunk type. | Note | You can generate the trunk utilization reports for route groups, route lists, and route patterns that are connected through
                                                               trunks. |
| Note | The List of Trunks box will list up to 200 trunks that are configured for the chosen trunk type. |
| Note | You can generate the trunk utilization reports for route groups, route lists, and route patterns that are connected through
                                                               trunks. |
| Step 4 | Choose a trunk type from the list. The trunk name displays in the List of Trunks box. Note The List of Trunks box displays up to 200 trunks that are configured for the chosen trunk type. | Note | The List of Trunks box displays up to 200 trunks that are configured for the chosen trunk type. |
| Note | The List of Trunks box displays up to 200 trunks that are configured for the chosen trunk type. |
| Step 5 | In the List of Trunks box, choose the trunks that you want to include in the report. Note You can generate a report for up to five trunks at a time. | Note | You can generate a report for up to five trunks at a time. |
| Note | You can generate a report for up to five trunks at a time. |
| Step 6 | To move the chosen trunk to the list of Selected Trunks box, click the down arrow. The trunk(s) that you chose displays in the Selected Trunks box. |
| Step 7 | If you chose Generate New Report , enter the date range of the period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 8 | If you want the report in CSV format, choose CSV in the Report Format area. If you want the report in PDF format, choose PDF in the Report Format area. |
| Step 9 | Click View Report . |
| Step 10 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the cumulative utilization for each hour in a 24-hour period for the period that you specify in Step 7 . |
| Day of Week | Displays the cumulative utilization for the days of the week that occur within the period that you specify in Step 7 . |
| Day of Month | Displays the cumulative utilization for the days of the month that occur within the period that you specify in Step 7 . |

| Note | The Trunk Utilization report is not generated automatically. |
|---|---|

| Note | The List of Trunks box will list up to 200 trunks that are configured for the chosen trunk type. |
|---|---|

| Note | You can generate the trunk utilization reports for route groups, route lists, and route patterns that are connected through
                                                               trunks. |
|---|---|

| Note | The List of Trunks box displays up to 200 trunks that are configured for the chosen trunk type. |
|---|---|

| Note | You can generate a report for up to five trunks at a time. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|

| Field | Description |
|---|---|
| Date | The date when the call went through the gateway. |
| Orig. Time | The time when the call went through the gateway. |
| Term. Time | The time that the call terminated. |
| Duration(s) | The duration, in seconds, that the call was connected. The duration specifies the difference between the Dest Connect and
                                             the Dest Disconnect times. |
| Orig | The directory number from which the call was placed. |
| Dest | The directory number to which the call was originally placed. If the call was not forwarded, this directory number should
                                             match the Final Destination number. If the call was forwarded, this field contains the original destination number of the
                                             call before it was forwarded. |
| Orig. Codec | The codec code (compression or payload code) that the call originator used on its sending side during this call. This code
                                             may differ from the codec code that was used on its receiving side. |
| Dest. Codec | The codec code (compression or payload code) that the destination used on its sending side during this call. This code may
                                             differ from the codec code that was used on its receiving side. |
| Orig. Device | The device name of the device that placed the call. For incoming and tandem calls, this field specifies the device name of
                                             the gateway. |
| Dest Device | The device name of the device that received the call. For outgoing and tandem calls, this field specifies the device name
                                             of a gateway. For conference calls, this field specifies the device name of the conference bridge. |
| Orig QoS | QoS depicts the voice-quality grade that was achieved for the calls. |
| Dest QoS | The QoS category that was experienced by the receiver of the call. |

| Note | The Gateway Summary report segregates calls for each call classification that the user selects and divides the calls based
                                             on QoS type. |
|---|---|

| Field | Description |
|---|---|
| Call Classification | Shows the type of call (internal, incoming, and tandem.) |
| Quality of Service | Shows a summary of the performance of the various gateways with the total number of calls for each voice-quality category.
                                             The parameters set in the Define QoS Values provide the basis for all voice-quality categories. Good - QoS for these calls specifies the highest possible quality. Acceptable - QoS for these calls, although slightly degraded, still falls within an acceptable range. Fair - QoS for these calls, although degraded, still falls within a usable range. Poor - QoS for these calls was unsatisfactory. NA - These calls did not match any criteria for the established QoS categories. |
| Calls | Shows the total calls for the particular call classification. |
| Duration (sec) | Shows the total duration for all the calls for the particular call classification. |

| Field | Description |
|---|---|
| Time/Day | Time in one-hour blocks if you chose Hourly or one-day blocks if you chose weekly or monthly. The results show the utilization
                                             for each hour or day for the entire period that is shown in the from and to dates. |
| % | Gateway, route group, route list, or route pattern utilization percentage. This field gives the estimated utilization percentage
                                             of the gateways or route groups or route lists or route patterns relative to the total number of calls that all the gateways
                                             put together can support at any one time. |

| Field | Description |
|---|---|
| Time | Time in one-hour blocks if you chose Hourly or one-day blocks if you chose weekly or monthly. The results show the call details
                                             for each hour or day for the entire period that is shown in the from and to dates. |
| No.of Calls Presented/Received | Number of calls presented and received at the specified time duration/day. Number of calls received = Number of calls handled + Number of calls abandoned + Number of calls Forwarded due to no Answer
                                             + Number of calls Forwarded due to Busy + Number of calls Failed. |
| No.of Calls Handled/Answered | Number of calls answered. |
| No.of Calls Abandoned (Not Answered nor Redirected) | Number of calls that went on/off hook but were never connected or answered. |
| No.of Calls Forwarded due to no Answer (FONA) | Number of calls that were forwarded due to no reply. |
| No.of Calls Forwarded due to Busy (FOB) | Number of calls that were forwarded since the receiving end was busy. |
| No.of Calls Failed | Number of calls that failed to go through. |
| Hunt Pilot Name | Lists the name of the available Hunt Pilots. |
| Line Number | List the line numbers of the hunt members. |

| Field | Description |
|---|---|
| Date/Time connected | Date and Time when the call was received |
| Date/Time disconnected | Date and Time when the call ended |
| Duration | Time duration of the call |
| Calling Party | Directory number (DN) of the caller |
| Called Party | Hunt Pilot Directory number (DN) |
| Final Called Party Number | Directory Number where the call landed in the end. If the call is landed in Hunt Pilot, then it will show its member DN. Suppose
                                             the call forward is set from member DN to some other DN, it will show that DN where the call got forwarded. The number of the hunt member is displayed only when the Show Line Group Member DN in finalCalledPartyNumber CDR Field is
                                             set to true. If the value is set to false, the Hunt Pilot DN is displayed in this field. For details on setting this parameter
                                             see, Service Parameters Configuration in Cisco Unified CM Administration Guide. |
| Dest. Device Name | Device identifier of the device that answered the call. |
| Call Answered | Indicates if the call was answered or not. Values could be Yes or No. |
| Call Abandoned | Indicates if the call was abandoned. Values could be Yes or No. |
| Call Forwarded Due to No Answer (FONA) | Indicates if the call was forwarded due to no reply. Values could be Yes or No. |
| Call Forwarded Due to Busy (FOB) | Indicates if the call was forwarded since the answering end was busy. Values could be Yes or No. |
| Call Failed | Indicates if the call failed to get through. Values could be Yes or No. |
| Call Reference | Identification number to trace the call. This is the globalcallid_callid value in the CDR database. |

| Note | The report criteria include the type of conference (ad hoc and/or meet-me) and the From and To date range. |
|---|---|

| Field | Description |
|---|---|
| Orig. Time | Time that the first participant enters the conference. |
| Term. Time | Time that the last participant leaves the conference. |
| No. of Participants | Number of participants in the conference. |
| Duration | Sum of the duration of individual participants in the conference in seconds. |
| Device Name | Names of the conference devices that were used. |

| Field | Description |
|---|---|
| Conference Start Time | Time at which conference started. |
| Conference End Time | Time at which conference ended. |
| Connect Time | Time at which conference participants connected to conference. |
| Disconnect Time | Time at which conference participants disconnected from conference. |
| Duration | Total time of conference. |
| Directory Number | Directory number of participants. |
| Call Classification | Call types of conference (internal, incoming, and so on.) |
| Device Name | Names of the conference devices that were used. |
| QoS | Quality of service. |

| Field | Description |
|---|---|
| Time/Day | Time in one-hour blocks if you chose Hourly or one-day blocks if you chose day of week or daily. |
| % Usage | Conference bridge utilization percentage. |
| Conf. Bridge | The conference bridge device that is used to hold conference calls. |
| Type | Either hardware or software conference bridge. |
| Max Streams | The number of conferences that can be held at a time along with the number of people per conference. |

| Field | Description |
|---|---|
| Time/Day | Time in one-hour blocks if you chose Hourly or one-day blocks if you chose day of week or daily. |
| % Usage | Voice-messaging percentage. |
| Voice Messaging Ports | The sum of the maximum number of ports for all the gateways under the route patterns that are configured for the voice-messaging
                                             systems and the entries in the Device table of Unified Communications Manager that have type Class as 8. |
| Voice Messaging Gateways | The originating or destination device name of the gateways under the route patterns that are configured for the voice-messaging
                                             systems. |
| Number of Ports | The number of ports that the voice-messaging gateway supports. |

| Field | Description |
|---|---|
| Time/Day | Time in one-hour blocks if you chose Hourly or one-day blocks if you chose weekly or monthly. The results show the utilization
                                             for each hour or day for the entire period that is shown in the from and to dates. |
| % | Trunk utilization percentage. This field gives the estimated utilization of the trunks relative to the total number of calls
                                             that passed through the devices. |