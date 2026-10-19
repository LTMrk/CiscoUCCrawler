---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-maintenance-guide-pcce-b-1501-f-a8c2922a43
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/maintenance/guide/pcce_b_1501_features-guide/pcce_m_1501_ece-webex-connect-co-deployment.html
retrieved_at: 2026-10-19T10:47:54.874799+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: ECE and Webex Connect Co-deployment in Packaged CCE

## Chapter: ECE and Webex Connect Co-deployment in Packaged CCE

# ECE and Webex Connect Co-deployment in Packaged CCE

## Overview

CCE customers have been using ECE for digital channels, such as Chat and Email, for an extended period. With Digital Channels
                           Integration using Webex Connect in 12.6(2), Packaged CCE supports a wide variety of communication channels, including SMS,
                           Email, Facebook Messenger, WhatsApp, Live Chat, and Apple Messages for Business.

You can deploy Webex Connect and ECE together on a single Packaged CCE instance. This co-deployment enables contact center
                           agents to handle ECE interactions and Webex Connect digital-channel interactions independently from the same Cisco Finesse
                           desktop.

This co-deployment improves the agent experience by providing a seamless and consistent workflow across digital channels.

## Prerequisites

Before you configure ECE and Webex Connect in the same Packaged CCE deployment, meet the following requirements:

Configure ECE and Webex Connect individually.

Install ECE and provision Webex Connect for your organization through Cisco Commerce Workspace (CCW) or Control Hub.

Use Packaged CCE and ECE Release 15.0(1) SU2/ES202607. Use Cloud Connect and Cisco Finesse Release 15.0(1) SU2.

Enable Single Sign-On (SSO) for agents in both Packaged CCE and ECE. The Manage Digital Channels gadget authenticates with
                                 Webex Engage in SSO mode.

Create separate Media Routing Domains (MRDs) for ECE and Webex Connect. The two integrations cannot share an MRD.

Ensure that agents belong to the skill groups associated with the applicable nonvoice MRDs.

For deployments with multiple Agent PGs across main and remote sites, see Configuring Application Path in chapter Prepare Packaged CCE for the Integration of the Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise, Release 15.0(1) .

Obtain administrator access to Packaged CCE Administration, Configuration Manager, Cloud Connect, ECE, Webex Connect, Webex
                                 Engage, and Cisco Finesse.

This feature supports Packaged CCE deployments across the supported reference designs.

## Workflow for Configuring ECE and Webex Connect Co-deployment

Step

Task

ECE Digital Channels

Webex Connect Digital Channels

1

Establish certificate trust.

For more information, see the
                                       Establish secured connection between Cloud Connect and MR PG using self-signed certificate
                                       and
                                       Establish secured connection between Cloud Connect and MR PG using CA-signed certificate
                                       of the Certificate Management for Secured Connections chapter in Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) .

2

Add Cloud Connect to the Packaged CCE inventory.

In Packaged CCE Administration, go to Overview > Inventory . Click New and enter the Cloud Connect publisher details. Cloud Connect automatically discovers the subscriber details from the publisher.
                                       Verify the discovered subscriber details and save the inventory configuration.

For more information, see
                                       Configure Cloud Connect for 2000 Agent Deployment
                                       or
                                       Configure Cloud Connect for 4000/12000 Agent Deployment
                                       of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) .

3

Configure the Media Routing PIMs.

The MR PG is created automatically in Packaged CCE, but you must configure its PIMs.

In the Peripheral Gateway Component Properties window, click Add . From Client Type , select Media Routing . Select the required Media Routing PIM and click OK .

Enable the PIM and enter its peripheral name. In Peripheral ID , enter the Peripheral ID of the applicable peripheral. Do not enter the Logical Controller ID.

In Application Hostname (1) , enter the hostname or IP address of the Cloud Connect publisher. In Application Connection Port (1) , enter the application port. The default port is 38001 .

