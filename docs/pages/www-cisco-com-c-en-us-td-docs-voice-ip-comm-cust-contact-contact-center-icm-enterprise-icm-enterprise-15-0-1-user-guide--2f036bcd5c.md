---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-guide--2f036bcd5c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/guide/ucce_b_scripting-and-media-routing-guide-for-cisco-unified-icm-contact-center-enterprise-release-15_0/multichannel_routing.html
retrieved_at: 2026-08-16T20:36:35.697322+00:00
---

Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Multichannel Routing

## Chapter: Multichannel Routing

# Multichannel Routing

## Overview of Multichannel Services

When your system is integrated with multichannel features, you write routing scripts to route contacts that these features
                              handle. Multichannel features include Enterprise Chat and
                                    						Email , and third-party multichannel applications that use the Task
                                    					Routing APIs.

## Enterprise Chat and
                              						Email

You can configure CCE deployments with Enterprise Chat and
                                    						Email to use independent media queues, in which an agent can handle tasks for a single media channel. You can also use Task
                                    					Routing , in which an agent can handle tasks for several media channels.

### Supported Route Requests for ECE Web Request

Unified CCE supports the following types of multichannel route requests when integrated with ECE :

Web callback - A web callback request is a request that does not involve ECE . You click a button on a website that says, "Call me back." Then the caller and agent simply talk on the phone.

Text chat - The caller and agent can conduct a text chat session when a phone call is not desired or not possible. They can both chat
                                       and collaborate on the web.

Email message - The customer and agent communicate using electronic mail.

### Application Request Routing with ECE Web Request

The ECE routes requests to a Media Routing Peripheral gateway (MR-PG). The Media Routing Peripheral Interface Manager (MR-PIM) on
                                 the MR-PG provides a generic interface to queue and route requests. The MR-PIM communicates with the Router, which runs a
                                 routing script to determine how best to handle the request.

Unified CCE uses a media class ID to identify the type of media or channel. A media class is a communication channel that
                                 correlates to an application. Following are the predefined media classes in Unified CCE:

Cisco_Chat - chat requests

Cisco_Voice - web and delayed callbacks requests, and basic Unified CCE inbound and outbound voice calls

Cisco_Email - email requests

Each media class has at least one Media Routing Domain (MRD), which is a collection of skill groups and services that are
                                 associated with a medium. The Unified CCE uses the MRD to route a task to an agent who is associated with a skill group and
                                 a particular medium. Each MRD requires a Unified CCE script, but it is possible to route requests from different MRDs using
                                 one script.

### Synchronized Agents and Skill Groups for ECE

Agents are common across the multichannel software, but skill groups are application-specific. You can create agents using ECE or in contact center enterprise solutions and share the agents across applications. When agents or skill groups are created
                                 in ECE , they are simultaneously created in contact center enterprise solutions. If an agent is created in contact center enterprise
                                 solutions, you must enable the agent in ECE before the agent can work on those applications.

Only create, modify, or delete ECE skill groups in ECE . Skill groups are application-specific. When you create a skill group in ECE , the skill group is simultaneously created in the contact center enterprise solutions. But, you cannot enable that skill
                                 group in the core contact center enterprise applications.

### Independent Media Queues for ECE

You can configure the multichannel software to route all media through independent queues that are defined by media class.
                                 You can configure agents to log in to only one media type to take either email, text chat, or voice. In this configuration,
                                 requests are queued only to agents who have signed in to the corresponding media application.

You can use independent media queues in both the Unified CCE and ACD environments.

## Task
                              					Routing

Task
                                    					Routing describes the system's ability to route requests from different media channels to agents who work with customer contacts
                              in multiple media. Routing scripts can send requests to agents based on business rules regardless of the media channel from
                              which the request came. For example, based on an agent's skills and current tasks, Unified CCE can route phone, chat, and
                              email message requests to an agent who works with all these media. The agent can switch media on a task-by-task basis.

You can set up
                              		  routing scripts so that multichannel tasks are assigned to the longest
                              		  available agent in a skill group or precision queue in same Media Routing
                              		  Domain as the task. You can also prioritize multichannel tasks using skill
                              		  group and precision queue routing, as you would voice calls.

