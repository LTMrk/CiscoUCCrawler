---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-224893-troubleshoot-cuc-with-google-workspace-5cda2b2176
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/224893-troubleshoot-cuc-with-google-workspace.html
retrieved_at: 2026-08-16T18:57:27.239805+00:00
---

Troubleshoot CUC with Google Workspace Mailbox Out of Sync

# Troubleshoot CUC with Google Workspace Mailbox Out of Sync

### Download Options

Updated: September 15, 2025

Document ID: 224893

Contents

## Contents

## Introduction

This document describes how to troubleshoot when Mailbox Out of Sync between CUC and Google Workspace.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unity Connection (CUC)

- Google Workspace

- Simple Mail Transfer Protocol (SMTP)

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The Publisher and Subscriber servers are operational, but the attempts to send voicemail email notifications (Single Inbox or Voicemail to Email feature) failed.

Navigate to the CUC Administration Page > Unified Messaging > Unified Messaging Services > Open the Unified Messaging Account . Even though the configurations are correctly set up, there are errors of synchronization.

UM (Cisco Unity to Google Mail) Out of Sync

UM Validation Results

This error is also seen.

```
Status: User mailbox is out of sync, press Reset for resync Unified Messaging Service: Cisco Unity to Google Mail Service Type: Google Workspace User Corporate Email Address: userid@domain.com [Checked] Synchronize Connection and Google Workspace Mailboxes (Single inbox)
```

## Troubleshoot

### Google Configuration

Step 1. Navigate to the Google Console and delete the service account already created.

Step 2. Add a new service account.

Step 3. Assign these roles

- Service Account Key Admin

- Service Account User

- Pub/Sub Admin

Step 4. Save the account generated and download the Key File (JSON type).

S tep 5. Copy the Client ID of the service account. Step 6. In the OAuth scopes field (Google Admin Console), copy and paste these URLs comma-delimited list of scopes:

Step 7 . Authorized the scopes and save. Step 8. Uploaded the new JSON file into the Google Workspace UMS configuration and save.

If the service has failed after the checks performed, gather the Connection Google Workspace Notifier .

Set these Macrotraces:

- Single Inbox Traces

- Message Tracking Traces

Set these microtraces:

- CsMbxSync: 10-23

- CsEws: All

- EWSNotify: All

- CsWebDav: 10-14

- CuEsd: 0,5,7

- MTA: 10-30

- Cuca: All

- CsExMbxLocator: All

- DBEvent: 3,12

Tip : This microtraces and macrotraces debug levels apply to all Single Inbox / Unified Messaging issues.

In the Connection Google Workspace Notifier, the Invalid "JWT: Token must be a short-lived token (60 minutes) and in a reasonable timeframe" error is seen.

```
14:14:10.894 |3917,,,CuGSuiteSyncSrv,22,GSuiteServiceOpTh-40,com.cisco.unity.gsuite.services.GSuiteActionItems.sendMessage - Try # 1 Google Api send message on gsuite 14:14:11.052 |3917,,,CuGSuiteSyncSrv,23,GSuiteServiceOpTh-40,com.cisco.unity.gsuite.services.GSuiteActionItems.sendMessage - Google Api send message on gsuite failed with message 400 Bad Request { "error" : "invalid_grant", "error_description" : "Invalid JWT: Token must be a short-lived token (60 minutes) and in a reasonable timeframe. Check your iat and exp values and use a clock with skew to account for clock differences between systems." } 14:14:11.052 |3917,,,CuGSuiteSyncSrv,1,GSuiteServiceOpTh-40,com.cisco.unity.gsuite.serviceability.CuGsuiteSyncPerfCounters.incrementHttpsRqstError - Incrementing Http Request Failed counter by 1 14:14:11.052 |3917,,,CuGSuiteSyncSrv,1,GSuiteServiceOpTh-40,com.cisco.unity.gsuite.serviceability.CuGsuiteSyncPerfCounters.incrementHttpsRqstError - Total Http Request Failed after update: 3543 14:14:11.052 |3917,,,CuGSuiteSyncSrv,24,CxnResetSynchService.createNewMsgOnGSuite - 400 Bad Request { "error" : "invalid_grant", "error_description" : "Invalid JWT: Token must be a short-lived token (60 minutes) and in a reasonable timeframe. Check your iat and exp values and use a clock with skew to account for clock differences between systems." } Clock Skew: This suggests that the system clock on the server generating the token may be out of sync with Google's servers. Even a small mismatch (e.g., a few seconds) can cause this issue. 14:14:11.052 |3917,,,CuGSuiteSyncSrv,24,com.cisco.unity.gsuite.services.GSuiteActionItems.sendMessage(GSuiteActionItems.java:1132) com.cisco.unity.gsuite.GSuiteMessageUtility.createMessageOnGmail(GSuiteMessageUtility.java:615) com.cisco.unity.gsuite.GSuiteMessageUtility.createNewMessageOnGmail(GSuiteMessageUtility.java:475) com.cisco.unity.gsuite.reset.CxnResetSynchService.createNewMsgOnGSuite(CxnResetSynchService.java:343) com.cisco.unity.gsuite.reset.CxnResetSynchService.checkWhereToSync(CxnResetSynchService.java:318) com.cisco.unity.gsuite.reset.CxnResetSynchService.syncCnxMessage(CxnResetSynchService.java:282) com.cisco.unity.gsuite.reset.CxnResetSynchService.sync(CxnResetSynchService.java:755) com.cisco.unity.gsuite.reset.UMASyncWorker.resync(UMASyncWorker.java:220) com.cisco.unity.gsuite.reset.UMASyncWorker.run(UMASyncWorker.java:109) java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) java.util.concurrent.FutureTask.run(FutureTask.java:266) java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) java.lang.Thread.run(Thread.java:748)
```

## Solution

The JSON Web Token (JWT) used to authenticate with the Google API is invalid, and that is the reason of the failure, as seen the “invalid grant” error several times through the logs. It is either expired or its timestamp (iat or exp values) is outside the acceptable range.

The Google APIs require tokens to be short-lived (usually 1 hour or less) and the request to be made within the valid timeframe of the token. This is related to how the tokens are handled between the CUC and Google.

Make sure the Time-To-Live (TTL) of the Token is less than 60 minutes and that the Network Time Protocol (NTP) is synced across the servers, computers and Internet.

### Revision History

1.0

17-Sep-2025

Initial Release

### Contributed by Cisco Engineers

Miguel Eduardo Castillo Torres

Technical Consulting Engineer

### This Document Applies to These Products

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Sep-2025 | Initial Release |