In Application Hostname (2) , enter the hostname or IP address of the Cloud Connect subscriber. In Application Connection Port (2) , enter 38001 . Leave these fields empty only when a secondary Cloud Connect server is not deployed.

Set the heartbeat interval to 5 seconds and the reconnect interval to 10 seconds. Enable the secure connection and click OK .

For complete field descriptions, see
                                       Add PIMs to the Media Routing Peripheral Gateway
                                       of the Optional Configurations chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) .

4

Create unique MRDs and associate them with application paths.

Create a unique media routing domain for each ECE channel, such as chat and email, and map the MRD to the ECE instance.

For each Agent PG, create an ECE application path and add all ECE MRD-peripheral combinations that apply to the Agent PG.
                                       The application path can carry inbound email, outbound email, chat, callback, and delayed-callback activities.

Use the Media Routing Domain List tool to create the MRDs.

For more information, see
                                       Add and Maintain Media Routing Domains
                                       of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) .

Create unique MRDs for the Webex Connect digital channels that require separate reporting or queue behavior. You can also
                                       map multiple Webex Connect-powered channels under a single MRD if your deployment does not require channel-specific routing
                                       behavior.

For more information, see
                                       Add and Maintain Media Routing Domains
                                       of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) .

If you create the MRD in Packaged CCE Administration, it is automatically associated with the system-defined application path
                                       whose name ends in UQ.Desktop . If you create the MRD using Configuration Manager, manually associate it with the system-defined application path in List Tools > Application Path List Box > Attributes .

For more information, see
                                       Set up Media Channels
                                       of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) .

5

Create skill groups and assign agents.

Create skill groups or precision queues for the applicable nonvoice MRDs. Ensure that each agent belongs to a skill group
                                       associated with the nonvoice MRD that is linked to the required application path.

For more information, see
                                       Add and Maintain Skill Groups
                                       and
                                       Add and Maintain Precision Queues
                                       of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) .

6

Configure SSO and agent synchronization.

Enable Agent SSO in ECE.

For ECE configuration guidance, see the Enterprise Chat and Email administration documentation .

In Packaged CCE Administration, configure Digital Channels > Digital Channel Settings > User Sync . Enter the load-balancer or reverse-proxy FQDN in Network Entry Point , enter the primary and secondary AW database connection details, test the primary connection, enable failover to the secondary
                                       AW, enable scheduled synchronization or use Sync Now , review the last-sync status and agent synchronization details, and save the configuration.

Disable User Sync before rebuilding an AW database. Re-enable it only after the AW database has synchronized with the central
                                       controller database.

For more information, see Configure User Sync of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) .

7

Configure ECC variables for Digital Routing.

Configure the ECE ECC variables required for chat, inbound email, outbound email, callback, and delayed-callback activities.
                                       For chat, inbound email, and outbound email, configure user.ece.activity.id . For callback and delayed-callback activities, configure user.ece.activity.id and user.ece.customer.name .

For more information, see Configuring Expanded Call Context (ECC) Variables of the Prepare Packaged CCE for the Integration chapter in Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise, Release 15.0(1) .

In Packaged CCE Administration, navigate to Overview > Digital Channels > Digital Channel Settings > ECC Variable . Select and save user_DR_Primary , user_DR_Backup , and user_DR_MediaResourceID as mandatory variables, and user_DR_CustomerName and user_DR_MediaChannelName as optional variables.

For the complete procedure and the required variables, see Define ECC variables of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) .

8

Integrate Cloud Connect with Webex Connect.

In Digital Channels > Digital Channel Settings > Integration , configure the OAuth2 client ID, client secret, token-request URL, POST method, application/x-www-form-urlencoded content type, and access_token JSON path.

In Webex Connect, open the CCE prebuilt integration and copy its inbound Webhook URL. Paste this URL into the Webhook configuration in Packaged CCE Administration and save the integration.

For more information, see Integrate Cloud Connect with Webex Connect of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) .

9

Add the ECE and Webex Connect Digital Channels gadgets to the Cisco Finesse desktop layout.

