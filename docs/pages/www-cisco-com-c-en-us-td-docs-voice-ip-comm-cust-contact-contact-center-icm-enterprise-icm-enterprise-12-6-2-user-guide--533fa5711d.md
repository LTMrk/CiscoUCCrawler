---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-guide--533fa5711d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/guide/ucce_b_cisco-unified-contact-center-enterprise-reporting-user-guide-release1262/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_01010.html
retrieved_at: 2026-08-21T12:00:06.524204+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(2)

Updated: May 4, 2023

Chapter: All Fields Real Time Reports

## Chapter: All Fields Real Time Reports

# All Fields Real Time Reports

## Agent Precision
                        	 Queue Membership

Agent Precision
                              		  Queue Membership displays the active membership of agents in precision queues
                              		  along with the attributes in those precision queues. Note that this membership
                              		  is dynamic so this information is available in real-time only.

Query: This report data
                              		  is built from a Database Query.

Views: This report has one grid view, Agent Precision Queue Membership.

Grouping: This report is grouped by Agent.

Value List: Agent

Database Schema Tables from which data is retrieved:

Agent

Agent_Skill_Group_Real_Time

Attribute

Person

Precision Queue

### Available Fields
                           	 in the Agent Precision Queue Membership Grid View

Additional
                                 		  Available fields in this report are populated from fields in the
                                 		  Agent_Skill_Group_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Note also that:

Precision
                                       				Queue is derived from: Precision_Queue.EnterpriseName

Attribute
                                       				[1- n ] is derived
                                       				from: Attribute.EnterpriseName

### Current Fields in
                           	 the Agent Precision Queue Membership Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Agent

The last
                                             						and first name of the agent.

Derived
                                             						from: Person.LastName "," Person.FirstName

Precision Queue

The precision queues with which the agent is associated.

Derived
                                             						from: Precision_Queue.EnterpriseName

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

### Available Fields
                           	 in the Agent Precision Queue Membership Grid View

Additional
                                 		  Available fields in this report are populated from fields in the
                                 		  Agent_Skill_Group_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Note also that:

Precision
                                       				Queue is derived from: Precision_Queue.EnterpriseName

Attribute
                                       				[1- n ] is derived
                                       				from: Attribute.EnterpriseName

### Current Fields in
                           	 the Agent Precision Queue Membership Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Agent

The last
                                             						and first name of the agent.

Derived
                                             						from: Person.LastName "," Person.FirstName

Precision Queue

The precision queues with which the agent is associated.

Derived
                                             						from: Precision_Queue.EnterpriseName

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

## Agent Queue Real
                        	 Time

Agent Queue Real
                              		  Time provides combined information for Skill Groups and Precision Queues. Note
                              		  that agents with multiple skills or Precision Queues have a line item for each
                              		  one in this report. Use this report to understand activity and staffing of
                              		  Skill Groups and Precision Queues.

Views: This report has one grid view, Agent Queue Real Time.

Query: This report data
                              		  is built from a Database Query.

Grouping: This report is grouped by Skill Group.

Value List: Agent

Database Schema Tables from which data is retrieved:

Agent

Agent_Real_Time

Agent_Skill_Group_Real_Time

Attribute

Controller_Time

Media_Routing_Domain

Person

Precision Queue

Reason_Code

Service

Skill_Group

Skill_Group_Real_Time

### Available Fields in
                           	 the Agent Queue Real Time Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current.

Additional Available
                                 		  fields in this report are populated from fields in the Agent_Real_Time table as
                                 		  documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Note also that:

Media is derived from:
                                       				Media_Routing_Domain.EnterpriseName.

Service Name is derived
                                       				from: Service.EnterpriseName.

Enterprise Name is
                                       				derived from: Agent.EnterpriseName.

### Current Fields in the Agent Queue Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Precision Queue / Skill Group

Precision Queue or Skill Group or NotApplicable.

Precision
                                             						Queue is derived from:Precision_Queue.EnterpriseName.

The
                                             						precision route associated with the task on which the agent is currently
                                             						working. If the agent is not involved in any task in the media routing domain,
                                             						this field shows Not Applicable. Because an agent can log in to multiple
                                             						precision routes, this field is not filled until the agent is assigned a task.

Skill
                                             						Group Name is derived from: Skill_Group.EnterpriseName.

The skill
                                             						group associated with the task on which the agent is currently working. If the
                                             						agent is not involved in any task in the media routing domain, this field shows
                                             						Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             						this field is not filled until the agent is assigned a task.

Attributes 1 to 10

The attributes used in the precision queue definition. The report shows only those attributes that are used.

Derived from: Attribute.EnterpriseName

Agent

The last and first name of the agent.

Derived from: Person.LastName "," Person.FirstName.

Queued Now

The Queued Now field is a calculated field based onthe Agent_Real_Time.

The number in the field increments only if:

The ICM Script uses Queue to Agent Node.

The agent is not available to take the call.

There is no other way for the router to queue a call at an agent.

Extension

The phone extension into which the agent is logged.

Derived from: Agent_Real_Time.Extension

Agent State

The current state of the agent in this skill group.

Derived from:

Agent_Skill_Group_Real_Time.AgentState

Logged on Date Time

The time spent in the current agent state in this skill group in HH:MM:SS (hours, minutes, seconds) format.

Derived from: Agent_Real_Time.DateTimeLogin

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, getdate()).

Mobile Agent Mode

The mode by which the agent is connected (populated for CCE only):

0 = Not Mobile (Local agent; general ACD/CCE phone or non-voice task)

1 = Call By Call (Mobile agent's phone is connected for each incoming call)

2 = Nailed Connection (Mobile agent calls andlogs in once; line remains connected through multiple calls)

Derived from: Agent_Real_Time.PhoneType

Mobile Agent Phone#

For a mobile agent (an agent working remotely), the current phone number. Populated for CCE only.

Derived from:

Agent_Real_Time.RemotePhoneNumber

Reason

A code received from the peripheral that indicates the reason for the agent's last state change. If the code is not defined,
                                             this displays 0.

To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information.

Derived from: Agent_Real_Time.ReasonCode.

Supervisor Assist Requested

Whether or not the agent requested supervisor assistance: No|Yes.

Derived from:

Agent_Real_Time.RequestedSupervisorAssist

Destination

The type of outbound task on which the agent is currently working.

Derived from: Agent_Real_Time.Destination.

Direction

The direction of active task:

In (inbound task, as non-voice tasks are always inbound).

Out (outgoing external task).

Other (outgoing or incoming internal task).

Not Applicable (if the logged-in agent is not active in the skill group).

Derived from: Agent_Real_Time.Direction.

Available in MRD

Whether or not the agent is available to accept a task in this media routing domain:

NO (Not available)

YES_ICM ( Unified CCE available in media routing domain)

YES_APP (Application available in media routing domain)

An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready, the agent is not at the agent's maximum task limit for the MRD, and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is ICM-available, then Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent.

Active

The number of tasks associated with the skill group that the agent is working on.

Derived from: Agent_Skill_Group_Real_Time.CallsInProgress

Agent Skill Target ID

The
                                             						current state of the agent.

Derived
                                             						from: Agent_Real_Time.AgentState.

Skill Target ID

This report is grouped and sorted by Skill Target ID.

Skill Target ID Derived from: Skill_Group.SkillTargetID.

### Available Fields in
                           	 the Agent Queue Real Time Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current.

Additional Available
                                 		  fields in this report are populated from fields in the Agent_Real_Time table as
                                 		  documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Note also that:

Media is derived from:
                                       				Media_Routing_Domain.EnterpriseName.

Service Name is derived
                                       				from: Service.EnterpriseName.

Enterprise Name is
                                       				derived from: Agent.EnterpriseName.

### Current Fields in the Agent Queue Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Precision Queue / Skill Group

Precision Queue or Skill Group or NotApplicable.

Precision
                                             						Queue is derived from:Precision_Queue.EnterpriseName.

The
                                             						precision route associated with the task on which the agent is currently
                                             						working. If the agent is not involved in any task in the media routing domain,
                                             						this field shows Not Applicable. Because an agent can log in to multiple
                                             						precision routes, this field is not filled until the agent is assigned a task.

Skill
                                             						Group Name is derived from: Skill_Group.EnterpriseName.

The skill
                                             						group associated with the task on which the agent is currently working. If the
                                             						agent is not involved in any task in the media routing domain, this field shows
                                             						Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             						this field is not filled until the agent is assigned a task.

Attributes 1 to 10

The attributes used in the precision queue definition. The report shows only those attributes that are used.

Derived from: Attribute.EnterpriseName

Agent

The last and first name of the agent.

Derived from: Person.LastName "," Person.FirstName.

Queued Now

The Queued Now field is a calculated field based onthe Agent_Real_Time.

The number in the field increments only if:

The ICM Script uses Queue to Agent Node.

The agent is not available to take the call.

There is no other way for the router to queue a call at an agent.

Extension

The phone extension into which the agent is logged.

Derived from: Agent_Real_Time.Extension

Agent State

The current state of the agent in this skill group.

Derived from:

Agent_Skill_Group_Real_Time.AgentState

Logged on Date Time

The time spent in the current agent state in this skill group in HH:MM:SS (hours, minutes, seconds) format.

Derived from: Agent_Real_Time.DateTimeLogin

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, getdate()).

Mobile Agent Mode

The mode by which the agent is connected (populated for CCE only):

0 = Not Mobile (Local agent; general ACD/CCE phone or non-voice task)

