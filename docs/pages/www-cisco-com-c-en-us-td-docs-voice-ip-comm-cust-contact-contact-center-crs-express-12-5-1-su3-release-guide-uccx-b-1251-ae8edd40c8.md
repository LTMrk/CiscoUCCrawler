---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-release-guide-uccx-b-1251-ae8edd40c8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/release/guide/uccx_b_1251su3_solution-release-notes/uccx_b_1252solution-release-notes_chapter_01.html
retrieved_at: 2026-08-16T20:57:50.460019+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU3

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU3

Updated: May 8, 2023

Chapter: Cisco Unified Contact Center Express

## Chapter: Cisco Unified Contact Center Express

# Cisco Unified Contact Center Express

## New Features

The following commands are added as part of smart licensing management:

License smart hostname enable – This command is used to enable the privacy of UCCX during smart license registration with
                                 CSSM/On-prem SSM.

License smart hostname disable – This command is used to disable the privacy of UCCX during smart license registration with
                                 CSSM/On-prem SSM.

For more information, refer to Specific License Reservation Commands section in Command Line Interface chapter of Cisco Unified
                           Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/series.html#~tab-documents .

## Updated Features

The following features are updated for this release:

The product instance license reporting for smart licensing is refreshed every 8 hours.

The product instance immediately transitions to Out of Compliance state when CSSM reports out-of-compliance.

The type of license (Standard or Premium) reported is based on true consumption by agents and not on the configured value.

OAuth 2.0 support for IMAP — Unified CCX supports OAuth 2.0 for IMAP protocol (receiving the email) in the current Microsoft
                                 Office 365 integrations. SMTP (sending the email) may continue to use Basic authentication until Microsoft supports Basic
                                 authentication with SMTP.

## Deprecated Features

### Webex WFO Data Explorer

Cisco Webex WFO Data Explorer has been deprecated from Release 12.5(1) onward.

Webex WFO Data Explorer will be discontinued on March 14th, 2025 and will be replaced by Webex WFO Insights.

Till March 14th, 2025, both Webex WFO Data Explorer and Webex WFO Insights will be available for use.

Ensure that you update your subscription (change or modify) by March 28th, 2025, to maintain uninterrupted access to Webex
                              WFO Insights. For details, see the FAQ .

## Important Notes

Before upgrading to Release 12.5(1) SU3, you must download the pre-upgrade COP from https://software.cisco.com/download/home/270569179.

The following table lists the COP files that you need to apply prior to performing an upgrade:

Version

Release 12.5(1) SU3 Pre-Upgrade COP Name

11.6(2)

ciscouccx.1162.1251SU3PREUPGRADE.51.cop.sgn

ucos.keymanagement.v01.cop.sgn

12.0(1)

ciscouccx.1201.1251SU3PREUPGRADE.4.cop.sgn

ucos.keymanagement.v01.cop.sgn

12.5(1)

ciscouccx.1251.1251SU3PREUPGRADE.4.cop.sgn

ucos.keymanagement.v01.cop.sgn

12.5(1) SU1

ciscouccx.1251.SU1.1251SU3PREUPGRADE.59.cop.sgn

ucos.keymanagement.v02.cop.sgn

12.5(1) SU2

ucos.keymanagement.v02.cop.sgn

Version

Release 12.5(1) SU3 Pre-Upgrade COP Name

11.6(2)

ciscosm.keymanagement.v01.cop.sgn

ciscosm.refreshupgrade.pre12.5.cop.sgn

12.0(1)

ciscosm.keymanagement.v01.cop.sgn

ciscosm.refreshupgrade.pre12.5.cop.sgn

12.5(1)

ciscoccp.keymanagement.v01.cop.sgn

12.5(1) SU1

ciscoccp.keymanagement.v02.cop.sgn

12.5(1) SU2

ciscoccp.keymanagement.v02.cop.sgn

There is no specific order you must follow while installing the pre-upgrade COP files.

You must install the COP files on both the publisher and the subscriber nodes. The changes take effect immediately after you
                                             install the preupgrade COP files. Reboot is not needed.

No COP file is needed for a new installation.

Unified CCX now supports Chromium-based Microsoft Edge and does not support the earlier versions of Edge. For the list of
                                 browsers and operating systems that are supported, see Unified CCX Software Compatibility Matrix .

With the announcement from Microsoft to disable Basic authentication, Unified CCX supports OAuth 2.0 IMAP protocol (receiving
                                 the email) in the current Microsoft Office 365 integrations. Simple Mail Transfer Protocol (SMTP) may continue to use Basic
                                 authentication until Microsoft supports Basic authentication with SMTP. This feature is available from 12.5(1) SU2 ES03.

