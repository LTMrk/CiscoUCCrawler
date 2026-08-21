---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-report-343da5b0c5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_Reporting-User-Guide-12-5/pcce_b_cisco-packaged-contact-center-enterprise_chapter_01110.html
retrieved_at: 2026-08-21T16:58:13.995107+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

Updated: February 4, 2020

Chapter: Task Handling Metrics

## Chapter: Task Handling Metrics

# Task Handling Metrics

## Average Speed of Answer

Average Speed of Answer (ASA) is the average answer wait time (the sum of the time that all incoming tasks waited before being
                           answered).  Answer wait time includes delay time, queue time, and ring time.  ASA starts when the call enters a queue, and
                           is set for four entities:

Agent

Call type

Skill group

Precision queue

ASA is reported in hours, minutes, and seconds (HH:MM:SS).

For agents, the ASA is calculated by dividing the total answer wait time for calls answered by the agent  by the number of
                           calls that the agent answered. (AnswerWaitTime/CallsAnswered)

For call types, ASA is calculated by dividing the total answer wait time for the call type by the number of calls that were
                           handled by that call type. (AnswerWaitTime/CallsHandled)

For skill groups and precision queues, ASA is calculated by dividing the total answer wait time for calls answered by the
                           skill group or precision queue  by the number of calls that were answered by that skill group or precision queue. (AnswerWaitTime/CallsAnswered).
                           Consider this example:

A call is queued at skill group X for 30 seconds.

The call is then queued at skill group Y for 10 seconds.

In this case, the total queue time is 40 seconds and is used to calculate ASA for skill group Y, even though the call only
                           queued at skill group Y for 10 seconds.

## Service Level

Service levels help you set and measure goals for answering calls.

All calls
                           that are either answered or abandoned within a specified interval
                           are considered to be service level calls offered for that interval.

Two important configuration
                           parameters contribute to the calculation of service level:

Service level threshold --the number of seconds you set as a goal to treat a call. To calculate the
                                 service level for a period of time, Packaged CCE determines the number
                                 of calls that have had a service level event within that interval. For example, if your goal is to answer 80% of calls within
                                 two minutes, you would set the service level threshold to be 120 seconds.  Reports show you the percentage of calls that have
                                 had a service level event  within that interval.

Service level type --determines how calls that abandon before the service level threshold
                                 impact the service level calculation.  There are three options for service level type:

Ignore --Abandoned calls are excluded from the service level calculation.

Negative  impact --Calls that abandon within the service level threshold are not counted as treated calls.

Positive impact --Calls that abandon within the service level threshold are counted as treated calls.

The calculations for service level are based on the
                           service level type defined for the service level configuration. They are
                           described in the following table.

Service level type

Formula used to
                                       determine service level

Ignore abandoned calls

ServiceLevelCalls / (ServiceLevelCallsOffered –
                                       ServiceLevelAband)

Negative impact
                                       of abandoned calls

ServiceLevelCalls /  (ServiceLevelCallsOffered)

Positive impact of abandoned calls