Add the ECE gadget to the applicable Finesse desktop layout.

For more information, see Configuring Finesse of the Prepare Packaged CCE for the Integration chapter in Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise, Release 15.0(1) .

For information about using the ECE gadgets, see the Enterprise Chat and Email User Guide for Agents and Supervisors .

Add the Manage Digital Channels gadget to the applicable Finesse desktop layout. Agents can then work on ECE and Webex Connect
                                       tasks from the same Finesse desktop.

If ECE and Webex Connect use the same keyboard shortcut, Finesse reports a shortcut conflict and disables the key combination
                                       until the conflict is resolved. Adjust or disable conflicting shortcuts in the Finesse system settings.

For more information, see Add Manage Digital Channels gadget of the Manage Desktop Layouts chapter in Cisco Finesse Administration Guide .

For more information, see Manage Desktop Layouts of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) .

10

Optionally, configure workflows, rules, or events.

Configure workflows in Cisco Finesse.

For more information, see Manage Workflows in the Cisco Finesse Administration Guide .

Configure workflows in Cisco Finesse, or configure rules and events in Webex Engage. Rules and events in Webex Engage provide
                                       similar functionality as workflows in Cisco Finesse.

For more information, see Manage Workflows of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) . For Webex Engage rules and events, see the Events and Rules topic in the Administration and Setup Guide for Webex Engage with Cisco Contact Center Enterprise .

11

Verify reporting.

Verify that CUIC reports display agent and queue activity for the ECE MRDs. Use ECE reporting applications for platform-specific
                                       interaction details.

For ECE historical reporting, see the Enterprise Chat and Email Administrator's Guide to Reports Console . For CUIC reporting, see the Cisco Unified Intelligence Center User Guide .

Verify that CUIC reports display agent and queue activity for the Webex Connect MRDs. Use Webex Connect reports for platform-specific
                                       message and interaction details.

For more information, see Reporting of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) .

## Enable Notifications for ECE Gadget

To enable pop-over notifications for ECE gadgets:

Navigate to the following ECE JavaScript

```
<Install Dir>\eService\templates\finesse\gadget\agent\ece.js
```

Add the following code to the ECE JavaScript

```
finessse.containerServices.ContainerServices.init();
const showMyGadgetNotification = window.finesse.containerservices.ContainerServices.showMyGadgetNotification;
if (showMyGadgetNotification) {
    showMyGadgetNotification({
        messageFrom: task.title,    // Either the title or the message from where it is coming from
        message: detail.message,    // Detail of the message. Can be few initial lines of the message.
        isDismissable: true,        // The notification should be dismissable
        timeout: 8000,              // The notification will be shown for eight seconds on the top right corner.
        icon: {name: 'circle', size: 14, color: 'red'}      // The red circle icon will be seen in the notification popup.
    });
}
// The name and color can be changed as per the email and chat.
// It is upto you what color you would like to show on the finesse notification popup and in the notification center.
// you can use it as shown in the below comments
// icon: {name: 'email', size: 14, color: 'blue'}
// icon: {name: 'chat', size:14, color: 'green'}
```

Once activated, a red dot will appear on the "Manage Email and Chat" link in the left navigation pane in Finesse when a new
                           chat or a new email is received.

This feature would enable Notifications for new activities like chat or email, not for subsequent updates on an existing conversation.

## ECE and Webex Connect Digital Channels Comparison

Here’s a comparison of ECE and Webex Connect Digital Channels to help you understand the agent's experience when using both
                           groups of the Digital Channels in the same deployment.

Scenario/Action

ECE Digital Channels

Webex Connect Digital Channels

Agent Login/Logout

Agent Login

Prior to ES03 on ECE 12.6(1) or later, agents log into ECE automatically when they log into the Finesse Desktop. After applying the ES, agents log into
                                       Finesse Desktop and then log into ECE by clicking " Manage Chat and Email Gadget ."

Agent logs into the gadgets on multiple browsers.

Digital Channel Gadgets work as expected.

