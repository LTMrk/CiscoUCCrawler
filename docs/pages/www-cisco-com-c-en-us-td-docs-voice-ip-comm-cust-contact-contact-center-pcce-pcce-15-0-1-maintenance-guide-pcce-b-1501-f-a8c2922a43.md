---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-maintenance-guide-pcce-b-1501-f-a8c2922a43
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/maintenance/guide/pcce_b_1501_features-guide/pcce_m_1501_ece-webex-connect-co-deployment.html
retrieved_at: 2026-08-21T12:10:38.214253+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: ECE and Webex Connect Co-deployment in Packaged CCE

## Chapter: ECE and Webex Connect Co-deployment in Packaged CCE

# ECE and Webex Connect Co-deployment in Packaged CCE

## Overview

CCE customers have been using ECE for digital channels (Chat and Email) for an extended period. With the introduction of Digital
                           Channels Integration using Webex Connect in 12.6(2), a wide variety of communication channels such as SMS, Email, Facebook
                           Messenger, and Whatsapp were made available.

CCE now empowers customers to deploy both Webex Connect and ECE on a single Packaged CCE instance, allowing Contact Center
                           agents to independently leverage digital channels from both platforms.

This feature will significantly improve the agent's experience, ensuring a seamless, cohesive, and uninterrupted workflow.
                           Consequently, customer support across digital channels will be greatly enhanced.

## Prerequisites

Before you configure ECE and Webex Connect in the same Packaged CCE deployment, meet the following requirements:

Configure ECE and Webex Connect individually.

Use Packaged CCE, Cloud Connect, ECE, and Cisco Finesse Release 15.0(1). This feature does not require a feature-specific
                                 Engineering Special or Service Update.

Enable Single Sign-On (SSO) for agents in both Packaged CCE and ECE. The Manage Digital Channels gadget authenticates with
                                 Webex Engage in SSO mode.

Create separate Media Routing Domains (MRDs) for ECE and Webex Connect. The two integrations cannot share an MRD.

Ensure that agents belong to the skill groups associated with the applicable nonvoice MRDs.

Ensure that the Cloud Connect publisher is reachable. The DataConn service that synchronizes agents is active only on the
                                 publisher.

Obtain administrator access to Packaged CCE Administration, Configuration Manager, Cloud Connect, ECE, Webex Connect, Webex
                                 Engage, and Cisco Finesse.

This feature was qualified in the PCCE 2000-agent reference design. Confirm support for other Packaged CCE reference designs
                           in the applicable solution-design documentation before deployment.

## Workflow for Configuring ECE and Webex Connect Co-deployment

Step

Task

ECE Digital Channels

Webex Connect Digital Channels

1

Review the Packaged CCE objects that are created automatically.

Packaged CCE creates the DigitalRouting peripheral, the DigitalRouting routing client, the membership that associates the existing Agent_Targeting_Rule with the DigitalRouting routing client, and the Media Routing Peripheral Gateway (MR PG).

You must configure the Media Routing PIMs, establish certificate trust, add Cloud Connect to the Packaged CCE inventory, associate
                                       the ECE and Webex Connect media routing domains with their application paths, synchronize agents and ECC variables, configure
                                       the Webex Connect integration, and enable both gadgets in the Finesse desktop layout.

2

Establish certificate trust.

Export the platform certificate from both the Cloud Connect publisher and subscriber. On the MR PG, install each Cloud Connect
                                       certificate in the Personal certificate store and restart the MR PG.

Export or generate the MR PG certificate. RSA certificates are stored under <install_drive>:\icm\ssl\rsa ; ECDSA certificates are stored under <install_drive>:\icm\ssl\ecdsa . Import the MR PG certificate into the Cloud Connect publisher. Cloud Connect replicates it to the subscriber.

Restart the Digital Routing service on Cloud Connect:

```
utils cloudconnect stop digitalrouting
utils cloudconnect start digitalrouting
```

Also import the Cloud Connect publisher and subscriber certificates into the AW truststore. Restart Apache Tomcat after importing
                                       the certificates.

