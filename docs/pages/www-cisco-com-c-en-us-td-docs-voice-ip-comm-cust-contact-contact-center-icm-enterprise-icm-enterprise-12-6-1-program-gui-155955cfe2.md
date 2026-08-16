---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-155955cfe2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_ctios-developer-guide_12_6_1/ucce_b_ctios-developer-guide_12_5_chapter_01010.html
retrieved_at: 2026-08-16T20:24:44.913960+00:00
---

CTI OS Developer Guide for Cisco Unified ICM, Release 12.6(1)

# CTI OS Developer Guide for Cisco Unified ICM, Release 12.6(1)

Updated: May 12, 2021

Chapter: SkillGroup Object

## Chapter: SkillGroup Object

# SkillGroup Object

## SkillGroup Object

The SkillGroup object provides developers using the CTI OS Client Interface Library with an interface to Skill Group properties
                              and data. The SkillGroup is mainly a representation used for accessing statistics, which you can enable or disable via method
                              calls to the SkillGroup object. The SkillGroups are accessible directly from the Session object or the Agent object.

The SkillGroup object methods can be accessed as follows:

Via the Agent object inside the Session in Agent mode

Via the Agent object inside the Session in Monitor mode

In C++, Java, and .NET, via the session object inside the session in Monitor mode when the special SkillGroupStats filter
                                    is set.  For more information about code examples related to the special SkillGroupStats filter, see Skill Group Statistics in Chapter 8.

## Properties

The
                              		  following table lists the available SkillGroup properties.

The data type
                                          			 listed for each keyword is the standardized data type discussed in the section CTI OS CIL Data Types in CIL Coding Conventions For more information about the
                                          			 appropriate language specific types for these keywords, see Table 1 .

Keyword

Type

Description

SkillGroupNumber

INT

The
                                          					 optional, user-defined number of the SkillGroup from the Peripheral.

SkillGroupID

STRING

The
                                          					 system-assigned identifier of the SkillGroup, if available.

SkillGroupName

STRING

The Unified
                                          					 ICM SkillGroupName of the SkillGroup, if available.

SkillGroupState

INT

Values
                                          					 representing the current state of the associated agent with respect to the
                                          					 indicated Agent SkillGroup.

ClassIdentifier

INT

Value
                                          					 represents SkillGroup class.

To access
                              		  statistics, first use GetValue on the SkillGroup object to obtain the
                              		  Statistics Arguments array, then use GetValue to obtain the desired value.

Not all the
                                          			 statistics values listed in the above table are present in every system
                                          			 configuration. Whether a particular statistic value is available depends on
                                          			 both the protocol version of CTI Server with which CTI OS connects and on the
                                          			 peripheral on which the agent resides. The statistics listed in Table 1 are available in Protocol Version 8
                                          			 of CTI Server.

One very
                              		  important real-time skillgroup statistic is the number of calls currently in
                              		  queue. Previously, this value was provided in CallsQNow. Now the number of
                              		  calls currently in queue is stored in RouterCallsQNow.

## Statistics

The following table lists the available SkillGroup
                              		  statistics.

Statistic

Definition

AgentsLoggedOn

Number of agents that are currently logged on to the SkillGroup.

AgentsAvail

Number of agents for the SkillGroup in Available state ready
                                          					 to take calls.

AgentsNotReady

Number of agents in the Not Ready state for the SkillGroup.

AgentsReady

Number of agents that are in work state (TALKING, HELD,
                                          					 WORK_READY, AVAILABLE, or RESERVED). This statistic is used by the router to
                                          					 determine the number of working agents in the SkillGroup when estimating the
                                          					 expected delay. It is the difference between AgentsLoggedOn and AgentsNotReady.
                                          					 Reference AgentsAvail to get the number of agents that are available to take
                                          					 calls right now.

AgentsTalkingIn

Number of agents in the SkillGroup currently talking on
                                          					 inbound calls.

AgentsTalkingOut

Number of agents in the SkillGroup currently talking on
                                          					 outbound calls.

AgentsTalkingOther

Number of agents in the SkillGroup currently talking on
                                          					 internal (not inbound or outbound) calls.

AgentsWorkNot Ready

Number of agents in the SkillGroup in the Work Not Ready
                                          					 state.

AgentsWorkReady

Number of agents in the SkillGroup in the Work Ready state.

AgentsBusyOther

Number of agents currently busy with calls assigned to other
                                          					 SkillGroups.

AgentsReserved

Number of agents for the SkillGroup currently in the Reserved
                                          					 state.

AgentsHold

Number of calls to the SkillGroup currently on hold.

AgentsICM Available

Number of agents in the SkillGroup currently in the
                                          					 ICMAvailable state.

AgentsApplication Available

Number of agents in the SkillGroup currently in the
                                          					 Application Available state.

AgentsTalkingAutoOut

Number of calls to the SkillGroup currently talking on
                                          					 AutoOut (predictive) calls.

AgentsTalking Preview

Number of calls to the SkillGroup currently talking on
                                          					 outbound Preview calls.

AgentsTalking Reservation

Number of calls to the SkillGroup currently talking on agent
                                          					 reservation calls.

RouterCallsQNow**

The number of calls currently queued by the CallRouter for this SkillGroup. This field is set
                                          					 to 0xFFFFFFFF when this value is unknown or unavailable.

LongestRouterCallQNow**

The queue time, in seconds, of the currently Unified ICM call router queued call that has been queued to the
                                          					 SkillGroup the longest. This field is set to 0xFFFFFFFF when this value is
                                          					 unknown or unavailable.

CallsQNow*

The number of calls currently queued to the SkillGroup. This
                                          					 field is set to 0xFFFFFFFF when this value is unknown or unavailable.

CallsQTimeNow*

The total queue time, in seconds, of calls currently queued to
                                          					 the SkillGroup. This field is set to 0xFFFFFFFF when this value is unknown or
                                          					 unavailable.

LongestCallQNow*

The queue time, in seconds, of the currently queued call that
                                          					 has been queued to the SkillGroup the longest. This field is set to 0xFFFFFFFF
                                          					 when this value is unknown or unavailable.

AvailTimeTo5

Total seconds agents in the SkillGroup were in the Available
                                          					 state.

