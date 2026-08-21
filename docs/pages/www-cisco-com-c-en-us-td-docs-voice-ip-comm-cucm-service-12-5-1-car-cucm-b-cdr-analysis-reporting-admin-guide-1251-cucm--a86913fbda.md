---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--a86913fbda
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_01010.html
retrieved_at: 2026-08-21T01:34:04.270137+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: QoS System Reports

## Chapter: QoS System Reports

# QoS System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

Only CAR administrators generate the QoS detail report. The report details the QoS ratings that are attributed to inbound
                        and outbound calls on the Unified Communications Manager network for the period that is specified.

Managers or CAR administrators generate the QoS summary report.
                        		The report provides a two-dimensional pie chart that shows the distribution of
                        		QoS grades that are achieved for the specified call classifications and period.
                        		The report also provides a table that summarizes the calls for each QoS. The
                        		call details in CDRs and CMRs and the QoS parameters that are provided in the Define QoS Values provide a basis for assigning a particular voice-quality category to a call.

You can either view reports that the system automatically
                        		generates or generate new reports. Only CAR administrators can schedule reports
                        		for automatic generation. See Automatic Generation of CAR Reports and Alerts ,
                        		for more information.

QoS Parameter Operators

The following table describes the QoS parameter operators that
                        		you use in generating the QoS reports.

Operator

Description

>=

Choose this operator to generate jitter, latency, or lost
                                    				packet data that is greater than or equal to the specified value.

=

Choose this operator to generate jitter, latency, or lost
                                    				packet data that is equal to the specified value.

<=

Choose this operator to generate jitter, latency, or lost
                                    				packet data that is less than or equal to the specified value.

N.A.

Choose this operator to preclude jitter, latency, or lost
                                    				packet data.

Between

Choose this operator to generate jitter, latency, or lost
                                    				packet data that occurs between one value and another value. When you choose
                                    				this operator, a second field displays, so you can set the start and end
                                    				values.

## Generate QoS Detail Reports

This section describes how to generate, view, or mail
                              		  detailed information about the system QoS.

Choose System
                                             				  Reports > QoS > Detail .

The QoS Detail window displays.

In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want the report to include. The following table describes the
                                       			 call types.

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

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911.

In the Select QoS area, check the check boxes for the
                                       			 voice-quality categories that you want included in the report. The parameters
                                       			 set in the following table provide the basis for all voice-quality categories.

Voice Quality

Description

Good

QoS for these calls represents the highest
                                                      						  possible quality.

Acceptable

QoS for these calls, although slightly degraded,
                                                      						  still fall within an acceptable range.

Fair

Although QoS for these calls is degraded, calls
                                                      						  still fall within a usable range.

Poor

QoS for these calls designates unsatisfactory
                                                      						  quality.

NA

These calls did not match any criteria for the
                                                      						  established QoS categories.

Choose the date range for the period for which you want to see QoS
                                       			 information.

In the Select Users field, you can either choose all users or
                                       			 search for particular users. To choose all users, check the Select
                                          				All Users check box. To choose individual users, enter the user ID of the
                                       			 individual in the User ID field and click the Add button.

You can also use a provided search function. See the User Search .

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Generate QoS Summary Reports

This section describes how to generate, view, or mail
                              		  summary information about the system QoS.

Perform one of the following steps:

If you are a manager, choose QoS > Summary .

If you are a CAR administrator, choose System
                                                   						Reports > QoS > Summary .

The QoS Summary window displays.

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to the following step, or use the default setting,
                                       			 Generate New Report, and go to the next step

You can only choose the automatically generated report if you
                                                      				  are logged in as a CAR administrator. The automatically generated reports do
                                                      				  not display in the drop-down list box if you are logged in as a manager.

In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want the report to include. The following table describes the
                                       			 call types.

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

If you chose Generate New Report in the previous step, choose the
                                       			 date range for the period for which you want to generate the report.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Generate QoS by Gateway Reports

Only CAR administrators generate the QoS by Gateway report.
                              		  The report provides the percentage of calls that satisfy the selected QoS
                              		  criteria for a period that is specified for the selected gateways.

Use CAR only during off-peak hours. Otherwise, data collection and report generation could cause performance degradation on
                                          the Unified Communications Manager system.

This section describes how to generate, view, or mail QoS
                              		  information about all chosen gateways.

### Before you begin

Configure the gateway by using the procedures in the Set Up Gateway .

Choose System
                                             				  Reports > QoS > By
                                             				  Gateways .

The QoS based on Gateways window displays.

In the Generate Reports field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for hour of day.

Day of Week

Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of week.

Day of Month

Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of month.

