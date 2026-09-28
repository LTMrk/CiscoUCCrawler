---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--9c76880cbe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_ctios-supervisor-desktop-user-guide-125/ucce_b_ctios-supervisor-desktop-user-guide-125_chapter_0110.html
retrieved_at: 2026-08-22T00:00:49.252293+00:00
---

CTIOS Supervisor Desktop User Guide

# CTIOS Supervisor Desktop User Guide

Updated: January 31, 2020

Chapter: Statistical Information

## Chapter: Statistical Information

# Statistical Information

## Available Statistical Information

Click Statistics in the CTI Toolkit Supervisor Desktop Tools section to display the CTI Toolkit Statistics window.

## Agent Statistics

The Agent Statistics section provides statistical information about the current agent on a device. The information updates
                              periodically and at the end of a call. For details about the different methods to poll for agent statistics, refer to the CTI OS System Manager Guide for Cisco Unified ICM at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

The following table lists all the statistical information that is visible on the Agent Statistics display.

In agent statistic names, Today is defined as the time since midnight. Session is defined as the time since the agent logged in.

### Agent Statistics Values

Statistic

Definition

AvailTimeSession

The total time, in seconds, that the agent was in the Available state for any skill group.

LoggedOnTimeSession

The total time, in seconds, that the agent has been logged on.

NotReadyTimeSession

The total time, in seconds, that the agent was in the Not Ready state for all skill groups.

ICMAvailableTimeSession

The total time, in seconds, that the agent was in the Unified ICM Available state.

RoutableTimeSession

The total time, in seconds, that the agent was in the Routable state for all skill groups.

AgentOutCallsSession

The total number of completed outbound ACD calls made by agent.

AgentOutCallsTalkTimeSession

The total talk time, in seconds, for completed outbound ACD calls that the agent handled. The value includes the time spent
                                          from when the agent begins the call to when the agent begins after-call work for the call. The time includes hold time for
                                          the call.

AgentOutCallsTimeSession

The total handle time, in seconds, for completed outbound ACD calls that the agent handled. The value includes the time spent
                                          from when the agent starting the call to when the agent completes after-call work for the call. The time includes hold time
                                          for the call.

AgentOutCallsHeldSession

The total number of completed outbound ACD calls that the agent placed on hold at least once.

AgentOutCallsHeldTimeSession

The total number of seconds that outbound ACD calls were placed on hold.

HandledCallsSession

The total number of inbound ACD calls that the agent handled.

HandledCallsTalkTimeSession

The total talk time in seconds for inbound ACD calls counted as handled by the agent.

HandledCallsAfterCallTimeSession

The total after-call work time in seconds for inbound ACD calls counted as handled by the agent.

HandledCallsTimeSession

The total handle time, in seconds, for inbound ACD calls counted as handled by the agent. Includes the time spent from when
                                          the agent answers the call to when the agent completes the call. Includes hold time for the call.

IncomingCallsHeldSession

The total number of completed inbound ACD calls that the agent placed on hold at least once.

IncomingCallsHeldTimeSession

The total number of seconds that  completed inbound ACD calls were placed on hold.

InternalCallsSession

The number of internal calls that the agent  began.

InternalCallsTimeSession

The number of seconds spent on internal calls that the agent began.

InternalCallsRcvdSession

The number of internal calls that the agent  received.

InternalCallsRcvdTimeSession

The number of seconds spent on internal calls that the agent  received.

InternalCallsHeldSession

The total number of internal calls that the agent placed on hold at least once.

InternalCallsHeldTimeSession

The total number of seconds completed internal calls were placed on hold.

AutoOutCallsSession

The total number of AutoOut (predictive) calls that the agent completed.

AutoOutCallsTalkTimeSession

The total talk time, in seconds, of AutoOut (predictive) calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call.

AutoOutCallsTimeSession

The total handle time, in seconds, for AutoOut (predictive) calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes the call. The time includes hold time for the call.

AutoOutCallsHeldSession

The total number of completed AutoOut (predictive) calls that the agent placed on hold at least once.

AutoOutCallsHeldTimeSession

The total number of seconds that AutoOut (predictive) calls were placed on hold.

PreviewCallsSession

The total number of outbound Preview calls that the agent completed.

PreviewCallsTalkTimeSession

The total talk time, in seconds, of outbound Preview calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call.

PreviewCallsTimeSession

The total handle time, in seconds, for outbound Preview calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes the call. The time includes hold time for the call.

PreviewCallsHeldSession

The total number of completed outbound Preview calls that the agent placed on hold at least once.

PreviewCallsHeldTimeSession

The total number of seconds that outbound Preview calls were placed on hold.

ReservationCallsSession

The total number of agent reservation calls that the agent completed.

ReservationCallsTalkTimeSession

The total talk time, in seconds, of agent reservation calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call.

ReservationCallsTimeSession

The total handle time, in seconds, for agent reservation calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes the call. The time includes hold time for the call.

ReservationCallsHeldSession

The total number of completed agent reservation calls that the agent placed on hold at least once.

ReservationCallsHeldTimeSession

The total number of seconds that agent reservation calls were placed on hold.

BargeInCallsSession

The total number of supervisor call barge-ins completed.

InterceptCallsSession

The total number of supervisor call intercepts completed.

MonitorCallsSession

The total number of supervisor call monitors completed.

WhisperCallsSession

The total number of supervisor whisper calls completed.

EmergencyCallsSession

The total number of emergency calls.

AvailTimeToday

The total time, in seconds, that the agent was in the Available state for any skill group.

LoggedOnTimeToday

The total time, in seconds, that the agent has been logged on.

NotReadyTimeToday

The total time, in seconds, that the agent was in the Not Ready state for all skill groups.

ICMAvailableTimeToday

The total time, in seconds, that  the agent was in the Unified ICM Available state.

RoutableTimeToday

The total time, in seconds, that the agent was in the Routable state for all skill groups.

AgentOutCallsToday

The total number of completed outbound ACD calls that the agent made.

AgentOutCallsTalkTimeToday

The total talk time, in seconds, for completed outbound ACD calls that the agent handled. The value includes the time spent
                                          from when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call.

AgentOutCallsTimeToday

The total handle time, in seconds, for completed outbound ACD calls that the agent handled. The value includes the time spent
                                          from when the agent begins the call to when the agent completes for the call. The time includes hold time for the call.

AgentOutCallsHeldToday

The total number of completed outbound ACD calls that the agent placed on hold at least once.

AgentOutCallsHeldTimeToday

The total number of seconds that outbound ACD calls were placed on hold.

HandledCallsToday

The number of inbound ACD calls that the agent handled.

If the agent transfers the call, HandledCallsToday (in the AgentStatistics) does not update immediately. Instead, this statistic
                                                      updates as part of next call end. If that agent also transfers the next call, the count increments by 1 (the count is missed
                                                      for the second transferred call). If that agent handles the next call personally, then the count increments by 2 (which adjusts
                                                      the count correctly).

