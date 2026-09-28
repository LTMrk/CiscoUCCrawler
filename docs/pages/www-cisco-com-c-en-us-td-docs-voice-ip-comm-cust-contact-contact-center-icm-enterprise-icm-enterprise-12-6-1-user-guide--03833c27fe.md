---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--03833c27fe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/ucce_b_cisco-unified-contact-center-enterprise-1261/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_01101.html
retrieved_at: 2026-08-21T04:27:30.508697+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(1)

Updated: May 14, 2020

Chapter: Transitional Historical Reports

## Chapter: Transitional Historical Reports

# Transitional Historical Reports

## Agent Attendance
                        	 Historical

The Agent
                              		  Attendance Historical Report gives the total staffed time, handle time, wrap up time, not ready time, time in the ringing
                              state, available time, and the number
                              		  of tasks handled by an agent for the specified period for all splits or skills
                              		  the agent was logged into.

You can select Agent Attendance templates to display the data in a daily report (the default), a weekly report, or a monthly
                              report. When viewing the daily report, you can display an interval view by selecting Agent Attendance Interval Historical in the report drop-down list located on the top left corner. The interval view summarizes the data for each agent at the
                              configured interval, 15 or 30 minutes.

Query: This
                              		  report data is built from an Anonymous Block.

Views: These reports have the following grid views:

Report

View

Agent Attendance Historical

Agent Attendance Historical

Agent Attendance Interval Historical

Agent Attendance Weekly Historical

Agent Attendance Weekly Historical

Agent Attendance Monthly Historical

Agent Attendance Monthly Historical

Grouping: This report is grouped and sorted by Agent Name and then by Date (Daily); Date
                              		  Time (Interval); Week (Weekly); or Month (Monthly).

Value List: Agent

Database Schema Tables from which data is retrieved:

Agent

Agent_Interval

Person

Agent_Skill_Group_Interval

Skill_Group

Media_Routing_Domain

Precision_Queue

### Current Fields
                              		  in the Agent Attendance Historical Report

Current fields are those fields that appear by default in a report generated from the
                              		  stock template. Current fields are listed below in the order (left to right) in
                              		  which they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

Date/Date Time/Week/Month

The
                                          						date, interval, week, or month, depending on the Agent Attendance report selected.

Derived from: Agent_Skill_Group_Interval.DateTime

Year

(Appears only in Monthly report.)

The
                                          						year of the selected row's data.

Derived from: Agent_Skill_Group_Interval.DateTime

Logged on Time

The
                                          						total time during the interval the agent was logged in, measured in HH:MM:SS
                                          						(hours, minutes, seconds) format.

Derived
                                          						from: Agent_Interval.LoggedOnTime

Handled

The number of Unified CCE Routed tasks this agent has handled across skill groups during the interval.

Derived from: Agent_Skill_Group_Interval.CallsHandled

Handle
                                          						Time

The
                                          						total number of seconds spent on inbound tasks that have been answered and have
                                          						completed wrap-up by agents across skill groups during the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.HandledCallsTime

Wrap Up Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime

Agent
                                          						Ring Time

How long
                                          						an agent is in Reserved state. This is counted using Agent state.

Derived
                                          						from: Agent_Skill_Group_Interval.ReservedStateTime

Internal

The
                                          						number of internal tasks agents across skill groups ended during the interval.

Derived from: Agent_Skill_Group_Interval.InternalCalls

Internal
                                          						Time

The
                                          						total number of seconds an agent across skill groups spent on internal tasks
                                          						that ended during the reporting interval.

Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime

Available
                                          						Time

The
                                          						total time in seconds an agent was in the Not_Active state across skill groups
                                          						during the reporting interval. AvailTime is included in the calculation of
                                          						LoggedOnTime.

Derived
                                          						from: Agent_Interval.AvailTime

Not
                                          						Ready Time

The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. Value taken directly from the database.

Derived
                                          						from: Agent_Interval.NotReadyTime.

Report
                                 			 Summary: This report has a report summary for all data.

## Agent Skill
                        	 Historical

The Agent
                              		  Split/Skill Historical report shows an individual agent's performance by split or skill
                              		  for the specified period.

You can select Agent Skill Historical templates to display the report in a daily view (the default), a weekly view, or a monthly
                              view. When viewing the daily report, you can display an interval view by selecting Agent Skill Interval Historical in the report drop-down list located on the top left corner. The interval view summarizes the data for each agent at the
                              configured interval, 15 or 30 minutes.

Query: This report data
                              		  is built from an Anonymous Block.

Views: These reports have the following grid views:

Report

View

Agent Skill Historical

Agent Skill Historical

Agent Skill Interval Historical

Agent Skill Weekly Historical

Agent Skill Weekly Historical

Agent Skill Monthly Historical

Agent Skill Monthly Historical

Grouping: This report
                              		  is grouped by Agent Name then Skill Group Name, and sorted by Date (Daily);
                              		  Date Time (Interval); Week (Weekly); or Month (Monthly).

Value List: Agent

Database Schema Tables from which data is retrieved:

Agent

Agent_Interval

Person

Agent_Skill_Group_Interval

Skill_Group

Media_Routing_Domain

Precision_Queue

### Current Fields
                              		  in the Agent Skill Historical Report

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are listed below in the order (left to right) in which they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

Precision Queue/ Skill Group

The
                                          						precision queue's enterprise name or the enterprise skill group's enterprise
                                          						name.

Derived
                                          						from: Skill_Group.EnterpriseName (Skill_Group.EnterpriseSkillGroup)

Date/Date Time/Week/Month

The
                                          						interval, date, week, or month, depending on the view/report selected.

Derived from: Agent_Skill_Group_Interval.DateTime

Year

(Appears only in Monthly report.)

The year of the selected row's data.

Derived from: Agent_Skill_Group_Interval.DateTime

Handled

The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents in the skill group during the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.CallsHandled

Handle
                                          						Time

The
                                          						amount of time agents in the skill group have spent handling tasks during the
                                          						interval.

Derived
                                          						from: Agent_Skill_Group_Interval.HandledCallsTime

Wrap Up Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime

Internal

The
                                          						number of internal tasks agents associated with this skill group ended during
                                          						the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.InternalCalls

Internal
                                          						Time

The
                                          						total number of seconds an agent associated with this skill group spent on
                                          						internal tasks that ended during the reporting interval.

Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime

Assists

The
                                          						number of tasks for which an agent received supervisor assistance during the
                                          						report interval.

This is
                                          						a calculated field, derived from: Agent_Skill_Group_Interval.Emergency Assists
                                          						+ Agent_Skill_Group.SupervAssistCalls

Held

The
                                          						number of incoming tasks to this agent that were placed on hold in the
                                          						interval.

Derived
                                          						from: Agent_Skill_Group_Interval.IncomingCallsOnHold

Hold
                                          						Time

The
                                          						total number of seconds that inbound ACD tasks that an agent associated with
                                          						this skill group placed on hold that ended during the reporting interval.

Derived
                                          						from: Agent_Skill_Group_Interval. IncomingCallsOnHoldTime

Transferred

The
                                          						number of tasks this agent transferred to another agent or skill group in the
                                          						interval. This number includes Consultative Calls if this transfer was
                                          						consultative-not blind. The number is updated at the time the agent completes
                                          						the transfer of the task.

This field is
                                          						a calculated field, derived from:
                                          						Agent_Skill_Group_Interval.TransferredOutCalls +
                                          						Agent_Skill_Group_Interval.NetTransferredOutCalls

Report Summary: This
                              		  report has a report summary for all data.

## Agent Summary
                        	 Historical

The Agent Summary Historical report lists
                              		  the totals for each agent in the group summed over all splits/skills that the
                              		  agent was logged into during the time period covered in the report, displayed
                              		  on a daily basis (the default view). The report also contains information on
                              		  the overall occupancy of the selected agent group, expressed as a percentage,
                              		  both with and without Wrap Up Time included.

You can select Agent Summary Historical templates to display the data in a daily report (the default), a weekly report, or
                              a monthly report. When viewing the daily report, you can display an interval view by selecting Agent Summary Interval Historical in the report drop-down list located on the top left corner. The interval view summarizes the data for each agent at the
                              configured interval, 15 or 30 minutes.

Query: This
                              		  report data is built from an Anonymous Block.

Views: These reports have the following grid views:

Report

View

Agent Summary Historical

Agent Summary Interval Historical

Agent Summary Weekly Historical

Agent Summary Weekly Historical

Agent Summary Monthly Historical

Agent Summary Monthly Historical

Grouping: This report is grouped by Agent Name, Date. The report is sorted by Date (Daily); Date Time (Interval); Week (Weekly); or
                              Month (Monthly).

Value List: Agent

Agent

Agent_Interval

Person

Agent_Skill_Group_Interval

Skill_Group

Media_Routing_Domain

Precision_Queue

### Current Fields
                              		  in the Agent Summary Historical Report

Current fields are those fields that appear by default in a report generated from the
                              		  stock template. Current fields are listed below in the order (left to right) in
                              		  which they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

Date/Date Time/Week/Month

The
                                          						date, interval, week, or month, depending on the view/report selected.

Derived from: Agent_Skill_Group_Interval.DateTime

Year

(Appears only in Monthly report.)

The
                                          						year of the selected row's data. (Applicable only for monthly report.)

Derived from: Agent_Skill_Group_Interval.DateTime

Handled

The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents across skill groups during the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.CallsHandled

Handle Time

The
                                          						total number of seconds spent on inbound tasks that have been answered and have
                                          						completed wrap-up by agents across skill groups during the interval.

Derived from: Agent_Skill_Group_Interval.HandledCallsTime

Avg
                                          						Handle Time

The
                                          						average time spent by the agent in handling a task, measured in HH:MM:SS
                                          						(hours, minutes, seconds).

This field is
                                          						a calculated field derived from:

(Agent_Skill_Group_Interval.HandledCallsTime /
                                          						Agent_Skill_Group_Interval.CallsHandled)

Avg Wrap
                                          						Time

The
                                          						average time spent by the agent in after task work time, measured in HH:MM:SS
                                          						(hours, minutes, seconds).

This field is
                                          						a calculated field, derived from:

Agent_Skill_Group_Interval.WrapTime /
                                          						Agent_Skill_Group_Interval.CallsHandled

%
                                          						Occupancy

The
                                          						percentage of time that the agent has spent in Wrap-up state after incoming or
                                          						outgoing tasks to/from skill groups in relation to LoggedOnTime.

This field is
                                          						a calculated field derived from:

Agent_Skill_Group_Interval.TalkTime +
                                          						Agent_Skill_Group_Interval.WrapTime + Agent_Interval.NotReadyTime +
                                          						Agent_Skill_Group_Interval. HoldTime )* 1.0 / Agent_Interval.LoggedOnTime

%Occupancy Without Wrap Time

The
                                          						percentage of time that the agent has spent talking on tasks across skill
                                          						groups in relation to LoggedOnTime.

This field is
                                          						a calculated field, derived from:

Agent_Skill_Group_Interval.TalkTime +
                                          						Agent_Interval.NotReadyTime + Agent_Skill_Group_Interval. HoldTime
                                          						) * 1.0 / Agent_Interval.LoggedOnTime