LoggedOnTimeTo5

Total time, in seconds, agents in the SkillGroup were logged
                                          					 in.

NotReadyTimeTo5

Total seconds agents in the SkillGroup were in the Not Ready
                                          					 state.

AgentOutCallsTo5

Total number of completed outbound ACD calls made by agents in
                                          					 the SkillGroup.

AgentOutCallsTalk TimeTo5

Total talk time, in seconds, for completed outbound ACD calls
                                          					 handled by agents in the SkillGroup. The value includes the time spent from
                                          					 the call being initiated by the agent to the time the agent begins after call
                                          					 work for the call. The time includes hold time associated with the call.

AgentOutCallsTimeTo5

Total handle time, in seconds, for completed outbound ACD
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated by the agent to the time the agent completes
                                          					 after call work time for the call. The time includes hold time associated with
                                          					 the call.

AgentOutCallsHeldTo5

The total number of completed outbound ACD calls agents in the
                                          					 SkillGroup have placed on hold at least once.

AgentOutCallsHeldTimeTo5

Total number of seconds outbound ACD calls were placed on hold
                                          					 by agents in the SkillGroup.

HandledCallsTo5

The number of inbound ACD calls handled by agents in the SkillGroup.

HandledCallsTalk TimeTo5

Total talk time in seconds for Inbound ACD calls counted as
                                          					 handled by agents in the SkillGroup. Includes hold time associated with the
                                          					 call.

HandledCallsAfter CallTimeTo5

Total after call work time in seconds for Inbound ACD calls
                                          					 counted as handled by agents in the SkillGroup.

HandledCallsTime To5

Total handle time, in seconds, for inbound ACD calls counted
                                          					 as handled by agents in the SkillGroup. The time spent from the call being
                                          					 answered by the agent to the time the agent completed after call work time for
                                          					 the call. Includes hold time associated with the call.

IncomingCallsHeldTo5

The total number of completed inbound ACD calls agents in the
                                          					 SkillGroup placed on hold at least once.

IncomingCallsHeldTimeTo5

Total number of seconds completed inbound ACD calls were
                                          					 placed on hold by agents in the SkillGroup.

InternalCallsRcvdTo5

Number of internal calls received by agents in the SkillGroup.

InternalCallsRcvd TimeTo5

Number of seconds spent on internal calls received by agents
                                          					 in the SkillGroup.

InternalCallsHeldTo5

The total number of internal calls agents in the SkillGroup
                                          					 placed on hold at least once.

InternalCallsHeld TimeTo5

Total number of seconds completed internal calls were placed
                                          					 on hold by agents in the SkillGroup.

AutoOutCallsTo5

Total number of AutoOut (predictive) calls completed by agents
                                          					 in the SkillGroup.

AutoOutCallsTalk TimeTo5

Total talk time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent begins after
                                          					 call work for the call. The time includes hold time associated with the call.

AutoOutCallsTime To5

Total handle time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent completes after
                                          					 call work time for the call. The time includes hold time associated with the
                                          					 call.

AutoOutCallsHeld To5

The total number of completed AutoOut (predictive) calls that
                                          					 agents in the SkillGroup have placed on hold at least once.

AutoOutCallsHeld TimeTo5

Total number of seconds AutoOut (predictive) calls were placed
                                          					 on hold by agents in the SkillGroup.

PreviewCallsTo5

Total number of outbound Preview calls completed by agents in
                                          					 the SkillGroup.

PreviewCallsTalk TimeTo5

Total talk time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call.

PreviewCallsTime To5

Total handle time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call.

PreviewCallsHeld To5

The total number of completed outbound Preview calls that
                                          					 agents in the SkillGroup have placed on hold at least once.

PreviewCallsHeld TimeTo5

Total number of seconds outbound Preview calls were placed on
                                          					 hold by agents in the SkillGroup.

ReservationCallsTo5

Total number of agent reservation calls completed by agents in
                                          					 the SkillGroup.

ReservationCalls TalkTimeTo5

Total talk time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call.

ReservationCalls TimeTo5

Total handle time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call.

ReservationCalls HeldTo5

The total number of agent reservation calls that agents in the
                                          					 SkillGroup have placed on hold at least once.

ReservationCalls HeldTimeTo5

Total number of seconds agent reservation calls were placed on
                                          					 hold by agents in the SkillGroup.

BargeInCallsTo5

Total number of supervisor call barge-ins completed in the
                                          					 SkillGroup.

InterceptCallsTo5

Total number of supervisor call intercepts completed in the
                                          					 SkillGroup.

MonitorCallsTo5

Total number of supervisor call monitors completed in the
                                          					 SkillGroup.

WhisperCallsTo5

Total number of supervisor call whispers completed by agents
                                          					 in the SkillGroup.

EmergencyCallsTo5

Total number of emergency calls completed by agents in the
                                          					 SkillGroup.

CallsQ5*

The number of calls queued to the SkillGroup during the
                                          					 current five-minute. This field is set to 0xFFFFFFFF when this value is unknown
                                          					 or unavailable.

CallsQTime5*

The total queue time, in seconds, of calls queued to the SkillGroup during the current five-minute. This field is set to 0xFFFFFFFF
                                          when this
                                          					 value is unknown or unavailable.

LongestCallQ5*

The longest queue time, in seconds, of all calls queued to the
                                          					 SkillGroup during the current five-minute. This field is set to 0xFFFFFFFF
                                          					 when this value is unknown or unavailable.

AvailTimeToHalf

Total seconds agents in the SkillGroup were in the Available
                                          					 state.

LoggedOnTime ToHalf

Total time, in seconds, agents in the SkillGroup were logged
                                          					 in.

NotReadyTime ToHalf

Total seconds agents in the SkillGroup were in the Not Ready
                                          					 state.

AgentOutCallsTo Half

Total number of completed outbound ACD calls made by agents in
                                          					 the SkillGroup.

AgentOutCallsTalk TimeToHalf

Total talk time, in seconds, for completed outbound ACD calls
                                          					 handled by agents in the SkillGroup. The value includes the time spent from
                                          					 the call being initiated by the agent to the time the agent begins after call
                                          					 work for the call. The time includes hold time associated with the call.

AgentOutCallsTimeToHalf