HandledCallsTalkTimeToday

The total talk time in seconds for inbound ACD calls counted as handled by the agent.

HandledCallsAfterCallTimeToday

The total after-call work time in seconds for inbound ACD calls counted as handled by the agent.

HandledCallsTimeToday

The total handle time, in seconds, for inbound ACD calls counted as handled by the agent. The value includes the time spent
                                          from when the agent answers the call to when the agent completes the call. Includes hold time for the call.

IncomingCallsHeldToday

The total number of completed inbound ACD calls that the agent placed on hold at least once.

IncomingCallsHeldTimeToday

The total number of seconds that completed inbound ACD calls were placed on hold.

InternalCallsToday

The number of internal calls that the agent placed.

InternalCallsTimeToday

The number of seconds spent on internal calls that the agent placed.

InternalCallsRcvdToday

The number of internal calls that the agent received.

InternalCallsRcvdTimeToday

The number of seconds spent on internal calls that the agent received.

InternalCallsHeldToday

The total number of internal calls that the agent placed on hold at least once.

InternalCallsHeldTimeToday

The total number of seconds that completed internal calls were placed on hold.

AutoOutCallsToday

The total number of AutoOut (predictive) calls that the agent completed.

AutoOutCallsTalkTimeToday

The total talk time, in seconds, of AutoOut (predictive) calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call.

AutoOutCallsTimeToday

The total handle time, in seconds, for AutoOut (predictive) calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes after-call work. The time includes hold time for the call.

AutoOutCallsHeldToday

The total number of completed AutoOut (predictive) calls that the agent placed on hold at least once.

AutoOutCallsHeldTimeToday

The total number of seconds that AutoOut (predictive) calls were placed on hold.

PreviewCallsToday

The total number of outbound Preview calls that the agent completed.

PreviewCallsTalkTimeToday

The total talk time, in seconds, of outbound Preview calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call.

PreviewCallsTimeToday

The total handle time, in seconds, of outbound Preview calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent completes the call. The time includes hold time for the call.

PreviewCallsHeldToday

The total number of completed outbound Preview calls that the agent placed on hold at least once.

PreviewCallsHeldTimeToday

The total number of seconds that outbound Preview calls were placed on hold.

ReservationCallsToday

The total number of agent reservation calls that the agent completed.

ReservationCallsTalkTimeToday

The total talk time, in seconds, of agent reservation calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call.

ReservationCallsTimeToday

The total handle time, in seconds, for agent reservation calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes the call. The time includes hold time for the call.

ReservationCallsHeldToday

The total number of completed agent reservation calls that the agent placed on hold at least once.

ReservationCallsHeldTimeToday

The total number of seconds that agent reservation calls were placed on hold.

BargeInCallsToday

The total number of supervisor call barge-ins completed.

InterceptCallsToday

The total number of supervisor call intercepts completed.

MonitorCallsToday

The total number of supervisor call monitors completed.

WhisperCallsToday

The total number of completed supervisor whisper calls.

EmergencyCallsToday

The total number of emergency calls.

## Queues Statistics

The Queues Statistics display provides a feed of skill group statistics and queue-level statistics. 
                              The following lists all the statistics that appear in the  display.

Skill group statistics behave differently if the logged-in agent is configured as a supervisor. For a supervisor, the Queues Statistics displays rows for each skill group to which the supervisor belongs or to which the supervisor's team members belong.

For example, suppose that a supervisor belongs to skill groups 1 and 2 and their team members belong to skill groups 2 and
                                          3. The Queues Statistics for that supervisor displays three rows corresponding to skill groups 1, 2, and 3.

In skill group statistic names: To5 refers to the current five-minute interval. ToHalf refers to the current half-hour interval. Today is defined as the time since midnight. Session is defined as the time since the agent logged in.

### Default Skill Group

Certain calls do not belong to any configured skill group—for example, a direct call to an agent's phone. For reporting purposes,
                              however, Unified CCE assigns every call to a skill group. To cover these miscellaneous calls, Unified CCE creates a default
                              skill group. Unified CCE numbers and names the default skill group with a random string of digits. This random string avoids
                              conflicts with skill groups that users create.

The default skill group must appear in the CTI OS Skill Group Statistics. You cannot renumber or rename it.

For more information on the default skill group, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

### Queues Statistics Values

Statistic

Definition

AgentsLoggedOn

The number of agents that are currently logged on to the skill group.

AgentsAvail

The number of agents for the skill group in Available state.

AgentsNotReady

The number of agents in the Not Ready state for the skill group.

AgentsReady

The number of agents that are in a work state (TALKING, HELD, WORK_READY, AVAILABLE, or RESERVED). The router uses this statistic
                                          to determine the number of working agents in the skill group when estimating the expected delay. It is the difference between
                                          AgentsLoggedOn and AgentsNotReady. Reference AgentsAvail to get the number of agents that are available to take calls right
                                          now.

AgentsTalkingIn

The number of agents in the skill group who are currently talking on inbound calls.

AgentsTalkingOut

The number of agents in the skill group who are currently talking on outbound calls.

AgentsTalkingOther

The number of agents in the skill group who are currently talking on internal (not inbound or outbound) calls.

AgentsWorkNotReady

The number of agents in the skill group in the Work Not Ready state.

AgentsWorkReady

The number of agents in the skill group in the Work Ready state.

AgentsBusyOther

The number of agents in the skill group who are currently busy with calls assigned to other skill groups.

AgentsReserved

The number of agents in the skill group who are currently in the Reserved state.

AgentsHold

The number of calls to the skill group that are currently on hold.

AgentsICMAvailable

The number of agents in the skill group who are currently in the Unified ICM Available state.

AgentsApplicationAvailable

The number of agents in the skill group who are currently in the ApplicationAvailable state.

AgentsTalkingAutoOut

The number of calls to the skill group that are currently talking on AutoOut (predictive) calls.

AgentsTalkingPreview

The number of calls to the skill group that are currently talking on outbound Preview calls.

AgentsTalkingReservation

The number of calls to the skill group that are currently talking on agent reservation calls.

RouterCallsQNow

The number of calls that are currently queued by the Unified ICM call router for this skill group. This field is set to –1
                                          when this value is unknown or unavailable.

LongestRouterCallQNow

The queue time, in seconds, of the  Unified ICM call router queued call that currently has been queued to the skill group
                                          for the longest time. This field is set to –1 when this value is unknown or unavailable.

AvailTimeTo5

The total seconds that agents in the skill group were in the Available state.

LoggedOnTimeTo5

The total time, in seconds, that agents in the skill group were logged on.

NotReadyTimeTo5

The total seconds that agents in the skill group were in the Not Ready state.

