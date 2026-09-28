---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-release-guide-pcce-b-1251-pcce--93cfe22f08
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/release/guide/pcce_b_1251_pcce-release-notes/pcce_b_1251_pcce-release-notes_chapter_0101.html
retrieved_at: 2026-08-21T04:48:43.848764+00:00
---

Release Notes for Packaged Contact Center Enterprise Solution, Release 12.5(1)

# Release Notes for Packaged Contact Center Enterprise Solution, Release 12.5(1)

Updated: January 21, 2020

Chapter: Cisco Packaged Contact Center Enterprise

## Chapter: Cisco Packaged Contact Center Enterprise

# Cisco Packaged Contact Center Enterprise

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

Packaged CCE solution leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to provide services that assist
                              agents. These Contact Center AI services are available for the agents through the Agent Answers gadget and the Call Transcript
                              gadget on the Cisco Finesse desktop.

The Agent Answers gadget displays relevant suggestions and recommendations in real time for the agent to consider. The suggestions
                              and recommendations are based on the ongoing conversation between the caller and the agent. Agent Answers enhances the customer
                              experience because the timely suggestions improve the ability of the agent to respond.

The Call Transcript gadget dynamically converts the ongoing voice conversation to text and presents the text to an agent for
                              real-time viewing and reference.

For details on how to configure the Agent Answers and Call Transcription features, see the Agent Answers and the Call Transcription chapters in the following documents:

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

For information on the design considerations of the Agent Answers and Call Transcription features, see the Contact Center AI Services Considerations section in following documents:

Solution Design Guide for Cisco Packaged Contact Center Enterprise, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge) . For more information, see the Supported Browsers section in the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

To enable this browser
                                          support in Administration Client Setup for Cisco Unified ICM/Contact
                                             Center Enterprise , install the ICM_12.5(1)_ES30.

### Technology Refresh Upgrade

In this release, Technology Refresh upgrade support is added in all Packaged CCE deployments. Technology Refresh upgrade enables
                              you to set up a complete solution or a subset of solution components on a different hardware. The supported upgrade path is 12.0(1) to 12.5(1). This feature requires ICM_12.5(1)_ES12 to be installed on the 12.5(1) target
                                 system to enable the Technology Refresh upgrade process. For more information, see Technology Refresh Upgrade Process chapter in the Cisco Packaged Contact Center Enterprise Installation and Upgrade at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

### Smart Licensing

This release introduces Smart Licensing that delivers visibility into your license ownership and consumption. Smart Licensing
                              helps you to procure, deploy, and manage licenses easily and report license consumption. It pools license entitlements in
                              a single account and allows you to move licenses freely through the virtual accounts.

Smart Licensing registers the product instance, reports license usage, and obtains the necessary authorization from Cisco
                              Smart Software Manager or Cisco Smart Software Manager On-Prem.

For more information, see Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

### Cloud Connect

Cloud Connect is an infrastructure component that hosts services that enable integration with Cisco Webex Cloud Services,
                                 such as Cisco Webex Experience Management .

### Cisco Webex Experience Management

Cisco
                              Webex Experience Management (referred to as Experience Management) is the platform for
                              Customer Experience Management (CEM), integrated with powerful tools that allow you to
                              see your business from your customer's perspective.

With Experience Management integrated with Packaged CCE :

Administrators can configure post call surveys to collect feedback directly from customers.

Administrator can configure and initiate digital channel surveys when the agent responds to an email or chat from a customer
                                    by using the Enterprise Chat and Email gadget.

Administrators can configure analytical gadgets, which can be viewed on the Finesse desktop.

Agents and Supervisors can view pulse of the customers through industry standard metrics such as NPS, CSAT, and CES, or other
                                    KPIs.

See Experience Management Voice Surveys

See Experience Management Email/SMS Surveys

#### Experience Management Email/SMS Surveys

This feature allows customers to participate in the post-call surveys using links sent over SMS or Email.

Administrators can configure and customize the survey in Experience Management. The responses are displayed on the Customer
                                 Experience Journey gadget on the Finesse desktop.

For more information on the list of tasks required to integrate Experience Management, refer to the section Experience Management Task Flow in Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html

#### Experience Management Voice Surveys

The voice surveys can be triggered through Experience Management, using CVP IVR. Experience Management surveys use the same
                                 scripting and call flows as Post Call Survey, with the exception that the questionnaire is provided by the cloud-based Experience
                                 Management service. The Call Studio survey is configured in the router script that runs during the survey leg of the call,
                                 and is passed to the CVP through an ECC variable.

The CVP Call Studio survey application fetches the questions from the Experience Management service, collects the answers
                                 from the caller, and submits them to the Experience Management service over REST APIs.

For more information on how to configure Experience Management , see the Webex Experience Management chapter in the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html

### Command Execution Pane

In this release, a new user interface called Command Execution Pane has been added in the Infrastructure Settings page of Unified CCE Administration. This interface allows System Administrators
                              to execute REST API calls to the Unified CVP, Unified CVP Reporting, and Virtualized Voice Browser.

For more information, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### Multistage Upgrade Support

This release adds multistage upgrade support for Packaged CCE 2000, 4000, and 12000 deployments through the common ground
                              upgrade process. With multistage upgrade support each component on Packaged CCE can be on different versions during the upgrade
                              process, and you can perform the upgrade in multiple stages. The multistage upgrade support is backward compatible with Release
                              12.0(1) only. For more information, refer to Version Upgrade section in Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

### Agent Summary Live Data Report

This release adds the Agent Summary Live Data report which displays real-time agent statistics such as not ready time, total
                              number of calls handled, and wrap-up time. This report is also available in a Finesse gadget and displays agent statistics
                              to an agent and team statistics to a supervisor. The report is useful when monitoring the performance of an agent.

For details see the Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.5 at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

### Encryption Support for External DBLookUp Registry Configuration

External DBLookUp registry configuration will support only encrypted value, the CCEDataProtect Tool is used to encrypt and
                              decrypt sensitive information that the Windows registry stores in it. After upgrading to Release 12.5, if the DBLookUp is
                              configured, then you must reconfigure the external DBLookUp registry value using the CCEDataProtect Tool to encrypt the data
                              in the registry. For more information, refer to the Configure External DBLookUp Registry Value using CCEDataProtect Tool procedure in Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

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

For more details, see the PG Agent Capacity with Mobile Agents section in the Sizing and Operating Conditions for Reference Designs chapter at Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html

### IP Address or Hostname Update

This feature requires ICM_12.5(1)_ES12. In the Unified CCE Administration, administrators will be able to update the IP address or hostname of components in the
                              inventory. For more information, see Inventory Management section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### Non-Production System (NPS)

This feature requires ICM_12.5(1)_ES25  to be installed on the 12.5(1) target system
                                          to enable the Non-Production System (NPS) .

Non-Production System (NPS) usage mode gives you more control on license usage. With NPS, you can switch from production deployment
                              to other deployment types such as lab, testing, and staging.

For more information, see the Smart Licensing section in the Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

### Desktop Layout Editors

This feature requires ICM12.5(1)_ES7. This release provides the following Desktop Layout editors in the Teams and Resources pages of the Unified CCE Administration .

Text Editor — Allows you to view and edit code in text format. It is the default editor.

XML Editor — Allows you to view and edit code in XML format. However, you cannot add or edit comments (<!-- -->) in this editor.

For more information, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### Security Enhancements

This release introduces following security enhancements for CCE Administration:

It is mandatory to import self-signed certificates (if CA-signed certificates are not used) of all Solution components into the AW machines.

For more information, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

HTTP Security headers (Content-Security-Policy (CSP), X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, and Strict-Transport-Security)
                                    have been introduced in the browser response to prevent cross-site scripting (XSS) vulnerabilities.

