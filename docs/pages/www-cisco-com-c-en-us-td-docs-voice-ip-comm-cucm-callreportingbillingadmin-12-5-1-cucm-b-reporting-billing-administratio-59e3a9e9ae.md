---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-callreportingbillingadmin-12-5-1-cucm-b-reporting-billing-administratio-59e3a9e9ae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/callReportingBillingAdmin/12_5_1/cucm_b_reporting-billing-administration-guide-1251SU1/cucm_b_reporting-and-billing-administration-guide_chapter_011.html
retrieved_at: 2026-08-21T01:14:57.159041+00:00
---

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: October 9, 2024

Chapter: System Reports

## Chapter: System Reports

# System Reports

## CAR System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help with call monitoring for budgeting or security purposes
                                 and for determining the voice quality of the calls.

Individual users - Generate a billing report for calls of each user.

You may have access restrictions to view some reports depending on your job function.

### System Reports Summary Description

CDR Analysis and Reporting provide system reports for managers and CAR administrators. Managers or CAR administrators can
                                 access the QoS summary report. Only CAR administrators can access all other reports. This section describes the following
                                 reports:

QoS

Detail - Available for CAR administrators. The QoS detail report provides the QoS ratings that are attributed to inbound and
                                             outbound calls on the Unified Communications Manager network for the period that you specify. Use this report to help monitor the voice quality of all calls on a user-level basis
                                             for the entire system. The call details in CDRs and CMRs and the QoS parameters that you choose provide the basis for assigning
                                             a particular voice-quality category to a call.

Summary - Available for managers and CAR administrators. This report provides a two-dimensional pie chart that shows the distribution
                                             of QoS grades that are achieved for the specified call classifications and period. The report also provides a table that summarizes
                                             the calls for each QoS. The call details in CDRs and CMRs and the QoS parameters that you choose provide the basis for assigning
                                             a call to a particular voice-quality category. Use this report to monitor the voice quality of all calls through the network.

By Gateway - Available for CAR administrators. This report shows the percentage of the calls for each of the chosen gateways
                                             that meet the QoS criteria that the user chooses. You can generate this report on an hourly, daily, or weekly basis.

By Call Types - Available for CAR administrators. This report shows the percentage of the calls for each chosen call type
                                             that meet the QoS criteria that the user chooses. You can generate this report on an hourly, daily, or weekly basis.

Traffic

Summary - Available for CAR administrators. This report provides information about the call volume for a period that you specify
                                             and include only those call types and QoS voice-quality categories that you choose. Use this report to determine the number
                                             of calls that are being made on an hourly, weekly, or daily basis. This report helps you identify high- and low-traffic patterns
                                             for capacity planning.

Summary by Phone Number - Available for CAR administrators. This report provides information about the call volume for a period
                                             and set of phone numbers that you specify. It includes only those call types and phone numbers that you choose. You can generate
                                             the report on an hourly, weekly, or daily basis. This report helps you determine high-usage users or groups by aggregating
                                             the usage level across the users that you specify.

FAC/CMC

Client Matter Code - Available for CAR administrators. This report allows administrators to view the originating and destination
                                             numbers, the date, and time that the call originated, the call duration in seconds, and the call classification for calls
                                             that relate to each chosen client matter code.

Authorization Code Name - Available for CAR administrators. This report allows administrators to view the originating and
                                             destination numbers, the date, and time that the call originated, the call duration in seconds, the call classification, and
                                             the authorization level for calls that relate to each chosen authorization code name.

Authorization Level - Available for CAR administrators. This report allows administrators to view the originating and destination
                                             numbers, the date, and time that the call originated, the call duration in seconds, the authorization code name, and the call
                                             classification for calls that relate to each chosen authorization level.

Malicious Call Details - Available for CAR administrators. The Unified Communications Manager Malicious Call Identification (MCID) service tracks malicious calls. The Malicious Call Details report displays the details
                                       of malicious calls for a given date range.

Precedence Call Summary - Available for CAR administrators. The Unified Communications Manager Call Precedence service allows authenticated users to preempt lower priority phone calls. The PDF version of the CAR Precedence
                                       Call Summary report displays the Call Summary for the precedence values in the form of a bar chart, on an hour of the day,
                                       day of the week, or day of the month basis, for each of the precedence levels that you choose. CAR generates one chart for
                                       each precedence level, a table for each precedence level that lists the number of call legs, and a subtable that summarizes
                                       the percentage distribution for each precedence level. CAR makes the report available on-demand; the report does not get autogenerated.

System Overview - Available for CAR administrators. Use the System Overview report to see a high-level picture of the Unified Communications Manager network. The System Overview provides the following reports:

Top 5 Users Based on Charge

Top 5 Destinations Based on Charge

Top 5 Calls Based on Charge

Top 5 Users Based on Duration

Top 5 Destinations Based on Duration

Top 5 Calls Based on Duration

Traffic Summary Hour of Day - Incoming, Internal, International, Local, Long Distance, On Net, Others, Tandem, and Total calls

Traffic Summary Day of Week - Incoming, Internal, International, Local, Long Distance, On Net, Others, Tandem, and Total calls

Traffic Summary Day of Month - Incoming, Internal, International, Local, Long Distance, On Net, Others, Tandem, and Total
                                             calls

QoS Summary

Gateway Summary

CDR Error - Available for CAR administrators. This report provides statistics for the number of error records in the CAR Billing_Error
                                       table and the reason for the errors. Use this report to determine whether CAR incurred any errors with CDR data while the
                                       CDR data was loaded. This report lists the percentage of CDRs that are invalid and the reason that these CDRs have been classified
                                       as invalid.

### User Search

Many reports in CAR provide a search function, so you can look for users. The following CAR System reports support search
                                 by user: QoS Details and Traffic Summary by Phone Number. You can mail all reports that can be generated by using the Send
                                 Report button.

#### Before you begin

You must use the window in System Reports that allows you to search for users.

This section describes how to search for a user.

Step 1

Click the Search Users link.

A User Search window displays.

Step 2

In the First Name and Last Name fields, enter characters of the first or last name of the user and click Search .

A User Search Results window displays in the same window and lists all users who matched the search criteria that you entered.

Step 3

In the row for the user that you want, click Select link.

The user that you chose gets added to the List of Users in the User Search window. Repeat this step to add more users.

Step 4

When you have added all users, click Close in the User Search window.

## QoS System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help with call monitoring for budgeting or security purposes
                                 and for determining the voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

You may have access restrictions to view some reports depending on your job function.

Only CAR administrators generate the QoS detail report. The report details the QoS ratings that are attributed to inbound
                           and outbound calls on the Unified Communications Manager network for the period that is specified.

Managers or CAR administrators generate the QoS summary report. The report provides a two-dimensional pie chart that shows
                           the distribution of QoS grades that are achieved for the specified call classifications and period. The report also provides
                           a table that summarizes the calls for each QoS. The call details in CDRs and CMRs and the QoS parameters that are provided
                           in the Define QoS Values provide a basis for assigning a particular voice-quality category to a call.

You can either view reports that the system automatically generates or generate new reports. Only CAR administrators can schedule
                           reports for automatic generation. For more information, see Automatic Generation of CAR Reports and Alerts .

QoS Parameter Operators

The following table describes the QoS parameter operators that you use in generating the QoS reports.

Operator

Description

>=

Choose this operator to generate jitter, latency, or lost packet data that is greater than or equal to the specified value.

=

Choose this operator to generate jitter, latency, or lost packet data that is equal to the specified value.

<=

Choose this operator to generate jitter, latency, or lost packet data that is less than or equal to the specified value.

N.A.

Choose this operator to preclude jitter, latency, or lost packet data.

Between

Choose this operator to generate jitter, latency, or lost packet data that occurs between one value and another value. When
                                       you choose this operator, a second field displays, so you can set the start and end values.

### Generate QoS Detail Reports

This section describes how to generate, view, or mail detailed information about the system QoS.

Step 1

Choose System Reports > QoS > Detail .

The QoS Detail window displays.

Step 2

In the Select Call Types area, check the check boxes for the types of calls that you want the report to include. The following
                                          table describes the call types.

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. For more information, see Set Up Dial Plan .

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

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

Step 3

In the Select QoS area, check the check boxes for the voice-quality categories that you want to be included in the report.
                                          The parameters set in the following table provide the basis for all voice-quality categories.

Voice Quality

Description

Good

QoS for these calls represents the highest possible quality.

Acceptable

QoS for these calls, although slightly degraded, still fall within an acceptable range.

Fair

Although QoS for these calls is degraded, calls still fall within a usable range.

Poor

QoS for these calls designates unsatisfactory quality.

NA

These calls did not match any criteria for the established QoS categories.

Step 4

Choose the date range for the period for which you want to see QoS information.

Step 5

In Select Users field, you can either choose all users or search for particular users. To choose all users, check the Select All Users check box. To choose individual users, enter the user ID of the individual in the User ID field and click Add .

You can also use a provided search function. See the User Search .

Step 6

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 7

Click View Report .

Step 8

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