Because Task
                                    					Routing must coordinate an agent's work on multiple tasks across different channels, Task
                                    					Routing requires that Unified ICM have complete control over how agents are assigned tasks. Therefore, Task
                                    					Routing requires that you use the Unified ICM in a Unified CCE environment. Task
                                    					Routing is not supported in legacy ACD environments.

## Digital Routing using Webex Connect

You can configure the Contact Center Enterprise (CCE) deployments with Webex Connect using the Digital Routing service, in
                           which agents can handle tasks for several digital channels such as SMS, chat, and email.

### Digital Routing Task Requests

The Digital Routing service that is installed on Cloud Connect routes the digital channel tasks to the router through a Media
                              Routing Peripheral Gateway (MR-PG). The Media Routing Peripheral Interface Manager (MR-PIM) on the MR-PG provides a generic
                              interface to queue and route requests. The MR-PIM communicates with the Router, which runs a routing script to determine how
                              best to handle the request. You must have certain mandatory ECC variables defined in CCE for the Digital Routing tasks to
                              be routed successfully. For the list of mandatory ECC Variables that must be configured for the Digital Routing Tasks, see ECC Variables for Digital Routing Tasks . For instructions about how to add the ECC variables in CCE, see the Define ECC variables section in the Cisco Unified Contact Center Enterprise Features Guide .

If you are using ECC payloads, you must associate the ECC payloads that you created for the Digital Routing service to the
                              Network VRU using the Network VRU Explorer tool in the Unified CCE Configuration Manager. You must then associate the Network VRU to the MR-PG using the PG Explorer tool in the Unified CCE Configuration Manager. For instructions about how to associate ECC payloads to Network VRU and the Network VRU to the MR-PG,
                              see the Configure MR PG section in the Configuration Guide for Cisco Unified ICM Enterprise .

In case you use different ECC payloads, that is one for receiving task context data from MR-PG to the Router and another to
                              route the tasks to Finesse through Agent PG, ensure that the ECC variables defined for Digital Routing tasks are part of both
                              the ECC payloads. If you use the system's "Default" payload, ensure that the ECC variables are part of the "Default" payload.
                              These ECC variables carry task metadata that the Agent Desktop uses to identify a task as the digital channel task and to
                              interact with Webex Engage to load the media pane. If you do not define these variables and add them in the Unified CCE Administration
                              portal, the tasks do not appear in the Agent Desktop correctly. You can create and modify ECC payloads in the Configuration
                              Manager > List Tools > Expanded Call Variable Payload List tool. For more information about ECC variables and payloads , see Expanded Call Context (ECC) Variables .

### ECC Variables for Digital Routing Tasks

This section provides the list of Enterprise Call Control (ECC) Variables that you must configure for the Digital Channel
                                 interaction. All ECC variables are of type scalar and they are case-sensitive.

Mandatory ECC Variables are present only in the default ECC payload. If you use custom ECC payload in Media Routing Peripheral
                                             Interface Manager (MR PIM), you must add mandatory ECC variables to that payload and associate the payload to a Network VRU.

To add the payload to Network VRU, do the following:

In the Configuration Manger > Network VRU Explorer tool, create a new Network VRU for Digital Routing.

In the ECC Payload configuration, set the non-default ECC Payload list that contains the mandatory ECC variables.

Choose PG Explorer > Peripheral > Digital Channels MR PIM .

Click Advanced tab.

Set the Network VRU configuration with the newly created Digital Channels Network VRU.

Click Save .

Variable

Table Size

Length

Mandatory / Optional

Used to hold the FQDN of either the publisher node or the subscriber node of Cloud Connect. The FQDN denotes the Digital Routing
                                             service node that injected the task into CCE.

1 1 character + the length of the Cloud Connect FQDN.

Mandatory

Used to hold the FQDN of either the publisher node or the subscriber node of Cloud Connect. The FQDN denotes the peer node
                                             of the Digital Routing service, which can be used as a backup, in case the Primary node is unavailable.

1 character + the length of the Cloud Connect FQDN.

Mandatory

Used to hold the Conversation ID of Webex Engage, which the Webex Connect injects. The Cisco Finesse uses this conversation
                                             ID to load the media in the Manage Digital Channels gadget.

