---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-200689-unity-connection-procedure-to-change-d-89baf59e9e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/200689-Unity-Connection-Procedure-to-change-De.html
retrieved_at: 2026-08-16T18:54:22.646050+00:00
---

Unity Connection: Procedure to change Default Application Admin User

# Unity Connection: Procedure to change Default Application Admin User

### Download Options

Updated: October 14, 2016

Document ID: 200689

Contents

## Contents

## Introduction

This document describes the procedure to change the default application administrator user in Cisco Unity Connection (CUC).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUC.

### Components Used

The information in this document is based on CUC 8.x and higher.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

Complete these steps in order to change the default application administrator user name:

Step 1. Retrieve the objectID of the default application administrator user from the Unity Connection database.

```
admin:run cuc dbquery unitydirdb select name, value from vw_configuration where name='DefaultAdministrator' 

name                  value
--------------------  ------------------------------------
DefaultAdministrator  03ae9d8a-ef39-4c32-91fc-efb414a2f75e
```

Step 2. Retrieve the alias associated with the default application administrator objectID.

```
admin:run cuc dbquery unitydirdb select alias,objectid from vw_user where objectid='03ae9d8a-ef39-4c32-91fc-efb414a2f75e'

alias  objectid
-----  ------------------------------------
admin  03ae9d8a-ef39-4c32-91fc-efb414a2f75e
```

Step 3. Update the read only flag of the default application administrator user in order to make it editable.

```
admin:run cuc dbquery unitydirdb update tbl_user set readonly='0' where objectid='03ae9d8a-ef39-4c32-91fc-efb414a2f75e'

Rows: 1
```

Step 4. Update the default application administrator user and smtpaddress(pmailname@domain) in the Unity Connection database. Choose a desired username. In this example, admin is updated to cucadmin.

```
admin:run cuc dbquery unitydirdb execute procedure csp_usermodify(pobjectid='03ae9d8a-ef39-4c32-91fc-efb414a2f75e',palias='cucadmin',pdisplayname='cucadmin',pmailname='cucadmin')

Rows: 0
```

Step 5. Retrieve the default application administrator name and pkid from the Cisco CallManager (CCM) database.

```
admin:run sql select name, pkid from applicationuser
name                pkid                                 
=================== ==================================== 
admin               06bae444-79f0-34bc-0b73-042e90ad941b 
CCMSysUser          ffd322cd-a1c9-48ce-b23f-6d9475e3547e 
WDSysUser           a3d8edb3-8dcd-4e70-a662-dc9afa7f81d3 
CCMQRTSysUser       a024f7be-4f36-4373-80dc-a45cb4b891b9 
IPMASysUser         d0b9ceb0-d752-46df-96b6-68d37aed70eb 
WDSecureSysUser     aaecf22c-ba36-4afd-a8b1-85fb4f02c04f 
CCMQRTSecureSysUser 3f2bd34b-c7a1-4b04-a6d4-f75c24c05782 
IPMASecureSysUser   bd18e867-2c47-4a60-8740-83c36f178e99 
TabSyncSysUser      826888c4-ef7b-48ea-99ba-a86de6c3b369 
CUCService          c06dd551-7d3a-4d85-bae9-c450ff03b151
```

Note : When a CUC server is rebuild with a new application administrator username and a Disaster Recovery System (DRS) restore is performed on the system, the CUC database is updated with the old username. However, the CCM database still has the new username.

Step 6. Update CCM database with the new application administrator user if the entry is different.

```
admin:run sql update applicationuser set name='cucadmin' where pkid='06bae444-79f0-34bc-0b73-042e90ad941b'
Rows: 1
```

Step 7. Change the application administrator user password.

```
admin:utils cuc reset password cucadmin

Enter password: 
Re-enter password: 

cucadmin
09/10/2016 07:46:00.012 : Update SUCCEEDED
```

Step 8. Confirm the encryptiontype is 4 for web authentication for the default application administrator user (Credentialtype 3 is for web application password).

```
admin:run cuc dbquery unitydirdb select credentialtype,credentials,encryptiontype,objectid from vw_credential where userobjectid='03ae9d8a-ef39-4c32-91fc-efb414a2f75e'

credentialtype  credentials                                                       encryptiontype  objectid
--------------  ----------------------------------------------------------------  --------------  ------------------------------------
3               06ab0cd9a8d8bcc1d7ff4999a2e42cbaebc0f5b2a4e87d27cca8b6dcfa351d73  4               6e871c82-e512-43f9-8134-211324ce2716
4               57346139caa53dab4f0eb08f18f70e20527e65fb                          3               f54833e7-8fc3-4e6e-8987-b12417f8d440
```

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

26-Sep-2016

Initial Release

### Contributed by Cisco Engineers

Anirudh Mavilakandy

Cisco TAC Engineer

Naman Saini

Cisco TAC Engineer

### This Document Applies to These Products

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Sep-2016 | Initial Release |