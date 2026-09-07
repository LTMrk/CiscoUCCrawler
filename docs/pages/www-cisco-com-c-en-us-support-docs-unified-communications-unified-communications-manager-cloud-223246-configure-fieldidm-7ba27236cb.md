---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-cloud-223246-configure-fieldidm-7ba27236cb
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-cloud/223246-configure-fieldidmapping-on-broadworks.html
retrieved_at: 2026-09-07T13:02:03.186782+00:00
---

Configure FieldIdMapping on BroadWorks AS

# Configure FieldIdMapping on BroadWorks AS

### Download Options

Updated: July 7, 2025

Document ID: 223246

Contents

## Contents

## Introduction

This document describes the actions to perform to disable Fields from the CDRs (Call Detail Record) created by the BroadWorks Application Server (AS).

## Prerequisites

### Requirements

- Basic AS knowledge

- Basic BW bwcli knowledge

### Components Used

- Cisco BW AS

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

When new features are introduced in the AS, it can be also necessary to introduce new CDR fields, which are used for accounting and billing purposes. This could cause some Mediation Systems to reject the CDRs or to throw errors or alarms, because the new fields cannot be understood or recognised.

The problem can be often seen following the patching (up to Release 24) or upgrade (starting from Release 25) of the BroadWorks (BW) AS, as these are both actions that could introduce new features.

## Solution

The solution for this problem is to disable the fields, so that the AS does not populate the new fields in the CDRs.

To perform this, navigate to AS_CLI/Interface/Accounting/FieldIdMapping and run the get command to show the current field settings (showing a partial output for brevity):

```
AS_CLI> cd /Interface/Accounting/FieldIdMapping AS_CLI/Interface/Accounting/FieldIdMapping> get Internal Id  External Id                                               Description ================================================================================== ... 473          473                               stirShaken.attestationLevel 474          474                                       stirShaken.origUUID 475          475                                      publicNetworkAddress 476          476                                          visitedNetworkId 477          477                          groupCallQueuePut.invocationTime ...
```

You have already identified, from the error on your Mediation System, that the problem is caused by Field 475 publicNetworkAddress.

Run the clear command to disable the field, like in this example:

```
AS_CLI/Interface/Accounting/FieldIdMapping> clear 475 externalId A restart is required for the change to take effect.
```

Run the get again, to review the change:

```
AS_CLI> cd /Interface/Accounting/FieldIdMapping AS_CLI/Interface/Accounting/FieldIdMapping> get Internal Id  External Id                                               Description ================================================================================== ... 473          473                               stirShaken.attestationLevel 474          474                                       stirShaken.origUUID 475                                                   publicNetworkAddress 476          476                                          visitedNetworkId 477          477                          groupCallQueuePut.invocationTime ...
```

Now that the External Id in field 475 is blank, the AS does not populate it in the CDRs.

Note that the field is still present, and the number of fields can grow in the CDR when new features are added. The Mediation System must just discard excess fields or be updated to account for the new fields.

It is also important to note that, as per the warning in the bwcli after running the clear command, the BW processes need to be restarted for the changes to take effect.

In order to do this, from the AS bwcli run this command as bwadmin :

```
bwadmin@AS01$ restartbw
```

The restart of the BW processes must always be performed during a maintenance window.

For further information on BW AS Accounting and CDRs, you can check the Cisco BroadWorksAccounting Call Detail Record Interface Specification .

### Revision History

1.0

07-Jul-2025

Initial Release

### Contributed by Cisco Engineers

Diego Cimarosti

Technical Consulting Engineer

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Jul-2025 | Initial Release |