---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--72d49b4623
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting-concepts-for-cisco-unified12_5/ucce_b_reporting-concepts-for-cisco-unified12_5_chapter_01110.html
retrieved_at: 2026-08-22T00:03:20.169909+00:00
---

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Short Calls, Abandoned Calls, and Overflow Calls

## Chapter: Short Calls, Abandoned Calls, and Overflow Calls

# Short Calls, Abandoned Calls, and Overflow Calls

## Short Calls

A short call is a call that is either
                              abandoned very quickly or answered and terminated very quickly. By defining
                              what you believe to be a short call, you can filter out from reporting metrics
                              those calls that did not stay in the system long enough to be considered and
                              counted as events.

The Abandoned Call Wait timer , set at the
                                 peripheral, defines the threshold under which the abandoned call will not be
                              counted. If the abandoned threshold is lower than the service level threshold,
                              the call will not affect the service level. If call wait time is higher than
                              this threshold, the call is counted as Offered.

The Answered Short
                              Call threshold , also set at the peripheral, defines the time under which the
                              call will not be counted as answered and will not impact agent performance.

If you plan to use short calls to filter out false abandons or to
                              detect when calls are answered and terminated too quickly to be considered
                              handled, consider the following:

You can configure abandoned short calls globally for all
                                    call types.

You can configure abandoned short calls for
                                    the peripheral. These calls are tracked for the services that are configured for that
                                    peripheral.

You can choose not to count any abandoned
                                    calls as short calls regardless of how quickly they abandon.

You can choose how abandoned calls affect the service level—negatively,
                                    positively, or not at all.

You can configure
                                    answered short calls for agents
                                    and skill groups.

You cannot configure answered short
                                    calls for call type.

You can choose not to count any
                                    answered calls as short calls regardless of how quickly they
                                    terminate.

To access these short call capabilities, refer to the following section.

### Use Short Calls as Filters and Detection Devices

Perform these general steps:

Access the AW (DataServer).

Go into the Configuration Manager > Tools > Explorer Tools > PG Explorer .

Click Retrieve.

Expand Generic PG .

Click CUCM_PG #.

On the right side of the screen there is a group of tabs.

Peripheral

Advanced

Agent Distribution

Peripheral Monitor

Default route

Routing client

Skill Group Mask

### Abandoned Short Calls

A call is considered abandoned if it abandons after the value set for the Abandon Call Wait time
                                 threshold. This value is set globally.

If the call abandons before the Abandon Call Wait Time threshold, the call is
                                 reported as a short call.

Abandoned short calls affect reporting
                                 because they update the CallsOffered field but not the CallsAbandon field.

### Answered Short Calls

Answered short calls reflect when a caller ends the call quickly if there is no agent on the phone.

Answered short calls are reported for skill
                                 groups and agent skill groups.

The short call timer starts when
                                 the agent answers the call, and the CallsAnswered metric is updated for these
                                 calls.

The ShortCalls fields within the Skill_Group_Interval and
                                 Agent_Skill_Group_Interval tables are incremented if the Talk Time is less than or equal to  the Answered short call threshold
                                 configured for the peripheral. The call is
                                 reported both as handled and as a short call.

If auto-answer is enabled for the agent, and if there are a high number of short calls within a certain interval, you can
                                 use reporting on short calls to determine which agents were not at their stations when a call was automatically answered.
                                 This conclusion assumes that the caller ends the call quickly when there is no agent on the phone.

### Short Call Reports

Several  All
                                 Fields Reports contain a Short Tasks column to enable you to track calls that
                                 are offered but are not handled or abandoned.

The following reports display operational
                                 information on short calls:

Unified Intelligence Center Agent
                                       Historical All Fields Report

Unified Intelligence Center Call Type
                                       Historical All Fields Report

Unified Intelligence Center Agent Skill Group
                                       Historical All Fields

Precision Queue Interval All fields

## Abandoned Calls

A call is considered abandoned if the caller ends the call before being connected to an agent. This includes situations where
                              the caller ends the call while queued and waiting at the VRU ( CVP or IVR) . A high number of abandoned calls might be an indication that callers are waiting in the queue for too long.

Service
                              reports provide cumulative statistics for all abandoned calls. Call type
                              reports provide additional visibility on where calls are abandoning.

### How Abandoned Calls Affect Reporting

There are three types of abandon metrics: abandon at the VRU (prompt
                                 		  or self-service), abandon in queue, and abandon at the agent.

Unified CCE/Unified ICM tracks the abandon counts for each of these abandon types separately. The time these abandoned calls spend before abandoning
                                 is also tracked.

The value represented by the Aban column on the call type reports provides total abandon count for the call type. This value
                                 includes:

Calls that abandoned while at the VRU (prompting or self-service)

