---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-release-gui-636ce8b62b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/release/guide/rcct_b_cce-solution-rns-12-6/cuic_m_release-notes-1261.html
retrieved_at: 2026-08-16T19:38:14.313186+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

# Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

Updated: May 14, 2021

Chapter: Cisco Unified Intelligence Center

## Chapter: Cisco Unified Intelligence Center

# Cisco Unified Intelligence Center

## New Features

### Accessibility Compliance

This release ensures that the Cisco Unified Intelligence Center reporting application complies with Web Content Accessibility Guidelines (WCAG) 2.0. For more information on the supported JAWS version, see Voluntary
                                 Product Accessibility Templates (VPAT) report for Contact Center at https://www.cisco.com/c/en/us/about/accessibility/voluntary-product-accessibility-templates.html .

### Custom Logon Messages

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge). For information about supported versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Maximum Session Count

If a Unified Intelligence Center user reaches the maximum configured session count, that user can log in to another session
                                 only after signing out from an active session or if an active session times out due to inactivity. The session timeout duration
                                 is configured by using the set cuic properties session-timeout command. The maximum session count is configured by using the set webapp session maxlimit command. For more information, see the Command Line Interface chapter in the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

### Commands

The following commands have been introduced:

#### Allow External Links

The administrator can enable or disable the external links in Unified Intelligence Center dashboard using the set cuic properties allow-external-links { on|off } command.

#### CUIC Logging

In this release, the log trace setting in OAMP interface is removed. The administrator must use the utils cuic logging commands to set the log traces. To change the log level configuration on each node in the cluster, the command must be run
                                 separately on each node.

#### Report Query Timeout

The administrator can set the report query execution timeout value using the set cuic properties report-query-timeout number of seconds command. This command is applicable when you run the report using the interface and does not apply to scheduled reports.

For more information, see the Command Line Interface chapter in the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

## Updated Features

### SMTP Settings

If you select the Use TLS check box ( Cluster Configuration > SMTP Settings ), the communication between the Cisco Unified Intelligence Center and the mail server is encrypted with TLS. By default,
                                 SMTP TLS port 465 is used to connect to the mail server. For more information, see the Cluster Configuration chapter in the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

### All Users Group Access

The administrator can enable or disable the parameter using the set cuic properties allow-allusers-group-ui command.

## Important Notes

### Allow External Links

After the upgrade, the external links in the Unified Intelligence Center dashboard will be disabled. If required, the administrator
                              can enable the external links again using the set cuic properties allow-external-links command.

If enabled, the contents from external links are rendered within the HTML iFrame in the dashboard. This will include the frame-src* directive in the Content Security Policy of the Unified Intelligence Center web pages.

### Gadget URL

JSP format is not supported for Unified Intelligence Center gadgets (Live Data and Historical). To change the JSP format references
                              to XML format, the administrator must run the following commands on the primary Cisco Finesse server.

utils finesse layout updateCuicGadgetUrl 12.6.1+ —Updates the CUIC URL configured in the Cisco Finesse desktop layout to work with Release 12.6(1) and later versions. For
                                    more information, see the Upgrade section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Live Data

If Cisco Unified Intelligence Center is upgraded to version 12.6(1) and your Live Data (standalone) server remains on an earlier
                                    version (11.6(1), 12.0(1), or 12.5(1)), ensure that you update the Live Data server with the latest ES for that release. This
                                    is required for the Live Data gadgets to work in Finesse desktop.

Live Data 12.6(1) requires a new OVA for all deployments except the 2000 Agent deployment.

### HTTP Access

Cisco Unified Intelligence Center is not accessible using port 8081 in any manner. From this release, port 8081 is disabled
                              and does not redirect to HTTPS.

## Deprecated Features

None.

## Removed and Unsupported Features

### Log Trace

In this release, the log trace setting in OAMP is removed. The administrator must use the utils cuic logging commands to set the log traces.

The following commands are removed:

set cuic trace

show cuic trace

utils cuic authorize_remote_node

### Internet Explorer 11

In this release, support for Internet Explorer version 11 is removed. Edge Chromium (Microsoft Edge) is the replacement. For
                              more information about supported browsers, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### SNMP Object Identifiers (OIDs)

The following SNMP OIDs are removed:

cuicGeneralInfoServerName

cuicGeneralInfoServerDescription

cuicGeneralInfoVersion

cuicGeneralInfoStartTime

cuicGeneralInfoTimeZoneName

cuicGeneralInfoOpsConsoleURL

cuicReportingTotalKickedOffHistoricalReports

cuicReportingTotalKickedOffRealTimeReports

cuicSchedulerStatus

cuicSchedulerEmailServerStatus

cuicSchedulerJobsCompletedCount

cuicSchedulerJobsRunningCount

cuicSchedulerJobsFailedCount

cuicSecurityLoginFailedAttempts

cuicThreadsMaxAvailable

cuicThreadsRunning

cuicQueuedTasks

cuicQueuedTasksMax

## Third Party Software Impact

None.