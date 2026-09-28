---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-release-guide-uccx-b-uccx-solut-0c7e1fbfb9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/release/guide/uccx_b_uccx-solution-release-notes-125/uccx_b_uccx-solution-release-notes-125_chapter_01.html
retrieved_at: 2026-08-16T21:01:49.357266+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1)

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1)

Updated: January 31, 2020

Chapter: Cisco Unified Contact Center Express

## Chapter: Cisco Unified Contact Center Express

# Cisco Unified Contact Center Express

## New Features

### Specific License Reservation

With Smart Licensing, Unified CCX periodically shares license utilization data with Cisco SSM . Deployments that cannot share license utilization data with Cisco SSM on a periodic basis due to regulatory reasons can use the Specific License Reservation (SLR) feature. You can reserve licenses
                              (including add-on licenses) for your product instance on Cisco SSM . To enable Specific License Reservation, you must use Unified CCX CLI. For more information about Specific License Reservation
                              feature, see the Specific License Reservation section in Cisco Unified Contact Center Express Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-feature-guides-list.html .

This feature is available from Unified CCX R12.5(1) ES02.

### License Control

Smart Licensing allows you to use more licenses than you have purchased. However, if you want to limit the license usage to
                              the purchased quantity or less, use License Control . With License Control , you can disable Overage Allowance option to restrict the number of agents and ports that can be used in Unified CCX. For different license types, appropriate
                              fields will be displayed for you to restrict the usage of licenses and ports. For more information on License Control , see the Overview section of Smart Licensing chapter in Cisco Unified Contact Center Express Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-feature-guides-list.html .

This feature is available from Unified CCX R12.5(1) ES02.

### Federal Information Processing Standards 140-2 Level 1 Support

Unified CCX supports Federal Information Processing Standards (FIPS) 140-2 Level 1. FIPS 140-2 Level 1 is a U.S. and Canadian
                              government certification standard that defines minimum security requirements for cryptographic modules protecting sensitive
                              information in computer and telecommunications systems. It also defines algorithms that are allowed to be used to encrypt
                              sensitive information. These strictly defined requirements are important for government agencies, hospitals, and other customers
                              who would require a higher level of security. For more information about FIPS 140-2 mode support in Unified CCX, see the Solution Security chapter in Solution Design Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-implementation-design-guides-list.html .

This feature is available from Unified CCX R12.5(1) ES02.

### A-Law Codec Support

Recording and uploading of A-Law prompts is supported. You can record prompts by using Recording Step in Unified CCX or any
                                 third party utility and upload A-Law prompts.

### Assign Prompts

Administrators can assign all or specific prompts to Unified CCX applications. Supervisors with Advanced Supervisor Capability
                                 can view and manage the prompts that are associated with the assigned Unified CCX applications by using the Finesse desktop.

### Schedule Adding and Removing of Agents to Queue

In the Finesse desktop, supervisors with Advanced Supervisor Capability can set the date and time for auto-addition and auto-removal
                                 of agents from a queue. This allows the supervisors to automatically add and remove agents to a queue at the set date and
                                 time.

### WebProxy Service

This release introduces WebProxy Service within the Unified CCX server to provide SSL termination and caching services to the Finesse service to reduce latency and improve performance.
                                 For more information, see WebProxy Service section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Gadget developers must bypass the proxy to access the updated gadget responses for testing purposes. For more information,
                                 see Best Practices for Gadget Development section in REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide .

### Cloud Connect

Cloud Connect is an infrastructure component that hosts services that enable integration with Cisco Webex Cloud Services,
                                 such as Cisco Webex Experience Management .

### Cisco Webex Experience Management Post-Call Survey

Cisco Webex Experience Management is the platform for Customer Experience Management (CEM) , integrated with powerful tools that allow you to see your business
                                 from your customers' perspective. Experience Management powers customer journey mapping, text analytics, and predictive modeling using the feedback collected from customers via
                                 different channels such as email, SMS, and IVR.

After enabling Experience Management in Unified CCX:

Administrators can configure IVR, SMS, or email post-call surveys to collect feedback directly from customers. Configure the
                                       IVR survey when an inline survey has to be played to the customer at the end of a call. Configure the SMS or email survey
                                       when a survey link has to be sent to the customer after a call allowing them to provide feedback at their convenience.

Administrators can configure and add gadgets that can be viewed on the Finesse desktop. The Customer Experience Journey gadget
                                       displays the feedback provided by the customer across all the previous interactions. The Customer Experience Analytics gadget
                                       displays the performance of teams managed by the supervisor or the aggregated feedback data from all the customers about the
                                       agent.

Agents and supervisors can view pulse of the customers through industry standard metrics such as NPS, CSAT, and CES or other
                                       KPIs.

For information about how to enable and configure Experience Management , see Cisco Webex Experience Management chapter in the Cisco Unified Contact Center Express Features Guide

For information about the design considerations for triggering a post-call survey, see Cisco Webex Experience Management chapter in the Solution Design Guide for Cisco Unified Contact Center Express

### Customer Journey Analyzer for Business Metrics (Trials)

Customer Journey Analyzer is a cloud service that processes historical contact center data from on-premise deployment to generate specific Business
                                 Metrics across the contact center. It displays trends to help you identify patterns and gain insight for continuous improvement.
                                 You can view the Abandoned Contacts dashboard on the Customer Journey Analyzer which enables supervisors and business analysts to identify where contacts are being abandoned and take appropriate action.
                                 You can use Customer Journey Analyzer to create visualizations using Customer Activity Records, Customer Session Records, and Agent Activity Records.

Customer Journey Analyzer is available as Trials. Please contact your Cisco Support to get started on Trials.

### Smart Licensing

Cisco Smart Licensing helps you to procure, deploy, and manage licenses easily, and report license consumption. It pools the
                                 license entitlements in a single account and allows you to move licenses freely across virtual accounts. Smart Licensing is
                                 enabled across Cisco products and is managed by Cisco Smart Software Manager ( Cisco SSM ) or Cisco Smart Software Manager On-Prem ( Cisco SSM On-Prem ).

Smart Licensing registers the product instance, reports license usage, and obtains the necessary authorization from Cisco SSM or Cisco SSM On-Prem .

Cisco Workforce Optimization licenses are not supported with Smart Licensing. Consequently, customers who upgrade to 12.5
                                             must continue with Classic Licensing if they want to continue using Cisco WFO. Alternatively, customers who want to move to
                                             Smart Licensing for Unified CCX must consider migrating to the SolutionsPlus version of Workforce Optimization.

### Unified CCX Health Check Utility

This utility helps administrators to check the overall health of the Unified CCX system. Administrators can examine the following:

Hardware usage —CPU, Memory, Disk Space, and Disk I/O Latency status.

Unified CCX configuration —Configured parameters such as Agents, Skills, CSQs, Outbound Campaigns, Supervisors per team, and so on.

Database —Status, Replication status, Space usage, Number of Wallboard/External clients, and so on.

Unified CM configuration in Unified CCX —AXL, JTAPI, RmCm, and so on.

### MRCP V2 Support

Along with MRCP v1, MRCP v2 is supported for communicating with third-party ASR-TTS servers. For the complete list of supported
                                 VXML tags and attributes, see the topic Unified CCX VoiceXML Elements in the Cisco Unified Contact Center Express Getting Started with Scripts, Release 12.5(1) .

### Secure RTP for Unified CCX

This release ensures the RTP streamed for IVR is secured between gateway and the IVR port. When secure RTP is enabled, the
                                 signaling channel (JTAPI) between Unified CCX and Unified CM is also secured and encrypted.

### Cisco Unified CCX Editor

Unified CCX Editor Web Launcher, a Java based application that is supported on Windows, Mac, and Linux has been introduced.
                                 You must download the .jnlp file (Java Web start) from the Cisco Unified CCX Administration in order to use the editor.

### Delete Customer Collaboration Platform Configuration

Customer Collaboration Platform configuration can now be deleted using the Unified CCX Administration interface.

## Updated Features

### Security Updates

#### Security Enhancements

After installation (Fresh install) and prior to upgrade, you must copy the following certificates to Unified CCX Tomcat trust
                                       store:

If a self-signed certificate is used, upload the Tomcat certificates from all nodes of the CUCM cluster, Customer Collaboration Platform (CCP), and Standalone Cisco Unified Intelligence Center (CUIC).

If a CA signed or private CA signed certificate is used, upload root CA certificate of CUCM, CCP, and Standalone CUIC.

In this release, only TLS 1.2 is supported.

If the HTTP Content-type header is not explicitly set in HTTP trigger responses (in the Set Http Contact Info window of Editor), the Unified CCX system will assign Content-type: text/html; charset=utf-8 as the default header.

In the Unified CCX Script, if the URL of Make REST Call step is configured with HTTPS URL,
                                       the hostname in the URL and the hostname in the SSL certificate (either in CN or one of the SubjectAltName ) are checked to ensure
                                       that they are the same. This behavior can be disabled by making necessary
                                       changes in the scripts. For more information about script changes, see the Make REST Call section in Cisco Unified
                                          Contact Center Express Editor Step Reference Guide , available at https://developer.cisco.com/docs/contact-center-express/#!preface .

### Bubble Chat Support on Mobile Devices

From Unified CCX Release 12.5(1), Bubble Chat is supported on both desktop and mobile devices. To use Bubble Chat on mobile
                                 devices, you must integrate the latest chat widget code snippet into your website. For more information, see Integration of Chat Code into Customer Website in Cisco Unified Contact Center Express Administration and Operations Guide .

You can disable the download of Chat Transcript by modifying the Chat Widget code.

For more information, see Unified CCX Administration and Operations Guide .

### API Enhancements

The response structure has changed for Get Application with Script Parameters .

APIs that are related to scheduling resources are added. For more information, see Cisco Unified Contact Center Express Developer Guide, Release 12.5(1) .

## Deprecated Features

Deprecated features are fully supported. However, there is no additional development for deprecated features. These features
                              may be scheduled to be removed in a future release. Plan to transition to the designated replacement feature. If you are implementing
                              a new deployment, use the replacement technology rather than the deprecated feature.

### Customer Journey Analyzer

The trial of Customer Journey Analyzer feature has been concluded. This feature is not available from release 12.5(1) SU1.

### Internet Explorer 11

Support for Internet Explorer version 11 is deprecated.

## Important Notes

Agent desktops must be synchronized with NTP server so that the time in the auto incrementing fields of Live Data reports
                           match the server time.

This release does not support the 300 agent deployment model. Deployments that require more than 100 agents will have to use
                           the 400 agent OVA profile. The vRAM required for the 400 agent OVA profile has increased from 16GB to 20GB. Customers who
                           want to use Cloud Connect services with the BE6000 must increase the vRAM from 10GB to 14GB. For information about Resource
                           Requirements, refer to the Virtualization Wiki .

As the OVA profile is changed for 400 agent model deployments, if you do not change the OVA settings, upgrade will fail at
                                       Switch Version. For fresh install, new OVA must be used for deployment. For more information, see Cisco Unified Contact Center Express Design Guide .

Caution

Ensure that the reservation of CPU and memory adhere to the specification mentioned in the Virtualization Wiki .

After upgrading Unified CCX, the CAs that are not approved by Cisco are removed from the platform trust store. However, you
                           can add them back, if necessary.

For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki .

For information about adding a certificate, see the procedure from step 5 onwards under Obtain and Upload CA Certificate section in Cisco Unified Contact Center Express Administration and Operations Guide .

You can download Chat Transcript in only HTML format.

## Removed and Unsupported Features

### Removed Features

Classic Chat feature has been removed. The configuration of the Classic Chat in the previous release will not be migrated
                                    during an upgrade to this release. Customers must configure the Bubble Chat widget available in the Cisco Unified CCX Administration.

### Chat Transcript Download in a PDF Format

The chat transcript cannot be downloaded in a PDF format.

### Mobile Skill Manager

Mobile Skill Manager is not supported.

### TLS

TLS 1.0 and 1.1 are not supported.

### Cisco Context Service

Cisco Context Service is not supported.

### Unsupported Options on Finesse for Direct Preview Outbound

Finesse does not support Skip, Skip-Next, Skip-Close, Reject, Cancel Reservation, and Do Not Call for direct preview outbound
                              calls.

### Unsupported Features and Configurations for Progressive and Predictive Agent Outbound

Unsupported Features and Configurations for Progressive and Predictive Agent Outbound

The "Get Reporting Statistic" step is not supported for progressive and predictive agent-based outbound campaigns.

Unified CCX does not support the translation or modification of the phone number that it uses to dial outbound calls. If
                                    any "voice translation rules" that are configured in the gateway modify the phone number, those rules are not supported.

You can use either of the following two supported methods to modify a dialed number in the gateway:

To remove the initial digits of the phone number, use forward-digits or digit-strip in the dial-peer configuration.

To add a prefix to the phone number, use prefix in the dial-peer configuration.

For Outbound campaigns outside North America, additional configuration is required to add the area-code-to-time-zone mapping.
                                    For more information, see the Cisco Unified Contact Center Express Administration and Operations Guide , located at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html .

For multi-country Outbound campaigns, the area code must also include the country code.

Unified CCX dialer will dial outbound contacts only if the publisher database is in the "IN SERVICE" state.

Finesse does not support the Do Not Call option.

If you are not on Smart Licensing, outbound license usage is not captured in the License Utilization Cisco Unified Intelligence
                                    Center report.

You must enable Agent AutoAnswer manually for agent-based progressive and predictive calls when you upgrade from an older Unified CCX release.

### Unsupported Configuration for IPv6

Cisco Unified Communications Manager does not support SIP IPv6 signaling over UDP where the maximum transmission unit (MTU)
                                    is greater than 1500. To ensure that you do not experience intermittent call failure, change the transport protocol to TCP.

For more information, see the "Important Notes" section of the Release Notes for Cisco Unified Communications Manager , located at:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html

Also, see "CSCuo71306" for details on this limitation.

When using IPv6 and Outbound dialer, use a voice gateway IOS that contains the fix for "CSCul43754" .

### Unsupported Configurations and Scenarios for Unified CCX

Unified CCX does not support the following configurations:

CTI route points with directory numbers (DNs) that are members of line groups and, by extension, that are members of hunt
                                    lists of Unified CM.

Shared lines for CTI ports and CTI route points.

Agent devices cannot be shared with any other Directory Number, irrespective of the configured partition. (the Agent device
                                    and Directory Number must have 1:1 relationship).

ICD call answer or ICD call transfer using any third-party attendant console desk software.

Within the same script, using the "Place Call" step to generate a call and then placing the call, back into the same queue (creating a call loop).

SIP REFER between a switchboard and Unified CCX if the transfer is completed after the call is answered on the Unified CCX
                                    CTI port because of media reestablishment issues.

During TTS prompt playback, if the call is put on hold and then retrieved, the prompt does not continue from the position
                                    at which it was left.

Use of "Consult Transfer" , "Direct Transfer" , or "Redirect" to a translation pattern that maps back to a route point.

Use of "Consult Transfer" , "Redirect" , and "Place Call" steps to invoke or dial into "Conference Now" conferences.

The following scenarios have issues:

External -> Redirect to Unmonitored device -> Call Forward No Answer (CFNA) to UCCX RP

Use of Redirect Step to an unmonitored device which then uses CFNA to a UCCX route point.

External -> Consult Transfer to RP ->Consult Transfer to RP -> Redirect to Unmonitored device

External -> Redirect to RP -> Consult Transfer to RP -> Redirect to Unmonitored device

External -> Consult Transfer to RP -> Redirect to RP -> Redirect to Unmonitored device

External -> Consult Transfer to RP -> Redirect to Unmonitored device

Thus, use the Call Redirect Step in the script instead of Call Consult Transfer.

Unified CCX doesn't completely support E.164 numbering plan for route point directory numbers (DN).

This limitation is because of the Unified CM limit on device name length set as 15 characters. We add "_" between the device
                                    name prefix and the DN. So we support a maximum of 13 characters in the DN as device name prefix is mandatory and hence at
                                    least one character is needed there. For example, (Device name prefix) + '_' + (length of DN) = 15 ==> [(1 + '_' + 13) = 15].