Calls that abandon in queue

Calls that abandoned while ringing at the agent's phone or en route to the agent's phone

This value derives from the TotalCallsAband database field.

Reports also provide average time spent by these abandoned calls in
                                 		  the Avg Aban Delay Time field. This field represents the average delay time of
                                 		  all abandoned calls that ended in this call type during the current interval.
                                 		  This value derives from Call_Type_Interval.CallDelayAbandTime /
                                 		  Call_Type_Interval.TotalCallsAband.

To separate information gathering and queuing statistics, you can
                                 		  also determine how much time  a call spends only in the call type where the call
                                 		  abandoned. This value is tracked in the CTDelayTotalAbanTime database field. It
                                 		  includes only the time spent in the call type where the call abandoned and not
                                 		  all call types.

Consider this example:

A call spends 30 seconds in the information gathering call type, "Info_Call_Type" .

The script then changes the call type to the queuing call type—For example,
                                       				Queue_Call_Type. The call is queued.

After 15 seconds waiting in queue, the call is abandoned.

In this case, the total time the call spends before abandoning is 45 seconds. However, the time the call spends in the "Queue_Call_Type" where the call abandoned is15 seconds. The
                                 		  call type statistics for the "Queue_Call_Type" are updated as follows:

Queue_Call_Type

CallDelayAbandTime = 45 seconds

CTDelayTotalAbanTime = 15 seconds.

### How Abandoned Short Calls Affect Reporting

A
                                 short call at the call type is a call that abandons within the call type's
                                 Abandon Wait Time threshold. If you define a short call,
                                 you can filter out calls that you believe did not stay in the system long
                                 enough to count as a real call. You can define short calls for call types
                                 and services.

Short calls are configured globally for all call
                                             types.

The short call timer starts when  the route request is
                                 received for the call. The CallsOffered field is updated when the route request
                                 is received. If the call abandons within the Abandon Wait Time threshold, the
                                 ShortCalls field is updated, but the number of calls abandoned is not updated.
                                 Since the call type is the highest level reporting entity, calls that abandon
                                 at the VRU or at the agent's phone can also be considered short calls at the
                                 call type if they abandon within the call type's Abandon Wait Time threshold.

If you do not want to count any abandoned calls as short calls
                                 regardless of how quickly they abandon, you can disable abandoned short calls
                                 by leaving the Abandon Wait Time field for the call type blank.

### Abandoned Call Reports

The following reports display Abandon statistics for call types and services:

Unified Intelligence Center: Enterprise Service Historical All Fields

Unified Intelligence Center: Peripheral Service Historical All Fields

## Overflow

The software keeps counts of the number of calls moved out of each
                              		  service or route (overflowed out) and moved into each service or route
                              		  (overflowed in).

Overflow Out is incremented when the one of the following occurs:

The call type associated with the current call is changed through
                                    				use of a Call Type or Requalify node.

The call is sent to a label using a label node.

The call is redirected.

When a call is redirected, the PIM no longer can receive events
                                    				for the call and has no way of referencing or tracking the call.

For example, the call might have been redirected to a non- Unified CCE monitored device and then returned to the switch with a different call ID.

The Unified CCE Packaged CCE generates the termination call detail record with only the data originally tracked for the call. Calls marked as Redirected
                                    are counted as Overflow Out calls in the Unified CCE service and route tables.

The call was not default-routed, and the label was not a ring,
                                    				busy, or announcement label.

The call hit a release node

In Unified CCE , to more accurately reflect call status, CallDisposition is set to 15 (Redirected) instead of 4 (Abandon Delay) in the
                              following cases:

When a call leaves a CTI route point to be sent to IVR.

When the agent transfers call to another skill group, no agent is
                                    		  available, and the call is sent to IVR.

### Overflow Reports

The following reports display operational information on Overflow Out situations:

Unified Intelligence Center Call Type Historical /Call Type Daily All Fields

Unified Intelligence Center Call Type Real Time

Unified Intelligence Center Peripheral Service Real Time

| Note | The concept of short calls applies to the
                                       Voice media class only. |
|---|---|

| Note | If a call abandons before the Abandon Call Wait Time threshold, it is
                                       considered a short call. For example, if you configure the abandoned call wait
                                       time for 10 seconds, and a caller disconnects at nine seconds, that call is a
                                       short call—it is not considered offered or abandoned. |
|---|---|

| Note | You could write custom reports to able to report on the different
                                          		  abandons and the time spent by these abandons. To determine the counts and the
                                          		  time associated with the abandoned calls, for calls in the script, or at the
                                          		  VRU (prompt or self-service), subtract Agent Abandons and Queue Abandons from
                                          		  Total Abandons. |
|---|---|

| Note | Short calls are configured globally for all call
                                             types. |
|---|---|