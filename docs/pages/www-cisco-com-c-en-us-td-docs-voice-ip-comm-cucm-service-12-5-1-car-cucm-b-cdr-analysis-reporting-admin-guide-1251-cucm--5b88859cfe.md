---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--5b88859cfe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0100010.html
retrieved_at: 2026-08-21T01:37:41.244650+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR Rating Engine

## Chapter: CAR Rating Engine

# CAR Rating Engine

Use the CAR rating engine configuration to define the base rate
                        		and duration, time of day, and voice quality rating parameters for calls.

Rating parameters for calls get used during CAR loading. If you want
                                    		  old CDR records in the CAR database to use new values for these parameters, you
                                    		  must reload all the CDRs in the CAR database.

## Set Base Rate

To establish a cost basis for calls, you must specify a base
                              		  rate for all calls. For example, if your service provider charges you 6 cents
                              		  for each minute, billed in 10-second increments, you can set the base rate at
                              		  which all calls are charged at 1 cent for each 10-second increment.

This section describes how to establish the base charge and
                              		  duration values.

If you use the default base charge value, reports do not provide any
                                          			 costs. The system provides default values, but if left to the defaults, the
                                          			 Rating Engine stays disabled and does not provide costs.

Choose Report Config > Rating
                                                					 Engine > Duration .

The Call Duration window displays.

In the To (seconds) field, enter the seconds for which you want
                                       			 the base charge to be applied. For example, if you are billed in 6-second
                                       			 increments, enter 6 in this field. If you are billed a flat rate for each
                                       			 minute regardless of call duration, enter 60 in this field, so the charge is
                                       			 based on whole minutes.

In the Base Charge/Block field, enter the cost basis for the seconds that are shown in the
                                       			 To (seconds) field. For example, if you are billed 6 cents for each minute in
                                       			 6-second increments, enter 0.006 in this field. If you are billed 7 cents for
                                       			 each minute in whole minutes (no incremental billing), enter 0.07 in this
                                       			 field.

In the preceding examples, if you are billed in 6-second
                                          				increments and the cost is 0.006 for each 6-second increment, a call that lasts
                                          				7 seconds would cost 0.012. Rationale: Each 6-second increment costs 0.006, and
                                          				two blocks from 0 to 6 seconds occurred.

Likewise, if you are billed in whole minutes and the cost is 7
                                          				cents for each minute, a call that lasted 3 minutes would cost 21 cents.
                                          				Rationale: Each 60-second increment costs 7 cents, and three blocks of 1 minute
                                          				occurred.

Click the Update button.

To restore the default setting, click the Restore Defaults button. By restoring the
                                                      				  default value of 0 for the call charge/block, you effectively disable the other
                                                      				  factors that are used in determining call cost.

## Factor Time of Day

To further define the cost of calls, you can specify a
                              		  multiplication factor for certain times of day. For example, if you want to
                              		  charge subscribers a premium for daytime calls, you can apply a multiplication
                              		  factor to the base charge/block that you specified in the Call Duration window.

This section describes how to establish certain times of day
                              		  when calls cost more.

If you do not want to increase call cost by time of day, you can use
                                          			 the default values. The default multiplication factor specifies 1, so no
                                          			 increase in call cost for time of day occurs.

Choose Report Config > Rating
                                                					 Engine > Time of Day .

The Time of Day window displays.

To add rows, click the Add Rows link.

The system adds a row between 00:00:00 and 23:59:59.

To add additional rows, check the check box for the row above
                                       			 which you want to add a new row and click the Add Rows link.

To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link.

Enter the From and To time ranges in 24-hour, minute, and second
                                       			 format. A 24-hour period, from 00:00:00 to 23:59:59, represents the default
                                       			 time range. If you want to set one time-of-day range from 8 am to 5 pm, you
                                       			 will need to establish three time-of-day ranges: the first from 00:00:00 to
                                       			 07:59:59, the second from 08:00:00 to 16:59:59, and the third from 17:00:00 to
                                       			 23:59:59.

You must use Coordinated Universal Time (UTC), rather than a
                                                      				  12-hour clock, when factoring Time of Day into Call Cost.

Enter the Multiplication Factor that designates a number by which
                                       			 you want the base charge/block to be multiplied when a call occurs in the
                                       			 specified time range. For example, if you charge a premium of double the price
                                       			 for calls that are placed between 8 a.m. and 5 p.m., the multiplication factor
                                       			 equals 2.00. A multiplication factor of 1.00 does not affect the cost of the
                                       			 call.