Cisco Unified CCX system does not support modification, addition or deletion of the CTI ports and the CTI Route Points from
                                    the Cisco Unified Communication Manager. Performing the same can lead to issues with non-contiguous DN range for which Cisco
                                    Tomcat on Unified CCX Server needs to be restarted.

When the supervisor monitors the Team Performance report and during the time if there is any update or modification done
                                    to the team, this doesn't get updated automatically. The supervisor should refresh the browser page or select the respective
                                    team again to view the Team Performance report.

Use of two(2) wildcard CTI Route Points that overlap with each other is not supported. For example, Route Point 1: 123XXXX
                                    and Route Point 2: 1234XXX overlap with one another and is not supported.

However, a wildcard CTI Route point can overlap with a full DID (best match pattern) that doesn't contain a wildcard. For
                                    example, Route Point 1: 123XXXX and Route Point 2: 1234567 is supported.

A discrepancy in reports is observed when a call is transferred using Cisco Jabber by multiple agents in the same call flow.
                                    Use the Cisco Finesse desktop to transfer calls.

SIP URI dialing for CTI route points, CTI ports, and agent extensions.

Mid Call Caller ID updates when call is routed to Unified CM via MGCP gateway.

When incoming calls are routed to Unified CM via MGCP gateway, any mid call caller ID updates are reflected only after the
                                                call is connected.

### Unsupported Actions for Unified CCX Agents

Use of the following softkeys on a Cisco Unified IP Phone is not supported:

Barge

cBarge

DND

GPickup

iDivert

Conference Now

Park

Pickup

### Unsupported Configurations for Agent Phones

The following configurations are not supported for agent phones:

Two lines on an agent phone that have the same extension but exist in different partitions.

Unified CCX extension that is assigned to multiple devices.

Configuring the same Unified CCX extension in more than one device profile, or configuring the same Unified CCX extension
                                    in any combination of device profiles and devices. (Configuring a Unified CCX extension in a single device profile is supported.)

Silent Monitoring by supervisors who are logged in with Extend and Connect.

In the Unified Communications Manager Administration Directory Number Configuration web page for each Unified CCX line, setting
                                    Maximum Number of Calls to a value other than 2.

In the Unified Communications Manager Administration Directory Number Configuration web page for each Unified CCX line, setting
                                    Busy Trigger to a value other than 1.

No Cisco Unified Communications Manager device can be forwarded to the Unified CCX extension of an agent.

The Unified CCX extension of an agent cannot be configured to forward to a Cisco Unified CCX Trigger or CTI route point.

Configuring the Unified Communications Manager Intercom feature.

Configuring the Hold Reversion feature.

Agent extensions cannot be added to hunt lists or hunt groups. If an agent has only one line, the agent phone cannot be part
                                    of a hunt list or hunt group. In the case of multiple lines, none of the first four configured lines must be part of the hunt
                                    group. For more details on multiple lines support and number of monitored lines, see the Cisco Unified Contact Center Express Design Guide , located at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-implementation-design-guides-list.html .

Call Forward All to extensions which Unified CCX does not have control over. For example, if an agent extension has Call Forward
                                    All to a PSTN extension or Directory Number on another cluster which Unified CCX is unaware of.

All the Cisco IP Phones for Cisco Finesse IP Phone Agent currently do not support the Simplified New Call UI.

### Supported Configurations for Agent Phones

To determine the phone devices that are supported by Cisco Finesse and for use by Cisco Finesse IP Phone agents, see the Unified
                              CCX Compatibility related information located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

The following configurations are supported on agent phones:

A Unified CCX extension that is configured on a single device (but not on multiple devices).

A Unified CCX extension that is configured in a single device profile (but not in multiple device profiles).

Multiple agents sharing the same Unified CCX extension, which you can set up as follows:

Configure the Unified CCX extension to a single phone (not in a device profile).

Associate the phone with all the agents who will use this extension.

Select the appropriate directory number (DN) as the Unified CCX extension for each agent.

In this configuration, only one agent at a time can be logged in.

All agents who currently have the Unified CCX extension to be shared must log out before you configure additional agents to
                                                      share that extension.

