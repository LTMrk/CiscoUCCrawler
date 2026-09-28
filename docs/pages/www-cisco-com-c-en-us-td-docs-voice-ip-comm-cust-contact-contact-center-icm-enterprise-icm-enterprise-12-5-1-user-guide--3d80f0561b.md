---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--3d80f0561b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting-concepts-for-cisco-unified12_5/ucce_b_reporting-concepts-for-cisco-unified12_5_chapter_010011.html
retrieved_at: 2026-08-22T00:03:41.076904+00:00
---

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Reporting in a Multichannel Environment

## Chapter: Reporting in a Multichannel Environment

# Reporting in a Multichannel Environment

## Multichannel Options

When you include multichannel applications in a deployment, you can configure agents to handle nonvoice tasks such as chat
                              and email in addition to voice calls.

Supported multichannel applications include:

Enterprise Chat and
                                             						Email : This application enables organizations to
                                    intelligently route and process inbound emails, webform inquiries, faxes, and
                                    letters. It also enables text chat messaging and page-push abilities. Agents can assist customers while on the phone, by navigating
                                    through
                                    web pages that the customer is currently browsing.

Third-party multichannel applications : These applications use the Task
                                          					Routing APIs to send new task requests and control agent state and task activity. Third-parties can develop applications to submit
                                    any type of task request for routing,  such as chat, email, or SMS.

## Media Routing Domains

Media Routing Domains (MRDs) organize how Unified CCE routes requests for each communication medium, such as voice and email, to agents.

You assign each skill group or precision queue to an MRD. Unified CCE then can route a task to an agent who is associated both with a specific skill group or precision queue and with a specific
                              medium.

The
                              Voice MRD is created by default for all deployments.  You configure MRDs for each of the other media in your deployment, such
                              as chat, email, or SMS.

You can report on activity for all of the configured MRDs.

## Multichannel Reporting Data

Unified CCE databases store information about agent activity and tasks routed by Unified CCE , including nonvoice tasks such as chat and email. Reports contain a Media field, when appropriate, to identify the MRD of
                              each task included in the report.

The following table describes major differences between
                              voice and
                              nonvoice tasks in reports.

Type of Data

Data for Voice
                                          Tasks

Data for Nonvoice Tasks

Task direction

Task direction can be both incoming (agent receives a call) and
                                          outgoing (agent places a call).

Task direction is always incoming, and values of report
                                          fields pertaining to outgoing nonvoice tasks are set to null.

Session ownership changes

The ownership of a voice task can change through the life of the call.
                                          Agents can transfer the call or conference in another agent.

The ownership of a nonvoice task routed to Unified CCE from third-party multichannel applications that use the Task
                                                					Routing APIs can change during the life of the task. Agents can transfer these tasks. Agents cannot conference these tasks, and supervisors
                                          cannot barge in or intercept the tasks.

Nonvoice Enterprise Chat and
                                                						Email tasks do not change session ownership. These tasks
                                          cannot be transferred or conferenced and supervisors cannot barge into or
                                          intercept the task.

While it is possible for a Enterprise Chat and
                                                            						Email agent to allow another agent to join a session and then drop the session, leaving the second agent and the caller in session
                                                      together, this is not the same as a voice call transfer. Unified CCE software interprets this scenario as two different sessions, one for the original agent and one for the second agent.

Also, while Enterprise Chat and
                                                						Email agents can forward messages to other agents, this is not the same as a voice call transfer. Unified CCE interprets message forwarding as two different sessions, one for the original agent and one for the receiving agent.

Short
                                          calls

Voice calls are considered to be short
                                          calls if they disconnect within the time boundaries defined in the Agent Desk
                                          Settings for short tasks.

The Agent Desk Settings for short tasks do not apply to nonvoice tasks.  The concept of short calls is not applicable for
                                          these tasks.

Values of report fields pertaining to short
                                          calls are set to zero.

Service Level

You determine which Service Level type you want to use
                                          for voice tasks.

For third-party multichannel applications that use the Task
                                                					Routing APIs, you determine the Service Level type you want to use.

For Enterprise Chat and
                                                						Email , the Service Level is always set to "ignore
                                             abandoned calls" .

### Report Data for Multiple Tasks

Because multichannel agents can be configured to handle more than one task at once, task duration fields in reports can display
                              a value greater than the reporting interval for nonvoice tasks. For example, the half-hour duration fields can have a value
                              greater than 30 minutes.

The Voice MRD is not interruptible.  An agent handling a voice call cannot be interrupted with a task from another MRD.

If the deployment includes third-party multichannel applications that use the Task
                                    					Routing APIs:

For nonvoice MRDs, agents can be configured
                                    at login to handle multiple concurrent nonvoice tasks.

If an agent
                                    is engaged in several concurrent chat tasks, the reports contain data for each of the
                                    tasks.

A nonvoice MRD can be configured to be interruptible; an agent handling a task in that MRD can be interrupted with a task
                                    from another MRD.  The agent is configured at login to either accept or ignore interrupts:

Accept: The agent's state changes to Interrupted for the original task, and the time on that task stops while the agent is Interrupted.

Ignore: The agent's state is  Active for both tasks, and the time on the original task does not stop.

If the deployment includes Enterprise Chat and
                                    						Email :

Chat is not interruptible.  However, agents can be configured to handle multiple concurrent chat tasks.

If an agent
                                    is engaged in several concurrent chat tasks, the reports contain data for each of the
                                    tasks.

Email is interruptible.  An agent handling an email can be interrupted with a voice call or a chat.

Reports show the agent as Active for both the
                                    email and voice or chat task.

## Report Templates for Multichannel Applications

Cisco Unified Intelligence Center  templates report
                              on all voice and multichannel skill groups, agents, and tasks.

You can filter these Unified Intelligence Center report templates by Media Routing Domain:

Agent Real Time

Agent Skill Group Real Time

Enterprise Skill Group Real Time

Peripheral Skill Group Real Time
                                    All Fields

Precision Queue Real Time All Fields

Agent Precision Queue Historical All
                                    Fields

Agent Skill Group Historical All
                                    Fields

Peripheral Skill Group Historical All
                                    Fields

Precision Queue Abandon Answer
                                    Distribution Historical

Precision Queue Interval All Fields

Skill Group Abandon-Answer Distribution
                                    Historical

Precision Queue - Live Data

Skill Group - Live Data

Reports generated from Unified Intelligence Center templates do not contain details about specific events that transpire
                              during a task. For
                              example, the reports show that an agent handled a task in the chat Media Routing Domain,
                              but do not provide the text of a chat message.

If your deployment uses Enterprise Chat and
                                                						Email for multichannel functionality, you can use the reporting tool provided with that application to view more details about
                                          the task events.

| Type of Data | Data for Voice
                                          Tasks | Data for Nonvoice Tasks |
|---|---|---|
| Task direction | Task direction can be both incoming (agent receives a call) and
                                          outgoing (agent places a call). Note Calls placed by 
                                                   Outbound Option appear as incoming calls because of the manner in which the
                                                   Outbound Option Dialer places calls between agents and customers. | Note | Calls placed by 
                                                   Outbound Option appear as incoming calls because of the manner in which the
                                                   Outbound Option Dialer places calls between agents and customers. | Task direction is always incoming, and values of report
                                          fields pertaining to outgoing nonvoice tasks are set to null. |
| Note | Calls placed by 
                                                   Outbound Option appear as incoming calls because of the manner in which the
                                                   Outbound Option Dialer places calls between agents and customers. |
| Session ownership changes | The ownership of a voice task can change through the life of the call.
                                          Agents can transfer the call or conference in another agent. | The ownership of a nonvoice task routed to Unified CCE from third-party multichannel applications that use the Task
                                                					Routing APIs can change during the life of the task. Agents can transfer these tasks. Agents cannot conference these tasks, and supervisors
                                          cannot barge in or intercept the tasks. Nonvoice Enterprise Chat and
                                                						Email tasks do not change session ownership. These tasks
                                          cannot be transferred or conferenced and supervisors cannot barge into or
                                          intercept the task. Note While it is possible for a Enterprise Chat and
                                                            						Email agent to allow another agent to join a session and then drop the session, leaving the second agent and the caller in session
                                                      together, this is not the same as a voice call transfer. Unified CCE software interprets this scenario as two different sessions, one for the original agent and one for the second agent. Also, while Enterprise Chat and
                                                						Email agents can forward messages to other agents, this is not the same as a voice call transfer. Unified CCE interprets message forwarding as two different sessions, one for the original agent and one for the receiving agent. | Note | While it is possible for a Enterprise Chat and
                                                            						Email agent to allow another agent to join a session and then drop the session, leaving the second agent and the caller in session
                                                      together, this is not the same as a voice call transfer. Unified CCE software interprets this scenario as two different sessions, one for the original agent and one for the second agent. |
| Note | While it is possible for a Enterprise Chat and
                                                            						Email agent to allow another agent to join a session and then drop the session, leaving the second agent and the caller in session
                                                      together, this is not the same as a voice call transfer. Unified CCE software interprets this scenario as two different sessions, one for the original agent and one for the second agent. |
| Short
                                          calls | Voice calls are considered to be short
                                          calls if they disconnect within the time boundaries defined in the Agent Desk
                                          Settings for short tasks. | The Agent Desk Settings for short tasks do not apply to nonvoice tasks.  The concept of short calls is not applicable for
                                          these tasks. Values of report fields pertaining to short
                                          calls are set to zero. |
| Service Level | You determine which Service Level type you want to use
                                          for voice tasks. | For third-party multichannel applications that use the Task
                                                					Routing APIs, you determine the Service Level type you want to use. For Enterprise Chat and
                                                						Email , the Service Level is always set to "ignore
                                             abandoned calls" . |

| Note | Calls placed by 
                                                   Outbound Option appear as incoming calls because of the manner in which the
                                                   Outbound Option Dialer places calls between agents and customers. |
|---|---|

| Note | While it is possible for a Enterprise Chat and
                                                            						Email agent to allow another agent to join a session and then drop the session, leaving the second agent and the caller in session
                                                      together, this is not the same as a voice call transfer. Unified CCE software interprets this scenario as two different sessions, one for the original agent and one for the second agent. |
|---|---|

| Note | If your deployment uses Enterprise Chat and
                                                						Email for multichannel functionality, you can use the reporting tool provided with that application to view more details about
                                          the task events. |
|---|---|