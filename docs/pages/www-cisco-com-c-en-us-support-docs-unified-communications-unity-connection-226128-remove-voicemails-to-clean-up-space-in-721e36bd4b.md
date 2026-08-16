---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-226128-remove-voicemails-to-clean-up-space-in-721e36bd4b
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/226128-remove-voicemails-to-clean-up-space-in.html
retrieved_at: 2026-08-16T18:57:15.107551+00:00
---

Remove Voicemails to Clean Up Space in Unity Connection

# Remove Voicemails to Clean Up Space in Unity Connection

### Download Options

Updated: July 3, 2026

Document ID: 226128

Contents

## Contents

## Introduction

This document describes how to remove voicemails from the mailboxes that are using the most space in Cisco Unity Connection.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of this topic:

- Cisco Unity Connection (CUC)

### Components Used

- Cisco Unity Connection (CUC) CLI

The information in this document was created from the devices in a specific lab environment. All the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Troubleshooting

These steps are especially important when the CUC server shows error “The Current Size of the 'Mailbox Store' has exceeded the Maximum Size.”. To solve this, do these steps:

- Open the CUC Publisher CLI .

- Locate the mailboxes which are using the most space:

```
run cuc dbquery unitymbxdb1 select first 10 bytesize,description from vw_mailbox order by bytesize desc
```

3. Mark as Deleted the voicemails from the largest mailbox:

Note : Replace USERID with the actual mailbox username.

```
run cuc dbquery unitymbxdb1 update tbl_FolderItem set deleted = 1 where folderobjectid = (select folderobjectid from tbl_folder where mailboxobjectid= (select mailboxobjectid from vw_mailbox where description='USERID'))
```

Else, mark as Deleted the voicemails from the largest mailbox within a date range:

Note : Replace USERID with the actual mailbox username and replace the desired dates.

```
run cuc dbquery UnityMbxDb1 "update tbl_FolderItem set deleted = '1' where folderobjectid = (select folderobjectid from tbl_folder where mailboxobjectid = (select mailboxobjectid from vw_mailbox where description='USERID') and arrivaltime between '2018-03-20 06:00:00' and '2020-01-01 06:00:00')"
```

4. Delete the voicemails marked as Deleted from the largest mailbox:

Note : Replace USERID with the actual mailbox username.

```
run cuc dbquery unitymbxdb1 execute procedure csp_FolderPurge (pfolderobjectid = (select folderobjectid from tbl_folder where mailboxobjectid= (select mailboxobjectid from vw_mailbox where description='USERID')))
```

5. Refresh the folders count:

```
run cuc dbquery unitymbxdb1 execute procedure csp_FoldersRefreshCounts()
```

Repeat these steps as many times as needed, depending on the space you need to clean up.

Once the voicemails have been deleted, wait for 30 minutes. If the issue persists, reboot the CUC server to ensure the voicemails are completely deleted.

### Revision History

1.0

08-Jul-2026

Initial Release

### Contributed by Cisco Engineers

Yani Saavedra Chimal

Technical Consulting Engineer

### This Document Applies to These Products

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 08-Jul-2026 | Initial Release |