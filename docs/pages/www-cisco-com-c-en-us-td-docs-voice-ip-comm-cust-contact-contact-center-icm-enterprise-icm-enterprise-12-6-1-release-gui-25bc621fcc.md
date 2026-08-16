---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-release-gui-25bc621fcc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/release/guide/rcct_b_cce-solution-rns-12-6/rcct_m_cce-solutions-12-6.html
retrieved_at: 2026-08-16T19:38:04.112795+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

# Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

Updated: May 14, 2021

Chapter: Contact Center Enterprise Solutions

## Chapter: Contact Center Enterprise Solutions

# Contact Center Enterprise Solutions

## New Features

The following table lists the new features available for each Contact Center Enterprise solution in Release 12.6(1).

Feature

Unified CCE

Packaged CCE

VPN-less Access to Finesse Desktop (For Agents and Supervisors)

Yes

Yes

Agent Answers

Yes

Yes

Edge Chromium Browser Support

Yes

Yes

Yes

Yes

Graceful Shutdown

Yes

Yes

Yes

Yes

Support for 36000 Agents

Yes

Custom Truststore to Store Component Certificates

Yes

Yes

vMotion

Yes

Yes

Dual Platform Support

Yes

Yes

ECDSA Certificates

Yes

Yes

Yes

Yes

### Authentication for Reverse-Proxy Connections (ES02 Update)

Finesse introduces authentication at the edge for the reverse-proxy. Authentication is supported for both SSO and Non-SSO
                                 deployments. Authentication is enforced for all requests and protocols that are accepted at the proxy before they are forwarded
                                 to the respective component servers (Finesse, IdS, CUIC, and IdP). The component servers also enforce authentication locally.
                                 All authentications made at the proxy use the Finesse login credentials, irrespective of the component server to which the
                                 requests are made. For more information on authentication, see the Authentication topic under the VPN-Less Access to Finesse Desktop section in the Cisco Unified Contact Center Enterprise Features Guide . For complete list of enhancements to the VPN-Less configuration, refer to the Nginx TechNote article .

### Configurable Reverse-Proxy Host Verification (ES03 Update)

You can enable and disable SSL certificate verification for connections that are established from reverse-proxy hosts to Cisco
                                 Web Proxy Service by using the utils system reverse-proxy client-auth CLI command. For more information about reverse-proxy host authentication see the Configure Reverse-Proxy Host Authentication section in Cisco Unified Contact Center Enterprise Features Guide .

### VPN-less Access to Finesse Desktop (For Agents and Supervisors)

This feature provides the flexibility for agents and supervisors to access the Finesse desktop from anywhere through the Internet
                              without requiring VPN connectivity to the enterprise data center. To enable this feature, a reverse-proxy pair must be deployed in the DMZ. For more information on
                                 this feature, see the Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) and Security Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1) .

Media access remains unchanged in reverse-proxy deployments. To connect to the media, agents and supervisors can use Cisco
                              Jabber over MRA or the Mobile Agent capability of Contact Center Enterprise with a PSTN or mobile endpoint.

To use VPN-less access to Finesse desktop, you must upgrade Finesse, IdS, and CUIC to Release 12.6(1) ES02 or above. If you
                              are using Unified CCE 12.6(1), you must upgrade Live Data to 12.6(1) ES02 or above. You can access the 12.6(1) ES03 Release
                              and Readme from the following locations:

Finesse 12.6(1) ES

CUIC/LD/IdS 12.6(1) ES

For Nginx-based reverse-proxy rules, installation, configuration, and security hardening instructions, refer to the Nginx TechNote article . Any reverse-proxy supporting the required criteria (as mentioned in the Reverse-Proxy Selection Criteria section of Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) ) can be used in place of Nginx for supporting this feature.

If CORS status is "enabled", you must explicitly add the reverse-proxy domain name to the list of CORS trusted domain names.

### Agent Answers

Unified CCE leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to provide services that assist agents.
                              These Contact Center AI services are available for the agents through the Agent Answers gadget and the Call Transcript gadget
                              on the Cisco Finesse desktop.

