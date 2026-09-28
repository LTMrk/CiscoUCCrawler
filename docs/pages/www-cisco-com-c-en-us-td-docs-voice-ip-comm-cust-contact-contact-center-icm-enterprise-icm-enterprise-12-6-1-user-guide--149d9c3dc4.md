---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--149d9c3dc4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/reporting-concepts-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/network-queuing-and-reporting.html
retrieved_at: 2026-08-16T20:42:47.793454+00:00
---

Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

# Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

Updated: June 27, 2023

Chapter: Network Queuing and Reporting

## Chapter: Network Queuing and Reporting

- Network Queuing and Reporting

- Network VRU and                               	 Call Type                               	 Metrics

- Network VRU and Skill                              	 Group Metrics

# Network Queuing and Reporting

## Network VRU and Call Type 
                        	 Metrics

All of the Call Type metrics apply to both Unified CCE and Unified ICM . In Unified CCE systems, Answer Wait Time, ASA, and Service Level include both the time spent in the network queue and the
                              time spent in the ACD queue.

The measurement of Answer
                              		  Wait Time for a call begins when the call is queued . The
                              		  measurement of Service Level begins when the call arrives at the
                              		  routing script, or when its call type is changed . This
                              		  means that if self-service is performed on a call before the call is queued to
                              		  an agent, the routing script must be set up to change the call type of the call
                              		  when self-service is completed. Otherwise, the time spent in self-service
                              		  negatively impacts the Service Level.

With regard to ICM-Not-TR
                              		  systems, the Call Type abandoned metrics allow you to determine the number of
                              		  calls that abandoned while queued in the CallRouter, but they do not allow you
                              		  to determine the number of calls that abandoned while in self service, nor the
                              		  number of calls that were abandoned after they leave the VRU and before an
                              		  agent answers them. The Call Type answered metrics are always zero. The Call
                              		  Type Service Level metrics are meaningless and can be ignored.

The following table
                              		  shows the fields in the Call_Type_Real_Time table that affect reporting metrics
                              		  by metric category:

Queued
                                          					 Metrics

At VRU
                                          					 Metrics/ Answered Metrics

Service
                                          					 Level Metrics

Abandoned
                                          					 Metrics

AvgRouterDelayQHalf

AvgRouterDelayQNow

AvgRouterDelayQTo5

AvgRouterDelayQToday

CallsLeftQTo5

CallsAtVRUNow

RouterCallsQNow

RouterCallsQNowTime

RouterLongestCallQ

RouterQueueCallsHalf

RouterQueueCallsTo5

RouterQueueCallsToday

RouterQueueWaitTimeHalf

RouterQueueWaitTimeTo5

RouterQueueWaitTimeToday

ServiceLevelCallsQHeld

At VRU :

CallsAtVRUNow

Answered:

AnsweredWaitTimeHalf

AnswerWaitTimeTo5

AnswerWaitTimeToday

CallsAnsweredHalf

CallsAnsweredTo5

CallsAnsweredToday

CallsAtAgentNow

ServiceLevelAbandHalf

ServiceLevelAbandTo5

ServiceLevelAbandToday

ServiceLevelCallsHalf

ServiceLevelCallsTo5

ServiceLevelCallsToday

ServiceLevelCallsOfferedHalf

ServiceLevelCallsOfferedTo5

ServiceLevelCallsOfferedToday

ServiceLevelHalf

ServiceLevelTo5

ServiceLevelToday

CallDelayAbandTimeHalf

CallDelayAbandTimeTo5

CallDelayAbandTimeToday

CTDelayAbandTimeHalf

CTDelayAbandTimeTo5

CTDelayAbandTimeToday

DelayAgentAbandTimeHalf

DelayAgentAbandTimeTo55

DelayAgentAbandTimeToday

DelayQAbandTimeHalf

DelayQAbandTimeTo5

DelayQAbandTimeToday

RouterCallsAbandQHalf

RouterCallsAbandQTo5

RouterCallsAbandQToday