Internal

The
                                          						number of internal tasks agents across skill groups ended during the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.InternalCalls

Internal
                                          						Time

The
                                          						total number of seconds an agent across skill groups spent on internal tasks
                                          						that ended during the reporting interval.

Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime

Wrap Up Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval.

Derived from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime

Agent
                                          						Ring Time

How
                                          						long an agent is in Reserved state. This value  is counted using Agent state.

Derived from: Agent_Skill_Group_Interval.ReservedStateTime

Not
                                          						Ready Time

The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. This value is taken directly from the database.

Derived from: Agent_Interval.NotReadyTime.

Available
                                          						Time

The
                                          						total time in seconds an agent was in the Not_Active state across skill groups
                                          						during the reporting interval. AvailTime is included in the calculation of
                                          						LoggedOnTime.

Derived from: Agent_Interval.AvailTime

Logged on Time

The
                                          						total time during the interval the agent was logged in, measured in HH:MM:SS
                                          						(hours, minutes, seconds) format.

Derived from: Agent_Interval.LoggedOnTime

Transferred

The
                                          						number of tasks this agent transferred to another agent or skill group in the
                                          						interval. This number includes Consultative Calls if this transfer was
                                          						consultative-not blind. The number is updated at the time the agent completes
                                          						the transfer of the task.

This
                                          						is a calculated field, derived from:

Agent_Skill_Group_Interval.TransferredOutCalls +
                                          						Agent_Skill_Group_Interval.NetTransferredOutCalls

Held

The
                                          						number of incoming tasks to this agent that were placed on hold in the
                                          						interval.

Derived from: Agent_Skill_Group_Interval.IncomingCallsOnHold

Avg
                                          						Hold Time

The
                                          						average time in HH:MM:SS (hours, minutes, seconds) that tasks were put on hold
                                          						in the interval, for all incoming tasks that included hold time.

This field
                                          						is a calculated field, derived from:

(Agent_Skill_Group_Interval. IncomingCallsOnHoldTime /
                                          						Agent_Skill_Group_Interval.IncomingCallsOnHold)

Report
                                 			 Summary: This report has a report summary for all data.

## Agent Team
                        	 Historical

The Agent Team
                              		  Historical Report gives the total staffed time, handled time, wrap
                              		  time, occupancy, Not Ready time, time in the ringing state, extension time,
                              		  available time, and the number of tasks handled by a team and its agents for
                              		  the specified time period.

You can select Agent Team Historical templates to display the data in a daily report (the default), a weekly report, or a
                              monthly report. When viewing the daily report, you can display an interval view by selecting Agent Team Interval Historical in the report drop-down list located on the top left corner. The interval view summarizes the data for each team at the configured
                              interval, 15 or 30 minutes.

Query: This report data
                              		  is built from an Anonymous Block.

Views: These reports have the following grid views:

Report

View

Agent Team Historical

Agent Team Historical

Agent Team Interval Historical

Agent Team Weekly Historical

Agent Team Weekly Historical

Agent Team Monthly Historical

Agent Team Monthly Historical

Grouping: This
                              		  report is grouped and sorted by Team Name, then by Agent Name, and then by Date
                              		  (Daily); Date Time (Interval); Week (Weekly); or Month (Monthly).

Value List: Agent Teams

Database Schema Tables from which data is retrieved:

Agent

Agent_Interval

Person

Agent_Skill_Group_Interval

Skill_Group

Media_Routing_Domain

Agent_Team

Agent_Team_Member

Precision_Queue

### Current Fields
                              		  in the Agent Team Historical Report

Current fields are
                              		  those fields that appear by default in a report generated from the stock
                              		  template. Current fields are listed below in the order (left to right) in which
                              		  they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Team Name

The
                                          						Enterprise Name of the agent team.

Derived
                                          						from: Agent_Team.EnterpriseName

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

Date/Date Time/Week/Month

The date, interval, week, or month, depending on the
                                          						view/report selected.

Derived from: Agent_Skill_Group_Interval.DateTime

Year

(Appears only in Monthly report.)

The year of the selected row's data.

Derived from: Agent_Skill_Group_Interval.DateTime

Handled

The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents across skill groups during the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.CallsHandled

Handle Time

The
                                          						total number of seconds spent on inbound tasks that have been answered and have
                                          						completed wrap-up by agents across skill groups during the interval

Derived from: Agent_Skill_Group_Interval.HandledCallsTime

Avg
                                          						Handle Time

The
                                          						average time spent by the agent in handling a task, measured in HH:MM:SS
                                          						(hours, minutes, seconds).

This field is
                                          						a calculated field, derived from:

(Agent_Skill_Group_Interval.HandledCallsTime /
                                          						Agent_Skill_Group_Interval.CallsHandled)

Avg Wrap
                                          						Time

The
                                          						average time spent by the agent in after task work time, measured in HH:MM:SS
                                          						(hours, minutes, seconds).

This field is
                                          						a calculated field, derived from:

Agent_Skill_Group_Interval.WrapTime /
                                          						Agent_Skill_Group_Interval.CallsHandled

%Occupancy

The
                                          						percentage of time that the agent has spent talking on tasks across skill
                                          						groups in relation to LoggedOnTime.

This field is
                                          						a calculated field, derived from:

Agent_Skill_Group_Interval.TalkTime +
                                          						Agent_Skill_Group_Interval.WrapTime + Agent_Skill_Group_Interval.NotReadyTime +
                                          						Agent_Skill_Group_Interval. HoldTime )* 1.0 / Agent_Interval.LoggedOnTime

%Occupancy Without Wrap Time

The
                                          						percentage of time that the agent has spent talking on tasks across skill
                                          						groups in relation to LoggedOnTime.

This field is
                                          						a calculated field, derived from:

Agent_Skill_Group_Interval.TalkTime +
                                          						Agent_Skill_Group_Interval.NotReadyTime + Agent_Skill_Group_Interval. HoldTime)
                                          						* 1.0 / Agent_Interval.LoggedOnTime

Internal

The
                                          						number of internal tasks agents across skill groups ended during the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.InternalCalls

Internal
                                          						Time

The
                                          						total number of seconds an agent spent on internal tasks (across skill groups)
                                          						that ended during the reporting interval.

Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime

Wrap Up
                                          						Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group.WorkReadyTime

Agent
                                          						Ring Time

How long
                                          						an agent is in Reserved state. This value is counted using Agent state.

Derived
                                          						from: Agent_Skill_Group_Interval.ReservedStateTime

Not
                                          						Ready Time

The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. This value is taken directly from the database.

Derived
                                          						from: Agent_Interval.NotReadyTime.

Available
                                          						Time

The
                                          						total time in seconds an agent was in the Not_Active state across skill groups
                                          						during the reporting interval. AvailTime is included in the calculation of
                                          						LoggedOnTime.

Derived
                                          						from: Agent_Interval.AvailTime

Logged On Time

The
                                          						total time that the agents were logged in (staffed) for the specified time
                                          						period in any split/skill, measured in HH:MM:SS (hours, minutes, seconds)
                                          						format.

Derived
                                          						from: Agent_Skill_Group_Interval.LoggedOnTime

Report Summary: This
                              		  report has a report summary for all data.

## Agent Team
                        	 Attendance Historical

The Agent
                              		  Team Attendance Historical Report displays the total staffed time, handled
                              		  time, wrap time, Not Ready time, time in the ringing state, extension time,
                              		  available time, and the number of tasks handled by a team for the specified
                              		  time period for all splits or skills the agent was logged into.

You can select Agent Team Attendance Historical templates to display the data in a daily report (the default), a weekly report,
                              or a monthly report. When viewing the daily report, you can display an interval view by selecting Agent Team Attendance Interval Historical in the report drop-down list located on the top left corner. The interval view summarizes the data for each agent at the
                              configured interval, 15 or 30 minutes.

Query: This report data
                              		  is built from an Anonymous Block.

Views: These reports have the following Grid views:

Report

View

Agent Team Attendance Historical

Agent Team Attendance Historical

Agent Team Attendance Interval Historical

Agent Team Attendance Weekly Historical

Agent Team Attendance Weekly Historical

Agent Team Attendance Monthly Historical

Agent Team Attendance Monthly Historical

Grouping: This report
                              		  is grouped and sorted by Agent Team, then by Agent Name, and then by Date
                              		  (Daily); Date Time (Interval); Week (Weekly); or Month (Monthly).

Value List: Agent Team

Agent

Agent_Interval

Person

Agent_Skill_Group_Interval

Skill_Group

Media_Routing_Domain

Agent_Team

Agent_Team_Member

Precision_Queue

### Current Fields
                              		  in the Agent Team Attendance Historical Report

Current fields are
                              		  those fields that appear by default in a report generated from the stock
                              		  template. Current fields are listed below in the order (left to right) in which
                              		  they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Team Name

The
                                          						enterprise name for the Agent Team Name.

Derived
                                          						from: Agent_Team.EnterpriseName

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

Date/Date Time/Week/Month

The
                                          						interval, date, week, or month, depending on the view/report selected.

Derived from: Agent_Skill_Group_Interval.DateTime

Year

(Appears only in Monthly report.)

The year of the selected row's data.

Derived from: Agent_Skill_Group_Interval.DateTime

Name

The
                                          						login name for the Agent.

Derived
                                          						from: Person.LoginName

Logged on Time

The
                                          						total time during the interval the agent was logged in, measured in HH:MM:SS
                                          						(hours, minutes, seconds) format.

Derived
                                          						from: Agent_Interval.LoggedOnTime

Handled

The
                                          						tasks handled by the particular agent.

Derived from:
                                          						SUM(ISNULL(Agent_skill_Group_Interval.CallsHandled, 0))

Handle Time

The
                                          						total time the agent spent handling tasks.

Derived
                                          						from: SUM(ISNULL(Agent_skill_Group_Interval.HandledCallsTime, 0))

Wrap Up
                                          						Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime

Agent
                                          						Ring Time

How long
                                          						an agent is in Reserved state. This value is counted using Agent state.

Derived
                                          						from: Agent_Skill_Group_Interval.ReservedStateTime

Internal

The
                                          						number of internal tasks handled by the agent.

Derived from: Agent_Skill_Group_Interval.InternalCalls

Internal
                                          						Time

The
                                          						total number of seconds an agent spent on internal tasks (across skill groups)
                                          						that ended during the reporting interval.

Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime

External

The
                                          						outgoing tasks handled by the particular agent.

Derived from:
                                          						SUM(ISNULL(Agent_skill_Group_Interval.AgentOutCalls, 0))

External Time

The
                                          						outgoing tasks time for the particular agent.

Derived
                                          						from: SUM(ISNULL(Agent_skill_Group_Interval.AgentOutCallsTime, 0))

Available
                                          						Time

The
                                          						total time in seconds an agent was in the Not_Active state across skill groups
                                          						during the reporting interval. AvailTime is included in the calculation of
                                          						LoggedOnTime.

Derived
                                          						from: Agent_Interval.AvailTime

Not
                                          						Ready Time

The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. This value is taken directly from the database.

Derived
                                          						from: Agent_Interval.NotReadyTime.