For certificate exchange procedures, see Certificate management for digital channels interaction in the Security Guide for Cisco Unified Contact Center Enterprise .

3

Add Cloud Connect to the Packaged CCE inventory.

In Packaged CCE Administration, go to Overview > Inventory . Click New , enter the publisher and subscriber details for Cloud Connect, and save the inventory configuration.

For the deployment-specific procedure, see Configure Cloud Connect for 2000 Agent Deployment or Configure Cloud Connect for 4000/12000 Agent Deployment in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide .

4

Configure the Media Routing PIMs.

The MR PG is created automatically in Packaged CCE, but you must configure its PIMs.

In the Peripheral Gateway Component Properties window, click Add . From Client Type , select Media Routing . Select the required Media Routing PIM and click OK .

Enable the PIM and enter its peripheral name. In Peripheral ID , enter the logical controller ID of the applicable peripheral. The database names include Multichannel for ECE and DigitalRouting for Webex Connect.

In Application Hostname (1) , enter the hostname or IP address of the media-routing services server. In Application Connection Port (1) , enter the application port. The default port is 38001 .

Leave the secondary application hostname and port empty unless your deployment requires them. Set the heartbeat interval to 5 seconds and the reconnect interval to 10 seconds. Enable the secure connection and click OK .

For the complete field descriptions, see Add PIMs to the Media Routing Peripheral Gateway in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide .

5

Create unique MRDs and associate them with application paths.

Create a unique media routing domain for each ECE channel, such as chat and email, and map the MRD to the ECE instance.

For each Agent PG, create an ECE application path and add all ECE MRD-peripheral combinations that apply to the Agent PG.
                                       The application path can carry inbound email, outbound email, chat, callback, and delayed-callback activities.

Use the Media Routing Domain List tool to create the MRDs. For field-level instructions, open Configuration Manager, navigate
                                       to List Tools > Media Routing Domain List > Media Routing Domain List Box > Attributes Tab (Media Routing Domain) , and press F1 to open the integrated help.

Create unique MRDs for the Webex Connect digital channels that require separate reporting or queue behavior. You can also
                                       map multiple Webex Connect-powered channels under a single MRD if your deployment does not require channel-specific routing
                                       behavior.

Associate the Webex Connect MRDs with the system-defined application path whose name ends in UQ.Desktop . This application path identifies Cisco Finesse as a client of the Agent PG and controls agent states for Webex Connect digital
                                       channels.

For MRD creation in Packaged CCE Administration, see Add and Maintain Media Routing Domains . To map the MRD to a Webex Connect channel, see Set up Media Channels in the Cisco Packaged Contact Center Enterprise Features Guide .

If you use Configuration Manager to create the MRD, associate it with the system-defined application path in List Tools > Application Path List Box > Attributes tab . Press F1 to open the integrated help for the selected field.

6

Create skill groups and assign agents.

Create skill groups or precision queues for the applicable nonvoice MRDs. Ensure that each agent belongs to a skill group
                                       associated with the nonvoice MRD that is linked to the required application path.

For Packaged CCE procedures, see Add and Maintain Skill Groups and Precision Queues . For Configuration Manager field-level help, open Explorer Tools Features > Skill Group Explorer and press F1 .

7

Configure SSO and agent synchronization.

Enable Agent SSO in ECE.

For ECE configuration guidance, see the Enterprise Chat and Email administration documentation .

In Packaged CCE Administration, configure Digital Channels > Digital Channel Settings > User Sync . Enter the load-balancer or reverse-proxy FQDN in Network Entry Point , enter the primary and secondary AW database connection details, test the primary connection, enable failover to the secondary
                                       AW, enable scheduled synchronization or use Sync Now , review the last-sync status and agent synchronization details, and save the configuration.

Disable User Sync before rebuilding an AW database. Re-enable it only after the AW database has synchronized with the central
                                       controller database.

For the complete procedure, see Configure User Sync in the Cisco Packaged Contact Center Enterprise Features Guide .

8

Select ECC variables for DRAPI.

In Packaged CCE Administration, open Digital Channels > Digital Channel Settings > ECC Variable . Add the required non-built-in ECC variables and save the configuration. The selected variables are synchronized to DRAPI.