16 characters

Mandatory

Used to display the customer name in the pop-over notification that an agent views when a task is received in the Manage Digital
                                             Channels gadget.

Up to a maximum of 210 characters.

Optional

Used to populate the media channel name for the task, if you configure and add this ECC variable in the Unified Contact Center Enterprise Management portal. See the Define ECC variables section in the Cisco Unified Contact Center Enterprise Features Guide .

This is typically required if you have mapped more than one Digital Routing media channel to the same MRD but still want unique
                                             task icons to appear on the agent desktop. For example, in CCE, the system-defined media channels, chat and SMS are both mapped
                                             to the same MRD. If there is a 1:1 mapping between the media channel and MRD, the system automatically identifies the icon
                                             to be displayed on the desktop based on the media channel with which the task was associated.

8 character

Optional

## Media Routing Domains

Media Routing Domains (MRDs) organize how requests for each communication medium, such as voice and email, are routed to agents.
                              For example, the Enterprise Chat and
                                    						Email uses a Unified CCE MRD to route a task to an agent who is associated with a skill group or precision queue and a particular channel.

For Enterprise Chat and
                                    						Email , configure MRDs in Configuration Manager. For custom multichannel applications that use the Task Routing APIs, configure MRDs in Unified CCE Administration.

For Digital Channel tasks that are initiated from Webex Connect, you can create MRDs either using the Media Routing Domain
                              List tool in Configuration Manager, or through Unified CCE Administration tool. If you create the MRDs through the Unified
                              CCE Administration portal, the MRDs get automatically associated to the system-defined application paths. If you have created
                              the MRDs using the Media Routing Domain List tool in Configuration Manager, you must explicitly associate the MRD with the
                              application path.

For every agent peripheral gateway, there is a system-defined application path that gets created with a suffix "UQ.Desktop".
                              There is also an associated system-defined application called UQ.Desktop that automatically gets created in the sytem and
                              identifies the Cisco Finesse server as a client to the Agent PG, to control Agent states in MRDs created for digital channels.
                              The first number in the application path identifies the Logical Controller ID of the Agent PG. An example of the system-defined
                              application path is 5000.UQ.Desktop .

### Media Routing Domains and Interruptibility

When you configure MRDs, you indicate whether tasks for the MRD are
                                 interruptible. If the MRD is not interruptible, an agent working on
                                 tasks for that MRD is not assigned tasks from other MRDs. If the MRD is
                                 interruptible, the agent may be assigned tasks from another MRD.

Typically, tasks in which the agent and customer interact synchronously, such as voice calls and chats, are not interruptible.
                                 Email messages are typically interruptible because contact with the customer is asynchronous. Therefore, an agent responding
                                 to an email message may be interrupted by a phone call or chat session.

Whenever there are changes to the MRD interruptibility settings, the agent must log out and then log in to the desktop for
                                             the changes to take effect.

### Use Media Routing
                           	 Domains to Categorize Contacts

You can categorize contacts based on the MRD of the route request.

For example, you can have different MRDs for email and chat. You can have a single script for both types of requests that
                                 branches so that it routes email messages and chats to different targets.

For multichannel tasks submitted by applications using the Task
                                                   					Routing APIs, Unified CCE determines the MRD based on the dialed number/script selector in the task request.

Use the Media Routing Domain node (in the Routing tab of the Palette).

Insert targets and connections from the MRD node before you define the node's properties.

Following is the properties dialog box for the Media Routing Domain node:

Step 1

To associate an MRD with a branch, select the branch:

Click Add .

Choose an MRD from the drop-down list.

Step 2

To delete a branch, select it and click Delete .

Step 3

To rename a branch, select it, click Rename , and type the new name.

Step 4

You can define a branch as Otherwise by selecting the branch and clicking Make Otherwise . Execution follows this branch if none of the specified time ranges apply. You can specify only one Otherwise branch for
                                          the node.

## Pick / Pull Node

The Pick / Pull node is available from the Routing tab Object Palette .

Pick / Pull node verifies that the route request is a valid pick or pull request for the specified MRD. The node checks that serviceRequested is one of the following:

4 = ROUTE_SERVICE_REQUEST_PICK_EXT_QUEUE

5 = ROUTE_SERVICE_REQUEST_PULL_EXT_QUEUE

6 = ROUTE_SERVICE_REQUEST_PICK_UCCE_AGENT

7 = ROUTE_SERVICE_REQUEST_TRANSFER_PICK

For these values, the script proceeds and terminates after the pick or pull is completed. For any other value of serviceRequested , the request flows through the node's failure branch. Check the error code in VRUStatus .

The node provides real-time monitoring of the following:

Pick successes.

Pull successes.

Pick errors.

Pull errors.

The following meters are applicable for the Pick/Pull node.

Pick meter - Displays the number of nonvoice task pick requests that were successful.

Pull meter - Displays the number of nonvoice task pull requests that were successful.

Pick error meter - Displays the number of nonvoice task pick requests that failed.

Pull error meter - Displays the number of nonvoice task pull requests that failed.

```
HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\ICM\ucce\RouterA\Router\CurrentVersion\Configuration\Config.
```

The Registry key is dynamic and doesn’t require a restart of the router, for changes to take effect. The default value is
                                          0 or disabled. To enable the Registry key, set the value to 1.

## Skill Group and Precision Queue Routing for Nonvoice Tasks

Routing to skill groups and precision queues is largely the same for voice calls and nonvoice tasks. However, the way that
                              contact center enterprise distributes tasks has the following implications for agents who can handle multiple concurrent tasks:

Precision queues —In precision queue routing, Unified CCE assigns tasks to agents in order of the precision queue steps. Unified CCE assigns tasks to agents who match the attributes for step one, up to their task limit, until all those agents are busy. Unified CCE then assigns tasks to agents who match attributes for step two, and so on. If you configure agents to handle three concurrent
                                    tasks, Unified CCE assigns three tasks to each agent in the first step. It then moves on to the second step and assigns any remaining tasks
                                    to those agents.

Overflow skill groups —Routing scripts can specify a preferred skill group and an overflow skill group. Unified CCE assigns tasks to all agents in the preferred skill group, up to their task limit, before assigning any tasks in the overflow
                                    skill group. If you configure agents to handle three concurrent tasks, Unified CCE assigns three tasks to each agent in the preferred skill group. It then moves on to the overflow skill group and assigns
                                    any remaining tasks to those agents.

The number of available slots is an important factor in the Longest Available Agent (LAA) calculation.

The number of available slots = The maximum concurrent task limit for the MRD that an Agent has logged into - Current tasks being handled by the Agent or routed to the Agent.

If there are multiple skill groups that are part of the queue node, then the skill group that has the higher LAA is picked.
                                                Then, the agents within the picked skill group (or the Precision Queue) who have the highest number of available slots for
                                                non-voice tasks get prioritised.

Agents with the same number of available slots get prioritized based on the time in the available state or the LAA mechanism.

## Queue to Agent Node

You can queue a contact directly to an agent by using the Queue to Agent node (in the Queue tab of the Palette).

You can change the Queue to Agent type to:

Specify an agent directly

Select an agent by expression

## Change Queue to Agent Type

Step 1

In the Queue to Agent properties dialog box, click Change . The Queue Agent Type dialog box opens:

Step 2

To select a specific agent, select Explicit agent references .

Step 3

To select and agent by an expression, select Lookup agent references by expression .

Step 4

Select a Priority between 1 (the highest) and 20 (the lowest).

Step 5

Optionally, select Enable target requery .

## Specify an Agent Directly

Following is the properties dialog box of the Queue to Agent node when you select to specify agents directly:

To specify agents directly:

Step 1

If necessary, change the Queue to Agent type to Explicit agent references .

Step 2

In the Agent column, select an agent.

Step 3

In the Media Routing Domain column, select the media routing domain for the selected agent.

Step 4

In the Skill Group column, select the skill group for the selected agent and media routing domain.

Step 5

In the Route column, select the route for the selected agent and media routing domain.

Step 6

Optionally, select Queue if agent not logged in , to have the contact queued to the agent even if the agent is not currently logged in.

Step 7

To test the data you entered, click Validate .

Step 8

Optionally, modify Connection Labels .