RouterCallsAbandToAgentHalf

RouterCallsAbandToAgentTo5

RouterCallsAbandToAgentToday

TotalCallsAbandHalf

TotalCallsAbandTo5

TotalCallsAbandToday

The following table
                              		  shows the fields (by metric category) in the Call_Type_Interval table that
                              		  affect reporting metrics:

Queued
                                          					 Metrics

At VRU
                                          					 Metrics/ Answered Metrics

Service
                                          					 Level Metrics

Abandoned
                                          					 Metrics

AvgRouterDelayQ

CallsQHandled

RouterQueueCalls

RouterQueueCallType Limit

RouterQueueGlobalLimit

RouterQueueWaitTime

At VRU :

CTVRUTime

VRUTime

Answered:

AnsInterval1
                                          					 - AnsInterval10

AnswerWaitTime

CallsAnswered

ServiceLevelAband

ServiceLevelCalls

ServieLevelCallsOffered

ServiceLevel

AbandInterval1 - AbandInterval10

CallDelayAbandTime

CTDelayAbandTime

DelayAgentAbandTime

DelayQAbandTime

RouterCallsAbandQ

RouterCallsAbandToAgent

TotalCallsAband

For additional information on the Call_Type_Real_Time and Call_Type_Interval table fields, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise .

## Network VRU and Skill
                        	 Group Metrics

For a call that is
                              		  queued by CVP, the Answer Wait Time and ASA metrics for the skill group do not
                              		  include the time spent in the network queue. However, service level metrics for
                              		  the skill group do include the time spent in the network queue.

The skill group
                              		  abandoned metrics allow you to determine the number of calls that abandoned
                              		  while queued to the CallRouter , but
                              		  they do not allow you to determine the number of calls that abandoned after
                              		  they left the VRU and before an agent
                              		  answered them. The skill group answered
                                 			 metrics are always zero. The skill group service level metrics are meaningless
                                 			 and can be ignored.

The following table
                              		  shows the fields (by metric category) in the Skill_Group_Real_Time table that
                              		  affect reporting metrics:

Queued
                                          					 Metrics

At VRU Metrics/ Answered
                                          					 Metrics

Service
                                          					 Level Metrics

Abandoned
                                          					 Metrics

CallsQueuedNow

LongestCallQ

RouterCallsQNow

RouterLongestCallInQ

At VRU:

None.

Answered:

AnswerWaitTimeTo5

CallsAnsweredTo5

ServiceLevelTo5

ServiceLevelCallsTo5

ServiceLevelCallsAbandTo5

ServiceLevelCallsDequeuedTo5

ServiceLevelRonaTo5

ServiceLevelCallsOfferedTo5

RouterCallsAbandQTo5

RouterCallsAbandToAgentTo5

The following table
                              		  shows the fields (by metric category) in the Skill_Group_Interval table that
                              		  affect reporting metrics:

Queued
                                          					 Metrics

At VRU Metrics/ Answered
                                          					 Metrics

Service
                                          					 Level Metrics

Abandoned
                                          					 Metrics

CallsQueued

RouterQueueCalls

At VRU:

None.

Answered:

AnswerWaitTime

CallsAnswered

ServiceLevel

ServiceLevelCalls

ServiceLevelCallsAband

ServiceLevelCallsDequeued

ServiceLevelError

AbandonRingCalls

AbandonRingTime

RouterCallsAbandQ

RouterCallsAbandToAgent

For additional information about the Skill_Group_Real_Time and Skill_Group_Interval table fields, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

| Queued
                                          					 Metrics | At VRU
                                          					 Metrics/ Answered Metrics | Service
                                          					 Level Metrics | Abandoned
                                          					 Metrics |
