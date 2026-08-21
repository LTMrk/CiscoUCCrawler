---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-configuration-guide-pcce-b-admi-294136fdcf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/configuration/guide/pcce_b_admin-and-config-guide_12_5/pcce_b_admin-and-config-guide_12_5_chapter_01010.html
retrieved_at: 2026-08-21T04:44:41.997551+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

Updated: June 11, 2024

Chapter: Network VRUs

## Chapter: Network VRUs

# Network VRUs

## VRU
                        	 Functionality

You can use routing scripts to divert a call to a Network VRU for
                              additional call processing.

A VRU, or Voice
                              		  Response Unit, is a telecommunications device, also called an Interactive Voice
                              		  Response Unit (IVR), that plays recorded announcements and responds to
                              		  caller-entered touch-tone digits. Cisco Unified Customer Voice Portal (CVP) is
                              		  the supported VRU for Packaged CCE. A VRU can also be equipped with Automatic
                              		  Speech Recognition (ASR) or Text-to-Speech (TTS) capabilities.

## Access to VRU Scripts in Unified CCE Packaged CCE Routing Scripts

You can write routing scripts that send calls to the VRU, queue
                              		  the call, and invoke specific VRU scripts. VRU scripts are configured using the
                              		  Network VRU Scripts tool in the Unified CCE Administration tool.

## Send Call to a VRU
                        	 with Send to VRU Node

You can send a call to Unified CVP for further processing by using the Send to VRU node (in the Queue tab of the Palette).

When Unified CCE Packaged CCE runs a Send to VRU Node, it looks up the call's Dialed Number, the Dialed Number's Customer, and the Customer’s Network VRU.
                              If that fails to retrieve a Network VRU, the router uses the system default Network VRU.

There are two
                              		  failure cases:

If the label
                                    				does not exist, script execution continues with control flowing through the
                                    				nodes failure output terminal.

If Unified CCE Packaged CCE does not receive confirmation, execution continues with control flowing through the nodes failure output terminal.

In all other cases
                              		  script execution continues with control flowing through the nodes success
                              		  output terminal.

Notes:

If the Run External Script, Play, Menu, Collect Data, or Queue node is used in a script before a Send To VRU node, an implicit
                                    Send To VRU node is assumed. Y ou do not have to use the Send To VRU node. However, include the node in routing scripts as a visual aid if you ever need
                                    to troubleshoot the script.

If the call is delivered to the Unified CVP but then abandoned, script execution ends. In monitor mode, a special label on the Send To VRU node accounts for these cases.

You do not need to
                              		  set properties for the Send to VRU node. However, you can optionally add
                              		  comments or connection labels.

## Run External
                        	 Scripts

You can use multiple Run External Script nodes to run a series of scripts on the Unified CVP .

The execution of Unified CCE Packaged CCE routing script waits for the external script to finish:

If the external script runs successfully, control then passes through the success branch of the Run External Script node.

If the external script does not run successfully for any reason, then control passes through the failure branch of the Run
                                    External Script node.

If the current call is not at a Unified CVP when the Run External Script node is run, Unified CCE Packaged CCE sends the call to the associated Network VRU, as run a Send to VRU node.

Design scripts so that the Failure branch of a Run External Script Node contains a test for the Call.VRUStatus variable. If
                                                the value is 2, the VRU is likely to be not functioning properly. Therefore, the script avoids executing any subsequent Run
                                                External Script nodes on this Failure branch.

Following is the Properties dialog box for the Run External Script node:

Step 1

Select the Unified CCE Packaged CCE Script/External Script Name you want to run.

Step 2

Optionally, add
                                       			 comments and connection labels.

## VRU Errors

The following table lists the possible values for the VruStatus variable:

Value

Meaning

Description

0

VRU_SUCCESS

The last VRU node was successful.

1

VRU_ERROR

The last VRU node failed because of a routing or
                                          configuration error.

2

VRU_TIMEOUT

The last Send To VRU failed because the routing client did not respond within 20 seconds or the last Run External Script node
                                          failed because the timeout limit defined for the script expired.