1 = Call By Call (Mobile agent's phone is connected for each incoming call)

2 = Nailed Connection (Mobile agent calls andlogs in once; line remains connected through multiple calls)

Derived from: Agent_Real_Time.PhoneType

Mobile Agent Phone#

For a mobile agent (an agent working remotely), the current phone number. Populated for CCE only.

Derived from:

Agent_Real_Time.RemotePhoneNumber

Reason

A code received from the peripheral that indicates the reason for the agent's last state change. If the code is not defined,
                                             this displays 0.

To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information.

Derived from: Agent_Real_Time.ReasonCode.

Supervisor Assist Requested

Whether or not the agent requested supervisor assistance: No|Yes.

Derived from:

Agent_Real_Time.RequestedSupervisorAssist

Destination

The type of outbound task on which the agent is currently working.

Derived from: Agent_Real_Time.Destination.

Direction

The direction of active task:

In (inbound task, as non-voice tasks are always inbound).

Out (outgoing external task).

Other (outgoing or incoming internal task).

Not Applicable (if the logged-in agent is not active in the skill group).

Derived from: Agent_Real_Time.Direction.

Available in MRD

Whether or not the agent is available to accept a task in this media routing domain:

NO (Not available)

YES_ICM ( Unified CCE available in media routing domain)

YES_APP (Application available in media routing domain)

An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready, the agent is not at the agent's maximum task limit for the MRD, and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is ICM-available, then Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent.

Active

The number of tasks associated with the skill group that the agent is working on.

Derived from: Agent_Skill_Group_Real_Time.CallsInProgress

Agent Skill Target ID

The
                                             						current state of the agent.

Derived
                                             						from: Agent_Real_Time.AgentState.

Skill Target ID

This report is grouped and sorted by Skill Target ID.

Skill Target ID Derived from: Skill_Group.SkillTargetID.

## Agent Real
                        	 Time

This report presents a table of selected agents showing each agent's currently active skill group, state, and call direction
                              within each Media Routing Domain into which the agent is logged. Agent Real Time provides information about current individual
                              agent activity, such as how long an agent has been on a call or whether the agent is currently handling a voice or chat interaction.

Query: This report data
                              		  is built from a Database Query.

Views: This report has one grid view, Agent Real Time.

Grouping: This report is grouped and sorted by Agent.

Value Lists: Agent,  Media Routing Domain

Database Schema Tables from which data is retrieved:

Agent

Agent_Real_Time

Agent_Skill_Group_Real_Time

Controller_Time

Media_Routing_Domain

Person

Precision_Queue

Reason_Code

Service

Skill_Group

### Available Fields in
                           	 the Agent Real Time Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. Additional
                                 		  Available fields in this report are populated from fields in the
                                 		  Agent_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Note that:

Media is derived from:
                                       				Media_Routing_Domain.EnterpriseName.

Service Name is derived
                                       				from: Service.EnterpriseName.

Enterprise Name is
                                       				derived from: Skill_Group.EnterpriseName.

### Current Fields in the Agent Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Agent

The last
                                             						and first name of the agent.

Derived
                                             						from: Person.LastName "," Person.FirstName.

Precision Queue / Skill Group

Precision Queue or Skill Group or NotApplicable.

Precision
                                             						Queue is derived from:Precision_Queue.EnterpriseName.

The
                                             						precision route associated with the task on which the agent is currently
                                             						working. If the agent is not involved in any task in the media routing domain,
                                             						this field shows Not Applicable. Because an agent can log in to multiple
                                             						precision routes, this field is not filled until the agent is assigned a task.

Skill
                                             						Group Name is derived from: Skill_Group.EnterpriseName.

The skill
                                             						group associated with the task on which the agent is currently working. If the
                                             						agent is not involved in any task in the media routing domain, this field shows
                                             						Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             						this field is not filled until the agent is assigned a task.

Media

The enterprise name of the Media Routing Domain associated with the Precision
                                             						Queue or  Skill Group Name.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

Derived from:  Attribute.EnterpriseName

AgentState

The
                                             						current state of the agent.

Derived
                                             						from: Agent_Real_Time.AgentState.

Destination

The type
                                             						of outbound task on which the agent is currently working.

Derived
                                             						from: Agent_Real_Time.Destination.

Direction

The
                                             						direction of active task:

In
                                                   							 (inbound task, as non-voice tasks are always inbound).

Out
                                                   							 (outgoing external task).

Other
                                                   							 (outgoing or incoming internal task).

Not
                                                   							 Applicable (if the logged-in agent is not active in the skill group).

Derived
                                             						from: Agent_Real_Time.Direction.

Duration

The time
                                             						spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This field is a
                                             						calculated field derived from: DATEDIFF(seconds,
                                             						Agent_Real_Time.DateTimeLastStateChange, getdate()).

Reason

The text associated with the ReasonCode numeric value, which is a code received from the peripheral, indicates the reason
                                             for the agent's last state change.

If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed.

To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information.

Derived from: Agent_Real_Time.ReasonCode.

### Available Fields in
                           	 the Agent Real Time Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. Additional
                                 		  Available fields in this report are populated from fields in the
                                 		  Agent_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Note that:

Media is derived from:
                                       				Media_Routing_Domain.EnterpriseName.

Service Name is derived
                                       				from: Service.EnterpriseName.

Enterprise Name is
                                       				derived from: Skill_Group.EnterpriseName.

### Current Fields in the Agent Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Agent

The last
                                             						and first name of the agent.

Derived
                                             						from: Person.LastName "," Person.FirstName.

Precision Queue / Skill Group

Precision Queue or Skill Group or NotApplicable.

Precision
                                             						Queue is derived from:Precision_Queue.EnterpriseName.

The
                                             						precision route associated with the task on which the agent is currently
                                             						working. If the agent is not involved in any task in the media routing domain,
                                             						this field shows Not Applicable. Because an agent can log in to multiple
                                             						precision routes, this field is not filled until the agent is assigned a task.

Skill
                                             						Group Name is derived from: Skill_Group.EnterpriseName.

The skill
                                             						group associated with the task on which the agent is currently working. If the
                                             						agent is not involved in any task in the media routing domain, this field shows
                                             						Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             						this field is not filled until the agent is assigned a task.

Media

The enterprise name of the Media Routing Domain associated with the Precision
                                             						Queue or  Skill Group Name.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

Derived from:  Attribute.EnterpriseName

AgentState

The
                                             						current state of the agent.

Derived
                                             						from: Agent_Real_Time.AgentState.

Destination

The type
                                             						of outbound task on which the agent is currently working.

Derived
                                             						from: Agent_Real_Time.Destination.

Direction

The
                                             						direction of active task:

In
                                                   							 (inbound task, as non-voice tasks are always inbound).

Out
                                                   							 (outgoing external task).

Other
                                                   							 (outgoing or incoming internal task).

Not
                                                   							 Applicable (if the logged-in agent is not active in the skill group).

Derived
                                             						from: Agent_Real_Time.Direction.

Duration

The time
                                             						spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This field is a
                                             						calculated field derived from: DATEDIFF(seconds,
                                             						Agent_Real_Time.DateTimeLastStateChange, getdate()).

Reason

The text associated with the ReasonCode numeric value, which is a code received from the peripheral, indicates the reason
                                             for the agent's last state change.

If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed.

To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information.

Derived from: Agent_Real_Time.ReasonCode.

## Agent Skill Group Real Time

The Agent Skill Group Real Time report presents
                              		  a table of agents within selected skill groups.  The table provides information about each agent's current activity, such
                              as the current state, the duration in the current state,  the Mobile agent mode, and the call direction within each Media
                              Routing Domain into which the agent
                              		  is logged.

Query: This report data
                              		  is built from a Database Query.

Views: This report has one grid view, Agent Skill Group Real Time.

Grouping: This report is grouped by Skill Group and then sorted by Agent.

Value List: Skill Group, Media Routing Domain

Database Schema Tables from which data is retrieved:

Agent

Agent_Real_Time

Agent_Skill_Group_Real_Time

Controller_Time

Media_Routing_Domain

Person

Reason_Code

Service

Skill_Group

Skill_Group_Real_Time

### Available Fields
                           	 in the Agent Skill Group Real Time Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are populated from fields in the
                                 		  Agent_Real_Time and Skill_Group_Real_Time tables as documented in the Database
                                    			 Schema Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

### Current Fields in the Agent Skill Group Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Skill Group

The skill group enterprise name for the selected skill group.

Derived from:
                                             Skill_Group.EnterpriseName

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Agent

The last name and first name of the agent.

Derived from: Person.LastName + ", " + Person.FirstName

Queued Now

The number of tasks currently queued for the skill group.

Derived from: Skill_Group_Real_Time.RouterCallsQNow

Extension

The phone extension into which the agent is logged.

Derived from: Agent_Real_Time.Extension

Agent State

The current state of the agent in this skill group.

Derived from:  Agent_Skill_Group_Real_Time.AgentState

Log On DateTime

The time spent in the current agent state in this skill group in HH:MM:SS (hours, minutes, seconds) format.

Derived from: Agent_Real_Time.DateTimeLogin

Duration

The time spent in the current agent
                                             state in HH:MM:SS (hours, minutes, seconds) format.

This is a calculated field derived
                                             from: DATEDIFF(seconds,
                                             Agent_Skill_Group_Real_Time.DateTimeLastStateChange, getdate())

Mobile Agent Mode

The mode by which the agent is connected (populated for CCE only):

0 = Not Mobile (Local agent; general ACD/CCE phone or non-voice task)

1 = Call By Call (Mobile agent's phone is connected for each incoming call)

2 = Nailed Connection (Mobile agent calls and logs in once; line remains connected through multiple calls)

Derived from: Agent_Real_Time.PhoneType

Mobile Agent Phone#

For a mobile agent (an agent working
                                             remotely), the current phone number. Populated for CCE only.

Derived from: Agent_Real_Time.RemotePhoneNumber

Reason

A code received from the peripheral that indicates the reason for the agent's last state change. If the code is not defined,
                                             the reason code displays 0.

To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information.

Derived from: Agent_Real_Time.ReasonCode

Supervisor Assist Requested

Whether or not the agent requested
                                             supervisor assistance: No|Yes.

Derived from:
                                             Agent_Real_Time.RequestedSupervisorAssist

Destination

The type of outbound task on which
                                             the agent is currently working.

Derived from: Agent_Real_Time.Destination

Direction

The direction of the call that the
                                             agent is currently working on:

NULL = None

0 = None

1 = In

2 = Out

3 = Other In

4 = Other Out/Outbound Direct Preview

5 = Outbound Reserve

6 = Outbound Preview

7 = Outbound Predictive/Progressive

Derived from: Agent_Real_Time.Direction

Avail in MRD

Whether or not the agent is
                                             available to accept a task in this media routing domain:

NO (Not available)

YES_ICM ( Unified CCE available in media routing domain)

YES_APP (Application available in media routing domain)

An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready, the agent is not at the agent's maximum task limit for the MRD, and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is ICM-available, then Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent.

Active

The number of tasks associated with
                                             the skill group that the agent is working on.

Derived from:
                                             Agent_Skill_Group_Real_Time.CallsInProgress

### Available Fields
                           	 in the Agent Skill Group Real Time Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are populated from fields in the
                                 		  Agent_Real_Time and Skill_Group_Real_Time tables as documented in the Database
                                    			 Schema Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

### Current Fields in the Agent Skill Group Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Skill Group

The skill group enterprise name for the selected skill group.

Derived from:
                                             Skill_Group.EnterpriseName

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Agent

The last name and first name of the agent.

Derived from: Person.LastName + ", " + Person.FirstName

Queued Now

The number of tasks currently queued for the skill group.

Derived from: Skill_Group_Real_Time.RouterCallsQNow

Extension

The phone extension into which the agent is logged.

Derived from: Agent_Real_Time.Extension

Agent State

The current state of the agent in this skill group.

Derived from:  Agent_Skill_Group_Real_Time.AgentState

Log On DateTime

The time spent in the current agent state in this skill group in HH:MM:SS (hours, minutes, seconds) format.

Derived from: Agent_Real_Time.DateTimeLogin

Duration

The time spent in the current agent
                                             state in HH:MM:SS (hours, minutes, seconds) format.

This is a calculated field derived
                                             from: DATEDIFF(seconds,
                                             Agent_Skill_Group_Real_Time.DateTimeLastStateChange, getdate())

Mobile Agent Mode

The mode by which the agent is connected (populated for CCE only):

0 = Not Mobile (Local agent; general ACD/CCE phone or non-voice task)

1 = Call By Call (Mobile agent's phone is connected for each incoming call)

2 = Nailed Connection (Mobile agent calls and logs in once; line remains connected through multiple calls)

Derived from: Agent_Real_Time.PhoneType

Mobile Agent Phone#

For a mobile agent (an agent working
                                             remotely), the current phone number. Populated for CCE only.

Derived from: Agent_Real_Time.RemotePhoneNumber

Reason

A code received from the peripheral that indicates the reason for the agent's last state change. If the code is not defined,
                                             the reason code displays 0.

To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information.

Derived from: Agent_Real_Time.ReasonCode

Supervisor Assist Requested

Whether or not the agent requested
                                             supervisor assistance: No|Yes.

Derived from:
                                             Agent_Real_Time.RequestedSupervisorAssist

Destination

The type of outbound task on which
                                             the agent is currently working.

Derived from: Agent_Real_Time.Destination

Direction

The direction of the call that the
                                             agent is currently working on:

NULL = None

0 = None

1 = In

2 = Out

3 = Other In

4 = Other Out/Outbound Direct Preview

5 = Outbound Reserve

6 = Outbound Preview

7 = Outbound Predictive/Progressive

Derived from: Agent_Real_Time.Direction

Avail in MRD

Whether or not the agent is
                                             available to accept a task in this media routing domain:

NO (Not available)

YES_ICM ( Unified CCE available in media routing domain)

YES_APP (Application available in media routing domain)

An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready, the agent is not at the agent's maximum task limit for the MRD, and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is ICM-available, then Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent.

Active

The number of tasks associated with
                                             the skill group that the agent is working on.

Derived from:
                                             Agent_Skill_Group_Real_Time.CallsInProgress

## Agent State Real
                        	 Time Graph

This report is a pie
                              		  chart showing the current total count of agents in different agent states.

Views: This report has one chart view,  Agent State Real Time Graph.

Query: This report data
                              		  is built from an Anonymous Block.

Value List: Agent

Database Schema Tables from
                                 			 which data is retrieved: Agent_Real_Time.AgentState

The following
                              		  data is represented in the Agent State Real Time pie chart graph.

Field

Description

Not Ready

The agent is
                                          					 not available to be assigned a task.

Ready

The agent
                                          					 has put himself in the Ready state using his agent desktop tool.

Active

The agent is
                                          					 working on a task or a call.

Wrap Up

The agent is
                                          					 performing wrap-up work for a call.

Reserved

The agent has been
                                          					 offered a call or task.

For voice
                                          					 calls, agents are Reserved when their phones are ringing.

Interrupted

The agent receives a non-interrupted call or task while handling an interrupted task.

Unknown

The agent
                                          					 state is unknown.

Hold

For agents
                                          					 handling Outbound Option calls, the Hold state indicates that the agent is  reserved for a call because the Outbound
                                          Dialer put the agent on hold
                                          					 while connecting the call.

## Agent Team Real
                        	 Time

This report shows
                              		  the current status of the selected Agent Teams and the current agent states of
                              		  each agent within the selected Agent Teams. Agent Team Real Time provides
                              		  similar information to the Agent State Real Time but presented and grouped by
                              		  teams.

Views: This report has one grid view, Agent Team Real Time.

Query: This report data
                              		  is built from a Database Query.

Grouping: This report is grouped and sorted by Agent Team and then by Supervisor.

Value List: Agent Team

Database Schema Tables from which data is retrieved:

Agent

Agent_Real_Time

Agent_Skill_Group_Real_Time

Agent_Team

Agent_Team_Member

Media_Routing_Domain

Person

Precision Queue

Service

Skill_Group

### Available Fields in
                           	 the Agent Team Real Time Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. Additional
                                 		  Available fields in this report are from the Agent_Real_Time table as
                                 		  documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Other tables used
                                 		  are:

Agent_Team

The Agent
                                             					 Team field is derived from: Agent_Team.AgentTeamID.

The
                                             					 PriSupervisor Skill Target ID field is derived from:
                                             					 Agent_Team.PriSupervisorSkillTargetID.

Person

FirstName is
                                             					 derived from: Person.FirstName.

LastName is
                                             					 derived from: Person.LastName.

Media_Routing_Domain

The Media
                                             					 field is derived from: Media_Routing_Domain.EnterpriseName.

Service

Service Name
                                             					 is derived from: Service.EnterpriseName.

### Current Fields in
                           	 the Agent Team Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column (Field)

Description

Agent Team

The Enterprise Name of the Agent Team.

Derived from: Agent_Team.EnterpriseName.

Supervisor

The Agent Team's primary supervisor.

Derived from: Person.LastName ", " Person.FirstName.

Agent

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

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

Derived from: Attribute.EnterpriseName

State

The current state of the agent.

Derived from: Agent_Real_Time.AgentState.

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, Select NowTime From
                                             Controller_Time)

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

Report Summary: There is a summary row for Agent Team, a summary row for each Supervisor and a report summary for all data. For more information,
                                 see Report Summary Rows .

### Available Fields in
                           	 the Agent Team Real Time Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. Additional
                                 		  Available fields in this report are from the Agent_Real_Time table as
                                 		  documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Other tables used
                                 		  are:

Agent_Team

The Agent
                                             					 Team field is derived from: Agent_Team.AgentTeamID.

The
                                             					 PriSupervisor Skill Target ID field is derived from:
                                             					 Agent_Team.PriSupervisorSkillTargetID.

Person

FirstName is
                                             					 derived from: Person.FirstName.

LastName is
                                             					 derived from: Person.LastName.

Media_Routing_Domain

The Media
                                             					 field is derived from: Media_Routing_Domain.EnterpriseName.

Service

Service Name
                                             					 is derived from: Service.EnterpriseName.

### Current Fields in
                           	 the Agent Team Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column (Field)

Description

Agent Team

The Enterprise Name of the Agent Team.

Derived from: Agent_Team.EnterpriseName.

Supervisor

The Agent Team's primary supervisor.

Derived from: Person.LastName ", " Person.FirstName.

Agent

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

Attributes

The attributes used in the precision queue definition. The report shows only those attributes that are used.

Derived from: Attribute.EnterpriseName

State

The current state of the agent.

Derived from: Agent_Real_Time.AgentState.

Duration

The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format.

This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, Select NowTime From
                                             Controller_Time)

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

Report Summary: There is a summary row for Agent Team, a summary row for each Supervisor and a report summary for all data. For more information,
                                 see Report Summary Rows .

## Agent Team State
                        	 Counts Real Time

Agent Team State
                              		  Counts provides the distribution of agent states per team. Use this report to
                              		  identify how many agents are available in a current team.

Views: This report has one grid view, Agent Team State Count Real Time.

Query: This report data
                              		  is built from a Database Query.

Grouping: There is no
                              		  grouping for this report. It is sorted by Agent Team.

Value List: Agent Team

Database Schema Tables from which data is retrieved:

Agent

Agent_Real_Time

Agent_Team

Agent_Team_Member

Media_Routing_Domain

Person

### Available Fields in
                           	 the Agent Team State Counts Real Time Report

Available fields for
                                 		  this report include all fields that appear by default as Current. In the
                                 		  Current panel, they appear by their display names (for example, Hold ). In the Available panel, they appear by their
                                 		  database names (for example, hold_state ).

These fields are
                                 		  from the Person, Agent_Team, Agent_Team_Member, and Agent_Real_Time tables.

Agent Team ID Derived
                                       				from:  Agent_Team_Member.AgentTeamID.

Media Derived from:
                                       				 Media_Routing_Domain.EnterpriseName.

Eligible for Task Derived
                                       				from: Count of agents where Agent_Real_Time.AvailableInMRD is 0.

The number of
                                       				agents who are eligible to receive tasks in the specified Media Routing Domain.

An agent can be
                                       				in the Not Active state (available) and not be Eligible For Task in a Media
                                       				Routing Domain.

This can occur
                                       				under the following circumstances:

In Media
                                             					 Routing Domains other than Voice: if the agent is currently working on a Voice
                                             					 task.

In the
                                             					 Voice media routing domain: if the agent is currently working on a multimedia
                                             					 task other than an Email task.

### Current Fields in
                           	 the Agent Team State Counts Real Time Report

Current fields
                                 		  are those fields that appear by default in a report generated from the stock
                                 		  template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Columns
                                             						(Fields)

Description

Agent Team

The
                                             						enterprise name of the Agent Team.

Derived
                                             						from: Agent_Team.EnterpriseName.

Supervisor

The team's
                                             						primary supervisor.

Derived
                                             						from: Person.LastName + ' ' + Person.FirstName.

Total On
                                             						Team

The count
                                             						of agents configured for the individual team.

Derived
                                             						from:  Count(Agent_Team_Member.SkillTargetID).

Agent
                                             						Logged On

The number
                                             						of agents currently logged in.

Derived
                                             						from: Count of agents with Agent_Real_Time.AgentState not equal to 0.

Active In

The number
                                             						of agents currently working on incoming tasks.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 1.

Active Out

The number
                                             						of agents currently working on outbound tasks.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 2.

Active
                                             						Other

The number
                                             						of agents currently working on internal (neither inbound nor outbound) tasks.
                                             						Examples of other tasks include agent-to-agent transfers and supervisor tasks.

Derived
                                             						from: count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 3.

Hold

The number
                                             						of agents that have all active tasks on hold and have paused tasks. The agent
                                             						is not in the Hold state with one task on hold and talking on another task (for
                                             						example, a consultative call). The agent must have all active tasks on hold.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 10 or 12.

Not Active

The number
                                             						of agents in the Not Active state, the state where the agent is ready to accept
                                             						tasks, but is not currently involved in task work.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 3 or 14.

Wrap Up

The number
                                             						of agents in the Work Not Ready state and Work Ready state. The Work Not Ready
                                             						state is a state in which an agent is involved in after task work and is
                                             						assumed not to be ready to accept incoming tasks when done. The Work Ready
                                             						state is a state in which an agent is involved in after a task work and is
                                             						assumed to be ready to accept incoming tasks when done.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 5 or 6.

Not Ready

The number
                                             						of agents in the Not Ready state, a state in which agents are logged in but are
                                             						neither involved in any task handling activity nor available to handle a task.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 2.

Reserved

The number
                                             						of agents currently in the Reserved state, a state in which an agent is
                                             						selected to receive a task. An agent is in the Reserved state until the task is
                                             						answered.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 8.

Report Summary: There is
                                 		  a summary row for the total report. For more information, see Report Summary Rows .

### Available Fields in
                           	 the Agent Team State Counts Real Time Report

Available fields for
                                 		  this report include all fields that appear by default as Current. In the
                                 		  Current panel, they appear by their display names (for example, Hold ). In the Available panel, they appear by their
                                 		  database names (for example, hold_state ).

These fields are
                                 		  from the Person, Agent_Team, Agent_Team_Member, and Agent_Real_Time tables.

Agent Team ID Derived
                                       				from:  Agent_Team_Member.AgentTeamID.

Media Derived from:
                                       				 Media_Routing_Domain.EnterpriseName.

Eligible for Task Derived
                                       				from: Count of agents where Agent_Real_Time.AvailableInMRD is 0.

The number of
                                       				agents who are eligible to receive tasks in the specified Media Routing Domain.

An agent can be
                                       				in the Not Active state (available) and not be Eligible For Task in a Media
                                       				Routing Domain.

This can occur
                                       				under the following circumstances:

In Media
                                             					 Routing Domains other than Voice: if the agent is currently working on a Voice
                                             					 task.

In the
                                             					 Voice media routing domain: if the agent is currently working on a multimedia
                                             					 task other than an Email task.

### Current Fields in
                           	 the Agent Team State Counts Real Time Report

Current fields
                                 		  are those fields that appear by default in a report generated from the stock
                                 		  template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Columns
                                             						(Fields)

Description

Agent Team

The
                                             						enterprise name of the Agent Team.

Derived
                                             						from: Agent_Team.EnterpriseName.

Supervisor

The team's
                                             						primary supervisor.

Derived
                                             						from: Person.LastName + ' ' + Person.FirstName.

Total On
                                             						Team

The count
                                             						of agents configured for the individual team.

Derived
                                             						from:  Count(Agent_Team_Member.SkillTargetID).

Agent
                                             						Logged On

The number
                                             						of agents currently logged in.

Derived
                                             						from: Count of agents with Agent_Real_Time.AgentState not equal to 0.

Active In

The number
                                             						of agents currently working on incoming tasks.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 1.

Active Out

The number
                                             						of agents currently working on outbound tasks.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 2.

Active
                                             						Other

The number
                                             						of agents currently working on internal (neither inbound nor outbound) tasks.
                                             						Examples of other tasks include agent-to-agent transfers and supervisor tasks.

Derived
                                             						from: count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 3.

Hold

The number
                                             						of agents that have all active tasks on hold and have paused tasks. The agent
                                             						is not in the Hold state with one task on hold and talking on another task (for
                                             						example, a consultative call). The agent must have all active tasks on hold.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 10 or 12.

Not Active

The number
                                             						of agents in the Not Active state, the state where the agent is ready to accept
                                             						tasks, but is not currently involved in task work.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 3 or 14.

Wrap Up

The number
                                             						of agents in the Work Not Ready state and Work Ready state. The Work Not Ready
                                             						state is a state in which an agent is involved in after task work and is
                                             						assumed not to be ready to accept incoming tasks when done. The Work Ready
                                             						state is a state in which an agent is involved in after a task work and is
                                             						assumed to be ready to accept incoming tasks when done.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 5 or 6.

Not Ready

The number
                                             						of agents in the Not Ready state, a state in which agents are logged in but are
                                             						neither involved in any task handling activity nor available to handle a task.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 2.

Reserved

The number
                                             						of agents currently in the Reserved state, a state in which an agent is
                                             						selected to receive a task. An agent is in the Reserved state until the task is
                                             						answered.

Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 8.

Report Summary: There is
                                 		  a summary row for the total report. For more information, see Report Summary Rows .

## Call Type Real
                        	 Time

Reports generated
                              		  from the Call Type Real Time template show the current status of call types.
                              		  The report provides an overall view, by Call Type, of current activity such as
                              		  Calls in Queue, longest call in queue, and last 5-minute statistics.

Query: This report data is built from a Database Query.

Views: This report has a default grid view (Call Type Real Time) and a chart view (Call Type Queue Now).

Value List: Call Type

Database Schema Tables from
                                 			 which data is retrieved :

Call_Type

Call_Type_Real_Time

### Available Fields in
                           	 the Call Type Real Time Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. Additional
                                 		  Available fields in this report are populated from the Call_Type_Real_Time
                                 		  table as documented in the Database Schema
                                    			 Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in
                           	 the Call Type Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report grid view generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Call Type Name

The
                                             						enterprise name for the call type.

Derived
                                             						from: Call_Type.EnterpriseName.

Avg Speed of Answer 5

Average
                                             						Speed of Answer during the rolling five-minute interval. The total Answer Time
                                             						for all tasks of the call type divided by the number of tasks of this type
                                             						answered during the current five-minute interval.

This field
                                             						is a calculated field, derived from: (Call_Type_Real_Time.AnswerWaitTimeTo5 /
                                             						Call_Type_Real_Time.CallsAnsweredTo5).

VRU not Queued Now

The number
                                             						of tasks in Run VRUScript or Wait state. This represents the number of tasks at
                                             						VRU prompting or self service.

This field
                                             						is a calculated field, derived from: Call_Type_Real_Time.CallsAtVRUNow -
                                             						Call_Type_Real_Time.RouterCallsQNow.

Queued Now

The number
                                             						of tasks currently in the queue.

Derived
                                             						from: Call_Type_Real_Time.RouterCallsQNow.

CCE Agent
                                             						Now

The number of tasks that have been routed to the Unified CCE agents but are not yet ended. This column is incremented when the call is answered and decremented when the call ends, after
                                             wrap up is complete, if applicable.

Derived
                                             						from: Call_Type_Real_Time.CallsAtAgentNow.

Longest
                                             						Queued

The time
                                             						spent in queue for the longest currently queued task, measured in HH:MM:SS
                                             						(hours, minutes, seconds) format.

This field
                                             						is a calculated field, determined by subtracting the time the task entered the
                                             						queue (Derived from: Call_Type_Real_Time.RouterLongestCallQ) from the current
                                             						time.

Service
                                             						Level

The Unified ICM/Unified CCE service level for the rolling five-minute interval.

Derived
                                             						from: Call_Type_Interval.ServiceLevelTo5.

Handled5

The number
                                             						of calls of this call type handled for the call type ending during the rolling
                                             						five-minute interval.

Derived
                                             						from: Call_Type_Real_Time.CallsHandledTo5.

Aband5

The number
                                             						of tasks abandoned at the IVR during the rolling five-minute interval, while
                                             						offered to the agent and on route to the agent.

Derived
                                             						from: Call_Type_Real_Time.TotalCallsAbandTo5.

Abandoned Within Service Level

The
                                             						number of tasks abandoned before the service level timer expired during the
                                             						rolling five-minute interval.

Derived
                                             						from: Call_Type_Real_Time.ServiceLevelAbandTo5.

Average Abandon

The
                                             						average time of abandoned calls for this call type during the rolling
                                             						five-minute interval, measured in HH:MM:SS (hours, minutes, seconds) format.

This field
                                             						is a calculated field, derived from: Call_Type_Real_Time.CallDelayAbandTimeTo5
                                             						/ Call_Type_Real_Time.TotalCallsAbandTo5.

Report Summary: There is
                                 		  a summary for all data in the report.

### Available Fields in
                           	 the Call Type Real Time Grid View

Available fields for
                                 		  this report include the fields that appear by default as Current. Additional
                                 		  Available fields in this report are populated from the Call_Type_Real_Time
                                 		  table as documented in the Database Schema
                                    			 Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in
                           	 the Call Type Real Time Grid View

Current fields are those
                                 		  fields that appear by default in a report grid view generated from the stock
                                 		  template.

Current fields are
                                 		  listed here in the order (left to right) in which they appear by default in the
                                 		  stock template.

Column
                                             						(Field)

Description

Call Type Name

The
                                             						enterprise name for the call type.

Derived
                                             						from: Call_Type.EnterpriseName.

Avg Speed of Answer 5

Average
                                             						Speed of Answer during the rolling five-minute interval. The total Answer Time
                                             						for all tasks of the call type divided by the number of tasks of this type
                                             						answered during the current five-minute interval.

This field
                                             						is a calculated field, derived from: (Call_Type_Real_Time.AnswerWaitTimeTo5 /
                                             						Call_Type_Real_Time.CallsAnsweredTo5).

VRU not Queued Now

The number
                                             						of tasks in Run VRUScript or Wait state. This represents the number of tasks at
                                             						VRU prompting or self service.

This field
                                             						is a calculated field, derived from: Call_Type_Real_Time.CallsAtVRUNow -
                                             						Call_Type_Real_Time.RouterCallsQNow.

Queued Now

The number
                                             						of tasks currently in the queue.

Derived
                                             						from: Call_Type_Real_Time.RouterCallsQNow.

CCE Agent
                                             						Now

The number of tasks that have been routed to the Unified CCE agents but are not yet ended. This column is incremented when the call is answered and decremented when the call ends, after
                                             wrap up is complete, if applicable.

Derived
                                             						from: Call_Type_Real_Time.CallsAtAgentNow.

Longest
                                             						Queued

The time
                                             						spent in queue for the longest currently queued task, measured in HH:MM:SS
                                             						(hours, minutes, seconds) format.

This field
                                             						is a calculated field, determined by subtracting the time the task entered the
                                             						queue (Derived from: Call_Type_Real_Time.RouterLongestCallQ) from the current
                                             						time.

Service
                                             						Level

The Unified ICM/Unified CCE service level for the rolling five-minute interval.

Derived
                                             						from: Call_Type_Interval.ServiceLevelTo5.

Handled5

The number
                                             						of calls of this call type handled for the call type ending during the rolling
                                             						five-minute interval.

Derived
                                             						from: Call_Type_Real_Time.CallsHandledTo5.

Aband5

The number
                                             						of tasks abandoned at the IVR during the rolling five-minute interval, while
                                             						offered to the agent and on route to the agent.

Derived
                                             						from: Call_Type_Real_Time.TotalCallsAbandTo5.

Abandoned Within Service Level

The
                                             						number of tasks abandoned before the service level timer expired during the
                                             						rolling five-minute interval.

Derived
                                             						from: Call_Type_Real_Time.ServiceLevelAbandTo5.

Average Abandon

The
                                             						average time of abandoned calls for this call type during the rolling
                                             						five-minute interval, measured in HH:MM:SS (hours, minutes, seconds) format.

This field
                                             						is a calculated field, derived from: Call_Type_Real_Time.CallDelayAbandTimeTo5
                                             						/ Call_Type_Real_Time.TotalCallsAbandTo5.

Report Summary: There is
                                 		  a summary for all data in the report.

## Enterprise Skill
                        	 Group Real Time

The Enterprise
                              		  Skill Group Real Time report shows the current status of the selected
                              		  enterprise skill groups, providing real time information about calls in queue
                              		  for Enterprise Skill Groups. Enterprise Skill Groups provide the ability to
                              		  group skill groups within a peripheral or in different peripherals.

If a call is queued
                              		  to an Enterprise skill group, then the call is queued at each peripheral
                              		  skill group that belongs to the enterprise skill group. Therefore one call
                              		  queued to an enterprise skill group composed of five peripheral skill groups
                              		  shows up as five calls.

For more information about Enterprise Skill groups, see Reporting Concepts for
                                 				  Cisco Unified ICM/CCE at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

Query: This report data is built from a Database Query.

Views: This report has one grid view, Enterprise Skill Group Real Time.

Value Lists: Enterprise
                              		  Skill Group, Media Routing Domain

Database Schema Tables from which data is retrieved:

Enterprise_Skill_Group

Enterprise_Skill_Group_Member

Media_Routing_Domain

Skill_Group

Skill_Group_Real_Time

### Available Fields in the Enterprise Skill Group Real Time Grid View

Available
                                 fields for this report include the fields that appear by default as Current.
                                 Additional Available fields in this report are derived from the
                                 Skill_Group_Real_Time table as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

### Current Fields in the Enterprise Skill Group Real Time Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Enterprise Skill Group

The
                                             						enterprise skill group's enterprise name and ID.

Derived
                                             						from: Enterprise_Skill_Group.EnterpriseName
                                             						(Enterprise_Skill_Group.EnterpriseSkillGroupID).

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Queued Now

The
                                             						number of calls currently queued to the skill group at the CallRouter and at
                                             						the local ACD queue.

This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Queued Now (ICM) is Available by default.

Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow.

Longest Queued

The
                                             						longest queued task on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format.

This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Longest Task Q (ICM) is Available by default.

Derived
                                             						from: Skill_Group_Real_Time.RouterLongestCallInQ.

ASA5

The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the skill group during the rolling five minute interval.

Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5.

Handled

The
                                             						number of tasks that were handled during the rolling five minute interval.

Derived
                                             						from: Skill_Group_Real_Time.CallsHandledTo5.

Avg Handle Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it has taken during the
                                             						rolling five minute interval to handle a task.

Derived
                                             						from: Skill_Group_Real_Time.HandleCallsTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5.

Log On

The
                                             						number of agents that are currently logged in to the skill group. This count is
                                             						updated each time an agent logs in and each time an agent logs out.

Derived
                                             						from: Skill_Group_Real_Time.LoggedOn.

Not
                                             						Ready

The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged in but are neither involved in any call
                                             						handling activity nor available to handle a call.

Derived
                                             						from: Skill_Group_Real_Time.NotReady.

Not
                                             						Active

The
                                             						number of agents in the skill group who are currently not working on a task
                                             						associated with the skill group.

Derived
                                             						from: Skill_Group_Real_Time.Avail.

Active
                                             						In

The
                                             						number of agents in the skill group currently working on inbound tasks.

Derived
                                             						from: Skill_Group_Real_Time.TalkingIn.

Active
                                             						Out

The
                                             						number of agents in the skill group currently talking on outbound calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingOut.

Active
                                             						Other

The
                                             						number of agents in the skill group currently talking on internal (neither
                                             						inbound nor outbound) calls.

Examples
                                             						of other calls include agent-to-agent transfers and supervisor calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingOther.

Active
                                             						Auto Out

The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingAutoOut.

Active
                                             						Preview

The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingPreview.

Active
                                             						Reservation

The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingReserve.

Avg Active Time

The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval.

Derived
                                             						from: (Skill_Group_Real_Time.HandledCallsTalkTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5).

Wrap Up

The
                                             						number of agents currently in wrap-up state for this skill group. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state.

Derived
                                             						from: Skill_Group_Real_Time.WorkReady + Skill_Group_Real_Time.WorkNotReady.

Hold

The
                                             						number of agents that have all active calls on hold or whose state to the skill
                                             						group is Paused. The agent is not in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold.

Derived
                                             						from: Skill_Group_Real_Time.Hold.

Reserved

The number
                                             						of agents for the skill group currently in the Reserved state.

Derived
                                             						from: Skill_Group_Real_Time.ReservedAgents.

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state.

Busy
                                             						Other is a state in which the agent is handling calls assigned to other skill
                                             						groups during the interval.

For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged in to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state.

Derived
                                             						from: Skill_Group_Real_Time.BusyOther.

%
                                             						Utilization

The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready.

Derived
                                             						from: Skill_Group_Real_Time.PercentUtilizationTo5.

Report Summary: There is a report summary for all data.

### Available Fields in the Enterprise Skill Group Real Time Grid View

Available
                                 fields for this report include the fields that appear by default as Current.
                                 Additional Available fields in this report are derived from the
                                 Skill_Group_Real_Time table as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

### Current Fields in the Enterprise Skill Group Real Time Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Enterprise Skill Group

The
                                             						enterprise skill group's enterprise name and ID.

Derived
                                             						from: Enterprise_Skill_Group.EnterpriseName
                                             						(Enterprise_Skill_Group.EnterpriseSkillGroupID).

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Queued Now

The
                                             						number of calls currently queued to the skill group at the CallRouter and at
                                             						the local ACD queue.

This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Queued Now (ICM) is Available by default.

Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow.

Longest Queued

The
                                             						longest queued task on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format.

This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Longest Task Q (ICM) is Available by default.

Derived
                                             						from: Skill_Group_Real_Time.RouterLongestCallInQ.

ASA5

The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the skill group during the rolling five minute interval.

Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5.

Handled

The
                                             						number of tasks that were handled during the rolling five minute interval.

Derived
                                             						from: Skill_Group_Real_Time.CallsHandledTo5.

Avg Handle Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it has taken during the
                                             						rolling five minute interval to handle a task.

Derived
                                             						from: Skill_Group_Real_Time.HandleCallsTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5.

Log On

The
                                             						number of agents that are currently logged in to the skill group. This count is
                                             						updated each time an agent logs in and each time an agent logs out.

Derived
                                             						from: Skill_Group_Real_Time.LoggedOn.

Not
                                             						Ready

The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged in but are neither involved in any call
                                             						handling activity nor available to handle a call.

Derived
                                             						from: Skill_Group_Real_Time.NotReady.

Not
                                             						Active

The
                                             						number of agents in the skill group who are currently not working on a task
                                             						associated with the skill group.

Derived
                                             						from: Skill_Group_Real_Time.Avail.

Active
                                             						In

The
                                             						number of agents in the skill group currently working on inbound tasks.

Derived
                                             						from: Skill_Group_Real_Time.TalkingIn.

Active
                                             						Out

The
                                             						number of agents in the skill group currently talking on outbound calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingOut.

Active
                                             						Other

The
                                             						number of agents in the skill group currently talking on internal (neither
                                             						inbound nor outbound) calls.

Examples
                                             						of other calls include agent-to-agent transfers and supervisor calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingOther.

Active
                                             						Auto Out

The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingAutoOut.

Active
                                             						Preview

The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingPreview.

Active
                                             						Reservation

The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingReserve.

Avg Active Time

The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval.

Derived
                                             						from: (Skill_Group_Real_Time.HandledCallsTalkTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5).

Wrap Up

The
                                             						number of agents currently in wrap-up state for this skill group. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state.

Derived
                                             						from: Skill_Group_Real_Time.WorkReady + Skill_Group_Real_Time.WorkNotReady.

Hold

The
                                             						number of agents that have all active calls on hold or whose state to the skill
                                             						group is Paused. The agent is not in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold.

Derived
                                             						from: Skill_Group_Real_Time.Hold.

Reserved

The number
                                             						of agents for the skill group currently in the Reserved state.

Derived
                                             						from: Skill_Group_Real_Time.ReservedAgents.

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state.

Busy
                                             						Other is a state in which the agent is handling calls assigned to other skill
                                             						groups during the interval.

For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged in to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state.

Derived
                                             						from: Skill_Group_Real_Time.BusyOther.

%
                                             						Utilization

The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready.

Derived
                                             						from: Skill_Group_Real_Time.PercentUtilizationTo5.

Report Summary: There is a report summary for all data.

## Peripheral Service
                        	 Real Time All Fields

With Unified CCE , the Peripheral Service Real Time report provides current information, such as calls in queue per service.

For more information about services, see Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html . For information on mapping TDM entities, such as VDNs in Avaya, see the relevant ACD supplement at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

Peripheral Service
                              		  reports are not applicable to Contact Center Enterprise environments.

Query: This report data is built from a Database Query.

Views: This report has one grid view, Peripheral Service Real Time All Fields.

Value List: Service

Database Schema Tables from which data is retrieved:

Service

Service_Real_Time

### Available Fields in the Peripheral Service Real Time All Fields Grid View

Available fields for
                                 		  this report grid include the fields that appear by default as Current.
                                 		  Available fields in this report are populated from the Service_Real_Time table
                                 		  as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

The exception is the
                                 		  Service field, which is derived from Service.EnterpriseName.

### Current Fields in the Peripheral Service Real Time All Fields Grid View

Current fields
                                 		  are those fields that appear by default in a report grid generated from the
                                 		  stock template.

Column
                                             						(Field)

Description

Service
                                             						Name

The
                                             						enterprise name of the peripheral service.

Derived
                                             						from: Service.EnterpriseName.

In
                                             						Progress

The number of
                                             						inbound and outbound calls currently that were previously offered (for example,
                                             						calls being played, an announcement, queued calls, or connected calls) and are
                                             						currently being handled for the service.

Derived
                                             						from: Service_Real_Time.CallsInProgress.

Queued Now

The tasks
                                             						in queue associated with the service now at the peripheral.

Derived
                                             						from: Service_Real_Time.CallsQNow.

Abandoned in Queue 5

The number of tasks associated with the service that were abandoned while
                                             						in queue or ringing during the rolling five-minute interval.

An abandoned task is one in which the caller ended the call before being connected with an agent. If the caller ends the call
                                             almost immediately, you might not want to count that as an abandoned task. When configuring each peripheral, you can specify
                                             the minimum length of an abandoned task.

Derived
                                             						from: Service_Real_Time.CallsAbandQTo5.

Average Delay in Queue Aban5

The
                                             						average delay time of tasks associated with the service that were abandoned in
                                             						the service queue during the rolling five-minute interval. This value is
                                             						calculated as follows:DelayQAbandTimeTo5 / CallsAbandQTo5.

Derived
                                             						from: Service_Real_Time.AvgDelayQAbandTo5.

Average Speed of Answer to 5

The
                                             						average answer wait time for tasks associated with the service during the
                                             						rolling five-minute interval: AnswerWaitTimeTo5 / CallsOfferedTo5.

Answer
                                             						wait time is the elapsed time from when the task is offered at the peripheral
                                             						to when it is answered. This includes all DelayTime, LocalQTime, and RingTime
                                             						associated with the task.

Derived
                                             						from: Service_Real_Time.AvgSpeedAnswerTo5.

Average Handle Time to 5

The
                                             						average handle time in HH:MM:SS (hours, minutes, seconds) for tasks associated
                                             						with the service during the rolling five-minute interval. The value is
                                             						calculated as follows: HandleTimeTo5 / CallsHandledTo5.

Derived
                                             						from: Service_Real_Time.AvgHandleTimeTo5.

Longest Available Agent

The time
                                             						that the longest available agent associated with the service became available.

Derived
                                             						from: Service_Real_Time.LongestAvailAgent.

Longest Task in Queue

The time
                                             						that the longest call in the queue for the service was put there.

Derived
                                             						from: Service_Real_Time.LongestCallQ.

Flow In 5

The number
                                             						of calls the peripheral overflowed into this service during the rolling
                                             						five-minute interval.

Derived
                                             						from: Service_Real_Time.OverflowInTo5.

Flow Out 5

The number
                                             						of calls overflowed out of this service during the rolling five-minute
                                             						interval.

Derived
                                             						from: Service_Real_Time.OverflowOutTo5.

Service Level to 5

The
                                             						Enterprise service level for the service during the rolling five-minute
                                             						interval.

Derived
                                             						from: Service_Real_Time.ServiceLevelTo5.

Service Level to 5 Aban

The number
                                             						of calls to the service abandoned within the service level threshold during the
                                             						rolling five-minute interval.

Derived
                                             						from: Service_Real_Time.ServiceLevelAbandTo5.

Service Level to 5 Tasks

The number of calls to the service answered within the Unified ICM service level during the rolling five-minute interval.

Derived
                                             						from: Service_Real_Time.ServiceLevelCallsTo5.

Report Summary: The report has a total summary row for all fields. For
                                 		  more information, see Report Summary Rows .

### Available Fields in the Peripheral Service Real Time All Fields Grid View

Available fields for
                                 		  this report grid include the fields that appear by default as Current.
                                 		  Available fields in this report are populated from the Service_Real_Time table
                                 		  as documented in the Database Schema Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

The exception is the
                                 		  Service field, which is derived from Service.EnterpriseName.

### Current Fields in the Peripheral Service Real Time All Fields Grid View

Current fields
                                 		  are those fields that appear by default in a report grid generated from the
                                 		  stock template.

Column
                                             						(Field)

Description

Service
                                             						Name

The
                                             						enterprise name of the peripheral service.

Derived
                                             						from: Service.EnterpriseName.

In
                                             						Progress

The number of
                                             						inbound and outbound calls currently that were previously offered (for example,
                                             						calls being played, an announcement, queued calls, or connected calls) and are
                                             						currently being handled for the service.

Derived
                                             						from: Service_Real_Time.CallsInProgress.

Queued Now

The tasks
                                             						in queue associated with the service now at the peripheral.

Derived
                                             						from: Service_Real_Time.CallsQNow.

Abandoned in Queue 5

The number of tasks associated with the service that were abandoned while
                                             						in queue or ringing during the rolling five-minute interval.

An abandoned task is one in which the caller ended the call before being connected with an agent. If the caller ends the call
                                             almost immediately, you might not want to count that as an abandoned task. When configuring each peripheral, you can specify
                                             the minimum length of an abandoned task.

Derived
                                             						from: Service_Real_Time.CallsAbandQTo5.

Average Delay in Queue Aban5

The
                                             						average delay time of tasks associated with the service that were abandoned in
                                             						the service queue during the rolling five-minute interval. This value is
                                             						calculated as follows:DelayQAbandTimeTo5 / CallsAbandQTo5.

Derived
                                             						from: Service_Real_Time.AvgDelayQAbandTo5.

Average Speed of Answer to 5

The
                                             						average answer wait time for tasks associated with the service during the
                                             						rolling five-minute interval: AnswerWaitTimeTo5 / CallsOfferedTo5.

Answer
                                             						wait time is the elapsed time from when the task is offered at the peripheral
                                             						to when it is answered. This includes all DelayTime, LocalQTime, and RingTime
                                             						associated with the task.

Derived
                                             						from: Service_Real_Time.AvgSpeedAnswerTo5.

Average Handle Time to 5

The
                                             						average handle time in HH:MM:SS (hours, minutes, seconds) for tasks associated
                                             						with the service during the rolling five-minute interval. The value is
                                             						calculated as follows: HandleTimeTo5 / CallsHandledTo5.

Derived
                                             						from: Service_Real_Time.AvgHandleTimeTo5.

Longest Available Agent

The time
                                             						that the longest available agent associated with the service became available.

Derived
                                             						from: Service_Real_Time.LongestAvailAgent.

Longest Task in Queue

The time
                                             						that the longest call in the queue for the service was put there.

Derived
                                             						from: Service_Real_Time.LongestCallQ.

Flow In 5

The number
                                             						of calls the peripheral overflowed into this service during the rolling
                                             						five-minute interval.

Derived
                                             						from: Service_Real_Time.OverflowInTo5.

Flow Out 5

The number
                                             						of calls overflowed out of this service during the rolling five-minute
                                             						interval.

Derived
                                             						from: Service_Real_Time.OverflowOutTo5.

Service Level to 5

The
                                             						Enterprise service level for the service during the rolling five-minute
                                             						interval.

Derived
                                             						from: Service_Real_Time.ServiceLevelTo5.

Service Level to 5 Aban

The number
                                             						of calls to the service abandoned within the service level threshold during the
                                             						rolling five-minute interval.

Derived
                                             						from: Service_Real_Time.ServiceLevelAbandTo5.

Service Level to 5 Tasks

The number of calls to the service answered within the Unified ICM service level during the rolling five-minute interval.

Derived
                                             						from: Service_Real_Time.ServiceLevelCallsTo5.

Report Summary: The report has a total summary row for all fields. For
                                 		  more information, see Report Summary Rows .

## Peripheral Skill
                        	 Group Real Time All Fields

Peripheral Skill
                              		  Group reports show real time statistics per skill group such as calls in queue
                              		  and longest delay. Use this report for skill group activity.

If there are
                                          			 primary or secondary skill groups defined for the base skill group, then the
                                          			 base skill group is not shown.

Query: This report data
                              		  is built from a Database Query.

Views: This report has one grid view, Peripheral Skill Group Real Time All Fields.

Grouping: This report is
                              		  grouped by Skill Group

Value Lists: Skill Group,
                              		  Media Routing Domain

Database Schema Tables from
                                 			 which data is retrieved:

Media_Routing_Domain

Skill_Group

Skill_Group_Real_Time

### Available Fields
                           	 in the Peripheral Skill Group Real Time All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are derived from the
                                 		  Skill_Group_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in the Peripheral Skill Group Real Time All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Skill Group

The
                                             						enterprise name of the skill group and its skill target ID.

Derived
                                             						from: Skill_Group.EnterpriseName and Skill_Group.SkillTargetID.

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Queued Now

The number of calls currently queued to the skill group at the Unified CCE (Network Queue) and at the local ACD queue .

This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Queued Now (ICM) is Available by default.

Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow.

Longest Queued

The
                                             						longest queued task on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format.

This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Longest Task Q (ICM) is Available by default.

Derived
                                             						from: Skill_Group_Real_Time.RouterLongestCallInQ.

Average Speed of Answer to 5

The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the skill group during the rolling five minute interval.

Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5.

Answered Within Service Level

The
                                             						Average Speed of Answer during the rolling five minute interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds) format for the skill group.

Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5.

