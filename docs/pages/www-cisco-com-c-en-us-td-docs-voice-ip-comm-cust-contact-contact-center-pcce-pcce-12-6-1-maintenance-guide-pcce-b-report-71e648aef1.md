---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-report-71e648aef1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_Reporting-User-Guide-12_6_1/pcce_b_cisco-packaged-contact-center-enterprise_chapter_01010.html
retrieved_at: 2026-08-21T16:54:04.472311+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

Updated: May 10, 2021

Chapter: Agent and Supervisor Reporting

## Chapter: Agent and Supervisor Reporting

# Agent and Supervisor Reporting

## Agent States

Agent states are determined from an agent's
                              activity within a skill group or precision queue . Agent state is recorded in
                              numerous database tables and is presented in reports as both a number
                              ( Not Ready ) and as a percentage ( % Not
                                 Ready ).

You can monitor agent states in real time to
                              view current agent activity. You can also review past performance data to
                              identify trends in agent states. For example, historical reports can show how
                              much time an agent spends in Not Ready state, which indicates whether the agent
                              is adhering to the schedule.

Information
                              for some states is different when an agent is configured to handle multiple concurrent tasks in a Media Routing Domain (MRD).
                              This table highlights these
                              differences.

State in Skill Group or Precision Queue

Description for single-session MRDs

Description for multisession MRDs

Active or Talking

The agent is working
                                          on a task or a call in this skill group or precision queue.

For agents who handle
                                          nonvoice tasks, this state is reported as Active .

For agents who handle voice tasks, this state is reported as Talking .

The
                                          agent is working on one or more tasks associated with this skill group or precision queue.
                                          For these agents, the state is reported as Active .

Work Ready

The agent is
                                          performing wrap-up work for a call or task in this skill group or precision queue.

If the agent is handling a voice call, the agent enters Ready state
                                          when wrap-up is complete.

If the agent is handling a nonvoice task,
                                          the agent may enter Not Active or Not Ready state when wrap-up is
                                          complete.

The agent is performing
                                          wrap-up work for a task associated with this skill group or precision queue. The agent is not in
                                          the Active state for a task associated with this skill
                                          group.

Work Not
                                          Ready

The agent is performing
                                          wrap-up work for a call in this skill group or precision queue. The agent enters Not Ready state
                                          when wrap-up is complete.

This state is not used for agents signed into Enterprise Chat and
                                                						Email skill groups or precision queues.

This state is used during failover for agents signed into  skill groups or precision queues for third-party  multichannel
                                          applications that use the Task
                                                					Routing APIs.

This state is used during failover for agents signed in to  skill groups or precision queues for third-party  multichannel
                                          applications that use the Task
                                                					Routing APIs.

Paused or Hold

For agents who handle nonvoice tasks, the state is reported as Paused .

For agents who handle voice tasks,
                                          the state is reported as Hold .

For agents handling Outbound Option calls, the Hold state indicates that the agent has been reserved for a call because the
                                          Outbound Dialer puts the agent on hold while connecting the call.

The agent
                                          is Paused for a  task associated with this
                                          skill group or precision queue.

Reserved

The agent has been offered
                                          a call or task associated with the skill group or precision queue.

For voice calls,
                                          agents are Reserved when their phones are ringing.

Agents handling
                                          Outbound Option calls are never placed in Reserved state; the Outbound Option
                                          Dialer puts the agent on hold when reserving the agent for a call.

The agent is not in Active, Work Ready, or Paused
                                          state in this skill group or precision queue. The agent has been offered one or more tasks
                                          associated with this skill group or precision queue.

Busy Other

Busy Other is a state in
                                          which the agent handling calls is assigned to other skill groups during the
                                          interval.

For example, an agent could be talking on an inbound
                                          call in one skill group while simultaneously logged on to, and ready to accept
                                          calls from, other skill groups.

The agent can be active (talking
                                          on or handling calls) in only one skill group at a time. Therefore, while
                                          active in one skill group, for the other skill group the agent is considered to
                                          be in the Busy Other state.

The
                                          agent is Active, Work Ready, Reserved, or on Hold/Paused in another skill group
                                          or precision queue in the same MRD.

The agent is not
                                          in Active, Work Ready, Reserved, or Paused state for a task
                                          associated with this skill group or precision queue. The agent is in Active, Work Ready, Reserved,
                                          or Paused in another skill group or precision queue in the same MRD.

Not Active or Ready

The agent is not working on a task or call associated with this skill
                                          group or precision queue.

Same as single-session MRD.

Interrupted

The agent has been interrupted by a task from another MRD. If an agent is Interrupted in one skill group or precision queue,
                                          the agent is Interrupted in all skill groups or precision queues within the
                                          same MRD.

Voice calls cannot be interrupted.

This state is not used for agents signed in to Enterprise Chat and
                                                						Email skill groups or precision queues.

This state is used for agents signed in to  skill groups or precision queues for third-party  multichannel applications that
                                          use the Task
                                                					Routing APIs, if the agents are configured to accept interrupts.

Same as single-session MRD

Not Ready

The agent is not available to be assigned a call or task. If an agent is Not
                                          Ready in one skill group or precision queue, the agent is Not Ready in all skill groups or precision queues within the
                                          same MRD.