3

VRU_ABORTED

The last VRU node did not complete because the caller ended the call or stopped responding. (Because this causes the routing
                                          script to terminate immediately, this value is never seen.)

4

VRU_DIALOG_ FAILED

The last VRU node failed because communication with
                                          the VRU ended unexpectedly.

5

VRU_SCRIPT_ NOT_FOUND

The VRU failed because the referenced VRU script was not found in the Unified CCE Packaged CCE configuration.

6

STATUS_MAX_QUEUE_LIMIT_EXCEEDED

The last node failed because the maximum call queuing limit was exceeded.

7

STATUS_NO_VALID_EXPRESSION

The last node failed because no valid expression was found.

8

STATUS_NO_VALID_TARGET

The last node failed because no valid target was found.

10

STATUS_NO_MRD_MATCH

The last node failed because no targets matched with the Media Routing Domain on the call.

11

STATUS_CONSIDER_IF_FAILED

The last node failed because the Consider If expression failed on all targets.

12

STATUS_NO_VALID_PERIPHERAL

The last node failed because none of the targets were configured on the supported peripheral.

13

STATUS_NO_ONLINE_PERIPHERAL

The last node failed because all targets are on peripherals that are offline.

## Call Queuing at
                        	 VRUs

You can queue a call at a Network VRU until a specific resource becomes available. A call can be queued for one or more skill
                              groups, or a precision queue. As soon as an agent becomes available at one of the specified targets, the call is removed from the queue
                              and sent to the target.

Specifically, you
                              		  can:

Place a call in
                                    				a precision queue.

Place the call in one or more skill groups.

Adjust the priority of call in a queue for one or more skill groups.

Remove the
                                    				current call from any queues to which it is assigned.

Call Flow:

The call is
                                    				first sent to the Network VRU. This step is required before you queue the call.

The call is
                                    				queued for three skill groups.

If the call is successfully queued, the script cycles between a Wait node and a Run External Script node so that the caller
                                    hears an announcement every 30 seconds.

If an agent in one of the skill groups becomes available, the call is removed from queue and taken back from the Unified CVP . Routing script execution ends and the call is delivered to the target.

You could use other nodes like Queue to Skill Group or Queue to Precision Queue to queue the calls to different targets.

Caution

Do not use the nodes like Route Select to queue the calls when the script cycles between a Wait node and a Run External Script
                                                node.

## Place a Call in Queue

If an agent becomes available in one of the skill groups, the call is routed to that resource.

If the current call is not at a Unified CVP when the Queue node runs, Packaged CCE sends the call to the associated Network
                                          VRU. (This does not apply to Type 2 VRUs, which are VRUs at customer premises.)

The Queue node includes a Priority field, which sets the initial queuing priority for the calls processed through this node versus other calls queued for the
                              same target. The priority is expressed as an integer from 1 (top priority) to 20 (least priority). The default value is 5.

If more than one call is queued to a group when an agent becomes available, the queued call with the lowest priority number
                              is routed to the target first. For example, assume an agent in a skill group becomes available and two calls are queued to
                              that skill group. If one call has priority 3 and the other has priority 5, the call with priority 3, the lower value, is routed
                              to the skill group while the other call continues to wait.

The Queue node does not actually result in instructions being sent to the VRU. When queuing occurs the Queue node exits immediately
                                          through the success branch and the call is assumed to be at the VRU; the script should then continue with a Run External Script
                                          node to instruct the VRU what to do while holding the call until an agent to becomes available. Typically this would invoke
                                          a Network VRU script that plays music-on-hold, possibly interrupted on a regular basis with an announcement.

Following is the Properties dialog box for the Queue node:

Step 1

To change the queue type:

Click Change . The Queue Type dialog box opens.

Select a Target Type (Skill Group). You cannot reference more than one type of target within a single Queue node. To queue a call to more than
                                             one target type, run multiple Queue nodes sequentially.