Total handle time, in seconds, for completed outbound ACD
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated by the agent to the time the agent completes
                                          					 after call work time for the call. The time includes hold time associated with
                                          					 the call.

AgentOutCallsHeldToHalf

The total number of completed outbound ACD calls agents in the
                                          					 SkillGroup have placed on hold at least once.

AgentOutCallsHeldTimeToHalf

Total number of seconds outbound ACD calls were placed on hold
                                          					 by agents in the SkillGroup.

HandledCallsToHalf

The number of inbound ACD calls handled by agents in the SkillGroup.

HandledCallsTalk TimeToHalf

Total talk time in seconds for Inbound ACD calls counted as
                                          					 handled by agents in the SkillGroup. Includes hold time associated with the
                                          					 call.

HandledCallsAfter CallTimeToHalf

Total after call work time in seconds for Inbound ACD calls
                                          					 counted as handled by agents in the SkillGroup.

HandledCallsTime ToHalf

Total handle time, in seconds, for inbound ACD calls counted
                                          					 as handled by agents in the SkillGroup. The time spent from the call being
                                          					 answered by the agent to the time the agent completed after call work time for
                                          					 the call. Includes hold time associated with the call.

IncomingCallsHeldToHalf

The total number of completed inbound ACD calls agents in the
                                          					 SkillGroup placed on hold at least once.

IncomingCallsHeldTimeToHalf

Total number of seconds completed inbound ACD calls were
                                          					 placed on hold by agents in the SkillGroup.

InternalCallsRcvdToHalf

Number of internal calls received by agents in the SkillGroup.

InternalCallsRcvd TimeToHalf

Number of seconds spent on internal calls received by agents
                                          					 in the SkillGroup.

InternalCallsHeldToHalf

The total number of internal calls agents in the SkillGroup
                                          					 placed on hold at least once.

InternalCallsHeld TimeToHalf

Total number of seconds completed internal calls were placed
                                          					 on hold by agents in the SkillGroup.

AutoOutCallsToHalf

Total number of AutoOut (predictive) calls completed by agents
                                          					 in the SkillGroup.

AutoOutCallsTalk TimeToHalf

Total talk time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent begins after
                                          					 call work for the call. The time includes hold time associated with the call.

AutoOutCallsTime ToHalf

Total handle time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent completes after
                                          					 call work time for the call. The time includes hold time associated with the
                                          					 call.

AutoOutCallsHeld ToHalf

The total number of completed AutoOut (predictive) calls that
                                          					 agents in the SkillGroup have placed on hold at least once.

AutoOutCallsHeld TimeToHalf

Total number of seconds AutoOut (predictive) calls were placed
                                          					 on hold by agents in the SkillGroup.

PreviewCallsToHalf

Total number of outbound Preview calls completed by agents in
                                          					 the SkillGroup.

PreviewCallsTalk TimeToHalf

Total talk time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call.

PreviewCallsTime ToHalf

Total handle time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call.

PreviewCallsHeldToHalf

The total number of completed outbound Preview calls that
                                          					 agents in the SkillGroup have placed on hold at least once.

PreviewCallsHeld TimeToHalf

Total number of seconds outbound Preview calls were placed on
                                          					 hold by agents in the SkillGroup.

ReservationCallsToHalf

Total number of agent reservation calls completed by agents in
                                          					 the SkillGroup.

ReservationCalls TalkTimeToHalf

Total talk time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call.

ReservationCalls TimeToHalf

Total handle time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call.

ReservationCalls HeldToHalf

The total number of agent reservation calls that agents in the
                                          					 SkillGroup have placed on hold at least once.

ReservationCalls HeldTimeToHalf

Total number of seconds agent reservation calls were placed on
                                          					 hold by agents in the SkillGroup.

BargeInCallsToHalf

Total number of supervisor call barge-ins completed in the
                                          					 SkillGroup.

InterceptCallsTo Half

Total number of supervisor call intercepts completed in the
                                          					 SkillGroup.

MonitorCallsToHalf

Total number of supervisor call monitors completed in the
                                          					 SkillGroup.

WhisperCallsToHalf

Total number of supervisor call whispers completed by agents
                                          					 in the SkillGroup.

EmergencyCalls ToHalf

Total number of emergency calls completed by agents in the
                                          					 SkillGroup.

CallsQHalf*

The number of calls queued to the SkillGroup during the
                                          					 current half hour. This field is set to 0xFFFFFFFF when this value is unknown
                                          					 or unavailable.

CallsQTimeHalf*

The total queue time, in seconds, of calls queued to the SkillGroup during the current half hour. This field is set to 0xFFFFFFFF
                                          when this
                                          					 value is unknown or unavailable.

LongestCallQHalf*

The longest queue time, in seconds, of all calls queued to the
                                          					 SkillGroup during the current half hour. This field is set to 0xFFFFFFFF when
                                          					 this value is unknown or unavailable.

AvailTimeToday

Total seconds agents in the SkillGroup were in the Available
                                          					 state.

LoggedOnTime Today

Total time, in seconds, agents in the SkillGroup were logged
                                          					 in.

NotReadyTime Today

Total seconds agents in the SkillGroup were in the Not Ready
                                          					 state.

AgentOutCalls Today

Total number of completed outbound ACD calls made by agents in
                                          					 the SkillGroup.

AgentOutCallsTalk TimeToday

Total talk time, in seconds, for completed outbound ACD calls
                                          					 handled by agents in the SkillGroup. The value includes the time spent from
                                          					 the call being initiated by the agent to the time the agent begins after call
                                          					 work for the call. The time includes hold time associated with the call.

AgentOutCallsTimeToday

Total handle time, in seconds, for completed outbound ACD
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated by the agent to the time the agent completes
                                          					 after call work time for the call. The time includes hold time associated with
                                          					 the call.

AgentOutCallsHeldToday

The total number of completed outbound ACD calls agents in the
                                          					 SkillGroup have placed on hold at least once.

AgentOutCallsHeldTimeToday

Total number of seconds outbound ACD calls were placed on hold
                                          					 by agents in the SkillGroup.

HandledCallsToday

The number of inbound ACD calls handled by agents in the SkillGroup.

HandledCallsTalk TimeToday

