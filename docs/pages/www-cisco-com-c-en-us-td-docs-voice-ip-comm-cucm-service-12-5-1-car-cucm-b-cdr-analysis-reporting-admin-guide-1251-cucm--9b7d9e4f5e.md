---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--9b7d9e4f5e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0101.html
retrieved_at: 2026-08-21T01:33:42.811877+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Top N User Reports

## Chapter: Top N User Reports

# Top N User Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for their calls.

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

## Top N Reports

Top N Charge reports the users who made the maximum charge for
                           		the specified date range. If you are a manager, the report includes the top
                           		charges for all calls that users who report to you made during the specified
                           		period. If you are a CAR administrator, the report includes the top charges for
                           		all calls that all users on the system made for the specified period. You can
                           		generate each Top N Charge report with options to show the information by
                           		individual users, by destinations, or by all calls.

Top N Duration reports the top number of users that incurred a
                           		maximum time on calls during a period that you specify. If you are a manager,
                           		the report lists the top number of users who report to you that incurred a
                           		maximum time for calls that were made during the chosen date range, starting
                           		with the longest. If you are a CAR administrator, the report lists the top
                           		number of users that incurred a maximum time for calls that were made during
                           		the chosen date range, starting with the longest. You can generate each Top N
                           		Duration report with options to show the information by individual users, by
                           		destinations, or by all calls.

Top N Number of Calls reports the top number of calls that were
                           		made and received by users during a period that you specify. If you are a
                           		manager, the report lists the top number of calls by users among the users who
                           		report to you for the chosen date range. If you are a CAR administrator, the
                           		report lists the top number of calls for each user in the system. You can
                           		generate each Top N Number of Calls report with options to show the information
                           		by individual users and by extensions.

### Generate Top N by Charge Reports

This section describes how to generate, view, or mail reports
                                 		  about the top calls when classified by cost.

Perform one of the following tasks:

If you are a manager, choose Top N > By
                                                      						Charge .

If you are a CAR administrator, choose User Reports > Top
                                                      						N > By Charge .

The Top N Charge window displays.

In the Select Call Types area, check the check boxes for the types
                                          			 of calls that you want the report to include. These boxes display only when you
                                          			 choose Generate New Report from the Available Reports drop-down list box, as
                                          			 described in the following table. The next table describes the call types.

To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All .

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

Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network and enter the Unified Communications Manager network through a gateway.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911.

In the Report Type field, choose a report type as described in the
                                          			 following table.

Report Type

Description

By Individual Users

This report lists the users who incurred the
                                                         						  maximum charges.

By Destinations

This report lists the destinations that incurred
                                                         						  the maximum charges.

By All Calls

This default report lists the calls that incurred
                                                         						  the maximum charges.

Top N Destination by Charge reports display the top destinations
                                                         				  based on the charge incurred. If the same destination number comprises
                                                         				  different call classifications (for example, some are Internal, and some are
                                                         				  Incoming), they get treated and listed separately in these reports.

In the Available Reports field, choose an automatically generated report
                                          			 (if available) and go to the table or use the default setting, Generate New
                                          			 Report, and go to the table.

You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager.

Enter the number (n) of records to display in the report in the No
                                          			 of Records field. The default designates five.

Choose the date range for the period for which you want to
                                          			 generate the report.

If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports .

### Generate Top N by Duration Reports

This section describes how to generate, view, or mail reports
                                 		  about the top calls when they are classified by duration.

Perform one of the following tasks:

If you are a manager, choose Top N > By
                                                      						Duration.

If you are a CAR administrator, choose User Reports > Top
                                                      						N > By Duration. .

The Top N by Duration window displays.

In the Select Call Types area, check the check boxes for the types
                                          			 of calls that you want included in the report. These boxes display only when
                                          			 you choose Generate New Report from the Available Reports drop-down list box,
                                          			 as described in the following table. The next table describes the call types.

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

Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and then are transferred outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911.

In the Report Type field, choose a report type as described in the
                                          			 following table.

Report Type

Description

By Individual Users

This report lists the users who incurred the
                                                         						  maximum duration.

By Destinations

This report lists the destinations that incurred
                                                         						  the maximum duration.

By All Calls

This report lists the calls that incurred the
                                                         						  maximum duration.

