---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-user-guide-uccx-b-1251su2-d20b1209b0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/user/guide/uccx_b_1251su2_finesse-agent-supervisor-desktop-user-guide/uccx_b_1252finesse-agent-supervisor-desktop-guide_appendix_01001.html
retrieved_at: 2026-08-16T21:24:25.501379+00:00
---

Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU2

# Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU2

Updated: April 10, 2022

Chapter: Behavior of Adding and Removing Agents to CSQ

## Chapter: Behavior of Adding and Removing Agents to CSQ

- Behavior of Adding and Removing Agents to CSQ

# Behavior of Adding and Removing Agents to CSQ

When you add or remove agents to CSQ, the skills and competencies of the agents are updated to match the queue requirements.
                           The changes are explained with an example. In this example, the following are considered:

Skills : English, Sales, and Services

Agent Name : Michael

Supervisor Name : Sandra

CSQ details :

CSQ Name

Skill(Competency)

SalesQueue

English(8), Sales(5)

ServicesQueue

English(5), Services(5)

GeneralQueue

English(8)

Assumptions:

All scenarios start with empty skills for an agent, unless explained in the specific scenario.

Supervisor uses Advanced Capabilities in Finesse to add and remove agents to CSQ.

Administrator uses Unified CCX Administration UI to add and remove agents to CSQ.

There are no two queues with similar skills and competencies.

Add strategy : When supervisors add agents to a queue, the skills and competencies of the agents that are required to be part of the queue
                           are updated at the server.

Remove strategies : When a supervisor removes an agent from a queue, two strategies Minimal Impact and Revert are adopted.

Minimal Impact strategy - Reduces the competency of a skill or removes the skill, such that the agent is removed from the queue and impact on the
                                 other queues is minimal.

Revert strategy- Revert the operation that is done during Add by removing the respective skills.

The behavior is explained by considering some of the scenarios.

Scenario 1- Before upgrading unified CCX to 12.0 release, administrator adds Michael to SalesQueue. After upgrading to unified CCX 12.0
                           release, Sandra removes Michael from SalesQueue.

Agent Skill(Competency) before Action

Action

Agent Skill(Competency) after Action

Strategy

No Skill

Admin adds Michael to SalesQueue

English(8), Sales(5)

Add

Michael is also part of GeneralQueue because the skill English(8) is common for both the queues.

English(8), Sales(5)

Sandra removes Michael from SalesQueue

English(8), Sales(4)

Minimal Impact

As Michael was added to the queue by administrator before upgrading to unified CCX 12.0 release, the competency of the Sales
                                                   skill is reduced by 1.

Scenario 2 - Sandra adds Michael to SalesQueue and later removes him from SalesQueue.

Agent Skill(Competency) before Action

Action

Agent Skill(Competency) after Action

Strategy

No Skill

Sandra adds Michael to SalesQueue

English(8), Sales(5)

Add

Michael is also added to GeneralQueue because the skill English(8) is common for both the queues.

English(8), Sales(5)

Sandra removes Michael from SalesQueue

No Skill

Revert

Michael is removed from GeneralQueue also.

Scenario 3 - Sandra adds Michael to SalesQueue and ServicesQueue. Later she removes him first from ServicesQueue and then from SalesQueue.

Agent Skill(Competency) before Action

Action

Agent Skill(Competency) after Action

Strategy

No Skill

Sandra adds Michael to SalesQueue

English(8), Sales(5)

Add

Michael is also added to GeneralQueue because the skill English(8) is common for both the queues.

English(8), Sales(5)

Sandra adds Michael to ServicesQueue

English(8), Sales(5), Services(5)

Add

English(8), Sales(5), Services(5)

Sandra removes Michael from ServicesQueue

English(8), Sales(5)

Revert

English(8), Sales(5)

Sandra removes Michael from SalesQueue

No Skill

Revert

Scenario 4 - Sandra adds Michael to SalesQueue and ServicesQueue. Later she removes him first from SalesQueue and then from ServicesQueue.

Agent Skill(Competency) before Action

Action

Agent Skill(Competency) after Action

Strategy

No Skill

Sandra adds Michael to SalesQueue

English(8), Sales(5)

Add

Michael is also added to GeneralQueue because the skill English(8) is common for both the queues.

English(8), Sales(5)

Sandra adds Michael to ServicesQueue

English(8), Sales(5), Services(5)

Add

English(8), Sales(5), Services(5)

Sandra removes Michael from SalesQueue

English(8), Services(5)

Revert

Revert is partially applied. Only Sales skill is removed and the common skill and competency English(8) is retained.

English(8), Services(5)

Sandra removes Michael from ServicesQueue

English(8)

Revert

Only Services skill is removed. English(8) is not removed because Michael is part of the GeneralQueue.

In this scenario, Sandra has to manually remove Michael from the GeneralQueue.

Scenario 5 - Sandra adds Michael to GeneralQueue and ServicesQueue. Later she removes him first from GeneralQueue and then from the ServicesQueue.

Agent Skill(Competency) before Action

Action

Agent Skill(Competency) after Action

Strategy

No Skill

Sandra adds Michael to GeneralQueue

English(8)

Add

English(8)

Sandra adds Michael to ServicesQueue

English(8), Services(5)

Add

English(8), Services(5)

Sandra removes Michael from GeneralQueue

English(7), Services(5)

Minimal Impact

A minimal change is made to the competency of the common skill English so that the required skills and competencies are maintained.

English(7), Services(5)

Sandra removes Michael from ServicesQueue

No Skill

Revert

As part of Revert strategy, only Services skill is removed. After the revert operation English(7) skill is also removed because
                                                   it is not associated with any queue and no longer required by Michael.

Scenario 6 - Sandra adds Michael to GeneralQueue and SalesQueue. Later she removes him first from GeneralQueue and then from the SalesQueue.

Agent Skill(Competency) before Action

Action

Agent Skill(Competency) after Action

Strategy

No Skill

Sandra adds Michael to GeneralQueue

English(8)

Add

English(8)

Sandra adds Michael to SalesQueue

English(8), Sales(5)

Add

English(8), Sales(5)

Sandra removes Michael from GeneralQueue

No Skill

Revert

As the skill English(8) is common for both GeneralQueue and SalesQueue, Minimal Impact or Partial Revert cannot be applied.
                                                   Michael will be removed from both the queues.

| CSQ Name | Skill(Competency) |
|---|---|
| SalesQueue | English(8), Sales(5) |
| ServicesQueue | English(5), Services(5) |
| GeneralQueue | English(8) |

| Agent Skill(Competency) before Action | Action | Agent Skill(Competency) after Action | Strategy |
|---|---|---|---|
| No Skill | Admin adds Michael to SalesQueue | English(8), Sales(5) | Add Note Michael is also part of GeneralQueue because the skill English(8) is common for both the queues. | Note | Michael is also part of GeneralQueue because the skill English(8) is common for both the queues. |
| Note | Michael is also part of GeneralQueue because the skill English(8) is common for both the queues. |
| English(8), Sales(5) | Sandra removes Michael from SalesQueue | English(8), Sales(4) | Minimal Impact Note As Michael was added to the queue by administrator before upgrading to unified CCX 12.0 release, the competency of the Sales
                                                   skill is reduced by 1. | Note | As Michael was added to the queue by administrator before upgrading to unified CCX 12.0 release, the competency of the Sales
                                                   skill is reduced by 1. |
| Note | As Michael was added to the queue by administrator before upgrading to unified CCX 12.0 release, the competency of the Sales
                                                   skill is reduced by 1. |

| Note | Michael is also part of GeneralQueue because the skill English(8) is common for both the queues. |
|---|---|

| Note | As Michael was added to the queue by administrator before upgrading to unified CCX 12.0 release, the competency of the Sales
                                                   skill is reduced by 1. |
|---|---|

| Agent Skill(Competency) before Action | Action | Agent Skill(Competency) after Action | Strategy |
|---|---|---|---|
| No Skill | Sandra adds Michael to SalesQueue | English(8), Sales(5) | Add Note Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. | Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
| Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
| English(8), Sales(5) | Sandra removes Michael from SalesQueue | No Skill | Revert Note Michael is removed from GeneralQueue also. | Note | Michael is removed from GeneralQueue also. |
| Note | Michael is removed from GeneralQueue also. |

| Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
|---|---|

| Note | Michael is removed from GeneralQueue also. |
|---|---|

| Agent Skill(Competency) before Action | Action | Agent Skill(Competency) after Action | Strategy |
|---|---|---|---|
| No Skill | Sandra adds Michael to SalesQueue | English(8), Sales(5) | Add Note Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. | Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
| Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
| English(8), Sales(5) | Sandra adds Michael to ServicesQueue | English(8), Sales(5), Services(5) | Add |
| English(8), Sales(5), Services(5) | Sandra removes Michael from ServicesQueue | English(8), Sales(5) | Revert |
| English(8), Sales(5) | Sandra removes Michael from SalesQueue | No Skill | Revert |

| Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
|---|---|

| Agent Skill(Competency) before Action | Action | Agent Skill(Competency) after Action | Strategy |
|---|---|---|---|
| No Skill | Sandra adds Michael to SalesQueue | English(8), Sales(5) | Add Note Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. | Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
| Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
| English(8), Sales(5) | Sandra adds Michael to ServicesQueue | English(8), Sales(5), Services(5) | Add |
| English(8), Sales(5), Services(5) | Sandra removes Michael from SalesQueue | English(8), Services(5) | Revert Note Revert is partially applied. Only Sales skill is removed and the common skill and competency English(8) is retained. | Note | Revert is partially applied. Only Sales skill is removed and the common skill and competency English(8) is retained. |
| Note | Revert is partially applied. Only Sales skill is removed and the common skill and competency English(8) is retained. |
| English(8), Services(5) | Sandra removes Michael from ServicesQueue | English(8) | Revert Note Only Services skill is removed. English(8) is not removed because Michael is part of the GeneralQueue. In this scenario, Sandra has to manually remove Michael from the GeneralQueue. | Note | Only Services skill is removed. English(8) is not removed because Michael is part of the GeneralQueue. In this scenario, Sandra has to manually remove Michael from the GeneralQueue. |
| Note | Only Services skill is removed. English(8) is not removed because Michael is part of the GeneralQueue. In this scenario, Sandra has to manually remove Michael from the GeneralQueue. |

| Note | Michael is also added to GeneralQueue because the skill English(8) is common for both the queues. |
|---|---|

| Note | Revert is partially applied. Only Sales skill is removed and the common skill and competency English(8) is retained. |
|---|---|

| Note | Only Services skill is removed. English(8) is not removed because Michael is part of the GeneralQueue. In this scenario, Sandra has to manually remove Michael from the GeneralQueue. |
|---|---|

| Agent Skill(Competency) before Action | Action | Agent Skill(Competency) after Action | Strategy |
|---|---|---|---|
| No Skill | Sandra adds Michael to GeneralQueue | English(8) | Add |
| English(8) | Sandra adds Michael to ServicesQueue | English(8), Services(5) | Add |
| English(8), Services(5) | Sandra removes Michael from GeneralQueue | English(7), Services(5) | Minimal Impact Note A minimal change is made to the competency of the common skill English so that the required skills and competencies are maintained. | Note | A minimal change is made to the competency of the common skill English so that the required skills and competencies are maintained. |
| Note | A minimal change is made to the competency of the common skill English so that the required skills and competencies are maintained. |
| English(7), Services(5) | Sandra removes Michael from ServicesQueue | No Skill | Revert Note As part of Revert strategy, only Services skill is removed. After the revert operation English(7) skill is also removed because
                                                   it is not associated with any queue and no longer required by Michael. | Note | As part of Revert strategy, only Services skill is removed. After the revert operation English(7) skill is also removed because
                                                   it is not associated with any queue and no longer required by Michael. |
| Note | As part of Revert strategy, only Services skill is removed. After the revert operation English(7) skill is also removed because
                                                   it is not associated with any queue and no longer required by Michael. |

| Note | A minimal change is made to the competency of the common skill English so that the required skills and competencies are maintained. |
|---|---|

| Note | As part of Revert strategy, only Services skill is removed. After the revert operation English(7) skill is also removed because
                                                   it is not associated with any queue and no longer required by Michael. |
|---|---|

| Agent Skill(Competency) before Action | Action | Agent Skill(Competency) after Action | Strategy |
|---|---|---|---|
| No Skill | Sandra adds Michael to GeneralQueue | English(8) | Add |
| English(8) | Sandra adds Michael to SalesQueue | English(8), Sales(5) | Add |
| English(8), Sales(5) | Sandra removes Michael from GeneralQueue | No Skill | Revert Note As the skill English(8) is common for both GeneralQueue and SalesQueue, Minimal Impact or Partial Revert cannot be applied.
                                                   Michael will be removed from both the queues. | Note | As the skill English(8) is common for both GeneralQueue and SalesQueue, Minimal Impact or Partial Revert cannot be applied.
                                                   Michael will be removed from both the queues. |
| Note | As the skill English(8) is common for both GeneralQueue and SalesQueue, Minimal Impact or Partial Revert cannot be applied.
                                                   Michael will be removed from both the queues. |

| Note | As the skill English(8) is common for both GeneralQueue and SalesQueue, Minimal Impact or Partial Revert cannot be applied.
                                                   Michael will be removed from both the queues. |
|---|---|