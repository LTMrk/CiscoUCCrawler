---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--5e4ec9a9b4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_010110.html
retrieved_at: 2026-08-21T01:36:54.583548+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Voice Messaging Utilization Device Reports

## Chapter: Voice Messaging Utilization Device Reports

# Voice Messaging Utilization Device Reports

CAR provides reporting capabilities for three levels of users:
                        		administrators, managers, and individual users. Only administrators generate
                        		device reports.

Device reports track the load and performance of Unified Communications Manager related devices, such as conference bridges, voice-messaging servers, and gateways.

## Generate Voice Messaging Utilization Reports

Only CAR administrators generate the Voice Messaging
                              		  Utilization report. The report provides an estimate of the maximum utilization
                              		  percentage of the voice-messaging devices for the period and not the exact
                              		  utilization. For example, the system calculates the utilization of a
                              		  voice-messaging port/voice-messaging DNs between 11hrs and 12hrs by using the
                              		  duration of the calls that used the voice-messaging port/voice messaging DNs.
                              		  The system calculates utilization for the voice-messaging port as the (sum of
                              		  duration of calls that used the voice-messaging port in that hour*100) /
                              		  (maximum duration seconds in an hour * number of days between the fromDate and
                              		  toDate selected). The utilization calculation for voice-messaging DNs
                              		  represents the (sum of duration of calls that used the voice-messaging DNs in
                              		  that hour * 100) / (maximum duration seconds in an hour * number of days
                              		  between the fromDate and toDate selected * maximum number of ports in a gateway
                              		  that is connected to the voice-messaging DN). The same value will display in
                              		  the report as the utilization for the time between 11hrs and 12hrs.

You can review the Voice Messaging Utilization report for
                              		  Voice Messaging Ports only as a newly generated report and not as a report that
                              		  the system automatically generates.

You can automatically generate the Voice Messaging
                              		  Utilization report for Voice Messaging DNs, or you can generate it as a new
                              		  report. Only CAR administrators can schedule reports for automatic generation.
                              		  See CAR System Scheduler for more information.

The CAR Voice Messaging Utilization report supports the Cisco Unity and Cisco Unity Connection voice-messaging systems.

This section describes how to generate, mail, or view Voice
                              		  Messaging Utilization reports.

Choose Device Reports > Voice
                                                					 Messaging > Utilization .

The Voice Messaging Utilization window displays.

In the Generate Report field, choose a time as described in the
                                       			 following table.

Parameter

Description

Hour of Day

Displays the utilization results for each hour in
                                                      						  a 24-hour period for the period that you specify in Step 10 .

Day of Week

Displays the utilization for the days of the week
                                                      						  that occur within the period that you specify in Step 10 .

Day of Month

Displays the utilization for the days of the
                                                      						  month that occur within the period that you specify in Step 10 .

In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 12 or use the default setting, Generate New Report, and go to Step 4 .

To choose a voice-messaging DN, click Voice Messaging DNs in the Voice Utilization
                                       			 pane.

The previously configured voice-messaging DN displays.

The Voice Messaging DN that displays in this window represents
                                                      				  the Voice Messaging DN that you configure in the VoiceMailDn service parameter,
                                                      				  which supports the Cisco Messaging Interface service. Set the parameter name
                                                      				  VoiceMailDn to the routing pattern that you have created on the machine.
                                                      				  Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the
                                                      				  service Cisco Messaging Interface .

Choose the voice-messaging DN.

The DN that you chose displays in the List of DNs/Ports list box.

To choose a voice-messaging port, click Voice Messaging Ports in the Voice Utilization
                                       			 pane.

A list of configured voice-messaging ports displays.

From the list of ports, choose a voice-messaging port.

The port that you chose displays in the List of DNs/Ports list
                                          				box.

In Select Voice Messaging DNs/Ports, click the down arrow.

The port that you chose displays in the Selected DNs/Ports list
                                          				box.

Repeat Step 7 and Step 8 until you have chosen the ports that you want to include in the report.

For this report, you can choose a maximum of five Voice
                                                      				  Messaging Ports/Voice Messaging DNs. You can choose the default Voice Messaging
                                                      				  DN and four Voice Messaging Ports, or you can choose five Voice Messaging
                                                      				  Ports.

If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information.

Ensure the date and time range does not exceed one month.

If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area.

Click the View Report button.

The report displays .

If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure described in the Mail Reports .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Note | The CAR Voice Messaging Utilization report supports the Cisco Unity and Cisco Unity Connection voice-messaging systems. |
|---|---|

| Step 1 | Choose Device Reports > Voice
                                                					 Messaging > Utilization . The Voice Messaging Utilization window displays. |
|---|---|
| Step 2 | In the Generate Report field, choose a time as described in the
                                       			 following table. Table 1. Generate Report Fields Parameter Description Hour of Day Displays the utilization results for each hour in
                                                      						  a 24-hour period for the period that you specify in Step 10 . Day of Week Displays the utilization for the days of the week
                                                      						  that occur within the period that you specify in Step 10 . Day of Month Displays the utilization for the days of the
                                                      						  month that occur within the period that you specify in Step 10 . | Parameter | Description | Hour of Day | Displays the utilization results for each hour in
                                                      						  a 24-hour period for the period that you specify in Step 10 . | Day of Week | Displays the utilization for the days of the week
                                                      						  that occur within the period that you specify in Step 10 . | Day of Month | Displays the utilization for the days of the
                                                      						  month that occur within the period that you specify in Step 10 . |