The Agent Answers gadget displays relevant suggestions and recommendations in real time for the agent to consider. The suggestions
                              and recommendations are based on the ongoing conversation between the caller and the agent. Agent Answers enhances the customer
                              experience because the timely suggestions improve the ability of the agent to respond.

The Call Transcript gadget dynamically converts the ongoing voice conversation to text and presents the text to an agent for
                              real-time viewing and reference.

For details on how to configure the Agent Answers and Call Transcription features, see the Agent Answers and the Call Transcription chapters in the following documents:

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

For information on the design considerations of the Agent Answers and Call Transcription features, see the Contact Center AI Services Considerations section in following documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

Solution Design Guide for Cisco Packaged Contact Center Enterprise, Release 12.6 at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html

To enable Agent Answers or Call Transcript features, ensure your Cisco Unified CVP is on 12.6(1) ES 06, Cisco Finesse is on
                                          12.6(1) ES 01, and Cloud Connect is on 12.6.

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge) . For more information, see the Supported Browsers section in the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Simplified Upgrade

The Orchestration feature provides partners and administrators an option to automatically
                              download software updates and simplify the installation and rollback processes.
                              Integration of Graceful Shutdown feature within the Orchestration framework ensures that
                              the software updates are updated with minimal downtime. The Orchestration framework is
                              built within the Cloud Connect server that connects to the Cisco-hosted cloud software
                              repository. This framework provides the ability to check and download new software
                              updates as and when they are available and notify the administrators via email about the
                              new updates along with the release notes. Orchestration currently supports installation
                              and rollback of Cisco Engineering Specials (ES), Service Updates (SU), Minor Releases
                              (MR), and Microsoft Patches.

Cloud Connect server version 12.6(1) supports Orchestration in the following
                              scenarios:

CCE 12.5(x) ES, 12.6(x) ES and Windows Updates can be orchestrated from 12.6(x)
                                    Cloud Connect server

CCE 12.5(1) to 12.5(2) or 12.6(1) software upgrade can be orchestrated from
                                    12.6(x) Cloud Connect server

ICM 12.5(2) to 12.6(1) upgrade is not supported either manually or via
                                                orchestration.

Apply the mandatory patch on Cloud Connect to Orchestrate 12.5(2) ES and
                                                software upgrade.

The following are the known limitations:

Orchestration is not supported for Tech Refresh and fresh install.

Orchestration is not supported for Cisco Customer Collaboration Platform (CCP),
                                    Cisco Enterprise Chat and Email (ECE), Cisco Unified Contact Center Domain
                                    Manager (CCDM), Cisco Unified Contact Center Management Portal (CCMP), and
                                    non-Contact Center Cisco products such as Cisco Unified Communications Manager
                                    (CUCM), IM&P etc.

The administrators should read the release notes specifically for ES releases that are notified via email to understand the
                                    dependency on each component. The Orchestration framework does not track this aspect automatically. For example, if an ES
                                    of Finesse has a dependency on an ES of Live Data and has to be installed in a specific order, then the administrator should
                                    consider this before initiating the patch installation from the Cloud Connect server.

Only Microsoft Exchange Server is supported for email notification; Office 365
                                    and Gmail are not supported as of now.

Orchestration is not supported for 12000, 24000, and 36000 agent deployment
                                          models.

### Graceful Shutdown

Graceful shutdown allows you to perform firmware upgrades, apply security patches, and apply Engineering Specials (ES) without
                              the need for a maintenance window. With this feature, active calls and sessions are transitioned over to secondary or redundant
                              components before an upgrade process is initiated on the target system. Agent states, call states, and call context are maintained.
                              Operations such as reskilling and changing an agent's team membership are not affected.

For more information, see the following documents:

Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

### AppDynamics Native Integration with CCE

For Cisco Contact Center Enterprise solution, it is important to have continuous and
                              seamless monitoring of the deployed solution and automated alerting when anomalies are
                              detected. AppDynamics provides a solution for application and platform performance
                              monitoring that helps to achieve the following:

Platform, application, and End User Monitoring (EUM) through dashboards and
                                    metrics.

Automated alerting mechanism in case of anomaly detection.

For ordering and setting up AppDynamics SAAS controller, please contact appd_ucce_sales@cisco.com

For AppDynamics, CCE supports SaaS and On-Prem controller (version 21.4.10-24683)
                                             over secure connection only.

### Support for 36000 Agents

You can modify your existing 24000 agent reference design to scale up to 36000 agents. This is accomplished by adding more
                              peripheral VMs and peripheral gateways to the deployment and modifying specific configuration limits. You must also modify
                              the OVA files for Live Data and Cisco Identity Service (IdS).

For more information about configuring your solution for 36000 agents, see the following documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center at https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/products-implementation-design-guides-list.html .

For more details, see the Scale up to 36000 Agents topic in the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

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

### vMotion

Cisco Contact Center Enterprise solution components now support vMotion of live virtual machines (VMs) on Cisco Hyperflex
                              servers. VMware vMotion enables the live migration of running VMs from one physical server to another with zero downtime,
                              continuous service availability, and complete transaction integrity. vMotion is a key enabling technology for creating dynamic,
                              automated, and self-optimizing data centers.

### Dual Platform Support

Contact Center Enterprise (CCE) components supports the following platforms:

Microsoft Windows Server 2016 and Microsoft SQL Server 2017

Microsoft Windows Server 2019 and Microsoft SQL Server 2019

The cross combination of platforms is not supported. For example, Windows Server 2016
                                          with SQL Server 2019 or Windows Server 2019 with SQL Server 2017 is not
                                          supported.

For more information, see the Install Microsoft Windows Server section in the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

### ECDSA Certificates

This release supports Elliptic Curve Digital Signature Algorithm (ECDSA) certificate,
                              which can be enabled in Unified CCE, Cisco Unified CVP, Cisco Finesse, Cloud Connect,
                              CUIC, Cisco VVB, Cisco IdS, and ECE.

For details on how to enable ECDSA, see Enabling ECDSA for Unified CCE Solution in Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

To enable ECDSA certificate, the following solution components in the specified versions,
                              and the respective Engineering Specials (ES) are required. You have to install the below
                              ESes in the order listed:

### Webex Workforce Optimization (WFO) Support with Contact Center Enterprise (CCE) Solutions

The Contact Center Enterprise (Unified CCE/Packaged CCE/Webex CCE) solutions supports the Webex Workforce Optimization offering. See https://www.cisco.com/c/en/us/support/contact-center/webex-workforce-optimization/series.html .

## Updated Features

The following table lists the updated features available for each Contact Center Enterprise solution in Release 12.6(1).

Feature

Unified CCE

Packaged CCE

Webex Experience Management Integration with Post Call Survey

Yes

Yes

SMS and Email Survey after Voice

Yes

Yes

Non-Production System (NPS)

Yes

Yes

Database Schema Changes

Yes

Yes

Password Hashing

Yes

Yes

Diagnostic Framework Portico

Yes

Yes

Increased PG Agent Capacity for Mobile Agents

Yes

Yes

Enable or Disable Outbound Dialer from Redialing Failed Personal Callbacks (ES65 Update)

Yes

Yes

Inactivity Timer

Yes

Yes

### Webex Experience Management Integration with Post Call Survey

The Voice surveys can be triggered through Webex Experience Management or by using the traditional Post Call Survey (using
                              CVP IVR).

Webex Experience Management surveys use the same scripting and call flows as Post Call Survey, except that the Questionnaire
                              is provided by the cloud-based Experience Management service. The Call Studio survey application, to be invoked, is configured
                              in the router script that runs during the survey leg of the call, and is passed to the CVP through an ECC variable.

The Call Studio application fetches the questions from the Experience Management service, collects the answers from the caller,
                              and submits them to the Experience Management service over REST APIs.

For more information on how to configure Experience Management , see the Webex Experience Management Integration chapter in the following documents:

Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

Experience Management is supported in all the deployment types. For more information on the call flow and design considerations, see the following
                              documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html

