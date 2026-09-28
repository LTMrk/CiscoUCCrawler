---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-guide--3db915214e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/guide/ucce_b_scripting-and-media-routing-guide_1262/ucce_b_scripting-and-media-routing-guide_chapter_01101.html
retrieved_at: 2026-08-16T20:32:23.474045+00:00
---

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

# Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

Updated: November 21, 2022

Chapter: Example Scripts

## Chapter: Example Scripts

# Example Scripts

## Example Collaboration Scripts

You can configure the Unified ICM and Enterprise Chat and
                                    						Email so that
                              the Unified ICM routes Web Collaboration requests that are processed by Enterprise Chat and
                                    						Email .

### Overview of ECE Web Request Routing Through Unified ICM

With the ECE integrated with the Unified ICM, the Unified ICM can route chat requests.

The process for routing Web requests through the Unified ICM can be
                                 divided into 5 parts, as shown in the following image:

### Web Requests and Media Routing Domains

Enterprise Chat and
                                       						Email can take advantage of the following
                                 types of Media Routing Domains (MRDs):

Non-voice MRDs

Voice MRD

For more information about MRDs, see the Administration Guide for Cisco Unified Contact Center Enterprise .

### Non-Voice MRDs

The Enterprise Chat and
                                       						Email uses Non-voice MRDs for chat requests.

### The Voice MRD

The Voice MRD handles these types of requests:

Blended chat with legacy ACDs (these are requests for chat,
                                       but with agent reservation on the ACD)

Web callback and delayed callback with both ACDs and Unified
                                       CCE

### Script That Queues a Web Request to a Skill Group

The following script example shows how a Web request can be queued to
                                 		  a skill group:

In this example:

This script is scheduled to run for web chat requests. For more
                                       				information about call types and scheduling Web requests routing scripts, see Example - How Unified ICM
                                          				  Determines the Call Type for Web Request .

The script queues the request to a chat skill group. At this time,
                                       				Unified ICM attempts to find an available agent who is a member of that skill
                                       				group. When the agent is found, the system software returns the agent ID to the
                                       				Cisco Interaction Manager.

The script is run and the Enterprise Chat and
                                             						Email processes a new chat request. This script is scheduled to run for chat requests.

The script queues the request to a chat skill group. At this time,
                                       				the Unified ICM attempts to find an available agent who is a member of that skill
                                       				group. When the agent is found, the Unified ICM returns the agent ID to the Enterprise Chat and
                                             						Email .

### Script That Pushes a URL to a Waiting Caller

The following script example shows how a script can push a URL to a
                                 waiting caller before the Web request is queued to a skill group:

In this example, the Run External Script node pushes the selected URL
                                 to the caller's browser.

### Script That Queues Directly to an Agent

The following script example shows how you can queue a Web request directly to an agent:

In this example:

You can schedule this script to run for a particular type of
                                       request.

The script attempts to queue the request directly to an agent
                                       using the Queue to Agent node. The Queue to Agent node uses a
                                       direct reference to the agent, as shown in its Properties dialog
                                       box:

The script tries to do this for 600 seconds before ending, as
                                       defined in the Wait node.

### Script That Routes Based on the Media Routing Domain

The following script example shows how you can queue Web requests from different
                                 MRDs to different skill groups:

In this example:

The script is run to process a chat request. This script is scheduled to run for all these types of requests.

The script first detects the MRD of the request using the
                                       Media Routing Domain node. This node has two branches for the
                                       MRDs of the request: the email MRD (branch A) or
                                       chat MRD (branch B).

The script queues the request to the appropriate skill group
                                       for that type of request. At this time, the Unified ICM attempts to
                                       find an available agent who is a member of that skill group.
                                       When the agent is found, the system software returns the agent
                                       ID to the Cisco Interaction Manager.

## Modify CCE Scripts for Experience Management Voice, SMS, and Email Surveys

In Script Editor, modify your CCE call routing scripts for incoming calls as follows:

Add nodes to invoke the call studio survey script, if needed. The following example explains when you might need to explicitly
                           add nodes to call the survey script.

A script is called that asks callers if they want to participate in a survey. The script then sets the user.microapp.isPostCallSurvey variable according to the caller's response.

You can use POD.ID to send cc_CustomerID , and this cc_CustomerID can be used to filter the data in finesse gadget.

POD.ID is an optional field in Experience Management voice survey and the supported POD. ID format will be xxx, where xxx is the Customer_id.

### Create Experience Management Routing Script for Voice

Create the following routing script for the Experience Management Call Type to play your survey script or application to the caller.

Step 1

In Script Editor, create the routing script as shown in the example.

Step 2

Do the following to ensure the routing script is mapped to the call type you created for Experience Management .

Navigate to Script > Call Type Manager .

