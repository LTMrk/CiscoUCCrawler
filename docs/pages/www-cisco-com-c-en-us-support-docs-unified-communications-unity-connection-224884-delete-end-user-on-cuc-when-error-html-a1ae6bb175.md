---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-224884-delete-end-user-on-cuc-when-error-html-a1ae6bb175
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/224884-delete-end-user-on-cuc-when-error.html
retrieved_at: 2026-08-16T18:57:31.309236+00:00
---

Delete End User on CUC when Error "Object not found User" is Seen

# Delete End User on CUC when Error "Object not found User" is Seen

### Download Options

Updated: September 11, 2025

Document ID: 224884

Contents

## Contents

## Introduction

This document describes how to delete an end user from the Cisco Unity Connection (CUC) Web GUI when the error "Object not found User" is prompted.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unity Connection (CUC)

- Structured Query Language (SQL)

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

There are instances when you are required to delete an end user from the CUC Administration page, and the error "Object not found User" is displayed without the possibility of deleting it.

## Solution 1

Step 1. Navigate to the Primary CUC via CLI. Log in there and run the command: run cuc dbquery unitydirdb SELECT objectId, dtmfaccessid from vw_User WHERE alias = "user_alias"

This command gets you the object identifier associated to the end user.

Note : Keep in mind that the SQL query is case sensitive.

```
admin: run cuc dbquery unitydirdb SELECT objectId, dtmfaccessid from vw_User WHERE alias = "Lusky" objectid                                    dtmfaccessid ------------------------------------        ------------ 644d3092-ed63-4694-a2ad-e0a5d2c8ad63        803103
```

Step 2 . Proceed with the execution of the delete statement, with the command: run cuc dbquery unitydirdb execute procedure csp_userdelete(pobjectid= "ObjectID_from_first_command" )

This command can be executed successfully with the message rows: 1 or with an error.

Once done, return to the CUC Administration > Users > Users page and confirm that the user has been deleted, if not, try delete it again from the GUI page.

However, if the issue persists, and the end user is unable to be deleted or the command throws an error, proceed with the troubleshooting steps.

## Solution 2

Step 1. Validate if there are call handlers associated to the use with the command: run cuc dbquery unitydirdb select objectid, displayname from vw_callhandler where recipient_subscriberobjectid = "ObjectID_from_first_command"

Step 2 . Delete the reference with the command: run cuc dbquery unitydirdb EXECUTE PROCEDURE csp_callhandlerDelete (pObjectId = "ObjectId_from_the_previous_step ")

Step 3 . Delete the user with the comamnd: run cuc dbquery unitydirdb EXECUTE PROCEDURE csp_UserDelete (pObjectId = "ObjectID_from_first_command" )

Return to the CUC Administration > Users > Users page and confirm that the user has been deleted, if not, try delete it again from the GUI page.

## Solution 3

```
admin:run cuc dbquery unitydirdb execute procedure csp_userdelete(pobjectid='644d3092-ed63-4694-a2ad-e0a5d2c8ad63') Key value for constraint (informix.pk_tbl_scheduleset) is still being referenced. Command failed
```

As seen in the output, the error displays that the user is referenced to the Schedules Tables.

Step 1. Run this SQL command to obtain the information from the Schedule Table: run cuc dbquery unitydirdb select displayname, objectid from vw_scheduleset where owner_subscriberobjectid =" ObjectID_from_first_command"

```
admin:run cuc dbquery unitydirdb select displayname, objectid from vw_scheduleset where owner_subscriberobjectid ='644d3092-ed63-4694-a2ad-e0a5d2c8ad63' displayname                                                    objectid -------------------------------------------------------------- ------------------------------------ Notification Schedule for 645b0777-d6f4-4f99-9d1c-62916e8f0bb5 e44b5344-0889-4f75-8a6f-778eab98988e
```