For the complete procedure and the required variables, see Define ECC variables in the Cisco Packaged Contact Center Enterprise Features Guide .

9

Integrate Cloud Connect with Webex Connect.

In Digital Channels > Digital Channel Settings > Integration , configure the OAuth2 client ID, client secret, token-request URL, POST method, application/x-www-form-urlencoded content type, and access_token JSON path.

In Webex Connect, open the CCE prebuilt integration and copy its inbound Webhook URL. Paste this URL into the Webhook configuration in Packaged CCE Administration and save the integration.

For the complete procedure, see Integrate Cloud Connect with Webex Connect in the Cisco Packaged Contact Center Enterprise Features Guide .

10

Add the ECE and Webex Connect Digital Channels gadgets to the Cisco Finesse desktop layout.

Add the ECE gadget to the applicable Finesse desktop layout.

For details, see the Configuring Finesse topic in the Post-Installation Tasks chapter of the Enterprise Chat and Email Installation and Configuration Guide .

For information about using the ECE gadgets, see the Enterprise Chat and Email User Guide for Agents and Supervisors .

Add the Manage Digital Channels gadget to the applicable Finesse desktop layout. Agents can then work on ECE and Webex Connect
                                       tasks from the same Finesse desktop.

If ECE and Webex Connect use the same keyboard shortcut, Finesse reports a shortcut conflict and disables the key combination
                                       until the conflict is resolved. Adjust or disable conflicting shortcuts in the Finesse system settings.

For the gadget procedure, see Add Manage Digital Channels gadget in the Cisco Finesse Administration Guide . For the Packaged CCE desktop-layout procedure, see Manage Desktop Layouts .

11

Optionally, configure workflows, rules, or events.

Configure workflows in Cisco Finesse.

For more information, see Manage Workflows in the Cisco Finesse Administration Guide .

Configure workflows in Cisco Finesse, or configure rules and events in Webex Engage. Rules and events in Webex Engage provide
                                       similar functionality as workflows in Cisco Finesse.

For the Packaged CCE workflow procedure, see Manage Workflows . For Webex Engage rules and events, see the Events and Rules topic in the Administration and Setup Guide for Webex Engage with Cisco Contact Center Enterprise .

You can also refer to Example of Webex Connect Flow . This topic explains how to set up a Flow for a Call Survey that can be embedded in a chat channel. The Flow is designed
                                       within Webex Connect and uses an Event created in Webex Engage.

12

Verify reporting.

Verify that CUIC reports display agent and queue activity for the ECE MRDs. Use ECE reporting applications for platform-specific
                                       interaction details.

For ECE historical reporting, see the Enterprise Chat and Email Administrator's Guide to Reports Console . For CUIC reporting, see the Cisco Unified Intelligence Center User Guide .

Verify that CUIC reports display agent and queue activity for the Webex Connect MRDs. Use Webex Connect reports for platform-specific
                                       message and interaction details.

For the supported report types and stock templates, see Reporting in the Cisco Packaged Contact Center Enterprise Features Guide .

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

## Example of Webex Connect Flow

This section explains how to set up a Flow for a Call Survey that can be embedded in a chat channel. The Flow is designed
                              within Webex Connect and uses an Event created in Webex Engage.

The following example illustrates how Webex Engage and Webex Connect can be used to establish a call survey, and it should
                                          be regarded as a reference rather than a comprehensive guide. When creating a flow in your deployment, you will need to make
                                          adjustments based on your specific business requirements and system environment.

Step 1

In Webex Connect, create a new Webhook URL to start a Webex Connect Flow that triggers a survey right after a call ends.

Log into Webex Connect.

On the left pane, select Services.

On the Services page, choose the required service.

From the left sidebar, click on Assets , and then select Integrations from the displayed menu.

On the Integrations page, click Add Integration , and then select Inbound Webhook from the displayed menu.

On the Configure New Integration - Inbound Webhook dialog, the Webhook URL is displayed by default. This URL triggers the Call Survey Event that you will create in the upcoming
                                             steps. Enter a unique name in the Webhook name field.

