---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--f5a6c34a01
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0100.html
retrieved_at: 2026-08-21T01:33:38.614049+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Bills User Reports

## Chapter: Bills User Reports

# Bills User Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for their calls.

This chapter contains the following topics:

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

## Bills Reports

Individual bills provide call information for the date range
                           		that you specify. You can either view reports that the system automatically
                           		generates or generate new reports. Only CAR administrators can schedule reports
                           		for automatic generation. If you are an administrator, see Automatic Generation of CAR Reports and Alerts for more information.

Department bills provide call information and QoS ratings. If
                           		you are a manager, you can generate a summary or detailed report of the calls
                           		that all users who report to you made, or only those users that you choose.

If you are a CAR administrator, you can generate a summary or
                           		detailed report of the calls that some or all users in the system made. This
                           		report helps you keep track of all calls on a user-level basis for the entire
                           		system.

This section contains the following procedures:

Generate Individual Bills Reports

Generate Department Bills Reports

### Generate Individual Bills Reports

This section describes how to view, or mail, summary or
                                 		  detail information reports about users, managers, and administrators.
                                 		  Administration users do not get access to this report.

Before you can configure the Individual Bills report, you must ensure that a device with an assigned Owner User ID exists
                                 in Cisco Unified CM Administration for each user that is included in the report. Use the following procedure to create the Owner User IDs:

In Cisco Unified CM Administration , choose Device > Add a New Phone > Phone > Phone Configuration .

Add the information for the device and the user.

If the Extension Mobility feature is enabled on the device and the user logs in to the phone and places a call, the User ID
                                                         that gets recorded in the CDRs matches the logged in User ID. If extension mobility is not enabled on the device, the User
                                                         ID that gets recorded in the CDRs equals the "Owner User ID" that is configured for the device. In the situation were neither the User ID nor the Owner User ID is configured (that is,
                                                         extension mobility is not enabled, and the Owner User ID is not configured), the User ID field in the CDRs gets recorded as
                                                         blank. In this situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs do not appear in the Individual Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database. If you look for the reports for a particular end user in the directory, either the
                                                         User ID for the particular end user must be configured as the Owner User ID for the device, or the particular end user must
                                                         have logged in to the device with the extension mobility feature enabled.

You are now ready to configure the Individual Bills report.

Perform one of the following tasks:

If you are a user or manager, choose Bills > Individual .

If you are a CAR administrator, choose User
                                                      						Reports > Bills > Individual .

The Individual Bill window displays.

In the Report Type field, choose Summary or Detail .

Summary reports provide a summary of all calls for a chosen
                                             				period, including the call classification (Internal, Local, Long Distance,
                                             				International, or On Net), the QoS information, the total number of calls that
                                             				were made, and the charges that were incurred. Detailed reports provide the
                                             				date of the call, origination time of the call, origination number (calling
                                             				number), destination number (called number), call classification (On Net,
                                             				Internal, Local, Long Distance, International, or Others), QoS information,
                                             				duration of time for which the call lasted (in seconds), and the charge for the
                                             				call, based on the rating engine configuration in CAR for all calls over a
                                             				chosen period.

In the Available Reports field, choose an automatically generated
                                          			 report (if available) and go to Step 8 or use the default Generate New Report and go to Step 6 .

You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager or
                                                         				  individual user.

Choose the date range for the period for which you want to see
                                          			 call information.

If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report, follow
                                          			 the procedure that is described in the Mail Reports .

### Generate Department Bills Reports

This section describes how to generate, view, or mail summary
                                 		  or detail information about departmental bills. Application users do not get
                                 		  access to this report.

Before you can configure the Department Bills report, you
                                 		  must ensure a device with an assigned Owner User ID and Manager User ID exists
                                 		  in Cisco Unified CM Administration for each user that is included
                                 		  in the report. Use the following procedure to add the device, Owner User ID,
                                 		  and the associated Manager User ID for each user:

In Cisco Unified CM Administration , choose Device > Phone > Add
                                                				  a New Phone > Phone
                                                				  Configuration .

Add the information for the device and the user.

In Cisco Unified CM Administration , choose User Management > End
                                                				  User > Add .

Add the Manager User ID information to the end user information.

If the Extension Mobility feature is enabled on the device and
                                                         				  the user logs into the phone and places a call, the User ID that gets recorded
                                                         				  in the CDRs is the logged in User ID. If extension mobility is not enabled on
                                                         				  the device, the User ID that gets recorded in the CDRs specifies the "Owner User ID" that is configured for the device. In the
                                                         				  situation where neither the User ID nor the Owner User ID is configured (that
                                                         				  is, extension mobility is not enabled, and the Owner User ID is not
                                                         				  configured), the User ID field in the CDRs gets recorded as blank. In this
                                                         				  situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs are
                                                         				  not seen in the Department Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database.
                                                         				  If you look for the reports for a particular end user in the directory, either
                                                         				  the User ID for the particular end user must be configured as the Owner User ID
                                                         				  for the device or the particular end user must have logged in to the device
                                                         				  with the Extension Mobility feature enabled.

You are now ready to configure the Department Bills reports.

Perform one of the following tasks:

If you are a manager, choose Bills > Department .

If you are a CAR administrator, choose User
                                                      						Reports > Bills > Department .

The Department Bill window displays.

In the Report Type field, choose Summary or Detail .

Summary reports provide a summary of all calls for a chosen
                                             				period, including the call classification (On Net, Internal, Local, Long
                                             				Distance, International, Incoming, Tandem, or Others), the QoS information, the
                                             				total number of calls that were made, and the charges that were incurred.
                                             				Detailed reports provide the date of the call, origination time of the call,
                                             				origination number (calling number), destination number (called number), call
                                             				classification (On Net, Internal, Local, Long Distance, International, or
                                             				Others), QoS information, duration for which the call lasted (in seconds), and
                                             				the charge for the call, based on the rating engine configuration in CAR for
                                             				all calls over a chosen period.

In the Available Reports field, choose an automatically generated
                                          			 report (if available) and go to Step 17 or use the default Generate New Report and go to Step 8 .

You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager.

Choose the date range for the period for which you want to see
                                          			 call information.

If you are a manager, continue with Step 10 ;
                                          			 otherwise, if you are a CAR administrator, continue with Step 14 .

To choose all of your direct reports, check the Select All Reportees check box.

The List of Reportees shows your direct reports.

Click the Down button to view your direct reports.
                                                         				  Use the Up and Down buttons to move up and down the
                                                         				  report chain information.

To choose individual reportees, choose the reports that are shown
                                          			 in the List of Reportees.

Click the Add button.

The department bill includes only users who are listed in the
                                             				Selected Reportees box.

To see the reportees under a particular user, choose the user and
                                          			 click the Down button.

All reportees to the chosen user display.

If you are a CAR administrator, check the Select All
                                             				Users check box to include all users. If you are a manager, proceed to Step 16 .

To specify individual users, enter the user ID of the individual
                                          			 that you want to include in the report in the User ID field. Click the Add button.

You can also use a provided user search function. See the Search Users ,
                                             				for instructions on using the search feature.

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