### Generate QoS Summary Reports

This section describes how to generate, view, or mail summary information about the system QoS.

Step 1

Perform one of the following steps:

If you are a manager, choose QoS > Summary .

If you are a CAR administrator, choose System Reports > QoS > Summary .

The QoS Summary window displays.

Step 2

In the Available Reports field, choose an automatically generated report (if available) and go to the following step, or use the default setting, Generate New Report , and go to the next step

You can only choose the automatically generated report if you are logged in as a CAR administrator. The automatically generated
                                                         reports do not display in the drop-down list box if you are logged in as a manager.

Step 3

In the Select Call Types area, check the check boxes for the types of calls that you want the report to include. The following
                                          table describes the call types.

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
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

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

Step 4

If you chose Generate New Report in the previous step, choose the date range for the period for which you want to generate
                                          the report.

Step 5

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 6

Click View Report .

Step 7

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

### Generate QoS by Gateway Reports

Only CAR administrators generate the QoS by Gateway report. The report provides the percentage of calls that satisfy the selected
                                 QoS criteria for a period that is specified for the selected gateways.

Caution

Use CAR only during off-peak hours. Otherwise, data collection and report generation could cause performance degradation on
                                             the Unified Communications Manager system.

This section describes how to generate, view, or mail QoS information about all chosen gateways.

#### Before you begin

Configure the gateway by using the procedures in the Set Up Gateway .

Step 1

Choose System Reports > QoS > By Gateways .

The QoS based on Gateways window displays.

Step 2

In the Generate Reports field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for an hour of the day.

Day of Week

Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for a day of the week.

Day of Month

Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for day of month.

Step 3

In the Jitter field, choose the operator that you want to use and enter the value for jitter. See the Table 1 for descriptions of operators.

Step 4

In the Latency field, choose the operator that you want to use and enter the value for latency. See the Table 1 for descriptions of operators.

Step 5

In the LostPackets field, choose the operator that you want to use and enter the value for a number of lost packets. See the Table 1 for descriptions of operators.

Step 6

Choose the date range of the period for which you want to see call information.

Step 7

To choose the type of gateway that you want to be included in the report, perform one of the following tasks:

To display all the gateways that are configured in the system, click Gateway Types in the column on the left side of the window.

To expand the tree structure and display the type of gateway from which you can choose, click the icon next to Gateway Types.

To choose a gateway that uses a particular route pattern/hunt pilot, rather than a gateway type, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays the gateways that are associated with
                                                the configured Route Patterns/Hunt Pilots.

To expand the tree structure and display route pattern/hunt pilot for you to choose, click the icon next to Route Patterns/Hunt
                                                Pilots.

You can also search for specific route patterns/hunt pilots by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               pilot(s) that matches the search string.

Step 8

From the list, choose a gateway type.

The gateway name displays in the List of Gateways box.

The List of Gateways box display up to 200 gateways that are configured for the chosen gateway type.

Step 9

In the List of Gateways box, select the gateways that you want to include in the report.

You can generate a report for up to 15 gateways at a time. If you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate a new report."

Step 10

Click the down arrow icon to move the chosen gateway to the list of Selected Gateways box.

The gateway that you chose displays in the Selected Gateways box.

Step 11

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 12

Click View Report .

Step 13

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

### Generate QoS by Call Types Reports

Only CAR administrators generate the QoS by Call Types report. The report provides jitter, latency, and lost packet information
                                 for a period that is specified for all calls of a chosen type.

This section describes how to generate, view, or mail QoS information about all calls of a certain type.

Caution

Use CAR only during off-peak hours. Otherwise, data collection and report generation could cause performance degradation on
                                             the Unified Communications Manager system.

Step 1

Choose System Reports > QoS > By Call Types .

The QoS based on Call Types window displays.

Step 2

In the Generate Report field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for an hour of the day.

Day of Week

Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the week.

Day of Month

Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the month.

Step 3

In the Jitter field, choose the operator that you want to use and enter the value for jitter. See the Table 1 for descriptions of operators.

Step 4

In the Latency field, choose the operator that you want to use and enter the value for latency. See the Table 1 for descriptions of operators.

Step 5

In the LostPackets field, choose the operator that you want to use and enter the value for a number of lost packets. See the Table 1 for descriptions of operators.

Step 6

In the Select Call Types area, check the check boxes for the types of calls that you want the report to include. The following table describes the
                                          call types.

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

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

Step 7

Choose the date range for the period for which you want to see call information.

Step 8

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 9

Click View Report .

Step 10

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

## Traffic System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help with call monitoring for budgeting or security purposes
                                 and for determining the voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

You may have access restrictions to view some reports depending on your job function.

Only CAR administrators can generate the traffic summary report. The report provides information about the call volume for
                           a period that you specify. It includes only those call types and QoS voice-quality categories that you chose.

Tip

When you configure CAR to generate a traffic summary report, you can choose different call types (On Net, Internal, Local,
                                       Long Distance, and so on). CAR compares the traffic volume for every hour interval and identifies the hour with the highest
                                       traffic volume (the Busy Hour Call Completion [BHCC] number). To obtain the overall BHCC number, choose all call types when
                                       you configure CAR. Under the report title, a separate line displays the BHCC number for that day.

Only CAR administrators can generate the traffic summary by phone numbers report. The report provides information about the
                           call volume for a period and set of phone numbers that you specify, and includes only those call types and phone numbers that
                           you choose.

Tip

You can use this report to track call usage by a specified group of users, by a department, or by another criteria, such as
                                       lobby phones or conference room phones. You can set up this report to generate on a weekly basis. This report helps you determine
                                       high-usage users or groups by aggregating the usage level across the users that you specify.

### Generate Traffic Summary Reports

Only CAR administrators generate the Traffic Summary report. The report provides information about the call volume for a period
                                 that you specify.

You can either view reports that the system automatically generates or generate new reports. For more information, see Set Up CDR Load Schedule .

This section describes how to generate, view, or mail summary information about system traffic.

Step 1

Choose System Reports > Traffic > Summary .

The Traffic Summary window displays.

Step 2

In the Generate Report field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for an hour of the day.

If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour interval and identifies the hour with the highest
                                                         traffic volume as the BHCC number for that day.

Day of Week

Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for the day of the week.

Day of Month

Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for a day of the month.

Step 3

In the Available Reports field, choose an automatically generated report (if available) and go to Step 8 or use the default setting, Generate New Report and go to Step 4 .

Step 4

Choose the date range for the period for which you want to generate the report.

Step 5

In the Select Call Types area, check the check boxes for the types of calls that you want to include in the report. To obtain the overall BHCC number
                                          for a particular hour or 24-hour period, choose all call types. The following table describes the call types.

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different
                                                         Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call
                                                         if it is configured as such in the CAR dial plan configuration window. See Set Up Dial Plan .

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified
                                                         Communications Manager network (no gateways or trunks are used).

Local

Local calls that route through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified
                                                         Communications Manager network.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will designate the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report.

Step 6

In the Select QoS area, check the check boxes for the voice-quality categories that you want to include in the report. The parameters that
                                          are set in the following table provide the basis for all voice-quality categories.

Voice Quality

Description

Good

QoS for these calls represents the highest possible quality.

Acceptable

QoS for these calls, although slightly degraded, still falls within an acceptable range.

Fair

QoS for these calls, although degraded, remains within a usable range.

Poor

Poor voice quality indicates that QoS for these calls is unsatisfactory.

NA

These calls did not match any criteria for the established QoS categories.

Step 7

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 8

Click View Report .

Step 9

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

### Generate Traffic Summary by Phone Number Reports

Only CAR administrators generate the Traffic Summary by Phone Number report. The report provides information about the call
                                 volume for a period and set of phone numbers that you specify.

This section describes how to generate, view, or mail a traffic summary report based on user phone numbers.

Step 1

Choose System Reports > Traffic > Summary By Phone Number .

The Traffic Summary that is based on Phone Number(s) window displays.

Step 2

In the Generate Report field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day.

Ensure that the date and time range does not exceed one month.

Day of Week

Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the week.

Ensure that the date and time range does not exceed one month.

Day of Month

Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the month.

Ensure that the date and time range does not exceed one month.

Step 3

In the Select Call Types area, check the check boxes for the types of calls that you want to include in the report. The following table describes
                                          the call types.

Call Type

Description

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
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

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will represent the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report.

Step 4

In the Select Phone Number(s) group box, you can either choose all phone numbers or search for phone numbers based on users.

You can enter a wildcard pattern like "!" or "X" to search on phone numbers. The "!" represents any n digit that has 0-9 as
                                                         each of its digits, and the "X" represents a single digit in the range 0-9.

To choose all phone numbers, check the Select All Phone Number(s) check box. To choose phone numbers based on users, enter the phone number of the individual in the Phone Number field and
                                             click the Add Phone Number button. You can also use a provided search function, as described in the User Search .

Step 5

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area,  if you want the report in PDF format.

Step 6

Click View Report .

Step 7

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

## FAC/CMC System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help with call monitoring for budgeting or security purposes
                                 and for determining the voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

