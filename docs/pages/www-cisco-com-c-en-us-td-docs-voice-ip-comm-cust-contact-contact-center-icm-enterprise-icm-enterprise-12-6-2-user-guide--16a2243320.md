---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-guide--16a2243320
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/guide/ucce_b_cisco-unified-contact-center-enterprise-reporting-user-guide-release1262/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_01001.html
retrieved_at: 2026-08-21T12:00:01.369822+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(2)

Updated: May 4, 2023

Chapter: All Fields Historical Reports

## Chapter: All Fields Historical Reports

# All Fields Historical Reports

## Agent Answers Analytics Report

The Agent Answers Analytics report helps you understand the impact of the Agent Answers services on an agent's performance.
                              It allows you to compare an agent's handle time when Agent Answers was enabled vs. when Agent Answers was disabled. You can
                              select Agent Answers views to display the data in a monthly report.

The report is built on the Termination Call Detail table. The report response time can be more than 10 minutes based on the
                                          Termination Call Detail table's data size. For this reason, it has to be run as a scheduled report on HDS-DDS when the call
                                          volume is less.

To improve the query performance, you can create additional indexes on the Termination Call Detail table. Use the following
                                          queries to create the index:

```
CREATE INDEX XIE5Termination_Call_Detail ON t_Termination_Call_Detail
(
CallTypeID
)

CREATE INDEX XIE6Termination_Call_Detail ON t_Termination_Call_Detail
(
AgentTeamID
)
```

Adding the indexes consume additional database space. For this reason, include the space consumed by the new indexes in your
                                          overall database size allocation.

Create these indexes only on the HDS-DDS from where you run this report.

```
DROP INDEX XIE5Termination_Call_Detail ON t_Termination_Call_Detail
```

```
DROP INDEX XIE6Termination_Call_Detail ON t_Termination_Call_Detail
```

Query: This report data is built from a Database Query.

Views: This report has the following views:

Agent Answers Analytics report (Grid view)

Agent Answers Analytics Handled Time (Line Chart)

Agent Answers Analytics Call Type (Column Chart)

Agent Answers Analytics Agent (Column Chart)

Grouping: This report is grouped by DateTime, Agent, Agent Team and Call Type.

Value List: Call Type and Agent Team

Database Schema Tables from which data is retrieved:

Person

Agent

Agent_Team

Termination_Call_Details

Call_Type

### Available Fields in the Agent Answers Analytics Grid View

#### Available Fields in the Agent Answers Analytics Report

Current fields are those fields that appear by default in a report generated from the stock template. The following current fields
                                 are listed in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Interval

The date and time of the data for a selected row in the MMM-YYYY format.

Derived from: Termination_Call_Details.DateTime

Team

The enterprise name of the Agent Team.

Derived from Termination_Call_Details.AgentTeamID.

Agent

The last name and first name of the agent.

This field is a calculated field, derived from Person.LastName + ", " + Person.FirstName.

Call Type

Derived from: Termination_Call_Details.CallTypeID

Total contacts handled

Total number of contacts handled in the selected interval.

This is a calculated field derived from: Total Contacts Handled when Agent Answers Services were Enabled + Total Contacts
                                             Handled when Agent Answers Services were Disabled.

Total contacts handled when Agent Answers Services were Disabled

The total number of contacts handled in the selected interval when the Agent Answers services were disabled.

Derived from Termination_Call_Details.AgentAnswersEnabled='N' or Termination_Call_Details.AgentAnswersEnabled is NULL

Average  Handled Time when Agent Answers Services were Disabled

The average time an agent spent handling calls in the selected interval while the Agent Answers services were disabled.

This field is a calculated field, derived from Total Duration (Termination_Call_Details.TalkTime + Termination_Call_Details.HoldTime
                                             + Termination_Call_Details.WorkTime) when Agent Answers Services were Disabled/Total Contacts Handled by Agent Answers Service
                                             were Disabled.

Total contacts handled when Agent Answers Services were Enabled

The total number of contacts handled in the selected interval when the Agent Answers services were enabled.

Derived from Termination_Call_Details.AgentAnswersEnabled='Y'

Average  Handled Time when Agent Answers Services were Enabled

The average time an agent spent handling calls in the selected interval while the Agent Answers services were enabled.

This field is a calculated field, derived from Total Duration  (Termination_Call_Details.TalkTime + Termination_Call_Details.HoldTime
                                             + Termination_Call_Details.WorkTime) when Agent Answers Services were Enabled/Total Contacts Handled when Agent Answers Services
                                             were Enabled.

### Available Fields in the Agent Answers Analytics Grid View

#### Available Fields in the Agent Answers Analytics Report

Current fields are those fields that appear by default in a report generated from the stock template. The following current fields
                                 are listed in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Interval

The date and time of the data for a selected row in the MMM-YYYY format.

Derived from: Termination_Call_Details.DateTime

Team

The enterprise name of the Agent Team.

Derived from Termination_Call_Details.AgentTeamID.

Agent

The last name and first name of the agent.

This field is a calculated field, derived from Person.LastName + ", " + Person.FirstName.

Call Type

Derived from: Termination_Call_Details.CallTypeID

Total contacts handled

Total number of contacts handled in the selected interval.

This is a calculated field derived from: Total Contacts Handled when Agent Answers Services were Enabled + Total Contacts
                                             Handled when Agent Answers Services were Disabled.

Total contacts handled when Agent Answers Services were Disabled

The total number of contacts handled in the selected interval when the Agent Answers services were disabled.

Derived from Termination_Call_Details.AgentAnswersEnabled='N' or Termination_Call_Details.AgentAnswersEnabled is NULL

Average  Handled Time when Agent Answers Services were Disabled

The average time an agent spent handling calls in the selected interval while the Agent Answers services were disabled.

This field is a calculated field, derived from Total Duration (Termination_Call_Details.TalkTime + Termination_Call_Details.HoldTime
                                             + Termination_Call_Details.WorkTime) when Agent Answers Services were Disabled/Total Contacts Handled by Agent Answers Service
                                             were Disabled.

Total contacts handled when Agent Answers Services were Enabled

The total number of contacts handled in the selected interval when the Agent Answers services were enabled.

Derived from Termination_Call_Details.AgentAnswersEnabled='Y'

Average  Handled Time when Agent Answers Services were Enabled

The average time an agent spent handling calls in the selected interval while the Agent Answers services were enabled.

This field is a calculated field, derived from Total Duration  (Termination_Call_Details.TalkTime + Termination_Call_Details.HoldTime
                                             + Termination_Call_Details.WorkTime) when Agent Answers Services were Enabled/Total Contacts Handled when Agent Answers Services
                                             were Enabled.

## Agent Historical
                        	 All Fields

The Agent
                              		  Historical All Fields report presents a historical view of the activity of
                              		  selected agents, showing each agent's skill groups, completed tasks, and agent
                              		  state times.

Query: This report data
                              		  is built from an Anonymous Block type query.

Views: This report has one grid view, Agent Historical All Fields.

Grouping: This report
                              		  is grouped and sorted by agent name and then by skill group.

Value List: Agents

Database Schema Tables from which data is retrieved:

Agent

Agent_Skill_Group_Interval

Skill_Group

Person

Media_Routing_Domain

Agent_Interval

Precision_Queue

### Available Fields in the Agent Historical All Fields Grid View

In addition to
                                 		  the fields that appear by default as Current, most Available fields in this
                                 		  report are derived from the Agent_Interval and Agent_Skill_Group_Interval
                                 		  tables.

The Handled field  is
                                 		  derived from  CallsHandled in the Agent_Skill_Group_Interval table.

Handled is the
                                 		  number of inbound calls that were answered and have completed wrap-up by agents
                                 		  in the skill group during the interval.

The Wrap
                                    			 Time field is a calculated field derived from
                                 		  Agent_Skill_Group_Interval.WorkNotReadyTime +
                                 		  Agent_Skill_Group_Interval.WorkReadyTime.

Wrap Time is the
                                 		  total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                 		  wrap-up on incoming and outgoing tasks in the interval.

### Current Fields in
                           	 the Agent Historical All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed
                                 below in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Agent

The last name and first name of the agent.

This field is a calculated field, derived from Person.LastName + ", " + Person.FirstName.

Precision Queue/Skill Group

The agent skill group's enterprise name.

Derived from Skill_Group.EnterpriseName.

Attributes

The names of the attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Derived from Agent_Interval.DateTime.

COMPLETED TASKS

Handled

The number of inbound calls that were answered and have completed wrap-up by agents during the interval.

Derived from Agent_Skill_Group_Interval.CallsHandled.

Average Handle Time

The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds).

This field is a calculated field, derived from

Agent_Skill_Group_Interval.HandledCallsTime/Agent_Skill_Group_Interval.CallsHandled.

Held

The number of incoming calls to this agent that were placed on hold in the interval.

Derived from Agent_Skill_Group_Interval.IncomingCallsOnHold.

Average Hold Time

The average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold in the interval, for all incoming calls
                                             that included hold time.

This field is a calculated field, derived from

Agent_Skill_Group_Interval.IncomingCallsOnHoldTime/Agent_Skill_Group_Interval.IncomingCallsOnHold.

Abandon Ring

For voice: the total number of calls that were abandoned while the agent's phone was ringing.

For non-voice: the total number of tasks that were abandoned while being offered to an agent.

Derived from Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number of tasks that left the agent's phone or terminal that were redirected to another dialed number because of no answer
                                             in the interval.

Derived from Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval.

Derived from Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number of incoming calls that were transferred to this agent from other agents within the same peripheral that did not
                                             go to IVR for queuing in the interval. This value is updated when the agent completes the call.

For blind transfers in the Unified CCE with a Unified CCE System PG, this field updates when the call that was blind transferred to an IVR is subsequently transferred to another agent
                                             and the agent answers the call. For this call scenario, this field is not updated in the Unified CCE without a Unified CCE System PG.

Derived from Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number of calls this agent transferred to another agent, precision queue, or skill group in the interval. This includes
                                             Consultative Calls if this transfer was consultative-not blind. The value is updated at the time the agent completes the transfer
                                             of the call.

This field is a calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls + Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number of outgoing external calls that this agent made in the interval.

Derived from Agent_Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIMES

Logged On Time

The total time during the interval the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format.

Derived from Agent_Interval.LoggedOnTime.

%Active

The percentage of time that the agent spent talking on calls in relation to the agent's LoggedOnTime.

This field is a calculated field, derived from:(Agent_Skill_Group_Interval.TalkInTime + Agent_Skill_Group_Interval.TalkOutTime
                                             + Agent_Skill_Group_Interval.TalkOtherTime + Agent_Skill_Group_Interval.TalkAutoOutTime + Agent_Skill_Group_Interval.TalkPreviewTime
                                             + Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime.

%Hold

The percentage of time that the agent put a call on hold or paused a task in relation to LoggedOnTime or the interval, whichever
                                             is less.

This field is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime/Agent_Interval.LoggedOnTimeTime.

%Not Active

The percentage of time that the agent spent in the Not Active or Available state in relation to LoggedOnTime. Applies to all
                                             skill groups and precision queues.

This field is a calculated field derived from Agent_Interval.AvailTime/Agent_Interval.LoggedOnTime.

%Not Ready

The percentage of time that the agent spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever
                                             is less. Applies to all skill groups and precision queues.

This field is a calculated field, derived from Agent_Interval.NotReadyTime / Agent_Interval.LoggedOnTime.

%Reserved

The percentage of time that the agent spent in Reserved state waiting for task from this skill group or precision queue in
                                             relation to LoggedOnTime.

This field is a calculated field, derived from Agent_Skill_Group_Interval.ReservedStateTime /Agent_Interval.LoggedOnTime.

%Wrap Up

The percentage of time that the agent spent in Wrap-up state after an incoming or outgoing call to or from this skill group
                                             or precision queue in relation to LoggedOnTime.

The agent state time percentages in the Report Summary row add up to 100 percent only after you select all the skill groups
                                             or precision queues for an agent. When viewing a subset of an agent's skill groups or precision queues, the percentages may
                                             not balance.

This field is a calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime + Agent_Skill_Group_Interval.WorkNotReadyTime)/Agent_Interval.LoggedOnTime.

%Busy Other

The percentage of time that the agent spent in the Busy Other state by handling calls assigned to other skill group or precision
                                             queue in relation to LoggedOnTime.

This field is a calculated field, derived from Agent_Skill_Group_Interval.BusyOtherTime/Agent_Interval.LoggedOnTime.

### Available Fields in the Agent Historical All Fields Grid View

In addition to
                                 		  the fields that appear by default as Current, most Available fields in this
                                 		  report are derived from the Agent_Interval and Agent_Skill_Group_Interval
                                 		  tables.

The Handled field  is
                                 		  derived from  CallsHandled in the Agent_Skill_Group_Interval table.

Handled is the
                                 		  number of inbound calls that were answered and have completed wrap-up by agents
                                 		  in the skill group during the interval.

The Wrap
                                    			 Time field is a calculated field derived from
                                 		  Agent_Skill_Group_Interval.WorkNotReadyTime +
                                 		  Agent_Skill_Group_Interval.WorkReadyTime.

Wrap Time is the
                                 		  total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                 		  wrap-up on incoming and outgoing tasks in the interval.

### Current Fields in
                           	 the Agent Historical All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed
                                 below in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Agent

The last name and first name of the agent.

This field is a calculated field, derived from Person.LastName + ", " + Person.FirstName.

Precision Queue/Skill Group

The agent skill group's enterprise name.

Derived from Skill_Group.EnterpriseName.

Attributes

The names of the attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Derived from Agent_Interval.DateTime.

COMPLETED TASKS

Handled

The number of inbound calls that were answered and have completed wrap-up by agents during the interval.

Derived from Agent_Skill_Group_Interval.CallsHandled.

Average Handle Time

The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds).

This field is a calculated field, derived from

Agent_Skill_Group_Interval.HandledCallsTime/Agent_Skill_Group_Interval.CallsHandled.

Held

The number of incoming calls to this agent that were placed on hold in the interval.

Derived from Agent_Skill_Group_Interval.IncomingCallsOnHold.

Average Hold Time

The average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold in the interval, for all incoming calls
                                             that included hold time.

This field is a calculated field, derived from

Agent_Skill_Group_Interval.IncomingCallsOnHoldTime/Agent_Skill_Group_Interval.IncomingCallsOnHold.

Abandon Ring

For voice: the total number of calls that were abandoned while the agent's phone was ringing.

For non-voice: the total number of tasks that were abandoned while being offered to an agent.

Derived from Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number of tasks that left the agent's phone or terminal that were redirected to another dialed number because of no answer
                                             in the interval.

Derived from Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval.

Derived from Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number of incoming calls that were transferred to this agent from other agents within the same peripheral that did not
                                             go to IVR for queuing in the interval. This value is updated when the agent completes the call.

For blind transfers in the Unified CCE with a Unified CCE System PG, this field updates when the call that was blind transferred to an IVR is subsequently transferred to another agent
                                             and the agent answers the call. For this call scenario, this field is not updated in the Unified CCE without a Unified CCE System PG.

Derived from Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number of calls this agent transferred to another agent, precision queue, or skill group in the interval. This includes
                                             Consultative Calls if this transfer was consultative-not blind. The value is updated at the time the agent completes the transfer
                                             of the call.

This field is a calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls + Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number of outgoing external calls that this agent made in the interval.

Derived from Agent_Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIMES

Logged On Time

The total time during the interval the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format.

Derived from Agent_Interval.LoggedOnTime.

%Active

The percentage of time that the agent spent talking on calls in relation to the agent's LoggedOnTime.

This field is a calculated field, derived from:(Agent_Skill_Group_Interval.TalkInTime + Agent_Skill_Group_Interval.TalkOutTime
                                             + Agent_Skill_Group_Interval.TalkOtherTime + Agent_Skill_Group_Interval.TalkAutoOutTime + Agent_Skill_Group_Interval.TalkPreviewTime
                                             + Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime.

%Hold

The percentage of time that the agent put a call on hold or paused a task in relation to LoggedOnTime or the interval, whichever
                                             is less.

This field is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime/Agent_Interval.LoggedOnTimeTime.

%Not Active

The percentage of time that the agent spent in the Not Active or Available state in relation to LoggedOnTime. Applies to all
                                             skill groups and precision queues.

This field is a calculated field derived from Agent_Interval.AvailTime/Agent_Interval.LoggedOnTime.

%Not Ready

The percentage of time that the agent spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever
                                             is less. Applies to all skill groups and precision queues.

This field is a calculated field, derived from Agent_Interval.NotReadyTime / Agent_Interval.LoggedOnTime.

%Reserved

The percentage of time that the agent spent in Reserved state waiting for task from this skill group or precision queue in
                                             relation to LoggedOnTime.

This field is a calculated field, derived from Agent_Skill_Group_Interval.ReservedStateTime /Agent_Interval.LoggedOnTime.

%Wrap Up

The percentage of time that the agent spent in Wrap-up state after an incoming or outgoing call to or from this skill group
                                             or precision queue in relation to LoggedOnTime.

The agent state time percentages in the Report Summary row add up to 100 percent only after you select all the skill groups
                                             or precision queues for an agent. When viewing a subset of an agent's skill groups or precision queues, the percentages may
                                             not balance.

This field is a calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime + Agent_Skill_Group_Interval.WorkNotReadyTime)/Agent_Interval.LoggedOnTime.

%Busy Other

The percentage of time that the agent spent in the Busy Other state by handling calls assigned to other skill group or precision
                                             queue in relation to LoggedOnTime.

This field is a calculated field, derived from Agent_Skill_Group_Interval.BusyOtherTime/Agent_Interval.LoggedOnTime.

## Agent Not Ready Historical

The Agent Not Ready Historical report shows
                              		  the total Logged On Time, total Not Ready time, and Not Ready time for each
                              		  reason code for an agent.

Views: This report has one grid view, Agent Not Ready Historical.

Query: This report data is built from an Anonymous Block.

Grouping: This report is grouped and sorted by Agent Name and then by Date and Time every
                              		  interval.

Value List: Agent

Database Schema Tables from which data is retrieved:

Agent

Person

Agent_Team_Member

Agent_Team

Agent_Interval

Agent_Event_Detail

### Current Fields
                              		  in the Agent Not Ready Historical Report

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed below
                              in the order (left to right) in which they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

DateTime

The date
                                          						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                          						HH:MM:SS (hours, minutes, seconds) format.

Derived
                                          						from: Agent_Skill_Group_Interval.DateTime

Logged On
                                          						Time

The
                                          						total time that the agents were logged in (staffed) for the specified time
                                          						period in any split/skill, measured in HH:MM:SS (hours, minutes, seconds)
                                          						format.

Derived
                                          						from: Agent_Skill_Group_Interval.LoggedOnTime

Not
                                          						Ready Time

The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. Value taken directly from the database.

Derived
                                          						from: Agent_Interval.NotReadyTime

Time in

RC0 to RC9

The time
                                          						that the agent spent in Not Ready state with each of the reason codes 0 - 9.

Derived
                                          						from: Agent_Event_Detail

RC50002

Not Ready Time spent in 50002. A CTI component failed, causing the agent to be set to Not Ready. This could be due to closing
                                          the agent desktop application, heartbeat timeout, a CTI server failure, or a CTI server client failure (such as Finesse).

RC50003

Not
                                          						Ready Time spent in 50003; the agent was logged out because the Unified CM
                                          						reported the agent's device as out of service.

RC50004

Not
                                          						Ready Time spent in 50004; the agent was logged out due to agent inactivity as
                                          						configured in agent desk settings.

RC50010

Not
                                          						Ready Time spent in 50010; the agent did not receive multiple consecutive tasks
                                          						routed to him/her. The system makes the agent Not Ready automatically so that
                                          						additional tasks are not routed to the agent. By default, the number of
                                          						consecutive tasks missed before the agent is made Not Ready is two.

RC50020

Not
                                          						Ready Time spent in 50020; for deskilling operations on active agents, the
                                          						agent was logged out of the skill group due to a deskilling operation that
                                          						removed the skill group assignment to that agent. This reason code is used in
                                          						the Agent_Event_Detail record and the Agent_Skill_Group_Logout record to
                                          						identify the skill group the agent was removed from (due to the deskilling
                                          						operation).

RC50030

Not
                                          						Ready Time spent in 50030; the agent was logged out because the agent was
                                          						logged into a dynamic device target that was using the same dialed number (DN)
                                          						as the PG static device target.

RC50040

Not
                                          						Ready Time spent in 50040; the mobile agent was logged out because the task
                                          						failed.

RC50041

Not
                                          						Ready Time spent in 50041; the agent's state was changed to Not Ready because
                                          						the task failed when the agent's phone line rings busy.

RC50042

Not
                                          						Ready Time spent in 50042; the mobile agent was logged out because the phone
                                          						line is connected when using nailed connection mode.

RC32767

Not
                                          						Ready Time spent in 32767; the agent's state was changed to Not Ready because
                                          						the agent did not answer a task and the task was redirected to a different
                                          						agent or skill group.

RC20001

Not
                                          						Ready Time spent in 20001; the agent's state was changed to Not Ready and the
                                          						agent was forcibly logged out.

RC20002

Not Ready Time spent in 20002; the general logout reason code condition from Not Ready.

RC20003

Not
                                          						Ready Time spent in 20003; the agent is not in Not Ready state. A request is
                                          						made to place the agent in Not Ready state and then a logout request is made to
                                          						log the agent out.

Report
                                 			 Summary: This report has a report summary for all data.

## Agent Not Ready
                        	 Detail

Use this report to identify how
                              				agents spend their time when they are not handling contacts. Not Ready reason codes
                              				can be used for agents to identify this time by using numeric codes to identify
                              				Break, Training, or Follow up for example. You can use this report to identify which
                              				Not Ready states agents use and how much time agents spend in each of them.

Query: This report data is
                              				built from an Anonymous Block.

Views: This report only has one grid view, Agent Not Ready Detail.

Grouping: This report is
                              				grouped and sorted by Agent and then by Logon Date Time.

Value List: Agent

Database Schema Tables from
                              				which data is retrieved:

Agent

Agent_Event_Detail

Media_Routing_Domain

Person

Reason_Code

The report summarizes states by
                              				login date time. You might see one row for an agent's entire login session rather
                              				than individual rows for each state change.

An agent can have multiple records for each LogOnDateTime, including one for each MRD (such as voice or email and chat) the
                              agent logged into.

To report on Agent Not Ready reason codes, configure the Not Ready Reason codes on the agent desktop software and in either
                                          the ICM Configuration manager (for Unified CCE ) or Unified CCE Administration (for Packaged CCE) .

In a Unified CCE environment, ensure that agent event detail is enabled on the peripheral. It is enabled by default in the ICM Configuration
                              Manager only for the Unified CCE peripheral.

### Available Fields in the Agent Not Ready Detail Grid View

Available fields for this report include the fields that
                                 appear by default as Current. Additional Available fields in this
                                 report are:

EndDate This field is a calculated field derived from
                                       the SQL query.

Reason Code Derived from
                                       Reason_Code.ReasonCodeName (if reason code text is configured) and
                                       Agent_Event_Detail.ReasonCode.

Skill Target ID Derived from:
                                       Agent_Event_Detail.skilltargetid.

StartDate This field is a calculated field derived from
                                       the SQL query.

Total Time Not Ready This field is a calculated field
                                       derived from the SQL query.

### Current Fields in the Agent Not Ready Detail Grid View

Current fields are those fields that appear by default in
                                 a report generated from the stock template.

Current fields are listed below in the order (left to right) in which they
                                 appear by default in the stock template.

Column (Field)

Description

Agent

The first and last name of the agent.

Derived from: Person.LastName ","
                                             Person.FirstName

Log On Date Time

The date and time the agent logged in, measured in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hours,
                                             minutes, seconds) format.

This field is a calculated field derived from
                                             Agent_Event_Detail.LoginDateTime.

Log On Duration

The amount of time the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field derived from
                                             ( Agent_Event_Detail.LoginDuration).

Reason Code

A code and text (if configured) from the peripheral
                                             that indicates the reason for the agent's last state
                                             change. If it is not defined, the reason code displays 0.

This field is a calculated field derived from
                                             Reason_Code.ReasonCodeName (if reason code text is
                                             configured) and Agent_Event_Detail.ReasonCode.

Duration

The amount of time in HH:MM:SS (hours, minutes,
                                             seconds) that the agent spent in the Not Ready state for
                                             the given reason.

Derived from Agent_Event_Detail.Duration.

% Log On Duration

The percent of the agent's total login session that
                                             the agent spent in the Not Ready state for the given
                                             reason.

Derived from
                                             Agent_Event_Detail.Duration / Agent_Event_Detail.LoginDuration.

% Not Ready

The percentage of time an agent spent in each Not
                                             Ready state relative to the other Not Ready states.

This field is a calculated field derived from 
                                             (Agent_Event_Detail.Duration / (sum of
                                             Agent_Event_Detail.Duration for all not ready reason
                                             codes)).

Report Summary: This report has a summary row for Agent and a report
                                 summary for all data. For more information, see Report Summary Rows .

### Available Fields in the Agent Not Ready Detail Grid View

Available fields for this report include the fields that
                                 appear by default as Current. Additional Available fields in this
                                 report are:

EndDate This field is a calculated field derived from
                                       the SQL query.

Reason Code Derived from
                                       Reason_Code.ReasonCodeName (if reason code text is configured) and
                                       Agent_Event_Detail.ReasonCode.

Skill Target ID Derived from:
                                       Agent_Event_Detail.skilltargetid.

StartDate This field is a calculated field derived from
                                       the SQL query.

Total Time Not Ready This field is a calculated field
                                       derived from the SQL query.

### Current Fields in the Agent Not Ready Detail Grid View

Current fields are those fields that appear by default in
                                 a report generated from the stock template.

Current fields are listed below in the order (left to right) in which they
                                 appear by default in the stock template.

Column (Field)

Description

Agent

The first and last name of the agent.

Derived from: Person.LastName ","
                                             Person.FirstName

Log On Date Time

The date and time the agent logged in, measured in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hours,
                                             minutes, seconds) format.

This field is a calculated field derived from
                                             Agent_Event_Detail.LoginDateTime.

Log On Duration

The amount of time the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field derived from
                                             ( Agent_Event_Detail.LoginDuration).

Reason Code

A code and text (if configured) from the peripheral
                                             that indicates the reason for the agent's last state
                                             change. If it is not defined, the reason code displays 0.

This field is a calculated field derived from
                                             Reason_Code.ReasonCodeName (if reason code text is
                                             configured) and Agent_Event_Detail.ReasonCode.

Duration

The amount of time in HH:MM:SS (hours, minutes,
                                             seconds) that the agent spent in the Not Ready state for
                                             the given reason.

Derived from Agent_Event_Detail.Duration.

% Log On Duration

The percent of the agent's total login session that
                                             the agent spent in the Not Ready state for the given
                                             reason.

Derived from
                                             Agent_Event_Detail.Duration / Agent_Event_Detail.LoginDuration.

% Not Ready

The percentage of time an agent spent in each Not
                                             Ready state relative to the other Not Ready states.

This field is a calculated field derived from 
                                             (Agent_Event_Detail.Duration / (sum of
                                             Agent_Event_Detail.Duration for all not ready reason
                                             codes)).

Report Summary: This report has a summary row for Agent and a report
                                 summary for all data. For more information, see Report Summary Rows .

## Agent Precision Queue Historical All Fields

Use this report to review the outcome of calls by Precision Queue and agent state percentages per Precision Queue.  This report
                              is comparable to the Agent Skill Group Historical report.

Views: This report has one grid view, Agent Precision Queue Historical All Fields.

Grouping: This report is grouped and sorted by Precision
                              Queue and then by Agent.

Value Lists: Precision Queue, Media Routing Domain

Database Schema Tables from which data is retrieved:

Agent

Agent_Interval

Agent_Skill_Group_Interval

Attribute

Media_Routing_Domain

Person

Precision_Queue

### Available Fields in the  Agent Precision Queue Historical All Fields Grid View

Available fields for this report include the fields that display by default as Current.

In addition to the fields that display by default as Current, most Available fields in this report are derived from the Agent_Interval
                                 and Agent_Skill_Group_Interval tables.

Handled is derived from  CallsHandled in the Agent_Skill_Group_Interval table.

Handled is the number of inbound calls for which agents in the precision queue during the interval answered and completed
                                 wrap-up.

All fields, excluding one, take their value directly from the database.

### Current Fields in
                           	 the Agent Precision Queue Historical All Fields Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                          					 (Field)

Description

Precision Queue

The
                                          					 enterprise name of the Agent Precision Queue.

Derived
                                          					 from Precision_Queue.EnterpriseName

Agent

The
                                          					 first and last name of the agent.

This field
                                          					 is a calculated field, derived from Person.LastName+","+Person.Firstname.

Media

The enterprise name of the Media Routing Domain associated with the agent.

Media is derived from:
                                          				Media_Routing_Domain.EnterpriseName.

DateTime

The date
                                          					 and time of the data for a selected row.

Derived
                                          					 from Agent_Skill_Group_Interval.DateTime.

Attributes

The
                                          					 attributes used in the precision queue definition. The report shows only those
                                          					 attributes that are used.

COMPLETED TASKS

Handled

The
                                          					 number of inbound calls for which agents in the precision queue during the
                                          					 interval answered and completed.

Derived
                                          					 from Agent_Skill_Group_Interval. CallsHandled

Avg Handle Time

This is a
                                          					 calculated field, derived from: Agent_Skill_Group_Interval.HandledCallsTime /
                                          					 Agent_Skill_Group_Interval.CallsHandled

The
                                          					 average time spent by the agent in handling a task in the interval, measured in
                                          					 HH:MM:SS (hours, minutes, seconds).

Held

The
                                          					 number of incoming calls to this agent that are placed on hold in the interval.

Derived
                                          					 from Agent_Skill_Group_Interval.IncomingCallsOnHold

Avg Hold Time

The
                                          					 average time in HH:MM:SS (hours, minutes, seconds) for calls placed on hold in
                                          					 the interval, for all incoming calls which include hold time.

This field
                                          					 is a calculated field, derived from (Agent_Skill_Group_Interval.
                                          					 IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.IncomingCallsOnHold)

Abandon Ring

For
                                          					 voice: The total number of calls that are abandoned while the agent phone is
                                          					 ringing.

For
                                          					 non-voice: The total number of tasks that are abandoned when offered to an
                                          					 agent.

Derived
                                          					 from Agent_Skill_Group_Interval.AbandonRingCalls

RONA

The
                                          					 number of tasks that left the agent phone or terminal that are redirected to
                                          					 another dialed number because of no answer in the interval.

Derived
                                          					 from Agent_Skill_Group_Interval.RedirectNoAnsCalls

Abandon Hold

The number of Unified ICM routed calls to the agent that are abandoned while the call is on hold and the number of paused tasks that the agent ended in the
                                          interval.

Derived
                                          					 from Agent_Skill_Group_Interval.AbandonHoldCalls

Transfer In

The
                                          					 number of incoming calls that are transferred to this agent from other agents
                                          					 within the same peripheral that do not go to VRU for queuing in the interval.
                                          					 This value is updated when the agent completes the call.

For blind transfers in Unified CCE with a Unified CCE System PG, this field is updated when the call that is blind transferred to a VRU is later transferred to another agent and
                                          the agent answers the call. For this call scenario this field is not updated in Unified CCE without a Unified CCE System PG.

Derived
                                          					 from Agent_Skill_Group_Interval.TransferredInCalls

Transfer Out

The
                                          					 number of calls this agent transferred to another agent or precision queue in
                                          					 the interval. This number includes consultative calls if this transfer was
                                          					 consultative-not blind. The value is updated at the time the agent completes
                                          					 the transfer of the call.

This field
                                          					 is a calculated field, derived from
                                          					 Agent_Skill_Group_Interval.TransferredOutCalls +
                                          					 Agent_Skill_Group_Interval.NetTransferredOutCalls

External Out

The
                                          					 number of outgoing external calls that this agent made in the interval.

Derived
                                          					 from Agent_Skill_Group_Interval.AgentOutCalls

Agent State Times

Logged On Time

The
                                          					 total time during the interval the agent was logged in, measured in HH:MM:SS
                                          					 (hours, minutes, seconds) format.

Derived
                                          					 from Agent_Interval.LoggedOnTime

% Active

The
                                          					 percentage of time that the agent spent talking on calls in this precision
                                          					 queue in relation to LoggedOnTime.

This field
                                          					 is a calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime +
                                          					 Agent_Skill_Group_Interval.TalkOutTime +
                                          					 Agent_Skill_Group_Interval.TalkOtherTime +
                                          					 Agent_Skill_Group_Interval.TalkAutoOutTime +
                                          					 Agent_Skill_Group_Interval.TalkPreviewTime +
                                          					 Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime

% Hold

The
                                          					 percentage of time that the agent put a call on hold or paused a task in
                                          					 relation to LoggedOnTime or the interval, whichever is less.

This field
                                          					 is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime /
                                          					 Agent_Interval.LoggedOnTimeTime

% Not
                                          					 Active

The
                                          					 percentage of time that the agent spent in the NotActive or Available state in
                                          					 relation to LoggedOnTime. This field applies to all precision queues.

This field
                                          					 is a calculated field derived from Agent_Interval.AvailTime /
                                          					 Agent_Interval.LoggedOnTime

% Not
                                          					 Ready

The
                                          					 percentage of time that the agent spent in the NotReady state in relation to
                                          					 LoggedOnTime or the interval, whichever is less. This field applies to all
                                          					 precision queues.

This
                                          					 field is a calculated field, derived from Agent_Interval.NotReadyTime /
                                          					 Agent_Interval.LoggedOnTime

%
                                          					 Reserved

The percentage of time that the agent spent in the Reserved state waiting for a n ICM routed task from this precision queue in relation to LoggedOnTime.

This
                                          					 field is a calculated field, derived from
                                          					 Agent_Skill_Group_Interval.ReservedStateTime / Agent_Interval.LoggedOnTime

% Wrap
                                          					 Up

The
                                          					 percentage of time that the agent spent in the Wrap-up state after an incoming
                                          					 or outgoing call to or from this precision queue in relation to LoggedOnTime.

The
                                          					 agent state time percentages in the Report Summary row add up to 100 percent
                                          					 only when you select all the precision queues for an agent. When you view a
                                          					 subset of precision queues for an agent, the percentages may not balance.

This
                                          					 field is a calculated field, derived from
                                          					 (Agent_Skill_Group_Interval.WorkReadyTime +
                                          					 Agent_Skill_Group_Interval.WorkNotReadyTime) / Agent_Interval.LoggedOnTime

Report Summary: There
                                 		  is a summary for Precision Queue Name and a report summary for all data. See Report Summary Rows .

### Available Fields in the  Agent Precision Queue Historical All Fields Grid View

Available fields for this report include the fields that display by default as Current.

In addition to the fields that display by default as Current, most Available fields in this report are derived from the Agent_Interval
                                 and Agent_Skill_Group_Interval tables.

Handled is derived from  CallsHandled in the Agent_Skill_Group_Interval table.

Handled is the number of inbound calls for which agents in the precision queue during the interval answered and completed
                                 wrap-up.

All fields, excluding one, take their value directly from the database.

### Current Fields in
                           	 the Agent Precision Queue Historical All Fields Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                          					 (Field)

Description

Precision Queue

The
                                          					 enterprise name of the Agent Precision Queue.

Derived
                                          					 from Precision_Queue.EnterpriseName

Agent

The
                                          					 first and last name of the agent.

This field
                                          					 is a calculated field, derived from Person.LastName+","+Person.Firstname.

Media

The enterprise name of the Media Routing Domain associated with the agent.

Media is derived from:
                                          				Media_Routing_Domain.EnterpriseName.

DateTime

The date
                                          					 and time of the data for a selected row.

Derived
                                          					 from Agent_Skill_Group_Interval.DateTime.

Attributes

The
                                          					 attributes used in the precision queue definition. The report shows only those
                                          					 attributes that are used.

COMPLETED TASKS

Handled

The
                                          					 number of inbound calls for which agents in the precision queue during the
                                          					 interval answered and completed.

Derived
                                          					 from Agent_Skill_Group_Interval. CallsHandled

Avg Handle Time

This is a
                                          					 calculated field, derived from: Agent_Skill_Group_Interval.HandledCallsTime /
                                          					 Agent_Skill_Group_Interval.CallsHandled

The
                                          					 average time spent by the agent in handling a task in the interval, measured in
                                          					 HH:MM:SS (hours, minutes, seconds).

Held

The
                                          					 number of incoming calls to this agent that are placed on hold in the interval.

Derived
                                          					 from Agent_Skill_Group_Interval.IncomingCallsOnHold

Avg Hold Time

The
                                          					 average time in HH:MM:SS (hours, minutes, seconds) for calls placed on hold in
                                          					 the interval, for all incoming calls which include hold time.

This field
                                          					 is a calculated field, derived from (Agent_Skill_Group_Interval.
                                          					 IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.IncomingCallsOnHold)

Abandon Ring

For
                                          					 voice: The total number of calls that are abandoned while the agent phone is
                                          					 ringing.

For
                                          					 non-voice: The total number of tasks that are abandoned when offered to an
                                          					 agent.

Derived
                                          					 from Agent_Skill_Group_Interval.AbandonRingCalls

RONA

The
                                          					 number of tasks that left the agent phone or terminal that are redirected to
                                          					 another dialed number because of no answer in the interval.

Derived
                                          					 from Agent_Skill_Group_Interval.RedirectNoAnsCalls

Abandon Hold

The number of Unified ICM routed calls to the agent that are abandoned while the call is on hold and the number of paused tasks that the agent ended in the
                                          interval.

Derived
                                          					 from Agent_Skill_Group_Interval.AbandonHoldCalls

Transfer In

The
                                          					 number of incoming calls that are transferred to this agent from other agents
                                          					 within the same peripheral that do not go to VRU for queuing in the interval.
                                          					 This value is updated when the agent completes the call.

For blind transfers in Unified CCE with a Unified CCE System PG, this field is updated when the call that is blind transferred to a VRU is later transferred to another agent and
                                          the agent answers the call. For this call scenario this field is not updated in Unified CCE without a Unified CCE System PG.

Derived
                                          					 from Agent_Skill_Group_Interval.TransferredInCalls

Transfer Out

The
                                          					 number of calls this agent transferred to another agent or precision queue in
                                          					 the interval. This number includes consultative calls if this transfer was
                                          					 consultative-not blind. The value is updated at the time the agent completes
                                          					 the transfer of the call.

This field
                                          					 is a calculated field, derived from
                                          					 Agent_Skill_Group_Interval.TransferredOutCalls +
                                          					 Agent_Skill_Group_Interval.NetTransferredOutCalls

External Out

The
                                          					 number of outgoing external calls that this agent made in the interval.

Derived
                                          					 from Agent_Skill_Group_Interval.AgentOutCalls

Agent State Times

Logged On Time

The
                                          					 total time during the interval the agent was logged in, measured in HH:MM:SS
                                          					 (hours, minutes, seconds) format.

Derived
                                          					 from Agent_Interval.LoggedOnTime

% Active

The
                                          					 percentage of time that the agent spent talking on calls in this precision
                                          					 queue in relation to LoggedOnTime.

This field
                                          					 is a calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime +
                                          					 Agent_Skill_Group_Interval.TalkOutTime +
                                          					 Agent_Skill_Group_Interval.TalkOtherTime +
                                          					 Agent_Skill_Group_Interval.TalkAutoOutTime +
                                          					 Agent_Skill_Group_Interval.TalkPreviewTime +
                                          					 Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime

% Hold

The
                                          					 percentage of time that the agent put a call on hold or paused a task in
                                          					 relation to LoggedOnTime or the interval, whichever is less.

This field
                                          					 is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime /
                                          					 Agent_Interval.LoggedOnTimeTime

% Not
                                          					 Active

The
                                          					 percentage of time that the agent spent in the NotActive or Available state in
                                          					 relation to LoggedOnTime. This field applies to all precision queues.

This field
                                          					 is a calculated field derived from Agent_Interval.AvailTime /
                                          					 Agent_Interval.LoggedOnTime

% Not
                                          					 Ready

The
                                          					 percentage of time that the agent spent in the NotReady state in relation to
                                          					 LoggedOnTime or the interval, whichever is less. This field applies to all
                                          					 precision queues.

This
                                          					 field is a calculated field, derived from Agent_Interval.NotReadyTime /
                                          					 Agent_Interval.LoggedOnTime

%
                                          					 Reserved

The percentage of time that the agent spent in the Reserved state waiting for a n ICM routed task from this precision queue in relation to LoggedOnTime.

This
                                          					 field is a calculated field, derived from
                                          					 Agent_Skill_Group_Interval.ReservedStateTime / Agent_Interval.LoggedOnTime

% Wrap
                                          					 Up

The
                                          					 percentage of time that the agent spent in the Wrap-up state after an incoming
                                          					 or outgoing call to or from this precision queue in relation to LoggedOnTime.

The
                                          					 agent state time percentages in the Report Summary row add up to 100 percent
                                          					 only when you select all the precision queues for an agent. When you view a
                                          					 subset of precision queues for an agent, the percentages may not balance.

This
                                          					 field is a calculated field, derived from
                                          					 (Agent_Skill_Group_Interval.WorkReadyTime +
                                          					 Agent_Skill_Group_Interval.WorkNotReadyTime) / Agent_Interval.LoggedOnTime

Report Summary: There
                                 		  is a summary for Precision Queue Name and a report summary for all data. See Report Summary Rows .

## Agent Queue Interval

Use this report to show call dispositions and state time percentages for agents who have been assigned both skills and precision
                              queues.

Query: This report
                              data is built from an Anonymous Block.

Views: This report has one grid view, Agent Queue Interval.

Grouping: This template is grouped by agent name and then by
                              Skill Group or Precision Queue.

Value List: Agent

Database Schema Tables from which data is retrieved:

Agent

Agent_Interval

Agent_Skill_Group_Interval

Attribute

Media_Routing_Domain

Person

Precision Queue

Skill_Group

### Current Fields in
                           	 the Agent Queue Interval Grid View

Current fields
                                 		  are those fields that appear by default in a grid view generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear
                                 		  by default in the stock template.

Column
                                             						(Field)

Description

Agent

The first
                                             						and last name of the agent.

This field is a
                                             						calculated field, derived from Person.LastName+ "," +Person.FirstName.

Precision Queue / Skill Group

The
                                             						enterprise name for the skill group or agent precision queue. You can identify
                                             						a precision queue by the presence of Attributes next to the queue name.

Derived
                                             						from Skill_Group.EnterpriseName or Precision_Queue.EnterpriseName

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

DateTime

The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format.

Derived
                                             						from Agent_Skill_Group_Interval.DateTime.

COMPLETED TASKS

Handled

The number
                                             						of inbound calls that were answered and have completed wrap-up by agents in the
                                             						skill group during the interval.

Derived
                                             						from  CallsHandled in the Agent_Skill_Group_Interval table.

Avg Handle Time

The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds).

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime /
                                             						Agent_Skill_Group_Interval.CallsHandled).

Held

The number
                                             						of incoming calls to this agent that were placed on hold in the interval.

Derived
                                             						from Agent_Skill_Group_Interval.IncomingCallsOnHold.

Avg Hold Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold
                                             						in the interval, for all incoming calls which included hold time.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.
                                             						IncomingCallsOnHoldTime / Agent_Skill_Group_Interval. IncomingCallsOnHold).

Abandon Rings

For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing.

For
                                             						non-voice: the total number of tasks that were abandoned while being offered to
                                             						an agent.

Derived
                                             						from: Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer in the interval.

Derived
                                             						from Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval.

Derived
                                             						from Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing in the interval. This
                                             						value is updated when the agent completes the call.

For blind transfers in the Unified CCE with a Unified CCE System PG, this field is updated when the call that was blind transferred to an Interactive Voice Response (IVR) is later
                                             transferred to another agent and the agent answers the call. For this call scenario, this field is not updated in Unified CCE without a Unified CCE System PG.

Derived
                                             						from Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number
                                             						of calls this agent transferred to another agent or skill group in the
                                             						interval. This includes Consultative Calls if this transfer was
                                             						consultative-not blind. The value is updated at the time the agent completes
                                             						the transfer of the call.

This field is a
                                             						calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls
                                             						+ Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number
                                             						of outgoing external calls that this agent made in the interval.

Derived
                                             						from Agent_Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIMES

Logged On Time

The total
                                             						time during the interval the agent was logged in, measured in HH:MM:SS (hours,
                                             						minutes, seconds) format.

Derived
                                             						from  Agent_Interval.LoggedOnTime.

% Active

The
                                             						percentage of time that the agent spent talking on calls in this skill group in
                                             						relation to the agent's LoggedOnTime.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime +
                                             						Agent_Skill_Group_Interval.TalkOutTime +
                                             						Agent_Skill_Group_Interval.TalkOtherTime +
                                             						Agent_Skill_Group_Interval.TalkAutoOutTime +
                                             						Agent_Skill_Group_Interval.TalkPreviewTime +
                                             						Agent_Skill_Group_Interval.TalkReserveTime) /
                                             						 Agent_Interval.LoggedOnTime.

% Hold

The
                                             						percentage of time that the agent has put a call on hold or paused a task in
                                             						relation to LoggedOnTime or the interval, whichever is less.

This field is a
                                             						calculated field, derived from Agent_Skill_Group_Interval.HoldTime /
                                             						Agent_Interval.LoggedOnTimeTime.

% Not
                                             						Active

The
                                             						percentage of time that the agent spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. Applies to all skill groups.

This field is a
                                             						calculated field derived from (Agent_Interval.AvailTime
                                             						/Agent_Interval.LoggedOnTime).

% Not
                                             						Ready

The
                                             						percentage of time that the agent spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Applies to all skill groups.

This field is a
                                             						calculated field, derived from: (Agent_Interval.NotReadyTime /
                                             						Agent_Interval.LoggedOnTime).

% Reserved

The
                                             						percentage of time that the agent spent in Reserved state waiting for a task
                                             						from this skill group in relation to LoggedOnTime.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.ReservedStateTime
                                             						/ Agent_Interval.LoggedOnTime).

% Wrap Up

The
                                             						percentage of time that the agent spent in Wrap-up state after an incoming or
                                             						outgoing call to or from this skill group in relation to LoggedOnTime.

The agent state time percentages in the Report Summary row
                                             						add up  to 100 percent only after you select all the skill groups for an agent. When
                                             						viewing a subset of an agent's skill groups, the percentages may not balance.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime
                                             						+Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             						/ Agent_Interval.LoggedOnTime.

Report Summary: There is
                                 		  a summary for all data. See Report Summary Rows .

### Current Fields in
                           	 the Agent Queue Interval Grid View

Current fields
                                 		  are those fields that appear by default in a grid view generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear
                                 		  by default in the stock template.

Column
                                             						(Field)

Description

Agent

The first
                                             						and last name of the agent.

This field is a
                                             						calculated field, derived from Person.LastName+ "," +Person.FirstName.

Precision Queue / Skill Group

The
                                             						enterprise name for the skill group or agent precision queue. You can identify
                                             						a precision queue by the presence of Attributes next to the queue name.

Derived
                                             						from Skill_Group.EnterpriseName or Precision_Queue.EnterpriseName

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

DateTime

The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format.

Derived
                                             						from Agent_Skill_Group_Interval.DateTime.

COMPLETED TASKS

Handled

The number
                                             						of inbound calls that were answered and have completed wrap-up by agents in the
                                             						skill group during the interval.

Derived
                                             						from  CallsHandled in the Agent_Skill_Group_Interval table.

Avg Handle Time

The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds).

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime /
                                             						Agent_Skill_Group_Interval.CallsHandled).

Held

The number
                                             						of incoming calls to this agent that were placed on hold in the interval.

Derived
                                             						from Agent_Skill_Group_Interval.IncomingCallsOnHold.

Avg Hold Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold
                                             						in the interval, for all incoming calls which included hold time.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.
                                             						IncomingCallsOnHoldTime / Agent_Skill_Group_Interval. IncomingCallsOnHold).

Abandon Rings

For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing.

For
                                             						non-voice: the total number of tasks that were abandoned while being offered to
                                             						an agent.

Derived
                                             						from: Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer in the interval.

Derived
                                             						from Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval.

Derived
                                             						from Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing in the interval. This
                                             						value is updated when the agent completes the call.

For blind transfers in the Unified CCE with a Unified CCE System PG, this field is updated when the call that was blind transferred to an Interactive Voice Response (IVR) is later
                                             transferred to another agent and the agent answers the call. For this call scenario, this field is not updated in Unified CCE without a Unified CCE System PG.

Derived
                                             						from Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number
                                             						of calls this agent transferred to another agent or skill group in the
                                             						interval. This includes Consultative Calls if this transfer was
                                             						consultative-not blind. The value is updated at the time the agent completes
                                             						the transfer of the call.

This field is a
                                             						calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls
                                             						+ Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number
                                             						of outgoing external calls that this agent made in the interval.

Derived
                                             						from Agent_Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIMES

Logged On Time

The total
                                             						time during the interval the agent was logged in, measured in HH:MM:SS (hours,
                                             						minutes, seconds) format.

Derived
                                             						from  Agent_Interval.LoggedOnTime.

% Active

The
                                             						percentage of time that the agent spent talking on calls in this skill group in
                                             						relation to the agent's LoggedOnTime.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime +
                                             						Agent_Skill_Group_Interval.TalkOutTime +
                                             						Agent_Skill_Group_Interval.TalkOtherTime +
                                             						Agent_Skill_Group_Interval.TalkAutoOutTime +
                                             						Agent_Skill_Group_Interval.TalkPreviewTime +
                                             						Agent_Skill_Group_Interval.TalkReserveTime) /
                                             						 Agent_Interval.LoggedOnTime.

% Hold

The
                                             						percentage of time that the agent has put a call on hold or paused a task in
                                             						relation to LoggedOnTime or the interval, whichever is less.

This field is a
                                             						calculated field, derived from Agent_Skill_Group_Interval.HoldTime /
                                             						Agent_Interval.LoggedOnTimeTime.

% Not
                                             						Active

The
                                             						percentage of time that the agent spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. Applies to all skill groups.

This field is a
                                             						calculated field derived from (Agent_Interval.AvailTime
                                             						/Agent_Interval.LoggedOnTime).

% Not
                                             						Ready

The
                                             						percentage of time that the agent spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Applies to all skill groups.

This field is a
                                             						calculated field, derived from: (Agent_Interval.NotReadyTime /
                                             						Agent_Interval.LoggedOnTime).

% Reserved

The
                                             						percentage of time that the agent spent in Reserved state waiting for a task
                                             						from this skill group in relation to LoggedOnTime.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.ReservedStateTime
                                             						/ Agent_Interval.LoggedOnTime).

% Wrap Up

The
                                             						percentage of time that the agent spent in Wrap-up state after an incoming or
                                             						outgoing call to or from this skill group in relation to LoggedOnTime.

The agent state time percentages in the Report Summary row
                                             						add up  to 100 percent only after you select all the skill groups for an agent. When
                                             						viewing a subset of an agent's skill groups, the percentages may not balance.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime
                                             						+Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             						/ Agent_Interval.LoggedOnTime.

Report Summary: There is
                                 		  a summary for all data. See Report Summary Rows .

## Agent Queue
                        	 Hourly

Use this report to
                              		  show call dispositions and state time percentages for agents who have been
                              		  assigned both skills and precision queues.

Query : This
                              		  report data is built from an Anonymous Block.

Views : This report has one grid view, Agent Queue Hourly.

Grouping : This template
                              		  does not support grouping.

Value List : Agent

Database Schema Tables from which data is retrieved:

Agent

Agent_Interval

Agent_Skill_Group_Interval

Attribute

Media_Routing_Domain

Person

Precision Queue

Skill_Group

Note : The data is
                              		  summarized to hourly boundaries instead of 15 or 30-minutes interval
                              		  boundaries.

### Current Fields in
                           	 the Agent Queue Hourly Grid View

Current fields
                                 		  are those fields that appear by default in a grid view generated from the stock
                                 		  template.

Current fields
                                 		  are listed here in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column (Field)

Description

Agent

The first and last name of the agent.

This field is a calculated field, derived from Person.LastName+ "," +Person.FirstName.

Precision Queue /Skill Group

The enterprise name for the skill group or agent precision queue. You can identify a precision queue by the presence of Attributes
                                             next to the queue name.

Derived from Skill_Group.EnterpriseName or Precision_Queue.EnterpriseName.

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format.

Derived from Agent_Skill_Group_Interval.DateTime.

COMPLETED TASKS

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the skill group during the interval.

Derived from CallsHandled in the Agent_Skill_Group_Interval table.

Average Handle Time

The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds).

This field is a calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime / Agent_Skill_Group_Interval.CallsHandled).

Held

The number of incoming calls to this agent that are placed on hold in the interval.

Derived from Agent_Skill_Group_Interval.IncomingCallsOnHold

Average Hold Time

The average time in HH:MM:SS (hours, minutes, seconds)during which the calls were put on hold in the interval, for all incoming
                                             calls that included hold time.

This field is a calculated field, derived from (Agent_Skill_Group_Interval. IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.
                                             IncomingCallsOnHold).

Abandon Rings

For voice: the total number of calls that were abandoned while the agent's phone was ringing.

For non-voice: the total number of tasks that were abandoned while being offered to an agent.

Derived from: Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number of tasks that left the agent's phone or terminal that were redirected to another dialed number because of no answer
                                             in the interval.

Derived from Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in the
                                             interval.

Derived from Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number of incoming calls that were transferred to this agent from other agents within the same peripheral that did not
                                             go to IVR for queuing in the interval. This value is updated when the agent completes the call.

For blind transfers in the Unified CCE with a Unified CCE System PG, this field is updated when the call that was blind transferred to an IVR is later transferred to another agent
                                             and the agent answers the call. For this call scenario, this field is not updated in Unified CCE without a Unified CCE System PG.

Derived from Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number of calls this agent transferred to another agent or skill group in the interval. This includes Consultative Calls
                                             if this transfer was consultative-not blind. The value is updated at the time the agent completes the transfer of the call.

This field is a calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls + Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number of outgoing external calls that this agent made in the interval.

Derived from Agent_Skill_Group_Interval.AgentOutCalls.

Agent State Times

Logged On Time

The total time during the interval the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format.

Derived from Agent_Interval.LoggedOnTime.

% Active

The percentage of time that the agent spent talking on calls in this skill group in relation to the agent's LoggedOnTime.

This field is a calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime + Agent_Skill_Group_Interval.TalkOutTime
                                             + Agent_Skill_Group_Interval.TalkOtherTime + Agent_Skill_Group_Interval.TalkAutoOutTime + Agent_Skill_Group_Interval.TalkPreviewTime
                                             + Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime

% Hold

The percentage of time that the agent has put a call on hold or paused a task in relation to LoggedOnTime or the interval,
                                             whichever is less.

This field is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime / Agent_Interval.LoggedOnTimeTime.

% Not Active

The percentage of time that the agent spent in the Not Active or Available state in relation to LoggedOnTime. Applies to
                                             all skill groups.

This field is a calculated field derived from (Agent_Interval.AvailTime /Agent_Interval.LoggedOnTime).

% Not Ready

The percentage of time that the agent spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever
                                             is less. Applies to all skill groups.

This field is a calculated field, derived from: (Agent_Interval.NotReadyTime / Agent_Interval.LoggedOnTime).

% Reserved

The percentage of time that the agent spent in Reserved state waiting for a task from this skill group in relation to LoggedOnTime.

This field is a calculated field, derived from (Agent_Skill_Group_Interval.ReservedStateTime / Agent_Interval.LoggedOnTime).

% Wrap Up

The percentage of time that the agent spent in Wrap-up state after an incoming or outgoing call to or from this skill group
                                             in relation to LoggedOnTime.

The agent state time percentages in the Report Summary row add up to 100 percent only after you select all the skill groups
                                             for an agent. When viewing a subset of an agent's skill groups, the percentages may not balance.

This field is a calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime +Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             / Agent_Interval.LoggedOnTime.

%Busy Other

The percentage of time that the agent spent in the Busy Other state by handling calls assigned to other skill group or precision
                                             queue in relation to LoggedOnTime.

This field is a calculated field, derived from Agent_Skill_Group_Interval.BusyOtherTime/Agent_Interval.LoggedOnTime.

There is a
                                 		  summary for all data. See Report
                                    			 Summary Rows .

### Current Fields in
                           	 the Agent Queue Hourly Grid View

Current fields
                                 		  are those fields that appear by default in a grid view generated from the stock
                                 		  template.

Current fields
                                 		  are listed here in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column (Field)

Description

Agent

The first and last name of the agent.

This field is a calculated field, derived from Person.LastName+ "," +Person.FirstName.

Precision Queue /Skill Group

The enterprise name for the skill group or agent precision queue. You can identify a precision queue by the presence of Attributes
                                             next to the queue name.

Derived from Skill_Group.EnterpriseName or Precision_Queue.EnterpriseName.

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format.

Derived from Agent_Skill_Group_Interval.DateTime.

COMPLETED TASKS

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the skill group during the interval.

Derived from CallsHandled in the Agent_Skill_Group_Interval table.

Average Handle Time

The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds).

This field is a calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime / Agent_Skill_Group_Interval.CallsHandled).

Held

The number of incoming calls to this agent that are placed on hold in the interval.

Derived from Agent_Skill_Group_Interval.IncomingCallsOnHold

Average Hold Time

The average time in HH:MM:SS (hours, minutes, seconds)during which the calls were put on hold in the interval, for all incoming
                                             calls that included hold time.

This field is a calculated field, derived from (Agent_Skill_Group_Interval. IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.
                                             IncomingCallsOnHold).

Abandon Rings

For voice: the total number of calls that were abandoned while the agent's phone was ringing.

For non-voice: the total number of tasks that were abandoned while being offered to an agent.

Derived from: Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number of tasks that left the agent's phone or terminal that were redirected to another dialed number because of no answer
                                             in the interval.

Derived from Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in the
                                             interval.

Derived from Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number of incoming calls that were transferred to this agent from other agents within the same peripheral that did not
                                             go to IVR for queuing in the interval. This value is updated when the agent completes the call.

For blind transfers in the Unified CCE with a Unified CCE System PG, this field is updated when the call that was blind transferred to an IVR is later transferred to another agent
                                             and the agent answers the call. For this call scenario, this field is not updated in Unified CCE without a Unified CCE System PG.

Derived from Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number of calls this agent transferred to another agent or skill group in the interval. This includes Consultative Calls
                                             if this transfer was consultative-not blind. The value is updated at the time the agent completes the transfer of the call.

This field is a calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls + Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number of outgoing external calls that this agent made in the interval.

Derived from Agent_Skill_Group_Interval.AgentOutCalls.

Agent State Times

Logged On Time

The total time during the interval the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format.

Derived from Agent_Interval.LoggedOnTime.

% Active

The percentage of time that the agent spent talking on calls in this skill group in relation to the agent's LoggedOnTime.

This field is a calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime + Agent_Skill_Group_Interval.TalkOutTime
                                             + Agent_Skill_Group_Interval.TalkOtherTime + Agent_Skill_Group_Interval.TalkAutoOutTime + Agent_Skill_Group_Interval.TalkPreviewTime
                                             + Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime

% Hold

The percentage of time that the agent has put a call on hold or paused a task in relation to LoggedOnTime or the interval,
                                             whichever is less.

This field is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime / Agent_Interval.LoggedOnTimeTime.

% Not Active

The percentage of time that the agent spent in the Not Active or Available state in relation to LoggedOnTime. Applies to
                                             all skill groups.

This field is a calculated field derived from (Agent_Interval.AvailTime /Agent_Interval.LoggedOnTime).

% Not Ready

The percentage of time that the agent spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever
                                             is less. Applies to all skill groups.

This field is a calculated field, derived from: (Agent_Interval.NotReadyTime / Agent_Interval.LoggedOnTime).

% Reserved

The percentage of time that the agent spent in Reserved state waiting for a task from this skill group in relation to LoggedOnTime.

This field is a calculated field, derived from (Agent_Skill_Group_Interval.ReservedStateTime / Agent_Interval.LoggedOnTime).

% Wrap Up

The percentage of time that the agent spent in Wrap-up state after an incoming or outgoing call to or from this skill group
                                             in relation to LoggedOnTime.

The agent state time percentages in the Report Summary row add up to 100 percent only after you select all the skill groups
                                             for an agent. When viewing a subset of an agent's skill groups, the percentages may not balance.

This field is a calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime +Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             / Agent_Interval.LoggedOnTime.

%Busy Other

The percentage of time that the agent spent in the Busy Other state by handling calls assigned to other skill group or precision
                                             queue in relation to LoggedOnTime.

This field is a calculated field, derived from Agent_Skill_Group_Interval.BusyOtherTime/Agent_Interval.LoggedOnTime.

There is a
                                 		  summary for all data. See Report
                                    			 Summary Rows .

## Agent Skill Group
                        	 Historical All Fields

Agent Skill Group
                              		  Historical All Fields shows call dispositions and agent state percentages
                              		  grouped by skill group and then agent.

Query: This report data
                              		  is built from an Anonymous Block type query.

Views: This report has one grid view, Agent Skill Group Historical All Fields.

Grouping: This report is grouped and sorted by Skill Group and then by Agent.

Value Lists: Skill Group, Media Routing Domain Database Schema Tables from which data is retrieved:

Agent

Agent_Interval

Agent_Skill_Group_Interval

Media_Routing_Domain

Skill_Group

Person

### Available Fields in the Agent Skill Group Historical All Fields Grid View

Available fields for this report include the fields that appear by
                                 default as Current.

In addition to the fields that appear by default as Current, most
                                 Available fields in this report are derived from the Agent_Interval and
                                 Agent_Skill_Group_Interval tables.

Handled is derived from  CallsHandled in the
                                 Agent_Skill_Group table.

Handled is the number of inbound calls that were answered and have
                                 completed wrap-up by agents in the skill group during the interval.

All fields but one take their value directly from the database.

The one exception is Wrap Time , which is a calculated
                                 field derived from: (Agent_Skill_Group_Interval.WorkNotReadyTime +
                                 Agent_Skill_Group_Interval.WorkReadyTime).

Wrap Time is the total time in HH:MM:SS (hours, minutes, seconds) that the
                                 agent spent in wrap-up on incoming and outgoing tasks in the interval.

### Current Fields in
                           	 the Agent Skill Group Historical All Fields Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Skill Group

The agent
                                             						skill group's enterprise name.

Derived
                                             						from Skill_Group.EnterpriseName.

Agent

The first
                                             						and last name of the agent.

This is a
                                             						calculated field, derived from  Person.LastName + ", " + Person.FirstName.

Media

The enterprise name of the Media Routing Domain associated with the agent.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

DateTime

The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format.

Derived
                                             						from Agent_Skill_Group_Interval.DateTime.

COMPLETED TASKS

Handled

The number
                                             						of inbound calls that were answered and have completed wrap-up by agents in the
                                             						skill group during the interval.

Derived
                                             						from  Agent_Skill_Group_Interval. CallsHandled.

Avg Handle Time

The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds).

This is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime /
                                             						Agent_Skill_Group_Interval.CallsHandled).

Held

The number
                                             						of incoming calls to this agent that were placed on hold in the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.IncomingCallsOnHold.

Avg Hold Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold
                                             						in the interval, for all incoming calls that included hold time.

This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.
                                             						IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.IncomingCallsOnHold).

Abandon Rings

For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing.

For
                                             						non-voice: the total number of tasks that were abandoned while being offered to
                                             						an agent.

Derived
                                             						from  Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer in the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval.

Derived
                                             						from Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing in the interval. This
                                             						value is updated when the agent completes the call.

For blind transfers in the Unified CCE with a Unified CCE System PG, this field updates when the call that was blind transferred to an IVR is later transferred to another agent and
                                             the agent answers the call. For this call scenario, this field is not updated in the Unified CCE without a Unified CCE System PG.

Derived
                                             						from  Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number
                                             						of calls this agent transferred to another agent or skill group in the
                                             						interval. This number includes Consultative Calls if this transfer was
                                             						consultative-not blind. The value is updated at the time the agent completes
                                             						the transfer of the call.

This field is a
                                             						calculated field, derived from: Agent_Skill_Group_Interval.TransferredOutCalls
                                             						+ Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number
                                             						of outgoing external calls that this agent made in the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIMES

Logged On Time

The total
                                             						time during the interval the agent was logged in, measured in HH:MM:SS (hours,
                                             						minutes, seconds) format.

Derived
                                             						from   Agent_Interval.LoggedOnTime.

% Active

The
                                             						percentage of time that the agent spent talking on calls in this skill group in
                                             						relation to the agent's LoggedOnTime.

This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.TalkInTime +
                                             						Agent_Skill_Group_Interval.TalkOutTime +
                                             						Agent_Skill_Group_Interval.TalkOtherTime +
                                             						Agent_Skill_Group_Interval.TalkAutoOutTime +
                                             						Agent_Skill_Group_Interval.TalkPreviewTime +
                                             						Agent_Skill_Group_Interval.TalkReserveTime) /
                                             						 Agent_Interval.LoggedOnTime.

% Hold

The
                                             						percentage of time that the agent put a call on hold or paused a task in
                                             						relation to LoggedOnTime or the interval, whichever is less.

This field  is a
                                             						calculated field, derived from  Agent_Skill_Group_Interval.HoldTime /
                                             						Agent_Interval.LoggedOnTimeTime.

% Not
                                             						Active

The
                                             						percentage of time that the agent spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. Applies to all skill groups.

This field is a
                                             						calculated field derived from  (Agent_Interval.
                                             						AvailTime/Agent_Interval.LoggedOnTime).

% Not
                                             						Ready

The
                                             						percentage of time that the agent spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Applies to all skill groups.

This field  is a
                                             						calculated field, derived from  (Agent_Interval.NotReadyTime /
                                             						Agent_Interval.LoggedOnTime).

% Reserved

The
                                             						percentage of time that the agent spent in Reserved state waiting for task from
                                             						this skill group in relation to LoggedOnTime.

This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.ReservedStateTime
                                             						/ Agent_Interval.LoggedOnTime).

% Wrap Up

The
                                             						percentage of time that the agent spent in Wrap-up state after an incoming or
                                             						outgoing call to/from this skill group in relation to LoggedOnTime.

The
                                             						agent state time percentages in the Report Summary row add up to 100 percent
                                             						only after you select all the skill groups for an agent. When you view a subset of an
                                             						agent's skill groups, you might notice that the percentages may not balance.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime
                                             						+Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             						/ Agent_Interval.LoggedOnTime.

Report Summary: There is a summary for Skill Group and a
                                 				report summary for all data. For more information, see Report Summary Rows .

### Available Fields in the Agent Skill Group Historical All Fields Grid View

Available fields for this report include the fields that appear by
                                 default as Current.

In addition to the fields that appear by default as Current, most
                                 Available fields in this report are derived from the Agent_Interval and
                                 Agent_Skill_Group_Interval tables.

Handled is derived from  CallsHandled in the
                                 Agent_Skill_Group table.

Handled is the number of inbound calls that were answered and have
                                 completed wrap-up by agents in the skill group during the interval.

All fields but one take their value directly from the database.

The one exception is Wrap Time , which is a calculated
                                 field derived from: (Agent_Skill_Group_Interval.WorkNotReadyTime +
                                 Agent_Skill_Group_Interval.WorkReadyTime).

Wrap Time is the total time in HH:MM:SS (hours, minutes, seconds) that the
                                 agent spent in wrap-up on incoming and outgoing tasks in the interval.

### Current Fields in
                           	 the Agent Skill Group Historical All Fields Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Skill Group

The agent
                                             						skill group's enterprise name.

Derived
                                             						from Skill_Group.EnterpriseName.

Agent

The first
                                             						and last name of the agent.

This is a
                                             						calculated field, derived from  Person.LastName + ", " + Person.FirstName.

Media

The enterprise name of the Media Routing Domain associated with the agent.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

DateTime

The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format.

Derived
                                             						from Agent_Skill_Group_Interval.DateTime.

COMPLETED TASKS

Handled

The number
                                             						of inbound calls that were answered and have completed wrap-up by agents in the
                                             						skill group during the interval.

Derived
                                             						from  Agent_Skill_Group_Interval. CallsHandled.

Avg Handle Time

The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds).

This is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime /
                                             						Agent_Skill_Group_Interval.CallsHandled).

Held

The number
                                             						of incoming calls to this agent that were placed on hold in the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.IncomingCallsOnHold.

Avg Hold Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold
                                             						in the interval, for all incoming calls that included hold time.

This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.
                                             						IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.IncomingCallsOnHold).

Abandon Rings

For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing.

For
                                             						non-voice: the total number of tasks that were abandoned while being offered to
                                             						an agent.

Derived
                                             						from  Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer in the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval.

Derived
                                             						from Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing in the interval. This
                                             						value is updated when the agent completes the call.

For blind transfers in the Unified CCE with a Unified CCE System PG, this field updates when the call that was blind transferred to an IVR is later transferred to another agent and
                                             the agent answers the call. For this call scenario, this field is not updated in the Unified CCE without a Unified CCE System PG.

Derived
                                             						from  Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number
                                             						of calls this agent transferred to another agent or skill group in the
                                             						interval. This number includes Consultative Calls if this transfer was
                                             						consultative-not blind. The value is updated at the time the agent completes
                                             						the transfer of the call.

This field is a
                                             						calculated field, derived from: Agent_Skill_Group_Interval.TransferredOutCalls
                                             						+ Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number
                                             						of outgoing external calls that this agent made in the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIMES

Logged On Time

The total
                                             						time during the interval the agent was logged in, measured in HH:MM:SS (hours,
                                             						minutes, seconds) format.

Derived
                                             						from   Agent_Interval.LoggedOnTime.

% Active

The
                                             						percentage of time that the agent spent talking on calls in this skill group in
                                             						relation to the agent's LoggedOnTime.

This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.TalkInTime +
                                             						Agent_Skill_Group_Interval.TalkOutTime +
                                             						Agent_Skill_Group_Interval.TalkOtherTime +
                                             						Agent_Skill_Group_Interval.TalkAutoOutTime +
                                             						Agent_Skill_Group_Interval.TalkPreviewTime +
                                             						Agent_Skill_Group_Interval.TalkReserveTime) /
                                             						 Agent_Interval.LoggedOnTime.

% Hold

The
                                             						percentage of time that the agent put a call on hold or paused a task in
                                             						relation to LoggedOnTime or the interval, whichever is less.

This field  is a
                                             						calculated field, derived from  Agent_Skill_Group_Interval.HoldTime /
                                             						Agent_Interval.LoggedOnTimeTime.

% Not
                                             						Active

The
                                             						percentage of time that the agent spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. Applies to all skill groups.

This field is a
                                             						calculated field derived from  (Agent_Interval.
                                             						AvailTime/Agent_Interval.LoggedOnTime).

% Not
                                             						Ready

The
                                             						percentage of time that the agent spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Applies to all skill groups.

This field  is a
                                             						calculated field, derived from  (Agent_Interval.NotReadyTime /
                                             						Agent_Interval.LoggedOnTime).

% Reserved

The
                                             						percentage of time that the agent spent in Reserved state waiting for task from
                                             						this skill group in relation to LoggedOnTime.

This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.ReservedStateTime
                                             						/ Agent_Interval.LoggedOnTime).

% Wrap Up

The
                                             						percentage of time that the agent spent in Wrap-up state after an incoming or
                                             						outgoing call to/from this skill group in relation to LoggedOnTime.

The
                                             						agent state time percentages in the Report Summary row add up to 100 percent
                                             						only after you select all the skill groups for an agent. When you view a subset of an
                                             						agent's skill groups, you might notice that the percentages may not balance.

This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime
                                             						+Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             						/ Agent_Interval.LoggedOnTime.

Report Summary: There is a summary for Skill Group and a
                                 				report summary for all data. For more information, see Report Summary Rows .

## Agent Team Historical All Fields

Use the Agent Team Historical
                              report to view call distribution and agent state percentages by team.

Views: This report has one grid view, Agent Team Historical All Fields.

Query: This report data is
                              built from an Anonymous Block.

Grouping: This template is
                              grouped and sorted by Agent Team, and then by Supervisor, and then by Agent.

Value List: Agent Team

Database Schema Tables from
                              which data is retrieved:

Agent

Agent_Interval

Agent_Skill_Group_Interval

Agent_Team

Agent_Team_Member

Media_Routing_Domain

Person

Precision_Queue

Skill_Group

This report displays data related to current agent team members only.

### Available Fields in the Agent Team Historical All Fields Grid View

Available fields for this report include the fields that appear by
                                 default as Current. Additional Available fields in this report are populated
                                 directly from the Agent_Skill_Group_Interval table. For example, Aban Calls Ring Time is derived from
                                 Agent_Skill_Group_Interval.AbandRingTime.

An exception is Wrap Time , which is a calculated field derived
                                 from: (Agent_Skill_Group_Interval.WorkNotReadyTime +
                                 Agent_Skill_Group_Interval.WorkReadyTime)

Other tables used for Available fields in this report
                                 are:

Agent_Team

Agent_Team.AgentTeamID

Agent_Interval

Avail Time - Derived from: Agent_Interval.AvailTime

Media_Routing_Domain

The Media field is derived
                                             from Media_Routing_Domain.EnterpriseName

### Current Fields in the Agent Team Historical All Fields Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Agent Team

The
                                             						Enterprise Name of the Agent Team.

Derived
                                             						from  Agent_Team.EnterpriseName.

Agent

The last
                                             						and first name of the agent.

Derived
                                             						from Person.LastName "," Person.FirstName.

DateTime

The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format.

Derived
                                             						from Agent_Skill_Group_Interval.DateTime.

COMPLETED TASKS

Handled

The number of Unified ICM routed tasks this agent handled.

Derived
                                             						from  Agent_Skill_Group_Interval.CallsHandled.

Held

The number
                                             						of incoming calls to this agent that were placed on hold.

Derived
                                             						from  Agent_Skill_Group_Interval.IncomingCallsOnHold.

Abandon Rings

For voice: The total number of calls that were abandoned while the agent's phone was
                                             						ringing.

For non-voice: The total number of tasks that were abandoned while
                                             						being offered to an agent.

Derived
                                             						from  Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer.

Derived
                                             						from  Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing. This value is updated
                                             						when the agent completes the call.

Derived
                                             						from  Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number
                                             						of calls this agent transferred to another agent or skill group. This number includes
                                             						Consultative Calls if this transfer was consultative-not blind. This value is
                                             						updated when the agent completes the transfer.

This is a
                                             						calculated field derived from  Agent_Skill_Group_Interval.TransferredOutCalls +
                                             						Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number
                                             						of Outgoing external calls that this agent made in the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.AgentOutCalls.

Talk Time

The total time in HH:MM:SS (hours, minutes, seconds) that agents spent talking on the phone.

This field is a calculated field derived from

sum(isnull(TalkInTime,0)) +sum(isnull(TalkOutTime,0)) +sum(isnull(TalkOtherTime,0)) +sum(isnull(TalkAutoOutTime,0)) +sum(isnull(TalkPreviewTime,0))
                                             +sum(isnull(TalkReserveTime,0)).

Report Summary: There is a summary row for Agent Team and a
                                 				report summary for all data. For more information, see Report Summary Rows .

### Available Fields in the Agent Team Historical All Fields Grid View

Available fields for this report include the fields that appear by
                                 default as Current. Additional Available fields in this report are populated
                                 directly from the Agent_Skill_Group_Interval table. For example, Aban Calls Ring Time is derived from
                                 Agent_Skill_Group_Interval.AbandRingTime.

An exception is Wrap Time , which is a calculated field derived
                                 from: (Agent_Skill_Group_Interval.WorkNotReadyTime +
                                 Agent_Skill_Group_Interval.WorkReadyTime)

Other tables used for Available fields in this report
                                 are:

Agent_Team

Agent_Team.AgentTeamID

Agent_Interval

Avail Time - Derived from: Agent_Interval.AvailTime

Media_Routing_Domain

The Media field is derived
                                             from Media_Routing_Domain.EnterpriseName

### Current Fields in the Agent Team Historical All Fields Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Agent Team

The
                                             						Enterprise Name of the Agent Team.

Derived
                                             						from  Agent_Team.EnterpriseName.

Agent

The last
                                             						and first name of the agent.

Derived
                                             						from Person.LastName "," Person.FirstName.

DateTime

The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format.

Derived
                                             						from Agent_Skill_Group_Interval.DateTime.

COMPLETED TASKS

Handled

The number of Unified ICM routed tasks this agent handled.

Derived
                                             						from  Agent_Skill_Group_Interval.CallsHandled.

Held

The number
                                             						of incoming calls to this agent that were placed on hold.

Derived
                                             						from  Agent_Skill_Group_Interval.IncomingCallsOnHold.

Abandon Rings

For voice: The total number of calls that were abandoned while the agent's phone was
                                             						ringing.

For non-voice: The total number of tasks that were abandoned while
                                             						being offered to an agent.

Derived
                                             						from  Agent_Skill_Group_Interval.AbandonRingCalls.

RONA

The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer.

Derived
                                             						from  Agent_Skill_Group_Interval.RedirectNoAnsCalls.

Abandon Hold

The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.AbandonHoldCalls.

Transfer In

The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing. This value is updated
                                             						when the agent completes the call.

Derived
                                             						from  Agent_Skill_Group_Interval.TransferredInCalls.

Transfer Out

The number
                                             						of calls this agent transferred to another agent or skill group. This number includes
                                             						Consultative Calls if this transfer was consultative-not blind. This value is
                                             						updated when the agent completes the transfer.

This is a
                                             						calculated field derived from  Agent_Skill_Group_Interval.TransferredOutCalls +
                                             						Agent_Skill_Group_Interval.NetTransferredOutCalls.

External Out

The number
                                             						of Outgoing external calls that this agent made in the interval.

Derived
                                             						from  Agent_Skill_Group_Interval.AgentOutCalls.

Talk Time

The total time in HH:MM:SS (hours, minutes, seconds) that agents spent talking on the phone.

This field is a calculated field derived from

sum(isnull(TalkInTime,0)) +sum(isnull(TalkOutTime,0)) +sum(isnull(TalkOtherTime,0)) +sum(isnull(TalkAutoOutTime,0)) +sum(isnull(TalkPreviewTime,0))
                                             +sum(isnull(TalkReserveTime,0)).

Report Summary: There is a summary row for Agent Team and a
                                 				report summary for all data. For more information, see Report Summary Rows .

## Call Type Abandon/Answer Distribution Historical

Use Call Type Abandon Answer
                              				Distribution to identify where in the routing, callers are abandoning and to
                              				identify the typical wait times for callers.

Query: This report data is
                              				built from a Database Query.

Views: This report has one grid view, Call Type Abandon Answer Distribution Historical.

Grouping: This report is
                              				grouped and sorted by Call Type.

Value List: Call Type

Database Schema Tables from
                                 					which data is retrieved:

Bucket_Intervals

Call_Type

Call_Type_Interval

### Available Fields in
                           	 the Call Type Abandon/Answer Distribution Historical Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. Additional
                                 		  Available fields in this report are populated from the following tables.

These Available
                                 		  fields are from the Call_Type_Interval table:

Ans Wait Time Derived
                                       				from: Call_Type_Interval.AnswerWaitTime.

BucketIntervalID Derived
                                       				from: Call_Type_Interval.BucketIntervalID.

Calls Handled Derived from: Call_Type_Interval.CallsHandled.

CallTypeID Derived from: Call_Type_Interval.CallsTypeID.

DelayQAban Derived from: Call_Type_Interval.CallDelayAbandTime.

Router Calls Aban :
                                       				Derived from: Call_Type_Interval.TotalCallsAband.

These fields are
                                 		  derived from the Bucket_Intervals table, as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html :

int1 - int 9 : Derived
                                 		  from: Bucket_Intervals.IntervalUpperBound1 - IntervalUpperBound9.

### Current Fields in the Call Type Abandon/Answer Distribution Historical Grid View

Current fields are those
                                 		  fields that appear by default in a report grid view generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

The headings for the
                                 		  Interval fields are dynamic headers; they show the intervals you defined.

Column
                                             						(Field)

Description

Call Type

The
                                             						enterprise name for the call type.

Derived
                                             						from Call_Type.EnterpriseName.

Date Time

The date
                                             						and time when the call type interval data was generated in MM/DD/YYYY (month,
                                             						day, year) and HH:MM:SS (hours, minutes, seconds) format.

For every
                                             						interval in the selected time period, there is summary row for each selected
                                             						call type.

Derived
                                             						from: Call_Type_Interval.DateTime.

Avg Speed of Answer

Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels.

This field is a
                                             						calculated field, derived from: Call_Type_Interval.AnswerWaitTime/
                                             						 Call_Type_Interval.CallsHandled.

Avg Abandon Delay

The
                                             						average delay time of all abandoned calls that ended in this call type during
                                             						the current interval. This value includes calls that were abandoned in queue, calls
                                             						that were abandoned while at the IVR (prompting or self service) and calls that
                                             						were abandoned while ringing at the agent's phone or en route to the agent's
                                             						phone.

This field is a
                                             						calculated field, derived from: Call_Type_Interval.CallDelayAbandTime /
                                             						Call_Type_Interval.TotalCallsAband.

Int 1 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between the time set to begin measuring and
                                             						interval 1. The system default interval 1 is 8 seconds. For example: 00:00 -
                                             						00:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(1) and
                                             						Call_Type_Interval.AbandInterval(1).

Int 2 Ans
                                             						and Aban

The number
                                             						of calls answered/abandoned between interval 1 and interval 2. The system
                                             						default interval 2 is 30 seconds. For example: 00:08 - 00:38.

Derived
                                             						from: Call_Type_Interval.AnsInterval(2) and
                                             						Call_Type_Interval.AbandInterval(2).

Int 3 Ans
                                             						and Aban

The number
                                             						of calls answered/abandoned between interval 2 and interval 3. The system
                                             						default interval 3 is 60 seconds (1 minute). For example: 00:38 - 01:38.

Derived
                                             						from: Call_Type_Interval.AnsInterval(3) and
                                             						Call_Type_Interval.AbandInterval(3).

Int 4 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 3 and interval 4. The
                                             						system default interval 4 is 90 seconds. For example: 01:38 - 03:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(4) and
                                             						Call_Type_Interval.AbandInterval(4).

Int 5 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 4 and interval 5. The
                                             						system default interval 5 is 120 seconds (2 minutes). For example: 03:08 -
                                             						05:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(5) and
                                             						Call_Type_Interval.AbandInterval(5).

Int 6 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 5 and interval 6. The
                                             						system default interval 6 is 180 seconds (3 minutes). For example: 05:08 -
                                             						08:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(6) and
                                             						Call_Type_Interval.AbandInterval(6).

Int 7 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 6 and interval 7. The
                                             						system default interval 7 is 300 seconds (5 minutes). For example: 08:08 -
                                             						13:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(7) and
                                             						Call_Type_Interval.AbandInterval(7).

Int 8 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 7 and interval 8. The
                                             						system default interval 8 is 600 seconds (10 minutes). For example: 13:08 -
                                             						23:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(8) and
                                             						Call_Type_Interval.AbandInterval(8).

Int 9 Ans
                                             						and Aban

The number
                                             						of calls answered/abandoned between interval 8 and interval 9. The system
                                             						default interval 9 is 1200 seconds (20 minutes). For example: 23:08 - 43:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(9) and
                                             						Call_Type_Interval.AbandInterval(9).

> Int 9
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned within the remaining time in the report time
                                             						period measured in minutes and seconds. For example: > 43:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(10) and
                                             						Call_Type_Interval.AbandInterval(10).

MaxQueued

The
                                             						maximum number of calls in queue for this call type during this interval.

Derived
                                             						from: Call_Type_Interval. MaxCallsQueued.

The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later.

Longest Queued

The
                                             						longest time a call had to wait before it was dispositioned (abandoned or
                                             						answered) in this interval.

Derived
                                             						from: Call_Type_Interval. MaxCallWaitTime.

The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later.

Report Summary: The summary line shows an average for the Avg
                                 				Speed of Answer and Avg Abandon Delay columns, totals for the interval columns, and
                                 				Max for MaxQueued and Longest Queued columns. For more information, see Report Summary Rows .

### Available Fields in
                           	 the Call Type Abandon/Answer Distribution Historical Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. Additional
                                 		  Available fields in this report are populated from the following tables.

These Available
                                 		  fields are from the Call_Type_Interval table:

Ans Wait Time Derived
                                       				from: Call_Type_Interval.AnswerWaitTime.

BucketIntervalID Derived
                                       				from: Call_Type_Interval.BucketIntervalID.

Calls Handled Derived from: Call_Type_Interval.CallsHandled.

CallTypeID Derived from: Call_Type_Interval.CallsTypeID.

DelayQAban Derived from: Call_Type_Interval.CallDelayAbandTime.

Router Calls Aban :
                                       				Derived from: Call_Type_Interval.TotalCallsAband.

These fields are
                                 		  derived from the Bucket_Intervals table, as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html :

int1 - int 9 : Derived
                                 		  from: Bucket_Intervals.IntervalUpperBound1 - IntervalUpperBound9.

### Current Fields in the Call Type Abandon/Answer Distribution Historical Grid View

Current fields are those
                                 		  fields that appear by default in a report grid view generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

The headings for the
                                 		  Interval fields are dynamic headers; they show the intervals you defined.

Column
                                             						(Field)

Description

Call Type

The
                                             						enterprise name for the call type.

Derived
                                             						from Call_Type.EnterpriseName.

Date Time

The date
                                             						and time when the call type interval data was generated in MM/DD/YYYY (month,
                                             						day, year) and HH:MM:SS (hours, minutes, seconds) format.

For every
                                             						interval in the selected time period, there is summary row for each selected
                                             						call type.

Derived
                                             						from: Call_Type_Interval.DateTime.

Avg Speed of Answer

Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels.

This field is a
                                             						calculated field, derived from: Call_Type_Interval.AnswerWaitTime/
                                             						 Call_Type_Interval.CallsHandled.

Avg Abandon Delay

The
                                             						average delay time of all abandoned calls that ended in this call type during
                                             						the current interval. This value includes calls that were abandoned in queue, calls
                                             						that were abandoned while at the IVR (prompting or self service) and calls that
                                             						were abandoned while ringing at the agent's phone or en route to the agent's
                                             						phone.

This field is a
                                             						calculated field, derived from: Call_Type_Interval.CallDelayAbandTime /
                                             						Call_Type_Interval.TotalCallsAband.

Int 1 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between the time set to begin measuring and
                                             						interval 1. The system default interval 1 is 8 seconds. For example: 00:00 -
                                             						00:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(1) and
                                             						Call_Type_Interval.AbandInterval(1).

Int 2 Ans
                                             						and Aban

The number
                                             						of calls answered/abandoned between interval 1 and interval 2. The system
                                             						default interval 2 is 30 seconds. For example: 00:08 - 00:38.

Derived
                                             						from: Call_Type_Interval.AnsInterval(2) and
                                             						Call_Type_Interval.AbandInterval(2).

Int 3 Ans
                                             						and Aban

The number
                                             						of calls answered/abandoned between interval 2 and interval 3. The system
                                             						default interval 3 is 60 seconds (1 minute). For example: 00:38 - 01:38.

Derived
                                             						from: Call_Type_Interval.AnsInterval(3) and
                                             						Call_Type_Interval.AbandInterval(3).

Int 4 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 3 and interval 4. The
                                             						system default interval 4 is 90 seconds. For example: 01:38 - 03:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(4) and
                                             						Call_Type_Interval.AbandInterval(4).

Int 5 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 4 and interval 5. The
                                             						system default interval 5 is 120 seconds (2 minutes). For example: 03:08 -
                                             						05:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(5) and
                                             						Call_Type_Interval.AbandInterval(5).

Int 6 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 5 and interval 6. The
                                             						system default interval 6 is 180 seconds (3 minutes). For example: 05:08 -
                                             						08:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(6) and
                                             						Call_Type_Interval.AbandInterval(6).

Int 7 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 6 and interval 7. The
                                             						system default interval 7 is 300 seconds (5 minutes). For example: 08:08 -
                                             						13:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(7) and
                                             						Call_Type_Interval.AbandInterval(7).

Int 8 Ans
                                             						and Aban

The
                                             						number of calls answered/abandoned between interval 7 and interval 8. The
                                             						system default interval 8 is 600 seconds (10 minutes). For example: 13:08 -
                                             						23:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(8) and
                                             						Call_Type_Interval.AbandInterval(8).

Int 9 Ans
                                             						and Aban

The number
                                             						of calls answered/abandoned between interval 8 and interval 9. The system
                                             						default interval 9 is 1200 seconds (20 minutes). For example: 23:08 - 43:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(9) and
                                             						Call_Type_Interval.AbandInterval(9).

> Int 9
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned within the remaining time in the report time
                                             						period measured in minutes and seconds. For example: > 43:08.

Derived
                                             						from: Call_Type_Interval.AnsInterval(10) and
                                             						Call_Type_Interval.AbandInterval(10).

MaxQueued

The
                                             						maximum number of calls in queue for this call type during this interval.

Derived
                                             						from: Call_Type_Interval. MaxCallsQueued.

The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later.

Longest Queued

The
                                             						longest time a call had to wait before it was dispositioned (abandoned or
                                             						answered) in this interval.

Derived
                                             						from: Call_Type_Interval. MaxCallWaitTime.

The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later.

Report Summary: The summary line shows an average for the Avg
                                 				Speed of Answer and Avg Abandon Delay columns, totals for the interval columns, and
                                 				Max for MaxQueued and Longest Queued columns. For more information, see Report Summary Rows .

## Call Type Historical All Fields

Use Call Type Historical All Fields to view incoming calls/contacts, key statistics like Average Speed of Answer and Service
                              Level, and call disposition information.

Query: This report data
                              		  is built from a Database Query.

Views: This report has the following grid views and a pie chart view. The pie chart shows the percentage of calls answered in each
                              call type.

Answered by Call Type (Chart View)

Call Type Historical- Daily (Grid View)

Call Type Historical- Monthly (Grid View)

Call Type Historical- Weekly (Grid View)

Call Type Historical All Fields (Grid View)

Select the view you want to see from the report drop-down list located on the top left corner.

Grouping: This report is grouped by call type and then by date and time.

Value List: Call Type

Database Schema Tables from which data is retrieved :

Call_Type

Call_Type_Interval

### Available Fields in the Call Type Historical All Fields Grid View

Available fields for the grid view for this report include the fields that
                                 appear by default as Current. Additional Available fields in this report
                                 are taken directly from the Call_Type_Interval table.

### Current Fields for
                           	 the Call Type Historical All Fields Grid View

Current fields are those
                                 		  fields that appear by default in the grid view for this report.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Call Type

The
                                             						enterprise name for the call type.

Derived
                                             						from: Call_Type.EnterpriseName.

DateTime

The date
                                             						and time when the record was generated in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hours, minutes, seconds) format.

Derived
                                             						from: Call_Type_Interval.DateTime.

Service
                                             						Level

Service
                                             						Level Type used to calculate Service level for the interval.

Derived
                                             						from: Call_Type_Interval.ServiceLevel.

Abandon
                                             						Within Service Level

The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes.

This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                             and the queue.

Derived
                                             						from: Call_Type_Interval.ServiceLevelAband.

Avg Speed
                                             						of Answer

Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels.

This field
                                             						is a calculated field, derived from: Call_Type_Interval.AnswerWaitTime /
                                             						Call_Type_Interval.CallsAnswered.

TASKS

Offered

Tasks that
                                             						were offered to this call type during the interval.

Derived
                                             						from: Call_Type_Interval.CallsOffered.

Assigned
                                             						from Q

The number
                                             						of tasks of the call type assigned from the queue to be routed in the interval.

Derived
                                             						from: Call_Type_Interval.RouterQueueCalls.

Answered

The total number of calls of this call type answered by agents in the interval. This field is applicable to both Unified ICM and Unified CCE with the following exception: if the call is answered by an agent on a standard ACD, this field is incremented only if the
                                                call was translation routed.

Derived
                                             						from: Call_Type_Interval.CallsAnswered.

Answer
                                             						Wait Time

Answer Wait Time. The sum of answer wait time in seconds for all calls that were answered for the call type during the reporting
                                             interval. This field is applicable to both Unified ICM and Unified CCE with the following exception: if the call is answered by an agent on a standard ACD, this field is incremented only if the
                                                call was translation routed.

Derived
                                             						from: Call_Type_Interval.AnswerWaitTime.

COMPLETED TASKS

Handled

The total
                                             						number of tasks handled to completion for the call type in the interval.

Derived
                                             						from: Call_Type_Interval.CallsHandled.

Abandon

The total number of calls abandoned while in VRU (that is, while undergoing prompting or listening to voice menus options),
                                             calls abandoned while queued to skill group, and calls abandoned at agent desktop. This value also includes abandons for calls
                                             that are not in the queue; for example, when the caller ends the call while listening to a VRU prompt. Therefore, the number
                                             of calls abandoned at a VRU before being queued is TotalCallsAband minus RouterCallsAbandToAgent and RouterCallsAbandQ. Does
                                             not include short calls.

Derived
                                             						from: Call_Type_Interval.TotalCallsAband.

Return

The number of tasks of the call type that ICM software routed to Return nodes in the interval.

This field
                                             						is a calculated field, derived from: Call_Type_Interval.ReturnBusy +
                                             						Call_Type_Interval.ReturnRing + Call_Type_Interval.ReturnRelease.

Default
                                             						Treatment

The number
                                             						of tasks of the call type that were given default treatment or end nodes in the
                                             						interval.

Derived
                                             						from: Call_Type_Interval.ICRDefaultRouted.

Network
                                             						Routed

The number of tasks of the call type that were routed not by ICM software but by the carrier in the interval. For prerouted calls, the carrier decides where to route the call.

Derived
                                             						from: Call_Type_Interval.NetworkDefaultRouted.

Flow Out

The number
                                             						of tasks of the call type that flowed out of the call type to another call type
                                             						in the interval.

Derived
                                             						from: Call_Type_Interval.OverflowOut.

Calls
                                             						Error

The number
                                             						of calls for this call type that had errors or were incomplete in the interval.

This field
                                             						is a calculated field, derived from: Call_Type_Interval.ErrorCount +
                                             						Call_Type_Interval.IncompleteCalls + Call_Type_Interval.AgentErrorCount.

Other

The number
                                             						of tasks of the call type that are Short, were routed to non-Agent targets, or
                                             						were redirected in the interval.

This field
                                             						is a calculated field, derived from: Call_Type_Interval.CallsRONA +
                                             						Call_Type_Interval.CallsRoutedNonAgent + Call_Type_Interval.ShortCalls.

% Queued

The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval.

This field
                                             						is a calculated field, derived from: (Call_Type_Interval.CallsQHandled /
                                             						Call_Type_Interval.CallsHandled).

% Aban

The
                                             						percentage of all the tasks that came in to the call type in the interval that
                                             						were abandoned.

This field
                                             						is a calculated field, derived from:

(Call_Type_Interval.TotalCallsAband /
                                             						(Call_Type_Interval.CallsHandled+ Call_Type_Interval.TotalCallsAband +
                                             						Call_Type_Interval.IncompleteCalls + Call_Type_Interval.ReturnBusy +
                                             						Call_Type_Interval.ReturnRing + Call_Type_Interval.ICRDefaultRouted +
                                             						Call_Type_Interval.NetworkDefaultRouted + Call_Type_Interval.OverflowOut +
                                             						Call_Type_Interval.CallsRONA + Call_Type_Interval.ReturnRelease +
                                             						Call_Type_Interval.CallsRoutedNonAgent + Call_Type_Interval.ShortCalls+
                                             						Call_Type_Interval.ErrorCount + Call_Type_Interval.AgentErrorCount).

Avg Aban
                                             						Delay

The
                                             						average delay time of all abandoned calls that ended in this call type during
                                             						the current interval. This includes calls that were abandoned in queue, calls
                                             						that were abandoned while at the IVR (prompting or self service) and calls that
                                             						were abandoned while ringing at the agent's phone or en route to the agent's
                                             						phone.

This field
                                             						is a calculated field. Derived from: Call_Type_Interval.CallDelayAbandTime /
                                             						Call_Type_Interval.TotalCallsAband.

Short
                                             						Calls

The number
                                             						of calls abandoned during the Call_Type Abandon Call Wait Time. Calls abandoned
                                             						after this time period are counted as Abandoned, not Short Calls.

Derived
                                             						from: Call_Type_Interval.ShortCalls.

Tasks Picked

The total number of pick requests successfully routed by this call type in the reporting interval.

Tasks Pulled

The total number of  pull requests successfully routed by this call type in the reporting interval.

Picks Failed

Number of pick request resulting in an error.

Pulls Failed

Number of pull requests resulting in an error.

MaxQueued

The maximum number of calls in queue for this call type during this interval.

Derived from: Call_Type_Interval. MaxCallsQueued.

Longest Queued

The longest time a call had to wait before it was dispositioned (abandoned or answered) in this interval.

Derived from: Call_Type_Interval. MaxCallWaitTime.

The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later.

Report Summaries

Call Type Summary

Field totals, except the Service Level field, for each call type in the report. The Service
                                       						Level fields have percentage values. The summary also displays the Average
                                       						for Avg Speed of Answer

Report Summary

Field totals, except the Service Level field, for all call types in the report. The Service
                                       						Level fields have percentage values. The summary displays the Max for
                                       						MaxQueued and Longest Queued.

### Available Fields in the Call Type Historical All Fields Grid View

Available fields for the grid view for this report include the fields that
                                 appear by default as Current. Additional Available fields in this report
                                 are taken directly from the Call_Type_Interval table.

### Current Fields for
                           	 the Call Type Historical All Fields Grid View

Current fields are those
                                 		  fields that appear by default in the grid view for this report.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Call Type

The
                                             						enterprise name for the call type.

Derived
                                             						from: Call_Type.EnterpriseName.

DateTime

The date
                                             						and time when the record was generated in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hours, minutes, seconds) format.

Derived
                                             						from: Call_Type_Interval.DateTime.

Service
                                             						Level

Service
                                             						Level Type used to calculate Service level for the interval.

Derived
                                             						from: Call_Type_Interval.ServiceLevel.

Abandon
                                             						Within Service Level

The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes.

This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                             and the queue.

Derived
                                             						from: Call_Type_Interval.ServiceLevelAband.

Avg Speed
                                             						of Answer

Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels.

This field
                                             						is a calculated field, derived from: Call_Type_Interval.AnswerWaitTime /
                                             						Call_Type_Interval.CallsAnswered.

TASKS

Offered

Tasks that
                                             						were offered to this call type during the interval.

Derived
                                             						from: Call_Type_Interval.CallsOffered.

Assigned
                                             						from Q

The number
                                             						of tasks of the call type assigned from the queue to be routed in the interval.

Derived
                                             						from: Call_Type_Interval.RouterQueueCalls.

Answered

The total number of calls of this call type answered by agents in the interval. This field is applicable to both Unified ICM and Unified CCE with the following exception: if the call is answered by an agent on a standard ACD, this field is incremented only if the
                                                call was translation routed.

Derived
                                             						from: Call_Type_Interval.CallsAnswered.

Answer
                                             						Wait Time

Answer Wait Time. The sum of answer wait time in seconds for all calls that were answered for the call type during the reporting
                                             interval. This field is applicable to both Unified ICM and Unified CCE with the following exception: if the call is answered by an agent on a standard ACD, this field is incremented only if the
                                                call was translation routed.

Derived
                                             						from: Call_Type_Interval.AnswerWaitTime.

COMPLETED TASKS

Handled

The total
                                             						number of tasks handled to completion for the call type in the interval.

Derived
                                             						from: Call_Type_Interval.CallsHandled.

Abandon

The total number of calls abandoned while in VRU (that is, while undergoing prompting or listening to voice menus options),
                                             calls abandoned while queued to skill group, and calls abandoned at agent desktop. This value also includes abandons for calls
                                             that are not in the queue; for example, when the caller ends the call while listening to a VRU prompt. Therefore, the number
                                             of calls abandoned at a VRU before being queued is TotalCallsAband minus RouterCallsAbandToAgent and RouterCallsAbandQ. Does
                                             not include short calls.

Derived
                                             						from: Call_Type_Interval.TotalCallsAband.

Return

The number of tasks of the call type that ICM software routed to Return nodes in the interval.

This field
                                             						is a calculated field, derived from: Call_Type_Interval.ReturnBusy +
                                             						Call_Type_Interval.ReturnRing + Call_Type_Interval.ReturnRelease.

Default
                                             						Treatment

The number
                                             						of tasks of the call type that were given default treatment or end nodes in the
                                             						interval.

Derived
                                             						from: Call_Type_Interval.ICRDefaultRouted.

Network
                                             						Routed

The number of tasks of the call type that were routed not by ICM software but by the carrier in the interval. For prerouted calls, the carrier decides where to route the call.

Derived
                                             						from: Call_Type_Interval.NetworkDefaultRouted.

Flow Out

The number
                                             						of tasks of the call type that flowed out of the call type to another call type
                                             						in the interval.

Derived
                                             						from: Call_Type_Interval.OverflowOut.

Calls
                                             						Error

The number
                                             						of calls for this call type that had errors or were incomplete in the interval.

This field
                                             						is a calculated field, derived from: Call_Type_Interval.ErrorCount +
                                             						Call_Type_Interval.IncompleteCalls + Call_Type_Interval.AgentErrorCount.

Other

The number
                                             						of tasks of the call type that are Short, were routed to non-Agent targets, or
                                             						were redirected in the interval.

This field
                                             						is a calculated field, derived from: Call_Type_Interval.CallsRONA +
                                             						Call_Type_Interval.CallsRoutedNonAgent + Call_Type_Interval.ShortCalls.

% Queued

The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval.

This field
                                             						is a calculated field, derived from: (Call_Type_Interval.CallsQHandled /
                                             						Call_Type_Interval.CallsHandled).

% Aban

The
                                             						percentage of all the tasks that came in to the call type in the interval that
                                             						were abandoned.

This field
                                             						is a calculated field, derived from:

(Call_Type_Interval.TotalCallsAband /
                                             						(Call_Type_Interval.CallsHandled+ Call_Type_Interval.TotalCallsAband +
                                             						Call_Type_Interval.IncompleteCalls + Call_Type_Interval.ReturnBusy +
                                             						Call_Type_Interval.ReturnRing + Call_Type_Interval.ICRDefaultRouted +
                                             						Call_Type_Interval.NetworkDefaultRouted + Call_Type_Interval.OverflowOut +
                                             						Call_Type_Interval.CallsRONA + Call_Type_Interval.ReturnRelease +
                                             						Call_Type_Interval.CallsRoutedNonAgent + Call_Type_Interval.ShortCalls+
                                             						Call_Type_Interval.ErrorCount + Call_Type_Interval.AgentErrorCount).

Avg Aban
                                             						Delay

The
                                             						average delay time of all abandoned calls that ended in this call type during
                                             						the current interval. This includes calls that were abandoned in queue, calls
                                             						that were abandoned while at the IVR (prompting or self service) and calls that
                                             						were abandoned while ringing at the agent's phone or en route to the agent's
                                             						phone.

This field
                                             						is a calculated field. Derived from: Call_Type_Interval.CallDelayAbandTime /
                                             						Call_Type_Interval.TotalCallsAband.

Short
                                             						Calls

The number
                                             						of calls abandoned during the Call_Type Abandon Call Wait Time. Calls abandoned
                                             						after this time period are counted as Abandoned, not Short Calls.

Derived
                                             						from: Call_Type_Interval.ShortCalls.

Tasks Picked

The total number of pick requests successfully routed by this call type in the reporting interval.

Tasks Pulled

The total number of  pull requests successfully routed by this call type in the reporting interval.

Picks Failed

Number of pick request resulting in an error.

Pulls Failed

Number of pull requests resulting in an error.

MaxQueued

The maximum number of calls in queue for this call type during this interval.

Derived from: Call_Type_Interval. MaxCallsQueued.

Longest Queued

The longest time a call had to wait before it was dispositioned (abandoned or answered) in this interval.

Derived from: Call_Type_Interval. MaxCallWaitTime.

The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later.

Report Summaries

Call Type Summary

Field totals, except the Service Level field, for each call type in the report. The Service
                                       						Level fields have percentage values. The summary also displays the Average
                                       						for Avg Speed of Answer

Report Summary

Field totals, except the Service Level field, for all call types in the report. The Service
                                       						Level fields have percentage values. The summary displays the Max for
                                       						MaxQueued and Longest Queued.

## Call Type Queue
                        	 Interval All Fields

Reports generated
                              		  from this template show the summary statistics for Skill Groups and Precision
                              		  Queues within Call Type ID. This information is useful for tying queues to
                              		  resources and for forecasting and scheduling.

Note: For Unified CCE , the presence of certain data depends on the use of Enterprise Queuing and on whether Translation Routing is implemented.

Query: This report data
                              		  is built from an Anonymous Block type query.

Views: This report has the following grid views:

Call Type Queue Interval All Fields

Call Type Queue Skillgroup Summary

Select the view you want to see from the report drop-down list located on the top left corner.

Grouping: This report is grouped by call type
                              		  and then by date and time.

Value List: Call Type

Database Schema Tables from which data is retrieved :

Call_Type

Precision_Queue

Call_Type_SG_Interval

Attribute

Router_Queue_Interval

Skill_Group

Media_Routing_Domain

### Available Fields in the Call Type Queue Interval All Fields Grid View

Available fields for this report include the fields that appear by
                                 default as Current.

Additional Available fields in this report are taken directly from the
                                 Call_Type_SG_Interval table.

### Current Fields in
                           	 the Call Type Queue Interval All Fields Grid View

Current fields are those
                                 		  fields that appear by default in a report grid view generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Call Type

The
                                             						enterprise name for the call type.

Derived
                                             						from Call_Type.EnterpriseName.

Precision Queue / Skill Group

The
                                             						enterprise name for the skill group or agent precision queue. You can identify
                                             						a precision queue by the presence of Attributes next to the queue name.

Derived
                                             						from: Skill_Group.Enterprise or Precision_Queue.EnterpriseName

DateTime

The date
                                             						and time for the data of a selected row.

Derived
                                             						from: Call_Type_SG_Interval.DateTime.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

Handled

The total
                                             						number of tasks handled to completion for the call type in the interval.

Derived
                                             						from: Call_Type_SG_Interval.CallsHandled.

Avg Handle Time

The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds).

This field is a
                                             						calculated field, derived from: Call_Type_SG_Interval.Handle Time /
                                             						Call_Type_SG_Interval.CallsHandled.

%Queued

The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval.

This field  is a
                                             						calculated field, derived from Call_Type_SG_Interval. CallsQHandled
                                             						/Call_Type_SG_Interval.CallsHandled.

Service Level

Service
                                             						Level Type used to calculate Service level for the interval.

Derived
                                             						from: Call_Type_SG_Interval.ServiceLevel.

Avg Speed of Answer

Average Speed of Answer. The average answer waiting time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels.

This field is a
                                             						calculated field, derived from: Call_Type_SG_Interval.AnswerWaitTime /
                                             						Call_Type_SG_Interval.CallsAnswered.

Abandon Within Service Level

The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes.

This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                             and the queue.

Derived
                                             						from: Call_Type_Interval.ServiceLevelAband.

Abandon in Queue

The number
                                             						of calls to the call type that were abandoned in the Router queue during the
                                             						interval.

Derived
                                             						from: Call_Type_SG_Interval.RouterCalls AbandQ.

Longest Queued

The longest a task had to wait before
                                             									being answered, abandoned, or otherwise ended. This value
                                             									includes time in the network queue, local queue, and ringing at
                                             									the agent, if applicable.

Derived
                                             						from: Router_Queue_Interval.MaxCallWaitTime

MaxQueued

The maximum number of tasks queued for
                                             									this skill group during this interval. Calls queued against
                                             									multiple skill groups are included in the count for each skill
                                             									group to which the calls are queued.

Derived
                                             						from: Router_Queue_Interval.MaxCallsQueued

Tasks Picked

The total number of pick requests successfully routed to this skill group or precision queue by this call type in the reporting
                                             interval.

Tasks Pulled

The total number of pull requests successfully routed to this skill group or precision queue by this call type in the reporting
                                             interval.

Picks Failed

Number of pick request resulting in an error.

Pulls Failed

Number of pull requests resulting in an error.

Report Summaries

The summary line displays the maximum for
                                 				MaxQueued and Longest Queued.

#### Current Fields in the Call Type Queue Skillgroup Summary Grid View

If you select the Call Type Queue Skillgroup Summary view, the report displays the following fields:

Call Type

DateTime

Handled

Avg Handle Time

%Queued

Service Level

Avg Speed of Answer

Abandon Within Service Level

Abandon in Queue

Queue

### Available Fields in the Call Type Queue Interval All Fields Grid View

Available fields for this report include the fields that appear by
                                 default as Current.

Additional Available fields in this report are taken directly from the
                                 Call_Type_SG_Interval table.

### Current Fields in
                           	 the Call Type Queue Interval All Fields Grid View

Current fields are those
                                 		  fields that appear by default in a report grid view generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Call Type

The
                                             						enterprise name for the call type.

Derived
                                             						from Call_Type.EnterpriseName.

Precision Queue / Skill Group

The
                                             						enterprise name for the skill group or agent precision queue. You can identify
                                             						a precision queue by the presence of Attributes next to the queue name.

Derived
                                             						from: Skill_Group.Enterprise or Precision_Queue.EnterpriseName

DateTime

The date
                                             						and time for the data of a selected row.

Derived
                                             						from: Call_Type_SG_Interval.DateTime.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

Handled

The total
                                             						number of tasks handled to completion for the call type in the interval.

Derived
                                             						from: Call_Type_SG_Interval.CallsHandled.

Avg Handle Time

The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds).

This field is a
                                             						calculated field, derived from: Call_Type_SG_Interval.Handle Time /
                                             						Call_Type_SG_Interval.CallsHandled.

%Queued

The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval.

This field  is a
                                             						calculated field, derived from Call_Type_SG_Interval. CallsQHandled
                                             						/Call_Type_SG_Interval.CallsHandled.

Service Level

Service
                                             						Level Type used to calculate Service level for the interval.

Derived
                                             						from: Call_Type_SG_Interval.ServiceLevel.

Avg Speed of Answer

Average Speed of Answer. The average answer waiting time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels.

This field is a
                                             						calculated field, derived from: Call_Type_SG_Interval.AnswerWaitTime /
                                             						Call_Type_SG_Interval.CallsAnswered.

Abandon Within Service Level

The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes.

This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                             and the queue.

Derived
                                             						from: Call_Type_Interval.ServiceLevelAband.

Abandon in Queue

The number
                                             						of calls to the call type that were abandoned in the Router queue during the
                                             						interval.

Derived
                                             						from: Call_Type_SG_Interval.RouterCalls AbandQ.

Longest Queued

The longest a task had to wait before
                                             									being answered, abandoned, or otherwise ended. This value
                                             									includes time in the network queue, local queue, and ringing at
                                             									the agent, if applicable.

Derived
                                             						from: Router_Queue_Interval.MaxCallWaitTime

MaxQueued

The maximum number of tasks queued for
                                             									this skill group during this interval. Calls queued against
                                             									multiple skill groups are included in the count for each skill
                                             									group to which the calls are queued.

Derived
                                             						from: Router_Queue_Interval.MaxCallsQueued

Tasks Picked

The total number of pick requests successfully routed to this skill group or precision queue by this call type in the reporting
                                             interval.

Tasks Pulled

The total number of pull requests successfully routed to this skill group or precision queue by this call type in the reporting
                                             interval.

Picks Failed

Number of pick request resulting in an error.

Pulls Failed

Number of pull requests resulting in an error.

Report Summaries

The summary line displays the maximum for
                                 				MaxQueued and Longest Queued.

#### Current Fields in the Call Type Queue Skillgroup Summary Grid View

If you select the Call Type Queue Skillgroup Summary view, the report displays the following fields:

Call Type

DateTime

Handled

Avg Handle Time

%Queued

Service Level

Avg Speed of Answer

Abandon Within Service Level

Abandon in Queue

Queue

## Call Type Skill
                        	 Group Historical All Fields

The Call Type Skill Group Historical All Fields report shows the summary statistics for Call Types and Skill Groups
                              		  within each Call Type during the interval.

Query: This report data is built from a Database Query.

Views: This report has one grid view, Call Type Skill Group Historical All Fields.

Grouping: This report is grouped by Call Type
                              		  Name, and then by Skill Group Name, and then by date and time.

Value List: Call Type

Database Schema Tables from which data is retrieved :

Call_Type_SG_Interval

Call_Type

Skill_Group

### Available Fields
                           	 in the Call Type Skill Group Historical All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.

Additional
                                 		  Available fields in this report are taken directly from the
                                 		  Call_Type_SG_Interval table.

### Current Fields in
                           	 the Call Type Skill Group Historical All Fields Grid View

Current fields are those fields that appear by default in a report grid view generated from the stock template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Call Type

The
                                             						enterprise name for the call type.

Derived
                                             						from: Call_Type_SG_Interval.EnterpriseName.

Skill Group

The
                                             						enterprise name for the skill group.

Derived
                                             						from: Skill_Group.Enterprise

DateTime

The date and time for the data of a selected row.

Derived from: Call_Type.DateTime

Handled

The
                                             						total number of tasks handled to completion for the call type in the interval.

Derived
                                             						from: Call_Type_SG_Interval.CallsHandled.

Avg Handle Time

The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds).

This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.Handle
                                             						Time/Call_Type_SG_Interval.CallsHandled.

%Queued

The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval.

This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.CallsQHandled
                                             						/Call_Type_SG_Interval.CallsHandled.

Service Level

Service Level Type used to calculate Service level for the interval.

Derived
                                             						from: Call_Type_SG_Interval.ServiceLevel.

Avg Speed of Answer

Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels.

This field is
                                             						a calculated field, derived from:

Call_Type_SG_Interval.AnswerWaitTime/Call_Type_SG_Interval.CallsAnswered.

Aban
                                             						within SL

The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes.

Derived
                                             						from: Call_Type_SG_Interval.ServiceLevelAband.

Aban in
                                             						Queue

The
                                             						number of calls to the call type that were abandoned in the Router queue during
                                             						the interval.

Derived
                                             						from: Call_Type_SG_Interval.RouterCallsAbandQ.

MaxQueued

The
                                             						maximum number of calls queued for this skill group during this interval. Calls
                                             						queued against multiple skill groups are included in the count for each skill
                                             						group to which the calls are queued.

Derived
                                             						from: Call_Type_SG_Interval.MaxCallsQueued

Longest Queued

The
                                             						longest a call had to wait before being answered, abandoned, or otherwise
                                             						ended. This value includes time in the network queue, local queue, and ringing at the
                                             						agent if applicable.

Derived
                                             						from: Call_Type_SG_Interval.MaxCallWaitTime

Tasks Picked

The total number of pick requests successfully routed to this skill group by this call type in the reporting interval.

Tasks Pulled

The total number of pull requests successfully routed to this skill group by this call type in the reporting interval.

Picks Failed

Number of pick request resulting in an error.

Pulls Failed

Number of pull requests resulting in an error.

Report Summaries: The summary line displays the averages from
                                 				Avg Handle Time, Avg Speed of Answer, and %Queued; and totals for Handled, Aban
                                 				within SL, and Aban in Queue.

### Available Fields
                           	 in the Call Type Skill Group Historical All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.

Additional
                                 		  Available fields in this report are taken directly from the
                                 		  Call_Type_SG_Interval table.

### Current Fields in
                           	 the Call Type Skill Group Historical All Fields Grid View

Current fields are those fields that appear by default in a report grid view generated from the stock template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Call Type

The
                                             						enterprise name for the call type.

Derived
                                             						from: Call_Type_SG_Interval.EnterpriseName.

Skill Group

The
                                             						enterprise name for the skill group.

Derived
                                             						from: Skill_Group.Enterprise

DateTime

The date and time for the data of a selected row.

Derived from: Call_Type.DateTime

Handled

The
                                             						total number of tasks handled to completion for the call type in the interval.

Derived
                                             						from: Call_Type_SG_Interval.CallsHandled.

Avg Handle Time

The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds).

This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.Handle
                                             						Time/Call_Type_SG_Interval.CallsHandled.

%Queued

The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval.

This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.CallsQHandled
                                             						/Call_Type_SG_Interval.CallsHandled.

Service Level

Service Level Type used to calculate Service level for the interval.

Derived
                                             						from: Call_Type_SG_Interval.ServiceLevel.

Avg Speed of Answer

Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels.

This field is
                                             						a calculated field, derived from:

Call_Type_SG_Interval.AnswerWaitTime/Call_Type_SG_Interval.CallsAnswered.

Aban
                                             						within SL

The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes.

Derived
                                             						from: Call_Type_SG_Interval.ServiceLevelAband.

Aban in
                                             						Queue

The
                                             						number of calls to the call type that were abandoned in the Router queue during
                                             						the interval.

Derived
                                             						from: Call_Type_SG_Interval.RouterCallsAbandQ.

MaxQueued

The
                                             						maximum number of calls queued for this skill group during this interval. Calls
                                             						queued against multiple skill groups are included in the count for each skill
                                             						group to which the calls are queued.

Derived
                                             						from: Call_Type_SG_Interval.MaxCallsQueued

Longest Queued

The
                                             						longest a call had to wait before being answered, abandoned, or otherwise
                                             						ended. This value includes time in the network queue, local queue, and ringing at the
                                             						agent if applicable.

Derived
                                             						from: Call_Type_SG_Interval.MaxCallWaitTime

Tasks Picked

The total number of pick requests successfully routed to this skill group by this call type in the reporting interval.

Tasks Pulled

The total number of pull requests successfully routed to this skill group by this call type in the reporting interval.

Picks Failed

Number of pick request resulting in an error.

Pulls Failed

Number of pull requests resulting in an error.

Report Summaries: The summary line displays the averages from
                                 				Avg Handle Time, Avg Speed of Answer, and %Queued; and totals for Handled, Aban
                                 				within SL, and Aban in Queue.

## CVA Historical

The CVA Historical Report shows the total number of calls handled at IVR, calls
                              abandoned at IVR, calls transferred to agents, and the average time spent on
                              IVR.

To run the CVA Historical Report, you must select the Call Types which are
                                          handling IVR Calls.

Views: This report has one Grid view and Column Chart view.

Query: This report data is built from the SQL Query.

Grouping: This report is grouped and sorted by Call Type.

Value List: Call Type

Database Schema Tables from which data is retrieved:

Call_Type_Interval

Call_Type

### Available Fields in the CVA Historical All Fields Grid View

Available fields for this report include the fields that appear by default as
                                 Current. Additional Available fields in this report are:

Time Spent on IVR: Derived from Call_Type_Interval.VRUTime

### Current Fields in the CVA Historical Report Grid View

Current fields are those fields that appear by default in a report generated from
                                 the stock template. Current fields are listed below in the order (left to right) in
                                 which they appear by default in the stock template.

Column (Field)

Description

Call Type

The enterprise name for the call type.

Derived from: Call_Type.EnterpriseName.

DateTime

The date and time of the selected row's data in MM/DD/YYYY
                                             (month, day, year) and HH:MM:SS (hours, minutes, seconds)
                                             format.

Derived from: Call_Type_Interval.DateTime

Total Calls Handled at IVR

Total number of calls handled at IVR.

Derived from: Call_Type_Interval.CallsOffered.

Calls Abandoned at IVR

Derived from:
                                             Call_Type_Interval.TotalCallsAband -
                                             Call_Type_Interval.RouterCallsAbandQ -
                                             Call_Type_Interval.RouterCallsAbandToAgent

Average Time Spent on IVR

The average time spent on IVR is measured in HH:MM:SS (hours,
                                             minutes,seconds) format.

Derived from:
                                             Call_Type_Interval.VRUTime/Call_Type_Interval.CallsOffered

Calls Transferred to Agent

Total number of calls getting transferred to the Agents.

Derived from: Call_Type_Interval.VruAssistedCalls +
                                             Call_Type_Interval.VruOptOutIUnhandledCalls +
                                             Call_Type_Interval. VruScriptedXferredCalls +
                                             Call_Type_Interval.VruForcedXferredCalls

#### Current Fields in the CVA Historical Report Column Chart View

If you select the CVA Historical Column Chart view, the report displays the following
                                 tables:

Calls Abandoned at IVR

Calls Transferred to Agent

Total Calls Handled at IVR

### Available Fields in the CVA Historical All Fields Grid View

Available fields for this report include the fields that appear by default as
                                 Current. Additional Available fields in this report are:

Time Spent on IVR: Derived from Call_Type_Interval.VRUTime

### Current Fields in the CVA Historical Report Grid View

Current fields are those fields that appear by default in a report generated from
                                 the stock template. Current fields are listed below in the order (left to right) in
                                 which they appear by default in the stock template.

Column (Field)

Description

Call Type

The enterprise name for the call type.

Derived from: Call_Type.EnterpriseName.

DateTime

The date and time of the selected row's data in MM/DD/YYYY
                                             (month, day, year) and HH:MM:SS (hours, minutes, seconds)
                                             format.

Derived from: Call_Type_Interval.DateTime

Total Calls Handled at IVR

Total number of calls handled at IVR.

Derived from: Call_Type_Interval.CallsOffered.

Calls Abandoned at IVR

Derived from:
                                             Call_Type_Interval.TotalCallsAband -
                                             Call_Type_Interval.RouterCallsAbandQ -
                                             Call_Type_Interval.RouterCallsAbandToAgent

Average Time Spent on IVR

The average time spent on IVR is measured in HH:MM:SS (hours,
                                             minutes,seconds) format.

Derived from:
                                             Call_Type_Interval.VRUTime/Call_Type_Interval.CallsOffered

Calls Transferred to Agent

Total number of calls getting transferred to the Agents.

Derived from: Call_Type_Interval.VruAssistedCalls +
                                             Call_Type_Interval.VruOptOutIUnhandledCalls +
                                             Call_Type_Interval. VruScriptedXferredCalls +
                                             Call_Type_Interval.VruForcedXferredCalls

#### Current Fields in the CVA Historical Report Column Chart View

If you select the CVA Historical Column Chart view, the report displays the following
                                 tables:

Calls Abandoned at IVR

Calls Transferred to Agent

Total Calls Handled at IVR

## Enterprise Service Historical All Fields

Enterprise Services may be configured in an ICM environment to report collectively on a group of services across ACDs. This report is not applicable to Contact Center Enterprise
                              environments.

Query: This report data
                              		  is built from a Database Query.

Views: This report has one grid view, Enterprise Service Historical All Fields.

Grouping: This report is grouped by Enterprise Name.

Value List: Service

Database Schema Tables from which data is retrieved:

Enterprise_Service

Enterprise_Service_Member

Service_Interval

Service

### Available Fields in the Enterprise Service Historical All Fields Grid View

Available fields for this report include the fields that appear by default as Current. Additional Available fields in this
                                 report are populated from the Service_Interval table as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

### Current Fields in the Enterprise Service Historical All Fields Grid View

Current fields are those fields that appear by default in
                                 a report generated from the stock template.

Column (Field)

Description

Enterprise Service

The enterprise name of the enterprise service.

Derived from: Enterprise_Service.EnterpriseName.

Peripheral Service

The enterprise name of the peripheral service.

Derived from: Service.EnterpriseName

DateTime

The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format.

DateTime Derived from:
                                             Service_Interval.DateTime.

Ans

The total number of tasks associated with the service
                                             that were answered by agents in the interval.

Derived from: Service_Interval.CallsAnswered.

Avg Speed of Answer

The average answer wait time in HH:MM:SS (hours,
                                             minutes, seconds) for all tasks answered for the service
                                             in the interval.

Derived from: Service_Interval.AvgSpeedAnswer.

Handled

The number of tasks associated with the service that
                                             were handled in the interval.

Derived from: Service_Interval.CallsHandled.

Avg Handle Time

The average handle time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service ending in
                                             the interval.

Derived from: Service_Interval.AvgHandleTime.

Abandoned Queue

The number of tasks associated with the service that
                                             were abandoned in queue in the interval.

Derived from: Service_Interval.CallsAbandQ.

Avg Delay Queue Abandoned

Average delay time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service that were
                                             abandoned in queue in the interval.

Derived from: Service_Interval.AvgDelayQAband.

Task Queue

The number of tasks associated with the service that
                                             were queued in the interval.

Derived from: Service_Interval.CallsQ.

Avg Delay Queue

The average delay in the queue for the tasks
                                             associated with the service in the interval.

Derived from: Service_Interval.AvgDelayQ.

Service Level

The number of tasks associated with the service answered within the Unified ICM/Unified CCE service level threshold in the interval.

Derived from: Service_Interval.ServiceLevel.

Service Level Type

The default value that indicates how Unified ICM software calculates the service level (that is, how it handles abandoned calls in calculating the service level). You can
                                             override this default for individual services.

Derived From: Service_Interval.ServiceLevelType.

Transfer In

The number of tasks transferred into the service in
                                             the interval. The value is updated in the database when
                                             the call is completed.

Derived from: Service_Interval.TransferInCalls.

Transfer Out

The number of tasks transferred out of the service in
                                             the interval. The value is updated in the database when
                                             the transfer of the call is completed.

Derived from: Service_Interval.TransferOutCalls.

Out

The number of outbound tasks placed by agents
                                             associated with the service in the interval.

Derived from: Service_Interval.CallsOut.

RONA

The count of tasks that are redirected with no answer
                                             within the skill group service level threshold in the
                                             last interval.

Derived from:
                                             Service_Interval.ServiceLevelCallsDequeued.

Report Summary: The report has a summary row for each
                                 Enterprise Service in the table and a total summary for all Enterprise Services. For
                                 more information, see Report Summary Rows .

### Available Fields in the Enterprise Service Historical All Fields Grid View

Available fields for this report include the fields that appear by default as Current. Additional Available fields in this
                                 report are populated from the Service_Interval table as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

### Current Fields in the Enterprise Service Historical All Fields Grid View

Current fields are those fields that appear by default in
                                 a report generated from the stock template.

Column (Field)

Description

Enterprise Service

The enterprise name of the enterprise service.

Derived from: Enterprise_Service.EnterpriseName.

Peripheral Service

The enterprise name of the peripheral service.

Derived from: Service.EnterpriseName

DateTime

The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format.

DateTime Derived from:
                                             Service_Interval.DateTime.

Ans

The total number of tasks associated with the service
                                             that were answered by agents in the interval.

Derived from: Service_Interval.CallsAnswered.

Avg Speed of Answer

The average answer wait time in HH:MM:SS (hours,
                                             minutes, seconds) for all tasks answered for the service
                                             in the interval.

Derived from: Service_Interval.AvgSpeedAnswer.

Handled

The number of tasks associated with the service that
                                             were handled in the interval.

Derived from: Service_Interval.CallsHandled.

Avg Handle Time

The average handle time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service ending in
                                             the interval.

Derived from: Service_Interval.AvgHandleTime.

Abandoned Queue

The number of tasks associated with the service that
                                             were abandoned in queue in the interval.

Derived from: Service_Interval.CallsAbandQ.

Avg Delay Queue Abandoned

Average delay time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service that were
                                             abandoned in queue in the interval.

Derived from: Service_Interval.AvgDelayQAband.

Task Queue

The number of tasks associated with the service that
                                             were queued in the interval.

Derived from: Service_Interval.CallsQ.

Avg Delay Queue

The average delay in the queue for the tasks
                                             associated with the service in the interval.

Derived from: Service_Interval.AvgDelayQ.

Service Level

The number of tasks associated with the service answered within the Unified ICM/Unified CCE service level threshold in the interval.

Derived from: Service_Interval.ServiceLevel.

Service Level Type

The default value that indicates how Unified ICM software calculates the service level (that is, how it handles abandoned calls in calculating the service level). You can
                                             override this default for individual services.

Derived From: Service_Interval.ServiceLevelType.

Transfer In

The number of tasks transferred into the service in
                                             the interval. The value is updated in the database when
                                             the call is completed.

Derived from: Service_Interval.TransferInCalls.

Transfer Out

The number of tasks transferred out of the service in
                                             the interval. The value is updated in the database when
                                             the transfer of the call is completed.

Derived from: Service_Interval.TransferOutCalls.

Out

The number of outbound tasks placed by agents
                                             associated with the service in the interval.

Derived from: Service_Interval.CallsOut.

RONA

The count of tasks that are redirected with no answer
                                             within the skill group service level threshold in the
                                             last interval.

Derived from:
                                             Service_Interval.ServiceLevelCallsDequeued.

Report Summary: The report has a summary row for each
                                 Enterprise Service in the table and a total summary for all Enterprise Services. For
                                 more information, see Report Summary Rows .

## Enterprise Skill
                        	 Group Historical All Fields

Use this report to review key
                              				statistics like incoming call rates and average speed of answer for Enterprise Skill
                              				Groups. Enterprise Skill Groups provide the ability to group skill groups within a
                              				peripheral or in different peripherals.

Applicable Environment: Unified CCE and Unified ICM

Query: This report data
                              				is built from a Database Query.

Views: This report has one grid view, Enterprise Skill Group Historical All Fields.

Grouping: This report is
                              				grouped by Enterprise Skill Group.

Value List: Enterprise Skill Group

This template also contains fields from entskg25: ICM Enterprise Skill Group Consolidated Half Hour, from entskg27: Enterprise Skill Group Historical All Fields, and calculated
                              fields from entskg08: FTE for Enterprise Skill Groups Half Hour.

Database Schema Tables from
                                 					which data is retrieved:

Enterprise_Skill_Group

Enterprise_Skill_Group_Member

Skill_Group

Skill_Group_Interval

Media_Routing_Domain

### Available Fields in the Enterprise Skill Group Historical All Fields Grid View

Available fields for this report include the fields that appear by
                                 default as Current. Additional Available fields in this report are derived from
                                 the Skill_Group_Interval table as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

One exception is Enterprise Skill Group , which is
                                 derived from: Enterprise_Skill_Group.EnterpriseName.

Most fields
                                 take their value directly from the database.

Exceptions
                                 are the FTE Agent State fields. These are calculated based on how you have
                                 configured interval reporting. For example, FTE Agents Active is derived from: (Skill_Group_Interval.TalkTime / 1800) or from
                                 (Skill_Group_Interval.TalkTime / 900).

### Current Fields in the Enterprise Skill Group Historical All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column (Field

Description

Enterprise Skill Group

The enterprise skill group's enterprise name and ID.

Derived from: Enterprise_Skill_Group.EnterpriseName (Enterprise_Skill_Group.EnterpriseSkillGroupID).

DateTime

The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format.

Derived from: Skill_Group_Interval.DateTime.

Ent Queued

The number of tasks queued to this Skill Group in the interval. Derived from: Skill_Group_Interval.RouterCallsQueued.

This field is Current by default and is applicable to Unified CCE only . The equivalent field for Unified CCE is named Total Queued (ICM) is Available by default.

Avg Speed of Answer

The skill group's average speed of answer in HH:MM:SS (hour, minutes, seconds) calculated from the time spent by callers when
                                             placed in queue and ringing at the agent's desktop before the task is answered divided by the number of tasks answered.

Derived from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered.

COMPLETED TASKS

Total

The total number of tasks completed by this skill group in the interval.

Derived from: (Skill_Group_Interval.CallsHandled + Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonRingCalls
                                             + Skill_Group_Interval.RedirectNoAnswer).

Abandoned

For voice: the total number of calls that were abandoned while the agent's phone was ringing. For non-voice: the total number
                                             of tasks that were abandoned while being offered to an agent.

Derived from: (Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonCallsRing ).

RONA

The number of ACD calls to the skill group that rang at an agent's terminal and redirected on failure to answer. The value
                                             is counted at the time the call is diverted to another device, and the database is updated every reporting.

Handled

The number of Routed tasks handled within this skill group in the interval.

Derived from: Skill_Group_Interval.CallsHandled.

Avg Handle Time

The Average Handle Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the skill group.

Derived from: Skill_Group_Interval.HandledCallsTime / Skill_Group_Interval.CallsHandled.

Avg Active Time

The Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the skill group.

Derived from: Skill_Group_Interval.HandledCallsTalkTime / Skill_Group_Interval.CallsHandled.

Abandon Hold

The number of tasks offered to the skill group that abandoned while being held or paused by the agent. The value is incremented
                                             at the time the call disconnects.

Derived from: Skill_Group_Interval.AbandonHoldCalls.

End of Completed Tasks Grouping

Transfer In

The time in HH:MM:SS (hours, minutes, seconds) that handling calls transferred into the skill group in the interval.

Derived from: Skill_Group_Interval.TransferInCallsTime.

Transfer Out

The number of tasks transferred out of the service in the interval. The value is updated in the database when the transfer
                                             of the call is completed.

Derived from: Service_Interval.TransferOutCalls.

External Out

The number of completed outbound ACD calls made by agents in the skill group, during a interval. The value is updated in the
                                             database when any after-call work time associated with the call is completed.

Derived from: Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIMES

Active Time

The total time spent in the Active state within this skill group in the interval, measured in HH:MM:SS (hours, minutes, seconds)
                                             format.

Derived from: Skill_Group_Interval.TalkTime.

Hold Time

The total time agents spent in the Hold/Paused state in this skill group in the interval, measured in HH:MM:SS (hours, minutes,
                                             seconds) format.

Derived from: Skill_Group_Interval.HoldTime.

Log On Duration

The total time in the interval the agents were logged into this skill group, measured in HH:MM:SS (hours, minutes, seconds)
                                             format.

Derived from: Skill_Group_Interval.LoggedOnTime.

% Not Active

The percentage of time that agents have spent in the Not Active or Available state in relation to LoggedOnTime or the interval,
                                             whichever is less.

Derived from: (Skill_Group_Interval.AvailTime / Skill_Group_Interval.LoggedOnTime).

% Not Ready

The percentage of time that agents spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever is
                                             less.

Derived from: (Skill_Group_Interval.NotReadyTime / Skill_Group_Interval.LoggedOnTime).

% Active

The percentage of time the interval that the agent of this skill group has spent in Active state in this Skill Group in relation
                                             to LoggedOnTime.

Derived from: Skill_Group_Interval.TalkTime / Skill_Group_Interval.LoggedOnTime.

% Hold

The percentage of time the interval that agents have put a call from this skill group on hold in relation to LoggedOnTime.

Derived from: (Skill_Group_Interval.HoldTime / Skill_Group_Interval.LoggedOnTime).

% Reserved

The percentage of time the interval that agents have spent in Reserved state waiting for an ICM routed call from this skill group in relation to LoggedOnTime.

Derived from: (Skill_Group_Interval.ReservedStateTime / Skill_Group_Interval.LoggedOnTime).

% Wrap Up

The percentage of time the interval that agents have spent in Wrap-up state after incoming or outgoing tasks in relation to
                                             LoggedOnTime or interval, whichever is less.

Derived from: (Skill_Group_Interval.WorkReadyTime + Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime).

Report Summary: There is a summary for each Enterprise Skill
                                 				Group and a total report summary. The summary line displays the Max for MaxQueued
                                 				and RouterQueueCalls.

### Available Fields in the Enterprise Skill Group Historical All Fields Grid View

Available fields for this report include the fields that appear by
                                 default as Current. Additional Available fields in this report are derived from
                                 the Skill_Group_Interval table as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

One exception is Enterprise Skill Group , which is
                                 derived from: Enterprise_Skill_Group.EnterpriseName.

Most fields
                                 take their value directly from the database.

Exceptions
                                 are the FTE Agent State fields. These are calculated based on how you have
                                 configured interval reporting. For example, FTE Agents Active is derived from: (Skill_Group_Interval.TalkTime / 1800) or from
                                 (Skill_Group_Interval.TalkTime / 900).

### Current Fields in the Enterprise Skill Group Historical All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column (Field

Description

Enterprise Skill Group

The enterprise skill group's enterprise name and ID.

Derived from: Enterprise_Skill_Group.EnterpriseName (Enterprise_Skill_Group.EnterpriseSkillGroupID).

DateTime

The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format.

Derived from: Skill_Group_Interval.DateTime.

Ent Queued

The number of tasks queued to this Skill Group in the interval. Derived from: Skill_Group_Interval.RouterCallsQueued.

This field is Current by default and is applicable to Unified CCE only . The equivalent field for Unified CCE is named Total Queued (ICM) is Available by default.

Avg Speed of Answer

The skill group's average speed of answer in HH:MM:SS (hour, minutes, seconds) calculated from the time spent by callers when
                                             placed in queue and ringing at the agent's desktop before the task is answered divided by the number of tasks answered.

Derived from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered.

COMPLETED TASKS

Total

The total number of tasks completed by this skill group in the interval.

Derived from: (Skill_Group_Interval.CallsHandled + Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonRingCalls
                                             + Skill_Group_Interval.RedirectNoAnswer).

Abandoned

For voice: the total number of calls that were abandoned while the agent's phone was ringing. For non-voice: the total number
                                             of tasks that were abandoned while being offered to an agent.

Derived from: (Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonCallsRing ).

RONA

The number of ACD calls to the skill group that rang at an agent's terminal and redirected on failure to answer. The value
                                             is counted at the time the call is diverted to another device, and the database is updated every reporting.

Handled

The number of Routed tasks handled within this skill group in the interval.

Derived from: Skill_Group_Interval.CallsHandled.

Avg Handle Time

The Average Handle Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the skill group.

Derived from: Skill_Group_Interval.HandledCallsTime / Skill_Group_Interval.CallsHandled.

Avg Active Time

The Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the skill group.

Derived from: Skill_Group_Interval.HandledCallsTalkTime / Skill_Group_Interval.CallsHandled.

Abandon Hold

The number of tasks offered to the skill group that abandoned while being held or paused by the agent. The value is incremented
                                             at the time the call disconnects.

Derived from: Skill_Group_Interval.AbandonHoldCalls.

End of Completed Tasks Grouping

Transfer In

The time in HH:MM:SS (hours, minutes, seconds) that handling calls transferred into the skill group in the interval.

Derived from: Skill_Group_Interval.TransferInCallsTime.

Transfer Out

The number of tasks transferred out of the service in the interval. The value is updated in the database when the transfer
                                             of the call is completed.

Derived from: Service_Interval.TransferOutCalls.

External Out

The number of completed outbound ACD calls made by agents in the skill group, during a interval. The value is updated in the
                                             database when any after-call work time associated with the call is completed.

Derived from: Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIMES

Active Time

The total time spent in the Active state within this skill group in the interval, measured in HH:MM:SS (hours, minutes, seconds)
                                             format.

Derived from: Skill_Group_Interval.TalkTime.

Hold Time

The total time agents spent in the Hold/Paused state in this skill group in the interval, measured in HH:MM:SS (hours, minutes,
                                             seconds) format.

Derived from: Skill_Group_Interval.HoldTime.

Log On Duration

The total time in the interval the agents were logged into this skill group, measured in HH:MM:SS (hours, minutes, seconds)
                                             format.

Derived from: Skill_Group_Interval.LoggedOnTime.

% Not Active

The percentage of time that agents have spent in the Not Active or Available state in relation to LoggedOnTime or the interval,
                                             whichever is less.

Derived from: (Skill_Group_Interval.AvailTime / Skill_Group_Interval.LoggedOnTime).

% Not Ready

The percentage of time that agents spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever is
                                             less.

Derived from: (Skill_Group_Interval.NotReadyTime / Skill_Group_Interval.LoggedOnTime).

% Active

The percentage of time the interval that the agent of this skill group has spent in Active state in this Skill Group in relation
                                             to LoggedOnTime.

Derived from: Skill_Group_Interval.TalkTime / Skill_Group_Interval.LoggedOnTime.

% Hold

The percentage of time the interval that agents have put a call from this skill group on hold in relation to LoggedOnTime.

Derived from: (Skill_Group_Interval.HoldTime / Skill_Group_Interval.LoggedOnTime).

% Reserved

The percentage of time the interval that agents have spent in Reserved state waiting for an ICM routed call from this skill group in relation to LoggedOnTime.

Derived from: (Skill_Group_Interval.ReservedStateTime / Skill_Group_Interval.LoggedOnTime).

% Wrap Up

The percentage of time the interval that agents have spent in Wrap-up state after incoming or outgoing tasks in relation to
                                             LoggedOnTime or interval, whichever is less.

Derived from: (Skill_Group_Interval.WorkReadyTime + Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime).

Report Summary: There is a summary for each Enterprise Skill
                                 				Group and a total report summary. The summary line displays the Max for MaxQueued
                                 				and RouterQueueCalls.

## Trunk Group And IVR Ports Performance Historical

Use this report to determine the business of the Cisco IVR and to evaluate information like percentage busy to help with IVR
                              capacity planning.

You can use the report for Trunk Groups associated with TDM peripherals.

Query: This report data is built from a Database Query.

Views: This report has one grid view, Trunk Group and IVR Ports Performance Historical.

Grouping: This report is grouped by Trunk Group and IVR Ports.

Value List: Trunk

Database Schema Tables from which data is retrieved: Trunk Group and Trunk_Group_Half_Hour.

### Available Fields in the Trunk Group And IVR Ports Performance Historical Grid View

Additional
                                 		  Available fields for this template are populated from the Trunk Group and
                                 		  Trunk_Group_Half_Hour tables as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

### Current Fields in the Trunk Group And IVR Ports Performance Historical Grid View

Current fields are those fields that appear by default in
                                 a grid view report generated from the stock template.

Column (Field)

Description

IVR Ports

The name of the IVR port used by the trunk group.

Derived from: Trunk_Group.EnterpriseName.

DateTime

The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format.

Derived from: Trunk_Group_Half_Hour.DateTime.

Ports

The number of ports in the group in service at the end
                                             of the interval.

Derived from: Trunk_Group_Half_Hour.TrunksInService.

% Busy

The percentage of time that the trunk groups in
                                             service were in use in the interval (for Inbound Only).

Derived from: Trunk_Group_Half_Hour.InUseInboundTime
                                             / Trunk_Group_Half_Hour.InServiceTime.

All Ports Busy

The total time, in HH:MM:SS (hours, minutes, seconds),
                                             in the interval, that all ports in the group were busy.

Derived from: Trunk_Group_Half_Hour.AllTrunksBusy.

Report Summary

This report has a Group Summary for each IVR Port for each interval. It
                                 also has a Report Summary showing all fields for all IVR Ports. For more information, see Report Summary Rows .

### Available Fields in the Trunk Group And IVR Ports Performance Historical Grid View

Additional
                                 		  Available fields for this template are populated from the Trunk Group and
                                 		  Trunk_Group_Half_Hour tables as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

### Current Fields in the Trunk Group And IVR Ports Performance Historical Grid View

Current fields are those fields that appear by default in
                                 a grid view report generated from the stock template.

Column (Field)

Description

IVR Ports

The name of the IVR port used by the trunk group.

Derived from: Trunk_Group.EnterpriseName.

DateTime

The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format.

Derived from: Trunk_Group_Half_Hour.DateTime.

Ports

The number of ports in the group in service at the end
                                             of the interval.

Derived from: Trunk_Group_Half_Hour.TrunksInService.

% Busy

The percentage of time that the trunk groups in
                                             service were in use in the interval (for Inbound Only).

Derived from: Trunk_Group_Half_Hour.InUseInboundTime
                                             / Trunk_Group_Half_Hour.InServiceTime.

All Ports Busy

The total time, in HH:MM:SS (hours, minutes, seconds),
                                             in the interval, that all ports in the group were busy.

Derived from: Trunk_Group_Half_Hour.AllTrunksBusy.

Report Summary

This report has a Group Summary for each IVR Port for each interval. It
                                 also has a Report Summary showing all fields for all IVR Ports. For more information, see Report Summary Rows .

## Peripheral Service Historical All Fields

With ICM, the Peripheral Service Historical report provides summary interval information such as calls handled and average speed of answer
                              for services. For information on mapping TDM entities, such as VDNs in Avaya, see the relevant ACD supplement. Peripheral
                              Service reports are not applicable to Contact Center Enterprise environments.

Query: This report data
                              		  is built from a Database Query.

Views: This report has one grid view, Peripheral Service Historical All Fields.

Grouping: This report is grouped by Service.

Value List: Service

Database Schema Tables from which data is retrieved:

Service

Service_Interval

### Available Fields in the Peripheral Service Historical All Fields Grid View

Available fields for this report grid include the fields that appear by
                                 default as Current. Additional Available fields in this report are populated
                                 from the Service_Interval table as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

The exception is the Service field, which is derived from
                                 Service.ServiceName.

### Current Fields in the Peripheral Service Historical All Fields Grid View

Current fields are those fields that appear by default in
                                 a report grid generated from the stock template.

Current fields are listed in the order (left to right) in which they
                                 appear by default in the stock template.

Column (Field)

Description

Service

The enterprise name of the peripheral service.

Derived from: Service.EnterpriseName.

DateTime

The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format.

Derived from: Service_Interval.DateTime.

Answered

The total number of tasks associated with the service
                                             that were answered by agents in the interval.

Derived from: Service_Interval.CallsAnswered.

Avg Speed of Answer

The average answer wait time in HH:MM:SS (hours,
                                             minutes, seconds) for all tasks answered for the service
                                             in the interval.

Derived from: Service_Interval.AvgSpeedAnswer.

Handled

The number of tasks associated with the service that
                                             were handled in the interval.

Derived from: Service_Interval.CallsHandled.

Avg Handle Time

The average handle time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service ending in
                                             the interval.

Derived from:  Service_Interval.HandleTime / Service_Interval.CallsHandled.

Aban in Queue

The number of tasks associated with the service that
                                             were abandoned in queue in the interval.

Derived from: Service_Interval.CallsAbandQ.

Average Delay Queue Abandon

The average delay time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service that were
                                             abandoned in queue in the interval.

Derived from:  Serivce_Interval.DelayQAbandTime / Service_Interval.CallsAbandQ.

Task In Queue

The total number of tasks associated with the service
                                             that were queued in the interval.

Derived from: Service_Interval.CallsQ.

Avg Delay in Queue

The average delay in queue for tasks associated with
                                             the service in the interval.

Derived from: Service_Interval.AvgDelayQ.

Service Level

The Enterprise service level for the service in the
                                             interval.

Derived from: Service_Interval.ServiceLevel.

Service Level Type

The default value that indicates how the service level is calculated by the ICM software (that is, how abandoned calls are handled in calculating the service level). You can override this default for individual
                                             services.

Derived From: Service_Interval.ServiceLevelType.

Transfer In

The number of tasks transferred into the service in
                                             the interval. The value is updated in the database when
                                             the call is completed.

Derived from: Service_Interval.TransferInCalls.

Transfer Out

The number of tasks transferred out of the service in
                                             the interval. The value is updated in the database when
                                             the transfer of the call is completed.

Derived from: Service_Interval.TransferOutCalls.

Out

The number of outbound tasks placed by agents
                                             associated with the service in the interval.

Derived from: Service_Interval.CallsOut.

RONA

The count of calls that are redirected with no answer
                                             within the skill group service level threshold in the
                                             last interval.

Derived from:
                                             Service_Interval.RedirectNoAnsCalls.

Report Summary: The report has a summary row for each
                                 Service and a total summary for all Services. For more information, see Report Summary Rows .

### Available Fields in the Peripheral Service Historical All Fields Grid View

Available fields for this report grid include the fields that appear by
                                 default as Current. Additional Available fields in this report are populated
                                 from the Service_Interval table as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

The exception is the Service field, which is derived from
                                 Service.ServiceName.

### Current Fields in the Peripheral Service Historical All Fields Grid View

Current fields are those fields that appear by default in
                                 a report grid generated from the stock template.

Current fields are listed in the order (left to right) in which they
                                 appear by default in the stock template.

Column (Field)

Description

Service

The enterprise name of the peripheral service.

Derived from: Service.EnterpriseName.

DateTime

The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format.

Derived from: Service_Interval.DateTime.

Answered

The total number of tasks associated with the service
                                             that were answered by agents in the interval.

Derived from: Service_Interval.CallsAnswered.

Avg Speed of Answer

The average answer wait time in HH:MM:SS (hours,
                                             minutes, seconds) for all tasks answered for the service
                                             in the interval.

Derived from: Service_Interval.AvgSpeedAnswer.

Handled

The number of tasks associated with the service that
                                             were handled in the interval.

Derived from: Service_Interval.CallsHandled.

Avg Handle Time

The average handle time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service ending in
                                             the interval.

Derived from:  Service_Interval.HandleTime / Service_Interval.CallsHandled.

Aban in Queue

The number of tasks associated with the service that
                                             were abandoned in queue in the interval.

Derived from: Service_Interval.CallsAbandQ.

Average Delay Queue Abandon

The average delay time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service that were
                                             abandoned in queue in the interval.

Derived from:  Serivce_Interval.DelayQAbandTime / Service_Interval.CallsAbandQ.

Task In Queue

The total number of tasks associated with the service
                                             that were queued in the interval.

Derived from: Service_Interval.CallsQ.

Avg Delay in Queue

The average delay in queue for tasks associated with
                                             the service in the interval.

Derived from: Service_Interval.AvgDelayQ.

Service Level

The Enterprise service level for the service in the
                                             interval.

Derived from: Service_Interval.ServiceLevel.

Service Level Type

The default value that indicates how the service level is calculated by the ICM software (that is, how abandoned calls are handled in calculating the service level). You can override this default for individual
                                             services.

Derived From: Service_Interval.ServiceLevelType.

Transfer In

The number of tasks transferred into the service in
                                             the interval. The value is updated in the database when
                                             the call is completed.

Derived from: Service_Interval.TransferInCalls.

Transfer Out

The number of tasks transferred out of the service in
                                             the interval. The value is updated in the database when
                                             the transfer of the call is completed.

Derived from: Service_Interval.TransferOutCalls.

Out

The number of outbound tasks placed by agents
                                             associated with the service in the interval.

Derived from: Service_Interval.CallsOut.

RONA

The count of calls that are redirected with no answer
                                             within the skill group service level threshold in the
                                             last interval.

Derived from:
                                             Service_Interval.RedirectNoAnsCalls.

Report Summary: The report has a summary row for each
                                 Service and a total summary for all Services. For more information, see Report Summary Rows .

## Peripheral Skill Group Historical All Fields

Peripheral Skill Group reports show
                              key statistics per skill group such as average
                              speed of answer and calls handled, as well as
                              agent state times per skill group. Use this report
                              to evaluate skill group performance.

Note: Completed tasks are all the tasks that
                              completed during the time shown (that is, on the
                              row in the report). This includes any tasks which
                              began before the time frame shown. However, this
                              does not include tasks where the caller abandoned
                              in the local ACD queue.

This report displays the same data
                              as the Enterprise Skill Group Historical report
                              except that this report is organized by media
                              rather then by skill group.

Query: This report data is built from a
                              Database Query.

Views: This report has a grid view (Peripheral Skill Group Historical All Fields) and a stacked bar chart view (Service Level).

Grouping: This report is grouped by Skill
                              Group.

Value Lists: Skill Group, Media Routing
                              Domain

Database Schema Tables from which
                                 data is retrieved:

Media_Routing_Domain

Skill_Group

Skill_Group_Interval

### Available Fields in
                           	 the Peripheral Skill Group Historical Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. In addition,
                                 		  most Available fields in this report are derived from the Skill_Group_Interval
                                 		  table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

One exception is Enterprise Skill
                                    			 Group , which is derived from: Enterprise_Skill_Group.EnterpriseName.

Most fields but one
                                 		  take their value directly from the database.

Exceptions are the
                                 		  FTE Agent State fields. These are calculated based on how you have configured
                                 		  interval reporting. For example, FTE Agents Active is derived from:
                                 		  (Skill_Group_Interval.TalkTime / 1800) or from (Skill_Group_Interval.TalkTime /
                                 		  900).

### Current Fields in
                           	 the Peripheral Skill Group Historical Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Skill Group

The
                                             						skill group's enterprise name and ID.

Derived
                                             						from:  Skill_Group.EnterpriseName (Skill_Group.SkillTargetID).

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

DateTime

The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format.

Derived
                                             						from: Skill_Group_Interval.DateTime.

Ent Queued

The number
                                             						of tasks queued to this Skill Group in the interval.

Derived
                                             						from:  Skill_Group_Interval.RouterQueueCalls + Skill_Group_Interval.CallsQueued.

This field is Current by default and is applicable to Unified CCE only. The equivalent field for Unified CCE is named Total Queued (ICM) is Available by default.

Avg Speed of Answer

The skill
                                             						group's average speed of answer in HH:MM:SS (hour, minutes, seconds) calculated
                                             						from the time spent by callers when placed in queue and ringing at the agent's
                                             						desktop before the task is answered divided by the number of tasks answered.

Derived
                                             						from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered.

SERVICE LEVEL

Service Level Answer

The count
                                             						of calls that are routed to the skill group or queued to the skill group in the
                                             						last interval.

Derived
                                             						from: Skill_Group_Interval.ServiceLevelCalls.

Service Level Abandon

The count
                                             						of calls that are abandoned within the skill group service level threshold in
                                             						the last interval.

Derived
                                             						from:  Skill_Group_Interval.ServiceLevelCallsAband.

COMPLETED TASKS

Total

The total
                                             						number of tasks completed by this skill group in the interval.

Derived
                                             						from: (Skill_Group_Interval.CallsHandled +
                                             						Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonRingCalls
                                             						+ Skill_Group_Interval.RedirectNoAnswer).

Abandoned

For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing. For non-voice: the total number of tasks that were abandoned while
                                             						being offered to an agent.

Derived
                                             						from: (Skill_Group_Interval.RouterCallsAbandQ +
                                             						Skill_Group_Interval.AbandonCallsRing).

RONA

The count of calls that are redirected with no answer within the skill group service level threshold in the last interval.

Derived
                                             						from:  Skill_Group_Interval.RedirectNoAnsCalls.

Handled

The number
                                             						of Routed tasks handled within this skill group in the interval.

Derived
                                             						from: Skill_Group_Interval.CallsHandled.

Avg Handle Time

The
                                             						Average Handle Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						skill group.

Derived
                                             						from: Skill_Group_Interval.HandledCallsTime /
                                             						Skill_Group_Interval.CallsHandled.

Avg Active Time

The
                                             						Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						skill group.

Derived
                                             						from: Skill_Group_Interval.HandledCallsTalkTime /
                                             						Skill_Group_Interval.CallsHandled.

Abandon Hold

The number
                                             						of tasks offered to the skill group that abandoned while being held or paused
                                             						by the agent. The value is incremented at the time the call disconnects.

Derived
                                             						from: Skill_Group_Interval.AbandonHoldCalls.

Tasks Picked

The total number of pick requests successfully routed to this skill group in the reporting interval.

Tasks Pulled

The total number of pull requests successfully routed to this skill group in the reporting interval.

Picks Failed

Number of Pick request resulting in an error.

Pulls Failed

Number of Pull request resulting in an error.

End of Completed Tasks
                                                						  Grouping

Transfer In

The number of tasks transferred into the skill group in the interval. The value is updated in the database when the call
                                             is completed.

Derived
                                             						from:  Skill_Group_Interval.TransferInCalls.

Transfer Out

The number
                                             						of tasks this agent transferred to another agent or skill group in the
                                             						interval. This includes Consultative Calls. The value is updated in the
                                             						database when the transfer of the call is completed.

Derived
                                             						from: Skill_Group_Interval.TransferredOutCalls +
                                             						Skill_Group_Interval.NetTransferredOutCalls.

External Out

For
                                             						default skill groups: the number of times an agent initiated an outgoing
                                             						external call in the interval. For routing skill groups: the number of times an
                                             						agent initiated a transfer or conference to an external device in the interval.

Derived
                                             						from: Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIME

Active
                                             						Time

The time
                                             						in HH:MM:SS (hours, minutes, seconds) that agents in the skill group were in
                                             						the Active state in the interval.

Derived
                                             						from: Skill_Group_Interval.TalkTime.

Hold Time

The total
                                             						time agents spent in the Hold/Paused state in this skill group, measured in
                                             						HH:MM:SS (hours, minutes, seconds) format. Includes Incoming Direct and
                                             						Outgoing Internal, although call counts are not shown in this report.

Derived
                                             						from: Skill_Group_Interval.HoldTime.

Logged On Duration

The total duration in HH:MM:SS (hours, minutes, and seconds)
                                             									during the period that agents were logged into this skill group.

Derived from: Skill_Group_Interval.LoggedOnTime

% Not
                                             						Active

The
                                             						percentage of agents in the skill group who are NOT currently involved in tasks
                                             						and who are ready to accept calls or tasks.

Derived
                                             						from:  Skill_Group_Interval.AvailTime / Skill_Group_Interval.LoggedOnTime.

% Not
                                             						Ready

The
                                             						percentage of time that agents spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less.

Derived
                                             						from: (Skill_Group_Interval.NotReadyTime / Skill_Group_Interval.LoggedOnTime).

% Active

The
                                             						percentage of agents in the skill group who are working on incoming tasks or
                                             						who are in one of the talking states.

Derived
                                             						from: (Skill_Group_Skill_Group_Interval.TalkingInTime + Skill_Group_Skill_Group_Interval.TalkingOutTime +
                                             						Skill_Group_Skill_Group_Interval.TalkingOtherTime + Skill_Group.Skill_Group_Interval.TalkingAutoOutTime +
                                             						Skill_Group.Skill_Group_Interval.TalkingPreviewTime + Skill_Group.Skill_Group_Interval.TalkingReserveTime) /
                                             						Skill_Group_Skill_Group_Interval.LoggedOnTime.

% Hold

The
                                             						percentage of time that agents spent in the Hold/Paused state in relation to
                                             						LoggedOnTime or interval, whichever is less.

Derived
                                             						from: (Skill_Group_Interval.HoldTime / Skill_Group_Interval.LoggedOnTime).

%
                                             						Reserved

The
                                             						percentage of time that agents spent working on Reserved time in relation to
                                             						LoggedOnTime or interval, whichever is less.

Derived
                                             						from: (Skill_Group_Interval. ReservedStateTime /
                                             						Skill_Group_Interval.LoggedOnTime).

% Wrap
                                             						Up

The
                                             						percentage of time that agents have spent in Wrap-up state after incoming or
                                             						outgoing calls in relation to LoggedOnTime or interval, whichever is less.

Derived
                                             						from: ((Skill_Group_Interval.WorkReadyTime +
                                             						Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime).

Max Queued

The
                                             						maximum number of calls in queue for this call type during this interval.

Derived
                                             						from: Skill_Group_Interval.RouterMaxCallsQueued.

Longest Queued

The
                                             						longest time a call had to wait before it was dispositioned
                                             						(abandoned, answered, and so on) in this interval.

Derived
                                             						from: Skill_Group_Interval.RouterMaxCallWaitTime.

Abandon Rings

The
                                             						total number of ACD calls to the skill group that were abandoned while ringing
                                             						at an agent's position. The value is incremented at the time the call
                                             						disconnects.

Derived
                                             						from: Skill_Group_Interval.AbandonRingCalls.

Answered

The
                                             						number of calls answered by agents associated with a skill group during the
                                             						reporting interval. This value is set by the PG. The number of calls answered
                                             						includes only handled calls and internal calls received. The value is
                                             						incremented at the time the call is answered.

Derived
                                             						from: Skill_Group_Interval.CallsAnswered.

Report Summary: There is a summary for each Skill Group and
                                 				a total report summary. The summary line displays the Max for MaxQueued and
                                 				RouterQueueCalls. For more information, see Report Summary Rows .

### Available Fields in
                           	 the Peripheral Skill Group Historical Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. In addition,
                                 		  most Available fields in this report are derived from the Skill_Group_Interval
                                 		  table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

One exception is Enterprise Skill
                                    			 Group , which is derived from: Enterprise_Skill_Group.EnterpriseName.

Most fields but one
                                 		  take their value directly from the database.

Exceptions are the
                                 		  FTE Agent State fields. These are calculated based on how you have configured
                                 		  interval reporting. For example, FTE Agents Active is derived from:
                                 		  (Skill_Group_Interval.TalkTime / 1800) or from (Skill_Group_Interval.TalkTime /
                                 		  900).

### Current Fields in
                           	 the Peripheral Skill Group Historical Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Skill Group

The
                                             						skill group's enterprise name and ID.

Derived
                                             						from:  Skill_Group.EnterpriseName (Skill_Group.SkillTargetID).

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

DateTime

The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format.

Derived
                                             						from: Skill_Group_Interval.DateTime.

Ent Queued

The number
                                             						of tasks queued to this Skill Group in the interval.

Derived
                                             						from:  Skill_Group_Interval.RouterQueueCalls + Skill_Group_Interval.CallsQueued.

This field is Current by default and is applicable to Unified CCE only. The equivalent field for Unified CCE is named Total Queued (ICM) is Available by default.

Avg Speed of Answer

The skill
                                             						group's average speed of answer in HH:MM:SS (hour, minutes, seconds) calculated
                                             						from the time spent by callers when placed in queue and ringing at the agent's
                                             						desktop before the task is answered divided by the number of tasks answered.

Derived
                                             						from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered.

SERVICE LEVEL

Service Level Answer

The count
                                             						of calls that are routed to the skill group or queued to the skill group in the
                                             						last interval.

Derived
                                             						from: Skill_Group_Interval.ServiceLevelCalls.

Service Level Abandon

The count
                                             						of calls that are abandoned within the skill group service level threshold in
                                             						the last interval.

Derived
                                             						from:  Skill_Group_Interval.ServiceLevelCallsAband.

COMPLETED TASKS

Total

The total
                                             						number of tasks completed by this skill group in the interval.

Derived
                                             						from: (Skill_Group_Interval.CallsHandled +
                                             						Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonRingCalls
                                             						+ Skill_Group_Interval.RedirectNoAnswer).

Abandoned

For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing. For non-voice: the total number of tasks that were abandoned while
                                             						being offered to an agent.

Derived
                                             						from: (Skill_Group_Interval.RouterCallsAbandQ +
                                             						Skill_Group_Interval.AbandonCallsRing).

RONA

The count of calls that are redirected with no answer within the skill group service level threshold in the last interval.

Derived
                                             						from:  Skill_Group_Interval.RedirectNoAnsCalls.

Handled

The number
                                             						of Routed tasks handled within this skill group in the interval.

Derived
                                             						from: Skill_Group_Interval.CallsHandled.

Avg Handle Time

The
                                             						Average Handle Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						skill group.

Derived
                                             						from: Skill_Group_Interval.HandledCallsTime /
                                             						Skill_Group_Interval.CallsHandled.

Avg Active Time

The
                                             						Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						skill group.

Derived
                                             						from: Skill_Group_Interval.HandledCallsTalkTime /
                                             						Skill_Group_Interval.CallsHandled.

Abandon Hold

The number
                                             						of tasks offered to the skill group that abandoned while being held or paused
                                             						by the agent. The value is incremented at the time the call disconnects.

Derived
                                             						from: Skill_Group_Interval.AbandonHoldCalls.

Tasks Picked

The total number of pick requests successfully routed to this skill group in the reporting interval.

Tasks Pulled

The total number of pull requests successfully routed to this skill group in the reporting interval.

Picks Failed

Number of Pick request resulting in an error.

Pulls Failed

Number of Pull request resulting in an error.

End of Completed Tasks
                                                						  Grouping

Transfer In

The number of tasks transferred into the skill group in the interval. The value is updated in the database when the call
                                             is completed.

Derived
                                             						from:  Skill_Group_Interval.TransferInCalls.

Transfer Out

The number
                                             						of tasks this agent transferred to another agent or skill group in the
                                             						interval. This includes Consultative Calls. The value is updated in the
                                             						database when the transfer of the call is completed.

Derived
                                             						from: Skill_Group_Interval.TransferredOutCalls +
                                             						Skill_Group_Interval.NetTransferredOutCalls.

External Out

For
                                             						default skill groups: the number of times an agent initiated an outgoing
                                             						external call in the interval. For routing skill groups: the number of times an
                                             						agent initiated a transfer or conference to an external device in the interval.

Derived
                                             						from: Skill_Group_Interval.AgentOutCalls.

AGENT STATE TIME

Active
                                             						Time

The time
                                             						in HH:MM:SS (hours, minutes, seconds) that agents in the skill group were in
                                             						the Active state in the interval.

Derived
                                             						from: Skill_Group_Interval.TalkTime.

Hold Time

The total
                                             						time agents spent in the Hold/Paused state in this skill group, measured in
                                             						HH:MM:SS (hours, minutes, seconds) format. Includes Incoming Direct and
                                             						Outgoing Internal, although call counts are not shown in this report.

Derived
                                             						from: Skill_Group_Interval.HoldTime.

Logged On Duration

The total duration in HH:MM:SS (hours, minutes, and seconds)
                                             									during the period that agents were logged into this skill group.

Derived from: Skill_Group_Interval.LoggedOnTime

% Not
                                             						Active

The
                                             						percentage of agents in the skill group who are NOT currently involved in tasks
                                             						and who are ready to accept calls or tasks.

Derived
                                             						from:  Skill_Group_Interval.AvailTime / Skill_Group_Interval.LoggedOnTime.

% Not
                                             						Ready

The
                                             						percentage of time that agents spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less.

Derived
                                             						from: (Skill_Group_Interval.NotReadyTime / Skill_Group_Interval.LoggedOnTime).

% Active

The
                                             						percentage of agents in the skill group who are working on incoming tasks or
                                             						who are in one of the talking states.

Derived
                                             						from: (Skill_Group_Skill_Group_Interval.TalkingInTime + Skill_Group_Skill_Group_Interval.TalkingOutTime +
                                             						Skill_Group_Skill_Group_Interval.TalkingOtherTime + Skill_Group.Skill_Group_Interval.TalkingAutoOutTime +
                                             						Skill_Group.Skill_Group_Interval.TalkingPreviewTime + Skill_Group.Skill_Group_Interval.TalkingReserveTime) /
                                             						Skill_Group_Skill_Group_Interval.LoggedOnTime.

% Hold

The
                                             						percentage of time that agents spent in the Hold/Paused state in relation to
                                             						LoggedOnTime or interval, whichever is less.

Derived
                                             						from: (Skill_Group_Interval.HoldTime / Skill_Group_Interval.LoggedOnTime).

%
                                             						Reserved

The
                                             						percentage of time that agents spent working on Reserved time in relation to
                                             						LoggedOnTime or interval, whichever is less.

Derived
                                             						from: (Skill_Group_Interval. ReservedStateTime /
                                             						Skill_Group_Interval.LoggedOnTime).

% Wrap
                                             						Up

The
                                             						percentage of time that agents have spent in Wrap-up state after incoming or
                                             						outgoing calls in relation to LoggedOnTime or interval, whichever is less.

Derived
                                             						from: ((Skill_Group_Interval.WorkReadyTime +
                                             						Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime).

Max Queued

The
                                             						maximum number of calls in queue for this call type during this interval.

Derived
                                             						from: Skill_Group_Interval.RouterMaxCallsQueued.

Longest Queued

The
                                             						longest time a call had to wait before it was dispositioned
                                             						(abandoned, answered, and so on) in this interval.

Derived
                                             						from: Skill_Group_Interval.RouterMaxCallWaitTime.

Abandon Rings

The
                                             						total number of ACD calls to the skill group that were abandoned while ringing
                                             						at an agent's position. The value is incremented at the time the call
                                             						disconnects.

Derived
                                             						from: Skill_Group_Interval.AbandonRingCalls.

Answered

The
                                             						number of calls answered by agents associated with a skill group during the
                                             						reporting interval. This value is set by the PG. The number of calls answered
                                             						includes only handled calls and internal calls received. The value is
                                             						incremented at the time the call is answered.

Derived
                                             						from: Skill_Group_Interval.CallsAnswered.

Report Summary: There is a summary for each Skill Group and
                                 				a total report summary. The summary line displays the Max for MaxQueued and
                                 				RouterQueueCalls. For more information, see Report Summary Rows .

## Precision Queue Abandon Answer Distribution Historical

Precision Queue Abandon Answer Distribution is used to identify where (in the routing) callers are abandoning and to identify
                              the typical wait times and caller tolerance. For each precision queue, reports generated from this template display the number
                              of answered and abandoned calls for separate intervals for the report time period, broken out into interval summaries.

Query: This report data
                              		  is built from a Database Query.

Views: This report has one grid view, Precision Queue Abandon Answer Distribution Historical.

Value Lists: Precision Queue, Media Routing Domain

Database Schema Tables from which data is retrieved:

Attribute

Bucket_Intervals

Precision_Queue

Media_Routing_Domain

Router_Queue_Interval

Skill_Group_Interval

### Available Fields
                           	 in the Precision Queue Abandon-Answer Distribution Historical Grid View

Available fields
                                 		  for this report include the fields that display by default as Current.
                                 		  Additional Available fields for this template are populated from the
                                 		  Skill_Group_Interval and Bucket_Intervals tables as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

The following
                                 		  fields are from the Skill_Group_Interval table:

Ans Wait Time: Derived
                                       				from Skill_Group_Interval.AnswerWaitTime

BucketIntervalID: Derived from Skill_Group_Interval.BucketIntervalID

Calls Handled: Derived
                                       				from Skill_Group_Interval.CallsHandled

SkillTargetID: Derived
                                       				from Skill_Group_Interval.SkillTargetID

DelayQAban: Derived
                                       				from Skill_Group_Interval.RouterDelayQAbandTime

Router Calls Aban: Derived from Skill_Group_Interval.RouterCallsAbandToAgent
                                       				+Skill_Group_Interval.RouterCallsAbandQ

The following
                                 		  Available fields are from the Bucket_Intervals table:

Interval 1 - Interval
                                    			 10: Derived from Bucket_Intervals.IntervalUpperBound1 - IntervalUpperBound9
                                 		  where the tenth interval is everything greater than UpperBound9.

### Current Fields in
                           	 the Precision Queue Abandon-Answer Distribution Historical Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column (Field)

Description

Precision Queue

The enterprise name of the Precision Queue and its precision queue ID.

Derived from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID

Media

The enterprise name of the Media Routing Domain associated with the precision queue.

Media is derived from: Media_Routing_Domain.EnterpriseName.

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date and time at the start of the reporting interval.

Derived from: Router_Queue_Interval.DateTime

Avg Speed of Answer

The precision queue average speed of answer in HH:MM:SS (hour, minutes, seconds) based on the time spent by callers in the
                                             queue and ringing at an agent desktop before the task is answered divided by the number of answered tasks.

Derived from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered

Interval 1 - Interval 10

Interval

The amount of time that a call should be handled by.

Derived from: Bucket_Interval.UpperBound1(through 9)

Answered

The number of calls answered in this interval.

Derived from: RouterQueueInterval.AnsInterval1 (through10)

Note : AnsInterval1 is the number of calls answered within Interval 1. For Call Type Interval, AnsInterval is calculated from the
                                             time the call is queued to a skill group or a precision queue, to the time the call is answered. This includes any requery
                                             time. This field is applicable to both Unified ICM and Unified CCE with the following exception:

The field is not incremented if the call is answered by an agent on a standard ACD unless the call was translation routed.

Abandoned

The number of calls abandoned in this interval.

Derived from: RouterQueueInterval.AbandInterval1 (through10)

Note : AbandInterval1 is the number of calls abandoned within Interval 1. For Call Type Interval, AbandInterval is calculated from
                                             the time the call is queued to a skill group or a precision queue, to the time the call is abandoned. This includes any requery
                                             time. This field is applicable to both Unified ICM and Unified CCE with the following exception:

The field is not incremented if the call is answered by an agent on a standard ACD unless the call was translation routed.

MaxQueued

The maximum number of calls in queue for this Skill Group during this interval.

Derived from: Skill_Group_Interval.RouterMaxCallsQueued

Longest Queued

The longest time a call elapsed before it was abandoned or answered in this interval.

Derived from: Skill_Group_Interval.RouterMaxCallWaitTime

### Available Fields
                           	 in the Precision Queue Abandon-Answer Distribution Historical Grid View

Available fields
                                 		  for this report include the fields that display by default as Current.
                                 		  Additional Available fields for this template are populated from the
                                 		  Skill_Group_Interval and Bucket_Intervals tables as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

The following
                                 		  fields are from the Skill_Group_Interval table:

Ans Wait Time: Derived
                                       				from Skill_Group_Interval.AnswerWaitTime

BucketIntervalID: Derived from Skill_Group_Interval.BucketIntervalID

Calls Handled: Derived
                                       				from Skill_Group_Interval.CallsHandled

SkillTargetID: Derived
                                       				from Skill_Group_Interval.SkillTargetID

DelayQAban: Derived
                                       				from Skill_Group_Interval.RouterDelayQAbandTime

Router Calls Aban: Derived from Skill_Group_Interval.RouterCallsAbandToAgent
                                       				+Skill_Group_Interval.RouterCallsAbandQ

The following
                                 		  Available fields are from the Bucket_Intervals table:

Interval 1 - Interval
                                    			 10: Derived from Bucket_Intervals.IntervalUpperBound1 - IntervalUpperBound9
                                 		  where the tenth interval is everything greater than UpperBound9.

### Current Fields in
                           	 the Precision Queue Abandon-Answer Distribution Historical Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column (Field)

Description

Precision Queue

The enterprise name of the Precision Queue and its precision queue ID.

Derived from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID

Media

The enterprise name of the Media Routing Domain associated with the precision queue.

Media is derived from: Media_Routing_Domain.EnterpriseName.

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date and time at the start of the reporting interval.

Derived from: Router_Queue_Interval.DateTime

Avg Speed of Answer

The precision queue average speed of answer in HH:MM:SS (hour, minutes, seconds) based on the time spent by callers in the
                                             queue and ringing at an agent desktop before the task is answered divided by the number of answered tasks.

Derived from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered

Interval 1 - Interval 10

Interval

The amount of time that a call should be handled by.

Derived from: Bucket_Interval.UpperBound1(through 9)

Answered

The number of calls answered in this interval.

Derived from: RouterQueueInterval.AnsInterval1 (through10)

Note : AnsInterval1 is the number of calls answered within Interval 1. For Call Type Interval, AnsInterval is calculated from the
                                             time the call is queued to a skill group or a precision queue, to the time the call is answered. This includes any requery
                                             time. This field is applicable to both Unified ICM and Unified CCE with the following exception:

The field is not incremented if the call is answered by an agent on a standard ACD unless the call was translation routed.

Abandoned

The number of calls abandoned in this interval.

Derived from: RouterQueueInterval.AbandInterval1 (through10)

Note : AbandInterval1 is the number of calls abandoned within Interval 1. For Call Type Interval, AbandInterval is calculated from
                                             the time the call is queued to a skill group or a precision queue, to the time the call is abandoned. This includes any requery
                                             time. This field is applicable to both Unified ICM and Unified CCE with the following exception:

The field is not incremented if the call is answered by an agent on a standard ACD unless the call was translation routed.

MaxQueued

The maximum number of calls in queue for this Skill Group during this interval.

Derived from: Skill_Group_Interval.RouterMaxCallsQueued

Longest Queued

The longest time a call elapsed before it was abandoned or answered in this interval.

Derived from: Skill_Group_Interval.RouterMaxCallWaitTime

## Precision Queue Efficiency

Precision Queue Efficiency reports the efficiency and effectiveness of the Precision Queue logic by identifying the disposition
                              of contacts per step.

Precision Queue Efficiency is an interval report.

The Precision Queue Efficiency report reflects trends across intervals and is not intended for reconciling the numbers within
                              an interval.

It is possible for a call to span intervals, therefore, a call may be offered in one time interval and answered in a second.

Views: This report has the following  grid views:

Precision Queue Efficiency

Precision Queue Efficiency All Fields

Query: This report data is built from a Database Query.

Grouping: This report is grouped by Precision Queue Name.

Value List: Precision Queue

Database Schema Tables from which data is retrieved:

Attribute

Precision_Queue

Router_Queue_Interval

### Available Fields in the Precision Queue Efficiency

Available fields for this report include the fields that appear by default as Current. Additional available fields in this
                              report are derived from the Router_Queue_Interval table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in the Precision Queue Efficiency Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

The following current fields are listed in the order (left to right) in which they appear by default in the stock template.

As Overflow and Skipped relate to following steps, they are inapplicable in step 10 (which has no following step) and, therefore, do not appear in
                              step 10 in the report.

Column (Field)

Description

Precision Queue

The enterprise name of the precision queue and its precision queue ID.

Derived from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID.

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date and time at the start of the reporting interval.

Derived from: Router_Queue_Interval.DateTime

Step 1 - Step 10

Offered

The number of calls offered in this step.

Derived from: Router_Queue_Interval.OfferedStep(n)

Answered

The total of all calls offered in this precision queue that were answered in this step.

Derived from: Router_Queue_Interval.AnsStep(n)

Chart

This is a link to a Precision Queue Efficiency Drill Down report. For more information, see Precision Queue Efficiency Drill Down .

### Current Fields in the Precision Queue Efficiency All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

The following current fields are listed in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Precision Queue

The enterprise name of the precision queue and its precision queue ID.

Derived from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID.

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date and time at the start of the reporting interval.

Derived from: Router_Queue_Interval.DateTime

Step 1 - Step 10

Offered

The number of calls offered in this step.

Derived from: Router_Queue_Interval.OfferedStep(n)

Skipped

The total of all calls offered in this precision queue that were skippeded in this step.

Derived from: Router_Queue_Interval.

Answered

The total of all calls offered in this precision queue that were answered in this step.

Derived from: Router_Queue_Interval.AnsStep(n)

Abandoned

The total of all calls offered in this precision queue that were abandoned in this step.

Derived from: Router_Queue_Interval.

Overflow

The total of all calls offered in this precision queue that overflowed.

Derived from: Router_Queue_Interval.

PreciscionQueueChart

This is a link to a Precision Queue Efficiency Drill Down report. For more information, see Precision Queue Efficiency Drill Down .

### Available Fields
                           	 in the Precision Queue Efficiency All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional available fields in this report are derived from the
                                 		  Router_Queue_Interval table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in
                           	 the Precision Queue Efficiency All Fields Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

The following
                                 		  current fields are listed in the order (left to right) in which they appear by
                                 		  default in the stock template.

As Overflow and Skipped relate to following steps, they are inapplicable in step 10 (which has no
                                 		  following step) and, therefore, do not appear in step 10 in the report.

Column
                                             						(Field)

Description

Precision Queue

The
                                             						enterprise name of the precision queue and its precision queue ID.

Derived
                                             						from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID.

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date
                                             						and time at the start of the reporting interval.

Derived
                                             						from: Router_Queue_Interval.DateTime

Step 1 - Step 10

Offered

The
                                             						number of calls offered in this step.

Derived
                                             						from: Router_Queue_Interval.OfferedStep(n)

Answered

The
                                             						total of all calls offered in this precision queue that were answered in this
                                             						step.

Derived
                                             						from: Router_Queue_Interval.AnsStep(n)

Chart

This is
                                             						a link to a Precision Queue Efficiency Drill Down report. For more information,
                                             						see Precision Queue Efficiency Drill Down .

### Available Fields
                           	 in the Precision Queue Efficiency All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional available fields in this report are derived from the
                                 		  Router_Queue_Interval table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in
                           	 the Precision Queue Efficiency All Fields Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

The following
                                 		  current fields are listed in the order (left to right) in which they appear by
                                 		  default in the stock template.

As Overflow and Skipped relate to following steps, they are inapplicable in step 10 (which has no
                                 		  following step) and, therefore, do not appear in step 10 in the report.

Column
                                             						(Field)

Description

Precision Queue

The
                                             						enterprise name of the precision queue and its precision queue ID.

Derived
                                             						from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID.

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

DateTime

The date
                                             						and time at the start of the reporting interval.

Derived
                                             						from: Router_Queue_Interval.DateTime

Step 1 - Step 10

Offered

The
                                             						number of calls offered in this step.

Derived
                                             						from: Router_Queue_Interval.OfferedStep(n)

Answered

The
                                             						total of all calls offered in this precision queue that were answered in this
                                             						step.

Derived
                                             						from: Router_Queue_Interval.AnsStep(n)

Chart

This is
                                             						a link to a Precision Queue Efficiency Drill Down report. For more information,
                                             						see Precision Queue Efficiency Drill Down .

## Precision Queue
                        	 Efficiency Drill Down

The Precision
                              		  Queue Efficiency Drill Down report is filtered by the Precision Queue name and an absolute Date Time range.  For each
                              15- or
                              		  30-minute interval in a time span, the percentage of calls that are answered
                              		  for each step of the Precision Queue are displayed on a stacked bar.

The Y axis is
                              		  percentage answered, and the X axis is time.

It is possible to
                              		  have more than 100% answered in a step because it is an interval based metric;
                              		  a call might have been offered in one time interval and answered in another.

If you select
                              		  multiple Precision Queues, the percent answered can grow to 200%.

The Precision
                              		  Queue Efficiency Drill Down report reflects trends across intervals and is not
                              		  intended for reconciling the numbers within an interval.

Query: This report data
                              		  is built from a Database Query.

Views: This report has a stacked bar chart view only.

Value List: Precision
                              		  Queue

Database Schema Tables from
                                 			 which data is retrieved:

Precision_Queue

Router_Queue_Interval

## Precision Queue Interval All Fields

Use this report to evaluate Precision Queue performance and staffing. Precision Queue Interval provides key statistics per
                              Precision Queue such as average speed of answer and contacts handled, as well as agent state times.   The Precision Queue
                              interval report is comparable to Peripheral Skill Group Historical.

Query: This report data
                              		  is built from a Database Query.

Views: This report has one grid view, Precision Queue Interval All Fields.

Grouping: This report is grouped by Precision Queue.

Value Lists: Precision Queue, Media Routing Domain

Database Schema Tables from which data is retrieved:

Attribute

Media_Routing_Domain

Precision_Queue

Router_Queue_Interval

Skill_Group_Interval

### Available Fields
                           	 in the Precision Queue Interval All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current. In
                                 		  addition, most Available fields in this report are derived from the
                                 		  Router_Queue_Interval and Skill_Group_Interval table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in
                           	 the Precision Queue Interval All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

The following current fields are listed in the order (left to right) in which they appear by default in the stock template.

Column
                                             						(Field)

Description

Precision Queue

The
                                             						enterprise name of the Agent Precision Queue.

Derived from: Precision_Queue.EnterpriseName.

Media

The
                                             						enterprise name of the Media Routing Domain associated with the precision
                                             						queue.

Media is derived
                                             						from: Media_Routing_Domain.EnterpriseName.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

DateTime

The
                                             						date and time of the data for a selected row.

Derived
                                             						from: Router_Queue_Interval.DateTime.

Queued

Derived
                                             						from: Router_Queue_Interval.QueueCalls.

Avg
                                             						Speed of Answer

The
                                             						precision queue average speed of answer in HH:MM:SS(hour, minutes, seconds)
                                             						based on the time spent by callers in the queue and ringing at an agent desktop
                                             						before the task is answered divided by the number of answered tasks.

Derived
                                             						from: Skill_Group_Interval.AnswerWaitTime /Skill_Group_Interval.CallsAnswered.

Service Level

Service Level

Service Level Type used to calculate Service level for the
                                             						interval.

Derived from: Router_Queue_Interval.ServiceLevel.

Answer

The
                                             						number of calls that are routed to the precision queue or queued to the
                                             						precision queue in the last interval.

Derived
                                             						from: Router_Queue_Interval.ServiceLevelCalls

Abandon

The
                                             						number of calls that are abandoned within the precision queue service level
                                             						threshold in the last interval.

Derived
                                             						from: Router_Queue_Interval.ServiceLevelCallsAband.

Completed Tasks

Total

The total number of tasks completed by this precision queue in the interval.

Derived from:(Router_Queue_Interval.CallsHandled++ Router_Queue_Interval.RedirectNoAnsCalls+ Router_Queue_Interval.CallsAbandQ+
                                             Router_Queue_Interval.RouterError+ Router_Queue_Interval.CallsAbandToAgent)

Abandoned

The
                                             						sum of:

The number of calls to the call type that are abandoned in the Router queue during the reporting interval.

The number of calls associated with this skillgroup that are abandoned at the agent desktop before being answered during the
                                                   reporting interval. Termination_Call_Detail records generated by agent PG with a Call Disposition Flag of 2 are also counted
                                                   for this field. This does not include short calls and the calls that were abandoned in the VRU.

Derived
                                             						from: Router_Queue_Interval.CallsAbandQ +

Router_Queue_Interval.CallsAbandToAgent.

RONA

The count of calls that are redirected with no answer within the Precision Queue service level threshold in the last interval.

Derived from: Router_Queue_Interval.RedirectNoAnsCalls

Handled

The number of inbound calls for which agents in the precision queue during the interval answered and completed.

Derived from: Router_Queue_Interval.CallsHandled.

Avg
                                             						Handle Time

The
                                             						average time spent by agents in this precision queue handling a task in the
                                             						interval.

This
                                             						field is a calculated field, derived from:
                                             						(Skill_Group_Interval.HandledCallsTime / Skill_Group_Interval.CallsHandled)

Avg
                                             						Active Time

The
                                             						Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						precision queue.

Derived
                                             						from: Skill_Group_Interval.HandledCallsTalkTime
                                             						/Skill_Group_Interval.CallsHandled

Abandon
                                             						Hold

The
                                             						number of tasks offered to the precision queue that are abandoned while being
                                             						held or paused by the agent. The value is incremented at the time the call
                                             						disconnects.

Derived
                                             						from: Skill_Group_Interval.AbandonHoldCalls

Tasks Picked

The total number of pick requests successfully routed by the precision queue.

Tasks Pulled

The total number of pull requests successfully routed by the precision queue.

Picks Failed

Number of pick request resulting in an error.

Pulls Failed

Number of pull request resulting in an error.

End of Completed Tasks Grouping

Transfer In

The number of tasks transferred into the precision queue in the interval.

Derived from: Skill_Group_Interval.TransferInCalls

Transfer Out

The number of tasks this agent transferred to another agent or precision queue in the interval. This includes Consultative
                                             Calls. The value is updated in the database when the transfer of the call is completed.

Derived from: Skill_Group_Interval.TransferredOutCalls + Skill_Group_Interval.NetTransferredOutCalls

External Out

For default precision queues: the number of times an agent initiated an outgoing external call in the interval. For routing
                                             precision queues: the number of times an agent initiated a transfer or conference to an external device in the interval.

Derived from: Skill_Group_Interval.AgentOutCalls

Agent State Time

Active
                                             						Time

The
                                             						time in HH:MM:SS (hours, minutes, seconds) that agents in the precision queue
                                             						were in the Active state in the interval.

Derived from: Skill_Group_Interval.TalkTime

Hold
                                             						Time

The
                                             						total time agents spent in the Hold/Paused state in this precision queue,
                                             						measured in HH:MM:SS (hours, minutes, seconds) format. Includes Incoming Direct
                                             						and Outgoing Internal, although call counts are not shown in this report.

Derived from: Skill_Group_Interval.HoldTime

Logged
                                             						On Time

The
                                             						total duration in HH:MM:SS (hours, minutes, and seconds) during the period that
                                             						agents were logged into this skill group.

Derived from: Skill_Group_Interval.LoggedOnTime

%Not
                                             						Active

The
                                             						percentage of time that agents spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. This field applies to all precision queues.

This
                                             						field is a calculated field derived from: Skill_Group_Interval.AvailTime /
                                             						Skill_Group_Interval.LoggedOnTime

%Not
                                             						Ready

The
                                             						percentage of time that agents spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. This field applies to all
                                             						precision queues.

This
                                             						field is a calculated field, derived from: Skill_Group_Interval.NotReadyTime /
                                             						Skill_Group_Interval.LoggedOnTime

%
                                             						Active

The
                                             						percentage of time that agents spent talking on calls in this precision queue
                                             						in relation to LoggedOnTime.

This
                                             						field is a calculated field, derived from: (Skill_Group_Interval.TalkInTime +
                                             						Skill_Group_Interval.TalkOutTime + Skill_Group_Interval.TalkOtherTime +
                                             						Skill_Group_Interval.TalkAutoOutTime + Skill_Group_Interval.TalkPreviewTime +
                                             						Skill_Group_Interval.TalkReserveTime) / Skill_Group_Interval.LoggedOnTime

% Hold

The
                                             						percentage of time that agents put a call on hold or paused a task in relation
                                             						to LoggedOnTime or the interval, whichever is less.

This
                                             						field is a calculated field, derived from: Skill_Group_Interval.HoldTime /
                                             						Skill_Group_Interval.LoggedOnTimeTime

%
                                             						Reserved

The percentage of time that agents spent in the Reserved state waiting for a n ICM routed task from this precision queue in relation to LoggedOnTime.

This
                                             						field is a calculated field, derived from:
                                             						Skill_Group_Interval.ReservedStateTime / Skill_Group_Interval.LoggedOnTime

% Wrap
                                             						Up

The
                                             						percentage of time that agents spent in the Wrap-upstate after incoming or
                                             						outgoing calls to/from this precision queue in relation to LoggedOnTime.

This
                                             						field is a calculated field, derived from: (Skill_Group_Interval.WorkReadyTime
                                             						+ Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime

%
                                             						Utilization

The
                                             						percentage of Ready time that agents in the precision queue spent talking or
                                             						doing call work during the current five-minute interval. This is the percentage
                                             						of time agents spend working on calls versus the time agents were ready.

Derived from: Skill_Group_Real_Time.PercentUtilizationTo5

End of Agent State Times Grouping

Answered

The number of routed calls answered by agents associated with this skillgroup during the given interval. CallsAnswered is
                                             incremented in the interval where the call is answered, as opposed to CallsHandled which is incremented in the interval where
                                             the call ends.

This is derived from skill_group_interval.CallsAnswered.

Abandon ring

For
                                             						voice: the total number of calls that are abandoned while the agent phone is
                                             						ringing.

For
                                             						non-voice: the total number of tasks that are abandoned when offered to an
                                             						agent.

Derived from: Skill_Group_Interval.AbandonRingCalls

Longest Queued

The
                                             						longest a call had to wait before being answered, abandoned, or otherwise
                                             						ended. This includes time in the network queue, local queue, and ringing at the
                                             						agent if applicable.

Derived from: Router_Queue_Interval.MaxCallWaitTime

MaxQueued

The
                                             						maximum number of calls queued for this precision queue during this interval.
                                             						Calls queued against multiple precision queues are included in the count for
                                             						each precision queue to which the calls are queued.

Derived from: Router_Queue_Interval.MaxCallsQueued

### Available Fields
                           	 in the Precision Queue Interval All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current. In
                                 		  addition, most Available fields in this report are derived from the
                                 		  Router_Queue_Interval and Skill_Group_Interval table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in
                           	 the Precision Queue Interval All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

The following current fields are listed in the order (left to right) in which they appear by default in the stock template.

Column
                                             						(Field)

Description

Precision Queue

The
                                             						enterprise name of the Agent Precision Queue.

Derived from: Precision_Queue.EnterpriseName.

Media

The
                                             						enterprise name of the Media Routing Domain associated with the precision
                                             						queue.

Media is derived
                                             						from: Media_Routing_Domain.EnterpriseName.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

DateTime

The
                                             						date and time of the data for a selected row.

Derived
                                             						from: Router_Queue_Interval.DateTime.

Queued

Derived
                                             						from: Router_Queue_Interval.QueueCalls.

Avg
                                             						Speed of Answer

The
                                             						precision queue average speed of answer in HH:MM:SS(hour, minutes, seconds)
                                             						based on the time spent by callers in the queue and ringing at an agent desktop
                                             						before the task is answered divided by the number of answered tasks.

Derived
                                             						from: Skill_Group_Interval.AnswerWaitTime /Skill_Group_Interval.CallsAnswered.

Service Level

Service Level

Service Level Type used to calculate Service level for the
                                             						interval.

Derived from: Router_Queue_Interval.ServiceLevel.

Answer

The
                                             						number of calls that are routed to the precision queue or queued to the
                                             						precision queue in the last interval.

Derived
                                             						from: Router_Queue_Interval.ServiceLevelCalls

Abandon

The
                                             						number of calls that are abandoned within the precision queue service level
                                             						threshold in the last interval.

Derived
                                             						from: Router_Queue_Interval.ServiceLevelCallsAband.

Completed Tasks

Total

The total number of tasks completed by this precision queue in the interval.

Derived from:(Router_Queue_Interval.CallsHandled++ Router_Queue_Interval.RedirectNoAnsCalls+ Router_Queue_Interval.CallsAbandQ+
                                             Router_Queue_Interval.RouterError+ Router_Queue_Interval.CallsAbandToAgent)

Abandoned

The
                                             						sum of:

The number of calls to the call type that are abandoned in the Router queue during the reporting interval.

The number of calls associated with this skillgroup that are abandoned at the agent desktop before being answered during the
                                                   reporting interval. Termination_Call_Detail records generated by agent PG with a Call Disposition Flag of 2 are also counted
                                                   for this field. This does not include short calls and the calls that were abandoned in the VRU.

Derived
                                             						from: Router_Queue_Interval.CallsAbandQ +

Router_Queue_Interval.CallsAbandToAgent.

RONA

The count of calls that are redirected with no answer within the Precision Queue service level threshold in the last interval.

Derived from: Router_Queue_Interval.RedirectNoAnsCalls

Handled

The number of inbound calls for which agents in the precision queue during the interval answered and completed.

Derived from: Router_Queue_Interval.CallsHandled.

Avg
                                             						Handle Time

The
                                             						average time spent by agents in this precision queue handling a task in the
                                             						interval.

This
                                             						field is a calculated field, derived from:
                                             						(Skill_Group_Interval.HandledCallsTime / Skill_Group_Interval.CallsHandled)

Avg
                                             						Active Time

The
                                             						Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						precision queue.

Derived
                                             						from: Skill_Group_Interval.HandledCallsTalkTime
                                             						/Skill_Group_Interval.CallsHandled

Abandon
                                             						Hold

The
                                             						number of tasks offered to the precision queue that are abandoned while being
                                             						held or paused by the agent. The value is incremented at the time the call
                                             						disconnects.

Derived
                                             						from: Skill_Group_Interval.AbandonHoldCalls

Tasks Picked

The total number of pick requests successfully routed by the precision queue.

Tasks Pulled

The total number of pull requests successfully routed by the precision queue.

Picks Failed

Number of pick request resulting in an error.

Pulls Failed

Number of pull request resulting in an error.

End of Completed Tasks Grouping

Transfer In

The number of tasks transferred into the precision queue in the interval.

Derived from: Skill_Group_Interval.TransferInCalls

Transfer Out

The number of tasks this agent transferred to another agent or precision queue in the interval. This includes Consultative
                                             Calls. The value is updated in the database when the transfer of the call is completed.

Derived from: Skill_Group_Interval.TransferredOutCalls + Skill_Group_Interval.NetTransferredOutCalls

External Out

For default precision queues: the number of times an agent initiated an outgoing external call in the interval. For routing
                                             precision queues: the number of times an agent initiated a transfer or conference to an external device in the interval.

Derived from: Skill_Group_Interval.AgentOutCalls

Agent State Time

Active
                                             						Time

The
                                             						time in HH:MM:SS (hours, minutes, seconds) that agents in the precision queue
                                             						were in the Active state in the interval.

Derived from: Skill_Group_Interval.TalkTime

Hold
                                             						Time

The
                                             						total time agents spent in the Hold/Paused state in this precision queue,
                                             						measured in HH:MM:SS (hours, minutes, seconds) format. Includes Incoming Direct
                                             						and Outgoing Internal, although call counts are not shown in this report.

Derived from: Skill_Group_Interval.HoldTime

Logged
                                             						On Time

The
                                             						total duration in HH:MM:SS (hours, minutes, and seconds) during the period that
                                             						agents were logged into this skill group.

Derived from: Skill_Group_Interval.LoggedOnTime

%Not
                                             						Active

The
                                             						percentage of time that agents spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. This field applies to all precision queues.

This
                                             						field is a calculated field derived from: Skill_Group_Interval.AvailTime /
                                             						Skill_Group_Interval.LoggedOnTime

%Not
                                             						Ready

The
                                             						percentage of time that agents spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. This field applies to all
                                             						precision queues.

This
                                             						field is a calculated field, derived from: Skill_Group_Interval.NotReadyTime /
                                             						Skill_Group_Interval.LoggedOnTime

%
                                             						Active

The
                                             						percentage of time that agents spent talking on calls in this precision queue
                                             						in relation to LoggedOnTime.

This
                                             						field is a calculated field, derived from: (Skill_Group_Interval.TalkInTime +
                                             						Skill_Group_Interval.TalkOutTime + Skill_Group_Interval.TalkOtherTime +
                                             						Skill_Group_Interval.TalkAutoOutTime + Skill_Group_Interval.TalkPreviewTime +
                                             						Skill_Group_Interval.TalkReserveTime) / Skill_Group_Interval.LoggedOnTime

% Hold

The
                                             						percentage of time that agents put a call on hold or paused a task in relation
                                             						to LoggedOnTime or the interval, whichever is less.

This
                                             						field is a calculated field, derived from: Skill_Group_Interval.HoldTime /
                                             						Skill_Group_Interval.LoggedOnTimeTime

%
                                             						Reserved

The percentage of time that agents spent in the Reserved state waiting for a n ICM routed task from this precision queue in relation to LoggedOnTime.

This
                                             						field is a calculated field, derived from:
                                             						Skill_Group_Interval.ReservedStateTime / Skill_Group_Interval.LoggedOnTime

% Wrap
                                             						Up

The
                                             						percentage of time that agents spent in the Wrap-upstate after incoming or
                                             						outgoing calls to/from this precision queue in relation to LoggedOnTime.

This
                                             						field is a calculated field, derived from: (Skill_Group_Interval.WorkReadyTime
                                             						+ Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime

%
                                             						Utilization

The
                                             						percentage of Ready time that agents in the precision queue spent talking or
                                             						doing call work during the current five-minute interval. This is the percentage
                                             						of time agents spend working on calls versus the time agents were ready.

Derived from: Skill_Group_Real_Time.PercentUtilizationTo5

End of Agent State Times Grouping

Answered

The number of routed calls answered by agents associated with this skillgroup during the given interval. CallsAnswered is
                                             incremented in the interval where the call is answered, as opposed to CallsHandled which is incremented in the interval where
                                             the call ends.

This is derived from skill_group_interval.CallsAnswered.

Abandon ring

For
                                             						voice: the total number of calls that are abandoned while the agent phone is
                                             						ringing.

For
                                             						non-voice: the total number of tasks that are abandoned when offered to an
                                             						agent.

Derived from: Skill_Group_Interval.AbandonRingCalls

Longest Queued

The
                                             						longest a call had to wait before being answered, abandoned, or otherwise
                                             						ended. This includes time in the network queue, local queue, and ringing at the
                                             						agent if applicable.

Derived from: Router_Queue_Interval.MaxCallWaitTime

MaxQueued

The
                                             						maximum number of calls queued for this precision queue during this interval.
                                             						Calls queued against multiple precision queues are included in the count for
                                             						each precision queue to which the calls are queued.

Derived from: Router_Queue_Interval.MaxCallsQueued

## Skill Group
                        	 Abandon-Answer Distribution Historical

The Skill Group Abandon-Answer
                              				Distribution Historical report identifies where in the skill group callers are
                              				abandoning and the typical wait times for callers.

Query: This report
                              				data is built from a Database Query.

Views: This report has one grid view, Skill Group Abandon-Answer Distribution Historical.

Grouping: This report is
                              				grouped and sorted by Skill Group.

Value Lists: Skill
                              				Groups, Media Routing Domain

Database Schema Tables from
                                 					which data is retrieved:

Bucket_Intervals

Media_Routing_Domain

Skill_Group

Skill_Group_Interval

### Available Fields
                           	 in the Skill Group Abandoned-Answer Distribution Historical Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are populated from the following
                                 		  tables.

These Available
                                 		  fields are from the Skill_Group_Interval table:

Ans Wait Time Derived
                                       				from: Skill_Group_Interval.AnswerWaitTime.

BucketIntervalID Derived from: Skill_Group_Interval.BucketIntervalID.

Calls Handled Derived from: Skill_Group_Interval.CallsHandled.

SkillTargetID Derived from: Skill_Group_Interval.SkillTargetID.

DelayQAban Derived from: Skill_Group_Interval.CallDelayAbandTime.

Router Calls Aban :
                                       				Derived from: Skill_Group_Interval.TotalCallsAband.

These fields are
                                 		  derived from the Bucket_Intervals table, as documented in the Database
                                    			 Schema Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html :

int1 - int 9 : Derived
                                 		  from: Bucket_Intervals.IntervalUpperBound1 - IntervalUpperBound9.

### Current Fields in
                           	 the Skill Group Abandoned-Answer Distribution Historical Grid View

Current fields are those fields that appear by default in a report grid view generated from the stock template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

The headings for
                                 		  the Interval fields are dynamic headers; they show the intervals you defined.

Column
                                             						(Field)

Description

Skill Group

The
                                             						enterprise name of the Skill Group.

Derived
                                             						from:Skill_Group.EnterpriseName.

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

DateTime

The date
                                             						and time when the call type interval data was generated in MM/DD/YYYY (month,
                                             						day, year) and HH:MM:SS (hours, minutes, seconds) format.

For
                                             						every interval in the selected time period, there is summary row for each
                                             						selected call type.

Derived
                                             						from:Skill_Group_Interval.DateTime.

Avg Speed of Answer

Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This is an important measure of service quality because the time can vary, even
                                             over the course of one day, due to call volumes and staff levels.

This is
                                             						a calculated field, derived from:Skill_Group_Interval.AnswerWaitTime/
                                             						Skill_Group_Interval.CallsAnswered.

Int 1
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between the time set to begin measuring and
                                             						interval 1. The system default interval 1 is 8 seconds. For example: 00:00 -
                                             						00:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(1) and
                                             						Skill_Group_Interval.AbandInterval(1).

Int 2
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 1 and interval 2. The
                                             						system default interval 2 is 30 seconds. For example: 00:08 - 00:38.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(2) and
                                             						Skill_Group_Interval.AbandInterval(2).

Int 3
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 2 and interval 3. The
                                             						system default interval 3 is 60 seconds (1 minute). For example: 00:38 - 01:38.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(3) and
                                             						Skill_Group_Interval.AbandInterval(3).

Int 4
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 3 and interval 4. The
                                             						system default interval 4 is 90 seconds. For example: 01:38 - 03:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(4) and
                                             						Skill_Group_Interval.AbandInterval(4).

Int 5
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 4 and interval 5. The
                                             						system default interval 5 is 120 seconds (2 minutes). For example: 03:08 -
                                             						05:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(5) and
                                             						Skill_Group_Interval.AbandInterval(5).

Int 6
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 5 and interval 6. The
                                             						system default interval 6 is 180 seconds (3 minutes). For example: 05:08 -
                                             						08:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(6) and
                                             						Skill_Group_Interval.AbandInterval(6).

Int 7
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 6 and interval 7. The
                                             						system default interval 7 is 300 seconds (5 minutes). For example: 08:08 -
                                             						13:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(7) and
                                             						Skill_Group_Interval.AbandInterval(7).

Int 8
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 7 and interval 8. The
                                             						system default interval 8 is 600 seconds (10 minutes). For example: 13:08 -
                                             						23:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(8) and
                                             						Skill_Group_Interval.AbandInterval(8).

Int 9
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 8 and interval 9. The
                                             						system default interval 9 is 1200 seconds (20 minutes). For example: 23:08 -
                                             						43:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(9) and
                                             						Skill_Group_Interval.AbandInterval(9).

> Int
                                             						9 Ans and Aban

The
                                             						number of calls answered/abandoned within the remaining time in the report time
                                             						period measured in minutes and seconds. For example: > 43:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(10) and
                                             						Skill_Group_Interval.AbandInterval(10).

Max Queued

The
                                             						maximum number of calls in queue for this call type during this interval.

Derived from : Skill_Group_Interval. MaxCallsQueued.

Longest Queued

The
                                             						longest time a call had to wait before it was dispositioned (abandoned or
                                             						answered) in this interval.

Derived from:Skill_Group_Interval. MaxCallWaitTime.

Report Summary: The summary line shows an average for the Avg
                                 				Speed of Answer and Avg Aban Delay columns, totals for the interval columns, and Max
                                 				for MaxQueued and Longest Queued columns.

### Available Fields
                           	 in the Skill Group Abandoned-Answer Distribution Historical Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are populated from the following
                                 		  tables.

These Available
                                 		  fields are from the Skill_Group_Interval table:

Ans Wait Time Derived
                                       				from: Skill_Group_Interval.AnswerWaitTime.

BucketIntervalID Derived from: Skill_Group_Interval.BucketIntervalID.

Calls Handled Derived from: Skill_Group_Interval.CallsHandled.

SkillTargetID Derived from: Skill_Group_Interval.SkillTargetID.

DelayQAban Derived from: Skill_Group_Interval.CallDelayAbandTime.

Router Calls Aban :
                                       				Derived from: Skill_Group_Interval.TotalCallsAband.

These fields are
                                 		  derived from the Bucket_Intervals table, as documented in the Database
                                    			 Schema Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html :

int1 - int 9 : Derived
                                 		  from: Bucket_Intervals.IntervalUpperBound1 - IntervalUpperBound9.

### Current Fields in
                           	 the Skill Group Abandoned-Answer Distribution Historical Grid View

Current fields are those fields that appear by default in a report grid view generated from the stock template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

The headings for
                                 		  the Interval fields are dynamic headers; they show the intervals you defined.

Column
                                             						(Field)

Description

Skill Group

The
                                             						enterprise name of the Skill Group.

Derived
                                             						from:Skill_Group.EnterpriseName.

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

DateTime

The date
                                             						and time when the call type interval data was generated in MM/DD/YYYY (month,
                                             						day, year) and HH:MM:SS (hours, minutes, seconds) format.

For
                                             						every interval in the selected time period, there is summary row for each
                                             						selected call type.

Derived
                                             						from:Skill_Group_Interval.DateTime.

Avg Speed of Answer

Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This is an important measure of service quality because the time can vary, even
                                             over the course of one day, due to call volumes and staff levels.

This is
                                             						a calculated field, derived from:Skill_Group_Interval.AnswerWaitTime/
                                             						Skill_Group_Interval.CallsAnswered.

Int 1
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between the time set to begin measuring and
                                             						interval 1. The system default interval 1 is 8 seconds. For example: 00:00 -
                                             						00:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(1) and
                                             						Skill_Group_Interval.AbandInterval(1).

Int 2
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 1 and interval 2. The
                                             						system default interval 2 is 30 seconds. For example: 00:08 - 00:38.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(2) and
                                             						Skill_Group_Interval.AbandInterval(2).

Int 3
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 2 and interval 3. The
                                             						system default interval 3 is 60 seconds (1 minute). For example: 00:38 - 01:38.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(3) and
                                             						Skill_Group_Interval.AbandInterval(3).

Int 4
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 3 and interval 4. The
                                             						system default interval 4 is 90 seconds. For example: 01:38 - 03:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(4) and
                                             						Skill_Group_Interval.AbandInterval(4).

Int 5
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 4 and interval 5. The
                                             						system default interval 5 is 120 seconds (2 minutes). For example: 03:08 -
                                             						05:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(5) and
                                             						Skill_Group_Interval.AbandInterval(5).

Int 6
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 5 and interval 6. The
                                             						system default interval 6 is 180 seconds (3 minutes). For example: 05:08 -
                                             						08:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(6) and
                                             						Skill_Group_Interval.AbandInterval(6).

Int 7
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 6 and interval 7. The
                                             						system default interval 7 is 300 seconds (5 minutes). For example: 08:08 -
                                             						13:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(7) and
                                             						Skill_Group_Interval.AbandInterval(7).

Int 8
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 7 and interval 8. The
                                             						system default interval 8 is 600 seconds (10 minutes). For example: 13:08 -
                                             						23:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(8) and
                                             						Skill_Group_Interval.AbandInterval(8).

Int 9
                                             						Ans and Aban

The
                                             						number of calls answered/abandoned between interval 8 and interval 9. The
                                             						system default interval 9 is 1200 seconds (20 minutes). For example: 23:08 -
                                             						43:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(9) and
                                             						Skill_Group_Interval.AbandInterval(9).

> Int
                                             						9 Ans and Aban

The
                                             						number of calls answered/abandoned within the remaining time in the report time
                                             						period measured in minutes and seconds. For example: > 43:08.

Derived
                                             						from:Skill_Group_Interval.AnsInterval(10) and
                                             						Skill_Group_Interval.AbandInterval(10).

Max Queued

The
                                             						maximum number of calls in queue for this call type during this interval.

Derived from : Skill_Group_Interval. MaxCallsQueued.

Longest Queued

The
                                             						longest time a call had to wait before it was dispositioned (abandoned or
                                             						answered) in this interval.

Derived from:Skill_Group_Interval. MaxCallWaitTime.

Report Summary: The summary line shows an average for the Avg
                                 				Speed of Answer and Avg Aban Delay columns, totals for the interval columns, and Max
                                 				for MaxQueued and Longest Queued columns.

| Note | The report is built on the Termination Call Detail table. The report response time can be more than 10 minutes based on the
                                          Termination Call Detail table's data size. For this reason, it has to be run as a scheduled report on HDS-DDS when the call
                                          volume is less. |
|---|---|

| Note | To improve the query performance, you can create additional indexes on the Termination Call Detail table. Use the following
                                          queries to create the index: CREATE INDEX XIE5Termination_Call_Detail ON t_Termination_Call_Detail
(
CallTypeID
)

CREATE INDEX XIE6Termination_Call_Detail ON t_Termination_Call_Detail
(
AgentTeamID
) Adding the indexes consume additional database space. For this reason, include the space consumed by the new indexes in your
                                          overall database size allocation. Create these indexes only on the HDS-DDS from where you run this report. If you do not plan to run this report any longer, use the following commands to drop the indexes from the Termination Call
                                          Detail table: DROP INDEX XIE5Termination_Call_Detail ON t_Termination_Call_Detail DROP INDEX XIE6Termination_Call_Detail ON t_Termination_Call_Detail |
|---|---|

| Column (Field) | Description |
|---|---|
| Interval | The date and time of the data for a selected row in the MMM-YYYY format. Derived from: Termination_Call_Details.DateTime |
| Team | The enterprise name of the Agent Team. Derived from Termination_Call_Details.AgentTeamID. |
| Agent | The last name and first name of the agent. This field is a calculated field, derived from Person.LastName + ", " + Person.FirstName. |
| Call Type | The enterprise name of the call type used by calls handled in the selected interval (month). Derived from: Termination_Call_Details.CallTypeID |
| Total contacts handled | Total number of contacts handled in the selected interval. This is a calculated field derived from: Total Contacts Handled when Agent Answers Services were Enabled + Total Contacts
                                             Handled when Agent Answers Services were Disabled. |
| Total contacts handled when Agent Answers Services were Disabled | The total number of contacts handled in the selected interval when the Agent Answers services were disabled. Derived from Termination_Call_Details.AgentAnswersEnabled='N' or Termination_Call_Details.AgentAnswersEnabled is NULL |
| Average  Handled Time when Agent Answers Services were Disabled | The average time an agent spent handling calls in the selected interval while the Agent Answers services were disabled. This field is a calculated field, derived from Total Duration (Termination_Call_Details.TalkTime + Termination_Call_Details.HoldTime
                                             + Termination_Call_Details.WorkTime) when Agent Answers Services were Disabled/Total Contacts Handled by Agent Answers Service
                                             were Disabled. |
| Total contacts handled when Agent Answers Services were Enabled | The total number of contacts handled in the selected interval when the Agent Answers services were enabled. Derived from Termination_Call_Details.AgentAnswersEnabled='Y' |
| Average  Handled Time when Agent Answers Services were Enabled | The average time an agent spent handling calls in the selected interval while the Agent Answers services were enabled. This field is a calculated field, derived from Total Duration  (Termination_Call_Details.TalkTime + Termination_Call_Details.HoldTime
                                             + Termination_Call_Details.WorkTime) when Agent Answers Services were Enabled/Total Contacts Handled when Agent Answers Services
                                             were Enabled. |

| Column (Field) | Description |
|---|---|
| Interval | The date and time of the data for a selected row in the MMM-YYYY format. Derived from: Termination_Call_Details.DateTime |
| Team | The enterprise name of the Agent Team. Derived from Termination_Call_Details.AgentTeamID. |
| Agent | The last name and first name of the agent. This field is a calculated field, derived from Person.LastName + ", " + Person.FirstName. |
| Call Type | The enterprise name of the call type used by calls handled in the selected interval (month). Derived from: Termination_Call_Details.CallTypeID |
| Total contacts handled | Total number of contacts handled in the selected interval. This is a calculated field derived from: Total Contacts Handled when Agent Answers Services were Enabled + Total Contacts
                                             Handled when Agent Answers Services were Disabled. |
| Total contacts handled when Agent Answers Services were Disabled | The total number of contacts handled in the selected interval when the Agent Answers services were disabled. Derived from Termination_Call_Details.AgentAnswersEnabled='N' or Termination_Call_Details.AgentAnswersEnabled is NULL |
| Average  Handled Time when Agent Answers Services were Disabled | The average time an agent spent handling calls in the selected interval while the Agent Answers services were disabled. This field is a calculated field, derived from Total Duration (Termination_Call_Details.TalkTime + Termination_Call_Details.HoldTime
                                             + Termination_Call_Details.WorkTime) when Agent Answers Services were Disabled/Total Contacts Handled by Agent Answers Service
                                             were Disabled. |
| Total contacts handled when Agent Answers Services were Enabled | The total number of contacts handled in the selected interval when the Agent Answers services were enabled. Derived from Termination_Call_Details.AgentAnswersEnabled='Y' |
| Average  Handled Time when Agent Answers Services were Enabled | The average time an agent spent handling calls in the selected interval while the Agent Answers services were enabled. This field is a calculated field, derived from Total Duration  (Termination_Call_Details.TalkTime + Termination_Call_Details.HoldTime
                                             + Termination_Call_Details.WorkTime) when Agent Answers Services were Enabled/Total Contacts Handled when Agent Answers Services
                                             were Enabled. |

| Column (Field) | Description |
|---|---|
| Agent | The last name and first name of the agent. This field is a calculated field, derived from Person.LastName + ", " + Person.FirstName. |
| Precision Queue/Skill Group | The agent skill group's enterprise name. Derived from Skill_Group.EnterpriseName. |
| Attributes | The names of the attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format. Derived from Agent_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents during the interval. Derived from Agent_Skill_Group_Interval.CallsHandled. |
| Average Handle Time | The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds). This field is a calculated field, derived from Agent_Skill_Group_Interval.HandledCallsTime/Agent_Skill_Group_Interval.CallsHandled. |
| Held | The number of incoming calls to this agent that were placed on hold in the interval. Derived from Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Average Hold Time | The average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold in the interval, for all incoming calls
                                             that included hold time. This field is a calculated field, derived from Agent_Skill_Group_Interval.IncomingCallsOnHoldTime/Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Abandon Ring | For voice: the total number of calls that were abandoned while the agent's phone was ringing. For non-voice: the total number of tasks that were abandoned while being offered to an agent. Derived from Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number of tasks that left the agent's phone or terminal that were redirected to another dialed number because of no answer
                                             in the interval. Derived from Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval. Derived from Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number of incoming calls that were transferred to this agent from other agents within the same peripheral that did not
                                             go to IVR for queuing in the interval. This value is updated when the agent completes the call. For blind transfers in the Unified CCE with a Unified CCE System PG, this field updates when the call that was blind transferred to an IVR is subsequently transferred to another agent
                                             and the agent answers the call. For this call scenario, this field is not updated in the Unified CCE without a Unified CCE System PG. Derived from Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number of calls this agent transferred to another agent, precision queue, or skill group in the interval. This includes
                                             Consultative Calls if this transfer was consultative-not blind. The value is updated at the time the agent completes the transfer
                                             of the call. This field is a calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls + Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number of outgoing external calls that this agent made in the interval. Derived from Agent_Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIMES |
| Logged On Time | The total time during the interval the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format. Derived from Agent_Interval.LoggedOnTime. |
| %Active | The percentage of time that the agent spent talking on calls in relation to the agent's LoggedOnTime. This field is a calculated field, derived from:(Agent_Skill_Group_Interval.TalkInTime + Agent_Skill_Group_Interval.TalkOutTime
                                             + Agent_Skill_Group_Interval.TalkOtherTime + Agent_Skill_Group_Interval.TalkAutoOutTime + Agent_Skill_Group_Interval.TalkPreviewTime
                                             + Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime. |
| %Hold | The percentage of time that the agent put a call on hold or paused a task in relation to LoggedOnTime or the interval, whichever
                                             is less. This field is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime/Agent_Interval.LoggedOnTimeTime. |
| %Not Active | The percentage of time that the agent spent in the Not Active or Available state in relation to LoggedOnTime. Applies to all
                                             skill groups and precision queues. This field is a calculated field derived from Agent_Interval.AvailTime/Agent_Interval.LoggedOnTime. |
| %Not Ready | The percentage of time that the agent spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever
                                             is less. Applies to all skill groups and precision queues. This field is a calculated field, derived from Agent_Interval.NotReadyTime / Agent_Interval.LoggedOnTime. |
| %Reserved | The percentage of time that the agent spent in Reserved state waiting for task from this skill group or precision queue in
                                             relation to LoggedOnTime. This field is a calculated field, derived from Agent_Skill_Group_Interval.ReservedStateTime /Agent_Interval.LoggedOnTime. |
| %Wrap Up | The percentage of time that the agent spent in Wrap-up state after an incoming or outgoing call to or from this skill group
                                             or precision queue in relation to LoggedOnTime. The agent state time percentages in the Report Summary row add up to 100 percent only after you select all the skill groups
                                             or precision queues for an agent. When viewing a subset of an agent's skill groups or precision queues, the percentages may
                                             not balance. This field is a calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime + Agent_Skill_Group_Interval.WorkNotReadyTime)/Agent_Interval.LoggedOnTime. |
| %Busy Other | The percentage of time that the agent spent in the Busy Other state by handling calls assigned to other skill group or precision
                                             queue in relation to LoggedOnTime. This field is a calculated field, derived from Agent_Skill_Group_Interval.BusyOtherTime/Agent_Interval.LoggedOnTime. |

| Column (Field) | Description |
|---|---|
| Agent | The last name and first name of the agent. This field is a calculated field, derived from Person.LastName + ", " + Person.FirstName. |
| Precision Queue/Skill Group | The agent skill group's enterprise name. Derived from Skill_Group.EnterpriseName. |
| Attributes | The names of the attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format. Derived from Agent_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents during the interval. Derived from Agent_Skill_Group_Interval.CallsHandled. |
| Average Handle Time | The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds). This field is a calculated field, derived from Agent_Skill_Group_Interval.HandledCallsTime/Agent_Skill_Group_Interval.CallsHandled. |
| Held | The number of incoming calls to this agent that were placed on hold in the interval. Derived from Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Average Hold Time | The average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold in the interval, for all incoming calls
                                             that included hold time. This field is a calculated field, derived from Agent_Skill_Group_Interval.IncomingCallsOnHoldTime/Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Abandon Ring | For voice: the total number of calls that were abandoned while the agent's phone was ringing. For non-voice: the total number of tasks that were abandoned while being offered to an agent. Derived from Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number of tasks that left the agent's phone or terminal that were redirected to another dialed number because of no answer
                                             in the interval. Derived from Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval. Derived from Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number of incoming calls that were transferred to this agent from other agents within the same peripheral that did not
                                             go to IVR for queuing in the interval. This value is updated when the agent completes the call. For blind transfers in the Unified CCE with a Unified CCE System PG, this field updates when the call that was blind transferred to an IVR is subsequently transferred to another agent
                                             and the agent answers the call. For this call scenario, this field is not updated in the Unified CCE without a Unified CCE System PG. Derived from Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number of calls this agent transferred to another agent, precision queue, or skill group in the interval. This includes
                                             Consultative Calls if this transfer was consultative-not blind. The value is updated at the time the agent completes the transfer
                                             of the call. This field is a calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls + Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number of outgoing external calls that this agent made in the interval. Derived from Agent_Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIMES |
| Logged On Time | The total time during the interval the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format. Derived from Agent_Interval.LoggedOnTime. |
| %Active | The percentage of time that the agent spent talking on calls in relation to the agent's LoggedOnTime. This field is a calculated field, derived from:(Agent_Skill_Group_Interval.TalkInTime + Agent_Skill_Group_Interval.TalkOutTime
                                             + Agent_Skill_Group_Interval.TalkOtherTime + Agent_Skill_Group_Interval.TalkAutoOutTime + Agent_Skill_Group_Interval.TalkPreviewTime
                                             + Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime. |
| %Hold | The percentage of time that the agent put a call on hold or paused a task in relation to LoggedOnTime or the interval, whichever
                                             is less. This field is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime/Agent_Interval.LoggedOnTimeTime. |
| %Not Active | The percentage of time that the agent spent in the Not Active or Available state in relation to LoggedOnTime. Applies to all
                                             skill groups and precision queues. This field is a calculated field derived from Agent_Interval.AvailTime/Agent_Interval.LoggedOnTime. |
| %Not Ready | The percentage of time that the agent spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever
                                             is less. Applies to all skill groups and precision queues. This field is a calculated field, derived from Agent_Interval.NotReadyTime / Agent_Interval.LoggedOnTime. |
| %Reserved | The percentage of time that the agent spent in Reserved state waiting for task from this skill group or precision queue in
                                             relation to LoggedOnTime. This field is a calculated field, derived from Agent_Skill_Group_Interval.ReservedStateTime /Agent_Interval.LoggedOnTime. |
| %Wrap Up | The percentage of time that the agent spent in Wrap-up state after an incoming or outgoing call to or from this skill group
                                             or precision queue in relation to LoggedOnTime. The agent state time percentages in the Report Summary row add up to 100 percent only after you select all the skill groups
                                             or precision queues for an agent. When viewing a subset of an agent's skill groups or precision queues, the percentages may
                                             not balance. This field is a calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime + Agent_Skill_Group_Interval.WorkNotReadyTime)/Agent_Interval.LoggedOnTime. |
| %Busy Other | The percentage of time that the agent spent in the Busy Other state by handling calls assigned to other skill group or precision
                                             queue in relation to LoggedOnTime. This field is a calculated field, derived from Agent_Skill_Group_Interval.BusyOtherTime/Agent_Interval.LoggedOnTime. |

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| DateTime | The date
                                          						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                          						HH:MM:SS (hours, minutes, seconds) format. Derived
                                          						from: Agent_Skill_Group_Interval.DateTime |
| Logged On
                                          						Time | The
                                          						total time that the agents were logged in (staffed) for the specified time
                                          						period in any split/skill, measured in HH:MM:SS (hours, minutes, seconds)
                                          						format. Derived
                                          						from: Agent_Skill_Group_Interval.LoggedOnTime |
| Not
                                          						Ready Time | The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. Value taken directly from the database. Derived
                                          						from: Agent_Interval.NotReadyTime |
| Time in |
| RC0 to RC9 | The time
                                          						that the agent spent in Not Ready state with each of the reason codes 0 - 9. Derived
                                          						from: Agent_Event_Detail |
| RC50002 | Not Ready Time spent in 50002. A CTI component failed, causing the agent to be set to Not Ready. This could be due to closing
                                          the agent desktop application, heartbeat timeout, a CTI server failure, or a CTI server client failure (such as Finesse). |
| RC50003 | Not
                                          						Ready Time spent in 50003; the agent was logged out because the Unified CM
                                          						reported the agent's device as out of service. |
| RC50004 | Not
                                          						Ready Time spent in 50004; the agent was logged out due to agent inactivity as
                                          						configured in agent desk settings. |
| RC50010 | Not
                                          						Ready Time spent in 50010; the agent did not receive multiple consecutive tasks
                                          						routed to him/her. The system makes the agent Not Ready automatically so that
                                          						additional tasks are not routed to the agent. By default, the number of
                                          						consecutive tasks missed before the agent is made Not Ready is two. |
| RC50020 | Not
                                          						Ready Time spent in 50020; for deskilling operations on active agents, the
                                          						agent was logged out of the skill group due to a deskilling operation that
                                          						removed the skill group assignment to that agent. This reason code is used in
                                          						the Agent_Event_Detail record and the Agent_Skill_Group_Logout record to
                                          						identify the skill group the agent was removed from (due to the deskilling
                                          						operation). |
| RC50030 | Not
                                          						Ready Time spent in 50030; the agent was logged out because the agent was
                                          						logged into a dynamic device target that was using the same dialed number (DN)
                                          						as the PG static device target. |
| RC50040 | Not
                                          						Ready Time spent in 50040; the mobile agent was logged out because the task
                                          						failed. |
| RC50041 | Not
                                          						Ready Time spent in 50041; the agent's state was changed to Not Ready because
                                          						the task failed when the agent's phone line rings busy. |
| RC50042 | Not
                                          						Ready Time spent in 50042; the mobile agent was logged out because the phone
                                          						line is connected when using nailed connection mode. |
| RC32767 | Not
                                          						Ready Time spent in 32767; the agent's state was changed to Not Ready because
                                          						the agent did not answer a task and the task was redirected to a different
                                          						agent or skill group. |
| RC20001 | Not
                                          						Ready Time spent in 20001; the agent's state was changed to Not Ready and the
                                          						agent was forcibly logged out. |
| RC20002 | Not Ready Time spent in 20002; the general logout reason code condition from Not Ready. |
| RC20003 | Not
                                          						Ready Time spent in 20003; the agent is not in Not Ready state. A request is
                                          						made to place the agent in Not Ready state and then a logout request is made to
                                          						log the agent out. |

| Note | To report on Agent Not Ready reason codes, configure the Not Ready Reason codes on the agent desktop software and in either
                                          the ICM Configuration manager (for Unified CCE ) or Unified CCE Administration (for Packaged CCE) . |
|---|---|

| Column (Field) | Description |
|---|---|
| Agent | The first and last name of the agent. Derived from: Person.LastName ","
                                             Person.FirstName |
| Log On Date Time | The date and time the agent logged in, measured in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hours,
                                             minutes, seconds) format. This field is a calculated field derived from
                                             Agent_Event_Detail.LoginDateTime. |
| Log On Duration | The amount of time the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field derived from
                                             ( Agent_Event_Detail.LoginDuration). |
| Reason Code | A code and text (if configured) from the peripheral
                                             that indicates the reason for the agent's last state
                                             change. If it is not defined, the reason code displays 0. This field is a calculated field derived from
                                             Reason_Code.ReasonCodeName (if reason code text is
                                             configured) and Agent_Event_Detail.ReasonCode. |
| Duration | The amount of time in HH:MM:SS (hours, minutes,
                                             seconds) that the agent spent in the Not Ready state for
                                             the given reason. Derived from Agent_Event_Detail.Duration. |
| % Log On Duration | The percent of the agent's total login session that
                                             the agent spent in the Not Ready state for the given
                                             reason. Derived from
                                             Agent_Event_Detail.Duration / Agent_Event_Detail.LoginDuration. |
| % Not Ready | The percentage of time an agent spent in each Not
                                             Ready state relative to the other Not Ready states. This field is a calculated field derived from 
                                             (Agent_Event_Detail.Duration / (sum of
                                             Agent_Event_Detail.Duration for all not ready reason
                                             codes)). |

| Column (Field) | Description |
|---|---|
| Agent | The first and last name of the agent. Derived from: Person.LastName ","
                                             Person.FirstName |
| Log On Date Time | The date and time the agent logged in, measured in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hours,
                                             minutes, seconds) format. This field is a calculated field derived from
                                             Agent_Event_Detail.LoginDateTime. |
| Log On Duration | The amount of time the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field derived from
                                             ( Agent_Event_Detail.LoginDuration). |
| Reason Code | A code and text (if configured) from the peripheral
                                             that indicates the reason for the agent's last state
                                             change. If it is not defined, the reason code displays 0. This field is a calculated field derived from
                                             Reason_Code.ReasonCodeName (if reason code text is
                                             configured) and Agent_Event_Detail.ReasonCode. |
| Duration | The amount of time in HH:MM:SS (hours, minutes,
                                             seconds) that the agent spent in the Not Ready state for
                                             the given reason. Derived from Agent_Event_Detail.Duration. |
| % Log On Duration | The percent of the agent's total login session that
                                             the agent spent in the Not Ready state for the given
                                             reason. Derived from
                                             Agent_Event_Detail.Duration / Agent_Event_Detail.LoginDuration. |
| % Not Ready | The percentage of time an agent spent in each Not
                                             Ready state relative to the other Not Ready states. This field is a calculated field derived from 
                                             (Agent_Event_Detail.Duration / (sum of
                                             Agent_Event_Detail.Duration for all not ready reason
                                             codes)). |

| Column
                                          					 (Field) | Description |
|---|---|
| Precision Queue | The
                                          					 enterprise name of the Agent Precision Queue. Derived
                                          					 from Precision_Queue.EnterpriseName |
| Agent | The
                                          					 first and last name of the agent. This field
                                          					 is a calculated field, derived from Person.LastName+","+Person.Firstname. |
| Media | The enterprise name of the Media Routing Domain associated with the agent. Media is derived from:
                                          				Media_Routing_Domain.EnterpriseName. |
| DateTime | The date
                                          					 and time of the data for a selected row. Derived
                                          					 from Agent_Skill_Group_Interval.DateTime. |
| Attributes | The
                                          					 attributes used in the precision queue definition. The report shows only those
                                          					 attributes that are used. |
| COMPLETED TASKS |
| Handled | The
                                          					 number of inbound calls for which agents in the precision queue during the
                                          					 interval answered and completed. Derived
                                          					 from Agent_Skill_Group_Interval. CallsHandled |
| Avg Handle Time | This is a
                                          					 calculated field, derived from: Agent_Skill_Group_Interval.HandledCallsTime /
                                          					 Agent_Skill_Group_Interval.CallsHandled The
                                          					 average time spent by the agent in handling a task in the interval, measured in
                                          					 HH:MM:SS (hours, minutes, seconds). |
| Held | The
                                          					 number of incoming calls to this agent that are placed on hold in the interval. Derived
                                          					 from Agent_Skill_Group_Interval.IncomingCallsOnHold |
| Avg Hold Time | The
                                          					 average time in HH:MM:SS (hours, minutes, seconds) for calls placed on hold in
                                          					 the interval, for all incoming calls which include hold time. This field
                                          					 is a calculated field, derived from (Agent_Skill_Group_Interval.
                                          					 IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.IncomingCallsOnHold) |
| Abandon Ring | For
                                          					 voice: The total number of calls that are abandoned while the agent phone is
                                          					 ringing. For
                                          					 non-voice: The total number of tasks that are abandoned when offered to an
                                          					 agent. Derived
                                          					 from Agent_Skill_Group_Interval.AbandonRingCalls |
| RONA | The
                                          					 number of tasks that left the agent phone or terminal that are redirected to
                                          					 another dialed number because of no answer in the interval. Derived
                                          					 from Agent_Skill_Group_Interval.RedirectNoAnsCalls |
| Abandon Hold | The number of Unified ICM routed calls to the agent that are abandoned while the call is on hold and the number of paused tasks that the agent ended in the
                                          interval. Derived
                                          					 from Agent_Skill_Group_Interval.AbandonHoldCalls |
| Transfer In | The
                                          					 number of incoming calls that are transferred to this agent from other agents
                                          					 within the same peripheral that do not go to VRU for queuing in the interval.
                                          					 This value is updated when the agent completes the call. For blind transfers in Unified CCE with a Unified CCE System PG, this field is updated when the call that is blind transferred to a VRU is later transferred to another agent and
                                          the agent answers the call. For this call scenario this field is not updated in Unified CCE without a Unified CCE System PG. Derived
                                          					 from Agent_Skill_Group_Interval.TransferredInCalls |
| Transfer Out | The
                                          					 number of calls this agent transferred to another agent or precision queue in
                                          					 the interval. This number includes consultative calls if this transfer was
                                          					 consultative-not blind. The value is updated at the time the agent completes
                                          					 the transfer of the call. This field
                                          					 is a calculated field, derived from
                                          					 Agent_Skill_Group_Interval.TransferredOutCalls +
                                          					 Agent_Skill_Group_Interval.NetTransferredOutCalls |
| External Out | The
                                          					 number of outgoing external calls that this agent made in the interval. Derived
                                          					 from Agent_Skill_Group_Interval.AgentOutCalls |
| Agent State Times |
| Logged On Time | The
                                          					 total time during the interval the agent was logged in, measured in HH:MM:SS
                                          					 (hours, minutes, seconds) format. Derived
                                          					 from Agent_Interval.LoggedOnTime |
| % Active | The
                                          					 percentage of time that the agent spent talking on calls in this precision
                                          					 queue in relation to LoggedOnTime. This field
                                          					 is a calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime +
                                          					 Agent_Skill_Group_Interval.TalkOutTime +
                                          					 Agent_Skill_Group_Interval.TalkOtherTime +
                                          					 Agent_Skill_Group_Interval.TalkAutoOutTime +
                                          					 Agent_Skill_Group_Interval.TalkPreviewTime +
                                          					 Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime |
| % Hold | The
                                          					 percentage of time that the agent put a call on hold or paused a task in
                                          					 relation to LoggedOnTime or the interval, whichever is less. This field
                                          					 is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime /
                                          					 Agent_Interval.LoggedOnTimeTime |
| % Not
                                          					 Active | The
                                          					 percentage of time that the agent spent in the NotActive or Available state in
                                          					 relation to LoggedOnTime. This field applies to all precision queues. This field
                                          					 is a calculated field derived from Agent_Interval.AvailTime /
                                          					 Agent_Interval.LoggedOnTime |
| % Not
                                          					 Ready | The
                                          					 percentage of time that the agent spent in the NotReady state in relation to
                                          					 LoggedOnTime or the interval, whichever is less. This field applies to all
                                          					 precision queues. This
                                          					 field is a calculated field, derived from Agent_Interval.NotReadyTime /
                                          					 Agent_Interval.LoggedOnTime |
| %
                                          					 Reserved | The percentage of time that the agent spent in the Reserved state waiting for a n ICM routed task from this precision queue in relation to LoggedOnTime. This
                                          					 field is a calculated field, derived from
                                          					 Agent_Skill_Group_Interval.ReservedStateTime / Agent_Interval.LoggedOnTime |
| % Wrap
                                          					 Up | The
                                          					 percentage of time that the agent spent in the Wrap-up state after an incoming
                                          					 or outgoing call to or from this precision queue in relation to LoggedOnTime. The
                                          					 agent state time percentages in the Report Summary row add up to 100 percent
                                          					 only when you select all the precision queues for an agent. When you view a
                                          					 subset of precision queues for an agent, the percentages may not balance. This
                                          					 field is a calculated field, derived from
                                          					 (Agent_Skill_Group_Interval.WorkReadyTime +
                                          					 Agent_Skill_Group_Interval.WorkNotReadyTime) / Agent_Interval.LoggedOnTime |

| Column
                                          					 (Field) | Description |
|---|---|
| Precision Queue | The
                                          					 enterprise name of the Agent Precision Queue. Derived
                                          					 from Precision_Queue.EnterpriseName |
| Agent | The
                                          					 first and last name of the agent. This field
                                          					 is a calculated field, derived from Person.LastName+","+Person.Firstname. |
| Media | The enterprise name of the Media Routing Domain associated with the agent. Media is derived from:
                                          				Media_Routing_Domain.EnterpriseName. |
| DateTime | The date
                                          					 and time of the data for a selected row. Derived
                                          					 from Agent_Skill_Group_Interval.DateTime. |
| Attributes | The
                                          					 attributes used in the precision queue definition. The report shows only those
                                          					 attributes that are used. |
| COMPLETED TASKS |
| Handled | The
                                          					 number of inbound calls for which agents in the precision queue during the
                                          					 interval answered and completed. Derived
                                          					 from Agent_Skill_Group_Interval. CallsHandled |
| Avg Handle Time | This is a
                                          					 calculated field, derived from: Agent_Skill_Group_Interval.HandledCallsTime /
                                          					 Agent_Skill_Group_Interval.CallsHandled The
                                          					 average time spent by the agent in handling a task in the interval, measured in
                                          					 HH:MM:SS (hours, minutes, seconds). |
| Held | The
                                          					 number of incoming calls to this agent that are placed on hold in the interval. Derived
                                          					 from Agent_Skill_Group_Interval.IncomingCallsOnHold |
| Avg Hold Time | The
                                          					 average time in HH:MM:SS (hours, minutes, seconds) for calls placed on hold in
                                          					 the interval, for all incoming calls which include hold time. This field
                                          					 is a calculated field, derived from (Agent_Skill_Group_Interval.
                                          					 IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.IncomingCallsOnHold) |
| Abandon Ring | For
                                          					 voice: The total number of calls that are abandoned while the agent phone is
                                          					 ringing. For
                                          					 non-voice: The total number of tasks that are abandoned when offered to an
                                          					 agent. Derived
                                          					 from Agent_Skill_Group_Interval.AbandonRingCalls |
| RONA | The
                                          					 number of tasks that left the agent phone or terminal that are redirected to
                                          					 another dialed number because of no answer in the interval. Derived
                                          					 from Agent_Skill_Group_Interval.RedirectNoAnsCalls |
| Abandon Hold | The number of Unified ICM routed calls to the agent that are abandoned while the call is on hold and the number of paused tasks that the agent ended in the
                                          interval. Derived
                                          					 from Agent_Skill_Group_Interval.AbandonHoldCalls |
| Transfer In | The
                                          					 number of incoming calls that are transferred to this agent from other agents
                                          					 within the same peripheral that do not go to VRU for queuing in the interval.
                                          					 This value is updated when the agent completes the call. For blind transfers in Unified CCE with a Unified CCE System PG, this field is updated when the call that is blind transferred to a VRU is later transferred to another agent and
                                          the agent answers the call. For this call scenario this field is not updated in Unified CCE without a Unified CCE System PG. Derived
                                          					 from Agent_Skill_Group_Interval.TransferredInCalls |
| Transfer Out | The
                                          					 number of calls this agent transferred to another agent or precision queue in
                                          					 the interval. This number includes consultative calls if this transfer was
                                          					 consultative-not blind. The value is updated at the time the agent completes
                                          					 the transfer of the call. This field
                                          					 is a calculated field, derived from
                                          					 Agent_Skill_Group_Interval.TransferredOutCalls +
                                          					 Agent_Skill_Group_Interval.NetTransferredOutCalls |
| External Out | The
                                          					 number of outgoing external calls that this agent made in the interval. Derived
                                          					 from Agent_Skill_Group_Interval.AgentOutCalls |
| Agent State Times |
| Logged On Time | The
                                          					 total time during the interval the agent was logged in, measured in HH:MM:SS
                                          					 (hours, minutes, seconds) format. Derived
                                          					 from Agent_Interval.LoggedOnTime |
| % Active | The
                                          					 percentage of time that the agent spent talking on calls in this precision
                                          					 queue in relation to LoggedOnTime. This field
                                          					 is a calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime +
                                          					 Agent_Skill_Group_Interval.TalkOutTime +
                                          					 Agent_Skill_Group_Interval.TalkOtherTime +
                                          					 Agent_Skill_Group_Interval.TalkAutoOutTime +
                                          					 Agent_Skill_Group_Interval.TalkPreviewTime +
                                          					 Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime |
| % Hold | The
                                          					 percentage of time that the agent put a call on hold or paused a task in
                                          					 relation to LoggedOnTime or the interval, whichever is less. This field
                                          					 is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime /
                                          					 Agent_Interval.LoggedOnTimeTime |
| % Not
                                          					 Active | The
                                          					 percentage of time that the agent spent in the NotActive or Available state in
                                          					 relation to LoggedOnTime. This field applies to all precision queues. This field
                                          					 is a calculated field derived from Agent_Interval.AvailTime /
                                          					 Agent_Interval.LoggedOnTime |
| % Not
                                          					 Ready | The
                                          					 percentage of time that the agent spent in the NotReady state in relation to
                                          					 LoggedOnTime or the interval, whichever is less. This field applies to all
                                          					 precision queues. This
                                          					 field is a calculated field, derived from Agent_Interval.NotReadyTime /
                                          					 Agent_Interval.LoggedOnTime |
| %
                                          					 Reserved | The percentage of time that the agent spent in the Reserved state waiting for a n ICM routed task from this precision queue in relation to LoggedOnTime. This
                                          					 field is a calculated field, derived from
                                          					 Agent_Skill_Group_Interval.ReservedStateTime / Agent_Interval.LoggedOnTime |
| % Wrap
                                          					 Up | The
                                          					 percentage of time that the agent spent in the Wrap-up state after an incoming
                                          					 or outgoing call to or from this precision queue in relation to LoggedOnTime. The
                                          					 agent state time percentages in the Report Summary row add up to 100 percent
                                          					 only when you select all the precision queues for an agent. When you view a
                                          					 subset of precision queues for an agent, the percentages may not balance. This
                                          					 field is a calculated field, derived from
                                          					 (Agent_Skill_Group_Interval.WorkReadyTime +
                                          					 Agent_Skill_Group_Interval.WorkNotReadyTime) / Agent_Interval.LoggedOnTime |

| Column
                                             						(Field) | Description |
|---|---|
| Agent | The first
                                             						and last name of the agent. This field is a
                                             						calculated field, derived from Person.LastName+ "," +Person.FirstName. |
| Precision Queue / Skill Group | The
                                             						enterprise name for the skill group or agent precision queue. You can identify
                                             						a precision queue by the presence of Attributes next to the queue name. Derived
                                             						from Skill_Group.EnterpriseName or Precision_Queue.EnterpriseName |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |
| DateTime | The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format. Derived
                                             						from Agent_Skill_Group_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number
                                             						of inbound calls that were answered and have completed wrap-up by agents in the
                                             						skill group during the interval. Derived
                                             						from  CallsHandled in the Agent_Skill_Group_Interval table. |
| Avg Handle Time | The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds). This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime /
                                             						Agent_Skill_Group_Interval.CallsHandled). |
| Held | The number
                                             						of incoming calls to this agent that were placed on hold in the interval. Derived
                                             						from Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Avg Hold Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold
                                             						in the interval, for all incoming calls which included hold time. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.
                                             						IncomingCallsOnHoldTime / Agent_Skill_Group_Interval. IncomingCallsOnHold). |
| Abandon Rings | For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing. For
                                             						non-voice: the total number of tasks that were abandoned while being offered to
                                             						an agent. Derived
                                             						from: Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer in the interval. Derived
                                             						from Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval. Derived
                                             						from Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing in the interval. This
                                             						value is updated when the agent completes the call. For blind transfers in the Unified CCE with a Unified CCE System PG, this field is updated when the call that was blind transferred to an Interactive Voice Response (IVR) is later
                                             transferred to another agent and the agent answers the call. For this call scenario, this field is not updated in Unified CCE without a Unified CCE System PG. Derived
                                             						from Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number
                                             						of calls this agent transferred to another agent or skill group in the
                                             						interval. This includes Consultative Calls if this transfer was
                                             						consultative-not blind. The value is updated at the time the agent completes
                                             						the transfer of the call. This field is a
                                             						calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls
                                             						+ Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number
                                             						of outgoing external calls that this agent made in the interval. Derived
                                             						from Agent_Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIMES |
| Logged On Time | The total
                                             						time during the interval the agent was logged in, measured in HH:MM:SS (hours,
                                             						minutes, seconds) format. Derived
                                             						from  Agent_Interval.LoggedOnTime. |
| % Active | The
                                             						percentage of time that the agent spent talking on calls in this skill group in
                                             						relation to the agent's LoggedOnTime. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime +
                                             						Agent_Skill_Group_Interval.TalkOutTime +
                                             						Agent_Skill_Group_Interval.TalkOtherTime +
                                             						Agent_Skill_Group_Interval.TalkAutoOutTime +
                                             						Agent_Skill_Group_Interval.TalkPreviewTime +
                                             						Agent_Skill_Group_Interval.TalkReserveTime) /
                                             						 Agent_Interval.LoggedOnTime. |
| % Hold | The
                                             						percentage of time that the agent has put a call on hold or paused a task in
                                             						relation to LoggedOnTime or the interval, whichever is less. This field is a
                                             						calculated field, derived from Agent_Skill_Group_Interval.HoldTime /
                                             						Agent_Interval.LoggedOnTimeTime. |
| % Not
                                             						Active | The
                                             						percentage of time that the agent spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. Applies to all skill groups. This field is a
                                             						calculated field derived from (Agent_Interval.AvailTime
                                             						/Agent_Interval.LoggedOnTime). |
| % Not
                                             						Ready | The
                                             						percentage of time that the agent spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Applies to all skill groups. This field is a
                                             						calculated field, derived from: (Agent_Interval.NotReadyTime /
                                             						Agent_Interval.LoggedOnTime). |
| % Reserved | The
                                             						percentage of time that the agent spent in Reserved state waiting for a task
                                             						from this skill group in relation to LoggedOnTime. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.ReservedStateTime
                                             						/ Agent_Interval.LoggedOnTime). |
| % Wrap Up | The
                                             						percentage of time that the agent spent in Wrap-up state after an incoming or
                                             						outgoing call to or from this skill group in relation to LoggedOnTime. The agent state time percentages in the Report Summary row
                                             						add up  to 100 percent only after you select all the skill groups for an agent. When
                                             						viewing a subset of an agent's skill groups, the percentages may not balance. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime
                                             						+Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             						/ Agent_Interval.LoggedOnTime. |

| Column
                                             						(Field) | Description |
|---|---|
| Agent | The first
                                             						and last name of the agent. This field is a
                                             						calculated field, derived from Person.LastName+ "," +Person.FirstName. |
| Precision Queue / Skill Group | The
                                             						enterprise name for the skill group or agent precision queue. You can identify
                                             						a precision queue by the presence of Attributes next to the queue name. Derived
                                             						from Skill_Group.EnterpriseName or Precision_Queue.EnterpriseName |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |
| DateTime | The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format. Derived
                                             						from Agent_Skill_Group_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number
                                             						of inbound calls that were answered and have completed wrap-up by agents in the
                                             						skill group during the interval. Derived
                                             						from  CallsHandled in the Agent_Skill_Group_Interval table. |
| Avg Handle Time | The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds). This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime /
                                             						Agent_Skill_Group_Interval.CallsHandled). |
| Held | The number
                                             						of incoming calls to this agent that were placed on hold in the interval. Derived
                                             						from Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Avg Hold Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold
                                             						in the interval, for all incoming calls which included hold time. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.
                                             						IncomingCallsOnHoldTime / Agent_Skill_Group_Interval. IncomingCallsOnHold). |
| Abandon Rings | For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing. For
                                             						non-voice: the total number of tasks that were abandoned while being offered to
                                             						an agent. Derived
                                             						from: Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer in the interval. Derived
                                             						from Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval. Derived
                                             						from Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing in the interval. This
                                             						value is updated when the agent completes the call. For blind transfers in the Unified CCE with a Unified CCE System PG, this field is updated when the call that was blind transferred to an Interactive Voice Response (IVR) is later
                                             transferred to another agent and the agent answers the call. For this call scenario, this field is not updated in Unified CCE without a Unified CCE System PG. Derived
                                             						from Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number
                                             						of calls this agent transferred to another agent or skill group in the
                                             						interval. This includes Consultative Calls if this transfer was
                                             						consultative-not blind. The value is updated at the time the agent completes
                                             						the transfer of the call. This field is a
                                             						calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls
                                             						+ Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number
                                             						of outgoing external calls that this agent made in the interval. Derived
                                             						from Agent_Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIMES |
| Logged On Time | The total
                                             						time during the interval the agent was logged in, measured in HH:MM:SS (hours,
                                             						minutes, seconds) format. Derived
                                             						from  Agent_Interval.LoggedOnTime. |
| % Active | The
                                             						percentage of time that the agent spent talking on calls in this skill group in
                                             						relation to the agent's LoggedOnTime. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime +
                                             						Agent_Skill_Group_Interval.TalkOutTime +
                                             						Agent_Skill_Group_Interval.TalkOtherTime +
                                             						Agent_Skill_Group_Interval.TalkAutoOutTime +
                                             						Agent_Skill_Group_Interval.TalkPreviewTime +
                                             						Agent_Skill_Group_Interval.TalkReserveTime) /
                                             						 Agent_Interval.LoggedOnTime. |
| % Hold | The
                                             						percentage of time that the agent has put a call on hold or paused a task in
                                             						relation to LoggedOnTime or the interval, whichever is less. This field is a
                                             						calculated field, derived from Agent_Skill_Group_Interval.HoldTime /
                                             						Agent_Interval.LoggedOnTimeTime. |
| % Not
                                             						Active | The
                                             						percentage of time that the agent spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. Applies to all skill groups. This field is a
                                             						calculated field derived from (Agent_Interval.AvailTime
                                             						/Agent_Interval.LoggedOnTime). |
| % Not
                                             						Ready | The
                                             						percentage of time that the agent spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Applies to all skill groups. This field is a
                                             						calculated field, derived from: (Agent_Interval.NotReadyTime /
                                             						Agent_Interval.LoggedOnTime). |
| % Reserved | The
                                             						percentage of time that the agent spent in Reserved state waiting for a task
                                             						from this skill group in relation to LoggedOnTime. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.ReservedStateTime
                                             						/ Agent_Interval.LoggedOnTime). |
| % Wrap Up | The
                                             						percentage of time that the agent spent in Wrap-up state after an incoming or
                                             						outgoing call to or from this skill group in relation to LoggedOnTime. The agent state time percentages in the Report Summary row
                                             						add up  to 100 percent only after you select all the skill groups for an agent. When
                                             						viewing a subset of an agent's skill groups, the percentages may not balance. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime
                                             						+Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             						/ Agent_Interval.LoggedOnTime. |

| Column (Field) | Description |
|---|---|
| Agent | The first and last name of the agent. This field is a calculated field, derived from Person.LastName+ "," +Person.FirstName. |
| Precision Queue /Skill Group | The enterprise name for the skill group or agent precision queue. You can identify a precision queue by the presence of Attributes
                                             next to the queue name. Derived from Skill_Group.EnterpriseName or Precision_Queue.EnterpriseName. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format. Derived from Agent_Skill_Group_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the skill group during the interval. Derived from CallsHandled in the Agent_Skill_Group_Interval table. |
| Average Handle Time | The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds). This field is a calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime / Agent_Skill_Group_Interval.CallsHandled). |
| Held | The number of incoming calls to this agent that are placed on hold in the interval. Derived from Agent_Skill_Group_Interval.IncomingCallsOnHold |
| Average Hold Time | The average time in HH:MM:SS (hours, minutes, seconds)during which the calls were put on hold in the interval, for all incoming
                                             calls that included hold time. This field is a calculated field, derived from (Agent_Skill_Group_Interval. IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.
                                             IncomingCallsOnHold). |
| Abandon Rings | For voice: the total number of calls that were abandoned while the agent's phone was ringing. For non-voice: the total number of tasks that were abandoned while being offered to an agent. Derived from: Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number of tasks that left the agent's phone or terminal that were redirected to another dialed number because of no answer
                                             in the interval. Derived from Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in the
                                             interval. Derived from Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number of incoming calls that were transferred to this agent from other agents within the same peripheral that did not
                                             go to IVR for queuing in the interval. This value is updated when the agent completes the call. For blind transfers in the Unified CCE with a Unified CCE System PG, this field is updated when the call that was blind transferred to an IVR is later transferred to another agent
                                             and the agent answers the call. For this call scenario, this field is not updated in Unified CCE without a Unified CCE System PG. Derived from Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number of calls this agent transferred to another agent or skill group in the interval. This includes Consultative Calls
                                             if this transfer was consultative-not blind. The value is updated at the time the agent completes the transfer of the call. This field is a calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls + Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number of outgoing external calls that this agent made in the interval. Derived from Agent_Skill_Group_Interval.AgentOutCalls. |
| Agent State Times |
| Logged On Time | The total time during the interval the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format. Derived from Agent_Interval.LoggedOnTime. |
| % Active | The percentage of time that the agent spent talking on calls in this skill group in relation to the agent's LoggedOnTime. This field is a calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime + Agent_Skill_Group_Interval.TalkOutTime
                                             + Agent_Skill_Group_Interval.TalkOtherTime + Agent_Skill_Group_Interval.TalkAutoOutTime + Agent_Skill_Group_Interval.TalkPreviewTime
                                             + Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime |
| % Hold | The percentage of time that the agent has put a call on hold or paused a task in relation to LoggedOnTime or the interval,
                                             whichever is less. This field is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime / Agent_Interval.LoggedOnTimeTime. |
| % Not Active | The percentage of time that the agent spent in the Not Active or Available state in relation to LoggedOnTime. Applies to
                                             all skill groups. This field is a calculated field derived from (Agent_Interval.AvailTime /Agent_Interval.LoggedOnTime). |
| % Not Ready | The percentage of time that the agent spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever
                                             is less. Applies to all skill groups. This field is a calculated field, derived from: (Agent_Interval.NotReadyTime / Agent_Interval.LoggedOnTime). |
| % Reserved | The percentage of time that the agent spent in Reserved state waiting for a task from this skill group in relation to LoggedOnTime. This field is a calculated field, derived from (Agent_Skill_Group_Interval.ReservedStateTime / Agent_Interval.LoggedOnTime). |
| % Wrap Up | The percentage of time that the agent spent in Wrap-up state after an incoming or outgoing call to or from this skill group
                                             in relation to LoggedOnTime. The agent state time percentages in the Report Summary row add up to 100 percent only after you select all the skill groups
                                             for an agent. When viewing a subset of an agent's skill groups, the percentages may not balance. This field is a calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime +Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             / Agent_Interval.LoggedOnTime. |
| %Busy Other | The percentage of time that the agent spent in the Busy Other state by handling calls assigned to other skill group or precision
                                             queue in relation to LoggedOnTime. This field is a calculated field, derived from Agent_Skill_Group_Interval.BusyOtherTime/Agent_Interval.LoggedOnTime. |

| Column (Field) | Description |
|---|---|
| Agent | The first and last name of the agent. This field is a calculated field, derived from Person.LastName+ "," +Person.FirstName. |
| Precision Queue /Skill Group | The enterprise name for the skill group or agent precision queue. You can identify a precision queue by the presence of Attributes
                                             next to the queue name. Derived from Skill_Group.EnterpriseName or Precision_Queue.EnterpriseName. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format. Derived from Agent_Skill_Group_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the skill group during the interval. Derived from CallsHandled in the Agent_Skill_Group_Interval table. |
| Average Handle Time | The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds). This field is a calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime / Agent_Skill_Group_Interval.CallsHandled). |
| Held | The number of incoming calls to this agent that are placed on hold in the interval. Derived from Agent_Skill_Group_Interval.IncomingCallsOnHold |
| Average Hold Time | The average time in HH:MM:SS (hours, minutes, seconds)during which the calls were put on hold in the interval, for all incoming
                                             calls that included hold time. This field is a calculated field, derived from (Agent_Skill_Group_Interval. IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.
                                             IncomingCallsOnHold). |
| Abandon Rings | For voice: the total number of calls that were abandoned while the agent's phone was ringing. For non-voice: the total number of tasks that were abandoned while being offered to an agent. Derived from: Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number of tasks that left the agent's phone or terminal that were redirected to another dialed number because of no answer
                                             in the interval. Derived from Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in the
                                             interval. Derived from Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number of incoming calls that were transferred to this agent from other agents within the same peripheral that did not
                                             go to IVR for queuing in the interval. This value is updated when the agent completes the call. For blind transfers in the Unified CCE with a Unified CCE System PG, this field is updated when the call that was blind transferred to an IVR is later transferred to another agent
                                             and the agent answers the call. For this call scenario, this field is not updated in Unified CCE without a Unified CCE System PG. Derived from Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number of calls this agent transferred to another agent or skill group in the interval. This includes Consultative Calls
                                             if this transfer was consultative-not blind. The value is updated at the time the agent completes the transfer of the call. This field is a calculated field, derived from Agent_Skill_Group_Interval.TransferredOutCalls + Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number of outgoing external calls that this agent made in the interval. Derived from Agent_Skill_Group_Interval.AgentOutCalls. |
| Agent State Times |
| Logged On Time | The total time during the interval the agent was logged in, measured in HH:MM:SS (hours, minutes, seconds) format. Derived from Agent_Interval.LoggedOnTime. |
| % Active | The percentage of time that the agent spent talking on calls in this skill group in relation to the agent's LoggedOnTime. This field is a calculated field, derived from (Agent_Skill_Group_Interval.TalkInTime + Agent_Skill_Group_Interval.TalkOutTime
                                             + Agent_Skill_Group_Interval.TalkOtherTime + Agent_Skill_Group_Interval.TalkAutoOutTime + Agent_Skill_Group_Interval.TalkPreviewTime
                                             + Agent_Skill_Group_Interval.TalkReserveTime) / Agent_Interval.LoggedOnTime |
| % Hold | The percentage of time that the agent has put a call on hold or paused a task in relation to LoggedOnTime or the interval,
                                             whichever is less. This field is a calculated field, derived from Agent_Skill_Group_Interval.HoldTime / Agent_Interval.LoggedOnTimeTime. |
| % Not Active | The percentage of time that the agent spent in the Not Active or Available state in relation to LoggedOnTime. Applies to
                                             all skill groups. This field is a calculated field derived from (Agent_Interval.AvailTime /Agent_Interval.LoggedOnTime). |
| % Not Ready | The percentage of time that the agent spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever
                                             is less. Applies to all skill groups. This field is a calculated field, derived from: (Agent_Interval.NotReadyTime / Agent_Interval.LoggedOnTime). |
| % Reserved | The percentage of time that the agent spent in Reserved state waiting for a task from this skill group in relation to LoggedOnTime. This field is a calculated field, derived from (Agent_Skill_Group_Interval.ReservedStateTime / Agent_Interval.LoggedOnTime). |
| % Wrap Up | The percentage of time that the agent spent in Wrap-up state after an incoming or outgoing call to or from this skill group
                                             in relation to LoggedOnTime. The agent state time percentages in the Report Summary row add up to 100 percent only after you select all the skill groups
                                             for an agent. When viewing a subset of an agent's skill groups, the percentages may not balance. This field is a calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime +Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             / Agent_Interval.LoggedOnTime. |
| %Busy Other | The percentage of time that the agent spent in the Busy Other state by handling calls assigned to other skill group or precision
                                             queue in relation to LoggedOnTime. This field is a calculated field, derived from Agent_Skill_Group_Interval.BusyOtherTime/Agent_Interval.LoggedOnTime. |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The agent
                                             						skill group's enterprise name. Derived
                                             						from Skill_Group.EnterpriseName. |
| Agent | The first
                                             						and last name of the agent. This is a
                                             						calculated field, derived from  Person.LastName + ", " + Person.FirstName. |
| Media | The enterprise name of the Media Routing Domain associated with the agent. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| DateTime | The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format. Derived
                                             						from Agent_Skill_Group_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number
                                             						of inbound calls that were answered and have completed wrap-up by agents in the
                                             						skill group during the interval. Derived
                                             						from  Agent_Skill_Group_Interval. CallsHandled. |
| Avg Handle Time | The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds). This is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime /
                                             						Agent_Skill_Group_Interval.CallsHandled). |
| Held | The number
                                             						of incoming calls to this agent that were placed on hold in the interval. Derived
                                             						from  Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Avg Hold Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold
                                             						in the interval, for all incoming calls that included hold time. This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.
                                             						IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.IncomingCallsOnHold). |
| Abandon Rings | For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing. For
                                             						non-voice: the total number of tasks that were abandoned while being offered to
                                             						an agent. Derived
                                             						from  Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer in the interval. Derived
                                             						from  Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval. Derived
                                             						from Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing in the interval. This
                                             						value is updated when the agent completes the call. For blind transfers in the Unified CCE with a Unified CCE System PG, this field updates when the call that was blind transferred to an IVR is later transferred to another agent and
                                             the agent answers the call. For this call scenario, this field is not updated in the Unified CCE without a Unified CCE System PG. Derived
                                             						from  Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number
                                             						of calls this agent transferred to another agent or skill group in the
                                             						interval. This number includes Consultative Calls if this transfer was
                                             						consultative-not blind. The value is updated at the time the agent completes
                                             						the transfer of the call. This field is a
                                             						calculated field, derived from: Agent_Skill_Group_Interval.TransferredOutCalls
                                             						+ Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number
                                             						of outgoing external calls that this agent made in the interval. Derived
                                             						from  Agent_Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIMES |
| Logged On Time | The total
                                             						time during the interval the agent was logged in, measured in HH:MM:SS (hours,
                                             						minutes, seconds) format. Derived
                                             						from   Agent_Interval.LoggedOnTime. |
| % Active | The
                                             						percentage of time that the agent spent talking on calls in this skill group in
                                             						relation to the agent's LoggedOnTime. This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.TalkInTime +
                                             						Agent_Skill_Group_Interval.TalkOutTime +
                                             						Agent_Skill_Group_Interval.TalkOtherTime +
                                             						Agent_Skill_Group_Interval.TalkAutoOutTime +
                                             						Agent_Skill_Group_Interval.TalkPreviewTime +
                                             						Agent_Skill_Group_Interval.TalkReserveTime) /
                                             						 Agent_Interval.LoggedOnTime. |
| % Hold | The
                                             						percentage of time that the agent put a call on hold or paused a task in
                                             						relation to LoggedOnTime or the interval, whichever is less. This field  is a
                                             						calculated field, derived from  Agent_Skill_Group_Interval.HoldTime /
                                             						Agent_Interval.LoggedOnTimeTime. |
| % Not
                                             						Active | The
                                             						percentage of time that the agent spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. Applies to all skill groups. This field is a
                                             						calculated field derived from  (Agent_Interval.
                                             						AvailTime/Agent_Interval.LoggedOnTime). |
| % Not
                                             						Ready | The
                                             						percentage of time that the agent spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Applies to all skill groups. This field  is a
                                             						calculated field, derived from  (Agent_Interval.NotReadyTime /
                                             						Agent_Interval.LoggedOnTime). |
| % Reserved | The
                                             						percentage of time that the agent spent in Reserved state waiting for task from
                                             						this skill group in relation to LoggedOnTime. This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.ReservedStateTime
                                             						/ Agent_Interval.LoggedOnTime). |
| % Wrap Up | The
                                             						percentage of time that the agent spent in Wrap-up state after an incoming or
                                             						outgoing call to/from this skill group in relation to LoggedOnTime. The
                                             						agent state time percentages in the Report Summary row add up to 100 percent
                                             						only after you select all the skill groups for an agent. When you view a subset of an
                                             						agent's skill groups, you might notice that the percentages may not balance. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime
                                             						+Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             						/ Agent_Interval.LoggedOnTime. |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The agent
                                             						skill group's enterprise name. Derived
                                             						from Skill_Group.EnterpriseName. |
| Agent | The first
                                             						and last name of the agent. This is a
                                             						calculated field, derived from  Person.LastName + ", " + Person.FirstName. |
| Media | The enterprise name of the Media Routing Domain associated with the agent. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| DateTime | The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format. Derived
                                             						from Agent_Skill_Group_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number
                                             						of inbound calls that were answered and have completed wrap-up by agents in the
                                             						skill group during the interval. Derived
                                             						from  Agent_Skill_Group_Interval. CallsHandled. |
| Avg Handle Time | The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds). This is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.HandledCallsTime /
                                             						Agent_Skill_Group_Interval.CallsHandled). |
| Held | The number
                                             						of incoming calls to this agent that were placed on hold in the interval. Derived
                                             						from  Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Avg Hold Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) that calls were put on hold
                                             						in the interval, for all incoming calls that included hold time. This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.
                                             						IncomingCallsOnHoldTime / Agent_Skill_Group_Interval.IncomingCallsOnHold). |
| Abandon Rings | For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing. For
                                             						non-voice: the total number of tasks that were abandoned while being offered to
                                             						an agent. Derived
                                             						from  Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer in the interval. Derived
                                             						from  Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval. Derived
                                             						from Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing in the interval. This
                                             						value is updated when the agent completes the call. For blind transfers in the Unified CCE with a Unified CCE System PG, this field updates when the call that was blind transferred to an IVR is later transferred to another agent and
                                             the agent answers the call. For this call scenario, this field is not updated in the Unified CCE without a Unified CCE System PG. Derived
                                             						from  Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number
                                             						of calls this agent transferred to another agent or skill group in the
                                             						interval. This number includes Consultative Calls if this transfer was
                                             						consultative-not blind. The value is updated at the time the agent completes
                                             						the transfer of the call. This field is a
                                             						calculated field, derived from: Agent_Skill_Group_Interval.TransferredOutCalls
                                             						+ Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number
                                             						of outgoing external calls that this agent made in the interval. Derived
                                             						from  Agent_Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIMES |
| Logged On Time | The total
                                             						time during the interval the agent was logged in, measured in HH:MM:SS (hours,
                                             						minutes, seconds) format. Derived
                                             						from   Agent_Interval.LoggedOnTime. |
| % Active | The
                                             						percentage of time that the agent spent talking on calls in this skill group in
                                             						relation to the agent's LoggedOnTime. This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.TalkInTime +
                                             						Agent_Skill_Group_Interval.TalkOutTime +
                                             						Agent_Skill_Group_Interval.TalkOtherTime +
                                             						Agent_Skill_Group_Interval.TalkAutoOutTime +
                                             						Agent_Skill_Group_Interval.TalkPreviewTime +
                                             						Agent_Skill_Group_Interval.TalkReserveTime) /
                                             						 Agent_Interval.LoggedOnTime. |
| % Hold | The
                                             						percentage of time that the agent put a call on hold or paused a task in
                                             						relation to LoggedOnTime or the interval, whichever is less. This field  is a
                                             						calculated field, derived from  Agent_Skill_Group_Interval.HoldTime /
                                             						Agent_Interval.LoggedOnTimeTime. |
| % Not
                                             						Active | The
                                             						percentage of time that the agent spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. Applies to all skill groups. This field is a
                                             						calculated field derived from  (Agent_Interval.
                                             						AvailTime/Agent_Interval.LoggedOnTime). |
| % Not
                                             						Ready | The
                                             						percentage of time that the agent spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Applies to all skill groups. This field  is a
                                             						calculated field, derived from  (Agent_Interval.NotReadyTime /
                                             						Agent_Interval.LoggedOnTime). |
| % Reserved | The
                                             						percentage of time that the agent spent in Reserved state waiting for task from
                                             						this skill group in relation to LoggedOnTime. This field is a
                                             						calculated field, derived from  (Agent_Skill_Group_Interval.ReservedStateTime
                                             						/ Agent_Interval.LoggedOnTime). |
| % Wrap Up | The
                                             						percentage of time that the agent spent in Wrap-up state after an incoming or
                                             						outgoing call to/from this skill group in relation to LoggedOnTime. The
                                             						agent state time percentages in the Report Summary row add up to 100 percent
                                             						only after you select all the skill groups for an agent. When you view a subset of an
                                             						agent's skill groups, you might notice that the percentages may not balance. This field is a
                                             						calculated field, derived from (Agent_Skill_Group_Interval.WorkReadyTime
                                             						+Agent_Skill_Group_Interval.WorkNotReadyTime)
                                             						/ Agent_Interval.LoggedOnTime. |

| Note | This report displays data related to current agent team members only. |
|---|---|

| Column
                                             						(Field) | Description |
|---|---|
| Agent Team | The
                                             						Enterprise Name of the Agent Team. Derived
                                             						from  Agent_Team.EnterpriseName. |
| Agent | The last
                                             						and first name of the agent. Derived
                                             						from Person.LastName "," Person.FirstName. |
| DateTime | The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format. Derived
                                             						from Agent_Skill_Group_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number of Unified ICM routed tasks this agent handled. Derived
                                             						from  Agent_Skill_Group_Interval.CallsHandled. |
| Held | The number
                                             						of incoming calls to this agent that were placed on hold. Derived
                                             						from  Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Abandon Rings | For voice: The total number of calls that were abandoned while the agent's phone was
                                             						ringing. For non-voice: The total number of tasks that were abandoned while
                                             						being offered to an agent. Derived
                                             						from  Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer. Derived
                                             						from  Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval. Derived
                                             						from  Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing. This value is updated
                                             						when the agent completes the call. Derived
                                             						from  Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number
                                             						of calls this agent transferred to another agent or skill group. This number includes
                                             						Consultative Calls if this transfer was consultative-not blind. This value is
                                             						updated when the agent completes the transfer. This is a
                                             						calculated field derived from  Agent_Skill_Group_Interval.TransferredOutCalls +
                                             						Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number
                                             						of Outgoing external calls that this agent made in the interval. Derived
                                             						from  Agent_Skill_Group_Interval.AgentOutCalls. |
| Talk Time | The total time in HH:MM:SS (hours, minutes, seconds) that agents spent talking on the phone. This field is a calculated field derived from sum(isnull(TalkInTime,0)) +sum(isnull(TalkOutTime,0)) +sum(isnull(TalkOtherTime,0)) +sum(isnull(TalkAutoOutTime,0)) +sum(isnull(TalkPreviewTime,0))
                                             +sum(isnull(TalkReserveTime,0)). |

| Column
                                             						(Field) | Description |
|---|---|
| Agent Team | The
                                             						Enterprise Name of the Agent Team. Derived
                                             						from  Agent_Team.EnterpriseName. |
| Agent | The last
                                             						and first name of the agent. Derived
                                             						from Person.LastName "," Person.FirstName. |
| DateTime | The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format. Derived
                                             						from Agent_Skill_Group_Interval.DateTime. |
| COMPLETED TASKS |
| Handled | The number of Unified ICM routed tasks this agent handled. Derived
                                             						from  Agent_Skill_Group_Interval.CallsHandled. |
| Held | The number
                                             						of incoming calls to this agent that were placed on hold. Derived
                                             						from  Agent_Skill_Group_Interval.IncomingCallsOnHold. |
| Abandon Rings | For voice: The total number of calls that were abandoned while the agent's phone was
                                             						ringing. For non-voice: The total number of tasks that were abandoned while
                                             						being offered to an agent. Derived
                                             						from  Agent_Skill_Group_Interval.AbandonRingCalls. |
| RONA | The number
                                             						of tasks that left the agent's phone or terminal that were redirected to
                                             						another dialed number because of no answer. Derived
                                             						from  Agent_Skill_Group_Interval.RedirectNoAnsCalls. |
| Abandon Hold | The number of Unified ICM routed calls to the agent that were abandoned while the call was on hold and the number of paused tasks that the agent ended in
                                             the interval. Derived
                                             						from  Agent_Skill_Group_Interval.AbandonHoldCalls. |
| Transfer In | The number
                                             						of incoming calls that were transferred to this agent from other agents within
                                             						the same peripheral that did not go to IVR for queuing. This value is updated
                                             						when the agent completes the call. Derived
                                             						from  Agent_Skill_Group_Interval.TransferredInCalls. |
| Transfer Out | The number
                                             						of calls this agent transferred to another agent or skill group. This number includes
                                             						Consultative Calls if this transfer was consultative-not blind. This value is
                                             						updated when the agent completes the transfer. This is a
                                             						calculated field derived from  Agent_Skill_Group_Interval.TransferredOutCalls +
                                             						Agent_Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | The number
                                             						of Outgoing external calls that this agent made in the interval. Derived
                                             						from  Agent_Skill_Group_Interval.AgentOutCalls. |
| Talk Time | The total time in HH:MM:SS (hours, minutes, seconds) that agents spent talking on the phone. This field is a calculated field derived from sum(isnull(TalkInTime,0)) +sum(isnull(TalkOutTime,0)) +sum(isnull(TalkOtherTime,0)) +sum(isnull(TalkAutoOutTime,0)) +sum(isnull(TalkPreviewTime,0))
                                             +sum(isnull(TalkReserveTime,0)). |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type | The
                                             						enterprise name for the call type. Derived
                                             						from Call_Type.EnterpriseName. |
| Date Time | The date
                                             						and time when the call type interval data was generated in MM/DD/YYYY (month,
                                             						day, year) and HH:MM:SS (hours, minutes, seconds) format. For every
                                             						interval in the selected time period, there is summary row for each selected
                                             						call type. Derived
                                             						from: Call_Type_Interval.DateTime. |
| Avg Speed of Answer | Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels. This field is a
                                             						calculated field, derived from: Call_Type_Interval.AnswerWaitTime/
                                             						 Call_Type_Interval.CallsHandled. |
| Avg Abandon Delay | The
                                             						average delay time of all abandoned calls that ended in this call type during
                                             						the current interval. This value includes calls that were abandoned in queue, calls
                                             						that were abandoned while at the IVR (prompting or self service) and calls that
                                             						were abandoned while ringing at the agent's phone or en route to the agent's
                                             						phone. This field is a
                                             						calculated field, derived from: Call_Type_Interval.CallDelayAbandTime /
                                             						Call_Type_Interval.TotalCallsAband. |
| Int 1 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between the time set to begin measuring and
                                             						interval 1. The system default interval 1 is 8 seconds. For example: 00:00 -
                                             						00:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(1) and
                                             						Call_Type_Interval.AbandInterval(1). |
| Int 2 Ans
                                             						and Aban | The number
                                             						of calls answered/abandoned between interval 1 and interval 2. The system
                                             						default interval 2 is 30 seconds. For example: 00:08 - 00:38. Derived
                                             						from: Call_Type_Interval.AnsInterval(2) and
                                             						Call_Type_Interval.AbandInterval(2). |
| Int 3 Ans
                                             						and Aban | The number
                                             						of calls answered/abandoned between interval 2 and interval 3. The system
                                             						default interval 3 is 60 seconds (1 minute). For example: 00:38 - 01:38. Derived
                                             						from: Call_Type_Interval.AnsInterval(3) and
                                             						Call_Type_Interval.AbandInterval(3). |
| Int 4 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 3 and interval 4. The
                                             						system default interval 4 is 90 seconds. For example: 01:38 - 03:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(4) and
                                             						Call_Type_Interval.AbandInterval(4). |
| Int 5 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 4 and interval 5. The
                                             						system default interval 5 is 120 seconds (2 minutes). For example: 03:08 -
                                             						05:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(5) and
                                             						Call_Type_Interval.AbandInterval(5). |
| Int 6 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 5 and interval 6. The
                                             						system default interval 6 is 180 seconds (3 minutes). For example: 05:08 -
                                             						08:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(6) and
                                             						Call_Type_Interval.AbandInterval(6). |
| Int 7 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 6 and interval 7. The
                                             						system default interval 7 is 300 seconds (5 minutes). For example: 08:08 -
                                             						13:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(7) and
                                             						Call_Type_Interval.AbandInterval(7). |
| Int 8 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 7 and interval 8. The
                                             						system default interval 8 is 600 seconds (10 minutes). For example: 13:08 -
                                             						23:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(8) and
                                             						Call_Type_Interval.AbandInterval(8). |
| Int 9 Ans
                                             						and Aban | The number
                                             						of calls answered/abandoned between interval 8 and interval 9. The system
                                             						default interval 9 is 1200 seconds (20 minutes). For example: 23:08 - 43:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(9) and
                                             						Call_Type_Interval.AbandInterval(9). |
| > Int 9
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned within the remaining time in the report time
                                             						period measured in minutes and seconds. For example: > 43:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(10) and
                                             						Call_Type_Interval.AbandInterval(10). |
| MaxQueued | The
                                             						maximum number of calls in queue for this call type during this interval. Derived
                                             						from: Call_Type_Interval. MaxCallsQueued. The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later. |
| Longest Queued | The
                                             						longest time a call had to wait before it was dispositioned (abandoned or
                                             						answered) in this interval. Derived
                                             						from: Call_Type_Interval. MaxCallWaitTime. The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type | The
                                             						enterprise name for the call type. Derived
                                             						from Call_Type.EnterpriseName. |
| Date Time | The date
                                             						and time when the call type interval data was generated in MM/DD/YYYY (month,
                                             						day, year) and HH:MM:SS (hours, minutes, seconds) format. For every
                                             						interval in the selected time period, there is summary row for each selected
                                             						call type. Derived
                                             						from: Call_Type_Interval.DateTime. |
| Avg Speed of Answer | Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels. This field is a
                                             						calculated field, derived from: Call_Type_Interval.AnswerWaitTime/
                                             						 Call_Type_Interval.CallsHandled. |
| Avg Abandon Delay | The
                                             						average delay time of all abandoned calls that ended in this call type during
                                             						the current interval. This value includes calls that were abandoned in queue, calls
                                             						that were abandoned while at the IVR (prompting or self service) and calls that
                                             						were abandoned while ringing at the agent's phone or en route to the agent's
                                             						phone. This field is a
                                             						calculated field, derived from: Call_Type_Interval.CallDelayAbandTime /
                                             						Call_Type_Interval.TotalCallsAband. |
| Int 1 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between the time set to begin measuring and
                                             						interval 1. The system default interval 1 is 8 seconds. For example: 00:00 -
                                             						00:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(1) and
                                             						Call_Type_Interval.AbandInterval(1). |
| Int 2 Ans
                                             						and Aban | The number
                                             						of calls answered/abandoned between interval 1 and interval 2. The system
                                             						default interval 2 is 30 seconds. For example: 00:08 - 00:38. Derived
                                             						from: Call_Type_Interval.AnsInterval(2) and
                                             						Call_Type_Interval.AbandInterval(2). |
| Int 3 Ans
                                             						and Aban | The number
                                             						of calls answered/abandoned between interval 2 and interval 3. The system
                                             						default interval 3 is 60 seconds (1 minute). For example: 00:38 - 01:38. Derived
                                             						from: Call_Type_Interval.AnsInterval(3) and
                                             						Call_Type_Interval.AbandInterval(3). |
| Int 4 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 3 and interval 4. The
                                             						system default interval 4 is 90 seconds. For example: 01:38 - 03:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(4) and
                                             						Call_Type_Interval.AbandInterval(4). |
| Int 5 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 4 and interval 5. The
                                             						system default interval 5 is 120 seconds (2 minutes). For example: 03:08 -
                                             						05:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(5) and
                                             						Call_Type_Interval.AbandInterval(5). |
| Int 6 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 5 and interval 6. The
                                             						system default interval 6 is 180 seconds (3 minutes). For example: 05:08 -
                                             						08:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(6) and
                                             						Call_Type_Interval.AbandInterval(6). |
| Int 7 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 6 and interval 7. The
                                             						system default interval 7 is 300 seconds (5 minutes). For example: 08:08 -
                                             						13:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(7) and
                                             						Call_Type_Interval.AbandInterval(7). |
| Int 8 Ans
                                             						and Aban | The
                                             						number of calls answered/abandoned between interval 7 and interval 8. The
                                             						system default interval 8 is 600 seconds (10 minutes). For example: 13:08 -
                                             						23:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(8) and
                                             						Call_Type_Interval.AbandInterval(8). |
| Int 9 Ans
                                             						and Aban | The number
                                             						of calls answered/abandoned between interval 8 and interval 9. The system
                                             						default interval 9 is 1200 seconds (20 minutes). For example: 23:08 - 43:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(9) and
                                             						Call_Type_Interval.AbandInterval(9). |
| > Int 9
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned within the remaining time in the report time
                                             						period measured in minutes and seconds. For example: > 43:08. Derived
                                             						from: Call_Type_Interval.AnsInterval(10) and
                                             						Call_Type_Interval.AbandInterval(10). |
| MaxQueued | The
                                             						maximum number of calls in queue for this call type during this interval. Derived
                                             						from: Call_Type_Interval. MaxCallsQueued. The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later. |
| Longest Queued | The
                                             						longest time a call had to wait before it was dispositioned (abandoned or
                                             						answered) in this interval. Derived
                                             						from: Call_Type_Interval. MaxCallWaitTime. The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type | The
                                             						enterprise name for the call type. Derived
                                             						from: Call_Type.EnterpriseName. |
| DateTime | The date
                                             						and time when the record was generated in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hours, minutes, seconds) format. Derived
                                             						from: Call_Type_Interval.DateTime. |
| Service
                                             						Level | Service
                                             						Level Type used to calculate Service level for the interval. Derived
                                             						from: Call_Type_Interval.ServiceLevel. |
| Abandon
                                             						Within Service Level | The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes. This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                             and the queue. Derived
                                             						from: Call_Type_Interval.ServiceLevelAband. |
| Avg Speed
                                             						of Answer | Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels. This field
                                             						is a calculated field, derived from: Call_Type_Interval.AnswerWaitTime /
                                             						Call_Type_Interval.CallsAnswered. |
| TASKS |
| Offered | Tasks that
                                             						were offered to this call type during the interval. Derived
                                             						from: Call_Type_Interval.CallsOffered. |
| Assigned
                                             						from Q | The number
                                             						of tasks of the call type assigned from the queue to be routed in the interval. Derived
                                             						from: Call_Type_Interval.RouterQueueCalls. |
| Answered | The total number of calls of this call type answered by agents in the interval. This field is applicable to both Unified ICM and Unified CCE with the following exception: if the call is answered by an agent on a standard ACD, this field is incremented only if the
                                                call was translation routed. Derived
                                             						from: Call_Type_Interval.CallsAnswered. |
| Answer
                                             						Wait Time | Answer Wait Time. The sum of answer wait time in seconds for all calls that were answered for the call type during the reporting
                                             interval. This field is applicable to both Unified ICM and Unified CCE with the following exception: if the call is answered by an agent on a standard ACD, this field is incremented only if the
                                                call was translation routed. Derived
                                             						from: Call_Type_Interval.AnswerWaitTime. |
| COMPLETED TASKS |
| Handled | The total
                                             						number of tasks handled to completion for the call type in the interval. Derived
                                             						from: Call_Type_Interval.CallsHandled. |
| Abandon | The total number of calls abandoned while in VRU (that is, while undergoing prompting or listening to voice menus options),
                                             calls abandoned while queued to skill group, and calls abandoned at agent desktop. This value also includes abandons for calls
                                             that are not in the queue; for example, when the caller ends the call while listening to a VRU prompt. Therefore, the number
                                             of calls abandoned at a VRU before being queued is TotalCallsAband minus RouterCallsAbandToAgent and RouterCallsAbandQ. Does
                                             not include short calls. Derived
                                             						from: Call_Type_Interval.TotalCallsAband. |
| Return | The number of tasks of the call type that ICM software routed to Return nodes in the interval. This field
                                             						is a calculated field, derived from: Call_Type_Interval.ReturnBusy +
                                             						Call_Type_Interval.ReturnRing + Call_Type_Interval.ReturnRelease. |
| Default
                                             						Treatment | The number
                                             						of tasks of the call type that were given default treatment or end nodes in the
                                             						interval. Derived
                                             						from: Call_Type_Interval.ICRDefaultRouted. |
| Network
                                             						Routed | The number of tasks of the call type that were routed not by ICM software but by the carrier in the interval. For prerouted calls, the carrier decides where to route the call. Derived
                                             						from: Call_Type_Interval.NetworkDefaultRouted. |
| Flow Out | The number
                                             						of tasks of the call type that flowed out of the call type to another call type
                                             						in the interval. Derived
                                             						from: Call_Type_Interval.OverflowOut. |
| Calls
                                             						Error | The number
                                             						of calls for this call type that had errors or were incomplete in the interval. This field
                                             						is a calculated field, derived from: Call_Type_Interval.ErrorCount +
                                             						Call_Type_Interval.IncompleteCalls + Call_Type_Interval.AgentErrorCount. |
| Other | The number
                                             						of tasks of the call type that are Short, were routed to non-Agent targets, or
                                             						were redirected in the interval. This field
                                             						is a calculated field, derived from: Call_Type_Interval.CallsRONA +
                                             						Call_Type_Interval.CallsRoutedNonAgent + Call_Type_Interval.ShortCalls. |
| % Queued | The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval. This field
                                             						is a calculated field, derived from: (Call_Type_Interval.CallsQHandled /
                                             						Call_Type_Interval.CallsHandled). |
| % Aban | The
                                             						percentage of all the tasks that came in to the call type in the interval that
                                             						were abandoned. This field
                                             						is a calculated field, derived from: (Call_Type_Interval.TotalCallsAband /
                                             						(Call_Type_Interval.CallsHandled+ Call_Type_Interval.TotalCallsAband +
                                             						Call_Type_Interval.IncompleteCalls + Call_Type_Interval.ReturnBusy +
                                             						Call_Type_Interval.ReturnRing + Call_Type_Interval.ICRDefaultRouted +
                                             						Call_Type_Interval.NetworkDefaultRouted + Call_Type_Interval.OverflowOut +
                                             						Call_Type_Interval.CallsRONA + Call_Type_Interval.ReturnRelease +
                                             						Call_Type_Interval.CallsRoutedNonAgent + Call_Type_Interval.ShortCalls+
                                             						Call_Type_Interval.ErrorCount + Call_Type_Interval.AgentErrorCount). |
| Avg Aban
                                             						Delay | The
                                             						average delay time of all abandoned calls that ended in this call type during
                                             						the current interval. This includes calls that were abandoned in queue, calls
                                             						that were abandoned while at the IVR (prompting or self service) and calls that
                                             						were abandoned while ringing at the agent's phone or en route to the agent's
                                             						phone. This field
                                             						is a calculated field. Derived from: Call_Type_Interval.CallDelayAbandTime /
                                             						Call_Type_Interval.TotalCallsAband. |
| Short
                                             						Calls | The number
                                             						of calls abandoned during the Call_Type Abandon Call Wait Time. Calls abandoned
                                             						after this time period are counted as Abandoned, not Short Calls. Derived
                                             						from: Call_Type_Interval.ShortCalls. |
| Tasks Picked | The total number of pick requests successfully routed by this call type in the reporting interval. |
| Tasks Pulled | The total number of  pull requests successfully routed by this call type in the reporting interval. |
| Picks Failed | Number of pick request resulting in an error. |
| Pulls Failed | Number of pull requests resulting in an error. |
| MaxQueued | The maximum number of calls in queue for this call type during this interval. Derived from: Call_Type_Interval. MaxCallsQueued. |
| Longest Queued | The longest time a call had to wait before it was dispositioned (abandoned or answered) in this interval. Derived from: Call_Type_Interval. MaxCallWaitTime. The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type | The
                                             						enterprise name for the call type. Derived
                                             						from: Call_Type.EnterpriseName. |
| DateTime | The date
                                             						and time when the record was generated in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hours, minutes, seconds) format. Derived
                                             						from: Call_Type_Interval.DateTime. |
| Service
                                             						Level | Service
                                             						Level Type used to calculate Service level for the interval. Derived
                                             						from: Call_Type_Interval.ServiceLevel. |
| Abandon
                                             						Within Service Level | The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes. This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                             and the queue. Derived
                                             						from: Call_Type_Interval.ServiceLevelAband. |
| Avg Speed
                                             						of Answer | Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels. This field
                                             						is a calculated field, derived from: Call_Type_Interval.AnswerWaitTime /
                                             						Call_Type_Interval.CallsAnswered. |
| TASKS |
| Offered | Tasks that
                                             						were offered to this call type during the interval. Derived
                                             						from: Call_Type_Interval.CallsOffered. |
| Assigned
                                             						from Q | The number
                                             						of tasks of the call type assigned from the queue to be routed in the interval. Derived
                                             						from: Call_Type_Interval.RouterQueueCalls. |
| Answered | The total number of calls of this call type answered by agents in the interval. This field is applicable to both Unified ICM and Unified CCE with the following exception: if the call is answered by an agent on a standard ACD, this field is incremented only if the
                                                call was translation routed. Derived
                                             						from: Call_Type_Interval.CallsAnswered. |
| Answer
                                             						Wait Time | Answer Wait Time. The sum of answer wait time in seconds for all calls that were answered for the call type during the reporting
                                             interval. This field is applicable to both Unified ICM and Unified CCE with the following exception: if the call is answered by an agent on a standard ACD, this field is incremented only if the
                                                call was translation routed. Derived
                                             						from: Call_Type_Interval.AnswerWaitTime. |
| COMPLETED TASKS |
| Handled | The total
                                             						number of tasks handled to completion for the call type in the interval. Derived
                                             						from: Call_Type_Interval.CallsHandled. |
| Abandon | The total number of calls abandoned while in VRU (that is, while undergoing prompting or listening to voice menus options),
                                             calls abandoned while queued to skill group, and calls abandoned at agent desktop. This value also includes abandons for calls
                                             that are not in the queue; for example, when the caller ends the call while listening to a VRU prompt. Therefore, the number
                                             of calls abandoned at a VRU before being queued is TotalCallsAband minus RouterCallsAbandToAgent and RouterCallsAbandQ. Does
                                             not include short calls. Derived
                                             						from: Call_Type_Interval.TotalCallsAband. |
| Return | The number of tasks of the call type that ICM software routed to Return nodes in the interval. This field
                                             						is a calculated field, derived from: Call_Type_Interval.ReturnBusy +
                                             						Call_Type_Interval.ReturnRing + Call_Type_Interval.ReturnRelease. |
| Default
                                             						Treatment | The number
                                             						of tasks of the call type that were given default treatment or end nodes in the
                                             						interval. Derived
                                             						from: Call_Type_Interval.ICRDefaultRouted. |
| Network
                                             						Routed | The number of tasks of the call type that were routed not by ICM software but by the carrier in the interval. For prerouted calls, the carrier decides where to route the call. Derived
                                             						from: Call_Type_Interval.NetworkDefaultRouted. |
| Flow Out | The number
                                             						of tasks of the call type that flowed out of the call type to another call type
                                             						in the interval. Derived
                                             						from: Call_Type_Interval.OverflowOut. |
| Calls
                                             						Error | The number
                                             						of calls for this call type that had errors or were incomplete in the interval. This field
                                             						is a calculated field, derived from: Call_Type_Interval.ErrorCount +
                                             						Call_Type_Interval.IncompleteCalls + Call_Type_Interval.AgentErrorCount. |
| Other | The number
                                             						of tasks of the call type that are Short, were routed to non-Agent targets, or
                                             						were redirected in the interval. This field
                                             						is a calculated field, derived from: Call_Type_Interval.CallsRONA +
                                             						Call_Type_Interval.CallsRoutedNonAgent + Call_Type_Interval.ShortCalls. |
| % Queued | The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval. This field
                                             						is a calculated field, derived from: (Call_Type_Interval.CallsQHandled /
                                             						Call_Type_Interval.CallsHandled). |
| % Aban | The
                                             						percentage of all the tasks that came in to the call type in the interval that
                                             						were abandoned. This field
                                             						is a calculated field, derived from: (Call_Type_Interval.TotalCallsAband /
                                             						(Call_Type_Interval.CallsHandled+ Call_Type_Interval.TotalCallsAband +
                                             						Call_Type_Interval.IncompleteCalls + Call_Type_Interval.ReturnBusy +
                                             						Call_Type_Interval.ReturnRing + Call_Type_Interval.ICRDefaultRouted +
                                             						Call_Type_Interval.NetworkDefaultRouted + Call_Type_Interval.OverflowOut +
                                             						Call_Type_Interval.CallsRONA + Call_Type_Interval.ReturnRelease +
                                             						Call_Type_Interval.CallsRoutedNonAgent + Call_Type_Interval.ShortCalls+
                                             						Call_Type_Interval.ErrorCount + Call_Type_Interval.AgentErrorCount). |
| Avg Aban
                                             						Delay | The
                                             						average delay time of all abandoned calls that ended in this call type during
                                             						the current interval. This includes calls that were abandoned in queue, calls
                                             						that were abandoned while at the IVR (prompting or self service) and calls that
                                             						were abandoned while ringing at the agent's phone or en route to the agent's
                                             						phone. This field
                                             						is a calculated field. Derived from: Call_Type_Interval.CallDelayAbandTime /
                                             						Call_Type_Interval.TotalCallsAband. |
| Short
                                             						Calls | The number
                                             						of calls abandoned during the Call_Type Abandon Call Wait Time. Calls abandoned
                                             						after this time period are counted as Abandoned, not Short Calls. Derived
                                             						from: Call_Type_Interval.ShortCalls. |
| Tasks Picked | The total number of pick requests successfully routed by this call type in the reporting interval. |
| Tasks Pulled | The total number of  pull requests successfully routed by this call type in the reporting interval. |
| Picks Failed | Number of pick request resulting in an error. |
| Pulls Failed | Number of pull requests resulting in an error. |
| MaxQueued | The maximum number of calls in queue for this call type during this interval. Derived from: Call_Type_Interval. MaxCallsQueued. |
| Longest Queued | The longest time a call had to wait before it was dispositioned (abandoned or answered) in this interval. Derived from: Call_Type_Interval. MaxCallWaitTime. The system displays data in this field only if your Unified Intelligence Center system is connected to Unified CCE Release 8.0(3) or later. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type | The
                                             						enterprise name for the call type. Derived
                                             						from Call_Type.EnterpriseName. |
| Precision Queue / Skill Group | The
                                             						enterprise name for the skill group or agent precision queue. You can identify
                                             						a precision queue by the presence of Attributes next to the queue name. Derived
                                             						from: Skill_Group.Enterprise or Precision_Queue.EnterpriseName |
| DateTime | The date
                                             						and time for the data of a selected row. Derived
                                             						from: Call_Type_SG_Interval.DateTime. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |
| Handled | The total
                                             						number of tasks handled to completion for the call type in the interval. Derived
                                             						from: Call_Type_SG_Interval.CallsHandled. |
| Avg Handle Time | The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds). This field is a
                                             						calculated field, derived from: Call_Type_SG_Interval.Handle Time /
                                             						Call_Type_SG_Interval.CallsHandled. |
| %Queued | The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval. This field  is a
                                             						calculated field, derived from Call_Type_SG_Interval. CallsQHandled
                                             						/Call_Type_SG_Interval.CallsHandled. |
| Service Level | Service
                                             						Level Type used to calculate Service level for the interval. Derived
                                             						from: Call_Type_SG_Interval.ServiceLevel. |
| Avg Speed of Answer | Average Speed of Answer. The average answer waiting time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels. This field is a
                                             						calculated field, derived from: Call_Type_SG_Interval.AnswerWaitTime /
                                             						Call_Type_SG_Interval.CallsAnswered. |
| Abandon Within Service Level | The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes. This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                             and the queue. Derived
                                             						from: Call_Type_Interval.ServiceLevelAband. |
| Abandon in Queue | The number
                                             						of calls to the call type that were abandoned in the Router queue during the
                                             						interval. Derived
                                             						from: Call_Type_SG_Interval.RouterCalls AbandQ. |
| Longest Queued | The longest a task had to wait before
                                             									being answered, abandoned, or otherwise ended. This value
                                             									includes time in the network queue, local queue, and ringing at
                                             									the agent, if applicable. Derived
                                             						from: Router_Queue_Interval.MaxCallWaitTime |
| MaxQueued | The maximum number of tasks queued for
                                             									this skill group during this interval. Calls queued against
                                             									multiple skill groups are included in the count for each skill
                                             									group to which the calls are queued. Derived
                                             						from: Router_Queue_Interval.MaxCallsQueued |
| Tasks Picked | The total number of pick requests successfully routed to this skill group or precision queue by this call type in the reporting
                                             interval. |
| Tasks Pulled | The total number of pull requests successfully routed to this skill group or precision queue by this call type in the reporting
                                             interval. |
| Picks Failed | Number of pick request resulting in an error. |
| Pulls Failed | Number of pull requests resulting in an error. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type | The
                                             						enterprise name for the call type. Derived
                                             						from Call_Type.EnterpriseName. |
| Precision Queue / Skill Group | The
                                             						enterprise name for the skill group or agent precision queue. You can identify
                                             						a precision queue by the presence of Attributes next to the queue name. Derived
                                             						from: Skill_Group.Enterprise or Precision_Queue.EnterpriseName |
| DateTime | The date
                                             						and time for the data of a selected row. Derived
                                             						from: Call_Type_SG_Interval.DateTime. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |
| Handled | The total
                                             						number of tasks handled to completion for the call type in the interval. Derived
                                             						from: Call_Type_SG_Interval.CallsHandled. |
| Avg Handle Time | The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds). This field is a
                                             						calculated field, derived from: Call_Type_SG_Interval.Handle Time /
                                             						Call_Type_SG_Interval.CallsHandled. |
| %Queued | The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval. This field  is a
                                             						calculated field, derived from Call_Type_SG_Interval. CallsQHandled
                                             						/Call_Type_SG_Interval.CallsHandled. |
| Service Level | Service
                                             						Level Type used to calculate Service level for the interval. Derived
                                             						from: Call_Type_SG_Interval.ServiceLevel. |
| Avg Speed of Answer | Average Speed of Answer. The average answer waiting time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels. This field is a
                                             						calculated field, derived from: Call_Type_SG_Interval.AnswerWaitTime /
                                             						Call_Type_SG_Interval.CallsAnswered. |
| Abandon Within Service Level | The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes. This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                             and the queue. Derived
                                             						from: Call_Type_Interval.ServiceLevelAband. |
| Abandon in Queue | The number
                                             						of calls to the call type that were abandoned in the Router queue during the
                                             						interval. Derived
                                             						from: Call_Type_SG_Interval.RouterCalls AbandQ. |
| Longest Queued | The longest a task had to wait before
                                             									being answered, abandoned, or otherwise ended. This value
                                             									includes time in the network queue, local queue, and ringing at
                                             									the agent, if applicable. Derived
                                             						from: Router_Queue_Interval.MaxCallWaitTime |
| MaxQueued | The maximum number of tasks queued for
                                             									this skill group during this interval. Calls queued against
                                             									multiple skill groups are included in the count for each skill
                                             									group to which the calls are queued. Derived
                                             						from: Router_Queue_Interval.MaxCallsQueued |
| Tasks Picked | The total number of pick requests successfully routed to this skill group or precision queue by this call type in the reporting
                                             interval. |
| Tasks Pulled | The total number of pull requests successfully routed to this skill group or precision queue by this call type in the reporting
                                             interval. |
| Picks Failed | Number of pick request resulting in an error. |
| Pulls Failed | Number of pull requests resulting in an error. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type | The
                                             						enterprise name for the call type. Derived
                                             						from: Call_Type_SG_Interval.EnterpriseName. |
| Skill Group | The
                                             						enterprise name for the skill group. Derived
                                             						from: Skill_Group.Enterprise |
| DateTime | The date and time for the data of a selected row. Derived from: Call_Type.DateTime |
| Handled | The
                                             						total number of tasks handled to completion for the call type in the interval. Derived
                                             						from: Call_Type_SG_Interval.CallsHandled. |
| Avg Handle Time | The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds). This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.Handle
                                             						Time/Call_Type_SG_Interval.CallsHandled. |
| %Queued | The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval. This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.CallsQHandled
                                             						/Call_Type_SG_Interval.CallsHandled. |
| Service Level | Service Level Type used to calculate Service level for the interval. Derived
                                             						from: Call_Type_SG_Interval.ServiceLevel. |
| Avg Speed of Answer | Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels. This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.AnswerWaitTime/Call_Type_SG_Interval.CallsAnswered. |
| Aban
                                             						within SL | The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes. Derived
                                             						from: Call_Type_SG_Interval.ServiceLevelAband. |
| Aban in
                                             						Queue | The
                                             						number of calls to the call type that were abandoned in the Router queue during
                                             						the interval. Derived
                                             						from: Call_Type_SG_Interval.RouterCallsAbandQ. |
| MaxQueued | The
                                             						maximum number of calls queued for this skill group during this interval. Calls
                                             						queued against multiple skill groups are included in the count for each skill
                                             						group to which the calls are queued. Derived
                                             						from: Call_Type_SG_Interval.MaxCallsQueued |
| Longest Queued | The
                                             						longest a call had to wait before being answered, abandoned, or otherwise
                                             						ended. This value includes time in the network queue, local queue, and ringing at the
                                             						agent if applicable. Derived
                                             						from: Call_Type_SG_Interval.MaxCallWaitTime |
| Tasks Picked | The total number of pick requests successfully routed to this skill group by this call type in the reporting interval. |
| Tasks Pulled | The total number of pull requests successfully routed to this skill group by this call type in the reporting interval. |
| Picks Failed | Number of pick request resulting in an error. |
| Pulls Failed | Number of pull requests resulting in an error. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type | The
                                             						enterprise name for the call type. Derived
                                             						from: Call_Type_SG_Interval.EnterpriseName. |
| Skill Group | The
                                             						enterprise name for the skill group. Derived
                                             						from: Skill_Group.Enterprise |
| DateTime | The date and time for the data of a selected row. Derived from: Call_Type.DateTime |
| Handled | The
                                             						total number of tasks handled to completion for the call type in the interval. Derived
                                             						from: Call_Type_SG_Interval.CallsHandled. |
| Avg Handle Time | The
                                             						average time spent by the agent in handling a task in the interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds). This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.Handle
                                             						Time/Call_Type_SG_Interval.CallsHandled. |
| %Queued | The
                                             						percentage of all handled tasks of the call type that were queued in the
                                             						interval. This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.CallsQHandled
                                             						/Call_Type_SG_Interval.CallsHandled. |
| Service Level | Service Level Type used to calculate Service level for the interval. Derived
                                             						from: Call_Type_SG_Interval.ServiceLevel. |
| Avg Speed of Answer | Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This value is an important measure of service quality because the time can vary,
                                             even over the course of one day, due to call volumes and staff levels. This field is
                                             						a calculated field, derived from: Call_Type_SG_Interval.AnswerWaitTime/Call_Type_SG_Interval.CallsAnswered. |
| Aban
                                             						within SL | The total number of calls of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes. Derived
                                             						from: Call_Type_SG_Interval.ServiceLevelAband. |
| Aban in
                                             						Queue | The
                                             						number of calls to the call type that were abandoned in the Router queue during
                                             						the interval. Derived
                                             						from: Call_Type_SG_Interval.RouterCallsAbandQ. |
| MaxQueued | The
                                             						maximum number of calls queued for this skill group during this interval. Calls
                                             						queued against multiple skill groups are included in the count for each skill
                                             						group to which the calls are queued. Derived
                                             						from: Call_Type_SG_Interval.MaxCallsQueued |
| Longest Queued | The
                                             						longest a call had to wait before being answered, abandoned, or otherwise
                                             						ended. This value includes time in the network queue, local queue, and ringing at the
                                             						agent if applicable. Derived
                                             						from: Call_Type_SG_Interval.MaxCallWaitTime |
| Tasks Picked | The total number of pick requests successfully routed to this skill group by this call type in the reporting interval. |
| Tasks Pulled | The total number of pull requests successfully routed to this skill group by this call type in the reporting interval. |
| Picks Failed | Number of pick request resulting in an error. |
| Pulls Failed | Number of pull requests resulting in an error. |

| Note | To run the CVA Historical Report, you must select the Call Types which are
                                          handling IVR Calls. |
|---|---|

| Column (Field) | Description |
|---|---|
| Call Type | The enterprise name for the call type. Derived from: Call_Type.EnterpriseName. |
| DateTime | The date and time of the selected row's data in MM/DD/YYYY
                                             (month, day, year) and HH:MM:SS (hours, minutes, seconds)
                                             format. Derived from: Call_Type_Interval.DateTime |
| Total Calls Handled at IVR | Total number of calls handled at IVR. Derived from: Call_Type_Interval.CallsOffered. |
| Calls Abandoned at IVR | Total number of calls abandoned at IVR. Derived from:
                                             Call_Type_Interval.TotalCallsAband -
                                             Call_Type_Interval.RouterCallsAbandQ -
                                             Call_Type_Interval.RouterCallsAbandToAgent |
| Average Time Spent on IVR | The average time spent on IVR is measured in HH:MM:SS (hours,
                                             minutes,seconds) format. Derived from:
                                             Call_Type_Interval.VRUTime/Call_Type_Interval.CallsOffered |
| Calls Transferred to Agent | Total number of calls getting transferred to the Agents. Derived from: Call_Type_Interval.VruAssistedCalls +
                                             Call_Type_Interval.VruOptOutIUnhandledCalls +
                                             Call_Type_Interval. VruScriptedXferredCalls +
                                             Call_Type_Interval.VruForcedXferredCalls |

| Column (Field) | Description |
|---|---|
| Call Type | The enterprise name for the call type. Derived from: Call_Type.EnterpriseName. |
| DateTime | The date and time of the selected row's data in MM/DD/YYYY
                                             (month, day, year) and HH:MM:SS (hours, minutes, seconds)
                                             format. Derived from: Call_Type_Interval.DateTime |
| Total Calls Handled at IVR | Total number of calls handled at IVR. Derived from: Call_Type_Interval.CallsOffered. |
| Calls Abandoned at IVR | Total number of calls abandoned at IVR. Derived from:
                                             Call_Type_Interval.TotalCallsAband -
                                             Call_Type_Interval.RouterCallsAbandQ -
                                             Call_Type_Interval.RouterCallsAbandToAgent |
| Average Time Spent on IVR | The average time spent on IVR is measured in HH:MM:SS (hours,
                                             minutes,seconds) format. Derived from:
                                             Call_Type_Interval.VRUTime/Call_Type_Interval.CallsOffered |
| Calls Transferred to Agent | Total number of calls getting transferred to the Agents. Derived from: Call_Type_Interval.VruAssistedCalls +
                                             Call_Type_Interval.VruOptOutIUnhandledCalls +
                                             Call_Type_Interval. VruScriptedXferredCalls +
                                             Call_Type_Interval.VruForcedXferredCalls |

| Column (Field) | Description |
|---|---|
| Enterprise Service | The enterprise name of the enterprise service. Derived from: Enterprise_Service.EnterpriseName. |
| Peripheral Service | The enterprise name of the peripheral service. Derived from: Service.EnterpriseName |
| DateTime | The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format. DateTime Derived from:
                                             Service_Interval.DateTime. |
| Ans | The total number of tasks associated with the service
                                             that were answered by agents in the interval. Derived from: Service_Interval.CallsAnswered. |
| Avg Speed of Answer | The average answer wait time in HH:MM:SS (hours,
                                             minutes, seconds) for all tasks answered for the service
                                             in the interval. Derived from: Service_Interval.AvgSpeedAnswer. |
| Handled | The number of tasks associated with the service that
                                             were handled in the interval. Derived from: Service_Interval.CallsHandled. |
| Avg Handle Time | The average handle time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service ending in
                                             the interval. Derived from: Service_Interval.AvgHandleTime. |
| Abandoned Queue | The number of tasks associated with the service that
                                             were abandoned in queue in the interval. Derived from: Service_Interval.CallsAbandQ. |
| Avg Delay Queue Abandoned | Average delay time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service that were
                                             abandoned in queue in the interval. Derived from: Service_Interval.AvgDelayQAband. |
| Task Queue | The number of tasks associated with the service that
                                             were queued in the interval. Derived from: Service_Interval.CallsQ. |
| Avg Delay Queue | The average delay in the queue for the tasks
                                             associated with the service in the interval. Derived from: Service_Interval.AvgDelayQ. |
| Service Level | The number of tasks associated with the service answered within the Unified ICM/Unified CCE service level threshold in the interval. Derived from: Service_Interval.ServiceLevel. |
| Service Level Type | The default value that indicates how Unified ICM software calculates the service level (that is, how it handles abandoned calls in calculating the service level). You can
                                             override this default for individual services. Derived From: Service_Interval.ServiceLevelType. |
| Transfer In | The number of tasks transferred into the service in
                                             the interval. The value is updated in the database when
                                             the call is completed. Derived from: Service_Interval.TransferInCalls. |
| Transfer Out | The number of tasks transferred out of the service in
                                             the interval. The value is updated in the database when
                                             the transfer of the call is completed. Derived from: Service_Interval.TransferOutCalls. |
| Out | The number of outbound tasks placed by agents
                                             associated with the service in the interval. Derived from: Service_Interval.CallsOut. |
| RONA | The count of tasks that are redirected with no answer
                                             within the skill group service level threshold in the
                                             last interval. Derived from:
                                             Service_Interval.ServiceLevelCallsDequeued. |

| Column (Field) | Description |
|---|---|
| Enterprise Service | The enterprise name of the enterprise service. Derived from: Enterprise_Service.EnterpriseName. |
| Peripheral Service | The enterprise name of the peripheral service. Derived from: Service.EnterpriseName |
| DateTime | The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format. DateTime Derived from:
                                             Service_Interval.DateTime. |
| Ans | The total number of tasks associated with the service
                                             that were answered by agents in the interval. Derived from: Service_Interval.CallsAnswered. |
| Avg Speed of Answer | The average answer wait time in HH:MM:SS (hours,
                                             minutes, seconds) for all tasks answered for the service
                                             in the interval. Derived from: Service_Interval.AvgSpeedAnswer. |
| Handled | The number of tasks associated with the service that
                                             were handled in the interval. Derived from: Service_Interval.CallsHandled. |
| Avg Handle Time | The average handle time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service ending in
                                             the interval. Derived from: Service_Interval.AvgHandleTime. |
| Abandoned Queue | The number of tasks associated with the service that
                                             were abandoned in queue in the interval. Derived from: Service_Interval.CallsAbandQ. |
| Avg Delay Queue Abandoned | Average delay time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service that were
                                             abandoned in queue in the interval. Derived from: Service_Interval.AvgDelayQAband. |
| Task Queue | The number of tasks associated with the service that
                                             were queued in the interval. Derived from: Service_Interval.CallsQ. |
| Avg Delay Queue | The average delay in the queue for the tasks
                                             associated with the service in the interval. Derived from: Service_Interval.AvgDelayQ. |
| Service Level | The number of tasks associated with the service answered within the Unified ICM/Unified CCE service level threshold in the interval. Derived from: Service_Interval.ServiceLevel. |
| Service Level Type | The default value that indicates how Unified ICM software calculates the service level (that is, how it handles abandoned calls in calculating the service level). You can
                                             override this default for individual services. Derived From: Service_Interval.ServiceLevelType. |
| Transfer In | The number of tasks transferred into the service in
                                             the interval. The value is updated in the database when
                                             the call is completed. Derived from: Service_Interval.TransferInCalls. |
| Transfer Out | The number of tasks transferred out of the service in
                                             the interval. The value is updated in the database when
                                             the transfer of the call is completed. Derived from: Service_Interval.TransferOutCalls. |
| Out | The number of outbound tasks placed by agents
                                             associated with the service in the interval. Derived from: Service_Interval.CallsOut. |
| RONA | The count of tasks that are redirected with no answer
                                             within the skill group service level threshold in the
                                             last interval. Derived from:
                                             Service_Interval.ServiceLevelCallsDequeued. |

| Column (Field | Description |
|---|---|
| Enterprise Skill Group | The enterprise skill group's enterprise name and ID. Derived from: Enterprise_Skill_Group.EnterpriseName (Enterprise_Skill_Group.EnterpriseSkillGroupID). |
| DateTime | The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format. Derived from: Skill_Group_Interval.DateTime. |
| Ent Queued | The number of tasks queued to this Skill Group in the interval. Derived from: Skill_Group_Interval.RouterCallsQueued. This field is Current by default and is applicable to Unified CCE only . The equivalent field for Unified CCE is named Total Queued (ICM) is Available by default. |
| Avg Speed of Answer | The skill group's average speed of answer in HH:MM:SS (hour, minutes, seconds) calculated from the time spent by callers when
                                             placed in queue and ringing at the agent's desktop before the task is answered divided by the number of tasks answered. Derived from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered. |
| COMPLETED TASKS |
| Total | The total number of tasks completed by this skill group in the interval. Derived from: (Skill_Group_Interval.CallsHandled + Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonRingCalls
                                             + Skill_Group_Interval.RedirectNoAnswer). |
| Abandoned | For voice: the total number of calls that were abandoned while the agent's phone was ringing. For non-voice: the total number
                                             of tasks that were abandoned while being offered to an agent. Derived from: (Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonCallsRing ). |
| RONA | The number of ACD calls to the skill group that rang at an agent's terminal and redirected on failure to answer. The value
                                             is counted at the time the call is diverted to another device, and the database is updated every reporting. |
| Handled | The number of Routed tasks handled within this skill group in the interval. Derived from: Skill_Group_Interval.CallsHandled. |
| Avg Handle Time | The Average Handle Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the skill group. Derived from: Skill_Group_Interval.HandledCallsTime / Skill_Group_Interval.CallsHandled. |
| Avg Active Time | The Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the skill group. Derived from: Skill_Group_Interval.HandledCallsTalkTime / Skill_Group_Interval.CallsHandled. |
| Abandon Hold | The number of tasks offered to the skill group that abandoned while being held or paused by the agent. The value is incremented
                                             at the time the call disconnects. Derived from: Skill_Group_Interval.AbandonHoldCalls. |
| End of Completed Tasks Grouping |
| Transfer In | The time in HH:MM:SS (hours, minutes, seconds) that handling calls transferred into the skill group in the interval. Derived from: Skill_Group_Interval.TransferInCallsTime. |
| Transfer Out | The number of tasks transferred out of the service in the interval. The value is updated in the database when the transfer
                                             of the call is completed. Derived from: Service_Interval.TransferOutCalls. |
| External Out | The number of completed outbound ACD calls made by agents in the skill group, during a interval. The value is updated in the
                                             database when any after-call work time associated with the call is completed. Derived from: Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIMES |
| Active Time | The total time spent in the Active state within this skill group in the interval, measured in HH:MM:SS (hours, minutes, seconds)
                                             format. Derived from: Skill_Group_Interval.TalkTime. |
| Hold Time | The total time agents spent in the Hold/Paused state in this skill group in the interval, measured in HH:MM:SS (hours, minutes,
                                             seconds) format. Derived from: Skill_Group_Interval.HoldTime. |
| Log On Duration | The total time in the interval the agents were logged into this skill group, measured in HH:MM:SS (hours, minutes, seconds)
                                             format. Derived from: Skill_Group_Interval.LoggedOnTime. |
| % Not Active | The percentage of time that agents have spent in the Not Active or Available state in relation to LoggedOnTime or the interval,
                                             whichever is less. Derived from: (Skill_Group_Interval.AvailTime / Skill_Group_Interval.LoggedOnTime). |
| % Not Ready | The percentage of time that agents spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever is
                                             less. Derived from: (Skill_Group_Interval.NotReadyTime / Skill_Group_Interval.LoggedOnTime). |
| % Active | The percentage of time the interval that the agent of this skill group has spent in Active state in this Skill Group in relation
                                             to LoggedOnTime. Derived from: Skill_Group_Interval.TalkTime / Skill_Group_Interval.LoggedOnTime. |
| % Hold | The percentage of time the interval that agents have put a call from this skill group on hold in relation to LoggedOnTime. Derived from: (Skill_Group_Interval.HoldTime / Skill_Group_Interval.LoggedOnTime). |
| % Reserved | The percentage of time the interval that agents have spent in Reserved state waiting for an ICM routed call from this skill group in relation to LoggedOnTime. Derived from: (Skill_Group_Interval.ReservedStateTime / Skill_Group_Interval.LoggedOnTime). |
| % Wrap Up | The percentage of time the interval that agents have spent in Wrap-up state after incoming or outgoing tasks in relation to
                                             LoggedOnTime or interval, whichever is less. Derived from: (Skill_Group_Interval.WorkReadyTime + Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime). |

| Column (Field | Description |
|---|---|
| Enterprise Skill Group | The enterprise skill group's enterprise name and ID. Derived from: Enterprise_Skill_Group.EnterpriseName (Enterprise_Skill_Group.EnterpriseSkillGroupID). |
| DateTime | The date and time of the selected row's data in MM/DD/YYYY (month, day, year) and HH:MM:SS (hour, minute, second) format. Derived from: Skill_Group_Interval.DateTime. |
| Ent Queued | The number of tasks queued to this Skill Group in the interval. Derived from: Skill_Group_Interval.RouterCallsQueued. This field is Current by default and is applicable to Unified CCE only . The equivalent field for Unified CCE is named Total Queued (ICM) is Available by default. |
| Avg Speed of Answer | The skill group's average speed of answer in HH:MM:SS (hour, minutes, seconds) calculated from the time spent by callers when
                                             placed in queue and ringing at the agent's desktop before the task is answered divided by the number of tasks answered. Derived from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered. |
| COMPLETED TASKS |
| Total | The total number of tasks completed by this skill group in the interval. Derived from: (Skill_Group_Interval.CallsHandled + Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonRingCalls
                                             + Skill_Group_Interval.RedirectNoAnswer). |
| Abandoned | For voice: the total number of calls that were abandoned while the agent's phone was ringing. For non-voice: the total number
                                             of tasks that were abandoned while being offered to an agent. Derived from: (Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonCallsRing ). |
| RONA | The number of ACD calls to the skill group that rang at an agent's terminal and redirected on failure to answer. The value
                                             is counted at the time the call is diverted to another device, and the database is updated every reporting. |
| Handled | The number of Routed tasks handled within this skill group in the interval. Derived from: Skill_Group_Interval.CallsHandled. |
| Avg Handle Time | The Average Handle Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the skill group. Derived from: Skill_Group_Interval.HandledCallsTime / Skill_Group_Interval.CallsHandled. |
| Avg Active Time | The Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the skill group. Derived from: Skill_Group_Interval.HandledCallsTalkTime / Skill_Group_Interval.CallsHandled. |
| Abandon Hold | The number of tasks offered to the skill group that abandoned while being held or paused by the agent. The value is incremented
                                             at the time the call disconnects. Derived from: Skill_Group_Interval.AbandonHoldCalls. |
| End of Completed Tasks Grouping |
| Transfer In | The time in HH:MM:SS (hours, minutes, seconds) that handling calls transferred into the skill group in the interval. Derived from: Skill_Group_Interval.TransferInCallsTime. |
| Transfer Out | The number of tasks transferred out of the service in the interval. The value is updated in the database when the transfer
                                             of the call is completed. Derived from: Service_Interval.TransferOutCalls. |
| External Out | The number of completed outbound ACD calls made by agents in the skill group, during a interval. The value is updated in the
                                             database when any after-call work time associated with the call is completed. Derived from: Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIMES |
| Active Time | The total time spent in the Active state within this skill group in the interval, measured in HH:MM:SS (hours, minutes, seconds)
                                             format. Derived from: Skill_Group_Interval.TalkTime. |
| Hold Time | The total time agents spent in the Hold/Paused state in this skill group in the interval, measured in HH:MM:SS (hours, minutes,
                                             seconds) format. Derived from: Skill_Group_Interval.HoldTime. |
| Log On Duration | The total time in the interval the agents were logged into this skill group, measured in HH:MM:SS (hours, minutes, seconds)
                                             format. Derived from: Skill_Group_Interval.LoggedOnTime. |
| % Not Active | The percentage of time that agents have spent in the Not Active or Available state in relation to LoggedOnTime or the interval,
                                             whichever is less. Derived from: (Skill_Group_Interval.AvailTime / Skill_Group_Interval.LoggedOnTime). |
| % Not Ready | The percentage of time that agents spent in the Not Ready state in relation to LoggedOnTime or the interval, whichever is
                                             less. Derived from: (Skill_Group_Interval.NotReadyTime / Skill_Group_Interval.LoggedOnTime). |
| % Active | The percentage of time the interval that the agent of this skill group has spent in Active state in this Skill Group in relation
                                             to LoggedOnTime. Derived from: Skill_Group_Interval.TalkTime / Skill_Group_Interval.LoggedOnTime. |
| % Hold | The percentage of time the interval that agents have put a call from this skill group on hold in relation to LoggedOnTime. Derived from: (Skill_Group_Interval.HoldTime / Skill_Group_Interval.LoggedOnTime). |
| % Reserved | The percentage of time the interval that agents have spent in Reserved state waiting for an ICM routed call from this skill group in relation to LoggedOnTime. Derived from: (Skill_Group_Interval.ReservedStateTime / Skill_Group_Interval.LoggedOnTime). |
| % Wrap Up | The percentage of time the interval that agents have spent in Wrap-up state after incoming or outgoing tasks in relation to
                                             LoggedOnTime or interval, whichever is less. Derived from: (Skill_Group_Interval.WorkReadyTime + Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime). |

| Note | You can use the report for Trunk Groups associated with TDM peripherals. |
|---|---|

| Column (Field) | Description |
|---|---|
| IVR Ports | The name of the IVR port used by the trunk group. Derived from: Trunk_Group.EnterpriseName. |
| DateTime | The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format. Derived from: Trunk_Group_Half_Hour.DateTime. |
| Ports | The number of ports in the group in service at the end
                                             of the interval. Derived from: Trunk_Group_Half_Hour.TrunksInService. |
| % Busy | The percentage of time that the trunk groups in
                                             service were in use in the interval (for Inbound Only). Derived from: Trunk_Group_Half_Hour.InUseInboundTime
                                             / Trunk_Group_Half_Hour.InServiceTime. |
| All Ports Busy | The total time, in HH:MM:SS (hours, minutes, seconds),
                                             in the interval, that all ports in the group were busy. Derived from: Trunk_Group_Half_Hour.AllTrunksBusy. |

| Column (Field) | Description |
|---|---|
| IVR Ports | The name of the IVR port used by the trunk group. Derived from: Trunk_Group.EnterpriseName. |
| DateTime | The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format. Derived from: Trunk_Group_Half_Hour.DateTime. |
| Ports | The number of ports in the group in service at the end
                                             of the interval. Derived from: Trunk_Group_Half_Hour.TrunksInService. |
| % Busy | The percentage of time that the trunk groups in
                                             service were in use in the interval (for Inbound Only). Derived from: Trunk_Group_Half_Hour.InUseInboundTime
                                             / Trunk_Group_Half_Hour.InServiceTime. |
| All Ports Busy | The total time, in HH:MM:SS (hours, minutes, seconds),
                                             in the interval, that all ports in the group were busy. Derived from: Trunk_Group_Half_Hour.AllTrunksBusy. |

| Column (Field) | Description |
|---|---|
| Service | The enterprise name of the peripheral service. Derived from: Service.EnterpriseName. |
| DateTime | The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format. Derived from: Service_Interval.DateTime. |
| Answered | The total number of tasks associated with the service
                                             that were answered by agents in the interval. Derived from: Service_Interval.CallsAnswered. |
| Avg Speed of Answer | The average answer wait time in HH:MM:SS (hours,
                                             minutes, seconds) for all tasks answered for the service
                                             in the interval. Derived from: Service_Interval.AvgSpeedAnswer. |
| Handled | The number of tasks associated with the service that
                                             were handled in the interval. Derived from: Service_Interval.CallsHandled. |
| Avg Handle Time | The average handle time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service ending in
                                             the interval. Derived from:  Service_Interval.HandleTime / Service_Interval.CallsHandled. |
| Aban in Queue | The number of tasks associated with the service that
                                             were abandoned in queue in the interval. Derived from: Service_Interval.CallsAbandQ. |
| Average Delay Queue Abandon | The average delay time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service that were
                                             abandoned in queue in the interval. Derived from:  Serivce_Interval.DelayQAbandTime / Service_Interval.CallsAbandQ. |
| Task In Queue | The total number of tasks associated with the service
                                             that were queued in the interval. Derived from: Service_Interval.CallsQ. |
| Avg Delay in Queue | The average delay in queue for tasks associated with
                                             the service in the interval. Derived from: Service_Interval.AvgDelayQ. |
| Service Level | The Enterprise service level for the service in the
                                             interval. Derived from: Service_Interval.ServiceLevel. |
| Service Level Type | The default value that indicates how the service level is calculated by the ICM software (that is, how abandoned calls are handled in calculating the service level). You can override this default for individual
                                             services. Derived From: Service_Interval.ServiceLevelType. |
| Transfer In | The number of tasks transferred into the service in
                                             the interval. The value is updated in the database when
                                             the call is completed. Derived from: Service_Interval.TransferInCalls. |
| Transfer Out | The number of tasks transferred out of the service in
                                             the interval. The value is updated in the database when
                                             the transfer of the call is completed. Derived from: Service_Interval.TransferOutCalls. |
| Out | The number of outbound tasks placed by agents
                                             associated with the service in the interval. Derived from: Service_Interval.CallsOut. |
| RONA | The count of calls that are redirected with no answer
                                             within the skill group service level threshold in the
                                             last interval. Derived from:
                                             Service_Interval.RedirectNoAnsCalls. |

| Column (Field) | Description |
|---|---|
| Service | The enterprise name of the peripheral service. Derived from: Service.EnterpriseName. |
| DateTime | The date and time of the selected row's data in
                                             MM/DD/YYYY (month, day, year) and HH:MM:SS (hour,
                                             minute, second) format. Derived from: Service_Interval.DateTime. |
| Answered | The total number of tasks associated with the service
                                             that were answered by agents in the interval. Derived from: Service_Interval.CallsAnswered. |
| Avg Speed of Answer | The average answer wait time in HH:MM:SS (hours,
                                             minutes, seconds) for all tasks answered for the service
                                             in the interval. Derived from: Service_Interval.AvgSpeedAnswer. |
| Handled | The number of tasks associated with the service that
                                             were handled in the interval. Derived from: Service_Interval.CallsHandled. |
| Avg Handle Time | The average handle time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service ending in
                                             the interval. Derived from:  Service_Interval.HandleTime / Service_Interval.CallsHandled. |
| Aban in Queue | The number of tasks associated with the service that
                                             were abandoned in queue in the interval. Derived from: Service_Interval.CallsAbandQ. |
| Average Delay Queue Abandon | The average delay time in HH:MM:SS (hours, minutes,
                                             seconds) of tasks associated with the service that were
                                             abandoned in queue in the interval. Derived from:  Serivce_Interval.DelayQAbandTime / Service_Interval.CallsAbandQ. |
| Task In Queue | The total number of tasks associated with the service
                                             that were queued in the interval. Derived from: Service_Interval.CallsQ. |
| Avg Delay in Queue | The average delay in queue for tasks associated with
                                             the service in the interval. Derived from: Service_Interval.AvgDelayQ. |
| Service Level | The Enterprise service level for the service in the
                                             interval. Derived from: Service_Interval.ServiceLevel. |
| Service Level Type | The default value that indicates how the service level is calculated by the ICM software (that is, how abandoned calls are handled in calculating the service level). You can override this default for individual
                                             services. Derived From: Service_Interval.ServiceLevelType. |
| Transfer In | The number of tasks transferred into the service in
                                             the interval. The value is updated in the database when
                                             the call is completed. Derived from: Service_Interval.TransferInCalls. |
| Transfer Out | The number of tasks transferred out of the service in
                                             the interval. The value is updated in the database when
                                             the transfer of the call is completed. Derived from: Service_Interval.TransferOutCalls. |
| Out | The number of outbound tasks placed by agents
                                             associated with the service in the interval. Derived from: Service_Interval.CallsOut. |
| RONA | The count of calls that are redirected with no answer
                                             within the skill group service level threshold in the
                                             last interval. Derived from:
                                             Service_Interval.RedirectNoAnsCalls. |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The
                                             						skill group's enterprise name and ID. Derived
                                             						from:  Skill_Group.EnterpriseName (Skill_Group.SkillTargetID). |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| DateTime | The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format. Derived
                                             						from: Skill_Group_Interval.DateTime. |
| Ent Queued | The number
                                             						of tasks queued to this Skill Group in the interval. Derived
                                             						from:  Skill_Group_Interval.RouterQueueCalls + Skill_Group_Interval.CallsQueued. This field is Current by default and is applicable to Unified CCE only. The equivalent field for Unified CCE is named Total Queued (ICM) is Available by default. |
| Avg Speed of Answer | The skill
                                             						group's average speed of answer in HH:MM:SS (hour, minutes, seconds) calculated
                                             						from the time spent by callers when placed in queue and ringing at the agent's
                                             						desktop before the task is answered divided by the number of tasks answered. Derived
                                             						from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered. |
| SERVICE LEVEL |
| Service Level Answer | The count
                                             						of calls that are routed to the skill group or queued to the skill group in the
                                             						last interval. Derived
                                             						from: Skill_Group_Interval.ServiceLevelCalls. |
| Service Level Abandon | The count
                                             						of calls that are abandoned within the skill group service level threshold in
                                             						the last interval. Derived
                                             						from:  Skill_Group_Interval.ServiceLevelCallsAband. |
| COMPLETED TASKS |
| Total | The total
                                             						number of tasks completed by this skill group in the interval. Derived
                                             						from: (Skill_Group_Interval.CallsHandled +
                                             						Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonRingCalls
                                             						+ Skill_Group_Interval.RedirectNoAnswer). |
| Abandoned | For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing. For non-voice: the total number of tasks that were abandoned while
                                             						being offered to an agent. Derived
                                             						from: (Skill_Group_Interval.RouterCallsAbandQ +
                                             						Skill_Group_Interval.AbandonCallsRing). |
| RONA | The count of calls that are redirected with no answer within the skill group service level threshold in the last interval. Derived
                                             						from:  Skill_Group_Interval.RedirectNoAnsCalls. |
| Handled | The number
                                             						of Routed tasks handled within this skill group in the interval. Derived
                                             						from: Skill_Group_Interval.CallsHandled. |
| Avg Handle Time | The
                                             						Average Handle Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						skill group. Derived
                                             						from: Skill_Group_Interval.HandledCallsTime /
                                             						Skill_Group_Interval.CallsHandled. |
| Avg Active Time | The
                                             						Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						skill group. Derived
                                             						from: Skill_Group_Interval.HandledCallsTalkTime /
                                             						Skill_Group_Interval.CallsHandled. |
| Abandon Hold | The number
                                             						of tasks offered to the skill group that abandoned while being held or paused
                                             						by the agent. The value is incremented at the time the call disconnects. Derived
                                             						from: Skill_Group_Interval.AbandonHoldCalls. |
| Tasks Picked | The total number of pick requests successfully routed to this skill group in the reporting interval. |
| Tasks Pulled | The total number of pull requests successfully routed to this skill group in the reporting interval. |
| Picks Failed | Number of Pick request resulting in an error. |
| Pulls Failed | Number of Pull request resulting in an error. |
| End of Completed Tasks
                                                						  Grouping |
| Transfer In | The number of tasks transferred into the skill group in the interval. The value is updated in the database when the call
                                             is completed. Derived
                                             						from:  Skill_Group_Interval.TransferInCalls. |
| Transfer Out | The number
                                             						of tasks this agent transferred to another agent or skill group in the
                                             						interval. This includes Consultative Calls. The value is updated in the
                                             						database when the transfer of the call is completed. Derived
                                             						from: Skill_Group_Interval.TransferredOutCalls +
                                             						Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | For
                                             						default skill groups: the number of times an agent initiated an outgoing
                                             						external call in the interval. For routing skill groups: the number of times an
                                             						agent initiated a transfer or conference to an external device in the interval. Derived
                                             						from: Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIME |
| Active
                                             						Time | The time
                                             						in HH:MM:SS (hours, minutes, seconds) that agents in the skill group were in
                                             						the Active state in the interval. Derived
                                             						from: Skill_Group_Interval.TalkTime. |
| Hold Time | The total
                                             						time agents spent in the Hold/Paused state in this skill group, measured in
                                             						HH:MM:SS (hours, minutes, seconds) format. Includes Incoming Direct and
                                             						Outgoing Internal, although call counts are not shown in this report. Derived
                                             						from: Skill_Group_Interval.HoldTime. |
| Logged On Duration | The total duration in HH:MM:SS (hours, minutes, and seconds)
                                             									during the period that agents were logged into this skill group. Derived from: Skill_Group_Interval.LoggedOnTime |
| % Not
                                             						Active | The
                                             						percentage of agents in the skill group who are NOT currently involved in tasks
                                             						and who are ready to accept calls or tasks. Derived
                                             						from:  Skill_Group_Interval.AvailTime / Skill_Group_Interval.LoggedOnTime. |
| % Not
                                             						Ready | The
                                             						percentage of time that agents spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Derived
                                             						from: (Skill_Group_Interval.NotReadyTime / Skill_Group_Interval.LoggedOnTime). |
| % Active | The
                                             						percentage of agents in the skill group who are working on incoming tasks or
                                             						who are in one of the talking states. Derived
                                             						from: (Skill_Group_Skill_Group_Interval.TalkingInTime + Skill_Group_Skill_Group_Interval.TalkingOutTime +
                                             						Skill_Group_Skill_Group_Interval.TalkingOtherTime + Skill_Group.Skill_Group_Interval.TalkingAutoOutTime +
                                             						Skill_Group.Skill_Group_Interval.TalkingPreviewTime + Skill_Group.Skill_Group_Interval.TalkingReserveTime) /
                                             						Skill_Group_Skill_Group_Interval.LoggedOnTime. |
| % Hold | The
                                             						percentage of time that agents spent in the Hold/Paused state in relation to
                                             						LoggedOnTime or interval, whichever is less. Derived
                                             						from: (Skill_Group_Interval.HoldTime / Skill_Group_Interval.LoggedOnTime). |
| %
                                             						Reserved | The
                                             						percentage of time that agents spent working on Reserved time in relation to
                                             						LoggedOnTime or interval, whichever is less. Derived
                                             						from: (Skill_Group_Interval. ReservedStateTime /
                                             						Skill_Group_Interval.LoggedOnTime). |
| % Wrap
                                             						Up | The
                                             						percentage of time that agents have spent in Wrap-up state after incoming or
                                             						outgoing calls in relation to LoggedOnTime or interval, whichever is less. Derived
                                             						from: ((Skill_Group_Interval.WorkReadyTime +
                                             						Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime). |
| End of Agent State Times Grouping |
| Max Queued | The
                                             						maximum number of calls in queue for this call type during this interval. Derived
                                             						from: Skill_Group_Interval.RouterMaxCallsQueued. |
| Longest Queued | The
                                             						longest time a call had to wait before it was dispositioned
                                             						(abandoned, answered, and so on) in this interval. Derived
                                             						from: Skill_Group_Interval.RouterMaxCallWaitTime. |
| Abandon Rings | The
                                             						total number of ACD calls to the skill group that were abandoned while ringing
                                             						at an agent's position. The value is incremented at the time the call
                                             						disconnects. Derived
                                             						from: Skill_Group_Interval.AbandonRingCalls. |
| Answered | The
                                             						number of calls answered by agents associated with a skill group during the
                                             						reporting interval. This value is set by the PG. The number of calls answered
                                             						includes only handled calls and internal calls received. The value is
                                             						incremented at the time the call is answered. Derived
                                             						from: Skill_Group_Interval.CallsAnswered. |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The
                                             						skill group's enterprise name and ID. Derived
                                             						from:  Skill_Group.EnterpriseName (Skill_Group.SkillTargetID). |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| DateTime | The date
                                             						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                             						HH:MM:SS (hour, minute, second) format. Derived
                                             						from: Skill_Group_Interval.DateTime. |
| Ent Queued | The number
                                             						of tasks queued to this Skill Group in the interval. Derived
                                             						from:  Skill_Group_Interval.RouterQueueCalls + Skill_Group_Interval.CallsQueued. This field is Current by default and is applicable to Unified CCE only. The equivalent field for Unified CCE is named Total Queued (ICM) is Available by default. |
| Avg Speed of Answer | The skill
                                             						group's average speed of answer in HH:MM:SS (hour, minutes, seconds) calculated
                                             						from the time spent by callers when placed in queue and ringing at the agent's
                                             						desktop before the task is answered divided by the number of tasks answered. Derived
                                             						from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered. |
| SERVICE LEVEL |
| Service Level Answer | The count
                                             						of calls that are routed to the skill group or queued to the skill group in the
                                             						last interval. Derived
                                             						from: Skill_Group_Interval.ServiceLevelCalls. |
| Service Level Abandon | The count
                                             						of calls that are abandoned within the skill group service level threshold in
                                             						the last interval. Derived
                                             						from:  Skill_Group_Interval.ServiceLevelCallsAband. |
| COMPLETED TASKS |
| Total | The total
                                             						number of tasks completed by this skill group in the interval. Derived
                                             						from: (Skill_Group_Interval.CallsHandled +
                                             						Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.AbandonRingCalls
                                             						+ Skill_Group_Interval.RedirectNoAnswer). |
| Abandoned | For voice:
                                             						the total number of calls that were abandoned while the agent's phone was
                                             						ringing. For non-voice: the total number of tasks that were abandoned while
                                             						being offered to an agent. Derived
                                             						from: (Skill_Group_Interval.RouterCallsAbandQ +
                                             						Skill_Group_Interval.AbandonCallsRing). |
| RONA | The count of calls that are redirected with no answer within the skill group service level threshold in the last interval. Derived
                                             						from:  Skill_Group_Interval.RedirectNoAnsCalls. |
| Handled | The number
                                             						of Routed tasks handled within this skill group in the interval. Derived
                                             						from: Skill_Group_Interval.CallsHandled. |
| Avg Handle Time | The
                                             						Average Handle Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						skill group. Derived
                                             						from: Skill_Group_Interval.HandledCallsTime /
                                             						Skill_Group_Interval.CallsHandled. |
| Avg Active Time | The
                                             						Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						skill group. Derived
                                             						from: Skill_Group_Interval.HandledCallsTalkTime /
                                             						Skill_Group_Interval.CallsHandled. |
| Abandon Hold | The number
                                             						of tasks offered to the skill group that abandoned while being held or paused
                                             						by the agent. The value is incremented at the time the call disconnects. Derived
                                             						from: Skill_Group_Interval.AbandonHoldCalls. |
| Tasks Picked | The total number of pick requests successfully routed to this skill group in the reporting interval. |
| Tasks Pulled | The total number of pull requests successfully routed to this skill group in the reporting interval. |
| Picks Failed | Number of Pick request resulting in an error. |
| Pulls Failed | Number of Pull request resulting in an error. |
| End of Completed Tasks
                                                						  Grouping |
| Transfer In | The number of tasks transferred into the skill group in the interval. The value is updated in the database when the call
                                             is completed. Derived
                                             						from:  Skill_Group_Interval.TransferInCalls. |
| Transfer Out | The number
                                             						of tasks this agent transferred to another agent or skill group in the
                                             						interval. This includes Consultative Calls. The value is updated in the
                                             						database when the transfer of the call is completed. Derived
                                             						from: Skill_Group_Interval.TransferredOutCalls +
                                             						Skill_Group_Interval.NetTransferredOutCalls. |
| External Out | For
                                             						default skill groups: the number of times an agent initiated an outgoing
                                             						external call in the interval. For routing skill groups: the number of times an
                                             						agent initiated a transfer or conference to an external device in the interval. Derived
                                             						from: Skill_Group_Interval.AgentOutCalls. |
| AGENT STATE TIME |
| Active
                                             						Time | The time
                                             						in HH:MM:SS (hours, minutes, seconds) that agents in the skill group were in
                                             						the Active state in the interval. Derived
                                             						from: Skill_Group_Interval.TalkTime. |
| Hold Time | The total
                                             						time agents spent in the Hold/Paused state in this skill group, measured in
                                             						HH:MM:SS (hours, minutes, seconds) format. Includes Incoming Direct and
                                             						Outgoing Internal, although call counts are not shown in this report. Derived
                                             						from: Skill_Group_Interval.HoldTime. |
| Logged On Duration | The total duration in HH:MM:SS (hours, minutes, and seconds)
                                             									during the period that agents were logged into this skill group. Derived from: Skill_Group_Interval.LoggedOnTime |
| % Not
                                             						Active | The
                                             						percentage of agents in the skill group who are NOT currently involved in tasks
                                             						and who are ready to accept calls or tasks. Derived
                                             						from:  Skill_Group_Interval.AvailTime / Skill_Group_Interval.LoggedOnTime. |
| % Not
                                             						Ready | The
                                             						percentage of time that agents spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. Derived
                                             						from: (Skill_Group_Interval.NotReadyTime / Skill_Group_Interval.LoggedOnTime). |
| % Active | The
                                             						percentage of agents in the skill group who are working on incoming tasks or
                                             						who are in one of the talking states. Derived
                                             						from: (Skill_Group_Skill_Group_Interval.TalkingInTime + Skill_Group_Skill_Group_Interval.TalkingOutTime +
                                             						Skill_Group_Skill_Group_Interval.TalkingOtherTime + Skill_Group.Skill_Group_Interval.TalkingAutoOutTime +
                                             						Skill_Group.Skill_Group_Interval.TalkingPreviewTime + Skill_Group.Skill_Group_Interval.TalkingReserveTime) /
                                             						Skill_Group_Skill_Group_Interval.LoggedOnTime. |
| % Hold | The
                                             						percentage of time that agents spent in the Hold/Paused state in relation to
                                             						LoggedOnTime or interval, whichever is less. Derived
                                             						from: (Skill_Group_Interval.HoldTime / Skill_Group_Interval.LoggedOnTime). |
| %
                                             						Reserved | The
                                             						percentage of time that agents spent working on Reserved time in relation to
                                             						LoggedOnTime or interval, whichever is less. Derived
                                             						from: (Skill_Group_Interval. ReservedStateTime /
                                             						Skill_Group_Interval.LoggedOnTime). |
| % Wrap
                                             						Up | The
                                             						percentage of time that agents have spent in Wrap-up state after incoming or
                                             						outgoing calls in relation to LoggedOnTime or interval, whichever is less. Derived
                                             						from: ((Skill_Group_Interval.WorkReadyTime +
                                             						Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime). |
| End of Agent State Times Grouping |
| Max Queued | The
                                             						maximum number of calls in queue for this call type during this interval. Derived
                                             						from: Skill_Group_Interval.RouterMaxCallsQueued. |
| Longest Queued | The
                                             						longest time a call had to wait before it was dispositioned
                                             						(abandoned, answered, and so on) in this interval. Derived
                                             						from: Skill_Group_Interval.RouterMaxCallWaitTime. |
| Abandon Rings | The
                                             						total number of ACD calls to the skill group that were abandoned while ringing
                                             						at an agent's position. The value is incremented at the time the call
                                             						disconnects. Derived
                                             						from: Skill_Group_Interval.AbandonRingCalls. |
| Answered | The
                                             						number of calls answered by agents associated with a skill group during the
                                             						reporting interval. This value is set by the PG. The number of calls answered
                                             						includes only handled calls and internal calls received. The value is
                                             						incremented at the time the call is answered. Derived
                                             						from: Skill_Group_Interval.CallsAnswered. |

| Column (Field) | Description |
|---|---|
| Precision Queue | The enterprise name of the Precision Queue and its precision queue ID. Derived from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID |
| Media | The enterprise name of the Media Routing Domain associated with the precision queue. Media is derived from: Media_Routing_Domain.EnterpriseName. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date and time at the start of the reporting interval. Derived from: Router_Queue_Interval.DateTime |
| Avg Speed of Answer | The precision queue average speed of answer in HH:MM:SS (hour, minutes, seconds) based on the time spent by callers in the
                                             queue and ringing at an agent desktop before the task is answered divided by the number of answered tasks. Derived from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered |
| Interval 1 - Interval 10 |
| Interval | The amount of time that a call should be handled by. Derived from: Bucket_Interval.UpperBound1(through 9) |
| Answered | The number of calls answered in this interval. Derived from: RouterQueueInterval.AnsInterval1 (through10) Note : AnsInterval1 is the number of calls answered within Interval 1. For Call Type Interval, AnsInterval is calculated from the
                                             time the call is queued to a skill group or a precision queue, to the time the call is answered. This includes any requery
                                             time. This field is applicable to both Unified ICM and Unified CCE with the following exception: The field is not incremented if the call is answered by an agent on a standard ACD unless the call was translation routed. |
| Abandoned | The number of calls abandoned in this interval. Derived from: RouterQueueInterval.AbandInterval1 (through10) Note : AbandInterval1 is the number of calls abandoned within Interval 1. For Call Type Interval, AbandInterval is calculated from
                                             the time the call is queued to a skill group or a precision queue, to the time the call is abandoned. This includes any requery
                                             time. This field is applicable to both Unified ICM and Unified CCE with the following exception: The field is not incremented if the call is answered by an agent on a standard ACD unless the call was translation routed. |
| MaxQueued | The maximum number of calls in queue for this Skill Group during this interval. Derived from: Skill_Group_Interval.RouterMaxCallsQueued |
| Longest Queued | The longest time a call elapsed before it was abandoned or answered in this interval. Derived from: Skill_Group_Interval.RouterMaxCallWaitTime |

| Column (Field) | Description |
|---|---|
| Precision Queue | The enterprise name of the Precision Queue and its precision queue ID. Derived from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID |
| Media | The enterprise name of the Media Routing Domain associated with the precision queue. Media is derived from: Media_Routing_Domain.EnterpriseName. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date and time at the start of the reporting interval. Derived from: Router_Queue_Interval.DateTime |
| Avg Speed of Answer | The precision queue average speed of answer in HH:MM:SS (hour, minutes, seconds) based on the time spent by callers in the
                                             queue and ringing at an agent desktop before the task is answered divided by the number of answered tasks. Derived from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered |
| Interval 1 - Interval 10 |
| Interval | The amount of time that a call should be handled by. Derived from: Bucket_Interval.UpperBound1(through 9) |
| Answered | The number of calls answered in this interval. Derived from: RouterQueueInterval.AnsInterval1 (through10) Note : AnsInterval1 is the number of calls answered within Interval 1. For Call Type Interval, AnsInterval is calculated from the
                                             time the call is queued to a skill group or a precision queue, to the time the call is answered. This includes any requery
                                             time. This field is applicable to both Unified ICM and Unified CCE with the following exception: The field is not incremented if the call is answered by an agent on a standard ACD unless the call was translation routed. |
| Abandoned | The number of calls abandoned in this interval. Derived from: RouterQueueInterval.AbandInterval1 (through10) Note : AbandInterval1 is the number of calls abandoned within Interval 1. For Call Type Interval, AbandInterval is calculated from
                                             the time the call is queued to a skill group or a precision queue, to the time the call is abandoned. This includes any requery
                                             time. This field is applicable to both Unified ICM and Unified CCE with the following exception: The field is not incremented if the call is answered by an agent on a standard ACD unless the call was translation routed. |
| MaxQueued | The maximum number of calls in queue for this Skill Group during this interval. Derived from: Skill_Group_Interval.RouterMaxCallsQueued |
| Longest Queued | The longest time a call elapsed before it was abandoned or answered in this interval. Derived from: Skill_Group_Interval.RouterMaxCallWaitTime |

| Column (Field) | Description |
|---|---|
| Precision Queue | The enterprise name of the precision queue and its precision queue ID. Derived from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date and time at the start of the reporting interval. Derived from: Router_Queue_Interval.DateTime |
| Step 1 - Step 10 |
| Offered | The number of calls offered in this step. Derived from: Router_Queue_Interval.OfferedStep(n) |
| Answered | The total of all calls offered in this precision queue that were answered in this step. Derived from: Router_Queue_Interval.AnsStep(n) |
| Chart | This is a link to a Precision Queue Efficiency Drill Down report. For more information, see Precision Queue Efficiency Drill Down . |

| Column (Field) | Description |
|---|---|
| Precision Queue | The enterprise name of the precision queue and its precision queue ID. Derived from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date and time at the start of the reporting interval. Derived from: Router_Queue_Interval.DateTime |
| Step 1 - Step 10 |
| Offered | The number of calls offered in this step. Derived from: Router_Queue_Interval.OfferedStep(n) |
| Skipped | The total of all calls offered in this precision queue that were skippeded in this step. Derived from: Router_Queue_Interval. |
| Answered | The total of all calls offered in this precision queue that were answered in this step. Derived from: Router_Queue_Interval.AnsStep(n) |
| Abandoned | The total of all calls offered in this precision queue that were abandoned in this step. Derived from: Router_Queue_Interval. |
| Overflow | The total of all calls offered in this precision queue that overflowed. Derived from: Router_Queue_Interval. |
| PreciscionQueueChart | This is a link to a Precision Queue Efficiency Drill Down report. For more information, see Precision Queue Efficiency Drill Down . |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the precision queue and its precision queue ID. Derived
                                             						from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date
                                             						and time at the start of the reporting interval. Derived
                                             						from: Router_Queue_Interval.DateTime |
| Step 1 - Step 10 |
| Offered | The
                                             						number of calls offered in this step. Derived
                                             						from: Router_Queue_Interval.OfferedStep(n) |
| Answered | The
                                             						total of all calls offered in this precision queue that were answered in this
                                             						step. Derived
                                             						from: Router_Queue_Interval.AnsStep(n) |
|  |
| Chart | This is
                                             						a link to a Precision Queue Efficiency Drill Down report. For more information,
                                             						see Precision Queue Efficiency Drill Down . |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the precision queue and its precision queue ID. Derived
                                             						from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. |
| DateTime | The date
                                             						and time at the start of the reporting interval. Derived
                                             						from: Router_Queue_Interval.DateTime |
| Step 1 - Step 10 |
| Offered | The
                                             						number of calls offered in this step. Derived
                                             						from: Router_Queue_Interval.OfferedStep(n) |
| Answered | The
                                             						total of all calls offered in this precision queue that were answered in this
                                             						step. Derived
                                             						from: Router_Queue_Interval.AnsStep(n) |
|  |
| Chart | This is
                                             						a link to a Precision Queue Efficiency Drill Down report. For more information,
                                             						see Precision Queue Efficiency Drill Down . |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the Agent Precision Queue. Derived from: Precision_Queue.EnterpriseName. |
| Media | The
                                             						enterprise name of the Media Routing Domain associated with the precision
                                             						queue. Media is derived
                                             						from: Media_Routing_Domain.EnterpriseName. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |
| DateTime | The
                                             						date and time of the data for a selected row. Derived
                                             						from: Router_Queue_Interval.DateTime. |
| Queued | Derived
                                             						from: Router_Queue_Interval.QueueCalls. |
| Avg
                                             						Speed of Answer | The
                                             						precision queue average speed of answer in HH:MM:SS(hour, minutes, seconds)
                                             						based on the time spent by callers in the queue and ringing at an agent desktop
                                             						before the task is answered divided by the number of answered tasks. Derived
                                             						from: Skill_Group_Interval.AnswerWaitTime /Skill_Group_Interval.CallsAnswered. |
| Service Level |
| Service Level | Service Level Type used to calculate Service level for the
                                             						interval. Derived from: Router_Queue_Interval.ServiceLevel. |
| Answer | The
                                             						number of calls that are routed to the precision queue or queued to the
                                             						precision queue in the last interval. Derived
                                             						from: Router_Queue_Interval.ServiceLevelCalls |
| Abandon | The
                                             						number of calls that are abandoned within the precision queue service level
                                             						threshold in the last interval. Derived
                                             						from: Router_Queue_Interval.ServiceLevelCallsAband. |
| Completed Tasks |
| Total | The total number of tasks completed by this precision queue in the interval. Derived from:(Router_Queue_Interval.CallsHandled++ Router_Queue_Interval.RedirectNoAnsCalls+ Router_Queue_Interval.CallsAbandQ+
                                             Router_Queue_Interval.RouterError+ Router_Queue_Interval.CallsAbandToAgent) |
| Abandoned | The
                                             						sum of: The number of calls to the call type that are abandoned in the Router queue during the reporting interval. The number of calls associated with this skillgroup that are abandoned at the agent desktop before being answered during the
                                                   reporting interval. Termination_Call_Detail records generated by agent PG with a Call Disposition Flag of 2 are also counted
                                                   for this field. This does not include short calls and the calls that were abandoned in the VRU. Derived
                                             						from: Router_Queue_Interval.CallsAbandQ + Router_Queue_Interval.CallsAbandToAgent. |
| RONA | The count of calls that are redirected with no answer within the Precision Queue service level threshold in the last interval. Derived from: Router_Queue_Interval.RedirectNoAnsCalls |
| Handled | The number of inbound calls for which agents in the precision queue during the interval answered and completed. Derived from: Router_Queue_Interval.CallsHandled. |
| Avg
                                             						Handle Time | The
                                             						average time spent by agents in this precision queue handling a task in the
                                             						interval. This
                                             						field is a calculated field, derived from:
                                             						(Skill_Group_Interval.HandledCallsTime / Skill_Group_Interval.CallsHandled) |
| Avg
                                             						Active Time | The
                                             						Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						precision queue. Derived
                                             						from: Skill_Group_Interval.HandledCallsTalkTime
                                             						/Skill_Group_Interval.CallsHandled |
| Abandon
                                             						Hold | The
                                             						number of tasks offered to the precision queue that are abandoned while being
                                             						held or paused by the agent. The value is incremented at the time the call
                                             						disconnects. Derived
                                             						from: Skill_Group_Interval.AbandonHoldCalls |
| Tasks Picked | The total number of pick requests successfully routed by the precision queue. |
| Tasks Pulled | The total number of pull requests successfully routed by the precision queue. |
| Picks Failed | Number of pick request resulting in an error. |
| Pulls Failed | Number of pull request resulting in an error. |
| End of Completed Tasks Grouping |
| Transfer In | The number of tasks transferred into the precision queue in the interval. Derived from: Skill_Group_Interval.TransferInCalls |
| Transfer Out | The number of tasks this agent transferred to another agent or precision queue in the interval. This includes Consultative
                                             Calls. The value is updated in the database when the transfer of the call is completed. Derived from: Skill_Group_Interval.TransferredOutCalls + Skill_Group_Interval.NetTransferredOutCalls |
| External Out | For default precision queues: the number of times an agent initiated an outgoing external call in the interval. For routing
                                             precision queues: the number of times an agent initiated a transfer or conference to an external device in the interval. Derived from: Skill_Group_Interval.AgentOutCalls |
| Agent State Time |
| Active
                                             						Time | The
                                             						time in HH:MM:SS (hours, minutes, seconds) that agents in the precision queue
                                             						were in the Active state in the interval. Derived from: Skill_Group_Interval.TalkTime |
| Hold
                                             						Time | The
                                             						total time agents spent in the Hold/Paused state in this precision queue,
                                             						measured in HH:MM:SS (hours, minutes, seconds) format. Includes Incoming Direct
                                             						and Outgoing Internal, although call counts are not shown in this report. Derived from: Skill_Group_Interval.HoldTime |
| Logged
                                             						On Time | The
                                             						total duration in HH:MM:SS (hours, minutes, and seconds) during the period that
                                             						agents were logged into this skill group. Derived from: Skill_Group_Interval.LoggedOnTime |
| %Not
                                             						Active | The
                                             						percentage of time that agents spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. This field applies to all precision queues. This
                                             						field is a calculated field derived from: Skill_Group_Interval.AvailTime /
                                             						Skill_Group_Interval.LoggedOnTime |
| %Not
                                             						Ready | The
                                             						percentage of time that agents spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. This field applies to all
                                             						precision queues. This
                                             						field is a calculated field, derived from: Skill_Group_Interval.NotReadyTime /
                                             						Skill_Group_Interval.LoggedOnTime |
| %
                                             						Active | The
                                             						percentage of time that agents spent talking on calls in this precision queue
                                             						in relation to LoggedOnTime. This
                                             						field is a calculated field, derived from: (Skill_Group_Interval.TalkInTime +
                                             						Skill_Group_Interval.TalkOutTime + Skill_Group_Interval.TalkOtherTime +
                                             						Skill_Group_Interval.TalkAutoOutTime + Skill_Group_Interval.TalkPreviewTime +
                                             						Skill_Group_Interval.TalkReserveTime) / Skill_Group_Interval.LoggedOnTime |
| % Hold | The
                                             						percentage of time that agents put a call on hold or paused a task in relation
                                             						to LoggedOnTime or the interval, whichever is less. This
                                             						field is a calculated field, derived from: Skill_Group_Interval.HoldTime /
                                             						Skill_Group_Interval.LoggedOnTimeTime |
| %
                                             						Reserved | The percentage of time that agents spent in the Reserved state waiting for a n ICM routed task from this precision queue in relation to LoggedOnTime. This
                                             						field is a calculated field, derived from:
                                             						Skill_Group_Interval.ReservedStateTime / Skill_Group_Interval.LoggedOnTime |
| % Wrap
                                             						Up | The
                                             						percentage of time that agents spent in the Wrap-upstate after incoming or
                                             						outgoing calls to/from this precision queue in relation to LoggedOnTime. This
                                             						field is a calculated field, derived from: (Skill_Group_Interval.WorkReadyTime
                                             						+ Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime |
| %
                                             						Utilization | The
                                             						percentage of Ready time that agents in the precision queue spent talking or
                                             						doing call work during the current five-minute interval. This is the percentage
                                             						of time agents spend working on calls versus the time agents were ready. Derived from: Skill_Group_Real_Time.PercentUtilizationTo5 |
| End of Agent State Times Grouping |
| Answered | The number of routed calls answered by agents associated with this skillgroup during the given interval. CallsAnswered is
                                             incremented in the interval where the call is answered, as opposed to CallsHandled which is incremented in the interval where
                                             the call ends. This is derived from skill_group_interval.CallsAnswered. |
| Abandon ring | For
                                             						voice: the total number of calls that are abandoned while the agent phone is
                                             						ringing. For
                                             						non-voice: the total number of tasks that are abandoned when offered to an
                                             						agent. Derived from: Skill_Group_Interval.AbandonRingCalls |
| Longest Queued | The
                                             						longest a call had to wait before being answered, abandoned, or otherwise
                                             						ended. This includes time in the network queue, local queue, and ringing at the
                                             						agent if applicable. Derived from: Router_Queue_Interval.MaxCallWaitTime |
| MaxQueued | The
                                             						maximum number of calls queued for this precision queue during this interval.
                                             						Calls queued against multiple precision queues are included in the count for
                                             						each precision queue to which the calls are queued. Derived from: Router_Queue_Interval.MaxCallsQueued |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the Agent Precision Queue. Derived from: Precision_Queue.EnterpriseName. |
| Media | The
                                             						enterprise name of the Media Routing Domain associated with the precision
                                             						queue. Media is derived
                                             						from: Media_Routing_Domain.EnterpriseName. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |
| DateTime | The
                                             						date and time of the data for a selected row. Derived
                                             						from: Router_Queue_Interval.DateTime. |
| Queued | Derived
                                             						from: Router_Queue_Interval.QueueCalls. |
| Avg
                                             						Speed of Answer | The
                                             						precision queue average speed of answer in HH:MM:SS(hour, minutes, seconds)
                                             						based on the time spent by callers in the queue and ringing at an agent desktop
                                             						before the task is answered divided by the number of answered tasks. Derived
                                             						from: Skill_Group_Interval.AnswerWaitTime /Skill_Group_Interval.CallsAnswered. |
| Service Level |
| Service Level | Service Level Type used to calculate Service level for the
                                             						interval. Derived from: Router_Queue_Interval.ServiceLevel. |
| Answer | The
                                             						number of calls that are routed to the precision queue or queued to the
                                             						precision queue in the last interval. Derived
                                             						from: Router_Queue_Interval.ServiceLevelCalls |
| Abandon | The
                                             						number of calls that are abandoned within the precision queue service level
                                             						threshold in the last interval. Derived
                                             						from: Router_Queue_Interval.ServiceLevelCallsAband. |
| Completed Tasks |
| Total | The total number of tasks completed by this precision queue in the interval. Derived from:(Router_Queue_Interval.CallsHandled++ Router_Queue_Interval.RedirectNoAnsCalls+ Router_Queue_Interval.CallsAbandQ+
                                             Router_Queue_Interval.RouterError+ Router_Queue_Interval.CallsAbandToAgent) |
| Abandoned | The
                                             						sum of: The number of calls to the call type that are abandoned in the Router queue during the reporting interval. The number of calls associated with this skillgroup that are abandoned at the agent desktop before being answered during the
                                                   reporting interval. Termination_Call_Detail records generated by agent PG with a Call Disposition Flag of 2 are also counted
                                                   for this field. This does not include short calls and the calls that were abandoned in the VRU. Derived
                                             						from: Router_Queue_Interval.CallsAbandQ + Router_Queue_Interval.CallsAbandToAgent. |
| RONA | The count of calls that are redirected with no answer within the Precision Queue service level threshold in the last interval. Derived from: Router_Queue_Interval.RedirectNoAnsCalls |
| Handled | The number of inbound calls for which agents in the precision queue during the interval answered and completed. Derived from: Router_Queue_Interval.CallsHandled. |
| Avg
                                             						Handle Time | The
                                             						average time spent by agents in this precision queue handling a task in the
                                             						interval. This
                                             						field is a calculated field, derived from:
                                             						(Skill_Group_Interval.HandledCallsTime / Skill_Group_Interval.CallsHandled) |
| Avg
                                             						Active Time | The
                                             						Average Active Time in HH:MM:SS (hours, minutes, seconds) for tasks sent to the
                                             						precision queue. Derived
                                             						from: Skill_Group_Interval.HandledCallsTalkTime
                                             						/Skill_Group_Interval.CallsHandled |
| Abandon
                                             						Hold | The
                                             						number of tasks offered to the precision queue that are abandoned while being
                                             						held or paused by the agent. The value is incremented at the time the call
                                             						disconnects. Derived
                                             						from: Skill_Group_Interval.AbandonHoldCalls |
| Tasks Picked | The total number of pick requests successfully routed by the precision queue. |
| Tasks Pulled | The total number of pull requests successfully routed by the precision queue. |
| Picks Failed | Number of pick request resulting in an error. |
| Pulls Failed | Number of pull request resulting in an error. |
| End of Completed Tasks Grouping |
| Transfer In | The number of tasks transferred into the precision queue in the interval. Derived from: Skill_Group_Interval.TransferInCalls |
| Transfer Out | The number of tasks this agent transferred to another agent or precision queue in the interval. This includes Consultative
                                             Calls. The value is updated in the database when the transfer of the call is completed. Derived from: Skill_Group_Interval.TransferredOutCalls + Skill_Group_Interval.NetTransferredOutCalls |
| External Out | For default precision queues: the number of times an agent initiated an outgoing external call in the interval. For routing
                                             precision queues: the number of times an agent initiated a transfer or conference to an external device in the interval. Derived from: Skill_Group_Interval.AgentOutCalls |
| Agent State Time |
| Active
                                             						Time | The
                                             						time in HH:MM:SS (hours, minutes, seconds) that agents in the precision queue
                                             						were in the Active state in the interval. Derived from: Skill_Group_Interval.TalkTime |
| Hold
                                             						Time | The
                                             						total time agents spent in the Hold/Paused state in this precision queue,
                                             						measured in HH:MM:SS (hours, minutes, seconds) format. Includes Incoming Direct
                                             						and Outgoing Internal, although call counts are not shown in this report. Derived from: Skill_Group_Interval.HoldTime |
| Logged
                                             						On Time | The
                                             						total duration in HH:MM:SS (hours, minutes, and seconds) during the period that
                                             						agents were logged into this skill group. Derived from: Skill_Group_Interval.LoggedOnTime |
| %Not
                                             						Active | The
                                             						percentage of time that agents spent in the Not Active or Available state in
                                             						relation to LoggedOnTime. This field applies to all precision queues. This
                                             						field is a calculated field derived from: Skill_Group_Interval.AvailTime /
                                             						Skill_Group_Interval.LoggedOnTime |
| %Not
                                             						Ready | The
                                             						percentage of time that agents spent in the Not Ready state in relation to
                                             						LoggedOnTime or the interval, whichever is less. This field applies to all
                                             						precision queues. This
                                             						field is a calculated field, derived from: Skill_Group_Interval.NotReadyTime /
                                             						Skill_Group_Interval.LoggedOnTime |
| %
                                             						Active | The
                                             						percentage of time that agents spent talking on calls in this precision queue
                                             						in relation to LoggedOnTime. This
                                             						field is a calculated field, derived from: (Skill_Group_Interval.TalkInTime +
                                             						Skill_Group_Interval.TalkOutTime + Skill_Group_Interval.TalkOtherTime +
                                             						Skill_Group_Interval.TalkAutoOutTime + Skill_Group_Interval.TalkPreviewTime +
                                             						Skill_Group_Interval.TalkReserveTime) / Skill_Group_Interval.LoggedOnTime |
| % Hold | The
                                             						percentage of time that agents put a call on hold or paused a task in relation
                                             						to LoggedOnTime or the interval, whichever is less. This
                                             						field is a calculated field, derived from: Skill_Group_Interval.HoldTime /
                                             						Skill_Group_Interval.LoggedOnTimeTime |
| %
                                             						Reserved | The percentage of time that agents spent in the Reserved state waiting for a n ICM routed task from this precision queue in relation to LoggedOnTime. This
                                             						field is a calculated field, derived from:
                                             						Skill_Group_Interval.ReservedStateTime / Skill_Group_Interval.LoggedOnTime |
| % Wrap
                                             						Up | The
                                             						percentage of time that agents spent in the Wrap-upstate after incoming or
                                             						outgoing calls to/from this precision queue in relation to LoggedOnTime. This
                                             						field is a calculated field, derived from: (Skill_Group_Interval.WorkReadyTime
                                             						+ Skill_Group_Interval.WorkNotReadyTime) / Skill_Group_Interval.LoggedOnTime |
| %
                                             						Utilization | The
                                             						percentage of Ready time that agents in the precision queue spent talking or
                                             						doing call work during the current five-minute interval. This is the percentage
                                             						of time agents spend working on calls versus the time agents were ready. Derived from: Skill_Group_Real_Time.PercentUtilizationTo5 |
| End of Agent State Times Grouping |
| Answered | The number of routed calls answered by agents associated with this skillgroup during the given interval. CallsAnswered is
                                             incremented in the interval where the call is answered, as opposed to CallsHandled which is incremented in the interval where
                                             the call ends. This is derived from skill_group_interval.CallsAnswered. |
| Abandon ring | For
                                             						voice: the total number of calls that are abandoned while the agent phone is
                                             						ringing. For
                                             						non-voice: the total number of tasks that are abandoned when offered to an
                                             						agent. Derived from: Skill_Group_Interval.AbandonRingCalls |
| Longest Queued | The
                                             						longest a call had to wait before being answered, abandoned, or otherwise
                                             						ended. This includes time in the network queue, local queue, and ringing at the
                                             						agent if applicable. Derived from: Router_Queue_Interval.MaxCallWaitTime |
| MaxQueued | The
                                             						maximum number of calls queued for this precision queue during this interval.
                                             						Calls queued against multiple precision queues are included in the count for
                                             						each precision queue to which the calls are queued. Derived from: Router_Queue_Interval.MaxCallsQueued |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The
                                             						enterprise name of the Skill Group. Derived
                                             						from:Skill_Group.EnterpriseName. |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| DateTime | The date
                                             						and time when the call type interval data was generated in MM/DD/YYYY (month,
                                             						day, year) and HH:MM:SS (hours, minutes, seconds) format. For
                                             						every interval in the selected time period, there is summary row for each
                                             						selected call type. Derived
                                             						from:Skill_Group_Interval.DateTime. |
| Avg Speed of Answer | Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This is an important measure of service quality because the time can vary, even
                                             over the course of one day, due to call volumes and staff levels. This is
                                             						a calculated field, derived from:Skill_Group_Interval.AnswerWaitTime/
                                             						Skill_Group_Interval.CallsAnswered. |
| Int 1
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between the time set to begin measuring and
                                             						interval 1. The system default interval 1 is 8 seconds. For example: 00:00 -
                                             						00:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(1) and
                                             						Skill_Group_Interval.AbandInterval(1). |
| Int 2
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 1 and interval 2. The
                                             						system default interval 2 is 30 seconds. For example: 00:08 - 00:38. Derived
                                             						from:Skill_Group_Interval.AnsInterval(2) and
                                             						Skill_Group_Interval.AbandInterval(2). |
| Int 3
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 2 and interval 3. The
                                             						system default interval 3 is 60 seconds (1 minute). For example: 00:38 - 01:38. Derived
                                             						from:Skill_Group_Interval.AnsInterval(3) and
                                             						Skill_Group_Interval.AbandInterval(3). |
| Int 4
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 3 and interval 4. The
                                             						system default interval 4 is 90 seconds. For example: 01:38 - 03:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(4) and
                                             						Skill_Group_Interval.AbandInterval(4). |
| Int 5
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 4 and interval 5. The
                                             						system default interval 5 is 120 seconds (2 minutes). For example: 03:08 -
                                             						05:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(5) and
                                             						Skill_Group_Interval.AbandInterval(5). |
| Int 6
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 5 and interval 6. The
                                             						system default interval 6 is 180 seconds (3 minutes). For example: 05:08 -
                                             						08:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(6) and
                                             						Skill_Group_Interval.AbandInterval(6). |
| Int 7
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 6 and interval 7. The
                                             						system default interval 7 is 300 seconds (5 minutes). For example: 08:08 -
                                             						13:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(7) and
                                             						Skill_Group_Interval.AbandInterval(7). |
| Int 8
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 7 and interval 8. The
                                             						system default interval 8 is 600 seconds (10 minutes). For example: 13:08 -
                                             						23:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(8) and
                                             						Skill_Group_Interval.AbandInterval(8). |
| Int 9
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 8 and interval 9. The
                                             						system default interval 9 is 1200 seconds (20 minutes). For example: 23:08 -
                                             						43:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(9) and
                                             						Skill_Group_Interval.AbandInterval(9). |
| > Int
                                             						9 Ans and Aban | The
                                             						number of calls answered/abandoned within the remaining time in the report time
                                             						period measured in minutes and seconds. For example: > 43:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(10) and
                                             						Skill_Group_Interval.AbandInterval(10). |
| Max Queued | The
                                             						maximum number of calls in queue for this call type during this interval. Derived from : Skill_Group_Interval. MaxCallsQueued. |
| Longest Queued | The
                                             						longest time a call had to wait before it was dispositioned (abandoned or
                                             						answered) in this interval. Derived from:Skill_Group_Interval. MaxCallWaitTime. |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The
                                             						enterprise name of the Skill Group. Derived
                                             						from:Skill_Group.EnterpriseName. |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| DateTime | The date
                                             						and time when the call type interval data was generated in MM/DD/YYYY (month,
                                             						day, year) and HH:MM:SS (hours, minutes, seconds) format. For
                                             						every interval in the selected time period, there is summary row for each
                                             						selected call type. Derived
                                             						from:Skill_Group_Interval.DateTime. |
| Avg Speed of Answer | Average Speed of Answer. The average answer wait time from when first queue to skill group or LAA select node was run for
                                             this call to when this call was answered. This is an important measure of service quality because the time can vary, even
                                             over the course of one day, due to call volumes and staff levels. This is
                                             						a calculated field, derived from:Skill_Group_Interval.AnswerWaitTime/
                                             						Skill_Group_Interval.CallsAnswered. |
| Int 1
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between the time set to begin measuring and
                                             						interval 1. The system default interval 1 is 8 seconds. For example: 00:00 -
                                             						00:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(1) and
                                             						Skill_Group_Interval.AbandInterval(1). |
| Int 2
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 1 and interval 2. The
                                             						system default interval 2 is 30 seconds. For example: 00:08 - 00:38. Derived
                                             						from:Skill_Group_Interval.AnsInterval(2) and
                                             						Skill_Group_Interval.AbandInterval(2). |
| Int 3
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 2 and interval 3. The
                                             						system default interval 3 is 60 seconds (1 minute). For example: 00:38 - 01:38. Derived
                                             						from:Skill_Group_Interval.AnsInterval(3) and
                                             						Skill_Group_Interval.AbandInterval(3). |
| Int 4
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 3 and interval 4. The
                                             						system default interval 4 is 90 seconds. For example: 01:38 - 03:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(4) and
                                             						Skill_Group_Interval.AbandInterval(4). |
| Int 5
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 4 and interval 5. The
                                             						system default interval 5 is 120 seconds (2 minutes). For example: 03:08 -
                                             						05:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(5) and
                                             						Skill_Group_Interval.AbandInterval(5). |
| Int 6
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 5 and interval 6. The
                                             						system default interval 6 is 180 seconds (3 minutes). For example: 05:08 -
                                             						08:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(6) and
                                             						Skill_Group_Interval.AbandInterval(6). |
| Int 7
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 6 and interval 7. The
                                             						system default interval 7 is 300 seconds (5 minutes). For example: 08:08 -
                                             						13:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(7) and
                                             						Skill_Group_Interval.AbandInterval(7). |
| Int 8
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 7 and interval 8. The
                                             						system default interval 8 is 600 seconds (10 minutes). For example: 13:08 -
                                             						23:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(8) and
                                             						Skill_Group_Interval.AbandInterval(8). |
| Int 9
                                             						Ans and Aban | The
                                             						number of calls answered/abandoned between interval 8 and interval 9. The
                                             						system default interval 9 is 1200 seconds (20 minutes). For example: 23:08 -
                                             						43:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(9) and
                                             						Skill_Group_Interval.AbandInterval(9). |
| > Int
                                             						9 Ans and Aban | The
                                             						number of calls answered/abandoned within the remaining time in the report time
                                             						period measured in minutes and seconds. For example: > 43:08. Derived
                                             						from:Skill_Group_Interval.AnsInterval(10) and
                                             						Skill_Group_Interval.AbandInterval(10). |
| Max Queued | The
                                             						maximum number of calls in queue for this call type during this interval. Derived from : Skill_Group_Interval. MaxCallsQueued. |
| Longest Queued | The
                                             						longest time a call had to wait before it was dispositioned (abandoned or
                                             						answered) in this interval. Derived from:Skill_Group_Interval. MaxCallWaitTime. |