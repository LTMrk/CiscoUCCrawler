---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--1da245462f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0110.html
retrieved_at: 2026-08-21T01:33:46.989205+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Assistant User Reports

## Chapter: Assistant User Reports

# Assistant User Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for their calls.

This chapter contains the following topics:

Assistant Usage Reports

Related Topics

Additional Documentation

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

## Assistant Usage Reports

CAR provides call completion usage reports for the following Cisco Unified Communications Manager Assistant users: manager(s) and the configured/assigned assistant(s) that manage the calls of the manager(s). Only CAR administrators
                           can generate Cisco Unified Communications Manager Assistant reports. The Cisco Unified Communications Manager Assistant menu allows you to choose all or a subset of managers or assistants by using simple search functionality that is based on
                           partial or complete first or last name. You can generate these reports on demand in either PDF or CSV format and e-mail them.
                           In addition, you can choose the time range and generate either detailed or summary level reports.

The manager reports can include calls that only managers handle
                           		for themselves, calls that only assistants handle for managers, and calls that
                           		qualify in either case. The summary report for a manager shows the number of
                           		calls of each call classification type, the total number of calls, and the
                           		total duration of all calls (in seconds) for each manager and/or assistant. The
                           		detail report for a manager shows the date, origination time, origination
                           		number (calling number), destination (called number), call classification, and
                           		duration (in seconds) for each call for each manager and/or assistants, and the
                           		cumulative duration total for the manager.

The assistant reports can include calls that only assistants
                           		handle for themselves, or calls that only assistants handle for managers, and
                           		calls that qualify in either case. The summary report for an assistant shows
                           		the number of calls of each type and total of them apart from duration for each
                           		manager (and/or assistant). The detail assistant report shows the date,
                           		origination time, origination (calling number), destination (called number),
                           		call classification, and duration (in seconds) for each call for all the
                           		managers (and/or assistant) and the cumulative duration total for the
                           		assistant.

This section contains the following procedures:

Generate Manager Call Usage Assistant Reports

Generate Assistant Call Usage Assistant Reports

### Generate Manager Call Usage Assistant Reports

This section describes how to generate a manager call usage report for Cisco Unified Communications Manager Assistant . Only CAR administrators can generate Cisco Unified Communications Manager Assistant reports.

Choose User Reports > Cisco Unified Communications Manager Assistant > Manager Call Usage .

The Call Usage for Manager window displays.

From the Report Type drop-down list, choose either Summary or Detail .

From the Calls handled by drop-down list, choose Manager , Assistant for Manager , or Manager & Assistant for Manager .

Choose the date range for the period for which you want to see
                                          			 call information.

In the Select Manager(s) box, either check the Select All Manager(s) check box and enter a
                                          			 manager ID or click the Select Manager(s) link to search for a manager ID and enter the ID(s) in
                                          			 the Manager Id field.

Click Add .

The ID that you chose displays in the Selected Manager(s) box.

If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports .

To remove a manager from the Selected Manager(s) list, highlight
                                                         				  the ID and click Remove . To remove all managers from the
                                                         				  list, click Remove All .

### Generate Assistant Call Usage Assistant Reports

This section describes how to generate an assistant call usage report for Cisco Unified Communications Manager Assistant . Only CAR administrators can generate these reports.

Choose User
                                                				  Reports > Cisco Unified Communications Manager
                                                				  Assistant > Assistant Call Usage .

The Call Usage for Assistant window displays.

From the Report Type drop-down list, choose either Summary or Detail .

From the Calls handled by drop-down list, choose Assistant , Assistant for Manager , or Assistant & Assistant for Manager .

Choose the date range for the period for which you want to see
                                          			 call information.

In the Select Assistant(s) box, either check the Select All Assistant(s) check box and enter an
                                          			 assistant ID or click the Select Assistant(s) link to search for an assistant ID and enter the ID(s) in
                                          			 the Assistant Id field.

Click Add .

The ID that you chose displays in the Selected Assistant(s) box.

If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports .

To remove a manager from the Selected Assistant(s) list,
                                                         				  highlight the ID and click Remove . To remove all assistants from the
                                                         				  list, click Remove All .

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

| Step 1 | Choose User Reports > Cisco Unified Communications Manager Assistant > Manager Call Usage . The Call Usage for Manager window displays. |
|---|---|
| Step 2 | From the Report Type drop-down list, choose either Summary or Detail . |
| Step 3 | From the Calls handled by drop-down list, choose Manager , Assistant for Manager , or Manager & Assistant for Manager . |
| Step 4 | Choose the date range for the period for which you want to see
                                          			 call information. |
| Step 5 | In the Select Manager(s) box, either check the Select All Manager(s) check box and enter a
                                          			 manager ID or click the Select Manager(s) link to search for a manager ID and enter the ID(s) in
                                          			 the Manager Id field. |
| Step 6 | Click Add . The ID that you chose displays in the Selected Manager(s) box. |
| Step 7 | If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records. The report displays . |
| Step 8 | If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports . Note To remove a manager from the Selected Manager(s) list, highlight
                                                         				  the ID and click Remove . To remove all managers from the
                                                         				  list, click Remove All . | Note | To remove a manager from the Selected Manager(s) list, highlight
                                                         				  the ID and click Remove . To remove all managers from the
                                                         				  list, click Remove All . |
| Note | To remove a manager from the Selected Manager(s) list, highlight
                                                         				  the ID and click Remove . To remove all managers from the
                                                         				  list, click Remove All . |

| Note | To remove a manager from the Selected Manager(s) list, highlight
                                                         				  the ID and click Remove . To remove all managers from the
                                                         				  list, click Remove All . |
|---|---|

| Step 1 | Choose User
                                                				  Reports > Cisco Unified Communications Manager
                                                				  Assistant > Assistant Call Usage . The Call Usage for Assistant window displays. |
|---|---|
| Step 2 | From the Report Type drop-down list, choose either Summary or Detail . |
| Step 3 | From the Calls handled by drop-down list, choose Assistant , Assistant for Manager , or Assistant & Assistant for Manager . |
| Step 4 | Choose the date range for the period for which you want to see
                                          			 call information. |
| Step 5 | In the Select Assistant(s) box, either check the Select All Assistant(s) check box and enter an
                                          			 assistant ID or click the Select Assistant(s) link to search for an assistant ID and enter the ID(s) in
                                          			 the Assistant Id field. |
| Step 6 | Click Add . The ID that you chose displays in the Selected Assistant(s) box. |
| Step 7 | If you want the report in CSV format, choose CSV (comma separated
                                          			 value) in the Report Format area. Be aware that the CSV-format report is
                                          			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                          			 (portable document format) in the Report Format area. Be aware that the
                                          			 PDF-format report is limited to 5000 records. |
| Step 8 | Click the View Report button. The report displays . |
| Step 9 | If you want to mail the report, click the Send Report button. To send the report,
                                          			 perform the procedure that is described in the Mail Reports . Note To remove a manager from the Selected Assistant(s) list,
                                                         				  highlight the ID and click Remove . To remove all assistants from the
                                                         				  list, click Remove All . | Note | To remove a manager from the Selected Assistant(s) list,
                                                         				  highlight the ID and click Remove . To remove all assistants from the
                                                         				  list, click Remove All . |
| Note | To remove a manager from the Selected Assistant(s) list,
                                                         				  highlight the ID and click Remove . To remove all assistants from the
                                                         				  list, click Remove All . |
| Step 10 | When you have added all users, click the Close button in the User Search window. |

| Note | To remove a manager from the Selected Assistant(s) list,
                                                         				  highlight the ID and click Remove . To remove all assistants from the
                                                         				  list, click Remove All . |
|---|---|