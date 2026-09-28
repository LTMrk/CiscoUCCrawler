---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-administrat-9879618db3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/administration/guide/ucce_b_administration-guide-for-cisco-unified12_5/ucce_b_administration-guide-for-cisco-unified12_5_chapter_010.html
retrieved_at: 2026-08-16T20:47:24.628645+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

Updated: February 7, 2019

Chapter: Desktop Feature Config

## Chapter: Desktop Feature Config

# Desktop Feature Config

## Agent Feature
                        	 Configuration with Agent Desk Settings List Tool

You must associate
                              		  each voice Agent record with an agent desk
                                 			 setting (not necessary for non-voice agents). You can use the agent desk
                              		  settings list tool configuration to associate a set of permissions or
                              		  characteristics with specific agents. You can use the agent desk settings list
                              		  tool to configure the following agent features:

Agent Wrap-up

Reason Codes

Redirection on
                                    				No Answer

Emergency and
                                    				Supervisor Assist Calls

In Parent/Child
                                          			 deployment type, the agent name is automatically configured for the customer.
                                          			 Spaces are not allowed in agent IDs. In a specific scenario, if a child agent
                                          			 is created with a space or a "-", in either the First Name or Last Name field,
                                          			 the name are not created on the parents.

For any change, you perform in the Agent Desk Settings to take effect, log out and then log in to the Finesse Agent Desktop.

### Agent Wrap-Up

Agents can enter Wrap-up mode after completing a call. Wrap-up mode
                                 		  enables the agent to finish with any tasks that require after-call work before
                                 		  entering a Ready state. When in Wrap-up mode, the agent is not routed any
                                 		  additional tasks.

Agents can manually enter Wrap-up state by activating the wrap-up
                                 		  button on their soft phone. You can also configure agent desk settings so that
                                 		  agents automatically enter Wrap-up mode after finishing each call.

When you create agent desk settings using the Unified ICM/Unified CCE Administration User Interface, you can specify whether
                                 agents enter Wrap-up mode automatically after finishing incoming calls. The Work Mode Settings allow you to specify whether
                                 the agent must enter Wrap-up mode after incoming calls. You can also use these settings to require agents to enter reason
                                 codes while in Wrap-up mode (incoming calls only).

### Reason Codes

Agents select Reason Codes when they:

Log out of the agent desktop system

Enter Wrap-up mode after a call

Change to a Not Ready state

Reason Codes allow you to track the agent's state and logout status as it changes. You configure Reason Codes using the agent
                                 desktop application.

### Agent Desk Settings
                           	 That Affect Reason Codes

Agent desk
                                             						setting option

Affects
                                             						this type of reason code

Work mode
                                             						on Incoming

Wrap-up

Idle reason required

Not Ready

Logout
                                             						reason required

Logout

Wrap-Up Reason Codes and Work
                                    			 Mode

If you use the agent desktop, you can use the Work Mode on Incoming option on the agent desk settings list window to specify
                                 when and if agents are required to enter Reason Codes when entering Wrap-up for incoming calls. The following table describes
                                 Work Mode on Incoming options and explains how Reason Codes are related to each.

Work Mode

Description

Reason
                                             						Code

Required

Ensures
                                             						that the agent automatically enters Wrap-up state after completing the call.

The agent
                                             						can choose to enter a Reason Code.

Optional

Allows
                                             						agents to choose whether to activate the wrap-up button or the Not Ready button at the end of the call.

If the
                                             						agent uses the wrap-up button, the agent can choose to enter a Reason Code.

Not
                                             						Allowed

Restricts
                                             						the agent from entering Wrap-up mode. The agent can go into Not Ready mode.

The agent
                                             						can decide whether to enter a Not Ready Reason Code.

Required
                                             						with wrap-up data

Ensures
                                             						that the agent automatically enters Wrap-up state after completing the call.

The agent
                                             						must enter a Reason Code.

### Predefined Reason Codes

Unified CCE uses several predefined reason codes to indicate certain
                                 		  system events, described in the following table.

Reason Code

Description

32767

Agent state changed because the agent did not answer the
                                             						call.

50001

The CTI client disconnected, logging the agent out.

50002

A CTI component failed, causing the agent to be logged out or set to Not Ready. This could be due to closing the agent desktop
                                             application, heartbeat time out, a CTI Server failure, or CTI server client failure (like Finesse.)

50003

