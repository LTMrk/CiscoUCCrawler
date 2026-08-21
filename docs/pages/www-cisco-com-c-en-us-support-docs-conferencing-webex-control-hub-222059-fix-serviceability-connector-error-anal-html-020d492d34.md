---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-222059-fix-serviceability-connector-error-anal-html-020d492d34
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/222059-fix-serviceability-connector-error-anal.html
retrieved_at: 2026-08-21T06:32:39.541755+00:00
---

Fix Serviceability Connector Error "Analysis Cannot Be Completed"

# Fix Serviceability Connector Error "Analysis Cannot Be Completed"

### Download Options

Updated: June 13, 2024

Document ID: 222059

Contents

## Contents

## Introduction

This document describes how to fix Serviceability Connector error: "Analysis can not be completed" in CCUC.

## Problem: "Analysis Can Not Be Completed" When Analyzing Call Logs (CCUC)

After the call logs have been collected and you click View Analysis in Cloud Connected Unified Connector (CCUC), the call analysis window appears and shows an error after analyzing the call logs: "Analysis can not be completed. The specificed call could not be located within the logs. There is no match for SDL files or lines containing the provided call identifier." Error Message in Control Hub Connected UC

The error means that logs were overwritten and are no longer available.

## Solution: Increase The Number of Signal Distribution Layer (SDL) Trace Files

The solution is to increase the number of Cisco Unified Call Manager (CUCM) SDL trace files to increase the time window coverage of the logs.

To increase the number of SDL files, complete these steps:

1. Log in to CUCM Administration and under Navigation , select Cisco Unified Serviceability . 2. Click Trace > Configuration > Service Group: CM Services > Service: Cisco CallManager . CUCM Trace Configuration 3. Click Related Links: SDL Configuration .

SDL Configuration

4. Scroll down to Trace Output Settings > Maximum No. of Files .

Trace Output Settings 5. Increase the number of files. 6. Click Save .

### How To Calculate Current Log Time Frame Captured

On the call processing nodes, capture the output of the CLI command: file list activelog cm/trace/ccm/sdl date detail . The difference between the time stamp of the first and last file tells you the time frame for which logs are available and calls can be analyzed.

### How To Calculate Maximum Number of Log Files Based on Available Diskspace (Logging Partition)

Take the output of the CLI command on each call processing node: show status . You can check how much more free space there is for Disk/logging .

Based on this, you can calculate how many more files can be written to the logging partition.

## Related Information

- Deployment guide for Serviceability Connector

### Revision History

1.0

14-Jun-2024

Initial Release

### Contributed by Cisco Engineers

Mariana Castaneda

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Control Hub

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 14-Jun-2024 | Initial Release |