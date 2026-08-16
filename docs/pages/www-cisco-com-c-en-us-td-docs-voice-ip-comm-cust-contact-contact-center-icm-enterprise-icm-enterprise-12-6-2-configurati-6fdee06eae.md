---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-6fdee06eae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_features-guide-1262/rcct_m_agent-answers_fg.html
retrieved_at: 2026-08-16T20:10:18.098115+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: April 30, 2025

Chapter: Agent Answers

## Chapter: Agent Answers

# Agent Answers

## Introduction

Unified CCE leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to provide services that assist agents. These
                           services are available for the agents in the Cisco Finesse desktop gadgets.

Agent Answers feature provides relevant suggestions and recommendations in real time for the agent to consider. The suggestions
                           and recommendations are based on the ongoing conversation between the caller and the agent.

More often than not, agents lack the depth of knowledge about the products and services of the business they serve. Agent
                           Answers enhances the customer experience because the timely suggestions improve the ability of the agent  to respond. Businesses
                           can cut down on training costs and time.

## Prerequisites

The prerequisites for configuring Agent Answers are:

The Agent Answers feature requires 17.12.3 or later version of the vCUBE Catalyst 8000V platform or ISRs 4431, 4451-X, or
                                 4461 CUBE platforms.

For more details on supported CUBE platforms and configuration, see the WebSocket-Based Media Forking for Cloud Speech Services
                                 chapter in the Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards at https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/websocket-forking-for-cube.html .

The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                             Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html .

The following components must be on release 12.6(2) : CCE components (Router, Logger, PG, and AW), Cisco Finesse, Cisco Unified CVP, and Cloud Connect.

Ensure that your Unified ICM AW server has 443/8443 ports opened and is able to access the following websites:

*.wbx2.com

*.ciscoccservice.com

Ensure that CUBE has access to the following websites:

*.cisco.com

*.ciscospark.com

*.rtmsprod.net

*.wbx2.com

Ensure that Unified CCE AW , Unified CCE OAMP, Cloud Connect, CUBE, and Agent Desktop components have access to Webex services to use the Agent Answers.

## Important Considerations

Consider the following before configuring the Agent Answers services:

Agent Answers services are supported on calls that originate from CVP routing clients. Calls originating from routing clients
                                 other than CVP or calls that are sent using the translation route to CVP do not support the Agent Answers services.

The following failover scenarios don’t support Agent Answers services:

CCE components running in maintenance modes switch to the peer side, passing the call context to the other side. If the call
                                       context (required to trigger the Agent Answers services) is lost, Agent Answers services may not work as expected.

Agent Answers services is supported during VRU PG failovers before and after the transfer. However, Agent Answers services
                                       aren’t supported when the transfer is in progress.

Agent Answers services aren’t supported during Agent PG failovers.

Agent Answers services aren’t supported in the following call scenarios:

Direct Extension calls

Outbound campaign calls and agent-initiated outbound calls.

Calls routed to agents on non-CUCM Peripheral Gateways such as the TDM PG and System PG

Transfer and conference calls

Agent Answers services are supported only with G.711 μ law.

A CUBE instance can support either WebSocket-based forking or Network-based Recording (NBR) forking. However, you cannot enable
                                 both types of forking on the same instance of CUBE.

## Contact Center AI Services Task Flow

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

To view and sync the Contact Center AI configuration which is associated with all call types as a global configuration.

To view, update, or delete the Contact Center AI configuration associated with a specific call type.

Step 7

Provision Cloud Connect on Cisco Finesse.

For more information, see the Cloud Connect Server Settings topic in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Step 8

Do the following in the Cisco Finesse Administration console.

To enable CCAI services in Cisco Finesse, see the AI Services Configuration section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

To add the Agent Answers gadget to the Cisco Finesse desktop layout, see the Contact Center AI Gadgets section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Once enabled, the Agent Answers gadget appears on the Home tab and displays relevant articles and suggestions during an incoming
                                          call. For details on how to use the gadget, see the Contact Center AI Gadgets Guide .

Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Step 9

