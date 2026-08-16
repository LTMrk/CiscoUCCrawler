---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-ucce-b-1501-5569b1feb5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/ucce_b_1501_features-guide/ucce_m_1501_agent-request.html
retrieved_at: 2026-08-16T20:08:58.661692+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Agent Request

## Chapter: Agent Request

# Agent Request

## Agent Request Feature Description

The Agent Request feature allows a customer to initiate a request on the web that results in a call from an agent.

To use Agent Request, your solution requires the Cisco Customer Collaboration Platform optional component. Cisco Customer
                              Collaboration Platform works in a Contact Center Enterprise (CCE) solution to process the request from its inception through
                              the delivery of the callback.

Important

The Agent Request feature can be used only if the customer or a partner develops a custom application. There is sample code
                                          on DevNet (formerly Cisco Developer Network) that you can use to understand how to start building your custom application
                                          to submit callback requests to Customer Collaboration Platform.

### Customer Collaboration Platform and Agent Request

Customer Collaboration Platform provides the Callback API used by a custom application to request a phone call from a contact
                              center agent.

The API works in conjunction with Customer Collaboration Platform callback feeds, campaigns, and notifications to pass callback
                              requests to the contact center for routing.

The Callback API:

Allows custom applications to initiate a callback.

Forwards the callback request and callback details to CCE using a notification mechanism (the Connection to CCE notification
                                    type) through a Media Routing (MR) connection.

Allows custom applications to retrieve the state of the callback as well as the estimated wait time (EWT) until an agent
                                    becomes available.

Allows custom applications to cancel a requested callback.

The Callback API supports the use of Call variables and ECC variables for callback requests. Call variables and ECC variables
                              send customer-specific information with the request. When you create a callback contact, the social contact associated with
                              the callback contact includes all of the specified variables as extension fields.

### CCE and Agent Request

When it receives an Agent Request, CCE performs the following tasks:

Process the callback request.

Route the callback request to an agent and place a call from the agent's phone to the customer.

Notify Customer Collaboration Platform that the agent has been selected.

### Agent Desktops and Agent Request

Cisco Finesse supports Agent Request.

### Enterprise Chat and Email

To configure prefixes and filters for dialed numbers in Enterprise Chat and Email, you must use the Unified CCE Script Editor.

### Unsupported Environments

Agent Request is not supported:

In a Parent/Child deployment

With Mobile Agents

In a hybrid deployment

### Agent Request Prerequisites

Install and configure Customer Collaboration Platform before implementing Agent Request. Customer Collaboration Platform must be geographically colocated with one side of the Media Routing Peripheral Gateway (MR PG).

The customer or partner must build a custom application for the Agent Request feature. See Use the Sample Code to Create a Customer Callback Request .

Customer Collaboration Platform is always deployed in a DMZ. Remember to open the port you have configured for the MR PG. See Set up the Media Routing PG and PIM .

### Agent Request Call Flow

The flow proceeds as follows:

The customer application initiates an agent request by requesting a callback.

Customer Collaboration Platform sends the request to the Media Routing PG.

The Media Routing PG sends the request to the Router.

The Router sends the request to the Agent PG.

The Agent PG sends the request to the agent.

A call is initiated from the agent's phone, on behalf of the agent, dialing the customer's phone number.

The agent does not control when the call is placed.

### Agent Request Scenarios

From the web, the customer requests to speak to an agent.

The customer receives feedback that the request is accepted.

The customer receives feedback that the call is queued and the estimated wait time.

The customer receives feedback that a call is on its way.

The agent's phone places an outbound call.

The agent is presented with call context.

The customer is available

The customer receives and answers the call, and speaks to the agent

The customer is busy when the callback occurs

The agent receives a busy tone

The customer does not answer when the callback occurs

The agent hears ringing

The customer cancels the callback before an agent is selected

There is no impact on the agent

## Configure Unified CCE for Agent Request

