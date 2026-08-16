---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-a3837f0d75
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct_b_1501_cce-solutions-rns/rcct_m_1501_cce-solutions.html
retrieved_at: 2026-08-16T19:36:38.338358+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

# Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

Updated: April 30, 2025

Chapter: Contact Center Enterprise Solutions

## Chapter: Contact Center Enterprise Solutions

# Contact Center Enterprise Solutions

## New Features

The following table lists the new features available for each Contact Center Enterprise solution in Release 15.0(1).

Feature

Unified CCE

Packaged CCE

Support for ECE and Webex Connect Digital Channels in the Same Deployment

Yes

No

Support for WhatsApp, Facebook Messenger, and Apple Messages for Business Digital Channels

Yes

Yes

Digital Channels Anti-Malware Capabilities

Yes

Yes

Cipher Management for Improved Security

Yes

Yes

Dual Platform Support

Yes

Yes

Enhanced Granular Reporting on Agent States

Yes

No

Product Version Reporting to Cisco Smart Software Manager

Yes

Yes

### Support for ECE and Webex Connect Digital Channels in the Same Deployment

CCE's digital channels include chat and email via ECE, as well as SMS, Facebook Messenger, WhatsApp, and Apple Messages for
                              Business, via integration with Webex Connect.

Now, CCE supports both Webex Connect and ECE in a single deployment, allowing agents to use both platforms. Each agent can
                              communicate via Chat and Email through ECE, and also use social channels such as SMS, Facebook Messenger, WhatsApp, and Apple
                              Messages for Business through Webex Connect from a single Finesse Desktop interface.

If you're using ECE as your main digital channel and plan to switch to Webex Connect digital channels, this new feature enables
                              training for your agents in batches, making the transition smoother.

For more information on how to configure and use this feature, see the ECE and WebexConnect in Same Deployment for Same Agent
                              chapter in the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

This feature is not supported in Packaged CCE deployments.

A maximum of 400 agents can handle tasks from both ECE and Webex Connect Digital Channels at the same time. This 400-limit
                                                only applies to agents with both ECE and Webex Connect channels enabled, regardless of whether ECE is in a co-located 400
                                                agent deployment or a distributed 2500 agent deployment.

Ensure that ECE is configured within the configuration limits defined for your deployment type. This also means that the limits
                                                that apply to ECE also apply to the combination of ECE and Webex Connect.

For more information on the configuration limits, see all limits defined for ECE in the Configuration Limits and Feature Availability for Reference Designs chapter in the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

### Support for WhatsApp, Facebook Messenger, and Apple Messages for Business Digital Channels

Contact Center Enterprise integrates with Webex Connect, empowering businesses to connect with their customers across multiple
                              digital channels. In addition to its existing support for Email, Live Chat, and SMS, this feature has now expanded its digital
                              channel offerings to include WhatsApp, Facebook Messenger, and Apple Messages for Business.

For details on how to configure the digital channel interaction using Webex Connect, see the Digital Channels Integration Using Webex Connect chapter in the following documents:

Cisco Unified Contact Center Enterprise Features Guide

Cisco Packaged Contact Center Enterprise Features Guide

For information on the design considerations, see the Digital channels integration using Webex Connect considerations section in following documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise

Solution Design Guide for Cisco Packaged Contact Center Enterprise

For information about how to configure the Manage Digital Channels gadget, see the Manage Digital Channels gadget section in the Cisco Finesse Administration Guide .

For information about how to use the Manage Digital Channels gadget, see the Cisco Contact Center Enterprise Manage Digital Channels Gadget User Guide .

To set up a WhatsApp Business account (WABA) and connect it with Webex Connect for interacting with Contact Center agents
                              via WhatsApp on mobile, desktop app, or WhatsApp web, see WhatsApp Integration with Webex Connect User Guide .

To set up a Facebook page and connect it with Webex Connect for interacting with Contact Center agents via Facebook Messenger
                              on mobile, desktop app, or web page, see Facebook Messenger Integration with Webex Connect User Guide .

### Digital Channels Anti-Malware Capabilities

Webex Connect now provides enhanced malware protection for CCE digital channels by continuously monitoring file activity for
                              faster threat detection. Malware detection is enabled by default across all digital channels, protecting agents and customers,
                              thereby helping organizations prevent breaches.

The latest Webex Connect Workflows automatically detect malware in attachments and notify both agents and customers if a file
                              is dropped due to malicious content. The template flow includes pre-filled channel-specific variables that display the results
                              of the malware scan on the attachment.

For details on setting up Webex ConnectWorkflow to process anti-malware scan results and more, see the Anti-Malware Scan for
                              Attachments topic in the Digital Channels Integration Using Webex Connect chapter of the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

### Cipher Management for Improved Security

Previously, modifying a cipher in Unified Intelligence Center, Finesse, Cisco VVB, and Cloud Connect required assistance from
                              the Cisco Technical Assistance Center (TAC). Now, administrators have access to a set of new CLI commands specifically designed
                              for managing ciphers. These commands enable administrators to list, add, and remove ciphers. By directly managing the ciphers,
                              administrators can guarantee that their systems adhere to security policies and industry standards.

For more information on the CLI commands, see the Cipher Management topic in the Administration Guide for Cisco Unified Contact Center Enterprise guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html

### Dual Platform Support

Contact Center Enterprise (CCE) components supports the following platforms:

Microsoft Windows Server 2019 and Microsoft SQL Server 2019

Microsoft Windows Server 2022 and Microsoft SQL Server 2022

The cross combination of platforms is not supported. For example, Windows Server 2022 with SQL Server 2019 or Windows Server
                                          2019 with SQL Server 2022 is not supported.

For more information, see the Preparation chapter the following guides:

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

### Enhanced Granular Reporting on Agent States

CCE has enhanced its capability to capture detailed information regarding agent states, enabling the creation of advanced,
                              granular reports. The Agent Event Detail table captures agent transition events and tracks the duration the agent spent in
                              each state.

To enable this feature, check the Agent event details check box in the PG Explorer , and check the Extended Event Detail check box under Call Settings > Miscellaneous window in the Unified CCE Administration.

This feature is available only for 36000 agent deployments and requires the Logger VM to have 8 vCPUs, 12000 MHz, a physical
                                          CPU base frequency of 2.50 GHz, 16 GB of vRAM, an 80 GB vDisk, and 2 vNICs. This configuration is identical to Logger VM configuration
                                          for 48000 agent deployments as documented in the Version 15.0(1) section of the Virtualization Guide for Unified Contact Center Enterprise .

For information about the agent events, see the Agent_Event_Details topic in the Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1) .

### Product Version Reporting to Cisco Smart Software Manager

Cisco Smart Software Licensing now reports the product's version details, in addition to the license entitlement, to the Cisco
                              Smart Software Manager (SSM). You can access Cisco SSM at https://software.cisco.com to find the entitlement details.

For more information, see the Product Version Reporting to Cisco SSM section in the following guides:

Administration Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

## Beta Features

In this release, Contact Center Enterprise introduces a range of exciting Beta Features.

Beta refers to the stage in the product lifecycle where select customers are invited to evaluate and provide feedback on features
                           that have not yet reached GA.

Beta features are not enabled by default and are "out of the box". To join Beta testing or enable these features, email the
                           Product Management team at cce-pm-team@cisco.com .

All Beta features need additional configurations to be enabled. For more information, see the Commands to enable beta Features
                                       section of the CLI Commands chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html.

Note that running the CLI commands is a one-time process, allowing access to multiple Beta Features afterwards.

Beta Feature

Unified CCE

Packaged CCE

Cisco AI Assistant

Yes

Yes

Webex AI Agent

Yes

Yes

### Cisco AI Assistant

AI Assistant revolutionizes customer service by enhancing your efficiency and elevating customer satisfaction.

Here's what the Cisco AI Assistant offers:

AI-generated call summaries at various touchpoints throughout the agent-customer interaction. Receive concise, context-rich
                                    summaries at critical points throughout the customer journey. By providing agents with a clear overview of previous interactions
                                    with AI agents, the AI Assistant reduces customer repetition and speeds up issue resolution—resulting in a smoother, more
                                    satisfying customer experience.

AI-generated call transcription at various touchpoints throughout the agent-customer interaction. Automatically capture and
                                    display complete transcriptions of interactions between customers and AI agents. This enables the live agent to quickly reference
                                    past conversations, search for relevant details, and engage with customers more effectively—asking the right questions.

### Webex AI Agent

The Webex AI Agent, an AI-powered virtual assistant, is now available in Scripted mode. With the Webex AI Agent, you can create
                              AI-driven voice agents to automate customer service and support interactions before involving a human agent.

These agents facilitate voice interactions with intonation, language comprehension, and contextual awareness throughout conversations.
                              Customers will benefit from an experience similar to having a personal assistant, receiving help with inquiries, information
                              retrieval, and reduced wait times.

Here's what the Webex AI Agent offers:

Scripted Mode : Scripted agents use conventional machine learning algorithms for Natural Language Understanding (NLU) to capture user intents
                                    and respond accordingly.

Voice Channel Support : Launch scripted agents effortlessly on voice.

Human Agent Handoff : Escalate conversations to human agents as part of your workflows, using built-in AI assistant integration for handoff summaries.

Multi-Lingual Support : Configure agents to support multiple languages (refer to the List of supported languages documentation).

Non-English language support is currently in Beta. These languages will be made generally available once sufficient usage
                                    data and feedback are collected.

Built-in Reporting : Access a wide range of out-of-the-box analytics and reporting within the AI agent studio.

Integration Capabilities : Seamlessly connect with business systems and existing automation workflows via Webex Connect.

## Updated Features

The following table lists the updated features available for each Contact Center Enterprise solution in Release 15.0(1).

Feature

Unified CCE

Packaged CCE

Identity Token Authentication for Cisco Devhub Artifactory

Yes

Yes

Inactivity Timer

Yes

Yes

Support for Third Party Gateways

No

Yes

Smart Transport Mode for Smart Licensing

Yes

Yes

Agent Multi Edit Attribute

Yes

Yes

Serviceability and Monitoring using AppDynamics

Yes

Yes

### Identity Token Authentication for Cisco Devhub Artifactory

Orchestration now supports both Identity Token and API key as authentication methods for Cisco Devhub Artifactory. A new CLI
                              option has been introduced, allowing administrators to configure their preferred authentication method. By default, the authentication
                              method is set to API key, but administrators can switch to Identity Token and vice versa. After selecting the preferred method,
                              authentication credentials can be configured using the CLI command for setting Artifactory Authentication Credentials.

For more information about Identity Token support, refer to the details available in the CLI to Configure Authentication Method for Artifactory topic in Deployment Tasks under the CCE Orchestration chapter of the Cisco Unified Contact Center Enterprise Install and Upgrade Guide, 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

### Smart Transport Mode for Smart Licensing

Cisco Contact Center Enterprise now supports Smart Transport as the transport mode to communicate license usage information
                              from the product instance to the Cisco Smart Software Manager (CSSM). Smart Transport improves the performance and security
                              of data transfer to CSSM.

For information about smart transport mode for smart licensing, see the Administration Guide for Cisco Unified Contact Center Enterprise https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

### Inactivity Timer

Administrators can now configure the inactivity timeout for a session to avoid being logged out after 30 minutes of inactivity.
                              Navigate to the Unified CCE Administration Portal > Call Settings > Miscellaneous > Global > Login Session > Session Inactivity Timeout to set the inactivity time.

This feature is only applicable for sessions where administrators are using the Unified CCE Administration Console and does
                                          not apply to agent sessions in Finesse Desktop and ECE.

For more information, see the following guides:

The System Setting for Unified CCE Deployment section in the Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html

The Miscellaneous section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

### Support for Third Party Gateways

Administrators can now add third-party gateways to the inventory for routing calls. For instructions, see the Optional Configurations section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide .

Cisco does not test or provide support for these third-party gateways.

### Agent Multi-Edit Attribute

Administrators and supervisors can now edit multiple attributes for a set of agents at the same time. Ensure that the agents
                              belong to the same site and department. The agents can also be global agents.

For instructions, see the Agent Multi Edit Attribute section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide .

For instructions, see the Manage Agents section in the Administration Guide for Cisco Unified Contact Center Enterprise .

### Serviceability and Monitoring using AppDynamics

The AppDynamics Agents are not deployed as a pre-packaged default option in Unified CCE 15.0(x). Before planning for one of
                                 the following scenarios, please contact Cisco Support for details on how to enable the AppDynamics in Unified CCE 15.0(x):

Upgrade from Unified CCE versions, where AppDynamics is configured for monitoring, to Unified CCE 15.0(x).

Configure AppDynamics for the first time on Unified CCE 15.0(x) deployment.

## Important Notes

### Flex CC 3.0 License Update for Third-Party MR PG Integrations

In the previous release, using MR PG with a third party integration by a partner consumed a Premium Agent license. Starting
                              from version 15.0(1), only a Standard Agent license will be needed for third-party integrations, in line with the Flex CC
                              3.0 offer.

### Migration of All Applications to 64-Bit System

The 15.0(1) release brings major platform upgrades that align with industry standards.  The improvements include a Linux change
                              that guarantees long-term support. Furthermore, a move to a 64-bit application architecture has been implemented to handle
                              memory constraints and lessen the impact of the impending end-of-life (EOL) of 32-bit architectures/processors.

For the CCE VMs only the Router and SNMP agents are 64-bit applications; the rest remain as 32-bit applications.

### SQL Server Execution Plan Issue

Microsoft SQL Server 2016 and later versions include an execution plan enhancement that can cause performance issues with
                              CCE database operations. To avoid performance issues on CCE servers, set the SQL Server compatibility level for the CCE databases
                              (Logger, AW, BA, and HDS) to the SQL Server 2014 equivalent—compatibility level 120. For more information, see CSCvw51851.

Do not change the compatibility level for SQL Server system databases.

Run the following query against each applicable CCE database:

ALTER DATABASE <CCE_database_name> SET COMPATIBILITY_LEVEL = 120

You can run this query while the system is in operation.

After upgrading to CCE Release 15.0(1) or installing a Release 15.0(1) Engineering Special up to ES202603, verify the SQL
                              Server compatibility level. Due to CSCwu46995, the upgrade or Engineering Special installation might reset a manually configured
                              compatibility level to the default for the SQL Server version installed on the CCE server. If it is reset, set the applicable
                              CCE databases back to compatibility level 120.

## Deprecated Features

Deprecated features are fully supported. However, there is no additional development for deprecated features. These features
                              may be scheduled to be removed in a future release. Plan to transition to the designated replacement feature. If you are implementing
                              a new deployment, use the replacement technology rather than the deprecated feature.

Deprecated Feature

Announced

Replacement

Notes

Smart Call Home: Transport Mode for Smart Licensing

15.0(1)

Smart Transport

With the deprecation of Smart Call Home , it is recommended that you select Smart Transport as the transport mode to fully leverage the features and functionalities that Smart Licensing offers.

Microsoft Windows Server 2019

15.0(1)

Microsoft Windows Server 2022

None

Microsoft SQL Server 2019

15.0(1)

Microsoft SQL Server 2022

None

Cisco Unified IP Interactive Voice Response (IVR)

15.0(1)

CVP

15.0(1) will be the final CCE version that supports IP IVR.

Virtual Agent - Voice (VAV) over Premise-based Connector (Dialogflow CX)

15.0(1)

VAV over Cloud-based Connector

VAV over Premise based Connector, which utilizes Google's Dialogflow CX service leveraging DialogflowCX element in the Unified Call Studio is now deprecated.

VAV over Premise-based Connector (Dialogflow ES)

15.0(1)

VAV over Cloud-based Connector

The Dialogflow ES integration, which is supported through the Cisco OAMP UI and powered by a service account, is now deprecated.

## Removed and Unsupported Features

The features listed in the following table are no longer available.

Notes

Integrity Check Tool

12.6(2)

None

External Script Validation

12.6(2)

None

Translation Route Wizard

12.6(2)

Translation Route Explorer

Generic PG

12.6(2)

Agent PG and VRU PG

Cisco Hosted Collaboration Solution for Contact Center (HCS for CC)

12.6(1)

Unified CCE or Webex CCE.

MIB Objects:

cccaDistAwWebViewEnabled

cccaDistAwWebViewServerName

cccaSupportToolsURL

cccaDialerCallAttemptsPerSec

12.6(1)

None

"Sprawler" deployment

12.6(1)

Packaged CCE deployment

Shared ACD Line

12.6(1)

Agent Device Selection

For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html .

ECSPIM/Avaya (Definity) PG using CVLAN interface

12.5(2)

TAESPIM/Avaya (Definity) PG using TSAPI interface

Avaya Aura Contact Center (AACC - formerly Symposium) PG

12.5(2)

Migrate to Contact Center Enterprise or Webex CCE.

Aspect PG

12.5(2)

Migrate to Contact Center Enterprise or Webex CCE.

Symposium ACD

12.5(2)

Migrate to Contact Center Enterprise or Webex CCE.

Customer Journey Analyzer for Business Metrics (Trials)

12.5(2)

None

Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued.

Internet Explorer 11

12.5(2)

Edge Chromium (Microsoft Edge)

## Third Party Software Impacts

For the list of third-party software, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Feature | Unified CCE | Packaged CCE |
|---|---|---|
| Support for ECE and Webex Connect Digital Channels in the Same Deployment | Yes | No |
| Support for WhatsApp, Facebook Messenger, and Apple Messages for Business Digital Channels | Yes | Yes |
| Digital Channels Anti-Malware Capabilities | Yes | Yes |
| Cipher Management for Improved Security | Yes | Yes |
| Dual Platform Support | Yes | Yes |
| Enhanced Granular Reporting on Agent States | Yes | No |
| Product Version Reporting to Cisco Smart Software Manager | Yes | Yes |

| Note | This feature is not supported in Packaged CCE deployments. A maximum of 400 agents can handle tasks from both ECE and Webex Connect Digital Channels at the same time. This 400-limit
                                                only applies to agents with both ECE and Webex Connect channels enabled, regardless of whether ECE is in a co-located 400
                                                agent deployment or a distributed 2500 agent deployment. Ensure that ECE is configured within the configuration limits defined for your deployment type. This also means that the limits
                                                that apply to ECE also apply to the combination of ECE and Webex Connect. For more information on the configuration limits, see all limits defined for ECE in the Configuration Limits and Feature Availability for Reference Designs chapter in the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html |
|---|---|

| Note | The cross combination of platforms is not supported. For example, Windows Server 2022 with SQL Server 2019 or Windows Server
                                          2019 with SQL Server 2022 is not supported. |
|---|---|

| Note | This feature is available only for 36000 agent deployments and requires the Logger VM to have 8 vCPUs, 12000 MHz, a physical
                                          CPU base frequency of 2.50 GHz, 16 GB of vRAM, an 80 GB vDisk, and 2 vNICs. This configuration is identical to Logger VM configuration
                                          for 48000 agent deployments as documented in the Version 15.0(1) section of the Virtualization Guide for Unified Contact Center Enterprise . |
|---|---|

| Note | All Beta features need additional configurations to be enabled. For more information, see the Commands to enable beta Features
                                       section of the CLI Commands chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html. Note that running the CLI commands is a one-time process, allowing access to multiple Beta Features afterwards. |
|---|---|

| Beta Feature | Unified CCE | Packaged CCE |
|---|---|---|
| Cisco AI Assistant | Yes | Yes |
| Webex AI Agent | Yes | Yes |

| Feature | Unified CCE | Packaged CCE |
|---|---|---|
| Identity Token Authentication for Cisco Devhub Artifactory | Yes | Yes |
| Inactivity Timer | Yes | Yes |
| Support for Third Party Gateways | No | Yes |
| Smart Transport Mode for Smart Licensing | Yes | Yes |
| Agent Multi Edit Attribute | Yes | Yes |
| Serviceability and Monitoring using AppDynamics | Yes | Yes |

| Note | This feature is only applicable for sessions where administrators are using the Unified CCE Administration Console and does
                                          not apply to agent sessions in Finesse Desktop and ECE. |
|---|---|

| Note | Cisco does not test or provide support for these third-party gateways. |
|---|---|

| Note | For the CCE VMs only the Router and SNMP agents are 64-bit applications; the rest remain as 32-bit applications. |
|---|---|

| Deprecated Feature | Announced | Replacement | Notes |
|---|---|---|---|
| Smart Call Home: Transport Mode for Smart Licensing | 15.0(1) | Smart Transport | With the deprecation of Smart Call Home , it is recommended that you select Smart Transport as the transport mode to fully leverage the features and functionalities that Smart Licensing offers. |
| Microsoft Windows Server 2019 | 15.0(1) | Microsoft Windows Server 2022 | None |
| Microsoft SQL Server 2019 | 15.0(1) | Microsoft SQL Server 2022 | None |
| Cisco Unified IP Interactive Voice Response (IVR) | 15.0(1) | CVP | 15.0(1) will be the final CCE version that supports IP IVR. |
| Virtual Agent - Voice (VAV) over Premise-based Connector (Dialogflow CX) | 15.0(1) | VAV over Cloud-based Connector | VAV over Premise based Connector, which utilizes Google's Dialogflow CX service leveraging DialogflowCX element in the Unified Call Studio is now deprecated. |
| VAV over Premise-based Connector (Dialogflow ES) | 15.0(1) | VAV over Cloud-based Connector | The Dialogflow ES integration, which is supported through the Cisco OAMP UI and powered by a service account, is now deprecated. |

| Feature | Effective from Release | Replacement | Notes |
|---|---|---|---|
| Unified Intelligent Contact Management (ICM) deployments including all NICs | 15.0(1) | None | INCRP NIC is the only exception, as it will continue to be used for routing calls between two Unified CCE instances and in
                                    Contact Director deployments. |
| TAESPIM/Avaya (Definity) PG using TSAPI interface | 15.0(1) | None |  |
| UCC Enterprise Gateway PG (Parent PG in Parent-Child deployments) | 15.0(1) | None |  |
| Unified CCE System PG | 15.0(1) | Agent PG and VRU PG |  |
| CTI OS | 15.0(1) | Cisco Finesse on Unified CCE or Packaged CCE deployments |  |
| Contact Share | 15.0(1) | None |  |
| Webex Experience Management | 15.0(1) | None |  |
| Microsoft Windows Server 2016 | 15.0(1) | Microsoft Windows Server 2022 |  |
| Microsoft SQL Server 2017 | 15.0(1) | Microsoft SQL Server 2022 |  |
| Integrity Check Tool | 12.6(2) | None |  |
| External Script Validation | 12.6(2) | None |  |
| Translation Route Wizard | 12.6(2) | Translation Route Explorer |  |
| Generic PG | 12.6(2) | Agent PG and VRU PG |  |
| Cisco Hosted Collaboration Solution for Contact Center (HCS for CC) | 12.6(1) | Unified CCE or Webex CCE. | Before upgrading a HCS for CC deployment to version 15.0(1), switch to a Unified CCE deployment type first. |
| MIB Objects: cccaDistAwWebViewEnabled cccaDistAwWebViewServerName cccaSupportToolsURL cccaDialerCallAttemptsPerSec | 12.6(1) | None |  |
| "Sprawler" deployment | 12.6(1) | Packaged CCE deployment |  |
| Shared ACD Line | 12.6(1) | Agent Device Selection Note For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . | Note | For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |  |
| Note | For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |
| ECSPIM/Avaya (Definity) PG using CVLAN interface | 12.5(2) | TAESPIM/Avaya (Definity) PG using TSAPI interface |  |
| Avaya Aura Contact Center (AACC - formerly Symposium) PG | 12.5(2) | Migrate to Contact Center Enterprise or Webex CCE. |  |
| Aspect PG | 12.5(2) | Migrate to Contact Center Enterprise or Webex CCE. |  |
| Symposium ACD | 12.5(2) | Migrate to Contact Center Enterprise or Webex CCE. |  |
| Customer Journey Analyzer for Business Metrics (Trials) | 12.5(2) | None Note Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued. | Note | Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued. |  |
| Note | Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued. |
| Internet Explorer 11 | 12.5(2) | Edge Chromium (Microsoft Edge) |  |

| Note | For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |
|---|---|

| Note | Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued. |
|---|---|