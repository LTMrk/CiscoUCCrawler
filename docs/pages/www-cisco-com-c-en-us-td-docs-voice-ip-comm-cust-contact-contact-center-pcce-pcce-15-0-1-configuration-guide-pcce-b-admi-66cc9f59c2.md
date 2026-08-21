---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-configuration-guide-pcce-b-admi-66cc9f59c2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/configuration/guide/pcce_b_admin-and-config-guide-15_0_1/pcce_m_scripting-specifics-in-a-packaged-cce-environment_15_0.html
retrieved_at: 2026-08-21T16:50:42.223358+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Scripting Specifics in a Packaged CCE Environment

## Chapter: Scripting Specifics in a Packaged CCE Environment

# Scripting Specifics in a Packaged CCE Environment

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

A script that routes to Packaged CCE agents needs to check for an available agent within a skill group. If an agent is not available, then the script should use
                              a Queue to Skill Group node. The script execution ends when an agent becomes available or when the caller disconnects.

## Scripts for Precision Queues

To implement Precision Routing in your contact center, you must create scripts.

You can create and use configured (static) and dynamic precision queue nodes in your scripts.

Static precision queue nodes target a single, configured precision queue. When the script utilizes a single precision queue,
                                 use static precision queues.

Dynamic precision queue nodes are used to target one or more previously configured precision queues. Use dynamic precision
                                 queues when you want a single routing script for multiple precision queues (for example, when the overall call treatment does
                                 not vary from one precision queue to another). Dynamic precision queues can simplify and reduce the overall number of routing
                                 scripts in the system.

### Precision Queue
                           	 Script Node

Use the Precision
                              		Queue script node to queue a call based on caller requirements until an agent
                              		with desired proficiency become available. This node contains multiple agent
                              		selection criteria which are separated into steps.

A single call can be queued on multiple precision queues. If an agent becomes available in one of the precision queues, the
                              call is routed to that resource. You cannot reference multiple precision queues with a single Precision Queue node. However,
                              you can run multiple Precision Queue nodes sequentially to achieve this.

The Precision Queue
                              		node includes a Priority field, which sets the initial queuing priority for the
                              		calls processed through this node versus other calls queued to the other
                              		targets using different nodes. The priority is expressed as an integer from 1
                              		(top priority) to 10 (least priority). The default value is 5.

If more than one call
                              		is queued to a precision queue when an agent becomes available, the queued call
                              		with the lowest priority number is routed to the target first. For example,
                              		assume an agent in a precision queue becomes available and two calls are queued
                              		to that precision queue. If one call has priority 3 and the other has priority
                              		5, the call with priority 3, the lower value, is routed to the precision queue
                              		while the other call continues to wait. If the priorities of the two calls are
                              		same, then the call queued first is routed first.

VRU (voice response unit) script instructions are not sent to the VRU. If a call enters the precision queue node and no resource
                              is available, the call is queued to the precision queue and the node transfers the call to the default VRU, if the call is
                              not already on a VRU. The script flow then exits immediately through the success branch. The script should then continue with
                              a run external script node to instruct the VRU what to do while holding the call until an agent becomes available. Typically,
                              this invokes a network VRU script that plays music-on-hold, possibly interrupted on a regular basis with an announcement.
                              The script flow can also use other queuing nodes to queue the same call to other targets, for example, Queue to Skill Group
                              and Queue to Agent.

Non-voice tasks can also be picked
                                          				or pulled out of turn from queues, not necessarily based on the priority of the
                                          				call. Such non-voice tasks that are picked or pulled by a specific agent, require a
                                          				Pick/Pull node to be used in the ICM script. However, the agents belonging to other
                                          				skill groups or precision queues can also pick tasks that may be queued in Skill
                                          				Groups or Precision Queues other than their own. These are denoted by Picked by another
                                             					Skillgroup/PQ or Pulled
                                             					by another Skillgroup/PQ monitor labels, when viewing the scripts in monitor
                                          				mode.

### Configure a Static
                           	 Precision Queue

Step 1

