---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--5767e91a2b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0100101.html
retrieved_at: 2026-08-21T01:37:53.885183+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR Reports Notification Limits

## Chapter: CAR Reports Notification Limits

# CAR Reports Notification Limits

Before You Begin

Before you start generating reports with CAR, configure the
                        		system.

## Set Notification Limits

This section describes how to specify the notification limits
                              		  for QoS and daily charges.

Choose Report
                                             				  Config > Notification Limits .

The Set Limits for Notification window displays.

In the Daily QoS Parameters area, enter a threshold for good and
                                       			 poor calls.

The threshold applies in the form of a percentage of all calls
                                          				that must be exceeded to trigger an e-mail alert to the administrator. The
                                          				default for good calls specifies less than 20 percent, meaning that when good
                                          				calls represent less than 20 percent of all calls per day, an alert gets sent.
                                          				The default for poor calls specifies greater than 30 percent, meaning that when
                                          				poor calls represent more than 30 percent of all calls per day, an alert gets
                                          				sent. The alert is called the QoS Notification.

In the Daily Charge Limit area, enter the number of monetary units
                                       			 (such as dollars, francs, or pounds) that, when exceeded by any user in the
                                       			 system, will trigger sending an e-mail alert to the administrator. The alert is
                                       			 called the Charge Limit Notification.

Click the Update button.

Changes take effect immediately. The new values get used whenever
                                          				the next alert is sent.

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability
                                       				  Administration Guide

Cisco Unified Communications
                                       				  Manager Call Detail Records Administration Guide

| Step 1 | Choose Report
                                             				  Config > Notification Limits . The Set Limits for Notification window displays. |
|---|---|
| Step 2 | In the Daily QoS Parameters area, enter a threshold for good and
                                       			 poor calls. The threshold applies in the form of a percentage of all calls
                                          				that must be exceeded to trigger an e-mail alert to the administrator. The
                                          				default for good calls specifies less than 20 percent, meaning that when good
                                          				calls represent less than 20 percent of all calls per day, an alert gets sent.
                                          				The default for poor calls specifies greater than 30 percent, meaning that when
                                          				poor calls represent more than 30 percent of all calls per day, an alert gets
                                          				sent. The alert is called the QoS Notification. |
| Step 3 | In the Daily Charge Limit area, enter the number of monetary units
                                       			 (such as dollars, francs, or pounds) that, when exceeded by any user in the
                                       			 system, will trigger sending an e-mail alert to the administrator. The alert is
                                       			 called the Charge Limit Notification. |
| Step 4 | Click the Update button. Changes take effect immediately. The new values get used whenever
                                          				the next alert is sent. |