The following information describes how to configure Agent Request for a Unified CCE deployment.

### Configuration Manager

Use these Configuration Manager tools and procedures to configure Agent Request.

#### Configure Network VRU and Network VRU Script

Step 1

In the Configuration Manager, use the Network VRU Explorer tool to configure and save a type 2 VRU.

The Network VRU is used to queue voice callback tasks if an agent is not available to handle them.

Step 2

In the Configuration Manager, use the Network VRU Script List tool to add a Network VRU Script that references the Network
                                             VRU that you configured in Step 1.

The Network VRU Script is used for Estimated Wait Time.

#### Configure the Media Routing PG and PIM

Step 1

In Configuration Manager, open the PG Explorer tool to configure a media routing PG.

Step 2

Create a media routing PIM and routing client for Customer Collaboration Platform .

Write down the Logical Controller ID and the Peripheral ID. You will use them when you set up the PG.

Step 3

On the Peripheral tab in the PG Explorer tool, check the Enable post routing check box.

Step 4

On the Routing Client tab in the PG Explorer tool, select the Multichannel option from the Routing Type drop-down list box.

Step 5

On the Advanced tab in the PG Explorer tool, select the type 2 Network VRU that you created.

#### Configure Call Type

Open the Call Type List tool, and create a call type to handle calls from an agent request voice callback.

#### Configure Dialed Number/Script Selector

Step 1

Open the Dialed Number/Script Selector List tool, and create a script selector on the routing client that you configured. Customer Collaboration Platform uses this script selector to request agents for voice callback. (The script selector configured here must be the same as
                                             the one entered in the Customer Collaboration Platform notification.)

Step 2

On the Attributes tab, select Cisco_Voice from the Media routing domain drop-down list box.

Step 3

On the Dialed Number Mapping tab, map the script selector to the call type you created.

#### Configure ECC Variables

Step 1

Open the Expanded Call Variable List tool.

Step 2

Add one or more ECC Variables for the callback request.

Arrays are not supported with the Agent Request feature.

CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                            CVP, Finesse, and Customer Collaboration Platform . CCE also supports the use of multi-byte character sets in limited usage for ECC and call variables when setting them in
                                                            Script Editor using double quotes.

### Set up the Media Routing PG and PIM

Step 1

From Cisco Unified CCE Tools, select Peripheral Gateway Setup .

Step 2

On the Components Setup screen, in the Instance Components panel, select the PG Instance component.

Step 3

If the PG does not exist, click Add ; if the PG exists, click Edit .

Step 4

Click Yes at the prompt to stop the service.

Step 5

From the Peripheral Gateway Component Properties screen, click Add , select the next PIM, and configure with the Client Type of Media Routing as follows.

Check Enabled .

In the Peripheral Name field, enter MR .

For Application Hostname (1) , enter the hostname or IP address of Customer Collaboration Platform .

The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                               for all the Hostname/ IP Address fields.

By default, Customer Collaboration Platform accepts the MR connection on Application Connection Port 38001. The Application Connection Port setting on Customer Collaboration Platform must match the setting on the MR PG; if you change the port on one side of the connection, you must change it on the other
                                                side.

Leave the Application Hostname (2) , field blank.

Keep all other values.

Click OK .

Step 6

On the Peripheral Gateway Component Properties screen, enter the Logical Controller ID that you recorded when you configured
                                          the Media Routing PG and PIM.

Step 7

Accept defaults and click Next until the Setup Complete screen opens.

Step 8

At the Setup Complete screen, check Yes to start the service, and then click Finish .

Step 9

Click Exit Setup .

Step 10

Repeat from Step 1 for Side B.

Step 11

Navigate to Unified CCE Administration > Infrastructure Settings > Inventory .

Step 12

Add Customer Collaboration Platform as an external machine.

Click Add .

Select Customer Collaboration Platform from the drop-down list.

Enter the required information.

Click Save .

## Configure Customer Collaboration Platform for a Voice Callback Agent Request

