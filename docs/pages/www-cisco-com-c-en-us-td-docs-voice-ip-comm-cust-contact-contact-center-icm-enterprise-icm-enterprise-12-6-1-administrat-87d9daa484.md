---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-administrat-87d9daa484
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/administration/guide/ucce_b_administration-guide-for-cisco-unified_1261/ucce_b_administration-guide-for-cisco-unified_1261_chapter_01.html
retrieved_at: 2026-08-16T20:46:12.679248+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1)

Updated: May 14, 2021

Chapter: Cisco Unified Contact Center Enterprise Agents

## Chapter: Cisco Unified Contact Center Enterprise Agents

# Cisco Unified Contact Center Enterprise Agents

## Add Users to Local Security Group

Configuration users can configure Agents, Supervisors or Teams and perform other configurations only after they are added
                              to the UcceConfig group on the local machines.

You need to add the Unified CCE configuration users to the UcceConfig group in all the local Distributor machines.

Step 1

Click Server Manager > Tools > Computer Management .

Step 2

Select Local Users and Groups .

Step 3

Double-click Groups .

Step 4

Right-click UcceConfig . Select Properties .

Step 5

Click Add and enter the user name in the Edit the object names to select text box. Click Check Names to validate the user name.

Step 6

After the user name is successfully validated, click OK .

Step 7

Click Apply and OK in the Properties dialog box.

Step 8

Close the Computer Management and Server Manager windows.

## Agent Administration

This section provides information about the Unified CCE agent, including associating the agent with database records and
                           		agent desk settings.

### Agents

An agent is an individual who handles customer contact within your contact center. In a Unified CCE configuration, you can
                                 create two types of agents:

Agent type

Description

Voice-only
                                             						agents

Agents can receive telephone calls. You can also configure voice-only agents to receive non-voice requests such as chat and
                                             email.

Multichannel agents

Agents can receive voice calls and requests from other media. You can also configure multichannel agents to only receive non-voice requests such as chat and email.

### Database Records for
                           	 Voice-Only Agents

In the Unified ICM
                                 		  database, you must associate each agent with two database records.

Unified
                                             						ICM database record

Description

Person
                                             						record

Identifies
                                             						the individual. Person records must exist for all Unified CCE agents. Every
                                             						agent in your configuration must have a single Person record. You can then
                                             						associate this record with one or multiple Agent records, as described below.

Agent
                                             						record

Identifies
                                             						the agent working on a particular peripheral. There must be a one-to-one
                                             						correspondence between each Agent record and its associated peripheral.
                                             						However, in Unified CCE, if an agent is going to be working on several
                                             						peripherals, you can create several Agent records and associate these with the
                                             						same Person record. In this way, a single agent can work on several different
                                             						peripherals.

When you create an
                                 		  Agent record, you have the option of associating it with an existing Person
                                 		  record (select Select
                                    			 Person ). If you do not associate the Agent record with an existing
                                 		  Person record, a new Person record is automatically created when you create the
                                 		  agent.

Before you assign an agent as a supervisor, ensure that the agent has
                                 		  an Active Directory account.

### Database Records for Multichannel Agents

Unified CCE agents who use multichannel software are associated
                                 		  with three different database records:

The Person record in the ICM Unified CCE database

The Agent record in the ICM Unified CCE database

The Agent record in the database for the multichannel application

### Agent Desk Settings
                           	 Configuration

You must associate
                                 		  each Agent record with an agent desk
                                    			 setting. You use the agent desk settings configuration to associate a set
                                 		  of permissions or characteristics with specific agents. These settings are
                                 		  comparable to Class of Service settings on a PBX or ACD. Desk settings are
                                 		  associated with an agent when the agent is configured in the Unified ICM
                                 		  database. The desk settings are global in scope and you can apply them to any
                                 		  configured agent on any peripheral within an ICM Unified CCE configuration.

If desktop settings
                                 		  are not associated with a configured agent, the agent is assigned the
                                 		  peripheral default settings. The peripheral default settings depend on the
                                 		  default setting for the Generic CUCM PG the agent is logged in to.

#### Using Multichannel
                              	 Gadgets in Cisco Finesse

The Agent is logged
                                 		into both voice and multichannel Media Routing Domains in Cisco Finesse desktop
                                 		using the multichannel gadgets and the Agent is also configured for Logout
                                 		non-activity time in the Unified CCE Agent Desk Settings Configuration.

In this scenario, if the Agent is idle, which means the Agent is Not Ready in the Voice Media Routing Domain, the Peripheral
                                 Gateway logouts out the Agent from the voice Media Routing Domain after the configured Logout non-activity timer has elapsed.
                                 The Cisco Finesse desktop closes the Agent’s session and this terminates the Agent’s multichannel Media Routing Domain session,
                                 although the Agent may be actively working on a multichannel task.

As a result, the
                                 		Agent's multichannel Media Routing Domain state and tasks state both are
                                 		remained in the same state before the Agent logged out of voice Media Routing
                                 		Domain.

