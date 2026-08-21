---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-report-e86045a3ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_Reporting-User-Guide-12_6_1/pcce_b_cisco-packaged-contact-center-enterprise_chapter_010111.html
retrieved_at: 2026-08-21T16:57:11.222035+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

Updated: May 10, 2021

Chapter: Live Data Report Templates

## Chapter: Live Data Report Templates

# Live Data Report Templates

## Live Data Report
                        	 Templates

The Live Data
                           		reports derive their data from a stream processing system that continuously
                           		pushes data to the reporting clients so reports can be updated as the events
                           		occur.

Live Data
                           		continuously processes agent and call events from the peripheral gateway and
                           		the router, and publishes data directly to Unified Intelligence Center. Live
                           		Data continuously pushes only changed data to the reporting clients without the
                           		delay of writing to, and reading from the database. Individual state values,
                           		such as agent states, refresh as they happen. Other values, such as calls in
                           		queue, refresh approximately every 3 seconds.

- Add or remove columns from
                                 		  the grid view using a checkbox UI

- Disable and enable
                                 		  auto-refresh to view a snapshot of the system activity without updates

- Enable and disable Show
                                 		  Thresholds Only. When enabled, only data configured with threshold values are
                                 		  displayed in the report.

## Live Data
                        	 Failover

Live Data reports
                              		  can be viewed as gadgets in the Cisco Finesse desktop and on the report viewer
                              		  in Unified Intelligence Center. Live Data failover occurs when any of the
                              		  following fails:

Live Data
                                    				Socket.IO Service

Network
                                    				Connectivity

Live Data Web
                                    				Service

Unified CCE Live Data NGINX Service

“Live Data is not availab le after repeated attempts. Retrying” message is displayed during failover when the gadget and the report viewer aren’t able to connect to the primary and secondary
                              Live Data server. The gadget and Unified Intelligence Center continue to retry until it connects to one of the servers and
                              regain updates to the reports.

The Live Data gadget fails to load if the Intelligence Center Reporting Service is unavailable when the Live Data gadget is
                              being rendered. If the service is unavailable after the gadget is rendered, it has no effect. By configuring the alternateHosts attribute to have a fallback Cisco Unified Intelligence Center VM host name, you can achieve failover for the Intelligence
                              Center Reporting Service. For more information, see the alternateHosts Configuration section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

## Agent

Data Source: This report displays attributes published by the Live Data Reporting System, which continuously processes events from the
                              Router and Agent Peripheral Gateway. The Live Data system updates the report's individual attributes as the events occur.

Views: This report has the following grid views:

Agent

Agent Names All Fields

Select the view you want to see from the report drop-down list that is located on the top left corner.

Grouping: Grouping is not supported in Live Data reports.

### Agent View

#### Current Fields in the Agent View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

Columns (Fields)

Description

Agent Name

The name of the agent. This field is composed of Last Name and First Name.

State

The
                                             						current state of the agent:

Logged Out

Logged On

Not Ready

Ready

Talking

Work Not Ready

Work Ready

Busy Other

Reserved

Unknown

Hold

Active

Paused

Interrupted

Not Active

Reason

The reason code and text indicating the reason the agent entered the Not Ready state.

Note: If an agent is Not Ready, the Not Ready reason code and text are only updated when the agent goes to Ready or to another Not Ready state with a different Reason code. If the Not Ready agent receives an internal call or makes an outbound call, Reason continues
                                             to show the current Not Ready code and text.

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

Domain

The
                                             						media routing domain name.

Direction

The
                                             						direction of the call that the agent is currently working on:

In

Out

Other In

Other Out

Out Reserve

Out Preview

Out Predictive

Not Applicable

(if the logged in agent is not active in the skill group)

Precision Queue/Skill Group

The enterprise name of the precision queue or the skill group associated with the task on which the agent is currently working.
                                             If the agent is not involved in any task in the media routing domain, this field shows Not Applicable . Because an agent can be logged into multiple skill groups, this field is not filled until the agent is assigned a task.

If not
                                             						applicable, the column is left blank.

Attributes

The
                                             						names of the attributes used in the precision queue definition. The report
                                             						shows only those attributes that are used.

Reason Code

A code received from the peripheral that indicates the reason for the agent's last state change. If not defined, Reason is
                                             None.

### Agent Live Data
                           	 Available Fields

Available fields are
                                 		  the fields that are visible in the All Fields view. You can use the column
                                 		  selection tool to add or remove fields from the report.

Report
                                             						Field

Description

Agent
                                             						Name

The name
                                             						of the agent. Composed of Last Name, First Name.

Team
                                             						Name

The
                                             						Enterprise Name of the Agent Team.

State

The
                                             						current state of the agent:

- Logged Out

- Logged On

- Not Ready

- Ready

- Talking

- Work Not Ready

- Work Ready

- Busy Other

- Reserved

- Unknown

- Hold

- Active

- Paused

- Interrupted

- Not Active

Reason

The
                                             						reason code and text indicating the reason the agent entered the Not Ready
                                             						state.

Note: If an agent is
                                             						Not Ready, the Not Ready reason code and text are only updated when the agent
                                             						goes to Ready or to another Not Ready state with a different Reason code. If
                                             						the Not Ready agent receives an internal call or makes an outbound call, Reason
                                             						continues to show the current Not Ready code and text.

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

Precision Queue/Skill Group

The
                                             						enterprise name of the precision queue or the skill group associated with the
                                             						task on which the agent is currently working. If the agent is not involved in
                                             						any task in the media routing domain, this field shows Not Applicable. Because
                                             						an agent can be logged into multiple skill groups, this field is not filled
                                             						until the agent is assigned a task.

Router Calls Queued Now

The number
                                             						of calls currently queued at the router.

Longest Call in Queue

The
                                             						length of time the longest queued call on the routing media has been queued,
                                             						measured in HH:MM:SS (hours, minutes, seconds) format.

Domain

The
                                             						media routing domain name.

Direction

The
                                             						direction of the call that the agent is currently working on:

Not
                                                   							 Applicable

In
                                                   							 (inbound task - non voice tasks are always inbound).

Out
                                                   							 (outgoing external task).

Other (outgoing or incoming internal task).

Not
                                                   							 Applicable (if the logged in agent is not active in the skill group).

Destination

The type
                                             						of outbound task on which the agent is currently working:

- 1 = ACD

- 2 = Direct

- 3 = Auto Out

- 4 = Reserve

- 5 = Preview

- All other values = Not
                                                						  Applicable

Routable

Calls
                                             						can be routed to the agent:

- 1 = Yes

- All other values = No

Tasks
                                             						in Progress

The
                                             						number of tasks currently queued for the skill group.

Max
                                             						Tasks

The
                                             						maximum number of tasks that may be assigned to an agent.

Device
                                             						Type

- 0 = Local agent; normal
                                                   						  ACD/Unified CCE phone or non-voice task.