To support a callback request, Customer Collaboration Platform must be configured with:

A callback feed

A campaign

A Connection to CCE notification configured for the campaign mentioned above that will be triggered by incoming callback requests
                                    with a matching tag.

### Create Feed

Step 1

Sign in to Customer Collaboration Platform .

Step 2

Click Configuration .

Step 3

On the Manage Feeds panel, click New .

Step 4

For Type , select Callback .

Step 5

Name the feed.

Step 6

For Reply Template , retain the default No reply template .

Step 7

Configure the feed to automatically tag all callback requests that come in on that feed. For example, autotag with 'sendtocontactcenter'.

Make a note of the tag; it triggers the notification to CCE.

Step 8

Click Save .

### Create Campaign

Step 1

Sign in to Customer Collaboration Platform .

Step 2

Click Configuration .

Step 3

On the Manage Campaigns panel, click New .

Step 4

Name the campaign.

Step 5

Enter an optional description.

Step 6

Make no selection in the Chat Invitation Feed drop-down list.

Step 7

Locate the Callback feed in the Available panel and move it to Selected .

Step 8

Click Save .

### Create Notification

Step 1

Sign in to Customer Collaboration Platform .

Step 2

Click Administration .

Step 3

On the Manage Notifications panel, click New .

Step 4

For Type , select Connection to CCE .

Step 5

Name the notification.

Step 6

From the Campaigns drop-down list, select the campaign that you created for the callback.

Step 7

In the Tags field, enter the tag that is automatically applied to callback requests by the feed.

In our example 'sendtocontactcenter'.

Step 8

For Request Type , select Callback .

Step 9

In the Dialed Number/Script Selector field, enter the dialed number string that you have configured.

Unified CCE— Configure Dialed Number/Script Selector

Step 10

Click Save .

#### What to do next

For more Customer Collaboration Platform configuration information, see the Cisco Customer Collaboration Platform User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/socialminer/products-user-guide-list.html .

## Agent Request Script

The Agent Request Script is used to implement an optional dial-plan, queue a call to the skill group node, and calculate the
                           estimated wait time for a voice callback to a customer.

A customer who requests a voice callback might want to know approximately how long it will be before the call is returned.
                           You can configure voice callback to provide an estimate of the wait time back to the customer. The estimated wait time is
                           calculated once, when the call enters the queue. The time is not updated as the position in the queue changes.

The default estimated wait time algorithm is based on a running five minute window of the rate of calls leaving the queue.
                           Any calls that are routed or abandoned during the first five minutes are taken into account as part of the rate leaving queue.
                           For Precision Queues, the rate leaving queue represents the rate at which calls are delivered or abandoned from the entire
                           Precision queue, not any individual Precision Queue steps. The algorithm computes the wait time for each of the queues against
                           which the call is queued (Skill Groups or Precision Queues) and then returns the minimum estimated wait time. Queue to Agent
                           is not supported.

While the queue builds, the small number of calls in the queue makes the estimated wait time less accurate and the value fluctuates
                           rapidly. As the queue operates with more calls over time, the estimated wait time is more accurate and consistent.

The built-in function also applies to inbound calls that queue.

### Create Agent Request Script

Step 1

Start node: Create the Start node by selecting a new Routing Script from the Script Editor.

Step 2

(Optional) Set Variable (Call.Calling Line ID) node: If required, set the CallingLineID (CLID/ ANI) node to implement a "dial-plan," prepending a set of digits to the phone number provided by the customer so that it can be
                                          correctly routed.

For example, it is often necessary to add 9 to the phone number to reach an outside line. In other cases, more prepended digits
                                             may be required to reach the end customer.

You can also set up Unified Communications Manager Route Patterns to respond to a certain set of digits by routing the call
                                             to an outside line with a specified area code. To implement a dial-plan, add a Set Variable node before the queue, as shown
                                             in this example. In this case, a 9 is pre-pended to the customer phone number using the built-in concatenate function.

