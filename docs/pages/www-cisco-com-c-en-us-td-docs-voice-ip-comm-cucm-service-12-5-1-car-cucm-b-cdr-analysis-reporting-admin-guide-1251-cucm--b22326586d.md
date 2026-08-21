---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--b22326586d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0100100.html
retrieved_at: 2026-08-21T01:37:49.988716+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: Automatic Generation of CAR Reports and Alerts

## Chapter: Automatic Generation of CAR Reports and Alerts

# Automatic Generation of CAR Reports and Alerts

Before You Begin

Before you start generating reports with CAR, configure the
                        		system.

The following table displays the list of reports that the
                        		system enables or disables for automatic generation, the report generation
                        		interval, and the recipients of the report.

Name of Report

Report Generation Interval

Recipients

Department Bill Summary

Monthly

- CAR managers

- CAR administrators

Gateway Summary

Monthly

- CAR administrators

Individual Bill

Monthly

- Individual users
                                       				  configured in Cisco Unified CM.

Administration users do not get access to this report.

Individual Bill Summary

Monthly

- Individual users
                                       				  configured in Cisco Unified CM

- CAR managers

- CAR administrators

Conference Summary

Monthly

- CAR administrators

Conference Detail

Daily

- CAR administrators

QoS Summary

Monthly

- CAR managers

- CAR administrators

System Overview

Monthly

- CAR administrators

Top N Charge

Daily

- CAR managers

- CAR administrators

Top N Charge

Monthly

- CAR managers

- CAR administrators

Top N Duration

Daily

- CAR managers

- CAR administrators

Top N Duration

Monthly

- CAR managers

- CAR administrators

Top N Calls

Daily

- CAR managers

- CAR administrators

Top N Calls

Monthly

- CAR managers

- CAR administrators

Traffic Summary - Day of Month

Monthly

- CAR administrators

Traffic Summary - Day of Week

Weekly

- CAR administrators

Traffic Summary - Hour of Day

Daily

- CAR administrators

Conference Bridge Util - Day of Week

Weekly

- CAR administrators

Voice Messaging Util - Day of Week

Weekly

- CAR administrators

Route Pattern/Hunt Pilot Util - Day of Week

Weekly

- CAR administrators

Route/Hunt List Util - Day of Week

Weekly

- CAR administrators

Route Group Util - Day of Week

Weekly

- CAR administrators

Line Group Util - Day of Week

Weekly

- CAR administrators

Gateway Util - Day of Week

Weekly

- CAR administrators

In large setups, with a large number of gateways, route groups, route
                                    		lists, and route patterns, enabling all the Utilization reports (Gateway
                                    		Utilization, Line Group Utilization, Route Group Utilization, Route List
                                    		Utilization, and Route Pattern Utilization) increases the CPU usage of the
                                    		system, therefore increasing the time in which reports are generated. This also
                                    		affects system performance. Cisco recommends that you enable only Gateway
                                    		Utilization reports for automatic generation, due to the number of gateways
                                    		that are typically found in a large system. You can generate all Utilization
                                    		reports on demand by selecting five or less gateways, route groups, route
                                    		lists, or route groups.

Automatically generating reports involves a two-step process:

- First, enable the reports that
                           		you want to generate unless they are enabled by default.

- Second, schedule the reports
                           		for the day and time that you want them to generate. (CAR provides a default
                           		schedule. If the default schedule is acceptable, only enable the reports that
                           		you want to generate automatically.)

CAR provides e-mail alerts for various events. Enabling the
                        	 system for e-mail alerts involves a two-step process:

- First, enable the e-mail
                           		alerts. Default enables some, but not all, reports.

- Second, configure the e-mail
                           		that is sent when the alert criteria are met.

## Enable Automatic Generation Reports

This section describes how to enable or disable one or all
                              		  reports for automatic generation. You can also customize the report parameters
                              		  and enable a mailing option, so reports get e-mailed when they are created.
                              		  When the report gets mailed, CAR generates the e-mail address by using the mail
                              		  ID for the CAR administrator(s) and the mail domain that is configured in the
                              		  Mail Parameters window; that is, CAR uses <mail ID for the CAR
                              		  administrator> @ <domain that is configured in the mail parameters
                              		  window>.

For all new installations of Unified Communications Manager , you must first enable the e-mail alerts and reports for automatic generation. The default status for all reports and alerts
                              specifies Disabled .

For all Unified Communications Manager upgrades from Release 5.x to a later release of Unified Communications Manager , the tbl_pregenmail_option table data migrates only if the CAR Scheduler service is active.

When you upgrade to another version of Unified Communications Manager , disable all reports and alerts while the upgrade is in process to conserve system resources. Remember to enable the reports
                              and alerts after the upgrade completes.

The Generated Report Schedule describes reports that are enabled by default.

Choose Report Config > Automatic
                                             				  Generation/Alert .

The Automatic Report Generation/Alert Option window displays.

In the Reports [Report Generation Interval] box, choose the report
                                       			 that you want to automatically generate based on the schedule that you defined
                                       			 in the System Scheduler. See the CAR System Scheduler .

In the Status field, choose Enabled or Disabled .

To customize the report or have the report e-mailed when it is
                                       			 generated, click the Customize Parameters button.

The Customize Parameters window displays.

Each report provides different customization options, depending
                                                      				  on the type of report.

Choose the CSV or PDF radio button, depending on the type of
                                       			 report that you want the system to mail.

To have the report mailed to all CAR administrators, check the Mailing Option check box.

To save the values that you specified, click the Update button.