Total talk time in seconds for Inbound ACD calls counted as
                                          					 handled by agents in the SkillGroup. Includes hold time associated with the
                                          					 call.

HandledCallsAfter CallTimeToday

Total after call work time in seconds for Inbound ACD calls
                                          					 counted as handled by agents in the SkillGroup.

HandledCallsTime Today

Total handle time, in seconds, for inbound ACD calls counted
                                          					 as handled by agents in the SkillGroup. The time spent from the call being
                                          					 answered by the agent to the time the agent completed after call work time for
                                          					 the call. Includes hold time associated with the call.

IncomingCallsHeldToday

The total number of completed inbound ACD calls agents in the
                                          					 SkillGroup placed on hold at least once.

IncomingCallsHeldTimeToday

Total number of seconds completed inbound ACD calls were
                                          					 placed on hold by agents in the SkillGroup.

InternalCallsRcvd Today

Number of internal calls received by agents in the SkillGroup.

InternalCallsRcvd TimeToday

Number of seconds spent on internal calls received by agents
                                          					 in the SkillGroup.

InternalCallsHeld Today

The total number of internal calls agents in the SkillGroup
                                          					 placed on hold at least once.

InternalCallsHeld TimeToday

Total number of seconds completed internal calls were placed
                                          					 on hold by agents in the SkillGroup.

AutoOutCallsToday

Total number of AutoOut (predictive) calls completed by agents
                                          					 in the SkillGroup.

AutoOutCallsTalk TimeToday

Total talk time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent begins after
                                          					 call work for the call. The time includes hold time associated with the call.

AutoOutCallsTime Today

Total handle time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent completes after
                                          					 call work time for the call. The time includes hold time associated with the
                                          					 call.

AutoOutCallsHeld Today

The total number of completed AutoOut (predictive) calls that
                                          					 agents in the SkillGroup have placed on hold at least once.

AutoOutCallsHeld TimeToday

Total number of seconds AutoOut (predictive) calls were placed
                                          					 on hold by agents in the SkillGroup.

PreviewCallsToday

Total number of outbound Preview calls completed by agents in
                                          					 the SkillGroup.

PreviewCallsTalk TimeToday

Total talk time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call.

PreviewCallsTime Today

Total handle time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call.

PreviewCallsHeld Today

The total number of completed outbound Preview calls that
                                          					 agents in the SkillGroup have placed on hold at least once.

PreviewCallsHeld TimeToday

Total number of seconds outbound Preview calls were placed on
                                          					 hold by agents in the SkillGroup.

ReservationCalls Today

Total number of agent reservation calls completed by agents in
                                          					 the SkillGroup.

ReservationCalls TalkTimeToday

Total talk time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call.

ReservationCalls TimeToday

Total handle time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call.

ReservationCalls HeldToday

The total number of agent reservation calls that agents in the
                                          					 SkillGroup have placed on hold at least once.

ReservationCalls HeldTimeToday

Total number of seconds agent reservation calls were placed on
                                          					 hold by agents in the SkillGroup.

BargeInCallsToday

Total number of supervisor call barge-ins completed in the
                                          					 SkillGroup.

InterceptCallsToday

Total number of supervisor call intercepts completed in the
                                          					 SkillGroup.

MonitorCallsToday

Total number of supervisor call monitors completed in the
                                          					 SkillGroup.

WhisperCallsToday

Total number of supervisor call whispers completed by agents
                                          					 in the SkillGroup.

EmergencyCalls Today

Total number of emergency calls completed by agents in the
                                          					 SkillGroup.

CallsQToday*

The number of calls queued to the skill. This field is set to
                                          					 0xFFFFFFFF when this value is unknown or unavailable.

CallsQTimeToday*

The total queue time, in seconds, of calls queued to the SkillGroup. This field is set to 0xFFFFFFFF when this value is unknown
                                          or
                                          					 unavailable.

LongestCallQToday*

The longest queue time, in seconds, of all calls queued to the
                                          					 SkillGroup. This field is set to 0xFFFFFFFF when this value is unknown or
                                          					 unavailable.

* This statistic is available for TDM switches only. It is
                              		  not valid for Unified CCE.

** This statistic is available for Unified CCE only or
                              		  Network Queuing.

## Methods

The following table lists the SkillGroup object methods.

Method

Description

GroupStatistics

Disables SkillGroup statistic messages.

DumpProperties

For more information, see CtiOs Object

EnableSkillGroupStatistics

Enables SkillGroup statistic messages.

GetElement

For more information, see CtiOs Object

GetNumProperties

For more information, see CtiOs Object

GetPropertyName

For more information, see CtiOs Object

GetValue

For more information, see CtiOs Object

GetValueInt (C++)

GetValueIntObj (Java)

For more information, see CtiOs Object

GetValueString

For more information, see CtiOs Object

IsValid

For more information, see CtiOs Object

SetValue

For more information, see CtiOs Object

### DisableSkillGroupStatistics

The DisableSkillGroupStatistics method requests that
                                 		  real-time statistics stop being sent to the SkillGroup object.

#### Syntax

#### Parameters

If this method is called in C++, Java, or .NET via the session object
                                       		  in monitor mode with the special SkillGroupStats filter, the args parameter has
                                       		  two required values for PeripheralId and SkillGroupNumber. For more information about a code example, see the Remarks
                                       		  section. Otherwise, this parameter is not used.

An output parameter (return parameter in VB) that contains an error
                                       		  code, if any.

#### Return Value

Default CTI OS return values. For more information, see CIL Coding Conventions .

#### Remarks

The CTI OS server sends SkillGroup statistics in an
                                 		  OnSkillGroupStatisticsUpdated event. If this request is successful, the
                                 		  OnNewSkillGroupStatistics event is no longer received.

The following is a C++ code example where the args parameter
                                 		  contains values for PeripheralID and SkillGroupNumber.

```
Arguments & argsStatBroadcast = Arguments::CreateInstance();
argsStatBroadcast.AddItem(CTIOS_SkillGroupNUMBER, intSG);
argsStatBroadcast.AddItem(CTIOS_PERIPHERALID, m_periphID);
m_pSkGrStatSession->DisableSkillGroupStatistics ( argsStatBroadcast );
argsStatBroadcast.Release();
```

