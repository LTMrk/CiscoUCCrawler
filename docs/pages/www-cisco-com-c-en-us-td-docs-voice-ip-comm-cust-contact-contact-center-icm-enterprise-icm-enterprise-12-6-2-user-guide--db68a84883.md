---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-guide--db68a84883
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/guide/ucce_b_scripting-and-media-routing-guide_1262/ucce_b_scripting-and-media-routing-guide_chapter_0100.html
retrieved_at: 2026-08-16T20:31:44.830928+00:00
---

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

# Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

Updated: November 21, 2022

Chapter: Selection of Routing Targets

## Chapter: Selection of Routing Targets

# Selection of Routing Targets

## Routing Targets

After defining how a script is used to categorize contacts, you typically
                              use the nodes available in Script Editor to specify how the contact is to be
                              routed to a target. By selecting routing targets, you determine the
                              destination for contacts.

A routing target is an entity to which the system can route a contact.
                              The routing target receives the contact and processes it accordingly.

Peripheral-level skill targets include:

Agents

Skill groups

There are two types of routing targets: Skill targets and Network targets.

## Routes

A value returned by a routing script that maps to a target at a
                              peripheral, such as a service, skill group, agent, or translation route to a
                              label.

## Translation Routes

A translation route is a target at a peripheral that does not map to a
                              specific service, skill group, or agent. When a contact arrives with the
                              trunk group and DNIS that correspond to a translation route, the Peripheral
                              Gateway (PG) is responsible for determining the ultimate target.

When
                              Unified ICM routes a call to a translation route, it sends a message to the
                              PG. In this message the PG receives the call context from the Router, including  the ultimate target and further instructions
                              for
                              the PG.  This enables the PG to seamlessly pass information set or retrieved in the Routing script to the PIM/peripheral as
                              well as to CTI clients. For example, the PG might be instructed to coordinate with a host
                              computer so that the caller's account number appears on the teleset of
                              the agent who picks up the call.

## Target Sets

A target set is a list of possible targets. During script processing, the
                              actual target is chosen from the set by the preceding node on the script
                              branch, a Select Node or Distribute Node.

## Skill Targets

A skill target is an entity at a peripheral or in the enterprise to which
                              Unified ICM can route a contact. There are two types of skill targets: Peripheral-level skill targets and Enterprise-level skill targets .

Peripheral-level skill targets include:

Agents

Skill groups

Services

Enterprise-level skill targets include:

Enterprise skill groups

Enterprise services

## Agent Routing Nodes

The following nodes available for agent
                              routing:

Queue to Agent Node. For more information, see Specify an Agent Directly

Agent to Agent Node. For more information, see Transfer Calls from Agents to Agents

Agent Node.

### Define Agent Node Properties

- Selecting the target by
                                    			 rules (Select node)

- Distributing contacts to
                                    			 targets in the set (Distribute node)

- A combination of selecting
                                    			 the target and distributing contacts (Route Select node)

Following is the Properties dialog box of the Agent node:

Step 1

For each agent in the target set the following:

In the Agent column, for each row used, select the agent to
                                                				  which the contact can be routed. You can use the drop-down list for each table
                                                				  cell, or select multiple agents by clicking Add Targets and using the dialog box that opens to select
                                                				  multiple agents.

In the Route column, select the route that maps to a specific
                                                				  target at the peripheral.

Optionally, in the Translation Route column, select a
                                                				  translation route.

Step 2

Optionally, check Allow connection for each target to have an
                                          			 output terminal appear to the right of each individual target defined in the
                                          			 node. Control passes through this terminal when the associated target is
                                          			 chosen. When the script terminates, the route for the selected agent is still
                                          			 used.

Step 3

Click Validate to check whether the targets you defined are valid.
                                          			 Correct any errors that are flagged.

Step 4

Optionally, add connection labels.

## Define Set of Skill Groups to Receive the Contact

You define a set of
                           		skill groups that can receive the contact using the Skill Group node in the
                           		Targets tab of the Palette.

You can specify the skill groups in the set in  two ways:

Select Explicit target references to   specify static skill group configurations, including the Skill Group, Route, and, optionally, a Translation Route. See Define Skill Groups by Explicit Target Reference .

Select Lookup target references by expression to enter formulas that are resolved to skill group references at runtime. See Define Skill Groups Using an Expression .

From the defined set, your script can
                           		determine the target skill group  by one of the following methods:

- Selecting the target by
                              			 rules (Select node)

- Distributing contacts to
                              			 targets in the set (Distribute node)

- A combination of selecting
                              			 the target and distributing contacts (Route Select node)

### Define Skill Groups by Explicit Target Reference

On the Skill Group node in the
                                 		Targets tab of the Palette, select Explicit target references to specify the skill groups that can receive the contact:

Step 1

For each skill group in the target set the following:

In the Skill Group column, for each row used, select the skill
                                                				  group to which the contact can be routed. You can use the drop-down list for
                                                				  each table cell, or select multiple skill groups by clicking Add Targets and using the dialog box that opens to select
                                                				  multiple skill groups.

In the Route column, select the route that maps to a specific
                                                				  target at the peripheral.

Optionally, in the Translation Route column, select a
                                                				  translation route.

Step 2

Optionally, check Allow connection for each target to have an output terminal
                                          			 appear to the right of each individual target defined in the node. Control
                                          			 passes through this terminal when the associated target is chosen. When the
                                          			 script terminates, the route for the selected skill group is still used.

Step 3

Click Validate to check whether the targets you defined are valid.
                                          			 Correct any errors that are flagged.

Step 4

Optionally, add connection labels.

### Define Skill Groups Using an  Expression

On the Skill Group node in the Targets tab of
                                 the Palette, select Look up target references by expression to enter expressions to
                                 select Skill Groups. The formulas are evaluated dynamically at run-time to determine
                                 the actual skill groups.

Step 1

Select Look up target
                                             references by expression

Step 2

Select whether to select the skill groups by name or ID:

- Select By name to select a skill group by the skill group enterprise name.

- Select By ID to select the skill group by the skill group database ID.

Step 3

Write your  formulas to select skill groups on the Skill Group page.

Click Formula Editor for help building a formula.

Step 4

Optionally, click Validate to check for errors in the expression.

Step 5

Click OK to save and close the dialog.

When you use a ScriptTarget node with dynamic skill group configuration as a target node for a
                                 ScriptSelect or ScriptDistribute node, the router evaluates all the targets of the ScriptTarget node and then returns only
                                 valid targets.
                                 If the skill group
                                 expression cannot be evaluated to a valid skill group object, the node continues  on the failure branch and  the router logs
                                 an error message.

Look up Target References by Expression only supports
                                             skill groups that target Unified CCE peripherals. Expressions that evaluate to
                                             skill groups on any other type of peripheral are not considered valid
                                             targets.

## Define a Set of Queue to Skill Groups to Receive the Contact

You define a set of
                           		queue to skill groups that can receive the contact using the Queue node in the
                           		Queue tab of the Palette.

You can specify the queue to skill groups in the set in  two ways:

Select Explicit target references to   specify static queue to skill group configurations, including the Skill Group, Consider If, Route, and, optionally,
                                 a Translation Route.

Select Lookup target references by expression to enter formulas that are resolved to queue to skill group references at runtime.

### Define Queue to Skill Groups by Explicit Target Reference

You can select  explicit target references to specify the skill groups that can receive the contact.

Step 1

From the Queue tab of the Palette, click Queue to create a Queue to Skill Group node.

Step 2

From the node, right-click and select Properties .

Step 3

Select the Explicit target references option.

Step 4

For each skill group in the target, set the following:

In the Skill Group column, for each row used, select the skill
                                                				  group to which the contact can be routed. You can use the drop-down list for
                                                				  each table cell, or select multiple skill groups by clicking Add Targets and using the dialog box that opens to select
                                                				  multiple skill groups.

In the Consider If column, add an expression to one or more rows. If a Consider If expression returns True, the expression
                                                considers the skill group and queues there.

In the Route column, select the route that maps to a specific
                                                				  target at the peripheral.

Optionally, in the Translation Route column, select a
                                                				  translation route.

Step 5

Click Validate to check whether the targets you defined are valid.
                                          			 Correct any errors that are flagged.

### Define Queue to Skill Groups Using an Expression

You can look up target references by expression to enter expressions to select Queue to Skill Groups. The formulas are evaluated
                                 dynamically at run-time to determine the actual skill groups.

Step 1

From the Queue tab of the Palette, click Queue to create a Queue to Skill Group node.

Step 2

From the node, right-click and select Properties .

Step 3

Select Lookup target references by expression

Step 4

Select whether to choose the skill groups by name or ID:

- Select By name to choose a skill group by the skill group name.

- Select By ID to choose the skill group by the skill group database ID.

Step 5

Write your  formulas to select skill groups on the Skill Group page.

Click Formula Editor for help building a formula.

Step 6

Optionally, click Validate to check for errors in the expression.

Step 7

Click OK to save and close the dialog.

When you use a queue to skill group node with dynamic queue to skill group configuration as a target, the router evaluates
                                 all the targets of the queue to skill group node and then returns only valid targets.
                                 If the queue to skill group
                                 expression cannot be evaluated to a valid queue to skill group object, the node continues  on the failure branch and  the
                                 router logs an error message.

Look up Target References by Expression only supports
                                             skill groups that target Unified CCE peripherals. Expressions that evaluate to
                                             skill groups on any other type of peripheral are not considered valid
                                             targets.

## Define Set of Services to Receive the Contact

Selecting the target by rules (Select node)

Distributing contacts to targets in the set (Distribute node)

A combination of selecting the target and distributing contacts (Route Select node)

Following is the Properties dialog box of the Service node:

Step 1

For each service in the target set the following:

In the Service column, for each row used, select the service
                                             				  to which the contact can be routed. You can use the drop-down list for each
                                             				  table cell, or select multiple services by clicking Add Targets and using the dialog box that opens to select
                                             				  multiple services.

In the Route column, select the route that maps to a specific
                                             				  target at the peripheral.

Optionally, in the Translation Route column, select a
                                             				  translation route.

Step 2

Optionally, check Allow connection for each target to have an output terminal
                                       			 appear to the right of each individual target defined in the node. Control
                                       			 passes through this terminal when the associated target is chosen. When the
                                       			 script terminates, the route for the selected service is still used.

Step 3

Click Validate to check whether the targets you defined are valid.
                                       			 Correct any errors that are flagged.

Step 4

Optionally, add connection labels.

## Define Set of Enterprise Skill Groups to Receive the Contact

Selecting the target by rules (Select node)

Distributing contacts to targets in the set (Distribute node)

A combination of selecting the target and distributing contacts (Route Select node)

Following is the Properties dialog box of the Enterprise Skill Group
                              		  node:

Step 1

From the Business Entity drop-down list, select the business
                                       			 entity for the enterprise skill groups.

Step 2

From the Enterprise target drop-down list, select the enterprise
                                       			 target for the enterprise skill groups.

Step 3

For each enterprise skill group in the target set the following:

In the Skill Group column, for each row used, select the
                                             				  enterprise skill group to which the contact can be routed.

In the Route column, select the route that maps to a specific
                                             				  target at the peripheral.

Optionally, in the Translation Route column, select a
                                             				  translation route.

Step 4

Optionally, check Allow connection for each target to have an output terminal
                                       			 appear to the right of each individual target defined in the node. Control
                                       			 passes through this terminal when the associated target is chosen. When the
                                       			 script terminates, the route for the selected enterprise skill group is still
                                       			 used.

Step 5

Click Validate to check whether the targets you defined are valid.
                                       			 Correct any errors that are flagged.

Step 6

Optionally, add connection labels.

## Define Set of Enterprise Services to Receive the Contact

Selecting the target by rules (Select node)

Distributing contacts to targets in the set (Distribute node)

A combination of selecting the target and distributing contacts (Route Select node)

Following is the Properties dialog box of the Enterprise Service node:

Step 1

From the Business Entity drop-down list, select the business
                                       			 entity for the enterprise services.

Step 2

Choose the enterprise target for the enterprise services from the
                                       			 Enterprise target drop-down list.

Step 3

For each enterprise service in the target set the following:

In the Service column, for each row used, select the
                                             				  enterprise service to which the contact can be routed.

In the Route column, select the route that maps to a specific
                                             				  target at the peripheral.

Optionally, in the Translation Route column, select a
                                             				  translation route.

Step 4

Optionally, check Allow connection for each target to have an output terminal
                                       			 appear to the right of each individual target defined in the node. Control
                                       			 passes through this terminal when the associated target is chosen. When the
                                       			 script terminates, the route for the selected enterprise service is still used.

Step 5

Click Validate to check whether the targets you defined are valid.
                                       			 Correct any errors that are flagged.

Step 6

Optionally, add connection labels.

## Network Targets

A network target is an end point on the network to which a
                              script can send a contact. Following are the supported network targets:

Announcement

Scheduled Select

Ring

Busy

Label

Divert Label

## Route Call to an Announcement

When executing the Announcement Node, Unified ICM returns the label
                              		  associated with the announcement to the routing client. The Announcement Node
                              		  terminates the script.

- Explain why the call
                                 			 cannot currently be handled.

- Direct the caller to
                                 			 another phone number or to another way of contacting the company.

Following is the Properties dialog box of the Announcement node:

Step 1

Choose an announcement from the Announcements list.

Step 2

Optionally, add comments.

## Route Call to a Scheduled Target

Unified ICM keeps track of the schedule and the number of calls sent to the target. The routing client informs Unified ICM
                              when a call at the target ends, so it always knows how many calls are currently in progress at the target and whether it can
                              handle an additional call.

When Unified ICM runs the Scheduled Select Node, it searches the list of selected targets for one that is capable of handling
                              the contact, based on its current schedule. If a target is found, the routing script ends and returns a label associated with
                              the target to the routing client. The routing client then translates the label to a peripheral target.

Not all routing clients support the Scheduled Select node.

Following is the Properties dialog box of the Announcement node:

Step 1

In the Evaluation Order field select:

Start with first target to have Unified
                                             ICM always start the search from the first target in the
                                             list.

Start with next target to have Unified
                                             ICM start the search from the first target after the last
                                             chosen target.

Step 2

Click Add Target to add a new scheduled target.
                                       In the Add Schedule Targets dialog box, select targets to add from
                                       the Available targets list, and click Add> to
                                       move them to the Add targets list. When finished, click OK . The targets are added to the list.

Step 3

To add a time period for the scheduled target, select the target
                                       and click Add Period . The Add Periodic Schedule
                                       dialog box opens. Define the time period and click OK .

Step 4

To modify a time period for the scheduled target, select the time
                                       period and click Modify Period . The Modify Periodic
                                       Schedule dialog box opens. Modify the time period and click OK .

Step 5

To edit Max Calls for a time period, select the time period and
                                       click Edit Max Calls . The number in the Max Calls
                                       column is now editable. Modify the value as needed

Step 6

Optionally, add connection labels.

## Route Call to an Unanswered Ring

When Unified ICM runs a Ring node, it returns the first Ring label associated with the routing client; the routing client then plays an unanswered
                              ring for the caller.

Note: You must define a Ring label using Unified ICM Configuration Manager. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

Note: Not all routing clients support the Ring Node.

To define the Ring node properties, you simply add comments to the node.

## Route Call to a Busy Signal

When Unified ICM runs a Busy node, it returns the first Busy label associated with the routing client; the routing client
                              then plays a busy signal for the caller.

Note: You must define a Busy label using Unified ICM Configuration Manager. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

Note: Not all routing clients support the Busy node.

To define the Busy node properties, you simply add comments to the node.

## Return Label to Routing Client

You can return a label to a routing client by using the Label node in the Targets tab of the Palette.

When Unified ICM runs a Label node, it returns the first valid label for the routing client.

This differs from the Divert Label node, which returns all the values in the Selected Labels list to the routing client.

If Unified ICM finds no valid label, it returns the default label for the Dialed Number. In either case, the Label node terminates
                              execution of the script

When you define a Label Node, you can select Configured Labels and Dynamic Labels. Configured labels are static, defined through
                              the Unified ICM Configuration Manager. Dynamic Labels are expressions the CallRouter processes in real time, converting an expression into
                              a character string that is then returned to the routing client as a label. You use formulas to create a Dynamic Label.

The following registry setting in the router controls where to send the dynamic labels for network transferred calls. This
                              registry setting controls ALL of the network transferred calls:

```
HKLM\Cisco Systems,Inc\ICM\<inst>
```

```
\Router<side>\Router\CurrentVersion\Configuration
```

```
\Global\NetworkXferDynLabelDestination
```

```
<setting>
```

If <setting> =

Then the label is sent to

0

The network transfer routing client

1

The network routing client

2

Either the network transfer routing client or the network routing client, based on the NetworkTransferPreferred setting of
                                          the network routing client

The Label node supports Target Requery.

Following is the Properties dialog box of the Label node:

Define Label node properties as follows:

Step 1

Choose the one of the following from Label Type:

Configured, to select from a list of configured
                                             labels.

Dynamic, to define an expression that is to be
                                             returned as a label.

Warning

The incorrect use of dynamic labels in scripts can result in call surges. The router does not do extrapolation for dynamic
                                                            labels. So if many calls come in at the same time, the router may send these calls to the same label, and the Available and
                                                            LongestAvailable will not be extrapolated. To avoid a site becoming flooded with calls, use static labels assigned to skill
                                                            groups and services rather than dynamic labels. The router does extrapolation for labels assigned to skill groups and services.

Step 2

If you select Configured, select labels from the Available
                                       labels list and click Add> to add them to the
                                       Selected labels list.

Step 3

If you select Dynamic, enter a Label Expression, optionally using the Formula Editor .

Step 4

Optionally, check Enable target requery .

Step 5

Optionally, add comments.

## Return Multiple
                        	 Labels to Routing Client

When Unified ICM runs a Divert Label node, it returns all the values in the Selected Labels list to the routing client.

This differs from the Label node, which returns the first valid label for the current routing client.

Unified ICM then tries each label until it finds one that does not produce a Busy or Ring Tone No Response.

In most cases, you can specify up to ten labels in the Divert Label node. The exception is in NAM/CICM configurations, where
                              you can specify up to nine labels; you must reserve one label for use by the NAM.

When you define a Divert Label node, you can select Configured Labels and Dynamic Labels. Configured labels are static, defined
                              through the Unified ICM Configuration Manager. Dynamic Labels are expressions the CallRouter processes in real time, converting an expression into
                              a character string that is then returned to the routing client as a label. You use formulas to create a Dynamic Label.

- With the Divert Label Node, you can only select labels for routing clients with client types that support DivertOnBusy. Unified
                                 Contact Center client type does not support DivertOnBusy. The following client types do support DivertOnBusy:  CRSP, 
                                 					
                                 					 AUCS INAP NIC,  SS7IN NIC, NTL NIC and MCI NIC.

- When using a Divert Label node, arrange the labels so that a label defined with a type Busy or Ring the last label in the
                                 Divert Label Selected labels list. The reason for this is that a Busy or Ring label terminates the call; any label appearing
                                 after Ring or Busy is never used. Also, never use a Divert Label node when only one label exists in the list; use the Label
                                 node, instead.

- Never use a Divert Label node when only one label exists in the list; use the Label node instead.

Step 1