Abandoned Within Service Level

The count of calls that are answered within the skill group service level threshold during the rolling five minute interval.

Derived
                                             						from:  Skill_Group_Real_Time.ServiceLevelCallsTo5.

Handled

The
                                             						number of tasks that were handled during the rolling five-minute interval.

Derived
                                             						from: Skill_Group_Real_Time.CallsHandledTo5.

Average Handle Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it takes during the rolling
                                             						five-minute interval to handle a task.

Derived
                                             						from: Skill_Group_Real_Time.HandleCallsTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5.

Log On

The
                                             						number of agents that are currently logged in to the skill group. This count is
                                             						updated each time an agent logs in and each time an agent logs out.

Derived
                                             						from: Skill_Group_Real_Time.LoggedOn.

Not
                                             						Ready

The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged on but are neither involved in any call
                                             						handling activity nor available to handle a call.

Derived
                                             						from: Skill_Group_Real_Time.NotReady.

Not
                                             						Active

The
                                             						number of agents in the skill group who are currently not working on a task
                                             						associated with the skill group.

Derived
                                             						from: Skill_Group_Real_Time.Avail.

Active
                                             						In

The
                                             						number of agents in the skill group currently working on inbound tasks.

Derived
                                             						from: Skill_Group_Real_Time.TalkingIn.