To work on the
                                 		multichannel Media Routing Domain tasks, agent has to login again to Cisco
                                 		Finesse desktop.

### Agent Teams and
                           	 Supervisors

You can organize
                                 		  Unified CCE voice agents into teams . A team
                                 		  is a collection of agents grouped for reporting purposes.

Unified ICM/CCE
                                 		  software allows you to group individual agents into agent teams that
                                 		  supervisors can manage. Agent teams are assigned to a specific peripheral, so
                                 		  you must assign all agents of a given team to the same Unified CM peripheral.

Unified ICM/CCE
                                 		  software lets you assign both Primary and Secondary supervisors to an
                                 		  individual team; set up your teams with both a Primary and a Secondary
                                 		  supervisor. This setup helps to accommodate Supervisor and Emergency assist
                                 		  scenarios.

Supervisors listed on the agents team list are able to view real-time statistics (using your reporting application). Supervisors
                                 can, for example, barge-in, intercept, silently monitor, and log out agents in the associated team.

For reporting
                                 		  purposes, you can report on agent teams and agents grouped into teams. Also,
                                 		  supervisors can run reports on their teams. (For more information about
                                 		  reporting, see Cisco Unified Contact Center Enterprise Reporting User Guide .)

Each team you set up must have an agent supervisor associated with it. You can then configure supervisory agent features,
                                 to allow the supervisor to improve monitor agent activity and assist agents on their team. When you create an agent supervisor,
                                 you must enter the following information for the supervisor:

Windows Domain
                                       				name to which the agent team belongs

Windows User ID
                                       				for the supervisor

Windows password
                                       				for the supervisor

When configuring
                                 		  agent teams, be aware of the following rules:

An agent can be
                                       				a member of only one agent team.

An agent team
                                       				can have only one Primary Supervisor.

A supervisor can
                                       				be a supervisor of any number of agent teams.

A supervisor for
                                       				an agent team can also be a member of that agent team.

All agents
                                       				belonging to an agent team and all supervisors for that agent team must be on
                                       				the same peripheral.

A supervisor
                                       				cannot be using the Windows administrator account when logging in as
                                       				supervisor.

For more information
                                 		  on team limits, see the appendix on system requirements in the Solution Design Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### Agent teams and
                           	 Multichannel Applications

You can group voice agents into teams using the Unified ICM/Unified CCE Administration User Interface. However, there is no
                              team feature in Enterprise Chat and
                                    						Email ; therefore, you cannot group Enterprise Chat and
                                    						Email agents into teams.

For more information about supervisory features, see CTI OS System Manager Guide for Cisco Unified ICM .

## Single-Line Versus Multi-line Behavior

The following table details single-line behavior versus multi-line
                              		  behavior.

Action

Single-line behavior

Multi-line behavior

Accept a routed call while call is on second line?

Yes

Yes, when Non ACD Line Impact is set no impact for the
                                          						deployment.

Supervisor Monitor using Unified CM-based silent monitor

Yes

Yes.

Non-ACD lines do not support Unified CM-based silent monitoring.

Call park

Supported on unmonitored second line

Not supported because all lines are monitored.

Join Across Lines (JAL)/Direct Transfer across Lines (DTAL)

Not supported

Use of JAL and DTAL phone features is deprecated. Do not use these features in new deployments.

Shared line

Supported on unmonitored line; no configuration limitations

Supported on non-ACD lines. Sign-in is allowed for only one agent on a shared extension when shared lines exist between multiple
                                          devices.However, one agent can have two phones that share a second common line. The agent cannot sign into both phones at
                                          the same time.

Unified CCE does not support shared lines for ACD lines.

Call Waiting / Busy trigger > 1

Supported with caveats. For more information, see the section Direct Agent Dialing in the Solution Design Guide for Cisco Unified Contact Center Enterprise https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

State Agent Login rejected if Busy trigger is not 1, and max calls is not 2 for each of the non-ACD lines.

Reporting on second line calls

Use CDRs in Unified CM

Termination Call Detail Records for call to or from an
                                          						agent's Non ACD line with an unmonitored device or another agent's Non ACD line
                                          						is reported with a Non ACD Peripheral Call Type. Reporting for all calls
                                          						on the Non ACD line is captured in the Agent Interval table for that
                                          						agent.

Number of configured lines on phone

No limit described (only monitoring one line)

Maximum of four lines. Agent login will be rejected. Config
                                          						Alert generated.

For more information about enabling the Cisco Round Table phones, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide . For more information about configuring the Cisco Round Table phones, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide and the Cisco Unified Communications Manager documentation.

| Step 1 | Click Server Manager > Tools > Computer Management . |
|---|---|
| Step 2 | Select Local Users and Groups . |
| Step 3 | Double-click Groups . |
| Step 4 | Right-click UcceConfig . Select Properties . |
| Step 5 | Click Add and enter the user name in the Edit the object names to select text box. Click Check Names to validate the user name. |
| Step 6 | After the user name is successfully validated, click OK . |
| Step 7 | Click Apply and OK in the Properties dialog box. |
| Step 8 | Close the Computer Management and Server Manager windows. |

