---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-200957-how-to-collect-logs-for-uc-applications-html-1ea7545cdd
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/200957-How-to-Collect-Logs-for-UC-Applications.html
retrieved_at: 2026-08-16T22:56:22.717626+00:00
---

Collect Logs for UC Applications

# Collect Logs for UC Applications

### Download Options

Updated: May 10, 2024

Document ID: 200957

Contents

## Contents

## Introduction

This document describes how to collect logs for the Cisco Unified Communication (UC) Applications.

## UC Applications Log Collection How to Guide

UC Applications that are covered here are Cisco Jabber clients, Cisco Unified Communication Integration for Microsoft Lync (CUCI-Lync), Cisco Unified Attendant Console (CUAC)-Standard, CUAC-Advanced, Cisco Instant Messaging & Presence (IM&P), and Cisco Internet Protocol Communicator (CIPC).

Note : CIPC is now End of Service (EOS).

For each scenario, provide details about the problem and note the time the problem occurred, the calling number.

### Jabber for Windows

Step 1 .  Navigate to Help > Report a Problem to create a problem report.

Step 2 .  Choose the option that denotes the problem.

Step 3 .  Under options, describe the problem and generate the report.

Step 4 .  This places a ZIP file on the user desktop.

```
Default Jabber log location %userprofile%\AppData\Local\Cisco\Unified Communications\Jabber\CSF\Logs
```

### Jabber for MAC

Step 1 .  Navigate to Help > Report a Problem to create a problem report.

Step 2 .  Choose the option that denotes the problem.

Step 3 .  Under options, describe the problem and generate the report.

Step 4 .  This places a ZIP file on the user desktop.

```
Default Jabber log location /Users/<userid>/Library/Logs/Jabber/
```

### Jabber for iPhone, iPad, and Android

Step 1 .  Navigate to Menu > Settings > Problem Reporting .

Step 2 .  Enable Detailed Logging .

Step 3 .  Exit Jabber and relaunch.

Step 4 .  When the problem occurs, navigate to Menu > Settings > Problem Reporting .

Step 5 .  Click Send Problem Report and email the problem report.

Tip : You can use these Cisco Video links: How to Clear the Cache Create a Jabber Problem Report Collect logs for Phone Issues Collect Logs from Expressway (When Jabber is over MRA)

### CUCI-Lync

Step 1 .  Navigate to Help > Report a Problem to create a problem report.

Step 2 .  Choose the option that denotes the problem.

Step 3 .  Under options, describe the problem and generate the report.

Step 4 .  This places a ZIP file on the user desktop.

```
Default CUCI-Lync log location %userprofile%\AppData\Local\Cisco\Unified Communications\Jabber\CSF\Logs
```

### VXME for Windows

Step 1 .  Navigate to Help > Report a Problem to create a problem report.

Step 2 .  Choose the option that denotes the problem.

Step 3 .  Under options, describe the problem and generate the report.

Step 4 .  This places a ZIP file on the user desktop.

```
Default VXME log locations VXME Client Log location: %userprofile%\AppData\Local\Cisco\VXME\ VXME Agent Log Location: %userprofile%\Local\Cisco\Unified Communications\Jabber\CSF\Logs\Virtualisation\
```

### Cisco IM and Presence

#### Set Logging Levels to Debug

Step 1 . Log in to Cisco Unified Serviceability for the IM&P server.

Step 2 .  Navigate to Trace > Configuration.

Step 3 .  Select the IM&P server from the drop-down.

Step 4 .  Select the Service Group from the drop-down.

Step 5 .  Select the Service .

Step 6 .  Click Trace On box.

Step 7 .  Select Debug level trace.

Step 8 .  Click Save button.

#### Collect Logs with Real-Time Monitoring Tool (RTMT)

Download RTMT and collect logs, for more information on how to download and collect files refer to IM and Presence Server RTMT Log Collection Configuration Example .

Tip : You can use these Cisco Video links: Configuring Service Trace Levels Collect logs from the RTMT Obtain a Packet Capture from the IM&P

### Cisco IP Communicator

Step 1 .  Right-click anywhere on CIPC,navigate to Preferences > User tab . Check Enable Logging.

Step 2. Restart Cisco IP Communicator to place the application in a known state.

Step 3. On the Windows desktop, navigate to Start > All Programs > Cisco IP Communicator > Create CIPC Problem Report