Unified CCX now supports Private Network Access (PNA) in Chrome from 12.5(1) SU2 ES04.

FIPS 140-2 mode is supported only on releases that have been through FIPS compliance.

In a HA setup, FIPS 140-2 mode must be first enabled or disabled on the publisher and then on the subscriber. Before enabling
                                 or disabling FIPS 140-2 mode on the subscriber, ensure that all the services are running on the publisher.

Ensure that SRTP is disabled before enabling or disabling FIPS 140-2 mode in Unified CCX. You can enable SRTP after enabling
                                 or disabling FIPS 140-2 mode in Unified CCX.

When FIPS 140-2 mode is enabled or disabled, the keys and certificates are regenerated, and the Unified CCX server reboots.
                                 While rebooting, the system performs the cryptographic modules integrity check, and runs certification self-tests.

Back up the system before and after enabling FIPS 140-2 mode.

When SRTP is disabled on your system and if you are restoring from a backup that was taken when SRTP was enabled, you must
                                 disable SRTP in the System Parameters page after the restore.

When SRTP is enabled on your system and if you are restoring from a backup that was taken when SRTP was disabled, you must
                                 disable and enable SRTP again in the System Parameters page after the restore.

You can localize most of the messages by using Unified CCX Administration. However, some of the accessibility messages that
                                 are read by the screen reader on the Bubble Chat interface have to be localized in the HTML code snippet.

An SRTP-enabled HA setup requires distinct RmCm provider users. So, the system generates a separate RmCm Provider User Id
                                 with the suffix " _ccxsub " for the subscriber node.

Associate devices and device profiles only with the RmCm Provider User that is configured in the Cisco Unified CM Configuration
                                 page (primary RmCm user).

Agent desktops must be synchronized with NTP server so that the time in the auto incrementing fields of Live Data reports
                                 match the server time.

From Unified CCX Release 12.5(1), the 300 agent deployment model is not supported. Deployments that require more than 100
                                 agents have to use the 400 agent OVA profile. The vRAM required for the 400 agent OVA profile has increased from 16GB to 20GB.
                                 Customers who want to use Cloud Connect services with the BE6000 must increase the vRAM from 10GB to 14GB. For information
                                 about Resource Requirements, refer to the Virtualization Wiki .

If FIPS must be enabled on 12.5(1) SU3, the CUCM version to be used is 14.0 SU3. This is because of change in the security
                                 provider used in the product.

As the OVA profile is changed for 400 agent model deployments, if you do not change the OVA settings, the upgrade fails at
                                             Switch Version. For fresh install, the new OVA must be used for deployment. For more information, see Cisco Unified Contact Center Express Design Guide .

Caution

Ensure that the reservation of CPU and memory adhere to the specification mentioned in the Virtualization Wiki .

After upgrading Unified CCX, the CAs that are not approved by Cisco are removed from the platform trust store. However, you
                                 can add them back, if necessary.

For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki .

For information about adding a certificate, see the procedure from step 5 onwards under the Obtain and Upload CA Certificate section in Cisco Unified Contact Center Express Administration and Operations Guide .

You can download the Chat Transcript in only HTML format.

You can configure the maximum number of concurrent sessions for a user of the following applications: Cisco Identity Service
                                 Management, Disaster Recovery System, Cisco Unified CCX Administration, Cisco Finesse Administration, Cisco Unified Serviceability,
                                 Cisco Unified CCX Serviceability, Cisco Unified OS Administration, and Cisco Unified Intelligence Center.

If a user reaches the configured limit, further login attempts are rejected. The maximum number of concurrent sessions is
                                 configured by using the set webapp session maxlimit command. For more information about this command, see the Command Line Interface chapter in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

The DataConn container consumes CPU resources. If DataConn is not being used, use the utils cloudconnect stop dataconn command to shut the container down. This command needs to be executed after every reboot from each of the nodes.

## Removed and Unsupported features

### Removed features

The Classic Chat feature has been removed. The configuration of the Classic Chat in the previous release won’t be migrated
                                    during an upgrade to this release. Customers must configure the Bubble Chat widget available in the Cisco Unified CCX Administration.

### Unsupported features

From release 12.5(1) onwards, Unified CCX doesn’t support the Trusted List of Hosts in HTTP referrer header feature.

From release 12.5(1) SU1 onwards, Unified CCX doesn't support the following commands:

utils uccx notification-service log

utils uccx notification-service log disable

utils uccx notification-service log enable

utils uccx notification-service log status

### Hosted Collaboration Solution for Contact Center support withdrawn

From release 12.5(1) SU3 onwards, Unified CCX won’t support Hosted Collaboration Solution for Contact Center. There will be
                              no new security updates, non-security updates, assisted support options or online technical content updates.

### Chat transcript download in a PDF format

The chat transcript can’t be downloaded in a PDF format.

### Mobile skill manager

Mobile Skill Manager isn’t supported.

### TLS

TLS 1.0 and 1.1 aren’t supported.

### Directed Call Park

The Directed Call Park feature on consult calls is not supported.

### Cisco context Service

Cisco Context Service isn’t supported.

### Customer Journey Analyzer

The trial of the Customer Journey Analyzer feature has been concluded. This feature isn’t available from release 12.5(1) SU1.

### Internet Explorer

Support for Internet Explorer is removed.

### Unsupported options on Finesse for Direct Preview Outbound

Finesse doesn’t support Skip, Skip-Next, Skip-Close, Reject, Cancel Reservation, and Do Not Call for direct preview outbound
                              calls.

### Unsupported features and configurations for Progressive and Predictive Agent Outbound

Unsupported Features and Configurations for Progressive and Predictive Agent Outbound

The "Get Reporting Statistic" step isn’t supported for progressive and predictive agent-based outbound campaigns.

Unified CCX doesn’t support the translation or modification of the phone number that it uses to dial outbound calls. If any "voice translation rules" that are configured in the gateway modify the phone number, those rules aren’t supported.

You can use either of the following two supported methods to modify a dialed number in the gateway:

To remove the initial digits of the phone number, use forward-digits or digit-strip in the dial-peer configuration.

To add a prefix to the phone number, use prefix in the dial-peer configuration.

For Outbound campaigns outside North America, additional configuration is required to add the area-code-to-time-zone mapping.
                                    For more information, see the Cisco Unified Contact Center Express Administration and Operations Guide , located at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html .

For multi-country Outbound campaigns, the area code must also include the country code.

Unified CCX dialer dials outbound contacts only if the publisher database is in the "IN SERVICE" state.

Finesse doesn’t support the Do Not Call option.

If you aren’t on Smart Licensing, outbound license usage isn’t captured in the License Utilization Cisco Unified Intelligence
                                    Center report.

You must enable Agent AutoAnswer manually for agent-based progressive and predictive calls when you upgrade from an older Unified CCX release.

### Unsupported configuration for IPv6

Cisco Unified Communications Manager doesn’t support SIP IPv6 signaling over UDP where the maximum transmission unit (MTU)
                                    is greater than 1500. To ensure that you don’t experience intermittent call failure, change the transport protocol to TCP.

For more information, see the "Important Notes" section of the Release Notes for Cisco Unified Communications Manager , located at:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html

Also, see "CSCuo71306" for details on this limitation.

When using IPv6 and Outbound dialer, use a voice gateway IOS that contains the fix for "CSCul43754" .

### Unsupported configurations and scenarios for Unified CCX

Unified CCX doesn’t support the following configurations:

CTI route points with directory numbers (DNs) that are members of line groups and, by extension, that are members of hunt
                                    lists of Unified CM.

Shared lines for CTI ports and CTI route points.

Agent devices can’t be shared with any other Directory Number, irrespective of the configured partition. (The Agent device
                                    and Directory Number must have a 1:1 relationship).

ICD call answer or ICD call transfer using any third-party attendant console desk software.

Within the same script, using the "Place Call" step to generate a call and then placing the call, back into the same queue (creating a call loop).

SIP REFER between a switchboard and Unified CCX if the transfer is completed after the call is answered on the Unified CCX
                                    CTI port because of media reestablishment issues.

During TTS prompt playback, if the call is put on hold and then retrieved, the prompt doesn’t continue from the position at
                                    which it was left.

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

Unified CCX doesn't completely support the E.164 numbering plan for route point directory numbers (DN).

This limitation is because of the Unified CM limit on device name length set as 15 characters. We add "_" between the device
                                    name prefix and the DN. So we support a maximum of 13 characters in the DN as the device name prefix is mandatory and hence
                                    at least one character is needed there. For example, (Device name prefix) + '_' + (length of DN) = 15 ==> [(1 + '_' + 13)
                                    = 15].

Cisco Unified CCX system doesn’t support modification, addition or deletion of the CTI ports and the CTI Route Points from
                                    the Cisco Unified Communication Manager. Performing the same can lead to issues with the non-contiguous DN range for which
                                    Cisco Tomcat on Unified CCX Server needs to be restarted.