Report
                                 			 Summary: This report has a report summary for all data.

## Call Type Skill
                        	 Group Historical

The Call Type
                              		  Skill Group Historical Report summarizes the activity for an entire skill for
                              		  each call type, displaying the date, inbound tasks, average speed of answer,
                              		  abandoned tasks, average abandoned time, handled tasks, average handled time,
                              		  average wrap time for a given period, service level, and abandoned within
                              		  service level on a daily basis (the default view).

You can choose from three  Call Type Skill
                              	 Group Historical templates to display the data in a daily/interval report (the default), a weekly
                              		  report, or a monthly report:

Call Type Skill
                                    	 Group Historical

Call Type Skill Group Weekly Historical

Call Type Skill Group Monthly Historical

When viewing the Call Type Skill Group Historical report, you can display the interval view by selecting Call Type Skill Group Interval Historical in the report drop-down list located on the top left corner. The interval view summarizes the data for each agent at the
                              configured interval, 15 or 30 minutes.

Query: This report data
                              		  is built from an Anonymous Block.

Views: These reports have the following grid views:

Report

View

Call Type Skill Group Historical

Call Type Skill Group Historical

Call Type Skill Group Interval Historical

Call Type Skill Group Weekly Historical

Call Type Skill Group Weekly Historical

Call Type Skill Group Monthly Historical

Call Type Skill Group Monthly Historical

Grouping: This report
                              		  is grouped and sorted by Call Type Name, Skill Group Name, and then by Date
                              		  (Daily); Date Time (Interval); Week (Weekly); or Month (Monthly).

Value List: Call Types

Database Schema Tables from which data is retrieved:

Skill_Group

Call_Type

Call_Type_SG_Interval

Media_Routing_Domain

Precision_Queue

### Current Fields
                              		  in the Call Type Skill Group Historical Report

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

Precision Queue/Skill Group

The
                                          						enterprise name for the Skill Group.

Derived
                                          						form: Skill_Group.EnterpriseName

Date/Date Time/Week/Month

The date, interval, week, or month, depending on the
                                          						view/report selected.

Derived
                                          						from: Call_Type.DateTime

Year

(Appears only in Monthly report.)

The year of the selected row's data.

Derived from: Call_Type_SG_Interval.DateTime

Inbound

Tasks
                                          						that have been offered to this call type during the interval.

Derived
                                          						from: sum(isnull(Call_Type_SG_Interval.CallsOffered,0))

Avg
                                          						Speed of Answer

The average answer wait time from when first queue to skill group or LAA select node was run for this call to when this call
                                          was answered.

This field is
                                          						a calculated field derived from:

```
CASE WHEN sum(isnull(Call_Type_SG_Interval.CallsAnswered,0)) = 0
 THEN 0
 ELSE sum(isnull(Call_Type_SG_Interval.AnswerWaitTime,0)) * 1.0 / 
sum(isnull(Call_Type_SG_Interval.CallsAnswered,0))
END
```

%
                                          						Queued

The
                                          						percentage of all handled tasks of the call type that were queued in the
                                          						interval.

This
                                          						field is a calculated field derived from:

(Call_Type_SG_Interval.CallsQHandled /

Call_Type_SG_Interval.CallsHandled).

Abandon in
                                          						Queue

The
                                          						total number of tasks abandoned while in VRU (that is, while undergoing
                                          						prompting or listening to voice menus options), tasks abandoned while queued to
                                          						skill group, and tasks abandoned at agent desktop. This value also includes
                                          						abandons for tasks that are not in the queue. Therefore, the number of tasks
                                          						abandoned at a VRU before being queued is TotalCallsAband minus
                                          						RouterCallsAbandToAgent and RouterCallsAbandQ. The number does not include short tasks.

