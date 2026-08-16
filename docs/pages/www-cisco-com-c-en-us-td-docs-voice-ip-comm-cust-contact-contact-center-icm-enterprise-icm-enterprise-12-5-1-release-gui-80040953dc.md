---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-release-gui-80040953dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/release/guide/ucce_b_1251-ucce-release-notes/ucce_b_1251-ucce-release-notes_chapter_0110.html
retrieved_at: 2026-08-16T19:40:16.032348+00:00
---

Release Notes for Unified Contact Center Enterprise, Release 12.5(1)

# Release Notes for Unified Contact Center Enterprise, Release 12.5(1)

Updated: January 21, 2020

Chapter: Unified Contact Center Enterprise

## Chapter: Unified Contact Center Enterprise

# Unified Contact Center Enterprise

## New Features

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

Unified CCE solution leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to provide services that assist
                              agents. These Contact Center AI services are available for the agents through the Agent Answers gadget and the Call Transcript
                              gadget on the Cisco Finesse desktop.

The Agent Answers gadget displays relevant suggestions and recommendations in real time for the agent to consider. The suggestions
                              and recommendations are based on the ongoing conversation between the caller and the agent. Agent Answers enhances the customer
                              experience because the timely suggestions improve the ability of the agent to respond.

The Call Transcript gadget dynamically converts the ongoing voice conversation to text and presents the text to an agent for
                              real-time viewing and reference.

For details on how to configure the Agent Answers and Call Transcription features, see the Agent Answers and the Call Transcription chapters in the following documents:

Cisco Unified Contact Center Enterprise Features Guide, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

For information on the design considerations of the Agent Answers and Call Transcription features, see the Contact Center AI Services Considerations section in following documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

### Support for 36000 Agents

You can modify your existing 24000 agent reference design to scale up to 36000 agents. This is accomplished by adding more
                              peripheral VMs and peripheral gateways to the deployment and modifying specific configuration limits. You must also modify
                              the OVA files for Live Data and Cisco Identity Service (IdS).

The following engineering specials are required to support 36000 agents:

ICM_12.5(1)_ES45

CUIC_12.5(1)_ES07 if you are using Live Data

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge) . For more information, see the Supported Browsers section in the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

To enable this browser
                                          support in Administration Client Setup for Cisco Unified ICM/Contact
                                             Center Enterprise , install the ICM_12.5(1)_ES30.

### Smart Licensing

This release introduces Smart Licensing that delivers visibility into your license ownership and consumption. Smart Licensing
                              helps you to procure, deploy, and manage licenses easily and report license consumption. It pools license entitlements in
                              a single account and allows you to move licenses freely through the virtual accounts.

Smart Licensing registers the product instance, reports license usage, and obtains the necessary authorization from Cisco
                              Smart Software Manager or Cisco Smart Software Manager On-Prem.

For more information, see Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

For more information, see Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

### Cloud Connect

Cloud Connect is an infrastructure component that hosts services that enable integration with Cisco Webex Cloud Services,
                                 such as Cisco Webex Experience Management .

### Cisco Webex Experience Management

Cisco
                              Webex Experience Management (referred to as Experience Management) is the platform for
                              Customer Experience Management (CEM), integrated with powerful tools that allow you to
                              see your business from your customer's perspective.

With Experience Management integrated with Unified CCE :

Administrators can configure post call surveys to collect feedback directly from customers.

Administrator can configure and initiate digital channel surveys when the agent responds to an email or chat from a customer
                                    by using the Enterprise Chat and Email gadget.

Administrators can configure analytical gadgets, which can be viewed on the Finesse desktop.

Agents and Supervisors can view pulse of the customers through industry standard metrics such as NPS, CSAT, and CES, or other
                                    KPIs.

See Experience Management Voice Surveys

See Experience Management Email/SMS Surveys

#### Experience Management Voice Surveys

The voice surveys can be triggered through Experience Management, using CVP IVR. Experience Management surveys use the same
                                 scripting and call flows as Post Call Survey, with the exception that the questionnaire is provided by the cloud-based Experience
                                 Management service. The Call Studio survey is configured in the router script that runs during the survey leg of the call,
                                 and is passed to the CVP through an ECC variable.

The CVP Call Studio survey application fetches the questions from the Experience Management service, collects the answers
                                 from the caller, and submits them to the Experience Management service over REST APIs.

For more information on how to configure Experience Management , see the Webex Experience Management chapter in the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Experience Management is supported in all the deployment types. For more information on the call flow and design considerations, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

#### Experience Management Email/SMS Surveys

This feature allows customers to participate in the post-call surveys using links sent over SMS or Email.

Administrators can configure and customize the survey in Experience Management. The responses are displayed on the Customer
                                 Experience Journey gadget on the Finesse desktop.

For more information on the list of tasks required to integrate Experience Management, refer to the section Experience Management Task Flow in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

### Agent Summary Live Data Report

This release adds the Agent Summary Live Data report which displays real-time agent statistics such as not ready time, total
                              number of calls handled, and wrap-up time. This report is also available in a Finesse gadget and displays agent statistics
                              to an agent and team statistics to a supervisor. The report is useful when monitoring the performance of an agent.

For details see the Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.5 at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

### Encryption Support for External DBLookUp Registry Configuration

External DBLookUp registry configuration will support only encrypted value, the CCEDataProtect Tool is used to encrypt and
                              decrypt sensitive information that the Windows registry stores in it. After upgrading to Release 12.5, if the DBLookUp is
                              configured, then you must reconfigure the external DBLookUp registry value using the CCEDataProtect Tool to encrypt the data
                              in the registry. For more information, refer to the Configure External DBLookUp Registry Value using CCEDataProtect Tool procedure in Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

### Campaign Skillgroup Dialing Mode

Configure the mode and percentage of the Campaign Skillgroup directly from the Campaign Skillgroup tab. This eliminates the
                              need to use an administrative script to update the skill groups dynamically. An administrative script, if used, will override
                              the configuration changes made from the Campaign Skillgroup tab.

For more details, see the Administrative Scripts for Outbound Option and Set Up an Administrative Script sections in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

### Live Data CLIs

#### Live Data HSTS Configuration

This release allows an Administrator to turn on or off HTTP Strict Transport Security (HSTS) on live-data and also show the
                                 current status of the HSTS property.

HSTS is a web security policy mechanism that helps to protect websites against protocol downgrade attacks and cookie hijacking.
                                 It allows web servers to declare that the web browsers (or other complying user agents) interact with it using only secure
                                 HTTPS connections, and never through the insecure HTTP protocol.

For more information, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

#### Live Data HTTP Configuration

This release allows an Administrator to turn on or off HTTP access to live-data and also show the current status of the http-enabled
                                 property.

Any changes to http-enabled status needs a restart of CCE Live Data NGINX Service.

For more information, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

### Agents Placing Outbound Calls in Available State

