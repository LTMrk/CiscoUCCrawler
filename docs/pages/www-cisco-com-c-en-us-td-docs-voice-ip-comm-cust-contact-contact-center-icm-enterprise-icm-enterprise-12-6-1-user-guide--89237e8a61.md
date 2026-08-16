---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--89237e8a61
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/reporting-concepts-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/routing-in-unified-icm-deployments.html
retrieved_at: 2026-08-16T20:42:52.129946+00:00
---

Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

# Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

Updated: June 27, 2023

Chapter: Routing in Unified CCE Deployments

## Chapter: Routing in Unified CCE Deployments

# Routing in Unified CCE Deployments

## Different Cisco Unified CCE Deployments

Cisco Unified CCE reports help to monitor operational effectiveness, customer experience and contact center agent performance across your enterprise.

In order to effectively run your call center using the data provided by enterprise reports, it is important to understand
                              the different Cisco Unified CCE deployments.

The Peripheral Gateway component in a Unified CCE system is used to interface with peripherals at the different call centers in your enterprise.

The capabilities provided by the Unified CCE software when connected by a traditional TDM PG to a legacy TDM ACD differ from the capabilities provided by a Gateway PG
                              and a Unified CM PG.

Unified CCE can be deployed with different types of Peripheral Gateways to meet the call center needs in your enterprise.

## Deployments with Enterprise Routing

In this deployment, Unified CCE is configured with PGs that can connect to legacy ACDs using any of the supported TDM PGs (Aspect, Avaya, and so forth) as
                              well as the Unified CCE Gateway PGs.

When Unified CCE is configured with these types of PGs, the call treatment and queuing (ACD queuing) is provided by the ACD . That is, it is the ACD that controls the queuing and chooses the agent required to handle the call.

Unified CCE software is primarily used for intelligent call routing to sites and consolidated reporting for these ACDs. Optionally Unified CCE software can be used to provide initial call treatment and/or enterprise queuing (Enterprise queue). In this case the call
                              is routed to a site when an agent becomes available.

The ACD
                              offers the call to agents based on skill definitions on the ACD. If an agent is
                              not available, the ACD queues the call (in the ACD queue) and then directs the
                              call when an agent becomes available.

This illustration shows a Unified CCE system connected to two PGs for legacy ACDs and to a network VRU.

When calls are routed to an ACD, call treatment is provided on the
                                    ACD and the ACD controls the queuing.

Network VRU1 can
                                    be any Service Control VRU that can be used to provide initial call treatment
                                    and serve as the telephony platform for queuing calls across all call center
                                    ACDs. VRU1 can also be used for information gathering and
                                    self-service.

### Routing and
                           	 Scripting

In this deployment, Cisco Unified CCE software uses real-time reporting statistics gathered from the different peripherals (ACDs) to make routing decisions to
                                 route calls to the ACD at a site that is best suited to answer the call.

The following
                                 		  routing capabilities can be provided in this deployment.

Site-based Routing: Cisco Unified CCE software, using ICM routing capabilities, can use real time reporting statistics gathered from the different peripherals
                                       (ACDs) to make routing decisions to route calls to the ACD at a site that is best suited to answer the call.

Site selection
                                       				can be scripted using real time Service and Skill Group metrics provided by the
                                       				PG.

Several metrics
                                       				can be used to make the selection, such as Agent availability, CallsInProgress,
                                       				and a Minimum Expected Delay (MED) calculation.

Agent Level Routing: Not
                                       				Supported.

A typical script
                                 		  used to route calls in this deployment is illustrated and explained below.

The script is
                                       				associated with a Call Type. The example is shown for an enterprise that has
                                       				two sites (Boston and New York), each running a call center.

The call center at either site can provide call treatment to handle "Support" calls. "Support" is configured as a Service in Unified CCE .

Both call centers have agents trained to handle calls for either "Laptop Support" or "Server Support" . These categories are configured as Skill Groups in Unified CCE . The relationship of the Service to Skill Groups is configured as Service Members in Cisco Unified CCE .

The Boston call center has an Avaya ACD (peripheral) connected with an Avaya PG, and the New York call center has an Aspect
                                       ACD (peripheral) connected with the Aspect PG. Service and Skill Groups are configured for each peripheral in Unified CCE .

The script
                                 		  illustrated above shows an example of pre-routing and ACD queuing, processed as
                                 		  follows:

The script is
                                       				associated with a Call Type to route Support calls.