On the Schedules tab, from the Call Type drop-down list, select the call type that you created for Experience Management .

For more information refer to the topic Call Type and Survey Association in Unified CCE Admin in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Click Add .

Click OK .

For more information on optimizing the threshold values for SMS and Email batch processing, refer to the topic Configure SMS/Email Thresholds in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html

### Create Experience Management Routing Script for SMS and Email

Experience Management Deferred (SMS/Email) survey is used for getting feedback on the overall customer journey experience.
                              For invoking this survey, the caller's mobile number, email address, and other details have to be collected from Call Studio
                              and passed to ICM. To configure this, refer to the following sections:

#### Configure Call Studio App Data Format

Create Call Studio application with the use of CVP SubDialogReurn element and fill the customer data as external VXML variables.

Example: External VXML 0 = Email=abcd@cisco.com;cc_CustomerId=xyz;cc_language=en-US;Optin=yes;Mobile=911234567890;

Each key-value pair is separated by a semi colon.

The variable names are case sensitive.

Refer to the following table for the variables and their descriptions.

Variable Name

Description

cc_CustomerId

Unique ID for a customer across multiple channels.

Required

Email

Customer email ID

Either email or phone number is required

Mobile

Customer mobile number with country code.

Example: 919911223344

Either email or phone number is required

cc_language

Survey language

Example: en-US

Optional

Optin

Option to check if customer wants to opt for the survey:

Values: yes/no

Default value is yes when the value is not captured from Call Studio.

Optional

#### Configure ICM Script

Step 1

Create the ICM script as shown in the following screen shot:

Step 2

Fill the ECC variable POD.ID values from user.microapp.FromExtVXML array and pass it to ICM.

Example: POD.ID=cc_CustomerId=xyz;Email=abcd@cisco.com;cc_language=en-US;Optin=yes;Mobile=911234567890;

Step 3

Save the script.

## Example Enterprise Chat and
                              						Email - Email Scripts

You can configure the Unified ICM and the Enterprise Chat and
                                    						Email so that the system software routes email messages that are processed by Enterprise Chat and
                                    						Email .

For more information about configuring Unified ICM and Enterprise Chat and
                                    						Email in an integrated environment, see the following documents:

Configuration Guide for Cisco Unified ICM/Contact Center Enterprise

Cisco Unified Web and E-Mail Interaction Manager Installation Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-email-interaction-manager/products-installation-guides-list.html

Cisco ICM Multichannel Software Implementation Map

Cisco ICM Multichannel Software Overview

### Overview of ECE E-mail Routing Through Unified ICM

When the ECE is in an integrated environment, the administrator can choose to defer message assignment to Unified ICM. The administrator
                                 determines if skill groups can initiate message routing through the system software when the skill groups are created. The
                                 administrator then defines rules to assign messages to those Unified ICM Routing skill groups.

In this situation:

A message enters the ECE .

A rule assigns the message to a Unified ICM Routing skill
                                       group.

ECE sends a request for assignment to Unified ICM.

The Router runs a routing script to determine which ECE agent to assign the message to. The routing script can also determine that the message should be assigned to a local ECE routing skill group.

Based on the routing script's determination, the Unified ICM instructs the ECE to assign the message to a particular agent or ECE routing skill group.

The message is placed in the agent's or skill group's queue.

If the message is assigned to an agent by the Unified ICM, it is presented to the agent in push mode; if the message is assigned
                                       to an ECE routing skill group, it is placed in that skill group's queue.

### Script That Queues E-mail to a Skill Group

The following script example shows how an e-mail message can be queued
                                 to a skill group:

In this example:

The script is run when a e-mail message is assigned to a Unified ICM Routing skill group. This script is scheduled to run
                                       for messages assigned to that skill group. For more information about call types and scheduling e-mail routing scripts, see Example - How Unified ICM Determines the Call Type for an E-Mail contact .

The script queues the request to the skill group. At this
                                       time, the Unified ICM attempts to find an available agent who is a
                                       member of that skill group. When the agent is found, the system
                                       software instructs the Enterprise Chat and
                                             						Email to push the e-mail message to that
                                       agent, so the agent can respond to the customer.

If no agent is found within 30 seconds, as defined in the Wait
                                       node, the script uses the Label node to return a label
                                       associated with the Enterprise Chat and
                                             						Email local skill group.
                                       The Enterprise Chat and
                                             						Email then places the message in that
                                       local skill group. Enterprise Chat and
                                             						Email load balances the e-mail
                                       assignments to the available agent, based on load
                                       balancing.

### Script That Routes a Message Based on the Priority

The following script example shows how you can queue an e-mail message directly to an agent or to a skill group, depending
                                 on the message's priority:

In this example:

The script is run when a e-mail message is assigned by the Enterprise Chat and
                                             						Email to a Unified ICM Routing skill group. This script is scheduled to run for messages in that skill group. For more information
                                       on call types and scheduling e-mail routing scripts, see Example - How Unified ICM Determines the Call Type for an E-Mail Contact .

The script tests the message's priority, the value of the cisco.ece.Priority variable. For more information, see Data for E-Mail Requests .

If the message is marked "Urgent" (cisco.ece.Priority value of 3), control passes to the Queue to Agent node. That node lists
                                       two agents who are e-mail supervisors and who handle urgent messages. The Enterprise Chat and
                                             						Email then pushes the message to the first of these agents who is logged in.

If the message is not urgent, control passes to the Queue to Skill Group node. The Unified ICM attempts to find an available
                                       agent who is a member of that skill group. When the agent is found, the Unified ICM instructs the Enterprise Chat and
                                             						Email to push the e-mail message to that agent.

If no agent is found within 30 seconds, in either the Queue to Agent node or Queue to Skill Group node, as defined in the
                                       Wait node, the script uses the Label node to return a label associated with a Enterprise Chat and
                                             						Email local skill group. The Enterprise Chat and
                                             						Email then places the message in that local skill group. The message is not pushed to an agent; rather, it waits in the local skill
                                       group queue for an agent to pick it.

These Expanded Call Context (ECC) variables are optional. Before you use these ECC variables, configure them in Unified CCE
                                             and ECE.

To configure these ECC variables in Configuration Manager's Expanded Call Variable List Tool, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

To configure these ECC variables in ECE, see at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

### Script That Routes Requests Based on Pick/Pull/Push

The following script example shows how you can use a single script to route a push request or a pick or pull request using
                                 an IF node:

In this example:

The script is run when the Enterprise Chat and Email assigns an email message to a Unified ICM Routing Skill Group.

The script checks whether the service requested is one of the Pick or Pull service type using the builtin function – isPickPullRequest().
                                       The success branch of IF node connects to Pick/Pull node and the failure branch connects to a queue node, which can be either a Queue to Skill Group
                                       node or Precision Queue node.

If the IF node evaluates to False, control passes to path of Push routing. The script queues the request to the skill group. At this
                                       time, the Unified ICM attempts to find an available agent who is a member of that skill group. When an agent is found, the
                                       system software instructs the Enterprise Chat and Email to push the e-mail message to that agent, so the agent can respond
                                       to the customer.

If no agent found within 30 seconds, as defined in the Wait node, the script uses the Label node to return a label associated with the Enterprise Chat and Email local skill group. The
                                       Enterprise Chat and Email then places the message in that local skill group. Enterprise Chat and Email load balances the e-mail
                                       assignments to the available agent, based on load balancing.

If the IF node evaluates to True, control passes to Pick / Pull routing. Based on the pick or pull service requested, the request will
                                       be handled in the Pick/Pull node.

Pick / Pull node can be used directly without an IF node which is shown in the example. In such case, the failure path can be used for Push routing. In addition, the reason for
                                       the failure through the Pick / Pull node is captured in the VRUStatus variable which can be set in one of the peripheral variables
                                       to be captured in the Route Call Detail record.

## Example Digital Channel Interactions Using Webex Connect

You can configure Contact Center Enterprise (CCE) and Webex Connect so that the system software routes the digital channel
                              tasks that are processed by Webex Connect.

For more information about configuring CCE and Webex Connect in an integrated environment, see the Digital Channels Integration Using Webex Connect chapter in the following documents:

Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/series.html#%7Etab-documents

### Overview of Digital Channel Routing using Webex Connect

In an integrated environment where Webex Connect is used to route digital channel contacts through the Digital Routing service,
                              an administrator can set up a routing script that can either assign tasks directly to specific agent or to Skill Groups /
                              Precision Queues across different media channels or media routing domains.

In this scenario:

A digital channel task enters Webex Connect and is routed to Unified CCE through Digital Routing service.

The Webex Connect platform uses channel-specific flows to pass task context to the Digital Routing service through call variables
                                    and ECC variables. Optionally, a Flow designer can set the Preferred Owner field in the CCE Create Task node in Webex Connect with the Agent Skill Target ID or Peripheral Number of an agent, who should be queued or routed to,
                                    if available. The value passed in the flow is populated as the call variable, Call.PreferredAgentID, which can then be used
                                    to queue the task using a QueueToAgent node in the routing script.

The Digital Routing service sends a request for assignment to Unified CCE.

The Router runs a routing script to determine which non-voice or digital channel agent to assign the task to. The routing
                                    script can also determine that the task should be assigned to a Digital Routing skill group or precision queue.

Based on the routing script's determination, the Unified CCE instructs the Digital Routing service to assign the task to a
                                    particular agent.