Same as single-session MRD

### Agent States, Skill
                           	 Groups, and Precision Queues

Agents can belong to
                                 		  multiple skill groups or precision queues in a Media Routing Domain (MRD). When
                                 		  an agent is handling a task that was routed to a skill group or precision queue,
                                 		  the agent is Active in that skill group or precision queue.

For direct
                                       				incoming calls or transferred routed calls that do not use the dialed number,
                                       				the active skill group is the default or first skill group defined for the
                                       				agent.

For new outgoing
                                       				calls (AgentOutCalls or InternalCalls) or transferred outbound calls, the
                                       				active skill group is 
                                       				the first skill group defined for the agent.

Agents can be configured to work on more than one task at a time, such as multiple chat sessions. When reporting on these
                                 agents, gather state information from both the Available in MRD and Agent State columns.

The agents' state
                                 		  in the active skill group or precision queue determines the state in the  other
                                 		  skill groups or precision queues in the MRD, as follows:

If the agent is
                                       				Not Ready in one skill group or precision queue in the MRD, the agent is Not
                                       				Ready in all skill groups or precision queues in the MRD.

If the agent is
                                       				Active, Work Ready, Reserved, or Hold/Paused in one skill group or precision
                                       				queue in the MRD, the agent state is Busy Other for all other skill groups or
                                       				precision queues in the MRD.

### Agent State and Task State Relationship

Agent state times are reported on interval boundaries regardless
                                 of whether the call or task is finished. Call and task state times are
                                 reported only when the task ends. The call or task ends when wrap-up is
                                 complete.

The following figure illustrates the correlation
                                 between agent state and call state for a voice call. The agent reserve time
                                 includes network time and offer/ring time. Network time is the time it took the call to arrive at the agent’s phone or desktop.
                                 Offering/ring time is   the amount of time that the call rang on the agent’s
                                 phone or waited on the agent’s desktop.

- Call Arrives and queues against SG1 (A) after  33 seconds the call also queues for agents in SG2 (B).

- The call remains queued to SG1 and SG2 for an additional  12  seconds, until it is routed to an agent who goes ready in SG2
                                    (C).

- Call rings on the agent’s phone (C) and is then answered by the agent (D), who talks on the call for  10  seconds before putting
                                    the call on hold (E).

- After 12  seconds, the agent retrieves the call (F) and talks for another 20  seconds.

At (G) the call is dropped which results in the agent going into Wrap state to perform after after-call work for  20  seconds
                                       at which time the agent becomes ready (H).

If the interval
                                       boundary ends when the call is ringing on the agent's phone, the reserved time
                                       for the agent includes the network time and part of the ring time. At the next
                                       interval, the remaining ring time is reported in the reserved time of the
                                       agent. However, the call’s time does not appear on a report until wrap-up has
                                       been completed on the call.

## Agent Logout Reason Codes

Agent logout reason codes are defined in the agent desktop software and
                              appear in historical reports as their numeric equivalent, with no text code.
                              For example, if reason code 1 equals "end of shift" and the agent selects that
                              reason for logging out, the report displays "1" .

In addition to
                              the codes configured at the desktop, some codes are generated automatically
                              when the agent is logged out by the software. The following table describes these
                              built-in logout reason codes.

Built-in Logout Reason Code

Description

-1

The agent reinitialized due to
                                          peripheral restart.

-2

The PG reset the agent, normally due to a PG failure.

-3

An
                                          administrator modified the agent's extension while the agent was logged
                                          in.

999

The agent was logged out by from Finesse by a supervisor.

50002

A CTI OS component failed, causing the agent to be logged out. This could
                                          be due to closing the agent desktop application, heartbeat time out, a CTI OS
                                          Server failure, or a CTI OS failure.

50004

The agent was logged out due
                                          to agent inactivity as configured in agent desk settings.

50020

The agent was
                                          logged out when the agent's skill group assignment dynamically changed.

50030

The agent was
                                          logged out when the agent's skill group assignment dynamically changed on the
                                          Administration & DataServer.

50040

The mobile agent was logged out because
                                          the call failed.

50042

The mobile agent was logged out because the phone line
                                          disconnected when using nailed connection mode.

20001—applicable if you are using Cisco Agent Desktop

The agent's state was changed to NOT READY.

20002—applicable if you are using Cisco Agent Desktop

Forces the logout request; for example, when Agent A attempts to login to Cisco Agent Desktop and Agent B is already logged
                                          in under that agent ID, Agent A is asked whether or not to force the login.

If Agent A answers yes, Agent B is logged out and Agent A is logged in. Reports would then show that Agent B logged out at
                                          a certain time with a reason code of 20002 (Agent B was forcibly logged out).

20003—applicable if you are using Cisco Agent Desktop

Not Ready for logout.

## Agent Not Ready
                        	 Reason Codes

There are reports
                              		  that show the codes agents select when entering Not Ready state, that calculate
                              		  the percentage of time spent in the Not Ready state, and that show specific Not
                              		  Ready reasons based on the time range you specify.

These reports help
                              		  you identify whether agents are taking the appropriate number of breaks and
                              		  whether their breaks are the appropriate length.