If agents in Available state place outbound calls, the Unified CCE system sets the agent's state to NotReady before allowing
                              the call (without manually setting the agent's state to NotReady from the CTI interface). The system changes the agent's state
                              back to Available when the call ends or fails to connect.

For details on the reason code, see the Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html . For details on the call manner type, see the CTI Server Message Reference Guide (Protocol Version 23) for Cisco Unified Contact Center Enterprise, Release 12.5(1) .

This enhancement also enables the Finesse Make Call from Ready feature via the Finesse API. For details, see Changes in REST APIs and the REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide .

### Shared ACD Line

Shared ACD line feature introduced in an ICM_12.5(1)_ES4, will require additional configuration in case you want to use it
                                          on 12.6(1). The behavior changes are: in that you will now select which device to use when you log into Finesse. It also requires
                                          a change in agent desk settings to enable for the agent.

When you log in to Finesse, you will now select which device to use.

Additional changes are required in agent desk setting incase you want to enable it for the agents.

This release includes shared ACD lines support for up to two devices. The support enables an agent with devices at different
                              locations to utilize the same extension.

UCM auto-answer and Agent Desk Settings auto-answer are not supported when shared ACD lines are in use.

For more information, see the Call Type Considerations for Phone Extensions section in the Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### Customer Journey Analyzer for Business Metrics (Trials)

Customer Journey Analyzer is a cloud service that processes historical contact center data from on-premise deployment to generate specific Business
                                 Metrics across the contact center. It displays trends to help you identify patterns and gain insight for continuous improvement.
                                 You can view the Abandoned Contacts dashboard on the Customer Journey Analyzer which enables supervisors and business analysts to identify where contacts are being abandoned and take appropriate action.
                                 You can use Customer Journey Analyzer to create visualizations using Customer Activity Records, Customer Session Records, and Agent Activity Records.

Customer Journey Analyzer is available as Trials. Please contact your Cisco Support to get started on Trials.

### Webex Workforce Optimization (WFO) Support with Contact Center Enterprise (CCE) Solutions

The Contact Center Enterprise (Unified CCE/Packaged CCE/Webex CCE) solutions supports the Webex Workforce Optimization offering. See https://www.cisco.com/c/en/us/support/contact-center/webex-workforce-optimization/series.html .

## Updated Features

### Increased PG Agent Capacity for Mobile Agents

#### Added on May 14th, 2021

The mobile agent capacity on the PG has increased as follows:

2000 with nailed-up connections (1:1)

1500 with nailed-up connections if the average handle time is less than 3 minutes, or if agent greeting or whisper announcement
                                       features are used with the mobile agent (1.3:1)

1500 with call-by-call connections (1.3:1)

For more details, see the PG Agent Capacity with Mobile Agents section in the Sizing and Operating Conditions for Reference Designs chapter at Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

### Non-Production System (NPS)

This feature requires ICM_12.5(1)_ES25  to be installed on the 12.5(1) target system
                                          to enable the Non-Production System (NPS) .

Non-Production System (NPS) usage mode gives you more control on license usage. With NPS, you can switch from production deployment
                              to other deployment types such as lab, testing, and staging.

For more information, see the Smart Licensing section in the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

### Security Enhancements

This release introduces following security enhancements for CCE Administration:

It is mandatory to import self-signed certificates (if CA-signed certificates are not used) of Solution components into the
                                    AW machines.

For more information, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

HTTP Security headers (Content-Security-Policy (CSP), X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, and Strict-Transport-Security)
                                    have been introduced in the browser response to prevent cross-site scripting (XSS) vulnerabilities.

### Tomcat Upgrade

Tomcat is upgraded from 7.0.x to 9.0.21 .

### Configuration Limit Changes

The following configuration limits have increased from this release:

Outbound dialer maximum calls per second per dialer increased from 20 to 60 for the 2000 agent deployment and from 30 to 60
                                       for the 4000 agent, 12000 agent, and 24000 agent deployments.

Outbound dialer maximum ports per SIP dialer increased from 1500 to 3000 for all the deployment types.

Number of campaigns per system increased from 600 to 1500 for all the deployment types.

For more details see the Outbound Campaign Limits section in the Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 12.5 at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### Replication Enhancements

With Outbound Option High Availability, replication of data is managed by the Campaign Manager running on the standby side,
                                 through a series of files in a replication folder. For more information, see Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

Direct access to the Personal_Callback_List table is not supported with Outbound Option High Availability enabled. Use the
                                             Outbound API to insert customer records directly into the Personal_Callback_List table. For information on Outbound APIs,
                                             see the Cisco Unified Contact Center Enterprise Developer Reference at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html

### Outbound Option Predictive Algorithm Enhancements

To enable these Outbound Option enhancements, you must install the ICM_12.5(1)_ES90 on
                                             12.5(1) .

The following enhancements have been made to the Outbound Option feature:

EnhancedPredictiveDialing , a new registry setting is added to reduce the
                                    idle time when there is a low hit rate for voice customers and when the agent
                                    idle times are long. This change adapts to the dialing rate more aggressively,
                                    irrespective of the configured abandon limit. This feature is disabled by
                                    default.

The logic associated with the existing ReclassifyTransferFailures registry
                                    setting is modified so that the answering machine calls that are abandoned due
                                    to lack of agent or IVR resources are not counted as abandoned voice calls but
                                    as answering machine calls. ReclassifyTransferFailures registry setting
                                    is enabled by default on fresh installs and disabled by default in upgraded
                                    systems.

For more information, see the Dialer Registry Settings section in the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

### Database Schema Changes

#### Unified CCE Database Schema Changes

Release 12.5.1 includes several changes to the database schema for the main database. The release adds the following new tables:

Smart_License_Server

Smart_License_Info

Smart_License_Entitlements

Smart_License_Product

The release includes datatype changes to the following tables:

Table

Changes

Config_Message_Log

Changed datatype of ConfigMessage to varbinary(max).

Event

Changed datatype of BinData to varbinary(max).

Application_Event

Changed datatype of BinData to varbinary(max).

Feature_Control_Set

Changed datatype of  FeatureSetData to varbinary(max).

Route_Call_Detail

Changed datatype of  CallTrace to varbinary(max).

Machine_Connection_Profile

Changed datatype of  Password to varbinary(max).

Machine_Service

Changed datatype of EnablePassword to varbinary(max).

Changed datatype of Password to varbinary(max).

Script_Real_Time

Changed datatype of ScriptMeters to varbinary(max).

Script_Data

Changed datatype of ScriptData to varbinary(max).

System_Capacity_Interval

Changed datatype of DbDateTime to DBDATETIME NULL.

The release added new fields to the following tables:

Table

Changes

ICR_Globals

Added these fields:

AnalyzerIntegrated

CVPCxSurveyAppName

System_Capacity_Interval

Added these fields:

MaxVoiceAgentsLoggedIn

MaxNonVoiceAgentsLoggedIn

MaxAgentsHandledPrevOB

MaxAgentsHandledPredProgOB

MaxPerpetualPremiumAgentsLoggedIn

MaxFlexStdAgentsLoggedIn

MaxFlexPremiumAgentsLoggedIn

CustomerDefinitionId

System_Capacity_Real_Time

Added these fields:

MaxVoiceAgentsLoggedIn

MaxNonVoiceAgentsLoggedIn

MaxAgentsHandledPrevOB

MaxAgentsHandledPredProgOB

MaxPerpetualPremiumAgentsLoggedInNow

MaxStdAgentsLoggedInNow

MaxPremiumAgentsLoggedInNow

MaxCVPCallControlPorts

MaxVRUPorts

CustomerDefinitionId

FutureUseInt3

FutureUseInt4

Agent_Event_Detail

Added these fields:

RouterCallKey

RouterCallKeyDay

PeripheralCallKey

AgentDialedNumber

EventDateTimeUTC

DialedNumber

TaskIndex

AgentSessionId

AgentState

RouterCallKeySequenceNumber

Direction

PrecisionQueueID

SkillGroupID

WrapupData

Route_Call_Detail

Added the CallStartDateTimeUTC field.

Termination_Call_Detail

Added these fields:

AnsweredDateTimeUTC

WrapUpStartDateTimeUTC

ConsultStartDateTimeUTC

ConsultEndDateTimeUTC

ConferenceStartDateTimeUTC

ConferenceEndDateTimeUTC

TransferredDateTimeUTC

CallTerminatedDateTimeUTC

AgentSessionId

User_Group

Added the EmailAddress field.

The release removed this field from the following table:

Table

Changes

ICR_Globals

Removed the ContextServiceConnectionData field.

## Important Notes

### SQL Server Execution Plan Issue

Microsoft SQL Server 2017 and later versions include an execution plan enhancement that can intermittently cause performance
                              issues with CCE database operations. If your CCE deployment uses SQL Server 2017 or later, set the SQL Server compatibility
                              level for the CCE databases (Logger, AW, BA, and HDS) to the SQL Server 2014 equivalent—compatibility level 120. For more
                              information, see CSCvw51851.

Do not change the compatibility level for SQL Server system databases.

Run the following query against each applicable CCE database:

```
ALTER DATABASE <CCE_database_name> SET COMPATIBILITY_LEVEL = 120
```

You can run this query while the system is in operation.

### OpenJDK Java Runtime Environment Update

A new 12.5(1a) base installer is
                              available for customers, which has OpenJDK JRE as the supporting Java runtime for all CCE applications. It is no different from
                              the preceding 12.5(1) installer except for the Java runtime environment installed on the
                              CCE virtual machines (VMs).

You can continue to use Oracle JRE if
                              you installed CCE 12.5(1) before the release of 12.5(1a). Further Java security updates
                              and fixes can be downloaded and installed from the Oracle website.

There is no requirement to
                              redeploy/reinstall existing 12.5 CCE VMs using the 12.5(1a) installer to switch to
                              OpenJDK. Download and install ES55 (mandatory OpenJDK ES) instead, as needed.

However, if you want to install any ESs released after ES55 on 12.5(1), then you must first install ES55 (mandatory OpenJDK
                              ES) on the relevant VMs as a prerequisite.

### SocialMiner Renamed

SocialMiner will be referred to as Customer Collaboration Platform from release 12.5(1) onwards.

### Certificate Validation

All components now enforce certificate validations. If you use any third-party Certificate Authority (CA) signed or self-signed
                                 certificates for any components that are not trusted by the platform by default, then the certificates must be mandatorily
                                 imported into the dependent component server trust store.

For more information, see Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

### Outbound Option Import Rule

In Outbound Option Import Rule, when you add or modify a field in the import rule table, change the target table name to save
                                 your changes to the import rule. After the name change, the old table remains in the database, but the system does not use
                                 it.

## Deprecated Features

Deprecated features are fully supported. However, there is no additional development for Deprecated features. These features
                              may be scheduled to be removed in a future release. Plan to transition to the designated replacement feature. If you are implementing
                              a new deployment, use the replacement technology rather than the deprecated feature.

Please review the applicable notes for details about exceptions or other qualifiers.

Deprecated Feature

Announced in Release

Replacement

Notes

Internet Explorer 11

Not applicable 1

Edge Chromium (Microsoft Edge v79 and later)

None.

Avaya Aura Contact Center (AACC - formerly Symposium) PG

12.5(1)

None.

None.

UCC Enterprise Gateway PG (Parent PG in Parent-Child deployments)

12.5(1)

None.

None.

Aspect PG

12.5(1)

None.

None.

Integrity Check Tool

12.0(1)

None.

None.

External Script Validation

12.0(1)

None.

None.

Translation Route Wizard

12.0(1)

None.

None.

Symposium ACD

12.0(1)

None.

None.

MIB Objects:

cccaDistAwWebViewEnabled

cccaDistAwWebViewServerName

cccaSupportToolsURL

cccaDialerCallAttemptsPerSec

11.6(1)

None.

None.

Generic PG

11.5(1)

Agent PG and VRU PG

None

ECSPIM

11.5(1)

TAESPIM

Avaya SEI/CVLAN protocol was deprecated by vendor.

"Sprawler" deployment

10.0(1)

A Packaged CCE deployment

A "Sprawler" was a Progger with an Administration & Data Server on a single box. It was used for lab deployments.

## Removed and Unsupported Features

The following features are no longer available:

Feature

Effective from Release

Replacement

Context Service

12.5(1)

None.

Cisco MediaSense

12.5(1)

None.

SHA-1 certificate

12.5(1)

SHA-256

TLS 1.0 and TLS 1.1

12.5(1)

TLS 1.2

Cisco Remote Expert Mobile

12.5(1)

None.

## Third Party Software Impacts

See the Unified CCE Compatibility related information located at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html for information on third-party software.

| Note | For Nginx-based reverse-proxy rules, installation, configuration, and security hardening instructions, refer to the Nginx TechNote article . Any reverse-proxy supporting the required criteria (as mentioned in the Reverse-Proxy Selection Criteria section of Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) ) can be used in place of Nginx for supporting this feature. If CORS status is "enabled", you must explicitly add the reverse-proxy domain name to the list of CORS trusted domain names. |
|---|---|