If the desired agent is not available, or all agents are busy in the Skill Group or Precision Queue, the task gets queued
                                    in the CCE Router. An administrator can choose to send an estimated wait time and additional task context that are carried
                                    by ECC variables through "Run External Script" node. The Digital Routing service sends the "QUEUED" webhook notification event,
                                    which invokes a "QUEUED" flow in Webex Connect to relay the estimated wait time and additional context to the customer who
                                    is active on a live chat session or on asynchronous social channels such as SMS.

### Script that Queues a Digital Channel Task to a Skill Group

The following script example shows how a digital channel task can be queued to a skill group. In this example there are two
                              scenarios:

Scenario 1

The task is queued and routed to an agent based on the wait time defined.

The routing script decides the skill group from where an agent must be picked. The same script can be used to route tasks
                                    belonging to different media channels such as Email, Chat, SMS or Web Callback (which maps to Cisco_Voice MRD) and unique
                                    Script Selectors / Dialed Numbers. In this example, the script queues the task to "Sales" or "Insurance" skill groups corresponding
                                    to Chat and Email MRDs based on the Script Selectors / Dialed Numbers received in the route request from Webex Connect. For
                                    more information about how Unified CCE determines the Call Type for a task routed through digital channels, see Determination of Call Type for a Digital Routing Task .

The script queues the task request to the skill group. At this time, Unified ICM attempts to find an available agent who is a member of that skill group. Unified ICM runs an external script to notify the customer an estimated wait time. When the agent is found, the system software instructs
                                    the Digital Routing API service to push the task to that agent, so the agent can respond to the customer.

In the example script, a loop is run to send periodic updates to the Digital Routing service about the Estimated Wait Time
                                    (EWT). An EWT is simulated by assigning it a 5 minutes (300 seconds) static value and decrementing the count in a loop, however,
                                    a custom formula can be used to relay the same based on your requirements. If the task is queued for more than 6 hours, the
                                    script bails out and ends the queueing.

The CCE wait node can be used to keep the task in the queue when the agent is not available (for example, during a weekend)
                              by setting the wait node to a high value such as 172800 seconds (48 hours). The maximum time that an activity can remain in
                              the ICM queue is determined by the MRD setting "Max time in queue". By default, this setting is blank for all MRDs and the
                              setting defined in the router registry is used. The default value in the router registry is 3600 seconds.

Scenario 2

The router rejects the queuing request as there are no queue slots available.

When queueing the task to the skill group, the router checks the following:

The global limit of maximum queued calls and maximum queued calls per call type as defined in the router registry under the
                                          following registry hive: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\InstanceName\RouterA\Router\CurrentVersion\Configuration\Queuing

The "MaxCalls" denotes the maximum queued calls, which is set as 15,000 calls or tasks and the "MaxCallsPerCallType" denotes
                                          the maximum queued calls per call type, which is set as 10,000.

Whether the number of tasks queued in the skill group has exceeded the maximum number of tasks defined in the MRD for the
                                          skill group.

If it has exceeded the maximum number of tasks defined, then the script checks the VRUStatus call variable in the failure
                                    path of the Queue node.

If the value of the VRUStatus call variable is 6, that is STATUS_MAX_QUEUE_LIMIT_EXCEEDED, the script sends the call to the
                                    release node.

The router populates a special CauseCode as part of the Release node processing that instructs the Digital Routing service
                                    to queue the task at the head of the queue, such that the task routing does not fail. The Digital Routing service tries to
                                    queue the task again in a periodic manner, as queue slots become available.

## Example Universal Queue Scripts

You can design scripts to route contacts from different media in a
                              Universal Queue environment.

These scripts are only examples; your company's needs may differ.

For more information about configuring Task Routing with third-party multichannel applications see the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

For more information about configuring Enterprise Chat and
                                    						Email , see the following documents, at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html :

Configuration Guide for Cisco Unified ICM/Contact Center Enterprise

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide

Administration Guide for Cisco Unified Contact Center Enterprise

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

Note that a Run External Script node is required to send the EstimatedWaitTime to Customer Collaboration Platform .

## Example Unified CCE Scripts

Following are example scripts for use when the Unified ICM is part
                              of a Unified CCE environment.

Redirection on Ring No Answer

Agent Transfer

These scripts are only examples; your company's needs may differ.

For more information about configuring Unified ICM as part of
                              a Unified CCE environment, see the following documents:

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide

Administration Guide for Cisco Unified Contact Center Enterprise

### Redirection on Ring No Answer

When configuring the Unified ICM in a Unified CCE environment, you
                                 configure Agent Desk Settings. When creating agents, you then associate
                                 each agent with one of the Agent Desk Settings you created.

One attribute of Agent Desk Settings is the Ring no answer
                                    dialed number:

For calls to be routed when an agent does not answer, you
                                 must create and schedule a script for the Call Type mapped to the Dialed
                                 Number selected for the agent's Desktop Settings.

For example, you may schedule a simple script to run when agents do
                                 not answer that tries to select the longest available agent from a set
                                 of skill groups, and if that fails, requalifies the call to a new Call
                                 Type to have it rerouted:

### Agent Transfer

When configuring Call Types and dialed numbers in a Unified CCE
                                 environment, you typically may have a Dialed Number of Routing_client .9999 for internal calls from
                                 agent to agent. You would create a call type associated with the Dialed
                                 Number, and schedule a script for calls of this call type. The script
                                 routes internal calls, which also allows you to track and report on such
                                 calls.

For example, you may schedule a simple script to run for internal
                                 calls that tries to route directly to the agent using the Agent to Agent
                                 node, which selects the agent by peripheral and the expression
                                 Call.CallerEnteredDigits:

If the node fails, then the script tries to select the longest
                                 available agent from the set of supervisor skill groups:

## Additional Example Outbound Option Scripts

Following are example scripts for use when the Unified ICM is part
                              of an Outbound environment:

Setting the OutboundControl Variable and Skill Group Reservation
                                    Percentage

Using the Dialed Number for the MR Routing Client and Routing
                                    through a Select Node to a Skill Group

Transfer to IVR Using Outbound Option with Unified IP IVR

Transfer to IVR Using Outbound Option with Unified CVP

These scripts are only examples, your needs may differ.

### Control of OutboundControl Variable and Skill Group Reservation Percentage

You can use an administrative script to control the setting the
                                 OutboundControl variable and the skill group reservation percentage.
                                 The Outbound Option Dialer uses these values to determine which
                                 mode each skill group uses. You can use one script to control all
                                 Outbound Option skill groups, or multiple scripts can control multiple
                                 Outbound Option skill groups.

This administrative script comprises of Start, Set, If , and End
                                 nodes. Use the Set node to set skill group variables (OutboundControl
                                 and OutboundPercent).

Set the OutboundControl variable by entering it in the
                                 Value field of the Set Properties window:

INBOUND: Indicates that this skill group is disabled for
                                       outbound use and only takes inbound calls.

PREDICTIVE_ONLY: Dials several customers per agent. After
                                       reaching a live contact, the Predictive Dialer transfers the
                                       customer to a live agent along with a screen pop to the agent’s
                                       desk. The predictive algorithm is designed to calculate the
                                       number of lines to dial per available agent to keep agent wait
                                       time to a minimum.

PREDICTIVE_BLENDED: Agents receive inbound calls, but could be
                                       used for an outbound call when available.

PREVIEW_ONLY: Reserves an agent prior to initiating an
                                       outbound call and presents the agent with a screen pop. The
                                       agent might then:

Accept the call:

Dials the customer and transfers the call to the
                                             agent.

Skip the call:

Agent receives another customer call.

Skip-Close the call:

Skips the current preview call and closes the record
                                             so it will not be called again.

Reject the call:

Releases the agent. At this point, the system might
                                             deliver the agent another preview outbound call or a new
                                             inbound call.

Reject-Close the call:

Rejects the current preview call and closes the record
                                             so it will not be called again.

PREVIEW_BLENDED: Agents receive inbound calls, but could be
                                       used for an outbound preview call when available.

PREVIEW_DIRECT_ONLY: Agents can only place outbound calls and
                                       hear ring tones, such as phone ringing or busy signal.

PREVIEW_DIRECT_BLENDED: Agents can receive inbound calls,
                                       place outbound calls, and hear ring tones, such as phone ringing
                                       or busy signal.

PROGRESSIVE_ONLY: Similar to PREDICTIVE_ONLY; however, lines
                                       to dial per agent are not calculated—users configure a fixed
                                       number of lines that will always be dialed per available
                                       agent.

PROGRESSIVE_BLENDED: Similar to PREDICTIVE_BLENDED, but a
                                       fixed number of lines will always be dialed per available
                                       agent.

Make sure that the
                                                   skill group being controlled is the base skill group, and not the
                                                   primary or secondary skill groups. Although agents may be logged in to
                                                   just the primary or secondary skill group, the outbound control variable
                                                   must always be set on the base skill group

Verify that the outbound
                                                   control variable mode is spelled correctly.

Set the OutboundPercent variable in the same administrative script.
                                 Select the OutboundPercent variable in the Set Properties window and
                                 enter the agent percentage in the Value field. This variable controls
                                 the percentage of agents that are logged in to a particular skill
                                 group, which should be used for outbound dialing. For example, if there
                                 are 100 agents logged into skill group N, and the OutboundPercent
                                 variable is set to 50%, 50 agents would be allocated for outbound
                                 dialing.