To add the Agent Answers gadget to the Cisco Finesse desktop layout:

Enable the Agent Answers gadget in Cisco Finesse Administration.

For details, see the Manage Desktop Layout section in the Cisco Finesse Administration Guide .

Enable the Agent Answers service in Unified CCE Administration for an agent or multiple agents together.

Once enabled, the Agent Answers gadget appears on the Home tab and displays relevant articles and suggestions during an incoming
                                          call. For details on how to use the gadget, see the Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise .

Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide .

Step 10

Perform the following steps to configure WebSocket-based forking in CUBE.

Create a SIP profile and associate it at the dial-peer level in CUBE. For details, see Importing Cube Certificate .

Import the WebSocket Connector certificate to CUBE. For details, see Importing Cube Certificate .

Configure WebSocket-based forking in CUBE. For details, see the WebSocket-Based Media Forking for Cloud Speech Services chapter in the Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards .

CUBE uses a WebSocket connection to fork the media streams of the agent and the caller towards the Webex CCAI Orchestrator
                                          service. For more details, see the Contact Center AI Services Considerations section in the Solution Design Guide for Cisco Unified Contact Center Enterprise .

The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html .

Step 11

To use the regionalised media support, see the Regional Media Data Center Region Mapping section.

## Contact Center AI Configuration

