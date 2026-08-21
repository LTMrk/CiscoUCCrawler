---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--83c64bc65d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/ucce_b_scripting-and-media-routing-guide_12_6/ucce_b_scripting-and-media-routing-guide_chapter_01011.html
retrieved_at: 2026-08-21T11:54:55.420317+00:00
---

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

# Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

Updated: June 11, 2020

Chapter: Scripting Specifics in CCE Environment

## Chapter: Scripting Specifics in CCE Environment

# Scripting Specifics in CCE Environment

## Unified CCE Gateway

The Unified CCE Gateway PG allows a site Unified CCE system to connect to a Unified ICM. The Unified ICM parent views the
                              system as an
                              ACD.

This view is important because it allows a "parent" Unified ICM to monitor and send calls to a "child" Unified CCE system.
                              Previous to the availability of the Unified CCE Gateway feature, monitoring this using intelligent (PG-based) routing was
                              not possible. This allows improved scaling, resiliency, and simpler, more standardized scripting across sites.

The Unified CCE Gateway PG looks to the Unified ICM like any other PG; it does not
                              look like Unified CCE. The Gateway PG  has a Peripheral type to allow
                              connection to a "child" Unified CCE system.
                              The child system is listed as "Unified CCE Gateway" in the setup screen for the PG. The Gateway PG does not support
                              third-party call control (CTI) so that all agent desktops, etc., are
                              connected to the child Unified CCE system. The link
                              supports voice only. The child system may support multi-media but the Unified
                              ICM only routes voice calls to the child.

Object tracking is accomplished the same as on all legacy PIMs, through matching Peripheral Numbers on the agent, skill group,
                              and service table. Routing to the child is to peripheral targets (skill groups/services) as with all legacy TDMs, in contrast
                              to the Unified CCE. The usual TDM functionality is supported: Pre-Routing, Pre-Routing with Translation routing, post routing,
                              etc. Third-party call control is the only exception. Full variable passing is done between the parent and child (you can send/receive
                              call variables 1-10 and ECC variables).

Scripting is consistent with traditional PGs, not Unified CCE. Scripts use
                              LAA, MED, target services, and skill groups; but not agents.

### Deployment of Unified CCE Gateway for Unified CCE

Where to deploy Unified CCE Gateway for Unified
                                 CCE:

The gateway PG is ideal for deployments that have several call
                                       centers spread geographically.

The call centers are independent of the Central Controller so
                                       in a WAN outage, the call centers (System PG systems) can
                                       operate totally independently of Unified ICM.

The gateway PG is also an ideal way to integrate new IP call
                                       centers into an existing Unified ICM environment with many TDM
                                       ACD sites.

How does it work:

The gateway PG works by monitoring all the events that happen
                                       on the child Unified CCE system. This is identical in function
                                       to a PG/PIM connected to any other ACD. By knowing the active
                                       call and agent states the Unified ICM router can have information
                                       available to decide if that "site" is the best to send a call
                                       to.

The child system can also send up route requests to the parent
                                       Unified ICM to decide where to send a call (Post/Translation
                                       routing).

The event monitoring is accomplished by the PIM connecting to
                                       the child systems CTI Server modified version of the CTI
                                       Protocol.

Object Mapping Overview (Enterprise)

Agents on the child map to agents on the parent

Skill groups on the child map to skill groups on the
                                       parent

Call Types on the child map to services on the parent.

## Unified CCE

This topic contains information for
                           writing routing scripts when Unified ICM is part of a Unified CCE
                           environment.

## Prioritize Agents

Step 1

Use a Select node and group the agents that have a higher
                                       priority in a skill group in the first Select Longest Available
                                       Agent (LAA) node,

Step 2

Look for available agents in a subsequent Select node that have
                                       another lower priority grouping of agents.

### What to do next

This is done in the case where there are idle agents when a call comes in.
                              The order of the Select nodes within the script determines the agent
                              prioritization.

## Call Priority

When a call is queued to a skill group because there are no agents
                              available, the Queue to Skill Group node sets the call's priority. The Queue
                              Priority node can then promote the call's priority based on time the caller
                              has waited. The call can be queued to multiple skill groups with the same or
                              different priorities.