Step 3

Queue to Skill Group node: Queue to Skill Group node.

The Agent Request call can be queued against one or more Skill Groups, Precision Queues, or a queue-to-agent node. In the
                                             example script, the call is queued against a single skill group.

Step 4

Set Variable (Call.Estimated Wait Time) node: Set the Call Wait time as follows:

From the Set Variable node, select Call from the Object type drop-down menu.

From the Variable drop-down menu, choose Estimated Wait Time() . You can then work with the Formula Editor to use the default estimated wait value or create a formula and use your own value.

Click Formula Editor . You can either use the default estimated wait value, by clicking the Built-In Functions tab and choosing EstimatedWaitTime() . Or to create a formula and use your own estimated time value, click the Variables tab, and choose an entry in the Object type list and Object list. Then double-click a variable in the Variable list.

Step 5

Run Ext Script node: Apply the Network VRU script as follows:

Click the Queue tab.

Click Run External Script .

Click inside the script. A Run External Script node appears.

Double-click the node and choose the Network VRU script from the list and then click OK . The call variable Estimated Wait Time now contains a value in the EstimatedWaitTime field and can be passed to peripherals.

Note that a Run External Script node is required to send the EstimatedWaitTime to Customer Collaboration Platform .

Step 6

Wait node: The wait period for an agent becomes available.

Step 7

End node: The script ends if no agent becomes available.

## Use the Sample Code to Create a Customer Callback Request

Cisco Systems has made sample callback application code available to use as a baseline in building your own application. This
                              sample includes retrieving and displaying the estimated wait time, assuming it has been configured in Unified CCE . You can find the sample code on DevNet.

You cannot copy and paste this code to achieve a working application. It is a only a guideline.

For more information about how to use the Callback API, see the Cisco Customer Collaboration Platform Developer Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html .

Step 1

Retrieve the feed id by entering this URL in a browser: https://< Customer Collaboration Platform _Hostname_or_Ip>/ccp-webapp/ccp/feed .

In the example output below, note that the value in the <name> field is "Callback." Look for the number of the feed id identified
                                          at the end of the refURL path (in this case, it is 100000) just before the </refURL> tag. Copy this number.

```
<feeds>
<Feed>
<changeStamp>0</changeStamp>
<name>Callback</name>
<pushFeedURL>https://128.107.81.27/ccp/callback/feed/100000</pushFeedURL>
<refURL>https://128.107.81.27/ccp-webapp/ccp/feed/100000</refURL>
<status>1</status>
<tags>
<tag>trial</tag>
</tags>
<type>10</type>
</Feed>
</feeds>
```

Step 2

Access the sample application from DevNet: https://developer.cisco.com .

Step 3

Enter values in the fields:

Title: A title or subject for the callback request.

Author: The name of the person submitting the callback request.

Phone: The phone number to call back.

Feed Id: The value from the refURL above.

Step 4

Click Call me back .

## Agent Request Reporting

Cisco Unified Intelligence Center CCE reports include data for Agent Requests.

Agent requests that fail before being routed to CCE will not be included in the CCE solution-level reports. The Customer Collaboration Platform search function can be used to identify these requests.

### Call Type and Call Type Skill Group Metrics

Calls Offered — Incremented when Call Type is entered (through Script Selector or Call Type node).

Calls Abandoned in Queue — Incremented when a Queued Callback request is canceled by the customer prior to when an Agent is selected to handle the
                                    Voice Callback call.

Calls Answered — Incremented if the call is placed from the agent and represents work accepted by the agent.

Calls Handled — Incremented if the customer answers the call. Calls Answered minus Calls Handled indicates how many calls failed to reach
                                    the intended customer.

Service Level Offered — Incremented for all routed calls, including voice callback calls initiated through the agent request API.

ServiceLevelCalls — Incremented if the call is presented to the agent within a service level.

