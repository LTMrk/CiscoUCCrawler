---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-212049-troubleshoot-context-ser-a9ea4a0d06
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/212049-Troubleshoot-Context-Service-Gadget-not.html
retrieved_at: 2026-08-16T15:07:01.465585+00:00
---

Troubleshoot Context Service Gadget not showing a Register button

# Troubleshoot Context Service Gadget not showing a Register button

Updated: September 13, 2017

Document ID: 212049

Contents

## Contents

## Introduction

This document describes how to troubleshoot a Unified Contact Center Express (UCCX) integrated with Context Service (CS) where the CS does not show a register button available for context service

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- UCCX

- Cisco CS

### Components Used

The information in this document is based on these software versions:

- UCCX 11.5

- Cisco CS

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem

When you Log in to the Context Service Management page in Finesse Administration, there can be an error message

```
Unable to determine the registration status of the system. Please refresh the page to try again.
```

Step 1. Refresh the page

Step 2. Sign out from Finesse admin page and log back in

Step 3. If the above steps do not resolve the issue, pull fusion-mgmt-connector log from Cisco Unified Real-Time Monitoring Tool (RTMT)

Log may show the following confirming this issue

```
com.cisco.user.CapabilityNotFoundException: Capability does not exist for user: USER, capability class: class com.cisco.user.AdministratorCapability
    at com.cisco.user.impl.CCMUserStubImpl.getCapability(CCMUserStubImpl.java:877)
    at com.cisco.user.User.getCapability(User.java:579)
    at com.cisco.uccx.UccxRealm.hasCapability(UccxRealm.java:137)
    at com.cisco.uccx.UccxRealm.checkAppAdminCapability(UccxRealm.java:260)
```

## Solution

You must log in Finesse admin page with the Appadmin user. Register button is not enabled for any user other than the Appadmin user.

### Revision History

1.0

13-Sep-2017

Initial Release

### Contributed by Cisco Engineers

Raghu Krishnan

Cisco Engineer

Edited by Ishan Sambhi and ChandraMouli Vaithiyanathan

Cisco TAC Engineers

### This Document Applies to These Products

- Unified Contact Center Express

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 13-Sep-2017 | Initial Release |