You may have access restrictions to view some reports depending on your job function.

Only CAR administrators can generate Forced Authorization Code (FAC)/Client Matter Code (CMC) reports.

The following sections describe how to configure FAC/CMC reports:

### Generate Client Matter Code Reports

Only CAR administrators can generate the Client Matter Code report. You can generate a report that shows the origination (calling
                                 number), destination (called number), origination date time (the date and time that the call originated), duration (call duration
                                 in seconds), and the call classification that relates to each CMC.

The following procedure describes how to generate a report that shows the usage of specific client matter codes.

Step 1

Choose System Reports > FAC/CMC > Client Matter Code .

The Call Details for Client Matter Code window displays a list of all client matter codes that are configured in the system.

Step 2

In the List of Client Matter Codes box, choose the codes that you want to be included in the report.

You can choose up to 100 Client Matter Codes.

Step 3

To add the chosen code(s) to the Selected Client Matter Codes box, click down arrow.

The report includes all codes, for which data is available, that are listed in this box.

Step 4

In the From Date and To Date pull-down list boxes, enter the date range of the period for which you want to see Client Matter Code information.

Step 5

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 6

Click View Report .

Step 7

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in Mail Reports .

### Generate Authorization Code Name Reports

Only CAR administrators can generate the Authorization Code Name report. You can generate a report that shows the origination
                                 (calling number), destination (called number), origination date time (the date and time that the call originated), duration
                                 (call duration in seconds), and the call classification that relates to each chosen authorization code name.

For security purposes, the authorization code does not display; instead, the authorization code name (description) displays.

The following procedure describes how to generate a report that shows the usage of specific authorization code names.

Step 1

Choose System Reports > FAC/CMC > Authorization Code Name .

The Call Details for Authorization Code Name window displays a list of all authorization code names that are configured in
                                             the system.

Step 2

In the List of Authorization Code Names box, choose the code names that you want to be included in the report.

You can choose up to 30 code names.

Step 3

To add the chosen code name(s) to the Selected Authorization Code Names box, click the down arrow.

The report includes all code names, for which data is available, that are listed in this box.

Step 4

In the From Date and To Date drop-down list boxes, enter the date range of the period for which you want to see authorization code name information.

Step 5

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 6

Click View Report .

Step 7

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in Mail Reports .

### Generate Authorization Level Reports

Only CAR administrators can generate the Authorization Level report. You can generate a report that shows the origination
                                 (calling number), destination (called number), origination date time (the date and time that the call originated), duration
                                 (call duration in seconds), and the call classification that relate to each chosen authorization level.

The following procedure describes how to generate a report that shows the usage of specific authorization levels.

Step 1

Choose System Reports > FAC/CMC > Authorization Level .

The Call Details by Authorization Level window displays a list of all authorization levels that are configured in the system.

Step 2

In the List of Authorization Levels box, choose the levels that you want to be included in the report.

Step 3

To add the chosen level(s) to the Selected Authorization Levels box, click the down arrow.

The report includes all levels, for which data is available, that are listed in this box.

Only FAC authorization levels reports that are associated with Route Patterns will get generated.

Step 4

In the From Date and To Date drop-down list boxes, enter the date range of the period for which you want to see authorization level information.

Step 5

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 6

Click View Report .

Step 7

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

## Malicious Call Details System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help with call monitoring for budgeting or security purposes
                                 and for determining the voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

You may have access restrictions to view some reports depending on your job function.

### Generate Malicious Call Details Reports

Only CAR administrators generate the Malicious Call Details report. The report displays the following details about malicious
                                 calls for a particular date range: origination time, termination time, duration (in seconds), origination (calling number),
                                 destination (called number), origination device, destination device, and call classification.

This section describes how to generate, view, or mail a Malicious Call Detail report.

Step 1

Choose System Reports > Malicious Call Details .

The Malicious Call Details window displays.

Step 2

In the From Date drop-down list boxes, choose the month, day, and year from which you want malicious call details.

Step 3

In the To Date drop-down list boxes, choose the month, day, and year to which you want malicious call details.

Step 4

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 5

To view the report, click View Report .

Step 6

To mail the report to an email recipient, see the Mail Reports .

## Precedence Call Summary System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help with call monitoring for budgeting or security purposes
                                 and for determining the voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

You may have access restrictions to view some reports depending on your job function.

### Generate Precedence Call Summary Reports

Only CAR administrators generate the Call Summary by Precedence report. The report displays the Call Summary for the precedence
                                 values that you choose by Hour of Day, Day of Week, or Day of Month.

This section describes how to generate, view, or mail a Call Summary by Precedence report.

Step 1

Choose System Reports > Precedence Call Summary .

The Call Summary by Precedence window displays.

Step 2

In the Generate Reports field, choose a time as described in the following table.

Parameter

Description

Hour of Day

Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day.

Ensure that the date and time range does not exceed one month.

Day of Week

Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the week.

Ensure that the date and time range does not exceed one month.

Day of Month

Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the month.

Ensure that the date and time range does not exceed one month.

Step 3

In the Select Precedence Levels field, check a precedence level that you want in the report or click Select All to check all precedence levels.

Voice Quality

Description

Flash Override

Highest precedence setting for MLPP calls.

Flash

Second highest precedence setting for MLPP calls.

Immediate

Third highest precedence setting for MLPP calls.

Priority

Fourth highest precedence setting for MLPP calls.

Routine

Lowest precedence setting for MLPP calls.

The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report.

To uncheck the precedence level check boxes, click Clear All .

Step 4

In the From Date drop-down list boxes, choose the month, day, and year from which you want precedence summary information.

Step 5

In the To Date drop-down list boxes, choose the month, day, and year for which you want precedence summary information.

Step 6

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 7

Click View Report .

Step 8

To mail the report to an e-mail recipient, see the Mail Reports .

## System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help with call monitoring for budgeting or security purposes
                                 and for determining the voice quality of the calls.

Individual users - Generate a billing report for each call by each user.

You may have access restrictions to view some reports depending on your job function.

### Generate System Reports

Only CAR administrators generate the System Overview report that provides the entire set of system reports in one report.

The System Overview report includes the following information:

Top five users based on charge.

Top five destinations based on charge.

Top five calls based on charge.

Top five users based on duration.

Top five destinations based on duration.

Top five calls based on duration.

Traffic summary - Hour of day for incoming, internal, international, local, long distance, on the net, others, tandem, and
                                       total calls.

Traffic summary - Day of the week for incoming, internal, international, local, long distance, on the net, others, tandem,
                                       and total calls.

Traffic summary - Day of month for incoming, internal, international, local, long distance, on the net, others, tandem, and
                                       total calls.

Quality of service summary.

Gateway summary.

For more information about the System Overview reports, see the System Reports Results .

You can either view reports that the system automatically generates or generate new reports. Only CAR administrators can schedule
                                 reports for automatic generation. For more information, see Set Up CDR Load Schedule .

This section describes how to generate, view, or mail summary information about the Unified Communications Manager system.

Step 1

Choose System Reports > System Overview .

The System Overview window displays.

Step 2

In the Available Reports field, select an automatically generated report (if available) and go to Step 6 , or use the default setting, Generate New Report, and go to Step 3 .

Step 3

Choose the date range for the period for which you want to generate the report.

Step 4

From the List of Reports, select the reports that you want to be generated by highlighting the report and clicking the right
                                          arrow.

The reports that you select appear in the Selected Reports list box.

Tip

You can highlight more than one report at a time by pressing the Ctrl key on your keyboard while clicking the reports.

Step 5

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 6

Click View Report .

Step 7

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in Mail Reports .

## CDR Error System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help with call monitoring for budgeting or security purposes
                                 and for determining the voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

You may have access restrictions to view some reports depending on your job function.

### Generate CDR Error Reports

Only CAR administrators generate the CDR Error report. The report provides statistics for the number of error records in the
                                 CAR Billing Error (tbl_billing_error) table for a particular time period.

In order to determine why the error records failed the CDR Load, you must review the information in the tbl_error_id_map table.

The following table lists the CDR error codes and the definition of the error.

Error Code

Definition

CDRs

31101

CDR globalCallID_callManagerId <= 0

31102

CDR globalCallID_callId <= 0

31103

CDR origLegCallIdentifier <= 0

31105

CDR dateTimeOrigination <= 0

31108

CDR destLegIdentifier <= 0

31110

CDR dateTimeConnect <= 0

31111

CDR dateTimeDisconnect <= 0

31119

CDR originalCalledPartyNumber is empty

31120

CDR finalCalledPartyNumber is empty

31122

CDR duration < 0

31137

CDR LDAP error while retrieving UserID or ManagerID

31139

CDR callingPartyNumber is empty

31147

CDR origDeviceName is empty

31148

CDR destDeviceName is empty

31151

CDR origCallTerminationOnBehalfOf < 0

31152

CDR destCallTerminationOnBehalfOf < 0

31153

CDR lastRedirectRedirectOnBehalfOf < 0

31155

CDR destConversationId < 0

31156

