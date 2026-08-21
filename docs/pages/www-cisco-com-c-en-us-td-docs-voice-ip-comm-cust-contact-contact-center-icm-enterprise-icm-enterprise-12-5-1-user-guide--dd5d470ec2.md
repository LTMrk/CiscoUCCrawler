---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--dd5d470ec2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_scripting-and-media-routing-guide_12_5/ucce_b_scripting-and-media-routing-guide_12_5_chapter_01110.html
retrieved_at: 2026-08-21T12:04:06.064678+00:00
---

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

# Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

Updated: May 26, 2022

Chapter: Hosted Script Considerations

## Chapter: Hosted Script Considerations

# Hosted Script Considerations

## NAM Script Configuration

This section covers scripting considerations to use in an IP Contact Center
                              Hosted-Edition system. For more information about scripting in a Unified ICM/Unified NAM
                              environment, see the Setup and Configuration Guide for Cisco Unified ICM .

Scripting on the NAM requires only one Dialed Number script per Customer
                              Instance. However, your design may include more.

The NAM routing script sends the Dialed Number to the correct Unified CVP
                              Media Server for treatment, then ultimately to the Unified ICM Gateway of the
                              CICM instance for the particular Dialed Number.

The first script node after the Start should be a "set
                                 variable" node that contains the following:

Object Type — Call

Object — (no selection)

Variable — NetworkTransferEnabled

Value — 1

After you set the variable for NetworkTransferEnabled you can create
                              a Dialed Number (DN) node to route to a particular CICM Instance Routing
                              Client.

If the Dialed Number node is true, then you typically send the call to
                              the Unified CVP Media Server using another Set Variable node as described
                              below.

The first script node after the star should be a "set
                                 variable" node that contains the following:

Object Type — Call

Object — (no selection)

Variable — user.microapp.media_server

Value — the IP address of the Unified CVP Media Server, enclosed in
                                    quotes, for example "192.168.10.11"

At this point, scripting is conducted on the Unified CVP. For more information about scripting in the Unified CVP, see the Configuration Guide for
                                       				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Next, the call is sent to the Unified ICM gateway of a particular customer
                              instance.

If you use multiple DNs, then you can send the call to a different
                              Unified CVP Media Server based on the different DN.

Finally, the call is sent to the Unified ICM gateway of a particular customer
                              instance. Add a Unified ICM Gateway node and select the customer to which to
                              route the call.

## Customer Intelligent Contact Management (CICM) Script Considerations

### Create CICM VRU Scripts

VRU scripts differ from Unified ICM routing scripts. A configured
                                 VRU script runs only when the Unified ICM instructs it to do so from a
                                 Unified ICM routing script. A VRU script on the Unified ICM is the
                                 configured record for the VRU Script that resides on Unified CVP. A
                                 VRU script executes to collect digits, play hold music, or perform
                                 many other common VRU functions.

Step 1

From the Unified ICM Configuration Manager,
                                          choose Targets > Network VRU Script > Network VRU
                                             Script List .

The Network VRU Script List dialog box appears.

Step 2

On the Attributes tab, enter the following
                                             configuration information for the BasicQ
                                             script:

- Network VRU Enter isnvru.

- VRU Script Name Enter script name (for example, BasicQ).

- NameEnter the script file name (for example,
                                                BasicQ.aef).

- Timeout (seconds)Enter 180.

- Configuration paramLeave blank.

- CustomerSelect the same Unified ICM customer you selected
                                                for Call Type from the drop-down list.

Step 3

Select the Interruptible check box.

Step 4

Click Save and then click Close .

### CICM VRU Script Considerations

Use the Script Editor SendToVRU node to connect the call to the
                                 Network VRU.

For more information about creating scripts, see Configuration Guide for
                                          				  Cisco Unified Customer Voice Portal .

### RONA and Unified
                           	 CVP

When using the Unified CCE with the Unified CVP, the Unified ICM Router Requery function is used to take the call away from
                                 the non-answering agent and requeue it for service.

The following scenario explains the various conditions after Unified CVP RNA expires.

Agent state set is READY after CVP RNA expires when:

In Agent Desk Settings, the Ring no answer dialed number field is set to blank.

You entered a value in the Ring No Answer time field. This value must be at least 2 seconds more than timeout configured at Unified CVP for RNA Timeout.

Agent state set is NOT_READY after CVP RNA  expires when:

In Agent Desk Settings, the Ring no answer dialed number field is set to blank.

You do not enter a value in the Ring No Answer time field.

In the example script Scripting for RONA:

The Queue node for the skill group that selects the first agent must have Target Requery enabled.

Raise the priority of the call so that it moves to the front of the queue.

### Scripts for
                           	 RONA

When scripting for
                                 		  RONA, you should Enable Requery on the node in the script that selects the
                                 		  first agent. Depending on the type of node used, the Requery mechanism selects
                                 		  a new target from the available agents or requires additional scripting.

If there is an
                                 		  available agent, the Queue node selects the longest available agent from the
                                 		  configured skill groups. If there is no available agent, the script then queues
                                 		  the call with a priority set in the node and continues down the success exit of
                                 		  the node.

When an agent
                                 		  becomes available, the Unified ICM always selects the longest queued call from
                                 		  the ones with the highest priority. The RONA mechanism works as follows:

The Queue node
                                       				selects an agent.

If the agent
                                       				does not answer the call, then the script exits through the failure terminal of
                                       				the Queue node.

The If node
                                       				tests the RequeryStatus variable. If it has value of greater than zero, this is
                                       				a requery call and the script re-queues the call.

In the Scripting
                                       				for RONA example above, it also sets a flag using a call variable for reporting
                                       				purposes.

Assuming that
                                       				there are no agents available, the Queue node immediately exits through the
                                       				success terminal.

- If this is a required call,
                                    			 It increases the Queue Priority of the call so that it is handled before any
                                    			 other calls in queue.

It then enters
                                       				the normal wait loop with RunScripts.

| Note | Do NOT select the Validate returned labels check box. If you do, you
                                       must provision the NAM with all of the labels that exist on every
                                       customer instance. |
|---|---|

| Note | For more information about general scripting requirements for a Unified ICM Instance, see Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|

| Note | For more information about the Unified CVP additional scripting considerations, see Configuration Guide for
                                                				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
|---|---|

| Step 1 | From the Unified ICM Configuration Manager,
                                          choose Targets > Network VRU Script > Network VRU
                                             Script List . The Network VRU Script List dialog box appears. |
|---|---|
| Step 2 | On the Attributes tab, enter the following
                                             configuration information for the BasicQ
                                             script: Network VRU Enter isnvru. VRU Script Name Enter script name (for example, BasicQ). NameEnter the script file name (for example,
                                                BasicQ.aef). Timeout (seconds)Enter 180. Configuration paramLeave blank. CustomerSelect the same Unified ICM customer you selected
                                                for Call Type from the drop-down list. |
| Step 3 | Select the Interruptible check box. |
| Step 4 | Click Save and then click Close . |

| Note | A RunVRU Script or Queue node is an "implicit" SendToVRU node,
                                          although error handling is easier if you use the explicit "SendToVRU" node. |
|---|---|