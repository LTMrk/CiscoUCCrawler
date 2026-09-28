---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-report-d7a221b0a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_Reporting-User-Guide-12-5/pcce_b_cisco-packaged-contact-center-enterprise_chapter_01011.html
retrieved_at: 2026-08-21T16:58:01.682385+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.5(1)

Updated: February 4, 2020

Chapter: Skill Group Reporting

## Chapter: Skill Group Reporting

- Skill Group Reporting

- Skill Group Activity

- Default Skill                              	 Group Data in Reports

# Skill Group Reporting

## Skill Group Activity

You can report on skill groups using  Agent Skill Group reports and Skill Group reports.

Agent Skill Group reports. Report on all of the agents in one or more skill groups.  For an agent who belongs to more than one skill group, these reports
                           allow you to monitor that agent across all of those skill groups.

Skill Group reports. Monitor operational performance. For example, you could compare the performance of several skill groups or to see if calls
                           are being distributed evenly by your routing scripts and configuration.

## Default Skill
                        	 Group Data in Reports

A default skill
                           		group is created for each configured Media Routing Domain. The default skill
                           		group acts as a bucket to capture information about voice calls and non-voice
                           		tasks, in the following situations:

A call is not
                                 			 routed by a Packaged CCE routing script.

A skill group is
                                 			 not specified in a routing script.

The Agent to
                                 			 Agent node is used in a routing script for agent-to-agent dialing.

The Queue to
                                 			 Agent node queues a task to an agent and the agent is not logged into the skill
                                 			 group specified in that node.

Including the
                           		default skill group in reports helps to identify non- Packaged CCE-routed calls
                           		within agent and skill group reports, and ensures that agent/skill group
                           		reports balance with call type reports, because call type reports include only
                           		Packaged CCE-routed calls.

Metrics for the
                           		default skill group are affected by different types of calls, including new
                           		calls, agent-to-agent dialing, transfers and conferences, and Emergency and
                           		Supervisor Assist.

New outbound and incoming
                              		  direct calls increment default skill group metrics, as follows:

AgentOutCalls
                                 			 for external outbound calls.

InternalCalls
                                 			 for the internal outbound calls.

InternalCallRcvd
                                 			 for the direct incoming calls.

CallsHandled is
                                       		  not incremented for the default skill group, because the default skill group
                                       		  can not be referenced in any script.

Agent-to-agent dialing using the agent to agent node in the script increments default skill group
                           		metrics, as follows:

OutgoingExternal
                                 			 or OutgoingInternal is incremented for the default skill group of the agent
                                 			 initiating the agent to agent call.

InternalCallsReceived is incremented for the default skill group
                                 			 of the agent receiving the agent to agent call.

Transfers and
                              		  conferences increment default skill group metrics, as follows:

If agent A
                                 			 transfers or conferences a Packaged CCE–routed call to agent B directly without
                                 			 using a script, OutgoingExternal or OutgoingInternal for agent A is incremented
                                 			 against the skill group of the Packaged CCE-routed call. For agent B,
                                 			 IncomingDirect is incremented against the default skill group.

If the agent A
                                 			 transfers or conferences a Packaged CCE–routed call to a dialed number that
                                 			 accesses a transfer or conference script that has an agent to agent node,
                                 			 OutgoingExternal or OutgoingInternal for agent A is incremented for the skill
                                 			 group of the Packaged CCE-routed call. For agent B, IncomingDirect is
                                 			 incremented for the default skill group

Emergency and Supervisor
                              		  Assist calls increment InternalCallsRcvd for the supervisor's default skill
                           		group.

| Note | When an agent
                                          			 makes an outbound call as part of a consultative call, the call is not
                                          			 attributed to the default skill group. It is attributed to the skill group for
                                          			 the consulting agent on the original call. |
|---|---|

| Note | CallsHandled is
                                       		  not incremented for the default skill group, because the default skill group
                                       		  can not be referenced in any script. |
|---|---|