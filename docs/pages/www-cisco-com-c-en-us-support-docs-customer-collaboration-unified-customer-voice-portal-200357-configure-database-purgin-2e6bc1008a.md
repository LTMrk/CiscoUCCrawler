---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-200357-configure-database-purgin-2e6bc1008a
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal/200357-Configure-Database-Purging-schedule-on-C.html
retrieved_at: 2026-08-16T19:23:08.068805+00:00
---

Configure Database Purging schedule on CVP Reporting Server when OAMP Server is unavailable.

# Configure Database Purging schedule on CVP Reporting Server when OAMP Server is unavailable.

Updated: February 12, 2016

Document ID: 200357

Contents

## Contents

## Introduction

This document describes the procedure to schedule Database Purge on CVP (Cisco Unified Customer Voice Portal) Reporting Server when OAMP (Operation Console) Server is unavailable.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software versions:

- Cisco Unified Customer Voice Portal (CVP)

- Operation Console (OAMP)

## Configure

Normal Database Schedule Steps (Solution Reference Network Design)

Step 1. Navigate to Device Management > CVP Reporting Server .

Step 2. Select a Reporting Server by either clicking in the link with its name field or on the radio button preceding it and then click Edit .

Step 3. At the Edit Reporting Server Configuration window, select the Database Administration menu in the toolbar, then select Data Delete .

Step 4. On the Reporting Server- Data Delete page and change the data retention time for each category of data.

Step 5. Select the hours and minutes in order to execute purge each day. This defines the time for the primary (Nightly) purge and sets the Midday purge to run 12 hours later.

Step 6. Fill in your Informix Password and click Save & Deploy .

Change the CVP Reporting Server Database Purging time without OAMP console

Step 1. Reporting server installation creates a window batch file CVPPURGE.BAT located in C:\Cisco\CVP\bin directory.  This batch file simply runs a Java backend code in order to start the Database purging process, which is also scheduled to run through the window scheduler on each individual CVP Reporting Server.

Step 2. Now the Reporting Server gives two window schedule tasks, CVPDBMidDayPurge and CVPDBNightlyPurge. Each task corresponds to the Midday purge and Nightly purge activity respectively, as mentioned in the Step 5 of the Normal Database Schedule Steps.

Step 3. Both purges use the same CVPPURGE.BAT file, however, different parameters are fed into the batch file for different purge activities. Moreover, the database purging time can be changed through window scheduler tasks on a individual Reporting Server.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

## There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

11-Feb-2016

Initial Release

### Contributed by Cisco Engineers

Tian Lei Xia

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Customer Voice Portal

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 11-Feb-2016 | Initial Release |