Step 2. With the new Object Identified from the Notification Schedule table, you can delete the reference between the user and the Notification Device Table. run cuc dbquery unitydirdb delete from tbl_notificationdevice where subscriberobjectid=" ObjectID_from_the_previous_command"

```
admin:run cuc dbquery unitydirdb delete from tbl_notificationdevice where subscriberobjectid='2a6ba228-cd2c-43fb-b43f-72ffb45b16b7' Rows: 5
```

Step 3. Validate that there are no cross-references with the user configuration. Run the command: run cuc dbquery unitydirdb select * from vw_subscriberreference where objectid IN (select objectid from vw_subscriber where alias = "user_alias")

```
admin:run cuc dbquery unitydirdb select * from vw_subscriberreference where objectid IN (select objectid from vw_subscriber where alias = "Lusky") objectid                               displayname referencetype referrerobjectid                      referrerobjecttype ------------------------------------   ----------- ------------- ------------------------------------  ------------------ 2a6ba228-cd2c-43fb-b43f-72ffb45b16b7   Lusky       Recipient     cbc63641-2eb6-4590-93a1-9bbdaeabbb63  3
```

Step 4. Validate that the user is not associated to any Call Handlers with the SQL query: run cuc dbquery unitydirdb select objectid from tbl_callaction where targethandlerobjectid IN (select callhandlerobjectid from vw_subscriber where fn_tolower(alias) = fn_tolower( "user_alias" ))

```
admin:run cuc dbquery unitydirdb select objectid from tbl_callaction where targethandlerobjectid IN (select callhandlerobjectid from vw_subscriber where fn_tolower(alias) = fn_tolower("Lusky")) No records found
```

Note : If records were found, delete the reference with the command run cuc dbquery unitydirdb delete from tbl_callaction where objectid=" ObjectID_from_the_previous_command"

Step 5. Validate that the user does not have any auto attendant entry from other extensions with the SQL query: run cuc dbquery unitydirdb select displayname from vw_callhandler where objectid = (select callhandlerobjectid from vw_menuentry where targethandlerobjectid IN (select callhandlerobjectid from vw_subscriber where fn_tolower(alias) = lower( "user_alias" )))

```
admin:run cuc dbquery unitydirdb select displayname from vw_callhandler where objectid = (select callhandlerobjectid from vw_menuentry where targethandlerobjectid IN (select callhandlerobjectid from vw_subscriber where fn_tolower(alias) = lower('Lusky'))) No records found
```

Note : If records were found, delete the reference with the command run cuc dbquery unitydirdb delete from vw_callhandler where objectid=" ObjectID_from_the_previous_command"

Step 6. Confirm that the user is part of the mailstore membership with the command: run cuc dbquery unitydirdb select alias,objectid,object_globaluserobjectid from tbl_alias where object_globaluserobjectid= "ObjectID_from_first_command"

```
admin:run cuc dbquery unitydirdb select alias,objectid,object_globaluserobjectid from tbl_alias where object_globaluserobjectid='813af2a0-fce7-42ad-ac4e-d150e769a26e' alias  objectid                              object_globaluserobjectid -----  ------------------------------------- ---------------------------------------- Lusky  96a1f758-432e-4b9e-ac89-daa0c06489ad  644d3092-ed63-4694-a2ad-e0a5d2c8ad63 Ansky  92eefd9-6ee0-4afc-9567-50726bf3b41f   644d3092-ed63-4694-a2ad-e0a5d2c8ad63
```

As seen, the same object identifier is assigned to two users. Therefore, proceed with the deletion of the second user, that has a different alias from the one you want to delete with the command: run cuc dbquery unitydirdb select objectid,dtmfaccessid from tbl_Globaluser where alias='second_user_alias'

admin: run cuc dbquery unitydirdb select objectid,dtmfaccessid from tbl_Globaluser where alias='2861'

rows: 1

Navigate back to the CUC Administration > Users > Users page and delete the user you wanted to delete from the web GUI.

### Revision History

1.0

11-Sep-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 11-Sep-2025 | Initial Release |