To add the time-of-day and multiplication factors, click the Update button.

To restore the default setting, click the Restore Defaults button.

## Factor Voice Quality

To further define the cost of calls, you can specify a multiplication factor for the voice quality of a call. For example,
                              if subscribers are paying a premium price to ensure the highest voice quality on calls, you can apply various multiplication
                              factors to the base charge/block that you specified in the Call Duration window depending on the voice quality. Using a multiplication
                              factor other than 1.00 helps differentiate between the various voice qualities calls as well.

This section describes how to establish call cost when calls
                              		  that have a certain voice quality cost more.

If you do not want to increase, call cost by voice quality, you can use the default values. The default multiplication factor
                                          equals 1.00, so no increase in call cost occurs for voice quality.

Choose Report Config > Rating
                                             				  Engine > Voice Quality .

The Voice Quality window displays.

In the Multiplication Factor field, enter the number by which you want the base charge/block to be multiplied when a call
                                       occurs in the specified voice-quality category. The 'Define QoS values' section defines the voice-quality categories: Good,
                                       Acceptable, Fair, and Poor.

Example

Voice Quality Good; Factor 1.2

Voice Quality Acceptable; Factor 1.0

Voice Quality Fair; Factor 1.0

Voice Quality Poor; Factor 0.8

A good call gets charged 1.2 times that of an acceptable or fair call. A poor call gets charged 0.8 times that of an acceptable
                                          or fair call.

Multiplication factor for a good call >= the multiplication factor for acceptable >= multiplication factor for fair >= multiplication
                                                      factor for poor.

Cick Update .

To restore the default setting, click Restore Defaults .

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Note | Rating parameters for calls get used during CAR loading. If you want
                                    		  old CDR records in the CAR database to use new values for these parameters, you
                                    		  must reload all the CDRs in the CAR database. |
|---|---|

| Note | If you use the default base charge value, reports do not provide any
                                          			 costs. The system provides default values, but if left to the defaults, the
                                          			 Rating Engine stays disabled and does not provide costs. |
|---|---|

| Step 1 | Choose Report Config > Rating
                                                					 Engine > Duration . The Call Duration window displays. |
|---|---|
| Step 2 | In the To (seconds) field, enter the seconds for which you want
                                       			 the base charge to be applied. For example, if you are billed in 6-second
                                       			 increments, enter 6 in this field. If you are billed a flat rate for each
                                       			 minute regardless of call duration, enter 60 in this field, so the charge is
                                       			 based on whole minutes. |
| Step 3 | In the Base Charge/Block field, enter the cost basis for the seconds that are shown in the
                                       			 To (seconds) field. For example, if you are billed 6 cents for each minute in
                                       			 6-second increments, enter 0.006 in this field. If you are billed 7 cents for
                                       			 each minute in whole minutes (no incremental billing), enter 0.07 in this
                                       			 field. In the preceding examples, if you are billed in 6-second
                                          				increments and the cost is 0.006 for each 6-second increment, a call that lasts
                                          				7 seconds would cost 0.012. Rationale: Each 6-second increment costs 0.006, and
                                          				two blocks from 0 to 6 seconds occurred. Likewise, if you are billed in whole minutes and the cost is 7
                                          				cents for each minute, a call that lasted 3 minutes would cost 21 cents.
                                          				Rationale: Each 60-second increment costs 7 cents, and three blocks of 1 minute
                                          				occurred. |
| Step 4 | Click the Update button. Tip To restore the default setting, click the Restore Defaults button. By restoring the
                                                      				  default value of 0 for the call charge/block, you effectively disable the other
                                                      				  factors that are used in determining call cost. | Tip | To restore the default setting, click the Restore Defaults button. By restoring the
                                                      				  default value of 0 for the call charge/block, you effectively disable the other
                                                      				  factors that are used in determining call cost. |
| Tip | To restore the default setting, click the Restore Defaults button. By restoring the
                                                      				  default value of 0 for the call charge/block, you effectively disable the other
                                                      				  factors that are used in determining call cost. |

| Tip | To restore the default setting, click the Restore Defaults button. By restoring the
                                                      				  default value of 0 for the call charge/block, you effectively disable the other
                                                      				  factors that are used in determining call cost. |