| Note | The following engineering specials are required to support 36000 agents: ICM_12.5(1)_ES45 CUIC_12.5(1)_ES07 if you are using Live Data |
|---|---|

| Note | To enable this browser
                                          support in Administration Client Setup for Cisco Unified ICM/Contact
                                             Center Enterprise , install the ICM_12.5(1)_ES30. |
|---|---|

| Note | By default, HTTP is disabled. You can enable HTTP (if required) using the set live-data properties http-enabled on command. |
|---|---|

| Note | Shared ACD line feature introduced in an ICM_12.5(1)_ES4, will require additional configuration in case you want to use it
                                          on 12.6(1). The behavior changes are: in that you will now select which device to use when you log into Finesse. It also requires
                                          a change in agent desk settings to enable for the agent. When you log in to Finesse, you will now select which device to use. Additional changes are required in agent desk setting incase you want to enable it for the agents. |
|---|---|

| Note | UCM auto-answer and Agent Desk Settings auto-answer are not supported when shared ACD lines are in use. |
|---|---|

| Note | Customer Journey Analyzer is available as Trials. Please contact your Cisco Support to get started on Trials. |
|---|---|

| Note | This feature requires ICM_12.5(1)_ES25  to be installed on the 12.5(1) target system
                                          to enable the Non-Production System (NPS) . |