The script uses
                                       				caller entered digits (CED) to determine the skill group (Laptop Support or
                                       				Server Support) required to handle the call and/or the Service treatment
                                       				(Support) required by the caller.

The script uses
                                       				the LAA (longest available agent) node to look for an available agent across
                                       				the enterprise who can handle the call.

Unified CCE software routes the call to the call center site that has an available agent. The ACD at that site picks an agent and assigns
                                       the call.

If an agent is
                                       				not available, the script uses the MED (Minimum Expected Delay) node to select
                                       				a site that can handle the call with minimum delay.

Once the site
                                       				with the least expected wait time is selected, the call is routed to the ACD at
                                       				that site.

After the call
                                       				arrives on the ACD, call treatment is provided by the ACD. If an agent is
                                       				available, the ACD assigns the call to that agent.

If an agent is
                                       				not available, the ACD will queue the call to a skill group to wait for an
                                       				available agent.

### Reporting Considerations

This section is an overview of reporting categories to use to meet the
                                 		  reporting needs for your enterprise in this deployment.

Two key factors that affect reporting are:

Are you using ACD queuing or Enterprise queuing?

Are you using Translation Routing to route calls to the ACD?

The information is therefore presented based in the four scenarios described in this section.

#### Scenario One: Calls Are Queued on the ACD and Are Not Translation Routed

For Enterprise reporting, use the following report categories:

Use Enterprise Service reports for an enterprise view of reporting
                                       			 statistics for the application.

Use Enterprise Skill Group reports for enterprise view of reporting
                                       			 statistics routed to a particular skill group.

This table shows other report categories and the statistics they
                                 		provide.

Report Focus

Reporting Statistics Needed

Report Template

Key Statistics

Application

Before the call is routed to the ACD

Call Type

Number of calls routed

Number of calls received

Number of calls that encountered an error or received default
                                             					 treatment

After the call is routed to the ACD, calls queued on the ACD

Peripheral Service

Enterprise Service

Queue Statistics (ACD Queue)

Abandons

Service Level

RONA

After the call is answered by agent

Peripheral Service

Enterprise Service

ASA

Calls Handled

Avg. Handle Time

Transfers

Skill Group

For calls routed to skill groups and queued calls

Peripheral Skill Group

Enterprise Skill Group

Queue Statistics (ACD Queue)

Abandons

RONA

After the call is answered by agent

Peripheral Skill Group

Enterprise Skill Group

ASA

Calls Handled

Avg. Handle Time

Avg. Talk Time

Agent Info

Peripheral Skill Group

Enterprise Skill Group

FTEs and Percent Utilization

Agents

Agent Info

Agent

Agent's current state

Duration in state

Agents logged out

Calls Handled

Avg. Handle Time

Avg. Talk Time

#### Scenario Two: Calls Are Queued on the ACD and Are Translation Routed

The report categories to use are the same as for Scenario One (Calls Queued on the ACD that are not
                                    		  Translation Routed) , with the additional statistics available for Call
                                 		Type (cradle-to-grave):

Report Focus

Reporting Statistics Needed

Report Template

Key Statistics

Application

After the call is routed to the ACD, calls queued on the ACD

Call Type

Abandons

After the call is answered by agent

Call Type

ASA

Calls Handled

#### Scenario Three: Calls Are Enterprise Queued and Are Not Translation Routed

For Enterprise reporting, use the following report categories:

Use Enterprise Service reports for an enterprise view of some
                                       			 reporting statistics for the application.

Use Call Type and Enterprise Skill Group reports for an enterprise
                                       			 view of queued and abandon in queue statistics for the application and skill
                                       			 group respectively.

Use Enterprise Skill Group reports for enterprise view of reporting
                                       			 statistics when routed to a particular skill group.

Skill Group and Agent reporting are the same as for Scenario One (Calls Queued on the ACD that are not
                                    		  Translation Routed) .

This table shows other report categories and the statistics they
                                 		provide.

Report Focus

Reporting Statistics Needed

Report Template

Key Statistics

Application

Before the call is routed to the ACD, queued in the enterprise

Call Type

Number of calls routed

Number of calls received

Number of calls that encountered an error

Enterprise Queue Statistics and Abandon in Enterprise Queue

After the call is routed to ACD

Peripheral Service

Enterprise Service

Abandons

RONA

After the call is answered by the agent

Peripheral Service

Enterprise Service

Calls Handled

Avg Handled Time

Transfers