|---|---|

| Note | If you do not want to increase call cost by time of day, you can use
                                          			 the default values. The default multiplication factor specifies 1, so no
                                          			 increase in call cost for time of day occurs. |
|---|---|

| Step 1 | Choose Report Config > Rating
                                                					 Engine > Time of Day . The Time of Day window displays. |
|---|---|
| Step 2 | To add rows, click the Add Rows link. The system adds a row between 00:00:00 and 23:59:59. |
| Step 3 | To add additional rows, check the check box for the row above
                                       			 which you want to add a new row and click the Add Rows link. Note To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link. | Note | To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link. |
| Note | To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link. |
| Step 4 | Enter the From and To time ranges in 24-hour, minute, and second
                                       			 format. A 24-hour period, from 00:00:00 to 23:59:59, represents the default
                                       			 time range. If you want to set one time-of-day range from 8 am to 5 pm, you
                                       			 will need to establish three time-of-day ranges: the first from 00:00:00 to
                                       			 07:59:59, the second from 08:00:00 to 16:59:59, and the third from 17:00:00 to
                                       			 23:59:59. Note You must use Coordinated Universal Time (UTC), rather than a
                                                      				  12-hour clock, when factoring Time of Day into Call Cost. | Note | You must use Coordinated Universal Time (UTC), rather than a
                                                      				  12-hour clock, when factoring Time of Day into Call Cost. |
| Note | You must use Coordinated Universal Time (UTC), rather than a
                                                      				  12-hour clock, when factoring Time of Day into Call Cost. |
| Step 5 | Enter the Multiplication Factor that designates a number by which
                                       			 you want the base charge/block to be multiplied when a call occurs in the
                                       			 specified time range. For example, if you charge a premium of double the price
                                       			 for calls that are placed between 8 a.m. and 5 p.m., the multiplication factor
                                       			 equals 2.00. A multiplication factor of 1.00 does not affect the cost of the
                                       			 call. |
| Step 6 | To add the time-of-day and multiplication factors, click the Update button. Tip To restore the default setting, click the Restore Defaults button. | Tip | To restore the default setting, click the Restore Defaults button. |
| Tip | To restore the default setting, click the Restore Defaults button. |

| Note | To delete rows, check the check box for the row that you want to
                                                      				  delete and click the Delete Rows link. |
|---|---|

| Note | You must use Coordinated Universal Time (UTC), rather than a
                                                      				  12-hour clock, when factoring Time of Day into Call Cost. |
|---|---|

| Tip | To restore the default setting, click the Restore Defaults button. |
|---|---|

| Note | If you do not want to increase, call cost by voice quality, you can use the default values. The default multiplication factor
                                          equals 1.00, so no increase in call cost occurs for voice quality. |
|---|---|

| Step 1 | Choose Report Config > Rating
                                             				  Engine > Voice Quality . The Voice Quality window displays. |
|---|---|
| Step 2 | In the Multiplication Factor field, enter the number by which you want the base charge/block to be multiplied when a call
                                       occurs in the specified voice-quality category. The 'Define QoS values' section defines the voice-quality categories: Good,
                                       Acceptable, Fair, and Poor. Example Voice Quality Good; Factor 1.2 Voice Quality Acceptable; Factor 1.0 Voice Quality Fair; Factor 1.0 Voice Quality Poor; Factor 0.8 A good call gets charged 1.2 times that of an acceptable or fair call. A poor call gets charged 0.8 times that of an acceptable
                                          or fair call. Note Multiplication factor for a good call >= the multiplication factor for acceptable >= multiplication factor for fair >= multiplication
                                                      factor for poor. | Note | Multiplication factor for a good call >= the multiplication factor for acceptable >= multiplication factor for fair >= multiplication
                                                      factor for poor. |
| Note | Multiplication factor for a good call >= the multiplication factor for acceptable >= multiplication factor for fair >= multiplication
                                                      factor for poor. |
| Step 3 | Cick Update . Tip To restore the default setting, click Restore Defaults . | Tip | To restore the default setting, click Restore Defaults . |
| Tip | To restore the default setting, click Restore Defaults . |

| Note | Multiplication factor for a good call >= the multiplication factor for acceptable >= multiplication factor for fair >= multiplication
                                                      factor for poor. |
|---|---|

| Tip | To restore the default setting, click Restore Defaults . |
|---|---|