---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-225038-troubleshoot-hybrid-calendar-with-html-bf87d21898
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/225038-troubleshoot-hybrid-calendar-with.html
retrieved_at: 2026-08-16T22:05:47.492640+00:00
---

Troubleshoot Hybrid Calendar with Exchange Connector Error "Pending Activation by Admin"

# Troubleshoot Hybrid Calendar with Exchange Connector Error "Pending Activation by Admin"

### Download Options

Updated: September 25, 2025

Document ID: 225038

Contents

## Contents

## Introduction

This document describes how to identity and repair errors while enabling Scheduling with Hybrid Calendar with Exchange for Webex users in Control Hub.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Webex Organization.

- Webex Hybrid Calendar.

- Microsoft Exchange Admin Console.

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Control Hub build 20240919-84b27c9

- Microsoft Exchange 15.2 (Build 529.5)

- Chrome browser 129.0.6668.58 (Official Build) (arm64)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

When enabling Hybrid Calendar with Exchange for Webex users in Control Hub, the status does not change to Activated and is stuck in error: "Pending Activation by admin..."

## Control Hub error

At Control Hub > Management > Users > User affected > Hybrid Services > Calendar Service , the status is stuck on " Pending Activation by admin ... "

Control Hub error

## Gathering logs

### Control Hub

From your browser (preferably in incognito mode) :

Chrome: Open DevTools > Network

FireFox: Open Web Developer Tools > Network .

Navogate to admin.webex.com > Management > Users > User affected > Hybrid Services > Calendar Service .

Click Status and locate the Request URL which ends with &serviceId=squared-fusion-cal .

Request URL

### Request URL

```
https://uss-a.wbx2.com/uss/api/v1/orgs/904cbfb5-0f49-4339-a40c-ad473ac7ab24/userJournal/45877071-3636-473f-a6f6-c34e91514609?limit=100&serviceId=squared-fusion-cal
```

The userId appears after /userJournal/ and before the ?limit parameter. This identifier is needed to lookup inside of the Expressway Logs.

```
45877071-3636-473f-a6f6-c34e91514609
```

Tip : The fastest way to find the user ID is by checking the URL in the address bar.

Address Bar

### Expressway Connector

With the userId from Control Hub, proceed to enable Diagnostic Logging, deactivate and reactivate the user, wait roughly five (5) minutes, and then collect the logs.

Navigate to Maintenance > Diagnostics > Diagnostic logging .

Caution : Make sure to set Log Levels to DEBUG or WARNING to trap the required logs. Go to Maintenance > Diagnostics > Hybrid Services Log Levels .

Hybrid Services Log Levels

### Understanding Logging Levels

Navigate to Maintenance > Diagnostics > Diagnostic logging and click Start new log button to initiate logging. If Expressways are part of a Cluster, enable them in the primary node.

Diagnostic logging

Deactivate the user affected from Control Hub and wait 4 -7  minutes, then click Stop logging button.

Stop logging

Click Collect log to initiate the process of gathering and compiling diagnostic information into a downloadable archive.

Collect log

After the archive is created, the Download log button appears, allowing the administrator to save the file to their local machine. This file is typically uploaded to a Cisco TAC (Technical Assistance Center) case for analysis.

Download log

### Expressway Connector log analysis

With the userId of the affected user collected from Control Hub:

Extract the Expressway logs locally and locate and open the file loggingsnapshot_<Expressway-HostName>_<Date>.txt

```
diagnostic_log_ccnp-expressway-hybrid1_2025-09-22_12/58/19 > loggingsnapshot_ccnp-expressway-hybrid1_2025-09-22_12/58/19.txt
```

Filter out userId and locate the EWSServices.bindToCalendar request right after the discover event containing the userId.

```
2025-09-22T08:38:08.654-04:00 localhost UTCTime="2025-09-22 12:38:08,654" Module="hybridservices.c_cal" Level="ERROR" Thread="pool-4474-thread-1" TrackingId="" Detail="EWSServices.bindToCalendar(00000000-0000-0000-0000-000000000000, https://srv-xchge.vizcainovich.com/ews/exchange.asmx) threw ServiceRequest exception.The request failed. microsoft.exchange.webservices.data.ServiceResponseException: The account does not have permission to impersonate the requested user."
```

```
2025-09-22T08:38:08.657-04:00 localhost UTCTime="2025-09-22 12:38:08,656" Module="hybridservices.c_cal" Level="DEBUG" Thread="DiscoveryExecutor-1" TrackingId="ATLAS_91cf6741-7fb2-4687-8fcb-f5d07def961d_t:b2efac54_82" Detail="Sending 14 discover events for e34d8673-d937-4d0a-b5f3-ea5b83c7600bDiscoverEvent{userId=fd7a4d33-baae-4051-9f6e-afafa06460f8, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=313b303a-607e-41cb-bdd5-a8142b5e304a, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=b2d5da40-9457-4a05-8cfc-b0659df7cce2, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=c71fb15e-e1dd-4de1-8217-0747afeb7484, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=45877071-3636-473f-a6f6-c34e91514609, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=005cc3e4-2c55-466a-8350-8a9dba37effb, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=7235db5d-102b-4e77-b0a8-8b6dc0a6d554, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=9df909c1-e737-49f6-ba75-f6c5e2e6e668, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=fc74df95-8a56-45b2-83b7-c4bb0b561ec9, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=6e0ae1de-463c-44fa-97cf-02ec70888d0c, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=c6df9679-ef9f-49b2-8ca9-19167b4ef2e0, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=34b0ebf5-000c-48ee-944f-e0c04318c8c3, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=63e5774b-8c8e-4232-bba2-c2ca67f7575c, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}DiscoverEvent{userId=022f9f11-6590-4f43-83ab-5789bc62d11b, serviceType=squared-fusion-cal, clusterId=bd300d7d-40f2-4b68-91df-22e516074d59, score=-1, isOperational=false}"
```