| Agent type | Description |
|---|---|
| Voice-only
                                             						agents | Agents can receive telephone calls. You can also configure voice-only agents to receive non-voice requests such as chat and
                                             email. |
| Multichannel agents | Agents can receive voice calls and requests from other media. You can also configure multichannel agents to only receive non-voice requests such as chat and email. Note You
                                                      						must have Cisco multichannel software installed as part of your Unified CCE
                                                      						configuration to create multichannel agents. | Note | You
                                                      						must have Cisco multichannel software installed as part of your Unified CCE
                                                      						configuration to create multichannel agents. |
| Note | You
                                                      						must have Cisco multichannel software installed as part of your Unified CCE
                                                      						configuration to create multichannel agents. |

| Note | You
                                                      						must have Cisco multichannel software installed as part of your Unified CCE
                                                      						configuration to create multichannel agents. |
|---|---|

| Note | In most cases,
                                          		  the Cisco Unified Communications Manager (Unified CM) peripheral on the Generic
                                          		  CUCM peripheral gateway (PG), which is set up with your initial Unified CCE
                                          		  installation, tracks and records the state and activity of all voice and
                                          		  non-voice agents. You can configure a non-voice PG rather than a Unified CM PG
                                          		  to monitor state and activity of agents configured as non-voice agents.
                                          		  However, this is optional, and is not necessary if you have a Unified CM
                                          		  peripheral on the Generic CUCM PG. |
|---|---|

| Unified
                                             						ICM database record | Description |
|---|---|
| Person
                                             						record | Identifies
                                             						the individual. Person records must exist for all Unified CCE agents. Every
                                             						agent in your configuration must have a single Person record. You can then
                                             						associate this record with one or multiple Agent records, as described below. |
| Agent
                                             						record | Identifies
                                             						the agent working on a particular peripheral. There must be a one-to-one
                                             						correspondence between each Agent record and its associated peripheral.
                                             						However, in Unified CCE, if an agent is going to be working on several
                                             						peripherals, you can create several Agent records and associate these with the
                                             						same Person record. In this way, a single agent can work on several different
                                             						peripherals. |

| Note | Do not configure
                                          		Logout non-activity time in Unified CCE Agent Desk Settings configuration, if
                                          		you are using the Cisco Finesse desktop to login Agents in both voice and
                                          		multichannel gadgets as mentioned above. |
|---|---|

| Note | A single agent
                                          		  can belong to only one team. |
|---|---|

| Action | Single-line behavior | Multi-line behavior |
|---|---|---|
| Accept a routed call while call is on second line? | Yes | Yes, when Non ACD Line Impact is set no impact for the
                                          						deployment. |
| Supervisor Monitor using Unified CM-based silent monitor | Yes | Yes. Note Non-ACD lines do not support Unified CM-based silent monitoring. | Note | Non-ACD lines do not support Unified CM-based silent monitoring. |
| Note | Non-ACD lines do not support Unified CM-based silent monitoring. |
| Call park | Supported on unmonitored second line | Not supported because all lines are monitored. |
| Join Across Lines (JAL)/Direct Transfer across Lines (DTAL) | Not supported | Note Use of JAL and DTAL phone features is deprecated. Do not use these features in new deployments. | Note | Use of JAL and DTAL phone features is deprecated. Do not use these features in new deployments. |
| Note | Use of JAL and DTAL phone features is deprecated. Do not use these features in new deployments. |
| Shared line | Supported on unmonitored line; no configuration limitations | Supported on non-ACD lines. Sign-in is allowed for only one agent on a shared extension when shared lines exist between multiple
                                          devices.However, one agent can have two phones that share a second common line. The agent cannot sign into both phones at
                                          the same time. Unified CCE does not support shared lines for ACD lines. |
| Call Waiting / Busy trigger > 1 | Supported with caveats. For more information, see the section Direct Agent Dialing in the Solution Design Guide for Cisco Unified Contact Center Enterprise https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html | State Agent Login rejected if Busy trigger is not 1, and max calls is not 2 for each of the non-ACD lines. |
| Reporting on second line calls | Use CDRs in Unified CM | Termination Call Detail Records for call to or from an
                                          						agent's Non ACD line with an unmonitored device or another agent's Non ACD line
                                          						is reported with a Non ACD Peripheral Call Type. Reporting for all calls
                                          						on the Non ACD line is captured in the Agent Interval table for that
                                          						agent. |
| Number of configured lines on phone | No limit described (only monitoring one line) | Maximum of four lines. Agent login will be rejected. Config
                                          						Alert generated. |

| Note | Non-ACD lines do not support Unified CM-based silent monitoring. |
|---|---|

| Note | Use of JAL and DTAL phone features is deprecated. Do not use these features in new deployments. |
|---|---|