AgentOutCallsTo5

The total number of completed outbound ACD calls that the agents made in the skill group.

AgentOutCallsTalkTimeTo5

The total talk time, in seconds, for completed outbound ACD calls that agents handled in the skill group. The value includes
                                          the time spent from when the agent began the call to when the agent begins after-call work. The time includes hold time for
                                          the call.

AgentOutCallsTimeTo5

The total handle time, in seconds, for completed outbound ACD calls that agents handled in the skill group. The value includes
                                          the time spent from when the agent began the call to when the agent completes after-call work. The time includes hold time
                                          for the call.

AgentOutCallsHeldTo5

The total number of completed outbound ACD calls that agents in the skill group placed on hold at least once.

AgentOutCallsHeldTimeTo5

The total number of seconds that outbound ACD calls were placed on hold by agents in the skill group.

HandledCallsTo5

The number of inbound ACD calls that agents handled in the skill group.

HandledCallsTalkTimeTo5

The total talk time in seconds for inbound ACD calls counted as handled by agents in the skill group.

HandledCallsAfterCallTimeTo5

The total after-call work time in seconds for inbound ACD calls counted as handled by agents in the skill group.

HandledCallsTimeTo5

The total handle time, in seconds, for inbound ACD calls counted as handled by agents in the skill group. The time spent from
                                          when the agent answered the call to when the agent completed the call. Includes hold time for the call.

IncomingCallsHeldTo5

The total number of completed inbound ACD calls that agents in the skill group placed on hold at least once.

IncomingCallsHeldTimeTo5

The total number of seconds that agents placed completed inbound ACD calls in the skill group on hold.

InternalCallsRcvdTo5

The number of internal calls that agents received in the skill group.

InternalCallsRcvdTimeTo5

The number of seconds spent on internal calls that agents received in the skill group.

InternalCallsHeldTo5

The total number of internal calls that agents in the skill group placed on hold at least once.

InternalCallsHeldTimeTo5

The total number of seconds that agents placed completed internal calls on hold in the skill group.

AutoOutCallsTo5

The total number of AutoOut (predictive) calls that agents in the skill group completed.

AutoOutCallsTalkTimeTo5

The total talk time, in seconds, for completed AutoOut (predictive) calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent begins after-call work. The time includes hold time for
                                          the call.

AutoOutCallsTimeTo5

The total handle time, in seconds, for completed AutoOut (predictive) calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes after-call work. The time includes hold time
                                          for the call.

AutoOutCallsHeldTo5

The total number of completed AutoOut (predictive) calls that agents in the skill group placed on hold at least once.

AutoOutCallsHeldTimeTo5

The total number of seconds that agents in the skill group placed AutoOut (predictive) calls on hold.

PreviewCallsTo5

The total number of outbound Preview calls that agents in the skill group completed.

PreviewCallsTalkTimeTo5

The total talk time, in seconds, for completed outbound Preview calls that agents handled in the skill group. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call.

PreviewCallsTimeTo5

The total handle time, in seconds, for completed outbound Preview calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call.

PreviewCallsHeldTo5

The total number of completed outbound Preview calls that agents in the skill group placed on hold at least once.

PreviewCallsHeldTimeTo5

The total number of seconds that agents in the skill group placed outbound Preview calls on hold.

ReservationCallsTo5

The total number of agent reservation calls that agents in the skill group completed.

ReservationCallsTalkTimeTo5

The total talk time, in seconds, for completed agent reservation calls that agents handled in the skill group. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call.

ReservationCallsTimeTo5

The total handle time, in seconds, for completed agent reservation calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call.

ReservationCallsHeldTo5

The total number of agent reservation calls that agents in the skill group placed on hold at least once.

ReservationCallsHeldTimeTo5

The total number of seconds that agents in the skill group placed agent reservation calls on hold.

BargeInCallsTo5

The total number of supervisor call barge-ins completed in the skill group.

InterceptCallsTo5

The total number of supervisor call intercepts completed in the skill group.

MonitorCallsTo5

The total number of supervisor call monitors completed in the skill group.

WhisperCallsTo5

The total number of supervisor call whispers completed by agents in the skill group.

EmergencyCallsTo5

The total number of emergency calls that agents in the skill group completed.

AvailTimeToHalf

The total seconds that agents in the skill group were in the Available state.

LoggedOnTimeToHalf

The total time, in seconds, that agents in the skill group were logged on.

NotReadyTimeToHalf

The total seconds that agents in the skill group were in the Not Ready state.

AgentOutCallsToHalf

The total number of completed outbound ACD calls that the agents in the skill group made.

AgentOutCallsTalkTimeToHalf

The total talk time, in seconds, for completed outbound ACD calls that agents handled in the skill group. The value includes
                                          the time spent from when the agent began the call to when the agent begins after-call work. The time includes hold time for
                                          the call.

AgentOutCallsTimeToHalf

The total handle time, in seconds, for completed outbound ACD calls that agents handled in the skill group. The value includes
                                          the time spent from when the agent began the call to when the agent completes after-call work. The time includes hold time
                                          for the call.

AgentOutCallsHeldToHalf

The total number of completed outbound ACD calls that agents in the skill group placed on hold at least once.

AgentOutCallsHeldTimeToHalf

The total number of seconds that agents in the skill group placed outbound ACD calls on hold.

HandledCallsToHalf

The number of inbound ACD calls that agents handled in the skill group.

HandledCallsTalkTimeToHalf

The total talk time in seconds for inbound ACD calls counted as handled by agents in the skill group.

HandledCallsAfterCallTimeToHalf

The total after-call work time in seconds for inbound ACD calls counted as handled by agents in the skill group.

HandledCallsTimeToHalf

The total handle time, in seconds, for inbound ACD calls counted as handled by agents in the skill group. The time spent from
                                          when the agent answered the call to when the agent completed the call. Includes hold time for the call.

IncomingCallsHeldToHalf

The total number of completed inbound ACD calls that agents in the skill group placed on hold at least once.

IncomingCallsHeldTimeToHalf

The total number of seconds that agents in the skill group placed completed inbound ACD calls on hold.

InternalCallsRcvdToHalf

The number of internal calls that agents received in the skill group.

InternalCallsRcvdTimeToHalf

The number of seconds spent on internal calls that agents in the skill group received.

InternalCallsHeldToHalf

The total number of internal calls that agents in the skill group placed on hold at least once.

InternalCallsHeldTimeToHalf

The total number of seconds that agents in the skill group placed completed internal calls on hold.

AutoOutCallsToHalf

The total number of AutoOut (predictive) calls that agents in the skill group completed.

AutoOutCallsTalkTimeToHalf

The total talk time, in seconds, for completed AutoOut (predictive) calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent begins after-call work. The time includes hold time for
                                          the call.

AutoOutCallsTimeToHalf

