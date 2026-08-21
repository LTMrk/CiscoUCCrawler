---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--dc3c50f5fb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0100011.html
retrieved_at: 2026-08-21T01:37:45.468269+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR Reports QoS Values

## Chapter: CAR Reports QoS Values

# CAR Reports QoS Values

## Define QoS Values

QoS values get configured for lost packets, jitter, and
                              		  latency based on good, acceptable, fair, or poor criteria.

If a call does not satisfy any of the criteria that are set
                              		  for any of the four voice-quality categories, it receives a classification of
                              		  NA (not applicable); likewise, if the system is not configured to generate CMR
                              		  data (or if the CMR is bad), the CMR receives a classification of NA (not
                              		  applicable).

Enter NA to ignore the values of a parameter. For example, a
                              		  QoS parameter such as jitter, has NA, and the QoS is defined as good, which
                              		  means that the QoS depends only on the values of latency and lost packets. All
                              		  three parameters cannot have NA as values. Infinity designates the maximum
                              		  value that is available for any parameter. If you specify a rule where a jitter
                              		  value from 500 to Infinity is considered poor, a call with jitter greater than
                              		  500 receives a classification of poor.

Be aware that the classifications of "NA" and "Infinity" are case-sensitive.

This section describes how to define the QoS values.

Choose Report Config > Define
                                             				  QoS .

The Define Quality of Service window displays. The following table
                                          				describes the QoS default values.

QoS Parameter

Default

Lost Packets

Good - 0.00 to 15.00Acceptable - 15.01 to
                                                      						  30.00Fair - 30.01 to 45.00Poor - 45.01 to infinity

Jitter

Good - 0 to 20Acceptable - 21 to 100Fair - 101 to
                                                      						  150Poor - 151 to infinity

Latency

No default values apply.

To add rows, check the check box for the row above which you want
                                       			 to add a new row and click the Add Rows link.

The new row gets added above the row that you checked, and the
                                          				check box is cleared.

The rows represent the values that CAR uses to quantify the
                                          				conditions good, acceptable, fair, and poor in the QoS reports. For each value
                                          				set, enter the upper and lower limits in the From and To columns.

To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link.

For each value that you have set, choose the Quality of Service.

Click the Update button.

To restore the default QoS values, click the Restore Defaults button.

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Note | Be aware that the classifications of "NA" and "Infinity" are case-sensitive. |
|---|---|

| Step 1 | Choose Report Config > Define
                                             				  QoS . The Define Quality of Service window displays. The following table
                                          				describes the QoS default values. Table 1. QoS Default Values QoS Parameter Default Lost Packets Good - 0.00 to 15.00Acceptable - 15.01 to
                                                      						  30.00Fair - 30.01 to 45.00Poor - 45.01 to infinity Jitter Good - 0 to 20Acceptable - 21 to 100Fair - 101 to
                                                      						  150Poor - 151 to infinity Latency No default values apply. | QoS Parameter | Default | Lost Packets | Good - 0.00 to 15.00Acceptable - 15.01 to
                                                      						  30.00Fair - 30.01 to 45.00Poor - 45.01 to infinity | Jitter | Good - 0 to 20Acceptable - 21 to 100Fair - 101 to
                                                      						  150Poor - 151 to infinity | Latency | No default values apply. |
|---|---|---|---|---|---|---|---|---|---|
| QoS Parameter | Default |
| Lost Packets | Good - 0.00 to 15.00Acceptable - 15.01 to
                                                      						  30.00Fair - 30.01 to 45.00Poor - 45.01 to infinity |
| Jitter | Good - 0 to 20Acceptable - 21 to 100Fair - 101 to
                                                      						  150Poor - 151 to infinity |
| Latency | No default values apply. |
| Step 2 | To add rows, check the check box for the row above which you want
                                       			 to add a new row and click the Add Rows link. The new row gets added above the row that you checked, and the
                                          				check box is cleared. The rows represent the values that CAR uses to quantify the
                                          				conditions good, acceptable, fair, and poor in the QoS reports. For each value
                                          				set, enter the upper and lower limits in the From and To columns. Note To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link. | Note | To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link. |
| Note | To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link. |
| Step 3 | For each value that you have set, choose the Quality of Service. |
| Step 4 | Click the Update button. Tip To restore the default QoS values, click the Restore Defaults button. | Tip | To restore the default QoS values, click the Restore Defaults button. |
| Tip | To restore the default QoS values, click the Restore Defaults button. |

| QoS Parameter | Default |
|---|---|
| Lost Packets | Good - 0.00 to 15.00Acceptable - 15.01 to
                                                      						  30.00Fair - 30.01 to 45.00Poor - 45.01 to infinity |
| Jitter | Good - 0 to 20Acceptable - 21 to 100Fair - 101 to
                                                      						  150Poor - 151 to infinity |
| Latency | No default values apply. |

| Note | To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link. |
|---|---|

| Tip | To restore the default QoS values, click the Restore Defaults button. |
|---|---|