In the Precision
                                             				Queue Properties dialog box, select the Statically option.

Step 2

From the list,
                                          			 select a precision queue to which to route all calls that enter this node.

Step 3

In the Priority
                                             				selection box, select the initial queuing priority for calls
                                          			 processed through this node. You can select from 1 - 10. The default is 5.

Step 4

Check the Enable
                                             				target requery check box to enable the requery feature for calls
                                          			 processed through this node.

Step 5

Check the Wait if Agents Not Logged In check box.

Step 6

To edit a
                                          			 precision queue, select a precision queue from the list, and then click Edit
                                             				Precision Queue .

### Configure a Dynamic
                           	 Precision Queue

Step 1

In the Precision
                                             				Queue Properties dialog box, select the Dynamically option.

Step 2

In the Priority
                                             				selection section, select the initial queuing priority for calls
                                          			 processed through this node. You can select from 1 - 10. The default is 5.

Step 3

Check the Enable
                                             				target requery check box to enable the requery feature for calls
                                          			 processed through this node.

Step 4

Check the Wait if Agents Not Logged In check box.

Step 5

Select a queue
                                          			 option:

- To dynamically route calls
                                             				that enter this node to a precision queue name, select the Precision Queue Name option.

- To dynamically route calls
                                             				that enter this node to a precision queue ID, select the Precision Queue ID option.

Step 6

Click Formula
                                             				Editor to create a formula that determines the precision queue name
                                          			 or ID to which to route calls.

### Queuing Behavior of
                           	 the Precision Queue Node

Precision queues internally are configured with one or more time-based steps, each with a configured wait time. After a call
                              is queued, the first step begins and the timer starts. This occurs although the path of the script exited the success node
                              and a new node may be targeted (for example, Run Ext. Script).

If the timer for the first step expires, control moves to the second step (assuming one exists), and so on. As long as the
                              call remains in queue and there are steps left to perform, the call internally continues to move between steps regardless
                              of the path the call takes after it leaves the precision queue node. If a call is queued to two or more precision queues,
                              the call internally walks through the steps for each precision queue in parallel. After the call reaches the last step on
                              a precision queue, it remains queued on that step until the call is routed, abandoned, or ended.

If there is an update to the precision queue definition, then all queued calls in the precision queue are re-evaluated and
                              are re-run from the first step.

For example, consider the wait time for an ongoing call at step 1 to be 1080 seconds, of which 1000 seconds has already elapsed.
                              Now, suppose the wait time is changed to 900 seconds, then the wait time for this call is also reset to 900 seconds, even
                              though only 80 more seconds are left to move to the next step.

## Cancel Queuing Node

If the call needs to be taken out of a skill group, then use the Cancel
                              Queuing node. The Cancel Queuing node takes the call out of all the skill
                              groups it is queued to.

## End Node

The End node  either tries default routing, or if there is no default
                              label, it sends an error (dialog fail) to the routing client.

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

## Unified CVP as a queue point

Packaged CCE relies on the Unified CVP to queue the call while it is waiting for an available agent.

The Unified CCE Packaged CCE sends the call to the Unified CVP port for queuing:

To provide the
                                    				call with a termination point that allows the VoIP Gateway to return the
                                    				correct signals or messages back to the PSTN.

Provide
                                    				announcements or music or expected wait time or initial position in queue to
                                    				the caller while they are waiting for an agent. Allow the caller an option to
                                    				leave a message if the caller does not want to wait for an agent.

To obtain
                                    				further information from the caller that is not sent from the network

The Unified CVP lets Unified CCE Packaged CCE know when the caller disconnects through the Event Report Message with an Event Type of either DISCONNECT or ABANDON. When
                              an agent becomes available, Unified CCE Packaged CCE automatically instructs Unified CVP to route the call to the agent through the Connect message.

### Interruptible vs. Non-interruptible

If the VRU script is collecting digits from the customer to
                                 ascertain information regarding the caller that is crucial for a screen
                                 pop or call routing, put the VRU script in a non-interruptible
                                 mode.

