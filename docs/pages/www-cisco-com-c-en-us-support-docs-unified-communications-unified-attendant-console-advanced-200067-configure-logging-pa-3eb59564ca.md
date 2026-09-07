---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-advanced-200067-configure-logging-pa-3eb59564ca
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-advanced/200067-Configure-Logging-Path-for-CUAC-Advanced.html
retrieved_at: 2026-09-07T15:48:33.890106+00:00
---

Configure Logging Path for CUAC Advanced Server

# Configure Logging Path for CUAC Advanced Server

### Download Options

Updated: August 25, 2015

Document ID: 200067

Contents

## Contents

## Introduction

This document describes the procedure to change the log location of Cisco Unified Attendant Console Advanced (CUAC) server when the default drive is full. The logs are stored in C:\Program Files (x86)\Cisco\Logging.

## Prerequisites

### Requirements

Cisco recommends that you have basic knowledge of these topics:

- CUAC Server

- Microsoft Windows 2008 Server

### Components used

The information in this document is based on these software and hardware versions:

- CUAC 10.x

- Microsoft Windows 2008 Server

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## How to Change the Logging Location

### SRV Logging (ICD.log)

1. Navigate to the registry path.

Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Arc Solutions\Call Connect\Server\Runtime Logging

2. Double-click the Logging File Name registry key and edit the location.

### Web Admin Logging

1. Navigate to the specified location in Registry Editor.

Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Arc Solutions\Call Connect\Web Admin\Runtime Logging

2. Double-click the Logging File name registry key and update the required location.

### LDAP Logging (ldaptrace/ldapwarning.log)

1. Navigate to the specified location in Registry Editor.

Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Arc Solutions\Call Connect\LDAP Synchronize Server\Runtime Logging

2. Double-click the Logging File Name registry key and update the required location.

### CUPS Logging (cupsplugin.log)

This log cannot be edited from the registry settings. To change the logging location, navigate to the following location: C:\Program Files (x86)\Cisco\CUPS

1. Open the Cisco Presence Server Plug-in.exe file. This is an XML file as shown in this image.

2.  Edit the location inside the XML file to the new location and save the file.

### CTI Server (ctiserverlog)

This log cannot be edited from the registry settings. To change the logging location, navigate to the following location: C:\Program Files (x86)\Cisco\CUPS

1. Open the CTI Server.exe file. This is an XML file as shown in this image.

2. Edit the location inside the XML file to the new location and save the file.

## Verify

The log location is changed from the default to the new location as described in this document.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

Contributed by Cisco Engineers

### Contributed by Cisco Engineers