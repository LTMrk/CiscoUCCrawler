---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-b443bd6482
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-1501_es202603/rcct-m-feature-summary-1501-es202603.html
retrieved_at: 2026-08-16T19:35:59.551231+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions Engineering Specials, 15.0(1) SU1/ES202603

# Release notes for Cisco Contact Center Enterprise Solutions Engineering Specials, 15.0(1) SU1/ES202603

Find Matches in This Book

## Results

Updated: March 31, 2026

Chapter: Feature

## Chapter: Feature

# Feature

## Feature Summary

For 15.0(1) SU1/ES202603, the following components have made features available:

General Availability Features

General Availability refers to the stage in the product lifecycle when the software version and its documentation are officially
                           released and publicly available to all customers.

Solution/

Component

Unified CCE/Packaged CCE

Increased Reliability and Scale for Contact Center AI Features

This update is applicable only to Unified CCE. Refer to the Controlled Availability Features section for Packaged CCE.

Install 15.0(1) ES202603 on the Administration & Data Server, Administration Client, Router, Logger, and PG.

Install CVP 15.0(1) ES202603 on Unified CVP.

Upgrade Cisco VVB to 15.0(1) SU1. For information on how to upgrade Cisco VVB, see the Cisco VVB Upgrade chapter of the Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 15.0(1) .

Cross-Origin Resource Sharing for CCE

Install the 15.0(1) ES202603 on Administration & Data Server, Adminstration Client, Router, Logger, and PG.

Enhanced Secure Communication across CCE Components

Automated Identity Token Rotation for Cisco Devhub Artifactory

Upgrade Cloud Connect to 15.0(1) SU1. For information on how to upgrade, see Upgrade Cloud Connect

Parallel Patching Support

Enhanced Patch Management for all supported CCE Deployments via Orchestration

Bring Your Own Virtual Agent Integration

Install 15.0(1) ES202603 on Unified CVP.

Upgrade Cisco VVB to 15.0(1) SU1. For information on how to upgrade Cisco VVB, see the Cisco VVB Upgrade chapter of the Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 15.0(1) .

Upgrade Cloud Connect to 15.0(1) SU1. For information on how to upgrade, see Upgrade Cloud Connect

Cloud Connect

Upgrade Cloud Connect to 15.0(1) SU1. For information on how to upgrade, see Upgrade Cloud Connect

Finesse

Enhanced Content Security Policy (CSP)

Upgrade Cisco Finesse to 15.0(1) SU1. For information on how to upgrade, see the Upgrade chapter of the Cisco Finesse Installation and Upgrade Guide, Release 15.0(1) .

Enhanced Database Port Configuration in Cisco Finesse

Cisco IdS

Unified CVP

High Availability for CVP Port Usage Cache Service

Install 15.0(1) ES202603 on Unified CVP.

ECE

ECE Agent Desktop & Notification Features

ECE Configuration & Administration

ECE Security & Compliance Enhancements

Install 15.0(1) ES202603 on ECE.

Unified CCMP

Install 15.0(1) ES202603 on Unified CCMP.

Controlled Availability Features

Controlled Availability refers to the stage in the product lifecycle when a software version is officially released and made
                           publicly available to a limited set of customers, regions, markets, or industries. This allows for evaluation and feedback
                           on features that have not yet reached General Availability.

To join Controlled Availability testing or to request access to documentation, please email the Product Management team at cce-pm-team@cisco.com .

Solution/

Component

Controlled Availability Features

Installation / Upgrade Requirements

Unified CCE/Packaged CCE

Increased Reliability and Scale for Contact Center AI Features

This update is applicable only to Packaged CCE. Refer to the General Availability Features section for Unified CCE.

Install 15.0(1) ES202603 on the Administration & Data Server, Administration Client, Router, Logger, and PG.

Install CVP 15.0(1) ES202603 on Unified CVP.

Upgrade Cisco VVB to 15.0(1) SU1. For information on how to upgrade Cisco VVB, see the Cisco VVB Upgrade chapter of the Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 15.0(1) .

Integrating Webex Common Identity for Single Sign-On

Install 15.0(1) ES202603 on the Administration & Data Server, Administration Client, Router, Logger, and PG.

Integrating Webex Common Identity for Single Sign-On in CCE

Beta Features

Beta refers to the stage in the product lifecycle where select customers are invited to evaluate and provide feedback on features
                           that have not yet reached General Availability.

Beta features are not enabled by default. To join Beta testing or enable these features, email the Product Management team
                           at cce-pm-team@cisco.com .

Beta Features

Installation / Upgrade Requirements

Unified CCE/Packaged CCE

VMware to Nutanix Migration Support

For 15.0(1) deployments, 15.0(1) SU1/ES202603 is required; for 12.6(2) deployments, the required ES is component-dependent.
                                       For more information, see the Beta documentation for this feature.

Support for Migration of ECE to Nutanix

Support for Migration of Unified CCMP to Nutanix

Cisco AI Assistant

Upgrade Cloud Connect to 15.0(1) SU1. For information on how to upgrade, see Upgrade Cloud Connect

## General Availability Features

### New Features

#### SU1/ES202603

##### Increased Reliability and Scale for Contact Center AI Features

Cisco Unified Contact Center Enterprise (CCE) introduces the Media Gateway service to improve AI capabilities for live agent
                                    interactions in on-premises deployments. This service bridges on-premises infrastructure with cloud-based AI platforms, enabling
                                    real-time AI experiences for agents and supervisors.

To enable this feature:

Cisco VVB provides the following modes for this feature:Cisco VVB Service Only, Media Gateway (MGW) Service Only, or Mixed
                                          Mode (Cisco VVB & Media Gateway).

For deployments using MGW Service Only or Mixed Mode, a medium profile OVA is required. Mixed Mode deployments additionally
                                                      require increased vRAM (16 GB instead of the default 10 GB). For more information, see the Cisco VVB virtualization page.

For Unified CCE, configuration is done via the Unified CVP Operations Console (NOAMP).

For more information on how to configure the Media Gateway service, see the Call Transcription chapter in the Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

For more information on the design considerations, see the Media Gateway for CCAI Services and Contact Center AI services Task Flow section in the Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

##### Bring Your Own Virtual Agent (BYOVA) Integration

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

##### Cross-Origin Resource Sharing for CCE

Cross-Origin Resource Sharing (CORS) for CCE allows web applications running on different origins (domains, protocols, or
                                    ports) to securely access CCE APIs.

For more information, see the Cross-Origin Resource Sharing for CCE section in the Working with Unified CCE API chapter of Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1) at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_working-with-unified-cce-apis_1501.html#PCCE_RF_M76B1FFD_00 .

##### Enhanced Secure Communication across CCE Components

Transport Layer Security (TLS) is implemented over existing TCP connections to enable secure communication between Router,
                                    Logger, Administration & Data Server, Administration Client, and Peripheral Gateway (PG).

For more information, see the following guides:

The Unified CCE and Packaged CCE Port Utilization section in the Port Utilization in Contact Center Enterprise chapter of Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html.

The Add Components to Unified CCE Instance section in the Installation chapter of Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

The Enable Secure Communication Between CCE Components section in the Security Consideration chapter of Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

The Manage Secured PII in Transit and CCE Internal Interface Secure Connection sections in the Certificate Management for Secured Connections chapter of Security Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

##### Automated Identity Token Rotation for Cisco Devhub Artifactory

Orchestration now supports the automatic rotation of Cisco Devhub Artifactory Identity Token. This feature proactively updates
                                    the token in Orchestration before it expires, eliminating the need for manual intervention. This feature is disabled by default
                                    and can be enabled via the CLI. If email notifications are enabled, the system will alert administrators of both successful
                                    and failed rotation attempts.

For details on enabling the Identity Token Auto Rotation, see the Configure Identity Token Auto Rotation topic in the Deployment Tasks under CCE Orchestration chapter of the Cisco Unified Contact Center Enterprise Install and Upgrade Guide, 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

##### Parallel Patching Support

This release introduces enhanced options for the Patch Install and Rollback Orchestration CLI commands, allowing for more
                                    efficient selection of platforms and node groups.

You can now perform parallel patch installations or rollbacks across all Side A or all Side B nodes for both VOS and Windows
                                    platforms within your deployment.

The following options are now available in Patch install and rollback CLI:

VOS Platform:

All Side A VOS based-nodes in the inventory

All Side B VOS based-nodes in the inventory

Windows Platform:

All Side A Windows based-nodes in the inventory

All Side B Windows based-nodes in the inventory

These enhancements enable you to perform simultaneous operations on all selected nodes of the specified side and platform,
                                    significantly reducing maintenance windows. This new option of selecting all Side A or B nodes can be used to install or rollback
                                    15.0(1) quarterly cumulative ES and this option will support patches from 15.0(1) release onwards.

Parallel patching is applicable for all the node selection options in the patch install and roll back CLI for all the selected
                                    nodes irrespective of the target node version.

Parallel patching is enabled by default. See the "CLI to Configure Orchestration Maximum Parallel Tasks" topic under the Deployment
                                    Tasks section in the CCE Orchestration chapter of the Cisco Unified Contact Center Enterprise Install and Upgrade Guide, 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html for changing the default configuration.

##### Enhanced Patch Management for all supported CCE Deployments via Orchestration

Orchestration now supports full-lifecycle patch management-including listing, installing, and rolling back-across all supported
                                    CCE deployment types including the recent support for deployments with more than 4000 agents.

By leveraging a centralised deployment cache and parallel patching capabilities, orchestration ensures scalable and efficient
                                    patch operations for all supported CCE deployments.

For details instructions on managing the deployment cache, see the following sections in the CCE Orchestration chapter of
                                    the Cisco Unified Contact Center Enterprise Install and Upgrade Guide, 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html :

CLI to Enforce Deployment Cache Update

CLI to Configure Orchestration Scheduled Jobs ( Deployment Cache Update option)

##### Cloud Connect Subscriber Proxy Support

The Cloud Connect Integration page has been restructured into two tabs:

Cluster Configuration

Proxy settings can now be configured separately for the publisher and subscriber, with the subscriber defaulting to the publisher's
                                    proxy after installation. The Cluster Configuration tab also displays read-only hostname fields for both nodes.

Node Registration

The Node Registration tab includes a refresh button to retrieve the latest registration status.

Environments requiring a proxy server must now configure proxy settings before proceeding with node registration.

For more information, see the Cloud Connect Integration topic in the Web Based CCE Administration chapter of the Administration Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

##### Enhanced Content Security Policy (CSP) for Finesse Agents and Supervisor Desktops

Starting with this release, a strict CSP is enabled by default across the agent desktop to protect against unauthorized content
                                    and security threats. Administrators can use the new 15.0(1) CLI command to enable or disable CSP.

For more information on CLI commands, see the Manage Content Security Policy in Desktop Properties section in Cisco Finesse CLI chapter of Cisco Finesse Administration Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html

It is recommended that the custom third-party gadgets also adhere to CSP guidelines. To make these gadgets strictly CSP-compliant,
                                    see the Content Security Policy Guidelines in Gadgets and Components section of the Manage Desktop Layout chapter in the Cisco Finesse Administration Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html

##### Enhanced Database Port Configuration in Cisco Finesse

The Cisco Finesse administration console now supports separate SQL port configuration for primary and secondary Administration
                                    & Data Server Database (AWDB) connections. This enhancement replaces the single shared port field with independent port fields.

For more information, see Contact Center Enterprise Administration and Data Server Settings section in the following guides:

Cisco Finesse Administration Guide, Release 15.0(1) guide and Cisco Finesse Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html

##### Enhanced security for Identity Service (IdS) Admin

All IdS admin gadgets are now fully compliant with Content Security Policy (CSP) standards. This enhancement hardens the security
                                    of the administration portal by providing better protection against cross-site scripting (XSS) and other data injection attacks.

##### High Availability for CVP Port Usage Cache Service

The CVP Port Usage API now incorporates a resilient high-availability (HA) cache architecture to ensure uninterrupted access
                                    to essential license utilization metrics. With the deployment of Primary and Secondary Cache Service instances, the system
                                    removes single points of failure through an automated failover process.

For more information, see High Availability of the Cache Service for the CVP Port Usage API section of the User Guide for Unified CVP VXML Server and Unified CVP Call Studio, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html

##### ECE Agent Desktop & Notification Features

###### Chat and Email Audio Alerts

Audio alert settings are enhanced to support customizable sounds for chat and email interactions. Users can configure alerts
                                       for new chats, new chat messages, pull chat notifications, and new email alerts. The Manage Audio option allows users to preview
                                       out-of-the-box audio files and upload custom sounds, providing a more personalized and responsive notification experience.

###### Pull Chat Option in Agent Desktop

A new Pull Chat setting is introduced to allow agents to manually pick up incoming chat requests. When enabled, the Pull Chat
                                       option is displayed in the Agent Desktop whenever a customer initiates a chat, enabling agents to assign the chat to themselves.

###### Auto-Remove Abandoned Chats from Inbox

A new setting is introduced under Integration Settings to automatically manage abandoned chat activities. This enhancement
                                       ensures that when a chat is abandoned by the customer and not selected by any agent, the system automatically completes the
                                       activity and removes it from the inbox when the setting is enabled.

##### ECE Configuration & Administration

###### ECE Feature Flag Framework Integration

A new Feature Flag setting is introduced to enable dynamic control of application features. When enabled, ECE connects to
                                       the external Feature Flag Management Dashboard via Cloud Connect to read feature states and apply them at runtime.

This enhancement allows administrators to enable or disable features for specific tenants without code changes or deployments,
                                       providing greater flexibility and faster feature rollout.

###### Database Server Refresh Utility – Port Update Support

The awdb_server_refresh utility is enhanced to support updating the port number during server refresh.

###### Database Connection Migration Utility

A new Database Connection Migration Utility is introduced to simplify the migration of database connections from one SQL Server
                                       to another. The utility updates connection pool configurations within deployment.zip files through an interactive, guided
                                       console interface.

This enhancement enables administrators to easily review existing database connections, provide updated server details, and
                                       configure authentication credentials. The utility also supports creating required SQL Server logins during the process and
                                       automatically extracts updated configuration files to the appropriate directories, reducing manual effort and minimizing configuration
                                       errors during migration.

###### Common Identity Support for Webex CCE

Support for Common Identity is introduced to provide a unified authentication and identity management experience across Cisco
                                       contact center solutions. Webex CCE now integrates with Common Identity using OAuth2 to enable Single Sign-On for agents and
                                       supervisors.

##### ECE Security & Compliance Enhancements

###### Accessibility Enhancements for ECE Chat Templates

The chat templates have been enhanced to make them more accessible, ensuring a smoother experience for users relying on screen
                                       readers or other assistive tools.

For more information, see the Accessibility chapter in the Enterprise Chat and Email Administrator's Guide to Chat and Collaboration
                                       Resources, Release 15.

###### ECE Gadget Updated for CSP Compliance

The ECE gadget loader is updated to comply with the Content Security Policy (CSP) requirements of Finesse.

###### Improved Log Content for Security Compliance

Logging is enhanced to include comprehensive event details required for security monitoring and incident response. Log entries
                                       now capture key information such as what action occurred, source and target identifiers, location details, timestamps in standard
                                       format, and the outcome of the action.

This enhancement ensures logs provide sufficient detail for auditing, troubleshooting, and compliance with security standards
                                       while avoiding inclusion of sensitive data.

##### Non-Default SQL Port Configuration for CCMP

A configurable port number field has been introduced in the Integrated Configuration Environment (ICE), installers, and configuration
                                    tools. This field accepts numeric values only. If no port is specified, the system defaults to port 1433. This enhancement
                                    enables support for SQL Server instances running on non-default ports.

#### ES202511

For more information, see the Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202511 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-1501_es202511.html .

#### ES202508

For more information, see the Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202508 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-for-es.html .

## Controlled Availability Features

### Increased Reliability and Scale for Contact Center AI Features

Cisco Packaged Contact Center Enterprise (CCE) introduces the Media Gateway service to improve AI capabilities for live agent
                              interactions in on-premises deployments. This service bridges on-premises infrastructure with cloud-based AI platforms, enabling
                              real-time AI experiences for agents and supervisors.

To enable this feature:

Cisco VVB provides the following modes for this feature:Cisco VVB Service Only, Media Gateway (MGW) Service Only, or Mixed
                                    Mode (Cisco VVB & Media Gateway).

For deployments using MGW Service Only or Mixed Mode, a medium profile OVA is required. Mixed Mode deployments additionally
                                                require increased vRAM (16 GB instead of the default 10 GB). For more information, see the Cisco VVB virtualization page.

For Packaged CCE, configuration is done via the Unified CCE Administration console by selecting the Media Gateway check box
                                    on the Inventory page.

To ensure system stability and security, keep all Windows-based and VOS-based components updated to the latest versions. Specifically,
                                          Media Gateway requires unique patches for proper operation. Contact Cisco Technical Support to obtain the necessary updates
                                          for your environment.

For more information on the documentation, please email the Product Management team at cce-pm-team@cisco.com .

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

### VMware to Nutanix Migration Support

CCE 12.6(2) or 15.0(1) deployments running on VMware are now supported for migration to 15.0(1) SU1 on Nutanix.

VOS-based components : For components including Cloud Connect, Finesse, IdS, Cisco VVB, Cisco Unified Intelligence Center, and Live Data, administrators
                              should use the new " Fresh Install with Import " option when deploying on Nutanix. This process involves exporting platform and application data from the existing VMware
                              environment to an SFTP server and importing it during the deployment of 15.0(1) SU1 on Nutanix. See the System Requirements
                              section in this feature’s beta documentation for the required software and patch levels on both the source and destination
                              CCE deployments.

Windows-Based Components : For CCE, Unified CVP, ECE, and Unified CCMP components, follow the existing Technology Refresh and data migration procedures.

Dedicated Nutanix-specific OVA files have been released for all CCE components. There are no changes to resource requirements
                              between 15.0(1) and 15.0(1) SU1.

All CCE deployment models are supported on Nutanix, except for the Packaged CCE 2000 Agent deployment.

### Support for Migration of ECE to Nutanix

CCE now supports migration of ECE from version 15.0(1)  on VMware to version 15.0(1) SU1 on Nutanix. This enhancement enables
                              customers to transition existing deployments to Nutanix while maintaining the same release version.

### Support for Migration of Unified CCMP to Nutanix

CCE now supports migration of Unified CCMP from version 15.0(1) on VMware to version 15.0(1) SU1 on Nutanix. This enhancement
                              enables customers to transition existing deployments to Nutanix while maintaining the same release version.

### Cisco AI Assistant

Cisco AI Assistant offers voice agents with AI-powered assistance, offering Virtual agent transfer summaries, Real-Time call
                              transcript, Real-Time Assist, and Wrap-up summaries to optimize customer interactions. The AI Assistant feature supports the
                              agents and supervisors to achieve business results more quickly and with less stress. Administrator can enable or disable
                              the required AI features for specific users from the Unified CCE Administration console.

Virtual agent transfer summaries : AI-generated call summaries deliver concise, context-rich summaries at critical points throughout the customer journey.
                                    By providing agents with a clear overview of previous interactions with AI agents, the AI Assistant reduces customer repetition
                                    and speeds up issue resolution—resulting in smoother, more satisfying customer experience.

'Virtual Agent transfer Summary' is the same as 'AI Agent transfer Summary'.

Call transcript : AI-generated transcripts assist live agents in enhancing communication and maintaining focus during customer interactions
                                    by providing live transcriptions directly on the Cisco Finesse Desktop. This feature improves clarity, reduces misunderstandings,
                                    and supports agents in delivering high-quality service. Agents can view ongoing transcriptions, gain instant insights, and
                                    seamlessly manage multi-party conversations, ensuring smooth communication and continuity throughout interactions.

'Call transcript' is the same as 'Real-Time Transcription'.

Real-Time Assist : An AI-generated real-time assist utilizes an automated backend workflow to deliver contextual message prompts to live agents,
                                    enabling them to respond swiftly with relevant, tailored suggestions during live engagements.

Wrap-up summaries : AI-generated summaries produced at the conclusion of a customer call that captures essential details such as the reason
                                    for the call, actions performed, resolution outcome, and any required follow-up tasks. Agents can review, modify, and finalize
                                    this summary to minimize manual note-taking and enhance documentation accuracy and efficiency.

| Solution/ Component | General Availability Features | Installation / Upgrade Requirements |
|---|---|---|
| Unified CCE/Packaged CCE | Increased Reliability and Scale for Contact Center AI Features Note This update is applicable only to Unified CCE. Refer to the Controlled Availability Features section for Packaged CCE. | Note | This update is applicable only to Unified CCE. Refer to the Controlled Availability Features section for Packaged CCE. | Install 15.0(1) ES202603 on the Administration & Data Server, Administration Client, Router, Logger, and PG. Install CVP 15.0(1) ES202603 on Unified CVP. Upgrade Cisco VVB to 15.0(1) SU1. For information on how to upgrade Cisco VVB, see the Cisco VVB Upgrade chapter of the Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 15.0(1) . |
| Note | This update is applicable only to Unified CCE. Refer to the Controlled Availability Features section for Packaged CCE. |
| Cross-Origin Resource Sharing for CCE | Install the 15.0(1) ES202603 on Administration & Data Server, Adminstration Client, Router, Logger, and PG. |
| Enhanced Secure Communication across CCE Components |
| Automated Identity Token Rotation for Cisco Devhub Artifactory | Upgrade Cloud Connect to 15.0(1) SU1. For information on how to upgrade, see Upgrade Cloud Connect |
| Parallel Patching Support |
| Enhanced Patch Management for all supported CCE Deployments via Orchestration |
| Bring Your Own Virtual Agent Integration | Install 15.0(1) ES202603 on Unified CVP. Upgrade Cisco VVB to 15.0(1) SU1. For information on how to upgrade Cisco VVB, see the Cisco VVB Upgrade chapter of the Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 15.0(1) . Upgrade Cloud Connect to 15.0(1) SU1. For information on how to upgrade, see Upgrade Cloud Connect |
| Cloud Connect | Cloud Connect Subscriber Proxy Support | Upgrade Cloud Connect to 15.0(1) SU1. For information on how to upgrade, see Upgrade Cloud Connect |
| Finesse | Enhanced Content Security Policy (CSP) | Upgrade Cisco Finesse to 15.0(1) SU1. For information on how to upgrade, see the Upgrade chapter of the Cisco Finesse Installation and Upgrade Guide, Release 15.0(1) . |
| Enhanced Database Port Configuration in Cisco Finesse |
| Cisco IdS | Enhanced security for Identity Service (IdS) Admin | Upgrade IdS to 15.0(1) SU1. For information on how to upgrade Cisco IdS, see the Upgrades chapter of the Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 15.0(1) . |
| Unified CVP | High Availability for CVP Port Usage Cache Service | Install 15.0(1) ES202603 on Unified CVP. |
| ECE | ECE Agent Desktop & Notification Features ECE Configuration & Administration ECE Security & Compliance Enhancements | Install 15.0(1) ES202603 on ECE. |
| Unified CCMP | Non-Default SQL Port Configuration for CCMP | Install 15.0(1) ES202603 on Unified CCMP. |

| Note | This update is applicable only to Unified CCE. Refer to the Controlled Availability Features section for Packaged CCE. |
|---|---|

| Solution/ Component | Controlled Availability Features | Installation / Upgrade Requirements |
|---|---|---|
| Unified CCE/Packaged CCE | Increased Reliability and Scale for Contact Center AI Features Note This update is applicable only to Packaged CCE. Refer to the General Availability Features section for Unified CCE. | Note | This update is applicable only to Packaged CCE. Refer to the General Availability Features section for Unified CCE. | Install 15.0(1) ES202603 on the Administration & Data Server, Administration Client, Router, Logger, and PG. Install CVP 15.0(1) ES202603 on Unified CVP. Upgrade Cisco VVB to 15.0(1) SU1. For information on how to upgrade Cisco VVB, see the Cisco VVB Upgrade chapter of the Installation and Upgrade Guide for Cisco Virtualized Voice Browser, Release 15.0(1) . |
| Note | This update is applicable only to Packaged CCE. Refer to the General Availability Features section for Unified CCE. |
| Integrating Webex Common Identity for Single Sign-On | Install 15.0(1) ES202603 on the Administration & Data Server, Administration Client, Router, Logger, and PG. |
| Integrating Webex Common Identity for Single Sign-On in CCE | Install 15.0(1) ES202603 on Unified CCMP. |

| Note | This update is applicable only to Packaged CCE. Refer to the General Availability Features section for Unified CCE. |
|---|---|

|  | Beta Features | Installation / Upgrade Requirements |
|---|---|---|
| Unified CCE/Packaged CCE | VMware to Nutanix Migration Support | For 15.0(1) deployments, 15.0(1) SU1/ES202603 is required; for 12.6(2) deployments, the required ES is component-dependent.
                                       For more information, see the Beta documentation for this feature. |
| Support for Migration of ECE to Nutanix |
| Support for Migration of Unified CCMP to Nutanix |
| Cisco AI Assistant | Upgrade Cloud Connect to 15.0(1) SU1. For information on how to upgrade, see Upgrade Cloud Connect |

| Note | For deployments using MGW Service Only or Mixed Mode, a medium profile OVA is required. Mixed Mode deployments additionally
                                                      require increased vRAM (16 GB instead of the default 10 GB). For more information, see the Cisco VVB virtualization page. |
|---|---|

| Note | Environments requiring a proxy server must now configure proxy settings before proceeding with node registration. |
|---|---|

| Note | For deployments using MGW Service Only or Mixed Mode, a medium profile OVA is required. Mixed Mode deployments additionally
                                                require increased vRAM (16 GB instead of the default 10 GB). For more information, see the Cisco VVB virtualization page. |
|---|---|

| Note | To ensure system stability and security, keep all Windows-based and VOS-based components updated to the latest versions. Specifically,
                                          Media Gateway requires unique patches for proper operation. Contact Cisco Technical Support to obtain the necessary updates
                                          for your environment. |
|---|---|

| Note | All CCE deployment models are supported on Nutanix, except for the Packaged CCE 2000 Agent deployment. |
|---|---|

| Note | 'Virtual Agent transfer Summary' is the same as 'AI Agent transfer Summary'. |
|---|---|

| Note | 'Call transcript' is the same as 'Real-Time Transcription'. |
|---|---|