Top N Destinations by Duration reports display the top
                                                         				  destinations based on the duration of the calls. If the same destination number
                                                         				  comprises different call classifications (for example, some are Internal and
                                                         				  some are Incoming), they get treated and listed separately in these reports.

In the Available Reports field, choose an automatically generated report
                                          			 (if available) and go to the table or use the default setting, Generate New
                                          			 Report and go to the table.

You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager.

Enter the number (n) of records to display in the report in the No
                                          			 of Records field. The default designates five.

Choose the date range for the period for which you want to
                                          			 generate the report.

If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports .

### Generate Top N by Number of Calls Reports

This section describes how to generate, view, or mail
                                 		  reports about the top calls when classified by volume.

Perform one of the following tasks:

If you are a manager, choose Top N > By Number of
                                                      						Calls .

If you are a CAR administrator, choose User Reports > Top
                                                      						N > By Number of Calls .

The Top N by Number of Calls window displays.

In the Select Call Types area, check the check boxes for the types
                                          			 of calls that you want included in the report. These boxes display only when
                                          			 you choose Generate New Report from the Available Reports drop-down list box,
                                          			 as described in the following table. The next table describes the call types.

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

Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN.

International

International calls that originate in the Unified Communications Manager network and go out through the PSTN.

Incoming

Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network.

Tandem

Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway.

Others

All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911.

In the Report Type field, choose a report type as described in the
                                          			 following table.

Report Type

Description

By Individual Users

This report lists the users who incurred the
                                                         						  maximum number of calls.

By Extensions

This report lists the extensions that have
                                                         						  placed or received the greatest number of calls in your group (managers) or the
                                                         						  system (CAR administrators).

In the Available Reports field, choose an automatically generated report
                                          			 (if available) and go to the table or use the default Generate New Report and
                                          			 go to the table.

You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager.

Enter the number (n) of records that display in the report in the
                                          			 No of Records field. The default designates five.

Choose the date range for the period for which you want to
                                          			 generate the report.

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

| Step 1 | Perform one of the following tasks: If you are a manager, choose Top N > By
                                                      						Charge . If you are a CAR administrator, choose User Reports > Top
                                                      						N > By Charge . The Top N Charge window displays. |
|---|---|
| Step 2 | In the Select Call Types area, check the check boxes for the types
                                          			 of calls that you want the report to include. These boxes display only when you
                                          			 choose Generate New Report from the Available Reports drop-down list box, as
                                          			 described in the following table. The next table describes the call types. Tip To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All . Table 1. Top N by Charge Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network and enter the Unified Communications Manager network through a gateway. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. | Tip | To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All . | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network and enter the Unified Communications Manager network through a gateway. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |
| Tip | To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All . |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network and enter the Unified Communications Manager network through a gateway. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |
| Step 3 | In the Report Type field, choose a report type as described in the
                                          			 following table. Table 2. Top N by Charge Report Types Report Type Description By Individual Users This report lists the users who incurred the
                                                         						  maximum charges. By Destinations This report lists the destinations that incurred
                                                         						  the maximum charges. By All Calls This default report lists the calls that incurred
                                                         						  the maximum charges. Note Top N Destination by Charge reports display the top destinations
                                                         				  based on the charge incurred. If the same destination number comprises
                                                         				  different call classifications (for example, some are Internal, and some are
                                                         				  Incoming), they get treated and listed separately in these reports. | Report Type | Description | By Individual Users | This report lists the users who incurred the
                                                         						  maximum charges. | By Destinations | This report lists the destinations that incurred
                                                         						  the maximum charges. | By All Calls | This default report lists the calls that incurred
                                                         						  the maximum charges. | Note | Top N Destination by Charge reports display the top destinations
                                                         				  based on the charge incurred. If the same destination number comprises
                                                         				  different call classifications (for example, some are Internal, and some are
                                                         				  Incoming), they get treated and listed separately in these reports. |
| Report Type | Description |
| By Individual Users | This report lists the users who incurred the
                                                         						  maximum charges. |
| By Destinations | This report lists the destinations that incurred
                                                         						  the maximum charges. |
| By All Calls | This default report lists the calls that incurred
                                                         						  the maximum charges. |
| Note | Top N Destination by Charge reports display the top destinations
                                                         				  based on the charge incurred. If the same destination number comprises
                                                         				  different call classifications (for example, some are Internal, and some are
                                                         				  Incoming), they get treated and listed separately in these reports. |