Active
                                             						Out

The
                                             						number of agents in the skill group currently talking on outbound calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingOut.

Active
                                             						Other

The
                                             						number of agents in the skill group currently talking on internal (neither
                                             						inbound nor outbound) calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingOther.

Active
                                             						Auto Out

The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingAutoOut.

Active
                                             						Preview

The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingPreview.

Active
                                             						Reservation

The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingReserve.

Avg Active Time

The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval.

Derived
                                             						from: (Skill_Group_Real_Time.HandledCallsTalkTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5).

Wrap Up

The
                                             						number of agents currently in wrap-up state for this skill group. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state.

Derived
                                             						from: Skill_Group_Real_Time.WorkReady + Skill_Group_Real_Time.WorkNotReady.

Hold

The
                                             						number of agents that have all active calls on hold or whose state to the skill
                                             						group is Paused. The agent is not in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold.

Derived
                                             						from: Skill_Group_Real_Time.Hold.

Reserved

The
                                             						number of agents for the skill group currently in the Reserved state. Reserved
                                             						is a state in which an agent is awaiting a call and is unavailable to receive
                                             						any incoming calls. This state applies only to agents on Northern Meridian
                                             						ACDs.

Derived
                                             						from: Skill_Group_Real_Time.ReservedAgents.

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state.

Busy
                                             						Other is a state in which the agent is handling calls assigned to other skill
                                             						groups during the interval.

For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged in to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state.

Derived
                                             						from: Skill_Group_Real_Time.BusyOther.

%
                                             						Utilization

The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready.

Derived from: Skill_Group_Real_Time.PercentUtilizationTo5.

Report Summary: There is a summary row for Skill Group. There is a total report summary for all fields except % Busy Other.

### Available Fields
                           	 in the Peripheral Skill Group Real Time All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are derived from the
                                 		  Skill_Group_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in the Peripheral Skill Group Real Time All Fields Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are
                                 		  listed below in the order (left to right) in which they appear by default in
                                 		  the stock template.

Column
                                             						(Field)

Description

Skill Group

The
                                             						enterprise name of the skill group and its skill target ID.

Derived
                                             						from: Skill_Group.EnterpriseName and Skill_Group.SkillTargetID.

Media

The enterprise name of the Media Routing Domain associated with the skill group.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Queued Now

The number of calls currently queued to the skill group at the Unified CCE (Network Queue) and at the local ACD queue .

This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Queued Now (ICM) is Available by default.

Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow.

Longest Queued

The
                                             						longest queued task on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format.

This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Longest Task Q (ICM) is Available by default.

Derived
                                             						from: Skill_Group_Real_Time.RouterLongestCallInQ.

Average Speed of Answer to 5

The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the skill group during the rolling five minute interval.

Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5.

Answered Within Service Level

The
                                             						Average Speed of Answer during the rolling five minute interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds) format for the skill group.

Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5.

Abandoned Within Service Level

The count of calls that are answered within the skill group service level threshold during the rolling five minute interval.

Derived
                                             						from:  Skill_Group_Real_Time.ServiceLevelCallsTo5.

Handled

The
                                             						number of tasks that were handled during the rolling five-minute interval.

Derived
                                             						from: Skill_Group_Real_Time.CallsHandledTo5.

Average Handle Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it takes during the rolling
                                             						five-minute interval to handle a task.

Derived
                                             						from: Skill_Group_Real_Time.HandleCallsTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5.

Log On

The
                                             						number of agents that are currently logged in to the skill group. This count is
                                             						updated each time an agent logs in and each time an agent logs out.

Derived
                                             						from: Skill_Group_Real_Time.LoggedOn.

Not
                                             						Ready

The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged on but are neither involved in any call
                                             						handling activity nor available to handle a call.

Derived
                                             						from: Skill_Group_Real_Time.NotReady.

Not
                                             						Active

The
                                             						number of agents in the skill group who are currently not working on a task
                                             						associated with the skill group.

Derived
                                             						from: Skill_Group_Real_Time.Avail.

Active
                                             						In

The
                                             						number of agents in the skill group currently working on inbound tasks.

Derived
                                             						from: Skill_Group_Real_Time.TalkingIn.

Active
                                             						Out

The
                                             						number of agents in the skill group currently talking on outbound calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingOut.

Active
                                             						Other

The
                                             						number of agents in the skill group currently talking on internal (neither
                                             						inbound nor outbound) calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingOther.

Active
                                             						Auto Out

The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingAutoOut.

Active
                                             						Preview

The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingPreview.

Active
                                             						Reservation

The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls.

Derived
                                             						from: Skill_Group_Real_Time.TalkingReserve.

Avg Active Time

The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval.

Derived
                                             						from: (Skill_Group_Real_Time.HandledCallsTalkTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5).

Wrap Up

The
                                             						number of agents currently in wrap-up state for this skill group. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state.

Derived
                                             						from: Skill_Group_Real_Time.WorkReady + Skill_Group_Real_Time.WorkNotReady.

Hold

The
                                             						number of agents that have all active calls on hold or whose state to the skill
                                             						group is Paused. The agent is not in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold.

Derived
                                             						from: Skill_Group_Real_Time.Hold.

Reserved

The
                                             						number of agents for the skill group currently in the Reserved state. Reserved
                                             						is a state in which an agent is awaiting a call and is unavailable to receive
                                             						any incoming calls. This state applies only to agents on Northern Meridian
                                             						ACDs.

Derived
                                             						from: Skill_Group_Real_Time.ReservedAgents.

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state.

Busy
                                             						Other is a state in which the agent is handling calls assigned to other skill
                                             						groups during the interval.

For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged in to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state.

Derived
                                             						from: Skill_Group_Real_Time.BusyOther.

%
                                             						Utilization

The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready.

Derived from: Skill_Group_Real_Time.PercentUtilizationTo5.

Report Summary: There is a summary row for Skill Group. There is a total report summary for all fields except % Busy Other.

## Precision Queue
                        	 Real Time All Fields

The Precision
                              		  Queue Real Time report shows the current status of the selected precision
                              		  queues. The report provides information such as calls in queue and longest
                              		  delay per precision queue.

Query: This report data is built from a Database Query.

Views: This report one grid view, Precision Queue Real Time All Fields.

Grouping: This report is grouped by Precision Queue.

Value Lists: Precision
                              		  Queue, Media Routing Domain

Database Schema Tables from which data is retrieved:

Attributes

Media_Routing_Domain

Precision_Q_Real_Time

Precision_Queue

### Available Fields
                           	 in the Precision Queue Real Time All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are derived from the
                                 		  Precision_Queue_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in the Precision Queue Real Time All Fields Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

The following
                                 		  current fields are listed in the order (left to right) in which they appear by
                                 		  default in the stock template.

Column
                                             						(Field)

Description

Precision Queue

The
                                             						enterprise name of the precision queue.

Derived
                                             						from: Precision_Queue.EnterpriseName.

Media

The enterprise name of the Media Routing Domain associated with the precision queue.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

Derived from: Attribute.EnterpriseName

Queued
                                             						Now

The
                                             						number of calls currently queued to the precision queue.

Derived
                                             						from: Precision_Q_Real_Time.CallsQNow.

Longest Queued

The
                                             						longest queued call on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format.

Derived
                                             						from: Precision_Q_Real_Time.LongestCallInQ

Avg Speed of Answer 5

The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the precision queue during the rolling five-minute interval.

Derived
                                             						from: Precision_Q_Real_Time.AnswerWaitTimeTo5/
                                             						Precision_Q_Real_Time.CallsAnsweredTo5.

Answered Within Service Level

The
                                             						count of calls that are answered within the precision queue service level
                                             						threshold during the rolling five-minute interval.

Derived
                                             						from: Precision_Q_Real_Time.ServiceLevelCallsAnsTo5

Abandon Within Service Level

The
                                             						count of calls that are abandoned within the precision queue service level
                                             						threshold during the rolling five-minute interval.

Derived
                                             						from: Precision_Q_Real_Time.ServiceLevelCallsAbandTo5.

Handled

The
                                             						number of tasks that have been handled during the rolling five-minute interval.

Derived
                                             						from: Precision_Q_Real_Time.CallsHandledTo5.

Avg Handle Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it takes during the rolling
                                             						five-minute interval to handle a task.

Derived
                                             						from: Precision_Q_Real_Time.HandleCallsTimeTo5 /
                                             						Precision_Q_Real_Time.CallsHandledTo5.

Logged On

The
                                             						number of agents that are currently logged in to the precision queue. This
                                             						count is updated each time an agent logs on and each time an agent logs off.

Derived
                                             						from: Precision_Q_Real_Time.LoggedOn.

Not
                                             						Ready

The
                                             						number of agents in the Not Ready state for the precision queue. Not Ready is a
                                             						state in which agents are logged in but are neither involved in any call
                                             						handling activity nor available to handle a call.

Derived
                                             						from: Precision_Q_Real_Time.NotReady.

Not
                                             						Active

The
                                             						number of agents in the precision queue who are currently not working on a task
                                             						associated with the precision queue.

Derived
                                             						from: Precision_Q_Real_Time.Avail.

Active
                                             						In

The
                                             						number of agents in the  precision queue currently working on inbound tasks.

Derived
                                             						from:  Precision_Q_Real_Time.TalkingIn

Active
                                             						Other

The number of agents in the precision queue currently talking on international (neither inbound nor outbound) calls.

Derived
                                             						from:  Precision_Q_Real_Time.TalkingOther

Avg Active Time

The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval.

Derived
                                             						from: ( Precision_Q_Real_Time.HandledCallsTalkTimeTo5
                                             						/  Precision_Q_Real_Time.CallsHandledTo5)

Wrap
                                             						Up

The
                                             						number of agents currently in wrap-up state for this  precision queue. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state.

Derived from:  Precision_Q_Real_Time.WorkReady +
                                             						 Precision_Q_Real_Time.WorkNotReady

Hold

The
                                             						number of agents that have all active calls on hold or whose state to the  precision queue is Paused. The agent is not
                                             in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold.

Derived from:  Precision_Q_Real_Time.Hold

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state.

Busy
                                             						Other is a state in which the agent is  handling calls assigned to other  precision queues during the interval.

For
                                             						example, an agent might be talking on an inbound call in one  precision queue while
                                             						simultaneously logged on to and ready to accept calls from other  precision queues.
                                             						The agent can be active (talking on or handling calls) in only one  precision queue
                                             						at a time. Therefore, while active in one  precision queue, for the other  precision queue the agent is considered to
                                             be in the Busy Other state.

Derived from:  Precision_Q_Real_Time.BusyOther

%
                                             						Utilization

The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready.

Derived from: Skill_Group_Real_Time.PercentUtilizationTo5

### Available Fields
                           	 in the Precision Queue Real Time All Fields Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are derived from the
                                 		  Precision_Queue_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in the Precision Queue Real Time All Fields Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

The following
                                 		  current fields are listed in the order (left to right) in which they appear by
                                 		  default in the stock template.

Column
                                             						(Field)

Description

Precision Queue

The
                                             						enterprise name of the precision queue.

Derived
                                             						from: Precision_Queue.EnterpriseName.

Media

The enterprise name of the Media Routing Domain associated with the precision queue.

Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName.

Attributes

The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used.

Derived from: Attribute.EnterpriseName

Queued
                                             						Now

The
                                             						number of calls currently queued to the precision queue.

Derived
                                             						from: Precision_Q_Real_Time.CallsQNow.

Longest Queued

The
                                             						longest queued call on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format.

Derived
                                             						from: Precision_Q_Real_Time.LongestCallInQ

Avg Speed of Answer 5

The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the precision queue during the rolling five-minute interval.

Derived
                                             						from: Precision_Q_Real_Time.AnswerWaitTimeTo5/
                                             						Precision_Q_Real_Time.CallsAnsweredTo5.

Answered Within Service Level

The
                                             						count of calls that are answered within the precision queue service level
                                             						threshold during the rolling five-minute interval.

Derived
                                             						from: Precision_Q_Real_Time.ServiceLevelCallsAnsTo5

Abandon Within Service Level

The
                                             						count of calls that are abandoned within the precision queue service level
                                             						threshold during the rolling five-minute interval.

Derived
                                             						from: Precision_Q_Real_Time.ServiceLevelCallsAbandTo5.

Handled

The
                                             						number of tasks that have been handled during the rolling five-minute interval.

Derived
                                             						from: Precision_Q_Real_Time.CallsHandledTo5.

Avg Handle Time

The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it takes during the rolling
                                             						five-minute interval to handle a task.

Derived
                                             						from: Precision_Q_Real_Time.HandleCallsTimeTo5 /
                                             						Precision_Q_Real_Time.CallsHandledTo5.

Logged On

The
                                             						number of agents that are currently logged in to the precision queue. This
                                             						count is updated each time an agent logs on and each time an agent logs off.

Derived
                                             						from: Precision_Q_Real_Time.LoggedOn.

Not
                                             						Ready

The
                                             						number of agents in the Not Ready state for the precision queue. Not Ready is a
                                             						state in which agents are logged in but are neither involved in any call
                                             						handling activity nor available to handle a call.

Derived
                                             						from: Precision_Q_Real_Time.NotReady.

Not
                                             						Active

The
                                             						number of agents in the precision queue who are currently not working on a task
                                             						associated with the precision queue.

Derived
                                             						from: Precision_Q_Real_Time.Avail.

Active
                                             						In

The
                                             						number of agents in the  precision queue currently working on inbound tasks.

Derived
                                             						from:  Precision_Q_Real_Time.TalkingIn

Active
                                             						Other

The number of agents in the precision queue currently talking on international (neither inbound nor outbound) calls.

Derived
                                             						from:  Precision_Q_Real_Time.TalkingOther

Avg Active Time

The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval.

Derived
                                             						from: ( Precision_Q_Real_Time.HandledCallsTalkTimeTo5
                                             						/  Precision_Q_Real_Time.CallsHandledTo5)

Wrap
                                             						Up

The
                                             						number of agents currently in wrap-up state for this  precision queue. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state.

Derived from:  Precision_Q_Real_Time.WorkReady +
                                             						 Precision_Q_Real_Time.WorkNotReady

Hold

The
                                             						number of agents that have all active calls on hold or whose state to the  precision queue is Paused. The agent is not
                                             in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold.

Derived from:  Precision_Q_Real_Time.Hold

Busy
                                             						Other

The
                                             						number of agents currently in the BusyOther state.

Busy
                                             						Other is a state in which the agent is  handling calls assigned to other  precision queues during the interval.

For
                                             						example, an agent might be talking on an inbound call in one  precision queue while
                                             						simultaneously logged on to and ready to accept calls from other  precision queues.
                                             						The agent can be active (talking on or handling calls) in only one  precision queue
                                             						at a time. Therefore, while active in one  precision queue, for the other  precision queue the agent is considered to
                                             be in the Busy Other state.

Derived from:  Precision_Q_Real_Time.BusyOther

%
                                             						Utilization

The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready.

Derived from: Skill_Group_Real_Time.PercentUtilizationTo5

## Precision Queue
                        	 Step Real Time

The Precision
                              		  Queue Step Real Time report generated from this template shows the current
                              		  status of the selected precision queues. The report provides real time
                              		  information on a per-step basis to provide visibility into which step calls are
                              		  queued in currently.

Query: This report is built from a Database Query.

Views: This report has one grid view, Precision Step Real Time.

Grouping: This report is grouped by Precision Queue and by Step Order.

Value List: Precision
                              		  Queue

Database Schema Tables from which data is retrieved:

Precision_Queue

Precision_Queue_Step

Precision_Q_Step_Real_Time

### Available Fields
                           	 in the Precision Queue Step Real Time Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are derived from the
                                 		  Precision_Q_Step_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in
                           	 the Precision Queue Step Real Time Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

The following
                                 		  current fields are listed in the order (left to right) in which they appear by
                                 		  default in the stock template.

Column
                                             						(Field)

Description

Precision Queue

The
                                             						enterprise name of the precision queue and its precision queue ID.

Derived
                                             						from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID.

Step

An integer
                                             						that defines the unique row for a precision queue step. It is the primary key.

Derived
                                             						from: Precision_Queue_Step.PrecisionQueueStepID.

Agents Logged On

The number of agents logged on for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.AgentsLoggedIn.

Agents Available

The
                                             						number of agents eligible and available for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.AgentsAvailable.

Longest Available Agent

The
                                             						length of time that the next agent to be selected has been available.

Derived
                                             						from: Precision_Q_Step_Real_Time.NextAvailAgent.