### Tomcat Upgrade

Tomcat is upgraded from 7.0.x to 9.0.21 .

### CVP Configuration for Media Server

In this release, support for the following has been provided in the Inventory page of Unified CCE Administration :

Addition, modification, and deletion of external Media Servers

Access to FTP configuration in external Media Servers

Access to FTP configuration in CVPs where Media Servers are installed

Any configuration change in Media Server gets propagated to all CVPs across sites.

For more information, see Media Server section in the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### Configuration Limit Changes

The following configuration limits have increased from this release:

Outbound dialer maximum calls per second per dialer increased from 20 to 60 for the 2000 agent deployment and from 30 to 60
                                       for the 4000 agent and 12000 agent deployments.

Outbound dialer maximum ports per SIP dialer increased from 1500 to 3000 for all the deployment types.

Number of campaigns per system increased from 600 to 1500 for all the deployment types.

For more details see the Outbound Campaign Limits section in the Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 12.5 at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### Replication Enhancements

With Outbound Option High Availability, replication of data is managed by the Campaign Manager running on the standby side,
                                 through a series of files in a replication folder. For more information, see Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

Direct access to the Personal_Callback_List table is not supported with Outbound Option High Availability enabled. Use the
                                             Outbound API to insert customer records directly into the Personal_Callback_List table. For information on Outbound APIs,
                                             see the Cisco Unified Contact Center Enterprise Developer Reference at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html

## Important Notes

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

Integrity Check Tool

12.0(1)

None.

None.

External Script Validation

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

See the Contact Center Enterprise Compatibility Matrix for this release at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html for information on third-party software.

| Note | For Nginx-based reverse-proxy rules, installation, configuration, and security hardening instructions, refer to the Nginx TechNote article . Any reverse-proxy supporting the required criteria (as mentioned in the Reverse-Proxy Selection Criteria section of Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) ) can be used in place of Nginx for supporting this feature. If CORS status is "enabled", you must explicitly add the reverse-proxy domain name to the list of CORS trusted domain names. |
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

| Note | This feature requires ICM_12.5(1)_ES25  to be installed on the 12.5(1) target system
                                          to enable the Non-Production System (NPS) . |
|---|---|

| Note | Any configuration change in Media Server gets propagated to all CVPs across sites. |
|---|---|

| Note | Direct access to the Personal_Callback_List table is not supported with Outbound Option High Availability enabled. Use the
                                             Outbound API to insert customer records directly into the Personal_Callback_List table. For information on Outbound APIs,
                                             see the Cisco Unified Contact Center Enterprise Developer Reference at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html |
|---|---|

| Deprecated Feature | Announced in Release | Replacement | Notes |
|---|---|---|---|
| Internet Explorer 11 | Not applicable 1 | Edge Chromium (Microsoft Edge v79 and later) | None. |
| Avaya Aura Contact Center (AACC - formerly Symposium) PG | 12.5(1) | None. | None. |
| Integrity Check Tool | 12.0(1) | None. | None. |
| External Script Validation | 12.0(1) | None. | None. |
| MIB Objects: cccaDistAwWebViewEnabled cccaDistAwWebViewServerName cccaSupportToolsURL cccaDialerCallAttemptsPerSec | 11.6(1) | None. | None. |
| Generic PG | 11.5(1) | Agent PG and VRU PG | None |
| "Sprawler" deployment | 10.0(1) | A Packaged CCE deployment | A "Sprawler" was a Progger with an Administration & Data Server on a single box. It was used for lab deployments. |

| Feature | Effective from Release | Replacement |
|---|---|---|
| Context Service | 12.5(1) | None. |
| Cisco MediaSense | 12.5(1) | None. |
| SHA-1 certificate | 12.5(1) | SHA-256 |
| TLS 1.0 and TLS 1.1 | 12.5(1) | TLS 1.2 |
| Cisco Remote Expert Mobile | 12.5(1) | None. |