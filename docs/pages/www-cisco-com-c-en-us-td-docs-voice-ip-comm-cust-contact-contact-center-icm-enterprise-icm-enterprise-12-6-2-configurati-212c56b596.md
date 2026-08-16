---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-212c56b596
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_features-guide-1262/rcct_m_agent-call-transcription_fg.html
retrieved_at: 2026-08-16T20:10:35.058273+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: April 30, 2025

Chapter: Call Transcription

## Chapter: Call Transcription

# Call Transcription

## Introduction

Unified CCE leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to provide services that assist agents. These
                           services are available for the agents in the Cisco Finesse desktop gadgets.

In the Transcript gadget, you can view in real-time, the voice conversation that was dynamically converted to text.

## Prerequisites

The prerequisites for configuring Call Transcription are:

Call Transcription feature requires CUBE platform software release version 17.12.3SMU or later versions (on all platforms,
                                 including vCUBE).

For more details on supported CUBE platforms and configuration, see the WebSocket-Based Media Forking for Cloud Speech Services
                                 chapter in the Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards at https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/websocket-forking-for-cube.html .

The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                             Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html .

The following components must be on release 12.6(2) : CCE components (Router, Logger, AW, and PG), Cisco Finesse, Cisco Unified CVP, and Cloud Connect.

Ensure that the Unified CCE AW, Unified CCE OAMP, Cloud Connect, CUBE, and Agent Desktop components have access to Webex services
                                             to use the Call Transcription.

## Important Considerations

Call Transcription is not supported for transferred or conferenced calls.

## Contact Center AI Services Task Flow

Follow this procedure to enable the Contact Center AI (CCAI) Services that equips your Contact Center for Call Transcription
                              Services.

Step 1

Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services.

Step 2

Ensure that the Cloud Connect publisher and subscriber are installed.

For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 3

Configure Cloud Connect in the CVP Operations Console (OAMP). For details see the section Configure CVP Devices for Cloud Connect in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 4

Register Cloud Connect in the Unified CCE Administration console to establish a secure and trusted communication channel between
                                       the Cisco Contact Center on-premises deployment and cloud services.

For details, see the Cloud Connect Integration section in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

Step 5

Import the Cloud Connect certificate to the CVP Server.

For details, see the section Import Cloud Connect Certificate to Unified CVP Keystore in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 6

In the Unified CCE Administration console, do the following with the CCAI configuration (created in step 1):

To view and sync the Contact Center AI configuration which is associated with all call types as a global configuration, see Associate Contact Center AI Configuration with All Call Types .

To view, update, or delete the Contact Center AI configuration associated with a specific call type, see Associate Contact Center AI Configuration with a Call Type .

Step 7

By default, the locale is set to English. To use languages other than English, in ICM Script Editor, set the user.microapp.locale variable to the language specified for your conversation profile. For example, set the value of the variable to "es-ES" for
                                       Spanish.

Step 8

Provision Cloud Connect on Cisco Finesse.

For more information, see the Cloud Connect Server Settings topic in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Step 9

To add the Call Transcript gadget to the Cisco Finesse desktop layout:

Enable the Call Transcript gadget in Cisco Finesse Administration.

For details, see the Manage Desktop Layout section in the Cisco Finesse Administration Guide .

Enable the Call Transcription service in Unified CCE Administration for an agent or multiple agents together.

For details, see Enable or Disable Contact Center AI Services for Agents .

Once enabled, the Call Transcript gadget appears on the Home tab. For details on how to use the gadget, see the Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise .

Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide .

Step 10

Perform the following steps to configure WebSocket-based forking in CUBE.

Create a SIP profile and associate it at the dial-peer level in CUBE. For details, see Create a SIP Profile at the Dial-Peer Level in CUBE .

Import the WebSocket Connector certificate to CUBE. For details, see Import or Verify WebSocket Connector Certificate to CUBE .

Configure WebSocket-based forking in CUBE. For details, see the WebSocket-Based Media Forking for Cloud Speech Services chapter in the Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards .

The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html .

## Enable or Disable Contact Center AI Services for Agents

Contact Center AI Services can be configured for each agent. Administrators and supervisors can enable or disable the services for an agent or multiple
                           agents together.

