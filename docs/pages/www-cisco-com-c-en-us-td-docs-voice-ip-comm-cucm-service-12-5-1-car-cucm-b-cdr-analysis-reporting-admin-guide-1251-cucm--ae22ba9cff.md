---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--ae22ba9cff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_01100.html
retrieved_at: 2026-08-21T01:34:12.332022+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: FAC/CMC System Reports

## Chapter: FAC/CMC System Reports

# FAC/CMC System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

Only CAR administrators can generate Forced Authorization Code
                        		(FAC)/Client Matter Code (CMC) reports.

The following sections describe how to configure FAC/CMC
                        		reports:

## Generate Client Matter Code Reports

Only CAR administrators can generate the Client Matter Code
                              		  report. You can generate a report that shows the origination (calling number),
                              		  destination (called number), origination date time (the date and time that the
                              		  call originated), duration (call duration in seconds), and the call
                              		  classification that relates to each CMC.

The following procedure describes how to generate a report
                              		  that shows the usage of specific client matter codes.

Choose System
                                             				  Reports > FAC/CMC > Client Matter
                                             				  Code .

The Call Details for Client Matter Code window displays a list of
                                          				all client matter codes that are configured in the system.

In the List of Client Matter Codes box, choose the codes that you
                                       			 want included in the report.

You can choose up to 100 Client Matter Codes.

To add the chosen code(s) to the Selected Client Matter Codes box,
                                       			 click the down arrow.

The report will include all codes, for which data is available,
                                          				that are listed in this box.

In the From Date and To Date pull-down list boxes, enter the date
                                       			 range of the period for which you want to see Client Matter Code information.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click View Report .

The report displays.

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in Mail Reports .

## Generate Authorization Code Name Reports

Only CAR administrators can generate the Authorization Code
                              		  Name report. You can generate a report that shows the origination (calling
                              		  number), destination (called number), origination date time (the date and time
                              		  that the call originated), duration (call duration in seconds), and the call
                              		  classification that relates to each chosen authorization code name.

For security purposes, the authorization code does not display;
                                          			 instead, the authorization code name (description) displays.

The following procedure describes how to generate a report
                              		  that shows the usage of specific authorization code names.

Choose System
                                             				  Reports > FAC/CMC > Authorization Code
                                             				  Name .

The Call Details for Authorization Code Name window displays a
                                          				list of all authorization code names that are configured in the system.

In the List of Authorization Code Names box, choose the code names
                                       			 that you want included in the report.

You can choose up to 30 code names.

To add the chosen code name(s) to the Selected Authorization Code
                                       			 Names box, click the down arrow.

The report will include all code names, for which data is
                                          				available, that are listed in this box.

In the From Date and To Date drop-down list boxes, enter the date
                                       			 range of the period for which you want to see authorization code name
                                       			 information.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click View Report .

The report displays.

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in Mail Reports .

## Generate Authorization Level Reports

Only CAR administrators can generate the Authorization Level
                              		  report. You can generate a report that shows the origination (calling number),
                              		  destination (called number), origination date time (the date and time that the
                              		  call originated), duration (call duration in seconds), and the call
                              		  classification that relate to each chosen authorization level.

The following procedure describes how to generate a report
                              		  that shows the usage of specific authorization levels.

Choose System
                                             				  Reports > FAC/CMC > Authorization
                                             				  Level .

The Call Details by Authorization Level window displays a list of
                                          				all authorization levels that are configured in the system.

In the List of Authorization Levels box, choose the levels that
                                       			 you want included in the report.

To add the chosen level(s) to the Selected Authorization Levels
                                       			 box, click the down arrow.

The report will include all levels, for which data is available,
                                          				that are listed in this box.

Only FAC authorization levels reports that are associated with
                                                      				  Route Patterns will get generated.

In the From Date and To Date drop-down list boxes, enter the date
                                       			 range of the period for which you want to see authorization level information.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

Click View Report .

The report displays.

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

| Step 1 | Choose System
                                             				  Reports > FAC/CMC > Client Matter
                                             				  Code . The Call Details for Client Matter Code window displays a list of
                                          				all client matter codes that are configured in the system. |
|---|---|
| Step 2 | In the List of Client Matter Codes box, choose the codes that you
                                       			 want included in the report. Note You can choose up to 100 Client Matter Codes. | Note | You can choose up to 100 Client Matter Codes. |
| Note | You can choose up to 100 Client Matter Codes. |
| Step 3 | To add the chosen code(s) to the Selected Client Matter Codes box,
                                       			 click the down arrow. The report will include all codes, for which data is available,
                                          				that are listed in this box. |
| Step 4 | In the From Date and To Date pull-down list boxes, enter the date
                                       			 range of the period for which you want to see Client Matter Code information. |
| Step 5 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 6 | Click View Report . The report displays. |
| Step 7 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in Mail Reports . |

| Note | You can choose up to 100 Client Matter Codes. |
|---|---|

| Note | For security purposes, the authorization code does not display;
                                          			 instead, the authorization code name (description) displays. |
|---|---|

| Step 1 | Choose System
                                             				  Reports > FAC/CMC > Authorization Code
                                             				  Name . The Call Details for Authorization Code Name window displays a
                                          				list of all authorization code names that are configured in the system. |
|---|---|
| Step 2 | In the List of Authorization Code Names box, choose the code names
                                       			 that you want included in the report. Note You can choose up to 30 code names. | Note | You can choose up to 30 code names. |
| Note | You can choose up to 30 code names. |
| Step 3 | To add the chosen code name(s) to the Selected Authorization Code
                                       			 Names box, click the down arrow. The report will include all code names, for which data is
                                          				available, that are listed in this box. |
| Step 4 | In the From Date and To Date drop-down list boxes, enter the date
                                       			 range of the period for which you want to see authorization code name
                                       			 information. |
| Step 5 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 6 | Click View Report . The report displays. |
| Step 7 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in Mail Reports . |

| Note | You can choose up to 30 code names. |
|---|---|

| Step 1 | Choose System
                                             				  Reports > FAC/CMC > Authorization
                                             				  Level . The Call Details by Authorization Level window displays a list of
                                          				all authorization levels that are configured in the system. |
|---|---|
| Step 2 | In the List of Authorization Levels box, choose the levels that
                                       			 you want included in the report. |
| Step 3 | To add the chosen level(s) to the Selected Authorization Levels
                                       			 box, click the down arrow. The report will include all levels, for which data is available,
                                          				that are listed in this box. Note Only FAC authorization levels reports that are associated with
                                                      				  Route Patterns will get generated. | Note | Only FAC authorization levels reports that are associated with
                                                      				  Route Patterns will get generated. |
| Note | Only FAC authorization levels reports that are associated with
                                                      				  Route Patterns will get generated. |
| Step 4 | In the From Date and To Date drop-down list boxes, enter the date
                                       			 range of the period for which you want to see authorization level information. |
| Step 5 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 6 | Click View Report . The report displays. |
| Step 7 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure that is described in the Mail Reports . |

| Note | Only FAC authorization levels reports that are associated with
                                                      				  Route Patterns will get generated. |
|---|---|