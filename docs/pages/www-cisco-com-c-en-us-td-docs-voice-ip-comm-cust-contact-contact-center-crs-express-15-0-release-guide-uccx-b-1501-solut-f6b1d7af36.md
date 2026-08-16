---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-release-guide-uccx-b-1501-solut-f6b1d7af36
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/release/guide/uccx_b_1501_solution-release-notes/uccx_m_1501_cisco-unified-contact-center-express.html
retrieved_at: 2026-08-16T20:56:55.534300+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 15.0

# Release Notes for Cisco Unified Contact Center Express Solution, Release 15.0

Updated: April 30, 2025

Chapter: Cisco Unified Contact Center Express

## Chapter: Cisco Unified Contact Center Express

# Cisco Unified Contact Center Express

## New Features

### Cipher Management

The following new CLI commands are introduced for administrators to manage Ciphers:

utils system tls_ciphers config list —Displays the current list of TLS ciphers.

utils system tls_ciphers config export —Exports the TLS cipher list configured in /usr/local/bin/base_scripts/tls_settings to a specified SFTP location.

utils system tls_ciphers config import —Imports the TLS cipher list from a specified SFTP server location and updates the configuration in /usr/local/bin/base_scripts/tls_settings .

utils system tls_ciphers config reset —Resets the TLS cipher configuration to the base version available with the product's standard release. This will undo any
                                       modifications made to the TLS cipher configuration by restoring it to the base version.

These commands are required to remove weaker ciphers identified during security scans, ensuring compliance with security policies
                                 and industry standards. By customizing the TLS cipher configuration, you can enhance your system’s security posture by disabling
                                 ciphers that are considered vulnerable or outdated. For more information about Cipher Management, see the Cipher Management section in the Cisco Unified Contact Center Express Administration and Operations Guide .

### Secure connections to external database

The connections to external databases from Unified CCX are encrypted. All the "data in transit" is encrypted with TLS 1.2
                                 protocol for the following databases:

Oracle 21c

Oracle 19c

MS SQL Server 2019

MS SQL Server 2016

MS SQL Server 2014 (SP3 or later with CU updates)

For Oracle 19c and Oracle 21c databases, it is necessary to change the JDBC driver from ojdbc6.jar to ojdbc8.jar . The ojdbc6.jar is not compatible with TLS in Unified CCX version 15.0.

For more information about enabling secure database connection, see the Datasource Configuration Web Page section in the Cisco Unified Contact Center Express Administration and Operations Guide .

### Smart Transport

Along with Smart Call Home , now Smart Transport is added. Going forward, Smart Transport will be used as the transport for communicating license usage information to CSSM. For more information about Smart Transport,
                                 see the Configure transport settings for smart licensing section in the Cisco Unified Contact Center Express Administration and Operations Guide .

### Utils Commands

The following new utils commands are added:

utils uccx database reindex tablename : This command allows you to reindex some specific Unified CCX tables.

utils network dns check enable : This command allows you to enable the forward and reverse lookup with DNS after successful change of IP or hostname.

utils network dns check disable : This command allows you to disable the forward and reverse lookup with DNS during IP or hostname change.

For more information about these commands, see the Utils Commands section in the Cisco Unified Contact Center Express Administration and Operations Guide .

### Migrate from 100 OVA to 400 OVA

You can migrate from 100 agent profile (100 OVA) to 400 agent profile (400 OVA). You can perform the following:

Backup 100 OVA setup

Fresh Install 400 OVA setup

Restore the 100 OVA backup on 400 OVA Setup

Trigger OVA migration

For more information, see the Migrate from 100 OVA to 400 OVA section in the Cisco Unified Contact Center Express Administration and Operations Guide .

### Secure connection to Informix database

The connections to Informix database can now be secured. You can secure the connections only with CLI. Use the following CLIs
                                 to manage the connection:

utils uccx informix_ssl status

utils uccx informix_ssl cert generate

utils uccx informix_ssl cert info

utils uccx informix_ssl enable

utils uccx informix_ssl disable

For more information about the CLIs, see the Utils Commands chapter in the Cisco Unified Contact Center Express Administration and Operations Guide .

## Updated Features

Supported Ciphers: The supported list of ciphers in Unified CCX is updated. For the complete list, see the Supported Ciphers section in the Solution Design Guide for Cisco Unified Contact Center Express .

Accessibility: New keyboard shortcuts are introduced, such as, Tab key , Advanced Capabilities , Accept chat , Scroll through chat , and so on. For more information, see the Accessibility section in the Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express .

## Deprecated Features

Smart Call Home (SCH)

Smart Licensing (Smart Agent) will discontinue support for Smart Call Home (SCH) as a communication transport, as SCH is transitioning to End of Life (EOL) .

## Important Notes

CentOS is now replaced with Alma Linux.

If you switch back from Unified CCX 15.0 to any of the previous versions, the chat related information in the Cassandra database,
                                 that are updated for 15.0, will not be synced.

## Removed and Unsupported features

### Removed features

The following licenses are removed:

NFR

Perpetual Premium

Perpetual Enhanced

Flex HCS

The following features have been removed from Unified CCX 15.0 and no longer available:

Cisco Webex Experience Management

Cloud Connect

### Unsupported features

From release 12.5(1) onwards, Unified CCX doesn’t support the Trusted List of Hosts in HTTP referrer header feature.

From release 12.5(1) SU1 onwards, Unified CCX doesn't support the following commands:

utils uccx notification-service log

utils uccx notification-service log disable

utils uccx notification-service log enable

utils uccx notification-service log status

### Chat transcript download in a PDF format

The chat transcript can’t be downloaded in a PDF format.

### Mobile Skill Manager

Mobile Skill Manager isn’t supported.

### TLS

TLS 1.0 and 1.1 aren’t supported.

### Directed Call Park

The Directed Call Park feature on consult calls is not supported.

### Cisco Context Service

Cisco Context Service isn’t supported.

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

None.

| Note | For Oracle 19c and Oracle 21c databases, it is necessary to change the JDBC driver from ojdbc6.jar to ojdbc8.jar . The ojdbc6.jar is not compatible with TLS in Unified CCX version 15.0. |
|---|---|

| Note | You can use either of the following two supported methods to modify a dialed number in the gateway: To remove the initial digits of the phone number, use forward-digits or digit-strip in the dial-peer configuration. To add a prefix to the phone number, use prefix in the dial-peer configuration. |
|---|---|

| Note | When incoming calls are routed to Unified CM through MGCP gateway, any mid-call caller ID updates are reflected only after
                                                the call is connected. |
|---|---|

| Note | All agents who currently have the Unified CCX extension to be shared must log out before you configure more agents to share
                                                      that extension. |
|---|---|