### Enable or Disable Contact Center AI Services for an Agent

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Click on the agent row whose services are to be modified.

Step 3

Click the Contact Center AI tab.

Step 4

To enable or disable the required Contact Center AI Services , check or uncheck the check boxes corresponding to the services.

Step 5

Click Save .

### Enable or Disable Contact Center AI Services for Multiple Agents

All agents must belong to the same site and the same department, or all agents must be global agents. The Edit button is disabled if:

Agents from different sites , departments, or peripheral sets are selected.

A mix of global and departmental agents are selected.

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Check the check box corresponding to each agent whose services you want to edit.

Step 3

Click Edit > Contact Center AI .

If the service is enabled for all the agents selected for editing, the check box is checked.

If the service is disabled for all the agents selected for editing, the check box is unchecked.

If the service is enabled for some agents and disabled for the others, the check box has a dash (—).

Step 4

To enable or disable the Contact Center AI Services , check or uncheck the check boxes corresponding to the services.

Step 5

Click Save , and then click Yes to confirm the changes.

### Enable or Disable Answers Contact Center AI Services for Agents using Bulk Job

Step 1

Navigate to Unified CCE Administration > Overview > Bulk Import .

Step 2

Click Templates .

The Download Templates popup window opens.

Step 3

Click the Download icon for the Contact Center AI template you want to use.

Step 4

Click OK to close the Download Templates popup window.

Step 5

Open the .csv template in Microsoft Excel.

Step 6

Populate the file as described in the Bulk Contact Center AI Services Content File .

Step 7

Save the populated file to the local machine.

Step 8

Navigate to Unified CCE Administration > Overview > Bulk Import .

Step 9

Click New .

Step 10

In the optional Description field, enter up to 255 characters to describe the bulk job.

Step 11

In the Content file field, choose the file to upload, and then click Save .

#### Bulk Contact Center AI Services Content File

The content file for Contact Center AI bulk job contains the fields given in the following table. Enter the values appropriately in the given fields to enable or
                                 disable Contact Center AI Services for the agents.

Field

Required?

Description

agentId

Agent ID or Username

Existing agentId for which you want to enable or disable the Contact Center AI Services .

You must provide either an agentId or the userName. If both are provided, agentId takes precedence over the userName. If the
                                             agentId value is left blank, the userName will reference an existing agent.

userName

Username of the agent for which you want to enable or disable the Contact Center AI Services .

If no agent is found with the given username, the Contact Center AI Services association fails.

agentServices

Yes (to enable Contact Center AI Services )

The type of Contact Center AI Services to be associated with the agent. Supported values are AgentAnswers and Transcript. To associate more than one services, seperate the values using semicolon (;).

If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                             with the agent.

| Note | The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                             Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . |
|---|---|

| Note | Ensure that the Unified CCE AW, Unified CCE OAMP, Cloud Connect, CUBE, and Agent Desktop components have access to Webex services
                                             to use the Call Transcription. |
|---|---|

| Step 1 | Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services. For details, see the Create a Contact Center AI Configuration article. |
|---|---|
| Step 2 | Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 3 | Configure Cloud Connect in the CVP Operations Console (OAMP). For details see the section Configure CVP Devices for Cloud Connect in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 4 | Register Cloud Connect in the Unified CCE Administration console to establish a secure and trusted communication channel between
                                       the Cisco Contact Center on-premises deployment and cloud services. For details, see the Cloud Connect Integration section in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
| Step 5 | Import the Cloud Connect certificate to the CVP Server. For details, see the section Import Cloud Connect Certificate to Unified CVP Keystore in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 6 | In the Unified CCE Administration console, do the following with the CCAI configuration (created in step 1): To view and sync the Contact Center AI configuration which is associated with all call types as a global configuration, see Associate Contact Center AI Configuration with All Call Types . To view, update, or delete the Contact Center AI configuration associated with a specific call type, see Associate Contact Center AI Configuration with a Call Type . |
| Step 7 | By default, the locale is set to English. To use languages other than English, in ICM Script Editor, set the user.microapp.locale variable to the language specified for your conversation profile. For example, set the value of the variable to "es-ES" for
                                       Spanish. |