| Step 4 | In the Available Reports field, choose an automatically generated report
                                          			 (if available) and go to the table or use the default setting, Generate New
                                          			 Report, and go to the table. Note You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager. | Note | You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager. |
| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager. |
| Step 5 | Enter the number (n) of records to display in the report in the No
                                          			 of Records field. The default designates five. |
| Step 6 | Choose the date range for the period for which you want to
                                          			 generate the report. |
| Step 7 | If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records. |
| Step 8 | Click the View Report button. The report displays . |
| Step 9 | If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports . |

| Tip | To check all check boxes, click Select All ; to uncheck the check boxes, click Clear All . |
|---|---|

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network and enter the Unified Communications Manager network through a gateway. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |

| Report Type | Description |
|---|---|
| By Individual Users | This report lists the users who incurred the
                                                         						  maximum charges. |
| By Destinations | This report lists the destinations that incurred
                                                         						  the maximum charges. |
| By All Calls | This default report lists the calls that incurred
                                                         						  the maximum charges. |

| Note | Top N Destination by Charge reports display the top destinations
                                                         				  based on the charge incurred. If the same destination number comprises
                                                         				  different call classifications (for example, some are Internal, and some are
                                                         				  Incoming), they get treated and listed separately in these reports. |
|---|---|

| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager. |
|---|---|

| Step 1 | Perform one of the following tasks: If you are a manager, choose Top N > By
                                                      						Duration. If you are a CAR administrator, choose User Reports > Top
                                                      						N > By Duration. . The Top N by Duration window displays. |
|---|---|
| Step 2 | In the Select Call Types area, check the check boxes for the types
                                          			 of calls that you want included in the report. These boxes display only when
                                          			 you choose Generate New Report from the Available Reports drop-down list box,
                                          			 as described in the following table. The next table describes the call types. Table 3. Top N by Duration Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and then are transferred outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and then are transferred outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and then are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |
| Step 3 | In the Report Type field, choose a report type as described in the
                                          			 following table. Table 4. Top N by Duration Report Types Report Type Description By Individual Users This report lists the users who incurred the
                                                         						  maximum duration. By Destinations This report lists the destinations that incurred
                                                         						  the maximum duration. By All Calls This report lists the calls that incurred the
                                                         						  maximum duration. Note Top N Destinations by Duration reports display the top
                                                         				  destinations based on the duration of the calls. If the same destination number
                                                         				  comprises different call classifications (for example, some are Internal and
                                                         				  some are Incoming), they get treated and listed separately in these reports. | Report Type | Description | By Individual Users | This report lists the users who incurred the
                                                         						  maximum duration. | By Destinations | This report lists the destinations that incurred
                                                         						  the maximum duration. | By All Calls | This report lists the calls that incurred the
                                                         						  maximum duration. | Note | Top N Destinations by Duration reports display the top
                                                         				  destinations based on the duration of the calls. If the same destination number
                                                         				  comprises different call classifications (for example, some are Internal and
                                                         				  some are Incoming), they get treated and listed separately in these reports. |
| Report Type | Description |
| By Individual Users | This report lists the users who incurred the
                                                         						  maximum duration. |
| By Destinations | This report lists the destinations that incurred
                                                         						  the maximum duration. |
| By All Calls | This report lists the calls that incurred the
                                                         						  maximum duration. |
| Note | Top N Destinations by Duration reports display the top
                                                         				  destinations based on the duration of the calls. If the same destination number
                                                         				  comprises different call classifications (for example, some are Internal and
                                                         				  some are Incoming), they get treated and listed separately in these reports. |
| Step 4 | In the Available Reports field, choose an automatically generated report
                                          			 (if available) and go to the table or use the default setting, Generate New
                                          			 Report and go to the table. Note You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. | Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
| Step 5 | Enter the number (n) of records to display in the report in the No
                                          			 of Records field. The default designates five. |
| Step 6 | Choose the date range for the period for which you want to
                                          			 generate the report. |
| Step 7 | If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records. |
| Step 8 | Click the View Report button. The report displays . |
| Step 9 | If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports . |

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and then are transferred outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |

| Report Type | Description |
|---|---|
| By Individual Users | This report lists the users who incurred the
                                                         						  maximum duration. |
| By Destinations | This report lists the destinations that incurred
                                                         						  the maximum duration. |
| By All Calls | This report lists the calls that incurred the
                                                         						  maximum duration. |

| Note | Top N Destinations by Duration reports display the top
                                                         				  destinations based on the duration of the calls. If the same destination number
                                                         				  comprises different call classifications (for example, some are Internal and
                                                         				  some are Incoming), they get treated and listed separately in these reports. |
|---|---|

| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
|---|---|

| Step 1 | Perform one of the following tasks: If you are a manager, choose Top N > By Number of
                                                      						Calls . If you are a CAR administrator, choose User Reports > Top
                                                      						N > By Number of Calls . The Top N by Number of Calls window displays. |
|---|---|
| Step 2 | In the Select Call Types area, check the check boxes for the types
                                          			 of calls that you want included in the report. These boxes display only when
                                          			 you choose Generate New Report from the Available Reports drop-down list box,
                                          			 as described in the following table. The next table describes the call types. Table 5. Top N by Number of Calls Call Types Call Type Description On Net Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . Internal Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). Local Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. Long Distance Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. International International calls that originate in the Unified Communications Manager network and go out through the PSTN. Incoming Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. Tandem Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. Others All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. | Call Type | Description | On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . | Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). | Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. | Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. | International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. | Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. | Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. | Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |
| Call Type | Description |
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |
| Step 3 | In the Report Type field, choose a report type as described in the
                                          			 following table. Table 6. Top N by Number of Calls Report Types Report Type Description By Individual Users This report lists the users who incurred the
                                                         						  maximum number of calls. By Extensions This report lists the extensions that have
                                                         						  placed or received the greatest number of calls in your group (managers) or the
                                                         						  system (CAR administrators). | Report Type | Description | By Individual Users | This report lists the users who incurred the
                                                         						  maximum number of calls. | By Extensions | This report lists the extensions that have
                                                         						  placed or received the greatest number of calls in your group (managers) or the
                                                         						  system (CAR administrators). |
| Report Type | Description |
| By Individual Users | This report lists the users who incurred the
                                                         						  maximum number of calls. |
| By Extensions | This report lists the extensions that have
                                                         						  placed or received the greatest number of calls in your group (managers) or the
                                                         						  system (CAR administrators). |
| Step 4 | In the Available Reports field, choose an automatically generated report
                                          			 (if available) and go to the table or use the default Generate New Report and
                                          			 go to the table. Note You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. | Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
| Step 5 | Enter the number (n) of records that display in the report in the
                                          			 No of Records field. The default designates five. |
| Step 6 | Choose the date range for the period for which you want to
                                          			 generate the report. |
| Step 7 | If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records. |
| Step 8 | Click the View Report button. The report displays . |
| Step 9 | If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports . |

| Call Type | Description |
|---|---|
| On Net | Outgoing calls that originate on one Unified Communications Manager network, go out through a trunk, and terminate on a different Unified Communications Manager network. For CAR purposes, be aware that any outgoing call can be classified as an On Net call if it is configured as such
                                                         in the CAR dial plan configuration window. See Set Up Dial Plan . |
| Internal | Calls, including intracluster calls, that originate in the Unified Communications Manager network and end in the same Unified Communications Manager network (no gateways or trunks are used). |
| Local | Local calls that are routed through the public
                                                         						  switched telephone network (PSTN) to numbers without an area code or that
                                                         						  include one of the local area codes. |
| Long Distance | Long-distance calls that originate in the Unified Communications Manager network going out through the PSTN. |
| International | International calls that originate in the Unified Communications Manager network and go out through the PSTN. |
| Incoming | Inbound calls that originate outside the Unified Communications Manager network, enter through a gateway, and go into the Unified Communications Manager network. |
| Tandem | Inbound calls that originate outside the Unified Communications Manager network, enter the Unified Communications Manager network through a gateway, and transfer outbound from the Unified Communications Manager network through a gateway. |
| Others | All other outgoing calls, such as toll-free
                                                         						  numbers or emergency calls such as 911. |

| Report Type | Description |
|---|---|
| By Individual Users | This report lists the users who incurred the
                                                         						  maximum number of calls. |
| By Extensions | This report lists the extensions that have
                                                         						  placed or received the greatest number of calls in your group (managers) or the
                                                         						  system (CAR administrators). |

| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
|---|---|