---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-211608-troubleshoot-cuic-user-coll-112488d72a
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/211608-Troubleshoot-CUIC-User-Collection-Permis.html
retrieved_at: 2026-08-16T19:25:34.374714+00:00
---

Troubleshoot CUIC User Collection Permissions

# Troubleshoot CUIC User Collection Permissions

Updated: August 17, 2017

Document ID: 211608

Contents

## Contents

## Introduction

This document describes troubleshoot process for user permissions in Cisco Unified Intelligence Center (CUIC) server.

## CUIC User Collection Permissions

A typical CUIC issue is that a particular user cannot see collections or value lists to which the user has permissions.

### Check Permissions in CUIC Web Page

In this example, a user cuicu1 has execute permission for Tech collection. Check the permissions configured for the user.

The same user cuicu1 belongs to a group admin_custom that has permission to Sales collection.

As a result, when the user runs a report there are two collections available in the list: Sales and Tech .

### Check Permissions in CUIC Database

The same information can be verified from the database.

Step 1. Get user groups.

```
admin: run sql SELECT gm.memberid,u.name,gm.groupid,g.name FROM cuic_data:cuicgroupmember gm \ INNER JOIN cuic_data:cuicuser u ON u.id==gm.memberid INNER JOIN cuic_data:cuicgroup g ON g.id==gm.groupid WHERE u.name LIKE '%cuicu1%' memberid name groupid name ================================ ==================== ================================ ============ F7DB93871000015C0000001E0A302F8E ADMINISTRATOR\cuicu1 2222222222222222222222222222AAAA AllUsers F7DB93871000015C0000001E0A302F8E ADMINISTRATOR\cuicu1 7CA0F8121000015C000003DE0A302F8E admin_custom
```

The combined permissions list for this user is consists of three entires: 1st for the user itself, 2nd and 3rd for the group the user admin_custom belongs to. These values are used in the next queries.

```
F7DB93871000015C0000001E0A302F8E, 2222222222222222222222222222AAAA, 7CA0F8121000015C000003DE0A302F8E
```

Step 2. Get all permissions for this user and his groups for the collections.

```
admin: run sql SELECT ca.usergroupid user_or_groupid,ca.collectionid,c.name collection FROM cuic_data:cuiccollectionauth ca \ INNER JOIN cuic_data:cuiccollection c ON c.id==ca.collectionid \ WHERE ca.usergroupid IN ('F7DB93871000015C0000001E0A302F8E','2222222222222222222222222222AAAA','7CA0F8121000015C000003DE0A302F8E') user_or_groupid                  collectionid                     collection ================================ ================================ ========== F7DB93871000015C0000001E0A302F8E EA6464501000015D0000007A0A302F8E Tech 7CA0F8121000015C000003DE0A302F8E EA6420C11000015D000000750A302F8E Sales
```

The list of collections from the output in the step 2 should match the list the user can see in the CUIC web page. Also the output from the database must be the same on all of the nodes in CUIC cluster.

In case an inconsistency in permissions is found please contact Cisco TAC support.

### Revision History

1.0

17-Aug-2017

Initial Release

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Aug-2017 | Initial Release |