Answer Intervals (1 - 10) — The appropriate bucket is incremented based on how long the call was in the queue.

### Skill Group Metrics

Call Type Skill Group and Skill Group metrics are not counted in the same way. The skill group metric treats each call as
                              agent-initiated; therefore, Calls Answered and Calls Handled are not incremented. AgentOutCallsTime, AgentOutCalls, AgentOutCallsTalkTime,
                              AgentOutCallsOnHold, and AgentOutCallsOnHoldTime are incremented.

### Agent Real Time

The direction in the Agent Real Time table is listed as Outbound.

### Termination Call Detail

For custom reporting, the Termination Call Detail records contain a PeripheralCallType of 41 -Voice Callback.

Calls which do not successfully connect to a customer have a call disposition of 10 - Disconnect/Drop no answer . This includes agent request calls to busy numbers.

| Important | The Agent Request feature can be used only if the customer or a partner develops a custom application. There is sample code
                                          on DevNet (formerly Cisco Developer Network) that you can use to understand how to start building your custom application
                                          to submit callback requests to Customer Collaboration Platform. |
|---|---|

| Note | The agent does not control when the call is placed. |
|---|---|

| If | Then |
|---|---|
| The customer is available | The customer receives and answers the call, and speaks to the agent |
| The customer is busy when the callback occurs | The agent receives a busy tone |
| The customer does not answer when the callback occurs | The agent hears ringing |
| The customer cancels the callback before an agent is selected | There is no impact on the agent |

| Note | Configure Unified CCE before you configure Customer Collaboration Platform. |
|---|---|

| Step 1 | In the Configuration Manager, use the Network VRU Explorer tool to configure and save a type 2 VRU. The Network VRU is used to queue voice callback tasks if an agent is not available to handle them. |
|---|---|
| Step 2 | In the Configuration Manager, use the Network VRU Script List tool to add a Network VRU Script that references the Network
                                             VRU that you configured in Step 1. The Network VRU Script is used for Estimated Wait Time. |

| Step 1 | In Configuration Manager, open the PG Explorer tool to configure a media routing PG. |
|---|---|
| Step 2 | Create a media routing PIM and routing client for Customer Collaboration Platform . Write down the Logical Controller ID and the Peripheral ID. You will use them when you set up the PG. |
| Step 3 | On the Peripheral tab in the PG Explorer tool, check the Enable post routing check box. |
| Step 4 | On the Routing Client tab in the PG Explorer tool, select the Multichannel option from the Routing Type drop-down list box. |
| Step 5 | On the Advanced tab in the PG Explorer tool, select the type 2 Network VRU that you created. |

| Open the Call Type List tool, and create a call type to handle calls from an agent request voice callback. |
|---|

| Step 1 | Open the Dialed Number/Script Selector List tool, and create a script selector on the routing client that you configured. Customer Collaboration Platform uses this script selector to request agents for voice callback. (The script selector configured here must be the same as
                                             the one entered in the Customer Collaboration Platform notification.) |
|---|---|
| Step 2 | On the Attributes tab, select Cisco_Voice from the Media routing domain drop-down list box. |
| Step 3 | On the Dialed Number Mapping tab, map the script selector to the call type you created. |

| Step 1 | Open the Expanded Call Variable List tool. |
|---|---|
| Step 2 | Add one or more ECC Variables for the callback request. Note Arrays are not supported with the Agent Request feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                            CVP, Finesse, and Customer Collaboration Platform . CCE also supports the use of multi-byte character sets in limited usage for ECC and call variables when setting them in
                                                            Script Editor using double quotes. | Note | Arrays are not supported with the Agent Request feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                            CVP, Finesse, and Customer Collaboration Platform . CCE also supports the use of multi-byte character sets in limited usage for ECC and call variables when setting them in
                                                            Script Editor using double quotes. |
| Note | Arrays are not supported with the Agent Request feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                            CVP, Finesse, and Customer Collaboration Platform . CCE also supports the use of multi-byte character sets in limited usage for ECC and call variables when setting them in
                                                            Script Editor using double quotes. |