Agent was logged out because the Unified CM reported the
                                             						device out of service.

50004

Agent was logged out due to agent inactivity as configured
                                             						in agent desk settings.

50005

For a Unified CCE agent deployment, where the Agent Phone
                                             						Line Control is enabled in the peripheral and the Non ACD Line Impact is
                                             						configured to impact agent state, the agent is set to Not Ready while
                                             						talking on a call on the Non ACD line with this reason code.

50010

Agent was set to Not Ready state because the agent was
                                             						routed two consecutive calls that did not arrive.

50020

Agent was logged out when the agent's skill group
                                             						dynamically changed on the Administration & Data Server.

50030

If an agent is logged in to a dynamic device target that is
                                             						using the same dialed number (DN) as the PG static device target, the agent is
                                             						logged out.

50040

Mobile agent was logged out because the call failed.

50041

Mobile agent state changed to Not Ready because the call
                                             						fails when the mobile agent's phone line rings busy.

50042

Mobile agent was logged out because the phone line
                                             						disconnected while using nailed connection mode.

-1

Agent reinitialized (used if peripheral restarts).

-2

PG reset the agent, usually due to a PG failure.

-3

An administrator modified the agent's extension while the
                                             						agent was logged in.

These reason codes appear in these reports:

Agent log out reports if the event caused the agent to log out.

Agent real time reports if the agent was set to a Not Ready state.

Agent Not Ready reports.

Important

### Redirection on No
                           	 Answer

You can configure
                                 		  your Unified CCE system to handle and accurately report on situations when the
                                 		  agent does not answer their phone. These situations are referred to as
                                 		  Redirection on No Answer.

Although you can
                                 		  specify some values that control Redirection on No Answer situations,
                                 		  configuring Redirection on No Answer involves additional steps:

Unified
                                       				ICM/Unified CCE configuration

Unified
                                       				ICM/Unified CCE scripting

Unified CM
                                       				configuration

Redirection on No Answer conditions are handled by two routing scripts: the initial routing script and a script specifically
                                 set up for these conditions. The initial routing script handles the incoming call; when the call is redirected on no answer
                                 from the agent's IP phone, the script branches to another script set up specifically for Ring No Answer conditions. For more
                                 information on Redirection on No Answer, see the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1001/products_user_guide_list.html .

### Emergency and Supervisor Assist Calls

Agents can activate Supervisor Assist or Emergency Assist buttons on
                                 		  their desktop when they need special assistance from the primary or secondary
                                 		  supervisor assigned to their team.

Agents can use the Supervisor and Emergency assist features,
                                 		  regardless of whether or not they are on a call.

There are two types of Supervisor and Emergency Assist calls:

Existing call—Consult must be selected as an option on
                                       					 the agent desktop settings for supervisor or emergency assist. If the agent is
                                       					 on a call when they activate either the supervisor or emergency assist feature
                                       					 on their desktop, the CTI software activates the conference key on behalf of
                                       					 the agent's phone and calls the supervisor via the Supervisor or Emergency
                                       					 Assist script. (This example assumes the emergency or supervisor assist script
                                       					 has an Agent-to-Agent node to find a supervisor.) The supervisor answers the
                                       					 call and consult privately with the agent. During the consultation, the
                                       					 supervisor can decide to barge into the call.

No call—If the agent is not on a call when they
                                       					 activate either the supervisor or emergency assist feature on the agent's
                                       					 desktop, the CTI software activates the make call functionality on behalf of
                                       					 the agent's phone and calls the supervisor via the Supervisor or Emergency
                                       					 Assist script.

## Agent
                        	 Reskilling

Unified Contact Center includes the CCE web Administration application, which is a browser-based application and is  separate
                              from the supervisor desktop. CCE web administration lets supervisors change the skill group designations of agents on their
                              team, quickly view skill group members, and view details on individual agents.

If an agent is
                                                				  currently in a call, a change to the agent's skill group membership takes place
                                                				  after the call has terminated.

## Skill Groups and Precision Queues per Agent Limit

Unified ICM and Unified CCE impose a default limit on the number of skill groups and precision queues that you can assign
                              to a single agent. After this limit is reached, you cannot reassign additional skill groups or precision queues.

You can also use the Configuration Limit tool to specify your own limit on the number of skill groups and precision queues
                              that you can assign to an agent. For optimum performance, you can specify a limit far lower than the system default.

