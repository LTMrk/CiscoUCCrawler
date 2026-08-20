---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-218104-configure-directory-connector-to-soft-de-html-4329b170a0
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/218104-configure-directory-connector-to-soft-de.html
retrieved_at: 2026-08-20T21:12:44.865803+00:00
---

Configure Directory Connector to Soft-Delete Users in Dry Run

# Configure Directory Connector to Soft-Delete Users in Dry Run

### Download Options

Updated: August 26, 2022

Document ID: 218104

Contents

## Contents

## Introduction

This document describes Directory Connector release 3.7.3 enhancement to display soft-delete users under Dry Run reports.

## Prerequisites

### Requirements

- Microsoft Windows Server 2003, 2008R2, 2012, 2012R2, 2016, 2019

- It is required to use version, at the minimum, Cisco Directory Connector 3.7.3000

### Components Used

- Microsoft Windows Server 2019

- Cisco Webex DIrectory Connector 3.7.3000

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

This article shows how to delete users from the Active Directory to flag them as soft-delete users and use the Dry Run report to directly delete them from the Webex Cloud in the next synchronization with Directory Connector. The Webex Administrator can now force deletion of users permanently in the next synchronization by selection of partial users or all users.

An Administrator can delete a user from the the Active Directory and the user is marked as soft-delete in Webex Cloud after the synchronization task is performed. By design, soft-delete users are hard deleted after 7 days. During the soft-delete period of 7 days, the Administrator is unable to add another new user with the same email address.

In the past, the Administrator who needed to hard delete the soft-delete user from the Webex Cloud opened a TAC Case to work with the Engineering team and then to add the new user via the synchronization task.

With this enhancement, the Webex Administrator can now force deletion of those users permanently in the next syncrhonization task by selection of partial users or all users without the need to engage Cisco TAC.

## Remove the User from Active Directory

In this example, the Active (Verified) user with UUID 108cf4e8-150c-4e60-8a92-594b9a25e65d is deleted.

### Open Active Directory Users and Computers

From the Windows Server, navigate to Server Manager > Local Serve r > TASKS > Active Directory Users and Computers .

Look up the desired user to delete from the specific Organizational Unit (OU), select the user, and click Delete at the Action bar.

Confirm the deletion task.

### Use PowerShell

You can remove user objects from an Active Directory domain with the PowerShell cmdlet.

```
Remove-ADUser
```

This cmdlet is a part of the ActiveDirectory Module for Windows PowerShell, which must be pre-installed and imported into the PowerShell session with the command:

```
Import-Module activedirectory
```

You can delete a user with the username in several ways, by selection of: distinguished name (DN), GUID, security identifier (SID), or SAM account name. To remove the user with the user logon name, run the command:

```
Remove-ADUser soft-deleteduser
```

A prompt appears that asks you to confirm the removal of the user object from the domain. To delete a user, press Y and press the Enter key.

To remove the AD user without confirmation prompt, add -Confirm:$False at the end of the command:

```
Remove-ADUser soft-deleteduser -Confirm:$False
```

The user was deleted successfully from Active Directory.

## Use Directory Connector to Update Webex Control Hub

### Perform a Synchronization Task to Change Synced User to Soft-Deleted User

From Cisco Directory Connector, perform a Dry Run task to verify the user was deleted.

From the generated Dry Run report, the user does not have Distinguished Name information, which means the user is no longer present in Active Directory 2 and is to be deleted from the Webex Cloud 3 in the next synchronization.

Run an Incremental Synchronization task to verify the user has changed to Inactive status from the Webex Control Hub.

```
2022-08-02 00:44:19,913 INFO sync-task-runner-1 com.cisco.codev.identity.dirsync.engine.handler.dirsync.DirSyncUtils.createSummaryLog [tracking: ] [org: 904cbfb5-0f49-4339-a40c-ad473ac7ab24] [domain: adds-vizcainovich.com] [user: ] [session: 3f5e36b2-bcc6-4dfb-bc0f-c7c4edb61388] [task: 867b27c4-4fb3-4eb3-9cfb-86c65c3cf84e] - Synchronization Summary StatusCode: SUCCESS Domain: adds-vizcainovich.com Incremental Synchronization: yes Start Time: 2022-08-02T00:44:09Z End Time: 2022-08-02T00:44:19Z Object Added: 0 Object Deleted: 1 Object Modified: 0 Warning Count: 1 Avatar Failure Count: 1 Failure Count: 0
```

### Perform a Synchronization Task to Trigger the Hard Delete of the User

From the Cisco Directory Connector, perform a Dry Run task to see the Soft-deleted Objects tab.

From the generated Dry Run report, the user is now in the Soft-deleted Objects tab.

To inmediatly delete the user, the Administrator can check the user and the user is hard-deleted in the next synchronization.

Run an Incremental Synchronization task to verify the user is successfully hard deleted from the Webex Cloud, which means the user is not present anymore in the Webex Control Hub.

```
2022-08-02 01:20:04,313 INFO sync-task-runner-5 com.cisco.codev.identity.dirsync.engine.handler.dirsync.DirSyncUtils.createSummaryLog [tracking: ] [org: 904cbfb5-0f49-4339-a40c-ad473ac7ab24] [domain: adds-vizcainovich.com] [user: ] [session: 2abf8994-0fa0-4f7d-a56c-3b306b6a70a1] [task: 0eb43a7b-82b4-49dc-87fc-007476722f80] - Synchronization Summary StatusCode: SUCCESS Domain: adds-vizcainovich.com Incremental Synchronization: yes Start Time: 2022-08-02T01:19:53Z End Time: 2022-08-02T01:20:04Z Object Added: 0 Object Deleted: 0 Object Modified: 0 Failure Count: 0
```

## References

Delete Users Permanently After Soft Delete

Directory Connector release notes - Announcements

### Revision History

1.0

26-Aug-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Aug-2022 | Initial Release |