Derived
                                          						from: sum(isnull(Call_Type_SG_Interval.RouterCallsAbandQ, 0)

Avg Abandon
                                          						Time

The
                                          						average time of abandoned tasks for this call type measured in HH:MM:SS (hours,
                                          						minutes, seconds) format.

This field is
                                          						a calculated field, derived from:

```
CASE WHEN sum( isnull (Call_Type_SG_Interval.TotalCallsAband, 0)) = 0 THEN 0
 ELSE isnull ((sum( isnull (Call_Type_SG_Interval.DelayQAbandTime, 0)) / sum (isnull 
(Call_Type_SG_Interval.TotalCallsAband, 0))),0)
END
```

Handled

The
                                          						number of tasks handled across agents in the call type.

Derived
                                          						from: sum(isnull(Call_Type_SG_Interval.CallsHandled,0))

Avg
                                          						Handle Time

The
                                          						average time in HH:MM:SS (hours, minutes, seconds) it has taken to handle a
                                          						task.

sum(isnull(Call_Type_SG_Interval.HandleTime,0)) /
                                          						sum(isnull(CTSG.CallsHandled,0))

Avg Wrap
                                          						Time

The
                                          						average time spent across agents in the call type after call work time,
                                          						measured in HH:MM:SS (hours, minutes, seconds).

This field is
                                          						a calculated field, derived from:

```
CASE WHEN (sum(isnull(Call_Type_SG_Interval.HandleTime,0)) 
- sum(isnull(Call_Type_SG_Interval.TalkTime,0)) 
- sum(isnull(Call_Type_SG_Interval.HoldTime,0))) = 0
 THEN 0
 ELSE (sum(isnull(Call_Type_SG_Interval.HandleTime,0)) 
- sum(isnull(Call_Type_SG_Interval.TalkTime,0)) 
- sum(isnull(Call_Type_SG_Interval.HoldTime,0))) / sum(isnull(Call_Type_SG_Interval.CallsHandled,0))
END
```

Service Level

The
                                          						Service Level Type used to calculate Service level for the interval.

Derived from: Call_Type_Interval.ServiceLevel.

Abandon
                                          						Within Service Level

The total number of tasks of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes.

Derived from: Call_Type_Interval.ServiceLevelAband.

Report
                                 			 Summary: This report has a report summary for all data.

## Skill
                        	 Historical

The Skill Historical Report displays the tasks handled, agent time and assists, and transfers and holds for each agent in
                              a skill. This report shows only the time each agent worked in this particular skill.

You can choose from four Skill Historical templates to display the data in a daily report (the default), an interval report,
                              a weekly report, or a monthly report:

Skill Daily Historical

Skill Interval Historical

Skill Weekly Historical

Skill Monthly Historical

The interval view summarizes the data for each agent at the configured interval, 15 or 30 minutes.

Query: This report data is built from an Anonymous Block.

Views: These reports have the following grid views:

Report

View

Skill Daily Historical

Skill Daily Historical

Skill Interval Historical

Skill Historical

Skill Weekly Historical

Skill Weekly Historical

Skill Monthly Historical

Skill Monthly Historical

Select the view you want to see from the report drop-down list located on the top left corner.

Grouping: This report is grouped by Skill Group Name and Agent Name, then by Date (Daily); Date Time (Interval); Week (Weekly); or
                              Month (Monthly).

Value List: Skill Groups

Database Schema Tables from which data is retrieved:

Agent

Agent_Interval

Person

Agent_Skill_Group_Interval

Skill_Group

Media_Routing_Domain

### Current Fields
                              		  in the Skill Historical Report

Current fields are
                              		  those fields that appear by default in a report generated from the stock
                              		  template. Current fields are listed in the order (left to right) in which
                              		  they appear by default in the stock template.

Column
                                          						(Field)

Description

Skill
                                          						Group Name

The
                                          						enterprise skill group's enterprise name.

Derived
                                          						from: Skill_Group.EnterpriseName

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

Date/Date Time/Week/Month

The
                                          						date, interval, week, or month, depending on the report selected.

Derived
                                          						from: Agent_Skill_Group_Interval.DateTime

Year

(Appears only in Monthly report.)

The
                                          						year of the selected row's data.

Derived from: Agent_Skill_Group_Interval.DateTime

Handled

The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents in the skill group during the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.CallsHandled

Handle Time

The
                                          						percentage of time,  in relation to LoggedOnTime, that the agent has spent in Wrap-up state after incoming or
                                          						outgoing tasks for each skill group.

Derived from: Agent_Skill_Group_Interval.HandledCallsTime

Avg
                                          						Handle Time

The
                                          						average time spent by the agent in handling a task, measured in HH:MM:SS
                                          						(hours, minutes, seconds).

This field is
                                          						a calculated field derived from:

(Agent_Skill_Group_Interval.HandledCallsTime /
                                          						Agent_Skill_Group_Interval.CallsHandled)

Avg Wrap
                                          						Time

The
                                          						average time spent by the agent in after task work time, measured in HH:MM:SS
                                          						(hours, minutes, seconds).

This field is
                                          						a calculated field, derived from:

Agent_Skill_Group_Interval.WrapTime /
                                          						Agent_Skill_Group_Interval.CallsHandled

Wrap Up
                                          						Time

The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval.

Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime

Agent
                                          						Ring Time

How long
                                          						an agent is in Reserved state. This value is counted using Agent state.

Derived
                                          						from: Agent_Skill_Group_Interval.ReservedStateTime

Not
                                          						Ready Time

The
                                          						total time that the agents spent in Not Ready state for this skill for the
                                          						specified time period. This value is taken directly from the database.

Derived
                                          						from: Agent_Interval.NotReadyTime.

Available
                                          						Time

The
                                          						total time in seconds an agent associated with this skill group was in the
                                          						Not_Active state with respect to this skill group during the reporting
                                          						interval. AvailTime is included in the calculation of LoggedOnTime.

Derived
                                          						from: Agent_Interval.AvailTime

Logged On
                                          						Time

The
                                          						total time during the interval the agent was logged in, measured in HH:MM:SS
                                          						(hours, minutes, seconds) format.

Derived from: Agent_Interval.LoggedOnTime

Assists

The
                                          						number of tasks for which an agent received supervisor assistance during the
                                          						report interval.

This
                                          						is a calculated field, derived from:

Agent_Skill_Group_Interval.Emergency Assists +
                                          						Agent_Skill_Group_Interval.SupervAssistCalls

Transferred

The
                                          						number of tasks this agent transferred to another agent or skill group in the
                                          						interval. This number includes Consultative Calls if this transfer was
                                          						consultative-not blind. The number is updated at the time the agent completes
                                          						the transfer of the task.

This
                                          						is a calculated field, derived from:

Agent_Skill_Group_Interval.TransferredOutCalls +
                                          						Agent_Skill_Group_Interval.NetTransferredOutCalls

Held

The
                                          						number of incoming tasks to this agent that were placed on hold in the
                                          						interval.

Derived from: Agent_Skill_Group_Interval.IncomingCallsOnHold

Avg
                                          						Hold Time

The
                                          						average time in HH:MM:SS (hours, minutes, seconds) that tasks were put on hold
                                          						in the interval, for all incoming tasks that included hold time.

This
                                          						field is a calculated field, derived from:

(Agent_Skill_Group_Interval. IncomingCallsOnHoldTime /
                                          						Agent_Skill_Group_Interval.IncomingCallsOnHold)

Report
                                 			 Summary: This report has a report summary for all data.

## Skill Call Profile
                        	 Historical

The Skill Call Profile Historical report shows
                              		  how well the skill you specify performed compared to the predefined service
                              		  levels for your call center for the date you specify, for a given time period.

You can choose from three  Skill Call Profile
                              	 Historical templates to display the data in a daily/interval report (the default), a weekly
                              		  report, or a monthly report:

Skill Call Profile
                                    	 Historical

Skill Call Profile
                                    	 Weekly Historical

Skill Call Profile
                                    	 Monthly Historical

When viewing the Skill Call Profile Historical report, you can display the interval view by selecting Skill Call Profile Interval Historical in the report drop-down list located on the top left corner. The interval view summarizes the data for each agent at the
                              configured interval, 15 or 30 minutes.

Query: This
                              		  report data is built from an Anonymous Block.

Views: These reports have the following grid views:

Report

View

Skill Call Profile Historical

Skill Call Profile Historical

Skill Call Profile Interval Historical

Skill Call Profile Weekly Historical

Skill Call Profile Weekly Historical

Skill Call Profile Monthly Historical

Skill Call Profile Monthly Historical

Grouping: This report is grouped by Skill Group Name and sorted by Date (Daily); Date
                              		  Time (Interval); Week (Weekly); or Month (Monthly).

Value List: Skill Groups

Skill_Group_Interval

Bucket_Interval

Skill_Group

### Current Fields
                              		  in the Skill Call Profile Historical Report

Current fields are those fields that appear by default in a report generated from the
                              		  stock template. Current fields are listed below in the order (left to right) in
                              		  which they appear by default in the stock template.

Column
                                          						(Field)

Description

Skill
                                          						Group Name

The
                                          						enterprise skill group's enterprise name.

Derived from: Skill_Group.EnterpriseName
                                          						(Skill_Group.EnterpriseSkillGroupID)

Date/Date Time/Week/Month

The
                                          						date, interval, week, or month, depending on the report selected.

Derived
                                          						from: Skill_Group_Interval.DateTime

Year

(Appears only in Monthly report.)

The
                                          						year of the selected row's data. 
                                          					 (Applicable only for monthly report.)

Derived from: Skill_Group_Interval.DateTime

Handled

The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents in the skill group during the interval.

Derived from: Skill_Group_Interval.CallsHandled

Avg
                                          						Speed Of Answer

The
                                          						average time the skill ACD tasks were waiting in queue and ringing before being
                                          						answered by an agent.

Derived from: Skill_Group_Interval.AnswerWaitTime /
                                          						Skill_Group_Interval.CallsAnswered

%Answer

The
                                          						percentage of tasks queued to the skill that was answered by agents for this
                                          						skill.

This
                                          						is a calculated field, derived from: Skill_Group_Interval.CallsHandled
                                          						/Skill_Group_Interval.CallsOffered

Abandon Calls

The
                                          						number of skill ACD tasks that abandoned within each service level increment.

Derived
                                          						from: (Skill_Group_Interval.RouterCallsAbandQ +
                                          						RouterCallsAbandToAgent )

Avg Abandon
                                          						Time

The
                                          						average time the skill ACD tasks were waiting in queue or ringing before
                                          						abandoning.

Derived
                                          						from: Skill_Group_Interval.RouterDelayQAbandTime +
                                          						SGHH.AbandonRingTime/SGHH.RouterCallsAbandQ+SGHH.AbandonRingCal

%Abandon

The
                                          						percentage of tasks abandoned.

This field is
                                          						a calculated field, derived from:

(Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.AbandonCallsRing )/Skill_Group_Interval.CallsOffered

Abandon, 0-9

The
                                          						number of abandoned tasks in each Bucket Interval.

Derived from: Skill_Group_Interval.RouterAbandInterval

Answered, 0-9

The
                                          						total number of answered tasks in each Bucket Interval.

Derived from: Skill_Group_Interval.RouterAnsInterval

Report
                                 			 Summary: This report has a report summary for all data.

## Skill Summary
                        	 Historical

The Skill Summary
                              		  Historical Report summarizes the activity for an entire skill by time. You can use this
                              		  report to analyze the overall performance of a skill or to compare two or more
                              		  comparable skills.

You can choose from three  Skill Summary
                              	 Historical templates to display the data in a daily/interval report (the default), a weekly
                              		  report, or a monthly report:

Skill Summary Historical

Skill Summary Weekly Historical

Skill Summary Monthly Historical

When viewing the Skill Summary Historical report, you can display the interval view by selecting Skill Summary Interval Historical in the report drop-down list located on the top left corner. The interval view summarizes the data for each agent at the
                              configured interval, 15 or 30 minutes.

Query: This
                              		  report data is built from an Anonymous Block.

Views: These reports have the following grid views:

Report

View

Skill Summary Historical

Skill Summary Historical

Skill Summary Interval Historical

Skill Summary Weekly Historical

Skill Summary Weekly Historical

Skill Summary Monthly Historical

Skill Summary Monthly Historical

Grouping: This report is grouped by Skill Group and sorted by Date (Daily); Date Time
                              		  (Interval); Week (Weekly); or Month (Monthly).

Value List: Skill Groups

Skill_Group

Skill_Group_Interval

Media_Routing_Domain

### Current Fields
                              		  in the Skill Summary Historical Report

Current fields are those fields that appear by default in a report generated from the
                              		  stock template. Current fields are listed below in the order (left to right) in
                              		  which they appear by default in the stock template.

Column
                                          						(Field)

Description

Skill
                                          						Group Name

The
                                          						enterprise skill group's enterprise name and ID.

Derived
                                          						from: Enterprise_Skill_Group.EnterpriseName
                                          						(Enterprise_Skill_Group.EnterpriseSkillGroupID)

Date/Date Time/Week/Month

The
                                          						date, interval, week, or month, depending on the view/report selected.

Derived from: Skill_Group_Interval.DateTime

Media

(Appears only in Weekly report)

A unique name for this media class. Initially, the EnterpriseName is set to Cisco_Voice.

Year

(Appears only in Monthly report.)

The
                                          						year of the selected row's data.

Derived from: Skill_Group_Interval.DateTime

Avg
                                          						Speed Of Answer

The
                                          						average time the skill ACD tasks were waiting in queue and ringing before being
                                          						answered by an agent.

Derived
                                          						from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered

Avg Abandon
                                          						Time

The
                                          						average time the split/skill ACD tasks were waiting in queue or ringing before
                                          						abandoning.

Derived
                                          						from: Skill_Group_Interval.RouterDelayQAbandTime +
                                          						Skill_Group_Interval.AbandonRingTime / Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.AbandonRingCall

Handled

The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents in the skill group during the interval.

Derived
                                          						from: Skill_Group_Interval.CallsHandled

Avg
                                          						Handle Time

The
                                          						average time spent by the agent in handling a task, measured in HH:MM:SS
                                          						(hours, minutes, seconds).

This field is
                                          						a calculated field derived from:

(Skill_Group_Interval.HandledCallsTime /
                                          						Skill_Group_Interval.CallsHandled)

Avg Wrap
                                          						Time

The
                                          						average time spent by the agent in after task work time, measured in HH:MM:SS
                                          						(hours, minutes, seconds).

This field is
                                          						a calculated field, derived from:

Skill_Group_Interval.WrapTime /
                                          						Skill_Group_Interval.CallsHandled

Abandon

For
                                          						voice: the total number of tasks that were abandoned while the agent's phone
                                          						was ringing. For non-voice: the total number of tasks that were abandoned while
                                          						being offered to an agent.

Derived
                                          						from: (Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.RouterCallsAbandToAgent)

Max
                                          						Delay Time

The
                                          						longest a task had to wait before being answered, abandoned, or otherwise
                                          						ended.

Derived
                                          						from: Skill_Group_Interval.RouterMaxCallsWaitTime

Dequeued

The
                                          						number of tasks that were dequeued from this skill group to be routed to
                                          						another skill group in the reporting interval.

Derived
                                          						from: Skill_Group_Interval.RouterCallsDequeued

%
                                          						Handle Time

The
                                          						percentage of time on handled tasks.

This
                                          						is a calculated field, derived from:

Skill_Group_Interval.HandledCallsTime
                                          						/Skill_Group_Interval.LoggedOnTime

% Answer

The
                                          						percentage of answered tasks.

This
                                          						field is a calculated field, derived from:

Skill_Group_Interval.CallsHandled
                                          						/Skill_Group_Interval.CallsOffered

Report
                                 			 Summary This report has a report summary for all data.

## Agent Login/Logout
                        	 Historical

The Agent
                              		  Login/Logout (Skill) Historical report shows the times that agents logged in and logged
                              		  out, the reason codes associated with the logout (if there is one), and the
                              		  skills with which the agents logged in and out.

Query: This
                              		  report data is built from an Anonymous Block.

Views: This report one grid view, Agent Login Logout Historical.

Grouping: This report is grouped by Agent Name and sorted by Date Time.

Value List: Agent

Agent_Logout

Agent_Skill_Group_Logout

Skill_Group

Agent

Person

Reason_Code

Agent_Attribute

Attribute

### Current Fields
                              		  in the Agent Login/Logout Report

Current fields are those fields that appear by default in a report generated from the
                              		  stock template. Current fields are listed below in the order (left to right) in
                              		  which they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from:Person.LastName "," Person.FirstName

Extension

The
                                          						phone extension into which the agent is logged. Taken directly from the table.

Derived from: Agent_Logout.Extension

Logged On DateTime

The date that the agent logged on to the given set of skills, measured in MM:DD:YYYY (month, day, year) and HH:MM:SS (hours,
                                          minutes, seconds) format.

Derived from: Agent_Logout.LogoutDateTime-Agent_Logout.LoginDuration

Logout
                                          						DateTime

The
                                          						date that the agent logged out from the given set of skills, measured in
                                          						MM:DD:YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Derived from: Agent_Logout.LogoutDateTime

Logged On Time

The
                                          						total time that the agents were logged in (staffed) for the specified time
                                          						period in any split/skill, measured in HH:MM:SS (hours, minutes, seconds)
                                          						format.

Derived
                                          						from: Agent_Skill_Group_Interval.LoggedOnTime

Logout
                                          						Reason

A code
                                          						and text (if configured) from the peripheral that indicates the reason for the
                                          						agent's last state change. If not defined, this value displays 0.

Derived
                                          						from: Agent_Logout.Reason_Code

Attribute, 1 to 3

The
                                          						attributes with which the agent primarily interacted during this session.

Skill,
                                          						1 to 3

The
                                          						skills with which the agent primarily interacted during this session.

Derived
                                          						from: Agent_Skill_Group_Logout.SkillGroupSkillTargetID

Report
                                 			 Summary: This report has a report summary for all data.

## Agent Not Ready
                        	 Historical

The Agent Not Ready Historical report shows
                              		  the total Logged On Time, total Not Ready time, and Not Ready time for each
                              		  reason code for an agent.

Query: This
                              		  report data is built from an Anonymous Block.

Views: This report has one grid view, Agent Not Ready Historical.

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

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are listed below in the order (left to right) in which they appear by default in the stock template.

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

Not Ready Time spent in 50002. A CTI OS component failed, causing the agent to be set to Not Ready. This could be due to closing
                                          the agent desktop application, heartbeat timeout, a CTI OS Server failure, or a CTI OS failure.

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

## Agent State Trace
                        	 Historical

The Agent State
                              		  Trace Historical Report lists each agent's activity and the time the activity
                              		  occurred.

Query: This
                              		  report data is built from an Anonymous Block.

Views: This report has one grid view, Agent State Trace Historical.

Grouping: This report is grouped and sorted by Agent Name and then by Date
                              		  and Time (Interval).

Value List: Agent

Database Schema Tables from which data is retrieved:

Agent_State_Trace

Agent

Person

Skill_Group

Media_Routing_Domain

### Current Fields
                              		  in the Agent State Trace Historical Report

Current fields are those fields that appear by default in a report generated from the
                              		  stock template. Current fields are listed below in the order (left to right) in
                              		  which they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Name

The
                                          						first name and last name of the agent.

Derived
                                          						from: Person.LastName "," Person.FirstName

Precision Queue / Skill Group

The
                                          						Skill Group or the Precision Queue associated with an agent for the
                                          						corresponding Agent State.

Derived
                                          						from: Skill_Group.EnterpriseName

DateTime

The date
                                          						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                          						HH:MM:SS (hours, minutes, seconds) format.

Derived
                                          						from: Agent_Skill_Group_Interval.DateTime

Agent
                                          						State

The
                                          						state for the Agent.

Derived
                                          						from:

```
CASE Agent_State_Trace.AgentState 
WHEN 0 THEN 'Logged Out' 
WHEN 1 THEN 'Logged On' 
WHEN 2 THEN 'Not Ready' 
WHEN 3 THEN 'Ready' 
WHEN 4 THEN 'Talking' 
WHEN 5 THEN 'Work Not Ready' 
WHEN 6 THEN 'Work Ready' 
WHEN 7 THEN 'Busy Other' 
WHEN 8 THEN 'Reserved' 
WHEN 9 THEN 'Unknown' 
WHEN 10 THEN 'Hold' 
WHEN 11 THEN 'Active' 
WHEN 12 THEN 'Paused' 
WHEN 13 THEN 'Interrupted' 
WHEN 14 THEN 'Not Active' 
ELSE CONVERT(VARCHAR, Agent_State_Trace.AgentState) 
END
```

Logout
                                          						Reason

The
                                          						reason why an agent logged out.

Derived
                                          						from:

```
CASE WHEN Agent_State_Trace.EventName=2 THEN 
  (SELECT ReasonText FROM Reason_Code WHERE Deleted='N' andReasonCode=Agent_State_Trace.ReasonCode)
    ELSE 'None' 
END
```

Not
                                          						Ready Reason

The
                                          						reason why an agent is in a Not Ready state.

Derived
                                          						from:

```
CASE WHEN Agent_State_Trace.EventName=3 THEN 
   SELECT ReasonText FROM Reason_Code WHERE Deleted='N' and ReasonCode=Agent_State_Trace.ReasonCode)
    ELSE 'None' 
END
```

Media

The
                                          						enterprise name for the Domain.

Derived
                                          						from: Media_Routing_Domain.EnterpriseName

Direction

The
                                          						direction of the task.

Derived
                                          						from:

```
CASE WHEN AST.Direction=1 THEN 'In'
WHEN AST.Direction = 2 THEN 'Out'
WHEN AST.Direction = 3 THEN 'Other In'
WHEN AST.Direction = 4 THEN 'Other Out'
WHEN AST.Direction = 5 THEN 'Out Reserve'
WHEN AST.Direction = 6 THEN 'Out Preview'
WHEN AST.Direction = 7 THEN 'Out Predictive'
   ELSE 'None'
END
```

Peripheral Call Key

The key
                                          						assigned by the peripheral to the task associated with the event.

Derived
                                          						from: ISNULL(Agent_State_Trace.PeripheralCallKey,0)

Router
                                          						Call Key

This
                                          						field is not set for tasks.

Derived
                                          						from: ISNULL(Agent_State_Trace.RouterCallKey,0)

Router
                                          						Call Key Day

This
                                          						field is not set for tasks.

Derived from: ISNULL(Agent_State_Trace.RouterCallKeyDay,0) in
                                          						the calculation of LoggedOnTime.

Router
                                          						Call Key Sequence Number

This
                                          						field is not set for tasks.

Derived from: ISNULL(Agent_State_Tra
                                          						ce.RouterCallKeySequenceNumber,0)

## Agent Team Not
                        	 Ready Historical

The Agent Team Not
                              		  Ready Historical Report shows the total staffed time, total Not Ready time, and
                              		  Not Ready time for each reason code for all agents in an agent group.

Query: This
                              		  report data is built from an Anonymous Block.

Views: This report has one grid view, Agent Team Not Ready Historical.

Grouping: This report is grouped and sorted by Team Name, then by Agent
                              		  Name, and then by Date and Time at every interval.

Value List: AgentTeam

Database Schema Tables from which data is retrieved:

Agent

Person

Agent_Team_Member

Agent_Team

Agent_Interval

Agent_Event_Detail

### Current Fields
                              		  in the Agent Team Not Ready Historical Report

Current fields are those fields that appear by default in a report generated from the
                              		  stock template. Current fields are listed below in the order (left to right) in
                              		  which they appear by default in the stock template.

Column
                                          						(Field)

Description

Agent
                                          						Team Name

The
                                          						Enterprise Name of the agent team.

Derived
                                          						from: Agent_Team. EnterpriseName

Agent
                                          						Name

The
                                          						first and last name of the agent.

Derived
                                          						from Person. LastName ", 
                                             						" Person. FirstName

DateTime

The date
                                          						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                          						HH:MM:SS (hours, minutes, seconds) format.

Derived
                                          						from: Agent_Skill_Group_Interval. DateTime

Logged On
                                          						Time

The
                                          						total time that the agents were logged in (staffed) for the specified time
                                          						period in any split/skill, measured in HH:MM:SS (hours, minutes, seconds)
                                          						format.

Derived
                                          						from: Agent_Skill_Group_Interval. LoggedOnTime

Not
                                          						Ready Time

The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. Value taken directly from the database.

Derived
                                          						from: Agent_Interval. NotReadyTime

Time in

RC0 to RC9

The time
                                          						that the agent spent in Not Ready state with each of the reason codes 0 - 9.

Derived
                                          						from: Agent_Event_Detail

RC50002

Not
                                          						Ready Time spent in 50002; a CTI OS component failed, causing the agent to be
                                          						logged out. This could be due to closing the agent desktop application,
                                          						heartbeat timeout, a CTI OS Server failure, or a CTI OS failure.

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

| Report | View |
|---|---|
| Agent Attendance Historical | Agent Attendance Historical Agent Attendance Interval Historical |
| Agent Attendance Weekly Historical | Agent Attendance Weekly Historical |
| Agent Attendance Monthly Historical | Agent Attendance Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| Date/Date Time/Week/Month | The
                                          						date, interval, week, or month, depending on the Agent Attendance report selected. Derived from: Agent_Skill_Group_Interval.DateTime |
| Year (Appears only in Monthly report.) | The
                                          						year of the selected row's data. Derived from: Agent_Skill_Group_Interval.DateTime |
| Logged on Time | The
                                          						total time during the interval the agent was logged in, measured in HH:MM:SS
                                          						(hours, minutes, seconds) format. Derived
                                          						from: Agent_Interval.LoggedOnTime |
| Handled | The number of Unified CCE Routed tasks this agent has handled across skill groups during the interval. Derived from: Agent_Skill_Group_Interval.CallsHandled |
| Handle
                                          						Time | The
                                          						total number of seconds spent on inbound tasks that have been answered and have
                                          						completed wrap-up by agents across skill groups during the interval. Derived
                                          						from: Agent_Skill_Group_Interval.HandledCallsTime |
| Wrap Up Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval. Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime |
| Agent
                                          						Ring Time | How long
                                          						an agent is in Reserved state. This is counted using Agent state. Derived
                                          						from: Agent_Skill_Group_Interval.ReservedStateTime |
| Internal | The
                                          						number of internal tasks agents across skill groups ended during the interval. Derived from: Agent_Skill_Group_Interval.InternalCalls |
| Internal
                                          						Time | The
                                          						total number of seconds an agent across skill groups spent on internal tasks
                                          						that ended during the reporting interval. Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime |
| Available
                                          						Time | The
                                          						total time in seconds an agent was in the Not_Active state across skill groups
                                          						during the reporting interval. AvailTime is included in the calculation of
                                          						LoggedOnTime. Derived
                                          						from: Agent_Interval.AvailTime |
| Not
                                          						Ready Time | The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. Value taken directly from the database. Derived
                                          						from: Agent_Interval.NotReadyTime. |

| Report | View |
|---|---|
| Agent Skill Historical | Agent Skill Historical Agent Skill Interval Historical |
| Agent Skill Weekly Historical | Agent Skill Weekly Historical |
| Agent Skill Monthly Historical | Agent Skill Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| Precision Queue/ Skill Group | The
                                          						precision queue's enterprise name or the enterprise skill group's enterprise
                                          						name. Derived
                                          						from: Skill_Group.EnterpriseName (Skill_Group.EnterpriseSkillGroup) |
| Date/Date Time/Week/Month | The
                                          						interval, date, week, or month, depending on the view/report selected. Derived from: Agent_Skill_Group_Interval.DateTime |
| Year (Appears only in Monthly report.) | The year of the selected row's data. Derived from: Agent_Skill_Group_Interval.DateTime |
| Handled | The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents in the skill group during the interval. Derived
                                          						from: Agent_Skill_Group_Interval.CallsHandled |
| Handle
                                          						Time | The
                                          						amount of time agents in the skill group have spent handling tasks during the
                                          						interval. Derived
                                          						from: Agent_Skill_Group_Interval.HandledCallsTime |
| Wrap Up Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval. Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime |
| Internal | The
                                          						number of internal tasks agents associated with this skill group ended during
                                          						the interval. Derived
                                          						from: Agent_Skill_Group_Interval.InternalCalls |
| Internal
                                          						Time | The
                                          						total number of seconds an agent associated with this skill group spent on
                                          						internal tasks that ended during the reporting interval. Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime |
| Assists | The
                                          						number of tasks for which an agent received supervisor assistance during the
                                          						report interval. This is
                                          						a calculated field, derived from: Agent_Skill_Group_Interval.Emergency Assists
                                          						+ Agent_Skill_Group.SupervAssistCalls |
| Held | The
                                          						number of incoming tasks to this agent that were placed on hold in the
                                          						interval. Derived
                                          						from: Agent_Skill_Group_Interval.IncomingCallsOnHold |
| Hold
                                          						Time | The
                                          						total number of seconds that inbound ACD tasks that an agent associated with
                                          						this skill group placed on hold that ended during the reporting interval. Derived
                                          						from: Agent_Skill_Group_Interval. IncomingCallsOnHoldTime |
| Transferred | The
                                          						number of tasks this agent transferred to another agent or skill group in the
                                          						interval. This number includes Consultative Calls if this transfer was
                                          						consultative-not blind. The number is updated at the time the agent completes
                                          						the transfer of the task. This field is
                                          						a calculated field, derived from:
                                          						Agent_Skill_Group_Interval.TransferredOutCalls +
                                          						Agent_Skill_Group_Interval.NetTransferredOutCalls |

| Report | View |
|---|---|
| Agent Summary Historical | Agent Summary Historical Agent Summary Interval Historical |
| Agent Summary Weekly Historical | Agent Summary Weekly Historical |
| Agent Summary Monthly Historical | Agent Summary Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| Date/Date Time/Week/Month | The
                                          						date, interval, week, or month, depending on the view/report selected. Derived from: Agent_Skill_Group_Interval.DateTime |
| Year (Appears only in Monthly report.) | The
                                          						year of the selected row's data. (Applicable only for monthly report.) Derived from: Agent_Skill_Group_Interval.DateTime |
| Handled | The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents across skill groups during the interval. Derived
                                          						from: Agent_Skill_Group_Interval.CallsHandled |
| Handle Time | The
                                          						total number of seconds spent on inbound tasks that have been answered and have
                                          						completed wrap-up by agents across skill groups during the interval. Derived from: Agent_Skill_Group_Interval.HandledCallsTime |
| Avg
                                          						Handle Time | The
                                          						average time spent by the agent in handling a task, measured in HH:MM:SS
                                          						(hours, minutes, seconds). This field is
                                          						a calculated field derived from: (Agent_Skill_Group_Interval.HandledCallsTime /
                                          						Agent_Skill_Group_Interval.CallsHandled) |
| Avg Wrap
                                          						Time | The
                                          						average time spent by the agent in after task work time, measured in HH:MM:SS
                                          						(hours, minutes, seconds). This field is
                                          						a calculated field, derived from: Agent_Skill_Group_Interval.WrapTime /
                                          						Agent_Skill_Group_Interval.CallsHandled |
| %
                                          						Occupancy | The
                                          						percentage of time that the agent has spent in Wrap-up state after incoming or
                                          						outgoing tasks to/from skill groups in relation to LoggedOnTime. This field is
                                          						a calculated field derived from: Agent_Skill_Group_Interval.TalkTime +
                                          						Agent_Skill_Group_Interval.WrapTime + Agent_Interval.NotReadyTime +
                                          						Agent_Skill_Group_Interval. HoldTime )* 1.0 / Agent_Interval.LoggedOnTime |
