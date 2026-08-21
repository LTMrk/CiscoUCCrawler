---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-maintenance-guide-pcce-b-1501-f-f59fe6763d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/maintenance/guide/pcce_b_1501_features-guide/pcce_m_1501-webex-ai-agent.html
retrieved_at: 2026-08-21T04:33:10.308095+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Webex AI Agent

## Chapter: Webex AI Agent

# Webex AI Agent

## Feature Overview

Webex AI Agent is an AI-powered solution designed to create, manage, and deploy automated AI Agents to fulfil customer service
                           and support needs. It is designed to enhance customer interactions by automating routine tasks, delivering prompt responses,
                           and increasing overall customer satisfaction.

Webex AI Agent provides automated assistance to customers before they interact with human agents. These agents support voice
                           interactions with intonation, language understanding, and contextual awareness within conversations. AI Agents seamlessly
                           and informatively handle digital channel interactions on all supported digital channels. Customers benefit from a personalized
                           service, receiving assistance with questions, information retrieval, and minimizing wait times.

The AI Agent experience includes two agent types: Scripted AI Agent and Autonomous AI Agent . Each agent type supports a different set of capabilities depending on the interaction model and the level of automation
                           required. Scripted AI Agent is intended for guided, predefined conversational flows, while Autonomous AI Agent supports more
                           dynamic and flexible interactions, including advanced event handling and transfer scenarios.

Scripted AI Agents are rule-based agents that use a predefined set of rules, Natural Language Understanding (NLU) frameworks
                                 and classical machine learning models to generate responses, allowing the developer to define the response the AI Agent uses
                                 for specific customer queries.

The Scripted AI Agent supports the following capabilities:

EU AI Act Compliance

Scripted AI Agent supports compliance-related requirements aligned with the EU AI Act. This helps ensure that AI-driven interactions
                                       can meet applicable transparency, governance, and regulatory expectations where required.

A-law Codec Support

Scripted AI Agent supports the A-law codec for voice interactions. This enables compatibility with deployments or telephony
                                       environments that require A-law audio encoding.

An Autonomous AI Agent that can generate human-like, conversational responses to a customer query dynamically by using a Large
                                 Language Model (LLM).

The Autonomous AI Agent supports the following capabilities:

EU AI Act Compliance

Webex AI Agent now includes compliance-related enhancements that support AI development, data privacy, security, and safety
                                       requirements for customer interactions. For more information, see the AI development, data privacy, security, and safety section in the Webex AI Agent Studio Administration Guide .

A-law Codec Support

Autonomous AI Agent supports the A-law codec for supported voice integrations. This allows the agent to be used in environments
                                       where A-law codec support is required.

For more information, see the following guides:

The Feature Overview section in the Webex AI Agent chapter of Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1) and Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1) .

Dynamic Welcome Message

Autonomous AI Agent now supports dynamic welcome messages, allowing greetings to be personalized based on context such as
                                       the customer profile, entry point, or interaction scenario. For more information, see the Update Autonomous AI Agent Profile section in the Webex AI Agent Studio Administration Guide .

Custom Events: Custom Exit and Re-entry

Autonomous AI Agent now supports custom events for exit and re-entry flows. This enables more flexible conversation handling
                                       when a customer leaves a flow and later returns, or when a specific event-based path needs to be triggered. For more information,
                                       see the Configure Custom Transfer Action section in the Webex AI Agent Studio Administration Guide .

Silent and Announced Transfer

Autonomous AI Agent now supports silent transfer and announced transfer. Silent transfer moves an interaction to another destination
                                       without requiring additional customer action, while announced transfer provides for an announcement before completing the
                                       transfer. For more information about silent and announced transfers, see the Configure custom transfer action section in the Webex AI Agent Studio Administration Guide .

MCP Fulfillment Actions

Autonomous AI Agent now supports Model Context Protocol (MCP) fulfillment actions, enabling AI agents to connect directly
                                       to third-party tools and services during live conversations. For more information, see the Configure MCP client action section in the Webex AI Agent Studio Administration Guide .

Web URLs as Knowledge Sources

Autonomous AI Agent now supports web URLs as knowledge sources, allowing administrators to extract content from authorized
                                       public websites and use it for AI Agent responses. For more information, see the Create web URL knowledge source section in the Webex AI Agent Studio Administration Guide .

Webex AI Pro Europe Engine

Autonomous AI Agent now supports the Webex AI Pro-Europe 1.0 engine, providing a localized experience for Europe-based customers.
                                       For more information, see the Update autonomous AI agent profile section in the Webex AI Agent Studio Administration Guide .