In the Jitter field, choose the operator that you want to use and enter
                                       			 the value for jitter. See the Table 1 for descriptions of operators.

In the Latency field, choose the operator that you want to use and enter
                                       			 the value for latency. See the Table 1 for descriptions of operators.

In the Lost Packets field, choose the operator that you want to use and
                                       			 enter the value for number of lost packets. See the Table 1 for descriptions of operators.

Choose the date range of the period for which you want to see call
                                       			 information.

To choose the type of gateway that you want included in the
                                       			 report, perform one of the following tasks:

To display all the gateways that are configured in the system,
                                             				  click Gateway Types in the column on the left side of the window.

To expand the tree structure and display the type of gateway
                                             				  from which you can choose, click the icon next to Gateway Types.

To choose a gateway that uses a particular route pattern/hunt
                                             				  pilot, rather than a gateway type, click Route Patterns/Hunt Pilots in the column on the left side of the window. The
                                             				  tree structure expands and displays the gateways that are associated with the
                                             				  configured Route Patterns/Hunt Pilots.

To expand the tree structure and display route pattern/hunt
                                             				  pilot for you to choose, click the icon next to Route Patterns/Hunt Pilots.

You can also search for specific route patterns/hunt pilots
                                                            						by entering part of the name of the route pattern(s)/hunt pilot(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt pilot(s) that matches the search string.

From the list, choose a gateway type.

The gateway name displays in the List of Gateways box.

The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type.

In the List of Gateways box, select the gateways that you want to
                                       			 include in the report.

You can generate a report for up to 15 gateways at a time. If
                                                      				  you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate new report."

Click the down arrow icon to move the chosen gateway to the list of Selected Gateways box.

The gateway that you chose displays in the Selected Gateways box.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports .

## Generate QoS by Call Types Reports

Only CAR administrators generate the QoS by Call Types
                              		  report. The report provides jitter, latency, and lost packet information for a
                              		  period that is specified for all calls of a chosen type.

This section describes how to generate, view, or mail QoS
                              		  information about all calls of a certain type.

Use CAR only during off-peak hours. Otherwise, data collection and report generation could cause performance degradation on
                                          the Unified Communications Manager system.

Choose System
                                             				  Reports > QoS > By Call
                                             				  Types .

The QoS based on Call Types window displays.

In the Generate Report field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for hour of day.

Day of Week

Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of week.

Day of Month

Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of month.

In the Jitter field, choose the operator that you want to use and enter
                                       			 the value for jitter. See the Table 1 for descriptions of operators.

In the Latency field, choose the operator that you want to use and enter
                                       			 the value for latency. See the Table 1 for descriptions of operators.

In the Lost Packets field, choose the operator that you want to
                                       			 use and enter the value for number of lost packets. See the Table 1 for descriptions of operators.

In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want the report to include. The following table describes the
                                       			 call types.

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

Choose the date range for the period for which you want to see
                                       			 call information.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

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

| Operator | Description |
|---|---|
| >= | Choose this operator to generate jitter, latency, or lost
                                    				packet data that is greater than or equal to the specified value. |
| = | Choose this operator to generate jitter, latency, or lost
                                    				packet data that is equal to the specified value. |
| <= | Choose this operator to generate jitter, latency, or lost
                                    				packet data that is less than or equal to the specified value. |
| N.A. | Choose this operator to preclude jitter, latency, or lost
                                    				packet data. |
| Between | Choose this operator to generate jitter, latency, or lost
                                    				packet data that occurs between one value and another value. When you choose
                                    				this operator, a second field displays, so you can set the start and end
                                    				values. |

| Step 1 | Choose System
                                             				  Reports > QoS > Detail . The QoS Detail window displays. |
|---|---|
| Step 2 | In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want the report to include. The following table describes the
                                       			 call types. Table 2. QoS Detail Report Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
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
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
| Step 3 | In the Select QoS area, check the check boxes for the
                                       			 voice-quality categories that you want included in the report. The parameters
                                       			 set in the following table provide the basis for all voice-quality categories. Table 3. QoS Detail Report Voice Quality Voice Quality Description Good QoS for these calls represents the highest
                                                      						  possible quality. Acceptable QoS for these calls, although slightly degraded,
                                                      						  still fall within an acceptable range. Fair Although QoS for these calls is degraded, calls
                                                      						  still fall within a usable range. Poor QoS for these calls designates unsatisfactory
                                                      						  quality. NA These calls did not match any criteria for the
                                                      						  established QoS categories. | Voice Quality | Description | Good | QoS for these calls represents the highest
                                                      						  possible quality. | Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still fall within an acceptable range. | Fair | Although QoS for these calls is degraded, calls
                                                      						  still fall within a usable range. | Poor | QoS for these calls designates unsatisfactory
                                                      						  quality. | NA | These calls did not match any criteria for the
                                                      						  established QoS categories. |
| Voice Quality | Description |
| Good | QoS for these calls represents the highest
                                                      						  possible quality. |
| Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still fall within an acceptable range. |
| Fair | Although QoS for these calls is degraded, calls
                                                      						  still fall within a usable range. |
| Poor | QoS for these calls designates unsatisfactory
                                                      						  quality. |
| NA | These calls did not match any criteria for the
                                                      						  established QoS categories. |
| Step 4 | Choose the date range for the period for which you want to see QoS
                                       			 information. |
| Step 5 | In the Select Users field, you can either choose all users or
                                       			 search for particular users. To choose all users, check the Select
                                          				All Users check box. To choose individual users, enter the user ID of the
                                       			 individual in the User ID field and click the Add button. Note You can also use a provided search function. See the User Search . | Note | You can also use a provided search function. See the User Search . |
| Note | You can also use a provided search function. See the User Search . |
| Step 6 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 7 | Click the View Report button. The report displays . |
| Step 8 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

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
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |

| Voice Quality | Description |
|---|---|
| Good | QoS for these calls represents the highest
                                                      						  possible quality. |
| Acceptable | QoS for these calls, although slightly degraded,
                                                      						  still fall within an acceptable range. |
| Fair | Although QoS for these calls is degraded, calls
                                                      						  still fall within a usable range. |
| Poor | QoS for these calls designates unsatisfactory
                                                      						  quality. |
| NA | These calls did not match any criteria for the
                                                      						  established QoS categories. |

| Note | You can also use a provided search function. See the User Search . |
|---|---|

| Step 1 | Perform one of the following steps: If you are a manager, choose QoS > Summary . If you are a CAR administrator, choose System
                                                   						Reports > QoS > Summary . The QoS Summary window displays. |
|---|---|
| Step 2 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to the following step, or use the default setting,
                                       			 Generate New Report, and go to the next step Note You can only choose the automatically generated report if you
                                                      				  are logged in as a CAR administrator. The automatically generated reports do
                                                      				  not display in the drop-down list box if you are logged in as a manager. | Note | You can only choose the automatically generated report if you
                                                      				  are logged in as a CAR administrator. The automatically generated reports do
                                                      				  not display in the drop-down list box if you are logged in as a manager. |
| Note | You can only choose the automatically generated report if you
                                                      				  are logged in as a CAR administrator. The automatically generated reports do
                                                      				  not display in the drop-down list box if you are logged in as a manager. |
| Step 3 | In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want the report to include. The following table describes the
                                       			 call types. Table 4. QoS Summary Report Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
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
| Step 4 | If you chose Generate New Report in the previous step, choose the
                                       			 date range for the period for which you want to generate the report. |
| Step 5 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 6 | Click the View Report button. The report displays . |
| Step 7 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Note | You can only choose the automatically generated report if you
                                                      				  are logged in as a CAR administrator. The automatically generated reports do
                                                      				  not display in the drop-down list box if you are logged in as a manager. |
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

| Caution | Use CAR only during off-peak hours. Otherwise, data collection and report generation could cause performance degradation on
                                          the Unified Communications Manager system. |
|---|---|

| Step 1 | Choose System
                                             				  Reports > QoS > By
                                             				  Gateways . The QoS based on Gateways window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the
                                       			 following table. Table 5. Generate Report Fields Parameter Description Hour of Day Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for hour of day. Day of Week Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of week. Day of Month Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of month. | Parameter | Description | Hour of Day | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for hour of day. | Day of Week | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of week. | Day of Month | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of month. |
| Parameter | Description |
| Hour of Day | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for hour of day. |
| Day of Week | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of week. |
| Day of Month | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of month. |
| Step 3 | In the Jitter field, choose the operator that you want to use and enter
                                       			 the value for jitter. See the Table 1 for descriptions of operators. |
| Step 4 | In the Latency field, choose the operator that you want to use and enter
                                       			 the value for latency. See the Table 1 for descriptions of operators. |
| Step 5 | In the Lost Packets field, choose the operator that you want to use and
                                       			 enter the value for number of lost packets. See the Table 1 for descriptions of operators. |
| Step 6 | Choose the date range of the period for which you want to see call
                                       			 information. |
| Step 7 | To choose the type of gateway that you want included in the
                                       			 report, perform one of the following tasks: To display all the gateways that are configured in the system,
                                             				  click Gateway Types in the column on the left side of the window. To expand the tree structure and display the type of gateway
                                             				  from which you can choose, click the icon next to Gateway Types. To choose a gateway that uses a particular route pattern/hunt
                                             				  pilot, rather than a gateway type, click Route Patterns/Hunt Pilots in the column on the left side of the window. The
                                             				  tree structure expands and displays the gateways that are associated with the
                                             				  configured Route Patterns/Hunt Pilots. To expand the tree structure and display route pattern/hunt
                                             				  pilot for you to choose, click the icon next to Route Patterns/Hunt Pilots. Note You can also search for specific route patterns/hunt pilots
                                                            						by entering part of the name of the route pattern(s)/hunt pilot(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt pilot(s) that matches the search string. | Note | You can also search for specific route patterns/hunt pilots
                                                            						by entering part of the name of the route pattern(s)/hunt pilot(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt pilot(s) that matches the search string. |
| Note | You can also search for specific route patterns/hunt pilots
                                                            						by entering part of the name of the route pattern(s)/hunt pilot(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt pilot(s) that matches the search string. |
| Step 8 | From the list, choose a gateway type. The gateway name displays in the List of Gateways box. Note The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type. | Note | The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type. |
| Note | The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type. |
| Step 9 | In the List of Gateways box, select the gateways that you want to
                                       			 include in the report. Note You can generate a report for up to 15 gateways at a time. If
                                                      				  you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate new report." | Note | You can generate a report for up to 15 gateways at a time. If
                                                      				  you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate new report." |
| Note | You can generate a report for up to 15 gateways at a time. If
                                                      				  you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate new report." |
| Step 10 | Click the down arrow icon to move the chosen gateway to the list of Selected Gateways box. The gateway that you chose displays in the Selected Gateways box. |
| Step 11 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 12 | Click the View Report button. The report displays . |
| Step 13 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for hour of day. |
| Day of Week | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of week. |
| Day of Month | Displays the percentage of the calls, for each
                                                      						  selected gateway, that satisfies the QoS criteria for the period that you
                                                      						  specify in Step 6 .
                                                      						  The percentage results show for day of month. |

| Note | You can also search for specific route patterns/hunt pilots
                                                            						by entering part of the name of the route pattern(s)/hunt pilot(s) in the Route
                                                            						Patterns/Hunt Pilots box in the column on the left side of the window. CAR
                                                            						searches for the route pattern(s)/hunt pilot(s) that matches the search string. |
|---|---|

| Note | The List of Gateways box will display up to 200 gateways that
                                                      				  are configured for the chosen gateway type. |
|---|---|

| Note | You can generate a report for up to 15 gateways at a time. If
                                                      				  you select more than 15 gateways, you will see the message "Select 15 or fewer gateways to generate new report." |
|---|---|

| Caution | Use CAR only during off-peak hours. Otherwise, data collection and report generation could cause performance degradation on
                                          the Unified Communications Manager system. |
|---|---|

| Step 1 | Choose System
                                             				  Reports > QoS > By Call
                                             				  Types . The QoS based on Call Types window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the
                                       			 following table. Table 6. Generate Report Fields Parameter Description Hour of Day Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for hour of day. Day of Week Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of week. Day of Month Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of month. | Parameter | Description | Hour of Day | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for hour of day. | Day of Week | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of week. | Day of Month | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of month. |
| Parameter | Description |
| Hour of Day | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for hour of day. |
| Day of Week | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of week. |
| Day of Month | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of month. |
| Step 3 | In the Jitter field, choose the operator that you want to use and enter
                                       			 the value for jitter. See the Table 1 for descriptions of operators. |
| Step 4 | In the Latency field, choose the operator that you want to use and enter
                                       			 the value for latency. See the Table 1 for descriptions of operators. |
| Step 5 | In the Lost Packets field, choose the operator that you want to
                                       			 use and enter the value for number of lost packets. See the Table 1 for descriptions of operators. |
| Step 6 | In the Select Call Types area, check the check boxes for the types
                                       			 of calls that you want the report to include. The following table describes the
                                       			 call types. Table 7. QoS Parameters by Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                      in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public
                                                      						  switched telephone network (PSTN) to numbers without an area code or that
                                                      						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network and go out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free
                                                      						  numbers or emergency calls such as 911. |
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
| Step 7 | Choose the date range for the period for which you want to see
                                       			 call information. |
| Step 8 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 9 | Click the View Report button. The report displays . |
| Step 10 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for hour of day. |
| Day of Week | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of week. |
| Day of Month | Displays the percentage of the calls, for each
                                                      						  call type, that satisfies the QoS criteria for the period that you specify in Step 7 .
                                                      						  The percentage results show for day of month. |

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