---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-a1b5d33b8e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-1501_es202511/rcct-m-feature-summary-1501-es202511.html
retrieved_at: 2026-08-16T19:36:12.098409+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202511

# Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202511

Find Matches in This Book

## Results

Updated: November 30, 2025

Chapter: Feature

## Chapter: Feature

# Feature

## Feature Summary

The release phases are:

General Availability refers to the stage in the product lifecycle when the software version and its documentation are officially
                                 released and publicly available to all customers.

Controlled Availability refers to the stage in the product lifecycle when a software version is officially released and made
                                 publicly available to a limited set of customers, regions, markets, or industries. This allows for evaluation and feedback
                                 on features that have not yet reached General Availability.

To join Controlled Availability testing or to request access to documentation, please email the Product Management team at cce-pm-team@cisco.com .

Beta refers to the stage in the product lifecycle where select customers are invited to evaluate and provide feedback on features
                                 that have not yet reached General Availability.

Beta features are not enabled by default. To join Beta testing or enable these features, email the Product Management team
                                 at cce-pm-team@cisco.com .

For 15.0(1) ES202511, the following components have made features available:

Engineering Special

Solution/

Component

Controlled Availability Features

Beta Features

ES202511

Unified CCE/Packaged CCE

Webex AI Agent (Scripted and Autonomous)

AppDynamics Controller Certificate Management for AppDynamics Agents

Managing AppDynamics Agent Installation and Version Updates

Integrating Webex Common Identity for Single Sign-On

Bring Your Own Virtual Agent Integration

Finesse

Enhanced Login and Lockout Notifications

Unified CVP

Enhanced CVP Port Monitoring with Real-Time Usage API

ECE

Accessibility Enhancements

Unified CCMP

Integrating Webex Common Identity for Single Sign-On

Unified CCE/Packaged CCE

New Features

Agent Typing Notification for Chat Templates

CTI Server State Sync and ECE Agent State

Ability to Search Department While Importing MRDs and Users

Support for Entra ID

Updated Features

Disabling Personal Callback Reattempt

Graceful Shutdown for Router

Webex AI Agent

## General Availability Features

### New Features

#### Webex AI Agent

The Webex AI Agent acts as a smart assistant that handles initial customer interactions across both voice and digital channels.
                                 It works in two modes:

Scripted Mode: Uses predefined rules and natural language understanding to respond accurately to common customer intents.

Autonomous Mode: Employs advanced Large Language Models (LLMs) to engage in more natural, human-like conversations, adapting dynamically to
                                       customer needs.

This means many routine inquiries are resolved before they reach you, reducing your workload and allowing you to focus on
                                 more complex customer needs.

Here's what the Webex AI Agent offers:

Seamless Human Agent Handoff: When the AI Agent escalates a conversation to you, it provides a clear summary of the interaction so far. This helps you
                                       quickly understand the customer's issue without making them repeat themselves, enabling faster and more effective support.

Multi-Channel Support: Whether customers reach out via voice calls, chat, SMS, or other digital channels, the AI Agent manages these interactions
                                       smoothly, ensuring you have consistent context regardless of the channel.

Multi-Lingual Capabilities: The AI Agent supports multiple languages, helping you assist a diverse customer base with greater ease.

Built-in Reporting and Insights: Supervisors can access detailed analytics and reports within the AI Agent Studio to monitor AI performance and customer interactions,
                                       helping optimize workflows and improve service quality.

Integration with Business Systems: The AI Agent connects seamlessly with existing business applications and automation workflows, ensuring that customer requests
                                       are handled efficiently and accurately.

For more information on the design considerations, see the following:

Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .

For more information on the how to configure and use the feature, see the following:

Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/contact-center/packaged-contact-center-enterprise-15-0-1/model.html .

#### Automated Identity Token Rotation for Cisco Devhub Artifactory

Orchestration now supports the automatic rotation of Cisco Devhub Artifactory Identity Token. This feature proactively updates
                                 the token in Orchestration before it expires, eliminating the need for manual intervention. This feature is disabled by default
                                 and can be enabled via the CLI. If email notifications are enabled, the system will alert administrators of both successful
                                 and failed rotation attempts.

For details on enabling the Identity Token Auto Rotation, see the Configure Identity Token Auto Rotation topic in the Deployment Tasks under CCE Orchestration chapter of the Cisco Unified Contact Center Enterprise Install and Upgrade Guide, 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

#### Enhanced Self Service Port Monitoring with Real-Time Usage API

A new Self-Service Port Usage and Availability API for on-premises deployment has been introduced to simplify monitoring of
                                 self-service port capacity. This enhancement provides administrators with programmatic visibility into entitled and in-use
                                 self-service ports, helping them assess current system utilization more effectively. The API also supports node-level visibility
                                 for individual CVP systems to assist with operational monitoring and troubleshooting. In addition, threshold-based syslog
                                 notifications can be used to identify high port usage conditions proactively. This capability can also support outbound calling
                                 campaigns by allowing campaigns to be adjusted based on the number of self-service ports currently in use, helping improve
                                 capacity planning and operational efficiency.

For more information, see the User Guide for Unified CVP VXML Server and Unified CVP Call Studio, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html

For details on how to configure, see the Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html

This feature is availale only if you install Unified CVP 15.0.1_ES202603.

#### Enhanced Login and Lockout Notifications

Finesse now displays a message indicating the number of remaining login attempts after each unsuccessful attempt by an agent
                                 or supervisor. If the agent or supervisor is locked out, a message appears on the login screen indicating that the account
                                 is locked.

For more information, see Account Lockout Management section in Cisco Finesse Agent and Supervisor Desktop User Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html

#### Agent Account Lockout Management

Administrators can now enable or disable the agent account lockout using a CLI command. By default, Finesse locks the account
                                 for five minutes after five consecutive unsuccessful login attempts. This new capability allows you to turn off account lockout
                                 as needed.

For more information, see the Account Locked after Five Failed Sign in Attempts section in Cisco Finesse Administration Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

#### Expanded Global Phone Books

Previously, Cisco Finesse supported up to 10 global phone books with a total of 50,000 contacts across all phone books. Starting
                                 with the Finesse 15.0(1) ES202511 release, Finesse supports a maximum of 25 global phone books and a system wide total of
                                 100,000 contacts. This improvement helps organizations to create more segmented and specialized phone books. This enhances
                                 contact management and accessibility for agents and supervisors.

For more details, see Phone Books and Contacts section in Manage Phone Books chapter in the Cisco Finesse Administration Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

#### Managing AppDynamics Agent Installation and Version Updates

Administrators can now deploy AppDynamics (AppD) agents tailored to your requirements. AppD agents such as Machine agent,
                                 Java agent, .NET agents, and .NET agent extension are no longer bundled with the software. Instead, you can import these agents
                                 from an SFTP server to the Cloud Connect server. After importing, you can update the AppD agents on all solution components.
                                 New commands have also been introduced to simplify the management of AppD agents.

For more information, see the CCE Serviceability and Monitoring using AppDynamics chapter in Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/cce_serviceability_and_monitoring_using_appdynamics.html

#### AppDynamics Controller Certificate Management for AppDynamics Agents

Administrators can now use a CLI on Unified Intelligence Center, Finesse, Cisco VVB, Cisco IdS, Cloud Connect, and Live Data
                                 to import private or public CA certificates used by the AppDynamics controller into the AppDynamics AppServer Agent and Machine
                                 Agent trust stores. This enhancement removes the reliance on default pre-packaged certificates for these agents.

For more information, see the CCE Serviceability and Monitoring using AppDynamics chapter in Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/cce_serviceability_and_monitoring_using_appdynamics.html

#### ECE Accessibility Enhancements

The chat templates have been enhanced to make them more accessible, ensuring a smoother experience for users relying on screen
                                 readers or other assistive tools.

For more information, see the Accessibility chapter in the Enterprise Chat and Email Administrator’s Guide to Administration Console, Release 15 ES2 .

#### Vue-Based ECE Chat Template

A Vue-based chat template (Base) is now available in ECE 15, supporting both docked and undocked modes. It includes features
                                 such as SSO compatibility, file attachments, localization, accessibility compliance, chat continuity on page refresh, and
                                 integration with survey forms and custom attributes.

For more information about configuring the chat template, see the Chat Templates chapter in the Enterprise Chat and Email Administrator’s Guide to Chat and Collaboration Resources, Release 15 ES2 .

#### Agent Typing Notification for ECE Chat Templates

Customers don’t have to wait and guess anymore as they can now see a real time indicator when an agent is typing a response
                                 to their query. This feature is available across the templates and custom implementation using APIs.

#### CTI Server State sync with ECE Agent state

ECE Agent state will be updated real time in case of any disconnects or logout event from the CTI server. This will help enhance
                                 the agent experience while working on chat and email.

#### Ability to search Department while importing MRDs and Users

Administrators can now search the Department, while importing UCCE MRDs and Users into ECE.

#### Support for Entra ID

CCMP Portal now allows logins using Entra ID, in addition to Windows Authentication and ADFS.

### Updated Features

#### Graceful Shutdown for Router

You can now initiate maintenance mode on Router or Rogger via orchestration.

For more information about maintenance mode in orchestration, see the Initiate maintenance mode for a specific node(s) section in CCE Orchestration chapter of the following guides:

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

#### Disabling Personal Callback Reattempt

This outbound enhacement improves agent productivity and customer experience by preventing agents from being assigned to unanswered
                                    Personal Callback (PCB) calls and by restricting redialing. Rescheduling is disabled for unreachable personal callback records
                                    with call results 2, 4, 6, 8, 9, or 16. The list of unanswered calls for manual rescheduling can also be retrieved.

CCE now allows you to use the PersonalCallbackReattempt registry item on both the Campaign Manager and Dialer to control redial attempts for unanswered.

You can prevent retry of unanswered PCB calls by disabling the PersonalCallbackReattempt registry item on both the Dialer and Campaign Manager. This configuration stops the Dialer from redialing unanswered PCB
                                    calls and ensures that the Campaign Manager does not reschedule them, instead marking the records with a closed status (C).

For more information about enabling or disabling the PersonalCallbackReattempt registry, see the Registry Settings chapter in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

## Controlled Availability Features

### Integrating Webex Common Identity for Single Sign-On in CCE

CCE now integrates Webex Common Identity for Single Sign-On to provide a unified identity framework that centralizes user
                              identities, authentication, and authorization.

Key features:

Enables AI features for Unified CCE and Packaged CCE deployments.

Federation with customer Identity Providers (IdPs) that are SAML 2.0 compliant

Alignment with Cisco security and privacy requirements

Webex Common Identity supports ECE for digital channels.

Important considerations :

Please review the following considerations carefully before enabling Webex Common Identity:

Webex Common Identity is supported only for agents and supervisors but not for administrators. Administrators will continue
                                    to use local authentication.

Supervisors can log in to the Unified CCE Admininstration console and Unified Intelligence Center using Webex Common Identity.

CCE supports SSO with Cisco IdS and Webex Common Identity, but only one can be configured for any user.

As part of the unified identity platform, Webex Common Identity integrates with CCE and is managed through Control Hub.

### Integrating Webex Common Identity for Single Sign-On in Unified CCMP

Unified CCMP now supports provisioning agents with Webex Common Identity-based SSO when integrated with Unified CCE 15.0(1),
                              and automatically recognizes Common Identity persons imported from Unified CCE whenever SSO is enabled.

For more information, see the following sections in the User Guide for Cisco Unified Contact Center Management Portal, Release 15.0 ES2 :

SSO Enabled (only available in Mixed Mode) field description in the Creating Persons chapter

Select Existing Persons > SSO Enabled and Create a New Person > SSO Enabled (only available in Mixed Mode) field description in the Creating Agents chapter

## Beta Features

### Bring Your Own Virtual Agent (BYOVA) Integration

Third-party vendors can now seamlessly integrate their Virtual Agents with Unified CCE and Packaged CCE solutions. The key
                              aspects and benefits of this feature include:

Vendor/Customer onboarding:

A structured, step-by-step onboarding process has been established, with clearly defined phases, entry criteria, activities,
                                    and success checkpoints. Once a partner or customer meets the qualification criteria, completes all required functional and
                                    non-functional validations, and submits the necessary compliance documentation, their solution becomes eligible for listing
                                    on the Cisco Marketplace. This approach streamlines the process for partners and expands customer access.

Visibility control:

Customers can choose whether to make their Virtual Agent bot available to other customers or restrict it so that it is accessible
                                    only within their own tenant.

AI provider choice:

Customers have the flexibility to select virtual agents from any provider that best meets their business, language, or domain
                                    requirements.

Diverse VA models:

The platform supports integration with virtual agents operating in either scripted or autonomous modes, allowing customers
                                    to deploy the type that best fits their needs.

Seamless integration: Once integrated, your Virtual Agents can function smoothly within the CCE solution. This enables central call flow management,
                                    session control, and AI-driven engagement without requiring changes to existing systems.

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Engineering Special | Solution/ Component | General Availability Features | Controlled Availability Features | Beta Features |
|---|---|---|---|---|
| ES202511 | Unified CCE/Packaged CCE | Webex AI Agent (Scripted and Autonomous) AppDynamics Controller Certificate Management for AppDynamics Agents Managing AppDynamics Agent Installation and Version Updates | Integrating Webex Common Identity for Single Sign-On | Bring Your Own Virtual Agent Integration |
| Finesse | Enhanced Login and Lockout Notifications Agent Account Lockout Management |  |  |
| Unified CVP | Enhanced CVP Port Monitoring with Real-Time Usage API |  |  |
| ECE | Accessibility Enhancements Vue-Based Chat Template |  |  |
| Unified CCMP |  | Integrating Webex Common Identity for Single Sign-On |  |
| ES202508 | Unified CCE/Packaged CCE | New Features Agent Typing Notification for Chat Templates CTI Server State Sync and ECE Agent State Ability to Search Department While Importing MRDs and Users Support for Entra ID Updated Features Disabling Personal Callback Reattempt Graceful Shutdown for Router |  | Webex AI Agent |

| Note | This feature is available only if you install Cisco VVB 15.0(1) SU1, Finesse 15.0(1) SU1, Unified CVP 15.0(1) ES202603, and
                                          ICM 15.0(1) ES202603. |
|---|---|

| Note | This feature is availale only if you install Unified CVP 15.0.1_ES202603. |
|---|---|

| Note | Account lockout settings apply only to Finesse local authentication; SSO account lockouts are managed by the Identity Provider
                                          (IdP), and  Webex Common Identity user lockouts are managed by Webex Control Hub. |
|---|---|