## Select an Agent by an Expression

Following is the properties dialog box of the Queue to Agent node when you select to use an expression:

To specify agents by expression:

Step 1

If necessary, change the Queue to Agent type to Lookup agent references by expression .

Step 2

In the Peripheral column, to choose an agent by Peripheral number, choose a peripheral and provide a formula in the Agent Expression that translates
                                       to the Agent’s Peripheral number. If no peripheral is chosen, the agent expression should translate to the SkillTargetID or
                                       Enterprise Name of the agent.

Step 3

In the Agent Expression column, provide a formula using the formula editor that translates to the agent’s Peripheral number or SkillTargetID or agent
                                       Enterprise Name. To choose a peripheral (in Peripheral) and provide a formula that translates to an agent’s Peripheral number.

The Peripheral column controls how the AgentExpression column is evaluated as an ICM ID. However, if you select a Peripheral
                                                      from the Peripheral column, then the Agent Expression column is evaluated as an Agent Peripheral number.

Step 4

Optionally, in the Consider if column, enter the formula that evaluates to true for the target when the ICM system runs the Queue to Agent node, or that
                                       target will not be selected. For help in creating a formula, put the cursor in this field and then click the Formula Editor button.

Step 5

Select the Enterprise Skill Group that includes the appropriate skill groups to cover all media routing domain cases for the selected Agent.

Step 6

Select the Enterprise Route that has an appropriate collection of routes, or the Route , matching the agent and media routing domain.

If you do not select either an Enterprise Route or a Route , the following error message appears:

If you select both Enterprise Route and Route , the following error message appears:

The specified Enterprise Route or Route is used to send the call to an agent.

Step 7

Optionally, select Queue if agent not logged in , to have the contact queued to the agent even if the agent is not currently logged in.

Step 8

To test the data you entered, click Validate .

Step 9

Optionally, modify connection labels.

## RONA and Transfer Scripting for Task
                              					Routing and Digital Routing

Tasks submitted by third-party multichannel applications that use the Task
                                                      					Routing APIs.

Tasks submitted by Webex Connect that use the Digital Routing APIs.

The ServiceRequested call variable is set when tasks are transferred or RONA. You can determine the value of the ServiceRequested call variable in an If node in the routing script. Based on the value of this field, the script can take different actions. For example, the script
                              can raise the priority of the task so that it goes to the front of the queue.

The relevant ServiceRequested values are:

2: This value identifies a transferred task.

3: This value identifies a RONA task.

## Estimated Wait Time Scripting for Task
                              					Routing and Digital Routing

Tasks submitted by third-party multichannel applications that use the Task
                                                      					Routing APIs.

Tasks submitted by Webex Connect that use the Digital Routing APIs.

Customers submitting a task request might want to know approximately how long they will wait for an agent. You can configure
                              the routing script to provide the customer with an estimate of the wait time. The estimated wait time is calculated once,
                              when the task enters the queue. The time is not updated as the position in the queue changes.

The default estimated wait time algorithm is based on a running five minute window of the rate of tasks leaving the queue.
                              Any tasks that are routed or abandoned during the previous 5 minutes are considered as part of the rate leaving queue. For
                              Precision Queues, the rate leaving the queue represents the rate at which tasks are delivered or abandoned from the entire
                              precision queue, not any individual Precision Queue steps. The algorithm computes the wait time for each of the queues against
                              which the task is queued (Skill Groups or Precision Queues) and then returns the minimum estimated wait time.

Queue to Agent is not
                                          		supported.

While the queue
                              		builds, the small number of tasks in the queue makes the estimated wait time
                              		less accurate and the value fluctuates rapidly. As the queue operates with more
                              		tasks over time, the estimated wait time is more accurate and consistent.

Scripts for estimated wait time include:

A Set Variable node, Call.EstimatedWaitTime to set the estimated wait time.

A Run External Script node to apply a Network VRU script that returns the estimated wait time to the customer.