Browser is closed or the system is shut down

The agent remains active.

Default user sign-out option is set to Sign out from Voice Channel .

ECE will log out of Chat MRD in 120 seconds, while the agent's ready state may be preserved for a little longer in an Email
                                       MRD before logging out.

Agent closes the browser and logs in again within 60 seconds.

The agent state is not retained and they must log in again.

Agent closes the browser and logs in again within 120 seconds.

The agent will be logged out.

The agent will be logged out.

Agent Logout

Log out of the ECE gadget.

Logout of Finesse Desktop to logout of the Digital Channels gadget.

Display of the Finesse Digital Channel State Control (FNC) icons

ECE and Digital Channels are very similar, making it difficult to tell them apart.

Availability of the FNC icons

Prior to ES10 on ECE 12.6(1) , icons appear when agents log into the Finesse Desktop. Post the ES application, icons appear after agents click on the " Manage ECE Gadget ".

Handling Tasks

Task Transfer

Agent can transfer tasks to a queue or to an other agent.

Agent can transfer tasks to a queue only.

Task Offer

All tasks are automatically accepted.

Tasks are displayed as a pop-up dialog box in Finesse Desktop and must be accepted to begin.

Auto-pushback task

Auto-push back is supported when agent does not start the task within the configured time.

Auto-push back is not supported.

Task Interrupt/Timeout

Initiate the necessary Finesse workflow when a task is interrupted.

The Finesse workflow is not initiated as the Interrupt is not accepted.

Digital Channel gadget works as expected.

AgentState-13 (Interrupted) needs to be displayed on Agent_Real_Time when an agent is interrupted.

ECE works as expected.

RONA (Redirection on No Answer (RONA)

The task is redirected back to the queue after the agent fails to start the task within a specified time.

Workflows/Rules and Events

Applying a workflow to specific teams.

The workflow can be applied to a specific team or multiple teams.

All Rules and Events will apply to the one available team: the default team.

Applicable trigger points for the workflows or rules and events

You can create workflows for any of the trigger options listed in the When to Perform Actions drop-down in the Add Workflow gadget in Cisco Finesse.

Workflows can only be created for some of the trigger options available in the Fire When drop-down in the Events and Rules page in Webex Engage. For more information on supported options, see the Add a New Rule
                                       section in the Administration and Setup Guide for Webex Engage with Cisco Contact Center Enterprise .

Others

Conflicting keyboard shortcuts

If shortcuts of ECE and Digital Channels gadget conflict and you install Finesse 12.6(2) ES 05 , the shortcut will work on the gadget that is currently active (open in the active tab). For example, the default shortcut
                                       key Ctrl + Shift + 4 activates the Ready for Email state on whichever gadget (ECE or Digital Channel) is currently active. If the ECE gadget is
                                       active, the ECE's Email channel transitions to the Ready state. Similarly, if the Digital Channel gadget is open, the Digital
                                       Channel's Email channel transitions to the Ready state.

If there are conflicts between the ECE shortcuts and Digital Channels gadget before installing the patch, you might encounter
                                       keyboard conflict errors and the shortcut keys will not work as expected.

Inactive gadget pause during Gadget Switch

The ECE gadget does not automatically pause and stays active.

Digital Channel gadget pauses as expected.

Failover and failback of gadgets

At times, failover and failback of the ECE server may not work seamlessly.

Digital Channel gadgets failover and failback as expected.

| Step | Task | ECE Digital Channels | Webex Connect Digital Channels |
|---|---|---|---|
| 1 | Establish certificate trust. | For more information, see the
                                       Establish secured connection between Cloud Connect and MR PG using self-signed certificate
                                       and
                                       Establish secured connection between Cloud Connect and MR PG using CA-signed certificate
                                       of the Certificate Management for Secured Connections chapter in Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) . |