CDR globalCallId_ClusterID is empty

Orig CMR

31123

Orig CMR globalCallID_callManagerId <= 0

31124

Orig CMR globalCallID_callId <= 0

31125

Orig CMR numberPacketsSent < 0

31126

Orig CMR numberPacketsReceived < 0

31127

Orig CMR jitter < 0

31129

Orig CMR callIdentifier <= 0

31149

Orig CMR deviceName is empty

31157

Orig CMR globalCallId_ClusterID is empty

Dest CMR

31140

Dest CMR globalCallID_callManagerId <= 0

31141

Dest CMR globalCallID_callId <= 0

31142

Dest CMR numberPacketsSent < 0

31143

Dest CMR numberPacketsReceived < 0

31144

Dest CMR jitter < 0

31145

Dest CMR callIdentifier <= 0

31150

Dest CMR deviceName is empty

31158

Dest CMR globalCallId_ClusterID is empty

This section describes how to generate, view, or mail information about the CDR Error report.

Step 1

Choose System Reports > CDR Error .

The CDR Error window displays.

Step 2

Choose the date range of the period for which you want to generate the report.

Step 3

Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format.

Step 4

Click View Report .

Step 5

Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports .

## System Reports Results

This chapter describes report output information for each CAR system report.

### QoS Detail Report Results

The results of the QoS Detail report include the following fields. See the following table.

Field

Description

Orig. Time

The time that the call was placed, in 24-hour, minute, and second format.

Term. Time

The time that the call disconnected, in 24 hour, minute, and second format.

Duration(s)

The time, in seconds, that the call was connected.

Orig.

The originating number from which the call was placed.

Dest.

The destination number to which the call was directed.

Call Classification - Call categories specify classes.

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                             in the CAR dial plan configuration window. See Set Up Dial Plan .

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                             one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network that go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

Orig. Codec

The codec that the originating device uses.

Dest. Codec

The codec that the destination device uses.

Orig. Device

The name of the device that placed the call.

Dest. Device

The name of the device that received the call.

Orig. QoS

The voice quality that the device that placed the call experienced.

Dest. QoS

The voice quality that the device that received the call experienced.

The following figure displays sample output of the QoS Detail report in PDF format.

### QoS Summary Report Results

The QoS Summary report includes the following fields. See the table. If you select PDF format for the report output, the report
                                 shows a pie chart that displays the QoS of the total number of calls.

Field

Description

Quality of Service

The quality of service of the calls.

Call Legs

Number of call legs with the quality of service that the Quality of Service field specified.

QoS Summary Report in PDF Format displays sample output of the QoS Summary Report in PDF format.

### QoS by Gateways Report Results

The QoS by Gateways report provides the following information. See the table.

Field

Description

Time/Day

Indicates the cumulative hours of the day(s), the days of the week, or the days of the month for the selected date range.

% of Call Legs

Displays the percentage of calls for each gateway for the hours of the day, the days of the week, or the days of the month
                                             for the selected date range.

QoS by Gateways Report displays sample output of the QoS by Gateways report in PDF format.

### QoS by Call Types Report Results

The QoS by Call Types report provides the following information. See the table.

Field

Description

Time/Day

The cumulative hours of the day(s), the days of the week, or the days of the month for the selected date range.

% of Call Legs

The percentage of calls for each gateway for the hours of the day, the days of the week, or the days of the month for the
                                             selected date range.

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                             one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network that go out through the PSTN.

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                             in the CAR dial plan configuration window. See Set Up Dial Plan .

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

QoS by Call Types Report displays sample output of the QoS by Call Types report in PDF format.

### Traffic Summary Report Results

The Traffic Summary and Traffic Summary by Phone Number reports contain the same information and include some or all the following
                                 fields. See the table. A separate line displays under the report title for the Busy Hour Call Completion (BHCC) number for
                                 that day.

Field

Description

Time/Day

The cumulative hours of the day(s), the days of the week, or the days of the month for the selected date range.

Average Number of Calls

The percentage of calls for each gateway for the hours of the day, the days of the week, or the days of the month for the
                                             selected date range.

On Net

Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk,and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                             in the CAR dial plan configuration window. See Set Up Dial Plan .

Internal

Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used).

Local

Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                             one of the local area codes.

Long Distance

Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN.

International

International calls that originate in the Unified Communications Manager network that goes out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free numbers or emergency calls such as 911.

Total

The total number of calls for each hour or day.

Traffic Summary Report Results and Traffic Summary By Phone Number Report Results display sample output of the Traffic Summary and the Traffic Summary by Phone Number report results in PDF format.

### Authorization Code Name Call Details Report Results

This report shows the usage of specific authorization code names. For security purposes, the authorization code name (description)
                                 displays and not the authorization code. The Authorization Code Name Call Details report includes the following fields (see
                                 the table).

Field

Description

Orig.

The originating number from which the call was placed.

Dest.

The destination number to which the call was directed.

Orig. Date Time

The date and time that the call originated.

Duration (sec)

The time, in seconds, that the call connected.

Call Classification

The type of call (internal, incoming, on so on.)

Authorization Level

The authorization level for calls for each chosen authorization code name.

Authorization Code Name Call Details Report displays sample output of the Authorization Code Name Call Details report in PDF format.

### Authorization Level Call Details Report Results

This report shows the usage of specific authorization levels. The Authorization Level Call Details report includes the following
                                 fields (see the table).

Field

Description

Orig.

The originating number from which the call was placed.

Dest.

The destination number to which the call was directed.

Orig. Date Time

The date and time that the call originated.

Duration (sec)

The time, in seconds, that the call connected.

Call Classification

The type of call (internal, incoming, and so on.)

Authorization Code Name

The authorization code name for each authorization level that you chose.

Authorization Level Call Details Report displays sample output of the Authorization Level Call Details report in PDF format.

### Client Matter Code Details Report Results

The report shows the usage of specific client matter codes. The Client Matter Code Details report includes the following fields
                                 (see the following table).

Field

Description

Orig.

The originating number from which the call was placed.

Dest.

The destination number to which the call was directed.

Orig. Date Time

The date and time that the call originated.

Duration (sec)

The time, in seconds, that the call connected.

Call Classification

The type of call (internal, incoming, and so on).

Client Matter Code Details Report displays sample output of the Client Matter Code Details report in PDF format.

### Malicious Call Details Report Results

The Malicious Call Details report provides information about malicious calls. The report provides the following fields. See
                                 the table.

Field

Description

Orig. Time

Time at which the malicious call originated.

Term. Time

Time at which the malicious call terminated.

Duration

Total time of malicious call in seconds.

Orig.

Originating DN.

Dest.

Destination DN.

Orig. Device

Name of the originating device.

Dest. Device

Name of the destination device.

Call Classification

Classification of the malicious call.

Malicious Calls Detail Report displays sample output of the Malicious Calls Detail report in PDF format.

### Precedence Call Summary Report Results

The Precedence Call Summary report provides information about calls based on precedence levels. The report displays the call
                                 summary for the precedence values in the form of a bar chart on an "Hour of Day," "Day of Week," or "Day of Month" basis for each precedence level that you choose. If you choose to display the report in PDF format, two tables, one reflecting
                                 the bar chart, and the other listing the "Number of Calls" and "Percentage" for each precedence level that was chosen, display in the report. See the table.

Field

Description

Time/Day

Indicates the cumulative hours of the day(s), the days of the week, or the days of the month for the selected date range.

Call Legs

Number of calls for each precedence level by time/day.

Precedence Level

Precedence level value of the call.

No. of Call Legs

Number of call legs per each precedence level.

Percentage

Percentage of calls per each precedence level.

Precedence Call Summary Report displays sample output of the Precedence Call Summary by Hour of Day report in PDF format.

### System Report Results

The system overview provides information about all parts of the Unified Communications Manager network. The report provides the following sections. See the table.

Field

Description

Top 5 Users based on Charge

Details the five users who have incurred the highest charges for calls that occurred during the specified date range. See
                                             the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Destinations based on Charge

Details the five called numbers that have incurred the highest charges for calls during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Calls based on Charge

Details the five calls that have incurred the highest charges for calls during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Users based on Duration

Details the five users who have spent the most time on calls during the specified date range. See Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Destinations based on Duration

Details the five called numbers that have been engaged in calls for the longest time during the specified date range. See
                                             the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Top 5 Calls based on Duration

Details the five longest calls for the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report.

Traffic Summary Report - Hour of Day

Shows the volume of calls during the specified date range based on each hour of the day. If the date range is within one day,
                                             the system identifies the hour with the highest traffic volume (the BHCC number). See the Traffic Summary Report Results for details about this section of the system overview report.

Traffic Summary Report - Day of Week

Shows the volume of calls during the specified date range based on each day of the week. See the Traffic Summary Report Results for details about this section of the system overview report.

Traffic Summary Report - Day of Month

Shows the volume of calls during the specified date range based on each day of the month. See the Traffic Summary Report Results for details about this section of the system overview report.

Quality of Service Report - Summary

