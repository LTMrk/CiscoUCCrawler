---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-212058-configure-re-e4b9935e99
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/212058-Configure-Real-Time-Monitoring-Tool-to-A.html
retrieved_at: 2026-08-21T13:56:44.969738+00:00
---

Configure Real Time Monitoring Tool to Audit Admin Activity in Cisco Unified Communications Manager

# Configure Real Time Monitoring Tool to Audit Admin Activity in Cisco Unified Communications Manager

### Download Options

Updated: September 13, 2017

Document ID: 212058

Contents

## Contents

## Introduction

This document describes how to configure the Real Time Monitoring Tool (RTMT) to view and audit real time activity in Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM Administration

- CUCM Trace Configuration

- RTMT Navigation

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Unified Communications Manager

- Real Time Monitoring Tool

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, Ensure that you understand the potential impact of any command.

### Background Information

For CUCM the application audit log supports configuration updates for CUCM interfaces such as Communications Manager Administration, Cisco Unified RTMT, Cisco Unified Communications Manager CDR Analysis and Reporting and Cisco Unified Serviceability.

For IM and Presence Service the application audit log supports configuration updates for IM and Presence interfaces such as Cisco Unified Communications Manager IM and Presence Administration, Cisco Unified IM and Presence Real-Time Monitoring Tool and Cisco Unified IM and Presence Serviceability.

For Cisco Unity Connection the application audit log supports configuration updates for Cisco Unity Connection interfaces, Cisco Unity Connection Administration, Cisco Unity Connection Serviceability, Cisco Personal Communications Assistant and clients that use the Connection REST Application Programing Interfaces (APIs).

## Configure

Follow these steps in order to configure audit log capability and view audit trail from RTMT.

Step 1. Enable Audit Log. Navigate to Cisco Unified Serviceability > Tools > Audit Log Configuration and enable these parameters

- Enable Audit Log

- Enable Purging

- Enable Log Rotation

- Detailed Audit Logging (Detailed audit logs provide the same items as regular audit logs, but also include configuration changes. For example, the audit log includes items that were added, updated, and deleted, including the modified values.)

Note : You must enable these services, Network Service Audit Event Service and Network Service Cisco Log Partitions Monitoring

Tip : When log rotation is disabled (unchecked), audit log ignores the Maximum No. of Files setting.

Step 2. Now you can use RTMT to view Audit Logs. Open and log in to Cisco RTMT. Navigate to Sytem > Tools > AuditLog Viewer and select the node from which you would like to monitor activity. Step 3. Select AuditApp Logs and from the selection list and choose the desired .log file. You are presented with a view of events for the selected log file.

Step 4. Select the desired entry twice to view further event details. In this example we have a CLI command audit trail that indicates the command show myself was performed on node, cucm1151pub . Select the icon with double page image to copy the alert details which can be pasted elsewhere.

Tip : Select the checkbox for Auto Refresh to enable dynamic updates to log entries within the AuditLog Viewer.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

- Audit Log Configuration Settings

### Contributed by Cisco Engineers

Joy Pal

Cisco TAC Engineer

Eric Leite

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)