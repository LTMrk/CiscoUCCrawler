---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-118883-technote-cuc-00-html-db84fad972
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/118883-technote-cuc-00.html
retrieved_at: 2026-08-16T18:58:05.532042+00:00
---

Single Inbox Synchronization Issues with Microsoft Exchange On-Premises Deployments

# Single Inbox Synchronization Issues with Microsoft Exchange On-Premises Deployments

### Download Options

Updated: April 2, 2015

Document ID: 118883

Contents

## Contents

## Introduction

This document provides information on the synchronization issues seen between Cisco Unity Connection (CUC) and Microsoft Exchange On-Premises deployments.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUC.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Issues

There are three types of synchronization issues:

- No synchronization

- Delayed synchronization from both sides (CUC to Exchange Server and vice versa)

- Delayed synchronization from Exchange Server to CUC

## Troubleshoot

This section provides information on how to troubleshoot the three issues. The first two issues are combined into one section as the approach to troubleshoot the issues is the same.

### Delayed or No Synchronization between CUC and Exchange

There could be various reasons for which there is no or delayed synchronization between CUC and Exchange. In this scenario, check communication failures between CUC and the Exchange Server either via the CLI or by log collection via the Real-Time Monitoring Tool (RTMT).

RTMT

Choose Trace & Log Central > Collect Files . Choose Connection Mailbox Sync logs and proceed.

Root

On CUC (/var/log/active/cuc) via the CLI:

In order to view the file, enter cat <filename> or vi <filename> , where <filename> is diag_CuMbxSync_xxxxxxxx.uc.

Admin CLI

The logs can also be viewed via the Admin CLI, but it is quite difficult.

In order to list the files, enter file list activelog /cuc/diag_CuMbxSync* detail reverse .

In order to view a file, enter file view activelog /cuc/diag_CuMbxSync_xxxxxxxx.uc where xxxxxxxx is the file number.

In order to transfer the files to a Secure FTP (SFTP) server, enter file get activelog /cuc/diag_CuMbxSync* .

Check the latest CuMbxSync logs for any HTTP failures or warnings. Since errors or warnings are written by default in the traces, there is no need to enable traces at this point.

HTTP failures could stop (intermittently or completely) messaging operation synchronization from CUC to the Exchange server and vice versa. If HTTP failures are seen in the logs, then the next step is to troubleshoot and fix these issues.

The Unity Connection Single Inbox Troubleshooting TechNote document provides some information on the various errors seen in the CuMbxSync logs.

If there are no errors / failures in the CuMbxSync log, then enable CsEws and CuMbxSync micro traces - all levels. Choose Cisco Unity Connection Serviceability > Trace > Micro Trace . Click the reset option on the Unified Messaging Account page of the User and collect the logs once again. Contact the Cisco Technical Assistance Center (TAC) for further assistance.

### Delayed Synchronization from Exchange Server to CUC

Exchange communicates to the CUC server on port 7080. This section provides steps in order to troubleshoot the issue.

Admin CLI

Root

In the CUC CLI, enter utils network capture file SIBTrace count 100000 size ALL .

On Exchange, download and run Wireshark .

In the CUC capture, you should see this packet pattern on port 7080 (port used to receive notifications):

Confirm (with the help of the IP address highlighted in the screen capture) that the notification has been sent from the Exchange server to CUC and not to some proxy server. If you do not see the same pattern at port 7080 (or do not see any traffic on port 7080), check with the Exchange server team. Notifications from Exchange to CUC could be of two types:

- Keep-alive notifications

- Message operation notification

Keep-alive messages are sent from Exchange to CUC. Here is a sample keep-alive notification message:

The Exchange server sends this notification every five minutes (by default) for every subscribed user. This notification is sent by Exchange to the Exchange Web Services (EWS) client (CUC in this case) in order to keep subscriptions alive in CUC.

Notifications from the Exchange server are received at the CUC server by Jetty, which parses the notifications and updates data in the tbl_ExSubscription table.

Sample Entries in tbl_ExSubscription :

The same information can be viewed via the Admin CLI. Enter the run cuc dbquery unitydyndb select first 10 * from tbl_exsubscription command.

tbl_ExSubscription stores information about each mailbox subscription registered with Exchange via EWS. timestamputc (highlighted in the previous screenshot) is one of the columns in this table. It contains Date-time in UTC time which indicates the time a notification for this subscription was last received by CUC from the Exchange server.

The CuMbxSync process has a thread that monitors for stale subscriptions every two minutes and does a resubscription for any stale entries. In the sample log, the thread considers a set of subscription entries as stale. This is not an ideal case (if everything is fine and Exchange sends keep-alive notifications in a timely manner). This field is used to detect stale subscriptions by the CuMbxSync process. The condition used to filter out the stale subscriptions is timestamputc < (CurrentTime - 15 minutes) .

Even if there is no change in a subscriber mailbox at the Exchange side, the Exchange Server by default still sends notifications for each and every subscriber (subscriber on Exchange server) at a five minute interval.

Keep-alive notifications that come from Exchange can be seen in 'Connection Jetty' logs. These logs can be collected from RTMT (choose Trace & Log Central > Collect Files > Connection Jetty and proceed) or via Root Access  ( /usr/local/jetty/logs ).

This log shows the response sent by CUC corresponding to keep-alive notifications sent by the Exchange Server. If keep-alive notifications do not arrive at CUC from Exchange then the subscription will be resubscribed after every 16 minutes (approximately) and only then does mailbox synchronization occur.

Potential reasons for such behavior could be one of these:

- Proxy configuration at the Exchange Server

- Network Address Translation (NAT) configuration at CUC

- Firewall configuration between CUC and the Exchange Server, and so on

Involve the network team and Exchange team in order to get the actual reason of this behavior.

If CUC recieves notification from the Exchange server on-time and the update is not reflected in the CUC mailbox, contact the TAC for assistance to troubleshoot the issue.

### Revision History

1.0

02-Apr-2015

Initial Release

### Contributed by Cisco Engineers

Ratnesh Nath and Anirudh Mavilakandy

Cisco TAC Engineers.

### This Document Applies to These Products

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 02-Apr-2015 | Initial Release |