---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--7e8ae1373a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0100001.html
retrieved_at: 2026-08-21T01:37:37.170574+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR Reports Configurations

## Chapter: CAR Reports Configurations

# CAR Reports Configurations

Use the CAR report configuration to define the following
                        		parameters:

Rating parameters for calls - duration, time of day, voice quality

Quality of service

Automatic generation of reports with alerts

Notification limits

## CAR Reports Configuration

Before you start generating reports with CAR, configure the
                              		  system.

### Rating Engine

You can use CAR to set a base monetary rate for the cost of
                              		  calls based on a time increment. You can further qualify the cost by applying
                              		  the time-of-day and voice-quality factors. Service providers who must account
                              		  for service to subscribers commonly use this feature. Some organizations also
                              		  use this information to establish billing costs for users and departments in
                              		  the organization for accounting or budgeting purposes.

Reports that use these rating parameters include Individual
                              		  Bill, Department Bill, Top N by Charge, Top N by Duration, and Top N by Number
                              		  of Calls.

If you do not change the default value for charge base/block, the
                                          			 cost will always equal zero because the default base charge per block equals
                                          			 zero.

The charge of any call comprises the multiplication of the
                              		  basic charge of the call, multiplication factor for time of day, and
                              		  multiplication factor for voice quality. You can set the basic charge for a
                              		  call through the Report Config > Rating
                                    				Engine > Duration window . See the
                              		  following list:

Basic charge = cost, or number of units, applied to the duration
                                    				block that is specified in the Number of Blocks section.

Number of blocks = total duration of call, in seconds, for which
                                    				you want the base charge to be applied.

You can set the multiplication factor for time of day through
                              		  the Report Config > Rating
                                    				Engine > Time of Day window. The
                              		  basis of the settings provides the connect time of the call.

You can set the multiplication factor for voice quality
                              		  through the Report Config > Rating
                                    				Engine > Voice Quality window.

### QoS Values

CAR generates QoS reports. To qualify the data that is
                              		  presented in those reports, CAR uses predefined values that are set about voice
                              		  quality. You can specify the value ranges that are good, acceptable, fair, and
                              		  poor for jitter, latency, and lost packets.

### Automatic Generation of Reports and Alerts

CAR automatically generates reports based on a schedule.
                              		  Report generation can include a daily, weekly, or monthly summary report, QoS
                              		  reports, traffic reports, Device/Route Plan utilization reports, and so on,
                              		  that you may want to view on a regular basis.

### Notification Limits

You can specify limits for QoS and daily charges, so the
                              		  administrator gets alerted by e-mail when these limits are exceeded. The alerts
                              		  go to all users that are designated as CAR Administrators through Cisco Unified CM Administration .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Note | If you do not change the default value for charge base/block, the
                                          			 cost will always equal zero because the default base charge per block equals
                                          			 zero. |
|---|---|