| Note | Mandatory ECC Variables are present only in the default ECC payload. If you use custom ECC payload in Media Routing Peripheral
                                             Interface Manager (MR PIM), you must add mandatory ECC variables to that payload and associate the payload to a Network VRU. To add the payload to Network VRU, do the following: In the Configuration Manger > Network VRU Explorer tool, create a new Network VRU for Digital Routing. In the ECC Payload configuration, set the non-default ECC Payload list that contains the mandatory ECC variables. Choose PG Explorer > Peripheral > Digital Channels MR PIM . Click Advanced tab. Set the Network VRU configuration with the newly created Digital Channels Network VRU. Click Save . |
|---|---|

| Variable | Table Size | Length | Mandatory / Optional |
|---|---|---|---|
| user_DR_Primary | Used to hold the FQDN of either the publisher node or the subscriber node of Cloud Connect. The FQDN denotes the Digital Routing
                                             service node that injected the task into CCE. | 1 1 character + the length of the Cloud Connect FQDN. | Mandatory |
| user_DR_Backup | Used to hold the FQDN of either the publisher node or the subscriber node of Cloud Connect. The FQDN denotes the peer node
                                             of the Digital Routing service, which can be used as a backup, in case the Primary node is unavailable. | 1 character + the length of the Cloud Connect FQDN. | Mandatory |
| user_DR_MediaResourceID | Used to hold the Conversation ID of Webex Engage, which the Webex Connect injects. The Cisco Finesse uses this conversation
                                             ID to load the media in the Manage Digital Channels gadget. | 16 characters | Mandatory |
| user_DR_CustomerName | Used to display the customer name in the pop-over notification that an agent views when a task is received in the Manage Digital
                                             Channels gadget. | Up to a maximum of 210 characters. | Optional |
| user_DR_MediaChannelName | Used to populate the media channel name for the task, if you configure and add this ECC variable in the Unified Contact Center Enterprise Management portal. See the Define ECC variables section in the Cisco Unified Contact Center Enterprise Features Guide . This is typically required if you have mapped more than one Digital Routing media channel to the same MRD but still want unique
                                             task icons to appear on the agent desktop. For example, in CCE, the system-defined media channels, chat and SMS are both mapped
                                             to the same MRD. If there is a 1:1 mapping between the media channel and MRD, the system automatically identifies the icon
                                             to be displayed on the desktop based on the media channel with which the task was associated. | 8 character | Optional |

| Note | Whenever there are changes to the MRD interruptibility settings, the agent must log out and then log in to the desktop for
                                             the changes to take effect. |
|---|---|

| Note | For multichannel tasks submitted by applications using the Task
                                                   					Routing APIs, Unified CCE determines the MRD based on the dialed number/script selector in the task request. |
|---|---|

| Note | A branch can include multiple MRDs, but you can associate a single MRD with only one branch. |
|---|---|

| Step 1 | To associate an MRD with a branch, select the branch: Click Add . Choose an MRD from the drop-down list. |
|---|---|
| Step 2 | To delete a branch, select it and click Delete . |
| Step 3 | To rename a branch, select it, click Rename , and type the new name. |
| Step 4 | You can define a branch as Otherwise by selecting the branch and clicking Make Otherwise . Execution follows this branch if none of the specified time ranges apply. You can specify only one Otherwise branch for
                                          the node. |

| Note | All Pick / Pull routing works for agents in the Ready or Available state. To be able to do this in Not Ready state, enable the Registry key. The Registry key that needs to be enabled on the CCE Router is EnablePickPullWhileInNotReady.
                                          This is located under the following registry hive on the CCE Router VM HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems,Inc.\ICM\ucce\RouterA\Router\CurrentVersion\Configuration\Config. The Registry key is dynamic and doesn’t require a restart of the router, for changes to take effect. The default value is
                                          0 or disabled. To enable the Registry key, set the value to 1. |
|---|---|

| Note | The number of available slots is an important factor in the Longest Available Agent (LAA) calculation. The number of available slots = The maximum concurrent task limit for the MRD that an Agent has logged into - Current tasks being handled by the Agent or routed to the Agent. If there are multiple skill groups that are part of the queue node, then the skill group that has the higher LAA is picked.
                                                Then, the agents within the picked skill group (or the Precision Queue) who have the highest number of available slots for
                                                non-voice tasks get prioritised. Agents with the same number of available slots get prioritized based on the time in the available state or the LAA mechanism. |