Webex AI Agent offers the following feature specifically for voice channels:

AI Agent Call Transcription : Provides detailed transcripts of interactions between end customers and the Webex AI Agent, capturing every aspect of the
                                 conversation. This ensures precise documentation, so no information is missed or misinterpreted. The comprehensive transcripts
                                 allow businesses to analyze interactions more thoroughly, identify trends, recurring issues, and areas for improvement. They
                                 also help organizations better understand customer preferences and pain points, enabling more personalized and effective service.

CCE supports AI Agent capabilities for digital channels by providing agents with access to the customer interactions, rather
                                       than delivering real-time transcription of the conversation. This functionality is available across a variety of digital engagement
                                       channels, including WhatsApp, SMS, Facebook Messenger, Apple Messages for Business, and Live Chat. The feature automatically
                                       records and displays the entire interaction between customers and AI agents, allowing live agents to seamlessly review the
                                       interaction directly from their desktop interface. This comprehensive context equips agents with valuable insights, enabling
                                       them to provide more relevant and informed responses when they join the conversation.

Virtual Agent Voice (VAV) supports both G.711 μ-law and G.711 A-law codecs.

However, A-law codec is not supported for Google Dialogflow CX (DFCX) via Cloud.

## Webex AI Agent Studio

Webex AI Agent Studio is a sophisticated platform designed to create, manage, and deploy automated AI agents that fulfil customer
                           service and support needs.

Consider the following before configuring Webex AI Agent:

Task

Reference

To learn more about the Webex AI Agent Studio and its features

See the article at Webex AI Agent Studio Administration guide

For detailed information on intents, entities, and responses within AI Agent Studio

See the article at Understand intents, entities, and responses in AI Agent Studio

To explore the various templates available for creating autonomous and scripted AI agents in Webex AI Agent Studio.

See the article at Use AI agent templates

For a list of supported languages and voices for AI agents

See the article at Supported languages and voices for AI agents

To understand the different AI engines used for AI agents

See the article at Understand AI engines for AI agents

For guidelines and best practices in automating with AI agents

See the article at Guidelines and best practices for automating with AI agent

Each article provides in-depth information to help you effectively utilize the capabilities and features of Webex AI Agent
                                       Studio.

## Prerequisites

Ensure that the following components are on release 15.0(1) ES202511 or later: Cisco Unified CVP, Cisco VVB, Finesse, and Cloud Connect.

Ensure that you recompile your custom applications to maintain compatibility with JDK 17.0.For more information, see the User
                                 Guide for Unified CVP VXML Server and Unified CVP CallStudio at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html .

Order an addon for Webex AI Agent in Cisco Commerce Workspace (CCW). See the Cisco Collaboration Flex Plan Contact Center
                                 Ordering Guide page at https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/collab-flex-3-contact-center-og.html .

Enable the hybrid organization setup, which integrates both cloud and on-premises environments with necessary entitlements.
                                 The ordering process involves selecting the appropriate AI Agent units under the Collaboration Flex 3.0 Contact Center Offering.
                                 Digital AI Agents also get activated as part of the voice subscription order. The voice AI Agent entitlement grants access
                                 to Webex AI Agent Studio, enabling you to design and create AI Agents tailored to your specific use case requirements.

The allowed list in your network, where the Cisco VVB and other related contact center components operate, must include the
                                 URLs listed below. Based on the location where the hybrid organization is created, allow the following URLs in the firewall
                                 to enable network connectivity between Cisco VVB and the associated cloud services:

The following must be configured only for voice channels.

The URLs listed below collectively facilitate secure, scalable, and seamless communication between on-premises contact center
                                 components and the associated cloud services:

Ensure that you replace <regional-media-data-center> with the actual regional data center identifiers specific to your deployment. For more information on regional data center
                                             mapping, see the Regional Media Data Center Region Mapping section of the Cisco Unified/Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

Orchestrator :  This URL is configured in firewall and proxy settings.

https://insight-orchestrator. <regional-media-data-center> .rtmsprod.net:443

For example: https://insight-orchestrator.us1.rtmsprod.net:443

ID broker :  This URL is configured in the Identity Provider (IdP) settings.

https://idbroker.webex.com:443

VVB (Media / U2C / RTMS) : These URLs are set up within the firewall and proxy configurations to enable media and control communication between on-premises
                                       components and cloud services.

https://u2c-a.wbx2.com:443/u2c/api/v1

https://insight-orchestrator. <regional-media-data-center> .rtmsprod.net