In Queue

The number of tasks in queue for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.CallsInQueue.

Avg Queue Time

The
                                             						average length of queue time for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.AvgCallsInQueueTime.

Longest Queued

The time
                                             						stamp of the longest call in queue for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.LongestCallInQueue.

### Available Fields
                           	 in the Precision Queue Step Real Time Grid View

Available fields
                                 		  for this report include the fields that appear by default as Current.
                                 		  Additional Available fields in this report are derived from the
                                 		  Precision_Q_Step_Real_Time table as documented in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

### Current Fields in
                           	 the Precision Queue Step Real Time Grid View

Current fields are
                                 		  those fields that appear by default in a report generated from the stock
                                 		  template.

The following
                                 		  current fields are listed in the order (left to right) in which they appear by
                                 		  default in the stock template.

Column
                                             						(Field)

Description

Precision Queue

The
                                             						enterprise name of the precision queue and its precision queue ID.

Derived
                                             						from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID.

Step

An integer
                                             						that defines the unique row for a precision queue step. It is the primary key.

Derived
                                             						from: Precision_Queue_Step.PrecisionQueueStepID.

Agents Logged On

The number of agents logged on for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.AgentsLoggedIn.

Agents Available

The
                                             						number of agents eligible and available for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.AgentsAvailable.

Longest Available Agent

The
                                             						length of time that the next agent to be selected has been available.

Derived
                                             						from: Precision_Q_Step_Real_Time.NextAvailAgent.

In Queue

The number of tasks in queue for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.CallsInQueue.

Avg Queue Time

The
                                             						average length of queue time for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.AvgCallsInQueueTime.

Longest Queued

The time
                                             						stamp of the longest call in queue for this precision queue step.

Derived
                                             						from: Precision_Q_Step_Real_Time.LongestCallInQueue.

## System Capacity
                        	 Real Time

The System
                              		  Capacity Real Time report presents a summary of overall system capacity. The
                              		  table provides system capacity, congestion information, and key performance
                              		  indicators.

Query: This report data
                              		  is built from a Database Query.

Views:

This report has one grid view, System Capacity Real Time and the following chart views:

Congestion Information

Current Rejection Percentage

Key Performance Indicators

Grouping: This report is grouped by Unified CCE Instance Enterprise Name.

Value List: ICR
                              		  Instance

Database Schema Tables from
                                 			 which data is retrieved:

System_Capacity_Real_Time

ICR_Instance

Controller_Time

Congestion_Control

### Available
                              		  Fields in the System Capacity Real Time Grid View and Gauge View

Available fields
                              		  for the grid view for this report include the fields that display by default as
                              		  current. Additional available fields in this report are taken directly from the
                              		  System_Capacity Real_time table as documented in the Database
                                 			 Schema Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

There is one
                              		  additional available field in this report, which is ICRInstanceID. This field
                              		  is derived from System_Capacity_Real_Time.ICRInstanceID and is a unique
                              		  identifier for the instance.

Grid views and a
                              		  gauge view are available. The grid views are as follows:

Congestion
                                    				Information, which displays the congestion details in real time.

Key
                                    				Performance Indicators, which displays the capacity details in real time.

System
                                    				Capacity Real Time, which displays both congestion and system capacity details
                                    				in real time.

The gauge view
                              		  has a Rejection Percentage view, which displays the current rejection
                              		  percentage.

### Current Fields
                              		  in the System Capacity Report Views

Current fields are those fields that appear by default in a report generated from the stock template.

Current fields are listed in the order (left to right) in which they appear by default in the stock template.

Columns
                                          						(Fields)

Description

Unified CCE Instance Name

An
                                          						enterprise name for the node. This name must be unique for all nodes in the
                                          						enterprise.

Derived
                                          						from ICR_Instance.EnterpriseName.

Deployment Type

The Unified CCE deployment type.

DateTime

The
                                          						date and time of the selected row's data in YYYY/MM/DD ( year, month, date) and
                                          						HH:MM:SS (hour, minute, second) format.

Derived
                                          						from System_Capacity_Real_Time.DateTime.

Current
                                          						Congestion Level

The
                                          						current congestion mode in the system:

No Congestion = General operating mode with no congestion

Level 1 = Congestion mode is level 1

Level 2 = Congestion mode is level 2

Level 3 = Congestion mode is level 3

The
                                          						threshold that has been set for this field:

On
                                                							 No Congestion, the background color field is Green

On
                                                							 Level 1, the background color field is Yellow

On
                                                							 Level 2, the background color field is Yellow

On
                                                							 Level 3, the background color field is Red

Current
                                          						Rejection Percentage

The call
                                          						reduction percentage based on the current congestion level:

For Level 0, reduction percentage is 0 %.

For Level 1, reduction percentage is 10 %.

For Level 2, reduction percentage is 30 %.

For Level 3, reduction percentage varies from 30% to 100%
                                                							 depending on the incoming call rate.

Duration
                                          						Congested at Current Level

The
                                          						time that the system has been at the current congestion level, even if it is
                                          						Level 0 (No Congestion.) Measured in HH:MM:SS (hours, minutes, seconds) format.

This
                                          						field is a calculated field derived from: DATEDIFF(minutes,
                                          						System_Capacity_Real_Time.DateTimeCurrentLevel, Controller_Time.NowTime).

Duration
                                          						Congested

The
                                          						time spent in congestion measured in HH:MM:SS (hours, minutes, seconds) format.
                                          						This value is 0 if the current congestion level is Level 0 (No Congestion).

This
                                          						is a calculated field derived from: DATEDIFF(minutes,
                                          						System_Capacity_Real_Time.DateTimeCongested, Controller_Time.NowTime).

Level1
                                          						Onset CPS

Onset
                                          						Calls Per Second (CPS) determination for Congestion level 1.

Level1
                                          						Abatement CPS

Abatement CPS determination for Congestion Level 1.

Derived
                                          						from System_Capacity_Real_Time.Level1Abatement

Level1
                                          						Reduction

Call
                                          						rate reduction percentage for Congestion Level 1.

Derived from System_Capacity_Real_Time.Level1Reduction

Level2
                                          						Onset CPS

Onset
                                          						CPS determination for Congestion level 2.

Derived from System_Capacity_Real_Time.Level2Onset

Level2
                                          						Abatement CPS

Abatement CPS determination for Congestion level 2.

Derived from System_Capacity_Real_Time.Level2Abatement

Level2
                                          						Reduction

Call
                                          						rate reduction percentage for Congestion Level 2.

Derived from System_Capacity_Real_Time.Level2Reduction

Level3
                                          						Onset CPS

Onset
                                          						CPS determination for Congestion level 3.

Derived from System_Capacity_Real_Time.Level3Onset

Level3
                                          						Abatement CPS

Abatement CPS determination for Congestion level 3.

Derived from System_Capacity_Real_Time.Level3Abatement

Level3
                                          						Reduction

Call
                                          						rate reduction percentage for Congestion Level 3.

Derived from System_Capacity_Real_Time.Level3Reduction

Total
                                          						Agents Logged On

The
                                          						total number of agents logged in to the system.

Derived from System_Capacity_Real_Time.TotalAgentsLoggedOn

Avg
                                          						Skills Per Agent

The
                                          						average number of skill groups associated per agent.

Derived from System_Capacity_Real_Time.AverageSkillsPerAgent

Configured Capacity in CPS

Configured call per second capacity of the system.

Derived from System_Capacity_Real_Time.ConfiguredCapacity

Adjusted Capacity in CPS

Adjusted Call per second capacity during run time.

Derived from System_Capacity_Real_Time.AdjustedCapacity

Avg
                                          						CPS

Runtime weighed averaged call per second.

Derived from System_Capacity_Real_Time.AverageCPS

| Column
                                             						(Field) | Description |
|---|---|
| Agent | The last
                                             						and first name of the agent. Derived
                                             						from: Person.LastName "," Person.FirstName |
| Precision Queue | The precision queues with which the agent is associated. Derived
                                             						from: Precision_Queue.EnterpriseName |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |

| Column
                                             						(Field) | Description |
|---|---|
| Agent | The last
                                             						and first name of the agent. Derived
                                             						from: Person.LastName "," Person.FirstName |
| Precision Queue | The precision queues with which the agent is associated. Derived
                                             						from: Precision_Queue.EnterpriseName |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue / Skill Group | Precision Queue or Skill Group or NotApplicable. Precision
                                             						Queue is derived from:Precision_Queue.EnterpriseName. The
                                             						precision route associated with the task on which the agent is currently
                                             						working. If the agent is not involved in any task in the media routing domain,
                                             						this field shows Not Applicable. Because an agent can log in to multiple
                                             						precision routes, this field is not filled until the agent is assigned a task. Skill
                                             						Group Name is derived from: Skill_Group.EnterpriseName. The skill
                                             						group associated with the task on which the agent is currently working. If the
                                             						agent is not involved in any task in the media routing domain, this field shows
                                             						Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             						this field is not filled until the agent is assigned a task. |
| Attributes 1 to 10 | The attributes used in the precision queue definition. The report shows only those attributes that are used. Derived from: Attribute.EnterpriseName |
| Agent | The last and first name of the agent. Derived from: Person.LastName "," Person.FirstName. |
| Queued Now | The Queued Now field is a calculated field based onthe Agent_Real_Time. The number in the field increments only if: The ICM Script uses Queue to Agent Node. The agent is not available to take the call. There is no other way for the router to queue a call at an agent. |
| Extension | The phone extension into which the agent is logged. Derived from: Agent_Real_Time.Extension |
| Agent State | The current state of the agent in this skill group. Derived from: Agent_Skill_Group_Real_Time.AgentState |
| Logged on Date Time | The time spent in the current agent state in this skill group in HH:MM:SS (hours, minutes, seconds) format. Derived from: Agent_Real_Time.DateTimeLogin |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, getdate()). |
| Mobile Agent Mode | The mode by which the agent is connected (populated for CCE only): 0 = Not Mobile (Local agent; general ACD/CCE phone or non-voice task) 1 = Call By Call (Mobile agent's phone is connected for each incoming call) 2 = Nailed Connection (Mobile agent calls andlogs in once; line remains connected through multiple calls) Derived from: Agent_Real_Time.PhoneType |
| Mobile Agent Phone# | For a mobile agent (an agent working remotely), the current phone number. Populated for CCE only. Derived from: Agent_Real_Time.RemotePhoneNumber |
| Reason | A code received from the peripheral that indicates the reason for the agent's last state change. If the code is not defined,
                                             this displays 0. To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information. Derived from: Agent_Real_Time.ReasonCode. |
| Supervisor Assist Requested | Whether or not the agent requested supervisor assistance: No\|Yes. Derived from: Agent_Real_Time.RequestedSupervisorAssist |
| Destination | The type of outbound task on which the agent is currently working. Derived from: Agent_Real_Time.Destination. |
| Direction | The direction of active task: In (inbound task, as non-voice tasks are always inbound). Out (outgoing external task). Other (outgoing or incoming internal task). Not Applicable (if the logged-in agent is not active in the skill group). Derived from: Agent_Real_Time.Direction. |
| Available in MRD | Whether or not the agent is available to accept a task in this media routing domain: NO (Not available) YES_ICM ( Unified CCE available in media routing domain) YES_APP (Application available in media routing domain) An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready, the agent is not at the agent's maximum task limit for the MRD, and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is ICM-available, then Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent. |
| Active | The number of tasks associated with the skill group that the agent is working on. Derived from: Agent_Skill_Group_Real_Time.CallsInProgress |
| Agent Skill Target ID | The
                                             						current state of the agent. Derived
                                             						from: Agent_Real_Time.AgentState. |
| Skill Target ID | This report is grouped and sorted by Skill Target ID. Skill Target ID Derived from: Skill_Group.SkillTargetID. |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue / Skill Group | Precision Queue or Skill Group or NotApplicable. Precision
                                             						Queue is derived from:Precision_Queue.EnterpriseName. The
                                             						precision route associated with the task on which the agent is currently
                                             						working. If the agent is not involved in any task in the media routing domain,
                                             						this field shows Not Applicable. Because an agent can log in to multiple
                                             						precision routes, this field is not filled until the agent is assigned a task. Skill
                                             						Group Name is derived from: Skill_Group.EnterpriseName. The skill
                                             						group associated with the task on which the agent is currently working. If the
                                             						agent is not involved in any task in the media routing domain, this field shows
                                             						Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             						this field is not filled until the agent is assigned a task. |
| Attributes 1 to 10 | The attributes used in the precision queue definition. The report shows only those attributes that are used. Derived from: Attribute.EnterpriseName |
| Agent | The last and first name of the agent. Derived from: Person.LastName "," Person.FirstName. |
| Queued Now | The Queued Now field is a calculated field based onthe Agent_Real_Time. The number in the field increments only if: The ICM Script uses Queue to Agent Node. The agent is not available to take the call. There is no other way for the router to queue a call at an agent. |
| Extension | The phone extension into which the agent is logged. Derived from: Agent_Real_Time.Extension |
| Agent State | The current state of the agent in this skill group. Derived from: Agent_Skill_Group_Real_Time.AgentState |
| Logged on Date Time | The time spent in the current agent state in this skill group in HH:MM:SS (hours, minutes, seconds) format. Derived from: Agent_Real_Time.DateTimeLogin |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, getdate()). |
| Mobile Agent Mode | The mode by which the agent is connected (populated for CCE only): 0 = Not Mobile (Local agent; general ACD/CCE phone or non-voice task) 1 = Call By Call (Mobile agent's phone is connected for each incoming call) 2 = Nailed Connection (Mobile agent calls andlogs in once; line remains connected through multiple calls) Derived from: Agent_Real_Time.PhoneType |
| Mobile Agent Phone# | For a mobile agent (an agent working remotely), the current phone number. Populated for CCE only. Derived from: Agent_Real_Time.RemotePhoneNumber |
| Reason | A code received from the peripheral that indicates the reason for the agent's last state change. If the code is not defined,
                                             this displays 0. To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information. Derived from: Agent_Real_Time.ReasonCode. |
| Supervisor Assist Requested | Whether or not the agent requested supervisor assistance: No\|Yes. Derived from: Agent_Real_Time.RequestedSupervisorAssist |
| Destination | The type of outbound task on which the agent is currently working. Derived from: Agent_Real_Time.Destination. |
| Direction | The direction of active task: In (inbound task, as non-voice tasks are always inbound). Out (outgoing external task). Other (outgoing or incoming internal task). Not Applicable (if the logged-in agent is not active in the skill group). Derived from: Agent_Real_Time.Direction. |
| Available in MRD | Whether or not the agent is available to accept a task in this media routing domain: NO (Not available) YES_ICM ( Unified CCE available in media routing domain) YES_APP (Application available in media routing domain) An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready, the agent is not at the agent's maximum task limit for the MRD, and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is ICM-available, then Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent. |
| Active | The number of tasks associated with the skill group that the agent is working on. Derived from: Agent_Skill_Group_Real_Time.CallsInProgress |
| Agent Skill Target ID | The
                                             						current state of the agent. Derived
                                             						from: Agent_Real_Time.AgentState. |
| Skill Target ID | This report is grouped and sorted by Skill Target ID. Skill Target ID Derived from: Skill_Group.SkillTargetID. |

| Column
                                             						(Field) | Description |
|---|---|
| Agent | The last
                                             						and first name of the agent. Derived
                                             						from: Person.LastName "," Person.FirstName. |
| Precision Queue / Skill Group | Precision Queue or Skill Group or NotApplicable. Precision
                                             						Queue is derived from:Precision_Queue.EnterpriseName. The
                                             						precision route associated with the task on which the agent is currently
                                             						working. If the agent is not involved in any task in the media routing domain,
                                             						this field shows Not Applicable. Because an agent can log in to multiple
                                             						precision routes, this field is not filled until the agent is assigned a task. Skill
                                             						Group Name is derived from: Skill_Group.EnterpriseName. The skill
                                             						group associated with the task on which the agent is currently working. If the
                                             						agent is not involved in any task in the media routing domain, this field shows
                                             						Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             						this field is not filled until the agent is assigned a task. |
| Media | The enterprise name of the Media Routing Domain associated with the Precision
                                             						Queue or  Skill Group Name. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. Derived from:  Attribute.EnterpriseName |
| AgentState | The
                                             						current state of the agent. Derived
                                             						from: Agent_Real_Time.AgentState. |
| Destination | The type
                                             						of outbound task on which the agent is currently working. Derived
                                             						from: Agent_Real_Time.Destination. |
| Direction | The
                                             						direction of active task: In
                                                   							 (inbound task, as non-voice tasks are always inbound). Out
                                                   							 (outgoing external task). Other
                                                   							 (outgoing or incoming internal task). Not
                                                   							 Applicable (if the logged-in agent is not active in the skill group). Derived
                                             						from: Agent_Real_Time.Direction. |
| Duration | The time
                                             						spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This field is a
                                             						calculated field derived from: DATEDIFF(seconds,
                                             						Agent_Real_Time.DateTimeLastStateChange, getdate()). |
| Reason | The text associated with the ReasonCode numeric value, which is a code received from the peripheral, indicates the reason
                                             for the agent's last state change. Note If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed. To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information. Derived from: Agent_Real_Time.ReasonCode. | Note | If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed. |
| Note | If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed. |

| Note | If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed. |
|---|---|

| Column
                                             						(Field) | Description |
|---|---|
| Agent | The last
                                             						and first name of the agent. Derived
                                             						from: Person.LastName "," Person.FirstName. |
| Precision Queue / Skill Group | Precision Queue or Skill Group or NotApplicable. Precision
                                             						Queue is derived from:Precision_Queue.EnterpriseName. The
                                             						precision route associated with the task on which the agent is currently
                                             						working. If the agent is not involved in any task in the media routing domain,
                                             						this field shows Not Applicable. Because an agent can log in to multiple
                                             						precision routes, this field is not filled until the agent is assigned a task. Skill
                                             						Group Name is derived from: Skill_Group.EnterpriseName. The skill
                                             						group associated with the task on which the agent is currently working. If the
                                             						agent is not involved in any task in the media routing domain, this field shows
                                             						Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             						this field is not filled until the agent is assigned a task. |
| Media | The enterprise name of the Media Routing Domain associated with the Precision
                                             						Queue or  Skill Group Name. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. Derived from:  Attribute.EnterpriseName |
| AgentState | The
                                             						current state of the agent. Derived
                                             						from: Agent_Real_Time.AgentState. |
| Destination | The type
                                             						of outbound task on which the agent is currently working. Derived
                                             						from: Agent_Real_Time.Destination. |
| Direction | The
                                             						direction of active task: In
                                                   							 (inbound task, as non-voice tasks are always inbound). Out
                                                   							 (outgoing external task). Other
                                                   							 (outgoing or incoming internal task). Not
                                                   							 Applicable (if the logged-in agent is not active in the skill group). Derived
                                             						from: Agent_Real_Time.Direction. |
| Duration | The time
                                             						spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This field is a
                                             						calculated field derived from: DATEDIFF(seconds,
                                             						Agent_Real_Time.DateTimeLastStateChange, getdate()). |
| Reason | The text associated with the ReasonCode numeric value, which is a code received from the peripheral, indicates the reason
                                             for the agent's last state change. Note If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed. To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information. Derived from: Agent_Real_Time.ReasonCode. | Note | If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed. |
| Note | If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed. |

| Note | If the ReasonCode does not have a corresponding entry in the Reason_Code table, then a numerical Reason Code is displayed.
                                                         Also, If the Reason Code is 0, "NONE" is displayed. |
|---|---|

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The skill group enterprise name for the selected skill group. Derived from:
                                             Skill_Group.EnterpriseName |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Agent | The last name and first name of the agent. Derived from: Person.LastName + ", " + Person.FirstName |
| Queued Now | The number of tasks currently queued for the skill group. Derived from: Skill_Group_Real_Time.RouterCallsQNow |
| Extension | The phone extension into which the agent is logged. Derived from: Agent_Real_Time.Extension |
| Agent State | The current state of the agent in this skill group. Derived from:  Agent_Skill_Group_Real_Time.AgentState |
| Log On DateTime | The time spent in the current agent state in this skill group in HH:MM:SS (hours, minutes, seconds) format. Derived from: Agent_Real_Time.DateTimeLogin |
| Duration | The time spent in the current agent
                                             state in HH:MM:SS (hours, minutes, seconds) format. This is a calculated field derived
                                             from: DATEDIFF(seconds,
                                             Agent_Skill_Group_Real_Time.DateTimeLastStateChange, getdate()) |
| Mobile Agent Mode | The mode by which the agent is connected (populated for CCE only): 0 = Not Mobile (Local agent; general ACD/CCE phone or non-voice task) 1 = Call By Call (Mobile agent's phone is connected for each incoming call) 2 = Nailed Connection (Mobile agent calls and logs in once; line remains connected through multiple calls) Derived from: Agent_Real_Time.PhoneType |
| Mobile Agent Phone# | For a mobile agent (an agent working
                                             remotely), the current phone number. Populated for CCE only. Derived from: Agent_Real_Time.RemotePhoneNumber |
| Reason | A code received from the peripheral that indicates the reason for the agent's last state change. If the code is not defined,
                                             the reason code displays 0. To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information. Derived from: Agent_Real_Time.ReasonCode |
| Supervisor Assist Requested | Whether or not the agent requested
                                             supervisor assistance: No\|Yes. Derived from:
                                             Agent_Real_Time.RequestedSupervisorAssist |
| Destination | The type of outbound task on which
                                             the agent is currently working. Derived from: Agent_Real_Time.Destination |
| Direction | The direction of the call that the
                                             agent is currently working on: NULL = None 0 = None 1 = In 2 = Out 3 = Other In 4 = Other Out/Outbound Direct Preview 5 = Outbound Reserve 6 = Outbound Preview 7 = Outbound Predictive/Progressive Derived from: Agent_Real_Time.Direction |
| Avail in MRD | Whether or not the agent is
                                             available to accept a task in this media routing domain: NO (Not available) YES_ICM ( Unified CCE available in media routing domain) YES_APP (Application available in media routing domain) An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready, the agent is not at the agent's maximum task limit for the MRD, and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is ICM-available, then Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent. |
| Active | The number of tasks associated with
                                             the skill group that the agent is working on. Derived from:
                                             Agent_Skill_Group_Real_Time.CallsInProgress |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The skill group enterprise name for the selected skill group. Derived from:
                                             Skill_Group.EnterpriseName |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Agent | The last name and first name of the agent. Derived from: Person.LastName + ", " + Person.FirstName |
| Queued Now | The number of tasks currently queued for the skill group. Derived from: Skill_Group_Real_Time.RouterCallsQNow |
| Extension | The phone extension into which the agent is logged. Derived from: Agent_Real_Time.Extension |
| Agent State | The current state of the agent in this skill group. Derived from:  Agent_Skill_Group_Real_Time.AgentState |
| Log On DateTime | The time spent in the current agent state in this skill group in HH:MM:SS (hours, minutes, seconds) format. Derived from: Agent_Real_Time.DateTimeLogin |
| Duration | The time spent in the current agent
                                             state in HH:MM:SS (hours, minutes, seconds) format. This is a calculated field derived
                                             from: DATEDIFF(seconds,
                                             Agent_Skill_Group_Real_Time.DateTimeLastStateChange, getdate()) |
| Mobile Agent Mode | The mode by which the agent is connected (populated for CCE only): 0 = Not Mobile (Local agent; general ACD/CCE phone or non-voice task) 1 = Call By Call (Mobile agent's phone is connected for each incoming call) 2 = Nailed Connection (Mobile agent calls and logs in once; line remains connected through multiple calls) Derived from: Agent_Real_Time.PhoneType |
| Mobile Agent Phone# | For a mobile agent (an agent working
                                             remotely), the current phone number. Populated for CCE only. Derived from: Agent_Real_Time.RemotePhoneNumber |
| Reason | A code received from the peripheral that indicates the reason for the agent's last state change. If the code is not defined,
                                             the reason code displays 0. To display Reason Codes in a Unified Intelligence Center report, you must configure them. See your configuration documentation
                                             for more information. Derived from: Agent_Real_Time.ReasonCode |
| Supervisor Assist Requested | Whether or not the agent requested
                                             supervisor assistance: No\|Yes. Derived from:
                                             Agent_Real_Time.RequestedSupervisorAssist |
| Destination | The type of outbound task on which
                                             the agent is currently working. Derived from: Agent_Real_Time.Destination |
| Direction | The direction of the call that the
                                             agent is currently working on: NULL = None 0 = None 1 = In 2 = Out 3 = Other In 4 = Other Out/Outbound Direct Preview 5 = Outbound Reserve 6 = Outbound Preview 7 = Outbound Predictive/Progressive Derived from: Agent_Real_Time.Direction |
| Avail in MRD | Whether or not the agent is
                                             available to accept a task in this media routing domain: NO (Not available) YES_ICM ( Unified CCE available in media routing domain) YES_APP (Application available in media routing domain) An agent is available for a task in a media routing domain (MRD) if the agent's state in that MRD is anything other than Not
                                             Ready, the agent is not at the agent's maximum task limit for the MRD, and the agent is not working on a non-interruptible
                                             task in another MRD. If an agent is ICM-available, then Unified CCE can assign tasks to the agent. If an agent is Application-available, then the application can assign tasks to the agent.
                                             In the former case, only Unified CCE can assign tasks to the agent. In the latter, only the application can assign tasks to the agent. |
| Active | The number of tasks associated with
                                             the skill group that the agent is working on. Derived from:
                                             Agent_Skill_Group_Real_Time.CallsInProgress |

| Field | Description |
|---|---|
| Not Ready | The agent is
                                          					 not available to be assigned a task. |
| Ready | The agent
                                          					 has put himself in the Ready state using his agent desktop tool. |
| Active | The agent is
                                          					 working on a task or a call. |
| Wrap Up | The agent is
                                          					 performing wrap-up work for a call. |
| Reserved | The agent has been
                                          					 offered a call or task. For voice
                                          					 calls, agents are Reserved when their phones are ringing. |
| Interrupted | The agent receives a non-interrupted call or task while handling an interrupted task. |
| Unknown | The agent
                                          					 state is unknown. |
| Hold | For agents
                                          					 handling Outbound Option calls, the Hold state indicates that the agent is  reserved for a call because the Outbound
                                          Dialer put the agent on hold
                                          					 while connecting the call. |

| Column (Field) | Description |
|---|---|
| Agent Team | The Enterprise Name of the Agent Team. Derived from: Agent_Team.EnterpriseName. |
| Supervisor | The Agent Team's primary supervisor. Derived from: Person.LastName ", " Person.FirstName. |
| Agent | The last and first name of the agent. Derived from: Person.LastName ", " Person.FirstName. |
| Precision Queue / Skill Group | Precision Queue or Skill Group or Not Applicable. Precision Queue is derived from: Agent_Team.EnterpriseName. The precision route associated with the task on which the agent is currently working. If the agent is not involved in any
                                             task in the Media Routing Domain, this field shows Not Applicable. Because an agent can log in to multiple precision routes,
                                             this field is not filled until the agent is assigned a task. Skill Group Name is derived from: Skill_Group.EnterpriseName. The skill group associated with the task on which the agent is currently working. If the agent is not involved in any task
                                             in the Media Routing Domain, this field shows Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             this field is not filled until the agent is assigned a task. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. Derived from: Attribute.EnterpriseName |
| State | The current state of the agent. Derived from: Agent_Real_Time.AgentState. |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, Select NowTime From
                                             Controller_Time) |