### CUAC Standard

#### CUAC Standard Client

Step 1. Navigate to Options > Logging > Collect Logs. Save to the desktop.

#### Cisco TSP

Collect all the files in this directory.

```
C:\Temp\CiscoTSP001Log
```

### CUAC Advanced

Attendant Server Serv ice Logs:

Step 1 .  Log in to the CUAC-Advanced web page.

Step 2 .  Navigate to Engineering > Logging Management.

Step 3 .  Select all checkboxes on Cisco Unified Attendant Server section.

Step 4 .  Collect logs.

```
Default file locations for CUAC-A 10.x and Earlier 32 Bit CUAC-A Server - C:\Program Files\Cisco\Logging\SRV
64 Bit CUAC-A Server - C:\Program Files (x86)\Cisco\Logging\SRV Default file locations for CUAC-A 11.X and Later %ALLUSERSPROFILE%\Cisco\CUACA\Server\Logging\SVR
```

LDAP Plug-in Logs:

Step 1 .  Log in to the CUAC-Advanced web page.

Step 2 .  Navigate to Engineering > Logging Management .

Step 3 .  Select all checkboxes on LDAP Plug-in section.

Step 4 .  Collect logs.

```
Default file locations for CUAC-A 10.x and earlier 32 Bit CUAC-A Server - C:\Program Files\Cisco\Logging\LDAP
64 Bit CUAC-A Server - C:\Program Files (x86)\Cisco\Logging\LDAP Default file location for CUAC-A 11.X and later %ALLUSERSPROFILE%\Cisco\CUACA\Server\Logging\LDAP\
```

CUPS Plug-in Logs

Step 1 .  Log in to the CUAC-Advanced web page.

Step 2 .  Navigate to Engineering > Logging Management.

Step 3 .  Select all checkboxes on CUPS Plug-in Logs section.

Step 4 .  Collect logs.

```
Default file locations for CUAC-A 10.x and earlier 32 Bit CUAC-A Server - C:\Program Files\Cisco\Logging\CUPS
64 Bit CUAC-A Server - C:\Program Files (x86)\Cisco\Logging\CUPS Default file location for CUAC-A 11.x and later %ALLUSERSPROFILE%\Cisco\CUACA\Server\Logging\CUPS\
```

BLF Plug-in Logs:

Step 1 .  Log in to the CUAC-Advanced web page.

Step 2 .  Navigate to Engineering > Logging Management .

Step 3 .  Select all checkboxes on BLF Plug-in Logs section.

Step 4 .  Collect logs.

```
Default file locations for CUAC-A 10.x and earlier 32 Bit CUAC-A Server - C:\Program Files\Cisco\Logging\CTIS
64 Bit CUAC-A Server - C:\Program Files (x86)\Cisco\Logging\CTIS Default file location for CUAC-A 11.x and later %ALLUSERSPROFILE%\Cisco\CUACA\Server\Logging\CTI\
```

Cisco TSP

Collect all the files in this directory.

```
C:\Temp\CiscoTSP001Log
```

CUAC Advanced Client (version 11.X and later)

Step 1. Launch and log in (if unable to log in, proceed to Step 4) to the CUAC-Advanced operator client.

Step 2. Navigate to Options > Preferences > Logging .

Step 3. Place a check into the Database and Server Communication checkboxes.  Select Apply .

Step 4. Reproduce the problem.

Step 5. Navigate to Help > Collect Logs .

Step 6. Enter the location where the log files must be saved.

Step 7. Select Start .

### Revision History

4.0

10-May-2024

Updated Title, TOC, Introduction, SEO, Style Requirements, Machine Translation, Gerunds, Grammar and Formatting.
Added Note that CIPC is EOS.

2.0

17-Mar-2022

New Links Added

1.0

07-Feb-2017

Initial Release

### Contributed by Cisco Engineers

Josh Hammonds

Cisco TAC Engineer

Joseph Hardy

Cisco TAC Engineer

Joel Burleigh

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber

- Jabber for Windows

| Revision | Publish Date | Comments |
|---|---|---|
| 4.0 | 10-May-2024 | Updated Title, TOC, Introduction, SEO, Style Requirements, Machine Translation, Gerunds, Grammar and Formatting.
Added Note that CIPC is EOS. |
| 2.0 | 17-Mar-2022 | New Links Added |
| 1.0 | 07-Feb-2017 | Initial Release |