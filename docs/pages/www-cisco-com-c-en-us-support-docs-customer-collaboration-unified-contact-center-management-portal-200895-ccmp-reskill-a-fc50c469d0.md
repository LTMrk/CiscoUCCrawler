---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-management-portal-200895-ccmp-reskill-a-fc50c469d0
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-management-portal/200895-CCMP-Reskill-attempt-generates-error-Gl.html
retrieved_at: 2026-08-21T12:08:15.767621+00:00
---

CCMP Reskill attempt generates error "Global Operation request failed: SEC_Provision_Route"

# CCMP Reskill attempt generates error "Global Operation request failed: SEC_Provision_Route"

### Download Options

Updated: October 26, 2016

Document ID: 200895

Contents

## Contents

## Introduction

This document outlines the issue where Cisco Unified Contact Center Management Portal (CCMP) supervisor users are unable to perform reskill transactions.

## Prerequisites

Understand Administration of CCMP

### Requirements

There are no specific requirements for this document.

## Problem

After upgrade of CCMP from 8.5 to 10.5. Agent reskill by supervisor using skill group tab in CCMP will fail with the following error…

The research of error points to the following CDETS and workaround.

CSCup34703 - Upgrading CCMP from 8.5(4) to 9.1(1) stops users from reskilling

```
Symptom:
Error message seen when adding or removing the Agents from a SG. Error attached to the defect.

Conditions:
This is because there is a new link between the route and skillgroup which is now imported, used by the system to add functionality and enforced by security i.e. the user must have rights to browse routes that are linked to skill groups. This essentially means that they should be stored in the same folder as the skillgroup to ensure security is ok.

Error messages in the logs:
Specific Error:
2014-06-05 04:56:55,692 DEBUG 4224 Application.DataCommand Exception: LoadEntitiesCommand Exception: Exony.Security.ExonySecurityException
Message: Request for operation permission failed - Demand: Operation: SEC_LIST_DIMENSIONS, Path: /tenant1
Source: Exony
at Exony.Security.ExonyOperationPermission.Demand() in t:\Dev\Source\Reporting\D9_2_1\App\Exony\Security\ExonyOperationPermission.cs:line 132
at System.Security.PermissionSet.DemandNonCAS()
at Exony.Reporting.Application.Provisioning.LoadEntitiesCommand.ExecuteCommand() in t:\Dev\Source\Reporting\D9_2_1\App\Exony.Reporting.Application.Provisioning\LoadEntitiesCommand.cs:line 41
at Exony.Reporting.Application.DataCommand.ExecuteMethodWithRetries(DatabaseMethod method, Boolean allowTransaction, Exception& exception) in t:\Dev\Source\Reporting\D9_2_1\App\Exony.Reporting.Application\DataCommand.cs:line 860

Workaround:
We can run the following script on both DB servers to move the routes to the skillgroup folder
update r 
set r.FOLDER_ID = s.FOLDER_ID 
from VW_DIM_ROUTE_SKILLGROUP_MEMBER as rsm 
inner join TB_DIM_SKILLGROUP as s 
on rsm.PARENT_ITEM_BIZ_URN = s.ITEM_BIZ_URN 
inner join TB_DIM_ROUTE as r 
on rsm.CHILD_ITEM_BIZ_URN = r.ITEM_BIZ_URN
restart the app server
```

The workaround was applied but the following error persisted.

At this point, CCMP is working properly otherwise.

- Provisioning transactions succeed.

- From agent tab, reskill works.

- From skill group tab, reskill fails with error above when using supervisor credentials

- From skill group tab, reskill succeeds when using admin credentials

The error message still point to CSCup34703 , except there is no specific expected error message in the log.

2014-06-05 04:56:55,692 DEBUG 4224 Application.DataCommand Exception: LoadEntitiesCommand Exception: Exony.Security.ExonySecurityException Message: Request for operation permission failed - Demand: Operation: SEC_LIST_DIMENSIONS, Path: /tenant1 Source: Exony at Exony.Security.ExonyOperationPermission.Demand() in t:\Dev\Source\Reporting\D9_2_1\App\Exony\Security\ExonyOperationPermission.cs:line 132 at System.Security.PermissionSet.DemandNonCAS() at Exony.Reporting.Application.Provisioning.LoadEntitiesCommand.ExecuteCommand() in t:\Dev\Source\Reporting\D9_2_1\App\Exony.Reporting.Application.Provisioning\LoadEntitiesCommand.cs:line 41 at Exony.Reporting.Application.DataCommand.ExecuteMethodWithRetries(DatabaseMethod method, Boolean allowTransaction, Exception& exception) in t:\Dev\Source\Reporting\D9_2_1\App\Exony.Reporting.Application\DataCommand.cs:line 860

## Solution

The issue was specific to the Global Roles which must have been reset during the Database (DB) upgrade.  it is required to enable the "Provision Routes" at the Global Role level since Routes can have memberships to Skills which then allowed the user to reskill etc. without getting the error.

### Revision History

1.0

17-Dec-2016

Initial Release

### Contributed by Cisco Engineers

Jason Pare

### This Document Applies to These Products

- Unified Contact Center Management Portal

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Dec-2016 | Initial Release |