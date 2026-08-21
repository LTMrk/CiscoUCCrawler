---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-report-7d445cfe04
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_Reporting-User-Guide-12-5/pcce_b_cisco-packaged-contact-center-enterprise_chapter_010100.html
retrieved_at: 2026-08-21T16:58:41.677217+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

Updated: February 4, 2020

Chapter: Real Time Transitional Report Templates

## Chapter: Real Time Transitional Report Templates

# Real Time Transitional Report Templates

## Agents Real
                        	 Time

The Agents Real
                              		  Time Report displays the current activities of agents assigned to a skill.

Query: This
                              		  report data is built from a database query.

Views:

This report has one grid view, Agents Real Time.

Grouping: This report is grouped by Skill Group Name and sorted by Agent Name.

Value List: Skill Groups

Database Schema
                                 			 Tables from which data is retrieved:

Person

Agent

Agent_Real_Time

Agent_Skill_Group_Real_Time

Skill_Group_Real_Time

Service

Skill_Group

Media_Routing_Domain

### Current Fields
                              		  in the Agents Real Time Report Grid View

Current fields are those fields that appear by default in a report generated from the
                              		  stock template. Current fields are listed below in the order (left to right) in
                              		  which they appear by default in the stock template.

Column
                                          						(Field)

Description

Skill Group Name

The
                                          						enterprise skill group's enterprise name.

Derived from: Skill_Group.EnterpriseName

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

Name

The
                                          						login name of the agent.

Derived
                                          						from: Agent.LoginName

Extension

The
                                          						phone extension into which the agent is logged.

Derived
                                          						from: Agent_Real_Time.Extension

Peripheral Number

The
                                          						login ID of the agent.

This
                                          						value is taken directly from the database.

Derived
                                          						from: Agent.PeripheralNumber

Reason

A code
                                          						and text (if configured) from the peripheral that indicates the reason for the
                                          						agent's last state change. If no reason code is defined, this value is 0
                                          						(zero).

This
                                          						field is a calculated field derived from:

```
CASE WHEN Agent_Skill_Group_Reat_Time.ReasonCode = 0
THEN NONE
ELSE (select ReasonText from Reason_Code where ReasonCode = Agent_Skill_Group_Real_Time.Reason Code)
```

State

The
                                          						current state of the agent.

Derived
                                          						from: Agent_Real_Time.AgentState

Time

The
                                          						time spent in the current agent state in HH:MM:SS (hours, minutes, seconds)
                                          						format.

This
                                          						field is a calculated field derived from: DATEDIFF(seconds,
                                          						Agent_Real_Time.DateTimeLastStateChange, Select NowTime From Controller_Time)

Direction

Whether the call is inbound, outbound, or neither of these.

This
                                          						value is taken directly from the database.

Derived from: Agent_Real_Time.Direction

Media

The
                                          						method of communication: phone, chat, or email.

This
                                          						value is taken directly from the database.

Derived from: Media_Routing_Domain

Report
                                 			 Summary: This report has a report summary for all data.

## Agent Team Real
                        	 Time

Run this report to show the agent status in real time.

Views:

This report has one grid view, Agent Team Real Time.

Current fields are those
                              		  fields that appear by default in a report generated from the stock template.

Current fields are
                              		  listed below in the order (left to right) in which they appear by default in
                              		  the stock template.

Column (Field)

Description

Agent Team Name

The Enterprise Name of the Agent Team.

Derived from: Agent_Team.EnterpriseName.

Agent Name

The last and first name of the agent.

Derived from: Person.LastName ", " Person.FirstName.

Precision Queue / Skill Group

Precision Queue or Skill Group or Not Applicable.

Precision Queue is derived from: Agent_Team.EnterpriseName.

The precision route associated with the task on which the agent is currently working. If the agent is not involved in any
                                          task in the Media Routing Domain, this field shows Not Applicable. Because an agent can log in to multiple precision routes,
                                          this field is not filled until the agent is assigned a task.

Skill Group Name is derived from: Skill_Group.EnterpriseName.

The skill group associated with the task on which the agent is currently working. If the agent is not involved in any task
                                          in the Media Routing Domain, this field shows Not Applicable. Because an agent can be logged in to multiple skill groups,
                                          this field is not filled until the agent is assigned a task.

State

The current state of the agent.

Derived from: Agent_Real_Time.AgentState.

Direction

The direction of the call that the agent is currently working on:

NULL= None

0 = None

1 = In

2 =Out

3= Other

Derived from: Agent_Real_Time.Direction.

Destination

The type of outbound task on which the agent is currently working.

Derived from: Agent_Real_Time.Destination.

Reason

A code received from the peripheral that indicates the reason for the agent's last state change. If no reason code is defined,
                                          this value is 0 (zero).

Derived from: Agent_Real_Time.ReasonCode.

Name

The login name for the Agent.Derived from: Person.LoginName

Extenstion

The phone extension into which the agent is logged.

Derived from: Agent_Real_Time.Extension

Pheripheral Number

The login ID of the agent. This value is taken directly from the database.

Derived from: Agent.PeripheralNumber

Time

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, Select NowTime From
                                          Controller_Time)