|---|---|---|---|
| AvgRouterDelayQHalf AvgRouterDelayQNow AvgRouterDelayQTo5 AvgRouterDelayQToday CallsLeftQTo5 CallsAtVRUNow RouterCallsQNow RouterCallsQNowTime RouterLongestCallQ RouterQueueCallsHalf RouterQueueCallsTo5 RouterQueueCallsToday RouterQueueWaitTimeHalf RouterQueueWaitTimeTo5 RouterQueueWaitTimeToday ServiceLevelCallsQHeld | At VRU : CallsAtVRUNow Answered: AnsweredWaitTimeHalf AnswerWaitTimeTo5 AnswerWaitTimeToday CallsAnsweredHalf CallsAnsweredTo5 CallsAnsweredToday CallsAtAgentNow | ServiceLevelAbandHalf ServiceLevelAbandTo5 ServiceLevelAbandToday ServiceLevelCallsHalf ServiceLevelCallsTo5 ServiceLevelCallsToday ServiceLevelCallsOfferedHalf ServiceLevelCallsOfferedTo5 ServiceLevelCallsOfferedToday ServiceLevelHalf ServiceLevelTo5 ServiceLevelToday | CallDelayAbandTimeHalf CallDelayAbandTimeTo5 CallDelayAbandTimeToday CTDelayAbandTimeHalf CTDelayAbandTimeTo5 CTDelayAbandTimeToday DelayAgentAbandTimeHalf DelayAgentAbandTimeTo55 DelayAgentAbandTimeToday DelayQAbandTimeHalf DelayQAbandTimeTo5 DelayQAbandTimeToday RouterCallsAbandQHalf RouterCallsAbandQTo5 RouterCallsAbandQToday RouterCallsAbandToAgentHalf RouterCallsAbandToAgentTo5 RouterCallsAbandToAgentToday TotalCallsAbandHalf TotalCallsAbandTo5 TotalCallsAbandToday |

| Queued
                                          					 Metrics | At VRU
                                          					 Metrics/ Answered Metrics | Service
                                          					 Level Metrics | Abandoned
                                          					 Metrics |
|---|---|---|---|
| AvgRouterDelayQ CallsQHandled RouterQueueCalls RouterQueueCallType Limit RouterQueueGlobalLimit RouterQueueWaitTime | At VRU : CTVRUTime VRUTime Answered: AnsInterval1
                                          					 - AnsInterval10 AnswerWaitTime CallsAnswered | ServiceLevelAband ServiceLevelCalls ServieLevelCallsOffered ServiceLevel | AbandInterval1 - AbandInterval10 CallDelayAbandTime CTDelayAbandTime DelayAgentAbandTime DelayQAbandTime RouterCallsAbandQ RouterCallsAbandToAgent TotalCallsAband |

| Note | None of the skill
                                       		  group metrics include time spent in self-service or calls that ended during
                                       		  self-service, because a call is not associated with a skill group until it is
                                       		  queued, and a call is queued after self-service is complete. |
|---|---|

| Queued
                                          					 Metrics | At VRU Metrics/ Answered
                                          					 Metrics | Service
                                          					 Level Metrics | Abandoned
                                          					 Metrics |
|---|---|---|---|
| CallsQueuedNow LongestCallQ RouterCallsQNow RouterLongestCallInQ | At VRU: None. Answered: AnswerWaitTimeTo5 CallsAnsweredTo5 | ServiceLevelTo5 ServiceLevelCallsTo5 ServiceLevelCallsAbandTo5 ServiceLevelCallsDequeuedTo5 ServiceLevelRonaTo5 ServiceLevelCallsOfferedTo5 | RouterCallsAbandQTo5 RouterCallsAbandToAgentTo5 |

| Queued
                                          					 Metrics | At VRU Metrics/ Answered
                                          					 Metrics | Service
                                          					 Level Metrics | Abandoned
                                          					 Metrics |
|---|---|---|---|
| CallsQueued RouterQueueCalls | At VRU: None. Answered: AnswerWaitTime CallsAnswered | ServiceLevel ServiceLevelCalls ServiceLevelCallsAband ServiceLevelCallsDequeued ServiceLevelError | AbandonRingCalls AbandonRingTime RouterCallsAbandQ RouterCallsAbandToAgent |