When the supervisor monitors the Team Performance report and during the time if there’s any update or modification done to
                                    the team, this doesn't get updated automatically. The supervisor should refresh the browser page or select the respective
                                    team again to view the Team Performance report.

Use of two(2) wildcard CTI Route Points that overlap with each other isn’t supported. For example, Route Point 1: 123XXXX
                                    and Route Point 2: 1234XXX overlap with one another and isn’t supported.

However, a wildcard CTI Route point can overlap with a full DID (best match pattern) that doesn't contain a wildcard. For
                                    example, Route Point 1: 123XXXX and Route Point 2: 1234567 is supported.

A discrepancy in reports is observed when a call is transferred using Cisco Jabber by multiple agents in the same call flow.
                                    Use the Cisco Finesse desktop to transfer calls.

SIP URI dialing for CTI route points, CTI ports, and agent extensions.

Mid-Call Caller ID updates when the call is routed to Unified CM through MGCP gateway.

When incoming calls are routed to Unified CM through MGCP gateway, any mid-call caller ID updates are reflected only after
                                                the call is connected.

### Unsupported actions for Unified CCX agents

Use of the following softkeys on a Cisco Unified IP Phone isn’t supported:

Barge

cBarge

DND

GPickup

iDivert

Conference Now

Park

Pickup

### Unsupported configurations for agent phones

The following configurations aren’t supported for agent phones:

Two lines on an agent phone that have the same extension but exist in different partitions.

Configuring the same Unified CCX extension in more than one device profile, or configuring the same Unified CCX extension
                                    in any combination of device profiles and devices. (Configuring a Unified CCX extension in a single device profile is supported.)

Silent Monitoring by supervisors who are logged in with Extend and Connect.

In the Unified Communications Manager Administration Directory Number Configuration web page for each Unified CCX line, setting
                                    Maximum Number of Calls to a value other than 2.

In the Unified Communications Manager Administration Directory Number Configuration web page for each Unified CCX line, setting
                                    Busy Trigger to a value other than 1.

No Cisco Unified Communications Manager device can be forwarded to the Unified CCX extension of an agent.

The Unified CCX extension of an agent can’t be configured to forward to a Cisco Unified CCX Trigger or CTI route point.

Configuring the Unified Communications Manager Intercom feature.

Configuring the Hold Reversion feature.

Agent extensions can’t be added to hunt lists or hunt groups. If an agent has only one line, the agent phone can’t be part
                                    of a hunt list or hunt group. In case of multiple lines, none of the first four configured lines must be part of the hunt
                                    group. For more details on multiple lines support and the number of monitored lines, see the Cisco Unified Contact Center Express Design Guide , located at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-implementation-design-guides-list.html .

Call Forward All to extensions which Unified CCX doesn’t have control over. For example, if an agent extension has Call Forward
                                    All to a PSTN extension or Directory Number on another cluster which Unified CCX is unaware of.

All the Cisco IP Phones for Cisco Finesse IP Phone Agent currently don’t support the Simplified New Call UI.

### Supported configurations for agent phones

To determine the phone devices that are supported by Cisco Finesse and for use by Cisco Finesse IP Phone agents, see the Unified
                              CCX Compatibility related information located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

The following configurations are supported on agent phones:

A Unified CCX extension that is configured on a single device (but not on multiple devices).

A Unified CCX extension that is configured in a single device profile (but not in multiple device profiles).

Multiple agents sharing the same Unified CCX extension, which you can set up as follows:

Configure the Unified CCX extension to a single phone (not in a device profile).

Associate the phone with all the agents who use this extension.

Select the appropriate directory number (DN) as the Unified CCX extension for each agent.

In this configuration, only one agent at a time can be logged in.

All agents who currently have the Unified CCX extension to be shared must log out before you configure more agents to share
                                                      that extension.

Video is now supported if you’re using Cisco Jabber for Windows as the agent phone. The agent desktop where Jabber is used
                                    for Video should comply to the Cisco Jabber hardware requirements listed in the Cisco Jabber for Windows 11.0.x and 11.1.x Release Notes , located at:

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Windows/11_0/RN/JABW_BK_C5E7828C_00_cisco-jabber-windows-11-release-notes.html .

### Unsupported and supported configurations for remote agents

Unified CCX supports Cisco Expressway 8.7.1. The current version of Cisco Expressway doesn’t support BiB and thus the Contact
                              Center can’t achieve silent monitoring and recording functionalities.