Media

The enterprise name of the Media Routing Domain associated with the Precision Queue or Skill Group Name.

Media is derived from: Media_Routing_Domain.EnterpriseName.

Report Summary: There is a summary row for Agent Team, a summary row for each Supervisor and a report summary for all data. For more information,
                              see Report Summary Rows .

## Call Type Real
                        	 Time

Views:

This report has the following grid views:

Call Type Real Time

Call Type Today Real Time

Select the view you want to see from the report drop-down list located on the top left corner.

Query: This report data is built from a database query.

Call_Type

Call_Type_Real_Time

Grouping: This template is sorted by Call Type Name.

### Call Type Real
                           	 Time View

The Call Type Real Time Report
                                 		  displays information about how call types are handled during the current
                                 		  interval.

Value List: CallTypeId

#### Current Fields
                                 		  in the Call Type Real Time Report Grid View

Current fields are those fields that appear by default in a report generated from the
                                 		  stock template. Current fields are listed below in the order (left to right) in
                                 		  which they appear by default in the stock template.

Column
                                             						(Field)

Description

Call
                                             						Type Name

The
                                             						enterprise name for the call type.

Derived
                                             						from: Call_Type.EnterpriseName

Calls
                                             						Waiting

The
                                             						number of tasks currently in the queue.

Derived
                                             						from: Call_Type_Real_Time.RouterCallsQNow

Longest Queued

The
                                             						time spent in queue for the longest currently queued task, measured in HH:MM:SS
                                             						(hours, minutes, seconds) format.

This
                                             						field is a calculated field, derived from: DATEDIFF(ss,
                                             						Call_Type_Real_Time.RouterLongestCallQ, (SELECT NowTime from Controller_Time))

Avg
                                             						Speed Of Answer

The Average
                                             						Speed of Answer during the rolling five-minute interval. The total Answer Time
                                             						for all tasks of the call type divided by the number of tasks of this type
                                             						answered during the current 5-minute interval.

This is
                                             						a calculated field, derived from: (Call_Type_Real_Time.AnswerWaitTimeTo5 /
                                             						Call_Type_Real_Time.CallsAnsweredTo5)

Abandon

The
                                             						number of tasks abandoned at the IVR during the rolling five-minute interval,
                                             						while offered to the agent and on route to the agent.

Derived
                                             						from: Call_Type_Real_Time.TotalCallsAbandTo5

Avg Abandon
                                             						Time

The
                                             						average time of abandoned calls for this call type during the rolling five-minute interval, measured in HH:MM:SS (hours,
                                             minutes, seconds) format.

This field is
                                             						a calculated field, derived from: Call_Type_Real_Time.CallDelayAbandTimeTo5 /
                                             						Call_Type_Real_Time.TotalCallsAbandTo5

Handled

The
                                             						number of calls of this call type handled for the call type ending during the
                                             						rolling five-minute interval.

Derived
                                             						from: Call_Type_Real_Time.CallsHandledTo5

Avg
                                             						Handle Time

The average time taken during the rolling five-minute interval to handle a task in HH:MM:SS (hours, minutes, seconds) format.

This field is calculated based on: Call_Type_Real_Time.HandleTimeTo5 / Call_Type_Real_Time.CallsHandledTo5

Flow In

The number of calls that are Redirected On No Answer in the rolling five-minute interval. This does not include calls rerouted
                                             using the router requery feature.

Derived
                                             						from: Call_Type_Real_Time.CallsRONATo5

Flow Out

The number of tasks that are run as a Requalify or Call Type node and flowed to another call type during the rolling five-minute
                                             interval.

Derived
                                             						from: Call_Type_Real_Time.OverflowOutTo5

Active

The number of calls active for this call type offered during the rolling five-minute interval.

This field is derived from: CallsAtAgentNow+CallsAtVRUNow

Report
                                    			 Summary: This report has a report summary for all data.

### Call Type Today Real Time View

The Call Type Today Real Time report displays the information for each call type at the start of the day.

Value List: Call Types

#### Current Fields in the Call Type Today Real Time Report Grid View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed
                                 below in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Call Type Name

The enterprise name for the call type.

Derived from: Call_Type.EnterpriseName

Calls Waiting

The number of tasks currently in the queue.

Derived from: Call_Type_Real_Time.RouterCallsQNow

Longest Queued

The time spent in queue for the longest currently queued task, measured in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field, derived from: DATEDIFF(ss, Call_Type_Real_Time.RouterLongestCallQ, (SELECT NowTime from
                                             Controller_Time))

Avg Speed Of Answer

The Average Speed of Answer during the rolling five-minute interval. The total Answer Time for all tasks of the call type
                                             divided by the number of tasks of this type answered during the current 5-minute interval.

This is a calculated field, derived from: (Call_Type_Real_Time.AnswerWaitTimeTo5 / Call_Type_Real_Time.CallsAnsweredTo5)

Abandon

The number of tasks abandoned at the IVR during the rolling five-minute interval, while offered to the agent and on route
                                             to the agent.

Derived from: Call_Type_Real_Time.TotalCallsAbandTo5

Avg Abandon Time