### DumpProperties

For more information about the DumpProperties method, see CtiOs Object .

### EnableSkillGroupStatistics

The EnableSkillGroupStatistics method requests that
                                 		  real-time statistics be sent to the SkillGroup object. In an agent mode
                                 		  application, this request is usually made through the Agent object (see Call Object ). If the argument array
                                 		  is empty, then statistics for all SkillGroups are enabled. This is useful when
                                 		  a monitoring application needs to view all statistics without having to
                                 		  enumerate and loop over each statistic to enable it.

#### Syntax

#### Parameters

If this method is called via the session object in monitor mode with
                                       		  the special SkillGroupStats filter, the args parameter has two required values
                                       		  for PeripheralId and SkillGroupNumber. For more information about a code
                                       		  example, see the Remarks section. Otherwise, this parameter is not used.

An output parameter (return parameter in VB) that contains an error
                                       		  code, if any.

#### Return Value

Default CTI OS return values. For more information, see CIL Coding Conventions .

#### Remarks

CTI OS Server sends SkillGroup statistics in an
                                 		  OnSkillGroupStatisticsUpdated event.

The following is a C++ code example where the args parameter
                                 		  contains values for PeripheralID and SkillGroupNumber.

```
Arguments & argsStatBroadcast = Arguments::CreateInstance();
argsStatBroadcast.AddItem(CTIOS_SkillGroupNUMBER, intSG);
argsStatBroadcast.AddItem(CTIOS_PERIPHERALID, m_periphID);
m_pSkGrStatSession-> EnableSkillGroupStatistics ( argsStatBroadcast );
argsStatBroadcast.Release();
```

### GetElement

For more information about the GetElement method, see CtiOs Object .

### GetValue Methods

For more information about the GetValue, GetValueInt, GetValueList, and GetValueString methods, see CtiOs Object .

### IsValid

For more information about the IsValid method, see CtiOs Object .

### SetValue

For more information about the SetValue method, see CtiOs Object .

| Note | The data type
                                          			 listed for each keyword is the standardized data type discussed in the section CTI OS CIL Data Types in CIL Coding Conventions For more information about the
                                          			 appropriate language specific types for these keywords, see Table 1 . |
|---|---|

| Keyword | Type | Description |
|---|---|---|
| SkillGroupNumber | INT | The
                                          					 optional, user-defined number of the SkillGroup from the Peripheral. |
| SkillGroupID | STRING | The
                                          					 system-assigned identifier of the SkillGroup, if available. |
| SkillGroupName | STRING | The Unified
                                          					 ICM SkillGroupName of the SkillGroup, if available. |
| SkillGroupState | INT | Values
                                          					 representing the current state of the associated agent with respect to the
                                          					 indicated Agent SkillGroup. |
| ClassIdentifier | INT | Value
                                          					 represents SkillGroup class. |

| Note | Not all the
                                          			 statistics values listed in the above table are present in every system
                                          			 configuration. Whether a particular statistic value is available depends on
                                          			 both the protocol version of CTI Server with which CTI OS connects and on the
                                          			 peripheral on which the agent resides. The statistics listed in Table 1 are available in Protocol Version 8
                                          			 of CTI Server. |
|---|---|

| Statistic | Definition |
|---|---|
| AgentsLoggedOn | Number of agents that are currently logged on to the SkillGroup. |
| AgentsAvail | Number of agents for the SkillGroup in Available state ready
                                          					 to take calls. |
| AgentsNotReady | Number of agents in the Not Ready state for the SkillGroup. |
| AgentsReady | Number of agents that are in work state (TALKING, HELD,
                                          					 WORK_READY, AVAILABLE, or RESERVED). This statistic is used by the router to
                                          					 determine the number of working agents in the SkillGroup when estimating the
                                          					 expected delay. It is the difference between AgentsLoggedOn and AgentsNotReady.
                                          					 Reference AgentsAvail to get the number of agents that are available to take
                                          					 calls right now. |
| AgentsTalkingIn | Number of agents in the SkillGroup currently talking on
                                          					 inbound calls. |
| AgentsTalkingOut | Number of agents in the SkillGroup currently talking on
                                          					 outbound calls. |
| AgentsTalkingOther | Number of agents in the SkillGroup currently talking on
                                          					 internal (not inbound or outbound) calls. |
| AgentsWorkNot Ready | Number of agents in the SkillGroup in the Work Not Ready
                                          					 state. |
| AgentsWorkReady | Number of agents in the SkillGroup in the Work Ready state. |
| AgentsBusyOther | Number of agents currently busy with calls assigned to other
                                          					 SkillGroups. |
| AgentsReserved | Number of agents for the SkillGroup currently in the Reserved
                                          					 state. |
| AgentsHold | Number of calls to the SkillGroup currently on hold. |
| AgentsICM Available | Number of agents in the SkillGroup currently in the
                                          					 ICMAvailable state. |
| AgentsApplication Available | Number of agents in the SkillGroup currently in the
                                          					 Application Available state. |
| AgentsTalkingAutoOut | Number of calls to the SkillGroup currently talking on
                                          					 AutoOut (predictive) calls. |
| AgentsTalking Preview | Number of calls to the SkillGroup currently talking on
                                          					 outbound Preview calls. |
| AgentsTalking Reservation | Number of calls to the SkillGroup currently talking on agent
                                          					 reservation calls. |
| RouterCallsQNow** | The number of calls currently queued by the CallRouter for this SkillGroup. This field is set
                                          					 to 0xFFFFFFFF when this value is unknown or unavailable. |
| LongestRouterCallQNow** | The queue time, in seconds, of the currently Unified ICM call router queued call that has been queued to the
                                          					 SkillGroup the longest. This field is set to 0xFFFFFFFF when this value is
                                          					 unknown or unavailable. |
| CallsQNow* | The number of calls currently queued to the SkillGroup. This
                                          					 field is set to 0xFFFFFFFF when this value is unknown or unavailable. |
| CallsQTimeNow* | The total queue time, in seconds, of calls currently queued to
                                          					 the SkillGroup. This field is set to 0xFFFFFFFF when this value is unknown or
                                          					 unavailable. |