If there are calls in the agent's skill group queues when an agent becomes available, the agent is presented with the highest
                              priority (1-20 with 1 being the highest priority) call that has waited the longest within the skill group(s) that the agent
                              is assigned to.

## Check for Available Agents

A script that routes to Unified CCE agents needs to check for an available agent within a skill group. If an agent is not available, then the script should use
                              a Queue to Skill Group node. The script execution ends when an agent becomes available or when the caller disconnects.

## Select Node

You can use the
                              		  Select node to check for the Longest Available Agent (LAA). However, the Select
                              		  node cannot check for Minimum Expected Delay (MED) of a service, because
                              		  Unified CCE skill groups do not have a valid expected delay because the calls
                              		  in the queue are on Unified IP IVR PG service.

By default, the
                              		  Queue to Skill Group node uses LAA for agent selection. Do not put LAA Select
                              		  nodes before or after a Queue to Skill Group node for the same skill group. You
                              		  can only use this node if the call is not already queued to a skill group.

There is, however, a
                              		  lengthy workaround to determine the MED for a call using an IF node.

## Queue to Skill Group
                        	 Node

If agents are assigned to
                              			 base skill groups, use base skill groups in this node.

If the script has both Queue
                              		  to Skill Group and Queue to Enterprise Skill Group nodes, then do not include
                              		  skill groups defined within the Queue to Skill Group nodes that belong to the
                              		  enterprise skill groups that are defined within the Queue to Enterprise Skill
                              		  Group node.

## Cancel Queuing Node

If the call needs to be taken out of a skill group, then use the Cancel
                              Queuing node. The Cancel Queuing node takes the call out of all the skill
                              groups it is queued to.

## Busy Node