Click the copy icon to copy the Webhook URL to your clipboard.

Click Save .

The new Inbound Webhook is created and displayed on the Integrations page.

Step 2

In Webex Engage, create a new event.

Log into Webex Engage.

From the left sidebar, select Groups .

From the list of groups, select your group.

Webex Engage displays its only team: the default team. Click on Default to access it.

Go to the Events and Rules tab and click Add new event .

In the Configure Events section, enter the following:

Name —Enter a unique name for the new event.

Method —Choose POST.

URL —Paste the Webhook URL you copied in the previous step (1 g).

Expected Response Format —Choose JSON.

Add Param —Include the variables you want in your flow. Useful options are shown in the following screenshot.

Click Save changes .

Step 3

In Webex Connect, create the Flow for the Call Survey.

From the left sidebar, select Services .

On the Services page, choose the required service.

Select the Flows tab and then click Create Flow in the upper-right corner.

On the Create Flow dialog, enter the following:

Flow Name — Enter a name for the new Flow.

Type — Select Work Flow .

Method — Choose New Flow .

Click Start from Scratch .

Click Create .

On the Select Trigger Category dialog, select Webhook .

Webex Connect displays the Flow Builder canvas with the Webhook node. The Configure Webhook page opens, enabling you to configure the Webhook node. Alternatively, you can access this page by double-clicking the node
                                                in the Flow Builder.

To configure the Webhook node:

On the Configuration tab, keep the default selection of the Select existing webhook radio button. From the Webhook Name field, select the Webhook you created earlier.

On the Transition Actions (optional) tab, add the necessary variables for your flow as shown in the below screenshot, then click Save . You can also include the custom variables created in Webex Engage during step 2 by selecting Add Params . Additionally, you have the option to add default variables like 'n2.chatid' that are readily available in Webex Engage.
                                                      Ensure that the variables you enter in Webex Connect match exactly with those in Webex Engage. For more information, see Transition Actions .

Add the Evaluate node if your business logic needs it.

Drag the Live Chat or In-App Messaging node onto the Flow builder canvas. Double-click the node, enter the following,:

Destination Type — Set to UserId

Destination — Set to $(CustomerID).

Thread ID — Enter $(ChatThreadVariable). This entry makes sure the Call Survey form is sent to the correct chat thread.

Set Message Type to Form, the Content Type to STATIC , and set Form Template to an existing Call Survey form.

Click Save .

Drag the Receive node onto the Flow builder canvas. Double-click the node and enter the following:

Form(threadId) —Enter $(ChatThreadVariable). This entry makes sure the Call Survey form is sent to the correct chat thread.

Form(userId) —Set to $(CustomerId).

Set Event Name to Form Response, the Content Type to STATIC , and Form Template to an existing Call Survey form.

Click Save .

In the Transition Actions (Optional) tab, you can opt to generate logs when the flow exits this node by adding a logID, as shown below.

Drag the Append Conversation node onto the Flow builder canvas. Double-click the node and enter the following:

Method Name — Choose Append Chat.

Node Authentication —Choose WxmTestEngage.

Channel — Choose Livechat.

Conversation ID —Enter $(ConversationId).

Step 4

Complete your Flow by creating connections between the various nodes within the canvas, as illustrated below.

| Step | Task | ECE Digital Channels | Webex Connect Digital Channels |
|---|---|---|---|
| 1 | Review the Packaged CCE objects that are created automatically. | Packaged CCE creates the DigitalRouting peripheral, the DigitalRouting routing client, the membership that associates the existing Agent_Targeting_Rule with the DigitalRouting routing client, and the Media Routing Peripheral Gateway (MR PG). You must configure the Media Routing PIMs, establish certificate trust, add Cloud Connect to the Packaged CCE inventory, associate
                                       the ECE and Webex Connect media routing domains with their application paths, synchronize agents and ECC variables, configure
                                       the Webex Connect integration, and enable both gadgets in the Finesse desktop layout. |
| 2 | Establish certificate trust. | Export the platform certificate from both the Cloud Connect publisher and subscriber. On the MR PG, install each Cloud Connect
                                       certificate in the Personal certificate store and restart the MR PG. Export or generate the MR PG certificate. RSA certificates are stored under <install_drive>:\icm\ssl\rsa ; ECDSA certificates are stored under <install_drive>:\icm\ssl\ecdsa . Import the MR PG certificate into the Cloud Connect publisher. Cloud Connect replicates it to the subscriber. Restart the Digital Routing service on Cloud Connect: utils cloudconnect stop digitalrouting
utils cloudconnect start digitalrouting Also import the Cloud Connect publisher and subscriber certificates into the AW truststore. Restart Apache Tomcat after importing
                                       the certificates. For certificate exchange procedures, see Certificate management for digital channels interaction in the Security Guide for Cisco Unified Contact Center Enterprise . |
| 3 | Add Cloud Connect to the Packaged CCE inventory. | In Packaged CCE Administration, go to Overview > Inventory . Click New , enter the publisher and subscriber details for Cloud Connect, and save the inventory configuration. For the deployment-specific procedure, see Configure Cloud Connect for 2000 Agent Deployment or Configure Cloud Connect for 4000/12000 Agent Deployment in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide . |
| 4 | Configure the Media Routing PIMs. | The MR PG is created automatically in Packaged CCE, but you must configure its PIMs. In the Peripheral Gateway Component Properties window, click Add . From Client Type , select Media Routing . Select the required Media Routing PIM and click OK . Enable the PIM and enter its peripheral name. In Peripheral ID , enter the logical controller ID of the applicable peripheral. The database names include Multichannel for ECE and DigitalRouting for Webex Connect. In Application Hostname (1) , enter the hostname or IP address of the media-routing services server. In Application Connection Port (1) , enter the application port. The default port is 38001 . Leave the secondary application hostname and port empty unless your deployment requires them. Set the heartbeat interval to 5 seconds and the reconnect interval to 10 seconds. Enable the secure connection and click OK . For the complete field descriptions, see Add PIMs to the Media Routing Peripheral Gateway in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide . |
| 5 | Create unique MRDs and associate them with application paths. | Create a unique media routing domain for each ECE channel, such as chat and email, and map the MRD to the ECE instance. For each Agent PG, create an ECE application path and add all ECE MRD-peripheral combinations that apply to the Agent PG.
                                       The application path can carry inbound email, outbound email, chat, callback, and delayed-callback activities. Use the Media Routing Domain List tool to create the MRDs. For field-level instructions, open Configuration Manager, navigate
                                       to List Tools > Media Routing Domain List > Media Routing Domain List Box > Attributes Tab (Media Routing Domain) , and press F1 to open the integrated help. | Create unique MRDs for the Webex Connect digital channels that require separate reporting or queue behavior. You can also
                                       map multiple Webex Connect-powered channels under a single MRD if your deployment does not require channel-specific routing
                                       behavior. Associate the Webex Connect MRDs with the system-defined application path whose name ends in UQ.Desktop . This application path identifies Cisco Finesse as a client of the Agent PG and controls agent states for Webex Connect digital
                                       channels. For MRD creation in Packaged CCE Administration, see Add and Maintain Media Routing Domains . To map the MRD to a Webex Connect channel, see Set up Media Channels in the Cisco Packaged Contact Center Enterprise Features Guide . If you use Configuration Manager to create the MRD, associate it with the system-defined application path in List Tools > Application Path List Box > Attributes tab . Press F1 to open the integrated help for the selected field. |
| 6 | Create skill groups and assign agents. | Create skill groups or precision queues for the applicable nonvoice MRDs. Ensure that each agent belongs to a skill group
                                       associated with the nonvoice MRD that is linked to the required application path. For Packaged CCE procedures, see Add and Maintain Skill Groups and Precision Queues . For Configuration Manager field-level help, open Explorer Tools Features > Skill Group Explorer and press F1 . |
