---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-116942-technote-uc-00-html-a7073638f6
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/116942-technote-uc-00.html
retrieved_at: 2026-08-16T18:57:56.959006+00:00
---

Unity Connection Cluster Replication Rebuild

# Unity Connection Cluster Replication Rebuild

### Download Options

Updated: November 24, 2015

Document ID: 116942

Contents

## Contents

## Introduction

This document describes steps to verify and attempt to address the issue when replication becomes out of sync or breaks entirely.

## Problem

It is important to know that there are two types of replication that occur within Unity Connection (UC):

- Enterprise Replication (ER) - platform Cisco CallManager (CCM) related

- Unity Connection Replication

### Enterprise Replication

It is important that ER is always Real Time Monitoring Tool (RTMT) state of (2)'s on both the Publisher and the Subscriber.

In order to confirm this, enter the utils dbreplication runtimestate command.

Another helpful command that can be used is utils dbreplication status .

### Unity Connection Replication

Without the proper ER running, Unity Connection Replication does not work correctly. Commands used to troubleshoot UC replication are:

utils cuc cluster overwritedb

utils cuc cluster renegotiate

## Solution

If ER is down (RTMT does not = 2), complete these steps:

On the Subscriber, enter the utils dbreplication stop command. Wait for it to complete before you start the next step.

On the Publisher, enter the utils dbreplication stop command. Wait for it to complete before you start the next step.

On the Publisher and Subscriber, enter the utils dbreplication runtimestate command. Ensure that both servers are RPC reachable column = YES).

On the Publisher, enter the utils dbreplication dropadmindb command.

On the Subscriber, enter the utils dbreplication dropadmindb command. If you run Release 9.x, skip to step 8.

On the Publisher, enter the utils dbreplication clusterreset command. Wait for it to complete before you start the next step.

Restart the Subscriber. Wait for the Subscriber to come back up and services all start before you start the next step.

On the Publisher, enter the utils dbreplication reset all command.

On Publisher and Subscriber, periodically enter the utils dbreplication runtimestate command in order to monitor the RTMT state they each have for one another. They should progress and both ultimately end up at (2) if replication sets up properly. This can take some time.

If RTMT states do not go from 0's to 2's after you wait a good amount of time, collect this information from BOTH the Publisher and the Subscriber:

- utils dbreplication runtimestate

- file get activelog cm/trace/dbl/*.log

- file get activelog cm/trace/dbl/sdi/dbmon*.txt

- file get activelog cm/log/informix/dbl_repl*.log

- file get activelog cm/log/informix/ccm*.log

Open a case with the Technical Assistance Center (TAC) and provide the information collected in step 10.

## Related Information

- Command Line Interface Reference Guide for Cisco Unified Communications Solutions Release 8.6(1)

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

24-Nov-2015

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 24-Nov-2015 | Initial Release |