### Increased PG Agent Capacity for Mobile Agents

The mobile agent capacity on the PG are as follows:

2000 with nailed-up connections (1:1)

1500 with nailed-up connections if the average handle time is less than 3 minutes, or if agent greeting or whisper announcement
                                    features are used with the mobile agent (1.3:1)

1500 with call-by-call connections (1.3:1)

For more details, see the PG Agent Capacity with Mobile Agents section in the Sizing and Operating Conditions for Reference Designs chapter in the following documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

Solution Design Guide for Cisco Packaged Contact Center Enterprise, Release 12.6 at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html

### SMS and Email Survey after Voice

Cisco Webex Experience Management (referred to as Experience Management) , introduced in 12.5(1), is a Customer Experience Management (CEM) solution that allows you to see your business from the perspective of your customers.

In 12.6(1), this feature is extended to SMS and Email. Customers can participate in surveys using the links sent over SMS or email. The survey results help the agents and the supervisors
                              to offer more personalized and contextual experience to the customers.

Administrators can configure and customize the survey in the Experience Management console. The responses are displayed on the Customer Experience Journey gadget in the Finesse.

For more information, refer to the section Webex Experience Management Integration in the following documents:

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

### Non-Production System (NPS)

In this release, Non-Production System (NPS) usage mode is introduced to give you more control on license usage. With NPS,
                              you can switch from production deployment to other deployment types such as lab, testing, and staging.

For more information, refer to the section Smart Licensing in one of the following documents:

Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html

Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

### Database Schema Changes

#### Unified CCE Database Schema Changes

This release introduces minor database schema changes. The release includes changes to these tables:

Table

Changes

Smart_License_Server

Added the following columns to the existing table.

UsageMode

SlrEnabled

SlrStatus

As part of Agent Answers added new tables:

Default_Configuration

Agent_Service_Enabled

-

Call_Type

Added a new column called CCAIConfigParamter.

Termination_Call_Detail

Added the following columns to the existing table.

AgentAnswersEnabled

AgentTeamID

ICR_Globals

Added a new column called GlobalSecureFlag.

### Password Hashing

This release includes a key security update which allows more secure hashing for agent and
                              supervisor passwords in the non-SSO mode.

A Global switch is introduced in the Manage Security tab on Unified CCE Administration console to enforce SHA-256 hashing. When the switch is turned on, the MD5-based hashes
                              are removed. The administrator must re-enter the passwords in the Unified CCE Administration console/Configuration Manager.
                              Then the passwords are hashed with SHA-256 algorithim. For more information on how to enable or disable the global switch
                              see one of the following documents:

Cisco Unified Contact Center Enterprise Developer Reference Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html

Cisco Packaged Contact Center Enterprise Developer Reference Guide at https://d1nmyq4gcgsfi5.cloudfront.net/site/packaged-contact-center/documentation/

### Diagnostic Framework Portico

The Unified ICM/Unified CCE Diagnostic Framework Portico has moved to form-based authentication for login. It has a new login
                              page, an option to log out, and a 30 minute session timeout.

The GetMenu URL is now deprecated.

For more information, see Diagnostic Tools section in the Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

### Enhanced Database Migration Tool (EDMT) Support

EDMT is used for seamlessly migrating data across different versions.

During the upgrade from 12.0(1) and 12.5(1) to 12.6(1), you can use EDMT 12.6(1) for data migration and synchronization.

You can also use EDMT 12.6(1), during the Technology Refresh migration from Windows Server 2016 to Windows Server 2019 on
                              12.6(1).

For more information on EDMT, see the following documents:

Cisco Unified Contact Center Installation and Upgrade Guide: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Cisco Packaged Contact Center Installation and Upgrade Guide: https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

### Enable or Disable Outbound Dialer from Redialing Failed Personal Callbacks (ES65 Update)

You can now update the Dialer registry settings to enable or disable the outbound Dialer from retrying or redialing failed
                              personal callbacks with dialing errors (where the CallResult value is 2).

For more information, see the Dialer Registry Settings section in the Cisco Unified Contact Center Enterprise Outbound Options Guide .