The following diagram displays a very simple administrative script
                                 where both the OutboundControl variable and the outbound percentage are
                                 set for a skill group. A script in a production call center would
                                 typically be more complex, perhaps changing these variables due to time
                                 of day or service level.

### Use Dialed Number for MR Routing Client

The following diagram displays a sample routing script that uses the Dialed Number for the MR routing client and routes through
                                 a Select node to a previously configured skill group. Add additional DN nodes to route to agents in additional skill groups
                                 as you must maintain a 1:1 ratio of dialed numbers to skill groups.

Warning

You must set the outbound percentage in the Set node to a value other than zero (0) or it appears to the node that there are
                                             no agents assigned to the Outbound Option and no outbound calls will be made.

Warning

Do not use Select Route nodes, multiple skill groups, or services.

Translation routes are not used in the Unified CCE System PG, so routing scripts using this PG do not need to use this object.

Configuring Queue to Agent Node

Step 1

Right-click the Queue to Agent node and select Properties .

Step 2

Click Change in the "Queue to agent type" section.

Step 3

Click Lookup agent reference by expression ,
                                          then click OK .

Step 4

Enter the agent expression Call.PreferredAgentID.

Step 5

Make sure the Peripheral column is left blank.

Step 6

Select the enterprise skill group.

Step 7

Select the enterprise route.

Step 8

Click OK to save the Queue to Agent
                                          node.

#### What to do next

Lines connecting objects cannot appear on top of objects and therefore, partially display under the objects. For example,
                                             the line connecting the "X" (output terminal failure) on the Select object to the End object runs partially under the Select object.

### Transfer to VRU Using Outbound Option with Unified IP IVR

The following diagram displays a routing script for a transfer to VRU
                                 campaign using the Outbound Option with the Unified IP IVR.

### Transfer to VRU Using Outbound Option with Unified CVP

The following diagram displays a routing script for a transfer to VRU
                                 campaign using the Outbound Option with the Unified CVP.

## Estimated Wait Time (EWT) Queues

The Script Editor's built-in Minimum Expected Delay (MED) calculation does
                              not apply to the Unified CCE. Instead, you can use the built-in function, EstimatedWaitTime, or write a formula on an IF node
                              to
                              determine the MED between two skill groups.

The default EstimatedWaitTime algorithm is based on a running five minute
                              window of the rate of calls leaving the queue. Any calls which are
                              routed or abandoned during the previous 5 minutes are taken into
                              account as part of the rate leaving queue. For Precision Queues,
                              the rate leaving queue represents the rate at which calls are
                              delivered or abandoned from the entire precision queue, not any
                              individual Precision Queue steps.
                              The algorithm computes the wait time for each of the
                              queues against which  the call is queued (Skill
                              Group(s) or Precision Queue(s)) and then returns
                              the minimum estimated wait time. Queue to Agent(s) is not supported. The estimated wait time is calculated once, when the
                              call enters the queue. The time is not updated as the position in the queue changes.

When a queue is just being built, the small number of calls in the queue makes the estimated wait time  less accurate and
                              the value   fluctuates rapidly.
                              As the queue operates with more calls over time, the estimated wait time is more accurate and consistent.

The current estimated wait time is determined using a rolling five-minute window and may be 0 or -1 based on the following
                                          conditions:

A value of 0 indicates that there are no calls queued in the skill group or precision queue.

A value of -1 indicates that there is not enough call data within the last five-minute window to calculate the estimated wait
                                                time (EWT).

If the built-in  EstimatedWaitTime function does not meet your needs, you can apply your own custom formula.

### When to Use EWT Queues

Look for a  secondary skillgroup choice in the following situations:

No available agents in the primary or first choice skill
                                       group

The call has already been sent to a VRU queue point

The call has been queued to the primary or first choice skill
                                       group

An adequate amount of time has elapsed (customer and call
                                       dependent)

After the above conditions have been met, if there are no agents
                                 available in the subsequent or secondary choice skillgroup, then Minimum
                                 Expected Delay (MED) of the subsequent skillgroup should be calculated.

### Example EWT/MED Script Formula

You can use the example formula below in an IF node to determine the
                                 EWT/MED for a call that you  can route to either a primary or secondary
                                 skill group. The call is routed to the skill group with the lowest
                                 MED:

EntSkill.Default\EnterpriseSkillgroupSec.Avail ||

(EntSkill.Default\EnterpriseSkillgroupPri.LoggedOn>0)

&&

(EntSkill.Default\EnterpriseSkillgroupSec.LoggedOn>0)

&&

((SkillGroup.CCM_PG_1.CCM_SG.sec.RouterCallsQNow+1)*

(ValidValue(EntSkill.Default\EnterpriseSkillgroupSec.AvgHandledCallsTimeTo5,<constant>))

/EntSkill.Default\EnterpriseSkillgroupSec.LoggedOn)