Log snippets show multiple attempts including usedId 45877071-3636-473f-a6f6-c34e91514609 pointing out to the impersonation account used to commnicate between Expressway Connector and the Exchange server showing this error :

```
The account does not have permission to impersonate the requested user.
```

## Validation

### Exchange server

Validate the impersonation account from the Exchange server running this Exchange Server PowerShell command to list all ApplicationImpersonation role assignments :

```
Get -ManagementRoleAssignment -Role ApplicationImpersonation
```

Management Role Assignment

Confirm that the impersonation mailbox is using the Throttling Policy for Hybrid Calendar from Exchange server running this Exchange Server PowerShell command:

```
Get -ThrottlingPolicyAssociation -Identity "impersonation account" | findstr "ThrottlingPolicy"
```

Throttling Policy Association

Lookup at your Hybrid Calendar deployment records to identify the RoleAssignment given to the impersonation account during the first time setup. In this scenario, the RoleAssignment is:

```
CalendarConnectorAcct
```

### MSExchange Event Viewer logs

From the Exchange server, go to Event Viewer > Applications and Services Logs > MSExchange Management and filter out Information level events containing "CmdletLogs" and/or name of the RoleAssignment "CalendarConnectorAcct if any.

Event Viewer logs

Double click on the event to open its properties.

Event Properties

### Exchange Management Shell

By using the build-in session history of Exchange Server PowerShell, commands used in the current session can be tracked.

The history is not available to other sessions and is deleted when the session ends.

Using the PSReadLine history tracks the commands used in all PowerShell sessions.

The history is written to a central file per host. That history file is available to all sessions and contains all past history. The history is not deleted when the session ends.

In this scenario, the built-in session is showing this output after running this command:

```
Get-History
```

Get-History

## Root Cause

Exchange admin deleted the RoleAssignment for the impersonation account using this Exchange Server PowerShell command:

```
Remove-ManagementRoleAssignment "CalendarConnectorAcct" -Confirm:$false
```

This action breaks the impersonation account role unable to subscribe users in Exchange server and causes users and workspaces activation to fail.

## Solution

From Exchange Server PowerShell, run this command to create a new ManagementRomeAssignment with name "CalendarConnectorAcct" and assign it to impersonation account hybridcal.

```
new-ManagementRoleAssignment -Name:CalendarConnectorAcct -Role:ApplicationImpersonation -User 'VIZCAINOVICH\hybridcal'
```

new-ManagementRoleAssignment

From Expressway server, restart the Calendar connector to accelerate the activation process for the affecter user(s) and/or workspace(s).

Navigate to Applications > Hybrid Services > Connector Management > Calendar Connector > Enabled hyperlink.

Connector Management

Inside of Calendar Connector, click the Enable to open the drop down menu.

Enabled button

Select Disabled from the drop-down menu.

drop-down menu

Click Save button to apply the changes in the Calendar Connector.

Save

After changes are saved, it lands in Connector Management. Click Check Calendar Connector Status at the bottom of the Calendar Connector service.

Calendar Connector Status

Wait a few minutes until the Calendar Connector initializes.

Restarted

Once Calendar Connector initializes, Expressway connectivity shows Exchange address and users successfully subscribed.

Connected

Return to Control Hub > Management > Users > Affected user shows Calendar service fully activated.

Activated

Expressway logs showing affected userId 45877071-3636-473f-a6f6-c34e91514609 getting a valid subscription from Exchange server:

```
2025-09-24T20:03:55.984-04:00 localhost UTCTime="2025-09-25 00:03:55,984" Module="hybridservices.c_cal" Level="DEBUG" Thread="ews-subscription-0" TrackingId="EXP_d5913454-640d-495e-b132-60ac0C76050F_t:5718eca5" Detail="Creating subscription for user 45877071-3636-473f-a6f6-c34e91514609 in group com.cisco.wx2.calendar.connector.ews.EWSServices$EWSSubscriptionConnection@4fce863b"

2025-09-24T20:03:55.984-04:00 localhost UTCTime="2025-09-25 00:03:55,984" Module="hybridservices.c_cal" Level="DEBUG" Thread="ews-subscription-0" TrackingId="EXP_d5913454-640d-495e-b132-60ac0C76050F_t:5718eca5" Detail="Binding user 45877071-3636-473f-a6f6-c34e91514609"

2025-09-24T20:03:56.049-04:00 localhost UTCTime="2025-09-25 00:03:56,049" Module="hybridservices.c_cal" Level="DEBUG" Thread="ews-subscription-0" TrackingId="EXP_d5913454-640d-495e-b132-60ac0C76050F_t:5718eca5" Detail="DAS.core:  activateUser: 45877071-3636-473f-a6f6-c34e91514609"
```

Note : The alarm ‘The account does not have permission to impersonate the requested user’ can have multiple causes; however, all of them are related to the impersonation account configuration or the Exchange server.

## Related Information

- Hybrid Services and Connector Troubleshooting

- Collect Expressway/VCS Diagnostic Log for Expressway MRA

Chrome DevTools

- Firefox DevTools

### Revision History

1.0

25-Sep-2025

Initial Release

| DEBUG | Detailed information for diagnosing issues |
|---|---|
| INFO | General operational messages |
| WARN | Potentially harmful situations |
| ERROR | Error events that still allow the app to continue running |
| FATAL | Very severe error events that lead to app termination |
| TRACE | The most verbose level, offering the most detailed diagnistics for in-depth troubleshooting |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 25-Sep-2025 | Initial Release |