| Note | Arrays are not supported with the Agent Request feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                            CVP, Finesse, and Customer Collaboration Platform . CCE also supports the use of multi-byte character sets in limited usage for ECC and call variables when setting them in
                                                            Script Editor using double quotes. |
|---|---|

| Step 1 | From Cisco Unified CCE Tools, select Peripheral Gateway Setup . |
|---|---|
| Step 2 | On the Components Setup screen, in the Instance Components panel, select the PG Instance component. |
| Step 3 | If the PG does not exist, click Add ; if the PG exists, click Edit . |
| Step 4 | Click Yes at the prompt to stop the service. |
| Step 5 | From the Peripheral Gateway Component Properties screen, click Add , select the next PIM, and configure with the Client Type of Media Routing as follows. Check Enabled . In the Peripheral Name field, enter MR . For Application Hostname (1) , enter the hostname or IP address of Customer Collaboration Platform . Note The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                               for all the Hostname/ IP Address fields. By default, Customer Collaboration Platform accepts the MR connection on Application Connection Port 38001. The Application Connection Port setting on Customer Collaboration Platform must match the setting on the MR PG; if you change the port on one side of the connection, you must change it on the other
                                                side. Leave the Application Hostname (2) , field blank. Keep all other values. Click OK . | Note | The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                               for all the Hostname/ IP Address fields. |
| Note | The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                               for all the Hostname/ IP Address fields. |
| Step 6 | On the Peripheral Gateway Component Properties screen, enter the Logical Controller ID that you recorded when you configured
                                          the Media Routing PG and PIM. |
| Step 7 | Accept defaults and click Next until the Setup Complete screen opens. |
| Step 8 | At the Setup Complete screen, check Yes to start the service, and then click Finish . |
| Step 9 | Click Exit Setup . |
| Step 10 | Repeat from Step 1 for Side B. |
| Step 11 | Navigate to Unified CCE Administration > Infrastructure Settings > Inventory . |
| Step 12 | Add Customer Collaboration Platform as an external machine. Click Add . Select Customer Collaboration Platform from the drop-down list. Enter the required information. Click Save . The system automatically enables and completes the CCE Configuration for Multichannel Routing settings in Customer Collaboration Platform Administration, including the Application Connection Port you specified. |

| Note | The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                               for all the Hostname/ IP Address fields. |
|---|---|

| Step 1 | Sign in to Customer Collaboration Platform . |
|---|---|
| Step 2 | Click Configuration . |
| Step 3 | On the Manage Feeds panel, click New . |
| Step 4 | For Type , select Callback . |
| Step 5 | Name the feed. |
| Step 6 | For Reply Template , retain the default No reply template . |
| Step 7 | Configure the feed to automatically tag all callback requests that come in on that feed. For example, autotag with 'sendtocontactcenter'. Make a note of the tag; it triggers the notification to CCE. |
| Step 8 | Click Save . |

| Step 1 | Sign in to Customer Collaboration Platform . |
|---|---|
| Step 2 | Click Configuration . |
| Step 3 | On the Manage Campaigns panel, click New . |
| Step 4 | Name the campaign. |
| Step 5 | Enter an optional description. |
| Step 6 | Make no selection in the Chat Invitation Feed drop-down list. |
| Step 7 | Locate the Callback feed in the Available panel and move it to Selected . |
| Step 8 | Click Save . |

| Step 1 | Sign in to Customer Collaboration Platform . |
|---|---|
| Step 2 | Click Administration . |
| Step 3 | On the Manage Notifications panel, click New . |
| Step 4 | For Type , select Connection to CCE . |
| Step 5 | Name the notification. |
| Step 6 | From the Campaigns drop-down list, select the campaign that you created for the callback. |
| Step 7 | In the Tags field, enter the tag that is automatically applied to callback requests by the feed. In our example 'sendtocontactcenter'. |
| Step 8 | For Request Type , select Callback . |
| Step 9 | In the Dialed Number/Script Selector field, enter the dialed number string that you have configured. Unified CCE— Configure Dialed Number/Script Selector |
| Step 10 | Click Save . |

