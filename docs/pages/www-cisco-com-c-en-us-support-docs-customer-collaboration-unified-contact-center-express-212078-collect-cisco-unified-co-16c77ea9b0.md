---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-212078-collect-cisco-unified-co-16c77ea9b0
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/212078-Collect-Cisco-Unified-Contact-Center-Exp.html
retrieved_at: 2026-08-16T15:07:14.636303+00:00
---

Use CLI to Collect Unified Contact Center Express Logs

# Use CLI to Collect Unified Contact Center Express Logs

### Download Options

Updated: July 14, 2022

Document ID: 212078

Contents

## Contents

## Introduction

This document describes the procedure to find, view, and download logs from a Unified Contact Center Express (UCCX) by use of the Command Line Interface (CLI).

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Find/View/Download Logs from the UCCX

The commands to find, view and download UCCX logs from the CLI via Secure Shell (SSH) are shown here:

### Find logs

Syntax:

file list {activelog | inactivelog | install | partBsalog | salog | tftp} file-spec [options]

file-spec: mandatory file to view options: optional - page|detail|reverse|[date|size]

- page —Displays the output one screen at a time.

- detail —Long listing with date and time

- reverse —Reverse sort direction

- date —Sort by date

- size —Sort by file size

Example:

```
admin:file list activelog / detail 15 Sep,2016 09:07:48 <dir> audit 15 Sep,2016 09:07:48 <dir> ccm_db 15 Sep,2016 09:07:48 <dir> cm 15 Sep,2016 09:07:48 <dir> core 15 Sep,2016 09:07:48 <dir> cuic 15 Sep,2016 09:07:48 <dir> desktop 15 Sep,2016 09:07:48 <dir> dp_db 15 Sep,2016 09:07:48 <dir> mgetty 15 Sep,2016 09:07:48 <dir> patches 15 Sep,2016 09:07:48 <dir> platform 15 Sep,2016 09:07:48 <dir> sa 15 Sep,2016 09:07:48 <dir> sso 15 Sep,2016 09:07:48 <dir> syslog 15 Sep,2016 09:07:48 <dir> tomcat 15 Sep,2016 09:07:48 <dir> uccx
```

### View logs

Syntax:

file view {activelog|inactivelog|install} file-spec

file-spec   mandatory   file to view

the file-spec must resolve to a single file

### Download logs

Syntax:

file get {activelog|inactivelog|install} file-spec [options]

file-spec   mandatory   file to transfer

options     optional    reltime months|weeks|days|hours|minutes timevalue

abstime hh:mm:MM/DD/YY hh:mm:MM/DD/YY

match regex

recurs

compress

- reltime —Relative time period, specified as minutes | hours | days | weeks | months value

- abstime —Absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY

- match —Match a particular string in the filename, specified as string value

- recurs —Get all files, includes subdirectories

- compress option allows you to download the files in a zipped format.

Note : In order to download the files, ensure that external Secure File Transfer Protocol (SFTP) server is configured and accessible.

Tip : The recurs option allows you to traverse the directory for all subdirectories and files. This is used if you want to pull all logs from a directory.

## View Realtime Logs

You can use the command : show open files regexp <logfile-expression-to-match> to get the currently written log(s) in realtime on the CLI. This method is useful to troubleshoot live - you can view the currently written log in memory, and then accordingly tail, view or get (download) that file from the CLI for investigation.

The command can match a regular expression that matches any log file name which allows you to troubleshoot issues in realtime (that can be reproduced live).

Examples :

1. Troubleshoot an error on the Appadmin to get or view the current log while you reproduce the problem in realtime

show open files regexp MADM

Copy the path of that current file from the current directory /uccx/log/MADM/<file.log>

```
admin:show open files regexp MADM Executing.. please wait. tomcat 29349 tomcat 729w REG 8,6 1905330 5640852 /common/log/taos-log-b /uccx/log/MADM/Cisco001MADM076.log admin:file view activelog /uccx/log/MADM/Cisco001MADM076.log admin:file get activelog /uccx/log/MADM/Cisco001MADM076.log
```

```
admin:file tail activelog /uccx/log/MADM/Cisco001MADM076.log
```

2. Troubleshoot an issue with Call failure on the Engine due to a step in the script while you reproduce the problem in realtime

show open files regexp MIVR

Copy the path of that current file from the current directory /uccx/log/MIVR/<file.log>

3. Troubleshoot an issue with Finesse or CUIC while you reproduce the problem in realtime

Finesse - show open files regexp Desktop-webservices

CUIC - show open files regexp CCBU-cuic

## Examples

Here are a few examples of how these commands are used:

- In order to view just the Finesse tomcat logs: file view activelog /desktop/finesse/logs/catalina.out

- In order download the Finesse tomcat logs: file get activelog /desktop/finesse/logs/catalina.out

- In order download ALL Finesse logs: file get activelog /desktop recurs compress

- In order to view  the system-history logs to find out the last reboot: file view install /system-history.log

Note : you do not need the '/'. Alternatively: file view install system-history.log works as well

- In order to troubleshoot NTP issues: file view activelog /syslog/sd_ntp.log

- In order to download the Voice Operating System (VOS) platform database replication logs (includes sysmaster, sysutils, sysuser, sysadmin, syscdr, db_phx_config, cuic_data, ccm_X_Y_Z_aaaaa_bb): file get activelog /cm/log/informix/ccm.log

- In order to download the UCCX Engine (MIVR) logs: file get activelog /uccx/log/MIVR recurs compress

- In order to download all of the logs from the active partition (except the install logs): file get activelog / recurs compress

- In order to collect a packet capture that you took on UCCX where the name of the capture is UCCxPackets: file get activelog /platform/cli/UCCxPackets.cap

- In order to view all of the service manager logs, you use a wildcard to filter only the servm logs: file list activelog /platform/log/servm*.log

## Related Information

- Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

### Revision History

2.0

14-Jul-2022

Fixed broken hyperlink in the "Related Information" section. Updated title. Edited for clarity.

1.0

14-Sep-2017

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 14-Jul-2022 | Fixed broken hyperlink in the "Related Information" section. Updated title. Edited for clarity. |
| 1.0 | 14-Sep-2017 | Initial Release |