The total handle time, in seconds, for completed AutoOut (predictive) calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call.

AutoOutCallsHeldToHalf

The total number of completed AutoOut (predictive) calls that agents in the skill group placed on hold at least once.

AutoOutCallsHeldTimeToHalf

The total number of seconds that agents in the skill group placed AutoOut (predictive) calls on hold.

PreviewCallsToHalf

The total number of outbound Preview calls that agents in the skill group completed.

PreviewCallsTalkTimeToHalf

The total talk time, in seconds, for completed outbound Preview calls that agents handled in the skill group. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call.

PreviewCallsTimeToHalf

The total handle time, in seconds, for completed outbound Preview calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call.

PreviewCallsHeldToHalf

The total number of completed outbound Preview calls that agents in the skill group placed on hold at least once.

PreviewCallsHeldTimeToHalf

The total number of seconds that agents in the skill group placed outbound Preview calls on hold.

ReservationCallsToHalf

The total number of agent reservation calls that agents in the skill group completed.

ReservationCallsTalkTimeToHalf

The total talk time, in seconds, for completed agent reservation calls that agents handled in the skill group. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call.

ReservationCallsTimeToHalf

The total handle time, in seconds, for completed agent reservation calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call.

ReservationCallsHeldToHalf

The total number of agent reservation calls that agents in the skill group placed on hold at least once.

ReservationCallsHeldTimeToHalf

The total number of seconds that agents in the skill group placed agent reservation calls on hold.

BargeInCallsToHalf

The total number of supervisor call barge-ins completed in the skill group.

InterceptCallsToHalf

The total number of supervisor call intercepts completed in the skill group.

MonitorCallsToHalf

The total number of supervisor call monitors completed in the skill group.

WhisperCallsToHalf

The total number of supervisor call whispers completed by agents in the skill group.

EmergencyCallsToHalf

The total number of emergency calls that agents in the skill group completed.

AvailTimeToday

The total seconds that agents in the skill group were in the Available state.

LoggedOnTimeToday

The total time, in seconds, that agents in the skill group were logged on.

NotReadyTimeToday

The total seconds that agents in the skill group were in the Not Ready state.

AgentOutCallsToday

The total number of completed outbound ACD calls that the agents in the skill group made.

AgentOutCallsTalkTimeToday

The total talk time, in seconds, for completed outbound ACD calls that agents in the skill group handled. The value includes
                                          the time spent from when the agent began the call to when the agent begins after-call work. The time includes hold time for
                                          the call.

AgentOutCallsTimeToday

The total handle time, in seconds, for completed outbound ACD calls that agents in the skill group handled. The value includes
                                          the time spent from when the agent began the call to when the agent completes the call. The time includes hold time for the
                                          call.

AgentOutCallsHeldToday

The total number of completed outbound ACD calls that agents in the skill group placed on hold at least once.

AgentOutCallsHeldTimeToday

The total number of seconds that agents in the skill group placed outbound ACD calls on hold.

HandledCallsToday

The number of inbound ACD calls that agents in the skill group handled.

HandledCallsTalkTimeToday

The total talk time in seconds for inbound ACD calls counted as handled by agents in the skill group.

HandledCallsAfterCallTimeToday

The total after-call work time in seconds for inbound ACD calls counted as handled by agents in the skill group.

HandledCallsTimeToday

The total handle time, in seconds, for inbound ACD calls counted as handled by agents in the skill group. The time spent from
                                          when the agent answered the call to when the agent completed the call. Includes hold time for the call.

IncomingCallsHeldToday

The total number of completed inbound ACD calls that agents in the skill group placed on hold at least once.

IncomingCallsHeldTimeToday

The total number of seconds that agents in the skill group placed completed inbound ACD calls on hold.

InternalCallsRcvdToday

The number of internal calls that agents in the skill group received.

InternalCallsRcvdTimeToday

The number of seconds spent on internal calls that agents in the skill group received.

InternalCallsHeldToday

The total number of internal calls that agents in the skill group placed on hold at least once.

InternalCallsHeldTimeToday

The total number of seconds that agents in the skill group placed completed internal calls on hold.

AutoOutCallsToday

The total number of AutoOut (predictive) calls that agents in the skill group completed.

AutoOutCallsTalkTimeToday

The total talk time, in seconds, for completed AutoOut (predictive) calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent begins after-call work. The time includes hold time for
                                          the call.

AutoOutCallsTimeToday

The total handle time, in seconds, for completed AutoOut (predictive) calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent completes after-call work. The time includes hold time
                                          for the call.

AutoOutCallsHeldToday

The total number of completed AutoOut (predictive) calls that agents in the skill group placed on hold at least once.

AutoOutCallsHeldTimeToday

The total number of seconds that agents in the skill group placed AutoOut (predictive) calls on hold.

PreviewCallsToday

The total number of outbound Preview calls that agents in the skill group completed.

PreviewCallsTalkTimeToday

The total talk time, in seconds, for completed outbound Preview calls that agents in the skill group handled. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call.

PreviewCallsTimeToday

The total handle time, in seconds, for completed outbound Preview calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call.

PreviewCallsHeldToday

The total number of completed outbound Preview calls that agents in the skill group placed on hold at least once.

PreviewCallsHeldTimeToday

The total number of seconds that agents in the skill group placed outbound Preview calls on hold.

ReservationCallsToday

The total number of agent reservation calls that agents in the skill group completed.

ReservationCallsTalkTimeToday

The total talk time, in seconds, for completed agent reservation calls that agents in the skill group handled. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call.

ReservationCallsTimeToday

The total handle time, in seconds, for completed agent reservation calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call.

ReservationCallsHeldToday

The total number of agent reservation calls that agents in the skill group placed on hold at least once.

ReservationCallsHeldTimeToday

The total number of seconds that agents in the skill group placed agent reservation calls on hold.

BargeInCallsToday

The total number of supervisor call barge-ins completed in the skill group.

InterceptCallsToday

The total number of supervisor call intercepts completed in the skill group.

MonitorCallsToday

The total number of supervisor call monitors completed in the skill group.

WhisperCallsToday

The total number of supervisor call whispers completed by agents in the skill group.

EmergencyCallsToday

The total number of emergency calls that agents in the skill group completed.

| Note | In agent statistic names, Today is defined as the time since midnight. Session is defined as the time since the agent logged in. |
|---|---|

| Statistic | Definition |
|---|---|
| AvailTimeSession | The total time, in seconds, that the agent was in the Available state for any skill group. |
| LoggedOnTimeSession | The total time, in seconds, that the agent has been logged on. |
| NotReadyTimeSession | The total time, in seconds, that the agent was in the Not Ready state for all skill groups. |
| ICMAvailableTimeSession | The total time, in seconds, that the agent was in the Unified ICM Available state. |
| RoutableTimeSession | The total time, in seconds, that the agent was in the Routable state for all skill groups. |
| AgentOutCallsSession | The total number of completed outbound ACD calls made by agent. |
| AgentOutCallsTalkTimeSession | The total talk time, in seconds, for completed outbound ACD calls that the agent handled. The value includes the time spent
                                          from when the agent begins the call to when the agent begins after-call work for the call. The time includes hold time for
                                          the call. |