Shows the number of calls that fell within each voice-quality category during the specified date range. See the QoS Summary Report Results for details about this section of the system overview report.

Gateway Summary Report

Shows the summary of the call classification for each gateway along with the QoS, the number of calls, and the duration for
                                             each classification for the gateway during the specified date range. See the QoS by Gateways Report Results for details about this section of the system overview report.

### CDR Error Report Results

The CDR Error report provides the following information. See the following table.

Field

Description

Time

The hour of the specified day that the error occurred.

No of Error CDRs

The total number of CDR records that were not processed during the CAR load because of an error.

No of Valid CDRs

The total number of CDR records that were successfully loaded into CAR.

% of Error CDRs

The percentage of failed CDR data records out of all the CDR data records to be loaded.

The following figure displays sample output of the CDR Error report in PDF format.

| Note | You may have access restrictions to view some reports depending on your job function. |
|---|---|

| Step 1 | Click the Search Users link. A User Search window displays. |
|---|---|
| Step 2 | In the First Name and Last Name fields, enter characters of the first or last name of the user and click Search . A User Search Results window displays in the same window and lists all users who matched the search criteria that you entered. |
| Step 3 | In the row for the user that you want, click Select link. The user that you chose gets added to the List of Users in the User Search window. Repeat this step to add more users. |
| Step 4 | When you have added all users, click Close in the User Search window. |

| Note | You may have access restrictions to view some reports depending on your job function. |
|---|---|

| Operator | Description |
|---|---|
| >= | Choose this operator to generate jitter, latency, or lost packet data that is greater than or equal to the specified value. |
| = | Choose this operator to generate jitter, latency, or lost packet data that is equal to the specified value. |
| <= | Choose this operator to generate jitter, latency, or lost packet data that is less than or equal to the specified value. |
| N.A. | Choose this operator to preclude jitter, latency, or lost packet data. |
| Between | Choose this operator to generate jitter, latency, or lost packet data that occurs between one value and another value. When
                                       you choose this operator, a second field displays, so you can set the start and end values. |

| Step 1 | Choose System Reports > QoS > Detail . The QoS Detail window displays. |
|---|---|
| Step 2 | In the Select Call Types area, check the check boxes for the types of calls that you want the report to include. The following
                                          table describes the call types. Table 2. QoS Detail Report Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. For more information, see Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and are transferred outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. For more information, see Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and are transferred outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. For more information, see Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Step 3 | In the Select QoS area, check the check boxes for the voice-quality categories that you want to be included in the report.
                                          The parameters set in the following table provide the basis for all voice-quality categories. Table 3. QoS Detail Report Voice Quality Voice Quality Description Good QoS for these calls represents the highest possible quality. Acceptable QoS for these calls, although slightly degraded, still fall within an acceptable range. Fair Although QoS for these calls is degraded, calls still fall within a usable range. Poor QoS for these calls designates unsatisfactory quality. NA These calls did not match any criteria for the established QoS categories. | Voice Quality | Description | Good | QoS for these calls represents the highest possible quality. | Acceptable | QoS for these calls, although slightly degraded, still fall within an acceptable range. | Fair | Although QoS for these calls is degraded, calls still fall within a usable range. | Poor | QoS for these calls designates unsatisfactory quality. | NA | These calls did not match any criteria for the established QoS categories. |
| Voice Quality | Description |
| Good | QoS for these calls represents the highest possible quality. |
| Acceptable | QoS for these calls, although slightly degraded, still fall within an acceptable range. |
| Fair | Although QoS for these calls is degraded, calls still fall within a usable range. |
| Poor | QoS for these calls designates unsatisfactory quality. |
| NA | These calls did not match any criteria for the established QoS categories. |
| Step 4 | Choose the date range for the period for which you want to see QoS information. |
| Step 5 | In Select Users field, you can either choose all users or search for particular users. To choose all users, check the Select All Users check box. To choose individual users, enter the user ID of the individual in the User ID field and click Add . Note You can also use a provided search function. See the User Search . | Note | You can also use a provided search function. See the User Search . |
| Note | You can also use a provided search function. See the User Search . |
| Step 6 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 7 | Click View Report . |
| Step 8 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. For more information, see Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |

| Voice Quality | Description |
|---|---|
| Good | QoS for these calls represents the highest possible quality. |
| Acceptable | QoS for these calls, although slightly degraded, still fall within an acceptable range. |
| Fair | Although QoS for these calls is degraded, calls still fall within a usable range. |
| Poor | QoS for these calls designates unsatisfactory quality. |
| NA | These calls did not match any criteria for the established QoS categories. |

| Note | You can also use a provided search function. See the User Search . |
|---|---|

| Step 1 | Perform one of the following steps: If you are a manager, choose QoS > Summary . If you are a CAR administrator, choose System Reports > QoS > Summary . The QoS Summary window displays. |
|---|---|
| Step 2 | In the Available Reports field, choose an automatically generated report (if available) and go to the following step, or use the default setting, Generate New Report , and go to the next step Note You can only choose the automatically generated report if you are logged in as a CAR administrator. The automatically generated
                                                         reports do not display in the drop-down list box if you are logged in as a manager. | Note | You can only choose the automatically generated report if you are logged in as a CAR administrator. The automatically generated
                                                         reports do not display in the drop-down list box if you are logged in as a manager. |
| Note | You can only choose the automatically generated report if you are logged in as a CAR administrator. The automatically generated
                                                         reports do not display in the drop-down list box if you are logged in as a manager. |
| Step 3 | In the Select Call Types area, check the check boxes for the types of calls that you want the report to include. The following
                                          table describes the call types. Table 4. QoS Summary Report Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Step 4 | If you chose Generate New Report in the previous step, choose the date range for the period for which you want to generate
                                          the report. |
| Step 5 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 6 | Click View Report . |
| Step 7 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Note | You can only choose the automatically generated report if you are logged in as a CAR administrator. The automatically generated
                                                         reports do not display in the drop-down list box if you are logged in as a manager. |
|---|---|

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |

| Caution | Use CAR only during off-peak hours. Otherwise, data collection and report generation could cause performance degradation on
                                             the Unified Communications Manager system. |
|---|---|

| Step 1 | Choose System Reports > QoS > By Gateways . The QoS based on Gateways window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the following table. Table 5. Generate Report Fields Parameter Description Hour of Day Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for an hour of the day. Day of Week Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for a day of the week. Day of Month Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for day of month. | Parameter | Description | Hour of Day | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for an hour of the day. | Day of Week | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for a day of the week. | Day of Month | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for day of month. |
| Parameter | Description |
| Hour of Day | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for an hour of the day. |
| Day of Week | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for a day of the week. |
| Day of Month | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for day of month. |
| Step 3 | In the Jitter field, choose the operator that you want to use and enter the value for jitter. See the Table 1 for descriptions of operators. |
| Step 4 | In the Latency field, choose the operator that you want to use and enter the value for latency. See the Table 1 for descriptions of operators. |
| Step 5 | In the LostPackets field, choose the operator that you want to use and enter the value for a number of lost packets. See the Table 1 for descriptions of operators. |
| Step 6 | Choose the date range of the period for which you want to see call information. |
| Step 7 | To choose the type of gateway that you want to be included in the report, perform one of the following tasks: To display all the gateways that are configured in the system, click Gateway Types in the column on the left side of the window. To expand the tree structure and display the type of gateway from which you can choose, click the icon next to Gateway Types. To choose a gateway that uses a particular route pattern/hunt pilot, rather than a gateway type, click Route Patterns/Hunt Pilots in the column on the left side of the window. The tree structure expands and displays the gateways that are associated with
                                                the configured Route Patterns/Hunt Pilots. To expand the tree structure and display route pattern/hunt pilot for you to choose, click the icon next to Route Patterns/Hunt
                                                Pilots. Note You can also search for specific route patterns/hunt pilots by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               pilot(s) that matches the search string. | Note | You can also search for specific route patterns/hunt pilots by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               pilot(s) that matches the search string. |
| Note | You can also search for specific route patterns/hunt pilots by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               pilot(s) that matches the search string. |
| Step 8 | From the list, choose a gateway type. The gateway name displays in the List of Gateways box. Note The List of Gateways box display up to 200 gateways that are configured for the chosen gateway type. | Note | The List of Gateways box display up to 200 gateways that are configured for the chosen gateway type. |
| Note | The List of Gateways box display up to 200 gateways that are configured for the chosen gateway type. |
| Step 9 | In the List of Gateways box, select the gateways that you want to include in the report. Note You can generate a report for up to 15 gateways at a time. If you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate a new report." | Note | You can generate a report for up to 15 gateways at a time. If you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate a new report." |
| Note | You can generate a report for up to 15 gateways at a time. If you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate a new report." |
| Step 10 | Click the down arrow icon to move the chosen gateway to the list of Selected Gateways box. The gateway that you chose displays in the Selected Gateways box. |
| Step 11 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 12 | Click View Report . |
| Step 13 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for an hour of the day. |
| Day of Week | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for a day of the week. |
| Day of Month | Displays the percentage of the calls, for each selected gateway, that satisfies the QoS criteria for the period that you specify
                                                         in Step 6 . The percentage results show for day of month. |

