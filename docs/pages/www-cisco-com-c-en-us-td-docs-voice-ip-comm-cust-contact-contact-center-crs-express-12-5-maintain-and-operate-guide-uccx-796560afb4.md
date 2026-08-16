---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-796560afb4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_uccx-125admin-and-operations-guide/uccx_b_uccx-125admin-and-operations-guide_chapter_010.html
retrieved_at: 2026-08-16T21:42:26.913479+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Unified CCX
	 Provision Checklist

## Chapter: Unified CCX
	 Provision Checklist

# Unified CCX
                     	 Provision Checklist

The Cisco Unified Communications
                              			 Manager (CM) product supports both single-node and two-node (high
                           		  availability) deployments available for the Cisco Unified Contact Center
                           		  Express (CCX).

The
                           		  deployment model is transparent to the Unified CCX installer as the clustering
                           		  for Unified CM is
                           		  performed through the Unified CCX Administration using the Unified CCX setup
                           		  wizard. The high availability over WAN feature of Unified CCX is supported only
                           		  for Unified CM deployments.

The
                           		  following topics introduce the Unified CCX subsystem and explain how to modify
                           		  the Unified CM information from Unified CCX.

## Unified
                        	 CCX

The
                              		  Unified CCX system uses the Unified CCX subsystem as part of an ACD system to
                              		  provide resource distribution and queueing to call centers.

Two types
                              		  of routing are available:

Contact Service Queue
                                       				  (CSQ)-based routing— CSQs are entities that route calls to your resources
                                    				(agents). Each CSQ controls incoming calls and determines where an incoming
                                    				call is placed in the queue and to which agent the call is sent.

Each CSQ
                                    				selects resources from an associated resource pool that you define or from
                                    				resource skills for all Unified CCX license packages. When an agent becomes
                                    				available to take a call, the system chooses a queued call from one of the CSQs
                                    				whose resource pool includes the agent, and routes that call to that agent.

Agent-based
                                       				  routing— Agent-based routing provides the ability to send a call to a specific agent, rather than any agent available in a CSQ.

A Unified
                              		  CCX agent can participate in both CSQ-based and agent-based routing. A Unified
                              		  CCX agent can be any one of the following:

Cisco Finesse

IP Phone Agent

Extension
                                    				Mobility (EM) Agent

Supervisor (if
                                    				the supervisor is taking calls)

A supervisor who
                                          			 is not taking calls is not considered to be an agent.

Calls are
                              		  queued in the Unified CCX server and sent to agents by the Unified CCX server.

The
                              		  machine you install your Unified CCX system on determines how many agents and
                              		  IVR ports Unified CCX can accommodate. However, be aware of the following
                              		  general configuration rules:

Each agent
                                    				cannot be associated with more than:

25 CSQs
                                          					 (This is a configuration design guideline; Unified CCX Administration does not
                                          					 enforce the rule.)

50 skills
                                          					 (Unified CCX Administration enforces this rule.)

Each CSQ
                                    				cannot be associated with more than 50 skills. (Unified CCX Administration
                                    				enforces this rule.)

A call should
                                    				not queue for more than 25 CSQs. (This is a configuration design guideline;
                                    				Unified CCX Administration does not enforce the rule.)

## Provision Unified
                        	 CCX

To
                              		  provision Unified CCX, complete the following tasks:

Step

Task

Unified CM

Step 1

Configure Unified CM users who will be agents in your Unified CCX system.

Provision Unified CM for Unified CCX

Step 2

Provision resources information for Unified CCX telephony and media.

Provision Unified CM Telephony Subsystem

Step 3

Provision RmCm Provider to allow RmCm Subsystem to be in service.

RmCm Provider Configuration

Step 4

Create resource groups.

Resource Groups

Step 5

Create skills.

Skills Configuration

Step 6

Assign agents to resource groups and assign skills to agents.

Agent Configuration

Step 7

Create Contact Service Queues.

Contact Service Queue Configuration

Step 9

Provision agent-based routing—if using Unified CCX Enhanced or Premium.

Configure Agent-Based Routing

Step 10

Create teams and assign agents to teams.

Teams Configuration

## Change Licensing
                        	 Packages

Now, the Unified CCX system can be upgraded from Enhanced to Premium.

While upgrading the licenses, you need to configure the following system parameters:

Enhanced to Premium— You need to configure the Number of Direct Preview Outbound Seats while upgrading to a Premium license.

Downgrade of license is not supported in Unified CCX.

Choose System > System
                                             				  Parameters from the Cisco Unified CCX Administration
                                       			 menu bar to open the System Parameters Configuration web page where you can
                                       			 update these values.

| Note | A supervisor who
                                          			 is not taking calls is not considered to be an agent. |
|---|---|

| Step | Task | Unified CM |
|---|---|---|
| Step 1 | Configure Unified CM users who will be agents in your Unified CCX system. | Provision Unified CM for Unified CCX |
| Step 2 | Provision resources information for Unified CCX telephony and media. | Provision Unified CM Telephony Subsystem |
| Step 3 | Provision RmCm Provider to allow RmCm Subsystem to be in service. | RmCm Provider Configuration |
| Step 4 | Create resource groups. | Resource Groups |
| Step 5 | Create skills. | Skills Configuration |
| Step 6 | Assign agents to resource groups and assign skills to agents. | Agent Configuration |
| Step 7 | Create Contact Service Queues. | Contact Service Queue Configuration |
| Step 9 | Provision agent-based routing—if using Unified CCX Enhanced or Premium. | Configure Agent-Based Routing |
| Step 10 | Create teams and assign agents to teams. | Teams Configuration |

| Note | Downgrade of license is not supported in Unified CCX. |
|---|---|

| Choose System > System
                                             				  Parameters from the Cisco Unified CCX Administration
                                       			 menu bar to open the System Parameters Configuration web page where you can
                                       			 update these values. |
|---|