| 2 | Add Cloud Connect to the Packaged CCE inventory. | In Packaged CCE Administration, go to Overview > Inventory . Click New and enter the Cloud Connect publisher details. Cloud Connect automatically discovers the subscriber details from the publisher.
                                       Verify the discovered subscriber details and save the inventory configuration. For more information, see
                                       Configure Cloud Connect for 2000 Agent Deployment
                                       or
                                       Configure Cloud Connect for 4000/12000 Agent Deployment
                                       of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) . |
| 3 | Configure the Media Routing PIMs. | The MR PG is created automatically in Packaged CCE, but you must configure its PIMs. In the Peripheral Gateway Component Properties window, click Add . From Client Type , select Media Routing . Select the required Media Routing PIM and click OK . Enable the PIM and enter its peripheral name. In Peripheral ID , enter the Peripheral ID of the applicable peripheral. Do not enter the Logical Controller ID. In Application Hostname (1) , enter the hostname or IP address of the Cloud Connect publisher. In Application Connection Port (1) , enter the application port. The default port is 38001 . In Application Hostname (2) , enter the hostname or IP address of the Cloud Connect subscriber. In Application Connection Port (2) , enter 38001 . Leave these fields empty only when a secondary Cloud Connect server is not deployed. Set the heartbeat interval to 5 seconds and the reconnect interval to 10 seconds. Enable the secure connection and click OK . For complete field descriptions, see
                                       Add PIMs to the Media Routing Peripheral Gateway
                                       of the Optional Configurations chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) . |
| 4 | Create unique MRDs and associate them with application paths. | Create a unique media routing domain for each ECE channel, such as chat and email, and map the MRD to the ECE instance. For each Agent PG, create an ECE application path and add all ECE MRD-peripheral combinations that apply to the Agent PG.
                                       The application path can carry inbound email, outbound email, chat, callback, and delayed-callback activities. Use the Media Routing Domain List tool to create the MRDs. For more information, see
                                       Add and Maintain Media Routing Domains
                                       of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) . | Create unique MRDs for the Webex Connect digital channels that require separate reporting or queue behavior. You can also
                                       map multiple Webex Connect-powered channels under a single MRD if your deployment does not require channel-specific routing
                                       behavior. For more information, see
                                       Add and Maintain Media Routing Domains
                                       of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) . If you create the MRD in Packaged CCE Administration, it is automatically associated with the system-defined application path
                                       whose name ends in UQ.Desktop . If you create the MRD using Configuration Manager, manually associate it with the system-defined application path in List Tools > Application Path List Box > Attributes . For more information, see
                                       Set up Media Channels
                                       of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) . |
| 5 | Create skill groups and assign agents. | Create skill groups or precision queues for the applicable nonvoice MRDs. Ensure that each agent belongs to a skill group
                                       associated with the nonvoice MRD that is linked to the required application path. For more information, see
                                       Add and Maintain Skill Groups
                                       and
                                       Add and Maintain Precision Queues
                                       of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) . |
| 6 | Configure SSO and agent synchronization. | Enable Agent SSO in ECE. For ECE configuration guidance, see the Enterprise Chat and Email administration documentation . | In Packaged CCE Administration, configure Digital Channels > Digital Channel Settings > User Sync . Enter the load-balancer or reverse-proxy FQDN in Network Entry Point , enter the primary and secondary AW database connection details, test the primary connection, enable failover to the secondary
                                       AW, enable scheduled synchronization or use Sync Now , review the last-sync status and agent synchronization details, and save the configuration. Disable User Sync before rebuilding an AW database. Re-enable it only after the AW database has synchronized with the central
                                       controller database. For more information, see Configure User Sync of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) . |
| 7 | Configure ECC variables for Digital Routing. | Configure the ECE ECC variables required for chat, inbound email, outbound email, callback, and delayed-callback activities.
                                       For chat, inbound email, and outbound email, configure user.ece.activity.id . For callback and delayed-callback activities, configure user.ece.activity.id and user.ece.customer.name . For more information, see Configuring Expanded Call Context (ECC) Variables of the Prepare Packaged CCE for the Integration chapter in Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise, Release 15.0(1) . | In Packaged CCE Administration, navigate to Overview > Digital Channels > Digital Channel Settings > ECC Variable . Select and save user_DR_Primary , user_DR_Backup , and user_DR_MediaResourceID as mandatory variables, and user_DR_CustomerName and user_DR_MediaChannelName as optional variables. For the complete procedure and the required variables, see Define ECC variables of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) . |