<

((SkillGroup.CCM_PG_1.CCM_SG.pri.RouterCallsQNow+1)*

(ValidValue(EntSkill.Default\EnterpriseSkillgroupPri.AvgHandledCallsTimeTo5,<constant>))

/EntSkill.Default\EnterpriseSkillgroupPri.LoggedOn)

### EWT/MED Script Explained

If there are agents available, then no there is no need to calculate
                                 the MED and the IF node should return a  TRUE value. If there are no agents
                                 available, then the MED of the secondary skillgroup should be
                                 calculated.

The formula first checks to make sure agents are logged in to both the
                                 primary (already queued to) and secondary (not queued to) skill groups.
                                 If there are agents logged in to both skill groups, then the minimum
                                 expected delay of the secondary skillgroup is compared to the minimum
                                 expected delay of the primary skillgroup to see which is less.

If the secondary skillgroup MED is less, then the call should be
                                 queued at the new secondary skillgroup. (The call can either be kept in
                                 the initial skillgroup or taken out of the initial skillgroup when it is
                                 queued to the secondary skillgroup.)

However, if the secondary skillgroup's MED is not less than the
                                 primary skillgroup's MED, then the call should remain queued at the
                                 initial skillgroup only. +1 is used to add this new call into the
                                 algorithm.

Because the RouterCallsQNow variable is only
                                 applicable at a Skillgroup and not an Enterprise Skillgroup level, then
                                 the aggregate of all the skill groups within the Enterprise Skillgroup RouterCallsQNow field must be multiplied
                                 by the Enterprise SkillGroup AvgHandledCallsTime .

The <constant> value is site
                                 dependent. It should be a value that represents the average Handle time
                                 of a call. This constant is only used if it is at the start of the
                                 day and the proper AvgHandledCallsTime has
                                 not been calculated.

| Note | For the Run External Script node to work, there must be an entry in
                                          the Network VRU list pointing to the URL map file. After the Run
                                          External Script node, the script functions just as the preceding
                                          example. |
|---|---|

| Note | You can use POD.ID to send cc_CustomerID , and this cc_CustomerID can be used to filter the data in finesse gadget. POD.ID is an optional field in Experience Management voice survey and the supported POD. ID format will be xxx, where xxx is the Customer_id. |
|---|---|

| Step 1 | In Script Editor, create the routing script as shown in the example. |
|---|---|
| Step 2 | Do the following to ensure the routing script is mapped to the call type you created for Experience Management . Navigate to Script > Call Type Manager . On the Schedules tab, from the Call Type drop-down list, select the call type that you created for Experience Management . For more information refer to the topic Call Type and Survey Association in Unified CCE Admin in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html Click Add . Click OK . For more information on optimizing the threshold values for SMS and Email batch processing, refer to the topic Configure SMS/Email Thresholds in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html |

| Create Call Studio application with the use of CVP SubDialogReurn element and fill the customer data as external VXML variables. Example: External VXML 0 = Email=abcd@cisco.com;cc_CustomerId=xyz;cc_language=en-US;Optin=yes;Mobile=911234567890; Note Each key-value pair is separated by a semi colon. Note The variable names are case sensitive. Figure 7. Example Refer to the following table for the variables and their descriptions. Table 1. Variables and their descriptions Variable Name Description Required/Optional cc_CustomerId Unique ID for a customer across multiple channels. Required Email Customer email ID Either email or phone number is required Mobile Customer mobile number with country code. Example: 919911223344 Either email or phone number is required cc_language Survey language Example: en-US Optional Optin Option to check if customer wants to opt for the survey: Values: yes/no Default value is yes when the value is not captured from Call Studio. Optional | Note | Each key-value pair is separated by a semi colon. | Note | The variable names are case sensitive. | Variable Name | Description | Required/Optional | cc_CustomerId | Unique ID for a customer across multiple channels. | Required | Email | Customer email ID | Either email or phone number is required | Mobile | Customer mobile number with country code. Example: 919911223344 | Either email or phone number is required | cc_language | Survey language Example: en-US | Optional | Optin | Option to check if customer wants to opt for the survey: Values: yes/no Default value is yes when the value is not captured from Call Studio. | Optional |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note | Each key-value pair is separated by a semi colon. |
| Note | The variable names are case sensitive. |
| Variable Name | Description | Required/Optional |
| cc_CustomerId | Unique ID for a customer across multiple channels. | Required |
| Email | Customer email ID | Either email or phone number is required |
| Mobile | Customer mobile number with country code. Example: 919911223344 | Either email or phone number is required |
| cc_language | Survey language Example: en-US | Optional |
| Optin | Option to check if customer wants to opt for the survey: Values: yes/no Default value is yes when the value is not captured from Call Studio. | Optional |