| Direction | The direction of the call that the agent is currently working on: NULL= None 0 = None 1 = In 2 =Out 3= Other Derived from: Agent_Real_Time.Direction. |
| Destination | The type of outbound task on which the agent is currently working. Derived from: Agent_Real_Time.Destination. |
| Reason | A code received from the peripheral that indicates the reason for the agent's last state change. If no reason code is defined,
                                             this value is 0 (zero). Derived from: Agent_Real_Time.ReasonCode. |

| Column (Field) | Description |
|---|---|
| Agent Team | The Enterprise Name of the Agent Team. Derived from: Agent_Team.EnterpriseName. |
| Supervisor | The Agent Team's primary supervisor. Derived from: Person.LastName ", " Person.FirstName. |
| Agent | The last and first name of the agent. Derived from: Person.LastName ", " Person.FirstName. |
| Precision Queue / Skill Group | Precision Queue or Skill Group or Not Applicable. Precision Queue is derived from: Agent_Team.EnterpriseName. The precision route associated with the task on which the agent is currently working. If the agent is not involved in any
                                             task in the Media Routing Domain, this field shows Not Applicable. Because an agent can log in to multiple precision routes,
                                             this field is not filled until the agent is assigned a task. Skill Group Name is derived from: Skill_Group.EnterpriseName. The skill group associated with the task on which the agent is currently working. If the agent is not involved in any task
                                             in the Media Routing Domain, this field shows Not Applicable. Because an agent can be logged in to multiple skill groups,
                                             this field is not filled until the agent is assigned a task. |
| Attributes | The attributes used in the precision queue definition. The report shows only those attributes that are used. Derived from: Attribute.EnterpriseName |
| State | The current state of the agent. Derived from: Agent_Real_Time.AgentState. |
| Duration | The time spent in the current agent state in HH:MM:SS (hours, minutes, seconds) format. This field is a calculated field derived from: DATEDIFF(seconds, Agent_Real_Time.DateTimeLastStateChange, Select NowTime From
                                             Controller_Time) |
| Direction | The direction of the call that the agent is currently working on: NULL= None 0 = None 1 = In 2 =Out 3= Other Derived from: Agent_Real_Time.Direction. |
| Destination | The type of outbound task on which the agent is currently working. Derived from: Agent_Real_Time.Destination. |
| Reason | A code received from the peripheral that indicates the reason for the agent's last state change. If no reason code is defined,
                                             this value is 0 (zero). Derived from: Agent_Real_Time.ReasonCode. |

| Note | An agent can
                                                				work on a task (Active In state) and be Eligible For Task in a media routing
                                                				domain. This can occur in the Multi Session Chat (MSC) Media Routing Domain. If
                                                				the agent is currently working on an MSC task, an agent is eligible to receive
                                                				a task up to the maximum task limit configured in the system. |
|---|---|

| Columns
                                             						(Fields) | Description |
|---|---|
| Agent Team | The
                                             						enterprise name of the Agent Team. Derived
                                             						from: Agent_Team.EnterpriseName. |
| Supervisor | The team's
                                             						primary supervisor. Derived
                                             						from: Person.LastName + ' ' + Person.FirstName. |
| Total On
                                             						Team | The count
                                             						of agents configured for the individual team. Derived
                                             						from:  Count(Agent_Team_Member.SkillTargetID). |
| Agent
                                             						Logged On | The number
                                             						of agents currently logged in. Derived
                                             						from: Count of agents with Agent_Real_Time.AgentState not equal to 0. |
| Active In | The number
                                             						of agents currently working on incoming tasks. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 1. |
| Active Out | The number
                                             						of agents currently working on outbound tasks. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 2. |
| Active
                                             						Other | The number
                                             						of agents currently working on internal (neither inbound nor outbound) tasks.
                                             						Examples of other tasks include agent-to-agent transfers and supervisor tasks. Derived
                                             						from: count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 3. |
| Hold | The number
                                             						of agents that have all active tasks on hold and have paused tasks. The agent
                                             						is not in the Hold state with one task on hold and talking on another task (for
                                             						example, a consultative call). The agent must have all active tasks on hold. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 10 or 12. |
| Not Active | The number
                                             						of agents in the Not Active state, the state where the agent is ready to accept
                                             						tasks, but is not currently involved in task work. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 3 or 14. |
| Wrap Up | The number
                                             						of agents in the Work Not Ready state and Work Ready state. The Work Not Ready
                                             						state is a state in which an agent is involved in after task work and is
                                             						assumed not to be ready to accept incoming tasks when done. The Work Ready
                                             						state is a state in which an agent is involved in after a task work and is
                                             						assumed to be ready to accept incoming tasks when done. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 5 or 6. |
| Not Ready | The number
                                             						of agents in the Not Ready state, a state in which agents are logged in but are
                                             						neither involved in any task handling activity nor available to handle a task. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 2. |
| Reserved | The number
                                             						of agents currently in the Reserved state, a state in which an agent is
                                             						selected to receive a task. An agent is in the Reserved state until the task is
                                             						answered. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 8. |

| Note | An agent can
                                                				work on a task (Active In state) and be Eligible For Task in a media routing
                                                				domain. This can occur in the Multi Session Chat (MSC) Media Routing Domain. If
                                                				the agent is currently working on an MSC task, an agent is eligible to receive
                                                				a task up to the maximum task limit configured in the system. |
|---|---|

| Columns
                                             						(Fields) | Description |
|---|---|
| Agent Team | The
                                             						enterprise name of the Agent Team. Derived
                                             						from: Agent_Team.EnterpriseName. |
| Supervisor | The team's
                                             						primary supervisor. Derived
                                             						from: Person.LastName + ' ' + Person.FirstName. |
| Total On
                                             						Team | The count
                                             						of agents configured for the individual team. Derived
                                             						from:  Count(Agent_Team_Member.SkillTargetID). |
| Agent
                                             						Logged On | The number
                                             						of agents currently logged in. Derived
                                             						from: Count of agents with Agent_Real_Time.AgentState not equal to 0. |
| Active In | The number
                                             						of agents currently working on incoming tasks. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 1. |
| Active Out | The number
                                             						of agents currently working on outbound tasks. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 2. |
| Active
                                             						Other | The number
                                             						of agents currently working on internal (neither inbound nor outbound) tasks.
                                             						Examples of other tasks include agent-to-agent transfers and supervisor tasks. Derived
                                             						from: count of agents where Agent_Real_Time.AgentState is 11 or 4 and
                                             						Agent_Real_Time.Direction is 3. |
| Hold | The number
                                             						of agents that have all active tasks on hold and have paused tasks. The agent
                                             						is not in the Hold state with one task on hold and talking on another task (for
                                             						example, a consultative call). The agent must have all active tasks on hold. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 10 or 12. |
| Not Active | The number
                                             						of agents in the Not Active state, the state where the agent is ready to accept
                                             						tasks, but is not currently involved in task work. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 3 or 14. |
| Wrap Up | The number
                                             						of agents in the Work Not Ready state and Work Ready state. The Work Not Ready
                                             						state is a state in which an agent is involved in after task work and is
                                             						assumed not to be ready to accept incoming tasks when done. The Work Ready
                                             						state is a state in which an agent is involved in after a task work and is
                                             						assumed to be ready to accept incoming tasks when done. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 5 or 6. |
| Not Ready | The number
                                             						of agents in the Not Ready state, a state in which agents are logged in but are
                                             						neither involved in any task handling activity nor available to handle a task. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 2. |
| Reserved | The number
                                             						of agents currently in the Reserved state, a state in which an agent is
                                             						selected to receive a task. An agent is in the Reserved state until the task is
                                             						answered. Derived
                                             						from: Count of agents where Agent_Real_Time.AgentState is 8. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type Name | The
                                             						enterprise name for the call type. Derived
                                             						from: Call_Type.EnterpriseName. |
| Avg Speed of Answer 5 | Average
                                             						Speed of Answer during the rolling five-minute interval. The total Answer Time
                                             						for all tasks of the call type divided by the number of tasks of this type
                                             						answered during the current five-minute interval. This field
                                             						is a calculated field, derived from: (Call_Type_Real_Time.AnswerWaitTimeTo5 /
                                             						Call_Type_Real_Time.CallsAnsweredTo5). |
| VRU not Queued Now | The number
                                             						of tasks in Run VRUScript or Wait state. This represents the number of tasks at
                                             						VRU prompting or self service. This field
                                             						is a calculated field, derived from: Call_Type_Real_Time.CallsAtVRUNow -
                                             						Call_Type_Real_Time.RouterCallsQNow. |
| Queued Now | The number
                                             						of tasks currently in the queue. Derived
                                             						from: Call_Type_Real_Time.RouterCallsQNow. |
| CCE Agent
                                             						Now | The number of tasks that have been routed to the Unified CCE agents but are not yet ended. This column is incremented when the call is answered and decremented when the call ends, after
                                             wrap up is complete, if applicable. Derived
                                             						from: Call_Type_Real_Time.CallsAtAgentNow. |
| Longest
                                             						Queued | The time
                                             						spent in queue for the longest currently queued task, measured in HH:MM:SS
                                             						(hours, minutes, seconds) format. This field
                                             						is a calculated field, determined by subtracting the time the task entered the
                                             						queue (Derived from: Call_Type_Real_Time.RouterLongestCallQ) from the current
                                             						time. |
| Service
                                             						Level | The Unified ICM/Unified CCE service level for the rolling five-minute interval. Derived
                                             						from: Call_Type_Interval.ServiceLevelTo5. |
| Handled5 | The number
                                             						of calls of this call type handled for the call type ending during the rolling
                                             						five-minute interval. Derived
                                             						from: Call_Type_Real_Time.CallsHandledTo5. |
| Aband5 | The number
                                             						of tasks abandoned at the IVR during the rolling five-minute interval, while
                                             						offered to the agent and on route to the agent. Derived
                                             						from: Call_Type_Real_Time.TotalCallsAbandTo5. |
| Abandoned Within Service Level | The
                                             						number of tasks abandoned before the service level timer expired during the
                                             						rolling five-minute interval. Derived
                                             						from: Call_Type_Real_Time.ServiceLevelAbandTo5. |
| Average Abandon | The
                                             						average time of abandoned calls for this call type during the rolling
                                             						five-minute interval, measured in HH:MM:SS (hours, minutes, seconds) format. This field
                                             						is a calculated field, derived from: Call_Type_Real_Time.CallDelayAbandTimeTo5
                                             						/ Call_Type_Real_Time.TotalCallsAbandTo5. |

| Column
                                             						(Field) | Description |
|---|---|
| Call Type Name | The
                                             						enterprise name for the call type. Derived
                                             						from: Call_Type.EnterpriseName. |
| Avg Speed of Answer 5 | Average
                                             						Speed of Answer during the rolling five-minute interval. The total Answer Time
                                             						for all tasks of the call type divided by the number of tasks of this type
                                             						answered during the current five-minute interval. This field
                                             						is a calculated field, derived from: (Call_Type_Real_Time.AnswerWaitTimeTo5 /
                                             						Call_Type_Real_Time.CallsAnsweredTo5). |
| VRU not Queued Now | The number
                                             						of tasks in Run VRUScript or Wait state. This represents the number of tasks at
                                             						VRU prompting or self service. This field
                                             						is a calculated field, derived from: Call_Type_Real_Time.CallsAtVRUNow -
                                             						Call_Type_Real_Time.RouterCallsQNow. |
| Queued Now | The number
                                             						of tasks currently in the queue. Derived
                                             						from: Call_Type_Real_Time.RouterCallsQNow. |
| CCE Agent
                                             						Now | The number of tasks that have been routed to the Unified CCE agents but are not yet ended. This column is incremented when the call is answered and decremented when the call ends, after
                                             wrap up is complete, if applicable. Derived
                                             						from: Call_Type_Real_Time.CallsAtAgentNow. |