### Inactivity Timer

Administrators can now configure the inactivity timeout for a session to avoid being logged out after 30 minutes of inactivity.
                              Navigate to the Unified CCE Administration Portal > Call Settings > Miscellaneous > Global > Login Session > Session Inactivity Timeout to set the inactivity time.

This feature is only applicable for sessions where administrators are using the Unified CCE Administration Console and does
                                          not apply to agent sessions in Finesse Desktop and ECE.

For more information, see the following guides:

The System Setting for Unified CCE Deployment section in the Administration Guide for Cisco Unified Contact Center Enterprise Release, 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html

The Miscellaneous section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

## Important Notes

### IdS Upgrade

If you are upgrading Cisco Identity Service (IdS) to 12.6(1) and above, after the upgrade, you must reestablish trust relationship
                                 between the Identity Provider (IdP) and the IdS. This step is not required if you are using Microsoft ADFS as the IdP.

### OpenJDK Java Runtime Update

CCE has transitioned from Oracle to OpenJDK for the Java runtime environment (JRE). The CCE 12.6(1) installer will install
                              the required OpenJDK version. If the existing Oracle JRE is not needed, you may uninstall it from the system manually.

For more information, see the following documents:

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

For information about supported Java versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

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

### Tomcat Utility Changes

The -revert command, which was used to revert Tomcat to its previous version, is removed. To revert Tomcat to a previous version, run
                              the Tomcat utility with the installer of that Tomcat version.

For more information, see the Security Guide for Cisco Unified ICM/Contact Center Enterprise: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Deprecated Features

Deprecated features are fully supported. However, there is no additional development for deprecated features. These features
                           may be scheduled to be removed in a future release. Plan to transition to the designated replacement feature. If you are implementing
                           a new deployment, use the replacement technology rather than the deprecated feature.

Deprecated Feature

Announced in Release

Replacement

Notes

UCC Enterprise Gateway PG (Parent PG in Parent-Child deployments)

12.5(1)

None

None

Integrity Check Tool

12.0(1)

None

None

External Script Validation

12.0(1)

None

None

Translation Route Wizard

12.0(1)

Translation Route Explorer

None

Generic PG

11.5(1)

Agent PG and VRU PG

None

ECSPIM/Avaya (Definity) PG using CVLAN interface

11.5(1)

TAESPIM/Avaya (Definity) PG using TSAPI interface

CVLAN interface is deprecated by vendor with limited or no active development support

Webex Experience Management

14 November, 2022

None

Experience Management integration planned.

## Removed and Unsupported Features

The features listed in the following table are no longer available.

Feature

Effective from Release

Replacement

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

For information about third-party software, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

| Feature | Unified CCE | Packaged CCE |
|---|---|---|
| VPN-less Access to Finesse Desktop (For Agents and Supervisors) | Yes | Yes |
| Agent Answers | Yes | Yes |
| Edge Chromium Browser Support | Yes | Yes |
| Simplified Upgrade | Yes | Yes |
| Graceful Shutdown | Yes | Yes |
| AppDynamics Native Integration with CCE | Yes | Yes |
| Support for 36000 Agents | Yes |  |
| Custom Truststore to Store Component Certificates | Yes | Yes |
| vMotion | Yes | Yes |
| Dual Platform Support | Yes | Yes |
| ECDSA Certificates | Yes | Yes |
| WFO Support | Yes | Yes |

| Note | For Nginx-based reverse-proxy rules, installation, configuration, and security hardening instructions, refer to the Nginx TechNote article . Any reverse-proxy supporting the required criteria (as mentioned in the Reverse-Proxy Selection Criteria section of Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) ) can be used in place of Nginx for supporting this feature. If CORS status is "enabled", you must explicitly add the reverse-proxy domain name to the list of CORS trusted domain names. |
|---|---|

| Note | To enable Agent Answers or Call Transcript features, ensure your Cisco Unified CVP is on 12.6(1) ES 06, Cisco Finesse is on
                                          12.6(1) ES 01, and Cloud Connect is on 12.6. |
|---|---|