Some reports display
                              		  both the text of the reason code (if configured) and the
                              		  corresponding number. For example, if an agent enters Not Ready state and
                              		  selects "Break" as the
                              		  reason code, and if you have configured text for this code, reports display "Break [1]" .
                              		  Other reports display the numeric Not Ready reason code only.

In addition to Not
                              		  Ready reason codes that you define, there are built-in Not Ready reason codes
                              		  for situations in which the software automatically makes the agent Not Ready. The following table describes these built-in
                              Not Ready reason codes.

Built-in Not
                                          					 Ready Reason Code

Description

-1

Agent
                                          					 reinitialized (used if peripheral restarts).

-2

PG reset
                                          					 the agent, normally due to a PG failure.

-3

An
                                          					 administrator modified the agent's extension while the agent was logged in.

999

A Finesse
                                          					 supervisor changed the agent state.

50001

The CTI OS
                                          					 client disconnected, logging out the agent.

This
                                                      					 reason code is converted to a 50002, so 50001 does not display in the agent log
                                                      					 out records.

50002

A CTI OS
                                          					 component failed, causing the agent to be logged out. This could be due to
                                          					 closing the agent desktop application, heartbeat time-out, a CTI OS Server
                                          					 failure, or a CTI OS failure.

50003

Agent was
                                          					 logged out because Unified CM reported the device out of service.

50004

Agent was
                                          					 logged out due to agent inactivity as configured in agent desk settings.

50005

For a
                                          					 deployment where the Multi-line Agent Control is enabled in the peripheral, and
                                          					 the Multi-line Agent Behavior is configured to impact agent state, the Agent
                                          					 is set to Not Ready with this code while talking on a call on the Non-ACD
                                          					 line.

50010

The agent
                                          					 did not receive multiple consecutive routed calls. The system makes the agent
                                          					 Not Ready automatically so that additional calls are not routed to the agent.
                                          					 By default, the number of consecutive calls missed before the agent is made Not
                                          					 Ready is 2.

50020

Agent was
                                          					 logged out when the agent's skill group dynamically changed on the
                                          					 Administration & Data Server.

50030

Agent was
                                          					 logged out because the agent was logged in to a dynamic device target that is
                                          					 using the same dialed number (DN) as the PG static device target.

50040

Mobile agent
                                          					 was logged out because the call failed.

50041

Mobile agent
                                          					 state changed to Not Ready because the call failed when the mobile agent's
                                          					 phone line rang busy.

50042

Mobile agent
                                          					 was logged out because the phone line disconnected while using nailed
                                          					 connection mode.

50041

The agent's
                                          					 state was changed to Not Ready because the agent's phone line rang busy and a
                                          					 call failed.

32767

The agent's
                                          					 state was changed to Not Ready because the agent did not answer a call and the
                                          					 call was redirected to a different agent or skill group.

20001 - applicable if you are using Cisco Agent Desktop

Places the agent in the Not Ready state first before forcibly logging off the agent.

20002 - applicable if you are using Cisco Agent Desktop

Forces the logout request. For example, when Agent A attempts to log in to Cisco Agent Desktop and Agent B is already logged
                                          in under that agent ID, Agent A is asked whether to force the login.

If Agent A answers yes, Agent B is logged out and Agent A is logged in. Reports would then show that Agent B logged out at
                                          a certain time with a reason code of 20002 (Agent B was forcibly logged out).

20003 - applicable if you are using Cisco Agent Desktop

Not Ready for logout.

If agent is not already in the Logout state, request is made to place agent in the Not Ready state. Then logout request is
                                          made to log out the agent.

By default, built-in
                              		  Not Ready reason codes do not have associated textual reason codes. They appear
                              		  as numbers in reports. To see a textual code for these Not Ready
                              		  reason codes, enter the built-in Not Ready reason code into the Reason Code tool with the related text. For example, you
                              		  can label the 32767 Not Ready reason code "Redirection on No Answer."

## Agent Task Handling

Agents can receive and initiate many different types
                           of tasks. There are reports that show you what kind of tasks agents are
                           handling and how well they are handling them. For example, there are reports
                           that display statistics for calls placed, received, transferred, and
                           conferenced, and there are reports that indicate how many calls were rerouted
                           when the agent failed to answer the call.

Tasks can be internal or external, and
                           incoming or outgoing, as follows:

Internal tasks are calls made to an agent from another person  or from another agent on Packaged CCE.

External tasks are calls that are placed off the Packaged CCE,
                                 tasks that come in via CVP, or tasks that are
                                 routed to an agent from a person outside Packaged CCE. For example,
                                 calls from the call center to customers are considered external.

Incoming tasks are tasks that an agent receives.
                                 Multichannel tasks are always incoming.

Outgoing tasks are calls that an agent places. For
                                 example, if a customer calls an agent, the call is incoming for the agent. If
                                 an agent calls a supervisor, the call is outgoing for the agent.

For voice calls only, agents can place consultative calls and engage in conference calls.

Agents can transfer voice calls and  nonvoice tasks that were routed to CCE from third-party multichannel applications that
                           use the Task
                                 					Routing APIs.  Agents cannot transfer nonvoice Enterprise Chat and
                                 						Email tasks.

For each type of task that an agent
                           can initiate, the amount of time that the agent spent working on that task is
                           recorded in the Agent_Skill_Group_Interval database table.

