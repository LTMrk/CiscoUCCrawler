---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-212381-troubleshoot-collections-no-09495bcfd2
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/212381-troubleshoot-collections-none-available.html
retrieved_at: 2026-08-16T19:25:38.399650+00:00
---

Troubleshoot Collections "None Available" Displayed for Non-Default Administrator in CUIC Server

# Troubleshoot Collections "None Available" Displayed for Non-Default Administrator in CUIC Server

Updated: October 23, 2017

Document ID: 212381

Contents

## Contents

## Introduction

This document describes how to troubleshoot the problem in Cisco Unified Intelligence Center (CUIC) server when user cannot see collections in the report filter.

## Prerequisites

### Components Used

The information in this document is based on CUIC version 11.5.1.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

Under User Permissions -> Assigned User Permissions administrator DC12NB\cuicu1 has Exec permission for Agents.Sales collection. When cuicu1 administrator is logged in and tries to run a report with Agent.Sales collection - the collection is not available in the list.

## Solution

In order to troubleshoot the problem check the content of CUIC database for the relevant configuraiton.

Information about permissions assigned to specific users for specific collections is stored in cuiccollectionauth table.

Permissions legend:

- Value 3 is for Exec permission

- Value 7 is for Exec+Write permission

### Single Query

The method described here confirms that a user has permission to access a collection. This method does not confirm the otherwise: that the user has no privileges to access the collection.

Use this SQL query to check the permissions that are set in the database.

```
admin: run sql SELECT u.name user,c.name collection,ca.permissions FROM cuic_data:cuiccollectionauth ca \ INNER JOIN cuic_data:cuiccollection c ON c.id==ca.collectionid \ INNER JOIN cuic_data:cuicuser u ON u.id==ca.usergroupid \ WHERE u.name LIKE '%cuicu1%' user          collection permissions ============= ========== =========== DC12NB\cuicu1 Sales      3
```

Note : All four lines of the query in bold font must be entered to get the output. The backslash character is used for better query presentation.

The output gives information about all permissions assigned to a user cuicu1 for collections. In the example user cuicu1 has permission to Sales collection.

### Several Queries

In case there is a need to check consolidated permissions set on the user and the group level use these commands.

Check the collection identifier in the DB.

```
admin: run sql SELECT id,name FROM cuic_data:cuiccollection WHERE name LIKE '%Sales%' id                               name 
================================ ====== A518DD1B100001540000002D0A302F8E Sales
```

List all of the user or group identifiers that have access to this collection. Use collection id as a filter in the query.

```
admin: run sql SELECT * FROM cuic_data:cuiccollectionauth WHERE collectionid='A518DD1B100001540000002D0A302F8E' collectionid                     usergroupid                      permissions assignedby replicated 
================================ ================================ =========== ================================ ========== 
A518DD1B100001540000002D0A302F8E 1111111111111111111111111111AAAA 7           1111111111111111111111111111AAAA t 
A518DD1B100001540000002D0A302F8E 2222222222222222222222222222BBBB 3           1111111111111111111111111111AAAA t 
A518DD1B100001540000002D0A302F8E 3778904E1000015A000000060A302F8E 3           SecurityAdmin                    t
```

Get the list of users with permissions for the collection. Users ccmadmin and cuicu1 both can see this collection in the filters.

```
admin: run sql SELECT id,name FROM cuic_data:cuicuser WHERE id IN \ ('1111111111111111111111111111AAAA','2222222222222222222222222222BBBB','3778904E1000015A000000060A302F8E') id                               name 
================================ =========================== 1111111111111111111111111111AAAA CUIC\ccmadmin 3778904E1000015A000000060A302F8E DC12NB\cuicu1
```

Get the list of groups with permissions for the collection. All users that belong to Administrators group can see this collection in the filters.

```
admin: run sql SELECT id,name FROM cuic_data:cuicgroup WHERE id IN \ ('1111111111111111111111111111AAAA','2222222222222222222222222222BBBB','3778904E1000015A000000060A302F8E') id                               name 
================================ ================= 2222222222222222222222222222BBBB Administrators
```

If you have the same problem for folder, dashboard, report, report definition, value list or data source refer to these tables.

- cuiccategoryauth

- cuicdashboardauth

- cuicreportauth

- cuicreportdefinitionauth

- cuicvaluelistauth

- cuicdatasourceauth

- cuiccollectionauth

### Revision History

1.0

25-Oct-2017

Initial Release

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 25-Oct-2017 | Initial Release |