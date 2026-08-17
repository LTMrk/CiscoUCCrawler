---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-118299-technote-cuc-00-html-72f02bad33
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/118299-technote-cuc-00.html
retrieved_at: 2026-08-17T03:56:50.625555+00:00
---

CUC SQL Queries for Message Counts and Mailbox Sizes

# CUC SQL Queries for Message Counts and Mailbox Sizes

Updated: December 8, 2014

Document ID: 118299

Contents

## Contents

## Introduction

This document describes how to obtain the message count and size of a user mailbox with Structured Query Language (SQL) queries via the CLI. This data can also be retrieved with the User Data Dump tool, from the Cisco Unified Communications Tools page.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unity Connection (CUC).

### Components Used

The information in this document is based on CUC Versions 8.X and later, but this information might work for earlier versions as well.

## Databases

The SQL queries are formed with the data from these databases:

- UnityDirDB - This database contains the user-related information.

- UnityMbxDB1 - This database contains the user mailbox information.

## Tables

The SQL queries are formed with the data in these views. A view is a table that is either a combination of two or more tables, or the same data in a single table.

These views are used in the UnityDirDB database:

- vw_mailbox - This view contains the mapping between the user and mailbox.

- vw_user - This view contains the user-related information.

These views are used in the UnityMbxDB1 database:

- vw_message - This view contains a message item in the system. This table is merely a holder of message properties.

- vw_mailbox - This view contains a mailbox on the system that holds inbound messages. This table contains general information about the individual mailbox, to include the way in which messages are stored in the mailbox.

## SQL Queries

This section describes the various SQL queries that you can use in CUC.

### List the Total Messages Count with a Known Alias

Enter this command in order to obtain a list of the total messages count with a known alias:

```
admin: run cuc dbquery unitymbxdb1 select count (*) as Messages from vw_message, unitydirdb:vw_mailbox, unitydirdb:vw_user where mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb:vw_user.objectid = unitydirdb: vw_mailbox.userobjectid and alias='Anirudh') messages -------- 3
```

This query is a high-complexity, double-database query that involves multiple tables. For servers with a very large database and mailbox size, an extended period of time might elapse before an output appears, even over an hour, which is not ideal. In such scenarios, you can use this query instead:

```
admin: run cuc dbquery unitymbxdb1 select count (*) as Messages from vw_message where mailboxobjectid in (select mailboxobjectid from vw_mailbox where description='Anirudh') messages -------- 3
```

The first query returns the data when alias is mentioned, which is Unique . The second query returns the data when description is mentioned, which is NOT Unique .

Note : When the mailbox is created, the description is the same as the alias; however, when the alias is updated, the description is not updated. For small databases, the first query is ideal. In order to demonstrate that the description is not changed after the alias is altered, test3 is modified to Atest3 and used for the next sections.

### List Users with Total Messages Count

Enter this command in order to obtain a list of users with the total messages count:

```
admin: run cuc dbquery unitymbxdb1 select alias as UserID, count (*) as messages from vw_message, unitydirdb:vw_mailbox, unitydirdb:vw_user where mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb: vw_user.objectid = unitydirdb:vw_mailbox.userobjectid) group by alias order by messages desc userid                        messages ----------------------------  -------- Anirudh                       3 Atest3                        2 undeliverablemessagesmailbox  1
```

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, count (*) as Messages from vw_message, vw_mailbox where vw_mailbox.mailboxobjectid = vw_message.mailboxobjectid group by description order by messages desc description                   messages ----------------------------  -------- Anirudh                       3 test3                         2 undeliverablemessagesmailbox  1
```

Note : In the second query, the description does not change from test3 to Atest3 after the alias is changed.

### List Users with Total Messages Count Based on First Character in Alias

Enter this command in order to obtain a list of users with the total messages count based on the first character of an alias:

```
admin: run cuc dbquery unitymbxdb1 select alias as UserID, count (*) as messages from vw_message, unitydirdb:vw_mailbox, unitydirdb:vw_user where deleted='0' and mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb: vw_user.objectid = unitydirdb:vw_mailbox.userobjectid) and alias like 'A%' group by alias order by messages userid   messages -------  -------- Atest3   2 Anirudh  3
```

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, count (*) as Messages from vw_message, vw_mailbox where vw_mailbox.mailboxobjectid = vw_message.mailboxobjectid and description like 'A%' group by description order by messages
```

