---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-configuration-guide-pcce-b-admi-5922dd8837
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/configuration/guide/pcce_b_admin-and-config-guide-15_0_1/pcce_m_multichannel-routing_15_0.html
retrieved_at: 2026-08-25T01:21:02.465942+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

Updated: July 31, 2026

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

### Supported Route Requests for Enterprise Chat and
                                 						Email

CCE supports the following types of multichannel route requests when integrated with Enterprise Chat and
                                       						Email :

Web callback - A web callback request is one that does not involve Enterprise Chat and
                                             						Email . A customer clicks a button on a website that says, "Call me back." Then the caller and agent simply talk on the phone.

Text chat - The caller and agent can conduct
                                       a text chat session when a telephone call is not desired or not
                                       possible. They can both chat and collaborate on the web.

E-mail message - The customer and agent
                                       communicate using electronic mail.

### Application Request Routing with Enterprise Chat and
                                 						Email

Enterprise Chat and
                                       						Email routes requests to the Media Routing Peripheral gateway (MR-PG). The Media Routing Peripheral Interface Manager (MR-PIM)
                                 on the MR-PG provides a generic interface to queue and route requests. The MR-PIM communicates with the CallRouter, which
                                 runs a routing script to determine how best to handle the request.

CCE   uses a media class ID to identify the type of
                                 media or channel. A media class is a communication channel that is
                                 correlated to an application. Cisco_Voice is a predefined media class that is used for web and delayed callbacks requests and Packaged CCE inbound and outbound
                                    voice calls.

Each media class has at least one Media Routing Domain (MRD), which is
                                 a collection of skill groups associated with a medium.
                                 CCE uses the MRD to route a task to an agent who is associated
                                 with a skill group and a particular medium. Each MRD requires a Packaged CCE script, but it is possible to route requests from different MRDs
                                 using one script.

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

## Media Routing Domains

Media Routing Domains (MRDs) organize how requests for each communication medium, such as voice and email, are routed to agents.
                              For example, the Enterprise Chat and
                                    						Email uses a Packaged CCE MRD to route a task to an agent who is associated with a skill group or precision queue and a particular channel.

For Enterprise Chat and
                                    						Email , configure MRDs in Configuration Manager. Associate each ECE MRD with the application path for the corresponding ECE application
                              instance. For each Agent PG, create one ECE application path and add all applicable MRD-peripheral combinations for that Agent
                              PG to the application-path member list. Do not add the Cisco_Voice MRD to the ECE application path.

For custom multichannel applications that use the Task Routing APIs, configure MRDs in Unified CCE Administration.

For Digital Channel tasks initiated from Webex Connect, you can create MRDs using either the Media Routing Domain List tool
                              in Configuration Manager or Unified CCE Administration. MRDs created through Unified CCE Administration are automatically
                              associated with the system-defined application paths. If you create an MRD using the Media Routing Domain List tool, explicitly
                              associate it with the appropriate system-defined application path.

For every agent peripheral gateway, a system-defined application path with a suffix "UQ.Desktop" is created for Webex Connect
                              Digital Channels. There is also an associated system-defined application called UQ.Desktop that automatically gets created
                              in the sytem and identifies the Cisco Finesse server as a client to the Agent PG, to control Agent states in MRDs created
                              for digital channels. The first number in the application path identifies the Logical Controller ID of the Agent PG. An example
                              of the system-defined application path is 5000.UQ.Desktop .

Do not use the UQ.Desktop application path as the ECE application path. ECE MRDs must be associated with the application path belonging to the corresponding
                                          ECE application instance.

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

Optionally, select the Enterprise Skill Group that includes the appropriate skill groups to cover all media routing domain cases for the selected Agent.

Step 6

Optionally, select the Enterprise Route that has an appropriate collection of routes, or the Route , matching the agent and media routing domain.

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

## Example Universal Queue Scripts

You can design scripts to route contacts from different media in a
                              Universal Queue environment.

These scripts are only examples; your company's needs may differ.

For more information about Task Routing with third-party multichannel applications or Enterprise Chat and
                                    						Email , see the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### Selection of Agents from Skill Groups

The following script example shows how contacts from different
                                 channels can be routed to the Longest Available Agents in skill groups
                                 that are specific to the different channels:

You schedule this script to run for Call Types associated with
                                 contacts from the different channels. The script then selects the
                                 Longest Available Agent from the skill group in the Media Routing Domain
                                 for that channel. The agents may be logged in to different Media Routing
                                 Domains and working with contacts from different channels; the Router
                                 determines an agent's availability across channels.

### Categorization by Media Routing Domain with Skill Groups

The following script example shows how contacts can be categorized by
                                 Media Routing Domain, then queued to skill groups specific to that Media
                                 Routing Domain:

You would schedule this script to run for Call Types associated with
                                 contacts from the different channels. The script then uses the Media
                                 Routing Domain node to detect the MRD of the contact and branches to a
                                 Queue to Skill Group node that specifies skill groups specific to that
                                 MRD.

### Categorization by Media Routing Domain with Precision Queues

The following script example shows how contacts can be categorized by
                                 Media Routing Domain, then queued to precision queues specific to that Media
                                 Routing Domain:

You would schedule this script to run for Call Types associated with
                                 contacts from the different channels. The script then uses the Media
                                 Routing Domain node to detect the MRD of the contact and branches to a
                                 Queue to Precision Queue node that a precision queue specific to that
                                 MRD.

### Script That Queues to Agents

The following script example shows how contacts from different
                                 channels can be queued to agents:

You would schedule this script to run for Call Types associated with
                                 contacts from the different channels. In the Queue to Agent node, each
                                 row defined for an agent also contains a Media Routing Domain selection.
                                 The script queues the contact to the agent with the selected MRD that
                                 matches the MRD of the contact.

### RONA and Transfer Script

This example only applies to tasks submitted by third-party multichannel applications that use the Task
                                       					Routing APIs. This example script shows the call priority increase if the service requested is 2 (TRANSFER).

If the Call ServiceRequested call variable is set to 2 (TRANSFER)   the call enters the Queue Priority node.  The Queue Priority
                                 of the call is increased so that it is handled before any other calls in the queue. The Queue Priority node sends the call
                                 to the Queue to Skill Group   node. If the Call ServiceRequested call variable is not set to 2 (TRANSFER), the call enters
                                 the Queue to Skill Group node.

### Estimated Wait Time Script

This example only applies to tasks submitted by third-party multichannel applications that use the Task
                                       					Routing APIs.

Scripts for estimated wait time include:

A Set Variable Node to set the estimated wait time.

A Run External Script node to apply a Network VRU script that returns the estimated wait time to the customer.

Set Variable
                                    		  (Call.Estimated Wait Time) node: Set the estimated wait 
                                 		time as follows:

From the Set
                                       			 Variable node, select Call from the Object type drop-down menu.

From the Variable drop-down menu, choose Estimated Wait Time() .

You can then work with the Formula Editor to use the default estimated wait value or create a formula and use your own value.

Click Formula Editor , and do either of the following:

To use the default estimated wait value, click the Built-In Functions tab and choose EstimatedWaitTime()

To create a formula and use your own value, click the Variables tab and choose an entry in the Object type list and an entry
                                             in the Object list. Then double-click a variable in the Variable list.

Run Ext Script node: Apply the Network VRU script as follows:

Click the Queue
                                       			 tab.

Click Run External
                                          				Script .

Click inside the
                                       			 script. A Run External Script node appears.

Double-click the
                                       			 node and choose the Network VRU script from the list; then click OK .

The call
                                       			 variable Estimated Wait Time now contains a value in the EstimatedWaitTime
                                       			 field and can be passed to peripherals.

Note that a Run External Script node is required to send the EstimatedWaitTime to SocialMiner .

## Example Enterprise Chat and
                              						Email Scripts

For example Enterprise Chat and
                                    						Email scripts, see the Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

| Note | Do not use the UQ.Desktop application path as the ECE application path. ECE MRDs must be associated with the application path belonging to the corresponding
                                          ECE application instance. |
|---|---|

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
| Step 5 | Optionally, select the Enterprise Skill Group that includes the appropriate skill groups to cover all media routing domain cases for the selected Agent. |
| Step 6 | Optionally, select the Enterprise Route that has an appropriate collection of routes, or the Route , matching the agent and media routing domain. |
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