The following table describes the tasks that an agent can receive and
                           initiate, how the time for each task is determined, and how those tasks are reported.

Type of task

Description

Reported as

Incoming direct/internal

Examples of this kind of call include calls that are
                                       directly transferred by another agent without going through a script and calls
                                       that resulted from agent-to-agent calling.

Data for these calls
                                       are stored in the InternalCallsRcvd fields of the Agent_Skill_Group_Interval
                                       historical database table.

The
                                       time for these tasks begins when the agent answers the task and ends when the
                                       task disconnects. The time is stored in the InternalCallsRcvdTime field.

Internal In

Outgoing external

These are calls initiated by agents from their extension that are placed outside the contact center. Outgoing External Tasks
                                       are always
                                       voice tasks.

Consultative, conference out, and transfer out calls are
                                       counted as outgoing external calls if they are placed outside the contact center or to remote
                                       agent extensions at another site.

Agent-to-Agent dialing is
                                       outgoing external for the agent initiating the call if the call has to be
                                       placed outside the contact center to get to the destination agent.

Data for these
                                       calls are stored in the AgentOutCalls fields of the Agent_Skill_Group_Interval
                                       historical database table.

The time for these tasks begins when
                                       the agent initiates the task and ends when the task disconnects. The time is
                                       stored in the AgentOutCallsTime field.

External Out
                                       Tasks

Outgoing internal

These are calls initiated by agents from their extension
                                       to another extension  within the contact center.
                                       Outgoing Internal Tasks are always voice tasks.

Consultative,
                                       conference out, and transfer out calls are counted as outgoing internal calls if
                                       they are placed to another CVP.

Agent-to-Agent calls are
                                       outgoing internal for the agent initiating the call.

Data for these calls are
                                       stored in the InternalCalls fields of the Agent_Skill_Group_Interval historical
                                       database table.

The time for these tasks begins when the agent initiates the
                                       task and ends when the task disconnects. The time is stored in the
                                       InternalCallsTime field.

Internal Out Tasks

CCE–routed calls

All calls that are routed to the agent.

Outbound Option calls are consideredCCE–routed/incoming
                                       calls.

Data for these calls are stored in the CallsHandled fields
                                       of the Agent_Skill_Group_Interval historical database table.

The time for these tasks begins when the agent answers the task and
                                       ends when the agent completes wrap-up. The time is stored in the
                                       HandledCallsTime field.

Tasks Handled

Tasks Handled includes all
                                       calls, including calls that are transferred and
                                       conferenced, and consultative calls. Tasks Handled provides a high level view
                                       of routed tasks. Other report columns such as Transfer In and Conf Out provide
                                       more details about how the task was handled.

Transferred in

Calls transferred to an agent from another agent. Calls that are blind transferred by one agent to CVP for re-routing are
                                       counted in this column for the agent who receives the rerouted call.

Nonvoice Task Routing tasks that are blind transferred are also counted in this column for the agent who receives the rerouted
                                       task.

The
                                       time for these tasks begins when the agent answers the transferred task and
                                       ends when the task disconnects. The time is stored in the
                                       TransferredInCallsTime field.

Data for these
                                       calls are stored in the TransferredIn fields of the Agent_Skill_Group_Interval
                                       historical database table.

Transfer In

Transferred out

Calls that are transferred from an agent. An agent can transfer both
                                       incoming and outgoing calls.

Nonvoice Task Routing tasks that are transferred from an agent are also counted in this column.

Data for these calls are stored in
                                       the TransferredOut fields of the Agent_Skill_Group_Interval historical database
                                       table.

The time for these tasks begins when the agent activates the transfer button
                                       and ends when the transfer is complete. The time is stored in the TransferredOutCallsTime field.

Transfer Out

Consultative

Calls in which an
                                       agent consulted with another agent or supervisor while having another call on
                                       hold.

Data for these calls are stored in the ConsultativeCalls
                                       fields of the Agent_Skill_Group_Interval historical database table.

The time
                                       for these tasks begins when the agent activates the transfer button and ends
                                       when the target agent answers and the held task is restored (drop consultative
                                       call) or consult party drops. The time is stored in the ConsultativeCallsTime
                                       field.

Cons Out

Conference in

Incoming calls that are
                                       conferenced.

Data for these calls are stored in the
                                       ConferencedInCalls fields of the Agent_Skill_Group_Interval historical database
                                       table.

The time for these tasks
                                       begins when the agent answers the task and ends when the task disconnects. The
                                       time is stored in the ConferenceInCallsTime field.

Conf In

Conference out

Outgoing calls
                                       that are conferenced.

Data for these calls are stored in the
                                       ConferencedOutCalls fields of the Agent_Skill_Group_Interval historical
                                       database table.

The time for these tasks begins when the agent
                                       activates the conference button and ends when the agent disconnects from the
                                       conference call and the supervisor drops out of the call. The time is stored in
                                       the ConferenceOutCallsTime field.

Conf Out

You might notice
                           overlapping data in your reports for the amount of time for different types of
                           calls. This happens because incoming tasks, such as CCE-routed tasks and calls
                           made directly to an agent, can be Transferred In and Conferenced In. Both incoming
                           calls and outgoing calls placed by agents can be Transferred Out and
                           Conferenced Out. The total time for the incoming or outgoing call includes
                           transfer and conference time.