For example: https://insight-orchestrator.us1.rtmsprod.net

Control Hub (AI Agent Studio) : This URL is configured in the Control Hub

https://studio.aiagent- <webexcc-data-center> .cisco.com/static/core/viewbots

Cloud Connect :  These URLs are part of the Cloud Connect component configuration.

https://idbroker.webex.com

https://u2c-a.wbx2.com/u2c/api/v1

https://config-gateway. <webexcc-data-center> .ciscoccservice.com

https://config-service. <webexcc-data-center> .ciscoccservice.com

Fusion Management Service for CC : These URLs are set up within Cloud Connect as part of the CloudConnectMgmt service configuration.

https://hercules-a.wbx2.com

https://hercules-k.wbx2.com

https://hercules-r.wbx2.com

AW / Admin PC (Cloud Connect Registration) : These URLs facilitate Cloud Connect registration and administration and are included within the configuration of the Cloud
                                       Connect component.

https://config-service. <webexcc-data-center> .ciscoccservice.com

https://config-service. <webexcc-data-center> .ciscoccservice.com

If your network permits the use of special wildcards such as "*", they can simplify firewall or proxy configurations by including
                                       the following generic group of URLs in their allowed list. This allowed list is typically configured in the firewall or proxy
                                       settings of your network where the Cisco VVB and associated services operate, ensuring unrestricted traffic to these domains.

*.cisco.com

*.ciscoservice.com

*.ciscoccservice.com

*.rtmsprod.net

*.webex.com

*.wbx2.com

## Configuration Task Flow - Voice Channels

Prerequisites

Ensure that the Cloud Connect publisher and subscriber nodes are installed.

For more information, see the Create VM for Cloud Connect Publisher and Create VM for Cloud Connect Subscriber sections in Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

Register Cloud Connect in the Unified CCE Administration console to establish a secure and trusted communication channel between
                                 the Cisco Contact Center on-premises deployment and cloud services.

For details, see the Cloud Connect Administration section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Configure Cloud Connect with CVP and VVB devices in Unified CCE Administration.

For more information, see Configure Cloud Connect Section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

After an upgrade, Cloud Connect must be reconfigured with VVB devices.

Import the Cloud Connect certificate to the CVP and VVB servers.

For more information, see the Unified CVP Security > Import Cloud Connect Certificate to Unified CVP Keystore section in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configure the Virtual Agent Voice (VAV) elements to enable Call Studio applications to communicate with the CCAI services.

For more information, see the section Settings of the VirtualAgentVoice chapter in the Element Specifications for Cisco Unified CVP VXML Server and Call Studio at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

### Setup AI agents

The following sections detail the configuration flow for integrating AI agents with the voice channel, enabling them to manage
                              voice-based customer interactions effectively:

Step

Task

Reference

Launch the Webex AI Agent Studio

See the section Access Webex AI Agent Studio in the Webex AI Agent Studio Administration guide .

Create and configure the AI agents

See the section Set up scripted AI agent and Setup Autonomous AI Agent in the Webex AI Agent Studio Administration guide .

After you configure the AI Agent in Webex AI Agent Studio, copy the Agent ID of your configured AI Agent.

See the section Create a scripted AI agent and Create a Autonomous AI agent of the Webex AI Agent Studio Administration guide .

In the Call Studio application, configure the Agent ID property of the Virtual Agent Voice element settings by copying the
                                          Agent ID configured in the Webex AI Agent Studio. Unified CVP invokes the script and sends the Agent ID to the orchestrator.
                                          The orchestrator invokes the Agent ID.

See the chapter Virtual Agent Voice of the Element Specifications for Cisco Unified CVP VXML Server and Call Studio at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

## Configuration Task Flow - Digital Channels

Prerequisites

Integrate Webex Connect and Contact Center Enterprise. Webex Connect and Contact Center Enterprise integration currently supports
                                 six channels, namely WhatsApp, SMS, Email, Facebook Messenger, Apple Messages for Business, and Live Chat. For more information
                                 on the integration, see the chapter Digital Channels Integration Using Webex Connect in the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

Configure your digital channel. For more information to configure the channel assets for each of these channels, see the section
                                 Channel Asset Configuration of the Webex Connect Documentation at https://help.webexconnect.io/docs/channel-asset-configuration-cce .

Creating flows using the flow builder. For more information, see the section Creating a Flow on Webex Connect of the Webex Connect Documentation at https://help.webexconnect.io/docs/create-a-new-flow .

### Setup AI Agents