Optionally, select a Priority to set the initial queuing priority for calls processed through this node versus other calls
                                             queued for the same target: 1 for top priority to 20 for least priority. (The default is 5.)

Optionally, check Enable Target Requery .

When Target Requery is enabled in a Queue node and a Requery happens, for example because the call is presented to an available
                                                            agent, but the agent does not answer, the script continues through the failure terminal. The script can then inspect the call
                                                            variable RequeryStatus to determine what to do next. The typical action in case of a No Answer would be to Queue the call
                                                            again, possibly to other skill groups, and possibly increase the priority so that it is taken out of the queue before regular
                                                            queued calls.

Click OK to close the Queue Type dialog box.

Step 2

To add targets:

Click Add Targets . The Add Targets dialog box opens, listing available targets of the type you specified.

Use the Available Targets list and the Add button to select targets.

Click OK to close the Add Targets dialog box. The target members you selected appear in the Properties dialog box.

Step 3

Optionally, continue defining Target Type information for the Route (Drop-down list) member. This is the route to send the call to when an agent in the target type becomes available.
                                          (The drop-down list includes all routes associated with the target.)

Step 4

Optionally, add connection labels.

### What to do next

When processing a Queue node, the router first checks for an available target, if there is none available then the router
                                          attempts to queue the call. The call does not move to the VRU if there is an available agent.

## Precision Queue
                        	 Script Node

You can use the Precision Queue script node to queue a call or task based on caller requirements until agents with desired
                              proficiency become available. This node contains multiple agent selection criterion which are separated into steps.

A single call can be queued on multiple precision queues. If an agent becomes available in one of the precision queues, the
                              call is routed to that resource. You cannot reference multiple precision queues with a single Precision Queue node. However,
                              you can run multiple Precision Queue nodes sequentially to achieve this.

The Precision Queue node includes a Priority field, which sets the initial queuing priority for the calls processed through this node versus other calls queued to the
                              other targets using different nodes. The priority is expressed as an integer from 1 (top priority) to 20 (least priority).
                              The default value is 5.

If more than one
                              		  call is queued to a precision queue when an agent becomes available, the queued
                              		  call with the lowest priority number is routed to the target first. For
                              		  example, assume an agent in a precision queue becomes available and two calls
                              		  are queued to that precision queue. If one call has priority 3 and the other
                              		  has priority 5, the call with priority 3, the lower value, is routed to the
                              		  precision queue while the other call continues to wait. If the priorities of
                              		  the two calls are same, then the call queued first is routed first.

VRU script
                              		  instructions are not sent to the VRU. If a call enters the Precision Queue node
                              		  and no resource is available, the call is queued to the precision queue and the
                              		  node transfers the call to the default VRU, if the call is not already on a
                              		  VRU. The script flow then exits immediately through the success branch and
                              		  continues to a Run External Script node to instruct the VRU what to do while
                              		  holding the call until an agent becomes available. Typically, this invokes a
                              		  Network VRU script that plays music-on-hold, possibly interrupted on a regular
                              		  basis with an announcement. The script flow can also use other queuing nodes to
                              		  queue the same call to other targets, for example, Queue to Skill Group and
                              		  Queue to Agent.

### Precision Queue
                           	 Properties Dialog Box - Static Precision Queue

The following list
                              		describes the Precision Queue Properties dialog box for a static precision
                              		queue script node.

The following property
                              		is unique to static precision queues:

Drop-down list —To route
                                    			 calls that enter this node to a static precision queue, you must select a
                                    			 precision queue from the list.

The following
                              		properties are common to static and dynamic precision queues:

Select Precision Queue radio
                                    				buttons—You can select one of the following options for each a precision
                                    			 queue:

Statically —Select this
                                          				  option to choose a single precision queue to be selected for all the calls that
                                          				  enter this node.

Dynamically —Select this
                                          				  option to select a precision queue on a call-by-call basis based on a formula.

The dynamic
                                                				precision queue option is enabled only for System Administrators. For other
                                                				users, this option is disabled.

Priority selection —To select the initial queuing priority for calls processed through this node, you can select from 1 to 20. The default is
                                    5.

Enable target requery check
                                       				box —To enable the requery feature for calls processed through this node,
                                    			 select this check box. When a requery occurs, for example if a call is
                                    			 presented to an available agent and the agent does not answer, the script
                                    			 continues through the failure terminal. The script can then inspect the call
                                    			 variable RequeryStatus to determine what to do next. The typical action in case
                                    			 of a No Answer is to queue the call again to other precision queues, and
                                    			 increase the priority so that it is taken out of the queue before regular
                                    			 queued calls.

Wait if Agents Not Logged In check box — When this check box is selected and the agents who are associated with a step are not logged in, then the router will wait
                                    for the time that is configured for that step. When this check box is not selected, the router will not wait on any step.
                                    However, on the last step, the router will wait indefinitely irrespective of the selection.

### Precision Queue
                           	 Properties Dialog Box - Dynamic Precision Queue

The following list
                              		describes the Precision Queue Properties dialog box for a dynamic precision
                              		queue script node.

Use dynamic precision
                              		queues when you want a single routing script for multiple precision queues (for
                              		example, when the overall call treatment does not vary from one precision queue
                              		to another). Dynamic precision queues can simplify and reduce the overall
                              		number of routing scripts in the system.

The dynamic
                                          		  precision queue option is enabled only for System Administrators. For other
                                          		  users, this option is disabled.

The following
                              		properties are unique to dynamic precision queues:

Find By radio buttons —To
                                    			 dynamically route calls that enter this node to a Precision Queue name or ID,
                                    			 use the Find By radio buttons.

Precision Queue Name
                                             					 radio —Select this option to dynamically route calls that enter this node to
                                          				  a Precision Queue name.

Precision Queue ID —Select
                                          				  this option to dynamically route calls that enter this node to a Precision
                                          				  Queue ID.

Formula Editor button —To determine to which Precision Queue name or ID to route calls that enter this node, click the Formula Editor button to
                                    create a formula. The formula is then evaluated at run time to select a precision queue by either name or by database ID.
                                    For example, you can use the formula "Call.PeripheralVariable4" to look up the Precision Queue if call variable 4 contained
                                    the Precision Queue name, as a result of a database lookup or from Unified CVP call processing.

The section on static precision queues describes the properties that are common to static and dynamic precision queues.

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

## Adjust Priority of a Call in a Queue

You can override the priority of a call in queue set by the Queue node by
                           using the Queue Priority node (in the Queue tab of the Palette).

For example:

The original priority of the call in queue is set by the Queue to
                                 Skill Group node or the Precision Queue node.

The call waits in queue for 20 seconds while the caller listens to
                                 an announcement.

Call control passes to a second Wait node.

If 20 more seconds pass without an agent becoming available, the Queue Priority node is run and raises the call's priority
                                 in queue.

Notes:

Only use the Queue Priority node after a Queue to Skill Group node or a Precision Queue 
                                 node. Any subsequent use of the Queue to Skill Group node or the Precision Queue node results in
                                 setting the queue priority back to the original setting for that node.

The Queue Priority node sets the priority for a call within all
                                 queues that the call is placed in. If a call requires the
                                 priority to be raised in one queue only, you should use a subsequent Queue to Skill Group
                                 or Precision Queue node for only that skill group/queue  (with the new priority).

Queuing priorities should be handled very carefully. Just increasing Queue priority does not get a call handled sooner. The
                                 effect depends on the other call in the queue. For example, if all calls are treated using the example above, the priority
                                 increase has no net effect. If the script above is only used for the Platinum customers while the Standard customers script
                                 leaves them at the default priority level, the effect is that all Platinum customers that have been in queue for more than
                                 20 seconds are handled first regardless of other customers in queue. As the delay for Platinum customers is greater than 20
                                 seconds, no Standard customers are handled ever. The solution is to increase the priority level for Standard customers as
                                 well, but only after they have been in queue for a longer period, for example 3 minutes.

Following is the Properties dialog box for the Queue Priority node:

## Remove Call from a Queue

You do not have to define properties for the Cancel Queuing node. You can
                              optionally add comments or connection labels.

## Temporarily Halt
                        	 Script Execution

You can halt script execution for a specified number of seconds by using the Wait node (in the Queue tab of the Palette).

The Wait node simply stops script executing for the specified number of seconds. In the meantime, the Network VRU is waiting
                              for instructions.

Warning

You must set protocol time-out variables in Unified CVP to a value greater than the longest wait node used in the script.

Following is the Properties dialog box for the Wait node:

Define Wait node properties as follows:

Step 1

In the Timeout
                                       			 in field, specify an interval to wait, in seconds.

Step 2

Optionally, add
                                       			 comments or connection labels.

| Note | If the current call is not at a Unified CVP when the Run External Script node is run, Unified CCE Packaged CCE sends the call to the associated Network VRU, as run a Send to VRU node. Design scripts so that the Failure branch of a Run External Script Node contains a test for the Call.VRUStatus variable. If
                                                the value is 2, the VRU is likely to be not functioning properly. Therefore, the script avoids executing any subsequent Run
                                                External Script nodes on this Failure branch. |
|---|---|

| Note | When an uninterruptible script is used in a Run External Script node, the CallRouter waits for the script result from the
                                       VRU. It then runs the next node. Calls can only be routed when they reach an interruptible node. The Wait node and interruptible
                                       Run External Script node ( micro apps) are interruptible. Every other node is uninterruptible. |
|---|---|

| Step 1 | Select the Unified CCE Packaged CCE Script/External Script Name you want to run. |
|---|---|
| Step 2 | Optionally, add
                                       			 comments and connection labels. |

| Value | Meaning | Description |
|---|---|---|
| 0 | VRU_SUCCESS | The last VRU node was successful. |
| 1 | VRU_ERROR | The last VRU node failed because of a routing or
                                          configuration error. |
| 2 | VRU_TIMEOUT | The last Send To VRU failed because the routing client did not respond within 20 seconds or the last Run External Script node
                                          failed because the timeout limit defined for the script expired. |
| 3 | VRU_ABORTED | The last VRU node did not complete because the caller ended the call or stopped responding. (Because this causes the routing
                                          script to terminate immediately, this value is never seen.) |
| 4 | VRU_DIALOG_ FAILED | The last VRU node failed because communication with
                                          the VRU ended unexpectedly. |
| 5 | VRU_SCRIPT_ NOT_FOUND | The VRU failed because the referenced VRU script was not found in the Unified CCE Packaged CCE configuration. |
| 6 | STATUS_MAX_QUEUE_LIMIT_EXCEEDED | The last node failed because the maximum call queuing limit was exceeded. |
| 7 | STATUS_NO_VALID_EXPRESSION | The last node failed because no valid expression was found. |
| 8 | STATUS_NO_VALID_TARGET | The last node failed because no valid target was found. |
| 10 | STATUS_NO_MRD_MATCH | The last node failed because no targets matched with the Media Routing Domain on the call. |
| 11 | STATUS_CONSIDER_IF_FAILED | The last node failed because the Consider If expression failed on all targets. |
| 12 | STATUS_NO_VALID_PERIPHERAL | The last node failed because none of the targets were configured on the supported peripheral. |
| 13 | STATUS_NO_ONLINE_PERIPHERAL | The last node failed because all targets are on peripherals that are offline. |

| Caution | Do not use the nodes like Route Select to queue the calls when the script cycles between a Wait node and a Run External Script
                                                node. |
|---|---|

| Note | In this scenario,
                                       		  you would likely make the VRU script interruptible so that the routing script
                                       		  can retrieve the call immediately when the resource becomes available. |
|---|---|

| Note | If the current call is not at a Unified CVP when the Queue node runs, Packaged CCE sends the call to the associated Network
                                          VRU. (This does not apply to Type 2 VRUs, which are VRUs at customer premises.) |
|---|---|