The Customize Parameters window closes.

To enable or customize other reports, repeat the previous steps.

Click the Update button.

Changes take effect at midnight. You can force the change to take
                                          				effect immediately by stopping and restarting the CAR Scheduler service.

## Enable Email Alerts

There are two Alerts by Mail that are available. These
                              		  alerts are:

- Charge Limit Notification

- QoS Notification

See the Set Notification Limits for information on how to configure these alerts.

This section describes how to enable these alerts to be
                              		  mailed to users.

Choose Report Config > Automatic
                                             				  Generation/Alert .

The Automatic Report Generation/Alert window displays.

In the Alerts by Mail box, choose the alert that you want to enable or
                                       			 disable.

In the Status field, choose Enabled or Disabled .

Click the Update button.

To enable or disable alerts by mail, repeat the previous steps.

Changes take effect at midnight. You can force the change to take
                                          				effect immediately by stopping and restarting the CAR Scheduler service.

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Name of Report | Report Generation Interval | Recipients |
|---|---|---|
| Department Bill Summary | Monthly | CAR managers CAR administrators |
| Gateway Summary | Monthly | CAR administrators |
| Individual Bill | Monthly | Individual users
                                       				  configured in Cisco Unified CM. CAR administrators Note Administration users do not get access to this report. | Note | Administration users do not get access to this report. |
| Note | Administration users do not get access to this report. |
| Individual Bill Summary | Monthly | Individual users
                                       				  configured in Cisco Unified CM CAR managers CAR administrators |
| Conference Summary | Monthly | CAR administrators |
| Conference Detail | Daily | CAR administrators |
| QoS Summary | Monthly | CAR managers CAR administrators |
| System Overview | Monthly | CAR administrators |
| Top N Charge | Daily | CAR managers CAR administrators |
| Top N Charge | Monthly | CAR managers CAR administrators |
| Top N Duration | Daily | CAR managers CAR administrators |
| Top N Duration | Monthly | CAR managers CAR administrators |
| Top N Calls | Daily | CAR managers CAR administrators |
| Top N Calls | Monthly | CAR managers CAR administrators |
| Traffic Summary - Day of Month | Monthly | CAR administrators |
| Traffic Summary - Day of Week | Weekly | CAR administrators |
| Traffic Summary - Hour of Day | Daily | CAR administrators |
| Conference Bridge Util - Day of Week | Weekly | CAR administrators |
| Voice Messaging Util - Day of Week | Weekly | CAR administrators |
| Route Pattern/Hunt Pilot Util - Day of Week | Weekly | CAR administrators |
| Route/Hunt List Util - Day of Week | Weekly | CAR administrators |
| Route Group Util - Day of Week | Weekly | CAR administrators |
| Line Group Util - Day of Week | Weekly | CAR administrators |
| Gateway Util - Day of Week | Weekly | CAR administrators |

| Note | Administration users do not get access to this report. |
|---|---|

| Note | In large setups, with a large number of gateways, route groups, route
                                    		lists, and route patterns, enabling all the Utilization reports (Gateway
                                    		Utilization, Line Group Utilization, Route Group Utilization, Route List
                                    		Utilization, and Route Pattern Utilization) increases the CPU usage of the
                                    		system, therefore increasing the time in which reports are generated. This also
                                    		affects system performance. Cisco recommends that you enable only Gateway
                                    		Utilization reports for automatic generation, due to the number of gateways
                                    		that are typically found in a large system. You can generate all Utilization
                                    		reports on demand by selecting five or less gateways, route groups, route
                                    		lists, or route groups. |
|---|---|

| Step 1 | Choose Report Config > Automatic
                                             				  Generation/Alert . The Automatic Report Generation/Alert Option window displays. |
|---|---|
| Step 2 | In the Reports [Report Generation Interval] box, choose the report
                                       			 that you want to automatically generate based on the schedule that you defined
                                       			 in the System Scheduler. See the CAR System Scheduler . |
| Step 3 | In the Status field, choose Enabled or Disabled . |
| Step 4 | To customize the report or have the report e-mailed when it is
                                       			 generated, click the Customize Parameters button. The Customize Parameters window displays. Note Each report provides different customization options, depending
                                                      				  on the type of report. | Note | Each report provides different customization options, depending
                                                      				  on the type of report. |
| Note | Each report provides different customization options, depending
                                                      				  on the type of report. |
| Step 5 | Choose the CSV or PDF radio button, depending on the type of
                                       			 report that you want the system to mail. |
| Step 6 | To have the report mailed to all CAR administrators, check the Mailing Option check box. |
| Step 7 | To save the values that you specified, click the Update button. The Customize Parameters window closes. |
| Step 8 | To enable or customize other reports, repeat the previous steps. |
| Step 9 | Click the Update button. Changes take effect at midnight. You can force the change to take
                                          				effect immediately by stopping and restarting the CAR Scheduler service. |

| Note | Each report provides different customization options, depending
                                                      				  on the type of report. |
|---|---|

| Step 1 | Choose Report Config > Automatic
                                             				  Generation/Alert . The Automatic Report Generation/Alert window displays. |
|---|---|
| Step 2 | In the Alerts by Mail box, choose the alert that you want to enable or
                                       			 disable. |
| Step 3 | In the Status field, choose Enabled or Disabled . |
| Step 4 | Click the Update button. |
| Step 5 | To enable or disable alerts by mail, repeat the previous steps. Changes take effect at midnight. You can force the change to take
                                          				effect immediately by stopping and restarting the CAR Scheduler service. |