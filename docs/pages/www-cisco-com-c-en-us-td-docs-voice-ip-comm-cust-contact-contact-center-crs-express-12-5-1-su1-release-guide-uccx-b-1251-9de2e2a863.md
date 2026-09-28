---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-release-guide-uccx-b-1251-9de2e2a863
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/release/guide/uccx_b_1251su1solution-release-notes/uccx_b_1252solution-release-notes_chapter_010.html
retrieved_at: 2026-08-16T21:01:19.628931+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU1

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Cisco Unified Intelligence Center

## Chapter: Cisco Unified Intelligence Center

# Cisco Unified Intelligence Center

## New Features

## Updated Features

## Important Notes

### Maximum Session Count

If you reach the maximum-configured session count in the Cisco Unified Intelligence Center, you can sign in to another session
                              only after either of the following occurs:

You log out from an active session.

An active session times out due to inactivity.

The session timeout duration is configured by using the set cuic properties session-timeout command. For more information about this command, see the Command Line Interface chapter in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

### Value List Permissions

Upgrading from Unified CCX Release 12.5(1) sets the permissions of all the STOCK value lists for the ALLUSERS group to NONE.
                              If you want a user to use the entire value list, you must reset the permissions manually in Release 12.5(1) SU1.

### Report Execution Timeout

The set cuic properties report-query-timeout command allows you to set the report execution timeout for a query.

By default, the report query execution timeout value is three minutes (180 seconds). You can set the value up to one hour
                              (3600 seconds) .

For more information about this command, see the Command Line Interface chapter in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

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