Here are some important notes about this query:

- The A% sets the query to hit aliases that begin with the letter A.

- The format is where columnname like 'condition' . Here, the column name is alias for the first query and description for the second query.

Here are some example conditions:

- _n% - The first letter can be any character (a wildcard), followed by the letter n and any number of characters.

- %s - This sets the query to hit aliases that end with the letter s .

The queries that are mentioned thus far are used in order to obtain the total messages (inbox and deleted items). The next section describes queries that are used in order to obtain the total number of messages in the inbox and deleted items.

### List Users with Total Inbox Messages

Enter this command in order to obtain a list of users with the total inbox messages:

```
admin: run cuc dbquery unitymbxdb1 select alias as UserID, count (*) as inboxmessages from vw_message, unitydirdb:vw_mailbox, unitydirdb:vw_user where deleted='0' and mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb:vw_user.objectid = unitydirdb:vw_mailbox.userobjectid) and alias like 'A%' group by alias order by inboxmessages userid   inboxmessages -------  ------------- Atest3   2 Anirudh  3
```

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, count (*) as InboxMessages from vw_message, vw_mailbox where vw_mailbox.mailboxobjectid = vw_message.mailboxobjectid and deleted = '0' and description like 'A%' group by description order by InboxMessages
```

Here are some important notes about this query:

- The A% sets the query to hit aliases that begin with the letter A.

- The format is where columnname like 'condition' . Here, the column name is alias for the first query and description for the second query.

Here are some example conditions:

- _n% - The first letter can be any character (a wildcard), followed by the letter n and any number of characters.

- %s - This sets the query to hit aliases that end with the letter s .

Note : In this example, a condition is used in order to limit users with an alias/description that begins with the letter A .

These are some variations of this query:

- In order to list all users, remove and alias like 'A%' in the first query, or and description like 'A%' in the second query.

- In order to list a particular user (list the count for Anirudh's mailbox, for example), replace and alias like 'A%' with and alias='Anirudh' in the first query, or replace and description like 'A%' with and description ='Anirudh' in the second query. Ensure that the replacement is in the exact position, or the query fails.

### List Users with Total Deleted Messages

Enter this command in order to obtain a list of users with the total deleted messages:

```
admin: run cuc dbquery unitymbxdb1 select alias as UserID, count (*) as deletedmessages from vw_message, unitydirdb:vw_mailbox, unitydirdb:vw_user where deleted='1' and mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb:vw_user.objectid = unitydirdb:vw_mailbox.userobjectid) and alias like 'A%' group by alias order by deletedmessages No records found
```

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, count (*) as deletedmessages from vw_message, vw_mailbox where vw_mailbox.mailboxobjectid= vw_message.mailboxobjectid and deleted = '1' and description like 'A%' group by description order by deletedmessages
```

Note : In this example there are no deleted messages, so the output appears as No records found .

Here are some important notes about this query:

- The A% sets the query to hit aliases that begin with the letter A.

- The format is where columnname like 'condition' . Here, the column name is alias for the first query and description for the second query.

Here are some example conditions:

- _n% - The first letter can be any character (a wildcard), followed by the letter n and any number of characters.

- %s - This sets the query to hit aliases that end with the letter s .

Note : In this example, a condition is used in order to limit users with an alias/description that begins with the letter A .

These are some variations of this query:

- In order to list all users, remove and alias like 'A%' in the first query, or and description like 'A%' in the second query.