| %Occupancy Without Wrap Time | The
                                          						percentage of time that the agent has spent talking on tasks across skill
                                          						groups in relation to LoggedOnTime. This field is
                                          						a calculated field, derived from: Agent_Skill_Group_Interval.TalkTime +
                                          						Agent_Interval.NotReadyTime + Agent_Skill_Group_Interval. HoldTime
                                          						) * 1.0 / Agent_Interval.LoggedOnTime |
| Internal | The
                                          						number of internal tasks agents across skill groups ended during the interval. Derived
                                          						from: Agent_Skill_Group_Interval.InternalCalls |
| Internal
                                          						Time | The
                                          						total number of seconds an agent across skill groups spent on internal tasks
                                          						that ended during the reporting interval. Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime |
| Wrap Up Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval. Derived from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime |
| Agent
                                          						Ring Time | How
                                          						long an agent is in Reserved state. This value  is counted using Agent state. Derived from: Agent_Skill_Group_Interval.ReservedStateTime |
| Not
                                          						Ready Time | The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. This value is taken directly from the database. Derived from: Agent_Interval.NotReadyTime. |
| Available
                                          						Time | The
                                          						total time in seconds an agent was in the Not_Active state across skill groups
                                          						during the reporting interval. AvailTime is included in the calculation of
                                          						LoggedOnTime. Derived from: Agent_Interval.AvailTime |
