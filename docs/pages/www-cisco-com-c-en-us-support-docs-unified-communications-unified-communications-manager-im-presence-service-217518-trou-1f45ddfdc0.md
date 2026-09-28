---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-217518-trou-1f45ddfdc0
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/217518-troubleshoot-duplicated-users-alerts-on.html
retrieved_at: 2026-08-16T23:38:18.080393+00:00
---

Troubleshoot Duplicated Users Alerts on IM&P Server

# Troubleshoot Duplicated Users Alerts on IM&P Server

### Download Options

Updated: November 3, 2021

Document ID: 217518

Contents

## Contents

## Introduction

This document describes an example and the procedure to perform when duplicated-user alerts are seen on the Cisco IM and Presence (IM&P) nodes.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco IM and Presence Service (IM&P) Server

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background information

A duplicated-user alert normally shows up like this.

```
Monitoring Automation
Additional comments•05-21-2021 09:12:19
Created by: ALE4855981
Message key: ENTER024::APP_LXT_ENTER024_33f00f5388443c6e24801bce325255711c2bb4a475076ba004ac48df6664deb9
Additional Comments: Timestamp: 2021-05-21 13:12:46
Device:
IP address: Not Supported
Component: Not Supported
Severity: 3
Event Name: APP_LXT_MAJOR
Event SourceNode: ENTER024-LXT1
Message: LayerX.Alarms(10.10.10.10) LayerX ALERT_QUEUE table 0x0000033D 0 204
Custom Message: Alarm ID: 51111 (DuplicateUserid) : Event Message: (%[AlertName=SyslogSeverityMatchFound][AlertDetail= At Fri May 21 08:11:00 CDT 2021 on node impPub.ciscolab.com, the following SyslogSeverityMatchFound events generated: #012SeverityMatch : Alert#012MatchedEvent : May 21 08:10:24 impPub local7 1 : 62: impPub.ciscolab.com: May 21 2021 13:10:24.476 UTC : %UC_ReplWatcher-1-DuplicateUserid: %[AppID=Cisco IM and Presence Data Monitor][ClusterID=][NodeID=impPub]: Cisco IM and Presence Data Monitor has detected that two or more users on the system share the same UserID value.#012AppID : Cisco Syslog Agent#012ClusterID : #012NodeID : impPub#012 TimeStamp : Fri May 21 08:10:24 CDT 2021][AppID=Cisco AMC Service][ClusterID=][NodeID=cucmPub]: RTMT Alert
```

Note : The Cisco IM&P Configuration Guide only mentions a single method to identify duplicated users. Nonetheless, there are cases where the utils users validate all command does not show any information or presents an empty output.

## Troubleshoot

For those scenarios, this procedure is advised:

Step 1. Log into the IM&P’s Administration Webpage (GUI) and navigate to the System Troubleshooter tab.

Step 2. If any duplicated user entries have been found there, you can notice the user ID of the aforementioned user.

Step 3. Take note of that user ID and go back to the IM&P’s Command Line Interface (CLI)

Step 4. Run the  command:

run sql select * from enduser where enduser.userid=’ _user_ID ’

The system prints all the entries it can find for that particular user (in this example, the user ID was “ user92 ”)

```
admin:run sql select * from enduser where enduser.userid='user92' pkid                                 userid  xcp_user_id tkuserlocale imaddress           xep106imaddress     directoryuri        mailid              status fkdirectorypluginconfig              deletedtimestamp passwordreverse                                                  tkuserprofile tkassignmentstate ocsprimaryuseraddress   fkucccmcipprofile tkphonepresence primarynodeid xep106userid xep106mailid        auth_pwd login_stamp logout_stamp auth_count pwd_stamp  last_status fkucserviceprofile enablecalendarpresence enablecups discoveryuseridentity ==================================== ======= =========== ============ =================== =================== =================== =================== ====== ==================================== ================ ================================================================ ============= ================= ======================= ================= =============== ============= ============ =================== ======== =========== ============ ========== ========== =========== ================== ====================== ========== ===================== 633780c3-182b-153a-654a-6d073c2248ac user92 11412       1            user92@ciscolab.com user92@ciscolab.com user92@ciscolab.com user92@ciscolab.com 1      b5acd3a6-5ac2-055b-cf27-ba4f818533d6 NULL             aeef2675d3e72b6fbee00a9badf5d944aa016e0a7a302ac9704b79180f63f21e 1             0                 sip:user92@ciscolab.com NULL              NULL            NULL          user92       user92@ciscolab.com 0        2020-05-06                                                 NULL               t                      t 3a15e537-db7c-4b1f-8ff2-1daf5c5d4a05 user92 35283       1            user92@ciscolab.com user92@ciscolab.com user92@ciscolab.com 1                   NULL   NULL                                 NULL             d0d177e67ddc687c526364580c9d0c6ce9b0fb47dc51fed3ced90807105d9de9 100           1                 NULL                    NULL              2802                          user92       user92@ciscolab.com 0        2020-07-23                                                 NULL               f                      f
```

In this case, you see two entries for that particular user.

In order to get rid of those, perform the next steps:

Step 1. Run the command:

run sql delete from enduser where enduser.userid=’u ser_ID ’

Step 2. Navigate to the CUCM Administration page > User Management > End User > Select the duplicated user and bounce (uncheck & then re-check) the user’s Home Node Cluster checkbox in order to create a single entry for the same user

Step 3. Run this query one last time to verify that only a single entry for that user is displayed:

run sql select * from enduser where enduser.userid=’your user ID’

```
admin:run sql select * from enduser where enduser.userid='user92' pkid                                 userid  xcp_user_id tkuserlocale imaddress           xep106imaddress     directoryuri        mailid              status fkdirectorypluginconfig              deletedtimestamp passwordreverse                                                  tkuserprofile tkassignmentstate ocsprimaryuseraddress   fkucccmcipprofile tkphonepresence primarynodeid xep106userid xep106mailid        auth_pwd login_stamp logout_stamp auth_count pwd_stamp  last_status fkucserviceprofile enablecalendarpresence enablecups discoveryuseridentity ==================================== ======= =========== ============ =================== =================== =================== =================== ====== ==================================== ================ ================================================================ ============= ================= ======================= ================= =============== ============= ============ =================== ======== =========== ============ ========== ========== =========== ================== ====================== ========== ===================== 633780c3-182b-153a-654a-6d073c2248ac user92 11412       1            user92@ciscolab.com user92@ciscolab.com user92@ciscolab.com user92@ciscolab.com 1      b5acd3a6-5ac2-055b-cf27-ba4f818533d6 NULL             aeef2675d3e72b6fbee00a9badf5d944aa016e0a7a302ac9704b79180f63f21e 1             0                 sip:user92@ciscolab.com NULL              NULL            NULL          user92       user92@ciscolab.com 0        2020-05-06                                                 NULL               t                      t
```

### Revision History

2.0

03-Nov-2021

Initial Release

1.0

03-Nov-2021

Initial Release

### Contributed by Cisco Engineers

Ivan Rojas

Cisco TAC

### This Document Applies to These Products

- Unified Communications Manager IM & Presence Service

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 03-Nov-2021 | Initial Release |
| 1.0 | 03-Nov-2021 | Initial Release |