### Unsupported features in Unified Communications Manager and Cisco Business Edition 6000

The following Unified Communications Manager features aren’t supported by Unified CCX. These features are disabled by default
                              and you shouldn’t enable them for Unified CCX. For more information about these features, see the Unified Communications Manager
                              documentation, located at:

https://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html .

Block External to External Transfer.

DSCP IP CTIManager to Application service parameter.

You can enable this service parameter for Unified Communications Manager, but doing so doesn’t affect Unified CCX.

Advanced Ad Hoc Conference Enabled service parameter.

Drop the Ad Hoc conference when the creator leaves the conference.

Signaling (QSIG) Path Replacement (PR).

This feature must be disabled when Unified CCX is deployed. To disable this feature, set the Unified Communications Manager
                                    service parameters Path Replacement Enabled and Path Replacement on Tromboned Calls to False.

Forced Authorization Code and Client Matter Code.

Because these features can be enabled per route pattern, you should turn them off for all route patterns in the Unified Communications
                                    Manager cluster that Unified CCX might use. Enabling these features for route patterns that Unified CCX doesn’t use and doesn’t
                                    affect Unified CCX.

Multilevel precedence and preemption (MLPP).

You can enable this feature for devices in the cluster that don’t interact with Unified CCX.

Don’t use Unified Communications Manager Administration to add or change CTI ports or route points that are used by Unified
                                    CCX or application users that are created by Unified CCX.

### Unsupported features in Custom reports

The Do Not Call field is no longer available. While upgrading, a report won’t be generated if the Do Not Call column is present in the custom report. You can generate the report by removing the Do Not Call column from the custom reports.

A Custom report that was created from a Unified CCX Stock Report may not work as expected if the report definition of the
                                    original Stock Report is modified in the new release.

## Third Party Software Impacts

See the Unified CCX Compatibility related information located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html for information on third-party software.

| Version | Release 12.5(1) SU3 Pre-Upgrade COP Name |
|---|---|
| 11.6(2) | ciscouccx.1162.1251SU3PREUPGRADE.51.cop.sgn ucos.keymanagement.v01.cop.sgn |
| 12.0(1) | ciscouccx.1201.1251SU3PREUPGRADE.4.cop.sgn ucos.keymanagement.v01.cop.sgn |
| 12.5(1) | ciscouccx.1251.1251SU3PREUPGRADE.4.cop.sgn ucos.keymanagement.v01.cop.sgn |
| 12.5(1) SU1 | ciscouccx.1251.SU1.1251SU3PREUPGRADE.59.cop.sgn ucos.keymanagement.v02.cop.sgn |
| 12.5(1) SU2 | ucos.keymanagement.v02.cop.sgn |

| Version | Release 12.5(1) SU3 Pre-Upgrade COP Name |
|---|---|
| 11.6(2) | ciscosm.keymanagement.v01.cop.sgn ciscosm.refreshupgrade.pre12.5.cop.sgn |
| 12.0(1) | ciscosm.keymanagement.v01.cop.sgn ciscosm.refreshupgrade.pre12.5.cop.sgn |
| 12.5(1) | ciscoccp.keymanagement.v01.cop.sgn |
| 12.5(1) SU1 | ciscoccp.keymanagement.v02.cop.sgn |
| 12.5(1) SU2 | ciscoccp.keymanagement.v02.cop.sgn |

| Note | There is no specific order you must follow while installing the pre-upgrade COP files. You must install the COP files on both the publisher and the subscriber nodes. The changes take effect immediately after you
                                             install the preupgrade COP files. Reboot is not needed. No COP file is needed for a new installation. |
|---|---|

| Note | As the OVA profile is changed for 400 agent model deployments, if you do not change the OVA settings, the upgrade fails at
                                             Switch Version. For fresh install, the new OVA must be used for deployment. For more information, see Cisco Unified Contact Center Express Design Guide . |
|---|---|

| Caution | Ensure that the reservation of CPU and memory adhere to the specification mentioned in the Virtualization Wiki . |
|---|---|

| Note | You can use either of the following two supported methods to modify a dialed number in the gateway: To remove the initial digits of the phone number, use forward-digits or digit-strip in the dial-peer configuration. To add a prefix to the phone number, use prefix in the dial-peer configuration. |
|---|---|

| Note | When incoming calls are routed to Unified CM through MGCP gateway, any mid-call caller ID updates are reflected only after
                                                the call is connected. |
|---|---|

| Note | All agents who currently have the Unified CCX extension to be shared must log out before you configure more agents to share
                                                      that extension. |
|---|---|