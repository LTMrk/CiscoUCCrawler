---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--7e046cfe7e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_01001.html
retrieved_at: 2026-08-21T01:33:59.603933+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR System Reports

## Chapter: CAR System Reports

# CAR System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for calls of each user.

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

## System Reports Summary Description

CDR Analysis and Reporting provides system reports for
                              		  managers and CAR administrators. Managers or CAR administrators can access the
                              		  QoS summary report. Only CAR administrators can access all other reports. This
                              		  section describes the following reports:

QoS

Detail - Available for CAR administrators. The QoS detail report provides the QoS ratings that are attributed to inbound and
                                          outbound calls on the Unified Communications Manager network for the period that you specify. Use this report to help monitor the voice quality of all calls on a user-level basis
                                          for the entire system. The call details in CDRs and CMRs and the QoS parameters that you choose provide the basis for assigning
                                          a particular voice-quality category to a call.

Summary - Available for managers and CAR administrators. This
                                          					 report provides a two-dimensional pie chart that shows the distribution of QoS
                                          					 grades that are achieved for the specified call classifications and period. The
                                          					 report also provides a table that summarizes the calls for each QoS. The call
                                          					 details in CDRs and CMRs and the QoS parameters that you choose provide the
                                          					 basis for assigning a call to a particular voice-quality category. Use this
                                          					 report to monitor the voice quality of all calls through the network.

By Gateway - Available for CAR administrators. This report
                                          					 shows the percentage of the calls for each of the chosen gateways that meet the
                                          					 QoS criteria that the user chooses. You can generate this report on an hourly,
                                          					 daily, or weekly basis.

By Call Types - Available for CAR administrators. This report
                                          					 shows the percentage of the calls for each chosen call type that meet the QoS
                                          					 criteria that the user chooses. You can generate this report on an hourly,
                                          					 daily, or weekly basis.

Traffic

Summary - Available for CAR administrators. This report
                                          					 provides information about the call volume for a period that you specify and
                                          					 include only those call types and QoS voice-quality categories that you choose.
                                          					 Use this report to determine the number of calls that are being made on an
                                          					 hourly, weekly, or daily basis. This report helps you identify high- and
                                          					 low-traffic patterns for capacity planning.

Summary by Phone Number - Available for CAR administrators.
                                          					 This report provides information about the call volume for a period and set of
                                          					 phone numbers that you specify. It includes only those call types and phone
                                          					 numbers that you choose. You can generate the report on an hourly, weekly, or
                                          					 daily basis. This report helps you determine high-usage users or groups by
                                          					 aggregating the usage level across the users that you specify.

FAC/CMC

Client Matter Code - Available for CAR administrators. This
                                          					 report allows administrators to view the originating and destination numbers,
                                          					 the date and time that the call originated, the call duration in seconds, and
                                          					 the call classification for calls that relate to each chosen client matter
                                          					 code.

Authorization Code Name - Available for CAR administrators.
                                          					 This report allows administrators to view the originating and destination
                                          					 numbers, the date and time that the call originated, the call duration in
                                          					 seconds, the call classification, and the authorization level for calls that
                                          					 relate to each chosen authorization code name.

Authorization Level - Available for CAR administrators. This
                                          					 report allows administrators to view the originating and destination numbers,
                                          					 the date and time that the call originated, the call duration in seconds, the
                                          					 authorization code name, and the call classification for calls that relate to
                                          					 each chosen authorization level.

Malicious Call Details - Available for CAR administrators. The Unified Communications Manager Malicious Call Identification (MCID) service tracks malicious calls. The Malicious Call Details report displays the details
                                    of malicious calls for a given date range.

Precedence Call Summary - Available for CAR administrators. The Unified Communications Manager Call Precedence service allows authenticated users to preempt lower priority phone calls. The PDF version of the CAR Precedence
                                    Call Summary report displays the Call Summary for the precedence values in the form of a bar chart, on an hour of day, day
                                    of week, or day of month basis, for each of the precedence levels that you choose. CAR generates one chart for each precedence
                                    level, a table for each precedence level that lists the number of call legs, and a subtable that summarizes the percentage
                                    distribution for each precedence level. CAR makes the report available on-demand; the report does not get autogenerated.

System Overview - Available for CAR administrators. Use the System Overview report to see a high-level picture of the Unified Communications Manager network. The System Overview provides the following reports:

Top 5 Users Based on Charge

Top 5 Destinations Based on Charge

Top 5 Calls Based on Charge

Top 5 Users Based on Duration

Top 5 Destinations Based on Duration

Top 5 Calls Based on Duration

Traffic Summary Hour of Day - Incoming, Internal,
                                          					 International, Local, Long Distance, On Net, Others, Tandem, and Total calls

Traffic Summary Day of Week - Incoming, Internal,
                                          					 International, Local, Long Distance, On Net, Others, Tandem, and Total calls

Traffic Summary Day of Month - Incoming, Internal,
                                          					 International, Local, Long Distance, On Net, Others, Tandem, and Total calls

QoS Summary

Gateway Summary

CDR Error - Available for CAR administrators. This report provides
                                    				statistics for the number of error records in the CAR Billing_Error table and
                                    				the reason for the errors. Use this report to determine whether CAR incurred
                                    				any errors with CDR data while the CDR data was loaded. This report lists the
                                    				percentage of CDRs that are invalid and the reason that these CDRs have been
                                    				classified as invalid.

See Related Topics .

## User Search

Many reports in CAR provide a search function, so you can
                              		  look for users. The following CAR System reports support search by user: QoS
                              		  Details and Traffic Summary by Phone Number. You can mail all reports that can
                              		  be generated by using the Send Report button.

### Before you begin

You must use the window in System Reports that allows you to
                              		  search for users.

This section describes how to search for a user.

Click the Search Users link.

A User Search window displays.

In the First Name and Last Name fields, enter characters of the
                                       			 first or last name of the user and click the Search button.

A User Search Results window displays in the same window and lists
                                          				all users who matched the search criteria that you entered.

In the row for the user that you want, click the Select link.

The user that you chose gets added to the List of Users in the
                                          				User Search window. Repeat this step to add more users.

When you have added all users, click the Close button in the User Search window.

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

| Step 1 | Click the Search Users link. A User Search window displays. |
|---|---|
| Step 2 | In the First Name and Last Name fields, enter characters of the
                                       			 first or last name of the user and click the Search button. A User Search Results window displays in the same window and lists
                                          				all users who matched the search criteria that you entered. |
| Step 3 | In the row for the user that you want, click the Select link. The user that you chose gets added to the List of Users in the
                                          				User Search window. Repeat this step to add more users. |
| Step 4 | When you have added all users, click the Close button in the User Search window. |