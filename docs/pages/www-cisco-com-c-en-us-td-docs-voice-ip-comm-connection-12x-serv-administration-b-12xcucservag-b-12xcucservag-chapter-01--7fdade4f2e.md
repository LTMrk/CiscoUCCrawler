---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-serv-administration-b-12xcucservag-b-12xcucservag-chapter-01--7fdade4f2e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/serv_administration/b_12xcucservag/b_12xcucservag_chapter_01.html
retrieved_at: 2026-08-21T07:55:31.232379+00:00
---

Administration Guide for Cisco Unity Connection Serviceability Release 12.x

# Administration Guide for Cisco Unity Connection Serviceability Release 12.x

Updated: August 4, 2017

Chapter: Using Alarms

## Chapter: Using Alarms

# Using Alarms

## Understanding Alarms

Cisco Unity Connection Serviceability alarms provide information on runtime status and the state of the system, so you can
                           troubleshoot problems that are associated with the system. For example, you can use alarms to determine whether there are
                           any ports enabled to set MWIs. Alarm information includes the catalog, name, severity, explanation, recommended action, routing
                           list, and parameters.

You can enable or disable alarms to appear as syslog messages on the local server or on a remote server that you specify.
                           You can also set the severity level that you want to appear.

You use the trace and log central option in the Real-Time Monitoring Tool (RTMT) to collect alarms. You use the SysLog Viewer
                           in RTMT to view alarms.

## Alarm Definitions

Alarm definitions describe alarm messages—what they mean and how to recover from them.

You search the Alarm Message Definitions page for alarm information. When you select an alarm, a description of the alarm
                           information and a recommended action appears on the Alarm Information page. To help with troubleshooting, the definitions
                           include the alarm name, description, severity, explanation, recommended action, routing list, and parameters.

## Viewing Alarm
                        	 Definitions

You can search for and view alarm definitions in Alarm Message Definitions for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/alarm_messages/12cucalrmmsgdef.html .

## Alarm
                        	 Configurations

This section describes how to
                           		enable and disable alarms.

### Enabling Alarm

In Cisco Unity Connection Serviceability,
                                          			 select Alarm > Configurations .

In the Alarm Configurations window:

To enable the system to log the alarms
                                                   					 in the application logs area in the SysLog Viewer, under Local Syslogs, check
                                                   					 the Enable Alarm check box.

Under the syslog for which you have enabled
                                          			 alarms, in the Alarm Event Level field, select the severity level that you
                                          			 want.

Select Save .

### Disabling
                           	 Alarms

In Cisco Unity Connection Serviceability, select Alarm > Configurations .

In the Alarm Configurations window, uncheck the applicable Enable Alarm check box.

Select Save .

| Step 1 | In Cisco Unity Connection Serviceability,
                                          			 select Alarm > Configurations . |
|---|---|
| Step 2 | In the Alarm Configurations window: To enable the system to log the alarms
                                                   					 in the application logs area in the SysLog Viewer, under Local Syslogs, check
                                                   					 the Enable Alarm check box. |
| Step 3 | Under the syslog for which you have enabled
                                          			 alarms, in the Alarm Event Level field, select the severity level that you
                                          			 want. |
| Step 4 | Select Save . |

| Step 1 | In Cisco Unity Connection Serviceability, select Alarm > Configurations . |
|---|---|
| Step 2 | In the Alarm Configurations window, uncheck the applicable Enable Alarm check box. |
| Step 3 | Select Save . |