| Note | The built-in function also applies to inbound calls that queue. |
|---|---|

| Step 1 | Start node: Create the Start node by selecting a new Routing Script from the Script Editor. |
|---|---|
| Step 2 | (Optional) Set Variable (Call.Calling Line ID) node: If required, set the CallingLineID (CLID/ ANI) node to implement a "dial-plan," prepending a set of digits to the phone number provided by the customer so that it can be
                                          correctly routed. For example, it is often necessary to add 9 to the phone number to reach an outside line. In other cases, more prepended digits
                                             may be required to reach the end customer. You can also set up Unified Communications Manager Route Patterns to respond to a certain set of digits by routing the call
                                             to an outside line with a specified area code. To implement a dial-plan, add a Set Variable node before the queue, as shown
                                             in this example. In this case, a 9 is pre-pended to the customer phone number using the built-in concatenate function. |
| Step 3 | Queue to Skill Group node: Queue to Skill Group node. The Agent Request call can be queued against one or more Skill Groups, Precision Queues, or a queue-to-agent node. In the
                                             example script, the call is queued against a single skill group. |
| Step 4 | Set Variable (Call.Estimated Wait Time) node: Set the Call Wait time as follows: From the Set Variable node, select Call from the Object type drop-down menu. From the Variable drop-down menu, choose Estimated Wait Time() . You can then work with the Formula Editor to use the default estimated wait value or create a formula and use your own value. Click Formula Editor . You can either use the default estimated wait value, by clicking the Built-In Functions tab and choosing EstimatedWaitTime() . Or to create a formula and use your own estimated time value, click the Variables tab, and choose an entry in the Object type list and Object list. Then double-click a variable in the Variable list. |
| Step 5 | Run Ext Script node: Apply the Network VRU script as follows: Click the Queue tab. Click Run External Script . Click inside the script. A Run External Script node appears. Double-click the node and choose the Network VRU script from the list and then click OK . The call variable Estimated Wait Time now contains a value in the EstimatedWaitTime field and can be passed to peripherals. Note that a Run External Script node is required to send the EstimatedWaitTime to Customer Collaboration Platform . |
| Step 6 | Wait node: The wait period for an agent becomes available. |
| Step 7 | End node: The script ends if no agent becomes available. |

| Note | You cannot copy and paste this code to achieve a working application. It is a only a guideline. |
|---|---|

| Step 1 | Retrieve the feed id by entering this URL in a browser: https://< Customer Collaboration Platform _Hostname_or_Ip>/ccp-webapp/ccp/feed . In the example output below, note that the value in the <name> field is "Callback." Look for the number of the feed id identified
                                          at the end of the refURL path (in this case, it is 100000) just before the </refURL> tag. Copy this number. <feeds>
<Feed>
<changeStamp>0</changeStamp>
<name>Callback</name>
<pushFeedURL>https://128.107.81.27/ccp/callback/feed/100000</pushFeedURL>
<refURL>https://128.107.81.27/ccp-webapp/ccp/feed/100000</refURL>
<status>1</status>
<tags>
<tag>trial</tag>
</tags>
<type>10</type>
</Feed>
</feeds> |
|---|---|
| Step 2 | Access the sample application from DevNet: https://developer.cisco.com . |
| Step 3 | Enter values in the fields: Title: A title or subject for the callback request. Author: The name of the person submitting the callback request. Phone: The phone number to call back. Feed Id: The value from the refURL above. |
| Step 4 | Click Call me back . |

| Note | Agent requests that fail before being routed to CCE will not be included in the CCE solution-level reports. The Customer Collaboration Platform search function can be used to identify these requests. |
|---|---|