| 7 | Configure SSO and agent synchronization. | Enable Agent SSO in ECE. For ECE configuration guidance, see the Enterprise Chat and Email administration documentation . | In Packaged CCE Administration, configure Digital Channels > Digital Channel Settings > User Sync . Enter the load-balancer or reverse-proxy FQDN in Network Entry Point , enter the primary and secondary AW database connection details, test the primary connection, enable failover to the secondary
                                       AW, enable scheduled synchronization or use Sync Now , review the last-sync status and agent synchronization details, and save the configuration. Disable User Sync before rebuilding an AW database. Re-enable it only after the AW database has synchronized with the central
                                       controller database. For the complete procedure, see Configure User Sync in the Cisco Packaged Contact Center Enterprise Features Guide . |
| 8 | Select ECC variables for DRAPI. | In Packaged CCE Administration, open Digital Channels > Digital Channel Settings > ECC Variable . Add the required non-built-in ECC variables and save the configuration. The selected variables are synchronized to DRAPI. For the complete procedure and the required variables, see Define ECC variables in the Cisco Packaged Contact Center Enterprise Features Guide . |
| 9 | Integrate Cloud Connect with Webex Connect. |  | In Digital Channels > Digital Channel Settings > Integration , configure the OAuth2 client ID, client secret, token-request URL, POST method, application/x-www-form-urlencoded content type, and access_token JSON path. In Webex Connect, open the CCE prebuilt integration and copy its inbound Webhook URL. Paste this URL into the Webhook configuration in Packaged CCE Administration and save the integration. For the complete procedure, see Integrate Cloud Connect with Webex Connect in the Cisco Packaged Contact Center Enterprise Features Guide . |
| 10 | Add the ECE and Webex Connect Digital Channels gadgets to the Cisco Finesse desktop layout. | Add the ECE gadget to the applicable Finesse desktop layout. For details, see the Configuring Finesse topic in the Post-Installation Tasks chapter of the Enterprise Chat and Email Installation and Configuration Guide . For information about using the ECE gadgets, see the Enterprise Chat and Email User Guide for Agents and Supervisors . | Add the Manage Digital Channels gadget to the applicable Finesse desktop layout. Agents can then work on ECE and Webex Connect
                                       tasks from the same Finesse desktop. If ECE and Webex Connect use the same keyboard shortcut, Finesse reports a shortcut conflict and disables the key combination
                                       until the conflict is resolved. Adjust or disable conflicting shortcuts in the Finesse system settings. For the gadget procedure, see Add Manage Digital Channels gadget in the Cisco Finesse Administration Guide . For the Packaged CCE desktop-layout procedure, see Manage Desktop Layouts . |
| 11 | Optionally, configure workflows, rules, or events. | Configure workflows in Cisco Finesse. For more information, see Manage Workflows in the Cisco Finesse Administration Guide . | Configure workflows in Cisco Finesse, or configure rules and events in Webex Engage. Rules and events in Webex Engage provide
                                       similar functionality as workflows in Cisco Finesse. For the Packaged CCE workflow procedure, see Manage Workflows . For Webex Engage rules and events, see the Events and Rules topic in the Administration and Setup Guide for Webex Engage with Cisco Contact Center Enterprise . You can also refer to Example of Webex Connect Flow . This topic explains how to set up a Flow for a Call Survey that can be embedded in a chat channel. The Flow is designed
                                       within Webex Connect and uses an Event created in Webex Engage. |
| 12 | Verify reporting. | Verify that CUIC reports display agent and queue activity for the ECE MRDs. Use ECE reporting applications for platform-specific
                                       interaction details. For ECE historical reporting, see the Enterprise Chat and Email Administrator's Guide to Reports Console . For CUIC reporting, see the Cisco Unified Intelligence Center User Guide . | Verify that CUIC reports display agent and queue activity for the Webex Connect MRDs. Use Webex Connect reports for platform-specific
                                       message and interaction details. For the supported report types and stock templates, see Reporting in the Cisco Packaged Contact Center Enterprise Features Guide . |

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

| Note | The following example illustrates how Webex Engage and Webex Connect can be used to establish a call survey, and it should
                                          be regarded as a reference rather than a comprehensive guide. When creating a flow in your deployment, you will need to make
                                          adjustments based on your specific business requirements and system environment. |