- 1 = Remote phone, call by
                                                   						  call (Mobile agent's phone is connected for each incoming call).

- 2 = Remote phone, nailed
                                                   						  connection (Mobile agent calls and logs in once; line remains connected through
                                                   						  multiple calls).

Available in MRD

Whether or not the agent is available to accept a task in this
                                             						Media Routing Domain:

- NO (Not available)

- YES_ICM (Unified ICM
                                                						  available in media routing domain)

- YES_APP (Application
                                                						  available in media routing domain)

- All other values = No

An
                                             						agent is available for a task in a media routing domain (MRD) if the agent's
                                             						state in that MRD is anything other than Not Ready; the agent is not at the
                                             						agent's maximum task limit for the MRD; and the agent is not working on a
                                             						non-interruptible task in another MRD. If an agent is Unified ICM-available,
                                             						then the Unified ICM can assign tasks to the agent. If an agent is
                                             						Application-available, then the application can assign tasks to the agent. In
                                             						the former case, only the Unified ICM can assign tasks to the agent. In the
                                             						latter, only the application can assign tasks to the agent.

Request Supervisor Assist

Whether or not the agent requested supervisor assistance:

- 1 = Yes

- All other values = No

Precision Queue Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

Extension

The
                                             						phone extension into which the agent is logged.

Remote
                                             						Address

The
                                             						remote address associated with this MRD (remote extension used for Mobile
                                             						Agents).

Last
                                             						Level Change

The
                                             						date and time of the agent's last task level change in this MRD.

Chat
                                             						agents have a maximum number of open slots. The task level changes when the
                                             						number of open slots changes as a result of the number of calls in progress
                                             						changing (the number of open slots = the maximum number of tasks - calls in
                                             						progress).

This
                                             						applies to all other agents as well; however, the task level is always 0 or 1.

Last
                                             						Mode Change

The
                                             						date and time of the agent last mode change in this MRD.

An
                                             						agent has a mode with respect to each Media Routing Domain the agent is logged
                                             						in to. These modes are either routable or not routable.

If the mode is routable,
                                             						the Unified ICM controls the agent and assigns tasks to the agent. When an
                                             						agent is routable for an MRD, an application instance (for example, Enterprise Chat and
                                                   						Email )
                                             						will not allow the agent to work on a task unless Unified ICM assigns the task.

If the mode is not
                                             						routable, the application instance controls the agent and assigns tasks to the
                                             						agent. The software tracks the agent activity by monitoring Offer Task, Start
                                             						Task, and other messages from the application that describe the task the agent
                                             						is working on.

For Enterprise Chat and
                                                   						Email ,
                                             						an agent mode never changes. Each agent is always routable.

An
                                             						agent mode is always routable with respect to the voice MRD.

Last
                                             						State Change

The
                                             						date and time of the agent's last state change in this MRD.

Login

The
                                             						date and time that the agent logged in. The format is MM/DD/YYYY (month, day,
                                             						year) and HH:MM:SS (hours, minutes, seconds) format.

Reason Code

A code
                                             						received from the peripheral that indicates the reason for the agent's last
                                             						state change. If not defined, Reason is None.

## Agent Summary Report

This report presents agent statistics for each Agent in real time.

Data Source: This report displays the attributes that are published by the Live Data Reporting System, which continuously processes events
                              from the Agent Peripheral Gateway. The Live Data Reporting System updates the individual attributes of the report as and when
                              the events occur.

Views : This report has the following grid views:

Agent Summary

Agent Summary All Fields

Grouping : Grouping is not supported in Live Data reports.

### Agent Summary

#### Current Fields in the Agent Summary

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

The agent statistics that are displayed in this report resets during midnight at Peripheral Gateway.

This report displays the statistics on daily basis.

You can use the column selection tool to add or remove fields from the report.

For more information on the fields and desciptons see, AgentState section in Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html

Columns (Fields)

Description

Agent

The name of the agent, which includes the first and the last name of the agent.

State

The state of the agent.

For more information, see AgentState section in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at. https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html

Logged On Time

Total time, in seconds, the agent has been logged on. For this time to be accurate, ensure that time on the client machine
                                             is set correctly as per the timezone.

Not ReadyTime

The total time that the agent spent in Not Ready state. For this time to be accurate, ensure that time on the client machine
                                             is set correctly as per the timezone.

Ready Time

The total time that the agent spent in Ready state. For this time to be accurate, ensure that time on the client machine is
                                             set correctly as per the timezone.

% Not Ready Time

The percentage of time that the agent has spent in Not Ready state with respect to the total Logged On Time.

Handled Calls

The number of inbound calls that were answered and have completed wrap-up by the agent.

Avg Handled Calls Time

Average handle time in seconds, for inbound ACD calls counted as handled by the agent. The time that agent spent on the call
                                             to the time the agent wrap-up the work on the call. Includes hold time that is associated with the call.

Avg Handled Calls Talk Time

Average talk time, in seconds, for Inbound ACD calls counted as handled by the agent.

Avg Handled Calls Held Time

Average held time, in seconds, for Inbound ACD calls counted as handled by the agent.

Avg Wrap-UpTime

The average length of time the agents spent in wrap-up work.

Total Wrap-UpTime

The total number of seconds agents spent in wrap-up work.

%Wrap-UpTime

The percentage of time that agents spent in the wrap-up state.

Other On PhoneTime

Total time the agent spent on Other calls.

### Agent Summary All Fields

#### Current Fields in the All Fields View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

All Fields are the fields that are visible in the All Fields view. You can use the column selection tool to add or remove fields from
                                 the report.

Columns (Fields)

Description

Agent

The name of the agent, which includes the first and the last name of the agent.

MR Domain Name

The media routing domain name.

State

The state of the agent.

For more information, see AgentState section in Database Schema Handbook for Cisco Unified Contact Center Enterprise at. https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Logged OnTime

Total time, in seconds, the agent has been logged on. For this time to be accurate, ensure that time on the client machine
                                          is set correctly as per the timezone.

Not Ready Time

The total time that the agent spent in Not Ready state. For this time to be accurate, ensure that time on the client machine
                                          is set correctly as per the timezone.

Ready Time

The total time that the agent spent in Ready state. For this time to be accurate, ensure that time on the client machine is
                                          set correctly as per the timezone.

Handled Calls

The number of inbound calls that were answered and have completed wrap-up by the agent.

Handled Calls Time

Total handle time, in seconds, for inbound ACD calls counted as handled by the agent. The time that is spent from the call
                                          being answered by the agent to the time the agent wrap-up time for the call. Includes hold time associated with the call.

Handled Calls Talk Time

Total talk time in seconds, for Inbound ACD calls counted as handled by the agent.

Handled Calls Held

The total number of completed inbound ACD call agent placed on hold at least once.

Handled Calls Held Time

Total number of seconds completed inbound ACD calls were placed on hold.

Wrap-UpTime

The length of time the agent spent in wrap-up work.

Auto Out Calls

Total number of AutoOut (predictive) calls completed by the agent.

Auto Out Calls Time

Total handle time, in seconds, for completed AutoOut (predictive) calls handled by the agent. The value includes the time
                                          that is spent from the call being initiated to the time the agent wrap-up time for the call. The time includes hold time associated
                                          with the call.

Auto Out Calls Talk Time

Total talk time, in seconds, for completed AutoOut (predictive) calls handled by the agent.

Auto Out Calls Held Time

Total time, in seconds, for AutoOut (predictive) calls were placed on hold by the agent.

Auto Out Calls Held

The total number of completed AutoOut (predictive) calls that the agent has placed on hold at least once.

Agent Out Calls

Total number of completed outbound ACD calls made by the agent.

Agent Out Calls Time

Total handle time, in seconds, for completed outbound ACD calls handled by the agent. The value includes the time that is
                                          spent from the call being initiated by the agent to the time the agent wrap-up time for the call. The time includes hold time
                                          associated with the call.

Agent Out Calls Talk Time

Total talk time, in seconds, for completed outbound ACD calls handled by the agent.

Agent Out Calls Held

The total number of completed outbound ACD calls that the agent has placed on hold at least once.

Agent Out Calls Held Time

Total time, in seconds, the calls were placed on hold by the agent.

Internal Calls

Number of internal calls initiated by the agent.

Internal Calls Time

Total time, in seconds, spent on internal calls initiated by the agent.

Internal Calls Rcvd

Number of internal calls received by the agent.

Internal Calls Rcvd Time

Total time, in seconds, spent on internal calls received by the agent.

Internal Calls Held

The total number of internal calls the agent placed on hold at least once.

Internal Calls Held Time

Total time, in seconds, the completed internal calls that were placed on hold.

Preview Calls

Total number of outbound Preview calls completed by the agent.

Preview Calls Time

Total handle time, in seconds, for outbound Preview calls completed by the agent. The value includes the time that is spent
                                          from the call being initiated to the time the agent wrap-up time for the call. The time includes hold time associated with
                                          the call.

Preview Calls Talk Time

Total talk time, in seconds, of outbound Preview calls completed by the agent.

Preview Calls Held

The total number of completed outbound Preview calls the agent has placed on hold at least once.

Preview Calls Held Time

Total time, in seconds, for which outbound Preview calls were placed on hold.

Reserve Calls

For Outbound Option, the number of reservation calls received by an agent in this skill group during the reporting interval.

Reserve Calls Time

For Outbound Option, the time during the reporting interval that an outbound agent in this skill group spent on reservation
                                          calls waiting for the Campaign customer call to be delivered. This includes preview time for Preview, Direct Preview, and
                                          Personal Callback calls.

Reserve Calls Talk Time

For Outbound Option, the talk time for an agent in this skill group on reservation calls during the reporting interval. This
                                          is calculated using Call State.

Reserve Calls Held

For Outbound Option, the number of reservation calls for an agent in this skill group placed on hold during the reporting
                                          interval.

Reserve Calls Held Time

For Outbound Option, the time that reservation calls for an agent in this skill group are on hold during the reporting interval.

Non-ACD Call in Count

Total number of incoming calls received by the agent on Non-ACD line.

Non-ACD Call in Time

Total time in seconds, spent by the agent on a Non-ACD call.

Non-ACD Call Out Count

Total number of out going calls by the agent on Non-ACD line.

Non-ACD Call OutTime

Total time, in seconds, spent by the agent on a Non-ACD outbound call.

### Agent Summary

#### Current Fields in the Agent Summary

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

The agent statistics that are displayed in this report resets during midnight at Peripheral Gateway.

This report displays the statistics on daily basis.

You can use the column selection tool to add or remove fields from the report.

For more information on the fields and desciptons see, AgentState section in Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html

Columns (Fields)

Description

Agent

The name of the agent, which includes the first and the last name of the agent.

State

The state of the agent.

For more information, see AgentState section in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at. https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html

Logged On Time

Total time, in seconds, the agent has been logged on. For this time to be accurate, ensure that time on the client machine
                                             is set correctly as per the timezone.

Not ReadyTime

The total time that the agent spent in Not Ready state. For this time to be accurate, ensure that time on the client machine
                                             is set correctly as per the timezone.

Ready Time

The total time that the agent spent in Ready state. For this time to be accurate, ensure that time on the client machine is
                                             set correctly as per the timezone.

% Not Ready Time

The percentage of time that the agent has spent in Not Ready state with respect to the total Logged On Time.

Handled Calls

The number of inbound calls that were answered and have completed wrap-up by the agent.

Avg Handled Calls Time

Average handle time in seconds, for inbound ACD calls counted as handled by the agent. The time that agent spent on the call
                                             to the time the agent wrap-up the work on the call. Includes hold time that is associated with the call.

Avg Handled Calls Talk Time

Average talk time, in seconds, for Inbound ACD calls counted as handled by the agent.

Avg Handled Calls Held Time

Average held time, in seconds, for Inbound ACD calls counted as handled by the agent.

Avg Wrap-UpTime

The average length of time the agents spent in wrap-up work.

Total Wrap-UpTime

The total number of seconds agents spent in wrap-up work.

%Wrap-UpTime

The percentage of time that agents spent in the wrap-up state.

Other On PhoneTime

Total time the agent spent on Other calls.

### Agent Summary All Fields

#### Current Fields in the All Fields View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

All Fields are the fields that are visible in the All Fields view. You can use the column selection tool to add or remove fields from
                                 the report.

Columns (Fields)

Description

Agent

The name of the agent, which includes the first and the last name of the agent.

MR Domain Name

The media routing domain name.

State

The state of the agent.

For more information, see AgentState section in Database Schema Handbook for Cisco Unified Contact Center Enterprise at. https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Logged OnTime

Total time, in seconds, the agent has been logged on. For this time to be accurate, ensure that time on the client machine
                                          is set correctly as per the timezone.

Not Ready Time

The total time that the agent spent in Not Ready state. For this time to be accurate, ensure that time on the client machine
                                          is set correctly as per the timezone.

Ready Time

The total time that the agent spent in Ready state. For this time to be accurate, ensure that time on the client machine is
                                          set correctly as per the timezone.

Handled Calls

The number of inbound calls that were answered and have completed wrap-up by the agent.

Handled Calls Time

Total handle time, in seconds, for inbound ACD calls counted as handled by the agent. The time that is spent from the call
                                          being answered by the agent to the time the agent wrap-up time for the call. Includes hold time associated with the call.

Handled Calls Talk Time

Total talk time in seconds, for Inbound ACD calls counted as handled by the agent.

Handled Calls Held

The total number of completed inbound ACD call agent placed on hold at least once.

Handled Calls Held Time

Total number of seconds completed inbound ACD calls were placed on hold.

Wrap-UpTime

The length of time the agent spent in wrap-up work.

Auto Out Calls

Total number of AutoOut (predictive) calls completed by the agent.

Auto Out Calls Time

Total handle time, in seconds, for completed AutoOut (predictive) calls handled by the agent. The value includes the time
                                          that is spent from the call being initiated to the time the agent wrap-up time for the call. The time includes hold time associated
                                          with the call.

Auto Out Calls Talk Time

Total talk time, in seconds, for completed AutoOut (predictive) calls handled by the agent.

Auto Out Calls Held Time

Total time, in seconds, for AutoOut (predictive) calls were placed on hold by the agent.

Auto Out Calls Held

The total number of completed AutoOut (predictive) calls that the agent has placed on hold at least once.

Agent Out Calls

Total number of completed outbound ACD calls made by the agent.

Agent Out Calls Time

Total handle time, in seconds, for completed outbound ACD calls handled by the agent. The value includes the time that is
                                          spent from the call being initiated by the agent to the time the agent wrap-up time for the call. The time includes hold time
                                          associated with the call.

Agent Out Calls Talk Time

Total talk time, in seconds, for completed outbound ACD calls handled by the agent.

Agent Out Calls Held

The total number of completed outbound ACD calls that the agent has placed on hold at least once.

Agent Out Calls Held Time

Total time, in seconds, the calls were placed on hold by the agent.

Internal Calls

Number of internal calls initiated by the agent.

Internal Calls Time

Total time, in seconds, spent on internal calls initiated by the agent.

Internal Calls Rcvd

Number of internal calls received by the agent.

Internal Calls Rcvd Time

Total time, in seconds, spent on internal calls received by the agent.

Internal Calls Held

The total number of internal calls the agent placed on hold at least once.

Internal Calls Held Time

Total time, in seconds, the completed internal calls that were placed on hold.

Preview Calls

Total number of outbound Preview calls completed by the agent.

Preview Calls Time

Total handle time, in seconds, for outbound Preview calls completed by the agent. The value includes the time that is spent
                                          from the call being initiated to the time the agent wrap-up time for the call. The time includes hold time associated with
                                          the call.

Preview Calls Talk Time

Total talk time, in seconds, of outbound Preview calls completed by the agent.

Preview Calls Held

The total number of completed outbound Preview calls the agent has placed on hold at least once.

Preview Calls Held Time

Total time, in seconds, for which outbound Preview calls were placed on hold.

Reserve Calls

For Outbound Option, the number of reservation calls received by an agent in this skill group during the reporting interval.

Reserve Calls Time

For Outbound Option, the time during the reporting interval that an outbound agent in this skill group spent on reservation
                                          calls waiting for the Campaign customer call to be delivered. This includes preview time for Preview, Direct Preview, and
                                          Personal Callback calls.

Reserve Calls Talk Time

For Outbound Option, the talk time for an agent in this skill group on reservation calls during the reporting interval. This
                                          is calculated using Call State.

Reserve Calls Held

For Outbound Option, the number of reservation calls for an agent in this skill group placed on hold during the reporting
                                          interval.

Reserve Calls Held Time

For Outbound Option, the time that reservation calls for an agent in this skill group are on hold during the reporting interval.

Non-ACD Call in Count

Total number of incoming calls received by the agent on Non-ACD line.

Non-ACD Call in Time

Total time in seconds, spent by the agent on a Non-ACD call.

Non-ACD Call Out Count

Total number of out going calls by the agent on Non-ACD line.

Non-ACD Call OutTime

Total time, in seconds, spent by the agent on a Non-ACD outbound call.

## Recent Call
                        	 History

This report presents tables that display the call history of selected agents. Details including the type of call, number,
                              call disposition, wrap-up reason, queue, start time, and duration are displayed.

Data Source: This
                              		  report displays the attributes published by the Live Data Reporting System,
                              		  which continuously processes events from the Router and Agent Peripheral
                              		  Gateway. The Live Data Reporting System updates the individual attributes of
                              		  the report as and when the events occur.

Views : This report has the following grid views:

Recent Call History

Recent Call History All Fields

Recent Call History for Agent

Grouping : Grouping is
                              		  not supported in Live Data reports.

Note :

In Recent Call History, the maximum number of entries for an agent login session is 300. If the maximum number of entries
                                    exceeds this limit, the latest 300 entries are retained.

After the agent logs out, all the entries are cleared.

### Recent Call
                           	 History View

#### Current Fields in the Recent Call History View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

The Recent Call History view provides live data feed that can be viewed on the Cisco Finesse desktop gadgets. This view is visible on the Unified
                                 Intelligence Center report viewer only for the users on Cisco Finesse.

Columns (Fields)

Description

Type

The
                                             						call type: Inbound or outbound call.

The
                                             						value is Inbound or Outbound in the following scenarios:

If
                                                   							 the agent receives a call, this field reports the call type as Inbound.

If
                                                   							 the agent initiates a call, this field reports the call type as Outbound.

If
                                                   							 Outbound Options feature initiates the call, this field reports the call type
                                                   							 as Inbound.

Number

The number of the phone that made or received the call. If the call is an inbound call, the number is picked from the Source
                                             field. If the call is an outbound call, the number is picked from the Destination field.

When agents have not logged in, this field will display
                                                         										UNKNOWN for local CUCM DN.

Disposition

The
                                             						final disposition of the call. For more information on call disposition, see
                                             						the Database Schema Handbook for Cisco Unified Contact Center
                                                						  Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Wrap-up
                                             						Reason

The data
                                             						entered by the agent during call wrap-up.

Queue

The
                                             						skill group name on which the agent handled the call.

Start
                                             						Time

The time
                                             						when the call started.

Duration

The
                                             						duration of the call in seconds.

### Recent Call
                           	 History All Fields

#### Current Fields in the Recent Call History All Fields View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

The Recent Call History All Fields view provides live data feed that can be viewed on the Cisco Finesse desktop gadgets. This view is visible on the Unified
                                 Intelligence Center report viewer only for the users on Cisco Finesse.

Columns (Fields)

Description

Agent

The name of the agent who is in the call.

Type

The call type: Inbound or outbound call.

The value is Inbound or Outbound in the following scenarios:

If the agent receives a call, this field reports the call type as Inbound.

If the agent initiates a call, this field reports the call type as Outbound.

If Outbound Options feature initiates the call, this field reports the call type as Inbound.

Number

The number of the phone that made or received the call. If the call is an inbound call, the number is picked from the Source
                                             field. If the call is an outbound call, the number is picked from the Destination field.

When agents have not logged in, this field will display UNKNOWN for local CUCM DN.

Source

The peripheral number of the agent who initiated the call.

Destination

The DNIS value, provided by the ACD, that arrives with the call.

Disposition

The final disposition of the call. For more information on call disposition, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Disposition Detail

The details of call disposition.

Wrap-up Reason

The data entered by the agent during call wrap-up.

Queue

The skill group name on which the agent handled the call.

Start Time

The time when the call started.

Talk Time

The cumulative time, in seconds, that the call was in a talking state on the destination device. Talk Time is a completed
                                             call time and not an agent state time.

Hold Time

The cumulative time, in seconds, for the call put on hold by an agent.

Duration

The duration of the call in seconds.

Ring Time

The number of seconds that the call spent ringing at the agent's phone before it was answered.

Delay Time

The time in seconds during which the call is active on the switch, but is not queued to a skill group or a trunk resource.

Answered

The status whether the call has been answered or not. It is true if the call is answered.

Peripheral Call Type

The type of the call reported by the peripheral.

Wrap-up Time

The cumulative number of seconds of the after-call work time associated with the call.

### Recent Call
                           	 History for Agent

#### Current Fields in the Recent Call History for Agent View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

The Recent Call History for Agent view provides live data feed that can be viewed on the Cisco Finesse desktop gadgets. This view is visible on the Unified
                                 Intelligence Center report viewer only for the supervisors on Cisco Finesse.

Columns (Fields)

Description

Start
                                             						Time

The time
                                             						when the call started.

Duration

The
                                             						duration of the call in seconds.

Type

The call
                                             						type: Inbound or outbound call.

The
                                             						value is Inbound or Outbound in the following scenarios:

If
                                                   							 the agent receives a call, this field reports the call type as Inbound.

If
                                                   							 the agent initiates a call, this field reports the call type as Outbound.

If
                                                   							 Outbound Options feature initiates the call, this field reports the call type
                                                   							 as Inbound.

Number

The number of the phone that made or received the call. If the call is an inbound call, the number is picked from the Source
                                             field. If the call is an outbound call, the number is picked from the Destination field.

When agents have not logged in, this field will display UNKNOWN for local CUCM DN.

Disposition

The
                                             						final disposition of the call. For more information on call disposition, see
                                             						the Database Schema Handbook for Cisco Unified Contact Center
                                                						  Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Queue

The
                                             						skill group name on which the agent handled the call.

Wrap-up
                                             						Reason

The data
                                             						entered by the agent during call wrap-up.

## Recent State
                        	 History

This report presents tables that display the historical state information for each Agent. Live Data stores and displays details
                           for each agent including the state, reason code, start time, duration.

Data Source: This
                           		report displays the attributes published by the Live Data Reporting System,
                           		which continuously processes events from the Agent Peripheral Gateway. The Live
                           		Data Reporting System updates the individual attributes of the report as and
                           		when the events occur.

Views : This report has the following grid views:

Recent State History

Recent State History All Fields

Grouping : Grouping is
                           		not supported in Live Data reports.

Note :

In Recent State History, the maximum number of entries for an agent login session is 1500. If the maximum number of entries
                                 exceeds this limit, the latest 1500 entries are retained.

After the agent logs out, all the entries are cleared.

### Recent State
                           	 History View

#### Current Fields in the Recent State History View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

The Recent State History view provides live data feed that can be viewed on the Cisco Finesse desktop gadgets. This view is visible on the Unified
                                 Intelligence Center report viewer only for the users on Cisco Finesse.

You can use the column selection tool to add or remove fields from the report.

Columns (Fields)

Description

Start Time

Time when the agent started being in this state.

State

The state of the agent.

For more information on agent state, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Reason

The reason why the agent entered the Not Ready state.

Note: If an agent is Not Ready, the Not Ready reason is updated when the agent goes to Ready or to another Not Ready state with
                                             a different Reason. If the Not Ready agent receives an internal call or makes an outbound call, Reason continues to show the
                                             current Not Ready reason.

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

### Recent State
                           	 History All Fields

#### Current Fields in the Recent State History All Fields View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

The Recent State History All Fields view provides live data feed that can be viewed on the Cisco Finesse desktop gadgets. This view is visible on the Unified
                                 Intelligence Center report viewer only for the users on Cisco Finesse.

You can use the column selection tool to add or remove fields from the report.

Columns (Fields)

Description

Agent Name

The name of the agent, which includes the Last Name and the First Name.

Start Time

Time when the agent started being in this state.

State

The state of the agent.

For more information on agent state, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Reason

The reason why the agent entered the Not Ready state.

Note: If an agent is Not Ready, the Not Ready reason is updated when the agent goes to Ready or to another Not Ready state with
                                             a different Reason. If the Not Ready agent receives an internal call or makes an outbound call, Reason continues to show the
                                             current Not Ready reason.

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

Domain

The media routing domain name.

## Agent Skill
                        	 Group

This report shows all skill group activity for the selected agents, showing each agent's skill group, state, and call direction
                              within each skill group and Media Routing Domain into which the agent is logged.

For Avaya PG, only the base skill groups are displayed in the Live Data report. All the agent activities that are performed
                                          in the sub-skill groups are reported against the base skill group.

Data Source: This
                              		  report displays attributes published by the Live Data Reporting System, which
                              		  continuously processes events from the Router and Agent Peripheral Gateway. The
                              		  Live Data system updates the report's individual attributes as the events
                              		  occur.

Views: This report has the following grid views:

Agent Skill Group

Agent Skill Group All Fields

Select the view you want to see from the report drop-down list that is located on the top left corner.

Grouping :Grouping is not supported in Live Data reports.

### Agent Skill Group View

#### Current Fields in the Agent Skill Group View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

Columns (Fields)

Description

Precision Queue/Skill Group

The
                                             						enterprise name of the precision queue or the skill group associated with the
                                             						task on which the agent is currently working. If the agent is not involved in
                                             						any task in the media routing domain, this field shows Not Applicable. Because
                                             						an agent can be logged into multiple skill groups, this field is not filled
                                             						until the agent is assigned a task.

If not
                                             						applicable, the column is left blank.

Agent Name

The name
                                             						of the agent.

State

The
                                             						current state of the agent.

Reason

The
                                             						reason code and text indicating the reason the agent entered the Not Ready
                                             						state.

Note: If an agent is
                                             						Not Ready, the Not Ready reason code and text are only updated when the agent
                                             						goes to Ready or to another Not Ready state with a different Reason code. If
                                             						the Not Ready agent receives an internal call or makes an outbound call, Reason
                                             						continues to show the current Not Ready code and text.

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. For this time to be accurate, ensure
                                             that time on the client machine is set correctly as per the timezone.

Domain

The
                                             						media routing domain name.

Direction

The
                                             						direction of the call that the agent is currently working on:

In

Out

Other In

Other Out

Out Reserve

Out Preview

Out Predictive

Not Applicable

(if the logged in agent is not active in the skill group)

Logged On

The date
                                             						and time the agent logged in with the given set of skills, measured in
                                             						MM:DD:YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format.

Destination

The type
                                             						of outbound task on which the agent is currently working:

1 = ACD

2 = Direct

3 = Auto Out

4 = Reserve

5 = Preview

All other values = Not Applicable

Attributes

The
                                             						names of the attributes used in the precision queue definition. The report
                                             						shows only those attributes that are used.

### Agent Skill Group All Fields

#### Current Fields in the Agent Skill Group All Fields View

Current fields are the fields that appear by default in a report that is generated from the stock template.

This view displays the default fields are the fields that are visible in the Agent Skill Group All Fields view. You can use
                                 the column selection tool to add or remove fields from the report.

Column (Field)

Description

Precision Queue/Skill Group

The
                                             						enterprise name of the precision queue or the skill group associated with the
                                             						task on which the agent is currently working. If the agent is not involved in
                                             						any task in the media routing domain, this field shows Not Applicable. Because
                                             						an agent can be logged into multiple skill groups, this field is not filled
                                             						until the agent is assigned a task.

If not
                                             						applicable, the column is left blank.

Agent Name

The name
                                             						of the agent. Composed of Last Name, First Name.

State

The
                                             						current state of the agent.

Reason

The
                                             						reason code and text indicating the reason the agent entered the Not Ready
                                             						state.

Note: If an agent is
                                             						Not Ready, the Not Ready reason code and text are only updated when the agent
                                             						goes to Ready or to another Not Ready state with a different Reason code. If
                                             						the Not Ready agent receives an internal call or makes an outbound call, Reason
                                             						continues to show the current Not Ready code and text.

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

Domain

The
                                             						media routing domain name.

Direction

The
                                             						direction of the call that the agent is currently working on:

In

Out

Other In

Other Out

Out Reserve

Out Preview

Out Predictive

Not Applicable

(if the logged in agent is not active in the skill group)

Logged On

The date
                                             						and time that the agent logged in. The format is MM/DD/YYYY (month, day, year)
                                             						and HH:MM:SS (hours, minutes, seconds) format.

Destination

The type
                                             						of outbound task on which the agent is currently working:

1 = ACD

2 = Direct

3 = Auto Out

4 = Reserve

5 = Preview

All other values = Not Applicable

Extension

The
                                             						phone extension into which the agent is logged.

Available in MRD

Whether
                                             						or not the agent is available to accept a task in this Media Routing Domain:

NO (Not available)

YES_ICM ( Unified CCE available in media routing domain)

YES_APP (Application available in media routing domain)

All other values = No

An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready; the agent is not at the agent's maximum task limit for the MRD; and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is Unified CCE -available, then the Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only the Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent.

Device
                                             						Type

The kind of phone being used:

0 = Local agent; normal ACD/ Unified CCE phone or non-voice task.

1 = Remote phone, call by call (Mobile agent's phone is connected for each incoming call).

2 = Remote phone, nailed connection (Mobile agent calls and logs in once; line remains connected through multiple calls).

Team

The
                                             						Enterprise Name of the Agent Team.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

Tasks
                                             						in Progress

The number of tasks currently queued for the agent's skill group.

Max
                                             						Tasks

The
                                             						maximum number of tasks that may be assigned to an agent.

On
                                             						Hold

Agent
                                             						on hold:

1 = Yes

All other values = No

Requested Supervisor Assist

Whether or not the agent requested supervisor assistance:

1 = Yes

All other values = No

Routable

Calls
                                             						can be routed to the agent:

1 = Yes

All other values = No

Reason
                                             						Code

A code
                                             						received from the peripheral that indicates the reason for the agent's last
                                             						state change. If not defined, Reason is None.

## Precision Queue

This report shows all precision queue activity for all agents logged in to the precision queue.

Data Source: This report displays attributes published by the Live Data Reporting System, which continuously processes events from the
                              Router and Agent Peripheral Gateway. The Live Data system updates the report's individual attributes as the events occur.

Views: This report has the following grid views:

Agent Utilization view

All Fields view

Default view

Grouping: Grouping is not supported in Live Data reports.

### Precision Queue Default View

#### Current Fields in the Precision Queue Default View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

Precision Queue

The
                                             						enterprise name of the precision queue.

Domain

The enterprise name of the Media Routing Domain associated with the precision queue.

Domain is derived from: Media_Routing_Domain.EnterpriseName.

Queued

The number of tasks currently queued for the precision queue.

Longest Queued

The
                                             						longest time in hours, minutes, and seconds (HH:MM:SS) that a task has been
                                             						waiting in the precision queue to be handled by an agent.

Logged
                                             						On

The
                                             						number of agents who are currently logged in to the precision queue. This count
                                             						is updated each time an agent logs on and each time an agent logs off.

CURRENT STATE
                                                						  DISTRIBUTION

Ready

The
                                             						number of agents in the precision queue in the Ready state.

Reserved

The
                                             						number of agents in the precision queue who are in Reserved state and awaiting
                                             						incoming tasks.

Active
                                             						In

The
                                             						number of agents in the precision queue who are currently working on incoming
                                             						tasks.

Active
                                             						Out

The
                                             						number of agents in the precision queue who are currently working on outbound
                                             						tasks.

Active
                                             						Other

The
                                             						number of agents in the precision queue who are currently working on internal
                                             						(neither inbound nor outbound) tasks.

Hold

The
                                             						number of agents who have all active calls on hold or whose state to the
                                             						precision queue is Paused.

The
                                             						agent is not in the Hold state with one call on hold and talking on another
                                             						call (for example, a consultative call). The agent must have all active calls
                                             						on hold.

Wrap
                                             						Up

The
                                             						number of agents in the precision queue who are in the Work Not Ready state and
                                             						Work Ready state.

The
                                             						Work Not Ready state is a state in which an agent is involved in after task
                                             						work and is assumed not to be ready to accept incoming tasks when done. The
                                             						Work Ready state is a state in which an agent is involved in after a task work
                                             						and is assumed to be ready to accept incoming tasks when done.

Not
                                             						Ready

The
                                             						number of agents in the precision queue who are in the Not Ready state, a state
                                             						in which agents are logged in but are neither involved in any task handling
                                             						activity nor available to handle a task.

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state. Busy Other is a state in
                                             						which the agent is handling calls assigned to other precision queues during the
                                             						interval.

For
                                             						example, an agent might be talking on an inbound call in one precision queue
                                             						while simultaneously logged on to and ready to accept calls from other
                                             						precision queues. The agent can be active (talking on or handling calls) in
                                             						only one precision queue at a time. Therefore, while active in one precision
                                             						queue, for the other precision queue the agent is considered to be in the Busy
                                             						Other state.

TO INTERVAL

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the precision queue during the current
                                             interval.

Average Handle Time

The average time spent by  agents in the precision queue in handling a task during the current interval, measured in HH:MM:SS
                                             (hours, minutes, seconds).

% Ready

The percentage of Logged On time during which an agent was Ready during the current interval.

TODAY

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the precision queue today.

Average Handle Time

The average time spent by  agents in the precision queue in handling a task today, measured in HH:MM:SS (hours, minutes, seconds).

% Ready

The percentage of Logged On time during which an agent was Ready today.

### Precision Queue Agent Utilization View

#### Current Fields in the Precision Queue Agent Utilization View

The Precision Queue Agent Utilization View contains fields that appear by default in a report generated from the stock template. The fields are listed below in the
                                 order (left to right) in which they appear by default in the stock template.

Precision Queue

The
                                          					 enterprise name of the precision queue.

Domain

The enterprise name of the Media Routing Domain associated with the skill group.

Domain is derived from: Media_Routing_Domain.EnterpriseName.

Queued

The number of tasks currently queued for the precision queue.

Longest Queued

The longest call in queue as reported by the router.

Logged
                                          					 On

The
                                          					 number of agents who are currently logged in to the precision queue. This count is
                                          					 updated each time an agent logs on and each time an agent logs off.

CURRENT STATE
                                             						DISTRIBUTION

Ready

The
                                          					 number of agents in the precision queue in the Ready state.

Reserved

The
                                          					 number of agents in the precision queue who are in Reserved state and awaiting
                                          					 incoming tasks.

Active
                                          					 In

The
                                          					 number of agents in the precision queue who are currently working on incoming
                                          					 tasks.

Active
                                          					 Out

The
                                          					 number of agents in the precision queue who are currently working on outbound
                                          					 tasks.

Active
                                          					 Other

The
                                          					 number of agents in the precision queue who are currently working on internal
                                          					 (neither inbound nor outbound) tasks.

Hold

The
                                          					 number of agents who have all active calls on hold or whose state to the precision queue is Paused.

The
                                          					 agent is not in the Hold state with one call on hold and talking on another
                                          					 call (for example, a consultative call). The agent must have all active calls
                                          					 on hold.

Wrap Up

The
                                          					 number of agents in the precision queue who are in the Work Not Ready state and
                                          					 Work Ready state.

The Work
                                          					 Not Ready state is a state in which an agent is involved in after task work and
                                          					 is assumed not to be ready to accept incoming tasks when done. The Work Ready
                                          					 state is a state in which an agent is involved in after a task work and is
                                          					 assumed to be ready to accept incoming tasks when done.

Not
                                          					 Ready

The
                                          					 number of agents in the precision queue who are in the Not Ready state, a state in
                                          					 which agents are logged in but are neither involved in any task handling
                                          					 activity nor available to handle a task.

Busy
                                          					 Other

The
                                          					 number of agents currently in the BusyOther state. Busy Other is a state in
                                          					 which the agent is handling calls assigned to other precision queues during the
                                          					 interval.

For
                                          					 example, an agent might be talking on an inbound call in one precision queue while
                                          					 simultaneously logged on to and ready to accept calls from other precision queues.
                                          					 The agent can be active (talking on or handling calls) in only one precision queue
                                          					 at a time. Therefore, while active in one precision queue, for the other precision queue the agent is considered to
                                          be in the Busy Other state.

TO INTERVAL

Logged On

The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this precision queue during the current
                                          interval.

Ready

The total time in seconds an agent associated with this precision queue was in the Not_Active state with respect to this precision
                                          queue during the current interval. AvailTime is included in the calculation of LoggedOnTime.

Not Ready

The total time that the agents spent in Not Ready state for this skill for the current interval. This value is taken directly
                                          from the database.

% Ready

The percentage of Logged On time during which agents were Ready during the current interval.

TODAY

Logged On

The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this precision queue today.

Ready

The total time in seconds an agent associated with this precision queue was in the Not_Active state with respect to this precision
                                          queue today. AvailTime is included in the calculation of LoggedOnTime.

Not Ready

The total time that the agents spent in Not Ready state for this skill today. This value is taken directly from the database.

% Ready

The percentage of Logged On time during which an agent was Ready today.

### Precision Queue All Fields

#### Current Fields in the Precision Queue All Fields View

Current fields are the fields that appear by default in a report that is generated from the stock template.

This view displays the default fields that are visible in the All Fields view. You can use the column selection tool to add
                                 or remove fields from the report.

Precision Queue

The
                                             						enterprise name of the precision queue.

Domain

The enterprise name of the Media Routing Domain associated with the precision queue.

Domain is derived from: Media_Routing_Domain.EnterpriseName.

Queued

The number of tasks currently queued for the precision queue.

Longest Queued

The longest call in queue as reported by the router.

Logged
                                             						On

The
                                             						number of agents who are currently logged in to the precision queue. This count
                                             						is updated each time an agent logs on and each time an agent logs off.

CURRENT STATE
                                                						  DISTRIBUTION

Ready

The
                                             						number of agents in this precision queue in the Ready state.

Reserved

The
                                             						number of agents in this precision queue who are in Reserved state and awaiting
                                             						incoming tasks.

Active
                                             						In

The
                                             						number of agents in this precision queue who are currently working on incoming
                                             						tasks.

Active
                                             						Out

The
                                             						number of agents in this precision queue who are currently working on outbound
                                             						tasks.

Active
                                             						Other

The
                                             						number of agents in this precision queue who are currently working on internal
                                             						(neither inbound nor outbound) tasks.

Hold

The
                                             						number of agents who have all active calls on hold or whose state to the
                                             						precision queue is Paused.

The
                                             						agent is not in the Hold state with one call on hold and talking on another
                                             						call (for example, a consultative call). The agent must have all active calls
                                             						on hold.

Wrap Up

The
                                             						number of agents in this precision queue who are in the Work Not Ready state
                                             						and Work Ready state.

The Wrap Up state is a state in which an agent is involved in after task work and is assumed not to be ready to accept incoming
                                             tasks when done.

The Work Ready state is a state in which an agent is involved in after a task work and is assumed to be ready to accept incoming
                                             tasks when done.

Not
                                             						Ready

The
                                             						number of agents in this precision queue who are in the Not Ready state, a
                                             						state in which agents are logged in but are neither involved in any task
                                             						handling activity nor available to handle a task.

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state. Busy Other is a state in
                                             						which the agent is handling calls assigned to other precision queues during the
                                             						interval.

For
                                             						example, an agent might be talking on an inbound call in one precision queue
                                             						while simultaneously logged on to and ready to accept calls from other
                                             						precision queues. The agent can be active (talking on or handling calls) in
                                             						only one precision queue at a time. Therefore, while active in one precision
                                             						queue, for the other precision queue the agent is considered to be in the Busy
                                             						Other state.

OUTBOUND OPTION STATES

Active
                                             						Reserve

The
                                             						number of agents in the precision queue currently talking on agent reservation
                                             						calls.

Active
                                             						Preview

The
                                             						number of agents in the precision queue currently talking on outbound Preview
                                             						calls.

Active
                                             						Auto Out

The
                                             						number of agents in the precision queue currently talking on AutoOut
                                             						(predictive) calls.

(no header)

ICM
                                             						Available

The number of agents belonging to this precision queue who are currently ICMAvailable for the MRD associated with this precision queue.

Agents are ICMAvailable if they are Routable and Available for the MRD.
                                             If an agent is ICMAvailable , the system
                                             software can assign tasks to the agent.

Eligible

The number of agents who are Routable for the MRD associated with this precision queue, and whose state in this precision
                                             queue is currently something other than NOT_READY or WORK_NOT_READY.

WRAPUP STATE
                                                						  DISTRIBUTION

Work
                                             						Ready

The
                                             						agent is performing wrap-up work for a call or task in the precision queue.

If the
                                             						agent is handling a voice call, the agent enters Not Active state when wrap-up
                                             						is complete. If the agent is handling a non-voice task, the agent might enter
                                             						Not Active or Not Ready state when wrap-up is complete.

Wrap Up

The
                                             						agent is performing wrap-up work for a call in the precision queue. The agent
                                             						enters Not Ready state when wrap-up is complete.

(no header)

Application
                                             						Available

The
                                             						number of agents belonging to this precision queue who are currently
                                             						Application Available with respect to the MRD to which the precision queue
                                             						belongs.

An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready; the agent is not at the agent's maximum task limit for the MRD; and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is Application-available, then only an application in the MRD, for example chat, can assign
                                             tasks to the agent.

TO INTERVAL

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the precision queue during the current
                                             interval.

Avg Handle Time

The average time spent by  agents in handling a task during the current interval, measured in HH:MM:SS (hours, minutes, seconds).

Logged On

The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this precision queue during the current
                                             interval.

Ready

The total time in seconds an agent associated with this precision queue was in the Not_Active state with respect to this precision
                                             queue during the current interval. AvailTime is included in the calculation of LoggedOnTime.

Not Ready

The total time that the agents spent in Not Ready state for this skill for the current interval. This value is taken directly
                                             from the database.

% Ready

The percentage of Logged On time during which agents were Ready during the current interval.

TODAY

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the precision queue today.

Avg Handle Time

The average time spent by  agents in handling a task today, measured in HH:MM:SS (hours, minutes, seconds).

Logged On

The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this precision queue today.

Ready

The total time in seconds an agent associated with this precision queue was in the Not_Active state with respect to this precision
                                             queue today. AvailTime is included in the calculation of LoggedOnTime.

Not Ready

The total time that the agents spent in Not Ready state for this skill today. This value is taken directly from the database.

% Ready

The percentage of Logged On time during which an agent was Ready today.

## Skill
                        	 Group

This report shows
                              		  all skill group activity for all agents logged in to the skill group.

Data Source: This
                              		  report displays attributes published by the Live Data Reporting System, which
                              		  continuously processes events from the Router and Agent Peripheral Gateway. The
                              		  Live Data system updates the report's individual attributes as the events
                              		  occur.

Views: This report has three views:

Agent Utilization

All Fields

Default View

Grouping: Grouping is
                              		  not supported in Live Data reports.

### Skill Group
                           	 Default View

#### Current Fields in the Default View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

Skill
                                          					 Group

The
                                          					 enterprise name of the skill group.

Domain

The enterprise name of the Media Routing Domain associated with the skill group.

Domain is derived from: Media_Routing_Domain.EnterpriseName.

Router

Queued

The number of tasks currently queued for the skill group in the Router queue.

Longest in Queue

The longest call in queue as reported by the router.

Local

Queued

The number of tasks currently queued for the skill group in the Router queue.

Longest Queued

The longest call in queue as reported by the router.

Logged
                                          					 On

The number of agents who are currently logged in to the skill group. This count is updated each time an agent logs on and
                                          each time an agent logs off.

Current State Distribution

Ready

The number of agents in the skill group in the Ready state.

Reserved

The number of agents in the skill group who are in Reserved state and awaiting incoming tasks.

Active
                                          					 In

The number of agents in the skill group who are currently working on incoming tasks.

Active
                                          					 Out

The number of agents in the skill group who are currently working on outbound tasks.

Active
                                          					 Other

The number of agents in the skill group who are currently working on internal (neither inbound nor outbound) tasks.

Hold

The number of agents who have all active calls on hold or whose state to the skill group is Paused.

The
                                          					 agent is not in the Hold state with one call on hold and talking on another
                                          					 call (for example, a consultative call). The agent must have all active calls
                                          					 on hold.

The number of agents in the skill group who are in the Wrap Up state and Ready state.

The Wrap Up state is a state in which an agent is involved in after task work and is assumed not to be ready to accept incoming
                                          tasks when done.

The Ready state is a state in which an agent is involved in after a task work and is assumed to be ready to accept incoming
                                          tasks when done.

Not
                                          					 Ready

The
                                          					 number of agents in the skill group who are in the Not Ready state, a state in
                                          					 which agents are logged in but are neither involved in any task handling
                                          					 activity nor available to handle a task.

Busy
                                          					 Other

The
                                          					 number of agents currently in the BusyOther state. Busy Other is a state in
                                          					 which the agent is handling calls assigned to other skill groups during the
                                          					 interval.

For
                                          					 example, an agent might be talking on an inbound call in one skill group while
                                          					 simultaneously logged on to and ready to accept calls from other skill groups.
                                          					 The agent can be active (talking on or handling calls) in only one skill group
                                          					 at a time. Therefore, while active in one skill group, for the other skill
                                          					 group the agent is considered to be in the Busy Other state.

To Interval

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the skill group during the current
                                          interval.

Average Handle Time

The average time spent by  agents in handling a task during the current interval, measured in HH:MM:SS (hours, minutes, seconds).

Today

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the skill group today.

Average Handle Time

The average time spent by  agents in handling a task today, measured in HH:MM:SS (hours, minutes, seconds).

(no header)

Longest Task In Queue

The longest time in hours, minutes, and seconds (HH:MM:SS) that a task has been waiting to be handled by an agent.

Tasks Queued

The number of tasks queued to this Skill Group.

### Skill Group Agent Utilization View

#### Current Fields in the Agent Utilization View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

The Agent Utilization View contains fields that appear by default in a report generated from the stock template.

Skill
                                          					 Group

The
                                          					 enterprise name of the skill group.

Domain

The enterprise name of the Media Routing Domain associated with the skill group.

Domain is derived from: Media_Routing_Domain.EnterpriseName.

Router

Queued

The
                                          					 number of tasks currently queued for the skill group in the Router queue.

Router Longest Task in Queue

The longest call in queue as reported by the router.

Local

Queued

The
                                          					 number of tasks currently queued for the skill group in the Router queue.

Longest Queued

The longest call in queue as reported by the router.

(no header)

Logged
                                          					 On

The
                                          					 number of agents who are currently logged in to the skill group. This count is
                                          					 updated each time an agent logs on and each time an agent logs off.

Current State Distribution

Ready

The
                                          					 number of agents in the skill group in the Ready state.

Reserved

The
                                          					 number of agents in the skill group who are in Reserved state and awaiting
                                          					 incoming tasks.

Active
                                          					 In

The
                                          					 number of agents in the skill group who are currently working on incoming
                                          					 tasks.

Active
                                          					 Out

The
                                          					 number of agents in the skill group who are currently working on outbound
                                          					 tasks.

Active
                                          					 Other

The
                                          					 number of agents in the skill group who are currently working on internal
                                          					 (neither inbound nor outbound) tasks.

Hold

The
                                          					 number of agents who have all active calls on hold or whose state to the skill
                                          					 group is Paused.

The
                                          					 agent is not in the Hold state with one call on hold and talking on another
                                          					 call (for example, a consultative call). The agent must have all active calls
                                          					 on hold.

Wrap Up

The number of agents in the skill group who are in the Wrap Up state and Work Ready state.

The Wrap Up state is a state in which an agent is involved in after task work and is assumed not to be ready to accept incoming
                                          tasks when done. The Work Ready state is a state in which an agent is involved in after a task work and is assumed to be ready
                                          to accept incoming tasks when done.

Not
                                          					 Ready

The
                                          					 number of agents in the skill group who are in the Not Ready state, a state in
                                          					 which agents are logged in but are neither involved in any task handling
                                          					 activity nor available to handle a task.

Busy
                                          					 Other

The number of agents currently in the Busy Other state. Busy Other is a state in which the agent is handling calls assigned
                                          to other skill groups during the interval.

For
                                          					 example, an agent might be talking on an inbound call in one skill group while
                                          					 simultaneously logged on to and ready to accept calls from other skill groups.
                                          					 The agent can be active (talking on or handling calls) in only one skill group
                                          					 at a time. Therefore, while active in one skill group, for the other skill
                                          					 group the agent is considered to be in the Busy Other state.

To Interval

Logged On

The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this skill group during the current
                                          interval.

Ready

The total time in seconds an agent associated with this skill group was in the Not_Active state with respect to this skill
                                          group during the current interval. AvailTime is included in the calculation of LoggedOnTime.

Not Ready

The total time that the agents spent in Not Ready state for this skill for the current interval. This value is taken directly
                                          from the database.

% Ready

The percentage of Logged On time during which agents were Ready during the current interval.

Today

Logged On

The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this skill group today.

Ready

The total time in seconds an agent associated with this skill group was in the Not_Active state with respect to this skill
                                          group today. AvailTime is included in the calculation of LoggedOnTime.

Not Ready

The total time that the agents spent in Not Ready state for this skill today. This value is taken directly from the database.

% Ready

The percentage of Logged On time during which an agent was Ready today.

(no header)

Longest Task In Queue

The longest time in hours, minutes, and seconds (HH:MM:SS) that a task has been waiting to be handled by an agent.

Tasks Queued

The number of tasks queued to this Skill Group.

### Skill Group All Fields

#### Current Fields in the All Fields View

Current fields are the fields that appear by default in a report that is generated from the stock template.

The default fields are listed in the table below in the order (left to right) in which they appear in the stock template.

All Fields are the fields that are visible in the All Fields view. You can use the column selection tool to add or remove fields from
                                 the report.

Skill
                                             						Group

The
                                             						enterprise name of the skill group.

Domain

The enterprise name of the Media Routing Domain associated with the skill group.

Domain is derived from: Media_Routing_Domain.EnterpriseName.

Router

Queued

The
                                             					 number of tasks currently queued for the skill group in the Router queue.

Longest in Queue

The longest call in queue as reported by the router.

Local

Queued

The
                                             					 number of tasks currently queued for the skill group in the Router queue.

Longest Queued

The longest call in queue as reported by the router.

(no header)

Logged
                                             						On

The
                                             						number of agents who are currently logged in to the skill group. This count is
                                             						updated each time an agent logs on and each time an agent logs off.

Current State Distribution

Ready

The
                                             						number of agents in the skill group in the Ready state.

Reserved

The
                                             						number of agents in the skill group who are in Reserved state and awaiting
                                             						incoming tasks.

Active
                                             						In

The
                                             						number of agents in the skill group who are currently working on incoming
                                             						tasks.

Active
                                             						Out

The
                                             						number of agents in the skill group who are currently working on outbound
                                             						tasks.

Active
                                             						Other

The
                                             						number of agents in the skill group who are currently working on internal
                                             						(neither inbound nor outbound) tasks.

Hold

The
                                             						number of agents who have all active calls on hold or whose state to the skill
                                             						group is Paused.

The
                                             						agent is not in the Hold state with one call on hold and talking on another
                                             						call (for example, a consultative call). The agent must have all active calls
                                             						on hold.

Wrap Up

The number of agents in the skill group who are in the Wrap Up state and Work Ready state.

The Wrap Up state is a state in which an agent is involved in after task work and is assumed not to be ready to accept incoming tasks
                                             when done. The Work Ready state is a state in which an agent is involved in after a task work and is assumed to be ready to accept incoming tasks
                                             when done.

Not
                                             						Ready

The
                                             						number of agents in the skill group who are in the Not Ready state, a state in
                                             						which agents are logged in but are neither involved in any task handling
                                             						activity nor available to handle a task.

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state. Busy Other is a state in
                                             						which the agent is handling calls assigned to other skill groups during the
                                             						interval.

For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged on to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state.

Outbound Option States

Active
                                             						Reserve

The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls.

Active
                                             						Preview

The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls.

Active
                                             						Auto Out

The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls.

(no header)

ICM
                                             						Available

The number of agents belonging to this skill
                                             group who are currently ICMAvailable for the MRD associated with this skill group.

Agents are ICMAvailable if they are Routable and Available for the MRD.
                                             If an agent is ICMAvailable , the system
                                             software can assign tasks to the agent.

Eligible

The number of agents who are Routable for the MRD associated with this skill group, and whose agent state in this skill
                                             group is currently something other than NOT_READY or WORK_NOT_READY.

Wrap Up State Distribution

Ready

The
                                             						agent is performing wrap-up work for a call or task in the skill group.

If the
                                             						agent is handling a voice call, the agent enters Not Active state when wrap-up
                                             						is complete. If the agent is handling a non-voice task, the agent might enter
                                             						Not Active or Not Ready state when wrap-up is complete.

Wrap Up

The
                                             						agent is performing wrap-up work for a call in the skill group. The agent
                                             						enters Not Ready state when wrap-up is complete.

(no header)

Application Available

The
                                             						number of agents belonging to this skill group who are currently
                                             						Application Available with respect to the MRD to which the skill group belongs.
                                             						An agent is Application available if the agent is Not Routable and Available
                                             						for the MRD.

To Interval

Logged On

The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this skill group during the current
                                             interval.

Ready

The total time in seconds an agent associated with this skill group was in the Not_Active state with respect to this skill
                                             group during the current interval. AvailTime is included in the calculation of LoggedOnTime.

Not Ready

The total time that the agents spent in Not Ready state for this skill for the current interval. This value is taken directly
                                             from the database.

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the skill group during the current
                                             interval.

Avg Handle Time

The average time spent by  agents in handling a task during the current interval, measured in HH:MM:SS (hours, minutes, seconds).

% Ready

The percentage of Logged On time during which agents were Ready during the current interval.

Today

Logged On

The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this skill group today.

Ready

The total time in seconds an agent associated with this skill group was in the Not_Active state with respect to this skill
                                             group today. AvailTime is included in the calculation of LoggedOnTime.

Not Ready

The total time that the agents spent in Not Ready state for this skill today. This value is taken directly from the database.

Handled

The number of inbound calls that were answered and have completed wrap-up by agents in the skill group today.

Avg Handle Time

The average time spent by  agents in handling a task today, measured in HH:MM:SS (hours, minutes, seconds).

% Ready

The percentage of Logged On time during which an agent was Ready today.

| Columns (Fields) | Description |
|---|---|
| Agent Name | The name of the agent. This field is composed of Last Name and First Name. |
| State | The
                                             						current state of the agent: Logged Out Logged On Not Ready Ready Talking Work Not Ready Work Ready Busy Other Reserved Unknown Hold Active Paused Interrupted Not Active |
| Reason | The reason code and text indicating the reason the agent entered the Not Ready state. Note: If an agent is Not Ready, the Not Ready reason code and text are only updated when the agent goes to Ready or to another Not Ready state with a different Reason code. If the Not Ready agent receives an internal call or makes an outbound call, Reason continues
                                             to show the current Not Ready code and text. |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. |
| Domain | The
                                             						media routing domain name. |
| Direction | The
                                             						direction of the call that the agent is currently working on: In Out Other In Other Out Out Reserve Out Preview Out Predictive Not Applicable (if the logged in agent is not active in the skill group) |
| Precision Queue/Skill Group | The enterprise name of the precision queue or the skill group associated with the task on which the agent is currently working.
                                             If the agent is not involved in any task in the media routing domain, this field shows Not Applicable . Because an agent can be logged into multiple skill groups, this field is not filled until the agent is assigned a task. If not
                                             						applicable, the column is left blank. |
| Attributes | The
                                             						names of the attributes used in the precision queue definition. The report
                                             						shows only those attributes that are used. |
| Reason Code | A code received from the peripheral that indicates the reason for the agent's last state change. If not defined, Reason is
                                             None. |

| Report
                                             						Field | Description |
|---|---|
| Agent
                                             						Name | The name
                                             						of the agent. Composed of Last Name, First Name. |
| Team
                                             						Name | The
                                             						Enterprise Name of the Agent Team. |
| State | The
                                             						current state of the agent: Logged Out Logged On Not Ready Ready Talking Work Not Ready Work Ready Busy Other Reserved Unknown Hold Active Paused Interrupted Not Active |
| Reason | The
                                             						reason code and text indicating the reason the agent entered the Not Ready
                                             						state. Note: If an agent is
                                             						Not Ready, the Not Ready reason code and text are only updated when the agent
                                             						goes to Ready or to another Not Ready state with a different Reason code. If
                                             						the Not Ready agent receives an internal call or makes an outbound call, Reason
                                             						continues to show the current Not Ready code and text. |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. |
| Precision Queue/Skill Group | The
                                             						enterprise name of the precision queue or the skill group associated with the
                                             						task on which the agent is currently working. If the agent is not involved in
                                             						any task in the media routing domain, this field shows Not Applicable. Because
                                             						an agent can be logged into multiple skill groups, this field is not filled
                                             						until the agent is assigned a task. |
| Router Calls Queued Now | The number
                                             						of calls currently queued at the router. |
| Longest Call in Queue | The
                                             						length of time the longest queued call on the routing media has been queued,
                                             						measured in HH:MM:SS (hours, minutes, seconds) format. |
| Domain | The
                                             						media routing domain name. |
| Direction | The
                                             						direction of the call that the agent is currently working on: Not
                                                   							 Applicable In
                                                   							 (inbound task - non voice tasks are always inbound). Out
                                                   							 (outgoing external task). Other (outgoing or incoming internal task). Not
                                                   							 Applicable (if the logged in agent is not active in the skill group). |
| Destination | The type
                                             						of outbound task on which the agent is currently working: 1 = ACD 2 = Direct 3 = Auto Out 4 = Reserve 5 = Preview All other values = Not
                                                						  Applicable |
| Routable | Calls
                                             						can be routed to the agent: 1 = Yes All other values = No |
| Tasks
                                             						in Progress | The
                                             						number of tasks currently queued for the skill group. |
| Max
                                             						Tasks | The
                                             						maximum number of tasks that may be assigned to an agent. |
| Device
                                             						Type | The
                                             						kind of phone being used: 0 = Local agent; normal
                                                   						  ACD/Unified CCE phone or non-voice task. 1 = Remote phone, call by
                                                   						  call (Mobile agent's phone is connected for each incoming call). 2 = Remote phone, nailed
                                                   						  connection (Mobile agent calls and logs in once; line remains connected through
                                                   						  multiple calls). |
| Available in MRD | Whether or not the agent is available to accept a task in this
                                             						Media Routing Domain: NO (Not available) YES_ICM (Unified ICM
                                                						  available in media routing domain) YES_APP (Application
                                                						  available in media routing domain) All other values = No An
                                             						agent is available for a task in a media routing domain (MRD) if the agent's
                                             						state in that MRD is anything other than Not Ready; the agent is not at the
                                             						agent's maximum task limit for the MRD; and the agent is not working on a
                                             						non-interruptible task in another MRD. If an agent is Unified ICM-available,
                                             						then the Unified ICM can assign tasks to the agent. If an agent is
                                             						Application-available, then the application can assign tasks to the agent. In
                                             						the former case, only the Unified ICM can assign tasks to the agent. In the
                                             						latter, only the application can assign tasks to the agent. |
| Request Supervisor Assist | Whether or not the agent requested supervisor assistance: 1 = Yes All other values = No |
| Precision Queue Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |
| Extension | The
                                             						phone extension into which the agent is logged. |
| Remote
                                             						Address | The
                                             						remote address associated with this MRD (remote extension used for Mobile
                                             						Agents). |
| Last
                                             						Level Change | The
                                             						date and time of the agent's last task level change in this MRD. Chat
                                             						agents have a maximum number of open slots. The task level changes when the
                                             						number of open slots changes as a result of the number of calls in progress
                                             						changing (the number of open slots = the maximum number of tasks - calls in
                                             						progress). This
                                             						applies to all other agents as well; however, the task level is always 0 or 1. |
| Last
                                             						Mode Change | The
                                             						date and time of the agent last mode change in this MRD. An
                                             						agent has a mode with respect to each Media Routing Domain the agent is logged
                                             						in to. These modes are either routable or not routable. If the mode is routable,
                                             						the Unified ICM controls the agent and assigns tasks to the agent. When an
                                             						agent is routable for an MRD, an application instance (for example, Enterprise Chat and
                                                   						Email )
                                             						will not allow the agent to work on a task unless Unified ICM assigns the task. If the mode is not
                                             						routable, the application instance controls the agent and assigns tasks to the
                                             						agent. The software tracks the agent activity by monitoring Offer Task, Start
                                             						Task, and other messages from the application that describe the task the agent
                                             						is working on. For Enterprise Chat and
                                                   						Email ,
                                             						an agent mode never changes. Each agent is always routable. An
                                             						agent mode is always routable with respect to the voice MRD. |
| Last
                                             						State Change | The
                                             						date and time of the agent's last state change in this MRD. |
| Login | The
                                             						date and time that the agent logged in. The format is MM/DD/YYYY (month, day,
                                             						year) and HH:MM:SS (hours, minutes, seconds) format. |
| Reason Code | A code
                                             						received from the peripheral that indicates the reason for the agent's last
                                             						state change. If not defined, Reason is None. |

| Note | The agent statistics that are displayed in this report resets during midnight at Peripheral Gateway. This report displays the statistics on daily basis. |
|---|---|

| Note | For more information on the fields and desciptons see, AgentState section in Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html |
|---|---|

| Columns (Fields) | Description |
|---|---|
| Agent | The name of the agent, which includes the first and the last name of the agent. |
| State | The state of the agent. For more information, see AgentState section in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at. https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html |
| Logged On Time | Total time, in seconds, the agent has been logged on. For this time to be accurate, ensure that time on the client machine
                                             is set correctly as per the timezone. |
| Not ReadyTime | The total time that the agent spent in Not Ready state. For this time to be accurate, ensure that time on the client machine
                                             is set correctly as per the timezone. |
| Ready Time | The total time that the agent spent in Ready state. For this time to be accurate, ensure that time on the client machine is
                                             set correctly as per the timezone. |
| % Not Ready Time | The percentage of time that the agent has spent in Not Ready state with respect to the total Logged On Time. |
| Handled Calls | The number of inbound calls that were answered and have completed wrap-up by the agent. |
| Avg Handled Calls Time | Average handle time in seconds, for inbound ACD calls counted as handled by the agent. The time that agent spent on the call
                                             to the time the agent wrap-up the work on the call. Includes hold time that is associated with the call. |
| Avg Handled Calls Talk Time | Average talk time, in seconds, for Inbound ACD calls counted as handled by the agent. |
| Avg Handled Calls Held Time | Average held time, in seconds, for Inbound ACD calls counted as handled by the agent. |
| Avg Wrap-UpTime | The average length of time the agents spent in wrap-up work. |
| Total Wrap-UpTime | The total number of seconds agents spent in wrap-up work. |
| %Wrap-UpTime | The percentage of time that agents spent in the wrap-up state. |
| Other On PhoneTime | Total time the agent spent on Other calls. |

| Columns (Fields) | Description |
|---|---|
| Agent | The name of the agent, which includes the first and the last name of the agent. |
| MR Domain Name | The media routing domain name. |
| State | The state of the agent. For more information, see AgentState section in Database Schema Handbook for Cisco Unified Contact Center Enterprise at. https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html . |
| Logged OnTime | Total time, in seconds, the agent has been logged on. For this time to be accurate, ensure that time on the client machine
                                          is set correctly as per the timezone. |
| Not Ready Time | The total time that the agent spent in Not Ready state. For this time to be accurate, ensure that time on the client machine
                                          is set correctly as per the timezone. |
| Ready Time | The total time that the agent spent in Ready state. For this time to be accurate, ensure that time on the client machine is
                                          set correctly as per the timezone. |
| Handled Calls | The number of inbound calls that were answered and have completed wrap-up by the agent. |
| Handled Calls Time | Total handle time, in seconds, for inbound ACD calls counted as handled by the agent. The time that is spent from the call
                                          being answered by the agent to the time the agent wrap-up time for the call. Includes hold time associated with the call. |
| Handled Calls Talk Time | Total talk time in seconds, for Inbound ACD calls counted as handled by the agent. |
| Handled Calls Held | The total number of completed inbound ACD call agent placed on hold at least once. |
| Handled Calls Held Time | Total number of seconds completed inbound ACD calls were placed on hold. |
| Wrap-UpTime | The length of time the agent spent in wrap-up work. |
| Auto Out Calls | Total number of AutoOut (predictive) calls completed by the agent. |
| Auto Out Calls Time | Total handle time, in seconds, for completed AutoOut (predictive) calls handled by the agent. The value includes the time
                                          that is spent from the call being initiated to the time the agent wrap-up time for the call. The time includes hold time associated
                                          with the call. |
| Auto Out Calls Talk Time | Total talk time, in seconds, for completed AutoOut (predictive) calls handled by the agent. |
| Auto Out Calls Held Time | Total time, in seconds, for AutoOut (predictive) calls were placed on hold by the agent. |
| Auto Out Calls Held | The total number of completed AutoOut (predictive) calls that the agent has placed on hold at least once. |
| Agent Out Calls | Total number of completed outbound ACD calls made by the agent. |
| Agent Out Calls Time | Total handle time, in seconds, for completed outbound ACD calls handled by the agent. The value includes the time that is
                                          spent from the call being initiated by the agent to the time the agent wrap-up time for the call. The time includes hold time
                                          associated with the call. |
| Agent Out Calls Talk Time | Total talk time, in seconds, for completed outbound ACD calls handled by the agent. |
| Agent Out Calls Held | The total number of completed outbound ACD calls that the agent has placed on hold at least once. |
| Agent Out Calls Held Time | Total time, in seconds, the calls were placed on hold by the agent. |
| Internal Calls | Number of internal calls initiated by the agent. |
| Internal Calls Time | Total time, in seconds, spent on internal calls initiated by the agent. |
| Internal Calls Rcvd | Number of internal calls received by the agent. |
| Internal Calls Rcvd Time | Total time, in seconds, spent on internal calls received by the agent. |
| Internal Calls Held | The total number of internal calls the agent placed on hold at least once. |
| Internal Calls Held Time | Total time, in seconds, the completed internal calls that were placed on hold. |
| Preview Calls | Total number of outbound Preview calls completed by the agent. |
| Preview Calls Time | Total handle time, in seconds, for outbound Preview calls completed by the agent. The value includes the time that is spent
                                          from the call being initiated to the time the agent wrap-up time for the call. The time includes hold time associated with
                                          the call. |
| Preview Calls Talk Time | Total talk time, in seconds, of outbound Preview calls completed by the agent. |
| Preview Calls Held | The total number of completed outbound Preview calls the agent has placed on hold at least once. |
| Preview Calls Held Time | Total time, in seconds, for which outbound Preview calls were placed on hold. |
| Reserve Calls | For Outbound Option, the number of reservation calls received by an agent in this skill group during the reporting interval. |
| Reserve Calls Time | For Outbound Option, the time during the reporting interval that an outbound agent in this skill group spent on reservation
                                          calls waiting for the Campaign customer call to be delivered. This includes preview time for Preview, Direct Preview, and
                                          Personal Callback calls. |
| Reserve Calls Talk Time | For Outbound Option, the talk time for an agent in this skill group on reservation calls during the reporting interval. This
                                          is calculated using Call State. |
| Reserve Calls Held | For Outbound Option, the number of reservation calls for an agent in this skill group placed on hold during the reporting
                                          interval. |
| Reserve Calls Held Time | For Outbound Option, the time that reservation calls for an agent in this skill group are on hold during the reporting interval. |
| Non-ACD Call in Count | Total number of incoming calls received by the agent on Non-ACD line. |
| Non-ACD Call in Time | Total time in seconds, spent by the agent on a Non-ACD call. |
| Non-ACD Call Out Count | Total number of out going calls by the agent on Non-ACD line. |
| Non-ACD Call OutTime | Total time, in seconds, spent by the agent on a Non-ACD outbound call. |

| Note | The agent statistics that are displayed in this report resets during midnight at Peripheral Gateway. This report displays the statistics on daily basis. |
|---|---|

| Note | For more information on the fields and desciptons see, AgentState section in Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html |
|---|---|

| Columns (Fields) | Description |
|---|---|
| Agent | The name of the agent, which includes the first and the last name of the agent. |
| State | The state of the agent. For more information, see AgentState section in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at. https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html |
| Logged On Time | Total time, in seconds, the agent has been logged on. For this time to be accurate, ensure that time on the client machine
                                             is set correctly as per the timezone. |
| Not ReadyTime | The total time that the agent spent in Not Ready state. For this time to be accurate, ensure that time on the client machine
                                             is set correctly as per the timezone. |
| Ready Time | The total time that the agent spent in Ready state. For this time to be accurate, ensure that time on the client machine is
                                             set correctly as per the timezone. |
| % Not Ready Time | The percentage of time that the agent has spent in Not Ready state with respect to the total Logged On Time. |
| Handled Calls | The number of inbound calls that were answered and have completed wrap-up by the agent. |
| Avg Handled Calls Time | Average handle time in seconds, for inbound ACD calls counted as handled by the agent. The time that agent spent on the call
                                             to the time the agent wrap-up the work on the call. Includes hold time that is associated with the call. |
| Avg Handled Calls Talk Time | Average talk time, in seconds, for Inbound ACD calls counted as handled by the agent. |
| Avg Handled Calls Held Time | Average held time, in seconds, for Inbound ACD calls counted as handled by the agent. |
| Avg Wrap-UpTime | The average length of time the agents spent in wrap-up work. |
| Total Wrap-UpTime | The total number of seconds agents spent in wrap-up work. |
| %Wrap-UpTime | The percentage of time that agents spent in the wrap-up state. |
| Other On PhoneTime | Total time the agent spent on Other calls. |

| Columns (Fields) | Description |
|---|---|
| Agent | The name of the agent, which includes the first and the last name of the agent. |
| MR Domain Name | The media routing domain name. |
| State | The state of the agent. For more information, see AgentState section in Database Schema Handbook for Cisco Unified Contact Center Enterprise at. https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html . |
| Logged OnTime | Total time, in seconds, the agent has been logged on. For this time to be accurate, ensure that time on the client machine
                                          is set correctly as per the timezone. |
| Not Ready Time | The total time that the agent spent in Not Ready state. For this time to be accurate, ensure that time on the client machine
                                          is set correctly as per the timezone. |
| Ready Time | The total time that the agent spent in Ready state. For this time to be accurate, ensure that time on the client machine is
                                          set correctly as per the timezone. |
| Handled Calls | The number of inbound calls that were answered and have completed wrap-up by the agent. |
| Handled Calls Time | Total handle time, in seconds, for inbound ACD calls counted as handled by the agent. The time that is spent from the call
                                          being answered by the agent to the time the agent wrap-up time for the call. Includes hold time associated with the call. |
| Handled Calls Talk Time | Total talk time in seconds, for Inbound ACD calls counted as handled by the agent. |
| Handled Calls Held | The total number of completed inbound ACD call agent placed on hold at least once. |
| Handled Calls Held Time | Total number of seconds completed inbound ACD calls were placed on hold. |
| Wrap-UpTime | The length of time the agent spent in wrap-up work. |
| Auto Out Calls | Total number of AutoOut (predictive) calls completed by the agent. |
| Auto Out Calls Time | Total handle time, in seconds, for completed AutoOut (predictive) calls handled by the agent. The value includes the time
                                          that is spent from the call being initiated to the time the agent wrap-up time for the call. The time includes hold time associated
                                          with the call. |
| Auto Out Calls Talk Time | Total talk time, in seconds, for completed AutoOut (predictive) calls handled by the agent. |
| Auto Out Calls Held Time | Total time, in seconds, for AutoOut (predictive) calls were placed on hold by the agent. |
| Auto Out Calls Held | The total number of completed AutoOut (predictive) calls that the agent has placed on hold at least once. |
| Agent Out Calls | Total number of completed outbound ACD calls made by the agent. |
| Agent Out Calls Time | Total handle time, in seconds, for completed outbound ACD calls handled by the agent. The value includes the time that is
                                          spent from the call being initiated by the agent to the time the agent wrap-up time for the call. The time includes hold time
                                          associated with the call. |
| Agent Out Calls Talk Time | Total talk time, in seconds, for completed outbound ACD calls handled by the agent. |
| Agent Out Calls Held | The total number of completed outbound ACD calls that the agent has placed on hold at least once. |
| Agent Out Calls Held Time | Total time, in seconds, the calls were placed on hold by the agent. |
| Internal Calls | Number of internal calls initiated by the agent. |
| Internal Calls Time | Total time, in seconds, spent on internal calls initiated by the agent. |
| Internal Calls Rcvd | Number of internal calls received by the agent. |
| Internal Calls Rcvd Time | Total time, in seconds, spent on internal calls received by the agent. |
| Internal Calls Held | The total number of internal calls the agent placed on hold at least once. |
| Internal Calls Held Time | Total time, in seconds, the completed internal calls that were placed on hold. |
| Preview Calls | Total number of outbound Preview calls completed by the agent. |
| Preview Calls Time | Total handle time, in seconds, for outbound Preview calls completed by the agent. The value includes the time that is spent
                                          from the call being initiated to the time the agent wrap-up time for the call. The time includes hold time associated with
                                          the call. |
| Preview Calls Talk Time | Total talk time, in seconds, of outbound Preview calls completed by the agent. |
| Preview Calls Held | The total number of completed outbound Preview calls the agent has placed on hold at least once. |
| Preview Calls Held Time | Total time, in seconds, for which outbound Preview calls were placed on hold. |
| Reserve Calls | For Outbound Option, the number of reservation calls received by an agent in this skill group during the reporting interval. |
| Reserve Calls Time | For Outbound Option, the time during the reporting interval that an outbound agent in this skill group spent on reservation
                                          calls waiting for the Campaign customer call to be delivered. This includes preview time for Preview, Direct Preview, and
                                          Personal Callback calls. |
| Reserve Calls Talk Time | For Outbound Option, the talk time for an agent in this skill group on reservation calls during the reporting interval. This
                                          is calculated using Call State. |
| Reserve Calls Held | For Outbound Option, the number of reservation calls for an agent in this skill group placed on hold during the reporting
                                          interval. |
| Reserve Calls Held Time | For Outbound Option, the time that reservation calls for an agent in this skill group are on hold during the reporting interval. |
| Non-ACD Call in Count | Total number of incoming calls received by the agent on Non-ACD line. |
| Non-ACD Call in Time | Total time in seconds, spent by the agent on a Non-ACD call. |
| Non-ACD Call Out Count | Total number of out going calls by the agent on Non-ACD line. |
| Non-ACD Call OutTime | Total time, in seconds, spent by the agent on a Non-ACD outbound call. |

| Columns (Fields) | Description |
|---|---|
| Type | The
                                             						call type: Inbound or outbound call. The
                                             						value is Inbound or Outbound in the following scenarios: If
                                                   							 the agent receives a call, this field reports the call type as Inbound. If
                                                   							 the agent initiates a call, this field reports the call type as Outbound. If
                                                   							 Outbound Options feature initiates the call, this field reports the call type
                                                   							 as Inbound. |
| Number | The number of the phone that made or received the call. If the call is an inbound call, the number is picked from the Source
                                             field. If the call is an outbound call, the number is picked from the Destination field. Note When agents have not logged in, this field will display
                                                         										UNKNOWN for local CUCM DN. | Note | When agents have not logged in, this field will display
                                                         										UNKNOWN for local CUCM DN. |
| Note | When agents have not logged in, this field will display
                                                         										UNKNOWN for local CUCM DN. |
| Disposition | The
                                             						final disposition of the call. For more information on call disposition, see
                                             						the Database Schema Handbook for Cisco Unified Contact Center
                                                						  Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html . |
| Wrap-up
                                             						Reason | The data
                                             						entered by the agent during call wrap-up. |
| Queue | The
                                             						skill group name on which the agent handled the call. |
| Start
                                             						Time | The time
                                             						when the call started. |
| Duration | The
                                             						duration of the call in seconds. |

| Note | When agents have not logged in, this field will display
                                                         										UNKNOWN for local CUCM DN. |
|---|---|

| Columns (Fields) | Description |
|---|---|
| Agent | The name of the agent who is in the call. |
| Type | The call type: Inbound or outbound call. The value is Inbound or Outbound in the following scenarios: If the agent receives a call, this field reports the call type as Inbound. If the agent initiates a call, this field reports the call type as Outbound. If Outbound Options feature initiates the call, this field reports the call type as Inbound. |
| Number | The number of the phone that made or received the call. If the call is an inbound call, the number is picked from the Source
                                             field. If the call is an outbound call, the number is picked from the Destination field. Note When agents have not logged in, this field will display UNKNOWN for local CUCM DN. | Note | When agents have not logged in, this field will display UNKNOWN for local CUCM DN. |
| Note | When agents have not logged in, this field will display UNKNOWN for local CUCM DN. |
| Source | The peripheral number of the agent who initiated the call. |
| Destination | The DNIS value, provided by the ACD, that arrives with the call. |
| Disposition | The final disposition of the call. For more information on call disposition, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html . |
| Disposition Detail | The details of call disposition. |
| Wrap-up Reason | The data entered by the agent during call wrap-up. |
| Queue | The skill group name on which the agent handled the call. |
| Start Time | The time when the call started. |
| Talk Time | The cumulative time, in seconds, that the call was in a talking state on the destination device. Talk Time is a completed
                                             call time and not an agent state time. |
| Hold Time | The cumulative time, in seconds, for the call put on hold by an agent. |
| Duration | The duration of the call in seconds. |
| Ring Time | The number of seconds that the call spent ringing at the agent's phone before it was answered. |
| Delay Time | The time in seconds during which the call is active on the switch, but is not queued to a skill group or a trunk resource. |
| Answered | The status whether the call has been answered or not. It is true if the call is answered. |
| Peripheral Call Type | The type of the call reported by the peripheral. |
| Wrap-up Time | The cumulative number of seconds of the after-call work time associated with the call. |

| Note | When agents have not logged in, this field will display UNKNOWN for local CUCM DN. |
|---|---|

| Columns (Fields) | Description |
|---|---|
| Start
                                             						Time | The time
                                             						when the call started. |
| Duration | The
                                             						duration of the call in seconds. |
| Type | The call
                                             						type: Inbound or outbound call. The
                                             						value is Inbound or Outbound in the following scenarios: If
                                                   							 the agent receives a call, this field reports the call type as Inbound. If
                                                   							 the agent initiates a call, this field reports the call type as Outbound. If
                                                   							 Outbound Options feature initiates the call, this field reports the call type
                                                   							 as Inbound. |
| Number | The number of the phone that made or received the call. If the call is an inbound call, the number is picked from the Source
                                             field. If the call is an outbound call, the number is picked from the Destination field. Note When agents have not logged in, this field will display UNKNOWN for local CUCM DN. | Note | When agents have not logged in, this field will display UNKNOWN for local CUCM DN. |
| Note | When agents have not logged in, this field will display UNKNOWN for local CUCM DN. |
| Disposition | The
                                             						final disposition of the call. For more information on call disposition, see
                                             						the Database Schema Handbook for Cisco Unified Contact Center
                                                						  Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html . |
| Queue | The
                                             						skill group name on which the agent handled the call. |
| Wrap-up
                                             						Reason | The data
                                             						entered by the agent during call wrap-up. |

| Note | When agents have not logged in, this field will display UNKNOWN for local CUCM DN. |
|---|---|

| Columns (Fields) | Description |
|---|---|
| Start Time | Time when the agent started being in this state. |
| State | The state of the agent. For more information on agent state, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html . |
| Reason | The reason why the agent entered the Not Ready state. Note: If an agent is Not Ready, the Not Ready reason is updated when the agent goes to Ready or to another Not Ready state with
                                             a different Reason. If the Not Ready agent receives an internal call or makes an outbound call, Reason continues to show the
                                             current Not Ready reason. |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. |

| Columns (Fields) | Description |
|---|---|
| Agent Name | The name of the agent, which includes the Last Name and the First Name. |
| Start Time | Time when the agent started being in this state. |
| State | The state of the agent. For more information on agent state, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html . |
| Reason | The reason why the agent entered the Not Ready state. Note: If an agent is Not Ready, the Not Ready reason is updated when the agent goes to Ready or to another Not Ready state with
                                             a different Reason. If the Not Ready agent receives an internal call or makes an outbound call, Reason continues to show the
                                             current Not Ready reason. |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. |
| Domain | The media routing domain name. |

| Note | For Avaya PG, only the base skill groups are displayed in the Live Data report. All the agent activities that are performed
                                          in the sub-skill groups are reported against the base skill group. |
|---|---|

| Columns (Fields) | Description |
|---|---|
| Precision Queue/Skill Group | The
                                             						enterprise name of the precision queue or the skill group associated with the
                                             						task on which the agent is currently working. If the agent is not involved in
                                             						any task in the media routing domain, this field shows Not Applicable. Because
                                             						an agent can be logged into multiple skill groups, this field is not filled
                                             						until the agent is assigned a task. If not
                                             						applicable, the column is left blank. |
| Agent Name | The name
                                             						of the agent. |
| State | The
                                             						current state of the agent. |
| Reason | The
                                             						reason code and text indicating the reason the agent entered the Not Ready
                                             						state. Note: If an agent is
                                             						Not Ready, the Not Ready reason code and text are only updated when the agent
                                             						goes to Ready or to another Not Ready state with a different Reason code. If
                                             						the Not Ready agent receives an internal call or makes an outbound call, Reason
                                             						continues to show the current Not Ready code and text. |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. For this time to be accurate, ensure
                                             that time on the client machine is set correctly as per the timezone. |
| Domain | The
                                             						media routing domain name. |
| Direction | The
                                             						direction of the call that the agent is currently working on: In Out Other In Other Out Out Reserve Out Preview Out Predictive Not Applicable (if the logged in agent is not active in the skill group) |
| Logged On | The date
                                             						and time the agent logged in with the given set of skills, measured in
                                             						MM:DD:YYYY (month, day, year) and HH:MM:SS (hours, minutes, seconds) format. |
| Destination | The type
                                             						of outbound task on which the agent is currently working: 1 = ACD 2 = Direct 3 = Auto Out 4 = Reserve 5 = Preview All other values = Not Applicable |
| Attributes | The
                                             						names of the attributes used in the precision queue definition. The report
                                             						shows only those attributes that are used. |

| Column (Field) | Description |
|---|---|
| Precision Queue/Skill Group | The
                                             						enterprise name of the precision queue or the skill group associated with the
                                             						task on which the agent is currently working. If the agent is not involved in
                                             						any task in the media routing domain, this field shows Not Applicable. Because
                                             						an agent can be logged into multiple skill groups, this field is not filled
                                             						until the agent is assigned a task. If not
                                             						applicable, the column is left blank. |
| Agent Name | The name
                                             						of the agent. Composed of Last Name, First Name. |
| State | The
                                             						current state of the agent. |
| Reason | The
                                             						reason code and text indicating the reason the agent entered the Not Ready
                                             						state. Note: If an agent is
                                             						Not Ready, the Not Ready reason code and text are only updated when the agent
                                             						goes to Ready or to another Not Ready state with a different Reason code. If
                                             						the Not Ready agent receives an internal call or makes an outbound call, Reason
                                             						continues to show the current Not Ready code and text. |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. |
| Domain | The
                                             						media routing domain name. |
| Direction | The
                                             						direction of the call that the agent is currently working on: In Out Other In Other Out Out Reserve Out Preview Out Predictive Not Applicable (if the logged in agent is not active in the skill group) |
| Logged On | The date
                                             						and time that the agent logged in. The format is MM/DD/YYYY (month, day, year)
                                             						and HH:MM:SS (hours, minutes, seconds) format. |
| Destination | The type
                                             						of outbound task on which the agent is currently working: 1 = ACD 2 = Direct 3 = Auto Out 4 = Reserve 5 = Preview All other values = Not Applicable |
| Extension | The
                                             						phone extension into which the agent is logged. |
| Available in MRD | Whether
                                             						or not the agent is available to accept a task in this Media Routing Domain: NO (Not available) YES_ICM ( Unified CCE available in media routing domain) YES_APP (Application available in media routing domain) All other values = No An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready; the agent is not at the agent's maximum task limit for the MRD; and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is Unified CCE -available, then the Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only the Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent. |
| Device
                                             						Type | The kind of phone being used: 0 = Local agent; normal ACD/ Unified CCE phone or non-voice task. 1 = Remote phone, call by call (Mobile agent's phone is connected for each incoming call). 2 = Remote phone, nailed connection (Mobile agent calls and logs in once; line remains connected through multiple calls). |
| Team | The
                                             						Enterprise Name of the Agent Team. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |
| Tasks
                                             						in Progress | The number of tasks currently queued for the agent's skill group. |
| Max
                                             						Tasks | The
                                             						maximum number of tasks that may be assigned to an agent. |
| On
                                             						Hold | Agent
                                             						on hold: 1 = Yes All other values = No |
| Requested Supervisor Assist | Whether or not the agent requested supervisor assistance: 1 = Yes All other values = No |
| Routable | Calls
                                             						can be routed to the agent: 1 = Yes All other values = No |
| Reason
                                             						Code | A code
                                             						received from the peripheral that indicates the reason for the agent's last
                                             						state change. If not defined, Reason is None. |

| Column (Fields) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the precision queue. |
| Domain | The enterprise name of the Media Routing Domain associated with the precision queue. Domain is derived from: Media_Routing_Domain.EnterpriseName. |
| Queued | The number of tasks currently queued for the precision queue. |
| Longest Queued | The
                                             						longest time in hours, minutes, and seconds (HH:MM:SS) that a task has been
                                             						waiting in the precision queue to be handled by an agent. |
| Logged
                                             						On | The
                                             						number of agents who are currently logged in to the precision queue. This count
                                             						is updated each time an agent logs on and each time an agent logs off. |
| CURRENT STATE
                                                						  DISTRIBUTION |
| Ready | The
                                             						number of agents in the precision queue in the Ready state. |
| Reserved | The
                                             						number of agents in the precision queue who are in Reserved state and awaiting
                                             						incoming tasks. |
| Active
                                             						In | The
                                             						number of agents in the precision queue who are currently working on incoming
                                             						tasks. |
| Active
                                             						Out | The
                                             						number of agents in the precision queue who are currently working on outbound
                                             						tasks. |
| Active
                                             						Other | The
                                             						number of agents in the precision queue who are currently working on internal
                                             						(neither inbound nor outbound) tasks. |
| Hold | The
                                             						number of agents who have all active calls on hold or whose state to the
                                             						precision queue is Paused. The
                                             						agent is not in the Hold state with one call on hold and talking on another
                                             						call (for example, a consultative call). The agent must have all active calls
                                             						on hold. |
| Wrap
                                             						Up | The
                                             						number of agents in the precision queue who are in the Work Not Ready state and
                                             						Work Ready state. The
                                             						Work Not Ready state is a state in which an agent is involved in after task
                                             						work and is assumed not to be ready to accept incoming tasks when done. The
                                             						Work Ready state is a state in which an agent is involved in after a task work
                                             						and is assumed to be ready to accept incoming tasks when done. |
| Not
                                             						Ready | The
                                             						number of agents in the precision queue who are in the Not Ready state, a state
                                             						in which agents are logged in but are neither involved in any task handling
                                             						activity nor available to handle a task. |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy Other is a state in
                                             						which the agent is handling calls assigned to other precision queues during the
                                             						interval. For
                                             						example, an agent might be talking on an inbound call in one precision queue
                                             						while simultaneously logged on to and ready to accept calls from other
                                             						precision queues. The agent can be active (talking on or handling calls) in
                                             						only one precision queue at a time. Therefore, while active in one precision
                                             						queue, for the other precision queue the agent is considered to be in the Busy
                                             						Other state. |
| TO INTERVAL |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the precision queue during the current
                                             interval. |
| Average Handle Time | The average time spent by  agents in the precision queue in handling a task during the current interval, measured in HH:MM:SS
                                             (hours, minutes, seconds). |
| % Ready | The percentage of Logged On time during which an agent was Ready during the current interval. |
| TODAY |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the precision queue today. |
| Average Handle Time | The average time spent by  agents in the precision queue in handling a task today, measured in HH:MM:SS (hours, minutes, seconds). |
| % Ready | The percentage of Logged On time during which an agent was Ready today. |

| Column (Field) | Description |
|---|---|
| Precision Queue | The
                                          					 enterprise name of the precision queue. |
| Domain | The enterprise name of the Media Routing Domain associated with the skill group. Domain is derived from: Media_Routing_Domain.EnterpriseName. |
| Queued | The number of tasks currently queued for the precision queue. |
| Longest Queued | The longest call in queue as reported by the router. |
| Logged
                                          					 On | The
                                          					 number of agents who are currently logged in to the precision queue. This count is
                                          					 updated each time an agent logs on and each time an agent logs off. |
| CURRENT STATE
                                             						DISTRIBUTION |
| Ready | The
                                          					 number of agents in the precision queue in the Ready state. |
| Reserved | The
                                          					 number of agents in the precision queue who are in Reserved state and awaiting
                                          					 incoming tasks. |
| Active
                                          					 In | The
                                          					 number of agents in the precision queue who are currently working on incoming
                                          					 tasks. |
| Active
                                          					 Out | The
                                          					 number of agents in the precision queue who are currently working on outbound
                                          					 tasks. |
| Active
                                          					 Other | The
                                          					 number of agents in the precision queue who are currently working on internal
                                          					 (neither inbound nor outbound) tasks. |
| Hold | The
                                          					 number of agents who have all active calls on hold or whose state to the precision queue is Paused. The
                                          					 agent is not in the Hold state with one call on hold and talking on another
                                          					 call (for example, a consultative call). The agent must have all active calls
                                          					 on hold. |
| Wrap Up | The
                                          					 number of agents in the precision queue who are in the Work Not Ready state and
                                          					 Work Ready state. The Work
                                          					 Not Ready state is a state in which an agent is involved in after task work and
                                          					 is assumed not to be ready to accept incoming tasks when done. The Work Ready
                                          					 state is a state in which an agent is involved in after a task work and is
                                          					 assumed to be ready to accept incoming tasks when done. |
| Not
                                          					 Ready | The
                                          					 number of agents in the precision queue who are in the Not Ready state, a state in
                                          					 which agents are logged in but are neither involved in any task handling
                                          					 activity nor available to handle a task. |
| Busy
                                          					 Other | The
                                          					 number of agents currently in the BusyOther state. Busy Other is a state in
                                          					 which the agent is handling calls assigned to other precision queues during the
                                          					 interval. For
                                          					 example, an agent might be talking on an inbound call in one precision queue while
                                          					 simultaneously logged on to and ready to accept calls from other precision queues.
                                          					 The agent can be active (talking on or handling calls) in only one precision queue
                                          					 at a time. Therefore, while active in one precision queue, for the other precision queue the agent is considered to
                                          be in the Busy Other state. |
| TO INTERVAL |
| Logged On | The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this precision queue during the current
                                          interval. |
| Ready | The total time in seconds an agent associated with this precision queue was in the Not_Active state with respect to this precision
                                          queue during the current interval. AvailTime is included in the calculation of LoggedOnTime. |
| Not Ready | The total time that the agents spent in Not Ready state for this skill for the current interval. This value is taken directly
                                          from the database. |
| % Ready | The percentage of Logged On time during which agents were Ready during the current interval. |
| TODAY |
| Logged On | The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this precision queue today. |
| Ready | The total time in seconds an agent associated with this precision queue was in the Not_Active state with respect to this precision
                                          queue today. AvailTime is included in the calculation of LoggedOnTime. |
| Not Ready | The total time that the agents spent in Not Ready state for this skill today. This value is taken directly from the database. |
| % Ready | The percentage of Logged On time during which an agent was Ready today. |

| Column (Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the precision queue. |
| Domain | The enterprise name of the Media Routing Domain associated with the precision queue. Domain is derived from: Media_Routing_Domain.EnterpriseName. |
| Queued | The number of tasks currently queued for the precision queue. |
| Longest Queued | The longest call in queue as reported by the router. |
| Logged
                                             						On | The
                                             						number of agents who are currently logged in to the precision queue. This count
                                             						is updated each time an agent logs on and each time an agent logs off. |
| CURRENT STATE
                                                						  DISTRIBUTION |
| Ready | The
                                             						number of agents in this precision queue in the Ready state. |
| Reserved | The
                                             						number of agents in this precision queue who are in Reserved state and awaiting
                                             						incoming tasks. |
| Active
                                             						In | The
                                             						number of agents in this precision queue who are currently working on incoming
                                             						tasks. |
| Active
                                             						Out | The
                                             						number of agents in this precision queue who are currently working on outbound
                                             						tasks. |
| Active
                                             						Other | The
                                             						number of agents in this precision queue who are currently working on internal
                                             						(neither inbound nor outbound) tasks. |
| Hold | The
                                             						number of agents who have all active calls on hold or whose state to the
                                             						precision queue is Paused. The
                                             						agent is not in the Hold state with one call on hold and talking on another
                                             						call (for example, a consultative call). The agent must have all active calls
                                             						on hold. |
| Wrap Up | The
                                             						number of agents in this precision queue who are in the Work Not Ready state
                                             						and Work Ready state. The Wrap Up state is a state in which an agent is involved in after task work and is assumed not to be ready to accept incoming
                                             tasks when done. The Work Ready state is a state in which an agent is involved in after a task work and is assumed to be ready to accept incoming
                                             tasks when done. |
| Not
                                             						Ready | The
                                             						number of agents in this precision queue who are in the Not Ready state, a
                                             						state in which agents are logged in but are neither involved in any task
                                             						handling activity nor available to handle a task. |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy Other is a state in
                                             						which the agent is handling calls assigned to other precision queues during the
                                             						interval. For
                                             						example, an agent might be talking on an inbound call in one precision queue
                                             						while simultaneously logged on to and ready to accept calls from other
                                             						precision queues. The agent can be active (talking on or handling calls) in
                                             						only one precision queue at a time. Therefore, while active in one precision
                                             						queue, for the other precision queue the agent is considered to be in the Busy
                                             						Other state. |
| OUTBOUND OPTION STATES |
| Active
                                             						Reserve | The
                                             						number of agents in the precision queue currently talking on agent reservation
                                             						calls. |
| Active
                                             						Preview | The
                                             						number of agents in the precision queue currently talking on outbound Preview
                                             						calls. |
| Active
                                             						Auto Out | The
                                             						number of agents in the precision queue currently talking on AutoOut
                                             						(predictive) calls. |
| (no header) |
| ICM
                                             						Available | The number of agents belonging to this precision queue who are currently ICMAvailable for the MRD associated with this precision queue. Agents are ICMAvailable if they are Routable and Available for the MRD.
                                             If an agent is ICMAvailable , the system
                                             software can assign tasks to the agent. |
| Eligible | The number of agents who are Routable for the MRD associated with this precision queue, and whose state in this precision
                                             queue is currently something other than NOT_READY or WORK_NOT_READY. |
| WRAPUP STATE
                                                						  DISTRIBUTION |
| Work
                                             						Ready | The
                                             						agent is performing wrap-up work for a call or task in the precision queue. If the
                                             						agent is handling a voice call, the agent enters Not Active state when wrap-up
                                             						is complete. If the agent is handling a non-voice task, the agent might enter
                                             						Not Active or Not Ready state when wrap-up is complete. |
| Wrap Up | The
                                             						agent is performing wrap-up work for a call in the precision queue. The agent
                                             						enters Not Ready state when wrap-up is complete. |
| (no header) |
| Application
                                             						Available | The
                                             						number of agents belonging to this precision queue who are currently
                                             						Application Available with respect to the MRD to which the precision queue
                                             						belongs. An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready; the agent is not at the agent's maximum task limit for the MRD; and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is Application-available, then only an application in the MRD, for example chat, can assign
                                             tasks to the agent. |
| TO INTERVAL |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the precision queue during the current
                                             interval. |
| Avg Handle Time | The average time spent by  agents in handling a task during the current interval, measured in HH:MM:SS (hours, minutes, seconds). |
| Logged On | The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this precision queue during the current
                                             interval. |
| Ready | The total time in seconds an agent associated with this precision queue was in the Not_Active state with respect to this precision
                                             queue during the current interval. AvailTime is included in the calculation of LoggedOnTime. |
| Not Ready | The total time that the agents spent in Not Ready state for this skill for the current interval. This value is taken directly
                                             from the database. |
| % Ready | The percentage of Logged On time during which agents were Ready during the current interval. |
| TODAY |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the precision queue today. |
| Avg Handle Time | The average time spent by  agents in handling a task today, measured in HH:MM:SS (hours, minutes, seconds). |
| Logged On | The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this precision queue today. |
| Ready | The total time in seconds an agent associated with this precision queue was in the Not_Active state with respect to this precision
                                             queue today. AvailTime is included in the calculation of LoggedOnTime. |
| Not Ready | The total time that the agents spent in Not Ready state for this skill today. This value is taken directly from the database. |
| % Ready | The percentage of Logged On time during which an agent was Ready today. |

| Columns (Fields) | Description |
|---|---|
| Skill
                                          					 Group | The
                                          					 enterprise name of the skill group. |
| Domain | The enterprise name of the Media Routing Domain associated with the skill group. Domain is derived from: Media_Routing_Domain.EnterpriseName. |
| Router |
| Queued | The number of tasks currently queued for the skill group in the Router queue. |
| Longest in Queue | The longest call in queue as reported by the router. |
| Local |
| Queued | The number of tasks currently queued for the skill group in the Router queue. |
| Longest Queued | The longest call in queue as reported by the router. |
| Logged
                                          					 On | The number of agents who are currently logged in to the skill group. This count is updated each time an agent logs on and
                                          each time an agent logs off. |
| Current State Distribution |
| Ready | The number of agents in the skill group in the Ready state. |
| Reserved | The number of agents in the skill group who are in Reserved state and awaiting incoming tasks. |
| Active
                                          					 In | The number of agents in the skill group who are currently working on incoming tasks. |
| Active
                                          					 Out | The number of agents in the skill group who are currently working on outbound tasks. |
| Active
                                          					 Other | The number of agents in the skill group who are currently working on internal (neither inbound nor outbound) tasks. |
| Hold | The number of agents who have all active calls on hold or whose state to the skill group is Paused. The
                                          					 agent is not in the Hold state with one call on hold and talking on another
                                          					 call (for example, a consultative call). The agent must have all active calls
                                          					 on hold. |
| Wrap Up | The number of agents in the skill group who are in the Wrap Up state and Ready state. The Wrap Up state is a state in which an agent is involved in after task work and is assumed not to be ready to accept incoming
                                          tasks when done. The Ready state is a state in which an agent is involved in after a task work and is assumed to be ready to accept incoming
                                          tasks when done. |
| Not
                                          					 Ready | The
                                          					 number of agents in the skill group who are in the Not Ready state, a state in
                                          					 which agents are logged in but are neither involved in any task handling
                                          					 activity nor available to handle a task. |
| Busy
                                          					 Other | The
                                          					 number of agents currently in the BusyOther state. Busy Other is a state in
                                          					 which the agent is handling calls assigned to other skill groups during the
                                          					 interval. For
                                          					 example, an agent might be talking on an inbound call in one skill group while
                                          					 simultaneously logged on to and ready to accept calls from other skill groups.
                                          					 The agent can be active (talking on or handling calls) in only one skill group
                                          					 at a time. Therefore, while active in one skill group, for the other skill
                                          					 group the agent is considered to be in the Busy Other state. |
| To Interval |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the skill group during the current
                                          interval. |
| Average Handle Time | The average time spent by  agents in handling a task during the current interval, measured in HH:MM:SS (hours, minutes, seconds). |
| Today |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the skill group today. |
| Average Handle Time | The average time spent by  agents in handling a task today, measured in HH:MM:SS (hours, minutes, seconds). |
| (no header) |
| Longest Task In Queue | The longest time in hours, minutes, and seconds (HH:MM:SS) that a task has been waiting to be handled by an agent. |
| Tasks Queued | The number of tasks queued to this Skill Group. |

| Columns (Fields) | Description |
|---|---|
| Skill
                                          					 Group | The
                                          					 enterprise name of the skill group. |
| Domain | The enterprise name of the Media Routing Domain associated with the skill group. Domain is derived from: Media_Routing_Domain.EnterpriseName. |
| Router |
| Queued | The
                                          					 number of tasks currently queued for the skill group in the Router queue. |
| Router Longest Task in Queue | The longest call in queue as reported by the router. |
| Local |
| Queued | The
                                          					 number of tasks currently queued for the skill group in the Router queue. |
| Longest Queued | The longest call in queue as reported by the router. |
| (no header) |
| Logged
                                          					 On | The
                                          					 number of agents who are currently logged in to the skill group. This count is
                                          					 updated each time an agent logs on and each time an agent logs off. |
| Current State Distribution |
| Ready | The
                                          					 number of agents in the skill group in the Ready state. |
| Reserved | The
                                          					 number of agents in the skill group who are in Reserved state and awaiting
                                          					 incoming tasks. |
| Active
                                          					 In | The
                                          					 number of agents in the skill group who are currently working on incoming
                                          					 tasks. |
| Active
                                          					 Out | The
                                          					 number of agents in the skill group who are currently working on outbound
                                          					 tasks. |
| Active
                                          					 Other | The
                                          					 number of agents in the skill group who are currently working on internal
                                          					 (neither inbound nor outbound) tasks. |
| Hold | The
                                          					 number of agents who have all active calls on hold or whose state to the skill
                                          					 group is Paused. The
                                          					 agent is not in the Hold state with one call on hold and talking on another
                                          					 call (for example, a consultative call). The agent must have all active calls
                                          					 on hold. |
| Wrap Up | The number of agents in the skill group who are in the Wrap Up state and Work Ready state. The Wrap Up state is a state in which an agent is involved in after task work and is assumed not to be ready to accept incoming
                                          tasks when done. The Work Ready state is a state in which an agent is involved in after a task work and is assumed to be ready
                                          to accept incoming tasks when done. |
| Not
                                          					 Ready | The
                                          					 number of agents in the skill group who are in the Not Ready state, a state in
                                          					 which agents are logged in but are neither involved in any task handling
                                          					 activity nor available to handle a task. |
| Busy
                                          					 Other | The number of agents currently in the Busy Other state. Busy Other is a state in which the agent is handling calls assigned
                                          to other skill groups during the interval. For
                                          					 example, an agent might be talking on an inbound call in one skill group while
                                          					 simultaneously logged on to and ready to accept calls from other skill groups.
                                          					 The agent can be active (talking on or handling calls) in only one skill group
                                          					 at a time. Therefore, while active in one skill group, for the other skill
                                          					 group the agent is considered to be in the Busy Other state. |
| To Interval |
| Logged On | The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this skill group during the current
                                          interval. |
| Ready | The total time in seconds an agent associated with this skill group was in the Not_Active state with respect to this skill
                                          group during the current interval. AvailTime is included in the calculation of LoggedOnTime. |
| Not Ready | The total time that the agents spent in Not Ready state for this skill for the current interval. This value is taken directly
                                          from the database. |
| % Ready | The percentage of Logged On time during which agents were Ready during the current interval. |
| Today |
| Logged On | The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this skill group today. |
| Ready | The total time in seconds an agent associated with this skill group was in the Not_Active state with respect to this skill
                                          group today. AvailTime is included in the calculation of LoggedOnTime. |
| Not Ready | The total time that the agents spent in Not Ready state for this skill today. This value is taken directly from the database. |
| % Ready | The percentage of Logged On time during which an agent was Ready today. |
| (no header) |
| Longest Task In Queue | The longest time in hours, minutes, and seconds (HH:MM:SS) that a task has been waiting to be handled by an agent. |
| Tasks Queued | The number of tasks queued to this Skill Group. |

| Columns (Fields) | Description |
|---|---|
| Skill
                                             						Group | The
                                             						enterprise name of the skill group. |
| Domain | The enterprise name of the Media Routing Domain associated with the skill group. Domain is derived from: Media_Routing_Domain.EnterpriseName. |
| Router |
| Queued | The
                                             					 number of tasks currently queued for the skill group in the Router queue. |
| Longest in Queue | The longest call in queue as reported by the router. |
| Local |
| Queued | The
                                             					 number of tasks currently queued for the skill group in the Router queue. |
| Longest Queued | The longest call in queue as reported by the router. |
| (no header) |
| Logged
                                             						On | The
                                             						number of agents who are currently logged in to the skill group. This count is
                                             						updated each time an agent logs on and each time an agent logs off. |
| Current State Distribution |
| Ready | The
                                             						number of agents in the skill group in the Ready state. |
| Reserved | The
                                             						number of agents in the skill group who are in Reserved state and awaiting
                                             						incoming tasks. |
| Active
                                             						In | The
                                             						number of agents in the skill group who are currently working on incoming
                                             						tasks. |
| Active
                                             						Out | The
                                             						number of agents in the skill group who are currently working on outbound
                                             						tasks. |
| Active
                                             						Other | The
                                             						number of agents in the skill group who are currently working on internal
                                             						(neither inbound nor outbound) tasks. |
| Hold | The
                                             						number of agents who have all active calls on hold or whose state to the skill
                                             						group is Paused. The
                                             						agent is not in the Hold state with one call on hold and talking on another
                                             						call (for example, a consultative call). The agent must have all active calls
                                             						on hold. |
| Wrap Up | The number of agents in the skill group who are in the Wrap Up state and Work Ready state. The Wrap Up state is a state in which an agent is involved in after task work and is assumed not to be ready to accept incoming tasks
                                             when done. The Work Ready state is a state in which an agent is involved in after a task work and is assumed to be ready to accept incoming tasks
                                             when done. |
| Not
                                             						Ready | The
                                             						number of agents in the skill group who are in the Not Ready state, a state in
                                             						which agents are logged in but are neither involved in any task handling
                                             						activity nor available to handle a task. |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy Other is a state in
                                             						which the agent is handling calls assigned to other skill groups during the
                                             						interval. For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged on to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state. |
| Outbound Option States |
| Active
                                             						Reserve | The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls. |
| Active
                                             						Preview | The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls. |
| Active
                                             						Auto Out | The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls. |
| (no header) |
| ICM
                                             						Available | The number of agents belonging to this skill
                                             group who are currently ICMAvailable for the MRD associated with this skill group. Agents are ICMAvailable if they are Routable and Available for the MRD.
                                             If an agent is ICMAvailable , the system
                                             software can assign tasks to the agent. |
| Eligible | The number of agents who are Routable for the MRD associated with this skill group, and whose agent state in this skill
                                             group is currently something other than NOT_READY or WORK_NOT_READY. |
| Wrap Up State Distribution |
| Ready | The
                                             						agent is performing wrap-up work for a call or task in the skill group. If the
                                             						agent is handling a voice call, the agent enters Not Active state when wrap-up
                                             						is complete. If the agent is handling a non-voice task, the agent might enter
                                             						Not Active or Not Ready state when wrap-up is complete. |
| Wrap Up | The
                                             						agent is performing wrap-up work for a call in the skill group. The agent
                                             						enters Not Ready state when wrap-up is complete. |
| (no header) |
| Application Available | The
                                             						number of agents belonging to this skill group who are currently
                                             						Application Available with respect to the MRD to which the skill group belongs.
                                             						An agent is Application available if the agent is Not Routable and Available
                                             						for the MRD. |
| To Interval |
| Logged On | The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this skill group during the current
                                             interval. |
| Ready | The total time in seconds an agent associated with this skill group was in the Not_Active state with respect to this skill
                                             group during the current interval. AvailTime is included in the calculation of LoggedOnTime. |
| Not Ready | The total time that the agents spent in Not Ready state for this skill for the current interval. This value is taken directly
                                             from the database. |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the skill group during the current
                                             interval. |
| Avg Handle Time | The average time spent by  agents in handling a task during the current interval, measured in HH:MM:SS (hours, minutes, seconds). |
| % Ready | The percentage of Logged On time during which agents were Ready during the current interval. |
| Today |
| Logged On | The total time in HH:MM:SS (hours, minutes, and seconds) that agents were logged into this skill group today. |
| Ready | The total time in seconds an agent associated with this skill group was in the Not_Active state with respect to this skill
                                             group today. AvailTime is included in the calculation of LoggedOnTime. |
| Not Ready | The total time that the agents spent in Not Ready state for this skill today. This value is taken directly from the database. |
| Handled | The number of inbound calls that were answered and have completed wrap-up by agents in the skill group today. |
| Avg Handle Time | The average time spent by  agents in handling a task today, measured in HH:MM:SS (hours, minutes, seconds). |
| % Ready | The percentage of Logged On time during which an agent was Ready today. |