The average time of abandoned calls for this call type during the rolling five-minute interval, measured in HH:MM:SS (hours,
                                             minutes, seconds) format.

This field is a calculated field, derived from: Call_Type_Real_Time.CallDelayAbandTimeTo5 / Call_Type_Real_Time.TotalCallsAbandTo5

Handled

The number of calls of this call type handled for the call type ending during the rolling five-minute interval.

Derived from: Call_Type_Real_Time.CallsHandledTo5

Avg Handled Time

The average time in HH:MM:SS (hours, minutes, seconds) it has taken during the rolling five-minute interval to handle a task.

This field is a calculated field, derived from: Call_Type_Real_Time.HandleCallsTimeTo5 / Call_Type_Real_Time.CallsHandledTo5

Flow In

The number of calls that have been Redirected On No Answer in the rolling five-minute interval. This number does not include
                                             calls rerouted using the router requery feature.

Derived from: Call_Type_Real_Time.CallsRONATo5

Flow Out

The number of tasks that run a Requalify or Call Type node and flowed to another call type during the rolling five-minute
                                             interval.

Derived from: Call_Type_Real_Time.OverflowOutTo5

Active Calls

The number of calls of this call type offered during the rolling five-minute interval.

This field is a calculated field, derived from: CallsAtAgentNow + CallsAtVRUNow

Report Summary: This report has a report summary for all data.

## Skill Group Not Ready

### Skill Group Not
                           	 Ready Detail Real Time

The Skill Group
                                 		  Not Ready Detail Real Time Report displays the number of agents in Not Ready
                                 		  state for one or more specified skill groups.

Query: Anonymous Block

Views:

This report has one grid view, Skill Group Not Ready Detail Real Time.

Grouping: This report is grouped and sorted by Skill Target
                                 		  ID.

Value List: Skill Groups

Skill_Group

Skill_Group_Real_Time

Agent_Skill_Group_Real_Time

#### Skill Group
                                 		  Not Ready Detail Real Time Report

Current fields are those fields that appear by default in a report generated from the
                                 		  stock template. Current fields are listed below in the order (left to right) in
                                 		  which they appear by default in the stock template.

Column
                                             						(Field)

Description

Skill Group Name

The
                                             						precision queue or skill group associated with the task on which the agent is
                                             						currently working. If the agent is not involved in any task in the media
                                             						routing domain, this field shows Not Applicable. Because an agent can be logged
                                             						into multiple skill groups, this field is not filled until the agent is
                                             						assigned a task.

Derived
                                             						from: Skill_Group.EnterpriseName

Calls
                                             						Waiting

The
                                             						number of tasks currently in the queue.

Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow '+
                                             						Skill_Group_Real_Time.CallsQueuedNow'

Agents
                                             						Logged On

The
                                             						number of agents that are currently logged on to the skill group. This count is
                                             						updated each time an agent logs on and each time an agent logs off.

Derived
                                             						from: Skill_Group_Real_Time.LoggedOn

Not
                                             						Ready Agents

The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged on but are neither involved in any call
                                             						handling activity nor available to handle a call.

Derived
                                             						from: Skill_Group_Real_Time.NotReady

Reason
                                             						code RC0 - RC9

A code
                                             						received from the peripheral that indicates the reason for the last state
                                             						change for the agents. If no reason code is defined, this value is zero (0).

This is
                                             						directly derived from: Agent_Skill_Group_Real_Time

Report
                                    			 Summary: This report has a report summary for all data.

### Skill Group Not Ready Real Time

The Skill Group Not Ready Real Time Report identifies the agents who are in the Not Ready state for one or more specified
                                 skill groups.

Query: This report data is built from a database query.

Views: This report has one grid view, Skill Group Not Ready Real Time and one chart view, Skill Group Not Ready Graphical Real Time.

Grouping: This report is grouped and sorted by Skill Group Name.

Value List: Skill Groups

Database Schema Tables from which data is retrieved:

Person

Agent

Agent_Real_Time

Agent_Skill_Group_Real_Time

Service

Skill_Group

Media_Routing_Domain

Skill_Group_Real_Time

#### Current Fields in the Skill Group Not Ready Time Report Grid View

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed
                                 below in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Skill Group Name

The enterprise skill group's enterprise name.

Derived from: Skill_Group.EnterpriseName

Agent Name

The last name and the first name of the agent.

Derived from: Person.LastName "," Person.FirstName

Name

The agent's login name.

Derived from: Person.LoginName

Peripheral Number

The agent's login ID.

Derived from: Agent.PeripheralNumber

Reason

A code received from the peripheral that indicates the reason for the agent's last state change. If no reason code is defined,
                                             this value is 0 (zero).

Derived from:

```
CASE WHEN Agent_Real_Time.ReasonCode = 0
THEN 'NONE'
ELSE (select ReasonText from Reason_Code where ReasonCode =Agent_Real_Time.ReasonCode) END
```

Duration

The length of time since the agent's last change, measured in HH:MM:SS (hours, minutes, seconds) format.

This field  is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange , Select Nowtime
                                             From Controller_Time)

Report Summary: This report has a report summary for all data.