## Agent Utilization: Full-Time Equivalents and Percent Utilization

Because agents can work on multiple media and in multiple skill
                              groups, they typically do not spend all of their time handling tasks for a
                              single skill group. Determining staffing needs based on agents whose time is
                              divided among skill groups and media can be difficult.

Report templates provide two types of statistics that give you a improved view of how agents are being utilized and how many
                              full-time agents would be required to handle the amount of work performed during an interval for a particular skill group.

These statistics are:

% Utilization (percent utilization)

FTE
                                    (full-time equivalent)

Percent
                                 utilization (% Utilization in reports) shows you how well agents are
                              being utilized within a skill group.  This metric is computed in reports by
                              dividing the total time agents spend handling calls in a skill group by the
                              total time agents were ready to handle tasks. To calculate the time that an
                              agent was ready, the system subtracts the Not Ready time from the total time
                              that agents were logged on. For example, if the agent spent 20 minutes
                              of the log on duration handling calls and was available to handle calls for 40
                              minutes, the percent utilization is 50%.

The full-time
                                 equivalent (FTE in reports) is the number of full-time agents that
                              would be required to perform the work done during that interval for a skill
                              group. To calculate the FTE, the system divides the total time that work was
                              performed by the total time in the interval. For example, if agents spent a
                              total of 3 hours handling tasks during a 30-minute interval,
                              the FTE for task handling during the interval is  3 hours / 0.5 hours, which
                              equals 6 full-time persons. This means that if all agents handled tasks
                              full-time, the work could have been done by 6 agents.

## Supervisor Activity

Agent team supervisors can take advantage of supervisory features available on their desktops. Use reports to see when agents requested assistance and when supervisors had to use the Barge-In and Intercept features.

### Supervisor Assist and Emergency Assist for Existing Call

Agents can activate supervisor assist or emergency assist buttons on
                                 their desktop when they need special assistance from the primary or secondary
                                 supervisor assigned to their team.

Follow
                                 these guidelines to ensure that you can obtain accurate and useful data
                                 from these features:

Configure skill groups
                                       for supervisors handling Supervisor Assist and Emergency Assist requests. For
                                       example, you can configure one skill group for all the supervisors of an agent team. This way, you can direct requests to
                                       these
                                       skill groups and report on Supervisor and Emergency Assist call activity for
                                       these skill groups.

Create call types and
                                       configure dialed numbers that map to the created call type.

Configure scripts to direct the requests to the supervisor skill group.

You can select consult as an option on the
                                 agent desktop settings for supervisor or emergency assist. If the
                                 agent is on a call when the agent activates either the Supervisor or Emergency
                                 Assist desktop feature, the CTI software activates the conference
                                 key on behalf of the agent's phone and calls the supervisor using the Supervisor
                                 or Emergency Assist script. This example assumes that the emergency or supervisor
                                 assist script has an Agent-to-Agent node to find a supervisor.
                                 The supervisor answers the call and consults privately with the agent. The
                                 following fields are incremented within the Agent Skill Group and Skill group
                                 tables.

Fields incremented for agent's skill group to which the call was
                                             routed

Fields incremented for supervisor's
                                             default skill group

CallsHandled, InternalCall, SupervisorAssistCalls/EmergencyAssist

InternalCallsRcvd

For the agent, the call is reported in Tasks Handled
                                 and either Sup Assist or Emergency report fields. For the supervisor, the call
                                 is reported in Tasks Handled report fields.

### Barge-In

When the supervisor activates the Barge-In desktop feature, the agent's desktop completes a conference to the
                                 supervisor so that the supervisor can join into the conversation with the call.
                                 The following fields increment for both the agent and the supervisor in the agent skill group and skill group
                                 tables.

Fields incremented for agent's skill group to which the call was
                                             routed

Fields incremented for supervisor's
                                             default skill group

CallsHandled, InternalCalls, BargeInCalls

BargeInCalls, InternalCallsRcvd

For the agent, the call is reported in Tasks Handled and Barge-In report fields. For the supervisor, the call is reported
                                 in Tasks Handled and
                                 Barge-In report fields.

### Intercept

If the supervisor decides to intercept (take over)
                                 the call, the supervisor activates the Intercept desktop button.
                                 This interception drops the agent out of the conference, which allows the
                                 supervisor to take over the call. The following fields are incremented during
                                 the intercept operation for both the agent skill group and skill group
                                 tables.

Fields incremented for agent's skill group to which the call was
                                             routed

Fields incremented for supervisor's
                                             default skill group

InterceptCalls

InterceptCalls

For the agent, the call is
                                 reported in the Intercept report field. For the supervisor, the call is
                                 reported in the Intercept report field.

| State in Skill Group or Precision Queue | Description for single-session MRDs | Description for multisession MRDs |
|---|---|---|
| Active or Talking | The agent is working
                                          on a task or a call in this skill group or precision queue. For agents who handle
                                          nonvoice tasks, this state is reported as Active . For agents who handle voice tasks, this state is reported as Talking . | The
                                          agent is working on one or more tasks associated with this skill group or precision queue.
                                          For these agents, the state is reported as Active . |
| Work Ready | The agent is
                                          performing wrap-up work for a call or task in this skill group or precision queue. If the agent is handling a voice call, the agent enters Ready state
                                          when wrap-up is complete. If the agent is handling a nonvoice task,
                                          the agent may enter Not Active or Not Ready state when wrap-up is
                                          complete. | The agent is performing
                                          wrap-up work for a task associated with this skill group or precision queue. The agent is not in
                                          the Active state for a task associated with this skill
                                          group. |
| Work Not
                                          Ready | The agent is performing
                                          wrap-up work for a call in this skill group or precision queue. The agent enters Not Ready state
                                          when wrap-up is complete. This state is not used for agents signed into Enterprise Chat and
                                                						Email skill groups or precision queues. This state is used during failover for agents signed into  skill groups or precision queues for third-party  multichannel
                                          applications that use the Task
                                                					Routing APIs. | This state is used during failover for agents signed in to  skill groups or precision queues for third-party  multichannel
                                          applications that use the Task
                                                					Routing APIs. |
| Paused or Hold | For agents who handle nonvoice tasks, the state is reported as Paused . For agents who handle voice tasks,
                                          the state is reported as Hold . For agents handling Outbound Option calls, the Hold state indicates that the agent has been reserved for a call because the
                                          Outbound Dialer puts the agent on hold while connecting the call. | The agent
                                          is Paused for a  task associated with this
                                          skill group or precision queue. |
| Reserved | The agent has been offered
                                          a call or task associated with the skill group or precision queue. For voice calls,
                                          agents are Reserved when their phones are ringing. Agents handling
                                          Outbound Option calls are never placed in Reserved state; the Outbound Option
                                          Dialer puts the agent on hold when reserving the agent for a call. | The agent is not in Active, Work Ready, or Paused
                                          state in this skill group or precision queue. The agent has been offered one or more tasks
                                          associated with this skill group or precision queue. |
| Busy Other Busy Other is a state in
                                          which the agent handling calls is assigned to other skill groups during the
                                          interval. For example, an agent could be talking on an inbound
                                          call in one skill group while simultaneously logged on to, and ready to accept
                                          calls from, other skill groups. The agent can be active (talking
                                          on or handling calls) in only one skill group at a time. Therefore, while
                                          active in one skill group, for the other skill group the agent is considered to
                                          be in the Busy Other state. | The
                                          agent is Active, Work Ready, Reserved, or on Hold/Paused in another skill group
                                          or precision queue in the same MRD. | The agent is not
                                          in Active, Work Ready, Reserved, or Paused state for a task
                                          associated with this skill group or precision queue. The agent is in Active, Work Ready, Reserved,
                                          or Paused in another skill group or precision queue in the same MRD. |
| Not Active or Ready | The agent is not working on a task or call associated with this skill
                                          group or precision queue. | Same as single-session MRD. |
| Interrupted | The agent has been interrupted by a task from another MRD. If an agent is Interrupted in one skill group or precision queue,
                                          the agent is Interrupted in all skill groups or precision queues within the
                                          same MRD. Voice calls cannot be interrupted. This state is not used for agents signed in to Enterprise Chat and
                                                						Email skill groups or precision queues. This state is used for agents signed in to  skill groups or precision queues for third-party  multichannel applications that
                                          use the Task
                                                					Routing APIs, if the agents are configured to accept interrupts. | Same as single-session MRD |
| Not Ready | The agent is not available to be assigned a call or task. If an agent is Not
                                          Ready in one skill group or precision queue, the agent is Not Ready in all skill groups or precision queues within the
                                          same MRD. | Same as single-session MRD |

| Built-in Logout Reason Code | Description |
|---|---|
| -1 | The agent reinitialized due to
                                          peripheral restart. |
| -2 | The PG reset the agent, normally due to a PG failure. |
| -3 | An
                                          administrator modified the agent's extension while the agent was logged
                                          in. |
| 999 | The agent was logged out by from Finesse by a supervisor. |
| 50002 | A CTI OS component failed, causing the agent to be logged out. This could
                                          be due to closing the agent desktop application, heartbeat time out, a CTI OS
                                          Server failure, or a CTI OS failure. |
| 50004 | The agent was logged out due
                                          to agent inactivity as configured in agent desk settings. |
| 50020 | The agent was
                                          logged out when the agent's skill group assignment dynamically changed. |
| 50030 | The agent was
                                          logged out when the agent's skill group assignment dynamically changed on the
                                          Administration & DataServer. |
| 50040 | The mobile agent was logged out because
                                          the call failed. |
| 50042 | The mobile agent was logged out because the phone line
                                          disconnected when using nailed connection mode. |
| 20001—applicable if you are using Cisco Agent Desktop | The agent's state was changed to NOT READY. |
| 20002—applicable if you are using Cisco Agent Desktop | Forces the logout request; for example, when Agent A attempts to login to Cisco Agent Desktop and Agent B is already logged
                                          in under that agent ID, Agent A is asked whether or not to force the login. If Agent A answers yes, Agent B is logged out and Agent A is logged in. Reports would then show that Agent B logged out at
                                          a certain time with a reason code of 20002 (Agent B was forcibly logged out). Note Cisco Unified Mobile Agent is the only exception, where CAD will not allow you to log out a login name/ID that is already
                                                   in use. | Note | Cisco Unified Mobile Agent is the only exception, where CAD will not allow you to log out a login name/ID that is already
                                                   in use. |
| Note | Cisco Unified Mobile Agent is the only exception, where CAD will not allow you to log out a login name/ID that is already
                                                   in use. |
| 20003—applicable if you are using Cisco Agent Desktop | Not Ready for logout. |

| Note | Cisco Unified Mobile Agent is the only exception, where CAD will not allow you to log out a login name/ID that is already
                                                   in use. |
|---|---|

| Built-in Not
                                          					 Ready Reason Code | Description |
|---|---|
| -1 | Agent
                                          					 reinitialized (used if peripheral restarts). |
| -2 | PG reset
                                          					 the agent, normally due to a PG failure. |
| -3 | An
                                          					 administrator modified the agent's extension while the agent was logged in. |
| 999 | A Finesse
                                          					 supervisor changed the agent state. |
| 50001 | The CTI OS
                                          					 client disconnected, logging out the agent. Note This
                                                      					 reason code is converted to a 50002, so 50001 does not display in the agent log
                                                      					 out records. | Note | This
                                                      					 reason code is converted to a 50002, so 50001 does not display in the agent log
                                                      					 out records. |
| Note | This
                                                      					 reason code is converted to a 50002, so 50001 does not display in the agent log
                                                      					 out records. |
| 50002 | A CTI OS
                                          					 component failed, causing the agent to be logged out. This could be due to
                                          					 closing the agent desktop application, heartbeat time-out, a CTI OS Server
                                          					 failure, or a CTI OS failure. |
| 50003 | Agent was
                                          					 logged out because Unified CM reported the device out of service. |
| 50004 | Agent was
                                          					 logged out due to agent inactivity as configured in agent desk settings. |
| 50005 | For a
                                          					 deployment where the Multi-line Agent Control is enabled in the peripheral, and
                                          					 the Multi-line Agent Behavior is configured to impact agent state, the Agent
                                          					 is set to Not Ready with this code while talking on a call on the Non-ACD
                                          					 line. |
| 50010 | The agent
                                          					 did not receive multiple consecutive routed calls. The system makes the agent
                                          					 Not Ready automatically so that additional calls are not routed to the agent.
                                          					 By default, the number of consecutive calls missed before the agent is made Not
                                          					 Ready is 2. |
| 50020 | Agent was
                                          					 logged out when the agent's skill group dynamically changed on the
                                          					 Administration & Data Server. |
| 50030 | Agent was
                                          					 logged out because the agent was logged in to a dynamic device target that is
                                          					 using the same dialed number (DN) as the PG static device target. |
| 50040 | Mobile agent
                                          					 was logged out because the call failed. |
| 50041 | Mobile agent
                                          					 state changed to Not Ready because the call failed when the mobile agent's
                                          					 phone line rang busy. |
| 50042 | Mobile agent
                                          					 was logged out because the phone line disconnected while using nailed
                                          					 connection mode. |
| 50041 | The agent's
                                          					 state was changed to Not Ready because the agent's phone line rang busy and a
                                          					 call failed. |
| 32767 | The agent's
                                          					 state was changed to Not Ready because the agent did not answer a call and the
                                          					 call was redirected to a different agent or skill group. |
| 20001 - applicable if you are using Cisco Agent Desktop | Places the agent in the Not Ready state first before forcibly logging off the agent. |
| 20002 - applicable if you are using Cisco Agent Desktop | Forces the logout request. For example, when Agent A attempts to log in to Cisco Agent Desktop and Agent B is already logged
                                          in under that agent ID, Agent A is asked whether to force the login. If Agent A answers yes, Agent B is logged out and Agent A is logged in. Reports would then show that Agent B logged out at
                                          a certain time with a reason code of 20002 (Agent B was forcibly logged out). |
| 20003 - applicable if you are using Cisco Agent Desktop | Not Ready for logout. If agent is not already in the Logout state, request is made to place agent in the Not Ready state. Then logout request is
                                          made to log out the agent. |

| Note | This
                                                      					 reason code is converted to a 50002, so 50001 does not display in the agent log
                                                      					 out records. |
|---|---|

| Type of task | Description | Reported as |
|---|---|---|
| Incoming direct/internal | Incoming Direct
                                    Tasks are tasks that come directly to the agent's extension. Examples of this kind of call include calls that are
                                       directly transferred by another agent without going through a script and calls
                                       that resulted from agent-to-agent calling. Data for these calls
                                       are stored in the InternalCallsRcvd fields of the Agent_Skill_Group_Interval
                                       historical database table. The
                                       time for these tasks begins when the agent answers the task and ends when the
                                       task disconnects. The time is stored in the InternalCallsRcvdTime field. | Internal In |
