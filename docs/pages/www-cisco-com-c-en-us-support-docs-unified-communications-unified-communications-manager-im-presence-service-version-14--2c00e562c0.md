---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-version-14--2c00e562c0
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service-version-14/220329-troubleshoot-im-and-presence-server-with.html
retrieved_at: 2026-08-16T23:40:20.911027+00:00
---

Troubleshoot IM and Presence Server with Synchronization Issues

# Troubleshoot IM and Presence Server with Synchronization Issues

### Download Options

Updated: March 31, 2023

Document ID: 220329

Contents

## Contents

## Introduction

This document describes how to troubleshoot when Instant Messaging and Presence (IM and Presence) server has synchronization issue with LDAP via CUCM.

## Prerequisites

### Requirements

The information in this document is based on these software and hardware versions:

- Cisco Unified Communications Manager (CUCM) 12.5 SU(7)

- IM and Presence 12.5 SU(7)

- Secure Shell (SSH) / Command Line Interface (CLI) usage

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

In a CUCM  and IM and Presence deployment the information about the Lightweight Directory Access Protocol (LDAP) is managed by the CUCM and the IM and Presence takes the information from the CUCM directly; however, when there is a change in the LDAP server like a change in the IP address it is important to verify if the information on the CUCM database and the IM and Presence database are in sync otherwise it cannot be possible for the IM and Presence to get the information about new LDAP IP Address; for example, when there is a healthy sync between nodes the output for the query must be exactly the same in both nodes via the CLI (CUCM and IM and Presence)

CUCM (correct entry)

```
admin : run sql select * from ldapauthenticationhost pkid                                 tkldapprotocol hostname   priority sslenabled portnumber ==================================== ============== ========= ======== ========== ========== Correct_pkid_information_1 1 IP_ADDRESS 1 f 3268
```

IM and Presence servers (correct entry)

```
admin : run sql select * from ldapauthenticationhost pkid                                 tkldapprotocol hostname   priority sslenabled portnumber ==================================== ============== ========= ======== ========== ========== Correct_pkid_information_1           1 IP_ADDRESS 1 f 3268
```

On the other hand, if the result of the query presents a mismatch where CUCM has the new accurate LDAP information but not the IM and Presence:

CUCM (correct entry)

```
admin : run sql select * from ldapauthenticationhost pkid                                 tkldapprotocol hostname   priority sslenabled portnumber ==================================== ============== ========= ======== ========== ========== Correct_pkid_information_1 1 IP_ADDRESS 1 f 3268
```

IM and Presence servers (Old entries)

```
admin : run sql select * from ldapauthenticationhost pkid                                 tkldapprotocol hostname         priority sslenabled portnumber ==================================== ============== =============== ======== ========== ========== Incorrect_old_pkid_information_1 1 OLD_ IP_ADDRESS_1 1 f 3268 Incorrect_old_pkid_information_2     1              OLD_IP_ADDRESS_2  1       f          3268
```

It is needed to troubleshoot the mismatch from the IM and Presence side.

## Troubleshoot

In order to troubleshoot it is needed to collect certain logs previously set to debug from IM and Presence nodes

- Cisco Sync Agent.

- Cisco XCP Router.

- Event Viewer Application Log.

- Event Viewer System Log.

## Log Analysis

If the output of the mentioned commands has a clear mismatch of information between CUCM node and IM and Presence node it is necessary to verify the traces for Cisco Sync Agent Service where it is possible to identify this error

```
2021-11-15 12:13:16,950 DEBUG [main] sync.SyncUtil - clearNodeRebootNotification(): notifInfo.description = srm.automatic.failover.peerdown, notifInfo.node = example_domain_dot_com, localHostname = domain_dot_com 2021-11-15 12:13:16,950 INFO  [main] sync.CcmSyncAgent - SyncAgent is running on Subscriber node. Put it in wait mode
```

Also when this command is entered it is possible to see a failure on Sync Agent Status

```
admin:run sql select syncstatus from epassyncagentcfg syncstatus ========================================================================== Sync Completed, but currently failed to connect to the CUCM Database Monitor. Retrying... 2021-11-15 01:04:27
```

### Workaround and Fix

When the IM and Presence Pub sees itself like Sub there is a chance for mismatch, hence no update from IM and Presence side, then it is imperative to make sure that the lines in the box are present via root on IM and Presence Subscriber nodes but not in the IM and Presence Publisher node, those lines indicate that the node is tagged as a Subscriber

```
[root@impname ciscotac]# cat /usr/local/platform/conf/platformConfig.xml <CUPDBHost> <ParamNameText>Host Name for the CUP DB Pub node</ParamNameText> <ParamDefaultValue>none</ParamDefaultValue> <ParamValue>domain_dot_com</ParamValue> </CUPDBHost> [root@impname ciscotac]# cat /usr/local/cm/conf/dbl/prefs.xml <entry key="publisher" value="domain_dot_com"/> It is important to notice that the above tags:
```

```
CUPDBHost
```

```
<entry key="publisher" value="domain_dot_com"/>
```

must not be present in this file in IM and Presence Pub, hence if those lines appear to be present on the IM and Presence Publisher then they need to be removed because that tag ( CUPDBHost ) must appear only on IM and Presence subscriber node platformConfig.xml file as it indicates it is a subscriber node.

Restart the Sync Agent Status from IM and Presence Pub and verify that the database is now in sync on IM and Presence Pub CLI

```
admin : run sql select * from ldapauthenticationhost pkid                                 tkldapprotocol hostname   priority sslenabled portnumber ==================================== ============== ========= ======== ========== ========== Correct_pkid_information_1 1 IP_ADDRESS 1 f 3268
```

Verify the sync status as well

```
admin:run sql select syncstatus from epassyncagentcfg syncstatus ============================= Completed 2022-10-15 15:03:55
```

Note : This behavior is described in the the present defect on IM and Presence: Cisco bug ID CSCuy18383

## Related Information

- Cisco Technical Support & Downloads

### Revision History

1.0

31-Mar-2023

Initial Release

### Contributed by Cisco Engineers

Mario Aguilar Olea

Cisco TAC Escalation Engineer

### This Document Applies to These Products

- Unified Communications Manager IM and Presence Service Version 14

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 31-Mar-2023 | Initial Release |