Select the Label
                                       			 Type:

Configured,
                                             				  to select from a list of configured labels.

Dynamic, to
                                             				  define an expression that is to be returned as a label.

Step 2

If you select
                                       			 Configured, select labels from the Available labels list and click Add> to
                                       			 add them to the Selected labels list.

Step 3

If you select
                                       			 Dynamic, enter a Label Expression, optionally using the Formula Editor.

Step 4

Optionally, add
                                       			 comments.

## Selection of Targets by Rules

You can create a script to select a specific target from set of targets
                              based on the rule you select or define.

For example, you can create a script that selects as a target the skill
                              group with longest available agent (LAA) from a set of skill groups.

When defining scripts to select targets by rules, you must be
                              aware of the following:

Types of Target Searching

Standard Selection Rules

Custom Selection Rules

### Types of Target Searches

When you use a Select node, you specify if the script is to search for
                                 the target that matches the criteria you define starting with the first
                                 target in the list, or the next target after the previously chosen
                                 target:

Start with first target - Also referred to as a
                                 homing search, this option has the script search for the target that
                                 meets the criteria you define starting with the first item in the list.
                                 For example, you can define a script to select the longest available
                                 agent from either the Technical Support skill group (the first skill
                                 group in the list) or the backup skill group (the second, and last, item
                                 in the list). When you choose this option, whenever the script can find
                                 an available agent in the Technical support skill group, the contact is
                                 routed to that agent. Agents from the Backup skill group are only
                                 selected as targets when the script fails to find an available agent in
                                 the Technical support skill group. When you select this option, targets
                                 towards the top of the list typically receive a higher percentage
                                 of the contacts.

Start with next target - Also referred to as a rotary
                                 search, this option has the script search for the target that meets the
                                 criteria you define starting with the item in the list after the target
                                 previously selected. For example, you can define a script to select the
                                 longest available agent from one of three separate technical support
                                 skill groups. When you select this option, after a script selects an
                                 agent from the first skill group, for the next contact, the script
                                 starts looking for an agent in the second skill group. When you select
                                 this option, contacts are distributed more evenly among the potential
                                 targets.

### Standard Selection
                           	 Rules

When you use the
                                 		  Select node, you can choose from one of the following standard selection rules:

Selection
                                             					 Rule

Applicable
                                             					 Targets

Formula

Description

Always
                                             					 Select

Any target

Selects the
                                             					 first target that passes the specified acceptance rule.

Longest
                                             					 Available Agent (LAA)

Skill Groups
                                             					 and Enterprise Skill Groups

Consider if:
                                             					 *.AgentsAvail > 0 Evaluate: MAX (*.LongestAvailable)

Selects the target with the agent who has been available for the longest time. This selection rule helps to ensure that all
                                             agents in the skill group set are kept equally busy. It does not ensure that a particular agent is assigned the contact. If
                                             the target set includes a skill group that has subgroups (.pri, .sec, etc.), only agents logged in to the base group are considered.
                                             Because agents do not usually log in to the base group, specify the base groups you want to consider.

Next
                                             					 Available Agent (NAA)

Skill Groups
                                             					 and Enterprise Skill Groups

Consider if:
                                             					 *.AgentsAvail > 0 Evaluate: MAX

(*.
                                             					 AgentsAvail/*. AgentsSignedOn)

Selects the
                                             					 target with the highest percentage of available agents.

Minimum
                                             					 Average Speed Answer (Min ASA)

Services and
                                             					 Enterprise Services

Evaluate:
                                             					 MIN (*.AvgSpeedAnswerTo5)

Selects the
                                             					 target in the set that is, on average, answering contacts most quickly. Because
                                             					 this selection rule evaluates the historical average, it does not select a
                                             					 target based on the current or expected future state of the contact center.
                                             					 Therefore, unexpected load imbalances may occur when you use this rule. To
                                             					 avoid this potential problem, you can use the Minimum Expected Delay selection
                                             					 rule instead.

Minimum
                                             					 Calls in Queue Per Position (Min C/Q)

Services and
                                             					 Enterprise Services

Evaluate:
                                             					 MIN (*.CallsQNow/*.AgentsReady)

Selects the
                                             					 target in the set with the lowest ratio of calls waiting and staffed stations.
                                             					 If agents are equally efficient at each target in the set, this rule tends to
                                             					 lead to the shortest average hold times. However, if agents are not equally
                                             					 efficient, some customers might wait longer than necessary at the less
                                             					 efficient target. To avoid this potential problem, you can use the Minimum
                                             					 Expected Delay selection rule instead.

Minimum
                                             					 Average Queue Delay (Min AvgQD)

Services and
                                             					 Enterprise Services

Evaluate:
                                             					 MIN (*.AvgDelayQTo5)

Selects the
                                             					 target in the set with shortest average hold times, assuming that agents at
                                             					 each target are equally efficient. Because this selection rule evaluates the
                                             					 historical average, it does not select a target based on the current or
                                             					 expected future state of the contact center. Therefore, unexpected load
                                             					 imbalances may occur when you use this rule. To avoid this potential problem,
                                             					 you can use the Minimum Expected Delay selection rule instead.

Minimum
                                             					 Longest Delayed Call (Min Delay)

Services and
                                             					 Enterprise Services

Evaluate:
                                             					 MIN (*.LongestCallQ)

Selects the
                                             					 target with the shortest longest delayed call. Note: This selection rule
                                             					 evaluates the historical average, not the current or expected future state of
                                             					 the contact center. Routing contacts to the target with the shortest longest
                                             					 delayed call does not immediately change the longest delay value. Therefore,
                                             					 this selection rule may route a disproportionately large number of calls to a
                                             					 single target. To avoid this potential problem, you can use the Minimum
                                             					 Expected Delay selection rule instead.

Minimum
                                             					 Expected Delay (MED)

Services and
                                             					 Enterprise Services

Evaluate:
                                             					 MIN (*.ExpectedDelay)

Selects the
                                             					 target with the shortest expected delay. In making this evaluation, this
                                             					 selection rule considers the average handle time, the number of contacts in
                                             					 queue, and the number of positions staffed. This rule is usually the most
                                             					 effective rule for keeping queue times to a minimum. The MED algorithm is not
                                             					 supported on Unified CCE.

Caution: Values used by
                                 		  the standard selection rules Minimum Average Speed Answer, Minimum Average
                                 		  Queue Delay, and Minimum Longest Delayed Call change slowly. Because the
                                 		  averages in these rules only consider what has happened in the past rather than
                                 		  what is currently happening, using these rules inappropriately can lead to load
                                 		  imbalances as newly routed contacts have little immediate effect on the values
                                 		  used to route later contacts. In contrast, the standard selection rule Minimum
                                 		  Expected Delay takes into account each contact as it is routed. Selecting the
                                 		  service using the Minimum Expected Delay rule usually provides the best balance
                                 		  among the services in the target set.

### Custom Selection Rules

Instead of using one of the standard selection rules, you can create a
                                 custom selection rule. To write custom selection rules, you must be
                                 familiar with using formulas. For more information on formulas, see the chapter Use of Formulas.

A custom selection rule has three parts:

Consider if statement 0. This expression ensures that only
                                       skill groups with at least one available agents are considered
                                       as targets; if a skill group has no available agents, the
                                       expression returns False and the skill group is not considered.

Selection criteria . A numeric expression plus
                                       an evaluation rule. The numeric expression determines a certain
                                       value of each target for which the Consider if statement
                                       returned True. The evaluation rule determines if the target with
                                       the minimum or maximum value returned is selected. If you do not
                                       define selection criteria, the first target to return True for
                                       the Consider if statement is selected. For example, the
                                       Selection criteria for the predefined Longest Available Agent
                                       selection rule is MAX (*.LongestAvailable). This expression
                                       determines the highest LongestAvailable value of all the skill
                                       groups in the target set for which the Consider if statement
                                       returned True.

Accept if statement . A Boolean expression that returns
                                       True or False for the target selected by the selection criteria.
                                       If the Accept if statement returns True, the target is selected;
                                       if it returns False, no target is selected by the Select node.

### Selection of Targets by Rules

You can select targets by rules by using the Select node in the
                                 Routing tab of the Palette.

The Select node sets up a rule by which the node chooses from a set of
                                 routing targets for the contact. You can select a standard rule or
                                 define your own custom rule. This node also has target requery
                                 capabilities.

Notes:

You can follow the instructions in this section to select
                                       targets by rules using the Select node. You can also use the
                                       Route Select node to select targets as well as distribute
                                       contacts to targets.

You must add a skill target and create a connection from the
                                       Select node's success terminal, and define at least one target
                                       in the target set, before defining the Select node.

The Select Node supports Target Requery.

Following is the Properties dialog box of the Select node:

Define Select node properties as follows:

Select from the list of Standard rules, or select
                                       Custom and:

In the Consider if field, enter a Boolean expression. A target is considered for selection only if the Consider If expression is true for that
                                             target. Optionally, use the Formula Editor.

Select Pick the target with the minimum value
                                                of or Pick the target with the
                                                maximum value of and enter an expression to
                                             select the target.

Optionally, in the Accept if field, enter a Boolean expression that must evaluate to true for the target to be selected. It determines whether the target
                                       must be returned or the process must end. The Boolean expression does not permit wild cards and evaluates various conditions
                                       to determine if any target must be returned. For example, you can use a peripheral user variable such as Peripheral.PG_CCM.userRouteToCustomerService==1 in the Accept if field of a Select node to determine whether the script is routed to any customer service skill groups at a particular time.

Select Start with first target or Start with next target to indicate how
                                       Unified ICM looks for targets. For more information, see the section Types of Target Searching .

Optionally, check Enable target requery .

Optionally, add comments and connection labels.

## Distribute Contacts to Targets

For example, you can distribute contacts among a set of services based
                              		  on the number of agents in the service in the Ready state. Services with more
                              		  agents in the ready state are routed more contacts than services with fewer
                              		  agents in the Ready state, thus keeping the load balanced.

You can distribute contacts to any of the following types of target
                              		  sets: Agent, Skill Group, Service, Enterprise Skill Group, or Enterprise
                              		  Service.

When creating a script to distribute contacts to targets, you must
                              		  define the following for the Distribute node 
                              		  using formulas. For more information on using formulas, see the chapter Use of Formulas.

- Consider
                                    				if statement . A Boolean expression that returns True or False
                                 			 for each target in the target set. Only targets in the set for which the
                                 			 expression is True are eligible to be distributed contacts. If you do not
                                 			 define an expression for the Consider if statement, all targets in the target
                                 			 set are considered. For example,

- Distribute
                                    				by statement . A formula used to distribute contacts to targets

- You can follow the
                                 			 instructions in this section to distribute contacts to targets using the
                                 			 Distribute node. You can also use the Route Select node to select targets as
                                 			 well as distribute contacts to targets.

- You must add a skill
                                 			 target and create a connection from the Distribute node's success terminal, and
                                 			 define at least one target in the target set, before defining the Distribute
                                 			 Enter node.

Following is the Properties dialog box of the Distribute node:

Step 1

Enter a condition in the Consider if field to test potential
                                       			 targets against.

Step 2

Enter a formula by which to distribute contacts in the Distribute
                                       			 by field.

Step 3

Optionally, add comments and connection labels.

## Select Targets and Distribute Contacts with One Node

Following is the Properties dialog box for the Route Select node:

Step 1

To select the Route select type, click Change . The Route Select Type dialog box
                                       opens:

For Target Type, select Agent , Enterprise Service , Enterprise
                                                Skill Group , Service , Service Array , or Skill
                                                Group .

If you selected Enterprise Service or Enterprise Skill
                                             Group, select a Business Entity and Enterprise target .

Select Distribute among targets or Select most eligible target .

If you selected Select most eligible target , select Pick the target with the minimum value or Pick the target with the maximum value . In the Accept target if field, enter a condition that the target must meet to be selected. Select Start with first target or Start with next target . For more information, see Types of Target Searching .

Unlike the Select most eligible target option to pick targets, where the Call Router scans all eligible targets (the ones that satisfy the Consider If condition),
                                             based on either a Minimum or Maximum value of a parameter, the Distribute among targets option attempts to pick targets based on an algorithm such that targets with higher weightage or “Distribute By” expression
                                             tend to get picked over the others. The Distribute among targets option sums up all the values for each valid/eligible target (those that satisfy the Consider If condition), and then multiplies
                                             the sum by a random factor using the rand() method to get a random number between 0 and the sum of values of the targets by
                                             using something like below:

random = sum * ((double)rand() / (double)RAND_MAX);

The constant RAND_MAX is the maximum value that can be returned by the rand() function. RAND_MAX is defined as the value 0x7fff.

It then scans the list of targets again among the eligible ones and keeps adding the individual values defined under the “Distribute
                                                By” column to a running sum value. The Call Router picks the first target whose value when added to the running summation,
                                                is higher than the random number derived by the formula above (between 0 and the sum of all eligible targets). So, targets
                                                with higher values tend to get picked for the call over others, thereby achieving a sort of load balancing among the targets.

In the Target references field, select Explicit
                                                target references to use direct references to
                                             targets, or Lookup target references by
                                                expression to use expressions that evaluate to
                                             names of targets. Note Lookup target references by
                                                expression is not available when an External Authorization server is used with Internet Script Editor and will be grayed out in the
                                             interface.

Optionally, check Enable target requery .

Click OK .

Step 2

The fields in the Route Select Properties dialog box change
                                       depending on your route select type selections. Enter and select
                                       data appropriate for the type you selected.

Step 3

Click Validate to check whether the targets you
                                       defined are valid. Correct any errors that are flagged.

Step 4

Optionally, add connection labels.

## Transfer Calls from
                        	 Agents to Agents

The Agent to Agent node routes the call to the specified agent. You define the agent either by directly selecting the agent
                              from the database or by providing an expression using a formula. The expression must translate to agent peripheral number
                              or SkillTargetID. The router then finds a valid label for the agent. If there are no labels configured for the specified agent,
                              the failure node of the Agent to Agent node is run.

Following is the Properties dialog box for the Agent to Agent node:

Step 1

Choose an option
                                       			 from the Select agent
                                          				by drop-down list:

Peripheral
                                             				  number - To select a peripheral and a provide formula that translates to the
                                             				  agent's peripheral number.

Enterprise
                                             				  Name - To select the agent from the list of configured agents.

Skill target
                                             				  ID - To select the agent by providing an expression that translates into the
                                             				  agent's SkillTargetID. In the supervisory case, the expression should use the
                                             				  call's PreferredAgentID.

Step 2

Based on your
                                       			 selection in Step 1, select the peripheral or agent, or enter an expression, as
                                       			 necessary.

Step 3

Optionally,
                                       			 check or uncheck Fail node if
                                       			 agent is unavailable:

When checked, the success branch of the Agent to Agent node is run and the router sends the call if the router finds a valid
                                             label for the agent, the agent is available, and the agent state is Ready.

The failure branch of the Agent to Agent node is run if the router does not find a valid label for the agent, or the agent
                                             is not available or the agent is in TempUnavailable mode (the router has just send a call to the agent).

When not checked, the success branch of the Agent to Agent node is run and the router sends the call if the router finds a
                                             valid label for the agent. The failure branch of the Agent to Agent node is run if the Router does not find a valid label
                                             for the agent.

Step 4

Optionally, add
                                       			 comments and connection labels.

Step 5

Optionally, check Enable Target Requery .

## Send Contact to a Different Unified ICM System

You send a contact to a different system by using the ICM Gateway node in the Routing tab of the Palette.

The ICM Gateway node passes a routing request to the selected Unified ICM system.

Step 1

In the Send tab:

Select the gateway to Unified ICM system (and hence the
                                             specific Unified ICM instance) from the ICM Gateways list to
                                             which you want to send the request.

Check Validate returned labels to have
                                             Unified ICM validate the returned labels.

Specify whether Calling Line ID masking instructions
                                             should be applied before the request is passed to the other
                                             Unified ICM system. The Calling Line ID masking refers to
                                             when the caller's phone number is modified so that Unified
                                             ICM application does not display all of the digits; this is
                                             used in a NAM environment, where NAM sends the call to a
                                             customer Unified ICM. Choose one of the following:

1) Do not apply masking rule - If selected, masking instructions are ignored.

2) Apply masking rule if call is presentation restricted - If selected, applies masking instructions if the call variable CLIDRestricted is set to 1.

3) Always apply masking rule - If selected, masking instructions are always applied.

Step 2

In the Default Label tab:

In the Available Labels list, select one default label for
                                             each routing client to be used by the targeted Unified ICM
                                             system.

Click Add to move the selected label to
                                             the Selected labels list.

Step 3

Optionally, add comments and connection labels.

## Nodes Used to Stop Script Processing

You can use the following nodes to stop script
                              processing:

End Node

Termination Node

Release Call Node

### End Node

You can terminate the script by using the End node in the General tab
                                 of the Palette.

If the script reaches the End node, it has failed to find a target for the contact. Unified ICM then uses the default route for the Dialed Number.

Several End nodes can appear in the same script. The End node is never
                                 required; a script can terminate with any node.

You do not define any properties for the End node. You can optionally
                                 add comments.

### Termination Node

You can terminate the script and specify how to handle the contact by
                                 using the Termination node in the Targets tab of the Palette.

The Termination node includes the following options to
                                 invoke a default contact processing action or route for the Dialed
                                 Number:

Default Label - Unified ICM uses the default label configured
                                       for the Dialed Number.

Network Default - The routing client uses its own default
                                       processing.

Ring - Makes the Termination node equivalent to a Ring node.

Busy - Makes the Termination node equivalent to a Busy node.

Following is the Properties dialog box for the Termination node:

### Release Call
                           	 Node

You can terminate
                                 		  the script and disconnect the caller by using the Release Call node in the
                                 		  Targets tab of the Palette.

You can use a Release Call node in situations where the caller needs no further service after executing several VRU scripts.

You do not define
                                 		  any properties for the Release Call node. You can optionally add comments.

## Service Requested

ServiceRequested is a call variable available in Script Editor. It provides more details regarding the routing request. The
                              field is currently only set for multichannel routing ( Task Routing ), voice callback (Agent Request) and Pick/ Pull routing, otherwise it is set to 0. Based on the value of this field, the
                              script can take different actions.

### ServiceRequested Variable

Service Requested Variable

Description

0 = ROUTE_SERVICE_REQUEST_NONE

No service requested.

1 = ROUTE_SERVICE_REQUEST_VOICE_CALLBACK

Caller is requesting a voice callback.

2 = ROUTE_SERVICE_REQUEST_TRANSFER

Transfer a task that is already assigned to an agent back to a queue.

3 = ROUTE_SERVICE_REQUEST_RONA

A task is being rerouted on no answer (RONA).

4 = ROUTE_SERVICE_REQUEST_PICK_EXT_QUEUE

Pick a task that is associated external application queue for a specified agent.

5 = ROUTE_SERVICE_REQUEST_PULL_EXT_QUEUE

Pull a task that is associated external application queue for a specified agent.

6 = ROUTE_SERVICE_REQUEST_PICK_UCCE_AGENT

Pick a task that is already assigned to another agent for a specified agent.

7 = ROUTE_SERVICE_REQUEST_TRANSFER_PICK

Transfer a task that is already assigned to an agent directly to another agent, instead of back to a queue.

## Target Requery

Target Requery is a script node feature that you can use to handle routing failures, for example
                              due to No Answer or Busy responses, or for  unreachable targets caused by transient failures in the network (such as network
                              congestion). If
                              the determined destination for a contact is available but not reachable,
                              Target Requery attempts to find a different valid destination.

You need Target Requery to address the following failures:

Failure to deliver a call to an ACD agent.

Failure to deliver a call to an individual Enterprise Agent (EA).

Failure of the outbound leg of a blind-mode Network Transfer.

Target Requery works on a per call basis; that is, the routing
                                    information for one call does not affect the state for other calls.
                                    If the first target selected for the contact was not reachable, the
                                    target is not eliminated from the potential routing destinations for
                                    other contacts.

You can enable the Target Requery feature for CVP, ICM to ICM gateway, and a subset of the supported carrier NICs. You cannot
                                          use the requery feature with any of the multimedia requests because the MR PG does not support requery mechanism.

### Target Requery Functionality

In the system, when queried, the CallRouter returns a label to
                                 the routing client. The routing client then routes the call to the
                                 destination specified by the label. If the destination is not reachable
                                 (for example, because of a busy signal or no answer), the call is routed
                                 to the default destination.

With Target Requery in a Label, Route Select, or Select node, if the router fails to route to a target node,
                                 a second attempt is made. If the failure occurs a second time, then the
                                 router continues from the failure path in the node.

In the event of a failure, you can handle requerying in the scripting
                                 environment, as you deem appropriate.

Target Requery:

Is compatible with translation routes.

Does not require different definitions for different failure cases. However, you can choose to handle different failures differently.

Assigns the SERVICE_DIVERT_ON_BUSY service type for calls that use target requery. The Event Select in the connect message
                                       includes a REROUTE_REQUESTED_MASK. When a destination cannot be reached, the NIC queries the CallRouter for an alternative
                                       destination label.

### Test of the RequeryStatus Variable

You can test the error path of these script nodes using Target Requery
                                 to determine the specific network cause of failure and conditionally
                                 retry the attempt as necessary. You can accomplish this using an If node to check
                                 the value of the call variable RequeryStatus. The decision path for the
                                 script is then determined by the value of the RequeryStatus variable.

The following are possible values for the RequeryStatus variable:

Requery Status Variable

Description

REQUERY_ANSWER (0)

Script ends. The call
                                             was successfully sent to the chosen target.

REQUERY_ROUTE_SELECT_FAILURE (1)

Routing client generated an error code from
                                             ReRouteReq msg indicating a Route Select failure.

REQUERY_CALLED_PARTY_BUSY (2)

Routing client generated error code from
                                             ReRouteReq msg indicating the called party is busy.

REQUERY_NO_ANSWER (3)

Routing client generated an error code from
                                             ReRouteReq msg indicating no answer.

REQUERY_ERROR (4)

CallRouter generated an error code. The attempt to
                                             send the call to target failed because the target
                                             was not reachable (i.e., busy, ring no answer).

REQUERY_ABORTED (5)

The attempt to send the call to a target failed because the caller abandoned before the call could be delivered to its destination.
                                             In the case of ABANDON and DISCONNECT, the CallRouter assumes the call has ended and ends the script. The RequeryStatus value
                                             is set to 5, indicating REQUERY_ABORTED.

REQUERY_TIMED_OUT (6)

The call attempt failed because the routing client did not respond to the router within the DivertOnBusyCallTimeout period
                                             (180 seconds by default). If the target node has Router Requery enabled, when DivertOnBusyCallTimeout period expires, the
                                             Router closes the Router Requery with REQUERY_TIMED_OUT .

### Nodes That Support Target Requery

The following nodes support Target Requery:

Label

Queue

Queue to Agent

Precision Queue

Route Select

Select

Agent to Agent

Scheduled Targets do not support Target Requery.

### Target Requery with Unified CCE and Unified IP IVR

Target Requery is not supported when Unified IP IVR is used as the queue
                                 point in a Unified CCE system because Unified IP IVR cannot requeue the call. The call is requeued from
                                 Cisco Communications Manager instead. Setting the Target Requery option
                                 on the script node has no effect on the requeuing of the call, and may
                                 lead to timeouts and other script errors for that particular call.

Do not enable Target Requery in script nodes when you  use Unified IP
                                 IVR.

### Use Target Requery

You define nodes to enable Target Requery. For the Queue, Queue to Agent, Agent to Agent, and Route Select nodes:

Step 1

Open the node properties.

Step 2

Click Change . A dialog box opens.

Step 3

Check Enable target requery .

Step 4

Click OK to close the dialog box.

Step 5

Click OK to close the properties dialog box.

Step 6

For the Label, Select and Precision Queue nodes:

For the Label and Select nodes:

Open the node properties.

Check Enable Target Requery .

Click OK to close the properties dialog box.

### Target checking

## About Call Tracer

You can use the Call Tracer utility from within Script Editor to test
                              and debug a routing script and to confirm that the Unified ICM is selecting
                              targets as you expect. Call Tracer simulates a contact to the CallRouter
                              and generates a text-based description of how the contact was handled.
                              The test contact is processed by the active CallRouter, using all the
                              real-time data of Unified ICM as it exists at that moment, but
                              interactions with any peripheral is simulated.

## Check Targets

### Before you begin

Step 1

In the Call Tracer window, choose a Media Domain as voice, a Routing Client, and a Dialed Number.

Step 2

Optionally, enter an ANI (callers telephone number).

Step 3

If you want to test a response from a VRU routing script,
                                       enter values in Caller-Entered-Digits (CED) and VRU Responses
                                       for External Script.

Step 4

To use Network Transfer Call, a feature that
                                       integrates Unified ICM Post-Routing function with a carrier
                                       network's call control ability so that a call can be
                                       transferred anywhere in the network without the use of
                                       transfer/connect services or inter-site tie lines:

Select Use Network Transfer.

Select a routing client and a Dialed Number value.

Step 5

Click Send Call to submit the request. The
                                       results appear in the Call Trace Results field.

Step 6

To send additional calls, optionally change any of the call
                                       parameters and then click Send Call again. The
                                       Call Trace Results field is updated.

Step 7

Unified ICM runs only installed scripts in response to requests from the Call Tracer. Any uninstalled changes in scripts
                                       are not reflected in the Call Tracer results.

Step 1

In the Call Tracer window, choose a Media Domain other than a voice call, a Routing Client, and a Script Selector.

Step 2

Optionally, enter an Application String 1 and Application String 2.

Step 3

For tracing PICK/PULL request.

Select a Service Type , and choose a Queue Type

Enter a Queue ID and select the CCUM/system Peripherals with a Preferred Agent .

Step 4

Click Send Call to submit the request. The results appear in the Call Trace Results field.

Step 5

To send additional calls, optionally change any of the call parameters and then click Send Call again. The Call Trace Results field is updated.

Step 6

Unified ICM runs only installed scripts in response to requests from the Call Tracer. Any uninstalled changes in scripts
                                       are not reflected in the Call Tracer results.

## Example Results

In the following example results from Call Tracer, Unified ICM invokes a script called sales. It begins with the Start node
                              and then runs a Percent Allocation node that has three branches allocated for 42%, 16%, and 42%, respectively. The asterisk
                              indicates that for this call, Unified ICM chooses the first branch. This branch leads to a target that maps to the service
                              Scranton.Sales. Had this been an actual call, the call would be delivered to that service.

As you continue to send calls to the Unified ICM, the numbers for each
                              node change to indicate how calls have been distributed. Each time a
                              call arrives at a Percent Allocation node, the Unified ICM calculates the
                              percentage of calls previously sent to each branch:

> DialedNumber (8005551212) using CallType
                                 (General_Sales - 6)

Start #3

__Sales\Sales__General (version 2)

Percent allocation #54

__*42% = 0

__ 16% = 0

__ 42% = 0

Target #64

__Service: Scranton.Sales R

Route: Scranton.Sales

Peripheral target: DNIS: 1111, Trunk group:
                                 Scranton.Incoming800

Label: 2010000000

In the next example, for each branch the new call is counted in the denominator. Therefore, the numbers add up to less than
                              1.0 and gradually, as you send more calls, the total increases up to 1.0. Unified ICM picks the branch that is below its allocation
                              value. For the example allocation, Unified ICM picked the third branch as 0.375 is below the allocation of 42% or 0.42 and
                              sent the call to the Gary.Sales service.

Traces are linked to live scripts. For example, clicking on the trace
                              details of a Percent Allocation node immediately, if it is not already
                              open, opens the script and locates that node in the Script Editor
                              window. Previously, you needed to manually decode script, script version
                              and node ID information, and then visually scan the script for the
                              desired node. Node titles in the trace window support localization.

The Call Tracer results refer to script nodes by their internal
                              integer identifiers. To find which node maps to each identifier, open
                              the script and choose Display Node IDs from the Script menu:

> DialedNumber (8005551212) using CallType
                                 (General_Sales - 6)

Start #3

__Sales\Sales__General (version 2)

Percent allocation #54

__42% = 0.416667

__16% = 0.166667

__*42% = 0.375

Target #58

__Service: Gary.Sales

Route: Gary.Sales

Peripheral target: DNIS: 1111, Trunk group:
                                 Gary.Incoming800

Label: 3010000000

## Check VRU Scripts

### Before you begin

- Fail. Unified ICM treats the External Script nodes as though
                                 it had failed.

- No Response. Unified ICM assumes it received no response from
                                 the Run External Script node.

- Response. You can specify a CED value and values for Variable1
                                 through Variable10. Unified ICM assumes these values were
                                 returned by the External Script node.

Step 1

In the Call Tracer dialog box, click Add . The
                                       VRU Response dialog box opens.

Step 2

Select the type of response (Fail, No Response, Response) the
                                       Call Tracer is to simulate.

Step 3

If you chose Response in Step 2, optionally specify values to
                                       be returned for CED and Variable1 through Variable10.

Step 4

Click OK to apply changes and close the
                                       dialog box.

### What to do next

| Note | You create routes through Unified ICM Configuration Manager before writing routing scripts. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Note | You create translation routes through Unified ICM Configuration Manager before writing routing scripts. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Note | Do not use this node in Unified CCE environments. It is
                                          		  intended for use with ACDs. |
|---|---|

| Step 1 | For each agent in the target set the following: In the Agent column, for each row used, select the agent to
                                                				  which the contact can be routed. You can use the drop-down list for each table
                                                				  cell, or select multiple agents by clicking Add Targets and using the dialog box that opens to select
                                                				  multiple agents. In the Route column, select the route that maps to a specific
                                                				  target at the peripheral. Optionally, in the Translation Route column, select a
                                                				  translation route. |
|---|---|
| Step 2 | Optionally, check Allow connection for each target to have an
                                          			 output terminal appear to the right of each individual target defined in the
                                          			 node. Control passes through this terminal when the associated target is
                                          			 chosen. When the script terminates, the route for the selected agent is still
                                          			 used. |
| Step 3 | Click Validate to check whether the targets you defined are valid.
                                          			 Correct any errors that are flagged. |
| Step 4 | Optionally, add connection labels. |

| Step 1 | For each skill group in the target set the following: In the Skill Group column, for each row used, select the skill
                                                				  group to which the contact can be routed. You can use the drop-down list for
                                                				  each table cell, or select multiple skill groups by clicking Add Targets and using the dialog box that opens to select
                                                				  multiple skill groups. In the Route column, select the route that maps to a specific
                                                				  target at the peripheral. Optionally, in the Translation Route column, select a
                                                				  translation route. |
|---|---|
| Step 2 | Optionally, check Allow connection for each target to have an output terminal
                                          			 appear to the right of each individual target defined in the node. Control
                                          			 passes through this terminal when the associated target is chosen. When the
                                          			 script terminates, the route for the selected skill group is still used. |
| Step 3 | Click Validate to check whether the targets you defined are valid.
                                          			 Correct any errors that are flagged. |
| Step 4 | Optionally, add connection labels. |

| Step 1 | Select Look up target
                                             references by expression |
|---|---|
| Step 2 | Select whether to select the skill groups by name or ID: Select By name to select a skill group by the skill group enterprise name. Select By ID to select the skill group by the skill group database ID. |
| Step 3 | Write your  formulas to select skill groups on the Skill Group page. Click Formula Editor for help building a formula. |
| Step 4 | Optionally, click Validate to check for errors in the expression. |
| Step 5 | Click OK to save and close the dialog. When you  save the dialog, the configured expressions are validated. If errors are found, the dialog displays a warning and
                                          highlights the rows with errors. |

| Note | Look up Target References by Expression only supports
                                             skill groups that target Unified CCE peripherals. Expressions that evaluate to
                                             skill groups on any other type of peripheral are not considered valid
                                             targets. |
|---|---|

| Step 1 | From the Queue tab of the Palette, click Queue to create a Queue to Skill Group node. |
|---|---|
| Step 2 | From the node, right-click and select Properties . |
| Step 3 | Select the Explicit target references option. |
| Step 4 | For each skill group in the target, set the following: In the Skill Group column, for each row used, select the skill
                                                				  group to which the contact can be routed. You can use the drop-down list for
                                                				  each table cell, or select multiple skill groups by clicking Add Targets and using the dialog box that opens to select
                                                				  multiple skill groups. In the Consider If column, add an expression to one or more rows. If a Consider If expression returns True, the expression
                                                considers the skill group and queues there. In the Route column, select the route that maps to a specific
                                                				  target at the peripheral. Optionally, in the Translation Route column, select a
                                                				  translation route. |
| Step 5 | Click Validate to check whether the targets you defined are valid.
                                          			 Correct any errors that are flagged. |

| Step 1 | From the Queue tab of the Palette, click Queue to create a Queue to Skill Group node. |
|---|---|
| Step 2 | From the node, right-click and select Properties . |
| Step 3 | Select Lookup target references by expression |
| Step 4 | Select whether to choose the skill groups by name or ID: Select By name to choose a skill group by the skill group name. Select By ID to choose the skill group by the skill group database ID. |
| Step 5 | Write your  formulas to select skill groups on the Skill Group page. Click Formula Editor for help building a formula. |
| Step 6 | Optionally, click Validate to check for errors in the expression. |
| Step 7 | Click OK to save and close the dialog. When you  save the dialog, the configured expressions are validated. If errors are found, the dialog displays a warning and
                                          highlights the rows with errors. |

| Note | Look up Target References by Expression only supports
                                             skill groups that target Unified CCE peripherals. Expressions that evaluate to
                                             skill groups on any other type of peripheral are not considered valid
                                             targets. |
|---|---|

| Step 1 | For each service in the target set the following: In the Service column, for each row used, select the service
                                             				  to which the contact can be routed. You can use the drop-down list for each
                                             				  table cell, or select multiple services by clicking Add Targets and using the dialog box that opens to select
                                             				  multiple services. In the Route column, select the route that maps to a specific
                                             				  target at the peripheral. Optionally, in the Translation Route column, select a
                                             				  translation route. |
|---|---|
| Step 2 | Optionally, check Allow connection for each target to have an output terminal
                                       			 appear to the right of each individual target defined in the node. Control
                                       			 passes through this terminal when the associated target is chosen. When the
                                       			 script terminates, the route for the selected service is still used. |
| Step 3 | Click Validate to check whether the targets you defined are valid.
                                       			 Correct any errors that are flagged. |
| Step 4 | Optionally, add connection labels. |

| Step 1 | From the Business Entity drop-down list, select the business
                                       			 entity for the enterprise skill groups. |
|---|---|
| Step 2 | From the Enterprise target drop-down list, select the enterprise
                                       			 target for the enterprise skill groups. |
| Step 3 | For each enterprise skill group in the target set the following: In the Skill Group column, for each row used, select the
                                             				  enterprise skill group to which the contact can be routed. In the Route column, select the route that maps to a specific
                                             				  target at the peripheral. Optionally, in the Translation Route column, select a
                                             				  translation route. |
| Step 4 | Optionally, check Allow connection for each target to have an output terminal
                                       			 appear to the right of each individual target defined in the node. Control
                                       			 passes through this terminal when the associated target is chosen. When the
                                       			 script terminates, the route for the selected enterprise skill group is still
                                       			 used. |
| Step 5 | Click Validate to check whether the targets you defined are valid.
                                       			 Correct any errors that are flagged. |
| Step 6 | Optionally, add connection labels. |

| Step 1 | From the Business Entity drop-down list, select the business
                                       			 entity for the enterprise services. |
|---|---|
| Step 2 | Choose the enterprise target for the enterprise services from the
                                       			 Enterprise target drop-down list. |
| Step 3 | For each enterprise service in the target set the following: In the Service column, for each row used, select the
                                             				  enterprise service to which the contact can be routed. In the Route column, select the route that maps to a specific
                                             				  target at the peripheral. Optionally, in the Translation Route column, select a
                                             				  translation route. |
| Step 4 | Optionally, check Allow connection for each target to have an output terminal
                                       			 appear to the right of each individual target defined in the node. Control
                                       			 passes through this terminal when the associated target is chosen. When the
                                       			 script terminates, the route for the selected enterprise service is still used. |
| Step 5 | Click Validate to check whether the targets you defined are valid.
                                       			 Correct any errors that are flagged. |
| Step 6 | Optionally, add connection labels. |

| Note | You must configure Announcements and associate them with labels
                                       		  using Unified ICM Configuration Manager. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
|---|---|

| Step 1 | Choose an announcement from the Announcements list. |
|---|---|
| Step 2 | Optionally, add comments. |

| Note | You must configure Scheduled targets and associated them with labels using Unified ICM Configuration Manager. For more information,
                                       see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
|---|---|

| Step 1 | In the Evaluation Order field select: Start with first target to have Unified
                                             ICM always start the search from the first target in the
                                             list. Start with next target to have Unified
                                             ICM start the search from the first target after the last
                                             chosen target. |
|---|---|
| Step 2 | Click Add Target to add a new scheduled target.
                                       In the Add Schedule Targets dialog box, select targets to add from
                                       the Available targets list, and click Add> to
                                       move them to the Add targets list. When finished, click OK . The targets are added to the list. |
| Step 3 | To add a time period for the scheduled target, select the target
                                       and click Add Period . The Add Periodic Schedule
                                       dialog box opens. Define the time period and click OK . |
| Step 4 | To modify a time period for the scheduled target, select the time
                                       period and click Modify Period . The Modify Periodic
                                       Schedule dialog box opens. Modify the time period and click OK . |
| Step 5 | To edit Max Calls for a time period, select the time period and
                                       click Edit Max Calls . The number in the Max Calls
                                       column is now editable. Modify the value as needed |
| Step 6 | Optionally, add connection labels. |

| If <setting> = | Then the label is sent to |
|---|---|
| 0 | The network transfer routing client |
| 1 | The network routing client |
| 2 | Either the network transfer routing client or the network routing client, based on the NetworkTransferPreferred setting of
                                          the network routing client |

| Note | The Label node supports Target Requery. |
|---|---|

| Step 1 | Choose the one of the following from Label Type: Configured, to select from a list of configured
                                             labels. Dynamic, to define an expression that is to be
                                             returned as a label. Warning The incorrect use of dynamic labels in scripts can result in call surges. The router does not do extrapolation for dynamic
                                                            labels. So if many calls come in at the same time, the router may send these calls to the same label, and the Available and
                                                            LongestAvailable will not be extrapolated. To avoid a site becoming flooded with calls, use static labels assigned to skill
                                                            groups and services rather than dynamic labels. The router does extrapolation for labels assigned to skill groups and services. | Warning | The incorrect use of dynamic labels in scripts can result in call surges. The router does not do extrapolation for dynamic
                                                            labels. So if many calls come in at the same time, the router may send these calls to the same label, and the Available and
                                                            LongestAvailable will not be extrapolated. To avoid a site becoming flooded with calls, use static labels assigned to skill
                                                            groups and services rather than dynamic labels. The router does extrapolation for labels assigned to skill groups and services. |
|---|---|---|---|
| Warning | The incorrect use of dynamic labels in scripts can result in call surges. The router does not do extrapolation for dynamic
                                                            labels. So if many calls come in at the same time, the router may send these calls to the same label, and the Available and
                                                            LongestAvailable will not be extrapolated. To avoid a site becoming flooded with calls, use static labels assigned to skill
                                                            groups and services rather than dynamic labels. The router does extrapolation for labels assigned to skill groups and services. |
| Step 2 | If you select Configured, select labels from the Available
                                       labels list and click Add> to add them to the
                                       Selected labels list. |
| Step 3 | If you select Dynamic, enter a Label Expression, optionally using the Formula Editor . |
| Step 4 | Optionally, check Enable target requery . |
| Step 5 | Optionally, add comments. |

| Warning | The incorrect use of dynamic labels in scripts can result in call surges. The router does not do extrapolation for dynamic
                                                            labels. So if many calls come in at the same time, the router may send these calls to the same label, and the Available and
                                                            LongestAvailable will not be extrapolated. To avoid a site becoming flooded with calls, use static labels assigned to skill
                                                            groups and services rather than dynamic labels. The router does extrapolation for labels assigned to skill groups and services. |
|---|---|

| Step 1 | Select the Label
                                       			 Type: Configured,
                                             				  to select from a list of configured labels. Dynamic, to
                                             				  define an expression that is to be returned as a label. |
|---|---|
| Step 2 | If you select
                                       			 Configured, select labels from the Available labels list and click Add> to
                                       			 add them to the Selected labels list. |
| Step 3 | If you select
                                       			 Dynamic, enter a Label Expression, optionally using the Formula Editor. |
| Step 4 | Optionally, add
                                       			 comments. |

| Selection
                                             					 Rule | Applicable
                                             					 Targets | Formula | Description |
|---|---|---|---|
| Always
                                             					 Select | Any target |  | Selects the
                                             					 first target that passes the specified acceptance rule. |
| Longest
                                             					 Available Agent (LAA) | Skill Groups
                                             					 and Enterprise Skill Groups | Consider if:
                                             					 *.AgentsAvail > 0 Evaluate: MAX (*.LongestAvailable) | Selects the target with the agent who has been available for the longest time. This selection rule helps to ensure that all
                                             agents in the skill group set are kept equally busy. It does not ensure that a particular agent is assigned the contact. If
                                             the target set includes a skill group that has subgroups (.pri, .sec, etc.), only agents logged in to the base group are considered.
                                             Because agents do not usually log in to the base group, specify the base groups you want to consider. |
| Next
                                             					 Available Agent (NAA) | Skill Groups
                                             					 and Enterprise Skill Groups | Consider if:
                                             					 *.AgentsAvail > 0 Evaluate: MAX (*.
                                             					 AgentsAvail/*. AgentsSignedOn) | Selects the
                                             					 target with the highest percentage of available agents. |
| Minimum
                                             					 Average Speed Answer (Min ASA) | Services and
                                             					 Enterprise Services | Evaluate:
                                             					 MIN (*.AvgSpeedAnswerTo5) | Selects the
                                             					 target in the set that is, on average, answering contacts most quickly. Because
                                             					 this selection rule evaluates the historical average, it does not select a
                                             					 target based on the current or expected future state of the contact center.
                                             					 Therefore, unexpected load imbalances may occur when you use this rule. To
                                             					 avoid this potential problem, you can use the Minimum Expected Delay selection
                                             					 rule instead. |
| Minimum
                                             					 Calls in Queue Per Position (Min C/Q) | Services and
                                             					 Enterprise Services | Evaluate:
                                             					 MIN (*.CallsQNow/*.AgentsReady) | Selects the
                                             					 target in the set with the lowest ratio of calls waiting and staffed stations.
                                             					 If agents are equally efficient at each target in the set, this rule tends to
                                             					 lead to the shortest average hold times. However, if agents are not equally
                                             					 efficient, some customers might wait longer than necessary at the less
                                             					 efficient target. To avoid this potential problem, you can use the Minimum
                                             					 Expected Delay selection rule instead. |
| Minimum
                                             					 Average Queue Delay (Min AvgQD) | Services and
                                             					 Enterprise Services | Evaluate:
                                             					 MIN (*.AvgDelayQTo5) | Selects the
                                             					 target in the set with shortest average hold times, assuming that agents at
                                             					 each target are equally efficient. Because this selection rule evaluates the
                                             					 historical average, it does not select a target based on the current or
                                             					 expected future state of the contact center. Therefore, unexpected load
                                             					 imbalances may occur when you use this rule. To avoid this potential problem,
                                             					 you can use the Minimum Expected Delay selection rule instead. |
| Minimum
                                             					 Longest Delayed Call (Min Delay) | Services and
                                             					 Enterprise Services | Evaluate:
                                             					 MIN (*.LongestCallQ) | Selects the
                                             					 target with the shortest longest delayed call. Note: This selection rule
                                             					 evaluates the historical average, not the current or expected future state of
                                             					 the contact center. Routing contacts to the target with the shortest longest
                                             					 delayed call does not immediately change the longest delay value. Therefore,
                                             					 this selection rule may route a disproportionately large number of calls to a
                                             					 single target. To avoid this potential problem, you can use the Minimum
                                             					 Expected Delay selection rule instead. |
| Minimum
                                             					 Expected Delay (MED) | Services and
                                             					 Enterprise Services | Evaluate:
                                             					 MIN (*.ExpectedDelay) | Selects the
                                             					 target with the shortest expected delay. In making this evaluation, this
                                             					 selection rule considers the average handle time, the number of contacts in
                                             					 queue, and the number of positions staffed. This rule is usually the most
                                             					 effective rule for keeping queue times to a minimum. The MED algorithm is not
                                             					 supported on Unified CCE. |

| Step 1 | Enter a condition in the Consider if field to test potential
                                       			 targets against. |
|---|---|
| Step 2 | Enter a formula by which to distribute contacts in the Distribute
                                       			 by field. |
| Step 3 | Optionally, add comments and connection labels. |

| Note | The Route Select Node supports Target Requery. |
|---|---|

| Step 1 | To select the Route select type, click Change . The Route Select Type dialog box
                                       opens: For Target Type, select Agent , Enterprise Service , Enterprise
                                                Skill Group , Service , Service Array , or Skill
                                                Group . If you selected Enterprise Service or Enterprise Skill
                                             Group, select a Business Entity and Enterprise target . Select Distribute among targets or Select most eligible target . Figure 29. Route Select Type with Select most eligible target Option Figure 30. Route Select Type with Distribute among targets Option If you selected Select most eligible target , select Pick the target with the minimum value or Pick the target with the maximum value . In the Accept target if field, enter a condition that the target must meet to be selected. Select Start with first target or Start with next target . For more information, see Types of Target Searching . Unlike the Select most eligible target option to pick targets, where the Call Router scans all eligible targets (the ones that satisfy the Consider If condition),
                                             based on either a Minimum or Maximum value of a parameter, the Distribute among targets option attempts to pick targets based on an algorithm such that targets with higher weightage or “Distribute By” expression
                                             tend to get picked over the others. The Distribute among targets option sums up all the values for each valid/eligible target (those that satisfy the Consider If condition), and then multiplies
                                             the sum by a random factor using the rand() method to get a random number between 0 and the sum of values of the targets by
                                             using something like below: random = sum * ((double)rand() / (double)RAND_MAX); The constant RAND_MAX is the maximum value that can be returned by the rand() function. RAND_MAX is defined as the value 0x7fff. It then scans the list of targets again among the eligible ones and keeps adding the individual values defined under the “Distribute
                                                By” column to a running sum value. The Call Router picks the first target whose value when added to the running summation,
                                                is higher than the random number derived by the formula above (between 0 and the sum of all eligible targets). So, targets
                                                with higher values tend to get picked for the call over others, thereby achieving a sort of load balancing among the targets. In the Target references field, select Explicit
                                                target references to use direct references to
                                             targets, or Lookup target references by
                                                expression to use expressions that evaluate to
                                             names of targets. Note Lookup target references by
                                                expression is not available when an External Authorization server is used with Internet Script Editor and will be grayed out in the
                                             interface. Optionally, check Enable target requery . Click OK . |
|---|---|
| Step 2 | The fields in the Route Select Properties dialog box change
                                       depending on your route select type selections. Enter and select
                                       data appropriate for the type you selected. |
| Step 3 | Click Validate to check whether the targets you
                                       defined are valid. Correct any errors that are flagged. |
| Step 4 | Optionally, add connection labels. |

| Step 1 | Choose an option
                                       			 from the Select agent
                                          				by drop-down list: Peripheral
                                             				  number - To select a peripheral and a provide formula that translates to the
                                             				  agent's peripheral number. Enterprise
                                             				  Name - To select the agent from the list of configured agents. Skill target
                                             				  ID - To select the agent by providing an expression that translates into the
                                             				  agent's SkillTargetID. In the supervisory case, the expression should use the
                                             				  call's PreferredAgentID. |
|---|---|
| Step 2 | Based on your
                                       			 selection in Step 1, select the peripheral or agent, or enter an expression, as
                                       			 necessary. |
| Step 3 | Optionally,
                                       			 check or uncheck Fail node if
                                       			 agent is unavailable: When checked, the success branch of the Agent to Agent node is run and the router sends the call if the router finds a valid
                                             label for the agent, the agent is available, and the agent state is Ready. The failure branch of the Agent to Agent node is run if the router does not find a valid label for the agent, or the agent
                                             is not available or the agent is in TempUnavailable mode (the router has just send a call to the agent). When not checked, the success branch of the Agent to Agent node is run and the router sends the call if the router finds a
                                             valid label for the agent. The failure branch of the Agent to Agent node is run if the Router does not find a valid label
                                             for the agent. |
| Step 4 | Optionally, add
                                       			 comments and connection labels. |
| Step 5 | Optionally, check Enable Target Requery . |

| Note | Before you can successfully use an ICM Gateway node in a script, you must use the Unified ICM Configuration Manager to configure a gateway to the Unified ICM system to which you send the request. For more information,
                                       see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
|---|---|

| Step 1 | In the Send tab: Select the gateway to Unified ICM system (and hence the
                                             specific Unified ICM instance) from the ICM Gateways list to
                                             which you want to send the request. Check Validate returned labels to have
                                             Unified ICM validate the returned labels. Specify whether Calling Line ID masking instructions
                                             should be applied before the request is passed to the other
                                             Unified ICM system. The Calling Line ID masking refers to
                                             when the caller's phone number is modified so that Unified
                                             ICM application does not display all of the digits; this is
                                             used in a NAM environment, where NAM sends the call to a
                                             customer Unified ICM. Choose one of the following: 1) Do not apply masking rule - If selected, masking instructions are ignored. 2) Apply masking rule if call is presentation restricted - If selected, applies masking instructions if the call variable CLIDRestricted is set to 1. 3) Always apply masking rule - If selected, masking instructions are always applied. Note The Calling line ID masking rule is set through the Unified ICM Configuration
                                                   Manager's System Information dialog box. | Note | The Calling line ID masking rule is set through the Unified ICM Configuration
                                                   Manager's System Information dialog box. |
|---|---|---|---|
| Note | The Calling line ID masking rule is set through the Unified ICM Configuration
                                                   Manager's System Information dialog box. |
| Step 2 | In the Default Label tab: Figure 34. ICM Gateway Properties In the Available Labels list, select one default label for
                                             each routing client to be used by the targeted Unified ICM
                                             system. Click Add to move the selected label to
                                             the Selected labels list. |
| Step 3 | Optionally, add comments and connection labels. |

| Note | The Calling line ID masking rule is set through the Unified ICM Configuration
                                                   Manager's System Information dialog box. |
|---|---|

| Service Requested Variable | Description |
|---|---|
| 0 = ROUTE_SERVICE_REQUEST_NONE | No service requested. |
| 1 = ROUTE_SERVICE_REQUEST_VOICE_CALLBACK | Caller is requesting a voice callback. |
| 2 = ROUTE_SERVICE_REQUEST_TRANSFER | Transfer a task that is already assigned to an agent back to a queue. |
| 3 = ROUTE_SERVICE_REQUEST_RONA | A task is being rerouted on no answer (RONA). |
| 4 = ROUTE_SERVICE_REQUEST_PICK_EXT_QUEUE | Pick a task that is associated external application queue for a specified agent. |
| 5 = ROUTE_SERVICE_REQUEST_PULL_EXT_QUEUE | Pull a task that is associated external application queue for a specified agent. |
| 6 = ROUTE_SERVICE_REQUEST_PICK_UCCE_AGENT | Pick a task that is already assigned to another agent for a specified agent. |
| 7 = ROUTE_SERVICE_REQUEST_TRANSFER_PICK | Transfer a task that is already assigned to an agent directly to another agent, instead of back to a queue. |

| Note | You can enable the Target Requery feature for CVP, ICM to ICM gateway, and a subset of the supported carrier NICs. You cannot
                                          use the requery feature with any of the multimedia requests because the MR PG does not support requery mechanism. |
|---|---|

| Note | In a Queue node, just one target is used.  If the router fails to route to the target node, the failure path of the
                                          node is  taken immediately. To implement requery in a Queue node, you can create a script that increases the
                                          priority and requeries the call from the failure path to the same
                                          queue. |
|---|---|

| Requery Status Variable | Description |
|---|---|
| REQUERY_ANSWER (0) | Script ends. The call
                                             was successfully sent to the chosen target. Note This variable is used internally  by  the CallRouter.  You cannot test for this variable in an IF node. | Note | This variable is used internally  by  the CallRouter.  You cannot test for this variable in an IF node. |
| Note | This variable is used internally  by  the CallRouter.  You cannot test for this variable in an IF node. |
| REQUERY_ROUTE_SELECT_FAILURE (1) | Routing client generated an error code from
                                             ReRouteReq msg indicating a Route Select failure. |
| REQUERY_CALLED_PARTY_BUSY (2) | Routing client generated error code from
                                             ReRouteReq msg indicating the called party is busy. |
| REQUERY_NO_ANSWER (3) | Routing client generated an error code from
                                             ReRouteReq msg indicating no answer. |
| REQUERY_ERROR (4) | CallRouter generated an error code. The attempt to
                                             send the call to target failed because the target
                                             was not reachable (i.e., busy, ring no answer). |
| REQUERY_ABORTED (5) | The attempt to send the call to a target failed because the caller abandoned before the call could be delivered to its destination.
                                             In the case of ABANDON and DISCONNECT, the CallRouter assumes the call has ended and ends the script. The RequeryStatus value
                                             is set to 5, indicating REQUERY_ABORTED. Note This variable is used internally by the CallRouter. You cannot test this variable in an IF node. | Note | This variable is used internally by the CallRouter. You cannot test this variable in an IF node. |
| Note | This variable is used internally by the CallRouter. You cannot test this variable in an IF node. |
| REQUERY_TIMED_OUT (6) | The call attempt failed because the routing client did not respond to the router within the DivertOnBusyCallTimeout period
                                             (180 seconds by default). If the target node has Router Requery enabled, when DivertOnBusyCallTimeout period expires, the
                                             Router closes the Router Requery with REQUERY_TIMED_OUT . Note This variable is used internally by the CallRouter. You cannot test this variable in an IF node. | Note | This variable is used internally by the CallRouter. You cannot test this variable in an IF node. |
| Note | This variable is used internally by the CallRouter. You cannot test this variable in an IF node. |

| Note | This variable is used internally  by  the CallRouter.  You cannot test for this variable in an IF node. |
|---|---|

| Note | This variable is used internally by the CallRouter. You cannot test this variable in an IF node. |
|---|---|

| Note | This variable is used internally by the CallRouter. You cannot test this variable in an IF node. |
|---|---|

| Note | Scheduled Targets do not support Target Requery. |
|---|---|

| Step 1 | Open the node properties. |
|---|---|
| Step 2 | Click Change . A dialog box opens. |
| Step 3 | Check Enable target requery . |
| Step 4 | Click OK to close the dialog box. |
| Step 5 | Click OK to close the properties dialog box. |
| Step 6 | For the Label, Select and Precision Queue nodes: For the Label and Select nodes: Open the node properties. Check Enable Target Requery . Click OK to close the properties dialog box. |

| Step 1 | In the Call Tracer window, choose a Media Domain as voice, a Routing Client, and a Dialed Number. |
|---|---|
| Step 2 | Optionally, enter an ANI (callers telephone number). |
| Step 3 | If you want to test a response from a VRU routing script,
                                       enter values in Caller-Entered-Digits (CED) and VRU Responses
                                       for External Script. |
| Step 4 | To use Network Transfer Call, a feature that
                                       integrates Unified ICM Post-Routing function with a carrier
                                       network's call control ability so that a call can be
                                       transferred anywhere in the network without the use of
                                       transfer/connect services or inter-site tie lines: Select Use Network Transfer. Select a routing client and a Dialed Number value. |
| Step 5 | Click Send Call to submit the request. The
                                       results appear in the Call Trace Results field. |
| Step 6 | To send additional calls, optionally change any of the call
                                       parameters and then click Send Call again. The
                                       Call Trace Results field is updated. |
| Step 7 | Unified ICM runs only installed scripts in response to requests from the Call Tracer. Any uninstalled changes in scripts
                                       are not reflected in the Call Tracer results. |

| Step 1 | In the Call Tracer window, choose a Media Domain other than a voice call, a Routing Client, and a Script Selector. |
|---|---|
| Step 2 | Optionally, enter an Application String 1 and Application String 2. |
| Step 3 | For tracing PICK/PULL request. Select a Service Type , and choose a Queue Type Enter a Queue ID and select the CCUM/system Peripherals with a Preferred Agent . |
| Step 4 | Click Send Call to submit the request. The results appear in the Call Trace Results field. |
| Step 5 | To send additional calls, optionally change any of the call parameters and then click Send Call again. The Call Trace Results field is updated. |
| Step 6 | Unified ICM runs only installed scripts in response to requests from the Call Tracer. Any uninstalled changes in scripts
                                       are not reflected in the Call Tracer results. |

| Step 1 | In the Call Tracer dialog box, click Add . The
                                       VRU Response dialog box opens. |
|---|---|
| Step 2 | Select the type of response (Fail, No Response, Response) the
                                       Call Tracer is to simulate. |
| Step 3 | If you chose Response in Step 2, optionally specify values to
                                       be returned for CED and Variable1 through Variable10. |
| Step 4 | Click OK to apply changes and close the
                                       dialog box. |

| Note | You can also set the initial condition of the 10 call variables for
                                       the first run of the External Script. |
|---|---|