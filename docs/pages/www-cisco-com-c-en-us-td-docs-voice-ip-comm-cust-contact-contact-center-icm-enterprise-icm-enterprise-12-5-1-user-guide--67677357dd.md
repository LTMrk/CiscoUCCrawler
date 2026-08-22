---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--67677357dd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting-concepts-for-cisco-unified12_5/ucce_b_reporting-concepts-for-cisco-unified12_5_chapter_01001.html
retrieved_at: 2026-08-22T00:02:58.814589+00:00
---

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Average Speed of Answer

## Chapter: Average Speed of Answer

# Average Speed of Answer

## How ASA Is Calculated

Calculations for ASA differ based on the type
                              of system associated with the reporting object.

Reporting Object

Calculation

Skill_Group_Interval

Skill_Group_ Interval.AnswerWaitTime / Skill_Group_
                                          Interval.CallsAnswered

CallType _Interval

Call_Type_
                                          Interval.AnswerWaitTime / Call_Type_ Interval.CallsHandled

Call_Type_Skill_Group_Interval

Call_Type_Skill_Group_Interval. AnswerWaitTime /
                                          Call_Type_Skill_Group_Interval.CallsAnswered

Route_Real_Time. AvgSpeedAnswerTo5

N/A

Route_Half _Hour

Route_Half _Hour.AnswerWait TimeToHalf / Route_Half _Hour.CallsAnswered
                                          ToHalf

Service_Real_Time

Service_Real_Time.
                                          AvgSpeedToAnswerTo5

Service_Real_Time.AnswerWaitTimeTo5 /
                                          Service_Real_Time.CallsAnsweredTo5

Service_Interval. AnswerWaitTime

Service_Interval. AvgSpeedToAnswer

N/A

Precision Queue ASA

Skill_Group_ Interval.AnswerWaitTime / Skill_Group_ Interval.CallsAnswered

Call_Type 
                                          _Skill_Group

Call_Type _Interval

Skill_Group _Interval (Unified ICM)

Skill_Group ( Unified CCE )

Service_Interval (Unified ICM)

Service_Interval ( Unified CCE )

Delay Time/ Switch Time

Contains Network
                                          Delay

X

Contains Network Delay

Local Queue Time

X

X

X

Not Avail

X

Not Avail

Network Queue Time

SG Time

X

X

SG Time

X

Ring Time

X

X

X

X

X

X

Network Delay Time

X

X

X

## ASA for Agent and Skill Group

Agent. The ASA is calculated for
                              the agent at the PG level.

The internal queuing time is sent to the PG by Unified CCE Packaged CCE when an agent becomes available for the call. The PG adds up the internal queue time, ring time, and network time and adds
                              that into AnswerWaitTime in the agent skill group table. AnswerWaitTime is then divided by the CallsAnswered for the agent.

skill group. The ASA is calculated for the skill group at the PG level.

For Unified CCE Enterprise Queuing, the time spent in the enterprise queue is not used in the calculation of AnswerWaitTime. The calculation
                              includes the ACD queue time only.

For ACD queuing, the queue time
                              is reported by the PG based on events received from the ACD.

Consider this example:

A call is
                                    queued at skill group X.

At Time T, the call is then
                                    queued at skill group Y at time T+30 seconds.

An
                                    additional 10 seconds transpire before the call is answered by an agent at
                                    skill group Y.

In this case, the internal queuing
                              time will be 40 seconds. This is the total length that the call has been queued
                              even though it was only queued at skill group Y for 10 seconds.

The agent's PG adds the internal queue time, ring time, and network time to
                              create the total AnswerWaitTime for the call and adds it to AnswerWaitTime in
                              the skill group table. AnswerWaitTime is then divided by CallsAnswered within
                              the skill group table to arrive at the ASA for the skill group.

Precision queue. The ASA is calculated for the precision queue by summing skill
                              groups across PGs which are associated with the precision queue.

### Reports That Show ASA for Agents

The  following reports show ASA
                                 statistics for agents and skill groups:

Unified IC
                                       Peripheral Skill Group Real Time All Fields

Unified IC
                                       Peripheral Skill Group Historical All Fields

## ASA for Call Type and Service

The call type ASA is calculated as AnswerWaitTime divided by
                              CallsAnswered.

Call type ASA is applicable only when calls are
                              translation routed and includes time spent in the Enterprise Queue as well as
                              time spent in the ACD queue.

ASA for the service is computed based
                              on the AnswerWaitTime as reported from the peripheral. This value includes the time
                              spent on the ACD after the call was offered up until the time the call was
                              answered. If an Enterprise Queue is used, ASA reported for the service does not
                              include time spent in the Enterprise Queue.

### Reports That Show ASA for Call Type and Service

The following  report 
                                 contains ASA statistics:

Unified IC Call Type Historical All Fields

| Reporting Object | Calculation |
|---|---|
| Skill_Group_Interval | Skill_Group_ Interval.AnswerWaitTime / Skill_Group_
                                          Interval.CallsAnswered |
| CallType _Interval | Call_Type_
                                          Interval.AnswerWaitTime / Call_Type_ Interval.CallsHandled |
| Call_Type_Skill_Group_Interval | Call_Type_Skill_Group_Interval. AnswerWaitTime /
                                          Call_Type_Skill_Group_Interval.CallsAnswered |
| Route_Real_Time. AvgSpeedAnswerTo5 | N/A |
| Route_Half _Hour | Route_Half _Hour.AnswerWait TimeToHalf / Route_Half _Hour.CallsAnswered
                                          ToHalf |
| Service_Real_Time Service_Real_Time.
                                          AvgSpeedToAnswerTo5 | Service_Real_Time.AnswerWaitTimeTo5 /
                                          Service_Real_Time.CallsAnsweredTo5 |
| Service_Interval. AnswerWaitTime Service_Interval. AvgSpeedToAnswer | N/A |
| Precision Queue ASA | Skill_Group_ Interval.AnswerWaitTime / Skill_Group_ Interval.CallsAnswered |

| Note | The method used to calculate ASA differs based on the type of system associated with the reporting object Unified CCE ). The following table shows the calculations. X means that the value is included in the calculation. |
|---|---|

|  | Call_Type 
                                          _Skill_Group | Call_Type _Interval | Skill_Group _Interval (Unified ICM) | Skill_Group ( Unified CCE ) | Service_Interval (Unified ICM) | Service_Interval ( Unified CCE ) |
|---|---|---|---|---|---|---|
| Delay Time/ Switch Time |  |  |  | Contains Network
                                          Delay | X | Contains Network Delay |
| Local Queue Time | X | X | X | Not Avail | X | Not Avail |
| Network Queue Time | SG Time | X | X | SG Time |  | X |
| Ring Time | X | X | X | X | X | X |
| Network Delay Time | X | X | X |  |  |  |