Use the Busy node for initial overflow conditions. Do not use this
                              treatment if the call has already received ringback tone or given
                              announcements or music. If a Busy CTI Route point and CTI port are defined
                              on Unified IP IVR and the Cisco Unified Communications Manager, then Unified IP IVR 
                              tells Cisco Unified Communications Manager to return a busy signal. If a Busy CTI
                              Route point and CTI port are not defined on Cisco Unified Communications Manager and
                              Unified IP IVR and the call is already connected to an Unified IP IVR port,
                              then Unified IP IVR port plays a busy tone from a .wav file for 30
                              seconds and then disconnects the call. If the VRU port plays a busy tone from
                              a .wav file then, answer supervision returns to the far end. This
                              causes charges to occur for the call. If the call is a toll free call
                              (for example, 800#), then the Contact Center accrues the charges;
                              otherwise the caller has to pay.

You must define a  Busy CTI route point and one CTI port on the Cisco
                              Unified Communications Manager and associated it with the Unified IP IVR user. The one CTI
                              port can be used for multiple calls. In Unified IP IVR Administration, a new
                              CTI Route point of Type Busy and a CTI port need to be defined whose Dialed
                              Numbers match what was previously defined on the Cisco Communications Manager.

Define a label of type busy with a Label field that corresponds to the
                              aforementioned CTI Route point dialed Number in the Cisco Unified Communications Manager
                              and Unified IP IVR.

If the call is not at a VRU port and the Busy CTI Route point is not
                              defined on the Cisco Unified Communications Manager and the Unified IP IVR, and the  Unified ICM
                              returns a busy label to the Cisco Unified Communications Manager, the Cisco Unified Communications
                              Manager returns a fast busy to the caller for 30 seconds and then the call
                              is disconnected.

## Ring Node

You can use the Ring node for diverting blocked list callers. It is supported as a post route from the Cisco Unified Communications
                              Manager. The call is given ringback tone until the caller ends the call. No answer supervision is returned for this call because
                              it is not connected to a VRU port. This means that if this is the initial treatment given the caller, then no charges will
                              be accrued for this call.

You need to define a Ring No Answer CTI port group in the Cisco Unified Communications
                              Manager, but you do not have to define CTI ports. In Unified IP IVR
                              Administration, you need to define a new CTI Route Point of Type Ring No
                              Answer whose Dialed Number matches what was previously defined on the Cisco
                              Unified Communications Manager.

Define a label of type Ring with a Label field corresponds to the CTI
                              Route Point Dialed Number in Cisco Unified Communications Manager and Unified IP
                              IVR.

## Release Call Node

Use the Release Call node for initial overflow conditions. It is supported
                              as a post route from the Cisco Unified Communications Manager. Do not use this node if
                              the call has already received ringback tone or announcements or music. The
                              call is given busy tone for 30 seconds before it is disconnected on
                              the Cisco Unified Communications Manager. No answer supervision is returned for
                              this call because it is not connected to a CTI port. This means that no
                              charges will be accrued for this call.

No configuration needs to be done within the Cisco Unified Communications Manager or
                              Unified IP IVR. No label needs to be defined within Unified ICM.

## End Node

The End node  either tries default routing, or if there is no default
                              label, it sends an error (dialog fail) to the routing client.

## Call Treatment Comparison

Attributes/Treatment

Busy Node

Ring Node

Release Node

End Node

Answer Supervision

No if Busy CTI Route Point defined

Yes if Busy CTI
                                          Route Point not defined

No

No

No

Voice port required

Yes (only 1 CTI port needed)

No

No

No

Timing

Initial treatment only

Anytime

Initial treatment only

Initial treatment only

Applications

Overflow Conditions

Blocked list Callers

Overflow Conditions

Overflow Conditions

Treatment provided by Unified IP IVR

Unified IP IVR

Cisco Unified Communications Manager

Cisco Unified Communications Manager

## Agent to Agent Node

You can use the Agent to Agent node for agent to agent transfers; the
                              router checks agent availability before sending the call to the agent. If
                              the agent is not available, the script queues the call to a skill group. You can also use the 
                              Agent to Agent node to send a call to the agent: the
                              "caller" is not required to be an agent.

For a transfer to  a specific target agent, the initiating agent enters the target agent ID. The DNP entry matching the dialed
                              number (agent ID) must have a DNP type of PBX. For this DNP type, the PIM enters the dialed number (agent ID) into the Caller-Entered
                              Digits (CED) field while sending the route request to the Router. To have the Router handle the call properly, specify the
                              CED field as the location of the agent ID in the Agent to Agent node.

Agent IDs must not match any of the extensions on the Unified Communications Manager cluster. If you make all agent IDs of
                              the same length and begin with the same number, a generic wildcard string can match all agent IDs. With that wildcard string,
                              you need only one entry in the DNP for agent-to-agent routing.

The agent-to-agent node requires that you specify the PIM. If your environment has multiple PIMs, use an agent ID number plan
                              to determine which PIM contains an agent. Agent IDs are associated with a specific PIM and are not unique by themselves. You
                              can set up a consistent agent ID assignment plan (such as, all agent IDs on PIM 1 begin with 1, and so on). That pattern enables
                              you not to repeat agent IDs across the enterprise. Then, you can parse the CED field in the script editor to determine which
                              PIM contains a specific agent.

## Service and Enterprise Service Nodes

You do not need the Service node or Enterprise Service node to route calls
                              to Unified CCE agents because services are not required for Unified CCE
                              agents.

## Scheduled Select and Divert Label Nodes

Cisco Communications Manager does not support the Scheduled Select node
                              and Divert Label node. You cannot use these nodes to route calls to Unified
                              CCE agents.

## Unified IP IVR as a queue point

Unified CCE relies on the Unified IP IVR to queue the call while it is waiting for an available agent.

The Unified ICM sends the call to the VRU port for queuing:

To provide the
                                    				call with a termination point that allows the VoIP Gateway to return the
                                    				correct signals or messages back to the PSTN.

Provide
                                    				announcements or music or expected wait time or initial position in queue to
                                    				the caller while they are waiting for an agent. Allow the caller an option to
                                    				leave a message if the caller does not want to wait for an agent.

To obtain
                                    				further information from the caller that is not sent from the network

The Unified IP IVR lets Unified ICM know when the caller disconnects through the Event Report Message with an Event Type of either DISCONNECT or ABANDON.
                              When an agent becomes available, Unified ICM automatically instructs Unified IP IVR to route the call to the agent through the Connect message.

### Interruptible vs. Non-interruptible

If the VRU script is collecting digits from the customer to
                                 ascertain information regarding the caller that is crucial for a screen
                                 pop or call routing, put the VRU script in a non-interruptible
                                 mode.

If a call was queued to a skill group through a Queue to Skill Group or Queue to Enterprise Skill Group node and then sent to VRU to hear a non-interruptible VRU script, if during the time that the caller is interacting and listening
                                 to the non-interruptible VRU script, an agent becomes available, the call will not be connected to the agent. The Unified ICM only looks for available agents for that call when the VRU script is finished and the call runs an interruptible node such
                                 as a Wait node or a Run External Script node for a VRU script that is interruptible. The call does, however, maintain its
                                 place in the queue so when the call does become available for an agent, it is answered before calls that came in afterward
                                 it (assuming the same priority).

For announcement and music type of treatments, put the VRU Scripts in
                                 interruptible mode. This allows the call to be connected to the first
                                 available agent even while the caller is listening to a VRU script.

You set the interruptibility of a VRU script through the Configuration Manager, under the Add Network VRU script configuration . Neither the VRU or the Unified ICM script can overwrite this setting.

### VRU (IVR) Types

Listed in the table below are the VRU types that are supported for
                                 the Unified CCE. These types are defined in the Unified ICM in the Network VRU
                                 Configuration. These VRU types are used by the Unified ICM to determine the
                                 routing client, routing type, script node used, and VRU port status. Type
                                 3 and  7 can only be Network VRUs. However, Types 2 and 6 can be Network or
                                 On-premise VRUs.

VRU Type

Routing Client

Routing Type

Scripting Node Used to Send to VRU

Unified ICM Knows VRU Port Status

2, 8

Yes

Post-route from Cisco Communications Manager

Translation Route to VRU

Yes

3, 7

No

Pre-route

Send To VRU

No

5, 6

Yes

Post-route from VRU

N/A

Yes

Usually the VRU has been configured to support only one VRU type,
                                 although the Unified IP IVR can support both Type 2 and Type 6 based on
                                 whether the call is routed directly to the VRU or the call comes into a
                                 Translation Route point. In this case, the VRU type must be defined as
                                 Type 2.

### Translation Route to VRU Node

The Translation Route to VRU node is used by Type 2 VRUs that are post
                                 routed from the Cisco Unified Communications Manager, when the call is not at the
                                 VRU, but at another routing client. The call can be a pre-route from the
                                 IXC or it can be a post route from a Cisco Unified Communications Manager CTI
                                 Route point.

The Translation Route to VRU node is used to send the call
                                 to the VRU port. Translation routing is needed for:

Cradle to grave reporting (Termination Call Detail
                                       Reporting)

Ability to send call context data like the calling line ID or
                                       Dialed Number to the VRU

Ability to check if the VRU peripheral is online or if all VRU
                                       ports are busy before sending the call

The Translation Route to VRU node is typically followed by a Run External Script node. If some checking is done before the
                                 Run External Script node is initiated, the time it takes the Unified ICM to run the nodes in the script must not exceed the
                                 VRU Request Time-out timer. Information obtained from the caller during the VRU session can be passed to the Unified ICM for
                                 further processing.

## No Default Skill Groups in Routing Scripts

Ensure your Unified ICM routing scripts do not reference the default skill
                              group. This ensures that the default skill group does not capture statistics
                              for any Unified ICM-routed calls.

For more information, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide and Administration Guide for Cisco Unified Contact Center Enterprise .

## Router Behavior (During PG Failure)

In a Unified CCE environment, if the router is disconnected from the two
                              PGs (available on either side of the network/site between the routers) and
                              the PG fails, the router cannot receive any information about the failure
                              of the peripheral or about agents who are logged out. In such a scenario,
                              the router uses low frequency heartbeats (60 seconds) to determine the
                              failure of the peripheral and declares the peripheral to be offline at this
                              point. The router discards the real time values for the peripheral
                              (including service, skill group, enterprise agent, and agent state at their
                              last known value) and continues to send calls to these agents who were in
                              the "Ready" state before the connectivity to the PGs was lost. After the
                              router suspends the peripheral and declares it offline, you need to use an "IF" node with "Peripheral.online=1" in the script to avoid sending or
                              queuing calls to an offline peripheral. You should make this change
                              manually.

## Scripts in an Outbound Environment

Outbound Option only supports both Type 2 (Generic PG environment) and Type 9 (Unified CCE System PG environment). For Unified
                              CVP, Outbound Option supports Type 10, Type 7, and Type 5 (Unified CVP Comprehensive Model).

If using the transfer to VRU feature, create a transfer to VRU campaign. Transfer to VRU campaigns might require translation
                              routes if using a Type 2 VRU. For more information about setting up translation routes, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide . (Note that translation routes are not required when using the Unified CCE System PG.)

The transfer to VRU feature is only supported for Outbound Option on Unified CCE. You cannot use this feature in the Direct
                                          Preview or the regular Preview modes.

The dynamic routing client feature is used when an outbound agent
                              transfers a call using the Unified CVP to a Type 2 VRU. Make sure the routing
                              client for the translation route labels is the Cisco Unified Communications Manager,
                              which makes the outgoing call.

### Control OutboundControl Variable and Skill Group Reservation Percentage with Script

Step 1

Open the Unified ICM Script Editor application.

Step 2

Create an administrative script using a Start node, a Set node, an
                                          			 End node, and an If node (all required).

Step 3

Set the OutboundControl variable. OutboundControl Variable
                                          			 Settings:

INBOUND: Indicates that this skill group is disabled for
                                                				  outbound use and only takes inbound calls.

PREDICTIVE_ONLY: Dials several customers per agent. After
                                                				  reaching a live contact, the Predictive Dialer transfers the customer to a live
                                                				  agent along with a screen pop to the agent’s desk. The predictive algorithm is
                                                				  designed to calculate the number of lines to dial per available agent to keep
                                                				  agent wait time to a minimum.

PREDICTIVE_BLENDED: Agents receive inbound calls, but could be
                                                				  used for an outbound call when available.

PREDICTIVE_BLENDED: Agents receive inbound calls, but could be
                                                				  used for an outbound call when available.

PREVIEW_ONLY: Reserves an agent prior to initiating an
                                                				  outbound call and presents the agent with a screen pop. The agent might
                                                				  then Accept the call: Dials the customer and transfers the call to the
                                                				  agent. Skip the call: Agent receives another customer
                                                				  call. Skip-Close the call: Skips the current preview call and closes the
                                                				  record so it cannot be called again. Reject the call: Releases the
                                                				  agent. At this point, the system might deliver the agent another preview
                                                				  outbound call or a new inbound call. Reject-Close the call: Rejects the
                                                				  current preview call and closes the record so it cannot be called again.

PREVIEW_BLENDED: Agents receive inbound calls, but could be
                                                				  used for an outbound preview call when available.

PREVIEW_DIRECT_ONLY: Agents can only place outbound calls and
                                                				  hear ring tones, such as phone ringing or busy signal.

PREVIEW_DIRECT_BLENDED: Agents can receive inbound calls,
                                                				  place outbound calls, and hear ring tones, such as phone ringing or busy
                                                				  signal.

PROGRESSIVE_ONLY: Similar to PREDICTIVE_ONLY; however, lines
                                                				  to dial per agent is not calculated—users configure a fixed number of lines
                                                				  that will always be dialed per available agent.

PROGRESSIVE_BLENDED: Similar to PREDICTIVE_BLENDED, but a
                                                				  fixed number of lines will always be dialed per available agent.

Verify that the outbound control variable mode is spelled
                                                                     					 correctly.

Make sure that the skill group being controlled is the base
                                                                     					 skill group, and not the primary or secondary skill groups. Although agents may
                                                                     					 be logged into just the primary or secondary skill group, the outbound control
                                                                     					 variable must always be set on the base skill group

If the administrative script (where the OutboundControl
                                                                     					 variable or reservation percentage is set) is running, but the
                                                                     					 modes/percentages are not being updated at the Dialer, perform one of the
                                                                     					 following tasks:

Use the Set node to set skill group variables (OutboundControl
                                                                     				and OutboundPercent).

Step 4

Set the OutboundPercent variable by entering the agent percentage
                                          			 in the Value field of the Set Properties window.  This variable controls the
                                          			 percentage of agents, logged in to a particular skill group, to be used for
                                          			 outbound dialing. For example, if there are 100 agents logged in to skill group
                                          			 N, and the OutboundPercent variable is set to 50%, 50 agents would be allocated
                                          			 for outbound dialing.

This variable does not allocate specific agents for outbound
                                                               				dialing, just a total percentage.

Use the Set node to set skill group variables (OutboundControl
                                                               				and OutboundPercent).

#### What to do next

The following illustration displays a very simple administrative
                                 		  script where both the OutboundControl variable and the outbound percentage are
                                 		  set for a skill group. A script in a production call center is typically be
                                 		  more complex, perhaps changing these variables due to time of day or service
                                 		  level.

For more information about using the Script Editor, see Unified ICM Script Editor online help.

For more information about sample administrative and routing scripts for the Unified CCE System PG, see the 
                                                   		  section for sample
                                                   		  administrative and routing scripts for the Unified CCE System PG.

### Transfer to VRU Using Outbound Option with Unified IP IVR

The following illustration displays a routing script for a transfer to
                                 VRU campaign using the Outbound Option with the Unified IP IVR. (For more information about configuring a Outbound Option
                                 transfer to VRU campaign, see Outbound Option Guide for Unified Contact Center Enterprise .)

### Transfer to VRU Campaign Using Outbound Option with Unified CVP

The following illustration displays a routing script for a transfer to
                                 VRU campaign using the Outbound Option with the Unified CVP. (For more information  about configuring a Outbound Option transfer
                                 to VRU campaign, see Outbound Option Guide for Unified Contact Center Enterprise .)

Use the Unified ICM Script Editor application to create a routing script
                                 that uses the Dialed Number for the MR routing client, and routes
                                 through a Select node to the previously configured skill group.

Use the Unified ICM Script Editor Call Type Manager to associate the MR
                                 (and Personal Callback, if used) Dialed Number(s) with the configured
                                 call type and newly created routing script.

The following diagram displays an example routing script that uses the
                                 objects mentioned above.

Translation routes are not used in the Unified CCE System PG, so routing scripts using this PG do not need to use this object.

### Queue to Agent Node Configuration

The following illustration displays the Queue to Agent tab of the
                                 Queue to Agent Properties dialog box.

### Unified CCE System PG for Outbound Option

The Unified CCE System PG combines two PGs (Cisco Communications Manager and
                                 VRU PGs) into one PG and is only supported with Unified IP IVR.

Setting up an Unified CCE System PG for Outbound Option campaigns
                                 consists of two tasks:

Configuring the Unified CCE System PG.

Adding the PG.

Use the Unified ICM Script Editor and create an administrative script. The
                                 following illustration is an example of an administrative script.

The following diagram displays an example routing script using the
                                 Queue to Skill Group node.

| Note | NCT is not supported with the Enterprise Gateway because the CTI control is on the ACD (child) rather than on Unified
                                       ICM parent. |
|---|---|

| Note | In a single script node (MED) peripherals that are legacy and
                                                gateway type can be used to select the best "site" to send the
                                                call to. |
|---|---|

| Note | This is due to the child's reporting being based on Call Types
                                                and the parents reporting being based on services. |
|---|---|

| Step 1 | Use a Select node and group the agents that have a higher
                                       priority in a skill group in the first Select Longest Available
                                       Agent (LAA) node, |
|---|---|
| Step 2 | Look for available agents in a subsequent Select node that have
                                       another lower priority grouping of agents. |

| Attributes/Treatment | Busy Node | Ring Node | Release Node | End Node |
|---|---|---|---|---|
| Answer Supervision | No if Busy CTI Route Point defined Yes if Busy CTI
                                          Route Point not defined | No | No | No |
| Voice port required | Yes (only 1 CTI port needed) | No | No | No |
| Timing | Initial treatment only | Anytime | Initial treatment only | Initial treatment only |
| Applications | Overflow Conditions | Blocked list Callers | Overflow Conditions | Overflow Conditions |
| Treatment provided by Unified IP IVR | Unified IP IVR |  | Cisco Unified Communications Manager | Cisco Unified Communications Manager |

| VRU Type | Routing Client | Routing Type | Scripting Node Used to Send to VRU | Unified ICM Knows VRU Port Status |
|---|---|---|---|---|
| 2, 8 | Yes | Post-route from Cisco Communications Manager | Translation Route to VRU | Yes |
| 3, 7 | No | Pre-route | Send To VRU | No |
| 5, 6 | Yes | Post-route from VRU | N/A | Yes |

| Note | The transfer to VRU feature is only supported for Outbound Option on Unified CCE. You cannot use this feature in the Direct
                                          Preview or the regular Preview modes. |
|---|---|

| Note | The transfer to VRU feature is supported only for the Outbound Option
                                          		  on the Unified CCE. You can not use this feature in the Direct Preview or the
                                          		  regular Preview modes. |
|---|---|

| Step 1 | Open the Unified ICM Script Editor application. |
|---|---|
| Step 2 | Create an administrative script using a Start node, a Set node, an
                                          			 End node, and an If node (all required). |
| Step 3 | Set the OutboundControl variable. OutboundControl Variable
                                          			 Settings: INBOUND: Indicates that this skill group is disabled for
                                                				  outbound use and only takes inbound calls. PREDICTIVE_ONLY: Dials several customers per agent. After
                                                				  reaching a live contact, the Predictive Dialer transfers the customer to a live
                                                				  agent along with a screen pop to the agent’s desk. The predictive algorithm is
                                                				  designed to calculate the number of lines to dial per available agent to keep
                                                				  agent wait time to a minimum. PREDICTIVE_BLENDED: Agents receive inbound calls, but could be
                                                				  used for an outbound call when available. PREDICTIVE_BLENDED: Agents receive inbound calls, but could be
                                                				  used for an outbound call when available. PREVIEW_ONLY: Reserves an agent prior to initiating an
                                                				  outbound call and presents the agent with a screen pop. The agent might
                                                				  then Accept the call: Dials the customer and transfers the call to the
                                                				  agent. Skip the call: Agent receives another customer
                                                				  call. Skip-Close the call: Skips the current preview call and closes the
                                                				  record so it cannot be called again. Reject the call: Releases the
                                                				  agent. At this point, the system might deliver the agent another preview
                                                				  outbound call or a new inbound call. Reject-Close the call: Rejects the
                                                				  current preview call and closes the record so it cannot be called again. PREVIEW_BLENDED: Agents receive inbound calls, but could be
                                                				  used for an outbound preview call when available. PREVIEW_DIRECT_ONLY: Agents can only place outbound calls and
                                                				  hear ring tones, such as phone ringing or busy signal. PREVIEW_DIRECT_BLENDED: Agents can receive inbound calls,
                                                				  place outbound calls, and hear ring tones, such as phone ringing or busy
                                                				  signal. PROGRESSIVE_ONLY: Similar to PREDICTIVE_ONLY; however, lines
                                                				  to dial per agent is not calculated—users configure a fixed number of lines
                                                				  that will always be dialed per available agent. PROGRESSIVE_BLENDED: Similar to PREDICTIVE_BLENDED, but a
                                                				  fixed number of lines will always be dialed per available agent. Note Verify that the outbound control variable mode is spelled
                                                                     					 correctly. Make sure that the skill group being controlled is the base
                                                                     					 skill group, and not the primary or secondary skill groups. Although agents may
                                                                     					 be logged into just the primary or secondary skill group, the outbound control
                                                                     					 variable must always be set on the base skill group If the administrative script (where the OutboundControl
                                                                     					 variable or reservation percentage is set) is running, but the
                                                                     					 modes/percentages are not being updated at the Dialer, perform one of the
                                                                     					 following tasks: Use the Set node to set skill group variables (OutboundControl
                                                                     				and OutboundPercent). | Note | Verify that the outbound control variable mode is spelled
                                                                     					 correctly. Make sure that the skill group being controlled is the base
                                                                     					 skill group, and not the primary or secondary skill groups. Although agents may
                                                                     					 be logged into just the primary or secondary skill group, the outbound control
                                                                     					 variable must always be set on the base skill group If the administrative script (where the OutboundControl
                                                                     					 variable or reservation percentage is set) is running, but the
                                                                     					 modes/percentages are not being updated at the Dialer, perform one of the
                                                                     					 following tasks: Use the Set node to set skill group variables (OutboundControl
                                                                     				and OutboundPercent). |
| Note | Verify that the outbound control variable mode is spelled
                                                                     					 correctly. Make sure that the skill group being controlled is the base
                                                                     					 skill group, and not the primary or secondary skill groups. Although agents may
                                                                     					 be logged into just the primary or secondary skill group, the outbound control
                                                                     					 variable must always be set on the base skill group If the administrative script (where the OutboundControl
                                                                     					 variable or reservation percentage is set) is running, but the
                                                                     					 modes/percentages are not being updated at the Dialer, perform one of the
                                                                     					 following tasks: Use the Set node to set skill group variables (OutboundControl
                                                                     				and OutboundPercent). |
| Step 4 | Set the OutboundPercent variable by entering the agent percentage
                                          			 in the Value field of the Set Properties window.  This variable controls the
                                          			 percentage of agents, logged in to a particular skill group, to be used for
                                          			 outbound dialing. For example, if there are 100 agents logged in to skill group
                                          			 N, and the OutboundPercent variable is set to 50%, 50 agents would be allocated
                                          			 for outbound dialing. Note This variable does not allocate specific agents for outbound
                                                               				dialing, just a total percentage. Use the Set node to set skill group variables (OutboundControl
                                                               				and OutboundPercent). | Note | This variable does not allocate specific agents for outbound
                                                               				dialing, just a total percentage. Use the Set node to set skill group variables (OutboundControl
                                                               				and OutboundPercent). |
| Note | This variable does not allocate specific agents for outbound
                                                               				dialing, just a total percentage. Use the Set node to set skill group variables (OutboundControl
                                                               				and OutboundPercent). |

| Note | Verify that the outbound control variable mode is spelled
                                                                     					 correctly. Make sure that the skill group being controlled is the base
                                                                     					 skill group, and not the primary or secondary skill groups. Although agents may
                                                                     					 be logged into just the primary or secondary skill group, the outbound control
                                                                     					 variable must always be set on the base skill group If the administrative script (where the OutboundControl
                                                                     					 variable or reservation percentage is set) is running, but the
                                                                     					 modes/percentages are not being updated at the Dialer, perform one of the
                                                                     					 following tasks: Use the Set node to set skill group variables (OutboundControl
                                                                     				and OutboundPercent). |
|---|---|

| Note | This variable does not allocate specific agents for outbound
                                                               				dialing, just a total percentage. Use the Set node to set skill group variables (OutboundControl
                                                               				and OutboundPercent). |
|---|---|

| Note | For more information about using the Script Editor, see Unified ICM Script Editor online help. For more information about sample administrative and routing scripts for the Unified CCE System PG, see the 
                                                   		  section for sample
                                                   		  administrative and routing scripts for the Unified CCE System PG. |
|---|---|

| Note | For more information about using Unified ICM Script Editor's features, see the Unified ICM Script Editor online help . |
|---|---|

| Note | Lines connecting objects cannot appear on top of objects and
                                          therefore, partially display under the objects.  For example, the line
                                          connecting the "X" (output terminal failure) on the Select object to the
                                          End object runs partially under the Select object. |
|---|---|

| Note | Translation routes are not used in the Unified CCE System PG, so routing scripts using this PG do not need to use this object. |
|---|---|