|---|---|

| Note | Direct access to the Personal_Callback_List table is not supported with Outbound Option High Availability enabled. Use the
                                             Outbound API to insert customer records directly into the Personal_Callback_List table. For information on Outbound APIs,
                                             see the Cisco Unified Contact Center Enterprise Developer Reference at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html |
|---|---|

| Note | To enable these Outbound Option enhancements, you must install the ICM_12.5(1)_ES90 on
                                             12.5(1) . |
|---|---|

| Table | Changes |
|---|---|
| Config_Message_Log | Changed datatype of ConfigMessage to varbinary(max). |
| Event | Changed datatype of BinData to varbinary(max). |
| Application_Event | Changed datatype of BinData to varbinary(max). |
| Feature_Control_Set | Changed datatype of  FeatureSetData to varbinary(max). |
| Route_Call_Detail | Changed datatype of  CallTrace to varbinary(max). |
| Machine_Connection_Profile | Changed datatype of  Password to varbinary(max). |
| Machine_Service | Changed datatype of EnablePassword to varbinary(max). Changed datatype of Password to varbinary(max). |
| Script_Real_Time | Changed datatype of ScriptMeters to varbinary(max). |
| Script_Data | Changed datatype of ScriptData to varbinary(max). |
| System_Capacity_Interval | Changed datatype of DbDateTime to DBDATETIME NULL. |

