---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-serv-administration-guide-b-15cucservag-b-15cucservag-chapter--0c64201bb0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag/b_15cucservag_chapter_01.html
retrieved_at: 2026-08-17T03:44:30.869388+00:00
---

Administration Guide for Cisco Unity Connection Serviceability Release 15

# Administration Guide for Cisco Unity Connection Serviceability Release 15

Updated: December 18, 2023

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

User can search for and view alarm definitions in Alarm Message Definitions for Cisco Unity Connection Release 15 available at link https://www.cisco.com/c/td-xml/en_us/voice-ip-comm/connections/15/alarm_messages/15cucalrmmsgdef.html

## Alarm
                        	 Configurations

This section describes how to
                           		enable and disable alarms.

### Enabling Alarm

Step 1

In Cisco Unity Connection Serviceability,
                                          			 select Alarm > Configurations .

Step 2

In the Alarm Configurations window:

To enable the system to log the alarms
                                                   					 in the application logs area in the SysLog Viewer, under Local Syslogs, check
                                                   					 the Enable Alarm check box.

Step 3

Under the syslog for which you have enabled
                                          			 alarms, in the Alarm Event Level field, select the severity level that you
                                          			 want.

Step 4

Select Save .

### Disabling
                           	 Alarms

Step 1

In Cisco Unity Connection Serviceability, select Alarm > Configurations .

Step 2

In the Alarm Configurations window, uncheck the applicable Enable Alarm check box.

Step 3

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