| Logged on Time | The
                                          						total time during the interval the agent was logged in, measured in HH:MM:SS
                                          						(hours, minutes, seconds) format. Derived from: Agent_Interval.LoggedOnTime |
| Transferred | The
                                          						number of tasks this agent transferred to another agent or skill group in the
                                          						interval. This number includes Consultative Calls if this transfer was
                                          						consultative-not blind. The number is updated at the time the agent completes
                                          						the transfer of the task. This
                                          						is a calculated field, derived from: Agent_Skill_Group_Interval.TransferredOutCalls +
                                          						Agent_Skill_Group_Interval.NetTransferredOutCalls |
| Held | The
                                          						number of incoming tasks to this agent that were placed on hold in the
                                          						interval. Derived from: Agent_Skill_Group_Interval.IncomingCallsOnHold |
| Avg
                                          						Hold Time | The
                                          						average time in HH:MM:SS (hours, minutes, seconds) that tasks were put on hold
                                          						in the interval, for all incoming tasks that included hold time. This field
                                          						is a calculated field, derived from: (Agent_Skill_Group_Interval. IncomingCallsOnHoldTime /
                                          						Agent_Skill_Group_Interval.IncomingCallsOnHold) |

| Report | View |
|---|---|
| Agent Team Historical | Agent Team Historical Agent Team Interval Historical |
| Agent Team Weekly Historical | Agent Team Weekly Historical |
| Agent Team Monthly Historical | Agent Team Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Team Name | The
                                          						Enterprise Name of the agent team. Derived
                                          						from: Agent_Team.EnterpriseName |
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| Date/Date Time/Week/Month | The date, interval, week, or month, depending on the
                                          						view/report selected. Derived from: Agent_Skill_Group_Interval.DateTime |
| Year (Appears only in Monthly report.) | The year of the selected row's data. Derived from: Agent_Skill_Group_Interval.DateTime |
| Handled | The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents across skill groups during the interval. Derived
                                          						from: Agent_Skill_Group_Interval.CallsHandled |
| Handle Time | The
                                          						total number of seconds spent on inbound tasks that have been answered and have
                                          						completed wrap-up by agents across skill groups during the interval Derived from: Agent_Skill_Group_Interval.HandledCallsTime |
| Avg
                                          						Handle Time | The
                                          						average time spent by the agent in handling a task, measured in HH:MM:SS
                                          						(hours, minutes, seconds). This field is
                                          						a calculated field, derived from: (Agent_Skill_Group_Interval.HandledCallsTime /
                                          						Agent_Skill_Group_Interval.CallsHandled) |
| Avg Wrap
                                          						Time | The
                                          						average time spent by the agent in after task work time, measured in HH:MM:SS
                                          						(hours, minutes, seconds). This field is
                                          						a calculated field, derived from: Agent_Skill_Group_Interval.WrapTime /
                                          						Agent_Skill_Group_Interval.CallsHandled |
| %Occupancy | The
                                          						percentage of time that the agent has spent talking on tasks across skill
                                          						groups in relation to LoggedOnTime. This field is
                                          						a calculated field, derived from: Agent_Skill_Group_Interval.TalkTime +
                                          						Agent_Skill_Group_Interval.WrapTime + Agent_Skill_Group_Interval.NotReadyTime +
                                          						Agent_Skill_Group_Interval. HoldTime )* 1.0 / Agent_Interval.LoggedOnTime |
| %Occupancy Without Wrap Time | The
                                          						percentage of time that the agent has spent talking on tasks across skill
                                          						groups in relation to LoggedOnTime. This field is
                                          						a calculated field, derived from: Agent_Skill_Group_Interval.TalkTime +
                                          						Agent_Skill_Group_Interval.NotReadyTime + Agent_Skill_Group_Interval. HoldTime)
                                          						* 1.0 / Agent_Interval.LoggedOnTime |
| Internal | The
                                          						number of internal tasks agents across skill groups ended during the interval. Derived
                                          						from: Agent_Skill_Group_Interval.InternalCalls |
| Internal
                                          						Time | The
                                          						total number of seconds an agent spent on internal tasks (across skill groups)
                                          						that ended during the reporting interval. Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime |
| Wrap Up
                                          						Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval. Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group.WorkReadyTime |
| Agent
                                          						Ring Time | How long
                                          						an agent is in Reserved state. This value is counted using Agent state. Derived
                                          						from: Agent_Skill_Group_Interval.ReservedStateTime |
| Not
                                          						Ready Time | The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. This value is taken directly from the database. Derived
                                          						from: Agent_Interval.NotReadyTime. |
| Available
                                          						Time | The
                                          						total time in seconds an agent was in the Not_Active state across skill groups
                                          						during the reporting interval. AvailTime is included in the calculation of
                                          						LoggedOnTime. Derived
                                          						from: Agent_Interval.AvailTime |
| Logged On Time | The
                                          						total time that the agents were logged in (staffed) for the specified time
                                          						period in any split/skill, measured in HH:MM:SS (hours, minutes, seconds)
                                          						format. Derived
                                          						from: Agent_Skill_Group_Interval.LoggedOnTime |

| Report | View |
|---|---|
| Agent Team Attendance Historical | Agent Team Attendance Historical Agent Team Attendance Interval Historical |
| Agent Team Attendance Weekly Historical | Agent Team Attendance Weekly Historical |
| Agent Team Attendance Monthly Historical | Agent Team Attendance Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Team Name | The
                                          						enterprise name for the Agent Team Name. Derived
                                          						from: Agent_Team.EnterpriseName |
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| Date/Date Time/Week/Month | The
                                          						interval, date, week, or month, depending on the view/report selected. Derived from: Agent_Skill_Group_Interval.DateTime |
| Year (Appears only in Monthly report.) | The year of the selected row's data. Derived from: Agent_Skill_Group_Interval.DateTime |
| Name | The
                                          						login name for the Agent. Derived
                                          						from: Person.LoginName |
| Logged on Time | The
                                          						total time during the interval the agent was logged in, measured in HH:MM:SS
                                          						(hours, minutes, seconds) format. Derived
                                          						from: Agent_Interval.LoggedOnTime |
| Handled | The
                                          						tasks handled by the particular agent. Derived from:
                                          						SUM(ISNULL(Agent_skill_Group_Interval.CallsHandled, 0)) |
| Handle Time | The
                                          						total time the agent spent handling tasks. Derived
                                          						from: SUM(ISNULL(Agent_skill_Group_Interval.HandledCallsTime, 0)) |
| Wrap Up
                                          						Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval. Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime |
| Agent
                                          						Ring Time | How long
                                          						an agent is in Reserved state. This value is counted using Agent state. Derived
                                          						from: Agent_Skill_Group_Interval.ReservedStateTime |
| Internal | The
                                          						number of internal tasks handled by the agent. Derived from: Agent_Skill_Group_Interval.InternalCalls |
| Internal
                                          						Time | The
                                          						total number of seconds an agent spent on internal tasks (across skill groups)
                                          						that ended during the reporting interval. Derived
                                          						from: Agent_Skill_Group_Interval.InternalCallsTime |
| External | The
                                          						outgoing tasks handled by the particular agent. Derived from:
                                          						SUM(ISNULL(Agent_skill_Group_Interval.AgentOutCalls, 0)) |
| External Time | The
                                          						outgoing tasks time for the particular agent. Derived
                                          						from: SUM(ISNULL(Agent_skill_Group_Interval.AgentOutCallsTime, 0)) |