| Longest
                                             						Queued | The time
                                             						spent in queue for the longest currently queued task, measured in HH:MM:SS
                                             						(hours, minutes, seconds) format. This field
                                             						is a calculated field, determined by subtracting the time the task entered the
                                             						queue (Derived from: Call_Type_Real_Time.RouterLongestCallQ) from the current
                                             						time. |
| Service
                                             						Level | The Unified ICM/Unified CCE service level for the rolling five-minute interval. Derived
                                             						from: Call_Type_Interval.ServiceLevelTo5. |
| Handled5 | The number
                                             						of calls of this call type handled for the call type ending during the rolling
                                             						five-minute interval. Derived
                                             						from: Call_Type_Real_Time.CallsHandledTo5. |
| Aband5 | The number
                                             						of tasks abandoned at the IVR during the rolling five-minute interval, while
                                             						offered to the agent and on route to the agent. Derived
                                             						from: Call_Type_Real_Time.TotalCallsAbandTo5. |
| Abandoned Within Service Level | The
                                             						number of tasks abandoned before the service level timer expired during the
                                             						rolling five-minute interval. Derived
                                             						from: Call_Type_Real_Time.ServiceLevelAbandTo5. |
| Average Abandon | The
                                             						average time of abandoned calls for this call type during the rolling
                                             						five-minute interval, measured in HH:MM:SS (hours, minutes, seconds) format. This field
                                             						is a calculated field, derived from: Call_Type_Real_Time.CallDelayAbandTimeTo5
                                             						/ Call_Type_Real_Time.TotalCallsAbandTo5. |

| Column
                                             						(Field) | Description |
|---|---|
| Enterprise Skill Group | The
                                             						enterprise skill group's enterprise name and ID. Derived
                                             						from: Enterprise_Skill_Group.EnterpriseName
                                             						(Enterprise_Skill_Group.EnterpriseSkillGroupID). |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Queued Now | The
                                             						number of calls currently queued to the skill group at the CallRouter and at
                                             						the local ACD queue. This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Queued Now (ICM) is Available by default. Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow. |
| Longest Queued | The
                                             						longest queued task on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format. This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Longest Task Q (ICM) is Available by default. Derived
                                             						from: Skill_Group_Real_Time.RouterLongestCallInQ. |
| ASA5 | The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the skill group during the rolling five minute interval. Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5. |
| Handled | The
                                             						number of tasks that were handled during the rolling five minute interval. Derived
                                             						from: Skill_Group_Real_Time.CallsHandledTo5. |
| Avg Handle Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it has taken during the
                                             						rolling five minute interval to handle a task. Derived
                                             						from: Skill_Group_Real_Time.HandleCallsTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5. |
| Log On | The
                                             						number of agents that are currently logged in to the skill group. This count is
                                             						updated each time an agent logs in and each time an agent logs out. Derived
                                             						from: Skill_Group_Real_Time.LoggedOn. |
| Not
                                             						Ready | The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged in but are neither involved in any call
                                             						handling activity nor available to handle a call. Derived
                                             						from: Skill_Group_Real_Time.NotReady. |
| Not
                                             						Active | The
                                             						number of agents in the skill group who are currently not working on a task
                                             						associated with the skill group. Derived
                                             						from: Skill_Group_Real_Time.Avail. |
| Active
                                             						In | The
                                             						number of agents in the skill group currently working on inbound tasks. Derived
                                             						from: Skill_Group_Real_Time.TalkingIn. |
| Active
                                             						Out | The
                                             						number of agents in the skill group currently talking on outbound calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingOut. |
| Active
                                             						Other | The
                                             						number of agents in the skill group currently talking on internal (neither
                                             						inbound nor outbound) calls. Examples
                                             						of other calls include agent-to-agent transfers and supervisor calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingOther. |
| Active
                                             						Auto Out | The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingAutoOut. |
| Active
                                             						Preview | The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingPreview. |
| Active
                                             						Reservation | The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingReserve. |
| Avg Active Time | The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval. Derived
                                             						from: (Skill_Group_Real_Time.HandledCallsTalkTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5). |
| Wrap Up | The
                                             						number of agents currently in wrap-up state for this skill group. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state. Derived
                                             						from: Skill_Group_Real_Time.WorkReady + Skill_Group_Real_Time.WorkNotReady. |
| Hold | The
                                             						number of agents that have all active calls on hold or whose state to the skill
                                             						group is Paused. The agent is not in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold. Derived
                                             						from: Skill_Group_Real_Time.Hold. |
| Reserved | The number
                                             						of agents for the skill group currently in the Reserved state. Derived
                                             						from: Skill_Group_Real_Time.ReservedAgents. |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy
                                             						Other is a state in which the agent is handling calls assigned to other skill
                                             						groups during the interval. For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged in to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state. Derived
                                             						from: Skill_Group_Real_Time.BusyOther. |
| %
                                             						Utilization | The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready. Derived
                                             						from: Skill_Group_Real_Time.PercentUtilizationTo5. |

| Column
                                             						(Field) | Description |
|---|---|
| Enterprise Skill Group | The
                                             						enterprise skill group's enterprise name and ID. Derived
                                             						from: Enterprise_Skill_Group.EnterpriseName
                                             						(Enterprise_Skill_Group.EnterpriseSkillGroupID). |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Queued Now | The
                                             						number of calls currently queued to the skill group at the CallRouter and at
                                             						the local ACD queue. This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Queued Now (ICM) is Available by default. Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow. |
| Longest Queued | The
                                             						longest queued task on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format. This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Longest Task Q (ICM) is Available by default. Derived
                                             						from: Skill_Group_Real_Time.RouterLongestCallInQ. |
| ASA5 | The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the skill group during the rolling five minute interval. Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5. |
| Handled | The
                                             						number of tasks that were handled during the rolling five minute interval. Derived
                                             						from: Skill_Group_Real_Time.CallsHandledTo5. |
| Avg Handle Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it has taken during the
                                             						rolling five minute interval to handle a task. Derived
                                             						from: Skill_Group_Real_Time.HandleCallsTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5. |
| Log On | The
                                             						number of agents that are currently logged in to the skill group. This count is
                                             						updated each time an agent logs in and each time an agent logs out. Derived
                                             						from: Skill_Group_Real_Time.LoggedOn. |
| Not
                                             						Ready | The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged in but are neither involved in any call
                                             						handling activity nor available to handle a call. Derived
                                             						from: Skill_Group_Real_Time.NotReady. |
| Not
                                             						Active | The
                                             						number of agents in the skill group who are currently not working on a task
                                             						associated with the skill group. Derived
                                             						from: Skill_Group_Real_Time.Avail. |
| Active
                                             						In | The
                                             						number of agents in the skill group currently working on inbound tasks. Derived
                                             						from: Skill_Group_Real_Time.TalkingIn. |
| Active
                                             						Out | The
                                             						number of agents in the skill group currently talking on outbound calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingOut. |
| Active
                                             						Other | The
                                             						number of agents in the skill group currently talking on internal (neither
                                             						inbound nor outbound) calls. Examples
                                             						of other calls include agent-to-agent transfers and supervisor calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingOther. |
| Active
                                             						Auto Out | The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingAutoOut. |
| Active
                                             						Preview | The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingPreview. |
| Active
                                             						Reservation | The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingReserve. |
| Avg Active Time | The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval. Derived
                                             						from: (Skill_Group_Real_Time.HandledCallsTalkTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5). |
| Wrap Up | The
                                             						number of agents currently in wrap-up state for this skill group. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state. Derived
                                             						from: Skill_Group_Real_Time.WorkReady + Skill_Group_Real_Time.WorkNotReady. |
| Hold | The
                                             						number of agents that have all active calls on hold or whose state to the skill
                                             						group is Paused. The agent is not in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold. Derived
                                             						from: Skill_Group_Real_Time.Hold. |
| Reserved | The number
                                             						of agents for the skill group currently in the Reserved state. Derived
                                             						from: Skill_Group_Real_Time.ReservedAgents. |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy
                                             						Other is a state in which the agent is handling calls assigned to other skill
                                             						groups during the interval. For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged in to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state. Derived
                                             						from: Skill_Group_Real_Time.BusyOther. |
| %
                                             						Utilization | The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready. Derived
                                             						from: Skill_Group_Real_Time.PercentUtilizationTo5. |

| Column
                                             						(Field) | Description |
|---|---|
| Service
                                             						Name | The
                                             						enterprise name of the peripheral service. Derived
                                             						from: Service.EnterpriseName. |
| In
                                             						Progress | The number of
                                             						inbound and outbound calls currently that were previously offered (for example,
                                             						calls being played, an announcement, queued calls, or connected calls) and are
                                             						currently being handled for the service. Derived
                                             						from: Service_Real_Time.CallsInProgress. |
| Queued Now | The tasks
                                             						in queue associated with the service now at the peripheral. Derived
                                             						from: Service_Real_Time.CallsQNow. |
| Abandoned in Queue 5 | The number of tasks associated with the service that were abandoned while
                                             						in queue or ringing during the rolling five-minute interval. An abandoned task is one in which the caller ended the call before being connected with an agent. If the caller ends the call
                                             almost immediately, you might not want to count that as an abandoned task. When configuring each peripheral, you can specify
                                             the minimum length of an abandoned task. Derived
                                             						from: Service_Real_Time.CallsAbandQTo5. |
| Average Delay in Queue Aban5 | The
                                             						average delay time of tasks associated with the service that were abandoned in
                                             						the service queue during the rolling five-minute interval. This value is
                                             						calculated as follows:DelayQAbandTimeTo5 / CallsAbandQTo5. Derived
                                             						from: Service_Real_Time.AvgDelayQAbandTo5. |
| Average Speed of Answer to 5 | The
                                             						average answer wait time for tasks associated with the service during the
                                             						rolling five-minute interval: AnswerWaitTimeTo5 / CallsOfferedTo5. Answer
                                             						wait time is the elapsed time from when the task is offered at the peripheral
                                             						to when it is answered. This includes all DelayTime, LocalQTime, and RingTime
                                             						associated with the task. Derived
                                             						from: Service_Real_Time.AvgSpeedAnswerTo5. |
| Average Handle Time to 5 | The
                                             						average handle time in HH:MM:SS (hours, minutes, seconds) for tasks associated
                                             						with the service during the rolling five-minute interval. The value is
                                             						calculated as follows: HandleTimeTo5 / CallsHandledTo5. Derived
                                             						from: Service_Real_Time.AvgHandleTimeTo5. |
| Longest Available Agent | The time
                                             						that the longest available agent associated with the service became available. Derived
                                             						from: Service_Real_Time.LongestAvailAgent. |
| Longest Task in Queue | The time
                                             						that the longest call in the queue for the service was put there. Derived
                                             						from: Service_Real_Time.LongestCallQ. |
| Flow In 5 | The number
                                             						of calls the peripheral overflowed into this service during the rolling
                                             						five-minute interval. Derived
                                             						from: Service_Real_Time.OverflowInTo5. |
| Flow Out 5 | The number
                                             						of calls overflowed out of this service during the rolling five-minute
                                             						interval. Derived
                                             						from: Service_Real_Time.OverflowOutTo5. |
| Service Level to 5 | The
                                             						Enterprise service level for the service during the rolling five-minute
                                             						interval. Derived
                                             						from: Service_Real_Time.ServiceLevelTo5. |
| Service Level to 5 Aban | The number
                                             						of calls to the service abandoned within the service level threshold during the
                                             						rolling five-minute interval. Derived
                                             						from: Service_Real_Time.ServiceLevelAbandTo5. |
| Service Level to 5 Tasks | The number of calls to the service answered within the Unified ICM service level during the rolling five-minute interval. Derived
                                             						from: Service_Real_Time.ServiceLevelCallsTo5. |

| Column
                                             						(Field) | Description |
|---|---|
| Service
                                             						Name | The
                                             						enterprise name of the peripheral service. Derived
                                             						from: Service.EnterpriseName. |
| In
                                             						Progress | The number of
                                             						inbound and outbound calls currently that were previously offered (for example,
                                             						calls being played, an announcement, queued calls, or connected calls) and are
                                             						currently being handled for the service. Derived
                                             						from: Service_Real_Time.CallsInProgress. |
| Queued Now | The tasks
                                             						in queue associated with the service now at the peripheral. Derived
                                             						from: Service_Real_Time.CallsQNow. |
| Abandoned in Queue 5 | The number of tasks associated with the service that were abandoned while
                                             						in queue or ringing during the rolling five-minute interval. An abandoned task is one in which the caller ended the call before being connected with an agent. If the caller ends the call
                                             almost immediately, you might not want to count that as an abandoned task. When configuring each peripheral, you can specify
                                             the minimum length of an abandoned task. Derived
                                             						from: Service_Real_Time.CallsAbandQTo5. |
| Average Delay in Queue Aban5 | The
                                             						average delay time of tasks associated with the service that were abandoned in
                                             						the service queue during the rolling five-minute interval. This value is
                                             						calculated as follows:DelayQAbandTimeTo5 / CallsAbandQTo5. Derived
                                             						from: Service_Real_Time.AvgDelayQAbandTo5. |
| Average Speed of Answer to 5 | The
                                             						average answer wait time for tasks associated with the service during the
                                             						rolling five-minute interval: AnswerWaitTimeTo5 / CallsOfferedTo5. Answer
                                             						wait time is the elapsed time from when the task is offered at the peripheral
                                             						to when it is answered. This includes all DelayTime, LocalQTime, and RingTime
                                             						associated with the task. Derived
                                             						from: Service_Real_Time.AvgSpeedAnswerTo5. |
| Average Handle Time to 5 | The
                                             						average handle time in HH:MM:SS (hours, minutes, seconds) for tasks associated
                                             						with the service during the rolling five-minute interval. The value is
                                             						calculated as follows: HandleTimeTo5 / CallsHandledTo5. Derived
                                             						from: Service_Real_Time.AvgHandleTimeTo5. |
| Longest Available Agent | The time
                                             						that the longest available agent associated with the service became available. Derived
                                             						from: Service_Real_Time.LongestAvailAgent. |
| Longest Task in Queue | The time
                                             						that the longest call in the queue for the service was put there. Derived
                                             						from: Service_Real_Time.LongestCallQ. |
| Flow In 5 | The number
                                             						of calls the peripheral overflowed into this service during the rolling
                                             						five-minute interval. Derived
                                             						from: Service_Real_Time.OverflowInTo5. |
| Flow Out 5 | The number
                                             						of calls overflowed out of this service during the rolling five-minute
                                             						interval. Derived
                                             						from: Service_Real_Time.OverflowOutTo5. |
| Service Level to 5 | The
                                             						Enterprise service level for the service during the rolling five-minute
                                             						interval. Derived
                                             						from: Service_Real_Time.ServiceLevelTo5. |
| Service Level to 5 Aban | The number
                                             						of calls to the service abandoned within the service level threshold during the
                                             						rolling five-minute interval. Derived
                                             						from: Service_Real_Time.ServiceLevelAbandTo5. |
| Service Level to 5 Tasks | The number of calls to the service answered within the Unified ICM service level during the rolling five-minute interval. Derived
                                             						from: Service_Real_Time.ServiceLevelCallsTo5. |

| Note | If there are
                                          			 primary or secondary skill groups defined for the base skill group, then the
                                          			 base skill group is not shown. |
|---|---|

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The
                                             						enterprise name of the skill group and its skill target ID. Derived
                                             						from: Skill_Group.EnterpriseName and Skill_Group.SkillTargetID. |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Queued Now | The number of calls currently queued to the skill group at the Unified CCE (Network Queue) and at the local ACD queue . This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Queued Now (ICM) is Available by default. Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow. |
| Longest Queued | The
                                             						longest queued task on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format. This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Longest Task Q (ICM) is Available by default. Derived
                                             						from: Skill_Group_Real_Time.RouterLongestCallInQ. |
| Average Speed of Answer to 5 | The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the skill group during the rolling five minute interval. Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5. |
| Answered Within Service Level | The
                                             						Average Speed of Answer during the rolling five minute interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds) format for the skill group. Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5. |
| Abandoned Within Service Level | The count of calls that are answered within the skill group service level threshold during the rolling five minute interval. Derived
                                             						from:  Skill_Group_Real_Time.ServiceLevelCallsTo5. |
| Handled | The
                                             						number of tasks that were handled during the rolling five-minute interval. Derived
                                             						from: Skill_Group_Real_Time.CallsHandledTo5. |
| Average Handle Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it takes during the rolling
                                             						five-minute interval to handle a task. Derived
                                             						from: Skill_Group_Real_Time.HandleCallsTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5. |
| Log On | The
                                             						number of agents that are currently logged in to the skill group. This count is
                                             						updated each time an agent logs in and each time an agent logs out. Derived
                                             						from: Skill_Group_Real_Time.LoggedOn. |
| Not
                                             						Ready | The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged on but are neither involved in any call
                                             						handling activity nor available to handle a call. Derived
                                             						from: Skill_Group_Real_Time.NotReady. |
| Not
                                             						Active | The
                                             						number of agents in the skill group who are currently not working on a task
                                             						associated with the skill group. Derived
                                             						from: Skill_Group_Real_Time.Avail. |
| Active
                                             						In | The
                                             						number of agents in the skill group currently working on inbound tasks. Derived
                                             						from: Skill_Group_Real_Time.TalkingIn. |
| Active
                                             						Out | The
                                             						number of agents in the skill group currently talking on outbound calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingOut. |
| Active
                                             						Other | The
                                             						number of agents in the skill group currently talking on internal (neither
                                             						inbound nor outbound) calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingOther. |
| Active
                                             						Auto Out | The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingAutoOut. |
| Active
                                             						Preview | The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingPreview. |
| Active
                                             						Reservation | The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingReserve. |
| Avg Active Time | The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval. Derived
                                             						from: (Skill_Group_Real_Time.HandledCallsTalkTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5). |
| Wrap Up | The
                                             						number of agents currently in wrap-up state for this skill group. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state. Derived
                                             						from: Skill_Group_Real_Time.WorkReady + Skill_Group_Real_Time.WorkNotReady. |
| Hold | The
                                             						number of agents that have all active calls on hold or whose state to the skill
                                             						group is Paused. The agent is not in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold. Derived
                                             						from: Skill_Group_Real_Time.Hold. |
| Reserved | The
                                             						number of agents for the skill group currently in the Reserved state. Reserved
                                             						is a state in which an agent is awaiting a call and is unavailable to receive
                                             						any incoming calls. This state applies only to agents on Northern Meridian
                                             						ACDs. Derived
                                             						from: Skill_Group_Real_Time.ReservedAgents. |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy
                                             						Other is a state in which the agent is handling calls assigned to other skill
                                             						groups during the interval. For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged in to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state. Derived
                                             						from: Skill_Group_Real_Time.BusyOther. |
| %
                                             						Utilization | The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready. Derived from: Skill_Group_Real_Time.PercentUtilizationTo5. |

| Column
                                             						(Field) | Description |
|---|---|
| Skill Group | The
                                             						enterprise name of the skill group and its skill target ID. Derived
                                             						from: Skill_Group.EnterpriseName and Skill_Group.SkillTargetID. |
| Media | The enterprise name of the Media Routing Domain associated with the skill group. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Queued Now | The number of calls currently queued to the skill group at the Unified CCE (Network Queue) and at the local ACD queue . This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Queued Now (ICM) is Available by default. Derived
                                             						from: Skill_Group_Real_Time.RouterCallsQNow. |
