---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-advanced-217593-troubleshoot-no-repl-6d30296d22
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-advanced/217593-troubleshoot-no-replication-records-fou.html
retrieved_at: 2026-09-07T15:49:07.275559+00:00
---

Troubleshoot "No Replication Records Found" in CUAC Advanced Replication Report

# Troubleshoot "No Replication Records Found" in CUAC Advanced Replication Report

### Download Options

Updated: December 7, 2021

Document ID: 217593

Contents

## Contents

## Introduction

This document describes what actions to take to fix the "No replication records found" error in Cisco Attendant Console Advanced Replication Report.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Attendant Console Advanced

- Microsoft Windows (Server)

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

When you select the Replication report within the CUAC Advanced Administration GUI > Cisco Unified Replication > CUAC Publisher > ATTCFG or ATTLOG , you can see the error on the webpage: No replication records found , as in the image.

## Solution

The report is written to C:\ProgramData\Cisco\CUACA\Server - DBC_XML_File.xml . By default, the creator and administrators have full permissions to the repository and the users have all but full control designations.

You would need to verify that the Server folder and its files have the permissions mentioned before. If so, change the DBC_XML_File.xml filename to DBC_XML_File_OLD.xml , then click Reinitialize Replication on the CUAC Advanced Server. A new file with the same name must be created and the Replication report might not be empty anymore.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

14-Dec-2021

Initial Release

### Contributed by Cisco Engineers

Luis Miranda

Cisco TAC

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 14-Dec-2021 | Initial Release |