## Skill Group Status

### Skill Group Agent Status Real Time

The Skill Group Agent Status Real Time Report displays the agent status in real time.

Query: This report data is built from a database query.

Views: This report has one grid view, Skill Group Agent Status Real Time.

Grouping: This report is sorted by Skill Group Name.

Value List: Skill Groups

Person

Agent

Agent_Real_Time

Agent_Skill_Group_Real_Time

Service

Skill_Group

Skill_Group_Real_Time

Media_Routing_Domain

#### Current Fields in the Skill Group Real Time Agent Status

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed
                                 below in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Skill Group

The enterprise skill group's enterprise name.

Derived from: Skill_Group.EnterpriseName

Agent Name

The last name and first name of the agent.

Derived from: Person.LastName "," Person.FirstName

State

The current state of the agent.

Derived from: Agent_Real_Time.AgentState

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field, derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange , Select Nowtime
                                             From Controller_Time)

Report Summary: This report has a report summary for all data.

### Skill Group Real Time Status

The Skill Group Real Time Status Report displays call in service level, calls waiting, oldest call waiting, average speed
                                 of answer, handled calls, average handled time, abandoned calls and logged-on time for specified skill group(s).

Query: This report data is built from a database query.

Views:

This report has one grid view, Skill Group Real Time Status and the following chart views:

Calls Waiting Graph

Oldest Call Time Graph

Select the view you want to see from the report drop-down list located on the top left corner.

Grouping: This report is grouped and sorted by Skill Group Name.

Value List: Skill Groups

Database Schema Tables from which data is retrieved:

Skill_Group_Real_Time

Skill_Group

Media_Routing_Domain

#### Current Fields in the Skill Group Real Time Status

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed below
                                 in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Skill Group Name

The enterprise name for the skill group.

Derived from: Skill_Group.Enterprise

Calls Waiting

The number of split or skill ACD calls currently waiting to be answered. This includes calls that are in queue and calls that
                                             are ringing at an agent voice terminal. It does not include direct agent calls.

Derived from: Skill_Group_Real_Time.RouterCallsQNow

Longest Queued

The time spent in queue for the longest currently queued task, measured in HH:MM:SS (hours, minutes, seconds) format.

This is a calculated field, calculated by subtracting the time the task entered the queue from the current time and derived
                                             from: DATEDIFF(ss, Skill_Group_Real_Time.RouterLongestCallQ, (SELECT NowTime from Controller_Time)),0)

Avg
                                             						Speed Of Answer

The average time calls waited in queue or ringing before an agent answered. Average Speed of Answer during the rolling five-minute
                                             interval.

This is a calculated field, derived from: (Skill_Group_Real_Time.AnswerWaitTimeTo5 / Skill_Group_Real_Time.CallsAnsweredTo5)

Handled

The number of calls of this call type handled for the call type ending during the rolling five minute-interval.

Derived from: Skill_Group_Real_Time.CallsHandledTo5

Avg Handle Time

The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds).

This is a calculated field, derived from: Skill_Group_Real_Time.Handle Time / Skill_Group_Real_Time.CallsHandled

Abandon

The number of calls that are abandoned in the router queue during the interval for a skill group.

Derived from: Skill_Group_Real_Time.RouterCalls AbandQTo5

Logged On

The number of agents that are currently logged on to the skill group. This count is updated each time an agent logs on and
                                             each time an agent logs off.

Derived from: Skill_Group_Real_Time.LoggedOn

Report Summary: This report has a report summary for all data.

### Skill Group Status Graphical Real Time

The Skill Group Status Graphical Real Time Report displays the number of agents in each status for one or more specified skill
                                 groups.

Query: This report data is built from a database query.

Views: This report has a chart view, Skill Group Status Graphical Real Time.

Value List: Skill Groups

Person

Agent_Real_Time

Agent

Skill_Group

Service

Media_Routing_Domain

Skill_Group_Real_Time

#### Skill Group Status Graphical RealTime

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed
                                 below in the order (left to right) in which they appear by default in the stock template.

Field

Description

Logged Out

The agent is logged off.

Logged On

The agent is logged on.

Not Ready

The agent is not available to be assigned a task. If an agent is Not Ready in one skill group, the agent is Not Ready in
                                             all skill groups within the same Media Routing Domain.

Ready

The agent has put himself in the Ready state using his agent desktop tool.

Talking

The agent is working on a task or a call in this skill group.

Work Not Ready

The agent is performing wrap-up work for a call in this skill group. The agent enters Not Ready state when wrap up is complete.

Work Ready

The agent is performing wrap-up work for a call or task in this skill group.

If the agent is handling a voice call, the agent enters Not Active state when wrap up is complete.

If the agent is handling a non-voice task, the agent might enter Not Active or Not Ready state when wrap up is complete.

Busy Other

The agent is Active, Work Ready, Reserved, or on Hold/Paused in another skill group.

Reserved

The agent has been offered a call or task associated with the skill group.

For voice calls, agents are Reserved when their phones are ringing.

Unknown

The agent state is unknown.

Hold