| Note | ICM 12.5(2) to 12.6(1) upgrade is not supported either manually or via
                                                orchestration. Apply the mandatory patch on Cloud Connect to Orchestrate 12.5(2) ES and
                                                software upgrade. |
|---|---|

| Note | Orchestration is not supported for 12000, 24000, and 36000 agent deployment
                                          models. |
|---|---|

| Note | For AppDynamics, CCE supports SaaS and On-Prem controller (version 21.4.10-24683)
                                             over secure connection only. |
|---|---|

| Important | Use CCE_JAVA_HOME if upgrading from Unified CCE 12.5(1a) or Unified CCE 12.5(1) with ES55 (mandatory OpenJDK ES). |
|---|---|

| Note | The cross combination of platforms is not supported. For example, Windows Server 2016
                                          with SQL Server 2019 or Windows Server 2019 with SQL Server 2017 is not
                                          supported. |
|---|---|

| Feature | Unified CCE | Packaged CCE |
|---|---|---|
| Webex Experience Management Integration with Post Call Survey | Yes | Yes |
| SMS and Email Survey after Voice | Yes | Yes |
| Non-Production System (NPS) | Yes | Yes |
| Database Schema Changes | Yes | Yes |
| Password Hashing | Yes | Yes |
| Diagnostic Framework Portico | Yes | Yes |
| Increased PG Agent Capacity for Mobile Agents | Yes | Yes |
| Enable or Disable Outbound Dialer from Redialing Failed Personal Callbacks (ES65 Update) | Yes | Yes |
| Inactivity Timer | Yes | Yes |

| Table | Changes |
|---|---|
| Smart_License_Server | Added the following columns to the existing table. UsageMode SlrEnabled SlrStatus |
| As part of Agent Answers added new tables: Default_Configuration Agent_Service_Enabled | - |
| Call_Type | Added a new column called CCAIConfigParamter. |
| Termination_Call_Detail | Added the following columns to the existing table. AgentAnswersEnabled AgentTeamID |
| ICR_Globals | Added a new column called GlobalSecureFlag. |

| Note | The GetMenu URL is now deprecated. |
|---|---|

| Note | For more information, see Diagnostic Tools section in the Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
|---|---|

| Note | This feature is only applicable for sessions where administrators are using the Unified CCE Administration Console and does
                                          not apply to agent sessions in Finesse Desktop and ECE. |
|---|---|

| Note | This feature requires ICM_12.6(2) _ES9 to be installed on the 12.6(2) target system. |
|---|---|

| Deprecated Feature | Announced in Release | Replacement | Notes |
|---|---|---|---|
| UCC Enterprise Gateway PG (Parent PG in Parent-Child deployments) | 12.5(1) | None | None |
| Integrity Check Tool | 12.0(1) | None | None |
| External Script Validation | 12.0(1) | None | None |
| Translation Route Wizard | 12.0(1) | Translation Route Explorer | None |
| Generic PG | 11.5(1) | Agent PG and VRU PG | None |
| ECSPIM/Avaya (Definity) PG using CVLAN interface | 11.5(1) | TAESPIM/Avaya (Definity) PG using TSAPI interface | CVLAN interface is deprecated by vendor with limited or no active development support |
| Webex Experience Management | 14 November, 2022 | None | Experience Management integration planned. |

| Feature | Effective from Release | Replacement |
|---|---|---|
| Cisco Hosted Collaboration Solution for Contact Center (HCS for CC) | 12.6(1) | Unified CCE or Webex CCE. |
| MIB Objects: cccaDistAwWebViewEnabled cccaDistAwWebViewServerName cccaSupportToolsURL cccaDialerCallAttemptsPerSec | 12.6(1) | None |
| "Sprawler" deployment | 12.6(1) | Packaged CCE deployment |
| Shared ACD Line | 12.6(1) | Agent Device Selection Note For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . | Note | For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |
| Note | For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |
| ECSPIM/Avaya (Definity) PG using CVLAN interface | 12.5(2) | TAESPIM/Avaya (Definity) PG using TSAPI interface |
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