| Step 1 | In Cisco Unified CM Administration , choose Device > Add a New Phone > Phone > Phone Configuration . |
|---|---|
| Step 2 | Add the information for the device and the user. Note If the Extension Mobility feature is enabled on the device and the user logs in to the phone and places a call, the User ID
                                                         that gets recorded in the CDRs matches the logged in User ID. If extension mobility is not enabled on the device, the User
                                                         ID that gets recorded in the CDRs equals the "Owner User ID" that is configured for the device. In the situation were neither the User ID nor the Owner User ID is configured (that is,
                                                         extension mobility is not enabled, and the Owner User ID is not configured), the User ID field in the CDRs gets recorded as
                                                         blank. In this situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs do not appear in the Individual Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database. If you look for the reports for a particular end user in the directory, either the
                                                         User ID for the particular end user must be configured as the Owner User ID for the device, or the particular end user must
                                                         have logged in to the device with the extension mobility feature enabled. You are now ready to configure the Individual Bills report. | Note | If the Extension Mobility feature is enabled on the device and the user logs in to the phone and places a call, the User ID
                                                         that gets recorded in the CDRs matches the logged in User ID. If extension mobility is not enabled on the device, the User
                                                         ID that gets recorded in the CDRs equals the "Owner User ID" that is configured for the device. In the situation were neither the User ID nor the Owner User ID is configured (that is,
                                                         extension mobility is not enabled, and the Owner User ID is not configured), the User ID field in the CDRs gets recorded as
                                                         blank. In this situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs do not appear in the Individual Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database. If you look for the reports for a particular end user in the directory, either the
                                                         User ID for the particular end user must be configured as the Owner User ID for the device, or the particular end user must
                                                         have logged in to the device with the extension mobility feature enabled. |
| Note | If the Extension Mobility feature is enabled on the device and the user logs in to the phone and places a call, the User ID
                                                         that gets recorded in the CDRs matches the logged in User ID. If extension mobility is not enabled on the device, the User
                                                         ID that gets recorded in the CDRs equals the "Owner User ID" that is configured for the device. In the situation were neither the User ID nor the Owner User ID is configured (that is,
                                                         extension mobility is not enabled, and the Owner User ID is not configured), the User ID field in the CDRs gets recorded as
                                                         blank. In this situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs do not appear in the Individual Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database. If you look for the reports for a particular end user in the directory, either the
                                                         User ID for the particular end user must be configured as the Owner User ID for the device, or the particular end user must
                                                         have logged in to the device with the extension mobility feature enabled. |
| Step 3 | Perform one of the following tasks: If you are a user or manager, choose Bills > Individual . If you are a CAR administrator, choose User
                                                      						Reports > Bills > Individual . The Individual Bill window displays. |
| Step 4 | In the Report Type field, choose Summary or Detail . Summary reports provide a summary of all calls for a chosen
                                             				period, including the call classification (Internal, Local, Long Distance,
                                             				International, or On Net), the QoS information, the total number of calls that
                                             				were made, and the charges that were incurred. Detailed reports provide the
                                             				date of the call, origination time of the call, origination number (calling
                                             				number), destination number (called number), call classification (On Net,
                                             				Internal, Local, Long Distance, International, or Others), QoS information,
                                             				duration of time for which the call lasted (in seconds), and the charge for the
                                             				call, based on the rating engine configuration in CAR for all calls over a
                                             				chosen period. |
| Step 5 | In the Available Reports field, choose an automatically generated
                                          			 report (if available) and go to Step 8 or use the default Generate New Report and go to Step 6 . Note You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager or
                                                         				  individual user. | Note | You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager or
                                                         				  individual user. |
| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager or
                                                         				  individual user. |
| Step 6 | Choose the date range for the period for which you want to see
                                          			 call information. |
| Step 7 | If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records. |
| Step 8 | Click the View Report button. The report displays . |
| Step 9 | If you want to mail the report, click the Send Report button. To send the report, follow
                                          			 the procedure that is described in the Mail Reports . |

| Note | If the Extension Mobility feature is enabled on the device and the user logs in to the phone and places a call, the User ID
                                                         that gets recorded in the CDRs matches the logged in User ID. If extension mobility is not enabled on the device, the User
                                                         ID that gets recorded in the CDRs equals the "Owner User ID" that is configured for the device. In the situation were neither the User ID nor the Owner User ID is configured (that is,
                                                         extension mobility is not enabled, and the Owner User ID is not configured), the User ID field in the CDRs gets recorded as
                                                         blank. In this situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs do not appear in the Individual Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database. If you look for the reports for a particular end user in the directory, either the
                                                         User ID for the particular end user must be configured as the Owner User ID for the device, or the particular end user must
                                                         have logged in to the device with the extension mobility feature enabled. |
|---|---|

| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as CAR administrator. The automatically generated reports do not
                                                         				  display in the drop-down list box if you are logged in as a manager or
                                                         				  individual user. |
|---|---|

| Step 1 | In Cisco Unified CM Administration , choose Device > Phone > Add
                                                				  a New Phone > Phone
                                                				  Configuration . |
|---|---|
| Step 2 | Add the information for the device and the user. |
| Step 3 | In Cisco Unified CM Administration , choose User Management > End
                                                				  User > Add . |
| Step 4 | Add the Manager User ID information to the end user information. Note If the Extension Mobility feature is enabled on the device and
                                                         				  the user logs into the phone and places a call, the User ID that gets recorded
                                                         				  in the CDRs is the logged in User ID. If extension mobility is not enabled on
                                                         				  the device, the User ID that gets recorded in the CDRs specifies the "Owner User ID" that is configured for the device. In the
                                                         				  situation where neither the User ID nor the Owner User ID is configured (that
                                                         				  is, extension mobility is not enabled, and the Owner User ID is not
                                                         				  configured), the User ID field in the CDRs gets recorded as blank. In this
                                                         				  situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs are
                                                         				  not seen in the Department Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database.
                                                         				  If you look for the reports for a particular end user in the directory, either
                                                         				  the User ID for the particular end user must be configured as the Owner User ID
                                                         				  for the device or the particular end user must have logged in to the device
                                                         				  with the Extension Mobility feature enabled. You are now ready to configure the Department Bills reports. | Note | If the Extension Mobility feature is enabled on the device and
                                                         				  the user logs into the phone and places a call, the User ID that gets recorded
                                                         				  in the CDRs is the logged in User ID. If extension mobility is not enabled on
                                                         				  the device, the User ID that gets recorded in the CDRs specifies the "Owner User ID" that is configured for the device. In the
                                                         				  situation where neither the User ID nor the Owner User ID is configured (that
                                                         				  is, extension mobility is not enabled, and the Owner User ID is not
                                                         				  configured), the User ID field in the CDRs gets recorded as blank. In this
                                                         				  situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs are
                                                         				  not seen in the Department Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database.
                                                         				  If you look for the reports for a particular end user in the directory, either
                                                         				  the User ID for the particular end user must be configured as the Owner User ID
                                                         				  for the device or the particular end user must have logged in to the device
                                                         				  with the Extension Mobility feature enabled. |
| Note | If the Extension Mobility feature is enabled on the device and
                                                         				  the user logs into the phone and places a call, the User ID that gets recorded
                                                         				  in the CDRs is the logged in User ID. If extension mobility is not enabled on
                                                         				  the device, the User ID that gets recorded in the CDRs specifies the "Owner User ID" that is configured for the device. In the
                                                         				  situation where neither the User ID nor the Owner User ID is configured (that
                                                         				  is, extension mobility is not enabled, and the Owner User ID is not
                                                         				  configured), the User ID field in the CDRs gets recorded as blank. In this
                                                         				  situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs are
                                                         				  not seen in the Department Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database.
                                                         				  If you look for the reports for a particular end user in the directory, either
                                                         				  the User ID for the particular end user must be configured as the Owner User ID
                                                         				  for the device or the particular end user must have logged in to the device
                                                         				  with the Extension Mobility feature enabled. |
| Step 5 | Perform one of the following tasks: If you are a manager, choose Bills > Department . If you are a CAR administrator, choose User
                                                      						Reports > Bills > Department . The Department Bill window displays. |
| Step 6 | In the Report Type field, choose Summary or Detail . Summary reports provide a summary of all calls for a chosen
                                             				period, including the call classification (On Net, Internal, Local, Long
                                             				Distance, International, Incoming, Tandem, or Others), the QoS information, the
                                             				total number of calls that were made, and the charges that were incurred.
                                             				Detailed reports provide the date of the call, origination time of the call,
                                             				origination number (calling number), destination number (called number), call
                                             				classification (On Net, Internal, Local, Long Distance, International, or
                                             				Others), QoS information, duration for which the call lasted (in seconds), and
                                             				the charge for the call, based on the rating engine configuration in CAR for
                                             				all calls over a chosen period. |
| Step 7 | In the Available Reports field, choose an automatically generated
                                          			 report (if available) and go to Step 17 or use the default Generate New Report and go to Step 8 . Note You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. | Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
| Step 8 | Choose the date range for the period for which you want to see
                                          			 call information. |
| Step 9 | If you are a manager, continue with Step 10 ;
                                          			 otherwise, if you are a CAR administrator, continue with Step 14 . |
| Step 10 | To choose all of your direct reports, check the Select All Reportees check box. The List of Reportees shows your direct reports. Note Click the Down button to view your direct reports.
                                                         				  Use the Up and Down buttons to move up and down the
                                                         				  report chain information. | Note | Click the Down button to view your direct reports.
                                                         				  Use the Up and Down buttons to move up and down the
                                                         				  report chain information. |
| Note | Click the Down button to view your direct reports.
                                                         				  Use the Up and Down buttons to move up and down the
                                                         				  report chain information. |
| Step 11 | To choose individual reportees, choose the reports that are shown
                                          			 in the List of Reportees. |
| Step 12 | Click the Add button. The department bill includes only users who are listed in the
                                             				Selected Reportees box. |
| Step 13 | To see the reportees under a particular user, choose the user and
                                          			 click the Down button. All reportees to the chosen user display. |
| Step 14 | If you are a CAR administrator, check the Select All
                                             				Users check box to include all users. If you are a manager, proceed to Step 16 . |
| Step 15 | To specify individual users, enter the user ID of the individual
                                          			 that you want to include in the report in the User ID field. Click the Add button. You can also use a provided user search function. See the Search Users ,
                                             				for instructions on using the search feature. |
| Step 16 | If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records. |
| Step 17 | Click the View Report button. The report displays . |
| Step 18 | If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports . |

| Note | If the Extension Mobility feature is enabled on the device and
                                                         				  the user logs into the phone and places a call, the User ID that gets recorded
                                                         				  in the CDRs is the logged in User ID. If extension mobility is not enabled on
                                                         				  the device, the User ID that gets recorded in the CDRs specifies the "Owner User ID" that is configured for the device. In the
                                                         				  situation where neither the User ID nor the Owner User ID is configured (that
                                                         				  is, extension mobility is not enabled, and the Owner User ID is not
                                                         				  configured), the User ID field in the CDRs gets recorded as blank. In this
                                                         				  situation, CAR uses the default User ID of "_unspecified user" when it loads the CDRs, and the CDRs are
                                                         				  not seen in the Department Bills User reports because no user by the name "_unspecifieduser" exists in the Cisco Unified CM database.
                                                         				  If you look for the reports for a particular end user in the directory, either
                                                         				  the User ID for the particular end user must be configured as the Owner User ID
                                                         				  for the device or the particular end user must have logged in to the device
                                                         				  with the Extension Mobility feature enabled. |
|---|---|

| Note | You can only choose the automatically generated report if you
                                                         				  are logged in as a CAR administrator. The automatically generated reports do
                                                         				  not display in the drop-down list box if you are logged in as a manager. |
|---|---|

| Note | Click the Down button to view your direct reports.
                                                         				  Use the Up and Down buttons to move up and down the
                                                         				  report chain information. |
|---|---|