|---|---|

| Step 1 | In the Queue to Agent properties dialog box, click Change . The Queue Agent Type dialog box opens: Figure 3. Queue Agent Type |
|---|---|
| Step 2 | To select a specific agent, select Explicit agent references . |
| Step 3 | To select and agent by an expression, select Lookup agent references by expression . |
| Step 4 | Select a Priority between 1 (the highest) and 20 (the lowest). |
| Step 5 | Optionally, select Enable target requery . |

| Step 1 | If necessary, change the Queue to Agent type to Explicit agent references . |
|---|---|
| Step 2 | In the Agent column, select an agent. |
| Step 3 | In the Media Routing Domain column, select the media routing domain for the selected agent. |
| Step 4 | In the Skill Group column, select the skill group for the selected agent and media routing domain. |
| Step 5 | In the Route column, select the route for the selected agent and media routing domain. |
| Step 6 | Optionally, select Queue if agent not logged in , to have the contact queued to the agent even if the agent is not currently logged in. |
| Step 7 | To test the data you entered, click Validate . |
| Step 8 | Optionally, modify Connection Labels . |

| Step 1 | If necessary, change the Queue to Agent type to Lookup agent references by expression . |
|---|---|
| Step 2 | In the Peripheral column, to choose an agent by Peripheral number, choose a peripheral and provide a formula in the Agent Expression that translates
                                       to the Agent’s Peripheral number. If no peripheral is chosen, the agent expression should translate to the SkillTargetID or
                                       Enterprise Name of the agent. |
| Step 3 | In the Agent Expression column, provide a formula using the formula editor that translates to the agent’s Peripheral number or SkillTargetID or agent
                                       Enterprise Name. To choose a peripheral (in Peripheral) and provide a formula that translates to an agent’s Peripheral number. Note The Peripheral column controls how the AgentExpression column is evaluated as an ICM ID. However, if you select a Peripheral
                                                      from the Peripheral column, then the Agent Expression column is evaluated as an Agent Peripheral number. | Note | The Peripheral column controls how the AgentExpression column is evaluated as an ICM ID. However, if you select a Peripheral
                                                      from the Peripheral column, then the Agent Expression column is evaluated as an Agent Peripheral number. |
| Note | The Peripheral column controls how the AgentExpression column is evaluated as an ICM ID. However, if you select a Peripheral
                                                      from the Peripheral column, then the Agent Expression column is evaluated as an Agent Peripheral number. |
| Step 4 | Optionally, in the Consider if column, enter the formula that evaluates to true for the target when the ICM system runs the Queue to Agent node, or that
                                       target will not be selected. For help in creating a formula, put the cursor in this field and then click the Formula Editor button. |
| Step 5 | Select the Enterprise Skill Group that includes the appropriate skill groups to cover all media routing domain cases for the selected Agent. |
| Step 6 | Select the Enterprise Route that has an appropriate collection of routes, or the Route , matching the agent and media routing domain. If you do not select either an Enterprise Route or a Route , the following error message appears: Figure 6. No Enterprise Route or Route Chosen If you select both Enterprise Route and Route , the following error message appears: Figure 7. Both an Enterprise Route and a Route Chosen The specified Enterprise Route or Route is used to send the call to an agent. |
| Step 7 | Optionally, select Queue if agent not logged in , to have the contact queued to the agent even if the agent is not currently logged in. |
| Step 8 | To test the data you entered, click Validate . |
| Step 9 | Optionally, modify connection labels. |

| Note | The Peripheral column controls how the AgentExpression column is evaluated as an ICM ID. However, if you select a Peripheral
                                                      from the Peripheral column, then the Agent Expression column is evaluated as an Agent Peripheral number. |
|---|---|

| Note | This section applies to the following: Tasks submitted by third-party multichannel applications that use the Task
                                                      					Routing APIs. Tasks submitted by Webex Connect that use the Digital Routing APIs. |
|---|---|

| Note | This section applies to the following: Tasks submitted by third-party multichannel applications that use the Task
                                                      					Routing APIs. Tasks submitted by Webex Connect that use the Digital Routing APIs. |
|---|---|

| Note | Queue to Agent is not
                                          		supported. |
|---|---|