| Note | Each key-value pair is separated by a semi colon. |
|---|---|

| Note | The variable names are case sensitive. |
|---|---|

| Variable Name | Description | Required/Optional |
|---|---|---|
| cc_CustomerId | Unique ID for a customer across multiple channels. | Required |
| Email | Customer email ID | Either email or phone number is required |
| Mobile | Customer mobile number with country code. Example: 919911223344 | Either email or phone number is required |
| cc_language | Survey language Example: en-US | Optional |
| Optin | Option to check if customer wants to opt for the survey: Values: yes/no Default value is yes when the value is not captured from Call Studio. | Optional |

| Step 1 | Create the ICM script as shown in the following screen shot: |
|---|---|
| Step 2 | Fill the ECC variable POD.ID values from user.microapp.FromExtVXML array and pass it to ICM. Example: POD.ID=cc_CustomerId=xyz;Email=abcd@cisco.com;cc_language=en-US;Optin=yes;Mobile=911234567890; |
| Step 3 | Save the script. |

| Note | In a Unified ICM integrated with the ECE , the allowed responses for an invoked route request are: Return an Agent, Return a Label, or Failure (the script could not
                                                be found or something is wrong). The ECE deals with this by placing the e-mail message into the externalRoutingError system queue. |
|---|---|

| Note | To assign a message directly to an agent, the Unified ICM script
                                                must use the Queue to Agent node to route e-mail messages, not
                                                the Agent node. |
|---|---|

| Note | While the system software can assign a message directly to a local ECE routing skill group, you would not typically design a script to do this without first trying to queue the message to a skill
                                                group or directly to an agent. If the message, based on its content, is meant to be assigned to a local ECE routing skill group, you could make that assignment directly through ECE rules, and not use the software. |
|---|---|

| Note | The ICM wait node can be used to keep the email in the queue when the agent is not available (for example, during a weekend)
                                          by setting the wait node to a high value such as 172800 seconds (48 hours). The maximum time that an activity can remain in
                                          the ICM queue is determined by the MRD setting "Max time in queue".  By default, this setting is blank for all MRDs and the
                                          setting defined in the router registry is used. |
|---|---|

| Note | These Expanded Call Context (ECC) variables are optional. Before you use these ECC variables, configure them in Unified CCE
                                             and ECE. To configure these ECC variables in Configuration Manager's Expanded Call Variable List Tool, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . To configure these ECC variables in ECE, see at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html . |
|---|---|

| Note | Additional Unified CCE example scripts are available in the Cisco Unified Contact Center Enterprise Reporting User Guide at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html . |
|---|---|

| Note | If the administrative script (where the OutboundControl variable or
                                          reservation percentage is set) is running, but the modes/percentages are
                                          not being updated at the Dialer, do the following: Make sure that the
                                                   skill group being controlled is the base skill group, and not the
                                                   primary or secondary skill groups. Although agents may be logged in to
                                                   just the primary or secondary skill group, the outbound control variable
                                                   must always be set on the base skill group Verify that the outbound
                                                   control variable mode is spelled correctly. |
|---|---|

| Note | This variable does not allocate specific agents for outbound dialing,
                                          just a total percentage. |
|---|---|

| Warning | You must set the outbound percentage in the Set node to a value other than zero (0) or it appears to the node that there are
                                             no agents assigned to the Outbound Option and no outbound calls will be made. |
|---|---|

| Warning | Do not use Select Route nodes, multiple skill groups, or services. |
|---|---|

| Note | Translation routes are not used in the Unified CCE System PG, so routing scripts using this PG do not need to use this object. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Right-click the Queue to Agent node and select Properties . |  |
| Step 2 | Click Change in the "Queue to agent type" section. |  |
| Step 3 | Click Lookup agent reference by expression ,
                                          then click OK . |  |
| Step 4 | Enter the agent expression Call.PreferredAgentID. |  |
| Step 5 | Make sure the Peripheral column is left blank. |  |
| Step 6 | Select the enterprise skill group. |  |
| Step 7 | Select the enterprise route. |  |
| Step 8 | Click OK to save the Queue to Agent
                                          node. |  |

| Note | Lines connecting objects cannot appear on top of objects and therefore, partially display under the objects. For example,
                                             the line connecting the "X" (output terminal failure) on the Select object to the End object runs partially under the Select object. |
|---|---|

| Note | The current estimated wait time is determined using a rolling five-minute window and may be 0 or -1 based on the following
                                          conditions: A value of 0 indicates that there are no calls queued in the skill group or precision queue. A value of -1 indicates that there is not enough call data within the last five-minute window to calculate the estimated wait
                                                time (EWT). |
|---|---|