For more information, see the Dynamic Limits for Skill Groups and Precision Queues Per Agent topic in the Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1) and later at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

Caution

The Configuration Limit tool is a command-line tool utility from the bin directory of all Unified ICM and Unified CCE Administration
                                          & Data Servers. Access is limited to users with privileges for  Config Users for the chosen customer instance. For more information about the Configuration Limit tool, see Outbound Option Guide for Unified Contact Center Enterprise .

### Modify the Precision Queues and Skill Groups per Agent Limit

Complete the following steps to view and modify the current limit on the precision queues per agent and skill groups per agent
                                 using the Configuration Limit tool:

Step 1

From the Windows menu, select Start > Run , type configlimit , and then click Enter .

Run the Configuration Limit tool on the same machine as the Distributor for the instance you want to configure. If more than
                                                         one instance of the Administration & Data Server is installed on the Distributor machine, use the Select Administration Server
                                                         tool to select the instance you want to configure.

Step 2

To view the current configuration limit, run the following command:

```
cl /show
```

Step 3

To change the current limit, enter a command in the following format:

```
cl /id 1 /value [ConfigLimitCurrentValue] [/update]
```

Where:

id 1 = the ID of the skill groups/precision queues per agent limit.

ConfigLimitCurrentValue = the parameter limit. In this case, the parameter limit applies to both the skill groups per agent
                                                   and the number of precision queues per agent.

For example, to change the precision queues/skill groups per agent limit to 50, enter the following:

```
cl /id 1 value/50 /update
```

Using the Configuration Limit tool, you can change the ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue.

### Additional Requirements

#### Lowering the Limit

If you have modified the skill groups per agent
                                 limit to be lower than the system default, no additional changes are necessary.
                                 The new, lower limit is enforced immediately. Note that the new limit does not impact agents whose existing skill group membership
                                 exceeds the new limit until the next attempt to add a new skill group for those
                                 agents. At that time the new limit is enforced, preventing you from adding
                                 additional skill groups.

#### Exceeding the Default Limit

If you have modified the skill groups per agent limit
                                 to be higher than the system default (in spite of the Warning given above),
                                 certain deployments require additional changes (listed in the following
                                 sections) to your system to use the new limit and allow you to add
                                 additional skill groups.

#### IPCC Gateway PG

For IPCC Gateway deployments, modify the following registry keys on your
                                 		IPCC Gateway PGs to include the new value. A change to the registry
                                 		requires that you restart the PG service.

IPCC Enterprise Gateway PIM (Cisco Unified Contact Center Enterprise
                                 		parent):

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<
                                    		  customer_instance
                                    		  >\PG{n}[A|B]\PG\CurrentVersion\PIMS\pim{m}\ACMIData\Config\MaxSkills

IPCC Express Gateway PIM (Cisco Unified Contact Center Express parent):

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<
                                    		  customer_instance
                                    		  >\PG{n}[A|B]\PG\CurrentVersion\PIMS\pim{n}\ACMIData\Config\MaxSkills

## Network Transfer for IVRs

When a call is transferred from an IVR (for example, IP IVR) to an
                              		  agent and that agent wants to transfer the call to another agent, the transfer
                              		  can be made either from the agent's IP phone or the agent desktop.

Transfers made from the:

IP phone are made using CTI route points that point to a Unified
                                    				ICM/Unified CCE script.

Agent desktop are made using the Dialed Number Plan.

For network transfer from either the IP phone or the agent desktop, you must queue the call to the skill group in the first
                              Unified ICM/Unified CCE script; for example, "NetXfer1," to create the call context. In this script you must set the "networkTransferEnabled" flag to "1" .

## Unified CCE Routing

To understand how Unified CCE routes voice calls, you must understand
                           		the concepts of routing operation and routing configuration.

### Routing Operations

To understand how Unified CCE routing occurs, you must understand
                                 		  these concepts:

The Routing Client: The Unified CCE component that submits
                                       				a route request to the Central Controller.

In Unified CCE configurations, the routing client can be:

The Unified CM PG

An interexchange carrier (IXC)

A VRU PG

A Media Routing Peripheral Gateway