| AgentOutCallsTimeSession | The total handle time, in seconds, for completed outbound ACD calls that the agent handled. The value includes the time spent
                                          from when the agent starting the call to when the agent completes after-call work for the call. The time includes hold time
                                          for the call. |
| AgentOutCallsHeldSession | The total number of completed outbound ACD calls that the agent placed on hold at least once. |
| AgentOutCallsHeldTimeSession | The total number of seconds that outbound ACD calls were placed on hold. |
| HandledCallsSession | The total number of inbound ACD calls that the agent handled. |
| HandledCallsTalkTimeSession | The total talk time in seconds for inbound ACD calls counted as handled by the agent. |
| HandledCallsAfterCallTimeSession | The total after-call work time in seconds for inbound ACD calls counted as handled by the agent. |
| HandledCallsTimeSession | The total handle time, in seconds, for inbound ACD calls counted as handled by the agent. Includes the time spent from when
                                          the agent answers the call to when the agent completes the call. Includes hold time for the call. |
| IncomingCallsHeldSession | The total number of completed inbound ACD calls that the agent placed on hold at least once. |
| IncomingCallsHeldTimeSession | The total number of seconds that  completed inbound ACD calls were placed on hold. |
| InternalCallsSession | The number of internal calls that the agent  began. |
| InternalCallsTimeSession | The number of seconds spent on internal calls that the agent began. |
| InternalCallsRcvdSession | The number of internal calls that the agent  received. |
| InternalCallsRcvdTimeSession | The number of seconds spent on internal calls that the agent  received. |
| InternalCallsHeldSession | The total number of internal calls that the agent placed on hold at least once. |
| InternalCallsHeldTimeSession | The total number of seconds completed internal calls were placed on hold. |
| AutoOutCallsSession | The total number of AutoOut (predictive) calls that the agent completed. |
| AutoOutCallsTalkTimeSession | The total talk time, in seconds, of AutoOut (predictive) calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call. |
| AutoOutCallsTimeSession | The total handle time, in seconds, for AutoOut (predictive) calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes the call. The time includes hold time for the call. |
| AutoOutCallsHeldSession | The total number of completed AutoOut (predictive) calls that the agent placed on hold at least once. |
| AutoOutCallsHeldTimeSession | The total number of seconds that AutoOut (predictive) calls were placed on hold. |
| PreviewCallsSession | The total number of outbound Preview calls that the agent completed. |
| PreviewCallsTalkTimeSession | The total talk time, in seconds, of outbound Preview calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call. |
| PreviewCallsTimeSession | The total handle time, in seconds, for outbound Preview calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes the call. The time includes hold time for the call. |
| PreviewCallsHeldSession | The total number of completed outbound Preview calls that the agent placed on hold at least once. |
| PreviewCallsHeldTimeSession | The total number of seconds that outbound Preview calls were placed on hold. |
| ReservationCallsSession | The total number of agent reservation calls that the agent completed. |
| ReservationCallsTalkTimeSession | The total talk time, in seconds, of agent reservation calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call. |
| ReservationCallsTimeSession | The total handle time, in seconds, for agent reservation calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes the call. The time includes hold time for the call. |
| ReservationCallsHeldSession | The total number of completed agent reservation calls that the agent placed on hold at least once. |
| ReservationCallsHeldTimeSession | The total number of seconds that agent reservation calls were placed on hold. |
| BargeInCallsSession | The total number of supervisor call barge-ins completed. |
| InterceptCallsSession | The total number of supervisor call intercepts completed. |
| MonitorCallsSession | The total number of supervisor call monitors completed. |
| WhisperCallsSession | The total number of supervisor whisper calls completed. |
| EmergencyCallsSession | The total number of emergency calls. |
| AvailTimeToday | The total time, in seconds, that the agent was in the Available state for any skill group. |
| LoggedOnTimeToday | The total time, in seconds, that the agent has been logged on. |
| NotReadyTimeToday | The total time, in seconds, that the agent was in the Not Ready state for all skill groups. |
| ICMAvailableTimeToday | The total time, in seconds, that  the agent was in the Unified ICM Available state. |
| RoutableTimeToday | The total time, in seconds, that the agent was in the Routable state for all skill groups. |
| AgentOutCallsToday | The total number of completed outbound ACD calls that the agent made. |
| AgentOutCallsTalkTimeToday | The total talk time, in seconds, for completed outbound ACD calls that the agent handled. The value includes the time spent
                                          from when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call. |
| AgentOutCallsTimeToday | The total handle time, in seconds, for completed outbound ACD calls that the agent handled. The value includes the time spent
                                          from when the agent begins the call to when the agent completes for the call. The time includes hold time for the call. |
| AgentOutCallsHeldToday | The total number of completed outbound ACD calls that the agent placed on hold at least once. |
| AgentOutCallsHeldTimeToday | The total number of seconds that outbound ACD calls were placed on hold. |
| HandledCallsToday | The number of inbound ACD calls that the agent handled. Note If the agent transfers the call, HandledCallsToday (in the AgentStatistics) does not update immediately. Instead, this statistic
                                                      updates as part of next call end. If that agent also transfers the next call, the count increments by 1 (the count is missed
                                                      for the second transferred call). If that agent handles the next call personally, then the count increments by 2 (which adjusts
                                                      the count correctly). | Note | If the agent transfers the call, HandledCallsToday (in the AgentStatistics) does not update immediately. Instead, this statistic
                                                      updates as part of next call end. If that agent also transfers the next call, the count increments by 1 (the count is missed
                                                      for the second transferred call). If that agent handles the next call personally, then the count increments by 2 (which adjusts
                                                      the count correctly). |
| Note | If the agent transfers the call, HandledCallsToday (in the AgentStatistics) does not update immediately. Instead, this statistic
                                                      updates as part of next call end. If that agent also transfers the next call, the count increments by 1 (the count is missed
                                                      for the second transferred call). If that agent handles the next call personally, then the count increments by 2 (which adjusts
                                                      the count correctly). |
| HandledCallsTalkTimeToday | The total talk time in seconds for inbound ACD calls counted as handled by the agent. |
| HandledCallsAfterCallTimeToday | The total after-call work time in seconds for inbound ACD calls counted as handled by the agent. |
| HandledCallsTimeToday | The total handle time, in seconds, for inbound ACD calls counted as handled by the agent. The value includes the time spent
                                          from when the agent answers the call to when the agent completes the call. Includes hold time for the call. |