| 8 | Integrate Cloud Connect with Webex Connect. |  | In Digital Channels > Digital Channel Settings > Integration , configure the OAuth2 client ID, client secret, token-request URL, POST method, application/x-www-form-urlencoded content type, and access_token JSON path. In Webex Connect, open the CCE prebuilt integration and copy its inbound Webhook URL. Paste this URL into the Webhook configuration in Packaged CCE Administration and save the integration. For more information, see Integrate Cloud Connect with Webex Connect of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) . |
| 9 | Add the ECE and Webex Connect Digital Channels gadgets to the Cisco Finesse desktop layout. | Add the ECE gadget to the applicable Finesse desktop layout. For more information, see Configuring Finesse of the Prepare Packaged CCE for the Integration chapter in Enterprise Chat and Email Installation and Configuration Guide for Packaged Contact Center Enterprise, Release 15.0(1) . For information about using the ECE gadgets, see the Enterprise Chat and Email User Guide for Agents and Supervisors . | Add the Manage Digital Channels gadget to the applicable Finesse desktop layout. Agents can then work on ECE and Webex Connect
                                       tasks from the same Finesse desktop. If ECE and Webex Connect use the same keyboard shortcut, Finesse reports a shortcut conflict and disables the key combination
                                       until the conflict is resolved. Adjust or disable conflicting shortcuts in the Finesse system settings. For more information, see Add Manage Digital Channels gadget of the Manage Desktop Layouts chapter in Cisco Finesse Administration Guide . For more information, see Manage Desktop Layouts of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) . |
| 10 | Optionally, configure workflows, rules, or events. | Configure workflows in Cisco Finesse. For more information, see Manage Workflows in the Cisco Finesse Administration Guide . | Configure workflows in Cisco Finesse, or configure rules and events in Webex Engage. Rules and events in Webex Engage provide
                                       similar functionality as workflows in Cisco Finesse. For more information, see Manage Workflows of the Packaged CCE Administration chapter in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) . For Webex Engage rules and events, see the Events and Rules topic in the Administration and Setup Guide for Webex Engage with Cisco Contact Center Enterprise . |
| 11 | Verify reporting. | Verify that CUIC reports display agent and queue activity for the ECE MRDs. Use ECE reporting applications for platform-specific
                                       interaction details. For ECE historical reporting, see the Enterprise Chat and Email Administrator's Guide to Reports Console . For CUIC reporting, see the Cisco Unified Intelligence Center User Guide . | Verify that CUIC reports display agent and queue activity for the Webex Connect MRDs. Use Webex Connect reports for platform-specific
                                       message and interaction details. For more information, see Reporting of the Digital Channels Integration Using Webex Connect chapter in Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) . |

| Note | This feature would enable Notifications for new activities like chat or email, not for subsequent updates on an existing conversation. |
|---|---|

| Scenario/Action | ECE Digital Channels | Webex Connect Digital Channels |
|---|---|---|
| Agent Login/Logout |
| Agent Login | Prior to ES03 on ECE 12.6(1) or later, agents log into ECE automatically when they log into the Finesse Desktop. After applying the ES, agents log into
                                       Finesse Desktop and then log into ECE by clicking " Manage Chat and Email Gadget ." | Agents log into the Finesse Desktop and then click on " Manage Digital Channels ". They are then prompted to sign in, and once they do, they log in to the Digital Channels gadget. |