When a routing client makes a request for a route
                                       				from the Unified ICM/Unified CCE platform, it receives the response and delivers the
                                       				call to the specified destination. If an Unified CCE agent is available,
                                       				Unified ICM/Unified CCE software routes the call to the device target (phone) on the
                                       				Unified CM (device targets are dynamically associated with the agent when the
                                       				agent logs in to the system). If an agent is not available, you can configure Unified ICM/Unified CCE
                                       				software  to queue the call to IP IVR or Unified CVP.

Route and Queuing Requests: Messages sent from the routing
                                       				client to the Central Controller. Route requests typically pass along call
                                       				detail information about the incoming call. Unified ICM/Unified CCE software uses
                                       				information in the route request to determine which routing script is run
                                       				for the call.

Call detail information sent with the route request can include:

Dialed Number (DN)

Calling line ID (CLID)

Caller Entered Digits (CED)

Queueing requests are messages sent from the VRU using the Cisco
                                       				Service Control Interface. The VRU makes a queue request to provide
                                       				announcements or music when no Unified CCE agents are available to take the
                                       				call.

About Routing to the VRU with Unified CCE: With Unified CCE
                                       				you can ensure that voice calls are routed to the VRU when an agent is not
                                       				immediately available. The call is queued to the VRU and sent to the next
                                       				available agent via the routing script.

The configurations for routing to a VRU in a Unified CCE
                                       				environment include:

Translation Route to the VRU via a route on the PG. The
                                             					 Unified CM uses the DNIS in the translation route to direct the call to the
                                             					 VRU.

A network route request is issued by the carrier via the NIC.
                                             					 The DNIS and/or Correlation ID is retrieved from the carrier.

The call is sent directly to the VRU, so that caller entered
                                             					 digits (CED) can be collected.

You do not need a translation route to a Unified CM PG because it is
                                       				targeting agents and implicitly matches call data.

Routing a Call to the VRU: Translation routing is the
                                       				preferred method of routing a call to the VRU. The DNIS used in the translation
                                       				route is not the original number dialed by the customer, but rather, the Dialed
                                       				Number used to route the call to the VRU.

The scenario is as follows:

Call comes in to the Unified CM.

Unified CM identifies the number as a route point for the
                                             					 Unified CM PG.

The Unified CM PG receives a route request from the Unified CM and forwards it to the CallRouter.

The CallRouter runs the script for the translation route to
                                             					 the VRU.

A Label is returned to the Unified CM via the Unified CM PG.

The Unified CM routes the call to the VRU, based on the CTI
                                             					 route point for the translation route.

VRU sends up a request instruction with the DN as the DNIS.

VRU PG matches up the call and the Correlation ID, then
                                             					 informs the CallRouter of the call arrival with a "request instruction."

The CallRouter matches the correlation ID and finds the
                                             					 pending script/call.

The CallRouter continues with script (for example, run
                                             					 script).

For translation routing, the VRU Type to configure in the Network VRU in the Unified ICM/CCEho Administration User Interface
                                             is type 2.

Be sure the Unified CM PG routing client and the VRU PG
                                             					 routing client both have the labels mapped for the peripheral targets in the
                                             					 translation route.

### Routing
                           	 Configuration

To set up routing in
                                 		  your Unified CCE system, you must set up the following entities:

Dialed Numbers: The
                                       				dialed number is the number that the caller dials to contact an agent. It is
                                       				sent as part of the call detail information in the route request message sent
                                       				from the routing client.

In the system
                                       				software, you set up a Dialed Number List. It identifies all of the phone
                                       				numbers in your contact center that customers can dial to initiate contact.

The Dialed
                                       				Number plays an integral role in routing calls. Dialed Numbers are required
                                       				pieces of Unified ICM call types that are used to identify the appropriate
                                       				routing script for each call.

Call Types: A call type
                                       				is a category of incoming Unified ICM routable tasks. Each call type has a
                                       				schedule that determines which routing script or scripts are active for that
                                       				call type at any time. There are two classes of call types: voice (phone calls)
                                       				and non-voice (for example, email and text chat). Voice call types are
                                       				categorized by the dialed number (DN), the caller-entered digits (CED) and the
                                       				calling line ID (CLID). Non voice call types are categorized by the Script Type
                                       				Selector, Application String 1, and Application String 2. In either case, the
                                       				last two categories of the call type can be optional. For voice call types, the
                                       				caller-entered digits and the calling line ID can be optional, depending on the
                                       				call. For non voice call types, Application String 1 and Application String 2
                                       				can be optional, depending on the application.

Because the call
                                       				type determines which routing script is run for a call, the call type defines
                                       				call treatment in a Unified CCE system. Therefore, the call type is the highest
                                       				level reporting entity. Reporting on call type activity provides insight into
                                       				end-to-end customer interactions with the system and with agents by providing
                                       				data such as service level adherence, transfers, average speed of answer, calls
                                       				handled, and calls abandoned.

In routing
                                       				scripts, such as scripts for Self-Service VRU applications, you may change the
                                       				call type at specific points in the script to indicate that a transaction has
                                       				been completed. For example, if the customer is calling a bank and successfully
                                       				checks their account balance using a Self-Service script, you may want to
                                       				change the call type to indicate that the account balance transaction has
                                       				completed and a new transaction has begun.

You can also
                                       				change the call type in a script to invoke a new routing script associated with
                                       				that call type. For example, if a call is not answered at an agent's desktop,
                                       				you can change the call type in the script to redirect the call to a different
                                       				script designed for Redirection on No Answer. The Redirection on No Answer
                                       				script assigns a different agent to handle the call.

Routes: Unified
                                       				ICM/Unified CCE software uses routes to define the mapping of a target to a
                                       				specific label for a routing script. Targets include services (service
                                       				targets), skill groups (skill targets), agents (device targets), and
                                       				translation routes.

Routes must be
                                       				defined for VRU Translation Routing and to route calls to agents.

Device Targets: Device
                                       				targets are deprecated. A device target is a telephony device that can be
                                       				uniquely addressed (or identified) by a telephone number. A device target is
                                       				not associated with any one peripheral. Each device target must have one or
                                       				more labels associated with it, although only one label may exist per routing
                                       				client. Replace device targets with Agent
                                          				  Targeting Rules , which greatly simplifies call routing configuration.

Labels: A label is the
                                       				value that Unified ICM/Unified CCE software returns to a routing client
                                       				instructing it where to send the call. The routing client can map the label to
                                       				an announcement, a trunk group and DNIS, or a device target. Special labels
                                       				might instruct the routing client to take another action, such as playing a
                                       				busy signal or an unanswered ring to the caller.

If the label is
                                       				for a device target, the routing client is responsible for delivering the call
                                       				to the device target on the Unified CM through the voice gateway.

If the label is
                                       				for a VRU queue point, the routing client delivers the call to the Route Point
                                       				on the VRU. The VRU must recognize that the call has arrived and then request
                                       				queue instructions from Unified ICM/Unified CCE software. Unified ICM/Unified
                                       				CCE software returns either a destination for the call or instructions on what
                                       				script the VRU will run, based on a particular Call Type.

Services: You set up
                                       				Services in Unified ICM/Unified CCE software to represent the type of
                                       				processing that a caller requires, and to configure VRU Services to route calls
                                       				to the VRU. For example, you might define separate services for Sales, Support,
                                       				or Accounts Payable. A Service is often associated with a peripheral and can be
                                       				referred to as a Peripheral Service.

For Services
                                       				that are used to route a call to an agent, you must associate them with skill
                                       				groups. You associate different Skill Groups with Services by making them
                                       				members of the Service. Using Services allows you to group agents working in
                                       				like skill groups.

Skill Groups: Agents must be associated with skill groups to receive Unified ICM-routed calls. You create skill groups using the Unified
                                       ICM/Unified CCE Administration User Interface.

A base skill group is the main skill group created using the Unified ICM/Unified CCE Administration User Interface. Using base skill groups
                                       ensures accurate agent reporting and simplifies configuration and scripting for your contact center.

Agents must be
                                       				associated with skill groups or precision queues.

A sub-skill group is a subdivision of a base skill group. Sub-skill groups are not supported since Unified CCE 9.0(1); the only instance where
                                                   they are still supported is for Avaya PG and Avaya Aura PG peripherals in Unified ICM deployments. You cannot create a sub-skill group for the System PG, CallManager, and ARS PG peripheral types. You can only remove sub-skill groups
                                                   from these peripheral types. Sub-skill groups are also not supported for non-voice skill groups. You cannot create sub-skill
                                                   groups for chat and email.

Precision Queues: You
                                       				can create multidimensional precision queues based on predefined business
                                       				criteria using the Unified CCE Web Administration. Agents automatically become
                                       				members of these precision queues based on their attributes, dramatically
                                       				simplifying configuration and scripting.

Migrating from Sub-skill
                                          				  Groups to Base or Enterprise Skill Groups

Follow these
                                       				steps to migrate from sub-skill groups to base and enterprise skill groups:

Disable
                                             					 the sub-skill group mask for the peripheral using the PG Explorer tool. All
                                             					 skill groups created after you complete this are base skill groups.

Define a
                                             					 new base skill group to correspond with each sub-skill group being removed.

Assign
                                             					 agents to the new base skill groups and remove them from your sub-skill groups.

Optionally, create enterprise skill groups to group the base
                                             					 skill groups.

Update all
                                             					 of your routing scripts and routing templates so that they refer to the newly
                                             					 created base or enterprise skill groups.

### Routing Scripts

A routing
                                 script, created using the Script Editor, identifies the desired agent based
                                 upon skills and customer database profile, determines the call target, and
                                 returns a route response to the routing
                                 client.

| Note | In Parent/Child
                                          			 deployment type, the agent name is automatically configured for the customer.
                                          			 Spaces are not allowed in agent IDs. In a specific scenario, if a child agent
                                          			 is created with a space or a "-", in either the First Name or Last Name field,
                                          			 the name are not created on the parents. |
|---|---|

| Note | For any change, you perform in the Agent Desk Settings to take effect, log out and then log in to the Finesse Agent Desktop. |
|---|---|

| Agent desk
                                             						setting option | Affects
                                             						this type of reason code |
|---|---|
| Work mode
                                             						on Incoming | Wrap-up |
| Idle reason required | Not Ready |
| Logout
                                             						reason required | Logout |

| Work Mode | Description | Reason
                                             						Code |
|---|---|---|
| Required | Ensures
                                             						that the agent automatically enters Wrap-up state after completing the call. | The agent
                                             						can choose to enter a Reason Code. |
| Optional | Allows
                                             						agents to choose whether to activate the wrap-up button or the Not Ready button at the end of the call. | If the
                                             						agent uses the wrap-up button, the agent can choose to enter a Reason Code. |
| Not
                                             						Allowed | Restricts
                                             						the agent from entering Wrap-up mode. The agent can go into Not Ready mode. | The agent
                                             						can decide whether to enter a Not Ready Reason Code. |
| Required
                                             						with wrap-up data | Ensures
                                             						that the agent automatically enters Wrap-up state after completing the call. Note This
                                                      						mode is not supported for outgoing calls. | Note | This
                                                      						mode is not supported for outgoing calls. | The agent
                                             						must enter a Reason Code. |
| Note | This
                                                      						mode is not supported for outgoing calls. |

| Note | This
                                                      						mode is not supported for outgoing calls. |
|---|---|

| Reason Code | Description |
|---|---|
| 32767 | Agent state changed because the agent did not answer the
                                             						call. |
| 50001 | The CTI client disconnected, logging the agent out. Note This reason code is converted to a 50002, so 50001 does
                                                      						not display in the agent log out records. | Note | This reason code is converted to a 50002, so 50001 does
                                                      						not display in the agent log out records. |
| Note | This reason code is converted to a 50002, so 50001 does
                                                      						not display in the agent log out records. |
| 50002 | A CTI component failed, causing the agent to be logged out or set to Not Ready. This could be due to closing the agent desktop
                                             application, heartbeat time out, a CTI Server failure, or CTI server client failure (like Finesse.) |
| 50003 | Agent was logged out because the Unified CM reported the
                                             						device out of service. |
| 50004 | Agent was logged out due to agent inactivity as configured
                                             						in agent desk settings. |
| 50005 | For a Unified CCE agent deployment, where the Agent Phone
                                             						Line Control is enabled in the peripheral and the Non ACD Line Impact is
                                             						configured to impact agent state, the agent is set to Not Ready while
                                             						talking on a call on the Non ACD line with this reason code. |
| 50010 | Agent was set to Not Ready state because the agent was
                                             						routed two consecutive calls that did not arrive. |
| 50020 | Agent was logged out when the agent's skill group
                                             						dynamically changed on the Administration & Data Server. |
| 50030 | If an agent is logged in to a dynamic device target that is
                                             						using the same dialed number (DN) as the PG static device target, the agent is
                                             						logged out. |
| 50040 | Mobile agent was logged out because the call failed. |
| 50041 | Mobile agent state changed to Not Ready because the call
                                             						fails when the mobile agent's phone line rings busy. |
| 50042 | Mobile agent was logged out because the phone line
                                             						disconnected while using nailed connection mode. |
| -1 | Agent reinitialized (used if peripheral restarts). |
| -2 | PG reset the agent, usually due to a PG failure. |
| -3 | An administrator modified the agent's extension while the
                                             						agent was logged in. |

| Note | This reason code is converted to a 50002, so 50001 does
                                                      						not display in the agent log out records. |
|---|---|

| Important | For reporting on all PGs other than VRU PGS, be sure to select the Agent event detail check box on the Agent Distribution tab in the Unified ICM/Unified CCE Administration User Interface's PG Explorer tool.
                                          You must select this check box to report on Not Ready Reason Codes. |
|---|---|

| Note | The Target
                                          		  Requery script feature, implemented using the Label, Queue, Route Select, and
                                          		  Select nodes, is not supported for Unified CCE systems; however, it is
                                          		  supported for Cisco Unified Customer Voice Portal (Unified CVP). |
|---|---|

| Note | Blind Conference is not supported for Emergency and Supervisor
                                          		  Assist. |
|---|---|

| Note | If an agent is
                                                				  currently in a call, a change to the agent's skill group membership takes place
                                                				  after the call has terminated. |
|---|---|

| Caution | The Configuration Limit tool is a command-line tool utility from the bin directory of all Unified ICM and Unified CCE Administration
                                          & Data Servers. Access is limited to users with privileges for  Config Users for the chosen customer instance. For more information about the Configuration Limit tool, see Outbound Option Guide for Unified Contact Center Enterprise . |
|---|---|

| Step 1 | From the Windows menu, select Start > Run , type configlimit , and then click Enter . Note Run the Configuration Limit tool on the same machine as the Distributor for the instance you want to configure. If more than
                                                         one instance of the Administration & Data Server is installed on the Distributor machine, use the Select Administration Server
                                                         tool to select the instance you want to configure. | Note | Run the Configuration Limit tool on the same machine as the Distributor for the instance you want to configure. If more than
                                                         one instance of the Administration & Data Server is installed on the Distributor machine, use the Select Administration Server
                                                         tool to select the instance you want to configure. |
|---|---|---|---|
| Note | Run the Configuration Limit tool on the same machine as the Distributor for the instance you want to configure. If more than
                                                         one instance of the Administration & Data Server is installed on the Distributor machine, use the Select Administration Server
                                                         tool to select the instance you want to configure. |
| Step 2 | To view the current configuration limit, run the following command: cl /show |
| Step 3 | To change the current limit, enter a command in the following format: cl /id 1 /value [ConfigLimitCurrentValue] [/update] Where: id 1 = the ID of the skill groups/precision queues per agent limit. ConfigLimitCurrentValue = the parameter limit. In this case, the parameter limit applies to both the skill groups per agent
                                                   and the number of precision queues per agent. For example, to change the precision queues/skill groups per agent limit to 50, enter the following: cl /id 1 value/50 /update Note Using the Configuration Limit tool, you can change the ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue. | Note | Using the Configuration Limit tool, you can change the ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue. |
| Note | Using the Configuration Limit tool, you can change the ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue. |

| Note | Run the Configuration Limit tool on the same machine as the Distributor for the instance you want to configure. If more than
                                                         one instance of the Administration & Data Server is installed on the Distributor machine, use the Select Administration Server
                                                         tool to select the instance you want to configure. |
|---|---|

| Note | Using the Configuration Limit tool, you can change the ConfigLimitCurrentValue only. You cannot change the ConfigLimitDefaultValue. |
|---|---|

| Note | If the route point is configured using Unified CM, there is no
                                       		  difference between using the hard phone or the desktop phone. |
|---|---|

| Note | IP IVR does not support network transfer. Unified CVP 
                                       		  supports only network "blind" transfer. |
|---|---|

| Note | A sub-skill group is a subdivision of a base skill group. Sub-skill groups are not supported since Unified CCE 9.0(1); the only instance where
                                                   they are still supported is for Avaya PG and Avaya Aura PG peripherals in Unified ICM deployments. You cannot create a sub-skill group for the System PG, CallManager, and ARS PG peripheral types. You can only remove sub-skill groups
                                                   from these peripheral types. Sub-skill groups are also not supported for non-voice skill groups. You cannot create sub-skill
                                                   groups for chat and email. |
|---|---|