- In order to list a particular user (list the count for Anirudh's mailbox, for example), replace and alias like 'A%' with and alias='Anirudh' in the first query, or replace and description like 'A%' with and description ='Anirudh' in the second query. Ensure that the replacement is in the exact position, or the query fails.

### List Users with Total, Inbox, and Deleted Messages

Enter this command in order to obtain a list of users with the total, inbox, and deleted messages:

```
admin: run cuc dbquery unitymbxdb1 select alias as UserID, count (*) as messages, sum(case when deleted='0' then 1 else 0 end) as Inboxmessages, sum(case when deleted='1' then 1 else 0 end) as Deletedmessages from vw_message, unitydirdb: vw_mailbox, unitydirdb:vw_user where mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb:vw_user.objectid = unitydirdb:vw_mailbox.userobjectid) group by alias order by messages desc userid                        messages  inboxmessages  deletedmessages ----------------------------  --------  -------------  --------------- Anirudh                       3         3              0 Atest3                        2         2              0 undeliverablemessagesmailbox  1         1              0
```

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description as UserID, count (*) as messages, sum(case when deleted='0' then 1 else 0 end) as Inboxmessages, sum (case when deleted='1' then 1 else 0 end) as Deletedmessages  from vw_mailbox join vw_message on vw_message.mailboxobjectid=vw_mailbox.mailboxobjectid group by description order by messages desc
```

Here are some important notes about this query:

- The A% sets the query to hit aliases that begin with the letter A.

- The format is where columnname like 'condition' . Here, the column name is alias for the first query and description for the second query.

Here are some example conditions:

- _n% - The first letter can be any character (a wildcard), followed by the letter n and any number of characters.

- %s - This sets the query to hit aliases that end with the letter s .

Note : In this example, a condition is used in order to limit users with an alias/description that begins with the letter A .

These are some variations of this query:

- In order to list all users, remove and alias like 'A%' in the first query, or and description like 'A%' in the second query.

- In order to list a particular user (list the count for Anirudh's mailbox, for example), replace and alias like 'A%' with and alias='Anirudh' in the first query, or replace and description like 'A%' with and description ='Anirudh' in the second query. Ensure that the replacement is in the exact position, or the query fails.

### List User Message Count with Oldest Message Arrival Time

This query can be used in order to determine whether the scheduled jobs for mailboxe cleanup take effect:

```
admin: run cuc dbquery unitymbxdb1 select alias as UserID, count (*) as messages, min(arrivaltime) as OldestMessageTime from vw_message, unitydirdb:vw_mailbox, unitydirdb:vw_user where mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb:vw_user.objectid = unitydirdb:vw_mailbox.userobjectid) group by alias order by messages desc userid                        messages  oldestmessagetime ----------------------------  --------  ----------------------- Anirudh                       3         2013-03-19 14:38:14.459 Atest3                        2         2013-01-18 05:49:45.355 undeliverablemessagesmailbox  1         2012-07-05 01:10:19.961
```

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, count (*) as Messages, min(arrivaltime) as OldestMessageTime from vw_message, vw_mailbox where vw_mailbox.mailboxobjectid = vw_message.mailboxobjectid group by description order by messages desc
```

Note : In order to obtain the Last Arrival Time for the queries in the previous sections, add min(arrivaltime) as OldestMessageTime just after count(*) as Messages.

These are some variations of this query:

- In order to list all users with aliases that begin with the letter A, add and alias like 'A%' in the first query just before the group by alias condition, or and description like 'A%' in the second query just before the group by description condition. Ensure that the replacement is in the exact position, or the query fails.

- In order to list a particular user (list the count for Anirudh's mailbox, for example), add and alias='Anirudh' in the first query just before the group by alias condition, or and description ='Anirudh' in the second query just before the group by description condition. Ensure that the replacement is in the exact position, or the query fails.

### List User Message Count with Oldest Message Arrival Time and Mailbox Size / Total Duration

Enter this command in order to obtain a list of the user message count with the oldest message's arrival time and the mailbox size (without Total Duration):

```
admin: run cuc dbquery unitymbxdb1 select alias as UserID, count (*) as messages, min(arrivaltime) as OldestMessageTime, vw_mailbox.bytesize from vw_message, vw_mailbox, unitydirdb:vw_mailbox, unitydirdb:vw_user where vw_message.mailboxobjectid=vw_mailbox.mailboxobjectid and vw_mailbox.mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb:vw_user.objectid = unitydirdb:vw_mailbox.userobjectid) group by alias, vw_mailbox.bytesize order by messages desc userid                        messages  oldestmessagetime        bytesize ----------------------------  --------  -----------------------  -------- Anirudh                       3         2013-03-19 14:38:14.459  93319 Atest3                        2         2013-01-18 05:49:45.355  59890 undeliverablemessagesmailbox  1         2012-07-05 01:10:19.961  317003
```

Note : To get the total duration of messages: add " , sum(duration/1000) as TotalDuration_In_sec" just before " from vw_message". Do not forget the comma before sum. This can also be used for the queries in the previous sections.

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, count (*) as Messages, min(arrivaltime) as OldestMessageTime, vw_mailbox.bytesize from vw_message, vw_mailbox where vw_mailbox.mailboxobjectid = vw_message.mailboxobjectid group by description, vw_mailbox.bytesize order by messages desc
```

Note : In order t o get the total duration of messages: add " , sum(duration/1000) as TotalDuration_In_sec" just before " from vw_message". Do not forget the comma before sum. This can also be used for the queries in the previous sections.

These are some variations of this query:

- In order to list all users with aliases that begin with the letter A, add and alias like 'A%' in the first query just before the group by alias condition, or and description like 'A%' in the second query just before the group by description condition. Ensure that the replacement is in the exact position, or the query fails.

- In order to list a particular user (list the count for Anirudh's mailbox, for example), add and alias='Anirudh' in the first query just before the group by alias condition, or and description ='Anirudh' in the second query just before the group by description condition. Ensure that the replacement is in the exact position, or the query fails.

### List User Inbox and Deleted Messages Count with Oldest Message Arrival Time and Mailbox Size / Total Duration

Enter this command in order to obtain a list of the user inbox and deleted messages count with the oldest message's arrival time and the mailbox size (without Total Duration) :

```
admin: run cuc dbquery unitymbxdb1 select alias as UserID, count (*) as TotalMessages, sum(case when deleted='0' then 1 else 0 end) as Inbox, sum(case when deleted='1' then 1 else 0 end) as Deleted,  min (arrivaltime) as OldestMessageTime, vw_mailbox.bytesize from vw_message, vw_mailbox, unitydirdb:vw_mailbox, unitydirdb:vw_user where vw_message.mailboxobjectid=vw_mailbox.mailboxobjectid and vw_mailbox.mailboxobjectid in (select mailboxid from vw_mailbox where unitydirdb:vw_user.objectid = unitydirdb:vw_mailbox.userobjectid) group by alias, vw_mailbox.bytesize order by TotalMessages desc userid            total     inbox  deleted  oldestmessagetime        byte messages                                           size ----------------  --------  -----  -------  -----------------------  ------ Anirudh           3         3      0        2013-03-19 14:38:14.459  93319 Atest3            2         2      0        2013-01-18 05:49:45.355  59890 undeliverable     1         1      0        2012-07-05 01:10:19.961  317003 messagesmailbox
```

Note : In order to get the total duration of messages: add " , sum(duration/1000) as TotalDuration_In_sec" just before " from vw_message". Do not forget the comma before sum. This can also be used for the queries in the previous sections.

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, count (*) as TotalMessages, sum(case when deleted='0' then 1 else 0 end) as Inbox, sum(case when deleted='1' then 1 else 0 end) as Deleted, min(arrivaltime) as OldestMessageTime, vw_mailbox.bytesize from vw_message, vw_mailbox where vw_mailbox.mailboxobjectid = vw_message.mailboxobjectid group by description, vw_mailbox.bytesize order by TotalMessages desc
```

Note : To get the total duration of messages: add " , sum(duration/1000) as TotalDuration_In_sec" just before " from vw_message". Do not forget the comma before sum. This can also be used for the queries in the previous sections.

These are some variations of this query:

- In order to list all users with aliases that begin with the letter A, add and alias like 'A%' in the first query just before the group by alias condition, or and description like 'A%' in the second query just before the group by description condition. Ensure that the replacement is in the exact position, or the query fails.

- In order to list a particular user (list the count for Anirudh's mailbox, for example), add and alias='Anirudh' in the first query just before the group by alias condition, or and description ='Anirudh' in the second query just before the group by description condition. Ensure that the replacement is in the exact position, or the query fails.

### List the Total Number of Messages for All Mailboxes

Enter this command in order to obtain the total number of messages for all of the mailboxes combined:

```
admin: run cuc dbquery unitymbxdb1 select count(*) as messages from vw_message messages ---------- 6
```

### List a User Mailbox Size with Send and Receive Limits

Enter this command in order to obtain the user mailbox size with send and receive limits:

```
admin: run cuc dbquery unitydirdb select alias as UserID,bytesize,send,receive, warning from vw_user,unitymbxdb1:vw_mailbox where vw_user.objectid in (select userobjectid from vw_usermailboxmap where vw_usermailboxmap.mailboxid=unitymbxdb1:vw_mailbox.mailboxobjectid and alias='Anirudh') userid   bytesize  send      receive   warning -------  --------  --------  --------  -------- Anirudh  93319     13000000  14745600  12000000
```

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, bytesize,send,receive, warning from vw_mailbox where description ='Anirudh'
```

### List All User Mailbox Sizes with Send and Receive Limits

Enter this command in order to obtain all of the the user mailbox sizes with send and receive limits:

```
admin: run cuc dbquery unitydirdb select alias as UserID,bytesize,send,receive, warning from vw_user,unitymbxdb1:vw_mailbox where vw_user.objectid in (select userobjectid from vw_usermailboxmap where vw_usermailboxmap.mailboxid=unitymbxdb1:vw_mailbox.mailboxobjectid) order by bytesize desc userid                        bytesize  send      receive   warning ----------------------------  --------  --------  --------  -------- undeliverablemessagesmailbox  317003    13000000  14745600  12000000 Anirudh                       93319     13000000  14745600  12000000 Atest3                        59890     13000000  14745600  12000000 Solomon                       0         13000000  14745600  12000000 UnityConnection               0         50000000  50000000  45000000 Suvir                         0         13000000  14745600  12000000 dsas                          0         13000000  14745600  12000000 test1                         0         13000000  14745600  12000000 Atest2                        0         13000000  14745600  12000000 operator                      0         13000000  14745600  12000000
```

For the same reasons that are mentioned in the List the Total Messages Count with a Known Alias section, this query can also be used:

```
admin: run cuc dbquery unitymbxdb1 select description, bytesize,send,receive, warning from vw_mailbox order by bytesize desc
```

As a variation of this query in order to list all of the users with aliases that begin with the letter A , add and alias like 'A%' in the first query just after the vw_usermailboxmap.mailboxid=unitymbxdb1:vw_mailbox.mailboxobjectid and before ) order by condition, or you can add where description like 'A%' in the second query just before the order by condition. Ensure that this is added in the correct position, or the query fails.

### List the Total Size of All Mailboxes Combined

Enter this command in order to obtain the total size of all mailboxes combined:

```
admin: run cuc dbquery unitymbxdb1 select sum (bytesize) from vw_mailbox (sum) ------- 2683210 admin:
```

### Revision History

1.0

20-Aug-2014

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 20-Aug-2014 | Initial Release |