If a call was queued to a skill group through a Queue to Skill Group node and then sent to VRU to hear a non-interruptible
                                 VRU script, if during the time that the caller is interacting and listening to the non-interruptible VRU script, an agent
                                 becomes available, the call will not be connected to the agent. The Unified CCE Packaged CCE only looks for available agents for that call when the VRU script is finished and the call runs an interruptible node such
                                 as a Wait node or a Run External Script node for a VRU script that is interruptible. The call does, however, maintain its
                                 place in the queue so when the call does become available for an agent, it is answered before calls that came in afterward
                                 it (assuming the same priority).

For announcement and music type of treatments, put the VRU Scripts in
                                 interruptible mode. This allows the call to be connected to the first
                                 available agent even while the caller is listening to a VRU script.

You set the interruptibility of a VRU script through the Network VRU Scripts gadget in the Unified CCE Administration Web tool . Neither the VRU or the Unified CCE Packaged CCE script can overwrite this setting.

| Note | Non-voice tasks can also be picked
                                          				or pulled out of turn from queues, not necessarily based on the priority of the
                                          				call. Such non-voice tasks that are picked or pulled by a specific agent, require a
                                          				Pick/Pull node to be used in the ICM script. However, the agents belonging to other
                                          				skill groups or precision queues can also pick tasks that may be queued in Skill
                                          				Groups or Precision Queues other than their own. These are denoted by Picked by another
                                             					Skillgroup/PQ or Pulled
                                             					by another Skillgroup/PQ monitor labels, when viewing the scripts in monitor
                                          				mode. |
|---|---|

| Step 1 | In the Precision
                                             				Queue Properties dialog box, select the Statically option. |
|---|---|
| Step 2 | From the list,
                                          			 select a precision queue to which to route all calls that enter this node. |
| Step 3 | In the Priority
                                             				selection box, select the initial queuing priority for calls
                                          			 processed through this node. You can select from 1 - 10. The default is 5. |
| Step 4 | Check the Enable
                                             				target requery check box to enable the requery feature for calls
                                          			 processed through this node. |
| Step 5 | Check the Wait if Agents Not Logged In check box. If this check box is selected and the agents associated with this step are not logged in, then the router waits for the time
                                          that is configured for that step. Whereas, if this check box is not selected, the router does not wait on any step. Note The router waits indefinitely on the last step, irrespective of the selection of this check box. | Note | The router waits indefinitely on the last step, irrespective of the selection of this check box. |
| Note | The router waits indefinitely on the last step, irrespective of the selection of this check box. |
| Step 6 | To edit a
                                          			 precision queue, select a precision queue from the list, and then click Edit
                                             				Precision Queue . |

| Note | The router waits indefinitely on the last step, irrespective of the selection of this check box. |
|---|---|

| Step 1 | In the Precision
                                             				Queue Properties dialog box, select the Dynamically option. |
|---|---|
| Step 2 | In the Priority
                                             				selection section, select the initial queuing priority for calls
                                          			 processed through this node. You can select from 1 - 10. The default is 5. |
| Step 3 | Check the Enable
                                             				target requery check box to enable the requery feature for calls
                                          			 processed through this node. |
| Step 4 | Check the Wait if Agents Not Logged In check box. If this check box is selected and the agents associated with this step are not logged in, then the router waits for the time
                                          that is configured for that step. Whereas, if this check box is not selected, the router does not wait on any step. Note The router waits indefinitely on the last step, irrespective of the selection of this check box. | Note | The router waits indefinitely on the last step, irrespective of the selection of this check box. |
| Note | The router waits indefinitely on the last step, irrespective of the selection of this check box. |
| Step 5 | Select a queue
                                          			 option: To dynamically route calls
                                             				that enter this node to a precision queue name, select the Precision Queue Name option. To dynamically route calls
                                             				that enter this node to a precision queue ID, select the Precision Queue ID option. |
| Step 6 | Click Formula
                                             				Editor to create a formula that determines the precision queue name
                                          			 or ID to which to route calls. |

| Note | The router waits indefinitely on the last step, irrespective of the selection of this check box. |
|---|---|