#### Scenario Four: Calls Are Enterprise Queued and Are Translation Routed

For Enterprise reporting, use the following report categories:

Use Call Type reports for enterprise view of reporting statistics
                                       			 for the application.

Use Call Type and Enterprise Skill Group reports for enterprise view
                                       			 of queued and abandon in queue statistics for the application and skill group
                                       			 respectively.

Use Enterprise Skill Group reports for enterprise view of reporting
                                       			 statistics when routed to a particular skill group.

Skill Group and Agent reporting are the same as for Scenario One (Calls Queued on the ACD that are not
                                    		  Translation Routed) .

This table shows other report categories and the statistics they
                                 		provide.

Report Focus

Reporting Statistics Needed

Report Template

Key Statistics

Application

Before the call is routed to the ACD, queued in the enterprise

Call Type

Number of calls routed

Number of calls received

Number of calls that encountered an error

Queue Statistics and Abandon in Queue

After the call is routed to the ACD

Call Type

Abandons

Service Level

After the call is answered by agent

Call Type

Calls Handled

Avg Handled Time

ASA

## Deployments with Hybrid Routing

In this deployment, Unified CCE includes both TDM PGs for Enterprise Routing to legacy ACDs and Cisco Call Manager PGs to provide the Agent Routing Integration
                              (ARI) to an ACD/PBX such as Avaya.

### Routing and Scripting

The manner in which you configure and script your Unified CCE system in this deployment greatly affects the accuracy and usefulness of your reporting metrics. This section assumes that
                                 calls are shared and routed across call centers for the application and are managed the same way.

Follow these guidelines for configuring and scripting Unified CCE to ensure that your reports display correct and relevant metrics for your "hybrid" contact center implementation.

Guidelines:

Ensure all calls are routed by Unified CCE software.

Deploy a Service Control VRU to provide treatment and to queue
                                       				calls in the enterprise while waiting for an available agent in a skill group.

In other words, queue calls to skill groups in Unified CCE (Enterprise queuing) for all call centers. Avoid using ACD queues.

For legacy ACDs where Unified CCE software is used for Enterprise Routing, consider the following:

Ensure all calls are routed by Unified CCE software.

Use Translation Routes for routing calls to the legacy ACD.
                                             					 Always use translation routing when routing calls between ACDs.

Once the call is routed by Unified CCE and is terminated on the legacy ACD, make sure no treatment occurs at the ACD.

Avoid having agents transfer calls directly to other agent stations or agent IDs. Instead, use post routing capabilities to
                                             have Unified CCE provide treatment and queuing for transferred calls.

Avoid handling Redirection on No Answer (RONA) situations on the ACD. Instead use post routing capabilities to have the RONA
                                             calls routed by Unified CCE .

Plan for Call Type Reporting. To run this type of reporting:

Configure a separate call type for each type of treatment
                                             					 offered. For example: Create a separate call type for treating Support calls
                                             					 and Sales calls across all ACDs in your call centers.

If you want to separate Information Gathering VRU metrics from
                                             					 queue metrics, configure a separate call type for queuing.

Configure a separate call type associated with Redirection on
                                             					 No Answer situations. This enables you to direct calls that Ring No Answer to a
                                             					 routing script designed for this situation. This also enables you to use Call
                                             					 Type reports to report on this Redirection on No Answer and to see how calls
                                             					 that redirect on no answer are eventually handled.

Configure a separate call type associated with call transfers.
                                             					 This enables you to direct the transfer to a different routing script.

Create a custom formula using skill group metrics for site selection based on expected delay. This is required as the predefined
                                       MED (Minimum Expected Delay) calculation provided by Unified CCE scripts is not applicable for Agent Level Routing configurations.

Configure Enterprise Skill Groups for Enterprise Skill Group
                                       				reporting. Avoid grouping skill groups from the same peripheral into an
                                       				Enterprise Skill Group.

A typical ICM script used to route calls in this deployment is shown
                                 		  below.

In this example:

The enterprise has two sites (Boston and New York), each
                                       				running a call center.

A Call Type is defined that is associated with the routing script.
                                       				This Call Type is used to define the treatment provided by the call centers.

The call treatment to handle "Support" calls is provided by Unified CCE software through the call type and script association.

The call center at each site has agents who are skilled to handle
                                       				calls for either "Laptop Support" or "Server Support" . These categories are configured as Skill Groups in the
                                       				ICM.

