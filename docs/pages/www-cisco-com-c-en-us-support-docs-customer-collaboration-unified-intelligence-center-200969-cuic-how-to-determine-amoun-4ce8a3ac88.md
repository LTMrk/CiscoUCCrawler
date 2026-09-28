---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-200969-cuic-how-to-determine-amoun-4ce8a3ac88
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/200969-CUIC-How-to-Determine-Amount-of-Currentl.html
retrieved_at: 2026-08-16T19:25:21.274461+00:00
---

How to Determine Number of Reporting Users Currently Logged-In in CUIC

# How to Determine Number of Reporting Users Currently Logged-In in CUIC

Updated: October 11, 2017

Document ID: 200969

Contents

## Contents

## Introduction

This document describes a process to check the number of currently logged-in users in Cisco Unified Intelligence Center (CUIC) server.

## Background Information

When you run the CUIC server, you need to ensure that the number of currently logged in users to any reporting node in a cluster do not exceed the limit. For Unified Intelligence Server release 11.0 the limit is - 200 users per node. In case there are more users logged-in to a particular node, this can cause performance issues.

## Problem Example

User with login name ccmadmin closed the browser with CUIC reporting tab and did not logout correctly. You see two (duplicate) sessions in the output. To add to that, an incorrect number of currently logged-in reporting users is shown.

```
admin: utils cuic session list Command executed successfully Session ID details saved to file. To view file, type "file view activelog cuic-session.out" To SFTP file, type "file get activelog cuic-session.out" admin: file view activelog cuic-session.out User: CUIC\ccmadmin - Last Session Time: 13/Feb/2017 13:47:09 - SessionID: E819B0F5114A4A62778CB08C01BAB0F1 User: CUIC\ccmadmin - Last Session Time: 13/Feb/2017 15:04:38 - SessionID: E6AC6567352C245C8061E693BE1DC760 User: ADMINISTRATOR\cuicu1 - Last Session Time: 13/Feb/2017 15:21:17 - SessionID: 4EC191A25D946E5C7BF75AE2E79E0B72 end of the file reached options: q=quit, n=next, p=prev, b=begin, e=end (lines 1 - 3 of 3) : admin: show perf query counter ReportingEngineInfo ReportsUsersLoggedin - Perf class ReportingEngineInfo(ReportsUsersLoggedin) has values: -> ReportsUsersLoggedin = 3
```

## Verify

In order to check the number of users, this CUIC Command Line Interface (CLI) command can be used:

```
admin: show perf query counter ReportingEngineInfo ReportsUsersLoggedin - Perf class ReportingEngineInfo(ReportsUsersLoggedin) has values: -> ReportsUsersLoggedin = 2
```

An alternative way would be to check in Real-Time Monitoring Tool (RTMT) application. Navigate to System -> Performance . Select the node you want to monitor. Then unfold ReportingEngineInfo and double click on ReportsUsersLoggedIn .

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

In some cases this value can reflect not accurate number of logged in users.

A common root cause of this is that users who report to close their browser instead of clicking Log Out button at the top right corner.

In order to get the list of logged in users on a particular node, use this command.

```
admin: utils cuic session list Command executed successfully Session ID details saved to file. To view file, type "file view activelog cuic-session.out" To SFTP file, type "file get activelog cuic-session.out" admin: file view activelog cuic-session.out User: CUIC\ccmadmin - Last Session Time: 13/Feb/2017 15:04:38 - SessionID: E6AC6567352C245C8061E693BE1DC760 User: ADMINISTRATOR\cuicu1 - Last Session Time: 13/Feb/2017 15:21:17 - SessionID: 3860176B2BAD8D8BEB10D4643FBD011F end of the file reached options: q=quit, n=next, p=prev, b=begin, e=end (lines 1 - 3 of 3) :
```

Here you may find CUIC Reporting log reference with UserLoginAttempt (user pressed log in button), UserLoginSuccess and SessionEnd (user pressed log out button) operations.

```
admin: file tail activelog cuic/logs/cuic/ recent regexp "User login or logout" 0000001591: 10.48.47.142: Feb 13 2017 15:01:35.520 +0100: %CCBU__CUIC_SECURITY-7-OPERATION: %[MESSAGE=Total number of login attempts for the server=50][OPERATION_TYPE= UserLoginAttempt ][SESSION_ID= 3860176B2BAD8D8BEB10D4643FBD011F ][USER_ID=]: User login or logout request to server. 0000001636: 10.48.47.142: Feb 13 2017 15:01:35.576 +0100: %CCBU__CUIC_SECURITY-7-OPERATION: %[MESSAGE= Total number of logged-in user instance for the server=3 ][OPERATION_TYPE= UserLoginSuccess ][SESSION_ID= 3860176B2BAD8D8BEB10D4643FBD011F ][USER_ID= ADMINISTRATOR\cuicu1 ]: User login or logout request to server. 0000001683: 10.48.47.142: Feb 13 2017 15:22:01.559 +0100: %CCBU__CUIC_SECURITY-7-OPERATION: %[MESSAGE= Total number of logged-in user instance for the server=2 ][OPERATION_TYPE=SessionEnd][SESSION_ID= 3860176B2BAD8D8BEB10D4643FBD011F ][USER_ID= ADMINISTRATOR\cuicu1 ]: User login or logout request to server.
```

If you do not see SessionEnd event in the log file, it is a clear indication that CUIC server did not receive log out request from a client.

## Solution

Educate reporting users to click Log Out button in CUIC before they close the internet browser.

## Related Articles

- Collecting the Logs for CUIC Performance Issues

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

14-Feb-2017

Initial Release

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 14-Feb-2017 | Initial Release |