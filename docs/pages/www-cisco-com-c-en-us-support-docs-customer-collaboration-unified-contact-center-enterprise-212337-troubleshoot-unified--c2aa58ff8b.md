---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-enterprise-212337-troubleshoot-unified--c2aa58ff8b
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-enterprise/212337-troubleshoot-unified-contact-center-ente.html
retrieved_at: 2026-08-16T19:21:46.080668+00:00
---

Unified Contact Center Enterprise Diagnostic Portico Does Not List the Processes or Services

# Unified Contact Center Enterprise Diagnostic Portico Does Not List the Processes or Services

### Download Options

Updated: February 11, 2021

Document ID: 212337

Contents

## Contents

## Introduction

This article describes how to fix an issue with Unified Contact Center Enterprise (UCCE) Diagnostic Framework Portico that does not list the processes or services.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- UCCE

- Diagnostic Framework Portico

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

When you open Diagnostic Framework Portico you are not able to list the services or processes.

When you try to list the services you get:

```
ListServicesReply (Error) No ICM service found.
```

When you try to list the processes nothing is listed.

From the system CLI, the show process command gives a warning:

```
admin: show processes Warning: org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser: Property 'http://www.oracle.com/xml/jaxp/properties/entityExpansionLimit' is not recognized.

Warning: org.apache.xerces.parsers.SAXParser: Feature 'http://javax.xml.XMLConstants/feature/secure-processing' is not recognized.

Warning: org.apache.xerces.parsers.SAXParser: Property 'http://www.oracle.com/xml/jaxp/properties/entityExpansionLimit' is not recognized.
```

If you access the URL https://localhost:7890/icm-dp/rest/DiagnosticPortal/ , it does not work:

```
<?xml version="1.0" encoding="utf-8" ?>
- <dp:ListProcessesReply ReturnCode="0" xmlns:dp=" http://www.cisco.com/vtg/diagnosticportal"<http://www.cisco.com/vtg/diagnosticportal%22>>;
  <dp:Schema Version="1.0" />
  </dp:ListProcessesReply>
```

## Solution

This happens due to a Windows Management Instrumentation (WMI) failure.

From the Diagnostic Framework logs you can see an exception from WMI services when the service status is retrieved:

```
148048: LCDSA4104: Aug 17 2017 05:42:58.126 -04:00: %ListServices-INFO-[3132736] Request received.
148049: LCDSA4104: Aug 17 2017 05:42:58.126 -04:00: %ListServices-INFO-[3132736] Creating reply: 
148050: LCDSA4104: Aug 17 2017 05:42:58.126 -04:00: %ListServices-DEBUG-[3132736] Retrieving ICM Services Installed on the System
148051: LCDSA4104: Aug 17 2017 05:42:58.131 -04:00: %ListServices-ERROR-[3132736] Exception while getting the service: Not found 
148052: LCDSA4104: Aug 17 2017 05:42:58.136 -04:00: %ListServices-DEBUG-[3132736] The Exception trace is : at System.Management.ManagementException.ThrowWithExtendedInfo(ManagementStatus errorCode)
   at System.Management.ManagementScope.InitializeGuts(Object o)
   at System.Management.ManagementScope.Initialize()
   at System.Management.ManagementObject.Initialize(Boolean getObject)
   at System.Management.ManagementObject.Get()
   at Cisco.ICM.Serviceability.Diagnostics.DFSvcMgr.ListServices(String sInstance)
```

In order to fix the issue, recreate the WMI repositories. See Rebuilding the WMI Repository .

### Contributed by Cisco Engineers

Maria Jose Mendez Vazquez

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Contact Center Enterprise