| Agent logs into the gadgets on multiple browsers. | Finesse Desktop can show a random SSO "Login Error" message if the agent logs into the ECE gadget on multiple browsers. | Digital Channel Gadgets work as expected. |
| Browser is closed or the system is shut down | The agents are logged out of all gadgets. | The agent remains active. |
| Default user sign-out option is set to Sign out from Voice Channel . | ECE will log out of Chat MRD in 120 seconds, while the agent's ready state may be preserved for a little longer in an Email
                                       MRD before logging out. | Agent state remains ready in Digital Channels. |
| Agent closes the browser and logs in again within 60 seconds. | The agent state is not retained and they must log in again. | Agent state is retained. |
| Agent closes the browser and logs in again within 120 seconds. | The agent will be logged out. | The agent will be logged out. |
| Agent Logout | Log out of the ECE gadget. | Logout of Finesse Desktop to logout of the Digital Channels gadget. |
| Display/UX in Finesse Desktop |
| Display of the Finesse Digital Channel State Control (FNC) icons | ECE and Digital Channels are very similar, making it difficult to tell them apart. |
| Availability of the FNC icons | Prior to ES10 on ECE 12.6(1) , icons appear when agents log into the Finesse Desktop. Post the ES application, icons appear after agents click on the " Manage ECE Gadget ". | The icons appear after the agent clicks on Manage Digital Channels and then signs in again when prompted. |
| Handling Tasks |
| Task Transfer | Agent can transfer tasks to a queue or to an other agent. | Agent can transfer tasks to a queue only. |
| Task Offer | All tasks are automatically accepted. | Tasks are displayed as a pop-up dialog box in Finesse Desktop and must be accepted to begin. |
| Auto-pushback task | Auto-push back is supported when agent does not start the task within the configured time. | Auto-push back is not supported. |
| Task Interrupt/Timeout |
| Initiate the necessary Finesse workflow when a task is interrupted. | The Finesse workflow is not initiated as the Interrupt is not accepted. | Digital Channel gadget works as expected. |
| AgentState-13 (Interrupted) needs to be displayed on Agent_Real_Time when an agent is interrupted. | ECE works as expected. | AgentState-13 (Interrupted) is not being displayed on Agent_Real_Time when an agent working on Digital Channel Chat is interrupted. |
| RONA (Redirection on No Answer (RONA) | The task is redirected back to the queue after the agent fails to start the task within a specified time. | The task is redirected back to the queue after the agent fails to answer. |
| Workflows/Rules and Events |
| Applying a workflow to specific teams. | The workflow can be applied to a specific team or multiple teams. | All Rules and Events will apply to the one available team: the default team. |
| Applicable trigger points for the workflows or rules and events | You can create workflows for any of the trigger options listed in the When to Perform Actions drop-down in the Add Workflow gadget in Cisco Finesse. | Workflows can only be created for some of the trigger options available in the Fire When drop-down in the Events and Rules page in Webex Engage. For more information on supported options, see the Add a New Rule
                                       section in the Administration and Setup Guide for Webex Engage with Cisco Contact Center Enterprise . |
| Others |
| Conflicting keyboard shortcuts | If shortcuts of ECE and Digital Channels gadget conflict and you install Finesse 12.6(2) ES 05 , the shortcut will work on the gadget that is currently active (open in the active tab). For example, the default shortcut
                                       key Ctrl + Shift + 4 activates the Ready for Email state on whichever gadget (ECE or Digital Channel) is currently active. If the ECE gadget is
                                       active, the ECE's Email channel transitions to the Ready state. Similarly, if the Digital Channel gadget is open, the Digital
                                       Channel's Email channel transitions to the Ready state. If there are conflicts between the ECE shortcuts and Digital Channels gadget before installing the patch, you might encounter
                                       keyboard conflict errors and the shortcut keys will not work as expected. |
| Inactive gadget pause during Gadget Switch | The ECE gadget does not automatically pause and stays active. | Digital Channel gadget pauses as expected. |
| Failover and failback of gadgets | At times, failover and failback of the ECE server may not work seamlessly. | Digital Channel gadgets failover and failback as expected. |

## Figuras

![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)