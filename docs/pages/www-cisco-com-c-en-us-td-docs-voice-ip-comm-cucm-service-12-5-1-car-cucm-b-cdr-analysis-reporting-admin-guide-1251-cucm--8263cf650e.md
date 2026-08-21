---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--8263cf650e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_01101.html
retrieved_at: 2026-08-21T01:34:16.586811+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Malicious Call Details System Reports

## Chapter: Malicious Call Details System Reports

# Malicious Call Details System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

## Generate Malicious Call Details Reports

Only CAR administrators generate the Malicious Call Details
                              		  report. The report displays the following details about malicious calls for a
                              		  particular date range: origination time, termination time, duration (in
                              		  seconds), origination (calling number), destination (called number),
                              		  origination device, destination device, and call classification.

This section describes how to generate, view, or mail a
                              		  Malicious Call Detail report.

Choose System Reports > Malicious Call
                                             				  Details .

The Malicious Call Details window displays.

In the From Date drop-down list boxes, choose the month, day, and
                                       			 year from which you want malicious call details.

In the To Date drop-down list boxes, choose the month, day, and
                                       			 year to which you want malicious call details.

If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records.

To view the report, click View Report .

The report displays .

To mail the report to an e-mail recipient, see the Mail Reports .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

Feature Configuration Guide
                                    				for Cisco Unified Communications Manager

| Note | Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter. |
|---|---|

| Step 1 | Choose System Reports > Malicious Call
                                             				  Details . The Malicious Call Details window displays. |
|---|---|
| Step 2 | In the From Date drop-down list boxes, choose the month, day, and
                                       			 year from which you want malicious call details. |
| Step 3 | In the To Date drop-down list boxes, choose the month, day, and
                                       			 year to which you want malicious call details. |
| Step 4 | If you want the report in CSV format, choose CSV (comma separated
                                       			 value) in the Report Format area. Be aware that the CSV-format report is
                                       			 limited to 20,000 records. If you want the report in PDF format, choose PDF
                                       			 (portable document format) in the Report Format area. Be aware that the
                                       			 PDF-format report is limited to 5000 records. |
| Step 5 | To view the report, click View Report . The report displays . |
| Step 6 | To mail the report to an e-mail recipient, see the Mail Reports . |