| Available
                                          						Time | The
                                          						total time in seconds an agent was in the Not_Active state across skill groups
                                          						during the reporting interval. AvailTime is included in the calculation of
                                          						LoggedOnTime. Derived
                                          						from: Agent_Interval.AvailTime |
| Not
                                          						Ready Time | The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. This value is taken directly from the database. Derived
                                          						from: Agent_Interval.NotReadyTime. |

| Report | View |
|---|---|
| Call Type Skill Group Historical | Call Type Skill Group Historical Call Type Skill Group Interval Historical |
| Call Type Skill Group Weekly Historical | Call Type Skill Group Weekly Historical |
| Call Type Skill Group Monthly Historical | Call Type Skill Group Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Call
                                          						Type Name | The
                                          						enterprise name for the call type. Derived
                                          						from: Call_Type.EnterpriseName |
| Precision Queue/Skill Group | The
                                          						enterprise name for the Skill Group. Derived
                                          						form: Skill_Group.EnterpriseName |
| Date/Date Time/Week/Month | The date, interval, week, or month, depending on the
                                          						view/report selected. Derived
                                          						from: Call_Type.DateTime |
| Year (Appears only in Monthly report.) | The year of the selected row's data. Derived from: Call_Type_SG_Interval.DateTime |
| Inbound | Tasks
                                          						that have been offered to this call type during the interval. Derived
                                          						from: sum(isnull(Call_Type_SG_Interval.CallsOffered,0)) |
| Avg
                                          						Speed of Answer | The average answer wait time from when first queue to skill group or LAA select node was run for this call to when this call
                                          was answered. This field is
                                          						a calculated field derived from: CASE WHEN sum(isnull(Call_Type_SG_Interval.CallsAnswered,0)) = 0
 THEN 0
 ELSE sum(isnull(Call_Type_SG_Interval.AnswerWaitTime,0)) * 1.0 / 
sum(isnull(Call_Type_SG_Interval.CallsAnswered,0))
END |
| %
                                          						Queued | The
                                          						percentage of all handled tasks of the call type that were queued in the
                                          						interval. This
                                          						field is a calculated field derived from: (Call_Type_SG_Interval.CallsQHandled / Call_Type_SG_Interval.CallsHandled). |
| Abandon in
                                          						Queue | The
                                          						total number of tasks abandoned while in VRU (that is, while undergoing
                                          						prompting or listening to voice menus options), tasks abandoned while queued to
                                          						skill group, and tasks abandoned at agent desktop. This value also includes
                                          						abandons for tasks that are not in the queue. Therefore, the number of tasks
                                          						abandoned at a VRU before being queued is TotalCallsAband minus
                                          						RouterCallsAbandToAgent and RouterCallsAbandQ. The number does not include short tasks. Derived
                                          						from: sum(isnull(Call_Type_SG_Interval.RouterCallsAbandQ, 0) |
| Avg Abandon
                                          						Time | The
                                          						average time of abandoned tasks for this call type measured in HH:MM:SS (hours,
                                          						minutes, seconds) format. This field is
                                          						a calculated field, derived from: CASE WHEN sum( isnull (Call_Type_SG_Interval.TotalCallsAband, 0)) = 0 THEN 0
 ELSE isnull ((sum( isnull (Call_Type_SG_Interval.DelayQAbandTime, 0)) / sum (isnull 
(Call_Type_SG_Interval.TotalCallsAband, 0))),0)
END |
| Handled | The
                                          						number of tasks handled across agents in the call type. Derived
                                          						from: sum(isnull(Call_Type_SG_Interval.CallsHandled,0)) |
| Avg
                                          						Handle Time | The
                                          						average time in HH:MM:SS (hours, minutes, seconds) it has taken to handle a
                                          						task. sum(isnull(Call_Type_SG_Interval.HandleTime,0)) /
                                          						sum(isnull(CTSG.CallsHandled,0)) |
| Avg Wrap
                                          						Time | The
                                          						average time spent across agents in the call type after call work time,
                                          						measured in HH:MM:SS (hours, minutes, seconds). This field is
                                          						a calculated field, derived from: CASE WHEN (sum(isnull(Call_Type_SG_Interval.HandleTime,0)) 
- sum(isnull(Call_Type_SG_Interval.TalkTime,0)) 
- sum(isnull(Call_Type_SG_Interval.HoldTime,0))) = 0
 THEN 0
 ELSE (sum(isnull(Call_Type_SG_Interval.HandleTime,0)) 
- sum(isnull(Call_Type_SG_Interval.TalkTime,0)) 
- sum(isnull(Call_Type_SG_Interval.HoldTime,0))) / sum(isnull(Call_Type_SG_Interval.CallsHandled,0))
END |
| Service Level | The
                                          						Service Level Type used to calculate Service level for the interval. Derived from: Call_Type_Interval.ServiceLevel. |
| Abandon
                                          						Within Service Level | The total number of tasks of this call type abandoned within the service level threshold during the interval. Valid for both Unified CCE and standard ACD targets that use translation routes. This field represents the calls that are abandoned at VRU. It includes the calls abandoned at the menu prompt, welcome prompt,
                                       and the queue. Derived from: Call_Type_Interval.ServiceLevelAband. |

| Report | View |
|---|---|
| Skill Daily Historical | Skill Daily Historical |
| Skill Interval Historical | Skill Historical |
| Skill Weekly Historical | Skill Weekly Historical |
| Skill Monthly Historical | Skill Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Skill
                                          						Group Name | The
                                          						enterprise skill group's enterprise name. Derived
                                          						from: Skill_Group.EnterpriseName |
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| Date/Date Time/Week/Month | The
                                          						date, interval, week, or month, depending on the report selected. Derived
                                          						from: Agent_Skill_Group_Interval.DateTime |
| Year (Appears only in Monthly report.) | The
                                          						year of the selected row's data. Derived from: Agent_Skill_Group_Interval.DateTime |
| Handled | The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents in the skill group during the interval. Derived
                                          						from: Agent_Skill_Group_Interval.CallsHandled |
| Handle Time | The
                                          						percentage of time,  in relation to LoggedOnTime, that the agent has spent in Wrap-up state after incoming or
                                          						outgoing tasks for each skill group. Derived from: Agent_Skill_Group_Interval.HandledCallsTime |
| Avg
                                          						Handle Time | The
                                          						average time spent by the agent in handling a task, measured in HH:MM:SS
                                          						(hours, minutes, seconds). This field is
                                          						a calculated field derived from: (Agent_Skill_Group_Interval.HandledCallsTime /
                                          						Agent_Skill_Group_Interval.CallsHandled) |
| Avg Wrap
                                          						Time | The
                                          						average time spent by the agent in after task work time, measured in HH:MM:SS
                                          						(hours, minutes, seconds). This field is
                                          						a calculated field, derived from: Agent_Skill_Group_Interval.WrapTime /
                                          						Agent_Skill_Group_Interval.CallsHandled |
| Wrap Up
                                          						Time | The
                                          						total time in HH:MM:SS (hours, minutes, seconds) that the agent spent in
                                          						wrap-up on incoming and outgoing tasks in the interval. Derived
                                          						from: Agent_Skill_Group_Interval.WorkNotReadyTime +
                                          						Agent_Skill_Group_Interval.WorkReadyTime |
| Agent
                                          						Ring Time | How long
                                          						an agent is in Reserved state. This value is counted using Agent state. Derived
                                          						from: Agent_Skill_Group_Interval.ReservedStateTime |
| Not
                                          						Ready Time | The
                                          						total time that the agents spent in Not Ready state for this skill for the
                                          						specified time period. This value is taken directly from the database. Derived
                                          						from: Agent_Interval.NotReadyTime. |
| Available
                                          						Time | The
                                          						total time in seconds an agent associated with this skill group was in the
                                          						Not_Active state with respect to this skill group during the reporting
                                          						interval. AvailTime is included in the calculation of LoggedOnTime. Derived
                                          						from: Agent_Interval.AvailTime |
| Logged On
                                          						Time | The
                                          						total time during the interval the agent was logged in, measured in HH:MM:SS
                                          						(hours, minutes, seconds) format. Derived from: Agent_Interval.LoggedOnTime |
| Assists | The
                                          						number of tasks for which an agent received supervisor assistance during the
                                          						report interval. This
                                          						is a calculated field, derived from: Agent_Skill_Group_Interval.Emergency Assists +
                                          						Agent_Skill_Group_Interval.SupervAssistCalls |
| Transferred | The
                                          						number of tasks this agent transferred to another agent or skill group in the
                                          						interval. This number includes Consultative Calls if this transfer was
                                          						consultative-not blind. The number is updated at the time the agent completes
                                          						the transfer of the task. This
                                          						is a calculated field, derived from: Agent_Skill_Group_Interval.TransferredOutCalls +
                                          						Agent_Skill_Group_Interval.NetTransferredOutCalls |
| Held | The
                                          						number of incoming tasks to this agent that were placed on hold in the
                                          						interval. Derived from: Agent_Skill_Group_Interval.IncomingCallsOnHold |
| Avg
                                          						Hold Time | The
                                          						average time in HH:MM:SS (hours, minutes, seconds) that tasks were put on hold
                                          						in the interval, for all incoming tasks that included hold time. This
                                          						field is a calculated field, derived from: (Agent_Skill_Group_Interval. IncomingCallsOnHoldTime /
                                          						Agent_Skill_Group_Interval.IncomingCallsOnHold) |

| Report | View |
|---|---|
| Skill Call Profile Historical | Skill Call Profile Historical Skill Call Profile Interval Historical |
| Skill Call Profile Weekly Historical | Skill Call Profile Weekly Historical |
| Skill Call Profile Monthly Historical | Skill Call Profile Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Skill
                                          						Group Name | The
                                          						enterprise skill group's enterprise name. Derived from: Skill_Group.EnterpriseName
                                          						(Skill_Group.EnterpriseSkillGroupID) |
| Date/Date Time/Week/Month | The
                                          						date, interval, week, or month, depending on the report selected. Derived
                                          						from: Skill_Group_Interval.DateTime |
| Year (Appears only in Monthly report.) | The
                                          						year of the selected row's data. 
                                          					 (Applicable only for monthly report.) Derived from: Skill_Group_Interval.DateTime |
| Handled | The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents in the skill group during the interval. Derived from: Skill_Group_Interval.CallsHandled |
| Avg
                                          						Speed Of Answer | The
                                          						average time the skill ACD tasks were waiting in queue and ringing before being
                                          						answered by an agent. Derived from: Skill_Group_Interval.AnswerWaitTime /
                                          						Skill_Group_Interval.CallsAnswered |
| %Answer | The
                                          						percentage of tasks queued to the skill that was answered by agents for this
                                          						skill. This
                                          						is a calculated field, derived from: Skill_Group_Interval.CallsHandled
                                          						/Skill_Group_Interval.CallsOffered |
| Abandon Calls | The
                                          						number of skill ACD tasks that abandoned within each service level increment. Derived
                                          						from: (Skill_Group_Interval.RouterCallsAbandQ +
                                          						RouterCallsAbandToAgent ) |
| Avg Abandon
                                          						Time | The
                                          						average time the skill ACD tasks were waiting in queue or ringing before
                                          						abandoning. Derived
                                          						from: Skill_Group_Interval.RouterDelayQAbandTime +
                                          						SGHH.AbandonRingTime/SGHH.RouterCallsAbandQ+SGHH.AbandonRingCal |
| %Abandon | The
                                          						percentage of tasks abandoned. This field is
                                          						a calculated field, derived from: (Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.AbandonCallsRing )/Skill_Group_Interval.CallsOffered |
| Abandon, 0-9 | The
                                          						number of abandoned tasks in each Bucket Interval. Derived from: Skill_Group_Interval.RouterAbandInterval |
| Answered, 0-9 | The
                                          						total number of answered tasks in each Bucket Interval. Derived from: Skill_Group_Interval.RouterAnsInterval |

| Report | View |
|---|---|
| Skill Summary Historical | Skill Summary Historical Skill Summary Interval Historical |
| Skill Summary Weekly Historical | Skill Summary Weekly Historical |
| Skill Summary Monthly Historical | Skill Summary Monthly Historical |

| Column
                                          						(Field) | Description |
|---|---|
| Skill
                                          						Group Name | The
                                          						enterprise skill group's enterprise name and ID. Derived
                                          						from: Enterprise_Skill_Group.EnterpriseName
                                          						(Enterprise_Skill_Group.EnterpriseSkillGroupID) |
| Date/Date Time/Week/Month | The
                                          						date, interval, week, or month, depending on the view/report selected. Derived from: Skill_Group_Interval.DateTime |
| Media (Appears only in Weekly report) | A unique name for this media class. Initially, the EnterpriseName is set to Cisco_Voice. |
| Year (Appears only in Monthly report.) | The
                                          						year of the selected row's data. Derived from: Skill_Group_Interval.DateTime |
| Avg
                                          						Speed Of Answer | The
                                          						average time the skill ACD tasks were waiting in queue and ringing before being
                                          						answered by an agent. Derived
                                          						from: Skill_Group_Interval.AnswerWaitTime / Skill_Group_Interval.CallsAnswered |
| Avg Abandon
                                          						Time | The
                                          						average time the split/skill ACD tasks were waiting in queue or ringing before
                                          						abandoning. Derived
                                          						from: Skill_Group_Interval.RouterDelayQAbandTime +
                                          						Skill_Group_Interval.AbandonRingTime / Skill_Group_Interval.RouterCallsAbandQ +
                                          						Skill_Group_Interval.AbandonRingCall |
| Handled | The
                                          						number of inbound tasks that have been answered and have completed wrap-up by
                                          						agents in the skill group during the interval. Derived
                                          						from: Skill_Group_Interval.CallsHandled |
| Avg
                                          						Handle Time | The
                                          						average time spent by the agent in handling a task, measured in HH:MM:SS
                                          						(hours, minutes, seconds). This field is
                                          						a calculated field derived from: (Skill_Group_Interval.HandledCallsTime /
                                          						Skill_Group_Interval.CallsHandled) |
| Avg Wrap
                                          						Time | The
                                          						average time spent by the agent in after task work time, measured in HH:MM:SS
                                          						(hours, minutes, seconds). This field is
                                          						a calculated field, derived from: Skill_Group_Interval.WrapTime /
                                          						Skill_Group_Interval.CallsHandled |
| Abandon | For
                                          						voice: the total number of tasks that were abandoned while the agent's phone
                                          						was ringing. For non-voice: the total number of tasks that were abandoned while
                                          						being offered to an agent. Derived
                                          						from: (Skill_Group_Interval.RouterCallsAbandQ + Skill_Group_Interval.RouterCallsAbandToAgent) |
| Max
                                          						Delay Time | The
                                          						longest a task had to wait before being answered, abandoned, or otherwise
                                          						ended. Derived
                                          						from: Skill_Group_Interval.RouterMaxCallsWaitTime |
| Dequeued | The
                                          						number of tasks that were dequeued from this skill group to be routed to
                                          						another skill group in the reporting interval. Derived
                                          						from: Skill_Group_Interval.RouterCallsDequeued |
| %
                                          						Handle Time | The
                                          						percentage of time on handled tasks. This
                                          						is a calculated field, derived from: Skill_Group_Interval.HandledCallsTime
                                          						/Skill_Group_Interval.LoggedOnTime |
| % Answer | The
                                          						percentage of answered tasks. This
                                          						field is a calculated field, derived from: Skill_Group_Interval.CallsHandled
                                          						/Skill_Group_Interval.CallsOffered |

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from:Person.LastName "," Person.FirstName |
| Extension | The
                                          						phone extension into which the agent is logged. Taken directly from the table. Derived from: Agent_Logout.Extension |
| Logged On DateTime | The date that the agent logged on to the given set of skills, measured in MM:DD:YYYY (month, day, year) and HH:MM:SS (hours,
                                          minutes, seconds) format. Derived from: Agent_Logout.LogoutDateTime-Agent_Logout.LoginDuration |
| Logout
                                          						DateTime | The
                                          						date that the agent logged out from the given set of skills, measured in
                                          						MM:DD:YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format. Derived from: Agent_Logout.LogoutDateTime |
| Logged On Time | The
                                          						total time that the agents were logged in (staffed) for the specified time
                                          						period in any split/skill, measured in HH:MM:SS (hours, minutes, seconds)
                                          						format. Derived
                                          						from: Agent_Skill_Group_Interval.LoggedOnTime |
| Logout
                                          						Reason | A code
                                          						and text (if configured) from the peripheral that indicates the reason for the
                                          						agent's last state change. If not defined, this value displays 0. Derived
                                          						from: Agent_Logout.Reason_Code |
| Attribute, 1 to 3 | The
                                          						attributes with which the agent primarily interacted during this session. |
| Skill,
                                          						1 to 3 | The
                                          						skills with which the agent primarily interacted during this session. Derived
                                          						from: Agent_Skill_Group_Logout.SkillGroupSkillTargetID |

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
| RC50002 | Not Ready Time spent in 50002. A CTI OS component failed, causing the agent to be set to Not Ready. This could be due to closing
                                          the agent desktop application, heartbeat timeout, a CTI OS Server failure, or a CTI OS failure. |
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

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Name | The
                                          						first name and last name of the agent. Derived
                                          						from: Person.LastName "," Person.FirstName |
| Precision Queue / Skill Group | The
                                          						Skill Group or the Precision Queue associated with an agent for the
                                          						corresponding Agent State. Derived
                                          						from: Skill_Group.EnterpriseName |
| DateTime | The date
                                          						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                          						HH:MM:SS (hours, minutes, seconds) format. Derived
                                          						from: Agent_Skill_Group_Interval.DateTime |
| Agent
                                          						State | The
                                          						state for the Agent. Derived
                                          						from: CASE Agent_State_Trace.AgentState 
WHEN 0 THEN 'Logged Out' 
WHEN 1 THEN 'Logged On' 
WHEN 2 THEN 'Not Ready' 
WHEN 3 THEN 'Ready' 
WHEN 4 THEN 'Talking' 
WHEN 5 THEN 'Work Not Ready' 
WHEN 6 THEN 'Work Ready' 
WHEN 7 THEN 'Busy Other' 
WHEN 8 THEN 'Reserved' 
WHEN 9 THEN 'Unknown' 
WHEN 10 THEN 'Hold' 
WHEN 11 THEN 'Active' 
WHEN 12 THEN 'Paused' 
WHEN 13 THEN 'Interrupted' 
WHEN 14 THEN 'Not Active' 
ELSE CONVERT(VARCHAR, Agent_State_Trace.AgentState) 
END |
| Logout
                                          						Reason | The
                                          						reason why an agent logged out. Derived
                                          						from: CASE WHEN Agent_State_Trace.EventName=2 THEN 
  (SELECT ReasonText FROM Reason_Code WHERE Deleted='N' andReasonCode=Agent_State_Trace.ReasonCode)
    ELSE 'None' 
END |
| Not
                                          						Ready Reason | The
                                          						reason why an agent is in a Not Ready state. Derived
                                          						from: CASE WHEN Agent_State_Trace.EventName=3 THEN 
   SELECT ReasonText FROM Reason_Code WHERE Deleted='N' and ReasonCode=Agent_State_Trace.ReasonCode)
    ELSE 'None' 
