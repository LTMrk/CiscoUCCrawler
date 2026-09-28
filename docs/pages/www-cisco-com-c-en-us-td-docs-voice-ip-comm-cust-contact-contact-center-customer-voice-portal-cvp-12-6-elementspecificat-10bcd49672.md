---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-10bcd49672
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_c3df2ca6_00_callback_set_queue_defaults.html
retrieved_at: 2026-08-21T17:23:49.713329+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Callback_Set_Queue_Defaults

## Chapter: Callback_Set_Queue_Defaults

# Callback_Set_Queue_Defaults

The Callback_Set_Queue_Defaults element is responsible for
                                    				updating the DBServlet with the values that should be used for each queue.
                                    				There is always a default queue type. The values are used whenever a queue type is encountered for which
                                    				there are no explicitly defined values. For example, if an administrator has
                                    				defined values for a billing and default queues, but the caller is queued for mortgages .
                                    				In that case, the application uses the values from Callback_Set_Queue_Defaults .

When the
                                                				  DBServlet is not reachable to check the callback status for the duration of
                                                				  keepalive interval, the callback entry in the Reporting Server gets marked as a
                                                				  stale cached entry and subsequently gets cleared. As a result, a callback is
                                                				  not initiated.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Queue Name

string

Yes

true

false

None

The name of the queue.

Maximum Percentage

integer

No

true

false

50

Maximum percentage of
                                          callbacks that can exist in the queue. Maximum is 100, minimum is
                                          0.

Maximum
                                          Count

integer

No

true

false

9999999

Absolute number of
                                          callbacks that can exist in a queue.

Refresh Interval

integer

No

true

false

30

Number of minutes between
                                          DBServlet refreshes of this reference data. Maximum is 1440 minutes, minimum is
                                          1 minute.

Maximum
                                          Estimated Wait Time

integer

No

true

false

900

Callbacks are only offered for this queue when the estimated wait time
                                          (ewt) is greater than or equal this number of seconds. If 0, then callbacks are
                                          offered regardless of ewt. Maximum is 86400 seconds, minimum is
                                          0.

Timezone

string
                                          enum

No

true

false

None

The timezone to apply to this queue. Valid options
                                          available from pull-down menu.

Keepalive Interval

integer

No

true

false

180

Maximum keepalive interval in seconds. Maximum is 300, minimum is 1.
                                          'Ring No Answer Timeout' setting must be less than this
                                          value.

Dialed
                                          Number

string

No

true

false

None

Dialed Number to which a callback is directed for this queue.

Reconnect
                                          Time

integer

No

true

false

30

Approximate average time in
                                          seconds to reconnect caller. Take into account both ringtime and IVR time when
                                          determining this value. Maximum is 300, minimum is 1.

Service Level Agreement (SLA)

integer

No

true

false

60

Average number of seconds to wait before connecting to an agent after a
                                          caller is called back.

Calling Line ID

string

Yes

true

false

None

The CLI to be used on the
                                          callback.

Sample

string

No

true

false

0

Number of minutes in the
                                          interval used to calculate average time to leave queue. Maximum is 1440,
                                          minimum is 15.

Burst

string

No

true

false

10:1

X:Y, where X requests to
                                          method LeaveQueue in Y seconds. This is used to detect abnormal system failures
                                          so that the requests do not get included in the average time to leave queue
                                          calculation.

Ring No
                                          Answer Timeout

integer

No

true

false

30

The
                                          RNA timeout for the callback. Maximum is 300, minimum is 0. Must be less than
                                          the Keepalive Interval.

Sunday Time Range

string

No

true

false

00:00:00 – 23:59:59

Time range per
                                          day when callbacks can occur. Value "none" means no callbacks are allowed on
                                          that day. The default is all day if no value is specified. 00:00:00 – 23:59:59
                                          means all day.

Monday
                                          Time Range

Tuesday Time
                                          Range

Wednesday Time
                                          Range

Thursday Time
                                          Range

Friday Time
                                          Range

Saturday Time
                                          Range

Max No Response
                                          Count

string

No

true

false

3;300

Max Busy
                                          Count

string

No

true

false

4;300

Max
                                          attempts to try the callback when this error occurs and the next the interval
                                          (in seconds) in which to retry the call.

Max No Answer Count

string

No

true

false

4;300

Max Trunks
                                          Busy Count

string

No

true

false

4;300

Max Error
                                          Count

string

No

true

false

4;300

## Element Data

Name

Type

Notes

result

string

Contains the reconnect exit
                                          state.

## Exit States

Name

Notes

done

The element is successfully run and the value is retrieved.

error

The element failed to
                                          retrieve the
                                          value.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Cisco > Callback

