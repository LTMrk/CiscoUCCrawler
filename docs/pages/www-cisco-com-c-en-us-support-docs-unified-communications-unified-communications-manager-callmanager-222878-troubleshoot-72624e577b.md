---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-222878-troubleshoot-72624e577b
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/222878-troubleshoot-issues-when-tftp-reaches-ma.html
retrieved_at: 2026-08-16T18:00:26.028454+00:00
---

Troubleshoot Issues When TFTP Reaches Maximum Serving Count

# Troubleshoot Issues When TFTP Reaches Maximum Serving Count

### Download Options

Updated: March 21, 2025

Document ID: 222878

Contents

## Contents

## Introduction

This document describes TFTP stopping the serving of configuration files, preventing devices from receiving the required files during registration.

## Overview

Maximum Serving Count specifies the maximum number of client requests in order to accept and serve files at a time. S uggested values for a dedicated TFTP server: 1500 for a single-processor system and 3000 for a dual-processor system. For higher CPU configurations, the serving count can be up to 3500.

## Problem

A connection object is created whenever there is a file requested on TFTP. There are five active connection objects (design changed in 11.5). At a time, five requests can be served by TFTP, and the subsequent requests are put on the processing queue. Once one of the connection object goes free. it takes care of the 6th request, and so on. If all the connection objects are exhausted (that is, no connection object is released), pending requests will continue to pile up. Once the count reaches 3000 (or the maximum serving count set under the service parameters), TFTP responds with a 503 error, as indicated in the TFTP debug logs. Ideally this is supposed to clear within seconds or minutes. If not, raise a case with TAC.

When there is an invalid file request like static file not present or the file size = 0, the connection objects are not be released.

## Solution

Restart TFTP service on the affected node.

## Logs Required

- Cisco CallManager (CUCM) [debug/detailed]

- TFTP [debug/detailed]

- Event Viewer Sys/App

## Log Analysis

TFTP logs:

```
### static file request and response ### 01975217.004 |19:33:58.685 |AppInfo | ServeFile::validateFileName File Requested <file_name> . 01975217.008 |19:33:58.685 |AppInfo | ServeFile::CheckFileIsStatic <file_name> is (Static) File 01975218.024 |19:33:58.686 |AppInfo | ServeStaticFile::FindAndServe File to be searched onDisk is [ <file_name> ], onDisk = 0 01975218.026 |19:33:58.686 |AppInfo | ServeStaticFile:: processFileRequest File Not Found - 404 - Failure 01975220.002 |19:33:58.686 |AppInfo | HTTPConnection::wait_FileResponse Requested file NOT FOUND or File Contents EMPTY ... Sending error response ### Max serving count reached ### 00002296.000 |20:56:50.807 |AppInfo | TID[b44f0b70] TFTPEngine::getRequest0xb384bde0, server socket(8) INFO:: File Requested SEPXXXXXXXXXXXX.cnf.xml 00002299.000 |20:56:50.807 |AppInfo |TFTPEngine::isReadRequest[0xb384bde0 Y.Y.Y.Y~59499], [SEPXXXXXXXXXXXX.cnf.xml] opcode(1), Mode(octet), Serving Count(3000)* 00002300.000 |20:56:50.807 |AppInfo | TID[b44f0b70] TFTPServer::****recvMessage0x8954318 sockets:8 count(03000)**** , connect(0xb384bde0), nbytes(32) 00002301.000 |20:56:50.807 |AppInfo | TID[b44f0b70] TFTPServer::recvMessage0x8954318 sockets:8 Reached max count, returning 503
```

## FAQs

What are static files?

Static files are all load files that you can find under /usr/local/cm/tftp and Dynamic TFTP files are all configuration file like SEP<mac id>.cnf.xml .

Is there a way to monitor serving count?

Apart from TFTP logs (debug) there is no other way to monitor the serving count (like Performance counter and so on).

Where can I change the serving count?

Maximum serving count value can be checked/changed from CUCM GUI: System > Service Parameters > Service = Cisco TFTP.

### Revision History

1.0

21-Mar-2025

Initial Release

### Contributed by Cisco Engineers

Sourajit Hazra

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Mar-2025 | Initial Release |