The following sections detail the configuration flow for integrating AI agents with the digital channel, enabling them to
                              manage text-based customer interactions effectively:

Step

Task

Reference

Launch the Webex AI Agent Studio

See the section Access Webex AI Agent Studio in the Webex AI Agent Studio Administration guide .

Create and configure the AI agents

See the section Set up scripted AI agent and Setup Autonomous AI Agent in the Webex AI Agent Studio Administration guide .

Create and configure the flows of Webex Connect

See the section Flow Configurations of the Webex Connect Documentation at https://help.webexconnect.io/docs/cce-flow-configurations .

### Customers Also Viewed

- Implement CA-Signed Certificates in a CCE 12.6 Solution

| Note | CCE supports AI Agent capabilities for digital channels by providing agents with access to the customer interactions, rather
                                       than delivering real-time transcription of the conversation. This functionality is available across a variety of digital engagement
                                       channels, including WhatsApp, SMS, Facebook Messenger, Apple Messages for Business, and Live Chat. The feature automatically
                                       records and displays the entire interaction between customers and AI agents, allowing live agents to seamlessly review the
                                       interaction directly from their desktop interface. This comprehensive context equips agents with valuable insights, enabling
                                       them to provide more relevant and informed responses when they join the conversation. |
|---|---|

| Note | Virtual Agent Voice (VAV) supports both G.711 μ-law and G.711 A-law codecs. However, A-law codec is not supported for Google Dialogflow CX (DFCX) via Cloud. |
|---|---|

| Task | Reference |
|---|---|
| To learn more about the Webex AI Agent Studio and its features | See the article at Webex AI Agent Studio Administration guide |
| For detailed information on intents, entities, and responses within AI Agent Studio | See the article at Understand intents, entities, and responses in AI Agent Studio |
| To explore the various templates available for creating autonomous and scripted AI agents in Webex AI Agent Studio. | See the article at Use AI agent templates |
| For a list of supported languages and voices for AI agents | See the article at Supported languages and voices for AI agents |
| To understand the different AI engines used for AI agents | See the article at Understand AI engines for AI agents |
| For guidelines and best practices in automating with AI agents | See the article at Guidelines and best practices for automating with AI agent |

| Note | Each article provides in-depth information to help you effectively utilize the capabilities and features of Webex AI Agent
                                       Studio. |
|---|---|

| Note | The following must be configured only for voice channels. |
|---|---|

| Note | Ensure that you replace <regional-media-data-center> with the actual regional data center identifiers specific to your deployment. For more information on regional data center
                                             mapping, see the Regional Media Data Center Region Mapping section of the Cisco Unified/Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html . |
|---|---|

| Note | After an upgrade, Cloud Connect must be reconfigured with VVB devices. |
|---|---|

| Step | Task | Reference |
|---|---|---|
| 1 | Launch the Webex AI Agent Studio | See the section Access Webex AI Agent Studio in the Webex AI Agent Studio Administration guide . |
| 2 | Create and configure the AI agents | See the section Set up scripted AI agent and Setup Autonomous AI Agent in the Webex AI Agent Studio Administration guide . |
| 3 | After you configure the AI Agent in Webex AI Agent Studio, copy the Agent ID of your configured AI Agent. | See the section Create a scripted AI agent and Create a Autonomous AI agent of the Webex AI Agent Studio Administration guide . |
| 4 | In the Call Studio application, configure the Agent ID property of the Virtual Agent Voice element settings by copying the
                                          Agent ID configured in the Webex AI Agent Studio. Unified CVP invokes the script and sends the Agent ID to the orchestrator.
                                          The orchestrator invokes the Agent ID. | See the chapter Virtual Agent Voice of the Element Specifications for Cisco Unified CVP VXML Server and Call Studio at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html . |

| Step | Task | Reference |
|---|---|---|
| 1 | Launch the Webex AI Agent Studio | See the section Access Webex AI Agent Studio in the Webex AI Agent Studio Administration guide . |
| 2 | Create and configure the AI agents | See the section Set up scripted AI agent and Setup Autonomous AI Agent in the Webex AI Agent Studio Administration guide . |
| 3 | Create and configure the flows of Webex Connect | See the section Flow Configurations of the Webex Connect Documentation at https://help.webexconnect.io/docs/cce-flow-configurations . |
| 4 | Integrate AI Agents into your Webex Connect flows by using AI Agent pre-built integration node. | See the section AI Agent of the Webex Connect Documentation at https://help.webexconnect.io/docs/ai-agent-node . |