For agents handling Outbound Option calls, the Hold state indicates that the agent has been reserved for a call because the
                                             Outbound Dialer puts the agent on hold while connecting the call.

Active

The agent is talking on or handling calls.

An agent can be active in only one skill group at a time. While active in one skill group, the agent is considered to be
                                             in the Busy Other state for the other skill groups.

## Skill Status

### Skill Status Agent
                           	 Real Time

Run this report to
                                 		  show the agent status in real time.

Query: This
                                 		  report data is built from a database query.

Views:

This report has one grid view,  Skill Status Agent Real Time.

Grouping: This template is grouped by Skill Group Name and sorted by Date Time.

Value List: Skill Groups

Person

Agent

Agent_Real_Time

Agent_Skill_Group_Real_Time

Service

Skill_Group

Skill_Group_Real_Time

Media_Routing_Domain

#### Current Fields
                                 		  in the Skill Group Real Time Agent Status

Current fields are those fields that appear by default in a report generated from the
                                 		  stock template. Current fields are listed below in the order (left to right) in
                                 		  which they appear by default in the stock template.

Column
                                             						(Field)

Description

Skill Group Name

The enterprise skill group's enterprise name.

Derived
                                             						from: Skill_Group.EnterpriseName

Agent
                                             						Name

The last
                                             						and first name of the agent.

Derived
                                             						from: Person.LastName "," Person.FirstName

Name

Value
                                             						taken directly from the database.

Derived
                                             						from: Person.LoginName

Reason

A code
                                             						received from the peripheral that indicates the reason for the agents last
                                             						state change. If not defined, this places none.

Derived
                                             						from:

```
CASE WHEN Agent_Skill_Group_Real_Time.ReasonCode = 0
THEN 'NONE'
ELSE (select ReasonText from Reason_Code where ReasonCode = Agent_Skill_Group­_Real_Time.ReasonCode) END
```

Agent
                                             						State

The
                                             						current state of the agent.

Derived
                                             						from: Agent_Skill_Group_Real_Time.AgentState

Duration

The time
                                             						spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This is
                                             						a calculated field, derived from: DATEDIFF(seconds,
                                             						Agent_Skill_Group_Real_Time.DateTimeLastStateChange , Select Nowtime From
                                             						Controller_Time)

Report
                                    			 Summary: This report has a report summary for all data.

### Skill Status Real Time

Run this report to see calls waiting and Answer Wait Time for specified skill groups.

Query: This report data is built from a database query.

Views:

This report has one grid view, Skill Status Real Time.

Grouping: This template is grouped by Skill Group Name and sorted by Date Time.

Value List: Skill Groups

Database Schema Tables from which data is retrieved:

Skill_Group_Real_Time

Skill_Group

Media_Routing_Domain

#### Current Fields in the Skill Group Real Time Status

Current fields are those fields that appear by default in a report generated from the stock template. Current fields are listed below
                                 in the order (left to right) in which they appear by default in the stock template.

Column (Field)

Description

Skill Group Name

The enterprise skill group's enterprise name.

Derived from: Skill_Group.EnterpriseName

Calls Waiting

The number of split or skill ACD calls currently waiting to be answered. This includes calls that are in queue and calls that
                                             are ringing at an agent voice terminal. It does not include direct agent calls.

Derived from: Skill_Group_Real_Time.TotalQueuedNow

Longest Queued

The time spent in queue for the longest currently queued task, measured in HH:MM:SS (hours, minutes, seconds) format.

This is a calculated field, calculated by subtracting the time the task entered the queue from the current time and derived
                                             from: DATEDIFF(ss, Skill_Group_Real_Time.RouterLongestCallQ, (SELECT NowTime from Controller_Time)),0)

Report Summary: This report has a report summary for all data.

| Column
                                          						(Field) | Description |
|---|---|
| Skill Group Name | The
                                          						enterprise skill group's enterprise name. Derived from: Skill_Group.EnterpriseName |
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| Name | The
                                          						login name of the agent. Derived
                                          						from: Agent.LoginName |
| Extension | The
                                          						phone extension into which the agent is logged. Derived
                                          						from: Agent_Real_Time.Extension |
| Peripheral Number | The
                                          						login ID of the agent. This
                                          						value is taken directly from the database. Derived
                                          						from: Agent.PeripheralNumber |
| Reason | A code
                                          						and text (if configured) from the peripheral that indicates the reason for the
                                          						agent's last state change. If no reason code is defined, this value is 0
                                          						(zero). This
                                          						field is a calculated field derived from: CASE WHEN Agent_Skill_Group_Reat_Time.ReasonCode = 0
THEN NONE
ELSE (select ReasonText from Reason_Code where ReasonCode = Agent_Skill_Group_Real_Time.Reason Code) |
| State | The
                                          						current state of the agent. Derived
                                          						from: Agent_Real_Time.AgentState |
| Time | The
                                          						time spent in the current agent state in HH:MM:SS (hours, minutes, seconds)
                                          						format. This
                                          						field is a calculated field derived from: DATEDIFF(seconds,
                                          						Agent_Real_Time.DateTimeLastStateChange, Select NowTime From Controller_Time) |