| IncomingCallsHeldToday | The total number of completed inbound ACD calls that the agent placed on hold at least once. |
| IncomingCallsHeldTimeToday | The total number of seconds that completed inbound ACD calls were placed on hold. |
| InternalCallsToday | The number of internal calls that the agent placed. |
| InternalCallsTimeToday | The number of seconds spent on internal calls that the agent placed. |
| InternalCallsRcvdToday | The number of internal calls that the agent received. |
| InternalCallsRcvdTimeToday | The number of seconds spent on internal calls that the agent received. |
| InternalCallsHeldToday | The total number of internal calls that the agent placed on hold at least once. |
| InternalCallsHeldTimeToday | The total number of seconds that completed internal calls were placed on hold. |
| AutoOutCallsToday | The total number of AutoOut (predictive) calls that the agent completed. |
| AutoOutCallsTalkTimeToday | The total talk time, in seconds, of AutoOut (predictive) calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call. |
| AutoOutCallsTimeToday | The total handle time, in seconds, for AutoOut (predictive) calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes after-call work. The time includes hold time for the call. |
| AutoOutCallsHeldToday | The total number of completed AutoOut (predictive) calls that the agent placed on hold at least once. |
| AutoOutCallsHeldTimeToday | The total number of seconds that AutoOut (predictive) calls were placed on hold. |
| PreviewCallsToday | The total number of outbound Preview calls that the agent completed. |
| PreviewCallsTalkTimeToday | The total talk time, in seconds, of outbound Preview calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call. |
| PreviewCallsTimeToday | The total handle time, in seconds, of outbound Preview calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent completes the call. The time includes hold time for the call. |
| PreviewCallsHeldToday | The total number of completed outbound Preview calls that the agent placed on hold at least once. |
| PreviewCallsHeldTimeToday | The total number of seconds that outbound Preview calls were placed on hold. |
| ReservationCallsToday | The total number of agent reservation calls that the agent completed. |
| ReservationCallsTalkTimeToday | The total talk time, in seconds, of agent reservation calls that the agent completed. The value includes the time spent from
                                          when the agent begins the call to when the agent begins after-call work. The time includes hold time for the call. |
| ReservationCallsTimeToday | The total handle time, in seconds, for agent reservation calls that the agent completed. The value includes the time spent
                                          from when the agent begins the call to when the agent completes the call. The time includes hold time for the call. |
| ReservationCallsHeldToday | The total number of completed agent reservation calls that the agent placed on hold at least once. |
| ReservationCallsHeldTimeToday | The total number of seconds that agent reservation calls were placed on hold. |
| BargeInCallsToday | The total number of supervisor call barge-ins completed. |
| InterceptCallsToday | The total number of supervisor call intercepts completed. |
| MonitorCallsToday | The total number of supervisor call monitors completed. |
| WhisperCallsToday | The total number of completed supervisor whisper calls. |
| EmergencyCallsToday | The total number of emergency calls. |

| Note | If the agent transfers the call, HandledCallsToday (in the AgentStatistics) does not update immediately. Instead, this statistic
                                                      updates as part of next call end. If that agent also transfers the next call, the count increments by 1 (the count is missed
                                                      for the second transferred call). If that agent handles the next call personally, then the count increments by 2 (which adjusts
                                                      the count correctly). |
|---|---|

| Note | Skill group statistics behave differently if the logged-in agent is configured as a supervisor. For a supervisor, the Queues Statistics displays rows for each skill group to which the supervisor belongs or to which the supervisor's team members belong. For example, suppose that a supervisor belongs to skill groups 1 and 2 and their team members belong to skill groups 2 and
                                          3. The Queues Statistics for that supervisor displays three rows corresponding to skill groups 1, 2, and 3. |
|---|---|

| Note | In skill group statistic names: To5 refers to the current five-minute interval. ToHalf refers to the current half-hour interval. Today is defined as the time since midnight. Session is defined as the time since the agent logged in. |
|---|---|

| Statistic | Definition |
|---|---|
| AgentsLoggedOn | The number of agents that are currently logged on to the skill group. |
| AgentsAvail | The number of agents for the skill group in Available state. |
| AgentsNotReady | The number of agents in the Not Ready state for the skill group. |
| AgentsReady | The number of agents that are in a work state (TALKING, HELD, WORK_READY, AVAILABLE, or RESERVED). The router uses this statistic
                                          to determine the number of working agents in the skill group when estimating the expected delay. It is the difference between
                                          AgentsLoggedOn and AgentsNotReady. Reference AgentsAvail to get the number of agents that are available to take calls right
                                          now. |
| AgentsTalkingIn | The number of agents in the skill group who are currently talking on inbound calls. |
| AgentsTalkingOut | The number of agents in the skill group who are currently talking on outbound calls. |
| AgentsTalkingOther | The number of agents in the skill group who are currently talking on internal (not inbound or outbound) calls. |
| AgentsWorkNotReady | The number of agents in the skill group in the Work Not Ready state. |
| AgentsWorkReady | The number of agents in the skill group in the Work Ready state. |
| AgentsBusyOther | The number of agents in the skill group who are currently busy with calls assigned to other skill groups. |
| AgentsReserved | The number of agents in the skill group who are currently in the Reserved state. |
| AgentsHold | The number of calls to the skill group that are currently on hold. |
| AgentsICMAvailable | The number of agents in the skill group who are currently in the Unified ICM Available state. |
| AgentsApplicationAvailable | The number of agents in the skill group who are currently in the ApplicationAvailable state. |
| AgentsTalkingAutoOut | The number of calls to the skill group that are currently talking on AutoOut (predictive) calls. |
| AgentsTalkingPreview | The number of calls to the skill group that are currently talking on outbound Preview calls. |
| AgentsTalkingReservation | The number of calls to the skill group that are currently talking on agent reservation calls. |
| RouterCallsQNow | The number of calls that are currently queued by the Unified ICM call router for this skill group. This field is set to –1
                                          when this value is unknown or unavailable. |
| LongestRouterCallQNow | The queue time, in seconds, of the  Unified ICM call router queued call that currently has been queued to the skill group
                                          for the longest time. This field is set to –1 when this value is unknown or unavailable. |
| AvailTimeTo5 | The total seconds that agents in the skill group were in the Available state. |
| LoggedOnTimeTo5 | The total time, in seconds, that agents in the skill group were logged on. |
| NotReadyTimeTo5 | The total seconds that agents in the skill group were in the Not Ready state. |
| AgentOutCallsTo5 | The total number of completed outbound ACD calls that the agents made in the skill group. |
| AgentOutCallsTalkTimeTo5 | The total talk time, in seconds, for completed outbound ACD calls that agents handled in the skill group. The value includes
                                          the time spent from when the agent began the call to when the agent begins after-call work. The time includes hold time for
                                          the call. |