| Table | Changes |
|---|---|
| ICR_Globals | Added these fields: AnalyzerIntegrated CVPCxSurveyAppName |
| System_Capacity_Interval | Added these fields: MaxVoiceAgentsLoggedIn MaxNonVoiceAgentsLoggedIn MaxAgentsHandledPrevOB MaxAgentsHandledPredProgOB MaxPerpetualPremiumAgentsLoggedIn MaxFlexStdAgentsLoggedIn MaxFlexPremiumAgentsLoggedIn CustomerDefinitionId |
| System_Capacity_Real_Time | Added these fields: MaxVoiceAgentsLoggedIn MaxNonVoiceAgentsLoggedIn MaxAgentsHandledPrevOB MaxAgentsHandledPredProgOB MaxPerpetualPremiumAgentsLoggedInNow MaxStdAgentsLoggedInNow MaxPremiumAgentsLoggedInNow MaxCVPCallControlPorts MaxVRUPorts CustomerDefinitionId FutureUseInt3 FutureUseInt4 |
| Agent_Event_Detail | Added these fields: RouterCallKey RouterCallKeyDay PeripheralCallKey AgentDialedNumber EventDateTimeUTC DialedNumber TaskIndex AgentSessionId AgentState RouterCallKeySequenceNumber Direction PrecisionQueueID SkillGroupID WrapupData |
| Route_Call_Detail | Added the CallStartDateTimeUTC field. |
| Termination_Call_Detail | Added these fields: AnsweredDateTimeUTC WrapUpStartDateTimeUTC ConsultStartDateTimeUTC ConsultEndDateTimeUTC ConferenceStartDateTimeUTC ConferenceEndDateTimeUTC TransferredDateTimeUTC CallTerminatedDateTimeUTC AgentSessionId |
| User_Group | Added the EmailAddress field. |

| Table | Changes |
|---|---|
| ICR_Globals | Removed the ContextServiceConnectionData field. |

| Deprecated Feature | Announced in Release | Replacement | Notes |
|---|---|---|---|
| Internet Explorer 11 | Not applicable 1 | Edge Chromium (Microsoft Edge v79 and later) | None. |
| Avaya Aura Contact Center (AACC - formerly Symposium) PG | 12.5(1) | None. | None. |
| UCC Enterprise Gateway PG (Parent PG in Parent-Child deployments) | 12.5(1) | None. | None. |
| Aspect PG | 12.5(1) | None. | None. |
| Integrity Check Tool | 12.0(1) | None. | None. |
| External Script Validation | 12.0(1) | None. | None. |
| Translation Route Wizard | 12.0(1) | None. | None. |
| Symposium ACD | 12.0(1) | None. | None. |
| MIB Objects: cccaDistAwWebViewEnabled cccaDistAwWebViewServerName cccaSupportToolsURL cccaDialerCallAttemptsPerSec | 11.6(1) | None. | None. |
| Generic PG | 11.5(1) | Agent PG and VRU PG | None |
| ECSPIM | 11.5(1) | TAESPIM | Avaya SEI/CVLAN protocol was deprecated by vendor. |
| "Sprawler" deployment | 10.0(1) | A Packaged CCE deployment | A "Sprawler" was a Progger with an Administration & Data Server on a single box. It was used for lab deployments. |

| Feature | Effective from Release | Replacement |
|---|---|---|
| Context Service | 12.5(1) | None. |
| Cisco MediaSense | 12.5(1) | None. |
| SHA-1 certificate | 12.5(1) | SHA-256 |
| TLS 1.0 and TLS 1.1 | 12.5(1) | TLS 1.2 |
| Cisco Remote Expert Mobile | 12.5(1) | None. |