| Note | The Queue node does not actually result in instructions being sent to the VRU. When queuing occurs the Queue node exits immediately
                                          through the success branch and the call is assumed to be at the VRU; the script should then continue with a Run External Script
                                          node to instruct the VRU what to do while holding the call until an agent to becomes available. Typically this would invoke
                                          a Network VRU script that plays music-on-hold, possibly interrupted on a regular basis with an announcement. |
|---|---|

| Step 1 | To change the queue type: Click Change . The Queue Type dialog box opens. Select a Target Type (Skill Group). You cannot reference more than one type of target within a single Queue node. To queue a call to more than
                                             one target type, run multiple Queue nodes sequentially. Optionally, select a Priority to set the initial queuing priority for calls processed through this node versus other calls
                                             queued for the same target: 1 for top priority to 20 for least priority. (The default is 5.) Optionally, check Enable Target Requery . Note When Target Requery is enabled in a Queue node and a Requery happens, for example because the call is presented to an available
                                                            agent, but the agent does not answer, the script continues through the failure terminal. The script can then inspect the call
                                                            variable RequeryStatus to determine what to do next. The typical action in case of a No Answer would be to Queue the call
                                                            again, possibly to other skill groups, and possibly increase the priority so that it is taken out of the queue before regular
                                                            queued calls. Click OK to close the Queue Type dialog box. | Note | When Target Requery is enabled in a Queue node and a Requery happens, for example because the call is presented to an available
                                                            agent, but the agent does not answer, the script continues through the failure terminal. The script can then inspect the call
                                                            variable RequeryStatus to determine what to do next. The typical action in case of a No Answer would be to Queue the call
                                                            again, possibly to other skill groups, and possibly increase the priority so that it is taken out of the queue before regular
                                                            queued calls. |
|---|---|---|---|
| Note | When Target Requery is enabled in a Queue node and a Requery happens, for example because the call is presented to an available
                                                            agent, but the agent does not answer, the script continues through the failure terminal. The script can then inspect the call
                                                            variable RequeryStatus to determine what to do next. The typical action in case of a No Answer would be to Queue the call
                                                            again, possibly to other skill groups, and possibly increase the priority so that it is taken out of the queue before regular
                                                            queued calls. |
| Step 2 | To add targets: Click Add Targets . The Add Targets dialog box opens, listing available targets of the type you specified. Use the Available Targets list and the Add button to select targets. Click OK to close the Add Targets dialog box. The target members you selected appear in the Properties dialog box. |
| Step 3 | Optionally, continue defining Target Type information for the Route (Drop-down list) member. This is the route to send the call to when an agent in the target type becomes available.
                                          (The drop-down list includes all routes associated with the target.) |
| Step 4 | Optionally, add connection labels. |

| Note | When Target Requery is enabled in a Queue node and a Requery happens, for example because the call is presented to an available
                                                            agent, but the agent does not answer, the script continues through the failure terminal. The script can then inspect the call
                                                            variable RequeryStatus to determine what to do next. The typical action in case of a No Answer would be to Queue the call
                                                            again, possibly to other skill groups, and possibly increase the priority so that it is taken out of the queue before regular
                                                            queued calls. |
|---|---|

| Note | When processing a Queue node, the router first checks for an available target, if there is none available then the router
                                          attempts to queue the call. The call does not move to the VRU if there is an available agent. |
|---|---|

| Note | The dynamic
                                                				precision queue option is enabled only for System Administrators. For other
                                                				users, this option is disabled. |
|---|---|

| Note | The dynamic
                                          		  precision queue option is enabled only for System Administrators. For other
                                          		  users, this option is disabled. |
|---|---|

| Note | The section on static precision queues describes the properties that are common to static and dynamic precision queues. |
|---|---|

| Warning | You must set protocol time-out variables in Unified CVP to a value greater than the longest wait node used in the script. |
|---|---|

| Step 1 | In the Timeout
                                       			 in field, specify an interval to wait, in seconds. |
|---|---|
| Step 2 | Optionally, add
                                       			 comments or connection labels. |