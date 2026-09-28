---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-release-gui-b7e1e62c86
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/release/guide/rcct_b_cce-solutions-rns-12-6-2/cuic_m_release-notes-1262.html
retrieved_at: 2026-08-16T19:37:28.471124+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

# Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

Updated: February 27, 2026

Chapter: Cisco Unified Intelligence Center

## Chapter: Cisco Unified Intelligence Center

# Cisco Unified Intelligence Center

## New Features

None.

## Updated Features

### Logging and Tracing Information

The following utils oamp logging commands are introduced to set the log traces:

```
utils oamp show logging-level
```

```
utils oamp update logging-level
```

For information, see the Command Line Interface section in the Administration Console User Guide for Cisco Unified Intelligence Center .

### SNMP Object Identifiers (OIDs)

The following counters related to permalink are added to SNMP:

cuicReportingHistoricalHTMLPermalinkDataSetRead

cuicReportingHistoricalEXCELPermalinkDataSetRead

cuicReportingHistoricalXMLPermalinkDataSetRead

cuicReportingHistoricalHTMLPermalinkDataSetCreated

cuicReportingHistoricalEXCELPermalinkDataSetCreated

cuicReportingHistoricalXMLPermalinkDataSetCreated

cuicReportingRealtimeHTMLPermalinkDataSetRead

cuicReportingRealtimeEXCELPermalinkDataSetRead

cuicReportingRealtimeXMLPermalinkDataSetRead

cuicReportingRealtimeHTMLPermalinkDataSetCreated

cuicReportingRealtimeEXCELPermalinkDataSetCreated

cuicReportingRealtimeXMLPermalinkDataSetCreated

## Important Notes

### Allow External Links

If you are upgrading from 12.5(1) SU or earlier version,  the external links in the Unified Intelligence Center dashboard
                              will be disabled. If required, the administrator can enable the external links again using the set cuic properties allow-external-links command.

If enabled, the contents from external links are rendered within the HTML iFrame in the dashboard. This will include the frame-src* directive in the Content Security Policy of the Unified Intelligence Center web pages.

### Gadget URL

The JSP format is not supported for Unified Intelligence Center gadgets (Live Data and Historical). If you are upgrading from
                              12.5(1) SU or earlier version, to change the JSP format references to XML format, the administrator must run the following
                              commands on the primary Cisco Finesse server.

utils finesse layout updateCuicGadgetUrl 12.6.1+ —Updates the Unified Intelligence Center URL configured in the Cisco Finesse desktop layout to work with Release 12.6(2) and
                                    later versions. For more information, see the Upgrade section in the Cisco Finesse Administration Guide .

### Cisco IdS Upgrade

Cisco IdS 12.6(2) upgrade requires all SSO clients to log out from SSO, before any of the upgraded nodes is brought online.
                              Deployments using VPN-less access to Finesse desktop should also upgrade the reverse proxy to 12.6(2) before Cisco IdS is
                              upgraded to 12.6(2).

Graceful shutdown feature will not be available for Cisco IdS12.6(2) upgrade for the above reasons. Therefore, you must plan
                              for the required downtime for upgrading Cisco IdS to 12.6(2).

### Live Data

If Unified Intelligence Center is upgraded to 12.6(2) and your Live Data (standalone) server remains on the earlier version,
                                    ensure that you update the Live Data server with the latest ES for that release. This is required for the Live Data gadgets
                                    to work in Finesse desktop.

If you are upgrading Live Data from 12.5(1) ES06 or earlier, the Live Data Virtual Machine(VM) configuration requirement changes
                                    for 12.6(2). For information on configuration requirements, see Virtualization Guide.

AppDynamics monitoring for LiveData-Worker JVM App Agent is disabled by default, because of performance overhead. You can
                                    enable it using the set live-data appd-monitoring enable CLI. For more information on the CLI, see the Live Data CLI Commands Commands section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide.

### Unified Intelligence Center Gadgets Failover in VPN-less Setup

In VPN-less setups, if the primary reverse proxy goes down, the Unified Intelligence Center gadget does not render till the
                              primary node comes back online. If you anticipate an extended downtime of the primary reverse proxy, change the gadget URL
                              in the Desktop Settings to point to the Unified Intelligence Center node that is configured with the failover reverse proxy.
                              For instructions, see the Manage System Settings chapter in the Cisco Finesse Administration Guide .

This issue is addressed in release 12.6(2) ES01. From release 12.6(2) ES01, the Unified Intelligence Center gadget renders
                                          when the primary reverse-proxy goes down.

## Deprecated Features

None.

## Removed and Unsupported Features

### Log Trace

In this release, the log trace setting OAMP Web page is removed. The administrator must use the utils oamp logging commands
                                 to set the log traces.

For information, see the Command Line Interface section in the Administration Console User Guide for Cisco Unified Intelligence Center .

## Third Party Software Impact

For the list of third-party softwares, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.

| Note | This issue is addressed in release 12.6(2) ES01. From release 12.6(2) ES01, the Unified Intelligence Center gadget renders
                                          when the primary reverse-proxy goes down. |
|---|---|