(ServiceLevelCalls + ServiceLevelAband) 
                                       / (ServiceLevelCallsOffered

For an example of how service level type is calculated,
                           consider the following call counts:

Answered within
                                 service level threshold (ServiceLevelCalls) = 70 calls

Abandoned within service level threshold (ServiceLevelAband) = 10 calls

Exceeded service level threshold
                                 (ServiceLevelCallsOffered – (ServiceLevelCalls + ServiceLevelAband)) = 20 calls

Total service level events (ServiceLevelCallsOffered)
                                 = 100 calls

For these call counts, the service level
                           is calculated as follows:

For this service level
                                       type:

The service level calculation is:

Abandoned calls
                                       ignored

70 / (100-10) = 77%

Abandoned calls negatively impact

70 /100 = 70%

Abandoned calls
                                       positively impact

(70 + 10) / 100 = 80%

Service level threshold and type  can be set for the system as a whole and for individual call types, skill groups, and precision
                           queues. Settings for individual entities  override those set at the system level.

### Service Level at the Call Type

For measuring overall customer experience, the call type provides the
                              most insight into call treatment and how callers are experiencing the
                              system.

The service level threshold timer at the call type starts
                              as soon as the call enters the call type that has a service level defined. When
                              the service level timer expires, the service level is applied to the current
                              call type associated with the call.

Only call types that are
                              associated with scripts that use the Queue To nodes define
                              service levels. If a call type is changed using the Requalify or Call Type
                              nodes, then the service threshold timer is reset.

There are four service level events that can
                              occur for the call type:

The call is answered by an
                                    agent before the service level threshold expires. In this case, the
                                    ServiceLevelsCallsOffered and ServiceLevelCalls database fields are
                                    incremented.

The call abandons while in the  Unified CVP or at the agent's phone before the service level threshold expires.
                                    In this case, the ServiceLevelCallsOffered and ServiceLevelAband database
                                    fields are incremented.

The call redirects on no answer
                                    before the service level threshold expires. In this case, the
                                    ServiceLevelCallsOffered database field is
                                    incremented.

The service level threshold timer
                                    expires; for example, the call reaches the service level threshold without being
                                    answered by an agent or abandoned. In this case, the ServiceLevelCallsOffered
                                    database field is incremented.

If calls encounter an
                              error before the service level threshold expires, the ServiceLevelError
                              database field is incremented, but ServiceLevelOffered is not incremented. If
                              the call encounters an error after the service level threshold expires,
                              ServiceLevelOffered is incremented.

To exclude errors from your service
                              level calculation, adjust the
                              ServiceLevelCallsOffered by excluding error calls: adjusted SL Offered calls =
                              SL Offered calls – (Total Error calls - ServiceLevelError).

In this example, abandoned calls have a negative impact: ServiceLevel =
                              ServiceLevelCalls / (ServiceLevelCallsoffered – (AgentErrorCount + ErrorCount –
                              ServiceLevelError)).

### Service Level at the Skill Group and Precision Queue

At the skill group and precision queue level, the service level metric is useful for
                              monitoring agent, skill group, and precision queue performance. The service level threshold timer
                              at the skill group or precision queue starts as soon as the call is queued to a skill group or precision queue.

There are five service
                              level events that can occur for a skill group or precision queue:

The
                                    call is answered by an agent before the service level threshold expires. In
                                    this case, the ServiceLevelsCallsOffered and ServiceLevelCalls database fields
                                    are incremented for the skill group or precision queue that answered the call. If
                                    the call is queued to more than one skill group, then the ServiceLevelsCallsOffered
                                    and ServiceLevelCallsDequeued database fields are incremented for the other
                                    skill groups or precision queues.

The call is dequeued from a skill group or precision queue
                                    before the service level threshold expires. In this case
                                    ServiceLevelsCallsOffered and ServiceLevelCallsDequeued database fields are
                                    incremented. Calls may be dequeued using the Cancel Queue node, when they are
                                    de-queued from the skill group or precision queue to be routed to a different skill group or precision queue.

The call abandons while in the VRU (queue) or at the agent's
                                    phone before the service level threshold expires. In this case, the
                                    ServiceLevelCallsOffered and ServiceLevelAband database fields are incremented.

The call redirects on no answer before the service
                                    level threshold expires. In this case, the ServiceLevelCallsOffered database field is incremented.

The
                                    service level threshold timer expires. Example: the call reaches the service
                                    level threshold without being answered by an agent or abandoned. In this case,
                                    the ServiceLevelCallsOffered database field is incremented.

If you want to remove
                                          errors from ServiceLevelCallsOffered, you can use this formula in a custom report:
                                          ServiceLevelCallsOffered – (Errors – SLErrors).

## Bucket Intervals

Bucket intervals allow you to track data for calls
                              abandoned or answered within specific time increments. For example, you can track data for calls abandoned or answered between
                              0
                              and 8 seconds, or under 60 seconds.

Bucket intervals are associated with the following:

Call types

Skill groups

Precision queues

You can set bucket intervals  for the system as a whole and for individual call types, skill groups, and precision queues.
                              Settings for individual entities  override settings set at the system level.

Service
                              level tells you what percentage of calls are being answered within a certain
                              time, but does not tell you how closely to the service level calls are being
                              answered or abandoned. Bucket intervals provide more insight into how
                              long callers are waiting before their calls are answered or before they
                              abandon.

For example, if your service level is two minutes, you
                              might want to set up intervals for 30 seconds, one minute, 90 seconds, 120
                              seconds, 180 seconds, 210 seconds, and 240 seconds. Using these intervals, you
                              can see whether calls are being answered in the 30 seconds after the
                              service level threshold of 180 seconds or if most are waiting a full minute
                              longer to be answered.

The intervals also give you insight into
                              how long callers are willing to wait before abandoning. Many callers do
                              not abandon until two minutes past the service level. This might indicate that
                              you can modify your service level goal.

To avoid inconsistencies in reporting, create a new Bucket Interval List with your desired parameters. Follow this updated
                              Bucket Interval parameter for Call Types, Skill Groups or Precision Queues only at specific times (that is, end of the day,
                              week, or month). Ensure that no one is running the reports for the intervals, while you modify the boundaries.

| Note | Service level is not affected for calls
                                    that are neither answered nor abandoned within the service level time. For
                                    example, calls that encounter an error condition within the service level threshold do not affect
                                    the service level. |
|---|---|

| Service level type | Formula used to
                                       determine service level |
|---|---|
| Ignore abandoned calls | ServiceLevelCalls / (ServiceLevelCallsOffered –
                                       ServiceLevelAband) |
| Negative impact
                                       of abandoned calls | ServiceLevelCalls /  (ServiceLevelCallsOffered) |
| Positive impact of abandoned calls | (ServiceLevelCalls + ServiceLevelAband) 
                                       / (ServiceLevelCallsOffered |

| For this service level
                                       type: | The service level calculation is: |
|---|---|
| Abandoned calls
                                       ignored | 70 / (100-10) = 77% |
| Abandoned calls negatively impact | 70 /100 = 70% |
| Abandoned calls
                                       positively impact | (70 + 10) / 100 = 80% |

| Note | If you want to remove
                                          errors from ServiceLevelCallsOffered, you can use this formula in a custom report:
                                          ServiceLevelCallsOffered – (Errors – SLErrors). |
|---|---|