| Note | You can also search for specific route patterns/hunt pilots by entering part of the name of the route pattern(s)/hunt pilot(s)
                                                               in the Route Patterns/Hunt Pilots box in the column on the left side of the window. CAR searches for the route pattern(s)/hunt
                                                               pilot(s) that matches the search string. |
|---|---|

| Note | The List of Gateways box display up to 200 gateways that are configured for the chosen gateway type. |
|---|---|

| Note | You can generate a report for up to 15 gateways at a time. If you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate a new report." |
|---|---|

| Caution | Use CAR only during off-peak hours. Otherwise, data collection and report generation could cause performance degradation on
                                             the Unified Communications Manager system. |
|---|---|

| Step 1 | Choose System Reports > QoS > By Call Types . The QoS based on Call Types window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the following table. Table 6. Generate Report Fields Parameter Description Hour of Day Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for an hour of the day. Day of Week Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the week. Day of Month Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the month. | Parameter | Description | Hour of Day | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for an hour of the day. | Day of Week | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the week. | Day of Month | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the month. |
| Parameter | Description |
| Hour of Day | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for an hour of the day. |
| Day of Week | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the week. |
| Day of Month | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the month. |
| Step 3 | In the Jitter field, choose the operator that you want to use and enter the value for jitter. See the Table 1 for descriptions of operators. |
| Step 4 | In the Latency field, choose the operator that you want to use and enter the value for latency. See the Table 1 for descriptions of operators. |
| Step 5 | In the LostPackets field, choose the operator that you want to use and enter the value for a number of lost packets. See the Table 1 for descriptions of operators. |
| Step 6 | In the Select Call Types area, check the check boxes for the types of calls that you want the report to include. The following table describes the
                                          call types. Table 7. QoS Parameters by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Step 7 | Choose the date range for the period for which you want to see call information. |
| Step 8 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 9 | Click View Report . |
| Step 10 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for an hour of the day. |
| Day of Week | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the week. |
| Day of Month | Displays the percentage of the calls, for each call type, that satisfies the QoS criteria for the period that you specify
                                                         in Step 7 . The percentage results show for a day of the month. |

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
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |

| Note | You may have access restrictions to view some reports depending on your job function. |
|---|---|

| Tip | When you configure CAR to generate a traffic summary report, you can choose different call types (On Net, Internal, Local,
                                       Long Distance, and so on). CAR compares the traffic volume for every hour interval and identifies the hour with the highest
                                       traffic volume (the Busy Hour Call Completion [BHCC] number). To obtain the overall BHCC number, choose all call types when
                                       you configure CAR. Under the report title, a separate line displays the BHCC number for that day. |
|---|---|

| Tip | You can use this report to track call usage by a specified group of users, by a department, or by another criteria, such as
                                       lobby phones or conference room phones. You can set up this report to generate on a weekly basis. This report helps you determine
                                       high-usage users or groups by aggregating the usage level across the users that you specify. |
|---|---|

| Step 1 | Choose System Reports > Traffic > Summary . The Traffic Summary window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the following table. Table 8. Generate Report Fields Parameter Description Hour of Day Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for an hour of the day. If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour interval and identifies the hour with the highest
                                                         traffic volume as the BHCC number for that day. Day of Week Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for the day of the week. Day of Month Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for a day of the month. | Parameter | Description | Hour of Day | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for an hour of the day. If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour interval and identifies the hour with the highest
                                                         traffic volume as the BHCC number for that day. | Day of Week | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for the day of the week. | Day of Month | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for a day of the month. |
| Parameter | Description |
| Hour of Day | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for an hour of the day. If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour interval and identifies the hour with the highest
                                                         traffic volume as the BHCC number for that day. |
| Day of Week | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for the day of the week. |
| Day of Month | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for a day of the month. |
| Step 3 | In the Available Reports field, choose an automatically generated report (if available) and go to Step 8 or use the default setting, Generate New Report and go to Step 4 . |
| Step 4 | Choose the date range for the period for which you want to generate the report. |
| Step 5 | In the Select Call Types area, check the check boxes for the types of calls that you want to include in the report. To obtain the overall BHCC number
                                          for a particular hour or 24-hour period, choose all call types. The following table describes the call types. Table 9. Traffic Summary by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different
                                                         Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call
                                                         if it is configured as such in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified
                                                         Communications Manager network (no gateways or trunks are used). Local Local calls that route through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified
                                                         Communications Manager network. Others All other outgoing calls, such as toll-free numbers or emergency calls such as 911. Note The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will designate the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different
                                                         Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call
                                                         if it is configured as such in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified
                                                         Communications Manager network (no gateways or trunks are used). | Local | Local calls that route through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified
                                                         Communications Manager network. | Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. | Note | The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will designate the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different
                                                         Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call
                                                         if it is configured as such in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified
                                                         Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that route through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified
                                                         Communications Manager network. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Note | The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will designate the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report. |
| Step 6 | In the Select QoS area, check the check boxes for the voice-quality categories that you want to include in the report. The parameters that
                                          are set in the following table provide the basis for all voice-quality categories. Table 10. QoS Detail Report Voice Quality Voice Quality Description Good QoS for these calls represents the highest possible quality. Acceptable QoS for these calls, although slightly degraded, still falls within an acceptable range. Fair QoS for these calls, although degraded, remains within a usable range. Poor Poor voice quality indicates that QoS for these calls is unsatisfactory. NA These calls did not match any criteria for the established QoS categories. | Voice Quality | Description | Good | QoS for these calls represents the highest possible quality. | Acceptable | QoS for these calls, although slightly degraded, still falls within an acceptable range. | Fair | QoS for these calls, although degraded, remains within a usable range. | Poor | Poor voice quality indicates that QoS for these calls is unsatisfactory. | NA | These calls did not match any criteria for the established QoS categories. |
| Voice Quality | Description |
| Good | QoS for these calls represents the highest possible quality. |
| Acceptable | QoS for these calls, although slightly degraded, still falls within an acceptable range. |
| Fair | QoS for these calls, although degraded, remains within a usable range. |
| Poor | Poor voice quality indicates that QoS for these calls is unsatisfactory. |
| NA | These calls did not match any criteria for the established QoS categories. |
| Step 7 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 8 | Click View Report . |
| Step 9 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for an hour of the day. If the period that you specify in Step 4 is within one day, the system compares the traffic volume for every hour interval and identifies the hour with the highest
                                                         traffic volume as the BHCC number for that day. |
| Day of Week | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for the day of the week. |
| Day of Month | Displays the average number of calls in the system for the period that you specify in Step 4 , the call types that you specify in Step 5 , and the QoS values that you specify in Step 6 for a day of the month. |

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk and terminate on a different
                                                         Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call
                                                         if it is configured as such in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified
                                                         Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that route through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified
                                                         Communications Manager network. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |

| Note | The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will designate the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report. |
|---|---|

| Voice Quality | Description |
|---|---|
| Good | QoS for these calls represents the highest possible quality. |
| Acceptable | QoS for these calls, although slightly degraded, still falls within an acceptable range. |
| Fair | QoS for these calls, although degraded, remains within a usable range. |
| Poor | Poor voice quality indicates that QoS for these calls is unsatisfactory. |
| NA | These calls did not match any criteria for the established QoS categories. |

| Step 1 | Choose System Reports > Traffic > Summary By Phone Number . The Traffic Summary that is based on Phone Number(s) window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the following table. Table 11. Generate Report Fields Parameter Description Hour of Day Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day. Note Ensure that the date and time range does not exceed one month. Day of Week Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the week. Note Ensure that the date and time range does not exceed one month. Day of Month Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the month. Note Ensure that the date and time range does not exceed one month. | Parameter | Description | Hour of Day | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. | Day of Week | Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the week. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. | Day of Month | Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the month. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Parameter | Description |
| Hour of Day | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Day of Week | Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the week. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Day of Month | Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the month. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Step 3 | In the Select Call Types area, check the check boxes for the types of calls that you want to include in the report. The following table describes
                                          the call types. Table 12. Traffic Summary (Phone Number) by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. Others All other outgoing calls, such as toll-free numbers or emergency calls such as 911. Note The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will represent the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. | Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. | Note | The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will represent the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Note | The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will represent the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report. |
| Step 4 | In the Select Phone Number(s) group box, you can either choose all phone numbers or search for phone numbers based on users. Note You can enter a wildcard pattern like "!" or "X" to search on phone numbers. The "!" represents any n digit that has 0-9 as
                                                         each of its digits, and the "X" represents a single digit in the range 0-9. To choose all phone numbers, check the Select All Phone Number(s) check box. To choose phone numbers based on users, enter the phone number of the individual in the Phone Number field and
                                             click the Add Phone Number button. You can also use a provided search function, as described in the User Search . | Note | You can enter a wildcard pattern like "!" or "X" to search on phone numbers. The "!" represents any n digit that has 0-9 as
                                                         each of its digits, and the "X" represents a single digit in the range 0-9. |
| Note | You can enter a wildcard pattern like "!" or "X" to search on phone numbers. The "!" represents any n digit that has 0-9 as
                                                         each of its digits, and the "X" represents a single digit in the range 0-9. |
| Step 5 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area,  if you want the report in PDF format. |
| Step 6 | Click View Report . |
| Step 7 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Day of Week | Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the week. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Day of Month | Displays the average calls in the system for the selected phone numbers for the date range that was chosen for the day of
                                                         the month. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |

| Note | Ensure that the date and time range does not exceed one month. |
|---|---|

| Note | Ensure that the date and time range does not exceed one month. |
|---|---|

| Note | Ensure that the date and time range does not exceed one month. |
|---|---|

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                                         one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |

| Note | The calls that the chart/table shows comprise an average number of calls per day. If the data that is generated is less and
                                                         you have chosen a wide date range, the report shows negligible values that are treated as 0, and the graph does not display.
                                                         For example, if a Day of Week report gets generated for eight days that comprise two Mondays, the data that is shown for Monday
                                                         represents the average number of calls for both the Mondays (the sum of all the calls in each Monday that is divided by 2).
                                                         Similarly, in an Hour of Day report, the data that displays against 05-06 will represent the average number of calls per day
                                                         between the time 05 and 06 of the date range that was chosen for the report. |
|---|---|

| Note | You can enter a wildcard pattern like "!" or "X" to search on phone numbers. The "!" represents any n digit that has 0-9 as
                                                         each of its digits, and the "X" represents a single digit in the range 0-9. |
|---|---|

| Note | You may have access restrictions to view some reports depending on your job function. |
|---|---|

| Step 1 | Choose System Reports > FAC/CMC > Client Matter Code . The Call Details for Client Matter Code window displays a list of all client matter codes that are configured in the system. |
|---|---|
| Step 2 | In the List of Client Matter Codes box, choose the codes that you want to be included in the report. Note You can choose up to 100 Client Matter Codes. | Note | You can choose up to 100 Client Matter Codes. |
| Note | You can choose up to 100 Client Matter Codes. |
| Step 3 | To add the chosen code(s) to the Selected Client Matter Codes box, click down arrow. The report includes all codes, for which data is available, that are listed in this box. |
| Step 4 | In the From Date and To Date pull-down list boxes, enter the date range of the period for which you want to see Client Matter Code information. |
| Step 5 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 6 | Click View Report . |
| Step 7 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in Mail Reports . |

| Note | You can choose up to 100 Client Matter Codes. |
|---|---|

| Note | For security purposes, the authorization code does not display; instead, the authorization code name (description) displays. |
|---|---|

| Step 1 | Choose System Reports > FAC/CMC > Authorization Code Name . The Call Details for Authorization Code Name window displays a list of all authorization code names that are configured in
                                             the system. |
|---|---|
| Step 2 | In the List of Authorization Code Names box, choose the code names that you want to be included in the report. Note You can choose up to 30 code names. | Note | You can choose up to 30 code names. |
| Note | You can choose up to 30 code names. |
| Step 3 | To add the chosen code name(s) to the Selected Authorization Code Names box, click the down arrow. The report includes all code names, for which data is available, that are listed in this box. |
| Step 4 | In the From Date and To Date drop-down list boxes, enter the date range of the period for which you want to see authorization code name information. |
| Step 5 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 6 | Click View Report . |
| Step 7 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in Mail Reports . |

| Note | You can choose up to 30 code names. |
|---|---|

| Step 1 | Choose System Reports > FAC/CMC > Authorization Level . The Call Details by Authorization Level window displays a list of all authorization levels that are configured in the system. |
|---|---|
| Step 2 | In the List of Authorization Levels box, choose the levels that you want to be included in the report. |
| Step 3 | To add the chosen level(s) to the Selected Authorization Levels box, click the down arrow. The report includes all levels, for which data is available, that are listed in this box. Note Only FAC authorization levels reports that are associated with Route Patterns will get generated. | Note | Only FAC authorization levels reports that are associated with Route Patterns will get generated. |
| Note | Only FAC authorization levels reports that are associated with Route Patterns will get generated. |
| Step 4 | In the From Date and To Date drop-down list boxes, enter the date range of the period for which you want to see authorization level information. |
| Step 5 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 6 | Click View Report . |
| Step 7 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Note | Only FAC authorization levels reports that are associated with Route Patterns will get generated. |
|---|---|

| Note | You may have access restrictions to view some reports depending on your job function. |
|---|---|

| Step 1 | Choose System Reports > Malicious Call Details . The Malicious Call Details window displays. |
|---|---|
| Step 2 | In the From Date drop-down list boxes, choose the month, day, and year from which you want malicious call details. |
| Step 3 | In the To Date drop-down list boxes, choose the month, day, and year to which you want malicious call details. |
| Step 4 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 5 | To view the report, click View Report . |
| Step 6 | To mail the report to an email recipient, see the Mail Reports . |

| Note | You may have access restrictions to view some reports depending on your job function. |
|---|---|

| Step 1 | Choose System Reports > Precedence Call Summary . The Call Summary by Precedence window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the following table. Table 13. Generate Report Fields Parameter Description Hour of Day Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day. Note Ensure that the date and time range does not exceed one month. Day of Week Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the week. Note Ensure that the date and time range does not exceed one month. Day of Month Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the month. Note Ensure that the date and time range does not exceed one month. | Parameter | Description | Hour of Day | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. | Day of Week | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the week. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. | Day of Month | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the month. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Parameter | Description |
| Hour of Day | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Day of Week | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the week. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Day of Month | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the month. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Step 3 | In the Select Precedence Levels field, check a precedence level that you want in the report or click Select All to check all precedence levels. Table 14. Call Precedence Levels Voice Quality Description Flash Override Highest precedence setting for MLPP calls. Flash Second highest precedence setting for MLPP calls. Immediate Third highest precedence setting for MLPP calls. Priority Fourth highest precedence setting for MLPP calls. Routine Lowest precedence setting for MLPP calls. Note The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report. Note To uncheck the precedence level check boxes, click Clear All . | Voice Quality | Description | Flash Override | Highest precedence setting for MLPP calls. | Flash | Second highest precedence setting for MLPP calls. | Immediate | Third highest precedence setting for MLPP calls. | Priority | Fourth highest precedence setting for MLPP calls. | Routine | Lowest precedence setting for MLPP calls. | Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report. | Note | To uncheck the precedence level check boxes, click Clear All . |
| Voice Quality | Description |
| Flash Override | Highest precedence setting for MLPP calls. |
| Flash | Second highest precedence setting for MLPP calls. |
| Immediate | Third highest precedence setting for MLPP calls. |
| Priority | Fourth highest precedence setting for MLPP calls. |
| Routine | Lowest precedence setting for MLPP calls. |
| Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report. |
| Note | To uncheck the precedence level check boxes, click Clear All . |
| Step 4 | In the From Date drop-down list boxes, choose the month, day, and year from which you want precedence summary information. |
| Step 5 | In the To Date drop-down list boxes, choose the month, day, and year for which you want precedence summary information. |
| Step 6 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 7 | Click View Report . |
| Step 8 | To mail the report to an e-mail recipient, see the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for an
                                                         hour of the day. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Day of Week | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the week. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |
| Day of Month | Displays the average number of calls in the system for the chosen phone numbers for the date range that was chosen for the
                                                         day of the month. Note Ensure that the date and time range does not exceed one month. | Note | Ensure that the date and time range does not exceed one month. |
| Note | Ensure that the date and time range does not exceed one month. |

| Note | Ensure that the date and time range does not exceed one month. |
|---|---|

| Note | Ensure that the date and time range does not exceed one month. |
|---|---|

| Note | Ensure that the date and time range does not exceed one month. |
|---|---|

| Voice Quality | Description |
|---|---|
| Flash Override | Highest precedence setting for MLPP calls. |
| Flash | Second highest precedence setting for MLPP calls. |
| Immediate | Third highest precedence setting for MLPP calls. |
| Priority | Fourth highest precedence setting for MLPP calls. |
| Routine | Lowest precedence setting for MLPP calls. |

| Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                         considered as Flash Override in this report. |
|---|---|

| Note | To uncheck the precedence level check boxes, click Clear All . |
|---|---|

| Note | You may have access restrictions to view some reports depending on your job function. |
|---|---|

| Step 1 | Choose System Reports > System Overview . The System Overview window displays. |
|---|---|
| Step 2 | In the Available Reports field, select an automatically generated report (if available) and go to Step 6 , or use the default setting, Generate New Report, and go to Step 3 . |
| Step 3 | Choose the date range for the period for which you want to generate the report. |
| Step 4 | From the List of Reports, select the reports that you want to be generated by highlighting the report and clicking the right
                                          arrow. The reports that you select appear in the Selected Reports list box. Tip You can highlight more than one report at a time by pressing the Ctrl key on your keyboard while clicking the reports. | Tip | You can highlight more than one report at a time by pressing the Ctrl key on your keyboard while clicking the reports. |
| Tip | You can highlight more than one report at a time by pressing the Ctrl key on your keyboard while clicking the reports. |
| Step 5 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 6 | Click View Report . |
| Step 7 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in Mail Reports . |

| Tip | You can highlight more than one report at a time by pressing the Ctrl key on your keyboard while clicking the reports. |
|---|---|

| Note | You may have access restrictions to view some reports depending on your job function. |
|---|---|

| Error Code | Definition |
|---|---|
| CDRs |
| 31101 | CDR globalCallID_callManagerId <= 0 |
| 31102 | CDR globalCallID_callId <= 0 |
| 31103 | CDR origLegCallIdentifier <= 0 |
| 31105 | CDR dateTimeOrigination <= 0 |
| 31108 | CDR destLegIdentifier <= 0 |
| 31110 | CDR dateTimeConnect <= 0 |
| 31111 | CDR dateTimeDisconnect <= 0 |
| 31119 | CDR originalCalledPartyNumber is empty |
| 31120 | CDR finalCalledPartyNumber is empty |
| 31122 | CDR duration < 0 |
| 31137 | CDR LDAP error while retrieving UserID or ManagerID |
| 31139 | CDR callingPartyNumber is empty |
| 31147 | CDR origDeviceName is empty |
| 31148 | CDR destDeviceName is empty |
| 31151 | CDR origCallTerminationOnBehalfOf < 0 |
| 31152 | CDR destCallTerminationOnBehalfOf < 0 |
| 31153 | CDR lastRedirectRedirectOnBehalfOf < 0 |
| 31155 | CDR destConversationId < 0 |
| 31156 | CDR globalCallId_ClusterID is empty |
| Orig CMR |
| 31123 | Orig CMR globalCallID_callManagerId <= 0 |
| 31124 | Orig CMR globalCallID_callId <= 0 |
| 31125 | Orig CMR numberPacketsSent < 0 |
| 31126 | Orig CMR numberPacketsReceived < 0 |
| 31127 | Orig CMR jitter < 0 |
| 31129 | Orig CMR callIdentifier <= 0 |
| 31149 | Orig CMR deviceName is empty |
| 31157 | Orig CMR globalCallId_ClusterID is empty |
| Dest CMR |
| 31140 | Dest CMR globalCallID_callManagerId <= 0 |
| 31141 | Dest CMR globalCallID_callId <= 0 |
| 31142 | Dest CMR numberPacketsSent < 0 |
| 31143 | Dest CMR numberPacketsReceived < 0 |
| 31144 | Dest CMR jitter < 0 |
| 31145 | Dest CMR callIdentifier <= 0 |
| 31150 | Dest CMR deviceName is empty |
| 31158 | Dest CMR globalCallId_ClusterID is empty |

| Step 1 | Choose System Reports > CDR Error . The CDR Error window displays. |
|---|---|
| Step 2 | Choose the date range of the period for which you want to generate the report. |
| Step 3 | Choose CSV in the Report Format area, if you want the report in CSV format. Choose PDF in the Report Format area, if you want the report in PDF format. |
| Step 4 | Click View Report . |
| Step 5 | Click Send Report , if you want to mail the report. To send the report, perform the procedure that is described in the Mail Reports . |

| Field | Description |
|---|---|
| Orig. Time | The time that the call was placed, in 24-hour, minute, and second format. |
| Term. Time | The time that the call disconnected, in 24 hour, minute, and second format. |
| Duration(s) | The time, in seconds, that the call was connected. |
| Orig. | The originating number from which the call was placed. |
| Dest. | The destination number to which the call was directed. |
| Call Classification - Call categories specify classes. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                             in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                             one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Orig. Codec | The codec that the originating device uses. |
| Dest. Codec | The codec that the destination device uses. |
| Orig. Device | The name of the device that placed the call. |
| Dest. Device | The name of the device that received the call. |
| Orig. QoS | The voice quality that the device that placed the call experienced. |
| Dest. QoS | The voice quality that the device that received the call experienced. |

| Field | Description |
|---|---|
| Quality of Service | The quality of service of the calls. |
| Call Legs | Number of call legs with the quality of service that the Quality of Service field specified. |

| Field | Description |
|---|---|
| Time/Day | Indicates the cumulative hours of the day(s), the days of the week, or the days of the month for the selected date range. |
| % of Call Legs | Displays the percentage of calls for each gateway for the hours of the day, the days of the week, or the days of the month
                                             for the selected date range. |

| Field | Description |
|---|---|
| Time/Day | The cumulative hours of the day(s), the days of the week, or the days of the month for the selected date range. |
| % of Call Legs | The percentage of calls for each gateway for the hours of the day, the days of the week, or the days of the month for the
                                             selected date range. |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                             one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network that go out through the PSTN. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                             in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |

| Field | Description |
|---|---|
| Time/Day | The cumulative hours of the day(s), the days of the week, or the days of the month for the selected date range. |
| Average Number of Calls | The percentage of calls for each gateway for the hours of the day, the days of the week, or the days of the month for the
                                             selected date range. |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk,and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an OnNet call if it is configured as such
                                             in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public switched telephone network (PSTN) to numbers without an area code or that include
                                             one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network that goes out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free numbers or emergency calls such as 911. |
| Total | The total number of calls for each hour or day. |

| Field | Description |
|---|---|
| Orig. | The originating number from which the call was placed. |
| Dest. | The destination number to which the call was directed. |
| Orig. Date Time | The date and time that the call originated. |
| Duration (sec) | The time, in seconds, that the call connected. |
| Call Classification | The type of call (internal, incoming, on so on.) |
| Authorization Level | The authorization level for calls for each chosen authorization code name. |

| Field | Description |
|---|---|
| Orig. | The originating number from which the call was placed. |
| Dest. | The destination number to which the call was directed. |
| Orig. Date Time | The date and time that the call originated. |
| Duration (sec) | The time, in seconds, that the call connected. |
| Call Classification | The type of call (internal, incoming, and so on.) |
| Authorization Code Name | The authorization code name for each authorization level that you chose. |

| Field | Description |
|---|---|
| Orig. | The originating number from which the call was placed. |
| Dest. | The destination number to which the call was directed. |
| Orig. Date Time | The date and time that the call originated. |
| Duration (sec) | The time, in seconds, that the call connected. |
| Call Classification | The type of call (internal, incoming, and so on). |

| Field | Description |
|---|---|
| Orig. Time | Time at which the malicious call originated. |
| Term. Time | Time at which the malicious call terminated. |
| Duration | Total time of malicious call in seconds. |
| Orig. | Originating DN. |
| Dest. | Destination DN. |
| Orig. Device | Name of the originating device. |
| Dest. Device | Name of the destination device. |
| Call Classification | Classification of the malicious call. |

| Field | Description |
|---|---|
| Time/Day | Indicates the cumulative hours of the day(s), the days of the week, or the days of the month for the selected date range. |
| Call Legs | Number of calls for each precedence level by time/day. |
| Precedence Level | Precedence level value of the call. |
| No. of Call Legs | Number of call legs per each precedence level. |
| Percentage | Percentage of calls per each precedence level. |

| Field | Description |
|---|---|
| Top 5 Users based on Charge | Details the five users who have incurred the highest charges for calls that occurred during the specified date range. See
                                             the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Destinations based on Charge | Details the five called numbers that have incurred the highest charges for calls during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Calls based on Charge | Details the five calls that have incurred the highest charges for calls during the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Users based on Duration | Details the five users who have spent the most time on calls during the specified date range. See Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Destinations based on Duration | Details the five called numbers that have been engaged in calls for the longest time during the specified date range. See
                                             the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Top 5 Calls based on Duration | Details the five longest calls for the specified date range. See the Top N by Charge or Duration Report Results for details about this section of the system overview report. |
| Traffic Summary Report - Hour of Day | Shows the volume of calls during the specified date range based on each hour of the day. If the date range is within one day,
                                             the system identifies the hour with the highest traffic volume (the BHCC number). See the Traffic Summary Report Results for details about this section of the system overview report. |
| Traffic Summary Report - Day of Week | Shows the volume of calls during the specified date range based on each day of the week. See the Traffic Summary Report Results for details about this section of the system overview report. |
| Traffic Summary Report - Day of Month | Shows the volume of calls during the specified date range based on each day of the month. See the Traffic Summary Report Results for details about this section of the system overview report. |
| Quality of Service Report - Summary | Shows the number of calls that fell within each voice-quality category during the specified date range. See the QoS Summary Report Results for details about this section of the system overview report. |
| Gateway Summary Report | Shows the summary of the call classification for each gateway along with the QoS, the number of calls, and the duration for
                                             each classification for the gateway during the specified date range. See the QoS by Gateways Report Results for details about this section of the system overview report. |

| Field | Description |
|---|---|
| Time | The hour of the specified day that the error occurred. |
| No of Error CDRs | The total number of CDR records that were not processed during the CAR load because of an error. |
| No of Valid CDRs | The total number of CDR records that were successfully loaded into CAR. |
| % of Error CDRs | The percentage of failed CDR data records out of all the CDR data records to be loaded. |