| AgentOutCallsTimeTo5 | The total handle time, in seconds, for completed outbound ACD calls that agents handled in the skill group. The value includes
                                          the time spent from when the agent began the call to when the agent completes after-call work. The time includes hold time
                                          for the call. |
| AgentOutCallsHeldTo5 | The total number of completed outbound ACD calls that agents in the skill group placed on hold at least once. |
| AgentOutCallsHeldTimeTo5 | The total number of seconds that outbound ACD calls were placed on hold by agents in the skill group. |
| HandledCallsTo5 | The number of inbound ACD calls that agents handled in the skill group. |
| HandledCallsTalkTimeTo5 | The total talk time in seconds for inbound ACD calls counted as handled by agents in the skill group. |
| HandledCallsAfterCallTimeTo5 | The total after-call work time in seconds for inbound ACD calls counted as handled by agents in the skill group. |
| HandledCallsTimeTo5 | The total handle time, in seconds, for inbound ACD calls counted as handled by agents in the skill group. The time spent from
                                          when the agent answered the call to when the agent completed the call. Includes hold time for the call. |
| IncomingCallsHeldTo5 | The total number of completed inbound ACD calls that agents in the skill group placed on hold at least once. |
| IncomingCallsHeldTimeTo5 | The total number of seconds that agents placed completed inbound ACD calls in the skill group on hold. |
| InternalCallsRcvdTo5 | The number of internal calls that agents received in the skill group. |
| InternalCallsRcvdTimeTo5 | The number of seconds spent on internal calls that agents received in the skill group. |
| InternalCallsHeldTo5 | The total number of internal calls that agents in the skill group placed on hold at least once. |
| InternalCallsHeldTimeTo5 | The total number of seconds that agents placed completed internal calls on hold in the skill group. |
| AutoOutCallsTo5 | The total number of AutoOut (predictive) calls that agents in the skill group completed. |
| AutoOutCallsTalkTimeTo5 | The total talk time, in seconds, for completed AutoOut (predictive) calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent begins after-call work. The time includes hold time for
                                          the call. |
| AutoOutCallsTimeTo5 | The total handle time, in seconds, for completed AutoOut (predictive) calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes after-call work. The time includes hold time
                                          for the call. |
| AutoOutCallsHeldTo5 | The total number of completed AutoOut (predictive) calls that agents in the skill group placed on hold at least once. |
| AutoOutCallsHeldTimeTo5 | The total number of seconds that agents in the skill group placed AutoOut (predictive) calls on hold. |
| PreviewCallsTo5 | The total number of outbound Preview calls that agents in the skill group completed. |
| PreviewCallsTalkTimeTo5 | The total talk time, in seconds, for completed outbound Preview calls that agents handled in the skill group. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call. |
| PreviewCallsTimeTo5 | The total handle time, in seconds, for completed outbound Preview calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call. |
| PreviewCallsHeldTo5 | The total number of completed outbound Preview calls that agents in the skill group placed on hold at least once. |
| PreviewCallsHeldTimeTo5 | The total number of seconds that agents in the skill group placed outbound Preview calls on hold. |
| ReservationCallsTo5 | The total number of agent reservation calls that agents in the skill group completed. |
| ReservationCallsTalkTimeTo5 | The total talk time, in seconds, for completed agent reservation calls that agents handled in the skill group. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call. |
| ReservationCallsTimeTo5 | The total handle time, in seconds, for completed agent reservation calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call. |
| ReservationCallsHeldTo5 | The total number of agent reservation calls that agents in the skill group placed on hold at least once. |
| ReservationCallsHeldTimeTo5 | The total number of seconds that agents in the skill group placed agent reservation calls on hold. |
| BargeInCallsTo5 | The total number of supervisor call barge-ins completed in the skill group. |
| InterceptCallsTo5 | The total number of supervisor call intercepts completed in the skill group. |
| MonitorCallsTo5 | The total number of supervisor call monitors completed in the skill group. |
| WhisperCallsTo5 | The total number of supervisor call whispers completed by agents in the skill group. |
| EmergencyCallsTo5 | The total number of emergency calls that agents in the skill group completed. |
| AvailTimeToHalf | The total seconds that agents in the skill group were in the Available state. |
| LoggedOnTimeToHalf | The total time, in seconds, that agents in the skill group were logged on. |
| NotReadyTimeToHalf | The total seconds that agents in the skill group were in the Not Ready state. |
| AgentOutCallsToHalf | The total number of completed outbound ACD calls that the agents in the skill group made. |
| AgentOutCallsTalkTimeToHalf | The total talk time, in seconds, for completed outbound ACD calls that agents handled in the skill group. The value includes
                                          the time spent from when the agent began the call to when the agent begins after-call work. The time includes hold time for
                                          the call. |
| AgentOutCallsTimeToHalf | The total handle time, in seconds, for completed outbound ACD calls that agents handled in the skill group. The value includes
                                          the time spent from when the agent began the call to when the agent completes after-call work. The time includes hold time
                                          for the call. |
| AgentOutCallsHeldToHalf | The total number of completed outbound ACD calls that agents in the skill group placed on hold at least once. |
| AgentOutCallsHeldTimeToHalf | The total number of seconds that agents in the skill group placed outbound ACD calls on hold. |
| HandledCallsToHalf | The number of inbound ACD calls that agents handled in the skill group. |
| HandledCallsTalkTimeToHalf | The total talk time in seconds for inbound ACD calls counted as handled by agents in the skill group. |
| HandledCallsAfterCallTimeToHalf | The total after-call work time in seconds for inbound ACD calls counted as handled by agents in the skill group. |
| HandledCallsTimeToHalf | The total handle time, in seconds, for inbound ACD calls counted as handled by agents in the skill group. The time spent from
                                          when the agent answered the call to when the agent completed the call. Includes hold time for the call. |
| IncomingCallsHeldToHalf | The total number of completed inbound ACD calls that agents in the skill group placed on hold at least once. |
| IncomingCallsHeldTimeToHalf | The total number of seconds that agents in the skill group placed completed inbound ACD calls on hold. |
| InternalCallsRcvdToHalf | The number of internal calls that agents received in the skill group. |
| InternalCallsRcvdTimeToHalf | The number of seconds spent on internal calls that agents in the skill group received. |
| InternalCallsHeldToHalf | The total number of internal calls that agents in the skill group placed on hold at least once. |
| InternalCallsHeldTimeToHalf | The total number of seconds that agents in the skill group placed completed internal calls on hold. |
| AutoOutCallsToHalf | The total number of AutoOut (predictive) calls that agents in the skill group completed. |
| AutoOutCallsTalkTimeToHalf | The total talk time, in seconds, for completed AutoOut (predictive) calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent begins after-call work. The time includes hold time for
                                          the call. |