| LongestCallQNow* | The queue time, in seconds, of the currently queued call that
                                          					 has been queued to the SkillGroup the longest. This field is set to 0xFFFFFFFF
                                          					 when this value is unknown or unavailable. |
| AvailTimeTo5 | Total seconds agents in the SkillGroup were in the Available
                                          					 state. |
| LoggedOnTimeTo5 | Total time, in seconds, agents in the SkillGroup were logged
                                          					 in. |
| NotReadyTimeTo5 | Total seconds agents in the SkillGroup were in the Not Ready
                                          					 state. |
| AgentOutCallsTo5 | Total number of completed outbound ACD calls made by agents in
                                          					 the SkillGroup. |
| AgentOutCallsTalk TimeTo5 | Total talk time, in seconds, for completed outbound ACD calls
                                          					 handled by agents in the SkillGroup. The value includes the time spent from
                                          					 the call being initiated by the agent to the time the agent begins after call
                                          					 work for the call. The time includes hold time associated with the call. |
| AgentOutCallsTimeTo5 | Total handle time, in seconds, for completed outbound ACD
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated by the agent to the time the agent completes
                                          					 after call work time for the call. The time includes hold time associated with
                                          					 the call. |
| AgentOutCallsHeldTo5 | The total number of completed outbound ACD calls agents in the
                                          					 SkillGroup have placed on hold at least once. |
| AgentOutCallsHeldTimeTo5 | Total number of seconds outbound ACD calls were placed on hold
                                          					 by agents in the SkillGroup. |
| HandledCallsTo5 | The number of inbound ACD calls handled by agents in the SkillGroup. |
| HandledCallsTalk TimeTo5 | Total talk time in seconds for Inbound ACD calls counted as
                                          					 handled by agents in the SkillGroup. Includes hold time associated with the
                                          					 call. |
| HandledCallsAfter CallTimeTo5 | Total after call work time in seconds for Inbound ACD calls
                                          					 counted as handled by agents in the SkillGroup. |
| HandledCallsTime To5 | Total handle time, in seconds, for inbound ACD calls counted
                                          					 as handled by agents in the SkillGroup. The time spent from the call being
                                          					 answered by the agent to the time the agent completed after call work time for
                                          					 the call. Includes hold time associated with the call. |
| IncomingCallsHeldTo5 | The total number of completed inbound ACD calls agents in the
                                          					 SkillGroup placed on hold at least once. |
| IncomingCallsHeldTimeTo5 | Total number of seconds completed inbound ACD calls were
                                          					 placed on hold by agents in the SkillGroup. |
| InternalCallsRcvdTo5 | Number of internal calls received by agents in the SkillGroup. |
| InternalCallsRcvd TimeTo5 | Number of seconds spent on internal calls received by agents
                                          					 in the SkillGroup. |
| InternalCallsHeldTo5 | The total number of internal calls agents in the SkillGroup
                                          					 placed on hold at least once. |
| InternalCallsHeld TimeTo5 | Total number of seconds completed internal calls were placed
                                          					 on hold by agents in the SkillGroup. |
| AutoOutCallsTo5 | Total number of AutoOut (predictive) calls completed by agents
                                          					 in the SkillGroup. |
| AutoOutCallsTalk TimeTo5 | Total talk time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent begins after
                                          					 call work for the call. The time includes hold time associated with the call. |
| AutoOutCallsTime To5 | Total handle time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent completes after
                                          					 call work time for the call. The time includes hold time associated with the
                                          					 call. |
| AutoOutCallsHeld To5 | The total number of completed AutoOut (predictive) calls that
                                          					 agents in the SkillGroup have placed on hold at least once. |
| AutoOutCallsHeld TimeTo5 | Total number of seconds AutoOut (predictive) calls were placed
                                          					 on hold by agents in the SkillGroup. |
| PreviewCallsTo5 | Total number of outbound Preview calls completed by agents in
                                          					 the SkillGroup. |
| PreviewCallsTalk TimeTo5 | Total talk time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call. |
| PreviewCallsTime To5 | Total handle time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call. |
| PreviewCallsHeld To5 | The total number of completed outbound Preview calls that
                                          					 agents in the SkillGroup have placed on hold at least once. |
| PreviewCallsHeld TimeTo5 | Total number of seconds outbound Preview calls were placed on
                                          					 hold by agents in the SkillGroup. |
| ReservationCallsTo5 | Total number of agent reservation calls completed by agents in
                                          					 the SkillGroup. |
| ReservationCalls TalkTimeTo5 | Total talk time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call. |
| ReservationCalls TimeTo5 | Total handle time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call. |
| ReservationCalls HeldTo5 | The total number of agent reservation calls that agents in the
                                          					 SkillGroup have placed on hold at least once. |
| ReservationCalls HeldTimeTo5 | Total number of seconds agent reservation calls were placed on
                                          					 hold by agents in the SkillGroup. |
| BargeInCallsTo5 | Total number of supervisor call barge-ins completed in the
                                          					 SkillGroup. |
| InterceptCallsTo5 | Total number of supervisor call intercepts completed in the
                                          					 SkillGroup. |
| MonitorCallsTo5 | Total number of supervisor call monitors completed in the
                                          					 SkillGroup. |
| WhisperCallsTo5 | Total number of supervisor call whispers completed by agents
                                          					 in the SkillGroup. |
| EmergencyCallsTo5 | Total number of emergency calls completed by agents in the
                                          					 SkillGroup. |
| CallsQ5* | The number of calls queued to the SkillGroup during the
                                          					 current five-minute. This field is set to 0xFFFFFFFF when this value is unknown
                                          					 or unavailable. |
| CallsQTime5* | The total queue time, in seconds, of calls queued to the SkillGroup during the current five-minute. This field is set to 0xFFFFFFFF
                                          when this
                                          					 value is unknown or unavailable. |
| LongestCallQ5* | The longest queue time, in seconds, of all calls queued to the
                                          					 SkillGroup during the current five-minute. This field is set to 0xFFFFFFFF
                                          					 when this value is unknown or unavailable. |
| AvailTimeToHalf | Total seconds agents in the SkillGroup were in the Available
                                          					 state. |
| LoggedOnTime ToHalf | Total time, in seconds, agents in the SkillGroup were logged
                                          					 in. |
