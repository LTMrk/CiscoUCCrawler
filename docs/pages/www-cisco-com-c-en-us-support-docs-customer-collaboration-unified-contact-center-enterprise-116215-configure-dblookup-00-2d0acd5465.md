---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-enterprise-116215-configure-dblookup-00-2d0acd5465
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-enterprise/116215-configure-dblookup-00.html
retrieved_at: 2026-08-21T04:22:07.058284+00:00
---

ICM DBLookup Function Configuration Example

# ICM DBLookup Function Configuration Example

Updated: April 13, 2017

Document ID: 116215

Contents

## Contents

## Introduction

This document describes how to configure the DBLookup function in the Intelligent Contact Manager (ICM) in order to fetch data from an external database and use it in the script. In order to illustrate how to configure the function, this document uses an example scenario where the user tries to identify if the caller is part of a list (for example, in order to provide priority service).

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Next, create a table in this database. Right-click Tables under the newly-created database. Then, you can add a few columns:

Note : Define all integer fields in tables accessed by a DBLookup node as NOT NULL. Only these data types are supported for SQL databases: SQLINT1 (tinyint), SQLINT2 (smallint), SQLINT4 (int), SQLCHAR (char), SQLVARCHAR (varchar), SQLFLT4DBFLT4 (real), SQLFLT8DBFLT8 (float), and SQLDATETIME (datetime). You must define all fields except SQLDATETIME, SQLVARCHAR, and SQLCHAR as NOT NULL fields. You can define these three fields as NULL.

Choose the varchar data type because it allows the flexibility to also have characters in the number. In order to set the Phone column as the primary key, uncheck Allow Nulls in the check box. In order to set this column as the primary key, right-click and choose Set Primary Key :

Once these steps are complete, save the changes. Now, you can add data to your table:

You also need to configure the username/password in order to log in to the database because the system uses sa with an empty password by default. Configure the username/password in the registry with this key:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\inst1\RouterA\Router\CurrentVersion\Configuration\Database\SQLLogin
```

This example shows how you can configure the key with the domain user:

```
\\POD2SPRAWLA\DBLookup=(ZFB\Administrator,password)
```

Note : Do not use the following special characters in the password: " = ", " ) ", " ( ", " , ", " ? ", " \ ", " / "

Ensure that you choose Enable Database Routing on the Edit Router screen, which can be accessed in the router setup on the web interface:

The lookup occurs on the column which is set as primary key. Later, you can use data from the same row to populate call variables. This example shows the addition of another column, City, both in the database and in the configuration manager, which can be populated in the script:

## Verify

Use this section to confirm that DB Worker is able to connect to the external database. Create a txt file dbw.txt that contains the logs since the last restart of the DB Worker process:

```
C:\Users\Administrator.ZFB> cdlog <instance_name> ra C:\icm\inst1\ra\logfiles> dumplog dbw /o /ms /last
```

Verify that DB Worker is able to connect to the database with dbw.txt :

```
12:39:08:413 ra-dbw Trace: Attempting integrated security open of POD2SPRAWLA using ZFB\Administrator 
12:39:08:451 ra-dbw Trace: Sucessfully impersonated ZFB\Administrator 
12:39:08:476 ra-dbw Trace: 'id' is column 2 in sysobjects. 
12:39:08:477 ra-dbw Trace: ID for table Priority is 5575058 
12:39:08:484 ra-dbw Trace: Columns for Priority: 
12:39:08:484 ra-dbw Trace: Column 1: Phone, type=47, length=30 
12:39:08:536 ra-dbw Trace: Primary key for Priority is Phone, column 1. 
12:39:08:557 ra-dbw Trace: Created connection to POD2SPRAWLA,DBLookup for thread 0 
12:39:08:557 ra-dbw Trace: Created connection to POD2SPRAWLA,DBLookup for thread 1 
12:39:08:558 ra-dbw Trace: Created connection to POD2SPRAWLA,DBLookup for thread 2 
12:39:08:558 ra-dbw Trace: Created connection to POD2SPRAWLA,DBLookup for thread 3 
12:39:08:558 ra-dbw Trace: Created connection to POD2SPRAWLA,DBLookup for thread 4 
12:39:08:558 ra-dbw Trace: ScriptTable Piority is now available. 
12:39:08:559 ra-dbw Trace: ScriptTable Piority (ID 5000) connected to POD2SPRAWLA,DBLookup,Priority 
12:39:08:559 ra-dbw Trace: Internal connect for POD2SPRAWLA,DBLookup,Priority 
12:39:08:559 ra-dbw Trace: 'id' is column 2 in sysobjects. 
12:39:08:560 ra-dbw Trace: ID for table Priority is 5575058 
12:39:08:560 ra-dbw Trace: Columns for Priority: 
12:39:08:560 ra-dbw Trace: Column 1: Phone, type=47, length=30 
12:39:08:561 ra-dbw Trace: Primary key for Priority is Phone, column 1. 
12:39:08:561 ra-dbw Trace: Column Phone (ID 5002) is table column 1, type 47. 
12:39:08:561 ra-dbw Trace: ScriptTable Piority (ID 5000) connected to POD2SPRAWLA,DBLookup,Priority
```

The DB Worker logs display this response when there is no entry that matches in the primary key column (triggered by DBLookup node in the script):

```
13:24:05:294 ra-dbw Trace: Queue a lookup request 13:24:05:295 ra-dbw Trace: DBWorker Thread 0 (ID 350760 Table:Priority): Received request: transactionID 1 13:24:05:295 ra-dbw Trace: DBWorker Thread 0 (ID 350760),transactionID 1, Attempt to read the record: 13:24:05:295 ra-dbw Trace: DBWorker transactionID 1, Failed! result=1
```

When there is a match, this is the response:

```
13:25:25:810 ra-dbw Trace: Queue a lookup request 13:25:25:810 ra-dbw Trace: DBWorker Thread 1 (ID 354428 Table:Piority): Received request: transactionID 2 13:25:25:810 ra-dbw Trace: DBWorker Thread 1 (ID 354428),transactionID 2, Attempt to read the record: 13:25:25:811 ra-dbw Trace: DBWorker Thread 1 (ID 354428),transactionID 2, Succeeded.
```

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

27-May-2013

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-May-2013 | Initial Release |