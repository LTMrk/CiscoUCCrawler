---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-214737-troubleshoot-jabber-login-failure-after-html-8f85a5bbf1
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/214737-troubleshoot-jabber-login-failure-after.html
retrieved_at: 2026-08-16T23:38:30.985739+00:00
---

Troubleshoot Jabber Login Failure after Unified IM and Presence (IM&P) Domain Change or IM Address Scheme

# Troubleshoot Jabber Login Failure after Unified IM and Presence (IM&P) Domain Change or IM Address Scheme

### Download Options

Updated: August 11, 2019

Document ID: 214737

Contents

## Contents

## Introduction

This document describesa problem encountered where Jabber is unable to login after a server reboot or XCP router service stop/start.

## Problem

If there is a requirement to reboot IM&P nodes following a domain name change, or to stop/start the XCP router service due to a change of IM address scheme, Jabber clients login may fail with “cannot communicate with server” error.

## Troubleshooting Steps

In order to troubleshoot this problem, verify these points:

1.     If there are multiple IM&P nodes in the cluster, check the dbreplication on the IM&P primary node CLI mode and ensure the status is showing “(2) Setup Completed”:

```
admin:utils dbreplication runtimestate Cluster Detailed View from IMP01 (2 Servers): PING            DB/RPC/      REPL.          Replication    REPLICATION SETUP SERVER-NAME         IP ADDRESS              (msec)          DbMon?       QUEUE          Group ID       (RTMT) & Details -----------         ----------              ------          -------      -----          -----------    ------------------ IMP01               x.x.x.1                 0.032           Y/Y/Y          0            (g_3)          (2) Setup Completed IMP02               x.x.x.2                 0.340           Y/Y/Y          0            (g_5)          (2) Setup Completed
```

2.     Ensure that on IM&P node(s), both XCP connection manger service and XCP authentication service are in started state.

Choose Diagnostics > System Troubleshooter >XCP Troubleshooter and verify that all are ticked.

3.     Start the Cisco XCP connection manger service and Cisco XCP authentication service manually in CLI if the services are not already started.

```
admin:utils service start Cisco XCP Authentication Service admin:utils service start Cisco XCP Connection Manager
```

Note : When you stop the Cisco XCP Router, all XCP feature services are automatically stopped.

For a basic IM and Presence Service deployment, the following services have to be turned on:

•              Cisco SIP Proxy

•              Cisco Presence Engine

•              Cisco XCP Connection Manager

•              Cisco XCP Authentication Service

### Reference link:

Configuration and Administration of the IM and Presence Service on Cisco Unified Communications Manager, Release 10.5(2)

### Revision History

1.0

11-Aug-2019

Initial Release

### Contributed by Cisco Engineers

Amy Lin

Cisco TAC

### This Document Applies to These Products

- Jabber

- Unified Communications Manager IM & Presence Service

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 11-Aug-2019 | Initial Release |