| Parameter | Description |
| Hour of Day | Displays the utilization results for each hour in
                                                      						  a 24-hour period for the period that you specify in Step 10 . |
| Day of Week | Displays the utilization for the days of the week
                                                      						  that occur within the period that you specify in Step 10 . |
| Day of Month | Displays the utilization for the days of the
                                                      						  month that occur within the period that you specify in Step 10 . |
| Step 3 | In the Available Reports field, choose an automatically generated report
                                       			 (if available) and go to Step 12 or use the default setting, Generate New Report, and go to Step 4 . |
| Step 4 | To choose a voice-messaging DN, click Voice Messaging DNs in the Voice Utilization
                                       			 pane. The previously configured voice-messaging DN displays. Note The Voice Messaging DN that displays in this window represents
                                                      				  the Voice Messaging DN that you configure in the VoiceMailDn service parameter,
                                                      				  which supports the Cisco Messaging Interface service. Set the parameter name
                                                      				  VoiceMailDn to the routing pattern that you have created on the machine.
                                                      				  Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the
                                                      				  service Cisco Messaging Interface . | Note | The Voice Messaging DN that displays in this window represents
                                                      				  the Voice Messaging DN that you configure in the VoiceMailDn service parameter,
                                                      				  which supports the Cisco Messaging Interface service. Set the parameter name
                                                      				  VoiceMailDn to the routing pattern that you have created on the machine.
                                                      				  Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the
                                                      				  service Cisco Messaging Interface . |
| Note | The Voice Messaging DN that displays in this window represents
                                                      				  the Voice Messaging DN that you configure in the VoiceMailDn service parameter,
                                                      				  which supports the Cisco Messaging Interface service. Set the parameter name
                                                      				  VoiceMailDn to the routing pattern that you have created on the machine.
                                                      				  Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the
                                                      				  service Cisco Messaging Interface . |
| Step 5 | Choose the voice-messaging DN. The DN that you chose displays in the List of DNs/Ports list box. |
| Step 6 | To choose a voice-messaging port, click Voice Messaging Ports in the Voice Utilization
                                       			 pane. A list of configured voice-messaging ports displays. |
| Step 7 | From the list of ports, choose a voice-messaging port. The port that you chose displays in the List of DNs/Ports list
                                          				box. |
| Step 8 | In Select Voice Messaging DNs/Ports, click the down arrow. The port that you chose displays in the Selected DNs/Ports list
                                          				box. |
| Step 9 | Repeat Step 7 and Step 8 until you have chosen the ports that you want to include in the report. Note For this report, you can choose a maximum of five Voice
                                                      				  Messaging Ports/Voice Messaging DNs. You can choose the default Voice Messaging
                                                      				  DN and four Voice Messaging Ports, or you can choose five Voice Messaging
                                                      				  Ports. | Note | For this report, you can choose a maximum of five Voice
                                                      				  Messaging Ports/Voice Messaging DNs. You can choose the default Voice Messaging
                                                      				  DN and four Voice Messaging Ports, or you can choose five Voice Messaging
                                                      				  Ports. |
| Note | For this report, you can choose a maximum of five Voice
                                                      				  Messaging Ports/Voice Messaging DNs. You can choose the default Voice Messaging
                                                      				  DN and four Voice Messaging Ports, or you can choose five Voice Messaging
                                                      				  Ports. |
| Step 10 | If you chose Generate New Report, enter the date range of the
                                       			 period for which you want to see call information. Note Ensure the date and time range does not exceed one month. | Note | Ensure the date and time range does not exceed one month. |
| Note | Ensure the date and time range does not exceed one month. |
| Step 11 | If you want the report in CSV format, choose CSV (comma separated value) in the Report
                                       			 Format area. If you want the report in PDF format, choose PDF (portable document format) in the Report
                                       			 Format area. |
| Step 12 | Click the View Report button. The report displays . |
| Step 13 | If you want to mail the report, click the Send Report button. To send the report,
                                       			 perform the procedure described in the Mail Reports . |

| Parameter | Description |
|---|---|
| Hour of Day | Displays the utilization results for each hour in
                                                      						  a 24-hour period for the period that you specify in Step 10 . |
| Day of Week | Displays the utilization for the days of the week
                                                      						  that occur within the period that you specify in Step 10 . |
| Day of Month | Displays the utilization for the days of the
                                                      						  month that occur within the period that you specify in Step 10 . |

| Note | The Voice Messaging DN that displays in this window represents
                                                      				  the Voice Messaging DN that you configure in the VoiceMailDn service parameter,
                                                      				  which supports the Cisco Messaging Interface service. Set the parameter name
                                                      				  VoiceMailDn to the routing pattern that you have created on the machine.
                                                      				  Configure this by opening Cisco Unified CM Administration and clicking System. Click Service Parameters ; then, select the
                                                      				  service Cisco Messaging Interface . |
|---|---|

| Note | For this report, you can choose a maximum of five Voice
                                                      				  Messaging Ports/Voice Messaging DNs. You can choose the default Voice Messaging
                                                      				  DN and four Voice Messaging Ports, or you can choose five Voice Messaging
                                                      				  Ports. |
|---|---|

| Note | Ensure the date and time range does not exceed one month. |
|---|---|