| AutoOutCallsTimeToHalf | The total handle time, in seconds, for completed AutoOut (predictive) calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call. |
| AutoOutCallsHeldToHalf | The total number of completed AutoOut (predictive) calls that agents in the skill group placed on hold at least once. |
| AutoOutCallsHeldTimeToHalf | The total number of seconds that agents in the skill group placed AutoOut (predictive) calls on hold. |
| PreviewCallsToHalf | The total number of outbound Preview calls that agents in the skill group completed. |
| PreviewCallsTalkTimeToHalf | The total talk time, in seconds, for completed outbound Preview calls that agents handled in the skill group. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call. |
| PreviewCallsTimeToHalf | The total handle time, in seconds, for completed outbound Preview calls that agents handled in the skill group. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call. |
| PreviewCallsHeldToHalf | The total number of completed outbound Preview calls that agents in the skill group placed on hold at least once. |
| PreviewCallsHeldTimeToHalf | The total number of seconds that agents in the skill group placed outbound Preview calls on hold. |
| ReservationCallsToHalf | The total number of agent reservation calls that agents in the skill group completed. |
| ReservationCallsTalkTimeToHalf | The total talk time, in seconds, for completed agent reservation calls that agents handled in the skill group. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call. |
| ReservationCallsTimeToHalf | The total handle time, in seconds, for completed agent reservation calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call. |
| ReservationCallsHeldToHalf | The total number of agent reservation calls that agents in the skill group placed on hold at least once. |
| ReservationCallsHeldTimeToHalf | The total number of seconds that agents in the skill group placed agent reservation calls on hold. |
| BargeInCallsToHalf | The total number of supervisor call barge-ins completed in the skill group. |
| InterceptCallsToHalf | The total number of supervisor call intercepts completed in the skill group. |
| MonitorCallsToHalf | The total number of supervisor call monitors completed in the skill group. |
| WhisperCallsToHalf | The total number of supervisor call whispers completed by agents in the skill group. |
| EmergencyCallsToHalf | The total number of emergency calls that agents in the skill group completed. |
| AvailTimeToday | The total seconds that agents in the skill group were in the Available state. |
| LoggedOnTimeToday | The total time, in seconds, that agents in the skill group were logged on. |
| NotReadyTimeToday | The total seconds that agents in the skill group were in the Not Ready state. |
| AgentOutCallsToday | The total number of completed outbound ACD calls that the agents in the skill group made. |
| AgentOutCallsTalkTimeToday | The total talk time, in seconds, for completed outbound ACD calls that agents in the skill group handled. The value includes
                                          the time spent from when the agent began the call to when the agent begins after-call work. The time includes hold time for
                                          the call. |
| AgentOutCallsTimeToday | The total handle time, in seconds, for completed outbound ACD calls that agents in the skill group handled. The value includes
                                          the time spent from when the agent began the call to when the agent completes the call. The time includes hold time for the
                                          call. |
| AgentOutCallsHeldToday | The total number of completed outbound ACD calls that agents in the skill group placed on hold at least once. |
| AgentOutCallsHeldTimeToday | The total number of seconds that agents in the skill group placed outbound ACD calls on hold. |
| HandledCallsToday | The number of inbound ACD calls that agents in the skill group handled. |
| HandledCallsTalkTimeToday | The total talk time in seconds for inbound ACD calls counted as handled by agents in the skill group. |
| HandledCallsAfterCallTimeToday | The total after-call work time in seconds for inbound ACD calls counted as handled by agents in the skill group. |
| HandledCallsTimeToday | The total handle time, in seconds, for inbound ACD calls counted as handled by agents in the skill group. The time spent from
                                          when the agent answered the call to when the agent completed the call. Includes hold time for the call. |
| IncomingCallsHeldToday | The total number of completed inbound ACD calls that agents in the skill group placed on hold at least once. |
| IncomingCallsHeldTimeToday | The total number of seconds that agents in the skill group placed completed inbound ACD calls on hold. |
| InternalCallsRcvdToday | The number of internal calls that agents in the skill group received. |
| InternalCallsRcvdTimeToday | The number of seconds spent on internal calls that agents in the skill group received. |
| InternalCallsHeldToday | The total number of internal calls that agents in the skill group placed on hold at least once. |
| InternalCallsHeldTimeToday | The total number of seconds that agents in the skill group placed completed internal calls on hold. |
| AutoOutCallsToday | The total number of AutoOut (predictive) calls that agents in the skill group completed. |
| AutoOutCallsTalkTimeToday | The total talk time, in seconds, for completed AutoOut (predictive) calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent begins after-call work. The time includes hold time for
                                          the call. |
| AutoOutCallsTimeToday | The total handle time, in seconds, for completed AutoOut (predictive) calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent completes after-call work. The time includes hold time
                                          for the call. |
| AutoOutCallsHeldToday | The total number of completed AutoOut (predictive) calls that agents in the skill group placed on hold at least once. |
| AutoOutCallsHeldTimeToday | The total number of seconds that agents in the skill group placed AutoOut (predictive) calls on hold. |
| PreviewCallsToday | The total number of outbound Preview calls that agents in the skill group completed. |
| PreviewCallsTalkTimeToday | The total talk time, in seconds, for completed outbound Preview calls that agents in the skill group handled. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call. |
| PreviewCallsTimeToday | The total handle time, in seconds, for completed outbound Preview calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call. |
| PreviewCallsHeldToday | The total number of completed outbound Preview calls that agents in the skill group placed on hold at least once. |
| PreviewCallsHeldTimeToday | The total number of seconds that agents in the skill group placed outbound Preview calls on hold. |
| ReservationCallsToday | The total number of agent reservation calls that agents in the skill group completed. |
| ReservationCallsTalkTimeToday | The total talk time, in seconds, for completed agent reservation calls that agents in the skill group handled. The value includes
                                          the time spent from when the call began to when the agent begins after-call work. The time includes hold time for the call. |
| ReservationCallsTimeToday | The total handle time, in seconds, for completed agent reservation calls that agents in the skill group handled. The value
                                          includes the time spent from when the call began to when the agent completes the call. The time includes hold time for the
                                          call. |
| ReservationCallsHeldToday | The total number of agent reservation calls that agents in the skill group placed on hold at least once. |
| ReservationCallsHeldTimeToday | The total number of seconds that agents in the skill group placed agent reservation calls on hold. |
| BargeInCallsToday | The total number of supervisor call barge-ins completed in the skill group. |
| InterceptCallsToday | The total number of supervisor call intercepts completed in the skill group. |
| MonitorCallsToday | The total number of supervisor call monitors completed in the skill group. |
| WhisperCallsToday | The total number of supervisor call whispers completed by agents in the skill group. |
| EmergencyCallsToday | The total number of emergency calls that agents in the skill group completed. |