END |
| Media | The
                                          						enterprise name for the Domain. Derived
                                          						from: Media_Routing_Domain.EnterpriseName |
| Direction | The
                                          						direction of the task. Derived
                                          						from: CASE WHEN AST.Direction=1 THEN 'In'
WHEN AST.Direction = 2 THEN 'Out'
WHEN AST.Direction = 3 THEN 'Other In'
WHEN AST.Direction = 4 THEN 'Other Out'
WHEN AST.Direction = 5 THEN 'Out Reserve'
WHEN AST.Direction = 6 THEN 'Out Preview'
WHEN AST.Direction = 7 THEN 'Out Predictive'
   ELSE 'None'
END |
| Peripheral Call Key | The key
                                          						assigned by the peripheral to the task associated with the event. Derived
                                          						from: ISNULL(Agent_State_Trace.PeripheralCallKey,0) |
| Router
                                          						Call Key | This
                                          						field is not set for tasks. Derived
                                          						from: ISNULL(Agent_State_Trace.RouterCallKey,0) |
| Router
                                          						Call Key Day | This
                                          						field is not set for tasks. Derived from: ISNULL(Agent_State_Trace.RouterCallKeyDay,0) in
                                          						the calculation of LoggedOnTime. |
| Router
                                          						Call Key Sequence Number | This
                                          						field is not set for tasks. Derived from: ISNULL(Agent_State_Tra
                                          						ce.RouterCallKeySequenceNumber,0) |

| Column
                                          						(Field) | Description |
|---|---|
| Agent
                                          						Team Name | The
                                          						Enterprise Name of the agent team. Derived
                                          						from: Agent_Team. EnterpriseName |
| Agent
                                          						Name | The
                                          						first and last name of the agent. Derived
                                          						from Person. LastName ", 
                                             						" Person. FirstName |
| DateTime | The date
                                          						and time of the selected row's data in MM/DD/YYYY (month, day, year) and
                                          						HH:MM:SS (hours, minutes, seconds) format. Derived
                                          						from: Agent_Skill_Group_Interval. DateTime |
| Logged On
                                          						Time | The
                                          						total time that the agents were logged in (staffed) for the specified time
                                          						period in any split/skill, measured in HH:MM:SS (hours, minutes, seconds)
                                          						format. Derived
                                          						from: Agent_Skill_Group_Interval. LoggedOnTime |
| Not
                                          						Ready Time | The
                                          						total time that the agents spent in Not Ready state in all splits/skills for
                                          						the specified time period. Value taken directly from the database. Derived
                                          						from: Agent_Interval. NotReadyTime |
| Time in |
| RC0 to RC9 | The time
                                          						that the agent spent in Not Ready state with each of the reason codes 0 - 9. Derived
                                          						from: Agent_Event_Detail |
| RC50002 | Not
                                          						Ready Time spent in 50002; a CTI OS component failed, causing the agent to be
                                          						logged out. This could be due to closing the agent desktop application,
                                          						heartbeat timeout, a CTI OS Server failure, or a CTI OS failure. |
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