The Boston call center has an Avaya ACD (peripheral) connected
                                       				with an ARS PG. The New York call center has an Aspect ACD (peripheral)
                                       				connected with an ACD PG.

Skill Groups are configured for each peripheral in the ICM.

The script above is used for the following:

The script is associated with a Call Type to route support calls.
                                       				The call type is used to define the treatment provided by the call centers.

The script uses Caller entered digits (CED) to determine the skill
                                       				group (Laptop Support or Server Support) required to handle the call.

The script uses the LAA (longest available agent) node to look for
                                       				an available agent at a particular call center. In this case the call may have
                                       				arrived at the Boston call center, and you prefer to look for an available agent
                                       				from that call center first.

If an agent is not available, the script uses the LAA (longest
                                       				available agent) node to look for an available agent across the enterprise.

If an agent is not available, the script instructs the ICM
                                       				software to translation route the call to the VRU and queue the call
                                       				(Enterprise queuing).

Depending on the call center where there is an available agent, the
                                       				ICM software does the following:

If an agent is available at the New York call center, the call
                                             					 routes to the Aspect ACD. The ACD at the site then picks an agent and assigns
                                             					 the call.

If an agent is available at the Boston (ARS) call center, Unified CCE software selects the agent and provides instructions to the routing client (VRU) to direct the call to the agent.

### Reporting
                           	 Considerations for Hybrid Routing Deployments

In order to get accurate and useful reporting metrics in this type of deployment, it is important to consider several factors
                                 that affect reporting. For more information, see Enterprise Routing .

Some of these
                                 		  factors include:

Two reporting
                                       				models used to provide reporting statistics for the application: Services are
                                       				used for Enterprise Routing and Call Types for Agent Level Routing.

The use of a
                                       				Service Control VRU in your deployment to provide initial call treatment and
                                       				enterprise queuing when sharing queues (skill groups) across call centers. This
                                       				entails queuing calls to skill groups waiting for an available agent across
                                       				your enterprise.

The reporting on queuing statistics—ACD queues and Enterprise queues.

The use of the
                                       				Translation Routing mechanism to route calls to legacy ACDs for enterprise
                                       				routing. This allows for call types to be used to provide reporting statistics
                                       				for the application (Cradle to Grave). Translation Routing is implicit with
                                       				Agent Level Routing.

Routing scripts
                                       				set up for your call center operations.

The table below
                                 		  defines the report categories to use to meet the reporting needs for your
                                 		  enterprise.

Enterprise Reporting

Use Call Type
                                       				reports for an enterprise view of reporting statistics for the application,
                                       				including queue statistics.

Use Enterprise
                                       				Skill Group reports for an enterprise view of reporting statistics when calls
                                       				are routed to a particular skill group, including queue statistics.

Report
                                             						focus

Reporting
                                             						Statistics Needed

Report
                                             						Template

Key
                                             						Statistics

Application

Before
                                             						call is routed to an agent

Call Type

Number of
                                             						calls routed.

Number of
                                             						calls received.

Number of
                                             						calls that encountered an error.

Queue
                                             						Statistics and Abandons.

After call
                                             						is routed to an agent

Call Type

Abandons

Service
                                             						Level

Redirection on No Answer (RONA)

After call
                                             						is answered by an agent

Call Type

ASA

Calls
                                             						Handled

Transfers

Skill
                                             						Group

Calls
                                             						routed to a skill group

Queued
                                             						calls

Peripheral
                                             						Skill Group & Enterprise Skill Group

Queue
                                             						Statistics

Abandons

RONA

Service
                                             						Levels

After call
                                             						is answered by an agent

Peripheral
                                             						Skill Group & Enterprise Skill Group

ASA

Calls
                                             						Handled

Avg.TalkTime

Avg.HandleTime

Agent Info

Peripheral
                                             						Skill Group & Enterprise Skill Group

Full Time
                                             						Equivalent Agents (FTE)

Percent
                                             						Utilization.

Agents

Agent Info

Agent by
                                             						individual, team, peripheral or skill group

Agent's
                                             						current state

Duration
                                             						in a state

Agents
                                             						logged out

Calls
                                             						Handled

Avg.Talk
                                             						Time

Avg.Handle
                                             						Time

| Note | Cisco Unified CCE scripts provide a predefined MED (Minimum Expected Delay) calculation that can be used only with ICM Services. |
|---|---|