| Longest Queued | The
                                             						longest queued task on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format. This field is Current by default and is applicable only to the Unified CCE . The equivalent field for the Unified CCE is named Longest Task Q (ICM) is Available by default. Derived
                                             						from: Skill_Group_Real_Time.RouterLongestCallInQ. |
| Average Speed of Answer to 5 | The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the skill group during the rolling five minute interval. Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5. |
| Answered Within Service Level | The
                                             						Average Speed of Answer during the rolling five minute interval, measured in
                                             						HH:MM:SS (hours, minutes, seconds) format for the skill group. Derived
                                             						from: Skill_Group_Real_Time.AnswerWaitTimeTo5 /
                                             						Skill_Group_Real_Time.CallsAnsweredTo5. |
| Abandoned Within Service Level | The count of calls that are answered within the skill group service level threshold during the rolling five minute interval. Derived
                                             						from:  Skill_Group_Real_Time.ServiceLevelCallsTo5. |
| Handled | The
                                             						number of tasks that were handled during the rolling five-minute interval. Derived
                                             						from: Skill_Group_Real_Time.CallsHandledTo5. |
| Average Handle Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it takes during the rolling
                                             						five-minute interval to handle a task. Derived
                                             						from: Skill_Group_Real_Time.HandleCallsTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5. |
| Log On | The
                                             						number of agents that are currently logged in to the skill group. This count is
                                             						updated each time an agent logs in and each time an agent logs out. Derived
                                             						from: Skill_Group_Real_Time.LoggedOn. |
| Not
                                             						Ready | The
                                             						number of agents in the Not Ready state for the skill group. Not Ready is a
                                             						state in which agents are logged on but are neither involved in any call
                                             						handling activity nor available to handle a call. Derived
                                             						from: Skill_Group_Real_Time.NotReady. |
| Not
                                             						Active | The
                                             						number of agents in the skill group who are currently not working on a task
                                             						associated with the skill group. Derived
                                             						from: Skill_Group_Real_Time.Avail. |
| Active
                                             						In | The
                                             						number of agents in the skill group currently working on inbound tasks. Derived
                                             						from: Skill_Group_Real_Time.TalkingIn. |
| Active
                                             						Out | The
                                             						number of agents in the skill group currently talking on outbound calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingOut. |
| Active
                                             						Other | The
                                             						number of agents in the skill group currently talking on internal (neither
                                             						inbound nor outbound) calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingOther. |
| Active
                                             						Auto Out | The
                                             						number of agents in the skill group currently talking on AutoOut (predictive)
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingAutoOut. |
| Active
                                             						Preview | The
                                             						number of agents in the skill group currently talking on outbound Preview
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingPreview. |
| Active
                                             						Reservation | The
                                             						number of agents in the skill group currently talking on agent reservation
                                             						calls. Derived
                                             						from: Skill_Group_Real_Time.TalkingReserve. |
| Avg Active Time | The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval. Derived
                                             						from: (Skill_Group_Real_Time.HandledCallsTalkTimeTo5 /
                                             						Skill_Group_Real_Time.CallsHandledTo5). |
| Wrap Up | The
                                             						number of agents currently in wrap-up state for this skill group. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state. Derived
                                             						from: Skill_Group_Real_Time.WorkReady + Skill_Group_Real_Time.WorkNotReady. |
| Hold | The
                                             						number of agents that have all active calls on hold or whose state to the skill
                                             						group is Paused. The agent is not in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold. Derived
                                             						from: Skill_Group_Real_Time.Hold. |
| Reserved | The
                                             						number of agents for the skill group currently in the Reserved state. Reserved
                                             						is a state in which an agent is awaiting a call and is unavailable to receive
                                             						any incoming calls. This state applies only to agents on Northern Meridian
                                             						ACDs. Derived
                                             						from: Skill_Group_Real_Time.ReservedAgents. |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy
                                             						Other is a state in which the agent is handling calls assigned to other skill
                                             						groups during the interval. For
                                             						example, an agent might be talking on an inbound call in one skill group while
                                             						simultaneously logged in to and ready to accept calls from other skill groups.
                                             						The agent can be active (talking on or handling calls) in only one skill group
                                             						at a time. Therefore, while active in one skill group, for the other skill
                                             						group the agent is considered to be in the Busy Other state. Derived
                                             						from: Skill_Group_Real_Time.BusyOther. |
| %
                                             						Utilization | The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready. Derived from: Skill_Group_Real_Time.PercentUtilizationTo5. |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the precision queue. Derived
                                             						from: Precision_Queue.EnterpriseName. |
| Media | The enterprise name of the Media Routing Domain associated with the precision queue. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. Derived from: Attribute.EnterpriseName |
| Queued
                                             						Now | The
                                             						number of calls currently queued to the precision queue. Derived
                                             						from: Precision_Q_Real_Time.CallsQNow. |
| Longest Queued | The
                                             						longest queued call on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format. Derived
                                             						from: Precision_Q_Real_Time.LongestCallInQ |
| Avg Speed of Answer 5 | The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the precision queue during the rolling five-minute interval. Derived
                                             						from: Precision_Q_Real_Time.AnswerWaitTimeTo5/
                                             						Precision_Q_Real_Time.CallsAnsweredTo5. |
| Answered Within Service Level | The
                                             						count of calls that are answered within the precision queue service level
                                             						threshold during the rolling five-minute interval. Derived
                                             						from: Precision_Q_Real_Time.ServiceLevelCallsAnsTo5 |
| Abandon Within Service Level | The
                                             						count of calls that are abandoned within the precision queue service level
                                             						threshold during the rolling five-minute interval. Derived
                                             						from: Precision_Q_Real_Time.ServiceLevelCallsAbandTo5. |
| Handled | The
                                             						number of tasks that have been handled during the rolling five-minute interval. Derived
                                             						from: Precision_Q_Real_Time.CallsHandledTo5. |
| Avg Handle Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it takes during the rolling
                                             						five-minute interval to handle a task. Derived
                                             						from: Precision_Q_Real_Time.HandleCallsTimeTo5 /
                                             						Precision_Q_Real_Time.CallsHandledTo5. |
| Logged On | The
                                             						number of agents that are currently logged in to the precision queue. This
                                             						count is updated each time an agent logs on and each time an agent logs off. Derived
                                             						from: Precision_Q_Real_Time.LoggedOn. |
| Not
                                             						Ready | The
                                             						number of agents in the Not Ready state for the precision queue. Not Ready is a
                                             						state in which agents are logged in but are neither involved in any call
                                             						handling activity nor available to handle a call. Derived
                                             						from: Precision_Q_Real_Time.NotReady. |
| Not
                                             						Active | The
                                             						number of agents in the precision queue who are currently not working on a task
                                             						associated with the precision queue. Derived
                                             						from: Precision_Q_Real_Time.Avail. |
| Active
                                             						In | The
                                             						number of agents in the  precision queue currently working on inbound tasks. Derived
                                             						from:  Precision_Q_Real_Time.TalkingIn |
| Active
                                             						Other | The number of agents in the precision queue currently talking on international (neither inbound nor outbound) calls. Derived
                                             						from:  Precision_Q_Real_Time.TalkingOther |
| Avg Active Time | The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval. Derived
                                             						from: ( Precision_Q_Real_Time.HandledCallsTalkTimeTo5
                                             						/  Precision_Q_Real_Time.CallsHandledTo5) |
| Wrap
                                             						Up | The
                                             						number of agents currently in wrap-up state for this  precision queue. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state. Derived from:  Precision_Q_Real_Time.WorkReady +
                                             						 Precision_Q_Real_Time.WorkNotReady |
| Hold | The
                                             						number of agents that have all active calls on hold or whose state to the  precision queue is Paused. The agent is not
                                             in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold. Derived from:  Precision_Q_Real_Time.Hold |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy
                                             						Other is a state in which the agent is  handling calls assigned to other  precision queues during the interval. For
                                             						example, an agent might be talking on an inbound call in one  precision queue while
                                             						simultaneously logged on to and ready to accept calls from other  precision queues.
                                             						The agent can be active (talking on or handling calls) in only one  precision queue
                                             						at a time. Therefore, while active in one  precision queue, for the other  precision queue the agent is considered to
                                             be in the Busy Other state. Derived from:  Precision_Q_Real_Time.BusyOther |
| %
                                             						Utilization | The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready. Derived from: Skill_Group_Real_Time.PercentUtilizationTo5 |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the precision queue. Derived
                                             						from: Precision_Queue.EnterpriseName. |
| Media | The enterprise name of the Media Routing Domain associated with the precision queue. Media is derived from:
                                             				Media_Routing_Domain.EnterpriseName. |
| Attributes | The
                                             						attributes used in the precision queue definition. The report shows only those
                                             						attributes that are used. Derived from: Attribute.EnterpriseName |
| Queued
                                             						Now | The
                                             						number of calls currently queued to the precision queue. Derived
                                             						from: Precision_Q_Real_Time.CallsQNow. |
| Longest Queued | The
                                             						longest queued call on the routing media, measured in HH:MM:SS (hours, minutes,
                                             						seconds) format. Derived
                                             						from: Precision_Q_Real_Time.LongestCallInQ |
| Avg Speed of Answer 5 | The
                                             						Average Speed of Answer measured in HH:MM:SS (hours, minutes, seconds) format
                                             						for the precision queue during the rolling five-minute interval. Derived
                                             						from: Precision_Q_Real_Time.AnswerWaitTimeTo5/
                                             						Precision_Q_Real_Time.CallsAnsweredTo5. |
| Answered Within Service Level | The
                                             						count of calls that are answered within the precision queue service level
                                             						threshold during the rolling five-minute interval. Derived
                                             						from: Precision_Q_Real_Time.ServiceLevelCallsAnsTo5 |
| Abandon Within Service Level | The
                                             						count of calls that are abandoned within the precision queue service level
                                             						threshold during the rolling five-minute interval. Derived
                                             						from: Precision_Q_Real_Time.ServiceLevelCallsAbandTo5. |
| Handled | The
                                             						number of tasks that have been handled during the rolling five-minute interval. Derived
                                             						from: Precision_Q_Real_Time.CallsHandledTo5. |
| Avg Handle Time | The
                                             						average time in HH:MM:SS (hours, minutes, seconds) it takes during the rolling
                                             						five-minute interval to handle a task. Derived
                                             						from: Precision_Q_Real_Time.HandleCallsTimeTo5 /
                                             						Precision_Q_Real_Time.CallsHandledTo5. |
| Logged On | The
                                             						number of agents that are currently logged in to the precision queue. This
                                             						count is updated each time an agent logs on and each time an agent logs off. Derived
                                             						from: Precision_Q_Real_Time.LoggedOn. |
| Not
                                             						Ready | The
                                             						number of agents in the Not Ready state for the precision queue. Not Ready is a
                                             						state in which agents are logged in but are neither involved in any call
                                             						handling activity nor available to handle a call. Derived
                                             						from: Precision_Q_Real_Time.NotReady. |
| Not
                                             						Active | The
                                             						number of agents in the precision queue who are currently not working on a task
                                             						associated with the precision queue. Derived
                                             						from: Precision_Q_Real_Time.Avail. |
| Active
                                             						In | The
                                             						number of agents in the  precision queue currently working on inbound tasks. Derived
                                             						from:  Precision_Q_Real_Time.TalkingIn |
| Active
                                             						Other | The number of agents in the precision queue currently talking on international (neither inbound nor outbound) calls. Derived
                                             						from:  Precision_Q_Real_Time.TalkingOther |
| Avg Active Time | The
                                             						average talk or active time measured in HH:MM:SS (hours, minutes, seconds)
                                             						format during the rolling five-minute interval. Derived
                                             						from: ( Precision_Q_Real_Time.HandledCallsTalkTimeTo5
                                             						/  Precision_Q_Real_Time.CallsHandledTo5) |
| Wrap
                                             						Up | The
                                             						number of agents currently in wrap-up state for this  precision queue. Wrap Up is
                                             						call-related work performed by an agent after the call is over. An agent
                                             						performing wrap up is in either the Work Ready or Work Not Ready state. Derived from:  Precision_Q_Real_Time.WorkReady +
                                             						 Precision_Q_Real_Time.WorkNotReady |
| Hold | The
                                             						number of agents that have all active calls on hold or whose state to the  precision queue is Paused. The agent is not
                                             in the Hold state with one call on hold and
                                             						talking on another call (for example, a consultative call). The agent must have
                                             						all active calls on hold. Derived from:  Precision_Q_Real_Time.Hold |
| Busy
                                             						Other | The
                                             						number of agents currently in the BusyOther state. Busy
                                             						Other is a state in which the agent is  handling calls assigned to other  precision queues during the interval. For
                                             						example, an agent might be talking on an inbound call in one  precision queue while
                                             						simultaneously logged on to and ready to accept calls from other  precision queues.
                                             						The agent can be active (talking on or handling calls) in only one  precision queue
                                             						at a time. Therefore, while active in one  precision queue, for the other  precision queue the agent is considered to
                                             be in the Busy Other state. Derived from:  Precision_Q_Real_Time.BusyOther |
| %
                                             						Utilization | The
                                             						percentage of Ready time that agents in the skill group spent talking or doing
                                             						call work during the current five-minute interval. This is the percentage of
                                             						time agents spend working on calls versus the time agents were ready. Derived from: Skill_Group_Real_Time.PercentUtilizationTo5 |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the precision queue and its precision queue ID. Derived
                                             						from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID. |
| Step | An integer
                                             						that defines the unique row for a precision queue step. It is the primary key. Derived
                                             						from: Precision_Queue_Step.PrecisionQueueStepID. |
| Agents Logged On | The number of agents logged on for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.AgentsLoggedIn. |
| Agents Available | The
                                             						number of agents eligible and available for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.AgentsAvailable. |
| Longest Available Agent | The
                                             						length of time that the next agent to be selected has been available. Derived
                                             						from: Precision_Q_Step_Real_Time.NextAvailAgent. |
| In Queue | The number of tasks in queue for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.CallsInQueue. |
| Avg Queue Time | The
                                             						average length of queue time for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.AvgCallsInQueueTime. |
| Longest Queued | The time
                                             						stamp of the longest call in queue for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.LongestCallInQueue. |

| Column
                                             						(Field) | Description |
|---|---|
| Precision Queue | The
                                             						enterprise name of the precision queue and its precision queue ID. Derived
                                             						from: Precision_Queue.EnterpriseName and Precision_Queue.PrecisionQueueID. |
| Step | An integer
                                             						that defines the unique row for a precision queue step. It is the primary key. Derived
                                             						from: Precision_Queue_Step.PrecisionQueueStepID. |
| Agents Logged On | The number of agents logged on for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.AgentsLoggedIn. |
| Agents Available | The
                                             						number of agents eligible and available for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.AgentsAvailable. |
| Longest Available Agent | The
                                             						length of time that the next agent to be selected has been available. Derived
                                             						from: Precision_Q_Step_Real_Time.NextAvailAgent. |
| In Queue | The number of tasks in queue for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.CallsInQueue. |
| Avg Queue Time | The
                                             						average length of queue time for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.AvgCallsInQueueTime. |
| Longest Queued | The time
                                             						stamp of the longest call in queue for this precision queue step. Derived
                                             						from: Precision_Q_Step_Real_Time.LongestCallInQueue. |

| Columns
                                          						(Fields) | Description |
|---|---|
| Generic System
                                          						Information |
| Unified CCE Instance Name | An
                                          						enterprise name for the node. This name must be unique for all nodes in the
                                          						enterprise. Derived
                                          						from ICR_Instance.EnterpriseName. |
| Deployment Type | The Unified CCE deployment type. Derived from Congestion_Control.DeploymentType |
| DateTime | The
                                          						date and time of the selected row's data in YYYY/MM/DD ( year, month, date) and
                                          						HH:MM:SS (hour, minute, second) format. Derived
                                          						from System_Capacity_Real_Time.DateTime. |
| Congestion
                                          						Information |
| Current
                                          						Congestion Level | The
                                          						current congestion mode in the system: No Congestion = General operating mode with no congestion Level 1 = Congestion mode is level 1 Level 2 = Congestion mode is level 2 Level 3 = Congestion mode is level 3 The
                                          						threshold that has been set for this field: On
                                                							 No Congestion, the background color field is Green On
                                                							 Level 1, the background color field is Yellow On
                                                							 Level 2, the background color field is Yellow On
                                                							 Level 3, the background color field is Red Derived from
                                       					 System_Capacity_Real_Time.CurrentCongestionLevel |
| Current
                                          						Rejection Percentage | The call
                                          						reduction percentage based on the current congestion level: For Level 0, reduction percentage is 0 %. For Level 1, reduction percentage is 10 %. For Level 2, reduction percentage is 30 %. For Level 3, reduction percentage varies from 30% to 100%
                                                							 depending on the incoming call rate. Derived from
                                       					 System_Capacity_Real_Time.RejectionPercentage |
| Duration
                                          						Congested at Current Level | The
                                          						time that the system has been at the current congestion level, even if it is
                                          						Level 0 (No Congestion.) Measured in HH:MM:SS (hours, minutes, seconds) format. This
                                          						field is a calculated field derived from: DATEDIFF(minutes,
                                          						System_Capacity_Real_Time.DateTimeCurrentLevel, Controller_Time.NowTime). |
| Duration
                                          						Congested | The
                                          						time spent in congestion measured in HH:MM:SS (hours, minutes, seconds) format.
                                          						This value is 0 if the current congestion level is Level 0 (No Congestion). This
                                          						is a calculated field derived from: DATEDIFF(minutes,
                                          						System_Capacity_Real_Time.DateTimeCongested, Controller_Time.NowTime). |
| Level1
                                          						Onset CPS | Onset
                                          						Calls Per Second (CPS) determination for Congestion level 1. Derived from System_Capacity_Real_Time.Level1Onset |
| Level1
                                          						Abatement CPS | Abatement CPS determination for Congestion Level 1. Derived
                                          						from System_Capacity_Real_Time.Level1Abatement |
| Level1
                                          						Reduction | Call
                                          						rate reduction percentage for Congestion Level 1. Derived from System_Capacity_Real_Time.Level1Reduction |
| Level2
                                          						Onset CPS | Onset
                                          						CPS determination for Congestion level 2. Derived from System_Capacity_Real_Time.Level2Onset |
| Level2
                                          						Abatement CPS | Abatement CPS determination for Congestion level 2. Derived from System_Capacity_Real_Time.Level2Abatement |
| Level2
                                          						Reduction | Call
                                          						rate reduction percentage for Congestion Level 2. Derived from System_Capacity_Real_Time.Level2Reduction |
| Level3
                                          						Onset CPS | Onset
                                          						CPS determination for Congestion level 3. Derived from System_Capacity_Real_Time.Level3Onset |
| Level3
                                          						Abatement CPS | Abatement CPS determination for Congestion level 3. Derived from System_Capacity_Real_Time.Level3Abatement |
| Level3
                                          						Reduction | Call
                                          						rate reduction percentage for Congestion Level 3. Derived from System_Capacity_Real_Time.Level3Reduction |
| Capacity Information |
| Total
                                          						Agents Logged On | The
                                          						total number of agents logged in to the system. Derived from System_Capacity_Real_Time.TotalAgentsLoggedOn |
| Avg
                                          						Skills Per Agent | The
                                          						average number of skill groups associated per agent. Derived from System_Capacity_Real_Time.AverageSkillsPerAgent |
| Configured Capacity in CPS | Configured call per second capacity of the system. Derived from System_Capacity_Real_Time.ConfiguredCapacity |
| Adjusted Capacity in CPS | Adjusted Call per second capacity during run time. Derived from System_Capacity_Real_Time.AdjustedCapacity |
| Avg
                                          						CPS | Runtime weighed averaged call per second. Derived from System_Capacity_Real_Time.AverageCPS |