---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--de350e31cd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting-concepts-for-cisco-unified12_5/ucce_b_reporting-concepts-for-cisco-unified12_5_chapter_01000.html
retrieved_at: 2026-08-22T00:02:54.495364+00:00
---

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Agent Teams and Supervisors

## Chapter: Agent Teams and Supervisors

# Agent Teams and Supervisors

## Agent Teams and Supervisors

This chapter provides information about agent teams and supervisors.

## Agent Team Reports

Supervisors can report on the agents in teams that they
                              supervise to monitor the performance of a
                              particular team.

Teams are peripheral-specific. All agents on
                              a team and the supervisors for the team must reside on the same peripheral.
                              An individual agent can be assigned to one team only.

Supervisors
                              are a special type of agents who were configured in the Configuration
                              Manager with limited reporting privileges to see information in the agent
                              report categories, and within those categories, to see data for only those
                              agents on teams that they supervise.

You can select 0 or 1
                              primary supervisor for an agent team, and you can select multiple secondary
                              supervisors for each team. Each supervisor can be a supervisor for multiple
                              teams.

## Supervisor Activity

Agent team supervisors can take advantage of supervisory features available on their desktops. Use reports to see  when supervisors
                              had to use the Barge-In and Intercept features.

### Barge-In ( Unified CCE )

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

### Intercept ( Unified CCE )

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

### Reports That Show Information on Agent Teams

The following reports contain information on agent teams:

Unified IC Agent Team Real Time All Fields

Unified
                                       IC Agent Team Historical All Fields

Agent Team State
                                       Counts Real Time

| Note | To use agent team reports, configure
                                       teams and supervisors in Configuration Manager. The team structure you choose
                                       is up to you. You can use your ACD configuration. You can also
                                       use your ACD reports to monitor agent teams. |
|---|---|

| Note | These supervisory features are not available to agents using MRDs other than Voice. |
|---|---|

| Note | If you deployed Unified CCE as the VRU, data is not gathered for Barge-In. |
|---|---|

| Fields incremented for agent's skill group to which the call was
                                             routed | Fields incremented for supervisor's
                                             default skill group |
|---|---|
| CallsHandled, InternalCalls, BargeInCalls | BargeInCalls, InternalCallsRcvd |

| Note | If you have deployed Unified CCE as the VRU, data is not gathered for Intercept. |
|---|---|

| Fields incremented for agent's skill group to which the call was
                                             routed | Fields incremented for supervisor's
                                             default skill group |
|---|---|
| InterceptCalls | InterceptCalls |