| Report Focus | Reporting Statistics Needed | Report Template | Key Statistics |
|---|---|---|---|
| Application | Before the call is routed to the ACD | Call Type | Number of calls routed Number of calls received Number of calls that encountered an error or received default
                                             					 treatment |
| After the call is routed to the ACD, calls queued on the ACD | Peripheral Service Enterprise Service | Queue Statistics (ACD Queue) Abandons Service Level RONA |
| After the call is answered by agent | Peripheral Service Enterprise Service | ASA Calls Handled Avg. Handle Time Transfers |
| Skill Group | For calls routed to skill groups and queued calls | Peripheral Skill Group Enterprise Skill Group | Queue Statistics (ACD Queue) Abandons RONA |
| After the call is answered by agent | Peripheral Skill Group Enterprise Skill Group | ASA Calls Handled Avg. Handle Time Avg. Talk Time |
| Agent Info | Peripheral Skill Group Enterprise Skill Group | FTEs and Percent Utilization |
| Agents | Agent Info | Agent | Agent's current state Duration in state Agents logged out Calls Handled Avg. Handle Time Avg. Talk Time |

| Report Focus | Reporting Statistics Needed | Report Template | Key Statistics |
|---|---|---|---|
| Application | After the call is routed to the ACD, calls queued on the ACD | Call Type | Abandons |
| After the call is answered by agent | Call Type | ASA Calls Handled |

| Note | Call Types cannot report on queued metrics for calls queued on the ACD (ACD queue), such as
                                          		the number of calls queued on the ACD. |
|---|---|

| Report Focus | Reporting Statistics Needed | Report Template | Key Statistics |
|---|---|---|---|
| Application | Before the call is routed to the ACD, queued in the enterprise | Call Type | Number of calls routed Number of calls received Number of calls that encountered an error Enterprise Queue Statistics and Abandon in Enterprise Queue |
| After the call is routed to ACD | Peripheral Service Enterprise Service | Abandons RONA |
| After the call is answered by the agent | Peripheral Service Enterprise Service | Calls Handled Avg Handled Time Transfers |

| Note | Skill Groups report on Enterprise queue statistics. |
|---|---|

| Report Focus | Reporting Statistics Needed | Report Template | Key Statistics |
|---|---|---|---|
| Application | Before the call is routed to the ACD, queued in the enterprise | Call Type | Number of calls routed Number of calls received Number of calls that encountered an error Queue Statistics and Abandon in Queue |
| After the call is routed to the ACD | Call Type | Abandons Service Level Note RONA calls are reported on services and are not available
                                                      					 for Call Types. | Note | RONA calls are reported on services and are not available
                                                      					 for Call Types. |
| Note | RONA calls are reported on services and are not available
                                                      					 for Call Types. |
| After the call is answered by agent | Call Type | Calls Handled Avg Handled Time ASA |

| Note | RONA calls are reported on services and are not available
                                                      					 for Call Types. |
|---|---|

| Note | Skill Groups report on Enterprise queue statistics. |
|---|---|

| Report
                                             						focus | Reporting
                                             						Statistics Needed | Report
                                             						Template | Key
                                             						Statistics |
|---|---|---|---|
| Application | Before
                                             						call is routed to an agent | Call Type | Number of
                                             						calls routed. Number of
                                             						calls received. Number of
                                             						calls that encountered an error. Queue
                                             						Statistics and Abandons. |
| After call
                                             						is routed to an agent | Call Type | Abandons Service
                                             						Level Redirection on No Answer (RONA) |
| After call
                                             						is answered by an agent | Call Type | ASA Calls
                                             						Handled Transfers |
| Skill
                                             						Group | Calls
                                             						routed to a skill group Queued
                                             						calls | Peripheral
                                             						Skill Group & Enterprise Skill Group | Queue
                                             						Statistics Abandons RONA Service
                                             						Levels |
| After call
                                             						is answered by an agent | Peripheral
                                             						Skill Group & Enterprise Skill Group | ASA Calls
                                             						Handled Avg.TalkTime Avg.HandleTime |
| Agent Info | Peripheral
                                             						Skill Group & Enterprise Skill Group | Full Time
                                             						Equivalent Agents (FTE) Percent
                                             						Utilization. |
| Agents | Agent Info | Agent by
                                             						individual, team, peripheral or skill group | Agent's
                                             						current state Duration
                                             						in a state Agents
                                             						logged out Calls
                                             						Handled Avg.Talk
                                             						Time Avg.Handle
                                             						Time |