| Direction | Whether the call is inbound, outbound, or neither of these. This
                                          						value is taken directly from the database. Derived from: Agent_Real_Time.Direction |
| Media | The
                                          						method of communication: phone, chat, or email. This
                                          						value is taken directly from the database. Derived from: Media_Routing_Domain |

| Column (Field) | Description |
|---|---|
| Agent Team Name | The Enterprise Name of the Agent Team. Derived from: Agent_Team.EnterpriseName. |
| Agent Name | The last and first name of the agent. Derived from: Person.LastName ", " Person.FirstName. |
| Precision Queue / Skill Group | Precision Queue or Skill Group or Not Applicable. Precision Queue is derived from: Agent_Team.EnterpriseName. The precision route associated with the task on which the agent is currently working. If the agent is not involved in any
                                          task in the Media Routing Domain, this field shows Not Applicable. Because an agent can log in to multiple precision routes,
                                          this field is not filled until the agent is assigned a task. Skill Group Name is derived from: Skill_Group.EnterpriseName. The skill group associated with the task on which the agent is currently working. If the agent is not involved in any task
                                          in the Media Routing Domain, this field shows Not Applicable. Because an agent can be logged in to multiple skill groups,
                                          this field is not filled until the agent is assigned a task. |
| State | The current state of the agent. Derived from: Agent_Real_Time.AgentState. |
| Direction | The direction of the call that the agent is currently working on: NULL= None 0 = None 1 = In 2 =Out 3= Other Derived from: Agent_Real_Time.Direction. |
| Destination | The type of outbound task on which the agent is currently working. Derived from: Agent_Real_Time.Destination. |
| Reason | A code received from the peripheral that indicates the reason for the agent's last state change. If no reason code is defined,
                                          this value is 0 (zero). Derived from: Agent_Real_Time.ReasonCode. |
| Name | The login name for the Agent.Derived from: Person.LoginName |
| Extenstion | The phone extension into which the agent is logged. Derived from: Agent_Real_Time.Extension |
| Pheripheral Number | The login ID of the agent. This value is taken directly from the database. Derived from: Agent.PeripheralNumber |
| Time | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, Select NowTime From
                                          Controller_Time) |
| Media | The enterprise name of the Media Routing Domain associated with the Precision Queue or Skill Group Name. Media is derived from: Media_Routing_Domain.EnterpriseName. |

| Column
                                             						(Field) | Description |
|---|---|
| Call
                                             						Type Name | The
                                             						enterprise name for the call type. Derived
                                             						from: Call_Type.EnterpriseName |
| Calls
                                             						Waiting | The
                                             						number of tasks currently in the queue. Derived
                                             						from: Call_Type_Real_Time.RouterCallsQNow |
| Longest Queued | The
                                             						time spent in queue for the longest currently queued task, measured in HH:MM:SS
                                             						(hours, minutes, seconds) format. This
                                             						field is a calculated field, derived from: DATEDIFF(ss,
                                             						Call_Type_Real_Time.RouterLongestCallQ, (SELECT NowTime from Controller_Time)) |
| Avg
                                             						Speed Of Answer | The Average
                                             						Speed of Answer during the rolling five-minute interval. The total Answer Time
                                             						for all tasks of the call type divided by the number of tasks of this type
                                             						answered during the current 5-minute interval. This is
                                             						a calculated field, derived from: (Call_Type_Real_Time.AnswerWaitTimeTo5 /
                                             						Call_Type_Real_Time.CallsAnsweredTo5) |
| Abandon | The
                                             						number of tasks abandoned at the IVR during the rolling five-minute interval,
                                             						while offered to the agent and on route to the agent. Derived
                                             						from: Call_Type_Real_Time.TotalCallsAbandTo5 |
| Avg Abandon
                                             						Time | The
                                             						average time of abandoned calls for this call type during the rolling five-minute interval, measured in HH:MM:SS (hours,
                                             minutes, seconds) format. This field is
                                             						a calculated field, derived from: Call_Type_Real_Time.CallDelayAbandTimeTo5 /
                                             						Call_Type_Real_Time.TotalCallsAbandTo5 |
| Handled | The
                                             						number of calls of this call type handled for the call type ending during the
                                             						rolling five-minute interval. Derived
                                             						from: Call_Type_Real_Time.CallsHandledTo5 |
| Avg
                                             						Handle Time | The average time taken during the rolling five-minute interval to handle a task in HH:MM:SS (hours, minutes, seconds) format. This field is calculated based on: Call_Type_Real_Time.HandleTimeTo5 / Call_Type_Real_Time.CallsHandledTo5 |
| Flow In | The number of calls that are Redirected On No Answer in the rolling five-minute interval. This does not include calls rerouted
                                             using the router requery feature. Derived
                                             						from: Call_Type_Real_Time.CallsRONATo5 |
| Flow Out | The number of tasks that are run as a Requalify or Call Type node and flowed to another call type during the rolling five-minute
                                             interval. Derived
                                             						from: Call_Type_Real_Time.OverflowOutTo5 |
| Active | The number of calls active for this call type offered during the rolling five-minute interval. This field is derived from: CallsAtAgentNow+CallsAtVRUNow |