| Outgoing external | These are calls initiated by agents from their extension that are placed outside the contact center. Outgoing External Tasks
                                       are always
                                       voice tasks. Consultative, conference out, and transfer out calls are
                                       counted as outgoing external calls if they are placed outside the contact center or to remote
                                       agent extensions at another site. Agent-to-Agent dialing is
                                       outgoing external for the agent initiating the call if the call has to be
                                       placed outside the contact center to get to the destination agent. Data for these
                                       calls are stored in the AgentOutCalls fields of the Agent_Skill_Group_Interval
                                       historical database table. The time for these tasks begins when
                                       the agent initiates the task and ends when the task disconnects. The time is
                                       stored in the AgentOutCallsTime field. | External Out
                                       Tasks |
| Outgoing internal | These are calls initiated by agents from their extension
                                       to another extension  within the contact center.
                                       Outgoing Internal Tasks are always voice tasks. Consultative,
                                       conference out, and transfer out calls are counted as outgoing internal calls if
                                       they are placed to another CVP. Agent-to-Agent calls are
                                       outgoing internal for the agent initiating the call. Data for these calls are
                                       stored in the InternalCalls fields of the Agent_Skill_Group_Interval historical
                                       database table. The time for these tasks begins when the agent initiates the
                                       task and ends when the task disconnects. The time is stored in the
                                       InternalCallsTime field. | Internal Out Tasks |
| CCE–routed calls | All calls that are routed to the agent. Outbound Option calls are consideredCCE–routed/incoming
                                       calls. Data for these calls are stored in the CallsHandled fields
                                       of the Agent_Skill_Group_Interval historical database table. The time for these tasks begins when the agent answers the task and
                                       ends when the agent completes wrap-up. The time is stored in the
                                       HandledCallsTime field. | Tasks Handled Tasks Handled includes all
                                       calls, including calls that are transferred and
                                       conferenced, and consultative calls. Tasks Handled provides a high level view
                                       of routed tasks. Other report columns such as Transfer In and Conf Out provide
                                       more details about how the task was handled. |
| Transferred in | Calls transferred to an agent from another agent. Calls that are blind transferred by one agent to CVP for re-routing are
                                       counted in this column for the agent who receives the rerouted call. Nonvoice Task Routing tasks that are blind transferred are also counted in this column for the agent who receives the rerouted
                                       task. The
                                       time for these tasks begins when the agent answers the transferred task and
                                       ends when the task disconnects. The time is stored in the
                                       TransferredInCallsTime field. Data for these
                                       calls are stored in the TransferredIn fields of the Agent_Skill_Group_Interval
                                       historical database table. | Transfer In |
| Transferred out | Calls that are transferred from an agent. An agent can transfer both
                                       incoming and outgoing calls. Nonvoice Task Routing tasks that are transferred from an agent are also counted in this column. Data for these calls are stored in
                                       the TransferredOut fields of the Agent_Skill_Group_Interval historical database
                                       table. The time for these tasks begins when the agent activates the transfer button
                                       and ends when the transfer is complete. The time is stored in the TransferredOutCallsTime field. | Transfer Out |
| Consultative | Calls in which an
                                       agent consulted with another agent or supervisor while having another call on
                                       hold. Data for these calls are stored in the ConsultativeCalls
                                       fields of the Agent_Skill_Group_Interval historical database table. The time
                                       for these tasks begins when the agent activates the transfer button and ends
                                       when the target agent answers and the held task is restored (drop consultative
                                       call) or consult party drops. The time is stored in the ConsultativeCallsTime
                                       field. | Cons Out |
| Conference in | Incoming calls that are
                                       conferenced. Data for these calls are stored in the
                                       ConferencedInCalls fields of the Agent_Skill_Group_Interval historical database
                                       table. The time for these tasks
                                       begins when the agent answers the task and ends when the task disconnects. The
                                       time is stored in the ConferenceInCallsTime field. | Conf In |
| Conference out | Outgoing calls
                                       that are conferenced. Data for these calls are stored in the
                                       ConferencedOutCalls fields of the Agent_Skill_Group_Interval historical
                                       database table. The time for these tasks begins when the agent
                                       activates the conference button and ends when the agent disconnects from the
                                       conference call and the supervisor drops out of the call. The time is stored in
                                       the ConferenceOutCallsTime field. | Conf Out |

| Note | Agents can transfer and conference
                                    incoming calls both in and out. However, they can transfer and conference
                                    outgoing calls out only. This difference means that if an agent transfers an outgoing task
                                    to another agent, it is still considered an outgoing task. |
|---|---|

| Note | If you select a report interval that is less than 8 hours, the
                                       resulting value will be lower than expected. |
|---|---|

| Note | These supervisory features are not available to agents using MRDs other than Voice. |
|---|---|

| Fields incremented for agent's skill group to which the call was
                                             routed | Fields incremented for supervisor's
                                             default skill group |
|---|---|
| CallsHandled, InternalCall, SupervisorAssistCalls/EmergencyAssist | InternalCallsRcvd |

| Note | During the
                                          consultation, the supervisor can decide to barge-in to the call using the
                                          supervisor desktop Barge-In feature. |
|---|---|

| Fields incremented for agent's skill group to which the call was
                                             routed | Fields incremented for supervisor's
                                             default skill group |
|---|---|
| CallsHandled, InternalCalls, BargeInCalls | BargeInCalls, InternalCallsRcvd |

| Fields incremented for agent's skill group to which the call was
                                             routed | Fields incremented for supervisor's
                                             default skill group |
|---|---|
| InterceptCalls | InterceptCalls |