| Step 8 | Provision Cloud Connect on Cisco Finesse. For more information, see the Cloud Connect Server Settings topic in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
| Step 9 | To add the Call Transcript gadget to the Cisco Finesse desktop layout: Enable the Call Transcript gadget in Cisco Finesse Administration. For details, see the Manage Desktop Layout section in the Cisco Finesse Administration Guide . Enable the Call Transcription service in Unified CCE Administration for an agent or multiple agents together. For details, see Enable or Disable Contact Center AI Services for Agents . Once enabled, the Call Transcript gadget appears on the Home tab. For details on how to use the gadget, see the Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise . Note Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide . | Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide . |
| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide . |
| Step 10 | Perform the following steps to configure WebSocket-based forking in CUBE. Create a SIP profile and associate it at the dial-peer level in CUBE. For details, see Create a SIP Profile at the Dial-Peer Level in CUBE . Import the WebSocket Connector certificate to CUBE. For details, see Import or Verify WebSocket Connector Certificate to CUBE . Configure WebSocket-based forking in CUBE. For details, see the WebSocket-Based Media Forking for Cloud Speech Services chapter in the Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards . CUBE uses a WebSocket connection to fork the media streams of the agent and the caller towards the Webex CCAI Orchestrator
                                       service. For more details, see the Contact Center AI Services Considerations section in the Solution Design Guide for Cisco Unified Contact Center Enterprise . Note The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . | Note | The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . |
| Note | The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . |

| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide . |
|---|---|

| Note | The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . |
|---|---|

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Click on the agent row whose services are to be modified. |
| Step 3 | Click the Contact Center AI tab. Displays a list of services enabled or disabled for the agent. |
| Step 4 | To enable or disable the required Contact Center AI Services , check or uncheck the check boxes corresponding to the services. |
| Step 5 | Click Save . |

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Check the check box corresponding to each agent whose services you want to edit. |
| Step 3 | Click Edit > Contact Center AI . The Edit Services dialog displays a list of services that are the service that is enabled or disabled. If the service is enabled for all the agents selected for editing, the check box is checked. If the service is disabled for all the agents selected for editing, the check box is unchecked. If the service is enabled for some agents and disabled for the others, the check box has a dash (—). |
| Step 4 | To enable or disable the Contact Center AI Services , check or uncheck the check boxes corresponding to the services. |
| Step 5 | Click Save , and then click Yes to confirm the changes. |

| Step 1 | Navigate to Unified CCE Administration > Overview > Bulk Import . |
|---|---|
| Step 2 | Click Templates . The Download Templates popup window opens. |
| Step 3 | Click the Download icon for the Contact Center AI template you want to use. |
| Step 4 | Click OK to close the Download Templates popup window. |
| Step 5 | Open the .csv template in Microsoft Excel. |
| Step 6 | Populate the file as described in the Bulk Contact Center AI Services Content File . |
| Step 7 | Save the populated file to the local machine. |
| Step 8 | Navigate to Unified CCE Administration > Overview > Bulk Import . |
| Step 9 | Click New . |
| Step 10 | In the optional Description field, enter up to 255 characters to describe the bulk job. |
| Step 11 | In the Content file field, choose the file to upload, and then click Save . |

| Note | Bulk job is available for administrators only when Cloud Connect is added in the inventory and registered on the Control Hub. |
|---|---|

| Field | Required? | Description |
|---|---|---|
| agentId | Agent ID or Username | Existing agentId for which you want to enable or disable the Contact Center AI Services . You must provide either an agentId or the userName. If both are provided, agentId takes precedence over the userName. If the
                                             agentId value is left blank, the userName will reference an existing agent. |
| userName | Username or Agent ID | Username of the agent for which you want to enable or disable the Contact Center AI Services . If no agent is found with the given username, the Contact Center AI Services association fails. |
| agentServices | Yes (to enable Contact Center AI Services ) | The type of Contact Center AI Services to be associated with the agent. Supported values are AgentAnswers and Transcript. To associate more than one services, seperate the values using semicolon (;). If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                             with the agent. |