Video is now supported if you are using Cisco Jabber for Windows as agent phone. The agent desktop where Jabber is used for
                                    Video should comply to the Cisco Jabber hardware requirements listed in the Cisco Jabber for Windows 11.0.x and 11.1.x Release Notes , located at:

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Windows/11_0/RN/JABW_BK_C5E7828C_00_cisco-jabber-windows-11-release-notes.html .

### Unsupported and Supported Configurations for Remote Agents

Unified CCX supports Cisco Expressway 8.7.1. The current version of Cisco Expressway does not support BiB and thus the contact
                              center cannot achieve silent monitoring and recording functionalities.

### Unsupported Features in Unified Communications Manager and Cisco Business Edition 6000

The following Unified Communications Manager features are not supported by Unified CCX. These features are disabled by default
                              and you should not enable them for Unified CCX. For more information about these features, see Unified Communications Manager
                              documentation, located at:

https://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html .

Block External to External Transfer.

DSCP IP CTIManager to Application service parameter.

You can enable this service parameter for Unified Communications Manager, but doing so does not affect Unified CCX.

Advanced Ad Hoc Conference Enabled service parameter.

Drop ad hoc conference when the creator leaves the conference.

Signaling (QSIG) Path Replacement (PR).

This feature must be disabled when Unified CCX is deployed. To disable this feature, set the Unified Communications Manager
                                    service parameters Path Replacement Enabled and Path Replacement on Tromboned Calls to False.

Forced Authorization Code and Client Matter Code.

Because these features can be enabled per route pattern, you should turn them off for all route patterns in the Unified Communications
                                    Manager cluster that Unified CCX might use. Enabling these features for route patterns that Unified CCX does not use does
                                    not affect Unified CCX.

Multilevel precedence and preemption (MLPP).

You can enable this feature for devices in the cluster that do not interact with Unified CCX.

Do not use Unified Communications Manager Administration to add or change CTI ports or route points that are used by Unified
                                    CCX or application users that are created by Unified CCX.

### Unsupported Features in Custom Reports

The Do Not Call field is no longer available. While upgrading, report will not be generated if the Do Not Call column is present in the custom report. You can generate the report by removing the Do Not Call column from the custom reports.

A Custom report that was created from a Unified CCX Stock Report may not work as expected if the report definition of the
                                    original Stock Report is modified in the new release.

## Third Party
                        	 Software Impacts

See the Unified CCX
                           		Compatibility related information located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html for information on third-party software.

| Note | This feature is available from Unified CCX R12.5(1) ES02. |
|---|---|

| Note | This feature is available from Unified CCX R12.5(1) ES02. |
|---|---|

| Note | This feature is available from Unified CCX R12.5(1) ES02. |
|---|---|

| Note | Customer Journey Analyzer is available as Trials. Please contact your Cisco Support to get started on Trials. |
|---|---|

| Note | Cisco Workforce Optimization licenses are not supported with Smart Licensing. Consequently, customers who upgrade to 12.5
                                             must continue with Classic Licensing if they want to continue using Cisco WFO. Alternatively, customers who want to move to
                                             Smart Licensing for Unified CCX must consider migrating to the SolutionsPlus version of Workforce Optimization. |
|---|---|

| Note | You can disable the download of Chat Transcript by modifying the Chat Widget code. |
|---|---|

| Note | As the OVA profile is changed for 400 agent model deployments, if you do not change the OVA settings, upgrade will fail at
                                       Switch Version. For fresh install, new OVA must be used for deployment. For more information, see Cisco Unified Contact Center Express Design Guide . |
|---|---|

| Caution | Ensure that the reservation of CPU and memory adhere to the specification mentioned in the Virtualization Wiki . |
|---|---|

| Note | You can use either of the following two supported methods to modify a dialed number in the gateway: To remove the initial digits of the phone number, use forward-digits or digit-strip in the dial-peer configuration. To add a prefix to the phone number, use prefix in the dial-peer configuration. |
|---|---|

| Note | When incoming calls are routed to Unified CM via MGCP gateway, any mid call caller ID updates are reflected only after the
                                                call is connected. |
|---|---|

| Note | All agents who currently have the Unified CCX extension to be shared must log out before you configure additional agents to
                                                      share that extension. |
|---|---|