| Column (Field) | Description |
|---|---|
| Call Type Name | The enterprise name for the call type. Derived from: Call_Type.EnterpriseName |
| Calls Waiting | The number of tasks currently in the queue. Derived from: Call_Type_Real_Time.RouterCallsQNow |
| Longest Queued | The time spent in queue for the longest currently queued task, measured in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field, derived from: DATEDIFF(ss, Call_Type_Real_Time.RouterLongestCallQ, (SELECT NowTime from
                                             Controller_Time)) |
| Avg Speed Of Answer | The Average Speed of Answer during the rolling five-minute interval. The total Answer Time for all tasks of the call type
                                             divided by the number of tasks of this type answered during the current 5-minute interval. This is a calculated field, derived from: (Call_Type_Real_Time.AnswerWaitTimeTo5 / Call_Type_Real_Time.CallsAnsweredTo5) |
| Abandon | The number of tasks abandoned at the IVR during the rolling five-minute interval, while offered to the agent and on route
                                             to the agent. Derived from: Call_Type_Real_Time.TotalCallsAbandTo5 |
| Avg Abandon Time | The average time of abandoned calls for this call type during the rolling five-minute interval, measured in HH:MM:SS (hours,
                                             minutes, seconds) format. This field is a calculated field, derived from: Call_Type_Real_Time.CallDelayAbandTimeTo5 / Call_Type_Real_Time.TotalCallsAbandTo5 |
| Handled | The number of calls of this call type handled for the call type ending during the rolling five-minute interval. Derived from: Call_Type_Real_Time.CallsHandledTo5 |
| Avg Handled Time | The average time in HH:MM:SS (hours, minutes, seconds) it has taken during the rolling five-minute interval to handle a task. This field is a calculated field, derived from: Call_Type_Real_Time.HandleCallsTimeTo5 / Call_Type_Real_Time.CallsHandledTo5 |
| Flow In | The number of calls that have been Redirected On No Answer in the rolling five-minute interval. This number does not include
                                             calls rerouted using the router requery feature. Derived from: Call_Type_Real_Time.CallsRONATo5 |
| Flow Out | The number of tasks that run a Requalify or Call Type node and flowed to another call type during the rolling five-minute
                                             interval. Derived from: Call_Type_Real_Time.OverflowOutTo5 |
| Active Calls | The number of calls of this call type offered during the rolling five-minute interval. This field is a calculated field, derived from: CallsAtAgentNow + CallsAtVRUNow |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group Name | The
                                             						precision queue or skill group associated with the task on which the agent is
                                             						currently working. If the agent is not involved in any task in the media
                                             						routing domain, this field shows Not Applicable. Because an agent can be logged
                                             						into multiple skill groups, this field is not filled until the agent is
                                             						assigned a task. Derived
                                             						from: Skill_Group.EnterpriseName |
| Calls
                                             						Waiting | The
                                             						number of tasks currently in the queue. Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow '+
                                             						Skill_Group_Real_Time.CallsQueuedNow' |
| Agents
                                             						Logged On | The
                                             						number of agents that are currently logged on to the skill group. This count is
                                             						updated each time an agent logs on and each time an agent logs off. Derived
                                             						from: Skill_Group_Real_Time.LoggedOn |
| Not
                                             						Ready Agents | The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged on but are neither involved in any call
                                             						handling activity nor available to handle a call. Derived
                                             						from: Skill_Group_Real_Time.NotReady |
| Reason
                                             						code RC0 - RC9 | A code
                                             						received from the peripheral that indicates the reason for the last state
                                             						change for the agents. If no reason code is defined, this value is zero (0). This is
                                             						directly derived from: Agent_Skill_Group_Real_Time |

| Column (Field) | Description |
|---|---|
| Skill Group Name | The enterprise skill group's enterprise name. Derived from: Skill_Group.EnterpriseName |
| Agent Name | The last name and the first name of the agent. Derived from: Person.LastName "," Person.FirstName |
| Name | The agent's login name. Derived from: Person.LoginName |
| Peripheral Number | The agent's login ID. Derived from: Agent.PeripheralNumber |
| Reason | A code received from the peripheral that indicates the reason for the agent's last state change. If no reason code is defined,
                                             this value is 0 (zero). Derived from: CASE WHEN Agent_Real_Time.ReasonCode = 0
THEN 'NONE'
ELSE (select ReasonText from Reason_Code where ReasonCode =Agent_Real_Time.ReasonCode) END |
| Duration | The length of time since the agent's last change, measured in HH:MM:SS (hours, minutes, seconds) format. This field  is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange , Select Nowtime
                                             From Controller_Time) |

| Column (Field) | Description |
|---|---|
| Skill Group | The enterprise skill group's enterprise name. Derived from: Skill_Group.EnterpriseName |
| Agent Name | The last name and first name of the agent. Derived from: Person.LastName "," Person.FirstName |
| State | The current state of the agent. Derived from: Agent_Real_Time.AgentState |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field, derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange , Select Nowtime
                                             From Controller_Time) |