com.cisco.cvp.vxml.custelem.callback.SetQueueDefaults

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| The Callback_Set_Queue_Defaults element is responsible for
                                    				updating the DBServlet with the values that should be used for each queue.
                                    				There is always a default queue type. The values are used whenever a queue type is encountered for which
                                    				there are no explicitly defined values. For example, if an administrator has
                                    				defined values for a billing and default queues, but the caller is queued for mortgages .
                                    				In that case, the application uses the values from Callback_Set_Queue_Defaults . Note When the
                                                				  DBServlet is not reachable to check the callback status for the duration of
                                                				  keepalive interval, the callback entry in the Reporting Server gets marked as a
                                                				  stale cached entry and subsequently gets cleared. As a result, a callback is
                                                				  not initiated. | Note | When the
                                                				  DBServlet is not reachable to check the callback status for the duration of
                                                				  keepalive interval, the callback entry in the Reporting Server gets marked as a
                                                				  stale cached entry and subsequently gets cleared. As a result, a callback is
                                                				  not initiated. |
|---|---|---|
| Note | When the
                                                				  DBServlet is not reachable to check the callback status for the duration of
                                                				  keepalive interval, the callback entry in the Reporting Server gets marked as a
                                                				  stale cached entry and subsequently gets cleared. As a result, a callback is
                                                				  not initiated. |

| Note | When the
                                                				  DBServlet is not reachable to check the callback status for the duration of
                                                				  keepalive interval, the callback entry in the Reporting Server gets marked as a
                                                				  stale cached entry and subsequently gets cleared. As a result, a callback is
                                                				  not initiated. |
|---|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Queue Name | string | Yes | true | false | None | The name of the queue. |
| Maximum Percentage | integer | No | true | false | 50 | Maximum percentage of
                                          callbacks that can exist in the queue. Maximum is 100, minimum is
                                          0. |
| Maximum
                                          Count | integer | No | true | false | 9999999 | Absolute number of
                                          callbacks that can exist in a queue. |
| Refresh Interval | integer | No | true | false | 30 | Number of minutes between
                                          DBServlet refreshes of this reference data. Maximum is 1440 minutes, minimum is
                                          1 minute. |
| Maximum
                                          Estimated Wait Time | integer | No | true | false | 900 | Callbacks are only offered for this queue when the estimated wait time
                                          (ewt) is greater than or equal this number of seconds. If 0, then callbacks are
                                          offered regardless of ewt. Maximum is 86400 seconds, minimum is
                                          0. |
| Timezone | string
                                          enum | No | true | false | None | The timezone to apply to this queue. Valid options
                                          available from pull-down menu. |
| Keepalive Interval | integer | No | true | false | 180 | Maximum keepalive interval in seconds. Maximum is 300, minimum is 1.
                                          'Ring No Answer Timeout' setting must be less than this
                                          value. |
| Dialed
                                          Number | string | No | true | false | None | Dialed Number to which a callback is directed for this queue. |
| Reconnect
                                          Time | integer | No | true | false | 30 | Approximate average time in
                                          seconds to reconnect caller. Take into account both ringtime and IVR time when
                                          determining this value. Maximum is 300, minimum is 1. |
| Service Level Agreement (SLA) | integer | No | true | false | 60 | Average number of seconds to wait before connecting to an agent after a
                                          caller is called back. |
| Calling Line ID | string | Yes | true | false | None | The CLI to be used on the
                                          callback. |
| Sample | string | No | true | false | 0 | Number of minutes in the
                                          interval used to calculate average time to leave queue. Maximum is 1440,
                                          minimum is 15. |
| Burst | string | No | true | false | 10:1 | X:Y, where X requests to
                                          method LeaveQueue in Y seconds. This is used to detect abnormal system failures
                                          so that the requests do not get included in the average time to leave queue
                                          calculation. |
| Ring No
                                          Answer Timeout | integer | No | true | false | 30 | The
                                          RNA timeout for the callback. Maximum is 300, minimum is 0. Must be less than
                                          the Keepalive Interval. |
| Sunday Time Range | string | No | true | false | 00:00:00 – 23:59:59 | Time range per
                                          day when callbacks can occur. Value "none" means no callbacks are allowed on
                                          that day. The default is all day if no value is specified. 00:00:00 – 23:59:59
                                          means all day. |
| Monday
                                          Time Range |
| Tuesday Time
                                          Range |
| Wednesday Time
                                          Range |
| Thursday Time
                                          Range |
| Friday Time
                                          Range |
| Saturday Time
                                          Range |
| Max No Response
                                          Count | string | No | true | false | 3;300 |
| Max Busy
                                          Count | string | No | true | false | 4;300 | Max
                                          attempts to try the callback when this error occurs and the next the interval
                                          (in seconds) in which to retry the call. |
| Max No Answer Count | string | No | true | false | 4;300 |
| Max Trunks
                                          Busy Count | string | No | true | false | 4;300 |
| Max Error
                                          Count | string | No | true | false | 4;300 |

| Name | Type | Notes |
|---|---|---|
| result | string | Contains the reconnect exit
                                          state. |

| Name | Notes |
|---|---|
| done | The element is successfully run and the value is retrieved. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.SetQueueDefaults |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |