---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-release-gui-06de92a5d4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/release/guide/rcct_b_cce-solutions-rns-12-6-2/rcct_m_cce-solutions-12-6-2.html
retrieved_at: 2026-08-16T19:37:20.866303+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

# Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

Updated: February 27, 2026

Chapter: Contact Center Enterprise Solutions

## Chapter: Contact Center Enterprise Solutions

# Contact Center Enterprise Solutions

## New Features

The following table lists the new features available for each Contact Center Enterprise solution in Release 12.6(2).

Feature

Unified CCE

Packaged CCE

Identity Token Authentication and Automated Identity Token Rotation for Cisco Devhub Artifactory

Yes

Yes

Enhanced Secure Communication across CCE Components (ES102, ES103, ES108)

Yes

Yes

Configure Custom SQL Server Port (ES98 and ES100)

Yes

Yes

Connect with business through digital channels using Webex Connect

Yes

Yes

Support for WhatsApp, Facebook Messenger, and Apple Messages for Business Digital Channels

Yes

Yes

Support for ECE and Webex Connect Digital Channels in the Same Deployment

Yes

No

Digital Channels Anti-Malware Capabilities

Yes

Yes

Agent Request or Web Callback using Webex Connect

Yes

Yes

Virtual Agent-Voice Call Transcription

Yes

Yes

Preflight request for Private Network Access

Yes

Yes

License Reservation

Yes

Yes

HTTP Strict Transport Security Support for Unified CCE Web Applications

Yes

Yes

Custom Truststore to Store Component Certificates

Yes

Yes

JTAPI credentials encryption (ES 35)

Yes

Yes

Support for 48000 Agents (ES04 and ES 25)

Yes

No

### Identity Token Authentication and Automated Identity Token Rotation for Cisco Devhub Artifactory

Orchestration now supports both Identity Token and API key as authentication methods for Cisco Devhub Artifactory. A new CLI
                              option has been introduced, allowing administrators to configure their preferred authentication method. By default, the authentication
                              method is set to API key, but administrators can switch to Identity Token and vice versa. After selecting the preferred method,
                              authentication credentials can be configured using the CLI command for setting Artifactory Authentication Credentials.

Orchestration also supports the automatic rotation of Cisco Devhub Artifactory Identity Token by proactively updating token
                              in Orchestration before it expires, eliminating the need for manual intervention. This feature is disabled by default and
                              can be enabled via the CLI. If email notifications are enabled, the system will alert administrators of both successful and
                              failed rotation attempts.

For more information about Identity Token support, refer to the details available in the CLI to Configure Authentication Method
                              for Artifactory topic in Deployment Tasks under the CCE Orchestration chapter of the Cisco Unified Contact Center Enterprise Install and Upgrade Guide, 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

For details on enabling the Identity Token Auto Rotation, see the Configure Identity Token Auto Rotation topic in the Deployment
                              Tasks under CCE Orchestration chapter of the Cisco Unified Contact Center Enterprise Install and Upgrade Guide, 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

This feature is available only if you install the Cloud Connect 12.6(2) ES04 https://software.cisco.com/download/home/268439622/type/286325642/release/12.6(2)ES4 .

### Enhanced Secure Communication across CCE Components (ES102, ES103, ES108)

Transport Layer Security (TLS) is implemented over existing TCP connections to enable secure communication between Router,
                              Logger, Administration & Data Server, Adminstration Client, and Peripheral Gateway (PG).

This feature is available only if you install the following Engineering Special (ES) or later cummulative ES releases:

For Administration & Data Server, Adminstration Client, install ICM12.6.2_ES102 .

For Router and Logger, install ICM12.6.2_ES103 .

For PG, install ICM12.6.2_ES108 .

For more information, see the following guides:

The Unified CCE and Packaged CCE Port Utilization section in the Port Utilization in Contact Center Enterprise chapter of Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

The Add Components to Unified CCE Instance section in the Installation chapter of Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

The Enable Secure Communication Between CCE Components section in the Security Consideration chapter of Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

The Manage Secured PII in Transit and CCE Internal Interface Secure Connection sections in the Certificate Management for Secured Connections chapter of Security Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

### Configure Custom SQL Server Port (ES98 and ES100)

Contact Center Enterprise now supports configuring custom SQL Server port. Administrators can specify a custom port other
                              than the default port 1433 to address security requirements and ensure compliance with the CIS Microsoft SQL Server Benchmark
                              recommendation to use non-standard port for SQL Server.

This feature is available only if you install the following installer or later cummulative ES releases:

For Logger and Router, install ICM12.6.2_ES98 .

For AW and Administration Client, install ICM12.6.2_ES100 .

For CUIC, install CUIC.1262.ES04 COP.

You can configure a custom SQL Server port for all CCE agent deployments.

The custom SQL Server port is supported on CCE databases and can be configured across Cisco Finesse, CUIC, Live Data, and
                                                Administration Client components that connect to these databases. However, it cannot be configured to Enterprise Chat and
                                                Email (ECE),  Contact Center Management Portal (CCMP), and Cloud Connect (for Digital Channels) for connection to CCE databases.

The Custom SQL Server port feature will be supported for Cloud Connect (Digital Channels) as part of CSCwr89012.

For more information, see the Custom SQL Server Port section in the SQL Server Hardening chapter of Security Guide for Cisco Unified ICM/Contact Center Enterprise .

### Connect with business through digital channels using Webex Connect

Today's customers want to connect with businesses through any communication channel of their choice. Webex Connect allows
                              the Contact Center business and its customers to interact using digital channels such as email, chat, and SMS.

The Contact Center Enterprise (CCE) solution integrates with Webex Connect to create a seamless omnichannel experience for your agents. This integration helps
                              your customers to interact across voice and digital communication channels as one unified solution.

Webex Connect offers a rich self-service and bot integration to empower your customers to get answers to some common questions.
                              It provides a unified solution for integrated routing, Agent Desktop, and reporting service. Webex Connect provides a simplified
                              framework that helps partners and customers interact through digital channels.

For details on how to configure the digital channel interaction using Webex Connect, see the Digital Channels Integration Using Webex Connect chapter in the following documents:

Cisco Unified Contact Center Enterprise Features Guide

Cisco Packaged Contact Center Enterprise Features Guide

For information on the design considerations, see the Digital channels integration using Webex Connect considerations section in following documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise

Solution Design Guide for Cisco Packaged Contact Center Enterprise

For information about how to configure the Manage Digital Channels gadget, see the Manage Digital Channels gadget section in the Cisco Finesse Administration Guide .

For information about how to use the Manage Digital Channels gadget, see the Cisco Contact Center Enterprise Manage Digital Channels Gadget User Guide .

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

### Digital Channels Anti-Malware Capabilities

Webex Connect now provides enhanced malware protection for CCE digital channels by continuously monitoring file activity for
                              faster threat detection. Malware detection is enabled by default across all digital channels, protecting agents and customers,
                              thereby helping organizations prevent breaches.

The latest Webex Connect Workflows automatically detect malware in attachments and notify both agents and customers if a file
                              is dropped due to malicious content. The template flow includes pre-filled channel-specific variables that display the results
                              of the malware scan on the attachment.

For details on setting up Webex ConnectWorkflow to process anti-malware scan results and more, see the Anti-Malware Scan for
                              Attachments topic in the Digital Channels Integration Using Webex Connect chapter of the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

### Agent Request or Web Callback using Webex Connect

The Agent Request or Web Callback feature allows customers to request a call from the Contact Center through the web. You
                              can use the Webex Connect platform to allow customers to submit a form with their preferred phone number to receive a callback
                              from a Contact Center agent.

Use this feature to switch between media channels when wait times are long. For example, if Live Chat has high wait times,
                              you can offer customers a voice callback option instead of making them wait.

For more information, see the Agent Request or Web Callback using Webex Connect topic in the Digital Channels Integration
                              Using Webex Connect chapter in the Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

### Virtual Agent-Voice Call Transcription

This feature is available to customers on request and only after necessary review and agreement. Please contact your Partner
                                          or Customer Success Manager or Cisco Support for details.

Cisco Contact Center Enterprise leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to provide
                              transcription services that assist agents. These services are available for the agents in the Cisco Finesse desktop gadgets.

If a customer has interacted with a virtual agent at the beginning of the call and then the call gets routed to an agent,
                              the Transcript gadget displays the transcript of the voice conversation between the customer and the virtual agent along with the live transcript.
                              It helps in gathering context from the earlier interaction with the virtual agent and capturing high level summary points
                              for wrapping up the call. In addition, there is a Highlights panel that displays the intents and intent parameters based on the customer's query. This helps the agent to assess the overall
                              interaction and how satisfied the customers are.

For details on how to configure VAV call transcription, refer to the following documents:

Virtual Agent–Voice Call Transcription chapter in the Cisco Unified Contact Center Enterprise Features Guide .

Virtual Agent–Voice Call Transcription chapter in the Cisco Packaged Contact Center Enterprise Features Guide .

For instructions about how to view the transcript, see the Transcript section in the Contact Center AI Gadgets User Guide for Cisco Contact Center Enterprise .

### Preflight request for Private Network Access

As browsers like Google Chrome, Microsoft Edge have now deprecated direct access to private network endpoints from public
                              websites, the preflight requests mechanism is enabled by default. This feature provides you a more secure access to web application
                              servers that reside in a private network.

To disable the preflight request feature:

In the HKEY_LOCAL_MACHINE root registry, go to SOFTWARE\Cisco Systems, Inc.\ICM\SystemSettings.

Create a DisablePnaPreflight string.

Set the value of the string to true.

The system accepts only the value true for disabling the feature or it remains in its default enabled state.

For more information, refer to the Field Notice at https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72432.html

### License Reservation

Unified CCE Deployments that are unable to share license utilization data with Cisco SSM on a regular basis due to regulatory
                              requirements can now use the Specific License Reservation (SLR) feature. Using this feature, you can reserve licenses (including
                              add-on licenses) for your product instance and share the license utilization data with Cisco SSM.

For information about Specific License Reservation, see the Smart Licensing section in the Administration Guide for Cisco Unified Contact Center Enterprise .

### HTTP Strict Transport Security Support for Unified CCE Web Applications

In this release, the Unified CCE web applications such as Diagnostic Portico, CCE Administration, and Websetup will support
                              HTTP Strict Transport Security (HSTS). The Unified CCE web applications will use the HSTS header to instruct the browsers
                              to use only the HTTPS connections.

The Internet Script Editor (ISE) will use the HTTPS connection to communicate with the Administration and Data Server.

The interface to download the ISE client from the Administration and Data Server will happen only over the HTTPS connection
                              and any attempt to download using an HTTP connection will be forbidden.

The following additional security hardening measures are added on the ISE installer location:

Disabled directory and wildcard listing.

Disabled anonymous authentication, and enabled basic or windows authentication.

Disabled the following unused HTTP methods: PUT , POST , and DELETE .

For more information, see the Internet Script Editor section in the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

### Custom Truststore to Store Component Certificates

Starting Unified CCE 12.6(x), a new custom truststore is created under the Unified ICM Installation directory <ICM install directory>\ssl\cacerts to store all the component certificates. With this new custom truststore, you don't need to export and import the certificates
                              each time Java is updated in the system.

After upgrading from Unified CCE 12.5(x) to Unified CCE 12.6(x), you should export the certificates from the Java truststore
                              to the custom truststore under the Unified ICM Installation directory <ICM install directory>\ssl\cacerts .

Export the certificate from the Java truststore:

Run the command at the command prompt: cd %JAVA_HOME%\bin .

Important

Export the certificates of all the components imported into the truststore.

Enter the truststore password when prompted.

Import the certificate to the custom truststore:

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Import the certificates for all the components that you exported from the Java truststore.

Enter the truststore password when prompted.

Enter 'yes' when prompted to trust the certificate.

### JTAPI credentials encryption (ES 35)

UCCE 12.6(2) ES35 supports Agent PG encrypting the JTAPI credentials which can be configured , if required . To use the Agent PG encryption
                              feature, install UCCE 12.6(2)_ES35 on Agent PG and follow the instructions in the ES35 reference document.

### Support for 48000 Agents (ES04 and ES 25)

UCCE 12.6(2), with ES 04 and ES 25 , supports an increased scale of up to 48000 concurrent agents on a single UCCE instance
                              . It is based on the 24000 and 36000 reference models and needs reconfiguration of the router. For more information about
                              moving to the 48000-deployment model, see the ES-specific Release Notes.

12.6(2) ES04

12.6(2) ES25

## Updated Features

The following table lists the updated features available for each Contact Center Enterprise solution in Release 12.6(2).

Feature

Unified CCE

Packaged CCE

Disabling Personal Callback Reattempt

Yes

Yes

Simplified upgrade

Yes

Yes

AppDynamics built-in integration with CCE

Yes

Yes

Inactivity Timer

Yes

Yes

Support for Third Party Gateways

No

Yes

Agent Multi Edit Attribute

Yes

Yes

Graceful Shutdown on Router

Yes

Yes

### Disabling Personal Callback Reattempt (ES85 for Router or Logger) (ES86 for PG)

The outbound enhacement improves agent productivity and customer experience by preventing agents from being assigned to unanswered
                              PCB calls and by restricting redialing. It also disables rescheduling of unreachable personal callback records with call results
                              2, 4, 6, 8, 9, or 16. Additionally, the list of unanswered calls for manual rescheduling can also be retrieved.

Contact Center Enterprise now allows you to use the PersonalCallbackReattempt registry on both the Campaign Manager and Dialer to control redial attempts for unanswered Personal Callback (PCB) calls.

You can prevent retry of unanswered PCB calls by disabling the PersonalCallbackReattempt registry on both the Dialer and Campaign Manager. This configuration stops the Dialer from redialing unanswered PCB calls
                              and ensures that the Campaign Manager does not reschedule them, instead marking the records with a closed status (C).

To leverage this feature in the Unified CCE 12.6(2), install the Unified CCE 12.6(2) ICM12.6.2_ES85 for Router or Logger, or install the Unified CCE 12.6(2) ICM12.6.2_ES86 for PG.

For more information about enabling or disabling the PersonalCallbackReattempt registry, see the Registry Settings chapter in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

### Simplified upgrade

The Orchestration feature provides partners and administrators an option to automatically download software updates and simplify
                              the installation and rollback processes.

The following CLIs are introduced in Release 12.6(2):

CLI to initiate software download from Cisco hosted software artifactory to Cloud Connect server. This CLI is used to initiate
                                    software download before the next scheduled download. The CLI can also be used to enforce the clean-up and download of restricted
                                    vs unrestricted software when the usage of restricted vs unrestricted software is changed for the deployment after initial
                                    configuration.

CLI to configure the bandwidth, used by orchestration, for downloading software from Cisco hosted software artifactory to
                                    Cloud Connect server. Bandwidth control is disabled by default, and you must configure it on Cloud Connect publisher and subscriber
                                    separately. Also, you must configure the bandwidth only after the software from Cisco hosted software artifactory is downloaded
                                    for the first time locally to the Cloud Connect server. We recommend a minimum of 10 Mbps bandwidth for optimal software download.

CLI to change the default schedule for software download from Cisco hosted software artifactory or to change the previously
                                    configured software download schedule. This is configured on Cloud Connect publisher and subscriber separately.

CLI to configure the proxy, used by Orchestration, for checking and fetching updates from Cisco-hosted cloud artifactory.
                                    Orchestration supports only HTTPS proxy.

For more information on the new CLIs, see the Orchestration chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide or Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide .

Orchestration supports upgrade and rollback of  12.5(2) and 12.5(2) ES.

Orchestration supports the recent change in multistage upgrade workflow for 4000 agents and above deployments, where Unified
                              CVP and Cisco VVB moved to Stage 2 and Stage 3 respectively in the updated workflow. For more information, refer to the following
                              documents:

Unified Contact Center Enterprise: See the Multistage UpgradeWorkflow for 4000 Agents and above section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

Packaged Contact Center Enterprise: See the Upgrade Flowcharts for 4000 Agents and above Deployments section in the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide .

Software download via orchestration now validates the digital signature for Unified ICM and Unified CVP software and removes
                              the software from Cloud Connect if the signature validation fails. Email notification is sent if the digital signature validation
                              fails.

Serviceability for software download entitlement failure is enhanced. The logs capture the MDFID along with the product name
                              for which the entitlement failed for the customer.

### AppDynamics built-in integration with CCE

For Cisco Contact Center Enterprise solution, it's important to have continuous and seamless monitoring of the deployed solution
                              and automated alerting when anomalies are detected. AppDynamics provides a solution for application and platform performance
                              monitoring.

CCE 12.6(2) introduces the following enhancements for AppDynamics monitoring:

Support for Windows Event Log monitoring in Unified ICM 12.6(2). You can enable this monitoring service while enabling AppDynamics
                                    monitoring for Unified ICM 12.6(2). If you have configured AppDynamics for Unified ICM 12.6(1), then post upgrade to 12.6(2),
                                    you must disable and re-enable AppDynamics to enable Windows Event Log Monitoring. Administrator must provide the AppDynamics
                                    controller username and password to enable Windows Event Log Monitoring on Unified ICM. For more information, see the Enable Performance Monitoring section in the Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise . You can also check if the Windows Event Log Monitoring service is enabled or disabled using the status CLI. For more information,
                                    see the Check Status of Performance Monitoring section in the Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise .

App Monitoring Proxy Set and Show CLIs introduced in 12.6(1) are removed in 12.6(2). App Monitoring enable CLI now provides
                                    an option to configure Proxy Host and Proxy Port. App Monitoring status CLI shows the proxy enabled status. The option to
                                    configure Proxy User Name and Proxy Password is removed in 12.6(2). For more information, see the Enable Performance Monitoring and Check Status of Performance Monitoring sections in the Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise .

If Cloud Connect is on 12.6(2) and the target Windows and VOS nodes are on 12.6(1) during stagewise upgrade, ensure the required
                                    ESs and COP are applied in respective 12.6(1) target nodes. For more information, see the CCE Serviceability and Monitoring using AppDynamics chapter in Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise .

When you install CCE 12.6(2)_ES37 , the AppDynamics agents deployed on the CCE VMs are upgraded to the following latest versions:

Agent

Version

DotNet

24.3

Machine

24.3

Java

24.3

CCE supports SaaS and On-Premise AppDynamics controller over secure connection only. For the supported On-Premise AppDynamics
                                                controller version, see the CCE Serviceability and Monitoring using AppDynamics chapter in Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise .

AppDynamics monitoring for VVB-Admin and Finesse-Notification Java App Agents is not supported in 12.6(2). Post upgrade from
                                                12.6(1) to 12.6(2), you will still see the VVB-Admin and Finesse-Notification services in the AppDynamics controller. But
                                                the metrics will not be received from the respective 12.6(2) nodes. You can right-click these services and remove them from
                                                the AppDynamics controller.

### Inactivity Timer

Administrators can now configure the inactivity timeout for a session to avoid being logged out after 30 minutes of inactivity.
                              Navigate to the Unified CCE Administration Portal > Call Settings > Miscellaneous > Global > Login Session > Session Inactivity Timeout to set the inactivity time.

This feature is only applicable for sessions where administrators are using the Unified CCE Administration Console and does
                                          not apply to agent sessions in Finesse Desktop and ECE.

For more information, see the following guides:

The System Setting for Unified CCE Deployment section in the Administration Guide for Cisco Unified Contact Center Enterprise Release, 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html

The Miscellaneous section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

### Support for Third Party Gateways

Administrators can now add third-party gateways to the inventory for routing calls. For instructions, see the Optional Configurations section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide .

Cisco does not test or provide support for these third-party gateways.

### Agent Multi-Edit Attribute

Administrators and supervisors can now edit multiple attributes for a set of agents at the same time. Ensure that the agents
                              belong to the same site and department. The agents can also be global agents.

For instructions, see the Agent Multi Edit Attribute section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide .

For instructions, see the Manage Agents section in the Administration Guide for Cisco Unified Contact Center Enterprise .

### Graceful Shutdown on Router (ES68)

This feature requires ICM12.6.2_ES68 to be installed on the 12.6(2) target system.

In 12.6(2), you can leverage the capabilities of graceful shutdown on Routers only if you apply the ICM12.6.2_ES68 patch.

Maintenance mode is only supported when both Side A and Side B Routers are on version 12.6(2).

Apply the ICM12.6.2_ES68 to both Side A and Side B of the Router to ensure that the maintenance mode takes effect. Failing to apply the patch to either
                                                side will result in the transition to maintenance mode getting rejected.

For more information, see the Graceful Shutdown section in the following guides:

Administration Guide for Cisco Unified Contact Center Enterprise Release, 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide Release, 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

## Important Notes

### Support for Microsoft Windows 11 (64 bit)

CCE supports the Microsoft Windows 11 (64 bit) operating system for Administration Client and Internet Script Editior (ISE)
                                 components.

### RAM and Mandatory ES for Cloud Connect

Cloud Connect 12.6(2) requires 16 GB of RAM. For details, see the Cloud Connect Virtualization page.

CCE 12.6(2) ES03 or later is required to optimize the functionality of Cloud Connect 12.6(2).

Ensure you increase the RAM and then apply the ES before upgrading to Cloud Connect 12.6(2).

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

### OpenJDK Java Runtime Update

The CCE 12.6(2) installer installs the OpenJDK version 1.8 (32-bit), update 432. If the existing Oracle JRE is not needed,
                              you may uninstall it from the system manually.

Install the most recent ES patch to obtain OpenJDK version 1.8 (32-bit) update 432.

For more information, see the following documents:

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide

Security Guide for Cisco Unified ICM/Contact Center Enterprise

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide

For information about supported Java versions, see the Contact Center Enterprise Solution Compatibility Matrix .

### Tomcat Upgrade

Tomcat is upgraded to 9.0.111. For details on how to apply later security patches on Tomcat 9, refer to the Upgrade Tomcat Utility section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise .

Install the most recent ES patch to obtain Tomcat 9.0.111.

### Account Lockout Support for Active Directory

The account lockout mechanism is now supported for Microsoft Active Directory users of the following applications:

Unified CCE Administration portal

Web Setup tool

Diagnostic Portico web service

For more information, see the following documents:

The Active Directory Deployment section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise .

The Active Directory and ICM/CCE section in the Staging Guide for Cisco Unified ICM/Contact Center Enterprise .

### CUIC Co-resident Compatibility

CUIC Co-resident Live Data can be used on 12.6(2) when the CCE Central Controller/AW is on 12.6(1). However, if both Live
                              Data and CCE Central Controller/AW are on 12.6(2), then the ports used in Live Data will change. Releases earlier than 12.6(2)
                              use ports 12005 and 12008; 12.6(2) and later releases use port 443.

## Deprecated Features

Deprecated features are fully supported. However, there is no additional development for deprecated features. These features
                           may be scheduled to be removed in a future release. Plan to transition to the designated replacement feature. If you are implementing
                           a new deployment, use the replacement technology rather than the deprecated feature.

Deprecated Feature

Announced

Replacement

Notes

ECSPIM/Avaya (Definity) PG using CVLAN interface

11.5(1)

Migrate to Contact Center Enterprise or Webex Contact Center Enterprise

None

TAESPIM/Avaya (Definity) PG using TSAPI interface

12.6(2)

Migrate to Contact Center Enterprise or Webex Contact Center Enterprise

None

Unified Intelligent Contact Management (ICM) deployments including all NICs

12.6(2)

None

INCRP NIC is the only exception, as it will continue to be used for routing calls between two Unified CCE instances and in
                                       Contact Director deployments.

Unified CCE System PG

12.6(2)

Agent PG and VRU PG

None

12.6(2)

Cisco Finesse on Unified CCE or Packaged CCE deployments

None

12.6(2)

None

None

Microsoft Windows Server 2016

12.6(2)

Microsoft Windows Server 2019

None

Microsoft SQL Server 2017

12.6(2)

Microsoft SQL Server 2019

None

Webex Experience Management

12.6(2)

None

None

UCC Enterprise Gateway PG (Parent PG in Parent-Child deployments)

12.5(1)

None

None

## Removed and Unsupported Features

The features listed in the following table are no longer available.

Feature

Effective from Release

Replacement

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

App Monitoring for VVB-Admin JVM App Agent

12.6(2)

NA

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

For the list of third-party softwares, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.

| Feature | Unified CCE | Packaged CCE |
|---|---|---|
| Identity Token Authentication and Automated Identity Token Rotation for Cisco Devhub Artifactory | Yes | Yes |
| Enhanced Secure Communication across CCE Components (ES102, ES103, ES108) | Yes | Yes |
| Configure Custom SQL Server Port (ES98 and ES100) | Yes | Yes |
| Connect with business through digital channels using Webex Connect | Yes | Yes |
| Support for WhatsApp, Facebook Messenger, and Apple Messages for Business Digital Channels | Yes | Yes |
| Support for ECE and Webex Connect Digital Channels in the Same Deployment | Yes | No |
| Digital Channels Anti-Malware Capabilities | Yes | Yes |
| Agent Request or Web Callback using Webex Connect | Yes | Yes |
| Virtual Agent-Voice Call Transcription | Yes | Yes |
| Preflight request for Private Network Access | Yes | Yes |
| License Reservation | Yes | Yes |
| HTTP Strict Transport Security Support for Unified CCE Web Applications | Yes | Yes |
| Custom Truststore to Store Component Certificates | Yes | Yes |
| JTAPI credentials encryption (ES 35) | Yes | Yes |
| Support for 48000 Agents (ES04 and ES 25) | Yes | No |

| Note | This feature is available only if you install the Cloud Connect 12.6(2) ES04 https://software.cisco.com/download/home/268439622/type/286325642/release/12.6(2)ES4 . |
|---|---|

| Note | This feature is available only if you install the following installer or later cummulative ES releases: For Logger and Router, install ICM12.6.2_ES98 . For AW and Administration Client, install ICM12.6.2_ES100 . For CUIC, install CUIC.1262.ES04 COP. You can configure a custom SQL Server port for all CCE agent deployments. The custom SQL Server port is supported on CCE databases and can be configured across Cisco Finesse, CUIC, Live Data, and
                                                Administration Client components that connect to these databases. However, it cannot be configured to Enterprise Chat and
                                                Email (ECE),  Contact Center Management Portal (CCMP), and Cloud Connect (for Digital Channels) for connection to CCE databases. The Custom SQL Server port feature will be supported for Cloud Connect (Digital Channels) as part of CSCwr89012. |
|---|---|

| Note | This feature is not supported in Packaged CCE deployments. A maximum of 400 agents can handle tasks from both ECE and Webex Connect Digital Channels at the same time. This 400-limit
                                                only applies to agents with both ECE and Webex Connect channels enabled, regardless of whether ECE is in a co-located 400
                                                agent deployment or a distributed 2500 agent deployment. Ensure that ECE is configured within the configuration limits defined for your deployment type. This also means that the limits
                                                that apply to ECE also apply to the combination of ECE and Webex Connect. For more information on the configuration limits, see all limits defined for ECE in the Configuration Limits and Feature Availability for Reference Designs chapter in the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html |
|---|---|

| Note | This feature is available to customers on request and only after necessary review and agreement. Please contact your Partner
                                          or Customer Success Manager or Cisco Support for details. |
|---|---|

| Note | The system accepts only the value true for disabling the feature or it remains in its default enabled state. |
|---|---|

| Important | Use CCE_JAVA_HOME if upgrading from Unified CCE 12.5(1a) or Unified CCE 12.5(1) with ES55 (mandatory OpenJDK ES). |
|---|---|

| Feature | Unified CCE | Packaged CCE |
|---|---|---|
| Disabling Personal Callback Reattempt | Yes | Yes |
| Simplified upgrade | Yes | Yes |
| AppDynamics built-in integration with CCE | Yes | Yes |
| Inactivity Timer | Yes | Yes |
| Support for Third Party Gateways | No | Yes |
| Agent Multi Edit Attribute | Yes | Yes |
| Graceful Shutdown on Router | Yes | Yes |

| Note | To leverage this feature in the Unified CCE 12.6(2), install the Unified CCE 12.6(2) ICM12.6.2_ES85 for Router or Logger, or install the Unified CCE 12.6(2) ICM12.6.2_ES86 for PG. |
|---|---|

| Note | Software download will not be initiated during Cloud Connect restart. |
|---|---|

| Agent | Version |
|---|---|
| DotNet | 24.3 |
| Machine | 24.3 |
| Java | 24.3 |

| Note | CCE supports SaaS and On-Premise AppDynamics controller over secure connection only. For the supported On-Premise AppDynamics
                                                controller version, see the CCE Serviceability and Monitoring using AppDynamics chapter in Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise . AppDynamics monitoring for VVB-Admin and Finesse-Notification Java App Agents is not supported in 12.6(2). Post upgrade from
                                                12.6(1) to 12.6(2), you will still see the VVB-Admin and Finesse-Notification services in the AppDynamics controller. But
                                                the metrics will not be received from the respective 12.6(2) nodes. You can right-click these services and remove them from
                                                the AppDynamics controller. |
|---|---|

| Note | This feature is only applicable for sessions where administrators are using the Unified CCE Administration Console and does
                                          not apply to agent sessions in Finesse Desktop and ECE. |
|---|---|

| Note | This feature requires ICM_12.6(2) _ES9 to be installed on the 12.6(2) target system. |
|---|---|

| Note | This feature requires ICM_12.6(2) _ES9 to be installed on the 12.6(2) target system. |
|---|---|

| Note | Cisco does not test or provide support for these third-party gateways. |
|---|---|

| Note | This feature requires ICM_12.6(2) _ES9 to be installed on the 12.6(2) target system. |
|---|---|

| Note | This feature requires ICM12.6.2_ES68 to be installed on the 12.6(2) target system. |
|---|---|

| Note | Maintenance mode is only supported when both Side A and Side B Routers are on version 12.6(2). Apply the ICM12.6.2_ES68 to both Side A and Side B of the Router to ensure that the maintenance mode takes effect. Failing to apply the patch to either
                                                side will result in the transition to maintenance mode getting rejected. |
|---|---|

| Note | Install the most recent ES patch to obtain OpenJDK version 1.8 (32-bit) update 432. |
|---|---|

| Note | Install the most recent ES patch to obtain Tomcat 9.0.111. |
|---|---|

| Deprecated Feature | Announced | Replacement | Notes |
|---|---|---|---|
| ECSPIM/Avaya (Definity) PG using CVLAN interface | 11.5(1) | Migrate to Contact Center Enterprise or Webex Contact Center Enterprise | None |
| TAESPIM/Avaya (Definity) PG using TSAPI interface | 12.6(2) | Migrate to Contact Center Enterprise or Webex Contact Center Enterprise | None |
| Unified Intelligent Contact Management (ICM) deployments including all NICs | 12.6(2) | None | INCRP NIC is the only exception, as it will continue to be used for routing calls between two Unified CCE instances and in
                                       Contact Director deployments. |
| Unified CCE System PG | 12.6(2) | Agent PG and VRU PG | None |
| CTI OS | 12.6(2) | Cisco Finesse on Unified CCE or Packaged CCE deployments | None |
| Contact Share | 12.6(2) | None | None |
| Microsoft Windows Server 2016 | 12.6(2) | Microsoft Windows Server 2019 | None |
| Microsoft SQL Server 2017 | 12.6(2) | Microsoft SQL Server 2019 | None |
| Webex Experience Management | 12.6(2) | None | None |
| UCC Enterprise Gateway PG (Parent PG in Parent-Child deployments) | 12.5(1) | None | None |

| Feature | Effective from Release | Replacement |
|---|---|---|
| Integrity Check Tool | 12.6(2) | None |
| External Script Validation | 12.6(2) | None |
| Translation Route Wizard | 12.6(2) | Translation Route Explorer |
| Generic PG | 12.6(2) | Agent PG and VRU PG |
| App Monitoring for VVB-Admin JVM App Agent | 12.6(2) | NA |
| Cisco Hosted Collaboration Solution for Contact Center (HCS for CC) | 12.6(1) | Unified CCE or Webex CCE. |
| MIB Objects: cccaDistAwWebViewEnabled cccaDistAwWebViewServerName cccaSupportToolsURL cccaDialerCallAttemptsPerSec | 12.6(1) | None |
| "Sprawler" deployment | 12.6(1) | Packaged CCE deployment |
| Shared ACD Line | 12.6(1) | Agent Device Selection Note For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . | Note | For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |
| Note | For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |
| Avaya Aura Contact Center (AACC - formerly Symposium) PG | 12.5(2) | Migrate to Contact Center Enterprise or Webex CCE. |
| Aspect PG | 12.5(2) | Migrate to Contact Center Enterprise or Webex CCE. |
| Symposium ACD | 12.5(2) | Migrate to Contact Center Enterprise or Webex CCE. |
| Customer Journey Analyzer for Business Metrics (Trials) | 12.5(2) | None Note Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued. | Note | Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued. |
| Note | Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued. |
| Internet Explorer 11 | 12.5(2) | Edge Chromium (Microsoft Edge) |

| Note | For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |
|---|---|

| Note | Customer Journey Analyzer was available for trials only in Release 12.5(1). The trials have been discontinued. |
|---|---|