---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--ccfdc33dd2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_01110.html
retrieved_at: 2026-08-21T01:34:20.326078+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Precedence Call Summary System Reports

## Chapter: Precedence Call Summary System Reports

# Precedence Call Summary System Reports

CAR provides reporting capabilities for three levels of users:

Administrators - Generate system reports to help with load
                              			 balancing, system performance, and troubleshooting.

Managers - Generate reports for users, departments, and QoS to help
                              			 with call monitoring for budgeting or security purposes and for determining the
                              			 voice quality of the calls.

Individual users - Generate a billing report for calls by each user.

Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter.

## Generate Precedence Call Summary Reports

Only CAR administrators generate the Call Summary by
                              		  Precedence report. The report displays the Call Summary for the precedence
                              		  values that you choose by Hour of Day, Day of Week, or Day of Month.

This section describes how to generate, view, or mail a Call
                              		  Summary by Precedence report.

Choose System Reports > Precedence Call
                                             				  Summary .

The Call Summary by Precedence window displays.

In the Generate Reports field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day.

Ensure that the date and time range does not exceed one
                                                                  							 month.

Day of Week

Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of week.

Ensure that the date and time range does not exceed one
                                                                  							 month.

Day of Month

Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of month.

Ensure that the date and time range does not exceed one
                                                                  							 month.

In the Select Precedence Levels field, check a precedence level
                                       			 that you want in the report or click Select All to check all precedence levels.

Voice Quality

Description

Flash Override

Highest precedence setting for MLPP calls.

Flash

Second highest precedence setting for MLPP calls.

Immediate

Third highest precedence setting for MLPP calls.

Priority

Forth highest precedence setting for MLPP calls.

Routine

Lowest precedence setting for MLPP calls.

The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                      considered as Flash Override in this report.

To uncheck the precedence level check boxes, click Clear All .

In the From Date drop-down list boxes, choose the month, day, and
                                       			 year from which you want precedence summary information.

In the To Date drop-down list boxes, choose the month, day, and
                                       			 year for which you want precedence summary information.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

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

| Note | Depending on your job function, you may not have access to every
                                    		  report that is described in this chapter. |
|---|---|

| Step 1 | Choose System Reports > Precedence Call
                                             				  Summary . The Call Summary by Precedence window displays. |
|---|---|
| Step 2 | In the Generate Reports field, choose a time as described in the
                                       			 following table. Table 1. Generate Report Fields Parameter Description Hour of Day Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day. Note Ensure that the date and time range does not exceed one
                                                                  							 month. Day of Week Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of week. Note Ensure that the date and time range does not exceed one
                                                                  							 month. Day of Month Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of month. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Parameter | Description | Hour of Day | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. | Day of Week | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of week. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. | Day of Month | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of month. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Parameter | Description |
| Hour of Day | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Day of Week | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of week. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Day of Month | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of month. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Step 3 | In the Select Precedence Levels field, check a precedence level
                                       			 that you want in the report or click Select All to check all precedence levels. Table 2. Call Precedence Levels Voice Quality Description Flash Override Highest precedence setting for MLPP calls. Flash Second highest precedence setting for MLPP calls. Immediate Third highest precedence setting for MLPP calls. Priority Forth highest precedence setting for MLPP calls. Routine Lowest precedence setting for MLPP calls. Note The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                      considered as Flash Override in this report. Note To uncheck the precedence level check boxes, click Clear All . | Voice Quality | Description | Flash Override | Highest precedence setting for MLPP calls. | Flash | Second highest precedence setting for MLPP calls. | Immediate | Third highest precedence setting for MLPP calls. | Priority | Forth highest precedence setting for MLPP calls. | Routine | Lowest precedence setting for MLPP calls. | Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                      considered as Flash Override in this report. | Note | To uncheck the precedence level check boxes, click Clear All . |
| Voice Quality | Description |
| Flash Override | Highest precedence setting for MLPP calls. |
| Flash | Second highest precedence setting for MLPP calls. |
| Immediate | Third highest precedence setting for MLPP calls. |
| Priority | Forth highest precedence setting for MLPP calls. |
| Routine | Lowest precedence setting for MLPP calls. |
| Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                      considered as Flash Override in this report. |
| Note | To uncheck the precedence level check boxes, click Clear All . |
| Step 4 | In the From Date drop-down list boxes, choose the month, day, and
                                       			 year from which you want precedence summary information. |
| Step 5 | In the To Date drop-down list boxes, choose the month, day, and
                                       			 year for which you want precedence summary information. |
| Step 6 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 7 | To view the report, click View Report . The report displays . |
| Step 8 | To mail the report to an e-mail recipient, see the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for hour
                                                      						  of day. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Day of Week | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of week. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Day of Month | Displays the average number of calls in the
                                                      						  system for the chosen phone numbers for the date range that was chosen for day
                                                      						  of month. Note Ensure that the date and time range does not exceed one
                                                                  							 month. | Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |

| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
|---|---|

| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
|---|---|

| Note | Ensure that the date and time range does not exceed one
                                                                  							 month. |
|---|---|

| Voice Quality | Description |
|---|---|
| Flash Override | Highest precedence setting for MLPP calls. |
| Flash | Second highest precedence setting for MLPP calls. |
| Immediate | Third highest precedence setting for MLPP calls. |
| Priority | Forth highest precedence setting for MLPP calls. |
| Routine | Lowest precedence setting for MLPP calls. |

| Note | The Executive Override precedence level that is mentioned in the MLPP Precedence level on the Administration page will be
                                                      considered as Flash Override in this report. |
|---|---|

| Note | To uncheck the precedence level check boxes, click Clear All . |
|---|---|