| NotReadyTime ToHalf | Total seconds agents in the SkillGroup were in the Not Ready
                                          					 state. |
| AgentOutCallsTo Half | Total number of completed outbound ACD calls made by agents in
                                          					 the SkillGroup. |
| AgentOutCallsTalk TimeToHalf | Total talk time, in seconds, for completed outbound ACD calls
                                          					 handled by agents in the SkillGroup. The value includes the time spent from
                                          					 the call being initiated by the agent to the time the agent begins after call
                                          					 work for the call. The time includes hold time associated with the call. |
| AgentOutCallsTimeToHalf | Total handle time, in seconds, for completed outbound ACD
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated by the agent to the time the agent completes
                                          					 after call work time for the call. The time includes hold time associated with
                                          					 the call. |
| AgentOutCallsHeldToHalf | The total number of completed outbound ACD calls agents in the
                                          					 SkillGroup have placed on hold at least once. |
| AgentOutCallsHeldTimeToHalf | Total number of seconds outbound ACD calls were placed on hold
                                          					 by agents in the SkillGroup. |
| HandledCallsToHalf | The number of inbound ACD calls handled by agents in the SkillGroup. |
| HandledCallsTalk TimeToHalf | Total talk time in seconds for Inbound ACD calls counted as
                                          					 handled by agents in the SkillGroup. Includes hold time associated with the
                                          					 call. |
| HandledCallsAfter CallTimeToHalf | Total after call work time in seconds for Inbound ACD calls
                                          					 counted as handled by agents in the SkillGroup. |
| HandledCallsTime ToHalf | Total handle time, in seconds, for inbound ACD calls counted
                                          					 as handled by agents in the SkillGroup. The time spent from the call being
                                          					 answered by the agent to the time the agent completed after call work time for
                                          					 the call. Includes hold time associated with the call. |
| IncomingCallsHeldToHalf | The total number of completed inbound ACD calls agents in the
                                          					 SkillGroup placed on hold at least once. |
| IncomingCallsHeldTimeToHalf | Total number of seconds completed inbound ACD calls were
                                          					 placed on hold by agents in the SkillGroup. |
| InternalCallsRcvdToHalf | Number of internal calls received by agents in the SkillGroup. |
| InternalCallsRcvd TimeToHalf | Number of seconds spent on internal calls received by agents
                                          					 in the SkillGroup. |
| InternalCallsHeldToHalf | The total number of internal calls agents in the SkillGroup
                                          					 placed on hold at least once. |
| InternalCallsHeld TimeToHalf | Total number of seconds completed internal calls were placed
                                          					 on hold by agents in the SkillGroup. |
| AutoOutCallsToHalf | Total number of AutoOut (predictive) calls completed by agents
                                          					 in the SkillGroup. |
| AutoOutCallsTalk TimeToHalf | Total talk time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent begins after
                                          					 call work for the call. The time includes hold time associated with the call. |
| AutoOutCallsTime ToHalf | Total handle time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent completes after
                                          					 call work time for the call. The time includes hold time associated with the
                                          					 call. |
| AutoOutCallsHeld ToHalf | The total number of completed AutoOut (predictive) calls that
                                          					 agents in the SkillGroup have placed on hold at least once. |
| AutoOutCallsHeld TimeToHalf | Total number of seconds AutoOut (predictive) calls were placed
                                          					 on hold by agents in the SkillGroup. |
| PreviewCallsToHalf | Total number of outbound Preview calls completed by agents in
                                          					 the SkillGroup. |
| PreviewCallsTalk TimeToHalf | Total talk time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call. |
| PreviewCallsTime ToHalf | Total handle time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call. |
| PreviewCallsHeldToHalf | The total number of completed outbound Preview calls that
                                          					 agents in the SkillGroup have placed on hold at least once. |
| PreviewCallsHeld TimeToHalf | Total number of seconds outbound Preview calls were placed on
                                          					 hold by agents in the SkillGroup. |
| ReservationCallsToHalf | Total number of agent reservation calls completed by agents in
                                          					 the SkillGroup. |
| ReservationCalls TalkTimeToHalf | Total talk time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call. |
| ReservationCalls TimeToHalf | Total handle time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call. |
| ReservationCalls HeldToHalf | The total number of agent reservation calls that agents in the
                                          					 SkillGroup have placed on hold at least once. |
| ReservationCalls HeldTimeToHalf | Total number of seconds agent reservation calls were placed on
                                          					 hold by agents in the SkillGroup. |
| BargeInCallsToHalf | Total number of supervisor call barge-ins completed in the
                                          					 SkillGroup. |
| InterceptCallsTo Half | Total number of supervisor call intercepts completed in the
                                          					 SkillGroup. |
| MonitorCallsToHalf | Total number of supervisor call monitors completed in the
                                          					 SkillGroup. |
| WhisperCallsToHalf | Total number of supervisor call whispers completed by agents
                                          					 in the SkillGroup. |
| EmergencyCalls ToHalf | Total number of emergency calls completed by agents in the
                                          					 SkillGroup. |
| CallsQHalf* | The number of calls queued to the SkillGroup during the
                                          					 current half hour. This field is set to 0xFFFFFFFF when this value is unknown
                                          					 or unavailable. |
| CallsQTimeHalf* | The total queue time, in seconds, of calls queued to the SkillGroup during the current half hour. This field is set to 0xFFFFFFFF
                                          when this
                                          					 value is unknown or unavailable. |
| LongestCallQHalf* | The longest queue time, in seconds, of all calls queued to the
                                          					 SkillGroup during the current half hour. This field is set to 0xFFFFFFFF when
                                          					 this value is unknown or unavailable. |
| AvailTimeToday | Total seconds agents in the SkillGroup were in the Available
                                          					 state. |
| LoggedOnTime Today | Total time, in seconds, agents in the SkillGroup were logged
                                          					 in. |
| NotReadyTime Today | Total seconds agents in the SkillGroup were in the Not Ready
                                          					 state. |
| AgentOutCalls Today | Total number of completed outbound ACD calls made by agents in
                                          					 the SkillGroup. |