| Column (Field) | Description |
|---|---|
| Skill Group Name | The enterprise name for the skill group. Derived from: Skill_Group.Enterprise |
| Calls Waiting | The number of split or skill ACD calls currently waiting to be answered. This includes calls that are in queue and calls that
                                             are ringing at an agent voice terminal. It does not include direct agent calls. Derived from: Skill_Group_Real_Time.RouterCallsQNow |
| Longest Queued | The time spent in queue for the longest currently queued task, measured in HH:MM:SS (hours, minutes, seconds) format. This is a calculated field, calculated by subtracting the time the task entered the queue from the current time and derived
                                             from: DATEDIFF(ss, Skill_Group_Real_Time.RouterLongestCallQ, (SELECT NowTime from Controller_Time)),0) |
| Avg
                                             						Speed Of Answer | The average time calls waited in queue or ringing before an agent answered. Average Speed of Answer during the rolling five-minute
                                             interval. This is a calculated field, derived from: (Skill_Group_Real_Time.AnswerWaitTimeTo5 / Skill_Group_Real_Time.CallsAnsweredTo5) |
| Handled | The number of calls of this call type handled for the call type ending during the rolling five minute-interval. Derived from: Skill_Group_Real_Time.CallsHandledTo5 |
| Avg Handle Time | The average time spent by the agent in handling a task in the interval, measured in HH:MM:SS (hours, minutes, seconds). This is a calculated field, derived from: Skill_Group_Real_Time.Handle Time / Skill_Group_Real_Time.CallsHandled |
| Abandon | The number of calls that are abandoned in the router queue during the interval for a skill group. Derived from: Skill_Group_Real_Time.RouterCalls AbandQTo5 |
| Logged On | The number of agents that are currently logged on to the skill group. This count is updated each time an agent logs on and
                                             each time an agent logs off. Derived from: Skill_Group_Real_Time.LoggedOn |

| Field | Description |
|---|---|
| Logged Out | The agent is logged off. |
| Logged On | The agent is logged on. |
| Not Ready | The agent is not available to be assigned a task. If an agent is Not Ready in one skill group, the agent is Not Ready in
                                             all skill groups within the same Media Routing Domain. |
| Ready | The agent has put himself in the Ready state using his agent desktop tool. |
| Talking | The agent is working on a task or a call in this skill group. |
| Work Not Ready | The agent is performing wrap-up work for a call in this skill group. The agent enters Not Ready state when wrap up is complete. |
| Work Ready | The agent is performing wrap-up work for a call or task in this skill group. If the agent is handling a voice call, the agent enters Not Active state when wrap up is complete. If the agent is handling a non-voice task, the agent might enter Not Active or Not Ready state when wrap up is complete. |
| Busy Other | The agent is Active, Work Ready, Reserved, or on Hold/Paused in another skill group. |
| Reserved | The agent has been offered a call or task associated with the skill group. For voice calls, agents are Reserved when their phones are ringing. |
| Unknown | The agent state is unknown. |
| Hold | For agents handling Outbound Option calls, the Hold state indicates that the agent has been reserved for a call because the
                                             Outbound Dialer puts the agent on hold while connecting the call. |
| Active | The agent is talking on or handling calls. An agent can be active in only one skill group at a time. While active in one skill group, the agent is considered to be
                                             in the Busy Other state for the other skill groups. |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group Name | The enterprise skill group's enterprise name. Derived
                                             						from: Skill_Group.EnterpriseName |
| Agent
                                             						Name | The last
                                             						and first name of the agent. Derived
                                             						from: Person.LastName "," Person.FirstName |
| Name | Value
                                             						taken directly from the database. Derived
                                             						from: Person.LoginName |
| Reason | A code
                                             						received from the peripheral that indicates the reason for the agents last
                                             						state change. If not defined, this places none. Derived
                                             						from: CASE WHEN Agent_Skill_Group_Real_Time.ReasonCode = 0
THEN 'NONE'
ELSE (select ReasonText from Reason_Code where ReasonCode = Agent_Skill_Group­_Real_Time.ReasonCode) END |
| Agent
                                             						State | The
                                             						current state of the agent. Derived
                                             						from: Agent_Skill_Group_Real_Time.AgentState |
| Duration | The time
                                             						spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This is
                                             						a calculated field, derived from: DATEDIFF(seconds,
                                             						Agent_Skill_Group_Real_Time.DateTimeLastStateChange , Select Nowtime From
                                             						Controller_Time) |

| Column (Field) | Description |
|---|---|
| Skill Group Name | The enterprise skill group's enterprise name. Derived from: Skill_Group.EnterpriseName |
| Calls Waiting | The number of split or skill ACD calls currently waiting to be answered. This includes calls that are in queue and calls that
                                             are ringing at an agent voice terminal. It does not include direct agent calls. Derived from: Skill_Group_Real_Time.TotalQueuedNow |
| Longest Queued | The time spent in queue for the longest currently queued task, measured in HH:MM:SS (hours, minutes, seconds) format. This is a calculated field, calculated by subtracting the time the task entered the queue from the current time and derived
                                             from: DATEDIFF(ss, Skill_Group_Real_Time.RouterLongestCallQ, (SELECT NowTime from Controller_Time)),0) |