|---|---|

| Step 1 | In Webex Connect, create a new Webhook URL to start a Webex Connect Flow that triggers a survey right after a call ends. Log into Webex Connect. On the left pane, select Services. On the Services page, choose the required service. From the left sidebar, click on Assets , and then select Integrations from the displayed menu. On the Integrations page, click Add Integration , and then select Inbound Webhook from the displayed menu. On the Configure New Integration - Inbound Webhook dialog, the Webhook URL is displayed by default. This URL triggers the Call Survey Event that you will create in the upcoming
                                             steps. Enter a unique name in the Webhook name field. Click the copy icon to copy the Webhook URL to your clipboard. Click Save . The new Inbound Webhook is created and displayed on the Integrations page. |
|---|---|
| Step 2 | In Webex Engage, create a new event. Log into Webex Engage. From the left sidebar, select Groups . From the list of groups, select your group. Webex Engage displays its only team: the default team. Click on Default to access it. Go to the Events and Rules tab and click Add new event . In the Configure Events section, enter the following: Name —Enter a unique name for the new event. Method —Choose POST. URL —Paste the Webhook URL you copied in the previous step (1 g). Expected Response Format —Choose JSON. Add Param —Include the variables you want in your flow. Useful options are shown in the following screenshot. Click Save changes . For more information on adding parameters, see the Add a New Event section in the Administration and Setup Guide for Webex Engage with Cisco Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/wxengage_for_digital_channels/admin/guide/Administration_and_Setup_Guide_for_Webex_Engage_with_CCE.pdf . |
| Step 3 | In Webex Connect, create the Flow for the Call Survey. From the left sidebar, select Services . On the Services page, choose the required service. Select the Flows tab and then click Create Flow in the upper-right corner. On the Create Flow dialog, enter the following: Flow Name — Enter a name for the new Flow. Type — Select Work Flow . Method — Choose New Flow . Click Start from Scratch . Click Create . On the Select Trigger Category dialog, select Webhook . Webex Connect displays the Flow Builder canvas with the Webhook node. The Configure Webhook page opens, enabling you to configure the Webhook node. Alternatively, you can access this page by double-clicking the node
                                                in the Flow Builder. To configure the Webhook node: On the Configuration tab, keep the default selection of the Select existing webhook radio button. From the Webhook Name field, select the Webhook you created earlier. On the Transition Actions (optional) tab, add the necessary variables for your flow as shown in the below screenshot, then click Save . You can also include the custom variables created in Webex Engage during step 2 by selecting Add Params . Additionally, you have the option to add default variables like 'n2.chatid' that are readily available in Webex Engage.
                                                      Ensure that the variables you enter in Webex Connect match exactly with those in Webex Engage. For more information, see Transition Actions . Add the Evaluate node if your business logic needs it. Drag the Live Chat or In-App Messaging node onto the Flow builder canvas. Double-click the node, enter the following,: Destination Type — Set to UserId Destination — Set to $(CustomerID). Thread ID — Enter $(ChatThreadVariable). This entry makes sure the Call Survey form is sent to the correct chat thread. Set Message Type to Form, the Content Type to STATIC , and set Form Template to an existing Call Survey form. Click Save . Drag the Receive node onto the Flow builder canvas. Double-click the node and enter the following: Form(threadId) —Enter $(ChatThreadVariable). This entry makes sure the Call Survey form is sent to the correct chat thread. Form(userId) —Set to $(CustomerId). Set Event Name to Form Response, the Content Type to STATIC , and Form Template to an existing Call Survey form. Click Save . In the Transition Actions (Optional) tab, you can opt to generate logs when the flow exits this node by adding a logID, as shown below. Drag the Append Conversation node onto the Flow builder canvas. Double-click the node and enter the following: Method Name — Choose Append Chat. Node Authentication —Choose WxmTestEngage. Channel — Choose Livechat. Conversation ID —Enter $(ConversationId). |
| Step 4 | Complete your Flow by creating connections between the various nodes within the canvas, as illustrated below. |