| AgentOutCallsTalk TimeToday | Total talk time, in seconds, for completed outbound ACD calls
                                          					 handled by agents in the SkillGroup. The value includes the time spent from
                                          					 the call being initiated by the agent to the time the agent begins after call
                                          					 work for the call. The time includes hold time associated with the call. |
| AgentOutCallsTimeToday | Total handle time, in seconds, for completed outbound ACD
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated by the agent to the time the agent completes
                                          					 after call work time for the call. The time includes hold time associated with
                                          					 the call. |
| AgentOutCallsHeldToday | The total number of completed outbound ACD calls agents in the
                                          					 SkillGroup have placed on hold at least once. |
| AgentOutCallsHeldTimeToday | Total number of seconds outbound ACD calls were placed on hold
                                          					 by agents in the SkillGroup. |
| HandledCallsToday | The number of inbound ACD calls handled by agents in the SkillGroup. |
| HandledCallsTalk TimeToday | Total talk time in seconds for Inbound ACD calls counted as
                                          					 handled by agents in the SkillGroup. Includes hold time associated with the
                                          					 call. |
| HandledCallsAfter CallTimeToday | Total after call work time in seconds for Inbound ACD calls
                                          					 counted as handled by agents in the SkillGroup. |
| HandledCallsTime Today | Total handle time, in seconds, for inbound ACD calls counted
                                          					 as handled by agents in the SkillGroup. The time spent from the call being
                                          					 answered by the agent to the time the agent completed after call work time for
                                          					 the call. Includes hold time associated with the call. |
| IncomingCallsHeldToday | The total number of completed inbound ACD calls agents in the
                                          					 SkillGroup placed on hold at least once. |
| IncomingCallsHeldTimeToday | Total number of seconds completed inbound ACD calls were
                                          					 placed on hold by agents in the SkillGroup. |
| InternalCallsRcvd Today | Number of internal calls received by agents in the SkillGroup. |
| InternalCallsRcvd TimeToday | Number of seconds spent on internal calls received by agents
                                          					 in the SkillGroup. |
| InternalCallsHeld Today | The total number of internal calls agents in the SkillGroup
                                          					 placed on hold at least once. |
| InternalCallsHeld TimeToday | Total number of seconds completed internal calls were placed
                                          					 on hold by agents in the SkillGroup. |
| AutoOutCallsToday | Total number of AutoOut (predictive) calls completed by agents
                                          					 in the SkillGroup. |
| AutoOutCallsTalk TimeToday | Total talk time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent begins after
                                          					 call work for the call. The time includes hold time associated with the call. |
| AutoOutCallsTime Today | Total handle time, in seconds, for completed AutoOut
                                          					 (predictive) calls handled by agents in the SkillGroup. The value includes the
                                          					 time spent from the call being initiated to the time the agent completes after
                                          					 call work time for the call. The time includes hold time associated with the
                                          					 call. |
| AutoOutCallsHeld Today | The total number of completed AutoOut (predictive) calls that
                                          					 agents in the SkillGroup have placed on hold at least once. |
| AutoOutCallsHeld TimeToday | Total number of seconds AutoOut (predictive) calls were placed
                                          					 on hold by agents in the SkillGroup. |
| PreviewCallsToday | Total number of outbound Preview calls completed by agents in
                                          					 the SkillGroup. |
| PreviewCallsTalk TimeToday | Total talk time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call. |
| PreviewCallsTime Today | Total handle time, in seconds, for completed outbound Preview
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call. |
| PreviewCallsHeld Today | The total number of completed outbound Preview calls that
                                          					 agents in the SkillGroup have placed on hold at least once. |
| PreviewCallsHeld TimeToday | Total number of seconds outbound Preview calls were placed on
                                          					 hold by agents in the SkillGroup. |
| ReservationCalls Today | Total number of agent reservation calls completed by agents in
                                          					 the SkillGroup. |
| ReservationCalls TalkTimeToday | Total talk time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent begins after call work for
                                          					 the call. The time includes hold time associated with the call. |
| ReservationCalls TimeToday | Total handle time, in seconds, for completed agent reservation
                                          					 calls handled by agents in the SkillGroup. The value includes the time spent
                                          					 from the call being initiated to the time the agent completes after call work
                                          					 time for the call. The time includes hold time associated with the call. |
| ReservationCalls HeldToday | The total number of agent reservation calls that agents in the
                                          					 SkillGroup have placed on hold at least once. |
| ReservationCalls HeldTimeToday | Total number of seconds agent reservation calls were placed on
                                          					 hold by agents in the SkillGroup. |
| BargeInCallsToday | Total number of supervisor call barge-ins completed in the
                                          					 SkillGroup. |
| InterceptCallsToday | Total number of supervisor call intercepts completed in the
                                          					 SkillGroup. |
| MonitorCallsToday | Total number of supervisor call monitors completed in the
                                          					 SkillGroup. |
| WhisperCallsToday | Total number of supervisor call whispers completed by agents
                                          					 in the SkillGroup. |
| EmergencyCalls Today | Total number of emergency calls completed by agents in the
                                          					 SkillGroup. |
| CallsQToday* | The number of calls queued to the skill. This field is set to
                                          					 0xFFFFFFFF when this value is unknown or unavailable. |
| CallsQTimeToday* | The total queue time, in seconds, of calls queued to the SkillGroup. This field is set to 0xFFFFFFFF when this value is unknown
                                          or
                                          					 unavailable. |
| LongestCallQToday* | The longest queue time, in seconds, of all calls queued to the
                                          					 SkillGroup. This field is set to 0xFFFFFFFF when this value is unknown or
                                          					 unavailable. |

| Method | Description |
|---|---|
| GroupStatistics | Disables SkillGroup statistic messages. |
| DumpProperties | For more information, see CtiOs Object |
| EnableSkillGroupStatistics | Enables SkillGroup statistic messages. |
| GetElement | For more information, see CtiOs Object |
| GetNumProperties | For more information, see CtiOs Object |
| GetPropertyName | For more information, see CtiOs Object |
| GetValue | For more information, see CtiOs Object |
| GetValueInt (C++) GetValueIntObj (Java) | For more information, see CtiOs Object |
| GetValueString | For more information, see CtiOs Object |
| IsValid | For more information, see CtiOs Object |
| SetValue | For more information, see CtiOs Object |