In the Unified CCE Administration console, the Contact Center AI (CCAI) feature tab allows administrators to associate the
                           CCAI configuration (created in the Control Hub at https://admin.webex.com/ ) with all the call types (global configuration) or with a specific call type. Upon associating a CCAI configuration with
                           the call type, the global configuration (if any) gets overridden for the specific call type.

To access this feature, add Cloud Connect to the inventory and register it in the Unified CCE Administration console.

### Associate Contact Center AI Configuration with All Call Types

You can view, update, or reset the Contact Center AI configuration, which is associated with all call types.

#### View Contact Center AI Configuration

In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI . The Contact Center AI Configuration search box displays the name of the CCAI configuration that was previously associated with all call types.

#### Reset Contact Center AI Global Configuration

This procedure explains how to reset the Contact Center AI configuration. Upon reset, the previously associated configuration
                                    is cleared from the search box.

Step 1

In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI .

Step 2

In the Contact Center AI Configuration search box, next to the configuration name, click the x icon.

Step 3

Click Save .

### Associate Contact Center AI Configuration with a Call Type

You can view, update, or delete the Contact Center AI configuration associated with a specific call type.

#### View Contact Center AI Configuration

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Type . The Contact Center AI Configuration search box displays the name of the CCAI configuration that was previously associated with the call type.

#### Update Associate Contact Center AI Configuration

You can create a Call Type using the Configuration Manager tool . However, you can use the Unified CCE Administration to associate a Contact Center AI configuration with a call type. This procedure explains how to update the Contact Center AI configuration associated with a call type.

Only one configuration can be associated with a call type.

Step 1

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings .

Step 2

Click the Call Type tab and select the call type for which Contact Center AI configuration has to be associated.

Step 3

Click the Contact Center AI tab.

Step 4

In the Contact Center AI Configuration search box, click the search icon. A pop-up window displays a list of CCAI configurations.

Step 5

Select the required configuration and click Save .

#### Reset Contact Center AI Configuration

This procedure explains how to reset the Contact Center AI configuration. Upon reset, the previously associated configuration
                                    with the call type is cleared from the search box.

Step 1

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings .

Step 2

Click the Call Type tab.

Step 3

In the Contact Center AI Configuration search box, next to the configuration name, click the x icon.

Step 4

Click Save .

### Enable or Disable Contact Center AI Services for Agents

Contact Center AI Services can be configured for each agent. Administrators and supervisors can enable or disable the services for an agent or multiple
                              agents together.

#### Enable or Disable Contact Center AI Services for an Agent

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

#### Enable or Disable Contact Center AI Services for Multiple Agents

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

#### Enable or Disable Answers Contact Center AI Services for Agents using Bulk Job

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

##### Bulk Contact Center AI Services Content File

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

## Create a SIP Profile at the Dial-Peer Level in CUBE

Run the following CLI commands on the CUBE terminal to create a SIP profile and associate that profile at the dial-peer level.
                           These commands add a SIP header to the SIP profile configuration, allowing CVP to identify which CUBE device can receive the
                           forking request.

```
voice class sip-profiles <SIP-profile-identifier-a>
request INVITE sip-header Call-Info add "X-Cisco-Forking: supported"
dial-peer voice <SIP-profile-identifier-b> voip
voice-class sip profiles <SIP-profile-identifier-a>
```

Example:

```
voice class sip-profiles 104
request INVITE sip-header Call-Info add "X-Cisco-Forking: supported"
dial-peer voice 4445 voip
voice-class sip profiles 104
```

## Import or Verify WebSocket Connector Certificate to CUBE

Step 1

Run the command to verify if the certificate is included.

```
show crypto pki trustpool | include IdenTrust
cn=IdenTrust Commercial Root CA 1
o=IdenTrust Inc
cn=IdenTrust Commercial Root CA 1
o=IdenTrust Inc
```

Step 2

If IdenTrust certificates are not present, add the certificates to CUBE.

Open the following URL https://www.cisco.com/security/pki/ .

Locate the Cisco Trusted Core Root Bundle under the Trusted Root Stores .

Select the Cisco Trusted Core Root Bundle , right click, and then select Copy link . The URL for the bundle is copied to your clipboard.

Run the following command in CUBE terminal:

```
CUBE# configure terminal
CUBE(config)# crypto pki trustpool import clean URL <URL copied in step 2(c)>
```

Example:

```
CUBE(config)# crypto pki trustpool import clean URL http://www.cisco.com/security/pki/trs/ios_core.p7b
```

Output

```
Reading file from http://www.cisco.com/security/pki/trs/ios_core.p7b
Loading http://www.cisco.com/security/pki/trs/ios_core.p7b
% PEM files import succeeded.
```

The IndenTrust certificates are added to CUBE. To verify the addition, run the following command show crypto pki trustpool | include IdenTrust . The output will display the IdenTrust certificates as shown in Step 1.

## Reconfigure Agent Answers after Upgrade to Unified CCE 12.6

### Before you begin

Reporting : The Agent Answers Analytics report compares an agent's handle time when the Agent Answers service was enabled vs. when the
                                    service was disabled. The report helps you understand the impact of the Agent Answers services on an agent's performance.

Enable the CCAI Configuration for Specific Call Types : The CCAI Configuration can be enabled for all or specific call types.

Enable the CCAI Services for Specific Agents : The CCAI Services can be configured for each agent. Administrators and supervisors can enable or disable the services for
                                    an agent or multiple agents.

If you used the CCAI Services on Unified CCE 12.5, you've already completed most of the configurations that are required for the Agent Answers and Call Transcript services
                              to work in Unified CCE 12.6. No changes are required to the existing Google CCAI, CUBE, or Cloud Connect configurations.

While configuring the CCAI services in Unified CCE 12.5, you enabled Cisco Finesse 12.6 to display the CCAI gadgets to all the agents by running the enableCustomAgentServices CLI command.

Once you complete the agent configurations (at Step 3 in the following procedure) and run the enableCustomAgentServices CLI command to disable the gadgets for all the agents (at Step 4), Cisco Finesse relies on agent-specific configuration in
                              Unified CCE Administration to display the gadgets.

Follow these steps to complete the CCAI configuration in Unified CCE 12.6 and leverage the enhanced capabilities listed above:

Step 1

In Control Hub, set a CCAI configuration as the default configuration for all calls. For more details, see Step 7a at https://help.webex.com/en-us/npbt02j/Configure-Contact-Center-AI .

Step 2

In the Unified CCE Administration console, do one of the following:

To view and sync the Contact Center AI configuration that is associated with all call types as a global configuration, see Associate Contact Center AI Configuration with All Call Types .

To view, update, or delete the Contact Center AI configuration that is associated with a specific call type, see Associate Contact Center AI Configuration with a Call Type .

Step 3

In the Unified CCE Administration console, enable or disable CCAI Services for an agent or multiple agents.

Step 4

Undo these CCAI settings configured when Unified CCE was in 12.5:

Delete the "call.user.configid" ECC variable you created for the Answers feature and remove the association of this variable
                                                with the CCE script.

For more details, see the Contact Center AI Services Task Flow section in the Cisco Unified Contact Center Enterprise Features Guide, Release 12.5 at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

In Cisco Finesse, run the following CLI command to disable the CCAI services from all the Cisco Finesse clusters:

```
utils finesse set_property webservices enableCustomAgentServices false
```

For more details, see the AI Services Configuration topic in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

| Note | The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                             Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . |
|---|---|

| Step 1 | Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services. For details, see the Create a Contact Center AI Configuration article. |
|---|---|
| Step 2 | Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 3 | Configure Cloud Connect in the CVP Operations Console (OAMP). For details see the section Configure CVP Devices for Cloud Connect in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 4 | Register Cloud Connect in the Unified CCE Administration console to establish a secure and trusted communication channel between
                                       the Cisco Contact Center on-premises deployment and cloud services. For details, see the Cloud Connect Integration section in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html . |
| Step 5 | Import the Cloud Connect certificate to the CVP Server. For details, see the section Import Cloud Connect Certificate to Unified CVP Keystore in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 6 | In the Unified CCE Administration console, do the following with the CCAI configuration (created in step 1): To view and sync the Contact Center AI configuration which is associated with all call types as a global configuration. To view, update, or delete the Contact Center AI configuration associated with a specific call type. |
| Step 7 | Provision Cloud Connect on Cisco Finesse. For more information, see the Cloud Connect Server Settings topic in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
| Step 8 | Do the following in the Cisco Finesse Administration console. To enable CCAI services in Cisco Finesse, see the AI Services Configuration section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . To add the Agent Answers gadget to the Cisco Finesse desktop layout, see the Contact Center AI Gadgets section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . Once enabled, the Agent Answers gadget appears on the Home tab and displays relevant articles and suggestions during an incoming
                                          call. For details on how to use the gadget, see the Contact Center AI Gadgets Guide . Note Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . | Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
| Step 9 | To add the Agent Answers gadget to the Cisco Finesse desktop layout: Enable the Agent Answers gadget in Cisco Finesse Administration. For details, see the Manage Desktop Layout section in the Cisco Finesse Administration Guide . Enable the Agent Answers service in Unified CCE Administration for an agent or multiple agents together. Once enabled, the Agent Answers gadget appears on the Home tab and displays relevant articles and suggestions during an incoming
                                          call. For details on how to use the gadget, see the Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise . Note Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide . | Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide . |
| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide . |
| Step 10 | Perform the following steps to configure WebSocket-based forking in CUBE. Create a SIP profile and associate it at the dial-peer level in CUBE. For details, see Importing Cube Certificate . Import the WebSocket Connector certificate to CUBE. For details, see Importing Cube Certificate . Configure WebSocket-based forking in CUBE. For details, see the WebSocket-Based Media Forking for Cloud Speech Services chapter in the Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards . CUBE uses a WebSocket connection to fork the media streams of the agent and the caller towards the Webex CCAI Orchestrator
                                          service. For more details, see the Contact Center AI Services Considerations section in the Solution Design Guide for Cisco Unified Contact Center Enterprise . Note The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . | Note | The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . |
| Note | The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . |
| Step 11 | To use the regionalised media support, see the Regional Media Data Center Region Mapping section. |

| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
|---|---|

| Note | Gadget auto-hide/un-hide and notifications capability is available only if the gadget is configured as a multi-tab gadget
                                                      in Cisco Finesse. For more details, see Configure Multi-Tab Gadget Layout section in the Cisco Finesse Administration Guide . |
|---|---|

| Note | The WebSocket-based forking method has been deprecated. The Agent Answer feature will now be supported via a new forking mechanism.
                                                      Please transition to the new method to maintain support and functionality. For details and guidance, refer to https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/deprecation-notice-websocket-based-media-forking.html . |
|---|---|

| Note | To access this feature, add Cloud Connect to the inventory and register it in the Unified CCE Administration console. |
|---|---|

| Step 1 | In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI . |
|---|---|
| Step 2 | In the Contact Center AI Configuration search box, next to the configuration name, click the x icon. |
| Step 3 | Click Save . |

| Note | Only one configuration can be associated with a call type. |
|---|---|

| Step 1 | In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings . |
|---|---|
| Step 2 | Click the Call Type tab and select the call type for which Contact Center AI configuration has to be associated. |
| Step 3 | Click the Contact Center AI tab. |
| Step 4 | In the Contact Center AI Configuration search box, click the search icon. A pop-up window displays a list of CCAI configurations. |
| Step 5 | Select the required configuration and click Save . |

| Step 1 | In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings . |
|---|---|
| Step 2 | Click the Call Type tab. |
| Step 3 | In the Contact Center AI Configuration search box, next to the configuration name, click the x icon. |
| Step 4 | Click Save . |

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

| Step 1 | Run the command to verify if the certificate is included. show crypto pki trustpool \| include IdenTrust
cn=IdenTrust Commercial Root CA 1
o=IdenTrust Inc
cn=IdenTrust Commercial Root CA 1
o=IdenTrust Inc |
|---|---|---|
| Step 2 | If IdenTrust certificates are not present, add the certificates to CUBE. Open the following URL https://www.cisco.com/security/pki/ . Locate the Cisco Trusted Core Root Bundle under the Trusted Root Stores . Select the Cisco Trusted Core Root Bundle , right click, and then select Copy link . The URL for the bundle is copied to your clipboard. Run the following command in CUBE terminal: CUBE# configure terminal
CUBE(config)# crypto pki trustpool import clean URL <URL copied in step 2(c)> Example: CUBE(config)# crypto pki trustpool import clean URL http://www.cisco.com/security/pki/trs/ios_core.p7b Output Reading file from http://www.cisco.com/security/pki/trs/ios_core.p7b
Loading http://www.cisco.com/security/pki/trs/ios_core.p7b
% PEM files import succeeded. The IndenTrust certificates are added to CUBE. To verify the addition, run the following command show crypto pki trustpool \| include IdenTrust . The output will display the IdenTrust certificates as shown in Step 1. |

| Step 1 | In Control Hub, set a CCAI configuration as the default configuration for all calls. For more details, see Step 7a at https://help.webex.com/en-us/npbt02j/Configure-Contact-Center-AI . |
|---|---|
| Step 2 | In the Unified CCE Administration console, do one of the following: To view and sync the Contact Center AI configuration that is associated with all call types as a global configuration, see Associate Contact Center AI Configuration with All Call Types . To view, update, or delete the Contact Center AI configuration that is associated with a specific call type, see Associate Contact Center AI Configuration with a Call Type . |
| Step 3 | In the Unified CCE Administration console, enable or disable CCAI Services for an agent or multiple agents. For more details, see Enable or Disable Contact Center AI Services for Agents . |
| Step 4 | Undo these CCAI settings configured when Unified CCE was in 12.5: Delete the "call.user.configid" ECC variable you created for the Answers feature and remove the association of this variable
                                                with the CCE script. For more details, see the Contact Center AI Services Task Flow section in the Cisco Unified Contact Center Enterprise Features Guide, Release 12.5 at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html . In Cisco Finesse, run the following CLI command to disable the CCAI services from all the Cisco Finesse clusters: utils finesse set_property webservices enableCustomAgentServices false For more details, see the AI Services Configuration topic in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |